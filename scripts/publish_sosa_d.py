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
REPORT="SOSA_G2_4A_Workbook_Validation_10NOV2026.json"
PREVIEW="SOSA_G2_4A_Workbook_Preview_10NOV2026.png"
OLD="8dab9447dd00ede955a1cdc36d48493d54726bf0d40c9b409b0da47801381750"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-G2-4A verification failed: "+message
def load(n):return json.loads((D/n).read_text(encoding="utf-8"))
def save(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def digest(b):return hashlib.sha256(b).hexdigest()
def source_csv(n):
    with (D/n).open(encoding="utf-8-sig",newline="") as f:return list(csv.reader(f))
def addr(i,j):return old.coord(i,j)
def check_source(m,l):
    need(m["schemaVersion"]=="0.15" and len(m["rows"])==329,"G2-4A live canonical source schema and rows")
    need(len(m["columns"])==15 and [x["key"] for x in m["columns"]][8:10]==["OpenGroupSOSA","SOSA"] and m["columns"][-1]["key"]=="DIM","distinct The Open Group vs W3C SOSA, proposed DIM right")
    need([x["key"] for x in m["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"],"case columns intact")
    grid=m["review_grid"]
    need(len(grid)==346 and all(len(x)==15 for x in grid) and len(m["review_sections"])==15,"346x15 original row/section presentation")
    need([r for i,r in enumerate(grid) if i>1 and i not in set(m["review_sections"])]==[r["display"] for r in m["rows"]],"row and reviewed source grid exact")
    need(grid==source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")==source_csv("ISA_Correction_Review_07NOV2026.csv"),"BOTH CSV mirrors equal source")
    a=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    b=(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    need(a.split("<table>",1)[1]==b.split("<table>",1)[1] and a.count('colspan="15"')==15,"BOTH readable horizontal comparisons equal source")
    need(len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73 and m["ISAEvidence"]["currentPrimaryReviews"]==480 and m["ISAEvidence"]["specificQuestions"]==6,"58 donor/73 case/ISA480 original evidence preserved")
    need(len(l["all_57_qualified_source_decisions"])==57 and len(l["integration_row_ledger"])==38,"existing SOSA-D coverage retained")
    g1=load("SOSA_G2_1_Original_Item_Inventory_09NOV2026.json")
    g2=load("SOSA_G2_2_Original_Item_Inventory_09NOV2026.json")
    g3=load("SOSA_G2_3_Original_Source_Item_Census_09NOV2026.json")
    g4=load("SOSA_G2_4A_Original_Source_Item_Coverage_10NOV2026.json")
    need(len(g1["items"])==201 and len(g2["source_items"])+len(g2["original_rule_appearances"])==352 and g3["counts"]["source_items"]==119,"all prior C239 research retained")
    need(len(g4["chapter1_5_toc_coverage"])==42 and len(g4["chapter7_11_pending"])==27 and len(g4["original_source_items"])==95,"42 text-audited original headings, 27 exact pending, 95 source-native items")
    need(g4["item_counts"]["QUALITY_ATTRIBUTE"]==10 and g4["item_counts"]["ARCHITECTURE_PRINCIPLE"]==15 and g4["item_counts"]["MODULE_CATALOG"]==27,"original chapter 3/4 exhaustive native inventory")
    need(g4["item_counts"]["previously_G1_UNREAD_1_5"]==27 and g4["item_counts"]["previously_G1_sampled_1_5"]==15,"source coverage grades, no claim native companion complete")
    ids={x["id"] for x in g4["original_source_items"]}
    need(len(ids)==95 and not g4["source"]["native_DSDM_IDL_OpenAPI_externally_referenced_files_read"],"valid original source IDs with native schema hold")
    need(sum(bool(r.get("G2_1_source_correspondence")) for r in m["rows"])==12
        and sum(bool(r.get("G2_2_source_correspondence")) for r in m["rows"])==22
        and sum(bool(r.get("G2_3_source_correspondence")) for r in m["rows"])==28,"prior cumulative SOSA source meanings retained")
    updated=[r for r in m["rows"] if r.get("G2_4A_source_correspondence")]
    need(len(updated)==20 and {r["row_id"] for r in updated}==set(m["workbookSnapshot"]["G2_4A_affected_row_ids"]),"only 20 target source rows qualified")
    for r in updated:
        ev=r["G2_4A_source_correspondence"]
        need(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]),"verified native source item references "+r["row_id"])
        need(ev["DIM_adopted"] is False and ev["unverified_native_companions"] is True,"explicit nonadoption and schema hold "+r["row_id"])
        need("G2-4A:" in r["display"][8] and ev["previous_sosa_cell_value"]!=r["display"][8],"previous source wording preserved "+r["row_id"])
    need(m["currentWorkbookSha256"]==OLD and not m["workbookSnapshot"]["currently_matches_readable_view"],"verified G2-3 baseline, same-packet 20-cell Excel gate")
    need(l["native_DSDM_IDL_OpenAPI_eight_files_uninspected"] and l["non_adoption"],"existing eight-native-source hold and DIM nonadoption")
    print("PASS: G2-4A original C239 Chapters1-5 42 heading audit, 95 native items, 20 qualified existing SOSA cells, both CSVs/Markdown, ISA/cases preserved")
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
       ["SOSA-G2-4A source-first Excel checkpoint","C239 Chapters 1–5 original inline source; donor remains OPEN"],
       ["Canonical comparison","329 information rows, 346 visual grid rows, 15 columns"],
       ["Original source inventory","42 C239 Chapter1–5 headings and 95 native concepts/definitions/examples"],
       ["Quality and architecture drivers","10 quality attributes; 15 principles, not Profile SHALLs"],
       ["SOSA module catalogue","27 numbered entries, of which 3 Reserved; not all deployed in any sensor"],
       ["Native physical and logical scopes","SOSA sensor, hardware element, host/pod, module, software RTE, interconnect, procurable unit"],
       ["Source-qualified comparisons","20 existing The Open Group SOSA column I cells changed; every other source cell retained"],
       ["Source limitations","Actual figures pixels, RIG and DSDM/IDL/OpenAPI companion files not fully inspected"],
       ["Pending original source headings","C239 Chapters7–11, 27 TOC headings, to be source-audited in G2-4B only"],
       ["Previous SOSA evidence","SOSA-D 76 selected, G2-1 201, G2-2 352, G2-3 119 items preserved"],
       ["Original case/donor/ISA evidence","58 donor records, 73 equipment cases, 480 ISA outcomes/six questions preserved"],
       ["No adoption","No DIM hierarchy, classes, cardinality, CSAPI SHALL or deployed hardware control adopted"],
       ["Saved file parity","Exact JSON/both CSVs/both readable master views/26-sheet Excel at 346x15"],
       ["Next only on owner Proceed","G2-4B Chapters7–11; SOSA donor OPEN, SAPIENT BLOCKED"]
    ]
def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        g2=r.get("G2_1_source_correspondence") or {}
        g22=r.get("G2_2_source_correspondence") or {}
        g23=r.get("G2_3_source_correspondence") or {}
        g24=r.get("G2_4A_source_correspondence") or {}
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),r.get("master_inclusion",""),r.get("dim_adoption",""),
           "; ".join(r.get("source_entry_ids",[])),json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
           "; ".join(so.get("records",[])+g2.get("source_item_ids",[])+g22.get("source_item_ids",[])+g23.get("source_item_ids",[])+g24.get("source_item_ids",[])),"; ".join(so.get("relations",[])+([g2["relation"]] if g2 else [])+([g22["mapping_relation"]] if g22 else [])+([g23["relation"]] if g23 else [])+([g24["relation"]] if g24 else [])),
           "G2-4A C239 architecture/taxonomy source inline reviewed; source diagrams/native DSDM/API remain incomplete" if g24 else "G2-3 C239 hardware/state source inline reviewed; native VITA/HOST/IPMI/DSDM/API dependencies not read" if g23 else "G2-2 C239 specialized source inline reviewed; native DSDM/API not read" if g22 else "G2-1 C239 inline original source reviewed; native DSDM/API not read" if g2 else "C239 selected source reviewed; native DSDM/API not read" if so else "Not assessed here"])
    return out
