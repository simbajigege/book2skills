/**
 * Tool Permission System — Core Types
 *
 * 从 Claude Code 源码提炼的完整权限类型体系。
 * 可直接作为自建 agent 权限系统的类型定义参考。
 *
 * 来源: src/types/permissions.ts (claude-code leaked 2026-03-31)
 */

// ============================================================================
// 权限模式（总开关）
// ============================================================================

export type PermissionMode =
  | 'default'           // 每个危险操作都弹确认框
  | 'acceptEdits'       // 文件修改自动通过，命令仍需确认
  | 'plan'              // 先列计划，用户审批后执行
  | 'bypassPermissions' // 完全不询问，自动执行一切（CI/脚本）
  | 'dontAsk'           // 把所有 ask 转为 deny（后台 agent 用）
  | 'auto'              // AI 分类器自动判断（实验性，内部）

// ============================================================================
// 规则行为（每条规则的效果）
// ============================================================================

export type PermissionBehavior = 'allow' | 'deny' | 'ask'

// ============================================================================
// 规则来源（优先级从高到低）
// ============================================================================

export type PermissionRuleSource =
  | 'policySettings'  // 企业管理员下发，用户无法覆盖（最高优先级）
  | 'userSettings'    // 用户全局 (~/.agent/settings.json)
  | 'projectSettings' // 项目级 (.agent/settings.json，可提交 git)
  | 'localSettings'   // 本地私有 (.agent/settings.local.json)
  | 'cliArg'          // 启动参数
  | 'command'         // 运行时命令动态设置
  | 'session'         // 当次会话临时生效

// ============================================================================
// 规则值（一条规则的内容）
// ============================================================================

export type PermissionRuleValue = {
  toolName: string       // 工具名，如 "Bash"、"FileEdit"
  ruleContent?: string   // 可选的工具特定内容，如 "git *"、"/src/*"
}

// 完整规则 = 规则值 + 来源 + 行为
export type PermissionRule = {
  source: PermissionRuleSource
  ruleBehavior: PermissionBehavior
  ruleValue: PermissionRuleValue
}

// ============================================================================
// 权限上下文（运行时状态）
// ============================================================================

export type ToolPermissionContext = {
  readonly mode: PermissionMode
  readonly alwaysAllowRules: Partial<Record<PermissionRuleSource, string[]>>
  readonly alwaysDenyRules:  Partial<Record<PermissionRuleSource, string[]>>
  readonly alwaysAskRules:   Partial<Record<PermissionRuleSource, string[]>>
  readonly shouldAvoidPermissionPrompts?: boolean  // true = 后台/无交互模式
  // 追加的工作目录（文件工具用于判断路径是否在允许范围内）
  readonly additionalWorkingDirectories: ReadonlyMap<string, { path: string; source: PermissionRuleSource }>
}

// ============================================================================
// 决策原因（用于 UI 展示 + 日志）
// ============================================================================

export type PermissionDecisionReason =
  | { type: 'rule';        rule: PermissionRule }                       // 匹配到规则
  | { type: 'mode';        mode: PermissionMode }                       // 模式决定
  | { type: 'hook';        hookName: string; reason?: string }          // Hook 拦截
  | { type: 'classifier';  classifier: string; reason: string }         // AI 分类器
  | { type: 'safetyCheck'; reason: string; classifierApprovable: boolean } // 安全路径保护
  | { type: 'asyncAgent';  reason: string }                             // 后台 agent 自动 deny
  | { type: 'other';       reason: string }

// ============================================================================
// 权限决策（流水线最终输出）
// ============================================================================

export type PermissionAllowDecision = {
  behavior: 'allow'
  updatedInput?: Record<string, unknown>  // 工具可修改输入（如规范化路径）
  decisionReason?: PermissionDecisionReason
}

export type PermissionAskDecision = {
  behavior: 'ask'
  message: string
  decisionReason?: PermissionDecisionReason
  suggestions?: PermissionUpdate[]  // 建议用户添加哪条规则
}

export type PermissionDenyDecision = {
  behavior: 'deny'
  message: string
  decisionReason: PermissionDecisionReason
}

// 流水线内部中间状态（工具 checkPermissions 可返回，最终会转换为 ask）
export type PermissionPassthrough = {
  behavior: 'passthrough'
  message: string
  decisionReason?: PermissionDecisionReason
}

export type PermissionDecision =
  | PermissionAllowDecision
  | PermissionAskDecision
  | PermissionDenyDecision

export type PermissionResult = PermissionDecision | PermissionPassthrough

// ============================================================================
// 权限更新（用户确认后如何持久化新规则）
// ============================================================================

export type PermissionUpdateDestination =
  | 'userSettings'
  | 'projectSettings'
  | 'localSettings'
  | 'session'
  | 'cliArg'

export type PermissionUpdate =
  | { type: 'addRules';    destination: PermissionUpdateDestination; rules: PermissionRuleValue[]; behavior: PermissionBehavior }
  | { type: 'replaceRules'; destination: PermissionUpdateDestination; rules: PermissionRuleValue[]; behavior: PermissionBehavior }
  | { type: 'removeRules'; destination: PermissionUpdateDestination; rules: PermissionRuleValue[]; behavior: PermissionBehavior }
  | { type: 'setMode';     destination: PermissionUpdateDestination; mode: PermissionMode }
