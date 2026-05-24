#!/usr/bin/env python3
"""
pre_compact_extract.py — 从 Claude Code 会话 JSONL 文件提取值得记忆的内容草稿

设计依据（来自 Claude Code 源码）：
- 会话存储格式: JSONL, 每行一条消息 (src/utils/sessionStorage.ts)
- 记忆类型: user/feedback/project/reference (src/memdir/memoryTypes.ts)
- 提取逻辑: 只记"不可推导"的信息——代码可读到的不记 (src/services/extractMemories/prompts.ts)
- 反馈类型同时记纠正和认可 (src/memdir/memoryTypes.ts: "Record from failure AND success")
- MEMORY.md 上限: 200 行 / 25KB (src/services/autoDream/consolidationPrompt.ts)

用法：
    python pre_compact_extract.py session.jsonl
    python pre_compact_extract.py --latest
    python pre_compact_extract.py --latest --check-memory   # 同时检查现有记忆冲突
    python pre_compact_extract.py session.jsonl --output extract.md
"""

import json
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime, timedelta

# ── 信号模式 ────────────────────────────────────────────────────────────────

DECISION_PATTERNS = [
    re.compile(r"(?:we(?:'re| are| decided| chose| went| picked| will)|i(?:'ll| will)|let'?s|going to)\s+(?:use|go with|adopt|implement|switch to|replace)\s+(.{10,80})", re.IGNORECASE),
    re.compile(r"(?:instead of|rather than|over)\s+(.{5,50})\s+(?:because|since|due to|as)", re.IGNORECASE),
    re.compile(r"(?:the reason|this is because|why we|that'?s why)\s+(.{10,100})", re.IGNORECASE),
]

FAILURE_PATTERNS = [
    re.compile(r"(?:doesn'?t work|failed|broken|won'?t work|can'?t use|avoid|don'?t use)\s+(.{10,80})", re.IGNORECASE),
    re.compile(r"(?:tried|attempted)\s+(.{10,60})\s+(?:but|however|unfortunately|though)", re.IGNORECASE),
    re.compile(r"(?:the problem|issue|bug)\s+(?:is|was|with)\s+(.{10,80})", re.IGNORECASE),
]

DISCOVERY_PATTERNS = [
    re.compile(r"(?:found out|discovered|learned|turns out|noticed|realized)\s+(?:that\s+)?(.{10,100})", re.IGNORECASE),
    re.compile(r"(?:interesting|important|note|warning|caveat):\s*(.{10,100})", re.IGNORECASE),
    re.compile(r"(?:key insight|takeaway|lesson):\s*(.{10,100})", re.IGNORECASE),
]

BLOCKER_PATTERNS = [
    re.compile(r"(?:blocked|stuck|waiting for|need to|can'?t proceed)\s+(.{10,80})", re.IGNORECASE),
    re.compile(r"(?:open question|unresolved|TODO|FIXME|need to figure out)\s*[:\-]?\s*(.{10,80})", re.IGNORECASE),
]

# 用户纠正（correction）
USER_CORRECTION_PATTERNS = [
    re.compile(r"(?:no,?\s+don'?t|please don'?t|stop|never|don'?t do that|wrong|incorrect)\s+(.{10,80})", re.IGNORECASE),
    re.compile(r"(?:i said|i meant|i want)\s+(.{10,80})", re.IGNORECASE),
]

# 用户认可（confirmation）— 同样重要，记录已验证有效的方案
USER_CONFIRMATION_PATTERNS = [
    re.compile(r"(?:yes,?\s+(?:exactly|perfect|that'?s it|great)|perfect,?\s+(?:keep|do it|yes)|exactly right|that'?s what i wanted)\s*(.{0,80})", re.IGNORECASE),
    re.compile(r"(?:good call|right call|that was the right)\s+(.{0,80})", re.IGNORECASE),
    re.compile(r"(?:confirmed|approved|looks good|lgtm)\s*[,.]?\s*(.{0,60})", re.IGNORECASE),
]

