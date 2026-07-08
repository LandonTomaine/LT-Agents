# Skills

This directory contains self-contained Codex skill packages.

## Plugin Quickstart

Install the repository root as a Codex plugin. The root manifest `.codex-plugin/plugin.json` points to `./skills/`, so the plugin includes every direct child skill package and its nested `references/`, `scripts/`, and `agents/` files.

Restart Codex, then run from the target repo:

```text
Use $bootstrap-repo-standards to bootstrap this repo.
```

## Raw Skill Quickstart

Raw install remains useful for local testing or installing one skill:

```text
$skill-installer install https://github.com/LandonTomaine/LT-Agents/tree/main/skills/bootstrap-repo-standards
```

Restart Codex, then run from the target repo:

```text
Use $bootstrap-repo-standards to bootstrap this repo.
```

## Public Skill Packages

Each direct child directory is a raw installable skill package for local use with `$skill-installer`. Nested `references/`, `scripts/`, and `agents/` folders are package internals.

| Skill | Purpose | Prerequisites |
| --- | --- | --- |
| [`audit-docs`](audit-docs/SKILL.md) | Review documentation systems for drift, duplication, missing routes, and unclear maintenance rules. | Git and `rg` recommended. |
| [`audit-skills`](audit-skills/SKILL.md) | Review skills for trigger quality, brevity, DRYness, and resource placement. | Git and `rg` recommended. |
| [`audit-work-tracking`](audit-work-tracking/SKILL.md) | Review backlog, tracker, status vocabulary, routing, artifact, and closeout systems. | Git and `rg` recommended. |
| [`bootstrap-repo-standards`](bootstrap-repo-standards/SKILL.md) | Bootstrap or overhaul repo standards through scan, interview, checklist, manifest approval, docs, validation, quality gates, and repo-local skill decisions. | Python 3 required for bundled scripts; Git and `rg` recommended. |
| [`ship-change`](ship-change/SKILL.md) | Implement a repo change end to end, validate it, and commit/push only after approval. | Git required for commit/push; repo validation commands as documented by the target repo. |

Install from GitHub with:

```text
$skill-installer install https://github.com/LandonTomaine/LT-Agents/tree/main/skills/<skill-name>
```

Then invoke with `$<skill-name>`, for example:

```text
Use $bootstrap-repo-standards to bootstrap this repo.
```

For broad public distribution, use the root Codex plugin manifest. Raw skill folders are still useful for local installation, testing, and private sharing.

## Adding Skills

Create a new directory under `skills/` with this minimum shape:

```text
skills/
  skill-name/
    SKILL.md
```

Use `references/`, `scripts/`, and `agents/` only when the skill needs them.

Before committing, run:

```powershell
python scripts\validate_skills.py
```