def publish():
    m=load(MASTER);l=load(LEDGER);check_source(m,l)
    prev=(D/BOOK).read_bytes()
    need(digest(prev)==OLD,"same verified 26-sheet G2-3 canonical workbook binary hash; do not replace")
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
    # Verify EXACTLY 22 donor-column-I changed values and zero changes elsewhere.
    oldcells=old.readcells(prev,"Master Crosswalk")
    newcells=old.readcells(new,"Master Crosswalk")
    delta=[a for a in set(oldcells)|set(newcells) if oldcells.get(a,"")!=newcells.get(a,"")]
    need(len(delta)==20 and all(re.fullmatch(r"I\d+",a) for a in delta),"only 20 The Open Group SOSA column I saved cells changed, no other source cell")
    m["currentWorkbookSha256"]=digest_new
    m["currentEvidenceCheckpoint"]="SOSA-G2-4A-SAVED_26_SHEET_XLSX_AND_SOURCE_PARITY_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-4A-CANONICAL-VERIFIED","sha256":digest_new,
        "information_rows":329,"columns":15,"currently_matches_readable_view":True,
        "lag":"NONE: all 346x15 saved XLSX cells agree with current JSON, BOTH CSVs and BOTH readable tables",
        "refreshed_cell_count":20,"G2_4A_affected_row_ids":m["workbookSnapshot"]["G2_4A_affected_row_ids"],
        "validation_file":REPORT})
    m["SOSAEvidence"]["G2_4A"].update({"excel_checkpoint":"SOSA-G2-4A-CANONICAL-VERIFIED",
        "excel_validation":REPORT,"excel_20_source_cells_synced":True})
    m["SOSAReviewCompletion"]["G2_4A_workbook_lagged_cells"]=0
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="SOSA-G2-4B original C239 Chapters7–11 source-first review only"
    m["publicationPolicy"]="Binding L23: Each substantive source-qualified donor packet changing canonical comparison cells must update JSON, both CSVs, both readable comparisons and verified SAME 26-sheet Excel before next research. G2-4A 20 SOSA cells synced, no owner DIM/Profile adoption."
    m["nextOwnerAction"]="SOSA-G2-4B only on separate owner Proceed: source-first C239 Chapters7–11 (Tasking, RF/EO-IR, signal/target processing, exploit, convey); still The Open Group SOSA donor open; SAPIENT blocked until donor closure."
    save(MASTER,m)
    record={"date":"2026-11-10","step":"SOSA-G2-4A-EXCEL-CHECKPOINT","result":"EXACT_SAVED_26_SHEET_XLSX_AND_TWO_CSV_TWO_MD_PARITY_PASS",
       "workbook_sha256":digest_new,"base_workbook_sha256":OLD,
       "workbook_sheets":list(paths),"refreshed_sheets":list(tables),
       "exact_original_untouched_xml_sha256":unchanged,
       "information_rows":329,"grid_rows":346,"columns":15,
       "original_donor_evidence":58,"case_evidence":73,"ISA_primary_source_outcomes":480,
       "G2_4A_original_inline_source_headings":42,"G2_4A_original_source_items":95,
       "G2_4A_qualified_existing_source_cells":20,"changed_saved_cells":sorted(delta),
       "G2_4B_C239_7_11_pending_headings":27,
       "native_DSDM_IDL_OpenAPI_unread":8,"original_ISA_source_questions_open":6,
       "checks":{"all_XLSX_346x15_grid_cells_equal_JSON_both_CSVs_both_MD":True,
          "two_CSV_mirrors_equal":True,"two_GitHub_readable_comparisons_equal":True,
          "same_26_worksheet_names_order":True,"22_historical_worksheet_XML_bytes_preserved":True,
          "only_20_original_SOSA_I_column_cells_changed":True,
          "valid_ZIP_CRC_and_XML":True,"zero_XLSX_error_type_cells":True,"zero_DIM_Profile_adoption":True},
       "limits":["No original SOSA RIG/conformance policy/DSDM/IDL/OpenAPI files inspected",
          "No source-figure pixel/arrow geometry independently verified",
          "Original C239 Chapters7–11 not audited this packet",
          "No comprehensive The Open Group SOSA donor coverage claim",
          "No actual hardware device runtime/command conformance",
          "Saved-cell PNG preview is not an Excel application screenshot"],
       "next":"SOSA-G2-4B original C239 Chapters7–11 only on separate owner Proceed"}
    save(REPORT,record)
    print("PASS: canonical workbook all 5190 source cells equal, 26 tabs retained; new SHA256",digest_new)
    return digest_new
