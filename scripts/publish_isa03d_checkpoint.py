#!/usr/bin/env python3
"""Publish the reviewed ISA-03D artifact_tool export using the existing assembler.
No spreadsheet authoring or semantic research runs on the CI runner.
"""
from __future__ import annotations
import argparse,base64,csv,hashlib,json,lzma,os,re,shutil,subprocess
from pathlib import Path
from publish_isa03a_checkpoint import assemble
from publish_isa02_checkpoint import workbook,frozen
D=Path('Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk')
BASE='e1f2ea2209165e7eae64c14eda6cc66af94a34aa'
BOOK='ISA_Correction_Review_ISA03D_07NOV2026.xlsx'
OLD='ISA_Correction_Review_ISA03C_07NOV2026.xlsx'
EV='ISA03D_Relationship_Visible_Evidence_07NOV2026.json'
REPORT='ISA03D_Publication_Record_07NOV2026.json'
ENC_HASH='9a013b29990edadf75c6f56e7ecb113d369914ccfda9e7688da27599f39b4e6a'
BOOK_HASH='c569018ee166940d205a007da53486492e47e96e3a5bc042ee0e62d463627404'
TARGETS={'ISA-DMS-099','ISA-DMS-118'}
def need(ok,msg):
    if not ok:raise AssertionError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def baseline(name):return subprocess.check_output(['git','show',BASE+':'+str(D/name)])
def decode():
    parts=sorted((D/'.isa03d_transfer').glob('part*.txt'))
    need(len(parts)==3,'Expected three exact transfer segments')
    b=b''.join(p.read_bytes().strip() for p in parts)
    need(len(b)==28812 and sha(b)==ENC_HASH,'Reviewed export transfer hash mismatch')
    p=json.loads(lzma.decompress(base64.b64decode(b,validate=True)))
    need(p['base_commit']==BASE,'Wrong exact input checkpoint')
    return p

def validate():
    frozen()
    prior=json.loads(baseline('ISA_Coverage_Register_07NOV2026.json'))
    r=load(D/'ISA_Coverage_Register_07NOV2026.json');e=load(D/EV);s=load(D/'ISA_Correction_Status_07NOV2026.json')
    need(len(r['dms_entries'])==480 and len(r['source_blocks'])==279 and len(r['row_targets'])==31 and len(r['legacy_records'])==25,'Original source inventory changed')
    for key in ['sources','source_blocks','row_targets','legacy_records','baseline','census_method','reconciliation','specific_questions']:
        need(r[key]==prior[key],'Unrelated source material changed: '+key)
    prev={x['id']:x for x in prior['dms_entries']}
    changed={x['id'] for x in r['dms_entries'] if x['semantic_review_status']!=prev[x['id']]['semantic_review_status']}
    need(changed==TARGETS,'Only Relationship and Visible may advance')
    for x in r['dms_entries']:
        if x['id'] not in TARGETS:need(x['semantic_review_status']==prev[x['id']]['semantic_review_status'],'Other entry advanced')
    need(sum(x['semantic_review_status'].startswith('REVIEWED_') for x in r['dms_entries'])==65,'Reviewed count wrong')
    need(sum(x['semantic_review_status']=='REVIEWED_SOURCE_SUPPORTED' for x in r['dms_entries'])==62,'Supported count wrong')
    need(sum(x['semantic_review_status']=='REVIEWED_QUESTION_RECORDED' for x in r['dms_entries'])==3,'Local question count wrong')
    need({x['entry_id'] for x in e['primary_records']}==TARGETS and len(e['primary_records'])==2,'Evidence scope differs')
    need(all(x['source_standing']=='CORE' and x['disposition']=='CANDIDATE_ROW' for x in e['primary_records']),'Two core supported rows missing')
    need(len(r['candidate_rows'])==61 and r['candidate_rows'][:59]==prior['candidate_rows'],'Old candidate rows changed')
    need(r['progress']['supporting_definitions_read']==47,'Supporting definitions double counted')
    need(len(r['review_grid'])==109 and len(r['review_sections'])==15,'Expected 92 information rows plus group/header rows')
    g=r['review_grid']
    need(g[:62]+g[63:101]+g[102:]==prior['review_grid'],'Earlier non-ISA/case or review cells changed')
    need(g[62][7]=='Relationship' and g[101][7]=='Visible','New native source cells misplaced')
    for row in [g[62],g[101]]:
        need(row[:4]==['Not linked here']*4 and row[4:7]==['Not assessed here']*3 and row[8:13]==['Not assessed here']*5,'Invented donor or case value')
    need('laser' in e['primary_records'][1]['original_meaning'].lower(),'Visible lost its laser-spectrum meaning')
    need('zero' in e['primary_records'][0]['original_meaning'].lower(),'Source child-list0+ cardinality lost')
    with (D/BOOK.replace('.xlsx','.csv')).open(encoding='utf-8',newline='') as f:need(list(csv.reader(f))==g,'CSV/register mismatch')
    with (D/'ISA_DMS_Entry_Inventory_07NOV2026.csv').open(encoding='utf-8',newline='') as f:inv=list(csv.DictReader(f))
    need(len(inv)==480,'Inventory mirror count wrong')
    for x in inv:
        if x['ID'] in TARGETS:need(x['Semantic review state']=='REVIEWED_SOURCE_SUPPORTED','Inventory outcome missing')
    need(sha((D/BOOK).read_bytes())==BOOK_HASH,'Exact authored workbook hash differs')
    oldpub=load(D/'ISA03C_Publication_Record_07NOV2026.json')
    need(sha((D/OLD).read_bytes())==oldpub['workbook_sha256'],'Historical ISA-03C workbook changed')
    a=workbook((D/OLD).read_bytes());b=workbook((D/BOOK).read_bytes())
    need(list(a)==list(b) and len(b)==12,'Worksheet roster changed')
    for sheet in ['Source Blocks','Row Coverage','Earlier Findings','Sources','Legend','Questions']:
        need(b[sheet]==a[sheet],'Untouched worksheet changed: '+sheet)
    for address,value in a['ISA Evidence'].items():
        if address!='A2':need(b['ISA Evidence'].get(address)==value,'Prior evidence changed:'+address)
    for i,row in enumerate(g,6):
        for j,value in enumerate(row):
            need((b['ISA Review'].get(chr(65+j)+str(i),('',None))[0] or '')==str(value or ''),'XLSX/source grid differs')
    for addr,wanted in {'A6':65,'D6':58,'G6':4,'G10':62,'G11':3,'G12':1,'G13':65/480,'G14':0}.items():
        need(abs(float(b['Summary'][addr][0])-wanted)<1e-10,'Summary formula cache wrong:'+addr)
    need(b['Validation']['B20'][0]=='55 / 10','Core/extension split differs')
    need(s['currentBatch']=='ISA-03D' and s['currentBatchDeliveryStatus']=='COMPLETE' and s['nextOnOwnerProceed']=='ISA-03E','Handoff differs')
    need(next(x for x in s['propertyBatches'] if x['id']=='ISA-03E')['state']=='NEXT','ISA-03E must remain unstarted')
    for name in ['PITON_ISA_Coverage_Correction_07NOV2026.md','PLAN_ISA_Coverage_Correction_07NOV2026.md','README.md']:
        text=(D/name).read_text(encoding='utf-8')
        need('ISA-03E' in text[:2200] and BOOK in text,'Stale recovery pointer:'+name)
    for name in ['PITON_ISA_Coverage_Correction_07NOV2026.md','ISA03D_Relationship_Visible_07NOV2026.md',BOOK.replace('.xlsx','.md')]:
        for link in re.findall(r'\]\(([^)]+)\)',(D/name).read_text(encoding='utf-8')):
            if '://' not in link and not link.startswith('#'):need((D/link.split('#',1)[0]).exists(),'Broken local link:'+link)
    print('PASS: only Relationship and Visible reviewed; physical attachment versus laser-spectrum meanings preserved;65 reviewed/62 supported/three unchanged questions.')
    print('PASS:92 information rows,12 worksheets, exact XLSX/CSV/JSON parity and correct formula caches; prior donor/case/evidence values preserved.')
    print('PASS:47 supporting definitions reused, no false later-catalogue completion; ISA-03D complete, ISA-03E next only.')

