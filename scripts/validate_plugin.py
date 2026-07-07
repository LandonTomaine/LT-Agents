#!/usr/bin/env python3
"""Validate the repository's Codex plugin manifest without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,62}[a-z0-9]$")
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)\."
    r"(0|[1-9]\d*)"
    r"(?:-(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*)(?:\."
    r"(?:0|[1-9]\d*|\d*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
HEX_COLOR_RE = re.compile(r"^#[0-9A-F]{6}$", re.IGNORECASE)
ALLOWED_TOP_LEVEL = {
    "id",
    "name",
    "version",
    "description",
    "skills",
    "apps",
    "mcpServers",
    "interface",
    "author",
    "homepage",
    "repository",
    "license",
    "keywords",
}
ALLOWED_AUTHOR_FIELDS = {"name", "email", "url"}
ALLOWED_INTERFACE_FIELDS = {
    "displayName",
    "shortDescription",
    "longDescription",
    "developerName",
    "category",
    "capabilities",
    "websiteURL",
    "privacyPolicyURL",
    "termsOfServiceURL",
    "brandColor",
    "composerIcon",
    "logo",
    "logoDark",
    "screenshots",
    "defaultPrompt",
    "default_prompt",
}


def reject_todo_markers(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, str):
        if "[TODO:" in value:
            errors.append(f"{path}: contains TODO placeholder")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            reject_todo_markers(item, f"{path}[{index}]", errors)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            reject_todo_markers(item, f"{path}.{key}", errors)


def reject_unknown_fields(
    data: dict[str, Any],
    allowed: set[str],
    label: str,
    errors: list[str],
) -> None:
    for key in sorted(set(data) - allowed):
        errors.append(f"{label}.{key}: unsupported field")


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
    return value


def validate_https_url(data: dict[str, Any], field: str, errors: list[str]) -> None:
    value = data.get(field)
    if value is None:
        return
    parsed = urlparse(value) if isinstance(value, str) else None
    if parsed is None or parsed.scheme != "https" or not parsed.netloc:
        errors.append(f"{field}: must be an absolute https:// URL")


def validate_relative_path(
    value: str,
    field: str,
    errors: list[str],
    *,
    expect_dir: bool = False,
    expect_file: bool = False,
) -> None:
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
        return
    if expect_dir and not target.is_dir():
        errors.append(f"{field}: path must be a directory: {value}")
    if expect_file and not target.is_file():
        errors.append(f"{field}: path must be a file: {value}")


def normalize_contract_path(raw_path: str) -> str | None:
    path = Path(raw_path)
    if path.is_absolute():
        return None
    normalized = path.as_posix().rstrip("/")
    return normalized or None


def validate_contract_path(
    data: dict[str, Any],
    field: str,
    expected: str,
    errors: list[str],
) -> None:
    value = data.get(field)
    if value is None:
        return
    normalized = normalize_contract_path(value) if isinstance(value, str) else None
    if normalized != expected:
        errors.append(f"{field}: must resolve to {expected}")


def validate_mcp_server_entries(
    servers: Any,
    source_label: str,
    field_label: str,
    errors: list[str],
) -> None:
    if not isinstance(servers, dict):
        errors.append(f"{field_label}: must be an object")
        return
    for key, value in servers.items():
        if not isinstance(key, str) or not key.strip():
            errors.append(f"{source_label}: server names must be non-empty strings")
        if not isinstance(value, dict):
            errors.append(f"{source_label}.{key}: server must be an object")


def validate_asset_path(
    base_dir: Path,
    allowed_root: Path,
    raw_path: Any,
    field: str,
    errors: list[str],
    *,
    require_png: bool = False,
) -> None:
    if not isinstance(raw_path, str) or not raw_path.strip():
        errors.append(f"{field}: must be a non-empty relative path")
        return
    candidate = PurePosixPath(raw_path.replace("\\", "/"))
    if candidate.is_absolute() or any(part in {"", ".", ".."} for part in candidate.parts):
        errors.append(f"{field}: must stay inside the plugin archive")
        return
    if require_png and candidate.suffix.lower() != ".png":
        errors.append(f"{field}: screenshots must be PNG files")
    resolved_path = (base_dir / candidate.as_posix()).resolve()
    try:
        resolved_path.relative_to(allowed_root.resolve())
    except ValueError:
        errors.append(f"{field}: must stay inside the plugin archive")
        return
    if not resolved_path.is_file():
        errors.append(f"{field}: points to a missing file")


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
    reject_todo_markers(data, "$", errors)
    reject_unknown_fields(data, ALLOWED_TOP_LEVEL, "plugin", errors)

    name = require_string(data, "name", errors)
    if name and not NAME_RE.match(name):
        errors.append(f"name: invalid plugin name: {name}")

    version = require_string(data, "version", errors)
    if version and not SEMVER_RE.match(version):
        errors.append(f"version: must be strict semver: {version}")

    require_string(data, "description", errors)
    validate_https_url(data, "homepage", errors)
    validate_https_url(data, "repository", errors)

    author = data.get("author")
    if not isinstance(author, dict):
        errors.append("author: missing object")
    else:
        reject_unknown_fields(author, ALLOWED_AUTHOR_FIELDS, "author", errors)
        require_string(data, "author.name", errors)
        validate_https_url(author, "url", errors)

    interface = data.get("interface")
    if not isinstance(interface, dict):
        errors.append("interface: missing object")
        interface = {}
    else:
        reject_unknown_fields(interface, ALLOWED_INTERFACE_FIELDS, "interface", errors)
    require_string(data, "interface.displayName", errors)
    require_string(data, "interface.shortDescription", errors)
    require_string(data, "interface.longDescription", errors)
    require_string(data, "interface.developerName", errors)
    require_string(data, "interface.category", errors)

    skills_path = require_string(data, "skills", errors)
    if skills_path:
        validate_relative_path(skills_path, "skills", errors, expect_dir=True)

    validate_contract_path(data, "apps", ".app.json", errors)

    mcp_servers = data.get("mcpServers")
    if isinstance(mcp_servers, str):
        validate_contract_path(data, "mcpServers", ".mcp.json", errors)
        validate_relative_path(mcp_servers, "mcpServers", errors, expect_file=True)
    elif mcp_servers is not None:
        validate_mcp_server_entries(
            mcp_servers,
            "mcpServers",
            "mcpServers",
            errors,
        )

    capabilities = interface.get("capabilities")
    if not isinstance(capabilities, list) or not all(
        isinstance(value, str) and value.strip() for value in capabilities
    ):
        errors.append("interface.capabilities: must be a list of strings")

    for field in ("websiteURL", "privacyPolicyURL", "termsOfServiceURL"):
        validate_https_url(interface, field, errors)

    brand_color = interface.get("brandColor")
    if brand_color is not None and (
        not isinstance(brand_color, str) or HEX_COLOR_RE.fullmatch(brand_color) is None
    ):
        errors.append("interface.brandColor: must use #RRGGBB")

    for field in ("composerIcon", "logo", "logoDark"):
        raw_path = interface.get(field)
        if raw_path is not None:
            validate_asset_path(ROOT, ROOT, raw_path, f"interface.{field}", errors)

    screenshots = interface.get("screenshots", [])
    if not isinstance(screenshots, list):
        errors.append("interface.screenshots: must be a list")
    else:
        for index, raw_path in enumerate(screenshots):
            validate_asset_path(
                ROOT,
                ROOT,
                raw_path,
                f"interface.screenshots[{index}]",
                errors,
                require_png=True,
            )

    default_prompt = interface.get("defaultPrompt", interface.get("default_prompt"))
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
    else:
        errors.append("interface.defaultPrompt: missing list")

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
