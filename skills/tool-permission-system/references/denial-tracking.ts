/**
 * Denial Tracking — Circuit Breaker for AI Permission Classifiers
 *
 * 当使用 AI 分类器自动判断工具权限时，分类器可能过于保守，
 * 导致用户频繁被打断。这个模块是安全阀：
 *
 * - 连续拒绝 3 次 → 回退到人工确认
 * - 累计拒绝 20 次 → 回退到人工确认（重置后继续）
 *
 * 任何一次"允许"都会重置连续拒绝计数器。
 *
 * 来源: src/utils/permissions/denialTracking.ts (claude-code leaked 2026-03-31)
 */

export type DenialTrackingState = {
  consecutiveDenials: number  // 连续拒绝次数（允许后重置）
  totalDenials: number        // 本次会话累计拒绝次数
}

export const DENIAL_LIMITS = {
  maxConsecutive: 3,   // 连续拒绝 3 次后回退
  maxTotal: 20,        // 累计拒绝 20 次后回退（重置后继续）
} as const

export function createDenialTrackingState(): DenialTrackingState {
  return { consecutiveDenials: 0, totalDenials: 0 }
}

export function recordDenial(state: DenialTrackingState): DenialTrackingState {
  return {
    consecutiveDenials: state.consecutiveDenials + 1,
    totalDenials: state.totalDenials + 1,
  }
}

export function recordSuccess(state: DenialTrackingState): DenialTrackingState {
  if (state.consecutiveDenials === 0) return state  // 无变化，返回原引用（避免触发状态更新）
  return { ...state, consecutiveDenials: 0 }
}

export function shouldFallbackToPrompting(state: DenialTrackingState): boolean {
  return (
    state.consecutiveDenials >= DENIAL_LIMITS.maxConsecutive ||
    state.totalDenials >= DENIAL_LIMITS.maxTotal
  )
}

/**
 * 使用示例（在 AI 分类器决策后调用）：
 *
 * const denialState = getDenialState()
 *
 * if (classifierSaysBlock) {
 *   const newState = recordDenial(denialState)
 *   saveDenialState(newState)
 *
 *   if (shouldFallbackToPrompting(newState)) {
 *     // circuit breaker 触发，回退到人工确认
 *     return { behavior: 'ask', message: '分类器连续拒绝，请人工审核' }
 *   }
 *   return { behavior: 'deny', message: classifierReason }
 * } else {
 *   const newState = recordSuccess(denialState)
 *   saveDenialState(newState)
 *   return { behavior: 'allow' }
 * }
 */

/**
 * 设计说明：
 *
 * 1. 为什么连续拒绝 3 次就回退？
 *    连续拒绝说明分类器对当前工作流有系统性误判，不是偶发性的。
 *    3 次是"可能误判"和"真的有问题"之间的经验阈值。
 *
 * 2. 为什么累计 20 次也回退？
 *    防止分类器在一个长会话中缓慢积累大量拒绝，逐渐架空用户的控制权。
 *    20 次是"今天工作量足够大"的信号。
 *
 * 3. 为什么 recordSuccess 在 consecutiveDenials === 0 时返回原引用？
 *    避免触发框架的状态更新机制，减少不必要的 re-render/re-sync。
 *
 * 4. headless/后台 agent 的特殊处理：
 *    当 shouldAvoidPermissionPrompts === true 时，达到 denial limit 不是
 *    回退到人工确认，而是直接 throw AbortError 终止整个 agent。
 *    因为无交互环境下"回退到人工确认"没有意义。
 */
