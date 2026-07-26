"""Pull the private Overleaf CV source and render it as Hugo content.

The Overleaf checkout lives under .external/ and is intentionally ignored by
the public website repository.  The current CV uses a small, regular subset of
LaTeX, so a dependency-free converter is preferable to copying rendered HTML
or maintaining a second hand-edited CV.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
OVERLEAF_DIR = REPO_ROOT / ".external" / "overleaf-cv"
OVERLEAF_URL = "https://git@git.overleaf.com/6a60bd158a3c2cea9ab34b7e"
MAIN_TEX = "resume.tex"
ENGLISH_PAGE = REPO_ROOT / "content" / "cv" / "index.en.md"
CHINESE_PAGE = REPO_ROOT / "content" / "cv" / "index.zh-cn.md"
CV_DATA = REPO_ROOT / "data" / "cv.json"
PDF_DESTINATION = REPO_ROOT / "static" / "cv" / "Haifei-Wang-CV.pdf"


class CvSyncError(RuntimeError):
    """A user-facing synchronization failure."""


def run(command: list[str], *, cwd: Path) -> None:
    printable = subprocess.list2cmdline(command)
    print(f"> {printable}")
    try:
        subprocess.run(command, cwd=cwd, check=True)
    except FileNotFoundError as exc:
        raise CvSyncError(f"Command not found: {command[0]}") from exc
    except subprocess.CalledProcessError as exc:
        raise CvSyncError(
            f"Command failed with exit code {exc.returncode}: {printable}"
        ) from exc


def ensure_checkout(*, pull: bool) -> None:
    if not (OVERLEAF_DIR / ".git").is_dir():
        OVERLEAF_DIR.parent.mkdir(parents=True, exist_ok=True)
        run(
            ["git", "clone", OVERLEAF_URL, str(OVERLEAF_DIR)],
            cwd=REPO_ROOT,
        )
    if pull:
        run(
            [
                "git",
                "-c",
                f"safe.directory={OVERLEAF_DIR.as_posix()}",
                "pull",
                "--ff-only",
            ],
            cwd=OVERLEAF_DIR,
        )


def source_revision() -> str:
    result = subprocess.run(
        [
            "git",
            "-c",
            f"safe.directory={OVERLEAF_DIR.as_posix()}",
            "rev-parse",
            "--short",
            "HEAD",
        ],
        cwd=OVERLEAF_DIR,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def strip_latex_comments(source: str) -> str:
    cleaned: list[str] = []
    for line in source.splitlines():
        for index, character in enumerate(line):
            if character != "%":
                continue
            preceding = 0
            cursor = index - 1
            while cursor >= 0 and line[cursor] == "\\":
                preceding += 1
                cursor -= 1
            if preceding % 2 == 0:
                line = line[:index]
                break
        cleaned.append(line.rstrip())
    return "\n".join(cleaned)


def parse_group(source: str, start: int) -> tuple[str, int]:
    if start >= len(source) or source[start] != "{":
        raise CvSyncError("Expected a LaTeX group while converting the CV.")
    depth = 0
    for index in range(start, len(source)):
        character = source[index]
        escaped = index > 0 and source[index - 1] == "\\"
        if character == "{" and not escaped:
            depth += 1
        elif character == "}" and not escaped:
            depth -= 1
            if depth == 0:
                return source[start + 1 : index], index + 1
    raise CvSyncError("Unclosed LaTeX group in the CV source.")


def command_arguments(
    source: str, command_start: int, name: str, count: int
) -> tuple[list[str], int] | None:
    cursor = command_start + len(name) + 1
    while cursor < len(source) and source[cursor].isspace():
        cursor += 1
    arguments: list[str] = []
    try:
        for _ in range(count):
            while cursor < len(source) and source[cursor].isspace():
                cursor += 1
            argument, cursor = parse_group(source, cursor)
            arguments.append(argument)
    except CvSyncError:
        return None
    return arguments, cursor


def convert_inline(source: str) -> str:
    source = (
        source.replace(r"Schr\"odinger", "Schrödinger")
        .replace("---", "—")
        .replace("--", "–")
    )
    output: list[str] = []
    cursor = 0
    single_argument = {
        "textbf": ("<strong>", "</strong>"),
        "textit": ("<em>", "</em>"),
        "emph": ("<em>", "</em>"),
        "texttt": ("<code>", "</code>"),
    }
    symbol_commands = {
        "&": "&amp;",
        "%": "%",
        "_": "_",
        "#": "#",
        "$": "$",
        "{": "{",
        "}": "}",
        "times": "×",
        "textperiodcentered": "·",
        "LaTeX": "LaTeX",
    }

    while cursor < len(source):
        character = source[cursor]
        if character == "\\":
            if cursor + 1 < len(source) and source[cursor + 1] == "\\":
                output.append(" ")
                cursor += 2
                continue
            match = re.match(r"\\([A-Za-z]+|.)", source[cursor:])
            if not match:
                output.append("\\")
                cursor += 1
                continue
            name = match.group(1)
            if name == "href":
                parsed = command_arguments(source, cursor, name, 2)
                if parsed:
                    arguments, cursor = parsed
                    url = html.escape(arguments[0].strip(), quote=True)
                    label = convert_inline(arguments[1].strip())
                    output.append(f'<a href="{url}">{label}</a>')
                    continue
            if name == "url":
                parsed = command_arguments(source, cursor, name, 1)
                if parsed:
                    arguments, cursor = parsed
                    url = arguments[0].strip()
                    escaped_url = html.escape(url, quote=True)
                    output.append(f'<a href="{escaped_url}">{html.escape(url)}</a>')
                    continue
            if name in single_argument:
                parsed = command_arguments(source, cursor, name, 1)
                if parsed:
                    arguments, cursor = parsed
                    opening, closing = single_argument[name]
                    output.append(
                        f"{opening}{convert_inline(arguments[0].strip())}{closing}"
                    )
                    continue
            if name in symbol_commands:
                output.append(symbol_commands[name])
                cursor += len(match.group(0))
                continue
            if name in {"small", "normalsize", "normalfont", "noindent"}:
                cursor += len(match.group(0))
                continue
            # Unknown formatting commands are dropped, but their braced text is
            # processed normally on the next iterations.
            cursor += len(match.group(0))
            continue
        if character in "{}$":
            cursor += 1
            continue
        if character == "~":
            output.append(" ")
        else:
            output.append(html.escape(character))
        cursor += 1

    return re.sub(r"[ \t]+", " ", "".join(output)).strip()


def replace_structural_commands(source: str) -> tuple[str, dict[str, str]]:
    output: list[str] = []
    tokens: dict[str, str] = {}
    cursor = 0
    pattern = re.compile(r"\\(section|datedsubsection)\b")
    while match := pattern.search(source, cursor):
        output.append(source[cursor : match.start()])
        name = match.group(1)
        argument_count = 1 if name == "section" else 2
        parsed = command_arguments(source, match.start(), name, argument_count)
        if not parsed:
            raise CvSyncError(f"Could not parse \\{name} in {MAIN_TEX}.")
        arguments, cursor = parsed
        if name == "section":
            rendered = f"## {convert_inline(arguments[0])}"
        else:
            # \datedsubsection titles are commonly wrapped across source lines.
            # Raw newlines inside the generated inline HTML make Goldmark nest
            # the date span inside the title span, defeating flex alignment.
            title = re.sub(r"\s+", " ", convert_inline(arguments[0])).strip()
            date = re.sub(r"\s+", " ", convert_inline(arguments[1])).strip()
            rendered = (
                '<div class="cv-entry-heading">'
                f'<span class="cv-entry-title">{title}</span>'
                f'<span class="cv-entry-date">{date}</span>'
                "</div>"
            )
        token = f"@@CVSTRUCT{len(tokens):04d}@@"
        tokens[token] = rendered
        output.append(f"\n\n{token}\n\n")
    output.append(source[cursor:])
    return "".join(output), tokens


def join_wrapped_lines(source: str) -> str:
    paragraphs: list[str] = []
    current: list[str] = []

    def flush() -> None:
        if current:
            paragraphs.append(" ".join(part.strip() for part in current))
            current.clear()

    for raw_line in source.splitlines():
        line = raw_line.strip()
        if not line:
            flush()
            continue
        if (
            line.startswith("## ")
            or line.startswith('<div class="cv-entry-heading">')
            or line.startswith("- ")
        ):
            flush()
            current.append(line)
            if not line.startswith("- "):
                flush()
            continue
        current.append(line)
    flush()
    return "\n\n".join(paragraphs)


def latex_body_to_html_markdown(source: str) -> str:
    source = strip_latex_comments(source)
    first_section = source.find(r"\section{Summary}")
    document_end = source.find(r"\end{document}")
    if first_section < 0 or document_end < 0:
        raise CvSyncError(
            f"{MAIN_TEX} does not contain the expected Summary section."
        )
    source = source[first_section:document_end]
    source, structural_tokens = replace_structural_commands(source)
    source = re.sub(r"\\begin\{itemize\}(?:\[[^\]]*\])?", "\n", source)
    source = re.sub(r"\\end\{itemize\}", "\n", source)
    source = re.sub(r"\\item[ \t]*", "\n- ", source)
    source = re.sub(r"\\(?:newpage|par|sepspace)\b", "\n\n", source)
    source = convert_inline(source)

    for token, rendered in structural_tokens.items():
        source = source.replace(token, rendered)
    source = join_wrapped_lines(source)
    return re.sub(r"\n{3,}", "\n\n", source).strip()


def split_cv_sections(body: str) -> list[dict[str, str]]:
    matches = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", body))
    if not matches:
        raise CvSyncError("The converted CV does not contain any sections.")
    sections: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        content_start = match.end()
        content_end = (
            matches[index + 1].start() if index + 1 < len(matches) else len(body)
        )
        sections.append(
            {
                "title": match.group(1).strip(),
                "content": body[content_start:content_end].strip(),
            }
        )
    return sections


def build_cv_data(*, body: str, revision: str) -> dict[str, object]:
    return {
        "source": {
            "provider": "Overleaf",
            "file": MAIN_TEX,
            "revision": revision,
        },
        "contacts": [
            {
                "label": "haifei_wang@u.nus.edu",
                "url": "mailto:haifei_wang@u.nus.edu",
            },
            {"label": "GitHub", "url": "https://github.com/hfwang132"},
            {
                "label": "ORCID",
                "url": "https://orcid.org/0009-0004-6041-3816",
            },
        ],
        "sections": split_cv_sections(body),
    }


def render_page_stub(*, title: str) -> str:
    return f"""---
