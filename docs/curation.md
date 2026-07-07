# Curation Guide

Use this repository as a collection of durable agent knowledge, not as a scratchpad.

## Layout

- `skills/<name>/SKILL.md`: primary skill instructions and trigger.
- `skills/<name>/references/`: supporting material selected by the skill.
- `skills/<name>/scripts/`: deterministic helpers.
- `skills/<name>/agents/`: optional metadata for agent UIs or catalogs.
- `.codex-plugin/plugin.json`: plugin manifest for standard Codex plugin installs.
- `docs/`: collection-level operating notes.
- `scripts/`: collection-level validation and maintenance helpers.

The plugin manifest points to `./skills/`, so plugin installs include each direct child skill package plus nested `references/`, `scripts/`, and `agents/` folders. Those nested folders belong to their parent package and are not separate public skills.

Raw skill-folder install docs remain useful for local testing, private sharing, or installing a single skill.

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
- `python scripts\validate_plugin.py` passes when plugin metadata or packaged files change.

## Maintenance Triggers

Update repository docs when:

- a skill is added, renamed, removed, or materially repurposed
- a skill package gains or loses `references/`, `scripts/`, or `agents/`
- install, sync, validation, or publishing expectations change
- plugin metadata, package paths, or included skill folders change
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
- plugin docs still say nested skill `references/`, `scripts/`, and `agents/` are included through `"skills": "./skills/"`

Stale or conflicting guidance should be fixed at the narrowest useful level. Prefer updating the authoritative doc and routing to it over duplicating the same rule in multiple files.
