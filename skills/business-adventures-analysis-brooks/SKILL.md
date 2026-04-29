---
name: business-adventures-analysis-brooks
description: Use Business Adventures for "why did this fail?", "analyze this crisis", "what pattern applies?", or "what would Brooks notice?"
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

# Business Adventures Analysis — Skill (John Brooks)

**Knowledge source:** *Business Adventures* by John Brooks.
**Architecture:** Orchestrator + 6 subskills. The main `SKILL.md` routes the user query; subskills execute the diagnostic workflows and own their reference IDs.

```text
business-adventures-analysis-brooks/
├── SKILL.md
├── quotes/
└── subskills/
    ├── m1_failure_diagnosis/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m2_market_panic/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m3_regulatory_risk/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m4_product_innovation/
    │   ├── module.md
    │   └── references/case_library.md
    ├── m5_governance_accountability/
    │   ├── module.md
    │   └── references/case_library.md
    └── m6_fraud_institutional_fragility/
        ├── module.md
        └── references/case_library.md
```

## Skill Purpose

Use this skill to apply John Brooks's *Business Adventures* as a diagnostic framework for corporate failures, market panics, product launches, governance breakdowns, regulatory risk, fraud, innovation, and financial culture.

The skill does not summarize the book or predict the future by analogy. It maps a live business situation to recurring Brooks patterns: panic, hubris, communication failure, incentive drift, regulatory lag, product-market mismatch, and institutional fragility.

## Core Principle

Human nature is the constant; institutions are the variable. Identify the repeating human pattern first, then examine how structure, incentives, rules, timing, and information flow amplify it.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Steps | Output | Should be subskill? |
|---|---|---|---|---|---|
| Failure diagnosis | "Why did this company, product, or strategy fail?" | Company/product, timeline, market context, decisions | Pattern map, decision chain, warning signals, preventable actions | Primary failure pattern and decision correction | Yes |
| Market panic analysis | "What is happening in this crash?" | Trigger, price moves, liquidity, media, forced sellers | Panic phase, technical amplifiers, stabilizers, uncertainty | Panic diagnosis and stabilizer map | Yes |
| Regulatory risk review | "Is this practice risky?" | Practice, disclosure, materiality, enforcement context | Materiality, public usability, tolerated-practice risk, rule-change trigger | Risk level and action | Yes |
| Product and innovation review | "Will this launch or innovation work?" | Product, customers, incumbents, distribution, research | Timing test, differentiation, incumbent blind spots, commercialization | Stop/redesign/accelerate/monitor recommendation | Yes |
| Governance accountability | "Is management handling this well?" | Board, incentives, crisis response, shareholder/stakeholder power | Formal power vs real consequences, incentives, accountability | Governance diagnosis | Yes |
| Fraud and institutional fragility | "How exposed is this system?" | Trust mechanism, counterparties, collateral, disclosure, losses | Hidden exposure, responsibility transfer, contagion path, controls | Fragility map and safeguards | Yes |

## When to Use This Skill

Invoke this skill when the user asks:

- "Why did this company, product, or strategy fail?"
- "Analyze this business case."
- "What historical pattern does this resemble?"
- "What would John Brooks say about this crisis?"
- "Is this governance, compliance, or regulatory behavior a warning sign?"
- "How do market panics typically unfold?"
- "What lessons from Edsel, Xerox, Texas Gulf Sulphur, Piggly Wiggly, or the 1962 crash apply here?"

## Routing Rules

| User question type | Must run | Optional run |
|---|---|---|
| Broad case diagnosis or postmortem | M1 Failure Diagnosis | M3, M4, M5, or M6 depending on facts |
| Market crash, liquidity stress, speculative mania, selloff | M2 Market Panic | M6 if counterparties or technical systems are central |
| Insider information, disclosure, antitrust, tax, tolerated practice | M3 Regulatory Risk | M5 if board/executive accountability matters |
| Product launch, failed product, innovation, incumbent blindness | M4 Product and Innovation | M1 for full failure postmortem |
| Board conduct, shareholder power, executive accountability, crisis leadership | M5 Governance Accountability | M3 if legal exposure is material |
| Fraud, collateral failure, hidden exposure, systemic support, institutional trust | M6 Fraud and Institutional Fragility | M2 if panic dynamics are present |
| User asks only for historical parallel | Run the closest single module | M1 if the parallel needs a broader diagnosis |

## Execution Rules

1. Read only the modules required by the routing table.
2. If the user gives a broad failure question, run M1 first and then route to the most relevant specialist module.
3. If the user data is thin, ask for the missing timeline, actors, incentives, disclosures, and consequences before giving a confident diagnosis.
4. Do not run every module for a narrow question.
5. Use historical parallels as diagnostic lenses, not as predictions.
6. Each module owns its reference IDs in `references/case_library.md`; when citing Brooks-derived claims, use the IDs from the module actually run.

