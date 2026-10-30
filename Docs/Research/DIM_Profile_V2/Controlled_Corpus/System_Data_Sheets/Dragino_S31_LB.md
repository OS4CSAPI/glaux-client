# System Data Sheet C — Dragino S31-LB

**Version 0.1 · 30 October 2026 · America/New_York**  
**Reference case:** external three-metre SHT31 probe, primary-battery S31-LB node. **Not S31B or LS.**  
**Purpose:** Itemized working information for later Domain Information Model (DIM) / OGC API – Connected Systems (CSAPI) work. Research data sheet, not a manufacturer-issued datasheet.  
**Basis:** [C audit](../05_Candidate_C_Evidence_Audit.md), [selection](../07_Corpus_Qualification_Decision.md) and [handoff](../08_Frozen_Corpus_Manifest_and_Handoff.md), repository revision `315034c25326dc4a08ecc0629f8bf3a933abe092`. Qualification is unchanged.

## How to use this sheet

**Design** = `PRIMARY_DESIGN_OR_SPEC`; **Example** = `PRIMARY_PUBLISHED_EXAMPLE`; **Derived** = `SYNTHETIC_OR_DERIVED`; **Unknown** = `UNAVAILABLE_OR_UNVERIFIED`. All settings and values retain that evidence standing. **No real node identity, applied configuration or actual telemetry was obtained.** Source keys resolve in §9; byte positions below are zero-based.

The audited manual was reread to itemize its product-specific payloads, controls and power facts. This includes extraction detail beyond the audit's selected tables, not a new equipment qualification or a claim that every manual revision applies to the pinned decoder. Full generic LoRaWAN-stack commands, image-only mechanical detail and firmware packages are not comprehensively extracted.

## 1. Identity, construction, communication and technical limits

| ID | Item / subject | Available fact or source-native value | Evidence / locator | Boundary |
| --- | --- | --- | --- | --- |
| C-I01 | Model | S31-LB | Design; C01; C02 §1.8 | Do not import S31B integrated-probe or LS solar construction. |
| C-I02 | Probe | 1 × SHT31; external cable 3 m | Design; C02 §§1.2/1.8 | Temperature/humidity outputs do not create two physical probe identities. |
| C-I03 | Node / support | Enclosure, onboard electronics/radio and primary battery | Design; C audit §A | Gateway/server are external dependencies, not automatically node constituents. |
| C-I04 | Reference battery | 8,500 mAh Li/SOCl2; non-rechargeable | Design; C02 §§1.2/1.3 | Nameplate capacity, not remaining capacity. |
| C-I05 | Battery pack | ER26500 + SPC1520 | Design; C02 §4 | Named pack; no installed serial, replacement or tested capacity. |
| C-I06 | Supply range | 2.5–3.6 V | Design; C02 §1.3 | Not a measured voltage. |
| C-I07 | Equipment operating temperature | −40 to 85°C | Design; C02 §1.3 | Separate from measured temperature and sensor range. |
| C-I08 | Temperature range / resolution | −40 to +80°C / 0.1°C | Design; C02 §1.3 | Specification, not observed performance. |
| C-I09 | Temperature accuracy statement | ±0.2 @ 0–90°C, as printed | Design; C02 §1.3 | Printed interval extends beyond printed range; no silent correction. |
| C-I10 | Humidity range / resolution | 0–99.9% RH / 0.01% RH | Design; C02 §1.3 | Payload scaling separately yields 0.1 increments; do not equate resolutions. |
| C-I11 | Humidity accuracy statement | ±2% RH (0–100% RH) | Design; C02 §1.3 | No independent calibration verification. |
| C-I12 | LoRaWAN | 1.0.3 Class A; default OTAA joining | Design; C02 §§1.2/2.1 | Supported/default behavior, not an observed connection. |
| C-I13 | Radio variants | CN470, EU433, KR920, US915, EU868, AS923, AU915, IN865 listed | Design; C02 §1.2 | No particular regional variant selected or authenticated. |
| C-I14 | Configuration links | Bluetooth 5.1 / UART AT commands / LoRaWAN downlink | Design; C02 §§1.2/3.1 | No commands sent; no active interface inferred. |
| C-I15 | Join identity | Device EUI / registration keys described | Design; C02 §§1.1/2.2 | No device EUI, AppKey or credentials obtained or published. |
| C-I16 | Firmware / region | Different regional firmware described; deployed values unknown | Unknown installed values; C02 §§2.7/2.8; C audit §A | Decoder filename v1.3 is not deployed firmware 1.3. |
| C-I17 | Decoder snapshot | 635417693adb215b32ac367c8e8909d9d609a120 | Design; C03; blob 59af776a4b7ce287dc4c3030763e215b31f645f8 | Implementation evidence; not complete firmware compatibility. |

