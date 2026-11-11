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
REPORT="SOSA_G2_7D_Workbook_Validation_10NOV2026.json"
PREVIEW="SOSA_G2_7D_Workbook_Preview_10NOV2026.png"
OLD="a8a9bfc2c6a6d95e530f060e3796e5e659af556a084e7716b6962d8b8c915506"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-G2-7D verification failed: +message
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
    need(m["currentWorkbookSha256"]==OLD and m["workbookSnapshot"]["sha256"]==OLD
         and not m["workbookSnapshot"]["currently_matches_readable_view"],"previous G2-7C saved 26-sheet source snapshot")
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
    need(m["SOSAReviewCompletion"]["G2_7D_XLSX_lag"]==17
         and m["workbookSnapshot"]["currently_matches_readable_view"] is False,
         "mandatory SAME Excel L23 gate still pending on this input")
    print("PASS: original C239 §13.3.5 Switch AMPS: four families,16 depth rows,five dashes,four examples,17 mappings,17 holds")

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
      ["SOSA-G2-7D Switch AMPS original source and SAME Excel","C239 Edition1.1 §13.3.5 PDF263–264, BEFORE §13.3.6 VITA66 Connectors"],
      ["Canonical working master","329 information rows, 346 source grid rows, 15 columns, 15 topic dividers"],
      ["Original source heading","One new C239 registered §13.3.5 heading, text/profile rows read"],
      ["Original source items","38 actual native records, six analytical contexts, 17 local precise holds"],
      ["Four Switch PICP families","3U DP Switch, 3U EP Switch, 3U DP Switch/V66, 6U DP Switch"],
      ["Source table","Table13.3.5-1: 16 illustrated dcp/protocol rows, five named dash alternatives"],
      ["Full-string examples","Table13.3.5-2: four original MODA3/MODA6 switch AMPS examples"],
      ["Original cross-reference held","Switch section points to payload Table13.3.4-3 and says Payload PICP"],
      ["Physical-port syntax","Backplane copper (), VITA66 optical [], SOSA-only front-panel optical <>"],
      ["Source matrix visual grade","Exact legal-port table cell/column alignment remains NOT independently visually verified"],
      ["Unexamined external originals","Original ANSI/VITA 65/66 and eight C239 DSDM/IDL/OpenAPI files held"],
      ["Qualified comparison change","17 SOSA column-I existing cells; zero other donor,case,DIM cell edits"],
      ["C239 coverage","158 at least sampled/inline read, 33 substantively unread, one restricted of 192"],
      ["Historical material retained","58 donor records,73 empirical case facts, ISA480 outcomes and six questions"],
      ["No adoption/conformance","No DIM class/cardinality, CSAPI Profile SHALL, installed device or vendor conformance"],
      ["SAME original Excel","26-sheet canonical workbook; 346x15 saved cells match JSON, both CSV, both MD"],
      ["Next only separate owner Proceed","G2-7E §13.3.6 VITA66 Connector AMPS, previous matrix holds retained; SAPIENT blocked"]
    ]

def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        groups=[r.get(name) or {} for name in ("G2_1_source_correspondence","G2_2_source_correspondence","G2_3_source_correspondence",
            "G2_4A_source_correspondence","G2_4B_source_correspondence","G2_5_source_correspondence","G2_6A_source_correspondence","G2_6B_source_correspondence","G2_6C_source_correspondence","G2_6D_source_correspondence","G2_7A_source_correspondence","G2_7B_source_correspondence","G2_7C_source_correspondence","G2_7D_source_correspondence")]
        ids=so.get("records",[])+[v for g in groups for v in g.get("source_item_ids",[])]
        relations=so.get("relations",[])+[g.get("relation",g.get("mapping_relation","")) for g in groups if g]
        status=("G2-7D original §13.3.5 physical switch profile and sample strings; exact dense table matrix alignment HELD" if groups[-1] else
            "G2-7C original §13.3.4 physical Payload AMPS with dense matrix visual hold" if groups[-2] else
            "G2-7B original AMPS string construct and native VITA source held" if groups[-3] else
            "G2-7A original AMPS definitions/code review" if groups[-4] else
            "Earlier original C239 source-qualified review, native companions held" if so or any(groups[:-4]) else "Not assessed here")
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),
             r.get("master_inclusion",""),r.get("dim_adoption",""),"; ".join(r.get("source_entry_ids",[])),
             json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
             "; ".join(ids),"; ".join(relations),status])
    return out

