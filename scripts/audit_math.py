"""Audit every rendered Hugo math expression with the site's KaTeX build."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
KATEX_LIBRARY = REPO_ROOT / "themes" / "LoveIt" / "assets" / "lib" / "katex" / "katex.min.js"
IGNORED_TAGS = {"script", "noscript", "style", "textarea", "pre", "code", "option"}
DELIMITERS = (
    ("$$", "$$", True),
    (r"\[", r"\]", True),
    (r"\begin{equation}", r"\end{equation}", True),
    (r"\begin{equation*}", r"\end{equation*}", True),
    (r"\begin{align}", r"\end{align}", True),
    (r"\begin{align*}", r"\end{align*}", True),
    (r"\begin{alignat}", r"\end{alignat}", True),
    (r"\begin{alignat*}", r"\end{alignat*}", True),
    (r"\begin{gather}", r"\end{gather}", True),
    (r"\begin{CD}", r"\end{CD}", True),
    ("$", "$", False),
    (r"\(", r"\)", False),
)
NATIVE_MATH = re.compile(
    r"(?P<inline>\\\((?P<inline_body>.*?)\\\))"
    r"|(?P<display>\\\[(?P<display_body>.*?)\\\])",
    re.DOTALL,
)
TEX_COMMAND_OUTSIDE_MATH = re.compile(
    r"\\(?:"
    r"begin|end|frac|dfrac|tfrac|sqrt|mathbb|mathcal|mathrm|mathsf|"
    r"operatorname|left|right|sum|prod|int|partial|nabla|otimes|wedge|"
    r"langle|rangle|alpha|beta|gamma|psi|phi|varphi|rho|sigma|epsilon|"
    r"delta|Gamma"
    r")(?![A-Za-z])"
)


@dataclass(frozen=True)
class TextNode:
    text: str
    line: int


@dataclass(frozen=True)
class Formula:
    source: str
    line: int
    display: bool
    left: str


@dataclass(frozen=True)
class AuditIssue:
    path: Path
    line: int
    kind: str
    detail: str


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ignored_tags: list[str] = []
        self.nodes: list[TextNode] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        del attrs
        normalized = tag.lower()
        if normalized in IGNORED_TAGS:
            self.ignored_tags.append(normalized)

    def handle_startendtag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        del tag, attrs

    def handle_endtag(self, tag: str) -> None:
        normalized = tag.lower()
        if self.ignored_tags and normalized == self.ignored_tags[-1]:
            self.ignored_tags.pop()

    def handle_data(self, data: str) -> None:
        if not self.ignored_tags and ("$" in data or "\\" in data):
            self.nodes.append(TextNode(data, self.getpos()[0]))


def find_math_end(text: str, start: int, right: str) -> int:
    """Match KaTeX auto-render's delimiter search with TeX brace awareness."""

    index = start
    brace_level = 0
    while index < len(text):
        character = text[index]
        if brace_level <= 0 and text.startswith(right, index):
            return index
        if character == "\\":
            index += 2
            continue
        if character == "{":
            brace_level += 1
        elif character == "}":
            brace_level -= 1
        index += 1
    return -1


def extract_formulas(node: TextNode) -> tuple[list[Formula], list[str]]:
    formulas: list[Formula] = []
    unmatched: list[str] = []
    cursor = 0
    while cursor < len(node.text):
        candidates = []
        for order, (left, right, display) in enumerate(DELIMITERS):
            position = node.text.find(left, cursor)
            if position >= 0:
                candidates.append((position, order, left, right, display))
        if not candidates:
            break
        position, _order, left, right, display = min(candidates)
        body_start = position + len(left)
        body_end = find_math_end(node.text, body_start, right)
        if body_end < 0:
            unmatched.append(left)
            cursor = body_start
            continue
        body = node.text[body_start:body_end]
        if left.startswith(r"\begin{"):
            body = f"{left}{body}{right}"
        formulas.append(Formula(body, node.line, display, left))
        cursor = body_end + len(right)
    return formulas, unmatched


