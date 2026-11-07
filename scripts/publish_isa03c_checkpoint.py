#!/usr/bin/env python3
"""Publish the already reviewed ISA-03C artifact_tool export.
Uses the established exact-file assembler and read-only XLSX parser. This runner
neither authors spreadsheet cells nor invents or redoes semantic source review.
"""
from __future__ import annotations
import argparse,base64,csv,hashlib,json,lzma,os,re,shutil,subprocess
from pathlib import Path
from publish_isa03a_checkpoint import assemble
from publish_isa02_checkpoint import workbook,frozen
D=Path('Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk')
BASE='d1d3ab5c607d9f4849df4be38d1eea29c8f65527'
BOOK='ISA_Correction_Review_ISA03C_07NOV2026.xlsx'
OLD='ISA_Correction_Review_ISA03B_07NOV2026.xlsx'
EV='ISA03C_Position_Orientation_Evidence_07NOV2026.json'
REPORT='ISA03C_Publication_Record_07NOV2026.json'
ENC_HASH='b51662746354227870b4de4895a2afd5855803eafa8e9f5e4515b212596f5c39'
BOOK_HASH='fd6d7a8f2d6faafd89688af54cd36c3d7bdebb9f83f6ab71572f30c7ee130c5d'
TARGETS={'ISA-DMS-083','ISA-DMS-086','ISA-DMS-088','ISA-DMS-089'}
def need(ok,msg):
    if not ok:raise AssertionError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def baseline(name):return subprocess.check_output(['git','show',BASE+':'+str(D/name)])
def decode():
    parts=sorted((D/'.isa03c_transfer').glob('part*.txt'))
    need(len(parts)==3,'Expected exactly three checkpoint transfer parts')
    data=b''.join(p.read_bytes().strip() for p in parts)
    need(len(data)==30028 and sha(data)==ENC_HASH,'Exact reviewed ISA-03C transfer checksum mismatch')
    result=json.loads(lzma.decompress(base64.b64decode(data,validate=True)))
    need(result['base_commit']==BASE,'Wrong reviewed input checkpoint')
    return result