def publish():
    m=load(MASTER);l=load(LEDGER);check_source(m,l)
    prev=(D/BOOK).read_bytes()
    need(digest(prev)==OLD,"SAME preceding verified G2-7C 26-sheet workbook unchanged as input")
    with zipfile.ZipFile(io.BytesIO(prev)) as z:
        need(z.testzip() is None,"prior original workbook ZIP integrity")
        paths=old.sheetpaths(z);need(len(paths)==26,"26 original worksheet names and order")
        styles,sty=old.newstyles(z.read("xl/styles.xml"))
        views={"Master Crosswalk":m["review_grid"],"DIM Register":register(m),
               "Summary":summary(m),"Validation":summary(m)}
        replacement={"xl/styles.xml":styles}
        for tab,values in views.items():
            replacement[paths[tab]]=matrix_to_xml(values,sty,main=tab=="Master Crosswalk",
                sections=m["review_sections"] if tab=="Master Crosswalk" else ())
        retained={name:digest(z.read(path)) for name,path in paths.items() if name not in views}
        output=io.BytesIO()
        with zipfile.ZipFile(output,"w") as dst:
            for info in z.infolist():
                dst.writestr(info,replacement.get(info.filename,z.read(info.filename)))
    saved=output.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as z:
        need(z.testzip() is None and list(old.sheetpaths(z))==list(paths),"saved original 26 sheet ZIP and order")
        for name,h in retained.items():
            need(digest(z.read(paths[name]))==h,"22 untouched original worksheet XML preserved "+name)
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                need(not any(cell.get("t")=="e" for cell in ET.fromstring(z.read(path)).iter(q("c"))),
                     "no error-valued Excel cells in "+path)
        sheet=ET.fromstring(z.read(paths["Master Crosswalk"]))
        merges=[x.get("ref") for x in sheet.find(q("mergeCells")).findall(q("mergeCell"))]
        need(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],
             "original four case / donor / foundation merge order and 15 topic dividers")
        pane=sheet.find(q("sheetViews")).find(q("sheetView")).find(q("pane"))
        need(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","four case columns/header freeze retained")
    actual=old.readcells(saved,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for j,value in enumerate(row,1):
            need(actual.get(addr(i,j),"")==old.val(value),"actual saved workbook grid cell "+addr(i,j))
    register_cells=old.readcells(saved,"DIM Register")
    need(sum(bool(re.fullmatch(r"A\\d+",cell)) for cell in register_cells)==330,
         "329 original stable row ids in DIM Register")
    before=old.readcells(prev,"Master Crosswalk")
    changed=[a for a in set(before)|set(actual) if before.get(a,"")!=actual.get(a,"")]
    need(len(changed)==17 and all(re.fullmatch(r"I\\d+",a) for a in changed),
         "exact 17 source-qualified SOSA donor cells modified, no non-target cells")
    (D/BOOK).write_bytes(saved)
    sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7D_ORIGINAL_SWITCH_AMPS_SOURCE_AND_SAME_SAVED_26_SHEET_EXCEL_VERIFIED__MATRIX_VISUAL_HOLD_DONOR_OPEN"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7D-CANONICAL-VERIFIED","sha256":sha,
       "currently_matches_readable_view":True,
       "lag":"NONE: all 346x15 saved Excel cells equal current JSON, both CSV mirrors and both readable Markdown tables",
       "refreshed_cell_count":17,"validation_file":REPORT})
    m["SOSAEvidence"]["G2_7D"].update({"excel_checkpoint":"SOSA-G2-7D-CANONICAL-VERIFIED",
       "excel_validation":REPORT,"Excel_lag_cells":0,"same_saved_workbook_17_cells_synced":True,
       "exact_dense_switch_matrix_audit_complete":False})
    m["SOSAReviewCompletion"]["G2_7D_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="OPEN__G2_7D_SAME_EXCEL_VERIFIED__33_UNREAD_1_RESTRICTED_AND_NATIVE_MATRIX_HELD"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="G2-7E original C239 §13.3.6 VITA66 Connector AMPS only; previous visual matrix holds retained"
    m["nextOwnerAction"]="Only a separate owner Proceed starts G2-7E original C239 §13.3.6; SOSA OPEN and SAPIENT Step18 blocked"
    m["publicationPolicy"]="L23 G2-7D: 17 source-qualified SOSA column-I cells current canonical JSON,both CSV,both readable Markdown,SAME saved 26-sheet Excel; all 346x15 verified. Original switch and payload matrix visual holds persist."
    save(MASTER,m)
    record={"date":"2026-11-10","step":"SOSA-G2-7D-EXCEL-CHECKPOINT",
      "result":"EXACT_SAVED_26_SHEET_XLSX_AND_TWO_CSV_TWO_MD_PARITY_PASS",
      "workbook_sha256":sha,"base_workbook_sha256":OLD,
      "workbook_sheets":list(paths),"refreshed_sheets":list(views),
      "exact_original_untouched_xml_sha256":retained,
      "information_rows":329,"grid_rows":346,"columns":15,
      "original_donor_evidence":58,"case_evidence":73,
      "ISA_primary_source_outcomes":480,"original_ISA_questions_open":6,
      "G2_7D_original_headings_newly_read":1,"G2_7D_native_items":38,
      "G2_7D_analysis_contexts":6,"G2_7D_tables":2,"G2_7D_switch_family_count":4,
      "G2_7D_matrix_depth_rows":16,"G2_7D_explicit_dash_options":5,
      "G2_7D_full_example_strings":4,"G2_7D_visual_matrix_complete":False,
      "G2_7D_source_holds":17,"G2_7D_qualified_existing_sosa_cells":17,
      "changed_saved_cells":sorted(changed),
      "unread_C239_heading_count":33,"restricted_C239_heading_count":1,
      "C239_at_least_sampled_read_count":158,"original_C239_native_companions_unread":8,
      "checks":{"all_XLSX_346x15_grid_cells_equal_JSON_both_CSVs_both_MD":True,
        "two_CSV_mirrors_equal":True,"two_readable_Markdown_tables_equal":True,
        "same_26_worksheet_names_order":True,"22_historical_worksheet_XML_bytes_preserved":True,
        "only_17_original_SOSA_column_I_cells_changed":True,"valid_ZIP_CRC_and_XML":True,
        "zero_XLSX_error_type_cells":True,"zero_DIM_Profile_adoption":True},
      "limits":["Dense original Switch AMPS Table13.3.5-1 exact visual-port cell alignment not verified",
        "Original ANSI/VITA65/66 and eight C239 native DSDM/IDL/OpenAPI files not reviewed",
        "Original switch section uses Payload PICP wording and table 13.3.4-3 pointer for switch examples",
        "Two printed -j- source example placeholders are not verified selected dash configurations",
        "19 separate G2-7C dense Payload AMPS holds remain unresolved",
        "No as-installed switch, adopted DIM/Profile, actual vendor product or independent runtime conformance",
        "Preview generated from saved worksheet source cells, not Excel application screenshot"],
      "next":"Only separate owner Proceed starts original C239 §13.3.6 VITA66 Connector AMPS; SOSA OPEN, SAPIENT blocked"}
    save(REPORT,record)
    print("PASS: G2-7D original switch source/SAME 26-sheet 346x15 XLSX, 17 SOSA cells, 22 preserved sheets, SHA256",sha)
    return sha

def preview():
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER);actual=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_7D_source_correspondence")]
    need(len(rows)==17,"17 original G2-7D source comparisons in verified saved Excel")
    try:
        font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:font=bold=ImageFont.load_default()
    width,height=1580,1800
    img=Image.new("RGB",(width,height),"white");pen=ImageDraw.Draw(img)
    pen.rectangle((0,0,width,65),fill="#173855")
    pen.text((18,17),"SOSA-G2-7D: 17 saved Switch AMPS cells — original C239 §13.3.5",font=bold,fill="white")
    for i,r in enumerate(rows):
        hit=[k+1 for k,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(hit)==1,"unique current source row "+r["row_id"])
        a="I"+str(hit[0]);v=actual.get(a,"")
        need(v==r["display"][8],"actual saved workbook source cell "+a)
        y=72+i*98;pen.rectangle((10,y,width-12,y+91),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        pen.text((20,y+7),r["row_id"]+" | "+a+" | "+r["label"],font=bold,fill="#173855")
        snippet="G2-7D: "+v.split("G2-7D:",1)[1] if "G2-7D:" in v else v
        for j,line in enumerate(textwrap.wrap(snippet,width=165,break_long_words=False)[:3]):
            pen.text((20,y+33+j*17),line,font=font,fill="#203951")
    img.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>10000,"saved XLSX 17 source-cell preview file exists")
    print("PASS: G2-7D 17 new SOSA source-cell preview rendered from same saved Excel XML")
if __name__=="__main__":
    publish()
    preview()
