# LT Agents

Public catalog of reusable Codex skills, agent instructions, references, and maintenance notes.

This repository is organized as a durable home for reusable agent knowledge. Each skill is kept as a self-contained package under `skills/`, with repository-level docs used only for indexing, contribution rules, and collection-wide conventions.

## Quickstart: Run The Bootstrapper

Prerequisites:

- Codex with plugin and skill support
- GitHub access to this repo
- Python 3 available to Codex for `bootstrap-repo-standards`

Install this repository as a Codex plugin from its GitHub source. The plugin manifest is `.codex-plugin/plugin.json` and includes all skill packages under `./skills/`, including nested `references/`, `scripts/`, and `agents/` files.

Restart Codex.

Run it from the repo you want to bootstrap:

```text
Use $bootstrap-repo-standards to bootstrap this repo.
```

What happens:

1. Scans the repo read-only.
2. Builds a checklist of present, missing, deferred, rejected, or not-applicable standards.
3. Asks targeted questions.
4. Proposes an exact file/action manifest.
5. Writes only approved files.

Raw single-skill install remains available for local testing:

```text
$skill-installer install https://github.com/LandonTomaine/LT-Agents/tree/main/skills/bootstrap-repo-standards
```

Manual raw install after cloning:

```powershell
git clone https://github.com/LandonTomaine/LT-Agents.git
Set-Location .\LT-Agents

$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
$skillsDir = Join-Path $codexHome "skills"
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
Copy-Item -Recurse -Force .\skills\bootstrap-repo-standards $skillsDir
```

Restart Codex, open the target repo, then run:

```text
Use $bootstrap-repo-standards to bootstrap this repo.
```

## Contents

| Path | Purpose |
| --- | --- |
| `skills/` | Installable or reusable Codex skill packages. |
| `docs/` | Collection-level notes, curation standards, and operating conventions. |
| `scripts/` | Catalog maintenance and validation helpers. |
| `AGENTS.md` | Instructions for Codex agents working in this repository. |

## Plugin Install

This repository is packaged as a Codex plugin. The plugin manifest lives at `.codex-plugin/plugin.json` and points to `./skills/`, so each skill package includes its nested `references/`, `scripts/`, and `agents/` files when installed as a plugin.

Install the plugin from this repository using Codex's standard plugin install flow for a GitHub plugin source. After install, restart Codex if needed and invoke the included skills by name, for example:

```text
Use $bootstrap-repo-standards to bootstrap this repo.
```

## Public Skill Packages

The plugin publishes these skills from `skills/<skill-name>/`. Raw skill-folder install with `$skill-installer` is still useful for local testing or installing a single skill.

Installable raw skills live only at `skills/<skill-name>/`. Files under a skill's `references/`, `scripts/`, or `agents/` folders are package internals, not separate public skills.

| Skill | What It Does | Invoke |
| --- | --- | --- |
| [`audit-docs`](skills/audit-docs/SKILL.md) | Audits repo docs and indexes for stale content, duplication, missing routes, ownership gaps, and maintenance clarity. | `Use $audit-docs to review the docs.` |
| [`audit-skills`](skills/audit-skills/SKILL.md) | Reviews Codex skills for trigger quality, brevity, DRYness, progressive disclosure, and resource placement. | `Use $audit-skills to review this skill.` |
| [`audit-work-tracking`](skills/audit-work-tracking/SKILL.md) | Reviews backlog, tracker, status vocabulary, routing, artifact, and closeout systems for drift or unnecessary token cost. | `Use $audit-work-tracking to review this repo's backlog workflow.` |
| [`bootstrap-repo-standards`](skills/bootstrap-repo-standards/SKILL.md) | Scans a target repo, interviews for product/architecture/tooling decisions, proposes docs, agent rules, validation, quality gates, and repo-local skills, then writes only approved files. | `Use $bootstrap-repo-standards to bootstrap this repo.` |
| [`ship-change`](skills/ship-change/SKILL.md) | Takes a repo change from request through analysis, implementation, validation, handoff, and optional approved commit/push. | `Use $ship-change to make this repo change.` |

## Skill Package Shape

Skill packages should stay portable and easy to install:

- `SKILL.md` contains the trigger, purpose, gates, and workflow.
- `references/` contains longer guidance loaded only when relevant.
- `scripts/` contains deterministic helpers used by the skill.
- `agents/` contains UI or marketplace metadata when needed.

## Install Other Skills

Install one skill with Codex's skill installer:

```text
$skill-installer install https://github.com/LandonTomaine/LT-Agents/tree/main/skills/<skill-name>
```

Current install URLs:

```text
$skill-installer install https://github.com/LandonTomaine/LT-Agents/tree/main/skills/audit-docs
$skill-installer install https://github.com/LandonTomaine/LT-Agents/tree/main/skills/audit-skills
$skill-installer install https://github.com/LandonTomaine/LT-Agents/tree/main/skills/audit-work-tracking
$skill-installer install https://github.com/LandonTomaine/LT-Agents/tree/main/skills/bootstrap-repo-standards
$skill-installer install https://github.com/LandonTomaine/LT-Agents/tree/main/skills/ship-change
```

Manual local install after cloning this repo:

```powershell
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
$skillsDir = Join-Path $codexHome "skills"
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
Copy-Item -Recurse -Force .\skills\<skill-name> $skillsDir
```

Install every skill in this repo:

```powershell
$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
$skillsDir = Join-Path $codexHome "skills"
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
Get-ChildItem .\skills -Directory | ForEach-Object {
  Copy-Item -Recurse -Force $_.FullName $skillsDir
}
```

Restart Codex after installing or updating skills. `$skill-installer` installs into `$CODEX_HOME/skills` by default. Repo-scoped checked-in skills for a target project belong under that project's `.agents/skills`.

## Plugin Distribution

For broad public distribution, use the root Codex plugin manifest. Keep raw skill-folder install docs for local setup, testing, and private sharing.

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

Run the catalog validator:

```powershell
python scripts\validate_skills.py
```

Run plugin validation when plugin metadata or packaged skills change:

```powershell
python scripts\validate_plugin.py
```

GitHub Actions runs the same skill and plugin validation on pushes and pull requests.

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
- Push to `origin/main` for normal catalog updates unless a larger change needs review on a branch first.
- Use a branch for broad rewrites, new multi-file skills, migrations, or anything that should be reviewed before landing on `main`.
- Do not rewrite published history unless explicitly approved.

For agent-driven changes, report:

- files changed
- validation performed
- commit SHA, if committed
- push target, if pushed

## License

MIT. See `LICENSE`.
