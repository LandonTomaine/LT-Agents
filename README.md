# LT Agents

Private collection of Codex skills, agent instructions, references, and maintenance notes.

This repository is organized as a durable home for reusable agent knowledge. Each skill is kept as a self-contained package under `skills/`, with repository-level docs used only for indexing, contribution rules, and collection-wide conventions.

## Contents

| Path | Purpose |
| --- | --- |
| `skills/` | Installable or reusable Codex skill packages. |
| `docs/` | Collection-level notes, curation standards, and operating conventions. |
| `AGENTS.md` | Instructions for Codex agents working in this repository. |

## Skills

- [`audit-docs`](skills/audit-docs/SKILL.md): Lightweight documentation audit workflow for drift, duplication, missing routes, and maintenance clarity.
- [`audit-skills`](skills/audit-skills/SKILL.md): Review skills for trigger quality, brevity, DRYness, and resource placement.
- [`bootstrap-repo-standards`](skills/bootstrap-repo-standards/SKILL.md): Inspect a repository, interview for missing context, and guide standards, docs, validation, and agent-rule setup before durable changes are written.
- [`ship-change`](skills/ship-change/SKILL.md): Lightweight workflow for analyzing, planning, implementing, validating, then committing and pushing after approval.

## Skill Package Shape

Skill packages should stay portable and easy to install:

- `SKILL.md` contains the trigger, purpose, gates, and workflow.
- `references/` contains longer guidance loaded only when relevant.
- `scripts/` contains deterministic helpers used by the skill.
- `agents/` contains UI or marketplace metadata when needed.

## Local Use

To use a skill from this repo, copy or sync the skill directory into your Codex skills directory, for example:

```powershell
Copy-Item -Recurse -Force .\skills\bootstrap-repo-standards $env:USERPROFILE\.codex\skills\
```

Keep the package directory name stable because Codex uses it as part of skill discovery.

## Maintaining This Repo

For humans:

- Add or update skills under `skills/<skill-name>/`.
- Keep each skill portable; it should work when copied without the rest of this repo.
- Update this README and `skills/README.md` whenever a skill is added, renamed, removed, or materially repurposed.
- Keep collection-level guidance in `docs/`; keep skill runtime guidance inside the skill package.
- Review skill changes before publishing so trigger text, references, and scripts stay aligned.

For agents:

- Start with `AGENTS.md`, then use this README and `docs/curation.md` as the repo map.
- Preserve package boundaries and avoid broad formatting churn in copied skill files.
- When changing a skill, check that every referenced `references/`, `scripts/`, or `agents/` file still exists.
- When adding repo-level guidance, prefer short human-readable docs over agent-only rules.
- Do not create durable files, repo-local skills, hooks, CI, or standards roadmaps without an explicit path/action manifest and approval.

## Validation

This repo has no app runtime, dependency install, build, or test suite today. For normal documentation or skill edits, validate with:

```powershell
git status --short
rg --files
```

For skill package changes, also verify:

- `SKILL.md` exists at the package root.
- The skill directory name matches the skill name.
- Relative links and referenced files resolve.
- Scripts are safe by default and documented from the skill or references that use them.

## Git Workflow

Use small, intentional commits. A normal change flow is:

```powershell
git status --short
git diff
git add <paths>
git commit -m "Describe the repo or skill change"
git push
```

Guidelines:

- Commit only the files that belong to the current change.
- Review `git diff` before staging.
- Use clear commit messages that name the changed skill or repo guidance.
- Keep copied upstream/global skill updates separate from local repo curation changes when practical.
- Push to `origin/main` for normal private-repo updates unless a larger change needs review on a branch first.
- Use a branch for broad rewrites, new multi-file skills, migrations, or anything that should be reviewed before landing on `main`.
- Do not rewrite published history unless explicitly approved.

For agent-driven changes, report:

- files changed
- validation performed
- commit SHA, if committed
- push target, if pushed
