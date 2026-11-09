#!/usr/bin/env python3
"""SOSA-D canonical XLSX publisher; preserves all 26 original tabs and source holds.
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
REPORT="Step17_SOSA_D_Workbook_Validation_09NOV2026.json"
PREVIEW="Step17_SOSA_D_Workbook_Preview_09NOV2026.png"
OLD="4b4874c036d90359ab3dd6ee00a7ea0dd14b14e2eb208761da948dce52fdf44b"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-D verification failed: "+message
def load(n):return json.loads((D/n).read_text(encoding="utf-8"))
def save(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def digest(b):return hashlib.sha256(b).hexdigest()
def source_csv(n):
    with (D/n).open(encoding="utf-8-sig",newline="") as f:return list(csv.reader(f))
def addr(i,j):return old.coord(i,j)
def check_source(m,l):
    need(m["schemaVersion"]=="0.11" and len(m["rows"])==329,"master schema and rows")
    need(len(m["columns"])==15 and [v["key"] for v in m["columns"]][8:10]==["OpenGroupSOSA","SOSA"] and m["columns"][-1]["key"]=="DIM","separate Open Group vs W3C and rightmost DIM")
    need([v["key"] for v in m["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"],"four source cases leftmost")
    g=m["review_grid"];sec=set(m["review_sections"])
    need(len(g)==346 and len(sec)==15 and all(len(r)==15 for r in g),"346x15 grid and section headings")
    need([r for i,r in enumerate(g) if i>1 and i not in sec]==[r["display"] for r in m["rows"]],"canonical row-display parity")
    need(g==source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")==source_csv("ISA_Correction_Review_07NOV2026.csv"),"CSV exact mirrors")
    a=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    b=(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    need(a.split("<table>",1)[1]==b.split("<table>",1)[1] and a.count('colspan="15"')==15,"Markdown/HTML comparison tables")
    need(len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73,"all historic donor/case evidence")
    need(m["ISAEvidence"]["currentPrimaryReviews"]==480 and m["ISAEvidence"]["specificQuestions"]==6,"480/6 original ISA evidence")
    need(len(l["all_57_qualified_source_decisions"])==57 and len(l["integration_row_ledger"])==38 and l["source_native_records"]==76,"SOSA 57/38/76 evidence")
    mapp={r["row_id"]:r["display_cell"] for r in l["integration_row_ledger"]}
    for r in m["rows"]:
        need(r["display"][8]==mapp.get(r["row_id"],"Not assessed here"),"source-first SOSA mapping at "+r["row_id"])
    need(l["native_DSDM_IDL_OpenAPI_eight_files_uninspected"] and l["non_adoption"],"native files and adoption boundary")
    print("PASS: 329 rows, 346×15 grid, both CSV and Markdown bodies, 57 SOSA source decisions / 38 cells")
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
        ["SOSA-D CURRENT CANONICAL WORKBOOK","Source-qualified with native file holds"],
        ["Information rows","329 / 346 presentation rows / 15 columns"],
        ["Column meaning","The Open Group SOSA C239 distinct from W3C SOSA/SSN"],
        ["The Open Group C239 original terms","76 source-checked conceptual terms or pointers (A/B/C)"],
        ["Source comparisons","57 bounded relation decisions across 38 existing rows"],
        ["Native source gap","DSDM, IDL and six SysMan OpenAPI files (eight exact native files NOT READ)"],
        ["Original evidence","58 previous donor mappings, 73 equipment case facts preserved"],
        ["ISA","480 original source outcomes and six unresolved exact interpretation questions"],
        ["Semantic boundary","Source relation does not adopt any DIM element or CSAPI Profile obligation"],
        ["Validity","Exact JSON/CSV/Markdown and saved XLSX cell, ZIP, XML, source-row parity"],
        ["Next on new Proceed","Original 40-step cross-donor Step18 SAPIENT v2; no automatic work"]
    ]
def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),r.get("master_inclusion",""),r.get("dim_adoption",""),
           "; ".join(r.get("source_entry_ids",[])),json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
           "; ".join(so.get("records",[])),"; ".join(so.get("relations",[])),
           "C239 narrative checked; native DSDM/API not read" if so else "Not assessed here"])
    return out
def publish():
    m=load(MASTER);l=load(LEDGER);check_source(m,l)
    prev=(D/BOOK).read_bytes()
    need(digest(prev)==OLD,"original 26-tab workbook hash exact")
    with zipfile.ZipFile(io.BytesIO(prev)) as z:
        need(z.testzip() is None,"old ZIP CRC")
        paths=old.sheetpaths(z);need(len(paths)==26,"26 original named tabs")
        styles,style=old.newstyles(z.read("xl/styles.xml"))
        tables={"Master Crosswalk":m["review_grid"],"DIM Register":register(m),"Summary":summary(m),"Validation":summary(m)}
        need(set(tables)<=set(paths),"live tabs exist")
        replacement={"xl/styles.xml":styles}
        for n,rows in tables.items():replacement[paths[n]]=matrix_to_xml(rows,style,main=n=="Master Crosswalk",sections=m["review_sections"] if n=="Master Crosswalk" else ())
        unchanged={n:digest(z.read(p)) for n,p in paths.items() if n not in tables}
        dst=io.BytesIO()
        with zipfile.ZipFile(dst,"w") as out:
            for info in z.infolist():out.writestr(info,replacement.get(info.filename,z.read(info.filename)))
    new=dst.getvalue()
    with zipfile.ZipFile(io.BytesIO(new)) as z:
        need(z.testzip() is None and list(old.sheetpaths(z))==list(paths),"new ZIP CRC and 26-tab order")
        for n,s in unchanged.items():need(digest(z.read(paths[n]))==s,"preserve untouched tab "+n)
        for p in z.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(z.read(p))
            if p.startswith("xl/worksheets/") and p.endswith(".xml"):
                need(not any(c.get("t")=="e" for c in ET.fromstring(z.read(p)).iter(q("c"))),"no Excel error type at "+p)
        master=ET.fromstring(z.read(paths["Master Crosswalk"]))
        actual_merges=[x.get("ref") for x in master.find(q("mergeCells")).findall(q("mergeCell"))]
        need(actual_merges==["A1:D1","E1:I1","J1:N1"]+[f"A{i+1}:O{i+1}" for i in m["review_sections"]],"group and section merges")
        pane=master.find(q("sheetViews")).find(q("sheetView")).find(q("pane"))
        need(pane.get("xSplit")=="4" and pane.get("ySplit")=="2","freeze panes")
    cells=old.readcells(new,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for j,value in enumerate(row,1):need(cells.get(addr(i,j),"")==old.val(value),"actual XLSX cell "+addr(i,j))
    reg=old.readcells(new,"DIM Register")
    need(sum(bool(re.fullmatch(r"A\d+",s)) for s in reg)==330,"register retains 329 source row IDs")
    (D/BOOK).write_bytes(new)
    digest_new=digest(new)
    m["currentWorkbookSha256"]=digest_new
    m["currentEvidenceCheckpoint"]="SOSA-D-CANONICAL-SOURCE-AND-WORKBOOK-PARITY-VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-D-CANONICAL-VERIFIED","sha256":digest_new,"information_rows":329,"columns":15,"currently_matches_readable_view":True,"lag":"NONE: 346x15 exact source/CSV/Markdown/XLSX parity; 26 original tabs preserved"})
    m["nextOwnerAction"]="SOSA-D complete with source holds. Original Step18 SAPIENT v2 only on a new owner Proceed"
    save(MASTER,m)
    l.update({"workbook_rebuild_status":"BINARY_WRITTEN_AND_SOURCE_CELL_VERIFIED","workbook_sha256":digest_new,"original_26_sheets":list(paths),"preserved_historical_xml_tab_hashes":unchanged,"next":"SOSA-D complete, original Step18 only on new owner Proceed"})
    save(LEDGER,l)
    record={"date":"2026-11-09","step":"17/SOSA-D","result":"SOURCE_AND_WORKBOOK_PARITY_PASS_WITH_NATIVE_SOURCE_HOLDS",
            "workbook_sha256":digest_new,"base_workbook_sha256":OLD,"workbook_sheets":list(paths),
            "refreshed_sheets":list(tables),"exact_original_untouched_xml_sha256":unchanged,
            "source_rows":329,"grid_rows":346,"columns":15,"original_donor_evidence":58,"case_evidence":73,
            "SOSA_source_concepts":76,"qualified_or_held_source_decisions":57,"SOSA_populated_review_cells":38,
            "unread_native_DSDM_IDL_OpenAPI_files":8,"open_ISA_original_questions":6,
            "tests":{"all_XLSX_grid_cells_exact":True,"CSV_and_Markdown_same":True,"26_original_tab_names_order_preserved":True,
              "22_untouched_worksheet_XML_bytes_preserved":True,"XML_and_ZIP_CRC_ok":True,"no_XLSX_error_type_cells":True,
              "DIM_new_content_adopted":False},
            "not_performed":["native C239 DSDM or management OpenAPI source inspection","full 403-page source audit",
              "Excel-native rendering","runtime SOSA/OGC conformance","physical hardware integration"],
            "next":"original Step18 SAPIENT v2 only on new user Proceed"}
    save(REPORT,record)
    print("PASS: canonical workbook all 5190 source cells equal, 26 tabs retained; new SHA256",digest_new)
    return digest_new
def preview():
    from PIL import Image,ImageDraw,ImageFont
    c=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    try:
        f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        fb=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:f=fb=ImageFont.load_default()
    widths=[190,195,220,210,185,190,190,235,340,205,205,205,220,220,250]
    im=Image.new("RGB",(sum(widths)+24,950),"white");p=ImageDraw.Draw(im)
    p.text((12,10),"SOSA-D · source-backed saved workbook A1:O12",font=fb,fill="#173855")
    y=45
    for i in range(1,13):
        h=36 if i==1 else 65 if i in (2,3,9) else 74
        x=12
        for j,w in enumerate(widths,1):
            bg="#173855" if i==1 else "#C5DCEC" if i==2 else "#DDEAF3" if i in (3,9) else "#F4F8FC" if i%2==0 else "white"
            p.rectangle((x,y,x+w,y+h),fill=bg,outline="#BDCDD9")
            v=c.get(addr(i,j),"")
            if v and (i not in (3,9) or j==1):
                for k,line in enumerate(textwrap.wrap(v,max(15,(w-14)//8),break_long_words=False)[:3]):
                    p.text((x+5,y+6+k*17),line,font=fb if i in (1,2,3,9) else f,fill="white" if i==1 else "#203951")
            x+=w
        y+=h
    im.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>15000,"source-cell visual render")
    print("PASS: actual saved-XLSX cell preview created (not native Excel)")
if __name__=="__main__":
    publish()
    preview()
