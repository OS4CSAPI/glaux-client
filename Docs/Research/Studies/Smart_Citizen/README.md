# Smart Citizen experiment paper

The maintained working paper is **Evaluating Sensor Information Preservation
Through OGC Integration**, version **0.1**, dated **24 October 2026** in
America/New_York. This first edition is a study protocol and preliminary source
assessment. The adapter, CSAPI publication, live experiment, and interface
comparison have not been executed.

## Read and maintain the paper

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
- [Native JSON excerpt](listings/01_native_temperature.json) and
  [proposed SensorML output](listings/02_proposed_temperature_output.sml.json):
  exact companion files for the two listings, with their different standing
  recorded in the manifest.

## Current contents and pending evidence

The first edition includes an abstract, eleven numbered sections, nineteen
references, two figures, four tables, and two code listings. It covers the
problem and rationale, technical baseline, research questions, source evidence,
mapping method, expected coverage, execution/evaluation protocol, screenshot
comparison method, results structure, limitations, and reproducibility.

Figures 3–5 reserve places for the actual vendor interface, matched generic and
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

Edit the manuscript and any affected listing, figure, and reference records in
one change. Preserve the status of each assertion: source-reported, model-level
documentation, integration-created fact, proposed interpretation, or unresolved.
Keep the references alphabetized and update same-author/year suffixes consistently.
Study-local labels do not allocate new identifiers in the master source register.

Use the existing [builder](../../../../scripts/build-smart-citizen-paper.py)
from the repository root with Python containing `python-docx`. SVG embedding uses
the primary runtime Node and `sharp`; the command makes no network requests.

```sh
"$CODEX_PRIMARY_RUNTIME_PYTHON" scripts/build-smart-citizen-paper.py --version 0.1 --date 2026-10-24
```

For a new edition, change the manuscript and manifest version/date and supply
those same values to the builder. Render the DOCX with the document toolchain,
inspect every page, and record the actual page count and review result in the
manifest. Then refresh its fingerprints and run the repository checks:

```sh
python3 scripts/verify-smart-citizen-paper.py --refresh
python3 scripts/verify-artifacts.py
```

The paper verifier checks citations, reference agreement, listing consistency,
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
