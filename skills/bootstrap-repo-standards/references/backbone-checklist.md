# Backbone Checklist

Use after the repo inventory is clear. Treat every item as a candidate, not a prescription.

## Documentation Backbone

- `README.md`: human repo entrypoint, setup pointer, repo shape, next-read links.
- `AGENTS.md`: tiny agent entrypoint, not a standards manual.
- `CLAUDE.md`: optional tiny redirect to `AGENTS.md`, only when the repo wants a Claude entrypoint.
- `agent-rules/README.md`: routing index, always-load list, task-to-doc routes, repo-local skill inventory.
- `agent-rules/core.md`: agent behavior that is always true in this repo.
- `agent-rules/communication-style.md`: repo-specific user-facing style, only if different from global norms.
- `agent-rules/shell.md`: repo/environment command constraints.
- `agent-rules/maintaining.md`: where guidance belongs and how to keep routes DRY.
- `agent-rules/working-modes.md`: optional task lenses for product, architecture, implementation, review.
- `docs/README.md`: human documentation map.
- `docs/architecture/overview.md`: boundaries, dependency flow, module ownership, source-of-truth tests.
- `docs/development/README.md`: coding/tooling/testing/workflow map.
- `docs/development/local-setup.md`: prerequisites, install/restore, env/secrets, services, run commands, URLs, data setup, troubleshooting.
- `docs/development/deployment.md`: environments, deploy/release/publish ownership, commands or pipelines, config/secrets, migrations, smoke checks, rollback/stop rules.
- `docs/development/backend.md`: backend standards when backend exists.
- `docs/development/frontend.md`: frontend standards when frontend exists.
- `docs/development/testing/strategy.md`: test layers, when to use each, validation before merge.
- `docs/development/validation.md`: local and deployed validation expectations by runtime surface and environment.
- `docs/development/tooling.md`: commands, hooks, format/lint/build/test references.
- `docs/development/git-hooks.md`: hook install command, installed hook path, fast local checks, CI mirror expectations.
- `docs/development/workflow.md`: branch, implementation, validation, handoff flow.
- `docs/development/security.md`: CodeQL/security scanning, dependency update policy, secrets, vulnerability handling.
- `docs/development/documentation.md`: documentation ownership, update triggers, stale-doc prevention, and docs review expectations.
- `CONTRIBUTING.md`: public or shared contribution workflow.
- `SECURITY.md`: vulnerability reporting and supported versions.
- `LICENSE`: only after the user chooses a license.
- `docs/development/standards-roadmap.md`: optional TODO/roadmap for deferred standards and quality-gate work.
- `docs/development/commits.md`: commit style if repo has conventions.
- `docs/development/pull-requests.md`: PR expectations if repo uses PRs.
- `docs/product/`: only after product interview or strong existing product docs.
- `docs/development/work-tracking.md`: generic TODO placeholder only when external tracker workflow is selected but not yet defined.
- `docs/backlog/`: only if this repo uses file-based planning/backlog files.
- file-based plan/workflow templates: only when file-based orchestration is approved.

Keep indexes as maps. Put actual policy in focused docs. Prefer shared docs over agent-only docs unless the guidance is purely agent behavior. For mostly agent-read files, use terse bullets/fragments over prose.

## Documentation Maintenance Choice

Load `references/documentation-maintenance.md` before resolving this section.

Find existing docs-maintenance guidance before proposing new files. Ask how documentation stays current when code, commands, product behavior, deployment, validation, architecture, standards, or integrations change.

Decide:

- where documentation maintenance rules live
- which changes require docs updates
- whether agents update docs with code, propose separately, or ask first
- which docs are authoritative versus historical/planning artifacts
- how stale, duplicated, or conflicting docs are handled
- whether PR/review guidance should include docs checks
- whether a repo-local `update-documentation` skill is useful

Use `docs/development/documentation.md` only when no adequate existing doc covers this.

## Standards Adoption Roadmap Choice

Ask whether to create or update a non-product standards TODO/roadmap. Keep this separate from backlog/work tracking unless the user explicitly wants one shared tracker.

Use it for deferred bootstrap follow-ups such as:

- formatter, linter, static analysis, or style gates
- architecture tests or source guards
- CI and local hooks
- dependency, vulnerability, license, or secret scanning
- CodeQL or equivalent code scanning
- public-repo files such as license, contribution, security, and code-of-conduct decisions
- generated-file cleanliness checks
- test-layer gaps
- validation, local setup, deployment, or documentation follow-ups
- agent rule or skill migration follow-ups

