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
            r"正文含有公式 \(a+b=c\\d\)。"
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
        self.assertIn(r"\(a+b=c\\d\)", rendered)
        self.assertIn('print("不要翻译")', rendered)
        self.assertIn('src="images/figure.png"', rendered)
        self.assertIn('title="Experimental setup"', rendered)
        self.assertIn("[Reference](#ref_1)", rendered)
        self.assertNotIn(MODULE.PROTECTED_TOKEN_PREFIX, rendered)

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
            self.assertIn(r"\(a+b=c\\d\)", rendered)


if __name__ == "__main__":
    unittest.main()
