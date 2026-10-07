# Curriculum Checklist — Cross-chat H0-safe state tracking

Use whenever a new problem ID/URL is submitted in **any** IOI Tutor chat,
whether assigned by the Goal Planner or spontaneously provided by the student.

## Authoritative storage

- Private Notion IOI Tutor child database: "USACO Guide 题目清单".
- One row per Guide \`uniqueId\`. Memberships (division/module/relative
  difficulty) are metadata on that row; the \`Completed\` checkbox is **one
  per real problem**. This avoids one AC creating inconsistent statuses in
  multiple Gold/Platinum modules.
- Existing Notion \`Problems\` and \`Sources\` remain canonical for Tutor
  IDs and judge source identities. Catalog entries are *not* canonical
  Problems and do not allocate \`Txxxxxx\` by themselves.
- Data fields: Problem, Guide ID, Original OJ URL, Original Source,
  Divisions, Module Keys, Relative Difficulties, Catalog Role,
  Status, Completed, Completion Evidence, Tutor ID, Latest Attempt ID,
  Last Checked, Catalog SHA, Notes.
- \`UNTRACKED\` means no evidence in IOI Tutor; it never means unsolved,
  weak, or not yet seen by the student.

## Resolve at problem intake

1. Discover the exact child database title within the private IOI Tutor
   Notion root and fetch its live schema. Never hardcode workspace IDs or
   Notion URLs into public GitHub files.
2. Normalize the submitted original OJ URL into a **judge-qualified**
   stable identity, e.g. \`USACO:CPID:993\` or \`CSES:1687\`; consult
   tools/catalog_checklist_policy.py for known URL forms.
3. Prefer exact Guide uniqueId when present; otherwise match a candidate
   from the authoritative Guide catalog by normalized original OJ identity
   and verify its original URL. Do not match only on title or metadata tags.
4. Query the checklist by exact Guide ID. If found, use one existing row.
   If not found, continue the **normal** single-problem workflow (it may be
   outside Guide or a new upstream addition). Do not invent a checklist hit.
5. Independently resolve/create canonical Notion Problem and original Source
   using problem-intake.md. Create a fresh Attempt at H0/SOLUTION_LOCKED.
6. Update the existing checklist row to ATTEMPTING and store Tutor ID,
   Latest Attempt ID and a date, preserving existing \`Completed\` and
   \`Completion Evidence\`. In a Redo, mark REVIEWING instead.
7. A guided or blind test must not show the Guide module, tags or solution
   path contrary to its H0 disclosure gate.

## Update on code, judge verdict, and postmortem

- Student code but no judge verdict → SUBMITTED_UNTESTED, preserving
  Completed/Evidence. Never mark SOLVED on static code analysis alone.
- WA/TLE/MLE/RE/CE/PARTIAL → still not completed on first attempt;
  if previously completed, preserve the old checkbox and mark REVIEWING
  for the current redo. Keep real subtasks in Attempt/Revision.
- Judge AC confirmed by verifiable official result → SOLVED,
  Completed=checked, Completion Evidence=JUDGE_CONFIRMED.
- Student-reported AC without independent judge verification → SOLVED,
  Completed=checked, Completion Evidence=SELF_REPORTED.
- Import from USACO Guide \`Solved\` → Completed=checked with
  Completion Evidence=GUIDE_IMPORT, not automatically Judge-confirmed
  or independent H0 proof.
- Redo and RETENTION keep older successful evidence and allocate another
  Attempt; never erase historical AC even when a later attempt fails.
- If a Notion write fails or the catalog item cannot be matched,
  explicitly report PENDING / NOT_LINKED rather than claiming a checkmark.
- Use the pure transition rules in tools/catalog_checklist_policy.py to
  derive a minimal Notion property patch. Judge evidence is source-of-truth
  for verdicts; the checklist is a summary, not an alternative judge.
- Idempotence: before creating or updating any catalog row, read current
  state and test exact Guide ID. Never duplicate rows on repeated chat
  messages or replayed imports.

## Visibility and anti-spoiler

The student may view the Notion master catalog independently. That is
**not permission** to reveal a problem's hidden technique during an H0
Attempt. In BLIND_ASSESSMENT, display only original OJ statement, neutral
metadata and time constraints; do not expose module-derived selection
rationale or source filenames. In redo, do not read historical Revisions,
root causes, hints or solution notes before new work is submitted.

## Manual user activity

Notion checkbox toggles without real judge evidence count as student-
reported progress, not certified independent AC. Reconcile contradictory
manual states conservatively rather than deleting earlier evidence.
USACO Guide registration is NOT required for this catalog workflow.
