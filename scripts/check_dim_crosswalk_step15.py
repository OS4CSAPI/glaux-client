#!/usr/bin/env python3
"""Independent read-only Step15 ISA original-source staging verifier.
No conformance, adopted model or live source claims.
"""
from pathlib import Path
from xml.etree import ElementTree as ET
import csv,json,zipfile

D=Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
OLD="Master_Donor_Concept_to_DIM_Crosswalk_v0.8_Step14_IEEE1451_06NOV2026"
NEW="Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026"
OVER="Step15_ISA_6_Proposed_14_Column_Overlay_07NOV2026"
AUD="Step15_ISA_6_Original_Source_Clause_Audit_07NOV2026"
STAGE="Step15_ISA6_Primary_Source_Staging_07NOV2026"
X="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
EXPECTED="Dragino AirGradient Campbell Bennett IEEE OPC SAPIENT SOSA OMS SWE SensorML CSAPI DIM".split()

def req(ok,message):
    if not ok:raise AssertionError(message)

def index(ref):
    col=0
    for letter in ref:
        if not letter.isalpha():break
        col=col*26+(ord(letter.upper())-64)
    return col-1

def read_grid(pkg,sheet,width):
    root=ET.fromstring(pkg.read("xl/worksheets/sheet"+str(sheet)+".xml"))
    rows=[]
    for row in root.find(X+"sheetData").findall(X+"row"):
        values=[""]*width
        for c in row.findall(X+"c"):
            i=index(c.get("r"))
            req(0<=i<width,"Cell outside expected worksheet column range")
            ins=c.find(X+"is")
            if ins is not None:
                values[i]="".join(t.text or "" for t in ins.iter(X+"t"))
            else:
                v=c.find(X+"v")
                if v is not None:values[i]=v.text or ""
        rows.append(values)
    return root,rows

def expected(old,stage):
    cols=old["columns"]
    preview=cols[:7]+[{
        "key":"ISA","name":"ISA 6.0 (proposed, source-checked)"
    }]+cols[7:]
    main=[["SOURCE EXAMPLES / documentary","","","",
           "OTHER DONOR STANDARDS / provisional","","",
           "FOUNDATIONAL SENSING/OBSERVATION","","","","","PROPOSED DIM"],
          [x["name"] for x in cols]]
    expanded=[["SOURCE CASES / documentary","","","",
               "OTHER DONORS / ISA PROVISIONAL","","","",
               "FOUNDATIONAL SENSING/OBSERVATION","","","","","PROPOSED DIM"],
              [x["name"] for x in preview]]
    loc={x["rowKey"]:x["nativeTerm"] for x in stage["mappings"]}
    bands=[]
    for row in old["rows"]:
        if row["type"]=="section":
            bands.append(len(expanded)+1)
            main.append([row["title"]+" — "+row["description"]]+[""]*12)
            expanded.append([row["title"]+" — "+row["description"]]+[""]*13)
        else:
            main.append(row["display"])
            expanded.append(row["display"][:7]+[
                ("≈ "+loc[row["rowKey"]]) if row["rowKey"] in loc else ""
            ]+row["display"][7:])
    # Compare the primary sheet against the actual frozen v0.8 CSV instead
    # of reconstructing presentation headings from an approximation.
    with (D/(OLD+".csv")).open(encoding="utf8",newline="") as f:
        main=list(csv.reader(f))
    return main,expanded,bands

