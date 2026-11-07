#!/usr/bin/env python3
"""Publish the saved ISA-01 checkpoint without rerunning research.

Lossless transfer is verified before publication-only metadata changes. The XLSX
publication-label update was made with artifact_tool and is transferred as an
exact binary delta. No source mapping, source entry or equipment fact is edited.
"""
from __future__ import annotations
import argparse, base64, collections, csv, hashlib, io, json, os, re, struct
from pathlib import Path
import shutil, xml.etree.ElementTree as ET, zipfile, lzma

D = Path('Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk')
ROOT = D.parent
LESSONS = 'LESSONS_Donor_Review_Process.md'
REPORT = 'ISA01_Publication_Recovery_07NOV2026.json'
BOOK = 'ISA_Correction_Review_ISA01_07NOV2026.xlsx'
PITON = 'PITON_ISA_Coverage_Correction_07NOV2026.md'
PLAN = 'PLAN_ISA_Coverage_Correction_07NOV2026.md'
STATUS = 'ISA_Correction_Status_07NOV2026.json'
REGISTER = 'ISA_Coverage_Register_07NOV2026.json'
PAYLOAD_SHA = 'e50c27336d766e8fd307d900d343618d5e683f9b48e556875b88d272a4f63ef3'
OLD_BOOK = '090d3314a822e1474a9ec32abafd360cb04a09280de55ad369a820424ab3cf5a'
NEW_BOOK = '01052ea7a88e45b62e7668799627cb9672dc1885002ffdfd2275b090f501eed2'
FROZEN = {
 'Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.xlsx':'bf87c64981bcab1bf0834b032a824fadf3b33783',
 'Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.json':'7f358d6a49ab1f9737e5ef60b731689d439b469b',
 'Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.csv':'fc271b757bcd094866f428bf7c3dc67bee7cc8eb',
 'Step15_ISA6_Primary_Source_Staging_07NOV2026.json':'1f857915c2227e6dc0b071f7db1ded4d3fc09fb4',
}
N = {'x':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
ALLOWED_CELLS = {('Summary','A24'),('Legend','B13'),('Validation','A2'),('Validation','B21')}


def need(ok, message):
    if not ok: raise AssertionError(message)


def sha(b): return hashlib.sha256(b).hexdigest()
def gitsha(b): return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def stable(v): return sha(json.dumps(v,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode())
def writejson(path,v): path.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def load_transfer(t: Path):
    parts=[t/f'exact{i:02}.txt' for i in range(1,12)]
    need(all(p.is_file() for p in parts),'A checkpoint transfer part is absent')
    encoded=b''.join(p.read_bytes().strip() for p in parts)
    need(len(encoded)==158744 and sha(encoded)==PAYLOAD_SHA,'Transfer payload hash mismatch')
    raw=lzma.decompress(base64.b64decode(encoded,validate=True))
    hlen=struct.unpack('>I',raw[:4])[0]
    meta=json.loads(raw[4:4+hlen]); offset=4+hlen; files={}
    need(len(meta)==14,'Expected fourteen saved deliverable files')
    for record in meta:
        name=record['name']; need(Path(name).name==name and name not in files,'Unsafe or duplicate file name')
        b=raw[offset:offset+record['size']]; offset+=record['size']
        need(len(b)==record['size'] and sha(b)==record['sha256'],'Saved file hash mismatch: '+name)
        files[name]=b
    need(offset==len(raw),'Trailing bytes in checkpoint')
    need(sha(files[BOOK])==OLD_BOOK,'Original workbook does not match saved artifact')
    patch=json.loads(lzma.decompress(base64.b64decode((t/'publication_workbook_patch.txt').read_bytes(),validate=True)))
    need(patch['source_sha256']==OLD_BOOK and patch['target_sha256']==NEW_BOOK,'Workbook delta identities differ')
    old=files[BOOK]
    new=b''.join(old[x['copy'][0]:sum(x['copy'])] if 'copy' in x else base64.b64decode(x['data'],validate=True) for x in patch['patch'])
    need(sha(new)==NEW_BOOK,'Publication workbook delta hash mismatch')
    a,_=book_cells(old); b,_=book_cells(new)
    changes={(s,c) for s in a for c in set(a[s])|set(b[s]) if a[s].get(c)!=b[s].get(c)}
    need(changes==ALLOWED_CELLS,'Workbook changed something other than four publication labels')
    return files, meta, new


def book_cells(data):
    result={}; grids={}
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        need(z.testzip() is None,'Workbook ZIP integrity failed')
        for p in z.namelist():
            if p.endswith(('.xml','.rels')): ET.fromstring(z.read(p))
        strings=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            strings=[''.join(t.itertext()) for t in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        wb=ET.fromstring(z.read('xl/workbook.xml'))
        sheets=wb.find('x:sheets',N)
        for number,sheet in enumerate(sheets,1):
            name=sheet.get('name'); cells={}; rows={}
            root=ET.fromstring(z.read(f'xl/worksheets/sheet{number}.xml'))
            for row in root.findall('x:sheetData/x:row',N):
                row_values={}
                for c in row:
                    v=c.find('x:v',N); inline=c.find('x:is',N); f=c.find('x:f',N)
                    val=v.text if v is not None else None
                    if c.get('t')=='s': val=strings[int(val)]
                    elif inline is not None: val=''.join(inline.itertext())
                    need(c.get('t')!='e','Excel cached error at '+name+'!'+c.get('r'))
                    cells[c.get('r')]=(val,f.text if f is not None else None)
                    row_values[c.get('r')]=val
                rows[int(row.get('r'))]=row_values
            result[name]=cells;grids[name]=rows
    return result,grids


def check_frozen():
    for name,want in FROZEN.items(): need(gitsha((D/name).read_bytes())==want,'Historical baseline changed: '+name)


def census_checks(register,book):
    need(len(register['dms_entries'])==480,'480 source entries missing')
    need(len(register['sources'])==12 and sum(x.get('cover_verified') is True for x in register['sources'])==11,'Source census metadata differs')
    kinds=collections.Counter(x['source_kind'] for x in register['dms_entries'])
    need(dict(kinds)=={'service':6,'modality':24,'property':91,'observable':39,'command':96,'data element':224},'Source entry category counts differ')
    for key,count in [('source_blocks',279),('row_targets',31),('legacy_records',25)]:
        need(len(register[key])==count,'Inventory size mismatch: '+key)
    for key in ['dms_entries','source_blocks','row_targets','legacy_records']:
        need(all(x.get('owner_pass') for x in register[key]),'Unassigned work: '+key)
    need(len({x['id'] for x in register['dms_entries']})==480,'Duplicate source entry ID')
    need(sum(x['owner_pass']=='ISA-02' for x in register['dms_entries'])==49,'ISA-02 queue changed')
    need(register['checks']['new_semantic_matches']==0,'Unexpected semantic review in publication')
    previous=list(csv.reader(io.StringIO((D/'Master_Donor_Concept_to_DIM_Crosswalk_v0.9_Step15_ISA_07NOV2026.csv').read_text(encoding='utf-8'))))
    current=register['review_grid']
    need(len(previous)==len(current)==39,'Review grid length differs')
    need(current[1][7]=='ISA 6.0 — coverage status','ISA column moved')
    for i in range(1,len(current)):
        need(current[i][:7]+current[i][8:]==previous[i],'Non-ISA display value changed at row '+str(i+1))
    cells,_=book_cells(book)
    need(list(cells)==['Summary','ISA Review','DMS Inventory','Source Blocks','Row Coverage','Earlier Findings','Sources','Legend','Validation'],'Workbook sheets differ')
    review=cells['ISA Review']
    matches=[ref for ref,(v,f) in review.items() if v=='Manufacturer name']
    need(len(matches)==1,'Manufacturer row missing from review')
    for sheet,field,denom in [('DMS Inventory','dms_entries',480),('Source Blocks','source_blocks',279),('Row Coverage','row_targets',31),('Earlier Findings','legacy_records',25)]:
        refs=[ref for ref,(v,f) in cells[sheet].items() if re.fullmatch(r'A\d+',ref) and int(ref[1:])>=5 and v not in (None,'')]
        need(len(refs)==denom,'Workbook inventory rows differ: '+sheet)
    summary=cells['Summary']
    need([summary[k][0] for k in ['A6','D6','G6']]==['480','11','31'],'Workbook cached count formulas differ')
    return {'named_entries':480,'source_blocks':279,'row_targets':31,'earlier_findings':25,'sources':12,'original_2023_sources':11,'non_isa_display_changes':0,'new_semantic_mappings':0,'workbook_sheets':9,'next_task':'ISA-02'}


def replace_section(text,heading,new):
    pattern=r'(?ms)^'+re.escape(heading)+r'\n.*?(?=^## |\Z)'
    revised,n=re.subn(pattern,lambda _:heading+'\n\n'+new.rstrip()+'\n\n',text,count=1)
    need(n==1,'Expected document section missing: '+heading)
    return revised


def publish():
    check_frozen()
    files,meta,book=load_transfer(D/'.isa01_transport')
    stage=json.loads(files[REGISTER]);counts=census_checks(stage,book)
    old_status=json.loads((D/STATUS).read_text(encoding='utf-8'))
    need(old_status.get('technicalIterationsCompleted',0)<=1,'Refusing to overwrite later correction work')
    lessons=(D/LESSONS).read_text(encoding='utf-8')
    need('L01' in lessons and 'L07' in lessons,'Existing approved lessons document missing')
    run_url='https://github.com/OS4CSAPI/glaux-client/actions/runs/'+os.environ['GITHUB_RUN_ID']
    pub={'state':'PUBLISHED_TO_GITHUB','repository':'OS4CSAPI/glaux-client','branch':'research/dim-profile-v2','technical_state':'ISA-01 COMPLETE','next_pass':'ISA-02','publication_record':REPORT,'workflow_run_url':run_url}
    for name,content in files.items(): (D/name).write_bytes(content)
    (D/BOOK).write_bytes(book)
    state=json.loads(files[STATUS]);state['repositoryPublication']=pub
    state['publicationRule']='GitHub is the authoritative checkpoint. Verify the committed workbook, evidence and current PITON after every authorized delivery; sandbox copies do not replace publication.'
    state['lessonsDocument']=LESSONS
    state['documentationCheckpoint']={'state':'COMPLETE','task':'Initial lessons record and ISA-01 GitHub publication recovery','counts_as_new_technical_iteration':False}
    writejson(D/STATUS,state)
    stage['publication']=pub;stage['checks']['github_ci']='See publication record and linked workflow run'
    writejson(D/REGISTER,stage)
    validation=json.loads(files['ISA01_Validation_07NOV2026.json'])
    validation.update({'github_committed':True,'github_ci':run_url,'publication_record':REPORT,'workbook_sha256':NEW_BOOK,'original_workbook_sha256':OLD_BOOK,'publication_label_cells_changed':4})
    writejson(D/'ISA01_Validation_07NOV2026.json',validation)
    text=files['ISA01_Source_Census_07NOV2026.md'].decode()
    text=text.replace('These census/preservation checks are local; no new GitHub Actions run is claimed.','The original census checks passed locally. Publication recovery repeats hash, census-accounting and workbook-preservation checks in GitHub; see the publication record.')
    text=replace_section(text,'## Publication and continuity',f'The completed ISA-01 checkpoint is published on `research/dim-profile-v2`, together with the [lessons record]({LESSONS}) and [publication verification]({REPORT}). The recovery restored the saved fourteen-file checkpoint; it did not repeat the source census. All saved file hashes were checked before publication metadata was updated. The current workbook differs only in four publication-label cells.\n\n**Next owner “proceed”: ISA-02 only — identity and the first property block.**')
    (D/'ISA01_Source_Census_07NOV2026.md').write_text(text,encoding='utf-8')
    text=files[PITON].decode()
    text=replace_section(text,'## Recovery authority and publication',f'**GitHub publication recovered and initial lessons checkpoint COMPLETE.** The repository on `research/dim-profile-v2` is the authoritative current checkpoint: ISA-01 complete, correction progress 1/12, next ISA-02 only. Do not redo ISA-01 because a historical prepublication copy said 0/12 or not committed.\n\nRead [progress]({STATUS}), [census](ISA01_Source_Census_07NOV2026.md), [coverage register]({REGISTER}), [current review](ISA_Correction_Review_ISA01_07NOV2026.md), [editable workbook]({BOOK}), [lessons]({LESSONS}), and [publication record]({REPORT}). The [twelve-pass plan]({PLAN}) remains controlling.\n\n**Publication contract:** use GitHub for every authorized delivery and read back the actual committed files. Sandbox files are additional recovery copies, not the handoff. Separate technical completion from publication, and finish both where the tools support it. Discover the available supported write actions before declaring an access limitation; do not attribute access to a model switch without evidence.\n\n**Lessons maintenance:** add a short lesson only when new evidence appears during the normal ISA closeout. Do not produce a separate report or restart other donors. At ISA-12 consolidate demonstrated practices into a reusable donor-review procedure; adapt it to the next donor rather than copying ISA’s twelve passes mechanically.')
    text=replace_section(text,'## Files and validation',f'The repository contains the workbook, Markdown/CSV review, complete source/row/prior-finding registers, progress, plan amendment and this recovery anchor. The [publication record]({REPORT}) includes saved and published hashes and the [GitHub verification run]({run_url}). Verification checks the restored source-accounting data, unchanged non-ISA display values and all saved artifact identities; it is not a repeat of the semantic source review.\n\n**Next substantive task remains ISA-02.** This publication/lessons checkpoint does not consume another technical correction iteration or authorize ISA-03.')
    (D/PITON).write_text(text,encoding='utf-8')
    name='ISA01_Plan_Amendment_07NOV2026.md';text=files[name].decode()
    text=re.sub(r'\*\*Publication:\*\*.*',f'**Publication:** committed with the recovered ISA-01 checkpoint. See [{REPORT}]({REPORT}); current technical progress remains 1/12 and next ISA-02.',text)
    (D/name).write_text(text,encoding='utf-8')
    name='ISA_Correction_Review_ISA01_07NOV2026.md';text=files[name].decode()
    text=re.sub(r'\*\*Publication state:\*\*.*',f'**Publication state:** GitHub checkpoint restored and verified against the saved census artifacts. [Publication record]({REPORT}) · [Lessons]({LESSONS}). Next ISA-02 only.',text)
    (D/name).write_text(text,encoding='utf-8')
    (D/'ISA01_Repository_Apply_Notes.md').write_text('# ISA-01 publication recovery — applied\n\nThe saved checkpoint has been published to the designated research branch. This is a record of the applied recovery, not an instruction to repeat ISA-01.\n\nSee [publication evidence]('+REPORT+'), [current PITON]('+PITON+'), and [lessons]('+LESSONS+'). All fourteen saved files passed their original hashes before publication-only updates; historical v0.9 files remain unchanged. The current workbook differs only in four publication labels.\n\n**Next technical task: ISA-02 only.**\n',encoding='utf-8')
    lessons+='\n## Verified publication recovery — 7 November 2026\n\nThe interrupted transfer was resumed from ten exact matching segments, not restarted. The completed checkpoint was recovered from its saved archive, every original file hash was verified, and publication labels and recovery routing were updated without changing census results. See [publication record]('+REPORT+') and the [verification run]('+run_url+'). This closes the GitHub-delivery action described in L07; ISA-01 remains complete and ISA-02 remains next.\n'
    (D/LESSONS).write_text(lessons,encoding='utf-8')
    plan=(D/PLAN).read_text(encoding='utf-8')
    plan=plan.replace('technical correction iterations 0/12','technical correction iterations 1/12')
    plan=plan.replace('**Next owner “proceed”: ISA-01 only — source census and coverage register.**','**Next owner “proceed”: ISA-02 only — identity and the first property block.**')
    plan=plan.replace('printed pp.14–17 (PDF pp.29–32)','printed pp.14–18 (PDF pp.29–33)')
    plan=plan.replace('printed pp.18–21 (PDF pp.33–36)','printed pp.18–22 (PDF pp.33–37)')
    title,rest=plan.split('\n',1)
    banner='\n\n**CURRENT: ISA-01 COMPLETE; correction progress 1/12. Publication and initial lessons checkpoint complete; next ISA-02 only.** [Census](ISA01_Source_Census_07NOV2026.md) · [coverage register]('+REGISTER+') · [entry-boundary amendment](ISA01_Plan_Amendment_07NOV2026.md) · [lessons]('+LESSONS+') · [publication]('+REPORT+'). The later semantic review includes full definitions and child fields, not only the 480 named headings.\n'
    plan=title+banner+rest
    plan=plan.replace('This planning checkpoint creates the plan and recovery update only. It does not execute ISA-01, change the workbook, accept the ISA column, or start Step16. The next owner “proceed” begins ISA-01.','Historical planning scope: the initial planning checkpoint created the plan. ISA-01 has now completed and been published. The next owner “proceed” begins ISA-02 only; Step16 follows the correction.')
    (D/PLAN).write_text(plan,encoding='utf-8')
    pointers=[(D/'README.md',''),(D/'PLAN_Donor_Concept_to_DIM_Master_Crosswalk_v0.1_05NOV2026.md',''),(D/'PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md',''),(ROOT/'README.md','Donor_DIM_Crosswalk/'),(ROOT/'Deliverables/README.md','../Donor_DIM_Crosswalk/')]
    for path,prefix in pointers:
        text=path.read_text(encoding='utf-8')
        banner=('<!-- CURRENT_ISA_CORRECTION_07NOV2026 -->\n\n**CURRENT — ISA-01 COMPLETE; correction 1/12. GitHub publication and initial lessons checkpoint complete. Next owner “proceed”: ISA-02 ONLY.**\n\n'
            f'[Current workbook]({prefix}{BOOK}) · [readable comparison]({prefix}ISA_Correction_Review_ISA01_07NOV2026.md) · [census]({prefix}ISA01_Source_Census_07NOV2026.md) · [lessons]({prefix}{LESSONS}) · [PITON]({prefix}{PITON}) · [progress]({prefix}{STATUS}) · [publication verification]({prefix}{REPORT}).\n\n'
            'The recovered census accounts for 480 named source entries, 279 source blocks, 31 row/topic targets and 25 prior ISA findings. No ISA-02 mapping was executed in this publication/lessons checkpoint. Current plan/PITON supersede older planning 0/12 and Step16-next language below; do not repeat ISA-01.\n\n<!-- END_CURRENT_ISA_CORRECTION_07NOV2026 -->')
        pattern=r'(?s)<!-- CURRENT_ISA_CORRECTION_07NOV2026 -->.*?<!-- END_CURRENT_ISA_CORRECTION_07NOV2026 -->'
        if re.search(pattern,text): text=re.sub(pattern,lambda _:banner,text,count=1)
        else:
            title,rest=text.split('\n',1);text=title+'\n\n'+banner+'\n'+rest
        text=text.replace('the next current prompt is ISA-01, not Step16','the next current prompt is ISA-02, not Step16')
        text=re.sub(r'^\*\*NEXT owner “proceed”: ISA-01 ONLY.*$', '**NEXT owner “proceed”: ISA-02 ONLY — identity and first property block, under the current correction plan.**',text,flags=re.M)
        path.write_text(text,encoding='utf-8')
    check_frozen()
    need(stage['dms_entries']==json.loads(files[REGISTER])['dms_entries'],'Source entries changed')
    for key in ['sources','source_blocks','row_targets','legacy_records','review_grid','review_sections','census_method','reconciliation','legend','baseline']:
        need(stage[key]==json.loads(files[REGISTER])[key],'Technical register content changed: '+key)
    record={'checkpoint':'ISA-01','publication_recovery':'COMPLETE','lessons_checkpoint':'COMPLETE','date':'2026-11-07','branch':'research/dim-profile-v2','next_technical_task':'ISA-02','technical_iterations_completed':1,'source_census_repeated':False,'new_semantic_mappings':0,'saved_files_verified':meta,'transfer_payload_sha256':PAYLOAD_SHA,'saved_workbook_sha256':OLD_BOOK,'published_workbook_sha256':NEW_BOOK,'workbook_publication_cells_changed':sorted([list(v) for v in ALLOWED_CELLS]),'historical_baseline_blobs':FROZEN,'counts_verified':counts,'register_technical_sha256':{k:stable(stage[k]) for k in ['sources','source_blocks','dms_entries','census_method','reconciliation','row_targets','legacy_records','review_grid','review_sections','baseline','legend']},'prepublication_checks':'PASS','postcommit_verification_run_url':run_url,'verification_note':'The separate read-only job checks the exact published commit. Consult its conclusion for the postcommit result.'}
    recorded=[D/name for name in files]+[D/PLAN,D/LESSONS]+[p for p,_ in pointers]
    record['published_file_sha256']={str(p):sha(p.read_bytes()) for p in recorded}
    writejson(D/REPORT,record)
    verify()
    shutil.rmtree(D/'.isa01_transport')
    print('PASS: recovered all fourteen saved files and completed publication-only updates.')
    print('PASS: census, mappings, equipment facts and historical v0.9 artifacts preserved.')
    print('PASS: lessons retained and linked; current progress 1/12, next ISA-02.')


def verify():
    record=json.loads((D/REPORT).read_text(encoding='utf-8'))
    check_frozen()
    for path,want in record['published_file_sha256'].items(): need(sha(Path(path).read_bytes())==want,'Published file differs: '+path)
    need(sha((D/BOOK).read_bytes())==NEW_BOOK,'Published workbook bytes differ')
    register=json.loads((D/REGISTER).read_text(encoding='utf-8'))
    for key,want in record['register_technical_sha256'].items(): need(stable(register[key])==want,'Published technical register differs: '+key)
    census_checks(register,(D/BOOK).read_bytes())
    state=json.loads((D/STATUS).read_text(encoding='utf-8'))
    need(state['technicalIterationsCompleted']==1 and state['nextOnOwnerProceed']=='ISA-02','Progress/next task incorrect')
    need(state['repositoryPublication']['state']=='PUBLISHED_TO_GITHUB','Repository publication unresolved')
    for path in [D/PITON,D/PLAN,D/'README.md']:
        text=path.read_text(encoding='utf-8')
        need('ISA-02' in text[:2500] and LESSONS in text,'Recovery routing missing '+str(path))
    for path in [D/PITON,D/PLAN,D/LESSONS,D/'ISA01_Source_Census_07NOV2026.md']:
        for link in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#'):continue
            need((path.parent/link.split('#',1)[0]).exists(),'Broken link '+str(path)+' -> '+link)
    print('PASS: exact committed file hashes, 480/279/31/25 inventories, nine-sheet XLSX, lessons links and recovery routing.')
    print('PASS: saved census retained; only four workbook publication labels changed; next ISA-02, not census restart.')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--verify',action='store_true');args=parser.parse_args()
    verify() if args.verify else publish()
