"""Build the Hugo site locally and publish its output to ``gh-pages``.

The source branch remains the authoritative copy of the Hugo project.  The
deployment branch contains only the generated website and is updated through
an isolated temporary Git worktree, so local source files and private drafts
cannot leak into the published branch.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BASE_URL = "https://haifei.pro/"
DEFAULT_DOMAIN = "haifei.pro"
DEFAULT_BRANCH = "gh-pages"
DEFAULT_REMOTE = "origin"


class DeployError(RuntimeError):
    """Raised when a deployment safety check fails."""


def run(
    command: list[str],
    *,
    cwd: Path = REPO_ROOT,
    capture: bool = False,
) -> subprocess.CompletedProcess[str]:
    printable = subprocess.list2cmdline(command)
    print(f"> {printable}")
    return subprocess.run(
        command,
        cwd=cwd,
        check=True,
        text=True,
        capture_output=capture,
    )


def git_output(*arguments: str, cwd: Path = REPO_ROOT) -> str:
    return run(["git", *arguments], cwd=cwd, capture=True).stdout.strip()


def require_clean_worktree() -> None:
    changes = git_output("status", "--porcelain", "--untracked-files=no")
    if changes:
        raise DeployError(
            "The source worktree has uncommitted tracked changes. "
            "Commit them first (normally by running updates.bat) so the "
            "published site corresponds to a reproducible source revision."
        )


def build_site(destination: Path, *, base_url: str, domain: str) -> None:
    hugo = shutil.which("hugo")
    if not hugo:
        raise DeployError("Hugo was not found on PATH.")

    cache_dir = destination.parent / "hugo-cache"
    run(
        [
            hugo,
            "--gc",
            "--minify",
            "--cleanDestinationDir",
            "--destination",
            str(destination),
            "--cacheDir",
            str(cache_dir),
            "--baseURL",
            base_url,
        ]
    )

    (destination / "CNAME").write_text(domain + "\n", encoding="utf-8")
    (destination / ".nojekyll").touch()
    verify_build(destination, base_url=base_url, domain=domain)


def verify_build(destination: Path, *, base_url: str, domain: str) -> None:
    index_path = destination / "index.html"
    if not index_path.is_file():
        raise DeployError("Hugo did not create index.html.")

    cname = (destination / "CNAME").read_text(encoding="utf-8").strip()
    if cname != domain:
        raise DeployError(f"CNAME contains {cname!r}, expected {domain!r}.")

    homepage = index_path.read_text(encoding="utf-8")
    if base_url not in homepage:
        raise DeployError(f"The generated homepage does not reference {base_url}.")

    forbidden_suffixes = {".md", ".markdown", ".toml", ".py", ".bat", ".sh"}
    forbidden = [
        path.relative_to(destination)
        for path in destination.rglob("*")
        if path.is_file() and path.suffix.lower() in forbidden_suffixes
    ]
    if forbidden:
        preview = ", ".join(str(path) for path in forbidden[:10])
        raise DeployError(f"Source-like files appeared in the build: {preview}")

    files = [path for path in destination.rglob("*") if path.is_file()]
    total_size = sum(path.stat().st_size for path in files)
    largest = max(files, key=lambda path: path.stat().st_size)
    largest_size = largest.stat().st_size
    if largest_size > 100 * 1024 * 1024:
        raise DeployError(
            f"{largest.relative_to(destination)} is larger than GitHub's "
            "100 MiB file limit."
        )

    print(
        "Build verified: "
        f"{len(files)} files, {total_size / 1024 / 1024:.1f} MiB total, "
        f"largest file {largest_size / 1024 / 1024:.1f} MiB."
    )


def replace_worktree_contents(worktree: Path, build: Path) -> None:
    run(
        ["git", "rm", "-r", "--ignore-unmatch", "."],
        cwd=worktree,
    )
    shutil.copytree(build, worktree, dirs_exist_ok=True)
    run(["git", "add", "-A"], cwd=worktree)


def publish_build(
    build: Path,
    *,
    remote: str,
    branch: str,
    source_revision: str,
) -> bool:
    run(["git", "fetch", remote, branch])
    remote_ref = f"refs/remotes/{remote}/{branch}"
    run(["git", "rev-parse", "--verify", remote_ref], capture=True)

    temporary_parent = build.parent
    worktree = temporary_parent / "worktree"
    run(["git", "worktree", "add", "--detach", str(worktree), remote_ref])
    try:
        replace_worktree_contents(worktree, build)
        diff = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=worktree,
            check=False,
        )
        if diff.returncode == 0:
            print("The gh-pages branch already matches the local build.")
            return False
        if diff.returncode != 1:
            raise subprocess.CalledProcessError(diff.returncode, diff.args)

        run(
            [
                "git",
                "-c",
                "commit.gpgsign=false",
                "commit",
                "-m",
                f"deploy: {source_revision}",
            ],
            cwd=worktree,
        )
        run(["git", "push", remote, f"HEAD:{branch}"], cwd=worktree)
        return True
    finally:
        run(["git", "worktree", "remove", "--force", str(worktree)])
        run(["git", "worktree", "prune"])


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build Hugo locally and publish generated files to gh-pages."
    )
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--domain", default=DEFAULT_DOMAIN)
    parser.add_argument("--branch", default=DEFAULT_BRANCH)
    parser.add_argument("--remote", default=DEFAULT_REMOTE)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="build and verify locally without fetching or pushing",
    )
    parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if not args.allow_dirty:
            require_clean_worktree()
        source_revision = git_output("rev-parse", "HEAD")
        with tempfile.TemporaryDirectory(prefix="haifei-pages-") as directory:
            temporary = Path(directory).resolve()
            build = temporary / "site"
            build_site(build, base_url=args.base_url, domain=args.domain)
            if args.dry_run:
                print("Dry run completed; nothing was pushed.")
                return 0
            changed = publish_build(
                build,
                remote=args.remote,
                branch=args.branch,
                source_revision=source_revision,
            )
        if changed:
            print(
                f"Published {source_revision} to {args.remote}/{args.branch} "
                f"for {args.base_url}"
            )
        return 0
    except (DeployError, FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(f"Deployment failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
