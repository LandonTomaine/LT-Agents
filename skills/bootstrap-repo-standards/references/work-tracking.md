# Work Tracking

Load before proposing PRD, backlog, issue, tracker, plan, or workflow-state files.

## Decision

Ask how the repo tracks work before creating backlog files.

Modes:

- `file-based`: repo stores PRDs, backlogs, plans, workflow state, and artifacts in files.
- `external-tracker`: GitHub, Azure DevOps, Linear, Jira, or another tracker owns work items.
- `none`: no durable work tracking needed in this repo.
- `defer`: create only an approved TODO placeholder.

## File-Based Mode

Use only when the user chooses file-based planning.

Candidate files:

- `docs/product/requirements/` for durable product requirements, if product planning is in scope.
- `docs/backlog/` for delivery backlogs, implementation plans, workflow state, and artifacts.
- An example capability folder only when approved.

Keep file-based examples generic. Do not imply all repos need PRDs, numbered capabilities, screenshots, or workflow-state files.

Optional communication docs:

- Create "what is next", release preview, roadmap, or stakeholder handoff docs only when communication planning is in scope.
- Keep communication docs separate from executable backlog, tracker, and workflow state.
- Do not expose internal backlog IDs, agent workflow terms, or implementation sequencing in user-facing copy unless explicitly approved.

Approved scaffold set:

- `file-backlog`: backlog index, bugs/incidents table, follow-ups table, example capability backlog, plan template, workflow-state template, and artifact folders.

Replace scaffold examples with repo-specific evidence before treating them as active work. Keep plan and workflow files short enough to reload cheaply.

## External Tracker Mode

Do not create a local PRD/backlog tree by default.

Create `docs/development/work-tracking.md` only when approved. It should be a TODO placeholder until the user confirms:

- tracker system
- work item types
- branch naming
- planning handoff
- status transitions
- review and validation expectations
- whether any local plan files are allowed

## Repo-Local Skill Candidate

Propose a work-tracking skill only when the repo has a repeated tracker workflow that docs alone will not guide well.

Candidate examples:

- plan a work item into an implementation plan
- implement one approved work item
- update tracker status and comments after validation
- convert a file-based backlog slice into tasks

Do not create the skill without approval and a clear trigger.
