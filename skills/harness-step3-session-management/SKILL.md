---
name: harness-step3-session-management
description: |
  Harness Engineering 第二阶段：建立跨 session 状态管理，解决 agent 每次对话失忆的问题。
  创建 tasks.json（任务清单）、progress.md（进度记录）、init.sh（环境初始化脚本）三个文件。

  当用户说"建立任务管理"、"让 agent 记住进度"、"创建 tasks.json"、"跨 session 保持状态"、
  "agent 每次都不记得上次做了什么"、"建立 progress 文件"、"初始化状态管理"时，立即使用此 skill。

  前置条件：harness-step1 和 harness-step2 已完成（项目有 AGENTS.md 和 docs/ 知识库）。
---

# Harness Step 3: 建立跨 Session 状态管理

## 目标

创建三个文件，让 agent 在任何新 session 开始时能在 30 秒内恢复工作状态：

- `init.sh`：环境初始化脚本，验证项目可以正常启动
- `tasks.json`：当前任务清单，agent 的工作指令来源
- `progress.md`：人类可读的进度摘要，记录每次 session 的关键信息

**核心原则**：状态靠文件传递，不靠 agent 的记忆。git log 是主记录，这三个文件是辅助。

---

## 执行步骤

### Step 1：扫描项目启动方式

在写 `init.sh` 之前，先确认项目如何启动和测试：

```bash
# 读 package.json 的 scripts（Node.js 项目）
cat package.json 2>/dev/null | grep -A 20 '"scripts"'

# 或读 Makefile（多语言项目）
cat Makefile 2>/dev/null | head -40

# 或读 pyproject.toml（Python 项目）
cat pyproject.toml 2>/dev/null | grep -A 20 '\[tool.poetry.scripts\]'

# 确认现有 AGENTS.md 里的启动命令
grep -A 5 '启动命令\|start\|dev\|run' AGENTS.md 2>/dev/null
```

收集：
- 开发服务器启动命令
- 测试命令
- 类型检查/lint 命令（如果有）
- 有没有需要先跑的初始化步骤（如数据库迁移）

---

### Step 2：创建 `init.sh`

`init.sh` 的作用：每次 session 开始时运行，**快速验证环境是否正常**，不正常就立即修复再继续。

```bash
#!/bin/bash
# init.sh — 每次 session 开始时运行
# 验证开发环境处于可工作状态

set -e  # 任何步骤失败就停止

echo "=== 检查环境 ==="

# 1. 确认在正确目录
echo "工作目录: $(pwd)"

# 2. 安装依赖（如果 node_modules 不存在）
# [根据技术栈选择，以下是示例]
# Node.js:
if [ ! -d "node_modules" ]; then
  echo "安装依赖..."
  npm install
fi

# 3. 冒烟测试：验证项目能正常启动
# [根据项目实际情况写，目标是用最快的方式验证基本功能正常]
# 示例：跑一个最快的测试
# npm run test -- --testPathPattern=smoke 2>/dev/null || echo "警告：冒烟测试失败，请先修复"

echo "=== 环境检查完成，可以开始工作 ==="
echo "提示：运行 'git log --oneline -10' 查看最近工作历史"
```

**写作要求**：
- 根据扫描到的实际启动命令填写，不要留示例注释
- 冒烟测试要快（< 30秒），目的是快速发现环境问题，不是跑完整测试套件
- 如果项目有数据库，加一步检查数据库连接是否正常
- 写完后实际运行一遍，确认脚本无报错：`bash init.sh`

---

### Step 3：创建 `tasks.json`

**结构设计**：

```json
{
  "project": "[项目名]",
  "last_updated": "[今天日期，格式 YYYY-MM-DD]",
  "current_focus": "[当前最重要的一件事，一句话]",
  "tasks": [
    {
      "id": "[模块缩写]-[序号]",
      "title": "[任务标题]",
      "description": "[具体做什么，1-3句话]",
      "status": "pending | in_progress | done | blocked",
      "priority": "high | medium | low",
      "blocked_by": "[阻塞原因，仅 blocked 状态时填写]",
      "verify": "[如何验证这个任务完成了]",
      "requires_eval": false
    }
  ]
}
```

**字段说明**（每次新增任务时必须逐字段填写，不能省略）：

| 字段 | 是否必填 | 说明 |
|------|----------|------|
| `id` | 必填 | 模块缩写 + 序号，如 `auth-01`、`ui-03`，简短可读 |
| `title` | 必填 | 任务标题，一句话 |
| `description` | 必填 | 具体做什么，1-3 句话 |
| `status` | 必填 | 初始值为 `pending`，由 agent 工作时更新 |
| `priority` | 必填 | `high / medium / low` |
| `blocked_by` | 仅 blocked 时填 | 阻塞原因 |
| `verify` | 必填 | 如何验证完成，必须是可执行的步骤（命令或操作） |
| `requires_eval` | 必填 | 是否需要独立 Evaluator 评审，默认 `false`，见判断标准 |

**`requires_eval` 判断标准**（新增任务时必须对照判断，不能不加思考直接填 false）：

