---
name: business-adventures-analysis-brooks
description: "Apply John Brooks' Business Adventures framework to analyze corporate failures, market crises, and business decisions. Trigger: \"why did this fail?\", \"what patterns apply?\", \"analyze this case\""
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

## Overview

This skill encodes the analytical frameworks from *Business Adventures: Twelve Classic Tales from the World of Wall Street* by John Brooks (originally New Yorker articles, 1969). The book examines 12 real business episodes — market crashes, product failures, price-fixing scandals, currency crises, and innovation stories — to reveal the timeless patterns governing corporate behavior, market psychology, and institutional failure.

Use this skill to analyze current business situations against historical precedents, diagnose why companies or products fail, evaluate corporate decision-making quality, and assess regulatory and governance risk.

**Intended users:** Business analysts, investors, executives, students of business history, journalists covering corporate affairs.

---

## When to Use This Skill

Trigger on any of these query patterns:
- "Why did [company/product] fail?"
- "What does this situation remind you of historically?"
- "Analyze this business case / corporate crisis"
- "What patterns apply to [market event / corporate scandal]?"
- "What would John Brooks say about [current event]?"
- "Lessons from [Edsel / Xerox / GE price-fixing / Texas Gulf / 1962 crash]"
- "Is this [executive behavior / business practice] a warning sign?"
- "How do market panics typically unfold?"

---

## Core Principle

**Human nature is the constant; institutions are the variable.**

Brooks's deepest observation: the same psychological patterns — panic, hubris, self-deception, communication failure, regulatory inertia — repeat across companies, markets, and decades. The specific technology, industry, or era changes; the underlying human dynamics do not. Analysis begins by recognizing which pattern is operating, then applying the historical template.

---

## DIMENSION 1: Market Psychology & Panic Patterns

**The Rule:** Market crises follow a predictable psychological arc — panic, uncertainty about the bottom, bargain-hunter entry, recovery — but the depth and timing of each phase remain unpredictable. Technical failures amplify the psychological ones.

### Key questions to ask:
- What phase of the panic arc is this? (early selling, cascade, maximum fear, early recovery, stabilization?)
- What technical amplifiers are present? (liquidity shortfalls, forced sellers, media amplification, margin calls?)
- Are there structural feedback loops that could deepen the decline? (fund redemptions, counterparty cascades?)
- How does this compare to the historical arc of 1962, 1929, or the sterling crisis of 1964?
- Is the selling driven by fundamentals or by fear of fear?

### Decision criteria / Checklist:
- [ ] Identify the trigger event — is it a genuine fundamental change or a sentiment shock?
- [ ] Measure technical stress: tape/settlement delays, order execution failures, bid-offer spreads widening
- [ ] Check feedback loops: are forced sellers (margin calls, fund redemptions) amplifying the decline?
- [ ] Assess media role: is broadcast coverage amplifying retail panic?
- [ ] Identify the stabilizing force: who are the potential bargain hunters and what price level triggers them?
- [ ] Look for specialist/market-maker behavior — are they absorbing selling or withdrawing?

### Warning signals:
- Settlement systems showing signs of strain (delayed confirmations, failed trades)
- Media interrupting regular programming to cover market moves
- "Nobody knows where the bottom is" becoming the dominant narrative
- Forced sellers with no discretion (margin calls, redemption gates) appearing in size

### Agent instruction:
When the user describes a market panic, crash, or sharp decline, apply this dimension by: (1) mapping the situation to the panic arc phases, (2) identifying technical amplifiers present, (3) comparing to the 1962 mini-crash template, and (4) assessing whether stabilizing mechanisms (specialists, bargain hunters, central banks) are likely to emerge and at what threshold.

---

## DIMENSION 2: Product Strategy & Market Timing

**The Rule:** No amount of preparation, research, or capital investment can substitute for genuine market fit and correct timing. The Edsel failed with $250M and years of research because it launched into a market that had changed.

### Key questions to ask:
- Has the market shifted since the product was designed? (recession, consumer preference change, competitive disruption?)
- Is the product's positioning based on what research said consumers want, or on what they actually buy?
- Is the launch date driven by internal commitments (dealer contracts, tooling) or by market readiness?
- Can the product's value proposition be stated in one sentence that resonates with the target buyer?
- Are key stakeholders (dealers, distributors) committed based on product merit or hype?

