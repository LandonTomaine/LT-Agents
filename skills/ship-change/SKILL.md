---
name: ship-change
description: Lightweight end-to-end coding workflow for taking a user request through analysis, a concise plan, implementation, validation, and handoff. Use when the user wants Codex to do a repo change from start to finish, especially when the work should be committed and pushed only after the user approves the final diff, commit message, and push target.
---

# Ship Change

## Goal

Move a repo request from intent to delivered local changes with minimal ceremony, while keeping approval boundaries clear before commit and push.

## Workflow

1. Understand the request.
   - Inspect the repo before assuming architecture, commands, or conventions.
   - Check `git status --short --branch` before editing.
   - Identify whether the worktree has unrelated user changes.

2. Plan briefly.
   - State the intended files or areas to touch.
   - Keep the plan proportional; use a short checklist for multi-step work.
   - Ask only when a missing decision would make the implementation risky.

3. Implement.
   - Follow existing repo patterns.
   - Keep edits scoped to the request.
   - Do not revert unrelated user changes.
   - Update docs or indexes when the change affects user or agent workflow.

4. Validate.
   - Run the repo's documented checks for the changed surface.
   - If no checks are documented, run the lightest relevant inspection and say that no stronger validation exists.
   - Report any skipped checks and why.

5. Review before shipping.
   - Show the changed files and validation result.
   - Inspect the diff yourself before asking for approval.
   - Propose a concise commit message.
   - Ask for explicit approval before committing or pushing unless the user already gave explicit approval for commit and push in the current request.

6. Commit and push after approval.
   - Stage only the intended files.
   - Commit with the approved or clearly proposed message.
   - Push to the approved remote and branch.
   - Report the commit SHA, branch, remote URL, and validation performed.

## Git Safety

- Never use `git reset --hard`, `git checkout --`, rebase, force-push, or history rewrite unless the user explicitly requests that exact operation.
- Do not use `git add -A` in a mixed worktree unless every changed file is in scope.
- If publishing requires auth, remote creation, or a new branch, explain the target before acting.
- If the push fails, stop and report the exact blocker; do not try destructive fixes.

## Handoff Format

Keep the final answer short:

- what changed
- validation run
- commit SHA and push target, if shipped
- anything not done or still needing approval
