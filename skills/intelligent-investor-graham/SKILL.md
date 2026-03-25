---
name: intelligent-investor-graham
description: Apply Benjamin Graham's value investing framework to evaluate stocks, portfolio allocation, and investment vs. speculation decisions. Trigger on: "Is this stock worth buying?", "Is this investment or speculation?", "How should I allocate my portfolio?", "Is this company a good value?", "should I sell in a downturn?", "evaluate this stock for a defensive investor".
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

## Overview

This skill encodes Benjamin Graham's framework from *The Intelligent Investor* (Revised Edition, 1973). It supports individual investors making decisions about stock valuation, portfolio allocation, and the psychology of market fluctuations. Designed for both defensive (passive) investors seeking safety and income, and enterprising (active) investors seeking superior returns through analysis.

## When to Use This Skill

- User asks whether a specific stock is worth buying or fairly valued
- User asks whether they are investing or speculating
- User asks how to respond to a market decline or crash
- User asks how to construct or rebalance a portfolio
- User asks whether to sell after a large price drop or buy after a rise
- User asks about margin of safety, P/E ratios, or book value in an investment context
- User wants to screen stocks for a conservative, long-term portfolio

## Core Principle

**Investment is most intelligent when it is most businesslike.** A stock is an ownership interest in a real business; its value derives from the business's earning power, not from the market's daily quotation. The intelligent investor buys at prices that provide a demonstrable margin of safety — a gap between price paid and underlying value — that absorbs miscalculations and bad luck. Speculation is not immoral, but it must be recognized as such and kept strictly separate from investment.

---

## DIMENSION 1: Investment vs. Speculation

**The Rule:** An investment operation is one which, upon thorough analysis, promises safety of principal and an adequate return. Everything else is speculation.

### Key questions to ask:
- Has the purchase been preceded by thorough analysis of the business?
- Is the principal reasonably protected against permanent loss?
- Is the expected return adequate relative to risk taken?
- Is the buyer using borrowed money (margin)? If yes → speculative by definition.
- Is the buyer relying primarily on price momentum rather than business value?

### Decision criteria / Checklist:
- ✅ Investment: analysis-driven, safety of principal, adequate return
- ✅ Investment: buying an established business at a known discount to value
- ❌ Speculation: buying because price went up (momentum)
- ❌ Speculation: buying a "hot" IPO or recently promoted issue
- ❌ Speculation: buying on margin without business analysis
- ❌ Speculation: relying on market timing or forecasting rather than valuation

### Warning signals:
- Believing you are investing when you are actually speculating
- Mixing speculative and investment funds in the same account
- Adding money to a speculative position because prices are rising
- Using recent market gains as justification for higher risk-taking

### Agent instruction:
When a user describes a purchase decision, first classify it as investment or speculation by checking: (1) Was thorough analysis done? (2) Is principal protected? (3) Is the expected return adequate? If any answer is no, label the operation speculation and warn clearly before proceeding with further analysis.

---

## DIMENSION 2: The Mr. Market Mental Model

**The Rule:** The stock market is an obliging but emotionally unstable business partner who offers to buy or sell your interest every day — use his irrational moods to your advantage; never let them determine your view of value.

### Key questions to ask:
- Is the current price driven by business fundamentals or by market sentiment?
- Is Mr. Market currently in a state of fear (depressing prices) or greed (inflating them)?
- Can you calculate an independent estimate of intrinsic value?
- Would you feel comfortable owning this business if no market quotation existed?

### Decision criteria / Checklist:
- Use market prices as an opportunity scanner, not as a valuation authority
- Buy from Mr. Market when he is irrationally pessimistic
- Sell to Mr. Market when he is irrationally optimistic
- Ignore Mr. Market when his price is neither clearly cheap nor clearly expensive
- The investor is NEVER forced to sell — this is the core advantage over a speculator

### Warning signals:
- Feeling anxiety or excitement based solely on price movements
- Selling a fundamentally sound position because the price declined
- Paying more for a stock because its price has recently risen
- Letting daily market news drive investment decisions

### Agent instruction:
When a user is reacting to a price movement (a stock fell 30%, market is crashing, stock surged), apply the Mr. Market model: ask whether the underlying business has changed. If not, a price decline is an opportunity, not a threat. Reframe the decision around business value, not price action.

---

## DIMENSION 3: Defensive Investor Stock Selection (7 Criteria)

**The Rule:** The defensive investor should only buy stocks that satisfy all seven quantitative criteria simultaneously — these criteria filter out both unsafe businesses and overpriced securities.

