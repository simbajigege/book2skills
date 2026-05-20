# compact-with-memory

An enhanced `/compact` for Claude Code that treats context compression as a memory opportunity. Before summarizing, it extracts the session's institutional knowledge — architectural decisions, eliminated approaches, collaboration rules — and persists them to `MEMORY.md`. After compression, future sessions can reconstruct the *reasoning* behind current state, not just the state itself.

## What It Does

- Scans existing `MEMORY.md` before writing to avoid duplicate entries
- Classifies session signals into four types: `feedback` (collaboration rules), `project` (decisions and eliminated approaches), `user` (role and preferences), `reference` (external system pointers)
- Writes structured topic files with `name`, `description`, `type` frontmatter and `**Why:**` / `**How to apply:**` rationale
- Prunes the MEMORY.md index to stay under the 200-line load budget
- Then runs standard `/compact`

## When to Use It

- When the user types `/compact` or says "compress context" / "compact the conversation"
- When the context window indicator is approaching the limit
- At natural session checkpoints after significant architectural decisions
- Any time you want to preserve "why we chose this" reasoning across sessions

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/compact-with-memory
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```
compact-with-memory/
├── SKILL.md    # Main skill instructions
├── README.md   # This file
└── LICENSE.txt
```

## License

Skill distillation for personal/educational use. Do not reproduce source passages verbatim.
