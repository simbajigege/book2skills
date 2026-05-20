# memory-architect

A Claude Code skill that restructures a chaotic or overgrown `MEMORY.md` into the 2-layer architecture that Claude Code's internal `autoDream` service (`services/autoDream/`) is designed to work with. Stale, superseded, or contradicted memories are deleted or corrected in place — not archived. The result is a healthy, always-current memory directory.

## What It Does

- Audits MEMORY.md line count and detects bloat (inline content, entries past line 200 that never load)
- Identifies topic files missing `name`/`description`/`type` frontmatter (the extraction agent uses `description` for deduplication — missing it causes duplicate writes)
- Merges near-duplicate topic files covering the same subject from different sessions
- Deletes superseded entries (checks against current codebase state, not just age)
- Converts relative dates to absolute dates ("last week" → specific date)
- Reports before/after line counts, files created/merged/deleted, and any contradictions resolved

## When to Use It

- "Clean up MEMORY.md" / "reorganize my memory files"
- "MEMORY.md is getting too long" / "fix my memory structure"
- When you observe MEMORY.md exceeds 200 lines
- When MEMORY.md contains paragraphs instead of one-line pointers
- When you notice duplicate topic files from different sessions
- Periodically (every 1–2 weeks) after heavy Claude Code use

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/memory-architect
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```
memory-architect/
├── SKILL.md    # Main skill instructions
├── README.md   # This file
└── LICENSE.txt
```

## License

Skill distillation for personal/educational use. Do not reproduce source passages verbatim.
