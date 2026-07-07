# Source Skill Patterns

Load when the user wants bootstrap to compare, adapt, migrate, or copy ideas from existing global or source-repo skills.

This is a pattern catalog, not a default manifest. Source skills are side references. Use them to ask better questions and draft better options, not to force a target repo into another repo's workflow.

Bias toward smaller adaptations. If a source skill became leaner and more focused, preserve that. If it is still too broad for the target repo, split the idea instead of copying the whole package.

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
8. Prefer one focused adaptation over importing a family of related skills at once.

## Global Skill Families

Usually reference or keep global:

- `audit-docs`: docs routing, duplication, stale guidance, ownership, maintenance.
- `audit-skills`: trigger quality, brevity, DRYness, `SKILL.md` vs `references/` vs `scripts/`.
- `improve-ai-self`: repeated agent failure analysis and durable guidance/script fixes.
- `brainstorm-app-idea`: early product discovery before repo standards or implementation planning.

Default placement:

- personal/global unless target-repo paths or team-shared rules materially change the workflow.
- repo-local only when the team wants the behavior versioned with the repo.

## Cuticly-Derived Workflow Families

Use as source patterns, not defaults:

- Intake and routing: `triage-backlog-intake`, `pick-next-backlog-item`.
- Product shaping: `draft-follow-on-prd`, `review-product-prd`, `draft-backlog-slices`, `review-backlog-slices`.
- Planning: `plan-implementation-work`, `review-implementation-plan`.
- Execution: `implement-planned-work`, `resolve-bug`.
- Review: `review-changed-code`.
- Orchestration: `orchestrate-work-plan`, `orchestrate-mvp-delivery`.
- Repo standards: `audit-standards-docs`, `audit-skill-opportunities`, architecture cleanup planning.
- Validation: `validate-ui-in-browser`, UI/UX audit, screenshots/artifacts.
- Product release notes: `update-whats-new-docs`.
- Product preview/comms: lightweight "what is coming next" or release-preview planning that informs stakeholders without becoming the execution queue.
- Domain implementation helpers: vertical-slice feature patterns.

Copy only the compact skill contract and useful gates. Do not copy product domain, provider setup, file paths, personas, Auth0/Azure/AppHost details, MVP cursor policy, or file-based backlog assumptions unless the target repo chooses them.

Common downsizing moves:

- split intake/routing from planning
- split PRD review, backlog review, and plan review into separate gates
- split planning from implementation when the source skill merged them
- split stakeholder comms from executable backlog handling
- convert review gates into a small reference doc when they are mostly policy
- keep orchestration optional unless the repo already works that way
- keep implementation skills ignorant of queue/cursor state unless called by an orchestrator
- keep orchestrators responsible for state reconciliation, not implementation internals

## Workflow Mode Questions

Ask before proposing orchestration or work-tracking skills:

- Work source: external tracker, file backlog, PRD tree, chat-only, or none?
- Scope unit: one ticket at a time, one slice at a time, capability, MVP cursor, or release train?
- State location: tracker comments, repo files, temp tracking only, or no durable state?
- Review gates: changed-code only, plan review, docs review, PRD/backlog review, or none?
- Validation gates: local command matrix, browser/API/CLI/job/deployed smoke, or manual owner check?
- Communication docs: none, release notes, what-is-next preview, roadmap, or stakeholder handoff?
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
- `preview-comms`: stakeholder-facing upcoming-work or release-preview doc; keep separate from executable task state.
- `no-orchestration`: create route docs, validation docs, and review skill only.
- `MVP-cursor`: full capability sequencing; use only when explicitly requested.

Default preference order:

1. `docs-only` or `one-ticket`
2. `bugfix` or `external-tracker`
3. `one-slice`
4. `file-backlog`
5. `preview-comms`
6. `no-orchestration`
7. `MVP-cursor`

Skill boundary defaults:

- Intake skill: classify and route only.
- Selection skill: choose one next target only.
- Planning skill: produce an executable task list only.
- Review skill: return findings only.
- Implementation skill: execute an approved plan or handoff only.
- Validation skill: prove one confirmed surface only.
- Orchestrator: own queue state and handoffs, then delegate.

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
