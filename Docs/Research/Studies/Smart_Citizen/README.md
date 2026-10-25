# Smart Citizen experiment paper

The maintained working paper is **Evaluating Sensor Information Preservation
Through OGC Integration**, version **0.6**, dated **24 October 2026** in
America/New_York. This edition is a study protocol and preliminary source
assessment. The adapter, CSAPI publication, live experiment, and interface
comparison have not been executed.

## Read and maintain the paper

Detailed engineering/research homework is intentionally maintained outside the paper in the [experiment workbook](Workbook/README.md), following the [execution roadmap](../../../Plans/SMART_CITIZEN_EXECUTION_ROADMAP.md). The paper should summarize and cite workbook evidence as needed rather than absorb exhaustive inventories, rejected mappings, run logs, and discrepancy records.


- [Manuscript](MANUSCRIPT.md): canonical editable text, CMOS 18 author-date
  citations, references, figure captions, and explained listings.
- [Word edition](SMART_CITIZEN_EXPERIMENT_PAPER.docx): generated reading and review
  copy. Apply accepted textual edits to the manuscript before regenerating it.
- [Reference records](REFERENCES.json): structured citation labels, complete
  reference text, source URLs, access date, and editorial authorship convention.
- [Publication manifest](MANUSCRIPT_MANIFEST.json): edition, evidence standing,
  planned figures, and file fingerprints. This is separate from the manifest of
  the fourteen imported originals.
- [Architecture figure](figures/figure_01_architecture.svg) and
  [model figure](figures/figure_02_model.svg): authored explanations of the
  proposed experiment. They are not screenshots or deployed-resource diagrams.
- [Smart Citizen Kit 2.3 photograph](figures/smart_citizen_kit_23.jpg) and
  [figure source record](figures/SOURCES.md): authentic official model reference,
  immutable source location, attribution, rights notices, and evidence limits.
  The photograph is not a verified image of public registration 19639.
- [Native JSON excerpt](listings/01_native_temperature.json) and
  [proposed SensorML output](listings/02_proposed_temperature_output.sml.json):
  exact companion files for the two listings, with their different standing
  recorded in the manifest.

## Current contents and pending evidence

Version 0.6 establishes the vendor-presentation baseline before Glaux implementation, adding two unchanged first-party Smart Citizen UI screenshots, documented source-provider intent, a reconstruction-question table, exact source/rights records, and reserved contemporaneous/CSAPI/Glaux comparison positions. Version 0.5 adds a first-class description of the experimental Glaux client, including its standalone application lineage, the rationale for choosing an explicit-control library boundary, the exact pinned ogc-client CSAPI dependency, the data/profile/presentation architecture, current Cloudflare runtime, and the connected-resource behavior still required for the Smart Citizen run. Figure 3 now documents the client interpretation boundary, and the new client-baseline evidence record preserves the underlying selection and deployment facts.

The current edition includes an abstract, eleven numbered sections, twenty-two
references, four figures, seven tables, and two code listings. It covers the
problem and rationale, technical baseline, research questions, source evidence,
mapping method, expected coverage, execution/evaluation protocol, screenshot
comparison method, results structure, limitations, and reproducibility.

Version 0.4 adds a dedicated experimental-CSAPI-server section covering the upstream pygeoapi/52°North lineage, the tested Oracle deployment, selection evidence, deployment adaptations and known configuration gaps. It adds an authored server-lineage figure and records the exact tested upstream commit and container image. Version 0.3 added an illustrated introduction to the selected environmental
monitoring system, its component roles, and public registration 19639. Table 1
distinguishes the system type, reported product model, registration, source
platform, and unverified physical installation. The first case uses public data;
an owned kit and independent AirGradient comparison remain later extensions.
The source photograph is preserved unchanged, credited, and distinguished from
actual-unit evidence in both the caption and figure source record.

Version 0.2 added a required explanation for every mapping and illustrative
temperature and battery lineage cases. Each explanation connects the native
assertion to the underlying DIM concept, exact MPSS rule, and CSAPI concepts and
SensorML/SWE representation. Every individual donor concept invoked must be
identified and cited, with its edition, exact locator, contribution, and reuse
or adaptation limits. Source vocabularies, established model donors, standard
carriers, MERLIN-authored bindings, and experiment choices retain distinct roles.

