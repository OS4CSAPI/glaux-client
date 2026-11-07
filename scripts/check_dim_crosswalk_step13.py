#!/usr/bin/env python3
"""Independent read-only Step13 W3C 2017 source, XLSX, mirror and preservation audit."""
import csv
import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

DIR=Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
NEW="Master_Donor_Concept_to_DIM_Crosswalk_v0.7_Step13_W3C_SOSA_SSN_06NOV2026"
OLD="Master_Donor_Concept_to_DIM_Crosswalk_v0.6_Step12_OMS_06NOV2026"
AUD="Step13_W3C_SOSA_SSN_2017_Original_Vocabulary_Audit_06NOV2026"
N="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R="{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
GRADE="W3C_2017_RECOMMENDATION_ORIGINAL_VOCABULARY_CHECKED_DIM_RELATION_PROPOSED"
EXPECTED="Dragino AirGradient Campbell Bennett IEEE OPC SAPIENT SOSA OMS SWE SensorML CSAPI DIM".split()

def require(ok, msg):
    if not ok: raise AssertionError(msg)

def column_offset(ref):
    result=0
    for char in ref:
        if not char.isalpha():break
        result=result*26+ord(char)-64
    return result-1

def grid(pkg,sheetnum,ncols):
    root=ET.fromstring(pkg.read("xl/worksheets/sheet"+str(sheetnum)+".xml"))
    sd=root.find(N+"sheetData")
    values=[]
    for row in sd.findall(N+"row"):
        out=[""]*ncols
        for c in row.findall(N+"c"):
            idx=column_offset(c.get("r"))
            require(0<=idx<ncols,"Cell exceeds table width "+c.get("r"))
            isel=c.find(N+"is")
            if isel is not None:out[idx]="".join(t.text or "" for t in isel.iter(N+"t"))
            else:
                ve=c.find(N+"v")
                if ve is not None:out[idx]=ve.text or ""
        values.append(out)
    return root,values

def main():
    src=json.loads((DIR/(NEW+".json")).read_text(encoding="utf-8"))
    old=json.loads((DIR/(OLD+".json")).read_text(encoding="utf-8"))
    audit=json.loads((DIR/(AUD+".json")).read_text(encoding="utf-8"))
    md=(DIR/(NEW+".md")).read_text(encoding="utf-8")
    report=(DIR/(AUD+".md")).read_text(encoding="utf-8")
    with (DIR/(NEW+".csv")).open(encoding="utf-8",newline="") as f:maincsv=list(csv.reader(f))
    require(src["ownerDecision"]==old["ownerDecision"],"Owner-approved format standing changed")
    require(src["columns"]==old["columns"],"13 owner-approved source/donor/DIM positions changed")
    require([x["key"] for x in src["columns"]]==EXPECTED,"Unexpected columns")
    require(len(src["rows"])==len(old["rows"])==37,"37 source rows changed")
    require(len([r for r in src["rows"] if r["type"]=="element"])==22,"DIM proposal count changed")
    require(len([r for r in src["rows"] if r["type"]=="case_hold"])==9,"Case hold count changed")
    require(len([r for r in src["rows"] if r["type"]=="section"])==6,"Topic section count changed")
    require(src["caseEvidence"]==old["caseEvidence"] and len(src["caseEvidence"])==73,
            "Original 73 source-qualified case statements changed")
    require(src["originalSourceInputHashes"]==old["originalSourceInputHashes"],
            "Original frozen source fingerprints changed")
    require(src["holds"]==old["holds"],"Preexisting unrelated holds changed")
    require(len(src["originalDonorEvidence"])==57==len(old["originalDonorEvidence"]), "Donor cell count changed")
    require([x for x in src["originalDonorEvidence"] if x["donorKey"]!="SOSA"]==
            [x for x in old["originalDonorEvidence"] if x["donorKey"]!="SOSA"],
            "One or more non-W3C donor source records changed")
    prioronly=[x for x in src["originalDonorEvidence"] if x["sourceVerification"]=="PRIOR_SOURCE_EXTRACT_ONLY"]
    require(len(prioronly)==20 and {x["donorKey"] for x in prioronly}=={"IEEE","OPC","SAPIENT"},
            "20 remaining IEEE/OPC/SAPIENT prior-only source records not retained")
    reviewed=[x for x in src["originalDonorEvidence"] if x["sourceVerification"]!=
              "PRIOR_SOURCE_EXTRACT_ONLY"]
    require(len(reviewed)==37,"37 original-source reviewed donor records not present")
    w3c=[x for x in src["originalDonorEvidence"] if x["donorKey"]=="SOSA"]
    require(len(w3c)==6 and all(x["sourceVerification"]==GRADE for x in w3c),
            "Six original 2017 W3C terms not source-qualified")
    require(len(audit["reviewedRows"])==6 and len(audit["nativeLeads"])==12,
            "Original W3C scope 6+12 violated")
    require(audit["source"]["edition"]=="W3C Recommendation 19 October 2017" and
            "2017/REC" in audit["source"]["originalURL"],"Wrong W3C edition or source")
    require(audit["explicitlySeparateLaterDraft"]["not2017Recommendation"] is True and
            "2026/WD" in audit["explicitlySeparateLaterDraft"]["url"],
            "2026 working draft conflated with 2017")
    relation={x["relation"] for x in audit["reviewedRows"]}
    require(relation=={"DIRECT","PARTIAL"} and
            sum(x["relation"]=="DIRECT" for x in audit["reviewedRows"])==2,
            "W3C mappings fit not 2 DIRECT, 4 PARTIAL")
    rowindex={x["rowKey"]:x for x in src["rows"] if x["type"]!="section"}
    for row,prev in zip(src["rows"],old["rows"]):
        require(row["type"]==prev["type"] and row.get("rowKey")==prev.get("rowKey") and
            row.get("dim")==prev.get("dim"),"Model row or holder was edited")
        if row["type"]=="section":
            require(row==prev,"Navigation divider changed")
        else:
            require(row["display"]==prev["display"],"Main table presentation altered")
            if row["type"]=="element":
                for donor,claim in prev.get("sourceClaims",{}).items():
                    if donor!="SOSA":require(row["sourceClaims"][donor]==claim,
                        "Unrelated source claim changed "+donor+" "+row["rowKey"])
    for item in audit["reviewedRows"]:
        evidence=next((x for x in w3c if x["rowKey"]==item["rowKey"]),None)
        require(evidence and evidence["nativeTerm"]==item["nativeTerm"] and
                evidence["relation"]==item["relation"] and
                evidence["sourceLocator"]==item["sourceClause"] and
                evidence["originalSourceUrl"]==item["originalDocumentURL"],
                "W3C audit and structured source evidence disagree")
        claim=rowindex[item["rowKey"]]["sourceClaims"]["SOSA"]
        require(claim["term"]==item["nativeTerm"] and claim["sourceVerification"]==GRADE,
                "Row-local W3C source claim not updated")
    expected=[["SOURCE EXAMPLES · documentary / historical","","","","OTHER DONOR STANDARDS · provisional","","",
      "FOUNDATIONAL SENSING / OBSERVATION","","","","","PROPOSED DIM"],[x["name"] for x in src["columns"]]]
    divider_positions=[]
    for row in src["rows"]:
        if row["type"]=="section":
            divider_positions.append(len(expected)+1)
            expected.append([row["title"]+" — "+row["description"]]+[""]*12)
        else:expected.append(row["display"])
    require(expected==maincsv,"JSON/csv source-grid parity failed")
    require(md.count('colspan="13"')==6 and md.count("<table>")==1,
            "GitHub-readable master lost full-width geometry")
    require("6 W3C" in md and "20 other" in md and "2026" in report,
            "GitHub output version/source distinctions not visible")
    with zipfile.ZipFile(DIR/(NEW+".xlsx")) as pkg,zipfile.ZipFile(DIR/(OLD+".xlsx")) as oldpkg:
        require(pkg.testzip() is None,"Generated ZIP is damaged")
        for part in pkg.namelist():
            if part.endswith(".xml") or part.endswith(".rels"):
                ET.fromstring(pkg.read(part))
        wb=ET.fromstring(pkg.read("xl/workbook.xml"))
        names=[n.get("name") for n in wb.find(N+"sheets").findall(N+"sheet")]
        require(names==["Master Crosswalk","Case Evidence","Donor Evidence","DIM Definitions",
           "Sources & Editions","Holds & Decisions","Read Me","CSAPI Clause Audit",
           "SensorML Clause Audit","SWE Common Clause Audit","OMS Clause Audit",
           "W3C SOSA SSN Audit"],"Workbook worksheet names/order changed")
        mainroot,rows=grid(pkg,1,13)
        require(rows==expected,"Actual 13-column workbook does not match JSON/CSV")
        merges=[n.get("ref") for n in mainroot.find(N+"mergeCells").findall(N+"mergeCell")]
        require(merges==["A1:D1","E1:G1","H1:L1"]+
            ["A"+str(k)+":M"+str(k) for k in divider_positions],
            "13-column grouped headers or 6 full-width topic dividers changed")
        for number in [2,4,6,8,9,10,11]:
            part="xl/worksheets/sheet"+str(number)+".xml"
            require(pkg.read(part)==oldpkg.read(part),"Non-W3C prior worksheet changed "+part)
        _,case=grid(pkg,2,9)
        require(len(case)==74,"73 equipment-source records lost")
        dr,ev=grid(pkg,3,11)
        require(len(ev)==58,"Donor source evidence count incorrect")
        for i,x in enumerate(src["originalDonorEvidence"],start=1):
            r=ev[i]
            for col,val in [(0,x["rowKey"]),(3,x["nativeTerm"]),(4,x["relation"]),
                    (5,x["sourceVerification"]),(6,x["sourceEdition"]),(7,x["sourceLocator"]),
                    (8,x["originalSourceUrl"]),(9,x["nonEquivalenceWarning"])]:
                require(r[col]==val,"Workbook evidence mismatch "+x["rowKey"]+" col "+str(col))
        require(len(dr.find(N+"hyperlinks").findall(N+"hyperlink"))==57,
                "57 original source URL hyperlinks not preserved")
        _,defrows=grid(pkg,4,7)
        require(len(defrows)==32,"22+9 original model/hold definitions changed")
        _,srcrows=grid(pkg,5,7)
        require(any("6 W3C 2017 Recommendation" in r[6] for r in srcrows),
                "Current W3C source standing missing from Sources/Edition tab")
        _,readme=grid(pkg,7,2)
        require(any("Step13 W3C source review"==r[0] for r in readme),
                "Latest source-review limitations missing from Read Me tab")
        auditroot,auditrows=grid(pkg,12,9)
        require(len(auditrows)==19,"W3C sheet should have 6 checked, 12 held and 1 header")
        require(sum(x[0]=="ORIGINAL W3C TERM CHECKED" for x in auditrows)==6,
                "Six reviewed 2017 W3C concepts missing")
        require(sum(x[0]=="SOURCE NATIVE LEAD HELD" for x in auditrows)==12,
                "12 W3C native source leads missing")
        require(len(auditroot.find(N+"hyperlinks").findall(N+"hyperlink"))==18,
                "W3C audit sheet must link all 18 source records")
    print("PASS: Step13 W3C 2017 original Recommendation source-backed, v0.7 12-sheet Excel ZIP/XML/JSON/CSV/evidence consistent.")
    print("PASS: 6 reviewed W3C terms (2 direct/4 partial), 12 held leads; 31 earlier source checks and 20 prior-only remain.")
    print("PASS: 13 owner columns, six topic dividers, 22 proposed DIM rows, 9 case holds, 73 original case examples, all prior audit sheets preserved.")
    print("LIMIT: W3C 2026 draft held separately; no adopted DIM, profile rules, authenticated source, native encoding, external interoperability or deployed changes.")

if __name__=="__main__":main()
