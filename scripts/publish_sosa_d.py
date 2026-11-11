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
REPORT="SOSA_G2_7I_Workbook_Validation_11NOV2026.json"
PREVIEW="SOSA_G2_7I_Workbook_Preview_11NOV2026.png"
OLD="890a1a672a0e79d4889a08c40a9f05e0a033cc1b229c525c5cb5066dff187be9"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-G2-7I verification failed: "+message
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
    need(obs["printed_method"]=="I" and obs["not_rule"] is None if False else obs["printed_method"]=="I",
         "Observation with (I) remains Observation")
    need(len(z["toc"])==3 and len(z["subclauses_read"])==4
         and (z["toc_coverage"]["total"],z["toc_coverage"]["at_least_sampled_or_inline"],
              z["toc_coverage"]["unread"],z["toc_coverage"]["restricted"])==(192,173,18,1)
         and z["toc_coverage"]["full_13_5_review"] is False,
         "3 newly sampled/inline C239 headings and 18 original unread remain")
    need(z["source"]["figures_pixel_verified"] is False
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
    need(m["SOSAReviewCompletion"]["G2_7I_XLSX_lag"]==25
         and m["workbookSnapshot"]["currently_matches_readable_view"] is False,
         "25 new source-qualified cells before SAME-Excel L23 exit")
    print("PASS: original G2-7I C239 Rule inventory and 25 semantic mappings, figure/native companion holds retained")

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
      ["SOSA-G2-7I source and SAME Excel checkpoint","C239 Ed1.1 §§13.5–13.5.2.2.2, PDF273–278; STOP BEFORE §13.5.2.3"],
      ["Approved original master","329 information rows, 346 grid rows, 15 columns, 15 topic dividers"],
      ["Source-read scope","Electrical Classes, Class1&2 connectors and J1 DC power/safety ground"],
      ["Source native inventory","82 items, 23 numbered SHALL Rules, 4 Permissions, 3 Observations"],
      ["Source rule methods","18 printed (I) Inspection, five printed (A) Analysis"],
      ["Source table rows","16 J1–J16 physical connectors and eleven J1 power/ground pins"],
      ["Electrical class scope","Class1&2, Class3 and Class5; SAE turret qualification narrower"],
      ["Connector alternative","Class1&2 requires J2 OR J14 OR J15, not all three"],
      ["J1 cardinality","At most one J1 per external sensing element; J6 dependent on J1"],
      ["Power and safety design limits","+28VDC; ≤25A/2s inrush, ≤15A nominal each, up to five paired rails, chassis isolation ≥1MΩ, ground ≤0.1Ω"],
      ["Source method/type caution","Observation13.5.2.2.1-2 includes (I) but remains Observation; Permission13.5.2-4 printed atypically"],
      ["Original source holds","20 new, including unread SAE/MIL/VITA, graphic contact geometry, J2 onward, eight C239 native files and later S251"],
      ["Source-qualified master comparisons","25 existing donor column-I cells only, zero case/ISA/W3C/OGC/DIM cell changes"],
      ["C239 registered heading standing","173 at least sampled/inline-read,18 unread,one restricted; two parent headings PARTIAL"],
      ["Source-case and previous donor evidence","58 donor facts,73 source-case facts,ISA480 source outcomes/six unresolved questions retained"],
      ["Adoption and conformance","ZERO DIM class/chassis/cardinality,Profile SHALL or independent physical test"],
      ["SAME original Excel","ALL 346x15 actual saved cells equal canonical JSON/BOTH CSV/BOTH Markdown"],
      ["Next new owner Proceed only","G2-7J original §13.5.2.3 J2 Signal Connector; SOSA open, SAPIENT blocked"]
    ]

