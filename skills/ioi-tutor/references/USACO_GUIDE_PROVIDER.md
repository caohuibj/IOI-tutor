# USACO Guide Curriculum Provider (v0.2 pilot)

## Authority and license

- Upstream facts: https://usaco.guide/ and https://github.com/cpinitiative/usaco-guide.
- Official permission summary: https://usaco.guide/license. Personal self-study and sharing links are permitted, with CC BY-NC-SA 4.0 conditions. Do not redistribute lesson text, editorials, reference code, the full problem catalog or the site's presentation in this public repository.
- This repository owns Tutor-specific mappings, workflows, schemas and progression criteria. They are **not** official USACO certification or ranking rules.
- Notion is the only authority for the student's current Goals, Module Progress and Assessments once their databases exist.

## Read-only runtime

The standard-library tool tools/usaco_guide_catalog.py reads the upstream Git SHA, content/ordering.ts, each MDX frontmatter, and each corresponding .problems.json. It emits a snapshot to stdout or a caller-selected local file; do not check generated snapshots into this repository. It never reads lesson bodies or editorials.

Examples (run from a checkout with Python 3.11 or newer):

    python tools/usaco_guide_catalog.py --module gold:intro-dp --module gold:dsu --module plat:binary-jump --output /tmp/usaco-guide-pilot.json
    python tools/usaco_guide_catalog.py --division gold --output /tmp/usaco-guide-gold.json
    python tools/usaco_guide_catalog.py --division plat --output /tmp/usaco-guide-plat.json
    python -m unittest discover -s tests/curriculum -p 'test_*.py' -v

The first command does not require downloading or storing solutions. Snapshot provenance includes the pinned upstream SHA. The tool is read-only: it neither allocates T-IDs nor writes Notion records.

## Identity and difficulty

1. Guide problem uniqueId is a **curriculum reference**, not a Tutor Problem ID or OJ Source ID.
2. Dedupe Tutor Problems only after resolving the original judge's stable identity against Notion Sources. Never dedupe on fuzzy titles.
3. A Guide problem may appear in multiple modules: its difficulty, starred status, section, position, tags and editorial kind belong to the **membership**, not the canonical Problem.
4. Guide Gold/Platinum placement, original contest division, Guide module-relative difficulty, and Tutor D1-D8 are distinct fields.
5. Preserve raw relative difficulty labels including Normal/Medium as given. Do not convert them automatically to D1-D8.
6. Module prerequisites are upstream curriculum IDs; map them separately to Tutor skills where justified. Absence of a prerequisite list is not evidence of readiness.

## Spoiler boundary

Tags, editorial kinds, hints and module relationship can be solution-bearing. They are marked LOCKED in the snapshot and must be filtered from H0 delivery unless the student explicitly entered topic-guided learning. In BLIND_ASSESSMENT, hide category/module, technique tags, starred hints and algorithm-identifying filenames or URLs; present the **original OJ statement** instead of a Guide module page. Redo must not retrieve prior Attempts, code, Errors or hints before a fresh submission.

## Current scope

P1 source discovery and read-only metadata snapshot are supported. A database migration and student Goal creation are separate steps; do not claim end-to-end auto-planning until the Goals/Progress/Assessments tables and evidence loop are working and evaluated. Follow workflows/curriculum-discovery.md.

Conclusion category modules are retained as distinct CONCLUSION metadata, not automatically treated as core lesson-mastery requirements. The lesson/module count displayed on the live website can differ from the raw upstream ordering snapshot; do not hard-code the UI count as a parser invariant.

## Private student checklist index

The student explicitly requested a private full per-problem checklist even before registering on Guide. An attributed minimal ID/title/original OJ link/module-relative difficulty index is therefore maintained in their private Notion IOI Tutor workspace. It contains no lesson/editorial bodies. Its 707 distinct IDs at pinned upstream SHA 81339eea4b5e43a0a1e26365f8dc8dfaa60f7705 represent 744 module-problem references (including focus/examples/conclusion); these **must not be equated** with the website's Gold 410 + Platinum 268 progress-counter totals. A source refresh must be idempotent on Guide uniqueId and must preserve all student progress state.

Follow workflows/catalog-checklist.md for cross-chat updating. Do not expose private Notion workspace URL or student progress counts in public repository content.
