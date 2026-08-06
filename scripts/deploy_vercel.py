"""Build the Hugo site locally and deploy only static output to Vercel."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VERCEL_DIR = REPO_ROOT / ".vercel"
OUTPUT_DIR = VERCEL_DIR / "output"
STATIC_DIR = OUTPUT_DIR / "static"
DEFAULT_BASE_URL = "https://haifei.pro/"
MAX_UPLOAD_FILES = 15_000
MAX_UPLOAD_SIZE = 100 * 1024 * 1024
VERCEL_ROUTES = [
    # Vercel's Build Output API serves static files literally. Hugo emits
    # pretty URLs as <route>/index.html, so resolve real assets first and
    # then map trailing-slash page requests to their generated HTML file.
    {"handle": "filesystem"},
    {"src": "/(.+)/", "dest": "/$1/index.html"},
]
VERCEL_OUTPUT_CONFIG = {
    "version": 3,
    "routes": VERCEL_ROUTES,
}


class DeployError(RuntimeError):
    """Raised when a local build or Vercel deployment is unsafe."""


def run(
    command: list[str],
    *,
    cwd: Path = REPO_ROOT,
    capture: bool = False,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    printable = subprocess.list2cmdline(command)
    print(f"> {printable}")
    return subprocess.run(
        command,
        cwd=cwd,
        check=True,
        text=True,
        capture_output=capture,
        env=env,
    )


def vercel_cli() -> Path:
    configured = os.environ.get("VERCEL_CLI")
    if configured:
        candidate = Path(configured).expanduser().resolve()
        if candidate.is_file():
            return candidate
        raise DeployError(f"VERCEL_CLI does not exist: {candidate}")

    installed = shutil.which("vercel") or shutil.which("vercel.cmd")
    if installed:
        return Path(installed).resolve()

    portable = REPO_ROOT / ".tools" / "vercel-cli" / "node_modules" / ".bin"
    names = ("vercel.cmd", "vercel") if os.name == "nt" else ("vercel",)
    for name in names:
        candidate = portable / name
        if candidate.is_file():
            return candidate

    raise DeployError(
        "Vercel CLI was not found. Install it with `npm install -g vercel` "
        "or restore the ignored .tools/vercel-cli directory."
    )


def require_linked_project() -> None:
    project_file = VERCEL_DIR / "project.json"
    if not project_file.is_file():
        raise DeployError(
            "This checkout is not linked to a Vercel project. Run "
            "`deploy-vercel.bat --link` once, then retry."
        )

    try:
        project = json.loads(project_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise DeployError(f"Invalid Vercel project file: {project_file}") from exc

    if not project.get("projectId") or not project.get("orgId"):
        raise DeployError(f"Incomplete Vercel project file: {project_file}")


def build_site(*, base_url: str) -> None:
    hugo = shutil.which("hugo")
    if not hugo:
        raise DeployError("Hugo was not found on PATH.")

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    STATIC_DIR.mkdir(parents=True)

    cache_dir = REPO_ROOT / ".hugo-cache" / "vercel"
    run(
        [
            hugo,
            "--gc",
            "--minify",
            "--cleanDestinationDir",
            "--destination",
            str(STATIC_DIR),
            "--cacheDir",
            str(cache_dir),
            "--baseURL",
            base_url,
        ]
    )

    config = prepare_static_files()
    (OUTPUT_DIR / "config.json").write_text(
        json.dumps(config, indent=2) + "\n",
        encoding="utf-8",
    )
    verify_build(base_url=base_url)


def prepare_static_files() -> dict[str, object]:
    """Store non-ASCII paths safely while preserving their public URLs.

    On Windows, Vercel CLI currently omits files whose local path contains
    non-ASCII characters from a prebuilt upload.  Hugo intentionally uses
    Chinese post slugs, so move those files to deterministic ASCII-only
    storage names and expose their original URL through Build Output API
    overrides.
    """

    overrides: dict[str, dict[str, str]] = {}
    relocated = 0
    files = sorted(path for path in STATIC_DIR.rglob("*") if path.is_file())
    for source in files:
        relative = source.relative_to(STATIC_DIR).as_posix()
        if relative.isascii():
            continue

        digest = hashlib.sha256(relative.encode("utf-8")).hexdigest()
        suffix = source.suffix.lower()
        stored_relative = Path("_vercel_unicode") / f"{digest}{suffix}"
        target = STATIC_DIR / stored_relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            raise DeployError(f"Vercel-safe path collision: {stored_relative}")
        source.replace(target)
        overrides[stored_relative.as_posix()] = {"path": relative}
        relocated += 1

    config = dict(VERCEL_OUTPUT_CONFIG)
    if overrides:
        config["overrides"] = overrides
    print(f"Prepared {relocated} non-ASCII files for Vercel-safe upload.")
    return config


def verify_build(*, base_url: str) -> None:
    index_path = STATIC_DIR / "index.html"
    if not index_path.is_file():
        raise DeployError("Hugo did not create index.html.")

    homepage = index_path.read_text(encoding="utf-8")
    if base_url not in homepage:
        raise DeployError(f"The generated homepage does not reference {base_url}.")

    forbidden_suffixes = {".md", ".markdown", ".toml", ".py", ".bat", ".sh"}
    forbidden = [
        path.relative_to(STATIC_DIR)
        for path in STATIC_DIR.rglob("*")
        if path.is_file() and path.suffix.lower() in forbidden_suffixes
    ]
    if forbidden:
        preview = ", ".join(str(path) for path in forbidden[:10])
        raise DeployError(f"Source-like files appeared in the build: {preview}")

    files = [path for path in STATIC_DIR.rglob("*") if path.is_file()]
    if not files:
        raise DeployError("The Hugo build is empty.")
    unsafe_paths = [
        path.relative_to(STATIC_DIR)
        for path in files
        if not path.relative_to(STATIC_DIR).as_posix().isascii()
    ]
    if unsafe_paths:
        preview = ", ".join(str(path) for path in unsafe_paths[:10])
        raise DeployError(f"Non-ASCII upload paths remain: {preview}")
    if len(files) > MAX_UPLOAD_FILES:
        raise DeployError(
            f"The build contains {len(files)} files; Vercel Hobby accepts at "
            f"most {MAX_UPLOAD_FILES:,} CLI-uploaded files."
        )

    total_size = sum(path.stat().st_size for path in files)
    if total_size > MAX_UPLOAD_SIZE:
        raise DeployError(
            f"The build is {total_size / 1024 / 1024:.1f} MiB; Vercel Hobby "
            "accepts at most 100 MiB per CLI deployment."
        )

    largest = max(files, key=lambda path: path.stat().st_size)
    print(
        "Build verified: "
        f"{len(files)} files, {total_size / 1024 / 1024:.1f} MiB total, "
        f"largest file {largest.stat().st_size / 1024 / 1024:.1f} MiB."
    )


def link_project(cli: Path) -> None:
    run([str(cli), "link"], env=vercel_environment(cli))


def vercel_environment(cli: Path) -> dict[str, str]:
    environment = os.environ.copy()
    cli_bin = cli.parent
    node_roots = sorted((REPO_ROOT / ".tools").glob("node-v*-win-x64"))
    path_entries = [str(cli_bin)]
    if node_roots:
        path_entries.insert(0, str(node_roots[-1]))
    environment["PATH"] = os.pathsep.join(
        [*path_entries, environment.get("PATH", "")]
    )
    return environment


def deploy(cli: Path) -> str:
    result = run(
        [
            str(cli),
            "deploy",
            "--prebuilt",
            "--prod",
            "--yes",
        ],
        capture=True,
        env=vercel_environment(cli),
    )
    if result.stderr:
        print(result.stderr, file=sys.stderr, end="")
    urls = re.findall(
        r"https://[A-Za-z0-9.-]+\.vercel\.app",
        f"{result.stdout}\n{result.stderr}",
    )
    if not urls:
        raise DeployError(
            "Vercel finished without returning a production deployment URL."
        )
    deployment_url = urls[-1]
    print(f"Published to {deployment_url}")
    return deployment_url


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build Hugo locally and publish only static output to Vercel."
    )
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument(
        "--link",
        action="store_true",
        help="interactively link this checkout to a Vercel project",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="build and validate locally without contacting Vercel",
    )
    parser.add_argument(
        "--keep-build",
        action="store_true",
        help="keep .vercel/output after a successful build or deployment",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        cli = vercel_cli()
        if args.link:
            link_project(cli)
            return 0

        if not args.dry_run:
            require_linked_project()
        build_site(base_url=args.base_url)
        if args.dry_run:
            print("Dry run completed; nothing was uploaded.")
        else:
            deploy(cli)
        if not args.keep_build:
            shutil.rmtree(OUTPUT_DIR)
        return 0
    except (DeployError, FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"Deployment failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
