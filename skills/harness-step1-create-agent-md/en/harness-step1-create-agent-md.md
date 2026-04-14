---
title: "Harness Step 1 — Create AGENTS.md & Knowledge Base"
author: "simbajigege"
book_code: "harness-step1-create-agent-md"
description: "Scans your codebase and generates AGENTS.md (the agent's orientation file) plus a complete docs/ knowledge base skeleton, so any Claude Code session orients in under 30 seconds without you re-explaining the project."
tagline: "Scan once, orient forever — give your agent a permanent memory of the codebase"
tags: ["AI engineering", "Claude Code", "developer tools", "Harness Engineering", "agent support"]
cover_url: "/assets/books/covers/harness-step1-create-agent-md.png"
github_url: "https://github.com/simbajigege/book2skills/skills/harness-step1-create-agent-md"
download_url: "/skills/harness-step1-create-agent-md.zip"
related_skills:
  - title: "Harness Step 2 — Fill docs/ with Real Content"
    url: "/en/book/harness-step2-fill-docs"
  - title: "Harness Step 3 — Session State Management"
    url: "/en/book/harness-step3-session-management"
  - title: "SEO Metadata Audit"
    url: "/en/book/seo-metadata-audit"
examples:
  - human: "I'm starting to use Claude Code heavily on a Node.js monorepo — three services, shared packages, Turborepo build system. Every new session I have to explain the structure from scratch. Help me set up harness engineering, starting with AGENTS.md."
    ai: |
      I'll scan the repo first, then generate the files.

      **Scan findings:**
      - Build system: Turborepo (`turbo.json` detected)
      - Services: `apps/api/` (Express), `apps/web/` (Next.js), `apps/worker/`
      - Shared packages: `packages/db/`, `packages/ui/`, `packages/config/`
      - Package manager: `pnpm` (workspace)
      - Test runner: Vitest

      ---

      Generated `AGENTS.md` (written to repo root):

      ```markdown
      # MyMonorepo — Agent Guide

      ## What This Is
      A Node.js monorepo with three apps (API, Web, Worker) and shared packages,
      managed with Turborepo and pnpm workspaces.

      ## Quick Orientation
      - **Stack**: Node.js 20 + TypeScript / Express / Next.js 14 / Turborepo
      - **API entry**: `apps/api/src/index.ts`
      - **Web entry**: `apps/web/src/app/layout.tsx`
      - **Dev (all)**: `pnpm dev` (runs all apps in parallel via Turborepo)
      - **Dev (single)**: `pnpm --filter api dev`
      - **Test**: `pnpm test`
      - **Build**: `pnpm build`

      ## Knowledge Map
      Read the relevant doc before making any changes:

      | I want to understand... | Read this |
      |------------------------|-----------|
      | Module boundaries, dependency rules | `docs/ARCHITECTURE.md` |
      | Naming conventions, file structure | `docs/CONVENTIONS.md` |
      | Why we chose this tech stack | `docs/TECH_DECISIONS.md` |
      | Definition of done | `docs/QUALITY.md` |
      | Active work | `docs/exec-plans/active/` |
      | Backlog | `docs/exec-plans/backlog.md` |
      | Known tech debt | `docs/exec-plans/tech-debt-tracker.md` |

      ## Hard Rules
      - Never import from `apps/*` inside `packages/*` — packages must not depend on apps
      - Do not modify `packages/db/migrations/` directly — use the migration CLI
      - `apps/web/out/` is build output, never edit manually
      ```

      Also created `docs/` skeleton with placeholder content in all five files.

      **What needs your input:**
      - `docs/TECH_DECISIONS.md` has several "TODO: reason unknown" entries — fill in why you chose Turborepo over Nx, and why pnpm over npm
      - `docs/exec-plans/backlog.md` is empty — tell me 3–5 features you're planning to ship next

      Run `/harness-step2-fill-docs` next so I can deep-read the codebase and replace placeholders with real content.

  - human: "What's the difference between what goes in AGENTS.md vs docs/ARCHITECTURE.md? I'm not sure where to draw the line."
    ai: |
      Think of it this way: **AGENTS.md is a table of contents, docs/ is the book.**

      ## The Rule in One Sentence

      If an agent needs to *find* something → AGENTS.md.
      If an agent needs to *understand* something → docs/.

      ---

      ## Concrete Examples

      | Information | Where it goes | Why |
      |-------------|---------------|-----|
      | "Backend entry is `apps/api/src/index.ts`" | AGENTS.md | Agent needs this to navigate immediately |
      | "Run `pnpm dev` to start all services" | AGENTS.md | Orientation info — needs to be instant |
      | "The API layer must not import from the DB layer directly" | docs/ARCHITECTURE.md | This is a rule with reasoning, not a navigation aid |
      | "We use Turborepo because Nx was too heavyweight for our team size" | docs/TECH_DECISIONS.md | Historical decision with context |
      | "A task is done when tests pass and the PR description explains the 'why'" | docs/QUALITY.md | Standards require explanation |

      ---

      ## The Failure Mode to Avoid

      The most common mistake is copy-pasting architecture explanations into AGENTS.md because it "feels important." It's important, but it belongs in docs/.

      If your AGENTS.md is over 150 lines, it almost certainly has docs/ content in it.
      Move the explanations to the appropriate docs/ file and replace them with a one-line pointer:

      ```markdown
      ## Architecture
      See docs/ARCHITECTURE.md — read before touching any module boundaries.
      ```

      That one line is all AGENTS.md needs on the topic of architecture. The agent will follow the pointer.
---

# Harness Step 1 — Create AGENTS.md & Knowledge Base

The core problem with Claude Code on real projects: every new session starts cold. The agent has no idea what the project is, how it's structured, or what the rules are. You end up re-explaining the same things across dozens of sessions. This skill fixes that at the source — scan the codebase once, generate structured knowledge files, and every future session orients in under 30 seconds without your help.

## What Gets Generated

```
project-root/
├── AGENTS.md                    ← agent's orientation file, 80-120 lines
└── docs/
    ├── ARCHITECTURE.md          ← module map, dependency rules, data flows
    ├── CONVENTIONS.md           ← naming patterns, file organization
    ├── TECH_DECISIONS.md        ← why each framework/library was chosen
    ├── QUALITY.md               ← Definition of Done, code review checklist
    └── exec-plans/
        ├── active/              ← in-progress work
        ├── backlog.md           ← planned but not yet scheduled
        └── tech-debt-tracker.md ← known quality issues
```

## Design Principles

- **AGENTS.md is the table of contents, docs/ is the book**: agents use AGENTS.md to orient, docs/ to understand
- **Inferred ≠ invented**: anything that can't be confirmed from the codebase is marked "TODO: confirm" — never fabricated
- **Stack-agnostic**: Python, Node.js, Go, Rust; monolith, microservices, monorepo — all work

## Supported Use Cases

- Adding agent support to an existing project for the first time
- Onboarding to an unfamiliar codebase (let the agent read it first, then work with you)
- Refreshing agent context after a major refactor
- Any situation where you want Claude Code to stop asking "what is this project?"

## How to Use

1. Open Claude Code in your project root
2. Say "add agent support" or "create AGENTS.md" or "start harness engineering"
3. The skill scans 2–3 directory levels, dependency files, and existing docs
4. All files are generated; the skill lists what needs human confirmation
5. Run `harness-step2-fill-docs` next to deep-fill docs/ with content from the actual code

## Limitations

The skill reads files only — it can't observe runtime behavior (API response shapes, DB contents). `TECH_DECISIONS.md` often needs human input for historical context: the code shows what was chosen, but not why.
