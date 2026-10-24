# MERLIN DIM and MPSS continuity

Updated 24 October 2026.

**Publication checkpoint:** the catalogue contains 14 original project artifacts
totalling 27,555,946 bytes. All imported files match their recovered source bytes
and registered SHA-256 fingerprints. Catalogue and repository-local documentation
link verification passed on 24 October 2026. Git history records the publication
commit containing this checkpoint and the files it verifies.

## Purpose and authority

This Git-native checkpoint carries the broader Domain Information Models (DIM)
research and Managed Physical Sensing Systems (MPSS) work forward from
[PITON v4.6](Source_Continuity/PITON_MERLIN_MPSS_Integration_Continuity_v4.6_22OCT2026.docx)
and the
[Evidence-to-Design Update Plan v1.6](Source_Continuity/MERLIN_MPSS_Evidence_to_Design_Update_Plan_v1.6_22OCT2026.docx),
both dated 22 October 2026. It governs subsequent project status, artifact
locations, and immediate next-action sequencing. The original documents retain
their versions, dates, contents, and historical claims.

The objective remains a coherent, standards-grounded description of the whole
employed physical sensing system, covering the eight connected information
subjects. Glaux demonstrates selected parts of that work. Its present Overview,
Equipment, and Condition screens do not redefine the profile's overall scope.

Use the following records for their stated responsibilities:

| Record | Responsibility |
| --- | --- |
| [Documentation index](../README.md) | Entry point and routes to the maintained material. |
| [Artifact Register](../ARTIFACT_REGISTER.md) and [artifact manifest](../ARTIFACTS.json) | Canonical repository locations, stable artifact keys, source editions, and file fingerprints for the 14 current artifacts. |
| This continuity checkpoint | Broader research lineage, current decisions, and immediate work sequencing after the recovered PITON and plan. |
| [Current client work](CURRENT_WORK.md) | Implemented client behavior, actual checks, and the current implementation checkpoint. |
| [Deployment record](CLOUDFLARE_DEPLOYMENT.md) | The runtime revision actually uploaded and its live verification. |
| Original profile, catalogue, research, and Details View artifacts | The source content and decision standing of their identified editions. A summary or import does not change their meaning. |

## Retained source baselines

| Artifact family | Retained edition and standing |
| --- | --- |
| Main technical profile | [MPSS v0.3.5, 17 October 2026](../Design/MPSS/MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx), including the four recorded approved bounded increments. This remains a working technical draft with remaining design choices; repository publication does not make it an adopted external standard. |
| Connected example and definition catalogue | [v0.3.5, 17 October 2026](../Design/MPSS/MERLIN_Profile_v0.3.5_Connected_Example_and_Definitions_17OCT2026.zip). The records are synthetic examples; the provisional `/0.3/` identifiers remain unchanged. |
| Standards-pedigree primer | [v0.5, 17 October 2026](../Design/MPSS/MERLIN_Profile_Standards_Pedigree_and_Design_Rationale_Primer_v0.5_17OCT2026.docx), an informative companion. Its version is not a technical profile v0.5. |
| Master research bibliography and source register | v0.10, 22 October 2026: 140 persistent source identities and 29 workbook worksheets. Exact files are linked in the Artifact Register. |
| Recovered continuity documents | PITON v4.6 and update plan v1.6, 22 October 2026. They retain the research checkpoint; this note carries later status and sequencing. |
| Details View sources | Requirements v0.8, dated 8 October and amended 9 October; Semantic Presentation and Interaction Guide v0.5, dated 8 October; and the 55-page Working Views packet named for 10 October, with equipment-review pages dated 11 October. Their recorded proposal and application-guidance boundaries remain visible. |

Publication does not revise the technical profile, close every donor-mapping gap,
or promote a proposal to an adopted requirement. The broader source and edition
record is in the [Artifact Register](../ARTIFACT_REGISTER.md); implementation
selections and exact source locators are in the
[Details View source index](../Research/SOURCE_INDEX.md).

## Completed work to preserve

The version-pinned SAPIENT walkthrough is complete and preserved. The October 19
server exercises and the recorded CS-GO #17 / OSH #363 issues concern the builds
actually tested. Do not restart that work as an unstarted task or claim it
verifies later server versions.

The October 22 OSCAR mapping and residual research are complete as research
deliverables: 27 mapping rows, eight residual records, ten dispositions, six
donor-lineage additions, and 18 recorded offline checks. The source limits and
conditional donor choices remain those recorded in the research package, PITON,
and update plan. Completion of the study does not establish a live OSCAR adapter
or completion of its proposed follow-on bindings.

