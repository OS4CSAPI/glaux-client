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
REPORT="SOSA_G2_6A_Workbook_Validation_10NOV2026.json"
PREVIEW="SOSA_G2_6A_Workbook_Preview_10NOV2026.png"
OLD="e793461d393bee743b8cf3464f2f6274244a0cbc4cb630a42b772f676615188a"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-G2-6A verification failed: "+message
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
    need(m["currentWorkbookSha256"]==OLD and m["workbookSnapshot"]["sha256"]==OLD
         and not m["workbookSnapshot"]["currently_matches_readable_view"],"previous G2-5 saved 26-sheet source snapshot")
    need(m["SOSAReviewCompletion"]["G2_6A_XLSX_lag"]==39,"explicit source-to-XLSX pending L23 exit")
    print("PASS: G2-6A original C239 13 headings, 98 Rule/8 Permission/3 Recommendation/21 Observation labels, 39 justified SOSA source cells and preserved history")
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
       ["SOSA-G2-6A original-source and Excel","C239 §§13.1–13.2.10 first bounded Hardware Element source audit"],
       ["Master shape","329 information rows; 346 presentation rows; 15 columns"],
       ["Original coverage","13 original TOC headings, 19 nested source sections, PDF208–229 with CoV line on230"],
       ["Native source standing","98 Rule SHALL, 8 Permission MAY, 3 Recommendation SHOULD, 21 Observations"],
       ["Native tables, figures, CoV","10 source tables, 5 figure captions, 11 source-required CoV disclosure fields"],
       ["Source inventory accounting","156 native labeled/table/CoV records plus 12 analytical contextual summaries"],
       ["Hardware identity","Physical PIC, PSC, chassis, backplane, XMC and host distinct; no universal DIM root"],
       ["Power source boundaries","VS rails, VBAT/ALT_VBAT voltage/current limits and PSC outputs not installed battery/telemetry"],
       ["Cooling and mechanical","3U/6U, 100mm short and 160mm, slot pitch, conduction/air/liquid compatibility conditional"],
       ["Management scope","Maintenance Console Port UART for service/debug, not operational control interface"],
       ["CoV/document source","Required hardware vendor memory disclosures, not verified original case vendor CoV"],
       ["C239 original source limitations","Uninspected original ANSI/VITA and 8 native DSDM/IDL/OpenAPI; exact figure pixel geometry held"],
       ["Source-qualified donor comparisons","39 existing The Open Group SOSA column-I cells, zero non-target edits"],
       ["Original-source corpus remaining","149 at least sampled/inline-reviewed, 42 unread, 1 restricted of 192 headings"],
       ["Evidence preservation","58 donor/73 case facts, ISA480 outcomes/6 questions, prior SOSA source findings"],
       ["Model adoption and conformance","No new DIM classes/cardinality, Profile SHALL or actual device test"],
       ["Actual saved workbook parity","Same 26 tabs, exact saved 346x15 JSON/2CSV/2MD Excel source cells"],
       ["Only next owner Proceed","SOSA-G2-6B from §13.2.11, bounded original hardware PICP source packet"]
    ]

def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        groups=[r.get(name) or {} for name in ("G2_1_source_correspondence","G2_2_source_correspondence","G2_3_source_correspondence",
            "G2_4A_source_correspondence","G2_4B_source_correspondence","G2_5_source_correspondence","G2_6A_source_correspondence")]
        ids=so.get("records",[])+[v for g in groups for v in g.get("source_item_ids",[])]
        relations=so.get("relations",[])+[g.get("relation",g.get("mapping_relation","")) for g in groups if g]
        status=("G2-6A C239 source hardware reviewed; original ANSI/VITA/DSDM and figure geometry held; no DIM/Profile adoption" if groups[-1] else
            "G2-5 C239 Chapter12 original inline source reviewed; original security/DIV companions held" if groups[-2] else
            "Earlier source-limited C239 original review, native companions held" if so or any(groups[:-2]) else "Not assessed here")
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),
             r.get("master_inclusion",""),r.get("dim_adoption",""),"; ".join(r.get("source_entry_ids",[])),
             json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
             "; ".join(ids),"; ".join(relations),status])
    return out

