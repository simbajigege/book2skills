---
name: munger-mental-models-worldly-wisdom
description: Apply Charlie Munger mental models to investments, decisions, and bias diagnosis. Trigger on Munger checklist or spot biases.
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

## Overview

This skill turns Charlie Munger's *Poor Charlie's Almanack* into an executable decision tool for investment evaluation, business judgment, and psychological misjudgment diagnosis. It helps users combine multidisciplinary mental models, inversion, circle-of-competence discipline, and bias checklists into structured recommendations.

## When to Use This Skill

- The user asks to analyze an investment, company, business decision, or strategy using Charlie Munger's approach.
- The user asks which mental models apply to a situation.
- The user wants to diagnose cognitive biases, market manias, frauds, scandals, or irrational behavior.
- The user wants a checklist for decision quality, preparation, patience, concentration, or opportunity cost.
- The user asks what could go wrong and how to invert a plan before acting.

## HOW TO USE THIS SKILL

1. Classify the user's request as investment evaluation, bias diagnosis, general decision review, or Munger-style synthesis.
2. Apply only the dimensions required by the query. Do not force every checklist into a narrow question.
3. Start with competence boundaries and inversion whenever the user asks for a recommendation.
4. Use citations for major Munger-derived claims by loading the closest relevant quote file and citing an anchor.
5. If the user needs current market or company facts, state what data is missing or browse current sources if available.

## CITATION RULES

Every substantive claim based on Munger's methodology must include a citation to the original text.

**Quote files (load the relevant one):**

- `main-framework-quotes.md`: broad framework statements, latticework language, and general book framing.
- `mental-models-quotes.md`: multiple mental models, multidisciplinary analysis, and business assessment.
- `worldly-wisdom-quotes.md`: worldly wisdom, circle of competence, checklists, and learning discipline.

**Citation format - always use this exact structure:**

> "Author's exact words here."
>
> - *Poor Charlie's Almanack*, topic anchor: https://github.com/simbajigege/book2skills/blob/main/skills/munger-mental-models-worldly-wisdom/quotes/FILENAME.md#ANCHOR

**Anchor mapping:**

- `main-framework-quotes.md`: `#quote-1`, `#quote-2`, `#quote-3`, `#quote-4`, `#quote-5`, `#quote-6`, `#quote-7`, `#quote-8`, `#quote-9`, `#quote-10`, `#quote-11`, `#quote-12`, `#quote-13`, `#quote-14`, `#quote-15`
- `mental-models-quotes.md`: `#mental-model-1`, `#mental-model-2`, `#mental-model-3`, `#mental-model-4`, `#mental-model-5`, `#mental-model-6`, `#mental-model-7`
- `worldly-wisdom-quotes.md`: `#wisdom-1`, `#wisdom-2`, `#wisdom-3`, `#wisdom-4`, `#wisdom-5`, `#wisdom-6`, `#wisdom-7`, `#wisdom-8`, `#wisdom-9`, `#wisdom-10`

**Rules:**

- Include at least one citation in each major response section that relies on Munger's method.
- Match the citation to the closest principle: mental models, worldly wisdom, or checklist discipline.
- If no exact quote matches a point, cite the closest chapter anchor and label the point as a paraphrase.
- Do not reproduce long passages in the answer. Quote briefly, then paraphrase the practical rule.

## Core Principle

Reliable judgment comes from building a latticework of the big ideas across disciplines, then applying them with humility, inversion, and bias control. A single favorite model is dangerous; the agent must combine models, know when a problem is outside its competence, and search first for failure modes.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Steps | Output | Independent trigger? | Distinct references? | Triage score | Should be subskill? | Reason |
|---|---|---|---|---|---|---|---:|---|---|
| Investment quality review | Analyze this company using Munger | Company facts, business model, valuation, moat evidence | Competence boundary -> inversion -> models -> 10 principles -> bias check | Investment scorecard and verdict | Yes | Partly | 3 | No | Independently triggerable, but uses the same shared dimensions and output grammar as the broader decision workflow. |
| Mental-model mapping | What models apply here? | Situation description and decision goal | Identify disciplines -> apply models -> synthesize implications | Cross-disciplinary model table | Yes | Yes | 3 | No | It is a slice of the primary workflow; keeping it as a dimension avoids a separate module with duplicated model lists. |
| Bias and misjudgment diagnosis | What biases are active here? | Behavior, incentives, social context, outcome | Scan tendencies -> detect reinforcing combinations -> prescribe antidotes | Bias map and corrective actions | Yes | Partly | 3 | No | Separately triggerable but compact enough to remain a dimension; it shares citation and output conventions. |
| Inversion review | What could make this fail? | Plan, assumptions, constraints | Name failure modes -> rank severity/probability -> safeguards | Failure-mode checklist | Yes | No | 2 | No | It is a universal step inside all recommendation workflows. |
| Circle of competence triage | Should I even analyze this? | User knowledge, domain complexity, data quality | Test understanding -> mark known/unknown -> decide too-hard or proceed | Competence boundary and data request | Yes | No | 2 | No | It gates the other workflows rather than producing a standalone method. |

