---
name: common-sense-index-investing-bogle
description: Apply John Bogle index investing rules for low-cost funds, asset allocation,
  fees, taxes, ETFs, advisers, and buy-hold discipline.
license: Skill distillation for personal/educational use. Do not reproduce source
  passages verbatim.
---


# The Little Book of Common Sense Investing — Index Investing Skill

**Knowledge source:** *The Little Book of Common Sense Investing* by John C. Bogle.

## Overview

Use this skill to evaluate investment fund choices, portfolio simplicity, cost drag, index fund discipline, asset allocation, and buy-hold behavior using Bogle's common-sense investing framework. It is educational decision support, not personalized financial advice.

## When to Use This Skill

Use this skill when the user asks:
- "Should I use an index fund or active fund?"
- "Are these fund fees too high?"
- "How should I think about ETFs, smart beta, or advisers?"
- "What stock/bond allocation is sensible?"
- "Am I overcomplicating my portfolio?"

## Core Principle

Own the broad market at very low cost and hold it for the long term. Before costs, investors collectively earn the market return; after costs, the more they pay intermediaries, trade, and chase winners, the less they keep.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Steps | Output | Independent trigger? | Distinct references? | Triage score | Should be subskill? | Reason |
|---|---|---|---|---|---|---:|---:|---|---|
| Fund comparison | "Which fund should I choose?" | Fees, turnover, strategy, benchmark, tax status | Compare cost, diversification, active risk, simplicity | Fund verdict | Yes | Yes | 3 | No | Primary index-investing workflow. |
| Cost drag analysis | "Do fees matter?" | Expense ratio, turnover, horizon | Estimate compounding drag | Cost warning | Yes | Yes | 3 | No | Same decision report. |
| Asset allocation | "How much stocks/bonds?" | Age, horizon, risk capacity, income need | Apply simple stock/bond discipline | Allocation range | Yes | Yes | 3 | No | Fits the same portfolio policy. |
| Product skepticism | "Should I buy ETF/smart beta/adviser pick?" | Product structure, costs, incentives | Check complexity, trading temptation, conflicts | Use/avoid verdict | Yes | Yes | 3 | No | Same Bogle cost/simplicity lens. |

## Architecture Justification

The workflows are askable separately, but Bogle's method is intentionally simple: cost, broad diversification, tax efficiency, and patient holding are inseparable. A single-file skill preserves the "simplicity and parsimony" rule.

## DIMENSION 1: Broad Market Ownership

**The Rule:** Prefer owning the entire market through a low-cost traditional index fund over trying to select winners.

### Key questions to ask:
- Is the fund broadly diversified or making a narrow bet?
- Does it eliminate stock-picking, sector, and manager risk?
- Is the investor seeking market return or chasing alpha?

### Decision criteria / Checklist:
- Broad-market exposure.
- Low tracking error to the intended market.
- No unnecessary sector, style, or manager concentration.
- Clear role in the portfolio.

### Warning signals:
- Fund selection based on recent outperformance.
- Concentrated funds marketed as safer than they are.
- Complexity presented as sophistication.

### Agent instruction:
When reviewing a fund, first determine whether it gives broad, low-cost market ownership or introduces avoidable active risk.

## DIMENSION 2: Cost Matters

**The Rule:** Costs are the most reliable predictor of investor outcomes because every dollar paid to intermediaries is a dollar not compounding for the owner.

### Key questions to ask:
- What expense ratio, trading cost, tax cost, advisory fee, and spread apply?
- How long will the investor hold it?
- Does higher cost buy a reliably higher net return?

### Decision criteria / Checklist:
- Compare total all-in cost.
- Penalize turnover and tax inefficiency.
- Treat low cost as a durable advantage.
- In bonds, apply extra cost sensitivity because expected returns are lower.

### Warning signals:
- Ignoring small annual fees over long horizons.
- Adviser recommendations biased toward high-cost products.
- Performance claims shown before costs, taxes, or survivorship bias.

### Agent instruction:
Always run cost analysis before accepting a performance story.

## DIMENSION 3: Reversion and Performance Chasing

**The Rule:** Past fund winners usually revert; chasing them turns a winner's game into a loser's game.

### Key questions to ask:
- Is the user selecting based on recent performance?
- Are failed funds excluded from the track record?
- Is the fund's alpha statistically and economically durable after costs?

### Decision criteria / Checklist:
- Examine long periods, not hot streaks.
- Watch for survivorship bias.
- Prefer repeatable structure over manager story.
- Assume excess return is rare and competed away.

