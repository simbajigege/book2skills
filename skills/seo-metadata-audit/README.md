# seo-metadata-audit

A skill for performing comprehensive SEO metadata audits on webpages and HTML documents.

## Installation

```bash
npx skills add simbajigege/book2skills/skills/seo-metadata-audit
```

## What it does

Given a URL, HTML source, or page description, this skill audits the 10 most important HTML meta tags, scores each one, and produces a prioritized report with corrected code snippets.

**The 10 tags covered:**

| # | Tag | SEO Impact |
|---|---|---|
| 1 | `<title>` | ✅ Direct (~15% ranking weight) |
| 2 | `<meta name="description">` | CTR (not ranking) |
| 3 | `<h1>`–`<h6>` Headings | 🔄 Indirect |
| 4 | `<img alt="">` Image Alt | 🔄 Indirect |
| 5 | `rel="nofollow"` | 🔄 Indirect |
| 6 | `<meta name="robots">` | 🔄 Indirect |
| 7 | `<link rel="canonical">` | ✅ Indirect (PageRank consolidation) |
| 8 | Schema Markup / Structured Data | ✅ Direct (~1% + Rich Results) |
| 9 | Open Graph / Twitter Cards | Social sharing |
| 10 | `<meta name="viewport">` | 🔄 Indirect (mobile ~5%) |

**Output:** a scored report (X/46) with grade A–F, tag-by-tag findings, priority fix list, and ready-to-paste corrected HTML.

## File structure

```
seo-metadata-audit/
├── SKILL.md                  — Main skill: audit workflow, principles, cheat sheet, tools
└── references/
    ├── tag-reference.md      — Per-tag checklists, scoring criteria, common mistakes
    └── seo_10_meta_tags.md   — Background reading: ranking weights and concept explanations
```

## When it triggers

- User shares a URL or HTML and asks about SEO
- "Check my metadata / title / description / canonical"
- "Why isn't my page ranking?"
- "Audit my site's SEO"
- "Generate an SEO report"
- Questions about schema markup, Open Graph, robots tags, viewport, etc.

## Sources

Grounded in [SearchEngineJournal](https://www.searchenginejournal.com/) and [Google Search Central](https://developers.google.com/search) documentation.
