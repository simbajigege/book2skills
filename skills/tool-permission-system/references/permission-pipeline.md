# 权限决策流水线

> 源自 Claude Code `src/utils/permissions/permissions.ts`
> 提炼为通用 agent 工具权限设计参考

---

## 完整决策流程

```
Tool call request
     │
     ▼
┌──────────────────────────────────────────────────────┐
│ 1a. 整个工具是否在 deny rules 中？                      │
│     getDenyRuleForTool(context, tool)                 │
│     是 → 立即 deny，返回错误给 agent                    │
└────────────────────────┬─────────────────────────────┘
                         │ 否
                         ▼
┌──────────────────────────────────────────────────────┐
│ 1b. 整个工具是否在 ask rules 中？                       │
│     getAskRuleForTool(context, tool)                  │
│     是 → 返回 ask（强制弹框）                           │
└────────────────────────┬─────────────────────────────┘
                         │ 否
                         ▼
┌──────────────────────────────────────────────────────┐
│ 1c. 工具自身的 checkPermissions()                      │
│     工具内部逻辑（检查命令前缀、文件路径等）              │
│     → 返回 allow / deny / ask / passthrough           │
└────────────────────────┬─────────────────────────────┘
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
          deny           ↓          passthrough
         (1d)      ask + type?      (继续流水线)
                    ├── 'rule'  → 返回 ask（bypass免疫）(1f)
                    ├── 'safetyCheck' → 返回 ask（bypass免疫）(1g)
                    └── 其他 → 继续流水线
                         │
                         ▼
┌──────────────────────────────────────────────────────┐
│ 1e. 工具是否需要用户交互（requiresUserInteraction）？   │
│     是 → 返回 ask（bypass免疫）                         │
└────────────────────────┬─────────────────────────────┘
                         │ 否
                         ▼
┌──────────────────────────────────────────────────────┐
│ 2a. 当前模式是否为 bypassPermissions？                  │
│     是 → 立即 allow（跳过后续所有检查）                   │
└────────────────────────┬─────────────────────────────┘
                         │ 否
                         ▼
┌──────────────────────────────────────────────────────┐
│ 2b. 整个工具是否在 allow rules 中？                     │
│     toolAlwaysAllowedRule(context, tool)              │
│     是 → 立即 allow                                   │
└────────────────────────┬─────────────────────────────┘
                         │ 否
                         ▼
┌──────────────────────────────────────────────────────┐
│ 3. passthrough → 转换为 ask（默认需要用户确认）           │
└──────────────────────────────────────────────────────┘
```

---

## 外层包装（作用于上述流程之后）

上述流水线输出 `ask` 后，外层还有三种模式转换：

```
流水线输出 ask
    │
    ├── mode === 'dontAsk' → 转为 deny（返回 DONT_ASK_REJECT_MESSAGE）
    │
    ├── mode === 'auto' → 转给 AI 分类器：
    │     ├── 快速通道1: acceptEdits 模式下会通过的操作 → allow（跳过 classifier API 调用）
    │     ├── 快速通道2: 安全工具白名单（read-only tools）→ allow
    │     ├── AI 分类器判断 safe → allow
    │     ├── AI 分类器判断 unsafe → deny（并记录 denial）
    │     └── 连续拒绝3次或累计20次 → 回退到人工确认（circuit breaker）
    │
    └── shouldAvoidPermissionPrompts === true（后台 agent）→
          先跑 PermissionRequest hooks
          hooks 返回 allow/deny → 使用 hook 决策
          hooks 无响应 → 自动 deny（AUTO_REJECT_MESSAGE）
```

---

## 关键设计原则

### 1. Bypass 免疫的三种情况

以下情况即使在 `bypassPermissions` 模式下也会弹出确认框：

1. **`decisionReason.type === 'rule'` 且 `ruleBehavior === 'ask'`** — 用户明确设置了 `ask` 规则
2. **`decisionReason.type === 'safetyCheck'`** — 系统保护的危险路径（`.git/`、`.claude/`、shell 配置文件等）
3. **`tool.requiresUserInteraction()`** — 工具本身需要用户参与（如 `AskUserQuestion` 工具）

### 2. 规则匹配语义

```
"Bash"           → 匹配整个 Bash 工具（任何命令）
"Bash(git *)"    → 匹配 Bash 工具中以 "git " 开头的命令
"FileEdit(/src/*)" → 匹配编辑 /src/ 下任何文件
"mcp__server1"   → 匹配某个 MCP server 下的所有工具
```

### 3. 规则优先级

同一工具可能同时有多个来源的规则。优先级：policySettings > userSettings > projectSettings > localSettings > cliArg > command > session

但注意：**这不是"覆盖"逻辑，而是"都执行"逻辑**。deny rules 和 ask rules 各自独立检查，找到第一个匹配就返回，所以高优先级来源的 deny 规则总会优先于低优先级来源的 allow 规则生效。

### 4. passthrough vs ask 的区别

- `passthrough`：工具内部没有明确意见，交给外层决定
- `ask`：工具明确说"需要用户确认"，外层会保留这个决策

`passthrough` 在最终输出时会被转换为 `ask`，但在中间步骤（如 bypass 模式判断之前）保持 passthrough 状态，使得 bypass 模式可以跳过它。

---

## 实现清单

自建权限系统时需要实现的接口：

```typescript
interface Tool {
  name: string

  // 工具自身的权限检查（步骤 1c）
  checkPermissions(input: unknown, context: ToolUseContext): Promise<PermissionResult>

  // 是否需要用户交互（步骤 1e）
  requiresUserInteraction?(): boolean
}

interface ToolPermissionContext {
  mode: PermissionMode
  alwaysAllowRules: Record<PermissionRuleSource, string[]>
  alwaysDenyRules:  Record<PermissionRuleSource, string[]>
  alwaysAskRules:   Record<PermissionRuleSource, string[]>
  shouldAvoidPermissionPrompts?: boolean
}
```