The subsequently authorized Glaux power demonstration is implemented, deployed,
and verified. It applies the existing synthetic source A/B replacement example:
distinct source identities, directed supply relationships with start-inclusive
and end-exclusive applicability, replacement history, and one 12.6 V reading
describing source B at 10:10 UTC, reported by the station. It supplies no earlier
source A reading or inferred battery capacity, runtime, active flow, or readiness.
The seven original example bodies remain byte-preserved. The
[power mapping](../Design/POWER_ARRANGEMENT.md) records the exact implemented
contract and limits.

The [24 October client checkpoint](https://github.com/OS4CSAPI/glaux-client/blob/b0626044b04241ff35ba6fe1b085dcb97ed6fd0b/Docs/Plans/CURRENT_WORK.md)
records 74 passing local tests, a passing production build, 23 existing browser
regression checks, 44 power browser checks, and 44 checks against the deployed
power example. These are bounded client results, separate from base-standard
schema validity, whole-profile conformance, native-source interoperability, and
measured comparative operator benefit.

| Deployment fact | Recorded value |
| --- | --- |
| Verified runtime commit | `d74b33dabc5fdfcf22574b8efa7f436b4cf32857` |
| Cloudflare Pages deployment | `770d234a-3cb5-415a-aa96-b8fea45180c4` |
| Verified example | <https://glaux-client.pages.dev/?example=power> |
| Project deployment method | Direct Upload; a Git push does not upload the runtime. |

Repository documentation can advance beyond the deployed runtime commit. This
artifact publication leaves that runtime unchanged. Preserve the separate
repository and deployment identities; a later implementation change uses the
existing build, upload, and live-verification workflow.

## Publication decision and immediate work

On 24 October 2026, the owner authorized publishing all identified project
artifacts in `OS4CSAPI/glaux-client`. That decision supersedes earlier directions
keeping those identified originals outside this repository. The catalogue covers
14 current artifacts, with the original source bytes retained and current
Git-native notes carrying subsequent status.

The authorized import includes the original files, readable register,
machine-readable manifest, reconciled documentation index and source references,
and this continuity checkpoint on the existing working branch. All 14 files were
compared with their recovered originals; the nine selected files from the OSCAR
package also match their exact members in the original package. The repository
verifier confirms file fingerprints, catalogue coverage, and local documentation
links. It is included in the existing GitHub Actions checks for future changes.
Use the [maintenance procedure](../Governance/ARTIFACT_MAINTENANCE.md) and run
`python3 scripts/verify-artifacts.py` from the repository root after relevant
updates. The source and implementation checkpoint before this import was
`b0626044b04241ff35ba6fe1b085dcb97ed6fd0b`.

This publication work requires no repeat approval and does not authorize a new
client feature, profile revision, donor survey, server operation, or device
integration. Continue the existing client review using the deployed example and
its recorded evidence. Keep any referenced but unavailable artifact explicit as
a recovery gap; do not reconstruct an original document from its citations.

## Broader open work retained

The radiation function/property vocabulary, selected association and media-access
bindings, and source-supported provenance handling remain the bounded design
backlog recorded by plan v1.6 and the OSCAR dispositions. They are not adopted by
publication and are not prerequisites for importing completed artifacts or
reviewing the deployed power example. Their earlier position as the next research
increment does not override the owner's subsequent client and publication tasks.

PROV retains its recorded candidate role for lineage needs. DCAT, Processes,
CMMN, and Operational Episode retain their conditional standing. The native N42,
IEEE, OMS, SAPIENT, and DISR evidence gates retain their exact source-specific
status; a gate for one claim does not block unrelated authorized work. The
detailed battery/interface proposal is not completed or approved by the bounded
source A/B demonstration.

Future source-selection or conformance-scope changes belong in the master
bibliography and source register as well as the relevant Git record. Any later
technical revision must identify the exact changed binding, reused donor meaning,
reason, and verification. The present publication changes neither those bindings
nor their source meanings.

## Recovering from older packages

An archived directory named `CURRENT` or `CURRENT_WORKING` describes that
package's own date. It does not supersede a later project checkpoint.

| Preserved package | Continuity documents inside it |
| --- | --- |
| Approved technical v0.3.5 package | PITON v4.4 and plan v1.4 under its `01_CURRENT_WORKING` directory. |
| Research v0.9 package | PITON v4.5 and plan v1.5. |
| October 22 OSCAR research package | PITON v4.6 and plan v1.6; technical v0.3.5 remains unchanged. |
| This October 24 Git checkpoint | Later client, deployment, artifact-location, and immediate-action status. The original PITON and plan versions are not renumbered. |

Begin a continuation with the [documentation index](../README.md),
[Artifact Register](../ARTIFACT_REGISTER.md), this note, and
[current client work](CURRENT_WORK.md). Then open the exact source artifact for
the relation or design decision being examined. Preserve earlier source IDs,
decisions, and completed-work evidence instead of rebuilding them from chat.
