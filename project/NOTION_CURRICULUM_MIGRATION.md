# v0.2 Notion Curriculum Migration (non-destructive)

This file is the implementation contract. An applied migration summary is recorded at the end; verify actual live schemas before further writes.

## Add three student-state databases under IOI Tutor

1. Learning Goals: Goal ID (title, Gxxxxxx), Curriculum, Target Division, Status, Stage, Baseline Status, Curriculum Commit, Started, Target Date, Notes.
2. Module Progress: Progress ID (title, MPxxxxxx), Goal (relation), Module Key, Progress Status, Mastery Status, Prerequisites Met, Independent Evidence, Transfer Evidence, Retention Evidence, Curriculum Commit, Next Review, Notes. One row per Goal+Module Key.
3. Assessments: Assessment ID (title, ASxxxxxx), Goal (relation), Assessment Type, Mode, Status, Result, Attempts (relation), Duration Min, Curriculum Commit, Rationale.

A single Notion Goal and multiple individual module progress rows may share the same Guide program; do not store the full external Guide catalog in Notion. No user skill/score is inferred from blank tables.

## Later small extensions to existing databases

- Attempts: Exposure Mode (GUIDED_LEARNING / BLIND_ASSESSMENT / UNKNOWN), Prior Exposure (YES / NO / UNKNOWN), optional Goal and Assessment relations.
- Training Queue: optional Goal and Module Key fields; continue to use existing Mode, Skill, Due, Priority, Status, Origin Attempt and Problem.
- Sources: optional Guide curriculum-reference field, while retaining the original OJ stable Source ID and original URL; unsupported origins may use Platform=OTHER with judge-qualified Source ID.
- Skill Profile: continue conservatively updating verified evidence. Start with UNKNOWN if no records exist.

## Migration safety

Fetch live schema before writes; add columns only if missing, never drop existing properties. Do not alter existing T/A/R/E/TR IDs, judge evidence, attempt history or code commits. Validate relation targets and preserve old Notion views. Do not auto-create 678 Training Queue entries, pretend an empty profile is mastered, or force a Goal to ACTIVE without the student's training intent.

## Acceptance checks

Create a *test Goal* only if explicitly requested or approved; attach one test progress and Assessment, verify relations, then delete/mark test data uncounted. Separately verify new H0 and redo isolation, unknown-exposure assessment exclusion, and pre-existing single-problem intake.

## Applied non-destructive migration — 2026-10-08

The three curriculum student-state databases were created under the private IOI Tutor Notion root: Learning Goals, Module Progress and Assessments. Resolve their actual IDs and URLs through the connected private Notion workspace at runtime; do not store private workspace identifiers in this public repository.

Module Progress has both a Goal relation and a stable Goal ID text key; Assessments has Goal and Attempts relations with matching stable ID fields. In the create_database connector, cross-data-source relations required a separate ADD COLUMN step after table creation.

Existing Attempts now additionally has Exposure Mode, Prior Exposure, Learning Goal and Assessment properties. Existing Training Queue additionally has Learning Goal, Module Key and Curriculum Commit properties. These are additive changes, not replacements.

Post-migration verification confirmed existing student records were preserved and no sample student-state rows were fabricated. Exact counts belong to Notion, not this repository.

Remaining P2 acceptance: real Gold Goal creation, at least one evidence-bearing Attempt round-trip through postmortem → Skill Profile → Module Progress → Training Queue, and a BLIND_ASSESSMENT check. Until then, never claim an end-to-end automated curriculum coach.