Default path when approved: `docs/development/standards-roadmap.md`.

Do not create it by default. If details are known and approved, write real checklist items; otherwise use a short approved TODO placeholder.

## Durable Bootstrap Checklist Choice

Default path: `docs/development/bootstrap-checklist.md`.

Propose this file in the first manifest unless the user rejects a durable checklist. It is the tracked repo ledger for what the bootstrap found, what exists, what is missing, what is not applicable, and what is deferred.

Use status values consistently:

- `present`: exists and is adequate for current repo needs.
- `partial`: exists but has known gaps.
- `missing`: needed but absent.
- `not applicable`: intentionally not relevant for this repo.
- `defer`: postponed with owner or trigger.
- `rejected`: intentionally not wanted.

Checklist rows should include:

- area
- status
- evidence path for `present` or `partial`
- decision or next step

Recommended checklist categories:

- repository shape: purpose, audience, runtime surfaces, package managers, project files
- human documentation: README, local setup/run, deployment/release/publish, documentation maintenance, work tracking
- product and architecture: product overview, domain terms, workflows, architecture overview, coding standards
- validation and quality gates: local validation, deployed validation, unit tests, integration/contract tests, formatter, linters, static analysis, architecture tests, hooks, CI, dependency/security checks
- agent guidance and skills: AGENTS.md, agent routing docs, repo-local skills, skill migration status

Keep future work here as standards/bootstrap follow-up. Use `docs/development/standards-roadmap.md` only when the user wants a separate roadmap for phased adoption detail.

## Quality Gates

Look for or propose stack-appropriate equivalents:

- editor config: indentation, line endings, charset, language style severities.
- formatter: `dotnet format`, Prettier, Biome, Black, Ruff format, gofmt, rustfmt, ktlint, etc.
- static analysis: Roslyn analyzers, StyleCop, ESLint, TypeScript strictness, Ruff, mypy/pyright, golangci-lint, clippy, SpotBugs, Checkstyle, Semgrep.
- frontend lint: TypeScript/JavaScript lint, markup lint, CSS/style lint, accessibility checks where practical.
- source guards: custom checks for repo-specific placement or "do not do X" rules.
- tests: unit, integration, contract, architecture, E2E, smoke, migration tests.
- architecture tests: executable dependency and convention checks.
- local validation: commands, manual checks, local URLs, ports, fixtures, env vars, and evidence required before completion.
- deployed validation: environment-specific smoke checks, safe test data, auth, logs/metrics/alerts, rollback, and stop conditions.
- generated-file cleanliness: fail if generated outputs are stale or uncommitted.
- build warnings: decide whether warnings fail locally, in CI, or only by phase.
- hooks: pre-commit/pre-push for fast local gates, documented as convenience not security.
- CI: mirrors merge-protecting checks; does not rely on local hooks.
- dependency hygiene: lockfiles, central versions, package audit, vulnerable dependency policy.
- CodeQL: propose only after repository languages are known; use `scripts/render_codeql_workflow.py` for approved language-specific workflows.
- secrets: ignore patterns, secret scanning, local secret setup docs.
- migrations: generation commands, naming, generated-code exceptions, review rules.
- deployment/runtime: environment variables, config ownership, smoke checks.

## Operational Docs Choice

Load `references/operational-docs.md` before resolving this section.

Find existing local setup/run and deployment/release docs before proposing new files. Treat existing docs as source material: route to them, update them, or mark gaps. Do not create duplicate docs just because the default file names do not exist.

Local setup/run must answer or explicitly defer:

- prerequisites and tool versions
- install/restore commands
- env vars, secrets, local config
- local services, containers, emulators, databases
- seed data, fixtures, or test accounts
- commands to run each app/service/surface
- local URLs, ports, endpoints, CLI entrypoints
- proof that local startup worked

Deployment/release must answer or explicitly defer:

- whether the repo deploys, releases, publishes, or has no deployable artifact
- environments and who owns them
- whether Codex may deploy/release or only document/validate
- command, CI pipeline, provider dashboard, or manual checklist
- secrets/config/feature flags/migrations/approvals
- post-deploy smoke checks and observability
- rollback, stop, and forbidden-production-action rules

Preferred docs when no adequate existing docs exist:

- `docs/development/local-setup.md`
- `docs/development/deployment.md`

For tiny repos, a concise root `README.md` section can be enough if it stays human-usable and agent-routable.

## Architecture Test Ideas

Only add tests that match real architecture decisions:

