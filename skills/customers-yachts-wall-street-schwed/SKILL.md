---
name: customers-yachts-wall-street-schwed
description: 'Analyze Wall Street conflicts. Trigger on: "can I trust this advisor?", "is this forecast reliable?", "whose interest does this serve?".'
license: 'Skill distillation for personal/educational use. Do not reproduce source passages verbatim.'
---

# Where Are the Customers' Yachts? Conflict Orchestrator

## Skill Purpose

Apply Fred Schwed Jr.'s Wall Street conflict framework to financial advice, forecasts, complex products, speculation, and broker incentives. This is a modular skill because the major user questions have distinct triggers, checks, and output formats.

## Routing Rules

| User intent | Route to |
|---|---|
| Advisor, broker, planner, fund salesperson, fiduciary conflict | `subskills/conflict-diagnostic.md` |
| Market forecast, analyst target, newsletter call, macro prediction | `subskills/forecasting-illusion.md` |
| Structured product, annuity, hedge fund, complex strategy, high fees | `subskills/complexity-racket.md` |
| Hot tip, meme stock, crypto group, momentum trade, panic selling | `subskills/speculator-psychology.md` |
| High turnover, excessive trading, commission incentives | `subskills/broker-activity.md` |

## Execution Rules

1. Ask who earns money if the user acts.
2. Separate investment from speculation before giving advice.
3. Prefer simple, low-cost alternatives unless complexity has a clear job.
4. Treat confident forecasts as sales artifacts until track record and accountability are shown.
5. Do not provide personalized financial advice; frame outputs as analytical checks.

## Multi-Module Output Format

- Conflict identification: who earns what.
- Schwed test applied: relevant module and checklist.
- Simple alternative: lower-conflict path.
- Verdict: aligned, partially aligned, or misaligned.

## Subskill Status

All subskills are required and present in `subskills/`.

## CITATION RULES

Use quotes only when the user asks for source grounding or when a claim needs attribution. Reference quote anchors by topic file and anchor. Keep quoted excerpts short.

- `conflicts-incentives-quotes.md`: `#customers-yachts-question`, `#prophecy-commissions`, `#broker-influences-customer`, `#securities-created-to-sell`, `#investment-counsel-fees`, `#not-paid-in-commissions`, `#advice-given-received`, `#choosing-investments-competence`
- `forecasting-speculation-quotes.md`: `#difficult-answer-dont-know`, `#prediction-loses-savings`, `#just-a-croupier`, `#charts-useful-accuracy`, `#probability-and-risk`, `#buy-boom-sell-depression`, `#panic-buy-stocks`, `#dying-rich`

## Critical Reminders

- The first question is always incentive alignment.
- Confidence is not accuracy.
- Complexity often prevents comparison.
- Do not reproduce long source passages.