Figures 8–10 reserve places for the actual vendor interface, matched generic and
profile-aware Glaux views, and implemented resource relationships. Add them only
with their capture metadata and associated source/mapping evidence. An unmatched
screen capture may illustrate an interface but cannot be presented as a matched
comparison. Results remain pending until the relevant run is performed.

The current protocol places public-data integration before hardware acquisition.
Captured examples support reproducibility throughout that work. Model and resource
metadata, varied observations, and integration provenance are part of the proposed
dataset. An owned kit is a later route to physical evidence gaps. The
[experiment plan](../../../Plans/SMART_CITIZEN_EXPERIMENT_PLAN.md) is reconciled
with this sequencing.

## Updating an edition

### Mapping explanations

Apply manuscript Table 4 to every new or revised mapping, including metadata and
relationships. Identify each donor concept individually; a generic citation to
an entire RFC or a list of standards is insufficient. Record direct reuse,
adaptation through a binding, an interpretive constraint, or an unestablished
equivalence as appropriate. A source can have more than one role, but the paper
must explain each contribution and any scope or meaning changed by the mapping.

Use a stable study-local mapping identifier and preserve source, model, binding,
standard-carrier, transformation, presentation, and review evidence together.
When an attribution has not been verified, say so and identify the missing
evidence. Do not infer historical donor lineage from similar labels or convert
a proposed interpretation into an adopted profile rule. The illustrative
`SC-TEMP-01` and `SC-BATT-01` discussions are incomplete execution cases, not
claims that the full dataset is mapped or the service path has been run.

### Paragraph structure

Every narrative paragraph must contain at least three and at most five sentences.
This includes the abstract and explanatory text after figure, table, and listing
caption titles. Headings, front matter, keywords, research-question list items,
table cells, code blocks, caption labels/titles, and bibliographic entries keep
their structural formats. Revise for coherent reasoning rather than padding a
paragraph to satisfy the count.

The verifier applies a deterministic sentence check for the manuscript's Markdown
style and reports the section, line, and opening words of any failing paragraph.
It handles the current citation, abbreviation, decimal, link, and code patterns;
editorial review still checks language and ambiguous cases. Inspect counts before
building with `python3 scripts/verify-smart-citizen-paper.py --paragraph-report`.

### System and figure identification

Introduce each added experimental system by type, reported product model, and
selected specimen before discussing its mappings. Distinguish model imagery
from verified photographs of the particular installation, and separate a public
registration from enduring physical identity. Preserve source credit, immutable
asset location where available, access date, any changes, rights notices, and
evidence limits in the figure source record. Do not infer a unit's installed
components, enclosure, power arrangement, or shipping variant from a model photo.

### Publication workflow

Edit the manuscript and any affected listing, figure, and reference records in
one change. Preserve the status of each assertion: source-reported, model-level
documentation, integration-created fact, proposed interpretation, or unresolved.
Keep the references alphabetized and update same-author/year suffixes consistently.
Study-local labels do not allocate new identifiers in the master source register.

Use the existing [builder](../../../../scripts/build-smart-citizen-paper.py)
from the repository root with Python containing `python-docx`. SVG embedding uses
the primary runtime Node and `sharp`; the command makes no network requests.

```sh
"$CODEX_PRIMARY_RUNTIME_PYTHON" scripts/build-smart-citizen-paper.py --version 0.6 --date 2026-10-24
```

For a new edition, change the manuscript and manifest version/date and supply
those same values to the builder. Render the DOCX with the document toolchain,
inspect every page, and record the actual page count and review result in the
manifest. Then refresh its fingerprints and run the repository checks:

```sh
python3 scripts/verify-smart-citizen-paper.py --refresh
python3 scripts/verify-artifacts.py
```

The paper verifier checks paragraph lengths, citations, reference agreement, listing consistency,
figure presence, document input fingerprints, and publication hashes. A manifest
refresh cannot legitimize a Word file generated from older text, figures, or
builder code. The Word file carries a combined fingerprint of those build inputs. The
repository's existing verification command also runs the paper checks.

Record substantive changes in the manifest revision history and the project
continuity note. Maintain a single current manuscript and Word edition here;
Git history preserves previous editions. Do not regenerate or relabel the original
MPSS and Details View artifacts to incorporate paper findings implicitly.

Return to [Research](../../README.md), the [artifact register](../../../ARTIFACT_REGISTER.md),
or the [documentation index](../../../README.md).
