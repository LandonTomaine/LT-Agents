# Repo-Local Skills

Load when proposing, creating, auditing, or migrating repo-local skills.

## Paths

- Preferred repo path: `.agents/skills/<skill-name>/`.
- Preferred user path: `$HOME/.agents/skills/<skill-name>/`.
- Legacy repo path to detect: `.codex/skills/<skill-name>/`.
- Do not create `.codex/skills` for new bootstraps unless the user explicitly chooses that path.
- Route repo-local skills from `agent-rules/README.md`; add a `.agents/README.md` only when the repo has a real need for that folder index.

## Creation

- Create a repo-local skill only when the workflow is repo-specific, repeated, multi-step, narrow, and not covered by shared docs or global skills.
- Use the user's `skill-creator` for new custom skills and target `.agents/skills`.
- The standard starter skill is `review-changed-code`; scaffold it only after approval and only if no equivalent exists.
- Consider `update-documentation` when docs updates are repeated, repo-specific, and tied to repo routes, authoritative docs, standards, commands, product behavior, validation, or deployment rules.
- Keep starter skills minimal when repo standards are still TODO-heavy.
- Put heavy checklists in `references/` and deterministic helpers in `scripts/`.

## Standard Optional Capabilities

Ask whether these capabilities should be repo-local, user/global, ignored, or deferred:

- `audit-skills`: review skills for trigger quality, brevity, DRYness, and resource placement.
- `improve-ai-self`: turn repeated agent failures or bad assumptions into updated guidance, skills, scripts, or docs.
- `update-documentation`: update or propose updates to repo docs and agent routes when code, commands, product behavior, architecture, validation, deployment, or standards change.

When asking the user, include the descriptions. Do not ask with unexplained skill names.

Use this compact shape:

- `audit-skills`: reviews skills for trigger quality, brevity, DRYness, and whether content belongs in `SKILL.md`, `references/`, or `scripts/`. Should this be repo-local, user/global, ignored, or deferred?
- `improve-ai-self`: analyzes repeated agent failures or bad assumptions and turns them into updated guidance, skills, scripts, or docs. Should this be repo-local, user/global, ignored, or deferred?
- `update-documentation`: updates or proposes updates to the repo's human docs and agent routes when code, commands, product behavior, architecture, validation, deployment, or standards change. Should this be repo-local, user/global, ignored, or deferred?

Decision options:

- `repo-local`: create or adapt under `.agents/skills` when the workflow needs target-repo standards, paths, or team-shared behavior.
- `user/global`: keep or install as a personal skill when the workflow should apply across repos.
- `ignore`: do not add or route this capability for this repo.
- `defer`: record the decision as open; do not scaffold a placeholder skill.

Rules:

- Do not copy a global skill into the repo just because it exists.
- If user/global is selected and the skill already exists globally, route or mention the capability without creating files.
- If repo-local is selected, use `skill-creator` and tailor the skill to the target repo.
- For `update-documentation`, tailor triggers to the repo's authoritative docs, stale-doc rules, route indexes, and review expectations.
- If ignored, leave it out of the manifest except for a short rejected/deferred decision note.

## Migration

Offer migration when `.codex/skills` exists:

- `keep`: leave legacy skills in place and route them as-is.
- `migrate`: copy or move approved skills to `.agents/skills`.
- `support both`: keep both paths temporarily and document the transition.

Before migration:

1. Run `scripts/check_skill_migration.py <repo>`.
2. Check for target-name conflicts in `.agents/skills`.
3. Check docs and skill files for `.codex/skills` references.
4. Check sibling-skill relative links if only some skills are moving.
5. Show an exact path/action manifest.

Migration rules:

- Preserve existing skill contents unless the user approves edits.
- Update routes and path references in the same approved batch.
- Validate migrated skills with the available skill validator.
- Do not delete the legacy copy until the migrated skill works and the user approves removal.
