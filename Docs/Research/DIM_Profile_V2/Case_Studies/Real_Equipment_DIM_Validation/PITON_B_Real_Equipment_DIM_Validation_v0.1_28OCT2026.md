# PITON B — Smart Citizen Case Study: Five-Finding Reconciliation and Gate B Continuity

**Date:** 28 October 2026  
**Version:** 0.1  
**Status:** **I01–I08 complete (8 of 13 iterations); I09 NEXT, not begun.**  
**Purpose:** Exact case-study recovery and evidence ceilings at the Phase B → Phase C boundary, **not** an adopted Domain Information Model (DIM), application profile, UML class model, verified deployed equipment description, or conformance claim.  
**Working repository / branch:** `OS4CSAPI/glaux-client` / **`research/dim-profile-v2`** (do not inadvertently inspect or commit to `main`).  
**Working folder:** `Docs/Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/`.

> **New-chat restart:** Re-fetch the current [README](README.md) and [13-iteration plan](PLAN_13_ITERATIONS_v0.1_27OCT2026.md) directly from the working branch **before trusting this PITON's historical status**. Then fetch [I08 reconciliation and Gate B](I08_Digital_Representation_and_Five_Pass_Reconciliation_v0.1_28OCT2026.md), [I04 evidence audit / Gate A](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md), and the specific cited sources that I09 will depend on. **A single user “proceed” authorizes precisely I09, not I10/I11 or a new research survey.**

## 1. What is actually complete

| Iteration | Committed artifact | Value earned, not claimed |
| --- | --- | --- |
| **I01** | [Equipment selection](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md) | Smart Citizen Kit 2.3 chosen as verifiable **product/design** example; no authenticated fielded unit |
| **I02** | [Frozen source corpus](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md) | 25 indexed original files from **four immutable upstream repository commits**; vendor web pages and live API are not frozen data |
| **I03** | [Source-native fact register](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md) | **60 stable F001–F060** evidence rows, 6 audit flags and 6 unit/data gaps; no imposed DIM structure |
| **I04** | [Independent evidence audit and Gate A](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md) + [PITON A](PITON_A_Real_Equipment_DIM_Validation_v0.1_27OCT2026.md) | **34/60** facts sample-checked; false alleged sensor-table mismatch **retracted**; 8 MB S25FL064L design backed by 2.3 manufacturing source; **Gate A CONDITIONAL** |
| **I05** | [Individual System and Kind](I05_Individual_System_and_Product_Kind_Mapping_v0.1_27OCT2026.md) | Manufacturer's reusable `SCK2.3` design ≠ verified individual equipment; CSAPI `System` vs `systemKind` roles correctly distinguished |
| **I06** | [Procedure/Method](I06_Procedure_and_Method_Mapping_v0.1_28OCT2026.md) | Real SHT31, SEN5X and AS7331 source routines; advanced `sc_air` processing blueprint, which is **not proven installed/used** in ordinary Kit; **method supported ≠ event executed** |
| **I07** | [Composition and Component Standing](I07_Composition_and_Component_Standing_Mapping_v0.1_28OCT2026.md) | **12** cited physical-design mappings: mating boards, mounted chips, cabled **in-enclosure** PM module, battery, storage, optional interfaces; separate description ≠ independent `System` |
| **I08** | [Digital Representation plus Five-Finding Reconciliation and Gate B](I08_Digital_Representation_and_Five_Pass_Reconciliation_v0.1_28OCT2026.md) | **8** digital evidence findings (DR01–DR08), **five-pass crosswalk**, explicit software-vs-hardware `Component` name collision, source limits and **Gate B CONDITIONAL** |

**Important:** These are *eight completed research iterations*, **not** eight implemented DIM modules, eight normative standards or eight empirical hardware tests. **No finished or adopted DIM slice exists yet.** I09 is where a bounded candidate conceptual slice may first be expressed. PITON A's status (I05 next) is an **old snapshot**; its source/evidence safeguards continue to apply, but this PITON and the living tracker establish the later milestone.

