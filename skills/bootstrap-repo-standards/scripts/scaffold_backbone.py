#!/usr/bin/env python3
"""Scaffold approved repo backbone files with safe defaults."""

from __future__ import annotations

import argparse
from pathlib import Path


TRACKING_DIR = Path(".agents") / "tmp" / "bootstrap-repo-standards"
PLACEHOLDER = "TODO: Fill this in after the repo owner confirms the decisions needed for this repo."


def placeholder(title: str) -> str:
    return f"# {title}\n\n{PLACEHOLDER}\n"


TEMPLATES: dict[str, dict[str, str]] = {
    "agent": {
        "AGENTS.md": """# Agent Guide

Start with `agent-rules/README.md`.
""",
        "agent-rules/README.md": """# Agent Rules

Load only the guidance needed for the task.

## Always Load

- [core.md](core.md)

## Routes

- Add task routes only after the referenced docs exist or are approved in the manifest.

## Repo-Local Skills

- Add skill routes only after the referenced skills exist or are approved in the manifest.
""",
        "agent-rules/core.md": """# Core Rules

- Use just enough context.
- Ask when ambiguity affects correctness, scope, data, architecture, or user-visible behavior.
- Prefer shared human docs over agent-only rules.
- Keep agent-read files terse.
""",
        "agent-rules/communication-style.md": """# Communication Style

- Lead with the answer or next action.
- Keep updates short.
- State uncertainty plainly.
""",
        "agent-rules/shell.md": """# Shell Rules

- Prefer focused commands.
- Prefer `rg` for search.
- Ask before destructive actions.
""",
        "agent-rules/maintaining.md": """# Maintaining Agent Rules

- Keep `AGENTS.md` tiny.
- Keep `agent-rules/` for routing and agent behavior.
- Keep durable engineering/product guidance in `docs/`.
- Update routes when adding or moving docs.
""",
        "agent-rules/working-modes.md": """# Working Modes

Use task lenses only when useful:

- Product: scope, users, workflows, acceptance.
- Architecture: boundaries, ownership, risks.
- Implementation: correctness, tests, local patterns.
- Review: bugs, regressions, missing validation.
""",
    },
    "docs": {
        "docs/README.md": """# Documentation

Shared documentation for humans and agents.

## Current Docs

- [architecture/overview.md](architecture/overview.md)
- [development/README.md](development/README.md)
""",
        "docs/architecture/overview.md": placeholder("Architecture Overview"),
        "docs/development/README.md": """# Development Docs

- [local-setup.md](local-setup.md): prerequisites, install, config, and local run commands.
- [deployment.md](deployment.md): deploy, release, or publish process.
- [tooling.md](tooling.md): commands, hooks, lint, format, build, test.
- [testing/strategy.md](testing/strategy.md): test layers and validation expectations.
- [validation.md](validation.md): local and deployed validation expectations.
- [workflow.md](workflow.md): development flow.
""",
        "docs/development/local-setup.md": placeholder("Local Setup"),
        "docs/development/deployment.md": placeholder("Deployment"),
        "docs/development/tooling.md": placeholder("Tooling"),
        "docs/development/validation.md": placeholder("Validation"),
        "docs/development/workflow.md": placeholder("Development Workflow"),
        "docs/development/commits.md": placeholder("Commits"),
        "docs/development/pull-requests.md": placeholder("Pull Requests"),
        "docs/development/testing/README.md": """# Testing Docs

- [strategy.md](strategy.md)
""",
        "docs/development/testing/strategy.md": placeholder("Testing Strategy"),
    },
    "backend": {
        "docs/development/backend.md": placeholder("Backend Standards"),
    },
    "frontend": {
        "docs/development/frontend.md": placeholder("Frontend Standards"),
    },
    "documentation": {
        "docs/development/documentation.md": placeholder("Documentation Maintenance"),
    },
    "bootstrap-checklist": {
        "docs/development/bootstrap-checklist.md": """# Bootstrap Checklist

Durable checklist for the repository standards bootstrap. Update this file when the repo gains, rejects, or defers standards, docs, tooling, validation, or agent guidance.

Status values:

- `present`: exists and is adequate for current repo needs
- `partial`: exists but has known gaps
- `missing`: needed but absent
- `not applicable`: intentionally not relevant for this repo
- `defer`: intentionally postponed with an owner or trigger
- `rejected`: intentionally not wanted

## Repository Shape

| Area | Status | Evidence | Decision or Next Step |
| --- | --- | --- | --- |
| Repo purpose and audience | missing |  |  |
| Runtime surfaces identified | missing |  |  |
| Package managers and project files | missing |  |  |

## Human Documentation

| Area | Status | Evidence | Decision or Next Step |
| --- | --- | --- | --- |
| README entrypoint | missing |  |  |
| Local setup and run docs | missing |  |  |
| Deployment, release, or publish docs | missing |  |  |
| Documentation maintenance rules | missing |  |  |
| Work tracking guidance | missing |  |  |

## Product and Architecture

| Area | Status | Evidence | Decision or Next Step |
| --- | --- | --- | --- |
| Product overview | missing |  |  |
| Domain terms and workflows | missing |  |  |
| Architecture overview | missing |  |  |
| Coding standards | missing |  |  |

## Validation and Quality Gates

| Area | Status | Evidence | Decision or Next Step |
| --- | --- | --- | --- |
| Local validation command matrix | missing |  |  |
| Deployed validation expectations | missing |  |  |
| Unit tests | missing |  |  |
| Integration or contract tests | missing |  |  |
| Formatter | missing |  |  |
| Linters | missing |  |  |
| Static analysis | missing |  |  |
| Architecture tests or source guards | missing |  |  |
| Git hooks | missing |  |  |
| CI gates | missing |  |  |
| Dependency, license, vulnerability, or secret checks | missing |  |  |

## Agent Guidance and Skills

| Area | Status | Evidence | Decision or Next Step |
| --- | --- | --- | --- |
| AGENTS.md or agent entrypoint | missing |  |  |
| Agent routing docs | missing |  |  |
| Repo-local skills | missing |  |  |
| Skill migration status | missing |  |  |
""",
    },
    "standards-roadmap": {
        "docs/development/standards-roadmap.md": placeholder("Standards Roadmap"),
    },
    "product": {
        "docs/product/README.md": """# Product Docs

Durable product context for humans and agents.
""",
        "docs/product/overview.md": placeholder("Product Overview"),
        "docs/product/ubiquitous-language.md": placeholder("Ubiquitous Language"),
        "docs/product/domain-concepts.md": placeholder("Domain Concepts"),
        "docs/product/personas.md": placeholder("Personas"),
        "docs/product/workflows.md": placeholder("Workflows"),
        "docs/product/requirements/README.md": placeholder("Product Requirements"),
    },
    "work-tracking": {
        "docs/development/work-tracking.md": placeholder("Work Tracking"),
    },
    "file-backlog": {
        "docs/backlog/README.md": """# Backlog

Track file-based delivery backlogs, implementation plans, workflow state, and artifacts only if this repo uses them.

See [index.md](index.md).
""",
        "docs/backlog/index.md": """# Backlog Index

List approved backlog areas.
""",
        "docs/backlog/example-capability/backlog.md": placeholder("Example Capability Backlog"),
        "docs/backlog/example-capability/plans/.gitkeep": "",
        "docs/backlog/example-capability/workflows/.gitkeep": "",
        "docs/backlog/example-capability/artifacts/.gitkeep": "",
    },
    "skills": {
        ".agents/skills/review-changed-code/SKILL.md": """---
name: review-changed-code
description: Review the current code changes against this repo's standards and directly related context. Use when the user asks for a code review, changed-code review, PR review, or reviewer pass on in-flight edits.
---

# Review Changed Code

Primary lens: `Review`.

## Goal

Review the current diff against this repo's documented standards and nearby code patterns.

## Workflow

1. Read `AGENTS.md`, then the routed docs needed for the changed area.
2. Inspect the diff and only the directly related context needed to judge it.
3. Prioritize bugs, regressions, architecture or standards violations, and missing validation.
4. Do not turn this into a whole-repo audit unless the user asks.

## Output

Return findings first, ordered by severity:

- `[high|medium|low] file:line - finding`
- `Why it matters: <short impact>`
- `Blocking: yes|no`

If there are no findings, say so and note any validation gaps.
""",
        ".agents/skills/review-changed-code/agents/openai.yaml": """interface:
  display_name: "Review Changed Code"
  short_description: "Review changes against repo standards"
  default_prompt: "Use $review-changed-code to review the current changes against this repo's standards."
""",
    },
}