## Multi-Module Output Format

```markdown
## Brooks Pattern Diagnosis
- Situation:
- Primary module:
- Supporting modules:
- Active human pattern:
- Closest historical parallel:

## Diagnostic Chain
- Trigger:
- Decisions:
- Incentives:
- Amplifiers:
- Warning signals:
- Missing facts:

## Risk / Opportunity
- Current risk:
- Latent risk:
- Rule-maker, stabilizer, or accountable actor:
- What would change the diagnosis:

## Recommendation
- Continue / change / stop:
- Immediate action:
- What to monitor:
- Evidence needed next:

## Sources
- REF-...
```

## Subskill Status

| Subskill | Path | Status |
|---|---|---|
| M1 Failure Diagnosis | `subskills/m1_failure_diagnosis/` | Available |
| M2 Market Panic | `subskills/m2_market_panic/` | Available |
| M3 Regulatory Risk | `subskills/m3_regulatory_risk/` | Available |
| M4 Product and Innovation | `subskills/m4_product_innovation/` | Available |
| M5 Governance Accountability | `subskills/m5_governance_accountability/` | Available |
| M6 Fraud and Institutional Fragility | `subskills/m6_fraud_institutional_fragility/` | Available |

## CITATION RULES

When the user asks for sources, or when producing a formal analysis, cite the quote files for Brooks-derived principles. Each routed module has a `references/case_library.md` with stable IDs mapped to the quote files and anchors below.

**Quote files:**

- `quotes/market-dynamics-quotes.md` — market fluctuation, panic psychology, technical breakdown, speculative cycles.
- `quotes/corporate-strategy-quotes.md` — product failure, Edsel, Xerox, innovation, corporate decline.
- `quotes/risk-crisis-quotes.md` — fraud, crisis, regulation, institutional fragility.
- `quotes/investor-behavior-quotes.md` — stockholder power, speculation, Wall Street behavior.
- `quotes/wall-street-wisdom-quotes.md` — finance culture and recurring market lessons.

**Anchor mapping:**

- `market-dynamics-quotes.md`: `#market-will-fluctuate`, `#morgans-maxim`, `#antiperistasis-defined`, `#expectation-vs-event`, `#tape-delay-consequences`, `#panic-psychology`, `#crisis-creates-chaos`, `#psychological-gestures`, `#bellwether-stocks`, `#round-number-psychology`, `#specialist-wisdom`, `#crisis-unfathomable`, `#speculative-cycles`, `#sweetness-of-honey`
- `corporate-strategy-quotes.md`: `#edsel-market-research`, `#car-personality`, `#edsel-name-decision`, `#timing-risk`, `#kaiser-lesson`, `#styling-decisions`, `#image-conflict`, `#copies-stigma`, `#copies-suspicion`, `#corner-game`, `#tragic-flaw`, `#communication-problem`, `#corporate-power`, `#meeting-authority`
- `risk-crisis-quotes.md`: `#insider-information-value`, `#stacked-deck`, `#insider-incentive`, `#haupt-risk`, `#vegetable-oil-exposure`, `#exchange-responsibility`, `#sherman-act`, `#conspiracy-concealment`, `#price-fixing-penalty`, `#central-bank-purpose`, `#federal-reserve-role`, `#tax-law-scope`, `#two-currencies`
- `investor-behavior-quotes.md`: `#never-give-advice`, `#entertainment-vs-greed`, `#jokes-as-attraction`, `#walk-ins-as-indicator`, `#lunch-hour-selling`, `#who-sold-in-crash`, `#mutual-funds-as-stabilizer`, `#funds-spotted-bargains`, `#losing-other-peoples-money`, `#fear-of-fund-redemptions`, `#air-of-unreality`, `#public-individuals-role`, `#margin-call-spiral`
- `wall-street-wisdom-quotes.md`: `#market-fragility`, `#edsel-lesson`, `#salad-oil-swindle`, `#stockholder-decline`, `#xerox-complacency`, `#go-go-years`, `#de-la-vega-observation`

**Citation format:**

```markdown
> "Author's exact words here."
>
> - [*Business Adventures*, cited excerpt](https://github.com/simbajigege/book2skills/blob/main/skills/business-adventures-analysis-brooks/quotes/market-dynamics-quotes.md#panic-psychology)
```

Use only exact quote text from the quote files. If no exact quote fits, cite the closest anchor or module reference ID and state that the reasoning is a paraphrased Brooks application.

## Do Not

- Do not treat historical parallels as deterministic forecasts.
- Do not explain a failure only with personality when incentives or structure made the behavior rational.
- Do not assume preparation, research, or capital equals product-market fit.
- Do not treat tolerated practices as safe when materiality, visibility, or public pressure can change enforcement.
- Do not confuse governance process with accountability.
- Do not cite quote text unless it appears in `quotes/` or a module `case_library.md`.
