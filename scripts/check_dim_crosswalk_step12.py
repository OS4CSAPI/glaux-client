#!/usr/bin/env python3
"""Read-only actual XLSX+source check for Step12 OMS 3.0. No conformance claim."""
import csv
import json
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

DIR=Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
NEW="Master_Donor_Concept_to_DIM_Crosswalk_v0.6_Step12_OMS_06NOV2026"
OLD="Master_Donor_Concept_to_DIM_Crosswalk_v0.5_Step11_SWECommon_06NOV2026"
N="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
EXPECTED="Dragino AirGradient Campbell Bennett IEEE OPC SAPIENT SOSA OMS SWE SensorML CSAPI DIM".split()
GRADE="OGC_20_082R4_ORIGINAL_CONCEPTUAL_REQUIREMENTS_CHECKED_DIM_RELATION_PROPOSED"

def require(ok,message):
    if not ok:raise AssertionError(message)

def grid(package,i,ncol):
    root=ET.fromstring(package.read(f"xl/worksheets/sheet{i}.xml"))
    rows=[]
    for row in root.find(N+"sheetData").findall(N+"row"):
        values=[""]*ncol
        for c in row.findall(N+"c"):
            letters="".join(x for x in c.attrib["r"] if x.isalpha())
            offset=0
            for ch in letters:offset=offset*26+ord(ch)-64
            offset-=1
            require(0<=offset<ncol,"Out-of-range cell "+c.attrib["r"])
            val=c.find(N+"is")
            if val is not None:values[offset]="".join(x.text or "" for x in val.iter(N+"t"))
        rows.append(values)
    return root,rows

