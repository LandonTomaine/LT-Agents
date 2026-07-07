#!/usr/bin/env python3
"""Scaffold approved repo backbone files with safe defaults."""

from __future__ import annotations

import argparse
from fnmatch import fnmatch
from pathlib import Path


TRACKING_DIR = Path(".agents") / "tmp" / "bootstrap-repo-standards"
PLACEHOLDER = "TODO: Fill this in after the repo owner confirms the decisions needed for this repo."


def placeholder(title: str) -> str:
    return f"# {title}\n\n{PLACEHOLDER}\n"


TEMPLATES: dict[str, dict[str, str]] = {
    "claude-entrypoint": {
        "CLAUDE.md": """# Claude Guide

Use [AGENTS.md](AGENTS.md) as the agent entrypoint for this repository.
""",
    },
    "agent": {
        "AGENTS.md": """# Agent Guide

See [agent-rules/README.md](agent-rules/README.md) for the agent entrypoint, repo-local skill inventory, and routes to codebase guidance.

Use just enough context:

- Start with `agent-rules/README.md`.
- Read the always-load file listed there before acting.
- Load only the docs needed for the current task.
- Do not bulk-read the repo when a focused doc will do.
""",
        "agent-rules/README.md": """# Agent Rules

This folder is the agent routing layer for the repository.

Goal: load what is needed for the current task, then stop.

Most durable guidance belongs in shared docs under `docs/`. This folder is for agent behavior, routing, ambiguity handling, and environment constraints.

## Always Load

- [core.md](core.md)

## Principles

- Use this index for routing, not as a checklist.
- Do not read every linked file.
- Load the smallest set that can answer the current task.

## Routes

- Shell or command behavior: [shell.md](shell.md)
- Maintaining this guidance system: [maintaining.md](maintaining.md)
- Communication style: [communication-style.md](communication-style.md)
- Task lenses: [working-modes.md](working-modes.md)
- Add codebase doc routes only after the referenced docs exist or are approved in the manifest.

## Repo-Local Skills

- Add skill routes only after the referenced skills exist or are approved in the manifest.

## Workflow

- After loading the minimum relevant docs, inspect the specific code and tests you are about to change.
- Treat docs as guidance and local code plus executable tests as the source of truth when they disagree.
- If the next action is clear, act instead of reading more docs.
""",
        "agent-rules/core.md": """# Core Rules

- Use just enough context.
- Ask when ambiguity affects correctness, scope, data, architecture, or user-visible behavior.
- Prefer shared human docs over agent-only rules.
- Keep agent-read files terse.
- Do not present assumptions as facts.
- Ask before destructive actions.
""",
        "agent-rules/communication-style.md": """# Communication Style

- Lead with the answer or next action.
- Keep updates short.
- State uncertainty plainly.
""",
        "agent-rules/shell.md": """# Shell Rules

- Prefer focused commands.
- Prefer `rg` for search.
- Ask before destructive actions.
""",
        "agent-rules/maintaining.md": """# Maintaining Agent Rules

- Keep `AGENTS.md` tiny.
- Keep `agent-rules/` for routing and agent behavior.
- Keep durable engineering/product guidance in `docs/`.
- Update routes when adding or moving docs.
- Keep indexes as routing tables, not hidden standards manuals.
- Remove or consolidate duplicated guidance instead of repeating it.
""",
        "agent-rules/working-modes.md": """# Working Modes

Use task lenses only when useful:

- Product: scope, users, workflows, acceptance.
- Architecture: boundaries, ownership, risks.
- Implementation: correctness, tests, local patterns.
- Review: bugs, regressions, missing validation.
""",
    },
    "docs": {
        "docs/README.md": """# Documentation

Shared documentation for humans and agents.

Use the smallest doc that fits the current task. Do not treat this index as a required reading list.

## Current Docs

- [architecture/overview.md](architecture/overview.md)
- [development/README.md](development/README.md)

## Maintenance

- Keep each doc self-contained.
- Split files when a section can be loaded independently.
- Keep docs DRY and brief.
- Prefer shared docs over agent-only docs when the guidance helps humans too.
""",
        "docs/architecture/overview.md": placeholder("Architecture Overview"),
        "docs/development/README.md": """# Development Docs

Shared engineering documentation for humans and agents.

Load only the docs needed for the current task.

## Current Docs

- [local-setup.md](local-setup.md): prerequisites, install, config, and local run commands.
- [deployment.md](deployment.md): deploy, release, or publish process.
- [tooling.md](tooling.md): commands, hooks, lint, format, build, test.
- [testing/strategy.md](testing/strategy.md): test layers and validation expectations.
- [validation.md](validation.md): local and deployed validation expectations.
- [workflow.md](workflow.md): development flow.

## Boundaries

- Keep cross-layer architecture rules in [../architecture/overview.md](../architecture/overview.md).
- Keep coding standards, tooling, workflow, testing, and common commands here.
- Do not duplicate product context here unless a short engineering-specific note is required.
""",
        "docs/development/local-setup.md": placeholder("Local Setup"),
        "docs/development/deployment.md": placeholder("Deployment"),
        "docs/development/tooling.md": placeholder("Tooling"),
        "docs/development/validation.md": placeholder("Validation"),
        "docs/development/workflow.md": placeholder("Development Workflow"),
        "docs/development/commits.md": placeholder("Commits"),
        "docs/development/pull-requests.md": placeholder("Pull Requests"),
        "docs/development/testing/README.md": """# Testing Docs

- [strategy.md](strategy.md)
""",
        "docs/development/testing/strategy.md": placeholder("Testing Strategy"),
    },
    "backend": {
        "docs/development/backend.md": placeholder("Backend Standards"),
    },
    "frontend": {
        "docs/development/frontend.md": placeholder("Frontend Standards"),
    },
    "documentation": {
        "docs/development/documentation.md": placeholder("Documentation Maintenance"),
    },
    "git-hooks": {
        "docs/development/git-hooks.md": """# Git Hooks

Local hooks are developer convenience checks, not the only enforcement layer. CI must enforce required merge gates.

## Install

```bash
python scripts/install_git_hooks.py
```

## Current Hooks

- `.githooks/pre-commit`: placeholder hook. Replace with approved fast checks.

## Rules

- Keep hooks fast.
- Do not require secrets or paid external services.
- Mirror required checks in CI before treating them as merge gates.
""",
        "scripts/install_git_hooks.py": """#!/usr/bin/env python3
\"\"\"Install this repo's tracked Git hooks.\"\"\"

from __future__ import annotations

import subprocess
from pathlib import Path


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    hooks = repo / ".githooks"
    if not hooks.is_dir():
        raise SystemExit(f"Missing hooks directory: {hooks}")
    subprocess.run(["git", "config", "core.hooksPath", ".githooks"], cwd=repo, check=True)
    print("Configured git core.hooksPath=.githooks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
""",
        ".githooks/pre-commit": """#!/bin/sh
set -eu

echo "No pre-commit checks configured yet. Replace .githooks/pre-commit with approved fast checks."
""",
    },
    "security": {
        "docs/development/security.md": """# Security

Document approved security checks, dependency policy, secret handling, and vulnerability response.

## Current Decisions

- CodeQL: TODO
- Dependency updates: TODO
- Secret scanning: TODO
- Vulnerability reporting: TODO

## Notes

- Generate CodeQL after languages are confirmed:

```bash
python <bootstrap-skill>/scripts/render_codeql_workflow.py <repo> --mode draft --language <language>
```
""",
        ".github/dependabot.yml": """version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
""",
    },
    "public-repo": {
        "CONTRIBUTING.md": """# Contributing

Thank you for improving this project.

## Workflow

1. Open an issue or discuss broad changes before large rewrites.
2. Keep changes focused.
3. Run documented validation before submitting.
4. Update related docs when behavior, setup, deployment, validation, or standards change.

## Pull Requests

- Describe what changed and why.
- Include validation evidence.
- Call out follow-up work or deferred checks.
""",
        "SECURITY.md": """# Security Policy

## Reporting A Vulnerability

Do not open public issues for suspected vulnerabilities. Contact the repository owner through the approved private channel.

## Supported Versions

This repository does not currently publish versioned releases unless stated elsewhere.
""",
        "docs/development/public-release.md": """# Public Repository Readiness

Use this checklist before making the repository public.

- License chosen and committed as `LICENSE`
- `CONTRIBUTING.md` reviewed
- `SECURITY.md` reviewed
- Code of conduct decision made
- Secret scan completed
- Private URLs, tokens, customer data, and internal-only notes removed
- Install instructions tested from a fresh checkout
""",
    },
    "bootstrap-checklist": {
        "docs/development/bootstrap-checklist.md": """# Bootstrap Checklist

Durable checklist for the repository standards bootstrap. Update this file when the repo gains, rejects, or defers standards, docs, tooling, validation, or agent guidance.

Status values:

- `present`: exists and is adequate for current repo needs
- `partial`: exists but has known gaps
- `missing`: needed but absent
- `not applicable`: intentionally not relevant for this repo
- `defer`: intentionally postponed with an owner or trigger
- `rejected`: intentionally not wanted

## Repository Shape

| Area | Status | Evidence | Decision or Next Step |
| --- | --- | --- | --- |
| Repo purpose and audience | missing |  |  |
| Runtime surfaces identified | missing |  |  |
| Package managers and project files | missing |  |  |

## Human Documentation

| Area | Status | Evidence | Decision or Next Step |
| --- | --- | --- | --- |
| README entrypoint | missing |  |  |
| Local setup and run docs | missing |  |  |
| Deployment, release, or publish docs | missing |  |  |
| Documentation maintenance rules | missing |  |  |
| Work tracking guidance | missing |  |  |

## Product and Architecture

| Area | Status | Evidence | Decision or Next Step |
| --- | --- | --- | --- |
| Product overview | missing |  |  |
| Domain terms and workflows | missing |  |  |
| Architecture overview | missing |  |  |
| Coding standards | missing |  |  |

## Validation and Quality Gates

| Area | Status | Evidence | Decision or Next Step |
| --- | --- | --- | --- |
| Local validation command matrix | missing |  |  |
| Deployed validation expectations | missing |  |  |
| Unit tests | missing |  |  |
| Integration or contract tests | missing |  |  |
| Formatter | missing |  |  |
| Linters | missing |  |  |
| Static analysis | missing |  |  |
| Architecture tests or source guards | missing |  |  |
| Git hooks | missing |  |  |
| CI gates | missing |  |  |
| Dependency, license, vulnerability, or secret checks | missing |  |  |
| CodeQL or equivalent code scanning | missing |  |  |
| Public repo license and contribution files | missing |  |  |

## Agent Guidance and Skills

| Area | Status | Evidence | Decision or Next Step |
| --- | --- | --- | --- |
| AGENTS.md or agent entrypoint | missing |  |  |
| Agent routing docs | missing |  |  |
| Repo-local skills | missing |  |  |
| Skill migration status | missing |  |  |
""",
    },
    "standards-roadmap": {
        "docs/development/standards-roadmap.md": placeholder("Standards Roadmap"),
    },
    "product": {
        "docs/product/README.md": """# Product Docs

Durable product context for humans and agents.
""",
        "docs/product/overview.md": placeholder("Product Overview"),
        "docs/product/ubiquitous-language.md": placeholder("Ubiquitous Language"),
        "docs/product/domain-concepts.md": placeholder("Domain Concepts"),
        "docs/product/personas.md": placeholder("Personas"),
        "docs/product/workflows.md": placeholder("Workflows"),
        "docs/product/requirements/README.md": placeholder("Product Requirements"),
    },
    "work-tracking": {
        "docs/development/work-tracking.md": placeholder("Work Tracking"),
    },
    "file-backlog": {
        "docs/backlog/README.md": """# Backlog

Track file-based delivery backlogs, implementation plans, workflow state, and artifacts only if this repo uses them.

See [index.md](index.md).
""",
        "docs/backlog/index.md": """# Backlog Index

List approved backlog areas.
""",
        "docs/backlog/bugs-and-incidents.md": """# Bugs And Incidents

Track active blocking bugs and concrete runtime incidents here only if this repo uses file-based work tracking.

| ID | Status | Severity | Symptom | Owner/Next Step |
| --- | --- | --- | --- | --- |
""",
        "docs/backlog/follow-ups.md": """# Follow-Ups

Track deferred risks, non-blocking cleanup, and standards follow-ups that should not block the current change.

| ID | Status | Area | Follow-Up | Trigger/Owner |
| --- | --- | --- | --- | --- |
""",
        "docs/backlog/example-capability/backlog.md": placeholder("Example Capability Backlog"),
        "docs/backlog/example-capability/plans/YYYY-MM-DD-example-plan.md": """# Plan: Example Slice

Goal: Replace this with the approved one-sentence outcome.

## Scope

In:
- One narrow implementation slice.

Out:
- Work outside the approved slice.

## Acceptance

- The behavior, docs, or standards change is complete.
- Validation evidence is recorded.

## Tasks

- [T1] Implement the slice.
  Files/Areas: TBD
  Depends on: -
  Parallel: no
  Validation: TBD

## Review

- Run the approved changed-code or docs review gate.

## Final Validation

- TBD
""",
        "docs/backlog/example-capability/workflows/YYYY-MM-DD-example-workflow.md": """# Workflow: Example Queue

Source: [../backlog.md](../backlog.md)
Branch: TBD
Status: draft

## Rules

- Execute one task at a time.
- Ask only blocking questions.
- Stop on failed validation, unsafe git state, or unexpected broad scope.

## Queue

| ID | Status | Depends On | Summary | Validation |
| --- | --- | --- | --- | --- |
| T1 | pending | - | Replace with one sentence. | TBD |

## Current Task

None

## Log

- Created workflow from the approved backlog.
""",
        "docs/backlog/example-capability/plans/.gitkeep": "",
        "docs/backlog/example-capability/workflows/.gitkeep": "",
        "docs/backlog/example-capability/artifacts/.gitkeep": "",
    },
    "skills": {
        ".agents/skills/review-changed-code/SKILL.md": """---
name: review-changed-code
description: Review the current code changes against this repo's standards and directly related context. Use when the user asks for a code review, PR review, changed-code review, diff review, or reviewer pass on in-flight edits. This skill reviews current changes only.
---

# Review Changed Code

Primary lens: `Review`.

Invoked by: implement-planned-work, resolve-bug, orchestrate-work-plan, user directly. Delegates to: none.

## Goal

Review the current diff and only the minimum surrounding context needed to judge it.

## Workflow

1. Load only the standards docs needed for the changed area.
2. Review the diff and directly related code.
3. Use validation output if provided; note missing validation as a gap.
4. Prioritize bugs, regressions, standards violations, risky dependency changes, and missing tests.
5. Do not edit files unless the user explicitly changes the role from reviewer to implementer.

## Output

Return findings first, ordered by impact:

- `[Blocking|Non-blocking] file:line - finding`
- `Why it matters: <short impact>`
- `Verdict: Pass|Fail`

If there are no findings, say so and note any validation gaps.

## Do Not

- Do not turn this into a repo-wide audit.
- Do not manufacture findings.
""",
        ".agents/skills/review-changed-code/agents/openai.yaml": """interface:
  display_name: "Review Changed Code"
  short_description: "Review changes against repo standards"
  default_prompt: "Use $review-changed-code to review the current changes against this repo's standards."
""",
    },
    "implementation-skills": {
        ".agents/skills/plan-implementation-work/SKILL.md": """---
name: plan-implementation-work
description: Plan a user story, bug, task, feature, repo change, or implementation request before coding. Use when Codex should clarify ambiguity, inspect relevant repo context, and produce an implementation-ready task list.
---

# Plan Implementation Work

Primary lens: `Implementation`.

Invoked by: orchestrate-work-plan, resolve-bug, user directly. Delegates to: none.

## Goal

Ask until the work has no material ambiguity, then produce a short task list another implementer can execute without hidden context.

Blocking questions are a stop condition, not a plan section.

## Workflow

1. Clarify outcome, constraints, non-goals, acceptance, and risk.
2. Use supplied issue, tracker, backlog, PRD, or artifacts before loading extra docs.
3. Read nearby patterns for each affected area.
4. Inspect only enough code to plan accurately.
5. Break work into small ordered tasks, usually 3-7.
6. Name files/areas, dependencies, parallel potential, and validation per task.
7. Add technical detail only when it prevents a likely mistake.
8. Present the draft plan in chat before writing durable plan files.

## Output

- `Goal`
- `Scope`: `In` and `Out`
- `Acceptance`
- `Execution Tier`, if the repo defines tiers
- `Assumptions`, only if useful
- `Tasks`: `[Tn]`, `Files/Areas`, `Depends on`, `Parallel`, `Validation`
- `Review`
- `Final Validation`
- `Leftovers`, only if useful

Do not include an `Open Questions` section in a completed plan.

## Do Not

- Do not hide blocking questions inside the plan.
- Do not over-plan internals that should be discovered during implementation.
""",
        ".agents/skills/plan-implementation-work/agents/openai.yaml": """interface:
  display_name: "Plan Implementation Work"
  short_description: "Create an implementation-ready task list"
  default_prompt: "Use $plan-implementation-work to plan this change before coding."
""",
        ".agents/skills/implement-planned-work/SKILL.md": """---
name: implement-planned-work
description: Execute an approved plan or low-context handoff packet in the current repo. Use when Codex should make scoped code/docs changes, run required validation, record the result, and leave orchestration state to the caller when delegated.
---

# Implement Planned Work

Primary lens: `Implementation`.

Invoked by: orchestrate-work-plan, resolve-bug, user directly. Delegates to: review-changed-code and approved validation/docs skills.

## Goal

Execute the supplied plan or handoff packet. Do not re-plan broad scope.

Source of truth:

- approved plan or handoff packet
- repo docs and directly relevant standards
- local code and tests

## Resolve Input

Accept:

- inline approved plan
- plan file
- tracker/issue/PR comment that contains or links an executable plan
- workflow/source item with a clear selected task
- low-context handoff packet from an orchestrator

If the plan is missing risk choices, unclear scope, or unresolved validation, stop for planning instead of inventing them.

## Execute

1. Check `git status --short --branch`.
2. Read overlapping modified files before editing.
3. Build a short checklist from acceptance, tasks, scope, and validation.
4. Implement only the approved scope.
5. Add/update tests at the layer named by the plan when practical.
6. Update docs only when the plan, changed behavior, or repo rules require it.
7. Run required validation.
8. Run `review-changed-code` when the plan, tier, or risk requires it.
9. Write or return the result artifact requested by the caller.

Leave backlog, workflow, cursor, tracker, commit, and PR state to the orchestrator unless explicitly delegated.

## Completion Report

- tasks completed
- files changed
- validation commands/results
- review result or deferred reason
- skipped validation or residual risk
- commit, PR, branch, or tracker updates only if performed

Do not mark work complete when required tasks, blocking review findings, or in-scope validation failures remain.
""",
        ".agents/skills/implement-planned-work/agents/openai.yaml": """interface:
  display_name: "Implement Planned Work"
  short_description: "Execute an approved plan end to end"
  default_prompt: "Use $implement-planned-work to execute this plan."
""",
        ".agents/skills/review-implementation-plan/SKILL.md": """---
name: review-implementation-plan
description: Review an implementation plan before coding for scope, task order, architecture fit, validation, unresolved ambiguity, and handoff clarity. Use when the execution tier, workflow gate, or user requires plan review.
---

# Review Implementation Plan

Primary lens: `Review`.

Invoked by: orchestrate-work-plan, user directly. Delegates to: none.

## Goal

Catch bad implementation plans before code is written.

## Workflow

1. Read the implementation plan.
2. Read the source issue/backlog/tracker item when available.
3. Load only needed standards docs for affected areas.
4. Return findings only; do not edit.

## Checklist

- Scope stays inside the selected work item.
- Tasks are concrete, ordered, dependency-aware, and small enough to validate.
- Risk tier or review gate is named when the repo defines one.
- Architecture, data, UX, auth, and external-system choices are explicit when relevant.
- Tests and validation match the repo strategy.
- No unresolved product, UX, data, architecture, or validation ambiguity remains.

## Output

- `[Blocking|Non-blocking] file:line - finding`
- `Why it matters: <short impact>`
- `Suggested fix: <short action>`
- `Verdict: Pass|Fail`

`Fail` means at least one blocking finding remains.
""",
        ".agents/skills/review-implementation-plan/agents/openai.yaml": """interface:
  display_name: "Review Implementation Plan"
  short_description: "Review a plan before coding"
  default_prompt: "Use $review-implementation-plan to check this plan before implementation."
""",
        ".agents/skills/resolve-bug/SKILL.md": """---
name: resolve-bug
description: Investigate, fix, and validate a reported bug, regression, or concrete runtime incident. Use when the user reports broken behavior, asks Codex to reproduce and fix a defect, or an orchestrated workflow needs a focused bug-resolution pass.
---

# Resolve Bug

Primary lens: `Implementation`.

Invoked by: orchestrate-work-plan, user directly. Delegates to: plan-implementation-work for sensitive changes, approved validation/docs skills, and review-changed-code.

## Goal

Turn a reported symptom into a minimal, validated fix with regression coverage where practical.

## Workflow

1. Clarify only blocking ambiguity.
   - Observed symptom, expected behavior, reproduction path, environment, affected workflow.
   - If the report is broad, narrow to the smallest failing behavior before editing.
2. Reproduce or prove the failure.
   - Prefer the fastest reliable reproduction: focused test, command, log, local flow, API call, or browser check.
   - Record what failed and how it was observed.
   - If reproduction is impossible, identify the strongest evidence and state the uncertainty before fixing.
3. Isolate the cause.
   - Inspect the smallest relevant code path and nearby patterns.
4. Plan only when scope or risk demands it.
5. Implement the minimal fix.
6. Validate the fix.
   - Re-run the failing reproduction first.
   - Add or update regression coverage at the right layer when useful.
   - Use approved UI/API/CLI/deployed validation skills when the surface changed.
7. Run `review-changed-code` when the fix is non-trivial, risky, or workflow-owned.
8. Report root cause, changed files, validation, and residual risk.

## Do Not

- Do not turn a bug pass into unrelated cleanup.
- Do not use this for broad code review, CI debugging, or unresolved PR review comments until they are converted into a concrete symptom.
""",
        ".agents/skills/resolve-bug/agents/openai.yaml": """interface:
  display_name: "Resolve Bug"
  short_description: "Reproduce, fix, and validate a defect"
  default_prompt: "Use $resolve-bug to investigate and fix this reported defect."
""",
    },
    "orchestration-skill": {
        ".agents/skills/orchestrate-work-plan/SKILL.md": """---
name: orchestrate-work-plan
description: Low-context queue runner for an approved backlog, implementation plan, workflow file, tracker item, or multi-task work source. Use when Codex should turn accepted work into one item at a time, create minimal handoff packets, delegate execution, reconcile durable state, and continue safely.
---

# Orchestrate Work Plan

Primary lens: `Implementation`; switch to `Review` only for gates.

Invoked by: user directly. Delegates to: plan-implementation-work, review-implementation-plan, implement-planned-work.

## Goal

Run the queue. Keep context small.

Own:

- source resolution
- queue/workflow state
- one-item selection
- implementation-plan gate
- compact worker handoff
- result reconciliation
- backlog/workflow/tracker status

Do not own:

- implementation internals
- changed-code review checklist
- browser/API/CLI validation procedure
- docs-update procedure

## Source Modes

- Implementation plan: execute directly.
- Workflow state: resume queue before selecting new work.
- Backlog or tracker item: select one ready item.
- Chat or issue: plan first unless already executable.

Default granularity: one ready item or smaller concrete task.

## Preconditions

1. Check `git status --short --branch`.
2. Require a clean worktree unless the active workflow owns the current diff or the user opted in.
3. Report unpushed baseline commits when remote-safe workflow is implied.

## Queue State

Workflow file stays concise:

- source path
- branch/worktree
- status
- queue table
- current task
- short log
- evidence/result artifact links

Detailed validation, screenshots, review output, docs audit, and residual risk go under `artifacts/<item-id>/`, not in the workflow body.

## Planning Gate

For a selected item:

1. Use an existing current implementation plan when present and still accurate.
2. Otherwise invoke `plan-implementation-work` with item ID, acceptance, likely affected areas, and expected validation.
3. Run `review-implementation-plan` when the repo workflow or risk requires it.
4. Write the approved plan under the repo's approved plan location when file-based plans are used.
5. Mark the item `planned`.

Raise only blocking ambiguity to the real user. Continue around blocked items when independent ready work remains.

## Execute One Item

1. Mark workflow/tracker/backlog item `in_progress`.
2. Write a minimal handoff packet:
   - item ID and goal
   - source and plan paths
   - scope in/out
   - acceptance
   - expected validation
   - result artifact path
3. Delegate to `implement-planned-work`.
4. Inspect returned result artifact, `git status`, and `git diff --stat`.
5. Reconcile backlog/workflow/tracker state.
6. Commit only when commit ownership was explicitly assigned.
7. Return control with paths, status, validation, review decisions, blockers, and residual risk.

The queue is not complete until every item is `done` or explicitly `skipped`.

## Compact Workflow Shape

```md
# Workflow: <title>
Source: <file, issue, chat, or tracker reference>
Branch: <branch>
Status: active

## Rules

- Execute one task at a time.
- Ask only blocking questions.
- Stop on failed validation, unsafe git state, or unexpected broad scope.

## Queue

| ID | Status | Depends On | Summary | Validation |
| --- | --- | --- | --- | --- |
| T1 | pending | - | <one sentence> | <focused check> |

## Current Task

None

## Log

- <date>: Created workflow from <source>.
```

## Stop Conditions

Stop after updating durable state when:

- worktree has overlapping unexpected changes
- all remaining items need user decisions
- validation fails after focused repair
- scope must expand beyond the item packet
- commit cannot be created cleanly
- queue state and git history disagree

## Resume

1. Read the workflow file first.
2. Check git status and recent commits.
3. Reconcile queue, source items, result artifacts, and git history.
4. Finish, block, or restore any `in_progress` task based on actual diff.
5. Continue with the next unblocked item.

## Completion Report

Report workflow/tracker path, completed IDs, validation, review result, blocked/skipped work, residual risk, and commit/PR status only if performed.
""",
        ".agents/skills/orchestrate-work-plan/agents/openai.yaml": """interface:
  display_name: "Orchestrate Work Plan"
  short_description: "Run approved work as a resumable workflow"
  default_prompt: "Use $orchestrate-work-plan on this source and advance the next ready task."
""",
    },
    "docs-audit-skills": {
        ".agents/skills/audit-standards-docs/SKILL.md": """---
name: audit-standards-docs
description: Audit repository standards and guidance docs for missing, stale, duplicated, misplaced, over-broad, or unnecessarily verbose guidance. Use to review `AGENTS.md`, `agent-rules/`, or `docs/` for standards coverage and just-enough-context routing.
---

# Audit Standards Docs

Primary lens: `Review`.

Invoked by: user directly, update-documentation, implement-planned-work. Delegates to: none.

## Goal

Audit the repository's guidance as a documentation system, not isolated files. Bias toward brevity, clear routes, and one source of truth per concept.

## Workflow

1. Start from entrypoints: `AGENTS.md`, route indexes, docs indexes.
2. Map scope before reading deeply.
3. Read only the docs needed for the audit question.
4. Check placement:
   - shared durable guidance in `docs/`
   - agent behavior and routing in `agent-rules/`
   - repo-local workflows in `.agents/skills/`
5. Check for stale facts, missing routes, duplicated guidance, hidden required reads, and oversized files.
6. Verify repo reality before calling guidance missing or stale.
7. Make focused fixes when requested; otherwise report findings.

## Output

- scope reviewed
- findings ordered by impact
- supporting file paths
- issue type: missing doc, wrong placement, stale content, duplication, over-context, or verbosity
- conclusion: fix now, defer, or no change needed

## Do Not

- Do not read draft or historical docs unless the task asks for them.
- Do not call guidance stale without checking repo evidence.
""",
        ".agents/skills/audit-standards-docs/agents/openai.yaml": """interface:
  display_name: "Audit Standards Docs"
  short_description: "Audit repo guidance for drift and routing gaps"
  default_prompt: "Use $audit-standards-docs to review this repo's guidance system."
""",
        ".agents/skills/audit-skill-opportunities/SKILL.md": """---
name: audit-skill-opportunities
description: Audit this repository for missing repo-local Codex skills. Use to decide whether repeated repo workflows belong in skills, shared docs, global skills, or no new guidance.
---

# Audit Skill Opportunities

Primary lens: `Review`.

Invoked by: user directly, bootstrap-repo-standards. Delegates to: none.

## Goal

Find high-value missing repo-local skills without inventing skills for work that should stay in shared docs, existing skills, or global behavior.

A candidate must be:

- repo-specific
- repeated
- narrow
- multi-step enough that docs alone are weak
- not already covered by existing docs, skills, or global capabilities

## Workflow

1. Inventory current repo-local skills and routed docs.
2. Inspect repeated task patterns and specialized tool flows.
3. Reject weak candidates aggressively.
4. For each surviving candidate, define:
   - workflow gap
   - repo evidence
   - why a skill beats docs
   - skill name
   - trigger wording
   - references or scripts needed
5. Do not create skills during the audit unless the user explicitly approves creation.

## Output

- scope reviewed
- current skills considered
- findings ordered by impact
- file evidence
- decision: `create skill`, `docs are enough`, `existing skill covers it`, or `defer`
- conclusion: `create now`, `defer`, or `no change needed`

## Do Not

- Do not create skills during this audit unless the user explicitly changes the task to creation.
- Do not recommend broad "do everything in this repo" skills.
""",
        ".agents/skills/audit-skill-opportunities/agents/openai.yaml": """interface:
  display_name: "Audit Skill Opportunities"
  short_description: "Find worthwhile repo-local skill candidates"
  default_prompt: "Use $audit-skill-opportunities to decide whether this repo needs another local skill."
""",
        ".agents/skills/update-documentation/SKILL.md": """---
name: update-documentation
description: Update or propose updates to repo docs and agent routes when code, commands, product behavior, architecture, validation, deployment, or standards change.
---

# Update Documentation

Primary lens: `Implementation`.

Invoked by: implement-planned-work, resolve-bug, user directly. Delegates to: audit-standards-docs when a broader docs review is needed.

## Goal

Keep human docs and agent routes current without duplicating guidance or turning every change into a broad docs rewrite.

## Workflow

1. Identify what changed and which docs could be affected.
2. Read the route indexes first, then the smallest authoritative docs.
3. Decide whether docs need:
   - no change
   - targeted update
   - route/index update
   - follow-up item
   - user decision
4. Keep shared docs useful to humans.
5. Put agent-only behavior in agent routes or repo-local skills.
6. Update only approved or clearly in-scope docs.
7. Verify links and report skipped docs work.

## Output

- docs checked
- docs updated
- route/index updates
- docs intentionally unchanged
- unresolved docs decisions or follow-ups

## Do Not

- Do not rewrite broad docs when a route or paragraph update is enough.
- Do not put agent-only behavior in human-facing docs.
""",
        ".agents/skills/update-documentation/agents/openai.yaml": """interface:
  display_name: "Update Documentation"
  short_description: "Keep docs and agent routes current"
  default_prompt: "Use $update-documentation to check whether this change needs docs or route updates."
""",
    },
    "ui-validation-skill": {
        ".agents/skills/validate-ui-in-browser/SKILL.md": """---
name: validate-ui-in-browser
description: Validate UI changes in the local app with the approved browser workflow. Use when Codex changed user-visible UI behavior and the repo has confirmed local UI run instructions, auth/test data, and browser validation scope.
---

# Validate UI In Browser

Primary lens: `UX`.

Invoked by: implement-planned-work, resolve-bug, user directly. Delegates to: none.

Load the browser-control skill first when available.

## Preconditions

- Repo has a confirmed UI surface.
- Local setup/run docs identify how to start the app.
- Validation docs identify routes, auth/test data, viewports, and screenshot expectations.
- No long-running build/test command from this agent is still running.

## Workflow

1. Read `AGENTS.md`, local setup/run docs, and validation docs.
2. Start the app using the approved local run path.
3. Open the local URL in the approved browser surface.
4. Name persona/auth source before sign-in or seeded-data use.
5. Verify the smallest flow that proves the change.
6. For layout-sensitive changes, check mobile, tablet, and desktop unless the plan narrows scope.
7. For interaction/accessibility risk, check keyboard, focus, labels, validation messages, and dialog behavior relevant to the change.
8. Capture screenshots only after live validation passes and only when required.
9. Stop local processes started for validation.

## Report

- URL used
- persona/auth source
- viewport sizes checked
- what passed
- screenshot artifact paths, if any
- console/UI issues
- cleanup result
- blockers

## Do Not

- Do not use this skill when the repo has no confirmed UI surface.
- Do not mark browser validation complete when required evidence is missing.
""",
        ".agents/skills/validate-ui-in-browser/agents/openai.yaml": """interface:
  display_name: "Validate UI In Browser"
  short_description: "Validate local UI changes in browser"
  default_prompt: "Use $validate-ui-in-browser to validate this UI change locally."
""",
    },
}


