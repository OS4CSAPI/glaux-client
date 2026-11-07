#!/usr/bin/env python3
"""Step09 read-only validation of committed source-checked CSAPI workbook and mirrors.

Tests structural/source-record integrity only. It DOES NOT establish semantic
adoption, OGC server conformance, or source publisher authenticity.
"""
import csv
import json
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

ROOT=Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
NAME="Master_Donor_Concept_to_DIM_Crosswalk_v0.3_Step09_CSAPI_06NOV2026"
N="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
EXPECTED_KEYS="Dragino AirGradient Campbell Bennett IEEE OPC SAPIENT SOSA OMS SWE SensorML CSAPI DIM".split()
COLS={c:i for i,c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}

def need(condition,msg):
    if not condition: raise AssertionError(msg)

def sheet(package,number,width):
    r=ET.fromstring(package.read(f"xl/worksheets/sheet{number}.xml"))
    rows=[]
    for el in r.find(N+"sheetData").findall(N+"row"):
        values=[""]*width
        for cell in el.findall(N+"c"):
            ref=cell.attrib["r"]
            letters="".join(c for c in ref if c.isalpha())
            j=0
            for c in letters:j=j*26+ord(c)-64
            j-=1
            need(0<=j<width,"cell outside worksheet "+ref)
            inline=cell.find(N+"is")
            values[j]="".join(t.text or "" for t in inline.iter(N+"t")) if inline is not None else ""
        rows.append(values)
    return r,rows

