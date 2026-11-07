#!/usr/bin/env python3
"""Independent Step14 IEEE public-source limitation and v0.8 XLSX preservation check."""
import csv,json,zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

DIR=Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
NEW="Master_Donor_Concept_to_DIM_Crosswalk_v0.8_Step14_IEEE1451_06NOV2026"
OLD="Master_Donor_Concept_to_DIM_Crosswalk_v0.7_Step13_W3C_SOSA_SSN_06NOV2026"
AUD="Step14_IEEE1451_2024_Public_Technical_Evidence_Audit_06NOV2026"
X="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R="{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
GRADE="IEEE_1451_2024_PUBLISHER_SCOPE_NIST_IML_PUBLIC_TECHNICAL_CHECKED_NORMATIVE_TEXT_UNINSPECTED"
ORDER="Dragino AirGradient Campbell Bennett IEEE OPC SAPIENT SOSA OMS SWE SensorML CSAPI DIM".split()

def require(ok,msg):
    if not ok:raise AssertionError(msg)

def colnum(ref):
    n=0
    for c in ref:
        if not c.isalpha():break
        n=n*26+ord(c)-64
    return n-1

def grid(pkg,sheet,cols):
    root=ET.fromstring(pkg.read("xl/worksheets/sheet"+str(sheet)+".xml"))
    out=[]
    for row in root.find(X+"sheetData").findall(X+"row"):
        arr=[""]*cols
        for c in row.findall(X+"c"):
            j=colnum(c.get("r"))
            require(0<=j<cols,"Cell outside checked range")
            node=c.find(X+"is")
            if node is not None:arr[j]="".join(x.text or "" for x in node.iter(X+"t"))
            else:
                node=c.find(X+"v")
                if node is not None:arr[j]=node.text or ""
        out.append(arr)
    return root,out

def main():
    d=json.loads((DIR/(NEW+".json")).read_text(encoding="utf-8"))
    prev=json.loads((DIR/(OLD+".json")).read_text(encoding="utf-8"))
    audit=json.loads((DIR/(AUD+".json")).read_text(encoding="utf-8"))
    md=(DIR/(NEW+".md")).read_text(encoding="utf-8")
    rpt=(DIR/(AUD+".md")).read_text(encoding="utf-8")
    with (DIR/(NEW+".csv")).open(newline="",encoding="utf-8") as stream:
        maincsv=list(csv.reader(stream))
    require([x["key"] for x in d["columns"]]==ORDER and d["columns"]==prev["columns"],
            "Owner accepted column geometry changed")
    require(len(d["rows"])==len(prev["rows"])==37,"Main DIM/held row count drift")
    require(sum(r["type"]=="element" for r in d["rows"])==22,"22 proposed DIM rows missing")
    require(sum(r["type"]=="case_hold" for r in d["rows"])==9,"9 case review holds missing")
    require(sum(r["type"]=="section" for r in d["rows"])==6,"Six section dividers missing")
    require(d["caseEvidence"]==prev["caseEvidence"] and len(d["caseEvidence"])==73,
            "Original 73 source-case facts altered")
    require(d["originalSourceInputHashes"]==prev["originalSourceInputHashes"],
            "Frozen source fingerprints altered")
    require(d["holds"]==prev["holds"],"Prior source review holds altered")
    require(d["ownerDecision"]==prev["ownerDecision"],"Owner presentation acceptance changed")
    require(len(prev["originalDonorEvidence"])==57 and len(d["originalDonorEvidence"])==58,
            "Need exactly one additional IEEE donor correspondence")
    require([x for x in d["originalDonorEvidence"] if x["donorKey"]!="IEEE"]==
            [x for x in prev["originalDonorEvidence"] if x["donorKey"]!="IEEE"],
            "Previously reviewed OGC/W3C or other donor evidence changed")
    req_prior=[x for x in d["originalDonorEvidence"] if x["sourceVerification"]=="PRIOR_SOURCE_EXTRACT_ONLY"]
    tech=[x for x in d["originalDonorEvidence"] if x["sourceVerification"]==GRADE]
    normative=[x for x in d["originalDonorEvidence"] if x["sourceVerification"] not in
               ("PRIOR_SOURCE_EXTRACT_ONLY",GRADE)]
    require(len(req_prior)==15 and {x["donorKey"] for x in req_prior}=={"OPC","SAPIENT"},
            "Other 15 previous-only donor evidence rows missing")
    require(len(tech)==6 and all(x["donorKey"]=="IEEE" for x in tech),
            "IEEE public technical evidence incorrectly graded")
    require(len(normative)==37 and len(tech)+len(normative)+len(req_prior)==58,
            "Source evidence grade arithmetic wrong")
    require(d["counts"]["originalDonorMappings"]==58 and
            d["counts"]["otherDonorCellsUnverified"]==15 and
            d["counts"]["publicTechnicalCheckedIEEECells"]==6,
            "Counts metadata no longer matches actual evidence")
    require(len(audit["reviewedRows"])==6 and len(audit["nativeLeads"])==14,
            "Bounded IEEE source audit missing or overexpanded")
    require(audit["sources"]["IEEEpublisher"]["normativeFullTextIndependentlyInspected"] is False,
            "IEEE 2024 publisher scope incorrectly promoted to full normative audit")
    require(audit["prohibitedOverclaims"] and any("1451.5-2007" in x for x in
            audit["prohibitedOverclaims"]),"PHY TEDS edition separation lost")
    require(d["step14"]["nextStep"]=="STEP15_NOT_STARTED_SEPARATE_OWNER_PROCEED_REQUIRED",
            "Step15 was started without owner approval")
    require(d["step14"]["uninspectedNormativeClausesExplicitHold"] is True,
            "Licensed IEEE 2024 full normative text marked reviewed")
    for newer,older in zip(d["rows"],prev["rows"]):
        require(newer["type"]==older["type"] and
                newer.get("rowKey")==older.get("rowKey") and
                newer.get("dim")==older.get("dim"),
                "Unapproved proposed DIM row or role change")
        if newer["type"]=="section":require(newer==older,"Topic divider edited")
        else:
            diffs=[n for n,(a,b) in enumerate(zip(newer["display"],older["display"])) if a!=b]
            require((diffs==[4] if newer["rowKey"]=="S06-R004" else not diffs),
                    "Unexpected donor/case presentation modified "+str(newer.get("rowKey")))
            if newer["type"]=="element":
                for donor,claim in older.get("sourceClaims",{}).items():
                    if donor!="IEEE":
                        require(newer["sourceClaims"][donor]==claim,
                                "Non-IEEE source-local row claim changed "+str(newer.get("rowKey")))
    new=next(x for x in d["originalDonorEvidence"] if x["rowKey"]=="S06-R004" and x["donorKey"]=="IEEE")
    require(new["nativeTerm"]=="MetaTEDS.UUID (TIM identifier)" and
            new["relation"]=="RELATED" and "normative clauses NOT inspected" in new["sourceEdition"],
            "TIM UUID source-grade/boundary wrong")
    require(next(x for x in d["rows"] if x.get("rowKey")=="S06-R004")["display"][4]=="≈ "+new["nativeTerm"],
            "New IEEE identity cell text missing")
    require(sum(x["relation"]=="DIRECT" for x in tech)==1 and
            sum(x["relation"]=="PARTIAL" for x in tech)==3 and
            sum(x["relation"]=="RELATED" for x in tech)==2,
            "IEEE mapping relations unexpectedly changed")
    heads=["SOURCE EXAMPLES · documentary / historical","","","","OTHER DONOR STANDARDS · provisional","","",
      "FOUNDATIONAL SENSING / OBSERVATION","","","","","PROPOSED DIM"]
    expected=[heads,[c["name"] for c in d["columns"]]]
    div=[]
    for row in d["rows"]:
        if row["type"]=="section":
            div.append(len(expected)+1)
            expected.append([row["title"]+" — "+row["description"]]+[""]*12)
        else:expected.append(row["display"])
    require(expected==maincsv,"CSV source-to-display JSON mismatch")
    require(md.count('colspan="13"')==6 and
            "≈ MetaTEDS.UUID (TIM identifier)" in md and
            "normative" in md.lower() and "15 prior-only" in md,
            "Readable GitHub master missing correctly qualified technical delta")
    require("1451.5-2007" in rpt and "normative" in rpt.lower(),
            "Mixed-edition or normative limits missing from written audit")
    with zipfile.ZipFile(DIR/(NEW+".xlsx")) as z,zipfile.ZipFile(DIR/(OLD+".xlsx")) as orig:
        require(z.testzip() is None,"Generated XLSX ZIP corrupted")
        for p in z.namelist():
            if p.endswith((".xml",".rels")):ET.fromstring(z.read(p))
        wb=ET.fromstring(z.read("xl/workbook.xml"))
        names=[s.get("name") for s in wb.find(X+"sheets").findall(X+"sheet")]
        require(len(names)==13 and names[-1]=="IEEE 1451 Audit" and names[-2]=="W3C SOSA SSN Audit",
                "All earlier audit sheets and new IEEE tab not found")
        root,main=grid(z,1,13)
        require(main==expected,"Actual XLSX main cells fail JSON/CSV parity")
        merges=[x.get("ref") for x in root.find(X+"mergeCells").findall(X+"mergeCell")]
        require(merges==["A1:D1","E1:G1","H1:L1"]+
                ["A"+str(x)+":M"+str(x) for x in div],
                "Owner 13-column grouped headers/dividers altered")
        for n in (2,4,6,8,9,10,11,12):
            path="xl/worksheets/sheet"+str(n)+".xml"
            require(z.read(path)==orig.read(path),
                    "Earlier source/OGC/W3C evidence tab changed "+path)
        _,cases=grid(z,2,9)
        require(len(cases)==74,"73 case evidence rows lost from Excel")
        evroot,ev=grid(z,3,11)
        require(len(ev)==59,"58 source mappings + header not present in donor worksheet")
        for i,x in enumerate(d["originalDonorEvidence"],start=1):
            row=ev[i]
            for col,value in [(0,x["rowKey"]),(3,x["nativeTerm"]),(4,x["relation"]),
                              (5,x["sourceVerification"]),(6,x["sourceEdition"]),
                              (7,x["sourceLocator"]),(8,x["originalSourceUrl"]),
                              (9,x["nonEquivalenceWarning"])]:
                require(row[col]==value,"Workbook source cell mismatch "+x["rowKey"]+" col "+str(col))
        require(len(evroot.find(X+"hyperlinks").findall(X+"hyperlink"))==58,
                "58 individual donor publisher/technical hyperlinks not preserved")
        _,defrows=grid(z,4,7)
        require(len(defrows)==32,"22 DIM proposals and nine holds definitions altered")
        _,srcrows=grid(z,5,7)
        require(any("6 IEEE 1451.0-2024" in r[6] for r in srcrows),
                "IEEE public-only technical standing missing from Sources & Editions")
        _,readme=grid(z,7,2)
        require(any(r[0]=="Step14 IEEE public technical review" for r in readme),
                "New status and caution absent from workbook Read Me")
        ir,ie=grid(z,13,9)
        require(len(ie)==21 and sum(row[0]=="PUBLIC TECHNICAL TERM CHECKED" for row in ie)==6
                and sum(row[0]=="PUBLIC TECHNICAL SOURCE LEAD HELD" for row in ie)==14,
                "Original six mapped + fourteen held IEEE audit rows incorrect")
        require(len(ir.find(X+"hyperlinks").findall(X+"hyperlink"))==20,
                "Source links for all IEEE 20 research records not found")
    print("PASS: IEEE 1451 Step14 v0.8 original IEEE publisher+NIST/IML public technical grade preserved; 13-sheet Excel ZIP/XML/JSON/CSV parity.")
    print("PASS: Five old IEEE mappings reviewed, one TIM UUID RELATED mapping added to existing row; fourteen native technical leads HELD.")
    print("PASS: 37 original OGC/W3C source-reviewed + 6 IEEE public technical (2024 normative UNINSPECTED) + 15 earlier-only = 58 evidence rows.")
    print("PASS: owner 13 columns, six dividers, 22 DIM proposals, nine case holds, 73 case source records, all eight prior source audit/metadata tabs intact.")
    print("LIMIT: PHY TEDS cites 1451.5-2007, not 1451.0-2024; no full IEEE clauses, installed device, external conformance, actual Command or deployed Profile claims.")

if __name__=="__main__":main()
