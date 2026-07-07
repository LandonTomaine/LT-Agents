---
name: audit-skills
description: Audit Codex skills for DRYness, brevity, trigger quality, progressive disclosure, and unnecessary duplication of always-loaded or tool-provided guidance. Use when the user asks to review, trim, tighten, de-duplicate, or improve one or more skills, especially when deciding what belongs in SKILL.md versus nearby references, scripts, or assets.
---

# Audit Skills

Primary lens: `Review`.

## Goal

Review skills as compact operating guides, not mini handbooks.

Bias hard toward brevity. Keep only wording that changes behavior, routing, or risk.

## Workflow

1. Scope first.
   - Identify the skill or skill set to review.
   - Read only the targeted `SKILL.md` files and directly relevant nearby resources.

2. Load the checklist after the scope is clear.
   - Read [references/audit-checklist.md](references/audit-checklist.md).
   - Use only the sections that match the current audit.

3. Audit for trigger quality.
   - Description says what the skill does and when to use it.
   - Invocation is not broader than the workflow.

4. Audit for DRYness and context discipline.
   - Repeated always-loaded rules.
   - Repo guidance that belongs in repo docs.
   - Duplicated text across `SKILL.md`, `references/`, and scripts.

5. Audit for brevity first, not style polish.
   - Cut filler, throat-clearing, duplicated framing, and obvious statements.
   - Prefer short bullets or fragments when clear.

6. Audit for progressive disclosure.
   - Keep core workflow guidance in `SKILL.md`.
   - Move details, examples, and checklists to nearby `references/`.
   - Prefer `scripts/` for repeatable deterministic helpers.

7. Verify before calling something redundant.
   - Point to where the duplicated guidance already lives.
   - Do not assume a rule is always loaded.

8. Edit or report.
   - If the task includes fixes, make focused edits.
   - Prefer deletion over rewriting, and rewriting over expansion.
   - If the skill is already concise and useful, say `no change needed`.

## Output

- the skills reviewed
- findings ordered by impact
- file paths that support each finding
- whether each issue is trigger drift, repeated always-loaded guidance, repeated repo guidance, over-verbose body content, misplaced detail that should move to `references/` or `scripts/`, duplication, or template residue
- a final conclusion: fix now, defer with rationale, or no change needed

## Do Not

- Do not manufacture low-value findings.
- Do not preserve full sentences just because they read better.
- Do not create cosmetic edits to avoid an empty audit.
