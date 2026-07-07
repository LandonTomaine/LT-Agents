---
name: bootstrap-repo-standards
description: Bootstrap or overhaul repository standards for a small to medium app, service, library, infrastructure, SaaS, edge, or integration-heavy repo. Use when Codex should inspect a repo with bundled repo_scan.py, interview about product and architecture decisions, and propose approved docs, AGENTS.md, agent rules, linters, formatters, tests, CI, hooks, validation workflows, repo-local skills, and a durable bootstrap checklist before writing files.
---

# Bootstrap Repo Standards

Primary lens: `Implementation`.

## Goal

Turn a repository into a well-routed, human-readable, agent-usable engineering system through evidence, questions, proposals, and explicit approval.

Discovery first. Do not finalize product meaning, architecture policy, coding standards, repo-local skills, or durable files from inference alone.

## Gates

- Treat the target repo as the path named by the user, or the current working directory if no path is given.
- Before broad manual inventory, run `scripts/repo_scan.py <repo>` from this skill and summarize its output. If it cannot run, report the exact blocker and then do an explicit manual fallback inventory.
- If Python is unavailable for bundled scripts, ask whether to install Python, use another available Python launcher, or proceed with a manual fallback. Do not silently skip the scripts.
- Start read-only. Do not create or modify durable repo files until the user approves an exact file/action manifest.
- Existing target files are source material. Read, compare, and patch; do not replace them with generic skeletons.
- Ask before running commands that may write generated files, install packages, alter hooks, migrate databases, or change lockfiles.
- Product docs require a product interview. Repo clues can suggest questions and draft outlines, not final truth.
- Keep non-agent docs useful to humans and agent docs short. Prefer routes, focused files, and terse directives over manuals.
- Do not call the skill done while material questions, checklist items, or validation decisions remain open unless the user explicitly accepts that stop point.
- Use `.agents/tmp/bootstrap-repo-standards/` only as approved working state, never as final documentation.
- Prefer scripts for deterministic folder/file scaffolding. Use AI for decisions and repo-specific content, not repetitive file creation.
- Use `scripts/scaffold_backbone.py` for approved standard shapes and `scripts/copy_skill_package.py` for approved source skill copies.
- Do not hand-write reusable skill packages from memory.
- Do not put TODO placeholders in always-loaded agent files.
- Do not mention where a pattern came from or earlier setup work in generated repo guidance. Use evidence to choose patterns, then write target-repo guidance only.
- Do not assume the repo has a UI, API, deployed environment, or any other runtime surface. Treat every validation surface as a question until file evidence and user confirmation settle it.
- Keep validation, setup/run, deployment/release, and docs-maintenance decisions explicit. If they are deferred, record the defer and owner/next step.
- Keep standards-improvement TODOs separate from product backlog unless the user explicitly wants one shared tracker.
- Include a durable tracked bootstrap checklist in the first proposed manifest unless the user rejects it.
- Every candidate skill requires an explicit placement decision: `repo-local`, `user/global`, `ignore`, or `defer`.
- Source skills are side references. Copy only a compact contract or narrow workflow shape after explicit repo-fit and manifest approval.

## Workflow

1. Establish scope.
   - Identify repo path, repo stage, desired outcome, and whether the user wants audit-only, proposal-only, or approved implementation after discussion.
   - Check git status and note dirty files. Do not overwrite user work.
   - Load [references/execution-contracts.md](references/execution-contracts.md) before creating temp tracking, judging completion, or running write-mode scaffold scripts.
   - Ask to create or reuse temp tracking files under `.agents/tmp/bootstrap-repo-standards/`. If approved, run `scripts/init_tracking.py <repo>`.

2. Inventory relentlessly but structurally.
   - First command after git status: `python <this-skill>/scripts/repo_scan.py <repo>` or equivalent Python launcher for the environment.
   - If no Python launcher works, ask before installing Python or using the manual fallback.
   - If the scan fails, capture the command, exit/failure reason, and fallback searches used.
   - Use targeted `rg --files` and `rg` searches to confirm docs, routes, setup/run, deployment/release, validation, tooling, skills, hooks, CI, tests, and runtime surfaces.
   - If the scan or searches find `.codex/skills`, `.agents/skills`, or possible skill migration work, run `scripts/check_skill_migration.py <repo>` before proposing anything about skill placement or migration.
   - Read current entrypoints first: `AGENTS.md`, `README*`, docs indexes, agent-rule indexes, setup/run/deployment docs, existing skills under `.agents/skills` or legacy `.codex/skills`, CI/hook configs, project/package files, and representative tests.
   - For existing repos, sample implementation code by layer or feature before proposing architecture rules.

