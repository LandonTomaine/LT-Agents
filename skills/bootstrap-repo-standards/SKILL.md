---
name: bootstrap-repo-standards
description: Deeply inspect a new or existing repository, interview the user about product, architecture, coding standards, local and deployed validation, quality gates, documentation, agent rules, and repo-local skills, then propose a standards backbone before writing durable files. Continue asking, discussing, tracking, and revising until the user says the skill is done or every question and checklist item is resolved with no material ambiguity. Use when Codex should bootstrap or overhaul repo guidance, AGENTS.md, agent-rules indexes, shared docs, linters, formatters, hooks, CI gates, architecture tests, validation workflows, or reusable Codex skills for a small through medium app, service, library, infrastructure, edge, SaaS, or integration-heavy repo.
---

# Bootstrap Repo Standards

## Goal

Turn a repository into a well-routed, human-readable, agent-usable engineering system through evidence, questions, proposals, and explicit approval.

This skill is discovery-first. Never finalize product meaning, architecture policy, coding standards, or durable files from inference alone unless the repo already makes the decision unambiguous and the user confirms it.

## Hard Gates

- Treat the target repo as the path named by the user, or the current working directory if no path is given.
- Start read-only: inspect files, run safe inventory commands, and draft in chat.
- Do not create or modify durable repo files until the user approves an exact file/action manifest.
- Durable files include docs, standards roadmap files, `AGENTS.md`, `agent-rules/`, `.agents/skills/`, legacy `.codex/skills/`, hook configs, CI configs, lint/format configs, tests, and scripts.
- Ask before running commands that may write generated files, install packages, alter hooks, migrate databases, or change lockfiles.
- Product docs require a product interview. Repo clues can create candidate questions and draft outlines, not final product truth.
- Non-agent docs must be useful to humans. Keep agent-only guidance for routing, behavior, and environment constraints.
- For mostly agent-read files, prefer fragments, bullets, and terse directives over prose.
- Prefer brief files, focused routes, and shared docs over large agent-only manuals.
- Do not call the skill done while any question ledger item or checklist item is open, ambiguous, unchecked, or assumption-only unless the user explicitly says to stop or finish anyway.
- Use `.agents/tmp/bootstrap-repo-standards/` for temporary tracking when approved. Treat it as working state, not final documentation.
- Prefer scripts for deterministic folder/file scaffolding. Use AI for decisions and repo-specific content, not repetitive file creation.
- Existing target files are source material. Read, compare, and propose updates; never replace them with skeletons.
- Do not put TODO placeholders in always-loaded agent files. Placeholder files are allowed only for non-always-loaded docs the user approved and is likely to fill later.
- Do not mention where a pattern came from or earlier setup work in generated repo guidance. Use evidence to choose patterns, then write target-repo guidance only.
- Do not assume the repo has a UI, API, deployed environment, or any other runtime surface. Treat every validation surface as a question until file evidence and user confirmation settle it.
- Do not leave validation ambiguity unresolved unless the user explicitly says it can be figured out later; record that as `defer` with an owner or next step.
- Do not treat operational guidance as complete until local setup/run instructions and deployment/release instructions are found, created, rejected as not applicable, or explicitly deferred by the user.
- Do not treat documentation maintenance as solved by creating docs once. Ask how docs should be updated when code, product behavior, commands, environments, or standards change.
- Keep standards-improvement TODOs separate from product backlog unless the user explicitly wants one shared tracker.

## Workflow

1. Establish scope.
   - Identify repo path, repo stage, desired outcome, and whether the user wants audit-only, proposal-only, or approved implementation after discussion.
   - Check git status and note dirty files. Do not overwrite user work.
   - Ask to create or reuse temp tracking files under `.agents/tmp/bootstrap-repo-standards/`. If approved, run `scripts/init_tracking.py <repo>`.

