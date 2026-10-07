"""Tests for checklist status transitions, redo isolation and OJ matching."""
import importlib.util
import pathlib
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[2] / "tools" / "catalog_checklist_policy.py"
spec = importlib.util.spec_from_file_location("catalog_checklist_policy", SCRIPT)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class ChecklistTests(unittest.TestCase):
    def test_missing_evidence_is_untracked(self):
        self.assertEqual(p.normalize_checklist_state({})["Status"], "UNTRACKED")

    def test_assign_is_not_completion(self):
        self.assertEqual(p.advance_checklist(None, "ASSIGN"), {
            "Status": "ATTEMPTING", "Completed": "__NO__", "Completion Evidence": "NONE"})

    def test_code_submission_does_not_earn_ac(self):
        result = p.advance_checklist(None, "CODE_SUBMITTED")
        self.assertEqual(result["Status"], "SUBMITTED_UNTESTED")
        self.assertEqual(result["Completed"], "__NO__")

    def test_self_report_ac_is_not_judge_verified(self):
        r = p.advance_checklist(None, "JUDGE_RESULT", verdict="AC")
        self.assertEqual(r["Completed"], "__YES__")
        self.assertEqual(r["Completion Evidence"], "SELF_REPORTED")

    def test_judge_confirmed_ac(self):
        r = p.advance_checklist(None, "JUDGE_RESULT", verdict="AC", judge_verified=True)
        self.assertEqual(r["Completion Evidence"], "JUDGE_CONFIRMED")

    def test_previous_ac_survives_redo_and_wa(self):
        solved = p.advance_checklist(None, "JUDGE_RESULT", verdict="AC")
        redo = p.advance_checklist(solved, "REDO")
        bad = p.advance_checklist(redo, "JUDGE_RESULT", verdict="WA")
        self.assertEqual(bad["Status"], "REVIEWING")
        self.assertEqual(bad["Completed"], "__YES__")
        self.assertEqual(bad["Completion Evidence"], "SELF_REPORTED")

    def test_partial_is_not_complete(self):
        r = p.advance_checklist(None, "JUDGE_RESULT", verdict="PARTIAL")
        self.assertEqual(r["Completed"], "__NO__")

    def test_guide_import_not_equivalent_to_judge(self):
        r = p.advance_checklist(None, "GUIDE_IMPORT", guide_status="Solved")
        self.assertEqual(r["Completed"], "__YES__")
        self.assertEqual(r["Completion Evidence"], "GUIDE_IMPORT")

    def test_unrecognized_verdict_fails_closed(self):
        with self.assertRaises(ValueError):
            p.advance_checklist(None, "JUDGE_RESULT", verdict="???")

    def test_usaco_url_normalization(self):
        a = "http://www.usaco.org/index.php?page=viewproblem2&cpid=993"
        b = "https://usaco.org/index.php?cpid=993&page=viewproblem2"
        self.assertEqual(p.normalize_original_oj(a), p.normalize_original_oj(b))
        self.assertEqual(p.normalize_original_oj(a), "USACO:CPID:993")

    def test_other_judges(self):
        pairs = [
            ("https://cses.fi/problemset/task/1687", "CSES:1687"),
            ("https://codeforces.com/contest/1418/problem/C", "CF:1418:C"),
            ("https://codeforces.com/problemset/problem/1418/C", "CF:1418:C"),
            ("https://atcoder.jp/contests/dp/tasks/dp_a", "AT:dp_a"),
            ("https://dmoj.ca/problem/ioi04p4", "DMOJ:ioi04p4"),
            ("https://oj.uz/problem/view/BOI19_valley", "OJUZ:boi19_valley"),
        ]
        for link, expected in pairs:
            with self.subTest(url=link):
                self.assertEqual(p.normalize_original_oj(link), expected)

    def test_never_fuzzy_match_other_origins(self):
        self.assertIsNone(p.normalize_original_oj("https://unknown.example/problem/993"))


if __name__ == "__main__":
    unittest.main()
