# Redo

Use when the student asks to redo an existing Problem.

## Hard lock

Redo creates a new independent Attempt for the same canonical Problem and re-locks all prior solution information.

Before the new submission, do not read or expose:

- previous student code;
- previous root causes or Error Events;
- previous key insights or solution notes;
- previous hint history;
- technique/pattern tags above the allowed spoiler level.

Neutral metadata such as statement/source, global difficulty and task constraints may be used.

## Process

1. Resolve the canonical Problem from Notion.
2. Allocate the next Attempt number under the same Problem.
3. Create `<problem_id>-Axx` with `Independent=true`, `Hint Max=H0`, `Hint Count=0`, `Status=ATTEMPTING`.
4. Enter `SOLUTION_LOCKED`.
5. Review the new work as a fresh Attempt.
6. Only after resolution/postmortem may the Tutor compare A01/A02/etc. for time, hints, submissions, score, root-cause recurrence and transfer/retention evidence.

A redo must never create a duplicate canonical Problem.