## Architecture Justification

Use a single-file skill because Munger's method is a compact decision discipline built from tightly coupled checks. The workflows are independently triggerable, but they use the same repeated reasoning sequence: competence boundary, inversion, multidisciplinary models, psychological bias control, and disciplined output. Splitting them into subskills would duplicate the central model list and make narrow questions heavier rather than clearer.

## DIMENSION 1: Latticework of Mental Models

**The Rule:** Do not analyze a complex problem through one favored lens; combine big ideas from several disciplines and look for their interactions.

### Key questions to ask:

- Which disciplines are relevant: mathematics, psychology, physics, biology, economics, engineering, history, or accounting?
- What does each discipline suggest that the others might miss?
- Which variables interact or reinforce each other?
- What second-order effect follows if the obvious first-order outcome happens?
- Is the user using one model because it is useful, or because it is familiar?

### Decision criteria / Checklist:

- Identify at least three relevant disciplines for broad decisions.
- Separate first-order, second-order, and feedback-loop effects.
- Check base rates before accepting a vivid story.
- Use opportunity cost whenever comparing alternatives.
- Mark the problem as too hard if the model outputs conflict and key facts are missing.

### Warning signals:

- One-metric reasoning, such as relying only on P/E, growth, market share, or narrative strength.
- Claims that ignore incentives, competition, or feedback loops.
- Treating a spreadsheet as truth when assumptions drive the result.
- Explaining a social system while ignoring psychology.

### Agent instruction:

When the user presents a business, investment, policy, or life decision, name the 3-5 most relevant models, explain what each model implies, then synthesize where the models agree or conflict. Cite `mental-models-quotes.md` when explaining why multiple models are required.

## DIMENSION 2: Worldly Wisdom and Learning Discipline

**The Rule:** Practical wisdom compounds through broad learning, intellectual humility, and repeated use of checklists.

### Key questions to ask:

- What does the user know firsthand, and what is borrowed confidence?
- Which basic disciplines has the user not consulted?
- Is the decision being rushed before the hard learning has been done?
- What checklist would prevent an obvious mistake?
- What must be practiced or refreshed so the user does not lose the skill?

### Decision criteria / Checklist:

- Define the decision in plain language before analyzing it.
- Convert vague principles into a checklist.
- Distinguish durable knowledge from timely facts.
- Ask for disconfirming evidence before final judgment.
- Track whether the user has done enough preparation for the size of the decision.

### Warning signals:

- Abstract intelligence without preparation.
- Confidence that rises as evidence gets thinner.
- Ignoring old lessons because the current case feels special.
- Refusing simple checklists because the user prefers sophistication.

### Agent instruction:

When the user's question is broad or ambiguous, first turn it into a practical decision and a short checklist. Cite `worldly-wisdom-quotes.md` when explaining learning discipline, wisdom, or checklist use.

## DIMENSION 3: Investment Judgment Checklist

**The Rule:** Good investing requires staying within competence, demanding a margin of safety, comparing opportunity costs, waiting patiently, and acting decisively only when the odds are favorable.

### Key questions to ask:

- Is the business understandable enough for a serious judgment?
- What creates durable competitive advantage, and how could it erode?
- What is the downside if the central thesis is wrong?
- Is the price attractive relative to conservative value, not just relative to excitement?
- What is the next best use of the capital?
- Is the user acting from patience and preparation or from envy, fear, or boredom?

### Decision criteria / Checklist:

| Principle | What to check |
|---|---|
| Risk | Permanent capital loss, leverage, fraud risk, cyclicality, margin of safety |
| Independence | Whether the thesis survives without consensus approval |
| Preparation | Depth of business, industry, and management understanding |
| Humility | Clear statement of what is unknown or outside competence |
| Rigor | Inversion, base rates, incentives, and second-order effects |
| Allocation | Opportunity cost versus other available ideas |
| Patience | Whether inaction is the higher-quality action |
| Decisiveness | Whether the evidence is strong enough for a concentrated action |
| Adaptability | Whether new facts would change the conclusion |
| Focus | Whether the thesis is simple, durable, and worth attention |

### Warning signals:

- Treating volatility as the only risk while ignoring permanent impairment.
- Buying a great business at a price that assumes everything goes right.
- Following admired investors without matching their information, constraints, or time horizon.
- Mistaking activity for progress.

### Agent instruction:

For investment questions, produce a scorecard with `Pass`, `Concern`, or `Unknown` for each principle. End with one of four verdicts: `Act`, `Watch`, `Research More`, or `Too Hard`. Cite the mental-model and worldly-wisdom quote files where the analysis relies on Munger's checklist discipline.

## DIMENSION 4: Psychological Misjudgment and Lollapalooza Effects

**The Rule:** Human judgment is predictably distorted by incentives, social proof, authority, commitment, denial, envy, overconfidence, and other reinforcing tendencies.

### Key questions to ask:

- What incentives are shaping each actor's behavior?
- Which psychological tendencies are active?
- Are multiple tendencies pushing in the same direction?
- Who benefits if the user accepts the story?
- What would a neutral observer think if labels, status, and social proof were removed?

