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
