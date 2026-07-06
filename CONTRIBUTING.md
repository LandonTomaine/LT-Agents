# Contributing

This repository is a curated catalog of reusable Codex skills. Keep changes focused, portable, and easy to install.

## Skill Requirements

Each skill lives under `skills/<skill-name>/` and must include:

- `SKILL.md` with YAML frontmatter containing `name` and `description`
- a directory name that matches the `name`
- concise instructions focused on the workflow

Optional resources:

- `agents/openai.yaml` for Codex UI metadata
- `references/` for longer guidance loaded only when needed
- `scripts/` for deterministic helpers
- `assets/` for templates or output resources

Do not add extra README, install, changelog, or guide files inside a skill package unless the skill genuinely needs them at runtime.

## Adding Or Updating A Skill

1. Add or edit the skill under `skills/`.
2. Update `README.md` and `skills/README.md`.
3. Keep package boundaries intact; do not depend on repo-level docs from inside a skill.
4. Run validation:

```powershell
python scripts\validate_skills.py
```

5. Review the diff before committing:

```powershell
git status --short
git diff
```

## Commit And Push

Use small commits that name the skill or catalog area changed.

Examples:

- `Add audit-docs skill`
- `Tighten bootstrap standards workflow`
- `Document skill install workflow`

Push to `origin/main` for normal catalog updates. Use a branch for broad rewrites, new multi-file skills, or changes that need review first.
