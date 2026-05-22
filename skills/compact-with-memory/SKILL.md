---
name: compact-with-memory
description: Executes /compact correctly — generates a high-quality conversation summary that preserves reasoning, decisions, and current state, with a brief memory pre-pass to persist institutional knowledge before compression. Use when the user says /compact, "compress context", "compact the conversation", or the context window is getting full.
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

# compact-with-memory

Executes `/compact` with a memory pre-pass: extract what's worth keeping permanently, then generate a summary good enough for a fresh session to pick up exactly where this one left off.

## When to execute

- User says `/compact` or "compress context"
- Context window is approaching its limit
- Session has produced decisions or knowledge that would be lost after compression

## How to execute

### Step 1 — Memory pre-pass

Before compressing, scan the conversation for signals that **can't be derived from code or git history**:

| Type | What to capture |
|---|---|
| `feedback` | Corrections ("don't do X") AND confirmations ("yes, exactly") — always with the *why* |
| `project` | Decisions made, approaches eliminated, active blockers, deadlines (convert relative dates to absolute) |
| `user` | Role, expertise, preferences learned this session |
| `reference` | Pointers to external systems (Linear, Grafana, Slack, doc URLs) |

Write these to memory files now — they will be gone after compaction. Quality bar: if a signal lacks a **Why:**, skip it. One good entry beats five generic ones.

### Step 2 — Generate the summary

The summary **replaces the entire conversation history**. It must be self-contained: a fresh session with only this summary should be able to continue the work without asking what happened.

**Eight sections — write every one that has content:**

**1. Task**
What was being worked on and *why* — the goal, not the steps taken.

**2. Current state**
Exactly where things stand at the end of this session. What is done, what is not, what is in progress. This is the most critical section — it must reflect the conversation endpoint, not the starting point.

**3. Key decisions**
Choices made and the reasoning behind them. Non-obvious decisions especially: "chose X because Y constraint" is worth writing; "used standard approach" is not.

**4. Eliminated approaches**
What was tried and ruled out, and *why*. Prevents re-exploring dead ends in the next session. If nothing was tried and ruled out, omit.

**5. Open questions / blockers**
Unresolved issues, unanswered questions, and blockers the next session needs to address first.

**6. Files changed**
Which files were modified and what changed in each — enough to orient a fresh session without re-reading diffs.

**7. Next steps**
Concrete actions remaining, in priority order.

**8. Context for next session**
Anything a fresh Claude needs to know that didn't fit the above — environment quirks, unstated constraints, relevant background.

**Quality criteria for the summary:**
- A fresh session reading only this summary can continue the work
- Reasoning over facts: *why* decisions were made, not just *what* was decided
- Current state accurately reflects where the conversation ends, not where it started
- No padding: omit any section that genuinely has nothing to say

### Step 3 — Execute `/compact`

Run `/compact`. In the summary note, reference what was persisted to memory: "Key decisions written to memory — see [filename] for [topic]."

### Step 4 — Confirm

Report to the user:
- **Compact**: completed, with a one-line description of what the summary covers
- **Memory**: how many files were written/updated and which files
- **MEMORY.md line count**: current count (must stay under 200 lines)

## What NOT to save to memory

Code patterns, conventions, architecture, file paths, git history, debugging recipes — these are derivable from reading the code. Only persist what a fresh session cannot reconstruct before reading any files.

**Boundary test**: "Would a fresh session benefit from knowing this *before* reading any code?" If no — skip it.
