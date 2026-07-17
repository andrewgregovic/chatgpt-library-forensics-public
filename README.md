# ChatGPT Library Forensics

Generated-ZIP downstream reuse failure was repeatedly observed for one ChatGPT account between 10 and 16 July 2026 through the recorded Library, picker and assistant-side routes. This repository preserves the evidence used to reach that scoped conclusion. It does not establish prevalence across users or identify OpenAI’s internal mechanism.

This is a curated public export from a larger private evidence vault. It contains the publication-safe material available to inspect the findings, their derivation and their stated limitations: one byte-verified controlled ZIP, redacted documentary screenshots, concise public-record metadata, evidence tables, contradiction records, and deterministic validators. It is not a mirror of the private research workspace.

## Core result

The strongest supported statement is:

> Two recorded direct generated-ZIP picker comparisons failed while uploaded controls worked; nine recorded assistant-side exact-target audits failed to resolve an independently usable generated ZIP; no success was identified among those eleven recorded targets.

This is an account-, period-, and route-scoped record. It is not a population estimate, a universal failure rate, or a diagnosis of a particular OpenAI service.

## Representation-state divergence

The investigation uses the following terms separately:

| Observable state | Meaning | Does not establish |
|---|---|---|
| Displayed filename | A name is shown in a UI or narrative. | Object identity or byte identity. |
| Library row | The object is visible in the Library. | Picker eligibility, attachment, or materialisation. |
| Explicit picker eligibility | The object can be selected through the composer picker. | Successful attachment or runtime use. |
| Semantic search result | A search returns a row, reference, or related result. | Exact target resolution or object identity. |
| Parsed representation | A tool exposes text, metadata, or a derivative. | The original bytes or every downstream route. |
| Attached object | An object is attached to a request. | Runtime-local availability or correct byte identity. |
| Current retrievable bytes | Current local bytes can be opened and hashed. | Historical origin, Library enrollment, or product-wide behavior. |
| Runtime-local materialisation | A runtime path is available for a task. | Durable Library persistence or later reuse. |

The evidence supports divergence between these states. It does not demonstrate a single common cause across Library, image, PDF, spreadsheet, connector, or progress anomalies.

## Contents

- EXECUTIVE_SUMMARY.md — concise results and evidentiary ceilings.
- METHODOLOGY.md — source, provenance, and validation rules.
- TIMELINE.md — incident and evidence chronology.
- ARTICLE_EVIDENCE_GATE_A_FILENAME_IS_NOT_A_FILE_v0.5.md — article-specific pointer and publication-readiness gate.
- KNOWN_LIMITATIONS.md — what remains unproven.
- evidence/ — the controlled specimen, redacted screenshots, public-record metadata, and tables.
- analysis/ — claims, contradictions, hypothesis statuses, ZIP findings, and state model.
- appendices/OTHER_REPORTED_ANOMALIES_MARCH_JULY_2026.md — a lower-confidence contextual record of separately reported and observed anomalies. It is not evidence for a common cause and does not alter the controlled generated-ZIP finding.
- scripts/ — dependency-free Python validators.

## Other reported anomalies

[Other reported and observed anomalies, March–July 2026](appendices/OTHER_REPORTED_ANOMALIES_MARCH_JULY_2026.md) is a compact contextual appendix. Its author observations have retained local-evidence ceilings, and every other-user report is anecdotal; it is lower-confidence than the controlled generated-ZIP evidence and makes no common-cause claim. The accompanying [CSV index](appendices/OTHER_REPORTED_ANOMALIES_INDEX.csv) and [snapshot ledger](evidence/public-records/OTHER_ANOMALIES_SNAPSHOT_LEDGER.csv) identify source status and external-only captures.

## Important limits

- “0/11” means eleven submitted recorded targets, not a measured population rate.
- The eleven rows comprise two direct picker comparisons and nine assistant-side resolution audits; the two direct comparisons recorded uploaded controls passing.
- The 31-row historical inventory is a retrospective first-party cohort, not 31 independent test conditions.
- The controlled ZIP excludes simple size, archive-structure, payload difference, and current-byte-corruption explanations for that specimen. It does not expose an internal mechanism.
- Rename-and-reupload created an operational replacement object in the recorded specimens; it did not prove repair of the original object.
- A visible Gmail reconnect surface is not evidence that Gmail was searched, read, drafted, or invoked.
- A route failure does not establish that a Library-visible object lacked bytes through every possible route.

## Verification

Run from the repository root:

    python3 scripts/verify_hashes.py
    python3 scripts/validate_controlled_specimens.py
    python3 scripts/validate_publication_safety.py

All three scripts use only the Python standard library and exit non-zero on an integrity, safety, pointer, or controlled-payload mismatch.

## Licence and third-party material

Andrew Gregovic’s original publication material is licensed under CC BY 2.0; see LICENSE.md. Third-party material is not relicensed; see THIRD_PARTY_MATERIALS.md.
