# Problem Retrieval

Use for old-problem lookup, source lookup, history questions, and requests such as “最近我 DP 哪里最弱”.

## Retrieval order

1. Query Notion durable state first; chat history is not authoritative.
2. Resolve exact identifiers before fuzzy matching: Tutor ID -> Source ID -> platform/external ID -> normalized title.
3. For performance questions, join conceptually across Attempts, Error Events, Skill Profile and Training Queue.
4. Return evidence counts and confidence where relevant; do not overstate mastery from one or two Attempts.
5. If the requested item is a code Revision, use its recorded GitHub repo/path/commit SHA.

## Redo privacy

If the user is starting a redo, retrieval may identify the Problem and neutral metadata, but must not expose previous code, root causes, key insights, solution tags or hint history. Route to `redo.md`.

## Training retrieval

When selecting practice, prefer unresolved/high-priority Training Queue items before inventing new recommendations. Use skill gap, spacing and transfer value, not only same-topic tags.
