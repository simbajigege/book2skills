---
name: jab-jab-right-hook-vaynerchuk
description: Apply Gary Vaynerchuk social content rules for native jabs, right hooks,
  platform fit, campaign critique, and engagement before conversion.
license: Skill distillation for personal/educational use. Do not reproduce source
  passages verbatim.
---


# Jab, Jab, Jab, Right Hook — Social Marketing Skill

**Knowledge source:** *Jab, Jab, Jab, Right Hook* by Gary Vaynerchuk.

## Overview

Use this skill to critique, design, or revise brand social media content so it earns attention natively before asking for conversion. It supports marketers, founders, creators, and agencies evaluating whether a post, campaign, or content calendar has enough value-giving "jabs" before the sales "right hook."

## When to Use This Skill

Use this skill when the user asks:
- "Is this social post any good?"
- "How do I adapt this campaign for Instagram, X, Facebook, Pinterest, Tumblr, or mobile?"
- "Are we asking for the sale too soon?"
- "Rewrite this post so it feels native to the platform."
- "Audit our content calendar for jabs and right hooks."

## Core Principle

Great social marketing earns the right to ask. Give native, context-aware, useful or entertaining micro-content repeatedly, then make a clear conversion ask only when the audience has been served and the platform context supports it.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Steps | Output | Independent trigger? | Distinct references? | Triage score | Should be subskill? | Reason |
|---|---|---|---|---|---|---:|---:|---|---|
| Native post critique | "Review this post" | Post text, asset, platform, goal | Check platform fit, interruption level, visual/text craft, ask | Scored critique and rewrite | Yes | Yes | 3 | No | Core workflow; dimensions must be applied together. |
| Jab/right-hook balance | "Are we selling too much?" | Calendar, funnel goal, audience state | Count value asks vs conversion asks; inspect sequencing | Jab/right-hook balance diagnosis | Yes | Yes | 3 | No | Same output format and same criteria as content critique. |
| Platform adaptation | "Make this work on Instagram/X/etc." | Base message, platforms, asset limits | Translate into platform-native language | Platform-specific variants | Yes | Yes | 3 | No | Independent but tightly coupled to native-content rules. |
| Campaign plan | "Plan a campaign" | Audience, product, channels, conversion goal | Sequence jabs, listening, timing, right hook | Campaign outline | Yes | No | 2 | No | Uses the same checks, just at calendar scale. |

## Architecture Justification

Although several question types can be triggered independently, they all use the same decision artifact: a native-content diagnosis followed by platform-fit fixes and a conversion-readiness verdict. Keeping this single-file prevents narrow platform rewrites from losing the jab/right-hook balance rule.

## DIMENSION 1: Native Platform Fit

**The Rule:** Content must speak the platform's native language instead of recycling the same ad everywhere.

### Key questions to ask:
- Which platform is this for, and what does good content look like there?
- Does the format match user behavior on that platform?
- Is the creative built for mobile scanning and fast context?
- Would this feel like part of the feed or like an interruption?

### Decision criteria / Checklist:
- Uses platform-native format, pacing, and visual grammar.
- Respects mobile constraints and attention fragmentation.
- Adjusts copy length, image treatment, hashtags, links, and call-to-action by platform.
- Does not simply cross-post the same asset unchanged.

### Warning signals:
- One identical post deployed everywhere.
- Brand-first copy that ignores the user's feed context.
- Creative that requires too much explanation before it creates value.

### Agent instruction:
When the user provides a post or campaign, first identify the target platform and judge whether the asset feels native before commenting on persuasion or conversion.

## DIMENSION 2: Jab Value Before the Ask

**The Rule:** A jab gives value, context, entertainment, or relationship before the right hook asks for conversion.

### Key questions to ask:
- What does this post give the audience before it asks?
- Is the brand listening or only broadcasting?
- Has the campaign built enough goodwill before the sales moment?
- Is the right hook clear, timely, and earned?

### Decision criteria / Checklist:
- Jabs are useful, entertaining, empathetic, or culturally timely.
- Engagement and relationship precede demand generation.
- Right hooks have a direct ask, obvious next step, and specific conversion goal.
- Calendar sequencing shows patience rather than constant selling.

### Warning signals:
- Every post asks users to buy, click, register, or share.
- Jabs are disguised ads with no independent value.
- The conversion ask appears before trust, relevance, or timing is established.

### Agent instruction:
For any campaign, separate jabs from right hooks and report whether the ratio and sequence earn the conversion ask.

## DIMENSION 3: Micro-Content Craft

**The Rule:** Social content wins through small, sharp, context-aware details.