def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        groups=[r.get(name) or {} for name in ("G2_1_source_correspondence","G2_2_source_correspondence","G2_3_source_correspondence",
            "G2_4A_source_correspondence","G2_4B_source_correspondence","G2_5_source_correspondence","G2_6A_source_correspondence","G2_6B_source_correspondence","G2_6C_source_correspondence","G2_6D_source_correspondence","G2_7A_source_correspondence","G2_7B_source_correspondence","G2_7C_source_correspondence","G2_7D_source_correspondence","G2_7E_source_correspondence","G2_7F_source_correspondence","G2_7G_source_correspondence","G2_7H_source_correspondence","G2_7I_source_correspondence")]
        ids=so.get("records",[])+[v for g in groups for v in g.get("source_item_ids",[])]
        relations=so.get("relations",[])+[g.get("relation",g.get("mapping_relation","")) for g in groups if g]
        status=("G2-7I §13.5 original Class1&2/J1 electrical Rules and table text, figures/SAE/MIL/VITA held" if groups[-1] else
            "G2-7H §13.4 original VNX textual/table review, numbered Rules absent and future/TBD + figure/native holds" if groups[-2] else
            "G2-7G §13.3.8 original analog/coax Rule/Rec/Obs and figure text read, full pixel geometry held" if groups[-3] else
            "G2-7F §13.3.7 original Rule/Observation/Permission text read" if groups[-4] else
            "G2-7E §13.3.6 VITA66 optical source text and original native companion held" if groups[-5] else
            "G2-7D §13.3.5 Switch AMPS dense matrix audit held" if groups[-6] else
            "G2-7C §13.3.4 Payload AMPS dense matrix audit held" if groups[-7] else
            "G2-7B AMPS grammar, original ANSI/VITA held" if groups[-8] else
            "G2-7A AMPS protocol code definitions read" if groups[-9] else
            "Earlier original C239 source-qualified review, native companions held" if so or any(groups[:-9]) else "Not assessed here")
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),
             r.get("master_inclusion",""),r.get("dim_adoption",""),"; ".join(r.get("source_entry_ids",[])),
             json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
             "; ".join(ids),"; ".join(relations),status])
    return out

