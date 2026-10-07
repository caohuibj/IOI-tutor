#!/usr/bin/env python3
"""Read-only, provenance-pinned USACO Guide curriculum metadata adapter.

Personal-study use only. Does not fetch or store editorials, lesson bodies, code,
student history, or canonical Tutor IDs. See https://usaco.guide/license.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

REPO = "cpinitiative/usaco-guide"
API = "https://api.github.com/repos/" + REPO
RAW = "https://raw.githubusercontent.com/" + REPO
DIVISION_DIRS = {"gold": "4_Gold", "plat": "5_Plat"}
DIVISION_IDS = tuple(DIVISION_DIRS)
SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")
MODULE_PATTERN = re.compile(r"^[A-Za-z0-9_-]+$")
USER_AGENT = "IOI-Tutor-Curriculum-Reader/0.2 (personal study)"


class CatalogError(ValueError):
    """A malformed or inconsistent upstream curriculum snapshot."""


def get_text(url: str) -> str:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def get_json(url: str):
    return json.loads(get_text(url))


def normalize_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        return value[1:-1].replace("''", "'")
    return value


def parse_frontmatter(body: str) -> dict:
    lines = body.splitlines()
    if not lines or lines[0].strip() != "---":
        raise CatalogError("Missing MDX frontmatter")
    try:
        stop = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration as exc:
        raise CatalogError("Unterminated MDX frontmatter") from exc

    fields: dict[str, str] = {}
    prerequisites: list[str] = []
    current = None
    for line in lines[1:stop]:
        match = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*$", line)
        if match:
            current = match.group(1)
            fields[current] = normalize_scalar(match.group(2))
            if current == "prerequisites" and fields[current].startswith("["):
                prerequisites.extend(
                    normalize_scalar(part)
                    for part in fields[current].strip("[]").split(",")
                    if part.strip()
                )
            continue
        if current == "prerequisites":
            item = re.match(r"^\s+-\s+(.+?)\s*$", line)
            if item:
                prerequisites.append(normalize_scalar(item.group(1)))
    if not fields.get("id") or not fields.get("title"):
        raise CatalogError("Module must have id and title")
    if not MODULE_PATTERN.fullmatch(fields["id"]):
        raise CatalogError("Invalid module id: " + fields["id"])
    frequency = fields.get("frequency")
    if frequency:
        try:
            frequency = int(frequency)
        except ValueError as exc:
            raise CatalogError("Invalid module frequency: " + str(frequency)) from exc
    else:
        frequency = None
    return {
        "id": fields["id"],
        "title": fields["title"],
        "prerequisites": prerequisites,
        "frequency": frequency,
    }


def parse_ordering(text: str, division: str) -> list[dict]:
    if division not in DIVISION_DIRS:
        raise CatalogError("Unknown division: " + division)
    start = re.search(r"(?m)^\s{2}" + re.escape(division) + r":\s*\[", text)
    if not start:
        raise CatalogError("Division missing from ordering.ts: " + division)
    rest = text[start.end():]
    next_division = re.search(r"(?m)^\s{2}(general|bronze|silver|gold|plat|adv):\s*\[", rest)
    section = rest[:next_division.start()] if next_division else rest
    category_headers = list(
        re.finditer(r"(?m)^\s*name:\s*(['\"])(.*?)\1\s*,?\s*$", section)
    )
    chapters = []
    seen = set()
    for pos, header in enumerate(category_headers):
        ending = category_headers[pos + 1].start() if pos + 1 < len(category_headers) else len(section)
        body = section[header.end():ending]
        items = re.search(r"\bitems:\s*\[([^\]]*)\]", body, re.DOTALL)
        if not items:
            raise CatalogError("Missing item list in category: " + header.group(2))
        module_ids = re.findall(r"['\"]([^'\"\n]+)['\"]", items.group(1))
        if not module_ids:
            raise CatalogError("Empty item list in category: " + header.group(2))
        for module_id in module_ids:
            if not MODULE_PATTERN.fullmatch(module_id) or module_id in seen:
                raise CatalogError("Duplicate/invalid ordered module: " + module_id)
            seen.add(module_id)
        chapters.append({"name": header.group(2), "module_ids": module_ids})
    if not chapters:
        raise CatalogError("No categories parsed for: " + division)
    return chapters


def extract_memberships(problems_data: dict, module_key: str) -> tuple[list[dict], list[dict]]:
    """Return independent problem identities plus module-relative memberships."""
    if not isinstance(problems_data, dict):
        raise CatalogError("Expected a JSON object of section -> problem list")
    problems = []
    memberships = []
    for section, entries in problems_data.items():
        if section == "MODULE_ID":
            continue
        if not isinstance(entries, list):
            raise CatalogError("Expected list for problems section: " + section)
        for position, item in enumerate(entries):
            if not isinstance(item, dict):
                raise CatalogError("Expected problem object in: " + section)
            unique_id = item.get("uniqueId")
            title, url = item.get("name"), item.get("url")
            if not all(isinstance(x, str) and x.strip() for x in (unique_id, title, url)):
                raise CatalogError("Problem missing stable guide id, title or URL")
            if not url.startswith(("https://", "http://")):
                raise CatalogError("Problem URL is not HTTP(S): " + str(url))
            native_difficulty = item.get("difficulty")
            if not isinstance(native_difficulty, str) or not native_difficulty:
                raise CatalogError("Missing module-relative difficulty for: " + unique_id)
            raw_tags = item.get("tags", [])
            if not isinstance(raw_tags, list) or any(not isinstance(t, str) for t in raw_tags):
                raise CatalogError("Invalid problem tags for: " + unique_id)
            solution = item.get("solutionMetadata") or {}
            if not isinstance(solution, dict):
                raise CatalogError("Invalid solutionMetadata for: " + unique_id)
            problems.append({
                "guide_problem_id": unique_id,
                "title": title,
                "original_oj_url": url,
                "original_source_label": item.get("source"),
            })
            memberships.append({
                "module_key": module_key,
                "guide_problem_id": unique_id,
                "section": section,
                "position": position,
                "relative_difficulty_raw": native_difficulty,
                "is_starred": bool(item.get("isStarred", False)),
                "tags_locked": raw_tags,
                "editorial_kind_locked": solution.get("kind", "unknown"),
                "has_hints_locked": bool(solution.get("hasHints", False)),
            })
    return problems, memberships


class UpstreamReader:
    """Pinned GitHub metadata reader; one REST call per directory, raw files otherwise."""

    def __init__(self, ref: str = "master"):
        if SHA_PATTERN.fullmatch(ref):
            self.sha = ref
        else:
            if not re.fullmatch(r"[A-Za-z0-9._/-]+", ref):
                raise CatalogError("Invalid Git ref")
            result = get_json(API + "/git/ref/heads/" + quote(ref, safe="/"))
            self.sha = result["object"]["sha"]
        if not SHA_PATTERN.fullmatch(self.sha):
            raise CatalogError("GitHub returned an invalid commit SHA")

    def read(self, path: str) -> str:
        return get_text(RAW + "/" + self.sha + "/" + path)

    def list_mdx(self, division: str) -> list[str]:
        directory = "content/" + DIVISION_DIRS[division]
        listing = get_json(API + "/contents/" + directory + "?ref=" + self.sha)
        if not isinstance(listing, list):
            raise CatalogError("Unexpected GitHub directory response: " + directory)
        paths = sorted(
            entry["path"] for entry in listing
            if entry.get("type") == "file" and entry.get("name", "").endswith(".mdx")
        )
        if not paths:
            raise CatalogError("No MDX files in " + directory)
        return paths


def build_catalog(reader: UpstreamReader, divisions: list[str], modules_filter: set[str] | None = None) -> dict:
    ordering_source = reader.read("content/ordering.ts")
    module_rows: list[dict] = []
    problem_index: dict[str, dict] = {}
    memberships: list[dict] = []
    for division in divisions:
        chapters = parse_ordering(ordering_source, division)
        ordered = [(module_id, chapter["name"])
                   for chapter in chapters for module_id in chapter["module_ids"]]
        paths = reader.list_mdx(division)
        with ThreadPoolExecutor(max_workers=8) as pool:
            parsed = list(pool.map(lambda p: (p, parse_frontmatter(reader.read(p))), paths))
        by_id = {}
        for path, meta in parsed:
            if meta["id"] in by_id:
                raise CatalogError("Duplicate upstream module id: " + meta["id"])
            by_id[meta["id"]] = (path, meta)

        for rank, (module_id, category) in enumerate(ordered):
            if module_id not in by_id:
                raise CatalogError("Ordered module missing source file: " + division + ":" + module_id)
            module_key = "USACO_GUIDE:" + division + ":" + module_id
            if modules_filter is not None and division + ":" + module_id not in modules_filter:
                continue
            path, meta = by_id[module_id]
            problems_path = path[:-4] + ".problems.json"
            raw = json.loads(reader.read(problems_path))
            if raw.get("MODULE_ID") != module_id:
                raise CatalogError("MODULE_ID mismatch in: " + problems_path)
            local_problems, local_memberships = extract_memberships(raw, module_key)
            for problem in local_problems:
                old = problem_index.get(problem["guide_problem_id"])
                if old is not None and (
                    old["original_oj_url"].rstrip("/") != problem["original_oj_url"].rstrip("/")
                ):
                    raise CatalogError("Guide ID has inconsistent original URLs: " + problem["guide_problem_id"])
                if old is None:
                    problem_index[problem["guide_problem_id"]] = problem
            memberships.extend(local_memberships)
            module_rows.append({
                "module_key": module_key,
                "division": division,
                "category": category,
                "module_kind": "CONCLUSION" if category.lower() == "conclusion" else "LESSON",
                "rank": rank,
                "guide_module_id": module_id,
                "title": meta["title"],
                "guide_url": "https://usaco.guide/" + division + "/" + module_id,
                "upstream_mdx_path": path,
                "upstream_problem_list_path": problems_path,
                "prerequisite_module_ids": meta["prerequisites"],
                "frequency_raw": meta["frequency"],
                "membership_count": len(local_memberships),
            })
    if modules_filter is not None:
        present = {r["division"] + ":" + r["guide_module_id"] for r in module_rows}
        if modules_filter != present:
            raise CatalogError("Unknown requested modules: " + ", ".join(sorted(modules_filter - present)))

    return {
        "schema_version": "0.2.0",
        "provider": "USACO_GUIDE",
        "source": {
            "repository": REPO,
            "commit_sha": reader.sha,
            "guide_url": "https://usaco.guide/",
            "license_url": "https://usaco.guide/license",
            "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        },
        "semantics": {
            "relative_difficulty": "Relative to module; never convert automatically to D1-D8",
            "tags_and_editorial": "Locked during H0 or blind assessment",
            "canonical_identity": "guide_problem_id is a curriculum reference, not a Tutor T-ID",
        },
        "modules": module_rows,
        "problems": list(problem_index.values()),
        "memberships": memberships,
        "statistics": {
            "modules": len(module_rows),
            "instructional_modules": sum(row["module_kind"] == "LESSON" for row in module_rows),
            "conclusion_modules": sum(row["module_kind"] == "CONCLUSION" for row in module_rows),
            "unique_guide_problem_ids": len(problem_index),
            "module_problem_memberships": len(memberships),
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--division", action="append", choices=DIVISION_IDS,
                        help="Gold or Platinum; repeat to select both (default: both)")
    parser.add_argument("--module", action="append",
                        help="Limit output to division:module-id, e.g. gold:intro-dp")
    parser.add_argument("--ref", default="master",
                        help="Upstream Git ref or 40-character commit SHA")
    parser.add_argument("--output", type=Path,
                        help="Optional local output file; by default writes to stdout")
    args = parser.parse_args(argv)
    filt = set(args.module) if args.module else None
    try:
        if filt:
            for item in filt:
                if ":" not in item or item.split(":", 1)[0] not in DIVISION_DIRS:
                    raise CatalogError("Invalid --module: " + item)
            inferred = [x.split(":", 1)[0] for x in args.module]
        else:
            inferred = list(DIVISION_IDS)
        divisions = list(dict.fromkeys(args.division or inferred))
        if filt and any(x.split(":", 1)[0] not in divisions for x in filt):
            raise CatalogError("--module division not selected by --division")
        catalog = build_catalog(UpstreamReader(args.ref), divisions, filt)
        output = json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(output, encoding="utf-8")
        else:
            sys.stdout.write(output)
        return 0
    except (CatalogError, HTTPError, URLError, json.JSONDecodeError, KeyError) as exc:
        print("Curriculum import failed without persisting partial data: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
