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


## Curriculum-goal extension (v0.2 pilot)

For a Gold/Platinum target, invoke goal-planner.md before ordinary Training Planner ranking. Read Learning Goals, Module Progress and assessment evidence when the new Notion tables exist. The curriculum provider supplies candidate modules/problems and upstream prerequisites; Tutor Skill Profile supplies student-specific mastery estimates. Neither source may substitute for the other.

When Skill Profile is empty or novelty/exposure data are unknown, report UNKNOWN and begin with a small diagnostic task instead of declaring readiness or treating zero as failure. Avoid inserting the entire Guide question list into Training Queue: select a few justified tasks only. Preserve the v0.1 ranking factors and modes, adding goal distance, prerequisite readiness and module verification gaps as explicit ranking inputs.

Never use module/topic labels to leak the intended algorithm in BLIND_ASSESSMENT. Course completion, verified transfer and official USACO qualification are separate states.
