# Tests

Planned deterministic tests for schema validity, ID stability, no-spoiler boundaries, redo isolation, and persistence invariants.

Initial priorities:
1. H0 must not reveal H2-H4 technique/pattern tags.
2. Redo must not read prior code/errors before new submission.
3. Error Event must separate root cause from symptom.
4. Revision IDs must be immutable and monotone within an Attempt.