def text_outside_math(text: str) -> str:
    """Return visible text after removing every complete math region."""

    result: list[str] = []
    cursor = 0
    while cursor < len(text):
        candidates = []
        for order, (left, right, _display) in enumerate(DELIMITERS):
            position = text.find(left, cursor)
            if position >= 0:
                candidates.append((position, order, left, right))
        if not candidates:
            result.append(text[cursor:])
            break
        position, _order, left, right = min(candidates)
        result.append(text[cursor:position])
        body_start = position + len(left)
        body_end = find_math_end(text, body_start, right)
        if body_end < 0:
            result.append(text[position:body_start])
            cursor = body_start
        else:
            cursor = body_end + len(right)
    return "".join(result)


def locate_node() -> Path | None:
    configured = os.environ.get("NODE_EXE")
    candidates = [
        Path(configured) if configured else None,
        Path(shutil.which("node")) if shutil.which("node") else None,
        Path.home()
        / ".cache"
        / "codex-runtimes"
        / "codex-primary-runtime"
        / "dependencies"
        / "node"
        / "bin"
        / "node.exe",
    ]
    return next((candidate for candidate in candidates if candidate and candidate.is_file()), None)


def check_with_katex(
    formulas: list[tuple[Path, Formula]], node_executable: Path
) -> list[AuditIssue]:
    javascript = r"""
const fs = require('fs');
const katex = require(process.argv[1]);
const formulas = JSON.parse(fs.readFileSync(0, 'utf8'));
const errors = [];
for (let index = 0; index < formulas.length; index += 1) {
  try {
    katex.renderToString(formulas[index].source, {
      displayMode: formulas[index].display,
      strict: false,
      throwOnError: true
    });
  } catch (error) {
    errors.push({ index, message: String(error.message || error) });
  }
}
process.stdout.write(JSON.stringify({ version: katex.version, errors }));
"""
    payload = [
        {"source": formula.source, "display": formula.display}
        for _path, formula in formulas
    ]
    completed = subprocess.run(
        [str(node_executable), "-e", javascript, str(KATEX_LIBRARY.resolve())],
        cwd=REPO_ROOT,
        input=json.dumps(payload, ensure_ascii=False),
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=True,
    )
    result = json.loads(completed.stdout)
    issues = []
    for path, formula in formulas:
        if re.search(r"(?<!\\)\\\\[{}]", formula.source):
            preview = " ".join(formula.source.split())[:160]
            issues.append(
                AuditIssue(
                    path,
                    formula.line,
                    "overescaped-brace",
                    f"line-break command before a grouping brace | {preview}",
                )
            )
    for error in result["errors"]:
        path, formula = formulas[error["index"]]
        preview = " ".join(formula.source.split())[:160]
        issues.append(
            AuditIssue(
                path,
                formula.line,
                "katex",
                f"{error['message']} | {preview}",
            )
        )
    print(f"KaTeX {result['version']}: checked {len(formulas)} expressions")
    return issues


def audit_site(site_dir: Path, *, require_katex: bool = True) -> list[AuditIssue]:
    issues: list[AuditIssue] = []
    formulas: list[tuple[Path, Formula]] = []
    for path in sorted(site_dir.rglob("*.html")):
        parser = VisibleTextParser()
        parser.feed(path.read_text(encoding="utf-8"))
        relative = path.relative_to(site_dir)
        for node in parser.nodes:
            extracted, unmatched = extract_formulas(node)
            formulas.extend((relative, formula) for formula in extracted)
            for delimiter in unmatched:
                # A bare dollar sign in prose is common and auto-render leaves it
                # untouched. Other unmatched delimiters indicate broken markup.
                if delimiter != "$":
                    preview = " ".join(node.text.split())[:160]
                    issues.append(
                        AuditIssue(
                            relative,
                            node.line,
                            "delimiter",
                            f"unmatched opening delimiter {delimiter!r} | {preview}",
                        )
                    )
            outside = text_outside_math(node.text)
            command = TEX_COMMAND_OUTSIDE_MATH.search(outside)
            if command:
                preview = " ".join(outside.split())[:160]
                issues.append(
                    AuditIssue(
                        relative,
                        node.line,
                        "unrendered-tex",
                        f"TeX command {command.group(0)!r} is outside math | {preview}",
                    )
                )
    node_executable = locate_node()
    if node_executable is None:
        if require_katex:
            raise RuntimeError("Node.js was not found; set NODE_EXE to run KaTeX checks.")
        print(f"Node.js unavailable: extracted {len(formulas)} expressions only")
    else:
        issues.extend(check_with_katex(formulas, node_executable))
    return issues


