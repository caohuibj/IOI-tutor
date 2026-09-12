# GitHub Code Archive

The private `caohuibj/OI-training` repository is the source of truth for student-submitted code once created and connected.

## Layout

```text
problems/
  T000001/
    A01/
      R01.cpp
      R02.cpp
    A02/
      R01.cpp
```

## Rules

1. Save the student's submitted code exactly; no silent repairs.
2. Allocate a new `Rxx` for every materially new code version. Never overwrite historical revisions.
3. Use commit messages: `[ioi] T000001 A01 R01`, optionally suffixed by an observed verdict after it is known.
4. Record repository, path, commit SHA, and code URL in the Notion Revision.
5. Tutor/reference implementations must not masquerade as student revisions. If explicitly requested at H6, store separately under `problems/Txxxxxx/reference/` only when the student wants it persisted.
6. Redo creates a new `Axx` directory and must not inspect prior code while independent mode is locked.

## Failure handling

If `OI-training` does not exist or is not writable, preserve the code in the current chat for analysis, create no false GitHub pointer, and report that durable code archival is incomplete.
