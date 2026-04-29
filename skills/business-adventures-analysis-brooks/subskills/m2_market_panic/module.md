# Skill: Market Panic Analysis (Business Adventures — Module 2)

**Knowledge source:** *Business Adventures* by John Brooks  
**Reference library:** `references/case_library.md`  
**Standalone use:** This module can run independently or as part of `../../SKILL.md`.

## When to Use

Use this module for market crashes, sudden selloffs, speculative manias, liquidity stress, margin-call spirals, delayed information, or questions about how panic unfolds.

## Module Inputs

- Market or security involved
- Trigger event and price movement
- Liquidity, margin, redemption, or forced-selling evidence
- Information quality and media/institutional response
- Possible stabilizers or rule-makers

## Module Outputs

- Panic phase assessment
- Trigger/amplifier separation
- Stabilizer and rule-maker map
- Signals that would confirm or weaken the panic diagnosis

## Execution Flow

### Overview

```text
Market panic
├── Step 1: Identify trigger
├── Step 2: Diagnose technical amplifiers
├── Step 3: Track psychology and narrative escalation
├── Step 4: Identify stabilizers and rule-makers
└── Step 5: State uncertainty and monitoring signals
```

### Step 1: Identify Trigger

**Core question:** Did new fundamental information start the move, or did market fear become the event?

**Decision rules:**

- Fundamental trigger: earnings, credit loss, policy shock, fraud, macro news.
- Technical trigger: leverage unwind, forced redemptions, short squeeze, settlement strain.
- Reflexive trigger: price decline causes fear, which causes further selling.

**Ask the user:** What was known before the price move, and what became known only after it started?

**Citation instruction:** Cite `REF-M2-001` for the principle that market fluctuation itself is an enduring fact.

### Step 2: Diagnose Technical Amplifiers

**Core question:** What market plumbing is amplifying the psychological move?

**Decision rules:**

| Amplifier | Evidence |
|---|---|
| Delayed information | Tape, quote, or reporting lag |
| Forced selling | Margin calls, redemptions, risk limits |
| Liquidity gap | Wider spreads, failed execution, absent buyers |
| Mechanical thresholds | Round numbers, index levels, collateral triggers |

**Ask the user:** Are sellers choosing to sell, or are they being forced to sell?

**Citation instruction:** Cite `REF-M2-002`, `REF-M2-003`, or `REF-M2-004` when those mechanisms are central.

### Step 3: Track Psychology

**Core question:** Is the dominant fear about the underlying asset, or about other participants' reactions?

**Decision rules:**

- Panic is likely when participants act on incomplete information as if it were certain.
- Narrative escalation is likely when media interpretation becomes evidence for further selling.
- Stabilization becomes credible only when identifiable buyers have capacity and incentive.

**Citation instruction:** Cite `REF-M2-005` for panic psychology and `REF-M2-006` for bargain-hunter stabilization.

## Output Format

```markdown
## Market Panic Diagnosis
- Market/security:
- Trigger:
- Panic phase:
- Fundamental news vs technical pressure:

## Amplifiers
- Forced sellers:
- Liquidity stress:
- Information delay:
- Narrative escalation:

## Stabilizers
- Potential buyers:
- Rule-makers:
- What to monitor:
- What would disconfirm panic:

## Sources
- REF-M2-...
```

## Do Not

- Do not explain every price move as fundamentals.
- Do not assume stabilizing buyers exist without identifying their incentives.
- Do not give a certainty level higher than the available information supports.
