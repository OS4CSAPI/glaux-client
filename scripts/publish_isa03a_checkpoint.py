#!/usr/bin/env python3
"""Publish the reviewed artifact_tool ISA-03A export; no semantic research.
Reuses the lossless copy/literal and ZIP-member checkpoint method from ISA-02.
Spreadsheet content is authored locally by artifact_tool, never by this runner.
"""
from __future__ import annotations
import argparse,base64,csv,hashlib,io,json,lzma,os,re,shutil,subprocess,zipfile
from pathlib import Path
from publish_isa02_checkpoint import workbook, frozen
D=Path('Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk')
BOOK='ISA_Correction_Review_ISA03A_07NOV2026.xlsx'
OLD='ISA_Correction_Review_ISA02_07NOV2026.xlsx'
REGISTER='ISA_Coverage_Register_07NOV2026.json'
EVIDENCE='ISA03A_Status_Name_State_Evidence_07NOV2026.json'
STATUS='ISA_Correction_Status_07NOV2026.json'
REPORT='ISA03A_Publication_Record_07NOV2026.json'
BASE='bf4d99af17281511a016a1d72757bd2a8a25c95f'
ENC_HASH='892abf54b5c0801927057e77fd9b308721240d9015bf17416781de12ca2b1dc3'
BOOK_HASH='a86a499fd3391a91cb952675324ebad1265e3f0b14bc2f61ec830b1ebde166f0'
TARGETS={'ISA-DMS-078','ISA-DMS-079','ISA-DMS-081','ISA-DMS-082'}

def need(ok,msg):
    if not ok:raise AssertionError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def baseline(name):return subprocess.check_output(['git','show',BASE+':'+str(D/name)])
def patch(a,ops):
    return b''.join(a[x['copy'][0]:sum(x['copy'])] if 'copy' in x else x['text'].encode('utf-8') for x in ops)
def decode():
    raw=b''.join((D/'.isa03a_transfer'/f'part{i:02}.txt').read_bytes().strip() for i in range(1,4))
    need(len(raw)==35496 and sha(raw)==ENC_HASH,'Exact transfer checksum mismatch')
    p=json.loads(lzma.decompress(base64.b64decode(raw,validate=True)))
    need(p['base_commit']==BASE,'Unexpected input checkpoint')
    return p

def assemble(p):
    for path,r in p['files'].items():
        need(path.startswith(str(D)+'/') or path in ['Docs/Research/DIM_Profile_V2/README.md','Docs/Research/DIM_Profile_V2/Deliverables/README.md'],'Unexpected output path')
        need('..' not in Path(path).parts,'Unsafe path')
        if r['kind']=='xlsx_export':
            old=Path(r['base']).read_bytes();need(sha(old)==r['base_sha256'],'Old workbook hash mismatch')
            buf=io.BytesIO()
            with zipfile.ZipFile(io.BytesIO(old)) as source,zipfile.ZipFile(buf,'w') as z:
                for name,m in r['members'].items():
                    if 'copy_from' in m:raw=source.read(m['copy_from'])
                    elif 'delta' in m:
                        a=source.read(name);need(sha(a)==m['base_sha256'],'Old XML mismatch: '+name)
                        raw=patch(a,m['delta'])
                    else:raw=m['text'].encode('utf-8')
                    need(sha(raw)==m['sha256'],'Authored XLSX member mismatch: '+name)
                    info=zipfile.ZipInfo(name,date_time=tuple(m['date_time']))
                    for attr in ['external_attr','create_system','create_version','extract_version','flag_bits','internal_attr']:
                        setattr(info,attr,m[attr])
                    info.extra=base64.b64decode(m['extra'])
                    z.writestr(info,raw,compress_type=zipfile.ZIP_DEFLATED,compresslevel=r['compresslevel'])
            b=buf.getvalue()
        else:
            need(r['kind']=='text_delta','Unexpected artifact kind')
            if 'text' in r:b=r['text'].encode('utf-8')
            else:
                a=Path(r['base']).read_bytes();need(sha(a)==r['base_sha256'],'Input document changed: '+path)
                b=patch(a,r['ops'])
        need(len(b)==r['size'] and sha(b)==r['sha256'],'Exact artifact mismatch: '+path)
        Path(path).write_bytes(b)

