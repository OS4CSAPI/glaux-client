#!/usr/bin/env python3
"""Read-only Step11 validation: source-checked SWE Common 3.0 workbook and evidence.

Checks actual ZIP/XML, 10 sheets and exact workbook/CSV/JSON parity.
Does NOT certify original publisher semantics, DIM adoption or deployed
OGC service/client conformance.
"""
import csv
import json
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

ROOT=Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
NEW="Master_Donor_Concept_to_DIM_Crosswalk_v0.5_Step11_SWECommon_06NOV2026"
BASE="Master_Donor_Concept_to_DIM_Crosswalk_v0.4_Step10_SensorML_06NOV2026"
NS="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
KEYS="Dragino AirGradient Campbell Bennett IEEE OPC SAPIENT SOSA OMS SWE SensorML CSAPI DIM".split()
GRADE="OGC_24_014_ORIGINAL_CLAUSE_JSON_SCHEMA_CHECKED_DIM_RELATION_PROPOSED"

def need(ok,reason):
    if not ok: raise AssertionError(reason)

def sheet(z,idx,width):
    root=ET.fromstring(z.read("xl/worksheets/sheet%d.xml" % idx))
    result=[]
    for row in root.find(NS+"sheetData").findall(NS+"row"):
        out=[""]*width
        for cell in row.findall(NS+"c"):
            ident=cell.attrib["r"]
            letters="".join(c for c in ident if c.isalpha())
            n=0
            for c in letters: n=26*n+ord(c)-64
            n-=1
            need(0<=n<width,"Invalid cell reference "+ident)
            value=cell.find(NS+"is")
            if value is not None:
                out[n]="".join(x.text or "" for x in value.iter(NS+"t"))
        result.append(out)
    return root,result

