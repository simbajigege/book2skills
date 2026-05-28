# agent-memory-implementation

A Claude Code skill that restructures overgrown or chaotic memory files into the clean 2-layer architecture that Claude Code's `autoDream` system uses internally — keeping the always-loaded index lean while making deeper knowledge available on demand.

## What It Does

- Audits `MEMORY.md` for line-count violations, inline content, broken pointers, and stale entries
- Restructures topic files with proper frontmatter (`name`, `description`, `type`) so the auto-extraction agent can dedup correctly
- Deletes or corrects superseded memories in place — no archive directory
- Explains how Claude Code's forked extraction agent works so you can write memories that survive the next autoDream cycle

## When to Use It

Trigger this skill when:
- You say "clean up MEMORY.md" or "reorganize my memory files"
- MEMORY.md exceeds 200 lines (Claude Code truncates beyond this limit)
- The index contains full paragraphs instead of one-line pointers
- Memory files are missing frontmatter or have a vague `description` field
- You notice duplicate or conflicting memory files after a long project

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/agent-memory-implementation
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```
agent-memory-implementation/
├── SKILL.md                           # Main skill instructions
├── README.md                          # This file
├── references/
│   └── memory-type-definitions.md    # Verbatim type specs from memoryTypes.ts
└── scripts/
    └── memory_audit.py               # Diagnostic script: scans memory dir and reports issues
```

## License

Skill implementation guide for personal/educational use.
