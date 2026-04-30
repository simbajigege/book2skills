---
name: contract-drafting-and-review-guidance-china-law
description: Apply China contract drafting review with San Guan Si Bu Fa. Trigger on contract review, drafting, clauses, or deal structure.
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

## Overview

This skill applies the Chinese contract drafting and review method known as "三观四步法" from *合同起草审查指南* (T/CAB 0121-2021). It helps lawyers, in-house counsel, business operators, and legal students structure contract review, draft contract frameworks, identify risks, and produce review comments under a China-law lens.

This skill is a workflow and checklist tool. It does not replace current legal research or advice from a licensed lawyer.

## When to Use This Skill

- The user asks to review a contract, draft a contract, or identify contract risks.
- The user asks how to structure a transaction before drafting documents.
- The user asks whether a contract form, clause order, or clause wording is appropriate.
- The user asks for a checklist for contract parties, subject matter, procedures, performance, breach, dispute resolution, or signing requirements.
- The contract is governed by PRC law or the user asks for China-law contract drafting logic.

## HOW TO USE THIS SKILL

1. Identify the user's task: contract review, contract drafting, deal-structure design, clause rewrite, or checklist generation.
2. Ask only for missing facts that are necessary: contract type, user role, transaction purpose, counterparty identity, subject matter, price/payment, timeline, and special risk tolerance.
3. Apply the four-step process: communicate needs -> analyze through three perspectives -> review -> submit.
4. Analyze in this order: macro transaction structure -> meso contract structure -> micro clause wording.
5. If legal validity depends on current statutes, regulatory approvals, judicial interpretations, or local rules, tell the user to verify current law or consult qualified counsel.

## CITATION RULES

Every substantive claim based on the guide's methodology must include a citation to the original text.

**Quote files (load the relevant one):**

- `contract-drafting-quotes.md`: definitions of macro, meso, micro analysis; drafting principles; transaction structure; parties; three-points-one-line method.
- `contract-review-quotes.md`: the complete 三观四步法 statement, review principles, transaction-structure framing, and comprehensive review.

**Citation format - always use this exact structure:**

> "Source text here."
>
> - *合同起草审查指南*, topic anchor: https://github.com/simbajigege/book2skills/blob/main/skills/contract-drafting-and-review-guidance-china-law/quotes/FILENAME.md#ANCHOR

**Anchor mapping:**

- `contract-drafting-quotes.md`: `#transaction-structure-importance`, `#meso-contract-structure`, `#micro-clause-expression`, `#four-steps-process`, `#promote-transaction-principle`, `#risk-control-balance`, `#legal-business-combination`, `#contract-types`, `#parties-identification`, `#three-points-one-line-method`, `#review-checklist`, `#standard-final-goal`
- `contract-review-quotes.md`: `#three-perspectives-four-steps`, `#promote-transaction`, `#macro-transaction-structure`, `#three-points-one-line`, `#standard-purpose`, `#comprehensive-review`

**Rules:**

- Cite the guide when explaining 三观四步法, macro/meso/micro analysis, promote-transaction principle, or the three-points-one-line method.
- Keep source passages brief. Use the quote files for exact text and paraphrase the workflow in the response.
- If the user asks for binding legal advice, state that the skill provides review structure and drafting issues, not a formal legal opinion.

## Core Principle

