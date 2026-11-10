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
REPORT="SOSA_G2_3_Workbook_Validation_09NOV2026.json"
PREVIEW="SOSA_G2_3_Workbook_Preview_09NOV2026.png"
OLD="35c36f7adfa47fed18b64a4cc2d4a7f3d40d24cf8ec683fdbbcdcdbd8ee5dfdb"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-G2-3 verification failed: "+message
def load(n):return json.loads((D/n).read_text(encoding="utf-8"))
def save(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def digest(b):return hashlib.sha256(b).hexdigest()
def source_csv(n):
    with (D/n).open(encoding="utf-8-sig",newline="") as f:return list(csv.reader(f))
def addr(i,j):return old.coord(i,j)
def check_source(m,l):
    need(m["schemaVersion"]=="0.14" and len(m["rows"])==329,"current G2-3 schema and information rows")
    need(len(m["columns"])==15 and [x["key"] for x in m["columns"]][8:10]==["OpenGroupSOSA","SOSA"] and m["columns"][-1]["key"]=="DIM","Open Group SOSA separate from W3C and DIM last")
    need([x["key"] for x in m["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"],"source case columns")
    grid=m["review_grid"]
    need(len(grid)==346 and all(len(x)==15 for x in grid) and len(m["review_sections"])==15,"exact 346x15 master grid and topic dividers")
    need([r for i,r in enumerate(grid) if i>1 and i not in set(m["review_sections"])] == [r["display"] for r in m["rows"]],"current row/display parity")
    need(grid==source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")==source_csv("ISA_Correction_Review_07NOV2026.csv"),"canonical and historical CSV mirrors")
    main=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    mirror=(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    need(main.split("<table>",1)[1]==mirror.split("<table>",1)[1] and main.count('colspan="15"')==15,"both 15-column GitHub-readable comparison bodies")
    need(len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73 and m["ISAEvidence"]["currentPrimaryReviews"]==480 and m["ISAEvidence"]["specificQuestions"]==6,"source donor/case/ISA evidence")
    need(len(l["all_57_qualified_source_decisions"])==57 and len(l["integration_row_ledger"])==38,"previous SOSA-D integration evidence")
    g1=load("SOSA_G2_1_Original_Item_Inventory_09NOV2026.json")
    g2=load("SOSA_G2_2_Original_Item_Inventory_09NOV2026.json")
    g3=load("SOSA_G2_3_Original_Source_Item_Census_09NOV2026.json")
    need(len(g1["items"])==201 and len(g2["source_items"])+len(g2["original_rule_appearances"])==352,"original earlier G2 research preserved")
    need(len(g3["source_clauses"])==76 and len(g3["source_states"])==32 and len(g3["architectural_context"])==11 and g3["counts"]["source_items"]==119,"all source-graded G2-3 items and exact counts")
    need(g3["counts"]["rule_shall"]==48 and g3["counts"]["rule_incomplete"]==1 and g3["counts"]["recommendations"]==8 and g3["counts"]["observations"]==11 and g3["counts"]["permissions"]==8,"source normativity grading")
    ids={x["id"] for x in g3["source_clauses"]+g3["source_states"]+g3["architectural_context"]}
    need(len(ids)==119,"unique stable original-source item IDs")
    new_rows=[r for r in m["rows"] if r.get("G2_3_source_correspondence")]
    need(len(new_rows)==28,"28 qualified new master cells, not 119 model fields")
    need(sum(bool(r.get("G2_1_source_correspondence")) for r in m["rows"])==12 and sum(bool(r.get("G2_2_source_correspondence")) for r in m["rows"])==22,"G2-1/G2-2 evidence still retained")
    for r in new_rows:
        ev=r["G2_3_source_correspondence"]
        need(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]),"verified original source references "+r["row_id"])
        need(ev["DIM_adopted"] is False and ev["native_external_references_read"] is False,"correct donor-source and nonadoption grade "+r["row_id"])
        need("G2-3:" in r["display"][8],"new source-qualified SOSA cell content "+r["row_id"])
    need(set(m["workbookSnapshot"]["G2_3_affected_row_ids"])=={r["row_id"] for r in new_rows},"only 28 original affected row identifiers")
    need(m["currentWorkbookSha256"]==OLD and m["workbookSnapshot"]["currently_matches_readable_view"] is False,"old saved G2-2 checkpoint accurately declared before refresh")
    need(l["native_DSDM_IDL_OpenAPI_eight_files_uninspected"] and l["non_adoption"],"no native file or DIM adoption overclaims")
    print("PASS: G2-3 source census 119 graded items, 28 donor cells, original 58+73+480 evidence, JSON/2CSV/2MD parity")

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
       ["SOSA-G2-3 CANONICAL EXCEL CHECKPOINT","C239 §§6.3–6.5 original inline text reviewed; donor OPEN"],
       ["Current table","329 information rows / 346 visual grid rows / 15 columns"],
       ["Original G2-3 source items","119 items: 76 Rule/Recommendation/Observation/Permission, 32 state definitions, 11 contexts"],
       ["Original rule standing","49 labeled Rules: 48 explicit SHALL, one source-labeled incomplete statement"],
       ["Other source standing","8 Recommendations, 11 Observations, 8 Permissions"],
       ["SOSA state definitions","20 sensor/PIC/module operational states; 12 separately scoped security states"],
       ["New qualified SOSA comparisons","28 existing source-donor I-column cells; no other columns changed"],
       ["Inherited donor evidence","SOSA-D 76 selected, G2-1 201, G2-2 352 items; native companions still unread"],
       ["Hardware source distinctions","Auxiliary management power vs payload, IPMC/FRU vs software, out-of-band vs in-band"],
       ["False equivalences held","P6/M6 Lost Communication not confirmed hardware fault; S0 typically not reported"],
       ["Evidence retained","58 earlier donor records, 73 case facts, 480 ISA source outcomes and six exact holds"],
       ["DIM/Profile adoption","None; no new class hierarchy, cardinality or runtime hardware test"],
       ["Formats and binary","Exact source/CSV/Markdown and SAVED 26-sheet XLSX 346x15 parity"],
       ["Next only on owner Proceed","SOSA-G2-4 native C239 §§1–5 and 7–11; SAPIENT blocked"]
    ]
def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        g2=r.get("G2_1_source_correspondence") or {}
        g22=r.get("G2_2_source_correspondence") or {}
        g23=r.get("G2_3_source_correspondence") or {}
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),r.get("master_inclusion",""),r.get("dim_adoption",""),
           "; ".join(r.get("source_entry_ids",[])),json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
           "; ".join(so.get("records",[])+g2.get("source_item_ids",[])+g22.get("source_item_ids",[])+g23.get("source_item_ids",[])),"; ".join(so.get("relations",[])+([g2["relation"]] if g2 else [])+([g22["mapping_relation"]] if g22 else [])+([g23["relation"]] if g23 else [])),
           "G2-3 C239 hardware/state source inline reviewed; native VITA/HOST/IPMI/DSDM/API dependencies not read" if g23 else "G2-2 C239 specialized source inline reviewed; native DSDM/API not read" if g22 else "G2-1 C239 inline original source reviewed; native DSDM/API not read" if g2 else "C239 selected source reviewed; native DSDM/API not read" if so else "Not assessed here"])
    return out
