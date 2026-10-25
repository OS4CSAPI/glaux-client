# Glaux Client selection and experimental architecture baseline

Recorded 24 October 2026. This evidence record supports the Smart Citizen study's description of the experimental client. It distinguishes recovered architecture decisions, current repository facts, and deployed behavior from capabilities that remain proposed.

## Application identity and purpose

`OS4CSAPI/glaux-client` is a standalone TypeScript/Vite browser application created as an experimental client for evaluating generic standards access, bounded MERLIN/MPSS interpretation, and operator-facing Resource Details behavior. It is not a GitHub fork of DGIWG-P507/glaux, CSAPI Explorer, Alephex, or the client library. The Glaux name records project relationship and possible future contribution without implying adoption or endorsement.

## Selection rationale

The recovered 23 October architecture review compared a CSAPI Explorer fork with smaller applications built on `OS4CSAPI/ogc-client-CSAPI_2` and `cs-client-ts`. Explorer was convenient but added application behaviors such as discovery fallbacks and proxy-relative URL substitutions that would make experimental attribution less clean. The `cs-client-ts` alternative offered substantial SDK conveniences, but its normalized common model would add another interpretation layer while MERLIN's own interpretation is being evaluated. The control-first recommendation therefore selected a standalone application using the ogc-client CSAPI fork, while retaining other clients as external inspection/comparison tools rather than experimental foundations.

The experiment-specific reason for this choice is observability: the project can retain the chain from server response, to parser output, to profile interpretation, to operator presentation. This is not a general ranking of CSAPI SDK quality. A later dependency change remains acceptable if it preserves the same evidence and interpretation boundary.

## Pinned standards-access dependency

| Item | Recorded value |
| --- | --- |
| Repository | `OS4CSAPI/ogc-client-CSAPI_2` |
| Upstream lineage | fork of `camptocamp/ogc-client` |
| Selected branch | `phase-10` |
| Exact commit | `4ca1d7db9b1ccdf545adbef42ef941139fe11977` |
| Package identity | `@camptocamp/ogc-client`, `1.3.1-dev` |
| Used export | `@camptocamp/ogc-client/csapi` |
| License | BSD-3-Clause, Camptocamp copyright 2023 |

The dependency is held as a commit-pinned Git submodule and is built from its own lockfile. The application does not silently substitute the npm release for this CSAPI revision. `Docs/DEPENDENCIES.md` is the maintained dependency provenance record.

## Application architecture

- `src/data`: read-only retrieval, independent original-response capture, pinned-library parsing, and generic extraction.
- `src/profile`: bounded interpretation of explicitly supported DIM/MPSS meanings; no generalized ontology engine.
- `src/presentation`: Standard View, Operator View, Resource Details navigation, source disclosures, and raw inspection.

Standard View and Operator View operate on the same captured source information. Unsupported and ambiguous content remains inspectable rather than being hidden to improve the apparent profile-aware result. This boundary is a deliberate experimental control.

## Current public deployment

| Item | Recorded value |
| --- | --- |
| Cloudflare project | `glaux-client` |
| Public URL | `https://glaux-client.pages.dev/` |
| Deployment method | Cloudflare Pages Direct Upload |
| Source branch metadata | `work/details-view-20261023` |
| Deployed application commit | `71297c971e2e7532f7c7139600f41e9b58bdcc22` |
| Deployment ID | `97c801c4-c44f-4484-a175-e6651639fe07` |
| Default Resource Details review frame | 560 × 440 CSS pixels |

The deployed runtime predates this v0.5 paper revision. Documentation commits do not change the public application unless a new build is explicitly uploaded to Pages.

## Current remote-read boundary

The deployed client can accept a direct System resource URL, issue a credential-free GET, preserve received bodies, and follow at most one advertised typed SensorML `alternate` or `describedby` link. It does not yet provide authenticated service access, general collection discovery, or traversal of the full connected resource graph required by the Smart Citizen experiment. Existing synthetic bundles therefore demonstrate bounded interpretation but not the planned live Smart Citizen graph retrieval.

## Smart Citizen client increment still required

The study requires Glaux to retrieve the System description and the connected resources that carry the mapped Smart Citizen information through the selected CSAPI server. That increment must retain original responses, keep generic inspection competent, and add only the bounded interpretation needed by the reviewed mappings. A run record must identify the Glaux source commit, deployed runtime, pinned library commit, server revision, adapter revision, Smart Citizen capture, and MPSS profile revision.

## Evidence sources and limits

- `README.md` records the application purpose, current code boundaries, remote-read behavior, and public deployment link.
- `Docs/DEPENDENCIES.md` records the exact library revision, build arrangement, license, and update procedure.
- `Docs/Plans/CLOUDFLARE_DEPLOYMENT.md` records the public deployment identity and verification.
- The recovered project record dated 23 October 2026 preserves the earlier Explorer / ogc-client / cs-client-ts comparison and the decision to create a standalone `OS4CSAPI/glaux-client` application.

This record does not claim that the current client has completed the Smart Citizen traversal, measured operator benefit, or implemented the whole MPSS profile. Those remain experimental results to be produced.