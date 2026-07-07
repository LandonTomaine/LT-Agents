# Repo-Local Skills

Load when proposing, creating, auditing, or migrating repo-local skills.

## Paths

- Preferred repo path: `.agents/skills/<skill-name>/`.
- User/global paths: active skill list, `$CODEX_HOME/skills`, or `$HOME/.codex/skills`.
- Legacy repo path to detect: `.codex/skills/<skill-name>/`.
- Do not create `.codex/skills` for new bootstraps unless the user explicitly chooses that path.
- Route repo-local skills from `agent-rules/README.md`; add a `.agents/README.md` only when the repo has a real need for that folder index.

## Creation

- Create a repo-local skill only when the workflow is repo-specific, repeated, multi-step, narrow, and not covered by shared docs or global skills.
- Ask placement for every candidate skill: `repo-local`, `user/global`, `ignore`, or `defer`.
- Use the user's `skill-creator` for new custom skills and target `.agents/skills`.
- The standard starter skill is `review-changed-code`; scaffold it only after approval and only if no equivalent exists.
- Consider `update-documentation` when docs updates are repeated, repo-specific, and tied to repo routes, authoritative docs, standards, commands, product behavior, validation, or deployment rules.
- Keep starter skills minimal when repo standards are still TODO-heavy.
- Put heavy checklists in `references/` and repeatable deterministic work in `scripts/`.
- Default to the smallest useful unit. Do not propose a whole skill suite when one focused skill or one route doc would cover the need.

## Candidate Skill Decision Checklist

Use one row per candidate before adding it to the manifest:

| Field | Required answer |
| --- | --- |
| Candidate skill | Name or workflow family. |
| Trigger | Exact task or user wording that should invoke it. |
| Evidence | Repo files, repeated workflow, or user confirmation proving recurrence. |
| Repo-specific inputs | Paths, commands, standards, validation, auth, deployment, routes, or tracker behavior. |
| Why docs are not enough | Procedural complexity that justifies a skill. |
| Existing global/source equivalent | Use global, copy shape, adapt, reference only, or skip. |
| Placement | `repo-local`, `user/global`, `ignore`, or `defer`. |
| Shape | scaffold set, copied package, custom skill, or no file. |
| References/scripts needed | What keeps `SKILL.md` short and deterministic. |
| Approval | `approved`, `rejected`, or `defer`. |

Decision rules:

- `repo-local`: all creation tests pass and the repo needs versioned paths, commands, standards, or team-shared behavior.
- `user/global`: useful across repos and not materially tied to target repo files or rules.
- `ignore`: broad, speculative, covered elsewhere, or not useful for this repo.
- `defer`: fit, recurrence, or ownership is unresolved; record owner or trigger.
- Docs only: the workflow is mostly policy plus a short command route.
- No skill package can be proposed without a placement answer.
- No placeholder skill for a deferred decision.

Compact standard skill shape:

- narrow trigger
- `Primary lens`
- optional `Invoked by` and `Delegates to`
- short `Goal`
- concrete `Workflow`
- explicit `Output`
- `Do Not` only for likely mistakes

Standard scaffold sets:

- `skills`: starter `review-changed-code`
- `implementation-skills`: separate planning, implementation, plan review, and bug resolution skills
- `orchestration-skill`: resumable work-plan orchestration
- `docs-audit-skills`: separate standards docs audit, skill-opportunity audit, and docs update skills
- `ui-validation-skill`: browser validation for confirmed UI repos only

Use `scripts/scaffold_backbone.py <repo> --mode draft --set <set> --only <path-or-skill-folder>` for individual approved draft candidates. Omit `--only` only when every generated file in the set is approved.

Use `scripts/copy_skill_package.py <source-skill-dir> <repo> --mode draft` for approved existing package copies. Use `skill-creator` for custom repo-specific skills.

When the user points to global skills or a source repo such as Cuticly, load [source-skill-patterns.md](source-skill-patterns.md). Treat those skills as side references unless the user approves a target-specific copy or adaptation.

When adapting a source skill:

- copy the compact contract, not the whole operating system
- preserve narrow boundaries like intake, review, planning, implementation, and orchestration instead of recombining them
- drop source-repo product language, tracker assumptions, personas, and environment details
- split oversized source workflows into smaller repo-local skills or docs when that fits the target better

## Standard Optional Capabilities

Ask whether these capabilities should be repo-local, user/global, ignored, or deferred:

- `triage-work-intake`: capture and route incoming work without planning or implementing it.
- `pick-next-work-item`: choose one next work target from an approved tracker or backlog.
- `audit-skills`: review skills for trigger quality, brevity, DRYness, and resource placement.
- `improve-ai-self`: turn repeated agent failures or bad assumptions into updated guidance, skills, scripts, or docs.
- `update-documentation`: update or propose updates to repo docs and agent routes when code, commands, product behavior, architecture, validation, deployment, or standards change.
- `plan-implementation-work`: turn ambiguous work into a short executable task plan.
- `review-implementation-plan`: review a plan before coding.
- `implement-planned-work`: execute an approved plan through validation and review.
- `orchestrate-work-plan`: advance approved work through a resumable task queue.
- `resolve-bug`: reproduce, fix, and validate a concrete defect.
- `review-changed-code`: review the current diff only.

When asking the user about any skill candidate, include the description, placement options, and likely target path or no-file outcome. Do not ask with unexplained skill names.

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
- Do not copy a source-repo skill just because it worked elsewhere.
- Do not combine intake, selection, planning, implementation, and review into one generated skill unless the user explicitly wants a single orchestrator.
- If user/global is selected and the skill already exists globally, route or mention the capability without creating files.
- If repo-local is selected, use `skill-creator` and tailor the skill to the target repo.
- If copying an existing package is approved, draft it with `copy_skill_package.py`, then tailor repo-specific content before apply.
- Prefer one copied or generated skill at a time. Add the next one only after the first proves useful.
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
