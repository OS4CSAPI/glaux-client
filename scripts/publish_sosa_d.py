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
REPORT="SOSA_G2_4B_Workbook_Validation_10NOV2026.json"
PREVIEW="SOSA_G2_4B_Workbook_Preview_10NOV2026.png"
OLD="fe63866c0ac561e9efcb903f72c5b108814afd3b4f3ee3bd1973dd6d1b5c4a0e"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-G2-4B verification failed: "+message
def load(n):return json.loads((D/n).read_text(encoding="utf-8"))
def save(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def digest(b):return hashlib.sha256(b).hexdigest()
def source_csv(n):
    with (D/n).open(encoding="utf-8-sig",newline="") as f:return list(csv.reader(f))
def addr(i,j):return old.coord(i,j)

def check_source(m,l):
    need(m["schemaVersion"]=="0.15" and len(m["rows"])==329 and len(m["columns"])==15,"original source schema, 329 source rows, 15 columns")
    need([x["key"] for x in m["columns"]][8:10]==["OpenGroupSOSA","SOSA"] and m["columns"][-1]["key"]=="DIM","The Open Group vs W3C SOSA and rightmost DIM preserved")
    need([x["key"] for x in m["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"],"four source-case columns intact")
    grid=m["review_grid"]
    need(len(grid)==346 and all(len(x)==15 for x in grid) and len(m["review_sections"])==15,"346x15 original source grid")
    need([r for i,r in enumerate(grid) if i>1 and i not in set(m["review_sections"])]==[r["display"] for r in m["rows"]],"row display and source grid exact")
    need(grid==source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")==source_csv("ISA_Correction_Review_07NOV2026.csv"),"BOTH CSV mirrors equal source")
    a=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    b=(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    need(a.split("<table>",1)[1]==b.split("<table>",1)[1] and a.count('colspan="15"')==15,"BOTH readable horizontal comparison tables equal")
    need(len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73 and m["ISAEvidence"]["currentPrimaryReviews"]==480 and m["ISAEvidence"]["specificQuestions"]==6,"58 donor/73 cases/480 ISA evidence and six ISA questions retained")
    need(len(l["all_57_qualified_source_decisions"])==57 and len(l["integration_row_ledger"])==38,"existing SOSA-D source decisions preserved")
    g1=load("SOSA_G2_1_Original_Item_Inventory_09NOV2026.json")
    g2=load("SOSA_G2_2_Original_Item_Inventory_09NOV2026.json")
    g3=load("SOSA_G2_3_Original_Source_Item_Census_09NOV2026.json")
    g4=load("SOSA_G2_4A_Original_Source_Item_Coverage_10NOV2026.json")
    g5=load("SOSA_G2_4B_Original_Source_Item_Coverage_10NOV2026.json")
    need(len(g1["items"])==201 and len(g2["source_items"])+len(g2["original_rule_appearances"])==352 and g3["counts"]["source_items"]==119,"prior C239 native source evidence retained")
    need(len(g4["chapter1_5_toc_coverage"])==42 and len(g4["original_source_items"])==95,"prior G2-4A source review retained")
    need(len(g5["chapter7_11_toc_coverage"])==27 and len(g5["original_source_items"])==234,"G2-4B 27 original heading and 234 native items")
    need(g5["source_item_counts"]["TASK_INTERACTION"]==36 and g5["source_item_counts"]["RF_INTERACTION"]==82 and g5["source_item_counts"]["explicit_original_C239_shall_rules"]==8 and g5["source_item_counts"]["reference_only_modules"]==9,"original native task / RF / rule / reference standing")
    need(g5["cumulative_C239_original_TOC_after_packet"]["at_least_source_sampled_or_inline_read"]==121 and g5["cumulative_C239_original_TOC_after_packet"]["still_substantively_unread"]==70,"honest C239 partial-coverage standing")
    need(not g5["source"]["external_MORA_VICTORY_VITA_source_files_inspected"] and g5["source"]["original_native_model_companion_files_uninspected"]==8,"unread original external companions remain held")
    need(sum(bool(r.get("G2_1_source_correspondence")) for r in m["rows"])==12
        and sum(bool(r.get("G2_2_source_correspondence")) for r in m["rows"])==22
        and sum(bool(r.get("G2_3_source_correspondence")) for r in m["rows"])==28
        and sum(bool(r.get("G2_4A_source_correspondence")) for r in m["rows"])==20,"prior cumulative SOSA source contributions retained")
    new=[r for r in m["rows"] if r.get("G2_4B_source_correspondence")]
    need(len(new)==29 and {r["row_id"] for r in new}==set(m["workbookSnapshot"]["G2_4B_affected_row_ids"]),"exactly 29 original SOSA source comparisons")
    ids={x["id"] for x in g5["original_source_items"]}
    need(len(ids)==234,"unique native original source IDs")
    for r in new:
        ev=r["G2_4B_source_correspondence"]
        need(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]),"real source item IDs "+r["row_id"])
        need(ev["DIM_adopted"] is False and ev["unverified_native_companions"] is True,"explicit nonadoption and source hold "+r["row_id"])
        need("G2-4B:" in r["display"][8] and ev["previous_sosa_cell_value"]!=r["display"][8],"prior SOSA meaning preserved "+r["row_id"])
    need(m["currentWorkbookSha256"]==OLD and m["workbookSnapshot"]["sha256"]==OLD and not m["workbookSnapshot"]["currently_matches_readable_view"],"same previously verified G2-4A XLSX, 29-cell pending exit")
    need(m["SOSAReviewCompletion"]["G2_4B_XLSX_lag"]==29,"explicit pending same-workbook source-cell lag")
    print("PASS: source-first C239 Chapters7-11 original 27 headings/234 items, 29 SOSA cells and prior full source/case/ISA evidence retained")
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
       ["SOSA-G2-4B source-first Excel checkpoint","C239 Chapters 7–11 original inline source; The Open Group SOSA remains OPEN"],
       ["Canonical comparison","329 information rows; 346 source grid rows; 15 columns"],
       ["Original source inventory","27 C239 chapter7–11 TOC headings, 234 native items"],
       ["Preliminary tasking","36 Table7.1.1-1 interactions, five conceptual detailed; not a required universal command schema"],
       ["RF functionality","19 CRE and 10 emitter functions; 20 CRE support functions (12 Future/8 V1.0), 10 emitter V1.0"],
       ["RF MORA interface","82 C239 Table8.3.5-1 interactions; three scoped original RF shall Rules"],
       ["Processing/analyze/report","9 source expressly not-defined reference-only module tables"],
       ["Storage/Retrieval Manager","5 original native shall Rules, 4 NVMe command/response rows; conditional source scope"],
       ["Source qualified comparisons","29 existing The Open Group SOSA column-I cells; all other donor/case/DIM cells retained"],
       ["Original C239 corpus","121 at least sampled/inline-reviewed; 70 substantively unread, 1 restricted"],
       ["Source limitations","MORA/VICTORY/VITA originals, 8 DSDM/IDL/OpenAPI native files and precise figure pixels unverified"],
       ["Preserved source work","G2-4A 20 cells/95 items; G2-3 119, G2-2 352, G2-1 201 native items"],
       ["Historical ISA/case","480 DMS outcomes and six questions; 58 donor / 73 cases preserved"],
       ["No adoption","No DIM classes, cardinality, CSAPI profile requirements, observed device control adopted"],
       ["Saved XLSX parity","Exact source JSON / both CSV / both readable MD / SAME 26-tab Excel saved 346x15"],
       ["Next owner controlled","SOSA-G2-5 original C239 Chapter12 source-only on separate Proceed; SAPIENT blocked"]
    ]

def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        gs=[r.get("G2_1_source_correspondence") or {},r.get("G2_2_source_correspondence") or {},r.get("G2_3_source_correspondence") or {},r.get("G2_4A_source_correspondence") or {},r.get("G2_4B_source_correspondence") or {}]
        src_ids=so.get("records",[])+[v for g in gs for v in g.get("source_item_ids",[])]
        relations=so.get("relations",[])+[g.get("relation",g.get("mapping_relation","")) for g in gs if g]
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),r.get("master_inclusion",""),r.get("dim_adoption",""),
           "; ".join(r.get("source_entry_ids",[])),json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
           "; ".join(src_ids),"; ".join(relations),
           "G2-4B C239 original source chapters7–11 inline reviewed; external MORA/native files held, no model adoption" if gs[-1]
           else "G2-4A C239 original chapters1–5 inline reviewed; native companions held" if gs[-2]
           else "C239 source scoped original review, native companions held" if any(gs[:3]) or so else "Not assessed here"])
    return out

