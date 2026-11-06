#!/usr/bin/env python3
"""Independent read-only check of actual committed Step08 revised XLSX + source mirrors.

Does not validate donor semantic equivalence or certify Excel UI rendering.
"""
from __future__ import annotations
import csv
import json
import re
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

BASE=Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
NAME="Master_Donor_Concept_to_DIM_Crosswalk_v0.2_06NOV2026"
X="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
EXPECTED=["Dragino","AirGradient","Campbell","Bennett","IEEE","OPC","SAPIENT",
          "SOSA","OMS","SWE","SensorML","CSAPI","DIM"]

def ensure(ok,detail):
    if not ok: raise AssertionError(detail)

def colnum(name):
    n=0
    for v in name:n=26*n+ord(v)-64
    return n-1

def worksheet(package,path,width):
    root=ET.fromstring(package.read(path))
    items=[]
    for row in root.find(X+"sheetData").findall(X+"row"):
        vals=[""]*width
        for c in row.findall(X+"c"):
            ref=c.attrib.get("r","")
            m=re.fullmatch(r"([A-Z]+)\d+",ref)
            ensure(m is not None,f"invalid cell {ref}")
            i=colnum(m.group(1))
            ensure(0<=i<width,f"cell outside width: {ref}")
            inline=c.find(X+"is")
            value=("".join(x.text or "" for x in inline.iter(X+"t")) if inline is not None
                  else (c.find(X+"v").text or "" if c.find(X+"v") is not None else ""))
            vals[i]=value
        items.append(vals)
    return root,items

def main():
    src=json.loads((BASE/(NAME+".json")).read_text(encoding="utf-8"))
    with (BASE/(NAME+".csv")).open(newline="",encoding="utf-8") as f:csvrows=list(csv.reader(f))
    md=(BASE/(NAME+".md")).read_text(encoding="utf-8")
    cases=src["caseEvidence"]
    donors=src["originalDonorEvidence"]
    keys=[c["key"] for c in src["columns"]]
    ensure(keys==EXPECTED,repr(keys))
    ensure(src["ownerDecision"]=="PENDING_STEP08_REVIEW","owner approval was invented")
    ensure(len(cases)==73 and len(donors)==51,"prior claims changed or case count wrong")
    ensure(all(d["sourceVerification"]=="PRIOR_SOURCE_EXTRACT_ONLY" for d in donors),
           "donor clauses were improperly relabeled original checked")
    ensure(len([r for r in src["rows"] if r["type"]=="element"])==22,"22 proposed rows lost")
    ensure(len([r for r in src["rows"] if r["type"]=="case_hold"])==9,"9 explicit review holds missing")
    ensure(len([r for r in src["rows"] if r["type"]=="section"])==6,"6 divider groups missing")
    expected=[["SOURCE EXAMPLES · documentary / historical","","","","OTHER DONOR STANDARDS · provisional","","","FOUNDATIONAL SENSING / OBSERVATION","","","","","PROPOSED DIM"],[c["name"] for c in src["columns"]]]
    dividerPositions=[]
    for r in src["rows"]:
        if r["type"]=="section":
            dividerPositions.append(len(expected)+1)
            expected.append([r["title"]+" — "+r["description"]]+[""]*12)
        else: expected.append(r["display"])
    ensure(csvrows==expected,"CSV literal grid deviates from source JSON")
    ensure(len(expected)==39,"master grid size changed")
    for r in src["rows"]:
        if r["type"]=="section":continue
        ensure(len(r["display"])==13,"row lacks 13 cells")
        if r["type"]=="case_hold":
            ensure(not any(r["display"][4:12]),"a review-hold row acquired an unapproved donor claim")
        ensure(r["display"][9]=="","SWE Common got an unreviewed mapping")
        if r["type"]=="element":
            for i,d in enumerate(EXPECTED[4:12],4):
                claim=r["sourceClaims"].get(d)
                wanted=("" if claim is None else ("" if claim["fit"]=="DIRECT" else "≈ ")+claim["term"])
                ensure(r["display"][i]==wanted,"historic donor term/mapping changed: "+r["rowKey"]+"/"+d)
    assert md.count('colspan="13"')==6
    assert md.count('colspan="4"')==1 and md.count('colspan="3"')==1 and md.count('colspan="5"')==1
    with zipfile.ZipFile(BASE/(NAME+".xlsx")) as package:
        ensure(package.testzip() is None,"XLSX ZIP CRC is invalid")
        for path in package.namelist():
            if path.endswith(".xml") or path.endswith(".rels"):ET.fromstring(package.read(path))
        workbook=ET.fromstring(package.read("xl/workbook.xml"))
        names=[s.attrib["name"] for s in workbook.find(X+"sheets").findall(X+"sheet")]
        ensure(names==["Master Crosswalk","Case Evidence","Donor Evidence","DIM Definitions",
                       "Sources & Editions","Holds & Decisions","Read Me"],"worksheet identities changed")
        sheet,m=worksheet(package,"xl/worksheets/sheet1.xml",13)
        ensure(m==expected,"actual Excel cells differ from JSON/CSV mirrors")
        merge=sheet.find(X+"mergeCells")
        actualMerge=[r.attrib["ref"] for r in merge.findall(X+"mergeCell")]
        expectedMerge=["A1:D1","E1:G1","H1:L1"]+[f"A{i}:M{i}" for i in dividerPositions]
        ensure(actualMerge==expectedMerge,f"merged group/section rows differ {actualMerge}")
        pane=sheet.find(X+"sheetViews").find(X+"sheetView").find(X+"pane")
        ensure(pane is not None and pane.attrib.get("ySplit")=="2","two-row header is not frozen")
        ensure(sheet.find(X+"autoFilter") is None,"master has invalid filter through merged section bands")
        croot,cr=worksheet(package,"xl/worksheets/sheet2.xml",9)
        droot,dr=worksheet(package,"xl/worksheets/sheet3.xml",11)
        ensure(len(cr)==74 and len(dr)==52,"evidence sheet record count changed")
        ensure(len(croot.find(X+"hyperlinks").findall(X+"hyperlink"))>=73,
               "case evidence/source hyperlinks missing")
        ensure(len(droot.find(X+"hyperlinks").findall(X+"hyperlink"))==51,
               "legacy donor source hyperlinks missing")
        for index,width,rows in [(4,7,32),(5,7,14),(6,5,16),(7,2,18)]:
            root,rs=worksheet(package,f"xl/worksheets/sheet{index}.xml",width)
            ensure(len(rs)==rows,f"tab {index} has {len(rs)} rows instead of {rows}")
        ensure(all(v=="PRIOR_SOURCE_EXTRACT_ONLY" for v in [r[5] for r in dr[1:]]),
               "donor evidence statuses were improperly upgraded")
        ensure(all(not row[9] for row in m[2:]),
               "SWE column may not contain existing donor concepts")
    # Inspect historical master unchanged on branch where possible, not copied/overwritten.
    ensure((BASE/"Master_Donor_Concept_to_DIM_Crosswalk.xlsx").exists(),
           "historical actual workbook was removed")
    print("PASS: committed revision XLSX opens structurally; 7 sheets; 13 grouped columns; 2 frozen header rows; 6 full-width dividers; 22 original proposed rows plus 9 clear review holds; 73 case cells and 51 donor claims; SWE intentionally blank; CSV/JSON literal parity; source hyperlinks retained; historical XLSX kept.")
    print("LIMIT: owner acceptance, original-standards semantic revalidation and deployed cross-system conformance NOT established.")
if __name__=="__main__":main()