### Warning signals:
- Top-quartile fund rankings used as buying triggers.
- High turnover after disappointing performance.
- Smart beta marketed as guaranteed outperformance.

### Agent instruction:
When a user cites performance, test whether it is durable, net of costs, and free of survivorship bias.

## DIMENSION 4: Simple Allocation and Holding Discipline

**The Rule:** Decide stock/bond allocation, keep costs low, rebalance, and hold through cycles.

### Key questions to ask:
- What horizon, income need, and risk capacity does the investor have?
- Is the portfolio simple enough to maintain?
- Does ETF trading flexibility tempt speculation?

### Decision criteria / Checklist:
- Use a simple stock/bond mix appropriate to risk capacity.
- Favor buy-hold implementation.
- Rebalance by policy, not emotion.
- Be cautious with ETFs that invite trading.

### Warning signals:
- Trading index products as if they were speculation vehicles.
- Portfolio crowded with overlapping funds.
- Changing allocation after market moves rather than life or risk changes.

### Agent instruction:
For allocation questions, give ranges and rebalancing discipline, not market forecasts.

## Query Response Framework

### Query Type 1: Compare funds
1. List each fund's exposure, cost, turnover, tax efficiency, and complexity.
2. Apply broad-market and cost tests.
3. Identify conflicts or performance-chasing risks.
4. Give Bogle-style verdict: prefer, avoid, simplify, or needs data.

### Query Type 2: Portfolio simplification
1. Identify current holdings and overlaps.
2. Reduce to broad low-cost building blocks.
3. Propose stock/bond policy and rebalancing rule.

### Query Type 3: Cost or adviser review
1. Map all explicit and hidden costs.
2. Estimate compounding drag qualitatively or quantitatively if data exists.
3. Recommend lower-cost alternatives where appropriate.

## Output Format

```markdown
## Bogle Common-Sense Investing Review
**Decision:** ...
**Verdict:** Prefer index / Avoid active cost / Simplify / Needs data

| Test | Finding | Result |
|---|---|---|

## Portfolio or Fund Recommendation
...

## Cost Discipline
...

## Citations
...
```

## Critical Reminders

1. Investors as a group receive market return minus costs.
2. Broad diversification eliminates avoidable selection risks.
3. Low cost is a durable edge.
4. Past performance is not a reliable selection method.
5. ETFs can be good tools but bad behavior enablers.

## CITATION RULES

Every substantive Bogle-method claim must include a citation to the original text.

**Quote files:**
- `cost-matters-quotes.md` — costs, taxes, performance chasing, bond costs, speculative return, survivorship bias, ETFs, and Graham margin of safety.
- `index-fund-quotes.md` — owning the market, common sense, cost hypothesis, alpha, arithmetic, eliminated risks, reversion, simplicity, and investor underperformance.
- `investing-wisdom-quotes.md` — buy-and-hold, dividends, allocation, timeless advice, Gotrocks, smart beta, adviser conflicts, and simplicity.

**Citation format:**

> "Author's exact words here."
>
> — [*The Little Book of Common Sense Investing*, cited excerpt](https://github.com/simbajigege/book2skills/blob/main/skills/common-sense-index-investing-bogle/quotes/FILENAME.md#ANCHOR)

**Anchor mapping:**
- `cost-matters-quotes.md`: `#tyranny-of-costs`, `#two-percent-costs`, `#taxes-are-costs`, `#past-performance-no-guarantee`, `#bond-costs-even-worse`, `#speculative-return`, `#survivorship-bias`, `#etf-trading-danger`, `#graham-margin-of-safety`
- `index-fund-quotes.md`: `#own-entire-market`, `#common-sense-investing`, `#cost-matters-hypothesis`, `#alpha-negative-sum`, `#relentless-arithmetic`, `#we-get-what-we-dont-pay-for`, `#index-fund-eliminates-risks`, `#reversion-to-mean`, `#simplicity-majesty`, `#investments-perform-better-than-investors`
- `investing-wisdom-quotes.md`: `#buy-hold-prosper`, `#dividends-best-friend`, `#asset-allocation-critical`, `#time-tested-advice`, `#gotrocks-parable`, `#smart-beta-costs`, `#advisers-conflicts`, `#keep-it-simple`

**Rules:**
- Cite cost-related decisions with a cost anchor.
- Cite product or behavior warnings with ETF, adviser, smart-beta, or performance anchors.
- Do not provide personalized regulated advice; frame as educational policy.
