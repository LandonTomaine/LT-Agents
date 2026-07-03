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

- [`bootstrap-repo-standards`](skills/bootstrap-repo-standards/SKILL.md): Inspect a repository, interview for missing context, and guide standards, docs, validation, and agent-rule setup before durable changes are written.

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