# 相对日期模式（需要转换为绝对日期）
RELATIVE_DATE_PATTERNS = [
    re.compile(r'\b(?:next|this)\s+(?:monday|tuesday|wednesday|thursday|friday|saturday|sunday|week|month)\b', re.IGNORECASE),
    re.compile(r'\bin\s+\d+\s+(?:day|week|month)s?\b', re.IGNORECASE),
    re.compile(r'\btomorrow\b', re.IGNORECASE),
    re.compile(r'\bby\s+(?:end\s+of\s+)?(?:the\s+)?(?:week|month|quarter|year)\b', re.IGNORECASE),
]


# ── 工具函数 ─────────────────────────────────────────────────────────────────

def load_jsonl(filepath: Path) -> list[dict]:
    messages = []
    try:
        with open(filepath, encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        messages.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    except Exception as e:
        print(f"读取文件失败: {e}")
        sys.exit(1)
    return messages


def extract_text(message: dict) -> tuple[str, str]:
    role = message.get('type', 'unknown')
    msg = message.get('message', {})
    if not msg:
        return role, ''
    content = msg.get('content', '')
    if isinstance(content, str):
        return role, content
    elif isinstance(content, list):
        texts = []
        for block in content:
            if isinstance(block, dict) and block.get('type') == 'text':
                texts.append(block.get('text', ''))
        return role, '\n'.join(texts)
    return role, ''


def detect_relative_dates(text: str) -> list[str]:
    found = []
    for pattern in RELATIVE_DATE_PATTERNS:
        for m in pattern.finditer(text):
            found.append(m.group(0))
    return found


def find_project_memory_dir() -> Path | None:
    cwd = Path.cwd()
    root = cwd
    for parent in [cwd, *cwd.parents]:
        if (parent / '.git').exists():
            root = parent
            break
    sanitized = str(root).replace('/', '-').replace('\\', '-').replace(':', '-').lstrip('-')
    mem_dir = Path.home() / '.claude' / 'projects' / sanitized / 'memory'
    return mem_dir if mem_dir.exists() else None


def check_existing_memory(mem_dir: Path) -> dict:
    """检查现有记忆：行数、文件列表、潜在过时条目"""
    result = {'memory_md_lines': 0, 'files': [], 'over_limit': False, 'old_files': []}
    memory_md = mem_dir / 'MEMORY.md'
    if memory_md.exists():
        lines = memory_md.read_text(encoding='utf-8').splitlines()
        result['memory_md_lines'] = len(lines)
        result['over_limit'] = len(lines) >= 180  # 200 行上限，180 发出警告

    cutoff = datetime.now() - timedelta(days=30)
    for f in mem_dir.glob('*.md'):
        if f.name == 'MEMORY.md':
            continue
        mtime = datetime.fromtimestamp(f.stat().st_mtime)
        age_days = (datetime.now() - mtime).days
        result['files'].append({'name': f.name, 'age_days': age_days})
        if mtime < cutoff:
            result['old_files'].append({'name': f.name, 'age_days': age_days})

    return result


# ── 信号提取 ─────────────────────────────────────────────────────────────────

def extract_signals(messages: list[dict]) -> dict:
    signals = {
        'decisions': [],
        'failures': [],
        'discoveries': [],
        'blockers': [],
        'user_corrections': [],    # 用户纠正（feedback）
        'user_confirmations': [],  # 用户认可（feedback — 同样重要）
        'relative_dates': [],      # 需要转换为绝对日期的项目记忆
    }

    for msg in messages:
        role, text = extract_text(msg)
        if not text or len(text) < 20:
            continue

        if role == 'assistant':
            for pattern in DECISION_PATTERNS:
                for m in pattern.finditer(text):
                    snippet = m.group(0)[:150].strip()
                    if snippet not in signals['decisions']:
                        signals['decisions'].append(snippet)

            for pattern in FAILURE_PATTERNS:
                for m in pattern.finditer(text):
                    snippet = m.group(0)[:150].strip()
                    if snippet not in signals['failures']:
                        signals['failures'].append(snippet)

            for pattern in DISCOVERY_PATTERNS:
                for m in pattern.finditer(text):
                    snippet = m.group(0)[:150].strip()
                    if snippet not in signals['discoveries']:
                        signals['discoveries'].append(snippet)

            for pattern in BLOCKER_PATTERNS:
                for m in pattern.finditer(text):
                    snippet = m.group(0)[:150].strip()
                    if snippet not in signals['blockers']:
                        signals['blockers'].append(snippet)

        elif role == 'user':
            for pattern in USER_CORRECTION_PATTERNS:
                for m in pattern.finditer(text):
                    snippet = m.group(0)[:150].strip()
                    if snippet not in signals['user_corrections']:
                        signals['user_corrections'].append(snippet)

            for pattern in USER_CONFIRMATION_PATTERNS:
                for m in pattern.finditer(text):
                    snippet = m.group(0)[:150].strip()
                    if snippet not in signals['user_confirmations']:
                        signals['user_confirmations'].append(snippet)

            # 相对日期检测
            dates = detect_relative_dates(text)
            for d in dates:
                if d not in signals['relative_dates']:
                    signals['relative_dates'].append(d)

    return signals


# ── 草稿生成 ─────────────────────────────────────────────────────────────────

def generate_memory_draft(signals: dict, session_path: Path, memory_check: dict | None = None) -> str:
    now = datetime.now().strftime('%Y-%m-%d')
    today_abs = datetime.now().strftime('%Y-%m-%d')

    lines = [
        f"# 会话记忆提取草稿",
        f"来源: {session_path.name}",
        f"提取时间: {now}",
        f"",
        f"> ⚠️ 自动提取的草稿，需人工审核后再写入 MEMORY.md",
        f"> 只保留没有 **Why:** 答案就说不清楚的条目——其他的跳过",
        f"",
    ]

    # 现有记忆状态
    if memory_check:
        lines.append("## 现有记忆状态")
        lines.append(f"- MEMORY.md 行数: {memory_check['memory_md_lines']} / 200")
        if memory_check['over_limit']:
            lines.append(f"- ⚠️ **接近上限（{memory_check['memory_md_lines']} 行）** — 写入前先合并或删除旧条目")
        if memory_check['old_files']:
            lines.append(f"- 超过 30 天未更新的记忆文件（可能需要验证或清理）：")
            for f in memory_check['old_files']:
                lines.append(f"  - `{f['name']}` ({f['age_days']} 天前)")
        lines.append("")

    # 用户纠正（feedback — correction）
    if signals['user_corrections']:
        lines.extend([
            "## 用户纠正 → `type: feedback`",
            "结构：先写规则，再写 **Why:** 和 **How to apply:**",
            "",
        ])
        for s in signals['user_corrections'][:5]:
            lines.append(f"- {s}")
        lines.append("")

    # 用户认可（feedback — confirmation，同等重要）
    if signals['user_confirmations']:
        lines.extend([
            "## 用户认可 → `type: feedback`（confirmation）",
            "已验证有效的方案，同样值得记——避免下次对正确做法过度保守",
            "",
        ])
        for s in signals['user_confirmations'][:5]:
            lines.append(f"- {s}")
        lines.append("")

    # 决策（project）
    if signals['decisions']:
        lines.extend([
            "## 决策 → `type: project`",
            "架构选择、方案取舍，包含 Why（这是必须有的）",
            "",
        ])
        for s in signals['decisions'][:8]:
            lines.append(f"- {s}")
        lines.append("")

    # 失败方案（feedback）
    if signals['failures']:
        lines.extend([
            "## 失败方案 → `type: feedback`",
            "试过但行不通的路，下次不要重试",
            "",
        ])
        for s in signals['failures'][:5]:
            lines.append(f"- {s}")
        lines.append("")

    # 新发现（project/reference）
    if signals['discoveries']:
        lines.extend([
            "## 新发现 → `type: project` 或 `reference`",
            "",
        ])
        for s in signals['discoveries'][:8]:
            lines.append(f"- {s}")
        lines.append("")

    # 当前阻塞点（project）
    if signals['blockers']:
        lines.extend([
            "## 当前阻塞点 → `type: project`",
            "下次会话还需要处理的问题",
            "",
        ])
        for s in signals['blockers'][:5]:
            lines.append(f"- {s}")
        lines.append("")

    # 相对日期提醒
    if signals['relative_dates']:
        lines.extend([
            "## ⚠️ 相对日期需转换为绝对日期",
            f"（今天是 {today_abs}，写入 project 记忆时请换算）",
            "",
        ])
        for d in signals['relative_dates']:
            lines.append(f"- 检测到: `{d}` → 请手动换算为 YYYY-MM-DD")
        lines.append("")

    total = sum(len(v) for v in signals.values())
    if total == 0:
        lines.extend([
            "_未提取到明显的记忆信号。_",
            "_这次会话可能不需要新记忆，或信号表述不在检测模式中，建议手动回顾对话。_",
            "",
        ])

    # 记忆文件模板
    lines.extend([
        "---",
        "## 记忆文件格式模板",
        "",
        "```markdown",
        "---",
        "name: <short-kebab-case-slug>",
        "description: <一行摘要 — 何时应召回这条记忆>",
        "type: feedback | project | user | reference",
        "---",
        "",
        "<规则或事实>",
        "",
        "**Why:** <原因 — 过去的事故、强烈偏好、或约束>",
        "**How to apply:** <什么情况下适用>",
        "```",
        "",
        "MEMORY.md 指针格式（每行 150 字符以内）：",
        "```",
        "- [Title](filename.md) — 一行说明何时相关",
        "```",
        "",
        "---",
        "## 不应写入记忆的内容",
        "",
        "- 代码结构、架构、文件路径 — 读代码可得",
        "- git 历史 — git log 有",
        "- 调试方案或 fix 步骤 — fix 已在代码里，commit 有上下文",
        "- CLAUDE.md 里已有的内容",
        "- 本次会话临时状态",
    ])

    return '\n'.join(lines)


# ── 会话查找 ─────────────────────────────────────────────────────────────────

def find_latest_session() -> Path | None:
    cwd = Path.cwd()
    root = cwd
    for parent in [cwd, *cwd.parents]:
        if (parent / '.git').exists():
            root = parent
            break

    sanitized = str(root).replace('/', '-').replace('\\', '-').replace(':', '-').lstrip('-')
    sessions_dir = Path.home() / '.claude' / 'projects' / sanitized

    if not sessions_dir.exists():
        return None

    jsonl_files = list(sessions_dir.glob('*.jsonl'))
    if not jsonl_files:
        return None

    return max(jsonl_files, key=lambda p: p.stat().st_mtime)


# ── 主程序 ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description='从 Claude Code 会话文件提取值得记忆的内容草稿'
    )
    parser.add_argument('session', nargs='?', help='会话 JSONL 文件路径')
    parser.add_argument('--latest', action='store_true', help='处理当前项目最新会话')
    parser.add_argument('--check-memory', action='store_true', help='检查现有 MEMORY.md 状态（行数、过时文件）')
    parser.add_argument('--output', '-o', help='输出文件路径（默认打印到终端）')

    args = parser.parse_args()

    if args.latest:
        session_path = find_latest_session()
        if not session_path:
            print("未找到会话文件。")
            sys.exit(1)
        print(f"处理最新会话: {session_path.name}")
    elif args.session:
        session_path = Path(args.session).expanduser()
    else:
        parser.print_help()
        sys.exit(0)

    if not session_path.exists():
        print(f"文件不存在: {session_path}")
        sys.exit(1)

    # 检查现有记忆（可选）
    memory_check = None
    if args.check_memory:
        mem_dir = find_project_memory_dir()
        if mem_dir:
            memory_check = check_existing_memory(mem_dir)
            print(f"记忆目录: {mem_dir}")
            print(f"MEMORY.md 行数: {memory_check['memory_md_lines']} / 200")
        else:
            print("未找到记忆目录（~/.claude/projects/<hash>/memory/）")

    print(f"读取会话: {session_path}")
    messages = load_jsonl(session_path)
    print(f"消息数: {len(messages)}")

    signals = extract_signals(messages)
    total = sum(len(v) for v in signals.values())
    print(f"提取信号: {total} 条")

    draft = generate_memory_draft(signals, session_path, memory_check)

    if args.output:
        output_path = Path(args.output)
        output_path.write_text(draft, encoding='utf-8')
        print(f"草稿已写入: {output_path}")
    else:
        print("\n" + "=" * 60)
        print(draft)
        print("=" * 60)


if __name__ == '__main__':
    main()
