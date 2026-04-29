# Skill: Superfan Diagnosis (Creating Superfans - Module 1)

**Knowledge source:** *Creating Superfans* by Brittany Hodak.
**Reference library:** `references/case_library.md`
**Standalone use:** This module can run independently or as the first diagnostic step for `../../SKILL.md`.

## When to Use

Use this module when the user asks why customers are not buying again, referring, reviewing, talking about the brand, or caring enough to act. Also use it when the user wants "more awareness" but has not checked retention, advocacy, or apathy.

## Module Inputs

- Business, product, or service description
- Target customer segment
- Current acquisition, retention, referral, review, or repeat-purchase symptoms
- Known customer journey touchpoints
- Any recent customer comments, reviews, support issues, churn notes, or silence patterns

## Module Outputs

Return a superfan diagnosis with:
- Current Ladder to Superfandom stage
- Awareness vs apathy distinction
- Weakest SUPER pillar
- Next modules to run
- One or two missing questions if the diagnosis is under-specified

## Execution Flow

### Overview

```text
Identify symptom -> place audience on ladder -> separate awareness from apathy -> find weak SUPER pillar -> route next workflow
```

### Step 1: Classify the business problem

**Core question:** Is this truly an awareness problem, or do customers know the brand but not care enough to act?

**Decision rules:**

| Signal | Diagnosis |
|--------|-----------|
| Target customers do not know the brand exists | Awareness issue |
| Customers know the brand but do not buy | Apathy or weak story issue |
| Customers buy once but do not return | Adoption or experience issue |
| Customers like the brand but do not refer | Affinity-to-advocacy issue |
| Customers used to advocate but stopped | Consistency or expectation issue |

**Ask the user:** Who already knows you exist? What do they do next? Where does the journey stall?

**Citation instruction:** When distinguishing awareness from apathy, cite `#great-is-no-longer-good-enough` or `#superfans-created-at-intersection`.

### Step 2: Place customers on the Ladder to Superfandom

**Core question:** Where are customers stuck between apathy, awareness, attraction, action, adoption, affinity, and advocacy?

**Decision rules:**

| Stage | Observable symptom |
|-------|--------------------|
| Apathy | They do not care enough to notice or act |
| Awareness | They recognize the brand but have no reason to choose it |
| Attraction | They show interest but do not buy |
| Action | They buy once |
| Adoption | They repeat or integrate the brand into routine |
| Affinity | They like the brand |
| Advocacy | They voluntarily recommend, review, defend, or share |

**Ask the user:** What percentage of first-time customers return, review, refer, or mention the brand unprompted?

**Citation instruction:** When defining superfans, cite `#superfan-definition`.

### Step 3: Identify the weakest SUPER pillar

**Core question:** Which pillar is most likely blocking progress to advocacy?

**Decision rules:**

| Weakness | Route next |
|----------|------------|
| Brand feels generic | M2 Story Positioning |
| Customer motives are unclear | M3 Customer Understanding |
| Experience feels impersonal | M4 Personalization |
| Experience is adequate but forgettable | M5 Exceed Expectations |
| Good moments are inconsistent | M7 Repeatable Supergroups |
| Recent failure damaged trust | M6 Service Recovery |

**Ask the user:** If one touchpoint had to explain why customers stay quiet, which one would it be?

**Citation instruction:** When introducing the full model, cite `#the-super-model`.

## Output Format

```text
M1 - Superfan Diagnosis

Ladder stage: [stage]
Problem type: [awareness / apathy / adoption / advocacy / consistency]
Weakest SUPER pillar: [Story / Understanding / Personalization / Expectations / Repeatability]

Evidence:
- [Observed symptom]

Next module:
- [M2/M3/M4/M5/M6/M7 and why]

Citation:
- [Short quote or paraphrase with anchor]
```

## Do Not

- Do not assume low growth means low awareness.
- Do not treat silence as satisfaction.
- Do not prescribe referrals before identifying whether customers have reached affinity.
- Do not skip this module when the user gives a broad retention, referral, or loyalty problem.
