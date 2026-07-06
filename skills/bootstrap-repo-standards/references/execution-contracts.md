# Execution Contracts

Load when temp tracking, completion checks, scaffold scripts, or final bootstrap status matters.

## Temp Tracking Files

Recommended path: `.agents/tmp/bootstrap-repo-standards/`

- `session.md`: scope, status, stop rule, latest checkpoint.
- `question-ledger.md`: every question, status, answer, source, ambiguity.
- `evidence-map.md`: file-backed facts, inferences, unknowns.
- `backbone-checklist.md`: candidate docs/gates/skills and decision status.
- `backbone-manifest.md`: proposed create/update/skip actions awaiting approval.
- `completion-checklist.md`: final stop criteria.
- `draft-files/`: script-generated draft skeletons mirroring target paths.

Rules:

- Ask before first creation unless the user already approved temp tracking files.
- Preserve existing files; append or update in place.
- Keep entries terse.
- Mark each question `unanswered`, `answered`, `ambiguous`, `assumption candidate`, or `defer`.
- `answered` requires enough detail to write or reject a durable item without guessing.
- `defer` requires an owner or explicit reason.
- Mark checklist items `open`, `checked`, `rejected`, or `defer`.
- `checked` requires evidence, user confirmation, or completed approved work.
- Do not graduate temp files into final docs unless approved in the manifest.
- If the repo tracks `.agents/tmp`, ask whether to ignore it before adding ignore rules.

## Durable Bootstrap Checklist

Default path: `docs/development/bootstrap-checklist.md`

- Propose this file in the first manifest unless the user rejects it.
- Update it after each approved bootstrap batch.
- Include evidence paths for every `present` or `partial` item.
- Keep future work here as standards/bootstrap follow-up, not product backlog.
- Use [backbone-checklist.md](backbone-checklist.md) for categories, statuses, and roadmap split rules.

## Completion Criteria

Done only when one is true:

- User explicitly says this pass is done, even with remaining open items.
- Or all are true:
  - `question-ledger.md`: no `unanswered`, `ambiguous`, or `assumption candidate`.
  - `backbone-checklist.md`: no `candidate` or `open`.
  - `backbone-manifest.md`: every row is `approved`, `done`, `rejected`, or `defer`.
  - `completion-checklist.md`: every row is `checked`, `rejected`, or `defer`.
  - No material product, architecture, standards, tooling, docs, quality-gate, or skill ambiguity remains.
  - Documentation maintenance is found, approved, rejected, or explicitly deferred.
  - Durable bootstrap checklist is approved and current, rejected, or explicitly deferred.
  - Standards roadmap is approved, rejected, or explicitly deferred.
  - Local setup/run guidance is found, approved, rejected as not applicable, or explicitly deferred.
  - Deployment/release guidance is found, approved, rejected as not applicable, or explicitly deferred.
  - Local and deployed validation expectations are explicit for every confirmed runtime surface, or explicitly deferred.
  - Validation for approved changes is recorded.

If not done, ask the next highest-risk unresolved question and keep working.

## Script Safety

- `repo_scan.py`: read-only; mandatory first inventory pass unless unavailable.
- `check_skill_migration.py`: read-only.
- `init_tracking.py`: writes temp tracking files only.
- `scaffold_backbone.py --mode draft`: writes temp draft files only.
- `scaffold_backbone.py --mode apply`: writes durable target files. Use only after approved manifest.
- `copy_skill_package.py --mode draft`: copies an approved source skill package under temp draft files only.
- `copy_skill_package.py --mode apply`: copies an approved source skill package into the durable target path. Use only after approved manifest.
- `render_codeql_workflow.py`: writes a language-specific CodeQL workflow in draft or apply mode. Use only after languages are confirmed and approved.
- Scaffold apply mode skips existing files by default.
- Skill package copy mode skips existing files by default and must report target conflicts.
- Scaffolded agent routes are minimal by design. Do not assume scaffold output is the final route map.
- Treat scaffold `skipped existing` output as a required review list.
- Do not use scaffold overwrite for existing guidance files. Prefer targeted patches.
- Use scaffold overwrite only for newly generated temp drafts or exact path-level replacement approved by the user.
- Before any write-mode script, state mode, target root, file sets, and whether durable files may be written.

Common scaffold sets:

- `agent`: minimal `AGENTS.md` and `agent-rules/` route layer.
- `claude-entrypoint`: minimal `CLAUDE.md` redirect to `AGENTS.md`.
- `docs`: shared docs skeleton.
- `bootstrap-checklist`: durable standards bootstrap ledger.
- `file-backlog`: file-based backlog, follow-up, bug, plan, and workflow templates.
- `skills`: starter `review-changed-code`.
- `implementation-skills`: plan, implement, plan-review, and bug-resolution skills.
- `orchestration-skill`: resumable work-plan orchestration.
- `docs-audit-skills`: standards-doc audit, skill-opportunity audit, and docs-update skills.
- `ui-validation-skill`: browser validation starter for confirmed UI repos.
- `git-hooks`, `security`, `public-repo`, `product`, `work-tracking`, `standards-roadmap`, `backend`, `frontend`, `documentation`: specialized approved sets.

Use `copy_skill_package.py` instead of scaffold sets only when the user approved copying or adapting a concrete existing skill package.

## Outputs

Before approval:

- scan summary
- evidence map
- question ledger
- proposed backbone manifest
- recommended adoption phases

After approval:

- changed files
- validation results
- remaining unanswered questions
- next recommended batch, if any
