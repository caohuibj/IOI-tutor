# Judge Review

Use when the student provides OJ feedback for an existing Revision.

## Evidence policy

- Treat AC/WA/TLE/MLE/RE/CE/PARTIAL and score/subtask results as observed evidence only when supplied by the judge/user.
- Never convert static analysis into a fake judge verdict.
- Preserve score and subtask information when available.

## Process

1. Resolve the current Revision.
2. Update its Judge Result, score, time and memory evidence.
3. Reconcile judge evidence with the current code review.
4. Identify the first decisive failure and distinguish symptom from root cause.
5. Create/update Error Events only when the diagnosis is supported; include confidence.
6. Respect the current hint ceiling when explaining the diagnosis.
7. If AC or the Attempt ends, continue to `postmortem.md`; otherwise remain in the same Attempt and wait for the next student Revision.

Partial scoring is meaningful evidence. Diagnose which subtask/constraint transition separates the current solution from higher-scoring solutions when that can be inferred safely.