def validate():
    frozen()
    oldreg=json.loads(baseline(REGISTER));r=load(D/REGISTER);e=load(D/EVIDENCE);state=load(D/STATUS)
    need(len(r['dms_entries'])==480 and len(r['source_blocks'])==279 and len(r['row_targets'])==31 and len(r['legacy_records'])==25,'Source census changed')
    for key in ['sources','source_blocks','legacy_records','specific_questions','baseline']:
        need(r[key]==oldreg[key],'Original source/category evidence changed: '+key)
    oldentries={x['id']:x for x in oldreg['dms_entries']}
    changed=set()
    for x in r['dms_entries']:
        before=oldentries[x['id']]
        if x['semantic_review_status']!=before['semantic_review_status']:changed.add(x['id'])
        if x['id'] not in TARGETS:need(x['semantic_review_status']==before['semantic_review_status'],'Other source review advanced')
    need(changed==TARGETS,'Exactly the four saved entries must advance')
    need(sum(x['semantic_review_status'].startswith('REVIEWED_') for x in r['dms_entries'])==53,'Primary reviewed count must be 53')
    need(sum(x['semantic_review_status']=='REVIEWED_SOURCE_SUPPORTED' for x in r['dms_entries'])==51,'Supported primary count must be 51')
    need(len(r['candidate_rows'])==49 and r['candidate_rows'][:45]==oldreg['candidate_rows'],'Previous candidates altered')
    for a,b in zip(r['row_targets'],oldreg['row_targets']):need(a['status']==b['status'],'Existing target falsely marked fully reviewed')
    olde=json.loads(baseline(EVIDENCE))
    need(e['supportingDefinitions']==olde['supportingDefinitions'],'Saved supporting meanings changed')
    for a,b in zip(e['decisions'],olde['decisions']):
        need({k:v for k,v in a.items() if k!='integrationState'}=={k:v for k,v in b.items() if k!='integrationState'},'Saved source decision rewritten')
        need(a['integrationState']=='INTEGRATED_CURRENT_WORKBOOK_AND_COVERAGE_REGISTER','Evidence integration flag not closed')
    grid=r['review_grid'];oldgrid=oldreg['review_grid']
    need(len(grid)==97 and len(r['review_sections'])==15,'80 information/review rows plus 15 sections and 2 headers expected')
    for i,row in enumerate(oldgrid):
        offset=(1 if i>=45 else 0)+(1 if i>=56 else 0)+(2 if i>=70 else 0)
        need(grid[i+offset]==row,'Original table row changed: '+str(i))
    need([grid[i][7] for i in [45,57,72,73]]==['Name','Operating State','Maximum Status Interval','Minimum Status Interval'],'New candidate positions or terms differ')
    with (D/'ISA_Correction_Review_ISA03A_07NOV2026.csv').open(encoding='utf-8',newline='') as f:
        need(list(csv.reader(f))==grid,'CSV/register mismatch')
    b=(D/BOOK).read_bytes();need(sha(b)==BOOK_HASH,'Published workbook hash mismatch')
    sheets=workbook(b);prior=workbook((D/OLD).read_bytes())
    need(list(sheets)==list(prior) and len(sheets)==12,'Existing workbook sheet roster changed')
    for sheet in ['Source Blocks','Row Coverage','Earlier Findings','Sources','Legend','Questions']:
        for addr,cell in prior[sheet].items():need(sheets[sheet].get(addr)==cell,'Untouched evidence sheet changed: '+sheet+'!'+addr)
    for addr,cell in prior['ISA Evidence'].items():
        if addr not in ['A1','A2']:need(sheets['ISA Evidence'].get(addr)==cell,'Earlier evidence altered: '+addr)
    for i,row in enumerate(grid,6):
        for j,value in enumerate(row):
            need((sheets['ISA Review'].get(chr(65+j)+str(i),(None,None))[0] or '')==str(value or ''),'Workbook/grid mismatch')
    for ref,wanted in {'A6':53,'D6':47,'G6':4,'G10':51,'G11':2,'G12':1,'G13':53/480,'G14':0}.items():
        need(abs(float(sheets['Summary'][ref][0])-wanted)<1e-10,'Summary calculation differs: '+ref)
    need(state['nextOnOwnerProceed']=='ISA-03B' and state['currentBatchDeliveryStatus']=='COMPLETE','Current checkpoint routing wrong')
    need(next(x for x in state['propertyBatches'] if x['id']=='ISA-03A')['state']=='COMPLETE','ISA-03A not closed')
    need(next(x for x in state['propertyBatches'] if x['id']=='ISA-03B')['state']=='NEXT','ISA-03B unexpectedly started')
    for name in ['PITON_ISA_Coverage_Correction_07NOV2026.md','PLAN_ISA_Coverage_Correction_07NOV2026.md', 'README.md']:
        text=(D/name).read_text(encoding='utf-8');need('ISA-03B' in text[:2000] and BOOK in text,'Recovery/index stale: '+name)
    for name in ['PITON_ISA_Coverage_Correction_07NOV2026.md','ISA03A_Status_Name_State_07NOV2026.md','ISA_Correction_Review_ISA03A_07NOV2026.md']:
        for link in re.findall(r'\]\(([^)]+)\)',(D/name).read_text(encoding='utf-8')):
            if '://' not in link and not link.startswith('#'):need((D/link.split('#',1)[0]).exists(),'Broken current link: '+link)
    print('PASS: exact four saved decisions integrated; 53 reviewed / 51 supported / two existing questions; no additional source research.')
    print('PASS: 80 information/review rows, 12 worksheet roster, old table cells and source evidence preserved; formula caches correct.')
    print('PASS: 480-entry inventory retained; ISA-03A complete, ISA-03B next; actual workbook, ledger and recovery pointers agree.')

