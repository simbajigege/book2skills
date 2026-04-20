# Common Stocks and Uncommon Profits — Philip Fisher Skill

A multi-module skill that applies Philip Fisher's growth stock investment framework to any company evaluation. Based on *Common Stocks and Uncommon Profits and Other Writings* (1958, revised 1996).

Fisher's core philosophy: find a small number of truly outstanding companies, research them deeply, and hold them almost indefinitely.

## What It Does

- Scores a company against Fisher's **15 Points** checklist — the definitive framework for identifying durable growth businesses
- Evaluates **management quality**: depth of talent, long-term orientation, and integrity
- Guides **Scuttlebutt intelligence gathering**: how to learn more from competitors, customers, and suppliers than from analyst reports
- Identifies the right **moment to buy**: when to act on a qualified company's temporary price weakness
- Applies Fisher's three **hold/sell criteria**: when to exit, and the far more common reasons not to

## When to Use It

Trigger this skill when a user:
- Wants to evaluate whether a company is a worthy long-term growth investment
- Asks about management quality, R&D commitment, or sales organization strength
- Wants to know how to gather competitive intelligence on a company
- Is deciding whether to buy a growth stock and unsure about timing
- Is considering selling a current position
- Mentions Philip Fisher, the 15 Points, scuttlebutt, or growth stock investing
- Asks "when is the best time to buy this?" or "should I sell it?"

## Module Structure

| Module | Focus |
|--------|-------|
| M1 — 15 Points | Systematic company quality scorecard |
| M2 — Management | Depth, integrity, and long-term orientation |
| M3 — Scuttlebutt | Competitive intelligence methodology |
| M4 — When to Buy | Entry timing: catching temporary price dislocations |
| M5 — When to Sell | Three sell criteria; why holding is usually right |

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/common-stocks-uncommon-profits-stock-pickup-phisher
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```
common-stocks-philip-fisher/
├── SKILL.md                          # Main orchestrator
├── README.md                         # This file
├── LICENSE.txt                       # License
└── subskills/
    ├── m1_fifteen_points/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m2_management/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m3_scuttlebutt/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m4_when_to_buy/
    │   ├── module.md
    │   └── references/case_library.md
    └── m5_when_to_sell/
        ├── module.md
        └── references/case_library.md
```

## License

This skill contains distilled knowledge from *Common Stocks and Uncommon Profits and Other Writings* by Philip A. Fisher. It is not a verbatim reproduction. For personal and educational use only. Please support the original author.
