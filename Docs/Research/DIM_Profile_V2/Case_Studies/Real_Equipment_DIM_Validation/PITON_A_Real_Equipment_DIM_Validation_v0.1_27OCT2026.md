# PITON A — Real Equipment DIM Validation: Evidence Gate Continuity

**Date:** 27 October 2026  
**Version:** 0.1  
**Standing:** **Current case-study restart and evidence handoff after I04**. Research-continuity control, **not** an adopted Domain Information Model (DIM), profile, conformance claim or proof of a physical-unit experiment.  
**Repository:** `OS4CSAPI/glaux-client`  
**Working branch:** `research/dim-profile-v2` — **NEVER default to `main`**  
**Case-study folder:** `Docs/Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/`

> **RESTART INSTRUCTION:** When the owner writes **“proceed”**, first fetch the current [case-study README](README.md), [13-iteration plan](PLAN_13_ITERATIONS_v0.1_27OCT2026.md), and the actual [I04 audit](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md) from this exact branch. Read the underlying case-study source registers and parent research as needed, **not a compressed conversation summary**. If this PITON's progress statement becomes historical, the **newer verified README and plan** control. Then perform **only the next named iteration** and stop.

## 1. Exact current state

- **I01 completed** — [Equipment Selection and Qualification](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md): **Smart Citizen Kit 2.3** chosen as the equipment-product design baseline; no physical serial number established.
- **I02 completed** — [Pinned Source Corpus](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md): 25 selected files in four full-Git-commit-pinned Fab Lab Barcelona repositories. **Not** a corpus of observed individual-unit data. Earlier false source discrepancy has a visible I04 correction note.
- **I03 completed** — [Source-Native Fact Register](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md): **60 stable F001–F060** evidence rows, six audit flags, six explicit unit/data gaps. It now has a visible I04 correction notice plus targeted source-faithfulness edits; **do not renumber fact IDs**. The register was intentionally made *without DIM mapping*.
- **I04 completed** — [Independent Audit and Gate A](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md): **34 of 60 facts independently source-checked**, plus selected engineering corroboration; explicit verdict and corrections recorded. **Gate A: CONDITIONAL PASS for product/design evidence only.** Individual-unit identity and real observations are **NOT VERIFIED / NOT TESTED**.
- **I05–I13 NOT STARTED.** **Next: I05 — Individual System Identity and Product / Model / Kind mapping**, using the already completed donor research and audited I03 facts. This is a candidate-mapping exercise, **not** a claim of a verified fielded unit.

**Overall status:** **4 / 13 substantive iterations completed**. PITON A is the I04 recovery checkpoint. PITON B is planned for I08; PITON C for I13. No case-study DIM slice, UML class model, CSAPI binding, profile obligation, or conformance test has been created.

## 2. Source of truth: how to read this project in a new chat

**Read in order:**

1. **Current execution/tracker:** [README](README.md) and [13-iteration plan](PLAN_13_ITERATIONS_v0.1_27OCT2026.md); check which Ixx is really next and the user-approved **one-`proceed`/one-iteration** rule.
2. **Actual evidence:** [I01 selection](I01_Equipment_Selection_and_Qualification_v0.1_27OCT2026.md) → [I02 versioned source corpus](I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md) → [I03 60-fact register](I03_Source_Native_Fact_Register_v0.1_27OCT2026.md) → **[I04 audit and source-fidelity corrections](I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md)**. Treat **I04's corrections and Gate A scope as controlling** over dated, superseded I02/I03 statements.
3. **Conceptual work being tested:** [Original Concept Baseline](../../DRAFT_Concept_Baseline_v0.1_25OCT2026.md), [DIM Concept and Method Basis](../../DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md), [Five-Pass Synthesis Checkpoint](../../DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md), and [Canonical Concept Consolidation Plan](../../DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md), which links the five original detailed pass notes.
4. **Preserved epistemic safeguards:** [Parent PITON v1.4](../../PITON_DIM_Profile_V2_Continuity_v1.4_26OCT2026.md), [C08 audit](../../DIM_Profile_V2_Anatomy_PhaseA_Validation_Audit_v0.1_26OCT2026.md) and [30-lineage trust triage](../../DIM_Profile_V2_Anatomy_PhaseA_Bulk_Trust_Triage_v0.1_26OCT2026.md). **Earlier anatomy Phase B/C/D outputs remain QUARANTINED.** Those notes' old progress statements are historical, **not** authority to repeat already finished research or stop at the wrong gate.

The main repository's existing research goal remains a whole-system DIM for equipment-realized sensing Systems, with **`systemType = Sensor` and `assetType = Equipment`** as current CSAPI-grounded characterization (not three new peer classes or a finalized domain title). **No new umbrella domain name is to be invented** without source and user judgment.

## 3. Four pinned upstream source commits

| Family | Frozen authoritative upstream Git commit | Valid use |
| --- | --- | --- |
| **D** — published documentation source | `fablabbcn/smartcitizen-docs@0a18bc0bd372d2bcedfca5bc5e6109f88ea8519f` | Manufacturer wording, version-specific sensor table, assembly, operation and platform descriptions |
| **H** — hardware/firmware | `fablabbcn/smartcitizen-kit-2x@3dbbc1061509920aca2dda2aca32abe82563500b` | SCK2.3 board design, source firmware, manufacturing list and compile-time support (not one installed unit) |
| **R** — data tooling/examples | `fablabbcn/smartcitizen-data@4f024f4d42cb40c2cd515062ee7e4815bd2798eb` | Official notebook code and `sc_air` processing blueprint (not real observed results) |
| **A** — backend source | `fablabbcn/smartcitizen-api@25a524cbfb036f8950c247b847d8884a4e776297` | API source and source-tree version; no established production deployment revision |

