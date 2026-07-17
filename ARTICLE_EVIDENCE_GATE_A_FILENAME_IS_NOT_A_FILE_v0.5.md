# Article evidence gate: *A Filename Is Not a File* v0.5

Status is evaluated against this public repository only. `PASS` means the public pointer resolves to the stated evidence. `PASS_WITH_PROVENANCE_CEILING` means the published artifact resolves but its origin, chronology, or underlying primary record remains limited. `BLOCKED` means the article-critical referent is unpublished or not located.

| Claim | Direct evidence | Public path | Status | Ceiling |
|---|---|---|---|---|
| False Chapter 13 receipt | No publication-safe original screenshot or direct transcript is available in this repository. A recovered PDF-derived visual exists privately, but has not been published as the original event record. | — | BLOCKED | The article must not treat the receipt as independently publicly auditable until a primary exhibit or a publication-safe derivative with complete provenance is released. |
| 01:34 image-reconstruction admission | `BLOCKED: 2026-07-13 01:34:01 SGT image-reconstruction event — original direct transcript or screenshot not located.` | — | BLOCKED | The supplied lead is not republished as a verbatim transcript; the unsupported earlier draft time has been removed. |
| 06:50 Library search miss | `BLOCKED: 2026-07-13 06:50:11 SGT Library-search event — original direct transcript or screenshot not located.` | — | BLOCKED | The exact filename and quoted exchange are not published without the original direct record. The claimed lead over the status notice is therefore not publicly supported. |
| OpenAI 17:11 acknowledgement and 22:35 resolution | First-party OpenAI status record; raw UTC values retained in the public record metadata. | [evidence/public-records/OPENAI_FILE_RECORDS.csv](evidence/public-records/OPENAI_FILE_RECORDS.csv) | PASS | Confirms the published incident timeline only, not a root cause, internal detection time, or relationship to an account observation. |
| Two direct picker comparisons | Curated test stratification record. | [evidence/tables/GENERATED_ZIP_TEST_STRATIFICATION.csv](evidence/tables/GENERATED_ZIP_TEST_STRATIFICATION.csv) | PASS_WITH_PROVENANCE_CEILING | Current controlled-ZIP bytes are verified; picker screenshots, object IDs, and the uploaded comparison bytes are withheld or unavailable. |
| Nine assistant-side exact-target non-resolutions | Curated audit stratum. | [evidence/tables/GENERATED_ZIP_TEST_STRATIFICATION.csv](evidence/tables/GENERATED_ZIP_TEST_STRATIFICATION.csv) | PASS_WITH_PROVENANCE_CEILING | The primary nine-target audit source is not included; these are not direct picker comparisons. |
| Book Package A Library/picker comparison | No publication-safe original Library/picker exhibit identifying that comparison is available. | — | BLOCKED | The article-specific visual comparison remains unpublished; do not treat a generic picker table as its substitute. |
| 133-byte Probe ZIP | Current byte-verified controlled specimen. | [evidence/controlled-specimens/library_resolver_probe_20260716T094002_864448_SGT.zip](evidence/controlled-specimens/library_resolver_probe_20260716T094002_864448_SGT.zip) | PASS_WITH_PROVENANCE_CEILING | Present bytes, size, archive structure and payload are verified; claimed original browser-download route is first-party attestation. |
| Rename-and-reupload record | No publication-safe before/after rename receipt or picker exhibit is available. | — | BLOCKED | The public record supports an operational replacement outcome only at a general, derived level; it does not publish this article-specific sequence. |
| Early-diagnosis screenshot | Redacted contemporaneous screenshot derivative with source-original hash. | [evidence/screenshots/early_diagnosis_redacted.png](evidence/screenshots/early_diagnosis_redacted.png) | PASS_WITH_PROVENANCE_CEILING | Documents the visible exchange and caveat, not OpenAI architecture or the exact incident chronology. |
| Retry-loop screenshot | Redacted contemporaneous screenshot derivative with source-original hash. | [evidence/screenshots/Library_loop_redacted.png](evidence/screenshots/Library_loop_redacted.png) | PASS_WITH_PROVENANCE_CEILING | Documents visible narration and a twenty-second pause, not hidden execution or a one-minute pause. |

## Result

The article is **not publication-ready** against this gate. Five article-critical referents remain blocked: the false Chapter 13 receipt, the 01:34 image-reconstruction admission, the 06:50 Library search miss, the Book Package A comparison, and the rename-and-reupload sequence. The first three are especially material to the opening and timeline. No blocked item may be upgraded from a later draft, semantic search result, or reconstruction.

## Direct-evidence search record

For the two new candidate timeline events, the required local search covered original conversation-export candidates, the operator packages and extracted transcripts, recovered screenshots/PDFs, browser/saved-HTML candidates, and project handoffs. No original direct transcript, screenshot, exported HTML, or browser export was located for either event. The article draft was treated only as a lead and not as direct transcript evidence.

No public `evidence/timeline/` exhibit has been created. That absence is deliberate: fabricating a screenshot, using ellipsised wording as a transcript, or substituting a later derived record would defeat the purpose of this gate.
