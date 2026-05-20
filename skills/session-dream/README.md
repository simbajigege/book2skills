# session-dream

A Claude Code skill that triggers on-demand memory distillation at the end of a session. It mirrors the logic of Claude Code's built-in `autoDream` background service — scanning the current conversation for key decisions, failed approaches, new discoveries, and blockers, then writing structured topic files to your project's memory directory.

Use it when a productive session is wrapping up and you don't want insights lost to context compaction.

## What It Does

- Scans the current conversation for high-value learnings worth preserving
- Creates or updates typed memory topic files (`feedback`, `project`, `user`, `reference`)
- Keeps `MEMORY.md` pruned and under the 200-line limit
- Reports which files were written and what was distilled

## When to Use It

Activate this skill by saying any of the following:

- `dream`
- `/dream`
- `save session memories`
- `distill this session`
- `what should I remember from this session?`
- Or naturally at the end of a long productive session

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/session-dream
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```
session-dream/
├── SKILL.md          # Main skill instructions
├── README.md         # This file
└── LICENSE.txt       # License
```

## License

This skill encodes the autoDream memory distillation pattern from Claude Code. Free for personal and educational use.
