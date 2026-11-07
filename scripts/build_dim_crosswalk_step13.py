#!/usr/bin/env python3
"""Publish the Step13 2017 W3C SOSA/SSN audit as an updated source-consistent XLSX.
Preserves the approved v0.6 workbook ZIP parts, existing styles and prior donor
audits. No external installation, profile-interop or app changes are implied.
"""
from __future__ import annotations
import copy
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

HERE = Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
OLD = "Master_Donor_Concept_to_DIM_Crosswalk_v0.6_Step12_OMS_06NOV2026"
NEW = "Master_Donor_Concept_to_DIM_Crosswalk_v0.7_Step13_W3C_SOSA_SSN_06NOV2026"
AUDIT = "Step13_W3C_SOSA_SSN_2017_Original_Vocabulary_Audit_06NOV2026"
X = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
P = "http://schemas.openxmlformats.org/package/2006/relationships"
CT = "http://schemas.openxmlformats.org/package/2006/content-types"
EP = "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
VT = "http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"
Q = lambda local: "{" + X + "}" + local
ET.register_namespace("", X)
ET.register_namespace("r", R)
ET.register_namespace("vt", VT)
GRADE = "W3C_2017_RECOMMENDATION_ORIGINAL_VOCABULARY_CHECKED_DIM_RELATION_PROPOSED"

def require(ok, msg):
    if not ok:
        raise AssertionError(msg)

def strings(c):
    return "".join(t.text or "" for t in c.iter(Q("t")))

def set_inline(c, val):
    for node in list(c):
        if node.tag in (Q("is"), Q("v"), Q("f")):
            c.remove(node)
    c.set("t", "inlineStr")
    sub = ET.SubElement(c, Q("is"))
    t = ET.SubElement(sub, Q("t"))
    value = str(val if val is not None else "")
    t.text = value
    if value[:1].isspace() or value[-1:].isspace():
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")

def cell(row, index):
    label = ""
    n = index + 1
    while n:
        n, remainder = divmod(n - 1, 26)
        label = chr(65 + remainder) + label
    ref = label + str(row.attrib["r"])
    for c in row.findall(Q("c")):
        if c.get("r") == ref:
            return c
    return ET.SubElement(row, Q("c"), {"r": ref, "t": "inlineStr"})

def asbytes(tree):
    return ET.tostring(tree, encoding="utf-8", xml_declaration=True)

def patch_evidence(binary, model):
    root = ET.fromstring(binary)
    rows = root.find(Q("sheetData")).findall(Q("row"))
    require(len(rows) == len(model["originalDonorEvidence"]) + 1,
            "Donor evidence worksheet row count unexpectedly changed")
    n = 0
    for i, item in enumerate(model["originalDonorEvidence"], start=1):
        row = rows[i]
        require(strings(cell(row, 0)) == item["rowKey"], "Wrong donor row at " + str(i))
        if item["donorKey"] != "SOSA":
            continue
        require(item["sourceVerification"] == GRADE, "W3C source verification grade missing")
        values = {
            3: item["nativeTerm"],
            4: item["relation"],
            5: item["sourceVerification"],
            6: item["sourceEdition"],
            7: item["sourceLocator"],
            8: item["originalSourceUrl"],
            9: item["nonEquivalenceWarning"],
        }
        for col, val in values.items():
            set_inline(cell(row, col), val)
        n += 1
    require(n == 6, "Expected exactly six modified W3C donor records")
    return asbytes(root)

def patch_source_roster(binary):
    root = ET.fromstring(binary)
    n = 0
    for row in root.find(Q("sheetData")).findall(Q("row")):
        contents = " | ".join(strings(c) for c in row.findall(Q("c")))
        if "SOSA" in contents and "2017" in contents:
            # Seventh-column concise original-source standing is the source
            # roster's human-readable audit slot; no donor or edition renaming.
            set_inline(cell(row, 6),
              "6 W3C 2017 Recommendation original terms checked; 2026 Working Draft separate, not promoted. 20 donor cells remain PRIOR_SOURCE_EXTRACT_ONLY.")
            n += 1
    require(n >= 1, "Could not locate W3C 2017 edition in source roster")
    return asbytes(root)

def patch_readme(binary):
    root = ET.fromstring(binary)
    sd = root.find(Q("sheetData"))
    existing = sd.findall(Q("row"))
    new_index = max(int(row.get("r")) for row in existing) + 1
    row = ET.SubElement(sd, Q("row"), {"r":str(new_index)})
    set_inline(cell(row, 0), "Step13 W3C source review")
    set_inline(cell(row, 1),
      "2017 W3C Recommendation: 6 native OWL class terms source-checked (2 direct, 4 partial); 12 further leads held. 37/57 donor records source-reviewed; 20 prior-only. 2026 W3C draft and Open Group SOSA separate. No DIM/Profile adoption.")
    return asbytes(root)

