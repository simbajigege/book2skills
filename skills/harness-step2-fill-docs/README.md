# Harness Step 2 — Fill docs/ with Real Content

Turn skeleton docs into a genuine knowledge base by deep-reading your code.

After `harness-step1` creates the `docs/` structure, this skill digs into the actual codebase — reading entry points, module boundaries, dependency declarations, and naming patterns — and fills every doc file with specific, accurate content grounded in what the code actually does.

## What It Does

- Deep-scans the codebase: entry files, module boundaries, `package.json` / `pyproject.toml`, existing docs
- Writes `docs/ARCHITECTURE.md`: module map, dependency direction rules, main data flows
- Writes `docs/CONVENTIONS.md`: file naming patterns, variable/function naming, directory organization — each rule backed by a real code example
- Writes `docs/TECH_DECISIONS.md`: why each major framework/library was chosen (inferred from usage; unknown reasons marked "待补充")
- Writes `docs/QUALITY.md`: project-specific Definition of Done, code review checklist, test requirements
- Adds entries to `docs/exec-plans/tech-debt-tracker.md` for anything found during the scan (TODOs, inconsistencies, oversized files, untested core modules)
- Never invents content — anything that can't be inferred is marked "待补充" and surfaced to the user

## When to Use It

Use this skill right after `harness-step1`, or whenever the docs/ files feel too generic and need to reflect the actual codebase.

Trigger phrases: "填充文档内容", "完善 docs/ 文件", "让文档有实质内容", "分析项目写架构文档", "写 ARCHITECTURE.md", "写技术决策文档", "fill in the docs", "analyze codebase and write docs".

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/harness-step2-fill-docs
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## Prerequisites

Project must already have `AGENTS.md` and a `docs/` directory skeleton (created by `harness-step1-create-agent-md`).

After running this skill, continue with:
- **Step 3** (`harness-step3-session-management`): Create `tasks.json`, `progress.md`, `init.sh` for cross-session state

## File Structure

```
harness-step2-fill-docs/
├── SKILL.md          # Main skill instructions
└── README.md         # This file
```

## License

Apache 2.0 — Original work. See LICENSE.
