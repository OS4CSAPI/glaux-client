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
REPORT="SOSA_G2_1_Workbook_Validation_09NOV2026.json"
PREVIEW="SOSA_G2_1_Workbook_Preview_09NOV2026.png"
OLD="531451e4b43b0502e9e90b62972a7398be048ceb3987eb24ef4963e3f0fb1fba"
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
    need(m["schemaVersion"]=="0.12" and len(m["rows"])==329,"G2-1 canonical master schema and 329 source rows")
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
    prior={r["row_id"]:r["display_cell"] for r in l["integration_row_ledger"]}
    inv=load("SOSA_G2_1_Original_Item_Inventory_09NOV2026.json")
    ids={x["id"] for x in inv["items"]}
    need(len(inv["items"])==201 and len(ids)==201,"201 original source/native item IDs")
    need(sum(x["kind"]=="RULE" for x in inv["items"])==6,"six C239 original Rules")
    changed=[]
    for r in m["rows"]:
        before=prior.get(r["row_id"],"Not assessed here")
        after=r["display"][8]
        add=r.get("G2_1_source_correspondence")
        if add:
            need(add["relation"] in ("PARTIAL","RELATED") and add["DIM_adopted"] is False,"qualified G2-1 correspondence")
            need(add["source_item_ids"] and all(z in ids for z in add["source_item_ids"]),"G2-1 original source-item references")
            need(after!=before and (after.startswith(before+" · ") if before!="Not assessed here" else after.startswith("Related only · ")),"preserve prior SOSA-D value in G2-1 cell")
            changed.append(r["row_id"])
        else:
            need(after==before,"untouched SOSA source cell "+r["row_id"])
    need(len(changed)==12 and set(changed)==set(m["workbookSnapshot"]["G2_1_affected_row_ids"]),"exact 12 justified G2-1 existing donor cells")
    need(not m["workbookSnapshot"]["currently_matches_readable_view"],"G2-1 has declared 12-cell lag before this authorized refresh")
    need(l["native_DSDM_IDL_OpenAPI_eight_files_uninspected"] and l["non_adoption"],"native files and adoption boundary")
    print("PASS: current 329×15 JSON, both CSVs/Markdown bodies, 201 G2-1 native items, exactly 12 SOSA-only source-qualified deltas")
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
        ["SOSA-G2-1 CANONICAL EXCEL CHECKPOINT","Source-qualified original C239 inline review; donor still OPEN"],
        ["Master comparison","329 information rows / 346 presentation rows / 15 columns"],
        ["Original G2-1 source evidence","201 original items = 124 functions, 71 interactions, six Rules"],
        ["Edition support","129 V1.0 and 66 Future source table entries (not runtime capabilities)"],
        ["New current SOSA comparisons","12 existing donor cells refreshed and verified from saved XLSX"],
        ["Previously retained SOSA-D","76 selected native records / 57 decisions / 38 source-qualified rows"],
        ["Source limitation","Original native DSDM, IDL and six OpenAPI files unread; C239 donor still open"],
        ["Historical evidence","58 other donor records, 73 four-equipment-case source facts retained"],
        ["ISA source holdings","480 DMS outcomes with six exact unresolved questions retained"],
        ["DIM adoption","No new classes, fields, cardinalities or CSAPI Profile SHALL obligations"],
        ["Formats and saved workbook","JSON, both CSVs, both readable comparisons, actual 26-sheet XLSX cells equal"],
        ["Next only on owner Proceed","SOSA-G2-2 original C239 §§6.2.6–6.2.9; SAPIENT Step18 blocked"]
    ]
def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        g2=r.get("G2_1_source_correspondence") or {}
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),r.get("master_inclusion",""),r.get("dim_adoption",""),
           "; ".join(r.get("source_entry_ids",[])),json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
           "; ".join(so.get("records",[])+g2.get("source_item_ids",[])),"; ".join(so.get("relations",[])+([g2["relation"]] if g2 else [])),
           "G2-1 C239 inline original source reviewed; native DSDM/API not read" if g2 else "C239 selected source reviewed; native DSDM/API not read" if so else "Not assessed here"])
    return out