### Decision criteria / Checklist:

- Always check incentives first.
- Look for reinforcing clusters: incentives plus authority, social proof plus scarcity, commitment plus denial, envy plus overconfidence.
- Distinguish a single bias from a system that manufactures misjudgment.
- Prescribe an antidote: checklist, pre-mortem, independent review, incentive redesign, cooling-off period, or smaller bet.

### Warning signals:

- The user defends a prior decision mainly because reversing it is painful.
- Everyone in the room benefits from the same conclusion.
- Authority figures are treated as substitutes for evidence.
- A market or organization rewards behavior that it publicly claims to discourage.

### Agent instruction:

When the user asks about irrational behavior, scandals, bubbles, or personal decision traps, identify active tendencies, check for reinforcing combinations, and give practical antidotes. Cite `main-framework-quotes.md` or `mental-models-quotes.md` when linking the diagnosis back to Munger's framework.

## DIMENSION 5: Inversion and Circle of Competence

**The Rule:** Before arguing for success, identify how the decision fails; before giving confidence, define the boundary of competence.

### Key questions to ask:

- What would make this fail badly?
- Which assumption matters most?
- Which facts would change the recommendation?
- Can the user explain the core mechanism simply?
- Is this decision inside, near the edge of, or outside the user's competence?

### Decision criteria / Checklist:

- List 3-7 failure modes before the positive case.
- Rank failure modes by severity and likelihood.
- Identify the one assumption that carries the most weight.
- State the competence boundary explicitly.
- If the boundary is unclear, ask for missing inputs or recommend the too-hard basket.

### Warning signals:

- Upside-only framing.
- Complex explanations that cannot be simplified.
- No named kill criteria.
- Large bet size near the edge of competence.

### Agent instruction:

For any recommendation, open with a competence and inversion check unless the user asked only for explanation. If the failure modes are severe or unknowable, make the verdict conservative even when upside exists.

## Query Response Framework

### Query Type 1: Analyze an investment or company using Munger

1. Define the business and the user's decision.
2. Run circle-of-competence triage.
3. Invert the thesis with failure modes.
4. Apply 3-5 mental models across disciplines.
5. Run the investment judgment checklist.
6. Scan for psychological misjudgment.
7. Give a verdict, key uncertainties, and next research questions.

### Query Type 2: Diagnose bias, scandal, bubble, or irrational behavior

1. Identify actors, incentives, and the decision environment.
2. Name the active psychological tendencies.
3. Check whether tendencies reinforce each other.
4. Explain what evidence would falsify the diagnosis.
5. Recommend antidotes or controls.

### Query Type 3: Review a strategic or personal decision

1. Translate the issue into a concrete decision.
2. Identify relevant models from multiple disciplines.
3. Invert the plan.
4. Mark competence boundaries and missing facts.
5. Offer a checklist and a conservative action plan.

### Query Type 4: Give a Munger-style synthesis

1. Select the relevant maxims from mental models, worldly wisdom, psychology, and inversion.
2. Explain where the user's framing is too narrow.
3. Give a short practical rule and a checklist the user can reuse.

## Output Format

### For investment evaluations

```markdown
## Munger Analysis: [Company or Investment]

### Decision and Data Quality
[What decision is being made, what data is known, and what is missing.]

### Circle of Competence
[Inside / Edge / Outside / Too Hard, with reason.]

### Inversion: How This Fails
| Failure mode | Severity | Likelihood | Evidence to check |
|---|---|---|---|

### Mental Models Applied
| Model | Discipline | Implication |
|---|---|---|

### Investment Judgment Checklist
| Principle | Status | Notes |
|---|---|---|

### Psychological Bias Check
[Active tendencies, incentives, and lollapalooza risk.]

### Verdict
[Act / Watch / Research More / Too Hard] - [one sentence rationale]
```

### For bias diagnosis

```markdown
## Misjudgment Diagnosis

### Incentive Map
[Who is rewarded for what.]

### Active Tendencies
| Tendency | Evidence | Antidote |
|---|---|---|

### Lollapalooza Risk
[Whether tendencies reinforce one another.]

### Corrective Action
[Checklist, independent review, incentive redesign, or cooling-off step.]
```

### For general decisions

```markdown
## Munger-Style Decision Review

### Problem Definition
[The decision in plain language.]

### Models That Matter
[3-5 models and what each implies.]

### Inversion
[Failure modes and safeguards.]

### Competence Boundary
[What is known, unknown, and too hard.]

### Action Checklist
[Concrete next steps.]
```

## Critical Reminders

1. Do not provide false precision. Munger-style judgment values simple, robust conclusions over fragile calculations.
2. Always check incentives. Incentives can distort both the subject being analyzed and the analyst.
3. Use inversion before optimism.
4. Prefer the too-hard basket to a confident answer outside competence.
5. Treat checklists as protection against preventable stupidity, not as bureaucracy.
6. Look for combinations of models and biases; extreme outcomes usually have multiple causes.
7. Keep quotes in `quotes/`; use the skill body for paraphrased, executable instructions.