def matches_only(relative_path: str, patterns: list[str]) -> bool:
    if not patterns:
        return True
    normalized = relative_path.replace("\\", "/")
    parts = set(normalized.split("/"))
    for pattern in patterns:
        wanted = pattern.replace("\\", "/")
        if normalized == wanted or fnmatch(normalized, wanted):
            return True
        if "/" not in wanted and "*" not in wanted and wanted in parts:
            return True
    return False


def selected_templates(sets: list[str], only_patterns: list[str] | None = None) -> dict[str, str]:
    files: dict[str, str] = {}
    for set_name in sets:
        if set_name not in TEMPLATES:
            allowed = ", ".join(sorted(TEMPLATES))
            raise SystemExit(f"Unknown set '{set_name}'. Allowed: {allowed}")
        files.update(TEMPLATES[set_name])
    patterns = only_patterns or []
    if patterns:
        files = {
            relative_path: content
            for relative_path, content in files.items()
            if matches_only(relative_path, patterns)
        }
        if not files:
            raise SystemExit(
                "No template files matched --only. Use --list to inspect available paths."
            )
    return files


def target_path(repo: Path, mode: str, relative_path: str) -> Path:
    if mode == "draft":
        return repo / TRACKING_DIR / "draft-files" / relative_path
    return repo / relative_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold approved repo backbone files.")
    parser.add_argument("repo", nargs="?", help="Target repository path.")
    parser.add_argument(
        "--mode",
        choices=["draft", "apply"],
        default="draft",
        help="draft writes under .agents/tmp; apply writes durable repo files.",
    )
    parser.add_argument(
        "--set",
        action="append",
        dest="sets",
        default=[],
        help=f"Template set to scaffold. Repeatable. Allowed: {', '.join(sorted(TEMPLATES))}.",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        metavar="PATH_OR_GLOB",
        help="Limit selected sets to matching relative paths, globs, or single path parts. Repeatable.",
    )
    parser.add_argument("--list", action="store_true", help="List template sets and files.")
    parser.add_argument(
        "--overwrite-approved",
        action="store_true",
        help="Overwrite existing files. Use only after exact path-level approval.",
    )
    args = parser.parse_args()

    if args.list:
        for set_name, templates in sorted(TEMPLATES.items()):
            print(f"{set_name}:")
            for path in sorted(templates):
                print(f"  {path}")
        return 0

    if not args.repo:
        parser.error("repo is required unless --list is used")

    repo = Path(args.repo).resolve()
    if not repo.is_dir():
        raise SystemExit(f"Repo path is not a directory: {repo}")

    if not args.sets:
        allowed = ", ".join(sorted(TEMPLATES))
        raise SystemExit(f"Choose at least one explicit --set. Allowed: {allowed}")

    sets = args.sets
    templates = selected_templates(sets, args.only)

    created: list[str] = []
    skipped: list[str] = []
    existing_targets: list[str] = []
    for relative_path, content in templates.items():
        existing_target = repo / relative_path
        if existing_target.exists():
            existing_targets.append(str(existing_target))

        path = target_path(repo, args.mode, relative_path)
        if path.exists() and not args.overwrite_approved:
            skipped.append(str(path))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        created.append(str(path))

    print(f"mode: {args.mode}")
    print(f"sets: {', '.join(sets)}")
    if args.only:
        print(f"only: {', '.join(args.only)}")
    print("created:")
    for path in created:
        print(f"- {path}")
    print("skipped:")
    for path in skipped:
        print(f"- {path}")
    print("existing target files:")
    for path in existing_targets:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
