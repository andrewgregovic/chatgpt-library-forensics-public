#!/usr/bin/env python3
"""Verify every public file recorded in SHA256SUMS.txt.

The checksum file intentionally excludes itself because a file cannot contain
its own stable checksum. The script rejects every other unrecorded regular file.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "SHA256SUMS.txt"
SELF_EXCLUDED = {"SHA256SUMS.txt"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_manifest() -> dict[str, str]:
    entries: dict[str, str] = {}
    for number, raw in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), 1):
        if not raw or raw.startswith("#"):
            continue
        try:
            digest, relative = raw.split("  ", 1)
        except ValueError as error:
            raise ValueError(f"line {number}: expected SHA-256 then two spaces then path") from error
        if len(digest) != 64 or any(char not in "0123456789abcdef" for char in digest):
            raise ValueError(f"line {number}: invalid SHA-256")
        if relative in entries or relative in SELF_EXCLUDED:
            raise ValueError(f"line {number}: duplicate or self-excluded path {relative!r}")
        candidate = Path(relative)
        if candidate.is_absolute() or ".." in candidate.parts:
            raise ValueError(f"line {number}: unsafe path {relative!r}")
        entries[relative] = digest
    return entries


def public_files() -> set[str]:
    results: set[str] = set()
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative not in SELF_EXCLUDED:
            results.add(relative)
    return results


def main() -> int:
    try:
        expected = load_manifest()
    except (OSError, ValueError) as error:
        print(f"FAIL manifest: {error}", file=sys.stderr)
        return 2

    actual = public_files()
    failures = 0
    for relative in sorted(set(expected) - actual):
        print(f"MISSING {relative}")
        failures += 1
    for relative in sorted(actual - set(expected)):
        print(f"EXTRA {relative}")
        failures += 1
    for relative in sorted(set(expected) & actual):
        observed = sha256(ROOT / relative)
        if observed != expected[relative]:
            print(f"MISMATCH {relative} expected={expected[relative]} observed={observed}")
            failures += 1

    if failures:
        print(f"FAIL {failures} integrity problem(s)", file=sys.stderr)
        return 1
    print(f"PASS {len(expected)} public files verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
