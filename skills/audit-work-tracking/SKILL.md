---
name: audit-work-tracking
description: Audit repository backlog, issue-tracker, PRD, workflow-state, implementation-plan, and artifact tracking for unclear ownership, stale status, oversized items, mixed status vocabularies, missing routing, or token-heavy agent workflows. Use when Codex is asked to review, tighten, migrate, or design how a repo tracks work.
---

# Audit Work Tracking

Primary lens: `Review`.

Goal: review the work-tracking system, not the whole repo. Return findings first; make edits only when the user asks for fixes.

## Scope

Start with the smallest relevant entrypoints:

- repo agent guide or contributor guide
- tracker/workflow docs
- backlog or issue indexes
- representative active item, plan, workflow state, and result artifact
- repo-local skills that select, plan, implement, or update work

Do not read every backlog item unless the audit explicitly needs coverage sampling.

## Checklist

- Source of truth: work item ownership is clear between tracker, PRD, backlog, plan, workflow state, and chat.
- Lanes: active, done, deferred, bugs/incidents, enhancements, and tech-debt lanes are explicit when file-based tracking is used.
- Status vocabularies: backlog, workflow queue, bug/incident, PR, and process-improvement states are distinct and documented.
- Granularity: executable items are small enough to plan, validate, review, and close independently.
- Routing: intake, selection, planning, implementation, review, and closeout have clear handoffs.
- Artifacts: screenshots, logs, validation, result notes, and residual risks live beside the owning work item or in a named tracker location.
- Token cost: agents can find the next action without loading broad PRDs, old plans, large artifacts, or every historical item.
- Closure: done/deferred items are archived or indexed without staying in active queues.

## Output

Return:

- `Scope reviewed`
- findings ordered by impact
- `Why it matters`
- `Suggested fix`
- `Skill or docs impact`, if any
- `Verdict`: `Pass`, `Pass with gaps`, or `Fail`

Prefer one or two concrete fixes over a new workflow system. Recommend a new skill only when the workflow is repeated, narrow, repo-specific, and docs alone are insufficient.

## Do Not

- Do not invent a file-based backlog for repos that use an external tracker.
- Do not merge intake, selection, planning, implementation, and review into one skill by default.
- Do not turn the audit into broad product planning or code review.
