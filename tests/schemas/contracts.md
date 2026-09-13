# Schema Contracts

These are invariant checks for durable records.

- `problem_id` matches `^T\d{6}$`.
- `attempt_id` is `<problem_id>-Axx` and attempt numbers increase within one canonical Problem.
- `revision_id` is `<attempt_id>-Rxx`; student revisions are immutable evidence.
- A Revision without real OJ evidence uses `UNTESTED` rather than an inferred verdict.
- Saved GitHub revisions must record repository, path, and immutable commit SHA.
- Error Events separate `ROOT_CAUSE`, `SECONDARY`, and `SYMPTOM` roles.
- Every Error Code must exist in the referenced error-taxonomy version.
- Every related Skill ID must exist in the referenced skill-graph version.
- Training items use one of `REPAIR`, `NEAR_TRANSFER`, `FAR_TRANSFER`, `CONTRAST`, `RETENTION`, `STRETCH`, `CONTEST`.
- Notion owns student state; GitHub taxonomy/workflow files must not contain a second mutable student profile or training queue.
