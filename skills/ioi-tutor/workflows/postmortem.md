# Postmortem

Use when an Attempt reaches AC/full score, is intentionally ended, or the student asks to close/review it.

## Purpose

Convert a transient solving conversation into durable learning evidence and a concrete training prescription.

## Required review

Summarize:

1. final algorithm/model actually used;
2. correctness invariant or proof obligation;
3. actual time and space complexity;
4. revision path (e.g. `WA -> TLE -> AC`) when available;
5. first decisive failure and primary root cause;
6. secondary implementation/debugging issues;
7. positive skill evidence;
8. negative/uncertain skill evidence;
9. independence level (`Hint Max`, hint count, contest/assisted mode);
10. partial-score/subtask strategy when relevant.

## Skill evidence

Do not equate one AC with mastery. Classify evidence where possible as:

- recognition;
- derivation;
- implementation;
- transfer;
- retention.

Update Notion `Skill Profile` conservatively. Mastery and confidence are separate: a high score with little evidence can still have low confidence.

## Training prescription

Generate only items justified by evidence. Prefer a small queue:

- `REPAIR` for a causal weakness;
- `NEAR_TRANSFER` to verify the same skill in a related setting;
- `FAR_TRANSFER` when abstraction transfer is the target;
- `CONTRAST` when discrimination is weak;
- `RETENTION` for spaced redo;
- `STRETCH` only after stable evidence;
- `CONTEST` for partial-score/time-allocation weaknesses.

Link each Training Queue item to the origin Attempt, target Skill, and target Problem if already selected.

## Finalize Attempt

Set final verdict/score, finish time/duration, status `RESOLVED` (or `ABANDONED` when appropriate), and preserve the full revision history. Never overwrite A01 when creating a later redo A02.