Contract drafting and review should promote viable transactions while controlling legal and business risk. The agent must analyze the transaction at three levels: whether the deal structure works, whether the contract structure fits the deal, and whether the individual clauses are complete, clear, and enforceable.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Steps | Output | Independent trigger? | Distinct references? | Triage score | Should be subskill? | Reason |
|---|---|---|---|---|---|---|---:|---|---|
| Contract review | Please review this contract | Contract text, user role, concerns, governing law | Needs -> macro -> meso -> micro -> review comments -> risk summary | Structured review memo | Yes | Same guide | 3 | No | Primary workflow; uses all dimensions in sequence. |
| Contract drafting | Draft a contract framework for this deal | Deal facts, parties, subject, price, timeline, risk allocation | Needs -> transaction structure -> form selection -> clause framework -> open questions | Drafting outline and clause checklist | Yes | Same guide | 3 | No | Shares the same analysis order as review, only output differs. |
| Deal-structure diagnosis | Can this transaction be done this way? | Transaction goal, parties, assets/services, approvals, constraints | Macro analysis -> legal/business obstacles -> alternatives | Structure recommendation | Yes | Same guide | 3 | No | A macro slice that remains tightly coupled to later drafting. |
| Clause rewrite | Is this clause clear or risky? | Clause text, role, commercial intent | Identify right/obligation/liability points -> rewrite -> residual risk | Revised clause and rationale | Yes | Same guide | 3 | No | Micro slice but still uses the same three-points-one-line method. |
| Final review before signing | What should I check before signing? | Final draft, signing process, approvals | Macro/meso/micro spot check -> signing formalities -> submission note | Pre-signing checklist | Yes | Same guide | 2 | No | Review-gate step inside the main workflow. |

## Architecture Justification

Use a single-file skill because the guide is one integrated standard rather than a multi-domain book. All user tasks route through the same 三观四步法 sequence and differ mainly in output format. Separate subskills would duplicate the same macro, meso, micro, and review rules.

## DIMENSION 1: Communicate Needs

**The Rule:** A contract cannot be reviewed or drafted properly until the transaction goal, user role, risk tolerance, and desired deliverable are clear.

### Key questions to ask:

- What type of contract or transaction is involved?
- Who is the user in the transaction: buyer, seller, service provider, customer, licensor, licensee, investor, borrower, lender, landlord, tenant, or another role?
- Is the task review, drafting, clause rewrite, risk spotting, or negotiation preparation?
- What are the user's top concerns: payment, delivery, quality, termination, liability cap, IP, confidentiality, dispute forum, timing, or compliance?
- Is a formal legal opinion, redline, email summary, or negotiation checklist needed?

### Decision criteria / Checklist:

- Confirm the transaction objective and business background.
- Confirm the contract type and governing law assumption.
- Confirm user-side role and desired risk posture.
- Identify missing documents: annexes, orders, specifications, authorization files, board resolutions, permits, or prior agreements.
- If the facts are insufficient, ask targeted questions before giving detailed drafting language.

### Warning signals:

- The user provides only a clause but asks for a whole-contract conclusion.
- The user's commercial goal conflicts with the contract form.
- The user asks for maximum risk avoidance in a way that may block the transaction.
- The user wants a final legal opinion without enough facts or current-law verification.

### Agent instruction:

Start every contract review or drafting task by listing the minimum assumptions and missing facts. Do not invent deal facts. If the user provides enough context, proceed directly and mark unresolved assumptions.

## DIMENSION 2: Macro Transaction Structure

**The Rule:** First decide whether the transaction can be done and what structure should express the parties' main rights and obligations.

### Key questions to ask:

- Is the chosen contract type consistent with the real transaction?
- Are the parties legally capable, properly authorized, and commercially able to perform?
- Is the subject matter legal, transferable, identifiable, and deliverable?
- Are approvals, filings, registrations, bidding procedures, internal resolutions, or permits required?
- Does the structure need guarantees, security, escrow, phased performance, conditions precedent, or alternative legal relationships?

### Decision criteria / Checklist:

- Contract type: named or unnamed contract, mixed contract, framework agreement, order model, lease/license/sale distinction.
- Parties: legal status, authority, qualification, credit, performance capacity, affiliates, actual controller, guarantor, or missing necessary party.
- Subject matter: ownership, defects, encumbrances, transfer restrictions, quality/specifications, IP ownership, service scope, compliance.
- Procedure: approval, registration, filing, public bidding, internal decision, seal/signature authority, electronic signing validity.
- Structure: direct or indirect transaction, single or multiple contracts, security arrangement, staged closing, condition precedent.

### Warning signals:

- Counterparty identity differs from the actual performer or payee.
- The subject matter is restricted, disputed, encumbered, or insufficiently described.
- Required approvals or internal resolutions are absent.
- The contract tries to hide an unlawful purpose through form.
- A one-contract structure cannot capture the real transaction relationships.

