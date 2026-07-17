#!/usr/bin/env python3
"""Validate publication-safety and article-evidence-gate constraints."""

from __future__ import annotations

import csv
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GATE = ROOT / "ARTICLE_EVIDENCE_GATE_A_FILENAME_IS_NOT_A_FILE_v0.5.md"
FORBIDDEN_TEXT = (
    "/Users" + "/agre",
    "file" + "://",
    "vscode" + "://",
    "bearer" + " ",
    "authorization" + ":",
    "gh" + "p_",
    "github" + "_pat_",
    "X-Amz-" + "Signature=",
    "session" + "_token=",
    "Cookie" + ":",
)
UNSUPPORTED_IMAGE_TIME = "01:25" + ":53"


def fail(message: str) -> None:
    print(f"FAIL {message}", file=sys.stderr)


def public_files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts
    )


def validate_no_symlinks() -> int:
    bad = [path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*") if path.is_symlink()]
    if bad:
        fail("symlink(s): " + ", ".join(bad))
        return 1
    return 0


def validate_text_safety() -> int:
    failures = 0
    for path in public_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        lowered = text.lower()
        for forbidden in FORBIDDEN_TEXT:
            if forbidden.lower() in lowered:
                fail(f"forbidden text {forbidden!r} in {path.relative_to(ROOT)}")
                failures += 1
        if UNSUPPORTED_IMAGE_TIME in text:
            fail(f"unsupported image-event time in {path.relative_to(ROOT)}")
            failures += 1
    return failures


def validate_gate_pointers() -> int:
    text = GATE.read_text(encoding="utf-8")
    failures = 0
    statuses = re.findall(r"^\|[^\n]*\| (PASS(?:_WITH_PROVENANCE_CEILING)?) \|", text, re.MULTILINE)
    if not statuses:
        fail("article evidence gate has no PASS rows")
        return 1
    for line in text.splitlines():
        if not line.startswith("|") or "| PASS" not in line:
            continue
        match = re.search(r"\]\(([^)]+)\)", line)
        if not match:
            fail("PASS row without a public path")
            failures += 1
            continue
        pointer = Path(match.group(1))
        if pointer.is_absolute() or ".." in pointer.parts or not (ROOT / pointer).is_file():
            fail(f"unresolved PASS pointer {match.group(1)!r}")
            failures += 1
    if "The article is **not publication-ready**" not in text:
        fail("article gate does not block promotion with unresolved critical exhibits")
        failures += 1
    return failures


def validate_publication_manifest() -> int:
    manifest = ROOT / "PUBLICATION_MANIFEST.csv"
    failures = 0
    with manifest.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            public_name = row["public_filename"].strip()
            if public_name and not (ROOT / public_name).is_file():
                fail(f"publication manifest points to missing file {public_name!r}")
                failures += 1
    return failures


def validate_clock_conversion() -> int:
    pairs = (
        ("2026-07-13T09:11:53Z", "2026-07-13 17:11:53 SGT"),
        ("2026-07-13T14:35:47Z", "2026-07-13 22:35:47 SGT"),
    )
    timeline = (ROOT / "TIMELINE.md").read_text(encoding="utf-8")
    failures = 0
    for raw_utc, expected_sgt in pairs:
        converted = (
            datetime.fromisoformat(raw_utc.replace("Z", "+00:00"))
            .astimezone(timezone.utc)
            .astimezone(timezone(offset=timedelta(hours=8)))
            .strftime("%Y-%m-%d %H:%M:%S SGT")
        )
        if converted != expected_sgt or raw_utc not in timeline or expected_sgt not in timeline:
            fail(f"UTC-to-SGT conversion mismatch for {raw_utc}")
            failures += 1
    return failures


def main() -> int:
    failures = validate_no_symlinks()
    failures += validate_text_safety()
    failures += validate_gate_pointers()
    failures += validate_publication_manifest()
    failures += validate_clock_conversion()
    if failures:
        return 1
    print("PASS publication safety, evidence-gate pointers, and UTC-to-SGT conversions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
