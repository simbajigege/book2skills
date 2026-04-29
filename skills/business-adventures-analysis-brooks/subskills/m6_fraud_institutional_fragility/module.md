# Skill: Fraud and Institutional Fragility (Business Adventures — Module 6)

**Knowledge source:** *Business Adventures* by John Brooks  
**Reference library:** `references/case_library.md`  
**Standalone use:** This module can run independently or as part of `../../SKILL.md`.

## When to Use

Use this module for fraud, collateral failure, counterparty exposure, hidden leverage, exchange or banking responsibility, institutional rescue, confidence crises, or "how exposed is the system?" questions.

## Module Inputs

- Trust mechanism being relied on
- Collateral, counterparty, disclosure, or custody structure
- Visible losses and suspected hidden exposure
- Institutions expected to absorb losses
- Possible contagion channels

## Module Outputs

- Trust mechanism under stress
- Hidden exposure map
- Responsibility-transfer diagnosis
- Safeguards, exit criteria, or disclosure actions

## Execution Flow

### Overview

```text
Fraud and fragility
├── Step 1: Identify the trust mechanism
├── Step 2: Map hidden exposure
├── Step 3: Test institutional responsibility
├── Step 4: Identify contagion path
└── Step 5: Recommend safeguards
```

### Step 1: Identify the Trust Mechanism

**Core question:** What must be true for the system to be safe?

**Decision rules:**

- Collateral must be real, accessible, valued correctly, and legally claimable.
- Disclosure must let outsiders understand exposure before loss.
- Reputation is not a control.
- Complex counterparties can hide concentration risk.

**Ask the user:** What asset, promise, or institution is everyone trusting?

**Citation instruction:** Cite `REF-M6-001` or `REF-M6-002` for salad-oil-style collateral and exposure risk.

### Step 2: Map Hidden Exposure

**Core question:** What losses are visible, and what losses may still be concealed?

**Decision rules:**

| Exposure type | Diagnostic question |
|---|---|
| Collateral | Has it been independently verified? |
| Counterparty | Who fails if the first party fails? |
| Liquidity | Can assets be sold without moving the market? |
| Reputation | Is confidence substituting for control? |
| Rule-maker | Who will be pressured to absorb losses? |

**Citation instruction:** Cite `REF-M6-003` when broader responsibility shifts to an exchange or institution.

### Step 3: Identify Contagion and Controls

**Core question:** How does private failure become institutional fragility?

**Decision rules:**

- Fragility rises when losses threaten market confidence, settlement, or public trust.
- Controls must change verification, collateral, disclosure, incentives, or exit rules.
- Rescue can reduce panic while preserving moral hazard if consequences are weak.

**Citation instruction:** Cite `REF-M6-004` for central-bank or system-stabilizing functions.

## Output Format

```markdown
## Fragility Diagnosis
- Trust mechanism:
- Visible loss:
- Hidden exposure:
- Brooks parallel:

## Exposure Map
- Collateral:
- Counterparties:
- Liquidity:
- Institution expected to absorb loss:
- Contagion path:

## Safeguards
- Verify:
- Disclose:
- Limit:
- Exit trigger:

## Sources
- REF-M6-...
```

## Do Not

- Do not accept collateral or disclosure at face value when the question is trust.
- Do not ignore who absorbs losses when a private failure threatens a public market.
- Do not recommend confidence-building gestures without structural controls.
