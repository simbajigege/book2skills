# Skill: Market Fluctuation Response (The Intelligent Investor / Module 4)

**Knowledge source:** *The Intelligent Investor* by Benjamin Graham.
**Reference library:** `references/case_library.md`
**Standalone use:** This module can run independently or as part of `../../SKILL.md`.

## When to Use

Use this module when the user asks what to do after a stock, sector, or market has risen or fallen sharply, or when fear/euphoria is driving the decision.

## Module Inputs

- Security or portfolio affected.
- Price change magnitude and timeframe.
- Business facts that changed, if any.
- Prior thesis and original margin of safety.
- Current valuation data.
- User liquidity needs, leverage, or forced-selling constraints.
- Current allocation versus policy target.

## Module Outputs

- Price-change versus value-change diagnosis.
- Forced-selling risk assessment.
- Hold/add/reduce/sell decision framework.
- Rebalancing instruction if portfolio-level.
- Citation IDs.

## Execution Flow

### Overview

1. Separate quotation from business value.
2. Check permanent impairment.
3. Recalculate margin of safety if data permits.
4. Apply allocation discipline and temperament rules.

### Step 1: Separate Price From Value

**Core question:** Did the business value change, or only Mr. Market's quotation?

**Decision rules:**

- Price down + value intact + no forced selling may improve expected return.
- Price down + value impaired may still be dangerous.
- Price up far above value may justify reducing even when business quality is intact.

**Citation instruction:** Cite `REF-M4-001` and `REF-M4-002` for Mr. Market.

### Step 2: Check Permanent Impairment

**Core question:** What facts would lower conservative value?

**Check:**

- Earnings power deterioration.
- Balance-sheet stress or refinancing risk.
- Dividend cut with weak coverage.
- Dilution, fraud, or accounting restatement.
- Industry economics permanently worse rather than temporarily unpopular.

### Step 3: Check Investor Constraint Risk

**Core question:** Can the user act as an investor, or are they forced into trader behavior?

**Decision rules:**

- Leverage, near-term cash needs, or concentration can convert volatility into real risk.
- If forced-selling risk exists, prioritize liquidity and allocation repair over valuation purity.

### Step 4: Recommend Discipline

| Diagnosis | Graham-style response |
|---|---|
| Value intact, price lower, margin improved | Hold or consider adding within allocation limits |
| Value impaired, price lower | Revalue; reduce or sell if margin is gone |
| Price above conservative value | Rebalance, reduce, or stop adding |
| Data missing | Do not act emotionally; gather facts required by M3 |

## Output Format

```markdown
## Market Fluctuation Response — [Security / Portfolio]

**What changed in price:** ...
**What changed in business value:** ...
**Forced-selling risk:** Yes/No/Unknown
**Margin of safety now:** Improved / worsened / gone / unknown

### Graham Diagnosis
- ...

### Action Discipline
- Hold / add within limits / reduce / sell / wait for data
- Rebalancing rule:
- Data to verify:

**Citations:** REF-M4-...
```

## Do Not

- Do not sell solely because the price fell.
- Do not buy solely because the price rose or because others are enthusiastic.
- Do not treat volatility as the same thing as permanent loss for an unleveraged long-term investor.