def main():
    new=json.loads((ROOT/(NEW+".json")).read_text(encoding="utf-8"))
    old=json.loads((ROOT/(BASE+".json")).read_text(encoding="utf-8"))
    audit=json.loads((ROOT/"Step11_SWE_Common_3_Original_Clause_Audit_06NOV2026.json").read_text(encoding="utf-8"))
    with (ROOT/(NEW+".csv")).open(newline="",encoding="utf-8") as f:
        csvrows=list(csv.reader(f))
    md=(ROOT/(NEW+".md")).read_text(encoding="utf-8")

    need([c["key"] for c in new["columns"]]==KEYS,"13-col owner-approved order changed")
    need(old["columns"]==new["columns"],"Column data/geometry not preserved")
    need(len(new["rows"])==len(old["rows"])==37,"Expected 6 section + 22 original + 9 case-only rows")
    need(len([r for r in new["rows"] if r["type"]=="element"])==22,"DIM row proposals altered")
    need(len([r for r in new["rows"] if r["type"]=="case_hold"])==9,"Case-only review holds altered")
    need(len([r for r in new["rows"] if r["type"]=="section"])==6,"Section bands changed")
    need(new["caseEvidence"]==old["caseEvidence"] and len(new["caseEvidence"])==73,"Case evidence mutated")
    need(len(new["originalDonorEvidence"])==57,"Expected 53 old + 4 SWE correspondence records")
    need(len(audit["reviewedRows"])==4 and len(audit["sourceNativeHolds"])==13,"SWE review/held record counts wrong")
    need(new["step11"]["nextStep"]=="STEP12_NOT_STARTED","Step12 already started")
    need(new["ownerDecision"].startswith("STEP08_WORKING_COLUMN_LAYOUT_ACCEPTED"),"Owner layout status was lost")

    unalteredOld=[x for x in old["originalDonorEvidence"] if x["donorKey"]!="SWE"]
    unalteredNew=[x for x in new["originalDonorEvidence"] if x["donorKey"]!="SWE"]
    need(unalteredOld==unalteredNew,"Other donor evidence records not byte-equivalent")
    swe=[x for x in new["originalDonorEvidence"] if x["donorKey"]=="SWE"]
    need(len(swe)==4 and all(x["sourceVerification"]==GRADE and
         x["disposition"]=="PROPOSED_NOT_ADOPTED" for x in swe),"SWE source verification status wrong")
    need(len([e for e in new["originalDonorEvidence"] if e["donorKey"]=="CSAPI"])==12,"CSAPI original-source terms lost")
    need(len([e for e in new["originalDonorEvidence"] if e["donorKey"]=="SensorML"])==10,"SensorML original-source terms lost")
    need(len([e for e in new["originalDonorEvidence"] if e["donorKey"] not in
         ("SWE","CSAPI","SensorML") and e["sourceVerification"]=="PRIOR_SOURCE_EXTRACT_ONLY"])==31,
         "Other previous-source-only cells wrongly upgraded")
    reviewed={x["rowKey"]:x for x in audit["reviewedRows"]}
    need(set(reviewed)=={"S06-R012","S06-R013","S06-R016","S06-R018"},
         "Unreviewed SWE cells added")
    earlier={r["rowKey"]:r for r in old["rows"] if r["type"]!="section"}
    for r in new["rows"]:
        if r["type"]=="section":continue
        prior=earlier[r["rowKey"]]
        need(r["dim"]==prior["dim"] and r["type"]==prior["type"],"Proposed DIM row changed")
        need(len(r["display"])==13,"DIM row width !=13")
        need(r["display"][:9]==prior["display"][:9] and r["display"][10:]==prior["display"][10:],
             "Non-SWE source/example/DIM column changed: "+r["rowKey"])
        if r["type"]=="case_hold":
            need(not any(r["display"][4:12]),"Held case row accidentally populated with donor claim")
        elif r["rowKey"] in reviewed:
            claim=r["sourceClaims"]["SWE"]
            rec=reviewed[r["rowKey"]]
            need(claim["term"]==rec["nativeTerm"] and claim["fit"]==rec["relation"],
                 "SWE data source mismatch "+r["rowKey"])
            need(r["display"][9]==(("≈ " if rec["relation"]!="DIRECT" else "")+rec["nativeTerm"]),
                 "SWE display cell wrong on "+r["rowKey"])
        else:
            need(r["display"][9]==prior["display"][9]=="","Unreviewed SWE donor cell changed")

    heading=["SOURCE EXAMPLES · documentary / historical","","","","OTHER DONOR STANDARDS · provisional","","",
             "FOUNDATIONAL SENSING / OBSERVATION","","","","","PROPOSED DIM"]
    grid=[heading,[c["name"] for c in new["columns"]]]
    bands=[]
    for row in new["rows"]:
        if row["type"]=="section":
            bands.append(len(grid)+1)
            grid.append([row["title"]+" — "+row["description"]]+[""]*12)
        else:grid.append(row["display"])
    need(csvrows==grid,"CSV not identical to structured JSON field grid")
    need(md.count('colspan="13"')==6,"Markdown full-width band count wrong")

    with zipfile.ZipFile(ROOT/(NEW+".xlsx")) as z, zipfile.ZipFile(ROOT/(BASE+".xlsx")) as baseline:
        need(z.testzip() is None,"ZIP CRC corrupted")
        for f in z.namelist():
            if f.endswith(".xml") or f.endswith(".rels"):
                ET.fromstring(z.read(f))
        book=ET.fromstring(z.read("xl/workbook.xml"))
        names=[x.attrib["name"] for x in book.find(NS+"sheets").findall(NS+"sheet")]
        need(names==["Master Crosswalk","Case Evidence","Donor Evidence","DIM Definitions",
                    "Sources & Editions","Holds & Decisions","Read Me","CSAPI Clause Audit",
                    "SensorML Clause Audit","SWE Common Clause Audit"],
             "Expected 10 worksheets with original evidence sheets preserved")
        root,main=sheet(z,1,13)
        need(main==grid,"Actual XLSX main cells disagree with JSON/CSV")
        merges=[x.attrib["ref"] for x in root.find(NS+"mergeCells").findall(NS+"mergeCell")]
        need(merges==["A1:D1","E1:G1","H1:L1"]+[f"A{i}:M{i}" for i in bands],
             "Approved column bands or section dividers modified")
        for i in (2,8,9):
            need(z.read("xl/worksheets/sheet%d.xml" % i)==baseline.read("xl/worksheets/sheet%d.xml" % i),
                 "Previous equipment/CSAPI/SensorML evidence sheet changed at tab "+str(i))
        _,case=sheet(z,2,9)
        need(len(case)==74,"73 source case rows missing")
        droot,donor=sheet(z,3,11)
        need(len(donor)==58,"Expected 57 donor evidence records plus header")
        for i,x in enumerate(new["originalDonorEvidence"],start=1):
            row=donor[i]
            need(row[0]==x["rowKey"] and row[3]==x["nativeTerm"] and
                 row[4]==x["relation"] and row[5]==x["sourceVerification"] and
                 row[6]==x["sourceEdition"] and row[7]==x["sourceLocator"] and
                 row[8]==x["originalSourceUrl"] and row[9]==x["nonEquivalenceWarning"],
                 "Donor Evidence mismatch at Excel row "+str(i+1))
        need(len(droot.find(NS+"hyperlinks").findall(NS+"hyperlink"))==57,"Donor Evidence source hyperlinks incomplete")
        _,defs=sheet(z,4,7)
        need(len(defs)==32,"DIM Definitions row count unexpectedly changed")
        for key in reviewed:
            row=next(r for r in defs if r[0]==key)
            n=sum(e["rowKey"]==key for e in new["originalDonorEvidence"])
            need(int(row[6])==n,"DIM source count wrong for "+key)
        _,sources=sheet(z,5,7)
        need(len(sources)==14 and "4 SWE Common clauses checked" in sources[10][6],"Sources tab missing current SWE standing")
        _,holds=sheet(z,6,5)
        need(len(holds)==16,"Holds tab changed unexpectedly")
        _,readme=sheet(z,7,2)
        need(len(readme)==18,"ReadMe tab changed structure")
        _,saudit=sheet(z,10,10)
        need(len(saudit)==18,"SWE original-clause audit has wrong row count")
        need(sum(r[0]=="SOURCE TERM CHECKED" for r in saudit[1:])==4,"Four reviewed SWE terms missing")
        need(sum(r[0]=="SOURCE LEAD HELD" for r in saudit[1:])==13,"Thirteen SWE source-native holds missing")
        sweRoot=ET.fromstring(z.read("xl/worksheets/sheet10.xml"))
        need(len(sweRoot.find(NS+"hyperlinks").findall(NS+"hyperlink"))==34,
             "OGC source/schema links missing from SWE audit")
    print("PASS: real 10-sheet Step11 SWE Common 3.0 master ZIP/XML; 13-column approved layout and 6 sections intact; 4 qualified SWE cells, 13 native-source holds, 22 proposed DIM rows, 9 case holds, 73 original case entries, 12 CSAPI+10 SensorML previous source checks and 31 historical other donors intact; JSON/CSV/workbook parity.")
    print("LIMIT: document term/schema checked, not an OGC conformance test, adopted DIM or authenticated operational source evidence.")

if __name__=="__main__":
    main()
