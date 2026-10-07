# Code Intake

Use when the student submits code for the active Attempt.

1. Resolve the active Attempt from Notion.
2. Allocate the next Revision ID: `<attempt_id>-Rxx`.
3. Preserve the submitted code exactly; never overwrite an older Revision.
4. When `OI-training` is available, save to `problems/<problem_id>/Axx/Rxx.<ext>` and record repo, path, commit SHA and code URL in Notion.
5. Until real judge evidence exists, set Judge Result to `UNTESTED`.
6. Continue to `code-review.md`.

Redo rule: do not read old Attempt code or diagnosis before reviewing the new independent submission.

Tutor-written reference code is not a student Revision and must be stored separately if archived.

## Guide checklist on submission

If the canonical Problem matches one of the private Guide checklist entries, persist SUBMITTED_UNTESTED after successful Revision intake. Preserve a prior Completed checkbox during Redo/revision. Never check Completed from code review alone or assume an untested submission was accepted. See catalog-checklist.md.
