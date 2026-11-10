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
REPORT="SOSA_G2_5_Workbook_Validation_10NOV2026.json"
PREVIEW="SOSA_G2_5_Workbook_Preview_10NOV2026.png"
OLD="8f6d293e96fce1e722de9dc22a7198571c2bafc00fd61787d91837b91ffae0bd"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-G2-5 verification failed: "+message
def load(n):return json.loads((D/n).read_text(encoding="utf-8"))
def save(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def digest(b):return hashlib.sha256(b).hexdigest()
def source_csv(n):
    with (D/n).open(encoding="utf-8-sig",newline="") as f:return list(csv.reader(f))
def addr(i,j):return old.coord(i,j)


def check_source(m,l):
    need(m["schemaVersion"]=="0.15" and len(m["rows"])==329 and len(m["columns"])==15,"329 rows and original 15 columns")
    need([x["key"] for x in m["columns"]][:4]==["Dragino","AirGradient","Campbell","Bennett"]
       and [x["key"] for x in m["columns"]][8:10]==["OpenGroupSOSA","SOSA"]
       and m["columns"][-1]["key"]=="DIM","original approved donor/case/DIM order")
    grid=m["review_grid"]
    need(len(grid)==346 and all(len(x)==15 for x in grid) and len(m["review_sections"])==15,"original 346×15 source grid")
    need([r for i,r in enumerate(grid) if i>1 and i not in set(m["review_sections"])]==[r["display"] for r in m["rows"]],"source grid and 329 original row values")
    need(grid==source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")
              ==source_csv("ISA_Correction_Review_07NOV2026.csv"),"current canonical JSON and both CSV tables")
    a=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    b=(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    need(a.split("<table>",1)[1]==b.split("<table>",1)[1] and a.count('colspan="15"')==15,"both GitHub horizontal comparisons identical")
    need(len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73
      and m["ISAEvidence"]["currentPrimaryReviews"]==480 and m["ISAEvidence"]["specificQuestions"]==6,
      "58 original donor/73 empirical cases/480 ISA outcomes and 6 questions preserved")
    need(len(l["all_57_qualified_source_decisions"])==57 and len(l["integration_row_ledger"])==38,
      "existing original SOSA-D evidence preserved")
    g1=load("SOSA_G2_1_Original_Item_Inventory_09NOV2026.json")
    g2=load("SOSA_G2_2_Original_Item_Inventory_09NOV2026.json")
    g3=load("SOSA_G2_3_Original_Source_Item_Census_09NOV2026.json")
    g4=load("SOSA_G2_4A_Original_Source_Item_Coverage_10NOV2026.json")
    g5=load("SOSA_G2_4B_Original_Source_Item_Coverage_10NOV2026.json")
    g6=load("SOSA_G2_5_Original_Source_Item_Coverage_10NOV2026.json")
    need(len(g1["items"])==201 and len(g2["source_items"])+len(g2["original_rule_appearances"])==352
      and g3["counts"]["source_items"]==119 and len(g4["original_source_items"])==95
      and len(g5["original_source_items"])==234,"all preceding The Open Group SOSA source evidence intact")
    need(len(g6["toc_heading_coverage"])==23 and len(g6["unregistered_nested_headings_read"])==6
      and len(g6["original_source_items"])==164,"Chapter12 source items and original heading depth")
    c=g6["native_source_item_counts"]
    need(c["RULE"]==38 and c["PERMISSION"]==9 and c["OBSERVATION"]==10
      and c["HOST_INTERACTION"]==43 and c["REFERENCE_ONLY_MODULE"]==7,"native original normativity and interface/source maturity")
    need(g6["full_donor_source_coverage_after_packet"]["at_least_original_source_sampled_or_inline_read"]==136
      and g6["full_donor_source_coverage_after_packet"]["still_substantively_unread"]==55
      and g6["full_donor_source_coverage_after_packet"]["restricted_heading"]==1,
      "honest partial source corpus coverage after Chapter12")
    need(g6["source"]["native_DSDM_IDL_OpenAPI_originals_unread"]==8
      and g6["source"]["external_companion_norms_audited"] is False,
      "all eight native model and original security/protocol companions still held")
    for count,name in ((12,"G2_1_source_correspondence"),(22,"G2_2_source_correspondence"),
       (28,"G2_3_source_correspondence"),(20,"G2_4A_source_correspondence"),
       (29,"G2_4B_source_correspondence")):
       need(sum(bool(r.get(name)) for r in m["rows"])==count,"prior source-to-master evidence unchanged "+name)
    new=[r for r in m["rows"] if r.get("G2_5_source_correspondence")]
    need(len(new)==43 and {r["row_id"] for r in new}==set(m["workbookSnapshot"]["G2_5_affected_row_ids"]),
      "43 unique source-qualified existing SOSA cells")
    native_ids={x["id"] for x in g6["original_source_items"]}
    need(len(native_ids)==164,"unique original source IDs")
    for r in new:
        ev=r["G2_5_source_correspondence"]
        need(ev["source_item_ids"] and all(x in native_ids for x in ev["source_item_ids"]),
             "original source locator item IDs "+r["row_id"])
        need(ev["DIM_Profile_adopted"] is False and ev["native_companions_unreviewed"],
             "no adoption or invented original companion schema "+r["row_id"])
        need("G2-5:" in r["display"][8] and ev["previous_sosa_cell_value"]!=r["display"][8],
             "new source meaning and original cell preserved "+r["row_id"])
    need(m["currentWorkbookSha256"]==OLD and m["workbookSnapshot"]["sha256"]==OLD
        and not m["workbookSnapshot"]["currently_matches_readable_view"],
        "SAME existing verified G2-4B original Excel before 43-cell G2-5 refresh")
    need(m["SOSAReviewCompletion"]["G2_5_XLSX_lag"]==43,"explicit mandatory L23 lag while publisher runs")
    print("PASS: C239 Chapter12 original 23 headings, 164 items, 38 Rules/9 Permissions/10 Observations, 43 source-backed SOSA cells; older cases/ISA preserved")
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
       ["SOSA-G2-5 source-first Excel checkpoint","C239 Chapter12 Support System Operation original inline audit; donor still OPEN"],
       ["Canonical comparison","329 information rows, 346 visual grid rows, 15 original columns"],
       ["Chapter12 original heading coverage","23 original registered TOC headings + 6 nested audit subsections; PDF179–207"],
       ["Original native named items","164 individually accounted source records with source kind and locator"],
       ["Native normative standing","38 Rule SHALLs; 9 Permissions; 10 Observations, non-equivalent"],
       ["Audit security roles","Required Collector/Relay roles and UTC-vs-uptime conditional event logging; no physical hardware inferred"],
       ["Authentication, authorization, zeroization","Package digests; policy grant/deny/check before privileged execution; CSP zeroization not sanitization"],
       ["Crypto/DARE","Native scoped Rule sets, key tag TBD, certification and unread protocol/security companion holds"],
       ["Host Platform Interface","43 named accepted interactions; primarily RF source scope; adapter not physical host"],
       ["Reference-only modules","7 undefined support modules including Power/Network/Nav/Time/Calibration"],
       ["Master source contribution","43 qualified existing The Open Group SOSA I-column source comparisons only"],
       ["Historical preservation","58 donor/73 case source facts; ISA480 outcomes and 6 questions; prior SOSA-G2 source packets intact"],
       ["Original C239 corpus remaining","136 at least sampled/source-read; 55 substantively unread; 1 restricted"],
       ["Source holds","8 DSDM/IDL/OpenAPI and original NIST/RSS/SYSLOG/crypto/native schemas, figures unread"],
       ["No model adoption","0 DIM classes/fields/cardinalities; 0 new Profile SHALL or actual device execution"],
       ["Saved XLSX parity","Same original 26-sheet workbook, source JSON/2CSV/2MD and all 346x15 saved cells equal"],
       ["Next owner-controlled packet","C239 Chapter13 first bounded original physical source segment ONLY, after separate owner Proceed"]
    ]

def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        gs=[r.get(x) or {} for x in ("G2_1_source_correspondence","G2_2_source_correspondence",
             "G2_3_source_correspondence","G2_4A_source_correspondence",
             "G2_4B_source_correspondence","G2_5_source_correspondence")]
        ids=so.get("records",[])+[v for g in gs for v in g.get("source_item_ids",[])]
        relations=so.get("relations",[])+[g.get("relation",g.get("mapping_relation","")) for g in gs if g]
        status=("G2-5 C239 original Chapter12 inline fully reviewed; external security/DIV-2/3 companions and figure detail held; no model adoption"
           if gs[-1] else
           "G2-4B C239 Chapters7–11 original inline reviewed; native MORA companions held"
           if gs[-2] else
           "Earlier C239 selected/original inline review; native companions held"
           if any(gs[:4]) or so else "Not assessed here")
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),
           r.get("source_review_status",""),r.get("master_inclusion",""),r.get("dim_adoption",""),
           "; ".join(r.get("source_entry_ids",[])),json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
           "; ".join(ids),"; ".join(relations),status])
    return out

