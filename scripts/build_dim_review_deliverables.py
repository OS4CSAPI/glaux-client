#!/usr/bin/env python3
"""Build GitHub-native DIM V2 review files from committed source records.

No network, no source mutations, no unverified equivalence promotion.
Binary XLSX is OOXML assembled using Python stdlib zipfile/XML; no office apps.
The workbook is REGENERATED from committed source reviews and is NOT a
byte-for-byte copy of a previously generated ChatGPT attachment.
"""
from __future__ import annotations
import csv, html, io, re, subprocess, zipfile
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'Docs/Research/DIM_Profile_V2'
OUT=SRC/'Deliverables'
OUT.mkdir(parents=True,exist_ok=True)
BASE_URL='https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/'
reg=SRC/'Donor_Alignment/03_Source_Accountability_Register.csv'
audit=SRC/'Donor_Alignment/05_Donor_to_R24_Artifact_Traceability_04NOV2026.csv'
dim=SRC/'Candidate_Specification/DIM.md'
donors=SRC/'Concept_Donor_Comparison/Donor_Contributions.md'
terms=SRC/'Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md'
puml=SRC/'Candidate_Specification/DIM_V2_Candidate_R24_UML_04NOV2026.puml'
assert all(p.exists() for p in [reg,audit,dim,donors,terms,puml])

def readcsv(p):
    with open(p,encoding='utf-8-sig',newline='') as fh:return list(csv.DictReader(fh))
artifact=readcsv(reg)
trace=readcsv(audit)
assert len(artifact)==len(trace)==182
by_id={int(r['artifact_id']):r for r in artifact}
assert len(by_id)==182
assert all(r.get('concept_review_status')=='NOT_ASSESSED' for r in artifact)

# Exactly the data/coverage stored in the source file; no accidental claim of an
# individual-artifact concept review. Each R24 topic is a family-level candidate.
family_rows=[]
family=defaultdict(lambda:{'artifacts':0,'topics':set(),'depth':set(),'citations':[]})
for r in trace:
    line=r.get('donor_lineage_from_original_register','') or 'UNASSIGNED'
    rec=family[line];rec['artifacts']+=1
    rec['depth'].add(r.get('lineage_review_depth',''))
    for x in re.findall(r'R24-\d{2}',r.get('R24_TOPICS_ONLY_not_artifact_level_equivalences','')):
        rec['topics'].add(x)
    rec['citations'].append(str(r['artifact_id']))
for label,x in sorted(family.items(),key=lambda item:item[0].lower()):
    ids=sorted(x['topics'])
    family_rows.append([label,x['artifacts'],', '.join(sorted(x['depth'])),'; '.join(ids),
        'SOURCE FAMILY TOPICS ONLY — NOT individual artifact mappings',
        BASE_URL+'Concept_Donor_Comparison/Donor_Contributions.md'])

# Original R24 rows exactly as present in candidate DIM, with their evidence
# snippets rather than synthetic superclass definitions.
r24=[]
for line in dim.read_text(encoding='utf-8').splitlines():
    if line.startswith('| **R24-'):
        cols=[x.strip() for x in line.split('|')[1:-1]]
        if len(cols)>=3:
            m=re.search(r'R24-\d{2}',cols[0])
            if m:r24.append([m.group(0),re.sub(r'[\\*\\x60]','',cols[0]),
                re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',cols[1]).replace('**',''),
                re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',cols[2]).replace('**',''),
                BASE_URL+'Candidate_Specification/DIM.md#r24-relationship-register--one-connected-model-individually-testable-meanings'])
assert len(r24)==15, f'Expected 15 unique R24 rows, got {len(r24)}'

# The existing side-by-side original donor terminology tables, retaining exact
# native terms across their columns and original heading. This is NOT a 54-row
# source-clause mapping claim: it is the actual committed terms comparison.
term_rows=[]
section='';head=[]
for line in terms.read_text(encoding='utf-8').splitlines():
    if line.startswith('## '):section=line[3:].strip()
    if not line.startswith('| '):continue
    cells=[x.strip() for x in line.split('|')[1:-1]]
    if not cells or all(set(x)<={'-',':',' '} for x in cells):continue
    if cells[0].startswith('Working ') or cells[0].startswith('What we want '):
        head=cells;continue
    if not head or not cells[0].startswith('**'):continue
    label=cells[0].strip('* ')
    if not label:continue
    for i,meaning in enumerate(cells[1:],1):
        if i>=len(head) or not meaning or meaning in ('—','-'):continue
        term_rows.append([section,label,head[i],meaning,'Working donor term comparison; native term and intended scope require clause-level recheck',
            BASE_URL+'Concept_Donor_Comparison/Donor_Terms_Side_by_Side.md'])
