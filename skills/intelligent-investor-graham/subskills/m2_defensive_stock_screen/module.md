# Skill: Defensive Stock Screen (The Intelligent Investor / Module 2)

**Knowledge source:** *The Intelligent Investor* by Benjamin Graham.
**Reference library:** `references/case_library.md`
**Standalone use:** This module can run independently or as part of `../../SKILL.md`.

## When to Use

Use this module when the user asks whether a stock qualifies for a defensive investor, passes Graham's checklist, or is suitable for a low-effort conservative stock portfolio.

## Module Inputs

- Company size and operating history.
- Current assets, current liabilities, long-term debt, equity or working capital.
- EPS for the past 10 years.
- Dividend history, preferably 20 years.
- EPS growth across a decade using multi-year averages.
- Current price, normalized EPS, book value per share.
- Industry context, especially for financials and utilities.

## Module Outputs

- Pass/fail table for Graham's defensive criteria.
- Disqualifying failures.
- Missing data list.
- Defensive-investor verdict: qualifies, fails, or cannot determine.

## Execution Flow

### Overview

1. Identify whether the user is asking from a defensive-investor posture.
2. Apply all seven tests.
3. Do not average away failures.
4. State whether the current price permits defensive ownership.

### Step 1: Confirm Defensive Standard

**Core question:** Is the user seeking safety, simplicity, and freedom from effort?

**Decision rules:**

- If yes or unknown, apply the defensive standard strictly.
- If the user is explicitly enterprising, use this screen only as a quality baseline and route to M7 for bargain hunting.

### Step 2: Apply Seven Criteria

| Criterion | Graham-style requirement | Result rule |
|---|---|---|
| Adequate size | Large, established enterprise | Fail if small or fragile |
| Financial condition | Strong liquidity and moderate debt | Fail if balance sheet is weak |
| Earnings stability | Positive earnings for each of the past 10 years | Any loss year fails |
| Dividend record | Long uninterrupted record, ideally 20 years | Short or broken record fails defensive test |
| Earnings growth | At least about one-third growth over 10 years using averages | Fail if stagnant or declining |
| Moderate P/E | No more than about 15x average earnings | Fail if price is too high |
| Moderate assets multiple | P/B about 1.5 or less, or P/E x P/B about 22.5 or less | Fail if valuation is stretched |

**Citation instruction:** Cite `REF-M2-001` for price discipline and `REF-M2-002` for the need to avoid extraordinary assumptions.

### Step 3: Treat Accounting and Cyclicality Skeptically

**Core question:** Are reported earnings representative?

**Decision rules:**

- Use average earnings rather than one peak year.
- Flag one-time gains, restructurings, aggressive adjustments, and dilution.
- If the user provides only current-year EPS, mark the stability and valuation tests incomplete.

**Citation instruction:** Cite `REF-M2-003` when warning that earnings can be manipulated.

## Output Format

```markdown
## Defensive Investor Screen — [Company]

| Criterion | Graham requirement | Current data | Pass/Fail |
|---|---|---:|---|
| Adequate size | Large established company | ... | ... |
| Financial condition | Strong liquidity, moderate debt | ... | ... |
| Earnings stability | 10 years positive earnings | ... | ... |
| Dividend record | Long uninterrupted record | ... | ... |
| Earnings growth | One-third 10-year growth | ... | ... |
| Moderate P/E | <= about 15x average earnings | ... | ... |
| Moderate P/B | <= about 1.5 or P/E x P/B <= about 22.5 | ... | ... |

**Defensive verdict:** Qualifies / Fails / Cannot determine
**Disqualifiers:** ...
**Missing data:** ...
**Citations:** REF-M2-...
```

## Do Not

- Do not turn the checklist into a weighted score.
- Do not say a stock qualifies defensively if any required criterion fails.
- Do not excuse a high valuation because the business is popular or high quality.
