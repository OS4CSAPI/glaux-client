# DIM / CSAPI Profile V2 — start here

**Current project-wide entry point — 28 October 2026.** This research workspace supports a **publishable Domain Information Model (DIM)**, a **publishable CSAPI application Profile**, and a **profile-aware client demonstration**. These are **not yet final**. The owner wants a meaningful common Resource Details UI for differently integrated sensing equipment, not just generic CSAPI/SensorML fields. **TRSS and OmniSense were the originating vendor examples.**

## Read these first

1. **[Original Problem and Outcome Baseline](DIM_Profile_V2_Problem_and_Outcome_Baseline_v0.1_28OCT2026.md)** — the **why**, original TRSS/OmniSense problem, proposed chassis→DIM→Profile→client solution, source-to-UI test, publication path, current limitations, and non-drift rules. **This is the authority for the owner's clarified purpose.**
2. **[PITON v1.5 — Current Project Continuity](PITON_DIM_Profile_V2_Continuity_v1.5_28OCT2026.md)** — the **where are we**, branch read order, which experiments exist, which claims are conditional, quarantined work, and which old PITON next-action instructions were superseded.
3. **[Provisional DIM Architecture Blueprint v0.1](DIM_Profile_V2_Provisional_Architecture_Blueprint_v0.1_28OCT2026.md)** — the **whole-model map**: current chassis, five researched semantic distinctions, eight candidate subject areas, cross-cutting qualifications, possible reusable modules/specializations and the path into Profile and UI. **Context map only; no accepted packages, classes, or new study plan.**
4. **[DIM Concept and Method Basis](DRAFT_DIM_Concept_and_Method_Basis_v0.1_25OCT2026.md)** and **[Concept Baseline](DRAFT_Concept_Baseline_v0.1_25OCT2026.md)** — original semantics and method. **[Five-pass synthesis](DIM_Profile_V2_Five_Pass_Synthesis_Checkpoint_v0.1_26OCT2026.md)** — five candidate *distinctions*, not five adopted classes.
5. **[Provisional Published DIM / CSAPI Profile Outlines](DIM_Profile_V2_Provisional_Document_Outlines_v0.1_26OCT2026.md)** — where mature research may ultimately become two separate publications; outlines are not adopted requirements.
6. **[Smart Citizen I13 research report](Case_Studies/Real_Equipment_DIM_Validation/I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md)** and **[I12 critical corrections](Case_Studies/Real_Equipment_DIM_Validation/I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md)** — completed 13-step source-based test and limits. **[Case README](Case_Studies/Real_Equipment_DIM_Validation/README.md)** shows 13/13 completed.

## Latest UI feedback and verified prototype

The **first Smart Citizen case page** showed research commentary and **was not what the owner asked for**. It is retained at [the earlier page](https://glaux-client.pages.dev/?page=resource-details-smart-citizen).

The **new separate test** is [Profile-aware Resource Details](https://glaux-client.pages.dev/?page=resource-details-profile-test). It compares generic field listing with a **candidate term-interpreting UI** inside the same Resource Details frame for SCK2.3 design and synthetic TRSS/OmniSense cases. Owner judgment: **janky but on the right path, appropriately early**, not final. The [app-side design record](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Design/RESOURCE_DETAILS_PROFILE_TEST.md) and [deployed build record](https://github.com/OS4CSAPI/glaux-client/blob/work/details-view-20261023/Docs/Plans/CLOUDFLARE_DEPLOYMENT.md) give exact status: 80 offline tests passed, production deployment verified; **no real CSAPI System/data retrieval, browser automation, normative Profile or completed DIM**.

**Branch discipline:** Research docs on **research/dim-profile-v2**; site code and design records on **work/details-view-20261023**. **Do not default to main.** No credential, operational vendor screenshot or unvetted proprietary material belongs in this public GitHub documentation.

## Important governance

- The chassis scope and full model remain **research questions**. No invented final domain name or mandatory anatomy. Previous over-promoted Anatomy Phase B/C/D files are **quarantined** and not an accepted DIM.
- The 13-step Smart Citizen study is **closed** and its Gate D accepted the *report conditionally*, not actual interoperability.
- The **post-case-study decision checkpoint** that earlier PITON C suggested as an automatic next step was **AI-invented, objected to by the owner, and superseded**. A bare “proceed” is **not automatic authorization** to execute it.
- **Latest owner-authorized step:** One [provisional architectural blueprint](DIM_Profile_V2_Provisional_Architecture_Blueprint_v0.1_28OCT2026.md) was created from the existing donor/whole-system research for owner review. **No class, module, profile obligation, further research pass, or site change was authorized by that map**. When further work is requested, tie it visibly to **vendor source meaning → donor semantics → DIM → Profile → actual client rendering** and explain it plainly before any long sequence.

The new [PITON v1.5](PITON_DIM_Profile_V2_Continuity_v1.5_28OCT2026.md) is the first-recovery reference for a new chat. Older PITON v1.4 and case PITON C remain historical research continuity, not controlling agenda.
