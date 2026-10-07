# Curriculum Discovery — USACO Guide

Use when the student starts a Gold/Platinum goal, asks for a Guide module, or requests a curriculum-targeted practice problem. The official site (https://usaco.guide/) is the upstream source of curriculum facts. This repository defines local behavior only.

## Read order

1. Confirm program USACO_GUIDE and division gold / plat; do not infer actual attainment.
2. Read official metadata at one pinned upstream commit. Prefer tools/usaco_guide_catalog.py in a capable runtime; alternatively use read-only GitHub source fetch of content/ordering.ts, module MDX frontmatter and its .problems.json.
3. Confirm the module id belongs to the requested division, and preserve category, source filename, module URL, prerequisites, raw frequency, module rank and upstream SHA.
4. Read section-organized problem entries, preserving uniqueId, original URL/source, per-module relative difficulty, starred flag, tags, solution availability and source order. Never fetch editorial bodies for candidate ranking.
5. Validate the same upstream uniqueId and module ID before reuse. On malformed or inconsistent data, report a source blocker; do not silently synthesize attributes.
6. Use references/curriculum-mapping.json only for Tutor-derived *candidate* Skill IDs; the mapping is not evidence that the student possesses the skill.

## Canonical identity

A Guide uniqueId is not a canonical Tutor Problem and must not become a T-ID. Resolve the original OJ Source against Notion first; create a new Problem only if no exact Source or strong exact identity exists. For USACO use stable cpid where available and consider legacy year/division Source aliases; for CF, AtCoder, CSES and other judges follow their stable native IDs. Platform labels, module ranks, URLs and fuzzy titles are not sufficient to merge Problems. Notion's existing Platform=OTHER option can represent unsupported judges, provided Source ID and original judge URL remain exact.

Create/reuse a canonical Problem only when an Attempt is actually assigned or when the user explicitly requests catalog ingestion. Never create hundreds of Problems or Training Queue items merely by visiting a course page. Keep Guide membership metadata separate from native Source rating and internal D1–D8.

## Privacy, spoilers and provenance

- In topic-guided learning, only the category and lesson content the student deliberately chose may be disclosed. Keep problem-specific decisive technique/pattern/answer information locked by H level.
- In BLIND_ASSESSMENT, never show Guide category/module, tags, or explanatory ranking; present the original judge statement/source and neutral logistics.
- In redo, retrieve no earlier code, root causes, hints, errors or solution notes before the new independent submission.
- Do not retain editorial text or reference code as student submissions.
- Record upstream commit SHA, fetched time, guide link and original judge URL; historical attempt metadata is immutable evidence even if Guide later changes.
- Upstream Guide difficulty is module-relative and may be inconsistent across modules. It is not D1–D8 and original contest division is a separate attribute.
- Respect https://usaco.guide/license, especially when storing/reproducing curated problem catalogs; prefer read-only on-demand metadata for individual self-study.

## Next step

Pass eligible candidates and their provenance to goal-planner.md or module-training.md. If the Notion curriculum tables are not installed yet, operate in read-only preview and explicitly mark Goal/Progress persistence as pending.
