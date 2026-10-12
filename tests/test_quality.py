"""Offline checks on deterministic utilities and the research contract.

Never fetch real profiles or contact external services during CI.
"""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from style_compare import cosine  # noqa: E402


class OfflineQualityTests(unittest.TestCase):
    def test_identical_synthetic_vectors_have_full_cosine_similarity(self):
        self.assertAlmostEqual(cosine([1.0, 0.0], [1.0, 0.0]), 1.0)

    def test_orthogonal_synthetic_vectors_have_zero_similarity(self):
        self.assertAlmostEqual(cosine([1.0, 0.0], [0.0, 1.0]), 0.0)

    def test_empty_vector_has_zero_similarity_not_nan(self):
        self.assertEqual(cosine([0.0, 0.0], [1.0, 0.0]), 0.0)

    def test_research_contract_and_ethics_are_documented(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        protocol = (ROOT / "docs" / "EVALUATION_PROTOCOL.md").read_text(encoding="utf-8")
        self.assertIn("## Ethics", readme)
        for term in ("negative control", "false-positive", "synthetic", "not proof"):
            self.assertIn(term, protocol.lower())


if __name__ == "__main__":
    unittest.main()
