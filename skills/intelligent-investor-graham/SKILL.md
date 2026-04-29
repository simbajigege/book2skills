---
name: intelligent-investor-graham
description: "Apply Graham value investing to stock screening, margin of safety, Mr. Market, portfolio allocation, and investment vs speculation questions."
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

## Overview

This skill applies Benjamin Graham's framework from *The Intelligent Investor* to practical investing decisions. It helps users evaluate whether an action is investment or speculation, screen stocks for defensive investors, estimate margin of safety, respond to market fluctuations, and choose a disciplined stock/bond allocation.

Use it as a decision-support tool for long-term, businesslike investing. Do not use it to forecast markets, chase momentum, justify leverage, or provide personalized regulated financial advice.

## When to Use This Skill

Use this skill whenever the user asks questions such as:

- "Is this stock worth buying under Graham's rules?"
- "Does this company pass the defensive investor checklist?"
- "What price would give me a margin of safety?"
- "The market dropped. Should I sell?"
- "Is this investment or speculation?"
- "How should I split my portfolio between stocks and bonds?"
- "Is this IPO, hot sector, or high-growth story investable?"

## CITATION RULES

Every substantive claim based on Graham's methodology must include a citation to the original text.

**Quote files to load when needed:**

- `value-investing-quotes.md` — core definitions, margin of safety, Mr. Market, defensive allocation, and Graham's central investing principles.
- `market-philosophy-quotes.md` — market cycles, earnings skepticism, IPO warnings, index funds, adviser conflicts, net-current-asset bargains, and historical humility.

**Citation format — always use this exact structure:**

