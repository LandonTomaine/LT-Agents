#!/usr/bin/env python3
"""Read-only repository inventory for bootstrap-repo-standards."""

from __future__ import annotations

import argparse
import json
import os
from collections import Counter
from pathlib import Path


SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".vs",
    ".idea",
    ".vscode-test",
    "node_modules",
    "bin",
    "obj",
    "dist",
    "build",
    "out",
    "coverage",
    "test-results",
    "artifacts",
    ".next",
    ".nuxt",
    ".pytest_cache",
    "__pycache__",
    ".mypy_cache",
    ".ruff_cache",
    "target",
}

ROOT_SIGNALS = [
    "README.md",
    "README",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    "global.json",
    "Directory.Build.props",
    "Directory.Build.targets",
    "Directory.Packages.props",
    ".config/dotnet-tools.json",
    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "tsconfig.json",
    "eslint.config.js",
    "eslint.config.mjs",
    ".eslintrc",
    ".eslintrc.json",
    ".stylelintrc",
    ".stylelintrc.json",
    ".prettierrc",
    "biome.json",
    "pyproject.toml",
    "ruff.toml",
    "mypy.ini",
    ".pre-commit-config.yaml",
    ".github/dependabot.yml",
    ".github/workflows/codeql.yml",
    ".github/workflows/codeql.yaml",
    "go.mod",
    "Cargo.toml",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    "Dockerfile",
    "docker-compose.yml",
    "compose.yml",
    "Procfile",
    "render.yaml",
    "fly.toml",
    "netlify.toml",
    "vercel.json",
    "firebase.json",
    "railway.json",
    "app.yaml",
    "cloudbuild.yaml",
    "azure.yaml",
    "wrangler.toml",
    "wrangler.json",
    "wrangler.jsonc",
    "supabase",
    "supabase/config.toml",
]

PROJECT_PATTERNS = {
    "dotnet_solution": [".sln"],
    "dotnet_project": [".csproj", ".fsproj", ".vbproj"],
    "node_package": ["package.json"],
    "python_project": ["pyproject.toml", "setup.py", "setup.cfg"],
    "go_module": ["go.mod"],
    "rust_package": ["Cargo.toml"],
    "java_maven": ["pom.xml"],
    "java_gradle": ["build.gradle", "build.gradle.kts"],
}

CONFIG_NAMES = {
    "ci": [".github/workflows", ".gitlab-ci.yml", "azure-pipelines.yml", "Jenkinsfile"],
    "deployment": [
        "Dockerfile",
        "docker-compose.yml",
        "compose.yml",
        "Procfile",
        "render.yaml",
        "fly.toml",
        "netlify.toml",
        "vercel.json",
        "firebase.json",
        "railway.json",
        "app.yaml",
        "cloudbuild.yaml",
        "azure.yaml",
        "wrangler.toml",
        "wrangler.json",
        "wrangler.jsonc",
        "cloudflare",
        ".cloudflare",
        "supabase",
        "deploy",
        "deployment",
        "k8s",
        "kubernetes",
        "helm",
        "infra",
        "infrastructure",
    ],
    "hooks": [".husky", ".githooks", ".pre-commit-config.yaml"],
    "security": [
        "SECURITY.md",
        ".github/dependabot.yml",
        ".github/workflows/codeql.yml",
        ".github/workflows/codeql.yaml",
    ],
    "public_repo": ["LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md"],
    "agent": ["AGENTS.md", "agent-rules", ".agents/skills", ".codex/skills"],
    "docs": ["docs", "doc", "documentation"],
    "tests": ["tests", "test", "__tests__", "spec"],
}

REPO_SKILL_DIRS = [Path(".agents") / "skills", Path(".codex") / "skills"]

ARCH_TEST_HINTS = [
    "architecture",
    "archtest",
    "netarchtest",
    "archunit",
    "dependencycruiser",
    "dependency-cruiser",
    "import-linter",
]

LOCAL_DOC_TERMS = [
    "getting started",
    "quick start",
    "quickstart",
    "local setup",
    "run locally",
    "running locally",
    "localhost",
    "dev server",
    "development server",
    "environment variables",
    "dotnet run",
    "npm run dev",
    "pnpm dev",
    "yarn dev",
    "docker compose up",
    "docker-compose up",
    "go run",
    "cargo run",
]

DEPLOY_DOC_TERMS = [
    "deploy",
    "deployment",
    "release",
    "publish",
    "preview",
    "staging",
    "production",
    "rollback",
    "smoke check",
    "health check",
    "app service",
    "cloudflare",
    "supabase",
    "wrangler",
    "vercel",
    "netlify",
    "render",
    "fly.io",
    "kubernetes",
    "helm",
]

