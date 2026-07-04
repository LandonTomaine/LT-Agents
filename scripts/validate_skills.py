#!/usr/bin/env python3
"""Validate the skill catalog structure without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: missing opening frontmatter delimiter"]
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        return {}, [f"{path}: missing closing frontmatter delimiter"]

    data: dict[str, str] = {}
    for lineno, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{path}:{lineno}: invalid frontmatter line")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, errors


def iter_markdown_files(skill_dir: Path) -> list[Path]:
    return sorted(skill_dir.rglob("*.md"))


def validate_links(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if (
            not target
            or target.startswith("#")
            or "://" in target
            or target.startswith("mailto:")
        ):
            continue
        target_path = target.split("#", 1)[0]
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path}: link escapes repo: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path}: broken relative link: {target}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir}: missing SKILL.md"]

    frontmatter, fm_errors = parse_frontmatter(skill_md)
    errors.extend(fm_errors)

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")
    if not name:
        errors.append(f"{skill_md}: missing frontmatter name")
    elif not NAME_RE.match(name):
        errors.append(f"{skill_md}: invalid skill name: {name}")
    elif name != skill_dir.name:
        errors.append(f"{skill_md}: name '{name}' does not match directory '{skill_dir.name}'")

    if not description:
        errors.append(f"{skill_md}: missing frontmatter description")

    extra_docs = [
        path
        for path in skill_dir.iterdir()
        if path.is_file() and path.name.upper() in {"README.md", "CHANGELOG.md", "INSTALLATION.md"}
    ]
    for path in extra_docs:
        errors.append(f"{path}: extra package-level doc; keep runtime guidance in SKILL.md/references")

    for md_path in iter_markdown_files(skill_dir):
        errors.extend(validate_links(md_path))

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"Missing skills directory: {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("No skill directories found.", file=sys.stderr)
        return 1

    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    for skill_dir in skill_dirs:
        print(f"- {skill_dir.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