def verify():
    record=load(D/REPORT)
    for name,digest in record['published_file_sha256'].items():need(sha(Path(name).read_bytes())==digest,'Published file differs:'+name)
    validate()
    print('PASS: read-only verification of exact published commit and all reviewed output hashes.')

def publish():
    p=decode();assemble(p)
    run='https://github.com/OS4CSAPI/glaux-client/actions/runs/'+os.environ['GITHUB_RUN_ID']
    record={'checkpoint':'ISA-03D','state':'COMPLETE','date':'2026-11-07','repository':'OS4CSAPI/glaux-client',
      'branch':'research/dim-profile-v2','base_input_commit':BASE,'next_task':'ISA-03E',
      'assigned_entries':2,'reviewed_entries':2,'new_supported_entries':2,'new_questions':0,
      'primary_entries_reviewed':65,'source_supported_primary':62,'specific_questions':3,
      'candidate_rows':61,'supported_candidate_rows':58,'information_review_rows':92,'unique_supporting_definitions':47,
      'non_ISA_and_equipment_value_changes':0,'workbook':BOOK,'workbook_sha256':BOOK_HASH,
      'workbook_bytes':(D/BOOK).stat().st_size,'workbook_sheets':12,
      'visual_checks':['Summary','physical Relationship candidate row','laser Visible candidate row','shifted group bands'],
      'source_image_inspected':'DMS PDF125 Relationship/Relation Link table',
      'workflow_run_url':run,'postcommit_verification':'Separate read-only job verifies the actual committed checkpoint.',
      'published_file_sha256':{name:r['sha256'] for name,r in p['files'].items()}}
    (D/REPORT).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    validate();shutil.rmtree(D/'.isa03d_transfer')
    print('PASS: exact bounded ISA-03D outputs ready for commit; ISA-03E not reviewed.')
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--verify',action='store_true');args=parser.parse_args()
    verify() if args.verify else publish()
