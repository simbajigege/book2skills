#!/usr/bin/env python3
"""
memory_audit.py — 诊断记忆文件健康状态

从 Claude Code 源码提取的验证逻辑：
- MAX_ENTRYPOINT_LINES = 200  (src/memdir/memdir.ts)
- MAX_ENTRYPOINT_BYTES = 25_000  (src/memdir/memdir.ts)
- FRONTMATTER_MAX_LINES = 30  (src/memdir/memoryScan.ts)
- MAX_MEMORY_FILES = 200  (src/memdir/memoryScan.ts)
- MEMORY_TYPES = ['user', 'feedback', 'project', 'reference']  (src/memdir/memoryTypes.ts)

用法：
    python memory_audit.py [memory_dir]
    python memory_audit.py ~/.claude/projects/<project>/memory/
    python memory_audit.py  # 自动查找当前项目记忆目录
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime

# --- 来自源码的常量 ---
MAX_ENTRYPOINT_LINES = 200
MAX_ENTRYPOINT_BYTES = 25_000
MAX_ENTRY_LINE_CHARS = 150   # 每行指针的推荐上限
FRONTMATTER_MAX_LINES = 30   # 源码中 memoryScan.ts 读取的前 N 行
MAX_MEMORY_FILES = 200
MEMORY_TYPES = {'user', 'feedback', 'project', 'reference'}
ENTRYPOINT_NAME = 'MEMORY.md'


def find_memory_dir() -> Path | None:
    """尝试查找当前项目的记忆目录"""
    # 从当前目录向上找 git root
    cwd = Path.cwd()
    root = cwd
    for parent in [cwd, *cwd.parents]:
        if (parent / '.git').exists():
            root = parent
            break

    # sanitize: 将 git root 路径转换为 Claude Code 存储格式
    # ~/.claude/projects/<sanitized-path>/memory/
    sanitized = str(root).replace('/', '-').replace('\\', '-').replace(':', '-').lstrip('-')
    candidate = Path.home() / '.claude' / 'projects' / sanitized / 'memory'
    if candidate.exists():
        return candidate

    # 也检查 ~/.claude/memory/
    global_mem = Path.home() / '.claude' / 'memory'
    if global_mem.exists():
        return global_mem

    return None


def parse_frontmatter(content: str) -> dict:
    """从 Markdown 文件提取 YAML frontmatter"""
    lines = content.split('\n')[:FRONTMATTER_MAX_LINES]
    if not lines or lines[0].strip() != '---':
        return {}
    fm = {}
    for line in lines[1:]:
        if line.strip() == '---':
            break
        if ':' in line:
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()
    return fm


def audit_entrypoint(mem_dir: Path) -> dict:
    """审计 MEMORY.md 索引文件"""
    entrypoint = mem_dir / ENTRYPOINT_NAME
    result = {
        'exists': entrypoint.exists(),
        'line_count': 0,
        'byte_count': 0,
        'line_truncated': False,
        'byte_truncated': False,
        'long_lines': [],      # 超过推荐长度的行
        'inline_content': [],  # 包含实际内容的行（应该只有指针）
        'broken_pointers': [], # 指向不存在文件的指针
        'issues': [],
    }

    if not entrypoint.exists():
        result['issues'].append('MEMORY.md 不存在')
        return result

    raw = entrypoint.read_text(encoding='utf-8')
    lines = raw.strip().split('\n')
    result['line_count'] = len(lines)
    result['byte_count'] = len(raw.encode('utf-8'))

    # 检查行数/字节数截断
    if result['line_count'] > MAX_ENTRYPOINT_LINES:
        result['line_truncated'] = True
        result['issues'].append(
            f'行数超限：{result["line_count"]} 行（上限 {MAX_ENTRYPOINT_LINES}）'
            f' — Claude Code 只加载前 {MAX_ENTRYPOINT_LINES} 行'
        )
    if result['byte_count'] > MAX_ENTRYPOINT_BYTES:
        result['byte_truncated'] = True
        result['issues'].append(
            f'字节数超限：{result["byte_count"]:,} bytes（上限 {MAX_ENTRYPOINT_BYTES:,}）'
            f' — 超出部分被截断'
        )

    pointer_pattern = re.compile(r'^\s*-\s*\[(.+?)\]\((.+?)\)')

    for i, line in enumerate(lines, 1):
        # 检查行长度
        if len(line) > MAX_ENTRY_LINE_CHARS:
            result['long_lines'].append((i, len(line), line[:80] + '...'))

        # 检查指针有效性
        m = pointer_pattern.match(line)
        if m:
            target = m.group(2)
            if not target.startswith('http'):
                target_path = mem_dir / target
                if not target_path.exists():
                    result['broken_pointers'].append((i, target))
                    result['issues'].append(f'第 {i} 行：指针指向不存在的文件 {target}')
        elif line.strip() and not line.strip().startswith('#') and not line.strip().startswith('>'):
            # 非空、非标题、非 blockquote 的行 — 可能是内联内容
            if len(line.strip()) > 100 and '- [' not in line:
                result['inline_content'].append((i, line[:80] + '...'))

    return result


def audit_topic_files(mem_dir: Path) -> dict:
    """审计所有主题文件"""
    result = {
        'total': 0,
        'missing_frontmatter': [],
        'missing_type': [],
        'invalid_type': [],
        'missing_description': [],
        'stale_files': [],       # 超过 30 天未更新
        'files': [],
    }

    md_files = [f for f in mem_dir.rglob('*.md') if f.name != ENTRYPOINT_NAME]
    result['total'] = len(md_files)

    if result['total'] > MAX_MEMORY_FILES:
        result['issues'] = [f'文件数超限：{result["total"]}（上限 {MAX_MEMORY_FILES}）']

    now = datetime.now().timestamp()

    for fpath in sorted(md_files):
        rel = fpath.relative_to(mem_dir)
        content = fpath.read_text(encoding='utf-8')
        fm = parse_frontmatter(content)
        mtime = fpath.stat().st_mtime
        age_days = int((now - mtime) / 86400)

        file_info = {
            'path': str(rel),
            'type': fm.get('type', ''),
            'description': fm.get('description', ''),
            'age_days': age_days,
            'issues': [],
        }

        if not fm:
            result['missing_frontmatter'].append(str(rel))
            file_info['issues'].append('缺少 frontmatter')

        if fm and not fm.get('type'):
            result['missing_type'].append(str(rel))
            file_info['issues'].append('frontmatter 缺少 type 字段')
        elif fm.get('type') and fm['type'] not in MEMORY_TYPES:
            result['invalid_type'].append((str(rel), fm['type']))
            file_info['issues'].append(f'无效 type: {fm["type"]}（有效值: {", ".join(MEMORY_TYPES)}）')

        if fm and not fm.get('description'):
            result['missing_description'].append(str(rel))
            file_info['issues'].append('frontmatter 缺少 description 字段（影响按需加载的相关性判断）')

        if age_days > 30:
            result['stale_files'].append((str(rel), age_days))

        result['files'].append(file_info)

    return result


def print_report(mem_dir: Path):
    """打印完整审计报告"""
    print(f"\n{'='*60}")
    print(f"  Memory 健康报告")
    print(f"  目录: {mem_dir}")
    print(f"  时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    ep = audit_entrypoint(mem_dir)
    topic = audit_topic_files(mem_dir)

    # MEMORY.md 状态
    print("## MEMORY.md 索引")
    if not ep['exists']:
        print("  ⚠️  MEMORY.md 不存在")
    else:
        line_status = '✅' if not ep['line_truncated'] else '❌'
        byte_status = '✅' if not ep['byte_truncated'] else '❌'
        print(f"  {line_status} 行数: {ep['line_count']}/{MAX_ENTRYPOINT_LINES}")
        print(f"  {byte_status} 大小: {ep['byte_count']:,}/{MAX_ENTRYPOINT_BYTES:,} bytes")

        if ep['long_lines']:
            print(f"\n  ⚠️  超长行（推荐 ≤{MAX_ENTRY_LINE_CHARS} 字符）:")
            for lineno, length, preview in ep['long_lines'][:5]:
                print(f"     第{lineno}行 ({length}字): {preview}")

        if ep['broken_pointers']:
            print(f"\n  ❌ 断链指针:")
            for lineno, target in ep['broken_pointers']:
                print(f"     第{lineno}行 → {target}")

        if ep['inline_content']:
            print(f"\n  ⚠️  疑似内联内容（应移入主题文件）:")
            for lineno, preview in ep['inline_content'][:3]:
                print(f"     第{lineno}行: {preview}")

    # 主题文件状态
    print(f"\n## 主题文件 ({topic['total']} 个)")

    if topic['missing_frontmatter']:
        print(f"\n  ❌ 缺少 frontmatter ({len(topic['missing_frontmatter'])} 个):")
        for f in topic['missing_frontmatter'][:5]:
            print(f"     {f}")

    if topic['invalid_type']:
        print(f"\n  ❌ 无效 type ({len(topic['invalid_type'])} 个):")
        for f, t in topic['invalid_type'][:5]:
            print(f"     {f}: type='{t}'")

    if topic['missing_description']:
        print(f"\n  ⚠️  缺少 description ({len(topic['missing_description'])} 个):")
        for f in topic['missing_description'][:5]:
            print(f"     {f}")

    if topic['stale_files']:
        print(f"\n  💤 超过 30 天未更新 ({len(topic['stale_files'])} 个):")
        for f, days in sorted(topic['stale_files'], key=lambda x: -x[1])[:5]:
            print(f"     {f}: {days} 天前")

    # 总结
    total_issues = (
        len(ep.get('issues', [])) +
        len(topic['missing_frontmatter']) +
        len(topic['invalid_type']) +
        len(topic['missing_description'])
    )

    print(f"\n{'='*60}")
    if total_issues == 0:
        print("  ✅ 记忆结构健康，无需修复")
    else:
        print(f"  ⚠️  发现 {total_issues} 个问题")
        print(f"  💡 运行 /memory-architect 来自动修复")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        mem_dir = Path(sys.argv[1]).expanduser()
    else:
        mem_dir = find_memory_dir()
        if not mem_dir:
            print("未找到记忆目录。请指定路径：")
            print("  python memory_audit.py ~/.claude/projects/<project>/memory/")
            sys.exit(1)
        print(f"自动发现记忆目录: {mem_dir}")

    if not mem_dir.exists():
        print(f"目录不存在: {mem_dir}")
        sys.exit(1)

    print_report(mem_dir)
