#!/usr/bin/env python3
"""ISA Delivery22 one-time workbook refresh from committed original-source records.
The existing 26-sheet XLSX is preserved and selected review sheets are rewritten
using standard OOXML ZIP/XML; no Office/LibreOffice or alternative spreadsheet
library and no new semantic mappings."""
import csv, hashlib, io, json, os, re, textwrap, zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

R=Path(__file__).resolve().parents[1]
D=R/"Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk"
X="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
SPACE="http://www.w3.org/XML/1998/namespace"
q=lambda s,ns=X:"{"+ns+"}"+s
ET.register_namespace("",X);ET.register_namespace("r",REL)
BOOK="Master_Donor_Concept_to_DIM_Crosswalk.xlsx"
AUDIT="ISA21_Source_First_31_Targets_25_Findings_6_Questions_09NOV2026.json"
OUT="ISA22_Validated_Workbook_Record_09NOV2026.json"
IMAGE="ISA22_Workbook_Visual_09NOV2026.png"
OLD="4a660bc7f4640850fdc3215d3ea3686155ce8d1f0f05c07ca29b27b6078c3806"

def require(a,s):
    if not a: raise AssertionError("ISA22 failed: "+s)
def obj(n): return json.loads((D/n).read_text(encoding="utf-8"))
def csvrows(n):
    with (D/n).open(encoding="utf-8-sig",newline="") as f:return list(csv.reader(f))
def sha(b):return hashlib.sha256(b).hexdigest()
def val(o):
    if o is None:return ""
    if isinstance(o,str):return o
    if isinstance(o,(bool,int,float)):return str(o)
    return json.dumps(o,ensure_ascii=False,separators=(",",":"))
def coord(i,j):
    a=""
    while j:
        j,k=divmod(j-1,26);a=chr(65+k)+a
    return a+str(i)

def read_source():
    m=obj("Master_Donor_Concept_to_DIM_Crosswalk.json")
    s=obj("ISA_Correction_Status_07NOV2026.json")
    c=obj("ISA_Coverage_Register_07NOV2026.json")
    a=obj(AUDIT)
    dms=csvrows("ISA_DMS_Entry_Inventory_07NOV2026.csv")
    blocks=csvrows("ISA_Source_Block_Register_07NOV2026.csv")
    grid=m["review_grid"]
    require(len(grid)==346 and all(len(r)==14 for r in grid),"346x14 grid")
    require(len(m["columns"])==14 and m["columns"][-1]["key"]=="DIM","DIM rightmost")
    require([x["key"] for x in m["columns"][:4]]==["Dragino","AirGradient","Campbell","Bennett"],"four cases leftmost")
    require(len(m["rows"])==329 and len({r["row_id"] for r in m["rows"]})==329,"329 unique rows")
    require(len(m["originalDonorEvidence"])==58 and len(m["caseEvidence"])==73,"58/73 original evidence")
    require(grid==csvrows("Master_Donor_Concept_to_DIM_Crosswalk.csv")==csvrows("ISA_Correction_Review_07NOV2026.csv"),"CSV/JSON exact parity")
    one=(D/"Master_Donor_Concept_to_DIM_Crosswalk.md").read_text(encoding="utf-8")
    two=(D/"ISA_Correction_Review_07NOV2026.md").read_text(encoding="utf-8")
    require(one.split("\n",1)[1]==two.split("\n",1)[1],"human Markdown table parity")
    require(len(dms)==481 and len({r[0] for r in dms[1:]})==480,"480 DMS CSV IDs")
    require(len(blocks)==280 and len({r[0] for r in blocks[1:]})==279,"279 source-block CSV IDs")
    require(len(c["dms_entries"])==480 and len(c["source_blocks"])==279,"coverage JSON 480/279")
    require(len(c["row_targets"])==31 and len(c["legacy_records"])==25,"coverage JSON 31/25")
    require([len(a[k]) for k in ("original_row_and_case_targets","original_earlier_findings","six_precise_source_questions")]==[31,25,6],"source audit 31/25/6")
    require(len({t["row_key"] for t in a["original_row_and_case_targets"]})==31,"unique original target IDs")
    require(len({v["id"] for v in a["original_earlier_findings"]})==25,"unique prior finding IDs")
    require(all(not x["question_closed"] for x in a["six_precise_source_questions"]),"six questions retain OPEN")
    require(m["ISAEvidence"]["currentPrimaryReviews"]==480 and m["ISAEvidence"]["sourceSupportedPrimary"]==474 and m["ISAEvidence"]["specificQuestions"]==6,"474/6 DMS")
    require(a["counts"]["qualified_native_correspondence"]==18 and a["counts"]["no_established_source_equivalence"]==4,"18/four correspondence")
    require(a["counts"]["case_holds_retained"]==9 and a["counts"]["design_findings_held"]==14,"nine/14 retained holds")
    require(m["ISAEvidence"]["sourceFirstCorrespondence"]["ISA_cells_changed"]==29 and a["counts"]["dim_content_adopted"]==0,"29 ISA-only cells; zero adopted DIM")
    require(s["nextOnOwnerProceed"]=="ISA-FINAL-VALIDATION-EXCEL-CLOSEOUT" and s["technicalIterationsCompleted"]==40,"Delivery22 starting authority")
    require(m["currentWorkbookSha256"]==OLD and sha((D/BOOK).read_bytes())==OLD,"old workbook exact original hash")
    native={r[0] for r in dms[1:]}
    refs={z for row in a["original_row_and_case_targets"] for z in row.get("native_dms_entry_ids",[])}
    require(refs<=native,"no invalid DMS ID in Delivery21")
    require(len([t for t in a["original_row_and_case_targets"] if t["row_key"].startswith("S06-R")])==22,"22 original DIM rows")
    print("SOURCE PASS: 329 data rows / 346 grid rows, 480 DMS, 279 blocks, 31/25/six source audit.")
    return m,a,dms,blocks

