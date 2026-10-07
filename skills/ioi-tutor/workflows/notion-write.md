# Notion Persistence

Notion is the source of truth for student state.

## Workspace discovery

Locate the private root page titled `IOI Tutor`, then use its child databases:

- `Problems`
- `Sources`
- `Attempts`
- `Revisions`
- `Error Events`
- `Skill Profile`
- `Training Queue`

Fetch database schemas before writes; use exact property names and relations.

## Identity allocation

- Problem ID: next `Txxxxxx` based on existing canonical Problems; never reuse an ID.
- Attempt ID: `<problem_id>-A<attempt_no:02d>`.
- Revision ID: `<attempt_id>-R<revision_no:02d>`.
- Error Event: next `E000001` style ID.
- Training Item: next `TR000001` style ID.

Allocation must query durable records; do not infer the next number from chat memory.

## Write boundaries

### Problem intake
Create/reuse Problem and Source; create active Attempt.

### Code revision
Create Revision metadata only after the student's code exists. Store GitHub repo/path/commit SHA when archived; never paste full code into Notion as the authoritative copy.

### Diagnosis
Create Error Events only when supported by concrete evidence; link Attempt, optional Revision, and Skill. Preserve taxonomy version.

### Postmortem
Finalize Attempt, update Skill Profile conservatively, and create Training Queue items.

## Consistency

- GitHub commit SHA is the immutable pointer for a stored revision.
- If GitHub archival fails, keep the Notion revision metadata explicit about the missing code pointer; do not claim persistence succeeded.
- Never create a second canonical Problem for redo.
- Never store taxonomy definitions in Notion; store stable IDs/version only.


## Curriculum-state extension (v0.2 pilot)

Once verified present, Learning Goals, Module Progress and Assessments are additional Notion-owned student-state databases. They MUST NOT be replicated into GitHub metadata snapshots. Always fetch live schemas before writes; if absent, follow project/NOTION_CURRICULUM_MIGRATION.md as a separate non-destructive migration task rather than inventing tables. Assign Gxxxxxx, MPxxxxxx and ASxxxxxx IDs by querying durable records, not chat memory. A module progress row has uniqueness key (Goal, Guide Module Key); a module in multiple curricula does not imply multiple student identities or duplicate Problems.

## Guide checklist database (private, personal-study source index)

The IOI Tutor root has a child database titled "USACO Guide 题目清单". Resolve this database by title from the authenticated private workspace, not public/hard-coded IDs. It stores 1 row per upstream uniqueId and a summary of student's Status, Completed and Completion Evidence. It is a *private personal-use index*, not an authoritative copy of Guide's content; Guide original OJ/source metadata remains upstream authoritative.

Never allocate a canonical T-ID simply because an item appears in this catalog. On every relevant Attempt/Revision/Judge action update the matching row according to workflows/catalog-checklist.md. Preserve underlying immutable revision evidence; do not write Guide lesson/editorial content. Idempotent lookup by exact Guide ID and normalized original OJ identity is required before any checkmark mutation. Do not convert UNTRACKED to "has never solved".
