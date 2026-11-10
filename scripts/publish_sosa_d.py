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
REPORT="SOSA_G2_2_Workbook_Validation_09NOV2026.json"
PREVIEW="SOSA_G2_2_Workbook_Preview_09NOV2026.png"
OLD="6a22fb1d76be9decd11a0023136d55750971020c8c23d60dc4dbb57ab332ec9b"
q=old.q
ET.register_namespace("",old.X);ET.register_namespace("r",old.REL)
def need(x,message):assert x,"SOSA-G2-2 verification failed: "+message
def load(n):return json.loads((D/n).read_text(encoding="utf-8"))
def save(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def digest(b):return hashlib.sha256(b).hexdigest()
def source_csv(n):
    with (D/n).open(encoding="utf-8-sig",newline="") as f:return list(csv.reader(f))
def addr(i,j):return old.coord(i,j)
def check_source(m,l):
    need(m["schemaVersion"] == "0.13" and len(m["rows"]) == 329, "current G2-2 schema and stable 329 source rows")
    need(len(m["columns"]) == 15 and [v["key"] for v in m["columns"]][8:10] == ["OpenGroupSOSA","SOSA"]
         and m["columns"][-1]["key"] == "DIM", "separate Open Group/W3C and rightmost proposed DIM")
    need([v["key"] for v in m["columns"][:4]] == ["Dragino","AirGradient","Campbell","Bennett"], "four source cases left")
    g=m["review_grid"]
    need(len(g)==346 and all(len(row)==15 for row in g) and len(m["review_sections"])==15, "346x15 rows and dividers")
    need([row for i,row in enumerate(g) if i>1 and i not in set(m["review_sections"])] == [row["display"] for row in m["rows"]], "JSON row-to-grid parity")
    need(g == source_csv("Master_Donor_Concept_to_DIM_Crosswalk.csv")
              == source_csv("ISA_Correction_Review_07NOV2026.csv"), "BOTH CSV mirrors exact")
    a=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    b=(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    need(a.split("<table>",1)[1] == b.split("<table>",1)[1] and a.count('colspan="15"')==15, "BOTH readable comparison tables")
    need(len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73, "all original donor and four-case records")
    need(m["ISAEvidence"]["currentPrimaryReviews"]==480 and m["ISAEvidence"]["specificQuestions"]==6, "ISA source evidence and holds")
    need(len(l["all_57_qualified_source_decisions"])==57 and len(l["integration_row_ledger"])==38
         and l["source_native_records"]==76, "original SOSA-D selected evidence preserved")
    earlier=load("SOSA_G2_1_Original_Item_Inventory_09NOV2026.json")
    need(len(earlier["items"])==201, "original G2-1 source records preserved")
    inv=load("SOSA_G2_2_Original_Item_Inventory_09NOV2026.json")
    items=inv["source_items"];rules=inv["original_rule_appearances"]
    ids={x["id"] for x in items+rules}
    need(len(items)==340 and len(rules)==12 and len(ids)==352, "all 352 original native C239 source records unique")
    need(sum(x["support"]=="V1.0" for x in items)==208 and sum(x["support"]=="Future" for x in items)==132, "native support grades exact")
    need(sum(x["normative_standing"]=="RULE_SHALL" for x in rules)==10
         and sum(x["normative_standing"]=="RULE_LABELED_DESCRIPTIVE" for x in rules)==2, "original rule standing exact")
    g1_rows=[x for x in m["rows"] if x.get("G2_1_source_correspondence")]
    g2_rows=[x for x in m["rows"] if x.get("G2_2_source_correspondence")]
    need(len(g1_rows)==12 and len(g2_rows)==22, "preserve 12 G2-1 and new 22 G2-2 source-qualified mappings")
    for row in g2_rows:
        ev=row["G2_2_source_correspondence"]
        need(ev["source_item_ids"] and all(x in ids for x in ev["source_item_ids"]), "actual native ID and nonempty mapping "+row["row_id"])
        need(ev["dim_adopted"] is False and ev["api_schema_bytes_read"] is False, "no invented model or native API source "+row["row_id"])
        need("G2-2:" in row["display"][8], "source-qualified G2-2 cell "+row["row_id"])
    need(set(m["workbookSnapshot"]["G2_2_affected_row_ids"]) == {x["row_id"] for x in g2_rows}, "exact 22 changed original row identifiers")
    need(m["currentWorkbookSha256"]==OLD and not m["workbookSnapshot"]["currently_matches_readable_view"], "unchanged 26-sheet G2-1 original workbook prior to refresh")
    need(l["native_DSDM_IDL_OpenAPI_eight_files_uninspected"] and l["non_adoption"], "native source and DIM adoption caveats preserved")
    print("PASS: G2-2 352 native source items/Rules, 22 qualified SOSA cells, JSON/2CSV/2Markdown 346x15 parity and old evidence retained")
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
        ["SOSA-G2-2 CANONICAL EXCEL CHECKPOINT","C239 inline source review; full donor still OPEN"],
        ["Master","329 information rows / 346 presentation rows / 15 columns"],
        ["Original G2-2 native source items","209 function entries, 131 interaction entries, 12 Rule-labeled paragraphs"],
        ["Source normative standing","10 original shall Rules, two descriptive paragraphs labeled Rule"],
        ["Source edition support","208 V1.0 and 132 Future source function/interaction entries"],
        ["Source-qualified updated donor cells","22 existing The Open Group SOSA cells refreshed, no other column edits"],
        ["Previous SOSA evidence","SOSA-D 76/57/38 plus G2-1 201 native items and 12 prior source-qualified rows"],
        ["Native source holds","C239 DSDM, IDL and six OpenAPI JSONs unread; B.3 reference conflicts and repeated PIC Rule IDs"],
        ["Source semantics","Chassis Manager hardware/low-level IPMI vs PIC direct/indirect management vs logical SW RTE"],
        ["Preserved historical evidence","58 donor records, 73 case facts, 480 ISA DMS outcomes including six exact holds"],
        ["DIM/Profile standing","No new DIM classes, cardinalities, Profile SHALL, runtime test or installed equipment command"],
        ["XLSX and mirrors","Exact saved XLSX cell parity with JSON, both CSVs and both readable comparisons; 26 sheets"],
        ["Next on owner Proceed","SOSA-G2-3: original C239 §§6.3–6.5; SAPIENT Step18 blocked"]
    ]
def register(m):
    out=[["Stable row ID","Proposed element","Definition","Status","Source grade","Inclusion","Adoption","Native ISA IDs","ISA source correspondence","SOSA C239 relation record IDs","SOSA relations","Native source status"]]
    for r in m["rows"]:
        so=r.get("sosa_correspondence") or {}
        g2=r.get("G2_1_source_correspondence") or {}
        g22=r.get("G2_2_source_correspondence") or {}
        out.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),r.get("source_review_status",""),r.get("master_inclusion",""),r.get("dim_adoption",""),
           "; ".join(r.get("source_entry_ids",[])),json.dumps(r.get("source_first_correspondence",{}),ensure_ascii=False)[:2000],
           "; ".join(so.get("records",[])+g2.get("source_item_ids",[])+g22.get("source_item_ids",[])),"; ".join(so.get("relations",[])+([g2["relation"]] if g2 else [])+([g22["mapping_relation"]] if g22 else [])),
           "G2-2 C239 specialized source inline reviewed; native DSDM/API not read" if g22 else "G2-1 C239 inline original source reviewed; native DSDM/API not read" if g2 else "C239 selected source reviewed; native DSDM/API not read" if so else "Not assessed here"])
    return out
