import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))
import migrate_post_names as MODULE  # noqa: E402


class PostFolderMigrationTests(unittest.TestCase):
    def test_renames_bundle_not_index_files_and_preserves_old_routes(self):
        with tempfile.TemporaryDirectory() as temporary:
            posts = Path(temporary) / "posts"
            source = posts / "old_slug"
            source.mkdir(parents=True)
            (source / "index.zh-cn.md").write_text(
                "---\n"
                'title: "文章/标题？"\n'
                "date: 2024-05-27T17:47:25+08:00\n"
                "draft: false\n"
                "---\n\n正文\n",
                encoding="utf-8",
            )
            (source / "index.en.md").write_text(
                "---\n"
                'title: "English title"\n'
                "date: 2024-06-01T00:00:00+08:00\n"
                "draft: false\n"
                "---\n\nBody\n",
                encoding="utf-8",
            )
            (source / "image.png").write_bytes(b"image")

            plan = MODULE.build_plan(posts)
            self.assertEqual(len(plan), 1)
            self.assertEqual(
                plan[0].destination.name,
                "Post_20240527_文章-标题",
            )
            MODULE.apply_plan(plan)

            destination = posts / "Post_20240527_文章-标题"
            self.assertFalse(source.exists())
            self.assertTrue((destination / "index.zh-cn.md").is_file())
            self.assertTrue((destination / "index.en.md").is_file())
            self.assertEqual((destination / "image.png").read_bytes(), b"image")
            self.assertIn(
                '  - "/old_slug/"',
                (destination / "index.zh-cn.md").read_text(encoding="utf-8"),
            )
            self.assertIn(
                '  - "/en/old_slug/"',
                (destination / "index.en.md").read_text(encoding="utf-8"),
            )
            MODULE.add_alias(
                destination / "index.zh-cn.md",
                "/another-old-route/",
            )
            zh_content = (destination / "index.zh-cn.md").read_text(
                encoding="utf-8"
            )
            self.assertIn('  - "/old_slug/"', zh_content)
            self.assertIn('  - "/another-old-route/"', zh_content)
            self.assertEqual(MODULE.build_plan(posts), [])


if __name__ == "__main__":
    unittest.main()