assert len(term_rows)>=30, f'Term extraction unexpectedly narrow: {len(term_rows)}'

# The original 182 artifact-level accountability, including exact status, is
# kept as its own sortable worksheet.
artifact_rows=[]
for a in artifact:
    id_=int(a['artifact_id'])
    t=next(x for x in trace if int(x['artifact_id'])==id_)
    artifact_rows.append([id_,a['citation'],a['anatomy_lineage'] or 'UNASSIGNED',
      a['primary_type'],a['concept_review_status'],
      t.get('lineage_review_depth',''),
      t.get('R24_TOPICS_ONLY_not_artifact_level_equivalences',''),
      'NOT ARTIFACT-LEVEL EQUIVALENCE',
      BASE_URL+'Donor_Alignment/03_Source_Accountability_Register.csv#L'+str(id_+1)])

matrix=[]
rids=[r[0] for r in r24]
for row in family_rows:
    matches=set(re.findall(r'R24-\d{2}',row[3]))
    matrix.append([row[0],row[1],*[(f'FAMILY TOPIC' if k in matches else '') for k in rids],
                   'CANDIDATE FAMILY-LEVEL ASSOCIATION; ARTIFACTS NOT INDIVIDUALLY ASSESSED'])
holds=[
 ['Original manufacturer issuer verification','HOLD','Authenticated source/issuer evidence absent; controlled oracles do not prove publisher signatures.'],
 ['OGC CSAPI requirements-class / ATS','HOLD','Native GeoJSON body-schema checks do not equal full advertised OGC class conformance.'],
 ['Portable Profile identifier/governance','HOLD','Project Profile URI tested only on local producer; no globally stable published contract.'],
 ['Independent third-party producer and consumer','HOLD','Actual browser success was one in-house native producer plus one in-house client.'],
 ['Bennett mean producing System','HOLD','Station vs datalogger role for completed mean remains unresolved from original source.'],
 ['Bennett original resultTime','UNKNOWN','Original NOAA CSV does not independently supply result availability time.'],
 ['Bennett exact probe swap','UNKNOWN','Calendar-day history and station maintenance do not give a particular minute.'],
 ['Bennett per-probe location','UNKNOWN','Published station location is not a surveyed point for each EE181 serial.'],
 ['Physical command / authorization / effect','EXCLUDED','Published command support does not validate a safe real physical command chain.'],
 ['Manufacturer references actual installed data','UNKNOWN','Dragino/AirGradient/Campbell design examples are not authenticated fielded units.'],
 ['Artifact-wide donor concept audits','NOT COMPLETE','All 182 record entries are marked NOT_ASSESSED at individual artifact level.'],
 ['IEEE 1451.0-2024 full normative text','PARTIAL','Public scope and Playground evidence inspected; not every 2024 normative SHALL verified.'],
 ['Whole-system source coverage','PARTIAL','Expanded source packet selections do not exhaust documented manufacturer information.'],
 ['Model acceptance and class/cardinality governance','PROPOSED','R24 associations are conditional analytical hypotheses, not adopted universal UML classes.'],
 ['Cloudflare native producer','NOT DEPLOYED','Static Glaux site and local Python native test producer are separate.']
]
readme=[
 ['DIM V2 | SOURCE-QUALIFIED REVIEW WORKBOOK','Status: CANDIDATE / NOT ADOPTED'],
 ['Use this workbook','Open "Family to R24", "Donor Terms", and "R24 Register".'],
 ['Meaning of dots','FAMILY TOPIC means a research lead, NOT individual-artifact equivalent terms.'],
 ['Original artifact accountability','All 182 original records explicitly marked NOT_ASSESSED.'],
 ['Data generation','Generated from actual research branch source CSV and candidate manuscript.'],
 ['Original 54-row workbook','Separate older conversation attachment not byte-copied by this reproducible repository generator.'],
 ['Model UML','GitHub Deliverables/README.md renders diagrams; PlantUML editable source is in Candidate_Specification.'],
 ['Acceptance','Gate E/F remain unclosed; Gate G reviewed with full release not approved.'],
 ['Research README',BASE_URL+'Deliverables/README.md'],
 ['Original DIM R24',BASE_URL+'Candidate_Specification/DIM.md'],
 ['Original donor register',BASE_URL+'Donor_Alignment/03_Source_Accountability_Register.csv']
]
sheetdata=[
 ('READ FIRST',['Topic','Interpretation or link'],readme,[25,100]),
 ('Donor Terms',['Category','Working DIM meaning','Donor original family/standard','Native term or qualification','Review warning','Source'],term_rows,[21,32,28,64,56,72]),
 ('Family to R24',['Donor lineage','Registered artifacts','Depth recorded in review','Candidate R24 topical links','Important limitation','Source'],family_rows,[28,15,55,70,65,75]),
 ('R24 Register',['ID','Original R24 term','Relation direction and proposed meaning','Evidence / false equivalence','Source'],r24,[13,30,78,90,75]),
 ('R24 x Donor Matrix',['Donor lineage','Source artifacts',*rids,'Scope'],matrix,[31,13,*([15]*15),65]),
 ('182 Artifact Inventory',['ID','Original full citation','Original lineage','Original source type','Individual review','Family review standing','Candidate topics only','Claim limitation','Original register URL'],artifact_rows,[9,95,36,40,20,44,70,37,77]),
 ('Open decisions',['Issue','Disposition','What is missing or must NOT be inferred'],holds,[47,20,115])
]