2. Inventory relentlessly but structurally.
   - Run `scripts/repo_scan.py <repo>` from this skill.
   - Use targeted `rg --files` and `rg` searches for docs, doc maintenance guidance, standards TODOs, agent rules, skills, package managers, linters, formatters, analyzers, hooks, CI, tests, architecture tests, validation scripts, generated assets, migrations, deployment, environments, secrets patterns, runtime surfaces, local setup, local run, release/publish, and product docs.
   - Read current entrypoints first: `AGENTS.md`, `README*`, docs indexes, agent-rule indexes, setup/run/deployment docs, existing skills under `.agents/skills` or legacy `.codex/skills`, CI/hook configs, project/package files, and representative tests.
   - For existing repos, sample implementation code by layer or feature before proposing architecture rules.

3. Build an evidence map.
   - Summarize what is proven by files, what is only inferred, and what is unknown.
   - Classify surfaces: product, architecture, backend, frontend, API, workers/jobs, CLI/library, data, tests, local setup/run, deployment/release, local validation, deployed validation, tooling, workflow, docs, documentation maintenance, standards roadmap, agent rules, repo-local skills, CI/hooks.
   - Load [references/backbone-checklist.md](references/backbone-checklist.md) after the repo shape is clear.

4. Interview before prescribing.
   - Load [references/question-bank.md](references/question-bank.md).
   - Load [references/documentation-maintenance.md](references/documentation-maintenance.md) before asking or resolving documentation maintenance, docs update workflow, stale-doc prevention, or docs-update skill questions.
   - Load [references/operational-docs.md](references/operational-docs.md) before asking or resolving local setup, local run, deployment, environment, release, or publish documentation questions.
   - Load [references/validation.md](references/validation.md) before asking or resolving testing, local validation, deployed validation, smoke-check, or validation-skill questions.
   - Ask many concrete questions over as many turns as needed, grouped by theme and ordered by risk.
   - Distinguish blocking decisions from non-blocking preferences.
   - Keep a visible question ledger: `answered`, `unanswered`, `ambiguous`, `assumption candidate`, `defer`.
   - If temp tracking exists, update `question-ledger.md` after every user answer batch.
   - For each inferred recommendation, say what evidence suggested it and ask the user to confirm, reject, or refine it.
   - Continue until decisions are explicit enough to draft and the ledger has no unresolved ambiguity.
   - Require each confirmed repo surface to have an explicit local validation answer and, when deployed environments exist, an explicit deployed validation answer.
   - Require a clear answer for where humans and agents learn how to run locally and how to deploy, release, or publish. If not applicable, record why.
   - Require a clear answer for whether the repo wants a documentation-update workflow or repo-local docs-maintenance skill.
   - Ask whether the repo should include a standards adoption TODO/roadmap for missing or deferred linters, architecture tests, CI, hooks, security checks, validation docs, or other approved quality improvements.
   - If anything remains open, ask the next useful question instead of finalizing.

5. Propose the backbone.
   - Produce a concise proposed file/action manifest:
     - file path
     - create/update/skip
     - audience: human, agent, or both
     - purpose
     - key contents
     - dependencies/routes
     - approval status
   - If temp tracking exists, keep the draft in `backbone-manifest.md` before writing approved final files.
   - Include quality-gate proposals: formatter, static analysis, lints, tests, architecture tests, hooks, CI, dependency/security checks, generated-file checks, and adoption phases.
   - Include repo-local skill proposals only for repeated, repo-specific workflows that docs alone do not cover.
   - Before proposing documentation maintenance docs or docs-update skills, load [references/documentation-maintenance.md](references/documentation-maintenance.md).
   - Before proposing local setup, local run, deployment, release, publish, or environment docs, load [references/operational-docs.md](references/operational-docs.md).
   - Before proposing validation docs, validation gates, smoke checks, deployed checks, or validation skills, load [references/validation.md](references/validation.md).
   - Before proposing, ignoring, globalizing, or migrating repo-local skills, load [references/repo-local-skills.md](references/repo-local-skills.md).
   - Before proposing backlog, PRD, issue, or tracker files, load [references/work-tracking.md](references/work-tracking.md).
   - Before proposing placeholder files, load [references/placeholders.md](references/placeholders.md).
   - Recommend which candidate patterns to adopt, adapt, skip, or avoid based on this repo's actual stack and size.
   - For standard folder/file skeletons, use `scripts/scaffold_backbone.py <repo> --mode draft --set <sets>` to create temp drafts.
   - Scaffolded `agent` files are intentionally minimal. Add doc routes and skill routes only as targeted updates when the referenced files are approved or already exist.
   - Use `--set file-backlog` only when the user chooses file-based work tracking.
   - Use `--set standards-roadmap` only when the user approves a standards adoption TODO/roadmap file.
   - When a target file already exists, mark it `update`, `keep`, or `defer`; do not mark it `create`.
   - If legacy `.codex/skills` exists, offer `keep`, `migrate to .agents/skills`, or `support both temporarily`. Run `scripts/check_skill_migration.py <repo>` before any migration proposal.

