#!/usr/bin/env python3
"""Copy an approved Codex skill package into a target repo safely."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


TRACKING_DIR = Path(".agents") / "tmp" / "bootstrap-repo-standards"
DEFAULT_TARGET_ROOT = Path(".agents") / "skills"
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
SKIP_SUFFIXES = {".pyc", ".pyo"}
SKILL_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
    ".ini",
    ".cfg",
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".css",
    ".html",
    ".sh",
    ".ps1",
}


def parse_replace(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("replacement must be FROM=TO")
    old, new = value.split("=", 1)
    if not old:
        raise argparse.ArgumentTypeError("replacement FROM value cannot be empty")
    return old, new


def safe_relative_path(value: str, *, argument: str) -> Path:
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise argparse.ArgumentTypeError(f"{argument} must be a safe relative path")
    return path


def parser_safe_relative_path(parser: argparse.ArgumentParser, value: str, *, argument: str) -> Path:
    try:
        return safe_relative_path(value, argument=argument)
    except argparse.ArgumentTypeError as exc:
        parser.error(str(exc))


def ensure_inside(base: Path, candidate: Path) -> None:
    try:
        candidate.resolve().relative_to(base.resolve())
    except ValueError as exc:
        raise SystemExit(f"Refusing to write outside {base}: {candidate}") from exc


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts) or path.suffix in SKIP_SUFFIXES


def is_text(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in {"SKILL.md"}


def rewrite_frontmatter_name(content: str, old_name: str, new_name: str) -> str:
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return content
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            break
        if line.startswith("name: "):
            lines[index] = f"name: {new_name}\n"
            break
    return "".join(lines)


def read_skill_name(skill_file: Path) -> str | None:
    try:
        content = skill_file.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            return None
        if line.startswith("name: "):
            return line.split(":", 1)[1].strip().strip('"').strip("'") or None
    return None


def read_with_rewrites(
    source: Path,
    relative_path: Path,
    *,
    old_name: str,
    new_name: str,
    replacements: list[tuple[str, str]],
) -> bytes:
    raw = source.read_bytes()
    if not is_text(source):
        return raw
    try:
        content = raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw
    if relative_path.as_posix() == "SKILL.md" and old_name != new_name:
        content = rewrite_frontmatter_name(content, old_name, new_name)
    for old, new in replacements:
        content = content.replace(old, new)
    return content.encode("utf-8")


def iter_source_files(source_skill: Path) -> list[Path]:
    files: list[Path] = []
    for path in source_skill.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(source_skill)
        if should_skip(relative):
            continue
        files.append(relative)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Copy an approved Codex skill package into a target repository."
    )
    parser.add_argument("source_skill", help="Source skill package directory.")
    parser.add_argument("repo", help="Target repository path.")
    parser.add_argument(
        "--mode",
        choices=["draft", "apply"],
        default="draft",
        help="draft writes under .agents/tmp; apply writes durable repo files.",
    )
    parser.add_argument(
        "--target-root",
        default=DEFAULT_TARGET_ROOT.as_posix(),
        help="Relative target skills root. Default: .agents/skills.",
    )
    parser.add_argument(
        "--target-name",
        help="Target skill folder and frontmatter name. Default: source skill name.",
    )
    parser.add_argument(
        "--replace",
        action="append",
        type=parse_replace,
        default=[],
        metavar="FROM=TO",
        help="Text replacement for copied UTF-8 text files. Repeatable.",
    )
    parser.add_argument(
        "--overwrite-approved",
        action="store_true",
        help="Overwrite existing files. Use only after exact path-level approval.",
    )
    args = parser.parse_args()

    source_skill = Path(args.source_skill).resolve()
    repo = Path(args.repo).resolve()
    if not source_skill.is_dir():
        raise SystemExit(f"Source skill path is not a directory: {source_skill}")
    if not (source_skill / "SKILL.md").is_file():
        raise SystemExit(f"Source skill package must contain SKILL.md: {source_skill}")
    if not repo.is_dir():
        raise SystemExit(f"Repo path is not a directory: {repo}")

    source_name = read_skill_name(source_skill / "SKILL.md") or source_skill.name
    target_root = parser_safe_relative_path(parser, args.target_root, argument="--target-root")
    target_name = args.target_name or source_name
    target_name_path = parser_safe_relative_path(parser, target_name, argument="--target-name")
    if len(target_name_path.parts) != 1:
        parser.error("--target-name must be a single folder name")
    if not SKILL_NAME_RE.match(target_name):
        parser.error("--target-name must be a valid skill name")

    durable_root = repo / target_root / target_name_path
    if args.mode == "draft":
        base_root = repo / TRACKING_DIR / "draft-files" / target_root / target_name_path
    else:
        base_root = durable_root
    ensure_inside(repo, base_root)

    source_files = iter_source_files(source_skill)
    created: list[str] = []
    skipped: list[str] = []
    existing_targets: list[str] = []

    for relative_path in source_files:
        source_file = source_skill / relative_path
        target_file = base_root / relative_path
        durable_file = durable_root / relative_path
        ensure_inside(repo, target_file)
        if durable_file.exists():
            existing_targets.append(str(durable_file))
        if target_file.exists() and not args.overwrite_approved:
            skipped.append(str(target_file))
            continue
        target_file.parent.mkdir(parents=True, exist_ok=True)
        content = read_with_rewrites(
            source_file,
            relative_path,
            old_name=source_name,
            new_name=target_name,
            replacements=args.replace,
        )
        target_file.write_bytes(content)
        shutil.copymode(source_file, target_file)
        created.append(str(target_file))

    print(f"mode: {args.mode}")
    print(f"source: {source_skill}")
    print(f"target package: {base_root}")
    print("created:")
    for path in created:
        print(f"- {path}")
    print("skipped:")
    for path in skipped:
        print(f"- {path}")
    print("existing durable target files:")
    for path in existing_targets:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