**I04's two supplemental exact H sources**, not part of I02's selected 25-file list but **inside the same immutable H commit**:

- [`hardware/SCK2.3/SCK_DATA_BOARD_2.3/SCK_DATA_BOARD_2.3_for_Manufacture/04-SCK_DATA_BOARD_2.3_pick&place.mnt`](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/hardware/SCK2.3/SCK_DATA_BOARD_2.3/SCK_DATA_BOARD_2.3_for_Manufacture/04-SCK_DATA_BOARD_2.3_pick%26place.mnt#L38-L40) — `IC6 S25FL064L` is the design's dedicated external flash component, different from `IC4 ESP-12-E`.
- [`lib/Sensors/Sensors.h`](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/lib/Sensors/Sensors.h#L35-L41) — `SCK23_AIR` compile-time sensor-family switches.

Additionally I04 actually inspected **I02 H03**, the pinned [SCK2.3 Urban Board Eagle schematic](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/3dbbc1061509920aca2dda2aca32abe82563500b/hardware/SCK2.3/SCK_URBAN_BOARD_2.3/SCK_URBAN_BOARD_2.3.sch#L7496-L7543), for exact 2.3 sensor references.

## 4. Corrections and limits that must survive future iterations

**Correction 1 — previous published-vs-frozen sensor table conflict was false.** I02/I03 had claimed public HTML named parts like `AS7311` while frozen Git named `AS7331`. The independent 27 October public-page recheck did **not** reproduce that: current public pages match Git, and the 2.3 Urban schematic supports `MPL3115A2`, `AS7331`, `ICS-43432`, `SHT31`, and `BH1730FVC`. The old alleged conflict is **RETRACTED as research error**, with visible correction notices in I02 and I03. **Do not hallucinate it back into the model.**

**Correction 2 — source conflict about flash storage.** D03 says **4 MB “extra” flash** while D07 specifies **8 MB S25FL064L**. I04's manufacturer 2.3 pick-and-place record **corroborates S25FL064L for the 2.3 design**, so the 8 MB description is better supported for that *specified dedicated reading buffer*. D03's 4 MB narrative is still a real historical source statement but not the preferred resolved design fact. The separate ESP module storage must not be conflated with the data buffer. No physical unit has been inspected.

**Correction 3 — targeted I03 precision.** `F023` citation expanded to cover the **2.2 comparison source**; `F025` no longer conflates PM size-designated mass-concentration channels with generic “mass fractions”; `F035` correctly says WARNING can preserve reading collection while an SD **or** network pathway is affected; `F047` preserves the manufacturer's inconsistent “four-digit / letters-and-numbers” DIY code wording. The **F001–F060 numbering is unchanged**.

**Still open and absolutely not to invent:**

- No verified serial/physical identifier, installed PM option, configuration, firmware, location, calibration/service events or state for any named SCK2.3 Kit.
- Platform IDs `18486–18489` occur in an **unexecuted official notebook** and are not verified individual-unit IDs, API records or readings. The notebook's `sc_air` blueprint does **not** prove advanced electrochemical sensors were installed on those units.
- Advanced Station/`Hardware ID`/calibration sticker is described in source; it is *not* automatically a basic SCK2.3 identifier. The platform `device ID` may change with re-registration.
- Source code `SAMverNum 0.9.11` and API repository `VERSION 1.1.5` do **not** prove actual deployed software versions. The observed public API retrieval failure is **not** proof no data exist.
- **The remaining 26/60 facts not independently sampled in I04** require exact-source targeted checking before they become consequential mappings.
- Do not turn source-specific hardware, API, field, firmware or data-processing names into new DIM classes, nor conflate `systemKind` with implemented `procedures`, CSAPI Composition with UML diamonds, System with representation, or donor semantic mappings with standards conformance.

## 5. Next action — only one `proceed`

**I05 — Individual System Identity and Product / Model / Kind.** Read Pass 1 and Pass 2 **actual** cited notes from the [canonical concept plan](../../DIM_Profile_V2_Canonical_Concept_Consolidation_Plan_v0.1_26OCT2026.md). Apply them to the **audited, line-anchored SCK2.3 fact IDs** (especially F001–F004, F020–F026, F047–F051, F058–F060). Separate known manufacturer product/kind properties from the *unknown* serial/physical equipment individual. Explain what is supported, partial and impossible to test; **do not invent a particular deployed unit**. Produce **one GitHub mapping note**, verify and link it, update README/plan, stop before I06.

If the physical-unit evidence gap prevents a claim, **say so**. The current Gate A verdict permits bounded source-faithful concept mapping but **not empirical device-identity validation**. The owner expects the end of every iteration to say **what was accomplished, why it matters, GitHub links, the precise next step**; a simple **“proceed”** must then start that next named step. No repetitive approval carousel.

**Next: I05 — Individual System Identity and Product / Model / Kind. Say “proceed” to begin.**
