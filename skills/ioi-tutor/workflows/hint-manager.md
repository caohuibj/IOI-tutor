# Hint Manager

Use when the student requests help before ending independent mode.

## Rules

1. Start every new Attempt at H0.
2. Increase `Hint Count` for each substantive hint and set `Hint Max` to the highest level disclosed.
3. Never decrease the recorded maximum hint level within an Attempt.
4. Give the smallest useful hint at the requested/necessary level; do not bundle higher-level information.
5. Prefer diagnosis and counterexamples over repair code until H5/H6.

## Levels

- **H1**: identify broad type of issue (e.g. complexity, state modeling, implementation boundary).
- **H2**: point to the local component/region where the issue occurs.
- **H3**: give a minimal counterexample or failure pattern without telling the fix.
- **H4**: reveal the key invariant, transformation, or algorithmic direction.
- **H5**: give pseudocode or a local repair skeleton.
- **H6**: full explanation/reference implementation allowed; independent attempt is considered ended if the solution is revealed before a valid submission.

## Persistence

Update the active Notion Attempt's `Hint Max` and `Hint Count` after each durable hint disclosure.
