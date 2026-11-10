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
REPORT="SOSA_G2_6D_Workbook_Validation_10NOV2026.json"
PREVIEW="SOSA_G2_6D_Workbook_Preview_10NOV2026.png"
OLD="1269d6f28527772ea00a7edf459264e97520adfd0ccd367483487c268d55bb7f"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-G2-6D verification failed: "+message
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
    need(m["currentWorkbookSha256"]==OLD and m["workbookSnapshot"]["sha256"]==OLD
         and not m["workbookSnapshot"]["currently_matches_readable_view"],"previous G2-6C saved 26-sheet source snapshot")
    need(m["SOSAReviewCompletion"]["G2_6D_XLSX_lag"]==14,"explicit source-to-XLSX pending L23 exit")
    print("PASS: G2-6D C239 Legacy source 20 native records, 6 analytical contexts and 14 qualified comparisons; prior original evidence preserved")
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
       ["SOSA-G2-6D original-source and Excel","C239 §13.2.13 Legacy PDF249–252 before §13.3 AMPS"],
       ["Master grid","329 information rows, 346 presentation rows, 15 columns"],
       ["Original source standing","One original C239 TOC heading, 3 nested original inline sections"],
       ["Native numbered clauses","4 Rules/SHALL; 2 Recommendations/SHOULD, not universal device rules"],
       ["Other source items","4 narrative process statements (2 conditional SHALL), 2 figure captions"],
       ["Native profile details","7 subordinate module-profile choices and 1 narrow radial-clock -1 legacy dash"],
       ["Item accounting","20 native source items and 6 analytical contexts, not new DIM fields"],
       ["Legacy definition","Edition1.1 planned future PICP profile removal, NOT installed device failure, expiry or retirement"],
       ["Certification timing","Actual removal date unverified; 18-month grace SHALL only after removal; submission bar after grace"],
       ["Source identifiers","3U 2F2U Payload/6U 16U20F Switch and specific radial-clock -1; VITA originals unread"],
       ["Original source discrepancy","Printed 6U Rules -2/-3 without -1; distinct MOD6-SWH-16F20U vs SLT6-SWH-16U20F"],
       ["Source access limitations","Original ANSI/VITA and eight DSDM/IDL/OpenAPI files, two figure geometries unexamined"],
       ["Qualified source master changes","14 existing SOSA column-I cells, zero non-target cell changes"],
       ["Original corpus remaining","152 sampled/inline-read, 39 substantively unread, one restricted of 192 headings"],
       ["Preserved records","58 original donor,73 source case, ISA480/six questions and all prior SOSA source evidence"],
       ["No adoption/conformance","No DIM classes/cardinality, Profile SHALL, actual device operation or tested certification"],
       ["Saved workbook parity","SAME 26-sheet Excel all 346x15 cells equal JSON/both CSV/both Markdown"],
       ["Only next owner Proceed","SOSA-G2-7A original §13.3 AMPS source-sized first packet; donor remains OPEN"]
    ]

def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        groups=[r.get(name) or {} for name in ("G2_1_source_correspondence","G2_2_source_correspondence","G2_3_source_correspondence",
            "G2_4A_source_correspondence","G2_4B_source_correspondence","G2_5_source_correspondence","G2_6A_source_correspondence","G2_6B_source_correspondence","G2_6C_source_correspondence","G2_6D_source_correspondence")]
        ids=so.get("records",[])+[v for g in groups for v in g.get("source_item_ids",[])]
        relations=so.get("relations",[])+[g.get("relation",g.get("mapping_relation","")) for g in groups if g]
        status=("G2-6D C239 Legacy original source reviewed; VITA figure and edition/removal date held; no DIM/Profile adoption" if groups[-1] else
            "G2-6C 6U PIC original inline source reviewed; external native VITA and geometry held" if groups[-2] else
            "G2-6B 3U PIC original inline source reviewed; external native geometry held" if groups[-3] else
            "G2-6A and earlier bounded C239 original review, native companions held" if so or any(groups[:-3]) else "Not assessed here")
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),
             r.get("master_inclusion",""),r.get("dim_adoption",""),"; ".join(r.get("source_entry_ids",[])),
             json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
             "; ".join(ids),"; ".join(relations),status])
    return out

