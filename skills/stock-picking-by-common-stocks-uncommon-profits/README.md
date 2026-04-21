# Common Stocks and Uncommon Profits — AI Skill

A multi-module AI skill that encodes Philip Fisher's complete growth stock investment methodology from *Common Stocks and Uncommon Profits* (1958). Fisher is one of history's greatest growth investors — Warren Buffett credits him alongside Benjamin Graham as the two thinkers who most shaped his own philosophy. This skill helps you evaluate whether any company meets Fisher's standards for a long-term growth investment.

## What It Does

- **15-Point Scorecard** — evaluates a company across all 15 Fisher criteria with ✅/⚠️/❌ ratings, including the non-negotiable integrity veto (Point 15)
- **Management Quality Analysis** — deep assessment of management depth, delegation, long-term orientation, and integrity using Fisher's frameworks
- **Scuttlebutt Intelligence** — guides you to gather competitive intelligence from customers, competitors, and suppliers — the way Fisher actually researched companies
- **Buy Timing** — applies Fisher's four buying opportunity types to determine whether now is the right moment to enter a position
- **Hold/Sell Decision** — tests your position against Fisher's only three valid reasons to sell

## When to Use It

Use this skill whenever you want to:
- Evaluate whether a company is a Fisher-quality growth stock
- Assess a management team's quality and long-term orientation
- Decide whether a stock's current decline is a buying opportunity or a warning sign
- Check whether you should hold or sell a position you already own
- Understand the Scuttlebutt research method

Trigger phrases: *"is X a growth stock"*, *"Fisher framework"*, *"15 points"*, *"scuttlebutt"*, *"should I buy X"*, *"should I sell X"*, *"management quality"*, *"growth stock analysis"*

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/stock-picking-by-common-stocks-uncommon-profits
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

### Option 3 — Download ZIP

Download the ZIP from [book2skills.com](https://book2skills.com/en/book/stock-picking-by-common-stocks-uncommon-profits) and upload directly to Claude.

## File Structure

```
stock-picking-by-common-stocks-uncommon-profits/
├── SKILL.md                              # Master dispatcher & routing rules
├── README.md                             # This file
├── LICENSE.txt                           # Usage license
└── subskills/
    ├── m1_fifteen_points/                # 15-Point evaluation framework
    │   ├── module.md
    │   └── references/case_library.md
    ├── m2_management/                    # Management quality deep analysis
    │   ├── module.md
    │   └── references/case_library.md
    ├── m3_scuttlebutt/                   # Competitive intelligence gathering
    │   ├── module.md
    │   └── references/case_library.md
    ├── m4_when_to_buy/                   # Entry timing judgment
    │   ├── module.md
    │   └── references/case_library.md
    └── m5_when_to_sell/                  # Hold/sell decision framework
        ├── module.md
        └── references/case_library.md
```

## Example Prompts

```
Is Microsoft a Fisher growth stock?
Is now a good time to buy Nvidia?
Should I sell my Tesla position?
How do I research a company using scuttlebutt?
Analyze Apple using Fisher's 15-point framework
```

## Source

Distilled from *Common Stocks and Uncommon Profits and Other Writings* by Philip A. Fisher (1958, revised 1996). Published by book2skills.com — [view the skill page](https://book2skills.com/en/book/stock-picking-by-common-stocks-uncommon-profits).

## License

See `LICENSE.txt`. This skill contains distilled knowledge from the source listed above. It is not a verbatim reproduction. For personal and educational use.
