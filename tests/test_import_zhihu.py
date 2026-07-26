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


class MetadataTests(unittest.TestCase):
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
    def test_detects_image_type_from_content_not_url_suffix(self):
        with tempfile.TemporaryDirectory() as temporary:
            disguised_png = Path(temporary) / "figure.jpg"
            disguised_png.write_bytes(b"\x89PNG\r\n\x1a\n" + b"payload")
            self.assertEqual(MODULE.detect_image_suffix(disguised_png), ".png")

    def test_creates_hugo_bundle_with_images_and_native_latex(self):
        args = argparse.Namespace(
            url="https://zhuanlan.zhihu.com/p/123",
            slug=None,
            tag=["physics"],
            category=["notes"],
            force=False,
            publish=False,
            no_build=True,
            published_date=None,
            html_file=None,
            cookie=None,
            cookie_file=None,
            cookie_from_browser=None,
        )

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


if __name__ == "__main__":
    unittest.main()
