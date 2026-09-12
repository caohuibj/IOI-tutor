# Training Planner

Use after postmortem or when the student asks what to train next.

## Inputs

Read durable evidence, not chat memory:

- recent Error Events and their root-cause roles;
- Skill Profile mastery/confidence/evidence count/trend;
- recent Attempts, hint levels, time, score, and revision patterns;
- existing Training Queue to avoid repetition;
- Problem taxonomy/difficulty for candidate fit.

## Recommendation principle

Recommend for **skill gap**, not merely shared problem tags.

Distinguish:

1. **Algorithm similarity** — same named algorithm/DS.
2. **Structural similarity** — same hidden invariant/transformation/pattern.
3. **Training similarity** — best task for repairing the same student weakness.

Training similarity has priority.

## Ranking

Use `training-rules.json`. Conceptually rank by:

`skill_gap × relevance × difficulty_fit × spacing × transfer_value × quality - recent_repetition`.

Do not claim a precise ML score in v0.1; this is a rule-based coach.

## Difficulty fit

- REPAIR: usually easier than the triggering problem.
- NEAR_TRANSFER: similar or slightly harder.
- FAR_TRANSFER: moderate difficulty; novelty should come from domain transfer, not raw difficulty.
- STRETCH: one band/meaningful dimension above demonstrated mastery.
- RETENTION: original problem or a close equivalent after spacing.

## Output

Create/update Notion Training Queue entries with Mode, Target Skill, Priority, Due, Origin Attempt, optional target Problem, and concise rationale.

When the user says `训练` or gives a time budget, select from queued items by due date/priority and construct a balanced session rather than generating unrelated recommendations.
