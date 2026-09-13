# Phase 2 — Operational Tutor

## Goal

Make the v0.1 architecture usable for daily training before adding advanced mastery estimation or recommendation models.

## Current durable boundaries

- Notion: Problems, Sources, Attempts, Revisions metadata, Error Events, Skill Profile, Training Queue.
- `caohuibj/IOI-tutor`: taxonomy, skill graph, schemas, workflows, tests and evals.
- `caohuibj/OI-training`: student code revisions. This repository must exist and be connected before code archival is enabled.

## Daily Notion views

- Problems: `Active Problems`.
- Attempts: `Recent Attempts`, `Active Attempts`.
- Skill Profile: `Weak Skills`.
- Training Queue: `Queued by Due`, `Retention Queue`.

The connector view DSL does not currently create a durable relative-date filter such as `today`. Therefore the tutor must compute `today/overdue` dynamically when the user asks for training, using the current local date and a data-source query. Do not hard-code the current date into a permanent view.

## E2E readiness checklist

1. `OI-training` exists and is private.
2. Initialize `README.md`, `problems/.gitkeep`, `templates/cpp20.cpp`, `templates/stress-test.cpp`.
3. Pick a real source problem.
4. Run `source -> canonical Problem -> A01 -> H0`.
5. Receive student code and archive exact `R01` with commit SHA.
6. Create Notion Revision metadata with `UNTESTED` until judge evidence arrives.
7. Add real OJ verdict/score; diagnose first failure and root cause.
8. Create Error Events and update skill evidence.
9. On resolution, run Postmortem and create Training Queue items.
10. Verify redo creates A02 and does not read A01 history before the new submission.

## Phase 2 exclusions

Do not yet implement complex Elo/IRT/Bayesian mastery, bulk platform crawlers, automatic submission to online judges, or large-scale similarity embeddings. Validate the data lifecycle first with real training attempts.
