"""Offline, source-independent tests for the USACO Guide metadata adapter."""
import importlib.util
import pathlib
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[2] / "tools" / "usaco_guide_catalog.py"
spec = importlib.util.spec_from_file_location("usaco_guide_catalog", SCRIPT)
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)

ORDERING = """
const MODULE_ORDERING = {
  gold: [
    {
      name: 'Dynamic Programming',
      description: 'Several concepts',
      items: ['intro-dp'],
    },
  ],
  plat: [
    {
      name: 'Trees',
      items: ['binary-jump'],
    },
  ],
  adv: [],
};
"""
GOLD_MDX = """---
id: intro-dp
title: 'Introduction to DP'
prerequisites:
  - complete-rec
  - modular
frequency: 4
---
Full lesson material is intentionally not copied here.
"""
PLAT_MDX = """---
id: binary-jump
title: Binary Jumping
prerequisites:
frequency: 3
---
Lesson omitted.
"""
GOLD_JSON = {
    "MODULE_ID": "intro-dp",
    "focus": [{
        "uniqueId": "usaco-993", "name": "Example A",
        "url": "https://usaco.org/index.php?page=viewproblem2&cpid=993",
        "source": "Gold", "difficulty": "Hard", "isStarred": True,
        "tags": ["DP"], "solutionMetadata": {"kind": "internal", "hasHints": True},
    }]
}
PLAT_JSON = {
    "MODULE_ID": "binary-jump",
    "sample": [{
        "uniqueId": "usaco-993", "name": "Example A",
        "url": "https://usaco.org/index.php?page=viewproblem2&cpid=993",
        "source": "Gold", "difficulty": "Easy", "isStarred": False,
        "tags": ["Binary Jumping"], "solutionMetadata": {"kind": "USACO"},
    }]
}


class FakeReader:
    sha = "a" * 40

    def __init__(self):
        import json
        self.files = {
            "content/ordering.ts": ORDERING,
            "content/4_Gold/Intro_DP.mdx": GOLD_MDX,
            "content/4_Gold/Intro_DP.problems.json": json.dumps(GOLD_JSON),
            "content/5_Plat/Binary_Jump.mdx": PLAT_MDX,
            "content/5_Plat/Binary_Jump.problems.json": json.dumps(PLAT_JSON),
        }

    def read(self, path):
        return self.files[path]

    def list_mdx(self, division):
        folder = catalog.DIVISION_DIRS[division]
        return sorted(p for p in self.files if p.startswith("content/" + folder) and p.endswith(".mdx"))


class ParserTests(unittest.TestCase):
    def test_ordering_preserves_division_and_categories(self):
        self.assertEqual(catalog.parse_ordering(ORDERING, "gold"),
                         [{"name": "Dynamic Programming", "module_ids": ["intro-dp"]}])
        self.assertEqual(catalog.parse_ordering(ORDERING, "plat")[0]["module_ids"],
                         ["binary-jump"])

    def test_frontmatter_preserves_prerequisites(self):
        result = catalog.parse_frontmatter(GOLD_MDX)
        self.assertEqual(result["id"], "intro-dp")
        self.assertEqual(result["prerequisites"], ["complete-rec", "modular"])
        self.assertEqual(result["frequency"], 4)

    def test_frontmatter_rejects_missing_id(self):
        with self.assertRaises(catalog.CatalogError):
            catalog.parse_frontmatter("---\ntitle: Some Module\n---")

    def test_catalog_separates_problem_and_module_membership(self):
        result = catalog.build_catalog(FakeReader(), ["gold", "plat"])
        self.assertEqual(result["statistics"], {
            "modules": 2,
            "instructional_modules": 2,
            "conclusion_modules": 0,
            "unique_guide_problem_ids": 1,
            "module_problem_memberships": 2,
        })
        self.assertEqual(result["problems"][0]["guide_problem_id"], "usaco-993")
        self.assertNotIn("problem_id", result["problems"][0])
        self.assertEqual([x["relative_difficulty_raw"] for x in result["memberships"]],
                         ["Hard", "Easy"])
        self.assertEqual([x["is_starred"] for x in result["memberships"]],
                         [True, False])
        self.assertEqual(result["modules"][0]["prerequisite_module_ids"],
                         ["complete-rec", "modular"])
        self.assertEqual(result["source"]["commit_sha"], "a" * 40)
        self.assertEqual(result["modules"][0]["module_kind"], "LESSON")

    def test_catalog_accepts_selected_module(self):
        result = catalog.build_catalog(FakeReader(), ["gold", "plat"],
                                       {"plat:binary-jump"})
        self.assertEqual(result["statistics"]["modules"], 1)
        self.assertEqual(result["modules"][0]["guide_module_id"], "binary-jump")

    def test_catalog_rejects_unknown_module(self):
        with self.assertRaises(catalog.CatalogError):
            catalog.build_catalog(FakeReader(), ["gold"], {"gold:does-not-exist"})

    def test_catalog_rejects_inconsistent_upstream_identity(self):
        reader = FakeReader()
        import json
        changed = dict(PLAT_JSON)
        changed["sample"] = [dict(PLAT_JSON["sample"][0], url="https://another.example/problem")]
        reader.files["content/5_Plat/Binary_Jump.problems.json"] = json.dumps(changed)
        with self.assertRaisesRegex(catalog.CatalogError, "inconsistent original URLs"):
            catalog.build_catalog(reader, ["gold", "plat"])

    def test_catalog_rejects_mismatched_module_id(self):
        reader = FakeReader()
        reader.files["content/4_Gold/Intro_DP.problems.json"] = '{"MODULE_ID":"wrong"}'
        with self.assertRaisesRegex(catalog.CatalogError, "MODULE_ID mismatch"):
            catalog.build_catalog(reader, ["gold"])


if __name__ == "__main__":
    unittest.main()