## 2. Power and operating behavior

| ID | Subject | Documented information | Evidence / locator | Limit |
| --- | --- | --- | --- | --- |
| C-P01 | Sleep consumption | 5 µA at 3.3 V | Design; C02 §1.3 | Not measured in this work. |
| C-P02 | Transmit consumption | 125 mA at 20 dBm; 82 mA at 14 dBm | Design; C02 §1.3 | Do not infer average drain without duty-cycle evidence. |
| C-P03 | Battery self-discharge | <1%/year at 25°C | Design; C02 §1.3 | Source rating; no age/condition record. |
| C-P04 | Battery current ratings | 130 mA continuous; 2 A boost for 1 second | Design; C02 §1.3 | Not an operating current measurement. |
| C-P05 | Battery voltage / capacity | Non-linear relationship; not a simple remaining-percentage conversion | Design; C04 §§1.1/1.3/4.0; C audit §F | No estimator or autonomy calculation adopted. |
| C-O01 | Deep Sleep Mode | Storage/shipping mode without LoRaWAN activity | Design; C02 §1.4 | No observed mode. |
| C-O02 | Working / IDLE | Join and sample/transmit; IDLE between activities | Design; C02 §1.4 | Source equates IDLE and deep-sleep consumption; not a test. |
| C-O03 | Default uplink | 20 minutes | Design; C02 §2.1 | Command examples use different illustrative intervals. |
| C-O04 | ACT 1–3 s | Joined node requests uplink; blue blink; BLE becomes available | Design; C02 §1.5 | Not an observed action. |
| C-O05 | ACT >3 s | Activation; green fast ×5; 3-second OTA window; join sequence | Design; C02 §1.5 | Quick-start separately says hold 5 s; no enforced timing contract inferred. |
| C-O06 | ACT ×5 | Deactivate; red indication 5 s; deep sleep | Design; C02 §1.5 | Not actual state. |
| C-O07 | BLE availability | On activation/uplink-button/power/reset; idle connection window 60 s | Design; C02 §1.6 | Not continuous remote-management availability. |
| C-O08 | Datalog prerequisite | SYNCMOD=1 and PNACKMD=1 described | Design; C02 §2.5.2 | No actual settings read. |
| C-O09 | Time synchronization | DeviceTimeReq/DeviceTimeAns; internal time if no reply; SYNCTDC default 10 days | Design; C02 §2.5.2 | Network support and time validity not demonstrated. |
| C-O10 | Unacknowledged history | Non-ACK records retained and later resent; 10 s recovery spacing described | Design; C02 §2.5.1 | No proof of delivery success or complete retained history. |
| C-O11 | No matching history | 11 zero bytes documented as no-data reply | Design; C02 §2.5.4 | Not eight zero-valued environmental observations. |
| C-O12 | Firmware servicing | Wireless OTA or UART/TTL methods described | Design; C02 §5 | No package downloaded, flashed or verified. |

## 3. Native message and decoder field inventory

**Source definitions:** C02 §§2.3–2.5; **implementation:** C03 `Decoder`, `datalog`, `getMyDate`. Values in the full original history example are in §4. Other values below are absent unless explicitly labeled scalar examples. All messages lack an authenticated physical-unit join in this evidence set.

### FPort 2 — sampling message, mode bits equal 0

All output fields below are covered; source bytes describe the node/probe report. The decoder uses `(bytes[6] & 0x7C) >> 2` for mode selection.

| ID | Native output / bytes | Type / unit | Meaning / available example | Boundary |
| --- | --- | --- | --- | --- |
| C-F01 | BatV / 0–1 | number / V | Unsigned integer ÷1000; manual scalar 0x0B45 = 2885 mV | No complete original FPort-2 packet acquired. |
| C-F02 | Data_time / 2–5 | string; underlying epoch seconds | Unsigned 32-bit epoch rendered by local date functions | Calendar string has no offset; do not label UTC unconditionally. |
| C-F03 | EXTI_Trigger / byte 6 bit 0 | string TRUE/FALSE | Decoder label; manual calls it alarm/interrupt flag | Do not infer only an external interrupt caused the flag. |
| C-F04 | Door_status / byte 6 bit 7 | string CLOSE/OPEN | Decoder convenience label for input flag | No installed door contact established. |
| C-F05 | TempC_SHT31 / 7–8 | number / °C | Signed 16-bit ÷10; scalar examples 0x0105 →26.1; 0xFF3F →−19.3 | Scalar examples are not a complete device record. |
| C-F06 | Hum_SHT31 / 9–10 | number / % RH | Unsigned 16-bit ÷10; 0x0197 →40.7 | Manual also prints 412; actual hexadecimal conversion is 407. |
| C-F07 | Node_type | string S31-LB | Hard-coded decoder output | Not verified model identification or unique identity. |

