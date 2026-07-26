#!/usr/bin/env python3
"""Rename existing Hugo post bundles to Post_YYYYMMDD_<article-title>.

The canonical date and title come from index.zh-cn.md. If a bundle has no
Chinese version, the first index.*.md file is used. Existing routes are added
as Hugo aliases before each bundle is moved.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from import_zhihu import ImportFailure, title_to_slug


REPO_ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = REPO_ROOT / "content" / "posts"
FRONT_MATTER = re.compile(
    r"\A---\r?\n(?P<body>.*?)\r?\n---(?P<tail>\r?\n)", re.DOTALL
)
FIELD = re.compile(
    r"^(?P<key>[A-Za-z][A-Za-z0-9_-]*)\s*:\s*(?P<value>.*)$"
)


@dataclass(frozen=True)
class BundleRename:
    source: Path
    destination: Path
    date: str
    title: str


def parse_scalar(value: str) -> str:
    value = value.strip()
    if value.startswith('"') and value.endswith('"'):
        try:
            return str(json.loads(value))
        except json.JSONDecodeError:
            pass
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def read_front_matter(path: Path) -> tuple[dict[str, str], str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if not match:
        raise ImportFailure(f"缺少 YAML front matter：{path}")
    values: dict[str, str] = {}
    for line in match.group("body").splitlines():
        field = FIELD.match(line)
        if field:
            values[field.group("key")] = parse_scalar(field.group("value"))
    return values, match.group("body"), text


def canonical_content_file(bundle: Path) -> Path:
    preferred = bundle / "index.zh-cn.md"
    if preferred.is_file():
        return preferred
    candidates = sorted(bundle.glob("index.*.md"))
    if not candidates:
        raise ImportFailure(f"文章目录中没有 index.*.md：{bundle}")
    return candidates[0]


def canonical_bundle_name(bundle: Path) -> tuple[str, str, str]:
    content = canonical_content_file(bundle)
    values, _, _ = read_front_matter(content)
    title = values.get("title", "").strip()
    date_value = values.get("date", "").strip()
    if not title or not date_value:
        raise ImportFailure(f"文章缺少 title 或 date：{content}")
    try:
        published = datetime.fromisoformat(date_value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ImportFailure(f"无法解析文章日期 {date_value}：{content}") from exc
    date = published.strftime("%Y%m%d")
    return f"Post_{date}_{title_to_slug(title)}", date, title


def build_plan(posts_dir: Path = POSTS_DIR) -> list[BundleRename]:
    plan: list[BundleRename] = []
    destinations: dict[str, Path] = {}
    for bundle in sorted(path for path in posts_dir.iterdir() if path.is_dir()):
        name, date, title = canonical_bundle_name(bundle)
        destination = posts_dir / name
        collision = destinations.get(name.casefold())
        if collision and collision != bundle:
            raise ImportFailure(
                f"命名冲突：{collision.name} 与 {bundle.name} 都会变成 {name}"
            )
        destinations[name.casefold()] = bundle
        if destination != bundle:
            plan.append(BundleRename(bundle, destination, date, title))
    return plan


def language_alias(content_file: Path, old_name: str) -> str:
    language = content_file.name.removeprefix("index.").removesuffix(".md")
    if language == "en":
        return f"/en/{old_name}/"
    return f"/{old_name}/"


def add_alias(content_file: Path, alias: str) -> None:
    _, front_matter, text = read_front_matter(content_file)
    newline = "\r\n" if "\r\n" in text else "\n"
    lines = front_matter.splitlines()
    alias_line = f'  - "{alias}"'
    if alias_line in lines:
        return
    aliases_at = next(
        (
            index
            for index, line in enumerate(lines)
            if line.strip() == "aliases:"
        ),
        None,
    )
    if aliases_at is None:
        insert_at = next(
            (
                index + 1
                for index, line in enumerate(lines)
                if line.startswith("date:")
            ),
            len(lines),
        )
        lines[insert_at:insert_at] = ["aliases:", alias_line]
    else:
        insert_at = aliases_at + 1
        while insert_at < len(lines) and re.match(r"^\s+-\s+", lines[insert_at]):
            insert_at += 1
        lines.insert(insert_at, alias_line)
    rewritten_front_matter = newline.join(lines)
    match = FRONT_MATTER.match(text)
    assert match
    rewritten = (
        "---"
        + newline
        + rewritten_front_matter
        + newline
        + "---"
        + match.group("tail")
        + text[match.end() :]
    )
    content_file.write_text(rewritten, encoding="utf-8", newline="")


def apply_plan(plan: list[BundleRename]) -> None:
    for item in plan:
        if item.destination.exists():
            raise ImportFailure(f"目标目录已存在：{item.destination}")
    for item in plan:
        for content_file in sorted(item.source.glob("index.*.md")):
            add_alias(
                content_file,
                language_alias(content_file, item.source.name),
            )
        item.source.rename(item.destination)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="按文章 front matter 的日期和标题统一重命名旧文章目录"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="实际写入 aliases 并移动目录；默认只显示计划",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        plan = build_plan()
        for item in plan:
            print(f"{item.source.name} -> {item.destination.name}")
        print(f"共 {len(plan)} 个文章目录需要重命名。")
        if args.apply:
            apply_plan(plan)
            print("重命名完成。")
        else:
            print("这是预览；确认后使用 --apply。")
        return 0
    except ImportFailure as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
