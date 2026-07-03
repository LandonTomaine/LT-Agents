#!/usr/bin/env python3
"""Create temporary tracking files for bootstrap-repo-standards."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path


FILES = {
    "session.md": """# Bootstrap Repo Standards Session

Status: active
Started: {timestamp}
Repo: {repo}

## Stop Rule

- Continue until the user says this pass is done, or every question and checklist item is resolved with no material ambiguity.
- Validation ambiguity must be answered or explicitly deferred by the user.

## Scope

- Outcome:
- Off limits:
- Approval mode:

## Checkpoints

- {timestamp}: Tracking initialized.
""",
    "question-ledger.md": """# Question Ledger

Status values: `unanswered`, `answered`, `ambiguous`, `assumption candidate`, `defer`.

| ID | Theme | Status | Question | Answer / Decision | Source | Ambiguity / Next Step |
| --- | --- | --- | --- | --- | --- | --- |
""",
    "evidence-map.md": """# Evidence Map

## Proven By Files

| Area | Evidence | Source |
| --- | --- | --- |

## Inferred

| Area | Inference | Evidence | Needs Confirmation |
| --- | --- | --- | --- |

## Unknown

| Area | Unknown | Blocking |
| --- | --- | --- |
""",
    "backbone-checklist.md": """# Backbone Checklist

Status values: `open`, `checked`, `candidate`, `approved`, `rejected`, `defer`, `done`.

| Area | Item | Status | Notes |
| --- | --- | --- | --- |
""",
    "backbone-manifest.md": """# Backbone Manifest

Only approved rows may be written as durable repo files.

| Path / Action | Audience | Purpose | Status | Notes |
| --- | --- | --- | --- | --- |
""",
    "completion-checklist.md": """# Completion Checklist

Status values: `open`, `checked`, `rejected`, `defer`.

| ID | Check | Status | Evidence / Notes |
| --- | --- | --- | --- |
| C1 | Repo scan complete | open | |
| C2 | Evidence map updated | open | |
| C3 | Product questions resolved or explicitly deferred | open | |
| C4 | Architecture questions resolved or explicitly deferred | open | |
| C5 | Coding standards questions resolved or explicitly deferred | open | |
| C6 | Quality-gate questions resolved or explicitly deferred | open | |
| C7 | Runtime surfaces confirmed or explicitly deferred | open | |
| C8 | Local setup/run docs found, approved, rejected, or explicitly deferred | open | |
| C9 | Deployment/release docs found, approved, rejected, or explicitly deferred | open | |
| C10 | Documentation maintenance workflow found, approved, rejected, or explicitly deferred | open | |
| C11 | Standards adoption roadmap approved, rejected, or explicitly deferred | open | |
| C12 | Local validation expectations resolved or explicitly deferred | open | |
| C13 | Deployed validation expectations resolved or explicitly deferred | open | |
| C14 | Documentation and agent-routing questions resolved or explicitly deferred | open | |
| C15 | Repo-local skill questions resolved or explicitly deferred | open | |
| C16 | Backbone checklist has no open/candidate items | open | |
| C17 | Manifest has no unapproved durable actions | open | |
| C18 | Approved work implemented or explicitly deferred | open | |
| C19 | Validation recorded for approved changes | open | |
| C20 | User reviewed final state or explicitly waived review | open | |
""",
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize temp tracking files.")
    parser.add_argument("repo", help="Target repository path.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    if not repo.is_dir():
        raise SystemExit(f"Repo path is not a directory: {repo}")

    target = repo / ".agents" / "tmp" / "bootstrap-repo-standards"
    target.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().astimezone().isoformat(timespec="seconds")
    for name, template in FILES.items():
        path = target / name
        if path.exists():
            continue
        path.write_text(
            template.format(timestamp=timestamp, repo=repo),
            encoding="utf-8",
            newline="\n",
        )

    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