def verify():
    report=load(D/REPORT)
    for path,digest in report['published_file_sha256'].items():need(sha(Path(path).read_bytes())==digest,'Committed output differs: '+path)
    validate()
    print('PASS: read-only check of actual published checkpoint; all committed artifact hashes match reviewed outputs.')

def publish():
    p=decode();assemble(p)
    run='https://github.com/OS4CSAPI/glaux-client/actions/runs/'+os.environ['GITHUB_RUN_ID']
    record={'checkpoint':'ISA-03A','state':'COMPLETE','action':'Integration/publication of four saved decisions only','date':'2026-11-07',
      'repository':'OS4CSAPI/glaux-client','branch':'research/dim-profile-v2','base_input_commit':BASE,'next_task':'ISA-03B',
      'source_reviews_repeated':False,'new_semantic_source_reviews':0,'integrated_decisions':4,'primary_entries_reviewed':53,
      'source_supported_primary':51,'existing_questions':2,'candidate_rows':49,'supported_candidate_rows':47,'information_review_rows':80,
      'non_ISA_and_equipment_value_changes':0,'workbook':BOOK,'workbook_sha256':BOOK_HASH,'workbook_bytes':89319,'workbook_sheets':12,
      'artifact_tool_export_sha256':'da7681e5e73a49404a57670273bb732854fba0afe2f3ad4a8511f90d3c366281',
      'packaging':'Deterministic ZIP compression; all artifact_tool-authored member bytes retained exactly.',
      'visual_checks':['Summary','Name row','Operating State row','two Status interval rows'],
      'workflow_run_url':run,'postcommit_verification':'Separate read-only job checks the exact commit; consult job conclusion.',
      'published_file_sha256':{path:r['sha256'] for path,r in p['files'].items()}}
    (D/REPORT).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    validate()
    shutil.rmtree(D/'.isa03a_transfer')
    print('PASS: applied reviewed workbook and documents; transfer staging removed; ready to commit.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--verify',action='store_true');args=parser.parse_args()
    verify() if args.verify else publish()
