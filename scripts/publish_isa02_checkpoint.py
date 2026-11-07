#!/usr/bin/env python3
"""Publish the already reviewed ISA-02 checkpoint and verify the committed files.

The workbook was edited/rendered/exported with artifact_tool. This script only
reconstructs that exact export from checksummed lossless byte deltas. It does
not author spreadsheet cells or perform semantic research on the runner.
"""
from __future__ import annotations
import argparse, base64, collections, csv, hashlib, io, json, lzma, os
from pathlib import Path
import re, shutil, struct, subprocess, zipfile
from xml.etree import ElementTree as ET

D=Path('Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk')
REGISTER='ISA_Coverage_Register_07NOV2026.json'
STATUS='ISA_Correction_Status_07NOV2026.json'
PLAN='PLAN_ISA_Coverage_Correction_07NOV2026.md'
PITON='PITON_ISA_Coverage_Correction_07NOV2026.md'
LESSONS='LESSONS_Donor_Review_Process.md'
BOOK='ISA_Correction_Review_ISA02_07NOV2026.xlsx'
VIEW='ISA_Correction_Review_ISA02_07NOV2026.md'
EVIDENCE='ISA02_Identity_and_Properties_Evidence_07NOV2026.json'
REPORT='ISA02_Publication_Record_07NOV2026.json'
HIST='9c4657d355f10da440c0aec18e8d64b665fd1740'
OLD_BOOK='ISA_Correction_Review_ISA01_07NOV2026.xlsx'
PAYLOAD_SHA='47c762545824820fbeb4819dc4f9217c20f8fa395bd83be5e414b8ae006e4e90'
BOOK_SHA='a9fd25f473ed0965b71009a7d2458db3addd495c57d3212471d5a003bf007d30'
FROZEN={
 'Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.xlsx':'bf87c64981bcab1bf0834b032a824fadf3b33783',
 'Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.json':'7f358d6a49ab1f9737e5ef60b731689d439b469b',
 'Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.csv':'fc271b757bcd094866f428bf7c3dc67bee7cc8eb',
 'Step15_ISA6_Primary_Source_Staging_07NOV2026.json':'1f857915c2227e6dc0b071f7db1ded4d3fc09fb4'
}
X='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'


def need(ok,msg):
    if not ok: raise AssertionError(msg)


