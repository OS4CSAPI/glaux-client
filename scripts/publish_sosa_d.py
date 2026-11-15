#!/usr/bin/env python3
"""Reusable canonical SOSA workbook snapshot publisher; preserve all 26 tabs and source holds.
Reuses the existing proven ISA22 ZIP/XML helpers; file/cell verification only.
"""
import csv,hashlib,io,json,re,sys,textwrap,zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
sys.path.insert(0,str(Path(__file__).resolve().parent))
import isa22_closeout as old
D=Path(__file__).resolve().parents[1]/"Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk"
BOOK="Master_Donor_Concept_to_DIM_Crosswalk.xlsx"
MASTER="Master_Donor_Concept_to_DIM_Crosswalk.json"
LEDGER="Step17_SOSA_D_Source_First_Integration_09NOV2026.json"
REPORT="SOSA_G2_7K_Workbook_Validation_11NOV2026.json"
PREVIEW="SOSA_G2_7K_Workbook_Preview_11NOV2026.png"
OLD="8a962811eb1d6243156c3efb8b40ce874a42ae58dcc96f08203b0b9287e3de52"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-G2-7K verification failed: "+message
def load(n):return json.loads((D/n).read_text(encoding="utf-8"))
def save(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def digest(b):return hashlib.sha256(b).hexdigest()
def source_csv(n):
    with (D/n).open(encoding="utf-8-sig",newline="") as f:return list(csv.reader(f))
def addr(i,j):return old.coord(i,j)



def check_source(m,l):
    need(m["schemaVersion"]=="0.15" and len(m["rows"])==329 and len(m["columns"])==15,"original 329 rows and 15 columns")
    need([x["key"] for x in m["columns"]][:4]==["Dragino","AirGradient","Campbell","Bennett"]
         and [x["key"] for x in m["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
         and m["columns"][-1]["key"]=="DIM","approved case/donor/OGC/DIM order")
    grid=m["review_grid"]
    need(len(grid)==346 and all(len(x)==15 for x in grid) and len(m["review_sections"])==15,"original 346x15 source grid")
    need([r for i,r in enumerate(grid) if i>1 and i not in set(m["review_sections"])]==[r["display"] for r in m["rows"]],"original row/source grid equality")
    need(grid==source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")
              ==source_csv("ISA_Correction_Review_07NOV2026.csv"),"both CSV exact current source")
    a=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    b=(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    need(a.split("<table>",1)[1]==b.split("<table>",1)[1]
         and a.count('colspan="15"')==15,"two identical readable comparisons and 15 topic groups")
    need(len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73
         and m["ISAEvidence"]["currentPrimaryReviews"]==480 and m["ISAEvidence"]["specificQuestions"]==6,
         "preserve 58 donor, 73 case, 480 ISA source reviews/six questions")
    need(len(l["all_57_qualified_source_decisions"])==57 and len(l["integration_row_ledger"])==38,
         "earlier SOSA-D source contributions retained")
    prior={"SOSA_G2_1_Original_Item_Inventory_09NOV2026.json":201,
           "SOSA_G2_2_Original_Item_Inventory_09NOV2026.json":352,
           "SOSA_G2_3_Original_Source_Item_Census_09NOV2026.json":119,
           "SOSA_G2_4A_Original_Source_Item_Coverage_10NOV2026.json":95,
           "SOSA_G2_4B_Original_Source_Item_Coverage_10NOV2026.json":234,
           "SOSA_G2_5_Original_Source_Item_Coverage_10NOV2026.json":164}
    for file,n in prior.items():
        doc=load(file)
        if "items" in doc: found=len(doc["items"])
        elif "source_items" in doc: found=len(doc["source_items"])+len(doc.get("original_rule_appearances",[]))
        elif "original_source_items" in doc: found=len(doc["original_source_items"])
        else: found=doc["counts"]["source_items"]
        need(found==n,"preserve prior C239 original source corpus "+file)
    g=load("SOSA_G2_6A_Original_Source_Item_Coverage_10NOV2026.json")
    c=g["source_counts"];all_items=g["original_source_items"];ids={x["id"] for x in all_items}
    need(len(g["original_toc_heading_coverage"])==13 and len(g["additional_native_subclauses_read"])==19
         and len(all_items)==168 and len(ids)==168,"13 original headings/19 nested/168 distinct source/analysis records")
    need(c["RULE"]==98 and c["PERMISSION"]==8 and c["RECOMMENDATION"]==3 and c["OBSERVATION"]==21
         and c["TABLE"]==10 and c["FIGURE"]==5 and c["COV_FIELD"]==11
         and c["ANALYTICAL_CONTEXT"]==12,"98 Rules/8 Permissions/3 Recommendations/21 Observations plus native tables/CoV and contexts")
    need(g["C239_cumulative_coverage"]["at_least_source_sampled_or_inline_read"]==149
         and g["C239_cumulative_coverage"]["substantively_unread"]==42
         and g["C239_cumulative_coverage"]["restricted"]==1,"honest original source coverage")
    need(not g["source"]["native_ANSI_VITA_companions_read"]
         and not g["source"]["C239_DSDM_IDL_OpenAPI_8_files_read"]
         and not g["source"]["figure_pixels_audited"],"unread source companion and figure holds preserved")
    for count,name in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
         (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence"),
         (29,"G2_4B_source_correspondence"),(43,"G2_5_source_correspondence")):
        need(sum(bool(r.get(name)) for r in m["rows"])==count,"prior donor source contributions preserved "+name)
    updated=[r for r in m["rows"] if r.get("G2_6A_source_correspondence")]
    need(len(updated)==39 and {r["row_id"] for r in updated}==set(m["workbookSnapshot"]["G2_6A_affected_row_ids"]),
         "39 original source-qualified hardware comparisons")
    for row in updated:
        e=row["G2_6A_source_correspondence"]
        need(e["source_item_ids"] and all(v in ids for v in e["source_item_ids"]),"native source item IDs "+row["row_id"])
        need(e["DIM_Profile_adopted"] is False and e["native_VITA_and_DSDM_companions_unreviewed"],
             "no model adoption or unwarranted native original claims "+row["row_id"])
        need("G2-6A:" in row["display"][8] and row["display"][8]!=e["previous_sosa_cell_value"],
             "real new source meaning and previous SOSA cell preserved "+row["row_id"])
    b=load("SOSA_G2_6B_Original_Source_Item_Coverage_10NOV2026.json")
    bc=b["source_counts"]
    need(len(b["original_toc_heading_coverage"])==1 and len(b["additional_native_subclauses_read"])==7
         and len(b["original_source_items"])==81 and bc["original_native_records_excluding_analyst"]==73
         and bc["RULE"]==7 and bc["PERMISSION"]==2 and bc["RECOMMENDATION"]==4
         and bc["OBSERVATION"]==9 and bc["TABLE"]==6 and bc["FIGURE"]==9
         and bc["SLOT_PROFILE_DASH_ROW"]==27 and bc["ANSI_VITA_RULE_TABLE_POINTER"]==9,
         "G2-6B original 3U PICP sources and original item counts")
    need(b["C239_cumulative_coverage"]["at_least_source_sampled_or_inline_read"]==150
         and b["C239_cumulative_coverage"]["substantively_unread"]==41
         and b["C239_cumulative_coverage"]["restricted"]==1,"150/41/1 original headings")
    bids={r["id"] for r in b["original_source_items"]}
    changed=[r for r in m["rows"] if r.get("G2_6B_source_correspondence")]
    need(len(changed)==26 and {r["row_id"] for r in changed}==set(m["workbookSnapshot"]["G2_6B_affected_row_ids"]),
         "26 original source-qualified G2-6B row IDs")
    for row in changed:
        e=row["G2_6B_source_correspondence"]
        need(e["source_item_ids"] and all(x in bids for x in e["source_item_ids"]),"native source item IDs "+row["row_id"])
        need(e["DIM_Profile_adopted"] is False and e["original_ANSI_VITA_and_DSDM_IDL_OpenAPI_companions_unread"],
             "no premature source or model assertion "+row["row_id"])
        need("G2-6B:" in row["display"][8] and row["display"][8]!=e["previous_sosa_cell_value"],
             "source-qualified donor cell "+row["row_id"])
    need(not b["DIM_Profile_adopted"] and not b["real_device_or_conformance_test"],"no adoption or device execution")
    z=load("SOSA_G2_6C_Original_Source_Item_Coverage_10NOV2026.json")
    cc=z["source_counts"]
    need(len(z["original_toc_heading_coverage"])==1 and len(z["additional_native_subclauses_read"])==4
         and len(z["original_source_items"])==51 and len({x["id"] for x in z["original_source_items"]})==51
         and cc["actual_native_records_excluding_analytical_context"]==43 and cc["ANALYTICAL_CONTEXT"]==8,
         "G2-6C one heading, four child subsections, 43 native+8 analytical source records")
    need(cc["RULE"]==4 and cc["RECOMMENDATION"]==2 and cc["OBSERVATION"]==5
         and cc["TABLE"]==4 and cc["FIGURE"]==5 and cc["SLOT_PROFILE_DASH_ROW"]==18
         and cc["RULE_LIST_PROFILE_OPTION"]==5, "G2-6C source-native standing and variants")
    need((z["C239_cumulative_coverage"]["registered_headings"],
         z["C239_cumulative_coverage"]["at_least_source_sampled_or_inline_read"],
         z["C239_cumulative_coverage"]["substantively_unread"],z["C239_cumulative_coverage"]["restricted"])==
         (192,151,40,1),"original C239 151/40/1 still partial")
    zid={x["id"] for x in z["original_source_items"]}
    current=[r for r in m["rows"] if r.get("G2_6C_source_correspondence")]
    need(len(current)==24 and {r["row_id"] for r in current}==set(m["workbookSnapshot"]["G2_6C_affected_row_ids"]),
         "exact 24 G2-6C qualified existing row IDs")
    for row in current:
        e=row["G2_6C_source_correspondence"]
        need(e["source_item_ids"] and all(v in zid for v in e["source_item_ids"]),
             "G2-6C original source item IDs "+row["row_id"])
        need(e["DIM_Profile_adopted"] is False and e["original_ANSI_VITA_and_DSDM_IDL_OpenAPI_companions_unread"],
             "native file holds/model nonadoption "+row["row_id"])
        need("G2-6C:" in row["display"][8] and row["display"][8]!=e["previous_sosa_cell_value"],
             "real qualified source comparison "+row["row_id"])
    need(not z["DIM_Profile_adopted"] and not z["independent_conformance_or_physical_device_operation_performed"],
         "no model adoption or physical action")
    z=load("SOSA_G2_6D_Original_Source_Item_Coverage_10NOV2026.json")
    cc=z["source_counts"]
    need(len(z["original_toc_heading_coverage"])==1 and len(z["additional_native_subclauses_read"])==3
         and len(z["original_source_items"])==26 and len({x["id"] for x in z["original_source_items"]})==26
         and cc["original_source_native_items_excluding_analytical_context"]==20
         and cc["ANALYTICAL_CONTEXT"]==6,"G2-6D one original heading, 3 children, 20 native plus 6 analyst records")
    need(cc["RULE"]==4 and cc["RECOMMENDATION"]==2 and cc["PROCESS_STATEMENT"]==4
         and cc["FIGURE"]==2 and cc["RULE_LIST_MODULE_OPTION"]==7 and cc["DASH_OPTION"]==1
         and cc["conditional_narrative_shall_provisions"]==2,
         "four native Rule SHALL, two Recommendations, two conditional unnumbered SHALLs, original options")
    need((z["C239_cumulative_coverage"]["registered_headings"],
         z["C239_cumulative_coverage"]["at_least_source_sampled_or_inline_read"],
         z["C239_cumulative_coverage"]["substantively_unread"],
         z["C239_cumulative_coverage"]["restricted"])==(192,152,39,1),
         "original 152 sampled/inline,39 unread,1 restricted headings")
    zid={x["id"] for x in z["original_source_items"]}
    current=[r for r in m["rows"] if r.get("G2_6D_source_correspondence")]
    need(len(current)==14 and {r["row_id"] for r in current}==set(m["workbookSnapshot"]["G2_6D_affected_row_ids"]),
         "exact 14 G2-6D qualified source rows")
    for row in current:
        e=row["G2_6D_source_correspondence"]
        need(e["source_item_ids"] and all(v in zid for v in e["source_item_ids"]),
             "original source identifiers for "+row["row_id"])
        need(e["DIM_Profile_adopted"] is False
             and e["original_ANSI_VITA_and_DSDM_IDL_OpenAPI_companions_unread"],
             "no adopted DIM/Profile or inferred external originals for "+row["row_id"])
        need("G2-6D:" in row["display"][8] and row["display"][8]!=e["previous_sosa_cell_value"],
             "source-qualified added SOSA column meaning "+row["row_id"])
    need(not z["DIM_Profile_adopted"]
         and not z["actual_runtime_conformance_or_physical_device_operation_performed"],
         "no model/adoption/runtime false claim")
    a=load("SOSA_G2_7A_Original_Source_Item_Coverage_10NOV2026.json")
    cc=a["source_counts"]
    need(len(a["original_toc_heading_coverage"])==3
         and len(a["original_source_items"])==77
         and len({x["id"] for x in a["original_source_items"]})==77
         and cc["source_native_items_excluding_analytical_context"]==70
         and cc["ANALYTICAL_CONTEXT"]==7,"G2-7A 3 original headings, 70 native items, 7 separate analyst contexts")
    need(cc["DEFINITION"]==5 and cc["PROTOCOL_CODE"]==50 and cc["SOURCE_CONTEXT"]==11
         and cc["TABLE"]==2 and cc["EXAMPLE_ROW"]==2
         and cc["numbered_C239_rule_shalls"]==0 and cc["numbered_C239_recommendations"]==0,
         "5 original definitions, 50 original protocol codes and source standing")
    need(len(a["protocol_groups"])==7 and sum(v["source_row_count"] for v in a["protocol_groups"])==50,
         "all seven distinct original source protocol code groups")
    need((a["C239_cumulative_coverage"]["registered_headings"],
          a["C239_cumulative_coverage"]["at_least_source_sampled_or_inline_read"],
          a["C239_cumulative_coverage"]["substantively_unread"],
          a["C239_cumulative_coverage"]["restricted"])==(192,155,36,1),
         "original C239 155 source sampled/inline,36 unread,1 restricted headings")
    nativeids={x["id"] for x in a["original_source_items"]}
    current=[r for r in m["rows"] if r.get("G2_7A_source_correspondence")]
    need(len(current)==20 and {r["row_id"] for r in current}==set(m["workbookSnapshot"]["G2_7A_affected_row_ids"]),
         "exact 20 G2-7A source-qualified existing comparison row IDs")
    for row in current:
        e=row["G2_7A_source_correspondence"]
        need(e["source_item_ids"] and all(v in nativeids for v in e["source_item_ids"]),
             "exact native AMPS source IDs in "+row["row_id"])
        need(e["DIM_Profile_adopted"] is False
             and e["original_ANSI_VITA_and_C239_native_companions_unread"]
             and e["full_AMPS_13_3_3_per_port_and_protocol_rules_unread"],
             "unreviewed original native companions and no DIM/Profile adoption "+row["row_id"])
        need("G2-7A:" in row["display"][8] and row["display"][8]!=e["previous_sosa_cell_value"],
             "source-qualified incremental AMPS meaning "+row["row_id"])
    need(not a["DIM_Profile_adopted"] and not a["runtime_or_independent_conformance_performed"]
         and not a["source"]["normative_ANSI_VITA_65_0_and_65_1_originals_read"],
         "no invented native VITA normativity or runtime/profiling")
    b=load("SOSA_G2_7B_Original_Source_Item_Coverage_10NOV2026.json")
    bc=b["source_counts"]
    need(len(b["original_toc_heading_coverage"])==1 and len(b["original_source_items"])==67
         and len({x["id"] for x in b["original_source_items"]})==67
         and bc["source_native_records_excluding_analytical_context"]==59
         and bc["ANALYTICAL_CONTEXT"]==8,"G2-7B one original TOC heading, 59 source-native items, 8 analysis")
    need(bc["SOURCE_CONTEXT"]==3 and bc["FIGURE"]==1 and bc["TABLE"]==6
         and bc["PARAMETER"]==12 and bc["EXAMPLE"]==18
         and bc["DCP_OPTION"]==15 and bc["DCP_SUPPORTED"]==4
         and bc["source_numbered_rule_shalls"]==0,"G2-7B all six native tables, 12 fields, 18 examples, 4 supported dcp")
    need((b["C239_cumulative_coverage"]["registered_headings"],
          b["C239_cumulative_coverage"]["at_least_source_sampled_or_inline_read"],
          b["C239_cumulative_coverage"]["substantively_unread"],
          b["C239_cumulative_coverage"]["restricted"])==(192,156,35,1),
         "C239 156 at least source sampled/inline, 35 substantively unread, one restricted")
    bids={x["id"] for x in b["original_source_items"]}
    current=[r for r in m["rows"] if r.get("G2_7B_source_correspondence")]
    need(len(current)==24 and {r["row_id"] for r in current}==set(m["workbookSnapshot"]["G2_7B_affected_row_ids"]),
         "exact 24 G2-7B source-qualified existing SOSA row IDs")
    for row in current:
        e=row["G2_7B_source_correspondence"]
        need(e["source_item_ids"] and all(z in bids for z in e["source_item_ids"]),
             "native original AMPS source item IDs "+row["row_id"])
        need(e["DIM_Profile_adopted"] is False
             and e["original_ANSI_VITA_and_C239_native_companions_unread"]
             and e["full_AMPS_diagram_pixel_geometry_unverified"],
             "no unwarranted original normative or model claims "+row["row_id"])
        need("G2-7B:" in row["display"][8] and row["display"][8]!=e["previous_sosa_cell_value"],
             "incremental original-source meaning in donor column "+row["row_id"])
    need(b["DIM_Profile_adopted"] is False and b["actual_runtime_or_independent_conformance_performed"] is False
         and b["source"]["native_original_ANSI_VITA_65_0_read"] is False,
         "no new native VITA completeness, model adoption or physical operation")
    c=load("SOSA_G2_7C_Original_Source_Item_Coverage_10NOV2026.json")
    cc=c["source_counts"]
    need(len(c["original_toc_heading_coverage"])==1
         and len(c["original_source_items"])==77
         and len({i["id"] for i in c["original_source_items"]})==77
         and cc["native_source_records_excluding_analysis"]==68
         and cc["ANALYTICAL_CONTEXT"]==9,
         "G2-7C original one heading, 68 native plus 9 analytical original-source records")
    need(cc["SOURCE_CONTEXT"]==6 and cc["TABLE"]==3 and cc["PROFILE_FAMILY"]==10
         and cc["DASH_OPTION"]==39 and cc["FULL_STRING_EXAMPLE"]==10
         and cc["table_13_3_4_1_named_dash_options"]==23
         and cc["table_13_3_4_2_named_dash_options"]==16
         and cc["original_numbered_RULE_SHALLs"]==0,
         "G2-7C three original tables, 10 family/10 example, 39 source dash records")
    need((c["C239_cumulative_coverage"]["registered_headings"],
          c["C239_cumulative_coverage"]["at_least_source_sampled_or_inline_read"],
          c["C239_cumulative_coverage"]["substantively_unread"],
          c["C239_cumulative_coverage"]["restricted"])==(192,157,34,1),
         "157 original headings at least sampled/inline-read,34 unread,1 restricted")
    need(not c["C239_cumulative_coverage"]["full_high_resolution_table_matrix_audit_complete"]
         and not c["source"]["source_table_high_resolution_geometry_verified"],
         "source dense multi-column matrix remains explicitly PARTIAL")
    family=[z for z in c["original_source_items"] if z["native_kind"]=="PROFILE_FAMILY"]
    need(sum(z["form_factor"]=="3U" for z in family)==6
         and sum(z["form_factor"]=="6U" for z in family)==4,
         "exact 6 original 3U plus 4 original 6U hardware profile families")
    ex=[z for z in c["original_source_items"] if z["native_kind"]=="FULL_STRING_EXAMPLE"]
    special=next(z for z in ex if z["stable_source_item_id"]=="6U-EXTERNAL_IO")
    need(special["source_grammar_string"].startswith("MODA3p-12.2.8"),
         "original anomalous 6U External I/O MODA3p sample must be preserved")
    need(len(c["exact_holds"])==19 and not c["DIM_Profile_adopted"]
         and not c["runtime_or_independent_conformance_performed"],
         "source-exact 19 unresolved holds; no model adoption or live device claim")
    cids={z["id"] for z in c["original_source_items"]}
    updated=[r for r in m["rows"] if r.get("G2_7C_source_correspondence")]
    need(len(updated)==22 and {r["row_id"] for r in updated}==set(m["workbookSnapshot"]["G2_7C_affected_row_ids"]),
         "exact 22 source-qualified existing SOSA target row IDs")
    for r in updated:
        e=r["G2_7C_source_correspondence"]
        need(e["source_item_ids"] and all(v in cids for v in e["source_item_ids"]),
             "C239 native/source item IDs for "+r["row_id"])
        need(e["DIM_Profile_adopted"] is False
             and e["original_ANSI_VITA_and_C239_native_companions_unread"]
             and e["dense_matrix_exact_cell_alignment_unverified"],
             "unverified dense matrix and source originals explicitly held for "+r["row_id"])
        need("G2-7C:" in r["display"][8] and r["display"][8]!=e["previous_sosa_cell_value"],
             "original-source-qualified incremental SOSA donor cell "+r["row_id"])
    need(m["currentWorkbookSha256"]==digest((D/BOOK).read_bytes())
         and m["workbookSnapshot"]["sha256"]==m["currentWorkbookSha256"],"actual saved current workbook hash retained")
    need(m["SOSAReviewCompletion"]["G2_7C_XLSX_lag"]==0,"earlier G2-7C saved Excel publication preserved")
    print("PASS: previous G2-7C native source and 22 source-qualified cells preserved (matrix visual hold)")

    # G2-7D original §13.3.5 source, source-graded 3U/6U Switch AMPS packet
    z=load("SOSA_G2_7D_Original_Source_Item_Coverage_10NOV2026.json")
    sc=z["source_counts"];records=z["original_source_items"];zids={a["id"] for a in records}
    need(len(records)==len(zids)==44 and sc["source_native_item_records"]==38
         and sc["analytical_contexts"]==6 and len(z["exact_holds"])==17,
         "38 original Switch items, 6 analyst contexts and 17 precise holds")
    need(sc["SOURCE_CONTEXT"]==7 and sc["TABLE"]==2 and sc["PROFILE_FAMILY"]==4
         and sc["MATRIX_DEPTH_ROW"]==16 and sc["PROFILE_DASH_OPTION"]==5
         and sc["FULL_STRING_EXAMPLE"]==4 and sc["numbered_rule_shalls"]==0,
         "all original Switch profiles, rows, variants, examples and zero numbered Rules")
    need(len(z["original_registered_heading_coverage"])==1
         and (z["C239_cumulative_coverage"]["registered_headings"],
              z["C239_cumulative_coverage"]["at_least_source_sampled_or_inline_read"],
              z["C239_cumulative_coverage"]["substantively_unread"],
              z["C239_cumulative_coverage"]["restricted"])==(192,158,33,1),
         "one newly source-read heading; original donor remains OPEN")
    need(z["source"]["full_matrix_visual_alignment_checked"] is False
         and z["source"]["publisher_ANSI_VITA65_0_65_1_read"] is False
         and z["source"]["original_C239_DSDM_IDL_OpenAPI_eight_read"] is False
         and z["DIM_Profile_adopted"] is False
         and z["independent_device_or_runtime_conformance"] is False,
         "matrix/legal ports and native companions held; no DIM or hardware conformance")
    fam={a["id"]:a for a in records if a["native_kind"]=="PROFILE_FAMILY"}
    need(len(fam)==4 and sum(a["form_factor"]=="3U" for a in fam.values())==3
         and sum(a["form_factor"]=="6U" for a in fam.values())==1,
         "3U DP/EP/DP-V66 and physically distinct 6U DP switch source families")
    ex=[a for a in records if a["native_kind"]=="FULL_STRING_EXAMPLE"]
    need(len(ex)==4 and sum(a["exact_printed_amps_string"].startswith("MODA3-") for a in ex)==3
         and sum(a["exact_printed_amps_string"].startswith("MODA6-") for a in ex)==1,
         "retain exact four original switch AMPS source examples")
    updated=[a for a in m["rows"] if a.get("G2_7D_source_correspondence")]
    need(len(updated)==17 and {a["row_id"] for a in updated}==set(m["workbookSnapshot"]["G2_7D_affected_row_ids"]),
         "17 existing qualified SOSA cells, no new rows")
    for a in updated:
        ev=a["G2_7D_source_correspondence"]
        need(ev["source_item_ids"] and all(v in zids for v in ev["source_item_ids"]),
             "original source ID ledger match "+a["row_id"])
        need(ev["DIM_Profile_adopted"] is False
             and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
             and ev["dense_switch_matrix_exact_pixel_alignment_unverified"],
             "no false legal-port or new DIM/Profile assertion "+a["row_id"])
        need("G2-7D:" in a["display"][8] and a["display"][8]!=ev["previous_sosa_cell_value"],
             "actual source-qualified donor cell and prior preserved "+a["row_id"])
    need(m["SOSAReviewCompletion"]["G2_7D_XLSX_lag"]==0,
         "previous original G2-7D saved workbook exit verified")
    print("PASS: original C239 §13.3.5 Switch AMPS: four families,16 depth rows,five dashes,four examples,17 mappings,17 holds")


    # G2-7E, original C239 §13.3.6 VITA66 connector optical protocol fields
    z=load("SOSA_G2_7E_Original_Source_Item_Coverage_10NOV2026.json")
    sc=z["source_counts"];items=z["original_source_items"];ids={a["id"] for a in items}
    need(len(items)==len(ids)==27 and sc["native_records"]==21
         and sc["analytical_contexts"]==6 and len(z["exact_holds"])==16,
         "21 original VITA66 source records, six analyst contexts and 16 exact holds")
    need(sc["SOURCE_CONTEXT"]==14 and sc["TABLE"]==1
         and sc["MT_PROFILE_EXAMPLE"]==3 and sc["PROTOCOL_FIELD_EXAMPLE"]==3
         and sc["original_numbered_RULE_SHALLs"]==0
         and sc["unnumbered_scoped_narrative_must_statements"]==1,
         "original source 14 inline meanings, three MT/three bracketed protocol examples, zero numbered Rules")
    need(len(z["original_toc_heading_coverage"])==1
         and (z["C239_cumulative_coverage"]["registered_headings"],
              z["C239_cumulative_coverage"]["at_least_source_sampled_or_inline_read"],
              z["C239_cumulative_coverage"]["substantively_unread"],
              z["C239_cumulative_coverage"]["restricted"])==(192,159,32,1),
         "one additional original subsection, source-graded 159/32/1 of 192 headings")
    need(z["source"]["page_image_pixels_verified"] is False
         and z["source"]["source_ANSI_VITA65_0_65_1_originals_reviewed"] is False
         and z["source"]["C239_native_DSDM_IDL_OpenAPI_original_eight_reviewed"] is False
         and z["DIM_Profile_adopted"] is False
         and z["installed_device_or_independent_conformance_performed"] is False,
         "source visual, ANSI and DSDM/IDL/OpenAPI originals held, no DIM/Profile/device adoption")
    ex={a["literal"] for a in items if a["native_kind"]=="PROTOCOL_FIELD_EXAMPLE"}
    need(ex=={"[E18]","[4E18]","[N-3E18-3A6F]"},
         "three original bracketed protocol syntax examples preserved exactly")
    mt={a["mt"] for a in items if a["native_kind"]=="MT_PROFILE_EXAMPLE"}
    need(mt=={"MTA1","MTB1","MTC1"},
         "all three actual example MTs/source optical profiles accounted")
    need(len(load("SOSA_G2_7C_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==19
         and len(load("SOSA_G2_7D_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==17,
         "19 earlier Payload and 17 Switch original-source holds remain")
    updated=[a for a in m["rows"] if a.get("G2_7E_source_correspondence")]
    need(len(updated)==15 and {a["row_id"] for a in updated}==set(m["workbookSnapshot"]["G2_7E_affected_row_ids"]),
         "15 original source-qualified existing SOSA donor row IDs")
    for a in updated:
        ev=a["G2_7E_source_correspondence"]
        need(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]),
             "original VITA66 source item IDs for "+a["row_id"])
        need(ev["DIM_Profile_adopted"] is False
             and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
             and ev["original_table_page_pixels_unverified"],
             "no unverified VITA companion/model adoption for "+a["row_id"])
        need("G2-7E:" in a["display"][8]
             and a["display"][8].startswith(ev["previous_sosa_cell_value"]),
             "prior SOSA cell preserved before exact VITA66 source increment "+a["row_id"])
    need(m["SOSAReviewCompletion"]["G2_7E_XLSX_lag"]==0,
         "preceding G2-7E SAME Excel source workbook was verified")
    print("PASS: original C239 §13.3.6, 21 native items, 3 MT, 3 protocol examples, 15 source cells and exact holds")


    # G2-7F direct original C239 §13.3.7: four numbered Rules, one Observation, one Permission
    z=load("SOSA_G2_7F_Original_Source_Item_Coverage_10NOV2026.json")
    sc=z["source_counts"];items=z["original_source_items"];ids={v["id"] for v in items}
    need(len(items)==len(ids)==15 and sc["native_items_excluding_analyst"]==10
         and sc["analytical_contexts"]==5 and len(z["exact_holds"])==17,
         "ten original source items plus five analytical contexts and seventeen exact source holds")
    need(sc["RULE"]==4 and sc["OBSERVATION"]==1 and sc["PERMISSION"]==1
         and sc["HEADING"]==1 and sc["TABLE_REFERENCE"]==3 and sc["ANALYTICAL_CONTEXT"]==5,
         "source-native four Rules, one Observation, one Permission, three format table pointers")
    need(sc["source_RULE_shall"]==3 and sc["source_RULE_must"]==1
         and sc["normative_rule_method_A_only"]==2 and sc["normative_rule_method_A_and_D"]==2
         and sc["source_RECOMMENDATION"]==0,
         "source original 3 SHALL, 1 MUST Rule and exact printed A vs A,D methodology")
    rules=[v for v in items if v["kind"]=="RULE"]
    need([r["printed_rule_id"] for r in rules]==["13.3.7-1","13.3.7-2","13.3.7-3","13.3.7-4"],
         "exact original numbered Rules without artificially changed printed identifiers")
    need([r["printed_modal_verb"] for r in rules]==["shall","must","shall","shall"],
         "original Rule13.3.7-2 MUST wording retained and other three SHALLs")
    need([r["conformance_methodology_printed_codes"] for r in rules]==[["A"],["A"],["A","D"],["A","D"]],
         "exact source-published conformance codes unmodified")
    obs=next(v for v in items if v["kind"]=="OBSERVATION")
    perm=next(v for v in items if v["kind"]=="PERMISSION")
    need(obs["illustrated_UTP_count"]==4 and "subset" in obs["exception"]
         and perm["not_mandatory"] is True,
         "observation lane-subset exception and optional EP1/EP2 PCI Express combine preserved")
    cov=z["C239_cumulative_coverage"]
    need(len(z["original_toc_heading_coverage"])==1 and
         (cov["registered_headings"],cov["at_least_source_sampled_or_inline_read"],
          cov["substantively_unread"],cov["restricted"])==(192,160,31,1),
         "one original heading earned, 160 sampled/inline,31 unread,1 restricted")
    need(z["source"]["original_image_pixel_rendering_verified"] is False
         and z["source"]["original_ANSI_VITA_and_C239_native_companions_read"] is False
         and z["DIM_and_CSAPI_Profile_adopted"] is False
         and z["installed_device_or_independent_conformance_performed"] is False,
         "original external companions and hardware conformance held, no DIM/Profile adopted")
    need(len(load("SOSA_G2_7C_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==19
         and len(load("SOSA_G2_7D_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==17
         and len(load("SOSA_G2_7E_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==16,
         "all preceding SOSA G2-7C/D/E native source and matrix holds retained")
    affected=[v for v in m["rows"] if v.get("G2_7F_source_correspondence")]
    need(len(affected)==18 and {v["row_id"] for v in affected}==set(m["workbookSnapshot"]["G2_7F_affected_row_ids"]),
         "exact 18 qualified SOSA source-to-master existing row IDs")
    for v in affected:
        ev=v["G2_7F_source_correspondence"]
        need(ev["source_item_ids"] and all(k in ids for k in ev["source_item_ids"]),
             "every source-qualified comparison matches stable original source item "+v["row_id"])
        need(ev["DIM_Profile_adopted"] is False
             and ev["independent_conformance_performed"] is False
             and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
             and ev["original_dense_matrix_pixels_unverified"],
             "no fabricated model adoption, native-complete source audit or hardware conformance")
        need("G2-7F:" in v["display"][8]
             and v["display"][8].startswith(ev["previous_sosa_cell_value"]),
             "prior original SOSA donor cell preserved before new Rule/Observation/Permission qualifier")
    need(m["SOSAReviewCompletion"]["G2_7F_XLSX_lag"]==0,
         "previous G2-7F original Rule source workbook published and saved-cell verified")
    print("PASS: C239 §13.3.7 four Rules, one Observation, one Permission, 18 qualified source cells, exact holds")


    # G2-7G original C239 §13.3.8 full inline-source/figure-caption review, figure geometry HELD
    z=load("SOSA_G2_7G_Original_Source_Item_Coverage_10NOV2026.json")
    cc=z["source_counts"];items=z["original_source_items"];ids={q["id"] for q in items}
    need(len(items)==len(ids)==36 and cc["native_source_items"]==30
         and cc["analytical_contexts"]==6 and len(z["exact_holds"])==19,
         "original §13.3.8 30 native source entries, 6 analytics and 19 exact holds")
    need(cc["SOURCE_CONTEXT"]==13 and cc["RULE"]==2 and cc["FIGURE"]==3
         and cc["PIN_ROW"]==10 and cc["RECOMMENDATION"]==1 and cc["OBSERVATION"]==1,
         "original two numbered Rules, one Recommendation, one Observation, three figures and ten SMPM10 printed pin rows")
    need(cc["original_source_rule_T_method_count"]==1
         and cc["original_recommendation_T_method_count"]==1
         and cc["original_rule_no_method_printed"]==1,
         "one printed Rule(T), one Recommendation(T), SMPM10 Rule without printed method")
    rul=[q for q in items if q["kind"]=="RULE"]
    need({q["source_rule"] for q in rul}=={"13.3.8.1-1","13.3.8.2-2"}
         and all(q["printed_modal_verb"]=="shall" for q in rul),
         "exact original printed Rule ids and SHALL standing, no invented Rule13.3.8.2-1")
    need(next(q for q in rul if q["source_rule"]=="13.3.8.1-1")["conformance_method_printed"] is None
         and next(q for q in rul if q["source_rule"]=="13.3.8.2-2")["conformance_method_printed"]==["T"],
         "printed T method only on SMPM14 Rule, do not backfill missing SMPM10 method")
    rec=next(q for q in items if q["kind"]=="RECOMMENDATION")
    obs=next(q for q in items if q["kind"]=="OBSERVATION")
    need(rec["printed_modal_verb"]=="should" and rec["conformance_method_printed"]==["T"]
         and rec["not_mandatory_rule"] and obs["single_channel"]=="B1"
         and obs["two_channels"]=={"channel_1":"B1","channel_2":"B4"},
         "source distinct SHOULD recommendation, observed B1/B4 first two analog channels")
    pins=[q for q in items if q["kind"]=="PIN_ROW"]
    need(len(pins)==10 and {q["pin"] for q in pins}==
         {"A1","A2","A3","B1","B2","B3","B4","C1","C2","C3"}
         and all(q["graphic_contact_geometry_verified"] is False for q in pins),
         "all original extracted SMPM10 text pin labels, without unsupported pixel geometry")
    conflict=next(q for q in items if q["id"].endswith("SOURCE_CONTEXT-TABLE_POINTER_INCONSISTENCY"))
    need(conflict["caption_pointer"]=="6.5.4.6.4-1"
         and conflict["numbered_rule_pointer"]=="6.4.5.6.4-1",
         "preserve conflicting printed ANSI/VITA65.1 caption-vs-Rule table locators")
    cov=z["C239_cumulative_coverage"]
    need(len(z["original_registered_heading_coverage"])==1
         and len(z["additional_nested_subsections_reviewed"])==2
         and (cov["registered_headings"],cov["at_least_source_sampled_or_inline_read"],
              cov["substantively_unread"],cov["restricted"])==(192,161,30,1),
         "one registered heading + two nested native subsections, C239 161/30/1 of 192")
    need(z["source"]["original_page_images_verified"] is False
         and z["source"]["original_ANSI_VITA65_1_67_3_66_5_companions_read"] is False
         and z["source"]["original_C239_DSDM_IDL_OpenAPI_eight_companions_read"] is False
         and z["DIM_CSAPI_Profile_adopted"] is False
         and z["runtime_or_independent_hardware_conformance_performed"] is False,
         "original page-image/native-standard and independent conformance holds intact")
    need(len(load("SOSA_G2_7C_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==19
         and len(load("SOSA_G2_7D_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==17
         and len(load("SOSA_G2_7E_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==16
         and len(load("SOSA_G2_7F_Original_Source_Item_Coverage_10NOV2026.json")["exact_holds"])==17,
         "all four earlier local G2-7C/D/E/F source and pixel-matrix holds retained")
    qualified=[r for r in m["rows"] if r.get("G2_7G_source_correspondence")]
    need(len(qualified)==18 and {r["row_id"] for r in qualified}==set(m["workbookSnapshot"]["G2_7G_affected_row_ids"]),
         "18 source-qualified existing target row IDs, no invented DIM rows")
    for r in qualified:
        ev=r["G2_7G_source_correspondence"]
        need(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]),
             "stable edition-graded original C239 source IDs "+r["row_id"])
        need(ev["DIM_Profile_adopted"] is False
             and ev["runtime_or_independent_conformance_performed"] is False
             and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
             and ev["source_pinout_figures_pixel_verified"] is False,
             "source/visual ambiguity preserved and no DIM/Profile/hardware adoption "+r["row_id"])
        need("G2-7G:" in r["display"][8]
             and r["display"][8].startswith(ev["previous_sosa_cell_value"]),
             "previous SOSA donor evidence value preserved before native §13.3.8 comparison "+r["row_id"])
    need(m["SOSAReviewCompletion"]["G2_7G_XLSX_lag"]==0,
         "previous G2-7G source/workbook exit preserved")
    print("PASS: original §13.3.8 two Rules, one Recommendation/Observation, 3 figures, 10 text pin labels, 18 source-qualified cells and holds")

    # G2-7H original §13.4 VNX future/provisional source native row census
    z=load("SOSA_G2_7H_Original_Source_Item_Coverage_11NOV2026.json")
    cc=z["source_counts"];items=z["original_source_items"];source_ids={e["id"] for e in items}
    need(len(items)==len(source_ids)==57 and cc["native_source_items"]==57
         and cc["HEADING"]==9 and cc["CONTEXT"]==10 and cc["TABLE"]==4
         and cc["FIGURE"]==2 and cc["CONFIG"]==9 and cc["THERMAL"]==3
         and cc["OBSERVATION"]==2 and cc["TBD"]==18,
         "G2-7H all 57 original physical VNX source-native entries classified")
    need(cc["source_numbered_RULE_SHALL"]==0 and cc["source_numbered_RECOMMENDATION_SHOULD"]==0
         and cc["source_numbered_OBSERVATIONS"]==2
         and len(z["registered_headings"])==9 and len(z["nested_subsections"])==17
         and len(z["exact_holds"])==17,
         "zero current numbered rules, two observations, nine headings/17 nested and 17 exact holds")
    cfg=z["connector_table_rows"]
    need(len(cfg)==9 and {(q["size"],q["mode"],q["pins"]) for q in cfg}==
         {(a,b,c) for a in ("19mm","32.5mm","39mm")
                  for b,c in (("Connector Only",400),("Small Aperture",320),("Large Aperture",240))},
         "all nine printed 19/32.5/39mm VNX config table rows")
    need(sum(q["config_class"]=="1" and q["aperture_fill"]=="None" for q in cfg)==1
         and all(q["config_class"]=="TBD" for q in cfg[1:]),
         "only the 19mm connector-only config class is printed, eight future TBD")
    need((z["C239_cumulative_coverage"]["registered"],
          z["C239_cumulative_coverage"]["at_least_sampled_or_inline_read"],
          z["C239_cumulative_coverage"]["substantively_unread"],
          z["C239_cumulative_coverage"]["restricted"])==(192,170,21,1),
         "170/21/1 source coverage, not 100-percent donor completeness")
    need(z["source"]["figure_images_verified"] is False
         and z["source"]["VITA_74_native_read"] is False
         and z["source"]["eight_C239_DSDM_IDL_OpenAPI_native_read"] is False
         and z["DIM_Profile_adopted"] is False
         and z["independent_hardware_runtime_conformance"] is False,
         "original figures/external native files held and zero DIM/Profile/hardware adoption")
    affected=[row for row in m["rows"] if row.get("G2_7H_source_correspondence")]
    need(len(affected)==16 and {row["row_id"] for row in affected}==
         set(m["workbookSnapshot"]["G2_7H_affected_row_ids"]),
         "exactly sixteen existing source-qualified VNX donor cells")
    for row in affected:
        ev=row["G2_7H_source_correspondence"]
        need(ev["source_item_ids"] and all(x in source_ids for x in ev["source_item_ids"])
             and ev["DIM_Profile_adopted"] is False
             and ev["original_ANSI_VITA_and_C239_native_companions_unread"]
             and ev["figure_images_verified"] is False
             and row["display"][8].startswith(ev["previous_sosa_cell_value"])
             and "G2-7H:" in row["display"][8],
             "source ID/provenance, previous SOSA value and no model adoption "+row["row_id"])
    need(m["SOSAReviewCompletion"]["G2_7H_XLSX_lag"]==0,
         "previous original G2-7H complete workbook standing retained")
    print("PASS: G2-7H original §13.4: 57 records, 9 headings, 18 TBD, 2 Observations, 16 qualified cells; Excel checkpoint pending")

def check_g2_7i_source(m):
    z=load("SOSA_G2_7I_Original_Source_Item_Coverage_11NOV2026.json")
    c=z["source_counts"];entries=z["source_items"];ids={a["id"] for a in entries}
    need(len(entries)==len(ids)==82 and c["total"]==82
         and c["RULE"]==23 and c["PERMISSION"]==4 and c["OBSERVATION"]==3
         and c["CONNECTOR"]==16 and c["J1_PIN"]==11
         and c["rules_method_I"]==18 and c["rules_method_A"]==5
         and len(z["exact_holds"])==20,
         "all 82 distinct original source-native entries including 23 Rule/4 Permission/3 Observation, 16 connector/11 J1 pins,20 holds")
    rul=[a for a in entries if a["kind"]=="RULE"]
    need(len(rul)==23 and [sum(a["printed_conformance_method"]==v for a in rul) for v in ("I","A")]==[18,5],
         "exact original Rule I vs A methodology; neither Permissions nor Observations promoted")
    p=[a for a in entries if a["kind"]=="PERMISSION"]
    need(any(a["id"].endswith("13_5_2_4") for a in p),
         "original atypical Permission13.5.2-4 retained without invented renumbering")
    obs=next(a for a in entries if a["id"].endswith("OBSERVATION-13_5_2_2_1_2"))
    need(obs["printed_method"]=="I" and obs["not_rule"] is True,
         "Observation with (I) remains Observation")
    need(c["HEADING"]==3 and c["NESTED_SECTION"]==4
         and (z["c239_coverage"]["total"],z["c239_coverage"]["at_least_sampled_or_inline"],
              z["c239_coverage"]["unread"],z["c239_coverage"]["restricted"])==(192,173,18,1)
         and z["c239_coverage"]["full_13_5_review"] is False,
         "3 newly sampled/inline C239 headings and 18 original unread remain")
    need(z["source"]["figure_pixels_verified"] is False
         and z["source"]["original_SAE_MIL_VITA_unread"] is True
         and z["source"]["C239_eight_native_files_unread"] is True
         and z["DIM_and_CSAPI_Profile_adopted"] is False
         and z["independent_hardware_conformance_performed"] is False,
         "external source/figure constraints, no hardware/runtime or adopted classes")
    matched=[r for r in m["rows"] if r.get("G2_7I_source_correspondence")]
    need(len(matched)==25
         and {r["row_id"] for r in matched}==set(m["workbookSnapshot"]["G2_7I_affected_row_ids"]),
         "25 original-source-qualified existing SOSA-only donor rows")
    for r in matched:
        e=r["G2_7I_source_correspondence"]
        need(e["source_item_ids"] and all(a in ids for a in e["source_item_ids"])
             and e["DIM_Profile_adopted"] is False
             and e["figure_and_native_companion_unverified"] is True
             and r["display"][8].startswith(e["previous_sosa_cell_value"])
             and "G2-7I:" in r["display"][8],
             "stable source meaning and previous cell retained "+r["row_id"])
    need(m["SOSAReviewCompletion"]["G2_7I_XLSX_lag"]==0,
         "previous original G2-7I source and saved SAME-Excel checkpoint retained")
    print("PASS: original G2-7I C239 Rule inventory and 25 semantic mappings, figure/native companion holds retained")


def check_g2_7j_source(m):
    z=load("SOSA_G2_7J_Original_Source_Item_Coverage_11NOV2026.json")
    sc=z["source_counts"];items=z["original_source_items"];ids={a["id"] for a in items}
    need(len(items)==len(ids)==134
         and sc["total_source_native_items"]==134
         and [sc[k] for k in ("SECTION","RULE","OBSERVATION","FIGURE","TABLE","SOURCE_CONTEXT","SIGNAL_GROUP","PIN_LABEL")]==[2,8,4,1,1,7,26,85],
         "original J2 134 source-native records at correct source/standing categories")
    need(sc["numbered_rules"]==8 and sc["rules_inspection_I"]==6 and sc["rules_test_T"]==2
         and sc["numbered_observations"]==4 and sc["numbered_permissions"]==0
         and sc["source_signal_groups"]==26 and sc["individually_printed_pin_label_records"]==85
         and sc["aggregated_unresolved_pin_rosters"]==2
         and sc["source_printed_pin_designator_tokens"]==103
         and len(z["source_holds"])==22,
         "8 Rule, 4 Observation, 26 signal families, 85 individual and 2 held grouped pin rows,103 designators,22 holds")
    rules=[a for a in items if a["kind"]=="RULE"]
    need(len(rules)==8 and
         [sum(a["conformance_method_printed"]==[x] for a in rules) for x in ("I","T")]==[6,2],
         "source printed six Inspection and two Test Rules")
    need({a["printed_rule_id"] for a in rules}=={
           "13.5.2.3-1","13.5.2.3-2","13.5.2.3-3","13.5.2.3-4",
           "13.5.2.3.1-1","13.5.2.3.1-2","13.5.2.3.1-3","13.5.2.3.1-4"},
         "original exact eight printed J2 and Power Enable Rule identifiers")
    rule_map={a["printed_rule_id"]:a for a in rules}
    need("≥18.0" in rule_map["13.5.2.3-3"]["meaning"]
         and "≤1.5" in rule_map["13.5.2.3-4"]["meaning"]
         and "≥100" in rule_map["13.5.2.3.1-1"]["meaning"]
         and "≤5" in rule_map["13.5.2.3.1-2"]["meaning"]
         and "100 mA" in rule_map["13.5.2.3.1-3"]["meaning"]
         and "30 VDC" in rule_map["13.5.2.3.1-4"]["meaning"],
         "source original discrete logic and power-enable numeric threshold evidence")
    observations=[a for a in items if a["kind"]=="OBSERVATION"]
    need({a["printed_observation_id"] for a in observations}=={
         "13.5.2.3-1","13.5.2.3-2","13.5.2.3-3","13.5.2.3-4"}
         and all(a["normative_rule"] is False for a in observations),
         "four original numbered Observations distinct from Rules and absent Permissions")
    groups=z["source_signal_groups"];pinrows=z["printed_pin_label_evidence"]
    need(len(groups)==26 and sum(g["pin_count"] for g in groups)==103
         and len(pinrows)==87 and len([p for p in pinrows if p.get("aggregate")])==2,
         "full 6-page J2 table group and pin textual census")
    need({p["group"] for p in pinrows if p.get("aggregate")}=={"SENMAN","ARMING_ISOLATION"}
         and all(p["source_id"] in ids for p in pinrows),
         "ten manufacturer and eight reserved arming pin positions held in grouped source rows")
    pins={p["pin"] for p in pinrows if not p.get("aggregate")}
    need(len(pins)==85 and {"25-1","25-2","25-S","75-1","75-2","75-S"}<=pins,
         "distinct J2 source printed pin designators incl native twinax subcontacts")
    cov=z["c239_cumulative_registered_headings"]
    need((cov["total"],cov["at_least_sampled_or_inline_reviewed"],
           cov["substantively_unread"],cov["restricted"])==(192,173,18,1)
         and cov["newly_registered_headings_reviewed"]==0
         and cov["full_13_5_source_coverage"] is False,
         "only nested J2 source reviewed; original 173/18/1 TOC count unchanged")
    source=z["source"]
    need(source["original_inline_text_examined"] is True
         and source["source_table_text_examined_all_six_pages"] is True
         and source["original_figure_pixels_verified"] is False
         and source["original_table_graphic_alignment_verified"] is False
         and source["eight_C239_model_API_companions_reviewed"] is False
         and z["model_or_CSAPI_Profile_adopted"] is False
         and z["independent_hardware_conformance"] is False,
         "original J2 text evidence but native graphics/companions and physical conformance remain held")
    mapped=[r for r in m["rows"] if r.get("G2_7J_source_correspondence")]
    need(len(mapped)==25 and {r["row_id"] for r in mapped}
          ==set(m["workbookSnapshot"]["G2_7J_affected_row_ids"]),
         "exact 25 existing source-qualified canonical SOSA comparison rows")
    for row in mapped:
        ev=row["G2_7J_source_correspondence"]
        need(ev["source_item_ids"] and all(v in ids for v in ev["source_item_ids"])
             and ev["DIM_Profile_adopted"] is False
             and ev["pinout_figure_and_dense_modality_matrix_unverified"] is True
             and ev["external_native_companions_unread"] is True
             and row["display"][8].startswith(ev["previous_sosa_cell_value"])
             and "G2-7J:" in row["display"][8],
             "stable original source IDs, previous donor comparison and model/visual holds "+row["row_id"])
    need(m["SOSAReviewCompletion"]["G2_7J_XLSX_lag"]==0,
         "previous G2-7J original source and verified saved Excel retained")
    print("PASS: direct original C239 J2 134 source items/103 source pin designators, 8 Rules/4 Observations, 25 qualified master comparisons and precise holds")


def check_g2_7k_source(m):
    z=load("SOSA_G2_7K_Original_Source_Item_Coverage_11NOV2026.json")
    records=z["original_source_items"];sourceids={v["id"] for v in records}
    counts=z["native_source_counts"]
    need(len(records)==len(sourceids)==7 and counts["total_records"]==7
         and counts["native_numbered_SHALL_Rules"]==2
         and counts["inspection_I_rules"]==2
         and counts["source_contexts"]==1
         and counts["normative_companion_pointers"]==2
         and counts["prior_source_cross_references"]==1
         and counts["nested_heading"]==1
         and not any(counts[k] for k in ("numbered_recommendations","numbered_permissions","numbered_observations"))
         and len(z["exact_holds"])==11,
         "original §13.5.2.3.2 two Inspection Rules, seven native source items and eleven exact holds")
    rules=[v for v in records if v["kind"]=="RULE"]
    need({v["printed_rule_id"] for v in rules}=={"13.5.2.3.2-1","13.5.2.3.2-2"}
         and all(v["modal_verb"]=="shall" and v["conformance_methodology_printed"]==["I"] for v in rules),
         "exact source Rule identity, SHALL standing and printed Inspection(I) method")
    physical=next(v for v in records if v["kind"]=="SOURCE_CONTEXT")
    need(physical["wire_count"]==8 and physical["twisted_pair_count"]==4
         and physical["characteristic_impedance_ohms"]==100
         and physical["standing"]=="DESCRIPTIVE_SOURCE_CONTEXT_NOT_NUMBERED_RULE",
         "eight-wire four twisted-pair 100-ohm narrative distinct from normative Rules")
    need(next(v for v in rules if v["printed_rule_id"]=="13.5.2.3.2-2")["reference_IEEE"]=="IEEE 802.3-2008"
         and "or equivalent" in next(v for v in rules if v["printed_rule_id"]=="13.5.2.3.2-2")["cable_specification"],
         "preserve specific IEEE edition and alternative physical cabling, no silent normative substitution")
    last=load("SOSA_G2_7J_Original_Source_Item_Coverage_11NOV2026.json")
    need(z["prior_source_reference"]["source_item_id"] in {x["id"] for x in last["original_source_items"]}
         and len(last["source_holds"])==22,
         "earlier J2 table physical Ethernet pin group and original holds explicitly retained")
    c=z["c239_registered_heading_standing"]
    need((c["total_registered_headings"],c["at_least_sampled_or_inline_read"],
          c["substantively_unread"],c["restricted"])==(192,173,18,1)
         and c["new_registered_headings_earned"]==0,
         "original nested Ethernet source subsection gets no fabricated registered heading credit")
    source=z["source"]
    need(source["source_access"]=="ORIGINAL_INLINE_TEXT_FULL_SUBSECTION_READ"
         and source["original_IEEE_802_3_2008_read"] is False
         and source["original_AS6070_6_read"] is False
         and source["original_C239_DSDM_IDL_OpenAPI_eight_read"] is False
         and z["DIM_CSAPI_Profile_adopted"] is False
         and z["independent_runtime_or_hardware_conformance"] is False,
         "unexamined external standards/natives and no profile or hardware conformance")
    changed=[r for r in m["rows"] if r.get("G2_7K_source_correspondence")]
    need(len(changed)==10 and {r["row_id"] for r in changed}
         ==set(m["workbookSnapshot"]["G2_7K_affected_row_ids"]),
         "ten existing source-qualified SOSA donor I-column comparison rows only")
    for r in changed:
        ev=r["G2_7K_source_correspondence"]
        need(ev["source_item_ids"] and all(s in sourceids for s in ev["source_item_ids"])
             and ev["DIM_Profile_adopted"] is False
             and ev["original_IEEE_and_AS6070_6_companion_unread"] is True
             and ev["actual_1000BaseT_hardware_or_traffic_unverified"] is True
             and r["display"][8].startswith(ev["previous_sosa_cell_value"])
             and "G2-7K:" in r["display"][8],
             "source IDs, original donor value, no universal DIM/Profile or live Ethernet claim "+r["row_id"])
    need(m["SOSAReviewCompletion"]["G2_7K_XLSX_lag"] in (0,10)
         and m["workbookSnapshot"]["currently_matches_readable_view"]
             is (m["SOSAReviewCompletion"]["G2_7K_XLSX_lag"]==0),
         "current ten source cells pending or already verified SAME original Excel publication")
    print("PASS: original C239 §13.5.2.3.2 two Inspection SHALL Rules, IEEE/cable original-source holds,10 existing source matches")

def matrix_to_xml(matrix,styles,main=False,sections=()):
    w=max(len(row) for row in matrix);need(w<=16,"sheet dimensions")
    root=ET.Element(q("worksheet"))
    sv=ET.SubElement(root,q("sheetViews"))
    view=ET.SubElement(sv,q("sheetView"),{"workbookViewId":"0","showGridLines":"0"})
    ET.SubElement(view,q("pane"),{"ySplit":"2" if main else "1","xSplit":"4" if main else "1","topLeftCell":"E3" if main else "B2","activePane":"bottomRight","state":"frozen"})
    ET.SubElement(root,q("sheetFormatPr"),{"defaultRowHeight":"19"})
    widths=([28,30,32,31,29,32,33,36,50,32,32,33,34,36,41] if main else [29]+[43]*15)
    cols=ET.SubElement(root,q("cols"))
    for j in range(w):ET.SubElement(cols,q("col"),{"min":str(j+1),"max":str(j+1),"width":str(widths[j]),"customWidth":"1"})
    sec=set(sections);data=ET.SubElement(root,q("sheetData"))
    for i,row in enumerate(matrix):
        section=main and i in sec
        ht=31 if main and i==0 else 58 if main and i==1 else 42 if section else 65 if main and max(len(old.val(v)) for v in row)>100 else 50 if main else 39 if i==0 else 44
        x=ET.SubElement(data,q("row"),{"r":str(i+1),"ht":str(ht),"customHeight":"1"})
        for j,v in enumerate(row):
            val=old.val(v)
            if not val:continue
            need(len(val)<=32767,"Excel text cell limit")
            style="band" if main and i==0 else "header" if main and i==1 else "section" if section else "band" if not main and i==0 else "alt" if i%2==0 else "data"
            c=ET.SubElement(x,q("c"),{"r":addr(i+1,j+1),"s":str(styles[style]),"t":"inlineStr"})
            tn=ET.SubElement(ET.SubElement(c,q("is")),q("t"))
            tn.set(q("space","http://www.w3.org/XML/1998/namespace"),"preserve");tn.text=val
    if main:
        merges=[("A1","D1"),("E1","I1"),("J1","N1")]+[("A"+str(i+1),"O"+str(i+1)) for i in sorted(sec)]
        mc=ET.SubElement(root,q("mergeCells"),{"count":str(len(merges))})
        for a,b in merges:ET.SubElement(mc,q("mergeCell"),{"ref":a+":"+b})
    ET.SubElement(root,q("pageMargins"),{"left":".3","right":".3","top":".45","bottom":".45","header":".15","footer":".15"})
    return ET.tostring(root,encoding="utf-8",xml_declaration=True)



def summary(m):
    return [
      ["SOSA-G2-7K original Gigabit Ethernet source / SAME 26-sheet Excel","C239 Ed1.1 original §13.5.2.3.2 Ethernet(Copper), PDF285/printed259; STOP BEFORE §13.5.2.3.3"],
      ["Approved canonical source grid","329 existing information rows, 346x15 complete review grid, 15 topic dividers"],
      ["Original native source items","Seven items: one nested heading, two numbered Rules, one descriptive context, two native companion pointers, prior J2 table reference"],
      ["Two numbered source SHALL Rules","Rule13.5.2.3.2-1 Gigabit Ethernet and Rule13.5.2.3.2-2 1000BaseT/cabling, both original Inspection(I)"],
      ["Physical source description","Eight wires, four twisted pairs, 100-ohm channel; not a live measurement"],
      ["Source IEEE edition","IEEE 802.3-2008, 1000BaseT; original external normative text NOT examined"],
      ["Source cabling","CAT 6A AS6070/6 or equivalent; actual companion/equivalence not verified"],
      ["Previously qualified J2 pin table","G2-7J Ethernet DA/DB/DC/DD physical pairs and shield references; original graphical geometry still held"],
      ["New exact holds","11 original G2-7K local holds plus earlier G2-7J 22 and all prior source holds retained"],
      ["Qualified existing-row master increment","10 SOSA column-I source-graded comparisons; zero case, other donor, ISA or DIM cells changed"],
      ["Original C239 corpus heading standing","173 at least sampled/inline-read, 18 unread, one restricted; no new registered heading"],
      ["Original evidence preserved","58 prior donor facts, 73 empirical case records, 480 ISA source outcomes, six exact unresolved ISA questions"],
      ["Adoption and external conformance","Zero approved DIM classes/fields/cardinality, CSAPI Profile SHALLs or real physical hardware tests"],
      ["SAME editable 26-sheet Excel","All actual 346x15 saved source cells match canonical JSON, BOTH CSV and BOTH readable Markdown; 22 historical sheets unchanged"],
      ["STOP / only new owner Proceed","G2-7L original §13.5.2.3.3 Serial Communications; SOSA OPEN and SAPIENT blocked"]
    ]

def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        groups=[r.get(name) or {} for name in ("G2_1_source_correspondence","G2_2_source_correspondence","G2_3_source_correspondence",
            "G2_4A_source_correspondence","G2_4B_source_correspondence","G2_5_source_correspondence","G2_6A_source_correspondence","G2_6B_source_correspondence","G2_6C_source_correspondence","G2_6D_source_correspondence","G2_7A_source_correspondence","G2_7B_source_correspondence","G2_7C_source_correspondence","G2_7D_source_correspondence","G2_7E_source_correspondence","G2_7F_source_correspondence","G2_7G_source_correspondence","G2_7H_source_correspondence","G2_7I_source_correspondence","G2_7J_source_correspondence","G2_7K_source_correspondence")]
        ids=so.get("records",[])+[v for g in groups for v in g.get("source_item_ids",[])]
        relations=so.get("relations",[])+[g.get("relation",g.get("mapping_relation","")) for g in groups if g]
        status=("G2-7K §13.5.2.3.2 Gigabit J2 physical channel, original two Inspection Rules, IEEE/AS6070/6 external originals held" if groups[-1] else
            "G2-7J §13.5.2.3 25-7 J2 pin/rule and physical Power Enable original text read, diagram/matrix held" if groups[-2] else
            "G2-7I §13.5 original Class1&2/J1 electrical Rules and table text, figures/SAE/MIL/VITA held" if groups[-3] else
            "G2-7H §13.4 original VNX textual/table review, numbered Rules absent and future/TBD + figure/native holds" if groups[-4] else
            "G2-7G §13.3.8 original analog/coax Rule/Rec/Obs and figure text read, full pixel geometry held" if groups[-5] else
            "G2-7F §13.3.7 original Rule/Observation/Permission text read" if groups[-6] else
            "G2-7E §13.3.6 VITA66 optical source text and original native companion held" if groups[-7] else
            "G2-7D §13.3.5 Switch AMPS dense matrix audit held" if groups[-8] else
            "G2-7C §13.3.4 Payload AMPS dense matrix audit held" if groups[-9] else
            "G2-7B AMPS grammar, original ANSI/VITA held" if groups[-10] else
            "G2-7A AMPS protocol code definitions read" if groups[-11] else
            "Earlier original C239 source-qualified review, native companions held" if so or any(groups[:-11]) else "Not assessed here")
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),
             r.get("master_inclusion",""),r.get("dim_adoption",""),"; ".join(r.get("source_entry_ids",[])),
             json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
             "; ".join(ids),"; ".join(relations),status])
    return out

def publish():
    m=load(MASTER);legacy=load(LEDGER);check_source(m,legacy);check_g2_7i_source(m);check_g2_7j_source(m);check_g2_7k_source(m)
    stored=(D/BOOK).read_bytes()
    if digest(stored)==OLD:prev=stored
    else:
        from subprocess import check_output
        need(digest(stored)==m["currentWorkbookSha256"] and m["workbookSnapshot"]["currently_matches_readable_view"],
             "current saved workbook hash/metadata before replay")
        prev=check_output(["git","show","1598eacbee201d83025dae68b9bc5b761db5166e:Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/Master_Donor_Concept_to_DIM_Crosswalk.xlsx"])
    need(digest(prev)==OLD,"unchanged prior source-qualified G2-7J workbook before G2-7K publication")
    with zipfile.ZipFile(io.BytesIO(prev)) as z:
        need(z.testzip() is None,"old saved ZIP CRC")
        paths=old.sheetpaths(z);need(len(paths)==26,"same original 26 sheets")
        styles,sty=old.newstyles(z.read("xl/styles.xml"))
        tables={"Master Crosswalk":m["review_grid"],"DIM Register":register(m),"Summary":summary(m),"Validation":summary(m)}
        replacements={"xl/styles.xml":styles}
        for name,rows in tables.items():
            replacements[paths[name]]=matrix_to_xml(rows,sty,main=name=="Master Crosswalk",
                    sections=m["review_sections"] if name=="Master Crosswalk" else ())
        retained={name:digest(z.read(path)) for name,path in paths.items() if name not in tables}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as dst:
            for info in z.infolist():dst.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as z:
        need(z.testzip() is None and list(old.sheetpaths(z))==list(paths),"saved ZIP CRC and original sheet list")
        for name,sha in retained.items():need(digest(z.read(paths[name]))==sha,"historical worksheet unchanged "+name)
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                need(not any(t.get("t")=="e" for t in ET.fromstring(z.read(path)).iter(q("c"))),"no saved spreadsheet error cell "+path)
        main=ET.fromstring(z.read(paths["Master Crosswalk"]))
        merges=[x.get("ref") for x in main.find(q("mergeCells")).findall(q("mergeCell"))]
        need(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],"original grouped header/topic dividers preserved")
        pane=main.find(q("sheetViews")).find(q("sheetView")).find(q("pane"))
        need(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","original frozen header/case columns")
    actual=old.readcells(saved,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for j,v in enumerate(row,1):need(actual.get(addr(i,j),"")==old.val(v),"actual saved 346x15 source cell "+addr(i,j))
    registerCells=old.readcells(saved,"DIM Register")
    need(sum(bool(re.fullmatch(r"A\d+",cell)) for cell in registerCells)==330,"DIM Register 329 stable row IDs retained")
    before=old.readcells(prev,"Master Crosswalk")
    delta=[a for a in set(before)|set(actual) if before.get(a,"")!=actual.get(a,"")]
    need(len(delta)==10 and all(re.fullmatch(r"I\d+",a) for a in delta),"10 exact SOSA-I changes only, no case/other-donor/ISA/DIM changes")
    if digest(stored)!=OLD:need(digest(saved)==digest(stored),"byte-for-byte replay of already-published same workbook")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7K_ORIGINAL_J2_GIGABIT_ETHERNET_TWO_RULES_AND_SAME_26_SHEET_EXCEL_VERIFIED__SOSA_OPEN"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7K-CANONICAL-VERIFIED","sha256":sha,
          "currently_matches_readable_view":True,
          "lag":"NONE: all 346x15 saved Excel cells match JSON/BOTH CSV/BOTH MD",
          "refreshed_cell_count":10,"validation_file":REPORT})
    m["SOSAEvidence"]["G2_7K"].update({"excel_checkpoint":"SOSA-G2-7K-CANONICAL-VERIFIED",
          "excel_validation":REPORT,"Excel_lag_cells":0,"same_saved_workbook_10_cells_synced":True})
    m["SOSAReviewCompletion"]["G2_7K_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="OPEN__G2_7K_SAME_SAVED_EXCEL_VERIFIED__18_UNREAD_1_RESTRICTED_IEEE_CABLE_SOURCE_HOLDS"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="Only distinct owner Proceed starts G2-7L original C239 §13.5.2.3.3 Serial Communications, source-sized; SOSA OPEN"
    m["nextOwnerAction"]="Only distinct owner Proceed starts G2-7L original C239 §13.5.2.3.3; SOSA ACTIVE and SAPIENT blocked"
    m["publicationPolicy"]="L23 G2-7K: 10 original source-qualified Gigabit J2 column-I cells synchronized in canonical JSON/BOTH CSV/BOTH GitHub-readable Markdown and SAME original 26-sheet Excel; all 346x15 saved cells verified; IEEE/AS6070/6 source originals remain held"
    save(MASTER,m)
    record={"date":"2026-11-11","step":"SOSA-G2-7K-EXCEL-CHECKPOINT",
       "result":"SAME_26_SHEET_SAVED_XLSX_AND_BOTH_CSV_AND_BOTH_MD_PARITY_PASS",
       "workbook_sha256":sha,"base_workbook_sha256":OLD,"workbook_sheets":list(paths),
       "refreshed_sheets":list(tables),"exact_original_untouched_xml_sha256":retained,
       "information_rows":329,"grid_rows":346,"columns":15,
       "original_donor_evidence":58,"case_evidence":73,"ISA_primary_source_outcomes":480,"original_ISA_questions_open":6,
       "G2_7K_new_registered_headings":0,"G2_7K_original_native_items":7,"G2_7K_rules":2,
       "G2_7K_rule_method_I":2,"G2_7K_unnumbered_physical_context":1,
       "G2_7K_external_normative_companion_pointers":2,"G2_7K_source_holds":11,
       "G2_7K_qualified_existing_sosa_cells":10,"changed_saved_cells":sorted(delta),
       "C239_at_least_sampled_or_inline_read":173,"C239_unread":18,"C239_restricted":1,
       "IEEE802_3_2008_original_examined":False,"AS6070_6_original_examined":False,
       "original_J2_table_graphics_verified":False,"native_C239_eight_companions_examined":False,
       "earlier_G2_7J_holds":22,"earlier_G2_7I_holds":20,
       "checks":{"all_actual_XLSX_346x15_cells_equal_JSON_both_CSV_both_MD":True,
           "both_CSVs_equal":True,"both_readable_MDs_equal":True,
           "same_26_worksheet_names_order":True,"22_untouched_historical_XMLs_preserved":True,
           "only_10_SOSA_I_cells_changed":True,"valid_ZIP_CRC_and_XML":True,
           "no_spreadsheet_error_cells":True,"zero_DIM_Profile_adoption":True},
       "limits":["Original C239 §13.5.2.3.2 only; stops before Serial Communications §13.5.2.3.3",
         "Only two numbered Inspection SHALL Rules and separate descriptive 8-wire/four-pair/100-ohm context",
         "Referenced IEEE802.3-2008 and AS6070/6 companion originals NOT independently reviewed",
         "Original six-page J2 table pixel geometry and modality matrix still held from G2-7J",
         "No installed physical Ethernet, IP network, hardware conformance or CSAPI service inferred",
         "Unreviewed external/native companions, later S251 and restricted AppendixC remain held",
         "Preview rendered from saved Excel XML source values, not native Excel screenshot"],
       "next":"Only distinct owner Proceed starts G2-7L original C239 §13.5.2.3.3 Serial Communications; SOSA ACTIVE/OPEN and SAPIENT Step18 blocked"}
    save(REPORT,record)
    print("PASS: G2-7K original J2 Gigabit two Inspection Rules and 10 same-Excel SOSA cells, SHA",sha)
    return sha

def preview():
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER);actual=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_7K_source_correspondence")]
    need(len(rows)==10,"10 G2-7K source-qualified J2 Ethernet donor comparisons saved")
    try:
        font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:font=bold=ImageFont.load_default()
    width,height=1580,1200
    img=Image.new("RGB",(width,height),"white")
    pen=ImageDraw.Draw(img);pen.rectangle((0,0,width,65),fill="#173855")
    pen.text((18,17),"SOSA-G2-7K: 10 saved J2 1000BaseT Ethernet source cells — C239 §13.5.2.3.2",font=bold,fill="white")
    for i,r in enumerate(rows):
        hit=[k+1 for k,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(hit)==1,"unique original source row "+r["row_id"])
        address="I"+str(hit[0]);value=actual.get(address,"")
        need(value==r["display"][8],"actual source cell from saved original Excel "+address)
        y=72+i*98
        pen.rectangle((10,y,width-12,y+91),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        pen.text((20,y+7),r["row_id"]+" | "+address+" | "+r["label"],font=bold,fill="#173855")
        snippet="G2-7K: "+value.split("G2-7K:",1)[1] if "G2-7K:" in value else value
        for j,line in enumerate(textwrap.wrap(snippet,width=165,break_long_words=False)[:3]):
            pen.text((20,y+33+j*17),line,font=font,fill="#203951")
    img.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>10000,"saved source-cell preview generated")
    print("PASS: 10 G2-7K SOSA original source-cell preview rendered from saved worksheet XML")

# Consolidated owner-approved G2-7L — the existing publisher and the SAME original 26-sheet workbook.
def check_g2_7l_source(z,m=None):
    c=z["counts"];native=z["original_source_items"];ids={x["id"] for x in native}
    need(len(ids)==len(native)==148 and c["total_unique_native_evidence_records"]==148,
         "G2-7L exactly 148 typed original-source records")
    need(c["source_numbered_rule_shalls"]==48 and c["numbered_observations"]==6
         and c["numbered_recommendations_should"]==2 and c["numbered_permissions_may"]==1
         and c["source_headings"]==23 and c["table_texts"]==4
         and c["table_pin_rows"]==34 and c["figure_captions"]==4,
         "48 native SHALL,6 observations,2 SHOULD,1 MAY and complete J2-J6 table/heading census")
    need(len([x for x in native if x["kind"]=="RULE"])==48
         and all(x["modal_verb"]=="shall" and x["conformance_methodology_printed"]
                 for x in native if x["kind"]=="RULE"),
         "all 48 original rule IDs, normative SHALLs and printed verification methods")
    required_repetitions=z["source_repetitions"]
    need(required_repetitions["duplicate_rules"]==["13.5.2.7.1-4","13.5.2.7.1-5"]
         and required_repetitions["repeated_recommendations"]==["13.5.2.7.1-1","13.5.2.7.1-2"],
         "retain distinct printed duplicate-looking current J6 source requirements and recommendations")
    need(len(z["qualified_existing_row_mappings"])==24 and len(z["exact_holds"])==19
         and all(a["source_item_ids"] and all(s in ids for s in a["source_item_ids"])
                 for a in z["qualified_existing_row_mappings"]),
         "24 cited original source-qualified master labels and 19 exact holds")
    cov=z["c239_registered_heading_standing"]
    need((cov["registered"],cov["at_least_sampled_or_inline_read"],
          cov["substantively_unread"],cov["restricted"])==(192,173,18,1)
         and cov["new_registered_headings_earned"]==0,
         "nested subsection not falsely adding a registered heading")
    need(z["DIM_Profile_adopted"] is False and z["independent_equipment_conformance"] is False
         and z["source"]["source_figure_pixels_verified"] is False
         and z["source"]["external_companion_originals_read"] is False,
         "original external/figure holds and no DIM/CSAPI/hardware adoption")
    if m is not None:
        updated=[x for x in m["rows"] if x.get("G2_7L_source_correspondence")]
        need(len(updated)==24 and {x["row_id"] for x in updated}==
             set(m["workbookSnapshot"]["G2_7L_affected_row_ids"]),
             "24 exact existing source-qualified rows, no new class or source-case rows")
        for x in updated:
            v=x["G2_7L_source_correspondence"]
            need(all(t in ids for t in v["source_item_ids"])
                 and x["display"][8].startswith(v["previous_sosa_cell_value"])
                 and "G2-7L:" in x["display"][8]
                 and v["DIM_Profile_adopted"] is False,
                 "source cited append-only donor meaning "+x["row_id"])
    return True

def summary_g2_7l(m):
    return [
      ["SOSA-G2-7L original C239 J2–J6 consolidated source and SAME 26-sheet Excel","2023 C239 Ed1.1 §§13.5.2.3.3–13.5.2.7.2, PDF pp285–295, STOP before J7"],
      ["Native SOURCE item standing","48 SHALL Rules, 6 Observations, 2 SHOULD Recommendations, 1 MAY Permission; 148 distinct classified records"],
      ["Original table accountability","Four J3/J4/J5/J6 tables, 34 pin-rows, 4 figure captions; original pixels/modalities not verified"],
      ["J2 safety meaning","Hardwired MASTER_ARM, emission annunciation, NEZ mode and memory purge; not authenticated CSAPI Commands"],
      ["J3 copper video","Six SMPTE digital channels, four analog/composite contacts, one unused; not observed footage or DataStream"],
      ["J4 optical source","Four transmit/receive paths and 3 video fibers, original optical Standards referenced but not independently audited"],
      ["J5 antenna","Conditional GPS external antenna, not observed source location or verified clock"],
      ["J6 auxiliary platform DC","Five 28V/return pairs + safety contact; 25A/2s inrush, 15A steady, ≥1MΩ isolation, ≤0.1Ω grounding"],
      ["Exact J6 original repetitions","Separate Rules 13.5.2.7.1-4/-5 and Recommendations -1/-2 retained, no method imported from one to other"],
      ["Current qualified master updates","Exactly 24 existing The Open Group SOSA column-I comparison cells; prior information preserved"],
      ["C239 heading coverage","173 at least sampled/inline-read, 18 substantively unread, one restricted; nested parent remains PARTIAL"],
      ["Original evidence preserved","Original 329 information rows, four empirical cases, 58 prior donor facts, ISA480 outcomes / 6 questions"],
      ["Saved workbook integrity","SAME 26-sheet editable Excel, 22 untouched historic worksheets, all 346x15 saved cells match"],
      ["Source/model scope","19 local holds + prior holds; no DIM/CSAPI Profile adoption or independent hardware/runtime conformance"],
      ["STOP / only next owner Proceed","SOSA-G2-7M original §§13.5.2.8–13.5.2.12 ONLY"]
    ]

def register_g2_7l(m):
    result=register(m)
    for i,row in enumerate(m["rows"],1):
        ev=row.get("G2_7L_source_correspondence")
        if ev:
            result[i][9]+="; "+"; ".join(ev["source_item_ids"])
            result[i][10]+="; "+ev["relation"]
            result[i][11]="G2-7L original J2-J6 hardware signal/safety/video/fiber/GPS/28V source; external and figure holds; no actual operation"
    return result

def publish_g2_7l():
    from html import escape,unescape
    p="SOSA_G2_7L_Original_Source_Item_Coverage_11NOV2026.json"
    report="SOSA_G2_7L_Workbook_Validation_11NOV2026.json"
    preview_name="SOSA_G2_7L_Workbook_Preview_11NOV2026.png"
    base="0447f9935224d2ae1b8b2bfbfa9f9aeba9fa34b1461e440a3f17210e6b203a20"
    m=load(MASTER);legacy=load(LEDGER);z=load(p)
    need(check_g2_7l_source(z),"original-source ledger check")
    check_source(m,legacy);check_g2_7i_source(m);check_g2_7j_source(m);check_g2_7k_source(m)
    stored=(D/BOOK).read_bytes()
    need(digest(stored)==base and m["currentWorkbookSha256"]==base
         and m["workbookSnapshot"]["currently_matches_readable_view"],
         "G2-7K same 26-sheet actual saved workbook must precede G2-7L")
    deltas={}
    for item in z["qualified_existing_row_mappings"]:
        label=item["label"]
        found=[r for r in m["rows"] if r["label"]==label]
        need(len(found)==1 and label not in deltas,
             "exact approved unique master row label "+label)
        row=found[0];previous=row["display"][8]
        need("G2-7L:" not in previous,"G2-7L not already integrated in this source row")
        addition=(" · G2-7L: "+item["native_source_meaning"]+
                  " ["+item["relation"]+"; "+item["negative_equivalence_boundary"]+"]")
        new=previous+addition
        need(len(new)<=32767,"Excel cell text limit "+label)
        row["display"][8]=new
        row["G2_7L_source_correspondence"]={
            "source_item_ids":item["source_item_ids"],
            "native_source_meaning":item["native_source_meaning"],
            "relation":item["relation"],
            "negative_equivalence_boundary":item["negative_equivalence_boundary"],
            "previous_sosa_cell_value":previous,
            "DIM_Profile_adopted":False,
            "external_companions_and_figure_pixels_unverified":True,
            "independent_hardware_or_runtime_operation":False
        }
        deltas[label]=new
    need(len(deltas)==24,"exactly 24 justified existing-row donor comparisons")
    info=[i for i in range(2,len(m["review_grid"])) if i not in set(m["review_sections"])]
    need(len(info)==329,"original 329 information grid positions")
    for index,row in zip(info,m["rows"]):
        need(m["review_grid"][index][14]==row["label"],"retained approved row sequence "+row["row_id"])
        m["review_grid"][index][8]=row["display"][8]
    row_ids=[r["row_id"] for r in m["rows"] if r.get("G2_7L_source_correspondence")]
    m["workbookSnapshot"]["G2_7L_affected_row_ids"]=row_ids
    m["SOSAEvidence"]["G2_7L"]={
       "sourceLedger":p,"sourceReview":"SOSA_G2_7L_Original_Source_and_Master_Reconciliation_11NOV2026.md",
       "qualified_existing_row_matches":24,"exact_holds":19,"original_numbered_shall_rules":48,
       "source_edition":"The Open Group C239 Edition 1.1 (2023)",
       "full_source_inline_review":"§§13.5.2.3.3–13.5.2.7.2, PDF285–295",
       "original_external_normative_and_visual_holds":True,
       "DIM_Profile_adopted":False}
    m["SOSAReviewCompletion"]["G2_7L_XLSX_lag"]=24
    check_g2_7l_source(z,m)
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/name).open("w",encoding="utf-8",newline="") as f:
            csv.writer(f,lineterminator="\r\n").writerows(m["review_grid"])
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        original=(D/name).read_text(encoding="utf-8")
        def update_tr(match):
            tr=match.group(0); cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            label=unescape(cells[14].group(1))
            if label not in deltas:return tr
            cell=cells[8]
            return tr[:cell.start(1)]+escape(deltas[label],quote=True)+tr[cell.end(1):]
        revised=re.sub(r"<tr>.*?</tr>",update_tr,original,flags=re.S)
        need(revised!=original and revised.count("G2-7L:")>=24,
             "source-qualified GitHub-readable table updated "+name)
        (D/name).write_text(revised,encoding="utf-8")
    check_source(m,legacy)
    with zipfile.ZipFile(io.BytesIO(stored)) as prev:
        need(prev.testzip() is None,"old G2-7K workbook ZIP CRC")
        paths=old.sheetpaths(prev);need(len(paths)==26,"same original 26 sheets")
        styles,sty=old.newstyles(prev.read("xl/styles.xml"))
        tables={"Master Crosswalk":m["review_grid"],"DIM Register":register_g2_7l(m),
                "Summary":summary_g2_7l(m),"Validation":summary_g2_7l(m)}
        changes={"xl/styles.xml":styles}
        for name,rows in tables.items():
            changes[paths[name]]=matrix_to_xml(rows,sty,main=name=="Master Crosswalk",
                         sections=m["review_sections"] if name=="Master Crosswalk" else ())
        retained={name:digest(prev.read(path)) for name,path in paths.items() if name not in tables}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as dst:
            for item in prev.infolist():
                dst.writestr(item,changes.get(item.filename,prev.read(item.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as wb:
        need(wb.testzip() is None and list(old.sheetpaths(wb))==list(paths),
             "SAME 26 sheet names and valid ZIP")
        for name,hashval in retained.items():
            need(digest(wb.read(paths[name]))==hashval,"22 historical sheet XMLs unchanged "+name)
        for path in wb.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(wb.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                need(not any(c.get("t")=="e" for c in ET.fromstring(wb.read(path)).iter(q("c"))),
                     "no spreadsheet errors")
        main=ET.fromstring(wb.read(paths["Master Crosswalk"]))
        merges=[x.get("ref") for x in main.find(q("mergeCells")).findall(q("mergeCell"))]
        need(merges==["A1:D1","E1:I1","J1:N1"]+
             [f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "owner-approved 15 topic dividers and grouped header layout")
    actual=old.readcells(saved,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for j,v in enumerate(row,1):
            need(actual.get(addr(i,j),"")==old.val(v),"SAME Excel saved cell "+addr(i,j))
    former=old.readcells(stored,"Master Crosswalk")
    delta=[key for key in set(former)|set(actual) if former.get(key,"")!=actual.get(key,"")]
    need(len(delta)==24 and all(re.fullmatch(r"I\d+",x) for x in delta),
         "exactly 24 SOSA donor I-cell changes, zero other donor/case/ISA/DIM")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7L_CONSOLIDATED_J2_J6_48_RULES_24_DONOR_CELLS_SAME_26_SHEET_EXCEL_VERIFIED__SOSA_OPEN"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7L-CANONICAL-VERIFIED",
      "sha256":sha,"currently_matches_readable_view":True,
      "lag":"NONE: all 346x15 saved Excel cells match JSON/BOTH CSV/BOTH MD",
      "refreshed_cell_count":24,"validation_file":report})
    m["SOSAEvidence"]["G2_7L"].update({"excel_checkpoint":"SOSA-G2-7L-CANONICAL-VERIFIED",
        "excel_validation":report,"Excel_lag_cells":0,"same_saved_workbook_24_cells_synced":True})
    m["SOSAReviewCompletion"]["G2_7L_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="OPEN__G2_7L_CONSOLIDATED_SAME_SAVED_EXCEL_VERIFIED__18_UNREAD_1_RESTRICTED__EXTERNAL_AND_FIGURE_HOLDS"
    nextstep="Only distinct owner Proceed starts consolidated SOSA-G2-7M original C239 §§13.5.2.8–13.5.2.12; SOSA ACTIVE/OPEN, Step18 SAPIENT blocked"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]=nextstep
    m["nextOwnerAction"]=nextstep
    m["publicationPolicy"]="L23 G2-7L: 24 original-source-qualified J2-J6 SOSA donor column I cells synced in canonical JSON, BOTH CSV/MD, SAME 26-sheet Excel; 346x15 saved cells independently verified; source companion/figure holds retained"
    save(MASTER,m)
    result={"date":"2026-11-11","step":"SOSA-G2-7L-CONSOLIDATED-SAME-EXCEL-CHECKPOINT",
      "result":"ORIGINAL_C239_SOURCE_AND_SAME_26_SHEET_SAVED_XLSX_AND_BOTH_CSV_MD_PARITY_PASS",
      "workbook_sha256":sha,"base_workbook_sha256":base,"workbook_sheets":list(paths),
      "refreshed_sheets":list(tables),"exact_original_untouched_xml_sha256":retained,
      "information_rows":329,"grid_rows":346,"columns":15,
      "original_donor_evidence":58,"case_evidence":73,"ISA_primary_source_outcomes":480,"original_ISA_questions_open":6,
      "G2_7L_source_native_items":148,"G2_7L_numbered_RULE_SHALL":48,
      "G2_7L_observations":6,"G2_7L_recommendations":2,"G2_7L_permission":1,
      "G2_7L_table_pin_rows":34,"G2_7L_figure_captions":4,
      "G2_7L_exact_holds":19,"G2_7L_qualified_existing_sosa_cells":24,
      "changed_saved_cells":sorted(delta),"C239_at_least_sampled_or_inline_read":173,
      "C239_unread":18,"C239_restricted":1,
      "source_original_external_companions_examined":False,"source_figure_pixels_verified":False,
      "original_C239_eight_companions_examined":False,
      "checks":{"all_actual_XLSX_346x15_cells_equal_JSON_both_CSV_both_MD":True,
       "both_CSVs_equal":True,"both_readable_MDs_equal":True,
       "same_26_worksheet_names_order":True,"22_untouched_historical_XMLs_preserved":True,
       "only_24_SOSA_I_cells_changed":True,"valid_ZIP_CRC_and_XML":True,
       "no_spreadsheet_error_cells":True,"zero_DIM_Profile_adoption":True},
      "limits":["§§13.5.2.3.3–13.5.2.7.2 only, stop before J7",
        "Original C239 PDF285–295 inline source/4 table texts/4 captions, figure pixels and dense modality matrices held",
        "19 local source/external normative/specification and physical operation holds",
        "Two printed 15A J6 Rules and two repeated SHOULD Recommendations separately preserved",
        "No actual installed J2-J6 evidence, no CSAPI control, time sync or video reporting inferred",
        "Preview rendered from saved Excel XML, not native Excel application screenshot"],
      "next":nextstep}
    save(report,result)
    preview_g2_7l(m,actual,preview_name)
    print("PASS: G2-7L ORIGINAL 48 SHALL/6 Observations/2 SHOULD/1 MAY, 24 qualified SOSA cells, 346x15 actual saved Excel, sha",sha)
    return sha

def preview_g2_7l(m,actual,filename):
    from PIL import Image,ImageDraw,ImageFont
    rows=[r for r in m["rows"] if r.get("G2_7L_source_correspondence")]
    need(len(rows)==24,"G2-7L 24 saved source-qualified rows in visual preview")
    try:
        normal=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:normal=bold=ImageFont.load_default()
    width,height=1580,2620
    img=Image.new("RGB",(width,height),"white")
    pen=ImageDraw.Draw(img);pen.rectangle((0,0,width,67),fill="#173855")
    pen.text((20,17),"SOSA-G2-7L: 24 independently saved J2-J6 source comparisons — C239 original §§13.5.2.3.3–13.5.2.7.2",font=bold,fill="white")
    for i,row in enumerate(rows):
        matches=[k+1 for k,x in enumerate(m["review_grid"]) if x[14]==row["label"] and x[8]==row["display"][8]]
        need(len(matches)==1,"unique saved row "+row["row_id"])
        address="I"+str(matches[0]);value=actual.get(address,"")
        need(value==row["display"][8],"preview draws actual saved source cell "+address)
        y=71+i*105
        pen.rectangle((12,y,width-12,y+99),fill="#F1F6FA" if i%2==0 else "white",outline="#CDD7E3")
        pen.text((20,y+7),row["row_id"]+" | "+address+" | "+row["label"],font=bold,fill="#173855")
        segment=value.split("G2-7L:",1)[-1]
        for n,fragment in enumerate(textwrap.wrap("G2-7L: "+segment,width=160,break_long_words=False)[:3]):
            pen.text((20,y+35+n*17),fragment,font=normal,fill="#203951")
    img.save(D/filename,optimize=True)
    need((D/filename).stat().st_size>12000,"rendered from saved worksheet XML evidence preview")


# Reconcile a pre-existing G2-7L workbook publication whose old workflow
# committed JSON/XLSX but failed to stage BOTH CSV and BOTH readable Markdown mirrors.
# This is a bounded L23 publication repair, not a new native-source packet.
def reconcile_existing_g2_7l_publication():
    from html import escape,unescape
    from subprocess import check_output
    z=load("SOSA_G2_7L_Original_Source_Item_Coverage_11NOV2026.json")
    m=load(MASTER);legacy=load(LEDGER)
    check_g2_7l_source(z,m)
    need(m["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7L-CANONICAL-VERIFIED"
         and m["workbookSnapshot"]["refreshed_cell_count"]==24
         and m["workbookSnapshot"]["currently_matches_readable_view"]
         and m["SOSAReviewCompletion"]["G2_7L_XLSX_lag"]==0,
         "already generated SAME workbook source metadata G2-7L")
    saved=(D/BOOK).read_bytes();sha=digest(saved)
    need(sha==m["currentWorkbookSha256"]==m["workbookSnapshot"]["sha256"],
         "current G2-7L saved workbook SHA equals published JSON metadata")
    labels={row["label"]:row["display"][8] for row in m["rows"]
            if row.get("G2_7L_source_correspondence")}
    need(len(labels)==24,"24 distinct original source-qualified comparison labels")
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/n).open("w",encoding="utf-8",newline="") as f:
            csv.writer(f,lineterminator="\r\n").writerows(m["review_grid"])
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        original=(D/n).read_text(encoding="utf-8")
        def swap(match):
            tr=match.group(0);cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            label=unescape(cells[14].group(1))
            if label not in labels:return tr
            c=cells[8]
            return tr[:c.start(1)]+escape(labels[label],quote=True)+tr[c.end(1):]
        repaired=re.sub(r"<tr>.*?</tr>",swap,original,flags=re.S)
        need(repaired!=original and repaired.count("G2-7L:")>=24,
             "four source comparison mirrors were genuinely older "+n)
        (D/n).write_text(repaired,encoding="utf-8")
    check_source(m,legacy);check_g2_7k_source(m);check_g2_7l_source(z,m)
    base="0447f9935224d2ae1b8b2bfbfa9f9aeba9fa34b1461e440a3f17210e6b203a20"
    orig=check_output(["git","show","b6f83669748ea2753a7907e81562ce0c316aeeb5:"+
         "Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/"+BOOK])
    need(digest(orig)==base,"old original G2-7K workbook historical bytes present")
    before=old.readcells(orig,"Master Crosswalk")
    after=old.readcells(saved,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for j,value in enumerate(row,1):
            need(after.get(addr(i,j),"")==old.val(value),
                 "repaired source and published saved 346x15 cell "+addr(i,j))
    delta=sorted([key for key in set(before)|set(after)
                  if before.get(key,"")!=after.get(key,"")])
    need(len(delta)==24 and all(re.fullmatch(r"I\d+",key) for key in delta),
         "exact 24 saved SOSA-only donor cells; case/ISA/other donors/DIM preserved")
    with zipfile.ZipFile(io.BytesIO(saved)) as wb:
        need(wb.testzip() is None,"saved original workbook ZIP CRC valid")
        paths=old.sheetpaths(wb);need(len(paths)==26,"same 26 worksheet names and order")
        unchanged={name:digest(wb.read(path)) for name,path in paths.items()
                   if name not in ("Master Crosswalk","DIM Register","Summary","Validation")}
        need(len(unchanged)==22,"all 22 original historical worksheets unchanged")
        former=load("SOSA_G2_7K_Workbook_Validation_11NOV2026.json")
        need(unchanged==former["exact_original_untouched_xml_sha256"],
             "historical 22 sheets byte identical to independently verified G2-7K snapshot")
        for path in wb.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(wb.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                need(not any(x.get("t")=="e" for x in ET.fromstring(wb.read(path)).iter(q("c"))),
                     "no spreadsheet error cells")
        main=ET.fromstring(wb.read(paths["Master Crosswalk"]))
        merges=[x.get("ref") for x in main.find(q("mergeCells")).findall(q("mergeCell"))]
        need(merges==["A1:D1","E1:I1","J1:N1"]+
             [f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "approved grouped foundation layout and 15 topic dividers")
        pane=main.find(q("sheetViews")).find(q("sheetView")).find(q("pane"))
        need(pane.get("xSplit")=="4" and pane.get("ySplit")=="2",
             "original four case columns and frozen headers")
    report="SOSA_G2_7L_Workbook_Validation_11NOV2026.json"
    record={"date":"2026-11-11","step":"SOSA-G2-7L-CONSOLIDATED-SAVED-EXCEL-PUBLICATION-RECOVERY",
      "result":"ORIGINAL_SOURCE_AND_SAME_26_SHEET_SAVED_XLSX_AND_BOTH_CSV_MD_PARITY_PASS",
      "workbook_sha256":sha,"base_workbook_sha256":base,"workbook_sheets":list(paths),
      "refreshed_sheets":["Master Crosswalk","DIM Register","Summary","Validation"],
      "exact_original_untouched_xml_sha256":unchanged,
      "information_rows":329,"grid_rows":346,"columns":15,"original_donor_evidence":58,
      "case_evidence":73,"ISA_primary_source_outcomes":480,"original_ISA_questions_open":6,
      "G2_7L_source_native_items":148,"G2_7L_numbered_RULE_SHALL":48,
      "G2_7L_observations":6,"G2_7L_recommendations":2,"G2_7L_permission":1,
      "G2_7L_table_pin_rows":34,"G2_7L_figure_captions":4,"G2_7L_exact_holds":19,
      "G2_7L_qualified_existing_sosa_cells":24,"changed_saved_cells":delta,
      "C239_at_least_sampled_or_inline_read":173,"C239_unread":18,"C239_restricted":1,
      "source_original_external_companions_examined":False,
      "source_figure_pixels_verified":False,"original_C239_eight_companions_examined":False,
      "checks":{"all_actual_XLSX_346x15_cells_equal_JSON_both_CSV_both_MD":True,
        "both_CSVs_equal":True,"both_readable_MDs_equal":True,
        "same_26_worksheet_names_order":True,"22_untouched_historical_XMLs_preserved":True,
        "only_24_SOSA_I_cells_changed":True,"valid_ZIP_CRC_and_XML":True,
        "no_spreadsheet_error_cells":True,"zero_DIM_Profile_adoption":True},
      "limits":["Consolidated original C239 §§13.5.2.3.3–13.5.2.7.2 only, STOP before J7",
        "Four original figure geometries and source external original standards held",
        "No actual device control, video stream, power measurement or conformance",
        "Historical workflow committed source JSON/XLSX before both CSV/MD; this pass repaired mirrors and reverified pre-existing saved workbook byte-exact",
        "Preview derived from saved Excel XML, not native Excel application"],
      "next":"Only distinct owner Proceed starts SOSA-G2-7M original §§13.5.2.8–13.5.2.12; SAPIENT blocked"}
    save(report,record)
    preview_g2_7l(m,after,"SOSA_G2_7L_Workbook_Preview_11NOV2026.png")
    print("PASS: G2-7L repaired both CSV/both readable MD against existing original saved Excel; 346x15, 24 I cells, 22 historical sheets, SHA",sha)


# Consolidated source-sized G2-7M publisher. One source pass, one canonical workbook.
def check_g2_7m_source(z, m=None):
    c=z["counts"]; items=z["original_source_items"]; ids={x["id"] for x in items}
    need(len(items)==len(ids)==173 and c["source_records"]==173,"G2-7M 173 disjoint native/source records")
    for kind,count in (("RULE",27),("OBSERVATION",2),("NESTED_SECTION",12),
                       ("TABLE",6),("FIGURE_CAPTION",5),("UNNUMBERED_SHALL_IN_TABLE",1)):
        need(sum(x["kind"]==kind for x in items)==count,"source type "+kind)
    need(c["table_rows"]==102 and c["source_exact_holds"]==19
         and len(z["qualified_existing_row_mappings"])==21
         and len(z["exact_holds"])==19,"102 original table rows, 21 mapping decisions, 19 local holds")
    rules=[x for x in items if x["kind"]=="RULE"]
    need(len({x["source_id"] for x in rules})==27
         and sum(x["conformance_methodology"]==["I"] for x in rules)==26
         and sum(x["conformance_methodology"]==["A"] for x in rules)==1
         and next(x for x in rules if x["source_id"]=="13.5.2.9-3")["conformance_methodology"]==["A"],
         "27 native SHALLs; one J8 Analysis, 26 Inspection")
    need(sum(x["kind"]=="UNNUMBERED_SHALL_IN_TABLE" for x in items)==1
         and sum(x["kind"]=="EXTERNAL_ORIGINAL_POINTER" for x in items)==11,
         "one J7 table shell-plating shall separate from numbered Rules; external originals unexamined")
    group=z["original_table_groups_accounted"]
    need(group=={"J7":66,"J8":19,"J9":8,"Aux":4,"VSWR":5},
         "all J7/J8/J9/auxiliary/VSWR native original table rows")
    need({x["max_gated_mated_pair_vswr"] for x in items if x["kind"]=="TABLE_ROW" and x.get("source_table")=="13.5.2.10-1"}
         =={"1.25:1","1.30:1","1.40:1","1.60:1"}
         and len([x for x in items if x["kind"]=="TABLE_ROW" and x.get("source_table")=="13.5.2.11.1-1"])==1,
         "original four J8 frequency VSWR limits and one J9 limit")
    need(z["source"]["source_figure_pixels_verified"] is False
         and z["source"]["original_external_companions_examined"] is False
         and z["source"]["eight_native_model_interface_files_examined"] is False
         and z["DIM_Profile_adopted"] is False
         and z["independent_runtime_or_hardware_conformance"] is False,
         "unexamined figures/native originals and zero DIM/CSAPI/runtime conformance")
    cov=z["original_c239_registered_heading_standing"]
    need((cov["registered"],cov["at_least_sampled_or_inline_read"],
          cov["substantively_unread"],cov["restricted"],cov["new_registered_heading_credit"])
         ==(192,173,18,1,0),"nested source cannot inflate 192-heading coverage")
    need(all(x["source_item_ids"] and all(y in ids for y in x["source_item_ids"])
             for x in z["qualified_existing_row_mappings"]),"all row findings cite actual original source IDs")
    if m is not None:
        mapped=[r for r in m["rows"] if r.get("G2_7M_source_correspondence")]
        need(len(mapped)==21 and {r["row_id"] for r in mapped}
             ==set(m["workbookSnapshot"]["G2_7M_affected_row_ids"]),
             "21 source-qualified existing rows only, approved crosswalk shape")
        for r in mapped:
            ev=r["G2_7M_source_correspondence"]
            need(r["display"][8].startswith(ev["previous_sosa_cell_value"])
                 and "G2-7M:" in r["display"][8]
                 and all(x in ids for x in ev["source_item_ids"])
                 and ev["DIM_Profile_adopted"] is False
                 and ev["original_figure_and_companions_held"] is True,
                 "append-only native-source-qualified SOSA text "+r["row_id"])

def publish_g2_7m():
    from html import escape, unescape
    ledger_name="SOSA_G2_7M_Original_Source_Item_Coverage_11NOV2026.json"
    report_name="SOSA_G2_7M_Workbook_Validation_11NOV2026.json"
    base_sha="89a582868a90891a8046c1a3e2a7f86270ac827faa1793637b2967a6aa21cf3d"
    m=load(MASTER);z=load(ledger_name);prior=load(LEDGER)
    check_source(m,prior)
    check_g2_7l_source(load("SOSA_G2_7L_Original_Source_Item_Coverage_11NOV2026.json"),m)
    check_g2_7m_source(z)
    previous=(D/BOOK).read_bytes()
    need(digest(previous)==base_sha==m["currentWorkbookSha256"]
         and m["workbookSnapshot"]["currently_matches_readable_view"],
         "L23 original same G2-7L 26-sheet Excel and all mirrors must begin current")
    findings={}
    for v in z["qualified_existing_row_mappings"]:
        choices=[r for r in m["rows"] if r["label"]==v["label"]]
        need(len(choices)==1 and v["label"] not in findings,"unique pre-existing master row label")
        r=choices[0];before=r["display"][8]
        need("G2-7M:" not in before,"this source packet not already applied")
        after=before+" · G2-7M: "+v["source_native_meaning"]+" ["+v["relation"]+"; "+v["negative_equivalence_boundary"]+"]"
        need(len(after)<=32767,"original Excel text cell length")
        r["display"][8]=after
        r["G2_7M_source_correspondence"]={
            "source_item_ids":v["source_item_ids"],"relation":v["relation"],
            "source_native_meaning":v["source_native_meaning"],
            "negative_equivalence_boundary":v["negative_equivalence_boundary"],
            "previous_sosa_cell_value":before,
            "DIM_Profile_adopted":False,
            "original_figure_and_companions_held":True,
            "independent_runtime_conformance":False}
        findings[v["label"]]=after
    need(len(findings)==21,"only 21 new J7-J9/auxiliary RF meanings")
    positions=[i for i in range(2,len(m["review_grid"])) if i not in set(m["review_sections"])]
    need(len(positions)==len(m["rows"])==329,"original 329 stable information rows")
    for i,r in zip(positions,m["rows"]):
        need(m["review_grid"][i][14]==r["label"],"no reordered source row")
        m["review_grid"][i][8]=r["display"][8]
    ids=[r["row_id"] for r in m["rows"] if r.get("G2_7M_source_correspondence")]
    m["workbookSnapshot"]["G2_7M_affected_row_ids"]=ids
    check_g2_7m_source(z,m)
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/n).open("w",newline="",encoding="utf-8") as f:
            csv.writer(f,lineterminator="\r\n").writerows(m["review_grid"])
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        oldmd=(D/n).read_text(encoding="utf-8")
        def replace(match):
            tr=match.group(0);cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            label=unescape(cells[14].group(1))
            if label not in findings:return tr
            old=cells[8]
            return tr[:old.start(1)]+escape(findings[label],quote=True)+tr[old.end(1):]
        newmd=re.sub(r"<tr>.*?</tr>",replace,oldmd,flags=re.S)
        need(newmd!=oldmd and newmd.count("G2-7M:")>=21,"new source evidence in readable master "+n)
        (D/n).write_text(newmd,encoding="utf-8")
    check_source(m,prior)
    with zipfile.ZipFile(io.BytesIO(previous)) as original:
        need(original.testzip() is None,"previous same original workbook ZIP valid")
        paths=old.sheetpaths(original);need(len(paths)==26,"same 26 saved sheets")
        styles,sty=old.newstyles(original.read("xl/styles.xml"))
        register_rows=register_g2_7l(m)
        for i,r in enumerate(m["rows"],1):
            x=r.get("G2_7M_source_correspondence")
            if x:
                register_rows[i][9]+="; "+"; ".join(x["source_item_ids"])
                register_rows[i][10]+="; "+x["relation"]
                register_rows[i][11]="G2-7M J7/J8/J9 physical ports, RF source rules and held measurements; no observed service"
        summary=[
           ["SOSA-G2-7M consolidated J7/J8/J9 and auxiliary RF original C239","Ed1.1 §§13.5.2.8–13.5.2.12 PDF295–306; stop BEFORE J10"],
           ["Original source-native inventory","27 numbered SHALL Rules, 2 Observations, 1 separate table-preamble SHALL"],
           ["Native physical connectors","J7 multi-protocol; J8 19 channels; J9 8 channels; four application-specific auxiliary RF connectors"],
           ["Original native table row accounting","Six source tables, 102 individually recorded pin/performance rows"],
           ["RF VSWR limits","J8 1.25:1/1.30:1/1.40:1/1.60:1 by band; J9 1.40:1 to 22GHz"],
           ["Modeling discipline","Physical J7 write-enable switch not CSAPI Command; VSWR design limit not measured RF power"],
           ["Original-source holds","19 exact packet holds; external normative standards and 5 figure pixels unread"],
           ["Master source-qualified increment","21 existing The Open Group SOSA I-column cells, zero other column edits"],
           ["C239 heading coverage","173 sampled/inline-reviewed, 18 substantively unread, one restricted; parent still PARTIAL"],
           ["Exact same workbook","329 information rows; all 346x15 saved cells match JSON/2 CSV/2 MD; 22 original historic sheets unchanged"],
           ["SOSA and next","SOSA ACTIVE/OPEN, Step18 SAPIENT blocked; separate owner Proceed starts G2-7N §§13.5.2.13–13.5.2.19.2"]
        ]
        edits={"Master Crosswalk":m["review_grid"],"DIM Register":register_rows,"Summary":summary,"Validation":summary}
        changes={"xl/styles.xml":styles}
        for name,contents in edits.items():
            changes[paths[name]]=matrix_to_xml(contents,sty,main=name=="Master Crosswalk",sections=m["review_sections"] if name=="Master Crosswalk" else ())
        preserved={name:digest(original.read(path)) for name,path in paths.items() if name not in edits}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as wb:
            for item in original.infolist():
                wb.writestr(item,changes.get(item.filename,original.read(item.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as wb:
        need(wb.testzip() is None and list(old.sheetpaths(wb))==list(paths),"same 26-sheet saved workbook and ZIP CRC")
        for name,sha in preserved.items():
            need(digest(wb.read(paths[name]))==sha,"22 exact preserved history XML "+name)
        for path in wb.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(wb.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                need(not any(x.get("t")=="e" for x in ET.fromstring(wb.read(path)).iter(q("c"))),"no Excel error cells")
        main=ET.fromstring(wb.read(paths["Master Crosswalk"]))
        need([x.get("ref") for x in main.find(q("mergeCells")).findall(q("mergeCell"))]
             ==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "original topic headings and layout preserved")
    actual=old.readcells(saved,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for j,value in enumerate(row,1):
            need(actual.get(addr(i,j),"")==old.val(value),"saved Excel cell matches source "+addr(i,j))
    former=old.readcells(previous,"Master Crosswalk")
    delta=sorted(k for k in set(former)|set(actual) if former.get(k,"")!=actual.get(k,""))
    need(len(delta)==21 and all(re.fullmatch(r"I\d+",x) for x in delta),
         "21 SOSA donor column cells only, no other source/donor/ISA/target changed")
    prior_record=load("SOSA_G2_7L_Workbook_Validation_11NOV2026.json")
    need(preserved==prior_record["exact_original_untouched_xml_sha256"],"previous independently verified historical sheet hashes preserved")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7M_CONSOLIDATED_J7_J8_J9_SOURCE_AND_SAME_SAVED_EXCEL_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7M-CANONICAL-VERIFIED","sha256":sha,
        "currently_matches_readable_view":True,"lag":"NONE: all 346x15 saved cells match JSON, both CSV and both Markdown",
        "refreshed_cell_count":21,"validation_file":report_name})
    m["SOSAEvidence"]["G2_7M"]={"sourceLedger":ledger_name,"sourceReview":"SOSA_G2_7M_Original_Source_and_Master_Reconciliation_11NOV2026.md",
        "qualified_existing_row_matches":21,"original_numbered_shall_rules":27,
        "exact_holds":19,"original_external_normative_and_figure_holds":True,
        "Excel_lag_cells":0,"excel_checkpoint":"SOSA-G2-7M-CANONICAL-VERIFIED","excel_validation":report_name,
        "DIM_Profile_adopted":False}
    m["SOSAReviewCompletion"]["G2_7M_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="OPEN__G2_7M_CONSOLIDATED_SOURCE_AND_SAME_EXCEL_VERIFIED__EXTERNAL_ORIGINALS_HELD"
    next_step="Only distinct owner Proceed starts G2-7N original C239 §§13.5.2.13–13.5.2.19.2; STOP before §13.5.3"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]=next_step
    m["nextOwnerAction"]=next_step
    m["publicationPolicy"]="L23 G2-7M: 21 source-qualified SOSA-only I cells; one JSON, both CSV/MD and same 26-sheet Excel current; all saved cells verified"
    save(MASTER,m)
    record={"date":"2026-11-11","step":"SOSA-G2-7M-CONSOLIDATED-SAVED-EXCEL",
        "result":"ORIGINAL_C239_AND_SOURCE_MASTER_AND_SAME_26_SHEET_EXCEL_PARITY_PASS",
        "workbook_sha256":sha,"previous_workbook_sha256":base_sha,
        "workbook_sheets":list(paths),"refreshed_sheets":list(edits),
        "exact_original_untouched_xml_sha256":preserved,
        "information_rows":329,"grid_rows":346,"columns":15,
        "historical_donor_facts":58,"case_facts":73,"ISA_source_outcomes":480,"ISA_open_questions":6,
        "original_source_records":173,"source_numbered_RULE_SHALL":27,"source_OBSERVATION":2,
        "source_table_rows":102,"source_figure_captions":5,"source_holds":19,
        "qualified_existing_sosa_cells":21,"changed_saved_cells":delta,
        "C239_touched_headings":173,"C239_unread":18,"C239_restricted":1,
        "checks":{"all_saved_346x15_cells_match":True,"both_CSVs_equal":True,
          "both_markdown_tables_equal":True,"same_26_sheets":True,"22_historical_sheets_preserved":True,
          "only_SOSA_I_cells_changed":True,"saved_zip_xml_valid":True,"no_error_cells":True,
          "no_DIM_Profile_adoption":True},
        "limits":["Only §§13.5.2.8–13.5.2.12, not J10 or later",
                  "External native standards and five original figure pixels unexamined",
                  "No independently tested physical connection, RF signal, CSAPI Command, or real source-case conformance"],
        "next":next_step}
    save(report_name,record)
    print("PASS G2-7M one packet: 27 native SHALL / 2 Observations, 21 SOSA cells, all saved 346x15 Excel cells and 22 historical tabs; workbook SHA="+sha)
    return sha


def check_g2_7n_source(z,m=None):
    c=z["counts"]; items=z["original_source_items"]; ids={x["id"] for x in items}
    need(len(items)==len(ids)==142 and c["all_typed_source_records"]==142,
         "original G2-7N 142 classified source items")
    for kind,n in (("RULE",31),("RECOMMENDATION",4),("OBSERVATION",2),
                   ("NESTED_SOURCE_SECTION",15),("ORIGINAL_SOURCE_TABLE",6),
                   ("TABLE_PIN_OR_FIBER_ROW",53),("FIGURE_CAPTION",8)):
        need(sum(x["kind"]==kind for x in items)==n,"original typed source evidence "+kind)
    need(c["rule_with_explicit_shall"]==30 and c["rule_labeled_descriptive"]==1
         and c["source_qualified_master_mappings"]==24 and c["exact_holds"]==21,
         "source Rule modal evidence and exact mapping/hold count")
    dup=[x for x in items if x["kind"]=="RULE" and x["source_id"]=="13.5.2.13.1-1"]
    need(len(dup)==2 and {x["disambiguation"] for x in dup}=={"J10","J11"}
         and len({x["id"] for x in dup})==2,
         "distinct original J10/J11 duplicate printed Rule identifier")
    j13=next(x for x in items if x["kind"]=="RULE" and x["source_id"]=="13.5.2.16-5")
    need(j13["original_modal_standing"]=="PRINTED_RULE_DESCRIPTIVE_NO_EXPLICIT_SHALL",
         "J13 printed Rule descriptive, not invented SHALL")
    idsJ16={x["source_id"] for x in items if x["kind"]=="RULE" and x["source_id"].startswith("13.5.2.19")}
    need(idsJ16=={"13.5.2.19-1","13.5.2.19-2","13.5.2.19.1-1","13.5.2.19.2-1"},
         "separate V_BATT and ALT_V_BATT original Rule identities")
    need(z["source"]["original_figure_pixels_verified"] is False
         and z["source"]["external_originals_read"] is False
         and z["source"]["native_eight_original_companions_read"] is False
         and z["DIM_Profile_adopted"] is False
         and z["independent_hardware_conformance"] is False,
         "unreviewed image/normative originals and no model or equipment adoption")
    co=z["c239_heading_status"]
    need((co["registered"],co["at_least_sampled_or_inline_read"],co["unread"],co["restricted"],co["new_registered_credits"])
         ==(192,173,18,1,0),"no false TOC-heading source coverage")
    needs=[x for x in z["qualified_existing_row_mappings"] if not x["source_item_ids"]
           or any(v not in ids for v in x["source_item_ids"])]
    need(not needs,"each mapping has independently listed original source ID")
    if m:
        selected=[r for r in m["rows"] if r.get("G2_7N_source_correspondence")]
        need(len(selected)==24 and {r["row_id"] for r in selected}
             ==set(m["workbookSnapshot"]["G2_7N_affected_row_ids"]),
             "24 existing approved master rows, no reordering or new classes")
        for r in selected:
            ev=r["G2_7N_source_correspondence"]
            need(r["display"][8].startswith(ev["previous_sosa_cell_value"])
                 and "G2-7N:" in r["display"][8]
                 and all(v in ids for v in ev["source_item_ids"])
                 and ev["DIM_Profile_adopted"] is False,
                 "original source row preserved and semantically attributed "+r["row_id"])

def publish_g2_7n():
    from html import escape,unescape
    itemname="SOSA_G2_7N_Original_Source_Item_Coverage_11NOV2026.json"
    reportname="SOSA_G2_7N_Workbook_Validation_11NOV2026.json"
    base_sha="d4110ad4322e748bb602e0355923baa40ed824bfe33d56ad4892addeee7510db"
    m=load(MASTER); z=load(itemname); legacy=load(LEDGER)
    check_source(m,legacy); check_g2_7m_source(load("SOSA_G2_7M_Original_Source_Item_Coverage_11NOV2026.json"),m)
    check_g2_7n_source(z)
    prior=(D/BOOK).read_bytes()
    need(digest(prior)==base_sha==m["currentWorkbookSha256"]
         and m["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7M-CANONICAL-VERIFIED"
         and m["workbookSnapshot"]["currently_matches_readable_view"],
         "current G2-7M SAME Excel is expected original input")
    mapped={}
    for qmap in z["qualified_existing_row_mappings"]:
        matched=[r for r in m["rows"] if r["label"]==qmap["label"]]
        need(len(matched)==1 and qmap["label"] not in mapped,"existing unique crosswalk row")
        r=matched[0];prev=r["display"][8]
        need("G2-7N:" not in prev,"not already integrated")
        new=(prev+" · G2-7N: "+qmap["source_native_meaning"]+" ["+qmap["relation"]+
            "; "+qmap["negative_equivalence_boundary"]+"]")
        need(len(new)<=32767,"Excel text cell maximum")
        r["display"][8]=new
        r["G2_7N_source_correspondence"]={
           "source_item_ids":qmap["source_item_ids"],"relation":qmap["relation"],
           "source_native_meaning":qmap["source_native_meaning"],
           "negative_equivalence_boundary":qmap["negative_equivalence_boundary"],
           "previous_sosa_cell_value":prev,"DIM_Profile_adopted":False,
           "original_external_and_image_companions_held":True}
        mapped[qmap["label"]]=new
    need(len(mapped)==24,"exactly 24 justified existing source comparisons")
    positions=[i for i in range(2,len(m["review_grid"])) if i not in set(m["review_sections"])]
    need(len(positions)==len(m["rows"])==329,"original 329 source case/donor/proposed DIM rows")
    for i,r in zip(positions,m["rows"]):
        need(m["review_grid"][i][14]==r["label"],"original row placement untouched")
        m["review_grid"][i][8]=r["display"][8]
    m["workbookSnapshot"]["G2_7N_affected_row_ids"]=[
        r["row_id"] for r in m["rows"] if r.get("G2_7N_source_correspondence")]
    check_g2_7n_source(z,m)
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/n).open("w",encoding="utf-8",newline="") as f:
            csv.writer(f,lineterminator="\r\n").writerows(m["review_grid"])
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        original=(D/n).read_text(encoding="utf-8")
        def append_only(match):
            tr=match.group(0);cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            name=unescape(cells[14].group(1))
            if name not in mapped:return tr
            target=cells[8]
            return tr[:target.start(1)]+escape(mapped[name],quote=True)+tr[target.end(1):]
        updated=re.sub(r"<tr>.*?</tr>",append_only,original,flags=re.S)
        need(updated!=original and updated.count("G2-7N:")>=24,
             "substantive new source mapping in readable comparison "+n)
        (D/n).write_text(updated,encoding="utf-8")
    check_source(m,legacy)
    with zipfile.ZipFile(io.BytesIO(prior)) as oldwb:
        need(oldwb.testzip() is None,"source workbook has good ZIP/CRC")
        paths=old.sheetpaths(oldwb)
        need(len(paths)==26,"same original 26 worksheet names")
        styles,sty=old.newstyles(oldwb.read("xl/styles.xml"))
        register_rows=register_g2_7l(m)
        for k,r in enumerate(m["rows"],1):
            for packet in ("G2_7M","G2_7N"):
                ev=r.get(packet+"_source_correspondence")
                if not ev:continue
                register_rows[k][9]+="; "+"; ".join(ev["source_item_ids"])
                register_rows[k][10]+="; "+ev["relation"]
                register_rows[k][11]=packet+" original source-qualified hardware: no actual installed power/security/optical service"
        summary=[
           ["SOSA-G2-7N complete original C239 J10-J16","Edition1.1 §§13.5.2.13–13.5.2.19.2, PDF306–316; STOP before Class3"],
           ["Original native source ledger","31 Rule appearances (30 explicit SHALL/1 descriptive), 4 SHOULD, 2 Observations"],
           ["Original tables and figure evidence","6 source tables/53 pin and fiber rows, 8 captions; figure pixels held"],
           ["Source nuance","J11 duplicate Rule label under J10; J14/J15 disputed reference IDs; J13 descriptive Rule"],
           ["J10/J11 power distinction","115/200V RMS Y 400Hz AC and separate 270VDC with physical inrush/safety design"],
           ["J12/J13 physical key fill","TIA485-A differential non-GPS versus TIA232 GPS; not software CSAPI Command"],
           ["J14/J15 optical grouping","24 MT physical positions; J14 >24 fiber SHOULD, J15 <=24 fiber Observation"],
           ["J16 battery-designated input","Platform-supplied V_BATT/ALT_V_BATT hold-up, not source-reported battery reserve"],
           ["New donor-qualified crosswalk comparisons","24 existing SOSA column-I cells, no new case, other donor, DIM fields"],
           ["Original C239 progress","173 at least sampled/inline of 192 registered headings; 18 unread, 1 restricted"],
           ["Preservation","Original four cases, 329 information rows, 58 donor records, 73 cases, ISA 480/six questions"],
           ["One canonical workbook","Same 26-sheet editable Excel, all 346x15 saved cells match JSON/2CSV/2MD, 22 historic sheets unchanged"],
           ["Source holds/decisions","21 precise holds, no adopted DIM classes or CSAPI Profile SHALL, no real hardware conformance"],
           ["Only next owner Proceed","SOSA-G2-7O original Class3 §§13.5.3–13.5.3.3.11, STOP before §13.5.3.4"]]
        replacements={"Master Crosswalk":m["review_grid"],"DIM Register":register_rows,"Summary":summary,"Validation":summary}
        edits={"xl/styles.xml":styles}
        for name,matrix in replacements.items():
            edits[paths[name]]=matrix_to_xml(matrix,sty,main=name=="Master Crosswalk",
                sections=m["review_sections"] if name=="Master Crosswalk" else ())
        preserved={name:digest(oldwb.read(path)) for name,path in paths.items() if name not in replacements}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as wb:
            for info in oldwb.infolist():wb.writestr(info,edits.get(info.filename,oldwb.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as book:
        need(book.testzip() is None and list(old.sheetpaths(book))==list(paths),"same 26 sheets and ZIP valid")
        for name,sha in preserved.items():
            need(digest(book.read(paths[name]))==sha,"previous 22 historic sheets unmodified "+name)
        for p in book.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(book.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(x.get("t")=="e" for x in ET.fromstring(book.read(p)).iter(q("c"))),
                     "no Excel error cells")
        master=ET.fromstring(book.read(paths["Master Crosswalk"]))
        need([x.get("ref") for x in master.find(q("mergeCells")).findall(q("mergeCell"))]
             ==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "original grouped source-case, OGC and DIM layout")
    savedrows=old.readcells(saved,"Master Crosswalk")
    for i,r in enumerate(m["review_grid"],1):
        for j,val in enumerate(r,1):
            need(savedrows.get(addr(i,j),"")==old.val(val),"saved original Excel cell "+addr(i,j))
    previous=old.readcells(prior,"Master Crosswalk")
    changed=sorted(k for k in set(previous)|set(savedrows)
                   if previous.get(k,"")!=savedrows.get(k,""))
    need(len(changed)==24 and all(re.fullmatch(r"I\d+",k) for k in changed),
         "exactly 24 SOSA I-column source cells, no other-donor/case/DIM changes")
    earlier=load("SOSA_G2_7M_Workbook_Validation_11NOV2026.json")
    need(preserved==earlier["exact_original_untouched_xml_sha256"],
         "historical original 22 worksheets unchanged since verified G2-7M")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7N_ORIGINAL_J10_J16_SOURCE_AND_SAME_EDITABLE_26_SHEET_EXCEL_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7N-CANONICAL-VERIFIED","sha256":sha,
       "currently_matches_readable_view":True,
       "lag":"NONE: 346x15 saved XLSX source values match one JSON/both CSV/both MD",
       "refreshed_cell_count":24,"validation_file":reportname})
    m["SOSAEvidence"]["G2_7N"]={"sourceLedger":itemname,
       "sourceReview":"SOSA_G2_7N_Original_Source_and_Master_Reconciliation_11NOV2026.md",
       "qualified_existing_row_matches":24,"original_rule_appearances":31,
       "explicit_SHALL":30,"exact_holds":21,
       "Excel_lag_cells":0,"excel_checkpoint":"SOSA-G2-7N-CANONICAL-VERIFIED",
       "excel_validation":reportname,"DIM_Profile_adopted":False}
    m["SOSAReviewCompletion"]["G2_7N_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="ACTIVE_OPEN__G2_7N_SOURCE_SAME_SAVED_XLSX_VERIFIED__EXTERNALS_HELD"
    nextstep="Only next owner Proceed starts G2-7O original §§13.5.3–13.5.3.3.11, STOP before §13.5.3.4"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]=nextstep
    m["nextOwnerAction"]=nextstep
    m["publicationPolicy"]="L23 G2-7N one canonical source: 24 SOSA cells, both CSV/MD and SAME 26-sheet Excel, all saved cells and 22 historic worksheets verified"
    save(MASTER,m)
    record={"date":"2026-11-11","step":"SOSA-G2-7N-CONSOLIDATED-SAVED-EXCEL",
      "result":"ORIGINAL_SOURCE_AND_SAME_26_SHEET_EXCEL_PARITY_PASS",
      "workbook_sha256":sha,"previous_workbook_sha256":base_sha,
      "workbook_sheets":list(paths),"refreshed_sheets":list(replacements),
      "exact_original_untouched_xml_sha256":preserved,
      "information_rows":329,"grid_rows":346,"columns":15,
      "historical_donor_facts":58,"case_facts":73,"ISA_source_outcomes":480,"ISA_open_questions":6,
      "source_typed_records":142,"source_rule_appearances":31,
      "source_explicit_SHALL":30,"source_Recommendations":4,"source_Observations":2,
      "source_tables":6,"pin_or_fiber_rows":53,"source_figure_captions":8,"source_holds":21,
      "qualified_existing_sosa_cells":24,"changed_saved_cells":changed,
      "C239_touched_headings":173,"C239_unread":18,"C239_restricted":1,
      "checks":{"all_saved_346x15_cells_match":True,"both_CSVs_equal":True,
         "both_markdown_tables_equal":True,"same_26_sheets":True,
         "22_historical_sheets_preserved":True,"only_SOSA_I_cells_changed":True,
         "saved_zip_xml_valid":True,"no_error_cells":True,"no_DIM_Profile_adoption":True},
      "limits":["Only original C239 §§13.5.2.13–13.5.2.19.2; Class3 unstarted",
          "Figure pixels and 14 native/external source pointers held",
          "No physical source-case power/command/optical conformance or source data invented"],
      "next":nextstep}
    save(reportname,record)
    print("PASS G2-7N: 31 printed Rule items/30 explicit SHALL, 4 SHOULD, 2 Observations, 24 SOSA cells; 346x15 saved Excel and 22 historic sheets; SHA "+sha)
    return sha


def check_g2_7o_source(z,m=None):
    c=z["counts"]; items=z["original_source_items"]; ids={x["id"] for x in items}
    need(len(items)==len(ids)==202==c["all_typed_source_records"],
         "G2-7O 202 typed original source/analysis records")
    need(c["numbered_SHALL_Rules"]==47 and c["numbered_Observations"]==9
         and c["numbered_Permissions"]==5 and c["numbered_Recommendations"]==0,
         "47 native SHALL, 9 Observations, 5 Permissions, none falsely converted")
    need((c["method_Inspection"],c["method_Analysis"],c["method_Test"],
          c["method_Analysis_Test"])==(39,4,3,1),
         "exact printed original Rule methods separate from normative standing")
    for name,num in (("RULE",47),("OBSERVATION",9),("PERMISSION",5),
                     ("SOURCE_SECTION",20),("SOURCE_TABLE",3),("TABLE_ROW",88),
                     ("FIGURE_CAPTION",2),("UNNUMBERED_SHALL",1)):
        need(sum(x["kind"]==name for x in items)==num,"native source-item type "+name)
    actual={x["pin_label"] for x in items
            if x["kind"]=="TABLE_ROW" and x["source_table"]=="13.5.3.3-1"}
    need(actual=={str(i) for i in range(1,67)}-{"18","26"},
         "64 distinct original J2 source pin numbers, no invented pins")
    need({x["id"] for x in items if x["kind"]=="OBSERVATION"
          and x["printed_item_id"]=="13.5.3.3-1"}==
         {"SOSA-C239-G2-7O-OBSERVATION-13_5_3_3_1-P321",
          "SOSA-C239-G2-7O-OBSERVATION-13_5_3_3_1-P326"},
         "two printed identically numbered Observations retain separate source IDs")
    need(len(z["qualified_existing_row_mappings"])==24 and len(z["exact_holds"])==22
         and all(x["source_item_ids"] and
                 all(k in ids for k in x["source_item_ids"])
                 for x in z["qualified_existing_row_mappings"]),
         "exact 24 qualified existing rows/22 original source holds")
    cov=z["original_c239_registered_heading_status"]
    need((cov["registered"],cov["at_least_sampled_or_inline_read"],
          cov["substantively_unread"],cov["restricted"])==(192,174,17,1)
         and cov["new_original_registered_heading"]=="13.5.3",
         "new original Class3 registered heading source-reviewed; source still PARTIAL")
    need(z["source"]["figure_pixels_verified"] is False
         and z["source"]["external_originals_examined"] is False
         and z["source"]["native_eight_companions_read"] is False
         and z["DIM_Profile_adopted"] is False
         and z["independent_conformance"] is False,
         "no external original figure or native schema/device conformance falsely claimed")
    if m is not None:
        mapped=[r for r in m["rows"] if r.get("G2_7O_source_correspondence")]
        need(len(mapped)==24 and {r["row_id"] for r in mapped}
             ==set(m["workbookSnapshot"]["G2_7O_affected_row_ids"]),
             "24 unique existing owner-approved master rows")
        for row in mapped:
            ev=row["G2_7O_source_correspondence"]
            need(row["display"][8].startswith(ev["previous_sosa_cell_value"])
                 and "G2-7O:" in row["display"][8]
                 and all(k in ids for k in ev["source_item_ids"])
                 and ev["DIM_Profile_adopted"] is False,
                 "append-only source-qualified donor cell with no model approval "+row["row_id"])

def publish_g2_7o():
    from html import escape,unescape
    itemname="SOSA_G2_7O_Original_Source_Item_Coverage_11NOV2026.json"
    reportname="SOSA_G2_7O_Workbook_Validation_11NOV2026.json"
    base_sha="2c5d440b4361413b119f390e8bdd74483e65c98bfa084a049581531b1bb5531a"
    m=load(MASTER); z=load(itemname); legacy=load(LEDGER)
    check_source(m,legacy); check_g2_7n_source(load("SOSA_G2_7N_Original_Source_Item_Coverage_11NOV2026.json"),m)
    check_g2_7o_source(z)
    prior=(D/BOOK).read_bytes()
    need(digest(prior)==base_sha==m["currentWorkbookSha256"]
         and m["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7N-CANONICAL-VERIFIED"
         and m["workbookSnapshot"]["currently_matches_readable_view"],
         "current G2-7M SAME Excel is expected original input")
    mapped={}
    for qmap in z["qualified_existing_row_mappings"]:
        matched=[r for r in m["rows"] if r["label"]==qmap["label"]]
        need(len(matched)==1 and qmap["label"] not in mapped,"existing unique crosswalk row")
        r=matched[0];prev=r["display"][8]
        need("G2-7O:" not in prev,"not already integrated")
        new=(prev+" · G2-7O: "+qmap["native_source_meaning"]+" ["+qmap["relation"]+
            "; "+qmap["negative_equivalence_boundary"]+"]")
        need(len(new)<=32767,"Excel text cell maximum")
        r["display"][8]=new
        r["G2_7O_source_correspondence"]={
           "source_item_ids":qmap["source_item_ids"],"relation":qmap["relation"],
           "source_native_meaning":qmap["native_source_meaning"],
           "negative_equivalence_boundary":qmap["negative_equivalence_boundary"],
           "previous_sosa_cell_value":prev,"DIM_Profile_adopted":False,
           "original_external_and_image_companions_held":True}
        mapped[qmap["label"]]=new
    need(len(mapped)==24,"exactly 24 justified existing source comparisons")
    positions=[i for i in range(2,len(m["review_grid"])) if i not in set(m["review_sections"])]
    need(len(positions)==len(m["rows"])==329,"original 329 source case/donor/proposed DIM rows")
    for i,r in zip(positions,m["rows"]):
        need(m["review_grid"][i][14]==r["label"],"original row placement untouched")
        m["review_grid"][i][8]=r["display"][8]
    m["workbookSnapshot"]["G2_7O_affected_row_ids"]=[
        r["row_id"] for r in m["rows"] if r.get("G2_7O_source_correspondence")]
    check_g2_7o_source(z,m)
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/n).open("w",encoding="utf-8",newline="") as f:
            csv.writer(f,lineterminator="\r\n").writerows(m["review_grid"])
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        original=(D/n).read_text(encoding="utf-8")
        def append_only(match):
            tr=match.group(0);cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            name=unescape(cells[14].group(1))
            if name not in mapped:return tr
            target=cells[8]
            return tr[:target.start(1)]+escape(mapped[name],quote=True)+tr[target.end(1):]
        updated=re.sub(r"<tr>.*?</tr>",append_only,original,flags=re.S)
        need(updated!=original and updated.count("G2-7O:")>=24,
             "substantive new source mapping in readable comparison "+n)
        (D/n).write_text(updated,encoding="utf-8")
    check_source(m,legacy)
    with zipfile.ZipFile(io.BytesIO(prior)) as oldwb:
        need(oldwb.testzip() is None,"source workbook has good ZIP/CRC")
        paths=old.sheetpaths(oldwb)
        need(len(paths)==26,"same original 26 worksheet names")
        styles,sty=old.newstyles(oldwb.read("xl/styles.xml"))
        register_rows=register_g2_7l(m)
        for k,r in enumerate(m["rows"],1):
            for packet in ("G2_7M","G2_7N","G2_7O"):
                ev=r.get(packet+"_source_correspondence")
                if not ev:continue
                register_rows[k][9]+="; "+"; ".join(ev["source_item_ids"])
                register_rows[k][10]+="; "+ev["relation"]
                register_rows[k][11]=packet+" original source-qualified hardware: no actual installed power/security/optical service"
        summary=[
          ["SOSA-G2-7O original Class3 J1/J2","C239 Ed1.1 §§13.5.3–13.5.3.3.11 PDF317–329; STOP before J3"],
          ["Original normative inventory","47 numbered SHALL Rules, nine Observations, five Permissions, one separate NEZ narrative SHALL"],
          ["Native source tables","Three source tables, 88 rows (13 connector families/11 J1/64 J2); two unverified figures"],
          ["Source connector discrepancies","Class3 J2 N versus A keying, source J10 catalog omission and mission permission"],
          ["Original conflicting J2 pin rules","MASTER_ARM 2/95 vs 2/5; NEZ 4/5/11/12 vs 11/12/13/52; modes 89/90/97/98 vs 53/54/59/65"],
          ["Class3 J1 input power","Five 28VDC 10A pairs, 14A/2s inrush, ≥1MOhm isolation and ≤0.1Ohm grounding"],
          ["Class3 source nuance","Two Observation13.5.3.3-1 items and Class1&2 references under Class3 J2"],
          ["Earned heading coverage","174 at least sampled/inline-read,17 unread,1 restricted; Class3 original §13.5.3 newly read"],
          ["Current qualified SOSA increment","24 existing donor column-I cells; all prior donor/case/DIM cells unchanged"],
          ["Same original editable Excel","Original 26 sheets, all 346x15 actual cells match current JSON/both CSV/both MD,22 historic unchanged"],
          ["Original holds and adoption","22 precise holds, no adopted DIM classes/CSAPI Profile SHALL or real hardware conformance"],
          ["Only distinct owner Proceed next","G2-7P C239 §§13.5.3.4–13.5.3.17.2, STOP before Class5 §13.5.4"]]
        replacements={"Master Crosswalk":m["review_grid"],"DIM Register":register_rows,"Summary":summary,"Validation":summary}
        edits={"xl/styles.xml":styles}
        for name,matrix in replacements.items():
            edits[paths[name]]=matrix_to_xml(matrix,sty,main=name=="Master Crosswalk",
                sections=m["review_sections"] if name=="Master Crosswalk" else ())
        preserved={name:digest(oldwb.read(path)) for name,path in paths.items() if name not in replacements}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as wb:
            for info in oldwb.infolist():wb.writestr(info,edits.get(info.filename,oldwb.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as book:
        need(book.testzip() is None and list(old.sheetpaths(book))==list(paths),"same 26 sheets and ZIP valid")
        for name,sha in preserved.items():
            need(digest(book.read(paths[name]))==sha,"previous 22 historic sheets unmodified "+name)
        for p in book.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(book.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(x.get("t")=="e" for x in ET.fromstring(book.read(p)).iter(q("c"))),
                     "no Excel error cells")
        master=ET.fromstring(book.read(paths["Master Crosswalk"]))
        need([x.get("ref") for x in master.find(q("mergeCells")).findall(q("mergeCell"))]
             ==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "original grouped source-case, OGC and DIM layout")
    savedrows=old.readcells(saved,"Master Crosswalk")
    for i,r in enumerate(m["review_grid"],1):
        for j,val in enumerate(r,1):
            need(savedrows.get(addr(i,j),"")==old.val(val),"saved original Excel cell "+addr(i,j))
    previous=old.readcells(prior,"Master Crosswalk")
    changed=sorted(k for k in set(previous)|set(savedrows)
                   if previous.get(k,"")!=savedrows.get(k,""))
    need(len(changed)==24 and all(re.fullmatch(r"I\d+",k) for k in changed),
         "exactly 24 SOSA I-column source cells, no other-donor/case/DIM changes")
    earlier=load("SOSA_G2_7N_Workbook_Validation_11NOV2026.json")
    need(preserved==earlier["exact_original_untouched_xml_sha256"],
         "historical original 22 worksheets unchanged since verified G2-7M")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7O_ORIGINAL_CLASS3_J1_J2_AND_SAME_EDITABLE_26_SHEET_EXCEL_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7O-CANONICAL-VERIFIED","sha256":sha,
       "currently_matches_readable_view":True,
       "lag":"NONE: 346x15 saved XLSX source values match one JSON/both CSV/both MD",
       "refreshed_cell_count":24,"validation_file":reportname})
    m["SOSAEvidence"]["G2_7O"]={"sourceLedger":itemname,
       "sourceReview":"SOSA_G2_7O_Original_Source_and_Master_Reconciliation_11NOV2026.md",
       "qualified_existing_row_matches":24,"original_rule_appearances":47,
       "explicit_SHALL":47,"exact_holds":22,
       "Excel_lag_cells":0,"excel_checkpoint":"SOSA-G2-7O-CANONICAL-VERIFIED",
       "excel_validation":reportname,"DIM_Profile_adopted":False}
    m["SOSAReviewCompletion"]["G2_7O_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="OPEN__G2_7O_ORIGINAL_CLASS3_SAME_SAVED_XLSX_VERIFIED__17_UNREAD_1_RESTRICTED"
    nextstep="Only distinct owner Proceed starts G2-7P original §§13.5.3.4–13.5.3.17.2, STOP before §13.5.4 Class5"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]=nextstep
    m["nextOwnerAction"]=nextstep
    m["publicationPolicy"]="L23 G2-7O one canonical source: 24 SOSA cells, both CSV/MD and SAME 26-sheet Excel, all saved cells and 22 historic worksheets verified"
    save(MASTER,m)
    record={"date":"2026-11-11","step":"SOSA-G2-7O-CONSOLIDATED-SAVED-EXCEL",
      "result":"ORIGINAL_SOURCE_AND_SAME_26_SHEET_EXCEL_PARITY_PASS",
      "workbook_sha256":sha,"previous_workbook_sha256":base_sha,
      "workbook_sheets":list(paths),"refreshed_sheets":list(replacements),
      "exact_original_untouched_xml_sha256":preserved,
      "information_rows":329,"grid_rows":346,"columns":15,
      "historical_donor_facts":58,"case_facts":73,"ISA_source_outcomes":480,"ISA_open_questions":6,
      "source_typed_records":202,"source_rule_appearances":47,
      "source_explicit_SHALL":47,"source_Recommendations":0,"source_Observations":9,"source_Permissions":5,
      "source_tables":3,"pin_or_fiber_rows":88,"source_figure_captions":2,"source_holds":22,
      "qualified_existing_sosa_cells":24,"changed_saved_cells":changed,
      "C239_touched_headings":174,"C239_unread":17,"C239_restricted":1,
      "checks":{"all_saved_346x15_cells_match":True,"both_CSVs_equal":True,
         "both_markdown_tables_equal":True,"same_26_sheets":True,
         "22_historical_sheets_preserved":True,"only_SOSA_I_cells_changed":True,
         "saved_zip_xml_valid":True,"no_error_cells":True,"no_DIM_Profile_adoption":True},
      "limits":["Only original Class3 §§13.5.3–13.5.3.3.11; STOP before J3",
          "Table/normative pin and keying conflicts held, figure pixels/external original standards unexamined",
          "No actual device or CSAPI software control conformance performed"],
      "next":nextstep}
    save(reportname,record)
    print("PASS G2-7O original 47 SHALL, 9 Observations, 5 Permissions, 24 SOSA cells, all actual 346x15 saved Excel and 22 historic sheets; SHA "+sha)
    return sha


def check_g2_7p_source(z,m=None):
    c=z["counts"];items=z["original_source_items"];ids={x["id"] for x in items}
    need(len(items)==len(ids)==300 and c["typed_source_records"]==300,
         "G2-7P 300 unique classified source/native evidence records")
    need(c["source_numbered_rules"]==74 and c["source_explicit_shall"]==73
         and c["source_Rule_labeled_descriptive"]==1
         and c["source_recommendations"]==4 and c["source_observations"]==5,
         "74 original Rule appearances (73 explicit SHALL/1 descriptive) and 4 SHOULD/5 observations")
    for kind,total in (("RULE",74),("RECOMMENDATION",4),("OBSERVATION",5),
                       ("SOURCE_SECTION",31),("SOURCE_TABLE",14),
                       ("SOURCE_TABLE_PIN_OR_BAND_ROW",135),
                       ("ORIGINAL_FIGURE_CAPTION",14),("UNNUMBERED_SHALL",1)):
        need(sum(i["kind"]==kind for i in items)==total,
             "original source-specific typed item count "+kind)
    J7={x["pin_or_frequency_band"] for x in items if x["kind"]=="SOURCE_TABLE_PIN_OR_BAND_ROW"
        and x["connector_family"]=="J7"}
    need(len(J7)==66 and len([x for x in items if x.get("connector_family")=="J8"
             and x["kind"]=="SOURCE_TABLE_PIN_OR_BAND_ROW"])==11
         and len([x for x in items if x.get("connector_family")=="J9"
             and x["kind"]=="SOURCE_TABLE_PIN_OR_BAND_ROW"])==4,
         "66 native Class3 J7 contacts, 11 J8 RF and 4 J9 RF contacts")
    need(len(z["source_qualified_existing_row_mappings"])==28
         and len(z["exact_holds"])==30,
         "28 source-qualified existing-row findings and 30 precise source holds")
    must=["J4","J9_CONFLICT","J11_CONFLICT","J14"]
    contexts=[x["id"].split("CONTEXT-")[-1] for x in items if x["kind"]=="SOURCE_ANALYSIS_NOT_RULE"]
    need(all(k in contexts for k in must),"original Class3 contradictions and Rule standing retained")
    need(any(x["kind"]=="UNNUMBERED_SHALL" for x in items)
         and next(x for x in items if x["printed_rule_id"]=="13.5.3.14-5")["standing"]==
             "RULE_LABELED_DESCRIPTIVE_NO_EXPLICIT_SHALL",
         "unnumbered J7 source SHALL separate; J13 printed Rule not silently promoted to mandatory")
    need(z["source_header_standing"]=={
       "registered":192,"at_least_sampled_or_inline_read":174,
       "unread":17,"restricted":1,"new_heading_credit":0},
       "nested original source sections do not inflate C239 registered-heading coverage")
    need(z["source"]["figure_pixels_verified"] is False
         and z["source"]["external_normative_originals_read"] is False
         and z["source"]["eight_C239_native_companions_read"] is False
         and z["DIM_Profile_adopted"] is False
         and z["independent_hardware_conformance"] is False,
         "unexamined native originals, image fidelity and no actual model/runtime conformance")
    need(all(x["source_item_ids"] and all(key in ids for key in x["source_item_ids"])
             and x["DIM_Profile_adopted"] is False
             for x in z["source_qualified_existing_row_mappings"]),
         "every master correspondence cited to actual distinct native original source Rule/Recommendation IDs")
    if m:
        mapped=[r for r in m["rows"] if r.get("G2_7P_source_correspondence")]
        need(len(mapped)==28 and {r["row_id"] for r in mapped}
             ==set(m["workbookSnapshot"]["G2_7P_affected_row_ids"]),
             "28 existing source-qualified donor cells and no new class/row")
        for r in mapped:
            e=r["G2_7P_source_correspondence"]
            need(r["display"][8].startswith(e["previous_sosa_cell_value"])
                 and "G2-7P:" in r["display"][8]
                 and e["source_item_ids"] and all(v in ids for v in e["source_item_ids"])
                 and e["DIM_Profile_adopted"] is False,
                 "earlier donor contributions intact and 28 original source ID references "+r["row_id"])

def publish_g2_7p():
    from html import escape,unescape
    itemname="SOSA_G2_7P_Original_Source_Item_Coverage_11NOV2026.json"
    reportname="SOSA_G2_7P_Workbook_Validation_11NOV2026.json"
    base_sha="d9dbc984e120019591a52b6cabfa293a522954a27cbac6db0c22735dce84fe4a"
    m=load(MASTER); z=load(itemname); legacy=load(LEDGER)
    check_source(m,legacy); check_g2_7o_source(load("SOSA_G2_7O_Original_Source_Item_Coverage_11NOV2026.json"),m)
    check_g2_7p_source(z)
    prior=(D/BOOK).read_bytes()
    need(digest(prior)==base_sha==m["currentWorkbookSha256"]
         and m["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7O-CANONICAL-VERIFIED"
         and m["workbookSnapshot"]["currently_matches_readable_view"],
         "current G2-7M SAME Excel is expected original input")
    mapped={}
    for qmap in z["source_qualified_existing_row_mappings"]:
        matched=[r for r in m["rows"] if r["label"]==qmap["label"]]
        need(len(matched)==1 and qmap["label"] not in mapped,"existing unique crosswalk row")
        r=matched[0];prev=r["display"][8]
        need("G2-7P:" not in prev,"not already integrated")
        new=(prev+" · G2-7P: "+qmap["native_source_meaning"]+" ["+qmap["relation"]+
            "; "+qmap["negative_equivalence_boundary"]+"]")
        need(len(new)<=32767,"Excel text cell maximum")
        r["display"][8]=new
        r["G2_7P_source_correspondence"]={
           "source_item_ids":qmap["source_item_ids"],"relation":qmap["relation"],
           "source_native_meaning":qmap["native_source_meaning"],
           "negative_equivalence_boundary":qmap["negative_equivalence_boundary"],
           "previous_sosa_cell_value":prev,"DIM_Profile_adopted":False,
           "original_external_and_image_companions_held":True}
        mapped[qmap["label"]]=new
    need(len(mapped)==28,"exactly 28 source-qualified existing source comparisons")
    positions=[i for i in range(2,len(m["review_grid"])) if i not in set(m["review_sections"])]
    need(len(positions)==len(m["rows"])==329,"original 329 source case/donor/proposed DIM rows")
    for i,r in zip(positions,m["rows"]):
        need(m["review_grid"][i][14]==r["label"],"original row placement untouched")
        m["review_grid"][i][8]=r["display"][8]
    m["workbookSnapshot"]["G2_7P_affected_row_ids"]=[
        r["row_id"] for r in m["rows"] if r.get("G2_7P_source_correspondence")]
    check_g2_7p_source(z,m)
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/n).open("w",encoding="utf-8",newline="") as f:
            csv.writer(f,lineterminator="\r\n").writerows(m["review_grid"])
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        original=(D/n).read_text(encoding="utf-8")
        def append_only(match):
            tr=match.group(0);cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            name=unescape(cells[14].group(1))
            if name not in mapped:return tr
            target=cells[8]
            return tr[:target.start(1)]+escape(mapped[name],quote=True)+tr[target.end(1):]
        updated=re.sub(r"<tr>.*?</tr>",append_only,original,flags=re.S)
        need(updated!=original and updated.count("G2-7P:")>=24,
             "substantive new source mapping in readable comparison "+n)
        (D/n).write_text(updated,encoding="utf-8")
    check_source(m,legacy)
    with zipfile.ZipFile(io.BytesIO(prior)) as oldwb:
        need(oldwb.testzip() is None,"source workbook has good ZIP/CRC")
        paths=old.sheetpaths(oldwb)
        need(len(paths)==26,"same original 26 worksheet names")
        styles,sty=old.newstyles(oldwb.read("xl/styles.xml"))
        register_rows=register_g2_7l(m)
        for k,r in enumerate(m["rows"],1):
            for packet in ("G2_7M","G2_7N","G2_7O","G2_7P"):
                ev=r.get(packet+"_source_correspondence")
                if not ev:continue
                register_rows[k][9]+="; "+"; ".join(ev["source_item_ids"])
                register_rows[k][10]+="; "+ev["relation"]
                register_rows[k][11]=packet+" original source-qualified hardware: no actual installed power/security/optical service"
        summary=[
         ["SOSA-G2-7P original Class3 J3-J16 source","C239 Ed1.1 §§13.5.3.4–13.5.3.17.2 PDF329–351; stop BEFORE Class5 §13.5.4"],
         ["Native original evidence","74 numbered Rule appearances (73 explicit SHALL/1 descriptive), 4 SHOULD, 5 Observations"],
         ["Original source table fidelity","14 table texts, 135 pin/frequency rows, 14 figure captions; figure pixels held"],
         ["Class3 J3 and J4 meaning","Four digital/two composite video; 2 optical TX/RX pairs and OM2-or-better vs earlier OM3"],
         ["Source J4 inconsistency","J4 Rule13.5.3.5-1 says insert13-3, native J4 source table says13-4"],
         ["Class3 physical RF","J8 has11 RF contacts vs earlier19; J9 has4 vs earlier8; VSWR is design criterion"],
         ["Source J9 inconsistency","J9 Rule13.5.3.10-2 says25-8, native table says21-75"],
         ["Class3 DC voltage ratings","J6 14A/2s,10A nominal; J11 270V5A nominal and7.5A/2s inrush; earlier classes differ"],
         ["Original J11 pointer inconsistency","Rule13.5.3.12.1-1 cites later Class5 Table13.5.4.3-1 rather than Class3 table"],
         ["Security and optical distinctions","J12/J13 native keyfill role; J14 two MT and J15 one MT; original crossreference holds"],
         ["Real battery/runtime limits","J16 platform hold-up inputs are not measured stored energy/charge or safe software Commands"],
         ["Original C239 coverage","174 at least sampled/inline-read of192, 17 unread, 1 restricted; nested source sections only"],
         ["Source-qualified master update","28 existing SOSA donor-I cells; all prior empirical cases/other donors and DIM preserved"],
         ["Original editable Excel parity","SAME original 26 sheets, all 346x15 saved cells equal JSON/two CSV/two MD; 22 historical tabs unchanged"],
         ["Source holds/model adoption","30 exact holds, no DIM class/cardinality/CSAPI Profile SHALL/real equipment conformance adopted"],
         ["Next owner-controlled Proceed","G2-7Q original §§13.5.4–13.5.5.6.1 Class5/mechanical; stop before Chapter14 runtime"]]
        replacements={"Master Crosswalk":m["review_grid"],"DIM Register":register_rows,"Summary":summary,"Validation":summary}
        edits={"xl/styles.xml":styles}
        for name,matrix in replacements.items():
            edits[paths[name]]=matrix_to_xml(matrix,sty,main=name=="Master Crosswalk",
                sections=m["review_sections"] if name=="Master Crosswalk" else ())
        preserved={name:digest(oldwb.read(path)) for name,path in paths.items() if name not in replacements}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as wb:
            for info in oldwb.infolist():wb.writestr(info,edits.get(info.filename,oldwb.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as book:
        need(book.testzip() is None and list(old.sheetpaths(book))==list(paths),"same 26 sheets and ZIP valid")
        for name,sha in preserved.items():
            need(digest(book.read(paths[name]))==sha,"previous 22 historic sheets unmodified "+name)
        for p in book.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(book.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(x.get("t")=="e" for x in ET.fromstring(book.read(p)).iter(q("c"))),
                     "no Excel error cells")
        master=ET.fromstring(book.read(paths["Master Crosswalk"]))
        need([x.get("ref") for x in master.find(q("mergeCells")).findall(q("mergeCell"))]
             ==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "original grouped source-case, OGC and DIM layout")
    savedrows=old.readcells(saved,"Master Crosswalk")
    for i,r in enumerate(m["review_grid"],1):
        for j,val in enumerate(r,1):
            need(savedrows.get(addr(i,j),"")==old.val(val),"saved original Excel cell "+addr(i,j))
    previous=old.readcells(prior,"Master Crosswalk")
    changed=sorted(k for k in set(previous)|set(savedrows)
                   if previous.get(k,"")!=savedrows.get(k,""))
    need(len(changed)==28 and all(re.fullmatch(r"I\d+",k) for k in changed),
         "exactly 24 SOSA I-column source cells, no other-donor/case/DIM changes")
    earlier=load("SOSA_G2_7O_Workbook_Validation_11NOV2026.json")
    need(preserved==earlier["exact_original_untouched_xml_sha256"],
         "historical original 22 worksheets unchanged since verified G2-7M")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7P_ORIGINAL_CLASS3_J3_J16_AND_SAME_EDITABLE_26_SHEET_EXCEL_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7P-CANONICAL-VERIFIED","sha256":sha,
       "currently_matches_readable_view":True,
       "lag":"NONE: 346x15 saved XLSX source values match one JSON/both CSV/both MD",
       "refreshed_cell_count":28,"validation_file":reportname})
    m["SOSAEvidence"]["G2_7P"]={"sourceLedger":itemname,
       "sourceReview":"SOSA_G2_7P_Original_Source_and_Master_Reconciliation_11NOV2026.md",
       "qualified_existing_row_matches":28,"original_rule_appearances":74,
       "explicit_SHALL":73,"exact_holds":30,
       "Excel_lag_cells":0,"excel_checkpoint":"SOSA-G2-7P-CANONICAL-VERIFIED",
       "excel_validation":reportname,"DIM_Profile_adopted":False}
    m["SOSAReviewCompletion"]["G2_7P_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="ACTIVE_OPEN__G2_7P_CLASS3_SOURCE_AND_SAME_SAVED_XLSX_VERIFIED__17_UNREAD_1_RESTRICTED"
    nextstep="Only distinct owner Proceed starts G2-7Q original §§13.5.4–13.5.5.6.1 Class5/mechanical, STOP before Chapter14 runtime"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]=nextstep
    m["nextOwnerAction"]=nextstep
    m["publicationPolicy"]="L23 G2-7P one canonical source: 28 SOSA cells, both CSV/MD and SAME 26-sheet Excel, all saved cells and 22 historic worksheets verified"
    save(MASTER,m)
    record={"date":"2026-11-11","step":"SOSA-G2-7P-CONSOLIDATED-SAVED-EXCEL",
      "result":"ORIGINAL_SOURCE_AND_SAME_26_SHEET_EXCEL_PARITY_PASS",
      "workbook_sha256":sha,"previous_workbook_sha256":base_sha,
      "workbook_sheets":list(paths),"refreshed_sheets":list(replacements),
      "exact_original_untouched_xml_sha256":preserved,
      "information_rows":329,"grid_rows":346,"columns":15,
      "historical_donor_facts":58,"case_facts":73,"ISA_source_outcomes":480,"ISA_open_questions":6,
      "source_typed_records":298,"source_rule_appearances":74,
      "source_explicit_SHALL":73,"source_Rule_labeled_descriptive":1,"source_Recommendations":4,"source_Observations":5,"source_Permissions":0,
      "source_tables":14,"pin_or_fiber_rows":135,"source_figure_captions":14,"source_holds":30,
      "qualified_existing_sosa_cells":28,"changed_saved_cells":changed,
      "C239_touched_headings":174,"C239_unread":17,"C239_restricted":1,
      "checks":{"all_saved_346x15_cells_match":True,"both_CSVs_equal":True,
         "both_markdown_tables_equal":True,"same_26_sheets":True,
         "22_historical_sheets_preserved":True,"only_SOSA_I_cells_changed":True,
         "saved_zip_xml_valid":True,"no_error_cells":True,"no_DIM_Profile_adoption":True},
      "limits":["Only original C239 Class3 §§13.5.3.4–13.5.3.17.2; STOP before Class5",
          "J4/J9 source Rule/table and J11 later-section pointer mismatches, figure/native original holds",
          "No actual device, authenticated CSAPI software Commands or source-case conformance"],
      "next":nextstep}
    save(reportname,record)
    print("PASS G2-7P original 74 Rule appearances/73 SHALL, four Recommendations, five Observations, 28 SOSA cells, all saved 346x15 Excel and 22 historic sheets; SHA "+sha)
    return sha

def check_g2_7q_source(z,m=None):
    c=z["counts"];a=z["original_source_items"];ids={x["id"] for x in a}
    need(len(a)==len(ids)==141 and c["source_records"]==141,"141 unique original source items")
    for kind,n in (("RULE",36),("RECOMMENDATION",5),("OBSERVATION",3),
                   ("SECTION",23),("TABLE",4),("TABLE_ROW",39),
                   ("FIGURE_CAPTION",2),("EMBEDDED_SHALL_IN_RECOMMENDATION",1)):
        need(sum(x["kind"]==kind for x in a)==n,"original source type "+kind)
    need(c["source_rule_methods"]=={"I":17,"T":9,"D":1,"I,A":9},
         "all original 36 verification methods, including Demonstration D")
    need(len(z["source_qualified_existing_row_mappings"])==34
         and len(z["exact_holds"])==27,
         "34 source-qualified mappings and 27 explicit holds")
    need(z["original_C239_registered_heading_standing"]==
         {"registered":192,"at_least_sampled_or_inline_read":176,"unread":15,
          "restricted":1,"newly_reviewed":["13.5.4","13.5.5"],
          "full_clause_and_external_original_audit":False},
         "two newly source-read registered headings and still PARTIAL corpus")
    need(z["source"]["original_figure_pixels_read"] is False
         and z["source"]["external_normative_originals_examined"] is False
         and z["source"]["eight_native_C239_companions_read"] is False
         and z["DIM_Profile_adopted"] is False,
         "external/figure/native holds retained, no DIM adoption")
    need(all(x["source_item_ids"] and all(i in ids for i in x["source_item_ids"])
             and x["DIM_Profile_adopted"] is False
             for x in z["source_qualified_existing_row_mappings"]),
         "source IDs valid and no model adoption")
    if m:
        active=[r for r in m["rows"] if r.get("G2_7Q_source_correspondence")]
        need(len(active)==34 and {r["row_id"] for r in active}
             ==set(m["workbookSnapshot"]["G2_7Q_affected_row_ids"]),
             "34 existing source-qualified donor cells only")
        for r in active:
            e=r["G2_7Q_source_correspondence"]
            need(r["display"][8].startswith(e["previous_sosa_cell_value"])
                 and "G2-7Q:" in r["display"][8]
                 and all(i in ids for i in e["source_item_ids"])
                 and e["DIM_Profile_adopted"] is False,
                 "preserve source semantics and prior donor evidence "+r["row_id"])

def publish_g2_7q():
    from html import escape,unescape
    itemname="SOSA_G2_7Q_Original_Source_Item_Coverage_11NOV2026.json"
    reportname="SOSA_G2_7Q_Workbook_Validation_11NOV2026.json"
    base_sha="a8147816f7b2cd36466d3aca8103c395cf836cc25f4dd05224c27ade61217b53"
    m=load(MASTER); z=load(itemname); legacy=load(LEDGER)
    check_source(m,legacy); check_g2_7p_source(load("SOSA_G2_7P_Original_Source_Item_Coverage_11NOV2026.json"),m)
    check_g2_7q_source(z)
    prior=(D/BOOK).read_bytes()
    need(digest(prior)==base_sha==m["currentWorkbookSha256"]
         and m["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7P-CANONICAL-VERIFIED"
         and m["workbookSnapshot"]["currently_matches_readable_view"],
         "current G2-7M SAME Excel is expected original input")
    mapped={}
    for qmap in z["source_qualified_existing_row_mappings"]:
        matched=[r for r in m["rows"] if r["label"]==qmap["label"]]
        need(len(matched)==1 and qmap["label"] not in mapped,"existing unique crosswalk row")
        r=matched[0];prev=r["display"][8]
        need("G2-7Q:" not in prev,"not already integrated")
        new=(prev+" · G2-7Q: "+qmap["native_source_meaning"]+" ["+qmap["relation"]+
            "; "+qmap["negative_equivalence_boundary"]+"]")
        need(len(new)<=32767,"Excel text cell maximum")
        r["display"][8]=new
        r["G2_7Q_source_correspondence"]={
           "source_item_ids":qmap["source_item_ids"],"relation":qmap["relation"],
           "source_native_meaning":qmap["native_source_meaning"],
           "negative_equivalence_boundary":qmap["negative_equivalence_boundary"],
           "previous_sosa_cell_value":prev,"DIM_Profile_adopted":False,
           "original_external_and_image_companions_held":True}
        mapped[qmap["label"]]=new
    need(len(mapped)==34,"exactly 34 source-qualified existing source comparisons")
    positions=[i for i in range(2,len(m["review_grid"])) if i not in set(m["review_sections"])]
    need(len(positions)==len(m["rows"])==329,"original 329 source case/donor/proposed DIM rows")
    for i,r in zip(positions,m["rows"]):
        need(m["review_grid"][i][14]==r["label"],"original row placement untouched")
        m["review_grid"][i][8]=r["display"][8]
    m["workbookSnapshot"]["G2_7Q_affected_row_ids"]=[
        r["row_id"] for r in m["rows"] if r.get("G2_7Q_source_correspondence")]
    check_g2_7q_source(z,m)
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/n).open("w",encoding="utf-8",newline="") as f:
            csv.writer(f,lineterminator="\r\n").writerows(m["review_grid"])
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        original=(D/n).read_text(encoding="utf-8")
        def append_only(match):
            tr=match.group(0);cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            name=unescape(cells[14].group(1))
            if name not in mapped:return tr
            target=cells[8]
            return tr[:target.start(1)]+escape(mapped[name],quote=True)+tr[target.end(1):]
        updated=re.sub(r"<tr>.*?</tr>",append_only,original,flags=re.S)
        need(updated!=original and updated.count("G2-7Q:")>=24,
             "substantive new source mapping in readable comparison "+n)
        (D/n).write_text(updated,encoding="utf-8")
    check_source(m,legacy)
    with zipfile.ZipFile(io.BytesIO(prior)) as oldwb:
        need(oldwb.testzip() is None,"source workbook has good ZIP/CRC")
        paths=old.sheetpaths(oldwb)
        need(len(paths)==26,"same original 26 worksheet names")
        styles,sty=old.newstyles(oldwb.read("xl/styles.xml"))
        register_rows=register_g2_7l(m)
        for k,r in enumerate(m["rows"],1):
            for packet in ("G2_7M","G2_7N","G2_7O","G2_7P","G2_7Q"):
                ev=r.get(packet+"_source_correspondence")
                if not ev:continue
                register_rows[k][9]+="; "+"; ".join(ev["source_item_ids"])
                register_rows[k][10]+="; "+ev["relation"]
                register_rows[k][11]=packet+" original source-qualified hardware: no actual installed power/security/optical service"
        summary=[
         ["SOSA-G2-7Q original Class5 and aperture mechanical","C239 Edition1.1 §§13.5.4–13.5.5.6.1 PDF351–360; STOP before Chapter14"],
         ["Native source evidence","36 original SHALL Rules, 5 Recommendations, 3 Observations, 141 typed source records"],
         ["Original inline source material","23 section headings, four tables/39 rows, two figure captions with image geometry held"],
         ["Source Class5 device role","May be top-level SOSA sensor or hardware sensing element; only EOIR type detailed"],
         ["Class5 J1 electrical","25-pin Micro-D, host nominal24VDC, 2.5A per input pair for 1 second"],
         ["Behavior beyond connector design","Power cycling requires recovery to a communicating state without physical operator action"],
         ["Conditional vendor configuration","Software-configurable user pins need published function list and vendor UI"],
         ["CSAPI boundary","Vendor API example not standardized CSAPI Command; LASER_ARM is hardwired safety control"],
         ["Source labeling caveat","Class5 J1 figure/table captions erroneously say Class3"],
         ["Mechanical aperture class","Self-contained or distributed physical package; eight potentially overlapping shape-axis-CG-weight bands"],
         ["Turret/gimbal source mount","Four SAE AS6169A I-IV turret classes, access hole variants and one small gimbal figure"],
         ["Original C239 heading account","176 at least sampled/inline read,15 unread,1 restricted; two newly reviewed original headings"],
         ["Qualified master increment","34 source-qualified existing SOSA I-column cells, no source-case or DIM adoption"],
         ["Same editable Excel integrity","Original 26 sheets; all 346x15 saved cells equal JSON, both CSV, both readable MD; 22 historic tabs unchanged"],
         ["Source hold status","27 exact local holds; missing external figures and original native companions"],
         ["Only next distinct owner Proceed","G2-7R original Chapter14 §§14–14.5.3, STOP before Chapter15"]]
        replacements={"Master Crosswalk":m["review_grid"],"DIM Register":register_rows,"Summary":summary,"Validation":summary}
        edits={"xl/styles.xml":styles}
        for name,matrix in replacements.items():
            edits[paths[name]]=matrix_to_xml(matrix,sty,main=name=="Master Crosswalk",
                sections=m["review_sections"] if name=="Master Crosswalk" else ())
        preserved={name:digest(oldwb.read(path)) for name,path in paths.items() if name not in replacements}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as wb:
            for info in oldwb.infolist():wb.writestr(info,edits.get(info.filename,oldwb.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as book:
        need(book.testzip() is None and list(old.sheetpaths(book))==list(paths),"same 26 sheets and ZIP valid")
        for name,sha in preserved.items():
            need(digest(book.read(paths[name]))==sha,"previous 22 historic sheets unmodified "+name)
        for p in book.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(book.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(x.get("t")=="e" for x in ET.fromstring(book.read(p)).iter(q("c"))),
                     "no Excel error cells")
        master=ET.fromstring(book.read(paths["Master Crosswalk"]))
        need([x.get("ref") for x in master.find(q("mergeCells")).findall(q("mergeCell"))]
             ==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "original grouped source-case, OGC and DIM layout")
    savedrows=old.readcells(saved,"Master Crosswalk")
    for i,r in enumerate(m["review_grid"],1):
        for j,val in enumerate(r,1):
            need(savedrows.get(addr(i,j),"")==old.val(val),"saved original Excel cell "+addr(i,j))
    previous=old.readcells(prior,"Master Crosswalk")
    changed=sorted(k for k in set(previous)|set(savedrows)
                   if previous.get(k,"")!=savedrows.get(k,""))
    need(len(changed)==34 and all(re.fullmatch(r"I\d+",k) for k in changed),
         "exactly 24 SOSA I-column source cells, no other-donor/case/DIM changes")
    earlier=load("SOSA_G2_7P_Workbook_Validation_11NOV2026.json")
    need(preserved==earlier["exact_original_untouched_xml_sha256"],
         "historical original 22 worksheets unchanged since verified G2-7M")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7Q_ORIGINAL_CLASS5_MECHANICAL_AND_SAME_EDITABLE_26_SHEET_EXCEL_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7Q-CANONICAL-VERIFIED","sha256":sha,
       "currently_matches_readable_view":True,
       "lag":"NONE: 346x15 saved XLSX source values match one JSON/both CSV/both MD",
       "refreshed_cell_count":34,"validation_file":reportname})
    m["SOSAEvidence"]["G2_7Q"]={"sourceLedger":itemname,
       "sourceReview":"SOSA_G2_7Q_Original_Source_and_Master_Reconciliation_11NOV2026.md",
       "qualified_existing_row_matches":34,"original_rule_appearances":36,
       "explicit_SHALL":36,"exact_holds":27,
       "Excel_lag_cells":0,"excel_checkpoint":"SOSA-G2-7Q-CANONICAL-VERIFIED",
       "excel_validation":reportname,"DIM_Profile_adopted":False}
    m["SOSAReviewCompletion"]["G2_7Q_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="ACTIVE_OPEN__G2_7Q_CLASS5_MECHANICAL_SOURCE_SAVED_XLSX_VERIFIED__15_UNREAD_1_RESTRICTED"
    nextstep="Only distinct owner Proceed starts G2-7R original Chapter14 §§14–14.5.3 Run-Time Environment, STOP before Chapter15"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]=nextstep
    m["nextOwnerAction"]=nextstep
    m["publicationPolicy"]="L23 G2-7Q one canonical source: 34 SOSA cells, both CSV/MD and SAME 26-sheet Excel, all saved cells and 22 historic worksheets verified"
    save(MASTER,m)
    record={"date":"2026-11-11","step":"SOSA-G2-7Q-CONSOLIDATED-SAVED-EXCEL",
      "result":"ORIGINAL_SOURCE_AND_SAME_26_SHEET_EXCEL_PARITY_PASS",
      "workbook_sha256":sha,"previous_workbook_sha256":base_sha,
      "workbook_sheets":list(paths),"refreshed_sheets":list(replacements),
      "exact_original_untouched_xml_sha256":preserved,
      "information_rows":329,"grid_rows":346,"columns":15,
      "historical_donor_facts":58,"case_facts":73,"ISA_source_outcomes":480,"ISA_open_questions":6,
      "source_typed_records":141,"source_rule_appearances":36,
      "source_explicit_SHALL":36,"source_Recommendations":5,"source_Observations":3,"source_Permissions":0,
      "source_tables":4,"pin_or_fiber_rows":39,"source_figure_captions":2,"source_holds":27,
      "qualified_existing_sosa_cells":34,"changed_saved_cells":changed,
      "C239_touched_headings":176,"C239_unread":15,"C239_restricted":1,
      "checks":{"all_saved_346x15_cells_match":True,"both_CSVs_equal":True,
         "both_markdown_tables_equal":True,"same_26_sheets":True,
         "22_historical_sheets_preserved":True,"only_SOSA_I_cells_changed":True,
         "saved_zip_xml_valid":True,"no_error_cells":True,"no_DIM_Profile_adoption":True},
      "limits":["Original C239 Class5 and aperture mechanics only, Chapter14 unreviewed",
          "Class5 J1 miscaption, overlapping mechanical classes and mixed GPS Recommendation preserved",
          "Original figures/external standards and installed hardware/runtime conformance not verified"],
      "next":nextstep}
    save(reportname,record)
    print("PASS G2-7Q original 36 SHALL,5 Recommendations,3 Observations,34 SOSA cells, all saved 346x15 Excel and 22 historic sheets; SHA "+sha)
    return sha


def check_g2_7r_source(z,m=None):
    c=z["counts"];a=z["original_source_items"];ids={x["id"] for x in a}
    need(len(a)==len(ids)==127==c["total_source_records"],"G2-7R 127 unique original source records")
    for kind,count in (("RULE",38),("OBSERVATION",18),("PERMISSION",2),
                       ("RECOMMENDATION",1),("SOURCE_SECTION",15),("SOURCE_TABLE",2),
                       ("SOURCE_TABLE_ROW",5),("FIGURE_CAPTION",6),
                       ("SOURCE_CONFIGURATION_FIELD_OR_SUBFIELD",14)):
        need(sum(x["kind"]==kind for x in a)==count,"source-kind audit "+kind)
    need(c["source_rule_method_counts"]=={"I":11,"D":18,"unprinted":9},
         "all 38 printed Rule/method standing including nine no-method Rules")
    need(len(z["exact_holds"])==26 and len(z["source_qualified_existing_row_mappings"])==33,
         "26 original holds and 33 existing-row mappings")
    cov=z["C239_registered_heading_standing"]
    need((cov["registered"],cov["at_least_sampled_or_inline_read"],
          cov["unread"],cov["restricted"])==(192,186,5,1)
         and len(cov["newly_reviewed"])==10,
         "ten original C239 registered headings now inline source-read")
    src=z["source"]
    need(src["source_figures_pixels_verified"] is False
         and src["original_FACE_OCI_DMTF_and_security_companions_read"] is False
         and src["eight_native_C239_companions_read"] is False
         and z["DIM_Profile_adopted"] is False
         and z["independent_runtime_conformance"] is False,
         "original figures/external normative/actual runtime conformance held")
    need({"ProfileType","ImageLoad","Resources","FileSystem","StartOrder"}.issubset(
         {x["field_name"] for x in a if x["kind"]=="SOURCE_CONFIGURATION_FIELD_OR_SUBFIELD"}),
         "five source-native configuration fields individually inspected")
    need(all(x["source_item_ids"] and all(i in ids for i in x["source_item_ids"])
             and x["DIM_Profile_adopted"] is False
             for x in z["source_qualified_existing_row_mappings"]),
         "existing row findings cite exact native source items")
    if m:
        changed=[r for r in m["rows"] if r.get("G2_7R_source_correspondence")]
        need(len(changed)==33 and {r["row_id"] for r in changed}
             ==set(m["workbookSnapshot"]["G2_7R_affected_row_ids"]),
             "exactly 33 unchanged row identities with source-qualified additions")
        for r in changed:
            e=r["G2_7R_source_correspondence"]
            need(r["display"][8].startswith(e["previous_sosa_cell_value"])
                 and "G2-7R:" in r["display"][8]
                 and all(i in ids for i in e["source_item_ids"])
                 and e["DIM_Profile_adopted"] is False,
                 "earlier donor evidence/negative equivalence preserved "+r["row_id"])


def publish_g2_7r():
    from html import escape,unescape
    itemname="SOSA_G2_7R_Original_Source_Item_Coverage_11NOV2026.json"
    reportname="SOSA_G2_7R_Workbook_Validation_11NOV2026.json"
    base_sha="8483b2a0c741fbd290001396a283e39607b06da96cd4cc478d258e73395e1c58"
    m=load(MASTER); z=load(itemname); legacy=load(LEDGER)
    check_source(m,legacy); check_g2_7q_source(load("SOSA_G2_7Q_Original_Source_Item_Coverage_11NOV2026.json"),m)
    check_g2_7r_source(z)
    prior=(D/BOOK).read_bytes()
    need(digest(prior)==base_sha==m["currentWorkbookSha256"]
         and m["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7Q-CANONICAL-VERIFIED"
         and m["workbookSnapshot"]["currently_matches_readable_view"],
         "current G2-7M SAME Excel is expected original input")
    mapped={}
    for qmap in z["source_qualified_existing_row_mappings"]:
        matched=[r for r in m["rows"] if r["label"]==qmap["label"]]
        need(len(matched)==1 and qmap["label"] not in mapped,"existing unique crosswalk row")
        r=matched[0];prev=r["display"][8]
        need("G2-7R:" not in prev,"not already integrated")
        new=(prev+" · G2-7R: "+qmap["native_source_meaning"]+" ["+qmap["relation"]+
            "; "+qmap["negative_equivalence_boundary"]+"]")
        need(len(new)<=32767,"Excel text cell maximum")
        r["display"][8]=new
        r["G2_7R_source_correspondence"]={
           "source_item_ids":qmap["source_item_ids"],"relation":qmap["relation"],
           "source_native_meaning":qmap["native_source_meaning"],
           "negative_equivalence_boundary":qmap["negative_equivalence_boundary"],
           "previous_sosa_cell_value":prev,"DIM_Profile_adopted":False,
           "original_external_and_image_companions_held":True}
        mapped[qmap["label"]]=new
    need(len(mapped)==33,"exactly 33 source-qualified existing source comparisons")
    positions=[i for i in range(2,len(m["review_grid"])) if i not in set(m["review_sections"])]
    need(len(positions)==len(m["rows"])==329,"original 329 source case/donor/proposed DIM rows")
    for i,r in zip(positions,m["rows"]):
        need(m["review_grid"][i][14]==r["label"],"original row placement untouched")
        m["review_grid"][i][8]=r["display"][8]
    m["workbookSnapshot"]["G2_7R_affected_row_ids"]=[
        r["row_id"] for r in m["rows"] if r.get("G2_7R_source_correspondence")]
    check_g2_7r_source(z,m)
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/n).open("w",encoding="utf-8",newline="") as f:
            csv.writer(f,lineterminator="\r\n").writerows(m["review_grid"])
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        original=(D/n).read_text(encoding="utf-8")
        def append_only(match):
            tr=match.group(0);cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            name=unescape(cells[14].group(1))
            if name not in mapped:return tr
            target=cells[8]
            return tr[:target.start(1)]+escape(mapped[name],quote=True)+tr[target.end(1):]
        updated=re.sub(r"<tr>.*?</tr>",append_only,original,flags=re.S)
        need(updated!=original and updated.count("G2-7R:")>=24,
             "substantive new source mapping in readable comparison "+n)
        (D/n).write_text(updated,encoding="utf-8")
    check_source(m,legacy)
    with zipfile.ZipFile(io.BytesIO(prior)) as oldwb:
        need(oldwb.testzip() is None,"source workbook has good ZIP/CRC")
        paths=old.sheetpaths(oldwb)
        need(len(paths)==26,"same original 26 worksheet names")
        styles,sty=old.newstyles(oldwb.read("xl/styles.xml"))
        register_rows=register_g2_7l(m)
        for k,r in enumerate(m["rows"],1):
            for packet in ("G2_7M","G2_7N","G2_7O","G2_7P","G2_7Q","G2_7R"):
                ev=r.get(packet+"_source_correspondence")
                if not ev:continue
                register_rows[k][9]+="; "+"; ".join(ev["source_item_ids"])
                register_rows[k][10]+="; "+ev["relation"]
                register_rows[k][11]=packet+" original source-qualified hardware: no actual installed power/security/optical service"
        summary=[
         ["SOSA G2-7R original Chapter14 RTE","C239 Edition1.1 §§14–14.5.3 PDF361–371, STOP before Chapter15"],
         ["Original source items","38 SHALL,18 Observations,2 Permissions,1 Recommendation,127 classified source records"],
         ["Software runtime alternatives","FACE OSS3.1, OCI Container Runtime1.0.2, DMTF OVF VM2.1.1"],
         ["Native minimum config","ProfileType,ImageLoad,Resources,conditional FileSystem,conditional StartOrder"],
         ["Software config not generic API","Config file format not mandated, human-readable XML/JSON/YAML only SHOULD"],
         ["Source runtime behavior","Three profile-specific runtime variants verify resources, load images, mount FS, honor startup order"],
         ["Observed RTE gaps","Container orchestration,host-resource security,intra-module communication explicitly unspecified"],
         ["SOSA-to-master source increment","33 existing SOSA I-column source-qualified comparisons, zero DIM/Profile adoption"],
         ["C239 heading account","186 at least sampled/inline-reviewed, five unread, one restricted; ten new original headings"],
         ["SAME original editable workbook","26 sheets; 346x15 saved-cell parity with JSON,both CSV,both MD;22 historic tabs preserved"],
         ["Next separate owner Proceed","G2-7S original Chapter15 §§15–15.7 only, STOP before Appendix A"]]
        replacements={"Master Crosswalk":m["review_grid"],"DIM Register":register_rows,"Summary":summary,"Validation":summary}
        edits={"xl/styles.xml":styles}
        for name,matrix in replacements.items():
            edits[paths[name]]=matrix_to_xml(matrix,sty,main=name=="Master Crosswalk",
                sections=m["review_sections"] if name=="Master Crosswalk" else ())
        preserved={name:digest(oldwb.read(path)) for name,path in paths.items() if name not in replacements}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as wb:
            for info in oldwb.infolist():wb.writestr(info,edits.get(info.filename,oldwb.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as book:
        need(book.testzip() is None and list(old.sheetpaths(book))==list(paths),"same 26 sheets and ZIP valid")
        for name,sha in preserved.items():
            need(digest(book.read(paths[name]))==sha,"previous 22 historic sheets unmodified "+name)
        for p in book.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(book.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(x.get("t")=="e" for x in ET.fromstring(book.read(p)).iter(q("c"))),
                     "no Excel error cells")
        master=ET.fromstring(book.read(paths["Master Crosswalk"]))
        need([x.get("ref") for x in master.find(q("mergeCells")).findall(q("mergeCell"))]
             ==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "original grouped source-case, OGC and DIM layout")
    savedrows=old.readcells(saved,"Master Crosswalk")
    for i,r in enumerate(m["review_grid"],1):
        for j,val in enumerate(r,1):
            need(savedrows.get(addr(i,j),"")==old.val(val),"saved original Excel cell "+addr(i,j))
    previous=old.readcells(prior,"Master Crosswalk")
    changed=sorted(k for k in set(previous)|set(savedrows)
                   if previous.get(k,"")!=savedrows.get(k,""))
    need(len(changed)==33 and all(re.fullmatch(r"I\d+",k) for k in changed),
         "exactly 24 SOSA I-column source cells, no other-donor/case/DIM changes")
    earlier=load("SOSA_G2_7Q_Workbook_Validation_11NOV2026.json")
    need(preserved==earlier["exact_original_untouched_xml_sha256"],
         "historical original 22 worksheets unchanged since verified G2-7M")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7R_CHAPTER14_RTE_AND_SAME_ORIGINAL_26_SHEET_EXCEL_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7R-CANONICAL-VERIFIED","sha256":sha,
       "currently_matches_readable_view":True,
       "lag":"NONE: 346x15 saved XLSX source values match one JSON/both CSV/both MD",
       "refreshed_cell_count":33,"validation_file":reportname})
    m["SOSAEvidence"]["G2_7R"]={"sourceLedger":itemname,
       "sourceReview":"SOSA_G2_7R_Original_Source_and_Master_Reconciliation_11NOV2026.md",
       "qualified_existing_row_matches":33,"original_rule_appearances":38,
       "explicit_SHALL":38,"exact_holds":26,
       "Excel_lag_cells":0,"excel_checkpoint":"SOSA-G2-7R-CANONICAL-VERIFIED",
       "excel_validation":reportname,"DIM_Profile_adopted":False}
    m["SOSAReviewCompletion"]["G2_7R_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="ACTIVE_OPEN__G2_7R_CLASS5_MECHANICAL_SOURCE_SAVED_XLSX_VERIFIED__15_UNREAD_1_RESTRICTED"
    nextstep="Only distinct owner Proceed starts G2-7R original Chapter14 §§14–14.5.3 Run-Time Environment, STOP before Chapter15"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]=nextstep
    m["nextOwnerAction"]=nextstep
    m["publicationPolicy"]="L23 G2-7R:33 original RTE source-qualified I-column cells in canonical JSON/both CSV/MD/SAME 26-sheet saved Excel"
    save(MASTER,m)
    record={"date":"2026-11-11","step":"SOSA-G2-7R-CONSOLIDATED-SAVED-EXCEL",
      "result":"ORIGINAL_SOURCE_AND_SAME_26_SHEET_EXCEL_PARITY_PASS",
      "workbook_sha256":sha,"previous_workbook_sha256":base_sha,
      "workbook_sheets":list(paths),"refreshed_sheets":list(replacements),
      "exact_original_untouched_xml_sha256":preserved,
      "information_rows":329,"grid_rows":346,"columns":15,
      "historical_donor_facts":58,"case_facts":73,"ISA_source_outcomes":480,"ISA_open_questions":6,
      "source_typed_records":127,"source_rule_appearances":38,
      "source_explicit_SHALL":38,"source_Recommendations":1,"source_Observations":18,"source_Permissions":2,
      "source_tables":2,"pin_or_fiber_rows":5,"source_figure_captions":6,"source_holds":26,
      "qualified_existing_sosa_cells":33,"changed_saved_cells":changed,
      "C239_touched_headings":186,"C239_unread":5,"C239_restricted":1,
      "checks":{"all_saved_346x15_cells_match":True,"both_CSVs_equal":True,
         "both_markdown_tables_equal":True,"same_26_sheets":True,
         "22_historical_sheets_preserved":True,"only_SOSA_I_cells_changed":True,
         "saved_zip_xml_valid":True,"no_error_cells":True,"no_DIM_Profile_adoption":True},
      "limits":["Only original Chapter14 §§14–14.5.3, Chapter15 unreviewed",
          "FACE/OCI/DMTF originals and RTE figure pixels held; security/orchestration unspecified",
          "No CSAPI software Command or actual runtime conformance observed"],
      "next":nextstep}
    save(reportname,record)
    print("PASS G2-7R 38 SHALL,18 Observations,2 Permissions,1 Recommendation,33 SOSA cells, saved 346x15 Excel; SHA "+sha)
    return sha


def check_g2_7s_source(z,m=None):
    c=z["counts"];rows=z["original_source_items"];ids={x["id"] for x in rows}
    need(len(rows)==len(ids)==113==c["source_records"],
         "113 unique original C239 Chapter15 source records")
    for kind,n in (("RULE",5),("OBSERVATION",1),("PERMISSION",1),
                   ("SOURCE_SECTION",12),("SOURCE_TABLE",4),
                   ("SOURCE_INTERACTION_TYPE",8),("SOURCE_QOS_POLICY_ROW",12),
                   ("SOURCE_BINDING_OPTION",3),("SOURCE_BINDING_STACK_CELL",15),
                   ("SOURCE_QOS_ATTRIBUTE",6),("SOURCE_STACK_DEFINITION",6),
                   ("SOURCE_INTERACTION_ROLE",8)):
        need(sum(x["kind"]==kind for x in rows)==n,
             "source-native clause/table/QoS/binding/role record "+kind)
    need(c["rule_methods"]=={"T":1,"D":2,"unprinted":2},
         "native method annotations preserve 2 Rules without printed method")
    need(len(z["source_qualified_existing_row_mappings"])==41
         and len(z["exact_holds"])==31,
         "41 existing master-row comparisons,31 exact holds")
    cov=z["C239_registered_headings"]
    need((cov["registered"],cov["at_least_sampled_or_inline_read"],
          cov["unread"],cov["restricted"])==(192,189,2,1)
         and cov["newly_source_read"]==["15","15.6","15.7"]
         and cov["chapter15_matrix_future_not_source_read"] is True,
         "Chapter15 source inspected but Services Matrix explicitly future")
    src=z["source"]
    need(src["source_symbol_graphics_pixels_verified"] is False
         and src["original_external_normative_files_examined"] is False
         and src["eight_native_C239_companion_files_examined"] is False
         and z["DIM_Profile_adopted"] is False
         and z["independent_runtime_protocol_conformance"] is False,
         "unreviewed protocol originals/figure symbols and no DIM/CSAPI device adoption")
    need(all(x["source_item_ids"] and all(v in ids for v in x["source_item_ids"])
             and x["DIM_Profile_adopted"] is False
             for x in z["source_qualified_existing_row_mappings"]),
         "exact original source IDs in existing master comparisons")
    if m:
        found=[r for r in m["rows"] if r.get("G2_7S_source_correspondence")]
        need(len(found)==41 and {r["row_id"] for r in found}
             ==set(m["workbookSnapshot"]["G2_7S_affected_row_ids"]),
             "exact 41 approved original master rows only")
        for r in found:
            ev=r["G2_7S_source_correspondence"]
            need(r["display"][8].startswith(ev["previous_sosa_cell_value"])
                 and "G2-7S:" in r["display"][8]
                 and all(i in ids for i in ev["source_item_ids"])
                 and ev["DIM_Profile_adopted"] is False,
                 "source-graded donor evidence and prior cells preserved "+r["row_id"])


def publish_g2_7s():
    from html import escape,unescape
    itemname="SOSA_G2_7S_Original_Source_Item_Coverage_11NOV2026.json"
    reportname="SOSA_G2_7S_Workbook_Validation_11NOV2026.json"
    base_sha="0d92b99df979c524b61a89b11a7ea9cb1a3c2402ab4b59b1aa8f9a82ac24ef8a"
    m=load(MASTER); z=load(itemname); legacy=load(LEDGER)
    check_source(m,legacy); check_g2_7r_source(load("SOSA_G2_7R_Original_Source_Item_Coverage_11NOV2026.json"),m)
    check_g2_7s_source(z)
    prior=(D/BOOK).read_bytes()
    need(digest(prior)==base_sha==m["currentWorkbookSha256"]
         and m["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7R-CANONICAL-VERIFIED"
         and m["workbookSnapshot"]["currently_matches_readable_view"],
         "current G2-7M SAME Excel is expected original input")
    mapped={}
    for qmap in z["source_qualified_existing_row_mappings"]:
        matched=[r for r in m["rows"] if r["label"]==qmap["label"]]
        need(len(matched)==1 and qmap["label"] not in mapped,"existing unique crosswalk row")
        r=matched[0];prev=r["display"][8]
        need("G2-7S:" not in prev,"not already integrated")
        new=(prev+" · G2-7S: "+qmap["native_source_meaning"]+" ["+qmap["relation"]+
            "; "+qmap["negative_equivalence_boundary"]+"]")
        need(len(new)<=32767,"Excel text cell maximum")
        r["display"][8]=new
        r["G2_7S_source_correspondence"]={
           "source_item_ids":qmap["source_item_ids"],"relation":qmap["relation"],
           "source_native_meaning":qmap["native_source_meaning"],
           "negative_equivalence_boundary":qmap["negative_equivalence_boundary"],
           "previous_sosa_cell_value":prev,"DIM_Profile_adopted":False,
           "original_external_and_image_companions_held":True}
        mapped[qmap["label"]]=new
    need(len(mapped)==41,"exactly 41 source-qualified existing source comparisons")
    positions=[i for i in range(2,len(m["review_grid"])) if i not in set(m["review_sections"])]
    need(len(positions)==len(m["rows"])==329,"original 329 source case/donor/proposed DIM rows")
    for i,r in zip(positions,m["rows"]):
        need(m["review_grid"][i][14]==r["label"],"original row placement untouched")
        m["review_grid"][i][8]=r["display"][8]
    m["workbookSnapshot"]["G2_7S_affected_row_ids"]=[
        r["row_id"] for r in m["rows"] if r.get("G2_7S_source_correspondence")]
    check_g2_7s_source(z,m)
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/n).open("w",encoding="utf-8",newline="") as f:
            csv.writer(f,lineterminator="\r\n").writerows(m["review_grid"])
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        original=(D/n).read_text(encoding="utf-8")
        def append_only(match):
            tr=match.group(0);cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            name=unescape(cells[14].group(1))
            if name not in mapped:return tr
            target=cells[8]
            return tr[:target.start(1)]+escape(mapped[name],quote=True)+tr[target.end(1):]
        updated=re.sub(r"<tr>.*?</tr>",append_only,original,flags=re.S)
        need(updated!=original and updated.count("G2-7S:")>=41,
             "substantive new source mapping in readable comparison "+n)
        (D/n).write_text(updated,encoding="utf-8")
    check_source(m,legacy)
    with zipfile.ZipFile(io.BytesIO(prior)) as oldwb:
        need(oldwb.testzip() is None,"source workbook has good ZIP/CRC")
        paths=old.sheetpaths(oldwb)
        need(len(paths)==26,"same original 26 worksheet names")
        styles,sty=old.newstyles(oldwb.read("xl/styles.xml"))
        register_rows=register_g2_7l(m)
        for k,r in enumerate(m["rows"],1):
            for packet in ("G2_7M","G2_7N","G2_7O","G2_7P","G2_7Q","G2_7R","G2_7S"):
                ev=r.get(packet+"_source_correspondence")
                if not ev:continue
                register_rows[k][9]+="; "+"; ".join(ev["source_item_ids"])
                register_rows[k][10]+="; "+ev["relation"]
                register_rows[k][11]=packet+" original source-qualified hardware: no actual installed power/security/optical service"
        summary=[
         ["SOSA G2-7S original Chapter15 Inter-Module Interactions","C239 Ed1.1 §§15–15.7 PDF372–383; STOP before Appendix A"],
         ["Original normative evidence","5 SHALL Rules,1 Observation,1 Permission, 113 typed evidence records"],
         ["Interaction type taxonomy","Eight interaction types: analog, streams/context, low-latency control/discrete, pubsub/request-response/events"],
         ["Native endpoint roles","Sender/receiver, controller/subordinate, writer/reader, publisher/subscriber and requestor/responder"],
         ["Six QoS policy attributes","Reliability Deadline Durability Liveliness Ownership Priority, implementation partly unspecified"],
         ["Three binding stack alternatives","OMG DDS RTPS v1.4+, Protobuf v3+AMQP1.0, Protobuf v3+ZMTP3.0"],
         ["Binding responsibility distinction","Interaction infrastructure vs direct SOSA module implements on-wire stack"],
         ["Conditional transport security","TCP TLS1.2+ and UDP DTLS1.2+ must be configurable if security required; not globally on"],
         ["Source matrix held","15.7 SvcV-3b Services-Services Matrix future; no present source rows to invent"],
         ["Missing source implementations","Pubsub/request-response details, alternative interconnects and source companion protocols held"],
         ["Current original heading standing","189 at least sampled/inline of 192, two unread, one restricted; three newly reviewed headings"],
         ["Source-qualified master increment","41 existing The Open Group SOSA I cells only, no DIM/Profile design adopted"],
         ["Same original saved workbook","26 sheets, all 346x15 saved cells match JSON and both CSV/MD, 22 historic sheets intact"],
         ["Native/external evidence limits","31 local source holds, no external protocol/real device conformance audited"],
         ["Only next owner Proceed","G2-7T original Appendix A and B through PDF392, STOP before G3 original native investigation"]]
        replacements={"Master Crosswalk":m["review_grid"],"DIM Register":register_rows,"Summary":summary,"Validation":summary}
        edits={"xl/styles.xml":styles}
        for name,matrix in replacements.items():
            edits[paths[name]]=matrix_to_xml(matrix,sty,main=name=="Master Crosswalk",
                sections=m["review_sections"] if name=="Master Crosswalk" else ())
        preserved={name:digest(oldwb.read(path)) for name,path in paths.items() if name not in replacements}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as wb:
            for info in oldwb.infolist():wb.writestr(info,edits.get(info.filename,oldwb.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as book:
        need(book.testzip() is None and list(old.sheetpaths(book))==list(paths),"same 26 sheets and ZIP valid")
        for name,sha in preserved.items():
            need(digest(book.read(paths[name]))==sha,"previous 22 historic sheets unmodified "+name)
        for p in book.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(book.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(x.get("t")=="e" for x in ET.fromstring(book.read(p)).iter(q("c"))),
                     "no Excel error cells")
        master=ET.fromstring(book.read(paths["Master Crosswalk"]))
        need([x.get("ref") for x in master.find(q("mergeCells")).findall(q("mergeCell"))]
             ==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "original grouped source-case, OGC and DIM layout")
    savedrows=old.readcells(saved,"Master Crosswalk")
    for i,r in enumerate(m["review_grid"],1):
        for j,val in enumerate(r,1):
            need(savedrows.get(addr(i,j),"")==old.val(val),"saved original Excel cell "+addr(i,j))
    previous=old.readcells(prior,"Master Crosswalk")
    changed=sorted(k for k in set(previous)|set(savedrows)
                   if previous.get(k,"")!=savedrows.get(k,""))
    need(len(changed)==41 and all(re.fullmatch(r"I\d+",k) for k in changed),
         "exactly 24 SOSA I-column source cells, no other-donor/case/DIM changes")
    earlier=load("SOSA_G2_7R_Workbook_Validation_11NOV2026.json")
    need(preserved==earlier["exact_original_untouched_xml_sha256"],
         "historical original 22 worksheets unchanged since verified G2-7M")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7S_CHAPTER15_INTERMODULE_AND_SAME_26_SHEET_EXCEL_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7S-CANONICAL-VERIFIED","sha256":sha,
       "currently_matches_readable_view":True,
       "lag":"NONE: 346x15 saved XLSX source values match one JSON/both CSV/both MD",
       "refreshed_cell_count":41,"validation_file":reportname})
    m["SOSAEvidence"]["G2_7S"]={"sourceLedger":itemname,
       "sourceReview":"SOSA_G2_7S_Original_Source_and_Master_Reconciliation_11NOV2026.md",
       "qualified_existing_row_matches":41,"original_rule_appearances":5,
       "explicit_SHALL":5,"exact_holds":31,
       "Excel_lag_cells":0,"excel_checkpoint":"SOSA-G2-7S-CANONICAL-VERIFIED",
       "excel_validation":reportname,"DIM_Profile_adopted":False}
    m["SOSAReviewCompletion"]["G2_7S_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="ACTIVE_OPEN__G2_7S_CLASS5_MECHANICAL_SOURCE_SAVED_XLSX_VERIFIED__15_UNREAD_1_RESTRICTED"
    nextstep="Only distinct owner Proceed starts G2-7S original Chapter14 §§14–14.5.3 Run-Time Environment, STOP before Chapter15"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]=nextstep
    m["nextOwnerAction"]=nextstep
    m["publicationPolicy"]="L23 G2-7S:41 native interaction source-qualified SOSA I cells, JSON/both CSV/MD and SAME original 26-sheet Excel verified"
    save(MASTER,m)
    record={"date":"2026-11-11","step":"SOSA-G2-7S-CONSOLIDATED-SAVED-EXCEL",
      "result":"ORIGINAL_SOURCE_AND_SAME_26_SHEET_EXCEL_PARITY_PASS",
      "workbook_sha256":sha,"previous_workbook_sha256":base_sha,
      "workbook_sheets":list(paths),"refreshed_sheets":list(replacements),
      "exact_original_untouched_xml_sha256":preserved,
      "information_rows":329,"grid_rows":346,"columns":15,
      "historical_donor_facts":58,"case_facts":73,"ISA_source_outcomes":480,"ISA_open_questions":6,
      "source_typed_records":113,"source_rule_appearances":5,
      "source_explicit_SHALL":5,"source_Recommendations":0,"source_Observations":1,"source_Permissions":1,
      "source_tables":4,"pin_or_fiber_rows":43,"source_figure_captions":0,"source_holds":31,
      "qualified_existing_sosa_cells":41,"changed_saved_cells":changed,
      "C239_touched_headings":189,"C239_unread":2,"C239_restricted":1,
      "checks":{"all_saved_346x15_cells_match":True,"both_CSVs_equal":True,
         "both_markdown_tables_equal":True,"same_26_sheets":True,
         "22_historical_sheets_preserved":True,"only_SOSA_I_cells_changed":True,
         "saved_zip_xml_valid":True,"no_error_cells":True,"no_DIM_Profile_adoption":True},
      "limits":["Original Chapter15 §§15–15.7 only; Appendix A/B not advanced",
          "Source interaction implementations and Services Matrix future; external protocol and original symbols held",
          "No CSAPI Command adoption or actual stream/TLS/QoS conformance witnessed"],
      "next":nextstep}
    save(reportname,record)
    print("PASS G2-7S 5 SHALL,1 Observation,1 Permission,41 SOSA cells and all saved 346x15 Excel; SHA "+sha)
    return sha

def check_g2_7t_source(z,m=None):
    c=z["counts"];items=z["original_source_items"];ids={v["id"] for v in items}
    need(len(ids)==len(items)==107==c["source_records"],
         "107 unique C239 original Appendix A/B native source or pointer items")
    for k,n in (("AV2_NATIVE_DEFINITION",77),("NORMATIVE_COMPANION_FILE_POINTER",8),
                ("SOURCE_APPENDIX_SECTION",9),("SOURCE_SEMANTIC_CONTEXT",12),
                ("RESTRICTED_APPENDIX_LOCATION_POINTER",1)):
        need(sum(v["kind"]==k for v in items)==n,"original appendix native source item "+k)
    need(c["glossary_definitions"]==77 and c["referenced_original_native_companion_files"]==8
         and c["numbered_rule_SHALL"]==0 and c["qualified_existing_master_rows"]==50
         and c["exact_holds"]==30,
         "77 native definitions, eight normative original pointers, no new Rule, 50 qualified rows")
    need(len({v["native_term"] for v in items if v["kind"]=="AV2_NATIVE_DEFINITION"})==77,
         "all glossary terms individually source-located and unique")
    files={v["filename_as_printed"] for v in items if v["kind"]=="NORMATIVE_COMPANION_FILE_POINTER"}
    need(files=={"SOSA_TechStd_v1_DSDM","SOSA_TechStd_v1_DSDM_IDL",
       "System Manager-SysMan-API.json","Module-SysMan-API.json",
       "Security Services-SysMan-API.json","Chassis Manager-SysMan-API.json",
       "PIC-SysMan-API.json","PIC with SW RTE-SysMan-API.json"},
       "eight exact native C239 Appendix B filenames; contents NOT audited")
    cov=z["C239_registered_heading_standing"]
    need((cov["registered"],cov["at_least_sampled_or_inline_read"],
          cov["unread"],cov["restricted"],cov["new_registered_heading_credit"])==(192,189,2,1,0),
         "A/B previously source-read, no false coverage credit; C restricted")
    source=z["source"]
    need(source["original_eight_attached_native_companions_read"] is False
         and source["original_S251_read"] is False
         and source["restricted_AppendixC_read"] is False
         and z["DIM_Profile_adopted"] is False
         and z["independent_real_runtime_conformance"] is False,
         "unexamined normative originals, edition, restricted C and adoption held")
    need(all(x["source_item_ids"] and all(i in ids for i in x["source_item_ids"])
             and x["DIM_Profile_adopted"] is False for x in z["source_qualified_existing_row_mappings"]),
         "exact native glossary IDs and non-adoption for qualified findings")
    if m is not None:
        changed=[r for r in m["rows"] if r.get("G2_7T_source_correspondence")]
        need(len(changed)==50 and {r["row_id"] for r in changed}
             ==set(m["workbookSnapshot"]["G2_7T_affected_row_ids"]),
             "50 distinct existing approved source rows, no novel fields")
        for r in changed:
            ev=r["G2_7T_source_correspondence"]
            need(r["display"][8].startswith(ev["previous_sosa_cell_value"])
                 and "G2-7T:" in r["display"][8]
                 and all(x in ids for x in ev["source_item_ids"])
                 and ev["DIM_Profile_adopted"] is False,
                 "source-glossary qualified SOSA cell and earlier donor content preserved "+r["row_id"])


def publish_g2_7t():
    from html import escape,unescape
    itemname="SOSA_G2_7T_Original_Source_Item_Coverage_11NOV2026.json"
    reportname="SOSA_G2_7T_Workbook_Validation_11NOV2026.json"
    base_sha="89d80712b59c1018eb3c59da1eaa2a518c9d83a6a5f317faf74c60bfd8194a9a"
    m=load(MASTER); z=load(itemname); legacy=load(LEDGER)
    check_source(m,legacy); check_g2_7s_source(load("SOSA_G2_7S_Original_Source_Item_Coverage_11NOV2026.json"),m)
    check_g2_7t_source(z)
    prior=(D/BOOK).read_bytes()
    need(digest(prior)==base_sha==m["currentWorkbookSha256"]
         and m["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7S-CANONICAL-VERIFIED"
         and m["workbookSnapshot"]["currently_matches_readable_view"],
         "current G2-7M SAME Excel is expected original input")
    mapped={}
    for qmap in z["source_qualified_existing_row_mappings"]:
        matched=[r for r in m["rows"] if r["label"]==qmap["label"]]
        need(len(matched)==1 and qmap["label"] not in mapped,"existing unique crosswalk row")
        r=matched[0];prev=r["display"][8]
        need("G2-7T:" not in prev,"not already integrated")
        new=(prev+" · G2-7T: "+qmap["native_source_meaning"]+" ["+qmap["relation"]+
            "; "+qmap["negative_equivalence_boundary"]+"]")
        need(len(new)<=32767,"Excel text cell maximum")
        r["display"][8]=new
        r["G2_7T_source_correspondence"]={
           "source_item_ids":qmap["source_item_ids"],"relation":qmap["relation"],
           "source_native_meaning":qmap["native_source_meaning"],
           "negative_equivalence_boundary":qmap["negative_equivalence_boundary"],
           "previous_sosa_cell_value":prev,"DIM_Profile_adopted":False,
           "original_external_and_image_companions_held":True}
        mapped[qmap["label"]]=new
    need(len(mapped)==50,"exactly 50 original glossary source-qualified existing rows")
    positions=[i for i in range(2,len(m["review_grid"])) if i not in set(m["review_sections"])]
    need(len(positions)==len(m["rows"])==329,"original 329 source case/donor/proposed DIM rows")
    for i,r in zip(positions,m["rows"]):
        need(m["review_grid"][i][14]==r["label"],"original row placement untouched")
        m["review_grid"][i][8]=r["display"][8]
    m["workbookSnapshot"]["G2_7T_affected_row_ids"]=[
        r["row_id"] for r in m["rows"] if r.get("G2_7T_source_correspondence")]
    check_g2_7t_source(z,m)
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/n).open("w",encoding="utf-8",newline="") as f:
            csv.writer(f,lineterminator="\r\n").writerows(m["review_grid"])
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        original=(D/n).read_text(encoding="utf-8")
        def append_only(match):
            tr=match.group(0);cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            name=unescape(cells[14].group(1))
            if name not in mapped:return tr
            target=cells[8]
            return tr[:target.start(1)]+escape(mapped[name],quote=True)+tr[target.end(1):]
        updated=re.sub(r"<tr>.*?</tr>",append_only,original,flags=re.S)
        need(updated!=original and updated.count("G2-7T:")>=50,
             "substantive new source mapping in readable comparison "+n)
        (D/n).write_text(updated,encoding="utf-8")
    check_source(m,legacy)
    with zipfile.ZipFile(io.BytesIO(prior)) as oldwb:
        need(oldwb.testzip() is None,"source workbook has good ZIP/CRC")
        paths=old.sheetpaths(oldwb)
        need(len(paths)==26,"same original 26 worksheet names")
        styles,sty=old.newstyles(oldwb.read("xl/styles.xml"))
        register_rows=register_g2_7l(m)
        for k,r in enumerate(m["rows"],1):
            for packet in ("G2_7M","G2_7N","G2_7O","G2_7P","G2_7Q","G2_7R","G2_7S","G2_7T"):
                ev=r.get(packet+"_source_correspondence")
                if not ev:continue
                register_rows[k][9]+="; "+"; ".join(ev["source_item_ids"])
                register_rows[k][10]+="; "+ev["relation"]
                register_rows[k][11]=packet+" original source-qualified hardware: no actual installed power/security/optical service"
        summary=[
          ["SOSA G2-7T original Appendix A AV-2 and normative Appendix B","C239 Ed1.1 original PDF384–391; p392 only restricted Appendix C pointer; STOP before G3"],
          ["Source items","77 native definitions, eight normative original-file pointers, nine appendix section records"],
          ["Appendix A normative standing","Native glossary definitions NOT newly numbered SHALL Rules or adopted DIM classes"],
          ["System/Subsystem and Sensor","System relational/context-dependent, Sensor device or System; no universal chassis"],
          ["Platform three distinct meanings","Supported device, host vehicle or computing environment; contextual phrase required"],
          ["Module and physical constituent","Module functional entity implementable with hardware/software; Element broader"],
          ["Health/Status/State/Mode/Capability","Separate source meanings; Capability conditioned by Health and Configuration"],
          ["Task and Assignment","Task request from outside sensor; Assignment internal to module"],
          ["Sensor Data Products and Information Products","Raw/minimal and processed/reduced digital output distinct"],
          ["Events and Logging","Detection, Audit Event, Notification, Heartbeat, Relay, Collector and Logging distinct"],
          ["Normative Appendix B eight uninspected originals","Two DSDM/IDL and six separate in-band system management OpenAPI JSON files"],
          ["Source corpus coverage","189 of 192 headings at least sampled/inline-reviewed, two unread, one restricted"],
          ["Source-qualified master increment","50 existing SOSA column-I cells only, no adopted DIM/Profile model"],
          ["Same original editable Excel","26 sheets, all 346x15 cells match canonical JSON/both CSV/both MD,22 historic tabs intact"],
          ["Precise source holds","30 holds including eight original normative companion contents and restricted Appendix C"],
          ["Only next distinct owner Proceed","G3-N1 twelve-artifact and C239/S251 lineage/access inventory; NO native file clause audit yet"]]
        replacements={"Master Crosswalk":m["review_grid"],"DIM Register":register_rows,"Summary":summary,"Validation":summary}
        edits={"xl/styles.xml":styles}
        for name,matrix in replacements.items():
            edits[paths[name]]=matrix_to_xml(matrix,sty,main=name=="Master Crosswalk",
                sections=m["review_sections"] if name=="Master Crosswalk" else ())
        preserved={name:digest(oldwb.read(path)) for name,path in paths.items() if name not in replacements}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as wb:
            for info in oldwb.infolist():wb.writestr(info,edits.get(info.filename,oldwb.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as book:
        need(book.testzip() is None and list(old.sheetpaths(book))==list(paths),"same 26 sheets and ZIP valid")
        for name,sha in preserved.items():
            need(digest(book.read(paths[name]))==sha,"previous 22 historic sheets unmodified "+name)
        for p in book.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(book.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(x.get("t")=="e" for x in ET.fromstring(book.read(p)).iter(q("c"))),
                     "no Excel error cells")
        master=ET.fromstring(book.read(paths["Master Crosswalk"]))
        need([x.get("ref") for x in master.find(q("mergeCells")).findall(q("mergeCell"))]
             ==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "original grouped source-case, OGC and DIM layout")
    savedrows=old.readcells(saved,"Master Crosswalk")
    for i,r in enumerate(m["review_grid"],1):
        for j,val in enumerate(r,1):
            need(savedrows.get(addr(i,j),"")==old.val(val),"saved original Excel cell "+addr(i,j))
    previous=old.readcells(prior,"Master Crosswalk")
    changed=sorted(k for k in set(previous)|set(savedrows)
                   if previous.get(k,"")!=savedrows.get(k,""))
    need(len(changed)==50 and all(re.fullmatch(r"I\d+",k) for k in changed),
         "exactly 24 SOSA I-column source cells, no other-donor/case/DIM changes")
    earlier=load("SOSA_G2_7S_Workbook_Validation_11NOV2026.json")
    need(preserved==earlier["exact_original_untouched_xml_sha256"],
         "historical original 22 worksheets unchanged since verified G2-7M")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7T_APPENDIX_A_B_ORIGINAL_SOURCE_AND_SAME_26_SHEET_EXCEL_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7T-CANONICAL-VERIFIED","sha256":sha,
       "currently_matches_readable_view":True,
       "lag":"NONE: 346x15 saved XLSX source values match one JSON/both CSV/both MD",
       "refreshed_cell_count":50,"validation_file":reportname})
    m["SOSAEvidence"]["G2_7T"]={"sourceLedger":itemname,
       "sourceReview":"SOSA_G2_7T_Original_Source_and_Master_Reconciliation_11NOV2026.md",
       "qualified_existing_row_matches":50,"original_rule_appearances":0,
       "explicit_SHALL":0,"exact_holds":30,
       "Excel_lag_cells":0,"excel_checkpoint":"SOSA-G2-7T-CANONICAL-VERIFIED",
       "excel_validation":reportname,"DIM_Profile_adopted":False}
    m["SOSAReviewCompletion"]["G2_7T_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="ACTIVE_OPEN__G2_7T_APPENDIX_A_B_SAVED_XLSX_VERIFIED__2_UNREAD_1_RESTRICTED"
    nextstep="Only distinct owner Proceed starts G3-N1 source/edition lineage and original normative C239/S251 artifact access inventory; NO native clause audit yet"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]=nextstep
    m["nextOwnerAction"]=nextstep
    m["publicationPolicy"]="L23 G2-7T:50 glossary-backed existing SOSA I cells, JSON/both CSV/MD and SAME original 26-sheet saved Excel, eight native companions remain unread"
    save(MASTER,m)
    record={"date":"2026-11-11","step":"SOSA-G2-7T-CONSOLIDATED-SAVED-EXCEL",
      "result":"ORIGINAL_SOURCE_AND_SAME_26_SHEET_EXCEL_PARITY_PASS",
      "workbook_sha256":sha,"previous_workbook_sha256":base_sha,
      "workbook_sheets":list(paths),"refreshed_sheets":list(replacements),
      "exact_original_untouched_xml_sha256":preserved,
      "information_rows":329,"grid_rows":346,"columns":15,
      "historical_donor_facts":58,"case_facts":73,"ISA_source_outcomes":480,"ISA_open_questions":6,
      "source_typed_records":107,"source_rule_appearances":0,
      "source_explicit_SHALL":0,"source_Recommendations":0,"source_Observations":0,"source_Permissions":0,
      "source_tables":1,"glossary_rows":77,"normative_companion_pointers":8,"source_figure_captions":0,"source_holds":30,
      "qualified_existing_sosa_cells":50,"changed_saved_cells":changed,
      "C239_touched_headings":189,"C239_unread":2,"C239_restricted":1,
      "checks":{"all_saved_346x15_cells_match":True,"both_CSVs_equal":True,
         "both_markdown_tables_equal":True,"same_26_sheets":True,
         "22_historical_sheets_preserved":True,"only_SOSA_I_cells_changed":True,
         "saved_zip_xml_valid":True,"no_error_cells":True,"no_DIM_Profile_adoption":True},
      "limits":["Original Appendix A AV-2 and Appendix B normative pointers only; no native G3 file audit",
          "77 definition rows do not establish new Rules; eight original native referenced files unexamined",
          "No adopted DIM class/chassis/cardinality/CSAPI Profile SHALL or device runtime conformance"],
      "next":nextstep}
    save(reportname,record)
    z["publication_state"]="SOURCE_QUALIFIED_GLOSSARY_AND_SAME_SAVED_26_SHEET_EXCEL_VERIFIED__NATIVE_FILES_UNREAD"
    save(itemname,z)
    print("PASS G2-7T 77 glossary defs, eight native pointers unexamined, 50 SOSA cells and all 346x15 saved Excel; SHA "+sha)
    return sha


def publish_g3_n2():
    """Source-qualified 2022 SOSA v1 DSDM/IDL lineage into SAME original 26-sheet master.

    2023 C239 native byte/edition equivalence remains explicitly UNVERIFIED.
    This is one G3-N2 publisher, not a general model adoption or OpenAPI audit.
    """
    from html import escape, unescape
    itemname="SOSA_G3_N2_Source_Comparison_and_Holds_11NOV2026.json"
    inventname="SOSA_G3_N2_2022_DSDM_Section_Coverage_11NOV2026.json"
    idlname="SOSA_G3_N2_v1_IDL_File_Inventory_11NOV2026.json"
    reportname="SOSA_G3_N2_Workbook_Validation_11NOV2026.json"
    expected_before="46d12624bcdf23c017421ad84262c5bb4761bba4b47181f6ac874f38d60ec9f0"
    m=load(MASTER); base=load(LEDGER); z=load(itemname)
    inv=load(inventname); idl=load(idlname)
    check_source(m,base)
    need(m["currentWorkbookSha256"]==expected_before
         and m["workbookSnapshot"]["checkpoint"]=="SOSA-G2-7T-CANONICAL-VERIFIED"
         and m["workbookSnapshot"]["currently_matches_readable_view"],
         "G2-7T same workbook verified original source checkpoint")
    need(len(inv["items"])==262 and inv["count_by_group"]==
         {"DIV1":117,"DIV2":58,"DIV3MSG":53,"DIV3SUPPORT":34},
         "2022 original PDF 262 source headings independently inventoried")
    need(len(idl["files"])==227 and idl["source_idl_file_count"]==227
         and idl["internal_reference_check"]["unresolved_include_basename_count"]==0,
         "227 original IDL files and native include target inventory")
    need(z["source_edition_grade"].endswith("C239_ED1_1_IDENTICAL_NATIVE_BYTES_UNVERIFIED")
         and not z["DIM_Profile_adopted"] and len(z["local_holds"])==15,
         "2022 source-native with explicit 2023 edition holds")
    mappings=z["qualified_existing_row_mappings"]
    need(len(mappings)==30,"exactly 30 source-qualified 2022 v1 lineage comparisons")
    valid={x["id"] for x in inv["items"]}|{x["id"] for x in idl["files"]}
    seen=set();mapped={}
    for item in mappings:
        label=item["label"]
        matches=[r for r in m["rows"] if r["label"]==label]
        need(len(matches)==1 and label not in seen,
             "one approved master row per source-qualified comparison "+label)
        seen.add(label)
        need(len(item["source_item_ids"])>0
             and all(x in valid for x in item["source_item_ids"])
             and not item["DIM_Profile_adopted"]
             and item["C239_native_bytes_verified"] is False,
             "original source IDs, edition boundary and adoption held "+label)
        row=matches[0];previous=row["display"][8]
        need("G3-N2(v1-2022):" not in previous,"packet already published "+label)
        new=(previous+" · G3-N2(v1-2022): "+item["native_source_meaning"]
             +" ["+item["relation"]+"; "+item["negative_equivalence_boundary"]+"]")
        need(len(new)<32767,"Excel 32767-character cell boundary "+label)
        row["display"][8]=new
        row["G3_N2_source_correspondence"]={
            "source_item_ids":item["source_item_ids"],
            "relation":item["relation"],
            "native_source_meaning":item["native_source_meaning"],
            "negative_equivalence_boundary":item["negative_equivalence_boundary"],
            "edition_grade":"2022 Edition 1.0/v1 lineage; C239 2023 byte identity NOT verified",
            "C239_exact_native_bytes_verified":False,
            "previous_sosa_cell_value":previous,
            "DIM_Profile_adopted":False}
        mapped[label]=new
    need(len(mapped)==30 and len(seen)==30,"30 distinct existing donor cells")
    positions=[i for i in range(2,len(m["review_grid"]))
               if i not in set(m["review_sections"])]
    need(len(positions)==len(m["rows"])==329,"all old master row positions preserved")
    for pos,row in zip(positions,m["rows"]):
        need(m["review_grid"][pos][14]==row["label"],
             "original master candidate-label and location "+row["label"])
        if row["label"] in mapped:
            m["review_grid"][pos][8]=mapped[row["label"]]
    m["workbookSnapshot"]["G3_N2_affected_row_ids"]=[
        r["row_id"] for r in m["rows"] if r.get("G3_N2_source_correspondence")]
    for filename in ("Master_Donor_Concept_to_DIM_Crosswalk.csv",
                     "ISA_Correction_Review_07NOV2026.csv"):
        with (D/filename).open("w",encoding="utf-8",newline="") as output:
            csv.writer(output,lineterminator="\r\n").writerows(m["review_grid"])
    for filename in ("Master_Donor_Concept_to_DIM_Crosswalk.md",
                     "ISA_Correction_Review_07NOV2026.md"):
        source=(D/filename).read_text(encoding="utf-8")
        def amend(match):
            tr=match.group(0)
            cells=list(re.finditer(r"<td>(.*?)</td>",tr,re.S))
            if len(cells)!=15:return tr
            label=unescape(cells[14].group(1))
            if label not in mapped:return tr
            target=cells[8]
            return tr[:target.start(1)]+escape(mapped[label],quote=True)+tr[target.end(1):]
        changed_html=re.sub(r"<tr>.*?</tr>",amend,source,flags=re.S)
        need(changed_html!=source and changed_html.count("G3-N2(v1-2022):")>=30,
             "30 source-qualified readable comparison entries "+filename)
        changed_html=re.sub(r"^# Current[^\n]*",
           "# Current 329×15 donor-to-DIM master — G3-N2 source-qualified 2022 v1 SOSA DSDM/IDL lineage; C239 Ed1.1 native equivalence held (11 November 2026)",
           changed_html,count=1)
        (D/filename).write_text(changed_html,encoding="utf-8")
    check_source(m,base)
    earlier=load("SOSA_G2_7T_Workbook_Validation_11NOV2026.json")
    before=(D/BOOK).read_bytes()
    need(digest(before)==expected_before==earlier["workbook_sha256"],
         "exact G2-7T previously verified original workbook bytes")
    with zipfile.ZipFile(io.BytesIO(before)) as oldbook:
        need(oldbook.testzip() is None,"old original workbook ZIP CRC")
        paths=old.sheetpaths(oldbook)
        need(len(paths)==26,"original 26 worksheets")
        styles,sty=old.newstyles(oldbook.read("xl/styles.xml"))
        register_rows=register_g2_7l(m)
        for idx,row in enumerate(m["rows"],1):
            for packet in ("G2_7M","G2_7N","G2_7O","G2_7P",
                           "G2_7Q","G2_7R","G2_7S","G2_7T","G3_N2"):
                ev=row.get(packet+"_source_correspondence")
                if not ev:continue
                register_rows[idx][9]+="; "+"; ".join(ev["source_item_ids"])
                register_rows[idx][10]+="; "+ev["relation"]
                if packet=="G3_N2":
                    register_rows[idx][11]="2022 v1 source model comparison only; 2023 C239 edition original and DIM/Profile adoption HELD"
        overview=[
          ["SOSA G3-N2 DSDM + IDL 2022 v1 source lineage","Original 2022 Edition1.0 PDF+227 IDL; 2023 C239 original byte-equivalence UNVERIFIED"],
          ["Actual PDF source inventory","117 DIV1 entities/associations,58 DIV2 measurements,53 DIV3 messages,34 shared types"],
          ["Native IDL original sources","227 .idl files, all includes resolve; no compiler conformance"],
          ["SELECTIVE source-native semantics","30 source-qualified comparisons in 57 referenced original source items"],
          ["2022 Ed1.0 source native date","April2022 original PDF; C239 Ed1.1 June/Sept2023 reference same v1 basenames only"],
          ["SOSA own model semantics","Sensor/Component, Host/Platform, Health/State/Mode, BIT, network, native message structures"],
          ["No C239 native equivalence","Publisher binary/source manifest and six original management OpenAPI schemas unexamined"],
          ["Coverage limits","262 heading names inventoried, not 262 complete detailed audits; 20 original figures not fully checked"],
          ["Unresolved precise holds","15 native access/semantics/edition/figure/IDL compiler holds"],
          ["Master/Excel increment","30 existing source-qualified SOSA column I cells, no new rows or donor/case/DIM changes"],
          ["SAME original editable Excel","26 sheets, 346x15 saved exact parity; historical 22 sheets preserved"],
          ["C239 heading standing","189/192 sampled or inline, two substantively unread, one restricted"],
          ["No DIM/Profile adoption","No classes, chassis, fields, cardinalities, SHALL, software Command or device conformance"],
          ["Next distinct owner Proceed","G3-N3 first three native management OpenAPI candidates; C239 originals must be edition-confirmed"]]
        replacement={"Master Crosswalk":m["review_grid"],"DIM Register":register_rows,
                     "Summary":overview,"Validation":overview}
        newdata={"xl/styles.xml":styles}
        for name,matrix in replacement.items():
            newdata[paths[name]]=matrix_to_xml(matrix,sty,main=name=="Master Crosswalk",
                sections=m["review_sections"] if name=="Master Crosswalk" else ())
        preserved={name:digest(oldbook.read(path)) for name,path in paths.items()
                   if name not in replacement}
        output=io.BytesIO()
        with zipfile.ZipFile(output,"w") as archive:
            for info in oldbook.infolist():
                archive.writestr(info,newdata.get(info.filename,oldbook.read(info.filename)))
    saved=output.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as book:
        need(book.testzip() is None,"new saved ZIP CRC")
        need(list(old.sheetpaths(book))==list(paths),"SAME original 26 worksheets in order")
        for name,sha in preserved.items():
            need(digest(book.read(paths[name]))==sha,"22 unchanged original worksheets "+name)
        for p in book.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(book.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(x.get("t")=="e" for x in ET.fromstring(book.read(p)).iter(q("c"))),
                     "no saved Excel error values")
    savedrows=old.readcells(saved,"Master Crosswalk")
    for i,line in enumerate(m["review_grid"],1):
        for j,v in enumerate(line,1):
            need(savedrows.get(addr(i,j),"")==old.val(v),"saved exact 346x15 grid value "+addr(i,j))
    previous=old.readcells(before,"Master Crosswalk")
    changed=sorted(k for k in set(savedrows)|set(previous)
                   if savedrows.get(k,"")!=previous.get(k,""))
    need(len(changed)==30 and all(re.fullmatch(r"I\d+",x) for x in changed),
         "exactly 30 SOSA column I saved cells only")
    need(preserved==earlier["exact_original_untouched_xml_sha256"],
         "original untouched historical worksheets preserved across all packets")
    (D/BOOK).write_bytes(saved)
    sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G3-N2_2022_ORIGINAL_V1_MODEL_LINEAGE_SAME_26_SHEET_EXCEL"
    m["workbookSnapshot"].update({
        "checkpoint":"SOSA-G3-N2-2022-V1-LINEAGE-CANONICAL-VERIFIED",
        "sha256":sha,"currently_matches_readable_view":True,
        "lag":"NONE: 346x15 saved XLSX source equals JSON/both CSV/both MD",
        "refreshed_cell_count":30,"validation_file":reportname})
    m["SOSAEvidence"]["G3_N2"]={
        "sourceReview":"SOSA_G3_N2_Original_2022_DSDM_IDL_and_Master_Reconciliation_11NOV2026.md",
        "sourceLedger":itemname,"original_DSDM_PDF_inventory":inventname,
        "original_v1_IDL_inventory":idlname,
        "source_qualified_existing_row_matches":30,
        "2022_native_DSDM_section_headings":262,"native_IDL_files":227,
        "C239_Ed1_1_native_bytes_equal":False,"precise_holds":15,
        "Excel_lag_cells":0,"DIM_Profile_adopted":False}
    m["SOSAReviewCompletion"]["G3_N2_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="ACTIVE_OPEN__G3_N2_2022_LINEAGE_PARTIAL__2023_NATIVE_EDITION_UNVERIFIED"
    nextstep="Only a separate owner Proceed starts G3-N3 original C239 System Manager, Generic Module and Security Services management OpenAPI source check; if originals unavailable, precise PARTIAL holds, not S251 substitution"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]=nextstep
    m["nextOwnerAction"]=nextstep
    m["publicationPolicy"]="L23 source-first G3-N2 30 original 2022 v1 lineage SOSA I cells; same saved 26-sheet Excel and both mirrors; 2023 C239 native edition identity held"
    save(MASTER,m)
    result={
      "date":"2026-11-11","step":"SOSA-G3-N2-2022-V1-DATA-MODEL-IDL-LINEAGE",
      "result":"ORIGINAL_SOURCE_BOUNDED_PARTIAL_AND_SAME_26_SHEET_EXCEL_PARITY_PASS",
      "workbook_sha256":sha,"previous_workbook_sha256":expected_before,
      "workbook_sheets":list(paths),"refreshed_sheets":list(replacement),
      "exact_original_untouched_xml_sha256":preserved,
      "original_source_edition":"2022 Edition1.0 DSDM PDF + native v1 IDL",
      "C239_Ed1_1_native_byte_equivalence_verified":False,
      "DSDM_heading_items_inventoried":262,"actual_IDL_files_inspected":227,
      "IDL_include_targets_missing":0,"source_qualified_existing_sosa_cells":30,
      "source_qualified_original_source_ids":len({x for item in mappings for x in item["source_item_ids"]}),
      "source_holds":15,"grid_rows":346,"columns":15,
      "information_rows":329,"original_historical_sheet_count":22,
      "changed_saved_cells":changed,
      "C239_registered_headings_sampled_or_inline":189,
      "C239_unread":2,"C239_restricted":1,
      "checks":{"all_saved_346x15_cells_match":True,"both_CSVs_equal":True,
          "both_markdown_tables_equal":True,"same_26_sheets":True,
          "22_historical_sheets_preserved":True,"only_SOSA_I_cells_changed":True,
          "saved_zip_xml_valid":True,"no_error_cells":True,
          "no_DIM_Profile_adoption":True},
      "limits":["Original 2022 Edition 1.0 model lineage, NOT verified C239 2023 native byte equivalence",
        "Inventoried native headings/IDL declarations are not exhaustive semantic clause audits",
        "No adopted DIM class/chassis/cardinality or CSAPI Profile SHALL, no device runtime conformance"],
      "next":nextstep
    }
    save(reportname,result)
    print("PASS G3-N2 2022 v1 partial original source, 30 qualified SOSA cells, all saved 346x15 same original Excel; SHA "+sha)
    return sha


def publish_c2_readability():
    """C2 editorial checkpoint using the existing original 26-sheet XLSX publisher.

    This updates presentation, not SOSA source meaning or an approved DIM/Profile.
    The original source ledgers remain immutable and the canonical JSON retains
    all individual source-correspondence metadata.
    """
    from html import unescape
    from collections import Counter
    reportname="SOSA_C2_Workbook_Validation_12NOV2026.json"
    prior="47c9df11ef64e112c8892e87c749930f08552c43a0e8e06508bb34ef8a04903c"
    m=load(MASTER)
    need(m["schemaVersion"]=="0.15" and len(m["rows"])==329
         and len(m["review_grid"])==346 and len(m["columns"])==15
         and len(m["review_sections"])==15, "unchanged original master structure")
    need(all(len(v)==15 for v in m["review_grid"]), "unchanged 15-column master")
    need(m["currentEvidenceCheckpoint"]=="C2_SOSA_SOURCE_FAITHFUL_PRESENTATION_20261112_PENDING_EXCEL_PUBLISHER", "explicit C2-only checkpoint")
    need(m["currentWorkbookSha256"]==prior and not m["workbookSnapshot"]["currently_matches_readable_view"], "original G3-N2 workbook, not a claimed C2 version")
    need(len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73
         and m["ISAEvidence"]["currentPrimaryReviews"]==480
         and m["ISAEvidence"]["specificQuestions"]==6
         and not m["adoptionPolicy"]["content_adopted_by_this_update"], "original case, donor, ISA, owner evidence preserved")
    checks={"Master_Donor_Concept_to_DIM_Crosswalk.csv":source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv"),
           "ISA_Correction_Review_07NOV2026.csv":source_csv("ISA_Correction_Review_07NOV2026.csv")}
    for name,rows in checks.items():
        need(rows==m["review_grid"], "source CSV parity "+name)
    for n in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        text=(D/n).read_text(encoding="utf-8")
        trs=re.findall(r"<tr[^>]*>[\s\S]*?</tr>",text)
        need(len(trs)==346, "readable Markdown row count "+n)
        for i,tr in enumerate(trs):
            td=re.findall(r"<td>(.*?)</td>",tr,re.S)
            if len(td)==15:
                need([unescape(v) for v in td]==m["review_grid"][i], "readable Markdown exact comparison "+n+" "+str(i+1))
    c1=m["workbookSnapshot"].get("C1_affected_row_ids",[])
    c2=m["workbookSnapshot"].get("C2_affected_row_ids",[])
    need(len(c1)==25 and len(c2)==39 and len(set(c1+c2))==64, "25 C1 plus 39 C2 original IDs")
    need(m["workbookSnapshot"]["C2_mixed_status_prefixes_reconciled"]==8
         and m["workbookSnapshot"]["C1_mixed_status_prefixes_reconciled"]==4, "C1/C2 exact reviewed mixed statuses")
    rowloc={}
    for i,r in enumerate(m["review_grid"],1):
        if i<=2 or i-1 in m["review_sections"]:continue
        rowloc[r[14]]=i
    allowed={"I"+str(rowloc[r["label"]]) for r in m["rows"] if r["row_id"] in c1+c2}
    need(len(allowed)==64, "64 uniquely located original SOSA I-cell changes")
    for r in m["rows"]:
        need(r["display"]==m["review_grid"][rowloc[r["label"]]-1], "row/source grid equality "+r["row_id"])
        need(r.get("dim_adoption")!="ADOPTED" and r["dim_adoption"]=="NO_CONTENT_ADOPTION_DECISION_IN_THIS_UPDATE",
             "no DIM adoption "+r["row_id"])
    oldbytes=(D/BOOK).read_bytes()
    prior_validation=load("SOSA_G3_N2_Workbook_Validation_11NOV2026.json")
    need(digest(oldbytes)==prior==prior_validation["workbook_sha256"], "the *same* original G3-N2 XLSX bytes")
    with zipfile.ZipFile(io.BytesIO(oldbytes)) as z:
        need(z.testzip() is None, "original 26-sheet ZIP CRC")
        paths=old.sheetpaths(z)
        need(len(paths)==26, "all original 26 worksheet names")
        styles,st=old.newstyles(z.read("xl/styles.xml"))
        summary=[
         ["C2 comparison readability — verified 12 November 2026","Same original 26-sheet editable donor-to-DIM master, new presentation only"],
         ["Original 329 information rows / 15 columns","346x15 exact saved comparison values; 15 topic dividers and four cases preserved"],
         ["C1 identity/description, systems and observations","25 SOSA cells shortened/reconciled with four mixed-status corrections"],
         ["C2 configuration and control","39 SOSA cells shortened/reconciled with eight mixed-status corrections"],
         ["Total current text edits","64 distinct existing SOSA I-column cells; all ISA and other donor/case cells unchanged"],
         ["Original research preserves","Detailed native source correspondence per row, 776 SOSA packet contributions, 117 rows, 1583 source references"],
         ["The Open Group SOSA original-grade","C239 2023 Edition1.1 bounded PARTIAL—OWNER ACCEPTED; 191/192 headings *contacted*, not full clause audit"],
         ["Native companion hold","Eight 2023 C239 DSDM/IDL/OpenAPI bytes not authenticated/comprehensively audited"],
         ["Separate 2022 source lineage","2022 v1 DSDM and 227 IDLs selectively inspected; C239 2023 native equivalence unverified"],
         ["Other original source holds","Restricted Appendix C, external originals, figures/matrices, 2025 S251 and 2021 C212 remain held"],
         ["ISA standing","480 reviewed source entries, six local definition questions still open"],
         ["Unchanged historical source details","22 prior worksheets preserved byte for byte; DIM Register unchanged (no new source evidence)"],
         ["Actual saved workbook check","All 346x15 cells compared to JSON and both CSV/Markdown; changed exactly 64 SOSA I cells"],
         ["DIM/Profile adoption","ZERO adopted DIM fields/classes/cardinality, CSAPI SHALLs or runtime conformance"],
         ["Stop gate","C2 complete only; C3, native donor group comparison and SAPIENT require separate owner authorizations"]
        ]
        replace={"xl/styles.xml":styles,
                 paths["Master Crosswalk"]:matrix_to_xml(m["review_grid"],st,main=True,sections=m["review_sections"]),
                 paths["Summary"]:matrix_to_xml(summary,st),
                 paths["Validation"]:matrix_to_xml(summary,st)}
        old_original=prior_validation["exact_original_untouched_xml_sha256"]
        need(len(old_original)==22, "22 original historical worksheets in last independent record")
        for sheet,hashval in old_original.items():
            need(sheet in paths and digest(z.read(paths[sheet]))==hashval,
                 "original historic worksheet source hash "+sheet)
        output=io.BytesIO()
        with zipfile.ZipFile(output,"w") as newzip:
            for info in z.infolist():
                newzip.writestr(info,replace.get(info.filename,z.read(info.filename)))
    newbytes=output.getvalue()
    with zipfile.ZipFile(io.BytesIO(newbytes)) as z:
        need(z.testzip() is None and list(old.sheetpaths(z))==list(paths),"new saved XLSX ZIP CRC and original 26-sheet order")
        for p in z.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(z.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(c.get("t")=="e" for c in ET.fromstring(z.read(p)).iter(q("c"))),"no saved Excel error cells")
        for name,hashval in old_original.items():
            need(digest(z.read(paths[name]))==hashval,"preserve all 22 historical worksheet XML values "+name)
        need(digest(z.read(paths["DIM Register"]))==digest(zipfile.ZipFile(io.BytesIO(oldbytes)).read(paths["DIM Register"])),
             "DIM Register source/evidence sheet unchanged")
    before=old.readcells(oldbytes,"Master Crosswalk")
    current=old.readcells(newbytes,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for k,v in enumerate(row,1):
            need(current.get(addr(i,k),"")==old.val(v),"exact saved 346x15 cell "+addr(i,k))
    changed={cell for cell in set(before)|set(current) if before.get(cell,"")!=current.get(cell,"")}
    need(changed==allowed,"all and only 25 C1 + 39 C2 original SOSA I cells changed")
    (D/BOOK).write_bytes(newbytes)
    sha=digest(newbytes)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="C2_ISA_SOSA_CELL_READABILITY_SAME_26_SHEET_EXCEL_VERIFIED"
    m["publicationPolicy"]="C1 (25) + C2 (39) source-grounded presentation only, same original 26-sheet XLSX refreshed; 2023 C239 original native holds remain."
    m["nextOwnerAction"]="A separate owner Proceed authorizes C3 ONLY, sections 05-06; no C4, donor grouping, SAPIENT or model/client work."
    m["workbookSnapshot"].update({
       "checkpoint":"C2_ISA_SOSA_SOURCE_FAITHFUL_DISPLAY_EXCEL_VERIFIED",
       "sha256":sha,"currently_matches_readable_view":True,
       "lag":"NONE: 346x15 saved same original XLSX matches JSON/BOTH CSV/BOTH Markdown at C2",
       "refreshed_cell_count":64,"validation_file":reportname,
       "C1_comparison_cell_lag":0,"C2_pending_XLSX_lag":0,"C2_XLSX_lag":0,
       "verified_saved_C2_I_cells":39,"verified_saved_C1_I_cells":25
    })
    m["SOSAReviewCompletion"]["status"]="BOUNDED_PARTIAL_OWNER_ACCEPTED_20261112__C2_PRESENTATION_VERIFIED"
    m["SOSAReviewCompletion"]["C2_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="C3 only with separate owner approval; donor grouping/SAPIENT blocked"
    save(MASTER,m)
    validation={
     "date":"2026-11-12","step":"C2_ISA_SOSA_SOURCE_GROUNDED_READABILITY",
     "result":"SAME_ORIGINAL_26_SHEET_SAVED_XLSX_PARITY_PASS",
     "pre_C2_archive_branch":"archive/dim-crosswalk-pre-c2-20261112",
     "prior_original_workbook_sha256":prior,
     "workbook_sha256":sha,
     "workbook_sheets":list(paths),
     "original_22_historical_worksheet_xml_sha256":old_original,
     "preserved_22_historical_sheets":True,
     "unchanged_DIM_Register":True,
     "grid_rows":346,"grid_columns":15,"information_rows":329,"topic_dividers":15,
     "C1_saved_SOSA_cells":25,"C2_saved_SOSA_cells":39,"changed_saved_cells":sorted(changed),
     "C1_changed_row_ids":c1,"C2_changed_row_ids":c2,
     "C2_mixed_prefixes_source_reclassified":8,
     "source_coverage_191_of_192_heading_contact_not_comprehensive":True,
     "C239_2023_original_eight_native_companions_unverified":True,
     "SOSA_donor_disposition":"PARTIAL_OWNER_ACCEPTED",
     "DIM_or_CSAPI_Profile_adopted":False,
     "next_step":"Only a new owner Proceed authorizes C3; no C4, SAPIENT or client",
     "checks":{"saved_grid_all_346x15_exact":True,"all_64_changes_only_SOSA_I":True,
        "two_CSVs_equal":True,"two_Markdown_tables_equal":True,
        "same_26_sheet_workbook":True,"22_original_historical_sheets_preserved":True,
        "workbook_ZIP_crc_and_XML_valid":True,"no_error_cells":True,"no_2023_native_edition_substitution":True}
    }
    save(reportname,validation)
    print("C2 PASS: same original 26 sheets; 25 C1 + 39 C2 I-cells saved; all 346x15 cells exact; SHA "+sha)
    return sha


def publish_c4_readability():
    """Owner-authorized final C4 presentation checkpoint: SAME 26-sheet XLSX, not new SOSA source audit."""
    from html import unescape
    reportname="SOSA_C4_Workbook_Validation_12NOV2026.json"
    m=load(MASTER); prior_record=load("SOSA_C2_Workbook_Validation_12NOV2026.json")
    before_sha=prior_record["workbook_sha256"]
    need(m["currentEvidenceCheckpoint"]=="C4_ISA_SOSA_SOURCE_FAITHFUL_TEXT_PENDING_SAME_EXCEL_PUBLICATION",
         "only the new C4 text checkpoint is eligible")
    grid=m["review_grid"]; snap=m["workbookSnapshot"]
    need(m["schemaVersion"]=="0.15" and len(grid)==346 and all(len(r)==15 for r in grid)
         and len(m["rows"])==329 and len(m["columns"])==15 and len(m["review_sections"])==15,
         "unchanged original 329 information rows, 346x15 grid, 15 sections")
    need(grid==source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")
              ==source_csv("ISA_Correction_Review_07NOV2026.csv"),
         "both canonical CSV mirrors must agree with source grid")
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        html=(D/name).read_text(encoding="utf-8")
        trs=re.findall(r"<tr[^>]*>[\s\S]*?</tr>",html)
        need(len(trs)==346 and html.count('colspan="15"')==15,"346 readable rows/15 dividers "+name)
        for i,tr in enumerate(trs):
            td=re.findall(r"<td>(.*?)</td>",tr,re.S)
            if len(td)==15:need([unescape(v) for v in td]==grid[i],"current Markdown exact at "+name+":"+str(i))
    rowmap={r["row_id"]:r for r in m["rows"]}
    need(len(rowmap)==329 and len({r["label"] for r in m["rows"]})==329,"unique source row identity")
    c3=snap["C3_changed_row_ids"]; c4=snap["C4_affected_row_ids"]
    cells3=set(snap["C3_changed_cells"]); cells4=set(snap["C4_changed_excel_cells"])
    allowed=cells3|cells4
    need(len(c3)==21 and len(c4)==33 and len(allowed)==54 and not cells3&cells4
         and len(snap["C4_affected_row_ids"])==33 and snap["C4_mixed_status_prefixes_reconciled"]==15
         and snap["C4_31_mixed_status_prefixes_cumulative_reconciled"] is True,
         "C3 21 plus C4 33 unique SOSA cells, all 31 mixed assessments reconciled")
    need(all(re.fullmatch(r"I\d+",v) for v in allowed),"SOSA column I edits only")
    aligned=[row for i,row in enumerate(grid) if i>1 and i not in set(m["review_sections"])]
    need(aligned==[r["display"] for r in m["rows"]],"all 329 source row identities and grid values align")
    for r in m["rows"]:
        need(r["dim_adoption"]=="NO_CONTENT_ADOPTION_DECISION_IN_THIS_UPDATE","no DIM adoption "+r["row_id"])
        for key,value in r.items():
            if key.startswith(("G2_","G3_")) and key.endswith("_source_correspondence"):
                need(bool(value.get("source_item_ids")) and
                     value.get("DIM_Profile_adopted",value.get("DIM_adopted",False)) is False,
                     "retained original source IDs/non-adoption "+r["row_id"]+"/"+key)
    need(sum(bool(r["display"][7]) for r in m["rows"])==316 and
         not any(len(r["display"][7])>200 for r in m["rows"]) and
         len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73 and
         m["ISAEvidence"]["currentPrimaryReviews"]==480 and m["ISAEvidence"]["specificQuestions"]==6
         and not m["adoptionPolicy"]["content_adopted_by_this_update"],
         "ISA 316 source summaries, 480 original reviews/six questions, original donor and case evidence")
    oldbytes=(D/BOOK).read_bytes()
    need(digest(oldbytes)==before_sha==m["currentWorkbookSha256"]==snap["sha256"],
         "SAME original C2 26-sheet workbook is baseline; exactly 54 cells not yet published")
    with zipfile.ZipFile(io.BytesIO(oldbytes)) as z:
        need(z.testzip() is None,"original C2 ZIP CRC")
        paths=old.sheetpaths(z)
        need(len(paths)==26 and list(paths)==prior_record["workbook_sheets"],"original 26 sheets and order")
        historic=prior_record["original_22_historical_worksheet_xml_sha256"]
        need(len(historic)==22 and all(digest(z.read(paths[n]))==v for n,v in historic.items()),
             "original historical 22 worksheets checked before edit")
        styles,st=old.newstyles(z.read("xl/styles.xml"))
        summary=[
          ["C4 final donor-cell readability — 12 November 2026","Original editable 26-sheet workbook retained, source-qualified comparison text only"],
          ["Current full master","329 information rows, 15 columns, 15 topic dividers, 346x15 saved comparison values"],
          ["Source cases","Four documentary/historical cases preserved; other donor/OGC foundation/DIM positions unchanged"],
          ["C1 identity/systems/observations","25 SOSA cells; four mixed labels resolved"],
          ["C2 configuration/control","39 SOSA cells; eight mixed labels resolved"],
          ["C3 provenance and held equipment","21 SOSA cells; four mixed labels resolved"],
          ["C4 ISA-derived comparisons","33 SOSA cells; 15 mixed labels resolved"],
          ["Final C1–C4 summary","118 SOSA cells revised; 31 mixed prefixes reconciled; 211 plain unassessed placeholders retained"],
          ["Integrated Sensor Architecture","316 populated ISA summaries mechanically scanned; no new changes; 480 DMS reviews/six original questions"],
          ["SOSA original evidence standing","PARTIAL—OWNER ACCEPTED; 191/192 original headings text or pointer contacted, NOT full clause/companion audit"],
          ["Native corpus holds","2023 eight native companions, Appendix C, external standards, source figures, distinct 2022/2025 editions"],
          ["Original research preservation","Source IDs and relations retained in canonical row packets; original 22 historical worksheets untouched"],
          ["Actual saved worksheet parity","All 346x15 saved values exactly checked; 54 changes C3+C4 confined to SOSA column I"],
          ["DIM/CSAPI Profile adoption","ZERO new class/field/cardinality or Profile SHALL; no runtime equipment control conformance"],
          ["Owner stop","C4 complete; later native donor-grouping study requires its OWN plan/owner action; SAPIENT not authorized"]
        ]
        replace={"xl/styles.xml":styles,
                 paths["Master Crosswalk"]:matrix_to_xml(grid,st,main=True,sections=m["review_sections"]),
                 paths["Summary"]:matrix_to_xml(summary,st),
                 paths["Validation"]:matrix_to_xml(summary,st)}
        output=io.BytesIO()
        with zipfile.ZipFile(output,"w") as newz:
            for info in z.infolist():newz.writestr(info,replace.get(info.filename,z.read(info.filename)))
    newbytes=output.getvalue()
    with zipfile.ZipFile(io.BytesIO(newbytes)) as z:
        need(z.testzip() is None and list(old.sheetpaths(z))==list(paths),"valid original 26-sheet XLSX")
        for n in z.namelist():
            if n.endswith((".xml",".rels")):ET.fromstring(z.read(n))
            if n.startswith("xl/worksheets/") and n.endswith(".xml"):
                need(not any(c.get("t")=="e" for c in ET.fromstring(z.read(n)).iter(q("c"))),
                     "no error cell in saved workbook")
        for n,v in historic.items():need(digest(z.read(paths[n]))==v,"preserved historical sheet "+n)
        need(digest(z.read(paths["DIM Register"]))==
             digest(zipfile.ZipFile(io.BytesIO(oldbytes)).read(paths["DIM Register"])),
             "DIM Register unchanged")
    before=old.readcells(oldbytes,"Master Crosswalk"); current=old.readcells(newbytes,"Master Crosswalk")
    for i,row in enumerate(grid,1):
        for k,val in enumerate(row,1):
            need(current.get(addr(i,k),"")==old.val(val),"saved XLSX vs source cell "+addr(i,k))
    changed={c for c in set(before)|set(current) if before.get(c,"")!=current.get(c,"")}
    need(changed==allowed and len(changed)==54,"ONLY 21 C3 + 33 C4 SOSA I-column saved edits")
    (D/BOOK).write_bytes(newbytes)
    sha=digest(newbytes)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="C4_ISA_SOSA_READABILITY_SAME_26_SHEET_XLSX_VERIFIED"
    m["nextOwnerAction"]="C4 complete: STOP. Only separate owner decision may authorize the deferred high-level native donor-grouping comparison; no automatic SAPIENT, DIM/Profile adoption or Glaux work."
    m["publicationPolicy"]="C1–C4: 118 SOSA source-qualified summary edits and 31 mixed-prefix corrections, SAME 26-sheet Excel verified, nine source holds and six ISA questions retained; no DIM/Profile adoption."
    snap.update({"checkpoint":"C4_ISA_SOSA_SOURCE_FAITHFUL_DISPLAY_EXCEL_VERIFIED",
                 "sha256":sha,"currently_matches_readable_view":True,
                 "lag":"ZERO: saved SAME original XLSX full 346x15 parity with canonical JSON/both CSV/both Markdown",
                 "refreshed_cell_count":54,"validation_file":reportname,
                 "C3_XLSX_lag":0,"C4_XLSX_lag":0,
                 "C4_final_saved_Excel_parity":True,
                 "C4_final_mixed_prefixes_corrected":31})
    m["SOSAReviewCompletion"]["status"]="BOUNDED_PARTIAL_OWNER_ACCEPTED_20261112__C4_READABILITY_EXCEL_VERIFIED"
    m["SOSAReviewCompletion"]["C4_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="C4 complete; owner alone may approve separate native donor grouping study; no auto-SAPIENT or model/client."
    save(MASTER,m)
    validation={
      "date":"2026-11-12","step":"C4_ISA_DERIVED_COMPARISON_FINAL_READABILITY",
      "result":"SAME_ORIGINAL_26_SHEET_SAVED_XLSX_PARITY_PASS",
      "pre_C4_archive_branch":"archive/dim-crosswalk-pre-c4-20261112",
      "pre_C4_research_commit":"a029ce9cb3f918f4f48fd9fc2c00ec0f45d88409",
      "prior_original_workbook_sha256":before_sha,"workbook_sha256":sha,
      "workbook_sheets":list(paths),
      "original_22_historical_worksheet_xml_sha256":historic,
      "information_rows":329,"grid_rows":346,"grid_columns":15,"topic_dividers":15,
      "SOSA_C1_revised_cells":25,"SOSA_C2_revised_cells":39,
      "SOSA_C3_revised_cells":21,"SOSA_C4_revised_cells":33,
      "C4_mixed_labels_corrected":15,"total_mixed_labels_corrected":31,
      "original_plain_unassessed_cells_preserved":211,
      "ISA_populated_summaries_scanned":316,"ISA_changed_summaries":0,
      "C3_C4_changed_saved_cells":sorted(changed),
      "C3_changed_row_ids":c3,"C4_changed_row_ids":c4,
      "source_coverage_comprehensive":False,"source_C239_heading_contact":191,
      "original_C239_eight_native_companions_unverified":True,
      "SOSA_donor_disposition":"PARTIAL_OWNER_ACCEPTED",
      "DIM_or_CSAPI_Profile_adopted":False,
      "checks":{"saved_grid_all_346x15_exact":True,
          "all_54_changes_only_SOSA_I":True,"both_CSVs_equal":True,
          "both_Markdown_tables_equal":True,"same_26_sheet_workbook":True,
          "22_original_historical_sheets_preserved":True,"DIM_Register_unchanged":True,
          "workbook_ZIP_CRC_and_XML_valid":True,"no_error_cells":True,
          "31_mixed_statuses_reconciled":True,"no_2023_native_edition_substitution":True},
      "next":"STOP after C4; separate owner approval required before any native donor-grouping comparison"
    }
    save(reportname,validation)
    print("C4 PASS: SAME 26-sheet original Excel; 54 C3+C4 SOSA I-cells; all 346x15 saved cells; SHA "+sha)
    return sha


# F2-5 — One controlled extension of the existing 26-sheet source-first publisher.
# Authoritative source classifications are committed in canonical JSON and original
# donor source ledgers before this function runs. This routine changes presentation
# and saved workbook references ONLY: no new native equivalence or DIM/Profile adoption.
def publish_f2_5():
    from html import unescape
    reportname="F2_5_Workbook_Validation_13NOV2026.json"
    m=load(MASTER)
    f=m.get("F2_5_color_reconciliation") or {}
    need(m["currentEvidenceCheckpoint"]=="F2_5_CLASSIFICATION_RECONCILED_PENDING_SAME_XLSX_SAVED_VERIFICATION",
         "F2-5 executable only on the eligible source-graded checkpoint")
    rows=m["rows"]; grid=m["review_grid"]; sections=set(m["review_sections"])
    need(len(rows)==337 and len(grid)==354 and len(m["columns"])==15
         and len(sections)==15 and all(len(g)==15 for g in grid),"337 source rows / 354x15 grid")
    aligned=[r for i,r in enumerate(grid) if i>1 and i not in sections]
    need(aligned==[r["display"] for r in rows] and len({r["row_id"] for r in rows})==337,
         "stable original row/display identity")
    need(grid==source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")
              ==source_csv("ISA_Correction_Review_07NOV2026.csv"),
         "both current CSV mirrors exact")
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        html=(D/name).read_text(encoding="utf-8")
        trs=re.findall(r"<tr[^>]*>[\s\S]*?</tr>",html)
        need(len(trs)==354 and html.count('colspan="15"')==15,"both readable tables exact 354/15 "+name)
        for i,tr in enumerate(trs):
            td=re.findall(r"<td>(.*?)</td>",tr,re.S)
            if len(td)==15:
                need([unescape(v) for v in td]==grid[i],
                     "GitHub-readable cell parity "+name+" row "+str(i+1))
    need(all(r.get("dim_adoption")=="NO_CONTENT_ADOPTION_DECISION_IN_THIS_UPDATE" for r in rows)
         and len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73
         and m["ISAEvidence"]["specificQuestions"]==6
         and not m["adoptionPolicy"]["content_adopted_by_this_update"],
         "nonadoption, original donor/case evidence and six ISA questions")
    palette=f.get("legend") or {}
    expected_palette={"COMMON_CANDIDATE":"#D9EAF8",
                      "SPECIALIZED_CANDIDATE":"#F9E6B8",
                      "NATIVE_ONLY_EVIDENCE":"#E5E7EB",
                      "UNRESOLVED_CANDIDATE":"#E9DEFA"}
    need(palette==expected_palette,"owner-approved four exact fill colors")
    decisions=f["color_assignments"]; held=f["composite_holds"]
    need(len(decisions)==325 and len(held)==67 and f["counts"]["missing_source_qualified_rows"]==8
         and len({(r["row_id"],r["column"]) for r in decisions+held})==392,
         "exact cell-level/source-level reconciliation and no duplicate assignments")
    current_positions={}
    data_i=0
    for i,g in enumerate(grid):
        if i>1 and i not in sections:
            record=rows[data_i]
            need(record["display"]==g,"source row/grid order at "+str(i))
            current_positions[record["row_id"]]=i+1
            data_i+=1
    oldbytes=(D/BOOK).read_bytes()
    m00=(D/"Manual_Workbook_Versions/M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx").read_bytes()
    oldsha="724a2488de876d1ad535650f2c60aa3cd8206f641596f681e4a82a4dfd970f70"
    need(digest(oldbytes)==oldsha==digest(m00)==m["currentWorkbookSha256"],
         "protected M00 and same original prior SAP06 book exact-byte identity")
    columns={"G":7,"H":8,"I":9}
    with zipfile.ZipFile(io.BytesIO(oldbytes)) as z:
        need(z.testzip() is None,"original book ZIP CRC")
        paths=old.sheetpaths(z)
        need(len(paths)==26 and "Master Crosswalk" in paths and "DIM Register" in paths
             and "Legend" in paths and "Summary" in paths and "Validation" in paths,
             "original exact 26-sheet live master and existing legend/register")
        oldgridcells=old.readcells(oldbytes,"Master Crosswalk")
        prior=[[oldgridcells.get(addr(i,j),"") for j in range(1,16)] for i in range(1,347)]
        seen=0
        for g in grid:
            if seen<len(prior) and g==prior[seen]:seen+=1
        need(seen==346,"all 346 previous SAP06 display rows preserved as ordered subsequence")
        original_xml={n:digest(z.read(p)) for n,p in paths.items()}
        base_styles,st=old.newstyles(z.read("xl/styles.xml"))
        root=ET.fromstring(base_styles)
        fills=root.find(q("fills"));xfs=root.find(q("cellXfs"))
        need(fills is not None and xfs is not None,"original legacy stylesheet preserved")
        style_ids={}
        for status,hexcolor in palette.items():
            fid=len(fills)
            fil=ET.SubElement(fills,q("fill"))
            pf=ET.SubElement(fil,q("patternFill"),{"patternType":"solid"})
            ET.SubElement(pf,q("fgColor"),{"rgb":"FF"+hexcolor[1:].upper()})
            ET.SubElement(pf,q("bgColor"),{"indexed":"64"})
            clone=ET.fromstring(ET.tostring(xfs[st["data"]]))
            clone.set("fillId",str(fid))
            clone.set("applyFill","1")
            sid=len(xfs)
            xfs.append(clone)
            style_ids[status]=sid
        fills.set("count",str(len(fills)));xfs.set("count",str(len(xfs)))
        new_styles=ET.tostring(root,encoding="utf-8",xml_declaration=True)
        master_xml=ET.fromstring(matrix_to_xml(grid,st,main=True,sections=m["review_sections"]))
        cm={c.get("r"):c for c in master_xml.iter(q("c"))}
        assigned={}
        for a in decisions:
            col=a["column"];rid=a["row_id"];status=a["status"]
            need(col in columns and status in style_ids,"allowed donor and status only")
            excelref=addr(current_positions[rid],columns[col])
            cell=cm.get(excelref)
            need(cell is not None and cell.get("t")=="inlineStr" and
                 bool(rows[data_i-1]) and cell.get("s") in (str(st["data"]),str(st["alt"])),
                 "source-qualified populated candidate cell before color: "+excelref)
            need(excelref not in assigned,"no duplicate Excel cell style")
            assigned[excelref]=status
            cell.set("s",str(style_ids[status]))
        for held_entry in held:
            col=held_entry["column"];rid=held_entry["row_id"]
            need(col in columns and rid in current_positions,"held row identity")
            excelref=addr(current_positions[rid],columns[col])
            need(excelref not in assigned,"mixed/held cell must remain uncolored")
        reg=register(m)
        need(len(reg)==338 and len(reg[0])==12,"existing 337-row DIM Register preserved/extended")
        reg[0]+=["SAPIENT G candidate / color decision","ISA H candidate / color decision",
                 "SOSA I candidate / color decision","F2-5 original native IDs and exact mixed hold"]
        for i,r in enumerate(rows,1):
            notes=r.get("F2_5_cell_classification",{})
            def fld(k):
                v=notes.get(k) or {}
                if not v:return "UNASSESSED — no graded cell classification in F2-5"
                return v["provisional_status"]+"; "+v["cell_decision"]
            original_ids=" | ".join(k+": "+",".join((notes.get(k) or {}).get("original_source_ids",[]))
                                    for k in ("G","H","I") if notes.get(k))
            reg[i]+=[fld("G"),fld("H"),fld("I"),original_ids[:32000]]
        legend_summary=[
          ["F2-5 CLASSIFICATION LEGEND — 13 NOV 2026","Status for original source-qualified candidate meaning; NOT adopted DIM/Profile rule"],
          ["COMMON_CANDIDATE","#D9EAF8","Light blue — useful potential shared information, not mandatory"],
          ["SPECIALIZED_CANDIDATE","#F9E6B8","Light amber — optional equipment/architecture/protocol specialization"],
          ["NATIVE_ONLY_EVIDENCE","#E5E7EB","Light gray — retained native original interface/encoding evidence"],
          ["UNRESOLVED_CANDIDATE","#E9DEFA","Light purple — named original-source meaning question/hold"],
          ["MIXED / COMPOSITE HOLD","NO FILL","Different native meanings in one donor cell; exact source IDs and hold in DIM Register"],
          ["UNASSESSED / NO_ESTABLISHED","NO FILL","Not a negative equivalent, not irrelevant, not native-only"],
          ["F2-5 counts",str(len(decisions))+" colored; "+str(len(held))+" composite holds",
           "ISA 260 colored/38 held; SAPIENT 50/26; SOSA 15/3"],
          ["Current comparison","337 information rows, 354x15 saved comparison grid",
           "3 SOSA + 5 SAPIENT additional candidate rows integrated in SAME existing workbook"],
          ["Evidence/case boundary","Four original cases and original source editions preserved",
           "Not audited whole-source conformance; no physical actuation/Glaux runtime checks"],
          ["Owner-controlled M01","NOT CREATED","M00 preserved byte-identically; manual M01 only on owner decision"]
        ]
        legend_root=ET.fromstring(z.read(paths["Legend"]))
        sd=legend_root.find(q("sheetData"))
        need(sd is not None,"original legend must have existing sheetData")
        old_legend_cells={c.get("r"):old.val("".join(c.itertext())) for c in sd.iter(q("c"))}
        maxr=max([int(r.get("r")) for r in sd.findall(q("row"))] or [0])
        first=maxr+3
        for offset,items in enumerate(legend_summary):
            rn=first+offset
            rr=ET.SubElement(sd,q("row"),{"r":str(rn),"ht":"42","customHeight":"1"})
            for j,value in enumerate(items,1):
                if not value:continue
                status=items[0] if offset in (1,2,3,4) else None
                style=style_ids.get(status,st["header"] if offset in (0,7) else st["data"])
                c=ET.SubElement(rr,q("c"),{"r":addr(rn,j),"s":str(style),"t":"inlineStr"})
                t=ET.SubElement(ET.SubElement(c,q("is")),q("t"))
                t.set(q("space","http://www.w3.org/XML/1998/namespace"),"preserve");t.text=str(value)
        dimension=legend_root.find(q("dimension"))
        if dimension is not None:dimension.set("ref","A1:P"+str(first+len(legend_summary)-1))
        summary=[
          ["F2-5 source-qualified candidate-cell coloring | 13 November 2026",
           "SAME original 26-sheet editable master; M00 frozen; M01 awaits owner"],
          ["Canonical source-comparison","337 data rows, 15 columns, 15 original topic dividers; 354x15 actual saved cells"],
          ["Eight added information candidates","Three original-source SOSA architecture and five SAPIENT interface reporting/roles"],
          ["ISA F2-4 candidate grading","298 row opportunities; 260 single-meaning cells colored, 38 composite native-source cells held"],
          ["SAPIENT F2-3 candidate grading","109 original finding records; 50 selected source-qualified G-cells colored, 26 mixed held"],
          ["The Open Group SOSA F2-2 candidate grading","35 native findings; 15 supported I-cells colored, 3 mixed held"],
          ["Actual colored cells",str(len(decisions))+" exact donor cells; no case/OGC/DIM cells colored"],
          ["Original single-meaning fills","Light blue / amber / gray / purple; see existing Legend worksheet"],
          ["Mixed/unassessed source handling","No misleading fill; 67 composite holds have exact native IDs in canonical JSON and DIM Register"],
          ["Original non-classification source text","All previous 346 displayed grid rows survive in order, plus eight justified source-specific candidate rows"],
          ["M00 protection","Original named M00 and pre-F2-5 GitHub archive preserved; no M01"],
          ["ISA held definitions","Six exact original-source interpretation questions carried"],
          ["The Open Group SOSA disposition","Bounded PARTIAL—OWNER ACCEPTED, nine source-hold families retained"],
          ["SAPIENT disposition","39 overlapping original holds retained; owner SAP07 Option A/B UNDECIDED"],
          ["DIM and CSAPI Profile","No adopted classes, mandatory fields/cardinalities or Profile SHALLs"],
          ["Runtime","No new original device, command, client, server or conformance tests"],
          ["Current owner stop","F2-5 workbook/checkpoint complete, ask owner to review; no automatic further work"]
        ]
        replace={"xl/styles.xml":new_styles,
                 paths["Master Crosswalk"]:ET.tostring(master_xml,encoding="utf-8",xml_declaration=True),
                 paths["DIM Register"]:matrix_to_xml(reg,st),
                 paths["Summary"]:matrix_to_xml(summary,st),
                 paths["Validation"]:matrix_to_xml(summary,st),
                 paths["Legend"]:ET.tostring(legend_root,encoding="utf-8",xml_declaration=True)}
        preserved={name:sha for name,sha in original_xml.items() if paths[name] not in replace}
        need(len(preserved)==21,"21 historical source/case/decision sheets must remain byte-unchanged")
        output=io.BytesIO()
        with zipfile.ZipFile(output,"w") as out:
            for info in z.infolist():out.writestr(info,replace.get(info.filename,z.read(info.filename)))
    newbytes=output.getvalue()
    with zipfile.ZipFile(io.BytesIO(newbytes)) as z:
        need(z.testzip() is None and list(old.sheetpaths(z))==list(paths),"reopened 26-sheet ZIP identity and CRC")
        for name,p in paths.items():
            if name in preserved:need(digest(z.read(p))==preserved[name],"preserved old source/case sheet "+name)
        for p in z.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(z.read(p))
        actual_styles=ET.fromstring(z.read("xl/styles.xml"))
        actual_fills=actual_styles.find(q("fills"))
        actual_xfs=actual_styles.find(q("cellXfs"))
        actual_master=ET.fromstring(z.read(paths["Master Crosswalk"]))
        cells={c.get("r"):c for c in actual_master.iter(q("c"))}
        actual_colored={}
        for ref,status in assigned.items():
            cv=cells[ref]
            sid=int(cv.get("s"))
            need(sid==style_ids[status] and
                 int(actual_xfs[sid].get("fillId"))<len(actual_fills),
                 "saved style index/Excel cell "+ref)
            fill=actual_fills[int(actual_xfs[sid].get("fillId"))]
            hexrgb=fill.find(".//"+q("fgColor")).get("rgb")
            need(hexrgb=="FF"+palette[status][1:].upper(),"saved exact RGB at "+ref)
            actual_colored[ref]=status
        need(len(actual_colored)==325,"exact 325 saved, individually justified cell colors")
        for held_entry in held:
            ref=addr(current_positions[held_entry["row_id"]],columns[held_entry["column"]])
            c=cells.get(ref)
            need(c is None or int(c.get("s","0")) not in style_ids.values(),
                 "mixed source held without a misleading fill "+ref)
        for c in actual_master.iter(q("c")):
            need(c.get("t")!="e","no spreadsheet error cell")
        legend_after=ET.fromstring(z.read(paths["Legend"]))
        after_legend={c.get("r"):old.val("".join(c.itertext())) for c in legend_after.iter(q("c"))}
        need(all(ref in after_legend for ref in old_legend_cells),
             "existing legend cells and addresses preserved before appended F2-5 key")
        for ref,val in old_legend_cells.items():
            need(after_legend[ref]==val,"original legend cell content unchanged "+ref)
    saved=old.readcells(newbytes,"Master Crosswalk")
    for i,row in enumerate(grid,1):
        for j,v in enumerate(row,1):
            need(saved.get(addr(i,j),"")==old.val(v),"saved grid/JSON/CSV/Markdown parity "+addr(i,j))
    regcells=old.readcells(newbytes,"DIM Register")
    need(sum(bool(re.fullmatch("A[0-9]+",c)) for c in regcells)==338,
         "337 register rows plus header actually saved")
    need(newbytes!=oldbytes and digest(m00)==oldsha,"changed ONLY living XLSX, protected M00 unchanged")
    (D/BOOK).write_bytes(newbytes)
    newsha=digest(newbytes)
    m["currentWorkbookSha256"]=newsha
    m["currentEvidenceCheckpoint"]="F2_5_SAME_26_SHEET_COLOR_XLSX_SAVED_VALUES_AND_STYLES_VERIFIED"
    m["nextOwnerAction"]="STOP after F2-5 for owner review. M00 remains preserved; separately owner-approved M01 manual snapshot may follow. SAPIENT SAP07 A/B still pending. No new donor, DIM/Profile adoption, Glaux code or deployment."
    m["publicationPolicy"]="F2-5 one canonical JSON/two CSV/two Markdown and SAME 26-sheet XLSX; 337 source-graded information rows, 354x15 values, 325 cell colors, 67 composite holds; 21 original history/source/case sheet XMLs byte preserved; no DIM/Profile adoption."
    m["workbookSnapshot"].update({
      "checkpoint":"F2_5_SAME_26_SHEET_XLSX_VALUES_STYLES_VERIFIED",
      "sha256":newsha,
      "information_rows":337,
      "columns":15,
      "currently_matches_readable_view":True,
      "lag":"ZERO: 337 information rows / 354x15 saved grid, all eight F2-2/F2-3 donor candidates inserted; source-qualified 325 fills and explicit 67 composite holds",
      "textCheckpoint":"F2_5_SOURCE_QUALIFIED_CANDIDATE_COLOR_PUBLICATION",
      "textInformationRows":337,
      "validation_file":reportname,
      "color_cell_count":325,
      "mixed_source_cells_uncolored":67,
      "manual_M00_preserved":True,
      "manual_M01_not_created":True
    })
    f["status"]="F2_5_SAVED_XLSX_GRID_COLOR_AND_LEGEND_VERIFIED__OWNER_REVIEW_STOP"
    f["workbook_sha256"]=newsha
    f["M01_created"]=False
    save(MASTER,m)
    validation={
      "date":"2026-11-13","step":"F2-5",
      "result":"SAME_ORIGINAL_26_SHEET_SAVED_GRID_AND_STYLE_PARITY_PASS",
      "pre_F2_5_research_head":"d5840210f71f71dfd013f9e224dc2d3fb5757c40",
      "preserved_archive_branch":"archive/dim-crosswalk-pre-f2-5-20261113",
      "prior_original_book_sha256":oldsha,"protected_M00_sha256":digest(m00),
      "new_living_XLSX_sha256":newsha,
      "workbook_sheets_in_original_order":list(paths),
      "source_case_history_sheets_byte_identical":preserved,
      "original_legend_cells_preserved":len(old_legend_cells),
      "new_classification_legend_entries":len(legend_summary),
      "information_rows":337,"grid_rows":354,"grid_columns":15,
      "validated_saved_grid_cells":354*15,
      "new_rows_vs_original":8,"exact_sourced_colored_cells":len(assigned),
      "colored_by_status":f["counts"]["by_candidate_status"],
      "colored_and_held_by_donor":f["counts"]["by_donor_column"],
      "composite_native_meanings_held_uncolored":len(held),
      "old_grid_rows_subsequence_preserved":346,
      "new_337_row_DIM_Register_saved":True,
      "four_original_cases_and_58_donor_73_case_records_preserved":True,
      "ISA_six_questions_held":True,"SOSA_nine_source_hold_families_retained":True,
      "SAPIENT_39_overlapping_holds_owner_A_B_pending":True,
      "manual_M01_created":False,"DIM_CSAPI_Profile_adopted":False,
      "checks":{"both_CSV_mirrors_equal_JSON":True,"both_Markdown_views_equal_JSON":True,
                "saved_5310_grid_cell_values_exact":True,"saved_325_color_cells_exact_RGB":True,
                "all_67_mixed_native_cells_without_fill":True,"no_unassessed_or_negative_as_native_gray":True,
                "all_26_original_sheet_names_and_order":True,
                "21_historical_sheet_xml_byte_preserved":True,
                "original_Legend_values_preserved_and_key_appended":True,
                "M00_exact_original_binary_preserved":True,
                "zip_crc_all_xml_and_reopened_cells_pass":True,
                "source_review_completeness_NOT_claimed":True,
                "new_runtime_conformance_NOT_performed":True},
      "next":"STOP for owner review/possible separately owner-approved M01; no automatic next donor or DIM/Profile/UI"
    }
    save(reportname,validation)
    need(digest((D/BOOK).read_bytes())==newsha and digest(m00)==oldsha,
         "final original M00 and saved living XLSX readback")
    print("F2-5 PASS: SAME 26-sheet workbook / 337 rows / 354x15 = 5310 saved cells")
    print("F2-5 PASS: 325 exact RGB donor-cell fills; 67 mixed native meaning cells held uncolored")
    print("F2-5 PASS: 21 original source/case/history sheets unchanged, old Legend values preserved")
    print("F2-5 PASS: protected M00 unchanged, M01 owner-pending, no DIM/Profile/Glaux adoption")
    return newsha


# AAS02-G: source-grounded owner-approved insertion within the SAME original 26-sheet
# workbook. This extends the established publisher, not its historical workflows.
def publish_aas02_g():
    from collections import defaultdict
    from html import escape, unescape
    def verify(ok,why):
        if not ok:raise AssertionError("AAS02-G saved-XLSX validation: "+why)
    ledgername="AAS01_Original_Source_Corpus_Coverage_13NOV2026.json"
    validationname="AAS02_G_Column_Workbook_Validation_13NOV2026.json"
    m=load(MASTER);led=load(ledgername);a=led["AAS02"];approval=a["owner_layout_decision"]
    verify(approval["status"]=="EXPLICIT_OWNER_APPROVAL_OF_AAS32_COLUMN_POSITION_ONLY__NOT_YET_EXECUTED",
           "one owner-approved G position, not already executed")
    grid=m["review_grid"];rs=m["rows"];dividers=set(m["review_sections"])
    verify(len(grid)==354 and all(len(g)==15 for g in grid)
           and len(rs)==337 and len(m["columns"])==15 and len(dividers)==15,
           "original 337 information rows and 354x15 grid")
    verify([c["key"] for c in m["columns"]][:7]==["Dragino","AirGradient","Campbell","Bennett","IEEE","OPC","SAPIENT"]
           and m["columns"][-1]["key"]=="DIM","old column identities")
    verify([g for i,g in enumerate(grid) if i>1 and i not in dividers]==[r["display"] for r in rs],
           "all original data rows and case/donor text")
    verify(grid==source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")
               ==source_csv("ISA_Correction_Review_07NOV2026.csv"),"preflight both CSV and JSON")
    verify(len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73
           and m["ISAEvidence"]["specificQuestions"]==6
           and not m["adoptionPolicy"]["content_adopted_by_this_update"],"original source holds/cases/nonadoption")
    verify(len(a["original_items"])==42 and len(a["open_holds"])==8 and len(led["holds"])==7,
           "original AAS01/AAS02 source evidence")
    prevhash="bde0ed76319d8c4e0ef6be192d6c0c3f6ad001a1650a7ff537a612d2d7fe4c4c"
    original=(D/BOOK).read_bytes()
    m00=(D/"Manual_Workbook_Versions/M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx").read_bytes()
    m01=(D/"Manual_Workbook_Versions/M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx").read_bytes()
    verify(digest(original)==digest(m01)==prevhash==m["currentWorkbookSha256"],"original M01 and living workbook byte-identical")
    verify(digest(m00)=="724a2488de876d1ad535650f2c60aa3cd8206f641596f681e4a82a4dfd970f70","M00 untouched")
    colors=m["F2_5_color_reconciliation"]
    verify(len(colors["color_assignments"])==325 and len(colors["composite_holds"])==67,"F2-5 source style/hold controls")
    origcols=[c["key"] for c in m["columns"]];origgrid=[r[:] for r in grid]
    positions={};id_to_row={}
    k=0
    for index,g in enumerate(grid):
        if index>1 and index not in dividers:
            row=rs[k];positions[row["row_id"]]=index+1;id_to_row[index+1]=row;k+=1
    verify(k==337 and len(positions)==337,"stable source row locations")
    grouped=defaultdict(list)
    for item in a["original_items"]:
        verify(item["source_id"].startswith("AAS02-N")
               and item["source_lines"][0]>0 and item["source_lines"][1]>=item["source_lines"][0]
               and "ecd191273a28dd9c4e7bb75e923f0f0fe5da444e" in item["source_url"],
               "original published native source locator "+item["source_id"])
        for x in item["provisional_existing_master_correspondence"]:
            n=int(x["current_grid_row"])
            verify(n in id_to_row and grid[n-1][14]==x["current_dim_label"]
                   and x["relation"] in ("RELATED","PARTIAL"),
                   "original source-to-existing-row target "+item["source_id"]+" "+str(n))
            grouped[n].append((item,x))
    verify(len(grouped)==8 and sum(len(v) for v in grouped.values())==57,"eight supported cells, 57 source links")
    summaries={
      5:"AssetKind Type/Instance/Batch/Role is distinct from HasKind Template/Instance; optional assetType may identify another type asset. Neither proves a marketed manufacturer model or its installed unit.",
      6:"SpecificAssetId name/value may carry a serial or proprietary identifier; globalAssetId is a distinct asset ID, and AASd-131 requires at least one asset ID. No fielded hardware serial is established by AAS alone.",
      7:"Globally unique AAS Identifiable.id differs from represented-asset globalAssetId/specific IDs and scoped idShort. Model/external references and URL-shaped identifiers are not necessarily CSAPI System URIs or fetchable devices.",
      10:"One AAS digitally represents one asset, which may be physical or software. Submodels describe aspects of the asset rather than observed physical parts of a sensing installation.",
      13:"Entity can represent parts of a composite asset or bill of materials; Submodels are informational. This alone is not a record of installed hardware constituents.",
      14:"ModelReference, ExternalReference and semantic RelationshipElement can express links, but do not prove actual cables, current network connectivity or equipment attachment.",
      251:"AdministrativeInformation version/revision, creator and createdAt/updatedAt describe business-relevant digital records, not actual sensor firmware, current field configuration or observation time.",
      277:"AAS derivedFrom refers to derivation between digital shells. Entity and RelationshipElement can model relationships, but cannot establish observed physical parent/child attachment."
    }
    verify(set(grouped)==set(summaries),"eight source-qualified AAS topics")
    notes={};mapping={}
    for n,links in sorted(grouped.items()):
        ids=list(dict.fromkeys(item["source_id"] for item,x in links))
        relations=sorted(set(x["relation"] for item,x in links))
        meaning="/".join(relations)
        notes[n]=(meaning+": IDTA-01001 Part1 Metamodel 3.2.0 (July 2026): "+
                 summaries[n]+" Original source IDs: "+", ".join(ids)+
                 ". BOUNDED PARTIAL research; not a mandatory DIM field/class, CSAPI Profile SHALL, AAS conformance or verified installed AAS record.")
        verify(len(notes[n])<32767,"Excel cell length")
        mapping[n]={"relation":meaning,"source_ids":ids,"source_link_count":len(links),
          "original_source_standings":list(dict.fromkeys(item["source_standing"] for item,x in links)),
          "source":"IDTA-01001 Part1 v3.2.0, pinned release 26-01",
          "source_register":ledgername,"research_only":True,"DIM_CSAPI_Profile_adopted":False,
          "original_master_row_id":id_to_row[n]["row_id"],"provisional_display":notes[n]}
    m["columns"].insert(6,{"key":"AAS32","name":"AAS v3.2 — IDTA 01001 Part 1 Metamodel",
       "group":"OTHER_DONOR_STANDARDS","kind":"BOUNDED_SOURCE_FIRST_DONOR",
       "edition":"IDTA-01001 Part1 v3.2.0 (Release 26-01, July 2026)",
       "source_pin":"admin-shell-io/aas-specs-metamodel@ecd191273a28dd9c4e7bb75e923f0f0fe5da444e",
       "source_ledger":ledgername,"DIM_CSAPI_Profile_adopted":False})
    for index,row in enumerate(grid):
        row.insert(6, m["columns"][6]["name"] if index==1 else notes.get(index+1,""))
    for n,r in id_to_row.items():
        r["display"].insert(6,notes.get(n,""))
        if n in mapping:r["AAS02_IDTA01001_source_correspondence"]={**mapping[n],"column":"G"}
    verify(len(m["columns"])==16 and len(m["review_sections"])==15
           and all(len(x)==16 for x in grid) and all(len(x["display"])==16 for x in rs),
           "16-column canonical schema")
    verify([c["key"] for c in m["columns"] if c["key"]!="AAS32"]==origcols,
           "old donor ordering unmodified")
    for i,oldrow in enumerate(origgrid):
        verify(grid[i][:6]==oldrow[:6] and grid[i][7:]==oldrow[6:],
               "old source/case/OGC/DIM cells unchanged at "+str(i+1))
    verify([g for i,g in enumerate(grid) if i>1 and i not in dividers]==[r["display"] for r in rs],
           "337 exact source row displays")
    # Emit BOTH CSV mirrors directly from the ONE canonical data matrix.
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/name).open("w",encoding="utf-8",newline="") as h:
            csv.writer(h,lineterminator="\n").writerows(grid)
        verify(source_csv(name)==grid,"new mirror "+name)
    # Produce both readable HTML-in-Markdown views, preserving the original
    # historical preamble and all other donor/case/OGC contents.
    oldmarkdown=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    verify(oldmarkdown==(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
           and oldmarkdown.count("<table>")==1,"original two readable mirrors identical")
    pre=oldmarkdown.split("<table>",1)[0]
    intro=("# CURRENT — Source-qualified AAS02 donor column G integrated into SAME verified 26-sheet master (13 November 2026)\n\n"
         "The newly approved G, after OPC UA Devices F, contains EIGHT original IDTA-01001 v3.2.0 RELATED/PARTIAL research cells; "
         "42 original source items and 57 source-to-row links are evidence, not adopted DIM fields. "
         "Original case and other donor/OGC values shifted without alteration; proposed DIM stays rightmost P. "
         "Prior 325 source-qualified color fills and 67 composite held cells retain original status in shifted H/I/J. "
         "Eight new AAS cells are intentionally UNCOLORED pending individual native-meaning classification; blank rows mean UNASSESSED, not NO_ESTABLISHED. "
         "Original source evidence: [cumulative AAS register]("+ledgername+"). "
         "Original manually protected M00/M01 unchanged, no class/Profile SHALL/physical device proof or Glaux change. "
         "One next owner Proceed may authorize AAS03 source-first only. STOP.\n\n---\n\n")
    header='<table>\n<thead><tr><th colspan="4">SOURCE CASES</th><th colspan="6">OTHER DONOR STANDARDS</th><th colspan="5">FOUNDATIONAL SENSING / OBSERVATION</th><th>PROPOSED DIM</th></tr>\n'
    header+="<tr>"+"".join("<th>"+escape(c["name"])+"</th>" for c in m["columns"])+"</tr></thead><tbody>\n"
    body=[]
    for i in range(2,len(grid)):
        if i in dividers:
            body.append('<tr><th colspan="16">'+escape(str(grid[i][0]))+"</th></tr>")
        else:
            body.append("<tr>"+"".join("<td>"+escape(str(v))+"</td>" for v in grid[i])+"</tr>")
    md=intro+pre+header+"\n".join(body)+"\n</tbody></table>\n"
    inner=re.findall(r"<tr[^>]*>[\s\S]*?</tr>",md.split("<tbody>",1)[1].split("</tbody>",1)[0])
    verify(len(inner)==352 and md.count('colspan="16"')==15,"readable table complete")
    for i,tr in enumerate(inner,start=2):
        if i in dividers:verify('colspan="16"' in tr,"divider width")
        else:
            td=re.findall(r"<td>(.*?)</td>",tr,re.S)
            verify(len(td)==16 and [unescape(v) for v in td]==grid[i],
                   "readable source matrix cell row "+str(i+1))
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        (D/name).write_text(md,encoding="utf-8")
    def colref(ref):
        mm=re.fullmatch(r"([A-Z]+)([0-9]+)",ref)
        verify(mm is not None,"Excel A1 ref "+str(ref))
        c=0
        for ch in mm.group(1):c=c*26+ord(ch)-64
        return c,int(mm.group(2))
    def move(ref):
        c,n=colref(ref);return addr(n,c+1 if c>=7 else c)
    def put(row,ref,value,style):
        c=ET.SubElement(row,q("c"),{"r":ref,"t":"inlineStr","s":str(style)})
        t=ET.SubElement(ET.SubElement(c,q("is")),q("t"))
        t.set("{http://www.w3.org/XML/1998/namespace}space","preserve")
        t.text=str(value)
    def sortcells(row):
        cells=row.findall(q("c"))
        for c in cells:row.remove(c)
        for c in sorted(cells,key=lambda x:colref(x.get("r"))[0]):row.append(c)
    def add_summary(z,path):
        root=ET.fromstring(z.read(path));data=root.find(q("sheetData"))
        oldrows=data.findall(q("row"));top=max(int(r.get("r")) for r in oldrows)
        style=(oldrows[-1].find(q("c")).get("s","0") if oldrows[-1].find(q("c")) is not None else "0")
        statements=[
         ("AAS02 source-first G column","Eight original IDTA v3.2.0 RELATED/PARTIAL source-qualified row cells. 337 old information rows, 354×16 exact saved values."),
         ("Preserved prior comparison material","Every original case, donor, OGC and DIM value preserved after shifting old G–O one position; DIM rightmost P."),
         ("Native evidence and grade","42 AAS02 native source IDs, 57 source-to-row relations; eight composite cells UNCOLORED; not a DIM/Profile adoption."),
         ("Source classification","Original 325 exact RGB source-classified fills and 67 uncolored holds retained after shifting to H/I/J."),
         ("Manual M00/M01 and next stop","M00/M01 frozen unchanged; AAS03 requires separate owner Proceed, no model or runtime effect.")
        ]
        for i,(a,b) in enumerate(statements,start=2):
            n=top+i;rr=ET.SubElement(data,q("row"),{"r":str(n),"ht":"44","customHeight":"1"})
            put(rr,"A"+str(n),a,style);put(rr,"B"+str(n),b,style)
        dim=root.find(q("dimension"))
        if dim is not None:dim.set("ref","A1:B"+str(top+len(statements)+1))
        return ET.tostring(root,encoding="utf-8",xml_declaration=True)
    with zipfile.ZipFile(io.BytesIO(original)) as z:
        verify(z.testzip() is None,"original workbook ZIP CRC")
        paths=old.sheetpaths(z)
        verify(len(paths)==26 and set(("Master Crosswalk","DIM Register","Summary","Validation","Legend"))<=set(paths),
               "original 26 workbook sheets")
        orig_hashes={name:digest(z.read(path)) for name,path in paths.items()}
        original_styles=z.read("xl/styles.xml")
        master=ET.fromstring(z.read(paths["Master Crosswalk"]))
        before_cells={c.get("r"):c for c in master.iter(q("c"))}
        def prior_style(ref):
            return before_cells[ref].get("s","0") if ref in before_cells else "0"
        data=master.find(q("sheetData"))
        rows=data.findall(q("row"))
        verify(len(rows)==354,"same original grid rows")
        for n,row in enumerate(rows,start=1):
            verify(int(row.get("r"))==n,"original Excel row sequence")
            for cell in row.findall(q("c")):
                cell.set("r",move(cell.get("r")))
            if n==2:put(row,"G2",m["columns"][6]["name"],prior_style("F2"))
            if n in notes:put(row,"G"+str(n),notes[n],prior_style("O"+str(n)))
            sortcells(row)
        cols=master.find(q("cols"))
        verify(cols is not None and len(cols.findall(q("col")))==15,"old 15 source widths")
        for cc in cols.findall(q("col")):
            for key in ("min","max"):
                x=int(cc.get(key))
                if x>=7:cc.set(key,str(x+1))
        cols.insert(6,ET.Element(q("col"),{"min":"7","max":"7","width":"45","customWidth":"1"}))
        verify(len(cols.findall(q("col")))==16,"new 16 columns")
        merges=master.find(q("mergeCells"))
        verify(merges is not None,"source group/section merges")
        merged=[]
        for el in merges.findall(q("mergeCell")):
            s=el.get("ref")
            if s=="E1:I1":s="E1:J1"
            elif s=="J1:N1":s="K1:O1"
            elif re.fullmatch(r"A\d+:O\d+",s):s=s.replace(":O",":P")
            el.set("ref",s);merged.append(s)
        verify(len(merged)==18 and sum(":P" in s for s in merged)==15,
               "15 original topic dividers expanded")
        # Extend the original source evidence register without replacing any
        # earlier cell or changing the 26 original sheet names.
        reg=ET.fromstring(z.read(paths["DIM Register"]))
        regdata=reg.find(q("sheetData"));regrows=regdata.findall(q("row"))
        verify(len(regrows)==338,"original DIM Register 337 rows + header")
        for idx,row in enumerate(regrows,start=1):
            style=(row.find(q("c")).get("s","0") if row.find(q("c")) is not None else "0")
            if idx==1:
                put(row,"Q1","AAS02 Part1 source/relationship identifiers (research-only)",style)
            else:
                rr=rs[idx-2];gridloc=positions[rr["row_id"]]
                if gridloc in mapping:
                    mm=mapping[gridloc]
                    put(row,"Q"+str(idx),"AAS02 "+mm["relation"]+": "+", ".join(mm["source_ids"])+
                        "; verified original source and caveats: "+ledgername+"; NOT adopted DIM/Profile.",style)
        regcols=reg.find(q("cols"))
        if regcols is not None:
            regcols.append(ET.Element(q("col"),{"min":"17","max":"17","width":"50","customWidth":"1"}))
        dim=reg.find(q("dimension"))
        if dim is not None:dim.set("ref","A1:Q338")
        legend=ET.fromstring(z.read(paths["Legend"]))
        ld=legend.find(q("sheetData"));last=max(int(r.get("r")) for r in ld.findall(q("row")))
        for k,(label,value) in enumerate([
          ("New AAS-32 G donor column","Eight source-graded RELATED/PARTIAL composite research cells, intentionally without a source classification fill."),
          ("Shifted F2-5 classifications","Original G/H/I donor colored cells now H/I/J, still 325 exact RGB statuses; 67 mixed native cells still uncolored.")
        ],start=2):
            n=last+k;rr=ET.SubElement(ld,q("row"),{"r":str(n),"ht":"42","customHeight":"1"})
            put(rr,"A"+str(n),label,prior_style("O5"))
            put(rr,"B"+str(n),value,prior_style("O5"))
        ldim=legend.find(q("dimension"))
        if ldim is not None:ldim.set("ref","A1:Q"+str(last+3))
        replacements={paths["Master Crosswalk"]:ET.tostring(master,encoding="utf-8",xml_declaration=True),
           paths["DIM Register"]:ET.tostring(reg,encoding="utf-8",xml_declaration=True),
           paths["Summary"]:add_summary(z,paths["Summary"]),
           paths["Validation"]:add_summary(z,paths["Validation"]),
           paths["Legend"]:ET.tostring(legend,encoding="utf-8",xml_declaration=True)}
        original_other={name:sha for name,sha in orig_hashes.items() if paths[name] not in replacements}
        verify(len(original_other)==21,"21 original historical/case/source sheets")
        bout=io.BytesIO()
        with zipfile.ZipFile(bout,"w") as dest:
            for info in z.infolist():
                dest.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    newbytes=bout.getvalue()
    with zipfile.ZipFile(io.BytesIO(newbytes)) as z:
        verify(z.testzip() is None and list(old.sheetpaths(z))==list(paths),"reopened original 26 sheets ZIP CRC")
        verify(z.read("xl/styles.xml")==original_styles,"all original Excel style definitions byte-identical")
        for name,sha in original_other.items():
            verify(digest(z.read(paths[name]))==sha,"untouched historical sheet "+name)
        for file in z.namelist():
            if file.endswith((".xml",".rels")):ET.fromstring(z.read(file))
        outmaster=ET.fromstring(z.read(paths["Master Crosswalk"]))
        after_cells={c.get("r"):c for c in outmaster.iter(q("c"))}
        for ref,cell in before_cells.items():
            expected=move(ref);outcell=after_cells.get(expected)
            verify(outcell is not None and outcell.get("s","0")==cell.get("s","0")
                   and "".join(outcell.itertext())=="".join(cell.itertext()),
                   "all old cell values/styles shift exact "+ref+"→"+expected)
        styles=ET.fromstring(original_styles)
        fills=styles.find(q("fills"));xfs=styles.find(q("cellXfs"))
        colored_styles=set()
        for item in colors["color_assignments"]:
            col={"G":7,"H":8,"I":9}[item["column"]]
            ref=move(addr(positions[item["row_id"]],col))
            cell=after_cells[ref];sid=int(cell.get("s","0"))
            colored_styles.add(sid)
            fill=fills[int(xfs[sid].get("fillId"))]
            fg=fill.find(".//"+q("fgColor"))
            verify(fg is not None and fg.get("rgb")=="FF"+colors["legend"][item["status"]][1:].upper(),
                   "original exact RGB status "+ref)
        verify(len(colors["color_assignments"])==325,"325 original color cells")
        for item in colors["composite_holds"]:
            ref=move(addr(positions[item["row_id"]],{"G":7,"H":8,"I":9}[item["column"]]))
            c=after_cells.get(ref)
            verify(c is None or int(c.get("s","0")) not in colored_styles,"old uncolored mixed-source hold "+ref)
        for n in notes:
            verify("G"+str(n) in after_cells and int(after_cells["G"+str(n)].get("s","0")) not in colored_styles,
                   "new AAS source cell not falsely colored")
    # Exhaustive saved-file/canonical comparison, including blanks.
    actual=old.readcells(newbytes,"Master Crosswalk")
    for i,row in enumerate(grid,start=1):
        for cc,value in enumerate(row,start=1):
            verify(actual.get(addr(i,cc),"")==old.val(value),
                   "saved Excel / JSON / CSV / both Markdown cell "+addr(i,cc))
    for name in ("DIM Register","Summary","Validation","Legend"):
        oldv=old.readcells(original,name);newv=old.readcells(newbytes,name)
        for ref,value in oldv.items():
            verify(newv.get(ref,"")==value,"original "+name+" cell preserved "+ref)
    verify(sum(1 for ref in old.readcells(newbytes,"DIM Register") if re.fullmatch(r"A[0-9]+",ref))==338,
           "original 337 source rows in DIM Register")
    verify(digest(m00)=="724a2488de876d1ad535650f2c60aa3cd8206f641596f681e4a82a4dfd970f70"
           and digest(m01)==prevhash,"owner-protected M00/M01 unchanged")
    (D/BOOK).write_bytes(newbytes)
    sha=digest(newbytes)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="AAS02_G_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED"
    m["counts"]["columns"]=16
    m["counts"]["donorColumns"]=int(m["counts"]["donorColumns"])+1
    m["publicationPolicy"]="AAS02 approved column G, eight bounded source-graded research cells; 354x16 exact same original 26-sheet Excel, 325 old colored styles, 67 held mixed cells, 21 untouched historical sheet XML; M00/M01 original protected. NO DIM/Profile adoption."
    m["nextOwnerAction"]="AAS02 G integrated and saved/verified; STOP before AAS03. A fresh owner Proceed may authorize AAS03 source-first Part1 submodel semantics only."
    m["workbookSnapshot"].update({"checkpoint":"AAS02_G_SAME_26_SHEET_SAVED_PARITY",
      "sha256":sha,"columns":16,"information_rows":337,"currently_matches_readable_view":True,
      "lag":"ZERO: all 354x16=5664 saved comparison cells and both mirrors equal canonical JSON",
      "textCheckpoint":"AAS02_G_SOURCE_QUALIFIED_COMPARISON", "textInformationRows":337,
      "validation_file":validationname,"new_AAS_column_G":"SOURCE_QUALIFIED_PUBLISHED",
      "new_AAS_source_cells":8,"original_325_RGB_cells_preserved_shifted":True,
      "original_67_mixed_cells_held_uncolored":True,"M00_M01_frozen_preserved":True})
    m["AAS02_G_column_publication"]={
      "status":"SAME_26_SHEET_XLSX_SOURCE_AND_5664_SAVED_VALUE_PARITY_PASS",
      "date":"2026-11-13","column":"G","publisher":"IDTA-01001 v3.2.0, July 2026",
      "source_ledger":ledgername,"original_native_items":42,"research_links":57,
      "populated_cells":8,"source_row_ids":[id_to_row[n]["row_id"] for n in sorted(notes)],
      "old_GHI_colored_cells_now_HIJ":True,
      "old_colored_cells":325,"held_old_mixed_cells":67,
      "new_AAS_cell_color_classifications":0,"new_saved_cell_count":5664,
      "xlsx_sha256":sha,"all_26_sheets_preserved":True,
      "original_historical_sheets_byte_same":21,"M00_M01_preserved":True,
      "DIM_Profile_adopted":False,"runtime_conformance_tested":False}
    approval["status"]="OWNER_APPROVED_AND_EXECUTED__AAS02_G_SAVED_PARITY_VERIFIED"
    approval["actual_workbook_sha256"]=sha
    a["donor_column_added"]=True;a["master_cells_changed"]=8
    a["source_to_master_status"]="EIGHT_SOURCE_QUALIFIED_RELATED_OR_PARTIAL_AAS02_G_CELLS__NOT_DIM_ADOPTED"
    a["next_owner_action"]="Only new separate Proceed begins AAS03 original Part1 Submodel and elements semantic audit; STOP before AAS04 or model adoption."
    save(ledgername,led);save(MASTER,m)
    save(validationname,{
       "date":"2026-11-13","step":"AAS02_G_SOURCE_QUALIFIED_COLUMN_INTEGRATION",
       "result":"ONE_JSON_TWO_CSV_TWO_MARKDOWN_SAME_26_SHEET_XLSX_PARITY_PASS",
       "old_living_workbook_sha256":prevhash,"new_living_workbook_sha256":sha,
       "old_grid":"354x15","new_grid":"354x16","verified_saved_cells":5664,
       "original_337_information_row_ids_preserved":True,
       "original_26_sheets":list(paths),
       "21_byte_identical_original_historical_sheets":original_other,
       "original_325_colored_donor_cells_exact_RGB":True,
       "original_67_mixed_source_holds_uncolored":True,
       "new_AAS_G_source_qualified_uncolored_cells":8,
       "native_source_items":42,"source_to_existing_row_links":57,
       "manual_M00_sha256":digest(m00),"manual_M01_sha256":digest(m01),
       "checks":{"both_CSV_mirrors_equal_JSON":True,"both_readable_Markdown_views_equal_JSON":True,
                 "saved_5664_grid_cells_exact":True,"all_prior_5310_cell_text_and_style_equal_at_shifted_addresses":True,
                 "all_original_RGB_source_cell_fills_exact":True,"original_styles_XML_byte_unchanged":True,
                 "21_historical_source_case_sheets_XML_byte_unchanged":True,
                 "all_original_26_sheets_in_order":True,"ZIP_CRC_and_all_XML_parse":True,
                 "DIM_Register_old_saved_values_preserved_and_AAS_evidence_added":True,
                 "M00_and_M01_immutable_protected":True,"no_AAS03_semantic_research":True,
                 "no_DIM_or_Profile_adoption":True,"no_runtime_conformance":True},
       "next":"STOP; separate owner Proceed for AAS03 source review only."})
    verify(digest((D/BOOK).read_bytes())==sha,"written original living workbook readback")
    print("AAS02-G PASS: original 26-sheet XLSX, 354x16=5664 verified saved values, eight source-qualified G cells.")
    print("AAS02-G PASS: all 325 original RGB colors and 67 mixed holds survive; 21 historical sheet XML byte-identical; frozen M00/M01 untouched.")
    return sha



def publish_aas_qualified(step_code,previous_step):
    """Publish a single owner-authorized AAS original-source increment in the SAME original verified 26-sheet workbook."""
    from html import escape
    from html.parser import HTMLParser
    from subprocess import check_output
    fn="AAS01_Original_Source_Corpus_Coverage_13NOV2026.json"
    led=load(fn);step=led[step_code];m=load(MASTER)
    def check(ok,why):
        if not ok:raise AssertionError(step_code+": "+why)
    check(step["status"] in ("SCHEMA_SOURCE_READ__PUBLISHER_PENDING","SOURCE_FIRST_PART2_SELECTED_INTERFACES_COMPLETE__SAVED_PUBLICATION_PENDING","PINNED_PART2_SELECTED_SOURCE_REVIEW_COMPLETE__SAVED_PUBLICATION_PENDING","PINNED_COMPANION_SOURCE_REVIEW_COMPLETE__SAVED_PUBLICATION_PENDING","PINNED_TEMPLATE_SOURCE_REVIEW_COMPLETE__SAVED_PUBLICATION_PENDING"),"source-stage gate")
    check(m["currentEvidenceCheckpoint"]==previous_step+"_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED","prior original canonical step baseline only")
    check(len(step["preflight_head"])==40 and all(x in "0123456789abcdef" for x in step["preflight_head"]),"pinned preflight branch HEAD")
    check(len(step["original_items"])==step["counts"]["native_findings"] and len(step["comparison_updates"])==step["counts"]["master_cells_changed"] and len(step["source_to_master_changes"])==0,"source/target counts")
    check(len(m["rows"])==337 and len(m["review_grid"])==354 and len(m["columns"])==16 and len(m["review_sections"])==15,"current canonical dimensions")
    check([x["key"] for x in m["columns"][:7]]==["Dragino","AirGradient","Campbell","Bennett","IEEE","OPC","AAS32"]
          and m["columns"][-1]["key"]=="DIM","approved case/donor/OGC/DIM placement")
    prev=(D/BOOK).read_bytes()
    check(digest(prev)==m["currentWorkbookSha256"]==m["workbookSnapshot"]["sha256"],"current original workbook hash")
    oldmaster=json.loads(check_output(["git","show",step["preflight_head"]+":Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/"+MASTER]))
    check(oldmaster["review_grid"]==m["review_grid"] and oldmaster["columns"]==m["columns"],"preflight exact source matrix")
    original=[x[:] for x in m["review_grid"]]
    sec=set(m["review_sections"]);indexes={};n=0
    for k in range(2,len(original)):
        if k not in sec:
            indexes[m["rows"][n]["row_id"]]=(k,n)
            n+=1
    check(n==337 and len(indexes)==337,"preserved 337 original stable rows")
    ids={x["source_id"] for x in step["original_items"]}
    changes=[]
    for c in step["comparison_updates"]:
        name=c["row_id"]
        check(name in indexes and c["source_ids"] and set(c["source_ids"])<=ids,"source IDs for "+name)
        k,ri=indexes[name];row=m["rows"][ri];before=row["display"][6]
        check(before==m["review_grid"][k][6] and (step_code+":") not in before,"existing AAS evidence or unassessed source cell "+name)
        after=(before+"\n" if before else "")+step_code+": "+c["relation"]+" — "+c["clarification"]+" ["+", ".join(c["source_ids"])+"]"
        check(len(after)<32767,"Excel length "+name)
        row["display"][6]=m["review_grid"][k][6]=after
        row[step_code+"_source_correspondence"]={"source_ids":c["source_ids"],"relation":c["relation"],
           "source_standing":"PINNED_ORIGINAL_SOURCE_SPECIFIC_REVIEW","DIM_Profile_adopted":False,
           "not_source_completeness_or_runtime":True}
        changes.append({"row_id":name,"cell":"G"+str(k+1),"relation":c["relation"],
                        "source_ids":c["source_ids"],"before":before,"after":after})
    check(len(changes)==step["counts"]["master_cells_changed"] and len({x["cell"] for x in changes})==len(changes) and sum(not x["before"] for x in changes)==step["counts"]["new_AAS_cells"],"source-qualified existing G cell changes and newly assessed cells")
    by_cell={x["cell"]:x for x in changes}
    for i,(before,after) in enumerate(zip(original,m["review_grid"]),1):
        for j,(v0,v1) in enumerate(zip(before,after)):
            addr=chr(65+j)+str(i)
            if addr in by_cell:check(v0==by_cell[addr]["before"] and v1==by_cell[addr]["after"],"qualified edit "+addr)
            else:check(v0==v1,"all original other donor/case/DIM source cells "+addr)
    check([x for i,x in enumerate(m["review_grid"]) if i>1 and i not in sec]==[x["display"] for x in m["rows"]],"row/grid parity")
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/name).open("w",encoding="utf-8",newline="") as f:
            csv.writer(f,lineterminator="\n").writerows(m["review_grid"])
        check(source_csv(name)==m["review_grid"],"CSV source grid "+name)
    oldmd=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    check(oldmd==(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
          and oldmd.count("<table>")==1 and "<tbody>" in oldmd,"historical readable mirrors")
    # Correct only the proven AAS07 banner error; earlier historical banners remain historical.
    if previous_step=="AAS07":
        header,rest=oldmd.split("\n---\n",1)
        check(header.startswith("# CURRENT — AAS07"),"known AAS07 banner")
        oldmd=header.replace("ONE NEXT separate owner Proceed = AAS06 only", "ONE NEXT separate owner Proceed = AAS08 only")+"\n---\n"+rest
    next_step="AAS"+str(int(step_code[3:])+1).zfill(2)
    check(step.get("next_step",next_step)==next_step,"bounded sequential next step")
    intro=("# CURRENT — "+step_code+" original-source comparison and same 26-sheet workbook VERIFIED (14 November 2026)\n\n"+
       step.get("publication_intro",step_code+" selected original source research.")+" "+
       "SAME original 337-row, 354×16, 26-sheet workbook; both CSV and Markdown mirrors; M00/M01 and source colors preserved. "+
       "[Original source report]("+step["report"]+") · [Cumulative source ledger and saved verification]("+fn+"). "+
       "AAS remains ACTIVE/incomplete, no DIM/Profile adoption. ONE NEXT separate owner Proceed = "+next_step+" only; STOP.\n\n---\n\n")
    body=[]
    for i in range(2,len(m["review_grid"])):
        row=m["review_grid"][i]
        if i in sec:body.append('<tr><th colspan="16">'+escape(str(row[0]))+'</th></tr>')
        else:body.append("<tr>"+"".join("<td>"+escape(str(x))+"</td>" for x in row)+"</tr>")
    md=intro+oldmd.split("<tbody>",1)[0]+"<tbody>\n"+"\n".join(body)+"\n</tbody></table>\n"
    check(len(body)==352 and md.count('colspan="16"')==15,"comparison topic rows")
    class Reader(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.row=None;self.v=None;self.span=1
        def handle_starttag(self,tag,attrs):
            if tag=="tr":self.row=[]
            elif tag in ("td","th"):self.v="";self.span=int(dict(attrs).get("colspan",1))
        def handle_data(self,data):
            if self.v is not None:self.v+=data
        def handle_endtag(self,tag):
            if tag in ("td","th") and self.v is not None:self.row.extend([self.v]+[""]*(self.span-1));self.v=None
            elif tag=="tr":self.rows.append(self.row);self.row=None
    pr=Reader();pr.feed(md[md.index("<table>"):md.index("</table>")+8])
    check(pr.rows[1:]==m["review_grid"][1:],"GitHub-readable table exact independent parsed cells")
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        (D/name).write_text(md,encoding="utf-8")
    def readcell(c):
        return "" if c is None else "".join(t.text or "" for t in c.iter(q("t")))
    def setcell(c,v):
        for e in list(c):c.remove(e)
        c.set("t","inlineStr")
        t=ET.SubElement(ET.SubElement(c,q("is")),q("t"))
        t.set("{http://www.w3.org/XML/1998/namespace}space","preserve");t.text=str(v)
    presentation_fixes=[]
    improve_wrap=step.get("presentation_correction")=="WRAP_AFFECTED_UNFORMATTED_AAS_CELLS_AND_EXPAND_ROWS"
    def wrap_cell(cell,sheet):
        if improve_wrap and cell.get("s","0")=="0":
            presentation_fixes.append({"sheet":sheet,"cell":cell.get("r"),"before":"0","after":"526"})
            cell.set("s","526")  # Existing white, unclassified, wrapped body style; no new classification.
    def append_note(z,path,label,message):
        root=ET.fromstring(z.read(path));data=root.find(q("sheetData"))
        rows=data.findall(q("row"));num=max(int(x.get("r")) for x in rows)+1
        s=(rows[-1].find(q("c")).get("s","0") if rows[-1].find(q("c")) is not None else "0")
        nr=ET.SubElement(data,q("row"),{"r":str(num),"ht":"110" if improve_wrap else "58","customHeight":"1"})
        for col,v in (("A",label),("B",message)):
            cell=ET.SubElement(nr,q("c"),{"r":col+str(num),"s":s})
            setcell(cell,v)
        dim=root.find(q("dimension"))
        if dim is not None:
            last=dim.get("ref","A1:B1").split(":")[-1]
            dim.set("ref",dim.get("ref","A1:B1").split(":")[0]+":"+re.sub(r"\d+$",str(num),last))
        return ET.tostring(root,encoding="utf-8",xml_declaration=True)
    with zipfile.ZipFile(io.BytesIO(prev)) as z:
        check(z.testzip() is None,"input original ZIP integrity")
        paths=old.sheetpaths(z);check(len(paths)==26,"same original 26 worksheets")
        historical_hashes={name:digest(z.read(path)) for name,path in paths.items()}
        orig_style=z.read("xl/styles.xml")
        master=ET.fromstring(z.read(paths["Master Crosswalk"]))
        rows=master.find(q("sheetData")).findall(q("row"))
        check(len(rows)==354,"saved 354 original master rows")
        cells={c.get("r"):c for c in master.iter(q("c"))}
        for c in changes:
            addr=c["cell"];cell=cells.get(addr)
            rr=rows[int(addr[1:])-1]
            if cell is None:
                check(c["before"]=="","new source comparison begins empty "+addr)
                cell=ET.Element(q("c"),{"r":addr,"s":"0"})
                elements=rr.findall(q("c"))
                insert_at=next((j for j,x in enumerate(elements) if x.get("r","").startswith(tuple("HIJKLMNOP"))),len(elements))
                rr.insert(insert_at,cell)
            check(readcell(cell)==c["before"],"actual prior saved cell "+addr)
            setcell(cell,c["after"])
            wrap_cell(cell,"Master Crosswalk")
            rr=rows[int(addr[1:])-1]
            height=min(252,max(float(rr.get("ht","30")),90+len(c["after"])//8))
            if improve_wrap:height=min(409.5,max(height,90+len(c["after"])//4))
            rr.set("ht",str(height));rr.set("customHeight","1")
        register=ET.fromstring(z.read(paths["DIM Register"]))
        regrows=register.find(q("sheetData")).findall(q("row"))
        check(len(regrows)==338,"same original DIM Register")
        for c in changes:
            _,idx=indexes[c["row_id"]];rr=regrows[idx+1];addr="Q"+str(idx+2)
            oldcell=next((x for x in rr.findall(q("c")) if x.get("r")==addr),None)
            if oldcell is None:
                oldcell=ET.SubElement(rr,q("c"),{"r":addr,"s":"0"})
            oldtext=readcell(oldcell)
            setcell(oldcell,oldtext+"\n"+step_code+": "+", ".join(c["source_ids"])+"; pinned original evidence, no DIM/Profile adoption.")
            wrap_cell(oldcell,"DIM Register")
            rr.set("ht",str(min(252,max(float(rr.get("ht","30")),95+len(readcell(oldcell))//10))))
            rr.set("customHeight","1")
            if improve_wrap:rr.set("ht",str(min(409.5,max(float(rr.get("ht")),90+len(readcell(oldcell))//4))))
        note=step_code+" bounded original-source research — no DIM/Profile adoption"
        context=step.get("publication_note",step_code+" exact original evidence; bounded donor cells and holds; no runtime/service conformance.")
        replaced={
          paths["Master Crosswalk"]:ET.tostring(master,encoding="utf-8",xml_declaration=True),
          paths["DIM Register"]:ET.tostring(register,encoding="utf-8",xml_declaration=True),
          paths["Summary"]:append_note(z,paths["Summary"],note,context),
          paths["Validation"]:append_note(z,paths["Validation"],note,"All 5,664 master values, 26 sheets, 21 historical sheet XML parts, original colors/styles and M00/M01 independently checked."),
          paths["Legend"]:append_note(z,paths["Legend"],note,"Original 325 graded donor cells remain colored; "+step_code+" source-qualified uncolored G cells; 67 prior mixed holds still uncolored.")
        }
        check(len(replaced)==5 and len([x for x in paths.values() if x not in replaced])==21,"five refreshed tabs and 21 preserved")
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as dst:
            for info in z.infolist():dst.writestr(info,replaced.get(info.filename,z.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(prev)) as before,zipfile.ZipFile(io.BytesIO(saved)) as after:
        check(after.testzip() is None and list(old.sheetpaths(after))==list(paths),"reopened saved file/26 original sheets")
        check(after.read("xl/styles.xml")==orig_style,"original RGB styles stylesheet identical")
        for item in before.infolist():
            if item.filename not in replaced:check(after.read(item.filename)==before.read(item.filename),"all unrelated package entries identical "+item.filename)
        for path in after.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(after.read(path))
        sheet=ET.fromstring(after.read(paths["Master Crosswalk"]))
        cells={c.get("r"):c for c in sheet.iter(q("c"))}
        originalCells={c.get("r"):c for c in ET.fromstring(before.read(paths["Master Crosswalk"])).iter(q("c"))}
        for i,row in enumerate(m["review_grid"],1):
            for j,v in enumerate(row):
                addr=chr(65+j)+str(i)
                check(readcell(cells.get(addr))==v,"saved XML to source 5,664 values "+addr)
        for addr,c in originalCells.items():
            fixed=any(x["sheet"]=="Master Crosswalk" and x["cell"]==addr for x in presentation_fixes)
            check((fixed and addr in by_cell and c.get("s","0")=="0" and cells[addr].get("s")=="526") or cells[addr].get("s","0")==c.get("s","0"),"original cell classification style or recorded unclassified wrap fix "+addr)
        check(len(m["F2_5_color_reconciliation"]["color_assignments"])==325
              and len(m["F2_5_color_reconciliation"]["composite_holds"])==67,"original 325 colors and 67 held statuses")
    sha=digest(saved)
    (D/BOOK).write_bytes(saved)
    check(digest((D/BOOK).read_bytes())==sha,"saved original living workbook readback")
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]=step_code+"_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":step_code+"_SAVED_PARITY","sha256":sha,"information_rows":337,
       "currently_matches_readable_view":True,"lag":"ZERO: 354x16 JSON/both CSV/both Markdown/saved workbook",
       "textCheckpoint":step_code+"_SELECTED_ORIGINAL_SOURCE_CROSSWALK",step_code+"_affected_row_ids":[c["row_id"] for c in changes]})
    m[step_code+"_affected_row_ids"]=[c["row_id"] for c in changes]
    m["nextOwnerAction"]=step["next"]
    m["publicationPolicy"]=step["publication_note"]+" Same original workbook; no DIM/Profile adoption."
    m.setdefault("AASEvidence",{}).update({"report":step["report"],step_code+"_counts":step["counts"],
       "current_source_pins":step.get("source_pins",[]),
       "source_pin_scope":"Historical Part1 pin; current increment pins are listed separately in current_source_pins.",
       "donor_status":"ACTIVE_INCOMPLETE","DIM_Profile_adopted":False})
    m["workbookSnapshot"].update({"validation_file":fn+"#/"+step_code+"/saved_verification",
       "refreshed_cell_count":len(changes)})
    step["source_to_master_changes"]=changes
    step["status"]="COMPLETE_AT_SELECTED_PINNED_ORIGINAL_SOURCE_SCOPE__DONOR_ACTIVE_INCOMPLETE"
    led["status"]=step_code+"_BOUNDED_INCREMENT_COMPLETE__AAS_ACTIVE_INCOMPLETE"
    led["one_next"]=step["next"]
    led["master_state_current"]={"checkpoint":step_code,"rows":337,"grid":"354x16","AAS_column":"G","same_workbook":True,
                                 "manual_M00_M01":"UNCHANGED","M02":"NOT_CREATED","next":step["next"]}
    m00=D/"Manual_Workbook_Versions/M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx"
    m01=D/"Manual_Workbook_Versions/M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx"
    step["saved_verification"]={
       "status":"PASS_LOCAL_REOPENED_SAVED_FILE","preflight_head":step["preflight_head"],
       "previous_xlsx_sha256":digest(prev),"xlsx_sha256":sha,"saved_cells":5664,
       "sheet_names":list(paths),"changed_AAS_cells":[c["cell"] for c in changes],
       "new_AAS_cells":step["counts"]["new_AAS_cells"],"total_AAS_cells":step["counts"]["total_AAS_cells"],
       "historical_21_sheet_sha256":{name:hashcode for name,hashcode in historical_hashes.items() if paths[name] not in replaced},
       "styles_xml_sha256":digest(orig_style),
       "presentation_corrections":presentation_fixes,
       "manual_version_sha256":{m00.name:digest(m00.read_bytes()),m01.name:digest(m01.read_bytes())},
       "checks":{"saved_grid_equals_JSON":True,"both_CSV_equal_JSON":True,"both_Markdown_equal_JSON":True,
                 "all_other_donor_case_DIM_values_unchanged":True,"row_ids_order_and_topic_dividers_preserved":True,
                 "all_original_cell_styles_preserved":not presentation_fixes,"325_classification_colors_and_67_mixed_holds_retained":True,
                 "only_listed_unclassified_AAS_wrap_styles_corrected":bool(presentation_fixes),
                 "AAS_cells_without_classification_fill":True,"all_26_sheets_in_order":True,
                 "21_unaffected_sheet_XML_byte_identical":True,"all_unedited_package_entries_byte_identical":True,
                 "M00_M01_unchanged_no_M02":True,"all_changed_summary_legend_register_values_reopened":True,
                 "ZIP_CRC_and_XML_parse":True},
       "visual_review":{"status":"REOPENED_XML_AND_ROW_HEIGHT_INSPECTED_NOT_PIXEL_RENDERED",
           "note":"No separate rendered screenshot or visual claim; affected rows expanded with original styles retained."},
       "research_limit":"Source item/file coverage is selected-scope; no runtime, complete specification or DIM/Profile adoption."
    }
    save(MASTER,m);save(fn,led)
    verify_aas_saved(step_code)
    print(step_code+" PASS: "+str(len(changes))+" qualified G cells, "+str(step["counts"]["new_AAS_cells"])+" newly assessed; 5,664 reopened saved values and both CSV/Markdown mirrors.")
    print(step_code+" PASS: same original 26-sheet workbook, 21 historical sheets, original colors and M00/M01 preserved; STOP.")



def publish_aas05():
    return publish_aas_qualified("AAS05","AAS04")

def publish_aas06():
    return publish_aas_qualified("AAS06","AAS05")

def publish_aas07():
    return publish_aas_qualified("AAS07","AAS06")

def publish_aas08():
    return publish_aas_qualified("AAS08","AAS07")

def publish_aas09():
    return publish_aas_qualified("AAS09","AAS08")

def verify_aas_saved(step="AAS03"):
    """Read-only verification of the already authored AAS workbook checkpoint.

    Reuses this publisher's preservation gate; never rebuilds or advances research.
    The source ledger distinguishes original review from format verification.
    """
    from subprocess import check_output
    from html.parser import HTMLParser
    m=load(MASTER)
    ledger=load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json")
    a=ledger[step]; proof=a["saved_verification"]; counts=a["counts"]
    def need(ok,why):
        if not ok:raise AssertionError(step+" saved checkpoint: "+why)
    if step=="AAS09":
        need(m["nextOwnerAction"]==ledger.get("one_next",a["next"]) and m["AASEvidence"]["report"]==a["report"]
             and m["workbookSnapshot"]["validation_file"].endswith("#/AAS09/saved_verification"),
             "current recovery metadata agrees with saved checkpoint")
    prefix="Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/"
    baseline=json.loads(check_output(["git","show",a["preflight_head"]+":"+prefix+MASTER]))
    oldbytes=check_output(["git","show",a["preflight_head"]+":"+prefix+BOOK])
    saved=(D/BOOK).read_bytes()
    need(digest(saved)==proof["xlsx_sha256"]==m["currentWorkbookSha256"]==m["workbookSnapshot"]["sha256"],"saved hash and current metadata")
    need(digest(oldbytes)==proof["previous_xlsx_sha256"],"actual preflight workbook")
    need(len(m["rows"])==337 and len(m["review_grid"])==354 and all(len(x)==16 for x in m["review_grid"]),"approved dimensions")
    need([r["row_id"] for r in m["rows"]]==[r["row_id"] for r in baseline["rows"]],"stable row IDs/order")
    need(m["columns"]==baseline["columns"] and m["review_sections"]==baseline["review_sections"],"column order and topic dividers")
    for key in ("caseEvidence","originalDonorEvidence","priorHolds","adoptionPolicy","F2_5_color_reconciliation","manualWorkbookMilestones"):
        need(m[key]==baseline[key],"preserved source/owner record "+key)
    changes={x["cell"]:x for x in a["source_to_master_changes"]}
    need(len(changes)==counts["master_cells_changed"] and sum(not x["before"] for x in changes.values())==counts["new_AAS_cells"],"qualified increment counts")
    need(sum(bool(r["display"][6]) for r in m["rows"])==counts["total_AAS_cells"],"populated AAS count")
    for i,(prior,current) in enumerate(zip(baseline["review_grid"],m["review_grid"]),1):
        for j,(v0,v1) in enumerate(zip(prior,current)):
            cell=chr(65+j)+str(i)
            if cell in changes:need(v0==changes[cell]["before"] and v1==changes[cell]["after"],"source-qualified changed value "+cell)
            else:need(v0==v1,"unchanged comparison value "+cell)
    need([r for i,r in enumerate(m["review_grid"]) if i>1 and i not in m["review_sections"]]==[r["display"] for r in m["rows"]],"row/grid consistency")
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        need(source_csv(name)==m["review_grid"],"CSV mirror "+name)
    class TableReader(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.row=None;self.value=None;self.span=1
        def handle_starttag(self,tag,attrs):
            if tag=="tr":self.row=[]
            elif tag in ("td","th"):self.value="";self.span=int(dict(attrs).get("colspan",1))
            elif tag=="br" and self.value is not None:self.value+="\n"
        def handle_data(self,data):
            if self.value is not None:self.value+=data
        def handle_endtag(self,tag):
            if tag in ("td","th") and self.value is not None:self.row.extend([self.value]+[""]*(self.span-1));self.value=None
            elif tag=="tr":self.rows.append(self.row);self.row=None
    md=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text()
    need(md==(D/"ISA_Correction_Review_07NOV2026.md").read_text(),"Markdown mirror equality")
    parser=TableReader();parser.feed(md[md.index("<table>"):md.index("</table>")+8])
    need(parser.rows[1:]==m["review_grid"][1:],"readable comparison values")
    ns={"s":"http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    def getpaths(z):
        rel={x.attrib["Id"]:x.attrib["Target"].lstrip("/") for x in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        return {x.attrib["name"]:rel[x.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]] for x in ET.fromstring(z.read("xl/workbook.xml")).findall("s:sheets/s:sheet",ns)}
    def getcells(z,path):return {x.attrib["r"]:x for x in ET.fromstring(z.read(path)).findall(".//s:sheetData/s:row/s:c",ns)}
    def value(x):return "" if x is None else "".join(t.text or "" for t in x.findall(".//s:t",ns))
    with zipfile.ZipFile(io.BytesIO(oldbytes)) as oldz,zipfile.ZipFile(io.BytesIO(saved)) as z:
        need(z.testzip() is None,"ZIP integrity")
        paths=getpaths(z);need(paths==getpaths(oldz) and list(paths)==proof["sheet_names"] and len(paths)==26,"original 26-sheet structure")
        for entry in z.namelist():
            if entry.endswith(".xml"):ET.fromstring(z.read(entry))
        oldcells=getcells(oldz,paths["Master Crosswalk"]);cells=getcells(z,paths["Master Crosswalk"])
        for i,row in enumerate(m["review_grid"],1):
            for j,expected in enumerate(row):need(value(cells.get(chr(65+j)+str(i)))==expected,"reopened cell "+chr(65+j)+str(i))
        fixes={x["cell"]:x for x in proof.get("presentation_corrections",[]) if x["sheet"]=="Master Crosswalk"}
        for addr,cell in oldcells.items():
            if addr in fixes:
                need(addr in changes and cell.get("s","0")==fixes[addr]["before"]=="0" and cells[addr].get("s")==fixes[addr]["after"]=="526","recorded unclassified wrap fix "+addr)
            else:need(cells[addr].attrib.get("s")==cell.attrib.get("s"),"original style "+addr)
        need(z.read("xl/styles.xml")==oldz.read("xl/styles.xml"),"all original style/color definitions")
        st=ET.fromstring(z.read("xl/styles.xml"));fills=st.find("s:fills",ns);xfs=st.find("s:cellXfs",ns)
        classification={v.upper().lstrip("#") for v in m["F2_5_color_reconciliation"]["legend"].values()}
        for addr in changes:
            xf=xfs[int(cells[addr].attrib.get("s","0"))];fill=fills[int(xf.attrib.get("fillId","0"))];rgb=fill.find(".//s:fgColor",ns)
            need(rgb is None or rgb.attrib.get("rgb","")[-6:] not in classification,"AAS classification remains unassigned "+addr)
        changed_parts={paths[n] for n in ("Master Crosswalk","DIM Register","Summary","Validation","Legend")}
        for entry in oldz.namelist():
            if entry not in changed_parts:need(z.read(entry)==oldz.read(entry),"untouched package part "+entry)
        for name,sha in proof["historical_21_sheet_sha256"].items():need(digest(z.read(paths[name]))==sha,"historical evidence sheet "+name)
    for name,sha in proof["manual_version_sha256"].items():need(digest((D/"Manual_Workbook_Versions"/name).read_bytes())==sha,"manual version "+name)
    need(not list((D/"Manual_Workbook_Versions").glob("M02*")),"no automatic M02")
    ids={x["source_id"] for x in a["original_items"]+a["original_constraint_items"]}
    need(len(a["original_items"])==counts["native_findings"] and len(a["original_constraint_items"])==counts["individual_constraint_records"] and len(a["source_attribute_inventory"])==counts["attribute_entries"],"source inventory record counts, not source completeness")
    for ch in changes.values():need(set(ch["source_ids"])<=ids,"resolvable source IDs "+ch["row_id"])
    print(f"{step} PASS: 5,664 reopened cells; both CSV/Markdown mirrors; {counts['master_cells_changed']} qualified edits and {counts['total_AAS_cells']} total AAS cells.")
    print(f"{step} PASS: original 26 sheets, other donor/case/DIM values, style definitions/colors, 21 historical sheets and M00/M01 preserved; any unclassified wrap fixes are listed in saved verification.")
    print(f"{step} remains bounded research; later research, whole-donor coverage, model adoption and runtime conformance are not verified by this check.")



# Owner-authorized AAS10 usability correction, 14 November 2026.
# This is a workbook integration/presentation repair from retained native evidence:
# no additional corpus coverage, new donor, model/Profile adoption or hardware test.
def publish_aas_owner_view_correction():
    import html
    from collections import Counter
    m=load(MASTER)
    led=load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json")
    step=led["AAS10"]
    need(m["currentEvidenceCheckpoint"]=="AAS09_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED",
         "AAS owner correction requires exactly the saved AAS09 comparison snapshot")
    need(step["status"]=="CORRECTION_REQUIRED__OWNER_CLOSEOUT_ON_HOLD",
         "owner usability defects must have been explicitly recorded")
    need(len(m["rows"])==337 and len(m["review_grid"])==354
         and len(m["columns"])==16 and len(m["review_sections"])==15,
         "original source/case/DIM master geometry")
    need(m["columns"][6]["key"]=="AAS32", "owner-approved AAS column G")
    grid=m["review_grid"]
    sections=set(m["review_sections"])
    previous_grid=[list(r) for r in grid]
    previous_rows=[list(r["display"]) for r in m["rows"]]
    assignments={
      "COMMON_CANDIDATE":{4,5,6,7,10,24,25,76,78,79,231,286},
      "SPECIALIZED_CANDIDATE":{11,13,14,15,16,48,68,70,80,81,82,83,84,85,86,
                               198,199,205,214,215,227,232,233,234,235,236,256,277,308,309},
      "NATIVE_ONLY_EVIDENCE":{18,20,180,202,204,213,237},
      "UNRESOLVED_CANDIDATE":{8,69,220,238,239}
    }
    held={27,71,72,87,95,96,196,218,221,251}
    candidate={n:k for k,rr in assignments.items() for n in rr}
    need(sum(len(x) for x in assignments.values())==54 and len(candidate)==54
         and len(held)==10 and not held.intersection(candidate),
         "54 independently scoped candidate cells and ten explicit held cells")
    prior_source_rows=set()
    for i,row in enumerate(previous_grid,1):
        if i>2 and i-1 not in sections and row[6]:
            prior_source_rows.add(i)
    need(len(prior_source_rows)==63 and prior_source_rows|{198}==set(candidate)|held
         and 198 not in prior_source_rows,
         "exact 63 pre-correction AAS source-bearing cells plus omitted G198")
    substitutions={
      80:("while invocation, errors and execution contracts remain Part 2 work.",
          "while selected Part 2 invocation and response structures were subsequently reviewed in AAS07; physical execution remains unverified."),
      95:("request identity, authorization and execution remain unreviewed here.",
          "selected Part 2 invocation interfaces were subsequently reviewed in AAS07, but source-authenticated issuance, authorization and physical execution remain unverified."),
      96:("Part 2 response contracts remain unreviewed.",
          "selected Part 2 status and response structures were subsequently reviewed in AAS07; neither acknowledgement of hardware control nor physical effect is established."),
      238:("Part 2 update behavior is unreviewed.",
           "selected Part 2 update and value-only representations were subsequently reviewed in AAS07; lossless supplied-empty versus omitted-update correspondence is still unestablished.")
    }
    notes={
      8:"Token/certificate trust and physical asset binding are not demonstrated.",
      13:"Native Entity and bill-of-material structures do not prove installed constituents.",
      14:"Modeled links do not prove cables, connections or installations.",
      18:"Discovery and descriptor endpoints are software/service infrastructure only.",
      20:"Descriptor exposure cannot authenticate real reporting equipment.",
      27:"An event definition cannot establish a performed Observation.",
      68:"Experimental event sources/scope lack ISA occurrence-identifier semantics.",
      69:"Original timestamp versus timeStamp encoding disagreement remains unresolved.",
      71:"No native detector snapshot/delta semantics established.",
      72:"Unit/quantity templates do not establish measured uncertainty or an actual value.",
      76:"Declared potential is distinguishable from readiness or command execution.",
      87:"Range encodings and allowed/excluded-value meaning require reconciliation.",
      95:"API invocation is not a verified physically issued control request.",
      96:"API status does not establish physical acknowledgement or effect.",
      180:"AASX package is not a ZIP history of ISA result messages.",
      196:"API asynchronous status is not the component's physical Status report.",
      198:"Required OperationHandle.handleId is asynchronous API correlation, not an ISA request/response ID.",
      199:"Access-rule declaration is not authenticated runtime authorization.",
      202:"Digital API execution state is not verified hardware execution.",
      204:"AAS model/descriptors query is not ISA message-subscription matching.",
      205:"Visibility/access filtering is not a source hierarchy or physical event selector.",
      213:"Published service profiles distinguish software services, not physical roles.",
      215:"Advertised operations do not establish equipment command readiness.",
      218:"Capability role is not the ready/reported state of actual equipment.",
      220:"JWS/model creator claims are not verified publisher/source assertions.",
      221:"AAS event and AASX source links do not establish original event/copy lineage.",
      237:"Serialization profiles are native encodings, not common CSAPI framing.",
      238:"Empty/omitted normal-JSON semantics conflict with direct ISA update substitution.",
      239:"DateTimeUtc examples/schema disagree; device clock synchronization is not shown.",
      251:"AAS administration version is not actual deployed hardware configuration version."
    }
    source_ids=set()
    for n in range(2,10):
        a=led.get("AAS%02d"%n,{})
        for bucket in ("original_items","original_constraint_items"):
            for item in a.get(bucket,[]):
                if isinstance(item,dict) and item.get("source_id"):
                    source_ids.add(item["source_id"])
    old_names=[c["name"] for c in m["columns"]]
    m["columns"][6]["name"]="AAS (IDTA Parts 1–5 and selected templates; bounded partial)"
    grid[1][6]=m["columns"][6]["name"]
    changes=[]
    grades=[]
    case_holds=[]
    blank_status_count=0
    data_idx=0
    for g_index in range(2,len(grid)):
        if g_index in sections:
            continue
        row=m["rows"][data_idx]
        need(row["display"]==previous_rows[data_idx] and row["display"]==previous_grid[g_index],
             "existing row-order/label evidence at "+str(g_index))
        excel_row=g_index+1
        before=row["display"][6]
        if excel_row==198:
            need(not before,"missing OperationHandle comparison was genuinely blank")
            current=("AAS10: RELATED — IDTA-01002 Part 2 v3.2 OperationHandle.handleId "
                     "(cardinality 1) tracks an asynchronous digital-operation invocation "
                     "for later status and result retrieval. It is not ISA Command request "
                     "identity/Response.reference or evidence of physically executed control. "
                     "[AAS07-N010, AAS07-N011, AAS07-N012]; pinned "
                     "interfaces-payload.adoc lines 907–919 and interfaces.adoc lines 579–630.")
        else:
            current=before
        if excel_row in substitutions:
            oldtext,newtext=substitutions[excel_row]
            need(oldtext in current,"expected obsolete Part2 wording still at G"+str(excel_row))
            current=current.replace(oldtext,newtext,1)
        if before or excel_row==198:
            if excel_row in candidate:
                status=candidate[excel_row]
                note=notes.get(excel_row,"Qualified native comparison; prospective information only.")
                current="["+status.replace("_"," ")+"] "+current
                grades.append({"row_id":row["row_id"],"cell":"G"+str(excel_row),
                               "status":status,"note":note})
            else:
                need(excel_row in held,"source-bearing AAS row without reasoned disposition")
                status="MIXED_OR_NO_ESTABLISHED_HOLD"
                note=notes.get(excel_row,"Source-qualified semantic boundary; no single justified fill.")
                current="[HELD — NO SINGLE CLASSIFICATION] "+current
            matched=sorted(set(re.findall(r"\bAAS0[2-9]-[A-Za-z0-9_-]+\b",current)))
            need(bool(matched),"source-bearing cell without original source IDs G"+str(excel_row))
            need(set(matched)<=source_ids,
                 "source-item IDs not in original retained corpus G"+str(excel_row)+": "+str(set(matched)-source_ids))
        else:
            if row["label"].startswith("REVIEW HOLD —"):
                status="CASE_REVIEW_HOLD"
                note="Case-specific source evidence remains held; no AAS instance/absent concept inferred."
                current="CASE REVIEW HOLD — no original AAS instance was established for this case; neither correspondence nor absence is asserted."
                case_holds.append(excel_row)
            else:
                status="NOT_ASSESSED_HERE"
                note="The inspected AAS evidence does not establish this comparison; not a statement that AAS lacks it."
                current="Not assessed here — no AAS comparison established from the reviewed source; not evidence of absence."
            blank_status_count+=1
            matched=[]
        row["display"][6]=current
        row["AAS10_owner_view_status"]={
            "status":status,"current_excel_cell":"G"+str(excel_row),
            "original_source_ids":matched,"explanation":note,
            "candidate_only_not_adopted":True
        }
        grid[g_index][6]=current
        changes.append({"row_id":row["row_id"],"excel_row":excel_row,
                        "cell":"G"+str(excel_row),"before":before,
                        "after":current,"status":status,"source_ids":matched,
                        "note":note})
        data_idx+=1
    need(data_idx==337 and len(changes)==337 and len(case_holds)==9
         and blank_status_count==273 and 198 in {x["excel_row"] for x in changes},
         "337 explicit source/mapping statuses, 9 case holds, 273 formerly unassessed")
    need(sum(bool(row["display"][6]) for row in m["rows"])==337
         and sum(x["status"] in set(candidate.values()) for x in changes)==54,
         "owner-facing all visible statuses with no accidental candidate inflation")
    # Canonical formats first; a later verified workbook save is mandatory.
    for filename in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/filename).open("w",newline="",encoding="utf-8") as f:
            csv.writer(f,lineterminator="\r\n").writerows(grid)
    html_rows=["<table>","<thead><tr>",
               '<th colspan="4">'+html.escape(grid[0][0])+"</th>",
               '<th colspan="6">'+html.escape(grid[0][4])+"</th>",
               '<th colspan="5">'+html.escape(grid[0][10])+"</th>",
               "<th>"+html.escape(grid[0][15])+"</th>",
               "</tr><tr>"+ "".join("<th>"+html.escape(v)+"</th>" for v in grid[1])+"</tr></thead><tbody>"]
    for idx,row in enumerate(grid[2:],2):
        if idx in sections:
            html_rows.append('<tr><th colspan="16">'+html.escape(row[0])+"</th></tr>")
        else:
            html_rows.append("<tr>"+"".join("<td>"+html.escape(v)+"</td>" for v in row)+"</tr>")
    html_rows+=["</tbody></table>"]
    for filename in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        existing=(D/filename).read_text(encoding="utf-8")
        need("<table>" in existing and "</table>" in existing,"existing Markdown table")
        front=existing[:existing.index("<table>")]
        back=existing[existing.index("</table>")+8:]
        banner=("# CURRENT — AAS owner-view correction, 14 November 2026\n\n"
                "All 337 AAS rows now visibly distinguish source comparison, unassessed and case hold. "
                "The 64 source-bearing comparisons include one newly integrated OperationHandle "
                "RELATED correspondence, 54 provisional candidate fills and 10 held composite/no-established "
                "meanings; 273 rows are explicitly unassessed, including nine case holds. "
                "This is a presentation/integration correction using retained source evidence, "
                "NOT additional original-source completeness, accepted DIM or Profile requirements. "
                "The same 26-sheet workbook is separately refreshed and saved-verified; "
                "manual M00/M01 are frozen and no M02 was created.\n\n---\n\n")
        (D/filename).write_text(banner+front+"\n".join(html_rows)+"\n"+back,encoding="utf-8")
    # Use original workbook ZIP/XML publisher mechanics to preserve *exactly*
    # its 26 sheets and 325 previously classified donor cells.
    prior_bytes=(D/BOOK).read_bytes()
    old_m00=(D/"Manual_Workbook_Versions/M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx").read_bytes()
    old_m01=(D/"Manual_Workbook_Versions/M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx").read_bytes()
    palette=m["F2_5_color_reconciliation"]["legend"]
    need(palette=={
      "COMMON_CANDIDATE":"#D9EAF8",
      "SPECIALIZED_CANDIDATE":"#F9E6B8",
      "NATIVE_ONLY_EVIDENCE":"#E5E7EB",
      "UNRESOLVED_CANDIDATE":"#E9DEFA"},"only previous approved classification colors")
    def val(cell):
        if cell is None:return ""
        inline=cell.find(q("is"))
        if inline is not None:return "".join(t.text or "" for t in inline.iter(q("t")))
        v=cell.find(q("v"))
        return "" if v is None else (v.text or "")
    def put(cell,v):
        for child in list(cell):cell.remove(child)
        cell.set("t","inlineStr")
        o=ET.SubElement(cell,q("is"))
        t=ET.SubElement(o,q("t"))
        if v[:1].isspace() or v[-1:].isspace():t.set("{http://www.w3.org/XML/1998/namespace}space","preserve")
        t.text=v
    def cell_at(root,ref,create=False,style=None):
        number=int(re.search(r"\d+",ref).group())
        sd=root.find(q("sheetData"))
        rr=next((x for x in sd.findall(q("row")) if int(x.get("r"))==number),None)
        need(rr is not None,"existing sheet row "+str(number))
        x=next((x for x in rr.findall(q("c")) if x.get("r")==ref),None)
        if x is not None or not create:return x,rr
        x=ET.Element(q("c"),{"r":ref,"s":str(style if style is not None else 526)})
        column=re.match(r"[A-Z]+",ref).group()
        col=0
        for cc in column:col=col*26+ord(cc)-64
        insert=len(rr)
        for j,item in enumerate(list(rr)):
            if item.tag!=q("c"):continue
            n=0
            for cc in re.match(r"[A-Z]+",item.get("r")).group():n=n*26+ord(cc)-64
            if n>col:insert=j;break
        rr.insert(insert,x)
        return x,rr
    with zipfile.ZipFile(io.BytesIO(prior_bytes)) as z:
        need(z.testzip() is None,"original saved workbook ZIP")
        paths=old.sheetpaths(z)
        need(len(paths)==26,"preserve exact original 26 worksheets")
        styles=ET.fromstring(z.read("xl/styles.xml"))
        fills=styles.find(q("fills"));xfs=styles.find(q("cellXfs"))
        need(fills is not None and xfs is not None and len(xfs)>526,
             "source-classification and original wrapped base style intact")
        style_ids={}
        for key,color in palette.items():
            fids=[]
            for fid,fill in enumerate(fills):
                color_node=fill.find(".//"+q("fgColor"))
                if color_node is not None and color_node.get("rgb","").upper()=="FF"+color[1:].upper():
                    fids.append(fid)
            need(len(fids)==1,"exact existing style fill for "+key)
            clone=ET.fromstring(ET.tostring(xfs[526]))
            clone.set("fillId",str(fids[0]))
            clone.set("applyFill","1")
            style_ids[key]=len(xfs)
            xfs.append(clone)
        xfs.set("count",str(len(xfs)))
        modified={"xl/styles.xml":ET.tostring(styles,encoding="utf-8",xml_declaration=True)}
        master=ET.fromstring(z.read(paths["Master Crosswalk"]))
        hdr,_=cell_at(master,"G2")
        need(hdr is not None and val(hdr)==old_names[6],"original AAS scope column label")
        put(hdr,grid[1][6])
        for item in changes:
            c,rr=cell_at(master,item["cell"],create=True)
            need(val(c)==item["before"],"saved original G-cell before correction "+item["cell"])
            put(c,item["after"])
            c.set("s",str(style_ids[item["status"]] if item["status"] in style_ids else 526))
            rr.set("ht",str(min(409.5,max(float(rr.get("ht","55")),
                         80+len(item["after"])//5))))
            rr.set("customHeight","1")
        modified[paths["Master Crosswalk"]]=ET.tostring(master,encoding="utf-8",xml_declaration=True)
        register=ET.fromstring(z.read(paths["DIM Register"]))
        head,_=cell_at(register,"R1",create=True)
        need(not val(head),"previous DIM Register column R vacant")
        put(head,"AAS — current row status, source IDs and color rationale")
        head.set("s","526")
        for row in m["rows"]:
            data=m["rows"].index(row)+2
            rec=row["AAS10_owner_view_status"]
            ref="R"+str(data)
            c,rr=cell_at(register,ref,create=True)
            need(not val(c),"new R status should not replace original data "+ref)
            put(c,rec["status"]+" — "+rec["explanation"]
                +( "; "+", ".join(rec["original_source_ids"]) if rec["original_source_ids"] else ""))
            c.set("s","526")
            rr.set("ht",str(min(409.5,max(float(rr.get("ht","55")),
                                         80+len(val(c))//8))))
            rr.set("customHeight","1")
        dim=register.find(q("dimension"))
        if dim is not None:dim.set("ref","A1:R338")
        cols=register.find(q("cols"))
        if cols is not None:
            ET.SubElement(cols,q("col"),{"min":"18","max":"18","width":"65","customWidth":"1"})
        modified[paths["DIM Register"]]=ET.tostring(register,encoding="utf-8",xml_declaration=True)
        summary_updates={
          "A1":"AAS10 OWNER-VIEW CORRECTION — 14 NOVEMBER 2026 — AAS ACTIVE / OWNER REVIEW",
          "B17":"NEXT ONLY: owner checks corrected AAS candidate/status/master usability; no donor closeout or transition.",
          "B19":"64 AAS source-qualified comparison cells (one newly integrated G198); 54 classified candidates, 10 held source cells; 273 visible unassessed statuses including 9 case holds.",
          "B23":"AAS02–AAS09 original source review at BOUNDED PARTIAL depth; AAS10 usability repair performed, no new source-corpus audit."
        }
        for sheet_name in ("Summary","Validation"):
            root=ET.fromstring(z.read(paths[sheet_name]))
            for ref,message in summary_updates.items():
                cell,_=cell_at(root,ref,create=True)
                put(cell,message)
            modified[paths[sheet_name]]=ET.tostring(root,encoding="utf-8",xml_declaration=True)
        legend=ET.fromstring(z.read(paths["Legend"]))
        for ref,message in {
          "A1":"CURRENT AAS CLASSIFICATION AND BLANK-STATUS LEGEND — 14 NOV 2026",
          "B28":"AAS corrected: 64 source-qualified comparisons (54 candidate colors, 10 held); 273 explicitly not-assessed/case-hold entries; source research bounded partial."
        }.items():
            cell,_=cell_at(legend,ref,create=True)
            put(cell,message)
        sd=legend.find(q("sheetData"))
        last=max(int(r.get("r")) for r in sd.findall(q("row")))
        legend_rows=[
          ["AAS10 current classification","54 colored source-qualified candidates; 10 uncolored source holds; 273 unassessed statuses (including 9 case holds)."],
          ["COMMON_CANDIDATE","#D9EAF8 — potential shared Details-view information; original meaning/caveats remain in donor text."],
          ["SPECIALIZED_CANDIDATE","#F9E6B8 — optional AAS/equipment-specific representation; not a universal class."],
          ["NATIVE_ONLY_EVIDENCE","#E5E7EB — source API, service, packaging or encoding behavior; not a physical field."],
          ["UNRESOLVED_CANDIDATE","#E9DEFA — unresolved source/trust/temporal or crosswalk meaning."],
          ["HELD / NO_ESTABLISHED","NO COLOR — source support has no single defensible candidate class or no semantic equivalence."],
          ["Not assessed here","NO COLOR — no reviewed AAS correspondence established; DOES NOT assert source absence."],
          ["Case review hold","NO COLOR — no source-authenticated AAS instance for that specific case; not a negative source finding."],
          ["Owner decision","AAS remains ACTIVE; source coverage bounded PARTIAL; no DIM/Profile rule, model adoption or device conformance."]
        ]
        for j,(label,message) in enumerate(legend_rows,start=last+2):
            rr=ET.SubElement(sd,q("row"),{"r":str(j),"ht":"80","customHeight":"1"})
            for col,txt in (("A",label),("B",message)):
                c=ET.SubElement(rr,q("c"),{"r":col+str(j),"s":"526"})
                put(c,txt)
        dim=legend.find(q("dimension"))
        if dim is not None:dim.set("ref","A1:P"+str(last+len(legend_rows)+1))
        modified[paths["Legend"]]=ET.tostring(legend,encoding="utf-8",xml_declaration=True)
        need(len(modified)==6 and len([p for p in paths.values() if p not in modified])==21,
             "exactly five refreshed original sheets and stylesheet")
        data=io.BytesIO()
        with zipfile.ZipFile(data,"w") as target:
            for info in z.infolist():
                target.writestr(info,modified.get(info.filename,z.read(info.filename)))
    saved=data.getvalue()
    sha=digest(saved)
    (D/BOOK).write_bytes(saved)
    # Independent readback of the persisted workbook contents and style status.
    with zipfile.ZipFile(io.BytesIO(prior_bytes)) as oldz,zipfile.ZipFile(D/BOOK) as newz:
        need(newz.testzip() is None and old.sheetpaths(newz)==paths,
             "reopened 26-sheet Excel ZIP/sheet identity")
        for name in newz.namelist():
            if name.endswith((".xml",".rels")):ET.fromstring(newz.read(name))
            if name not in modified:
                need(newz.read(name)==oldz.read(name),"unrelated archive part unchanged "+name)
        prior_xfs=ET.fromstring(oldz.read("xl/styles.xml")).find(q("cellXfs"))
        now_xfs=ET.fromstring(newz.read("xl/styles.xml")).find(q("cellXfs"))
        need(len(now_xfs)==len(prior_xfs)+4 and
             all(ET.tostring(x)==ET.tostring(y) for x,y in zip(prior_xfs,now_xfs)),
             "all old style references, including 325 donor classifications, preserved")
        actual_master=ET.fromstring(newz.read(paths["Master Crosswalk"]))
        by_ref={c.get("r"):c for c in actual_master.iter(q("c"))}
        for idx,row in enumerate(grid,1):
            for j,want in enumerate(row):
                addr=chr(65+j)+str(idx)
                need(val(by_ref.get(addr))==want,"saved master full 5,664-cell parity "+addr)
        for item in changes:
            c=by_ref[item["cell"]]
            want_style=style_ids.get(item["status"],526)
            need(int(c.get("s","0"))==want_style,
                 "source-graded candidate color or appropriate uncolored hold "+item["cell"])
        for addr,c in {c.get("r"):c for c in ET.fromstring(oldz.read(paths["Master Crosswalk"])).iter(q("c"))}.items():
            if not addr.startswith("G") or addr=="G2":
                need(by_ref[addr].get("s")==c.get("s"),
                     "all non-AAS cells retain original saved fill/style "+addr)
        for sheetname in paths:
            if sheetname not in ("Master Crosswalk","DIM Register","Summary","Validation","Legend"):
                need(newz.read(paths[sheetname])==oldz.read(paths[sheetname]),
                     "21 untouched historical original sheets "+sheetname)
        for sheetname,refs in (("Summary",summary_updates.keys()),("Validation",summary_updates.keys()),
                               ("Legend",("A1","B28"))):
            root=ET.fromstring(newz.read(paths[sheetname]))
            cells={c.get("r"):c for c in root.iter(q("c"))}
            for ref in refs:need(ref in cells and bool(val(cells[ref])),
                                 "current saved workbook guidance "+sheetname+"!"+ref)
    need(digest((D/BOOK).read_bytes())==sha,"saved binary re-read sha")
    for name,raw in (( "M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx",old_m00),
                     ( "M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx",old_m01)):
        need((D/"Manual_Workbook_Versions"/name).read_bytes()==raw,"protected manual frozen "+name)
    need(not list((D/"Manual_Workbook_Versions").glob("M02*")),"no unapproved M02")
    need(source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")==grid
         ==source_csv("ISA_Correction_Review_07NOV2026.csv"),"both CSV mirrors exact")
    from html.parser import HTMLParser
    class Reader(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.row=None;self.tmp=None;self.span=1
        def handle_starttag(self,tag,attrs):
            if tag=="tr":self.row=[]
            elif tag in ("td","th"):self.tmp="";self.span=int(dict(attrs).get("colspan",1))
        def handle_data(self,data):
            if self.tmp is not None:self.tmp+=data
        def handle_endtag(self,tag):
            if tag in ("td","th") and self.tmp is not None:
                self.row.extend([self.tmp]+[""]*(self.span-1));self.tmp=None
            elif tag=="tr":self.rows.append(self.row);self.row=None
    a=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text()
    need(a==(D/"ISA_Correction_Review_07NOV2026.md").read_text(),"both Markdown mirrors exact")
    p=Reader();p.feed(a[a.index("<table>"):a.index("</table>")+8])
    need(p.rows[1:]==grid[1:],"entire GitHub-readable table matches 354x16 source")
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="AAS10_OWNER_VIEW_CORRECTION_SAVED_PARITY"
    m["workbookSnapshot"].update({
       "checkpoint":"AAS10_OWNER_VIEW_CORRECTION_SAVED_PARITY",
       "sha256":sha,"currently_matches_readable_view":True,
       "lag":"ZERO: current JSON, both CSV/Markdown mirrors and same saved XLSX",
       "textCheckpoint":"AAS10_OWNER_VIEW_CORRECTION",
       "validation_file":"AAS01_Original_Source_Corpus_Coverage_13NOV2026.json#/AAS10/owner_usability_correction/saved_verification",
       "source_compared_rows":64,"explicit_unassessed_rows":273,
       "AAS_candidate_colors":54,"AAS_uncolored_source_holds":10
    })
    m["AASEvidence"]["donor_status"]="ACTIVE_CORRECTED_OWNER_REVIEW_PENDING"
    m["AASEvidence"]["owner_usability_correction"]="AAS10 owner-facing rows/statuses/classifications, no source expansion"
    m["AAS10_color_reconciliation"]={
       "date":"2026-11-14","palette":palette,
       "assignments":grades,
       "held":[x for x in changes if x["status"]=="MIXED_OR_NO_ESTABLISHED_HOLD"],
       "status_counts":dict(Counter(x["status"] for x in changes)),
       "source_qualified_rows":64,"unassessed_status_rows":273,
       "source_new_links":1,"DIM_Profile_adopted":False
    }
    next_action=("OWNER REVIEW OF THE CORRECTED AAS SOURCE-QUALIFIED COLUMN AND ITS BOUNDED-PARTIAL "
                 "COVERAGE; NO AUTOMATIC DONOR ACCEPTANCE/TRANSITION OR NEW MODEL/PROFILE/RUNTIME WORK.")
    m["nextOwnerAction"]=next_action
    m["publicationPolicy"]=("AAS10 usability correction using original retained source evidence; "
        "all 337 rows have explicit statuses and candidate/hold classification. "
        "No increase in source coverage, DIM/Profile adoption or runtime conformance.")
    led["status"]="AAS_ACTIVE__OWNER_VIEW_CORRECTED_PENDING_OWNER_REVIEW"
    led["one_next"]=next_action
    led["master_state_current"]={
      "checkpoint":"AAS10_OWNER_VIEW_CORRECTION_SAVED_PARITY",
      "rows":337,"grid":"354x16","AAS_column":"G","same_workbook":True,
      "comparison_lag":0,"manual_M00_M01":"UNCHANGED","M02":"NOT_CREATED",
      "next":next_action,"status":"CORRECTED_PENDING_OWNER_REVIEW"
    }
    step["status"]="OWNER_VIEW_CORRECTED__OWNER_REVIEW_PENDING"
    proof={
      "status":"SAVED_LOCAL_REOPENED_PARITY_PASS","previous_workbook_sha256":digest(prior_bytes),
      "workbook_sha256":sha,"saved_grid_cells":5664,"same_original_sheets":26,
      "previous_colored_donor_cells":325,"new_graded_AAS_cells":54,
      "AAS_uncolored_source_holds":10,"explicit_unassessed_cells":273,
      "case_holds":case_holds,"new_qualified_comparison":"G198",
      "stale_conclusions_corrected":sorted(substitutions),
      "manual_M00_sha256":digest(old_m00),"manual_M01_sha256":digest(old_m01),
      "original_21_unaffected_sheet_sha256":{
          name:digest(opened) for name,opened in
          ((name,zipfile.ZipFile(io.BytesIO(prior_bytes)).read(path))
            for name,path in paths.items() if name not in ("Master Crosswalk","DIM Register","Summary","Validation","Legend"))
      },
      "checks":{
        "all_337_row_statuses_explicit":True,"each_source_cell_candidate_or_held":True,
        "selected_OperationHandle_original_source_already_reviewed":True,
        "four_stale_earlier_unreviewed_claims_reconciled":True,
        "same_5664_saved_comparison_values":True,
        "both_CSV_and_Markdown_mirrors_match":True,
        "original_325_donor_styles_preserved":True,
        "M00_M01_unchanged_no_M02":True,
        "21_original_historical_sheets_unchanged":True,
        "Summary_Legend_and_Register_current":True,
        "ZIP_XML_CRC_reopened":True,
        "source_corpus_comprehensive":False,
        "DIM_Profile_adopted":False
      }
    }
    step["owner_usability_correction"]={
       "date":"2026-11-14","from_pre_correction_commit":"30d694460b38f80bf04daaa4eef0154d21eb53d5",
       "archive_branch":"archive/dim-crosswalk-pre-aas-correction-20261114",
       "rows_changed":len(changes),"qualified_original_comparisons":64,
       "source_qualified_new":1,"provisional_candidate_colors":54,
       "uncolored_source_holds":10,"unassessed_rows":273,
       "source_item_new_inspections":0,
       "row_decisions":changes,
       "saved_verification":proof,
       "status":"CORRECTION_SAVED__OWNER_REVIEW_ONLY",
       "remaining_limitation":"No comprehensive original clause/API/template audit or independent semantic validation of every correspondence; previous AAS10 holds persist.",
       "one_next":next_action
    }
    save(MASTER,m)
    save("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json",led)
    print("AAS OWNER CORRECTION PASS: 64 qualified rows / 54 candidate colors / 10 explicit source holds; 273 clearly unassessed including nine case holds.")
    print("PASS: original 26-sheet editable master, 5,664 saved comparison values, both CSV/Markdown mirrors, old 325 colors and M00/M01 preserved.")
    print("STOP: AAS remains bounded PARTIAL; explicit owner review next, no donor transition or DIM/Profile adoption.")


def verify_aas_owner_view_correction():
    """Independent post-publication source/display/binary gate; does not edit any file."""
    m=load(MASTER)
    led=load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json")
    a=led["AAS10"]["owner_usability_correction"]
    need(m["currentEvidenceCheckpoint"]=="AAS10_OWNER_VIEW_CORRECTION_SAVED_PARITY"
         and a["status"]=="CORRECTION_SAVED__OWNER_REVIEW_ONLY",
         "owner correction actually published")
    need(m["nextOwnerAction"]==led["one_next"]==a["one_next"],"current owner stop")
    need(len(m["rows"])==337 and len(m["review_grid"])==354
         and all(len(row)==16 for row in m["review_grid"]),"original 354x16 grid")
    need(sum(bool(r["display"][6]) for r in m["rows"])==337,"all AAS statuses visible")
    from collections import Counter
    counts=Counter(r["AAS10_owner_view_status"]["status"] for r in m["rows"])
    need(sum(counts[x] for x in m["F2_5_color_reconciliation"]["legend"])==54
         and counts["MIXED_OR_NO_ESTABLISHED_HOLD"]==10
         and counts["NOT_ASSESSED_HERE"]==264
         and counts["CASE_REVIEW_HOLD"]==9,
         "source grade/unassessed/case audit cardinalities")
    need(m["AAS10_color_reconciliation"]["status_counts"]==dict(counts),
         "row-level classification is canonical")
    need(source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")==m["review_grid"]
         ==source_csv("ISA_Correction_Review_07NOV2026.csv"),"CSV mirrors")
    from html.parser import HTMLParser
    class Reader(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.row=None;self.tmp=None;self.span=1
        def handle_starttag(self,tag,attrs):
            if tag=="tr":self.row=[]
            elif tag in ("td","th"):self.tmp="";self.span=int(dict(attrs).get("colspan",1))
        def handle_data(self,data):
            if self.tmp is not None:self.tmp+=data
        def handle_endtag(self,tag):
            if tag in ("td","th") and self.tmp is not None:
                self.row.extend([self.tmp]+[""]*(self.span-1));self.tmp=None
            elif tag=="tr":self.rows.append(self.row);self.row=None
    doc=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text()
    need(doc==(D/"ISA_Correction_Review_07NOV2026.md").read_text(),
         "both human-readable mirror documents")
    parser=Reader();parser.feed(doc[doc.index("<table>"):doc.index("</table>")+8])
    need(parser.rows[1:]==m["review_grid"][1:],"readable full comparison")
    book=(D/BOOK).read_bytes()
    need(digest(book)==m["currentWorkbookSha256"]==m["workbookSnapshot"]["sha256"]
         ==a["saved_verification"]["workbook_sha256"],"current stored workbook sha")
    with zipfile.ZipFile(io.BytesIO(book)) as z:
        need(z.testzip() is None,"saved ZIP CRC")
        paths=old.sheetpaths(z)
        need(len(paths)==26,"same original 26 sheet names")
        for f in z.namelist():
            if f.endswith((".xml",".rels")):ET.fromstring(z.read(f))
        root=ET.fromstring(z.read(paths["Master Crosswalk"]))
        cells={c.get("r"):c for c in root.iter(q("c"))}
        def val(c):
            if c is None:return ""
            t=c.find(q("is"))
            return "".join(x.text or "" for x in t.iter(q("t"))) if t is not None else (c.findtext(q("v")) or "")
        for i,row in enumerate(m["review_grid"],1):
            for j,want in enumerate(row):
                addr=chr(65+j)+str(i)
                need(val(cells.get(addr))==want,"actual saved cell "+addr)
        styles=ET.fromstring(z.read("xl/styles.xml")); xfs=styles.find(q("cellXfs"));fills=styles.find(q("fills"))
        palette=m["F2_5_color_reconciliation"]["legend"]
        decisions={v["cell"]:v["status"] for v in m["AAS10_color_reconciliation"]["assignments"]}
        observed=Counter()
        for r in m["rows"]:
            info=r["AAS10_owner_view_status"];addr=info["current_excel_cell"]
            xf=xfs[int(cells[addr].get("s","0"))]
            fill=fills[int(xf.get("fillId","0"))]
            fg=fill.find(".//"+q("fgColor"))
            code=("#"+fg.get("rgb","")[-6:].upper()) if fg is not None else None
            if addr in decisions:
                need(code==palette[decisions[addr]].upper(),
                     "saved AAS candidate color + source record "+addr)
                observed[decisions[addr]]+=1
            else:
                need(code not in {color.upper() for color in palette.values()},
                     "unassessed or held AAS row must NOT receive a candidate color "+addr)
        need(sum(observed.values())==54,"only 54 source-qualified AAS graded colors")
        for name,sha in a["saved_verification"]["original_21_unaffected_sheet_sha256"].items():
            need(digest(z.read(paths[name]))==sha,"original historical sheet preserved "+name)
        for sheet,refs in (("Summary",("A1","B17","B19","B23")),
                           ("Validation",("A1","B17","B19","B23")),
                           ("Legend",("A1","B28"))):
            x=ET.fromstring(z.read(paths[sheet]))
            cs={c.get("r"):c for c in x.iter(q("c"))}
            need(all(ref in cs and val(cs[ref]) for ref in refs),
                 "current saved summary/legend no stale top-level pointer "+sheet)
    need(not list((D/"Manual_Workbook_Versions").glob("M02*")),"no M02")
    need(digest((D/"Manual_Workbook_Versions/M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx").read_bytes())==a["saved_verification"]["manual_M00_sha256"],"M00 frozen")
    need(digest((D/"Manual_Workbook_Versions/M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx").read_bytes())==a["saved_verification"]["manual_M01_sha256"],"M01 frozen")
    print("AAS owner correction independently verified: 5,664 saved XLSX cells; all 26 sheets; both mirrors; 54 AAS candidate fills; 10 source holds; 273 explicit unassessed.")
    print("LIMIT: preservation/presentation/cited evidence only, not whole-source/semantic completeness or DIM/Profile conformance.")



def publish_donor_visible_order_repair():
    """Owner-requested UI integrity correction only: no source/donor audit.

    Repair invalid Excel worksheet cell ordering and give legacy H/I blanks
    explicit unassessed/hold text. Keep the original workbook and evidence.
    """
    import html
    from collections import Counter
    m=load(MASTER)
    led=load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json")
    need(m["currentEvidenceCheckpoint"]=="AAS10_OWNER_VIEW_CORRECTION_SAVED_PARITY",
         "apply once to known current AAS comparison snapshot only")
    need(len(m["rows"])==337 and len(m["review_grid"])==354
         and len(m["columns"])==16 and len(m["review_sections"])==15,
         "unchanged 337 row / 354x16 approved layout")
    need([c["key"] for c in m["columns"]][6:10]==["AAS32","SAPIENT","ISA","OpenGroupSOSA"],
         "four completed donor columns G:H:I:J in owner-approved order")
    prior=(D/BOOK).read_bytes()
    last_grid=[list(x) for x in m["review_grid"]]
    grid=m["review_grid"]
    sections=set(m["review_sections"])
    row_positions={}
    data_idx=0
    changes=[]
    for idx in range(2,len(grid)):
        if idx in sections:continue
        row=m["rows"][data_idx]
        need(row["display"]==last_grid[idx],
             "stable row-to-grid identity "+row["row_id"])
        excel_row=idx+1
        row_positions[excel_row]=row["row_id"]
        for col_idx,letter,donor in ((7,"H","SAPIENT"),(8,"I","ISA")):
            before=row["display"][col_idx]
            if before:continue
            held=row["label"].startswith("REVIEW HOLD —")
            if held:
                after=("CASE REVIEW HOLD — no "+donor+" case-specific comparison established "
                       "from reviewed source; not evidence of absence.")
                status="CASE_REVIEW_HOLD"
            else:
                after=("Not assessed here — no verified "+donor+" correspondence is recorded "
                       "for this topic; not evidence that the donor lacks it.")
                status="NO_ESTABLISHED_COMPARISON_NOT_ASSESSED"
            row["display"][col_idx]=after
            grid[idx][col_idx]=after
            row.setdefault("Donor_visible_status_repair_20261114",{})[donor]={
                "status":status,"original_cell":"","display_cell":letter+str(excel_row),
                "no_negative_source_claim":True
            }
            changes.append({"row_id":row["row_id"],"cell":letter+str(excel_row),
                            "status":status,"before":before,"after":after})
        data_idx+=1
    need(data_idx==337 and len(row_positions)==337,"all 337 information rows mapped")
    bycol=Counter(c["cell"][0] for c in changes)
    caseholds=Counter(c["cell"][0] for c in changes if c["status"]=="CASE_REVIEW_HOLD")
    need(dict(bycol)=={"H":51,"I":13} and dict(caseholds)=={"H":9,"I":9},
         "exactly 51 SAPIENT and 13 ISA original blanks, including 9+9 case holds")
    need(all(row["display"][j] for row in m["rows"] for j in (6,7,8,9)),
         "zero blank data cells across four completed donor columns")
    for idx,(before,after) in enumerate(zip(last_grid,grid)):
        for c,(v0,v1) in enumerate(zip(before,after)):
            if c not in (7,8):need(v0==v1,"never modify other donor/case/OGC/DIM text")
    need(len(m["F2_5_color_reconciliation"]["color_assignments"])==325
         and len(m["AAS10_color_reconciliation"]["assignments"])==54,
         "existing 325 original and 54 AAS candidate meanings preserved")

    # Both CSV mirrors and both readable comparisons are canonical display mirrors.
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.csv","ISA_Correction_Review_07NOV2026.csv"):
        with (D/name).open("w",newline="",encoding="utf-8") as f:
            csv.writer(f,lineterminator="\r\n").writerows(grid)
    htmlrows=["<table>","<thead><tr>",
              '<th colspan="4">'+html.escape(grid[0][0])+"</th>",
              '<th colspan="6">'+html.escape(grid[0][4])+"</th>",
              '<th colspan="5">'+html.escape(grid[0][10])+"</th>",
              "<th>"+html.escape(grid[0][15])+"</th>",
              "</tr><tr>"+"".join("<th>"+html.escape(v)+"</th>" for v in grid[1])+"</tr></thead><tbody>"]
    for idx,row in enumerate(grid[2:],2):
        if idx in sections:
            htmlrows.append('<tr><th colspan="16">'+html.escape(row[0])+"</th></tr>")
        else:
            htmlrows.append("<tr>"+"".join("<td>"+html.escape(v)+"</td>" for v in row)+"</tr>")
    htmlrows+=["</tbody></table>"]
    banner=("# CURRENT — Excel worksheet ordering and four-donor blank statuses corrected (14 November 2026)\n\n"
            "The previous saved XLSX contained physically out-of-order cell records, including G24/G25, "
            "which can cause Excel to repair/remove cells despite CSV/XLSX values appearing consistent. "
            "The workbook has been reordered, and the previously blank 51 SAPIENT and 13 ISA data cells "
            "now carry explicit source-neutral status labels. All G/H/I/J information cells are nonblank "
            "in the saved file; source-grade and DIM/Profile adoption are unchanged. "
            "This corrects a display/integrity failure, NOT the AAS native-first research audit.\n\n---\n\n")
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.md","ISA_Correction_Review_07NOV2026.md"):
        previous=(D/name).read_text(encoding="utf-8")
        need("<table>" in previous and "</table>" in previous,"readable comparison source table exists")
        front=previous[:previous.index("<table>")]
        back=previous[previous.index("</table>")+8:]
        (D/name).write_text(banner+front+"\n".join(htmlrows)+"\n"+back,encoding="utf-8")

    def qcol(ref):
        match=re.match(r"([A-Z]+)([0-9]+)$",ref or "")
        need(bool(match),"legal A1 ref "+str(ref))
        result=0
        for ch in match.group(1):result=26*result+ord(ch)-64
        return result

    def readcell(c):
        if c is None:return ""
        x=c.find(q("is"))
        if x is not None:return "".join(t.text or "" for t in x.iter(q("t")))
        x=c.find(q("v"))
        return "" if x is None else (x.text or "")
    def setcell(c,value):
        for child in list(c):c.remove(child)
        c.set("t","inlineStr")
        t=ET.SubElement(ET.SubElement(c,q("is")),q("t"))
        if value[:1].isspace() or value[-1:].isspace():
            t.set("{http://www.w3.org/XML/1998/namespace}space","preserve")
        t.text=value
    def order_cells(root):
        sd=root.find(q("sheetData"));need(sd is not None,"original sheetData exists")
        ordered_rows=0
        moved=0
        count=0
        for rr in sd.findall(q("row")):
            cs=rr.findall(q("c"))
            if not cs:continue
            refs=[c.get("r") for c in cs]
            need(len(refs)==len(set(refs)),"duplicate Excel source cell "+str(refs))
            sorted_cells=sorted(cs,key=lambda c:qcol(c.get("r")))
            if cs!=sorted_cells:
                others=[c for c in rr if c.tag!=q("c")]
                need(not others,"unexpected row children prevent safe cell order repair")
                for c in cs:rr.remove(c)
                for c in sorted_cells:rr.append(c)
                ordered_rows+=1
                moved+=sum(a is not b for a,b in zip(cs,sorted_cells))
            count+=len(cs)
            need(all(qcol(x.get("r"))<qcol(y.get("r")) for x,y in zip(rr.findall(q("c")),rr.findall(q("c"))[1:])),
                 "strict ascending cell column order required")
        return ordered_rows,moved,count

    with zipfile.ZipFile(io.BytesIO(prior)) as z:
        need(z.testzip() is None,"pre-fix workbook ZIP CRC")
        paths=old.sheetpaths(z)
        need(len(paths)==26,"preserve one 26-sheet original XLSX")
        prexml={name:digest(z.read(path)) for name,path in paths.items()}
        master=ET.fromstring(z.read(paths["Master Crosswalk"]))
        master_sd=master.find(q("sheetData"))
        original_cells={c.get("r"):c for c in master_sd.iter(q("c"))}
        evidence_styles={ref:c.get("s","0") for ref,c in original_cells.items()}
        # The OOXML parser in older CI read content but did not check child sequence.
        # Source values G24/G25 are present yet appear blank when Excel repairs.
        for ref in ("G24","G25"):
            need(ref in original_cells and readcell(original_cells[ref])==last_grid[int(ref[1:])-1][6],
                 "the observed blank was an Excel-open integrity defect, not source absence "+ref)
        for x in changes:
            excel_row=int(re.search(r"\d+",x["cell"]).group())
            rr=next((r for r in master_sd.findall(q("row")) if int(r.get("r"))==excel_row),None)
            need(rr is not None,"previous saved row exists "+x["cell"])
            cell=next((c for c in rr.findall(q("c")) if c.get("r")==x["cell"]),None)
            if cell is None:
                cell=ET.SubElement(rr,q("c"),{"r":x["cell"],"s":"526"})
            else:
                need(not readcell(cell),"previously blank cell truly blank "+x["cell"])
            setcell(cell,x["after"])
            # Existing white wrapped body style; this is not a classification.
            cell.set("s","526")
            rr.set("ht",str(min(409.5,max(float(rr.get("ht","30")),
                                         80+len(x["after"])//4))))
            rr.set("customHeight","1")
        fixed_rows,moved,source_cell_count=order_cells(master)
        need(fixed_rows>0 and moved>0,"out-of-order Excel cell records reproduced and repaired")
        replacements={paths["Master Crosswalk"]:ET.tostring(master,encoding="utf-8",xml_declaration=True)}
        def put_current(sheet,edits):
            root=ET.fromstring(z.read(paths[sheet]))
            allcells={c.get("r"):c for c in root.iter(q("c"))}
            for ref,text in edits.items():
                cell=allcells.get(ref)
                need(cell is not None,"current guidance cell exists "+sheet+"!"+ref)
                setcell(cell,text)
            order_cells(root)
            return ET.tostring(root,encoding="utf-8",xml_declaration=True)
        guidance={
          "A1":"CURRENT 14 NOV 2026 — four donor columns explicit; Excel worksheet cell order repaired",
          "B17":"Workbook visibility/integrity correction verified; native-first source opportunity audit is NOT started; owner review next.",
          "B19":"AAS 64 source comparisons + 273 unassessed; SAPIENT 51 former blanks labeled; ISA 13 former blanks labeled; SOSA 0 blanks. Every G/H/I/J data cell has visible status.",
          "B23":"AAS source coverage still bounded PARTIAL, no native-first new-row completeness conclusion; old 310 findings unchanged."
        }
        replacements[paths["Summary"]]=put_current("Summary",guidance)
        replacements[paths["Validation"]]=put_current("Validation",guidance)
        replacements[paths["Legend"]]=put_current("Legend",{
          "A1":"CURRENT LEGEND 14 NOV 2026 — no blank donor information cells and Excel XML cell order repaired",
          "B28":"G/H/I/J data rows have explicit values/status; 51 SAPIENT and 13 ISA blanks labeled; no source-negative absences or new source/audit claims."
        })
        need(len(replacements)==4 and len([n for n,path in paths.items() if path not in replacements])==22,
             "original four worksheet parts changed, 22 untouched preserved")
        output=io.BytesIO()
        with zipfile.ZipFile(output,"w") as dst:
            for info in z.infolist():
                dst.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    saved=output.getvalue()
    (D/BOOK).write_bytes(saved)
    with zipfile.ZipFile(io.BytesIO(prior)) as before,zipfile.ZipFile(D/BOOK) as after:
        need(after.testzip() is None and old.sheetpaths(after)==paths,
             "actual saved ZIP, same sheet identities and order")
        for name in after.namelist():
            if name.endswith((".xml",".rels")):ET.fromstring(after.read(name))
            if name not in replacements:
                need(after.read(name)==before.read(name),
                     "all other package parts byte-identical "+name)
        sheet=ET.fromstring(after.read(paths["Master Crosswalk"]))
        order_again,removes,cell_count=order_cells(sheet)
        need(order_again==0 and removes==0,"saved worksheet row cells strictly ordered")
        byref={c.get("r"):c for c in sheet.iter(q("c"))}
        for i,record in enumerate(grid,1):
            for j,textval in enumerate(record):
                ref=addr(i,j+1)
                need(readcell(byref.get(ref))==textval,"saved source-grid cell "+ref)
                if i>2 and record[15] and j in (6,7,8,9):
                    need(textval.strip(),"no unexplained blank donor entry "+ref)
        need(len(grid)==354 and all(len(r)==16 for r in grid),
             "unchanged approved grid dimensions")
        for ref,oldstyle in evidence_styles.items():
            if ref not in {x["cell"] for x in changes}:
                need(byref[ref].get("s","0")==oldstyle,
                     "all original source/case/classification styles untouched "+ref)
        for name,path in paths.items():
            if path not in replacements:
                need(digest(after.read(path))==prexml[name],
                     "historical worksheet byte preserved "+name)
    sha=digest(saved)
    need(digest((D/BOOK).read_bytes())==sha,"reopened saved current XLSX hash")
    need(source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")==grid
         ==source_csv("ISA_Correction_Review_07NOV2026.csv"),
         "both CSV mirrors exact")
    from html.parser import HTMLParser
    class Reader(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.row=None;self.tmp=None;self.span=1
        def handle_starttag(self,tag,attrs):
            if tag=="tr":self.row=[]
            elif tag in ("td","th"):self.tmp="";self.span=int(dict(attrs).get("colspan",1))
        def handle_data(self,data):
            if self.tmp is not None:self.tmp+=data
        def handle_endtag(self,tag):
            if tag in ("td","th") and self.tmp is not None:
                self.row.extend([self.tmp]+[""]*(self.span-1));self.tmp=None
            elif tag=="tr":self.rows.append(self.row);self.row=None
    md=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    need(md==(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8"),
         "both GitHub-readable comparisons identical")
    x=Reader();x.feed(md[md.index("<table>"):md.index("</table>")+8])
    need(x.rows[1:]==grid[1:],"all GitHub-readable current source-grid values")
    m["currentEvidenceCheckpoint"]="AAS10B_OFFICE_ORDER_AND_FOUR_DONOR_STATUSES_SAVED_VERIFIED"
    m["currentWorkbookSha256"]=sha
    m["workbookSnapshot"].update({
        "checkpoint":"AAS10B_OFFICE_ORDER_AND_FOUR_DONOR_STATUSES_SAVED_VERIFIED",
        "sha256":sha,"currently_matches_readable_view":True,
        "lag":"ZERO: canonical JSON, both CSVs, both Markdown views and saved 26-sheet XLSX",
        "textCheckpoint":"AAS10B_EXCEL_ORDER_AND_DONOR_STATUS_ONLY",
        "validation_file":"AAS01_Original_Source_Corpus_Coverage_13NOV2026.json#/AAS10/office_order_and_donor_blank_repair"
    })
    next_action=("OWNER REVIEW OF CORRECTED/REOPENED FOUR-DONOR WORKBOOK; "
                 "NEXT SEPARATELY AUTHORIZED STEP SHOULD BE AAS NATIVE-FIRST NEW-ROW "
                 "OPPORTUNITY AUDIT UNDER SOURCE-SIZED PLAN, NOT DONOR CLOSURE OR TRANSITION.")
    m["nextOwnerAction"]=next_action
    led["one_next"]=next_action
    led["master_state_current"].update({
       "checkpoint":"AAS10B_OFFICE_ORDER_AND_FOUR_DONOR_STATUSES_SAVED_VERIFIED",
       "comparison_lag":0,"next":next_action,
       "status":"FOUR_DONOR_STATUS_AND_OFFICE_CELL_ORDER_REPAIRED__SOURCE_COVERAGE_UNCHANGED"
    })
    saved_aas=led["AAS10"]
    saved_aas["office_order_and_donor_blank_repair"]={
        "date":"2026-11-14",
        "baseline_commit":"e44549f21f6ccfc53df63a91e08a2db1e16418c2",
        "archive_branch":"archive/dim-crosswalk-pre-excel-order-repair-20261114",
        "scope":"XLSX_CELL_SEQUENCE_AND_EXPLICIT_STATUSES_ONLY__NO_NATIVE_SOURCE_AUDIT",
        "previous_workbook_sha256":digest(prior),"current_workbook_sha256":sha,
        "worksheet_rows_reordered":fixed_rows,"cell_positions_moved_in_reordering":moved,
        "formerly_blank_statuses":changes,"counts":dict(bycol),
        "case_hold_counts":dict(caseholds),"affected_original_worksheets":["Master Crosswalk","Summary","Validation","Legend"],
        "historic_sheets_preserved":22,"original_325_colors_preserved":True,
        "original_54_AAS_candidate_fills_preserved":True,
        "M00_M01_preserved":True,"M02_created":False,
        "saved_grid_cells_checked":5664,"visual_owner_open_in_Microsoft_Excel":"NOT_YET_INDEPENDENTLY_RETESTED",
        "source_research_added":0,
        "one_next":next_action,"status":"VERIFIED_OOXML_GRID_ORDER_AND_DONOR_STATUS__OWNER_EXCEL_RENDER_REVIEW_PENDING"
    }
    need(not list((D/"Manual_Workbook_Versions").glob("M02*")),"owner manual versions remain unchanged")
    save(MASTER,m)
    save("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json",led)
    print("SAVED EXCEL ORDER REPAIR PASS:",fixed_rows,"worksheet rows reordered,",moved,"cell element positions moved.")
    print("PASS: 337x4 donor text statuses, SAPIENT 51 and ISA 13 legacy blanks labeled; original 54 AAS and 325 other donor candidate fills preserved.")
    print("PASS: same original 26-sheet workbook, 5664 saved grid cells, both CSV/Markdown mirrors, 22 unchanged sheet XML parts, M00/M01 untouched.")
    print("LIMIT: Excel actual on-screen repair/no-repair is not yet re-tested; original source coverage and native-first new-row audit still incomplete.")


def verify_donor_visible_order_repair():
    """Read-only independent saved-state check; invoked by the existing checker."""
    import hashlib
    m=load(MASTER)
    ledger=load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json")
    r=ledger["AAS10"]["office_order_and_donor_blank_repair"]
    need(m["currentEvidenceCheckpoint"]=="AAS10B_OFFICE_ORDER_AND_FOUR_DONOR_STATUSES_SAVED_VERIFIED"
         and r["status"]=="VERIFIED_OOXML_GRID_ORDER_AND_DONOR_STATUS__OWNER_EXCEL_RENDER_REVIEW_PENDING",
         "versioned corrected source state")
    need(len(m["rows"])==337 and len(m["review_grid"])==354
         and all(len(x)==16 for x in m["review_grid"]),"source dimensions unchanged")
    need(m["nextOwnerAction"]==ledger["one_next"]==r["one_next"],"one next owner action")
    need(sum(bool(x["display"][j]) for x in m["rows"] for j in (6,7,8,9))==337*4,
         "all four completed donor columns explicitly populated")
    need(sum(x["cell"].startswith("H") for x in r["formerly_blank_statuses"])==51
         and sum(x["cell"].startswith("I") for x in r["formerly_blank_statuses"])==13,
         "exact formerly blank source-neutral donor dispositions")
    need(len(m["F2_5_color_reconciliation"]["color_assignments"])==325
         and len(m["AAS10_color_reconciliation"]["assignments"])==54,
         "original source color classifications preserved")
    need(source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")==m["review_grid"]
         ==source_csv("ISA_Correction_Review_07NOV2026.csv"),
         "both source CSVs exact")
    saved=(D/BOOK).read_bytes()
    need(digest(saved)==m["currentWorkbookSha256"]==m["workbookSnapshot"]["sha256"]
         ==r["current_workbook_sha256"],"saved workbook source hash")
    with zipfile.ZipFile(io.BytesIO(saved)) as z:
        need(z.testzip() is None and len(old.sheetpaths(z))==26,"original XLSX package/sheet count")
        p=old.sheetpaths(z)
        s=ET.fromstring(z.read(p["Master Crosswalk"]))
        actual={}
        for row in s.find(q("sheetData")).findall(q("row")):
            cells=row.findall(q("c"))
            refs=[c.get("r") for c in cells]
            need(refs==sorted(refs,key=lambda x:(len(re.match(r"^[A-Z]+",x).group()),re.match(r"^[A-Z]+",x).group())) if False else True,"")
            nums=[]
            for c in cells:
                ref=c.get("r")
                n=0
                for char in re.match(r"^[A-Z]+",ref).group():n=n*26+ord(char)-64
                nums.append(n)
                need(ref not in actual,"no duplicate saved worksheet cell "+ref)
                v=c.find(q("is"))
                actual[ref]="".join(t.text or "" for t in v.iter(q("t"))) if v is not None else (c.findtext(q("v")) or "")
            need(nums==sorted(nums) and len(nums)==len(set(nums)),
                 "strict sorted OOXML cells in row "+row.get("r"))
        for idx,record in enumerate(m["review_grid"],1):
            for j,expected in enumerate(record,1):
                need(actual.get(addr(idx,j),"")==expected,
                     "actual saved cell equality "+addr(idx,j))
        for name,sha in ledger["AAS10"]["office_order_and_donor_blank_repair"].get("original_22_historical_sheet_sha256",{}).items():
            need(digest(z.read(p[name]))==sha,"historical sheet sha "+name)
    need(not list((D/"Manual_Workbook_Versions").glob("M02*")),"no M02")
    need(m["AASEvidence"]["donor_status"]=="ACTIVE_CORRECTED_OWNER_REVIEW_PENDING",
         "donor not closed or promoted")
    print("PASS: AAS10B independent OOXML row-order, no G/H/I/J blank cells, full 5664 saved values, 26 preserved sheets, CSV mirror parity.")
    print("LIMIT: Excel user-facing open/repair validation and original-source semantic completeness are separate.")


F3_ISA_EVIDENCE = "ISA21_Source_First_31_Targets_25_Findings_6_Questions_09NOV2026.json"
F3_ISA_BASE = "00ada697e070adb6eeafeda49819599ee8d3c5c2"


def f3_baseline(name, base=F3_ISA_BASE):
    """Read exact archived bytes for a source-classification checkpoint."""
    import subprocess
    root = Path(__file__).resolve().parents[1]
    return subprocess.check_output(
        ["git", "show", base + ":" + str((D / name).relative_to(root))], cwd=root)


def f3_cell_text(cell):
    if cell is None:
        return ""
    inline = cell.find(q("is"))
    if inline is not None:
        return "".join(t.text or "" for t in inline.iter(q("t")))
    return cell.findtext(q("v")) or ""


def f3_put(cell, value):
    for child in list(cell):
        cell.remove(child)
    cell.set("t", "inlineStr")
    ET.SubElement(ET.SubElement(cell, q("is")), q("t")).text = value


def f3_config(stage):
    if stage == "F3_05":
        return {"base": "ac19c6f31ab9aff7a270e96dbfa51781db729717",
                "evidence": "AAS01_Original_Source_Corpus_Coverage_13NOV2026.json",
                "donor": "AAS", "column": 6, "register": "R", "count": 64,
                "counts": {"COMMON_CANDIDATE": 37, "SPECIALIZED_CANDIDATE": 10,
                           "NATIVE_ONLY_EVIDENCE": 2, "UNRESOLVED_CANDIDATE": 3,
                           "MIXED_OR_HELD": 12}}
    if stage == "F3_04D":
        return {"base": "6c81253431361343e8e0351cf54b648958db4425",
                "evidence": "SOSA_G4_F_192_Heading_Source_and_Master_Ledger_11NOV2026.json",
                "donor": "OpenGroupSOSA", "column": 9, "register": "O", "count": 33,
                "counts": {"COMMON_CANDIDATE": 18, "SPECIALIZED_CANDIDATE": 2, "MIXED_OR_HELD": 13}}
    if stage == "F3_04C":
        return {"base": "82417e8663c54e706e93987ae06f2a04827dd612",
                "evidence": "SOSA_G4_F_192_Heading_Source_and_Master_Ledger_11NOV2026.json",
                "donor": "OpenGroupSOSA", "column": 9, "register": "O", "count": 21,
                "counts": {"COMMON_CANDIDATE": 4, "SPECIALIZED_CANDIDATE": 3, "MIXED_OR_HELD": 14}}
    if stage == "F3_04B":
        return {"base": "5aaa9523ada6c0518666e303c67fb5f5d8da6471",
                "evidence": "SOSA_G4_F_192_Heading_Source_and_Master_Ledger_11NOV2026.json",
                "donor": "OpenGroupSOSA", "column": 9, "register": "O", "count": 34,
                "counts": {"COMMON_CANDIDATE": 16, "SPECIALIZED_CANDIDATE": 7, "MIXED_OR_HELD": 11}}
    if stage == "F3_04A":
        return {"base": "cbc5139e4ab1298f0d9c46e9ee05435ebd33d85f",
                "evidence": "SOSA_G4_F_192_Heading_Source_and_Master_Ledger_11NOV2026.json",
                "donor": "OpenGroupSOSA", "column": 9, "register": "O", "count": 19,
                "counts": {"COMMON_CANDIDATE": 9, "SPECIALIZED_CANDIDATE": 3, "MIXED_OR_HELD": 7}}
    if stage == "F3_02":
        return {"base": F3_ISA_BASE, "evidence": F3_ISA_EVIDENCE, "donor": "ISA", "column": 8,
                "register": "N", "count": 18,
                "counts": {"COMMON_CANDIDATE": 9, "SPECIALIZED_CANDIDATE": 2, "MIXED_OR_HELD": 7}}
    need(stage == "F3_03", "known source-classification stage")
    return {"base": "f636b00d494ce8d5e9beb9d50faa90219bebc2f6",
            "evidence": "SAP01_Original_Corpus_Coverage_12NOV2026.json", "donor": "SAPIENT", "column": 7,
            "register": "M", "count": 51,
            "counts": {"COMMON_CANDIDATE": 13, "SPECIALIZED_CANDIDATE": 4,
                       "UNRESOLVED_CANDIDATE": 2, "MIXED_OR_HELD": 32}}


def publish_f3(stage="F3_02"):
    """Publish scoped source decisions through the existing workbook without rebuilding it."""
    import html
    cfg = f3_config(stage)
    key = stage + "_classification_review"
    rowkey = stage + "_" + cfg["donor"] + "_classification"
    label = stage.replace("_", "-")
    m = load(MASTER)
    evidence = load(cfg["evidence"])
    review = evidence[key]
    records = review["records"]
    need(m["currentEvidenceCheckpoint"] == stage + "_SOURCE_CLASSIFIED_PENDING_SAME_XLSX",
         label + " source decisions precede publication")
    prior = (D / BOOK).read_bytes()
    need(prior == f3_baseline(BOOK, cfg["base"]), "publish against the preserved exact pre-change workbook")
    grid = m["review_grid"]
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.csv", "ISA_Correction_Review_07NOV2026.csv"):
        with (D / name).open("w", newline="", encoding="utf-8") as f:
            csv.writer(f, lineterminator="\n").writerows(grid)
    table = ["<table><thead><tr>"]
    for idx, span in ((0, 4), (4, 6), (10, 5), (15, 1)):
        table.append(f'<th colspan="{span}">{html.escape(grid[0][idx])}</th>')
    table += ["</tr><tr>" + "".join("<th>" + html.escape(v) + "</th>" for v in grid[1]) + "</tr></thead><tbody>"]
    for idx, row in enumerate(grid[2:], 2):
        table.append('<tr><th colspan="16">' + html.escape(row[0]) + "</th></tr>" if idx in m["review_sections"]
                     else "<tr>" + "".join("<td>" + html.escape(v) + "</td>" for v in row) + "</tr>")
    table += ["</tbody></table>"]
    banner = (f"# CURRENT — {label} {cfg['donor']} classification checkpoint (14 November 2026)\n\n"
              f"{len(records)} individually recorded source-comparison decisions are published in the existing evidence. "
              "For F3-03, these are 39 previously ungraded cells (4 common, 3 specialized, 2 unresolved, 30 held) "
              "plus 12 corrections to prior classifications. " if stage == "F3_03" else
              "# CURRENT — F3-02 ISA classification checkpoint (14 November 2026)\n\n18 early ISA comparisons: 9 common, 2 specialized, 7 held. ")
    banner += ("All 337 rows, other donor/case values and original source holds are preserved. "
               "The same workbook matches these values; clean Microsoft Excel reopening remains unverified. "
               "Classification is not model adoption or comprehensive source coverage. " + review["next"] +
               "\n\nEarlier checkpoint banners below are historical.\n\n---\n\n")
    if stage == "F3_04A":
        banner = ("# CURRENT — F3-04A Open Group SOSA classification checkpoint (14 November 2026)\n\n"
                  "16 previously ungraded comparisons: 6 common, 3 specialized, 7 explicit holds. "
                  "Three prior physical-context classifications corrected to common candidates. "
                  "87 later SOSA comparisons remain ungraded. All 337 rows, other donor/case values, "
                  "original source evidence and holds are preserved. The same workbook matches these values; "
                  "clean Microsoft Excel reopening remains unverified. Classification is neither model adoption "
                  "nor comprehensive source coverage. " + review["next"] +
                  "\n\nEarlier checkpoint banners below are historical.\n\n---\n\n")
    if stage == "F3_04B":
        banner = ("# CURRENT — F3-04B Open Group SOSA classification checkpoint (14 November 2026)\n\n"
                  "33 previously ungraded comparisons: 15 common, 7 specialized, 11 explicit holds. "
                  "One prior control-request hold corrected to a common candidate; six relevant prior decisions retained. "
                  "54 later SOSA comparisons remain ungraded. All 337 rows, other donor/case values, "
                  "original source evidence and holds are preserved. The same workbook matches these values; "
                  "clean Microsoft Excel reopening remains unverified. Classification is neither model adoption "
                  "nor comprehensive source coverage. " + review["next"] +
                  "\n\nEarlier checkpoint banners below are historical.\n\n---\n\n")
    if stage == "F3_04C":
        banner = ("# CURRENT — F3-04C Open Group SOSA classification checkpoint (14 November 2026)\n\n"
                  "21 previously ungraded comparisons: 4 common, 3 specialized, 14 explicit holds, including nine case holds. "
                  "Four relevant earlier decisions checked and retained. 33 equipment comparisons remain ungraded. "
                  "All 337 rows, other donor/case values, original source evidence and holds are preserved. "
                  "The same workbook matches these values; clean Microsoft Excel reopening remains unverified. "
                  "Classification is neither model adoption nor comprehensive source coverage. " + review["next"] +
                  "\n\nEarlier checkpoint banners below are historical.\n\n---\n\n")
    if stage == "F3_04D":
        banner = ("# CURRENT — F3-04D Open Group SOSA classification checkpoint (14 November 2026)\n\n"
                  "33 previously ungraded equipment comparisons: 18 common, 2 specialized, 13 explicit holds. "
                  "Six relevant earlier decisions retained. SOSA: 76 colored, 45 held, zero ungraded. "
                  "All 337 rows, other donor/case values, original source evidence and holds are preserved. "
                  "The same workbook matches these values; clean Microsoft Excel reopening remains unverified. "
                  "Classification is neither model adoption nor comprehensive source coverage. " + review["next"] +
                  "\n\nEarlier checkpoint banners below are historical.\n\n---\n\n")
    if stage == "F3_05":
        banner = ("# CURRENT — F3-05 Asset Administration Shell classification checkpoint (14 November 2026)\n\n"
                  "64 existing comparisons: 37 common, 10 specialized, 2 native-only, 3 unresolved and 12 held. "
                  "Four holds gained qualified candidate support; six unsupported comparison colors were removed. "
                  "34 classifications changed and 30 were retained. AAS: 52 colored, 12 held, zero ungraded. "
                  "All 337 rows, other donor/case evidence and original holds are preserved. "
                  "The same workbook matches these values; clean Microsoft Excel reopening remains unverified. "
                  "This targeted classification pass is not full source coverage or model adoption. " + review["next"] +
                  "\n\nEarlier checkpoint banners below are historical.\n\n---\n\n")
    for name in ("Master_Donor_Concept_to_DIM_Crosswalk.md", "ISA_Correction_Review_07NOV2026.md"):
        before = f3_baseline(name, cfg["base"]).decode("utf-8")
        (D / name).write_text(banner + before[:before.index("<table>")] + "\n".join(table)
                             + before[before.index("</table>") + 8:], encoding="utf-8")
    with zipfile.ZipFile(io.BytesIO(prior)) as z:
        paths = old.sheetpaths(z)
        replacements = {}
        def edit_sheet(name, edits, styles=None):
            root = ET.fromstring(z.read(paths[name]))
            cells = {c.get("r"): c for c in root.iter(q("c"))}
            for ref, value in edits.items():
                if ref not in cells:
                    need(name == "DIM Register" and ref.startswith("P"), "only blank provenance cells may be materialized")
                    number = ref[1:]
                    rr = next(r for r in root.find(q("sheetData")) if r.get("r") == number)
                    cell = ET.Element(q("c"), {"r": ref, "s": cells["N" + number].get("s", "0")})
                    at = next((i for i, item in enumerate(rr) if item.get("r", "Z0").rstrip("0123456789") > "P"), len(rr))
                    rr.insert(at, cell)
                    cells[ref] = cell
                f3_put(cells[ref], value)
                if styles and ref in styles:
                    cells[ref].set("s", str(styles[ref]))
            if name in ("Summary", "Validation"):
                heights = {1: 60, 17: 65, 19: 80, 21: 75, 22: 65, 23: 95}
                for rr in root.find(q("sheetData")):
                    if int(rr.get("r")) in heights:
                        rr.set("ht", str(max(float(rr.get("ht", "15")), heights[int(rr.get("r"))])))
                        rr.set("customHeight", "1")
            if name == "Master Crosswalk":
                import textwrap
                for rr in root.find(q("sheetData")):
                    ref = chr(65 + cfg["column"]) + rr.get("r")
                    if ref in edits:
                        lines = len(textwrap.wrap(edits[ref], width=40))
                        rr.set("ht", str(min(409.5, max(float(rr.get("ht", "15")), lines * 12 + 12))))
                        rr.set("customHeight", "1")
            replacements[paths[name]] = ET.tostring(root, encoding="utf-8", xml_declaration=True)
        style_ids = {"COMMON_CANDIDATE": 528, "SPECIALIZED_CANDIDATE": 529,
                     "NATIVE_ONLY_EVIDENCE": 530, "UNRESOLVED_CANDIDATE": 531}
        prior_cells = {c.get("r"): c for c in ET.fromstring(z.read(paths["Master Crosswalk"])).iter(q("c"))}
        rowindex = {r["row_id"]: i for i, r in enumerate(m["rows"])}
        current_styles = {}
        for record in records:
            if record["fill"]:
                current_styles[record["cell"]] = style_ids[record["candidate_status"]]
            else:
                oldstyle = int(prior_cells[record["cell"]].get("s", "0"))
                # Historical F2 banding is by zero-based data-row ordinal, not worksheet row.
                current_styles[record["cell"]] = (526 + rowindex[record["row_id"]] % 2
                                                   if stage == "F3_05" or oldstyle in style_ids.values() else oldstyle)
        edit_sheet("Master Crosswalk", {r["cell"]: r["after"] for r in records}, current_styles)
        guidance = {
            "A1": "CURRENT 14 NOV 2026 — F3-02: 18 ISA early comparisons classified from original evidence",
            "B17": "F3-02 complete: 9 common, 2 specialized, 7 explicit held comparisons; no DIM/Profile adoption. Next separate Proceed: F3-03 SAPIENT only.",
            "B19": "ISA: 271 colored + 45 held + 0 ungraded source comparisons. Four donors: 390 colored + 84 held + 142 ungraded = 616 source-bearing cells. Other positions retain explicit statuses.",
            "A19": "Current four-donor classification standing",
            "B21": "F3-02 reopened targeted passages in DMS 6.0r12, SDD/ICD 6.0r5, CMPT/CNTR 6.0r4 and TOPICS 6.0r2; 18 ISA comparison dispositions and 9 selected older classifications checked. Not a whole-corpus re-audit.",
            "B22": "Current: 390 candidate colors and 84 explicit source holds. Previous 325 donor colors and 54 AAS colors retained; F3-02 adds 11 ISA colors and 7 explicit no-fill holds. Candidate status is not model adoption.",
            "A23": "Preserved source and owner holds",
            "B23": "Targeted passages in six ISA original editions reviewed; prior bounded coverage and six ISA questions retained. AAS native-first research waits for F3 owner gate. Clean Microsoft Excel reopen remains UNVERIFIED."
        }
        if stage == "F3_03":
            guidance = {
                "A1": "CURRENT 14 NOV 2026 — F3-03 SAPIENT classification and calibration complete",
                "B17": "39 ungraded: 4 common, 3 specialized, 2 unresolved, 30 held. Also 12 prior classifications corrected. Next separate Proceed: first bounded F3-04 SOSA packet.",
                "A19": "Current four-donor classification standing",
                "B19": "SAPIENT: 65 colored + 50 held + 0 ungraded. Four donors: 405 colored + 108 held + 103 ungraded = 616 source-bearing comparisons.",
                "B21": "Targeted BSI Flex 335 v2 original text and 11 pinned Protobuf files rechecked. 51 comparison decisions reference 62 existing native finding IDs; this is not 62 new clause audits or a whole-corpus review.",
                "B22": "Classification changes: 17 newly colored cells, 2 colors removed, 2 colors changed. All other donor/case values and original holds retained. Blue/amber candidates remain qualified; purple marks unresolved meaning.",
                "A23": "Preserved source and owner holds",
                "B23": "BSI content-time versus schema send-time remains unresolved. SAP07 bounded PARTIAL, its original source/access holds, ISA/SOSA holds and AAS findings retained. AAS native-first work waits for F3 owner gate. Clean Microsoft Excel reopen UNVERIFIED."
            }
        if stage == "F3_04A":
            guidance = {
                "A1": "CURRENT 14 NOV 2026 — F3-04A Open Group SOSA first classification packet complete",
                "B17": "16 ungraded: 6 common, 3 specialized, 7 held. Three prior physical-context decisions corrected to common. Next separate Proceed: F3-04B, 33 group-04 comparisons and relevant calibration only.",
                "A19": "Current four-donor classification standing",
                "B19": "Open Group SOSA: 26 colored + 8 held + 87 ungraded = 121. Four donors: 416 colored + 113 held + 87 ungraded = 616 source-bearing comparisons.",
                "B21": "Targeted original C239 2023 text/selected physical-context figure, 2022 DSDM text and four 2022 IDL files examined. Existing source IDs support 19 comparison decisions; no whole-corpus or 2023-native-byte equivalence claim.",
                "B22": "11 newly colored cells and one amber-to-blue correction. Candidate information is separate from exact mapping. Holds preserve different subjects, undefined occurrence timing and missing observing-act relationships.",
                "A23": "Preserved source and owner holds",
                "B23": "Nine SOSA hold families, six ISA questions, SAPIENT source/timestamp holds and all AAS findings retained. 2022 and 2023 editions remain distinct; no DIM/Profile adoption. AAS O1 waits for F3 gate. Clean Microsoft Excel reopen UNVERIFIED."
            }
        if stage == "F3_04B":
            guidance = {
                "A1": "CURRENT 14 NOV 2026 — F3-04B SOSA configuration/control classifications complete",
                "B17": "33 ungraded: 15 common, 7 specialized, 11 held. One prior control-request hold corrected to common; six prior decisions retained. Next separate Proceed: F3-04C, 21 evidence/message/case comparisons only.",
                "A19": "Current four-donor classification standing",
                "B19": "Open Group SOSA: 49 colored + 18 held + 54 ungraded = 121. Four donors: 439 colored + 123 held + 54 ungraded = 616 source-bearing comparisons.",
                "B21": "Targeted C239 2023 management/task/interaction text and selected support table, 2022 DSDM passages and 20 IDL files examined. 34 comparison changes; no whole-corpus, compilation or 2023-native-byte equivalence claim.",
                "B22": "23 newly colored cells. Typed fields, command contracts and bounded collections remain useful without exact ISA equivalence. Current component condition is not per-capability readiness; preliminary task and Future interfaces stay qualified.",
                "A23": "Preserved source and owner holds",
                "B23": "Nine SOSA hold families, six ISA questions, SAPIENT source/timestamp holds and all AAS findings retained. 2022 and 2023 editions remain distinct; no DIM/Profile adoption. AAS O1 waits for F3 gate. Clean Microsoft Excel reopen UNVERIFIED."
            }
        if stage == "F3_04C":
            guidance = {
                "A1": "CURRENT 14 NOV 2026 — F3-04C SOSA evidence/message/case classifications complete",
                "B17": "21 ungraded: 4 common, 3 specialized, 14 held, including nine case holds. Four relevant prior decisions retained. Next separate Proceed: F3-04D, 33 remaining equipment comparisons only.",
                "A19": "Current four-donor classification standing",
                "B19": "Open Group SOSA: 56 colored + 32 held + 33 ungraded = 121. Four donors: 446 colored + 137 held + 33 ungraded = 616 source-bearing comparisons.",
                "B21": "Targeted C239 2023 audit/management/QoS/binding/vendor-documentation passages, 2022 DSDM text and seven IDL files examined. 21 comparison decisions; no new case observation, whole-corpus or 2023-native-byte equivalence claim.",
                "B22": "Seven newly colored cells: message identity/source, administrative notifications, time basis, vendor declarations, standard standing and encoding metadata. Writer priority differs from message priority; deadline differs from data expiry.",
                "A23": "Preserved source and owner holds",
                "B23": "Nine SOSA hold families, six ISA questions, SAPIENT source/timestamp holds and all AAS findings retained. All nine case gaps remain unverified. No DIM/Profile adoption; AAS O1 waits for F3 gate. Clean Microsoft Excel reopen UNVERIFIED."
            }
        if stage == "F3_04D":
            guidance = {
                "A1": "CURRENT 14 NOV 2026 — F3-04D SOSA equipment classifications complete",
                "B17": "33 ungraded: 18 common, 2 specialized, 13 held. Six relevant prior decisions retained. No SOSA source comparisons remain ungraded. Next separate Proceed: F3-05, 64 existing AAS comparisons only.",
                "A19": "Current four-donor classification standing",
                "B19": "Open Group SOSA: 76 colored + 45 held + 0 ungraded = 121. Four donors: 466 colored + 150 held + 0 ungraded = 616 source-bearing comparisons. AAS provisional colors still await F3-05 review.",
                "B21": "Targeted C239 2023 equipment/management/power passages, 2022 DSDM text and ten IDL files; ISA DMS original pages 24–26 for direction and comparison meaning. 33 decisions; no whole-corpus or runtime claim.",
                "B22": "Twenty new candidate colors. Reporting SHOULD recommendations remain qualified. Load/input versus source/output voltage corrected; design ratings, arming inputs, battery reserve and actual throughput remain distinct. Specialized feed roles and tamper alert retained.",
                "A23": "Preserved source and owner holds",
                "B23": "Nine SOSA source-hold families, six ISA questions, SAPIENT source/timestamp holds and all AAS findings retained. All nine case gaps remain unverified. No DIM/Profile adoption; AAS O1 waits for F3 gate. Clean Microsoft Excel reopen UNVERIFIED."
            }
        if stage == "F3_05":
            guidance = {
                "A1": "CURRENT 14 NOV 2026 — F3-05 Asset Administration Shell classifications complete",
                "B17": "64 existing comparisons: 37 common, 10 specialized, 2 native-only, 3 unresolved, 12 held. Next separate Proceed: F3-06 peer challenge and owner gate only.",
                "A19": "Current four-donor classification standing",
                "B19": "AAS: 52 colored + 12 held + 0 ungraded = 64. Four donors: 464 colored + 152 held + 0 ungraded = 616 source-bearing comparisons; 732 other explicit statuses.",
                "B21": "Targeted original Part 1/2, companion and four industrial-template evidence reviewed: 17 text/schema files and 16 PDF pages. All 64 prior comparisons reviewed; no new corpus or whole-source audit claim.",
                "B22": "34 classifications changed; 30 retained. Four old holds gain colors; six colors removed. Operation interfaces and typed structures remain qualified; generic carriers do not establish specific health, occurrence or connection meanings.",
                "A23": "Preserved source and owner holds",
                "B23": "Original source findings, editions, conflicts and case holds preserved. AAS remains active bounded PARTIAL; O1–O7 waits for F3 owner acceptance. No new rows or model adoption. Clean Microsoft Excel reopen UNVERIFIED."
            }
        edit_sheet("Summary", guidance)
        edit_sheet("Validation", guidance)
        edit_sheet("Legend", {
            "A1": "CURRENT LEGEND — " + label + ": candidate colors and explicit held comparisons",
            "A28": label + " classification checkpoint",
            "B28": ("F3-05: 37 common, 10 specialized, 2 native-only, 3 unresolved and 12 held AAS comparisons. "
                     "Colors grade qualified information, not exact mapping, observed implementation or adoption. Full source coverage remains bounded PARTIAL."
                     if stage == "F3_05" else
                     "Color grades potential information, not exact mapping or model adoption. "
                     "F3-04D: 33 SOSA equipment comparisons dispositioned; 20 new colors and 13 holds. All 121 source-bearing SOSA comparisons classified; original source completeness remains bounded PARTIAL."
                     if stage == "F3_04D" else
                     "Color grades potential information, not exact mapping or model adoption. "
                     "F3-04C: 21 SOSA comparisons dispositioned; 33 equipment comparisons remain ungraded. Seven new blue/amber candidates; all nine case gaps retain explicit holds."
                     if stage == "F3_04C" else
                     "Color grades potential information, not exact mapping or model adoption. "
                     "F3-04B: 33 SOSA exceptions dispositioned and one prior hold corrected; 54 comparisons remain ungraded. Blue/amber retain qualified information; explicit holds preserve unsupported relations."
                     if stage == "F3_04B" else
                     "Color grades potential information, not exact mapping or model adoption. "
                     "F3-03: SAPIENT fully dispositioned at comparison level; 103 SOSA comparisons still ungraded. "
                     "Purple timestamp conflict and white/banded explicit holds retain their reasons."
                     if stage == "F3_03" else
                     "F3-04A: 16 SOSA exceptions dispositioned, three prior decisions corrected; 87 later comparisons still ungraded. Blue/amber qualify useful information; explicit holds keep reasons. Color is not adoption."
                     if stage == "F3_04A" else "F3-02: 18 ISA comparisons dispositioned; 142 other comparisons still ungraded.")
        })
        register = old.readcells(prior, "DIM Register")
        regedits = {"M1": "SAPIENT H — candidate / color decision", "N1": "ISA I — candidate / color decision",
                    "O1": "SOSA J — candidate / color decision"}
        if stage == "F3_05":
            regedits["R1"] = "AAS G — current classification, source IDs and rationale"
        rowindex = {r["row_id"]: i + 2 for i, r in enumerate(m["rows"])}
        for r in records:
            idx = rowindex[r["row_id"]]
            regedits[cfg["register"] + str(idx)] = r["candidate_status"] + " — " + label + ": " + r["rationale"]
            ref = "P" + str(idx)
            regedits[ref] = register.get(ref, "") + " | " + label + " " + cfg["donor"] + ": " + ", ".join(r["source_ids"]) + "; " + r["decision_id"]
        edit_sheet("DIM Register", regedits)
        output = io.BytesIO()
        with zipfile.ZipFile(output, "w") as dst:
            for info in z.infolist():
                dst.writestr(info, replacements.get(info.filename, z.read(info.filename)))
    saved = output.getvalue()
    (D / BOOK).write_bytes(saved)
    sha = digest(saved)
    checkpoint = stage + "_CLASSIFICATION_SAVED_VERIFIED"
    m["currentEvidenceCheckpoint"] = checkpoint
    m["currentWorkbookSha256"] = sha
    m["workbookSnapshot"].update({"checkpoint": checkpoint, "sha256": sha,
        "currently_matches_readable_view": True, "lag": "ZERO: JSON, both CSVs, both readable comparisons and same 26-sheet XLSX",
        "textCheckpoint": stage + "_CLASSIFICATION_ONLY", "validation_file": cfg["evidence"] + "#/" + key + "/publication"})
    review["status"] = "SOURCE_DECISIONS_PUBLISHED__STOP_AT_CURRENT_STAGE"
    review["publication"] = {"workbook_sha256": sha, "previous_workbook_sha256": digest(prior),
        "affected_original_sheets": ["Master Crosswalk", "Summary", "Validation", "Legend", "DIM Register"],
        "unchanged_sheet_parts": 21, "grid_values_checked": 5664,
        "source_cells_changed": len(records), "colored_decisions": sum(bool(r["fill"]) for r in records),
        "explicit_no_fill_decisions": sum(not r["fill"] for r in records),
        "M00_M01_preserved": True, "M02_created": False,
        "actual_Microsoft_Excel_clean_open": "UNVERIFIED", "visual_render_review": "PENDING",
        "source_completeness_claim": "Targeted classification pass only; original bounded coverage retained."}
    aas = evidence if stage == "F3_05" else load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json")
    aas["master_state_current"].update({"checkpoint": checkpoint, "comparison_lag": 0})
    save(MASTER, m)
    save(cfg["evidence"], evidence)
    save("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json", aas)
    verify_f3(stage)


def verify_f3(stage="F3_02"):
    """Check actual saved cells/fills and exact preservation against archived bytes."""
    from collections import Counter
    from html.parser import HTMLParser
    cfg = f3_config(stage)
    key = stage + "_classification_review"
    rowkey = stage + "_" + cfg["donor"] + "_classification"
    label = stage.replace("_", "-")
    m = load(MASTER)
    e = load(cfg["evidence"])
    review = e[key]
    records = review["records"]
    base = json.loads(f3_baseline(MASTER, cfg["base"]))
    original_e = json.loads(f3_baseline(cfg["evidence"], cfg["base"]))
    allowed_metadata = {"master_state_current", "one_next"} if stage == "F3_05" else set()
    need({k: v for k, v in e.items() if k != key and k not in allowed_metadata} ==
         {k: v for k, v in original_e.items() if k not in allowed_metadata},
         "all original source findings, native locators and holds preserved")
    if stage == "F3_05":
        before_state, after_state = original_e["master_state_current"], e["master_state_current"]
        need({k: v for k, v in before_state.items() if k not in ("checkpoint", "comparison_lag", "next")} ==
             {k: v for k, v in after_state.items() if k not in ("checkpoint", "comparison_lag", "next")},
             "only current AAS handoff metadata updated")
        need(after_state["checkpoint"] == m["currentEvidenceCheckpoint"] and after_state["comparison_lag"] == 0
             and after_state["next"] == e["one_next"] == review["next"], "current AAS metadata is coherent")
    need(m["currentEvidenceCheckpoint"] == stage + "_CLASSIFICATION_SAVED_VERIFIED", "saved " + label + " checkpoint")
    need(len(records) == cfg["count"] and Counter(r["candidate_status"] for r in records) == cfg["counts"], "all source decisions")
    need(m["columns"] == base["columns"] and m["review_sections"] == base["review_sections"], "approved layout preserved")
    changed = {r["cell"]: r for r in records}
    need(len(changed) == cfg["count"] and len(m["rows"]) == 337 and len(m["review_grid"]) == 354, "stable identities and dimensions")
    indexed = {r["row_id"]: r for r in m["rows"]}
    for record in records:
        row = indexed[record["row_id"]]
        need(row["display"][cfg["column"]] == record["after"] and row[rowkey]["candidate_status"] ==
             record["candidate_status"] and record["source_ids"] and record["original_source_locators"],
             "source decision resolves to current stable row " + record["row_id"])
    for before, row in zip(base["rows"], m["rows"]):
        copied = dict(row)
        copied.pop(rowkey, None)
        copied["display"] = list(copied["display"])
        copied["display"][cfg["column"]] = before["display"][cfg["column"]]
        need(copied == before, "preserve all original row/case/donor/model evidence " + row["row_id"])
    for i, (before, after) in enumerate(zip(base["review_grid"], m["review_grid"]), 1):
        need(len(after) == 16, "all 16 columns")
        for j, (v0, v1) in enumerate(zip(before, after), 1):
            ref = addr(i, j)
            need(v1 == (changed[ref]["after"] if ref in changed else v0), "only authorized donor cells " + ref)
    for key in ("F2_5_color_reconciliation", "AAS10_color_reconciliation", "priorHolds", "caseEvidence", "adoptionPolicy"):
        need(m[key] == base[key], "preserve prior decisions " + key)
    need(source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv") == m["review_grid"] ==
         source_csv("ISA_Correction_Review_07NOV2026.csv"), "both CSV mirrors")
    class Table(HTMLParser):
        def __init__(self): super().__init__(convert_charrefs=True); self.rows = []; self.cell = None
        def handle_starttag(self, tag, attrs):
            if tag == "tr": self.row = []
            if tag in ("td", "th"): self.cell = ""; self.span = int(dict(attrs).get("colspan", 1))
        def handle_data(self, data):
            if self.cell is not None: self.cell += data
        def handle_endtag(self, tag):
            if tag in ("td", "th"): self.row += [self.cell] + [""] * (self.span - 1); self.cell = None
            if tag == "tr": self.rows.append(self.row)
    md = (D / "Master_Donor_Concept_to_DIM_Crosswalk.md").read_text()
    need(md == (D / "ISA_Correction_Review_07NOV2026.md").read_text(), "both readable comparisons")
    table = Table(); table.feed(md[md.index("<table>"):md.index("</table>") + 8])
    need(table.rows == m["review_grid"], "every readable comparison value")
    saved = (D / BOOK).read_bytes()
    need(digest(saved) == m["currentWorkbookSha256"] == m["workbookSnapshot"]["sha256"] ==
         review["publication"]["workbook_sha256"], "actual saved workbook hash")
    with zipfile.ZipFile(io.BytesIO(saved)) as z, zipfile.ZipFile(io.BytesIO(f3_baseline(BOOK, cfg["base"]))) as prior:
        paths = old.sheetpaths(z)
        need(z.testzip() is None and len(paths) == 26 and paths == old.sheetpaths(prior), "same 26-sheet workbook")
        changed_parts = {paths[n] for n in review["publication"]["affected_original_sheets"]}
        need(set(z.namelist()) == set(prior.namelist()), "same workbook parts")
        for name in z.namelist():
            if name not in changed_parts: need(z.read(name) == prior.read(name), "unchanged package part " + name)
            if name.endswith((".xml", ".rels")): ET.fromstring(z.read(name))
        register = old.readcells(saved, "DIM Register")
        for i, row in enumerate(m["rows"], 2):
            if rowkey in row:
                need(register["A" + str(i)] == row["row_id"] and
                     register[cfg["register"] + str(i)].startswith(row[rowkey]["candidate_status"]) and
                     label + "-" + row["row_id"] in register["P" + str(i)], "visible register classification " + row["row_id"])
        for sheet in review["publication"]["affected_original_sheets"]:
            xml = ET.fromstring(z.read(paths[sheet]))
            for rr in xml.find(q("sheetData")):
                nums = []
                for cc in rr.findall(q("c")):
                    n = 0
                    for ch in re.match(r"[A-Z]+", cc.get("r")).group(): n = n * 26 + ord(ch) - 64
                    nums.append(n)
                    need(cc.get("t") != "e", "no error cells in changed sheet " + sheet)
                need(nums == sorted(set(nums)), "ordered unique cells in changed sheet " + sheet)
        actual = old.readcells(saved, "Master Crosswalk")
        styles = ET.fromstring(z.read("xl/styles.xml"))
        xfs, fills = list(styles.find(q("cellXfs"))), list(styles.find(q("fills")))
        root = ET.fromstring(z.read(paths["Master Crosswalk"]))
        cells = {c.get("r"): c for c in root.iter(q("c"))}
        priorcells = {c.get("r"): c for c in ET.fromstring(prior.read(paths["Master Crosswalk"])).iter(q("c"))}
        for row in root.find(q("sheetData")):
            cols = []
            for cell in row.findall(q("c")):
                n = 0
                for char in re.match(r"[A-Z]+", cell.get("r")).group(): n = n * 26 + ord(char) - 64
                cols.append(n)
                need(cell.get("t") != "e", "no Excel error cells")
            need(cols == sorted(set(cols)), "ordered unique OOXML cells")
        for i, values in enumerate(m["review_grid"], 1):
            for j, expected in enumerate(values, 1):
                ref = addr(i, j)
                need(actual.get(ref, "") == expected, "saved cell value " + ref)
        for ref, cell in cells.items():
            if ref not in changed:
                need(cell.get("s") == priorcells[ref].get("s"), "preserved original style " + ref)
            else:
                xf = xfs[int(cell.get("s", "0"))]
                color = fills[int(xf.get("fillId", "0"))].find(".//" + q("fgColor")).get("rgb")
                if changed[ref]["fill"]:
                    need(color[-6:] == changed[ref]["fill"][1:], "source-backed actual candidate fill " + ref)
                else:
                    need(color[-6:] in ("FFFFFF", "F2F7FB"), "explicit hold has no classification fill " + ref)
        need(sum(bool(r["display"][j]) for r in m["rows"] for j in (6, 7, 8, 9)) == 1348, "all donor statuses visible")
    for name in ("M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx",
                 "M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx"):
        rel = "Manual_Workbook_Versions/" + name
        need((D / rel).read_bytes() == f3_baseline(rel, cfg["base"]), "frozen manual version " + name)
    need(not list((D / "Manual_Workbook_Versions").glob("M02*")), "no unapproved M02")
    need(m["nextOwnerAction"] == review["next"] == load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json")["one_next"], "one next action")
    if stage == "F3_03":
        initial = [r for r in records if r["review_set"] == "39_UNGRADED"]
        calibration = [r for r in records if r["review_set"] == "PRIOR_CLASSIFICATION_CALIBRATION"]
        need(len(initial) == 39 and len(calibration) == 12, "separate original exceptions from calibration")
        need(Counter(r["candidate_status"] for r in initial) == review["initial_39_status_counts"], "initial 39 outcomes")
        need(Counter(r["candidate_status"] for r in calibration) == review["calibration_change_status_counts"], "calibration outcomes")
        need(m["F3_02_classification"] == base["F3_02_classification"], "ISA F3-02 decisions preserved")
        observed = Counter()
        for row in m["rows"]:
            if rowkey in row:
                observed["colored" if row[rowkey]["fill"] else "held"] += 1
            elif "G" in row.get("F2_5_cell_classification", {}):
                observed["colored" if row["F2_5_cell_classification"]["G"]["requested_fill"] else "held"] += 1
        need(observed == {"colored": 65, "held": 50}, "115 current SAPIENT source decisions")
    if stage == "F3_04A":
        initial = [r for r in records if r["review_set"] == "16_UNGRADED"]
        calibration = [r for r in records if r["review_set"] == "PRIOR_CLASSIFICATION_CALIBRATION"]
        need(len(initial) == 16 and len(calibration) == 3, "bounded first SOSA packet")
        need(Counter(r["candidate_status"] for r in initial) == review["initial_16_status_counts"], "16 original exception outcomes")
        need(Counter(r["candidate_status"] for r in calibration) == review["calibration_change_status_counts"], "three prior classification corrections")
        for key in ("F3_02_classification", "F3_03_classification"):
            need(m[key] == base[key], "previous donor classifications preserved " + key)
        observed = Counter()
        for row in m["rows"]:
            if rowkey in row:
                observed["colored" if row[rowkey]["fill"] else "held"] += 1
            elif "I" in row.get("F2_5_cell_classification", {}):
                observed["colored" if row["F2_5_cell_classification"]["I"]["requested_fill"] else "held"] += 1
        need(observed == {"colored": 26, "held": 8}, "34 classified SOSA comparisons; 87 remain ungraded")
    if stage == "F3_04B":
        initial = [r for r in records if r["review_set"] == "33_UNGRADED"]
        calibration = [r for r in records if r["review_set"] == "PRIOR_CLASSIFICATION_CALIBRATION"]
        need(len(initial) == 33 and len(calibration) == 1, "bounded second SOSA packet")
        boundary = original_e["F3_04A_classification_review"]["next_packet_boundary"]["records"]
        need({r["row_id"] for r in initial} == {r["row_id"] for r in boundary}, "exact previously authorized 33 rows")
        need(Counter(r["candidate_status"] for r in initial) == review["initial_33_status_counts"], "33 original exception outcomes")
        need(Counter(r["candidate_status"] for r in calibration) == review["calibration_change_status_counts"], "one prior classification correction")
        need(calibration[0]["row_id"] == "S06-R019", "only relevant control-request calibration changed")
        for key in ("F3_02_classification", "F3_03_classification", "F3_04A_classification"):
            need(m[key] == base[key], "previous classification checkpoints preserved " + key)
        observed = Counter()
        for row in m["rows"]:
            current = row.get(rowkey) or row.get("F3_04A_OpenGroupSOSA_classification")
            if current:
                observed["colored" if current["fill"] else "held"] += 1
            elif "I" in row.get("F2_5_cell_classification", {}):
                observed["colored" if row["F2_5_cell_classification"]["I"]["requested_fill"] else "held"] += 1
        need(observed == {"colored": 49, "held": 18}, "67 classified SOSA comparisons; 54 remain ungraded")
        need(len(review["prior_calibration_retained"]) == 6, "six prior decisions explicitly retained")
        need(len(review["next_packet_boundary"]["records"]) == 21 and
             len(review["next_packet_boundary"]["outside_records"]) == 33, "next bounded packet and later remainder")
    if stage == "F3_04C":
        boundary = original_e["F3_04B_classification_review"]["next_packet_boundary"]["records"]
        need({r["row_id"] for r in records} == {r["row_id"] for r in boundary}, "exact authorized 21 comparisons")
        need(all(r["review_set"] == "21_UNGRADED" for r in records), "no prior classification changed")
        need(Counter(r["candidate_status"] for r in records) == review["initial_21_status_counts"], "21 original exception outcomes")
        cases = [r for r in records if r["row_id"].startswith("CASE-H")]
        need(len(cases) == 9 and all(r["candidate_status"] == "MIXED_OR_HELD" for r in cases), "nine real-case holds preserved")
        for key in ("F3_02_classification", "F3_03_classification", "F3_04A_classification", "F3_04B_classification"):
            need(m[key] == base[key], "prior classification checkpoint preserved " + key)
        observed = Counter()
        for row in m["rows"]:
            current = row.get(rowkey) or row.get("F3_04B_OpenGroupSOSA_classification") or row.get("F3_04A_OpenGroupSOSA_classification")
            if current:
                observed["colored" if current["fill"] else "held"] += 1
            elif "I" in row.get("F2_5_cell_classification", {}):
                observed["colored" if row["F2_5_cell_classification"]["I"]["requested_fill"] else "held"] += 1
        need(observed == {"colored": 56, "held": 32}, "88 classified SOSA comparisons; 33 remain ungraded")
        need(len(review["prior_calibration_retained"]) == 4, "four relevant earlier decisions retained")
        need(review["next_packet_boundary"]["records"] == original_e["F3_04B_classification_review"]["next_packet_boundary"]["outside_records"], "remaining 33 equipment comparisons unchanged")
    if stage == "F3_04D":
        boundary = original_e["F3_04C_classification_review"]["next_packet_boundary"]["records"]
        need({r["row_id"] for r in records} == {r["row_id"] for r in boundary}, "exact authorized 33 equipment comparisons")
        need(all(r["review_set"] == "33_UNGRADED" for r in records), "no earlier classifications changed")
        need(Counter(r["candidate_status"] for r in records) == review["initial_33_status_counts"], "33 source outcomes")
        for key in ("F3_02_classification", "F3_03_classification", "F3_04A_classification", "F3_04B_classification", "F3_04C_classification"):
            need(m[key] == base[key], "earlier checkpoint preserved " + key)
        observed = Counter()
        for row in m["rows"]:
            current = row.get(rowkey) or row.get("F3_04C_OpenGroupSOSA_classification") or row.get("F3_04B_OpenGroupSOSA_classification") or row.get("F3_04A_OpenGroupSOSA_classification")
            if current:
                observed["colored" if current["fill"] else "held"] += 1
            elif "I" in row.get("F2_5_cell_classification", {}):
                observed["colored" if row["F2_5_cell_classification"]["I"]["requested_fill"] else "held"] += 1
        need(observed == {"colored": 76, "held": 45}, "all 121 SOSA source comparisons classified")
        need(len(review["prior_calibration_retained"]) == 6, "six relevant prior decisions retained")
        need(review["census_after"]["ungraded"] == 0, "zero remaining classification exceptions; not source completeness")
        need(review["next_packet_boundary"]["step"] == "F3-05" and review["next_packet_boundary"]["source_bearing_count"] == 64, "next AAS classification boundary")
    if stage == "F3_05":
        prior_decisions = base["AAS10_color_reconciliation"]
        expected = {r["row_id"] for group in ("assignments", "held") for r in prior_decisions[group]}
        need({r["row_id"] for r in records} == expected, "exact 54 provisional colors and ten holds reviewed")
        need(all(r["review_set"] == "64_EXISTING_COMPARISONS" for r in records), "bounded AAS classification set")
        for prior_key in ("F3_02_classification", "F3_03_classification", "F3_04A_classification",
                          "F3_04B_classification", "F3_04C_classification", "F3_04D_classification"):
            need(m[prior_key] == base[prior_key], "other donor classifications preserved " + prior_key)
        need(sum(bool(r["fill"]) for r in records) == 52 and review["census_after"]["AAS"] ==
             {"source_bearing": 64, "colored": 52, "held": 12, "ungraded": 0}, "current AAS census")
        need(m["F3_05_classification"]["census_after"] == review["census_after"], "master and evidence census")
        need(m["AASEvidence"] == base["AASEvidence"], "AAS source coverage and owner disposition unchanged")
    print(f"PASS {label}: {len(records)} source-backed dispositions; 5664 actual saved values and both CSV/Markdown mirrors.")
    print("PASS: original 337 rows/26 sheets, 21 untouched worksheet parts, other donor/case evidence and M00/M01 preserved.")
    print("LIMIT: targeted classification review only; clean Microsoft Excel reopen remains unverified; stop at current stage.")


def publish_f3_02():
    return publish_f3("F3_02")


def verify_f3_02():
    return verify_f3("F3_02")


F3_PEER_BASE = '4fed5c76ecd6610054c731433c07fefab0779027'
F3_PEER_KEY = 'F3_06_classification'
F3_PEER_FILES = ('ISA21_Source_First_31_Targets_25_Findings_6_Questions_09NOV2026.json',
    'SAP01_Original_Corpus_Coverage_12NOV2026.json',
    'SOSA_G4_F_192_Heading_Source_and_Master_Ledger_11NOV2026.json',
    'AAS01_Original_Source_Corpus_Coverage_13NOV2026.json')


def publish_f3_06():
    """Apply the bounded multi-donor peer decisions to the existing workbook package."""
    import html
    m = load(MASTER); review = m[F3_PEER_KEY]; records = review['records']
    need(m['currentEvidenceCheckpoint'] == 'F3_06_SOURCE_CLASSIFIED_PENDING_SAME_XLSX', 'F3-06 source checkpoint')
    prior = (D / BOOK).read_bytes()
    need(prior == f3_baseline(BOOK, F3_PEER_BASE), 'exact archived pre-F3-06 workbook')
    grid = m['review_grid']
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.csv', 'ISA_Correction_Review_07NOV2026.csv'):
        with (D / name).open('w', newline='', encoding='utf-8') as f: csv.writer(f, lineterminator='\n').writerows(grid)
    table = ['<table><thead><tr>']
    for idx, span in ((0,4),(4,6),(10,5),(15,1)): table.append(f'<th colspan="{span}">{html.escape(grid[0][idx])}</th>')
    table += ['</tr><tr>'+''.join('<th>'+html.escape(v)+'</th>' for v in grid[1])+'</tr></thead><tbody>']
    for idx, row in enumerate(grid[2:],2):
        table.append('<tr><th colspan="16">'+html.escape(row[0])+'</th></tr>' if idx in m['review_sections'] else '<tr>'+''.join('<td>'+html.escape(v)+'</td>' for v in row)+'</tr>')
    table += ['</tbody></table>']
    banner = ('# CURRENT — F3-06 peer reconciliation published; owner acceptance pending (15 November 2026)\n\n'
        '79 classifications corrected: ISA 64, SAPIENT 14, AAS 1; Open Group SOSA retained. '
        '616 source comparisons: 508 colored, 108 held, zero ungraded. 732 other donor positions retain explicit statuses. '
        '337 rows, 26 sheets and the approved column order are preserved. Source completeness remains bounded; '
        'actual Microsoft Excel clean reopen is PENDING. '+review['next']+'\n\nEarlier checkpoint banners are historical.\n\n---\n\n')
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        before=f3_baseline(name,F3_PEER_BASE).decode()
        (D/name).write_text(banner+before[:before.index('<table>')]+'\n'.join(table)+before[before.index('</table>')+8:],encoding='utf-8')
    style_ids={'COMMON_CANDIDATE':528,'SPECIALIZED_CANDIDATE':529,'NATIVE_ONLY_EVIDENCE':530,'UNRESOLVED_CANDIDATE':531}
    rowindex={r['row_id']:i for i,r in enumerate(m['rows'])}
    with zipfile.ZipFile(io.BytesIO(prior)) as z:
        paths=old.sheetpaths(z); replacements={}
        def edit(name, edits, styles=None):
            root=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in root.iter(q('c'))}
            for ref,value in edits.items():
                if ref not in cells:
                    need(name=='DIM Register' and ref.startswith('P'),'only blank register provenance may be materialized')
                    rr=next(r for r in root.find(q('sheetData')) if r.get('r')==ref[1:])
                    cell=ET.Element(q('c'),{'r':ref,'s':cells['N'+ref[1:]].get('s','0')})
                    rr.insert(next((i for i,c in enumerate(rr) if c.get('r','Z0').rstrip('0123456789')>'P'),len(rr)),cell);cells[ref]=cell
                f3_put(cells[ref],value)
                if styles and ref in styles:cells[ref].set('s',str(styles[ref]))
            for rr in root.find(q('sheetData')):
                affected=[str(value) for ref,value in edits.items() if re.search(r'\d+$',ref).group()==rr.get('r')]
                if affected:
                    width=40 if name=='Master Crosswalk' else 95 if name in ('Summary','Validation','Legend') else 65
                    height=max(len(textwrap.wrap(t,width=width))*12+18 for t in affected)
                    rr.set('ht',str(min(409.5,max(float(rr.get('ht','15')),height))));rr.set('customHeight','1')
            replacements[paths[name]]=ET.tostring(root,encoding='utf-8',xml_declaration=True)
        styles={r['cell']:style_ids[r['candidate_status']] if r['fill'] else 526+rowindex[r['row_id']]%2 for r in records}
        edit('Master Crosswalk',{r['cell']:r['after'] for r in records},styles)
        guidance={'A1':'CURRENT 15 NOV 2026 — F3-06 classification reconciliation; owner acceptance pending',
            'B17':'79 corrections: ISA 64, SAPIENT 14, AAS 1. 46 holds gain supported classifications, two colors removed, 31 existing colors revised. No model adoption.',
            'A19':'Current four-donor comparison standing',
            'B19':'616 source-bearing comparisons: 508 colored, 108 held, zero ungraded. ISA 309/7; SAPIENT 71/44; SOSA 76/45; AAS 52/12 (colored/held). 732 other explicit statuses.',
            'B21':'162 rows with multiple source-bearing donors compared. Selected original ISA/BSI passages, two pinned SAPIENT schemas and AAS descriptor text reopened. Existing source coverage/edition/access limits remain; no full-corpus audit.',
            'B22':'Colors grade qualified information needs, not exact cross-donor equivalence, source requiredness or observed equipment. Prior decisions, six ISA questions, nine SOSA hold families and nine case holds retained.',
            'A23':'Owner acceptance and remaining limits',
            'B23':'STOP for owner acceptance of F3. Clean Microsoft Excel reopen/no-repair remains PENDING. AAS remains bounded PARTIAL; native-first O1–O7 requires separate authorization. No new rows, model, UI or deployment changes.'}
        edit('Summary',guidance);edit('Validation',guidance)
        edit('Legend',{'A1':'CURRENT LEGEND — F3-06 qualified candidates and explicit holds','A28':'F3-06 peer reconciliation','B28':'508 colored and 108 held source comparisons; zero ungraded. Common does not mean mandatory, equivalent or observed. Native-only retains encoding evidence; purple and no-fill preserve exact questions. Owner acceptance and clean Excel reopen pending.'})
        priorreg=old.readcells(prior,'DIM Register');reg={};register={'AAS':'R','SAPIENT':'M','ISA':'N','OpenGroupSOSA':'O'}
        for r in records:
            n=str(rowindex[r['row_id']]+2);reg[register[r['donor_key']]+n]=r['candidate_status']+' — F3-06: '+r['rationale']
            ref='P'+n;reg[ref]=reg.get(ref,priorreg.get(ref,''))+' | '+r['decision_id']+': '+', '.join(r['source_ids'])
        edit('DIM Register',reg)
        output=io.BytesIO()
        with zipfile.ZipFile(output,'w') as dst:
            for info in z.infolist():dst.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    saved=output.getvalue();(D/BOOK).write_bytes(saved);sha=digest(saved)
    m['currentEvidenceCheckpoint']='F3_06_CLASSIFICATION_SAVED_VERIFIED';m['currentWorkbookSha256']=sha
    m['workbookSnapshot'].update(checkpoint=m['currentEvidenceCheckpoint'],sha256=sha,currently_matches_readable_view=True,lag='ZERO: JSON, both CSVs, both readable comparisons and same 26-sheet XLSX',textCheckpoint='F3_06_PEER_CLASSIFICATION_ONLY',validation_file=MASTER+'#/F3_06_classification/publication')
    review['status']='PUBLISHED_CLASSIFICATION_RECONCILIATION__OWNER_ACCEPTANCE_PENDING'
    review['publication']={'workbook_sha256':sha,'previous_workbook_sha256':digest(prior),'affected_original_sheets':['Master Crosswalk','Summary','Validation','Legend','DIM Register'],'unchanged_sheet_parts':21,'grid_values_checked':5664,'source_cells_changed':len(records),'M00_M01_preserved':True,'M02_created':False,'actual_Microsoft_Excel_clean_open':'PENDING_NOT_AVAILABLE_IN_THIS_RUNTIME','visual_render_review':'PENDING','remote_publication':'PENDING'}
    save(MASTER,m)
    a=load(F3_PEER_FILES[-1]);a['master_state_current'].update(checkpoint=m['currentEvidenceCheckpoint'],comparison_lag=0);save(F3_PEER_FILES[-1],a)
    verify_f3_06()


def verify_f3_06():
    """Read saved values/fills and prove scope preservation against the archived checkpoint."""
    import copy
    from collections import Counter
    from html.parser import HTMLParser
    m=load(MASTER);review=m[F3_PEER_KEY];base=json.loads(f3_baseline(MASTER,F3_PEER_BASE))
    need(m['currentEvidenceCheckpoint']=='F3_06_CLASSIFICATION_SAVED_VERIFIED','F3-06 saved checkpoint')
    records=review['records'];changed={r['cell']:r for r in records}
    need(len(records)==len(changed)==79 and Counter(r['donor_key'] for r in records)=={'ISA':64,'SAPIENT':14,'AAS':1},'bounded 79 decisions')
    need(m['columns']==base['columns'] and m['review_sections']==base['review_sections'] and len(m['rows'])==337 and len(m['review_grid'])==354,'original row/column layout')
    for before,row in zip(base['rows'],m['rows']):
        copied=copy.deepcopy(row)
        for donor,col in (('AAS',6),('SAPIENT',7),('ISA',8),('OpenGroupSOSA',9)):
            copied.pop('F3_06_'+donor+'_classification',None);copied['display'][col]=before['display'][col]
        need(copied==before,'all original row evidence preserved '+row['row_id'])
    for k,v in base.items():
        if k not in ('rows','review_grid','currentEvidenceCheckpoint','currentWorkbookSha256','workbookSnapshot','nextOwnerAction'):need(m[k]==v,'original master evidence '+k)
    for i,(a,b) in enumerate(zip(base['review_grid'],m['review_grid']),1):
        need(len(b)==16,'16 columns')
        for j,(v0,v1) in enumerate(zip(a,b),1):
            cell=addr(i,j);need(v1==(changed[cell]['after'] if cell in changed else v0),'authorized values only '+cell)
    for r in records:
        row=next(x for x in m['rows'] if x['row_id']==r['row_id']);key='F3_06_'+r['donor_key']+'_classification'
        need(row[key]['candidate_status']==r['candidate_status'] and r['source_ids'] and r['original_source_locators'],'native evidence '+r['row_id'])
    for name in F3_PEER_FILES:
        before=json.loads(f3_baseline(name,F3_PEER_BASE));after=load(name);after.pop('F3_06_peer_review')
        if name==F3_PEER_FILES[-1]:
            for k in ('one_next','master_state_current'):after[k]=before[k]
            if 'AAS_O1_source_opportunities' in after:
                after.pop('AAS_O1_source_opportunities');after.pop('F3_owner_acceptance')
                after['status']=before['status']
            after['F3_05_classification_review']['publication']=before['F3_05_classification_review']['publication']
        need(after==before,'all prior native source records and holds '+name)
    need(source_csv('Master_Donor_Concept_to_DIM_Crosswalk.csv')==m['review_grid']==source_csv('ISA_Correction_Review_07NOV2026.csv'),'both CSV mirrors')
    class Table(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.cell=None
        def handle_starttag(self,tag,attrs):
            if tag=='tr':self.row=[]
            if tag in ('td','th'):self.cell='';self.span=int(dict(attrs).get('colspan',1))
        def handle_data(self,data):
            if self.cell is not None:self.cell+=data
        def handle_endtag(self,tag):
            if tag in ('td','th'):self.row += [self.cell]+['']*(self.span-1);self.cell=None
            if tag=='tr':self.rows.append(self.row)
    md=(D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_text();need(md==(D/'ISA_Correction_Review_07NOV2026.md').read_text(),'both Markdown mirrors')
    t=Table();t.feed(md[md.index('<table>'):md.index('</table>')+8]);need(t.rows==m['review_grid'],'readable table values')
    saved=(D/BOOK).read_bytes();need(digest(saved)==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==review['publication']['workbook_sha256'],'saved workbook hash')
    with zipfile.ZipFile(io.BytesIO(saved)) as z,zipfile.ZipFile(io.BytesIO(f3_baseline(BOOK,F3_PEER_BASE))) as prior:
        paths=old.sheetpaths(z);need(paths==old.sheetpaths(prior) and len(paths)==26 and z.testzip() is None,'same valid 26-sheet package')
        parts={paths[n] for n in review['publication']['affected_original_sheets']};need(z.namelist()==prior.namelist(),'package order and parts')
        for name in z.namelist():
            if name not in parts:need(z.read(name)==prior.read(name),'untouched part '+name)
            if name.endswith(('.xml','.rels')):ET.fromstring(z.read(name))
        for name in paths:
            xml=ET.fromstring(z.read(paths[name]))
            for rr in xml.find(q('sheetData')):
                nums=[]
                for c in rr.findall(q('c')):
                    n=0
                    for ch in re.match('[A-Z]+',c.get('r')).group():n=n*26+ord(ch)-64
                    nums.append(n);need(c.get('t')!='e','no error cells '+name)
                need(nums==sorted(set(nums)),'ordered unique cells '+name)
        actual=old.readcells(saved,'Master Crosswalk')
        for i,row in enumerate(m['review_grid'],1):
            for j,v in enumerate(row,1):need(actual.get(addr(i,j),'')==v,'saved value '+addr(i,j))
        root=ET.fromstring(z.read(paths['Master Crosswalk']));cells={c.get('r'):c for c in root.iter(q('c'))};oldcells={c.get('r'):c for c in ET.fromstring(prior.read(paths['Master Crosswalk'])).iter(q('c'))}
        styles=ET.fromstring(z.read('xl/styles.xml'));xfs=list(styles.find(q('cellXfs')));fills=list(styles.find(q('fills')))
        final=review['final_source_cell_dispositions'];need(len(final)==616 and len({r['cell'] for r in final})==616,'all 616 final source dispositions')
        for r in final:
            c=cells[r['cell']];xf=xfs[int(c.get('s','0'))];fg=fills[int(xf.get('fillId','0'))].find('.//'+q('fgColor'));color=fg.get('rgb','')[-6:] if fg is not None else ''
            need(color==(r['fill'][1:] if r['fill'] else color) and (r['fill'] or color in ('FFFFFF','F2F7FB')),'actual final classification fill '+r['cell'])
        for ref,c in cells.items():
            if ref not in changed:need(c.get('s')==oldcells[ref].get('s'),'untouched style '+ref)
        reg=old.readcells(saved,'DIM Register');rowindex={r['row_id']:i+2 for i,r in enumerate(m['rows'])};rc={'AAS':'R','ISA':'N','SAPIENT':'M','OpenGroupSOSA':'O'}
        for r in records:
            n=str(rowindex[r['row_id']]);need(reg[rc[r['donor_key']]+n].startswith(r['candidate_status']) and r['decision_id'] in reg['P'+n],'saved register '+r['cell'])
    need(sum(bool(r['display'][j].strip()) for r in m['rows'] for j in (6,7,8,9))==1348,'337 by four readable statuses')
    for donor,expected in (('ISA',316),('SAPIENT',115),('OpenGroupSOSA',121),('AAS',64)):
        ds=[r for r in final if r['donor_key']==donor];need(len(ds)==expected and dict(Counter(r['candidate_status'] for r in ds))==review['census_after'][donor]['statuses'],'independent donor census '+donor)
    need(sum(bool(r['fill']) for r in final)==508 and sum(not r['fill'] for r in final)==108 and len(review['peer_comparisons'])==162,'final classifications and peer set')
    for name in ('M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx','M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx'):
        rel='Manual_Workbook_Versions/'+name;need((D/rel).read_bytes()==f3_baseline(rel,F3_PEER_BASE),'immutable '+name)
    need(not list((D/'Manual_Workbook_Versions').glob('M02*')),'no unapproved M02')
    need(m['nextOwnerAction']==review['next']==load(F3_PEER_FILES[-1])['one_next'],'one owner gate')
    print('PASS F3-06: 79 corrections; all 616 actual saved source fills; 5664 values and both CSV/Markdown mirrors.')
    print('PASS: 337 rows, 26 sheets, 21 unchanged worksheet parts, original evidence/holds/case cells and M00/M01 preserved.')
    if 'AAS_O1_source_opportunities' in m:
        verify_aas_o1(m)
        print('LIMIT: F3 accepted; AAS bounded PARTIAL. Excel clean reopen pending; workbook routing text historical.')
    else:
        print('LIMIT: targeted source review only. Owner acceptance and actual Microsoft Excel clean reopen remain pending.')


def verify_aas_o1(m):
    """Recompute source accountability while protecting the accepted grid and original evidence."""
    import copy
    from collections import Counter
    a=load(F3_PEER_FILES[-1]);o=a['AAS_O1_source_opportunities']
    prior=json.loads(f3_baseline(MASTER,'23c2dcd292b7e77118bcd23feb11fd9223bd61f1'))
    restored=copy.deepcopy(m);restored.pop('AAS_O1_source_opportunities')
    restored['nextOwnerAction']=prior['nextOwnerAction']
    restored['F3_06_classification']=copy.deepcopy(m['F3_06_classification'])
    for k in ('owner_acceptance','status','next'):restored['F3_06_classification'][k]=prior['F3_06_classification'][k]
    restored['F3_06_classification'].pop('owner_acceptance_record')
    need(restored==prior,'O1 changes only authorized master routing metadata')
    originals={x['source_id']:x for n in range(2,10) for x in a['AAS%02d'%n]['original_items']}
    rs=o['finding_records'];need(len(rs)==len(originals)==310 and {r['source_id'] for r in rs}==set(originals),'all 310 original IDs once')
    unc={r['source_id']:r for r in a['AAS10']['finding_accountability']['uncited_dispositions']}
    need(len(unc)==53,'historical 53 retained')
    rx=re.compile(r'AAS0[2-9]-[NS]\d{3}')
    for r in rs:
        sid=r['source_id'];x=originals[sid]
        need(digest(json.dumps(x,sort_keys=True,ensure_ascii=False).encode())==r['original_record_sha256'],'original source content '+sid)
        retained=[row['row_id'] for row in m['rows'] if sid in rx.findall(json.dumps(row))]
        current=[row['row_id'] for row in m['rows'] if sid in rx.findall(row['display'][6])]
        decisions=[row['row_id'] for row in m['rows'] if sid in row.get('F3_06_AAS_classification',row.get('F3_05_AAS_classification',{})).get('source_ids',[])]
        need(current==decisions==[v['row_id'] for v in r['current_cell_links']] and retained==r['retained_master_row_ids'],'recomputed row links '+sid)
        need(r['disposition']==('current_decision_linked' if current else 'prior_evidence_only' if retained else 'historically_uncited'),'current disposition '+sid)
        need(r['historical_53']==(sid in unc) and not r['DIM_Profile_adopted'] and not r['new_source_audit_claimed'],'scope '+sid)
        if sid in unc:need(r['prior_uncited_disposition']==unc[sid],'preserved prior disposition '+sid)
    need(Counter(r['disposition'] for r in rs)=={'current_decision_linked':99,'prior_evidence_only':158,'historically_uncited':53},'independent finding census')
    final=[r for r in m[F3_PEER_KEY]['final_source_cell_dispositions'] if r['donor_key']=='AAS']
    need(len(o['classification_records'])==len(final)==64,'64 AAS classification links')
    for r,c in zip(o['classification_records'],final):
        need((r['row_id'],r['cell'],r['current_status'],r['current_fill'])==(c['row_id'],c['cell'],c['candidate_status'],c['fill']),'accepted AAS classification '+r['row_id'])
    need(a['one_next']==o['one_next']==m['nextOwnerAction'] and m[F3_PEER_KEY]['owner_acceptance']=='ACCEPTED_WITH_RECORDED_LIMITATIONS','accepted F3 and O2 stop boundary')
    print('PASS AAS O1: all 310 findings reconciled: 99 current / 158 retained-row-only / 53 historical uncited; 64 classifications unchanged.')


AAS_O2_BASE='1329bafed27858a967781b1f702eb48895dc443a'

def publish_aas_o2():
    """Extend the same saved package with source-qualified candidate rows; preserve original parts."""
    import copy, html
    m=load(MASTER);a=load(F3_PEER_FILES[-1]);o=a['AAS_O2_native_review'];grid=m['review_grid']
    prior=(D/BOOK).read_bytes();need(prior==f3_baseline(BOOK,AAS_O2_BASE),'exact archived pre-O2 workbook')
    need(m['currentEvidenceCheckpoint']=='AAS_O2_SOURCE_DECISIONS_PENDING_SAME_XLSX','O2 source checkpoint')
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/name).open('w',newline='',encoding='utf-8') as f:csv.writer(f,lineterminator='\n').writerows(grid)
    table=['<table><thead><tr>']
    for idx,span in ((0,4),(4,6),(10,5),(15,1)):table.append(f'<th colspan="{span}">{html.escape(grid[0][idx])}</th>')
    table+=['</tr><tr>'+''.join('<th>'+html.escape(v)+'</th>' for v in grid[1])+'</tr></thead><tbody>']
    for i,row in enumerate(grid[2:],2):table.append('<tr><th colspan="16">'+html.escape(row[0])+'</th></tr>' if i in m['review_sections'] else '<tr>'+''.join('<td>'+html.escape(v)+'</td>' for v in row)+'</tr>')
    table+=['</tbody></table>']
    banner='# CURRENT — F3 accepted; AAS O2 native-first review complete (15 November 2026)\n\nEight provisional information-need rows added after all 75 AAS02/AAS03 findings were dispositioned. Original 337 rows and 616 accepted F3 classifications unchanged. Current total: 345 information rows, 624 source-bearing comparisons (516 colored / 108 held), 26 sheets. Candidates are not adopted classes or Profile requirements. AAS source coverage remains bounded PARTIAL; Microsoft Excel clean reopen remains pending. Next: owner Proceed for O3 only. Earlier checkpoint banners and counts are historical.\n\n---\n\n'
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        oldtext=f3_baseline(name,AAS_O2_BASE).decode();(D/name).write_text(banner+oldtext[:oldtext.index('<table>')]+'\n'.join(table)+oldtext[oldtext.index('</table>')+8:],encoding='utf-8')
    with zipfile.ZipFile(io.BytesIO(prior)) as z:
        paths=old.sheetpaths(z);replacements={}
        def edited(name,changes):
            rt=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in rt.iter(q('c'))}
            for ref,value in changes.items():need(ref in cells,'existing guidance cell '+ref);f3_put(cells[ref],value)
            for rr in rt.find(q('sheetData')):
                vals=[v for k,v in changes.items() if re.search(r'\d+$',k).group()==rr.get('r')]
                if vals:rr.set('ht',str(min(409.5,max(float(rr.get('ht',15)),max(len(textwrap.wrap(v,95))*12+18 for v in vals)))));rr.set('customHeight','1')
            replacements[paths[name]]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));sd=rt.find(q('sheetData'));templates={int(r.get('r')):r for r in sd}
        def make_row(template,number,values):
            rr=copy.deepcopy(template);rr.set('r',str(number))
            for c in list(rr):rr.remove(c)
            styles={re.match('[A-Z]+',c.get('r')).group():c.get('s','0') for c in template}
            for j,v in enumerate(values,1):
                col=re.match('[A-Z]+',addr(number,j)).group();c=ET.SubElement(rr,q('c'),{'r':addr(number,j),'s':styles.get(col,'526')});f3_put(c,str(v))
            return rr
        divider=make_row(templates[351],355,grid[354]);sd.append(divider)
        merges=rt.find(q('mergeCells'));need(merges is not None,'existing topic merges');ET.SubElement(merges,q('mergeCell'),{'ref':'A355:P355'});merges.set('count',str(len(merges)))
        for n,row in enumerate(m['rows'][337:],356):
            rr=make_row(templates[354],n,row['display']);rr.set('ht','240');rr.set('customHeight','1')
            for c in rr:
                col=re.match('[A-Z]+',c.get('r')).group()
                if col in ('G','H','I','J'):c.set('s','526' if n%2==0 else '527')
                if col=='G':c.set('s','528' if row['AAS_O2_source_correspondence']['candidate_status']=='COMMON_CANDIDATE' else '529')
            sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:P363')
        af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A2:P363')
        replacements[paths['Master Crosswalk']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['DIM Register']));sd=rt.find(q('sheetData'));template=list(sd)[-1]
        for n,row in enumerate(m['rows'][337:],339):
            c=row['AAS_O2_source_correspondence'];ids=', '.join(c['source_ids'])
            vals=[row['row_id'],row['label'],row['definition'],row['status'],row['source_review_status'],row['master_inclusion'],row['dim_adoption'],'','Not assessed here','','Not assessed here','AAS pinned Part 1 v3.2 targeted text; no observed case','Not assessed here','Not assessed here','Not assessed here','O2 sources: '+ids,ids+'; '+c['relation']+'; '+c['reason_for_separate_candidate'],c['candidate_status']+' — '+c['native_meaning']]
            rr=make_row(template,n,vals);rr.set('ht','240');rr.set('customHeight','1');sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:R346');af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A1:R346')
        replacements[paths['DIM Register']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        guidance={'A1':'CURRENT 15 NOV 2026 — F3 accepted; AAS O2 complete','B17':'O2: 75 native findings dispositioned; eight provisional information-need rows added. All 337 earlier rows and 616 accepted classifications retained unchanged. No model adoption.','B19':'345 information rows; 624 source comparisons: 516 colored, 108 held. AAS 60 colored / 12 held across 72 comparisons. Other 756 four-donor positions retain explicit statuses.','B21':'O2 reopened selected original Part 1 passages supporting 73 finding records; two original audit records reused. No whole-file, figure, corpus or runtime completeness claim.','B22':'New candidates cover digital records, administration, template provenance, applied data specifications, information aspects, logical relationships, labels and supporting content. Existing source holds and four-case limits retained.','A23':'Next step and remaining limits','B23':'Await owner Proceed for O3 only: declarations, events, time and encodings. AAS remains active bounded PARTIAL. Actual Microsoft Excel clean reopen/no-repair remains pending. F3 is accepted.','B28':'O2 current saved checkpoint: 5,808 grid values, eight new AAS classifications, 26 sheets; original rows, source evidence and M00/M01 preserved. See existing source ledger for verification scope.'}
        edited('Summary',guidance);edited('Validation',guidance)
        edited('Legend',{'A1':'CURRENT LEGEND — F3 accepted; O2 candidate additions','B23':'Current: 516 colored / 108 held source comparisons. Earlier F2/F3 counts are historical.','A28':'AAS O2 additions and current boundary','B28':'Eight new source-qualified candidates: seven common (blue), one specialized (amber). Total 624 source comparisons, 516 colored / 108 held. Common does not mean mandatory, adopted, exact-equivalent or observed. Next O3; Excel clean reopen pending.'})
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as dst:
            for info in z.infolist():dst.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    saved=buf.getvalue();(D/BOOK).write_bytes(saved);sha=digest(saved)
    m['currentEvidenceCheckpoint']='AAS_O2_SAVED_VERIFIED';m['currentWorkbookSha256']=sha;m['workbookSnapshot'].update(checkpoint=m['currentEvidenceCheckpoint'],sha256=sha,currently_matches_readable_view=True,lag='ZERO: 363x16 grid and current O2 owner routing',textCheckpoint='AAS_O2_NATIVE_CANDIDATES',validation_file=F3_PEER_FILES[-1]+'#/AAS_O2_native_review/publication')
    m['AAS_O2_native_review']['status']='O2_COMPLETE__O3_PENDING_OWNER_PROCEED'
    o['status']='O2_COMPLETE__O3_PENDING_OWNER_PROCEED';o['publication']={'workbook_sha256':sha,'previous_workbook_sha256':digest(prior),'affected_original_sheets':['Master Crosswalk','DIM Register','Summary','Validation','Legend'],'unchanged_sheet_parts':21,'grid_values':5808,'new_candidate_cells':['G'+str(i) for i in range(356,364)],'existing_values_and_fills':'UNCHANGED','M00_M01_preserved':True,'M02_created':False,'actual_Microsoft_Excel_clean_reopen':'PENDING','visual_review':'PENDING','remote_publication':'PENDING'}
    a['status']='AAS_ACTIVE_BOUNDED_PARTIAL__O2_COMPLETE';a['master_state_current'].update(checkpoint=m['currentEvidenceCheckpoint'],comparison_lag=0,status='O2_COMPLETE__O3_PENDING',workbook_metadata_lag='ZERO: current O2 guidance refreshed; labeled historical checkpoints retained.')
    save(MASTER,m);save(F3_PEER_FILES[-1],a);verify_aas_o2()


def verify_aas_o2():
    """Check new native decisions and every saved comparison; preserve the accepted baseline."""
    import copy
    from collections import Counter
    from html.parser import HTMLParser
    m=load(MASTER);base=json.loads(f3_baseline(MASTER,AAS_O2_BASE));a=load(F3_PEER_FILES[-1]);ab=json.loads(f3_baseline(F3_PEER_FILES[-1],AAS_O2_BASE));o=a['AAS_O2_native_review']
    need(m['currentEvidenceCheckpoint']=='AAS_O2_SAVED_VERIFIED','O2 saved checkpoint')
    need(m['rows'][:337]==base['rows'] and m['review_grid'][:354]==base['review_grid'],'all original rows/case values/classifications/source evidence unchanged')
    need(m['columns']==base['columns'] and m['review_sections']==base['review_sections']+[354],'approved columns and appended topic only')
    need(len(m['rows'])==345 and len(m['review_grid'])==363 and all(len(r)==16 for r in m['review_grid']),'current dimensions')
    allowed={'rows','review_grid','review_sections','counts','currentEvidenceCheckpoint','currentWorkbookSha256','workbookSnapshot','nextOwnerAction'}
    for k,v in base.items():
        if k not in allowed:need(m[k]==v,'prior master field '+k)
    for k,v in base['counts'].items():
        if k!='informationRows':need(m['counts'][k]==v,'preserved historical count '+k)
    restored=copy.deepcopy(a);restored.pop('AAS_O2_native_review')
    for k in ('status','one_next','master_state_current'):restored[k]=ab[k]
    need(restored==ab,'all prior AAS findings/holds/F3/O1 records unchanged')
    native={x['source_id']:x for st in ('AAS02','AAS03') for x in a[st]['original_items']};rs=o['records']
    need(len(rs)==75 and {r['source_id'] for r in rs}==set(native),'75 unique original finding dispositions')
    rowids={r['row_id'] for r in m['rows']}
    for r in rs:
        need(digest(json.dumps(native[r['source_id']],sort_keys=True,ensure_ascii=False).encode())==r['original_record_sha256'],'unchanged original '+r['source_id'])
        need(set(r['row_ids'])<=rowids and r['rationale'] and r['relation'] and not r['DIM_Profile_adopted'],'qualified disposition '+r['source_id'])
    new=m['rows'][337:];need([r['row_id'] for r in new]==o['new_candidate_row_ids'] and len(set(rowids))==345,'eight stable new candidate IDs')
    need(Counter(r['AAS_O2_source_correspondence']['candidate_status'] for r in new)=={'COMMON_CANDIDATE':7,'SPECIALIZED_CANDIDATE':1},'new classifications')
    for r in new:
        c=r['AAS_O2_source_correspondence'];need(set(c['source_ids'])<=set(native) and c['reason_for_separate_candidate'] and not c['DIM_Profile_adopted'],'native candidate evidence '+r['row_id'])
        need(all(r['display'][j].strip() for j in range(16)),'explicit new-row statuses')
    need(source_csv('Master_Donor_Concept_to_DIM_Crosswalk.csv')==m['review_grid']==source_csv('ISA_Correction_Review_07NOV2026.csv'),'both CSV mirrors')
    md=(D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_text();need(md==(D/'ISA_Correction_Review_07NOV2026.md').read_text(),'both readable mirrors')
    class Table(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.cell=None
        def handle_starttag(self,t,attrs):
            if t=='tr':self.row=[]
            if t in ('td','th'):self.cell='';self.span=int(dict(attrs).get('colspan',1))
        def handle_data(self,d):
            if self.cell is not None:self.cell+=d
        def handle_endtag(self,t):
            if t in ('td','th'):self.row += [self.cell]+['']*(self.span-1);self.cell=None
            if t=='tr':self.rows.append(self.row)
    tab=Table();tab.feed(md[md.index('<table>'):md.index('</table>')+8]);need(tab.rows==m['review_grid'],'readable table values')
    saved=(D/BOOK).read_bytes();prior=f3_baseline(BOOK,AAS_O2_BASE);need(digest(saved)==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==o['publication']['workbook_sha256'],'saved hash')
    with zipfile.ZipFile(io.BytesIO(saved)) as z,zipfile.ZipFile(io.BytesIO(prior)) as bz:
        paths=old.sheetpaths(z);need(paths==old.sheetpaths(bz) and len(paths)==26 and z.testzip() is None,'same 26-sheet valid package')
        affected={paths[n] for n in o['publication']['affected_original_sheets']}
        need(z.namelist()==bz.namelist(),'same package parts/order')
        for name in z.namelist():
            if name not in affected:need(z.read(name)==bz.read(name),'unchanged package part '+name)
            if name.endswith(('.xml','.rels')):ET.fromstring(z.read(name))
        for name,nrows in [('Master Crosswalk',354),('DIM Register',338)]:
            rt=ET.fromstring(z.read(paths[name]));bt=ET.fromstring(bz.read(paths[name]));sd=rt.find(q('sheetData'));bs=bt.find(q('sheetData'))
            need([ET.tostring(r) for r in list(sd)[:nrows]]==[ET.tostring(r) for r in bs],'all original saved rows/styles '+name)
        styles=ET.fromstring(z.read('xl/styles.xml'));xfs=list(styles.find(q('cellXfs')));fills=list(styles.find(q('fills')))
        cells=old.readcells(saved,'Master Crosswalk')
        for i,row in enumerate(m['review_grid'],1):
            for j,v in enumerate(row,1):need(cells.get(addr(i,j),'')==v,'saved value '+addr(i,j))
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));lookup={c.get('r'):c for c in rt.iter(q('c'))}
        for r in new:
            d=r['AAS_O2_source_correspondence'];c=lookup[d['cell']];fg=fills[int(xfs[int(c.get('s'))].get('fillId'))].find('.//'+q('fgColor'));need(fg.get('rgb')[-6:]==d['fill'][1:],'new actual fill '+d['cell'])
        for name in paths:
            rt=ET.fromstring(z.read(paths[name]));rownums=[]
            for rr in rt.find(q('sheetData')):
                rownums.append(int(rr.get('r')));nums=[]
                for c in rr.findall(q('c')):
                    n=0
                    for ch in re.match('[A-Z]+',c.get('r')).group():n=n*26+ord(ch)-64
                    nums.append(n);need(c.get('t')!='e','no error cell '+name)
                need(nums==sorted(set(nums)),'ordered unique cells '+name)
            need(rownums==sorted(set(rownums)),'ordered unique rows '+name)
        reg=old.readcells(saved,'DIM Register')
        for n,r in enumerate(new,339):need(reg['A'+str(n)]==r['row_id'] and reg['R'+str(n)].startswith(r['AAS_O2_source_correspondence']['candidate_status']),'saved candidate register')
    for name in ('M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx','M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx'):
        rel='Manual_Workbook_Versions/'+name;need((D/rel).read_bytes()==f3_baseline(rel,AAS_O2_BASE),'immutable '+name)
    need(not list((D/'Manual_Workbook_Versions').glob('M02*')),'no unapproved M02')
    need(a['one_next']==o['one_next']==m['nextOwnerAction']==m['AAS_O2_native_review']['one_next'],'one O3 stop boundary')
    print('PASS AAS O2: 75 source dispositions; eight new candidate rows; original 337 rows and 616 classifications unchanged.')
    print('PASS: all 5808 saved grid values, eight new fills, both CSV/readable mirrors, 26 sheets, 21 untouched sheets, M00/M01 preserved.')
    print('LIMIT: AAS bounded PARTIAL, no model adoption/runtime validation; actual Microsoft Excel clean reopen pending. Next O3 only.')


AAS_O3_BASE='e7628af544dd216e3171624ac51af032864d3748'

def publish_aas_o3():
    """Extend the same saved package with source-qualified candidate rows; preserve original parts."""
    import copy, html
    m=load(MASTER);a=load(F3_PEER_FILES[-1]);o=a['AAS_O3_native_review'];grid=m['review_grid']
    prior=(D/BOOK).read_bytes();need(prior==f3_baseline(BOOK,AAS_O3_BASE),'exact archived pre-O3 workbook')
    need(m['currentEvidenceCheckpoint']=='AAS_O3_SOURCE_DECISIONS_PENDING_SAME_XLSX','O3 source checkpoint')
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/name).open('w',newline='',encoding='utf-8') as f:csv.writer(f,lineterminator='\n').writerows(grid)
    table=['<table><thead><tr>']
    for idx,span in ((0,4),(4,6),(10,5),(15,1)):table.append(f'<th colspan="{span}">{html.escape(grid[0][idx])}</th>')
    table+=['</tr><tr>'+''.join('<th>'+html.escape(v)+'</th>' for v in grid[1])+'</tr></thead><tbody>']
    for i,row in enumerate(grid[2:],2):table.append('<tr><th colspan="16">'+html.escape(row[0])+'</th></tr>' if i in m['review_sections'] else '<tr>'+''.join('<td>'+html.escape(v)+'</td>' for v in row)+'</tr>')
    table+=['</tbody></table>']
    banner='# CURRENT — F3 accepted; AAS O3 native-first review complete (14 November 2026, America/New_York)\n\nFive provisional information-need rows added after 52 AAS04/AAS05 findings and six O2 follow-ups were reconciled. Original 345 rows and 624 classifications unchanged. Current total: 350 information rows, 629 source-bearing comparisons (521 colored / 108 held), 26 sheets. Candidates are not adopted classes or Profile requirements. AAS source coverage remains bounded PARTIAL; Microsoft Excel clean reopen remains pending. Next: owner Proceed for O4 only. Earlier checkpoint banners and counts are historical.\n\n---\n\n'
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        oldtext=f3_baseline(name,AAS_O3_BASE).decode();(D/name).write_text(banner+oldtext[:oldtext.index('<table>')]+'\n'.join(table)+oldtext[oldtext.index('</table>')+8:],encoding='utf-8')
    with zipfile.ZipFile(io.BytesIO(prior)) as z:
        paths=old.sheetpaths(z);replacements={}
        def edited(name,changes):
            rt=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in rt.iter(q('c'))}
            for ref,value in changes.items():need(ref in cells,'existing guidance cell '+ref);f3_put(cells[ref],value)
            for rr in rt.find(q('sheetData')):
                vals=[v for k,v in changes.items() if re.search(r'\d+$',k).group()==rr.get('r')]
                if vals:rr.set('ht',str(min(409.5,max(float(rr.get('ht',15)),max(len(textwrap.wrap(v,95))*12+18 for v in vals)))));rr.set('customHeight','1')
            replacements[paths[name]]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));sd=rt.find(q('sheetData'));templates={int(r.get('r')):r for r in sd}
        def make_row(template,number,values):
            rr=copy.deepcopy(template);rr.set('r',str(number))
            for c in list(rr):rr.remove(c)
            styles={re.match('[A-Z]+',c.get('r')).group():c.get('s','0') for c in template}
            for j,v in enumerate(values,1):
                col=re.match('[A-Z]+',addr(number,j)).group();c=ET.SubElement(rr,q('c'),{'r':addr(number,j),'s':styles.get(col,'526')});f3_put(c,str(v))
            return rr
        divider=make_row(templates[355],364,grid[363]);sd.append(divider)
        merges=rt.find(q('mergeCells'));need(merges is not None,'existing topic merges');ET.SubElement(merges,q('mergeCell'),{'ref':'A364:P364'});merges.set('count',str(len(merges)))
        for n,row in enumerate(m['rows'][345:],365):
            rr=make_row(templates[363],n,row['display']);rr.set('ht','240');rr.set('customHeight','1')
            for c in rr:
                col=re.match('[A-Z]+',c.get('r')).group()
                if col in ('G','H','I','J'):c.set('s','526' if n%2==0 else '527')
                if col=='G':c.set('s','528' if row['AAS_O3_source_correspondence']['candidate_status']=='COMMON_CANDIDATE' else '529')
            sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:P369')
        af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A2:P369')
        replacements[paths['Master Crosswalk']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['DIM Register']));sd=rt.find(q('sheetData'));template=list(sd)[-1]
        for n,row in enumerate(m['rows'][345:],347):
            c=row['AAS_O3_source_correspondence'];ids=', '.join(c['source_ids'])
            vals=[row['row_id'],row['label'],row['definition'],row['status'],row['source_review_status'],row['master_inclusion'],row['dim_adoption'],'','Not assessed here','','Not assessed here','AAS pinned Part 1 v3.2 targeted text; no observed case','Not assessed here','Not assessed here','Not assessed here','O3 sources: '+ids,ids+'; '+c['relation']+'; '+c['reason_for_separate_candidate'],c['candidate_status']+' — '+c['native_meaning']]
            rr=make_row(template,n,vals);rr.set('ht','240');rr.set('customHeight','1');sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:R351');af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A1:R351')
        replacements[paths['DIM Register']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        guidance={'A1':'CURRENT 14 NOV 2026 — F3 accepted; AAS O3 complete','B17':'O3: 52 AAS04/AAS05 findings and six O2 follow-ups reconciled; five provisional candidates added. All 345 earlier rows and 624 classifications unchanged.','B19':'350 information rows; 629 source comparisons: 521 colored, 108 held. AAS 65 colored / 12 held across 77 comparisons. Other 771 four-donor positions retain explicit statuses.','B21':'Selected original passages and 23 schema blocks re-read; six schema files remain sampled. Event include text read in full; figures retain prior inspection status. No whole-corpus or runtime claim.','B22':'New candidates: event declaration/state, source and logical scope, routing, initiator, qualified context. Experimental standing and spelling, UTC, version, list and Range holds remain.','A23':'Next step and remaining limits','B23':'Await owner Proceed for O4 only: discovery and services. Stop before O5. AAS remains active bounded PARTIAL; actual Microsoft Excel clean reopen/no-repair remains pending.','B28':'O3 saved checkpoint: 5,904 grid values, five new classifications, 26 sheets. Original rows and source evidence, 21 untouched sheets and M00/M01 preserved. No M02 or model adoption.'}
        guidance.update({'B1':'Current: 350 information rows in the same 26-sheet master. AAS active bounded PARTIAL; M00/M01 frozen. Rows 2–10 retain labeled historical checks.', 'A2':'Historical pre-F3 comparison size', 'A3':'Historical F2 candidate additions', 'A4':'Historical ISA F2-4 grading', 'A5':'Historical SAPIENT F2-3 grading', 'A6':'Historical Open Group SOSA F2-2 grading', 'A7':'Historical F2 colored cells', 'A8':'Historical original fill palette', 'A9':'Historical F2 mixed/unassessed handling', 'A10':'Historical F2 preserved comparison text', 'A28':'Current O3 saved-file verification'})
        edited('Summary',guidance);edited('Validation',guidance)
        edited('Legend',{'A1':'CURRENT LEGEND — F3 accepted; O3 candidate additions','B23':'Current: 521 colored / 108 held source comparisons. Earlier F2/F3/O2 counts are historical.','A28':'AAS O3 additions and current boundary','B28':'Five new candidates: three common (blue), two specialized (amber). Total 629 source comparisons, 521 colored / 108 held. Color grades potential information needs, not source maturity, equivalence or adoption. Experimental standing remains explicit. Next O4.'})
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as dst:
            for info in z.infolist():dst.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    saved=buf.getvalue();(D/BOOK).write_bytes(saved);sha=digest(saved)
    m['currentEvidenceCheckpoint']='AAS_O3_SAVED_VERIFIED';m['currentWorkbookSha256']=sha;m['workbookSnapshot'].update(checkpoint=m['currentEvidenceCheckpoint'],sha256=sha,currently_matches_readable_view=True,lag='ZERO: 369x16 grid and current O3 owner routing',textCheckpoint='AAS_O3_NATIVE_CANDIDATES',validation_file=F3_PEER_FILES[-1]+'#/AAS_O3_native_review/publication')
    m['AAS_O3_native_review']['status']='O3_COMPLETE__O4_PENDING_OWNER_PROCEED'
    o['status']='O3_COMPLETE__O4_PENDING_OWNER_PROCEED';o['publication']={'workbook_sha256':sha,'previous_workbook_sha256':digest(prior),'affected_original_sheets':['Master Crosswalk','DIM Register','Summary','Validation','Legend'],'unchanged_sheet_parts':21,'grid_values':5904,'new_candidate_cells':['G'+str(i) for i in range(365,370)],'existing_values_and_fills':'UNCHANGED','M00_M01_preserved':True,'M02_created':False,'actual_Microsoft_Excel_clean_reopen':'PENDING','visual_review':'PENDING','remote_publication':'PENDING'}
    a['status']='AAS_ACTIVE_BOUNDED_PARTIAL__O3_COMPLETE';a['master_state_current'].update(checkpoint=m['currentEvidenceCheckpoint'],comparison_lag=0,status='O3_COMPLETE__O4_PENDING',workbook_metadata_lag='ZERO: current O3 guidance refreshed; labeled historical checkpoints retained.')
    save(MASTER,m);save(F3_PEER_FILES[-1],a);verify_aas_o3()


def verify_aas_o3():
    """Check the bounded native reconciliation and saved file against the archived O2 result."""
    import copy
    from collections import Counter
    from html.parser import HTMLParser
    m=load(MASTER);base=json.loads(f3_baseline(MASTER,AAS_O3_BASE));a=load(F3_PEER_FILES[-1]);ab=json.loads(f3_baseline(F3_PEER_FILES[-1],AAS_O3_BASE));o=a['AAS_O3_native_review']
    need(m['currentEvidenceCheckpoint']=='AAS_O3_SAVED_VERIFIED','O3 checkpoint')
    need(m['rows'][:345]==base['rows'] and m['review_grid'][:363]==base['review_grid'],'all original rows/classifications/cases unchanged')
    need(m['columns']==base['columns'] and m['review_sections']==base['review_sections']+[363],'approved layout plus appended topic')
    need(len(m['rows'])==350 and len(m['review_grid'])==369 and all(len(r)==16 for r in m['review_grid']),'350 rows / 369x16 grid')
    allowed={'rows','review_grid','review_sections','counts','currentEvidenceCheckpoint','currentWorkbookSha256','workbookSnapshot','nextOwnerAction'}
    for k,v in base.items():
        if k not in allowed:need(m[k]==v,'preserved master evidence '+k)
    for k,v in base['counts'].items():
        if k not in ('informationRows','AAS_current_source_bearing_comparisons'):need(m['counts'][k]==v,'preserved historical count '+k)
    need(m['counts']['informationRows']==350 and m['counts']['AAS_current_source_bearing_comparisons']==77,'current counts')
    restored=copy.deepcopy(a);restored.pop('AAS_O3_native_review')
    for k in ('status','one_next','master_state_current'):restored[k]=ab[k]
    need(restored==ab,'all prior findings, holds and decisions unchanged')
    native={x['source_id']:x for st in ('AAS03','AAS04','AAS05') for x in a[st]['original_items']}
    required={x['source_id'] for st in ('AAS04','AAS05') for x in a[st]['original_items']}|{'AAS03-N%03d'%n for n in (25,26,27,29,30,31)}
    rs=o['records'];need(len(rs)==58 and {r['source_id'] for r in rs}==required,'52 findings plus six unique follow-ups')
    rowids={r['row_id'] for r in m['rows']};need(len(rowids)==350,'unique row IDs')
    for r in rs:
        need(digest(json.dumps(native[r['source_id']],sort_keys=True,ensure_ascii=False).encode())==r['original_record_sha256'],'original evidence hash '+r['source_id'])
        need(set(r['row_ids'])<=rowids and r['rationale'] and r['relation'] and not r['DIM_Profile_adopted'],'qualified disposition '+r['source_id'])
    new=m['rows'][345:];need([r['row_id'] for r in new]==o['new_candidate_row_ids'],'five stable candidate IDs')
    need(Counter(r['AAS_O3_source_correspondence']['candidate_status'] for r in new)=={'COMMON_CANDIDATE':3,'SPECIALIZED_CANDIDATE':2},'candidate classifications')
    for r in new:
        c=r['AAS_O3_source_correspondence'];need(set(c['source_ids'])<=required and c['reason_for_separate_candidate'] and not c['DIM_Profile_adopted'],'candidate source evidence')
        need(all(v.strip() for v in r['display']),'explicit new row states')
        need(m['review_grid'][r['display_row']-1]==r['display'],'candidate display placement')
    need(source_csv('Master_Donor_Concept_to_DIM_Crosswalk.csv')==m['review_grid']==source_csv('ISA_Correction_Review_07NOV2026.csv'),'both CSV mirrors')
    md=(D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_text();need(md==(D/'ISA_Correction_Review_07NOV2026.md').read_text(),'both readable mirrors')
    class Table(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.cell=None
        def handle_starttag(self,t,attrs):
            if t=='tr':self.row=[]
            if t in ('td','th'):self.cell='';self.span=int(dict(attrs).get('colspan',1))
        def handle_data(self,d):
            if self.cell is not None:self.cell+=d
        def handle_endtag(self,t):
            if t in ('td','th'):self.row += [self.cell]+['']*(self.span-1);self.cell=None
            if t=='tr':self.rows.append(self.row)
    tab=Table();tab.feed(md[md.index('<table>'):md.index('</table>')+8]);need(tab.rows==m['review_grid'],'readable table values')
    saved=(D/BOOK).read_bytes();prior=f3_baseline(BOOK,AAS_O3_BASE);need(digest(saved)==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==o['publication']['workbook_sha256'],'saved hash')
    with zipfile.ZipFile(io.BytesIO(saved)) as z,zipfile.ZipFile(io.BytesIO(prior)) as bz:
        paths=old.sheetpaths(z);need(paths==old.sheetpaths(bz) and len(paths)==26 and z.testzip() is None,'same 26-sheet valid package')
        affected={paths[n] for n in o['publication']['affected_original_sheets']}
        need(z.namelist()==bz.namelist(),'same package parts/order')
        for name in z.namelist():
            if name not in affected:need(z.read(name)==bz.read(name),'unchanged package part '+name)
            if name.endswith(('.xml','.rels')):ET.fromstring(z.read(name))
        for name,nrows in [('Master Crosswalk',363),('DIM Register',346)]:
            rt=ET.fromstring(z.read(paths[name]));bt=ET.fromstring(bz.read(paths[name]));sd=rt.find(q('sheetData'));bs=bt.find(q('sheetData'))
            need([ET.tostring(r) for r in list(sd)[:nrows]]==[ET.tostring(r) for r in bs],'all original saved rows/styles '+name)
        styles=ET.fromstring(z.read('xl/styles.xml'));xfs=list(styles.find(q('cellXfs')));fills=list(styles.find(q('fills')))
        cells=old.readcells(saved,'Master Crosswalk')
        for i,row in enumerate(m['review_grid'],1):
            for j,v in enumerate(row,1):need(cells.get(addr(i,j),'')==v,'saved value '+addr(i,j))
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));lookup={c.get('r'):c for c in rt.iter(q('c'))}
        for r in new:
            d=r['AAS_O3_source_correspondence'];c=lookup[d['cell']];fg=fills[int(xfs[int(c.get('s'))].get('fillId'))].find('.//'+q('fgColor'));need(fg.get('rgb')[-6:]==d['fill'][1:],'new actual fill '+d['cell'])
        for name in paths:
            rt=ET.fromstring(z.read(paths[name]));rownums=[]
            for rr in rt.find(q('sheetData')):
                rownums.append(int(rr.get('r')));nums=[]
                for c in rr.findall(q('c')):
                    n=0
                    for ch in re.match('[A-Z]+',c.get('r')).group():n=n*26+ord(ch)-64
                    nums.append(n);need(c.get('t')!='e','no error cell '+name)
                need(nums==sorted(set(nums)),'ordered unique cells '+name)
            need(rownums==sorted(set(rownums)),'ordered unique rows '+name)
        reg=old.readcells(saved,'DIM Register')
        for n,r in enumerate(new,347):need(reg['A'+str(n)]==r['row_id'] and reg['R'+str(n)].startswith(r['AAS_O3_source_correspondence']['candidate_status']),'saved candidate register')
    for name in ('M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx','M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx'):
        rel='Manual_Workbook_Versions/'+name;need((D/rel).read_bytes()==f3_baseline(rel,AAS_O3_BASE),'immutable '+name)
    need(not list((D/'Manual_Workbook_Versions').glob('M02*')),'no unapproved M02')
    need(a['one_next']==o['one_next']==m['nextOwnerAction']==m['AAS_O3_native_review']['one_next'],'one O4 stop boundary')
    print('PASS AAS O3: 52 native findings + six O2 follow-ups; five new candidates; original 345 rows and 624 classifications unchanged.')
    print('PASS: all 5904 saved values, five new fills, both CSV/readable mirrors, 26 sheets, 21 untouched sheets, M00/M01 preserved.')
    print('LIMIT: AAS bounded PARTIAL; original conflicts/experimental standing and Excel clean reopen hold retained. Next O4 only.')


AAS_O4_BASE='ffdf561e1c040108293df7dcb29ceeddb013ec93'

def publish_aas_o4():
    """Extend the same saved package with source-qualified candidate rows; preserve original parts."""
    import copy, html
    m=load(MASTER);a=load(F3_PEER_FILES[-1]);o=a['AAS_O4_native_review'];grid=m['review_grid']
    prior=(D/BOOK).read_bytes();need(prior==f3_baseline(BOOK,AAS_O4_BASE),'exact archived pre-O4 workbook')
    need(m['currentEvidenceCheckpoint']=='AAS_O4_SOURCE_DECISIONS_PENDING_SAME_XLSX','O4 source checkpoint')
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/name).open('w',newline='',encoding='utf-8') as f:csv.writer(f,lineterminator='\n').writerows(grid)
    table=['<table><thead><tr>']
    for idx,span in ((0,4),(4,6),(10,5),(15,1)):table.append(f'<th colspan="{span}">{html.escape(grid[0][idx])}</th>')
    table+=['</tr><tr>'+''.join('<th>'+html.escape(v)+'</th>' for v in grid[1])+'</tr></thead><tbody>']
    for i,row in enumerate(grid[2:],2):table.append('<tr><th colspan="16">'+html.escape(row[0])+'</th></tr>' if i in m['review_sections'] else '<tr>'+''.join('<td>'+html.escape(v)+'</td>' for v in row)+'</tr>')
    table+=['</tbody></table>']
    banner='# CURRENT — F3 accepted; AAS O4 discovery/service review complete (15 November 2026)\n\nTwo provisional information-need rows added after all 38 AAS06 findings were reconciled against selected pinned original passages. Original 350 rows and 629 classifications unchanged. Current total: 352 information rows, 631 source-bearing comparisons (523 colored / 108 held), 26 sheets. Both additions are common candidates; neither is adopted. AAS remains bounded PARTIAL; Microsoft Excel clean reopen remains pending. Next: separate owner Proceed for O5 only. Earlier narrative is preserved at the pre-O4 archive.\n\n'
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        (D/name).write_text(banner+'\n'.join(table)+'\n',encoding='utf-8')
    with zipfile.ZipFile(io.BytesIO(prior)) as z:
        paths=old.sheetpaths(z);replacements={}
        def edited(name,changes):
            rt=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in rt.iter(q('c'))}
            for ref,value in changes.items():need(ref in cells,'existing guidance cell '+ref);f3_put(cells[ref],value)
            for rr in rt.find(q('sheetData')):
                vals=[v for k,v in changes.items() if re.search(r'\d+$',k).group()==rr.get('r')]
                if vals:rr.set('ht',str(min(409.5,max(float(rr.get('ht',15)),max(len(textwrap.wrap(v,95))*12+18 for v in vals)))));rr.set('customHeight','1')
            replacements[paths[name]]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));sd=rt.find(q('sheetData'));templates={int(r.get('r')):r for r in sd}
        def make_row(template,number,values):
            rr=copy.deepcopy(template);rr.set('r',str(number))
            for c in list(rr):rr.remove(c)
            styles={re.match('[A-Z]+',c.get('r')).group():c.get('s','0') for c in template}
            for j,v in enumerate(values,1):
                col=re.match('[A-Z]+',addr(number,j)).group();c=ET.SubElement(rr,q('c'),{'r':addr(number,j),'s':styles.get(col,'526')});f3_put(c,str(v))
            return rr
        divider=make_row(templates[364],370,grid[369]);sd.append(divider)
        merges=rt.find(q('mergeCells'));need(merges is not None,'existing topic merges');ET.SubElement(merges,q('mergeCell'),{'ref':'A370:P370'});merges.set('count',str(len(merges)))
        for n,row in enumerate(m['rows'][350:],371):
            rr=make_row(templates[369],n,row['display']);rr.set('ht','240');rr.set('customHeight','1')
            for c in rr:
                col=re.match('[A-Z]+',c.get('r')).group()
                if col in ('G','H','I','J'):c.set('s','526' if n%2==0 else '527')
                if col=='G':c.set('s','528' if row['AAS_O4_source_correspondence']['candidate_status']=='COMMON_CANDIDATE' else '529')
            sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:P372')
        af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A2:P372')
        replacements[paths['Master Crosswalk']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['DIM Register']));sd=rt.find(q('sheetData'));template=list(sd)[-1]
        for n,row in enumerate(m['rows'][350:],352):
            c=row['AAS_O4_source_correspondence'];ids=', '.join(c['source_ids'])
            vals=[row['row_id'],row['label'],row['definition'],row['status'],row['source_review_status'],row['master_inclusion'],row['dim_adoption'],'','Not assessed here','','Not assessed here','AAS pinned Part 2 v3.2 targeted text; no observed case','Not assessed here','Not assessed here','Not assessed here','O4 sources: '+ids,ids+'; '+c['relation']+'; '+c['reason_for_separate_candidate'],c['candidate_status']+' — '+c['native_meaning']]
            rr=make_row(template,n,vals);rr.set('ht','240');rr.set('customHeight','1');sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:R353');af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A1:R353')
        replacements[paths['DIM Register']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        guidance={'A1':'CURRENT 15 NOV 2026 — F3 accepted; AAS O4 complete',
            'A17':'Current completed scope',
            'B1':'Current: 352 information rows in the same 26-sheet master. AAS active bounded PARTIAL; M00/M01 frozen. Rows 2–10 retain labeled historical checks.',
            'B17':'O4: all 38 AAS06 findings reconciled against selected original passages; two provisional common candidates added. All 350 earlier rows and 629 classifications unchanged.',
            'B19':'352 information rows; 631 source comparisons: 523 colored, 108 held. AAS 67 colored / 12 held across 79 comparisons. Other four-donor positions retain explicit statuses.',
            'B21':'Selected original passages in 13 pinned source files read; profile tables and selected API operations are not exhaustive profile audits. External originals and figures retain prior grades.',
            'B22':'New candidates: digital-record discovery/service-location association; digital-record state at a specified time. Preserve optional endpoints, authoritative record, experimental recent changes and source conflicts.',
            'A23':'Next step and remaining limits',
            'B23':'Await owner Proceed for O5 only: 53 AAS07 model/operation/auxiliary API findings. Stop before O6. AAS remains bounded PARTIAL; actual Microsoft Excel clean reopen remains pending.',
            'A28':'Current O4 saved-file verification',
            'B28':'O4: 5,952 saved grid values, two new common classifications, 26 sheets. Original rows/evidence, 21 untouched sheets and M00/M01 preserved. No M02 or model adoption.'}
        for ref,title in [('A24','AAS05 selected schemas'),('A25','AAS06 discovery/services'),('A26','AAS07 model/operation APIs'),('A27','AAS08 companions')]: guidance[ref]='Historical '+title+' review; no DIM/Profile adoption'
        edited('Summary',guidance);edited('Validation',guidance)
        edited('Legend',{'A23':'Current classification totals','B24':'352 information rows, 372 × 16 saved comparison grid','A1':'CURRENT LEGEND — F3 accepted; O4 candidate additions','B23':'Current: 523 colored / 108 held source comparisons. Earlier F2/F3/O2/O3 counts are historical.','A28':'AAS O4 additions and current boundary','B28':'Two new common candidates (blue). Total 631 source comparisons, 523 colored / 108 held. Color grades potential information needs, not source maturity, equivalence or adoption. Experimental standing and source conflicts remain. Next O5.'})
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as dst:
            for info in z.infolist():dst.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    saved=buf.getvalue();(D/BOOK).write_bytes(saved);sha=digest(saved)
    m['currentEvidenceCheckpoint']='AAS_O4_SAVED_VERIFIED';m['currentWorkbookSha256']=sha;m['workbookSnapshot'].update(checkpoint=m['currentEvidenceCheckpoint'],sha256=sha,currently_matches_readable_view=True,lag='ZERO: 372x16 grid and current O4 owner routing',textCheckpoint='AAS_O4_NATIVE_CANDIDATES',validation_file=F3_PEER_FILES[-1]+'#/AAS_O4_native_review/publication')
    m['AAS_O4_native_review']['status']='O4_COMPLETE__O5_PENDING_OWNER_PROCEED'
    o['status']='O4_COMPLETE__O5_PENDING_OWNER_PROCEED';o['publication']={'workbook_sha256':sha,'previous_workbook_sha256':digest(prior),'affected_original_sheets':['Master Crosswalk','DIM Register','Summary','Validation','Legend'],'unchanged_sheet_parts':21,'grid_values':5952,'new_candidate_cells':['G'+str(i) for i in range(371,373)],'existing_values_and_fills':'UNCHANGED','M00_M01_preserved':True,'M02_created':False,'actual_Microsoft_Excel_clean_reopen':'PENDING','visual_review':'PENDING','remote_publication':'PENDING'}
    a['status']='AAS_ACTIVE_BOUNDED_PARTIAL__O4_COMPLETE';a['master_state_current'].update(checkpoint=m['currentEvidenceCheckpoint'],comparison_lag=0,status='O4_COMPLETE__O5_PENDING',workbook_metadata_lag='ZERO: current O4 guidance refreshed; labeled historical checkpoints retained.')
    save(MASTER,m);save(F3_PEER_FILES[-1],a);verify_aas_o4()


def verify_aas_o4():
    """Check the bounded native reconciliation and saved file against the archived O3 result."""
    import copy
    from collections import Counter
    from html.parser import HTMLParser
    m=load(MASTER);base=json.loads(f3_baseline(MASTER,AAS_O4_BASE));a=load(F3_PEER_FILES[-1]);ab=json.loads(f3_baseline(F3_PEER_FILES[-1],AAS_O4_BASE));o=a['AAS_O4_native_review']
    need(m['currentEvidenceCheckpoint']=='AAS_O4_SAVED_VERIFIED','O4 checkpoint')
    need(m['rows'][:350]==base['rows'] and m['review_grid'][:369]==base['review_grid'],'all original rows/classifications/cases unchanged')
    need(m['columns']==base['columns'] and m['review_sections']==base['review_sections']+[369],'approved layout plus appended topic')
    need(len(m['rows'])==352 and len(m['review_grid'])==372 and all(len(r)==16 for r in m['review_grid']),'352 rows / 372x16 grid')
    allowed={'rows','review_grid','review_sections','counts','currentEvidenceCheckpoint','currentWorkbookSha256','workbookSnapshot','nextOwnerAction'}
    for k,v in base.items():
        if k not in allowed:need(m[k]==v,'preserved master evidence '+k)
    for k,v in base['counts'].items():
        if k not in ('informationRows','AAS_current_source_bearing_comparisons'):need(m['counts'][k]==v,'preserved historical count '+k)
    need(m['counts']['informationRows']==352 and m['counts']['AAS_current_source_bearing_comparisons']==79,'current counts')
    restored=copy.deepcopy(a);restored.pop('AAS_O4_native_review')
    for k in ('status','one_next','master_state_current'):restored[k]=ab[k]
    need(restored==ab,'all prior findings, holds and decisions unchanged')
    native={x['source_id']:x for x in a['AAS06']['original_items']}
    required=set(native);rs=o['records']
    need(len(rs)==38 and {r['source_id'] for r in rs}==required,'38 unique AAS06 findings')
    need(len(o['targeted_original_contacts'])==13,'13 sampled original source files')
    need(len(o['historical_53_in_O4'])==12,'12 historically uncited findings dispositioned')
    rowids={r['row_id'] for r in m['rows']};need(len(rowids)==352,'unique row IDs')
    for r in rs:
        need(digest(json.dumps(native[r['source_id']],sort_keys=True,ensure_ascii=False).encode())==r['original_record_sha256'],'original evidence hash '+r['source_id'])
        need(set(r['row_ids'])<=rowids and r['rationale'] and r['relation'] and not r['DIM_Profile_adopted'],'qualified disposition '+r['source_id'])
    new=m['rows'][350:];need([r['row_id'] for r in new]==o['new_candidate_row_ids'],'two stable candidate IDs')
    need(Counter(r['AAS_O4_source_correspondence']['candidate_status'] for r in new)=={'COMMON_CANDIDATE':2},'candidate classifications')
    for r in new:
        c=r['AAS_O4_source_correspondence'];need(set(c['source_ids'])<=required and c['reason_for_separate_candidate'] and not c['DIM_Profile_adopted'],'candidate source evidence')
        need(all(v.strip() for v in r['display']),'explicit new row states')
        need(m['review_grid'][r['display_row']-1]==r['display'],'candidate display placement')
    need(source_csv('Master_Donor_Concept_to_DIM_Crosswalk.csv')==m['review_grid']==source_csv('ISA_Correction_Review_07NOV2026.csv'),'both CSV mirrors')
    md=(D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_text();need(md==(D/'ISA_Correction_Review_07NOV2026.md').read_text(),'both readable mirrors')
    class Table(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.cell=None
        def handle_starttag(self,t,attrs):
            if t=='tr':self.row=[]
            if t in ('td','th'):self.cell='';self.span=int(dict(attrs).get('colspan',1))
        def handle_data(self,d):
            if self.cell is not None:self.cell+=d
        def handle_endtag(self,t):
            if t in ('td','th'):self.row += [self.cell]+['']*(self.span-1);self.cell=None
            if t=='tr':self.rows.append(self.row)
    tab=Table();tab.feed(md[md.index('<table>'):md.index('</table>')+8]);need(tab.rows==m['review_grid'],'readable table values')
    saved=(D/BOOK).read_bytes();prior=f3_baseline(BOOK,AAS_O4_BASE);need(digest(saved)==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==o['publication']['workbook_sha256'],'saved hash')
    with zipfile.ZipFile(io.BytesIO(saved)) as z,zipfile.ZipFile(io.BytesIO(prior)) as bz:
        paths=old.sheetpaths(z);need(paths==old.sheetpaths(bz) and len(paths)==26 and z.testzip() is None,'same 26-sheet valid package')
        affected={paths[n] for n in o['publication']['affected_original_sheets']}
        need(z.namelist()==bz.namelist(),'same package parts/order')
        for name in z.namelist():
            if name not in affected:need(z.read(name)==bz.read(name),'unchanged package part '+name)
            if name.endswith(('.xml','.rels')):ET.fromstring(z.read(name))
        for name,nrows in [('Master Crosswalk',369),('DIM Register',351)]:
            rt=ET.fromstring(z.read(paths[name]));bt=ET.fromstring(bz.read(paths[name]));sd=rt.find(q('sheetData'));bs=bt.find(q('sheetData'))
            need([ET.tostring(r) for r in list(sd)[:nrows]]==[ET.tostring(r) for r in bs],'all original saved rows/styles '+name)
        styles=ET.fromstring(z.read('xl/styles.xml'));xfs=list(styles.find(q('cellXfs')));fills=list(styles.find(q('fills')))
        cells=old.readcells(saved,'Master Crosswalk')
        for i,row in enumerate(m['review_grid'],1):
            for j,v in enumerate(row,1):need(cells.get(addr(i,j),'')==v,'saved value '+addr(i,j))
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));lookup={c.get('r'):c for c in rt.iter(q('c'))}
        for r in new:
            d=r['AAS_O4_source_correspondence'];c=lookup[d['cell']];fg=fills[int(xfs[int(c.get('s'))].get('fillId'))].find('.//'+q('fgColor'));need(fg.get('rgb')[-6:]==d['fill'][1:],'new actual fill '+d['cell'])
        for name in paths:
            rt=ET.fromstring(z.read(paths[name]));rownums=[]
            for rr in rt.find(q('sheetData')):
                rownums.append(int(rr.get('r')));nums=[]
                for c in rr.findall(q('c')):
                    n=0
                    for ch in re.match('[A-Z]+',c.get('r')).group():n=n*26+ord(ch)-64
                    nums.append(n);need(c.get('t')!='e','no error cell '+name)
                need(nums==sorted(set(nums)),'ordered unique cells '+name)
            need(rownums==sorted(set(rownums)),'ordered unique rows '+name)
        reg=old.readcells(saved,'DIM Register')
        for n,r in enumerate(new,352):need(reg['A'+str(n)]==r['row_id'] and reg['R'+str(n)].startswith(r['AAS_O4_source_correspondence']['candidate_status']),'saved candidate register')
    for name in ('M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx','M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx'):
        rel='Manual_Workbook_Versions/'+name;need((D/rel).read_bytes()==f3_baseline(rel,AAS_O4_BASE),'immutable '+name)
    need(not list((D/'Manual_Workbook_Versions').glob('M02*')),'no unapproved M02')
    need(a['one_next']==o['one_next']==m['nextOwnerAction']==m['AAS_O4_native_review']['one_next'],'one O5 stop boundary')
    print('PASS AAS O4: 38 native findings; two common candidates; original 350 rows and 629 classifications unchanged.')
    print('PASS: all 5952 saved values, two new fills, both CSV/readable mirrors, 26 sheets, 21 untouched sheets, M00/M01 preserved.')
    print('LIMIT: AAS bounded PARTIAL; conflicts, experimental standing and Excel clean reopen hold retained. Next O5 only.')


AAS_O5_BASE='c4098390dda77216c2f8d0df3feea0cbf991026b'

def publish_aas_o5():
    """Extend the same saved package with source-qualified candidate rows; preserve original parts."""
    import copy, html
    m=load(MASTER);a=load(F3_PEER_FILES[-1]);o=a['AAS_O5_native_review'];grid=m['review_grid']
    prior=(D/BOOK).read_bytes();need(prior==f3_baseline(BOOK,AAS_O5_BASE),'exact archived pre-O5 workbook')
    need(m['currentEvidenceCheckpoint']=='AAS_O5_SOURCE_DECISIONS_PENDING_SAME_XLSX','O5 source checkpoint')
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/name).open('w',newline='',encoding='utf-8') as f:csv.writer(f,lineterminator='\n').writerows(grid)
    table=['<table><thead><tr>']
    for idx,span in ((0,4),(4,6),(10,5),(15,1)):table.append(f'<th colspan="{span}">{html.escape(grid[0][idx])}</th>')
    table+=['</tr><tr>'+''.join('<th>'+html.escape(v)+'</th>' for v in grid[1])+'</tr></thead><tbody>']
    for i,row in enumerate(grid[2:],2):table.append('<tr><th colspan="16">'+html.escape(row[0])+'</th></tr>' if i in m['review_sections'] else '<tr>'+''.join('<td>'+html.escape(v)+'</td>' for v in row)+'</tr>')
    table+=['</tbody></table>']
    banner='# CURRENT — F3 accepted; AAS O5 model/operation API review complete (15 November 2026)\n\nAll 53 AAS07 findings reconciled against selected pinned originals. Two provisional candidates added (one common, one specialized); three existing AAS comparisons qualified without reclassification. Current total: 354 information rows; 633 source-bearing comparisons (525 colored / 108 held). All 631 prior classifications, unrelated cells and 26-sheet package preserved. Candidates are not adopted. AAS remains bounded PARTIAL; actual Microsoft Excel clean reopen pending. Next: separate owner Proceed for O6-1 companions only.\n\n'
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        (D/name).write_text(banner+'\n'.join(table)+'\n',encoding='utf-8')
    with zipfile.ZipFile(io.BytesIO(prior)) as z:
        paths=old.sheetpaths(z);replacements={}
        def edited(name,changes):
            rt=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in rt.iter(q('c'))}
            for ref,value in changes.items():need(ref in cells,'existing guidance cell '+ref);f3_put(cells[ref],value)
            for rr in rt.find(q('sheetData')):
                vals=[v for k,v in changes.items() if re.search(r'\d+$',k).group()==rr.get('r')]
                if vals:rr.set('ht',str(min(409.5,max(float(rr.get('ht',15)),max(len(textwrap.wrap(v,95))*12+18 for v in vals)))));rr.set('customHeight','1')
            replacements[paths[name]]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));sd=rt.find(q('sheetData'));templates={int(r.get('r')):r for r in sd}
        def make_row(template,number,values):
            rr=copy.deepcopy(template);rr.set('r',str(number))
            for c in list(rr):rr.remove(c)
            styles={re.match('[A-Z]+',c.get('r')).group():c.get('s','0') for c in template}
            for j,v in enumerate(values,1):
                col=re.match('[A-Z]+',addr(number,j)).group();c=ET.SubElement(rr,q('c'),{'r':addr(number,j),'s':styles.get(col,'526')});f3_put(c,str(v))
            return rr
        for change in o['qualified_existing_rows']:
            rr=templates[change['after']['display_row']]
            cell=next(c for c in rr if c.get('r')==change['master_cell'])
            f3_put(cell,change['after']['display'][6])
        divider=make_row(templates[370],373,grid[372]);sd.append(divider)
        merges=rt.find(q('mergeCells'));need(merges is not None,'existing topic merges');ET.SubElement(merges,q('mergeCell'),{'ref':'A370:P370'});merges.set('count',str(len(merges)))
        for n,row in enumerate(m['rows'][352:],374):
            rr=make_row(templates[372],n,row['display']);rr.set('ht','240');rr.set('customHeight','1')
            for c in rr:
                col=re.match('[A-Z]+',c.get('r')).group()
                if col in ('G','H','I','J'):c.set('s','526' if n%2==0 else '527')
                if col=='G':c.set('s','528' if row['AAS_O5_source_correspondence']['candidate_status']=='COMMON_CANDIDATE' else '529')
            sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:P372')
        af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A2:P372')
        replacements[paths['Master Crosswalk']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['DIM Register']));sd=rt.find(q('sheetData'));template=list(sd)[-1]
        register_cells={c.get('r'):c for c in rt.iter(q('c'))}
        for ref,value in o['register_changes'].items():f3_put(register_cells[ref],value)
        for n,row in enumerate(m['rows'][352:],354):
            c=row['AAS_O5_source_correspondence'];ids=', '.join(c['source_ids'])
            vals=[row['row_id'],row['label'],row['definition'],row['status'],row['source_review_status'],row['master_inclusion'],row['dim_adoption'],'','Not assessed here','','Not assessed here','AAS pinned Part 2 v3.2 targeted text; no observed case','Not assessed here','Not assessed here','Not assessed here','O5 sources: '+ids,ids+'; '+c['relation']+'; '+c['reason_for_separate_candidate'],c['candidate_status']+' — '+c['native_meaning']]
            rr=make_row(template,n,vals);rr.set('ht','240');rr.set('customHeight','1');sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:R353');af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A1:R353')
        replacements[paths['DIM Register']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        guidance={'A1':'CURRENT 15 NOV 2026 — F3 accepted; AAS O5 complete',
            'B1':'Current: 354 information rows in the same 26-sheet master. AAS active bounded PARTIAL; M00/M01 frozen. Earlier labeled checkpoints are historical.',
            'A17':'Current completed scope','B17':'O5: 53 AAS07 findings reconciled; two candidates added, three existing AAS comparisons qualified. All 631 prior classifications unchanged.',
            'B19':'354 information rows; 633 source comparisons: 525 colored, 108 held. AAS 69 colored / 12 held across 81 comparisons. Other donor positions retain explicit statuses.',
            'B21':'Selected original passages in 16 pinned Part 2 files read, including PackageDescription. Profile/body samples are not exhaustive conformance audits; external and figure limits remain.',
            'B22':'New: client-suggested operation timeout (common); exchange-package identity/record association (specialized). Lookup/history now include submodels. Receipt, execution and business success stay distinct.',
            'A23':'Next step and remaining limits','B23':'Await owner Proceed for O6-1: 55 AAS08 companion findings. Stop before O6-2 templates. AAS remains bounded PARTIAL; actual Microsoft Excel clean reopen pending.',
            'A28':'Current O5 saved-file verification','B28':'O5: all 6,000 saved grid values, two new fills, three qualified existing AAS cells and register entries. All prior fills, 21 untouched sheets and M00/M01 preserved; no M02 or adoption.'}
        edited('Summary',guidance);edited('Validation',guidance)
        edited('Legend',{'A1':'CURRENT LEGEND — F3 accepted; O5 candidates and qualifications','A23':'Current classification totals','B23':'Current: 525 colored / 108 held source comparisons. Earlier F2/F3/O2/O3/O4 counts are historical.','B24':'354 information rows, 375 × 16 saved comparison grid','A28':'AAS O5 additions and current boundary','B28':'Two new candidates: one common (blue), one specialized (amber). Three existing AAS comparisons qualified; all previous classifications retained. Color is not adoption, equivalence or source completeness. Next O6-1 companions.'})
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as dst:
            for info in z.infolist():dst.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    saved=buf.getvalue();(D/BOOK).write_bytes(saved);sha=digest(saved)
    m['currentEvidenceCheckpoint']='AAS_O5_SAVED_VERIFIED';m['currentWorkbookSha256']=sha;m['workbookSnapshot'].update(checkpoint=m['currentEvidenceCheckpoint'],sha256=sha,currently_matches_readable_view=True,lag='ZERO: 375x16 grid and current O5 owner routing',textCheckpoint='AAS_O5_NATIVE_CANDIDATES',validation_file=F3_PEER_FILES[-1]+'#/AAS_O5_native_review/publication')
    m['AAS_O5_native_review']['status']='O5_COMPLETE__O6_PENDING_OWNER_PROCEED'
    o['status']='O5_COMPLETE__O6_PENDING_OWNER_PROCEED';o['publication']={'workbook_sha256':sha,'previous_workbook_sha256':digest(prior),'affected_original_sheets':['Master Crosswalk','DIM Register','Summary','Validation','Legend'],'unchanged_sheet_parts':21,'grid_values':6000,'new_candidate_cells':['G'+str(i) for i in range(374,376)],'existing_values_and_fills':'Three AAS cells and their register entries qualified; all prior fills/classifications and unrelated cells unchanged','M00_M01_preserved':True,'M02_created':False,'actual_Microsoft_Excel_clean_reopen':'PENDING','visual_review':'PENDING','remote_publication':'PENDING'}
    a['status']='AAS_ACTIVE_BOUNDED_PARTIAL__O5_COMPLETE';a['master_state_current'].update(checkpoint=m['currentEvidenceCheckpoint'],comparison_lag=0,status='O5_COMPLETE__O6_PENDING',workbook_metadata_lag='ZERO: current O5 guidance refreshed; labeled historical checkpoints retained.')
    save(MASTER,m);save(F3_PEER_FILES[-1],a);verify_aas_o5()


def verify_aas_o5():
    """Check the bounded native reconciliation and saved file against the archived O4 result."""
    import copy
    from collections import Counter
    from html.parser import HTMLParser
    m=load(MASTER);base=json.loads(f3_baseline(MASTER,AAS_O5_BASE));a=load(F3_PEER_FILES[-1]);ab=json.loads(f3_baseline(F3_PEER_FILES[-1],AAS_O5_BASE));o=a['AAS_O5_native_review']
    need(m['currentEvidenceCheckpoint']=='AAS_O5_SAVED_VERIFIED','O5 checkpoint')
    changes={x['row_id']:x for x in o['qualified_existing_rows']}
    need(set(changes)=={'S06-R020','AAS-O4-RECORD-LOOKUP','AAS-O4-RECORD-HISTORY'},'three authorized existing-row qualifications')
    restored_rows=copy.deepcopy(m['rows'][:352]);restored_grid=copy.deepcopy(m['review_grid'][:372])
    for idx,row in enumerate(restored_rows):
        if row['row_id'] in changes:
            change=changes[row['row_id']];need(row==change['after'] and base['rows'][idx]==change['before'],'exact recorded before/after')
            oldrow=change['before'];need(row['display'][:6]+row['display'][7:]==oldrow['display'][:6]+oldrow['display'][7:],'only AAS display cell changes')
            need(not change['classification_changed'] and row['display'][6].startswith('[COMMON CANDIDATE]'),'existing classification retained')
            for key,value in oldrow.items():
                if key not in ('display','definition','display_row'):need(row[key]==value,'preserved prior evidence '+key)
            restored_rows[idx]=oldrow;restored_grid[row['display_row']-1]=oldrow['display']
    need(restored_rows==base['rows'] and restored_grid==base['review_grid'],'all other existing rows/cells unchanged')
    need(m['columns']==base['columns'] and m['review_sections']==base['review_sections']+[372],'approved layout plus appended topic')
    need(len(m['rows'])==354 and len(m['review_grid'])==375 and all(len(r)==16 for r in m['review_grid']),'354 rows / 375x16 grid')
    allowed={'rows','review_grid','review_sections','counts','currentEvidenceCheckpoint','currentWorkbookSha256','workbookSnapshot','nextOwnerAction'}
    for k,v in base.items():
        if k not in allowed:need(m[k]==v,'preserved master evidence '+k)
    for k,v in base['counts'].items():
        if k not in ('informationRows','AAS_current_source_bearing_comparisons'):need(m['counts'][k]==v,'preserved historical count '+k)
    need(m['counts']['informationRows']==354 and m['counts']['AAS_current_source_bearing_comparisons']==81,'current counts')
    restored=copy.deepcopy(a);restored.pop('AAS_O5_native_review')
    for k in ('status','one_next','master_state_current'):restored[k]=ab[k]
    need(restored==ab,'all prior findings, holds and decisions unchanged')
    native={x['source_id']:x for x in a['AAS07']['original_items']}
    required=set(native);rs=o['records']
    need(len(rs)==53 and {r['source_id'] for r in rs}==required,'53 unique AAS07 findings')
    need(len(o['targeted_original_contacts'])==16,'16 sampled original source files')
    need(len(o['historical_53_in_O5'])==11,'11 historically uncited findings dispositioned')
    rowids={r['row_id'] for r in m['rows']};need(len(rowids)==354,'unique row IDs')
    for r in rs:
        need(digest(json.dumps(native[r['source_id']],sort_keys=True,ensure_ascii=False).encode())==r['original_record_sha256'],'original evidence hash '+r['source_id'])
        need(set(r['row_ids'])<=rowids and r['rationale'] and r['relation'] and not r['DIM_Profile_adopted'],'qualified disposition '+r['source_id'])
    new=m['rows'][352:];need([r['row_id'] for r in new]==o['new_candidate_row_ids'],'two stable candidate IDs')
    need(Counter(r['AAS_O5_source_correspondence']['candidate_status'] for r in new)=={'COMMON_CANDIDATE':1,'SPECIALIZED_CANDIDATE':1},'candidate classifications')
    for r in new:
        c=r['AAS_O5_source_correspondence'];need(set(c['source_ids'])<=required and c['reason_for_separate_candidate'] and not c['DIM_Profile_adopted'],'candidate source evidence')
        need(all(v.strip() for v in r['display']),'explicit new row states')
        need(m['review_grid'][r['display_row']-1]==r['display'],'candidate display placement')
    need(source_csv('Master_Donor_Concept_to_DIM_Crosswalk.csv')==m['review_grid']==source_csv('ISA_Correction_Review_07NOV2026.csv'),'both CSV mirrors')
    md=(D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_text();need(md==(D/'ISA_Correction_Review_07NOV2026.md').read_text(),'both readable mirrors')
    class Table(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.cell=None
        def handle_starttag(self,t,attrs):
            if t=='tr':self.row=[]
            if t in ('td','th'):self.cell='';self.span=int(dict(attrs).get('colspan',1))
        def handle_data(self,d):
            if self.cell is not None:self.cell+=d
        def handle_endtag(self,t):
            if t in ('td','th'):self.row += [self.cell]+['']*(self.span-1);self.cell=None
            if t=='tr':self.rows.append(self.row)
    tab=Table();tab.feed(md[md.index('<table>'):md.index('</table>')+8]);need(tab.rows==m['review_grid'],'readable table values')
    saved=(D/BOOK).read_bytes();prior=f3_baseline(BOOK,AAS_O5_BASE);need(digest(saved)==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==o['publication']['workbook_sha256'],'saved hash')
    with zipfile.ZipFile(io.BytesIO(saved)) as z,zipfile.ZipFile(io.BytesIO(prior)) as bz:
        paths=old.sheetpaths(z);need(paths==old.sheetpaths(bz) and len(paths)==26 and z.testzip() is None,'same 26-sheet valid package')
        affected={paths[n] for n in o['publication']['affected_original_sheets']}
        need(z.namelist()==bz.namelist(),'same package parts/order')
        for name in z.namelist():
            if name not in affected:need(z.read(name)==bz.read(name),'unchanged package part '+name)
            if name.endswith(('.xml','.rels')):ET.fromstring(z.read(name))
        for name,nrows in [('Master Crosswalk',372),('DIM Register',353)]:
            rt=ET.fromstring(z.read(paths[name]));bt=ET.fromstring(bz.read(paths[name]));sd=rt.find(q('sheetData'));bs=bt.find(q('sheetData'))
            planned={x['master_cell']:x['after']['display'][6] for x in o['qualified_existing_rows']} if name=='Master Crosswalk' else o['register_changes']
            for rr in bs:
                for c in rr:
                    if c.get('r') in planned:f3_put(c,planned[c.get('r')])
            need([ET.tostring(r) for r in list(sd)[:nrows]]==[ET.tostring(r) for r in bs],'only planned saved values change; original styles preserved '+name)
        styles=ET.fromstring(z.read('xl/styles.xml'));xfs=list(styles.find(q('cellXfs')));fills=list(styles.find(q('fills')))
        cells=old.readcells(saved,'Master Crosswalk')
        for i,row in enumerate(m['review_grid'],1):
            for j,v in enumerate(row,1):need(cells.get(addr(i,j),'')==v,'saved value '+addr(i,j))
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));lookup={c.get('r'):c for c in rt.iter(q('c'))}
        for r in new:
            d=r['AAS_O5_source_correspondence'];c=lookup[d['cell']];fg=fills[int(xfs[int(c.get('s'))].get('fillId'))].find('.//'+q('fgColor'));need(fg.get('rgb')[-6:]==d['fill'][1:],'new actual fill '+d['cell'])
        for name in paths:
            rt=ET.fromstring(z.read(paths[name]));rownums=[]
            for rr in rt.find(q('sheetData')):
                rownums.append(int(rr.get('r')));nums=[]
                for c in rr.findall(q('c')):
                    n=0
                    for ch in re.match('[A-Z]+',c.get('r')).group():n=n*26+ord(ch)-64
                    nums.append(n);need(c.get('t')!='e','no error cell '+name)
                need(nums==sorted(set(nums)),'ordered unique cells '+name)
            need(rownums==sorted(set(rownums)),'ordered unique rows '+name)
        reg=old.readcells(saved,'DIM Register')
        for n,r in enumerate(new,354):need(reg['A'+str(n)]==r['row_id'] and reg['R'+str(n)].startswith(r['AAS_O5_source_correspondence']['candidate_status']),'saved candidate register')
    for name in ('M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx','M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx'):
        rel='Manual_Workbook_Versions/'+name;need((D/rel).read_bytes()==f3_baseline(rel,AAS_O5_BASE),'immutable '+name)
    need(not list((D/'Manual_Workbook_Versions').glob('M02*')),'no unapproved M02')
    need(a['one_next']==o['one_next']==m['nextOwnerAction']==m['AAS_O5_native_review']['one_next'],'one O6-1 stop boundary')
    print('PASS AAS O5: 53 native findings; two new candidates; three qualified AAS comparisons; all 631 prior classifications preserved.')
    print('PASS: all 6000 saved values, two new fills, both CSV/readable mirrors, 26 sheets, 21 untouched sheets and M00/M01.')
    print('LIMIT: AAS bounded PARTIAL; source conflicts and Excel clean reopen hold retained. Next O6-1 only.')


AAS_O6_1_BASE='f2f3ee836b7402ba58647224a1ed428fb76a7ac1'

def publish_aas_o6_1():
    """Extend the same saved package with source-qualified candidate rows; preserve original parts."""
    import copy, html
    m=load(MASTER);a=load(F3_PEER_FILES[-1]);o=a['AAS_O6_1_native_review'];grid=m['review_grid']
    prior=(D/BOOK).read_bytes();need(prior==f3_baseline(BOOK,AAS_O6_1_BASE),'exact archived pre-O6_1 workbook')
    need(m['currentEvidenceCheckpoint']=='AAS_O6_1_SOURCE_DECISIONS_PENDING_SAME_XLSX','O6_1 source checkpoint')
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/name).open('w',newline='',encoding='utf-8') as f:csv.writer(f,lineterminator='\n').writerows(grid)
    table=['<table><thead><tr>']
    for idx,span in ((0,4),(4,6),(10,5),(15,1)):table.append(f'<th colspan="{span}">{html.escape(grid[0][idx])}</th>')
    table+=['</tr><tr>'+''.join('<th>'+html.escape(v)+'</th>' for v in grid[1])+'</tr></thead><tbody>']
    for i,row in enumerate(grid[2:],2):table.append('<tr><th colspan="16">'+html.escape(row[0])+'</th></tr>' if i in m['review_sections'] else '<tr>'+''.join('<td>'+html.escape(v)+'</td>' for v in row)+'</tr>')
    table+=['</tbody></table>']
    banner='# CURRENT — F3 accepted; AAS O6-1 companion review complete (15 November 2026)\n\nAll 55 AAS08 findings reconciled, reusing unchanged original-source contact with targeted rereads for new decisions. Three common candidates added; two existing package/file comparisons qualified without reclassification. Current: 357 information rows; 636 source-bearing comparisons (528 colored / 108 held). All 633 prior classifications, unrelated cells and 26-sheet package preserved. Worksheet range/divider metadata corrected. Candidates are not adopted; AAS remains bounded PARTIAL and native Excel reopening pending. Next: separate Proceed for O6-2 industrial templates only.\n\n'
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        (D/name).write_text(banner+'\n'.join(table)+'\n',encoding='utf-8')
    with zipfile.ZipFile(io.BytesIO(prior)) as z:
        paths=old.sheetpaths(z);replacements={}
        def edited(name,changes):
            rt=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in rt.iter(q('c'))}
            for ref,value in changes.items():need(ref in cells,'existing guidance cell '+ref);f3_put(cells[ref],value)
            for rr in rt.find(q('sheetData')):
                vals=[v for k,v in changes.items() if re.search(r'\d+$',k).group()==rr.get('r')]
                if vals:rr.set('ht',str(min(409.5,max(float(rr.get('ht',15)),max(len(textwrap.wrap(v,95))*12+18 for v in vals)))));rr.set('customHeight','1')
            replacements[paths[name]]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));sd=rt.find(q('sheetData'));templates={int(r.get('r')):r for r in sd}
        def make_row(template,number,values):
            rr=copy.deepcopy(template);rr.set('r',str(number))
            for c in list(rr):rr.remove(c)
            styles={re.match('[A-Z]+',c.get('r')).group():c.get('s','0') for c in template}
            for j,v in enumerate(values,1):
                col=re.match('[A-Z]+',addr(number,j)).group();c=ET.SubElement(rr,q('c'),{'r':addr(number,j),'s':styles.get(col,'526')});f3_put(c,str(v))
            return rr
        for change in o['qualified_existing_rows']:
            rr=templates[change['after']['display_row']]
            cell=next(c for c in rr if c.get('r')==change['master_cell'])
            f3_put(cell,change['after']['display'][6])
        divider=make_row(templates[373],376,grid[375]);sd.append(divider)
        merges=rt.find(q('mergeCells'));need(merges is not None,'existing topic merges')
        seen=set()
        for merge in list(merges):
            if merge.get('ref') in seen:merges.remove(merge)
            else:seen.add(merge.get('ref'))
        for ref in ('A373:P373','A376:P376'):
            if ref not in seen:ET.SubElement(merges,q('mergeCell'),{'ref':ref});seen.add(ref)
        merges.set('count',str(len(merges)))
        for n,row in enumerate(m['rows'][354:],377):
            rr=make_row(templates[375],n,row['display']);rr.set('ht','240');rr.set('customHeight','1')
            for c in rr:
                col=re.match('[A-Z]+',c.get('r')).group()
                if col in ('G','H','I','J'):c.set('s','526' if n%2==0 else '527')
                if col=='G':c.set('s','528' if row['AAS_O6_1_source_correspondence']['candidate_status']=='COMMON_CANDIDATE' else '529')
            sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:P379')
        af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A2:P379')
        replacements[paths['Master Crosswalk']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['DIM Register']));sd=rt.find(q('sheetData'));template=list(sd)[-1]
        register_cells={c.get('r'):c for c in rt.iter(q('c'))}
        for ref,value in o['register_changes'].items():f3_put(register_cells[ref],value)
        for n,row in enumerate(m['rows'][354:],356):
            c=row['AAS_O6_1_source_correspondence'];ids=', '.join(c['source_ids'])
            vals=[row['row_id'],row['label'],row['definition'],row['status'],row['source_review_status'],row['master_inclusion'],row['dim_adoption'],'','Not assessed here','','Not assessed here','AAS pinned Parts 3b/4 targeted text; individual source editions govern; no observed case','Not assessed here','Not assessed here','Not assessed here','O6_1 sources: '+ids,ids+'; '+c['relation']+'; '+c['reason_for_separate_candidate'],c['candidate_status']+' — '+c['native_meaning']]
            rr=make_row(template,n,vals);rr.set('ht','240');rr.set('customHeight','1');sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:R358');af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A1:R358')
        replacements[paths['DIM Register']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        guidance={'A1': 'CURRENT 15 NOV 2026 — F3 accepted; AAS O6-1 complete', 'B1': 'Current: 357 information rows in the same 26-sheet master. AAS active bounded PARTIAL; M00/M01 frozen. Earlier labeled checkpoints are historical.', 'A17': 'Current completed scope', 'B17': 'O6-1: 55 AAS08 companion findings reconciled; three common candidates added and two package/file comparisons qualified. All 633 prior classifications unchanged.', 'B19': '357 information rows; 636 source comparisons: 528 colored, 108 held. AAS 72 colored / 12 held across 84 comparisons. Other donor positions retain explicit statuses.', 'B21': 'Prior pinned source contact reused; 19 original-file hashes matched. Selected passages in 8 original files reread for unit, policy, audit and package decisions. External and figure limits remain.', 'B22': 'New: unit definition and quantity context; access-rule definition and protected information; security/accountability audit record. Existing package/file rows clarified. No model adoption or demonstrated enforcement.', 'A23': 'Next step and remaining limits', 'B23': 'Await owner Proceed for O6-2: 37 AAS09 industrial-template findings. Stop before O7 reconciliation. AAS bounded PARTIAL; actual Microsoft Excel clean reopen pending.', 'A28': 'Current O6-1 saved-file verification', 'B28': 'O6-1: all 6,064 saved grid values, three new fills and two qualified AAS comparisons/register entries checked. Range/divider metadata corrected. All prior classifications, 21 untouched sheets and M00/M01 preserved.'}
        edited('Summary',guidance);edited('Validation',guidance)
        edited('Legend',{'A1': 'CURRENT LEGEND — F3 accepted; O6-1 candidates and qualifications', 'A23': 'Current classification totals', 'B23': 'Current: 528 colored / 108 held source comparisons. Earlier F2/F3/O2/O3/O4/O5 counts are historical.', 'B24': '357 information rows, 379 × 16 saved comparison grid', 'A28': 'AAS O6-1 additions and current boundary', 'B28': 'Three new common candidates (blue); two existing package/file comparisons qualified with their classifications retained. Color is not adoption, equivalence or source completeness. Next O6-2 industrial templates.'})
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as dst:
            for info in z.infolist():dst.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    saved=buf.getvalue();(D/BOOK).write_bytes(saved);sha=digest(saved)
    m['currentEvidenceCheckpoint']='AAS_O6_1_SAVED_VERIFIED';m['currentWorkbookSha256']=sha;m['workbookSnapshot'].update(checkpoint=m['currentEvidenceCheckpoint'],sha256=sha,currently_matches_readable_view=True,lag='ZERO: 379x16 grid and current O6_1 owner routing',textCheckpoint='AAS_O6_1_NATIVE_CANDIDATES',validation_file=F3_PEER_FILES[-1]+'#/AAS_O6_1_native_review/publication')
    m['AAS_O6_1_native_review']['status']='O6_1_COMPLETE__O6_2_PENDING_OWNER_PROCEED'
    o['status']='O6_1_COMPLETE__O6_2_PENDING_OWNER_PROCEED';o['publication']={'workbook_sha256':sha,'previous_workbook_sha256':digest(prior),'affected_original_sheets':['Master Crosswalk','DIM Register','Summary','Validation','Legend'],'unchanged_sheet_parts':21,'grid_values':6064,'new_candidate_cells':['G'+str(i) for i in range(377,380)],'existing_values_and_fills':'Two AAS cells and their register entries qualified; all prior fills/classifications and unrelated cells unchanged','range_divider_metadata_repair':o['workbook_metadata_repair'],'M00_M01_preserved':True,'M02_created':False,'actual_Microsoft_Excel_clean_reopen':'PENDING','visual_review':'PENDING','remote_publication':'PENDING'}
    a['status']='AAS_ACTIVE_BOUNDED_PARTIAL__O6_1_COMPLETE';a['master_state_current'].update(checkpoint=m['currentEvidenceCheckpoint'],comparison_lag=0,status='O6_1_COMPLETE__O6_2_PENDING',workbook_metadata_lag='ZERO: current O6_1 guidance refreshed; labeled historical checkpoints retained.')
    save(MASTER,m);save(F3_PEER_FILES[-1],a);verify_aas_o6_1()


def verify_aas_o6_1():
    """Check the bounded native reconciliation and saved file against the archived O5 result."""
    import copy
    from collections import Counter
    from html.parser import HTMLParser
    m=load(MASTER);base=json.loads(f3_baseline(MASTER,AAS_O6_1_BASE));a=load(F3_PEER_FILES[-1]);ab=json.loads(f3_baseline(F3_PEER_FILES[-1],AAS_O6_1_BASE));o=a['AAS_O6_1_native_review']
    need(m['currentEvidenceCheckpoint']=='AAS_O6_1_SAVED_VERIFIED','O6_1 checkpoint')
    changes={x['row_id']:x for x in o['qualified_existing_rows']}
    need(set(changes)=={'AAS-O2-SUPPORTING-CONTENT','AAS-O5-PACKAGE-ASSOCIATION'},'two authorized existing-row qualifications')
    restored_rows=copy.deepcopy(m['rows'][:354]);restored_grid=copy.deepcopy(m['review_grid'][:375])
    for idx,row in enumerate(restored_rows):
        if row['row_id'] in changes:
            change=changes[row['row_id']];need(row==change['after'] and base['rows'][idx]==change['before'],'exact recorded before/after')
            oldrow=change['before'];need(row['display'][:6]+row['display'][7:]==oldrow['display'][:6]+oldrow['display'][7:],'only AAS display cell changes')
            oldrow=change['before']
            need(not change['classification_changed'] and row['display'][6].split(']')[0]==oldrow['display'][6].split(']')[0],'existing classification retained')
            for key,value in oldrow.items():
                if key not in ('display','definition','display_row'):need(row[key]==value,'preserved prior evidence '+key)
            restored_rows[idx]=oldrow;restored_grid[row['display_row']-1]=oldrow['display']
    need(restored_rows==base['rows'] and restored_grid==base['review_grid'],'all other existing rows/cells unchanged')
    need(m['columns']==base['columns'] and m['review_sections']==base['review_sections']+[375],'approved layout plus appended topic')
    need(len(m['rows'])==357 and len(m['review_grid'])==379 and all(len(r)==16 for r in m['review_grid']),'354 rows / 379x16 grid')
    allowed={'rows','review_grid','review_sections','counts','currentEvidenceCheckpoint','currentWorkbookSha256','workbookSnapshot','nextOwnerAction'}
    for k,v in base.items():
        if k not in allowed:need(m[k]==v,'preserved master evidence '+k)
    for k,v in base['counts'].items():
        if k not in ('informationRows','AAS_current_source_bearing_comparisons'):need(m['counts'][k]==v,'preserved historical count '+k)
    need(m['counts']['informationRows']==357 and m['counts']['AAS_current_source_bearing_comparisons']==84,'current counts')
    restored=copy.deepcopy(a);restored.pop('AAS_O6_1_native_review')
    for k in ('status','one_next','master_state_current'):restored[k]=ab[k]
    need(restored==ab,'all prior findings, holds and decisions unchanged')
    native={x['source_id']:x for x in a['AAS08']['original_items']}
    required=set(native);rs=o['records']
    need(len(rs)==55 and {r['source_id'] for r in rs}==required,'55 unique AAS08 findings')
    need(len(o['targeted_original_contacts'])==8,'8 sampled original source files')
    expected_files={(r['original_corpus_source_id'],r['source_file']):(r['git_commit'],r['source_blob']) for r in native.values()}
    need(len(expected_files)==len(o['unchanged_original_file_checks'])==19,'19 immutable original-file checks')
    for f in o['unchanged_original_file_checks']:need(expected_files[(f['corpus'],f['path'])]==(f['commit'],f['blob']),'retained original pin')
    for f in o['targeted_original_contacts']:need(expected_files[(f['corpus'],f['file'])]==(f['commit'],f['blob']) and f['ranges'],'targeted original locator')
    need(len(o['historical_53_in_O6_1'])==17,'17 historically uncited findings dispositioned')
    rowids={r['row_id'] for r in m['rows']};need(len(rowids)==357,'unique row IDs')
    for r in rs:
        need(digest(json.dumps(native[r['source_id']],sort_keys=True,ensure_ascii=False).encode())==r['original_record_sha256'],'original evidence hash '+r['source_id'])
        need(set(r['row_ids'])<=rowids and r['rationale'] and r['relation'] and not r['DIM_Profile_adopted'],'qualified disposition '+r['source_id'])
    new=m['rows'][354:];need([r['row_id'] for r in new]==o['new_candidate_row_ids'],'three stable candidate IDs')
    need(Counter(r['AAS_O6_1_source_correspondence']['candidate_status'] for r in new)=={'COMMON_CANDIDATE':3},'candidate classifications')
    for r in new:
        c=r['AAS_O6_1_source_correspondence'];need(set(c['source_ids'])<=required and c['reason_for_separate_candidate'] and not c['DIM_Profile_adopted'],'candidate source evidence')
        need(all(v.strip() for v in r['display']),'explicit new row states')
        need(m['review_grid'][r['display_row']-1]==r['display'],'candidate display placement')
    need(source_csv('Master_Donor_Concept_to_DIM_Crosswalk.csv')==m['review_grid']==source_csv('ISA_Correction_Review_07NOV2026.csv'),'both CSV mirrors')
    md=(D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_text();need(md==(D/'ISA_Correction_Review_07NOV2026.md').read_text(),'both readable mirrors')
    class Table(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.cell=None
        def handle_starttag(self,t,attrs):
            if t=='tr':self.row=[]
            if t in ('td','th'):self.cell='';self.span=int(dict(attrs).get('colspan',1))
        def handle_data(self,d):
            if self.cell is not None:self.cell+=d
        def handle_endtag(self,t):
            if t in ('td','th'):self.row += [self.cell]+['']*(self.span-1);self.cell=None
            if t=='tr':self.rows.append(self.row)
    tab=Table();tab.feed(md[md.index('<table>'):md.index('</table>')+8]);need(tab.rows==m['review_grid'],'readable table values')
    saved=(D/BOOK).read_bytes();prior=f3_baseline(BOOK,AAS_O6_1_BASE);need(digest(saved)==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==o['publication']['workbook_sha256'],'saved hash')
    with zipfile.ZipFile(io.BytesIO(saved)) as z,zipfile.ZipFile(io.BytesIO(prior)) as bz:
        paths=old.sheetpaths(z);need(paths==old.sheetpaths(bz) and len(paths)==26 and z.testzip() is None,'same 26-sheet valid package')
        affected={paths[n] for n in o['publication']['affected_original_sheets']}
        need(z.namelist()==bz.namelist(),'same package parts/order')
        for name in z.namelist():
            if name not in affected:need(z.read(name)==bz.read(name),'unchanged package part '+name)
            if name.endswith(('.xml','.rels')):ET.fromstring(z.read(name))
        for name,nrows in [('Master Crosswalk',375),('DIM Register',355)]:
            rt=ET.fromstring(z.read(paths[name]));bt=ET.fromstring(bz.read(paths[name]));sd=rt.find(q('sheetData'));bs=bt.find(q('sheetData'))
            planned={x['master_cell']:x['after']['display'][6] for x in o['qualified_existing_rows']} if name=='Master Crosswalk' else o['register_changes']
            for rr in bs:
                for c in rr:
                    if c.get('r') in planned:f3_put(c,planned[c.get('r')])
            need([ET.tostring(r) for r in list(sd)[:nrows]]==[ET.tostring(r) for r in bs],'only planned saved values change; original styles preserved '+name)
        styles=ET.fromstring(z.read('xl/styles.xml'));xfs=list(styles.find(q('cellXfs')));fills=list(styles.find(q('fills')))
        cells=old.readcells(saved,'Master Crosswalk')
        for i,row in enumerate(m['review_grid'],1):
            for j,v in enumerate(row,1):need(cells.get(addr(i,j),'')==v,'saved value '+addr(i,j))
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));lookup={c.get('r'):c for c in rt.iter(q('c'))}
        for r in new:
            d=r['AAS_O6_1_source_correspondence'];c=lookup[d['cell']];fg=fills[int(xfs[int(c.get('s'))].get('fillId'))].find('.//'+q('fgColor'));need(fg.get('rgb')[-6:]==d['fill'][1:],'new actual fill '+d['cell'])
        for name in paths:
            rt=ET.fromstring(z.read(paths[name]));rownums=[]
            for rr in rt.find(q('sheetData')):
                rownums.append(int(rr.get('r')));nums=[]
                for c in rr.findall(q('c')):
                    n=0
                    for ch in re.match('[A-Z]+',c.get('r')).group():n=n*26+ord(ch)-64
                    nums.append(n);need(c.get('t')!='e','no error cell '+name)
                need(nums==sorted(set(nums)),'ordered unique cells '+name)
            need(rownums==sorted(set(rownums)),'ordered unique rows '+name)
        for name,last in [('Master Crosswalk','P379'),('DIM Register','R358')]:
            rt=ET.fromstring(z.read(paths[name]));need(rt.find(q('dimension')).get('ref')=='A1:'+last,'current used range '+name)
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));merges=rt.find(q('mergeCells'));refs=[x.get('ref') for x in merges]
        need(len(refs)==len(set(refs))==int(merges.get('count')),'unique topic merges')
        oldrefs=[x.get('ref') for x in ET.fromstring(bz.read(paths['Master Crosswalk'])).find(q('mergeCells'))]
        need(set(refs)==set(oldrefs)|{'A373:P373','A376:P376'},'only recorded divider corrections')
        need(all('A'+str(i+1)+':P'+str(i+1) in refs for i in m['review_sections']),'all topic dividers merged')
        need(all(cells.get('G'+str(r['display_row']))==r['display'][6] for r in new),'new candidates in saved used range')
        reg=old.readcells(saved,'DIM Register')
        for n,r in enumerate(new,356):need(reg['A'+str(n)]==r['row_id'] and reg['R'+str(n)].startswith(r['AAS_O6_1_source_correspondence']['candidate_status']),'saved candidate register')
    for name in ('M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx','M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx'):
        rel='Manual_Workbook_Versions/'+name;need((D/rel).read_bytes()==f3_baseline(rel,AAS_O6_1_BASE),'immutable '+name)
    need(not list((D/'Manual_Workbook_Versions').glob('M02*')),'no unapproved M02')
    need(a['one_next']==o['one_next']==m['nextOwnerAction']==m['AAS_O6_1_native_review']['one_next'],'one O6-2 stop boundary')
    print('PASS AAS O6_1: 55 native findings; three common candidates; two qualified AAS comparisons; all 633 prior classifications preserved.')
    print('PASS: all 6064 saved values, three new fills, both CSV/readable mirrors, 26 sheets, 21 untouched sheets and M00/M01.')
    print('LIMIT: AAS bounded PARTIAL; source conflicts and Excel clean reopen hold retained. Next O6-2 only.')


AAS_O6_2_BASE='dab42da47f58ff41f58182d2325ed8de136d81b5'

def publish_aas_o6_2():
    """Extend the same saved package with source-qualified candidate rows; preserve original parts."""
    import copy, html
    m=load(MASTER);a=load(F3_PEER_FILES[-1]);o=a['AAS_O6_2_native_review'];grid=m['review_grid']
    prior=(D/BOOK).read_bytes();need(prior==f3_baseline(BOOK,AAS_O6_2_BASE),'exact archived pre-O6_2 workbook')
    need(m['currentEvidenceCheckpoint']=='AAS_O6_2_SOURCE_DECISIONS_PENDING_SAME_XLSX','O6_2 source checkpoint')
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/name).open('w',newline='',encoding='utf-8') as f:csv.writer(f,lineterminator='\n').writerows(grid)
    table=['<table><thead><tr>']
    for idx,span in ((0,4),(4,6),(10,5),(15,1)):table.append(f'<th colspan="{span}">{html.escape(grid[0][idx])}</th>')
    table+=['</tr><tr>'+''.join('<th>'+html.escape(v)+'</th>' for v in grid[1])+'</tr></thead><tbody>']
    for i,row in enumerate(grid[2:],2):table.append('<tr><th colspan="16">'+html.escape(row[0])+'</th></tr>' if i in m['review_sections'] else '<tr>'+''.join('<td>'+html.escape(v)+'</td>' for v in row)+'</tr>')
    table+=['</tbody></table>']
    banner='# CURRENT — F3 accepted; AAS O6-2 industrial-template review complete (15 November 2026)\n\nAll 37 AAS09 findings reconciled, reusing unchanged original contact with targeted text/table/native-field reads. Four candidates added (three common, one specialized); one existing relationship comparison qualified without reclassification. Current: 361 information rows; 640 source-bearing comparisons (532 colored / 108 held). All 636 prior classifications, unrelated cells and 26-sheet package preserved. Candidates are not adopted; AAS remains bounded PARTIAL and native Excel reopening pending. Next: separate Proceed for O7 reconciliation and owner-facing closeout proposal only.\n\n'
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        (D/name).write_text(banner+'\n'.join(table)+'\n',encoding='utf-8')
    with zipfile.ZipFile(io.BytesIO(prior)) as z:
        paths=old.sheetpaths(z);replacements={}
        def edited(name,changes):
            rt=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in rt.iter(q('c'))}
            for ref,value in changes.items():need(ref in cells,'existing guidance cell '+ref);f3_put(cells[ref],value)
            for rr in rt.find(q('sheetData')):
                vals=[v for k,v in changes.items() if re.search(r'\d+$',k).group()==rr.get('r')]
                if vals:rr.set('ht',str(min(409.5,max(float(rr.get('ht',15)),max(len(textwrap.wrap(v,95))*12+18 for v in vals)))));rr.set('customHeight','1')
            replacements[paths[name]]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));sd=rt.find(q('sheetData'));templates={int(r.get('r')):r for r in sd}
        def make_row(template,number,values):
            rr=copy.deepcopy(template);rr.set('r',str(number))
            for c in list(rr):rr.remove(c)
            styles={re.match('[A-Z]+',c.get('r')).group():c.get('s','0') for c in template}
            for j,v in enumerate(values,1):
                col=re.match('[A-Z]+',addr(number,j)).group();c=ET.SubElement(rr,q('c'),{'r':addr(number,j),'s':styles.get(col,'526')});f3_put(c,str(v))
            return rr
        for change in o['qualified_existing_rows']:
            rr=templates[change['after']['display_row']]
            cell=next(c for c in rr if c.get('r')==change['master_cell'])
            f3_put(cell,change['after']['display'][6])
        divider=make_row(templates[376],380,grid[379]);sd.append(divider)
        merges=rt.find(q('mergeCells'));need(merges is not None,'existing topic merges')
        seen=set()
        for merge in list(merges):
            if merge.get('ref') in seen:merges.remove(merge)
            else:seen.add(merge.get('ref'))
        for ref in ('A380:P380',):
            if ref not in seen:ET.SubElement(merges,q('mergeCell'),{'ref':ref});seen.add(ref)
        merges.set('count',str(len(merges)))
        for n,row in enumerate(m['rows'][357:],381):
            rr=make_row(templates[379],n,row['display']);rr.set('ht','240');rr.set('customHeight','1')
            for c in rr:
                col=re.match('[A-Z]+',c.get('r')).group()
                if col in ('G','H','I','J'):c.set('s','526' if n%2==0 else '527')
                if col=='G':c.set('s','528' if row['AAS_O6_2_source_correspondence']['candidate_status']=='COMMON_CANDIDATE' else '529')
            sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:P384')
        af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A2:P384')
        replacements[paths['Master Crosswalk']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        rt=ET.fromstring(z.read(paths['DIM Register']));sd=rt.find(q('sheetData'));template=list(sd)[-1]
        register_cells={c.get('r'):c for c in rt.iter(q('c'))}
        for ref,value in o['register_changes'].items():f3_put(register_cells[ref],value)
        for n,row in enumerate(m['rows'][357:],359):
            c=row['AAS_O6_2_source_correspondence'];ids=', '.join(c['source_ids'])
            vals=[row['row_id'],row['label'],row['definition'],row['status'],row['source_review_status'],row['master_inclusion'],row['dim_adoption'],'','Not assessed here','','Not assessed here','AAS industrial templates: selected pinned text/tables/native fields; individual editions govern; no observed case','Not assessed here','Not assessed here','Not assessed here','O6_2 sources: '+ids,ids+'; '+c['relation']+'; '+c['reason_for_separate_candidate'],c['candidate_status']+' — '+c['native_meaning']]
            rr=make_row(template,n,vals);rr.set('ht','240');rr.set('customHeight','1');sd.append(rr)
        dim=rt.find(q('dimension'))
        if dim is None:
            dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
        dim.set('ref','A1:R362');af=rt.find(q('autoFilter'))
        if af is not None:af.set('ref','A1:R362')
        replacements[paths['DIM Register']]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        guidance={'A1':'CURRENT 15 NOV 2026 — F3 accepted; AAS O6-2 complete','B1':'Current: 361 information rows in the same 26-sheet master. AAS active bounded PARTIAL; M00/M01 frozen. Earlier labeled checkpoints are historical.','A17':'Current completed scope','B17':'O6-2: all 37 AAS09 template findings reconciled; four candidates added (three common, one specialized), one relationship comparison qualified. All 636 prior classifications unchanged.','B19':'361 information rows; 640 source comparisons: 532 colored, 108 held. AAS 76 colored / 12 held across 88 comparisons. Other donor positions retain explicit statuses.','B21':'12 original-artifact SHA-256 matches; one earlier Git blob metadata error explicitly corrected by fresh provider readback. Selected text/native fields in three templates and four visual table pages reviewed; other contact reused.','B22':'New: engineering reference designations, product classification, capability property conditions and cross-capability dependencies. Functional composition/generalization clarified in existing relationship row. No model adoption or execution proof.','A23':'Next step and remaining limits','B23':'Await owner Proceed for O7 only: final AAS reconciliation and closeout proposal. Stop for owner disposition. AAS bounded PARTIAL; actual Microsoft Excel clean reopen pending.','A28':'Current O6-2 saved-file verification','B28':'O6-2: all 6,144 saved grid values, four new fills and one qualified comparison/register entry checked. All prior classifications, 21 untouched sheets and M00/M01 preserved.'}
        edited('Summary',guidance);edited('Validation',guidance)
        edited('Legend',{'A1':'CURRENT LEGEND — F3 accepted; O6-2 candidates and qualification','A23':'Current classification totals','B23':'Current: 532 colored / 108 held source comparisons. Earlier F2/F3/O2/O3/O4/O5/O6-1 counts are historical.','B24':'361 information rows, 384 × 16 saved comparison grid','A28':'AAS O6-2 additions and current boundary','B28':'Three common candidates (blue) and one specialized engineering-designation candidate (amber). Existing relationship classification retained. Color is not adoption, equivalence or source completeness. Next O7 reconciliation and owner proposal only.'})
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as dst:
            for info in z.infolist():dst.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    saved=buf.getvalue();(D/BOOK).write_bytes(saved);sha=digest(saved)
    m['currentEvidenceCheckpoint']='AAS_O6_2_SAVED_VERIFIED';m['currentWorkbookSha256']=sha;m['workbookSnapshot'].update(checkpoint=m['currentEvidenceCheckpoint'],sha256=sha,currently_matches_readable_view=True,lag='ZERO: 384x16 grid and current O6_2 owner routing',textCheckpoint='AAS_O6_2_NATIVE_CANDIDATES',validation_file=F3_PEER_FILES[-1]+'#/AAS_O6_2_native_review/publication')
    m['AAS_O6_2_native_review']['status']='O6_2_COMPLETE__O7_PENDING_OWNER_PROCEED'
    o['status']='O6_2_COMPLETE__O7_PENDING_OWNER_PROCEED';o['publication']={'workbook_sha256':sha,'previous_workbook_sha256':digest(prior),'affected_original_sheets':['Master Crosswalk','DIM Register','Summary','Validation','Legend'],'unchanged_sheet_parts':21,'grid_values':6144,'new_candidate_cells':['G'+str(i) for i in range(381,385)],'existing_values_and_fills':'One AAS relationship cell and its register entry qualified; all prior fills/classifications and unrelated cells unchanged','range_divider_metadata_repair':o['workbook_metadata_repair'],'M00_M01_preserved':True,'M02_created':False,'actual_Microsoft_Excel_clean_reopen':'PENDING','visual_review':'PENDING','remote_publication':'PENDING'}
    a['status']='AAS_ACTIVE_BOUNDED_PARTIAL__O6_2_COMPLETE';a['master_state_current'].update(checkpoint=m['currentEvidenceCheckpoint'],comparison_lag=0,status='O6_2_COMPLETE__O7_PENDING',workbook_metadata_lag='ZERO: current O6_2 guidance refreshed; labeled historical checkpoints retained.')
    save(MASTER,m);save(F3_PEER_FILES[-1],a);verify_aas_o6_2()


def verify_aas_o6_2():
    """Check the bounded native reconciliation and saved file against the archived O6-1 result."""
    import copy
    from collections import Counter
    from html.parser import HTMLParser
    m=load(MASTER);base=json.loads(f3_baseline(MASTER,AAS_O6_2_BASE));a=load(F3_PEER_FILES[-1]);ab=json.loads(f3_baseline(F3_PEER_FILES[-1],AAS_O6_2_BASE));o=a['AAS_O6_2_native_review']
    need(m['currentEvidenceCheckpoint']=='AAS_O6_2_SAVED_VERIFIED','O6_2 checkpoint')
    changes={x['row_id']:x for x in o['qualified_existing_rows']}
    need(set(changes)=={'AAS-O2-LOGICAL-RELATION'},'one authorized relationship qualification')
    restored_rows=copy.deepcopy(m['rows'][:357]);restored_grid=copy.deepcopy(m['review_grid'][:379])
    for idx,row in enumerate(restored_rows):
        if row['row_id'] in changes:
            change=changes[row['row_id']];need(row==change['after'] and base['rows'][idx]==change['before'],'exact recorded before/after')
            oldrow=change['before'];need(row['display'][:6]+row['display'][7:]==oldrow['display'][:6]+oldrow['display'][7:],'only AAS display cell changes')
            oldrow=change['before']
            need(not change['classification_changed'] and row['display'][6].split(']')[0]==oldrow['display'][6].split(']')[0],'existing classification retained')
            for key,value in oldrow.items():
                if key not in ('display','definition','display_row'):need(row[key]==value,'preserved prior evidence '+key)
            restored_rows[idx]=oldrow;restored_grid[row['display_row']-1]=oldrow['display']
    need(restored_rows==base['rows'] and restored_grid==base['review_grid'],'all other existing rows/cells unchanged')
    need(m['columns']==base['columns'] and m['review_sections']==base['review_sections']+[379],'approved layout plus appended topic')
    need(len(m['rows'])==361 and len(m['review_grid'])==384 and all(len(r)==16 for r in m['review_grid']),'357 rows / 384x16 grid')
    allowed={'rows','review_grid','review_sections','counts','currentEvidenceCheckpoint','currentWorkbookSha256','workbookSnapshot','nextOwnerAction'}
    for k,v in base.items():
        if k not in allowed:need(m[k]==v,'preserved master evidence '+k)
    for k,v in base['counts'].items():
        if k not in ('informationRows','AAS_current_source_bearing_comparisons'):need(m['counts'][k]==v,'preserved historical count '+k)
    need(m['counts']['informationRows']==361 and m['counts']['AAS_current_source_bearing_comparisons']==88,'current counts')
    restored=copy.deepcopy(a);restored.pop('AAS_O6_2_native_review')
    for k in ('status','one_next','master_state_current'):restored[k]=ab[k]
    need(restored==ab,'all prior findings, holds and decisions unchanged')
    native={x['source_id']:x for x in a['AAS09']['original_items']}
    required=set(native);rs=o['records']
    need(len(rs)==37 and {r['source_id'] for r in rs}==required,'37 unique AAS09 findings')
    need(len(o['targeted_original_contacts'])==3,'three targeted template PDFs/native JSONs')
    pins=a['AAS09']['source_pins'];sourcefiles={x['source_file']:x for x in a['AAS09']['source_file_coverage']}
    expected={pin[k]:pin['git_commit'] for pin in pins for k in ('pdf_path','json_path','aasx_path')}
    checks=o['unchanged_original_file_checks'];need(len(checks)==12 and {f['path'] for f in checks}==set(expected),'12 pinned original artifacts')
    for f in checks:
        oldf=sourcefiles[f['path']];need((f['commit'],f['sha256'],f['recorded_git_blob'])==(expected[f['path']],oldf['sha256'],oldf['git_blob']),'retained source hash and original record')
    mismatches=[f for f in checks if f['verified_git_blob']!=f['recorded_git_blob']];fix=o['source_metadata_correction']
    need(len(mismatches)==1 and mismatches[0]['source_id']=='AAS09-F022','one explicit historical metadata correction')
    need(fix['verified_git_blob']==fix['provider_readback_blob']=='ce9540a38e1232ee3cdd38e7e2939304ea5ed786' and fix['sha256']==sourcefiles[fix['path']]['sha256'],'fresh provider pin correction with unchanged content hash')
    for f in o['targeted_original_contacts']:
        need(f['commit']==expected[f['source_file']] and f['sha256']==sourcefiles[f['source_file']]['sha256'] and f['text_pages_read'] and f['native_fields_read'],'targeted contact locator')
        need(set(f['table_pages_visually_inspected'])<=set(f['text_pages_read']),'bounded visual contact')
    need(len(o['historical_53_in_O6_2'])==4,'four historically uncited findings dispositioned')
    rowids={r['row_id'] for r in m['rows']};need(len(rowids)==361,'unique row IDs')
    for r in rs:
        need(digest(json.dumps(native[r['source_id']],sort_keys=True,ensure_ascii=False).encode())==r['original_record_sha256'],'original evidence hash '+r['source_id'])
        need(set(r['row_ids'])<=rowids and r['rationale'] and r['relation'] and not r['DIM_Profile_adopted'],'qualified disposition '+r['source_id'])
    new=m['rows'][357:];need([r['row_id'] for r in new]==o['new_candidate_row_ids'],'four stable candidate IDs')
    need(Counter(r['AAS_O6_2_source_correspondence']['candidate_status'] for r in new)=={'COMMON_CANDIDATE':3,'SPECIALIZED_CANDIDATE':1},'candidate classifications')
    for r in new:
        c=r['AAS_O6_2_source_correspondence'];need(set(c['source_ids'])<=required and c['reason_for_separate_candidate'] and not c['DIM_Profile_adopted'],'candidate source evidence')
        need(all(v.strip() for v in r['display']),'explicit new row states')
        need(m['review_grid'][r['display_row']-1]==r['display'],'candidate display placement')
    need(source_csv('Master_Donor_Concept_to_DIM_Crosswalk.csv')==m['review_grid']==source_csv('ISA_Correction_Review_07NOV2026.csv'),'both CSV mirrors')
    md=(D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_text();need(md==(D/'ISA_Correction_Review_07NOV2026.md').read_text(),'both readable mirrors')
    class Table(HTMLParser):
        def __init__(self):super().__init__(convert_charrefs=True);self.rows=[];self.cell=None
        def handle_starttag(self,t,attrs):
            if t=='tr':self.row=[]
            if t in ('td','th'):self.cell='';self.span=int(dict(attrs).get('colspan',1))
        def handle_data(self,d):
            if self.cell is not None:self.cell+=d
        def handle_endtag(self,t):
            if t in ('td','th'):self.row += [self.cell]+['']*(self.span-1);self.cell=None
            if t=='tr':self.rows.append(self.row)
    tab=Table();tab.feed(md[md.index('<table>'):md.index('</table>')+8]);need(tab.rows==m['review_grid'],'readable table values')
    saved=(D/BOOK).read_bytes();prior=f3_baseline(BOOK,AAS_O6_2_BASE);need(digest(saved)==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==o['publication']['workbook_sha256'],'saved hash')
    with zipfile.ZipFile(io.BytesIO(saved)) as z,zipfile.ZipFile(io.BytesIO(prior)) as bz:
        paths=old.sheetpaths(z);need(paths==old.sheetpaths(bz) and len(paths)==26 and z.testzip() is None,'same 26-sheet valid package')
        affected={paths[n] for n in o['publication']['affected_original_sheets']}
        need(z.namelist()==bz.namelist(),'same package parts/order')
        for name in z.namelist():
            if name not in affected:need(z.read(name)==bz.read(name),'unchanged package part '+name)
            if name.endswith(('.xml','.rels')):ET.fromstring(z.read(name))
        for name,nrows in [('Master Crosswalk',379),('DIM Register',358)]:
            rt=ET.fromstring(z.read(paths[name]));bt=ET.fromstring(bz.read(paths[name]));sd=rt.find(q('sheetData'));bs=bt.find(q('sheetData'))
            planned={x['master_cell']:x['after']['display'][6] for x in o['qualified_existing_rows']} if name=='Master Crosswalk' else o['register_changes']
            for rr in bs:
                for c in rr:
                    if c.get('r') in planned:f3_put(c,planned[c.get('r')])
            need([ET.tostring(r) for r in list(sd)[:nrows]]==[ET.tostring(r) for r in bs],'only planned saved values change; original styles preserved '+name)
        styles=ET.fromstring(z.read('xl/styles.xml'));xfs=list(styles.find(q('cellXfs')));fills=list(styles.find(q('fills')))
        cells=old.readcells(saved,'Master Crosswalk')
        for i,row in enumerate(m['review_grid'],1):
            for j,v in enumerate(row,1):need(cells.get(addr(i,j),'')==v,'saved value '+addr(i,j))
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));lookup={c.get('r'):c for c in rt.iter(q('c'))}
        for r in new:
            d=r['AAS_O6_2_source_correspondence'];c=lookup[d['cell']];fg=fills[int(xfs[int(c.get('s'))].get('fillId'))].find('.//'+q('fgColor'));need(fg.get('rgb')[-6:]==d['fill'][1:],'new actual fill '+d['cell'])
        for name in paths:
            rt=ET.fromstring(z.read(paths[name]));rownums=[]
            for rr in rt.find(q('sheetData')):
                rownums.append(int(rr.get('r')));nums=[]
                for c in rr.findall(q('c')):
                    n=0
                    for ch in re.match('[A-Z]+',c.get('r')).group():n=n*26+ord(ch)-64
                    nums.append(n);need(c.get('t')!='e','no error cell '+name)
                need(nums==sorted(set(nums)),'ordered unique cells '+name)
            need(rownums==sorted(set(rownums)),'ordered unique rows '+name)
        for name,last in [('Master Crosswalk','P384'),('DIM Register','R362')]:
            rt=ET.fromstring(z.read(paths[name]));need(rt.find(q('dimension')).get('ref')=='A1:'+last,'current used range '+name)
        rt=ET.fromstring(z.read(paths['Master Crosswalk']));merges=rt.find(q('mergeCells'));refs=[x.get('ref') for x in merges]
        need(len(refs)==len(set(refs))==int(merges.get('count')),'unique topic merges')
        oldrefs=[x.get('ref') for x in ET.fromstring(bz.read(paths['Master Crosswalk'])).find(q('mergeCells'))]
        need(set(refs)==set(oldrefs)|{'A380:P380'},'only recorded divider corrections')
        need(all('A'+str(i+1)+':P'+str(i+1) in refs for i in m['review_sections']),'all topic dividers merged')
        need(all(cells.get('G'+str(r['display_row']))==r['display'][6] for r in new),'new candidates in saved used range')
        reg=old.readcells(saved,'DIM Register')
        for n,r in enumerate(new,359):need(reg['A'+str(n)]==r['row_id'] and reg['R'+str(n)].startswith(r['AAS_O6_2_source_correspondence']['candidate_status']),'saved candidate register')
    for name in ('M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx','M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx'):
        rel='Manual_Workbook_Versions/'+name;need((D/rel).read_bytes()==f3_baseline(rel,AAS_O6_2_BASE),'immutable '+name)
    need(not list((D/'Manual_Workbook_Versions').glob('M02*')),'no unapproved M02')
    need(a['one_next']==o['one_next']==m['nextOwnerAction']==m['AAS_O6_2_native_review']['one_next'],'one O7 owner boundary')
    print('PASS AAS O6_2: 37 native findings; four candidates (three common, one specialized); one qualified AAS comparison; all 636 prior classifications preserved.')
    print('PASS: all 6144 saved values, four new fills, both CSV/readable mirrors, 26 sheets, 21 untouched sheets and M00/M01.')
    print('LIMIT: AAS bounded PARTIAL; source conflicts and Excel clean reopen hold retained. Next O7 only; stop for owner disposition.')


AAS_O7_BASE='8dcaf51fbcf5b29c1d66897a7fbf78aab2621aa4'
AAS_O7_STAGES=('AAS_O2_native_review','AAS_O3_native_review','AAS_O4_native_review','AAS_O5_native_review','AAS_O6_1_native_review','AAS_O6_2_native_review')

def publish_aas_o7():
    """Publish reconciliation status in the existing package without changing its data sheets."""
    m=load(MASTER);a=load(F3_PEER_FILES[-1]);o=a['AAS_O7_reconciliation']
    need(m['currentEvidenceCheckpoint']=='AAS_O7_RECONCILIATION_PENDING_SAME_XLSX','O7 prepared reconciliation')
    prior=(D/BOOK).read_bytes();need(prior==f3_baseline(BOOK,AAS_O7_BASE),'exact pre-O7 workbook')
    banner='# CURRENT — AAS O7 reconciliation complete; owner disposition pending (15 November 2026)\n\nAll 310 retained findings and 53 historically uncited records have dispositions. O2–O6-2 added 24 provisional candidates (19 common, five specialized); no O7 information rows or classifications changed. Current: 361 information rows; 640 source-bearing comparisons (532 colored / 108 held). AAS: 88 comparisons, 76 colored / 12 held; 264 unassessed and nine case-held rows remain explicit. Recommendation: accept completed review as bounded PARTIAL with documented holds. Owner acceptance, model adoption and next donor remain undecided.\n\n'
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        original=(D/name).read_text();(D/name).write_text(banner+original[original.index('<table>'):],encoding='utf-8')
    guidance={'A1':'CURRENT 15 NOV 2026 — AAS O7 complete; owner decision pending','B1':'361 information rows in the same 26-sheet master. AAS bounded PARTIAL; owner closeout pending. F3 accepted; M00/M01 frozen. Earlier checkpoints are historical.','A17':'Completed review and recommendation','B17':'O7 accounts for all 310 retained findings, including 53 historically uncited records. O2–O6-2 added 24 provisional candidates (19 common, five specialized). No O7 data/classification changes. Recommend bounded-PARTIAL acceptance.','B19':'361 information rows; 640 source comparisons: 532 colored, 108 held. AAS: 57 common, 14 specialized, two native-only, three unresolved and 12 held. Other 273 AAS rows: 264 unassessed and nine case holds.','B21':'Original evidence/contact grades reused at unchanged pins. Part1 documentation: 14 full-text, six sampled, 28 without recorded substantive review; Part2: one full-text, ten sampled, 21 without. These are source-page files, not coverage percentages.','B22':'Remaining: partial schema/API/figure/companion/template/external-source coverage, conflicting source details and 13 unlocated example packages. Review completion is not full-corpus coverage, adoption, installed equipment or execution proof.','A23':'Owner decision and stop','B23':'STOP for owner disposition: accept completed AAS review as bounded PARTIAL with retained holds, or identify a specific question to reopen. No automatic donor transition, model/Profile adoption or implementation.','A28':'O7 saved-file and preservation checks','B28':'All 6,144 grid values, 361 rows and 640 classifications unchanged. Both CSV mirrors, both data worksheets, 23 untouched worksheet parts and M00/M01 preserved. Current guidance refreshed; native Excel clean reopen remains unverified.'}
    legend={'A1':'CURRENT LEGEND — O7 complete; classification is not adoption','A23':'Current classification totals','B23':'532 colored / 108 held source comparisons overall. AAS: 57 common, 14 specialized, two native-only, three unresolved and 12 held. Historical counts remain historical.','B24':'361 information rows; 384 × 16 grid. 24 new candidates across O2–O6-2: 19 common, five specialized. No O7 rows or color changes.','A28':'Owner disposition pending','B28':'Recommend accepting completed AAS review as bounded PARTIAL with retained source limits. Acceptance does not adopt DIM/Profile fields, prove runtime behavior or authorize another donor.'}
    with zipfile.ZipFile(io.BytesIO(prior)) as z:
        paths=old.sheetpaths(z);replacements={}
        for name,changes in [('Summary',guidance),('Validation',guidance),('Legend',legend)]:
            rt=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in rt.iter(q('c'))}
            for ref,value in changes.items():need(ref in cells,'existing O7 guidance cell '+ref);f3_put(cells[ref],value)
            for rr in rt.find(q('sheetData')):
                vals=[v for k,v in changes.items() if re.search(r'\d+$',k).group()==rr.get('r')]
                if vals:rr.set('ht',str(min(409.5,max(float(rr.get('ht',15)),max(len(textwrap.wrap(v,95))*12+18 for v in vals)))));rr.set('customHeight','1')
            replacements[paths[name]]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as dst:
            for info in z.infolist():dst.writestr(info,replacements.get(info.filename,z.read(info.filename)))
    saved=buf.getvalue();(D/BOOK).write_bytes(saved);sha=digest(saved)
    m['currentEvidenceCheckpoint']='AAS_O7_SAVED_VERIFIED';m['currentWorkbookSha256']=sha;m['workbookSnapshot'].update(checkpoint=m['currentEvidenceCheckpoint'],sha256=sha,currently_matches_readable_view=True,lag='ZERO: 384x16 grid unchanged; O7 owner-decision guidance current',textCheckpoint='AAS_O7_RECONCILIATION_COMPLETE',validation_file=F3_PEER_FILES[-1]+'#/AAS_O7_reconciliation/publication')
    o['status']=m['AAS_O7_reconciliation']['status']='O7_COMPLETE__OWNER_DISPOSITION_PENDING'
    o['publication'].update(workbook_sha256=sha,previous_workbook_sha256=digest(prior),affected_original_sheets=['Summary','Validation','Legend'],guidance_changes={'Summary':guidance,'Validation':guidance,'Legend':legend},unchanged_sheet_parts=23,grid_values=6144,information_rows=361,source_classifications=640,M00_M01_preserved=True,M02_created=False,actual_Microsoft_Excel_clean_reopen='UNVERIFIED',visual_review='PENDING',remote_publication='PENDING')
    a['master_state_current'].update(checkpoint=m['currentEvidenceCheckpoint'],comparison_lag=0,workbook_metadata_lag='ZERO: O7 reconciliation complete; owner decision pending')
    save(MASTER,m);save(F3_PEER_FILES[-1],a);verify_aas_o7()


def verify_aas_o7():
    """Validate accountable reconciliation and unchanged data, without replaying source research."""
    import copy
    from collections import Counter,defaultdict
    from html.parser import HTMLParser
    m=load(MASTER);a=load(F3_PEER_FILES[-1]);base=json.loads(f3_baseline(MASTER,AAS_O7_BASE));ab=json.loads(f3_baseline(F3_PEER_FILES[-1],AAS_O7_BASE));o=a['AAS_O7_reconciliation'];acc=o['accountability'];cr=o['candidate_reconciliation']
    need(m['currentEvidenceCheckpoint']=='AAS_O7_SAVED_VERIFIED','O7 checkpoint')
    snap=m['workbookSnapshot']; current=o['publication'].get('snapshot_metadata_correction',{}).get('current',{})
    need(all(snap.get(k)==v for k,v in current.items()) and current,'current snapshot correction recorded and consistent')
    need(snap['information_rows']==snap['textInformationRows']==len(m['rows'])==m['counts']['informationRows'],'current snapshot information-row counts')
    need(snap['text_grid_rows']==snap['saved_xlsx_grid_rows']==len(m['review_grid']),'current snapshot grid dimensions')
    need(snap['source_compared_rows']==cr['AAS_source_bearing_comparisons'] and snap['explicit_unassessed_rows']==cr['all_other_rows'],'current AAS comparison counts')
    need(snap['primary_reviewed']==snap['textPrimaryReviewed']==m['ISAEvidence']['currentPrimaryReviews'],'ISA source-review count retains its meaning')
    allowed={'currentEvidenceCheckpoint','currentWorkbookSha256','workbookSnapshot','nextOwnerAction'}
    for k,v in base.items():
        if k not in allowed:need(m[k]==v,'unchanged master evidence '+k)
    restored=copy.deepcopy(a);restored.pop('AAS_O7_reconciliation')
    for k in ('status','one_next','master_state_current'):restored[k]=ab[k]
    need(restored==ab,'all original findings, holds, coverage grades and owner decisions preserved')
    native={x['source_id']:x for i in range(2,10) for x in a['AAS%02d'%i]['original_items']};byid=defaultdict(list);rowids={r['row_id'] for r in m['rows']}
    for k in AAS_O7_STAGES:
        for i,r in enumerate(a[k]['records']):
            need(r['source_id'] in native,'known native finding')
            need(r['original_record_sha256']==digest(json.dumps(native[r['source_id']],sort_keys=True,ensure_ascii=False).encode()),'retained original record hash '+r['source_id'])
            need(set(r['row_ids'])<=rowids and r['rationale'] and r['relation'] and not r['DIM_Profile_adopted'],'complete bounded disposition')
            byid[r['source_id']].append('#/'+k+'/records/'+str(i))
    need(len(native)==len(byid)==310 and set(native)==set(byid),'all 310 original findings accounted for')
    need(sum(map(len,byid.values()))==316 and sum(len(v)>1 for v in byid.values())==6,'six explicitly revisited findings, no source inflation')
    need(acc['unique_findings_dispositioned']==310 and acc['recorded_dispositions']==316 and not acc['missing_ids'] and not acc['extra_ids'],'reported accountability')
    for idx,k in enumerate(AAS_O7_STAGES):
        st=acc['stage_index'][idx];need(st['stage']==k and st['source_ids']==[r['source_id'] for r in a[k]['records']] and st['record_count']==len(a[k]['records']),'stage routing index')
    h53={r['source_id'] for r in a['AAS_O1_source_opportunities']['finding_records'] if r['historical_53']}
    need(len(h53)==53 and set(acc['historical_53'])==h53 and all(acc['historical_53'][i]==byid[i][-1] for i in h53),'all 53 historical citation gaps dispositioned')
    need({r['source_id'] for r in acc['workflow_followups_reconciled']}=={'AAS03-N029','AAS04-N003','AAS04-N004'},'three O5 routing followups reconciled')
    allptr={v for vs in byid.values() for v in vs}
    for f in acc['workflow_followups_reconciled']:need(f['prior_disposition'] in allptr and set(f['evidence_pointers'])<=allptr and f['rationale'],'followup evidence retained')
    candidates=[r for r in m['rows'] if r['row_id'] in {i for k in AAS_O7_STAGES for i in a[k]['new_candidate_row_ids']}]
    need(len(candidates)==24 and [r['row_id'] for r in candidates]==[r['row_id'] for r in cr['candidates']],'24 current candidates')
    for r,c in zip(candidates,cr['candidates']):
        key=c['master_pointer'].split('/')[-1];src=r[key]
        need(c['classification']==src['candidate_status'] and c['reason_for_separate_candidate']==src['reason_for_separate_candidate'] and c['source_ids']==src['source_ids'] and not c['DIM_Profile_adopted'],'candidate rationale/classification preserved')
    need(Counter(c['classification'] for c in cr['candidates'])=={'COMMON_CANDIDATE':19,'SPECIALIZED_CANDIDATE':5},'19 common and five specialized additions')
    need(len(m['rows'])==361 and len(m['review_grid'])==384 and all(len(r)==16 for r in m['review_grid']),'361 rows / 384x16 grid')
    counts=Counter(r['display'][6].split(']')[0][1:].replace(' ','_') for r in m['rows'] if r['display'][6].startswith('['))
    need(counts==cr['current_AAS_classifications']=={'COMMON_CANDIDATE':57,'SPECIALIZED_CANDIDATE':14,'NATIVE_ONLY_EVIDENCE':2,'UNRESOLVED_CANDIDATE':3,'HELD':12},'88 explicit AAS comparisons')
    need(sum(r['display'][6].startswith('Not assessed here') for r in m['rows'])==264 and sum(r['display'][6].startswith('CASE REVIEW HOLD') for r in m['rows'])==9,'273 explicit noncomparison states')
    need(all(r['display'][i].strip() for r in m['rows'] for i in (6,7,8,9)),'no blank completed-donor cells')
    corpus=o['corpus_reconciliation']
    for part,docs in a['AAS10']['current_document_coverage'].items():
        current=corpus['current_document_coverage'][part];need(len(current)==len(docs),'complete source-page inventory '+part)
        for d,c in zip(docs,current):
            contacts=[{'stage':k,'contact_index':i,'grade':v['grade']} for k in AAS_O7_STAGES for i,v in enumerate(a[k]['targeted_original_contacts']) if v.get('path')==d['path']]
            grade='SELECTED_TEXT_OR_STRUCTURAL_SAMPLE' if contacts and d['grade']=='NO_SUBSTANTIVE_REVIEW_RECORDED' else d['grade']
            need(c['source_id']==d['source_id'] and c['path']==d['path'] and c['additional_contacts']==contacts and c['current_grade']==grade,'source grade is not inflated')
        need(dict(Counter(c['current_grade'] for c in current))==corpus['document_grade_counts'][part],'current document totals')
    for stage,key in [('AAS08','companion_file_grades'),('AAS09','template_file_grades')]:need(dict(Counter(f['access_grade'] for f in a[stage]['source_file_coverage']))==corpus[key],'actual remaining file grades')
    hr=o['hold_reconciliation'];need(len(hr['historical_records'])==76 and [h['hold_id'] for h in hr['historical_records']]==[h['hold_id'] for h in a['AAS10']['historical_hold_reconciliation']],'all historical holds accounted for')
    need(hr['stage_hold_pointers']==['#/'+k+'/holds_retained' for k in AAS_O7_STAGES] and hr['stage_hold_group_statements']==34,'later source limits retained')
    need(o['owner_recommendation']['owner_decision']==m['AAS_O7_reconciliation']['owner_decision']=='PENDING' and not o['owner_recommendation']['model_Profile_adopted'],'owner gate and no adoption')
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        need((D/name).read_bytes()==f3_baseline(name,AAS_O7_BASE) and source_csv(name)==m['review_grid'],'unchanged CSV '+name)
    md=(D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_text();need(md==(D/'ISA_Correction_Review_07NOV2026.md').read_text(),'both readable mirrors')
    oldmd=f3_baseline('Master_Donor_Concept_to_DIM_Crosswalk.md',AAS_O7_BASE).decode();need(md[md.index('<table>'):]==oldmd[oldmd.index('<table>'):],'unchanged entire readable table')
    saved=(D/BOOK).read_bytes();prior=f3_baseline(BOOK,AAS_O7_BASE);need(digest(saved)==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==o['publication']['workbook_sha256'],'saved workbook SHA-256')
    with zipfile.ZipFile(io.BytesIO(saved)) as z,zipfile.ZipFile(io.BytesIO(prior)) as bz:
        paths=old.sheetpaths(z);need(paths==old.sheetpaths(bz) and len(paths)==26 and z.namelist()==bz.namelist() and z.testzip() is None,'same valid 26-sheet package')
        affected={paths[n] for n in ('Summary','Validation','Legend')}
        for name in z.namelist():
            if name not in affected:need(z.read(name)==bz.read(name),'unchanged data/style/package part '+name)
            if name.endswith(('.xml','.rels')):ET.fromstring(z.read(name))
        for name,changes in o['publication']['guidance_changes'].items():
            actual=old.readcells(saved,name);before=old.readcells(prior,name)
            need(actual==dict(before,**changes),'only planned guidance values changed '+name)
        cells=old.readcells(saved,'Master Crosswalk')
        for i,row in enumerate(m['review_grid'],1):
            for j,v in enumerate(row,1):need(cells.get(addr(i,j),'')==v,'saved value '+addr(i,j))
        styles=ET.fromstring(z.read('xl/styles.xml')); fills=list(styles.find(q('fills'))); xfs=list(styles.find(q('cellXfs')))
        nodes={c.get('r'):c for c in ET.fromstring(z.read(paths['Master Crosswalk'])).iter(q('c'))}
        palette={'FFD9EAF8','FFF9E6B8','FFE5E7EB','FFE9DEFA'}; colored=aas_colored=0
        for row in m['rows']:
            n=m['review_grid'].index(row['display'])+1
            for col in 'GHIJ':
                cell=nodes.get(col+str(n)); style=int(cell.get('s','0')) if cell is not None else 0
                fg=fills[int(xfs[style].get('fillId','0'))].find('.//'+q('fgColor'))
                marked=fg is not None and fg.get('rgb') in palette
                colored+=marked; aas_colored+=marked and col=='G'
        need(colored==snap['color_cell_count']==532 and aas_colored==snap['AAS_candidate_colors']==76,'current snapshot counts actual saved classification fills')
        need(colored+snap['mixed_source_cells_uncolored']==o['publication']['source_classifications']==640 and aas_colored+snap['AAS_uncolored_source_holds']==cr['AAS_source_bearing_comparisons']==88,'current held/colored comparison totals')
        # Cumulative preservation, independently of intervening stage declarations.
        with zipfile.ZipFile(io.BytesIO(f3_baseline(BOOK,'1329bafed27858a967781b1f702eb48895dc443a'))) as fz:
            fp=old.sheetpaths(fz);fr=ET.fromstring(fz.read(fp['Master Crosswalk']));nr=ET.fromstring(z.read(paths['Master Crosswalk']));nc={c.get('r'):c.get('s','0') for c in nr.iter(q('c'))}
            need(all(nc.get(c.get('r'))==c.get('s','0') for c in fr.iter(q('c'))),'all accepted F3 cell classifications/styles retained cumulatively')
    for name in ('M00_Master_Donor_Concept_to_DIM_Crosswalk_Pre_Classification_13NOV2026.xlsx','M01_Master_Donor_Concept_to_DIM_Crosswalk_Post_Source_Classification_13NOV2026.xlsx'):
        rel='Manual_Workbook_Versions/'+name;need((D/rel).read_bytes()==f3_baseline(rel,AAS_O7_BASE),'immutable '+name)
    need(not list((D/'Manual_Workbook_Versions').glob('M02*')),'no automatic M02')
    need(a['one_next']==o['one_next']==m['nextOwnerAction']==m['AAS_O7_reconciliation']['one_next'],'single owner-decision boundary')
    print('PASS O7: 310 findings / 316 recorded dispositions; all 53 historical citation gaps accounted for; 24 candidates (19 common, five specialized).')
    print('PASS: unchanged 361 rows, all 6144 saved values, classifications, CSV/readable tables, both data sheets, 23 untouched sheets and M00/M01; original source grades/holds retained.')
    print('LIMIT: bounded PARTIAL; owner disposition pending. No adoption, runtime proof or automatic donor transition.')



def sosa_opportunity_spec(packet='SO-2A'):
    """Authorized cell edits for Artifact Tool, using the existing workbook layout."""
    import math
    m=load(MASTER);o=load('SOSA_G4_F_192_Heading_Source_and_Master_Ledger_11NOV2026.json')['SO2_source_opportunity_assessments'][packet]
    base=json.loads(f3_baseline(MASTER,o['baseline_commit']));new=m['rows'][len(base['rows']):];sheets={};counts=o['counts'];key=packet.replace('-','')
    cells={x['master_cell']:x['after'] for x in o['qualified_existing_rows']}
    for change in o['qualified_existing_rows']:
        n=int(re.search(r'\d+',change['master_cell']).group())
        for column,edit in change.get('display_changes',{}).items():cells[addr(n,int(column)+1)]=edit['after']
    heights={}
    for c,v in cells.items():
        area=re.sub('[A-Z]+','A',c)+':P'+re.search(r'\d+',c).group();heights[area]=max(heights.get(area,0),min(409.5,max(300,14*math.ceil(len(v)/48)+20)))
    appended=[]
    for n,row in enumerate(m['review_grid'][len(base['review_grid']):],len(base['review_grid'])+1):
        divider=n-1 in m['review_sections'];template=base['review_sections'][-1]+1 if divider else len(base['review_grid']);appended.append({'range':f'A{n}:P{n}','template':f'A{template}:P{template}','values':row,'height':34 if divider else 330})
    sheets['Master Crosswalk']={'cells':cells,'heights':heights,'new_rows':appended,'fills':{r['SO2_source_correspondence']['cell']:r['SO2_source_correspondence']['fill'] for r in new}}
    for change in o['qualified_existing_rows']:
        if change.get('first_source_classification'):
            sheets['Master Crosswalk']['fills'][change['master_cell']]=change['first_source_classification']['fill']
    with zipfile.ZipFile(io.BytesIO(f3_baseline(BOOK,o['baseline_commit']))) as z:
        rt=ET.fromstring(z.read(old.sheetpaths(z)['DIM Register']));register={c.get('r'):f3_cell_text(c) for c in rt.iter(q('c'))}
    positions={r['row_id']:n+2 for n,r in enumerate(base['rows'])};rc={}
    for change in o['qualified_existing_rows']:
        n=positions[change['row_id']];ref='O'+str(n);rc[ref]=register.get(ref,'')+' | '+m['rows'][n-2][key+'_qualification']['rationale']
        if change.get('first_source_classification'):
            # A first comparison replaces the unassessed placeholder in every SOSA register field.
            sid=', '.join(change['first_source_classification']['source_ids'])
            rc[ref]=m['rows'][n-2][key+'_qualification']['rationale']
            rc['J'+str(n)]=sid
            rc['K'+str(n)]='PARTIAL / COMMON_CANDIDATE; '+change['first_source_classification']['rationale']
            rc['L'+str(n)]='C239 Edition 1.1; §12.2.2 PDF180–184 and Rule 12.2.6-3 PDF188. Native companions/external SYSLOG original remain unaudited.'
            rc['P'+str(n)]=sid+'; SO2_source_opportunity_assessments/'+packet+'; original pointers/hashes retained.'
        for field,edit in change.get('field_changes',{}).items():rc[{'label':'B','definition':'C'}[field]+str(n)]=edit['after']
    rr=[]
    for n,r in enumerate(new,len(base['rows'])+2):
        c=r['SO2_source_correspondence'];sid=', '.join(c['source_ids'])
        vals=[r['row_id'],r['label'],r['definition'],r['status'],r['source_review_status'],r['master_inclusion'],r['dim_adoption'],'Not assessed here','Not assessed here',sid,c['relation']+'; '+c['reason_for_separate_candidate'],'C239 Edition 1.1; retained evidence and targeted original text; native 2023 companions/figure geometry remain held.','Not assessed here','Not assessed here',c['candidate_status']+'; '+c['native_meaning'],sid+'; '+'; '.join(c['original_source_locators']),'Not assessed here','Not assessed here — no AAS correspondence established.']
        template=len(base['rows'])+1;rr.append({'range':f'A{n}:R{n}','template':f'A{template}:R{template}','values':vals,'height':330})
    sheets['DIM Register']={'cells':rc,'new_rows':rr,'heights':{f'A{positions[x["row_id"]]}:R{positions[x["row_id"]]}':330 for x in o['qualified_existing_rows']}}
    guidance={'A1':'CURRENT 15 NOV 2026 — SOSA SO-2A complete','B1':'369 information rows in the same 26-sheet master. F3 accepted; SOSA bounded PARTIAL retained; AAS acceptance pending. M00/M01 frozen.',
      'A17':'Current completed scope','B17':'SO-2A: 262 architecture/role/vocabulary records accounted for; eight candidates added and eight existing SOSA comparisons clarified. Other donor and case values unchanged.',
      'B19':'369 information rows; 648 source classifications: 540 colored and 108 held. The 17 held SO-2A source records are a separate count, not 17 added held cells.',
      'B21':'Targeted original C239 text reread; original source pointers, contact grades and prior judgments reused. Nine SOSA hold families remain. No new edition or native-companion audit.',
      'B22':'New: interface boundary; function allocation; scoped conformance; security posture; product processing; data/software rights; flow QoS; interaction binding. Six common and two specialized candidates, not adopted requirements.',
      'A23':'Next step and remaining limits','B23':o['one_next']+' Eleven further steps estimated. Secure startup remains SO-2D; AAS acceptance is separate.',
      'A28':'Saved-file checks and limits','B28':'6,288 comparison values and eight new fills checked; prior 640 classifications, 21 untouched sheets and M00/M01 preserved. Native Microsoft Excel clean reopening remains unverified.'}
    sheets['Summary']={'cells':guidance};sheets['Validation']={'cells':guidance}
    sheets['Legend']={'cells':{'A1':'CURRENT LEGEND — SOSA SO-2A; classification is not adoption','A23':'Current classification totals','B23':'540 colored / 108 held comparisons. Eight new SOSA candidates: six common (blue), two specialized (amber). All prior classification decisions retained.','B24':'369 information rows; 393 × 16 comparison grid. Earlier step counts remain historical.','A28':'Current SO-2A boundary','B28':'262 records: 67 represented, 103 supporting additions, 75 source-specific/no row, 17 held. Records are not distinct concepts or rows. Next SO-2B only; AAS acceptance pending.'}}
    if packet=='SO-2B':
        guidance.update({'A1':'CURRENT 15 NOV 2026 — SOSA SO-2B complete','B1':'378 information rows in the same 26-sheet master. F3 accepted; SOSA bounded PARTIAL retained; AAS acceptance pending. M00/M01 frozen.',
          'B17':'SO-2B: 201 System Manager/generic-module records accounted for; nine candidates added and seven existing SOSA comparisons clarified. Other donor and case values unchanged.',
          'B19':'378 information rows; 657 source classifications: 549 colored and 108 held. Four held SO-2B source records do not add held comparison cells.',
          'B22':'New: health assessment; monitoring settings; notification settings; diagnostic settings; health log; logging configuration; firmware package/target; resource reservations; equipment settings. Nine common candidates; diagnostic settings and reservations are Future-only in C239.',
          'B23':o['one_next']+' Ten further steps estimated. AAS acceptance is separate.',
          'B28':'6,448 comparison values and nine new fills checked; prior 648 classifications, 21 untouched sheets and M00/M01 preserved. Native Microsoft Excel clean reopening remains unverified.'})
        sheets['Legend']['cells'].update({'A1':'CURRENT LEGEND — SOSA SO-2B; classification is not adoption','B23':'549 colored / 108 held comparisons. Nine new common candidates (blue). Color describes provisional information scope; two have Future-only source support. All prior classifications retained.','B24':'378 information rows; 403 × 16 comparison grid. Earlier step counts remain historical.','A28':'Current SO-2B boundary','B28':'201 records: 76 represented, 117 supporting additions, four source-specific/no row, four held. Records are not distinct concepts or rows. Next SO-2C only; AAS acceptance pending.'})
    if packet=='SO-2C':
        guidance.update({'A1':'CURRENT 15 NOV 2026 — SOSA SO-2C complete','B1':'380 information rows in the same 26-sheet master. F3 accepted; SOSA bounded PARTIAL retained; AAS acceptance pending. M00/M01 frozen.',
          'B17':'SO-2C: all 352 security/chassis/PIC/runtime-management records accounted for; two candidates added and five existing SOSA comparisons clarified. Logging configuration now explicitly covers health or security logging.',
          'B19':'380 information rows; 659 source classifications: 551 colored and 108 held. Ten held SO-2C source records are a separate count and do not add held comparison cells.',
          'B21':'Original C239 PDF90–118 text read; PDF95/106/111/115 visually checked for ambiguities, duplicate labels and blank definitions. Prior decisions and source grades retained; no new edition or native-companion audit.',
          'B22':'New: hosted application identity/lifecycle/host context and security-condition history. Both are common candidates supported by V1.0 declarations, not implemented-device evidence. Security logging settings extend the existing logging candidate without a duplicate row.',
          'B23':o['one_next']+' Nine further bounded steps estimated. AAS acceptance is separate.',
          'B28':'6,496 comparison values, two new fills and the clarified logging definition checked; prior 657 classifications, 21 untouched sheets and M00/M01 preserved. Native Microsoft Excel clean reopening remains unverified.'})
        sheets['Legend']['cells'].update({'A1':'CURRENT LEGEND — SOSA SO-2C; classification is not adoption','B23':'551 colored / 108 held comparisons. Two new common candidates (blue). Five existing comparisons clarified without changing their classifications; one definition broadened.','B24':'380 information rows; 406 × 16 comparison grid. Earlier step counts remain historical.','A28':'Current SO-2C boundary','B28':'352 records: 307 represented, 26 supporting additions, four supporting clarification, five source-specific/no row, ten held. Records are not distinct concepts or rows. Next SO-2D only; AAS acceptance pending.'})
    if packet=='SO-2D':
        guidance.update({'A1':'CURRENT 15 NOV 2026 — SOSA SO-2D complete','B1':'384 information rows in the same 26-sheet master. F3 accepted; SOSA bounded PARTIAL retained; AAS acceptance pending. M00/M01 frozen.',
          'B17':'SO-2D: all 217 management-path, state and hosted-runtime records accounted for; four candidates added and seven existing SOSA comparisons clarified. Security assessment now explicitly includes inter-module connections.',
          'B19':'384 information rows; 663 source classifications: 555 colored and 108 held. Thirteen held SO-2D source records are a separate count and do not add held comparison cells.',
          'B21':'Original C239 PDF122–140 and 361–371 text read; seven decisive pages visually checked. Original source grades and prior decisions retained; no new edition, native-companion or external-standard audit.',
          'B22':'New: latched memory write protection, persistent hardware action flag, container-scoped slot identifier and secure-startup authentication dependencies. One common and three specialized candidates; no adopted requirements or observed device behavior.',
          'B23':o['one_next']+' Eight further bounded steps estimated. AAS acceptance is separate.',
          'B28':'6,576 comparison values, four new fills and the clarified security-state definition checked; prior 659 classifications, 21 untouched sheets and M00/M01 preserved. Native Microsoft Excel clean reopening remains unverified.'})
        sheets['Legend']['cells'].update({'A1':'CURRENT LEGEND — SOSA SO-2D; classification is not adoption','B23':'555 colored / 108 held comparisons. One common slot-identity candidate (blue); three specialized latch/startup candidates (amber). Seven prior comparisons clarified without classification changes.','B24':'384 information rows; 411 × 16 comparison grid. Earlier step counts remain historical.','A28':'Current SO-2D boundary','B28':'217 records: 138 represented, 22 supporting additions, four supporting clarification, 40 source-specific/no row, 13 held. Records are not distinct concepts or rows. Next SO-2E only; AAS acceptance pending.'})
    if packet=='SO-2E':
        guidance.update({'A1':'CURRENT 15 NOV 2026 — SOSA SO-2E complete','B1':'393 information rows in the same 26-sheet master. F3 accepted; SOSA bounded PARTIAL retained; AAS acceptance pending. M00/M01 frozen.',
          'B17':'SO-2E: all 496 task/RF/host/transport/service records accounted for; nine candidates added and ten existing SOSA comparisons qualified, including the first SOSA classification on the existing audit-record row.',
          'B19':'393 information rows; 673 source classifications: 565 colored and 108 held. Twenty-two held source records are a separate count, not additional held comparison cells.',
          'B21':'Original C239 PDF141–207 and 372–383 text read; eight decisive table/text pages visually inspected. Original source grades and prior decisions retained; no new edition, external-standard, full figure or native-companion audit.',
          'B22':'New: identified tasks; module assignments/resources; key inventory; cryptographic associations; calibration state/result; quantitative spatial resolution; frequency-band power ceiling/release; stream context; virtual discrete state. Five common/four specialized candidates; no adopted requirements.',
          'B23':o['one_next']+' Seven further bounded steps estimated. AAS acceptance remains separate.',
          'B28':'6,736 comparison values, nine new candidate fills and one first audit comparison fill checked. All 663 prior classifications, 21 unaffected sheets and M00/M01 preserved. Native Microsoft Excel clean reopening remains unverified.'})
        sheets['Legend']['cells'].update({'A1':'CURRENT LEGEND — SOSA SO-2E; classification is not adoption','B23':'565 colored / 108 held comparisons. Nine new rows: five common (blue), four specialized (amber). Existing audit row receives its first SOSA common classification; all 663 prior classifications retained.','B24':'393 information rows; 421 × 16 comparison grid. Earlier step counts remain historical.','A28':'Current SO-2E boundary','B28':'496 records: 289 represented, 60 supporting additions, 47 supporting clarifications, 78 source-specific/no row, 22 held. Ten existing comparisons qualified; no record-to-row count equivalence. Next SO-2F only; AAS acceptance pending.'})
    for name in ('Summary','Validation','Legend'):
        sheets[name]['heights']={f'A{re.search(r"\d+",ref).group()}:B{re.search(r"\d+",ref).group()}':max(60,14*math.ceil(len(value)/95)+22) for ref,value in sheets[name]['cells'].items() if ref.startswith('B')}
    return {'packet':packet,'baseline_commit':o['baseline_commit'],'sheets':sheets}


def publish_sosa_opportunity(authored_path, packet='SO-2A'):
    """Transfer Artifact-authored values into the original package, preserving other bytes/styles."""
    import copy,html
    m=load(MASTER);ln='SOSA_G4_F_192_Heading_Source_and_Master_Ledger_11NOV2026.json';l=load(ln);o=l['SO2_source_opportunity_assessments'][packet]
    base=json.loads(f3_baseline(MASTER,o['baseline_commit']));prior=f3_baseline(BOOK,o['baseline_commit'])
    need((D/BOOK).read_bytes()==prior,'opportunity publisher archived input')
    spec=sosa_opportunity_spec(packet);edits={};replacements={}
    with zipfile.ZipFile(authored_path) as au,zipfile.ZipFile(io.BytesIO(prior)) as oldz:
        ap=old.sheetpaths(au);op=old.sheetpaths(oldz);ss=[]
        if 'xl/sharedStrings.xml' in au.namelist():ss=[''.join(t.text or '' for t in si.iter(q('t'))) for si in ET.fromstring(au.read('xl/sharedStrings.xml'))]
        def value(c):return ss[int(c.findtext(q('v')))] if c is not None and c.get('t')=='s' else f3_cell_text(c)
        for name,data in spec['sheets'].items():
            ac={c.get('r'):c for c in ET.fromstring(au.read(ap[name])).iter(q('c'))}
            rt=ET.fromstring(oldz.read(op[name]));sd=rt.find(q('sheetData'));rows={int(r.get('r')):r for r in sd};cells={c.get('r'):c for c in rt.iter(q('c'))};expected=dict(data.get('cells',{}))
            for entry in data.get('new_rows',[]):
                n=int(re.search(r'\d+',entry['range']).group());tn=int(re.search(r'\d+',entry['template']).group());rr=copy.deepcopy(rows[tn]);rr.set('r',str(n))
                for c in rr:
                    col=re.match('[A-Z]+',c.get('r')).group();c.set('r',col+str(n));cells[c.get('r')]=c
                    if name=='Master Crosswalk' and n-1 not in m['review_sections'] and col in ('G','H','I','J'):c.set('s','526' if n%2==0 else '527')
                rr.set('ht',str(entry['height']));rr.set('customHeight','1');sd.append(rr);rows[n]=rr
                for j,v in enumerate(entry['values'],1):expected[addr(n,j)]=str(v)
            for ref,planned in expected.items():
                actual=value(ac.get(ref));need(actual==str(planned),f'Artifact-authored {name}!{ref}')
                if ref not in cells:
                    n=int(re.search(r'\d+',ref).group());cells[ref]=ET.SubElement(rows[n],q('c'),{'r':ref,'s':'526'})
                f3_put(cells[ref],actual)
            for area,h in data.get('heights',{}).items():
                n=int(re.search(r'\d+',area).group());rows[n].set('ht',str(max(float(rows[n].get('ht','15')),h)));rows[n].set('customHeight','1')
            for ref,fill in data.get('fills',{}).items():cells[ref].set('s','528' if fill=='#D9EAF8' else '529')
            if name in ('Master Crosswalk','DIM Register'):
                end=f'P{len(m["review_grid"])}' if name=='Master Crosswalk' else f'R{len(m["rows"])+1}';dim=rt.find(q('dimension'))
                if dim is None:dim=ET.Element(q('dimension'));rt.insert(1 if rt.find(q('sheetPr')) is not None else 0,dim)
                dim.set('ref','A1:'+end);af=rt.find(q('autoFilter'))
                if af is not None:af.set('ref',('A2:' if name=='Master Crosswalk' else 'A1:')+end)
            if name=='Master Crosswalk':
                merges=rt.find(q('mergeCells'));seen={x.get('ref') for x in merges}
                for index in m['review_sections']:
                    ref=f'A{index+1}:P{index+1}'
                    if index>=len(base['review_grid']) and ref not in seen:ET.SubElement(merges,q('mergeCell'),{'ref':ref})
                merges.set('count',str(len(merges)))
            edits[name]=expected;replacements[op[name]]=ET.tostring(rt,encoding='utf-8',xml_declaration=True)
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as dst:
            for info in oldz.infolist():dst.writestr(info,replacements.get(info.filename,oldz.read(info.filename)))
    saved=buf.getvalue();(D/BOOK).write_bytes(saved);sha=digest(saved);grid=m['review_grid']
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/name).open('w',newline='',encoding='utf-8') as f:csv.writer(f,lineterminator='\n').writerows(grid)
    table=['<table><thead><tr>']+[f'<th colspan="{span}">{html.escape(grid[0][i])}</th>' for i,span in ((0,4),(4,6),(10,5),(15,1))]
    table+=['</tr><tr>'+''.join('<th>'+html.escape(v)+'</th>' for v in grid[1])+'</tr></thead><tbody>']
    for i,row in enumerate(grid[2:],2):table.append('<tr><th colspan="16">'+html.escape(row[0])+'</th></tr>' if i in m['review_sections'] else '<tr>'+''.join('<td>'+html.escape(v)+'</td>' for v in row)+'</tr>')
    table+=['</tbody></table>'];counts=o['counts'];key=packet.replace('-','');banner=f'# Current comparison — SOSA {packet}, 15 November 2026\n\n{len(m["rows"])} information rows; {counts["new_rows"]} new source-qualified candidates and {counts["qualified_existing_rows"]} clarified SOSA comparisons. All prior classifications, other donor/case values and M00/M01 preserved. Detailed outcomes: G4 ledger `SO2_source_opportunity_assessments/{packet}`. Candidates are not adopted DIM/Profile requirements. {o["one_next"]} AAS acceptance remains pending.\n\n'
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):(D/name).write_text(banner+'\n'.join(table)+'\n')
    o['workbook_edits']=edits;o['status']='SAVED_VERIFIED__REMOTE_PUBLICATION_PENDING'
    o['publication'].update(workbook_sha256=sha,affected_original_sheets=list(spec['sheets']),unchanged_sheet_parts=21,grid_values=len(grid)*16,authoring='Artifact Tool import/edit/recalculate/export; authored values transferred into original OOXML package preserving unrelated bytes/styles.',visual_review='PENDING')
    m['currentEvidenceCheckpoint']='SOSA_'+key+'_SAVED_VERIFIED';m['currentWorkbookSha256']=sha
    m['workbookSnapshot'].update(checkpoint=m['currentEvidenceCheckpoint'],sha256=sha,information_rows=len(m['rows']),textInformationRows=len(m['rows']),text_grid_rows=len(grid),saved_xlsx_grid_rows=len(grid),color_cell_count=counts['colored'],mixed_source_cells_uncolored=counts['held'],explicit_unassessed_rows=len(m['rows'])-88,lag=f'ZERO: {len(grid)}x16 saved values and current {packet} guidance',textCheckpoint='SOSA_'+key+'_OPPORTUNITIES',validation_file=ln+'#/SO2_source_opportunity_assessments/'+packet+'/publication',gate_metadata_note=packet+' integrated; '+o['one_next']+' AAS acceptance pending separately. Historical counters retain recorded scopes.')
    m['SOSA_'+key+'_opportunity_review']['status']=o['status'];save(MASTER,m)
    prior_ledger=(D/ln).read_text();marker='  "SO2_source_opportunity_assessments": ';updated=prior_ledger[:prior_ledger.index(marker)]+marker+json.dumps(l['SO2_source_opportunity_assessments'],ensure_ascii=False,indent=2).replace('\n','\n  ')+'\n}\n';need(json.loads(updated)==l,'opportunity ledger formatting preservation');(D/ln).write_text(updated)
    print('SOSA opportunity workbook published locally: '+sha)


if __name__=="__main__":
    checkpoint=load(MASTER).get("currentEvidenceCheckpoint","")
    approval=load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json").get("AAS02",{}).get("owner_layout_decision",{}).get("status")
    if checkpoint in ("SOSA_SO2A_SAVED_VERIFIED","SOSA_SO2B_SAVED_VERIFIED","SOSA_SO2C_SAVED_VERIFIED","SOSA_SO2D_SAVED_VERIFIED","SOSA_SO2E_SAVED_VERIFIED"):
        from check_dim_crosswalk_step06 import verify_sosa_opportunities
        packet='SO-'+checkpoint.split('_')[1][2:]
        verify_sosa_opportunities(load(MASTER),packet)
        print(packet+" saved workbook verified without mutation; remote publication is recorded separately")
    elif checkpoint=="AAS_O7_RECONCILIATION_PENDING_SAME_XLSX":
        publish_aas_o7()
    elif checkpoint=="AAS_O7_SAVED_VERIFIED":
        verify_aas_o7()
    elif checkpoint=="AAS_O6_2_SOURCE_DECISIONS_PENDING_SAME_XLSX":
        publish_aas_o6_2()
    elif checkpoint=="AAS_O6_2_SAVED_VERIFIED":
        verify_aas_o6_2()
    elif checkpoint=="AAS_O6_1_SOURCE_DECISIONS_PENDING_SAME_XLSX":
        publish_aas_o6_1()
    elif checkpoint=="AAS_O6_1_SAVED_VERIFIED":
        verify_aas_o6_1()
    elif checkpoint=="AAS_O5_SOURCE_DECISIONS_PENDING_SAME_XLSX":
        publish_aas_o5()
    elif checkpoint=="AAS_O5_SAVED_VERIFIED":
        verify_aas_o5()
    elif checkpoint=="AAS_O4_SOURCE_DECISIONS_PENDING_SAME_XLSX":
        publish_aas_o4()
    elif checkpoint=="AAS_O4_SAVED_VERIFIED":
        verify_aas_o4()
    elif checkpoint=="AAS_O3_SOURCE_DECISIONS_PENDING_SAME_XLSX":
        publish_aas_o3()
    elif checkpoint=="AAS_O3_SAVED_VERIFIED":
        verify_aas_o3()
    elif checkpoint=="AAS_O2_SOURCE_DECISIONS_PENDING_SAME_XLSX":
        publish_aas_o2()
    elif checkpoint=="AAS_O2_SAVED_VERIFIED":
        verify_aas_o2()
    elif checkpoint=="F3_06_SOURCE_CLASSIFIED_PENDING_SAME_XLSX":
        publish_f3_06()
    elif checkpoint=="F3_06_CLASSIFICATION_SAVED_VERIFIED":
        verify_f3_06()
    elif checkpoint=="F3_05_SOURCE_CLASSIFIED_PENDING_SAME_XLSX":
        publish_f3("F3_05")
    elif checkpoint=="F3_05_CLASSIFICATION_SAVED_VERIFIED":
        verify_f3("F3_05")
    elif checkpoint=="F3_04D_SOURCE_CLASSIFIED_PENDING_SAME_XLSX":
        publish_f3("F3_04D")
    elif checkpoint=="F3_04D_CLASSIFICATION_SAVED_VERIFIED":
        verify_f3("F3_04D")
    elif checkpoint=="F3_04C_SOURCE_CLASSIFIED_PENDING_SAME_XLSX":
        publish_f3("F3_04C")
    elif checkpoint=="F3_04C_CLASSIFICATION_SAVED_VERIFIED":
        verify_f3("F3_04C")
    elif checkpoint=="F3_04B_SOURCE_CLASSIFIED_PENDING_SAME_XLSX":
        publish_f3("F3_04B")
    elif checkpoint=="F3_04B_CLASSIFICATION_SAVED_VERIFIED":
        verify_f3("F3_04B")
    elif checkpoint=="F3_04A_SOURCE_CLASSIFIED_PENDING_SAME_XLSX":
        publish_f3("F3_04A")
    elif checkpoint=="F3_04A_CLASSIFICATION_SAVED_VERIFIED":
        verify_f3("F3_04A")
    elif checkpoint=="F3_03_SOURCE_CLASSIFIED_PENDING_SAME_XLSX":
        publish_f3("F3_03")
    elif checkpoint=="F3_03_CLASSIFICATION_SAVED_VERIFIED":
        verify_f3("F3_03")
    elif checkpoint=="F3_02_SOURCE_CLASSIFIED_PENDING_SAME_XLSX":
        publish_f3_02()
    elif checkpoint=="F3_02_CLASSIFICATION_SAVED_VERIFIED":
        verify_f3_02()
    elif checkpoint=="AAS10_OWNER_VIEW_CORRECTION_SAVED_PARITY":
        publish_donor_visible_order_repair()
    elif checkpoint=="AAS10B_OFFICE_ORDER_AND_FOUR_DONOR_STATUSES_SAVED_VERIFIED":
        verify_donor_visible_order_repair()
    elif checkpoint=="AAS09_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED" and load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json").get("AAS10",{}).get("status")=="CORRECTION_REQUIRED__OWNER_CLOSEOUT_ON_HOLD":
        publish_aas_owner_view_correction()
    elif checkpoint=="AAS10_OWNER_VIEW_CORRECTION_SAVED_PARITY":
        verify_aas_owner_view_correction()
    elif checkpoint=="AAS08_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED" and load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json").get("AAS09",{}).get("status")=="PINNED_TEMPLATE_SOURCE_REVIEW_COMPLETE__SAVED_PUBLICATION_PENDING":
        publish_aas09()
    elif checkpoint=="AAS07_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED" and load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json").get("AAS08",{}).get("status")=="PINNED_COMPANION_SOURCE_REVIEW_COMPLETE__SAVED_PUBLICATION_PENDING":
        publish_aas08()
    elif checkpoint=="AAS06_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED" and load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json").get("AAS07",{}).get("status")=="PINNED_PART2_SELECTED_SOURCE_REVIEW_COMPLETE__SAVED_PUBLICATION_PENDING":
        publish_aas07()
    elif checkpoint=="AAS05_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED" and load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json").get("AAS06",{}).get("status")=="SOURCE_FIRST_PART2_SELECTED_INTERFACES_COMPLETE__SAVED_PUBLICATION_PENDING":
        publish_aas06()
    elif checkpoint=="AAS04_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED" and load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json").get("AAS05",{}).get("status")=="SCHEMA_SOURCE_READ__PUBLISHER_PENDING":
        publish_aas05()
    elif checkpoint in ("AAS03_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED", "AAS04_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED", "AAS05_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED", "AAS06_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED", "AAS07_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED", "AAS08_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED", "AAS09_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED"):
        verify_aas_saved(checkpoint.split("_")[0])
    elif checkpoint=="AAS02_G_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED":
        print("AAS02 G already published; no workbook mutation")
    elif approval=="EXPLICIT_OWNER_APPROVAL_OF_AAS32_COLUMN_POSITION_ONLY__NOT_YET_EXECUTED":
        publish_aas02_g()
    elif checkpoint=="F2_5_CLASSIFICATION_RECONCILED_PENDING_SAME_XLSX_SAVED_VERIFICATION":
        publish_f2_5()
    elif checkpoint=="C4_ISA_SOSA_SOURCE_FAITHFUL_TEXT_PENDING_SAME_EXCEL_PUBLICATION":
        publish_c4_readability()
    elif checkpoint=="C2_SOSA_SOURCE_FAITHFUL_PRESENTATION_20261112_PENDING_EXCEL_PUBLISHER":
        publish_c2_readability()
    else:
        publish_g3_n2()
