import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync_cv.py"
SPEC = importlib.util.spec_from_file_location("sync_cv", SCRIPT)
assert SPEC and SPEC.loader
sync_cv = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = sync_cv
SPEC.loader.exec_module(sync_cv)


class SyncCvTests(unittest.TestCase):
    def test_converts_structured_cv_latex(self):
        source = r"""
        \documentclass{resume}
        \begin{document}
        \section{Summary}
        FPGA \& quantum hardware.
        \section{Experience}
        \datedsubsection{\textbf{Researcher}, \textit{NUS}}{2023 -- Present}
        \begin{itemize}
          \item Built a $>$200$\times$ accelerator.
          \item Published in \href{https://example.com}{\textit{PRL}}.
        \end{itemize}
        \end{document}
        """
        rendered = sync_cv.latex_body_to_html_markdown(source)
        self.assertIn("## Summary", rendered)
        self.assertIn("<strong>Researcher</strong>", rendered)
        self.assertIn('<span class="cv-entry-date">2023 – Present</span>', rendered)
        self.assertIn("- Built a &gt;200× accelerator.", rendered)
        self.assertIn('<a href="https://example.com"><em>PRL</em></a>', rendered)

    def test_strips_comments_but_preserves_escaped_percent(self):
        source = "value \\% retained % removed\nnext"
        self.assertEqual(
            sync_cv.strip_latex_comments(source),
            "value \\% retained\nnext",
        )

    def test_splits_shared_data_into_sections(self):
        sections = sync_cv.split_cv_sections(
            "## Summary\n\nOne paragraph.\n\n## Experience\n\n- One item"
        )
        self.assertEqual(
            sections,
            [
                {"title": "Summary", "content": "One paragraph."},
                {"title": "Experience", "content": "- One item"},
            ],
        )

    def test_page_stubs_only_invoke_the_shared_renderer(self):
        rendered = sync_cv.render_page_stub(title="王海飞 — 简历")
        self.assertIn('title: "王海飞 — 简历"', rendered)
        self.assertIn("{{< cv >}}", rendered)
        self.assertNotIn("aliases:", rendered)


if __name__ == "__main__":
    unittest.main()