def sha(b): return hashlib.sha256(b).hexdigest()
def gitsha(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def load(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def dump(path,value): Path(path).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def text(path,value): Path(path).write_text(value.rstrip()+'\n',encoding='utf-8')


def saved_checkpoint():
    encoded=b''.join(subprocess.check_output(['git','show',f'{HIST}:{D}/.isa01_transport/exact{i:02}.txt']).strip() for i in range(1,12))
    need(len(encoded)==158744 and sha(encoded)=='e50c27336d766e8fd307d900d343618d5e683f9b48e556875b88d272a4f63ef3','Historical ISA-01 archive differs')
    data=lzma.decompress(base64.b64decode(encoded,validate=True))
    n=struct.unpack('>I',data[:4])[0]
    records=json.loads(data[4:4+n]); offset=4+n; saved={}
    need(len(records)==14,'Historical saved checkpoint must have fourteen files')
    for r in records:
        name=r['name']; need(Path(name).name==name and name not in saved,'Unsafe source filename')
        b=data[offset:offset+r['size']]; offset+=r['size']
        need(len(b)==r['size'] and sha(b)==r['sha256'],'Historical source hash differs: '+name)
        saved[name]=b
    need(offset==len(data),'Trailing source archive bytes')
    need(sha(saved[OLD_BOOK])=='090d3314a822e1474a9ec32abafd360cb04a09280de55ad369a820424ab3cf5a','Wrong workbook delta base')
    return saved


def payload():
    parts=[(D/'.isa02_transfer'/f'part{i:02}.txt').read_bytes().strip() for i in range(1,5)]
    # Correct the identified two-character transcription duplication, then
    # require the ORIGINAL complete payload hash. No checksum bypass exists.
    if b'QGTFYcece2MNB' in parts[2]:
        need(parts[2].count(b'QGTFYcece2MNB')==1,'Unexpected transfer correction count')
        parts[2]=parts[2].replace(b'QGTFYcece2MNB',b'QGTFYce2MNB')
    b=b''.join(parts)
    need(len(b)==63756 and sha(b)==PAYLOAD_SHA,'ISA-02 transfer bytes differ')
    return json.loads(lzma.decompress(base64.b64decode(b,validate=True)))


def apply_patch(value,operations):
    for op in operations:
        target=value
        for key in op[1][:-1]:target=target[key]
        key=op[1][-1]
        if op[0]=='set':target[key]=op[2]
        elif op[0]=='delete':del target[key]
        elif op[0]=='append':target[key].extend(op[2])
        else:raise AssertionError('Unknown patch operation')
    return value


def csv_write(path,rows):
    with Path(path).open('w',encoding='utf-8',newline='') as handle:
        csv.writer(handle,lineterminator='\n').writerows(rows)


def dict_csv(path,records):
    fields=list(dict.fromkeys(k for row in records for k in row))
    rows=[fields]
    for row in records:
        rows.append([json.dumps(row[k],ensure_ascii=False) if isinstance(row.get(k),(list,dict)) else row.get(k,'') for k in fields])
    csv_write(path,rows)


def restore(p,saved):
    old=load(D/REGISTER)
    baseline=json.loads(saved[REGISTER])
    for key in ['sources','source_blocks','dms_entries','row_targets','legacy_records','review_grid','review_sections','census_method','reconciliation','baseline','legend']:
        need(old[key]==baseline[key],'ISA-01 changed since reviewed baseline: '+key)
    current=apply_patch(baseline,p['coverage_patch'])
    dump(D/REGISTER,current)
    with zipfile.ZipFile(io.BytesIO(saved[OLD_BOOK])) as oldzip:
        for name,r in p['files'].items():
            need(Path(name).name==name,'Unsafe output filename')
            if r['kind']=='utf8':b=r['content'].encode('utf-8')
            else:
                need(r['kind']=='exact_xml_delta','Unknown artifact encoding')
                buffer=io.BytesIO()
                with zipfile.ZipFile(buffer,'w') as output:
                    for member,rec in sorted(r['members'].items()):
                        if 'text' in rec:raw=rec['text'].encode('utf-8')
                        else:
                            previous=oldzip.read(member)
                            need(sha(previous)==rec['base_sha256'],'XLSX source part differs: '+member)
                            raw=b''.join(previous[v['copy'][0]:sum(v['copy'])] if 'copy' in v else v['text'].encode('utf-8') for v in rec['delta'])
                        need(sha(raw)==rec['sha256'],'XLSX restored part differs: '+member)
                        info=zipfile.ZipInfo(member,date_time=(1980,1,1,0,0,0))
                        output.writestr(info,raw,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
                b=buffer.getvalue()
            need(sha(b)==r['sha256'],'Restored file differs: '+name)
            (D/name).write_bytes(b)
    ev=load(D/EVIDENCE)
    for key,name in [('row_targets','ISA_Row_Coverage_07NOV2026.csv'),('legacy_records','ISA_Prior_Findings_Register_07NOV2026.csv'),('source_blocks','ISA_Source_Block_Register_07NOV2026.csv')]:
        dict_csv(D/name,current[key])
    dict_csv(D/'ISA02_Property_Decisions_07NOV2026.csv',ev['primary_records'])
    csv_write(D/'ISA_Correction_Review_ISA02_07NOV2026.csv',current['review_grid'])
    reader=csv.DictReader(io.StringIO(saved['ISA_DMS_Entry_Inventory_07NOV2026.csv'].decode('utf-8')))
    headers=reader.fieldnames+['Source standing','Evidence record','Disposition','Target row','Question','Supporting definition read']
    byid={e['id']:e for e in current['dms_entries']}; rows=[headers]
    for row in reader:
        e=byid[row['ID']]
        row['Semantic review state']=e['semantic_review_status']
        values=list(row.values())+[e.get('source_standing',''),e.get('evidence_record',''),e.get('disposition',''),e.get('target_row',''),e.get('question_id',''),'; '.join(e.get('supporting_definition_checked_in',[]))]
        rows.append(values)
    csv_write(D/'ISA_DMS_Entry_Inventory_07NOV2026.csv',rows)
    for name,wanted in p['expected_sha256'].items():need(sha((D/name).read_bytes())==wanted,'Completed artifact recovery mismatch: '+name)
    return current,ev


def frozen():
    for name,wanted in FROZEN.items():need(gitsha((D/name).read_bytes())==wanted,'Historical v0.9 altered: '+name)


def workbook(data):
    result={}
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        need(z.testzip() is None,'XLSX ZIP corruption')
        for name in z.namelist():
            if name.endswith(('.xml','.rels')):ET.fromstring(z.read(name))
        strings=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            strings=[''.join(t.itertext()) for t in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        rels={x.get('Id'):x.get('Target') for x in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        for s in ET.fromstring(z.read('xl/workbook.xml')).find(X+'sheets'):
            target=rels[s.get(R+'id')]
            path=target.lstrip('/') if target.startswith('/') else 'xl/'+target
            cells={}
            for c in ET.fromstring(z.read(path)).iter(X+'c'):
                need(c.get('t')!='e','Cached spreadsheet error: '+s.get('name')+'!'+c.get('r'))
                v=c.find(X+'v'); inline=c.find(X+'is'); form=c.find(X+'f')
                value=v.text if v is not None else None
                if c.get('t')=='s':value=strings[int(value)]
                elif inline is not None:value=''.join(inline.itertext())
                cells[c.get('r')]=(value,form.text if form is not None else None)
            result[s.get('name')]=cells
    return result


def validate_content():
    frozen();c=load(D/REGISTER);e=load(D/EVIDENCE);state=load(D/STATUS)
    need(len(c['dms_entries'])==480 and len(c['source_blocks'])==279 and len(c['row_targets'])==31 and len(c['legacy_records'])==25,'Original inventory counts changed')
    assigned={x['id'] for x in c['dms_entries'] if x['owner_pass']=='ISA-02'}
    records=e['primary_records'];need(len(assigned)==len(records)==49,'Primary assigned entry count differs')
    need({x['entry_id'] for x in records}==assigned,'Assigned source entries missing or added')
    need(collections.Counter(r['review_status'] for r in records)=={'REVIEWED_SOURCE_SUPPORTED':47,'REVIEWED_QUESTION_RECORDED':2},'47 supported plus 2 specific questions not preserved')
    need(collections.Counter(r['source_standing'] for r in records)=={'CORE':46,'ACCEPTED_EXTENSION':3},'Source standing changed')
    need(len(e['supporting_definitions'])==46 and len(c['candidate_rows'])==45,'Dependencies or candidates missing')
    need({q['native_term'] for q in e['questions']}=={'Level','Link Loss'},'Question identities changed')
    nextentries=[x for x in c['dms_entries'] if x['owner_pass']=='ISA-03']
    need(len(nextentries)==42 and all(x['semantic_review_status']=='NOT_REVIEWED_IN_CORRECTION' for x in nextentries),'ISA-03 improperly advanced')
    need(sum(x['status']=='ISA02_SOURCE_REVIEW_COMPLETE' for x in c['row_targets'])==4,'Four identity review targets not closed')
    need(sum(x['correction_state']=='RECONCILED_ISA02' for x in c['legacy_records'])==1,'UCI reconciliation count differs')
    need(state['technicalIterationsCompleted']==2 and state['nextOnOwnerProceed']=='ISA-03','Progress or next task incorrect')
    prior=list(csv.reader(io.StringIO((D/'Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.csv').read_text(encoding='utf-8'))))
    grid=c['review_grid'];need(len(grid)==93 and all(len(row)==14 for row in grid),'Review geometry changed')
    for i in range(1,len(prior)):
        need(grid[i][:7]+grid[i][8:]==prior[i],'Original equipment/non-ISA display changed at row '+str(i))
    actual=list(csv.reader(io.StringIO((D/'ISA_Correction_Review_ISA02_07NOV2026.csv').read_text(encoding='utf-8'))))
    need(actual==grid,'Readable CSV differs from evidence grid')
    b=(D/BOOK).read_bytes();need(sha(b)==BOOK_SHA,'Workbook not exact validated artifact_tool export')
    sheets=workbook(b)
    need(list(sheets)==['Summary','ISA Review','DMS Inventory','Source Blocks','Row Coverage','Earlier Findings','Sources','Legend','Validation','ISA Evidence','Dependencies','Questions'],'Twelve expected workbook tabs missing')
    for i,row in enumerate(grid,start=6):
        for j,value in enumerate(row):
            ref=chr(65+j)+str(i)
            need((sheets['ISA Review'].get(ref,(None,None))[0] or '')==(str(value) if value is not None else ''),'Workbook review mismatch '+ref)
    counts={'A6':49,'D6':43,'G6':4,'G10':47,'G11':2,'G12':1,'G13':49/480,'G14':0}
    for ref,wanted in counts.items():need(abs(float(sheets['Summary'][ref][0])-wanted)<1e-10,'Summary formula cache mismatch '+ref)
    print('PASS: 49 assigned properties: 47 supported, two specific questions; 46 core and three accepted extensions.')
    print('PASS: 43 supported candidate rows and two question rows visible; UCI separately reconciled; 42 ISA-03 properties untouched.')
    print('PASS: 12-sheet exact exported workbook, formulas and 14-column review; original equipment/non-ISA cells and v0.9 artifacts preserved.')
    return c,e


def pointers(run_url):
    add=D/'ISA02_Lessons_Addendum_07NOV2026.md'
    old=(D/LESSONS).read_text(encoding='utf-8')
    need('## Evidence added at ISA-02' not in old,'ISA-02 lessons already appended')
    text(D/LESSONS,old.rstrip()+'\n\n'+add.read_text(encoding='utf-8'));add.unlink()
    plan=(D/PLAN).read_text(encoding='utf-8')
    plan=plan.replace('**CURRENT: ISA-01 COMPLETE; correction progress 1/12.', '**Historical ISA-01 checkpoint: correction progress 1/12.',1)
    plan=plan.replace('technical correction iterations 1/12','technical correction iterations 2/12',1)
    plan=plan.replace('**Next owner “proceed”: ISA-02 only — identity and the first property block.**','**Next owner “proceed”: ISA-03 only — remaining 42 properties, including Zones and Zoom.**')
    title,body=plan.split('\n',1)
    banner=('\n\n**CURRENT — ISA-02 COMPLETE; correction progress 2/12; next ISA-03 ONLY.** '
      'All 49 assigned properties have recorded outcomes: 47 supported and two precise definition questions. '
      'The new view includes 43 supported candidate rows plus two question rows; UCI reconciliation is separate. '
      f'[Workbook]({BOOK}) · [Review]({VIEW}) · [Evidence]({EVIDENCE}) · [Publication]({REPORT}) · [Lessons]({LESSONS}).\n')
    body=body.replace('The next owner “proceed” begins ISA-02 only; Step16 follows the correction.','ISA-02 is now complete. The next owner “proceed” begins ISA-03 only; Step16 follows the correction.')
    text(D/PLAN,title+banner+body)
    for path,prefix in [(D/'README.md',''),(D/'PLAN_Donor_Concept_to_DIM_Master_Crosswalk_v0.1_05NOV2026.md',''),(D/'PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md',''),(D.parent/'README.md','Donor_DIM_Crosswalk/'),(D.parent/'Deliverables/README.md','../Donor_DIM_Crosswalk/')]:
        old=path.read_text(encoding='utf-8')
        block=('<!-- CURRENT_ISA_CORRECTION_07NOV2026 -->\n\n'
          '**CURRENT — ISA-02 COMPLETE · correction progress 2/12 · next owner “proceed”: ISA-03 ONLY.** '
          'Identity omissions corrected; 49 assigned properties reviewed, 47 supported and two record-local questions. '
          '43 additional source-supported candidate rows and two question rows are visible; other donors and original equipment facts are preserved.\n\n'
          f'[Current workbook]({prefix}{BOOK}) · [Readable review]({prefix}{VIEW}) · [Source evidence]({prefix}{EVIDENCE}) · '
          f'[PITON]({prefix}{PITON}) · [Progress]({prefix}{STATUS}) · [Lessons]({prefix}{LESSONS}) · [Publication]({prefix}{REPORT}).\n\n'
          'ISA-01 census and ISA-02 review remain completed. The next source block is the 42 remaining properties, including Zones and Zoom. '
          'Older 0/12, 1/12, ISA-02-next and Step16-next text below is historical; current plan and PITON control.\n\n'
          '<!-- END_CURRENT_ISA_CORRECTION_07NOV2026 -->')
        pattern=r'(?s)<!-- CURRENT_ISA_CORRECTION_07NOV2026 -->.*?<!-- END_CURRENT_ISA_CORRECTION_07NOV2026 -->'
        need(re.search(pattern,old) is not None,'Current routing marker absent: '+str(path))
        changed=re.sub(pattern,lambda _:block,old,count=1)
        changed=changed.replace('the next current prompt is ISA-02, not Step16','the next current prompt is ISA-03, not Step16')
        changed=re.sub(r'^\*\*NEXT owner “proceed”: ISA-02 ONLY.*$','**NEXT owner “proceed”: ISA-03 ONLY — remaining 42 properties, under the current correction plan.**',changed,flags=re.M)
        text(path,changed)
    # Link publication evidence without changing the completed research narrative.
    for name in [PITON,'ISA02_Identity_and_Properties_07NOV2026.md']:
        body=(D/name).read_text(encoding='utf-8')
        text(D/name,body+'\n\n## Repository verification\n\n[Publication record]('+REPORT+') · [Read-only verification of the published commit]('+run_url+'). The correction remains 2/12; next ISA-03 only.\n')


def verify():
    record=load(D/REPORT)
    for name,wanted in record['published_sha256'].items():need(sha(Path(name).read_bytes())==wanted,'Published file mismatch: '+name)
    validate_content()
    for name in [PITON,PLAN,LESSONS,'ISA02_Identity_and_Properties_07NOV2026.md',VIEW]:
        for link in re.findall(r'\]\(([^)]+)\)',(D/name).read_text(encoding='utf-8')):
            if '://' not in link and not link.startswith('#'):
                need((D/link.split('#',1)[0]).exists(),'Broken publication link '+name+' -> '+link)
    need('L08' in (D/LESSONS).read_text(encoding='utf-8') and 'L09' in (D/LESSONS).read_text(encoding='utf-8'),'Lessons not integrated')
    need('ISA-03' in (D/PITON).read_text(encoding='utf-8')[:300],'Recovery next step incorrect')
    print('PASS: exact committed file identities, source outcomes, lessons and recovery links; ISA-02 COMPLETE, next ISA-03 only.')


def publish():
    frozen()
    need(load(D/STATUS)['nextOnOwnerProceed']=='ISA-02','Unexpected starting checkpoint; do not overwrite newer research')
    protected={str(p):sha(p.read_bytes()) for p in D.glob('*ISA01*') if p.is_file()}
    p=payload();saved=saved_checkpoint();c,e=restore(p,saved)
    validate_content()
    url='https://github.com/OS4CSAPI/glaux-client/actions/runs/'+os.environ.get('GITHUB_RUN_ID','LOCAL_TEST')
    pointers(url)
    for path,wanted in protected.items():need(sha(Path(path).read_bytes())==wanted,'Historical ISA-01 file altered: '+path)
    paths=[D/name for name in p['expected_sha256'] if name!='ISA02_Lessons_Addendum_07NOV2026.md']
    paths += [D/LESSONS,D/PLAN,D/'README.md',D/'PLAN_Donor_Concept_to_DIM_Master_Crosswalk_v0.1_05NOV2026.md',D/'PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md',D.parent/'README.md',D.parent/'Deliverables/README.md']
    record={'checkpoint':'ISA-02','status':'COMPLETE','date':'2026-11-07','repository':'OS4CSAPI/glaux-client','branch':'research/dim-profile-v2','next_task':'ISA-03','technical_iterations_completed':2,'assigned_entries':49,'supported_primary_entries':47,'specific_questions':2,'new_supported_candidate_rows':43,'new_question_rows':2,'earlier_UCI_reconciled':1,'supporting_types_read':46,'workbook_sha256':BOOK_SHA,'workbook_bytes':(D/BOOK).stat().st_size,'workbook_sheets':12,'input_transfer_sha256':PAYLOAD_SHA,'restored_artifact_sha256':p['expected_sha256'],'historical_frozen_blobs':FROZEN,'historical_ISA01_sha256':protected,'source_review':'Original definitions, extension standing and dependencies reviewed before artifact export; see evidence and validation.','local_visual_inspection':'Summary, identity and candidate views inspected before export.','postcommit_verification_run':url,'published_sha256':{str(path):sha(path.read_bytes()) for path in paths}}
    dump(D/REPORT,record);verify();shutil.rmtree(D/'.isa02_transfer')
    print('PASS: completed ISA-02 source work and artifact_tool workbook restored exactly for GitHub publication.')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--verify',action='store_true')
    args=parser.parse_args();verify() if args.verify else publish()