> "Author's exact words here."
>
> — [*The Intelligent Investor*, cited excerpt](https://github.com/simbajigege/book2skills/blob/main/skills/intelligent-investor-graham/quotes/FILENAME.md#ANCHOR)

**Anchor mapping:**

- `value-investing-quotes.md`: `#buffett-endorses-graham`, `#investment-vs-speculation`, `#margin-of-safety`, `#mr-market`, `#mr-market-servant`, `#defensive-portfolio-split`, `#price-matters-more`, `#graham-core-principles`, `#the-future-value-depends-on-price`, `#no-need-for-extraordinary`
- `market-philosophy-quotes.md`: `#market-is-a-pendulum`, `#earnings-can-be-manipulated`, `#avoid-ipos`, `#index-funds-best`, `#advisers-misaligned`, `#net-current-asset-bargains`, `#simplicity-beats-cleverness`, `#santayana-warning`

**Rules:**

- Include at least one citation per major section of a Graham-method answer.
- Match the citation anchor to the closest principle being applied.
- Use quotes only from the `quotes/` files. Do not invent or paraphrase quotation text as if it were verbatim.
- If no exact quote fits, cite the closest anchor and clearly state that your analysis is a paraphrased application.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Steps | Output | Architecture |
|---|---|---|---|---|---|
| Investment/speculation classification | "Is this trade investing?" | Security, thesis, holding period, analysis done, leverage | Test analysis, principal safety, adequate return, separation of speculation funds | Clear classification and risk boundary | Dimension |
| Defensive stock screen | "Does X pass Graham's criteria?" | Financial statements, price, EPS history, dividends, debt, book value | Apply seven criteria without exceptions | Pass/fail table and disqualification points | Dimension |
| Margin of safety estimate | "What price is safe?" | Current price, average earnings, book value, bond yield, assumptions | Estimate value conservatively, compare price to value, calculate discount/premium | Buy zone, no-buy zone, data gaps | Dimension |
| Market fluctuation response | "Stock fell. Should I sell?" | Price change, business change, valuation, investor constraints | Separate quotation from business value; assess permanent impairment | Hold/buy/sell framework, not prediction | Dimension |
| Portfolio policy | "How should I allocate?" | Investor type, time/effort, income need, stock/bond yields | Choose 25/50/75 stock-bond range and rebalancing rule | Allocation recommendation with guardrails | Dimension |
| Adviser/fund evaluation | "Should I use this fund/adviser?" | Fees, strategy, promises, incentives, benchmark | Check cost drag, incentive conflict, performance claims | Use/avoid verdict and index-fund default | Dimension |

This is a single-file skill because the workflows are tightly coupled by the same final decision: protect principal, demand adequate return, and avoid emotional or promotional errors. The dimensions may be applied independently, but a complete Graham answer usually combines several of them.

## Core Principle

Investment is most intelligent when it is most businesslike. Treat a stock as an ownership interest in a business, estimate value independently, and buy only when the quoted price gives a margin of safety. Market prices are offers, not instructions. Forecasts, excitement, and cleverness are unreliable substitutes for arithmetic, discipline, and temperament.

## DIMENSION 1: Investment vs. Speculation

**The Rule:** An investment operation requires thorough analysis, reasonable safety of principal, and an adequate return. Anything missing from that triad makes the operation speculative.

### Key questions to ask:

- What analysis has been done on the underlying business or security?
- Is the expected protection of principal based on assets, earnings power, or contractual coverage?
- Is the expected return adequate relative to the risk?
- Is the user relying on price momentum, forecasts, promotion, or market timing?
- Is leverage involved?
- Is the user mixing speculative capital with long-term investment capital?

### Decision criteria / Checklist:

- Investment: business or security analyzed, principal protection explicit, return adequate.
- Investment: price paid is justified by conservative facts, not optimistic projections.
- Speculation: thesis depends mainly on price appreciation, market mood, a catalyst, or someone else paying more.
- Speculation: IPOs, hot issues, promoted securities, and margin-financed trades require special warning.
- Speculation may be allowed only if labeled honestly, sized small, and kept separate.

### Warning signals:

- "This time is different."
- "Everyone is buying it."
- "The company is great, so price does not matter."
- "I will sell before the crowd does."
- "I can borrow cheaply and improve returns."

### Agent instruction:

When the user presents a buy/sell/trade decision, classify the operation before offering any valuation opinion. If the operation fails Graham's investment definition, label it speculation clearly and recommend a separate, limited speculation account rather than treating it as a core investment.

## DIMENSION 2: Defensive vs. Enterprising Investor

**The Rule:** Graham's advice depends on temperament and effort. Defensive investors seek safety, simplicity, and freedom from effort; enterprising investors may seek better results only by applying more work, discipline, and selectivity.

### Key questions to ask:

- How much time and skill will the user realistically devote to analysis?
- Is the user trying to avoid serious mistakes or to pursue above-average returns?
- Does the user have the temperament to act against market emotion?
- Is the user willing to hold a diversified portfolio and rebalance mechanically?

### Decision criteria / Checklist:

- Defensive investor: default to diversified high-grade bonds plus leading common stocks or broad index funds.
- Defensive investor: use strict stock selection criteria; do not stretch for popular growth stories.
- Enterprising investor: may search for bargain issues, secondary companies, and special situations, but only with rigorous analysis.
- Enterprising investor: extra return must come from extra discipline and work, not from extra risk or optimism.

### Warning signals:

- A defensive investor trying to behave like a trader.
- An enterprising investor relying on tips instead of analysis.
- Treating effort as a substitute for margin of safety.
- Concentrating because of confidence rather than demonstrable value.

### Agent instruction:

Ask or infer the user's investor type early. If the user has not provided enough evidence of time, discipline, and analytical skill, default to defensive-investor recommendations.

## DIMENSION 3: Defensive Investor Stock Selection

**The Rule:** A defensive stock must pass Graham's quantitative tests for size, financial strength, earnings stability, dividends, earnings growth, and moderate valuation. A wonderful business can still fail the screen if the price is too high.

### Key questions to ask:

- Is the company large enough to avoid small-company fragility?
- Does the balance sheet show strong liquidity and moderate debt?
- Has the company earned money in every year of the last decade?
- Has it paid uninterrupted dividends for roughly two decades?
- Has per-share earnings grown meaningfully across a decade?
- Is the P/E ratio moderate using average earnings, not a single peak year?
- Is price-to-book moderate, or does the P/E x P/B product stay within Graham's combined limit?

### Decision criteria / Checklist:

Use these thresholds as Graham-style tests, while noting that dollar-size thresholds should be interpreted in today's market context:

1. Adequate size: large, established enterprise.
2. Strong financial condition: current ratio around 2.0 or better for industrials; debt not excessive relative to working capital or equity.
3. Earnings stability: positive earnings for each of the past 10 years.
4. Dividend record: long, uninterrupted dividend history, ideally 20 years.
5. Earnings growth: at least one-third growth in per-share earnings over 10 years, using multi-year averages.
6. Moderate P/E: no more than about 15 times average earnings.
7. Moderate assets multiple: price-to-book no more than about 1.5, or P/E x P/B no more than about 22.5.

### Warning signals:

- High P/E justified by "quality" or "AI/platform/brand premium."
- Book value ignored entirely for an asset-heavy or financial business.
- Dividend record broken or too short for a defensive investor.
- Earnings boosted by one-time items.
- Balance sheet strength assumed from reputation rather than tested.

### Agent instruction:

For a defensive stock evaluation, present a pass/fail table with the actual figure for each criterion. Do not average the score into a soft rating. If a criterion fails, state that the stock does not qualify for the defensive investor at the current price.

## DIMENSION 4: Margin of Safety

**The Rule:** The margin of safety is the central concept of sound investing. Buy only when the price is sufficiently below conservatively estimated value to absorb errors, adverse events, and ordinary uncertainty.

### Key questions to ask:

- What conservative value estimate is justified by current assets, normalized earnings, or bond-like coverage?
- How far below that value is the current price?
- Does the discount remain after adjusting for cyclicality, accounting quality, and business deterioration?
- Is the earnings yield attractive relative to high-grade bond yields?
- Is the margin based on facts already present, not hoped-for growth?

### Decision criteria / Checklist:

- Conservative valuation first; current market price second.
- Prefer normalized multi-year earnings to peak-year earnings.
- For defensive stocks, P/E and P/B limits are part of the safety test.
- For bargain issues, a large discount to net current asset value is especially strong evidence.
- Diversification is part of safety: one cheap stock can disappoint; a diversified group of cheap securities is more reliable.

### Warning signals:

- Paying full price for future growth.
- Reducing the required discount because the story is exciting.
- Calling a 5-10% discount a margin of safety when inputs are uncertain.
- Using aggressive terminal multiples or heroic growth rates.
- Ignoring dilution, debt, or accounting quality.

### Agent instruction:

When asked "is it cheap?" compute or request enough data to estimate normalized earnings value, earnings yield, P/E, P/B, and discount/premium to value. State the margin of safety as a percentage. If the result is a premium, say "negative margin of safety."

## DIMENSION 5: Mr. Market and Market Fluctuations

**The Rule:** Market quotation is there to serve the investor, not instruct the investor. Price declines are dangerous only when value deteriorates or the investor is forced to sell.

### Key questions to ask:

- Has the underlying business value changed, or only the quoted price?
- Is the price movement caused by temporary sentiment, cyclical fear, or permanent impairment?
- Would the user still want to own the business if the market closed for several years?
- Is the user leveraged or otherwise forced to sell?
- Does the new price create a better margin of safety?

### Decision criteria / Checklist:

- If business value is intact and price falls, expected return may improve.
- If business value deteriorates, a lower price may still be unsafe.
- If price rises far above value, consider selling or reducing.
- Never let daily quotations define intrinsic value.
- Use rebalancing and pre-set criteria to reduce emotional decisions.

### Warning signals:

- Selling because price fell, without business analysis.
- Buying because price rose, without margin of safety.
- Treating volatility as risk for a long-term unleveraged investor.
- Reading market news as if it were valuation.

### Agent instruction:

For any market-move question, begin by separating price change from value change. Then test whether the user's original thesis, balance sheet, earnings power, and margin of safety have changed.

## DIMENSION 6: Portfolio Allocation and Funds

**The Rule:** The defensive investor should hold both stocks and high-grade bonds, normally around 50/50 and never less than 25% in either category. Fund and adviser choices should be judged by cost, incentives, and realistic expectations.

### Key questions to ask:

- Is the user defensive or enterprising?
- What are current stock earnings yields relative to high-grade bond yields?
- Does the user need income stability, inflation protection, or long-term growth?
- What are the fees and incentives of any fund or adviser?
- Is the adviser promising market-beating results?

### Decision criteria / Checklist:

- Default allocation: 50% stocks / 50% high-grade bonds.
- Range: 25-75% stocks and 25-75% bonds.
- Shift only when relative valuations are clearly attractive or unattractive.
- Rebalance mechanically rather than forecasting market direction.
- For most defensive investors, low-cost index funds are preferable to expensive active funds.
- Evaluate advisers as risk managers and behavior coaches, not fortune-tellers.

### Warning signals:

- 100% stock or 100% bond allocation justified by a forecast.
- High fees sold as expertise.
- Adviser compensation that rewards activity or product sales.
- Recent fund performance marketed as repeatable skill.

### Agent instruction:

For allocation questions, recommend a stock/bond range, a rebalancing rule, and the data that would justify a tilt. Do not recommend all-in or all-out market timing.

## Query Response Framework

### Query Type 1: "Should I buy stock X?"

1. Identify investor type: defensive or enterprising.
2. Classify the proposed action as investment or speculation.
3. Run the defensive screen if the user is defensive or asks for Graham criteria.
4. Estimate margin of safety using normalized earnings, P/E, P/B, earnings yield, and conservative value.
5. Apply Mr. Market: is the current price an opportunity or a euphoric quotation?
6. Give a verdict: qualifies, watchlist only, speculative, or reject.

### Query Type 2: "What price would be attractive?"

1. Normalize earnings with multi-year averages.
2. Apply conservative valuation multiples rather than market multiples.
3. Compute maximum defensive price and a stricter safety price.
4. Explain what business deterioration would require lowering the estimate.
5. Output a buy zone, no-buy zone, and required monitoring data.

### Query Type 3: "The market dropped. Should I sell?"

1. Separate price movement from value movement.
2. Check business fundamentals and debt/liquidity.
3. Recalculate margin of safety at the new price.
4. Check whether the user is forced to sell.
5. Recommend hold, add, reduce, or sell based on value impairment and allocation discipline.

### Query Type 4: "How should I allocate my portfolio?"

1. Determine defensive vs. enterprising profile.
2. Start from 50/50 stocks/bonds.
3. Use the 25/75 guardrails.
4. Compare stock earnings yields with bond yields if data is available.
5. Recommend rebalancing rules and suitable low-cost vehicles.

### Query Type 5: "Should I trust this fund, adviser, IPO, or promoted idea?"

1. Identify incentives, fees, and promises.
2. Ask whether the opportunity has enough operating history and analyzable facts.
3. Treat aggressive promotion and hot issuance as warning signals.
4. Compare to a low-cost index or simple defensive portfolio.
5. Give a use/avoid verdict with the specific Graham reason.

## Output Format

### For Stock Evaluation

```markdown
## [Company] — Graham Investment Evaluation

**Investor type:** Defensive / Enterprising / Unknown
**Operation classification:** Investment / Speculation / Mixed

### Defensive Criteria
| Criterion | Graham requirement | Current data | Pass/Fail |
|---|---:|---:|---|

### Margin of Safety
- Normalized earnings value:
- Current price:
- Discount / premium to value:
- Earnings yield vs bond yield:
- P/B and P/E x P/B:

### Mr. Market Check
- What changed in price:
- What changed in business value:
- Emotional risk:

### Verdict
- Graham classification:
- Action: buy / watchlist / hold / reduce / avoid / speculative only
- Missing data:
- Citation:
```

### For Portfolio Allocation

```markdown
## Graham Portfolio Policy

- Investor type:
- Starting allocation:
- Recommended range:
- Valuation tilt:
- Rebalancing rule:
- Fund/adviser cautions:
- Citation:
```

## Critical Reminders

1. Price and value are different. Treat price as an offer, not a command.
2. Margin of safety is not optional; it is the central protection against error.
3. Never forecast the market as the basis for an investment policy.
4. A great company can be a poor investment at the wrong price.
5. Speculation must be named honestly, sized modestly, and kept separate.
6. Defensive investors should prefer simplicity, diversification, and low costs.
7. Earnings require skepticism; normalize them and watch for accounting distortions.
8. The investor's temperament is part of the method. Panic and enthusiasm both destroy discipline.
