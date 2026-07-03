# Repository Agent Instructions

This repository stores reusable Codex skills and agent knowledge.

## Rules

- Preserve skill package boundaries. Keep each skill under `skills/<skill-name>/`.
- Do not mix generated collection docs into a skill package unless the skill needs them at runtime.
- Keep `SKILL.md` focused on trigger, purpose, constraints, and workflow.
- Put longer task-specific guidance in `references/` and load it only when needed.
- Put deterministic helpers in `scripts/`; prefer scripts for repeatable scaffolding and checks.
- Keep examples concise and portable across repositories.
- When running PowerShell commands on Windows, do not use `&&` as a command separator. Run sequential commands as separate tool calls, or use clear native PowerShell control flow when one command truly depends on another.

## Change Hygiene

- Review copied skill changes before committing.
- Avoid unrelated formatting churn in skill files.
- Keep repository-level docs short and useful for curation.
- Do not commit local secrets, credentials, generated caches, or temporary Codex state.