def create_audit_sheet(audit):
    root = ET.Element(Q("worksheet"))
    ET.SubElement(root,Q("dimension"),{"ref":"A1:I19"})
    views=ET.SubElement(root,Q("sheetViews"))
    sv=ET.SubElement(views,Q("sheetView"),{"workbookViewId":"0"})
    ET.SubElement(sv,Q("pane"),{"ySplit":"1","topLeftCell":"A2","activePane":"bottomLeft","state":"frozen"})
    ET.SubElement(root,Q("sheetFormatPr"),{"defaultRowHeight":"18"})
    cols=ET.SubElement(root,Q("cols"))
    for i,w in enumerate((28,23,33,21,44,33,48,76,80),start=1):
        ET.SubElement(cols,Q("col"),{"min":str(i),"max":str(i),"width":str(w),"customWidth":"1"})
    sd=ET.SubElement(root,Q("sheetData"))
    headers=[
      "Review standing","DIM row / hold","W3C original native term",
      "Mapping fit / status","Original 2017 section","Source edition",
      "Original W3C publication URL","Original meaning or held context",
      "Boundary / prohibited inference"
    ]
    records=[headers]
    for item in audit["reviewedRows"]:
        records.append([
          "ORIGINAL W3C TERM CHECKED",item["rowKey"],item["nativeTerm"],
          item["relation"],item["sourceClause"],"2017-10-19 Recommendation",
          item["originalDocumentURL"],item["originalStandardMeaning"],
          item["nonEquivalenceBoundary"]
        ])
    for item in audit["nativeLeads"]:
        records.append([
          "SOURCE NATIVE LEAD HELD",item["relatedRowOrHold"],item["nativeTerm"],
          "HELD",item["clause"],"2017-10-19 Recommendation",
          item["originalSourceURL"],"Source-native distinction not adopted as DIM row",
          item["nonEquivalenceBoundary"]
        ])
    require(len(records)==19,"Audit worksheet must be 1+6+12 rows")
    for index,values in enumerate(records,start=1):
        row=ET.SubElement(sd,Q("row"),{"r":str(index),"ht":("30" if index==1 else "56"),"customHeight":"1"})
        for col,val in enumerate(values):
            c=cell(row,col)
            if index==1: c.set("s","1")
            set_inline(c,val)
    links=ET.SubElement(root,Q("hyperlinks"))
    rels=ET.Element("{"+P+"}Relationships")
    for rowno in range(2,20):
        ident="rId"+str(rowno-1)
        ET.SubElement(links,Q("hyperlink"),{"ref":"G"+str(rowno),"{"+R+"}id":ident})
        ET.SubElement(rels,"{"+P+"}Relationship",{
            "Id":ident,
            "Type":R+"/hyperlink",
            "Target":audit["source"]["originalURL"],"TargetMode":"External"
        })
    ET.SubElement(root,Q("pageMargins"),{
        "left":"0.3","right":"0.3","top":"0.6","bottom":"0.6","header":"0.3","footer":"0.3"
    })
    return asbytes(root), asbytes(rels)

def patch_workbook(binary):
    root=ET.fromstring(binary)
    sh=root.find(Q("sheets"))
    originals=sh.findall(Q("sheet"))
    require(len(originals)==11,"Expected 11 existing sheets")
    require(originals[-1].get("name")=="OMS Clause Audit","Unexpected current final audit tab")
    existing={x.get("{"+R+"}id") for x in originals}
    rnum=12
    while "rId"+str(rnum) in existing: rnum+=1
    newId="rId"+str(rnum)
    ET.SubElement(sh,Q("sheet"),{
        "name":"W3C SOSA SSN Audit","sheetId":"12","{"+R+"}id":newId
    })
    return asbytes(root),newId

def patch_workbook_rels(binary,identifier):
    root=ET.fromstring(binary)
    existing={x.get("Id") for x in root}
    require(identifier not in existing,"Workbook relationship id conflicts with another part")
    ET.SubElement(root,"{"+P+"}Relationship",{
        "Id":identifier,
        "Type":R+"/worksheet",
        "Target":"worksheets/sheet12.xml"
    })
    return asbytes(root)

def patch_content_types(binary):
    root=ET.fromstring(binary)
    require(not any("/xl/worksheets/sheet12.xml"==x.get("PartName") for x in root),
            "Sheet12 already exists")
    ET.SubElement(root,"{"+CT+"}Override",{
        "PartName":"/xl/worksheets/sheet12.xml",
        "ContentType":"application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"
    })
    return asbytes(root)