def publish():
    m=load(MASTER);l=load(LEDGER);check_source(m,l)
    prev=(D/BOOK).read_bytes()
    need(digest(prev)==OLD,"same verified prior G2-5 26-sheet workbook bytes")
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
    need(len(delta)==39 and all(re.fullmatch(r"I\d+",a) for a in delta),
         "exactly 39 source-qualified SOSA column-I cells changed; no other master edits")
    (D/BOOK).write_bytes(saved)
    sha=digest(saved)
    m["currentWorkbookSha256"]=sha
    m["currentEvidenceCheckpoint"]="SOSA-G2-6A_ORIGINAL_HARDWARE_SOURCE_AND_SAVED_26_SHEET_EXCEL_SOURCE_PARITY_VERIFIED__DONOR_OPEN"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-6A-CANONICAL-VERIFIED","sha256":sha,
        "currently_matches_readable_view":True,
        "lag":"NONE: all 346x15 actual saved XLSX cells match current source JSON, BOTH CSV and BOTH Markdown tables",
        "refreshed_cell_count":39,"validation_file":REPORT})
    m["SOSAEvidence"]["G2_6A"].update({"excel_checkpoint":"SOSA-G2-6A-CANONICAL-VERIFIED",
        "excel_validation":REPORT,"excel_lag_cells":0,"same_saved_workbook_39_cells_synced":True})
    m["SOSAReviewCompletion"]["G2_6A_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["status"]="OPEN__G2_6A_VERIFIED__42_UNREAD_1_RESTRICTED_AND_NATIVE_COMPANIONS"
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="SOSA-G2-6B original C239 §13.2.11 onward bounded hardware source only; no entire Chapter13 or next donor"
    m["nextOwnerAction"]="On separate owner Proceed: SOSA-G2-6B from C239 §13.2.11 only, source-first evidence-sized hardware PICP packet. SOSA remains OPEN and Step18 SAPIENT BLOCKED."
    m["publicationPolicy"]="L23 applied G2-6A: 39 source-qualified SOSA column-I cells current in canonical JSON, 2 CSV, 2 readable tables and SAME saved 26-sheet Excel, all 346x15 saved cells verified; donor completeness and adoption distinct."
    save(MASTER,m)
    record={"date":"2026-11-10","step":"SOSA-G2-6A-EXCEL-CHECKPOINT",
       "result":"EXACT_SAVED_26_SHEET_XLSX_AND_TWO_CSV_TWO_MD_PARITY_PASS",
       "workbook_sha256":sha,"base_workbook_sha256":OLD,"workbook_sheets":list(paths),
       "refreshed_sheets":list(tables),"exact_original_untouched_xml_sha256":retained,
       "information_rows":329,"grid_rows":346,"columns":15,"original_donor_evidence":58,"case_evidence":73,
       "ISA_primary_source_outcomes":480,"original_ISA_questions_open":6,
       "G2_6A_original_toc_headings":13,"G2_6A_nested_subclauses":19,
       "G2_6A_original_native_source_items":156,"G2_6A_analytical_context_records":12,
       "G2_6A_native_rule_shalls":98,"G2_6A_native_permissions":8,
       "G2_6A_native_recommendations":3,"G2_6A_native_observations":21,
       "G2_6A_qualified_existing_sosa_cells":39,"changed_saved_cells":sorted(delta),
       "unread_original_C239_TOC_headings":42,"restricted_original_C239_TOC_headings":1,
       "native_DSDM_IDL_OpenAPI_unread":8,"original_ANSI_VITA_unread":True,
       "checks":{"all_XLSX_346x15_grid_cells_equal_JSON_both_CSVs_both_MD":True,
        "two_CSV_mirrors_equal":True,"two_GitHub_readable_comparisons_equal":True,
        "same_26_worksheet_names_order":True,"22_historical_worksheet_XML_bytes_preserved":True,
        "only_39_original_SOSA_I_column_cells_changed":True,"valid_ZIP_CRC_and_XML":True,
        "zero_XLSX_error_type_cells":True,"zero_DIM_Profile_adoption":True},
       "limits":["Only original C239 §§13.1–13.2.10 inline text/tables read; §13.2.11+ not assessed",
           "Eight original SOSA DSDM/IDL/OpenAPI and ANSI/VITA native original specs uninspected",
           "Exact original figure pixel/arrow/dimension geometry unverified",
           "No case-vendor original Certificate of Volatility examined",
           "No installed hardware, live command, DIM/Profile adoption or independent conformance test",
           "PNG preview is saved XLSX XML/source-cell rendering, not Microsoft Excel application screenshot"],
       "next":"Only separate owner Proceed starts G2-6B original §13.2.11 source-sized hardware packet; SOSA OPEN, SAPIENT blocked"}
    save(REPORT,record)
    print("PASS: SAME saved 26-sheet Excel 346x15 JSON/2CSV/2MD parity; 22 untouched sheets; SHA256",sha)
    return sha

def preview():
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER);actual=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_6A_source_correspondence")]
    need(len(rows)==39,"39 original G2-6A comparisons in saved workbook")
    try:
        font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:font=bold=ImageFont.load_default()
    width,height=1580,3970
    img=Image.new("RGB",(width,height),"white");pen=ImageDraw.Draw(img)
    pen.rectangle((0,0,width,65),fill="#173855")
    pen.text((18,17),"SOSA-G2-6A: 39 actual saved Excel hardware source cells — original C239 §§13.1–13.2.10",font=bold,fill="white")
    for i,r in enumerate(rows):
        hit=[k+1 for k,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(hit)==1,"unique current source row "+r["row_id"])
        a="I"+str(hit[0]);v=actual.get(a,"")
        need(v==r["display"][8],"actual saved workbook cell "+a)
        y=72+i*98;pen.rectangle((10,y,width-12,y+91),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        pen.text((20,y+7),r["row_id"]+" | "+a+" | "+r["label"],font=bold,fill="#173855")
        snippet="G2-6A: "+v.split("G2-6A:",1)[1] if "G2-6A:" in v else v
        for j,line in enumerate(textwrap.wrap(snippet,width=165,break_long_words=False)[:3]):
            pen.text((20,y+33+j*17),line,font=font,fill="#203951")
    img.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>15000,"valid saved XLSX source-cell preview")
    print("PASS: 39 saved canonical SOSA source cell preview from actual Excel XML; not native Excel screenshot")
if __name__=="__main__":
    publish()
    preview()