def selected_templates(sets: list[str]) -> dict[str, str]:
    files: dict[str, str] = {}
    for set_name in sets:
        if set_name not in TEMPLATES:
            allowed = ", ".join(sorted(TEMPLATES))
            raise SystemExit(f"Unknown set '{set_name}'. Allowed: {allowed}")
        files.update(TEMPLATES[set_name])
    return files


def target_path(repo: Path, mode: str, relative_path: str) -> Path:
    if mode == "draft":
        return repo / TRACKING_DIR / "draft-files" / relative_path
    return repo / relative_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold approved repo backbone files.")
    parser.add_argument("repo", help="Target repository path.")
    parser.add_argument(
        "--mode",
        choices=["draft", "apply"],
        default="draft",
        help="draft writes under .agents/tmp; apply writes durable repo files.",
    )
    parser.add_argument(
        "--set",
        action="append",
        dest="sets",
        default=[],
        help=f"Template set to scaffold. Repeatable. Allowed: {', '.join(sorted(TEMPLATES))}.",
    )
    parser.add_argument("--list", action="store_true", help="List template sets and files.")
    parser.add_argument(
        "--overwrite-approved",
        action="store_true",
        help="Overwrite existing files. Use only after exact path-level approval.",
    )
    args = parser.parse_args()

    if args.list:
        for set_name, templates in sorted(TEMPLATES.items()):
            print(f"{set_name}:")
            for path in sorted(templates):
                print(f"  {path}")
        return 0

    repo = Path(args.repo).resolve()
    if not repo.is_dir():
        raise SystemExit(f"Repo path is not a directory: {repo}")

    if args.mode == "apply" and not args.sets:
        raise SystemExit("apply mode requires at least one explicit --set from the approved manifest.")

    sets = args.sets or ["agent", "docs", "skills"]
    templates = selected_templates(sets)

    created: list[str] = []
    skipped: list[str] = []
    existing_targets: list[str] = []
    for relative_path, content in templates.items():
        existing_target = repo / relative_path
        if existing_target.exists():
            existing_targets.append(str(existing_target))

        path = target_path(repo, args.mode, relative_path)
        if path.exists() and not args.overwrite_approved:
            skipped.append(str(path))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        created.append(str(path))

    print(f"mode: {args.mode}")
    print(f"sets: {', '.join(sets)}")
    print("created:")
    for path in created:
        print(f"- {path}")
    print("skipped:")
    for path in skipped:
        print(f"- {path}")
    print("existing target files:")
    for path in existing_targets:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
