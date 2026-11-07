#!/usr/bin/env python3
"""Publish the already source-reviewed ISA-03B artifact_tool export.
Reuse ISA-03A's exact-file assembler and read-only workbook parser; no spreadsheet
cells or source meanings are authored by this runner.
"""
from __future__ import annotations
import argparse,base64,csv,hashlib,io,json,lzma,os,re,shutil,subprocess
from pathlib import Path
from publish_isa03a_checkpoint import assemble
from publish_isa02_checkpoint import workbook,frozen
D=Path('Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk')
BASE='d83ae4877d4857122ed849341da2620a58f781bb'
BOOK='ISA_Correction_Review_ISA03B_07NOV2026.xlsx'
OLD='ISA_Correction_Review_ISA03A_07NOV2026.xlsx'
EV='ISA03B_Ownership_Versions_Support_Evidence_07NOV2026.json'
REPORT='ISA03B_Publication_Record_07NOV2026.json'
ENC_HASH='67b5ba59bc775422bf8882da810100925b7bdd40d2a4ef02184c83c377c6030d'
BOOK_HASH='95a174be078c374f4824857a6272747d6b00ce74d516438ae013ca1be18933ca'
TARGETS={'ISA-DMS-084','ISA-DMS-085','ISA-DMS-092','ISA-DMS-108','ISA-DMS-109','ISA-DMS-110'}
def need(ok,msg):
    if not ok:raise AssertionError(msg)
