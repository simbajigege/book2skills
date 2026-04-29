# Skill: Enterprising Bargain Hunt (The Intelligent Investor / Module 7)

**Knowledge source:** *The Intelligent Investor* by Benjamin Graham.
**Reference library:** `references/case_library.md`
**Standalone use:** This module can run independently or as part of `../../SKILL.md`.

## When to Use

Use this module when the user is an enterprising investor asking how to find Graham-style bargains, secondary companies, net-current-asset stocks, special situations, or unpopular securities.

## Module Inputs

- User's willingness and ability to do detailed work.
- Screen results or candidate list.
- Current assets, total liabilities, preferred stock, shares outstanding.
- Earnings record and current losses if any.
- Liquidity, governance, and catalyst information.
- Diversification plan.

## Module Outputs

- Bargain category classification.
- NCAV or asset-backing calculation when possible.
- Rejection flags.
- Research checklist.
- Portfolio construction warning.
- Citation IDs.

## Execution Flow

### Overview

1. Confirm enterprising posture.
2. Identify bargain category.
3. Verify asset or earnings support.
4. Reject value traps and promotional situations.
5. Require diversification.

### Step 1: Confirm Enterprising Posture

**Core question:** Is the user willing to do more work than the defensive investor?

**Decision rules:**

- If no, route to M5/M6 defensive defaults instead.
- If yes, proceed but state that extra return must come from extra analysis and discipline, not extra optimism.

### Step 2: Identify Bargain Type

| Bargain type | Required evidence | Key risk |
|---|---|---|
| Net-current-asset bargain | Price below conservatively calculated current assets less all liabilities | Assets overstated or cash burn continues |
| Secondary company discount | Sound but unpopular company priced below conservative value | Permanent competitive weakness |
| Special situation | Contractual or event-driven value with defined terms | Deal break, timing, legal complexity |
| Low-multiple stock | Stable normalized earnings at low price | Cyclical peak or accounting illusion |

**Citation instruction:** Cite `REF-M7-001` for NCAV bargains.

### Step 3: Verify the Bargain

**Checklist:**

- Calculate NCAV conservatively: current assets minus total liabilities and senior claims.
- Exclude inventory or receivables quality concerns where appropriate.
- Check whether the company is losing money fast enough to consume the bargain.
- Review debt maturities, dilution, governance, and shareholder treatment.
- Compare price to normalized earnings and book value.

**Citation instruction:** Cite `REF-M7-002` when earnings quality is central.

### Step 4: Diversify and Reject

**Decision rules:**

- Graham-style bargain investing depends on a group of statistically cheap securities, not one heroic pick.
- Reject if the only upside comes from a story, promotion, or hoped-for turnaround without asset or earnings support.
- Reject if management can destroy or withhold value from outside shareholders.

## Output Format

```markdown
## Enterprising Graham Bargain Review — [Candidate]

**Bargain category:** NCAV / Secondary company / Special situation / Low multiple / Not a Graham bargain

| Test | Result | Evidence |
|---|---|---|
| Conservative asset support | ... | ... |
| Earnings reality | ... | ... |
| Balance-sheet risk | ... | ... |
| Shareholder treatment | ... | ... |
| Diversification suitability | ... | ... |

**Verdict:** Research further / Reject / Speculative only / Candidate for diversified bargain basket
**Next research steps:** ...
**Citations:** REF-M7-...
```

## Do Not

- Do not recommend a single deep bargain as if diversification were unnecessary.
- Do not ignore cash burn, dilution, or governance.
- Do not treat low P/E alone as proof of value.