def main():
    before=json.loads((D/(OLD+".json")).read_text(encoding="utf8"))
    actual=json.loads((D/(NEW+".json")).read_text(encoding="utf8"))
    stage=json.loads((D/(STAGE+".json")).read_text(encoding="utf8"))
    audit=json.loads((D/(AUD+".json")).read_text(encoding="utf8"))
    md=(D/(NEW+".md")).read_text(encoding="utf8")
    overlay=(D/(OVER+".md")).read_text(encoding="utf8")
    report=(D/(AUD+".md")).read_text(encoding="utf8")
    with (D/(NEW+".csv")).open(encoding="utf8",newline="") as f:
        maincsv=list(csv.reader(f))
    with (D/(OVER+".csv")).open(encoding="utf8",newline="") as f:
        fullcsv=list(csv.reader(f))
    req(len(stage["documents"])==5,"Five original ISA 6.0 PDF titles missing")
    req(all(x["date"]=="2023-10-31" for x in stage["documents"]),
        "2023 publication/revision boundary changed")
    req("DISTRIBUTION_A_ORIGINAL" in stage["sourceGrade"],
        "ISA primary-source verification grade wrong")
    req(len(stage["mappings"])==11 and len(stage["holds"])==14,
        "11 proposed mappings/14 held source-native concepts missing")
    req(len({x["rowKey"] for x in stage["mappings"]})==11,
        "Duplicate ISA mapping row")
    req(set(x["relation"] for x in stage["mappings"])=={"PARTIAL","RELATED"},
        "Unsupported ISA direct/identity equivalence added")
    req("2023" in report and "original" in report.lower() and
        "ISA 6.0" in report and "STEP16" in report.upper(),
        "Research report source/owner boundaries missing")
    req(audit==stage,"Audited original-source decisions not identical to frozen stage")
    req(len(before["columns"])==13 and [x["key"] for x in before["columns"]]==EXPECTED,
        "Baseline owner layout not 13-col verified")
    for name in ["columns","rows","originalDonorEvidence","caseEvidence","holds",
                 "originalSourceInputHashes"]:
        req(actual[name]==before[name],"Main accepted source changed: "+name)
    req(actual["ownerDecision"]==before["ownerDecision"],
        "Step08 owner-approved presentation status changed")
    req(len(actual["originalDonorEvidence"])==58 and len(actual["caseEvidence"])==73,
        "Preexisting donor/case counts lost")
    req(len([x for x in actual["rows"] if x["type"]=="element"])==22,
        "22 proposed DIM rows altered")
    req(len([x for x in actual["rows"] if x["type"]=="case_hold"])==9,
        "Nine prior case holds altered")
    req(len([x for x in actual["rows"] if x["type"]=="section"])==6,
        "Six topic dividers altered")
    req(actual["step15"]["requiresOwnerAcceptanceForPromotion"] is True and
        actual["step15"]["mainPrimaryDonorCellCount"]==58,
        "ISA column automatically promoted or primary total inflated")
    req(actual["step15"]["nextStep"]==
        "STEP16_OWNER_CHECKPOINT_NOT_STARTED_REQUIRES_SEPARATE_PROCEED",
        "Owner checkpoint pre-empted")
    req(actual["counts"]["ISAStagedOriginalSourceCheckedMappings"]==11,
        "Staged mapping count missing")
    req(actual["counts"]["ISANativeSourceLeadsHeld"]==14,
        "Native held count missing")
    req(len([x for x in actual["originalDonorEvidence"]
             if x["sourceVerification"]=="PRIOR_SOURCE_EXTRACT_ONLY"])==15,
        "Previously unverified donor material wrongly recategorized")
    main_matrix,preview_matrix,bands=expected(before,stage)
    req(main_matrix==maincsv,"Primary 13-col CSV not same as previous JSON")
    req(preview_matrix==fullcsv,"Fourteen-col proposed CSV not same as source")
    req(md.count('colspan="13"')==6 and
        overlay.count('colspan="14"')==6,
        "GitHub-readable topic sections misplaced")
    req(overlay.count("ISA 6.0 (proposed, source-checked)")>=1 and
        "PROVISIONAL" in overlay,
        "Owner review preview mislabeled as adopted")
    with zipfile.ZipFile(D/(NEW+".xlsx")) as pkg,zipfile.ZipFile(D/(OLD+".xlsx")) as prior:
        req(pkg.testzip() is None,"Published Step15 workbook corrupt")
        for part in pkg.namelist():
            if part.endswith((".xml",".rels")):ET.fromstring(pkg.read(part))
        wb=ET.fromstring(pkg.read("xl/workbook.xml"))
        names=[e.get("name") for e in wb.find(X+"sheets").findall(X+"sheet")]
        req(len(names)==15 and names[-2:]==
            ["ISA Original Clause Audit","ISA Proposed Overlay"],
            "Two new ISA sheets not appended after 13 earlier sheets")
        for i in range(1,14):
            path="xl/worksheets/sheet"+str(i)+".xml"
            req(pkg.read(path)==prior.read(path),
                "Previous accepted workbook/audit worksheet was modified "+path)
        root,primary=read_grid(pkg,1,13)
        req(primary==main_matrix,"Published primary master no longer unchanged")
        auditroot,ar=read_grid(pkg,14,9)
        req(len(ar)==26 and ar[0][0]=="Evidence grade",
            "ISA original clause audit has wrong size")
        req(sum(x[0]=="ORIGINAL 2023 CLAUSE CHECKED / STAGED" for x in ar[1:])==11 and
            sum(x[0]=="ORIGINAL 2023 SOURCE HOLD" for x in ar[1:])==14,
            "Audit worksheet missing 11 source terms or 14 holds")
        ovr,ov=read_grid(pkg,15,14)
        req(ov==preview_matrix,"Actual Excel 14-col owner overlay not source-identical")
        merges=ovr.find(X+"mergeCells")
        req(merges is not None,"Preview merged bands missing")
        refs=[m.get("ref") for m in merges.findall(X+"mergeCell")]
        req(refs==["A1:D1","E1:H1","I1:M1"]+
            ["A"+str(i)+":N"+str(i) for i in bands],
            "ISA preview 14-col band geometry not preserved")
        need_isa={x["rowKey"] for x in stage["mappings"]}
        for r in actual["rows"]:
            if r.get("rowKey") in need_isa:
                pos=[i for i,x in enumerate(actual["rows"]) if x.get("rowKey")==r["rowKey"]][0]
                # Two front rows precede the existing 37 main rows
                req(ov[2+pos][7].startswith("≈ "),"Staged ISA display absent")
    print("PASS: Step15 source ledger 5 original Distribution A ISA 2023 titles; 11 original-checked provisional mappings, 14 native holds.")
    print("PASS: exact 15-sheet XLSX ZIP/XML; 13 earlier sheets byte-identical, primary 13 columns and all source claims preserved.")
    print("PASS: separate full 14-column proposed ISA overlay, 6 merged groups, DIM far right, case-left positions and all source/CSV/JSON mirrors.")
    print("PASS: 58 original primary donor records, 73 case evidence, 22 DIM proposals, 9 case holds; no new adopted DIM, Profile, device command or Step16 execution.")

if __name__=="__main__":
    main()
