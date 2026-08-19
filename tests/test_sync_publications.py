import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import sync_publications


SAMPLE_BIB = r"""
@article{Published2025,
  author = {First Author and Haifei Wang},
  title = {A Published Result},
  journal = {Physical Review Letters},
  volume = {135},
  pages = {060801},
  date = {2025-08-04},
  year = {2025},
  doi = {10.1103/example},
  url = {https://doi.org/10.1103/example},
  status = {published}
}

@misc{Preprint2026,
  author = {Haifei Wang and Second Author},
  title = {A New Preprint},
  date = {2026-08-16},
  year = {2026},
  eprint = {2608.00001},
  archiveprefix = {arXiv},
  primaryclass = {quant-ph},
  url = {https://arxiv.org/abs/2608.00001},
  status = {preprint}
}
"""


class PublicationSyncTests(unittest.TestCase):
    def test_parses_and_sorts_bibtex_entries(self):
        publications = sync_publications.build_publication_data(SAMPLE_BIB)

        self.assertEqual([item["year"] for item in publications], [2026, 2025])
        self.assertEqual(
            publications[0]["authors"], ["Haifei Wang", "Second Author"]
        )
        self.assertEqual(publications[0]["eprint"], "2608.00001")
        self.assertEqual(publications[1]["journal"], "Physical Review Letters")

    def test_rejects_missing_status_specific_fields(self):
        invalid = SAMPLE_BIB.replace("  eprint = {2608.00001},\n", "")
        with self.assertRaisesRegex(
            sync_publications.PublicationSyncError, "missing required field: eprint"
        ):
            sync_publications.build_publication_data(invalid)

    def test_check_detects_and_accepts_generated_data(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            directory = Path(temporary_directory)
            bib_path = directory / "publications.bib"
            json_path = directory / "publications.json"
            bib_path.write_text(SAMPLE_BIB, encoding="utf-8")

            with (
                patch.object(sync_publications, "BIB_SOURCE", bib_path),
                patch.object(sync_publications, "JSON_DESTINATION", json_path),
            ):
                with self.assertRaises(sync_publications.PublicationSyncError):
                    sync_publications.synchronize(check=True)
                sync_publications.synchronize()
                sync_publications.synchronize(check=True)

            data = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(len(data), 2)

    def test_repository_generated_data_matches_bibtex(self):
        expected = sync_publications.rendered_json(
            sync_publications.BIB_SOURCE.read_text(encoding="utf-8")
        )
        actual = sync_publications.JSON_DESTINATION.read_text(encoding="utf-8")
        self.assertEqual(actual, expected)

    def test_language_pages_only_invoke_shared_renderer(self):
        for page in (
            sync_publications.REPO_ROOT / "content" / "publication" / "index.en.md",
            sync_publications.REPO_ROOT
            / "content"
            / "publication"
            / "index.zh-cn.md",
        ):
            body = page.read_text(encoding="utf-8").split("---", 2)[-1].strip()
            self.assertEqual(body, "{{< publications >}}")


if __name__ == "__main__":
    unittest.main()
