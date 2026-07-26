#!/usr/bin/env python3
"""Apply verified Zhihu publication timestamps to historical Hugo posts.

The input is a reviewable JSON file. Each entry must contain an exact local
title, the matched Zhihu URL, and the page's datePublished timestamp. The
script updates every language file in the bundle, stores originalURL, renames
the bundle with the authoritative date, and preserves all previous routes.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from import_zhihu import (
    ImportFailure,
    SITE_TIMEZONE,
    title_to_slug,
    validate_zhihu_url,
)
from migrate_post_names import (
    POSTS_DIR,
    apply_plan,
    build_plan,
    canonical_content_file,
    read_front_matter,
)


DEFAULT_MAPPING = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "zhihu-publication-dates.json"
)


@dataclass(frozen=True)
class ZhihuDate:
    local_title: str
    zhihu_title: str
    source_url: str
    published_at: datetime

    @property
    def bundle_name(self) -> str:
        return (
            f"Post_{self.published_at.astimezone(SITE_TIMEZONE):%Y%m%d}_"
            f"{title_to_slug(self.local_title)}"
        )


def parse_timestamp(value: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError as exc:
        raise ImportFailure(f"Invalid datePublished timestamp: {value}") from exc
    if parsed.tzinfo is None:
        raise ImportFailure(f"datePublished must include a timezone: {value}")
    return parsed.astimezone(SITE_TIMEZONE)


def load_mapping(path: Path) -> list[ZhihuDate]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ImportFailure(f"Cannot read mapping file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ImportFailure(f"Invalid JSON mapping file: {path}") from exc
    if not isinstance(raw, list):
        raise ImportFailure("The date mapping must be a JSON array.")
    entries: list[ZhihuDate] = []
    seen_titles: set[str] = set()
    seen_urls: set[str] = set()
    for index, item in enumerate(raw, start=1):
        if not isinstance(item, dict):
            raise ImportFailure(f"Mapping entry {index} must be an object.")
        try:
            local_title = str(item["localTitle"]).strip()
            zhihu_title = str(item["zhihuTitle"]).strip()
            source_url = str(item["sourceURL"]).strip()
            published_at = parse_timestamp(str(item["datePublished"]))
        except KeyError as exc:
            raise ImportFailure(
                f"Mapping entry {index} is missing {exc.args[0]}."
            ) from exc
        validate_zhihu_url(source_url)
        if not local_title or not zhihu_title:
            raise ImportFailure(f"Mapping entry {index} has an empty title.")
        if local_title in seen_titles:
            raise ImportFailure(f"Duplicate localTitle: {local_title}")
        if source_url in seen_urls:
            raise ImportFailure(f"Duplicate sourceURL: {source_url}")
        seen_titles.add(local_title)
        seen_urls.add(source_url)
        entries.append(
            ZhihuDate(
                local_title,
                zhihu_title,
                source_url,
                published_at,
            )
        )
    return entries


def index_bundles(posts_dir: Path = POSTS_DIR) -> dict[str, Path]:
    indexed: dict[str, Path] = {}
    for bundle in sorted(path for path in posts_dir.iterdir() if path.is_dir()):
        content_file = canonical_content_file(bundle)
        values, _, _ = read_front_matter(content_file)
        title = values.get("title", "").strip()
        if not title:
            raise ImportFailure(f"Post has no title: {content_file}")
        if title in indexed:
            raise ImportFailure(f"Duplicate local post title: {title}")
        indexed[title] = bundle
    return indexed


def rewrite_metadata(
    content_file: Path,
    *,
    published_at: datetime,
    source_url: str,
) -> None:
    text = content_file.read_text(encoding="utf-8")
    newline = "\r\n" if "\r\n" in text else "\n"
    lines = text.splitlines()
    front_end = next(
        (
            index
            for index in range(1, len(lines))
            if lines[index].strip() == "---"
        ),
        None,
    )
    if front_end is None:
        raise ImportFailure(f"Invalid front matter: {content_file}")
    date_line = f"date: {published_at.astimezone(SITE_TIMEZONE).isoformat()}"
    original_line = f"originalURL: {json.dumps(source_url)}"
    date_at = next(
        (
            index
            for index in range(1, front_end)
            if re.match(r"^date\s*:", lines[index])
        ),
        None,
    )
    if date_at is None:
        raise ImportFailure(f"Post has no date: {content_file}")
    lines[date_at] = date_line
    original_at = next(
        (
            index
            for index in range(1, front_end)
            if re.match(r"^originalURL\s*:", lines[index])
        ),
        None,
    )
    if original_at is None:
        lines.insert(date_at + 1, original_line)
    else:
        lines[original_at] = original_line
    content_file.write_text(newline.join(lines) + newline, encoding="utf-8")


def apply_entries(
    entries: list[ZhihuDate],
    posts_dir: Path = POSTS_DIR,
) -> list[tuple[Path, Path]]:
    bundles = index_bundles(posts_dir)
    missing = [
        entry.local_title
        for entry in entries
        if entry.local_title not in bundles
    ]
    if missing:
        raise ImportFailure(
            "Mapping titles not found locally: " + ", ".join(missing)
        )
    expected_destinations: dict[str, str] = {}
    for entry in entries:
        folded = entry.bundle_name.casefold()
        previous = expected_destinations.get(folded)
        if previous:
            raise ImportFailure(
                f"Bundle name collision: {previous} and {entry.local_title}"
            )
        expected_destinations[folded] = entry.local_title

    moves: list[tuple[Path, Path]] = []
    for entry in entries:
        source = bundles[entry.local_title]
        destination = posts_dir / entry.bundle_name
        moves.append((source, destination))
        for content_file in sorted(source.glob("index.*.md")):
            rewrite_metadata(
                content_file,
                published_at=entry.published_at,
                source_url=entry.source_url,
            )
    apply_plan(build_plan(posts_dir))
    return moves


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Apply reviewed Zhihu datePublished metadata to historical posts."
        )
    )
    parser.add_argument(
        "--mapping",
        type=Path,
        default=DEFAULT_MAPPING,
        help=f"reviewed JSON mapping (default: {DEFAULT_MAPPING})",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="update front matter and rename bundles; default is a preview",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        entries = load_mapping(args.mapping)
        bundles = index_bundles()
        for entry in entries:
            source = bundles.get(entry.local_title)
            if source is None:
                raise ImportFailure(
                    f"Mapping title not found locally: {entry.local_title}"
                )
            print(
                f"{source.name} -> {entry.bundle_name} "
                f"({entry.source_url})"
            )
        print(f"{len(entries)} verified Zhihu posts in the mapping.")
        if args.apply:
            apply_entries(entries)
            print("Zhihu publication dates applied.")
        else:
            print("Preview only; use --apply after reviewing the mapping.")
        return 0
    except ImportFailure as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