### Agent instruction:

For review, produce a macro conclusion: `can proceed`, `can proceed after adjustment`, `high-risk`, or `do not proceed without counsel review`. For drafting, propose a structure before drafting clauses. Cite `contract-drafting-quotes.md#transaction-structure-importance` or `contract-review-quotes.md#macro-transaction-structure` when explaining macro analysis.

## DIMENSION 3: Meso Contract Structure

**The Rule:** Select the contract form and clause order that fit the transaction stage, operational workflow, and legal effect the parties need.

### Key questions to ask:

- Is this an intent letter, memorandum, reservation contract, framework contract, formal contract, order, settlement, supplement, or termination agreement?
- Should the document be binding, partially binding, or non-binding?
- Does a framework plus orders model fit repeated transactions?
- Are attachments, specifications, statements of work, acceptance standards, or service levels integrated correctly?
- Do clause order and definitions make the contract readable and internally consistent?

### Decision criteria / Checklist:

- Match document form to deal stage.
- Define legal effect for intent letters or negotiation-stage documents.
- For order models, define order issuance, acceptance, conflict rules, authority, and record retention.
- For electronic contracts, verify signature reliability, notice method, and format-clause risk.
- For group or affiliated-party contracts, define authorization and liability boundary.
- For package contracts, align main contract, annexes, side letters, and dispute-resolution clauses.

### Warning signals:

- A supposedly non-binding document contains binding obligations without saying so.
- Orders can be placed by unauthorized personnel.
- Annexes conflict with the main body.
- A later document modifies an earlier document without conflict rules.
- The contract structure is copied from a template that does not fit the transaction.

### Agent instruction:

When reviewing a contract's form, explain whether the document type matches the transaction and list structural fixes before line-level clause edits. Cite `contract-drafting-quotes.md#meso-contract-structure` when explaining meso analysis.

## DIMENSION 4: Micro Clause Expression and Three-Points-One-Line

**The Rule:** Clause review must connect prerequisites, rights and obligations, and liability consequences so the contract can be performed and enforced.

### Key questions to ask:

- What must happen before each obligation arises?
- Who has which right and who bears which obligation?
- What happens if the obligation is late, defective, partial, impossible, or refused?
- Are price, payment, delivery, acceptance, quality, IP, confidentiality, termination, breach, and dispute terms clear?
- Are terms defined consistently and drafted in enforceable language?

### Decision criteria / Checklist:

- Contract header: title, parties, recitals, authority, definitions.
- Core transaction clauses: subject, quantity/scope, quality, delivery or service process, acceptance, price, payment, invoice/tax, term, change process.
- Risk allocation: warranties, representations, confidentiality, IP ownership, data/security, compliance, insurance, force majeure.
- Exit and remedies: termination, rescission, cure period, liquidated damages, damages scope, liability cap, indemnity.
- Boilerplate: notice, governing law, dispute resolution, assignment, severability, entire agreement, counterparts, effectiveness, signing/seal.
- Expression quality: accurate, complete, unambiguous, non-contradictory, operationally executable.

### Warning signals:

- Rights exist without matching obligations or remedies.
- Liability clauses do not connect to specific breaches.
- Acceptance standards are subjective or missing.
- Payment timing is disconnected from delivery or acceptance.
- Broad obligations such as "all losses" or "best efforts" are undefined.

### Agent instruction:

For clause review, map the clause into prerequisite, right/obligation, and liability consequence. If any point is missing, propose revised language or a drafting instruction. Cite `contract-drafting-quotes.md#three-points-one-line-method` or `contract-review-quotes.md#three-points-one-line`.

## DIMENSION 5: Review, Submit, and Risk Communication

**The Rule:** A contract review is incomplete until macro, meso, and micro findings are checked together and communicated in a usable form.

### Key questions to ask:

- Do the proposed revisions support the user's business goal?
- Are the highest-risk issues separated from minor wording issues?
- Does the user need redlines, a risk memo, negotiation positions, or a final signing checklist?
- Are assumptions, missing facts, and unresolved legal questions clearly marked?
- Should any issue be escalated to licensed counsel, tax advisors, regulatory counsel, or business decision-makers?