def publish():
    m=load(MASTER);legacy=load(LEDGER);check_source(m,legacy);check_g2_7i_source(m)
    stored=(D/BOOK).read_bytes()
    if digest(stored)==OLD:prev=stored
    else:
        from subprocess import check_output
        need(digest(stored)==m["currentWorkbookSha256"] and m["workbookSnapshot"]["currently_matches_readable_view"],
             "current saved workbook hash/metadata before replay")
        prev=check_output(["git","show","8158322ddcf33c78de83e9f55071aee1ec46066b:Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk/Master_Donor_Concept_to_DIM_Crosswalk.xlsx"])
    need(digest(prev)==OLD,"unchanged prior source-qualified G2-7H workbook before G2-7I publication")
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
    need(sum(bool(re.fullmatch(r"A\\d+",cell)) for cell in registerCells)==330,"DIM Register 329 stable row IDs retained")
    before=old.readcells(prev,"Master Crosswalk")
    delta=[a for a in set(before)|set(actual) if before.get(a,"")!=actual.get(a,"")]
    need(len(delta)==25 and all(re.fullmatch(r"I\\d+",a) for a in delta),"25 exact SOSA-I changes only, no case/other-donor/ISA/DIM changes")
    if digest(stored)!=OLD:need(digest(saved)==digest(stored),"byte-for-byte replay of already-published same workbook")
    (D/BOOK).write_bytes(saved);sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-7I_ORIGINAL_CLASS12_J1_SOURCE_AND_SAME_26_SHEET_EXCEL_VERIFIED__SOSA_OPEN"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-7I-CANONICAL-VERIFIED","sha256":sha,
          "currently_matches_readable_view":True,
          "lag":"NONE: all 346x15 saved Excel cells match JSON/BOTH CSV/BOTH MD",
          "refreshed_cell_count":25,"validation_file":REPORT})
    m["SOSAEvidence"]["G2_7I"].update({"excel_checkpoint":"SOSA-G2-7I-CANONICAL-VERIFIED",
          "excel_validation":REPORT,"Excel_lag_cells":0,"same_saved_workbook_25_cells_synced":True})
    m["SOSAReviewCompletion"]["G2_7I_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="OPEN__G2_7I_SAME_SAVED_EXCEL_VERIFIED__18_UNREAD_1_RESTRICTED_EXTERNAL_SOURCE_HOLDS"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="G2-7J original C239 §13.5.2.3 J2 signal connector, one source-sized packet only"
    m["nextOwnerAction"]="Only distinct owner Proceed starts G2-7J original C239 §13.5.2.3; SOSA ACTIVE and SAPIENT blocked"
    m["publicationPolicy"]="L23 G2-7I:25 source-qualified column-I cells in JSON/BOTH CSV/BOTH Markdown/SAME original 26-sheet Excel, all 346x15 cells saved-verified"
    save(MASTER,m)
    record={"date":"2026-11-11","step":"SOSA-G2-7I-EXCEL-CHECKPOINT",
         "result":"SAME_26_SHEET_SAVED_XLSX_AND_BOTH_CSV_AND_BOTH_MD_PARITY_PASS",
         "workbook_sha256":sha,"base_workbook_sha256":OLD,"workbook_sheets":list(paths),
         "refreshed_sheets":list(tables),"exact_original_untouched_xml_sha256":retained,
         "information_rows":329,"grid_rows":346,"columns":15,
         "original_donor_evidence":58,"case_evidence":73,"ISA_primary_source_outcomes":480,"original_ISA_questions_open":6,
         "G2_7I_original_headings_newly_touched":3,"G2_7I_original_native_items":82,
         "G2_7I_numbered_rules":23,"G2_7I_rule_method_I":18,"G2_7I_rule_method_A":5,
         "G2_7I_permissions":4,"G2_7I_observations":3,"G2_7I_connector_rows":16,"G2_7I_J1_pin_rows":11,
         "G2_7I_source_holds":20,"G2_7I_qualified_existing_sosa_cells":25,"changed_saved_cells":sorted(delta),
         "C239_at_least_sampled_or_inline_read":173,"C239_unread":18,"C239_restricted":1,
         "original_figure_pixels_verified":False,"original_external_standards_or_C239_native_companions_examined":False,
         "earlier_G2_7H_holds":17,"earlier_G2_7G_holds":19,
         "checks":{"all_actual_XLSX_346x15_cells_equal_JSON_both_CSV_both_MD":True,
          "both_CSVs_equal":True,"both_readable_MDs_equal":True,
          "same_26_worksheet_names_order":True,"22_untouched_historical_XMLs_preserved":True,
          "only_25_SOSA_I_cells_changed":True,"valid_ZIP_CRC_and_XML":True,"no_spreadsheet_error_cells":True,
          "zero_DIM_Profile_adoption":True},
         "limits":["§13.5 overall and §13.5.2 parent only PARTIAL, stop before J2 §13.5.2.3",
          "External SAE/MIL/VITA original sources, images, native C239 DSDM/IDL/OpenAPI, later S251 and restricted AppendixC held",
          "Observation with printed (I) is not a numbered Rule; Permission13.5.2-4 native numbering retained",
          "No actual source-case installed physical interface or hardware runtime conformance tested",
          "Preview generated from actual saved worksheet XML, not native Excel app screenshot"],
         "next":"Only separate owner Proceed begins G2-7J original §13.5.2.3 J2, SOSA OPEN and SAPIENT blocked"}
    save(REPORT,record)
    print("PASS: 25 source-qualified G2-7I SOSA cells in SAME original saved 26-sheet Excel, SHA",sha)
    return sha

def preview():
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER);actual=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_7I_source_correspondence")]
    need(len(rows)==25,"25 G2-7I source-qualified donor comparisons saved")
    try:
        font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:font=bold=ImageFont.load_default()
    width,height=1580,2630
    img=Image.new("RGB",(width,height),"white")
    pen=ImageDraw.Draw(img);pen.rectangle((0,0,width,65),fill="#173855")
    pen.text((18,17),"SOSA-G2-7I: 25 saved electrical Class1&2 J1 source cells — C239 §13.5",font=bold,fill="white")
    for i,r in enumerate(rows):
        hit=[k+1 for k,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(hit)==1,"unique original source row "+r["row_id"])
        address="I"+str(hit[0]);value=actual.get(address,"")
        need(value==r["display"][8],"actual source cell from saved original Excel "+address)
        y=72+i*98
        pen.rectangle((10,y,width-12,y+91),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        pen.text((20,y+7),r["row_id"]+" | "+address+" | "+r["label"],font=bold,fill="#173855")
        snippet="G2-7I: "+value.split("G2-7I:",1)[1] if "G2-7I:" in value else value
        for j,line in enumerate(textwrap.wrap(snippet,width=165,break_long_words=False)[:3]):
            pen.text((20,y+33+j*17),line,font=font,fill="#203951")
    img.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>10000,"saved source-cell preview generated")
    print("PASS: 25 G2-7I SOSA original source-cell preview rendered from saved worksheet XML")
if __name__=="__main__":
    publish()
    preview()
