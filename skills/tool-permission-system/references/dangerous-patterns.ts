/**
 * 危险操作硬编码黑名单
 *
 * 这些命令如果出现在宽泛的 allow 规则中（如 Bash(python:*) 或 Bash(node:*)），
 * 等于允许 agent 通过解释器执行任意代码，完全绕过精细的权限检查。
 *
 * 用途：
 * 1. 进入高信任模式（如 auto mode）前，自动剥离这类宽泛规则
 * 2. 作为权限配置校验器的黑名单
 * 3. 生成安全审计报告时标记可疑规则
 *
 * 来源: src/utils/permissions/dangerousPatterns.ts (claude-code leaked 2026-03-31)
 */

/**
 * 跨平台危险命令（Unix + Windows 都存在）
 */
export const CROSS_PLATFORM_CODE_EXEC = [
  // 解释器（以 "interpreter:*" 形式出现在 allow rule 中等于任意代码执行）
  'python', 'python3', 'python2',
  'node',
  'deno',
  'tsx',
  'ruby',
  'perl',
  'php',
  'lua',
  // 包运行器（可以下载并执行任意 npm 包）
  'npx',
  'bunx',
  'npm run',
  'yarn run',
  'pnpm run',
  'bun run',
  // Shell（嵌套 shell = 任意命令执行）
  'bash',
  'sh',
  // 远程执行（ssh 执行远程命令）
  'ssh',
] as const

/**
 * Unix 额外危险命令
 */
export const DANGEROUS_BASH_PATTERNS: readonly string[] = [
  ...CROSS_PLATFORM_CODE_EXEC,
  'zsh', 'fish',    // 更多 shell
  'eval',           // 执行字符串为代码
  'exec',           // 替换当前进程
  'env',            // 可以注入环境变量执行命令
  'xargs',          // 把 stdin 作为命令参数执行
  'sudo',           // 权限提升
]

/**
 * 检查一条 allow rule 是否危险（是否包含可执行任意代码的命令前缀）
 *
 * 危险规则的形态：
 * - "Bash(python:*)"     → 允许所有 python 命令
 * - "Bash(node *)"       → 允许所有 node 命令
 * - "Bash(bash -c *)"    → 允许嵌套 bash
 */
export function isDangerousAllowRule(
  toolName: string,
  ruleContent: string,
  dangerousPatterns: readonly string[] = DANGEROUS_BASH_PATTERNS
): boolean {
  if (toolName !== 'Bash') return false

  return dangerousPatterns.some(pattern => {
    // 匹配 "pattern:*"、"pattern *"、"pattern" 等形态
    return (
      ruleContent === pattern ||
      ruleContent === `${pattern}:*` ||
      ruleContent.startsWith(`${pattern} `) ||
      ruleContent.startsWith(`${pattern}:`)
    )
  })
}

/**
 * 使用示例：进入 auto mode 前清理危险规则
 *
 * function stripDangerousRulesForAutoMode(context: ToolPermissionContext) {
 *   const strippedRules: string[] = []
 *   const cleanedAllowRules = { ...context.alwaysAllowRules }
 *
 *   for (const [source, rules] of Object.entries(context.alwaysAllowRules)) {
 *     cleanedAllowRules[source] = rules.filter(ruleString => {
 *       const { toolName, ruleContent } = parseRuleString(ruleString)
 *       if (ruleContent && isDangerousAllowRule(toolName, ruleContent)) {
 *         strippedRules.push(ruleString)
 *         return false  // 过滤掉危险规则
 *       }
 *       return true
 *     })
 *   }
 *
 *   return { cleanedContext: { ...context, alwaysAllowRules: cleanedAllowRules }, strippedRules }
 * }
 */
