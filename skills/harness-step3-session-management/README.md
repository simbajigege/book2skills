# Harness Step 3 — Session Management

Stop explaining "where we left off" at the start of every Claude session.

This skill creates three files that let any agent recover full working context in under 30 seconds: `init.sh` (environment health check), `tasks.json` (structured task queue), and `progress.md` (human-readable session log). State lives in files, not in the agent's memory.

## What It Does

- Generates `init.sh`: verifies dev environment (dependencies installed, configs present, smoke test passes) — run it at the start of every session to catch environment drift early
- Generates `tasks.json`: structured task list with `id`, `title`, `description`, `status`, `priority`, `verify` (executable check), and `requires_eval` (whether independent review is needed)
- Generates `progress.md`: append-only session log — each completed session adds one entry at the top
- Updates `AGENTS.md` with session startup protocol and task management rules
- Enforces a `verify` step per task: agents cannot mark a task `done` without running the check described in the `verify` field

## When to Use It

Use this skill after `harness-step1` and `harness-step2` are complete.

Trigger phrases: "建立任务管理", "让 agent 记住进度", "创建 tasks.json", "跨 session 保持状态", "agent 每次都不记得上次做了什么", "建立 progress 文件", "初始化状态管理", "set up session state", "create tasks.json".

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/harness-step3-session-management
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## Prerequisites

Project must have `AGENTS.md` and a filled-in `docs/` knowledge base (created by `harness-step1` and `harness-step2`).

This is **Step 3** of the Harness Engineering pipeline. The full sequence:
1. `harness-step1-create-agent-md` — create AGENTS.md + docs/ skeleton
2. `harness-step2-fill-docs` — fill docs/ with real content from the codebase
3. **`harness-step3-session-management`** ← you are here
4. `harness-step4-linter` — turn CONVENTIONS.md rules into enforced lint checks
5. `harness-step5-verify` — make task verify fields executable, not declarative

## File Structure

```
harness-step3-session-management/
├── SKILL.md          # Main skill instructions
└── README.md         # This file
```

## License

Apache 2.0 — Original work. See LICENSE.
