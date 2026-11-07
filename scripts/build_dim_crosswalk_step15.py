#!/usr/bin/env python3
"""ISA 6.0 Step15: source-derived, owner-reviewable staged workbook.
Keeps all thirteen accepted main columns and existing sheets untouched.
Adds a source audit and a fourteen-column PROPOSED ISA overlay for Step16.
"""
from pathlib import Path
from xml.etree import ElementTree as ET
import copy,csv,html,json,zipfile

D=Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
OLD="Master_Donor_Concept_to_DIM_Crosswalk_v0.8_Step14_IEEE1451_06NOV2026"
NEW="Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026"
OVER="Step15_ISA_6_Proposed_14_Column_Overlay_07NOV2026"
AUD="Step15_ISA_6_Original_Source_Clause_Audit_07NOV2026"
STAGE="Step15_ISA6_Primary_Source_Staging_07NOV2026"
X="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
P="http://schemas.openxmlformats.org/package/2006/relationships"
CT="http://schemas.openxmlformats.org/package/2006/content-types"
EP="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
VT="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"
q=lambda x:"{"+X+"}"+x
ET.register_namespace("",X)
ET.register_namespace("r",R)
ET.register_namespace("vt",VT)

def need(condition,message):
    if not condition:raise AssertionError(message)

def raw(root):
    return ET.tostring(root,encoding="utf-8",xml_declaration=True)

def a1(index):
    n=index+1
    letters=""
    while n:
        n,x=divmod(n-1,26)
        letters=chr(65+x)+letters
    return letters

def emit_cell(row,col,value,header=False):
    c=ET.SubElement(row,q("c"),{"r":a1(col)+row.attrib["r"],"t":"inlineStr"})
    if header:c.set("s","1")
    i=ET.SubElement(c,q("is"))
    t=ET.SubElement(i,q("t"))
    text=str(value if value is not None else "")
    t.text=text
    if text[:1].isspace() or text[-1:].isspace():
        t.set("{http://www.w3.org/XML/1998/namespace}space","preserve")

def worksheet(values,widths,freeze,merged=None):
    need(all(len(row)==len(widths) for row in values),"Sheet column width mismatch")
    root=ET.Element(q("worksheet"))
    ET.SubElement(root,q("dimension"),{"ref":"A1:"+a1(len(widths)-1)+str(len(values))})
    views=ET.SubElement(root,q("sheetViews"))
    view=ET.SubElement(views,q("sheetView"),{"workbookViewId":"0"})
    ET.SubElement(view,q("pane"),{
        "ySplit":str(freeze),"topLeftCell":"A"+str(freeze+1),
        "activePane":"bottomLeft","state":"frozen"
    })
    ET.SubElement(root,q("sheetFormatPr"),{"defaultRowHeight":"18"})
    cols=ET.SubElement(root,q("cols"))
    for index,width in enumerate(widths,start=1):
        ET.SubElement(cols,q("col"),{
            "min":str(index),"max":str(index),"width":str(width),"customWidth":"1"
        })
    sheet=ET.SubElement(root,q("sheetData"))
    for i,data in enumerate(values,start=1):
        row=ET.SubElement(sheet,q("row"),{
            "r":str(i),"ht":str(30 if i<=freeze else 55),"customHeight":"1"
        })
        for col,value in enumerate(data):emit_cell(row,col,value,header=i<=freeze)
    if merged:
        box=ET.SubElement(root,q("mergeCells"),{"count":str(len(merged))})
        for item in merged:ET.SubElement(box,q("mergeCell"),{"ref":item})
    ET.SubElement(root,q("pageMargins"),{
        "left":"0.3","right":"0.3","top":"0.6","bottom":"0.6",
        "header":"0.3","footer":"0.3"
    })
    return raw(root)

def preview(old,stage):
    main=old["columns"]
    need(len(main)==13 and main[-1]["key"]=="DIM" and main[7]["key"]=="SOSA",
         "Main owner-accepted column order changed")
    cols=main[:7]+[{
        "key":"ISA","name":"ISA 6.0 (proposed, source-checked)",
        "group":"OTHER_DONOR_STANDARDS","kind":"PROPOSED_NOT_ACCEPTED"
    }]+main[7:]
    known={x["rowKey"]:x for x in stage["mappings"]}
    rows=[]
    for row in old["rows"]:
        if row["type"]=="section":
            rows.append(dict(row))
            continue
        mapped=known.get(row["rowKey"])
        value=("≈ "+mapped["nativeTerm"]) if mapped else ""
        new=copy.deepcopy(row)
        new["display"]=row["display"][:7]+[value]+row["display"][7:]
        rows.append(new)
    need(all(len(r["display"])==14 for r in rows if r["type"]!="section"),
         "Preview donor geometry must be fourteen columns")
    return cols,rows