title: "{title}"
date: 2026-07-27T00:00:00+08:00
draft: false
comment: false
---

{{{{< cv >}}}}
"""


def compile_pdf(*, required: bool) -> bool:
    latexmk = shutil.which("latexmk")
    if not latexmk:
        if required:
            raise CvSyncError(
                "latexmk is not installed. Install TeX Live or MiKTeX with "
                "XeLaTeX support, then run the command again."
            )
        print("PDF skipped: latexmk was not found; the web CV is still updated.")
        return False

    run(
        [
            latexmk,
            "-xelatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            "-outdir=build",
            MAIN_TEX,
        ],
        cwd=OVERLEAF_DIR,
    )
    source_pdf = OVERLEAF_DIR / "build" / f"{Path(MAIN_TEX).stem}.pdf"
    if not source_pdf.is_file():
        raise CvSyncError(f"Compilation did not create {source_pdf}.")
    PDF_DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_pdf, PDF_DESTINATION)
    print(f"PDF updated: {PDF_DESTINATION.relative_to(REPO_ROOT)}")
    return True


def synchronize(*, pull: bool, require_pdf: bool) -> None:
    ensure_checkout(pull=pull)
    tex_path = OVERLEAF_DIR / MAIN_TEX
    if not tex_path.is_file():
        raise CvSyncError(f"Could not find {tex_path}.")
    revision = source_revision()
    body = latex_body_to_html_markdown(tex_path.read_text(encoding="utf-8"))
    CV_DATA.parent.mkdir(parents=True, exist_ok=True)
    CV_DATA.write_text(
        json.dumps(
            build_cv_data(body=body, revision=revision),
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
        newline="\n",
    )
    ENGLISH_PAGE.write_text(
        render_page_stub(
            title="Haifei WANG (王海飞) — CV",
        ),
        encoding="utf-8",
        newline="\n",
    )
    CHINESE_PAGE.write_text(
        render_page_stub(title="王海飞 — 简历"),
        encoding="utf-8",
        newline="\n",
    )
    print(f"Web CV updated from Overleaf revision {revision}.")
    compile_pdf(required=require_pdf)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Pull the Overleaf CV and update the Hugo CV pages."
    )
    parser.add_argument(
        "--no-pull",
        action="store_true",
        help="render the current local checkout without contacting Overleaf",
    )
    parser.add_argument(
        "--require-pdf",
        action="store_true",
        help="fail unless latexmk can compile and copy the PDF",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        synchronize(pull=not args.no_pull, require_pdf=args.require_pdf)
    except (CvSyncError, subprocess.CalledProcessError) as exc:
        print(f"CV sync failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
