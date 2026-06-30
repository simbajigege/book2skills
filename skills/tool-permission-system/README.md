# Tool Permission System

Design and implement a layered, configurable permission/safety system for agent tools.

This skill helps engineers build the permission pipeline that runs before every tool call in an AI agent: a single place that decides auto-allow, ask the user, or deny. The pipeline is layered so enterprise admins, users, project teams, and individual sessions can each contribute rules, with higher layers overriding lower ones, and it is extensible through a hook system.

## What It Does

- Specifies a single permission pipeline (deny → ask → tool self-check → safety checks → bypass → allow → default prompt) that every tool call passes through
- Defines layered rule sources (`policySettings → userSettings → projectSettings → localSettings → cliArg → command → session`) with a clear override order
- Defines a fail-closed tool safety interface (`isReadOnly` / `isDestructive` / `isConcurrencySafe` / `checkPermissions`) where undeclared attributes default to the most conservative assumption, plus a `safetyCheck` mechanism that stays immune to bypass modes
- Covers the hook system configuration format and lifecycle, plus an AI-classifier denial-tracking circuit breaker for unattended runs

## When to Use It

Use this skill when building an agent that needs to control which tool calls are auto-allowed, which require user confirmation, and which are denied — especially when the system must be configurable across multiple scopes (project / user / enterprise) and extensible via hooks.

Trigger phrases include: "权限系统", "工具安全", "tool permission", "permission system", "tool safety", "allow/deny rules", "hook system", and "构建安全机制".

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/tool-permission-system
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```text
tool-permission-system/
├── SKILL.md                         # Main skill instructions
├── README.md                        # This file
├── LICENSE                          # Apache 2.0 license
├── agents/
│   └── openai.yaml                  # Display metadata for OpenAI/Codex-style agents
└── references/
    ├── permission-types.ts          # Full TypeScript type definitions
    ├── permission-pipeline.md       # Annotated decision pipeline implementation
    ├── denial-tracking.ts           # Denial-tracking circuit breaker code
    ├── dangerous-patterns.ts        # Hardcoded dangerous-operation blocklist
    ├── hook-system.md               # Hook architecture and event types
    └── settings-examples.json       # Complete settings.json configuration examples
```

## License

Apache 2.0 — Original work. See LICENSE.
