import json
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
RULESET_PATH = REPO_ROOT / "config" / "repolinter-ruleset.json"


class RepolinterRulesetTests(unittest.TestCase):
    def setUp(self):
        self.raw_text = RULESET_PATH.read_text(encoding="utf-8")
        self.ruleset = json.loads(self.raw_text)

    def test_ruleset_is_valid_json(self):
        self.assertIsInstance(self.ruleset, dict)

    def test_ruleset_has_expected_top_level_shape(self):
        self.assertEqual(self.ruleset.get("version"), 2)
        self.assertIn("rules", self.ruleset)
        self.assertIsInstance(self.ruleset["rules"], dict)
        self.assertGreaterEqual(len(self.ruleset["rules"]), 1)

    def test_expected_rules_exist(self):
        expected_rules = {
            "license-file-is-MIT",
            "readme-file-exists",
            "codeowners-file-exists",
        }
        self.assertTrue(expected_rules.issubset(set(self.ruleset["rules"].keys())))

    def test_each_rule_has_required_policy_metadata(self):
        for name, rule_data in self.ruleset["rules"].items():
            with self.subTest(rule=name):
                self.assertIn("policyInfo", rule_data)
                self.assertIn("policyUrl", rule_data)
                self.assertTrue(str(rule_data["policyInfo"]).strip())
                self.assertTrue(str(rule_data["policyUrl"]).startswith("https://"))

    def test_format_disclaimer_references_repolinter_action(self):
        disclaimer = self.ruleset["formatOptions"]["disclaimer"]
        self.assertIn("repolinter-action", disclaimer)


if __name__ == "__main__":
    unittest.main()
