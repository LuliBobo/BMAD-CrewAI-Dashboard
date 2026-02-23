#!/usr/bin/env python3
"""Spusti kalibracne testy routovania a vypise zhrnutie."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

import route_orchestrator


def load_cases(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def run(cases: List[Dict[str, str]]) -> Dict[str, Any]:
    total = len(cases)
    correct = 0
    mismatches = []

    for case in cases:
        prompt = case["prompt"]
        expected = case["expected_primary_agent"]
        result = route_orchestrator.build_result(prompt)
        actual = result["primary_agent"]
        if actual == expected:
            correct += 1
        else:
            mismatches.append(
                {
                    "prompt": prompt,
                    "expected": expected,
                    "actual": actual,
                    "matched_keywords": result.get("matched_keywords", []),
                    "confidence": result.get("confidence", "n/a"),
                }
            )

    accuracy = 0.0 if total == 0 else correct / total
    return {
        "total": total,
        "correct": correct,
        "accuracy_percent": round(accuracy * 100, 2),
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
    }


def main() -> int:
    default_cases = (
        Path(__file__).resolve().parent.parent
        / "references"
        / "routing-calibration-cases-sk.json"
    )
    parser = argparse.ArgumentParser(description="Spusti kalibraciu routovania.")
    parser.add_argument(
        "--cases",
        type=Path,
        default=default_cases,
        help="Cesta k JSON suboru s testovacimi pripadmi.",
    )
    args = parser.parse_args()

    cases = load_cases(args.cases)
    report = run(cases)
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