### Decision criteria / Checklist:

- Re-check consistency across transaction structure, document form, and clauses.
- Rank risks by severity and negotiability.
- Provide exact amendment suggestions where possible.
- Mark business decisions separately from legal defects.
- Include signing formalities: names, seals, authority, dates, copies, annexes, electronic records.
- Preserve a written trail for major risk warnings.

### Warning signals:

- A long list of comments without prioritization.
- Treating minor drafting issues as deal blockers.
- Failing to document major risk warnings.
- Delivering clause edits without explaining business impact.

### Agent instruction:

End every review with a prioritized risk summary and next-action list. If the user needs a negotiation posture, classify each issue as `must change`, `should change`, `fallback`, or `business call`. Cite `contract-drafting-quotes.md#review-checklist` or `contract-review-quotes.md#comprehensive-review`.

## Query Response Framework

### Query Type 1: Review a contract

1. State assumptions and missing facts.
2. Identify contract type and user role.
3. Apply macro transaction-structure review.
4. Apply meso contract-structure review.
5. Apply micro clause review using three-points-one-line.
6. Rank risks and provide revision suggestions.
7. End with signing or negotiation next steps.

### Query Type 2: Draft a contract or contract outline

1. Confirm transaction goal, parties, subject, price, timeline, and risk posture.
2. Design the macro transaction structure.
3. Select the contract form and document architecture.
4. Produce a clause framework with key drafting points.
5. List open questions and required supporting documents.

### Query Type 3: Rewrite or evaluate a clause

1. Identify the clause's function.
2. Map prerequisite, rights/obligations, and liability consequences.
3. Identify ambiguity, gaps, or overreach.
4. Provide revised language or a drafting direction.
5. State residual risks and negotiation notes.

### Query Type 4: Pre-signing checklist

1. Confirm final draft and parties.
2. Check macro authority, approvals, and subject matter.
3. Check meso document consistency and annexes.
4. Check micro key clauses and signing formalities.
5. Provide a go/no-go checklist.

## Output Format

### Contract Review Memo

```markdown
## 合同审查意见

**合同类型:** [type]
**我方角色:** [role]
**适用法律假设:** [China law / unknown / user-specified]
**资料完整性:** [complete / missing items]

### 一、宏观 - 交易结构
| 项目 | 结论 | 风险 | 建议 |
|---|---|---|---|

### 二、中观 - 合同结构
| 项目 | 结论 | 风险 | 建议 |
|---|---|---|---|

### 三、微观 - 条款审查
| 条款 | 问题 | 修改建议 | 优先级 |
|---|---|---|---|

### 四、主要风险排序
1. [High-risk issue]
2. [Medium-risk issue]

### 五、下一步
[Redline / negotiate / ask for documents / counsel review / signing checklist]
```

### Contract Drafting Outline

```markdown
## 合同起草提纲

**交易目标:** [goal]
**当事方:** [parties]
**标的:** [subject]

### 一、交易结构设计
[Macro structure and required approvals.]

### 二、合同形式
[Document type and structure.]

### 三、条款框架（三点一线）
| 模块 | 应写内容 | 待确认事项 |
|---|---|---|

### 四、风险与谈判点
[Must-have terms and fallback positions.]
```

### Clause Rewrite Output

```markdown
## 条款审查与改写

### 条款功能
[What this clause is supposed to do.]

### 三点一线检查
| 点 | 是否完整 | 问题 |
|---|---|---|

### 修改建议
[Revised clause or drafting instruction.]

### 剩余风险
[What still needs business/legal confirmation.]
```

## Critical Reminders

1. Promote the transaction while controlling risk; do not make risk minimization the only goal.
2. Always analyze macro before meso and meso before micro.
3. Contract structure and clause wording must serve the real transaction, not the template.
4. Separate legal defects, business risks, and negotiable preferences.
5. Do not claim current legal validity without current-law verification.
6. Do not fabricate missing facts; ask concise follow-up questions or state assumptions.
7. This skill provides structured drafting and review support, not formal legal advice.
