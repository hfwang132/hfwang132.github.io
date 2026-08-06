import argparse
import importlib.util
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "import_zhihu.py"
SPEC = importlib.util.spec_from_file_location("import_zhihu", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class MathDelimiterTests(unittest.TestCase):
    def test_preserves_latex_backslashes(self):
        source = r"$\begin{aligned}a&=b\\c&=d\end{aligned}$"
        expected = r"\[\begin{aligned}a&=b\\c&=d\end{aligned}\]"
        self.assertEqual(MODULE.convert_math_delimiters(source), expected)

    def test_keeps_formula_inside_prose_inline(self):
        source = r"Energy is $E=mc^2$ here."
        expected = r"Energy is \(E=mc^2\) here."
        self.assertEqual(MODULE.convert_math_delimiters(source), expected)

    def test_converts_display_math(self):
        source = "$$x_1 \\\\\ny_2$$\n"
        expected = "\\[x_1 \\\\\ny_2\\]\n"
        self.assertEqual(MODULE.convert_math_delimiters(source), expected)

    def test_does_not_touch_code(self):
        source = "Use `$x$` here.\n```tex\n$x$\n```\n"
        self.assertEqual(MODULE.convert_math_delimiters(source), source)

    def test_converts_align_nested_in_inline_math_to_display_aligned(self):
        source = r"> $\begin{align}a&=b\\c&=d\end{align}$"
        expected = r"> \[\begin{aligned}a&=b\\c&=d\end{aligned}\]"
        self.assertEqual(MODULE.convert_math_delimiters(source), expected)

    def test_normalizes_align_nested_in_existing_display_math(self):
        source = (
            r"\[\left\{\begin{align}a&=b\\c&=d"
            r"\end{align}\right.\]"
        )
        expected = (
            r"\[\left\{\begin{aligned}a&=b\\c&=d"
            r"\end{aligned}\right.\]"
        )
        self.assertEqual(MODULE.normalize_katex_environments(source), expected)

    def test_removes_equation_environment_nested_in_math_delimiters(self):
        source = (
            r"Result: \(\begin{equation}x=1\end{equation}\)."
        )
        expected = r"Result: \[x=1\]."
        self.assertEqual(MODULE.normalize_katex_environments(source), expected)

    def test_does_not_normalize_katex_examples_inside_code(self):
        source = (
            "Use `\\(\\begin{align}a&=b\\end{align}\\)`.\n"
            "```tex\n"
            "\\[\\begin{align}a&=b\\end{align}\\]\n"
            "```\n"
        )
        self.assertEqual(MODULE.normalize_katex_environments(source), source)

    def test_normalizes_html_sensitive_relations_in_native_math(self):
        source = r"Range \(0<x<1\), bound \[y>0\]."
        expected = r"Range \(0\lt x\lt 1\), bound \[y\gt 0\]."
        self.assertEqual(MODULE.normalize_html_sensitive_math(source), expected)

    def test_does_not_normalize_html_sensitive_relations_inside_code(self):
        source = "Use `\\(0<x<1\\)` here.\n```tex\n\\[y>0\\]\n```\n"
        self.assertEqual(MODULE.normalize_html_sensitive_math(source), source)

    def test_removes_nested_delimiters_between_display_environments(self):
        source = (
            r"\[\begin{align}a&=b\end{align}"
            r"\( \)"
            r"\begin{align}c&=d\end{align}\]"
        )
        expected = (
            r"\[\begin{aligned}a&=b\end{aligned}"
            r" "
            r"\begin{aligned}c&=d\end{aligned}\]"
        )
        self.assertEqual(MODULE.normalize_katex_environments(source), expected)

    def test_repository_posts_have_no_nested_katex_block_environments(self):
        posts = Path(__file__).resolve().parents[1] / "content" / "posts"
        invalid = []
        for path in sorted(posts.glob("*/index*.md")):
            content = path.read_text(encoding="utf-8")
            if MODULE.normalize_katex_environments(content) != content:
                invalid.append(str(path.relative_to(posts.parent.parent)))
        self.assertEqual(invalid, [])

    def test_repository_posts_have_no_legacy_math_escape_artifacts(self):
        posts = Path(__file__).resolve().parents[1] / "content" / "posts"
        invalid = []
        for path in sorted(posts.glob("*/index*.md")):
            for line_number, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(),
                start=1,
            ):
                has_nested_passthrough = "$\\[" in line
                has_overescaped_brace = r"\\\\{" in line or r"\\\\}" in line
                if has_nested_passthrough or has_overescaped_brace:
                    relative = path.relative_to(posts.parent.parent)
                    invalid.append(f"{relative}:{line_number}")
        self.assertEqual(invalid, [])