def validate():
    frozen()
    old=load(D/'ISA03B_Publication_Record_07NOV2026.json')
    need(sha((D/OLD).read_bytes())==old['workbook_sha256'],'Historical ISA-03B workbook changed')
    prior=json.loads(baseline('ISA_Coverage_Register_07NOV2026.json'))
    r=load(D/'ISA_Coverage_Register_07NOV2026.json');e=load(D/EV);s=load(D/'ISA_Correction_Status_07NOV2026.json')
    need(len(r['dms_entries'])==480 and len(r['source_blocks'])==279 and len(r['row_targets'])==31 and len(r['legacy_records'])==25,'Original census changed')
    for key in ['sources','source_blocks','row_targets','legacy_records','baseline','census_method','reconciliation']:
        need(r[key]==prior[key],'Unrelated source content changed: '+key)
    oldentries={x['id']:x for x in prior['dms_entries']}
    changed={x['id'] for x in r['dms_entries'] if x['semantic_review_status']!=oldentries[x['id']]['semantic_review_status']}
    need(changed==TARGETS,'Exactly four assigned primary entries must advance')
    need(sum(x['semantic_review_status'].startswith('REVIEWED_') for x in r['dms_entries'])==63,'Reviewed total not 63')
    need(sum(x['semantic_review_status']=='REVIEWED_SOURCE_SUPPORTED' for x in r['dms_entries'])==60,'Supported total not 60')
    need(sum(x['semantic_review_status']=='REVIEWED_QUESTION_RECORDED' for x in r['dms_entries'])==3,'Question outcome total not three')
    need(len(e['primary_records'])==4 and {x['entry_id'] for x in e['primary_records']}==TARGETS,'Evidence scope differs')
    need(sum(x['source_standing']=='ACCEPTED_EXTENSION' for x in e['primary_records'])==2,'Two accepted extensions not retained')
    need(sum(x['source_standing']=='CORE' for x in e['primary_records'])==2,'Two core entries not retained')
    need(next(x for x in e['primary_records'] if x['native_term']=='Orientation')['question_id']=='ISA-Q003','Exact Orientation frame question absent')
    need(r['specific_questions'][:-1]==prior['specific_questions'] and r['specific_questions'][-1]['id']=='ISA-Q003','Previous Level/Link Loss questions changed')
    need(len(r['candidate_rows'])==59 and r['candidate_rows'][:55]==prior['candidate_rows'],'Earlier candidate rows changed')
    need(r['progress']['supporting_definitions_read']==47,'Reused supporting types double-counted')
    need(len(r['review_grid'])==107 and len(r['review_sections'])==15,'Expected 90 information rows plus headers/groups')
    need(r['review_grid'][:58]+r['review_grid'][62:]==prior['review_grid'],'Earlier grid/equipment/non-ISA values changed')
    expected=['Orientation · frame question ISA-Q003','Perceived Position · accepted extension','Position','Position Override · accepted extension']
    need([row[7] for row in r['review_grid'][58:62]]==expected,'Four spatial terms or positions differ')
    for row in r['review_grid'][58:62]:
        need(row[:4]==['Not linked here']*4 and row[4:7]==['Not assessed here']*3 and row[8:13]==['Not assessed here']*5,'New external donor/case values inferred')
    with (D/BOOK.replace('.xlsx','.csv')).open(encoding='utf-8',newline='') as f:need(list(csv.reader(f))==r['review_grid'],'CSV/register parity failed')
    with (D/'ISA_DMS_Entry_Inventory_07NOV2026.csv').open(encoding='utf-8',newline='') as f:inv=list(csv.DictReader(f))
    need(len(inv)==480,'Inventory CSV size differs')
    byid={x['id']:x for x in r['dms_entries']}
    for x in inv:
        if x['ID'] in TARGETS:need(x['Semantic review state']==byid[x['ID']]['semantic_review_status'],'CSV source outcome missing')
    need(sha((D/BOOK).read_bytes())==BOOK_HASH,'Exact authored workbook hash differs')
    b=workbook((D/BOOK).read_bytes());a=workbook((D/OLD).read_bytes())
    need(list(b)==list(a) and len(b)==12,'Workbook sheet roster changed')
    for sheet in ['Source Blocks','Row Coverage','Earlier Findings','Sources','Legend']:
        need(b[sheet]==a[sheet],'Untouched worksheet changed: '+sheet)
    for address,value in a['ISA Evidence'].items():
        if address!='A2':need(b['ISA Evidence'].get(address)==value,'Older source evidence changed: '+address)
    for address,value in a['Questions'].items():
        if address not in ['A1','A2']:need(b['Questions'].get(address)==value,'Older question changed: '+address)
    for n,row in enumerate(r['review_grid'],6):
        for j,value in enumerate(row):need((b['ISA Review'].get(chr(65+j)+str(n),(None,None))[0] or '')==str(value or ''),'XLSX grid differs from source')
    for addr,wanted in {'A6':63,'D6':56,'G6':4,'G10':60,'G11':3,'G12':1,'G13':63/480,'G14':0}.items():
        need(abs(float(b['Summary'][addr][0])-wanted)<1e-10,'Calculated summary differs: '+addr)
    need(b['Validation']['B20'][0]=='53 / 10','Core/extension split differs')
    need(s['nextOnOwnerProceed']=='ISA-03D' and s['currentBatch']=='ISA-03C' and s['currentBatchDeliveryStatus']=='COMPLETE','Current handoff differs')
    need(next(x for x in s['propertyBatches'] if x['id']=='ISA-03C')['state']=='COMPLETE','ISA-03C not closed')
    need(next(x for x in s['propertyBatches'] if x['id']=='ISA-03D')['state']=='NEXT','ISA-03D must remain unstarted')
    need('pending' not in s['completedTaskRule'].replace('No pending ISA-03A integration remains.',''),'Stale completed-task warning retained')
    for name in ['PITON_ISA_Coverage_Correction_07NOV2026.md','PLAN_ISA_Coverage_Correction_07NOV2026.md','README.md']:
        content=(D/name).read_text(encoding='utf-8')
        need('ISA-03D' in content[:2200] and BOOK in content,'Current recovery pointer stale: '+name)
    for name in ['PITON_ISA_Coverage_Correction_07NOV2026.md','ISA03C_Position_Orientation_07NOV2026.md',BOOK.replace('.xlsx','.md')]:
        for link in re.findall(r'\]\(([^)]+)\)',(D/name).read_text(encoding='utf-8')):
            if '://' not in link and not link.startswith('#'):need((D/link.split('#',1)[0]).exists(),'Broken repo link: '+link)
    print('PASS: four ISA-03C source outcomes; three supported position roles and one precise Orientation frame question; 63 reviewed/60 supported/three local questions.')
    print('PASS: 90 information rows, 12 worksheets, prior grid/evidence preserved, exact XLSX/CSV/JSON parity and formula caches correct.')
    print('PASS: 47 unique supporting definitions reused without false catalogue completion; source extension/core standing preserved; ISA-03D next only.')

def verify():
    record=load(D/REPORT)
    for name,digest in record['published_file_sha256'].items():need(sha(Path(name).read_bytes())==digest,'Published file differs: '+name)
    validate()
    print('PASS: read-only verification of the actual published commit and reviewed artifact hashes.')

def publish():
    p=decode();assemble(p)
    run='https://github.com/OS4CSAPI/glaux-client/actions/runs/'+os.environ['GITHUB_RUN_ID']
    record={'checkpoint':'ISA-03C','state':'COMPLETE','date':'2026-11-07','repository':'OS4CSAPI/glaux-client',
      'branch':'research/dim-profile-v2','base_input_commit':BASE,'next_task':'ISA-03D','assigned_entries':4,
      'reviewed_entries':4,'new_supported_entries':3,'new_questions':1,'primary_entries_reviewed':63,
      'source_supported_primary':60,'specific_questions':3,'candidate_rows':59,'supported_candidate_rows':56,
      'information_review_rows':90,'unique_supporting_definitions':47,'non_ISA_and_equipment_value_changes':0,
      'workbook':BOOK,'workbook_sha256':BOOK_HASH,'workbook_bytes':(D/BOOK).stat().st_size,'workbook_sheets':12,
      'visual_checks':['Summary','four spatial rows and question styling'],
      'source_image_inspected':'DMS PDF110 Geographic Position; original property-page indexed text read after image access failed',
      'workflow_run_url':run,'postcommit_verification':'Separate read-only job checks the exact published commit.',
      'published_file_sha256':{name:r['sha256'] for name,r in p['files'].items()}}
    (D/REPORT).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    validate();shutil.rmtree(D/'.isa03c_transfer')
    print('PASS: bounded ISA-03C checkpoint ready for publication; no ISA-03D source review executed.')
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--verify',action='store_true');args=parser.parse_args()
    verify() if args.verify else publish()
