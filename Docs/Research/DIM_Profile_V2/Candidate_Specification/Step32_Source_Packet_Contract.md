# Step 32 — Source-independent evidence packet and falsification-harness design

**2 November 2026 · Candidate research input contract v0.1 · STEP 32 design deliverable · NOT an OGC API – Connected Systems (CSAPI) wire Profile, normative schema, adopted ontology, deployed service, or shared client implementation.**  
**Execution basis:** [43-step plan, Step 32](../PLAN_DIM_Profile_V2_Whole_System_Recovery_to_Delivery_v0.1_31OCT2026.md#phase-f--implement-and-challenge-one-shared-interpretation-3239), [candidate Profile Step 31](CSAPI_Profile.md#step-31--contract-challenges-source-oracle-tests-and-bounded-gate-e-judgment), [integrated DIM Step 24](DIM.md#step-24--integrated-source-bounded-whole-system-dim-and-relationship-falsification), [workbook §35](../Whole_System_Recovery/README.md#35-step-31--candidate-profile-contract-scenarios-falsification-and-gate-e-decision), and [PITON v2.6](../PITON_DIM_Profile_V2_Continuity_v2.6_02NOV2026.md).  
**Status:** Source-packet *design and four restricted input examples*, not Phase F interpreter execution. The full Gate E decision remains **NOT CLOSED**; this work is bounded G30-01 repair preparation, not proof of portable interoperability.

## 1. The user-visible problem this packet tries to solve

A third-party, Profile-aware client must be able to tell whether a description concerns a **manufacturer reference design, a real physical individual, or a continuing station**, and which evidence supports each fact or relationship. If the available description is only a printed packet example, the client must not present it as live telemetry; if a real station report was duplicated into two server resources, the client must not count two source observations. Those differences currently survive in the research ledger and the Bennett-specific application, but **not yet through a demonstrated, discoverable generic producer→consumer contract**.

Step 32 deliberately defines **one small source-independent test input** to make those differences mechanically expressible before Step 33 implements a reader. The input should support an unchanged reader of Dragino, AirGradient, Campbell and Bennett's Point without testing manufacturer strings, model names, source-file paths, or specially known server IDs to decide meaning. Its scope is **source qualification and bounded evidence**, not a full operational sensor-control ontology, device command service, or universal original-data converter.

This is a **project-authored analytical packet**. The standard CSAPI/SensorML/SWE system still needs a separately selected, interoperable, discoverable way to publish or associate its statements; a valid JSON fixture in GitHub is **not itself** that missing carrier.

## 2. The complete bounded input set — one shape, four source levels

The packet uses [**packet.schema.json**](examples/step32-source-packets/packet.schema.json) as a candidate **JSON Schema Draft 2020-12** for study inputs, with four checked-in, machine-readable cases:

| Actual case evidence and example | Original scope | Nonnegotiable semantic distinction |
| --- | --- | --- |
| [Dragino S31-LB packet](examples/step32-source-packets/dragino.reference.packet.json) · [original research sheet](../Controlled_Corpus/System_Data_Sheets/Dragino_S31_LB.md) | Manufacturer reference node, single externally cabled SHT31; printed scalar example | One physical reference probe and **two** data properties; design battery/default ≠ current charge/setting; no installed unit or original Observation. |
| [AirGradient Open Air Max packet](examples/step32-source-packets/airgradient.reference.packet.json) · [original research sheet](../Controlled_Corpus/System_Data_Sheets/AirGradient_Open_Air_Max.md) | Gas-equipped O-M-1PPSTON-CE reference with pinned hardware/firmware sources | **PM1/PM2 physical hardware sockets** ≠ `pm01`, `pm25`, `pm10` source-reported property fields; published `pm25=27.7` is only an example, not observed telemetry. |
| [Campbell CR1000X + first-gen ClimaVue 50 packet](examples/step32-source-packets/campbell.reference.packet.json) · [original research sheet](../Controlled_Corpus/System_Data_Sheets/Campbell_CR1000X_ClimaVue50.md) | **Two distinct published reference products** and unrelated manufacturer status example | One sensor `aR7!` response has **14 positions**, not 14 physical Systems; logger `PanelTemp` example is not the ClimaVue air-temperature result or a joined actual station. |
| [Bennett's Point historical packet](examples/step32-source-packets/bennetts-point.historical.packet.json) · [frozen original-source selection](examples/bennetts-point-ee181.json) | One real station, individually identified equipment, **two** original NOAA temperature source rows and dated role history | **Two EE181 individuals over three day-scoped service statements**, a returning probe, two original source measurement events represented by four prior experimental CSAPI resources; source stamp, derived nominal interval, raw QA, and unknown result availability stay separate. |

The first three **must have empty `originalEvents` and `representations` arrays**. They are reference/design/schema/printed-example studies, not true captured field-unit activity. Bennett has **two original source events** only because the source archive establishes actual historical station reports. The fixtures are *selected high-value claims*, not exhaustive transcriptions of the vendor manuals, 182 donor artifacts, or a new complete equipment inventory.

## 3. Minimal wire-like structure — project test vocabulary, NOT OGC wire members

| Packet member | Required meaning, evidence boundary and relevant DIM/PR30 test |
| --- | --- |
| `format`, `id`, `focus` | Project version discriminator; **packet-local** key; one focal **source-described** referent. A packet identifier or focus key is not a CSAPI System UID or a manufacturer serial. R24-01/02; PR30-01. |
| `sources[]` | Source **issuer, edition/snapshot, original URL, source authority** and project research locator. The primary source remains the original manufacturer, operator or NOAA archive; the research sheet is an audit index, not a publisher or a replacement original. R24-01/15. |
| `subjects[]` | Explicit referent standing: `REFERENCE_ARRANGEMENT`, `REFERENCE_COMPONENT`, `SOURCE_IDENTIFIED_STATION`, or `SOURCE_IDENTIFIED_EQUIPMENT`. Real individual identities carry original issuer, scheme and raw identifier; reference design positions do not become real serial numbers. R24-02–05; PR30-01–06. |
| `assertions[]` | One assertion about a subject **or a source original event**, with an agreed **candidate local `concept`** and one source-qualified `value` or `target`, or an explicitly unsupported `UNKNOWN`. Source-native field/token, unit and interpretation have separate slots. R24-01/03–15; PR30-01/08/09/13–16/20/21. |
| `assertions[].standing` | Only **`SOURCE_FACT`, `SOURCE_EXAMPLE`, `DERIVED`, `UNKNOWN`** are valid *packet claim standings*. `SOURCE_FACT` from a manufacturer manual is a **fact about that published design**, not a newly discovered deployed instance. `SOURCE_EXAMPLE` never creates an original event. |
| `assertions[].evidence[]` | Source ID and exact native document/field/row locator; `nativeToken` only when an original literal is supported. A paraphrase in a project inventory must not masquerade as source bytes. The original evidence still requires independent fact checking in source-oracle tests. |
| `assertions[].value.raw` | String preserving the **source field's lexical value**, even when interpreted numerically; `unit`, `nativeField` and analyst `interpretation` are separately labeled. Example: the Bennett `F_ATemp` raw token includes a **trailing space** and `F_Record` is an **independently blank** record-wide field. |
| `assertions[].time` | Original date-only, as-of, source-local minute or **explicitly derived** UTC interval. A date-only use row is not assigned midnight, a maintenance-window endpoint, inclusive/exclusive exact exchange, or `now`; source station timestamp never automatically equals OMS `resultTime`. R24-09/12. |
| `assertions[].derivation` | Required for `DERIVED` statements; specifies the analyst method and **which other assertion IDs supplied the inputs**. Does not turn a join into a NOAA-authored field or a native Observation. R24-15. |
| `assertions[].reason` | Required when `standing=UNKNOWN`, **with no value or target**. Means a fact is not established within the cited source scope, **not** that the real-world property is intrinsically zero, false, healthy, absent or unknowable forever. |
| `originalEvents[]` | **Source-scoped original report identity** from original archive/issuer/edition, station, record locator and native measured field. A packet-local event ID only groups the selected original report; it is **not** an OGC observation URI or a universal event identifier. R24-09/15, PR30-12/15. |
| `representations[]` | An independent record of the **project's old CSAPI scalar/archival-copy resource IDs**, each pointing back to one original event, with explicit `HISTORICAL_PROJECT_EXPERIMENT` standing and an earlier verification trace. No new events or current live/conformant format are inferred. R24-15, PR30-15. |
| `holds[]` | Machine-readable list of the existing **G30** missing binding/claim ceilings. A packet makes source-fidelity gaps *visible*; it does not eliminate a missing original time, approved media schema, discoverability, producer relationship or authorization. |

These four input-standing and four subject-standing enumerations are **local experimental distinctions**. They are **not new DIM classes, published vocabulary URIs, OGC requirements-class names or adopted ISO/OGC media fields**. The other three original research labels—`CANDIDATE_MAPPING`, `VERIFIED_RUNTIME` and `REJECTED_EQUIVALENCE`—remain **research/evaluation dispositions**, not artificially promoted into assertions about original equipment.

The schema imposes only local **shape-level guards**: an `UNKNOWN` claim must have a reason instead of a guessed value; known claims use one literal value **or** one target; `DERIVED` must cite its input assertions; source and subject objects are bounded. A future test harness must additionally enforce **cross-reference uniqueness, source authorization/accuracy, derivation validity, case standing and event/copy equivalence**. Ordinary JSON Schema conformance alone cannot prove those.

## 4. Worked example — how the Bennett problem becomes explicit

In the [historical Bennett packet](examples/step32-source-packets/bennetts-point.historical.packet.json), `b-station` is a **real continuing station**. `b-probe3` and `b-probe4` are **two real distinct EE181 individuals**, not a third unit when the former returns. Their three `equipment.role_service` assertions retain the source's **calendar-day** bounds; the last use statement is **still in use as of 2024-12-31**, not “removed then,” not current 2026 status, and not an exact-time CSAPI Deployment.

The two original source-event anchors are deliberately **archive-row-plus-field** identities. The first is NOAA/CDMO 2024 CSV **line 10130 / `ATemp`**, the second **line 10418 / `ATemp`**, each at station `acebpmet`. Original 12:00 fixed-EST station stamps and values **29.1 °C** and **27.3 °C** are **SOURCE_FACT**; original `F_ATemp="<0> "` (including its trailing space) and separately blank `F_Record` are also source tokens. Their **16:45–17:00 UTC nominal intervals** and likely contributor-probe links are separately **DERIVED**, with cited inputs from the source rows, averaging rule and equipment-use periods.

For clarity, these are **two different assertions about the first report**, not one conflated Observation:

```json
{
  "id": "b-qc15",
  "about": "b-event15",
  "concept": "observation.raw_quality_token",
  "standing": "SOURCE_FACT",
  "value": { "raw": "<0> ", "nativeField": "F_ATemp" },
  "evidence": [{ "sourceId": "b-cdmo", "locator": "CSV line 10130, F_ATemp", "nativeToken": "<0> " }]
}
```

```json
{
  "id": "b-attribution15",
  "about": "b-event15",
  "concept": "observation.contributing_equipment",
  "standing": "DERIVED",
  "target": "b-probe4",
  "derivation": {
    "method": "Join actual station/period with separately documented equipment service history",
    "inputs": ["b-mean15", "b-stamp15", "b-period15", "b-service4"]
  },
  "evidence": [
    { "sourceId": "b-cdmo", "locator": "CSV line 10130" },
    { "sourceId": "b-operator", "locator": "Temp/RH sensor 4 use history" }
  ]
}
```

The sample snippets above omit other case-specific evidence details; the **actual checked-in packet** is authoritative for complete input syntax. The `b-result-time15` and `b-result-time18` assertions have `standing=UNKNOWN`, explain that result availability was not recorded, and carry **no invented time value**. `b-producing-system15/18` likewise preserve the unresolved station-versus-logger producing-System question rather than inferring a producer from the existing probe-owned test resources.

| Source report | Source event ID in this test packet | Prior scalar copy | Prior archival-report copy |
| --- | --- | --- | --- |
| 15 Apr 2024, 29.1 °C | `b-event15` | `4f3d3010-9e46-4227-9ba0-7d7014405efa` | `a742b704-c2cd-4c1d-970a-b97b5f628130` |
| 18 Apr 2024, 27.3 °C | `b-event18` | `33599d37-7992-4e14-a4c1-b0df85d62fc2` | `50bf940e-55a0-45b6-9331-e6391704f6c7` |

**Correct count: two source reports / four historical experiment representations.** These resource IDs are traceable to [PITON v1.9](../PITON_DIM_Profile_V2_Continuity_v1.9_31OCT2026.md) and the recorded October 31 Actions, not a new runtime discovery. `representations[].originalEventId` is **project-defined test linkage**, not a verified original server-side `sameAs` property, normative CSAPI original-event correlation, or final two-stream architectural recommendation.

## 5. Source packet ≠ CSAPI Profile: exact proposed boundary

| What an original OGC carrier may express when its source/classes are actually supported | What the Step 32 packet adds as project-owned test input | Remaining original obligation or HOLD |
| --- | --- | --- |
| Source-supported kind/`Procedure`, actual identified `System`, type/identifier when legitimately published; SensorML parts, processes and connections. | Source evidence standing, original issuer, source identity versus packet-local ID, and reference-kind versus actual-individual scope. | **G30-01:** no selected, published/discoverable producer→client evidence association. Project `standing` is not standard CSAPI JSON. |
| Defensible output/property descriptions and SWE Common field schemas for a real supported stream. | Native socket versus bus/address versus field/property meaning and exact reference/example scope. | No manufactured live DataStream or Observation for manufacturer examples; no assumed extra IEEE 1451 channel hierarchy. |
| Actual Part 2 DataStream/Observation only if producing System, required time/quality/format facts and claimed conformance class truly fit. | Original NOAA row/field, exact QA, DERIVED nominal period and probe relationship, explicit UNKNOWN resultTime and source-event copy links. | **G30-02, G30-04–07:** no chosen producer, independent resultTime, demonstrated period/quality mapping or current native SWE JSON verification. |
| Deployment/Host association only when a conformant original target and valid time are justified. | Date-only role-service assertions and 2024 as-of qualifier, separate from station position. | **G30-03:** no exact original probe switch instant, native Deployment encoding or per-probe surveyed site position. |
| Part 2 ControlStreams/Commands/Status only with actual supported classes, target and authorization. | At most bounded reference capability description; no executed command/asserted effect. | **G30-09:** executable management explicitly excluded from descriptive trial. |

**Important architectural stop:** Step 32 establishes **packet-internal mechanical expressibility**, not **portable CSAPI discovery or round-trip**. Neither publishing these JSON files at a GitHub path nor inventing a new `sourceStanding` key in a random SensorML extension would make an unknown client interoperable. The producer-advertisement mechanism, supported media type, link relation(s), format mapping, identity scope and actual server instance must be separately chosen and tested before Gate E can close. A project-owned extension could ultimately be justified, but its standing must remain explicit and it must not falsely claim an existing OGC requirement.

## 6. Falsification harness plan — two distinct validation layers

**Layer A: Step 32 packet/source checks (bounded input review).** Parse all five JSON documents; inspect their bounded schema shapes, source/member/derivation links and original event references; compare high-risk Bennett lexical fields, service periods and source row identities to the immutable [source selection](examples/bennetts-point-ee181.json). Confirm that the three manufacturer packets contain **no fabricated originalEvents/representations**, that `SOURCE_EXAMPLE` cannot silently become an actual event, and that two old scalar/archive resources point to each real NOAA report. These are **research fixture checks**, not evidence an API or common client has run.

**Layer B: planned Step 33+ unchanged reader and later OGC tests.** Implement one generic consumer which reads *the same contracted keys and assertion concepts* for all cases; it may display only source-supported data and must preserve unrecognized fields verbatim rather than reinterpret them via vendor names. Exercise source-positive and mutation-negative tests against **PR30-01/15/21**, while distinguishing a rejected invalid packet, a valid packet expressing UNKNOWN, a schema-valid but source-false assertion, and a source-faithful assertion lacking a valid CSAPI binding. The unchanged implementation must be challenged with at least two unlike evidence levels before calling any result generic.

| Planned oracle | Positive expectation for the *future* shared reader | Deliberate false mutation and expected treatment |
| --- | --- | --- |
| **S32-01 / C31-01 / PR30-01** | Reference Dragino/AirGradient/Campbell display **design/reference**; Bennett displays identified historical station and physical units. | Promote a published reference example to `SOURCE_IDENTIFIED_EQUIPMENT` without source-issued individual identity: reject as source-false; never invent a unit serial. |
| **S32-02 / C31-07–09** | One Dragino SHT31 with temperature and humidity; AirGradient PM1/PM2 sockets distinct from PM property field names; Campbell 14 response positions distinct from physical pieces and from logger PanelTemp. | Count fields as sensors or panel heat as outside air: reject qualified meaning, retain raw native field. |
| **S32-03 / C31-05/13** | Three Bennett day-scoped role-service statements; DERIVED 15-minute UTC period distinct from source stamp and UNKNOWN original resultTime. | Set swap to UTC midnight or `resultTime` to station stamp: fail source/temporal oracle, not repaired by format conversion. |
| **S32-04 / C31-14** | Exact Bennett `F_ATemp="<0> "` and separate blank `F_Record`; initial **parameter** QC only. | Trim the trailing space, treat blank row flag as QA pass or map it directly to native resultQuality without evidence: reject raw/source equivalence or hold claimed normative mapping. |
| **S32-05 / C31-15 / PR30-15** | Two unique original `source+edition+record+field` events; four experimental representations refer to those two, never counted as four source acts. | Duplicate source-event key or sever copy-to-original links: reject event semantics; no arbitrary timestamp-based deduplication. |
| **S32-06 / C31-15 / PR30-15** | Probe 4 contributes to the 15 Apr event, returning probe 3 to 18 Apr **only as DERIVED** from separate date history. | Swap contributor or label attribution NOAA original: reject source-oracle mismatch or false standing. |
| **S32-07 / C31-21 / PR30-21** | Unknown conditions remain unknown; no invented current config/status, extra installed reference hardware, or task execution. | Convert UNKNOWN to `false`, `0`, `null` or an asserted actual value: reject invalid claim shape or source-false interpretation. |
| **S32-08 / G30-01** | If future discovery works, an unknown compatible client locates and parses the packet without manufacturer-name/id-dependent rules. | A producer silently hides the packet, advertises unsupported media/class, or uses only a Bennett-specific URI: record **interoperability HOLD**, not PASS. |

**Actual Step 32 verification must state its limited level.** Structural JSON parsing and project consistency checks may pass without having executed JSON Schema tests through an independent library, and neither establishes source authenticity or standard-conformant CSAPI transformation. The later common interpreter, negative-mutation tests, native API encoding and live endpoint checks belong to subsequent steps; do not report them as performed in Step 32.

### Consumer invariants, independent of manufacturer string

1. Resolve `focus` to a source-declared subject and show its declared standing; packet and author-assigned keys are **not** manufacturer IDs.
2. Associate every known assertion with one original issuer/source locator and subject or original source event, preserving source-native lexical tokens where supplied. Reject broken pointers; preserve unknown/unrecognized concepts as raw labeled claims, not false general meanings.
3. Permit **SOURCE_FACT** assertions about manufacturer reference designs **only at design standing**; **SOURCE_EXAMPLE** values never become actual performed Observations.
4. Display **DERIVED** assertions with their source assertions and transformation; do not present them as operator-original. Treat `UNKNOWN` as explicitly unsupported, not a computed false/default/zero.
5. Use original **source-event identity**, not API Observation count, to count original reports. Multiple representations may refer to the same one source event; no statistical chart can double-count on that basis.
6. Reject provenance or time precision upgrades: calendar-day service cannot become an exact instant, a station stamp cannot become result availability, and a project period cannot become normative `phenomenonTime` without proven mapping.
7. Do not infer physical parts from output property count, version/firmware from source code commits, installed configuration from design defaults, or authorized Commands from documentation.

These are **future consumer acceptance predicates**, not Step 32 software implementation. The controlled `concept` values in the schema cover only a **small test vocabulary** linked to R24; they are **not** a pre-emptive final catalog of ontological classes. New original fields must remain available without manufacturing interpretation.

## 7. Completion boundary, risks and exactly what follows

**Step 32 is complete as a planned source-packet/design iteration when** (a) one candidate source-independent JSON Schema and four source-honest case packets exist; (b) original event identity, duplicate representation, original source time/quality, derivations and explicit UNKNOWNs are expressible; (c) the Step 32 source/structure checks are recorded without inflated runtime claims; (d) the future generic-reader positive/negative test design is explicit; and (e) this design and the cumulative workbook are linked from the controlling plan/README. It is **not contingent on Step 33's implementation**, and it does **not** close Gate E.

**The strongest unresolved risk is still G30-01.** We now have a *candidate packet structure* to test; **no accepted/discoverable native CSAPI carrier, standardized evidence-standing mapping or demonstrably source-independent consumer exists**. A packet could still turn out to be poorly bounded, unworkably verbose, source-lossy or wrong about a donor relationship when actual implementation begins. If that happens, revise the packet/Profile model and give a specific failure, not a hidden vendor adapter or invented source fact.

**NEXT ON A SEPARATE OWNER “PROCEED”: STEP 33 ONLY.** Implement one small, typed, **source-independent** reading path and a positive/negative test using this source packet contract, without manufacturer-name, file-name or hard-coded Bennett resource-ID branches, and preserving raw unknown fields. That step must not silently run all four future vendor cases, merge the application/research branches, claim OGC certification, publish a final source-evidence Profile, issue device commands, rewrite the Oracle/52°North service or trigger Cloudflare deployment merely because the fixtures exist. The rest of Phase F (Steps 34–39) and Phase G (Steps 40–43) remain separately pending.

**Research artifacts and original case evidence were unchanged by creating the packet fixtures.** The current [observation encoding decision](Observation_Encoding_Decision_31OCT2026.md), original [candidate Profile](CSAPI_Profile.md) and [DIM](DIM.md) remain qualified; this document supplements them, not retroactively adopting their draft proposals.
