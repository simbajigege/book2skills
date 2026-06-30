---
name: tool-permission-system
description: 'Design and implement a layered, configurable permission/safety system for agent tools. Use this skill when building an agent that needs to control which tool calls are auto-allowed, which require user confirmation, and which are denied — especially when the system must be configurable across multiple scopes (project/user/enterprise) and extensible via hooks. Triggers on: "权限系统", "工具安全", "tool permission", "permission system", "tool safety", "allow/deny rules", "hook system", "构建安全机制".'
---

# Tool Permission System

## Core Idea

Every time an agent calls a tool, a **permission pipeline** runs before execution. This pipeline is the single place that decides: auto-allow, ask the user, or deny. The pipeline is layered — different stakeholders (enterprise admin, user, project team, session) can each contribute rules, with higher layers overriding lower ones.

```
Tool call request
  ↓
[硬否决] Deny rules → immediate deny
  ↓
[强制确认] Ask rules → force prompt (even in bypass mode)
  ↓
[工具自身] Tool's checkPermissions() → tool-specific logic
  ↓
[安全绕过免疫] Safety checks (.git/, .claude/, shell configs) → prompt, immune to bypass
  ↓
[模式快速通过] Bypass / acceptEdits mode → immediate allow
  ↓
[白名单] Allow rules → immediate allow
  ↓
[默认] passthrough → prompt user (ask)
```

**外层包装**（作用于整条流水线之后）：
- `dontAsk` 模式：把所有 `ask` 转为 `deny`（用于无交互的后台 agent）
- `auto` 模式：把所有 `ask` 转给 AI 分类器判断，而不是打断用户
- `headless` 模式：先跑 PermissionRequest hooks，hooks 没回应就自动 deny

## Workflow

### 1. 定义三种决策行为

```typescript
type PermissionBehavior = 'allow' | 'deny' | 'ask'

type PermissionDecision =
  | { behavior: 'allow'; updatedInput?: unknown; decisionReason?: DecisionReason }
  | { behavior: 'ask';   message: string; suggestions?: PermissionUpdate[] }
  | { behavior: 'deny';  message: string; decisionReason: DecisionReason }
```

### 2. 建立分层规则来源

规则来源按优先级从高到低排列：

```
policySettings    ← 企业管理员，用户不可覆盖
userSettings      ← 用户全局 (~/.agent/settings.json)
projectSettings   ← 项目级 (.agent/settings.json，可提交 git)
localSettings     ← 本地私有 (.agent/settings.local.json)
cliArg            ← 启动参数
command           ← 运行时命令
session           ← 当次会话临时
```

每条规则的格式：`ToolName` 或 `ToolName(content)`。

### 3. 实现权限决策函数

```typescript
async function hasPermission(tool, input, context): Promise<PermissionDecision> {
  // Step 1: deny rules (优先级最高，含企业强制)
  const denyRule = findMatchingRule(context.denyRules, tool, input)
  if (denyRule) return { behavior: 'deny', message: '...', decisionReason: { type: 'rule', rule: denyRule } }

  // Step 2: ask rules (强制弹框，绕过模式也无法跳过)
  const askRule = findMatchingRule(context.askRules, tool, input)
  if (askRule) return { behavior: 'ask', message: '...' }

  // Step 3: 工具自身的 checkPermissions()
  const toolResult = await tool.checkPermissions(input, context)
  if (toolResult.behavior === 'deny') return toolResult
  if (toolResult.behavior === 'ask' && toolResult.decisionReason?.type === 'rule') return toolResult  // ask rule 免疫 bypass
  if (toolResult.behavior === 'ask' && toolResult.decisionReason?.type === 'safetyCheck') return toolResult  // 安全检查免疫 bypass

  // Step 4: bypass 模式快速通过
  if (context.mode === 'bypassPermissions') return { behavior: 'allow', updatedInput: input }

  // Step 5: allow rules 白名单
  const allowRule = findMatchingRule(context.allowRules, tool, input)
  if (allowRule) return { behavior: 'allow', updatedInput: input }

  // Step 6: 默认转 ask
  return { behavior: 'ask', message: `Agent requested to use ${tool.name}` }
}
```

### 4. 为每个工具定义安全属性接口（fail-closed 默认值）

工具与权限系统的接合点是工具接口上的一组**安全属性**。关键设计：所有属性都遵循**失败关闭（fail-closed）**——开发者不声明时，系统按"最保守"假设处理，必须主动声明"我是安全的"才放宽。

```typescript
// 工厂函数用 TOOL_DEFAULTS 填充未声明的属性
const TOOL_DEFAULTS = {
  isEnabled:         () => true,
  isConcurrencySafe: () => false,   // 默认不并发（怕数据竞争）
  isReadOnly:        () => false,   // 默认假设会写入
  isDestructive:     () => false,   // 默认假设不可逆操作要谨慎
  checkPermissions:  (input) => ({ behavior: 'allow', updatedInput: input }), // 默认交给中央权限系统
}
function buildTool(def) { return { ...TOOL_DEFAULTS, ...def } }
```

| 属性 | 返回 | 谁来问 / 影响什么 |
|---|---|---|
| `isReadOnly(input)` | boolean | 权限系统：只读操作可绕过部分限制 |
| `isDestructive(input)` | boolean | 权限系统：不可逆操作需更严格确认 |
| `isConcurrencySafe(input)` | boolean | Agent Loop：能否与其他工具并发执行（默认 false → 串行） |
| `checkPermissions(input, ctx)` | PermissionResult | 权限系统：工具专属权限逻辑（流水线 1c） |
| `validateInput(input, ctx)` | ValidationResult | Agent Loop：执行前的输入合法性校验 |