### Key questions to ask:
- Is the hook understandable without extra context?
- Does the image, caption, or format create immediate recognition?
- Is the message too broad for the platform moment?
- Does the creative leverage current culture without forcing it?

### Decision criteria / Checklist:
- One clear idea per post.
- Strong opening image, phrase, or cultural cue.
- Copy is concise enough for the platform.
- Brand voice is consistent but self-aware.

### Warning signals:
- Generic brand slogan with no social context.
- Long explanation before the payoff.
- Trend-jacking without relevance to audience or brand identity.

### Agent instruction:
Rewrite weak content into smaller, platform-native micro-content while preserving the brand goal.

## DIMENSION 4: Listening and Iteration

**The Rule:** Social media is a feedback system, not a publishing calendar alone.

### Key questions to ask:
- What audience signal will decide whether this is working?
- Is the brand responding to comments, culture, and platform behavior?
- What data should change the next jab or right hook?

### Decision criteria / Checklist:
- Defines engagement, conversion, and learning metrics separately.
- Builds in listening before the next ask.
- Uses data to improve the next piece of content.

### Warning signals:
- Success measured only by impressions.
- No plan for comments, replies, or cultural timing.
- Treating social platforms as cheap ad inventory.

### Agent instruction:
When the user asks for a plan, include feedback loops and decision rules for when to continue, revise, or launch the right hook.

## Query Response Framework

### Query Type 1: Review a social post
1. Identify platform, audience, and desired action.
2. Score Native Fit, Jab Value, Micro-Content Craft, and Right-Hook Readiness.
3. Name the biggest failure mode.
4. Provide a rewritten native version.

### Query Type 2: Build a campaign sequence
1. Clarify conversion goal and audience state.
2. Design a sequence of jabs by platform.
3. Add listening checkpoints.
4. Place the right hook only after value and context have accumulated.

### Query Type 3: Adapt one idea across platforms
1. Preserve the strategic message.
2. Translate format, voice, CTA, and visual treatment by platform.
3. Explain what changed and why.

## Output Format

```markdown
## Social Content Diagnosis
**Platform:** ...
**Goal:** ...
**Verdict:** Native / Needs adaptation / Too interruptive / Asking too soon

| Dimension | Rating | Evidence | Fix |
|---|---|---|---|

## Recommended Rewrite or Sequence
...

## Right-Hook Readiness
- Earned ask:
- Missing jabs:
- Next test:

## Citations
...
```

## Critical Reminders

1. Do not judge a post apart from its platform context.
2. Do not make every touchpoint a sales ask.
3. Do not confuse brand consistency with identical cross-posting.
4. Do not ignore mobile behavior and fragmented attention.
5. Treat engagement as earned through value, not demanded.

## CITATION RULES

Every substantive claim based on Vaynerchuk's method must include a citation to the original text.

**Quote files:**
- `jab-right-hook-framework-quotes.md` — jab/right-hook definitions, native content, brand consistency, platform uniqueness, and effort required.
- `social-media-platforms-quotes.md` — platform-specific storytelling, micro-content, mobile, context, engagement, and real-time marketing.

**Citation format:**

> "Author's exact words here."
>
> — [*Jab, Jab, Jab, Right Hook*, cited excerpt](https://github.com/simbajigege/book2skills/blob/main/skills/jab-jab-right-hook-vaynerchuk/quotes/FILENAME.md#ANCHOR)

**Anchor mapping:**
- `jab-right-hook-framework-quotes.md`: `#jab-jab-jab-right-hook-metaphor`, `#jab-definition`, `#right-hook-definition`, `#native-content-essential`, `#number-one-job`, `#social-media-best-chance`, `#native-content-definition`, `#story-non-intrusive`, `#brand-identity-consistency`, `#sweet-science-marketing`, `#platform-uniqueness`, `#perfect-right-hook-three-characteristics`, `#platform-native-language`, `#all-companies-media-companies`, `#effort-required`
- `social-media-platforms-quotes.md`: `#facebook-storytelling`, `#twitter-listening`, `#pinterest-glam`, `#instagram-art`, `#tumblr-animation`, `#context-is-key`, `#micro-content-matters`, `#mobile-first`, `#respect-platform-nuances`, `#different-platforms-different-formulas`, `#real-time-marketing`, `#engagement-before-conversion`, `#patience-required`, `#data-driven-decisions`, `#consumer-attention-fragmented`

**Rules:**
- Include at least one citation per major section of the response.
- Match the anchor to the closest relevant principle.
- If no exact quote matches, cite the closest anchor and label the analysis as a paraphrased application.