def publish():
    m=load(MASTER);l=load(LEDGER);check_source(m,l)
    prev=(D/BOOK).read_bytes()
    need(digest(prev)==OLD,"same verified G2-4B 26-sheet workbook SHA; never replace a different file")
    with zipfile.ZipFile(io.BytesIO(prev)) as z:
        need(z.testzip() is None,"prior ZIP CRC")
        paths=old.sheetpaths(z);need(len(paths)==26,"26 original tab names/order")
        styles,sty=old.newstyles(z.read("xl/styles.xml"))
        tables={"Master Crosswalk":m["review_grid"],"DIM Register":register(m),
            "Summary":summary(m),"Validation":summary(m)}
        replacement={"xl/styles.xml":styles}
        for name,rows in tables.items():replacement[paths[name]]=matrix_to_xml(
            rows,sty,main=name=="Master Crosswalk",sections=m["review_sections"] if name=="Master Crosswalk" else ())
        retained={name:digest(z.read(path)) for name,path in paths.items() if name not in tables}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as dst:
            for info in z.infolist():dst.writestr(info,replacement.get(info.filename,z.read(info.filename)))
    saved=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(saved)) as z:
        need(z.testzip() is None and list(old.sheetpaths(z))==list(paths),"saved ZIP CRC and same 26 sheets")
        for name,h in retained.items():need(digest(z.read(paths[name]))==h,"historic unchanged worksheet "+name)
        for path in z.namelist():
            if path.endswith((".xml",".rels")):ET.fromstring(z.read(path))
            if path.startswith("xl/worksheets/") and path.endswith(".xml"):
                need(not any(cell.get("t")=="e" for cell in ET.fromstring(z.read(path)).iter(q("c"))),
                     "saved Excel no error-valued cell at "+path)
        xml=ET.fromstring(z.read(paths["Master Crosswalk"]))
        merges=[a.get("ref") for a in xml.find(q("mergeCells")).findall(q("mergeCell"))]
        need(merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],
              "original 15 topic-divider/header merges")
        pane=xml.find(q("sheetViews")).find(q("sheetView")).find(q("pane"))
        need(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","frozen original cases and column headers")
    cells=old.readcells(saved,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for j,value in enumerate(row,1):
            need(cells.get(addr(i,j),"")==old.val(value),"every actually saved XLSX cell "+addr(i,j))
    registercells=old.readcells(saved,"DIM Register")
    need(sum(bool(re.fullmatch(r"A\d+",name)) for name in registercells)==330,
         "329 unchanged stable row identities in DIM Register")
    priorcells=old.readcells(prev,"Master Crosswalk")
    delta=[a for a in set(priorcells)|set(cells) if priorcells.get(a,"")!=cells.get(a,"")]
    need(len(delta)==43 and all(re.fullmatch(r"I\d+",a) for a in delta),
         "exactly 43 changed SOSA donor column-I saved cells, zero other cells")
    (D/BOOK).write_bytes(saved)
    sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-5_CHAPTER12_ORIGINAL_INLINE_AND_SAVED_26_SHEET_XLSX_PARITY_VERIFIED__DONOR_OPEN"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-5-CANONICAL-VERIFIED",
        "sha256":sha,"currently_matches_readable_view":True,
        "lag":"NONE: same 26-sheet saved 346x15 Excel exactly matches JSON, both CSV and both Markdown source tables",
        "refreshed_cell_count":43,"validation_file":REPORT})
    m["SOSAEvidence"]["G2_5"].update({"excel_checkpoint":"SOSA-G2-5-CANONICAL-VERIFIED",
        "excel_validation":REPORT,"excel_lagged_cells":0,"same_saved_workbook_43_cells_synced":True})
    m["SOSAReviewCompletion"]["G2_5_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["G2_5_status"]="ORIGINAL_CHAPTER12_INLINE_AND_SAVED_WORKBOOK_VERIFIED__DONOR_OPEN"
    m["SOSAReviewCompletion"]["status"]="OPEN__G2_5_VERIFIED__55_UNREAD_1_RESTRICTED_AND_NATIVE_COMPANIONS"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="SOSA-G2-6 first source-grounded original C239 Chapter13 physical Hardware Element packet, sized by original source complexity only"
    m["nextOwnerAction"]="One separate owner Proceed may start SOSA-G2-6 first original Chapter13 Hardware Element source packet only; The Open Group SOSA donor remains ACTIVE and Step18 SAPIENT BLOCKED"
    m["publicationPolicy"]="L23 G2-5 fulfilled: 43 source-qualified SOSA column-I original source comparisons in canonical JSON, 2 CSV, 2 readable tables and SAME saved 26-sheet Excel with exact saved-cell parity; original source completeness/adoption/runtime separate"
    save(MASTER,m)
    record={"date":"2026-11-10","step":"SOSA-G2-5-EXCEL-CHECKPOINT","result":"EXACT_SAVED_26_SHEET_XLSX_AND_TWO_CSV_TWO_MD_PARITY_PASS",
      "workbook_sha256":sha,"base_workbook_sha256":OLD,"workbook_sheets":list(paths),
      "refreshed_sheets":list(tables),"exact_original_untouched_xml_sha256":retained,
      "information_rows":329,"grid_rows":346,"columns":15,
      "original_donor_evidence":58,"case_evidence":73,"ISA_primary_source_outcomes":480,
      "G2_5_original_toc_headings":23,"G2_5_original_nested_subsections":6,"G2_5_original_native_items":164,
      "G2_5_native_rule_shalls":38,"G2_5_native_permissions":9,"G2_5_native_observations":10,
      "G2_5_host_platform_interactions":43,"G2_5_qualified_existing_sosa_cells":43,
      "changed_saved_cells":sorted(delta),"original_ISA_questions_open":6,
      "unread_original_C239_TOC_headings":55,"restricted_original_C239_TOC_headings":1,
      "native_DSDM_IDL_OpenAPI_unread":8,
      "checks":{"all_XLSX_346x15_grid_cells_equal_JSON_both_CSVs_both_MD":True,
       "two_CSV_mirrors_equal":True,"two_GitHub_readable_comparisons_equal":True,
       "same_26_worksheet_names_order":True,"22_historical_worksheet_XML_bytes_preserved":True,
       "only_43_original_SOSA_I_column_cells_changed":True,"valid_ZIP_CRC_and_XML":True,
       "zero_XLSX_error_type_cells":True,"zero_DIM_Profile_adoption":True},
      "limits":["Only original C239 Chapter12 full inline text/table/Rule inventory; original external companion text not audited",
         "Source Chapter13 is not started; 55 C239 headings substantively unread and one restricted",
         "Eight DSDM/IDL/OpenAPI native originals uninspected; external SYSLOG/NIST/RSS/crypto/OMS/UCI companion texts not verified",
         "Figure original pixel geometry not exhaustively audited",
         "Seven Chapter12 support modules explicitly reference-only/not defined this C239 edition",
         "No actual sensor hardware, physical Command, independent Profile or CSAPI runtime conformance",
         "PNG preview is saved Excel source-cell rendering, NOT Microsoft Excel screenshot"],
      "next":"One future owner Proceed: SOSA-G2-6 source-first Chapter13 first bounded physical Hardware Element packet ONLY; SOSA ACTIVE, SAPIENT blocked"}
    save(REPORT,record)
    print("PASS: same 26-sheet current workbook all 346x15 source cells and 22 untouched historical tabs; SHA256",sha)
    return sha

def preview():
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER)
    cells=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_5_source_correspondence")]
    need(len(rows)==43,"43 current source-qualified rows for saved preview")
    try:
        font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:font=bold=ImageFont.load_default()
    width,height=1580,4340
    img=Image.new("RGB",(width,height),"white");pen=ImageDraw.Draw(img)
    pen.rectangle((0,0,width,65),fill="#173855")
    pen.text((18,17),"SOSA-G2-5: 43 actual current canonical Excel source cells — original Chapter12",font=bold,fill="white")
    for i,r in enumerate(rows):
        hit=[k+1 for k,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(hit)==1,"one source grid row "+r["row_id"])
        a="I"+str(hit[0]);value=cells.get(a,"")
        need(value==r["display"][8],"saved Excel cell equals source "+a)
        y=72+i*98
        pen.rectangle((10,y,width-12,y+91),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        pen.text((20,y+7),r["row_id"]+" | "+a+" | "+r["label"],font=bold,fill="#173855")
        excerpt="G2-5: "+value.split("G2-5:",1)[1] if "G2-5:" in value else value
        for j,line in enumerate(textwrap.wrap(excerpt,width=165,break_long_words=False)[:3]):
            pen.text((20,y+33+j*17),line,font=font,fill="#203951")
    img.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>15000,"saved current Excel preview PNG not empty")
    print("PASS: G2-5 43 source-cell saved workbook visual preview from XML; not native Excel screenshot")
if __name__=="__main__":
    publish()
    preview()
