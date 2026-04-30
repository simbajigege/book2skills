---
name: seo-metadata-audit
description: Audit SEO metadata such as title, description, headings, alt, robots,
  canonical, schema, viewport, charset, and social tags.
license: Skill distillation for personal/educational use. Do not reproduce source
  passages verbatim.
---


# SEO Metadata Audit Skill

**Knowledge source:** 影响SEO最重要的10个metadata by 哥飞.

## Overview

Use this skill to audit a webpage's most important SEO metadata and produce a prioritized repair plan. It supports SEO practitioners, developers, founders, and content teams who need to diagnose whether a page gives search engines clear, crawlable, canonical, mobile-friendly, and structured signals.

## When to Use This Skill

Use this skill when the user provides a URL, HTML, page spec, or metadata list and asks:
- "Audit this page's SEO metadata."
- "Are my title and description good?"
- "Do I need canonical, robots, schema, or Open Graph tags?"
- "Why is this page not ranking or showing correctly?"
- "Create metadata for this page."

## Core Principle

SEO metadata works as a system: each tag clarifies what the page is about, how search engines should process it, and how users see it in search or social contexts. Do not optimize one tag while breaking crawlability, canonicalization, mobile rendering, or semantic structure.

## Workflow Inventory

| Workflow | User question pattern | Inputs | Steps | Output | Independent trigger? | Distinct references? | Triage score | Should be subskill? | Reason |
|---|---|---|---|---|---|---:|---:|---|---|
| Full metadata audit | "Audit this page" | URL/HTML, target keyword, page purpose | Inspect all tag families; rank issues | Priority issue table | Yes | Yes | 3 | No | Primary workflow; all tags interact. |
| Snippet optimization | "Fix title/description" | Title, description, keyword, intent | Check length, uniqueness, click value | Rewrite variants | Yes | Yes | 3 | No | Narrow but uses same metadata scoring. |
| Crawl/index control | "Should this page be indexed?" | Page role, duplicates, robots/canonical | Decide index, follow, canonical | Indexing directive plan | Yes | Yes | 3 | No | Kept single-file because output rolls into audit plan. |
| Structured/social preview | "Add schema/Open Graph" | Page type, entity data, social preview | Choose schema and OG/Twitter tags | Markup checklist | Yes | Yes | 3 | No | Same input and repair report. |

## Architecture Justification

Metadata tags can be checked independently, but mistakes often arise from interactions: canonical can override indexing intent, title affects snippet relevance, heading and schema affect semantic clarity, and viewport affects mobile rendering. A single audit skill keeps these dependencies visible.

## DIMENSION 1: Relevance and Snippet Signals

**The Rule:** Title, description, and headings must communicate page topic and search intent clearly without keyword stuffing.

### Key questions to ask:
- Is the title unique, concise, and keyword-relevant?
- Does the description improve click-through with natural language?
- Is there one clear H1 and a logical H2-H6 hierarchy?

### Decision criteria / Checklist:
- Title around 50-60 characters where possible.
- Description around 150-160 characters where possible.
- One H1 aligned with page intent.
- Headings structure the page rather than style text visually.

### Warning signals:
- Duplicate titles across pages.
- Keyword stuffing in title or description.
- Missing H1 or multiple confusing H1s.

### Agent instruction:
When the user shares HTML or metadata, audit snippet signals first because they determine both search understanding and user click behavior.

## DIMENSION 2: Crawl, Index, and Canonical Control

**The Rule:** Robots and canonical tags must tell search engines which URLs deserve indexing and authority consolidation.

### Key questions to ask:
- Should this page be indexed?
- Does canonical point to the true preferred URL?
- Are duplicate or parameterized pages consolidated correctly?
- Are important pages accidentally blocked?

### Decision criteria / Checklist:
- Robots meta matches the page's business role.
- Canonical points to the correct self or preferred equivalent URL.
- Nofollow is reserved for untrusted, paid, or user-generated links.
- Index control is not applied globally by accident.

### Warning signals:
- Canonical on every page points to homepage.
- Important pages marked noindex.
- Nofollow used indiscriminately on internal links.

### Agent instruction:
For indexation questions, state the desired search-engine behavior first, then choose robots and canonical directives to match that behavior.

