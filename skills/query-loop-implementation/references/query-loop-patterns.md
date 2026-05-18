# Query Loop Patterns

## ReAct to Query Loop Mapping

| ReAct concept | Production query loop |
|---|---|
| Thought | model reasoning or hidden thinking block |
| Action | structured tool/function call |
| Observation | structured tool result message |
| Answer | assistant response with no tool calls |

The production loop does not need to parse "Thought" text. The API response already tells the runtime whether the model wants to use a tool.

## Recommended Module Boundaries

```text
ConversationManager
  - durable messages
  - session persistence
  - user settings and auth
  - total usage and budget

QueryLoop
  - per-turn state
  - model call
  - tool call detection
  - continuation decisions
  - terminal reasons

ToolRuntime
  - tool registry
  - schema validation
  - permission checks
  - tool execution
  - tool_result formatting
```

## Continuation Decision

Continue only when the model produced at least one tool call:

```text
if tool_calls.length === 0:
  return completed
else:
  execute tools
  append tool_results
  call model again
```

This is the engineering equivalent of "the model saw the observation and thought again."

## Tool Result Shape

Use the provider's native shape. Conceptually it must carry:

```ts
{
  role: "tool",
  tool_call_id: call.id,
  content: serializedResult,
  is_error?: boolean
}
```

If the provider expects tool results as user-role content blocks, preserve the provider's exact pairing rules.

## Safety Checklist

- Every model-produced tool input is schema-validated.
- Risky tools require explicit permission or policy approval.
- Tool results are size-limited before being appended to history.
- Tool errors are formatted for model recovery when safe.
- Fatal errors terminate the loop with a clear terminal reason.
- `maxTurns` is mandatory.
- Abort signals propagate into model calls and tools.
- Long-running tools emit progress or are moved to background tasks.
- Message persistence happens before expensive/long-running calls when the host product owns persistence.

## Common Failure Modes

- Infinite loop because `maxTurns` is missing.
- Tool errors are thrown instead of returned, so the model cannot self-correct.
- Tool output is too large and blows the next prompt.
- Tool results are appended in the wrong provider role/shape.
- Parallel tool calls produce mismatched call/result ids.
- Permission checks happen after side effects.
- Final answer detection depends on text heuristics instead of "no tool calls."