### FPort 2 — alarm-settings reply, mode bits equal decimal 31

| ID | Native output / bytes | Type / unit | Meaning | Available value |
| --- | --- | --- | --- | --- |
| C-T01 | SHTEMP_MIN / 7 | signed 8-bit / °C | Lower temperature threshold | No original reply value acquired. |
| C-T02 | SHTEMP_MAX / 8 | signed 8-bit / °C | Upper temperature threshold | No original reply value acquired. |
| C-T03 | SHHUM_MIN / 9 | unsigned 8-bit / % RH | Lower humidity threshold | No original reply value acquired. |
| C-T04 | SHHUM_MAX / 10 | unsigned 8-bit / % RH | Upper humidity threshold | No original reply value acquired. |

The reply also contains the hard-coded `Node_type` already listed at C-F07. Documentation prints `0x7C >> 2 = 0x31`; the audit's independent calculation is decimal 31 / hexadecimal 0x1F, matching the code's decimal comparison. Both source statement and check remain recorded.

### FPort 3 — historical records

| ID | Native input/output | Type / unit | Meaning / availability | Boundary |
| --- | --- | --- | --- | --- |
| C-H01 | Entry bytes 0–1 | two bytes | Documented ignore; C03 does not use them | Not battery-voltage zero. |
| C-H02 | Entry bytes 2–3 | scaled integer / % RH | Humidity ÷10; values in §4 | C03 applies signed arithmetic; tested only on retained positive examples. |
| C-H03 | Entry bytes 4–5 | signed integer / °C | Temperature ÷10; values in §4 | Not a separate physical sensor inventory. |
| C-H04 | Entry byte 6 | bit flags | Poll / alarm / PA8 context; all original entries 0x40 | Retain raw flag; do not infer delivery success. |
| C-H05 | Entry bytes 7–10 | unsigned integer / seconds | Unix epoch; values in §4 | Original epoch retained separately from rendered calendar string. |
| C-H06 | DATALOG | string | Concatenated bracketed entries with trailing comma | Not a JSON array of typed records. |
| C-H07 | PNACKMD | string True/False | Reads first entry high bit in decoder | Not a queried configuration or all-entries delivery result. |
| C-H08 | Node_type | string S31-LB | Same hard-coded label as C-F07 | No physical identity evidence. |

### FPort 5 — device-status structure

| ID | Native output / bytes | Type / unit | Meaning / source example | Boundary |
| --- | --- | --- | --- | --- |
| C-S01 | SENSOR_MODEL / 0 | string | Code 0x0A recognized as S31-LB | Manual applies code to family; no variant identity proven. |
| C-S02 | FIRMWARE_VERSION / 1–2 | string | Nibble-based version; scalar 0x0100 means 1.0.0 | No actual firmware response obtained. |
| C-S03 | FREQUENCY_BAND / 3 | string | Band code decoded by C03 | No installed regional variant. |
| C-S04 | SUB_BAND / 4 | number or string NULL | C03 returns NULL string for 0xFF, else byte value | Manual band restrictions are not a captured setting. |
| C-S05 | BAT / 5–6 | number / V | Unsigned integer ÷1000; scalar 0x0B45 / 0x0B49 = 2.885 / 2.889 V | Voltage, not remaining charge or readiness. |

C-S03 code dictionary from the pinned decoder: `01 EU868; 02 US915; 03 IN865; 04 AU915; 05 KZ865; 06 RU864; 07 AS923; 08 AS923_1; 09 AS923_2; 0A AS923_3; 0B CN470; 0C EU433; 0D KR920; 0E MA869; 0F AS923_4`. These are hexadecimal codes and code-defined strings, not proof that every physical product is sold/configured for every listed band. The manual's spellings/range discussion remain separate.

## 4. Every record in the original published history example

**Origin:** C02 §2.5.4, 88 bytes / eight 11-byte entries embedded in the unchanged [checker](../05_Dragino_Example_Check.cjs). **Evidence:** Example bytes; the numerical expansion and UTC formatting below are Derived, not new measurements. All entries have ignored leading bytes `00 00` and raw flag `40` (hex).

