---
name: investing-from-darwin
description: Apply Pulak Prasad evolutionary investing rules for avoiding big losses,
  buying resilient quality, rejecting fragile forecasts, and being very lazy.
license: Skill distillation for personal/educational use. Do not reproduce source
  passages verbatim.
---


# What I Learned About Investing from Darwin — Evolutionary Investing Skill

**Knowledge source:** *What I Learned About Investing from Darwin* by Pulak Prasad.

## Overview

Use this skill to evaluate investments through evolutionary survival logic: avoid big risks, buy high-quality resilient businesses at fair prices, and stay very patient. It supports investors who want to avoid permanent capital loss, resist over-trading, and prefer robustness over fragile forecasting.

## When to Use This Skill

Use this skill when the user asks:
- "Is this business resilient enough to own?"
- "What big risks could permanently hurt this investment?"
- "Is this cheap stock a trap?"
- "Should I rely on this DCF?"
- "How patient should I be?"
- "How would Darwin-inspired investing judge this company?"

## Core Principle

Investment survival comes before investment brilliance. Like evolution, investing rewards robustness, adaptation, and patience more reliably than precision forecasts, frequent action, or bargain-hunting in fragile businesses.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Steps | Output | Independent trigger? | Distinct references? | Triage score | Should be subskill? | Reason |
|---|---|---|---|---|---|---:|---:|---|---|
| Big-risk screen | "What could kill this investment?" | Business model, debt, disruption, governance, valuation | Identify permanent-loss scenarios | Avoid/continue risk verdict | Yes | Yes | 3 | No | First rule of the same investing framework. |
| Quality-at-fair-price review | "Is this a quality company?" | Moat, returns, industry, price, scenarios | Test resilience, causation, robustness | Quality verdict | Yes | Yes | 3 | No | Must follow risk screen. |
| Forecast skepticism | "Does this DCF justify buying?" | Model assumptions, horizon, uncertainty | Stress precision and replay-the-tape fragility | Forecast reliability rating | Yes | Yes | 3 | No | Same robustness lens. |
| Very-lazy holding policy | "Should I trade or wait?" | Current holding, thesis, new data, opportunity set | Check rare-opportunity threshold | Hold/wait/act rule | Yes | Yes | 3 | No | Same three-rule framework. |

## Architecture Justification

The three sections form a sequential framework: avoid big risks, buy quality at a fair price, then be very lazy. Since each later judgment depends on survival and quality screens, a single-file architecture keeps the dependency explicit.

## DIMENSION 1: Avoid Big Risks

**The Rule:** The first job is to avoid permanent capital loss.

### Key questions to ask:
- What could cause a large, unrecoverable loss?
- Is the business exposed to debt, disruption, fraud, regulation, customer concentration, or obsolescence?
- Would a 50% loss require unrealistic recovery?
- Is the investor underestimating extinction risk?

### Decision criteria / Checklist:
- Identify existential business risks.
- Test balance-sheet resilience.
- Avoid situations where one adverse event can permanently impair capital.
- Prefer adaptable businesses over fragile strength.

### Warning signals:
- Leverage plus uncertain cash flows.
- Cheap valuation masking structural decline.
- Single-product, single-customer, or single-regulation dependence.

### Agent instruction:
Before discussing upside, produce a big-risk screen and reject investments that fail survival tests.

## DIMENSION 2: Buy Quality at a Fair Price

**The Rule:** Resilient quality beats apparent cheapness.

### Key questions to ask:
- What durable advantage helps the company survive changing environments?
- Is quality natural and embedded, or dependent on constant restructuring?
- Are high returns caused by real advantages or merely correlated indicators?
- Is the price fair enough for quality without requiring heroic forecasts?

### Decision criteria / Checklist:
- Durable moat or adaptive advantage.
- Simple focused business.
- Robust economics across multiple scenarios.
- Fair price, not necessarily bargain-basement price.

### Warning signals:
- Turnaround stories requiring continuous consultant intervention.
- Confusing correlation with causation.
- Low multiple used as substitute for business quality.

### Agent instruction:
When evaluating cheapness, force the user to prove business resilience before calling the opportunity attractive.

## DIMENSION 3: Robustness Over Forecast Precision

**The Rule:** Long-term precision forecasts are fragile; prefer businesses that can survive many futures.

