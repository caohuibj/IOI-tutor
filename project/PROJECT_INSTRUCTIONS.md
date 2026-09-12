# IOI Tutor Project Instructions

## Storage contract

- Notion page `IOI Tutor` and its seven databases are the authoritative student-state store.
- `caohuibj/IOI-tutor` is the authoritative tutor knowledge/rules store.
- `caohuibj/OI-training` is the intended private authoritative student-code store once created.
- Chat context is transient and must not substitute for durable records when records exist.

## Initial scope (v0.1)

- Multi-platform canonical problem identity.
- H0-H6 no-spoiler coaching.
- C++17/20/23 and basic Python revision metadata.
- Judge evidence: AC/WA/TLE/MLE/RE/CE/PARTIAL/UNTESTED.
- Root-cause Error Events and Skill mapping.
- Postmortem and rule-based Training Queue.
- Redo/retention and near/far transfer concepts.

## Out of scope for v0.1

- Machine-learned recommendation ranking.
- Exact cross-platform rating conversion.
- Automatic OJ submission.
- Automatic execution of untrusted student code.
- Treating one AC as mastery.

## Development rule

Taxonomy IDs are stable API identifiers. Prefer adding/deprecating IDs over silently changing their meaning. Bump taxonomy/skill/rule versions for semantic changes.
