# Transfer Training

Use when recommending or assigning related practice after a diagnosed skill gap.

## Similarity types

Do not equate “similar problem” with same topic tag. Evaluate:

1. Algorithm similarity — same algorithm/technique.
2. Structural similarity — same invariant, transformation, state sufficiency, monotonicity, contribution view, etc.
3. Training similarity — repairs the same diagnosed weakness.

Training similarity has highest priority for coaching.

## Modes

- `REPAIR`: isolate the weak micro-skill at lower cognitive load.
- `NEAR_TRANSFER`: same target skill in a nearby representation/topic.
- `FAR_TRANSFER`: same abstract skill in a different domain.
- `CONTRAST`: superficially similar problem where a different method is correct.
- `RETENTION`: delayed redo/review.
- `STRETCH`: one difficulty step beyond current demonstrated mastery.
- `CONTEST`: integrate multiple skills under time/score pressure.

## Selection rules

Prefer problems that match the target skill, fit current difficulty, are not too recently attempted, and provide new evidence. Avoid repetitive template drilling when recognition/implementation are already strong but modeling/transfer are weak.

Every recommendation should create or update a Training Queue item with mode, target skill, problem, origin attempt, priority, due date when appropriate, and rationale.
