# Other reported and observed anomalies, March–July 2026

> This appendix records other file, Library, retrieval, rendering, identity, connector and execution anomalies observed by the author or reported publicly during the preceding months. Most are incomplete, sporadic or weakly instrumented. These records preserve the wider observation field and its limits; they do not establish that the incidents share one cause, nor that every report is accurate.

This is contextual material, not an extension of the controlled generated-ZIP conclusion. **Grade A** is a first-party public record; **Grade B** is a directly preserved or byte-verified local record with the stated ceiling; **Grade C** is an author observation preserved only in a limited record; and **Grade D** is a reviewed public user report. Public reports are anecdotal unless a row says otherwise. `External-only snapshot` means a dated private capture exists but is not republished here to avoid unnecessary replication of user content; see [the snapshot ledger](../evidence/public-records/OTHER_ANOMALIES_SNAPSHOT_LEDGER.csv).

## Officially acknowledged incidents

No collected status record publishes a root cause. The records establish the stated affected feature and timeline only.

| Date | Anomaly class | Symptom | Source class | Grade | Citation | Status | Relationship to generated-ZIP finding |
|---|---|---|---|---|---|---|---|
| 10–12 Mar 2026 | File transfers | OpenAI separately recorded increased ChatGPT download errors and upload errors during this window. | First-party status | A | [S0032 download](https://status.openai.com/incidents/01KKD07DNHFKAWK5JCAMAASYGZ); [S0033 upload](https://status.openai.com/incidents/01KKCT34VDK552CSMP286DS9HE) | confirmed event | related symptom only |
| 25 Mar 2026 | Project files | OpenAI recorded that Project files could not be downloaded or previewed. | First-party status | A | [S0036](https://status.openai.com/incidents/01KMH5C6HVAYJ9SS3REEAWXB6R) | confirmed event | possibly adjacent |
| 11 May 2026 | File uploads | OpenAI recorded elevated ChatGPT file-upload errors; the same notice also named Codex Cloud task creation. | First-party status | A | [S0035](https://status.openai.com/incidents/75mc9vgr) | confirmed event | related symptom only |
| 23 Jun 2026 | File transfers | OpenAI recorded a partial outage with elevated ChatGPT upload and download errors. | First-party status | A | [S0034](https://status.openai.com/incidents/01KVTDW6E1PXBTY2A9XEBT4MY4) | confirmed event | related symptom only |
| 13 Jul 2026, 09:11–14:35 UTC | Library | OpenAI recorded elevated errors uploading, deleting and navigating files in the ChatGPT Library. | First-party status | A | [S0003](https://status.openai.com/incidents/01KXDBYJ7BWBE2NRDAQTKPM5WK) | confirmed event | possibly adjacent |

## Andrew’s unresolved or partially evidenced observations

These rows preserve symptoms or limited documentary records. They do not identify an internal cache, database, index, storage layer, or execution mechanism.

| Period | Anomaly class | Symptom | Source class | Grade | Local evidence ID | Status | Relationship to generated-ZIP finding |
|---|---|---|---|---|---|---|---|
| Jul 2026 | Library/picker divergence | Two recorded direct comparisons show a generated ZIP visible through the recorded route but unavailable through the explicit picker while the uploaded control worked. | Operator test record | B | E0049 | directly observed | related symptom only |
| Jul 2026 | Exact-target retrieval | Recorded assistant-side audits describe exact-looking search results that did not resolve the requested object and could instead surface neighbours. | Operator composite record | C | E0039; E0049 | partially evidenced | related symptom only |
| Mar–Jul 2026 | Displayed identity | Same displayed filenames were recorded with different downstream reachability; object identity was not independently established. | Operator composite record | C | E0039 | partially evidenced | related symptom only |
| Jul 2026 | EPUB | One recovered German EPUB is locally valid; its Library, picker and materialisation behaviour remains unestablished. | Local binary recovery | B | E0041 | directly observed | unknown |
| Mar–Jul 2026 | Image retrieval/opening | The author record describes textual search or representation succeeding while repeated image opening or byte retrieval did not; original image-route receipts are incomplete. | Operator composite record | C | E0039 | partially evidenced | unknown |
| Mar–Jul 2026 | PDF representation | The author record describes rendered PDF pages and extracted text or image content differing; it does not establish corruption or a product extraction defect. | Operator composite record | C | E0039 | partially evidenced | unknown |
| Mar–Jul 2026 | Spreadsheet content | The author record describes summaries or exports with unsupported or incomplete content; source/output pairs are not sufficient for a product-defect finding. | Operator composite record | C | E0039 | partially evidenced | unknown |
| Mar–Jul 2026 | CSV structure | The author record describes a header-only or structurally deficient generated CSV output; the preserved record does not establish a general export failure. | Operator composite record | C | E0039 | partially evidenced | unknown |
| Jul 2026 | Connector surface | A preserved image shows File Library search narration followed by a Reconnect Gmail card; it does not show Gmail being searched, read or invoked. | Local PDF visual forensics | B | E0042; SS-PUB-001 | directly observed | no demonstrated connection |
| Jul 2026 | Progress/blocker narration | A preserved image sequence shows progress-like language followed by repeated Library retrieval errors and an unfinished chapter; hidden execution is not established. | Local PDF visual forensics | B | E0042; SS-PUB-002 | directly observed | no demonstrated connection |
| Mar–Jul 2026 | Resume state | The author record describes resumed work retaining narrative context without retained physical artifacts; exact interruption traces remain incomplete. | Operator composite record | C | E0039 | partially evidenced | no demonstrated connection |
| Mar–Jul 2026 | Authority substitution | The author record describes reconstructed or metadata-level substitutes when authoritative bytes were unavailable; they are not treated as the original files. | Operator composite record | C | E0039 | partially evidenced | related symptom only |
| Jul 2026 | Download versus reuse | Recorded generated files could be exposed for browser download but were not later reusable through the recorded downstream route. | Operator test record | B | E0049 | directly observed | related symptom only |
| Jul 2026 | Generated versus uploaded objects | An uploaded operational copy was usable in the recorded direct comparison where the generated object was not; the original-generated/uploaded byte identity remains limited by provenance. | Operator test record | B | E0045; E0049 | directly observed | related symptom only |

## Public reports from other users

Each row is a reviewed **anecdotal public report**. The original link is publication-safe; a dated capture was made on 16 July 2026 where the source reference says `snapshot external-only`. The cited report establishes that the user made the report, not that the reported mechanism or product defect is confirmed.

| Date | Anomaly class | Symptom | Source class | Grade | Citation and snapshot state | Status | Relationship to generated-ZIP finding |
|---|---|---|---|---|---|---|---|
| 29 May 2026 | Library visibility | A user reported older uploads and images missing from Library while an export retained older items; another user did not reproduce it. | Community user report | D | [S0010](https://community.openai.com/t/storage-management-library-does-not-list-older-uploaded-files-and-images/1381990); snapshot external-only | anecdotal public report | possibly adjacent |
| 8 Jun 2026 | Library deletion | A user reported a delete confirmation with no effect and a user-supplied 404 observation across two browsers. | Community user report | D | [S0011](https://community.openai.com/t/uploaded-files-cannot-be-deleted-deletion-confirmation-has-no-effect/1383022); snapshot external-only | anecdotal public report | possibly adjacent |
| 9 Jul 2026 | Picker/navigation | A user requested Library browsing while attaching a file; current documentation later describes an Add-from-library flow, so availability or rollout at the report date is unresolved. | Community user report | D | [S0012](https://community.openai.com/t/feature-request-browse-file-library-when-attaching-files/1386122); snapshot external-only | contradicted or mismatched | related symptom only |
| 9 Jun 2026 | ZIP download | A user reported incomplete data-export ZIP downloads with differing byte counts and extraction errors. | Community user report | D | [S0013](https://community.openai.com/t/chatgpt-data-export-zip-downloads-are-incomplete-corrupted-and-cannot-be-extracted/1383110); snapshot external-only | anecdotal public report | related symptom only |
| 11 Mar 2026 | Generated artifact download | Several participants reported generated ZIP or document download failures, with same-day recovery posts also present. | Community user report | D | [S0015](https://community.openai.com/t/chatgpt-cannot-download-generated-zip-artifacts-mnt-data-download-failure/1376287); snapshot external-only | anecdotal public report | related symptom only |
| Jan 2026 | Agent persistence | One user reported inaccessible Knowledge alongside Updates Pending that did not persist; a same-author cross-post was omitted as duplicate. | Community user report | D | [S0037](https://community.openai.com/t/gpt-agent-cant-access-my-uploaded-files-updates-pending-stuck/1372846); snapshot external-only | anecdotal public report | no demonstrated connection |
| Jul 2026 | Visible source versus readable content | A user reported Project filenames visible while content could not be read; the assistant-authored diagnosis in the post is excluded. | Reddit user report | D | [S0024](https://www.reddit.com/r/ChatGPT/comments/1ukiz8y/projects_are_not_reading_source_files/); external-only | anecdotal public report | possibly adjacent |
| Jan 2026 | Mobile file reference | An Apps SDK issue reported mobile uploads reaching an MCP tool as incomplete references while web sent file objects; there is no maintainer confirmation. | GitHub user issue | D | [S0026](https://github.com/openai/openai-apps-sdk-examples/issues/185); snapshot external-only | anecdotal public report | no demonstrated connection |
| Apr 2024 | Wrong-object retrieval | An Assistant API issue reported inaccessible or incorrect uploaded-file access; comments describe several configuration and upload alternatives. | GitHub user issue | D | [S0027](https://github.com/openai/openai-openapi/issues/222); snapshot external-only | anecdotal public report | related symptom only |
| Jun 2026 | Downloadable but absent from Library | Users reported files or images downloadable from a conversation but not saved to Library; a Project-path distinction was suggested by one commenter. | Reddit user report | D | [S0028](https://www.reddit.com/r/ChatGPT/comments/1ue00oi/anyone_else_having_issues_with_files_not_saving/); external-only | anecdotal public report | related symptom only |
| Apr 2025 | Image opening | A user reported a generated PNG that downloaded but would not open in two desktop applications; no bytes were provided. | Reddit user report | D | [S0031](https://www.reddit.com/r/ChatGPT/comments/1js8r4f/); external-only | anecdotal public report | unknown |
| Jan/Jun 2025 | Spreadsheet handling | Separate users reported incorrect spreadsheet values or CSV/XLSX visualization/export errors, without input/output fixtures. | Reddit user reports | D | [S0039](https://www.reddit.com/r/ChatGPT/comments/1ie8jo9/); [S0040](https://www.reddit.com/r/ChatGPT/comments/1l43ox8/); external-only | anecdotal public report | unknown |
| Jun 2026 | PDF extraction/content | A user reported unsupported accounting numbers from a mixed text-and-image PDF; no source PDF or result was supplied. | Reddit user report | D | [S0041](https://www.reddit.com/r/ChatGPT/comments/1ufzn1g/how_to_upload_large_size_files_into_chatgpt_and/); external-only | anecdotal public report | unknown |

### Excluded or mismatched leads

Microsoft VS Code issue 323945 is excluded as support for artifact-progress behaviour: it concerns cache misses and AI-credit charges, not narration outrunning file inspection or execution. This is a source mismatch, not evidence against other progress reports.

## Conclusion

These records do not prove one defect or one architecture. They are not aggregated as evidence of prevalence, severity or a common cause. During the same period, users and OpenAI’s own status records described failures across several neighbouring file and execution surfaces. The main report rests on its controlled evidence; this appendix preserves the wider observation field and its limits.
