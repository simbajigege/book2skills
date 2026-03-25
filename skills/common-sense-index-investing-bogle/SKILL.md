---
name: common-sense-index-investing-bogle
description: "Applies Bogle's index fund framework to investment decisions. Use when evaluating index vs active funds, fund costs, stock/bond allocation, or performance-chasing risk."
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

## Overview

This skill distills John Bogle's *The Little Book of Common Sense Investing* into an agent-ready decision framework. It covers fund selection, cost evaluation, asset allocation, and the case for index investing. Intended for individual investors, financial advisors, and anyone evaluating their portfolio strategy.

## When to Use This Skill

- User asks whether to use index funds vs. actively managed funds
- User is comparing mutual fund options and wants a cost-based analysis
- User asks about asset allocation between stocks and bonds
- User is tempted by a "hot" fund or recent top-performer
- User asks "is this fund manager worth it?" or "should I follow past performance?"
- User asks about long-term wealth building strategy
- User asks about ETFs vs. traditional index funds
- User asks about retirement investing or target-date funds

## Core Principle

**The relentless rules of humble arithmetic:** Investors as a group must earn exactly the market return before costs. After costs, they must earn less. Therefore, the only guaranteed way to capture your fair share of market returns is to own the entire market at the lowest possible cost — a traditional index fund held forever. Attempting to beat the market is a loser's game; it enriches Wall Street at the expense of Main Street investors.

---

## DIMENSION 1: The Cost Imperative

**The Rule:** Every dollar paid in fees, commissions, and turnover costs is a dollar permanently removed from your compounding wealth — costs are the single most reliable predictor of long-term fund performance.

### Key questions to ask:
- What is the fund's expense ratio? (Target: under 0.10% for index funds; 0.80%+ is high)
- What is the portfolio turnover rate? (Each 100% turnover ≈ 1% additional hidden cost)
- Are there sales loads (front-end or back-end)? Any 12b-1 marketing fees?
- What is the total all-in cost (expense ratio + estimated turnover cost)?
- How does the cost compare to a no-load total market index fund?

### Decision criteria / Checklist:
- ✅ Expense ratio ≤ 0.10% → strong pass
- ✅ No sales load, no 12b-1 fee → strong pass
- ⚠️ Expense ratio 0.10%–0.50% → marginal; check turnover
- ❌ Expense ratio > 0.50% + high turnover → very likely to underperform long-term
- ❌ Sales load of any kind → permanent drag on returns; nearly always avoidable

### Warning signals:
- "Only" 1–2% annual fee sounds trivial but destroys 40–60% of terminal wealth over 50 years (compounding costs)
- Funds marketed on 3-year or 5-year "star ratings" — Morningstar stars reflect past performance, not future results
- High-cost funds claiming their managers justify the fee — 85–90% of active managers fail to beat their benchmark after costs
- Any fund promising alpha through complexity, proprietary models, or "smart beta" — adds cost, not reliable outperformance

### Agent instruction:
When user asks about a specific fund or compares funds, always compute or request the total annual cost (expense ratio + estimated turnover cost). Show the compounding impact over 10, 20, and 30 years using Bogle's framework: a 2% annual cost penalty on a $10,000 investment at 7% market return leaves the investor with $114,700 instead of $294,600 over 50 years — a 61% wealth destruction.

---

## DIMENSION 2: The Index Fund Advantage

**The Rule:** Owning all publicly traded businesses in the market through a broad, low-cost index fund mathematically guarantees capturing the market's return; active stock-picking and fund selection are negative-sum games after costs.

### Key questions to ask:
- Does the fund aim to match the total market, or to beat it through selection?
- What percentage of active funds in this category have outperformed a comparable index over 15 years? (SPIVA data: typically <20%)
- Has survivorship bias been corrected? (Failed funds disappear, inflating reported active fund averages)
- Over 1970–2016, only 2 of 355 equity funds outperformed by ≥2%/year — what's the probability this fund is one of them?

### Decision criteria / Checklist:
- ✅ Total stock market index fund or S&P 500 index fund → highest probability of long-term success
- ✅ Broadly diversified (holds hundreds to thousands of securities) → eliminates company-specific risk
- ⚠️ Sector or factor index funds → narrow diversification; higher risk
- ❌ Actively managed fund with no clear cost or performance edge → default to index alternative

### Warning signals:
- Any claim of "consistent outperformance" — past outperformance predicts nothing; it mostly reflects luck or timing
- Fund with large asset base chasing small-cap alpha — size kills outperformance
- Fund manager tenure under 5 years — average tenure is ~9 years; you inherit a stranger's record
- "This time is different" market conditions justifying active management — the math never changes

