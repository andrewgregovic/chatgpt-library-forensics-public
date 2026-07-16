# Executive summary

## Finding

Generated-ZIP downstream reuse failure was repeatedly observed in one account from 10–16 July 2026 across the recorded Library, picker, and assistant-side routes.

The published record contains:

- two recorded direct picker comparisons in which the generated ZIP failed and the uploaded control worked;
- nine recorded assistant-side exact-target audits that did not resolve an independently usable generated ZIP;
- no identified success among the eleven recorded targets;
- a byte-verified 133-byte controlled ZIP whose current bytes match the prior recorded uploaded-copy hash.

The correct scope is deliberately narrow. The record supports a repeated pattern in the submitted account history. It does not establish a universal defect, user prevalence, a current release-wide rate, or an internal cause.

## What the controlled specimen changes

The specimen is a valid one-member ZIP containing payload.txt with the 11-byte payload probe alpha. Its current size, archive structure, payload, and SHA-256 are independently verified. This removes several simple explanations for the recorded difference between the generated and uploaded routes: malformed current bytes, archive complexity, archive size, and a different payload.

It does not independently close the historical chain of custody. The browser-download origin is first-party attestation; the separately preserved uploaded object bytes, object IDs, browser history, Finder metadata, and original hash-computation receipt are unavailable.

## Broader descriptive model

The record supports representation-state divergence: a filename, Library row, picker selection, semantic search result, parsed representation, attachment, runtime-local path, browser download, and current local bytes are distinct observations. A success or failure at one state cannot safely be substituted for another.

## Counterevidence and alternatives

The repository preserves reasons not to overstate the result:

- the eleven rows are heterogeneous (two direct comparisons and nine lower-tier assistant-side audits);
- one test filename does not exactly join the historical inventory;
- the primary source for the nine-target audit is not included;
- the 31-row inventory contains sequential release families rather than independent experimental conditions;
- public records confirm discrete file incidents and current documented behavior, but do not identify a root cause;
- some reports are compatible with rollout, navigation, transient incident, configuration, or plan/path differences.

## Why screenshots are included

The redacted exhibits document two process-level observations:

1. an unverified contemporaneous hypothesis that a request-level health view can conceal a failing Library dependency; and
2. an attempted retry-and-pause restraint mechanism that the system followed only approximately.

Neither screenshot proves OpenAI’s monitoring architecture, actual Gmail invocation, or a specific internal service topology.
