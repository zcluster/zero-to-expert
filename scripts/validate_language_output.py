#!/usr/bin/env python3
"""Validate English or Simplified-Chinese language conformance in an HTML atlas."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys


CJK_RE = re.compile(r"[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]")
LATIN_RE = re.compile(r"[A-Za-z]")


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.skip_depth = 0
        self.lang = ""
        self.parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "html":
            self.lang = dict(attrs).get("lang") or ""
        if tag in {"script", "style", "noscript", "template"}:
            self.skip_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "template"} and self.skip_depth:
            self.skip_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)


def analyze(path: Path, expected: str) -> dict[str, object]:
    parser = VisibleTextParser()
    parser.feed(path.read_text(encoding="utf-8"))
    visible = " ".join(parser.parts)
    cjk = len(CJK_RE.findall(visible))
    latin = len(LATIN_RE.findall(visible))
    letters = cjk + latin
    cjk_ratio = cjk / letters if letters else 0.0

    failures: list[str] = []
    if len(re.sub(r"\s+", "", visible)) < 40:
        failures.append("too little reader-visible text to validate")

    normalized_lang = parser.lang.lower()
    if expected == "en":
        if not normalized_lang.startswith("en"):
            failures.append(f'html lang must start with "en", found {parser.lang!r}')
        if cjk_ratio > 0.08:
            failures.append(
                f"visible CJK ratio {cjk_ratio:.3f} exceeds English limit 0.080"
            )
    else:
        if not normalized_lang.startswith("zh"):
            failures.append(f'html lang must start with "zh", found {parser.lang!r}')
        if cjk_ratio < 0.35:
            failures.append(
                f"visible CJK ratio {cjk_ratio:.3f} is below Chinese minimum 0.350"
            )

    return {
        "file": str(path),
        "expected": expected,
        "html_lang": parser.lang,
        "cjk_characters": cjk,
        "latin_letters": latin,
        "cjk_ratio": round(cjk_ratio, 4),
        "status": "pass" if not failures else "fail",
        "failures": failures,
    }


def main() -> int:
    argument_parser = argparse.ArgumentParser(
        description="Check visible HTML text against a frozen English or Chinese language."
    )
    argument_parser.add_argument("html_file", type=Path)
    argument_parser.add_argument(
        "--expected", required=True, choices=("en", "zh-CN"), help="Frozen content language"
    )
    args = argument_parser.parse_args()

    if not args.html_file.is_file():
        argument_parser.error(f"HTML file not found: {args.html_file}")

    result = analyze(args.html_file, args.expected)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
