#!/usr/bin/env python3
"""Build the v0.8 Step14 IEEE 1451 public-technical-research XLSX.

Source first: update the frozen 12-sheet v0.7 workbook at six IEEE cells;
append exactly one new evidence record and one IEEE technical audit worksheet.
Do not alter prior original OGC/W3C audits or the 13-column owner layout.
This code packages XML directly to retain source workbook formatting and
hyperlinks; it does NOT perform a normative IEEE 1451.0-2024 conformance test.
"""
from pathlib import Path
from xml.etree import ElementTree as ET
import json, zipfile

DIR = Path("Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk")
OLD = "Master_Donor_Concept_to_DIM_Crosswalk_v0.7_Step13_W3C_SOSA_SSN_06NOV2026"
NEW = "Master_Donor_Concept_to_DIM_Crosswalk_v0.8_Step14_IEEE1451_06NOV2026"
AUD = "Step14_IEEE1451_2024_Public_Technical_Evidence_Audit_06NOV2026"
G = "IEEE_1451_2024_PUBLISHER_SCOPE_NIST_IML_PUBLIC_TECHNICAL_CHECKED_NORMATIVE_TEXT_UNINSPECTED"
X="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
P="http://schemas.openxmlformats.org/package/2006/relationships"
CT="http://schemas.openxmlformats.org/package/2006/content-types"
EP="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
VT="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"
Q=lambda x:"{"+X+"}"+x
ET.register_namespace("",X)
ET.register_namespace("r",R)
ET.register_namespace("vt",VT)

def req(cond,msg):
    if not cond: raise AssertionError(msg)

def textval(c):
    if c is None: return ""
    value=c.find(Q("is"))
    if value is not None:return "".join(v.text or "" for v in value.iter(Q("t")))
    value=c.find(Q("v"))
    return value.text or "" if value is not None else ""

def cell(row,n):
    index=n+1
    letters=""
    while index:
        index,d=divmod(index-1,26);letters=chr(65+d)+letters
    ref=letters+str(row.get("r"))
    for c in row.findall(Q("c")):
        if c.get("r")==ref:return c
    c=ET.SubElement(row,Q("c"),{"r":ref,"t":"inlineStr"})
    return c

def assign(c,value):
    for child in list(c):
        if child.tag in (Q("is"),Q("v"),Q("f")):c.remove(child)
    c.set("t","inlineStr")
    is_=ET.SubElement(c,Q("is"))
    t=ET.SubElement(is_,Q("t"))
    v=str(value if value is not None else "")
    t.text=v
    if v[:1].isspace() or v[-1:].isspace():
        t.set("{http://www.w3.org/XML/1998/namespace}space","preserve")

def binary(root):
    return ET.tostring(root,encoding="utf-8",xml_declaration=True)

def patch_master(original,model):
    root=ET.fromstring(original)
    matched=0
    for row in root.find(Q("sheetData")).findall(Q("row")):
        if textval(cell(row,12))=="Persistent System identifier":
            req(textval(cell(row,4))=="","Previously empty IEEE identifier cell no longer empty")
            desired=next(x for x in model["rows"] if x.get("rowKey")=="S06-R004")["display"][4]
            assign(cell(row,4),desired)
            matched+=1
    req(matched==1,"Exactly one main IEEE identifier cell must be updated")
    return binary(root)