6. Get explicit approval.
   - Ask for approval of the manifest or a named subset.
   - Do not write files from a vague approval like "looks good" if paths/actions are not shown.
   - If the user changes direction, revise the manifest in chat first.

7. Implement approved batches.
   - Write only approved files.
   - Prefer `scripts/scaffold_backbone.py <repo> --mode apply --set <sets>` for approved standard skeletons. Apply mode requires explicit `--set` values from the approved manifest.
   - Use scaffold apply only for approved files that do not already exist.
   - For existing files, read current content and apply approved targeted patches.
   - For new custom repo-local skills, invoke the user's `skill-creator` and target `.agents/skills`. Use scaffold only for the approved standard starter skill or approved standard skeletons.
   - For skill migration, update path references and routes in the same approved batch. Do not delete the legacy copy until the migrated skill is validated and the user approves removal.
   - Keep docs short. Use indexes as routing tables, not hidden standards manuals.
   - Update routes and indexes together.
   - Add tests/configs/hooks only when the exact gate and command are approved.
   - Run validation appropriate to the changed files and report what passed, failed, or was not run.

8. Review and iterate until complete.
   - Show the resulting docs/skills/gates as a reviewable system.
   - Ask whether to tighten, split, remove, or defer pieces before calling the backbone finished.
   - Leave unresolved product or architecture questions visible rather than burying them in assumptions.
   - Update `completion-checklist.md` when temp tracking exists.
   - Stop only when the user says the skill is done, or every raised question and checklist item is resolved with no material ambiguity.
   - If completion criteria are not met, keep going: ask, discuss, revise, update ledgers, and re-check.

## Temp Tracking Files

Recommended path: `.agents/tmp/bootstrap-repo-standards/`

- `session.md`: scope, status, stop rule, latest checkpoint.
- `question-ledger.md`: every question, status, answer, source, ambiguity.
- `evidence-map.md`: file-backed facts, inferences, unknowns.
- `backbone-checklist.md`: candidate docs/gates/skills and decision status.
- `backbone-manifest.md`: proposed create/update/skip actions awaiting approval.
- `completion-checklist.md`: final stop criteria.
- `draft-files/`: script-generated draft skeletons mirroring target paths.

Rules:

- Ask before first creation unless the user already approved temp tracking files.
- Preserve existing files; append or update in place.
- Keep entries terse.
- Mark each question one of: `unanswered`, `answered`, `ambiguous`, `assumption candidate`, `defer`.
- `answered` requires enough detail to write or reject a durable item without guessing.
- `defer` requires an owner or explicit reason.
- Mark checklist items `open`, `checked`, `rejected`, or `defer`.
- `checked` requires evidence, user confirmation, or completed approved work.
- Do not graduate temp files into final docs unless approved in the manifest.
- If the repo tracks `.agents/tmp`, ask whether to ignore it before adding ignore rules.

## Completion Criteria

Done only when one is true:

