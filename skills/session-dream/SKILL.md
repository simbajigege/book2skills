---
name: session-dream
description: End-of-session memory distillation — extracts key decisions, eliminated approaches, new discoveries, and current blockers from the current conversation and writes them to MEMORY.md topic files. Based on Claude Code's autoDream background consolidation service. Activate when the user says "dream", "/dream", "save session memories", "distill this session", "what should I remember from this session", or when a long productive session is ending and the user wants to preserve what was learned.
---

# session-dream

A manual trigger for the memory distillation that Claude Code's `autoDream` service does automatically in the background. Where `autoDream` fires after 5+ sessions and 24+ hours, this skill fires on demand — letting you capture a session's insights before they're lost in compaction.

## How autoDream works (the source pattern)

From `services/autoDream/consolidationPrompt.ts`, the autoDream process has 4 phases:

1. **Orient** — scan what memory already exists, avoid creating duplicates
2. **Gather signal** — identify new information worth persisting (logs, session transcripts, drifted facts)
3. **Consolidate** — write or update topic files, merge rather than duplicate, fix contradictions
4. **Prune and index** — keep MEMORY.md under max lines, one pointer per file, remove stale entries

This skill follows the same 4-phase structure but applies it to the current conversation rather than historical transcripts.

## Distillation Process

### Phase 1 — Orient

Check what memory already exists:
- Read `MEMORY.md` if it exists (or note that it doesn't)
- Scan memory topic files mentioned in the index
- Note which topics are already covered so new entries extend rather than duplicate

### Phase 2 — Gather signal from this session

Review the current conversation and identify:

**High-value (always distill):**
- Architectural decisions with reasoning ("chose X over Y because Z")
- Approaches that failed and why ("tried A, hit wall B, abandoned — don't retry")
- Surprising discoveries about the codebase or APIs
- User preferences stated or demonstrated repeatedly
- Constraints or requirements that weren't in any file
- Corrections to prior assumptions

**Medium-value (distill if not easily discoverable):**
- Naming conventions used in this session
- Test setup patterns discovered
- Environment-specific quirks
- Current blockers and their root causes

**Low-value / skip:**
- What files were read
- What commands were run
- Implementation details visible in code
- Step-by-step narration of what was done

### Phase 3 — Consolidate to memory files

For each high-value item:

1. Check if an existing topic file covers this. If yes, update or append to it.
2. If no existing file fits, create a new topic file.

**Topic file format:**
```markdown
---
name: [descriptive topic name]
description: [one line — what query would cause this file to be loaded?]
type: feedback | project | user | reference
---

[For feedback/project type, lead with the rule or fact]

**Why:** [the reason this matters — context that makes the rule sensible]

**How to apply:** [when/where this kicks in]
```

**Key types:**
- `feedback`: User preferences, corrections, confirmed approaches — things that shape HOW to work
- `project`: Facts about the current project — decisions, constraints, current state
- `user`: Information about the user's background, expertise, goals
- `reference`: Pointers to external resources, tools, docs

Convert relative dates to absolute dates: "yesterday" → "2026-04-15", "last week" → "2026-04-07".

### Phase 4 — Prune and index

Update `MEMORY.md`:
- Add pointers for new topic files: `- [Title](filename.md) — one-line hook`
- Update pointers for modified files if the description changed
- Remove any pointers that now point to deleted/superseded content
- Keep MEMORY.md under 200 lines (lines beyond 200 get truncated)
- Keep each pointer line under 150 chars

### Report

At the end, tell the user:
- How many memory items were written/updated/archived
- Which files were touched
- Any contradictions with existing memory that were resolved
- 1-2 sentence summary of the session's key learnings

## Example output

Good memory entry for a `feedback` type:
```
**Rule:** For this project, prefer explicit error types over generic Error objects.
**Why:** The error handling middleware needs to distinguish between validation errors (400) and server errors (500) — string matching on error messages is fragile.
**How to apply:** When writing any error-throwing code in the API layer, create or use a typed error class (ValidationError, AuthError, etc.).
```

Good memory entry for a `project` type:
```
The payments module uses Stripe's older API (v2019-10-17) pinned in config — do not upgrade without coordinating with the billing team.
**Why:** An upgrade in 2025-Q3 broke webhook signature validation and caused missed payment events. The pin is intentional.
**How to apply:** When touching payments code, verify any Stripe API usage against the v2019-10-17 docs, not the latest.
```
