# Project artifact maintenance

Updated 24 October 2026.

The owner authorized publication of all identified MERLIN DIM, MPSS, continuity,
and Details View project artifacts on 24 October 2026. This procedure applies that
decision to the catalogue of 14 current artifacts. Their original source bytes
are preserved; current repository notes record later implementation status and
decisions. Completed initial import verification is recorded in the
[continuity checkpoint](../Plans/CONTINUITY.md).

## Current records and responsibilities

| Record | Maintain it for |
| --- | --- |
| [Documentation index](../README.md) | The entry point and current reading routes. |
| [Artifact Register](../ARTIFACT_REGISTER.md) | Human-readable artifact identities, purpose, edition, authority, canonical file locations, and history. |
| [Artifact manifest](../ARTIFACTS.json) | The machine-readable catalogue and expected file fingerprints. |
| [MERLIN continuity](../Plans/CONTINUITY.md) | Broader DIM/MPSS status, completed work, remaining decisions, and current sequencing. |
| [Current client work](../Plans/CURRENT_WORK.md) | Implemented behavior and actual implementation checks. |
| [Deployment record](../Plans/CLOUDFLARE_DEPLOYMENT.md) | The runtime commit, upload result, and live verification. |
| [Implementation source index](../Research/SOURCE_INDEX.md) | Source editions and locators supporting the implemented mappings. |

The original files remain authoritative for the contents and decision standing
of their identified editions. A newer status note may supersede an old next-action
instruction without changing the old source document. Label that scope precisely.
Updates happen through recorded repository changes.

## Identity, editions, and dates

Use the registered `glaux-artifact-...` key consistently for each maintained
artifact. Keep its identity stable when a later edition becomes current. Record
edition-specific paths, dates, fingerprints, and predecessor/successor links
separately rather than assigning meaning from a filename alone.

Keep these dates distinct:

- **Source version and date:** what the original artifact itself identifies.
- **Amendment or appended review date:** a later change evidenced inside that
  artifact, when supplied.
- **Repository import date and commit:** when these exact bytes were published
  here.
- **Continuity update date:** when the repository's current status or sequencing
  changed.

Importing the profile on 24 October does not change MPSS v0.3.5's 17 October
source date. The Requirements filename's 8 October date does not erase its
9 October amendment. The Working Views filename's 10 October date does not erase
its 11 October appended review pages. The Git continuity note does not create an
unwritten PITON v4.7 or update plan v1.7.

## Preserve original files and explicit successors

Copy each imported original without rewriting, reformatting, or regenerating its
contents. Verify the raw-file SHA-256 against the registered fingerprint. An
office-file save, archive rebuild, or text normalization can change bytes even
when the visible text appears unchanged; the fingerprint is for the file itself.

Put new explanations and implementation status in the appropriate Git-native
note. If authorized work produces a genuinely revised source edition, retain a
clear predecessor, record the new version and reason, and update the current
register entry. Do not silently overwrite an imported baseline while retaining
its old edition or fingerprint.

Keep one canonical repository location for each registered current file. Use
links from other folders rather than competing copies. Record a file move in the
register and manifest and update affected links in the same change. If the bytes
are unchanged, the content fingerprint remains unchanged.

Distinguish an imported source edition, an informative companion, an adopted
bounded rule, a proposed design, a historical parent, and a recorded implementation
result. Publication alone changes none of those statuses. Preserve a reference
to an unavailable artifact as a recovery gap rather than fabricating a replacement
or counting it as a verified imported file.

## Keep the research identifiers intact

Repository artifact keys are separate from the existing master identifiers:

| Existing identifiers | Meaning to preserve |
| --- | --- |
| `S01`–`S140` | Persistent global research source identities. |
| `R01`–`R20` | MPSS profile relationships, not source IDs. |
| `IG01`–`IG11` and `OG01`–`OG08` | Integration-gap history and OSCAR residual records. |
| `OD01`–`OD10` | OSCAR dispositions. |
| `M01`–`M27` | OSCAR mapping rows. |
| `L01`–`L16` and `OL01`–`OL06` | Donor-lineage records. |
| `G01`–`G10`, plus the later named gates | Evidence-gate records with their own claim scope. |
| Study-qualified local IDs | Local study identities reconciled through the source register's Study ID Crosswalk. |
| `SRC-*` | Glaux's implementation citation keys. |

The source register's existing **Artifact Inventory** worksheet inventories donor
and evidence files against source IDs. One source ID can have several artifacts.
It is not the repository's project-document register. Cross-reference that sheet
when useful, without merging its IDs into `glaux-artifact-...` keys or allocating
a new global source ID merely because a project file was imported.

Preserve the workbook's study crosswalk, applied R01–R20 records, workstream
ledger, evidence gates, donor lineage/coverage, integration gaps, and change
ledger. A study-local `S01` must not silently become global `S01`. Future research
changes to source selection or conformance scope must be reconciled with the
master bibliography and source register; an import does not alter them.

## Procedure for a relevant change

1. Open the registered current artifact and the source or decision that warrants
   the change. Use the current continuity checkpoint to avoid restarting completed
   work from an older package's `CURRENT_WORKING` directory.
2. Apply the already authorized change in its appropriate artifact. Preserve
   original imported bytes, and identify an actual successor edition when one is
   produced. Do not infer a new technical decision from a documentation import.
3. Update the Artifact Register, artifact manifest, affected index/source links,
   and relevant continuity note in the same repository change. Record the reason,
   actual verification, and any superseded location or next-action instruction.
   Keep the broader DIM/MPSS history and the client checkpoint consistent.
4. From the repository root, run:

   ```sh
   python3 scripts/verify-artifacts.py
   ```

   Inspect the result and correct any reported catalogue, path, or fingerprint
   mismatch. Check the human reading route in the register and documentation index.
   Record only checks actually completed. This verifies artifact integrity and
   organization; it does not establish profile, OGC, or donor-standard conformance.
5. Save the coherent change to the existing working branch and record the
   repository checkpoint. Confirm that its published links resolve before marking
   publication complete. Keep an unresolved import or verification failure visible
   with its concrete cause.

This procedure adds no repeat approval step for the publication already
authorized. It does not require rerunning completed donor research or introducing
a new conformance-testing programme. When a change also affects implementation,
use the existing checks for the affected code and behavior.

## Deployment and work scope

The recorded runtime remains commit
`71297c971e2e7532f7c7139600f41e9b58bdcc22`, Pages deployment
`97c801c4-c44f-4484-a175-e6651639fe07`, including the page index and later
Resource Details template increment.
An artifact-only change advances the
repository documentation without changing that runtime. Record any later runtime
deployment separately through the existing build, Direct Upload, and live-check
workflow.

Maintain the unresolved radiation, association, media, provenance, and specialist
power work in the broader continuity record with its actual status. Artifact
maintenance does not authorize a new feature, profile obligation, server write,
device adapter, or renewed survey. Follow the owner's recorded task and retain
completed-work evidence so the next continuation starts from the actual checkpoint.