### Key questions to ask:
- What is the company's annual sales revenue and total asset size?
- What is the current ratio (current assets / current liabilities)?
- Does long-term debt exceed net current assets?
- Has the company earned a profit in each of the past 10 years?
- Has the company paid dividends continuously for 20+ years?
- Has earnings per share grown at least 1/3 over the past 10 years?
- What is the P/E ratio based on the past 3 years' average earnings?
- What is the price-to-book value ratio?

### Decision criteria / Checklist:
1. **Size**: Annual sales ≥ $100M (industrial) or total assets ≥ $50M (utility)
2. **Financial strength**: Current ratio ≥ 2.0; long-term debt ≤ net current assets (for industrials); for utilities, debt ≤ 2× equity
3. **Earnings stability**: Positive earnings in each of the past 10 years (no deficits)
4. **Dividend record**: Uninterrupted dividends for at least 20 consecutive years
5. **Earnings growth**: EPS growth ≥ 33% over the past 10 years (using 3-year averages at start and end)
6. **Moderate P/E**: Current price ÷ average EPS (past 3 years) ≤ 15
7. **Moderate price-to-book**: Price ÷ book value ≤ 1.5; OR (P/E) × (P/B) ≤ 22.5

### Warning signals:
- P/E above 15 without correspondingly low price-to-book (product > 22.5 is a fail)
- Any deficit year in the past decade
- Dividend history interrupted by even one year
- Current ratio below 2.0 — financial fragility
- Rapidly expanding debt not matched by asset growth

### Agent instruction:
When asked to evaluate a stock for a defensive investor, apply all 7 criteria. Present a pass/fail table for each criterion with the actual figure. A single fail is disqualifying. Stocks that pass all 7 represent suitable defensive investments. If data is incomplete, state clearly what is missing and that the evaluation cannot be completed.

---

## DIMENSION 4: Margin of Safety

**The Rule:** Never buy a security unless the price paid is demonstrably below the appraised value — the gap between price and value is the margin of safety that absorbs errors and adverse events.

### Key questions to ask:
- What is the intrinsic or appraised value of this security?
- How much below that value is the current price?
- Is the margin wide enough to survive a material decline in earnings?
- For bonds: does earnings coverage exceed interest charges by 5× or more (historically)?
- For stocks: is the earnings yield (E/P) meaningfully above the prevailing bond yield?
- Is the discount supported by arithmetic, not by optimistic forecasts?

### Decision criteria / Checklist:
- **Acceptable margin**: Price ≤ 2/3 of estimated intrinsic value (for bargain issues)
- **Earnings yield test**: E/P ratio should exceed the current high-grade bond yield
- **Asset backing**: For defensive stocks, price close to or below tangible book value strengthens safety
- **Diversification multiplies safety**: 20+ positions turn individual uncertainty into statistical advantage
- **Growth premium limit**: Even for growth stocks, price must be justifiable by conservative earnings projections, not hoped-for future glory

### Warning signals:
- Paying today for earnings growth that has not yet materialized
- Assuming future prospects can substitute for demonstrated past earning power
- Concentrating positions — removes the statistical protection of diversification
- Buying quality companies at any price (quality does not equal margin of safety)

### Agent instruction:
When asked whether a stock is a good buy, compute the earnings yield (most recent EPS ÷ current price × 100) and compare it to prevailing bond yields. Compute the P/B ratio. Estimate a rough intrinsic value using 15× average 3-year earnings and compare to current price. State the margin of safety explicitly as a percentage discount. If the stock is priced above intrinsic value, say so clearly.

---

## DIMENSION 5: Portfolio Allocation (Stocks vs. Bonds)

**The Rule:** The defensive investor should always hold a meaningful portion of both stocks and bonds — never less than 25% in either — and adjust the split based on relative valuations, not market forecasts.

### Key questions to ask:
- What is the current earnings yield on a representative stock index?
- What is the current yield on high-grade bonds?
- Does the investor need growth (inflation protection) or income (stability)?
- Is the investor defensive or enterprising in temperament and time commitment?
- Is the overall market level clearly high or clearly reasonable by historical value standards?

### Decision criteria / Checklist:
- **Default**: 50% stocks / 50% high-grade bonds
- **Minimum**: 25% stocks / 25% bonds (never go below either floor)
- **Shift toward bonds**: When earnings yield on stocks is clearly below bond yields
- **Shift toward stocks**: When stocks are demonstrably cheap relative to bonds and historical valuations
- **Rebalancing trigger**: Restore 50/50 when market moves the ratio by more than 5 percentage points
- **Dollar-cost averaging**: Investing a fixed amount at regular intervals (monthly) produces satisfactory long-run returns even through market cycles

### Warning signals:
- Moving to 100% stocks or 100% bonds based on a market prediction
- Selling all stocks because the market looks high (very likely to miss the subsequent advance)
- Treating market timing as a substitute for sound asset allocation
- Ignoring inflation risk in a 100% bond portfolio

