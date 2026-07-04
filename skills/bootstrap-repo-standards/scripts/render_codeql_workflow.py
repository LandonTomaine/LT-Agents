#!/usr/bin/env python3
"""Render an approved CodeQL workflow for selected languages."""

from __future__ import annotations

import argparse
from pathlib import Path


TRACKING_DIR = Path(".agents") / "tmp" / "bootstrap-repo-standards"

LANGUAGE_ALIASES = {
    "csharp": "csharp",
    "c#": "csharp",
    "cpp": "c-cpp",
    "c++": "c-cpp",
    "c-cpp": "c-cpp",
    "go": "go",
    "java": "java-kotlin",
    "kotlin": "java-kotlin",
    "java-kotlin": "java-kotlin",
    "javascript": "javascript-typescript",
    "typescript": "javascript-typescript",
    "javascript-typescript": "javascript-typescript",
    "python": "python",
    "ruby": "ruby",
    "swift": "swift",
}


def normalize_languages(values: list[str]) -> list[str]:
    languages: list[str] = []
    for value in values:
        for item in value.split(","):
            key = item.strip().lower()
            if not key:
                continue
            if key not in LANGUAGE_ALIASES:
                allowed = ", ".join(sorted(set(LANGUAGE_ALIASES)))
                raise SystemExit(f"Unsupported CodeQL language '{item}'. Allowed: {allowed}")
            language = LANGUAGE_ALIASES[key]
            if language not in languages:
                languages.append(language)
    if not languages:
        raise SystemExit("At least one --language value is required.")
    return languages


def workflow(languages: list[str]) -> str:
    rendered = "\n".join(f"          - {language}" for language in languages)
    return f"""name: CodeQL

on:
  pull_request:
  push:
    branches:
      - main
  schedule:
    - cron: "30 3 * * 1"

jobs:
  analyze:
    name: Analyze (${{{{ matrix.language }}}})
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language:
{rendered}

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Initialize CodeQL
        uses: github/codeql-action/init@v3
        with:
          languages: ${{{{ matrix.language }}}}

      - name: Autobuild
        uses: github/codeql-action/autobuild@v3

      - name: Perform CodeQL analysis
        uses: github/codeql-action/analyze@v3
"""


def target_path(repo: Path, mode: str) -> Path:
    relative = Path(".github") / "workflows" / "codeql.yml"
    if mode == "draft":
        return repo / TRACKING_DIR / "draft-files" / relative
    return repo / relative


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a CodeQL workflow for approved languages.")
    parser.add_argument("repo", help="Target repository path.")
    parser.add_argument("--language", action="append", default=[], help="CodeQL language. Repeatable or comma-separated.")
    parser.add_argument("--mode", choices=["draft", "apply"], default="draft")
    parser.add_argument("--overwrite-approved", action="store_true", help="Overwrite existing file after exact approval.")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    if not repo.is_dir():
        raise SystemExit(f"Repo path is not a directory: {repo}")

    path = target_path(repo, args.mode)
    if path.exists() and not args.overwrite_approved:
        raise SystemExit(f"Refusing to overwrite existing file without --overwrite-approved: {path}")

    languages = normalize_languages(args.language)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(workflow(languages), encoding="utf-8", newline="\n")
    print(f"mode: {args.mode}")
    print(f"languages: {', '.join(languages)}")
    print(f"created: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