DOC_MAINTENANCE_TERMS = [
    "documentation maintenance",
    "docs maintenance",
    "update docs",
    "update documentation",
    "stale docs",
    "stale documentation",
    "authoritative docs",
    "documentation owner",
    "docs owner",
    "keep docs",
]

STANDARDS_ROADMAP_TERMS = [
    "standards roadmap",
    "quality roadmap",
    "standards todo",
    "quality todo",
    "architecture tests",
    "source guards",
    "lint adoption",
    "linter adoption",
    "ci adoption",
    "security scanning",
    "dependency scanning",
]

UI_PACKAGE_HINTS = {
    "@angular/core",
    "@vitejs/plugin-react",
    "astro",
    "next",
    "nuxt",
    "react",
    "svelte",
    "vite",
    "vue",
}

API_PACKAGE_HINTS = {
    "@nestjs/core",
    "apollo-server",
    "express",
    "fastify",
    "graphql-yoga",
    "hapi",
    "koa",
}

CLI_PACKAGE_HINTS = {"commander", "yargs", "cac", "meow", "oclif"}

CLOUDFLARE_PACKAGE_HINTS = {
    "@cloudflare/vite-plugin",
    "@cloudflare/workers-types",
    "wrangler",
}

SUPABASE_PACKAGE_HINTS = {
    "@supabase/auth-helpers-nextjs",
    "@supabase/ssr",
    "@supabase/supabase-js",
    "supabase",
}

CLOUDFLARE_CONFIG_NAMES = {"wrangler.toml", "wrangler.json", "wrangler.jsonc"}


def should_skip_dir(path: Path) -> bool:
    if path.name in SKIP_DIRS:
        return True
    normalized = path.as_posix().lower()
    return normalized.endswith("/.agents/tmp") or normalized.endswith(
        "/.agents/tmp/bootstrap-repo-standards"
    )


def iter_files(root: Path):
    for current_root, dirs, files in os.walk(root):
        current = Path(current_root)
        dirs[:] = [d for d in dirs if not should_skip_dir(current / d)]
        for file_name in files:
            yield current / file_name


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def root_signal_paths(root: Path) -> list[str]:
    found = []
    for signal in ROOT_SIGNALS:
        path = root / signal
        if path.exists():
            found.append(signal)
    return found


def named_path_exists(root: Path, name: str) -> bool:
    return (root / name).exists()


def collect_config_paths(root: Path) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for group, names in CONFIG_NAMES.items():
        paths = []
        for name in names:
            candidate = root / name
            if candidate.exists():
                paths.append(name)
        result[group] = paths
    return result


