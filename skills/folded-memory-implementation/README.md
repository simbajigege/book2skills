# folded-memory-implementation

A developer implementation guide for building hierarchical (folded) memory into a Claude Agent. Instead of a single flat summary, maintain three memory layers at different levels of detail — recent turns stay raw and detailed, older content compresses into episodes, and the oldest material distills into abstract semantic facts.

**Prerequisite**: understand `compact-memory-implementation` first. Folded memory extends the same fork-agent and trigger concepts.

## What It Does

- Implements a three-layer memory architecture: L1 (working), L2 (episodic), L3 (semantic)
- Provides ready-to-use Python dataclasses (`FoldedMemory`, `Episode`, `SemanticMemory`)
- Includes fork-agent prompts for L1→L2 episode compaction and L2→L3 semantic extraction
- Shows threshold detection (`maybe_fold()`), system prompt assembly, and cross-session persistence

## When to Use It

- "My agent needs to remember decisions from 10 sessions ago"
- "compact-memory-implementation isn't retaining enough — context overflows keep losing important history"
- "Build a long-running agent that accumulates domain knowledge without re-discovering it"
- "I need hierarchical / layered memory in my Claude agent"
- Agent runs for hundreds of turns across many sessions

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/folded-memory-implementation
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```
folded-memory-implementation/
├── SKILL.md          # Main skill instructions with full implementation guide
├── README.md         # This file
└── LICENSE.txt       # Usage terms
```

## License

Original implementation guide for developer use. Code examples are provided as-is for educational purposes.
