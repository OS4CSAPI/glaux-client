#!/usr/bin/env python3
"""Read-only independent validation of Step10 SensorML 3.0 crosswalk workbook.

Checks actual committed XLSX ZIP/XML and cell/evidence parity, NOT semantic
adoption or OGC conformance of a fielded SensorML producer.
"""
from pathlib import Path
import csv, json, zipfile, xml.etree.ElementTree as ET

ROOT=Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
NAME="Master_Donor_Concept_to_DIM_Crosswalk_v0.4_Step10_SensorML_06NOV2026"
BASE="Master_Donor_Concept_to_DIM_Crosswalk_v0.3_Step09_CSAPI_06NOV2026"
N="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
IDS="Dragino AirGradient Campbell Bennett IEEE OPC SAPIENT SOSA OMS SWE SensorML CSAPI DIM".split()

def check(cond,message):
    if not cond: raise AssertionError(message)

def scan(package,index,width):
    root=ET.fromstring(package.read(f"xl/worksheets/sheet{index}.xml"))
    output=[]
    for row in root.find(N+"sheetData").findall(N+"row"):
        vals=[""]*width
        for cell in row.findall(N+"c"):
            ref=cell.attrib["r"]
            col="".join(c for c in ref if c.isalpha())
            colid=0
            for c in col: colid=26*colid+ord(c)-64
            colid-=1
            check(0<=colid<width,f"cell {ref} outside worksheet")
            inline=cell.find(N+"is")
            vals[colid]="".join(t.text or "" for t in inline.iter(N+"t")) if inline is not None else ""
        output.append(vals)
    return root,output

