---
name: intelligent-investor-graham
description: Use Graham value investing for Is this investment or speculation, defensive
  stock screens, margin of safety, Mr. Market, allocation, funds, IPOs.
license: Skill distillation for personal/educational use. Do not reproduce source
  passages verbatim.
---


# The Intelligent Investor — Skill (Benjamin Graham)

**Knowledge source:** *The Intelligent Investor* by Benjamin Graham, revised edition with commentary by Jason Zweig.
**Architecture:** Orchestrator + 7 subskills. This file routes the user query; subskills execute the actual Graham workflows.

```text
intelligent-investor-graham/
├── SKILL.md
├── quotes/
│   ├── market-philosophy-quotes.md
│   └── value-investing-quotes.md
└── subskills/
    ├── m1_investment_vs_speculation/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m2_defensive_stock_screen/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m3_margin_of_safety_pricing/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m4_market_fluctuation_response/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m5_portfolio_policy/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m6_fund_adviser_ipo_review/
    │   ├── module.md
    │   └── references/case_library.md
    └── m7_enterprising_bargain_hunt/
        ├── module.md
        └── references/case_library.md
```

## Skill Purpose

Use this skill to apply Graham's value-investing discipline to practical investor decisions: distinguishing investment from speculation, screening defensive stocks, estimating margin of safety, responding to market swings, setting portfolio policy, evaluating funds or advisers, and searching for enterprising-investor bargains.

This is not a market-forecasting, momentum-trading, tax-planning, or personalized financial-advice skill. Its job is to force businesslike analysis, conservative arithmetic, and temperament discipline before any action is labeled an investment.

## When to Use This Skill

Invoke this skill when the user asks questions such as:

- "Is this stock worth buying under Graham's rules?"
- "Is this an investment or speculation?"
- "Does this company pass the defensive investor checklist?"
- "What price gives enough margin of safety?"
- "The stock or market dropped. Should I sell?"
- "How should I split my portfolio between stocks and bonds?"
- "Should I buy this fund, adviser product, IPO, SPAC, or hot growth story?"
- "How would Graham look for bargain stocks?"

## CITATION RULES

Every substantive Graham-method claim must cite the original-text quote files when a module produces a final answer.

**Quote files:**

- `quotes/value-investing-quotes.md` — investment definition, margin of safety, Mr. Market, defensive allocation, price discipline, Graham's core principles.
- `quotes/market-philosophy-quotes.md` — market pendulum, earnings skepticism, IPO warnings, index funds, adviser conflicts, net-current-asset bargains, simplicity, historical humility.

**Citation format:**