def patch_evidence(original,model):
    root=ET.fromstring(original)
    sd=root.find(Q("sheetData"))
    rows=sd.findall(Q("row"))
    req(len(rows)==58,"Expected 57 previous donor records + header")
    previous=model["originalDonorEvidence"][:-1]
    req(len(previous)==57 and model["originalDonorEvidence"][-1]["donorKey"]=="IEEE",
        "New IEEE record must be appended after all frozen source records")
    n=0
    columns=(3,4,5,6,7,8,9)
    attrs=("nativeTerm","relation","sourceVerification","sourceEdition",
           "sourceLocator","originalSourceUrl","nonEquivalenceWarning")
    for i,e in enumerate(previous,start=1):
        row=rows[i]
        req(textval(cell(row,0))==e["rowKey"],"Donor source order changed "+str(i))
        if e["donorKey"]!="IEEE":continue
        req(e["sourceVerification"]==G,"IEEE evidence needs public-only grade")
        for col,attr in zip(columns,attrs):assign(cell(row,col),e[attr])
        n+=1
    req(n==5,"Expected five old IEEE mappings rewritten")
    x=model["originalDonorEvidence"][-1]
    rn=59
    row=ET.SubElement(sd,Q("row"),{"r":str(rn)})
    values=[x["rowKey"],x["dim"],x["donor"],x["nativeTerm"],
            x["relation"],x["sourceVerification"],x["sourceEdition"],
            x["sourceLocator"],x["originalSourceUrl"],x["nonEquivalenceWarning"],
            "PROPOSED_NOT_ADOPTED"]
    for i,value in enumerate(values):assign(cell(row,i),value)
    dim=root.find(Q("dimension"))
    if dim is not None:dim.set("ref","A1:K59")
    links=root.find(Q("hyperlinks"))
    req(links is not None and len(links.findall(Q("hyperlink")))==57,
        "57 previous donor evidence hyperlinks not present")
    existing={n.get("{"+R+"}id") for n in links}
    count=58
    while "rId"+str(count) in existing: count+=1
    rel="rId"+str(count)
    ET.SubElement(links,Q("hyperlink"),{"ref":"I59","{"+R+"}id":rel})
    return binary(root),rel

def patch_source_rels(original,new_relation,source):
    root=ET.fromstring(original)
    req(new_relation not in {x.get("Id") for x in root},
        "New donor link id already in use")
    ET.SubElement(root,"{"+P+"}Relationship",{
        "Id":new_relation,
        "Type":R+"/hyperlink",
        "Target":source,
        "TargetMode":"External"})
    return binary(root)

def patch_sources(original):
    root=ET.fromstring(original)
    n=0
    for row in root.find(Q("sheetData")).findall(Q("row")):
        desc=" | ".join(textval(c) for c in row.findall(Q("c")))
        if "IEEE" in desc and ("1451" in desc or "TEDS" in desc):
            assign(cell(row,6),
              "6 IEEE 1451.0-2024 publisher/NIST/IML PUBLIC TECHNICAL terms reviewed (NOT 2024 normative requirements); 14 source technical holds. Distinct PHY TEDS is 1451.5-2007; only OPC 6 + SAPIENT 9 remain prior-only.")
            n+=1
    req(n>=1,"IEEE 1451 source roster record not found")
    return binary(root)

def patch_readme(original):
    root=ET.fromstring(original)
    sd=root.find(Q("sheetData"));rows=sd.findall(Q("row"))
    idx=max(int(x.get("r")) for x in rows)+1
    row=ET.SubElement(sd,Q("row"),{"r":str(idx)})
    assign(cell(row,0),"Step14 IEEE public technical review")
    assign(cell(row,1),
      "IEEE 1451.0-2024 official publisher scope and NIST/IML technical Playground: five previously populated IEEE terms qualified and 1 TIM UUID relation added (6 technical-reviewed); 14 technical leads HELD; normative 2024 licensed text not independently inspected. 37 OGC/W3C original-source-reviewed, 6 IEEE public-technical-only, 15 prior-only, 58 total. PHY TEDS 1451.5-2007 separate. DIM/Profile not adopted.")
    dim=root.find(Q("dimension"))
    if dim is not None:dim.set("ref","A1:B"+str(idx))
    return binary(root)

