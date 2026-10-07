# IOI Tutor

A persistent, no-spoiler OI/IOI coaching system for ChatGPT.

## Architecture

- **ChatGPT**: reasoning, diagnosis, coaching, training planning.
- **Notion**: source of truth for student state (Problems, Sources, Attempts, Revisions metadata, Error Events, Skill Profile, Training Queue).
- **This repository**: source of truth for tutor taxonomy, skill graph, schemas, workflows, tests and evals.
- **OI-training repository**: source of truth for submitted code revisions (`problems/Txxxxxx/Axx/Rxx.cpp`).

## Core lifecycle

`problem/source -> SOLUTION_LOCKED -> attempt -> code revision -> judge evidence -> diagnosis -> postmortem -> training queue -> redo/transfer`

## ID rules

- Canonical problem: `T000001`
- Attempt: `T000001-A01`
- Revision: `T000001-A01-R01`
- Error event: `E000001`
- Training item: `TR000001`

## Version

MVP: 0.1.0


## Curriculum-driven training (development v0.2)

Development branch adds a read-only, upstream-SHA-pinned curriculum provider for USACO Guide Gold/Platinum and offline/live pilot tests. Modules, original-judge problems and per-module difficulty are separated. See skills/ioi-tutor/references/USACO_GUIDE_PROVIDER.md and project/NOTION_CURRICULUM_MIGRATION.md.

Current status: read-only pilot adapter and rules; Notion curriculum tables have been created separately, but no Gold/Platinum Goal or end-to-end adaptive readiness has been validated. Existing v0.1 H0, redo and judge evidence workflows remain in force.

Notion schema v0.2 pilot: the three curriculum tables and additive Attempt/Training Queue properties were created on 2026-10-08. Their data and workspace identifiers remain private; the adaptive evidence loop is **not yet E2E verified**.

## Student-requested personal Gold/Platinum checklist (v0.2-dev.2)

The private Notion IOI Tutor workspace now contains one attributed, minimal-metadata "USACO Guide 题目清单" for Gold and Platinum. Full-list and filtered completed/in-progress/review views share the same item status; no USACO Guide login is required. The source index was seeded at upstream SHA 81339eea4b5e43a0a1e26365f8dc8dfaa60f7705.

On each Guide-matched source intake/Revision/Judge event, apply workflows/catalog-checklist.md with tools/catalog_checklist_policy.py. UNTRACKED is not a negative skill assessment; code without verdict is not AC; self-reported AC is not independently judge-confirmed; redo preserves prior completion.

This is **not** a live Guide/online judge integration and is **not yet validated** as a complete cross-chat event loop. The PR remains draft and Project attachments must be synchronized after review. No private Notion IDs or student progress are committed here.
