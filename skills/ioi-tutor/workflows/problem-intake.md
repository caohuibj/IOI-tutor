# Problem Intake

Use for a new platform problem ID, title, or URL.

## Goal

Resolve the external Source to exactly one canonical Tutor Problem, create/reuse the durable Notion record, then open a new independent Attempt in `SOLUTION_LOCKED` state.

## Procedure

1. Normalize the input using `references/platforms.json`.
2. Fetch the public problem statement and constraints from the platform when possible.
3. Query Notion `Sources` by exact stable `Source ID`.
4. If found, follow its `Problem` relation. Do not create a duplicate canonical Problem.
5. If not found, check for a strong exact identity match (same explicit source or normalized statement). Never merge on fuzzy title alone.
6. If genuinely new, allocate the next `Txxxxxx`, create `Problems`, then create the `Sources` row and relation.
7. Internally classify problem taxonomy and difficulty. Preserve native platform difficulty separately.
8. Store taxonomy IDs in Notion, but enforce spoiler levels when speaking to the student.
9. Determine `attempt_no = prior independent attempts + 1`; create `Txxxxxx-Axx` with `status=ATTEMPTING`, `Hint Max=H0`, `Hint Count=0`, `Independent=true` unless explicitly contest/assisted mode.
10. Enter `SOLUTION_LOCKED`.

## Output at H0

May show: canonical Tutor ID, source identity, statement/constraints needed to work, native difficulty if already public on the platform, and neutral logistics.

Do not reveal technique/pattern/key insight tags whose spoiler level exceeds H0.

## Redo

For `重做 Txxxxxx`, reuse the Problem but create a new Attempt. Do not read old code, Error Events, key insights, or hint history before the new submission.


## Curriculum candidate resolution (v0.2 pilot)

A USACO Guide uniqueId is a curriculum reference, not an original OJ Source ID. Resolve the upstream problem URL to the judge's stable native ID; find existing Notion Sources and reuse its canonical Problem before allocating Txxxxxx. Preserve Guide module-relative difficulty and starred state per membership, rather than overwriting original contest rating or Tutor D1-D8. Multiple module memberships must not cause duplicate Problems.

For BLIND_ASSESSMENT, show the original OJ statement and neutral logistics only; suppress Guide module title/category, protected tags, editorial kind and selection rationale. GUIDED_LEARNING may reveal the topic the learner intentionally chose but no locked problem-specific solution. Record prior-exposure mode separately from H0.

## Checklist synchronization (v0.2-dev.2)

On every problem/source intake, follow catalog-checklist.md alongside this workflow. Resolve original OJ identity → match exact Guide ID in private "USACO Guide 题目清单" if present, then reuse/create canonical T ID and start H0 Attempt. Update checklist Status=ATTEMPTING, Tutor ID and Latest Attempt ID only after Attempt exists. The checklist itself is NOT the canonical Problems database. If no matching Guide entry, do not invent one; the existing single-problem workflow continues normally. Never show Guide-derived module/tags in BLIND_ASSESSMENT.