def preview():
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER)
    source=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_4A_source_correspondence")]
    need(len(rows)==20,"twenty source-qualified master rows for saved preview")
    try:
        f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        fb=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:f=fb=ImageFont.load_default()
    width,height=1560,2080
    img=Image.new("RGB",(width,height),"white")
    pen=ImageDraw.Draw(img)
    pen.rectangle((0,0,width,65),fill="#173855")
    pen.text((18,17),"SOSA-G2-4A: 20 actual saved canonical Excel donor cells",font=fb,fill="white")
    for i,r in enumerate(rows):
        hit=[k+1 for k,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(hit)==1,"one source row for "+r["row_id"])
        address="I"+str(hit[0]);value=source.get(address,"")
        need(value==r["display"][8],"saved workbook value equals source "+address)
        y=72+i*98
        pen.rectangle((10,y,width-12,y+91),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        pen.text((20,y+7),r["row_id"]+" | "+address+" | "+r["label"],font=fb,fill="#173855")
        excerpt="G2-4A: "+value.split("G2-4A:",1)[1] if "G2-4A:" in value else value
        for j,line in enumerate(textwrap.wrap(excerpt,width=165,break_long_words=False)[:3]):
            pen.text((20,y+33+j*17),line,font=f,fill="#203951")
    img.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>15000,"actual saved workbook preview PNG not empty")
    print("PASS: G2-4A saved XLSX twenty-cell preview rendered (not Microsoft Excel-native view)")

if __name__=="__main__":
    publish()
    preview()
