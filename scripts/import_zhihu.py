#!/usr/bin/env python3
"""Import a Zhihu article or answer into this Hugo site.

The third-party downloader remains an unmodified Git submodule. This script
orchestrates it, turns its output into a Hugo page bundle, preserves LaTeX, and
optionally validates and publishes the result.
"""

from __future__ import annotations

import argparse
import getpass
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from http.cookiejar import CookieJar
from pathlib import Path
from types import ModuleType
from urllib.parse import urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
DOWNLOADER_PATH = REPO_ROOT / "zhihu-download" / "main.py"
POSTS_DIR = REPO_ROOT / "content" / "posts"
DEFAULT_COOKIE_FILE = REPO_ROOT / ".secrets" / "zhihu-cookie.txt"
POST_AUTHOR = "Haifei"
YAML_HEADER = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)
FRONT_MATTER = re.compile(
    r"\A---(?P<newline>\r?\n)(?P<header>.*?)(?P=newline)---(?P=newline)",
    re.DOTALL,
)
ORIGINAL_URL_FIELD = re.compile(
    r'(?m)^originalURL:\s*["\']?(?P<url>https://[^\s"\']+)["\']?\s*$'
)
SITE_TIMEZONE = timezone(timedelta(hours=8))
MARKDOWN_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
SHORTCODE_IMAGE = re.compile(
    r'{{<\s*(?:figure|image)\s+[^>]*\bsrc="([^"]+)"[^>]*>}}'
)
MARKDOWN_IMAGE_LINE = re.compile(
    r'^\s*!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)'
    r'(?:\s+"(?P<title>[^"]*)")?\)\s*$'
)


class ImportFailure(RuntimeError):
    """A user-facing import error."""


@dataclass(frozen=True)
class ImportedPost:
    bundle_dir: Path
    content_file: Path
    title: str
    published_at: datetime
    image_count: int


@dataclass(frozen=True)
class PageMetadata:
    published_at: datetime | None
    modified_at: datetime | None


class ZhihuMetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.values: dict[str, str] = {}

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag.lower() != "meta":
            return
        attributes = dict(attrs)
        itemprop = attributes.get("itemprop", "")
        content = attributes.get("content")
        if itemprop and content:
            self.values[itemprop] = content