def sha(b):return hashlib.sha256(b).hexdigest()
def load(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def baseline(name):return subprocess.check_output(['git','show',BASE+':'+str(D/name)])
def decode():
    b=b''.join(p.read_bytes().strip() for p in sorted((D/'.isa03b_transfer').glob('part*.txt')))
    need(len(b)==32192 and sha(b)==ENC_HASH,'Exact reviewed transfer checksum mismatch')
    p=json.loads(lzma.decompress(base64.b64decode(b,validate=True)))
    need(p['base_commit']==BASE,'Wrong reviewed input checkpoint')
    return p

def validate():
    frozen()
    old=load(D/'ISA03A_Publication_Record_07NOV2026.json')
    need(sha((D/OLD).read_bytes())==old['workbook_sha256'],'Historical ISA-03A workbook altered')
    prior=json.loads(baseline('ISA_Coverage_Register_07NOV2026.json'))
    r=load(D/'ISA_Coverage_Register_07NOV2026.json');e=load(D/EV);s=load(D/'ISA_Correction_Status_07NOV2026.json')
    need(len(r['dms_entries'])==480 and len(r['source_blocks'])==279 and len(r['row_targets'])==31 and len(r['legacy_records'])==25,'Original source census altered')
    for k in ['sources','source_blocks','row_targets','legacy_records','specific_questions','baseline']:
        need(r[k]==prior[k],'Unrelated source or prior result changed: '+k)
    oldentries={x['id']:x for x in prior['dms_entries']}
    changed={x['id'] for x in r['dms_entries'] if x['semantic_review_status']!=oldentries[x['id']]['semantic_review_status']}
    need(changed==TARGETS,'Exactly the six authorized primary entries must advance')
    need(sum(x['semantic_review_status'].startswith('REVIEWED_') for x in r['dms_entries'])==59,'Reviewed count not 59')
    need(sum(x['semantic_review_status']=='REVIEWED_SOURCE_SUPPORTED' for x in r['dms_entries'])==57,'Supported count not 57')
    need(len(e['primary_records'])==6 and {x['entry_id'] for x in e['primary_records']}==TARGETS,'Evidence scope differs')
    need(sum(x['source_standing']=='ACCEPTED_EXTENSION' for x in e['primary_records'])==5,'Five source extensions not preserved')
    need(next(x for x in e['primary_records'] if x['native_term']=='Specification Version')['source_standing']=='CORE','Specification Version standing differs')
    need(len(r['candidate_rows'])==55 and r['candidate_rows'][:49]==prior['candidate_rows'],'Earlier candidate rows changed')
    need(r['progress']['supporting_definitions_read']==47,'Reused support was double-counted')
    need(len(r['review_grid'])==103 and len(r['review_sections'])==15,'86 information rows plus headers/groups expected')
    need(r['review_grid'][:46]+r['review_grid'][52:]==prior['review_grid'],'Earlier equipment/donor/grid values changed')
    need([x[7] for x in r['review_grid'][46:52]]==['Owner · accepted extension','Parameter Version · accepted extension','Program of Record · accepted extension','Software Version · accepted extension','Specification Version','Support · accepted extension'],'New source terms/positions differ')
    for row in r['review_grid'][46:52]:
        need(row[:4]==['Not linked here']*4 and row[4:7]==['Not assessed here']*3 and row[8:13]==['Not assessed here']*5,'New non-ISA data inferred')
    with (D/BOOK.replace('.xlsx','.csv')).open(encoding='utf-8',newline='') as f:
        need(list(csv.reader(f))==r['review_grid'],'CSV/register mismatch')
    with (D/'ISA_DMS_Entry_Inventory_07NOV2026.csv').open(encoding='utf-8',newline='') as f:
        inv=list(csv.DictReader(f))
    need(len(inv)==480,'CSV inventory size differs')
    for x in inv:
        if x['ID'] in TARGETS:need(x['Semantic review state']=='REVIEWED_SOURCE_SUPPORTED','Inventory CSV missing reviewed state')
    need(sha((D/BOOK).read_bytes())==BOOK_HASH,'Exact authored workbook hash differs')
    b=workbook((D/BOOK).read_bytes());a=workbook((D/OLD).read_bytes())
    need(list(b)==list(a) and len(b)==12,'Worksheet roster changed')
    for sheet in ['Source Blocks','Row Coverage','Earlier Findings','Sources','Legend','Questions']:
        need(b[sheet]==a[sheet],'Untouched worksheet changed: '+sheet)
    for addr,value in a['ISA Evidence'].items():
        if addr!='A2':need(b['ISA Evidence'].get(addr)==value,'Old semantic evidence changed: '+addr)
    for n,row in enumerate(r['review_grid'],6):
        for j,value in enumerate(row):
            need((b['ISA Review'].get(chr(65+j)+str(n),(None,None))[0] or '')==str(value or ''),'Workbook source grid mismatch')
    for addr,wanted in {'A6':59,'D6':53,'G6':4,'G10':57,'G11':2,'G12':1,'G13':59/480,'G14':0}.items():
        need(abs(float(b['Summary'][addr][0])-wanted)<1e-10,'Summary formula differs: '+addr)
    need(b['Validation']['B20'][0]=='51 / 8','Core/extension count differs')
    need(s['nextOnOwnerProceed']=='ISA-03C' and s['currentBatch']=='ISA-03B' and s['currentBatchDeliveryStatus']=='COMPLETE','Handoff routing differs')
    need(next(x for x in s['propertyBatches'] if x['id']=='ISA-03B')['state']=='COMPLETE','ISA-03B not closed')
    need(next(x for x in s['propertyBatches'] if x['id']=='ISA-03C')['state']=='NEXT','ISA-03C should not have started')
    for name in ['PITON_ISA_Coverage_Correction_07NOV2026.md','PLAN_ISA_Coverage_Correction_07NOV2026.md','README.md']:
        text=(D/name).read_text(encoding='utf-8')
        need('ISA-03C' in text[:2200] and BOOK in text,'Current recovery/index stale: '+name)
    for name in ['PITON_ISA_Coverage_Correction_07NOV2026.md','ISA03B_Ownership_Versions_Support_07NOV2026.md',BOOK.replace('.xlsx','.md')]:
        for link in re.findall(r'\]\(([^)]+)\)',(D/name).read_text(encoding='utf-8')):
            if '://' not in link and not link.startswith('#'):need((D/link.split('#',1)[0]).exists(),'Broken repository link: '+link)
    print('PASS: six reviewed ISA-03B properties; five Accepted extensions and one core term; 59 cumulative reviewed/57 supported/two unchanged questions.')
    print('PASS: 86 information rows, 12 worksheets, old grid/evidence retained, exact XLSX/CSV/JSON and calculated summaries match.')
    print('PASS: all original source counts and historical v0.9/ISA-03A work preserved; 47 unique supporting definitions, next ISA-03C only.')

def verify():
    p=load(D/REPORT)
    for name,digest in p['published_file_sha256'].items():need(sha(Path(name).read_bytes())==digest,'Committed artifact differs: '+name)
    validate()
    print('PASS: read-only verification of actual published commit and reviewed artifact hashes.')

def publish():
    p=decode();assemble(p)
    run='https://github.com/OS4CSAPI/glaux-client/actions/runs/'+os.environ['GITHUB_RUN_ID']
    record={'checkpoint':'ISA-03B','state':'COMPLETE','date':'2026-11-07','repository':'OS4CSAPI/glaux-client',
      'branch':'research/dim-profile-v2','base_input_commit':BASE,'next_task':'ISA-03C','assigned_entries':6,
      'reviewed_entries':6,'new_supported_entries':6,'new_questions':0,'primary_entries_reviewed':59,
      'source_supported_primary':57,'existing_questions':2,'candidate_rows':55,'supported_candidate_rows':53,
      'information_review_rows':86,'unique_supporting_definitions':47,'non_ISA_and_equipment_value_changes':0,
      'workbook':BOOK,'workbook_sha256':BOOK_HASH,'workbook_bytes':(D/BOOK).stat().st_size,'workbook_sheets':12,
      'visual_checks':['Summary complete merge extents','six new contact/version candidate rows'],
      'source_image_inspected':'Original DMS PDF page121 POC definition',
      'workflow_run_url':run,'postcommit_verification':'Separate read-only job verifies actual published commit.',
      'published_file_sha256':{name:r['sha256'] for name,r in p['files'].items()}}
    (D/REPORT).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    validate();shutil.rmtree(D/'.isa03b_transfer')
    print('PASS: reviewed ISA-03B workbook and documentation ready for atomic commit.')
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');args=ap.parse_args()
    verify() if args.verify else publish()
