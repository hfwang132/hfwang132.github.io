"""Generate shared Hugo publication data from one BibTeX source file."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BIB_SOURCE = REPO_ROOT / "bibliography" / "publications.bib"
JSON_DESTINATION = REPO_ROOT / "data" / "publications.json"
SUPPORTED_TYPES = {"article", "misc", "inproceedings", "proceedings"}
SUPPORTED_STATUSES = {"published", "preprint"}


class PublicationSyncError(RuntimeError):
    """Raised when the canonical bibliography is invalid or out of sync."""


def _skip_space_and_comments(source: str, cursor: int) -> int:
    while cursor < len(source):
        if source[cursor].isspace():
            cursor += 1
            continue
        if source[cursor] == "%":
            newline = source.find("\n", cursor)
            return len(source) if newline < 0 else _skip_space_and_comments(
                source, newline + 1
            )
        break
    return cursor


def _parse_braced(source: str, cursor: int) -> tuple[str, int]:
    if source[cursor] != "{":
        raise PublicationSyncError("Expected a braced BibTeX value.")
    depth = 1
    output: list[str] = []
    cursor += 1
    while cursor < len(source):
        character = source[cursor]
        escaped = cursor > 0 and source[cursor - 1] == "\\"
        if character == "{" and not escaped:
            depth += 1
            if depth > 1:
                output.append(character)
        elif character == "}" and not escaped:
            depth -= 1
            if depth == 0:
                return "".join(output).strip(), cursor + 1
            output.append(character)
        else:
            output.append(character)
        cursor += 1
    raise PublicationSyncError("Unclosed braced value in publications.bib.")


def _parse_quoted(source: str, cursor: int) -> tuple[str, int]:
    if source[cursor] != '"':
        raise PublicationSyncError("Expected a quoted BibTeX value.")
    output: list[str] = []
    cursor += 1
    while cursor < len(source):
        character = source[cursor]
        if character == '"' and source[cursor - 1] != "\\":
            return "".join(output).strip(), cursor + 1
        output.append(character)
        cursor += 1
    raise PublicationSyncError("Unclosed quoted value in publications.bib.")


def _parse_value(source: str, cursor: int) -> tuple[str, int]:
    cursor = _skip_space_and_comments(source, cursor)
    if cursor >= len(source):
        raise PublicationSyncError("Missing BibTeX field value.")
    if source[cursor] == "{":
        return _parse_braced(source, cursor)
    if source[cursor] == '"':
        return _parse_quoted(source, cursor)
    match = re.match(r"[^,}\s]+", source[cursor:])
    if not match:
        raise PublicationSyncError("Could not parse a BibTeX field value.")
    return match.group(0), cursor + len(match.group(0))


def parse_bibtex(source: str) -> list[dict[str, object]]:
    """Parse the regular BibTeX subset used by the publication page."""

    entries: list[dict[str, object]] = []
    cursor = 0
    while True:
        cursor = _skip_space_and_comments(source, cursor)
        if cursor >= len(source):
            break
        match = re.match(r"@([A-Za-z]+)\s*\{", source[cursor:])
        if not match:
            raise PublicationSyncError(
                f"Expected a BibTeX entry near character {cursor}."
            )
        entry_type = match.group(1).lower()
        if entry_type not in SUPPORTED_TYPES:
            raise PublicationSyncError(f"Unsupported BibTeX type: {entry_type}")
        cursor += match.end()
        key_end = source.find(",", cursor)
        if key_end < 0:
            raise PublicationSyncError("BibTeX entry is missing its citation key.")
        citation_key = source[cursor:key_end].strip()
        if not citation_key:
            raise PublicationSyncError("BibTeX citation key must not be empty.")
        cursor = key_end + 1
        fields: dict[str, str] = {}
        while True:
            cursor = _skip_space_and_comments(source, cursor)
            if cursor >= len(source):
                raise PublicationSyncError(f"Unclosed entry: {citation_key}")
            if source[cursor] == "}":
                cursor += 1
                break
            field_match = re.match(r"([A-Za-z][A-Za-z0-9_-]*)\s*=", source[cursor:])
            if not field_match:
                raise PublicationSyncError(
                    f"Invalid field in BibTeX entry {citation_key}."
                )
            field_name = field_match.group(1).lower()
            cursor += field_match.end()
            value, cursor = _parse_value(source, cursor)
            fields[field_name] = re.sub(r"\s+", " ", value).strip()
            cursor = _skip_space_and_comments(source, cursor)
            if cursor < len(source) and source[cursor] == ",":
                cursor += 1
            elif cursor >= len(source) or source[cursor] != "}":
                raise PublicationSyncError(
                    f"Expected a comma after {field_name} in {citation_key}."
                )
        entries.append(
            {"key": citation_key, "type": entry_type, "fields": fields}
        )
    return entries


def _required(fields: dict[str, str], field: str, key: str) -> str:
    value = fields.get(field, "").strip()
    if not value:
        raise PublicationSyncError(f"{key} is missing required field: {field}")
    return value


def build_publication_data(source: str) -> list[dict[str, object]]:
    publications: list[dict[str, object]] = []
    seen_keys: set[str] = set()
    for raw_entry in parse_bibtex(source):
        key = str(raw_entry["key"])
        if key in seen_keys:
            raise PublicationSyncError(f"Duplicate BibTeX citation key: {key}")
        seen_keys.add(key)
        entry_type = str(raw_entry["type"])
        fields = dict(raw_entry["fields"])
        title = _required(fields, "title", key)
        author_source = _required(fields, "author", key)
        authors = [part.strip() for part in re.split(r"\s+and\s+", author_source)]
        if not authors or any(not author for author in authors):
            raise PublicationSyncError(f"{key} contains an invalid author list.")
        year_text = _required(fields, "year", key)
        if not re.fullmatch(r"\d{4}", year_text):
            raise PublicationSyncError(f"{key} has an invalid year: {year_text}")
        publication_date = fields.get("date", f"{year_text}-01-01")
        try:
            date.fromisoformat(publication_date)
        except ValueError as exc:
            raise PublicationSyncError(
                f"{key} has an invalid ISO date: {publication_date}"
            ) from exc
        status = _required(fields, "status", key).lower()
        if status not in SUPPORTED_STATUSES:
            raise PublicationSyncError(
                f"{key} status must be published or preprint, not {status}."
            )
        if status == "published":
            _required(fields, "journal", key)
        if status == "preprint":
            _required(fields, "eprint", key)

        publication: dict[str, object] = {
            "key": key,
            "type": entry_type,
            "status": status,
            "title": title,
            "authors": authors,
            "date": publication_date,
            "year": int(year_text),
        }
        for field in (
            "journal",
            "volume",
            "number",
            "pages",
            "doi",
            "url",
            "eprint",
            "archiveprefix",
            "primaryclass",
        ):
            if value := fields.get(field):
                publication[field] = value
        publications.append(publication)

    publications.sort(
        key=lambda publication: (str(publication["date"]), str(publication["key"])),
        reverse=True,
    )
    return publications


def rendered_json(source: str) -> str:
    return (
        json.dumps(
            build_publication_data(source),
            ensure_ascii=False,
            indent=2,
        )
        + "\n"
    )


def synchronize(*, check: bool = False) -> None:
    if not BIB_SOURCE.is_file():
        raise PublicationSyncError(f"Missing bibliography: {BIB_SOURCE}")
    expected = rendered_json(BIB_SOURCE.read_text(encoding="utf-8"))
    if check:
        actual = (
            JSON_DESTINATION.read_text(encoding="utf-8")
            if JSON_DESTINATION.is_file()
            else ""
        )
        if actual != expected:
            raise PublicationSyncError(
                "data/publications.json is stale; run sync-publications.bat"
            )
        print("Publication data is synchronized with publications.bib.")
        return
    JSON_DESTINATION.write_text(
        expected,
        encoding="utf-8",
        newline="\n",
    )
    count = len(json.loads(expected))
    print(f"Generated data/publications.json from {count} BibTeX entries.")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate shared website publication data from BibTeX."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when the generated JSON does not match publications.bib",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        synchronize(check=args.check)
    except PublicationSyncError as exc:
        print(f"Publication sync failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
