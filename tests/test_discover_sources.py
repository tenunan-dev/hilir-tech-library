"""Offline tests for tools/discover_sources.py channel-1 mining."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import discover_sources as ds  # noqa: E402


class TestExtract(unittest.TestCase):
    def test_url_extraction_stops_at_punctuation(self):
        text = "See https://example.com/report and (https://other.org/page?a=1)."
        urls = ds.extract_urls(text)
        self.assertIn("https://example.com/report", urls)
        self.assertIn("https://other.org/page?a=1", urls)

    def test_phrase_extraction_from_hint_lines(self):
        line = "where: [{\"hint\": \"Hydraulic Institute and OEM catalogues for pump curves (open)\"}]"
        phrases = ds.extract_phrases(line)
        self.assertIn("Hydraulic Institute", phrases)
        # phrases are capital-word sequences; 3-letter acronyms are filtered by length
        self.assertNotIn("OEM catalogues", phrases)

    def test_prose_lines_are_ignored(self):
        phrases = ds.extract_phrases("The pump converts electric power into flow.")
        self.assertEqual(phrases, set())

    def test_noise_phrases_dropped(self):
        line = "hint: Web-checked 2026-10-28; Open process descriptions only"
        phrases = ds.extract_phrases(line)
        self.assertNotIn("Open process", phrases)
        self.assertNotIn("Web", phrases)

    def test_known_phrase_matching(self):
        names = {"hydraulic institute", "enyne"}
        self.assertTrue(ds.known_phrase("Hydraulic Institute", names))
        self.assertTrue(ds.known_phrase("Enyne press releases", names))
        self.assertFalse(ds.known_phrase("CanmetENERGY", names))

    def test_domain_matching(self):
        self.assertEqual(ds._domain("https://www.example.com/a"), "example.com")
        self.assertIsNone(ds._domain("not a url"))


if __name__ == "__main__":
    unittest.main()