> "Author's exact words here."
>
> — [*The Intelligent Investor*, cited excerpt](https://github.com/simbajigege/book2skills/blob/main/skills/intelligent-investor-graham/quotes/FILENAME.md#ANCHOR)

**Anchor mapping:**

- `value-investing-quotes.md`: `#buffett-endorses-graham`, `#investment-vs-speculation`, `#margin-of-safety`, `#mr-market`, `#mr-market-servant`, `#defensive-portfolio-split`, `#price-matters-more`, `#graham-core-principles`, `#the-future-value-depends-on-price`, `#no-need-for-extraordinary`
- `market-philosophy-quotes.md`: `#market-is-a-pendulum`, `#earnings-can-be-manipulated`, `#avoid-ipos`, `#index-funds-best`, `#advisers-misaligned`, `#net-current-asset-bargains`, `#simplicity-beats-cleverness`, `#santayana-warning`

**Rules:**

- Read the routed module's `references/case_library.md` for the relevant quote IDs.
- Include at least one citation per major section in substantive answers.
- Use only exact quotes from the quote files. Do not invent quotation text.
- If no exact quote fits, cite the closest anchor and state that the reasoning is a paraphrased Graham application.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Steps | Output | Independent trigger? | Distinct references? | Triage score | Should be subskill? | Reason |
|---|---|---|---|---|---|---:|---:|---|---|
| Investment/speculation classification | "Is this trade investing?" | Security, thesis, holding period, analysis, leverage, position sizing | Test analysis, principal safety, adequate return, promotional dependence | Investment/speculation verdict and boundary conditions | Yes | Yes | 4 | Yes | Foundation for every proposed purchase or trade. |
| Defensive stock screen | "Does X pass Graham's defensive checklist?" | 10-year earnings, dividends, balance sheet, price, EPS, book value | Apply seven defensive criteria without soft averaging | Pass/fail table and disqualifiers | Yes | Yes | 4 | Yes | Distinct inputs, rules, and pass/fail artifact. |
| Margin of safety pricing | "What price is attractive?" | Normalized earnings, assets, book value, debt, bond yield, current price | Estimate conservative value, discount, and no-buy zone | Buy zone, watch zone, avoid zone | Yes | Yes | 4 | Yes | Distinct valuation artifact. |
| Market fluctuation response | "The stock dropped. Should I sell?" | Price change, business change, valuation, liquidity needs, leverage | Separate quotation from value; test impairment and forced-selling risk | Hold/add/reduce/sell framework | Yes | Yes | 4 | Yes | Distinct behavioral and sell-discipline workflow. |
| Portfolio policy | "How should I allocate?" | Investor type, income need, effort, risk capacity, yields | Start at 50/50, apply 25/75 guardrails, rebalance | Allocation range and rebalancing rule | Yes | Yes | 4 | Yes | Different input type and output artifact. |
| Fund/adviser/IPO review | "Should I buy this fund or IPO?" | Fees, incentives, operating history, marketing claims, alternatives | Check conflicts, costs, promotion, analyzable facts | Use/avoid verdict and safer default | Yes | Yes | 4 | Yes | Product review workflow with distinct warnings. |
| Enterprising bargain hunt | "How would Graham find cheap stocks?" | Screens, financials, NCAV data, special situation facts, diversification plan | Search low expectations, verify asset backing, diversify | Research list and rejection rules | Yes | Yes | 4 | Yes | Distinct research workflow and reference needs. |

## Routing Rules

| User question type | Must run | Optional run |
|---|---|---|
| "Should I buy stock X?" | M1 -> M2 -> M3 | M4 if price moved sharply; M7 if user is enterprising |
| "Is this investment or speculation?" | M1 | M6 if promoted product, IPO, fund, or adviser |
| "Does this pass Graham's checklist?" | M2 | M3 |
| "What is a Graham buy price?" | M3 | M2 for defensive qualification |
| "The stock fell. Should I sell?" | M4 | M3 to recalculate margin of safety |
| "How should I allocate my portfolio?" | M5 | M6 for fund implementation |
| "Should I use this fund/adviser/IPO/SPAC/hot issue?" | M6 | M1 |
| "Find Graham-style bargains" | M7 | M3 for valuation discipline; M1 for classification |

## Execution Rules

1. Read only the modules required by the routing table.
2. Run M1 first whenever the user proposes a purchase, trade, or speculative product.
3. Run M2 before calling a stock suitable for a defensive investor.
4. Run M3 before giving any buy-price, cheap/expensive, add, reduce, or margin-of-safety conclusion.
5. Run M4 for market-move questions; do not treat price movement itself as proof of risk or opportunity.
6. If required data is missing, state the missing fields and give a provisional analysis rather than fabricating figures.
7. Do not run every module for a narrow question.

## Multi-Module Output Format

```markdown
## Graham Analysis — [Security / Decision]

**Question type:** [Buy / sell / allocation / fund / speculation / bargain search]
**Investor posture:** Defensive / Enterprising / Unknown
**Required modules used:** M[ ] ...

### 1. Investment vs. Speculation
- Classification:
- Reason:
- Boundary conditions:
- Citation:

### 2. Graham Tests Applied
- Defensive checklist result, margin of safety, market fluctuation diagnosis, allocation policy, or product review as routed.

### 3. Verdict
- Graham result: qualifies / watchlist / avoid / speculative only / hold / reduce / needs data
- Action discipline:
- Missing data:

### 4. Citations
- Closest Graham principle and quote link for each major conclusion.
```

## Subskill Status

| Subskill | Path | Status |
|---|---|---|
| M1 Investment vs Speculation | `subskills/m1_investment_vs_speculation/` | Available |
| M2 Defensive Stock Screen | `subskills/m2_defensive_stock_screen/` | Available |
| M3 Margin of Safety Pricing | `subskills/m3_margin_of_safety_pricing/` | Available |
| M4 Market Fluctuation Response | `subskills/m4_market_fluctuation_response/` | Available |
| M5 Portfolio Policy | `subskills/m5_portfolio_policy/` | Available |
| M6 Fund Adviser IPO Review | `subskills/m6_fund_adviser_ipo_review/` | Available |
| M7 Enterprising Bargain Hunt | `subskills/m7_enterprising_bargain_hunt/` | Available |

## Do Not

- Do not forecast the market or interest rates as the basis for a recommendation.
- Do not call an action "investment" unless analysis, principal safety, and adequate return have all been addressed.
- Do not excuse overpayment because the company is excellent, popular, or fast growing.
- Do not average a failed defensive checklist into a soft "mostly passes" verdict.
- Do not recommend leverage, all-in allocations, or panic selling under Graham's name.
- Do not provide personalized regulated financial advice; frame outputs as educational decision support.
