---
name: storybrand-messaging-framework
description: Use StoryBrand for "clarify my message", "rewrite my homepage", "create a BrandScript", "what is my one-liner", or "fix my CTA".
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

# StoryBrand Messaging Framework

## Overview

Use this skill to apply Donald Miller's StoryBrand SB7 framework to brand messaging, website copy, fundraising appeals, product positioning, sales pages, and marketing assets. The skill turns a confusing offer into a clear customer-centered story: the customer is the hero, the brand is the guide, the offer solves a real problem, and the next action is obvious.

This is a messaging-clarity skill. It does not validate whether a market exists, set paid-media budgets, or replace customer research.

## When to Use This Skill

Invoke this skill when the user asks:

- "Help me create a BrandScript for my business."
- "Clarify my message."
- "Rewrite my homepage using StoryBrand."
- "Does this pass the grunt test?"
- "What is my one-liner?"
- "Am I positioning myself as the hero or the guide?"
- "Write a better CTA, tagline, landing page, email, ad, or pitch."

## Core Principle

Clear messaging beats clever messaging. The user must leave with copy that quickly answers: what is being offered, how it improves the customer's life, and what the customer should do next.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Steps | Output |
|---|---|---|---|---|
| BrandScript creation | "Apply StoryBrand to my business" | Offer, customer, problem, proof, desired action | Fill all seven SB7 elements | Complete BrandScript |
| Website grunt test | "Review my homepage" | Existing copy or URL text | Test clarity, hierarchy, CTA, stakes, success | Rewrite and priority fixes |
| One-liner creation | "What is my pitch?" | Customer, problem, solution, result | Problem + solution + result | One-liner variants |
| CTA and funnel design | "What should the CTA be?" | Buying stage, friction, trust level | Direct and transitional CTA mapping | CTA set and placement |
| Asset rewrite | "Rewrite this email/ad/page" | Draft copy, audience, goal | Reframe customer as hero and brand as guide | Revised copy |

## The SB7 Framework

### 1. A Character

**Rule:** The customer is the hero, not the brand.

**Key questions:**

- What does the customer want?
- Can the desire be stated in one clear sentence?
- Is the copy centered on the customer's ambition rather than the company's story?

**Decision criteria:**

- One primary desire is visible above all secondary messages.
- The customer's current state and desired future state create a story gap.
- Company history and internal language are removed unless they prove guide authority.

**Agent instruction:** Name the customer's concrete want before writing any brand copy. If the user provides many audiences or goals, ask them to pick the primary buyer for this pass.

### 2. Has a Problem

**Rule:** Customers buy relief from internal frustration, not only solutions to external problems.

**Key questions:**

- What is the external practical problem?
- What internal frustration, fear, delay, embarrassment, or uncertainty does it create?
- What philosophical "this should not be this hard" statement makes the stakes feel meaningful?
- What force can be named as the villain without attacking a person?

**Decision criteria:**

- The copy includes external, internal, and philosophical problem language.
- The villain is a problem source such as complexity, waste, risk, or confusion.
- The emotional problem is specific enough to make the buyer feel understood.

**Agent instruction:** Diagnose all three problem levels and choose the one most likely to move the customer. Do not stop at feature-level pain points.

### 3. Meets a Guide

**Rule:** The brand must be the guide, not a competing hero.

**Key questions:**

- How can the brand show empathy for the customer's struggle?
- What proof establishes authority without bragging?
- Are testimonials, numbers, logos, credentials, or case results available?

**Decision criteria:**

- Empathy appears before or beside authority.
- Proof is used to reduce buyer risk, not to make the brand the protagonist.
- The copy avoids "we are amazing" language unless tied to the customer's outcome.

**Agent instruction:** Write one empathy line and one authority line. If proof is missing, mark it as a gap and suggest what evidence to collect.

### 4. Gives Them a Plan

**Rule:** A confused buyer does not move. A guide gives a simple path.

**Key questions:**

- What are the 3-4 steps from interest to success?
- What fears or objections need an agreement plan?
- Which step is the customer's next visible action?

**Decision criteria:**

- The plan has no more than four steps unless the user explicitly needs a complex process.
- Each step uses plain verbs.
- The plan reduces perceived risk.

**Agent instruction:** Produce a process plan for action and, when trust is low, an agreement plan that names guarantees, standards, or commitments.

### 5. Calls Them to Action

**Rule:** Customers do not act unless challenged to act.

**Key questions:**

- What is the direct CTA for ready buyers?
- What is the transitional CTA for not-yet-ready buyers?
- Does the CTA use a clear action verb instead of vague browsing language?

**Decision criteria:**

