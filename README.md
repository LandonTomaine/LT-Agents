# LT Agents

Private catalog of reusable Codex skills, agent instructions, references, and maintenance notes.

This repository is organized as a durable home for reusable agent knowledge. Each skill is kept as a self-contained package under `skills/`, with repository-level docs used only for indexing, contribution rules, and collection-wide conventions.

## Quickstart: Run The Bootstrapper

Prerequisites:

- Codex with skill support
- GitHub access to this repo
- Network access for `$skill-installer`
- Python 3 available to Codex for `bootstrap-repo-standards`

Install:

```text
$skill-installer install https://github.com/LandonTomaine/LT-Agents/tree/main/skills/bootstrap-repo-standards
```

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

Manual install after cloning:

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

## Public Skill Packages

This repo currently publishes raw Codex skill folders for local install with `$skill-installer`. Codex's preferred distribution unit for reusable public packages is a plugin; these folders are local-install packages until this repo adds plugin manifests.

Installable raw skills live only at `skills/<skill-name>/`. Files under a skill's `references/`, `scripts/`, or `agents/` folders are package internals, not separate public skills.

| Skill | What It Does | Invoke |
| --- | --- | --- |
| [`audit-docs`](skills/audit-docs/SKILL.md) | Audits repo docs and indexes for stale content, duplication, missing routes, ownership gaps, and maintenance clarity. | `Use $audit-docs to review the docs.` |
| [`audit-skills`](skills/audit-skills/SKILL.md) | Reviews Codex skills for trigger quality, brevity, DRYness, progressive disclosure, and resource placement. | `Use $audit-skills to review this skill.` |
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

For broad public distribution, package one or more skills as a Codex plugin with `.codex-plugin/plugin.json` and a plugin-root `skills/` directory. Use raw skill-folder install for local setup, testing, and private sharing; use plugins when the package should be discoverable, versioned, and installable as a reusable product.

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

GitHub Actions runs the same validation on pushes and pull requests.

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

## License

MIT. See `LICENSE`.
