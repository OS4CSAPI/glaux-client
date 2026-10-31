# Resource Details View — cross-vendor candidate profile-aware test

## Temperature of what? — Dragino and Campbell, 30 October 2026

[**Open the comparison in Glaux**](https://glaux-client.pages.dev/?page=resource-details-profile-test&case=temperature). Check **Show air temperature only**. Two rows remain: the Dragino S31-LB probe's **27.2 °C** and the ClimaVue 50's **No reading supplied**. Campbell's **25.91098 °C** disappears because it describes the CR1000X logger's wiring panel, not the air. Uncheck the box to see it again alongside the other quantities.

| What the screen labels | Published example or documented capability |
|---|---|
| Dragino S31-LB · external SHT31 probe | **27.2 °C** ambient air temperature and **56.6%** relative humidity, decoded from published history entry C-E01. Two quantities from one probe. |
| Campbell CR1000X · logger | **25.91098 °C** wiring-panel temperature, from the manufacturer's separate `PanelTemp` status example. |
| Campbell ClimaVue 50 · weather instrument | Air temperature and humidity-sensor temperature are defined at `aR7!` positions 8 and 12; no readings supplied for either field. |

Select **Generic CSAPI-style fields** to see the corresponding source field names or positions without changing the values. **Management → Sources** links to the evidence. This is the existing screen, not another application: the source picker still provides the previous examples. The common reader associates values with fields by source context, output and field name; the air-only filter uses the field's property definition, not its label, manufacturer or unit. Inputs are local, pinned copies of the [worked Profile examples](https://github.com/OS4CSAPI/glaux-client/tree/aa655461ac949648f32398291f7e00e77532e9c1/Docs/Research/DIM_Profile_V2/Candidate_Specification/examples), with Dragino's published C-E01 entry decoded in the input adapter.

**What was verified:** The [build, tests and deployment](https://github.com/OS4CSAPI/glaux-client/actions/runs/41165469841) published commit `27688aa6f7599dcffb1117ec1b0e634ec2633539` to [this immutable Pages deployment](https://6a1d2300.glaux-client.pages.dev/?page=resource-details-profile-test&case=temperature). A browser on the public production URL returned the five rows above, two after filtering, and five after clearing the filter. It also showed the source-field view, source links and a successful switch to Smart Citizen and back. This verifies client presentation of the supplied examples, not live hardware, a joined Campbell station, CSAPI service ingestion or full Profile conformance.

## Earlier experiment — 28 October 2026

**Project-wide objective and approved recovery:** [DIM/Profile V2 Original Problem and Outcome Baseline](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md) and [PITON v1.5](https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/PITON_DIM_Profile_V2_Continuity_v1.5_28OCT2026.md), on the **separate research branch**. These must be read before using this experiment to propose new model/profile/UI work. They preserve the original TRSS/OmniSense vendor-to-CSAPI normalization and presentation-fidelity problem, which earlier PITONs omitted.

**Owner assessment, 28 October 2026:** This profile-aware version is **“quite janky” but “on the right path,” at an appropriate preliminary stage and nowhere near finished**. The meaningful achievement is starting to render actual source-fixture JSON into the shared Resource Details canvases; the observed behavior should guide **iterative refinement of the DIM, Profile and profile-aware client together**. This is neither acceptance of the prototype's final navigation, nor proof of completed client/server interoperability. The prior research-commentary Smart Citizen page was **not** what the owner asked to test and is retained only for its optional research context.

**Documentation-only note:** No UI/fixture code or deployed site behavior was changed by this owner-feedback record.

**Date:** 28 October 2026. **Standing:** separate, non-normative client-side experiment. This is NOT a published DIM, a CSAPI application profile, a live CSAPI response, device control, or conformance verification. The existing Resource Details template, Activity page and previous Smart Citizen research walk-through remain unchanged.

**Route:** /?page=resource-details-profile-test

## Purpose

This page directly tests the original hypothesis: heterogeneous sensing systems can share a useful System Details experience if a domain-grounded semantic chassis and associated Profile tell clients what different source attributes mean, without erasing the important details particular to each vendor.

The issue is not that CSAPI and SensorML necessarily delete information. The OGC SensorML 3.0 Scope describes the model as a common framework and explicitly recognizes the benefit of community-specific semantic vocabularies. Generic property grids do not automatically know how to turn specialized source descriptions into a meaningful operational display. Published CSAPI 1.0 also distinguishes compact GeoJSON summary and rich SensorML descriptions (Part 1, Annex C.4).

## What the experiment renders

The same fixed 560 × 440 Resource Details module is reused with a source selector and a comparison between an illustrative **generic raw-field listing** and a **provisional profile-aware interpretation**. Both consume the same bounded source facts.

| Case | Basis | Valuable distinction |
| --- | --- | --- |
| Smart Citizen Kit 2.3 | Manufacturer design and source code, from our completed [I13 source-grounded study](../Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md) | Data and Urban Boards; cabled PM module normally in enclosure; one SHT31 yields temperature/humidity; one AS7331 yields UV-A/B/C; product options differ from actual installed configuration. No real physical-unit identity or Observation is invented. |
| TRSS ETU-II | Existing committed synthetic historical source fixture | Detector 1 and Detector 2 retain distinct configured choices, separate from supported options; source **estimated capacity percentage** is not a measured voltage. |
| OmniSense Core2 | Existing committed synthetic historical fixture | Five reported transducer labels retain their source meaning, without creating independent physical System IDs. |
| OmniSense Core5ADS | Separate committed synthetic historical fixture | Historical 15.43 V DC source value is **voltage**, not charge percentage or live readiness; a literal unverified source time remains unverified. |

The rulebook, shared across manufacturers, maps declared source term names into an **interpretive role and Resource Details view**, retaining source-defined groups. Unknown fields remain visible in Management / Sources, rather than being assigned invented meanings or dropped. This is an initial **client interpretation convention** only, not an adopted Profile vocabulary.

## How to use it

Begin with SCK2.3 and **Candidate profile-aware**, then inspect Operational / Equipment and Management / Configuration. Toggle **Generic CSAPI-style fields**: the same values remain visible but are not organized by operational meaning. Next switch to TRSS and OmniSense, without swapping UI components, and inspect Equipment/Condition. The layout remains consistent while applicable detail and qualifiers differ.

The test has no live sensor, actual observation, valid physical Kit identifier, verified hardware-to-platform association, or real device command. It deliberately distinguishes a manufacturer product kind from a CSAPI individual System. Local TRSS/OmniSense inputs are synthetic SensorML-shaped fixtures; their use here does NOT establish conformance to a published standard or future Profile.

**Success criterion:** A single client component can present meaningful common categories across heterogeneous descriptions, while retaining vendor labels, units, group relations, source basis, and explicit unknowns. Failure of any one test is feedback to the DIM/Profile research, not a reason to invent missing data.

## Traceability

Core source data and local interpretation: src/profile/resource-details-proof.ts. Shared UI renderer: src/presentation/resource-details-profile-test.ts. Scoped styling: src/presentation/resource-details-profile-test.css. Offline tests: tests/resource-details-proof.test.ts. Synthetic TRSS/OmniSense records are the original, unchanged files under public/fixtures. The Smart Citizen original manufacturer references are pinned to the commits recorded in [I02](../Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md).

This prototype does not adopt quarantined model anatomy or invent normative SHALLs. The owner determines whether the actual display helps solve the original vendor-to-CSAPI fidelity problem.
