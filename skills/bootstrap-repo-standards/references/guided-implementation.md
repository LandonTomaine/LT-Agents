# Guided Implementation Backbone

Load when turning bootstrap findings into an approved implementation system, especially for app repos that should support autonomous agent work.

## Repo Starting Points

Classify the repo before proposing files:

- `empty`: little or no code/docs. Start with route docs, local setup assumptions, validation decisions, and a bootstrap checklist. Avoid product/architecture claims until interviewed.
- `docs-prefilled`: docs exist before code or alongside sparse code. Audit routes, ownership, and stale assumptions before adding scaffolds.
- `code-prefilled`: code exists with thin docs. Prioritize exact setup/run, validation, architecture/source-of-truth tests, and route docs.
- `active app`: code, docs, tests, deployment, and work tracking exist. Preserve existing patterns; propose targeted updates, not replacement skeletons.

## Backbone Order

Prefer this sequence:

1. Minimal entrypoints and routes.
   - `AGENTS.md`: tiny pointer to `agent-rules/README.md`.
   - `agent-rules/README.md`: always-load file, task-to-doc routes, repo-local skill inventory.
   - `agent-rules/core.md`: agent behavior that truly belongs in every task.
2. Human docs map.
   - `docs/README.md`: map, not handbook.
   - `docs/development/README.md`: setup, tooling, testing, workflow routes.
3. Get the app running.
   - local prerequisites
   - install/restore
   - env/secrets
   - services/databases/emulators
   - run commands
   - URLs/ports
   - proof startup worked
4. Validation matrix.
   - local checks by change type
   - deployed checks by environment
   - browser/API/CLI/job/migration validation only for confirmed surfaces
5. Documentation maintenance.
   - update triggers
   - authoritative docs
   - stale-doc handling
   - review expectations
6. Work tracking.
   - external tracker, file-based tracking, none, or defer.
7. Repo-local skills.
   - only for repeated repo-specific workflows that docs alone do not handle well.
   - use [source-skill-patterns.md](source-skill-patterns.md) only as a side reference when comparing global/source-repo skills.
8. Quality gates.
   - formatter, lint, static analysis, architecture tests, hooks, CI, dependency/security scans.

## Copy, Adapt, Generate

Copy nearly exactly:

- minimal `AGENTS.md` route shape
- optional minimal `CLAUDE.md` redirect when the repo wants a Claude entrypoint
- `agent-rules/README.md` as a routing index
- compact plan/workflow headings for file-based work tracking

Adapt:

- `agent-rules/core.md`
- shell/environment rules
- architecture/testing/tooling docs
- validation skills
- implementation and orchestration skills, but only when the repo has a repeated workflow that one focused skill cannot cover

Generate by script when approved:

- route/index skeletons
- bootstrap checklist
- file backlog, bugs, follow-ups, plan, and workflow templates
- starter `review-changed-code`
- small repo-local skills first; scaffold sets are candidate batches, not adoption defaults
- hook/security/public-repo skeletons

Do not copy:

- product-specific docs
- domain vocabulary from another repo
- provider-specific setup such as Auth0, Azure, AppHost, Cloudflare, Supabase, or Vercel unless this repo uses it
- temporary agent state such as `.codex/tmp`, `.codex/state`, or local artifacts
- legacy `.codex/skills` as a new default path

## Repo-Local Skill Contract

Use this compact shape for generated or adapted repo-local skills:

- frontmatter with narrow trigger
- `Primary lens`
- `Invoked by` and `Delegates to`, when useful
- short `Goal`
- concrete `Workflow`
- explicit `Output`
- `Do Not` only for likely mistakes

Put long checklists in `references/`. Put deterministic helpers in `scripts/`.

## Scaffold Set Use

Use `scripts/scaffold_backbone.py <repo> --mode draft --set <set>` for approved draft skeletons. Add `--only <path-or-skill-folder>` when only one file or skill from a set is approved. The script requires explicit `--set`; do not rely on defaults.

Recommended batches:

- First docs route pass: `agent`, `docs`, `bootstrap-checklist`
- Optional Claude route: `claude-entrypoint`
- Code app with known backend/frontend: add `backend`, `frontend`, `documentation`
- File-based delivery: `file-backlog`, then only the individual approved skill candidates that cover the workflow
- Docs/skills governance: individual docs-audit or docs-update skills, not the whole set by default
- Confirmed UI/browser workflow: `ui-validation-skill`
- External/public/shared repo: `security`, `public-repo`, optional CodeQL render
- Local hooks after commands are stable: `git-hooks`

Never scaffold optional skills just because they exist. Show the manifest and get approval.

When adapting existing global or source-repo skills, load [source-skill-patterns.md](source-skill-patterns.md). Prefer variants such as one-ticket, external-tracker, docs-only, or no-orchestration when the target repo does not want file-based backlog tracking or MVP-wide orchestration.

Default to fewer skills:

- one focused repo-local skill beats a copied suite
- one review gate or one routing skill beats a bundled planning/execution package
- one route doc beats a repo-local skill when the workflow is mostly policy
- one-ticket or docs-only beats orchestration unless recurrence is already proven
- generated implementation skills should stay separate: plan, plan review, implement, bugfix, changed-code review

## Autonomous Orchestration Readiness

Autonomous orchestration is ready only when these are explicit or deferred with owner/trigger:

- work source: file backlog or external tracker
- task packet shape
- local setup/run
- local validation by surface
- deployed validation, if environments exist
- review gate
- docs-update rule
- commit/PR/tracker ownership
- stop conditions
- residual-risk location

If any item is unknown, ask the next blocking question or mark it `defer` only with explicit user agreement.