def patch_docprops(binary):
    root=ET.fromstring(binary)
    titles=root.find("{"+EP+"}TitlesOfParts")
    if titles is None:return binary
    vector=titles.find("{"+VT+"}vector")
    if vector is None:return binary
    ET.SubElement(vector,"{"+VT+"}lpstr").text="W3C SOSA SSN Audit"
    vector.set("size",str(len(vector)))
    headings=root.find("{"+EP+"}HeadingPairs")
    if headings is not None:
        values=list(headings.iter("{"+VT+"}i4"))
        if values and any(x.text=="11" for x in values):
            next(x for x in values if x.text=="11").text="12"
    return asbytes(root)

def main():
    model=json.loads((HERE/(NEW+".json")).read_text(encoding="utf-8"))
    old=json.loads((HERE/(OLD+".json")).read_text(encoding="utf-8"))
    audit=json.loads((HERE/(AUDIT+".json")).read_text(encoding="utf-8"))
    require(model["schemaVersion"].startswith("donor-dim-master-layout.v0.7"),"Wrong source JSON")
    require([x["key"] for x in model["columns"]]==[x["key"] for x in old["columns"]],"Owner layout drift")
    require(model["rows"]!=old["rows"] and len(model["rows"])==37,"Expected W3C-specific source-claim revision in fixed main grid")
    require(all(a["display"]==b["display"] for a,b in zip(model["rows"],old["rows"])), "Main presentation changed")
    require(model["caseEvidence"]==old["caseEvidence"], "Frozen case evidence changed")
    require(model["originalSourceInputHashes"]==old["originalSourceInputHashes"],"Original source pins changed")
    require(len(model["originalDonorEvidence"])==57,"Donor evidence count drift")
    require(len(audit["reviewedRows"])==6 and len(audit["nativeLeads"])==12,"W3C audit scope drift")
    with zipfile.ZipFile(HERE/(OLD+".xlsx")) as original:
        require(original.testzip() is None,"Original workbook failed ZIP integrity")
        names=original.namelist()
        require("xl/worksheets/sheet12.xml" not in names,"Input unexpectedly already has sheet12")
        binaryworkbook, relation=patch_workbook(original.read("xl/workbook.xml"))
        audit_xml,audit_rels=create_audit_sheet(audit)
        modified={
         "xl/workbook.xml":binaryworkbook,
         "xl/_rels/workbook.xml.rels":patch_workbook_rels(original.read("xl/_rels/workbook.xml.rels"),relation),
         "[Content_Types].xml":patch_content_types(original.read("[Content_Types].xml")),
         "xl/worksheets/sheet3.xml":patch_evidence(original.read("xl/worksheets/sheet3.xml"),model),
         "xl/worksheets/sheet5.xml":patch_source_roster(original.read("xl/worksheets/sheet5.xml")),
         "xl/worksheets/sheet7.xml":patch_readme(original.read("xl/worksheets/sheet7.xml")),
        }
        if "docProps/app.xml" in names:
            modified["docProps/app.xml"]=patch_docprops(original.read("docProps/app.xml"))
        output=HERE/(NEW+".xlsx")
        with zipfile.ZipFile(output,"w") as new:
            for member in original.infolist():
                new.writestr(member, modified.get(member.filename,original.read(member.filename)))
            new.writestr("xl/worksheets/sheet12.xml",audit_xml,compress_type=zipfile.ZIP_DEFLATED)
            new.writestr("xl/worksheets/_rels/sheet12.xml.rels",audit_rels,compress_type=zipfile.ZIP_DEFLATED)
    require(output.stat().st_size>100000,"Generated XLSX unexpectedly small")
    with zipfile.ZipFile(output) as pkg:
        require(pkg.testzip() is None,"Generated XLSX ZIP failed integrity")
        for name in pkg.namelist():
            if name.endswith((".xml",".rels")):
                ET.fromstring(pkg.read(name))
        wb=ET.fromstring(pkg.read("xl/workbook.xml"))
        names=[x.get("name") for x in wb.find(Q("sheets")).findall(Q("sheet"))]
        require(len(names)==12 and names[-1]=="W3C SOSA SSN Audit","Workbook sheet registry incorrect")
        unchanged=[2,4,6,8,9,10,11]
        with zipfile.ZipFile(HERE/(OLD+".xlsx")) as oldpkg:
            for n in unchanged:
                name="xl/worksheets/sheet"+str(n)+".xml"
                require(pkg.read(name)==oldpkg.read(name),"Non-W3C prior sheet was changed: "+name)
    print("PASS build v0.7 Step13 12-sheet XLSX: 6 W3C source-reviewed terms, 12 separate native leads, prior audits and cases preserved.")
    print("OUTPUT",output,output.stat().st_size)

if __name__=="__main__":
    main()
