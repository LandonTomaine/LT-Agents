# Documentation Maintenance

Load when asking, resolving, or proposing documentation maintenance, docs update workflows, stale-doc prevention, docs review rules, standards TODOs, or docs-update skills.

## Policy

- Creating docs is not enough. Ask how they stay current.
- Find existing documentation maintenance rules first. Do not duplicate them.
- Keep human-facing docs useful to humans; use agent files only for routing and agent behavior.
- Keep standards TODOs separate from product backlog unless the user explicitly chooses one shared tracker.
- Do not create a docs-update skill unless the workflow is repeated, repo-specific, and too procedural for short documentation.

## Documentation Maintenance Questions

Ask enough to make docs updates executable:

- Which changes require docs updates: product behavior, setup/run commands, deploy/release process, env vars/secrets, architecture boundaries, standards, API contracts, UI flows, migrations, or external integrations?
- Who owns doc accuracy?
- Where should docs maintenance rules live?
- Should PR/review guidance require checking related docs?
- Should agents update docs in the same change, propose doc updates separately, or ask first?
- Which docs are authoritative versus historical notes, planning artifacts, or examples?
- How should stale, duplicated, or conflicting docs be handled?
- What docs should never be overwritten without explicit review?

## Docs To Propose

Prefer existing docs when adequate. Otherwise use:

- `docs/development/documentation.md`: documentation ownership, update triggers, stale-doc prevention, authoritative source rules, and docs review expectations.

For tiny repos, a short `README.md` or `CONTRIBUTING.md` section may be enough if it is easy to find.

## Standards Adoption Roadmap

Ask whether the repo wants a non-product TODO/roadmap for standards and quality work found during bootstrap.

Use it for deferred or phased items such as:

- formatter/linter/static-analysis setup
- architecture tests or source guards
- CI and local hook adoption
- dependency, license, vulnerability, and secret checks
- generated-file cleanliness checks
- test-layer gaps
- validation, local setup, deployment, or docs-maintenance follow-ups
- migration of legacy agent/skill paths

Default path when approved:

- `docs/development/standards-roadmap.md`

Rules:

- Do not create this file by default.
- Do not use it as a feature backlog unless the user explicitly chooses that workflow.
- If details are known and approved, write real checklist items. If details are deferred, use a short TODO placeholder.
- Mark each item with enough context to act later: area, proposed action, status, owner or trigger, and source/evidence when known.

## Docs-Update Skill Candidate

Offer a focused `update-documentation` repo-local skill when docs maintenance is repeated and repo-specific.

Explain it to the user:

- `update-documentation`: updates or proposes updates to the repo's human docs and agent routes when code, commands, product behavior, architecture, validation, deployment, or standards change. It checks authoritative docs, avoids duplicate guidance, and reports stale or missing docs.

Ask whether it should be repo-local, user/global, ignored, or deferred.

If repo-local is approved:

- Use `skill-creator`.
- Target `.agents/skills/update-documentation`.
- Tailor triggers to the repo's docs, indexes, ownership rules, and review expectations.
- Keep detailed checklists in `references/` if needed.
- Do not let the skill silently rewrite broad docs; require targeted updates or a manifest when scope is broad.

## Manifest Requirements

Every documentation-maintenance proposal must include:

- path or skill name
- create/update/skip/defer/reject
- purpose and audience
- authoritative docs affected
- maintenance triggers or TODO categories
- routes/indexes that must be updated
- unresolved questions, if explicitly deferred
