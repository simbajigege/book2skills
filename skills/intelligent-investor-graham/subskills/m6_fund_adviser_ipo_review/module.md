# Skill: Fund, Adviser, IPO, and Promoted-Idea Review (The Intelligent Investor / Module 6)

**Knowledge source:** *The Intelligent Investor* by Benjamin Graham.
**Reference library:** `references/case_library.md`
**Standalone use:** This module can run independently or as part of `../../SKILL.md`.

## When to Use

Use this module when the user asks whether to buy an IPO, new issue, SPAC, hot sector fund, actively managed fund, adviser recommendation, newsletter idea, or heavily promoted investment.

## Module Inputs

- Product or security type.
- Fees, loads, expense ratios, advisory compensation, or embedded incentives.
- Operating history and performance history.
- Marketing claims and promised benefits.
- Underlying holdings or analyzable financial data.
- Comparable low-cost index or simple defensive alternative.

## Module Outputs

- Promotion and incentive diagnosis.
- Use/avoid/watch verdict.
- Safer default alternative.
- Missing due-diligence questions.
- Citation IDs.

## Execution Flow

### Overview

1. Identify whether the product is analyzable.
2. Inspect incentives and fees.
3. Detect promotional timing.
4. Compare to a simple low-cost alternative.
5. Decide whether Graham would avoid, watch, or use it cautiously.

### Step 1: Test Analyzable Facts

**Core question:** Is there enough operating record and financial data for investment analysis?

**Decision rules:**

- IPOs and new issues usually lack enough public operating history at the offered price.
- A story about a new industry is not a substitute for analyzable earnings, assets, and price.
- If the product cannot be analyzed, route to M1 and classify as speculation.

**Citation instruction:** Cite `REF-M6-001` for IPO warnings.

### Step 2: Inspect Incentives and Fees

**Core question:** Who benefits if the user buys?

**Decision rules:**

- High fees require a high burden of proof.
- Adviser or broker incentives tied to transactions or product sales are conflicts.
- Past outperformance claims need skepticism, especially when presented as repeatable certainty.

**Citation instruction:** Cite `REF-M6-002` for adviser conflicts.

### Step 3: Compare to Defensive Default

**Decision rules:**

- For defensive investors, compare the product with a low-cost broad index fund and high-grade bond allocation.
- Prefer simplicity when the complex product does not clearly improve safety, cost, or expected return.

**Citation instruction:** Cite `REF-M6-003` for index funds and `REF-M6-004` for simplicity.

## Output Format

```markdown
## Graham Product Review — [Fund / Adviser / IPO / Idea]

| Test | Result | Evidence |
|---|---|---|
| Analyzable record | Pass/Fail/Unknown | ... |
| Fee and incentive alignment | Pass/Fail/Unknown | ... |
| Promotion risk | Low/Medium/High | ... |
| Better simple alternative | Yes/No | ... |

**Verdict:** Use / Avoid / Watch only / Speculative only
**Graham reason:** ...
**Questions before committing capital:** ...
**Citations:** REF-M6-...
```

## Do Not

- Do not recommend IPOs or hot issues because of popularity.
- Do not treat adviser authority as a substitute for independent analysis.
- Do not ignore expense ratios, loads, or sales incentives.