class ImageShortcodeTests(unittest.TestCase):
    def test_converts_standalone_markdown_images(self):
        source = (
            "Before\n\n"
            '![A "quoted" diagram](images/figure.png "Caption")\n\n'
            "After\n"
        )
        expected = (
            "Before\n\n"
            '{{< figure src="images/figure.png" '
            'alt="A \\"quoted\\" diagram" title="Caption" >}}\n\n'
            "After\n"
        )
        self.assertEqual(MODULE.convert_images_to_shortcodes(source), expected)

    def test_does_not_convert_images_inside_code_fences(self):
        source = "```markdown\n![](images/figure.png)\n```\n"
        self.assertEqual(MODULE.convert_images_to_shortcodes(source), source)

    def test_allows_the_same_local_image_to_be_reused(self):
        with tempfile.TemporaryDirectory() as temporary:
            bundle = Path(temporary)
            images = bundle / "images"
            images.mkdir()
            (images / "reused.png").write_bytes(b"image")
            content = bundle / "index.zh-cn.md"
            content.write_text(
                '{{< figure src="images/reused.png" >}}\n'
                '{{< figure src="images/reused.png" >}}\n',
                encoding="utf-8",
            )

            MODULE.verify_bundle_images(content, expected_count=1)


class MetadataTests(unittest.TestCase):
    def test_imported_posts_use_site_author(self):
        self.assertEqual(MODULE.POST_AUTHOR, "Haifei")

    def test_extracts_downloader_header(self):
        source = (
            "# A title\n\n **Author:** [Haifei]\n\n"
            " **Link:** [https://example.test]\n\nBody\n"
        )
        title, author, body = MODULE.extract_downloaded_content(source, "fallback")
        self.assertEqual(title, "A title")
        self.assertEqual(author, "Haifei")
        self.assertEqual(body, "Body\n")

    def test_front_matter_contains_import_metadata(self):
        result = MODULE.build_front_matter(
            title="标题",
            author="Haifei",
            source_url="https://zhuanlan.zhihu.com/p/1",
            date_value=datetime(2026, 7, 26, tzinfo=timezone.utc),
            tags=["physics"],
            categories=["notes"],
        )
        self.assertIn('title: "标题"', result)
        self.assertIn("draft: false", result)
        self.assertIn("math: true", result)
        self.assertIn('originalURL: "https://zhuanlan.zhihu.com/p/1"', result)

    def test_refresh_front_matter_preserves_local_metadata(self):
        existing = (
            "---\n"
            'title: "Old title"\n'
            "date: 2020-01-01T00:00:00+08:00\n"
            'originalURL: "https://zhuanlan.zhihu.com/p/123"\n'
            "aliases:\n"
            '  - "/old-route/"\n'
            "draft: false\n"
            'tags: ["local tag"]\n'
            'categories: ["local category"]\n'
            "---\n\n"
            "Old body\n"
        )
        refreshed = MODULE.refresh_front_matter(
            existing,
            title="New title",
            author="Author",
            source_url="https://zhuanlan.zhihu.com/p/123",
            date_value=datetime(2026, 7, 26, tzinfo=MODULE.SITE_TIMEZONE),
            tags=[],
            categories=[],
        )
        self.assertIn('title: "New title"', refreshed)
        self.assertIn('author: "Author"', refreshed)
        self.assertIn('  - "/old-route/"', refreshed)
        self.assertIn('tags: ["local tag"]', refreshed)
        self.assertIn('categories: ["local category"]', refreshed)

    def test_cookie_header_only_contains_zhihu_domains(self):
        cookies = [
            argparse.Namespace(domain=".zhihu.com", name="a", value="1"),
            argparse.Namespace(domain="www.zhihu.com", name="b", value="2"),
            argparse.Namespace(domain=".example.com", name="secret", value="no"),
        ]
        self.assertEqual(MODULE.cookie_jar_to_header(cookies), "a=1; b=2")

    def test_extracts_original_publish_date_in_site_timezone(self):
        html = (
            '<meta itemprop="datePublished" '
            'content="2025-10-25T08:46:08.000Z">'
            '<meta itemprop="dateModified" '
            'content="2025-10-25T16:33:55.000Z">'
        )
        metadata = MODULE.extract_page_metadata(html)
        self.assertEqual(metadata.published_at.strftime("%Y-%m-%d"), "2025-10-25")
        self.assertEqual(metadata.modified_at.strftime("%Y-%m-%d"), "2025-10-26")

    def test_new_post_slug_is_prefixed_with_zhihu_publish_date(self):
        published = datetime(2025, 10, 25, tzinfo=MODULE.SITE_TIMEZONE)
        self.assertEqual(
            MODULE.build_post_slug(
                published,
                "阻抗匹配/信号完整性速成（实验室版）",
            ),
            "Post_20251025_阻抗匹配-信号完整性速成-实验室版",
        )
        self.assertEqual(
            MODULE.build_post_slug(
                published,
                "阻抗匹配/信号完整性速成（实验室版）",
                "impedance-matching",
            ),
            "Post_20251025_impedance-matching",
        )

    def test_title_slug_keeps_words_and_removes_unsafe_punctuation(self):
        self.assertEqual(
            MODULE.title_to_slug('  Python 协程/异步IO: "入门"？  '),
            "Python-协程-异步IO-入门",
        )


