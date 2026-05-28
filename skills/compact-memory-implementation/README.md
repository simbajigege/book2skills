# compact-memory-implementation

A developer implementation guide for adding **compact memory** to an Agent built with the Claude API or Claude Agent SDK. Covers the full pipeline: when to trigger compaction, how to fork a dedicated compactor sub-agent, what JSON schema to produce, and how to restore the compact in the next session.

## What It Does

- Provides copy-paste Python code for a token-threshold trigger, a forked compactor, and session persistence
- Specifies a structured JSON compact schema that captures task state, key decisions, eliminated approaches, and next steps
- Shows two injection patterns: system prompt injection (recommended) and first-message injection for stateless callers
- Explains how to chain compacts across sessions without accumulating stale context

## When to Use It

Trigger this skill when a developer:
- Asks "how do I implement compact memory in my agent?"
- Needs to manage context window limits in a long-running or multi-session agent
- Wants agents that resume with full reasoning context, not just current state
- Is building with the Anthropic API (`anthropic` SDK) or Claude Agent SDK

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/compact-memory-implementation
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```
compact-memory-implementation/
├── SKILL.md          # Main skill instructions (7-step developer guide with full code)
├── README.md         # This file
└── scripts/
    └── pre_compact_extract.py   # Helper: extract draft compact from session JSONL
```

## License

Skill implementation guide for personal/educational use.
