---
name: query-loop-implementation
description: Implement a production-ready LLM query loop / agent loop for AI applications. Use this skill whenever the user wants to add tool calling, ReAct-style reasoning-action-observation cycles, function calling loops, query engines, agent runtimes, tool_result feedback, max-turn exits, or Claude Code-like Agent Loop behavior to their own product or codebase.
---

# Query Loop Implementation

## Core Idea

Build the loop as product infrastructure, not prompt glue:

```text
ConversationManager -> QueryLoop -> ToolRuntime
```

- `ConversationManager` owns durable state: session id, messages, user settings, budget, persistence.
- `QueryLoop` owns one task turn: call model, detect tool calls, execute tools, append tool results, repeat.
- `ToolRuntime` owns registered tools: schemas, permission checks, execution, error formatting.

Use ReAct as the mental model:

```text
Thought -> Action -> Observation -> Thought -> Answer
```

Implement it as structured API traffic:

```text
model thinking/text -> tool_call -> tool_result -> next model call -> final text
```

## Implementation Workflow

1. Inspect the user's stack and current LLM call site.
   Find where messages are built, where the model is called, and whether tool/function calling is already configured.

2. Introduce a minimal query loop.
   Keep the first version narrow: one model call function, one tool registry, explicit exit conditions.

3. Normalize message shapes.
   Use the provider's structured tool-call format when available. Avoid parsing free-form `Action:` text unless the provider has no function/tool-calling API.

4. Add tool execution safety.
   Validate tool input against a schema, apply permission checks for risky tools, wrap failures as tool results, and log every call.

5. Add exit and budget guards before expanding features.
   Always include `maxTurns`, timeout/cancel support, token/cost budget checks, and a fatal-error path.

6. Keep context-window strategy outside this skill.
   Accept `messages` as loop input and return updated `messages`, but leave trimming, retrieval, summarization, and compaction to a separate context-management layer.

## Minimal Loop

Adapt this shape to the user's language and SDK:

```ts
async function runQueryLoop({
  initialMessages,
  model,
  tools,
  maxTurns = 10,
  signal,
}: {
  initialMessages: Message[]
  model: ModelClient
  tools: ToolRegistry
  maxTurns?: number
  signal?: AbortSignal
}) {
  let messages = [...initialMessages]

  for (let turn = 1; turn <= maxTurns; turn++) {
    if (signal?.aborted) return { status: "aborted", messages }

    const response = await model.generate({
      messages,
      tools: tools.definitions(),
      signal,
    })

    messages.push(response.message)

    const toolCalls = extractToolCalls(response.message)
    if (toolCalls.length === 0) {
      return {
        status: "completed",
        finalMessage: response.message,
        messages,
      }
    }

    for (const call of toolCalls) {
      const result = await tools.execute(call, { signal, messages })
      messages.push(makeToolResultMessage(call.id, result))
    }
  }

  return { status: "max_turns", messages }
}
```

The "model continues judging" step is not a separate function. It happens when the loop calls the model again after appending `tool_result` messages.

## Required Exit Conditions

Implement these before shipping:

- **Normal completion**: the model response has no tool calls.
- **Max turns**: stop after a fixed number of model-tool cycles.
- **Abort/timeout**: stop when the user cancels or the request exceeds its deadline.
- **Permission denied**: stop or return a tool error depending on the product's safety policy.
- **Budget exceeded**: stop when token, cost, or runtime budget is exhausted.
- **Fatal tool error**: stop when a tool failure cannot be corrected by the model.

Prefer returning structured terminal reasons:

```ts
type TerminalReason =
  | "completed"
  | "max_turns"
  | "aborted"
  | "timeout"
  | "permission_denied"
  | "budget_exceeded"
  | "fatal_tool_error"
```

## Tool Runtime Contract

Each tool should define:

```ts
type Tool = {
  name: string
  description: string
  inputSchema: unknown
  risk: "read" | "write" | "execute" | "external"
  validate(input: unknown): ValidatedInput
  canUse(input: ValidatedInput, ctx: ToolContext): Promise<PermissionDecision>
  call(input: ValidatedInput, ctx: ToolContext): Promise<ToolResult>
}
```

Execution order:

```text
find tool by name
-> schema validate model input
-> run tool-specific validation
-> check permission
-> call tool
-> format success or error as tool_result
```

Return tool errors to the model when it can plausibly recover, for example invalid arguments, file not found, empty search result, or transient API errors. Stop the loop for security violations, repeated failures, missing credentials, or budget exhaustion.

## Product Design Guidance

Keep "intelligence" in the model and "reliability" in code:

- Let the model decide whether it needs another tool call.
- Let code enforce schemas, permissions, budgets, and loop exits.
- Keep prompts focused on tool semantics and task policy.
- Keep implementation focused on deterministic control flow.

For simple AI apps, avoid subagents, worktrees, and streaming tool execution at first. Add them only when the product actually needs parallel work, isolation, or long-running tasks.

## When More Detail Is Needed

Read `references/query-loop-patterns.md` when designing a new query engine, reviewing an existing implementation, or explaining ReAct-to-query-loop architecture to another engineer.