## DIMENSION 3: Media, Mobile, and Encoding Foundations

**The Rule:** Search engines and users need accessible images, mobile rendering, and correct character interpretation.

### Key questions to ask:
- Do meaningful images have descriptive alt text?
- Is viewport configured for responsive mobile display?
- Is charset declared correctly?

### Decision criteria / Checklist:
- Alt describes image content or function naturally.
- Viewport includes responsive width and scale settings.
- Charset is declared early and matches the document.

### Warning signals:
- Empty alt on informative images.
- Missing viewport on mobile-facing pages.
- Encoding problems that break snippets or content display.

### Agent instruction:
When auditing technical metadata, flag these as foundational issues even if they are not the user's original focus.

## DIMENSION 4: Structured and Social Context

**The Rule:** Schema and social metadata help machines and platforms understand, classify, and preview the page.

### Key questions to ask:
- What schema type fits this page?
- Are required structured fields present and accurate?
- Do Open Graph or social tags match the intended share preview?

### Decision criteria / Checklist:
- Schema matches the page type and visible content.
- Structured data is accurate, not spammy.
- Social title, description, and image are deliberate.

### Warning signals:
- Schema claims content not visible on the page.
- Missing social image or mismatched preview copy.
- Structured data added without page-level purpose.

### Agent instruction:
Recommend schema and social tags only after identifying page type, entity, and user intent.

## Query Response Framework

### Query Type 1: Full SEO metadata audit
1. Identify page purpose and target search intent.
2. Audit relevance, crawl/index, technical foundations, and structured/social context.
3. Rank issues by search impact and implementation risk.
4. Provide corrected tag examples.

### Query Type 2: Generate metadata
1. Ask for page purpose, primary keyword, brand, canonical URL, page type, and locale if missing.
2. Draft title, description, canonical, robots, OG, Twitter, viewport, charset, and schema recommendations.
3. Explain why each tag is included or omitted.

### Query Type 3: Diagnose ranking/indexing problem
1. Check index eligibility and canonical first.
2. Then inspect title, headings, content alignment, and schema.
3. Separate metadata issues from broader content, authority, and technical SEO issues.

## Output Format

```markdown
## SEO Metadata Audit
**Page:** ...
**Verdict:** Healthy / Needs fixes / Indexing risk / Snippet weak

| Tag / Signal | Status | Issue | Recommended Fix | Priority |
|---|---|---|---|---|

## Corrected Metadata
```html
...
```

## Implementation Notes
- ...

## Citations
- ...
```

## Critical Reminders

1. Title is important, but metadata is a system.
2. Description influences clicks even when it is not a direct ranking factor.
3. Canonical errors can erase good content from search visibility.
4. Do not block important pages accidentally.
5. Schema must describe real visible content.

## CITATION RULES

Every substantive metadata recommendation must include a citation to the source quote files.

**Quote files:**
- `seo-metadata-quotes.md` — strategy, title, description, H1, alt, nofollow, canonical, and canonical mistakes.
- `seo-technical-quotes.md` — technical tag details, robots, viewport, charset, Open Graph, and schema markup.

**Citation format:**

> "Author's exact words here."
>
> — [*影响SEO最重要的10个metadata*, cited excerpt](https://github.com/simbajigege/book2skills/blob/main/skills/seo-metadata-audit/quotes/FILENAME.md#ANCHOR)

**Anchor mapping:**
- `seo-metadata-quotes.md`: `#comprehensive-strategy`, `#title-importance`, `#title-keyword-ranking`, `#semantic-matching`, `#description-click-rate`, `#h1-essential`, `#alt-for-image-search`, `#nofollow-weight`, `#canonical-weight-aggregation`, `#canonical-mistake`
- `seo-technical-quotes.md`: `#comprehensive-seo-strategy`, `#title-length-importance`, `#title-brand-position`, `#description-length`, `#heading-hierarchy`, `#alt-description-best-practice`, `#nofollow-evolution`, `#robots-meta-control`, `#canonical-purpose`, `#viewport-mobile`, `#charset-encoding`, `#open-graph-social`, `#schema-markup`

**Rules:**
- Cite the closest tag-specific anchor for each major recommendation.
- If auditing a real page, distinguish observed defects from general best practice.
- Do not invent quote text; use exact quote files only.
