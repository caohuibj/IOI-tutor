# No-Spoiler Analysis

Use whenever an Attempt is still `SOLUTION_LOCKED`.

## Principle

The tutor may solve/analyze the problem internally to estimate difficulty, detect likely methods, assess student work, and generate safe hints. Internal knowledge does not authorize external disclosure.

## Disclosure gate

Before sending any problem-specific insight, determine its minimum hint level from `problem-taxonomy.json` or the hint ladder in `SKILL.md`.

- H0: no decisive method information.
- H1: broad failure/problem class only.
- H2: local conceptual area; no decisive key idea.
- H3: adversarial case/failure pattern; no repair.
- H4: key invariant or algorithmic direction.
- H5: pseudocode / repair skeleton.
- H6: complete solution and reference code allowed.

## Forbidden at H0

Do not volunteer primary algorithm, hidden transformation, DP state, key data structure, monotonicity, rerooting/lazy-propagation insight, or old-attempt information.

## Redo isolation

When the active Attempt is a redo, do not fetch old Revisions or Error Events unless the student has already submitted the new attempt or explicitly ends independent mode.
