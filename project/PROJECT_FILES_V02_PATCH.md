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

Use only necessary read-only course metadata and original judge links for the student's individual training. Preserve an upstream commit SHA. Do not publicly republish licensed lesson/editorial contents or Guide datasets. A private, attributed minimal Guide-ID/link/module checklist exists in Notion for individual study; official Guide remains the source of catalog truth.

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


## Checklist additions for all four Project files (v0.2-dev.2)

### PROJECT_CONTEXT.md
One private Notion "USACO Guide 题目清单" index provides all linked Gold/Platinum items and one shared Completed status per Guide uniqueId. The original judge Source and Tutor T ID are separate objects. Checklisting is chat-triggered; it does not read judge or Guide accounts automatically.

### DATA_SOURCES.md
Private Notion database: USACO Guide 题目清单, child of IOI Tutor. Resolve by name at runtime. Its fields include Guide ID, Original OJ URL, Divisions, Module Keys, Relative Difficulties, Status, Completed, Completion Evidence, Tutor ID and Latest Attempt ID. UNTRACKED means no available evidence. Source: https://usaco.guide/; personal use only, CC BY-NC-SA 4.0, see https://usaco.guide/license.

### COMMANDS.md
On every incoming problem URL / platform ID: exact OJ/Guide identity → canonical T Problem → new H0 Attempt → checklist ATTEMPTING if matched. Student code → SUBMITTED_UNTESTED; WA/TLE/PARTIAL → still not newly completed; AC → SOLVED and Completed checkbox, with SELF_REPORTED or JUDGE_CONFIRMED provenance. Repeated Redo retains earlier Completion. Commands: "题目清单", "已完成题目", "正在做", "USACO Guide 进度".

### USER_GUIDE.md
The student does not need a USACO Guide account. The Guide checklist is privately seeded from public upstream course references, and individual ChatGPT chats update status only as submitted to Tutor. Open the database under Notion IOI Tutor to see views 全部题目/已完成题目/正在练习/需要复习. Start a fresh chat per problem as before; no new training Goal is necessary for a simple checklist update. To update without an Attempt, report an existing AC and original OJ reference, and mark the evidence SELF_REPORTED until independently checked.