def load_downloader(path: Path = DOWNLOADER_PATH) -> ModuleType:
    if not path.is_file():
        raise ImportFailure(
            "找不到 zhihu-download/main.py。请先运行 "
            "`git submodule update --init --recursive`。"
        )
    spec = importlib.util.spec_from_file_location("zhihu_downloader", path)
    if spec is None or spec.loader is None:
        raise ImportFailure(f"无法加载知乎下载器：{path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def cookie_jar_to_header(cookie_jar: CookieJar) -> str:
    cookies = [
        f"{cookie.name}={cookie.value}"
        for cookie in cookie_jar
        if cookie.domain.endswith("zhihu.com")
    ]
    if not cookies:
        raise ImportFailure("浏览器中没有找到 zhihu.com 的 Cookie。")
    return "; ".join(cookies)


def load_browser_cookie(browser_name: str) -> str:
    try:
        import browser_cookie3
    except ImportError as exc:
        raise ImportFailure(
            "浏览器 Cookie 功能需要 browser-cookie3；请先安装 requirements.txt。"
        ) from exc

    browser_loaders = {
        "chrome": browser_cookie3.chrome,
        "edge": browser_cookie3.edge,
        "firefox": browser_cookie3.firefox,
    }
    names = list(browser_loaders) if browser_name == "auto" else [browser_name]
    errors: list[str] = []
    for name in names:
        try:
            jar = browser_loaders[name](domain_name="zhihu.com")
            return cookie_jar_to_header(jar)
        except Exception as exc:  # Browser encryption/locking differs by platform.
            errors.append(f"{name}: {exc}")
    details = "; ".join(errors)
    raise ImportFailure(
        "无法从浏览器读取知乎 Cookie。浏览器加密或权限可能阻止了读取。"
        f"请改用 --cookie-file 或隐藏输入。详情：{details}"
    )


def resolve_cookie(args: argparse.Namespace) -> str:
    if args.cookie:
        return args.cookie.strip()

    env_cookie = os.environ.get("ZHIHU_COOKIE", "").strip()
    if env_cookie:
        return env_cookie

    if args.cookie_from_browser:
        return load_browser_cookie(args.cookie_from_browser)

    cookie_file = Path(args.cookie_file).expanduser() if args.cookie_file else None
    if cookie_file:
        try:
            cookie = cookie_file.read_text(encoding="utf-8").strip()
        except OSError as exc:
            raise ImportFailure(f"无法读取 Cookie 文件：{cookie_file}") from exc
        if not cookie:
            raise ImportFailure(f"Cookie 文件为空：{cookie_file}")
        return cookie

    if DEFAULT_COOKIE_FILE.is_file():
        cookie = DEFAULT_COOKIE_FILE.read_text(encoding="utf-8").strip()
        if cookie:
            return cookie

    if not sys.stdin.isatty():
        raise ImportFailure(
            "未提供 Cookie。请设置 ZHIHU_COOKIE、使用 --cookie-file，"
            "或在终端中运行以进行隐藏输入。"
        )
    cookie = getpass.getpass("请输入知乎 Cookie（输入不会显示）: ").strip()
    if not cookie:
        raise ImportFailure("Cookie 不能为空。")
    return cookie


def validate_zhihu_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in {
        "www.zhihu.com",
        "zhuanlan.zhihu.com",
    }:
        raise ImportFailure("仅支持 https://www.zhihu.com 或 zhuanlan.zhihu.com 链接。")
    if "/column/" in parsed.path:
        raise ImportFailure("自动入库目前支持单篇文章或回答，不支持整列专栏链接。")


def title_to_slug(title: str) -> str:
    """Turn an article title into a readable, cross-platform path component."""

    normalized = unicodedata.normalize("NFKC", title).strip()
    result: list[str] = []
    separator_pending = False
    for character in normalized:
        category = unicodedata.category(character)
        if category[0] in {"L", "N", "M"}:
            if separator_pending and result:
                result.append("-")
            result.append(character)
            separator_pending = False
        else:
            separator_pending = True
    slug = "".join(result).strip("-")
    if not slug:
        raise ImportFailure("文章标题无法生成目录名，请使用 --slug 指定文章名。")
    return slug


def build_post_slug(
    published_at: datetime, title: str, requested_slug: str | None = None
) -> str:
    prefix = f"Post_{published_at.astimezone(SITE_TIMEZONE):%Y%m%d}_"
    if requested_slug and requested_slug.startswith("Post_"):
        if not requested_slug.startswith(prefix):
            raise ImportFailure(
                f"目录名必须以知乎发布日期对应的 {prefix} 开头。"
            )
        suffix = title_to_slug(requested_slug[len(prefix) :])
        return prefix + suffix
    suffix = title_to_slug(requested_slug or title)
    return prefix + suffix


def parse_zhihu_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(normalized).astimezone(SITE_TIMEZONE)
    except ValueError as exc:
        raise ImportFailure(f"无法解析知乎时间：{value}") from exc


def extract_page_metadata(html: str) -> PageMetadata:
    parser = ZhihuMetadataParser()
    parser.feed(html)
    return PageMetadata(
        published_at=parse_zhihu_datetime(
            parser.values.get("datePublished") or parser.values.get("dateCreated")
        ),
        modified_at=parse_zhihu_datetime(parser.values.get("dateModified")),
    )


def parse_published_date_override(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise ImportFailure("--published-date 必须使用 YYYY-MM-DD 格式。") from exc
    return parsed.replace(tzinfo=SITE_TIMEZONE)


KATEX_MATH_DELIMITERS = re.compile(
    r"(?:"
    r"(?P<display_open>(?<!\\)\$\$)(?P<display_body>.*?)(?P<display_close>(?<!\\)\$\$)"
    r"|"
    r"(?P<inline_open>(?<!\\)(?<!\$)\$(?!\$))"
    r"(?P<inline_body>(?:\\.|[^$\n])+?)"
    r"(?P<inline_close>(?<!\\)(?<!\$)\$(?!\$))"
    r")",
    re.DOTALL,
)
KATEX_TOP_LEVEL_ENVIRONMENT = re.compile(
    r"\\begin\{(?:align\*?|alignat\*?|equation\*?)\}"
)


def _normalize_katex_formula(match: re.Match[str]) -> str:
    body = match.group("inline_body")
    inline = body is not None
    if body is None:
        body = match.group("display_body")

    # Markdown downloaders escape emphasis characters even inside formulas.
    # Goldmark passthrough preserves those backslashes, so remove only the
    # Markdown escapes that would otherwise change or invalidate TeX.
    normalized = re.sub(r"\\([_*])", r"\1", body)
    normalized = re.sub(r"\\\\([{}])", r"\\\1", normalized)
    if not KATEX_TOP_LEVEL_ENVIRONMENT.search(normalized):
        if inline:
            return f"${normalized}$"
        return f"$${normalized}$$"

    normalized = re.sub(
        r"\\begin\{align\*?\}",
        r"\\begin{aligned}",
        normalized,
    )
    normalized = re.sub(
        r"\\end\{align\*?\}",
        r"\\end{aligned}",
        normalized,
    )
    normalized = re.sub(
        r"\\begin\{alignat\*?\}",
        r"\\begin{alignedat}",
        normalized,
    )
    normalized = re.sub(
        r"\\end\{alignat\*?\}",
        r"\\end{alignedat}",
        normalized,
    )
    normalized = re.sub(
        r"\\(?:begin|end)\{equation\*?\}",
        "",
        normalized,
    )
    # A few downloader conversions insert empty inline delimiters between two
    # display environments. Delimiters cannot be nested inside display math.
    normalized = re.sub(
        r"(?<!\\)(?<!\$)\$(?!\$)(.*?)(?<!\\)(?<!\$)\$(?!\$)",
        r"\1",
        normalized,
        flags=re.DOTALL,
    )
    # Multi-line environments are display math even when the downloader
    # originally wrapped them in single-dollar inline delimiters.
    return f"$${normalized}$$"


def normalize_katex_environments(markdown: str) -> str:
    r"""Make top-level TeX environments valid inside KaTeX delimiters.

    KaTeX rejects top-level ``align`` inside inline dollar math
    because ``align`` and ``equation`` are top-level display environments.
    Convert them to their embeddable equivalents while preserving code.
    """

    result: list[str] = []
    prose: list[str] = []
    in_fence = False
    fence_char = ""

    def flush_prose() -> None:
        if not prose:
            return
        block = "".join(prose)
        segments = re.split(r"(`+[^`]*?`+)", block)
        for index, segment in enumerate(segments):
            if not index % 2:
                segments[index] = KATEX_MATH_DELIMITERS.sub(
                    _normalize_katex_formula,
                    segment,
                )
        result.append("".join(segments))
        prose.clear()

    for line in markdown.splitlines(keepends=True):
        stripped = line.lstrip()
        fence_match = re.match(r"(`{3,}|~{3,})", stripped)
        if fence_match:
            flush_prose()
            marker = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
            elif marker[0] == fence_char:
                in_fence = False
                fence_char = ""
            result.append(line)
            continue
        if in_fence:
            result.append(line)
            continue
        prose.append(line)
    flush_prose()
    return "".join(result)


def normalize_html_sensitive_math(markdown: str) -> str:
    r"""Keep dollar-delimited math from being interpreted as HTML tags.

    Hugo preserves dollar-delimited math verbatim. A literal ``<`` in that
    output can therefore start an HTML tag before KaTeX sees the formula.
    Use the equivalent TeX relation commands while protecting code examples.
    """

    result: list[str] = []
    prose: list[str] = []
    in_fence = False
    fence_char = ""

    def replace_formula(match: re.Match[str]) -> str:
        body = match.group("inline_body")
        inline = body is not None
        if body is None:
            body = match.group("display_body")
        normalized = re.sub(r"<\s*", r"\\lt ", body)
        normalized = re.sub(r">\s*", r"\\gt ", normalized)
        normalized = re.sub(r"\\(lt|gt)\s+", r"\\\1 ", normalized)
        if inline:
            return f"${normalized}$"
        return f"$${normalized}$$"

    def flush_prose() -> None:
        if not prose:
            return
        block = "".join(prose)
        segments = re.split(r"(`+[^`]*?`+)", block)
        for index, segment in enumerate(segments):
            if not index % 2:
                segments[index] = KATEX_MATH_DELIMITERS.sub(
                    replace_formula,
                    segment,
                )
        result.append("".join(segments))
        prose.clear()

    for line in markdown.splitlines(keepends=True):
        stripped = line.lstrip()
        fence_match = re.match(r"(`{3,}|~{3,})", stripped)
        if fence_match:
            flush_prose()
            marker = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
            elif marker[0] == fence_char:
                in_fence = False
                fence_char = ""
            result.append(line)
            continue
        if in_fence:
            result.append(line)
            continue
        prose.append(line)
    flush_prose()
    return "".join(result)


def convert_math_delimiters(markdown: str) -> str:
    """Normalize downloaded formulas to dollar-only Markdown delimiters.

    Fenced and inline code are protected. A formula occupying a whole line is
    display math; prose formulas remain inline. Legacy native delimiters are
    accepted as input but never emitted.
    """

    result: list[str] = []
    prose: list[str] = []
    in_fence = False
    fence_char = ""
    legacy_display_pattern = re.compile(r"\\\[(.+?)\\\]", re.DOTALL)
    legacy_inline_pattern = re.compile(r"\\\(([^\n]+?)\\\)")
    standalone_pattern = re.compile(
        r"^(\s*)(?<!\\)\$(?!\$)(.+?)(?<!\\)\$(?!\$)(\s*)$"
    )
    def flush_prose() -> None:
        if not prose:
            return
        block = "".join(prose)
        segments = re.split(r"(`+[^`]*?`+)", block)
        for index, segment in enumerate(segments):
            if index % 2:
                continue
            segment = legacy_display_pattern.sub(
                lambda match: f"$${match.group(1)}$$", segment
            )
            segment = legacy_inline_pattern.sub(
                lambda match: f"${match.group(1)}$", segment
            )
            segment = "".join(
                standalone_pattern.sub(
                    lambda match: (
                        f"{match.group(1)}$${match.group(2)}$${match.group(3)}"
                    ),
                    line,
                )
                for line in segment.splitlines(keepends=True)
            )
            segments[index] = segment
        result.append("".join(segments))
        prose.clear()

    for line in markdown.splitlines(keepends=True):
        stripped = line.lstrip()
        fence_match = re.match(r"(`{3,}|~{3,})", stripped)
        if fence_match:
            flush_prose()
            marker = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
            elif marker[0] == fence_char:
                in_fence = False
                fence_char = ""
            result.append(line)
            continue
        if in_fence:
            result.append(line)
            continue

        prose.append(line)
    flush_prose()
    normalized = normalize_katex_environments("".join(result))
    return normalize_html_sensitive_math(normalized)


def escape_shortcode_parameter(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def convert_images_to_shortcodes(markdown: str) -> str:
    """Convert standalone Markdown images to the site's compact figure shortcode."""

    converted: list[str] = []
    in_fence = False
    fence_char = ""
    for line in markdown.splitlines(keepends=True):
        stripped = line.lstrip()
        fence = re.match(r"(`{3,}|~{3,})", stripped)
        if fence:
            marker = fence.group(1)[0]
            if not in_fence:
                in_fence = True
                fence_char = marker
            elif marker == fence_char:
                in_fence = False
                fence_char = ""
            converted.append(line)
            continue
        match = None if in_fence else MARKDOWN_IMAGE_LINE.match(line.rstrip("\r\n"))
        if not match:
            converted.append(line)
            continue
        src = escape_shortcode_parameter(match.group("src"))
        attributes = [f'src="{src}"']
        alt = match.group("alt")
        title = match.group("title")
        if alt:
            attributes.append(f'alt="{escape_shortcode_parameter(alt)}"')
        if title:
            attributes.append(f'title="{escape_shortcode_parameter(title)}"')
        newline = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
        converted.append("{{< figure " + " ".join(attributes) + " >}}" + newline)
    return "".join(converted)


def extract_downloaded_content(markdown: str, fallback_title: str) -> tuple[str, str, str]:
    markdown = YAML_HEADER.sub("", markdown)
    lines = markdown.splitlines()
    title = fallback_title
    author = ""
    body_start = 0

    for index, line in enumerate(lines):
        if line.startswith("# "):
            title = line[2:].strip()
            body_start = index + 1
            break

    body_lines: list[str] = []
    for line in lines[body_start:]:
        stripped = line.strip()
        author_match = re.match(r"\*\*Author:\*\*\s*\[?([^\]]*)", stripped)
        if author_match:
            author = author_match.group(1).strip()
            continue
        if re.match(r"\*\*Link:\*\*", stripped):
            continue
        body_lines.append(line)

    body = "\n".join(body_lines).strip() + "\n"
    return title, author, body


def yaml_list(items: list[str]) -> str:
    return "[" + ", ".join(json.dumps(item, ensure_ascii=False) for item in items) + "]"


def build_front_matter(
    *,
    title: str,
    author: str,
    source_url: str,
    date_value: datetime,
    tags: list[str],
    categories: list[str],
) -> str:
    fields = [
        "---",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"date: {date_value.isoformat()}",
        "draft: false",
        "math: true",
        f"originalURL: {json.dumps(source_url, ensure_ascii=False)}",
    ]
    if author:
        fields.append(f"author: {json.dumps(author, ensure_ascii=False)}")
    if tags:
        fields.append(f"tags: {yaml_list(tags)}")
    if categories:
        fields.append(f"categories: {yaml_list(categories)}")
    fields.extend(["---", ""])
    return "\n".join(fields)


def source_identity(url: str) -> tuple[str, ...]:
    """Return a stable identity for a Zhihu article or answer URL."""

    parsed = urlparse(url)
    article = re.fullmatch(r"/p/(\d+)/?", parsed.path)
    if parsed.hostname == "zhuanlan.zhihu.com" and article:
        return ("article", article.group(1))
    answer = re.fullmatch(r"/question/(\d+)/answer/(\d+)/?", parsed.path)
    if parsed.hostname == "www.zhihu.com" and answer:
        return ("answer", answer.group(1), answer.group(2))
    return ("url", parsed.hostname or "", parsed.path.rstrip("/"))


def find_existing_bundle(source_url: str) -> Path | None:
    """Find an existing bundle by source ID, even when its title changed."""

    identity = source_identity(source_url)
    matches: list[Path] = []
    for content_file in POSTS_DIR.glob("*/index.zh-cn.md"):
        try:
            content = content_file.read_text(encoding="utf-8")
        except OSError as exc:
            raise ImportFailure(f"无法读取已有文章：{content_file}") from exc
        match = ORIGINAL_URL_FIELD.search(content)
        if match and source_identity(match.group("url")) == identity:
            matches.append(content_file.parent)
    if len(matches) > 1:
        paths = ", ".join(str(path) for path in matches)
        raise ImportFailure(f"同一知乎来源对应多个本地目录：{paths}")
    return matches[0] if matches else None


def _replace_or_append_scalar(
    lines: list[str], name: str, rendered_value: str
) -> None:
    prefix = f"{name}:"
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            lines[index] = f"{name}: {rendered_value}"
            return
    lines.append(f"{name}: {rendered_value}")


def refresh_front_matter(
    existing_content: str,
    *,
    title: str,
    author: str,
    source_url: str,
    date_value: datetime,
    tags: list[str],
    categories: list[str],
) -> str:
    """Refresh Zhihu-controlled fields while preserving local metadata."""

    match = FRONT_MATTER.match(existing_content)
    if not match:
        raise ImportFailure("已有文章缺少有效的 YAML front matter。")
    lines = match.group("header").splitlines()
    _replace_or_append_scalar(lines, "title", json.dumps(title, ensure_ascii=False))
    _replace_or_append_scalar(lines, "date", date_value.isoformat())
    _replace_or_append_scalar(lines, "draft", "false")
    _replace_or_append_scalar(lines, "math", "true")
    _replace_or_append_scalar(
        lines, "originalURL", json.dumps(source_url, ensure_ascii=False)
    )
    if author:
        _replace_or_append_scalar(
            lines, "author", json.dumps(author, ensure_ascii=False)
        )
    if tags:
        _replace_or_append_scalar(lines, "tags", yaml_list(tags))
    if categories:
        _replace_or_append_scalar(lines, "categories", yaml_list(categories))
    newline = match.group("newline")
    return "---" + newline + newline.join(lines) + newline + "---" + newline


def copy_preserved_bundle_files(source: Path, staging: Path) -> None:
    """Keep translations and local bundle files while replacing source/images."""

    if not source.is_dir():
        return
    for child in source.iterdir():
        if child.name in {"index.zh-cn.md", "images"}:
            continue
        destination = staging / child.name
        if child.is_dir():
            shutil.copytree(child, destination)
        else:
            shutil.copy2(child, destination)


def copy_assets_and_rewrite(
    body: str, source_root: Path, stem: str, target: Path
) -> tuple[str, int]:
    asset_dir = source_root / stem
    if not asset_dir.is_dir():
        return body, 0
    destination = target / "images"
    shutil.copytree(asset_dir, destination)
    rewritten = body.replace(f"{stem}/", "images/")
    image_files = [path for path in destination.rglob("*") if path.is_file()]
    for image_file in image_files:
        actual_suffix = detect_image_suffix(image_file)
        if not actual_suffix or image_file.suffix.lower() == actual_suffix:
            continue
        renamed = image_file.with_suffix(actual_suffix)
        if renamed.exists():
            raise ImportFailure(f"图片重命名发生冲突：{renamed.name}")
        old_relative = image_file.relative_to(target).as_posix()
        image_file.rename(renamed)
        new_relative = renamed.relative_to(target).as_posix()
        rewritten = rewritten.replace(old_relative, new_relative)
    return rewritten, len(image_files)


def detect_image_suffix(path: Path) -> str | None:
    with path.open("rb") as image_file:
        header = image_file.read(16)
    if header.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if header.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if header.startswith((b"GIF87a", b"GIF89a")):
        return ".gif"
    if header.startswith(b"RIFF") and header[8:12] == b"WEBP":
        return ".webp"
    return None


def prepare_zhihu_content(content_element: object) -> None:
    for link in content_element.find_all("a"):
        href = link.get("href", "")
        if urlparse(href).hostname == "zhida.zhihu.com":
            link.unwrap()
            continue
        if "data-text" not in link.attrs:
            link["data-text"] = link.get_text(" ", strip=True) or href

    for image in content_element.find_all("img"):
        preferred_source = (
            image.get("data-original")
            or image.get("data-actualsrc")
            or image.get("src")
        )
        if preferred_source:
            image["src"] = preferred_source


def transform_zhihu_html(
    downloader: ModuleType,
    html: str,
    url: str,
    work_dir: Path,
    metadata: PageMetadata,
) -> tuple[Path, str]:
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:
        raise ImportFailure("请先安装 requirements.txt 中的依赖。") from exc

    soup = BeautifulSoup(html, "html.parser")
    title_element = soup.select_one("h1.Post-Title, h1.QuestionHeader-title")
    content_element = soup.select_one(
        "div.Post-RichTextContainer, div.RichContent-inner"
    )
    author_info = soup.select_one("div.AuthorInfo")
    author_meta = (
        author_info.find("meta", {"itemprop": "name"}) if author_info else None
    )
    author = author_meta.get("content") if author_meta else "Unknown"
    if not title_element or not content_element:
        raise ImportFailure("知乎页面缺少标题或正文，页面结构可能已经变化。")

    prepare_zhihu_content(content_element)
    date_label = (
        metadata.published_at.strftime("%Y%m%d")
        if metadata.published_at
        else "Unknown"
    )
    previous_cwd = Path.cwd()
    try:
        os.chdir(work_dir)
        stem = downloader.save_and_transform(
            title_element,
            content_element,
            author,
            url,
            False,
            soup,
            date_label,
        )
    finally:
        os.chdir(previous_cwd)
    return work_dir / f"{stem}.md", stem


def run_downloader(
    url: str,
    cookie: str,
    work_dir: Path,
    *,
    html_file: Path | None = None,
) -> tuple[Path, str, PageMetadata]:
    downloader = load_downloader()
    if html_file:
        try:
            html = html_file.read_text(encoding="utf-8")
        except OSError as exc:
            raise ImportFailure(f"无法读取知乎页面文件：{html_file}") from exc
        metadata = extract_page_metadata(html)
        markdown_file, stem = transform_zhihu_html(
            downloader, html, url, work_dir, metadata
        )
    else:
        try:
            import requests
        except ImportError as exc:
            raise ImportFailure("请先安装 requirements.txt 中的依赖。") from exc
        session = requests.Session()
        session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/124.0.0.0 Safari/537.36"
                ),
                "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
                "Cookie": cookie,
            }
        )
        try:
            response = session.get(url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as exc:
            raise ImportFailure(f"无法读取知乎文章页面：{exc}") from exc
        metadata = extract_page_metadata(response.text)
        markdown_file, stem = transform_zhihu_html(
            downloader, response.text, url, work_dir, metadata
        )

    if not stem:
        raise ImportFailure("知乎下载器没有生成文章；Cookie 可能已过期，或页面结构已变化。")
    if not markdown_file.is_file():
        candidates = list(work_dir.glob("*.md"))
        if len(candidates) != 1:
            raise ImportFailure("无法确定下载器生成的 Markdown 文件。")
        markdown_file = candidates[0]
        stem = markdown_file.stem
    return markdown_file, stem, metadata


def verify_bundle_images(content_file: Path, expected_count: int) -> None:
    content = content_file.read_text(encoding="utf-8")
    local_images = [
        path
        for path in MARKDOWN_IMAGE.findall(content) + SHORTCODE_IMAGE.findall(content)
        if not urlparse(path).scheme and not path.startswith("/")
    ]
    unique_local_images = list(dict.fromkeys(local_images))
    missing = [
        path
        for path in unique_local_images
        if not (content_file.parent / path).is_file()
    ]
    if missing:
        raise ImportFailure(f"文章中有图片未成功下载：{', '.join(missing[:3])}")
    if len(unique_local_images) != expected_count:
        raise ImportFailure(
            f"图片数量不一致：正文引用 {len(local_images)} 次"
            f"（{len(unique_local_images)} 个唯一文件），"
            f"本地保存 {expected_count} 个文件。"
        )


def install_bundle(
    staging: Path,
    target: Path,
    *,
    expected_image_count: int,
) -> None:
    """Install a fully verified bundle and roll back failed replacements."""

    staged_content = staging / "index.zh-cn.md"
    verify_bundle_images(staged_content, expected_image_count)

    backup = target.with_name(target.name + ".backup")
    replacing = target.exists()
    if replacing:
        if backup.exists():
            raise ImportFailure(
                f"发现上次更新遗留的备份目录：{backup}。"
                "请先确认并处理该目录，避免覆盖可恢复内容。"
            )
        target.rename(backup)

    try:
        shutil.copytree(staging, target)
        verify_bundle_images(
            target / "index.zh-cn.md",
            expected_image_count,
        )
    except Exception:
        if target.exists():
            shutil.rmtree(target)
        if replacing and backup.exists():
            backup.rename(target)
        raise
    else:
        if backup.exists():
            shutil.rmtree(backup)


def import_post(args: argparse.Namespace) -> ImportedPost:
    validate_zhihu_url(args.url)
    html_file = Path(args.html_file).expanduser() if args.html_file else None
    cookie = "" if html_file else resolve_cookie(args)
    with tempfile.TemporaryDirectory(prefix="zhihu-import-") as temporary:
        work_dir = Path(temporary)
        markdown_file, stem, metadata = run_downloader(
            args.url, cookie, work_dir, html_file=html_file
        )
        published_at = (
            parse_published_date_override(args.published_date)
            or metadata.published_at
        )
        if not published_at:
            raise ImportFailure(
                "知乎页面缺少原始发布日期。为避免使用错误日期，"
                "请用 --published-date YYYY-MM-DD 明确指定。"
            )
        downloaded = markdown_file.read_text(encoding="utf-8")
        title, _source_author, body = extract_downloaded_content(downloaded, stem)
        slug = build_post_slug(published_at, title, args.slug)
        generated_target = POSTS_DIR / slug
        existing_bundle = find_existing_bundle(args.url)
        target = existing_bundle or generated_target
        if existing_bundle and not args.force:
            raise ImportFailure(
                f"该知乎内容已经导入：{existing_bundle}。如需更新，请加 --force。"
            )
        if (
            existing_bundle
            and generated_target.exists()
            and generated_target != existing_bundle
        ):
            raise ImportFailure(
                f"更新目标与新标题目录同时存在：{existing_bundle}、"
                f"{generated_target}。请先确认是否有重复文章。"
            )
        if target.exists() and not args.force:
            raise ImportFailure(f"目标目录已存在：{target}。如需更新，请加 --force。")
        body = convert_math_delimiters(body)

        staging = work_dir / "bundle"
        staging.mkdir()
        if target.exists():
            copy_preserved_bundle_files(target, staging)
        body, image_count = copy_assets_and_rewrite(body, work_dir, stem, staging)
        body = convert_images_to_shortcodes(body)
        existing_content_file = target / "index.zh-cn.md"
        if existing_content_file.is_file():
            existing_content = existing_content_file.read_text(
                encoding="utf-8"
            )
            front_matter = refresh_front_matter(
                existing_content,
                title=title,
                author=POST_AUTHOR,
                source_url=args.url,
                date_value=published_at,
                tags=args.tag,
                categories=args.category,
            )
        else:
            front_matter = build_front_matter(
                title=title,
                author=POST_AUTHOR,
                source_url=args.url,
                date_value=published_at,
                tags=args.tag,
                categories=args.category,
            )
        content_file = staging / "index.zh-cn.md"
        content_file.write_text(front_matter + "\n" + body, encoding="utf-8")
        install_bundle(
            staging,
            target,
            expected_image_count=image_count,
        )

    post = ImportedPost(
        target,
        target / "index.zh-cn.md",
        title,
        published_at,
        image_count,
    )
    return post


def run_checked(
    command: list[str],
    *,
    cwd: Path = REPO_ROOT,
    env: dict[str, str] | None = None,
) -> None:
    process_env = os.environ.copy()
    if env:
        process_env.update(env)
    try:
        subprocess.run(command, cwd=cwd, check=True, env=process_env)
    except FileNotFoundError as exc:
        raise ImportFailure(f"找不到命令：{command[0]}") from exc
    except subprocess.CalledProcessError as exc:
        raise ImportFailure(f"命令执行失败：{' '.join(command)}") from exc


def validate_site() -> None:
    with (
        tempfile.TemporaryDirectory(prefix="hugo-build-") as destination,
        tempfile.TemporaryDirectory(prefix="hugo-cache-") as cache_dir,
        tempfile.TemporaryDirectory(prefix="hugo-resources-") as resource_dir,
    ):
        run_checked(
            [
                "hugo",
                "--minify",
                "--cacheDir",
                cache_dir,
                "--destination",
                destination,
            ],
            env={"HUGO_RESOURCEDIR": resource_dir},
        )


def publish_post(post: ImportedPost, *, push: bool = True) -> None:
    staged = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=REPO_ROOT,
        check=False,
    )
    if staged.returncode != 0:
        raise ImportFailure(
            "Git 暂存区已有其他改动。为避免混入发布提交，请先提交或取消暂存。"
        )
    relative_bundle = post.bundle_dir.relative_to(REPO_ROOT)
    run_checked(["git", "add", "--", str(relative_bundle)])
    run_checked(["git", "commit", "-m", f"post: import {post.title}"])
    if push:
        run_checked(["git", "push"])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="把单篇知乎文章/回答导入 Hugo，并保留原生 LaTeX 公式。"
    )
    parser.add_argument("url", help="知乎文章或回答的 HTTPS 链接")
    parser.add_argument(
        "--slug",
        help="文章名覆盖值；默认使用知乎标题，最终目录为 Post_知乎发布日期_文章名",
    )
    parser.add_argument("--tag", action="append", default=[], help="文章标签，可重复")
    parser.add_argument(
        "--category", action="append", default=[], help="文章分类，可重复"
    )
    parser.add_argument("--force", action="store_true", help="覆盖同 slug 的已有文章")
    parser.add_argument(
        "--publish",
        action="store_true",
        help=(
            "commit and push the imported post after validation; "
            "the post uses draft: false even without this option"
        ),
    )
    parser.add_argument(
        "--skip-git-push",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    parser.add_argument(
        "--no-build", action="store_true", help="跳过 Hugo 构建验证（不推荐）"
    )
    parser.add_argument(
        "--published-date",
        help="知乎缺少发布日期元数据时的人工兜底，格式为 YYYY-MM-DD",
    )
    parser.add_argument(
        "--translate",
        choices=["en"],
        help="导入后使用 OpenAI API 生成对应语言版本；目前支持 en",
    )
    parser.add_argument(
        "--translation-model",
        help="OpenAI 翻译模型；默认由 translate_posts.py 选择",
    )
    parser.add_argument(
        "--openai-api-key-file",
        help=(
            "OpenAI API Key 文件；默认读取 .secrets/openai-api-key.txt，"
            "也可设置 OPENAI_API_KEY"
        ),
    )
    parser.add_argument(
        "--html-file",
        help=argparse.SUPPRESS,
    )
    cookie = parser.add_argument_group("Cookie 来源")
    cookie.add_argument(
        "--cookie",
        help="直接传 Cookie（会进入终端历史，不推荐；优先使用文件或隐藏输入）",
    )
    cookie.add_argument("--cookie-file", help="包含 Cookie 的 UTF-8 文本文件")
    cookie.add_argument(
        "--cookie-from-browser",
        choices=["auto", "chrome", "edge", "firefox"],
        help="经你明确授权，从本机浏览器读取 zhihu.com Cookie",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        post = import_post(args)
        translated_file = None
        if args.translate:
            try:
                from translate_posts import (
                    DEFAULT_MODEL,
                    TranslationFailure,
                    translate_bundle,
                )

                translated_file = translate_bundle(
                    post.bundle_dir,
                    model=args.translation_model or DEFAULT_MODEL,
                    api_key_file=args.openai_api_key_file,
                    force=args.force,
                )
            except TranslationFailure as exc:
                raise ImportFailure(
                    "中文文章已导入，但英文翻译失败；没有执行发布。"
                    f"修复后可单独重试翻译。原因：{exc}"
                ) from exc
        if not args.no_build:
            validate_site()
        if args.publish:
            publish_post(post, push=not args.skip_git_push)
        state = "Published" if args.publish else "Imported"
        print(
            f"{state}: {post.content_file}\n"
            f"Zhihu publication date: {post.published_at:%Y-%m-%d}; "
            f"local images: {post.image_count}"
            + (
                f"\nTranslated: {translated_file}"
                if translated_file is not None
                else ""
            )
        )
        return 0
    except ImportFailure as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