设为 `true` 的条件，满足任意一条即需要评审：
- 这是一个新功能（不只是修 bug 或改配置）
- 涉及安全、权限、数据校验相关逻辑
- 预计会修改 3 个以上文件
- 任务描述里有"重构"或"架构调整"

设为 `false` 的条件（以下全部满足才可以跳过评审）：
- 纯 bug 修复，改动范围明确
- 文档更新、注释补充
- 配置调整、环境变量修改
- 单元测试补充

**如何确定初始任务列表**：

优先从以下来源提取：
1. `docs/exec-plans/active/` 里的计划文件（如果有）
2. `docs/exec-plans/tech-debt-tracker.md` 里的高优先级债务
3. README 里提到的 TODO 或路线图
4. 询问用户：「当前最想推进的 3-5 个任务是什么？」

**写作要求**：
- `verify` 字段必须是可执行的步骤，不能写"确认功能正常"这种废话
- 任务粒度：一个任务应该在 1-2 小时内完成，太大的拆分
- 初始状态：所有任务都是 `pending`，由 agent 工作时更新

**询问用户**（如果无法从现有文档推断任务）：

> 我已经扫描了项目，准备创建任务清单。请告诉我：
> 当前最想推进的 3-5 个任务是什么？
> 每个任务用一句话描述就行。

---

### Step 4：创建 `progress.md`

初始内容：

```markdown
# 项目进度记录

> 每次 session 完成任务后，在顶部追加记录。不要删除历史。
> 格式：## [日期] [任务名]

---

## [今天日期] 初始化 Harness

- 完成 harness-step1：建立 docs/ 骨架
- 完成 harness-step2：填充知识库内容
- 完成 harness-step3：建立状态管理
- tasks.json 初始任务数：[N] 个
- 下次从这里开始：读 tasks.json，选 priority=high 且 status=pending 的任务开始
```

---

### Step 4b：更新 `AGENTS.md` —— 写入任务管理规则

找到 `AGENTS.md` 里 step2 写入的"每次完成一个任务后"部分，**替换**为以下内容：

```markdown
### 新增任务时，必须：
1. 填写 tasks.json 里的所有字段，不能省略
2. 对照以下标准判断 `requires_eval`，不能默认填 false 不加思考：
   - 新功能 / 涉及安全权限 / 改动超过 3 个文件 / 重构 → true
   - 纯 bug 修复 / 文档更新 / 配置调整 → false

### 每次完成一个任务后，必须按顺序执行：
1. 执行 `tasks.json` 里该任务 `verify` 字段描述的验证步骤
2. 若该任务 `requires_eval` 为 `true`：填写 `sprint_output.md`，等待 Evaluator 评审通过后才能标记 `done`
   若该任务 `requires_eval` 为 `false`：验证通过即可标记 `done`
3. git commit，格式：`type(scope): 做了什么，遗留了什么（如有）`
4. 在 `progress.md` 顶部追加本次记录

**禁止**：跳过 verify 步骤自行判断任务已完成。
**禁止**：不经判断直接把 `requires_eval` 设为 false。
```

---

### Step 5：验证整体联动

三个文件创建完后，模拟一次完整的 session 启动流程，验证联动是否正常：

```bash
# 模拟 agent 新 session 开始的操作序列
echo "=== 模拟新 session 启动 ==="

# 1. 跑 init.sh
bash init.sh

# 2. 看 git log
git log --oneline -10

# 3. 读 progress.md（确认文件存在且可读）
head -20 progress.md

# 4. 读 tasks.json（确认格式正确）
cat tasks.json | python3 -m json.tool > /dev/null && echo "tasks.json 格式正确" || echo "tasks.json 格式有误"
```

全部通过才算完成。

---

## 质量检验

- [ ] `init.sh` 实际运行无报错？
- [ ] `tasks.json` JSON 格式合法？每个任务都有 `verify` 和 `requires_eval` 字段？
- [ ] 每个任务的 `requires_eval` 是否对照判断标准填写，而非默认 false？
- [ ] `progress.md` 有初始记录？
- [ ] `AGENTS.md` 里是否包含新增任务和完成任务的两条规则？

---

## 完成后告知用户

输出摘要：

**创建的文件**：
- `init.sh`：[描述做了什么检查]
- `tasks.json`：[N] 个任务，其中需要 Evaluator 评审的 [N] 个
- `progress.md`：已初始化

**如何使用**：
> 现在你可以把项目交给 Claude Code 了。它每次启动时会自动读这三个文件 + git log，
> 恢复工作状态。你不需要每次都解释"上次做到哪里了"。

**需要你做的事**：
- 检查 `tasks.json` 里的任务列表是否符合你的预期，可以手动增删
- 确认 `requires_eval` 的判断是否合理
- 如果 `init.sh` 有步骤失败，告诉我，我来修复

**下一步**：
- Harness 地基已完成（step1 + step2 + step3）
- 可以开始正式使用 Claude Code 开发
- 遇到 agent 反复违反代码规范时，运行 `harness-step4-linter`，把规则变成机械约束
- 遇到 agent 自评不可信时，运行 `harness-step5-evaluator`，引入独立评审