def publish():
    m=load(MASTER);l=load(LEDGER);check_source(m,l)
    prev=(D/BOOK).read_bytes()
    need(digest(prev)==OLD,"same verified prior G2-6C 26-sheet workbook bytes")
    with zipfile.ZipFile(io.BytesIO(prev)) as z:
        need(z.testzip() is None,"prior source workbook ZIP CRC")
        paths=old.sheetpaths(z);need(len(paths)==26,"all 26 original sheets")
        styles,sty=old.newstyles(z.read("xl/styles.xml"))
        tables={"Master Crosswalk":m["review_grid"],"DIM Register":register(m),
                "Summary":summary(m),"Validation":summary(m)}
        replacement={"xl/styles.xml":styles}
        for n,rows in tables.items():
            replacement[paths[n]]=matrix_to_xml(rows,sty,main=n=="Master Crosswalk",
               sections=m["review_sections"] if n=="Master Crosswalk" else ())
        retained={n:digest(z.read(path)) for n,path in paths.items() if n not in tables}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as dst:
            for info in z.infolist():dst.writestr(info,replacement.get(info.filename,z.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as z:
        need(z.testzip() is None and list(old.sheetpaths(z))==list(paths),"saved ZIP CRC and original 26-sheet order")
        for name,h in retained.items():need(digest(z.read(paths[name]))==h,"untouched original worksheet "+name)
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                need(not any(cell.get("t")=="e" for cell in ET.fromstring(z.read(path)).iter(q("c"))),"no error cell "+path)
        root=ET.fromstring(z.read(paths["Master Crosswalk"]))
        merges=[x.get("ref") for x in root.find(q("mergeCells")).findall(q("mergeCell"))]
        need(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],"original header/topic merges")
        pane=root.find(q("sheetViews")).find(q("sheetView")).find(q("pane"))
        need(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","four original source cases/frozen headings")
    actual=old.readcells(saved,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for j,val in enumerate(row,1):need(actual.get(addr(i,j),"")==old.val(val),"actual saved cell "+addr(i,j))
    reg=old.readcells(saved,"DIM Register")
    need(sum(bool(re.fullmatch(r"A\d+",name)) for name in reg)==330,"same 329 stable source row ids in DIM Register")
    before=old.readcells(prev,"Master Crosswalk")
    delta=[a for a in set(before)|set(actual) if before.get(a,"")!=actual.get(a,"")]
    need(len(delta)==14 and all(re.fullmatch(r"I\d+",a) for a in delta),
         "exactly 14 source-qualified SOSA column-I cells changed; no other master edits")
    (D/BOOK).write_bytes(saved)
    sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-6D_ORIGINAL_LEGACY_PROFILE_SOURCE_AND_SAVED_26_SHEET_EXCEL_VERIFIED__DONOR_OPEN"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-6D-CANONICAL-VERIFIED","sha256":sha,
        "currently_matches_readable_view":True,
        "lag":"NONE: all 346x15 actual saved Excel cells equal canonical JSON/both CSV/both Markdown",
        "refreshed_cell_count":14,"validation_file":REPORT})
    m["SOSAEvidence"]["G2_6D"].update({"excel_checkpoint":"SOSA-G2-6D-CANONICAL-VERIFIED",
        "excel_validation":REPORT,"Excel_lag_cells":0,"same_saved_workbook_14_cells_synced":True})
    m["SOSAReviewCompletion"]["G2_6D_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="OPEN__G2_6D_VERIFIED__39_UNREAD_1_RESTRICTED_AND_NATIVE_COMPANIONS"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="SOSA-G2-7A original C239 §13.3 AMPS, bounded first source packet, only after separate owner Proceed"
    m["nextOwnerAction"]="Only separate owner Proceed may start G2-7A original §13.3 AMPS source-sized first packet; SOSA OPEN, Step18 SAPIENT blocked."
    m["publicationPolicy"]="L23 G2-6D applied: 14 source-qualified SOSA column-I cells in JSON, both CSV, both Markdown and SAME saved 26-sheet Excel; all 346x15 saved cells verified; source coverage/model adoption separate."
    save(MASTER,m)
    record={"date":"2026-11-10","step":"SOSA-G2-6D-EXCEL-CHECKPOINT",
       "result":"EXACT_SAVED_26_SHEET_XLSX_AND_TWO_CSV_TWO_MD_PARITY_PASS",
       "workbook_sha256":sha,"base_workbook_sha256":OLD,"workbook_sheets":list(paths),
       "refreshed_sheets":list(tables),"exact_original_untouched_xml_sha256":retained,
       "information_rows":329,"grid_rows":346,"columns":15,"original_donor_evidence":58,
       "case_evidence":73,"ISA_primary_source_outcomes":480,"original_ISA_questions_open":6,
       "G2_6D_original_toc_heading_newly_read":1,"G2_6D_inline_subclauses":3,
       "G2_6D_native_source_records":20,"G2_6D_analytical_contexts":6,"G2_6D_exact_holds":14,
       "G2_6D_source_numbered_rule_shalls":4,"G2_6D_source_numbered_recommendations":2,
       "G2_6D_source_conditional_narrative_shalls":2,"G2_6D_source_profile_alternatives":7,
       "G2_6D_qualified_existing_sosa_cells":14,"changed_saved_cells":sorted(delta),
       "unread_original_C239_TOC_headings":39,"restricted_original_C239_TOC_headings":1,
       "native_DSDM_IDL_OpenAPI_unread":8,"original_ANSI_VITA_unread":True,
       "checks":{"all_XLSX_346x15_grid_cells_equal_JSON_both_CSVs_both_MD":True,
         "two_CSV_mirrors_equal":True,"two_GitHub_readable_comparisons_equal":True,
         "same_26_worksheet_names_order":True,"22_historical_worksheet_XML_bytes_preserved":True,
         "only_14_original_SOSA_I_column_cells_changed":True,"valid_ZIP_CRC_and_XML":True,
         "zero_XLSX_error_type_cells":True,"zero_DIM_Profile_adoption":True},
       "limits":["Only original C239 §13.2.13 Legacy and children reviewed; §13.3 onward not audited",
         "ANSI/VITA original slot/module profiles, eight DSDM/IDL/OpenAPI native file contents unread",
         "Two figure captions/readable text inspected; precise original figure pixel geometry not verified",
         "No actual later standards removal date or certification expiry established; 18-month rule conditional",
         "No installed device/physical Command, DIM/Profile adoption or independent conformance",
         "PNG preview is based on saved XLSX XML source-cell rendering, NOT an Excel application screenshot"],
       "next":"Only separate owner Proceed starts G2-7A original §13.3 AMPS first bounded packet; SOSA OPEN, SAPIENT blocked"}
    save(REPORT,record)
    print("PASS: G2-6D SAME 26-sheet 346x15 saved-cell parity, 14 SOSA source cells, 22 preserved tabs; SHA256",sha)
    return sha

def preview():
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER);actual=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_6D_source_correspondence")]
    need(len(rows)==14,"14 original G2-6D comparisons in saved workbook")
    try:
        font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:font=bold=ImageFont.load_default()
    width,height=1580,1520
    img=Image.new("RGB",(width,height),"white");pen=ImageDraw.Draw(img)
    pen.rectangle((0,0,width,65),fill="#173855")
    pen.text((18,17),"SOSA-G2-6D: 14 saved Excel legacy PIC cells — original C239 §13.2.13",font=bold,fill="white")
    for i,r in enumerate(rows):
        hit=[k+1 for k,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(hit)==1,"unique current source row "+r["row_id"])
        a="I"+str(hit[0]);v=actual.get(a,"")
        need(v==r["display"][8],"actual saved workbook cell "+a)
        y=72+i*98;pen.rectangle((10,y,width-12,y+91),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        pen.text((20,y+7),r["row_id"]+" | "+a+" | "+r["label"],font=bold,fill="#173855")
        snippet="G2-6D: "+v.split("G2-6D:",1)[1] if "G2-6D:" in v else v
        for j,line in enumerate(textwrap.wrap(snippet,width=165,break_long_words=False)[:3]):
            pen.text((20,y+33+j*17),line,font=font,fill="#203951")
    img.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>10000,"valid saved XLSX source-cell preview")
    print("PASS: 14 G2-6D saved SOSA source-cell preview rendered from Excel XML")
if __name__=="__main__":
    publish()
    preview()