### Agent instruction:
When asked about portfolio allocation, start by asking the investor's type (defensive vs. enterprising). Recommend the 25/50/75 range system. If the user provides current market yield data, compare stock earnings yield to bond yields to suggest direction of tilt. Never recommend exiting equities entirely. Emphasize rebalancing as a mechanical, emotion-free process.

---

## Query Response Framework

### Query Type 1: "Should I buy [stock X] at [price Y]?"

1. Identify investor type: defensive or enterprising?
2. **For defensive investors**: Apply all 7 criteria from Dimension 3. Present pass/fail table. If any criterion fails, the stock does not qualify.
3. **For all investors**: Calculate earnings yield, P/B ratio, compare to intrinsic value estimate (15× 3-year average EPS). State the margin of safety.
4. Apply Mr. Market test: Is current price driven by fear, greed, or fundamentals?
5. Deliver verdict with explicit margin of safety figure.

### Query Type 2: "The market / my stock dropped X%. Should I sell?"

1. Apply Mr. Market model: Has the underlying business changed?
2. Reassess whether the original investment thesis is intact.
3. If business is unchanged or improving and price has fallen: this is an opportunity, not a crisis.
4. If the investor is leveraged or speculating: acknowledge the difference in risk profile.
5. Remind: the intelligent investor is never forced to sell. Time is the ally of the good business bought at a fair price.

### Query Type 3: "Am I investing or speculating?"

1. Apply Dimension 1 checklist: analysis? principal safety? adequate return?
2. Check for margin use, momentum motivation, short-term horizon.
3. Classify clearly as investment or speculation (or mixed).
4. If speculation: quantify what the investor can afford to lose. Recommend keeping speculative funds strictly separate.

### Query Type 4: "How should I allocate my portfolio?"

1. Determine investor type (defensive/enterprising).
2. Check current valuations: earnings yield vs. bond yields.
3. Recommend a stocks/bonds split within the 25–75% range.
4. Recommend index funds or diversified blue-chip stocks for defensive investor.
5. Emphasize mechanical rebalancing and dollar-cost averaging.

---

## Output Format

**For stock evaluation:**
```
## [Company Name] — Investment Evaluation

**Investor Type:** Defensive / Enterprising

### 7-Criteria Checklist (Defensive)
| Criterion | Required | Actual | Pass/Fail |
|-----------|----------|--------|-----------|
| Size | ≥$100M revenue | $XXXm | ✅/❌ |
| Current Ratio | ≥ 2.0 | X.X | ✅/❌ |
| Earnings Stability | 10 years positive | X years | ✅/❌ |
| Dividend Record | 20+ years | X years | ✅/❌ |
| Earnings Growth | ≥ 33% / 10yr | X% | ✅/❌ |
| P/E Ratio | ≤ 15× | X× | ✅/❌ |
| P/B Ratio | ≤ 1.5× (or P/E×P/B ≤ 22.5) | X× | ✅/❌ |

### Margin of Safety
- Estimated intrinsic value: $XX (15× 3-year avg. EPS)
- Current price: $XX
- Discount / Premium: X%
- Earnings yield: X% vs. bond yield X%

### Verdict
> [QUALIFIES / DOES NOT QUALIFY] for defensive investor.
> Margin of safety: [ADEQUATE / THIN / NEGATIVE].
> [1–2 sentence investment/speculation classification.]
```

**For market reaction questions:** Lead with the Mr. Market framework, then business fundamentals assessment. End with a clear action recommendation.

**For portfolio allocation:** State the recommended stock/bond split with rationale. Include a rebalancing rule.

---

## Critical Reminders

1. **Price and value are different things.** A rising price does not make a stock safer; a falling price does not make it more dangerous — unless the underlying business has deteriorated.
2. **The margin of safety is not optional.** It is the single concept that separates investment from speculation. Never waive it for an "exciting" opportunity.
3. **Never forecast the market.** The future of security prices is never predictable. Allocation decisions should be based on current valuations vs. historical standards, not predictions.
4. **Separate investment and speculation accounts.** If the user insists on speculating, help them do it safely in a separate, limited fund — never mixed with investment capital.
5. **Diversification is the mechanical realization of the margin of safety.** A single stock with a margin of safety can still lose money; 20 stocks with margins of safety almost certainly will not produce aggregate loss.
6. **The intelligent investor's greatest enemy is themselves.** Emotional responses to Mr. Market are the primary source of investment losses. The framework exists to make decisions mechanical and emotion-free.
7. **Quality is not a substitute for price.** The best company in the world bought at 40× earnings provides no margin of safety. Even mediocre businesses become sound investments at sufficiently low prices.