def publish():
    m=load(MASTER);l=load(LEDGER);check_source(m,l)
    prev=(D/BOOK).read_bytes()
    need(digest(prev)==OLD,"existing 26-tab SOSA-D snapshot hash exact; never replace canonical workbook")
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
    # Independently check that exactly 12 SOSA column values changed in the SAVED existing workbook.
    oldcells=old.readcells(prev,"Master Crosswalk")
    newcells=old.readcells(new,"Master Crosswalk")
    delta=[a for a in set(oldcells)|set(newcells) if oldcells.get(a,"")!=newcells.get(a,"")]
    need(len(delta)==12 and all(re.fullmatch(r"I\d+",a) for a in delta),"only 12 verified original SOSA I-column saved cells changed")
    m["currentWorkbookSha256"]=digest_new
    m["currentEvidenceCheckpoint"]="SOSA-G2-1-SAVED_26_SHEET_EXCEL_PARITY_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-1-CANONICAL-VERIFIED","sha256":digest_new,
        "information_rows":329,"columns":15,"currently_matches_readable_view":True,
        "lag":"NONE — all 346×15 current JSON/CSV/Markdown/XLSX cells agree and 26 original sheets are preserved",
        "refreshed_cell_count":12,"validation_file":REPORT})
    m["SOSAEvidence"]["G2_1"].update({"excel_checkpoint":"SOSA-G2-1-CANONICAL-VERIFIED",
        "excel_validation":REPORT,"excel_12_source_cells_synced":True})
    m["publicationPolicy"]="Binding L23: every substantive source-qualified donor packet with meaningful master cell changes must refresh and verify the SAME canonical XLSX before the next research packet; any deferred checkpoint requires an owner-approved precise exception, explicit stale snapshot and stopping point. SOSA-G2-1 12 source-qualified cells fully synchronized. Source audit completeness, DIM/Profile adoption and runtime conformance remain separate."
    m["nextOwnerAction"]="SOSA-G2-2 only on new owner Proceed: source-first C239 §§6.2.6–6.2.9 Security Services, Chassis Manager, PIC and PIC with software RTE; Step18 SAPIENT blocked until SOSA owner closure."
    save(MASTER,m)
    # Do not rewrite the historical SOSA-D source ledger or SOSA-D workbook validation.
    record={"date":"2026-11-09","step":"SOSA-G2-1-EXCEL-CHECKPOINT","result":"SAVED_26_SHEET_XLSX_AND_ALL_CURRENT_TEXT_FORMATS_PARITY_PASS",
        "workbook_sha256":digest_new,"base_workbook_sha256":OLD,
        "workbook_sheets":list(paths),"refreshed_sheets":list(tables),
        "exact_original_untouched_xml_sha256":unchanged,
        "source_rows":329,"grid_rows":346,"columns":15,
        "original_donor_evidence":58,"case_evidence":73,
        "source_item_count":201,"rule_count":6,"G2_1_source_qualified_updated_cells":12,
        "changed_saved_cells":sorted(delta),
        "native_DSDM_IDL_OpenAPI_unread":8,"ISA_original_questions_open":6,
        "tests":{"all_XLSX_grid_cells_exact":True,"both_CSVs_and_readable_tables_equal":True,
            "same_26_sheet_names_order":True,"untouched_22_worksheet_XML_bytes_preserved":True,
            "saved_12_SOSA_column_cells_only_changed":True,"XLSX_ZIP_CRC_and_XML_valid":True,
            "no_XLSX_error_type_cells":True,"DIM_or_Profile_adopted":False},
        "not_performed":["native C239 DSDM/IDL/OpenAPI review","comprehensive C239 donor completion",
            "Excel application-native rendering","runtime conformance or hardware command"],
        "next":"SOSA-G2-2 original C239 §§6.2.6–6.2.9 only on owner Proceed"}
    save(REPORT,record)
    print("PASS: canonical workbook all 5190 source cells equal, 26 tabs retained; new SHA256",digest_new)
    return digest_new
def preview():
    # Render the 12 newly synchronized source cells from the SAVED workbook, not a JSON mockup.
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER)
    cells=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_1_source_correspondence")]
    need(len(rows)==12,"twelve G2-1 visual evidence rows")
    try:
        f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",12)
        fb=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",14)
    except OSError:
        f=fb=ImageFont.load_default()
    width,height=1600,1250
    im=Image.new("RGB",(width,height),"white")
    p=ImageDraw.Draw(im)
    p.rectangle((0,0,width,62),fill="#173855")
    p.text((20,16),"SOSA-G2-1 | twelve source-qualified cells in the SAVED 26-sheet Excel",font=fb,fill="white")
    for i,r in enumerate(rows):
        gridrows=[n+1 for n,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(gridrows)==1,"exact visual source row "+r["row_id"])
        excelcell="I"+str(gridrows[0])
        observed=cells.get(excelcell,"")
        need(observed==r["display"][8],"actual Excel cell verified before preview "+excelcell)
        top=70+i*96
        p.rectangle((12,top,width-12,top+88),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        p.text((22,top+9),r["row_id"]+" · "+excelcell+" · "+r["label"],font=fb,fill="#173855")
        brief=textwrap.wrap(observed,width=180,break_long_words=False)
        for z,line in enumerate(brief[:3]):
            p.text((22,top+33+z*17),line,font=f,fill="#203951")
    im.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>15000,"actual saved XLSX source-cell visual inspection artifact")
    print("PASS: saved XLSX G2-1 12-cell preview created; not native Excel rendering")

if __name__=="__main__":
    publish()
    preview()
