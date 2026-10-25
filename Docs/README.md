# Documentation index

This is the single documentation root for the OS4CSAPI Glaux Client experiment.
Governance, Plans, and Research follow the organization of
[Glaux's Docs directory](https://github.com/DGIWG-P507/glaux/tree/main/Docs);
Design and Testing are additions for this client experiment. This organizational
reference does not imply adoption or endorsement.

## Start with the maintained artifacts

The [Artifact Register](ARTIFACT_REGISTER.md) is the authoritative catalogue of
the 14 published project source files. It links the requirements, guide, working
views, MPSS profile and examples, pedigree primer, bibliography/source register,
research reports, and original continuity documents. The
[machine-readable manifest](ARTIFACTS.json) records their versions and byte hashes.

The [current MERLIN continuity checkpoint](Plans/CONTINUITY.md) carries project
status and immediate sequencing forward to 24 October 2026. The original files
retain their source dates and contents; publication does not turn their proposals
into adopted requirements or revise the technical profile. Follow
[artifact maintenance](Governance/ARTIFACT_MAINTENANCE.md) when updating the set.

For the subsequent real-source evaluation, start with the maintained paper
**Evaluating Sensor Information Preservation Through OGC Integration**, v0.4,
24 October 2026: [canonical manuscript](Research/Studies/Smart_Citizen/MANUSCRIPT.md)
and [generated Word edition](Research/Studies/Smart_Citizen/SMART_CITIZEN_EXPERIMENT_PAPER.docx).
Its [maintenance guide](Research/Studies/Smart_Citizen/README.md) explains the
citation, figure, listing and evidence workflow. Its
[publication manifest](Research/Studies/Smart_Citizen/MANUSCRIPT_MANIFEST.json)
is separate from the manifest of the 14 preserved originals.

Version 0.4 adds the experimental CSAPI server as a first-class study component, documenting the pygeoapi/52°North lineage, tested Oracle deployment, bounded selection evidence, exact revision/image, deployment adaptations, and the configuration details that remain to be captured. Version 0.3 added an early illustrated overview of Smart Citizen as an
environmental-monitoring system. An authentic SCK 2.3 model reference photograph
is explicitly distinguished from public registration 19639, whose physical
installation remains unverified. The immediate case uses that public feed;
owned hardware and an independent AirGradient comparison remain later extensions.

The paper retains the seven-layer mapping explanation matrix and illustrative
temperature (`SC-TEMP-01`) and battery (`SC-BATT-01`) lineage cases. Every mapping
must connect its CSAPI and SensorML/SWE representation to the underlying DIM
concept, exact MPSS rule, individually attributed donor concepts and their reuse
status, and project-authored choices. The paper's maintenance rules also require
three to five sentences per narrative paragraph, including abstract and caption
explanations; headings, tables, code, and reference entries remain structural.

The paper is a study protocol and preliminary source assessment, supported by the
[candidate study](Research/Reports/OPEN_SENSOR_CANDIDATES_2026-10-24.md),
[access evidence](Research/Evidence/OPEN_SENSOR_ACCESS_2026-10-24.json), and
[experiment plan](Plans/SMART_CITIZEN_EXPERIMENT_PLAN.md). The proposed sequence
starts with public-source acquisition, an adapter, CSAPI publication and Glaux
evaluation, supported by captured replay and matched comparisons; owned hardware
comes later. No adapter, experiment run, CSAPI publication, screenshot comparison,
or conformance result is established by the paper's publication.

## Current authoritative material

For the current Details View increment, start with:

| Material | Current source |
| --- | --- |
| Original project artifacts, versions, authority, and canonical paths | [Artifact Register](ARTIFACT_REGISTER.md), [manifest](ARTIFACTS.json) |
| Broader DIM/MPSS continuity and sequencing | [Current MERLIN continuity](Plans/CONTINUITY.md) |
| Maintained Smart Citizen research paper v0.4 and publication record | [Manuscript](Research/Studies/Smart_Citizen/MANUSCRIPT.md), [Word edition](Research/Studies/Smart_Citizen/SMART_CITIZEN_EXPERIMENT_PAPER.docx), [maintenance guide and manifest](Research/Studies/Smart_Citizen/README.md) |
| Open sensor candidates, recommendations and actual access findings | [Candidate study](Research/Reports/OPEN_SENSOR_CANDIDATES_2026-10-24.md), [evidence record](Research/Evidence/OPEN_SENSOR_ACCESS_2026-10-24.json) |
| Proposed first real-source experiment and its PBI/profile outputs | [Smart Citizen experiment plan](Plans/SMART_CITIZEN_EXPERIMENT_PLAN.md) |
| How the document collection is maintained | [Artifact maintenance](Governance/ARTIFACT_MAINTENANCE.md) |
| Deployed page index and ongoing page metadata | [Page-index maintenance](Design/PAGE_INDEX.md) |
| Recovered Resource Details frame and blank review canvas | [Resource Details template](Design/RESOURCE_DETAILS_TEMPLATE.md) |
| Purpose, setup, scope, and implementation status | [Root README](../README.md) |
| Development boundaries and documentation convention | [AGENTS.md](../AGENTS.md) |
| Pinned library provenance, build method, and deliberate updates | [DEPENDENCIES.md](DEPENDENCIES.md) |
| Current implementation checkpoint and actual checks | [Current work](Plans/CURRENT_WORK.md) |
| Cloudflare deployment settings and actual status | [Cloudflare deployment](Plans/CLOUDFLARE_DEPLOYMENT.md) |
| Continue the deployment in local Codex / VS Code | [Codex VS Code handoff](Plans/CODEX_VSCODE_HANDOFF.md) |
| Exact source versions, locators, and evidence limits | [Source index](Research/SOURCE_INDEX.md) |
| Bounded bindings, experimental mappings, and unresolved profile gaps | [Details View mapping](Design/DETAILS_VIEW_MAPPING.md) |
| Existing power model, exact records and implemented behavior | [Power arrangement mapping](Design/POWER_ARRANGEMENT.md) |
| Acceptance criteria | [Details View acceptance](Testing/DETAILS_VIEW_ACCEPTANCE.md) |
| Reproducible browser checks and recorded results | [Browser verification](Testing/BROWSER_VERIFICATION.md), [check list](Testing/BROWSER_RESULTS.json) |
| Executable checks | [CSAPI smoke tests](../tests/csapi.smoke.test.ts), [retrieval tests](../tests/data.client.test.ts), [generic extraction tests](../tests/data.standard.test.ts), [interpretation tests](../tests/profile.interpret.test.ts) |
| Automated local-check definition | [CI workflow](../.github/workflows/ci.yml) |
| Bootstrap verification evidence | [Successful bootstrap CI run](https://github.com/OS4CSAPI/glaux-client/actions/runs/39970543341) |

The current increment reconstructs the first three operator tabs with synthetic
source examples and competent standard inspection. Live device integration, whole-profile
conformance, and a measured profile benefit are not established. The folder
introductions below identify destinations, not additional policies or approvals.

## Documentation destinations

| Folder | Intended contents |
| --- | --- |
| [Governance](Governance/README.md) | Project scope, operating rules, and recorded decisions |
| [Plans](Plans/README.md) | Implementation plans, current status, and continuity/handoff checkpoints |
| [Research](Research/README.md) | Source assessments, standards comparisons, mapping studies, and research registers |
| [Design](Design/README.md) | Wireframes, operator tasks, architecture, and profile-to-presentation mappings |
| [Testing](Testing/README.md) | Test plans, acceptance criteria, evaluation methods, and concise results linked to evidence |

## Status and publication

Keep this index pointed at current authoritative material as documentation grows.
Clearly distinguish proposals from recorded decisions and superseded history;
mark superseded documents and link to their current replacements. Record actual
decision status and supporting evidence rather than implying approval.
Creating a folder or recording a proposal does not approve a design change.

On 24 October 2026, the owner authorized publication of the identified project
artifact set. Those original files are now maintained at the registered paths.
The surrounding archival bundles and unrelated source collections are not part
of this selection. Actual wireframe and profile sources remain the evidence for
their respective claims; do not infer requirements from folder names.

Executable fixtures and tests remain in their appropriate code directories.
Documentation links to them and supporting evidence rather than creating
competing copies.