### Key questions to ask:
- Which DCF assumptions drive most of the valuation?
- Would the thesis survive if growth, margins, or terminal value were wrong?
- If history replayed differently, would the business still do well?
- What scenarios break the thesis?

### Decision criteria / Checklist:
- Stress test key assumptions.
- Prefer qualitative robustness over point-estimate precision.
- Avoid investments that need a narrow future path.
- Treat DCF as a discipline, not proof.

### Warning signals:
- Purchase thesis depends on precise terminal growth.
- Model hides uncertainty behind decimal-point accuracy.
- Bull case requires everything to go right.

### Agent instruction:
For model-based pitches, critique forecast fragility and replace false precision with scenario robustness.

## DIMENSION 4: Be Very Lazy

**The Rule:** Trade rarely; most good investing is waiting.

### Key questions to ask:
- Has the thesis changed or is the user reacting to noise?
- Is this a rare opportunity or routine market movement?
- Would action improve expected outcome after costs and errors?
- Is patience being confused with laziness, or laziness with discipline?

### Decision criteria / Checklist:
- Low turnover by default.
- Act decisively only when opportunity is rare and evidence strong.
- Hold resilient businesses through ordinary fluctuations.
- Keep a high bar for replacing existing holdings.

### Warning signals:
- Pavlovian reaction to quarterly news.
- Trading to relieve boredom.
- Mistaking constant research activity for better decisions.

### Agent instruction:
When the user wants to act, require evidence that the situation is a rare opportunity or thesis-breaking change.

## Query Response Framework

### Query Type 1: Evaluate a stock
1. Run Avoid Big Risks.
2. Test Quality at Fair Price.
3. Challenge forecast precision.
4. Decide whether to buy, avoid, hold, or wait very lazily.

### Query Type 2: Review a DCF or model
1. Identify fragile assumptions.
2. Stress multiple futures.
3. Decide whether robustness exists without precise prediction.

### Query Type 3: Sell/hold decision
1. Check whether thesis changed.
2. Separate noise from extinction risk.
3. Apply very-lazy discipline.

## Output Format

```markdown
## Darwin-Inspired Investment Review
**Company / Decision:** ...
**Verdict:** Avoid / Watch / Quality at fair price / Hold lazily / Needs data

| Rule | Evidence | Result |
|---|---|---|

## Big Risks
...

## Robustness Check
...

## Action Discipline
...

## Citations
...
```

## Critical Reminders

1. Avoiding big losses comes before seeking big gains.
2. Quality is not the same as cheapness.
3. Forecast precision is often false comfort.
4. Correlation is not causation.
5. Being very lazy means disciplined inaction, not neglect.

## CITATION RULES

Every substantive Prasad-method claim must include a citation to the original text.

**Quote files:**
- `evolutionary-investing-quotes.md` — Darwin/investing connection, survival, adaptation, moat, long-term perspective, diversification, selection, extinction, ecosystem, and patience.
- `investing-principles-quotes.md` — avoiding big losses, quality over price, DCF skepticism, replay-the-tape, very lazy behavior, punctuated equilibrium, rare opportunities, and three rules.

**Citation format:**

> "Author's exact words here."
>
> — [*What I Learned About Investing from Darwin*, cited excerpt](https://github.com/simbajigege/book2skills/blob/main/skills/investing-from-darwin/quotes/FILENAME.md#ANCHOR)

**Anchor mapping:**
- `evolutionary-investing-quotes.md`: `#darwin-investing-connection`, `#survival-of-the-fittest`, `#adaptation-key`, `#moat-as-adaptation`, `#long-term-perspective`, `#diversification-nature`, `#selection-criteria`, `#extinction-warning`, `#mutation-innovation`, `#ecosystem-thinking`, `#fitness-landscape`, `#patience-discipline`
- `investing-principles-quotes.md`: `#avoid-big-losses`, `#survival-before-thriving`, `#not-strongest-but-adaptable`, `#quality-over-price`, `#darwin-ate-my-dcf`, `#replay-the-tape`, `#be-very-lazy`, `#punctuated-equilibrium`, `#rare-opportunities`, `#three-rules-from-darwin`

**Rules:**
- Cite a survival or quality anchor before any buy verdict.
- Use DCF anchors when critiquing model precision.
- Do not provide personalized regulated financial advice.