def collect_projects(root: Path, files: list[Path]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {key: [] for key in PROJECT_PATTERNS}
    for file_path in files:
        name = file_path.name
        suffix = file_path.suffix
        for key, patterns in PROJECT_PATTERNS.items():
            if suffix in patterns or name in patterns:
                result[key].append(rel(root, file_path))
    return {key: value[:50] for key, value in result.items() if value}


def collect_package_scripts(root: Path, files: list[Path]) -> dict[str, dict[str, str]]:
    scripts: dict[str, dict[str, str]] = {}
    for package_file in [p for p in files if p.name == "package.json"]:
        try:
            data = json.loads(package_file.read_text(encoding="utf-8-sig"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError):
            continue
        package_scripts = data.get("scripts")
        if isinstance(package_scripts, dict):
            scripts[rel(root, package_file)] = {
                str(key): str(value) for key, value in sorted(package_scripts.items())
            }
    return scripts


def add_hint(result: dict[str, list[str]], key: str, value: str, limit: int = 50) -> None:
    bucket = result.setdefault(key, [])
    if value not in bucket and len(bucket) < limit:
        bucket.append(value)


def collect_runtime_surface_hints(root: Path, files: list[Path]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {
        "ui": [],
        "api_or_web": [],
        "api": [],
        "worker_or_job": [],
        "cli_or_package": [],
        "database_or_migration": [],
        "external_integration": [],
        "deployment": [],
    }
    deployment_names = {name.lower() for name in CONFIG_NAMES["deployment"]}

    for file_path in files:
        relative = rel(root, file_path)
        lowered = relative.lower()
        name = file_path.name.lower()
        suffix = file_path.suffix.lower()

        if name in deployment_names or lowered.startswith((
            ".cloudflare/",
            ".github/workflows/",
            "cloudflare/",
            "helm/",
            "infra/",
            "infrastructure/",
            "k8s/",
            "kubernetes/",
            "supabase/",
        )):
            add_hint(result, "deployment", relative)

        if name in CLOUDFLARE_CONFIG_NAMES or lowered.startswith(("cloudflare/", ".cloudflare/")):
            add_hint(result, "external_integration", f"Cloudflare: {relative}")
        if lowered.startswith("supabase/"):
            add_hint(result, "external_integration", f"Supabase: {relative}")
            if lowered.startswith("supabase/functions/"):
                add_hint(result, "worker_or_job", relative)

        if suffix in {".cshtml", ".razor", ".tsx", ".jsx", ".vue", ".svelte"} or any(
            marker in lowered
            for marker in [
                "wwwroot/",
                "public/index.html",
                "pages/",
                "views/",
                "components/",
                "vite.config",
                "next.config",
                "nuxt.config",
                "svelte.config",
                "angular.json",
            ]
        ):
            add_hint(result, "ui", relative)

        if any(
            marker in lowered
            for marker in [
                "controller",
                "controllers/",
                "routes/",
                "endpoints/",
                "openapi",
                "swagger",
                "graphql",
            ]
        ):
            add_hint(result, "api", relative)

        if any(
            marker in lowered
            for marker in [
                "worker",
                "workers/",
                "job",
                "jobs/",
                "queue",
                "scheduler",
                "hostedservice",
                "celery",
                "hangfire",
                "cron",
            ]
        ):
            add_hint(result, "worker_or_job", relative)

        if any(marker in lowered for marker in ["migrations/", "migration", "seed", "database/", "db/"]):
            add_hint(result, "database_or_migration", relative)

        if any(
            marker in lowered
            for marker in [
                "webhook",
                "integration",
                "integrations/",
                "stripe",
                "twilio",
                "sendgrid",
                "auth0",
                "oauth",
                "saml",
                "azure",
                "aws",
                "gcp",
            ]
        ):
            add_hint(result, "external_integration", relative)

        if file_path.name == "package.json":
            try:
                data = json.loads(file_path.read_text(encoding="utf-8-sig"))
            except (OSError, UnicodeDecodeError, json.JSONDecodeError):
                continue
            dependencies = set()
            for field in ["dependencies", "devDependencies", "peerDependencies", "optionalDependencies"]:
                values = data.get(field)
                if isinstance(values, dict):
                    dependencies.update(str(key) for key in values)
            if dependencies & UI_PACKAGE_HINTS:
                add_hint(result, "ui", f"{relative} dependencies")
            if dependencies & API_PACKAGE_HINTS:
                add_hint(result, "api_or_web", f"{relative} dependencies")
            if dependencies & CLI_PACKAGE_HINTS or data.get("bin"):
                add_hint(result, "cli_or_package", relative)
            if dependencies & CLOUDFLARE_PACKAGE_HINTS:
                add_hint(result, "deployment", f"Cloudflare package in {relative}")
                add_hint(result, "external_integration", f"Cloudflare package in {relative}")
            if dependencies & SUPABASE_PACKAGE_HINTS:
                add_hint(result, "external_integration", f"Supabase package in {relative}")

        if suffix in {".csproj", ".fsproj", ".vbproj"}:
            try:
                text = file_path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            lowered_text = text.lower()
            if "microsoft.net.sdk.web" in lowered_text:
                add_hint(result, "api_or_web", relative)
            if "outputtype>exe" in lowered_text:
                add_hint(result, "cli_or_package", relative)

        if name in {"cli.py", "main.py"} or "/commands/" in lowered or lowered.endswith("/cli.ts"):
            add_hint(result, "cli_or_package", relative)

    return {key: value for key, value in result.items() if value}


def collect_repo_local_skills(root: Path) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for relative_dir in REPO_SKILL_DIRS:
        skills_dir = root / relative_dir
        if not skills_dir.is_dir():
            continue
        result[relative_dir.as_posix()] = sorted(
            path.name for path in skills_dir.iterdir() if path.is_dir()
        )
    return result


def collect_husky_tasks(root: Path) -> object:
    task_runner = root / ".husky" / "task-runner.json"
    if not task_runner.exists():
        return None
    try:
        return json.loads(task_runner.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return "present-but-unreadable"


def collect_arch_hints(root: Path, files: list[Path]) -> list[str]:
    hints = []
    for file_path in files:
        relative = rel(root, file_path)
        lowered = relative.lower()
        if any(hint in lowered for hint in ARCH_TEST_HINTS):
            hints.append(relative)
            continue
        if file_path.suffix.lower() in {".cs", ".java", ".kt", ".ts", ".js", ".py"}:
            try:
                text = file_path.read_text(encoding="utf-8", errors="ignore").lower()
            except OSError:
                continue
            if any(hint in text for hint in ARCH_TEST_HINTS):
                hints.append(relative)
    return hints[:100]


def collect_doc_files(root: Path, files: list[Path]) -> list[str]:
    doc_roots = {"docs", "doc", "documentation", "agent-rules"}
    docs = []
    for file_path in files:
        parts = set(file_path.relative_to(root).parts)
        if parts & doc_roots or file_path.name in {"AGENTS.md", "README.md"}:
            if file_path.suffix.lower() in {".md", ".mdx", ".txt", ".rst"}:
                docs.append(rel(root, file_path))
    return docs[:200]


def is_doc_like(root: Path, file_path: Path) -> bool:
    relative = file_path.relative_to(root)
    parts = {part.lower() for part in relative.parts}
    if file_path.suffix.lower() not in {".md", ".mdx", ".txt", ".rst"}:
        return False
    return bool(parts & {"docs", "doc", "documentation"}) or file_path.name.lower() in {
        "readme.md",
        "readme.txt",
        "contributing.md",
    }


def collect_operational_doc_hints(root: Path, files: list[Path]) -> dict[str, list[str]]:
    hints: dict[str, list[str]] = {
        "local_setup": [],
        "deployment_release": [],
        "documentation_maintenance": [],
        "standards_roadmap": [],
    }
    for file_path in files:
        if not is_doc_like(root, file_path):
            continue
        try:
            if file_path.stat().st_size > 300_000:
                continue
            text = file_path.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            continue
        relative = rel(root, file_path)
        if any(term in text for term in LOCAL_DOC_TERMS):
            add_hint(hints, "local_setup", relative)
        if any(term in text for term in DEPLOY_DOC_TERMS):
            add_hint(hints, "deployment_release", relative)
        if any(term in text for term in DOC_MAINTENANCE_TERMS):
            add_hint(hints, "documentation_maintenance", relative)
        if any(term in text for term in STANDARDS_ROADMAP_TERMS) or file_path.name.lower() in {
            "standards-roadmap.md",
            "quality-roadmap.md",
        }:
            add_hint(hints, "standards_roadmap", relative)
    return {key: value for key, value in hints.items() if value}


def collect_gaps(
    root: Path,
    config_paths: dict[str, list[str]],
    projects: dict[str, list[str]],
    repo_local_skills: dict[str, list[str]],
    operational_doc_hints: dict[str, list[str]],
    runtime_surface_hints: dict[str, list[str]],
) -> list[str]:
    gaps = []
    has_code_or_runtime = bool(projects or runtime_surface_hints)
    if not named_path_exists(root, "README.md") and not named_path_exists(root, "README"):
        gaps.append("No root README found.")
    if not config_paths.get("public_repo"):
        gaps.append("No LICENSE, CONTRIBUTING.md, or CODE_OF_CONDUCT.md found; ask if this repo will be public or shared externally.")

    if not has_code_or_runtime:
        gaps.append(
            "No project/runtime detected; ask scope before proposing docs, hooks, CI, tests, or agent scaffolding."
        )
        return gaps

    if not named_path_exists(root, "AGENTS.md"):
        gaps.append("No AGENTS.md agent entrypoint found; ask before adding one.")
    if not named_path_exists(root, ".editorconfig"):
        gaps.append("No root .editorconfig found; treat as optional until coding standards are in scope.")
    if not config_paths.get("docs"):
        gaps.append("No docs/ directory found; a README may be enough for small repos.")
    if not config_paths.get("ci"):
        gaps.append("No common CI configuration found; treat as optional unless merge gates are in scope.")
    if not config_paths.get("hooks"):
        gaps.append("No common tracked local hook configuration found; treat as optional developer convenience.")
    if not config_paths.get("security"):
        gaps.append("No obvious CodeQL, Dependabot, or security policy config found; ask whether security scanning is in scope.")
    if projects and not config_paths.get("tests"):
        gaps.append("No conventional test directory found.")
    if config_paths.get("docs") and not named_path_exists(root, "docs/development/validation.md"):
        gaps.append("No dedicated local/deployed validation doc found.")
    if projects and not operational_doc_hints.get("local_setup"):
        gaps.append("No obvious local setup/run documentation found.")
    if projects and not operational_doc_hints.get("deployment_release"):
        gaps.append("No obvious deployment/release documentation found.")
    if "node_package" in projects:
        for package_path in projects["node_package"]:
            package_dir = (root / package_path).parent
            has_lint_config = any(
                (package_dir / name).exists()
                for name in [
                    "eslint.config.js",
                    "eslint.config.mjs",
                    ".eslintrc",
                    ".eslintrc.json",
                    "biome.json",
                ]
            )
            if not has_lint_config:
                gaps.append(f"Node/JS package {package_path} has no obvious adjacent ESLint or Biome config.")
    if "dotnet_solution" in projects or "dotnet_project" in projects:
        if not named_path_exists(root, "Directory.Packages.props"):
            gaps.append(".NET project found without root Directory.Packages.props central package file.")
    if ".codex/skills" in repo_local_skills and ".agents/skills" not in repo_local_skills:
        gaps.append("Legacy .codex/skills found without .agents/skills; consider an approved migration plan.")
    return gaps


def scan(root: Path) -> dict:
    root = root.resolve()
    files = list(iter_files(root))
    ext_counts = Counter(path.suffix.lower() or "<none>" for path in files)
    config_paths = collect_config_paths(root)
    projects = collect_projects(root, files)
    repo_local_skills = collect_repo_local_skills(root)
    operational_doc_hints = collect_operational_doc_hints(root, files)
    runtime_surface_hints = collect_runtime_surface_hints(root, files)
    return {
        "root": str(root),
        "file_count_scanned": len(files),
        "top_extensions": dict(ext_counts.most_common(25)),
        "root_signals": root_signal_paths(root),
        "configs": config_paths,
        "projects": projects,
        "package_scripts": collect_package_scripts(root, files),
        "runtime_surface_hints": runtime_surface_hints,
        "operational_doc_hints": operational_doc_hints,
        "repo_local_skills": repo_local_skills,
        "codex_skills": repo_local_skills.get(".codex/skills", []),
        "husky_tasks": collect_husky_tasks(root),
        "architecture_hints": collect_arch_hints(root, files),
        "docs_and_agent_files": collect_doc_files(root, files),
        "gap_hints": collect_gaps(
            root,
            config_paths,
            projects,
            repo_local_skills,
            operational_doc_hints,
            runtime_surface_hints,
        ),
    }


def print_markdown(data: dict) -> None:
    print(f"# Repo Scan: {data['root']}")
    print()
    print(f"- Files scanned: {data['file_count_scanned']}")
    print(f"- Root signals: {', '.join(data['root_signals']) or 'none'}")
    print()
    print("## Projects")
    for key, values in data["projects"].items():
        print(f"- {key}: {', '.join(values[:10])}")
    if not data["projects"]:
        print("- none detected")
    print()
    print("## Configs")
    for key, values in data["configs"].items():
        print(f"- {key}: {', '.join(values) if values else 'none'}")
    print()
    print("## Package Scripts")
    if data["package_scripts"]:
        for package_path, scripts in data["package_scripts"].items():
            print(f"- {package_path}: {', '.join(scripts.keys())}")
    else:
        print("- none")
    print()
    print("## Runtime Surface Hints")
    if data["runtime_surface_hints"]:
        for key, values in data["runtime_surface_hints"].items():
            print(f"- {key}: {', '.join(values[:10])}")
    else:
        print("- none")
    print()
    print("## Operational Doc Hints")
    if data["operational_doc_hints"]:
        for key, values in data["operational_doc_hints"].items():
            print(f"- {key}: {', '.join(values[:10])}")
    else:
        print("- none")
    print()
    print("## Repo-Local Skills")
    if data["repo_local_skills"]:
        for skill_dir, skills in data["repo_local_skills"].items():
            print(f"- {skill_dir}: {', '.join(skills) if skills else 'none'}")
    else:
        print("- none")
    print()
    print("## Architecture Hints")
    for hint in data["architecture_hints"][:25]:
        print(f"- {hint}")
    if not data["architecture_hints"]:
        print("- none")
    print()
    print("## Docs And Agent Files")
    for path in data["docs_and_agent_files"][:50]:
        print(f"- {path}")
    if not data["docs_and_agent_files"]:
        print("- none")
    print()
    print("## Gap Hints")
    for gap in data["gap_hints"]:
        print(f"- {gap}")
    if not data["gap_hints"]:
        print("- no obvious first-pass gaps")


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only repository standards inventory.")
    parser.add_argument("repo", help="Repository path to scan.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    args = parser.parse_args()

    root = Path(args.repo)
    if not root.is_dir():
        raise SystemExit(f"Repo path is not a directory: {root}")

    data = scan(root)
    if args.json:
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        print_markdown(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
