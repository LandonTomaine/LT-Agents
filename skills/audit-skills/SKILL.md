---
name: audit-skills
description: Audit Codex skills for DRYness, brevity, trigger quality, progressive disclosure, and unnecessary duplication of always-loaded or tool-provided guidance. Use when the user asks to review, trim, tighten, de-duplicate, or improve one or more skills, especially when deciding what belongs in SKILL.md versus nearby references, scripts, or assets.
---

# Audit Skills

## Goal

Review skills as compact operating guides, not mini handbooks. Bias hard toward brevity. Clear intent matters more than polished prose. Full sentences are optional. Fragments, short bullets, and terse directives are preferred when they stay unambiguous.

Identify where a skill is too verbose, repeats always-loaded rules, duplicates repo guidance, uses weak trigger wording, or keeps detail in `SKILL.md` that should live in nearby `references/` or `scripts/`.

It is valid for the audit to conclude that the reviewed skills are already fine. This skill is not expected to always find an issue, and it must not manufacture low-value nitpicks just to produce findings.

## Workflow

1. Define the audit scope first.
   - Identify the skill or skill set to review.
   - Read only the targeted `SKILL.md` files and directly relevant nearby resources.
2. Load the checklist after the scope is clear.
   - Read [references/audit-checklist.md](references/audit-checklist.md).
   - Use only the sections that match the current audit.
3. Audit for trigger quality.
   - Check whether the frontmatter description clearly states what the skill does and when to use it.
   - Check whether invocation should be explicit-only instead of inferred by context.
4. Audit for DRYness and context discipline.
   - Flag repeated agent rules that are already always loaded.
   - Flag repeated repo guidance that should stay in repo docs rather than in the skill body.
   - Flag duplicated text across `SKILL.md` and nearby references.
5. Audit for brevity first, not style polish.
   - Cut filler, throat-clearing, duplicated framing, and obvious statements.
   - Prefer short bullets or fragments over explanatory paragraphs.
   - Do not preserve full sentences just because they read better.
   - Keep only what changes agent behavior or prevents a likely mistake.
6. Audit for progressive disclosure.
   - Keep core workflow guidance in `SKILL.md`.
   - Move detailed checklists, examples, domain-specific notes, or skill-specific procedures into nearby `references/` when they do not need to live in the main body.
   - Prefer nearby `scripts/` for repeatable command sequences or deterministic helpers instead of embedding long command blocks in `SKILL.md`.
7. Verify before calling something redundant.
   - Check whether the supposedly duplicated guidance is actually available elsewhere in the skill, repo, or system instructions.
   - Do not assume a rule is always loaded unless you can point to where it comes from.
8. Conclude explicitly.
   - Make focused edits when the task includes improving the skills.
   - Otherwise report findings with recommended fixes.
   - If the skills are already in good shape, say so explicitly and make no changes.

## What Good Looks Like

- Short, specific trigger descriptions.
- A compact `SKILL.md` body with only workflow-critical guidance.
- Fragments and terse bullets where they are clear.
- No repetition of always-loaded rules unless the skill needs a narrow exception or specialization.
- References files for detailed, skill-specific material that does not need to load every time.
- Scripts for repeatable helper behavior that should not be rewritten ad hoc.
- No fake structure, filler headings, or template leftovers.
- No full-sentence bias. Clear and short beats polished and long.
- No unnecessary edits when the current skill is already concise, specific, and well-structured.

## Output

Produce a concise audit with:

- the skills reviewed
- findings ordered by impact
- file paths that support each finding
- whether each issue is trigger drift, repeated always-loaded guidance, repeated repo guidance, over-verbose body content, misplaced detail that should move to `references/` or `scripts/`, duplication, or template residue
- a final conclusion: fix now, defer with rationale, or no change needed

If you make edits, prefer deletion over rewriting, and rewriting over expansion. Default to shorter wording. Do not add prose where bullets or fragments are enough. Prefer moving detail into nearby skill resources rather than growing `SKILL.md`.

If there are no meaningful issues, return `no change needed` and stop. Do not create or apply cosmetic or speculative edits just to avoid an empty audit.