3. Build an evidence map.
   - Summarize what is proven by files, what is only inferred, and what is unknown.
   - Classify surfaces: product, architecture, backend, frontend, API, workers/jobs, CLI/library, data, tests, local setup/run, deployment/release, local validation, deployed validation, tooling, workflow, docs, documentation maintenance, standards roadmap, agent rules, repo-local skills, CI/hooks.
   - Load [references/backbone-checklist.md](references/backbone-checklist.md) after the repo shape is clear.
   - Load [references/guided-implementation.md](references/guided-implementation.md) before classifying the repo as empty, docs-prefilled, code-prefilled, or active app and before recommending autonomous orchestration scaffolds.
   - Prepare durable checklist entries for `present`, `partial`, `missing`, `not applicable`, `defer`, or `rejected` status with file evidence and next steps.

4. Interview before prescribing.
   - Load [references/question-bank.md](references/question-bank.md).
   - Load [references/documentation-maintenance.md](references/documentation-maintenance.md), [references/operational-docs.md](references/operational-docs.md), and [references/validation.md](references/validation.md) only when those themes are in scope.
   - Ask concrete questions, grouped by theme and ordered by risk.
   - Distinguish blocking decisions from non-blocking preferences.
   - Keep a visible question ledger: `answered`, `unanswered`, `ambiguous`, `assumption candidate`, `defer`.
   - If temp tracking exists, update `question-ledger.md` after every user answer batch.
   - For each inferred recommendation, cite the evidence and ask the user to confirm, reject, or refine it.
   - Continue until decisions are explicit enough to draft.
   - Require each confirmed repo surface to have an explicit local validation answer and, when deployed environments exist, an explicit deployed validation answer.
   - Require explicit decisions for setup/run routes, deployment/release routes, docs maintenance, work tracking, and standards roadmap handling.

5. Propose the backbone.
   - Produce a concise proposed file/action manifest:
     - file path
     - create/update/skip
     - audience: human, agent, or both
     - purpose
     - key contents
     - dependencies/routes
     - approval status
   - Include `docs/development/bootstrap-checklist.md` as `create` or `update` unless the user rejects a durable checklist.
   - If temp tracking exists, keep the draft in `backbone-manifest.md` before writing approved final files.
   - Include quality-gate proposals only when evidence or user goals justify them.
   - Include git hook, CodeQL, security, and public-repo readiness files only when the repo is public, shared externally, or the user wants those gates.
   - Load the relevant reference before proposing docs maintenance, operational docs, validation docs, repo-local skills, work tracking, placeholders, or source-skill copies.
   - Include skill proposals only after a per-skill decision table shows evidence, trigger, placement, docs-vs-skill rationale, source/global equivalent, and approval status.
   - Recommend which candidate patterns to adopt, adapt, skip, or avoid based on this repo's actual stack and size.
   - For the durable bootstrap checklist, use `scripts/scaffold_backbone.py <repo> --mode draft --set bootstrap-checklist` for a draft or `--mode apply --set bootstrap-checklist` after approval, then replace generic rows with repo-specific evidence.
   - Use draft mode first for optional skills, hooks, security/public-repo files, file-backlog, standards-roadmap, and approved source skill copies.
   - Use `--only <path-or-skill-folder>` when drafting or applying one approved generated skill from a larger scaffold set.
   - Do not propose broad skill bundles when one focused repo-local skill or one route doc would cover the need.

6. Get explicit approval.
   - Ask for approval of the manifest or a named subset.
   - Do not write files from a vague approval like "looks good" if paths/actions are not shown.
   - If the user changes direction, revise the manifest in chat first.

7. Implement approved batches.
   - Write only approved files.
   - Create or update the durable bootstrap checklist before broader standards files so later work has a tracked ledger.
   - Prefer `scripts/scaffold_backbone.py <repo> --mode draft --set <set> --only <path-or-skill-folder>` before apply for individual approved generated skills.
   - Use `scripts/copy_skill_package.py <source-skill-dir> <repo> --mode draft` before apply for approved source skill copies.
   - Use apply mode only for approved files and exact approved target paths.
   - For existing files, read current content and apply approved targeted patches.
   - For new custom repo-local skills, invoke the user's `skill-creator` and target `.agents/skills`. Use scaffold only for the approved standard starter skill or approved standard skeletons.
   - For skill migration, update path references and routes in the same approved batch. Do not delete the legacy copy until the migrated skill is validated and the user approves removal.
   - Keep docs short and update routes/indexes together.
   - Add tests/configs/hooks only when the exact gate and command are approved.
   - Run validation appropriate to the changed files and report what passed, failed, or was not run.

8. Review and iterate until complete.
   - Show the resulting docs, skills, and gates as a reviewable system.
   - Ask whether to tighten, split, remove, or defer pieces before calling the backbone finished.
   - Leave unresolved product or architecture questions visible rather than burying them in assumptions.
   - Update `completion-checklist.md` when temp tracking exists.
   - If completion criteria are not met, keep going: ask, revise, update ledgers, and re-check.

## Execution Contracts

Load [references/execution-contracts.md](references/execution-contracts.md) when temp tracking, durable bootstrap checklist rules, completion criteria, script safety, scaffold sets, or final output shape matters.

## Do Not

- Do not scaffold optional skill groups just because the script can generate them.
- Do not turn source-repo workflows into target-repo policy without user confirmation.
