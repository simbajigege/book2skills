---
title: "Harness Step 2 — Fill docs/ with Real Content"
author: "simbajigege"
book_code: "harness-step2-fill-docs"
description: "Deep-reads your codebase and fills every docs/ file with specific, accurate content grounded in what the code actually does — module rules with examples, naming patterns with real instances, tech decisions with inferred rationale."
tagline: "Turn skeleton docs into a knowledge base agents actually learn from"
tags: ["AI engineering", "Claude Code", "documentation", "Harness Engineering", "architecture docs"]
cover_url: "/assets/books/covers/harness-step2-fill-docs.png"
github_url: "https://github.com/simbajigege/book2skills/skills/harness-step2-fill-docs"
download_url: "/skills/harness-step2-fill-docs.zip"
related_skills:
  - title: "Harness Step 1 — Create AGENTS.md & Knowledge Base"
    url: "/en/harness-step1-create-agent-md"
  - title: "Harness Step 3 — Session State Management"
    url: "/en/harness-step3-session-management"
  - title: "SEO Metadata Audit"
    url: "/en/seo-metadata-audit"
examples:
  - human: "I ran harness-step1 and got the docs/ skeleton. Now I want to fill it in. The project is a Go microservices backend with a React dashboard. Start with ARCHITECTURE.md and CONVENTIONS.md."
    ai: |
      Scanning the codebase first. I'll only write what I can actually infer — anything uncertain gets flagged.

      ---

      ## Scan Results

      Read: `cmd/api/main.go`, `internal/handler/`, `internal/service/`, `internal/repository/`,
      `internal/domain/`, `go.mod`, `frontend/src/`, `frontend/package.json`

      Key observations:
      - Clean architecture pattern: `handler → service → repository → postgres`
      - Domain types live in `internal/domain/` — imported by all layers
      - `internal/repository/` uses `sqlx`, raw SQL (no ORM)
      - Frontend: React 18 + Vite + Zustand for state

      ---

      ## Writing `docs/ARCHITECTURE.md`

      ```markdown
      # Architecture

      ## Backend Layering

      HTTP → Handler (gin, request parsing only) → Service (all business logic)
           → Repository (sqlx, SQL queries) → PostgreSQL

      Dependency direction is strict: handlers import services, services import repositories,
      repositories import domain types. No layer may skip upward.

      Domain types (`internal/domain/`) are the only package imported across layers freely.

      ## Key Constraint
      Handlers must not call repository methods directly.
      Business rules must not live in handlers.
      SQL must not live in services.
      ```

      ## Writing `docs/CONVENTIONS.md`

      ```markdown
      # Conventions

      ## File Naming (Go)
      - Handlers: `{domain}_handler.go` — e.g. `user_handler.go`
      - Services: `{domain}_service.go`
      - Repositories: `{domain}_repository.go`
      - Domain types: `{domain}.go` inside `internal/domain/`

      ## Naming
      - Exported identifiers: PascalCase
      - Unexported: camelCase
      - Error variables: `ErrXxx` pattern
      - Interfaces: noun or `XxxService`, `XxxRepository` (never `IXxx`)
      ```

      ---

      **Marked "TODO: confirm" — needs your input:**
      - `TECH_DECISIONS.md`: Why `sqlx` over GORM? Inferred reason: team wanted SQL control over magic. Please confirm.
      - `TECH_DECISIONS.md`: Why Zustand over Redux? Inferred: smaller bundle, simpler API for this dashboard's scale. Confirm?
      - `QUALITY.md`: What's the p95 API response time target? Can't infer from code.

  - human: "The ARCHITECTURE.md looks good but the dependency rule section is vague. How do I make it more actionable for an agent?"
    ai: |
      The key is to make every rule answer "what happens if I break this?" — agents follow rules better when consequences are explicit.

      ## Weak vs. Strong Rule Writing

      **Weak (what you have):**
      ```markdown
      Dependency direction is strict: handlers import services, services import repositories.
      No layer may skip upward.
      ```

      **Strong (actionable):**
      ```markdown
      ## Dependency Rules

      | Layer | May import | May NOT import |
      |-------|-----------|----------------|
      | `handler/` | `service/`, `domain/` | `repository/` directly |
      | `service/` | `repository/`, `domain/` | `handler/` |
      | `repository/` | `domain/` | `service/`, `handler/` |
      | `domain/` | stdlib only | anything internal |

      **Why this matters:** A handler that calls a repository bypasses service-layer
      validation and transaction management. A repository that imports a service creates
      a circular dependency that breaks compilation.

      **How to check:** `go build ./...` catches circular imports at compile time.
      For layer violations, run `go vet` with the custom layering linter (see docs/linting.md).
      ```

      ## The Two Ingredients of an Actionable Rule

      1. **A table or explicit list** — agents parse structured data better than prose descriptions of the same information
      2. **A verify command** — if the agent can run a command to check compliance, it will

      Apply the same pattern to every rule in the file. If a rule can't be verified by running something, at minimum add an example of what a violation looks like so the agent can spot it in a diff.
---

# Harness Step 2 — Fill docs/ with Real Content

After Step 1 creates the docs/ skeleton, the most common outcome is a set of files with placeholder text. An agent reading "naming conventions: see code" gets nothing useful. This skill fixes the gap — it reads the actual codebase deeply and writes specific, accurate documentation backed by real code examples.

## What Gets Filled In

| File | Content written |
|------|----------------|
| `docs/ARCHITECTURE.md` | Module responsibilities, dependency direction rules (with reasons), main data flows |
| `docs/CONVENTIONS.md` | File naming patterns (with real examples), variable/function naming rules |
| `docs/TECH_DECISIONS.md` | Rationale for each major framework/library (inferred where possible; flagged where not) |
| `docs/QUALITY.md` | Project-specific Definition of Done, code review checklist |
| `docs/exec-plans/tech-debt-tracker.md` | Duplicate code, naming inconsistencies, TODO comments found during scan |

## Core Principle

**Inferred content is labeled as inferred. Unknown content is marked "TODO: confirm."** Nothing is fabricated to fill space.

After the scan, the skill produces a "TODO: confirm" list — typically 3–5 items per project, concentrated around historical tech decisions (the code shows the choice, not why it was made) and runtime metrics (which can't be read from files).

## Supported Use Cases

- Immediately after Step 1, to fill skeleton with real content
- After a major refactor, to resync docs with current code
- Taking over an unfamiliar codebase and generating architecture docs for it

## How to Use

1. Confirm the project has `AGENTS.md` and `docs/` directory (from Step 1)
2. Say "fill in the docs" or "write ARCHITECTURE.md" or "analyze codebase and write docs"
3. The skill reads entry files, module boundaries, dependency declarations, naming patterns
4. All docs/ files are written; "TODO: confirm" list is surfaced
5. You confirm or fill in only what the skill couldn't infer

## Limitations

The skill reads files — it doesn't access git history or team communication. Historical decision rationale ("why did we choose X?") typically needs human input. Runtime behavior (actual query performance, API response shapes) can't be inferred from source files.
