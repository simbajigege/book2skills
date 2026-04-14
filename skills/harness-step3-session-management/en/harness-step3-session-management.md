---
title: "Harness Step 3 — Session State Management"
author: "simbajigege"
book_code: "harness-step3-session-management"
description: "Creates init.sh (environment health check), tasks.json (structured task queue), and progress.md (append-only session log) — so any new Claude Code session recovers full working context in under 30 seconds, with no re-explanation from you."
tagline: "State lives in files, not agent memory — permanently solve the amnesia problem"
tags: ["AI engineering", "Claude Code", "task management", "Harness Engineering", "session state"]
cover_url: "/assets/books/covers/harness-step3-session-management.png"
github_url: "https://github.com/simbajigege/book2skills/skills/harness-step3-session-management"
download_url: "/skills/harness-step3-session-management.zip"
related_skills:
  - title: "Harness Step 1 — Create AGENTS.md & Knowledge Base"
    url: "/en/harness-step1-create-agent-md"
  - title: "Harness Step 2 — Fill docs/ with Real Content"
    url: "/en/harness-step2-fill-docs"
  - title: "SEO Metadata Audit"
    url: "/en/seo-metadata-audit"
examples:
  - human: "My AGENTS.md and docs/ are solid now. The remaining pain point is that every new Claude Code session starts cold — I have to re-explain what we were working on. Set up session state management for me."
    ai: |
      I'll create three files. After this, every new session starts by reading them —
      context is restored in under 30 seconds without you saying a word.

      ---

      ## `init.sh` (environment health check)

      ```bash
      #!/bin/bash
      set -e
      echo "=== Environment Check ==="

      # Runtime check
      node --version | grep -E "v(20|2[1-9])" > /dev/null && echo "✓ Node version OK"

      # Dependencies
      [ -d "node_modules" ] || { echo "⚠ node_modules missing, run: npm install"; exit 1; }

      # Smoke test — fastest possible check that the app is importable
      node -e "require('./src/config')" && echo "✓ Config loads cleanly"

      echo "=== Ready. Check tasks.json for next task. ==="
      ```

      ---

      ## `tasks.json` (task queue)

      Based on the project state I can see:

      ```json
      {
        "project": "my-project",
        "last_updated": "2026-04-13",
        "current_focus": "Ship the billing integration",
        "tasks": [
          {
            "id": "billing-01",
            "title": "Wire Stripe webhook handler",
            "description": "Handle invoice.payment_succeeded and invoice.payment_failed events. Update user subscription status in DB. Idempotency key on webhook event ID.",
            "status": "pending",
            "priority": "high",
            "verify": "Run `npm test -- billing.test.ts` — all pass; send test webhook from Stripe dashboard, confirm subscription record updates in DB",
            "requires_eval": true
          }
        ]
      }
      ```

      Note: `requires_eval: true` here because this is a new feature touching payment and auth logic.

      ---

      ## `progress.md` (session log)

      ```markdown
      # Progress Log

      ## 2026-04-13 — Harness initialized
      - step1 complete: AGENTS.md + docs/ skeleton
      - step2 complete: docs/ filled with real content from codebase scan
      - step3 complete: session state management set up
      - Next: start billing-01 (Stripe webhook handler)
      ```

      Added "Session Startup Protocol" to `AGENTS.md`:
      ```markdown
      ## Session Startup
      1. `bash init.sh` — verify environment
      2. `git log --oneline -10` — see recent history
      3. `head -20 progress.md` — see where we left off
      4. Read `tasks.json` — pick highest-priority pending task
      ```

  - human: "How should I handle tasks that get blocked mid-session? Like if I'm working on billing-01 and discover I need a DB migration first?"
    ai: |
      Two moves: update the blocked task, then create the blocker as a new task.

      ## Step 1 — Mark the Blocked Task

      ```json
      {
        "id": "billing-01",
        "title": "Wire Stripe webhook handler",
        "status": "blocked",
        "blocked_by": "DB schema missing subscription_events table — needs billing-00 first",
        "priority": "high"
      }
      ```

      The `blocked_by` field is a message to the next agent session, not to you.
      Write it as if you're explaining to someone who has no context.

      ## Step 2 — Create the Blocker Task

      ```json
      {
        "id": "billing-00",
        "title": "Add subscription_events table migration",
        "description": "Create migration file for subscription_events table. Columns: id, user_id, stripe_event_id (unique), event_type, payload (jsonb), created_at. Run migration in dev, verify table exists.",
        "status": "pending",
        "priority": "high",
        "verify": "psql -c '\\d subscription_events' — shows all expected columns; stripe_event_id has UNIQUE constraint",
        "requires_eval": false
      }
      ```

      ## Step 3 — Update progress.md

      ```markdown
      ## 2026-04-13 — Discovered blocker on billing-01

      - billing-01 blocked: DB schema not ready
      - Created billing-00 (migration) as prerequisite
      - Next session: start with billing-00, then unblock billing-01
      ```

      ## The Pattern

      Blocked tasks in `tasks.json` are free information for the next session.
      Without this, the next agent starts billing-01, hits the same wall, and wastes time re-discovering the blocker.
      With this, it reads `status: blocked`, sees `blocked_by`, jumps to billing-00 automatically.

      The whole point of tasks.json is to make discoveries persistent across sessions — not just progress, but dead ends too.
---

# Harness Step 3 — Session State Management

Claude Code sessions are stateless by design. When a session ends, the agent forgets everything — what was being worked on, what was discovered, what's blocked and why. The typical workaround is to re-explain context at the start of every session. This skill replaces that workaround with a proper solution: state lives in files, not in agent memory.

## The Three Files

**`init.sh` — Environment health check**
Run at the start of every session. Verifies dependencies are installed, config files exist, and the app's core modules load cleanly. Catches environment drift in seconds before it wastes a session.

**`tasks.json` — Structured task queue**
Each task has: `id`, `title`, `description`, `status`, `priority`, `verify` (an executable completion check), `requires_eval` (whether independent review is needed before marking done), and optionally `blocked_by`. Agents don't guess what to do next — they read the queue.

**`progress.md` — Append-only session log**
After each session, one entry is prepended. The next session reads the top 20 lines to know exactly where things stand. History is never deleted — it forms a traceable work log.

## Session Startup Protocol (added to AGENTS.md)

```
1. bash init.sh          → verify environment
2. git log --oneline -10 → see recent history
3. head -20 progress.md  → see where we left off
4. read tasks.json       → pick highest-priority pending task
```

## The verify Field

Every task's `verify` field must be executable steps — not vague descriptions. Test: *could a completely uninformed person follow this verify and independently determine whether the task is done?* If no, make it more specific.

## When to Use

- After completing Harness Steps 1 and 2, to close the loop on agent continuity
- Long-running projects with multiple work sessions
- Any project where you find yourself re-explaining context at the start of Claude sessions

## Limitations

`tasks.json` is a queue, not an executor — tasks don't run automatically. Blocked tasks should document their `blocked_by` reason in enough detail that the next session can jump directly to the prerequisite without re-investigating.