def audit_source_posts() -> list[AuditIssue]:
    """Catch characters that can corrupt native passthrough math in HTML."""

    issues: list[AuditIssue] = []
    posts = REPO_ROOT / "content" / "posts"
    for path in sorted(posts.glob("*/index*.md")):
        content = path.read_text(encoding="utf-8")
        in_fence = False
        prose_lines: list[str] = []
        for line in content.splitlines(keepends=True):
            marker = re.match(r"\s*(`{3,}|~{3,})", line)
            if marker:
                in_fence = not in_fence
                prose_lines.append("\n" if line.endswith("\n") else "")
            elif in_fence:
                prose_lines.append("\n" if line.endswith("\n") else "")
            else:
                prose_lines.append(line)
        prose = "".join(prose_lines)
        for line_number, line in enumerate(prose.splitlines(), start=1):
            without_code = re.sub(r"`+[^`]*?`+", "", line)
            single_dollars = re.findall(
                r"(?<!\\)(?<!\$)\$(?!\$)",
                without_code,
            )
            if len(single_dollars) % 2:
                preview = " ".join(without_code.split())[:160]
                issues.append(
                    AuditIssue(
                        path.relative_to(REPO_ROOT),
                        line_number,
                        "source-delimiter",
                        f"odd number of single-dollar delimiters | {preview}",
                    )
                )
        for match in NATIVE_MATH.finditer(prose):
            body = match.group("inline_body")
            if body is None:
                body = match.group("display_body")
            if "<" not in body:
                continue
            line_number = prose.count("\n", 0, match.start()) + 1
            preview = " ".join(body.split())[:160]
            issues.append(
                AuditIssue(
                    path.relative_to(REPO_ROOT),
                    line_number,
                    "source-html",
                    f"literal '<' in native math; use \\lt | {preview}",
                )
            )
    return issues


def build_site(destination: Path) -> None:
    hugo = shutil.which("hugo")
    if not hugo:
        raise RuntimeError("Hugo was not found on PATH.")
    subprocess.run(
        [hugo, "--destination", str(destination), "--cleanDestinationDir"],
        cwd=REPO_ROOT,
        check=True,
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the Hugo site and parse every rendered formula with KaTeX."
    )
    parser.add_argument(
        "--site-dir",
        type=Path,
        help="audit an existing Hugo output directory instead of building",
    )
    parser.add_argument(
        "--no-katex",
        action="store_true",
        help="only check rendered delimiter structure",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if args.site_dir:
            issues = audit_site(args.site_dir.resolve(), require_katex=not args.no_katex)
        else:
            with tempfile.TemporaryDirectory(prefix="hfwang-math-audit-") as temporary:
                destination = Path(temporary)
                build_site(destination)
                issues = audit_site(destination, require_katex=not args.no_katex)
        issues.extend(audit_source_posts())
    except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"Math audit failed: {exc}", file=sys.stderr)
        return 2

    if issues:
        for issue in issues:
            print(f"{issue.path}:{issue.line}: {issue.kind}: {issue.detail}")
        print(f"Math audit found {len(issues)} issue(s).", file=sys.stderr)
        return 1
    print("Math audit passed with no rendering errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