# Small, portable OOXML writer: zipfile/XML only, no opaque runtime, no macros,
# no remote source. Header fills, frozen header rows, filters and bounded widths.
def xs(s):
    return escape(str(s).replace('\x00','').replace('\r',' '),{'"':'&quot;'})
def refcol(n):
    s=''
    while n:n,k=divmod(n-1,26);s=chr(65+k)+s
    return s
def serialize_sheet(headers,rows,widths):
    data=[headers]+rows;pieces=[
      '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
      '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
      '<sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>',
      '<sheetFormatPr defaultRowHeight="17"/><cols>'
    ]
    for i,w in enumerate(widths,1):pieces.append(f'<col min="{i}" max="{i}" width="{min(105,max(8,w))}" customWidth="1"/>')
    pieces+=['</cols><sheetData>']
    for y,row in enumerate(data,1):
        pieces.append(f'<row r="{y}" ht="{26 if y==1 else 20}" customHeight="1">')
        for x,value in enumerate(row,1):
            if value is None or value=='':continue
            key=f'{refcol(x)}{y}';style='1' if y==1 else ('2' if y%2==0 else '0')
            if type(value) in (int,float):
                pieces.append(f'<c r="{key}" s="{style}"><v>{value}</v></c>')
            else:
                pieces.append(f'<c r="{key}" s="{style}" t="inlineStr"><is><t xml:space="preserve">{xs(value)}</t></is></c>')
        pieces.append('</row>')
    pieces.append('</sheetData>')
    if rows and len(headers)>1:
        pieces.append(f'<autoFilter ref="A1:{refcol(len(headers))}{len(data)}"/>')
    pieces.append('</worksheet>')
    return ''.join(pieces).encode('utf-8')