def publish():
    m=load(MASTER);l=load(LEDGER);check_source(m,l)
    prev=(D/BOOK).read_bytes()
    need(digest(prev)==OLD,"exact previously verified G2-2 26-tab workbook base hash; preserve same canonical workbook")
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
    need(len(delta)==28 and all(re.fullmatch(r"I\d+",a) for a in delta),"exactly 28 original source-qualified SOSA I-column saved cells changed, zero other cells")
    m["currentWorkbookSha256"]=digest_new
    m["currentEvidenceCheckpoint"]="SOSA-G2-3-SAVED_26_SHEET_XLSX_AND_SOURCE_PARITY_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-3-CANONICAL-VERIFIED","sha256":digest_new,
        "information_rows":329,"columns":15,"currently_matches_readable_view":True,
        "lag":"NONE: all 346x15 saved XLSX cells agree with canonical JSON, BOTH CSVs and BOTH readable comparisons",
        "refreshed_cell_count":28,"G2_3_affected_row_ids":m["workbookSnapshot"]["G2_3_affected_row_ids"],
        "validation_file":REPORT})
    m["SOSAEvidence"]["G2_3"].update({"excel_checkpoint":"SOSA-G2-3-CANONICAL-VERIFIED","excel_validation":REPORT,"excel_28_source_cells_synced":True})
    m["SOSAReviewCompletion"]["G2_3_XLSX_lag"]=0
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="SOSA-G2-4 C239 §§1–5 and §§7–11 original-source completeness screening only on separate owner Proceed"
    m["publicationPolicy"]="Binding L23: Each substantive donor source review that changes comparison cells must update JSON, both CSVs and both Markdown tables, then synchronize and verify this SAME canonical 26-sheet XLSX before any next source packet. G2-3 28 new source-qualified I-column cells synchronized; no DIM/Profile adoption or external native source completeness."
    m["nextOwnerAction"]="SOSA-G2-4 only on separate owner Proceed: original C239 §§1–5 and §§7–11 missing architecture, sensors/tasking/mission clauses, sized by original source complexity; SAPIENT blocked pending SOSA donor gate."
    save(MASTER,m)
    record={"date":"2026-11-09","step":"SOSA-G2-3-EXCEL-CHECKPOINT","result":"EXACT_SAVED_26_SHEET_AND_TWO_CSV_TWO_MD_PARITY_PASS",
      "workbook_sha256":digest_new,"base_workbook_sha256":OLD,
      "workbook_sheets":list(paths),"refreshed_sheets":list(tables),
      "exact_original_untouched_xml_sha256":unchanged,
      "source_rows":329,"grid_rows":346,"columns":15,"original_donor_evidence":58,"case_evidence":73,
      "G2_3_native_source_items":119,"G2_3_original_rule_labels":49,"G2_3_clear_source_shalls":48,
      "G2_3_original_rule_incomplete":1,"G2_3_source_state_labels":32,
      "G2_3_qualified_source_cell_count":28,"changed_saved_cells":sorted(delta),
      "unread_native_DSDM_IDL_OpenAPI_files":8,"unread_external_normative_hardware_standards":True,
      "open_original_ISA_questions":6,
      "checks":{"actual_XLSX_all_346x15_equal_current_JSON_CSV":True,
          "two_CSV_and_two_Markdown_comparisons_equal":True,"same_26_worksheet_names_order":True,
          "22_historical_worksheet_XML_bytes_preserved":True,"only_28_original_SOSA_I_column_cells_changed":True,
          "ZIP_CRC_and_XML_valid":True,"zero_XLSX_error_type_cells":True,"zero_DIM_Profile_adoption":True},
      "limits":["No ANSI/VITA/HOST/IPMI original normative companion audit","No C239 DSDM/IDL/OpenAPI original bytes inspected",
        "No comprehensive The Open Group SOSA donor coverage or conformance","Saved-cell PNG preview not Microsoft Excel-native rendering"],
      "next":"SOSA-G2-4 C239 §§1–5 and 7–11 only on separate owner Proceed"}
    save(REPORT,record)
    print("PASS: canonical workbook all 5190 source cells equal, 26 tabs retained; new SHA256",digest_new)
    return digest_new