### Agent instruction:
When user asks whether to choose an active fund, look up or ask for its 10–15 year return vs. its benchmark index. Apply survivorship-bias correction: most underperforming funds have already been liquidated. The burden of proof lies entirely with the active fund. Default recommendation: total stock market index fund unless clear evidence contradicts.

---

## DIMENSION 3: Business Returns vs. Speculative Returns

**The Rule:** Long-term stock market returns come from real business fundamentals (dividend yield + earnings growth = investment return); short-term price movements (speculative return) are unpredictable and mean-revert to zero over time.

### Key questions to ask:
- What is the current dividend yield of the market? What is expected long-term earnings growth?
- Has the current P/E ratio expanded significantly (adding temporary speculative return)? If so, future returns may be lower.
- Is the user trying to time the market based on price expectations, or invest based on business fundamentals?
- What is the "investment return" component (dividends + earnings growth) vs. the "speculative return" component (P/E expansion/contraction)?

### Decision criteria / Checklist:
- ✅ Invest for the long-term business return (historically ~9%/year: 4.4% dividend + 4.6% earnings growth, 1900–2016)
- ✅ Ignore short-term price fluctuations — the voting machine becomes a weighing machine over time
- ⚠️ If P/E is historically elevated, expect future total returns lower than the historical average
- ❌ Market timing based on P/E forecasts or economic predictions — speculative return is unpredictable

### Warning signals:
- Current P/E significantly above historical average (~15x) — speculative return has likely been pulled forward
- Investor extrapolating recent high returns into the future — includes a speculative component that will revert
- Panic selling in a downturn — locks in losses before business fundamentals reassert themselves

### Agent instruction:
When user asks "is now a good time to invest?" or "should I wait for the market to drop?", apply this dimension. Calculate the likely investment return (current dividend yield + consensus long-term earnings growth estimate). Acknowledge that speculative return is unknowable. Remind the user that time in the market beats timing the market, and that the investment return component is reliable over decades.

---

## DIMENSION 4: Reversion to the Mean

**The Rule:** Yesterday's top-performing funds become tomorrow's average or below-average performers — selecting funds based on past returns is not only unhelpful but counterproductive.

### Key questions to ask:
- Is the user choosing this fund because it recently outperformed?
- Has this fund's top-quintile record been sustained across multiple non-overlapping periods?
- What drove the outperformance — manager skill, lucky sector concentration, or style tailwind?
- Has the fund grown significantly in assets since its peak performance? (Size kills alpha)

### Decision criteria / Checklist:
- ✅ If fund selection is required, prefer consistently low-cost funds over top-returning funds
- ✅ Expect that top-quintile funds revert to average within 5 years, with near-random distribution across quintiles
- ❌ Do not chase 3-year or 5-year star ratings — these are mirrors, not windows
- ❌ Do not use Morningstar stars or "best funds" lists as primary selection criteria

### Warning signals:
- 5-star fund rated on trailing 3/5/10-year returns → exactly what NOT to buy (peak already in)
- Fund with massive recent inflows chasing past returns → subsequent investor returns always lower than fund returns
- Media coverage of a "hot" manager or "hot" sector → usually indicates the speculative peak

### Agent instruction:
When user is evaluating a fund based on recent returns, show the reversion-to-mean pattern: in Bogle's 5-year quintile studies (2001–2016), top-quintile funds showed essentially random distribution in the subsequent period. Ask: "Is there a structural, cost-based reason to expect this fund to outperform — or are you reacting to its recent return?" Redirect to cost-based selection.

---

## DIMENSION 5: Asset Allocation — Stocks vs. Bonds

**The Rule:** The single most important investment decision is how to divide assets between stocks and bonds; asset allocation explains ~94% of long-term return differences, and a low-cost allocation beats a high-cost one even at lower risk.

### Key questions to ask:
- What is the investor's time horizon? (Longer → more stocks)
- What is the investor's ability to take risk? (Financial position, future liabilities, years to retirement)
- What is the investor's willingness to take risk? (Can they hold steady through a 40–50% drawdown?)
- Is the investor near or in retirement? (Consider capital preservation over growth)

### Decision criteria / Checklist:
- ✅ General starting point: 50% stocks / 50% bonds; range of 75/25 to 25/75 based on personal factors
- ✅ Simple rule of thumb: bond % ≈ your age; remainder in stocks (adjustable for risk tolerance)
- ✅ Low-cost index funds for both components — cost savings can offset a more conservative allocation
- ⚠️ High equity allocation (>75%) only if investor has 20+ year horizon AND can stomach full market drawdowns
- ❌ 100% equity allocation for retirees drawing income — sequence-of-returns risk is devastating

