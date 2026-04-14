# Harness Step 1 — Create AGENTS.md & docs/

Give any Claude Code agent a permanent memory of your project — in one shot.

This skill scans your codebase and produces two things: a concise `AGENTS.md` that acts as a table of contents, and a `docs/` knowledge base (ARCHITECTURE, CONVENTIONS, TECH_DECISIONS, QUALITY, exec-plans). Every future agent session reads these files instead of rediscovering the project from scratch.

## What It Does

- Scans project structure (up to 3 levels), tech stack, entry points, and existing docs
- Generates `AGENTS.md` (~100 lines) — the single file an agent reads first in every session
- Creates `docs/ARCHITECTURE.md`, `docs/CONVENTIONS.md`, `docs/TECH_DECISIONS.md`, `docs/QUALITY.md`
- Creates `docs/exec-plans/` with `backlog.md` and `tech-debt-tracker.md`
- Marks anything it can't infer as "待补充" (to be filled in by a human) — never invents facts

## When to Use It

Use this skill whenever you want to:
- Add agent support to an existing project for the first time
- Help Claude Code understand your codebase without repeated explanations
- Start "Harness Engineering" — building a permanent agent knowledge layer
- Create AGENTS.md, set up docs/, or make AI work better in your repo

Trigger phrases: "为项目添加 agent 支持", "创建 AGENTS.md", "让 Claude Code 更好地工作", "开始 harness engineering", "搭建 agent 文档结构", "add agent support", "create AGENTS.md".

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/harness-step1-create-agent-md
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## Prerequisites

None. This is the **first step** in the Harness Engineering pipeline.

After running this skill, continue with:
- **Step 2** (`harness-step2-fill-docs`): Deep-read the code and fill in the docs with real content
- **Step 3** (`harness-step3-session-management`): Create `tasks.json`, `progress.md`, `init.sh` for cross-session state

## File Structure

```
harness-step1-create-agent-md/
├── SKILL.md          # Main skill instructions
└── README.md         # This file
```

## License

Apache 2.0 — Original work. See LICENSE.