def preview():
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER)
    cells=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_3_source_correspondence")]
    need(len(rows)==28,"28 G2-3 source-qualified saved workbook rows")
    try:
        f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        fb=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:f=fb=ImageFont.load_default()
    width,height=1600,2840
    im=Image.new("RGB",(width,height),"white")
    p=ImageDraw.Draw(im)
    p.rectangle((0,0,width,65),fill="#173855")
    p.text((20,16),"SOSA-G2-3 | 28 source-qualified rows in the ACTUAL saved 26-sheet canonical Excel",font=fb,fill="white")
    for i,r in enumerate(rows):
        hit=[k+1 for k,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(hit)==1,"unique saved crosswalk source row "+r["row_id"])
        cell="I"+str(hit[0]);value=cells.get(cell,"")
        need(value==r["display"][8],"original saved Excel cell matches source "+cell)
        y=72+i*97
        p.rectangle((10,y,width-12,y+90),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        p.text((20,y+8),r["row_id"]+" | "+cell+" | "+r["label"],font=fb,fill="#173855")
        excerpt="G2-3: "+value.split("G2-3:",1)[1] if "G2-3:" in value else value
        for z,line in enumerate(textwrap.wrap(excerpt,width=170,break_long_words=False)[:3]):
            p.text((20,y+32+z*17),line,font=f,fill="#203951")
    im.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>15000,"actual saved XLSX cells preview rendered")
    print("PASS: G2-3 saved XLSX preview from actual cells (not Excel-native screenshot)")

if __name__=="__main__":
    publish()
    preview()
