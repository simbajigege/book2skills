# Skill: Margin of Safety Pricing (The Intelligent Investor / Module 3)

**Knowledge source:** *The Intelligent Investor* by Benjamin Graham.
**Reference library:** `references/case_library.md`
**Standalone use:** This module can run independently or as part of `../../SKILL.md`.

## When to Use

Use this module when the user asks whether a security is cheap, what price is attractive, how much margin of safety exists, whether to add/reduce, or how to set a Graham-style buy zone.

## Module Inputs

- Current price.
- Normalized EPS or owner earnings across multiple years.
- Book value per share and tangible book if relevant.
- Net current asset value if available.
- Debt, dilution, and cyclicality.
- High-grade bond yield or user-provided hurdle rate.
- Any prior M2 defensive-screen result.

## Module Outputs

- Conservative value range.
- Margin of safety percentage.
- Buy zone, watch zone, avoid zone.
- Data gaps and sensitivity warnings.
- Citation IDs.

## Execution Flow

### Overview

1. Normalize earnings and assets.
2. Choose conservative valuation anchors.
3. Compare price to value.
4. Translate the gap into a margin-of-safety verdict.

### Step 1: Normalize the Facts

**Core question:** What value is supported by facts already present?

**Decision rules:**

- Prefer multi-year average earnings to peak earnings.
- Penalize cyclicality, leverage, dilution, and accounting uncertainty.
- Use book value or net current asset value when assets are central to the case.
- Do not capitalize promotional future growth as if it were already earned.

### Step 2: Estimate Conservative Value

**Decision rules:**

| Method | Use When | Graham discipline |
|---|---|---|
| Average earnings multiple | Stable profitable business | Use moderate multiple; avoid market-story multiples |
| Defensive P/E and P/B limits | Defensive stock candidate | Respect about 15x average EPS, about 1.5x book, or about 22.5 combined |
| Net current asset value | Deep bargain / liquidation-style candidate | Require price far below conservatively counted current assets less liabilities |
| Earnings yield comparison | Allocation or bond alternative question | Compare earnings yield with high-grade bond yield cautiously |

**Citation instruction:** Cite `REF-M3-001` for margin of safety and `REF-M3-002` for price-value discipline.

### Step 3: Calculate Margin of Safety

**Formula:** `(conservative value - current price) / conservative value`.

**Verdict rules:**

- Strong margin: large discount remains after conservative adjustments.
- Thin margin: modest discount that could vanish under normal error.
- Negative margin: current price exceeds conservative value.
- Unknown: insufficient normalized earnings, assets, or debt data.

### Step 4: Convert to Action Zones

- Buy zone: price provides clear margin of safety and other routed modules do not disqualify the idea.
- Watch zone: business may be acceptable but price is too close to value.
- Avoid zone: no margin of safety, aggressive assumptions required, or principal protection unclear.

## Output Format

```markdown
## Margin of Safety — [Security]

**Current price:** ...
**Conservative value range:** ...
**Margin of safety:** ...%

| Valuation anchor | Input | Conservative result | Notes |
|---|---:|---:|---|
| Normalized earnings | ... | ... | ... |
| Book / tangible book | ... | ... | ... |
| NCAV if relevant | ... | ... | ... |

**Buy zone:** ...
**Watch zone:** ...
**Avoid zone:** ...
**Key assumptions that would break the estimate:** ...
**Citations:** REF-M3-...
```

## Do Not

- Do not call a security cheap merely because it fell.
- Do not use aggressive terminal multiples or heroic growth assumptions.
- Do not treat a 5-10% discount as adequate when inputs are uncertain.