def main():
    src=json.loads((ROOT/(NAME+".json")).read_text(encoding="utf-8"))
    audit=json.loads((ROOT/"Step09_CSAPI_Parts1_2_Clause_Audit_06NOV2026.json").read_text(encoding="utf-8"))
    old=json.loads((ROOT/"Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.json").read_text(encoding="utf-8"))
    with (ROOT/(NAME+".csv")).open(encoding="utf-8",newline="") as f:csvrows=list(csv.reader(f))
    md=(ROOT/(NAME+".md")).read_text(encoding="utf-8")
    need([x["key"] for x in src["columns"]]==EXPECTED_KEYS,"Owner-accepted column order changed")
    need(len(src["rows"])==37,"Original 22 + 9 hold + 6 section rows changed")
    need(len(src["originalDonorEvidence"])==51,"Donor roster/evidence cardinality changed")
    need(len(src["caseEvidence"])==73,"Case evidence cardinality changed")
    need(len(audit["reviewedExistingCells"])==12,"12 original CSAPI reviews missing")
    need(len(audit["nativeSourceFactsHeld"])==8,"Eight source-native holds missing")
    need(src["step09"]["nextStep"]=="STEP10_NOT_STARTED","Step10 accidentally marked started")
    need(src["ownerDecision"].startswith("STEP08_WORKING_COLUMN_LAYOUT_ACCEPTED"),"Owner's format status not carried")
    csapi=[e for e in src["originalDonorEvidence"] if e["donorKey"]=="CSAPI"]
    other=[e for e in src["originalDonorEvidence"] if e["donorKey"]!="CSAPI"]
    need(len(csapi)==12 and len(other)==39,"Historical donor split is wrong")
    need(all(e["sourceVerification"]=="OGC_ORIGINAL_CLAUSE_TERM_CHECKED_DIM_RELATION_PROPOSED" for e in csapi),
         "An old CSAPI row has not been original-clause-checked")
    need(all(e["sourceVerification"]=="PRIOR_SOURCE_EXTRACT_ONLY" for e in other),
         "A non-CSAPI mapping was upgraded without a donor review")
    oldcase=old["caseEvidence"]
    need(src["caseEvidence"]==oldcase,"Case evidence was changed in a CSAPI-only pass")
    for k in EXPECTED_KEYS:
        if k=="CSAPI":continue
        col=next(x for x in src["donorColumns"] if x["key"]==k) if k not in ("Dragino","AirGradient","Campbell","Bennett","DIM") else None
    oldOther=[e for e in old["originalDonorEvidence"] if e["donorKey"]!="CSAPI"]
    need(other==oldOther,"Any non-CSAPI donor evidence record changed")
    oldElems={r["rowKey"]:r for r in old["rows"] if r["type"]=="element"}
    reviewed={r["rowKey"]:r for r in audit["reviewedExistingCells"]}
    for r in src["rows"]:
        if r["type"]=="section":continue
        need(len(r["display"])==13,"Main row is not 13 columns")
        need(r["display"][9]=="","SWE Common was populated without source review")
        if r["type"]=="case_hold":
            need(all(not v for v in r["display"][4:12]),"Review-only case row became a donor mapping")
        if r["type"]=="element":
            prev=oldElems[r["rowKey"]]
            need(r["display"][:11]==prev["display"][:11] and r["display"][12]==prev["display"][12],
                 "Unrelated case, donor, or DIM text changed on "+r["rowKey"])
            if r["rowKey"] not in reviewed:need(r["display"]==prev["display"],"Unreviewed CSAPI cell was changed")
            else:
                claim=r["sourceClaims"]["CSAPI"]
                record=reviewed[r["rowKey"]]
                need(claim["term"]==record["term"] and claim["fit"]==record["relation"],
                     "Cell does not match original-clause record: "+r["rowKey"])
                need(r["display"][11]==(("≈ " if record["relation"]!="DIRECT" else "")+record["term"]),
                     "Visual donor cell differs from audited term: "+r["rowKey"])
    head1=["SOURCE EXAMPLES · documentary / historical","","","","OTHER DONOR STANDARDS · provisional","","",
           "FOUNDATIONAL SENSING / OBSERVATION","","","","","PROPOSED DIM"]
    expected=[head1,[c["name"] for c in src["columns"]]]
    dividers=[]
    for r in src["rows"]:
        if r["type"]=="section":
            dividers.append(len(expected)+1)
            expected.append([r["title"]+" — "+r["description"]]+[""]*12)
        else:expected.append(r["display"])
    need(csvrows==expected,"CSV is not an exact source JSON mirror")
    need(md.count('colspan="13"')==6,"Markdown contains incorrect divider geometry")
    with zipfile.ZipFile(ROOT/(NAME+".xlsx")) as p:
        need(p.testzip() is None,"XLSX is corrupt/CRC error")
        for f in p.namelist():
            if f.endswith(".xml") or f.endswith(".rels"):
                ET.fromstring(p.read(f))
        book=ET.fromstring(p.read("xl/workbook.xml"))
        names=[e.attrib["name"] for e in book.find(N+"sheets").findall(N+"sheet")]
        need(names==["Master Crosswalk","Case Evidence","Donor Evidence","DIM Definitions",
                     "Sources & Editions","Holds & Decisions","Read Me","CSAPI Clause Audit"],
             "Workbook sheet identities wrong")
        mroot,m=sheet(p,1,13)
        need(m==expected,"Committed XLSX cells do not match source JSON/CSV")
        merges=[v.attrib["ref"] for v in mroot.find(N+"mergeCells").findall(N+"mergeCell")]
        need(merges==["A1:D1","E1:G1","H1:L1"]+[f"A{i}:M{i}" for i in dividers],
             "Owner's grouped and full-width divider geometry was modified")
        _,case=sheet(p,2,9);need(len(case)==74,"Case Evidence lost records")
        _,don=sheet(p,3,11);need(len(don)==52,"Donor Evidence lost records")
        for i,x in enumerate(src["originalDonorEvidence"],start=1):
            row=don[i]
            need(row[0]==x["rowKey"] and row[3]==x["nativeTerm"] and row[4]==x["relation"] and
                 row[5]==x["sourceVerification"] and row[7]==x["sourceLocator"] and
                 row[8]==x["originalSourceUrl"],"Donor evidence XLSX mismatch at "+str(i))
        _,auditRows=sheet(p,8,10)
        need(len(auditRows)==21,"CSAPI clause-audit sheet should have 20 records")
        need(sum("EXISTING CELL" in x[0] for x in auditRows[1:])==12,"Source-review sheet missing 12 corrected cells")
        need(sum("ROW HELD" in x[0] for x in auditRows[1:])==8,"Source-review sheet missing 8 held native terms")
        for no in range(4,8):
            cols={4:7,5:7,6:5,7:2}
            sheet(p,no,cols[no])
    need((ROOT/"Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026.xlsx").exists(),
         "Old accepted-layout workbook was lost")
    print("PASS: genuine v0.3 XLSX; eight worksheets; unchanged 13-column owner layout, 6 section bands; 22 proposed rows and 9 holds; 12 original-clause-qualified CSAPI donor cells; 8 native source terms held; 39 other donor claims/73 case evidence unchanged; source/evidence/CSV/Markdown parity.")
    print("LIMIT: Source term checked, not approved DIM ontology, OGC test suite pass or deployed evidence.")
if __name__=="__main__":main()
