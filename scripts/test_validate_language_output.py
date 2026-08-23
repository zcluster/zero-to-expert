#!/usr/bin/env python3
"""Unit tests for validate_language_output.py."""

from pathlib import Path
import tempfile
import unittest

from validate_language_output import analyze


class LanguageOutputValidationTests(unittest.TestCase):
    def analyze_html(self, html: str, expected: str) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "atlas.html"
            path.write_text(html, encoding="utf-8")
            return analyze(path, expected)

    def test_english_atlas_passes(self) -> None:
        body = " ".join(
            ["General intelligence requires transfer, adaptation, evidence, and reliability."]
            * 12
        )
        result = self.analyze_html(f'<html lang="en"><body>{body}</body></html>', "en")
        self.assertEqual(result["status"], "pass")

    def test_chinese_atlas_passes_with_english_terms(self) -> None:
        body = "通用人工智能需要迁移、适应、证据和可靠性。" * 24
        body += " Artificial general intelligence AGI benchmark."
        result = self.analyze_html(
            f'<html lang="zh-CN"><body>{body}</body></html>', "zh-CN"
        )
        self.assertEqual(result["status"], "pass")

    def test_chinese_body_fails_english_expectation(self) -> None:
        body = "这是一份关于通用人工智能、学习、推理、评测与部署的中文图谱。" * 20
        result = self.analyze_html(f'<html lang="en"><body>{body}</body></html>', "en")
        self.assertEqual(result["status"], "fail")

    def test_english_body_fails_chinese_expectation(self) -> None:
        body = " ".join(
            ["This atlas explains general intelligence with evidence and system maps."]
            * 15
        )
        result = self.analyze_html(
            f'<html lang="zh-CN"><body>{body}</body></html>', "zh-CN"
        )
        self.assertEqual(result["status"], "fail")

    def test_wrong_html_lang_fails(self) -> None:
        body = "通用人工智能需要迁移、适应、证据和可靠性。" * 24
        result = self.analyze_html(f'<html lang="en"><body>{body}</body></html>', "zh-CN")
        self.assertEqual(result["status"], "fail")


if __name__ == "__main__":
    unittest.main()
