# Code Review

Use when the student submits code or asks why a revision fails/performs poorly.

## Revision intake

1. Identify the active Attempt.
2. Allocate the next Revision ID `Txxxxxx-Axx-Rxx`.
3. Preserve the student's code exactly. Do not silently repair it before archiving.
4. If `OI-training` is available, archive the revision at `problems/Txxxxxx/Axx/Rxx.<ext>` and record repository/path/commit SHA in Notion `Revisions`.
5. If no judge evidence is supplied, set `Judge Result=UNTESTED` and keep static conclusions explicitly probabilistic.

## Review order

Reconstruct before criticizing:

1. **Algorithm reconstruction** — state what the submitted code is actually trying to compute.
2. **Correctness** — invariants, state semantics, transitions, coverage, boundaries.
3. **Complexity** — actual time/space including hidden loops/state growth/constants.
4. **Data structure fit** — only after model/complexity are understood.
5. **Implementation** — indexing, overflow, initialization, recursion, lifecycle.
6. **Debugging process** — whether failure could be localized more systematically.
7. **Contest strategy** — partial-score path, time allocation, premature coding.
8. **Code quality** — only after substantive correctness/performance.

## Diagnostic protocol

For a failing/partial revision, produce internally:

- `judge_evidence`: observed verdict/score/subtasks or UNTESTED.
- `first_failure`: earliest decisive logical/complexity/implementation failure.
- `symptoms[]`: e.g. WA, TLE, out-of-bounds.
- `root_cause`: one primary Error Taxonomy code when justified.
- `secondary_errors[]`.
- `evidence`: counterexample, dependency violation, complexity derivation, or code location.
- `confidence`: 0..1.
- `skill_targets[]`: map through `error-taxonomy.json` / `skill-graph.json`.

Do not label a symptom as root cause merely because it is visible first.

## Student-facing response

Respect the current Hint level. Normally:

- state the observed/static verdict distinction;
- identify the first failure at the allowed specificity;
- give the smallest useful counterexample/evidence;
- avoid rewriting the entire solution unless H6 is allowed.

## Persistence

Create/update the Notion Revision row. When a diagnostic conclusion is sufficiently supported, create Error Event rows linked to the Attempt, Revision, and relevant Skill Profile records. Store taxonomy version.

## AC code

AC does not imply the review ends. Verify asymptotic optimality, accidental correctness, unsafe assumptions, and whether a simpler/general solution is educationally important. Then route to `postmortem.md`.
