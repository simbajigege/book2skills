# Query Loop Implementation

Add a production-ready LLM query loop to AI applications.

This skill helps engineers implement the core agent runtime pattern behind tool calling: call the model, detect structured tool calls, execute tools safely, append tool results, and continue until the model returns a final answer or a guard stops the loop.

## What It Does

- Defines clean boundaries between `ConversationManager`, `QueryLoop`, and `ToolRuntime`
- Provides a minimal loop shape for model calls, tool execution, tool result feedback, and final answer detection
- Specifies required exit conditions: max turns, abort/timeout, permission denial, budget limits, and fatal tool errors
- Gives a tool runtime contract with schema validation, permission checks, execution, and recoverable error formatting

## When to Use It

Use this skill whenever you want to add tool calling, ReAct-style reasoning-action-observation cycles, function calling loops, query engines, agent runtimes, `tool_result` feedback, max-turn exits, or Claude Code-like agent loop behavior to an AI product or codebase.

Trigger phrases include: "add tool calling", "build an agent loop", "implement a query loop", "function calling loop", "ReAct loop", "tool_result feedback", "max turns", and "Claude Code-like agent runtime".

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/query-loop-implementation
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings -> Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```text
query-loop-implementation/
├── SKILL.md                         # Main skill instructions
├── README.md                        # This file
├── LICENSE                          # Apache 2.0 license
├── agents/
│   └── openai.yaml                  # Display metadata for OpenAI/Codex-style agents
└── references/
    └── query-loop-patterns.md       # Expanded implementation patterns and failure modes
```

## License

Apache 2.0 — Original work. See LICENSE.