- Direct CTA is concrete: buy, schedule, start, donate, subscribe, get quote.
- Transitional CTA offers useful value while moving the relationship forward.
- CTA text appears repeatedly where action is natural.

**Agent instruction:** Always output both direct and transitional CTAs unless the channel only permits one.

### 6. Helps Them Avoid Failure

**Rule:** Stakes make action meaningful, but fearmongering breaks trust.

**Key questions:**

- What cost of inaction is honest and specific?
- What frustration, loss, delay, risk, or missed opportunity continues without action?
- Is the warning balanced with a positive success vision?

**Decision criteria:**

- Stakes are clear but not manipulative.
- The cost of inaction is connected to the customer's stated problem.
- The copy avoids exaggerated catastrophe.

**Agent instruction:** Add one concise stakes statement, then quickly move to the success outcome.

### 7. Ends in Success

**Rule:** The brand must paint the customer's successful future.

**Key questions:**

- What specific result will the customer experience?
- How will the customer feel, be seen, or operate differently?
- What identity does the customer want to step into?

**Decision criteria:**

- Success language is concrete, visual, and outcome-oriented.
- The outcome is about the customer, not the product.
- The transformation is believable from the offer.

**Agent instruction:** End major copy outputs with a before/after transformation and an aspirational identity statement.

## Query Response Framework

### Full BrandScript

1. Identify product, customer, desired outcome, and buying action.
2. Fill the seven SB7 elements in order.
3. Flag missing proof, vague customer definition, weak stakes, or unclear CTA.
4. Extract reusable messaging assets.

### Website Review

1. Apply the grunt test: what is offered, how it improves life, what to do next.
2. Audit hero headline, subheadline, CTA, problem section, guide proof, plan, stakes, success.
3. Rewrite the highest-impact sections first.
4. Give prioritized fixes, not a generic critique.

### One-Liner

Use this structure:

```text
We help [customer] who struggle with [problem] get [solution] so they can [success].
```

### Asset Rewrite

1. Remove company-centered language.
2. Put the customer's problem and desired success first.
3. Add empathy, proof, plan, CTA, stakes, and success as appropriate for the channel.
4. Deliver polished copy plus a short rationale.

## Output Format

For a complete messaging request, respond with:

```markdown
## StoryBrand Diagnosis
- Customer:
- Primary desire:
- Main problem:
- Current clarity issue:

## BrandScript
1. Character:
2. Problem:
   - External:
   - Internal:
   - Philosophical:
   - Villain:
3. Guide:
   - Empathy:
   - Authority:
4. Plan:
5. Calls to action:
   - Direct:
   - Transitional:
6. Failure avoided:
7. Success:

## Copy Assets
- One-liner:
- Tagline options:
- Website hero:
- CTA set:

## Priority Fixes
1. ...
2. ...
3. ...
```

## CITATION RULES

When making substantive StoryBrand-method claims, cite the quote files if the user asks for sources or if the answer is a formal audit.

**Quote files:**

- `quotes/main-framework-quotes.md` — SB7 rules, clarity, guide positioning, plan, CTA, stakes, transformation.
- `quotes/storybrand-principles-quotes.md` — broader StoryBrand principles and implementation reminders.

**Anchor mapping:**

- `main-framework-quotes.md`: `#words-sell-things`, `#brain-drawn-to-clarity`, `#story-greatest-weapon`, `#customer-is-hero`, `#customer-looks-for-guide`, `#companies-sell-external`, `#trust-guide-with-plan`, `#call-to-action-required`, `#avoid-tragic-ending`, `#buying-transformation`, `#if-you-confuse-you-lose`, `#grunt-test`
- `storybrand-principles-quotes.md`: `#story-organizes-information`, `#brain-survive-and-thrive`, `#story-makes-music`, `#hero-in-a-hole`, `#three-levels-problems`, `#guide-positioning`, `#story-gap-power`, `#conflict-gets-attention`, `#villain-focus`, `#plan-removes-confusion`, `#two-types-cta`, `#whats-at-stake`, `#aspirational-identity`, `#one-liner-formula`, `#website-hierarchy`

**Citation format:**

```markdown
> "Author's exact words here."
>
> - [*Building a StoryBrand*, cited excerpt](https://github.com/simbajigege/book2skills/blob/main/skills/storybrand-messaging-framework/quotes/main-framework-quotes.md#customer-is-hero)
```

Use only exact quote text from the quote files. If no exact quote fits, cite the closest anchor and state that the analysis is a paraphrased application.

## Critical Reminders

- Customer first, company second.
- Clarity beats cleverness.
- Internal problems often matter more than external ones.
- Every serious page needs a direct CTA.
- Use stakes honestly and briefly.
- End with a concrete vision of success.
