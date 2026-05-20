---
name: compact-with-memory
description: Enhanced /compact that doesn't just summarize — it extracts and persists key decisions, eliminated approaches, new patterns, and current blockers into MEMORY.md before compressing the conversation. Use this skill whenever the user says /compact, "compress context", "compact the conversation", or when the context window is getting full and you want to preserve institutional knowledge from this session. It ensures that after compression, future sessions can reconstruct the reasoning behind current state, not just the state itself.
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

# compact-with-memory

An enhanced `/compact` that treats compression as a memory opportunity: before summarizing, extract what's worth keeping permanently and write it to memory files.

## Why this matters

Standard compaction generates a 9-section summary and replaces the conversation history — fast, but lossy. This skill adds a pre-compression pass that distills the session's institutional knowledge into durable memory files.

Core principle: **only persist what can't be derived from reading the code or git history.** Everything else is noise.

## Process

### Step 1 — Orient: survey existing memory

Before analyzing the conversation, scan what memory already exists to avoid duplicates:

1. Read `MEMORY.md` — note which topics are already covered and by which files
2. Check MEMORY.md line count — it must stay under **200 lines / 25KB total**
3. Note the last-modified dates on existing files — memories older than ~1 day will get staleness warnings when recalled; this session may have corrections for them

### Step 2 — Gather: classify signals from the conversation

Read back through the conversation and sort signals into four types:

**`feedback`** — collaboration lessons (record both corrections AND confirmations)
- *Corrections*: "don't do X" — things the user pushed back on, with reasons
- *Confirmations*: "yes, exactly" / "perfect, keep doing that" — non-obvious choices the user accepted without pushback
- Why record confirmations? If you only record corrections, you avoid past mistakes but grow overly conservative about approaches that already worked.
- Structure: lead with the rule, then **Why:** (the incident or preference that drives it) and **How to apply:** (when this kicks in, enough context to judge edge cases)

**`project`** — facts about ongoing work not visible in code or git
- Architectural decisions and the tradeoffs behind them ("chose X over Y because Z")
- Eliminated approaches ("tried A, failed because B — don't retry")
- Active blockers or unresolved questions that will matter next session
- Deadlines, freeze dates, constraints — **always convert relative dates to absolute** ("next Thursday" → "2026-05-29")

**`user`** — who the user is: role, domain expertise, preferences

**`reference`** — pointers to external systems (Linear projects, Grafana dashboards, Slack channels, docs URLs)

### Step 3 — Consolidate: write or update memory files

For each identified signal:

1. **Check MEMORY.md index first** — update an existing file rather than creating a duplicate
2. If the content is substantial (more than 2-3 sentences), create a topic file:

```markdown
---
name: <short-kebab-case-slug>
description: <one-line summary — what would make this file worth loading in a future session?>
type: feedback | project | user | reference
---

<Lead with the rule or fact>

**Why:** <the reason — a past incident, strong preference, or constraint>
**How to apply:** <when/where this guidance kicks in>
```

3. Link related memories with `[[slug-name]]` syntax (even if the target file doesn't exist yet — it marks something worth writing later)
4. Add a pointer line to `MEMORY.md` (under 150 chars each):
   ```
   - [Title](filename.md) — one-line hook describing when this is relevant
   ```

### Step 4 — Prune: keep the index healthy

After writing:
- Verify MEMORY.md stays under 200 lines — if over, merge closely related entries or shorten pointer lines
- Remove pointers to files that were consolidated or deleted this session
- If an existing memory was contradicted by this session's findings, update it now (don't leave stale facts for the age-warning system to catch)

### Step 5 — Compact

Run the standard `/compact` command. The generated summary should note what was persisted: "Key decisions written to memory — see [file] for X."

### Step 6 — Confirm

Tell the user:
- How many memory items were written/updated and which files
- Current MEMORY.md line count (and whether it's within limits)
- That compaction completed

## What NOT to save

These are derivable from the codebase — saving them adds noise without value:

- Code patterns, conventions, architecture, or file paths — read the current code
- Git history or who-changed-what — `git log` / `git blame` are authoritative
- Debugging solutions or fix recipes — the fix is in the code; the commit message has context
- Anything already documented in CLAUDE.md files
- Ephemeral task details, in-progress work, current-session context

**Boundary test**: ask "Would a fresh session benefit from knowing this *before* reading any code?" If no — skip it.

## Examples

**Write to memory:**
- "We're using optimistic locking here because the DB doesn't support SELECT FOR UPDATE in this version" → `project`
- "The auth service always returns 200 even on failure — check `data.success` not status code" → `feedback` (correction)
- "User prefers small focused PRs over large refactor PRs — confirmed multiple times this session" → `feedback` (confirmation)
- "Bugs tracked in Linear project INGEST" → `reference`
- "merge freeze begins 2026-05-29 for mobile release cut" → `project`

**Don't write to memory:**
- "Implemented user authentication with JWT" — the code is the record
- "Fixed bug in login flow" — git commit has this
- "Read 5 files and summarized them" — noise
- "The Button component uses Tailwind classes" — readable from the code

## Quality bar

One high-quality entry beats five generic ones. If a signal lacks a **Why:**, it probably isn't worth persisting.
