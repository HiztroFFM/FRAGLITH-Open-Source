#!/usr/bin/env python3
"""Classify CS2 log issues without echoing sensitive log contents.

This program does NOT anonymize or publish raw logs. It reports only category counts.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


RULES = (
    ("disk_space", ("not enough disk space", "failed to preallocate", "no space left on device")),
    ("plugin_dependencies", ("failed to locate managed application", "dependency resolution failed", "could not load plugin")),
    ("crash_signals", ("fatal error", "access violation", "segmentation fault", "unhandled exception")),
    ("world_position", ("outside of cell bounds", "m_vecorigin", "velocity too low")),
    ("animation_assets", ("missing animation", "animation graph", "bone mismatch", "skeleton mismatch")),
    ("asset_loading", ("failed to load", "file not found", "failed to find", "cannot find", ".vmdl", ".vpc", ".vanim")),
    ("other_errors", ("[error]", "[eror]", " error ", "exception")),
)


def classify(line: str) -> str | None:
    lower = line.lower()
    for category, needles in RULES:
        if any(needle in lower for needle in needles):
            return category
    return None


def summarize(lines) -> dict:
    counts: Counter[str] = Counter()
    total = 0
    matched = 0
    for line in lines:
        total += 1
        category = classify(line)
        if category is not None:
            counts[category] += 1
            matched += 1
    # No names, log lines, paths, user identifiers, credentials or hostnames retained.
    return {
        "format_version": 1,
        "total_lines": total,
        "categorized_lines": matched,
        "categories": dict(sorted(counts.items())),
        "note": "Heuristic counts only. Inspect raw logs locally. Do not publish unreviewed logs.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("log", type=Path, help="local CS2 text log, never uploaded by this tool")
    args = parser.parse_args()
    with args.log.open("r", encoding="utf-8", errors="replace") as stream:
        report = summarize(stream)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
