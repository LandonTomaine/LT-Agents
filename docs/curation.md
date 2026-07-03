# Curation Guide

Use this repository as a collection of durable agent knowledge, not as a scratchpad.

## Layout

- `skills/<name>/SKILL.md`: primary skill instructions and trigger.
- `skills/<name>/references/`: supporting material selected by the skill.
- `skills/<name>/scripts/`: deterministic helpers.
- `skills/<name>/agents/`: optional metadata for agent UIs or catalogs.
- `docs/`: collection-level operating notes.

## Standards

- Prefer small, explicit files over large manuals.
- Keep trigger descriptions concrete enough that Codex can decide when to load the skill.
- Move detailed variants, checklists, and templates out of `SKILL.md` into references.
- Use scripts for repeatable filesystem work instead of asking an agent to retype boilerplate.
- Keep private assumptions out of reusable instructions unless the repository is explicitly private and the assumption is meant to be reused.

## Review Checklist

- The skill name matches the directory name.
- `SKILL.md` has a clear description and workflow.
- Referenced files exist and are reachable by relative path.
- Scripts are deterministic and safe by default.
- The package can be copied into a Codex skills directory without depending on repository-level files.
