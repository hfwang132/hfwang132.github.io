import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))
import sync_zhihu_dates as MODULE  # noqa: E402


class ZhihuDateSyncTests(unittest.TestCase):
    def test_updates_all_languages_renames_bundle_and_keeps_routes(self):
        with tempfile.TemporaryDirectory() as temporary:
            posts = Path(temporary) / "posts"
            source = posts / "Post_20240527_文章标题"
            source.mkdir(parents=True)
            for language in ("zh-cn", "en"):
                prefix = "" if language == "zh-cn" else "/en"
                (source / f"index.{language}.md").write_text(
                    "---\n"
                    f'title: "{"文章标题" if language == "zh-cn" else "English title"}"\n'
                    "date: 2024-05-27T17:47:25+08:00\n"
                    "aliases:\n"
                    f'  - "{prefix}/old-route/"\n'
                    "draft: false\n"
                    "---\n\nBody\n",
                    encoding="utf-8",
                )

            mapping_file = Path(temporary) / "mapping.json"
            mapping_file.write_text(
                json.dumps(
                    [
                        {
                            "localTitle": "文章标题",
                            "zhihuTitle": "文章标题？",
                            "sourceURL": "https://zhuanlan.zhihu.com/p/123",
                            "datePublished": "2023-02-01T08:30:00Z",
                        }
                    ],
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            entries = MODULE.load_mapping(mapping_file)
            MODULE.apply_entries(entries, posts)

            destination = posts / "Post_20230201_文章标题"
            self.assertFalse(source.exists())
            for language in ("zh-cn", "en"):
                content = (destination / f"index.{language}.md").read_text(
                    encoding="utf-8"
                )
                self.assertIn(
                    "date: 2023-02-01T16:30:00+08:00",
                    content,
                )
                self.assertIn(
                    'originalURL: "https://zhuanlan.zhihu.com/p/123"',
                    content,
                )
                self.assertIn("old-route", content)
                self.assertIn("Post_20240527_文章标题", content)


if __name__ == "__main__":
    unittest.main()