def run():
    new=json.loads((ROOT/(NAME+".json")).read_text(encoding="utf-8"))
    old=json.loads((ROOT/(BASE+".json")).read_text(encoding="utf-8"))
    audit=json.loads((ROOT/"Step10_SensorML_3_Original_Clause_Audit_06NOV2026.json").read_text(encoding="utf-8"))
    with (ROOT/(NAME+".csv")).open(encoding="utf-8",newline="") as f: csvrows=list(csv.reader(f))
    md=(ROOT/(NAME+".md")).read_text(encoding="utf-8")
    check([x["key"] for x in new["columns"]]==IDS,"accepted 13-column order changed")
    check(new["columns"]==old["columns"],"the owner's column geometry or names changed")
    check(len(new["rows"])==len(old["rows"])==37,"22 proposed/9 held/6 section rows changed")
    check(len([r for r in new["rows"] if r["type"]=="element"])==22,"original proposed DIM rows changed")
    check(len([r for r in new["rows"] if r["type"]=="case_hold"])==9,"nine review holds changed")
    check(len([r for r in new["rows"] if r["type"]=="section"])==6,"six dividers changed")
    check(len(new["caseEvidence"])==73 and new["caseEvidence"]==old["caseEvidence"],"case evidence modified")
    check(len(new["originalDonorEvidence"])==53,"53 source mappings expected")
    check(len(audit["reviewedRows"])==10 and len(audit["heldNativeLeads"])==9,"SensorML audit sizes wrong")
    check(new["step10"]["nextStep"]=="STEP11_NOT_STARTED","Step11 started")
    check(len([r for r in new["originalDonorEvidence"] if r["donorKey"]=="SensorML"])==10,"10 SensorML rows expected")
    check(len([r for r in new["originalDonorEvidence"] if r["donorKey"]=="CSAPI"])==12,"12 CSAPI rows lost")
    other=[r for r in new["originalDonorEvidence"] if r["donorKey"] not in ("SensorML","CSAPI")]
    check(len(other)==31 and all(r["sourceVerification"]=="PRIOR_SOURCE_EXTRACT_ONLY" for r in other),
          "31 legacy other-source claims unexpectedly changed")
    untouchedNew=[r for r in new["originalDonorEvidence"] if r["donorKey"]!="SensorML"]
    untouchedOld=[r for r in old["originalDonorEvidence"] if r["donorKey"]!="SensorML"]
    check(untouchedNew==untouchedOld,"non-SensorML donor evidence was altered")
    sgrade="OGC_23_000_ORIGINAL_CLAUSE_AND_JSON_SCHEMA_CHECKED_DIM_RELATION_PROPOSED"
    check(all(r["sourceVerification"]==sgrade for r in new["originalDonorEvidence"] if r["donorKey"]=="SensorML"),
          "one SensorML clause was marked as checked without standing")
    checked={r["rowKey"]:r for r in audit["reviewedRows"]}
    check(len(checked)==10,"duplicate SensorML row audit")
    prev={r["rowKey"]:r for r in old["rows"] if r["type"]!="section"}
    newly=[r for r in audit["reviewedRows"] if r["isAddedPreviouslyUnpopulated"]]
    check({r["rowKey"] for r in newly}=={"S06-R009","S06-R013"},"expected two new source-supported correspondences")
    for row in new["rows"]:
        if row["type"]=="section":continue
        key=row["rowKey"]
        older=prev[key]
        check(row["type"]==older["type"] and row["dim"]==older["dim"],"DIM element or hold modified")
        check(row["display"][:10]==older["display"][:10] and row["display"][11:]==older["display"][11:],
              "non-SensorML columns changed on "+key)
        check(row["display"][9]=="","SWE Common populated prematurely")
        if row["type"]=="case_hold":
            check(all(not v for v in row["display"][4:12]),"review-only row silently adopted donor")
        if key in checked:
            record=checked[key]; claim=row["sourceClaims"]["SensorML"]
            check(claim["term"]==record["nativeTerm"] and claim["fit"]==record["relation"],"claim diff on "+key)
            check(row["display"][10]==(("≈ " if record["relation"]!="DIRECT" else "")+record["nativeTerm"]),
                  "visible SensorML cell mismatch on "+key)
        else:check(row["display"][10]==older["display"][10],"unreviewed SensorML cell changed "+key)
    header=["SOURCE EXAMPLES · documentary / historical","","","","OTHER DONOR STANDARDS · provisional","","",
            "FOUNDATIONAL SENSING / OBSERVATION","","","","","PROPOSED DIM"]
    expected=[header,[r["name"] for r in new["columns"]]]
    dividerRows=[]
    for row in new["rows"]:
        if row["type"]=="section":
            dividerRows.append(len(expected)+1)
            expected.append([row["title"]+" — "+row["description"]]+[""]*12)
        else:expected.append(row["display"])
    check(csvrows==expected,"the v0.4 CSV is not an exact JSON mirror")
    check(md.count('colspan="13"')==6,"GitHub markdown dividers mismatch")
    with zipfile.ZipFile(ROOT/(NAME+".xlsx")) as xlsx, zipfile.ZipFile(ROOT/(BASE+".xlsx")) as oldxlsx:
        check(xlsx.testzip() is None,"v0.4 ZIP CRC invalid")
        for path in xlsx.namelist():
            if path.endswith(".xml") or path.endswith(".rels"):
                ET.fromstring(xlsx.read(path))
        workbook=ET.fromstring(xlsx.read("xl/workbook.xml"))
        actual=[x.attrib["name"] for x in workbook.find(N+"sheets").findall(N+"sheet")]
        check(actual==["Master Crosswalk","Case Evidence","Donor Evidence","DIM Definitions",
              "Sources & Editions","Holds & Decisions","Read Me","CSAPI Clause Audit","SensorML Clause Audit"],
              "nine worksheet identities/order incorrect")
        root,main=scan(xlsx,1,13)
        check(main==expected,"actual committed workbook main cells disagree with source/CSV")
        merges=[x.attrib["ref"] for x in root.find(N+"mergeCells").findall(N+"mergeCell")]
        check(merges==["A1:D1","E1:G1","H1:L1"]+[f"A{i}:M{i}" for i in dividerRows],
              "accepted grouped/section formatting lost")
        check(xlsx.read("xl/worksheets/sheet2.xml")==oldxlsx.read("xl/worksheets/sheet2.xml"),
              "original case evidence tab was modified")
        check(xlsx.read("xl/worksheets/sheet8.xml")==oldxlsx.read("xl/worksheets/sheet8.xml"),
              "prior CSAPI clause audit tab was modified")
        _,case=scan(xlsx,2,9);check(len(case)==74,"case evidence tab missing rows")
        donorRoot,donor=scan(xlsx,3,11);check(len(donor)==54,"Donor Evidence tab must have 53+header rows")
        for i,e in enumerate(new["originalDonorEvidence"],start=1):
            r=donor[i]
            check(r[0]==e["rowKey"] and r[3]==e["nativeTerm"] and r[4]==e["relation"] and
                  r[5]==e["sourceVerification"] and r[6]==e["sourceEdition"] and
                  r[7]==e["sourceLocator"] and r[8]==e["originalSourceUrl"] and
                  r[9]==e["nonEquivalenceWarning"],"donor evidence row mismatch at "+str(i+1))
        check(len(donorRoot.find(N+"hyperlinks").findall(N+"hyperlink"))==53,
              "53 original source hyperlinks missing")
        _,defs=scan(xlsx,4,7);check(len(defs)==32,"DIM Definitions tab cardinality")
        for k in ("S06-R009","S06-R013"):
            row=next(r for r in defs if r[0]==k)
            check(int(row[6])==len([e for e in new["originalDonorEvidence"] if e["rowKey"]==k]),
                  "DIM definition donor counts not refreshed for "+k)
        _,sources=scan(xlsx,5,7);check(len(sources)==14,"Sources & Editions rows changed")
        _,holds=scan(xlsx,6,5);check(len(holds)==16,"historical Holds & Decisions changed")
        _,readme=scan(xlsx,7,2);check(len(readme)==18,"Read Me missing")
        _,csapi=scan(xlsx,8,10);check(len(csapi)==21,"prior CSAPI Clause Audit modified")
        auditRoot,sml=scan(xlsx,9,10)
        check(len(sml)==20,"SensorML audit needs 10 checked +9 held + header")
        check(sum(r[0]=="SOURCE TERM CHECKED" for r in sml[1:])==10,"ten SensorML source terms missing")
        check(sum(r[0]=="ORIGINAL SOURCE LEAD HELD" for r in sml[1:])==9,"nine SensorML held source leads missing")
        check(len(auditRoot.find(N+"hyperlinks").findall(N+"hyperlink"))==29,"SensorML source/schema hyperlinks missing")
    print("PASS: genuine nine-sheet Step10 XLSX; unchanged 13 owner columns, 6 section dividers; 22 proposed DIM rows, 9 holds; 10 source-checked SensorML mappings (8 revised, 2 new) and 9 native leads held; 12 CSAPI mappings preserved, 31 other donor extracts unchanged, 73 case records untouched; JSON/CSV/Markdown/ZIP/XML/evidence parity.")
    print("LIMIT: source term/schema checked, NOT adoption or an OGC producer/app interoperability conformance test.")

if __name__=="__main__":
    run()
