#!/usr/bin/env python3
"""Validate the repository's Codex plugin manifest without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def require_string(data: dict, path: str, errors: list[str]) -> str:
    current = data
    parts = path.split(".")
    for part in parts[:-1]:
        value = current.get(part)
        if not isinstance(value, dict):
            errors.append(f"{path}: missing object")
            return ""
        current = value
    value = current.get(parts[-1])
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{path}: missing string")
        return ""
    if "[TODO:" in value:
        errors.append(f"{path}: contains TODO placeholder")
    return value


def validate_relative_path(value: str, field: str, errors: list[str]) -> None:
    if not value.startswith("./"):
        errors.append(f"{field}: path must start with ./")
        return
    target = (ROOT / value[2:]).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        errors.append(f"{field}: path escapes repository")
        return
    if not target.exists():
        errors.append(f"{field}: path does not exist: {value}")


def main() -> int:
    if not PLUGIN_JSON.is_file():
        print(f"Missing plugin manifest: {PLUGIN_JSON}", file=sys.stderr)
        return 1

    try:
        data = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON in {PLUGIN_JSON}: {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []
    name = require_string(data, "name", errors)
    if name and not NAME_RE.match(name):
        errors.append(f"name: invalid plugin name: {name}")

    version = require_string(data, "version", errors)
    if version and not SEMVER_RE.match(version):
        errors.append(f"version: must be strict semver: {version}")

    require_string(data, "description", errors)
    require_string(data, "author.name", errors)
    require_string(data, "interface.displayName", errors)
    require_string(data, "interface.shortDescription", errors)
    require_string(data, "interface.longDescription", errors)
    require_string(data, "interface.developerName", errors)
    require_string(data, "interface.category", errors)

    skills_path = require_string(data, "skills", errors)
    if skills_path:
        validate_relative_path(skills_path, "skills", errors)

    default_prompt = data.get("interface", {}).get("defaultPrompt")
    if default_prompt is not None:
        if not isinstance(default_prompt, list):
            errors.append("interface.defaultPrompt: must be a list")
        elif len(default_prompt) > 3:
            errors.append("interface.defaultPrompt: must contain at most 3 entries")
        else:
            for index, prompt in enumerate(default_prompt):
                if not isinstance(prompt, str) or not prompt.strip():
                    errors.append(f"interface.defaultPrompt[{index}]: missing string")
                elif len(prompt) > 128:
                    errors.append(f"interface.defaultPrompt[{index}]: exceeds 128 characters")

    for field in ("apps", "mcpServers", "hooks"):
        if field in data and isinstance(data[field], str):
            validate_relative_path(data[field], field, errors)

    if "hooks" in data:
        errors.append("hooks: unsupported in plugin.json")

    if errors:
        print("Plugin validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Plugin validation passed: {PLUGIN_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