| ID | Original 11 bytes (hex) | Humidity % RH | Temperature °C | Epoch seconds | UTC rendering |
| --- | --- | --- | --- | --- | --- |
| C-E01 | 00 00 02 36 01 10 40 64 6D 84 E1 | 56.6 | 27.2 | 1684899041 | 2023-05-24T03:30:41Z |
| C-E02 | 00 00 02 37 01 10 40 64 6D 84 F8 | 56.7 | 27.2 | 1684899064 | 2023-05-24T03:31:04Z |
| C-E03 | 00 00 02 37 01 0F 40 64 6D 85 04 | 56.7 | 27.1 | 1684899076 | 2023-05-24T03:31:16Z |
| C-E04 | 00 00 02 3A 01 0F 40 64 6D 85 18 | 57.0 | 27.1 | 1684899096 | 2023-05-24T03:31:36Z |
| C-E05 | 00 00 02 3C 01 0F 40 64 6D 85 36 | 57.2 | 27.1 | 1684899126 | 2023-05-24T03:32:06Z |
| C-E06 | 00 00 02 3D 01 0E 40 64 6D 85 3F | 57.3 | 27.0 | 1684899135 | 2023-05-24T03:32:15Z |
| C-E07 | 00 00 02 3F 01 0E 40 64 6D 85 60 | 57.5 | 27.0 | 1684899168 | 2023-05-24T03:32:48Z |
| C-E08 | 00 00 02 40 01 0E 40 64 6D 85 6A | 57.6 | 27.0 | 1684899178 | 2023-05-24T03:32:58Z |

No absolute location, unique node, firmware version or regional band is present in these entry bodies. The published polling request is `31646D84E1646D856C05`; it supplies a start/stop interval, not a device identity. In the earlier checker, the same first epoch rendered `2023-05-24 03:30:41` under UTC and `2023-05-23 23:30:41` under America/New_York; that remains a decoder-context issue.

## 5. Configuration and command inventory

All rows below are **Design / Example** from C02, not a list of actions performed. `OK` in a printed command example is not a captured acknowledgement from our equipment. Calibration commands reflect the mutable manual as reread; applicability to any deployed firmware remains unverified.

| ID | Native command / field | Information supplied | Unit / source locator | Use boundary |
| --- | --- | --- | --- | --- |
| C-C01 | AT+TDC | Transmit interval; example 60000; downlink 0100003C | AT milliseconds; downlink seconds; §3.3.1 | Retain different unit conventions. |
| C-C02 | 0x26 01 | Request device status; reply FPort 5 | §§2.3.1/3.3.2 | Section prose also says alarm settings; FPort-5 structure retained separately. |
| C-C03 | AT+SHTEMP=min,max | Temperature thresholds; example 0,30; downlink 0C01001E | °C; §3.3.3 | Zero disables that bound under stated rules; no active setting. |
| C-C04 | AT+SHHUM=min,max | Humidity thresholds; example 70,0; downlink 0C024600 | % RH; §3.3.4 | Printed downlink comment uses SHTHUM; do not silently rename command. |
| C-C05 | AT+ATDC | Minimum alarm spacing; example 30; downlink 0D001E | minutes; §3.3.5 | Not measured notification latency. |
| C-C06 | 0x0E 01 | Request alarm settings; mode-31 reply | §3.3.6 | No original complete reply acquired. |
| C-C07 | AT+INTMOD | 0 disabled / digital input; 1 both edges; 2 falling; 3 rising | code; §3.3.7 | Input function does not prove a door sensor. |
| C-C08 | AT+5VT | 5-V output duration; default 0; example 1000; downlink 0701F4 means 500 | milliseconds; §3.3.8 | Supported output control, not an observed 5-V measurement. |
| C-C09 | AT+PDTA | Print stored pages; example 1,3; stated maximum 416 pages | page index; §3.3.9 | No downlink equivalent stated; old console sample not used as this node inventory. |
| C-C10 | AT+PLDTA | Print last entries; example 5 | entry count; §3.3.10 | Console example includes ds temp; do not invent an extra installed probe. |
| C-C11 | AT+CLRDTA | Clear datalog flash | §3.3.11 | Described only; not invoked. |
| C-C12 | AT+2PCATEMP=R1,S1,R2,S2 | Two-point temperature calibration; example 0,5,500,498 | integer tenths °C; §3.3.12.1 | Command description; no calibration performed. |
| C-C13 | AT+2PCALHUM=R1,S1,R2,S2 | Two-point humidity calibration; example 200,205,800,795 | integer tenths % RH; §3.3.12.2 | Command description; no calibration performed. |
| C-C14 | Calibration query / validation | Query with =?; no configured calibration example 0,0,0,0; S1/S2 distinct and not both zero | §3.3.12.1–3 | Default/no-calibration marker, not environmental zero. |
| C-C15 | SYNCMOD | 1 enables MAC time synchronization; documented default 1 | §2.5.2 | No actual queried setting. |
| C-C16 | PNACKMD | 1 enables documented datalog behavior | §2.5.2 | Do not equate with decoder string from a historical bit. |
| C-C17 | AT+SYNCTDC | Time-request period; stated default 10 days | §2.5.2 | Detailed generic command encoding not extracted. |
| C-C18 | Historical polling request | 31646D84E1646D856C05; first/last epoch and interval command example | §2.5.4 | Documentary request, not sent by this research. |

