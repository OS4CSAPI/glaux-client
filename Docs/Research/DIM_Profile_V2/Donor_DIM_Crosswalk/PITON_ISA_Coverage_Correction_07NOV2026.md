# Current PITON — communication, media and service selection complete

**8 November 2026 · Original ISA Step 5 of 12; four original steps COMPLETE. Accelerated delivery 4 COMPLETE. Commands 82/96 reviewed; 14 remain. Next “proceed”: ISA-COMMANDS-READOUT-HISTORY — seven assigned definitions only.**

Repository `OS4CSAPI/glaux-client`, branch `research/dim-profile-v2`, directory `Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/`. GitHub is authoritative.
[Plan](PLAN_ISA_Coverage_Correction_07NOV2026.md) · [Progress/exact queue](ISA_Correction_Status_07NOV2026.json) · [Comparison](ISA_Correction_Review_07NOV2026.md) · [Command evidence](ISA_Command_Catalogue_Evidence_07NOV2026.json) · [Coverage](ISA_Coverage_Register_07NOV2026.json) · [Workbook snapshot](ISA_Correction_Review_Observables_07NOV2026.xlsx) · [Workbook publication](ISA_Observables_Publication_Record_07NOV2026.json) · [Lessons](LESSONS_Donor_Review_Process.md).

## Earned progress
All 91 properties, 39 observables, their twelve-sheet workbook and 66 earlier command reviews remain COMPLETE. The 16 communication/media/service entries are now reviewed: all core, all supported, no new question. **Totals: 212 primary reviews / 206 supported / six unchanged questions; 239 information/review rows; 152 unique supporting definitions.** Original command owners ISA-05/06 now have 43/39 reviewed entries respectively. Their complete command/type/requirement packages are not falsely closed.

**Remaining forecast: 18 central prompted deliveries, working range 16–20.** Accelerated slot 4 completed without subdivision. Two command-source passes and one command-workbook checkpoint remain within this forecast. Technical iterations completed: 23. Retain original step numbers, earned increment and remaining forecast in closeouts; no new planning turn is due.

## Meaningful source distinctions
Add IP Address takes iface:String and address:IP Address; duplicate interface names are not allowed. The already reviewed IP Addresses property permits plus-sign subinterface naming for multiple addresses. Remove IP Address takes only iface:String; no unlisted address/mask/gateway field is added.

Discover queries currently available component messages, not future subscriptions. query:Data Query and include ucis:Boolean are required. The printed components:UCI list is Required0+ but included if requested; messages:Message is Required0+. Preserve the conditional prose and table together. Data Query has four optional message-content select clauses, required match clause, and required empty-capable with/without String lists; populated select clause is needed to receive that category. Function names, option vocabularies and whole message-envelope requirements are not invented or falsely marked reconciled.

Ping requests an ISA acknowledgement, not necessarily ICMP, a latency value or a health diagnosis. Recommend Video Stream takes original:URL and returns optional recommended:Resource Descriptor; possible transcoding is not guaranteed transcoding or completed transfer.

Service Notify distinguishes the sender’s provider input from optional recipient chosen result. Service Provider For Component queries a required provider result for a named service/consumer. The three Set service commands are recommendations; omitted service:UCI explicitly means no acceptable provider currently available. Service-name String parameters omit the word service as specified by the source. Sibling Service Providers and Trace Route preserve ordered visited lists, empty-capable result lists and optional ttl:Count as ISA-component distance, not seconds or IP packet TTL. Do not infer physical sibling relationships.

Start Data Input/Output SUCCESS means transfer started, not completed; names link to Data Inputs/Outputs. Output’s optional data name identifies the item and the prose says it is needed when multiple items could be transferred. Stop commands identify the transfer by name, not deletion of content or stopping all traffic. No actual network or equipment operation occurs.

## Actual source inspection and reuse
Primary DMS6.0r12 §3.3 text and page images37,51,56–64 inspected, including Start Data Output62–63 and Trace Route63–64. Original IP Addresses text27 checked; its image request failed, so no new visual-inspection claim for27. New dependencies: Boolean Wrapper66, Message72, Response Code132, and twenty filtering definitions across133–139. Filtering page133 text was available but its image was not; images134–139 and72 were inspected. Data Query, Boolean Function, Select and Field Value Selector cross-page definitions were followed. All23 new dependency records have field/variant manifests and locators, bringing the unique count from129 to152; later full-catalogue assignments stay separately tracked.

Known IP-address, resource, Count, URL, identity, transfer and scalar definitions were reused from exact-edition prior evidence. The query dependency work is saved for the forthcoming Discover/History/subscription and filtering reconciliation; do not research it again without a specific missing aspect. Original file ID `file_00000000ca1c81f48a3ccd49273425f8`; recover by exact title/revision if needed. Raw-byte/image access failures are not absence of readable original text.

## Next single group — accelerated slot 5
**ISA-COMMANDS-READOUT-HISTORY:** Create Zip Archive; Get Config; Get Last Operation State; Get Operation State History; Get Property; Get Status; History.
IDs: ISA-DMS-207,211,212,213,214,215,216. These seven remain unreviewed assignments. Inspect complete native inputs/results, temporal and staleness meanings, and necessary message/operation-state types. Reuse the saved query/response manifests. Update cumulative evidence, coverage, readable comparison and concise routing using the same assembler/workflow; no new per-group report, workflow, exporter or Excel release. Stop after the seven; no automatic advance to slot6.

## Preservation and boundaries
Excel remains the completed130-primary/157-row property/observable snapshot, SHA256 `68deb7b41c2fcfbf3350f7260929c560cfb81963246acaa0d3f134f1281b27a6`, with its original four questions. Current command text is newer and includes Q005/Q006; scheduled refresh is not failed publication. Preserve58 other-donor records,73 case facts,480 entries,279 source blocks,31 original row targets,25 earlier findings and every earlier comparison cell. New candidates are not automatic owner adoption of separate DIM classes.

Existing questions Level Q001,Link Loss Q002,Orientation Q003,Signal Strength Ratio Q004,Adjust Power Q005 and Rotation Rate Q006 remain exactly unchanged. Bennett retains two NOAA means/four representations and unknown original resultTime. No other donor,model adoption,Profile/UML,client/server/deployment or equipment operation. Broader donor-review Step16 follows this correction.

[Prior spatial/acquisition checkpoint](https://github.com/OS4CSAPI/glaux-client/blob/4ec2f8ef360f50a5aaf9174df1e67931c4ce9498/Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/PITON_ISA_Coverage_Correction_07NOV2026.md) retains history; its slot4-next routing is superseded here.
