# ChatGPT Project file additions for v0.2 (apply after merging this PR)

The four original Project attachments are orientation files. This file provides small **append-only** sections; it does not replace existing guidance or reprint source taxonomy. The live ChatGPT Project attachments/Instructions are not changed by updating GitHub. After reviewing the PR, manually replace the Project Instructions with project/PROJECT_INSTRUCTIONS.md and append these sections to the corresponding Project files.

## PROJECT_CONTEXT.md

### Curriculum-driven training

USACO Guide (https://usaco.guide/) is the primary Gold/Platinum course and problem-candidate source. Curriculum facts (module order, prerequisites, external problems, within-module difficulty, stars and solution availability) originate from the official Guide at a pinned upstream SHA. A Guide uniqueId is a curriculum reference only; original OJ Source ID and canonical Tutor T-ID remain distinct.

Learning Goals → baseline → Guide modules → module practice + transfer/retention → blind contest assessment → readiness review. Completion, verified mastery and official promotion are separate statuses.

Notion owns Learning Goals, Module Progress and Assessments; GitHub owns local curriculum mapping and rules, not student records. No problem-specific locked information may be exposed merely because a module or Guide metadata is available.

## DATA_SOURCES.md

### USACO Guide curriculum source

Official site https://usaco.guide/ ; upstream repository https://github.com/cpinitiative/usaco-guide ; license https://usaco.guide/license.

Use only necessary read-only course metadata and original judge links for the student's individual training. Preserve an upstream commit SHA. Do not duplicate the full licensed problem catalog, Guide article/editorial contents or student state into public GitHub/Notion.

### Additional Notion student-state databases

Learning Goals — child database under the private IOI Tutor Notion page
Module Progress — child database under the private IOI Tutor Notion page
Assessments — child database under the private IOI Tutor Notion page

Attempts and Training Queue gained additive Goal/Assessment/exposure properties; older entries retain their actual provenance. Blank Skill Profile means unknown capability, not zero mastery. Each module progress state is scoped by Goal+module key.

## COMMANDS.md

### Curriculum training

Examples:

- 开始 Gold 训练 — establish/reuse Gold Goal, conduct baseline if needed, no auto-promotion.
- Gold 进度 — query actual Goals, module progress and judge-supported skill evidence.
- 今天练 90 分钟 — balance due reviews, curriculum skill gaps and independent transfer.
- 练习 Gold DP — topic-guided module learning; every fresh exercise remains H0.
- Gold 模块考核 — novelty-checked module assessment, do not expose solution tags.
- Gold 综合考核 — unseen timed mixed-topic assessment.
- 进入 Platinum — review Gold readiness; avoid claiming official USACO promotion.
- Platinum 进度 — read real Platinum Goal and current evidence if present.

Use GUIDED_LEARNING for explicitly chosen topic study; use BLIND_ASSESSMENT for unseen tests. H0 refers to tutor hint disclosure; it does not mean the student has never seen the topic.

## USER_GUIDE.md

### Gold → Platinum training

After the GitHub PR is merged and live Project instructions/attachments are updated, start with '开始 Gold 训练'. The Tutor should check any authentic existing Attempts, treat absent Skill Profile as unknown, and plan a small baseline diagnostic rather than assuming current level. Gold and Platinum are internal learning goals; official competition promotion must be recorded as separate external evidence.

For self-study use USACO Guide's module lessons and original OJ links. The Tutor reads Guide metadata to choose exercises but does not reveal editorial details before H permission. Individual topic-guided exercise AC is learning evidence, not proof of blind contest mastery.

Monitor module status (NOT_STARTED / LEARNING / PRACTICING / REVIEWING / COMPLETED) separately from mastery (UNKNOWN / DEVELOPING / PROFICIENT / VERIFIED). Redo continues to create a new locked Attempt. Ask 'Gold 综合考核' when seeking independent readiness confirmation.
