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
ANOMALY_APPENDIX = ROOT / "appendices" / "OTHER_REPORTED_ANOMALIES_MARCH_JULY_2026.md"
DIRECT_ANOMALIES = ROOT / "appendices" / "anomalies" / "directly-observed"
ONLINE_ANOMALIES = ROOT / "appendices" / "anomalies" / "gathered-online"
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
    if "The article is **ready for promotion review with provenance ceilings**" not in text:
        fail("article gate does not state the required promotion-review disposition")
        failures += 1
    if "| BLOCKED |" in text:
        fail("article gate retains a blocked row after the authorized provenance-limited publication")
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
        ("2026-07-13T09:11:53.323Z", "2026-07-13 17:11:53 SGT"),
        ("2026-07-13T14:35:47.689Z", "2026-07-13 22:35:47 SGT"),
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


def read_index(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def validate_anomaly_provenance_split() -> int:
    failures = 0
    required = (
        DIRECT_ANOMALIES / "README.md",
        DIRECT_ANOMALIES / "OTHER_REPORTED_ANOMALIES_MARCH_JULY_2026.md",
        DIRECT_ANOMALIES / "OTHER_REPORTED_ANOMALIES_INDEX.csv",
        ONLINE_ANOMALIES / "README.md",
        ONLINE_ANOMALIES / "OTHER_REPORTED_ANOMALIES_MARCH_JULY_2026.md",
        ONLINE_ANOMALIES / "OTHER_REPORTED_ANOMALIES_INDEX.csv",
        ONLINE_ANOMALIES / "OTHER_ANOMALIES_SNAPSHOT_LEDGER.csv",
    )
    for path in required:
        if not path.is_file():
            fail(f"missing anomaly provenance file {path.relative_to(ROOT)}")
            failures += 1
    if failures:
        return failures

    direct_opening = (
        "These records concern anomalies directly observed in Andrew Gregovic’s own "
        "ChatGPT account and workflows. They vary in evidentiary strength and do not "
        "establish a common cause."
    )
    online_opening = (
        "These records were gathered from public online sources. Most are anecdotal "
        "and are preserved as reports of similar or neighbouring symptoms, not as proof "
        "of prevalence or common cause."
    )
    if direct_opening not in (DIRECT_ANOMALIES / "README.md").read_text(encoding="utf-8"):
        fail("directly-observed README opening text mismatch")
        failures += 1
    if online_opening not in (ONLINE_ANOMALIES / "README.md").read_text(encoding="utf-8"):
        fail("gathered-online README opening text mismatch")
        failures += 1

    direct_rows = read_index(DIRECT_ANOMALIES / "OTHER_REPORTED_ANOMALIES_INDEX.csv")
    online_rows = read_index(ONLINE_ANOMALIES / "OTHER_REPORTED_ANOMALIES_INDEX.csv")
    direct_ids = {row["item_id"] for row in direct_rows}
    online_ids = {row["item_id"] for row in online_rows}
    if not direct_rows or any(not item_id.startswith("AAR-") for item_id in direct_ids):
        fail("directly-observed index contains a non-AAR record or no records")
        failures += 1
    if not online_rows or any(not item_id.startswith("PAR-") for item_id in online_ids):
        fail("gathered-online index contains a non-PAR record or no records")
        failures += 1
    if direct_ids & online_ids:
        fail("anomaly provenance indexes duplicate record IDs")
        failures += 1

    appendix = ANOMALY_APPENDIX.read_text(encoding="utf-8")
    if appendix.count("## ") != 2 or "|" in appendix:
        fail("main anomaly appendix must contain only the two provenance links")
        failures += 1
    for link in ("anomalies/directly-observed/", "anomalies/gathered-online/"):
        if link not in appendix:
            fail(f"main anomaly appendix missing provenance link {link}")
            failures += 1
    return failures


def main() -> int:
    failures = validate_no_symlinks()
    failures += validate_text_safety()
    failures += validate_gate_pointers()
    failures += validate_publication_manifest()
    failures += validate_clock_conversion()
    failures += validate_anomaly_provenance_split()
    if failures:
        return 1
    print("PASS publication safety, evidence-gate pointers, and UTC-to-SGT conversions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