## 6. Synthetic checks kept outside original source observations

The prior checker also constructs measurement, alarm-setting, status and no-data inputs. Its status values `1.0.0`, `EU868`, and `2.885 V` arise from analyst-supplied bytes. They are **Derived test fixtures**, not discovered installed state. The constructed all-zero history message decodes to apparent zeros and a 1970 date; its purpose is to expose an absence-handling hazard, not supply an observation. Unsupported-port behavior was checked, not exhaustive decoder robustness. These fixtures remain in the original checker; they do not replace the original §4 evidence.

## 7. Starting references for power/condition work

Use **C-I04–I06**, **C-P01–P05**, **C-O01–O03/O08–O11**, **C-F01/F03/F04**, **C-S05**, and **C-C08** as the available power/condition-related input list. Keep battery design capacity, voltage, output-duration setting, alarm/input flags and communication history separate. The historical leading zero bytes do **not** supply a battery measurement. This shortlist does not adopt model categories or exclude other whole-System rows.

## 8. Gaps and unavailable material

| ID | Gap | Handling |
| --- | --- | --- |
| C-G01 | Authenticated installed unit, region, firmware, board revision | Unknown; no example or decoder name fills this gap. |
| C-G02 | Original full FPort-2/FPort-5/alarm-reply records | Definitions and scalar examples only; prior image-only examples not acquired. |
| C-G03 | Real operating history, current configuration, diagnostics and command outcomes | No qualifying records; actual-history coverage remains zero. |
| C-G04 | Pin/mechanical drawing dimensions and complete hardware schematic | Not extracted; do not guess from product family. |
| C-G05 | Firmware/changelog folder contents | Earlier access gap retained; no release contract inferred. |
| C-G06 | Generic stack commands and old console-sample applicability | Not completely extracted; ds temp does not establish an S31-LB part. |
| C-G07 | Battery estimator, autonomy, calibration certificate and source timestamp accuracy | Not established. |
| C-G08 | Decoder redistribution license | Not verified; source code stays an external dependency. |

## 9. Sources and preservation

Source IDs remain those of C audit §B. Current manual re-extraction: **30 October 2026, America/New_York**. The decoder's known commit/blob is retained, not upgraded to latest main. This sheet contains factual field/value/command inventories, not the manufacturer manual or decoder source.

- **C01:** Dragino, [S31-LB/LS product page](https://dragino.com/products/temperature-humidity-sensor/item/264-s31-lb-ls.html), construction as preserved in C audit §A.
- **C02:** Dragino, [S31/S31B-LB/LS manual](https://wiki.dragino.com/docs/LoRaWAN-End-Node/temperature-humidity-sensors/s31-lb/), exact numbered sections above; mutable HTML reread. Model-family coverage does not authenticate an example's physical source.
- **C03:** Dragino, [S31-LB_v1.3_TTN_decoder.txt at 6354176](https://github.com/dragino/dragino-end-node-decoder/blob/635417693adb215b32ac367c8e8909d9d609a120/S31-LB%26S31B-LB/S31-LB_v1.3_TTN_decoder.txt), Decoder / datalog / getMyDate. Blob `59af776a4b7ce287dc4c3030763e215b31f645f8`; precise prior inspection in C audit §E.
- **C04:** Dragino, [battery-life guidance](https://wiki.dragino.com/docs/FAQs/battery-life-calculation/), §§1.1/1.3/4.0 as qualified in C audit.
- **C05–C06:** Hardware-family and uninspected firmware-folder leads remain in [C audit §B](../05_Candidate_C_Evidence_Audit.md#b-primary-sources-provenance-and-access); not positive installed-version evidence.

The history bytes remain embedded in the unchanged checker; their SHA-256 is `a8d229062fd2aa1e4a34b04a07be8cdd85e7a7f7dd65f97fd54dfbd9fa2ac298`. §4 was independently recalculated from those bytes during this consolidation. No new decoder repair, command, hardware test, source qualification, DIM or Profile change occurred.
