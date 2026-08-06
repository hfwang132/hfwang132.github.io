import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "audit_math.py"
SPEC = importlib.util.spec_from_file_location("audit_math", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class MathAuditTests(unittest.TestCase):
    def test_extracts_inline_and_display_math(self):
        node = MODULE.TextNode(r"Before \(x_1\), then \[y^2\].", 12)
        formulas, unmatched = MODULE.extract_formulas(node)
        self.assertEqual([formula.source for formula in formulas], ["x_1", "y^2"])
        self.assertEqual([formula.display for formula in formulas], [False, True])
        self.assertEqual(unmatched, [])

    def test_keeps_right_delimiter_inside_braces(self):
        node = MODULE.TextNode(r"\(\text{literal \) text}\)", 3)
        formulas, unmatched = MODULE.extract_formulas(node)
        self.assertEqual([formula.source for formula in formulas], [r"\text{literal \) text}"])
        self.assertEqual(unmatched, [])

    def test_reports_unmatched_native_delimiter(self):
        formulas, unmatched = MODULE.extract_formulas(MODULE.TextNode(r"\(x+1", 4))
        self.assertEqual(formulas, [])
        self.assertEqual(unmatched, [r"\("])

    def test_text_outside_math_preserves_only_prose(self):
        source = r"Before \(x_1\), between, $y^2$, after."
        self.assertEqual(
            MODULE.text_outside_math(source),
            "Before , between, , after.",
        )

    def test_ignores_code_and_script_text(self):
        parser = MODULE.VisibleTextParser()
        parser.feed("<p>\\(x\\)</p><code>\\(bad</code><script>$bad$</script>")
        self.assertEqual([node.text for node in parser.nodes], [r"\(x\)"])

    def test_native_math_pattern_finds_html_sensitive_operator(self):
        match = MODULE.NATIVE_MATH.search(r"Text \(0<x<1\) text")
        self.assertIsNotNone(match)
        self.assertEqual(match.group("inline_body"), "0<x<1")

    def test_single_dollar_pattern_ignores_display_and_escaped_dollars(self):
        pattern = r"(?<!\\)(?<!\$)\$(?!\$)"
        text = r"$$x$$, \$10, and $y$."
        self.assertEqual(len(MODULE.re.findall(pattern, text)), 2)


if __name__ == "__main__":
    unittest.main()
