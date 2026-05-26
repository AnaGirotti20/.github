from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]


class CommunityHealthFileTests(unittest.TestCase):
    def test_required_community_health_files_exist_and_are_not_empty(self):
        required_paths = [
            REPO_ROOT / "README.md",
            REPO_ROOT / "CODE_OF_CONDUCT.md",
            REPO_ROOT / "CONTRIBUTING.md",
            REPO_ROOT / "SECURITY.md",
            REPO_ROOT / "profile" / "README.md",
            REPO_ROOT / "config" / "repolinter-ruleset.json",
        ]

        for path in required_paths:
            with self.subTest(path=str(path)):
                self.assertTrue(path.exists(), f"Missing expected file: {path}")
                self.assertGreater(path.stat().st_size, 0, f"File should not be empty: {path}")

    def test_markdown_files_start_with_heading(self):
        markdown_files = [
            REPO_ROOT / "README.md",
            REPO_ROOT / "CODE_OF_CONDUCT.md",
            REPO_ROOT / "CONTRIBUTING.md",
            REPO_ROOT / "SECURITY.md",
            REPO_ROOT / "profile" / "README.md",
        ]

        for path in markdown_files:
            with self.subTest(path=str(path)):
                content = path.read_text(encoding="utf-8").lstrip()
                self.assertTrue(content.startswith("#"), f"Expected markdown heading in {path}")


if __name__ == "__main__":
    unittest.main()