class ImportPipelineTests(unittest.TestCase):
    @staticmethod
    def import_args(*, force=False):
        return argparse.Namespace(
            url="https://zhuanlan.zhihu.com/p/123",
            slug=None,
            tag=["physics"],
            category=["notes"],
            force=force,
            publish=False,
            no_build=True,
            published_date=None,
            html_file=None,
            cookie=None,
            cookie_file=None,
            cookie_from_browser=None,
        )

    @staticmethod
    def incomplete_download(url, cookie, work_dir, *, html_file=None):
        stem = "(20260726)Article_Author"
        (work_dir / f"{stem}.md").write_text(
            "# Article\n\n **Author:** [Author]\n\n"
            f" **Link:** [{url}]\n\n"
            f"![]({stem}/downloaded.png)\n\n"
            f"![]({stem}/missing.png)\n",
            encoding="utf-8",
        )
        asset_dir = work_dir / stem
        asset_dir.mkdir()
        (asset_dir / "downloaded.png").write_bytes(b"image")
        metadata = MODULE.PageMetadata(
            published_at=datetime(
                2026, 7, 26, tzinfo=MODULE.SITE_TIMEZONE
            ),
            modified_at=None,
        )
        return work_dir / f"{stem}.md", stem, metadata

    def test_detects_image_type_from_content_not_url_suffix(self):
        with tempfile.TemporaryDirectory() as temporary:
            disguised_png = Path(temporary) / "figure.jpg"
            disguised_png.write_bytes(b"\x89PNG\r\n\x1a\n" + b"payload")
            self.assertEqual(MODULE.detect_image_suffix(disguised_png), ".png")

    def test_parser_accepts_one_click_english_translation(self):
        args = MODULE.build_parser().parse_args(
            [
                "https://zhuanlan.zhihu.com/p/123",
                "--translate",
                "en",
                "--publish",
            ]
        )
        self.assertEqual(args.translate, "en")
        self.assertTrue(args.publish)

    def test_creates_hugo_bundle_with_images_and_native_latex(self):
        args = self.import_args()

        def fake_download(url, cookie, work_dir, *, html_file=None):
            stem = "(20260726)Article_Author"
            (work_dir / f"{stem}.md").write_text(
                "# Article\n\n **Author:** [Author]\n\n"
                f" **Link:** [{url}]\n\nFormula $x_1$.\n\n"
                f"![]({stem}/figure.png)\n",
                encoding="utf-8",
            )
            asset_dir = work_dir / stem
            asset_dir.mkdir()
            (asset_dir / "figure.png").write_bytes(b"image")
            metadata = MODULE.PageMetadata(
                published_at=datetime(
                    2026, 7, 26, tzinfo=MODULE.SITE_TIMEZONE
                ),
                modified_at=None,
            )
            return work_dir / f"{stem}.md", stem, metadata

        with tempfile.TemporaryDirectory() as temporary:
            posts_dir = Path(temporary) / "posts"
            posts_dir.mkdir()
            with (
                mock.patch.object(MODULE, "POSTS_DIR", posts_dir),
                mock.patch.object(MODULE, "resolve_cookie", return_value="cookie"),
                mock.patch.object(MODULE, "run_downloader", side_effect=fake_download),
            ):
                post = MODULE.import_post(args)

            content = post.content_file.read_text(encoding="utf-8")
            self.assertEqual(post.bundle_dir.name, "Post_20260726_Article")
            self.assertIn("draft: false", content)
            self.assertIn(r"Formula \(x_1\).", content)
            self.assertIn(
                '{{< figure src="images/figure.png" >}}',
                content,
            )
            self.assertTrue((post.bundle_dir / "images" / "figure.png").is_file())

    def test_invalid_new_import_does_not_leave_a_partial_bundle(self):
        args = self.import_args()
        with tempfile.TemporaryDirectory() as temporary:
            posts_dir = Path(temporary) / "posts"
            posts_dir.mkdir()
            with (
                mock.patch.object(MODULE, "POSTS_DIR", posts_dir),
                mock.patch.object(MODULE, "resolve_cookie", return_value="cookie"),
                mock.patch.object(
                    MODULE,
                    "run_downloader",
                    side_effect=self.incomplete_download,
                ),
            ):
                with self.assertRaisesRegex(
                    MODULE.ImportFailure,
                    "图片未成功下载",
                ):
                    MODULE.import_post(args)

            self.assertEqual(list(posts_dir.iterdir()), [])

    def test_invalid_force_import_preserves_the_existing_bundle(self):
        args = self.import_args(force=True)
        with tempfile.TemporaryDirectory() as temporary:
            posts_dir = Path(temporary) / "posts"
            target = posts_dir / "Post_20260726_Article"
            target.mkdir(parents=True)
            marker = target / "existing.txt"
            marker.write_text("keep me", encoding="utf-8")
            with (
                mock.patch.object(MODULE, "POSTS_DIR", posts_dir),
                mock.patch.object(MODULE, "resolve_cookie", return_value="cookie"),
                mock.patch.object(
                    MODULE,
                    "run_downloader",
                    side_effect=self.incomplete_download,
                ),
            ):
                with self.assertRaisesRegex(
                    MODULE.ImportFailure,
                    "图片未成功下载",
                ):
                    MODULE.import_post(args)

            self.assertEqual(marker.read_text(encoding="utf-8"), "keep me")

    def test_force_import_finds_changed_title_by_source_and_keeps_translation(self):
        args = self.import_args(force=True)

        def fake_download(url, cookie, work_dir, *, html_file=None):
            stem = "(20260726)New_Title_Author"
            (work_dir / f"{stem}.md").write_text(
                "# New Title\n\n **Author:** [Author]\n\n"
                f" **Link:** [{url}]\n\nUpdated body.\n",
                encoding="utf-8",
            )
            metadata = MODULE.PageMetadata(
                published_at=datetime(
                    2026, 7, 26, tzinfo=MODULE.SITE_TIMEZONE
                ),
                modified_at=None,
            )
            return work_dir / f"{stem}.md", stem, metadata

        with tempfile.TemporaryDirectory() as temporary:
            posts_dir = Path(temporary) / "posts"
            existing = posts_dir / "Post_20260726_Old-Title"
            existing.mkdir(parents=True)
            (existing / "index.zh-cn.md").write_text(
                "---\n"
                'title: "Old Title"\n'
                "date: 2026-07-26T00:00:00+08:00\n"
                'originalURL: "https://zhuanlan.zhihu.com/p/123"\n'
                "aliases:\n"
                '  - "/old-title/"\n'
                'tags: ["physics"]\n'
                "---\n\nOld body.\n",
                encoding="utf-8",
            )
            (existing / "index.en.md").write_text(
                "---\ntitle: \"Old Title\"\n---\n\nOld translation.\n",
                encoding="utf-8",
            )
            with (
                mock.patch.object(MODULE, "POSTS_DIR", posts_dir),
                mock.patch.object(MODULE, "resolve_cookie", return_value="cookie"),
                mock.patch.object(MODULE, "run_downloader", side_effect=fake_download),
            ):
                post = MODULE.import_post(args)

            self.assertEqual(post.bundle_dir, existing)
            self.assertFalse((posts_dir / "Post_20260726_New-Title").exists())
            content = post.content_file.read_text(encoding="utf-8")
            self.assertIn('title: "New Title"', content)
            self.assertIn('  - "/old-title/"', content)
            self.assertIn('tags: ["physics"]', content)
            self.assertTrue((existing / "index.en.md").is_file())


if __name__ == "__main__":
    unittest.main()
