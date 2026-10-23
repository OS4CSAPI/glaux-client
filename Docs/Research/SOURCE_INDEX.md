# Details View source index

This index pins the sources used for the first Overview, Equipment, and Condition
increment. It records references and source locations so the implementation can be
reviewed without relying on a conversation. Original documents, manufacturer
manuals, research archives, and private transcripts are retained outside this
public repository.

The local citation keys below identify this implementation's sources. They do not
allocate identifiers in the MERLIN master bibliography or change its records.
The [view mapping](../Design/DETAILS_VIEW_MAPPING.md) distinguishes existing MPSS
rules from experiment-specific interpretation. The
[acceptance criteria](../Testing/DETAILS_VIEW_ACCEPTANCE.md) define the checks;
their presence is not a report that the implementation passed them.

## Sources read for this increment

| Local key | Exact source and version | Relevant locations and role |
| --- | --- | --- |
| `SRC-PROFILE` | `MERLIN_Managed_Physical_Sensing_Systems_Profile_Integrated_Binding_Draft_v0.3.5_17OCT2026.docx` | Sections 5.2-5.6: declaration, namespace, references, group contracts, identity and equipment. R11 in section 5.8: producer, subject and temporal context. R17 in section 5.10: quantity and estimate meaning. R20 in section 5.11: qualifying condition findings. Section 6.10: limited battery-voltage illustration. Section 7: presentation is not a mandatory domain-tab layout. |
| `SRC-CATALOGUE` | `domain_catalogue.json` within `MPSS_v0.3.5_example/` | Exact group and term identifiers, value kinds, profile scopes, authored versus translated meanings, and R11/R17 interpretation rules. It is a working example catalogue, not a published vocabulary. |
| `SRC-EXAMPLES` | `MERLIN_Profile_v0.3.5_Connected_Example_and_Definitions_17OCT2026.zip` | `01_model.sml.json` and `02_station.sml.json`: actual JSON group shapes and qualified references. `16_power_stream.json`, `17_power_schema.json`, `18_power_observation.json`: separate producer, observed subject, schema and observation. `31`-`33` plus `R17_BATTERY_VOLTAGE_MAPPING_CASE.md`: the qualified RFC 7577 illustration. The fictional station supplies no facts about TRSS or OmniSense. |
| `SRC-REQUIREMENTS` | `MERLIN_Resource_Details_Requirements_v0.8_08OCT2026.docx`, v0.8, amended 9 October 2026 | RD-C01-11: identity, tabs, disclosure, accessibility, partial retrieval, time and source inspection. RD-S01-03: marking context. RD-V02 and RD-V08: typed values and qualified estimates. RD-SYS-2/3/4/9: grouped descriptions, location, relationships and inheritance. The older Details > Summary proposal is reconciled in the mapping companion. |
| `SRC-GUIDE` | `MERLIN_Semantic_Presentation_and_Interaction_Guide_v0.5.docx` | Sections 2-3: separate source meaning, presentation meaning and rendering. Sections 10.1.1-10.1.7: System identity, location, condition, relationships, typed fallback and inherited-value provenance. |
| `SRC-VIEWS` | `MERLIN_System_Details_Working_Views_10OCT2026.pdf`, inspected 55-page version | Page 22: TRSS estimate. Page 23: separate Core 5 ADS voltage/test report. Pages 35-40: Operational > Overview and source-qualified facts. Pages 50-51: distinct Mission and Sensor string labels supersede the umbrella Assignment proposal. Page 52: TRSS configured detector types. Page 53: Core 2 reported transducers. Pages 54-55: equipment bindings and remaining gaps. Page numbers are PDF page numbers. The filename's date does not describe every appended review page. |

The source package holding the current profile and examples was
`MERLIN_OSCAR_Mapping_and_Gap_Research_COMPLETE_v1.0_22OCT2026.zip`. Its OSCAR case
and broader research were not substituted for the Details View sources. Only the
needed profile, catalogue and connected examples were used from that package.

## Selected example locators

| Example | Source locations | Literal content and boundary |
| --- | --- | --- |
| TRSS ETU-II | `SRC-VIEWS` page 22 for Condition; pages 35-40 and 50-51 for Overview; pages 52-55 and embedded equipment facts for Equipment. | Sensor string is MM101; Mission is not supplied. Detector selections and estimator inputs remain distinct from confirmed attachments and measured values. |
| OmniSense Core 2 | `SRC-VIEWS` pages 35-40 and 50-51 for Overview; page 53 and embedded equipment facts for Equipment. | Preserve the reported labels: Magnetic; Seismic (ext); Detection Switch 1; Detection Switch 2; Control Switch. No matching Condition report, Mission or Sensor string is supplied for this case. |
| OmniSense Core 5 ADS | `SRC-VIEWS` page 23. | A separate Condition example: 15.43 V DC, literal unverified clock `12/30/99 05:00:00`, source mode/interval/on-time and six individual Pass findings. It does not supply Core 2 condition. |
| Synthetic MPSS technical description | `SRC-PROFILE` sections 5.3, 5.5 and R01; `SRC-CATALOGUE`; `SRC-EXAMPLES` files 01-02 for the contract. | All technical fixture values are invented test data. The group contract is source-derived; manufacturer/device evidence is not claimed. |

