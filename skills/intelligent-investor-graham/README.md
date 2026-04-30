# The Intelligent Investor

This skill distills *The Intelligent Investor* by Benjamin Graham into an agent-ready decision-support workflow for investing, value investing, margin of safety.

## What It Does

- Applies the book's core framework to practical user questions.
- Provides checklists, routing rules, warning signs, and output formats.
- Uses quote anchors for source-grounded citations.
- Keeps source passages in `quotes/` rather than workflow prose.

## When to Use It

Use this skill for questions involving investing, value investing, margin of safety, portfolio policy, especially when the user wants a structured diagnosis, critique, or decision framework.

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/intelligent-investor-graham
```

### Option 2 — Manual upload

1. Download the skill folder or clone this repo.
2. In Claude.ai, go to Settings -> Skills and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```text
intelligent-investor-graham/
├── SKILL.md
├── README.md
├── LICENSE.txt
├── quotes/
└── subskills/
```

## License

Skill distillation for personal/educational use. Do not reproduce source passages verbatim.
