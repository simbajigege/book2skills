---
name: creating-superfans-hodak
description: Apply Brittany Hodak's SUPER Model for customer loyalty, referrals, word of mouth, personalization, service recovery, and scalable customer experience.
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

# Creating Superfans - Skill (Brittany Hodak)

**Knowledge source:** *Creating Superfans: Turning Everyday Customers into Enthusiastic Advocates* by Brittany Hodak, 2023.
**Architecture:** Orchestrator + 7 subskills. This file routes the user query; subskills execute the actual workflows.

```text
creating-superfans-hodak/
├── SKILL.md
└── subskills/
    ├── m1_superfan_diagnosis/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m2_story_positioning/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m3_customer_understanding/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m4_personalization/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m5_exceed_expectations/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m6_service_recovery/
    │   ├── module.md
    │   └── references/case_library.md
    └── m7_repeatable_supergroups/
        ├── module.md
        └── references/case_library.md
```

## Skill Purpose

Help founders, marketers, sales teams, customer success leaders, support teams, and operators turn ordinary customers into enthusiastic advocates. Hodak's core idea is that superfans are created where the brand's story intersects with the customer's story, then reinforced through understanding, personalization, expectation-exceeding experiences, recovery, and repeatable systems.

This is not a paid ads, SEO, pricing, funnel analytics, or generic growth-hacking playbook. Use it when the question involves customer experience, loyalty, retention, referrals, reviews, advocacy, service recovery, or cross-functional customer centricity.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Output | Subskill |
|----------|----------------------|--------|--------|----------|
| Superfan diagnosis | "Why are customers not coming back or referring?" | Customer segment, current journey, retention/referral symptoms | Ladder stage, apathy diagnosis, weak SUPER pillar | M1 |
| Story positioning | "How do we differentiate without lowering price?" | Brand origin, values, market, customer promise | Story intersection and category-of-one positioning | M2 |
| Customer understanding | "Who are our customers and what do they really want?" | Customer type, conversations, reviews, support notes | Customer STORY map and voice-of-customer questions | M3 |
| Personalization | "How do we make customers feel seen?" | Customer signals, CRM fields, journey stage, boundaries | Personalization actions and triggers | M4 |
| Exceed expectations | "How do we create word of mouth or memorable experiences?" | Journey touchpoints, expectations, emotional moments | Repeatable experience moments and advocacy triggers | M5 |
| Service recovery | "A customer had a bad experience. What should we do?" | Failure details, customer impact, relationship context | 5 As recovery plan and prevention fix | M6 |
| Repeatable supergroups | "How do we scale CX across teams?" | Team structure, processes, feedback loops, employee experience | System, ownership, metrics, and cross-functional rollout | M7 |

## When to Use This Skill

Use this skill when the user asks how to:

- Increase retention, repeat purchase, referrals, reviews, advocacy, or word of mouth
- Diagnose why customers are satisfied but quiet
- Differentiate a brand when products, prices, or features look similar
- Improve customer experience across marketing, sales, onboarding, service, community, or social media
- Personalize customer touchpoints without becoming intrusive
- Recover from a bad customer experience
- Scale excellent service through systems rather than founder heroics
- Build a more customer-centric team culture

## Routing Rules

| User question type | Must run | Optional run |
|--------------------|----------|--------------|
| "How do I improve retention or repeat purchase?" | M1 -> M3 -> M5 -> M7 | M4 |
| "How do I get more referrals or word of mouth?" | M1 -> M2 -> M5 -> M7 | M4 |
| "How do I differentiate without lowering price?" | M2 -> M3 -> M5 | M7 |
| "How do I understand my customers better?" | M3 | M1 |
| "How do I personalize this journey/message/gift?" | M3 -> M4 | M7 |
| "How do I wow customers?" | M5 | M3, M4, M7 |
| "A customer had a bad experience. What should I do?" | M6 -> M7 | M3 |
| "How do I scale customer experience as we grow?" | M1 -> M7 | M2 through M6 as needed |
| "How should marketing/sales/support/social apply SUPER?" | M7 | M2, M3, M5, M6 |

## Execution Rules

1. Read only the modules required by the routing table.
2. If a module depends on upstream context, run the upstream module first.
3. Pass each module's output into the next module when routed as a sequence.
4. If context is thin, ask for the customer type, product or service, current touchpoints, retention/referral symptoms, and one recent customer interaction.
5. Do not run every module for a narrow question.
6. Every substantive recommendation should cite the relevant module's `references/case_library.md`.
7. Keep direct quotes short and use them as evidence, not as the answer.

## Citation Rules

Each module owns its own citation library:

- M1 and M2 use `main-framework-quotes.md` copied into their module reference libraries.
- M3 uses `customer-understanding-quotes.md`.
- M4 uses `personalization-quotes.md`.
- M5 uses `exceeding-expectations-quotes.md`.
- M6 uses `apology-recovery-quotes.md`.
- M7 uses repeatability, experience measurement, and organization-wide customer centricity references.

When a routed module contains a "Citation instruction," read that module's `references/case_library.md`, select the closest anchor, and include a short citation in the answer.

## Multi-Module Output Format

For substantial answers, use this structure:

```text
Creating Superfans diagnosis - [Business / Situation]

1. Current superfan stage
   - Ladder stage:
   - Apathy risk:
   - Weakest SUPER pillar:

2. Hodak principle being applied
   - [Short principle with citation]

3. Action plan
   - [2-5 specific touchpoint or system changes]

4. Artifact
   - [Script, checklist, journey map, CRM trigger, service recovery draft, or team routine when useful]

5. Measurement
   - Behavior metric:
   - Customer-story signal:

6. Watch-outs
   - [The mistake most likely to weaken the plan]
```

For quick answers, provide the diagnosis, the next action, and one citation.

## Subskill Status

| Subskill | Path | Status |
|----------|------|--------|
| M1 Superfan Diagnosis | `subskills/m1_superfan_diagnosis/` | Available |
| M2 Story Positioning | `subskills/m2_story_positioning/` | Available |
| M3 Customer Understanding | `subskills/m3_customer_understanding/` | Available |
| M4 Personalization | `subskills/m4_personalization/` | Available |
| M5 Exceed Expectations | `subskills/m5_exceed_expectations/` | Available |
| M6 Service Recovery | `subskills/m6_service_recovery/` | Available |
| M7 Repeatable Supergroups | `subskills/m7_repeatable_supergroups/` | Available |

## Do Not

- Do not confuse awareness with caring; many growth problems are apathy problems.
- Do not treat satisfied customers as superfans unless they advocate voluntarily.
- Do not prescribe tactics before connecting the brand's story to the customer's story.
- Do not recommend personalization that is intrusive, creepy, or primarily brand-centered.
- Do not suggest grand gestures before fixing basic consistency.
- Do not treat service recovery as only compensation; require emotional repair and system repair.
- Do not tolerate abusive or wrong-fit customers in the name of customer centricity.
- Do not let customer experience depend on a single heroic employee.
