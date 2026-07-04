# Skills

This directory contains self-contained Codex skill packages.

## Available Skills

- [`audit-docs`](audit-docs/SKILL.md): Lightweight documentation audit workflow for repo docs and indexes.
- [`audit-skills`](audit-skills/SKILL.md): Skill audit workflow for trigger quality, brevity, DRYness, and resource placement.
- [`bootstrap-repo-standards`](bootstrap-repo-standards/SKILL.md): Repository standards bootstrapping workflow with references and helper scripts.
- [`ship-change`](ship-change/SKILL.md): Lightweight end-to-end change workflow with approval before commit and push.

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
