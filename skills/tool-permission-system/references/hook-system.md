# Hook 系统架构

> 源自 Claude Code `src/utils/hooks/` 和 `src/entrypoints/sdk/coreTypes.ts`

Hook 是在 agent 操作生命周期各节点预留的插座，让用户/企业插入自定义逻辑，而不需要修改 agent 核心代码。

---

## 生命周期事件（所有可挂钩的节点）

```typescript
const HOOK_EVENTS = [
  // 工具执行相关
  'PreToolUse',           // 工具执行前（可以拦截）
  'PostToolUse',          // 工具执行后（成功）
  'PostToolUseFailure',   // 工具执行后（失败）

  // 权限相关
  'PermissionRequest',    // 权限请求时（headless agent 用这个来决定 allow/deny）
  'PermissionDenied',     // 权限被拒绝时

  // 用户交互相关
  'UserPromptSubmit',     // 用户提交消息时

  // 会话生命周期
  'SessionStart',         // 会话开始
  'SessionEnd',           // 会话结束
  'Stop',                 // agent 完成回复
  'StopFailure',          // agent 回复失败

  // 子 agent
  'SubagentStart',        // 子 agent 启动
  'SubagentStop',         // 子 agent 结束

  // 上下文管理
  'PreCompact',           // 上下文压缩前
  'PostCompact',          // 上下文压缩后

  // 文件系统（Claude Code 特有）
  'FileChanged',          // 文件变更时
  'WorktreeCreate',       // 创建 git worktree
  'WorktreeRemove',       // 删除 git worktree
]
```

---

## Hook 的四种类型

### 1. `command` — 执行 shell 脚本

```json
{
  "type": "command",
  "command": "echo $CLAUDE_TOOL_INPUT | jq '.path' | xargs prettier --write",
  "shell": "bash",
  "timeout": 30000
}
```

- 退出码 0 → 通过
- 退出码 2 → block（工具不执行）
- 其他退出码 → 警告，继续执行
- stdout 输出会作为 context 添加给 agent

### 2. `prompt` — 让 agent 自己判断

```json
{
  "type": "prompt",
  "prompt": "Check if this file edit modifies any security-critical paths. If yes, output BLOCK."
}
```

适合需要上下文理解的判断（比 shell 脚本更灵活，但更慢）。

### 3. `agent` — 启动子 agent 处理

```json
{
  "type": "agent",
  "prompt": "Review this database query for SQL injection risks"
}
```

适合复杂的自动化审查，子 agent 有完整工具调用能力。

### 4. `http` — 发送 HTTP 请求

```json
{
  "type": "http",
  "url": "https://audit.internal/api/log",
  "method": "POST"
}
```

适合通知外部系统、写入审计日志、触发 webhook。

---

## Hook 的来源与优先级

```
policySettings   ← 企业强制（allowManagedHooksOnly=true 时，其余所有 hook 禁用）
userSettings     ← 用户全局 (~/.claude/settings.json)
projectSettings  ← 项目级 (.claude/settings.json)
localSettings    ← 本地私有 (.claude/settings.local.json)
pluginHook       ← 插件注册（最低优先级）
sessionHook      ← 当次会话临时 hook（通过 API 注册）
```

**关键：** `allowManagedHooksOnly = true` 时，用户/项目/本地的所有 Hook 配置都被忽略，只执行管理员下发的 Hook。这是企业合规场景的核心能力。

---

## 配置格式（settings.json）

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "audit-command.sh \"$CLAUDE_TOOL_INPUT_COMMAND\"",
            "if": "Bash(rm *)"
          }
        ]
      },
      {
        "matcher": "FileEdit",
        "hooks": [
          {
            "type": "command",
            "command": "if [[ '$CLAUDE_TOOL_INPUT_PATH' == *'/prod/'* ]]; then exit 2; fi"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "FileEdit",
        "hooks": [
          {
            "type": "command",
            "command": "prettier --write \"$CLAUDE_TOOL_INPUT_PATH\""
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "hooks": [
          {
            "type": "http",
            "url": "https://audit.internal/api/permission-request"
          }
        ]
      }
    ]
  }
}
```

---

## PermissionRequest Hook（特殊用途）

这个 Hook 专门用于 **headless/后台 agent** 场景，让外部系统决定是否允许工具调用：

```typescript
// Hook 返回结构
{
  permissionRequestResult: {
    behavior: 'allow' | 'deny',
    message?: string,
    updatedInput?: object,
    updatedPermissions?: PermissionUpdate[]  // 可顺带更新规则
  }
}
```

**工作流程：**
1. 后台 agent 遇到需要确认的操作
2. 无法弹出 UI 确认框（`shouldAvoidPermissionPrompts = true`）
3. 触发 `PermissionRequest` hook，等待外部系统响应
4. hook 返回 allow → 继续执行
5. hook 返回 deny（`interrupt: true`）→ 中止整个 agent
6. hook 无响应 → 自动 deny

---

## 环境变量（Hook 脚本可读取）

```bash
CLAUDE_TOOL_NAME           # 工具名，如 "Bash"、"FileEdit"
CLAUDE_TOOL_INPUT          # 工具输入（JSON 字符串）
CLAUDE_TOOL_INPUT_COMMAND  # Bash 工具：具体命令
CLAUDE_TOOL_INPUT_PATH     # 文件工具：文件路径
CLAUDE_SESSION_ID          # 当前会话 ID
CLAUDE_HOOK_EVENT          # 当前 hook 事件类型
```

---

## 实现建议

自建 Hook 系统的最简实现：

```typescript
type HookConfig =
  | { type: 'command'; command: string; timeout?: number }
  | { type: 'http';    url: string; method?: string }

type HookMatcher = {
  matcher?: string  // 工具名，undefined 表示匹配所有
  hooks: HookConfig[]
}

type HooksConfig = {
  PreToolUse?: HookMatcher[]
  PostToolUse?: HookMatcher[]
  PermissionRequest?: HookMatcher[]
  // ... 其他事件
}

async function runPreToolUseHooks(
  toolName: string,
  input: unknown,
  hooks: HooksConfig
): Promise<'allow' | 'block'> {
  const matchers = hooks.PreToolUse?.filter(
    m => !m.matcher || m.matcher === toolName
  ) ?? []

  for (const matcher of matchers) {
    for (const hook of matcher.hooks) {
      const result = await executeHook(hook, { toolName, input })
      if (result.exitCode === 2) return 'block'
    }
  }
  return 'allow'
}
```