def main():
    src=json.loads((DIR/(NEW+".json")).read_text(encoding="utf8"))
    old=json.loads((DIR/(OLD+".json")).read_text(encoding="utf8"))
    audit=json.loads((DIR/"Step12_OMS_3_Original_Clause_Audit_06NOV2026.json").read_text(encoding="utf8"))
    with (DIR/(NEW+".csv")).open(encoding="utf8",newline="") as stream:
        csvrows=list(csv.reader(stream))
    markdown=(DIR/(NEW+".md")).read_text(encoding="utf8")
    require(src["columns"]==old["columns"] and [x["key"] for x in src["columns"]]==EXPECTED,
        "Owner-accepted column geometry changed")
    require(len(src["rows"])==len(old["rows"])==37,"Expected original 22 proposed, 9 held, 6 section rows")
    require(len([r for r in src["rows"] if r["type"]=="element"])==22,"Proposed rows changed")
    require(len([r for r in src["rows"] if r["type"]=="case_hold"])==9,"Case review holds changed")
    require(len(src["caseEvidence"])==73 and src["caseEvidence"]==old["caseEvidence"],
        "Case evidence changed or lost")
    require(src["originalSourceInputHashes"]==old["originalSourceInputHashes"],
        "Frozen source fingerprint changed")
    require(len(src["originalDonorEvidence"])==57,"Original donor count changed")
    require(len(audit["reviewedRows"])==5 and len(audit["nativeLeads"])==12,
        "OMS reviewed or held records cardinality wrong")
    require(src["step12"]["nextStep"]=="STEP13_NOT_STARTED","Step13 is prematurely started")
    prior_others=[x for x in old["originalDonorEvidence"] if x["donorKey"]!="OMS"]
    current_others=[x for x in src["originalDonorEvidence"] if x["donorKey"]!="OMS"]
    require(prior_others==current_others,"Other source donors changed in OMS-only pass")
    oms=[x for x in src["originalDonorEvidence"] if x["donorKey"]=="OMS"]
    require(len(oms)==5 and all(x["sourceVerification"]==GRADE and
            x["disposition"]=="PROPOSED_NOT_ADOPTED" for x in oms),"OMS source standing invalid")
    counts={"CSAPI":12,"SensorML":10,"SWE":4}
    for donor,expected in counts.items():
        require(len([x for x in src["originalDonorEvidence"] if x["donorKey"]==donor])==expected,
            "Source-reviewed donor record count changed: "+donor)
    require(len([x for x in src["originalDonorEvidence"] if
         x["donorKey"] not in ("OMS","CSAPI","SensorML","SWE") and
         x["sourceVerification"]=="PRIOR_SOURCE_EXTRACT_ONLY"])==26,"26 historical other donor source records not retained")
    changes={x["rowKey"]:x for x in audit["reviewedRows"]}
    require(set(changes)=={"S06-R009","S06-R010","S06-R013","S06-R014","S06-R015"},
        "Unreviewed OMS rows changed")
    original={r["rowKey"]:r for r in old["rows"] if r["type"]!="section"}
    for r in src["rows"]:
        if r["type"]=="section":continue
        before=original[r["rowKey"]]
        require(r["type"]==before["type"] and r["dim"]==before["dim"],"Original DIM/hold row meaning changed")
        require(r["display"][:8]==before["display"][:8] and r["display"][9:]==before["display"][9:],
            "Non-OMS donor/case/target text altered on "+r["rowKey"])
        if r["type"]=="case_hold":
            require(not any(r["display"][4:12]),"Case-only hold row gained a donor claim")
        elif r["rowKey"] in changes:
            record=changes[r["rowKey"]]
            claim=r["sourceClaims"]["OMS"]
            require(claim["fit"]==record["relation"] and claim["term"]==record["nativeTerm"],
                "Source claim and approved audit disagree "+r["rowKey"])
            require(r["display"][8]==(("≈ " if record["relation"]!="DIRECT" else "")+record["nativeTerm"]),
                "Visual OMS cell mismatch "+r["rowKey"])
        else:
            require(r["display"]==before["display"],"Unreviewed OMS row unexpectedly edited")
    sectionHeader=["SOURCE EXAMPLES · documentary / historical","","","","OTHER DONOR STANDARDS · provisional","","",
      "FOUNDATIONAL SENSING / OBSERVATION","","","","","PROPOSED DIM"]
    expected=[sectionHeader,[x["name"] for x in src["columns"]]]
    dividers=[]
    for r in src["rows"]:
        if r["type"]=="section":
            dividers.append(len(expected)+1)
            expected.append([r["title"]+" — "+r["description"]]+[""]*12)
        else:expected.append(r["display"])
    require(expected==csvrows,"Source JSON and CSV main grid mismatch")
    require(markdown.count('colspan="13"')==6,"GitHub readable master section divider count changed")
    with zipfile.ZipFile(DIR/(NEW+".xlsx")) as z,zipfile.ZipFile(DIR/(OLD+".xlsx")) as orig:
        require(z.testzip() is None,"XLSX ZIP invalid")
        for f in z.namelist():
            if f.endswith(".xml") or f.endswith(".rels"): ET.fromstring(z.read(f))
        wb=ET.fromstring(z.read("xl/workbook.xml"))
        names=[x.attrib["name"] for x in wb.find(N+"sheets").findall(N+"sheet")]
        require(names==["Master Crosswalk","Case Evidence","Donor Evidence","DIM Definitions",
          "Sources & Editions","Holds & Decisions","Read Me","CSAPI Clause Audit",
          "SensorML Clause Audit","SWE Common Clause Audit","OMS Clause Audit"],
          "11 worksheet identities/order incorrect")
        mainroot,main=grid(z,1,13)
        require(main==expected,"Actual XLSX main cells not identical to JSON/CSV")
        merges=[x.attrib["ref"] for x in mainroot.find(N+"mergeCells").findall(N+"mergeCell")]
        require(merges==["A1:D1","E1:G1","H1:L1"]+[f"A{i}:M{i}" for i in dividers],
            "Owner's grouped/merged section geometry changed")
        for n in (2,8,9,10):
            require(z.read(f"xl/worksheets/sheet{n}.xml")==orig.read(f"xl/worksheets/sheet{n}.xml"),
              "Prior evidence worksheet changed: "+str(n))
        _,cases=grid(z,2,9)
        require(len(cases)==74,"Case evidence tab should contain 73 rows plus header")
        dono,donrows=grid(z,3,11)
        require(len(donrows)==58,"Donor evidence tab should contain 57 rows plus header")
        for i,e in enumerate(src["originalDonorEvidence"],start=1):
            row=donrows[i]
            require(row[0]==e["rowKey"] and row[3]==e["nativeTerm"] and row[4]==e["relation"] and
             row[5]==e["sourceVerification"] and row[6]==e["sourceEdition"] and
             row[7]==e["sourceLocator"] and row[8]==e["originalSourceUrl"] and
             row[9]==e["nonEquivalenceWarning"],"Donor source record mismatch at "+str(i+1))
        require(len(dono.find(N+"hyperlinks").findall(N+"hyperlink"))==57,
            "All 57 publisher hyperlinks were not preserved")
        _,defs=grid(z,4,7);require(len(defs)==32,"DIM definition rows changed")
        _,sources=grid(z,5,7)
        require(len(sources)==14 and "5 OMS original" in sources[9][6],"OMS original source standing not updated")
        _,holds=grid(z,6,5);require(len(holds)==16,"Previous holds changed")
        _,readme=grid(z,7,2);require(len(readme)==18,"ReadMe changed structure")
        auditroot,omsa=grid(z,11,9)
        require(len(omsa)==18,"OMS audit must have 5 reviewed +12 leads +header")
        require(sum(x[0]=="SOURCE CONCEPTUAL TERM CHECKED" for x in omsa[1:])==5,"Five OMS original-source terms absent")
        require(sum(x[0]=="NATIVE SOURCE LEAD HELD" for x in omsa[1:])==12,"Twelve OMS leads absent")
        require(len(auditroot.find(N+"hyperlinks").findall(N+"hyperlink"))==17,"Original OMS clause hyperlinks absent")
    print("PASS: authentic 11-sheet v0.6 Step12 workbook ZIP/XML; owner 13-column grouping and six dividers; 5 OMS concepts source-qualified, 12 native source leads held; 52 non-OMS donor records and 73 original case records unchanged; 22 proposals and 9 case holds unchanged; exact JSON/CSV/evidence parity.")
    print("LIMIT: OMS Abstract Specification source clauses checked, NOT native JSON serialization, conformant deployed Observation or adopted DIM.")

if __name__=="__main__":main()