def publish():
    m=load(MASTER);l=load(LEDGER);check_source(m,l)
    prev=(D/BOOK).read_bytes()
    need(digest(prev)==OLD,"exact verified 26-tab G2-1 workbook base hash; preserve same canonical workbook")
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
    need(len(delta)==22 and all(re.fullmatch(r"I\d+",a) for a in delta), "only 22 original The Open Group SOSA saved cells changed")
    m["currentWorkbookSha256"]=digest_new
    m["currentEvidenceCheckpoint"]="SOSA-G2-2-SAVED_26_SHEET_XLSX_AND_SOURCE_PARITY_VERIFIED"
    m["workbookSnapshot"].update({"checkpoint":"SOSA-G2-2-CANONICAL-VERIFIED","sha256":digest_new,
        "information_rows":329,"columns":15,"currently_matches_readable_view":True,
        "lag":"NONE: exact current 346x15 source/2CSV/2Markdown/26-sheet XLSX parity",
        "refreshed_cell_count":22,"G2_2_affected_row_ids":m["workbookSnapshot"]["G2_2_affected_row_ids"],
        "validation_file":REPORT})
    m["SOSAEvidence"]["G2_2"].update({"excel_checkpoint":"SOSA-G2-2-CANONICAL-VERIFIED",
        "excel_validation":REPORT,"excel_22_source_cells_synced":True})
    m["SOSAReviewCompletion"]["G2_2_excel_lag"]=0
    m["SOSAReviewCompletion"]["next_on_owner_proceed"]="SOSA-G2-3 C239 §§6.3–6.5 original out-of-band management/component-state source-first review"
    m["publicationPolicy"]="Binding L23: Each substantive donor-source packet with meaningful canonical comparison changes must finish with verified source JSON, BOTH CSVs, BOTH Markdown mirrors and SAME 26-sheet XLSX saved-cell parity before another research packet. G2-2 22 source-qualified cells now synchronized. Source coverage, DIM/Profile adoption and runtime conformance remain distinct."
    m["nextOwnerAction"]="SOSA-G2-3 only on next separate owner Proceed: original C239 §§6.3–6.5, out-of-band hardware management and component state; Step18 SAPIENT BLOCKED pending source-based donor completion."
    save(MASTER,m)
    # Keep historical SOSA-D and G2-1 research and workbook validation immutable.
    report={"date":"2026-11-09","step":"SOSA-G2-2-EXCEL-CHECKPOINT","result":"EXACT_SAVED_26_SHEET_AND_FOUR_TEXT_FORMAT_PARITY_PASS",
        "workbook_sha256":digest_new,"base_workbook_sha256":OLD,
        "workbook_sheets":list(paths),"refreshed_sheets":list(tables),
        "exact_original_untouched_xml_sha256":unchanged,
        "source_rows":329,"grid_rows":346,"columns":15,
        "original_donor_evidence":58,"case_evidence":73,
        "G2_2_native_source_table_items":340,"G2_2_rule_labeled_paragraphs":12,
        "G2_2_qualified_source_cell_count":22,"changed_saved_cells":sorted(delta),
        "G2_2_source_V1_0_entries":208,"G2_2_source_Future_entries":132,
        "G2_2_source_shall_rules":10,"G2_2_source_descriptive_rule_labels":2,
        "native_DSDM_IDL_OpenAPI_unread":8,"ISA_original_questions_open":6,
        "checks":{"actual_XLSX_all_346x15_equal_current_JSON_and_CSV":True,
            "both_CSV_and_GitHub_readable_mirrors_exact":True,
            "same_26_worksheet_names_order":True,"22_unmodified_historical_sheets_XML_byte_identical":True,
            "only_22_original_SOSA_I_column_cells_changed":True,
            "valid_XLSX_ZIP_CRC_XML":True,"zero_XLSX_error_cells":True,
            "zero_DIM_Profile_adoption":True},
        "limits":["No C239 original native OpenAPI/IDL/DSDM contents inspected",
                  "No C239/SOSA comprehensive original-source completion claim",
                  "No independent device runtime/interop or physical command","Actual saved-cell preview is not Microsoft Excel-native rendering"],
        "next":"SOSA-G2-3 C239 §§6.3–6.5 only on separate owner Proceed"}
    save(REPORT,report)
    print("PASS: canonical workbook all 5190 source cells equal, 26 tabs retained; new SHA256",digest_new)
    return digest_new
