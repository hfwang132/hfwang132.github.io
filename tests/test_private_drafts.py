import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIR = ROOT / "content"
DRAFT_TRUE = re.compile(
    r"^draft\s*[:=]\s*['\"]?true['\"]?\s*(?:#.*)?$",
    re.IGNORECASE | re.MULTILINE,
)


def front_matter(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() not in {"---", "+++"}:
        return ""

    delimiter = lines[0].strip()
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == delimiter:
            return "\n".join(lines[1:index])
    return ""


class PrivateDraftIsolationTests(unittest.TestCase):
    def test_public_content_contains_no_drafts(self) -> None:
        offenders = []
        for path in CONTENT_DIR.rglob("*.md"):
            text = path.read_text(encoding="utf-8-sig")
            if DRAFT_TRUE.search(front_matter(text)):
                offenders.append(path.relative_to(ROOT).as_posix())

        self.assertEqual(
            offenders,
            [],
            "Move draft pages from content/ to private-content/:\n"
            + "\n".join(offenders),
        )


if __name__ == "__main__":
    unittest.main()
