# common-stocks-uncommon-profits

> A growth stock analysis Skill based on Philip Fisher's *Common Stocks and Uncommon Profits*

---

## About the Book

| | |
|---|---|
| **Title** | *Common Stocks and Uncommon Profits and Other Writings* |
| **Author** | Philip A. Fisher |
| **First Published** | 1958 (revised 1960) |
| **Significance** | Warren Buffett called it one of the most influential books on his investment philosophy |

---

## What This Skill Does

Once installed, you can ask Claude directly:

**Identifying Growth Stocks**
- "Is NVIDIA a growth stock?"
- "Analyze Apple using Fisher's criteria"
- "How does TSMC score on Fisher's 15 points?"

**Company Research**
- "How should I research BYD?"
- "How exactly does the Scuttlebutt method work?"
- "Who should I talk to in order to learn about this company?"

**Buy & Sell Timing**
- "Is now a good time to buy Tesla?"
- "Should I sell my Amazon stock?"
- "What should I do when the market crashes?"

**Avoiding Mistakes**
- "What does Fisher say are the most common investor mistakes?"
- "How many stocks should I hold?"
- "Does a high P/E mean a stock is overvalued?"

---

## Skill Structure

```
common-stocks-uncommon-profits/
├── SKILL.md                    # Core framework + routing logic (Level 1+2)
└── references/
    ├── fifteen-points.md       # Complete 15-point evaluation criteria
    ├── scuttlebutt.md          # Scuttlebutt research methodology
    ├── when-to-buy-sell.md     # Buy and sell timing judgment
    └── donts.md                # 10 investment don'ts + diversification rules
```

---

## Installation

```bash
npx skills add simbajigege/book2skills/skills/common-stocks-uncommon-profits-stock-pickup-phisher
```

### Claude.ai
Download `common-stocks-uncommon-profits.skill` from [Releases](../../../releases) and upload it in Settings → Features → Custom Skills.

### Claude Code
```bash
cp -r common-stocks-uncommon-profits .claude/skills/
```

### Any platform supporting the agentskills.io standard
Copy the `common-stocks-uncommon-profits/` folder to the platform's skills directory.

---

## Core Methodology Overview

### Fisher's 15 Points (Growth Stock Evaluation Framework)

| Category | Point | Key Question |
|----------|-------|-------------|
| Business Quality | 1. Market Potential | Can the product/service grow significantly for many years? |
| | 2. R&D Commitment | Is management committed to developing next-generation products? |
| | 3. R&D Effectiveness | What is the R&D return on investment? |
| | 4. Sales Capability | Does the company have an outstanding sales organization? |
| | 5. Profit Margins | Are profit margins above the industry average? |
| | 6. Margin Maintenance | What is the company doing to maintain/improve margins? |
| Management Quality | 7. Labor Relations | Are employee relations outstanding? |
| | 8. Executive Relations | Is the executive team atmosphere healthy? |
| | 9. Management Depth | Is there a deep management bench? |
| | 10. Cost Controls | Are cost analysis and accounting controls effective? |
| | 11. Industry-Specific Factors | Are there industry-specific competitive advantages? |
| | 12. Long-term Outlook | Does management have a long-term profit perspective? |
| Financial Health | 13. Dilution Risk | Will financing plans significantly dilute shareholder value? |
| | 14. Transparency | Does management communicate honestly even in difficult times? |
| **★ Most Important** | **15. Management Integrity** | **Is management's integrity beyond question?** |

> **Point 15 is the only veto** — if integrity is in doubt, eliminate the company immediately, regardless of how strong everything else looks.

---

## Acknowledgments

This Skill is based on a complete reading and systematic distillation of the original book. All core insights are credited to Philip A. Fisher.
