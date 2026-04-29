# Skill: Portfolio Policy (The Intelligent Investor / Module 5)

**Knowledge source:** *The Intelligent Investor* by Benjamin Graham.
**Reference library:** `references/case_library.md`
**Standalone use:** This module can run independently or as part of `../../SKILL.md`.

## When to Use

Use this module when the user asks how to allocate between stocks and bonds, whether to go all-in or all-out, how to rebalance, or how a defensive investor should implement a simple policy.

## Module Inputs

- Investor type: defensive, enterprising, or unknown.
- Current stock/bond/cash allocation.
- Income needs, liquidity needs, time horizon, temperament.
- Current stock earnings yields and high-grade bond yields if available.
- Fund options and costs if implementation is requested.

## Module Outputs

- Starting allocation.
- Permitted stock/bond range.
- Rebalancing rule.
- Conditions for valuation tilt.
- Implementation cautions and citation IDs.

## Execution Flow

### Overview

1. Identify investor posture.
2. Start with Graham's balanced default.
3. Apply guardrails.
4. Define mechanical rebalancing.
5. Reject forecast-driven extremes.

### Step 1: Set the Default

**Core question:** What policy keeps the investor disciplined without forecasting?

**Decision rules:**

- Defensive default: 50% stocks and 50% high-grade bonds.
- Minimum/maximum guardrails: generally keep at least 25% and at most 75% in either stocks or bonds.
- If investor type is unknown, default defensive.

**Citation instruction:** Cite `REF-M5-001` for defensive portfolio split.

### Step 2: Decide Whether a Tilt Is Justified

**Core question:** Are relative valuations clearly favorable enough to move away from 50/50?

**Decision rules:**

- Move toward 75% stocks only when stocks are clearly attractive by conservative valuation and the user can tolerate volatility.
- Move toward 25% stocks when stocks are clearly expensive or the user needs stability.
- Never recommend 100% stocks or 100% bonds based on a forecast.

### Step 3: Define Rebalancing

**Recommended rules:**

- Rebalance annually, semiannually, or when allocation drifts materially from target.
- Use rebalancing to sell some of what has become relatively expensive and buy what has become relatively cheaper.
- Keep emergency liquidity outside the investment allocation if the user has near-term cash needs.

### Step 4: Implementation Vehicle

**Decision rules:**

- For most defensive investors, low-cost diversified index funds are the implementation default.
- High-cost active funds must justify fees, process, and incentives.

**Citation instruction:** Cite `REF-M5-002` when recommending index funds as the defensive default.

## Output Format

```markdown
## Graham Portfolio Policy

**Investor posture:** Defensive / Enterprising / Unknown
**Current allocation:** ...
**Starting point:** 50/50 stocks and high-grade bonds
**Recommended range:** ...% stocks / ...% bonds
**Rebalancing rule:** ...
**Valuation tilt, if any:** ...
**Implementation notes:** ...
**Citations:** REF-M5-...
```

## Do Not

- Do not recommend all-in or all-out allocations.
- Do not base allocation on a market forecast.
- Do not ignore fees and implementation costs.