### Decision criteria / Checklist:
- [ ] Validate that market research measures actual purchase intent, not stated preferences
- [ ] Confirm the launch timing reflects current market conditions, not the conditions when planning began
- [ ] Test whether the product name/positioning survives free association (what does it remind people of?)
- [ ] Check that dealer/distributor commitment is based on product demonstration, not promotional pitch
- [ ] Verify the product has a single clear differentiator — not a committee-designed compromise

### Warning signals:
- Market research produces extensive data but cannot answer the core question ("Which one should we name it?")
- Launch date is locked in by supplier contracts before product-market fit is confirmed
- Target segment defined by aspiration ("people who want to feel successful") not by behavior
- Competitors are successfully moving in the opposite direction (e.g., toward smaller/cheaper)

### Agent instruction:
When the user asks about a product launch failure or strategy question, apply this dimension by: (1) identifying whether the product's design was locked before market validation, (2) checking whether timing misaligns with market conditions, (3) testing whether the positioning is research-derived vs. behavior-derived, and (4) mapping to the Edsel template — extensive preparation ≠ product success.

---

## DIMENSION 3: Corporate Communication Failure

**The Rule:** Large organizations develop structural gaps between stated policy and actual behavior. Top management issues clear directives; middle management acknowledges them and acts contrary to them. The gap is maintained through plausible deniability.

### Key questions to ask:
- Does the stated corporate policy (ethics, compliance, strategy) match the incentive structures actually in place?
- Are there multiple layers of management between the policy-setter and the policy-executor?
- Is there a documented history of the same problem recurring despite previous policy reinforcement?
- Do executives use language that acknowledges questions without actually answering them?
- Are compliance and performance reviewed by the same manager, or by separate systems?

### Decision criteria / Checklist:
- [ ] Map the distance (in organizational layers) between the policy directive and the executing employees
- [ ] Check whether stated policy and compensation/promotion incentives point in the same direction
- [ ] Review whether "ethics training" is separated from operational performance reviews
- [ ] Look for passive-voice accountability ("mistakes were made," "I was responsive to that")
- [ ] Ask whether middle managers can claim plausible ignorance of what their subordinates are doing

### Warning signals (GE price-fixing template):
- Ethics compliance is managed by a separate organizational unit from business operations
- Senior executives regularly claim they "didn't know" about systematic patterns in their divisions
- Formal compliance certifications are signed annually but never verified against actual behavior
- The language of acknowledgment substitutes for the language of action ("I was responsive to that")
- Whistleblowers who raised issues were dismissed or ignored without documented follow-up

### Agent instruction:
When the user describes a corporate scandal, compliance failure, or strategy that isn't being executed, apply this dimension by: (1) identifying the organizational distance between directive and execution, (2) mapping whether incentives contradict stated policy, (3) applying the GE three-layer failure model (explicit instruction / implicit pressure / plausible deniability), and (4) assessing whether the failure is structural (will recur) or situational (addressable by better enforcement).

---

## DIMENSION 4: Regulatory & Legal Risk

**The Rule:** Regulatory enforcement follows crises with a long lag. Practices that were tolerated for decades become illegal overnight when a sufficiently visible case forces the issue. The risk is not just current rules but the rules that will be created after the next crisis.

### Key questions to ask:
- Has this practice been common and widely tolerated, creating a false sense of legality?
- Is there a recent high-profile case or investigation that could serve as the regulatory trigger?
- What is the "materiality" of the information or action — would a reasonable investor consider it significant?
- For insider trading: was the information public, when was it disclosed, and was adequate time allowed before trading?
- For antitrust: is there documented coordination, even informal, with competitors on price or market allocation?
- For trade secrets: can the employer specifically identify what is proprietary vs. what is general professional knowledge?

### Decision criteria / Checklist:
- [ ] Texas Gulf Sulphur materiality test: Would a reasonable investor consider this information important in deciding to buy or sell?
- [ ] Adequate disclosure test: Was the information genuinely accessible to the public, or merely technically released?
- [ ] Timing test: Did insiders wait a "reasonable amount of time" after public disclosure before trading?
- [ ] Antitrust checklist: Any coordination (even informal, even verbal) on prices, bids, or market allocation creates liability
- [ ] Trade secret test: Can the employer specifically describe the secret, separate from the employee's general skill?

### Warning signals:
- Long-established industry practice that has never been legally challenged
- Regulatory agency that has been inactive in enforcement for an extended period
- Company press release that minimizes or contradicts its own internal findings
- Executives buying company stock in the period between internal discovery and public announcement
- Price coordination described as "gentlemen's agreements" or "industry norms"