def audit_xml(audit):
    root=ET.Element(Q("worksheet"))
    records=[[
      "Audit standing","DIM row or review hold","IEEE native term",
      "Fit or lead status","Original / technical locator","Evidence category",
      "Primary/public technical source URL","Source meaning / crosswalk rationale",
      "Non-equivalence warning"
    ]]
    for x in audit["reviewedRows"]:
        records.append([
          "PUBLIC TECHNICAL TERM CHECKED",x["rowKey"],x["nativeTerm"],x["relation"],
          x["publisherOrTechnicalLocator"],"IEEE publisher + NIST/IML technical; 2024 normative NOT inspected",
          x["primaryOrTechnicalURL"],x["nativeMeaning"],x["nonEquivalenceBoundary"]
        ])
    for x in audit["nativeLeads"]:
        records.append([
          "PUBLIC TECHNICAL SOURCE LEAD HELD",x["relatedRowOrHold"],x["nativeTerm"],"HELD",
          x["sourceLocator"],x["sourceStanding"],x["technicalSourceURL"],
          "Public technical distinction retained for future model/row synthesis",x["nonEquivalenceBoundary"]
        ])
    req(len(records)==21,"Need 6 source-mapped +14 held +header on IEEE audit sheet")
    ET.SubElement(root,Q("dimension"),{"ref":"A1:I21"})
    views=ET.SubElement(root,Q("sheetViews"))
    view=ET.SubElement(views,Q("sheetView"),{"workbookViewId":"0"})
    ET.SubElement(view,Q("pane"),{"ySplit":"1","topLeftCell":"A2","activePane":"bottomLeft","state":"frozen"})
    ET.SubElement(root,Q("sheetFormatPr"),{"defaultRowHeight":"18"})
    cols=ET.SubElement(root,Q("cols"))
    for j,width in enumerate((32,24,37,23,55,46,52,77,82),start=1):
        ET.SubElement(cols,Q("col"),{"min":str(j),"max":str(j),"width":str(width),"customWidth":"1"})
    sd=ET.SubElement(root,Q("sheetData"))
    for i,items in enumerate(records,start=1):
        row=ET.SubElement(sd,Q("row"),{"r":str(i),"ht":str(32 if i==1 else 62),"customHeight":"1"})
        for j,value in enumerate(items):
            c=cell(row,j)
            if i==1:c.set("s","1")
            assign(c,value)
    h=ET.SubElement(root,Q("hyperlinks"))
    rs=ET.Element("{"+P+"}Relationships")
    for i,row in enumerate(records[1:],start=2):
        id_="rId"+str(i-1)
        ET.SubElement(h,Q("hyperlink"),{"ref":"G"+str(i),"{"+R+"}id":id_})
        ET.SubElement(rs,"{"+P+"}Relationship",{
            "Id":id_,"Type":R+"/hyperlink","Target":row[6],"TargetMode":"External"})
    ET.SubElement(root,Q("pageMargins"),{
        "left":"0.3","right":"0.3","top":"0.6","bottom":"0.6","header":"0.3","footer":"0.3"})
    return binary(root),binary(rs)

def patch_workbook(original,old_rel):
    root=ET.fromstring(original);s=root.find(Q("sheets"))
    sheets=s.findall(Q("sheet"))
    req(len(sheets)==12 and sheets[-1].get("name")=="W3C SOSA SSN Audit",
        "Expected the exact Step13 12-sheet workbook")
    used={x.get("{"+R+"}id") for x in sheets}|set(old_rel)
    j=13
    while "rId"+str(j) in used:j+=1
    relation="rId"+str(j)
    ET.SubElement(s,Q("sheet"),{"name":"IEEE 1451 Audit","sheetId":"13","{"+R+"}id":relation})
    return binary(root),relation

def patch_wbrels(original,new_id):
    root=ET.fromstring(original)
    req(new_id not in {r.get("Id") for r in root},"Workbook rId collision")
    ET.SubElement(root,"{"+P+"}Relationship",{
        "Id":new_id,"Type":R+"/worksheet","Target":"worksheets/sheet13.xml"})
    return binary(root)

def patch_ct(original):
    root=ET.fromstring(original)
    req(not any(x.get("PartName")=="/xl/worksheets/sheet13.xml" for x in root),
        "Sheet13 exists already")
    ET.SubElement(root,"{"+CT+"}Override",{
        "PartName":"/xl/worksheets/sheet13.xml",
        "ContentType":"application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"})
    return binary(root)

def patch_docprops(original):
    root=ET.fromstring(original)
    titles=root.find("{"+EP+"}TitlesOfParts")
    if titles is None:return original
    v=titles.find("{"+VT+"}vector")
    if v is None:return original
    ET.SubElement(v,"{"+VT+"}lpstr").text="IEEE 1451 Audit"
    v.set("size",str(len(v)))
    heads=root.find("{"+EP+"}HeadingPairs")
    if heads is not None:
        for el in heads.iter("{"+VT+"}i4"):
            if el.text=="12":el.text="13";break
    return binary(root)

