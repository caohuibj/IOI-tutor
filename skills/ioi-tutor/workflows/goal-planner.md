# Goal Planner — Gold → Platinum

Use for requests such as 开始 Gold 训练, Gold 进度, 进入 Platinum, and target-oriented training.

## State and sources

- Notion Learning Goals (once provisioned) is authoritative for active target and stage; it is not a copy of Guide's module catalog.
- Module Progress holds one record per Goal + module key, with curriculum commit provenance.
- The existing Skill Profile and Attempts provide capability evidence; no Skill Profile entries is UNKNOWN, never a proof of low or high mastery.
- The Guide provider supplies curriculum structure/relative difficulty only.
- Existing Training Queue remains the unit of prescribed work.

## Procedure

1. Query Notion Goals for active/planned USACO_GUIDE target. Reuse an existing Goal instead of creating another for the same active target.
2. If starting Gold, run baseline-assessment.md before assigning long stretches of curriculum practice; Silver/Bronze prerequisites are eligible if required.
3. If starting Platinum, first review Gold readiness. Allow conditional dual-track study, but do not label Gold officially achieved.
4. At each planning cycle, compute uncovered prerequisites and evidence gaps from actual completed Attempts plus Module Progress.
5. Select a small number of actions: due RETENTION, targeted REPAIR, curriculum progression, independent TRANSFER, or CONTEST. Do not fill Training Queue with all Guide problems.
6. Route selected work to existing problem-intake.md and H0/SOLUTION_LOCKED.
7. Update module progress and mastery only after evidence-bearing postmortem. Course completion, verified mastery and official contest promotion are three distinct claims.
8. When a milestone is requested, route to division-assessment.md.

## Internal states

Learning Goal stages: BASELINE → PREREQUISITES → MODULE_PRACTICE → CONTEST_READINESS → ASSESSMENT → COMPLETE.

Goal status: PLANNED, ACTIVE, PAUSED, COMPLETED.
Platinum does not automatically unlock from a raw question count. All thresholds in references/progression-rules.json are provisional *Tutor* heuristics.

## Compatibility

If Learning Goals, Module Progress or Assessments do not exist yet, identify the missing migration explicitly. Existing single-problem and no-spoiler workflows must continue working without them. Do not fabricate Goal rows, baseline scores or missing student evidence.
