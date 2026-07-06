#!/usr/bin/env python3
"""Check repo-local skill migration from .codex/skills to .agents/skills."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".vs",
    ".idea",
    "node_modules",
    "bin",
    "obj",
    "dist",
    "build",
    "out",
    "coverage",
    "test-results",
    "artifacts",
    "__pycache__",
}

SKIP_PATH_SUFFIXES = {
    ".agents/tmp",
    ".agents/tmp/bootstrap-repo-standards",
    ".codex/tmp",
    ".codex/state",
    ".codex/plans",
    ".codex/workflows",
}

TEXT_SUFFIXES = {
    ".md",
    ".mdx",
    ".txt",
    ".rst",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
    ".py",
    ".ps1",
    ".sh",
}

LEGACY_TOKENS = [".codex/skills", ".codex\\skills"]


def should_skip_dir(path: Path) -> bool:
    if path.name in SKIP_DIRS:
        return True
    normalized = path.as_posix().lower()
    return any(normalized.endswith(f"/{suffix}") for suffix in SKIP_PATH_SUFFIXES)


def iter_files(root: Path):
    for current_root, dirs, files in os.walk(root):
        current = Path(current_root)
        dirs[:] = [d for d in dirs if not should_skip_dir(current / d)]
        for file_name in files:
            yield current / file_name


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def skill_names(skills_dir: Path) -> list[str]:
    if not skills_dir.is_dir():
        return []
    return sorted(path.name for path in skills_dir.iterdir() if path.is_dir())


def read_lines(path: Path) -> list[str]:
    try:
        return path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return []


def collect_legacy_path_refs(root: Path) -> list[dict[str, object]]:
    refs: list[dict[str, object]] = []
    for file_path in iter_files(root):
        if file_path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        for index, line in enumerate(read_lines(file_path), start=1):
            if any(token in line for token in LEGACY_TOKENS):
                refs.append({"path": rel(root, file_path), "line": index, "text": line.strip()})
    return refs


def collect_sibling_refs(root: Path, legacy_skills: list[str]) -> list[dict[str, object]]:
    legacy_dir = root / ".codex" / "skills"
    if not legacy_dir.is_dir():
        return []

    refs: list[dict[str, object]] = []
    patterns = []
    for name in legacy_skills:
        patterns.extend([f"../{name}", f"..\\{name}"])

    for file_path in iter_files(legacy_dir):
        if file_path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        for index, line in enumerate(read_lines(file_path), start=1):
            matched = [pattern for pattern in patterns if pattern in line]
            if matched:
                refs.append(
                    {
                        "path": rel(root, file_path),
                        "line": index,
                        "patterns": matched,
                        "text": line.strip(),
                    }
                )
    return refs


def check(root: Path) -> dict[str, object]:
    root = root.resolve()
    legacy_dir = root / ".codex" / "skills"
    target_dir = root / ".agents" / "skills"
    legacy_skills = skill_names(legacy_dir)
    target_skills = skill_names(target_dir)
    conflicts = sorted(set(legacy_skills) & set(target_skills))
    return {
        "root": str(root),
        "legacy_dir": ".codex/skills",
        "target_dir": ".agents/skills",
        "legacy_skills": legacy_skills,
        "target_skills": target_skills,
        "target_conflicts": conflicts,
        "legacy_path_refs": collect_legacy_path_refs(root),
        "sibling_relative_refs": collect_sibling_refs(root, legacy_skills),
    }


def print_markdown(data: dict[str, object]) -> None:
    print(f"# Skill Migration Check: {data['root']}")
    print()
    print(f"- Legacy dir: {data['legacy_dir']}")
    print(f"- Target dir: {data['target_dir']}")
    print(f"- Legacy skills: {', '.join(data['legacy_skills']) if data['legacy_skills'] else 'none'}")
    print(f"- Target skills: {', '.join(data['target_skills']) if data['target_skills'] else 'none'}")
    print(f"- Target conflicts: {', '.join(data['target_conflicts']) if data['target_conflicts'] else 'none'}")
    print()
    print("## Legacy Path References")
    refs = data["legacy_path_refs"]
    if refs:
        for item in refs:
            print(f"- {item['path']}:{item['line']} - {item['text']}")
    else:
        print("- none")
    print()
    print("## Sibling Relative References")
    sibling_refs = data["sibling_relative_refs"]
    if sibling_refs:
        for item in sibling_refs:
            patterns = ", ".join(item["patterns"])
            print(f"- {item['path']}:{item['line']} ({patterns}) - {item['text']}")
    else:
        print("- none")
    print()
    print("## Notes")
    print("- Resolve target conflicts before migration.")
    print("- Update legacy path references in the same approved migration batch.")
    print("- If sibling relative references exist, migrate referenced sibling skills together or update those links.")
    print("- This script is read-only; it does not move, copy, edit, or delete files.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check skill migration safety.")
    parser.add_argument("repo", help="Target repository path.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    args = parser.parse_args()

    root = Path(args.repo)
    if not root.is_dir():
        raise SystemExit(f"Repo path is not a directory: {root}")

    data = check(root)
    if args.json:
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        print_markdown(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
