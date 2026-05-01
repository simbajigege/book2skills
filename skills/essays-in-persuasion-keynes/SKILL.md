---
name: essays-in-persuasion-keynes
description: 'Apply Keynes policy reasoning. Trigger on: "will austerity work?", "inflation or deflation?", "analyze this economic crisis".'
license: 'Skill distillation for personal/educational use. Do not reproduce source passages verbatim.'
---

# Essays in Persuasion: Keynes Policy Reasoning Orchestrator

## Skill Purpose

Apply John Maynard Keynes's policy reasoning from *Essays in Persuasion* to contemporary macroeconomic questions. This is a modular skill because users may ask separate, independently triggered questions about debt capacity, inflation versus deflation, fixed exchange-rate traps, demand shortfalls, or economic persuasion.

## Routing Rules

| User intent | Route to |
|---|---|
| Sovereign debt, reparations, sanctions, fiscal capacity, creditor demands | `subskills/transfer-problem.md` |
| Inflation, deflation, unemployment tradeoffs, real debt burdens | `subskills/inflation-deflation.md` |
| Gold standard, currency pegs, euro constraints, devaluation | `subskills/fixed-rate-trap.md` |
| Recession, austerity, stimulus, liquidity trap, animal spirits | `subskills/aggregate-demand.md` |
| Critique or write an economic argument meant to persuade | `subskills/economic-persuasion.md` |

## Execution Rules

1. Identify the user's concrete policy question and economic context.
2. Route to the smallest relevant subskill; combine subskills only when the question spans mechanisms.
3. Use current data when the user asks about a present economy or market.
4. Distinguish short-run consequences from long-run equilibrium claims.
5. State what evidence would change the verdict.

## Multi-Module Output Format

- Diagnosis line: identify the policy problem.
- Routed module(s): name the Keynesian lens used.
- Evidence: 2-3 data points or historical parallels.
- Verdict: recommendation with caveats.
- Revision condition: what would make the answer change.

## Subskill Status

All subskills are required and present in `subskills/`.

## CITATION RULES

Use quotes only when the user asks for source grounding or when a claim needs attribution. Reference quote anchors by topic file and anchor. Keep quoted excerpts short.

- `demand-confidence-quotes.md`: `#slump-trade-employment`, `#idle-workers-worldwide`, `#public-works-remedy`, `#doing-spending-enterprises`, `#restore-confidence-enterprise`, `#revive-enterprise-activity`, `#deflation-transfers-wealth`, `#active-to-inactive`
- `policy-diagnosis-quotes.md`: `#germany-pays-in-goods`, `#transfer-destroys-balance`, `#inflation-and-deflation-injure`, `#inflation-unjust-deflation-inexpedient`, `#deflation-provokes-unemployment`, `#reject-prewar-gold-standard`, `#gold-standard-links-city-wall-street`, `#economists-as-dentists`

## Critical Reminders

- Judge policy by real output, employment, price, and distributional consequences.
- Do not turn Keynes into a universal pro-stimulus slogan; context determines the prescription.
- Do not reproduce long source passages.
