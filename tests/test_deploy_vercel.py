import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import deploy_vercel


class VercelStaticPathTests(unittest.TestCase):
    def test_non_ascii_files_use_ascii_storage_and_keep_public_url(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            static_dir = Path(temporary_directory)
            source = static_dir / "Post_20240523_位置测量的塌缩态" / "index.html"
            source.parent.mkdir(parents=True)
            source.write_text("<h1>位置测量</h1>", encoding="utf-8")

            with patch.object(deploy_vercel, "STATIC_DIR", static_dir):
                config = deploy_vercel.prepare_static_files()

            self.assertFalse(source.exists())
            self.assertEqual(len(config["overrides"]), 1)
            stored_path, override = next(iter(config["overrides"].items()))
            self.assertTrue(stored_path.isascii())
            self.assertTrue(stored_path.startswith("_vercel_unicode/"))
            self.assertEqual(
                override["path"],
                "Post_20240523_位置测量的塌缩态/index.html",
            )
            self.assertEqual(
                (static_dir / stored_path).read_text(encoding="utf-8"),
                "<h1>位置测量</h1>",
            )
            self.assertTrue(json.dumps(config).isascii())

    def test_ascii_files_are_not_relocated(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            static_dir = Path(temporary_directory)
            source = static_dir / "posts" / "index.html"
            source.parent.mkdir(parents=True)
            source.write_text("posts", encoding="utf-8")

            with patch.object(deploy_vercel, "STATIC_DIR", static_dir):
                config = deploy_vercel.prepare_static_files()

            self.assertTrue(source.is_file())
            self.assertNotIn("overrides", config)


if __name__ == "__main__":
    unittest.main()