def preview():
    # Visualize the *actual saved canonical workbook cells* changed in this G2-2 packet.
    from PIL import Image,ImageDraw,ImageFont
    m=load(MASTER); cells=old.readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    rows=[r for r in m["rows"] if r.get("G2_2_source_correspondence")]
    need(len(rows)==22,"22 source-qualified rows visible in saved workbook")
    try:
        f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",11)
        fb=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",13)
    except OSError:f=fb=ImageFont.load_default()
    width,height=1600,2250
    im=Image.new("RGB",(width,height),"white")
    p=ImageDraw.Draw(im)
    p.rectangle((0,0,width,64),fill="#173855")
    p.text((18,17),"SOSA-G2-2 | 22 verified source-qualified cells in saved 26-sheet canonical Excel",font=fb,fill="white")
    for i,r in enumerate(rows):
        found=[k+1 for k,g in enumerate(m["review_grid"]) if g[14]==r["label"] and g[8]==r["display"][8]]
        need(len(found)==1,"unique saved original grid row "+r["row_id"])
        addr1="I"+str(found[0]); value=cells.get(addr1,"")
        need(value==r["display"][8],"preview cell actually matches saved XLSX "+addr1)
        y=75+i*97
        p.rectangle((12,y,width-12,y+90),fill="#F1F6FA" if i%2==0 else "white",outline="#CCD8E4")
        p.text((20,y+7),r["row_id"]+" | "+addr1+" | "+r["label"],font=fb,fill="#173855")
        display="G2-2: "+value.split("G2-2:",1)[1] if "G2-2:" in value else value
        for z,line in enumerate(textwrap.wrap(display,width=176,break_long_words=False)[:3]):
            p.text((20,y+31+z*17),line,font=f,fill="#203951")
    im.save(D/PREVIEW,optimize=True)
    need((D/PREVIEW).stat().st_size>15000,"real saved XLSX-cell visual PNG rendered")
    print("PASS: G2-2 real saved XLSX 22-cell preview created (not native Excel UI rendering)")

if __name__=="__main__":
    publish()
    preview()