## 2. Exactly which upstream evidence is frozen

All sources below are **official source repositories** pinned to full Git commits, not 2026 live-device observations:

| Source family | Official repository | Full frozen commit |
| --- | --- | --- |
| D — manufacturer documentation | `fablabbcn/smartcitizen-docs` | `0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f` |
| H — engineering and firmware | `fablabbcn/smartcitizen-kit-2x` | `3dbbc1061509920aca2dda2aca32abe82563500b` |
| R — data tools, example notebook and processing | `fablabbcn/smartcitizen-data` | `4f024f4d42cb40c2cd515062ee7e4815bd2798eb` |
| A — Smart Citizen API backend code | `fablabbcn/smartcitizen-api` | `25a524cbfb036f8950c247b847d8884a4e776297` |

**Newly examined in I08 (within the already frozen A commit; not additional deployed data):**

- [`app/models/device.rb`](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/models/device.rb) — backend Device's platform lifecycle, MAC reassignment, hardware-version metadata; a software record, not the physical System.
- [`app/lib/presenters/device_presenter.rb`](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/lib/presenters/device_presenter.rb) — digital fields `id`, `uuid`, `hardware`, `components`, `postprocessing` and access-limited fields.
- [`app/models/component.rb`](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/models/component.rb) — **critical**: source explicitly says `Component` **joins a Device record to a Sensor definition**; not a physical-circuit/part record.
- [`app/lib/presenters/component_presenter.rb`](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/app/lib/presenters/component_presenter.rb) — channels, reading values and timestamps.
- [Historical kit migration](https://github.com/fablabbcn/smartcitizen-api/blob/25a524cbfb036f8950c247b847d8884a4e776297/db/migrate/20230704150532_refactor_kits.rb#L104-L113) — **historical** field `kit_id` references a Kit type in the old schema; the human guide's “kit ID” refers to the **site registration number**. Do not equate them or claim this migration proves a current deployed field.

The full source path list and immutable links are in I02. The I04 and I08 notes identify supplemental files within those pinned trees. **The I02 count remains 25 *initially indexed* files**; it must not be silently rewritten as “only 25 files exist” or “we fetched a production database.”

## 3. Five findings now reconciled with real source design

**Individual System:** An individual physical Kit, when verifiable, is the subject, not the string `SCK2.3`, a network address, page number or software class. **No physical unit has been identified or validated.**

**Reusable kind/model:** `SCK2.3` describes a product generation, and `SEN50/SEN54/SEN55` are alternative PM sensor models with different supported outputs. These are not multiple individually deployed Kits. CSAPI `systemKind` uses a Procedure resource as a **kind-description carrier**; do not confuse it with CSAPI `procedures` (methods the System can implement).

**Method versus execution:** Actual frozen firmware specifies measurement/conditioning routines and a separate advanced offboard postprocessing blueprint specifies algorithms. **No verified event used one of these methods**; neither example code nor configuration support creates a historical Observation.

**Composition/standing:** The standard assembly includes Data/Urban Boards, mounted chips and a **cable-connected PM module physically secured in the enclosure**. Cabled/replacable does not automatically mean a temporary CSAPI Aggregation. The backend's digital `Component` entries are *not* evidence of circuit components. Source-determined granularity matters.

**Digital representation/proxy:** A physical Kit, vendor registration page, `Device` database object, API/CSV/web presentation, `Component` sensor association, processing blueprint and notebook can be related **but are not identical**. A backend `uuid` or device token is not automatically a CSAPI physical System `uniqueIdentifier`. No vendor-specific WoT/AAS/OPC UA proxy/twin/CSAPI service was demonstrated.

**Gate B judgment:** **CONDITIONAL PASS for coherent, traceable, design-level five-finding semantic alignment and demonstrated error prevention.** **NOT PASSED/NOT TESTED** for a positive *physical-to-digital identity join*, real installed component/model inventory, device-method execution, observed data, cross-system interoperability, or standards conformance. This is **not** a semantic failure and **not** a successful full-case empirical demonstration. I04's **Gate A remains CONDITIONAL**, not replaced by Gate B.

## 4. Critical prohibitions and still-open data requirements

Do **not** invent or claim any of the following:

- A specific SCK2.3 Kit serial/hardware identifier, physical-to-platform ID join, current firmware, installed PM sensor model, actual components, deployment/location or calibration/service history.
- Successful device/API access or actual measurements for candidate platform IDs **18486, 18487, 18488, 18489**: they appear in the *unexecuted* official notebook with **zero saved outputs**. No actual data for any of them was obtained.
- That Smart Citizen's backend `Component` denotes a physical board/subsystem, or that `Device.components` maps one-to-one to real hardware.
- That `sc_air` in a notebook proves a basic Kit has advanced electrochemical sensors or actually ran the blueprint.
- That the vendor has implemented CSAPI, WoT, OPC UA, AAS, SAREF, OSUS-R or a digital twin because their *conceptual analogies* are relevant.
- A universal `representedBy` property, `DigitalRepresentation` class, `ProductModel` class, mandatory nested System hierarchy, UML composition diamonds or new profile SHALL requirements.
- The **retracted** I02/I03 sensor part-number mismatch; I04 confirmed published/current 2.3 labels match pinned tables and schematic. Also preserve the 4 MB versus 8 MB design conflict's precise I04 resolution.
- Equivalence between CSAPI `assetType = Equipment` and **AAS `AssetInformation.assetType`**, between CSAPI `systemKind` and `procedures`, or between different donor schemes' identity and cardinality policies.

**Evidence ceiling:** Of original I03's 60 F### entries, I04 independently checked **34**. The others require targeted original-source checking if material to I09. Exact descriptions in the embedded schematic, firmware and backend model source are design/implementation evidence; they do **not** establish active equipment state or observed facts. The 21 October 2026 SOSA/SSN text is a **Working Draft** and not the same normative-edition reference as CSAPI 1.0. Earlier anatomy Phase B/C/D syntheses are **QUARANTINED**, not revived.

## 5. Precisely what I09 must accomplish on the next `proceed`

**Iteration I09 — smallest defensible candidate DIM slice.** Read [the actual I08 reconciliation](I08_Digital_Representation_and_Five_Pass_Reconciliation_v0.1_28OCT2026.md), [I05](I05_Individual_System_and_Product_Kind_Mapping_v0.1_27OCT2026.md), [I06](I06_Procedure_and_Method_Mapping_v0.1_28OCT2026.md), [I07](I07_Composition_and_Component_Standing_Mapping_v0.1_28OCT2026.md) and [I03 corrected facts](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md), plus the [original five-pass synthesis](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md) and exact donor/source notes where the mapping depends on them. Read [the DIM Concept and Method Basis](../../DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md), [modeling convention](../../DIM_Profile_V2_Modeling_Convention_v0.1_26OCT2026.md), and [visualization guide](../../DIM_Profile_V2_Modeling_and_Visualization_Guide_v0.1_25OCT2026.md) only as needed to avoid drifting into accidental final architecture.

Produce **one bounded, cited candidate conceptual-slice note**: identify only the warranted core notions and relationships, the difference between source-native constructs and provisional DIM semantics, exact evidence pointers, *source granularity*, alternative design options and explicit unpopulated instance/observation and digital-identity associations. If a two-dimensional traceability matrix or textual schema conveys more verified content than UML, use that; don't create a decorative class diagram or turn a source API object into a DIM root. No premature application-profile conformance requirements. Commit and **verify** to `research/dim-profile-v2`, update README/plan, stop. **I10–I13 remain not started**.

**At the end of I09:** Explain in conversational terms **what we accomplished**, **why it moves toward the DIM**, **where evidence is missing**, **exact working GitHub link(s)**, and the next step **I10**. The owner should only need to say **“proceed.”**

**Next: Iteration I09 — candidate conceptual DIM slice. Say “proceed” to begin.**