- User explicitly says this pass is done, even with remaining open items.
- Or all are true:
  - `question-ledger.md`: no `unanswered`, `ambiguous`, or `assumption candidate`.
  - `backbone-checklist.md`: no `candidate` or `open`.
  - `backbone-manifest.md`: every row is `approved`, `done`, `rejected`, or `defer`.
  - `completion-checklist.md`: every row is `checked`, `rejected`, or `defer`.
  - No material product, architecture, standards, tooling, docs, quality-gate, or skill ambiguity remains.
  - Documentation maintenance and docs-update workflow expectations are found, approved for creation/update, rejected as not needed, or explicitly deferred by the user.
  - Standards adoption TODO/roadmap is approved, rejected, or explicitly deferred by the user.
  - Local setup/run guidance is found, approved for creation/update, rejected as not applicable, or explicitly deferred by the user.
  - Deployment/release guidance is found, approved for creation/update, rejected as not applicable, or explicitly deferred by the user.
  - Local and deployed validation expectations are explicit for every confirmed runtime surface, or explicitly deferred by the user.
  - Validation for approved changes is recorded.

If not done, ask the next highest-risk unresolved question and keep working.

## Script Safety

- `repo_scan.py`: read-only.
- `check_skill_migration.py`: read-only.
- `init_tracking.py`: writes temp tracking files only.
- `scaffold_backbone.py --mode draft`: writes temp draft files only.
- `scaffold_backbone.py --mode apply`: writes durable target files. Use only after approved manifest.
- Scaffold apply mode skips existing files by default.
- Scaffolded agent routes are minimal by design. Do not assume scaffold output is the final route map.
- Treat scaffold "skipped existing" output as a required review list.
- Do not use scaffold overwrite for existing guidance files. Prefer targeted patches.
- Use scaffold overwrite only for newly generated temp drafts or exact path-level replacement approved by the user.
- Before any write-mode script, state mode, target root, file sets, and whether durable files may be written.

## Candidate Defaults

Use these as candidate patterns, not universal rules:

- Tiny `AGENTS.md` that routes to an agent index.
- `agent-rules/README.md` as the routing layer.
- Always-load agent files for core behavior and communication only.
- Shared `docs/` for product, architecture, development, local setup, deployment/release, testing, tooling, workflow, commits, PRs, and work tracking.
- `docs/development/documentation.md` for documentation ownership, update triggers, stale-doc prevention, and docs review expectations when no adequate existing doc exists.
- `docs/development/standards-roadmap.md` as an optional non-always-loaded TODO/roadmap for deferred quality gates and standards work such as linters, architecture tests, hooks, CI, security checks, dependency checks, generated-file checks, validation docs, or deployment docs.
- `docs/development/local-setup.md` for prerequisites, install/restore, secrets/env, local services, run commands, local URLs/interfaces, data setup, and troubleshooting when no adequate existing doc exists.
- `docs/development/deployment.md` for environments, deploy/release/publish ownership, commands or pipelines, config/secrets, migrations, smoke checks, rollback/stop rules, and access constraints when no adequate existing doc exists.
- `docs/development/validation.md` for local and deployed validation expectations, environment-specific smoke checks, manual checks, credentials/test-data assumptions, and completion proof.
- `docs/development/work-tracking.md` as the generic TODO placeholder when the repo uses GitHub, Azure DevOps, Linear, Jira, or another external tracker but the workflow is not decided yet.
- `docs/backlog/` only when the user chooses file-based PRD/backlog management; scaffold with `--set file-backlog`.
- Architecture tests as executable standards where stack support exists.
- Formatter/linter/static-analysis gates documented beside the actual configs.
- Hooks and CI that mirror the same meaningful checks.
- Repo-local skills under `.agents/skills`; offer migration for legacy `.codex/skills`.
- A minimal `review-changed-code` repo-local starter skill when skill scaffolding is approved and no equivalent exists.
- A focused `update-documentation` repo-local skill when docs maintenance is repeated, repo-specific, and too procedural for a short shared doc.
- Validation skills only when the corresponding surface exists and the workflow is repeated. Propose UI/browser validation only for repos with a confirmed UI; otherwise ask about API, CLI, worker/job, package/library, migration, or deployed smoke validation instead.

## Outputs

Before approval:
- scan summary
- evidence map
- question ledger
- proposed backbone manifest
- recommended adoption phases

After approval:
- changed files
- validation results
- remaining unanswered questions
- next recommended batch, if any
