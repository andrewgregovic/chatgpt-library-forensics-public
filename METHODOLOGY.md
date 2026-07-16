# Methodology

## Evidence classes and ceilings

Each claim is constrained by the most direct evidence actually present.

| Class | What it can establish | Key ceiling |
|---|---|---|
| First-party public record | The published incident or documentation statement. | Not an undisclosed root cause or all-account behavior. |
| Current binary specimen | Present bytes, size, structure, hash, and parse result. | Not historical origin or product-object identity without provenance. |
| Operator-submitted direct record | The recorded observation and exact stated values. | Underlying screenshots, object IDs, and tool traces may still be absent. |
| Retrospective cohort | The submitted inventory and recorded outcomes. | Not independent event receipts or a population denominator. |
| Redacted screenshot derivative | The visible content of the derivative and its documented source hash. | Not hidden tool state, internal architecture, or actions absent from the image. |
| Derived analysis | Recomputed accounting and interpretation. | Cannot independently establish a factual event. |

## Intake and validation

The private research process preserved raw submission bytes, recomputed sizes and SHA-256 values, checked ZIP safety and member hashes, parsed structured records, deduplicated copied or nested material, and recorded counterevidence and claim ceilings. This public export retains only the publication-safe result of that work.

The controlled ZIP is revalidated by scripts/validate_controlled_specimens.py. scripts/verify_hashes.py verifies each public file listed in SHA256SUMS.txt, rejects missing or extra files, and reports mismatches non-zero.

## Source selection

Public-source metadata is limited to directly relevant first-party OpenAI documentation and status records. The repository records URLs, titles, access dates, concise observations, and limitations rather than mirroring third-party webpages. Community and social reports are not treated as independent proof of a mechanism.

## Screenshot treatment

The original screenshots are withheld. Public derivatives use deterministic crop/redaction only, have metadata stripped, retain aspect ratio, and have separate hashes. The redaction log records all alterations. Transcript markers are explicit; redaction does not imply words were absent from the originals.

## Interpretation rules

- Gemini reports were discovery aids, not factual authority.
- Repetition is not independence.
- A proposed or narrated action is not an executed test.
- A current valid binary is not proof of its historical product route.
- Search or picker failure is not proof of universal byte absence.
- Similar symptoms are not a common-cause finding.