**`checkPermissions` 在流水线里的位置是"夹心结构"**：通用 deny/ask 规则在它**之前**（且 bypass 也拦不住），通用 allow 白名单在它**之后**。所以工具自检既挡不住企业 deny，也不必重复实现通用 allow——只管工具特有的逻辑：

```typescript
class MyTool implements Tool {
  isReadOnly = () => false
  isConcurrencySafe = () => false

  async checkPermissions(input, context): Promise<PermissionResult> {
    // 检查工具特定规则（如 Bash 检查具体命令前缀）
    const allowRules = getRuleContentsForTool(context, this, 'allow')
    if (allowRules.has(getCommandPrefix(input.command))) {
      return { behavior: 'allow' }
    }

    // 检查危险路径（命中后 type:'safetyCheck' → bypass 也拦不住，见下方说明）
    if (isDangerousPath(input.path)) {
      return {
        behavior: 'ask',
        message: '...',
        decisionReason: { type: 'safetyCheck', reason: '...', classifierApprovable: false }
      }
    }

    return { behavior: 'passthrough', message: '...' }  // 没意见 → 交给外层
  }
}
```

**危险路径黑名单**（`safetyCheck`）是一份硬编码的敏感文件/目录清单，即使 bypass / acceptEdits / 配了 allow 规则也强制弹框，防两类攻击：① 代码执行（`.git/` hooks、`.bashrc`/`.zshrc` 等 shell 启动脚本、`.vscode`/`.idea` 任务配置）；② AI 改自己的护栏（`.claude/`、`.mcp.json`、`.claude.json` —— agent 不能通过"正常编辑文件"给自己提权）。完整清单见 `references/dangerous-patterns.ts`。

### 5. 实现 Hook 系统（可选但推荐）

Hook 让用户/企业在工具生命周期各节点插入自定义逻辑：

```typescript
// 配置格式（settings.json）
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "MyTool",          // 可选，工具名过滤
      "hooks": [{
        "type": "command",          // command | prompt | agent | http
        "command": "check-safety.sh $TOOL_INPUT"
      }]
    }],
    "PostToolUse": [{
      "matcher": "FileEdit",
      "hooks": [{ "type": "command", "command": "prettier --write $FILE_PATH" }]
    }]
  }
}
```

Hook 执行结果影响权限决策：
- exit 0 → 通过
- exit 2 → block（工具不执行）
- stdout 包含 JSON `{"action": "allow"}` → 覆盖决策

### 6. 实现 Denial 追踪（AI 分类器场景）

当使用 AI 分类器自动判断权限时，需要 circuit breaker 防止分类器过于严格：

```typescript
// 连续拒绝 3 次或累计拒绝 20 次 → 回退到人工确认
const DENIAL_LIMITS = { maxConsecutive: 3, maxTotal: 20 }

function shouldFallback(state: DenialTrackingState): boolean {
  return (
    state.consecutiveDenials >= DENIAL_LIMITS.maxConsecutive ||
    state.totalDenials >= DENIAL_LIMITS.maxTotal
  )
}
```

## Required Decisions

设计时必须明确的三个问题：

1. **哪些操作永远不需要确认？** → 放入 allow rules（如只读操作）
2. **哪些操作永远需要确认，不可绕过？** → 用 `decisionReason.type === 'safetyCheck'` 标记
3. **无人值守场景（CI/后台 agent）怎么处理？** → `shouldAvoidPermissionPrompts = true` + 跑 hooks + 自动 deny

## Minimal Pattern

```typescript
// 最简实现：三层规则 + 工具自检
type Rule = { toolName: string; content?: string; behavior: 'allow' | 'deny' | 'ask' }

type PermissionContext = {
  mode: 'default' | 'bypassPermissions' | 'acceptEdits'
  allowRules: Rule[]
  denyRules: Rule[]
  askRules: Rule[]
}

async function checkPermission(toolName: string, input: unknown, ctx: PermissionContext) {
  if (ctx.denyRules.some(r => matches(r, toolName, input))) return 'deny'
  if (ctx.askRules.some(r => matches(r, toolName, input))) return 'ask'
  if (ctx.mode === 'bypassPermissions') return 'allow'
  if (ctx.allowRules.some(r => matches(r, toolName, input))) return 'allow'
  return 'ask'  // default: prompt
}
```

## Boundaries

This skill owns:
- 权限决策流水线的设计与实现
- 分层规则来源（policySettings → session）的优先级架构
- 工具级安全属性接口设计（`isReadOnly` / `isDestructive` / `isConcurrencySafe` / `checkPermissions` + fail-closed 默认值）
- Hook 系统的配置格式和生命周期事件
- AI 分类器 + Denial 追踪的 circuit breaker 模式
- 危险操作硬编码黑名单的设计原则

This skill does not own:
- 具体工具的业务逻辑（只关注权限接口）
- UI 确认弹框的实现（只关注决策结果）
- 用户认证/身份校验（不同于工具权限）
- AI 分类器的具体 prompt 工程

## When More Detail Is Needed

- 完整 TypeScript 类型定义 → `references/permission-types.ts`
- 决策流水线带注释的详细实现 → `references/permission-pipeline.md`
- Denial 追踪 circuit breaker 完整代码 → `references/denial-tracking.ts`
- Hook 系统架构与所有事件类型 → `references/hook-system.md`
- settings.json 配置完整示例 → `references/settings-examples.json`