The nil-value boundary follows `SRC-PROFILE` R17 and the qualified example
`33_battery_voltage_result_schema.json`: a declared nil token must retain its
reason and cannot become a physical reading. That example does not make its
particular token universal. The `EP` Category code spaces and carrier choices
are authored experiment contracts recorded in the mapping companion, not values
discovered in a native TRSS or OmniSense schema.

## Source fingerprints

SHA-256 values pin the exact bytes inspected. A changed file with the same name
requires a new source comparison; it should not silently inherit this index's
findings.

| Source | SHA-256 |
| --- | --- |
| `SRC-PROFILE` | `8096648ea481822ae7f98fd5bdd1443851b4bcf47556392de5a713a3b6ffa4f8` |
| `SRC-CATALOGUE` | `1f974ed2428e696efc0cb7cfe7193062c6493278ea7fcdf4df0fdad121823837` |
| `SRC-EXAMPLES` ZIP | `b45c7ce801adafb939e5f48231fd85a9dbae13ef6d3ce528a3fc1c7b0ce94b1f` |
| `SRC-REQUIREMENTS` | `56ec9b209f901e09d1221a5b4710a69f69ce3953033cd64f8883e3c495e59935` |
| `SRC-GUIDE` | `90bf51ce42c0c0b658aecef84a25d331425e8b923825310ef456779db06f1b95` |
| `SRC-VIEWS` | `38641d4fd1c436cda93c56e52f1c007c8b44793a687bc2e38b9800538699eaad` |

## Embedded evidence used

The working-view PDF contains its own review transcriptions. These are useful
evidence for the prior presentation decisions, not recovered manufacturer API
responses. They were read outside the repository; their original files are not
published here.

| Embedded filename | Use | SHA-256 |
| --- | --- | --- |
| `equipment_review_facts.json` | Selected TRSS detector values, supported choices, all five Core 2 transducer labels, and their qualifications. | `4f762ee829be15ffddc249f453d170b0b182c2bfffb3cd38f17a8e6e06df89f5` |
| `location_review_facts.json` | Source coordinate forms, missing reference/time information and unconfirmed Core 2 fix. | `d2e24d6dccf01f193a8424c1de6f6194ec0d6da27b7e8d85a847b7d28ff4ff99` |
| `relationship_review_facts.json` | Separate mission/string concepts and the limits of inferred membership, actor and time. | `2f70d06e996188cdff98d7af3f09ca16c2075fdb162a16dfc95a17b0d6e77cee` |

Historical check results embedded in the PDF concern earlier review artifacts.
They do not establish that this repository's implementation passes its tests.

## Manufacturer evidence traced through the working views

| Evidence named by the working packet | Relevant locator | Scope of this increment's access |
| --- | --- | --- |
| TRSS screenshot deck, Sentinel 1.0.7.2 Software Users Manual | Slides 10-11: General tab, detector selections and position. Slides 14-15: Battery Life estimate. The requirements record source code `N65236-TRSS-SUM-0005-2.00` and visible edition date 31 July 2014. | The working-view pages and embedded transcriptions were inspected. This increment does not claim a fresh audit of the complete manufacturer manual or a native TRSS payload. |
| SADU/OmniSense screenshot deck, OmniSense Central Computer Manual | Slides 1-6: Core 2; slide 6 and manual section 6.1.6.1/Figure 6-7: transducers. Slides 17-18/Figure 6-25: the separate Core 5 ADS status example. | The working-view pages and transcriptions were inspected. Missing edition, clock, schema and endpoint details remain unresolved. |

## Public standard and library references

These links identify the standards and implementation sources associated with the
retained contracts. Referencing them does not establish implementation conformance
or make a locally authored mapping an originating-standard requirement.

- [OGC API - Connected Systems Part 1, OGC 23-001](https://docs.ogc.org/is/23-001/23-001.html): System, Procedure, component/Deployment and Property mechanisms.
- [OGC API - Connected Systems Part 2, OGC 23-002](https://docs.ogc.org/is/23-002/23-002.html): stream, schema and observation mechanisms cited by the profile.
- [SensorML 3.0 JSON schemas](https://schemas.opengis.net/sensorML/3.0/json/): native descriptions and typed group carriers.
- [SWE Common 3.0 JSON schemas](https://schemas.opengis.net/sweCommon/3.0/json/): component types, quantities, categories, records and nil values.
- [RFC 6906](https://www.rfc-editor.org/rfc/rfc6906.html): the profile link relation.
- [RFC 8348, section 7.1](https://www.rfc-editor.org/rfc/rfc8348.html#section-7.1): source meanings informing MPSS technical-description terms; the MPSS JSON binding is authored work.
- [RFC 7577, section 5](https://www.rfc-editor.org/rfc/rfc7577.html#section-5): the separately qualified batteryActualVoltage illustration. It supplies no OmniSense binding.
- [Pinned CSAPI library and build provenance](../DEPENDENCIES.md): exact selected revision and reproducible build arrangement.

Return to the [documentation index](../README.md).