### Agent instruction:
When the user asks about a regulatory, legal, or compliance question, apply this dimension by: (1) applying the Texas Gulf Sulphur materiality standard to identify what constitutes material non-public information, (2) assessing whether regulatory enforcement is in an "active" or "dormant" phase (crises trigger activation), (3) checking whether the practice is one that has been tolerated and is therefore at heightened risk, and (4) distinguishing between current legal risk and future regulatory risk from rule changes.

---

## DIMENSION 5: Innovation & Disruption Dynamics

**The Rule:** Genuinely disruptive innovations are invisible to conventional market research because they create demand that didn't previously exist. Incumbents consistently underestimate disruption by measuring it against existing market metrics.

### Key questions to ask:
- Did the market for this product/service exist before the innovation, or did the innovation create the market?
- How many established companies passed on this technology before it found a champion? (Xerox was rejected by IBM, GE, RCA, Remington Rand)
- Does the incumbent's defense rely on the argument that the market is small or non-existent? (It is, until it isn't)
- Is the new technology protected by patents that create a meaningful moat?
- Is the adoption curve driven by demonstrated value or by price relative to incumbents?

### Decision criteria / Checklist:
- [ ] Identify whether the innovation requires users to change behavior (harder adoption) or enables existing behavior more cheaply (easier adoption)
- [ ] Check whether market size estimates are based on current behavior extrapolation or on new-use-case modeling
- [ ] Assess the strength of patent protection and lead time before incumbents can respond
- [ ] Look for early adopters who are using the product in ways the inventor didn't anticipate (signal of platform potential)
- [ ] Evaluate whether incumbents have structural reasons to underinvest in the new technology (protects existing revenue)

### Warning signals (incumbents):
- Market research consistently shows "insufficient demand" for a new technology
- Internal projections assume the new technology cannibalizes existing products 1:1
- Established company licenses or acquires the innovation but doesn't invest in scaling it
- The new technology's most enthusiastic early adopters are outside the incumbent's core customer base

### Agent instruction:
When the user asks about a new technology, disruption, or innovation investment decision, apply this dimension by: (1) testing whether the market can be measured with existing metrics or requires new-use-case modeling, (2) applying the Xerox template — how many rejections before a champion, and why did the champion succeed?, (3) assessing patent protection and lead time, and (4) identifying whether incumbents are structurally incentivized to ignore the threat.

---

## DIMENSION 6: Corporate Governance & Accountability

**The Rule:** Annual meetings, ethics codes, and compliance programs function as governance theater when not backed by genuine accountability mechanisms. The gap between formal governance and actual power is most visible during crises.

### Key questions to ask:
- Do shareholder meetings allow genuine challenge, or are dissenting voices managed into ineffectiveness?
- Is the board's response to a crisis "we are deeply grieved" (passive) or "we are changing X, Y, Z" (active)?
- Can executives transition from government to business (or vice versa) while maintaining genuine independence?
- Are professional activist shareholders (like the Gilbert brothers) raising substantive governance issues or performing?
- Does the compensation structure create accountability for the decisions executives make?

