# Skill: Failure Diagnosis (Business Adventures — Module 1)

**Knowledge source:** *Business Adventures* by John Brooks  
**Reference library:** `references/case_library.md`  
**Standalone use:** This module can run independently or as part of `../../SKILL.md`.

## When to Use

Use this module when the user asks why a company, product, strategy, campaign, or institution failed, or when they want a Brooks-style postmortem of a business case.

## Module Inputs

- Organization, product, or decision being diagnosed
- Timeline of key decisions and market changes
- Known incentives, constraints, and internal commitments
- Evidence of customer, investor, employee, regulator, or partner response

## Module Outputs

- Primary Brooks failure pattern
- Decision chain from trigger to consequence
- Preventable warning signals
- Most relevant historical parallel
- Practical change recommendation

## Execution Flow

### Overview

```text
Failure diagnosis
├── Step 1: Identify the human pattern
├── Step 2: Reconstruct the decision chain
├── Step 3: Separate trigger from amplifier
├── Step 4: Match the closest Brooks case
└── Step 5: Produce the correction
```

### Step 1: Identify the Human Pattern

**Core question:** What repeatable human behavior is driving the failure: hubris, panic, drift, secrecy, complacency, sunk cost, or rule exploitation?

**Decision rules:**

| Signal | Pattern |
|---|---|
| Planning continues after customer evidence weakens | Sunk-cost momentum |
| Formal policy diverges from incentives | Communication failure |
| Success creates market blindness | Complacency |
| Legal tolerance is treated as permanent safety | Regulatory lag |
| Price moves or crowd reaction drive decisions | Panic dynamics |

**Ask the user:** What decision looked rational internally but failed externally?

**Citation instruction:** For broad Brooks pattern framing, cite `REF-M1-001`. For product-planning failure, cite `REF-M1-002`.

### Step 2: Reconstruct the Decision Chain

**Core question:** Which decisions turned an ordinary problem into a failure?

**Decision rules:**

- Identify the first avoidable decision.
- Identify the point where evidence changed but the organization did not.
- Identify who benefited from continuing the old path.
- Separate execution mistakes from strategic mismatch.

**Ask the user:** What evidence did leaders have before the failure became public?

**Citation instruction:** When the failure involves internal communication or policy-execution gaps, cite `REF-M1-003`.

### Step 3: Separate Trigger From Amplifier

**Core question:** What started the failure, and what made it larger?

**Decision rules:**

- Trigger: the initial market, product, legal, or operational event.
- Amplifier: leverage, media, incentives, delayed information, rule changes, distribution weakness, or governance theater.
- Consequence: customer loss, capital loss, legal exposure, reputation loss, or institutional intervention.

**Ask the user:** Which part of the damage was inevitable, and which part came from the response?

**Citation instruction:** If the amplifier is market psychology, cite `REF-M1-004`.

### Step 4: Match the Closest Brooks Case

**Core question:** Which Brooks episode gives the best diagnostic parallel without overfitting?

**Decision rules:**

| Current case resembles | Use when |
|---|---|
| Edsel | Planning, research, name, timing, and market fit break down |
| Xerox | Breakthrough creates a market faster than incumbents understand |
| Texas Gulf Sulphur | Information advantage and disclosure timing create legal risk |
| Piggly Wiggly | Market structure and rule-makers shape the outcome |
| 1962 crash | Psychology and market plumbing amplify fear |
| Salad oil scandal | Trust, collateral, and institutional responsibility fail |

**Citation instruction:** Cite the module reference that matches the selected case.

## Output Format

```markdown
## Brooks Failure Diagnosis
- Case:
- Primary pattern:
- Closest Brooks parallel:

## Decision Chain
- Trigger:
- First avoidable decision:
- Amplifiers:
- Warning signals:
- Missing facts:

## Recommendation
- What should change:
- What to stop:
- What to monitor:
- What would change this diagnosis:

## Sources
- REF-M1-...
```

## Do Not

- Do not reduce a failure to a single villain if incentives made the conduct predictable.
- Do not treat a historical parallel as proof that the same outcome will repeat.
- Do not ignore timing, distribution, rules, and information flow.
