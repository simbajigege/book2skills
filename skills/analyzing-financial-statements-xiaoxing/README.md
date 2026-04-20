# Analyzing Financial Reports

A multi-module skill for reading Chinese public company financial statements and uncovering the real quality behind the numbers. Based on *一本书读懂财报* (Reading Financial Statements) by Professor Xiao Xing of Tsinghua University.

## What It Does

- Assesses **asset quality**: what balance sheet items actually represent in the real world
- Verifies **profit authenticity**: distinguishes earned profits from manufactured ones
- Evaluates **cash flow health**: whether operating cash tracks reported profits
- Measures **solvency and turnover ratios**: debt risk and operational efficiency
- Delivers a **composite ROIC-based verdict**: is this a genuinely good company?

## When to Use It

Trigger this skill when a user:
- Provides a company name or ticker and asks "is this financially healthy?"
- Shares financial data and wants to know if a metric looks normal for the industry
- Suspects accounting manipulation or wants to spot red flags
- Wants a holistic investment quality assessment across all three financial statements

## Module Structure

| Module | Focus |
|--------|-------|
| M1 Industry Analysis | Sets the industry baseline — all other analysis is relative to this |
| M2 Asset & Debt Analysis | Asset quality, receivables, inventory, fixed assets |
| M3 Profit Analysis | Revenue recognition, expense smoothing, profit authenticity |
| M4 Cash Flow Analysis | Operating cash vs. net income divergence |
| M5 Solvency Analysis | Turnover ratios, leverage, repayment risk |
| M6 ROIC Composite | Integrates all modules into a buy/avoid verdict |

## Installation

### Option 1 — CLI (recommended)

```bash
npx skills add simbajigege/book2skills/skills/analyzing-financial-reports
```

### Option 2 — Manual upload

1. Download the skill folder (or clone this repo).
2. In Claude.ai, go to **Settings → Skills** and upload the folder.
3. The skill will appear in your available skills list.

## File Structure

```
analyzing-financial-reports/
├── SKILL.md                          # Main orchestrator
├── README.md                         # This file
├── LICENSE.txt                       # License
└── subskills/
    ├── m1_industry_analysis/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m2_asset_debt_analysis/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m3_profit_analysis/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m4_cashflow_analysis/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m5_solvency_analysis/
    │   ├── module.md
    │   └── references/case_library.md
    └── m6_roic_analysis/
        ├── module.md
        └── references/case_library.md
```

## License

This skill contains distilled knowledge from *一本书读懂财报* by Xiao Xing (Tsinghua University Press, 2019 revised edition). It is not a verbatim reproduction. For personal and educational use only. Please support the original author.
