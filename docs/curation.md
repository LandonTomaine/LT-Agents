# Curation Guide

Use this repository as a collection of durable agent knowledge, not as a scratchpad.

## Layout

- `skills/<name>/SKILL.md`: primary skill instructions and trigger.
- `skills/<name>/references/`: supporting material selected by the skill.
- `skills/<name>/scripts/`: deterministic helpers.
- `skills/<name>/agents/`: optional metadata for agent UIs or catalogs.
- `docs/`: collection-level operating notes.
- `scripts/`: collection-level validation and maintenance helpers.

Only direct children of `skills/` are raw installable skill packages. Nested `references/`, `scripts/`, and `agents/` folders belong to their parent package.

For broad public distribution, prefer a Codex plugin with `.codex-plugin/plugin.json`. Use raw skill-folder install docs for local testing, private sharing, or early public catalogs.

## Standards

- Prefer small, explicit files over large manuals.
- Keep trigger descriptions concrete enough that Codex can decide when to load the skill.
- Move detailed variants, checklists, and templates out of `SKILL.md` into references.
- Use scripts for repeatable filesystem work instead of asking an agent to retype boilerplate.
- Keep private assumptions out of reusable instructions.

## Review Checklist

- The skill name matches the directory name.
- `SKILL.md` has a clear description and workflow.
- Referenced files exist and are reachable by relative path.
- Scripts are deterministic and safe by default.
- The package can be copied into a Codex skills directory without depending on repository-level files.
- `python scripts\validate_skills.py` passes from the repository root.

## Maintenance Triggers

Update repository docs when:

- a skill is added, renamed, removed, or materially repurposed
- a skill package gains or loses `references/`, `scripts/`, or `agents/`
- install, sync, validation, or publishing expectations change
- git commit, branch, review, or push expectations change
- a repo-level convention moves between `README.md`, `AGENTS.md`, `docs/`, or a skill package
- copied global skills diverge from the source version intentionally

When a skill changes, check:

- trigger text still describes when to use the skill
- references are linked only when they should be loaded
- scripts are still safe for their advertised mode
- examples do not depend on private local paths
- `README.md` and `skills/README.md` still route humans to the right package
- public install instructions still list every direct `skills/<name>/` package and no package internals
- public distribution language distinguishes raw skill-folder install from plugin packaging

Stale or conflicting guidance should be fixed at the narrowest useful level. Prefer updating the authoritative doc and routing to it over duplicating the same rule in multiple files.
