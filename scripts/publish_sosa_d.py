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
    check(step["status"] in ("SCHEMA_SOURCE_READ__PUBLISHER_PENDING","SOURCE_FIRST_PART2_SELECTED_INTERFACES_COMPLETE__SAVED_PUBLICATION_PENDING"),"source-stage gate")
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
    intro=("# CURRENT — "+step_code+" original-source comparison and same 26-sheet workbook VERIFIED (14 November 2026)\n\n"+
       step.get("publication_intro",step_code+" selected original source research.")+" "+
       "SAME original 337-row, 354×16, 26-sheet workbook; both CSV and Markdown mirrors; M00/M01 and source colors preserved. "+
       "[Original source report]("+step["report"]+") · [Cumulative source ledger and saved verification]("+fn+"). "+
       "AAS remains ACTIVE/incomplete, no DIM/Profile adoption. ONE NEXT separate owner Proceed = "+("AAS07" if step_code=="AAS06" else "AAS06")+" only; STOP.\n\n---\n\n")
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
    def append_note(z,path,label,message):
        root=ET.fromstring(z.read(path));data=root.find(q("sheetData"))
        rows=data.findall(q("row"));num=max(int(x.get("r")) for x in rows)+1
        s=(rows[-1].find(q("c")).get("s","0") if rows[-1].find(q("c")) is not None else "0")
        nr=ET.SubElement(data,q("row"),{"r":str(num),"ht":"58","customHeight":"1"})
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
            rr=rows[int(addr[1:])-1]
            height=min(252,max(float(rr.get("ht","30")),90+len(c["after"])//8))
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
            rr.set("ht",str(min(252,max(float(rr.get("ht","30")),95+len(readcell(oldcell))//10))))
            rr.set("customHeight","1")
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
            check(cells[addr].get("s")==c.get("s","0") or cells[addr].get("s","0")==c.get("s","0"),"original cell classification style "+addr)
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
       "manual_version_sha256":{m00.name:digest(m00.read_bytes()),m01.name:digest(m01.read_bytes())},
       "checks":{"saved_grid_equals_JSON":True,"both_CSV_equal_JSON":True,"both_Markdown_equal_JSON":True,
                 "all_other_donor_case_DIM_values_unchanged":True,"row_ids_order_and_topic_dividers_preserved":True,
                 "all_original_cell_styles_preserved":True,"325_classification_colors_and_67_mixed_holds_retained":True,
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
        for addr,cell in oldcells.items():need(cells[addr].attrib.get("s")==cell.attrib.get("s"),"original style "+addr)
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
    print(f"{step} PASS: original 26 sheets, other donor/case/DIM values, styles, 21 historical sheets and M00/M01 preserved.")
    print(f"{step} remains bounded research; later research, whole-donor coverage, model adoption and runtime conformance are not verified by this check.")


if __name__=="__main__":
    checkpoint=load(MASTER).get("currentEvidenceCheckpoint","")
    approval=load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json").get("AAS02",{}).get("owner_layout_decision",{}).get("status")
    if checkpoint=="AAS05_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED" and load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json").get("AAS06",{}).get("status")=="SOURCE_FIRST_PART2_SELECTED_INTERFACES_COMPLETE__SAVED_PUBLICATION_PENDING":
        publish_aas06()
    elif checkpoint=="AAS04_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED" and load("AAS01_Original_Source_Corpus_Coverage_13NOV2026.json").get("AAS05",{}).get("status")=="SCHEMA_SOURCE_READ__PUBLISHER_PENDING":
        publish_aas05()
    elif checkpoint in ("AAS03_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED", "AAS04_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED", "AAS05_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED", "AAS06_SAME_26_SHEET_SAVED_XLSX_PARITY_VERIFIED"):
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
