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

## Current authoritative material

For the current Details View increment, start with:

| Material | Current source |
| --- | --- |
| Original project artifacts, versions, authority, and canonical paths | [Artifact Register](ARTIFACT_REGISTER.md), [manifest](ARTIFACTS.json) |
| Broader DIM/MPSS continuity and sequencing | [Current MERLIN continuity](Plans/CONTINUITY.md) |
| How the document collection is maintained | [Artifact maintenance](Governance/ARTIFACT_MAINTENANCE.md) |
| Deployed page index and ongoing page metadata | [Page-index maintenance](Design/PAGE_INDEX.md) |
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
