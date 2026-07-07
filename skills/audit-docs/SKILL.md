---
name: audit-docs
description: Lightweight documentation audit workflow for checking repo docs, indexes, and agent guidance for stale content, duplication, missing routes, unclear ownership, and mismatches with the current repository. Use when the user asks to review, tighten, de-duplicate, or improve documentation without doing a broad standards bootstrap.
---

# Audit Docs

Primary lens: `Review`.

## Goal

Review docs as a navigable system. Find drift, duplication, missing routes, and unclear maintenance rules. Prefer focused fixes over new documentation layers.

## Workflow

1. Scope the audit.
   - Identify the docs or repo area to review.
   - Check `git status --short --branch`.
   - Read entrypoints first: `README*`, `AGENTS.md`, docs indexes, and skill indexes.

2. Build an evidence map.
   - List authoritative docs.
   - List route/index docs.
   - Note docs that appear historical, duplicated, stale, or incomplete.
   - Search for changed concepts across the repo before calling a doc stale.

3. Audit for maintainability.
   - Can a new human find the right next doc?
   - Can an agent find the right rule without loading unrelated material?
   - Are install, validation, commit, push, and publishing expectations clear when relevant?
   - Are repeated command sequences better as scripts than prose?
   - Are skill package routes current?
   - Are maintenance triggers documented?

4. Recommend or edit.
   - If the user asked for a review, report findings first with file paths.
   - If the user asked for fixes, make narrow edits to authoritative docs and indexes.
   - Prefer updating or deleting duplicate guidance over adding a new file.
   - Do not create broad docs, roadmaps, or repo-local skills without explicit approval.

5. Validate.
   - Run the repo's documented doc validation.
   - At minimum, run `git status --short` and `rg --files`.
   - For changed links or routes, verify referenced files exist.

## Output

Order findings by impact:

- stale or wrong guidance
- missing route or missing authoritative doc
- duplication or conflicting docs
- unclear ownership or maintenance trigger
- overlarge or misplaced agent-only guidance

If no meaningful issue exists, say `no change needed` and do not invent cosmetic findings.

## Do Not

- Do not create broad docs, roadmaps, or repo-local skills without explicit approval.
- Do not call a doc stale without checking repo evidence.
