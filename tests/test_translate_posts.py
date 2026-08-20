import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "translate_posts.py"
SPEC = importlib.util.spec_from_file_location("translate_posts", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class TranslationProtectionTests(unittest.TestCase):
    def make_source(self, root: Path):
        bundle = root / "content" / "posts" / "Post_20260726_Test"
        images = bundle / "images"
        images.mkdir(parents=True)
        (images / "figure.png").write_bytes(b"image")
        source_file = bundle / "index.zh-cn.md"
        source_file.write_text(
            "---\n"
            'title: "测试文章"\n'
            "date: 2026-07-26T10:00:00+08:00\n"
            'originalURL: "https://example.test/source"\n'
            "aliases:\n"
            '  - "/old-path/"\n'
            "draft: false\n"
            "math: true\n"
            'tags: ["量子光学"]\n'
            'categories: ["量子信息"]\n'
            "---\n\n"
            "## 中文标题\n\n"
            r"正文含有公式 $a+b=c\\d$。"
            "\n\n"
            '{{< figure src="images/figure.png" title="实验装置图" >}}\n\n'
            "```python\n"
            'print("不要翻译")\n'
            "```\n\n"
            "见 [参考文献](#ref_1)。\n",
            encoding="utf-8",
        )
        return MODULE.prepare_source(source_file)

    def translated_object(self, source):
        payload = MODULE.translation_payload(source)
        body = payload["body"].replace("中文标题", "English heading")
        body = body.replace("正文含有公式", "The text contains the equation")
        body = body.replace("见 ", "See ")
        body = body.replace("参考文献", "Reference")
        return {
            "title": "Test article",
            "tags": ["Quantum Optics"],
            "categories": ["Quantum Information"],
            "body": body,
            "captions": [
                {
                    "token": item["token"],
                    "alt": item["alt"],
                    "title": "Experimental setup",
                }
                for item in payload["captions"]
            ],
        }

    def test_renders_translation_without_changing_sensitive_markdown(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = self.make_source(Path(temporary))
            translated = self.translated_object(source)
            rendered = MODULE.render_translation(source, translated)

        self.assertIn('title: "Test article"', rendered)
        self.assertIn('tags: ["Quantum Optics"]', rendered)
        self.assertIn('  - "/en/old-path/"', rendered)
        self.assertIn(r"$a+b=c\\d$", rendered)
        self.assertIn('print("不要翻译")', rendered)
        self.assertIn('src="images/figure.png"', rendered)
        self.assertIn('title="Experimental setup"', rendered)
        self.assertIn("[Reference](#ref_1)", rendered)
        self.assertNotIn(MODULE.PROTECTED_TOKEN_PREFIX, rendered)

    def test_verifies_a_rendered_translation_pair(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = self.make_source(Path(temporary))
            translated = self.translated_object(source)
            rendered = MODULE.render_translation(source, translated)
            source.source_file.with_name("index.en.md").write_text(
                rendered, encoding="utf-8"
            )
            MODULE.verify_translation_pair(source.source_file)

    def test_rejects_a_changed_protection_token(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = self.make_source(Path(temporary))
            translated = self.translated_object(source)
            translated["body"] = translated["body"].replace(
                MODULE.PROTECTED_TOKEN_PREFIX, "@@CHANGED_", 1
            )
            with self.assertRaisesRegex(
                MODULE.TranslationFailure, "受保护标记"
            ):
                MODULE.render_translation(source, translated)

    def test_responses_request_uses_structured_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = self.make_source(Path(temporary))
            request = MODULE.response_request(source, "gpt-test")

        self.assertEqual(request["model"], "gpt-test")
        self.assertEqual(request["reasoning"], {"effort": "low"})
        self.assertEqual(
            request["text"]["format"]["name"], "translated_article"
        )
        self.assertEqual(
            request["text"]["format"]["schema"], MODULE.TRANSLATION_SCHEMA
        )
        self.assertEqual(json.loads(request["input"])["title"], "测试文章")

    def test_translate_parser_accepts_explicit_full_strategy(self):
        args = MODULE.build_parser().parse_args(
            [
                "translate",
                "content/posts/example",
                "--strategy",
                "full",
            ]
        )
        self.assertEqual(args.strategy, "full")

    def test_protection_does_not_create_nested_tokens(self):
        source = '<a href="https://example.test/path">链接</a>\n'
        protected, entries = MODULE.protect_markdown(source)
        translated = {
            "title": "Title",
            "tags": [],
            "categories": [],
            "body": protected,
            "captions": [],
        }
        translation_source = MODULE.TranslationSource(
            source_file=Path("index.zh-cn.md"),
            source_text="",
            header='title: "标题"',
            body=source,
            title="标题",
            tags=[],
            categories=[],
            protected_body=protected,
            protected=entries,
        )
        self.assertEqual(
            MODULE.restore_body(translation_source, translated), source
        )

    def test_url_used_as_link_label_does_not_create_nested_tokens(self):
        source = (
            "[https://doi.org/10.1000/example]"
            "(https://doi.org/10.1000/example)\n"
        )
        protected, entries = MODULE.protect_markdown(source)
        translated = {
            "title": "Title",
            "tags": [],
            "categories": [],
            "body": protected,
            "captions": [],
        }
        translation_source = MODULE.TranslationSource(
            source_file=Path("index.zh-cn.md"),
            source_text="",
            header='title: "标题"',
            body=source,
            title="标题",
            tags=[],
            categories=[],
            protected_body=protected,
            protected=entries,
        )
        self.assertEqual(
            MODULE.restore_body(translation_source, translated), source
        )
        self.assertFalse(
            any(MODULE.PROTECTED_TOKEN_PREFIX in entry.value for entry in entries)
        )

    def test_force_refresh_preserves_english_taxonomy_missing_from_source(self):
        rendered = (
            "---\n"
            'title: "Refreshed"\n'
            "draft: false\n"
            "---\n\n"
            "New body.\n"
        )
        existing = (
            "---\n"
            'title: "Old"\n'
            'tags: ["Time Tagger", "TDC"]\n'
            'categories: ["EECS"]\n'
            "---\n\n"
            "Old body.\n"
        )
        result = MODULE.preserve_existing_translation_metadata(rendered, existing)
        self.assertIn('tags: ["Time Tagger", "TDC"]', result)
        self.assertIn('categories: ["EECS"]', result)
        self.assertEqual(result.count("tags:"), 1)

    def test_protected_markdown_chunks_do_not_split_or_duplicate_tokens(self):
        source = (
            "First paragraph @@HFPROTECT_00000@@.\n\n"
            "Second paragraph @@HFPROTECT_00001@@.\n\n"
            "Third paragraph @@HFPROTECT_00002@@.\n"
        )
        chunks = MODULE.split_protected_markdown(source, max_chars=55)
        self.assertGreater(len(chunks), 1)
        self.assertEqual("".join(chunks), source)
        for token in (
            "@@HFPROTECT_00000@@",
            "@@HFPROTECT_00001@@",
            "@@HFPROTECT_00002@@",
        ):
            self.assertEqual(sum(chunk.count(token) for chunk in chunks), 1)

    def test_repairs_reused_tokens_for_byte_identical_math_only(self):
        entries = (
            MODULE.ProtectedEntry(
                "@@HFPROTECT_00000@@", "math", r"$\mathcal{F}$"
            ),
            MODULE.ProtectedEntry(
                "@@HFPROTECT_00001@@", "math", r"$\mathcal{F}$"
            ),
        )
        source = MODULE.TranslationSource(
            source_file=Path("index.zh-cn.md"),
            source_text="",
            header='title: "标题"',
            body="",
            title="标题",
            tags=[],
            categories=[],
            protected_body=(
                "@@HFPROTECT_00000@@ and @@HFPROTECT_00001@@"
            ),
            protected=entries,
        )
        translated = {
            "title": "Title",
            "tags": [],
            "categories": [],
            "body": "@@HFPROTECT_00001@@ and @@HFPROTECT_00001@@",
            "captions": [],
        }
        restored = MODULE.restore_body(source, translated)
        self.assertEqual(
            restored,
            r"$\mathcal{F}$ and $\mathcal{F}$",
        )

    def test_segment_request_enforces_exact_fragment_count(self):
        request = MODULE.segment_response_request(["one", "two"], "test-model")
        schema = request["text"]["format"]["schema"]
        translations = schema["properties"]["translations"]
        self.assertEqual(translations["minItems"], 2)
        self.assertEqual(translations["maxItems"], 2)

    def test_paragraph_request_requires_exact_mapping_keys(self):
        request = MODULE.paragraph_response_request(
            {"p000": "第一段", "p001": "第二段"},
            "test-model",
        )
        translations = request["text"]["format"]["schema"]["properties"][
            "translations"
        ]
        self.assertEqual(translations["required"], ["p000", "p001"])
        self.assertEqual(
            set(translations["properties"]), {"p000", "p001"}
        )

    def test_paragraph_placeholders_are_restored_by_source_order(self):
        source = (
            "定义 @@HFPROTECT_00088@@，然后使用 "
            "@@HFPROTECT_00102@@。"
        )
        encoded = MODULE.encode_paragraph_placeholders(source)
        self.assertIn('<ph id="00088"/>', encoded)
        translated = (
            'Define <ph id="00088"/>, then use <ph id="00088"/>.'
        )
        self.assertEqual(
            MODULE.restore_paragraph_placeholders(source, translated),
            "Define @@HFPROTECT_00088@@, then use "
            "@@HFPROTECT_00102@@.",
        )

    def test_valid_paragraph_placeholder_reordering_is_preserved(self):
        source = (
            "集合 @@HFPROTECT_00088@@ 的拓扑是 "
            "@@HFPROTECT_00102@@。"
        )
        translated = (
            'A topology <ph id="00102"/> on the set '
            '<ph id="00088"/>.'
        )
        self.assertEqual(
            MODULE.restore_paragraph_placeholders(source, translated),
            "A topology @@HFPROTECT_00102@@ on the set "
            "@@HFPROTECT_00088@@.",
        )

    def test_paragraph_placeholder_count_must_not_change(self):
        source = "定义 @@HFPROTECT_00088@@。"
        with self.assertRaises(MODULE.TranslationFailure):
            MODULE.restore_paragraph_placeholders(source, "Define it.")

    def test_markdown_structure_signature_tracks_quotes_and_headings(self):
        source = "## 标题\n> 引用\n1. 项目\n"
        translated = "## Title\n> Quote\n1. Item\n"
        self.assertEqual(
            MODULE.markdown_structure_signature(source),
            MODULE.markdown_structure_signature(translated),
        )

    def test_restores_markdown_prefixes_from_source_fragment(self):
        source = "## 中文标题\n> 引用\n1. 项目"
        translated = "English title\nQuote\nItem"
        self.assertEqual(
            MODULE.restore_markdown_structure(source, translated),
            "## English title\n> Quote\n1. Item",
        )

    def test_rejects_control_markers_and_extreme_segment_expansion(self):
        self.assertTrue(
            MODULE.suspicious_segment_translation(
                "normal source", "text <|endoftext|> assistant to=system"
            )
        )
        self.assertTrue(
            MODULE.suspicious_segment_translation("short", "x" * 1600)
        )
        self.assertFalse(
            MODULE.suspicious_segment_translation(
                "一段正常的中文", "A normal English paragraph."
            )
        )

    def test_edge_whitespace_is_split_without_losing_markdown_spacing(self):
        self.assertEqual(
            MODULE._edge_whitespace("\n  中文内容  \n"),
            ("\n  ", "中文内容", "  \n"),
        )

    def test_segmented_translation_cache_is_ignored_by_git(self):
        gitignore = (Path(__file__).resolve().parents[1] / ".gitignore").read_text(
            encoding="utf-8"
        )
        self.assertIn(".secrets/", gitignore)

    def test_adds_caption_to_compact_figure_shortcode(self):
        shortcode = '{{< figure src="images/a.png">}}'
        replaced = MODULE._replace_shortcode_caption(
            shortcode, "title", "A caption"
        )
        self.assertEqual(
            replaced,
            '{{< figure src="images/a.png" title="A caption" >}}',
        )


class ApiKeyTests(unittest.TestCase):
    def test_environment_key_has_priority(self):
        with (
            tempfile.TemporaryDirectory() as temporary,
            mock.patch.dict(os.environ, {"OPENAI_API_KEY": "sk-env"}, clear=False),
        ):
            key_file = Path(temporary) / "key.txt"
            key_file.write_text("sk-file", encoding="utf-8")
            self.assertEqual(MODULE.load_api_key(key_file), "sk-env")

    def test_reads_key_from_file_without_logging_it(self):
        with (
            tempfile.TemporaryDirectory() as temporary,
            mock.patch.dict(os.environ, {}, clear=True),
        ):
            key_file = Path(temporary) / "key.txt"
            key_file.write_text("sk-file\n", encoding="utf-8")
            self.assertEqual(MODULE.load_api_key(key_file), "sk-file")

    def test_missing_key_has_actionable_error(self):
        with (
            tempfile.TemporaryDirectory() as temporary,
            mock.patch.dict(os.environ, {}, clear=True),
        ):
            missing = Path(temporary) / "missing.txt"
            with self.assertRaisesRegex(
                MODULE.TranslationFailure, "OPENAI_API_KEY"
            ):
                MODULE.load_api_key(missing)

    def test_hidden_key_setup_writes_only_the_key(self):
        with tempfile.TemporaryDirectory() as temporary:
            key_file = Path(temporary) / ".secrets" / "openai-api-key.txt"
            with mock.patch.object(
                MODULE.getpass, "getpass", return_value="sk-hidden"
            ):
                saved = MODULE.save_api_key(key_file)

            self.assertEqual(saved, key_file)
            self.assertEqual(key_file.read_text(encoding="utf-8"), "sk-hidden\n")

    def test_key_setup_rejects_whitespace(self):
        with (
            tempfile.TemporaryDirectory() as temporary,
            mock.patch.object(
                MODULE.getpass, "getpass", return_value="sk bad"
            ),
        ):
            key_file = Path(temporary) / "key.txt"
            with self.assertRaisesRegex(
                MODULE.TranslationFailure, "空格或换行"
            ):
                MODULE.save_api_key(key_file)
            self.assertFalse(key_file.exists())


class BatchPipelineTests(unittest.TestCase):
    def test_selects_only_zhihu_column_articles_for_refresh(self):
        with tempfile.TemporaryDirectory() as temporary:
            posts_dir = Path(temporary)
            article = posts_dir / "article"
            answer = posts_dir / "answer"
            original = posts_dir / "original"
            article.mkdir()
            answer.mkdir()
            original.mkdir()
            (article / "index.zh-cn.md").write_text(
                "---\n"
                'title: "Article"\n'
                'originalURL: "https://zhuanlan.zhihu.com/p/123"\n'
                "---\n\nBody\n",
                encoding="utf-8",
            )
            (answer / "index.zh-cn.md").write_text(
                "---\n"
                'title: "Answer"\n'
                'originalURL: "https://www.zhihu.com/question/1/answer/2"\n'
                "---\n\nBody\n",
                encoding="utf-8",
            )
            (original / "index.zh-cn.md").write_text(
                "---\ntitle: \"Original\"\n---\n\nBody\n",
                encoding="utf-8",
            )
            with mock.patch.object(MODULE, "POSTS_DIR", posts_dir):
                selected = MODULE.select_translation_sources("zhihu-articles")

            self.assertEqual(selected, [article / "index.zh-cn.md"])

    def test_applies_completed_batch_with_source_hash_check(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            helper = TranslationProtectionTests()
            source = helper.make_source(root)
            translated = helper.translated_object(source)
            batch_id = "batch_test"
            batch_dir = root / ".secrets" / "openai-batches"
            batch_dir.mkdir(parents=True)
            state = {
                "batch_id": batch_id,
                "records": [
                    {
                        "custom_id": "post-0001-test",
                        "source": source.source_file.relative_to(root).as_posix(),
                        "source_sha256": source.source_sha256,
                    }
                ],
            }
            (batch_dir / f"{batch_id}.json").write_text(
                json.dumps(state), encoding="utf-8"
            )
            openai_body = {
                "output": [
                    {
                        "type": "message",
                        "content": [
                            {
                                "type": "output_text",
                                "text": json.dumps(
                                    translated, ensure_ascii=False
                                ),
                            }
                        ],
                    }
                ]
            }
            output = (
                json.dumps(
                    {
                        "custom_id": "post-0001-test",
                        "response": {
                            "status_code": 200,
                            "body": openai_body,
                        },
                        "error": None,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            ).encode("utf-8")

            class FakeClient:
                @staticmethod
                def retrieve_batch(received_id):
                    assert received_id == batch_id
                    return {
                        "id": batch_id,
                        "status": "completed",
                        "output_file_id": "file-output",
                    }

                @staticmethod
                def download_file(file_id):
                    assert file_id == "file-output"
                    return output

            with (
                mock.patch.object(MODULE, "REPO_ROOT", root),
                mock.patch.object(MODULE, "POSTS_DIR", root / "content" / "posts"),
                mock.patch.object(MODULE, "DEFAULT_BATCH_DIR", batch_dir),
            ):
                written = MODULE.apply_batch(batch_id, client=FakeClient())

            self.assertEqual(written, [source.source_file.with_name("index.en.md")])
            rendered = written[0].read_text(encoding="utf-8")
            self.assertIn('title: "Test article"', rendered)
            self.assertIn(r"$a+b=c\\d$", rendered)


if __name__ == "__main__":
    unittest.main()