def matrix(cols,rows,proposed=False):
    if proposed:
        headline=["SOURCE CASES / documentary","", "", "",
                  "OTHER DONORS / ISA PROVISIONAL","","","",
                  "FOUNDATIONAL SENSING/OBSERVATION","","","","","PROPOSED DIM"]
    else:
        headline=["SOURCE EXAMPLES / documentary","","","",
                  "OTHER DONOR STANDARDS / provisional","","",
                  "FOUNDATIONAL SENSING/OBSERVATION","","","","","PROPOSED DIM"]
    data=[headline,[x["name"] for x in cols]]
    sections=[]
    for row in rows:
        if row["type"]=="section":
            sections.append(len(data)+1)
            data.append([row["title"]+" — "+row["description"]]+[""]*(len(cols)-1))
        else:data.append(row["display"])
    return data,sections

def html_preview(cols,rows):
    esc=lambda s:html.escape(str(s),quote=True)
    out=[
      "<table>",
      '<thead><tr><th colspan="4">SOURCE CASES</th>'
      '<th colspan="4">OTHER DONORS — ISA PROPOSED</th>'
      '<th colspan="5">FOUNDATIONAL STANDARDS</th><th>PROPOSED DIM</th></tr>',
      "<tr>"+"".join("<th>"+esc(x["name"])+"</th>" for x in cols)+"</tr></thead><tbody>"
    ]
    for row in rows:
        if row["type"]=="section":
            out.append('<tr><th colspan="14">'+esc(row["title"]+" — "+row["description"])+"</th></tr>")
        else:
            out.append("<tr>"+"".join("<td>"+(
                "<strong>"+esc(v)+"</strong>" if n==13 else esc(v)
            )+"</td>" for n,v in enumerate(row["display"]))+"</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)+"\n"

def store_csv(path,records):
    with path.open("w",encoding="utf-8",newline="") as handle:
        csv.writer(handle,lineterminator="\r\n").writerows(records)

def audit_rows(old,stage):
    name={x["rowKey"]:x["dim"] for x in old["rows"] if x.get("rowKey")}
    files={x["id"]:x["filename"] for x in stage["documents"]}
    rows=[[
        "Evidence grade","DIM row / hold","Source-native ISA concept",
        "Fit / status","Exact original ISA clause/page","Original 2023 PDF",
        "Original meaning","Non-equivalence warning","Public context, NOT original PDF"
    ]]
    for item in stage["mappings"]:
        rows.append([
            "ORIGINAL 2023 CLAUSE CHECKED / STAGED",
            item["rowKey"]+" — "+name[item["rowKey"]],
            item["nativeTerm"],item["relation"],item["sourceLocator"],
            "; ".join(files[x] for x in item["documentIds"]),
            item["originalMeaning"],item["nonEquivalenceWarning"],
            stage["sideContext"][0]
        ])
    for item in stage["holds"]:
        rows.append([
            "ORIGINAL 2023 SOURCE HOLD",item["rowOrHold"],item["nativeTerm"],
            "HELD",item["sourceLocator"],"ISA 6.0 Distribution A original",
            "Original-source distinction reserved for synthesis",
            item["reason"],stage["sideContext"][0]
        ])
    need(len(rows)==26,"Expected eleven mapped and fourteen held ISA source records")
    return rows

def extend_wb(base,new_ids):
    root=ET.fromstring(base)
    sheets=root.find(q("sheets"))
    need(len(sheets.findall(q("sheet")))==13,"Expect source workbook thirteen sheets")
    for n,id_,title in [
        (14,new_ids[0],"ISA Original Clause Audit"),
        (15,new_ids[1],"ISA Proposed Overlay")
    ]:
        ET.SubElement(sheets,q("sheet"),{
            "name":title,"sheetId":str(n),"{"+R+"}id":id_
        })
    return raw(root)

def extend_rel(base,new_ids):
    root=ET.fromstring(base)
    for i,id_ in enumerate(new_ids,start=14):
        ET.SubElement(root,"{"+P+"}Relationship",{
            "Id":id_,"Type":R+"/worksheet",
            "Target":"worksheets/sheet"+str(i)+".xml"
        })
    return raw(root)

def extend_types(base):
    root=ET.fromstring(base)
    for i in [14,15]:
        ET.SubElement(root,"{"+CT+"}Override",{
            "PartName":"/xl/worksheets/sheet"+str(i)+".xml",
            "ContentType":"application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"
        })
    return raw(root)

def extend_properties(base):
    root=ET.fromstring(base)
    headings=root.find("{"+EP+"}HeadingPairs")
    if headings is not None:
        for n in headings.iter("{"+VT+"}i4"):
            if n.text=="13":n.text="15";break
    titles=root.find("{"+EP+"}TitlesOfParts")
    if titles is not None:
        vector=titles.find("{"+VT+"}vector")
        if vector is not None:
            for name in ["ISA Original Clause Audit","ISA Proposed Overlay"]:
                ET.SubElement(vector,"{"+VT+"}lpstr").text=name
            vector.set("size",str(len(vector)))
    return raw(root)

def build_workbook(old,stage,cols,rows,bands):
    proposed,_=matrix(cols,rows,True)
    merged=["A1:D1","E1:H1","I1:M1"]+[
        "A"+str(i)+":N"+str(i) for i in bands
    ]
    audit_xml=worksheet(
        audit_rows(old,stage),
        [32,37,43,20,73,59,81,90,82],1
    )
    overlay_xml=worksheet(
        proposed,
        [32,33,42,37,34,30,30,46,34,35,34,35,38,50],2,merged
    )
    path=D/(OLD+".xlsx")
    out=D/(NEW+".xlsx")
    with zipfile.ZipFile(path) as oldfile:
        need(oldfile.testzip() is None,"Previous workbook ZIP damaged")
        rels=ET.fromstring(oldfile.read("xl/_rels/workbook.xml.rels"))
        used={x.get("Id") for x in rels}
        ids=[];n=15
        while len(ids)<2:
            id_="rId"+str(n)
            if id_ not in used:ids.append(id_)
            n+=1
        changes={
            "xl/workbook.xml":extend_wb(oldfile.read("xl/workbook.xml"),ids),
            "xl/_rels/workbook.xml.rels":extend_rel(
                oldfile.read("xl/_rels/workbook.xml.rels"),ids
            ),
            "[Content_Types].xml":extend_types(
                oldfile.read("[Content_Types].xml")
            )
        }
        if "docProps/app.xml" in oldfile.namelist():
            changes["docProps/app.xml"]=extend_properties(
                oldfile.read("docProps/app.xml")
            )
        with zipfile.ZipFile(out,"w") as file:
            for member in oldfile.infolist():
                file.writestr(
                    member,changes.get(member.filename,oldfile.read(member.filename))
                )
            for path,payload in [
                ("xl/worksheets/sheet14.xml",audit_xml),
                ("xl/worksheets/sheet15.xml",overlay_xml)
            ]:
                info=zipfile.ZipInfo(path,date_time=(1980,1,1,0,0,0))
                info.compress_type=zipfile.ZIP_DEFLATED
                file.writestr(info,payload)
    with zipfile.ZipFile(out) as generated,zipfile.ZipFile(path) as oldfile:
        need(generated.testzip() is None,"Generated workbook ZIP invalid")
        for name in generated.namelist():
            if name.endswith(".xml") or name.endswith(".rels"):
                ET.fromstring(generated.read(name))
        for i in range(1,14):
            name="xl/worksheets/sheet"+str(i)+".xml"
            need(generated.read(name)==oldfile.read(name),
                 "Earlier worksheet changed: "+name)
    return out

def audit_markdown(stage,old):
    names={x["rowKey"]:x["dim"] for x in old["rows"] if x.get("rowKey")}
    docs="\n".join(
        "| "+x["title"]+" | "+x["edition"]+" | "+x["filename"]+" |"
        for x in stage["documents"]
    )
    mappings="\n".join(
        "| "+names[r["rowKey"]]+" | "+r["nativeTerm"]+" | "+r["relation"]+
        " | "+r["sourceLocator"]+" | "+r["nonEquivalenceWarning"]+" |"
        for r in stage["mappings"]
    )
    holds="\n".join(
        "| "+r["nativeTerm"]+" | "+r["sourceLocator"]+" | "+r["reason"]+" |"
        for r in stage["holds"]
    )
    return f"""# Step15 — Integrated Sensor Architecture (ISA) 6.0 original-source audit

**7 November 2026.** Examined textual pages of five original October 2023 ISA 6.0 Distribution Statement A project-uploaded PDFs. Eleven source-native candidate correspondences are staged and fourteen native-source distinctions held. The original source PDFs are not republished on GitHub because raw materialization was unavailable.

## Primary source documents and editions

| ISA original | Exact source edition (31 October 2023) | Prior project file |
|---|---|---|
{docs}

**Important:** A current 2026 Army Summit report and earlier 2023 Army public overview support context only; these do NOT replace the original 6.0 text. The ISA documents have different revision suffixes within release 6.0.

## Eleven source-checked mappings to existing proposed DIM rows

| Proposed DIM information element | ISA original term | Fit | Original clause and printed/PDF page | Boundary |
|---|---|---|---|---|
{mappings}

These are source-to-DIM research proposals, not ISA-authored equivalence declarations, adopted DIM elements or formal test results. Composition member and virtual/opaque/visible semantics must not be reduced to physical enclosure or individually installed hardware.

## Fourteen source-native ISA concepts deliberately held

| ISA original concept | Original clause and page | Why held |
|---|---|---|
{holds}

The Data Model Specification explicitly differentiates Custom, Nominated and Accepted nonstandard extension entries. A new data model extension is not necessarily a core adopted ISA data type.

## Four original case falsification checks

**Dragino:** one external SHT31 carrying temperature/humidity does not imply a particular ISA CIC or virtual component. **AirGradient:** two PMS5003 modules at PM1/PM2 sockets do not become three physical sensors because three particulate outputs exist. **Campbell:** fourteen ClimaVue response positions and thirty-one separate logger Status example fields do not prove an installed ISA Config/Status/Event producer. **Bennett:** the real historical station has two serial-numbered EE181 probes across three dated service-role statements and two original NOAA temperature means represented by four experimental API copies. The original resultTime is UNKNOWN, the source QA text including its trailing space remains intact, and a station site coordinate is not a surveyed probe point.

## Workbook disposition and Step16 owner checkpoint

The approved primary workbook remains 13 columns, 22 proposed DIM rows, nine case-only holds, 73 source-qualified cases, and 58 prior donor correspondence records (37 earlier original-standard-source-checked, 6 IEEE public-technical-only, 15 OPC/SAPIENT prior-only). The eleven ISA original-source-backed records are staged separately and do not inflate those primary totals.

The new v0.9 workbook includes both an ISA Original Clause Audit worksheet and the full 14-column ISA Proposed Overlay worksheet, in addition to all unchanged prior worksheets. A GitHub-readable 14-column overlay and CSV also exist. The candidate ISA column is not part of the accepted primary master until owner review.

**NEXT:** Step16 owner checkpoint only. Decide whether the ISA donor column and any previously held unique concepts should be promoted, adjusted or rejected. Step17 The Open Group SOSA is not started.

## Public contextual evidence (not the primary source PDFs)

U.S. Army, February 6, 2023: https://www.army.mil/article/263782/armys_interoperable_sensors_solution_keeps_military_modernization_efforts_on_track

U.S. Army / DVIDS, July 14, 2026: https://www.dvidshub.net/news/printable/569918
"""

def main():
    old=json.loads((D/(OLD+".json")).read_text(encoding="utf-8"))
    stage=json.loads((D/(STAGE+".json")).read_text(encoding="utf-8"))
    need(len(stage["mappings"])==11 and len(stage["holds"])==14
         and len(stage["documents"])==5,"Original ISA source decisions missing")
    cols,rows=preview(old,stage)
    need(len(cols)==14 and len(rows)==37,"Unexpected ISA preview")
    modified=copy.deepcopy(old)
    modified.update({
        "schemaVersion":"donor-dim-master-layout.v0.9-step15-isa-original-staged",
        "date":"2026-11-07",
        "previousWorkingMaster":OLD+".json",
        "scope":"STEP15_ISA6_11_SOURCE_CHECKED_STAGED_14_HELD_MAIN_OWNER_13_COL_UNCHANGED"
    })
    modified["counts"].update({
        "ISAStagedOriginalSourceCheckedMappings":11,
        "ISANativeSourceLeadsHeld":14,
        "ISAPreviewColumns":14,
        "ISAOriginalDocumentsReviewed":5
    })
    modified["step15"]={
        "status":"ORIGINAL_2023_SOURCE_EVIDENCE_STAGED_XLSX_VALIDATION_PENDING",
        "sourceGrade":stage["sourceGrade"],
        "sourceDocuments":stage["documents"],
        "proposedMappingRecords":stage["mappings"],
        "nativeHolds":stage["holds"],
        "acceptedMainColumnKeys":[x["key"] for x in old["columns"]],
        "stagedPreviewColumnKeys":[x["key"] for x in cols],
        "mainPrimaryDonorCellCount":58,
        "requiresOwnerAcceptanceForPromotion":True,
        "sourceAccess":stage["sourceAccess"],
        "nextStep":"STEP16_OWNER_CHECKPOINT_NOT_STARTED_REQUIRES_SEPARATE_PROCEED"
    }
    need(modified["columns"]==old["columns"] and
         modified["rows"]==old["rows"] and
         modified["originalDonorEvidence"]==old["originalDonorEvidence"] and
         modified["caseEvidence"]==old["caseEvidence"] and
         modified["originalSourceInputHashes"]==old["originalSourceInputHashes"],
         "Primary master evidence was unexpectedly altered")
    (D/(NEW+".json")).write_text(
        json.dumps(modified,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"
    )
    (D/(AUD+".json")).write_text(
        json.dumps(stage,indent=2,ensure_ascii=False)+"\n",encoding="utf-8"
    )
    accepted,_=matrix(old["columns"],old["rows"],False)
    expanded,sections=matrix(cols,rows,True)
    store_csv(D/(NEW+".csv"),accepted)
    store_csv(D/(OVER+".csv"),expanded)
    oldmd=(D/(OLD+".md")).read_text(encoding="utf-8")
    need("<table>" in oldmd,"Original accepted GitHub table missing")
    originalTable=oldmd[oldmd.index("<table>"):]
    acceptedMD=f"""# Source cases to donor standards to proposed DIM — ISA Step15 staged audit

**7 November 2026.** The owner-accepted 13-column primary master below stays exactly as previously approved. The original 2023 ISA documents establish eleven source-qualified proposed correspondences and fourteen native holds; the ISA column is presented in a separate 14-column owner review overlay, not silently promoted to this primary master.

**Primary data unchanged:** 58 previous donor evidence records, 37 original OGC/W3C checked + 6 IEEE public-technical-only + 15 prior-only; 73 source-case statements; 22 proposed DIM rows; nine case-only holds. Eleven ISA source-checked records are STAGED SEPARATELY.

[Full 14-column ISA proposed overlay]({OVER}.md) · [Current editable 15-sheet v0.9 Excel workbook]({NEW}.xlsx) · [Original ISA audit]({AUD}.md) · [Original ISA evidence JSON]({AUD}.json).

{originalTable}"""
    (D/(NEW+".md")).write_text(acceptedMD,encoding="utf-8")
    proposedMD=f"""# ISA 6.0 proposed 14-column horizontal crosswalk overlay — Step16 owner review

**PROVISIONAL REVIEW ONLY.** Four cases remain left, the new ISA donor candidate follows SAPIENT, the five foundational sensing/observation standards stay grouped, and proposed DIM remains rightmost. Eleven ISA candidate cells are grounded in original 2023 source clauses; all other donor/case rows are preserved. Blanks are unresolved correspondences, not proof of absence.

[Primary accepted 13-column master]({NEW}.md) · [Original ISA clause audit]({AUD}.md) · [Overlay CSV]({OVER}.csv) · [Editable 15-sheet workbook]({NEW}.xlsx).

{html_preview(cols,rows)}"""
    (D/(OVER+".md")).write_text(proposedMD,encoding="utf-8")
    (D/(AUD+".md")).write_text(audit_markdown(stage,old),encoding="utf-8")
    output=build_workbook(old,stage,cols,rows,sections)
    print("PASS: 15-sheet v0.9 ISA original-source reviewed staged workbook",output.stat().st_size)
    print("PASS: accepted 13-column main with original 13 worksheets byte preserved")
    print("PASS: eleven proposed ISA mappings, fourteen native holds, full 14-column review overlay")
    print("LIMIT: no new adopted DIM, owner column acceptance, runtime, command or conformance result")

if __name__=="__main__":main()