def publish():
    m=load(MASTER);l=load(LEDGER);check_source(m,l)
    prev=(D/BOOK).read_bytes()
    need(digest(prev)==OLD,"same verified 26-sheet G2-4A canonical workbook binary hash; do not replace")
    with zipfile.ZipFile(io.BytesIO(prev)) as z:
        need(z.testzip() is None,"prior workbook ZIP CRC")
        paths=old.sheetpaths(z);need(len(paths)==26,"26 original named tabs")
        styles,style=old.newstyles(z.read("xl/styles.xml"))
        tables={"Master Crosswalk":m["review_grid"],"DIM Register":register(m),"Summary":summary(m),"Validation":summary(m)}
        need(set(tables)<=set(paths),"live original sheets exist")
        replacement={"xl/styles.xml":styles}
        for n,rows in tables.items():replacement[paths[n]]=matrix_to_xml(rows,style,main=n=="Master Crosswalk",sections=m["review_sections"] if n=="Master Crosswalk" else ())
        unchanged={n:digest(z.read(p)) for n,p in paths.items() if n not in tables}
        dst=io.BytesIO()
        with zipfile.ZipFile(dst,"w") as out:
            for info in z.infolist():out.writestr(info,replacement.get(info.filename,z.read(info.filename)))
    new=dst.getvalue()
    with zipfile.ZipFile(io.BytesIO(new)) as z:
        need(z.testzip() is None and list(old.sheetpaths(z))==list(paths),"new ZIP CRC and 26-tab order")
        for n,h in unchanged.items():need(digest(z.read(paths[n]))==h,"preserve original untouched tab "+n)
        for p in z.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(z.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(c.get("t")=="e" for c in ET.fromstring(z.read(p)).iter(q("c"))),"no Excel error at "+p)
        master=ET.fromstring(z.read(paths["Master Crosswalk"]))
        merges=[x.get("ref") for x in master.find(q("mergeCells")).findall(q("mergeCell"))]
        need(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],"group and section merges")
        pane=master.find(q("sheetViews")).find(q("sheetView")).find(q("pane"))
        need(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","original main freeze panes")
    cells=old.readcells(new,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for j,value in enumerate(row,1):need(cells.get(addr(i,j),"")==old.val(value),"actual saved XLSX source cell "+addr(i,j))
    reg=old.readcells(new,"DIM Register")
    need(sum(bool(re.fullmatch(r"A\d+",s)) for s in reg)==330,"DIM Register retains 329 stable row identifiers")
    oldcells=old.readcells(prev,"Master Crosswalk")
    delta=[a for a in set(oldcells)|set(cells) if oldcells.get(a,"")!=cells.get(a,"")]
    need(len(delta)==29 and all(re.fullmatch(r"I\d+",a) for a in delta),"only 29 The Open Group SOSA column I saved cells change")
    (D/BOOK).write_bytes(new)
    sha=digest(new)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-4B_ORIGINAL_CHAPTERS7_11_AND_SAVED_XLSX_SOURCE_PARITY_VERIFIED__DONOR_OPEN"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-4B-CANONICAL-VERIFIED","sha256":sha,
        "information_rows":329,"columns":15,"currently_matches_readable_view":True,
        "lag":"NONE: all 346x15 actual XLSX cells agree with current JSON, BOTH CSV and BOTH readable tables",
        "refreshed_cell_count":29,"G2_4B_affected_row_ids":m["workbookSnapshot"]["G2_4B_affected_row_ids"],
        "validation_file":REPORT})
    m["SOSAEvidence"]["G2_4B"].update({"excel_publication":"SAVED_26_SHEET_XLSX_VERIFIED_NO_LAG","excel_validation":REPORT,"excel_29_source_cells_synced":True,"excel_lag_count":0})
    m["SOSAReviewCompletion"]["G2_4B_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="OPEN__G2_4B_ORIGINAL_INLINE_TEXT_TABLE_REVIEW_COMPLETE__REMAINING_CHAPTER12_13_14_15_AND_COMPANIONS"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="SOSA-G2-5 original C239 Chapter12 Support System Operation ONLY; further source coverage before donor closure"
    m["nextOwnerAction"]="SOSA-G2-5 only after separate owner Proceed: original C239 Chapter12 Support System Operation source review. The Open Group SOSA donor OPEN; SAPIENT blocked."
    m["publicationPolicy"]="Binding L23 verified G2-4B: 29 source-qualified SOSA comparison cells current in JSON, 2CSV, 2MD and SAME saved 26-sheet Excel. Original source coverage/donor closure, DIM/Profile adoption and runtime conformance remain separate."
    save(MASTER,m)
    record={"date":"2026-11-10","step":"SOSA-G2-4B-EXCEL-CHECKPOINT","result":"EXACT_SAVED_26_SHEET_XLSX_AND_TWO_CSV_TWO_MD_PARITY_PASS",
       "workbook_sha256":sha,"base_workbook_sha256":OLD,"workbook_sheets":list(paths),
       "refreshed_sheets":list(tables),"exact_original_untouched_xml_sha256":unchanged,
       "information_rows":329,"grid_rows":346,"columns":15,
       "original_donor_evidence":58,"case_evidence":73,"ISA_primary_source_outcomes":480,
       "G2_4B_original_inline_source_headings":27,"G2_4B_original_source_items":234,"G2_4B_source_normative_rules":8,
       "G2_4B_qualified_existing_source_cells":29,"changed_saved_cells":sorted(delta),
       "G2_5_C239_original_Chapter12_pending":True,"native_DSDM_IDL_OpenAPI_unread":8,
       "original_MORA_VICTORY_VITA_not_read":True,"original_ISA_source_questions_open":6,
       "checks":{"all_XLSX_346x15_grid_cells_equal_JSON_both_CSVs_both_MD":True,
          "two_CSV_mirrors_equal":True,"two_GitHub_readable_comparisons_equal":True,
          "same_26_worksheet_names_order":True,"22_historical_worksheet_XML_bytes_preserved":True,
          "only_29_original_SOSA_I_column_cells_changed":True,
          "valid_ZIP_CRC_and_XML":True,"zero_XLSX_error_type_cells":True,"zero_DIM_Profile_adoption":True},
       "limits":["Only original C239 Chapters7–11 inline text/tables read, not entire original C239 corpus",
          "MORA, VICTORY, ANSI/VITA native specifications not read",
          "Eight DSDM/IDL/OpenAPI companion originals uninspected; restricted Appendix C and S251 edition uninspected",
          "Figure pixel/arrow geometry not independently verified",
          "Reference-only modules do not have established 2023 normative implementations",
          "No hardware/CSAPI runtime, physical Command or independent OGC conformance test",
          "PNG preview rendered from saved XLSX values, not Microsoft Excel screenshot"],
       "next":"SOSA-G2-5 original C239 Chapter12 only on separate owner Proceed; donor remains OPEN"}
    save(REPORT,record)
    print("PASS: same 26-sheet workbook source parity 346x15 and preserved 22 historical tabs; new SHA256",sha)
    return sha

def preview():
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER)
    cells=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_4B_source_correspondence")]
    need(len(rows)==29,"29 original source-qualified rows for preview")
    try:
        f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        fb=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:f=fb=ImageFont.load_default()
    width,height=1560,2970
    img=Image.new("RGB",(width,height),"white")
    pen=ImageDraw.Draw(img)
    pen.rectangle((0,0,width,65),fill="#173855")
    pen.text((18,17),"SOSA-G2-4B: 29 saved canonical Excel source cells — original C239 Chapters7–11",font=fb,fill="white")
    for i,r in enumerate(rows):
        hit=[k+1 for k,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(hit)==1,"one source row for "+r["row_id"])
        address="I"+str(hit[0]);value=cells.get(address,"")
        need(value==r["display"][8],"saved Excel cell matches source "+address)
        y=72+i*98
        pen.rectangle((10,y,width-12,y+91),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        pen.text((20,y+7),r["row_id"]+" | "+address+" | "+r["label"],font=fb,fill="#173855")
        excerpt="G2-4B: "+value.split("G2-4B:",1)[1] if "G2-4B:" in value else value
        for j,line in enumerate(textwrap.wrap(excerpt,width=165,break_long_words=False)[:3]):
            pen.text((20,y+33+j*17),line,font=f,fill="#203951")
    img.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>15000,"actual saved workbook PNG preview")
    print("PASS: G2-4B saved XLSX source grid preview rendered; not native Excel screenshot")
if __name__=="__main__":
    publish()
    preview()
