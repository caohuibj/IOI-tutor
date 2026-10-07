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
