#!/usr/bin/env python3
"""Validate the exact controlled ZIP specimen with the Python standard library."""

from __future__ import annotations

import hashlib
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPECIMEN = ROOT / "evidence/controlled-specimens/library_resolver_probe_20260716T094002_864448_SGT.zip"
EXPECTED_SIZE = 133
EXPECTED_SHA256 = "5fab734dd83922a63bfbb1f4ce3e68b7a3d222ffaf6b039b49ea5a2e5137d046"
EXPECTED_MEMBER = "payload.txt"
EXPECTED_PAYLOAD = b"probe alpha"
EXPECTED_PAYLOAD_SHA256 = "40acdd19031d10d451f9e1f5695f8c9d575dda5b45fdba19a1865752ac05bddb"


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def main() -> int:
    if not SPECIMEN.is_file():
        print(f"FAIL missing specimen: {SPECIMEN.relative_to(ROOT)}", file=sys.stderr)
        return 1
    data = SPECIMEN.read_bytes()
    checks = {
        "size": len(data) == EXPECTED_SIZE,
        "sha256": sha256_bytes(data) == EXPECTED_SHA256,
    }
    try:
        with zipfile.ZipFile(SPECIMEN) as archive:
            bad_member = archive.testzip()
            members = archive.infolist()
            checks["zip_integrity"] = bad_member is None
            checks["member_count"] = len(members) == 1
            checks["member_name"] = len(members) == 1 and members[0].filename == EXPECTED_MEMBER
            payload = archive.read(EXPECTED_MEMBER)
            checks["payload_size"] = len(payload) == 11
            checks["payload"] = payload == EXPECTED_PAYLOAD
            checks["payload_sha256"] = sha256_bytes(payload) == EXPECTED_PAYLOAD_SHA256
    except (OSError, KeyError, zipfile.BadZipFile) as error:
        print(f"FAIL zip parse: {error}", file=sys.stderr)
        return 1

    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        print("FAIL " + ", ".join(failed), file=sys.stderr)
        return 1
    print("PASS controlled ZIP: 133 bytes, one payload.txt member, payload probe alpha")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