def make_xlsx(destination):
    wb='<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' + '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets>'
    rels=['<?xml version="1.0" encoding="UTF-8"?>','<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">']
    for i,(name,*_) in enumerate(sheetdata,1):
        wb+=f'<sheet name="{xs(name)}" sheetId="{i}" r:id="rId{i}"/>'
        rels.append(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet{i}.xml"/>')
    wb+='</sheets></workbook>'
    rels.append(f'<Relationship Id="rId{len(sheetdata)+1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>')
    rels.append('</Relationships>')
    styles='''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
    <fonts count="2"><font><sz val="10"/><name val="Aptos"/></font><font><b/><sz val="10"/><color rgb="FFFFFFFF"/><name val="Aptos"/></font></fonts>
    <fills count="4"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF19344F"/></patternFill></fill><fill><patternFill patternType="solid"><fgColor rgb="FFF1F6FA"/></patternFill></fill></fills>
    <borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders>
    <cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
    <cellXfs count="3"><xf fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment vertical="center" wrapText="0"/></xf>
      <xf fontId="1" fillId="2" borderId="0" xfId="0" applyFill="1" applyFont="1"><alignment vertical="center" wrapText="1"/></xf>
      <xf fontId="0" fillId="3" borderId="0" xfId="0" applyFill="1"><alignment vertical="center" wrapText="0"/></xf></cellXfs>
    <cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles></styleSheet>'''
    types=['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>','<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">','<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>','<Default Extension="xml" ContentType="application/xml"/>',
      '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>','<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>']
    for i in range(len(sheetdata)):types.append(f'<Override PartName="/xl/worksheets/sheet{i+1}.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>')
    types.append('</Types>')
    with zipfile.ZipFile(destination,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        z.writestr('[Content_Types].xml',''.join(types))
        z.writestr('_rels/.rels','<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr('xl/workbook.xml',wb)
        z.writestr('xl/_rels/workbook.xml.rels',''.join(rels))
        z.writestr('xl/styles.xml',styles)
        for i,(_,heads,rows,widths) in enumerate(sheetdata,1):
            z.writestr(f'xl/worksheets/sheet{i}.xml',serialize_sheet(heads,rows,widths))
    with zipfile.ZipFile(destination) as z:
        assert z.testzip() is None
        assert len([f for f in z.namelist() if f.startswith('xl/worksheets/sheet')])==7

# Render source-grounded two complementary pictures from the same R24 question.
core=r'''digraph G {
graph[rankdir=LR,bgcolor="white",fontname="DejaVu Sans",label="DIM V2 — REFERENTS, EQUIPMENT AND OUTPUTS\nCANDIDATE / NOT ADOPTED / ALL RELATIONS SOURCE-QUALIFIED",labelloc=t,fontsize=18,pad="0.25",nodesep="0.48",ranksep="0.85"];
node[shape=box,style="rounded,filled",fillcolor="#ECF5FA",color="#87A4B8",fontname="DejaVu Sans",fontsize=12];
edge[color="#52768D",fontname="DejaVu Sans",fontsize=10,arrowsize=0.6];
S[label="Original evidence assertion\nissuer / edition / locator",fillcolor="#DCEAF7"];
F[label="FOCAL SUBJECT\nreference, individual or station",fillcolor="#D1E8FA",penwidth=2];
K[label="Product kind / model"];
D[label="Digital description / proxy"];
E[label="Physical or software participant",fillcolor="#E5F4EC"];
H[label="Host / station context",fillcolor="#E5F4EC"];
R[label="Sensing / processing / reporting role",fillcolor="#E5F4EC"];
I[label="Protocol / interface / socket / address"];
O[label="Output fields\nquantity, unit, subject"];
S->F[label="R24-01"];
K->E[label="R24-02",style=dashed];
D->F[label="R24-02",style=dashed];
E->F[label="R24-03 part-of ONLY IF",style=dashed];
E->F[label="R24-04 external connection NOT part-of",style=dotted,color="#33967A",constraint=false];
E->H[label="R24-05",style=dashed];
E->R[label="R24-06",style=dashed];
E->I[label="R24-07",style=dashed];
R->O[label="R24-08",style=dashed];
I->O[label="R24-08",style=dashed,constraint=false];
}'''
activity=r'''digraph G {
graph[rankdir=LR,bgcolor="white",fontname="DejaVu Sans",label="DIM V2 — QUALIFIED STATE, OBSERVATIONS AND HISTORY\nCANDIDATE / UNKNOWN IS NOT A CURRENT STATUS",labelloc=t,fontsize=18,pad="0.25",nodesep="0.45",ranksep="0.88"];
node[shape=box,style="rounded,filled",fillcolor="#F4EDF9",color="#C9B1D7",fontname="DejaVu Sans",fontsize=11];
edge[color="#77588A",fontname="DejaVu Sans",fontsize=10,arrowsize=0.65,style=dashed];
E[label="Equipment / software"];
C[label="Declared capability\nnot an act"];
X[label="Actual request / ACK / effect\nif evidenced"];
S[label="Qualified setting/status\ndefault, applied, reported",fillcolor="#FFF1D5"];
O[label="Original output field"];
A[label="Performed observation\nnot a manual example"];
T[label="Individual service period\noriginal date precision"];
H[label="Host / station"];
M[label="Maintenance/update\ncorrect target"];
Q[label="Power / communications / security"];
D[label="Derived assertion or API copy"];
F[label="Original source record"];
E->S[label="R24-10"];
C->X[label="R24-11"];
O->A[label="R24-09"];
E->T[label="R24-12"];
T->H[label="R24-12"];
M->E[label="R24-13"];
Q->E[label="R24-14"];
D->F[label="R24-15"];
}'''
bennett=r'''digraph G {
graph[rankdir=TB,bgcolor="white",fontname="DejaVu Sans",label="BENNETT'S POINT — SOURCE-QUALIFIED HISTORICAL INSTANCE\n2 original NOAA means; 4 experimental API copies",labelloc=t,fontsize=18,pad="0.3"];
node[shape=box,style="rounded,filled",fontname="DejaVu Sans",fontsize=11,color="#89A4B5",fillcolor="#EAF4F8"];
edge[fontname="DejaVu Sans",fontsize=10,arrowsize=0.6,color="#698899"];
station[label="acebpmet continuing station\nsite location ≠ individual probe location",fillcolor="#D4EBF6"];
probe1[label="EE181 serial 21281600077814\ninitial service; returned 16 Apr 2024"];
probe2[label="EE181 serial 222016000109CE\ninterim service"];
a[label="15 Apr 2024 · 29.1°C\nORIGINAL NOAA MEAN",fillcolor="#F3E4F8"];
b[label="18 Apr 2024 · 27.3°C\nORIGINAL NOAA MEAN",fillcolor="#F3E4F8"];
copyA[label="2 experimental API representations\nfor 15 Apr event",fillcolor="#F8F0E3"];
copyB[label="2 experimental API representations\nfor 18 Apr event",fillcolor="#F8F0E3"];
station->probe1[label="day-granular role"];
station->probe2[label="day-granular role"];
probe2->a[label="likely contributor only\nDERIVED",color="#9362A4",style=dashed];
probe1->b[label="likely contributor only\nDERIVED",color="#9362A4",style=dashed];
a->copyA[label="represents same ORIGINAL",style=dashed];
b->copyB[label="represents same ORIGINAL",style=dashed];
}'''
make_xlsx(OUT/'DIM_V2_Donor_to_Model_Traceability.xlsx')
artifacts=[OUT/'DIM_V2_Donor_to_Model_Traceability.xlsx']
for name,dot in [('DIM_V2_Core_UML',core),('DIM_V2_Activity_UML',activity),('DIM_V2_Bennett_Instance',bennett)]:
    d=OUT/(name+'.dot');d.write_text(dot,encoding='utf-8');artifacts.append(d)
    for fmt in ['svg','png']:
        output=OUT/(name+'.'+fmt)
        subprocess.run(['dot','-T'+fmt,str(d),'-o',str(output)],check=True)
        artifacts.append(output)
# Copy the original editable PlantUML and preserve original accountability CSV.
(OUT/'DIM_V2_Candidate_UML.puml').write_bytes(puml.read_bytes())
artifacts.append(OUT/'DIM_V2_Candidate_UML.puml')
for source,target in [(audit,'DIM_V2_182_Artifact_Accountability.csv')]:
    dst=OUT/target;dst.write_bytes(source.read_bytes());artifacts.append(dst)
zpath=OUT/'DIM_V2_Donor_Mapping_and_UML_Review_Pack.zip'
with zipfile.ZipFile(zpath,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for file in artifacts:z.write(file,file.name)
with zipfile.ZipFile(zpath) as z:assert z.testzip() is None
print('PUBLISHED',len(artifacts),'files plus zip; 182 artifact rows,',
      len(term_rows),'native terminology pairs,',len(family_rows),
      'lineages,',len(r24),'R24 relationships.')