def main():
    model=json.loads((DIR/(NEW+".json")).read_text(encoding="utf-8"))
    old=json.loads((DIR/(OLD+".json")).read_text(encoding="utf-8"))
    audit=json.loads((DIR/(AUD+".json")).read_text(encoding="utf-8"))
    req(model["schemaVersion"].startswith("donor-dim-master-layout.v0.8"),"Wrong Step14 source")
    req([x["key"] for x in model["columns"]]==[x["key"] for x in old["columns"]],
        "Owner approved column order altered")
    req(len(model["rows"])==len(old["rows"])==37 and
        len(model["originalDonorEvidence"])==58 and
        len(old["originalDonorEvidence"])==57,
        "Rows or evidence size drift")
    req(model["caseEvidence"]==old["caseEvidence"],"Source case evidence modified")
    req(model["originalSourceInputHashes"]==old["originalSourceInputHashes"],
        "Original source fingerprints modified")
    req(len(audit["reviewedRows"])==6 and len(audit["nativeLeads"])==14,
        "Incorrect bounded IEEE review")
    with zipfile.ZipFile(DIR/(OLD+".xlsx")) as orig:
        req(orig.testzip() is None,"Previous XLSX damaged")
        members=orig.namelist()
        rel_root=ET.fromstring(orig.read("xl/_rels/workbook.xml.rels"))
        rel_ids={x.get("Id") for x in rel_root}
        wb_xml,wb_new_id=patch_workbook(orig.read("xl/workbook.xml"),rel_ids)
        donor_xml,new_link=patch_evidence(orig.read("xl/worksheets/sheet3.xml"),model)
        relfile="xl/worksheets/_rels/sheet3.xml.rels"
        req(relfile in members,"Source evidence relationship file absent")
        new_audit_xml,new_audit_rels=audit_xml(audit)
        mod={
          "xl/workbook.xml":wb_xml,
          "xl/_rels/workbook.xml.rels":patch_wbrels(orig.read("xl/_rels/workbook.xml.rels"),wb_new_id),
          "[Content_Types].xml":patch_ct(orig.read("[Content_Types].xml")),
          "xl/worksheets/sheet1.xml":patch_master(orig.read("xl/worksheets/sheet1.xml"),model),
          "xl/worksheets/sheet3.xml":donor_xml,
          relfile:patch_source_rels(orig.read(relfile),new_link,model["originalDonorEvidence"][-1]["originalSourceUrl"]),
          "xl/worksheets/sheet5.xml":patch_sources(orig.read("xl/worksheets/sheet5.xml")),
          "xl/worksheets/sheet7.xml":patch_readme(orig.read("xl/worksheets/sheet7.xml")),
        }
        if "docProps/app.xml" in members:
            mod["docProps/app.xml"]=patch_docprops(orig.read("docProps/app.xml"))
        target=DIR/(NEW+".xlsx")
        with zipfile.ZipFile(target,"w") as new:
            for member in orig.infolist():
                new.writestr(member,mod.get(member.filename,orig.read(member.filename)))
            for name,payload in [
                ("xl/worksheets/sheet13.xml",new_audit_xml),
                ("xl/worksheets/_rels/sheet13.xml.rels",new_audit_rels)]:
                info=zipfile.ZipInfo(name,date_time=(1980,1,1,0,0,0))
                info.compress_type=zipfile.ZIP_DEFLATED
                new.writestr(info,payload)
    req(target.stat().st_size>100000,"Output workbook unexpectedly small")
    with zipfile.ZipFile(target) as pkg,zipfile.ZipFile(DIR/(OLD+".xlsx")) as previous:
        req(pkg.testzip() is None,"XLSX integrity failed")
        for name in pkg.namelist():
            if name.endswith((".xml",".rels")):ET.fromstring(pkg.read(name))
        root=ET.fromstring(pkg.read("xl/workbook.xml"))
        sheets=[x.get("name") for x in root.find(Q("sheets")).findall(Q("sheet"))]
        req(len(sheets)==13 and sheets[-1]=="IEEE 1451 Audit","New worksheet invalid")
        for idx in (2,4,6,8,9,10,11,12):
            part="xl/worksheets/sheet"+str(idx)+".xml"
            req(pkg.read(part)==previous.read(part),"Prior case or original OGC/W3C audit overwritten "+part)
    print("PASS build IEEE Step14 v0.8: 13-sheet Excel, 6 technical-checked IEEE terms (5 reviewed, 1 new), 14 public-source holds; all older original evidence preserved.")
    print("OUTPUT",target,target.stat().st_size)

if __name__=="__main__":main()