### Warning signals:
- Chasing equity-heavy allocations during bull markets — recency bias; risk tolerance evaporates in crashes
- Ignoring bonds because yields are "too low" — bonds provide rebalancing fuel and volatility buffer
- Complex multi-asset allocation with dozens of funds — rarely outperforms a simple 2-fund index portfolio
- High-cost balanced or lifecycle funds — cost drag can negate the allocation benefit

### Agent instruction:
When user asks about asset allocation, establish their time horizon and risk tolerance first. Then show Bogle's key insight: a 25/75 stock/bond portfolio using low-cost index funds (0.05%/0.10%) can produce a *higher net return* than a 75/25 portfolio using high-cost active funds (2%/1%) — because cost savings compound powerfully. Present a two-fund portfolio recommendation (total stock market index + total bond market index) as the default.

---

## Query Response Framework

### Query Type 1: "Should I invest in [specific active fund]?" or "Is this fund worth it?"
1. Apply Dimension 1: Extract expense ratio + turnover cost → compute 20/30-year wealth impact
2. Apply Dimension 2: What is its 15-year record vs. benchmark? Correct for survivorship bias
3. Apply Dimension 4: Has it been a recent top-performer? Flag RTM risk
4. Output: Cost comparison table (active fund vs. total market index equivalent), long-term wealth projection, recommendation

### Query Type 2: "How should I allocate my portfolio?" or "How much should I hold in stocks vs. bonds?"
1. Establish time horizon and risk tolerance (Dimension 5 questions)
2. Apply Dimension 5: Derive starting allocation (50/50 baseline, adjust for age/risk)
3. Apply Dimension 1: Show how low-cost index funds can achieve same return at lower risk than high-cost alternatives
4. Output: Recommended allocation range, two-fund index portfolio, cost comparison at chosen allocation

### Query Type 3: "Is now a good time to invest?" or "Should I wait for a correction?"
1. Apply Dimension 3: Separate investment return (dividends + earnings growth) from speculative return (P/E movements)
2. Apply Dimension 2: Time in market > timing the market — compounding begins at first dollar invested
3. Output: Expected investment return estimate, reminder that speculative return is unpredictable, recommendation to invest consistently regardless of market level

### Query Type 4: "This fund was top-rated last year — should I buy it?"
1. Apply Dimension 4: Show RTM pattern — top quintile funds distribute randomly in subsequent periods
2. Apply Dimension 1: What are the costs? Active selection plus high fees is a double penalty
3. Apply Dimension 2: What is the structural edge, if any? If none, recommend index fund
4. Output: RTM illustration, cost analysis, alternative index fund recommendation

---

## Output Format

When responding to investment queries, use this structure:

```
## Analysis: [Fund/Question]

### Cost Impact
| Item | Active Fund | Index Fund |
|------|------------|------------|
| Expense ratio | X% | 0.04–0.10% |
| Est. turnover cost | X% | ~0% |
| Total annual drag | X% | ~0.05% |
| 30-year wealth on $10,000 | $X | $X |

### Performance Reality
- 15-year record vs. benchmark: [data or N/A]
- Survivorship-corrected assessment: []
- RTM risk: [High / Medium / Low]

### Verdict
> [One-sentence actionable conclusion]

**Recommended action:** [Specific, concrete next step]
```

For asset allocation queries, add a **Portfolio Blueprint** section with the specific two-fund recommendation and allocation percentages.

---

## Critical Reminders

1. **Costs are arithmetic certainty; returns are not.** Every analysis must start with costs — they are the only variable the investor fully controls.
2. **The market is a zero-sum game before costs, and a negative-sum game after costs.** By owning the whole market cheaply, you convert it back to a positive-sum game.
3. **Don't just stand there — do something is Wall Street's motto. Don't do something — just stand there is the investor's motto.** Inaction (holding an index fund) is almost always the right move.
4. **Past performance is a mirror, not a window.** Never select a fund based on trailing returns without examining costs and RTM risk.
5. **Compounding cuts both ways.** The same exponential math that builds wealth through returns destroys it through costs. A 2% annual cost drag eliminates 61% of terminal wealth over 50 years.
6. **Asset allocation > fund selection.** The choice between stocks and bonds matters more than which specific fund within each asset class.
7. **Simplicity beats complexity.** A two-fund portfolio (total stock market index + total bond market index) at lowest cost outperforms nearly all sophisticated alternatives over the long term.
8. **The investor's enemy is not the market — it is themselves.** Behavioral mistakes (performance chasing, panic selling, over-trading) destroy more wealth than market volatility.
