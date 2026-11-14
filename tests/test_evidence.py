import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.evidence import evidence_hit, exact_span, strict_starter_hit  # noqa: E402

CHUNK = {"id": "B-x", "source_id": "doc", "source": "doc.pdf", "page": 23,
         "text": "Điều 31. Thời hạn\n1. Thời hạn hoạt động của dự án\nđầu tư trong khu kinh tế không quá 70 năm.",
         "metadata": {"page_end": 24}}
QUOTE = "Thời hạn hoạt động của dự án đầu tư trong khu kinh tế không quá 70 năm."


class EvidenceTest(unittest.TestCase):
    def test_whitespace_and_page_range(self):
        self.assertTrue(evidence_hit(CHUNK, [{"source_id": "doc", "page": 23, "evidence": QUOTE}]))
        self.assertTrue(evidence_hit(CHUNK, [{"source_id": "doc", "page": 24, "evidence": QUOTE}]))
        self.assertFalse(strict_starter_hit(CHUNK, [{"source_id": "doc", "page": 23, "evidence": QUOTE}]))

    def test_rejects_wrong_page_source_or_text(self):
        self.assertFalse(evidence_hit(CHUNK, [{"source_id": "doc", "page": 25, "evidence": QUOTE}]))
        self.assertFalse(evidence_hit(CHUNK, [{"source_id": "other", "page": 23, "evidence": QUOTE}]))
        self.assertFalse(evidence_hit(CHUNK, [{"source_id": "doc", "page": 23, "evidence": "không quá 50 năm"}]))

    def test_exact_span_keeps_line_breaks(self):
        span = exact_span(CHUNK["text"], QUOTE)
        self.assertIn("\n", span)
        self.assertIn(span, CHUNK["text"])
        self.assertTrue(strict_starter_hit({**CHUNK}, [{"source_id": "doc", "page": 23, "evidence": span}]))


if __name__ == "__main__":
    unittest.main()