def sheetpaths(z):
    wb=ET.fromstring(z.read("xl/workbook.xml"))
    rels={r.get("Id"):r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
    ret={}
    for s in wb.find(q("sheets")):
        t=rels[s.get(q("id",REL))]
        ret[s.get("name")]=t.lstrip("/") if t.startswith("/") else "xl/"+t
    return ret

def newstyles(xml):
    root=ET.fromstring(xml); fonts=root.find(q("fonts")); fills=root.find(q("fills")); xfs=root.find(q("cellXfs"))
    require(fonts is not None and fills is not None and xfs is not None,"legacy styles structure")
    def font(color,bold=False):
        ix=len(fonts);f=ET.SubElement(fonts,q("font"));ET.SubElement(f,q("sz"),{"val":"10"})
        ET.SubElement(f,q("name"),{"val":"Aptos"})
        if bold:ET.SubElement(f,q("b"))
        ET.SubElement(f,q("color"),{"rgb":"FF"+color});return ix
    def fill(color):
        ix=len(fills); f=ET.SubElement(fills,q("fill"));p=ET.SubElement(f,q("patternFill"),{"patternType":"solid"})
        ET.SubElement(p,q("fgColor"),{"rgb":"FF"+color});ET.SubElement(p,q("bgColor"),{"indexed":"64"});return ix
    fw=font("FFFFFF",True);fd=font("16344C");fb=font("16344C",True)
    navy=fill("173855");pale=fill("D7E8F2");white=fill("FFFFFF");off=fill("F2F7FB")
    def sty(fi,bi):
        ix=len(xfs);x=ET.SubElement(xfs,q("xf"),{"numFmtId":"0","fontId":str(fi),"fillId":str(bi),"borderId":"0","xfId":"0","applyFont":"1","applyFill":"1","applyAlignment":"1"})
        ET.SubElement(x,q("alignment"),{"wrapText":"1","vertical":"center"});return ix
    names={"band":sty(fw,navy),"header":sty(fb,pale),"section":sty(fb,pale),
           "data":sty(fd,white),"alt":sty(fd,off)}
    for el in (fonts,fills,xfs):el.set("count",str(len(el)))
    return ET.tostring(root,encoding="utf-8",xml_declaration=True),names

def worksheet(rows,style,main=False,section_rows=()):
    require(len(rows)>0 and len(rows[0])<=20,"sheet source shape")
    root=ET.Element(q("worksheet"));view=ET.SubElement(ET.SubElement(root,q("sheetViews")),q("sheetView"),{"workbookViewId":"0","showGridLines":"0"})
    ET.SubElement(view,q("pane"),{"xSplit":"4" if main else "1","ySplit":"2" if main else "1","topLeftCell":"E3" if main else "B2","activePane":"bottomRight","state":"frozen"})
    ET.SubElement(root,q("sheetFormatPr"),{"defaultRowHeight":"19"})
    cols=ET.SubElement(root,q("cols"))
    widths=([28,30,32,31,29,32,33,36,31,31,32,33,35,40] if main else [24]+[37]*19)
    width=max(map(len,rows))
    for i in range(width):ET.SubElement(cols,q("col"),{"min":str(i+1),"max":str(i+1),"width":str(widths[i]),"customWidth":"1"})
    data=ET.SubElement(root,q("sheetData"));secs=set(section_rows)
    for i,row in enumerate(rows):
        section=main and i in secs
        height=35 if not main and i==0 else 38 if not main else 31 if i==0 else 51 if i==1 else 46 if section else 48
        node=ET.SubElement(data,q("row"),{"r":str(i+1),"ht":str(height),"customHeight":"1"})
        for j,value in enumerate(row):
            value=val(value)
            if not value:continue
            require(len(value)<=32767,"Excel cell text limit")
            which="band" if main and i==0 else "header" if main and i==1 else "section" if section else "band" if not main and i==0 else "alt" if i%2==0 else "data"
            c=ET.SubElement(node,q("c"),{"r":coord(i+1,j+1),"s":str(style[which]),"t":"inlineStr"})
            t=ET.SubElement(ET.SubElement(c,q("is")),q("t"));t.set(q("space",SPACE),"preserve");t.text=value
    if main:
        a=[("A1","D1"),("E1","H1"),("I1","M1")]+[("A"+str(i+1),"N"+str(i+1)) for i in sorted(secs)]
        merged=ET.SubElement(root,q("mergeCells"),{"count":str(len(a))})
        for l,r in a:ET.SubElement(merged,q("mergeCell"),{"ref":l+":"+r})
    ET.SubElement(root,q("pageMargins"),{"left":".3","right":".3","top":".45","bottom":".45","header":".15","footer":".15"})
    return ET.tostring(root,encoding="utf-8",xml_declaration=True)

def audit_sheet(a):
    rows=[["Category","ID","Original topic","Source-first disposition","Original source","Non-equivalence or unanswered question","DIM/model status","Source clauses"]]
    for x in a["original_row_and_case_targets"]:
        loc="; ".join(z.get("source","")+" "+z.get("section","") for z in x.get("original_source_locators",[]))
        rows.append(["Original target",x["row_key"],x.get("target_label",""),x.get("outcome",""),
                     x.get("native_source_term",""),x.get("boundary_and_negative_check",""),x.get("dim_adoption",""),loc])
    for x in a["original_earlier_findings"]:
        rows.append(["Earlier finding",x["id"],x.get("original_row_key",""),x.get("audited_relation_or_boundary",""),
                     x.get("source_term",""),x.get("source_first_conclusion",""),x.get("dim_adoption_or_design_decision",""),"; ".join(x.get("related_targets",[]))])
    for x in a["six_precise_source_questions"]:
        rows.append(["Open source question",x["id"],x.get("native_term",""),x["status"],x.get("source_first_finding",""),
                     x.get("unresolved_gap",""),"OPEN; no inferred source meaning","; ".join(x.get("checked_original_passages",[]))])
    return rows

def dim_register(m):
    rows=[["Stable row ID","Proposed DIM element","Working definition","Current status","Source review","Master inclusion","Model adoption","Native DMS evidence IDs","ISA source-first correspondence"]]
    for r in m["rows"]:
        rows.append([r["row_id"],r.get("label",""),r.get("definition",""),r.get("status",""),
                     r.get("source_review_status",""),r.get("master_inclusion",""),r.get("dim_adoption",""),
                     "; ".join(r.get("source_entry_ids",[])),r.get("source_first_correspondence","")])
    return rows

def review_rows(a):
    return [["Original target ID","Topic","Original ISA term","Source audit relation","Negative/hold boundary","DIM decision"]]+[
        [x["row_key"],x.get("target_label",""),x.get("native_source_term",""),x.get("outcome",""),x.get("boundary_and_negative_check",""),x.get("dim_adoption","")]
        for x in a["original_row_and_case_targets"]]
def old_findings(a):
    return [["Original finding ID","Target row","Native topic","Source-first adjudication","Model/design disposition"]]+[
        [x["id"],x.get("original_row_key",""),x.get("source_term",""),x.get("source_first_conclusion",""),x.get("dim_adoption_or_design_decision","")]
        for x in a["original_earlier_findings"]]
def questions(a):
    return [["Question ID","Original term","Unresolved source meaning","Source review statement","Retained review status","Original passages"]]+[
        [x["id"],x["native_term"],x["unresolved_gap"],x["source_first_finding"],x["status"],"; ".join(x["checked_original_passages"])]
        for x in a["six_precise_source_questions"]]
def summary():
    return [
      ["ISA22 FINAL SOURCE QUALIFICATION","Evidence-verified status"],
      ["ISA correction","22/22 deliveries; 41/41 technical iterations"],
      ["Master", "329 information rows / 14 columns / 346 visual rows"],
      ["Source entry coverage","480 native DMS = 474 source-supported + six precise open questions"],
      ["Original source-block register","279 blocks: 249 source-reviewed, 29 DMS headings accounted, one historic 2015 full-text HOLD"],
      ["Original source-first audit","31 targets: 18 qualified native correspondence, 4 no established equivalence, 9 case holds"],
      ["Older finding audit","25 records: 11 mappings source-qualified and 14 design holds"],
      ["Other donors and empirical cases","58 donor source records, 73 case facts preserved"],
      ["Master cell changes","29 ISA-only edits (already integrated in Delivery21)"],
      ["Model adoption","Zero; no mandatory ISA chassis or OGC Profile adoption"],
      ["Bennett historical evidence","Two original NOAA means vs four project digital representations"],
      ["External conformance","NOT tested; neither original OGC ATS nor physical Commands"],
      ["Next","Broader donor crosswalk Step16 owner checkpoint only after a new Proceed"]
    ]

def readcells(binary,name):
    with zipfile.ZipFile(io.BytesIO(binary)) as z:
        p=sheetpaths(z)[name]
        shared=[]
        if "xl/sharedStrings.xml" in z.namelist():
            shared=["".join(s.itertext()) for s in ET.fromstring(z.read("xl/sharedStrings.xml"))]
        cells={}
        for c in ET.fromstring(z.read(p)).iter(q("c")):
            inline=c.find(q("is")); vv=c.find(q("v"))
            data="".join(inline.itertext()) if inline is not None else (vv.text or "" if vv is not None else "")
            if c.get("t")=="s" and vv is not None:data=shared[int(vv.text)]
            cells[c.get("r")]=data
        return cells

def refresh(m,a,dms,blocks):
    original=(D/BOOK).read_bytes()
    with zipfile.ZipFile(io.BytesIO(original)) as z:
        require(z.testzip() is None,"original ZIP CRC")
        sheets=sheetpaths(z)
        require(len(sheets)==26 and "Master Crosswalk" in sheets,"all original 26 sheets and primary sheet")
        styles,style=newstyles(z.read("xl/styles.xml"))
        contents={
          "Master Crosswalk":m["review_grid"],
          "DIM Register":dim_register(m),
          "DMS Inventory":dms,
          "Source Blocks":blocks,
          "Row Coverage":review_rows(a),
          "Earlier Findings":old_findings(a),
          "Questions":questions(a),
          "ISA Evidence":audit_sheet(a),
          "Summary":summary(),
          "Validation":summary(),
        }
        required={"Master Crosswalk","DIM Register","DMS Inventory","Source Blocks","Row Coverage","Earlier Findings","Questions","ISA Evidence"}
        require(required<=set(sheets),"all current original-named workbook review tabs: "+str(sorted(required-set(sheets))))
        rewrite={"xl/styles.xml":styles}
        for n,rows in contents.items():
            if n in sheets:rewrite[sheets[n]]=worksheet(rows,style,n=="Master Crosswalk",m["review_sections"] if n=="Master Crosswalk" else ())
        unchanged={n:sha(z.read(p)) for n,p in sheets.items() if p not in rewrite}
        out=io.BytesIO()
        with zipfile.ZipFile(out,"w") as dst:
            for info in z.infolist():dst.writestr(info,rewrite.get(info.filename,z.read(info.filename)))
    result=out.getvalue()
    with zipfile.ZipFile(io.BytesIO(result)) as z:
        require(z.testzip() is None,"updated ZIP CRC")
        after=sheetpaths(z)
        require(list(after)==list(sheets) and len(after)==26,"all 26 original tabs survive in order")
        for n,digest in unchanged.items():require(sha(z.read(after[n]))==digest,"historical tab changed: "+n)
        for p in z.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(z.read(p))
    actual=readcells(result,"Master Crosswalk")
    for i,row in enumerate(m["review_grid"],1):
        for j,value in enumerate(row,1):
            require(actual.get(coord(i,j),"")==val(value),"current XLSX JSON parity at "+coord(i,j))
    expected={"DIM Register":330,"DMS Inventory":481,"Source Blocks":280,"Row Coverage":32,"Earlier Findings":26,"Questions":7,"ISA Evidence":63}
    for name,count in expected.items():
        c=readcells(result,name)
        require(sum(bool(re.fullmatch("A[0-9]+",key)) for key in c)==count,"updated original worksheet records: "+name)
    (D/BOOK).write_bytes(result)
    return {"workbook_sha256":sha(result),"sheets":list(sheets),"updated_tabs":[n for n in contents if n in sheets],
            "untouched_original_tabs":list(unchanged),"xlsx_bytes":len(result)}

def preview():
    from PIL import Image,ImageDraw,ImageFont
    cells=readcells((D/BOOK).read_bytes(),"Master Crosswalk")
    try:
        font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",13)
        bold=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",14)
    except OSError:font=bold=ImageFont.load_default()
    widths=[220,238,255,245,235,245,250,270,225,225,235,235,250,275]
    heights=[35,67,62,76,76,76,76,76,62,76,76]
    im=Image.new("RGB",(sum(widths)+36,sum(heights)+58),"white");d=ImageDraw.Draw(im)
    d.text((16,10),"ISA22: ACTUAL WORKBOOK / MASTER CROSSWALK A1:N11",font=bold,fill="#173855")
    y=48
    for i,h in enumerate(heights,1):
        x=18
        for j,w in enumerate(widths,1):
            color="#173855" if i==1 else "#C8DEED" if i==2 else "#DCEAF2" if i in (3,9) else "#F2F7FB" if i%2==0 else "#FFFFFF"
            d.rectangle((x,y,x+w,y+h),fill=color,outline="#B9CAD7")
            v=cells.get(coord(i,j),"")
            if v and (i not in (3,9) or j==1):
                lines=textwrap.wrap(v,max(19,(w-16)//9),break_long_words=False)[:3]
                for k,line in enumerate(lines):d.text((x+6,y+7+k*18),line,font=bold if i<=3 or i==9 else font,fill="white" if i==1 else "#16344C")
            x+=w
        y+=h
    im.save(D/IMAGE,optimize=True)
    require((D/IMAGE).stat().st_size>10000,"saved-workbook visual preview")
    return {"file":IMAGE,"range":"A1:N11","rendering":"PNG from re-opened actual XLSX cells using Pillow; not native Excel application","bytes":(D/IMAGE).stat().st_size}

def main():
    m,a,dms,blocks=read_source()
    info=refresh(m,a,dms,blocks)
    image=preview()
    record={
      "date":"2026-11-09","delivery":22,"status":"SCOPED_SOURCE_AND_WORKBOOK_VALIDATION_PASS",
      "source_commit":os.getenv("GITHUB_SHA","unavailable"),
      "source_master":"Master_Donor_Concept_to_DIM_Crosswalk.json",
      "source_first_evidence":AUDIT,"workbook":BOOK,
      **info,"preview":image,
      "counts":{"information_rows":329,"review_grid_rows":346,"columns":14,"DMS_outcomes":480,"source_supported":474,
        "precise_questions_open":6,"source_blocks":279,"source_text_reviewed":249,"DMS_heading_records":29,
        "2015_fulltext_access_HOLD":1,"source_first_targets":31,"earlier_findings":25,"qualified_correspondence":18,
        "no_established_correspondence":4,"case_holds":9,"design_holds":14,"donor_evidence":58,
        "case_evidence":73,"ISA_only_display_edits":29,"DIM_adopted":0},
      "checks":{"coverage_JSON_and_CSV_parity":True,"all_grid_cells_exact_after_XLSX_export":True,
        "all_26_original_worksheets_preserved_in_order":True,"non_updated_worksheet_XML_preserved":True,
        "original_ISA_source_questions_remain_unresolved":True,"zip_crc_and_xml_parse":True,
        "all_480_DMS_and_279_source_IDs_unique":True,"zero_runtime_conformance_claim":True},
      "not_checked":["Excel-native visual renderer","full independent original-source recensus",
         "full repository CI or physical equipment operation","2015 historical SPIE full article",
         "new standards/profile adoption or external interoperability"],
      "next_only_on_new_owner_proceed":"Original broader 40-step donor master Step16"}
    (D/OUT).write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    require(sha((D/BOOK).read_bytes())==info["workbook_sha256"],"final file readback")
    print("PASS ISA22: final 26-sheet XLSX rebuilt and verified",info["workbook_sha256"])
    print("PASS ISA22: original 480/279/31/25/six inventories and 58/73 cases preserved")
    print("PASS ISA22: preview from actual saved XLSX and exact all-grid-cell comparisons")
if __name__=="__main__":main()
