---
name: seo-metadata-audit
description: Perform a comprehensive SEO metadata audit on any webpage or HTML document, grounded in the 10 most important HTML meta tags. Use this skill whenever the user shares a URL, HTML source, or page content and asks about SEO, metadata, title tags, meta descriptions, canonical tags, schema markup, open graph tags, social sharing, mobile optimization, or why a page might not be ranking well. Also trigger for requests like "check my SEO", "review my page's metadata", "audit this site", "improve my search ranking", "generate an SEO report", or "what's wrong with my page's SEO". When in doubt, use this skill — it's better to run a partial audit than to answer SEO questions without it.
license: "Skill distillation for personal/educational use. Do not reproduce source passages verbatim."
---

# SEO Metadata Audit

Perform a structured audit of a webpage's HTML metadata against the 10 most important SEO meta tags. The framework is grounded in SearchEngineJournal and Google's official documentation.

For detailed per-tag audit checklists, scoring criteria, and common mistakes, read `references/tag-reference.md`.

---

## Audit Workflow

### Step 1 — Collect the Data

Ask for or extract the following from the provided URL, HTML source, or page description:

- `<title>` tag content and character count
- `<meta name="description">` content and character count
- All `<h1>` through `<h6>` tags
- Image `alt` attributes (sample if many)
- External link `rel` attributes
- `<meta name="robots">` tag
- `<link rel="canonical">` tag
- Any `<script type="application/ld+json">` blocks
- Open Graph (`og:*`) meta tags
- Twitter card meta tags
- `<meta name="viewport">` tag

If the user provides a URL, fetch the page to extract this data. If they provide HTML, parse it directly.

### Step 2 — Score Each Tag

Read `references/tag-reference.md` for the full checklist per tag.

Rate each tag from 0 to its max score and calculate a total out of 46 possible points.

| Score Range | Grade | Assessment |
|---|---|---|
| 40–46 | A | Excellent — production ready |
| 30–39 | B | Good — minor fixes needed |
| 20–29 | C | Fair — several important issues |
| 10–19 | D | Poor — significant gaps |
| 0–9 | F | Critical — metadata severely lacking |

### Step 3 — Generate the Audit Report

Use this exact structure:

```
# SEO Metadata Audit Report
## Page: [URL or Page Name]
## Date: [Date]

### Executive Summary
[2–3 sentence overview of key findings]

### Score: XX / 46 — Grade: [A/B/C/D/F]

### Tag-by-Tag Results

| Tag | Score | Status | Key Finding |
|---|---|---|---|
| Title | X/5 | ✅/⚠️/❌ | ... |
| Description | X/5 | ✅/⚠️/❌ | ... |
| Headings | X/5 | ✅/⚠️/❌ | ... |
| Image Alt | X/4 | ✅/⚠️/❌ | ... |
| Nofollow | X/4 | ✅/⚠️/❌ | ... |
| Robots | X/4 | ✅/⚠️/❌ | ... |
| Canonical | X/5 | ✅/⚠️/❌ | ... |
| Schema | X/5 | ✅/⚠️/❌ | ... |
| Social (OG/Twitter) | X/5 | ✅/⚠️/❌ | ... |
| Viewport | X/4 | ✅/⚠️/❌ | ... |

### Priority Fixes (Ordered by Impact)
1. [Highest impact issue]
2. [Second priority]
3. [Third priority]
...

### Detailed Findings & Recommendations
[Per tag: what was found, what should be done, example code if needed]
```

### Step 4 — Provide Corrected Code

For any tag that fails or scores below 50% of its max, provide a corrected HTML snippet the user can copy directly into their page.

---

## Key Principles

1. **Prioritize by ranking impact** — Fix `<title>` and `canonical` before social tags
2. **Never keyword stuff** — Natural language always wins over mechanical repetition
3. **Unique per page** — Title, description, canonical, and OG tags must all be page-specific
4. **Test after changes** — Recommend Google Search Console, Rich Results Test, and Mobile-Friendly Test for validation
5. **Mobile first** — If viewport is missing, flag it as high priority regardless of other scores

---

## Quick Cheat Sheet

```html
<!-- 1. Title -->
<title>Primary Keyword - Secondary Topic | Brand Name</title>

<!-- 2. Description -->
<meta name="description" content="1–2 natural sentences describing the page. Include keywords naturally. Under 160 characters.">

<!-- 3. Headings — in HTML body -->
<h1>Primary Keyword Topic</h1>
<h2>Subtopic One</h2>
<h3>Sub-subtopic</h3>

<!-- 4. Image Alt -->
<img src="product.jpg" alt="Descriptive alt text with keyword where natural">

<!-- 5. Nofollow Links -->
<a href="https://external.com" rel="noopener noreferrer nofollow">Link Text</a>

<!-- 6. Robots (noindex example) -->
<meta name="robots" content="noindex, nofollow">

<!-- 7. Canonical -->
<link rel="canonical" href="https://example.com/this-page-url">

<!-- 8. Schema Markup -->
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "Article",
  "name": "Article Title",
  "description": "Article description."
}
</script>

<!-- 9. Open Graph + Twitter Cards -->
<meta property="og:title" content="Page Title"/>
<meta property="og:description" content="Page description."/>
<meta property="og:url" content="https://example.com/page"/>
<meta property="og:type" content="website"/>
<meta property="og:image" content="https://example.com/image.jpg"/>
<meta property="og:image:alt" content="Image description"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="Page Title"/>
<meta name="twitter:description" content="Page description."/>
<meta name="twitter:image" content="https://example.com/image.jpg"/>

<!-- 10. Viewport -->
<meta name="viewport" content="width=device-width, initial-scale=1"/>
```

---

## Useful Tools

| Tool | URL | Purpose |
|---|---|---|
| AITDK Extension | https://aitdk.com/zh-CN/extension/ | Free browser plugin: Title, Description, Headings, traffic |
| Detailed SEO Extension | https://detailed.com/extension/ | Check Canonical, OG tags, Robots, Schema |
| Google Rich Results Test | https://search.google.com/test/rich-results | Validate structured data |
| Google Mobile-Friendly Test | https://search.google.com/test/mobile-friendly | Check mobile optimization |
| Google Search Console | https://search.google.com/search-console | Monitor indexing, coverage, and performance |
| Google Structured Data Markup Helper | https://www.google.com/webmasters/markup-helper/ | Generate JSON-LD schema code |
