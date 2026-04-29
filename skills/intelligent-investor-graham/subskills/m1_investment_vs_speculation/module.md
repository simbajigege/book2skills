# Skill: Investment vs. Speculation Classification (The Intelligent Investor / Module 1)

**Knowledge source:** *The Intelligent Investor* by Benjamin Graham.
**Reference library:** `references/case_library.md`
**Standalone use:** This module can run independently or as part of `../../SKILL.md`.

## When to Use

Use this module whenever the user proposes buying, selling, trading, leveraging, chasing a catalyst, following a tip, buying a hot issue, or asking whether an idea is "investing."

## Module Inputs

- Security or product name.
- User thesis and expected holding period.
- Analysis already performed.
- Expected source of return.
- Principal-risk controls.
- Leverage, options, margin, or concentration.
- Whether this is core capital or a separate speculation account.

## Module Outputs

- Classification: Investment, Speculation, or Mixed.
- Failed Graham conditions.
- Required boundary conditions if speculation remains.
- Missing data questions.
- Citation IDs from `references/case_library.md`.

## Execution Flow

### Overview

1. Test for analysis.
2. Test for safety of principal.
3. Test for adequate return.
4. Detect promotional, timing, leverage, and crowd-dependence signals.
5. Classify and set boundaries.

### Step 1: Test Thorough Analysis

**Core question:** Has the user analyzed the security as a business or contract, rather than as a ticker or story?

**Decision rules:**

| Signal | Interpretation |
|---|---|
| Multi-year earnings, assets, balance sheet, dividends, price/value reviewed | Can proceed toward investment classification |
| Thesis depends on chart, rumor, short-term catalyst, macro prediction, or social proof | Speculative unless further facts are provided |
| User cannot explain expected return source | Speculative |

**Ask the user:** What facts support the valuation and downside protection?

**Citation instruction:** Cite `REF-M1-001` for Graham's investment definition.

### Step 2: Test Safety of Principal

**Core question:** Is principal protection grounded in conservative value, asset coverage, earnings power, diversification, or contractual seniority?

**Decision rules:**

- If downside protection depends mainly on selling to someone else at a higher price, classify as speculation.
- If the idea uses margin, options, or forced liquidation risk, flag it as speculative even if the underlying security is sound.
- If the price is far above conservative value, principal safety is not demonstrated.

**Citation instruction:** Cite `REF-M1-002` when explaining that price paid determines future results.

### Step 3: Test Adequate Return

**Core question:** Is the expected return adequate relative to risk and available high-grade alternatives?

**Decision rules:**

- Adequate return requires a reasonable relationship between price, earnings/assets, and risk.
- Hoped-for growth alone is not adequate return.
- A low-quality security does not become an investment just because the upside is large.

### Step 4: Detect Speculation Signals

**Warning signals:**

- "Everyone is buying it."
- "It cannot go lower."
- "The company is great, so price does not matter."
- "I only need to hold until the catalyst."
- Borrowed money, options, or large concentration.

**Citation instruction:** Cite `REF-M1-003` for avoiding cleverness and extraordinary assumptions.

## Output Format

```markdown
## Investment vs. Speculation — [Idea]

| Graham test | Result | Evidence |
|---|---|---|
| Thorough analysis | Pass/Fail/Unknown | ... |
| Safety of principal | Pass/Fail/Unknown | ... |
| Adequate return | Pass/Fail/Unknown | ... |

**Classification:** Investment / Speculation / Mixed
**Why:** ...
**If pursued anyway:** keep separate from core capital, size modestly, avoid leverage, and define exit conditions.
**Missing data:** ...
**Citations:** REF-M1-...
```

## Do Not

- Do not classify an idea as investment just because it is a common stock.
- Do not ignore leverage or position sizing.
- Do not move to valuation before naming speculation risk.
