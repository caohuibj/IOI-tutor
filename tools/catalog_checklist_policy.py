#!/usr/bin/env python3
"""Pure checklist state transitions and best-effort stable judge ID parsing.

Does not read student history or perform Notion writes. Notion remains the
source of truth for actual student progress. Original OJ IDs must be verified
before merging with an existing canonical Tutor Problem.
"""
from __future__ import annotations

import re
from urllib.parse import parse_qs, urlparse

ACTIVE = {"UNTRACKED", "ASSIGNED", "ATTEMPTING", "SUBMITTED_UNTESTED",
          "SOLVED", "REVIEWING", "ABANDONED"}
EVIDENCE = {"NONE", "SELF_REPORTED", "JUDGE_CONFIRMED", "GUIDE_IMPORT"}


def normalize_original_oj(url: str) -> str | None:
    """Return a stable judge-qualified lookup token, or None if uncertain."""
    u = urlparse(url.strip())
    host = (u.hostname or "").lower().removeprefix("www.")
    path = u.path.strip("/")
    query = parse_qs(u.query)
    if host == "usaco.org":
        cpid = query.get("cpid", [""])[0]
        return "USACO:CPID:" + cpid if cpid.isdigit() else None
    if host == "cses.fi":
        m = re.match(r"problemset/task/(\d+)(?:/|$)", path)
        return "CSES:" + m.group(1) if m else None
    if host == "codeforces.com":
        m = re.match(r"(?:contest/|problemset/problem/)(\d+)/(?:problem/)?([A-Za-z]\d?)$", path)
        return "CF:" + m.group(1) + ":" + m.group(2).upper() if m else None
    if host == "atcoder.jp":
        m = re.match(r"contests/[^/]+/tasks/([a-z0-9_]+)$", path, re.I)
        return "AT:" + m.group(1).lower() if m else None
    if host == "dmoj.ca":
        m = re.match(r"problem/([a-z0-9_-]+)$", path, re.I)
        return "DMOJ:" + m.group(1).lower() if m else None
    if host == "oj.uz":
        m = re.match(r"problem/view/([a-z0-9_]+)$", path, re.I)
        return "OJUZ:" + m.group(1).lower() if m else None
    return None


def normalize_checklist_state(state: dict | None) -> dict:
    """Missing progress means untracked, not a negative ability judgment."""
    state = state or {}
    status = state.get("Status") or "UNTRACKED"
    if status not in ACTIVE:
        raise ValueError("Invalid Status: " + str(status))
    evidence = state.get("Completion Evidence") or "NONE"
    if evidence not in EVIDENCE:
        raise ValueError("Invalid Completion Evidence: " + str(evidence))
    completed = state.get("Completed", False)
    if completed in ("__YES__", True):
        completed = True
    elif completed in ("__NO__", False, None):
        completed = False
    else:
        raise ValueError("Invalid Completed flag")
    return {"Status": status, "Completed": completed, "Completion Evidence": evidence}


def advance_checklist(
    prior: dict | None,
    event: str,
    *,
    verdict: str | None = None,
    judge_verified: bool = False,
    guide_status: str | None = None,
) -> dict:
    """Calculate a minimal Notion patch. Preserve completed evidence on redo."""
    s = normalize_checklist_state(prior)
    completed, evidence = s["Completed"], s["Completion Evidence"]
    if event == "ASSIGN":
        next_status = "ATTEMPTING"
    elif event == "CODE_SUBMITTED":
        next_status = "SUBMITTED_UNTESTED"
    elif event == "REDO":
        next_status = "REVIEWING"
    elif event == "ABANDON":
        next_status = "ABANDONED"
    elif event == "MARK_REVIEW":
        next_status = "REVIEWING"
    elif event == "JUDGE_RESULT":
        if not verdict:
            raise ValueError("JUDGE_RESULT requires actual verdict")
        verdict = verdict.strip().upper()
        if verdict == "AC":
            completed = True
            new_evidence = "JUDGE_CONFIRMED" if judge_verified else "SELF_REPORTED"
            rank = {"NONE": 0, "GUIDE_IMPORT": 1, "SELF_REPORTED": 2, "JUDGE_CONFIRMED": 3}
            if rank[new_evidence] > rank[evidence]:
                evidence = new_evidence
            next_status = "SOLVED"
        elif verdict in {"WA", "TLE", "MLE", "RE", "CE", "PARTIAL", "UNSOLVED", "UNTESTED"}:
            next_status = "REVIEWING" if completed else "ATTEMPTING"
        else:
            raise ValueError("Unrecognized OJ verdict: " + verdict)
    elif event == "GUIDE_IMPORT":
        if guide_status is None:
            raise ValueError("GUIDE_IMPORT requires guide_status")
        translation = {
            "Not Attempted": "UNTRACKED",
            "Solving": "ATTEMPTING",
            "Solved": "SOLVED",
            "Reviewing": "REVIEWING",
            "Skipped": "ABANDONED",
            "Ignored": "UNTRACKED",
        }
        if guide_status not in translation:
            raise ValueError("Unrecognized Guide progress status")
        next_status = translation[guide_status]
        if guide_status in {"Solved", "Reviewing"}:
            completed = True
            if evidence == "NONE":
                evidence = "GUIDE_IMPORT"
    else:
        raise ValueError("Unsupported checklist event: " + event)
    return {
        "Status": next_status,
        "Completed": "__YES__" if completed else "__NO__",
        "Completion Evidence": evidence,
    }


def main() -> None:
    import argparse
    import json
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--original-url")
    p.add_argument("--event", choices=["ASSIGN", "CODE_SUBMITTED", "REDO",
                                       "ABANDON", "MARK_REVIEW", "JUDGE_RESULT",
                                       "GUIDE_IMPORT"])
    p.add_argument("--prior", default="{}", help="JSON state dictionary (do not put secrets here)")
    p.add_argument("--verdict")
    p.add_argument("--judge-verified", action="store_true")
    p.add_argument("--guide-status")
    a = p.parse_args()
    if a.original_url:
        print(normalize_original_oj(a.original_url))
    if a.event:
        print(json.dumps(advance_checklist(json.loads(a.prior), a.event,
                      verdict=a.verdict, judge_verified=a.judge_verified,
                      guide_status=a.guide_status), ensure_ascii=False))


if __name__ == "__main__":
    main()