- Layer dependency direction.
- Forbidden dependencies in domain/core modules.
- Feature/slice folder placement.
- Handler/service/controller naming and registration conventions.
- UI layer cannot access persistence directly.
- Queries/read paths use no tracking or read-only patterns where relevant.
- Commands write through approved transaction boundary.
- No service locator.
- No cross-feature imports except approved shared areas.
- API contract naming/versioning.
- Module size thresholds with explicit exception lists.
- Security boundaries such as tenant filters or authorization entrypoints.

Stack examples:

- .NET: NetArchTest.Rules, ArchUnitNET, Roslyn/source checks.
- Java/Kotlin: ArchUnit, Checkstyle, Error Prone.
- TypeScript: dependency-cruiser, ESLint boundary rules, ts-prune.
- Python: import-linter, Ruff custom checks, pytest architecture tests.
- Go: package import tests, staticcheck, custom `go list` checks.

## Repo-Local Skill Candidates

Load `references/repo-local-skills.md` before proposing, creating, copying, globalizing, ignoring, deferring, or migrating skills.

Common candidates:

- review changed code against repo standards
- plan implementation work
- implement approved plan
- review implementation plan before coding
- orchestrate a work plan through task queue, validation, review, and handoff
- resolve bug or regression
- update documentation when code, commands, product behavior, architecture, validation, deployment, or standards change
- validate UI in browser, only when the repo has a confirmed UI
- validate API smoke checks, only when the repo has a confirmed API
- validate CLI/package behavior, only when the repo has a confirmed CLI or library/package workflow
- validate worker, scheduled job, migration, or deployed smoke behavior only when those surfaces exist
- draft backlog slices from PRD, only for file-based planning repos
- audit standards docs
- audit skill opportunities
- add vertical-slice feature
- plan architecture cleanup

Reject broad "do everything in this repo" skills. Prefer focused skills with references or scripts for the detailed parts.
Require a per-skill decision row with evidence, trigger, placement, creation method, and approval status. Source/global skill comparisons must use `references/source-skill-patterns.md`.

## Validation Choice

Load `references/validation.md` before resolving this section.
Every confirmed runtime surface needs local validation. Every deployed environment needs deployed validation, or an explicit `defer` with owner and next step.

## Work Tracking Choice

Load `references/work-tracking.md` before proposing PRD, backlog, issue, tracker, plan, or workflow-state files. Ask for `file-based`, `external-tracker`, `none`, or `defer` before creating backlog files.

## Product Documentation Gate

Do not finalize product docs from code shape alone.

Minimum product interview areas:

- purpose and target users
- current product stage
- in-scope and out-of-scope workflows
- personas and permissions
- vocabulary and domain concepts
- core lifecycle states
- external integrations
- data/privacy/security boundaries
- non-functional expectations
- known client/stakeholder review questions
- decisions that block architecture

Useful product docs after approval:

- `docs/product/overview.md`
- `docs/product/ubiquitous-language.md`
- `docs/product/domain-concepts.md`
- `docs/product/personas.md`
- `docs/product/workflows.md`
- `docs/product/requirements/README.md`
- parent PRD and child PRDs only when the user wants durable product planning.

## Adoption Phases

Prefer phased adoption for existing repos:

1. Routing and documentation map.
2. Known commands documented exactly as they work today.
3. Non-invasive format/lint checks.
4. Tests and architecture tests for already-agreed boundaries.
5. Hooks/CI after commands are reliable.
6. Stricter warnings/security/dependency gates.
7. Repo-local skills for repeated workflows.

## Git Hooks Choice

Ask whether tracked local hooks should exist. Hooks are developer convenience; CI must enforce required checks.

Default scaffold set when approved: `git-hooks`.

The scaffold creates:

- `docs/development/git-hooks.md`
- `scripts/install_git_hooks.py`
- `.githooks/pre-commit`

Replace placeholder hook commands with approved fast checks before treating hooks as meaningful validation.

## Security And Public Repo Choice

Ask whether CodeQL/security scanning and public-repo files are in scope.

Use:

- `security` scaffold set for `docs/development/security.md` and `.github/dependabot.yml`.
- `scripts/render_codeql_workflow.py <repo> --mode draft --language <language>` after CodeQL languages are confirmed.
- `public-repo` scaffold set for `CONTRIBUTING.md`, `SECURITY.md`, and `docs/development/public-release.md`.

Do not create `LICENSE` until the user chooses the license text or license family.

For brand-new repos, draft the desired end state but still ask which gates should block work immediately.