### Decision criteria / Checklist:
- [ ] Test whether shareholder questions receive substantive answers or procedural deflection
- [ ] Check whether governance changes after a crisis address root causes or symptoms
- [ ] Assess conflict-of-interest risk in government-to-private transitions (access, regulatory relationships)
- [ ] Evaluate whether board composition reflects diverse, independent perspectives or captured insiders
- [ ] Determine whether accountability (consequences for failure) is personal or corporate (company pays, executives don't)

### Warning signals:
- Post-scandal response focuses on individual bad actors rather than structural causes
- CEO publicly states "I am deeply grieved" but takes no personal accountability
- Activist shareholders are praised for participation but their proposals are consistently voted down
- Government-to-business revolving door involves regulatory oversight of the new employer
- Annual meeting is held in a format that systematically limits time for shareholder questions

### Agent instruction:
When the user asks about corporate governance, accountability, or shareholder rights, apply this dimension by: (1) distinguishing between governance theater and genuine accountability mechanisms, (2) applying the GE model to assess whether stated values are backed by structural incentives, (3) evaluating whether crisis responses address root causes, and (4) assessing the Piggly Wiggly lesson — rules can change during a crisis, and the party with rule-making power wins.

---

## Query Response Framework

### Query Type 1: "Why did [company/product/strategy] fail?"

**Step 1:** Identify which dimensions are most relevant (usually 2–3 of the 6).
**Step 2:** Apply DIMENSION 2 (Product Strategy) — Was the failure driven by timing, research-action gap, or positioning?
**Step 3:** Apply DIMENSION 3 (Communication Failure) — Was execution misaligned with strategy due to organizational gaps?
**Step 4:** Apply DIMENSION 6 (Governance) — Did accountability gaps allow failure to persist?
**Step 5:** Name the historical case from Business Adventures that most closely maps to the failure.
**Output:** Lead with the primary failure cause, then supporting factors. End with "the closest historical parallel is [case]."

### Query Type 2: "What patterns apply to this market crisis / crash?"

**Step 1:** Apply DIMENSION 1 (Market Psychology) — Map the current situation to the panic arc phases.
**Step 2:** Identify technical amplifiers present.
**Step 3:** Identify stabilizing forces and likely recovery triggers.
**Step 4:** Compare to the 1962 crash template and the 1964 sterling crisis.
**Output:** Phase assessment → amplifiers → stabilizers → historical comparison → outlook.

### Query Type 3: "Is this [practice/behavior] a legal/regulatory risk?"

**Step 1:** Apply DIMENSION 4 (Regulatory Risk) — Apply the Texas Gulf Sulphur materiality test.
**Step 2:** Assess whether enforcement is in an active or dormant phase.
**Step 3:** Identify whether the practice has a long tolerance history (heightened risk of abrupt enforcement change).
**Output:** Current legal risk assessment → future regulatory risk → specific warning signals present.

### Query Type 4: "How does [new technology/company] compare historically?"

**Step 1:** Apply DIMENSION 5 (Innovation) — Was this market measurable before the innovation?
**Step 2:** Identify how many established players passed on it and why.
**Step 3:** Assess patent moat and adoption dynamics.
**Step 4:** Map to the Xerox template or the Piggly Wiggly self-service model.
**Output:** Innovation classification (creates market vs. improves existing) → adoption drivers → incumbent response → historical parallel.

### Query Type 5: "What should [executive/company] do in this situation?"

**Step 1:** Identify which dimension is most active in the situation.
**Step 2:** Apply the relevant dimension's checklist and warning signals.
**Step 3:** Pull the most applicable historical case as a cautionary or positive template.
**Step 4:** State the action recommendation, citing the historical precedent.
**Output:** Situation diagnosis → relevant historical case → recommended action → risk if action not taken.

---

## Output Format

Structure all responses as follows:

**Situation Diagnosis** (2–3 sentences: which pattern is operating, which dimension(s) are active)

**Historical Parallel** (name the most applicable case from the 12 chapters, 1–2 sentences on the match)

**Key Analysis** (apply the relevant dimension's checklist and criteria — use bullet points or a short table)

**Warning Signals Present / Absent** (explicit list)

**Recommendation or Outlook** (1–3 sentences: what to do or what to expect, grounded in the historical template)

> For market crisis queries: add a **Phase Assessment** header after Situation Diagnosis.
> For legal/regulatory queries: add a **Risk Level** (Low / Medium / High / Uncertain) header before Recommendation.

---

## Critical Reminders

1. **Human psychology is the constant.** Every analysis begins by identifying which human pattern is operating — panic, hubris, self-deception, communication breakdown — before analyzing structural factors.

2. **Preparation ≠ success.** The Edsel had $250M, years of research, and extensive dealer preparation. None of it mattered when market timing and genuine differentiation were absent.

3. **Regulatory enforcement lags crises.** Insider trading was common and unprosecuted for decades before Texas Gulf Sulphur. Antitrust was violated for years at GE before prosecution. Assess not just current rules but the rules the next crisis will create.

4. **Communication failure is structural, not individual.** When a large organization fails to execute its stated values, the cause is almost always incentive misalignment across organizational layers — not individual bad actors. Solutions that punish individuals without fixing structure will fail again.

5. **Rules change during crises.** The Piggly Wiggly corner failed because the NYSE changed the delivery deadline rules mid-game. The party with rule-making authority can alter the outcome. Assess who has that authority before taking a position that depends on rules remaining stable.

6. **The most dangerous practices are the widely tolerated ones.** Practices that have been common for years without prosecution carry a latent regulatory risk that spikes abruptly when a high-profile case forces the issue.

7. **Market research cannot size demand for the genuinely new.** Xerox was rejected by every major corporation using conventional market analysis. When the market didn't previously exist, conventional research is structurally incapable of assessing it.

8. **Annual meetings and ethics codes are theater unless backed by consequences.** Governance is real when it changes executive behavior; it is theater when it records dissent without acting on it. Evaluate governance by outcomes, not by process.
