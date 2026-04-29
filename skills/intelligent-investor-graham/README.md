# Intelligent Investor Graham

This skill applies Benjamin Graham's value-investing framework from *The Intelligent Investor* for investors who want disciplined decision support around speculation, defensive stock selection, margin of safety, market swings, portfolio policy, funds, advisers, IPOs, and bargain hunting.

## What It Does

- Classifies proposed actions as investment, speculation, or mixed under Graham's definition.
- Runs modular workflows for defensive stock screens, margin-of-safety pricing, Mr. Market responses, and allocation policy.
- Reviews funds, advisers, IPOs, promoted ideas, and enterprising-investor bargain candidates.
- Uses quote-backed citation rules and module reference libraries for traceable Graham-method answers.

## When to Use It

Use this skill when a user asks questions such as "Is this investment or speculation?", "Does this stock pass Graham's defensive checklist?", "What price gives enough margin of safety?", "Should I sell after a market drop?", "How should I allocate between stocks and bonds?", or "Should I buy this fund, adviser product, IPO, or hot issue?"

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/intelligent-investor-graham
```

### Option 2 — Manual upload

1. Download the skill folder or clone this repo.
2. In Claude.ai, go to **Settings -> Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```text
intelligent-investor-graham/
├── SKILL.md          # Main orchestrator instructions
├── README.md         # This file
├── LICENSE.txt       # Book-distillation license note
├── quotes/           # Citation quote files
└── subskills/        # Modular Graham workflows
```

## License

Skill distillation for personal/educational use. Do not reproduce source passages verbatim.
