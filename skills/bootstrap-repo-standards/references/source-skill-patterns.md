# Source Skill Patterns

Load when the user wants bootstrap to compare, adapt, migrate, or copy ideas from existing global or source-repo skills.

This is a pattern catalog, not a default manifest. Source skills are side references. Use them to ask better questions and draft better options, not to force a target repo into another repo's workflow.

## Source Locations

Use only when available or provided by the user:

- Global/user skills: active skill list, `$CODEX_HOME/skills`, or `$HOME/.codex/skills`.
- Source repo skills: a provided repo path such as `<source-repo>/.codex/skills` or `<source-repo>/.agents/skills`.
- Target repo skills: `<target-repo>/.agents/skills` or legacy `<target-repo>/.codex/skills`.

Do not hardcode a personal absolute path in generated target guidance. Use evidence from the target repo and the user's explicit source path.

## How To Use Source Skills

1. Inventory names and descriptions first.
2. Group by workflow family.
3. Decide for each family:
   - `copy shape`: same compact contract, target-specific content
   - `adapt`: reuse workflow idea with changed scope, routes, or stop conditions
   - `reference only`: mention as global/user capability, no repo files
   - `skip`: wrong for this repo
4. Ask the user for placement: `repo-local`, `user/global`, `ignore`, or `defer`.
5. Ask the user about workflow mode before proposing files.
6. Scaffold only approved standard shapes; use custom skill creation for repo-specific variants.
7. Use `scripts/copy_skill_package.py` for approved copies of concrete existing skill packages.

## Global Skill Families

Usually reference or keep global:

- `audit-docs`: docs routing, duplication, stale guidance, ownership, maintenance.
- `audit-skills`: trigger quality, brevity, DRYness, `SKILL.md` vs `references/` vs `scripts/`.
- `improve-ai-self`: repeated agent failure analysis and durable guidance/script fixes.
- `brainstorm-app-idea`: early product discovery before repo standards or implementation planning.

Default placement:

- personal/global unless target-repo paths or team-shared rules materially change the workflow.
- repo-local only when the team wants the behavior versioned with the repo.

## Cuticly-Style Skill Families

Use as source patterns, not defaults:

- Planning: `plan-implementation-work`, `review-implementation-plan`.
- Execution: `implement-planned-work`, `resolve-bug`.
- Review: `review-changed-code`, review gates for PRD/backlog/plan.
- Orchestration: `orchestrate-work-plan`, `orchestrate-mvp-delivery`.
- File-based product/backlog: `draft-follow-on-prd`, `draft-backlog-slices`, backlog review.
- Repo standards: `audit-standards-docs`, `audit-skill-opportunities`, architecture cleanup planning.
- Validation: `validate-ui-in-browser`, UI/UX audit, screenshots/artifacts.
- Product release notes: `update-whats-new-docs`.
- Domain implementation helpers: vertical-slice feature patterns.

Copy only the compact skill contract and useful gates. Do not copy product domain, provider setup, file paths, personas, Auth0/Azure/AppHost details, MVP cursor policy, or file-based backlog assumptions unless the target repo chooses them.

## Workflow Mode Questions

Ask before proposing orchestration or work-tracking skills:

- Work source: external tracker, file backlog, PRD tree, chat-only, or none?
- Scope unit: one ticket at a time, one slice at a time, capability, MVP cursor, or release train?
- State location: tracker comments, repo files, temp tracking only, or no durable state?
- Review gates: changed-code only, plan review, docs review, PRD/backlog review, or none?
- Validation gates: local command matrix, browser/API/CLI/job/deployed smoke, or manual owner check?
- Commit/PR behavior: agent may commit, draft PR only, user-owned, or no git actions?
- Stop rule: ask on ambiguity, continue around blocked tasks, or stop after one ticket?

## Common Variants

Prefer these variants over copying a source workflow wholesale:

- `one-ticket`: plan and implement exactly one tracker item; update tracker; no file backlog.
- `one-slice`: file-backed or tracker-backed slice with plan, validation, review, and handoff.
- `docs-only`: audit/update docs and routes; no code workflow.
- `bugfix`: reproduce, minimal fix, regression coverage, focused validation, changed-code review.
- `external-tracker`: tracker owns state; repo may have only `docs/development/work-tracking.md`.
- `file-backlog`: repo owns backlog, plans, workflows, artifacts; use only after approval.
- `no-orchestration`: create route docs, validation docs, and review skill only.
- `MVP-cursor`: full capability sequencing; use only when explicitly requested.

## Recommendation Shape

When proposing skill/reference adoption, return a small table:

| Source pattern | Target decision | Placement | Why | Creation method |
| --- | --- | --- | --- | --- |
| `review-changed-code` | adapt | repo-local | repeated code review against repo standards | `skills` scaffold |
| `orchestrate-mvp-delivery` | skip | ignore | target wants one ticket at a time | none |
| `audit-docs` | reference global | user/global | useful across repos, no target-specific paths | none |

Keep the source skill as evidence. Make the target repo's workflow the decision.

For each proposed skill, include placement and creation method in the manifest:

- placement: `repo-local`, `user/global`, `ignore`, or `defer`
- creation method: scaffold set, `copy_skill_package.py`, `skill-creator`, or none
