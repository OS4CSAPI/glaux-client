#!/usr/bin/env python3
"""Integrate source-qualified SOSA opportunities in the existing master and workbook.
Uses the repository's established OOXML/ZIP publisher helpers to preserve other parts.
--apply is idempotent; --verify checks the saved result without edits.
"""
import copy,csv,hashlib,html,io,json,re,subprocess,sys,zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
import publish_sosa_d as pub

ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'Docs/Research/DIM_Profile_V2/Donor_DIM_Crosswalk'
BOOK='Master_Donor_Concept_to_DIM_Crosswalk.xlsx'
MASTER='Master_Donor_Concept_to_DIM_Crosswalk.json'
LEDGER='SOSA_G4_F_192_Heading_Source_and_Master_Ledger_11NOV2026.json'
SOURCE='SOSA_SO2F_581_Record_Manifest_and_First_58_Assessment_15NOV2026.json'
PITON='PITON_Donor_Concept_to_DIM_Crosswalk_v0.1_05NOV2026.md'
BASE='d55f1462259b0fd72066a551472f1fd68b4c7c92'
SHA0='c66e67d64a1ca1ec8e28a65a99c3f019e17d53087a0e1b0bf68bf1b5ec0aa4d2'
CP='SOSA_SO2F1_SAVED_VERIFIED'
def need(v,s):
    if not v: raise AssertionError('SO2F1: '+s)
def load(n):return json.loads((D/n).read_text(encoding='utf-8'))
def save(n,v):(D/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def digest(b):return hashlib.sha256(b).hexdigest()
def prior(n):return subprocess.check_output(['git','show',BASE+':'+str((D/n).relative_to(ROOT))],cwd=ROOT)
def letter(n):return pub.addr(1,n)[:-1]

def add_candidates(m,source):
    need(len(m['rows'])==393 and len(m['review_grid'])==421 and len(m['columns'])==16,'frozen master shape')
    need(m['currentEvidenceCheckpoint']=='SOSA_SO2E_SAVED_VERIFIED','expected SO-2E checkpoint')
    need(digest((D/BOOK).read_bytes())==SHA0==m['currentWorkbookSha256'],'unchanged verified SO-2E workbook')
    old=json.loads(prior(MASTER))
    need(m['rows']==old['rows'] and m['review_grid']==old['review_grid'],'preserve prior 393 information rows and 421 grid rows')
    need(source['source_manifest']['total']==581 and len(source['source_manifest']['record_refs'])==581,'frozen 581 manifest')
    a=source['SO_2F_1']
    need(a['status']=='SOURCE_ASSESSMENT_RECORDED__CANONICAL_INTEGRATION_NOT_DONE' and len(a['records'])==58,'published 58-record assessment')
    need(a['outcomes']=={'ADEQUATELY_REPRESENTED':4,'ADDITION_WARRANTED_PENDING_INTEGRATION':46,'HELD_EXACT_QUESTION':4,'SOURCE_SPECIFIC_NO_NEW_ROW':4},'four bounded outcome counts')
    native={r['id']:r for r in load('SOSA_G2_6A_Original_Source_Item_Coverage_10NOV2026.json')['original_source_items']}
    for r in a['records']:need(r['id'] in native and r['locator']==native[r['id']]['original_source_locator'],'original ID and locator '+r['id'])
    expected={r[0] for r in source['source_manifest']['record_refs'] if r[1]=='SO-2F-1'}
    need(len(expected)==58 and expected=={r['id'] for r in a['records']},'exact frozen subpacket')
    candidates=a['proposed_candidates']
    need(len(candidates)==3 and sum(len(x['evidence_ids']) for x in candidates)==46,'three distinct candidate meanings')
    allids={r['row_id'] for r in m['rows']}
    for c in candidates:
        need(c['classification']=='SPECIALIZED_CANDIDATE' and c['row_id'] not in allids,'new specialized row')
        ids=c['evidence_ids']
        need(len(ids)==len(set(ids)) and len(ids)==sum(r['id'] in ids and r['outcome']=='ADDITION_WARRANTED_PENDING_INTEGRATION' for r in a['records']),'source-qualified supporting records')
        group=next(g for g in a['groups'] if g['group']==c['group'])
        n=len(m['review_grid'])+1
        display=['Not linked here — no case evidence established.']*4+['Not assessed here — no verified correspondence; not evidence of absence.']*11+['OPTIONAL information-need candidate: '+c['label'].removeprefix('Candidate — ')+' — NOT ADOPTED']
        display[9]='[SPECIALIZED CANDIDATE] PARTIAL / NEW INFORMATION NEED: '+c['definition']+' [C239 Edition 1.1 §13.1–§13.2.5, PDF208–216; SO-2F-1; original source IDs retained; figure/VITA holds.]'
        records=[r for r in a['records'] if r['id'] in ids]
        locs=sorted(set(r['locator'] for r in records))
        mapping={'donor':'The Open Group SOSA C239 Edition 1.1 (2023)','source_ids':ids,
             'original_source_locators':locs,'native_meaning':c['definition'],
             'closest_prior_rows':group['closest_existing_rows'],'reason_for_separate_candidate':group['rationale'],
             'relation':'RELATED_BUT_DISTINCT_ENGINEERING_DESIGN_NOT_INSTALLED_STATE',
             'candidate_status':'SPECIALIZED_CANDIDATE',
             'classification_rationale':'Source-specific hardware design capability, not an adopted universal model field or observed sensor state.',
             'fill':'#F9E6B8','cell':'J'+str(n),'DIM_Profile_adopted':False,
             'case_or_runtime_verified':False,'future_only':False,
             'figure_pixels_audited':False,'native_ANSI_VITA_companions_read':False,'source_manifest_file':SOURCE}
        row={'row_id':c['row_id'],'label':c['label'],'display_row':n,
             'status':'SO-2F-1 provisional specialized information-need candidate; NOT ADOPTED',
             'definition':c['definition'],'source_entry_ids':ids,'evidence_records':ids,
             'master_inclusion':'PROVISIONAL_NATIVE_SOSA_CANDIDATE','dim_adoption':'NO_CONTENT_ADOPTION_DECISION_IN_THIS_UPDATE',
             'source_review_status':'SO2F1_RETAINED_NATIVE_C239_TEXT_REVIEWED__FIGURES_AND_COMPANIONS_HELD',
             'display':display,'SO2_source_correspondence':mapping}
        need(len(display)==16 and all(x.strip() for x in display),'new case/donor cell explicit')
        m['rows'].append(row);m['review_grid'].append(display)
    need(len(m['rows'])==396 and len(m['review_grid'])==424 and len(m['review_sections'])==26,'final 396/424 dimensions')
    return candidates

def workbook(m,candidates):
    olddata=(D/BOOK).read_bytes();q=pub.q;edited={}
    summary={'A1':'CURRENT 15 NOV 2026 — SOSA SO-2F-1 complete',
      'B1':'396 information rows in SAME 26-sheet master. F3 accepted; SOSA bounded PARTIAL; AAS acceptance pending. M00/M01 preserved.',
      'B17':'SO-2F-1: 58 original hardware/profile records assessed. Three specialized candidates added: card input-power design, mechanical/mating profile, cooling/host compatibility.',
      'B19':'396 information rows; 676 classified comparisons: 568 colored and 108 held. Original four figure holds do not add new held comparisons.',
      'B21':'C239 Edition 1.1 PDF208–216 text and tables reviewed; figure geometry and ANSI/VITA companion originals held. No physical-device execution or universal conformance claim.',
      'B22':'New specialized information needs only: electrical input design, hardware geometry/mating, and cooling/host fit. None are adopted DIM/Profile requirements.',
      'B23':'STOP for Proceed; next SO-2F-2 ONLY, 73 power supply card source records. No transition to SO-2F-3 or client deployment.',
      'B28':'6,784 saved crosswalk values; three amber donor cells; all earlier rows, 21 untouched worksheets, manual M00/M01 preserved. Native Excel clean-open unverified.'}
    sheets={'Summary':summary,'Validation':summary,'Legend':{
       'A1':'CURRENT LEGEND — SOSA SO-2F-1, classification is not adoption',
       'B23':'568 colored / 108 held. Three specialized SOSA candidate cells amber; 673 earlier classifications unchanged.',
       'B24':'396 information rows; 424 × 16 comparison grid; 26 prior divider rows preserved.',
       'A28':'Current SO-2F-1 boundary',
       'B28':'58 native source records: 46 support three candidates; four represented; four source-specific/no row; four held figures. STOP before SO-2F-2.'}}
    with zipfile.ZipFile(io.BytesIO(olddata)) as z:
        paths=pub.old.sheetpaths(z);need(len(paths)==26,'original 26 sheets')
        for name in ('Master Crosswalk','DIM Register'):
            path=paths[name];root=ET.fromstring(z.read(path));sd=root.find(q('sheetData'))
            rows={int(r.get('r')):r for r in sd.findall(q('row'))}
            template=rows[421 if name=='Master Crosswalk' else 394]
            for j,c in enumerate(candidates):
                idx=(422+j if name=='Master Crosswalk' else 395+j)
                rr=copy.deepcopy(template);rr.set('r',str(idx));rr.set('ht','330');rr.set('customHeight','1')
                if name=='Master Crosswalk':values=m['review_grid'][421+j]
                else:
                    r=m['rows'][393+j];src=r['SO2_source_correspondence'];ids=', '.join(c['evidence_ids'])
                    values=[r['row_id'],r['label'],r['definition'],r['status'],r['source_review_status'],
                       r['master_inclusion'],r['dim_adoption'],'Not assessed here','Not assessed here',ids,
                       src['relation']+'; '+src['reason_for_separate_candidate'],
                       'C239 Ed1.1 §13.1–§13.2.5 PDF208–216. Figure/ANSI/VITA holds retained.',
                       'Not assessed here','Not assessed here','SPECIALIZED_CANDIDATE; '+c['definition'],
                       ids+'; '+SOURCE+'; '+', '.join(src['original_source_locators']),
                       'Not assessed here','Not assessed here — AAS equivalence unassessed.']
                width=16 if name=='Master Crosswalk' else 18
                need(len(values)==width,'native register width')
                existing={re.match('[A-Z]+',x.get('r')).group():x for x in rr.findall(q('c'))}
                for j2 in range(width):
                    key=letter(j2+1);cell=existing.get(key)
                    if cell is None:cell=ET.SubElement(rr,q('c'),{'r':key+str(idx)})
                    cell.set('r',key+str(idx));pub.f3_put(cell,str(values[j2]))
                sd.append(rr)
            dim=root.find(q('dimension'));need(dim is not None,'master dimension')
            dim.set('ref','A1:'+('P424' if name=='Master Crosswalk' else 'R397'))
            af=root.find(q('autoFilter'))
            if af is not None:af.set('ref',('A2:P424' if name=='Master Crosswalk' else 'A1:R397'))
            edited[path]=ET.tostring(root,encoding='utf-8',xml_declaration=True)
        for name,values in sheets.items():
            root=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in root.iter(q('c'))}
            for ref,value in values.items():
                need(ref in cells,name+' original guidance ref '+ref)
                pub.f3_put(cells[ref],value)
            edited[paths[name]]=ET.tostring(root,encoding='utf-8',xml_declaration=True)
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as out:
            for info in z.infolist():out.writestr(info,edited.get(info.filename,z.read(info.filename)))
    new=buf.getvalue();need(new!=olddata,'workbook changed')
    (D/BOOK).write_bytes(new)
    return digest(new)

def text_mirrors(m):
    grid=m['review_grid']
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/f).open('w',newline='',encoding='utf-8') as h:csv.writer(h,lineterminator='\n').writerows(grid)
    t=['<table><thead><tr>']+[f'<th colspan="{n}">{html.escape(grid[0][i])}</th>' for i,n in ((0,4),(4,6),(10,5),(15,1))]
    t+=['</tr><tr>'+''.join('<th>'+html.escape(v)+'</th>' for v in grid[1])+'</tr></thead><tbody>']
    for i,row in enumerate(grid[2:],2):
        t.append('<tr><th colspan="16">'+html.escape(row[0])+'</th></tr>' if i in m['review_sections'] else '<tr>'+''.join('<td>'+html.escape(v)+'</td>' for v in row)+'</tr>')
    t+=['</tbody></table>']
    banner='# Current comparison — SOSA SO-2F-1, 15 November 2026\n\n396 rows; three specialized source-qualified hardware design candidates, not adopted model requirements. All earlier comparison and classification cells retained. See '+SOURCE+' and G4 ledger for 58 evidence outcomes, original IDs and holds. STOP for SO-2F-2 owner Proceed.\n\n'
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        (D/f).write_text(banner+'\n'.join(t)+'\n',encoding='utf-8')

def routes(src,sha):
    a=src['SO_2F_1']
    a['status']='SAVED_VERIFIED__REMOTE_PUBLICATION_READBACK_PENDING'
    a['workbook_sha256']=sha
    a['master_workbook']='396 rows, same 26 sheets, three amber J422:J424, 424 × 16 saved values; earlier comparisons and holds retained.'
    a['next']='STOP for Proceed; only SO-2F-2 73 source records.'
    save(SOURCE,src)
    old=(D/LEDGER).read_text(encoding='utf-8')
    need(old.endswith('  }\n}\n') and '"SO-2F-1"' not in old,'G4 append-only source ledger preflight')
    entry={'status':'SAVED_VERIFIED__REMOTE_PUBLICATION_READBACK_PENDING',
        'source_manifest_file':SOURCE,'source_ids':[r['id'] for r in a['records']],
        'outcomes':a['outcomes'],'specialized_new_rows':[c['row_id'] for c in a['proposed_candidates']],
        'information_rows':396,'grid_values':6784,'new_sosa_cells':['J422','J423','J424'],
        'workbook_sha256':sha,'holds':'Four figure geometry, ANSI/VITA companions and all prior source holds remain. Not adopted.'}
    txt=old[:-6]+',\n    "SO-2F-1": '+json.dumps(entry,indent=2,ensure_ascii=False).replace('\n','\n    ')+'\n  }\n}\n'
    check=json.loads(txt)
    need(len(check['SO2_source_opportunity_assessments'])==6,'all prior G4 packets preserved')
    (D/LEDGER).write_text(txt,encoding='utf-8')
    p=(D/PITON).read_text(encoding='utf-8')
    p=p.replace('SO-2F-1 partial checkpoint.','SO-2F-1 integrated checkpoint.')
    p=p.replace('but **three proposed specialized rows still require canonical master/Excel integration**. No workbook content has been changed. Continue the same bounded step before SO-2F-2.',
      'and integrated three specialized source-qualified candidates into the same master and Excel. No interrupted SO-2F-1 delivery remains; next packet requires new owner Proceed.')
    p=p.replace('G4-ledger merge is deferred because a 4.7 MB write failed; source checkpoint exists separately without modifying originals.',
      'The existing G4 ledger now routes the published 581-ID manifest and SO-2F-1 source dispositions.')
    p=p.replace('**393 information rows**, **421×16 = 6,736 values**, **673 source classifications: 565 colored/108 held**',
      '**396 information rows**, **424×16 = 6,784 values**, **676 source classifications: 568 colored/108 held**')
    p=p.replace('New SOSA cells J413:J421;','New SO-2F-1 amber SOSA cells J422:J424; prior J413:J421 preserved;')
    p=p.replace('Workbook SHA-256 `'+SHA0+'`;','Current workbook SHA-256 `'+sha+'`; prior SO-2E SHA-256 `'+SHA0+'`;')
    p=p.replace('SO-2F-1 source assessment saved, but **not closed**. **STOP for Proceed**. Next Proceed completes SO-2F-1 canonical integration only: three warranted specialized candidates in master, both CSV/readable mirrors and same 26-sheet workbook; saved-cell/fill parity, publication/readback and G4 routing if feasible. Stop before SO-2F-2. No adoption, donor transition or deployment.',
      'SO-2F-1 assessment and same-master/workbook integration verified locally; remote publication readback still required. **STOP for Proceed.** Next Proceed authorizes **SO-2F-2 only: 73 power-supply-card records**; stop before SO-2F-3. No adoption, donor transition or deployment.')
    need(len(p.split())<=1000 and 'remote publication readback still required' in p,'compact honest PITON')
    (D/PITON).write_text(p,encoding='utf-8')

def verify():
    m=load(MASTER);a=load(SOURCE)
    need(m['currentEvidenceCheckpoint']==CP and len(m['rows'])==396 and len(m['review_grid'])==424,'checkpoint row counts')
    need(m['workbookSnapshot']['color_cell_count']==568 and m['workbookSnapshot']['mixed_source_cells_uncolored']==108,'preserved classification totals')
    base=json.loads(prior(MASTER))
    need(m['rows'][:393]==base['rows'] and m['review_grid'][:421]==base['review_grid'],'prior master data unchanged')
    need(digest((D/BOOK).read_bytes())==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256'],'saved canonical workbook hash')
    need(a['SO_2F_1']['workbook_sha256']==m['currentWorkbookSha256'],'source manifest workbook parity')
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/f).open(encoding='utf-8',newline='') as h:need(list(csv.reader(h))==m['review_grid'],'saved full mirror '+f)
    need((D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_bytes()==(D/'ISA_Correction_Review_07NOV2026.md').read_bytes(),'two readable mirrors identical')
    with zipfile.ZipFile(io.BytesIO(prior(BOOK))) as old,zipfile.ZipFile(D/BOOK) as new:
        need(new.testzip() is None and old.namelist()==new.namelist(),'original ZIP components')
        po=pub.old.sheetpaths(old);pn=pub.old.sheetpaths(new)
        need(len(po)==len(pn)==26 and po==pn,'all original 26 sheets')
        edited={pn[x] for x in ('Master Crosswalk','DIM Register','Summary','Validation','Legend')}
        need(all(old.read(f)==new.read(f) for f in old.namelist() if f not in edited),'21 unchanged sheets and all unrelated OOXML parts')
        q=pub.q
        root=ET.fromstring(new.read(pn['Master Crosswalk']))
        rows={int(r.get('r')):r for r in root.find(q('sheetData')).findall(q('row'))}
        for n,values in enumerate(m['review_grid'],1):
            cells={x.get('r'):x for x in rows[n].findall(q('c'))}
            for j,v in enumerate(values,1):
                key=letter(j)+str(n)
                if key not in cells:
                    need(v=='','missing Excel cell must correspond to an empty canonical value '+key)
                else:
                    need(pub.f3_cell_text(cells[key])==v,'saved crosswalk cell '+key)
        amber=[next(x.get('s') for x in rows[n] if x.get('r')=='J'+str(n)) for n in (421,422,423,424)]
        need(len(set(amber))==1,'all three added SOSA cells use existing specialized amber style')
        root=ET.fromstring(new.read(pn['DIM Register']));rows={int(r.get('r')):r for r in root.find(q('sheetData')).findall(q('row'))}
        for n,row in enumerate(m['rows'][-3:],395):
            need(next(pub.f3_cell_text(x) for x in rows[n] if x.get('r')=='A'+str(n))==row['row_id'],'register entry '+str(n))
        for name in ('Summary','Validation','Legend'):
            root=ET.fromstring(new.read(pn[name]))
            need(any('SO-2F-1' in pub.f3_cell_text(c) for c in root.iter(q('c'))),'current '+name+' sheet')
    l=load(LEDGER)
    need(len(l['SO2_source_opportunity_assessments'])==6 and l['SO2_source_opportunity_assessments']['SO-2F-1']['workbook_sha256']==m['currentWorkbookSha256'],'existing G4 ledger linked')
    need('SO-2F-2 only' in (D/PITON).read_text(),'next owner gate')
    print('PASS SO-2F-1: 396 rows, 424 × 16 grid, J422:J424 amber, 676 classifications, 26 sheets, 21 unmodified sheets, full mirror/source/hold parity.')
    print('LIMIT: Microsoft Excel native reopen and figure/VITA original audit unverified.')

def apply():
    m=load(MASTER)
    if m['currentEvidenceCheckpoint']==CP:
        verify();print('Already published; no further mutations.');return
    a=load(SOURCE);add=add_candidates(m,a);sha=workbook(m,add)
    m['currentWorkbookSha256']=sha;m['currentEvidenceCheckpoint']=CP
    m['counts']['informationRows']=396;m['counts']['SOSA_SO2F1_new_candidate_rows']=3
    m['counts']['SOSA_SO2F1_records_assessed']=58
    m['workbookSnapshot'].update(checkpoint=CP,sha256=sha,information_rows=396,
       textInformationRows=396,text_grid_rows=424,saved_xlsx_grid_rows=424,
       color_cell_count=568,mixed_source_cells_uncolored=108,explicit_unassessed_rows=308,
       lag='ZERO: saved 424 × 16 comparisons and three amber SOSA fills',
       textCheckpoint='SOSA_SO2F1_OPPORTUNITIES',validation_file=LEDGER+'#/SO2_source_opportunity_assessments/SO-2F-1')
    m['nextOwnerAction']='STOP for Proceed: SO-2F-2 only (73 PSC hardware records); no adoption, donor transition or deployment.'
    m['SOSA_SO2F1_opportunity_review']={'status':'SAVED_VERIFIED','manifest':SOURCE,'retained_records':58,
         'added_specialized_rows':[c['row_id'] for c in add],'new_cells':['J422','J423','J424'],
         'workbook_sha256':sha,'prior_source_holds_preserved':True}
    text_mirrors(m);save(MASTER,m);routes(a,sha);verify()


# ---- SO-2F-2 bounded PSC packet: source-assessed 73-record increment ----
BASE2='0c7b5499c85710b699c2f33e14400d9424679de9'
SHA1='c610b1ad7269ff56a5dbd97ba637952b0cbab9c584e9839970ac59a76e4cd49b'
CP2='SOSA_SO2F2_SAVED_VERIFIED'

def prior2(n):
    return subprocess.check_output(['git','show',BASE2+':'+str((D/n).relative_to(ROOT))],cwd=ROOT)

def packet2_preflight(m,src):
    need(m['currentEvidenceCheckpoint']==CP and len(m['rows'])==396 and len(m['review_grid'])==424,'SO2F2 requires exactly published SO2F1 starting master')
    need(m['currentWorkbookSha256']==SHA1 and digest((D/BOOK).read_bytes())==SHA1,'SO2F1 workbook has not drifted')
    before=json.loads(prior2(MASTER))
    need(m['rows']==before['rows'] and m['review_grid']==before['review_grid'],'published SO2F1 master and grid unchanged')
    historical=json.loads(prior2(SOURCE))
    need(src['source_manifest']==historical['source_manifest'] and src['SO_2F_1']==historical['SO_2F_1'],'581 original refs, hashes and first 58 assessments preserved')
    a=src['SO_2F_2']
    need(a['status']=='SOURCE_ASSESSMENT_RECORDED__CANONICAL_INTEGRATION_NOT_DONE','source assessment stage')
    manifest={rec[0]:rec for rec in src['source_manifest']['record_refs'] if rec[1]=='SO-2F-2'}
    need(len(manifest)==73 and len(a['records'])==73 and set(manifest)=={r['id'] for r in a['records']},'exact 73 original IDs and no duplicates')
    native=load('SOSA_G2_6A_Original_Source_Item_Coverage_10NOV2026.json')['original_source_items']
    tally={}
    for r in a['records']:
        ident=r['id']; rec=manifest[ident]
        need(rec[2]=='SOSA_G2_6A_Original_Source_Item_Coverage_10NOV2026.json' and rec[3]==r['source_pointer'] and rec[4]==r['source_sha256_retained'],'frozen ID/pointer/hash '+ident)
        j=int(rec[3].split('/')[-1]);need(native[j]['id']==ident,'source pointer must resolve original source item '+ident)
        need(r['locator']==native[j]['original_source_locator'] and r['source_kind']==native[j]['native_kind'] and r['standing']==native[j]['normative_standing'] and r['pdf_page']==native[j]['original_pdf_page'],'source edition/standing/locator '+ident)
        need(bool(r['native_meaning']) and bool(r['decision_rationale']) and bool(r['closest_existing_rows']),'per-record auditable meaning and closest-row decision '+ident)
        tally[r['outcome']]=tally.get(r['outcome'],0)+1
        if r['outcome']=='HELD_EXACT_QUESTION':need(bool(r.get('exact_hold')),'named hold '+ident)
    need(tally==a['outcomes']=={'ADDITION_WARRANTED_PENDING_INTEGRATION':55,'ADEQUATELY_REPRESENTED':3,'HELD_EXACT_QUESTION':8,'SOURCE_SPECIFIC_NO_NEW_ROW':7},'outcome reconciliation')
    c=a['proposed_candidates']; need(len(c)==3 and sorted(len(x['evidence_ids']) for x in c)==[8,13,34],'three non-arbitrary meanings')
    added={r['id'] for r in a['records'] if r['outcome']=='ADDITION_WARRANTED_PENDING_INTEGRATION'}
    allocated=[ident for x in c for ident in x['evidence_ids']]
    need(len(allocated)==len(added) and len(set(allocated))==len(allocated) and set(allocated)==added,'every warranted source record supports one distinct candidate')
    need(len({x['row_id'] for x in c})==3 and all(x['row_id'] not in {v['row_id'] for v in m['rows']} for x in c),'three new stable IDs')
    return c

def packet2_candidates(m,src):
    candidates=packet2_preflight(m,src)
    for c in candidates:
        i=len(m['review_grid'])+1
        default=['Not linked here — no case evidence established.']*4 + ['Not assessed here — no verified correspondence; not evidence of absence.']*11 + ['OPTIONAL information-need candidate: '+c['label'].removeprefix('Candidate — ')+' — NOT ADOPTED']
        need(len(default)==16 and all(v.strip() for v in default),'all new donor/case/DIM cells explicit')
        ids=c['evidence_ids'];locs=sorted({r['locator'] for r in src['SO_2F_2']['records'] if r['id'] in ids})
        default[9]='[SPECIALIZED CANDIDATE] PARTIAL / NEW INFORMATION NEED: '+c['definition']+' [C239 Edition 1.1 §13.2.6–§13.2.6.6, PDF216–225; SO-2F-2; original source IDs retained; ANSI/VITA and source-cross-reference holds.]'
        mapping={'donor':'The Open Group SOSA C239 Edition 1.1 (2023)','source_ids':ids,'original_source_locators':locs,
           'native_meaning':c['definition'],'closest_prior_rows':c['closest_existing_rows'],
           'reason_for_separate_candidate':c['rationale'],
           'relation':'RELATED_BUT_DISTINCT_PSC_ENGINEERING_INTERFACE_NOT_MEASURED_OR_INSTALLED_STATE',
           'candidate_status':'SPECIALIZED_CANDIDATE','classification_rationale':'Conditional PSC hardware interface/design information; no universal field, installed signal or conformance claim.',
           'fill':'#F9E6B8','cell':'J'+str(i),'DIM_Profile_adopted':False,'case_or_runtime_verified':False,'future_only':False,
           'figure_pixels_audited':False,'native_ANSI_VITA_companions_read':False,'source_manifest_file':SOURCE}
        m['rows'].append({'row_id':c['row_id'],'label':c['label'],'display_row':i,
          'status':'SO-2F-2 provisional specialized information-need candidate; NOT ADOPTED',
          'definition':c['definition'],'source_entry_ids':ids,'evidence_records':ids,
          'master_inclusion':'PROVISIONAL_NATIVE_SOSA_CANDIDATE','dim_adoption':'NO_CONTENT_ADOPTION_DECISION_IN_THIS_UPDATE',
          'source_review_status':'SO2F2_RETAINED_NATIVE_C239_TEXT_TABLES_REVIEWED__COMPANIONS_AND_SOURCE_CONFLICTS_HELD',
          'display':default,'SO2_source_correspondence':mapping})
        m['review_grid'].append(default)
    need(len(m['rows'])==399 and len(m['review_grid'])==427 and len(m['review_sections'])==26,'399 information rows; 427 grid rows; original 26 dividers')
    return candidates

def packet2_workbook(m,candidates):
    olddata=(D/BOOK).read_bytes();q=pub.q;edited={}
    cells_info={
      'Summary':{'A1':'CURRENT 15 NOV 2026 — SOSA SO-2F-2 complete',
        'B1':'399 information rows in SAME 26-sheet master. F3 accepted; SOSA bounded PARTIAL; AAS acceptance pending. M00/M01 preserved.',
        'B17':'SO-2F-2: 73 original power-supply-card records reviewed. Three source-qualified specialized candidate families: PSC power ports, regulation/synchronization interfaces, and utility-control/fault signals.',
        'B19':'399 information rows; 679 classified source comparisons: 571 colored, 108 held. Eight original-source holds do not generate new held classification cells.',
        'B21':'C239 Edition 1.1 PDF216–225 text and connector tables reviewed; native ANSI/VITA companions, source cross-reference conflicts and native Excel clean-open unverified.',
        'B22':'PSC ports and control interfaces are source-scoped design declarations, not reported supply voltage/current, installed battery, issued commands or model requirements.',
        'B23':'STOP for Proceed; next SO-2F-3 ONLY, 36 frozen source records. No advancement to SO-2F-4, donor transition or deployment.',
        'B28':'6,832 saved crosswalk values; three new amber J425:J427 cells; earlier 424 grid rows, 21 untouched worksheets and manual M00/M01 preserved.'},
      'Validation':{'A1':'CURRENT 15 NOV 2026 — SOSA SO-2F-2 complete',
        'B1':'399 information rows in SAME 26-sheet master. Source holds retained. No DIM/Profile adoption.',
        'B17':'SO-2F-2: 73 C239 §13.2.6 source records accounted for; 55 support three distinct specialized candidates, three represented, seven source-specific/no row, eight held.',
        'B19':'399 rows; 679 classified: 571 colored, 108 held. Saved full 427×16 parity is verified.',
        'B21':'Original PDF216–225 text and tables read; 2023 C239 source ambiguities and external ANSI/VITA companions held.',
        'B22':'Source coverage is bounded PARTIAL; neither installed PSC state nor live conformance verified.',
        'B23':'STOP: SO-2F-3 36 original source records requires separate owner Proceed.',
        'B28':'Prior 424 grid rows and 21 unaffected sheets retained; M00/M01 preserved; native Excel clean-open not verified.'},
      'Legend':{'A1':'CURRENT LEGEND — SOSA SO-2F-2; classification is not adoption',
        'B23':'571 colored / 108 held. J425:J427 three specialized SOSA candidate amber cells; 676 earlier classifications unchanged.',
        'B24':'399 information rows; 427 × 16 comparison grid; original 26 topic divider rows preserved.',
        'A28':'Current SO-2F-2 boundary',
        'B28':'73 C239 §13.2.6–§13.2.6.6 records: 55 supporting 3 candidates; 3 represented; 7 source-only; 8 exact holds. STOP before SO-2F-3.'}
    }
    with zipfile.ZipFile(io.BytesIO(olddata)) as z:
        paths=pub.old.sheetpaths(z);need(len(paths)==26,'same 26 original worksheets')
        for sheetname in ('Master Crosswalk','DIM Register'):
            path=paths[sheetname];root=ET.fromstring(z.read(path));sd=root.find(q('sheetData'))
            oldrows={int(rr.get('r')):rr for rr in sd.findall(q('row'))}
            template=oldrows[424 if sheetname=='Master Crosswalk' else 397]
            for j,c in enumerate(candidates):
                idx=(425+j if sheetname=='Master Crosswalk' else 398+j)
                rr=copy.deepcopy(template);rr.set('r',str(idx));rr.set('ht','330');rr.set('customHeight','1')
                if sheetname=='Master Crosswalk':
                    values=m['review_grid'][424+j];width=16
                else:
                    row=m['rows'][396+j];link=row['SO2_source_correspondence'];ids=', '.join(c['evidence_ids'])
                    values=[row['row_id'],row['label'],row['definition'],row['status'],row['source_review_status'],
                      row['master_inclusion'],row['dim_adoption'],'Not assessed here','Not assessed here',ids,
                      link['relation']+'; '+link['reason_for_separate_candidate'],
                      'C239 Ed1.1 §13.2.6 PDF216–225. Original cross-reference, figure/ANSI-VITA holds retained.',
                      'Not assessed here','Not assessed here','SPECIALIZED_CANDIDATE; '+c['definition'],
                      ids+'; '+SOURCE+'; '+', '.join(link['original_source_locators']),
                      'Not assessed here','Not assessed here — AAS equivalence unassessed.'];width=18
                need(len(values)==width,'original register/review sheet columns preserved')
                cc={re.match('[A-Z]+',x.get('r')).group():x for x in rr.findall(q('c'))}
                for j2,v in enumerate(values):
                    letterj=letter(j2+1);cell=cc.get(letterj)
                    if cell is None:cell=ET.SubElement(rr,q('c'),{'r':letterj+str(idx)})
                    cell.set('r',letterj+str(idx));pub.f3_put(cell,str(v))
                sd.append(rr)
            dim=root.find(q('dimension'));need(dim is not None,'native worksheet dimension')
            dim.set('ref','A1:'+('P427' if sheetname=='Master Crosswalk' else 'R400'))
            af=root.find(q('autoFilter'))
            if af is not None:af.set('ref','A2:P427' if sheetname=='Master Crosswalk' else 'A1:R400')
            edited[path]=ET.tostring(root,encoding='utf-8',xml_declaration=True)
        for sheetname,fields in cells_info.items():
            root=ET.fromstring(z.read(paths[sheetname]));cells={c.get('r'):c for c in root.iter(q('c'))}
            for address,val in fields.items():
                need(address in cells,'preserve original summary guidance cell '+sheetname+'!'+address)
                pub.f3_put(cells[address],val)
            edited[paths[sheetname]]=ET.tostring(root,encoding='utf-8',xml_declaration=True)
        outbytes=io.BytesIO()
        with zipfile.ZipFile(outbytes,'w') as zout:
            for info in z.infolist():zout.writestr(info,edited.get(info.filename,z.read(info.filename)))
    result=outbytes.getvalue();need(result!=olddata,'changed workbook expected')
    (D/BOOK).write_bytes(result)
    return digest(result)

def packet2_text(m):
    text_mirrors(m)
    banner=('# Current comparison — SOSA SO-2F-2, 15 November 2026\n\n'
       '399 rows; three additional specialized source-qualified PSC design/interface candidates, not adopted model requirements. '
       'All prior 424 comparison rows, earlier classifications, evidence and holds retained. '
       'See '+SOURCE+' SO_2F_2 and existing G4 ledger for 73 original IDs/outcomes. '
       'STOP for SO-2F-3 owner Proceed.\n\n')
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        p=D/f;txt=p.read_text(encoding='utf-8');pos=txt.find('<table>')
        need(pos>0,'readable comparison table preserved')
        p.write_text(banner+txt[pos:],encoding='utf-8')

def packet2_routes(src,sha):
    a=src['SO_2F_2'];a['status']='SAVED_VERIFIED__REMOTE_PUBLICATION_READBACK_PENDING'
    a['workbook_sha256']=sha
    a['master_workbook']='399 rows; same 26 worksheets, J425:J427 amber; 427 × 16 saved grid values. All earlier evidence/classifications retained.'
    a['next']='STOP for owner Proceed; only SO-2F-3 (36 source records).'
    save(SOURCE,src)
    old=(D/LEDGER).read_text(encoding='utf-8')
    need(old.endswith('  }\n}\n') and '"SO-2F-2"' not in old,'G4 source ledger append-only boundary')
    entry={'status':a['status'],'source_manifest_file':SOURCE,'source_ids':[r['id'] for r in a['records']],
       'outcomes':a['outcomes'],'candidate_groups':[{ 'row_id':x['row_id'],'source_record_count':len(x['evidence_ids'])} for x in a['proposed_candidates']],
       'specialized_new_rows':[x['row_id'] for x in a['proposed_candidates']],
       'information_rows':399,'grid_values':6832,'new_sosa_cells':['J425','J426','J427'],
       'workbook_sha256':sha,'holds':'Eight precise original/source-companion questions plus all earlier source holds retained. Not adopted.'}
    newtxt=old[:-6]+',\n    "SO-2F-2": '+json.dumps(entry,indent=2,ensure_ascii=False).replace('\n','\n    ')+'\n  }\n}\n'
    check=json.loads(newtxt);need(len(check['SO2_source_opportunity_assessments'])==7,'six earlier source packets plus new packet retained')
    (D/LEDGER).write_text(newtxt,encoding='utf-8')
    p=(D/PITON).read_text(encoding='utf-8')
    p=p.replace('SO-2F-1 integrated checkpoint.','SO-2F-2 integrated checkpoint.')
    p=p.replace('SO-2E fully published. SO-2F-1 has verified a frozen 581-ID/pointer manifest and assessed 58 native records, and integrated three specialized source-qualified candidates into the same master and Excel. No interrupted SO-2F-1 delivery remains; next packet requires new owner Proceed.',
       'SO-2E and SO-2F-1 published. SO-2F-2 assessed 73 frozen original IDs and integrated three more specialized, unadopted candidates in the same master/workbook. No interrupted local assessment remains; remote readback pending.')
    start=p.index('**SO-2F-1 source checkpoint:**');end=p.index('\n\n## Master and workbook',start)
    p=p[:start]+('**SO-2F source checkpoint:** Existing '+SOURCE+' preserves the frozen 581-ID/eight-source-file manifest and SO-2F-1 dispositions. '
      'SO-2F-2 covers 73 C239 §13.2.6 records, original PDF216–225 text and pin tables: '
      '55 source records support three new specialized PSC power-port, regulation/sync and utility-control candidate families; '
      '3 are represented, 7 source-specific/no row and 8 held. No record omitted or reassigned. '
      'Source cross-reference/pin-name conflicts, ANSI/VITA originals, figure pixels, installation, measured state and conformance remain held. '
      'Remaining SO-2F is 450 IDs; next separate owner Proceed reaches SO-2F-3 only (36 IDs).')+p[end:]
    p=p.replace('**396 information rows**, **424×16 = 6,784 values**, **676 source classifications: 568 colored/108 held**',
       '**399 information rows**, **427×16 = 6,832 values**, **679 source classifications: 571 colored/108 held**')
    p=p.replace('New SO-2F-1 amber SOSA cells J422:J424; prior J413:J421 preserved;',
       'New SO-2F-2 amber SOSA cells J425:J427; prior J422:J424 and J413:J421 preserved;')
    p=p.replace('Current workbook SHA-256 \x60'+SHA1+'\x60; prior SO-2E SHA-256',
       'Current workbook SHA-256 \x60'+sha+'\x60; prior SO-2F-1 SHA-256 \x60'+SHA1+'\x60; SO-2E SHA-256')
    p=p.replace('SO-2F-1 publisher checked 6,784 saved grid values, three amber cells, 21 unchanged sheets and preserved earlier rows.',
       'SO-2F-2 publisher checked 6,832 saved grid values, three new amber cells, 21 unchanged sheets and preserved all 424 earlier grid rows. Prior SO-2F-1 publisher checked 6,784 saved grid values, three earlier amber cells and 21 unchanged sheets.')
    start=p.index('## Next action and stop');end=p.index('\n\n## History',start)
    p=p[:start]+('## Next action and stop\n\n'
      'SO-2F-2 assessment and same-master/workbook integration verified locally by publication workflow; '
      '**remote publication/readback pending**. STOP for Proceed. '
      '**Next Proceed authorizes SO-2F-3 only: 36 frozen original source records.** '
      'No adoption, donor transition, client work or deployment.')+p[end:]
    need(len(p.split())<=1000 and 'SO-2F-3' in p and 'remote publication/readback pending' in p,'PITON compact status, correct next owner gate')
    (D/PITON).write_text(p,encoding='utf-8')

def packet2_verify():
    m=load(MASTER);s=load(SOURCE);a=s['SO_2F_2']
    need(m['currentEvidenceCheckpoint']==CP2 and len(m['rows'])==399 and len(m['review_grid'])==427,'verified current master 399/427')
    need(m['workbookSnapshot']['color_cell_count']==571 and m['workbookSnapshot']['mixed_source_cells_uncolored']==108,'classification totals preserved')
    previous=json.loads(prior2(MASTER))
    need(m['rows'][:396]==previous['rows'] and m['review_grid'][:424]==previous['review_grid'],'all old rows and 6,784 original comparison values retained')
    pastsrc=json.loads(prior2(SOURCE))
    need(s['source_manifest']==pastsrc['source_manifest'] and s['SO_2F_1']==pastsrc['SO_2F_1'],'frozen 581 IDs and previous 58 disposition evidence preserved')
    need(len(a['records'])==73 and sum(a['outcomes'].values())==73 and len(a['proposed_candidates'])==3,'73 outcomes and three candidate families')
    for j,c in enumerate(a['proposed_candidates']):
        row=m['rows'][396+j]
        need(row['row_id']==c['row_id'] and row['source_entry_ids']==c['evidence_ids'] and row['SO2_source_correspondence']['cell']=='J'+str(425+j),'source-to-master candidate link')
        need(row['display']==m['review_grid'][424+j] and all(bool(v.strip()) for v in row['display']),'new row has 16 explicit statuses')
    sha=digest((D/BOOK).read_bytes())
    need(sha==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==a['workbook_sha256'],'saved workbook hash equality')
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/f).open(encoding='utf-8',newline='') as h:need(list(csv.reader(h))==m['review_grid'],'complete saved CSV comparison parity '+f)
    need((D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_bytes()==(D/'ISA_Correction_Review_07NOV2026.md').read_bytes(),'two readable mirrors identical')
    with zipfile.ZipFile(io.BytesIO(prior2(BOOK))) as before,zipfile.ZipFile(D/BOOK) as after:
        need(after.testzip() is None and before.namelist()==after.namelist(),'entire XLSX ZIP parts valid/preserved')
        prevpaths=pub.old.sheetpaths(before);newpaths=pub.old.sheetpaths(after)
        need(len(prevpaths)==len(newpaths)==26 and prevpaths==newpaths,'26 identical sheet names/order')
        editing={newpaths[t] for t in ('Master Crosswalk','DIM Register','Summary','Validation','Legend')}
        need(all(before.read(part)==after.read(part) for part in before.namelist() if part not in editing),'21 worksheets and all unrelated OOXML parts byte-preserved')
        root=ET.fromstring(after.read(newpaths['Master Crosswalk']));q=pub.q
        rows={int(rr.get('r')):rr for rr in root.find(q('sheetData')).findall(q('row'))}
        for i,vals in enumerate(m['review_grid'],1):
            cc={cell.get('r'):cell for cell in rows[i].findall(q('c'))}
            for j,v in enumerate(vals,1):
                name=letter(j)+str(i)
                if name in cc:need(pub.f3_cell_text(cc[name])==v,'saved Excel equality '+name)
                else:need(v=='','unpopulated saved cell '+name)
        need(all(next(x.get('s') for x in rows[i] if x.get('r')=='J'+str(i))==next(x.get('s') for x in rows[424] if x.get('r')=='J424') for i in (425,426,427)), 'amber specialized source fills J425:J427')
        root=ET.fromstring(after.read(newpaths['DIM Register']))
        rr={int(x.get('r')):x for x in root.find(q('sheetData')).findall(q('row'))}
        for j,c in enumerate(a['proposed_candidates']):
            i=398+j
            need(next(pub.f3_cell_text(x) for x in rr[i].findall(q('c')) if x.get('r')=='A'+str(i))==c['row_id'],'DIM Register new stable row '+str(i))
        for name in ('Summary','Validation','Legend'):
            root=ET.fromstring(after.read(newpaths[name]))
            need(any('SO-2F-2' in pub.f3_cell_text(c) for c in root.iter(q('c'))),'current '+name+' source boundary')
    ledger=load(LEDGER)
    need(len(ledger['SO2_source_opportunity_assessments'])==7 and ledger['SO2_source_opportunity_assessments']['SO-2F-2']['workbook_sha256']==sha,'append-only G4 SO-2F-2 linked')
    need('SO-2F-3 only' in (D/PITON).read_text(),'next explicit owner Proceed boundary')
    print('PASS SO-2F-2: 73 original IDs, 55 supports/3 represented/7 source-only/8 held, 399 rows, 427×16 values, J425:J427 amber, 679 classifications, same 26 sheets, prior 424 rows and 21 sheets preserved.')
    print('LIMIT: native Microsoft Excel clean-open, ANSI/VITA companions, original ambiguities and any runtime/conformance unverified.')

def packet2_apply():
    m=load(MASTER);src=load(SOURCE)
    if m['currentEvidenceCheckpoint']==CP2:
        packet2_verify();print('Already saved; no further mutations.');return
    cc=packet2_candidates(m,src)
    sha=packet2_workbook(m,cc)
    m['currentWorkbookSha256']=sha;m['currentEvidenceCheckpoint']=CP2
    m['counts']['informationRows']=399;m['counts']['SOSA_SO2F2_new_candidate_rows']=3;m['counts']['SOSA_SO2F2_records_assessed']=73
    m['workbookSnapshot'].update(checkpoint=CP2,sha256=sha,information_rows=399,
       textInformationRows=399,text_grid_rows=427,saved_xlsx_grid_rows=427,
       color_cell_count=571,mixed_source_cells_uncolored=108,explicit_unassessed_rows=311,
       lag='ZERO: 427×16 saved comparisons; J425:J427 specialized amber fills; all previous content preserved',
       textCheckpoint='SOSA_SO2F2_PSC_OPPORTUNITIES',
       validation_file=LEDGER+'#/SO2_source_opportunity_assessments/SO-2F-2')
    m['nextOwnerAction']='STOP for owner Proceed: SO-2F-3 only (36 remaining frozen source records); no adoption, donor transition or deployment.'
    m['SOSA_SO2F2_opportunity_review']={'status':'SAVED_VERIFIED__REMOTE_PUBLICATION_READBACK_PENDING','manifest':SOURCE,
       'retained_records':73,'added_specialized_rows':[x['row_id'] for x in cc],
       'new_cells':['J425','J426','J427'],'workbook_sha256':sha,'prior_source_holds_preserved':True}
    packet2_text(m);save(MASTER,m);packet2_routes(src,sha);packet2_verify()



# Bounded SO-2F-3: original C239 mezzanine, maintenance, overlay and CoV
BASE3='628545c1fb72ccb80fef43f9ab3d1d7bcfd47f0e'
SHA2='f0b790dbc3b8eb16e8043098f9e7bfafe9836d43e653768b0eb523051cbc69ba'
CP3='SOSA_SO2F3_SAVED_VERIFIED'

def prior3(name):
    return subprocess.check_output(['git','show',BASE3+':'+str((D/name).relative_to(ROOT))],cwd=ROOT)

def check_source3(m,src):
    need(m['currentEvidenceCheckpoint']==CP2 and len(m['rows'])==399 and len(m['review_grid'])==427,'SO2F3 requires prior SO2F2 master')
    need(m['currentWorkbookSha256']==SHA2==digest((D/BOOK).read_bytes()),'unchanged SO2F2 canonical workbook')
    before=json.loads(prior3(MASTER))
    need(m['rows']==before['rows'] and m['review_grid']==before['review_grid'],'earlier source-qualified master unchanged')
    prev=json.loads(prior3(SOURCE))
    need(src['source_manifest']==prev['source_manifest'] and src['SO_2F_1']==prev['SO_2F_1'] and src['SO_2F_2']==prev['SO_2F_2'],'frozen original 581 IDs and preceding packets preserved')
    a=src['SO_2F_3']
    need(a['status']=='SOURCE_ASSESSMENT_RECORDED__CANONICAL_INTEGRATION_NOT_DONE','unintegrated original assessment')
    refs={v[0]:v for v in src['source_manifest']['record_refs'] if v[1]=='SO-2F-3'}
    need(len(refs)==len(a['records'])==36 and set(refs)=={x['id'] for x in a['records']},'exact original 36 source IDs')
    native=load('SOSA_G2_6A_Original_Source_Item_Coverage_10NOV2026.json')['original_source_items']
    outcomes={}
    for r in a['records']:
        id=r['id'];v=refs[id];n=native[int(v[3].split('/')[-1])]
        need(n['id']==id and v[3]==r['source_pointer'] and v[4]==r['source_sha256_retained'],'original ID pointer and retained hash '+id)
        need(n['original_source_locator']==r['locator'] and n['original_pdf_page']==r['pdf_page'] and n['native_kind']==r['source_kind'] and n['normative_standing']==r['standing'],'original normative standing '+id)
        need(bool(r['native_meaning']) and bool(r['closest_existing_rows']) and bool(r['decision_rationale']) and bool(r['source_contact']),'meaning, relationship and contact '+id)
        if r['outcome']=='HELD_EXACT_QUESTION':need(bool(r.get('exact_hold')),'named unresolved original '+id)
        outcomes[r['outcome']]=outcomes.get(r['outcome'],0)+1
    need(outcomes==a['outcomes']=={'ADEQUATELY_REPRESENTED':4,'ADDITION_WARRANTED_PENDING_INTEGRATION':24,'HELD_EXACT_QUESTION':2,'SOURCE_SPECIFIC_NO_NEW_ROW':6},'all 36 dispositions reconcile')
    cs=a['proposed_candidates']
    need(len(cs)==3 and sorted(len(x['evidence_ids']) for x in cs)==[5,6,13],'three source-coherent distinct candidates')
    assigned=[id for c in cs for id in c['evidence_ids']]
    needed={r['id'] for r in a['records'] if r['outcome']=='ADDITION_WARRANTED_PENDING_INTEGRATION'}
    need(set(assigned)==needed and len(set(assigned))==len(assigned)==24,'every supporting source allocated exactly once')
    need([c['classification'] for c in cs]==['COMMON_CANDIDATE','SPECIALIZED_CANDIDATE','COMMON_CANDIDATE'],'two common and one source-specific candidate')
    oldids={x['row_id'] for x in m['rows']}
    need(len({c['row_id'] for c in cs})==3 and all(c['row_id'] not in oldids for c in cs),'new stable row IDs')
    return cs

def new_rows3(m,src,cs):
    for c in cs:
        n=len(m['review_grid'])+1
        vals=['Not linked here — no case evidence established.']*4 + ['Not assessed here — no verified correspondence; not evidence of absence.']*11 + ['OPTIONAL information-need candidate: '+c['label'].removeprefix('Candidate — ')+' — NOT ADOPTED']
        need(len(vals)==16 and all(x.strip() for x in vals),'explicit new case/donor statuses')
        ids=c['evidence_ids'];locs=sorted({r['locator'] for r in src['SO_2F_3']['records'] if r['id'] in ids})
        color='#D9EAF8' if c['classification']=='COMMON_CANDIDATE' else '#F9E6B8'
        vals[9]='['+('COMMON' if c['classification']=='COMMON_CANDIDATE' else 'SPECIALIZED')+' CANDIDATE] PARTIAL / NEW INFORMATION NEED: '+c['definition']+' [C239 Ed1.1 §§13.2.7–13.2.10 PDF225–230; SO-2F-3 original IDs; VITA/figure/CoV holds retained.]'
        mapping={'donor':'The Open Group SOSA C239 Edition 1.1 (2023)','source_ids':ids,'original_source_locators':locs,
          'native_meaning':c['definition'],'closest_prior_rows':c['closest_existing_rows'],
          'reason_for_separate_candidate':c['rationale'],'relation':'RELATED_BUT_DISTINCT_DECLARED_NOT_INSTALLED_OR_CERTIFIED',
          'candidate_status':c['classification'],'classification_rationale':c['rationale'],
          'fill':color,'cell':'J'+str(n),'DIM_Profile_adopted':False,'case_or_runtime_verified':False,
          'pin_level_figure_geometry_verified':False,'native_ANSI_VITA_companions_read':False,
          'vendor_CoV_examined':False,'source_manifest_file':SOURCE}
        m['rows'].append({'row_id':c['row_id'],'label':c['label'],'display_row':n,
          'status':'SO-2F-3 provisional information-need candidate; NOT ADOPTED',
          'definition':c['definition'],'source_entry_ids':ids,'evidence_records':ids,
          'master_inclusion':'PROVISIONAL_NATIVE_SOSA_CANDIDATE','dim_adoption':'NO_CONTENT_ADOPTION_DECISION_IN_THIS_UPDATE',
          'source_review_status':'SO2F3_C239_PDF225_230_READ__FIGURE_OVERVIEW_ONLY__COMPANIONS_AND_INSTALLED_HOLDS',
          'display':vals,'SO2_source_correspondence':mapping})
        m['review_grid'].append(vals)
    need(len(m['rows'])==402 and len(m['review_grid'])==430 and len(m['review_sections'])==26,'402 rows 430 grid and original sections')

def workbook3(m,cs):
    q=pub.q;original=(D/BOOK).read_bytes();edited={}
    summaries={
     'Summary':{'A1':'CURRENT 15 NOV 2026 — SOSA SO-2F-3 complete',
       'B1':'402 rows, SAME 26-sheet workbook. F3 accepted; SOSA bounded PARTIAL; AAS acceptance pending. M00/M01 preserved.',
       'B17':'SO-2F-3: 36 original mezzanine/maintenance/overlay/CoV records. Three unadopted information needs: maintenance-only console, connector overlay and memory-volatility evidence.',
       'B19':'402 information rows; 682 source classifications, 574 colored and 108 held. Two exact source holds do not become color-coded source comparisons.',
       'B21':'C239 PDF225–230 text and native tables read; Figure13.2.9-1 visually inspected at overview. VITA companions, security Appendix C and actual CoV remain unverified.',
       'B22':'No inferred operational CSAPI endpoint, actual slot installation, certified security overlay, complete memory inventory or verified sanitization.',
       'B23':'STOP for owner Proceed: SO-2F-4 only, 72 frozen original source records. No adoption, donor transition or client work.',
       'B28':'6,880 saved grid values; J428/J430 common blue and J429 specialized amber; previous 427 rows, 21 untouched sheets and M00/M01 preserved.'},
     'Validation':{'A1':'CURRENT 15 NOV 2026 — SOSA SO-2F-3 verified',
       'B1':'402 rows in same workbook; source-qualified provisional candidates not DIM/Profile adoption.',
       'B17':'36 source records: 24 supporting 3 candidates; 4 represented, 6 source-specific, 2 held.',
       'B19':'430 × 16 saved grid values; 682 classified, 574 colored and 108 held.',
       'B21':'Original C239 §§13.2.7–13.2.10 PDF225–230; vendor CoV, ANSI/VITA, restricted Appendix C and precise diagram pins held.',
       'B22':'No actual memory wiping, installation, field access or certification verified.',
       'B23':'Separate owner Proceed required for SO-2F-4 only (72 records).',
       'B28':'Prior 427 rows and 21 unaffected original sheets preserved; M00/M01 retained; native Excel clean reopen unverified.'},
     'Legend':{'A1':'CURRENT LEGEND — SOSA SO-2F-3, classification not adoption',
       'B23':'574 colored / 108 held; new blue common J428/J430, new amber specialized J429. All previous 679 classifications preserved.',
       'B24':'402 information rows; 430×16 comparison grid; 26 existing topic dividers preserved.',
       'A28':'Current SO-2F-3 source boundary',
       'B28':'36 original source IDs: 24 support three candidates, 4 represented, 6 source-only and 2 exact holds. STOP before SO-2F-4.'}}
    with zipfile.ZipFile(io.BytesIO(original)) as zin:
        paths=pub.old.sheetpaths(zin);need(len(paths)==26,'same 26 sheets')
        for sheet in ('Master Crosswalk','DIM Register'):
            path=paths[sheet];root=ET.fromstring(zin.read(path));sd=root.find(q('sheetData'))
            oldrows={int(r.get('r')):r for r in sd.findall(q('row'))}
            template=oldrows[427 if sheet=='Master Crosswalk' else 400]
            commonstyle=None;specialstyle=None
            if sheet=='Master Crosswalk':
                commonstyle=next(x.get('s') for x in oldrows[388].findall(q('c')) if x.get('r')=='J388')
                specialstyle=next(x.get('s') for x in oldrows[427].findall(q('c')) if x.get('r')=='J427')
                need(commonstyle!=specialstyle,'prior blue and amber differentiated')
            for j,c in enumerate(cs):
                idx=428+j if sheet=='Master Crosswalk' else 401+j
                new=copy.deepcopy(template);new.set('r',str(idx));new.set('ht','330');new.set('customHeight','1')
                if sheet=='Master Crosswalk':vals=m['review_grid'][427+j];width=16
                else:
                    row=m['rows'][399+j];link=row['SO2_source_correspondence'];ids=', '.join(c['evidence_ids'])
                    vals=[row['row_id'],row['label'],row['definition'],row['status'],row['source_review_status'],
                      row['master_inclusion'],row['dim_adoption'],'Not assessed here','Not assessed here',ids,
                      link['relation']+'; '+link['reason_for_separate_candidate'],
                      'C239 Ed1.1 §§13.2.7–13.2.10 PDF225–230; original VITA/CoV/security/pin-routing holds.',
                      'Not assessed here','Not assessed here',c['classification']+'; '+c['definition'],
                      ids+'; '+SOURCE+'; '+', '.join(link['original_source_locators']),
                      'Not assessed here','Not assessed here — AAS equivalence unassessed.'];width=18
                need(len(vals)==width,'original register width')
                cells={re.match('[A-Z]+',x.get('r')).group():x for x in new.findall(q('c'))}
                for k,v in enumerate(vals):
                    col=letter(k+1);cell=cells.get(col)
                    if cell is None:cell=ET.SubElement(new,q('c'),{'r':col+str(idx)})
                    cell.set('r',col+str(idx));pub.f3_put(cell,str(v))
                    if sheet=='Master Crosswalk' and col=='J':
                        cell.set('s',commonstyle if c['classification']=='COMMON_CANDIDATE' else specialstyle)
                sd.append(new)
            dim=root.find(q('dimension'));need(dim is not None,'dimension')
            dim.set('ref','A1:'+('P430' if sheet=='Master Crosswalk' else 'R403'))
            f=root.find(q('autoFilter'))
            if f is not None:f.set('ref','A2:P430' if sheet=='Master Crosswalk' else 'A1:R403')
            edited[path]=ET.tostring(root,encoding='utf-8',xml_declaration=True)
        for sheet,data in summaries.items():
            root=ET.fromstring(zin.read(paths[sheet]));cells={c.get('r'):c for c in root.iter(q('c'))}
            for addr,val in data.items():
                need(addr in cells,'current '+sheet+' guidance cell '+addr)
                pub.f3_put(cells[addr],val)
            edited[paths[sheet]]=ET.tostring(root,encoding='utf-8',xml_declaration=True)
        out=io.BytesIO()
        with zipfile.ZipFile(out,'w') as zout:
            for info in zin.infolist():zout.writestr(info,edited.get(info.filename,zin.read(info.filename)))
    newbytes=out.getvalue();need(newbytes!=original,'new saved workbook')
    (D/BOOK).write_bytes(newbytes)
    return digest(newbytes)

def mirrors3(m):
    text_mirrors(m)
    banner=('# Current comparison — SOSA SO-2F-3, 15 November 2026\n\n'
       '402 rows, three source-qualified unadopted candidates, all earlier cells/classifications/source holds retained. '
       'See '+SOURCE+' SO_2F_3 and the existing G4 ledger for 36 exact evidence dispositions. '
       'STOP for separate SO-2F-4 owner Proceed.\n\n')
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        p=D/f;txt=p.read_text(encoding='utf-8');i=txt.find('<table>')
        need(i>0,'preserve comparison table')
        p.write_text(banner+txt[i:],encoding='utf-8')

def routes3(src,sha):
    a=src['SO_2F_3'];a['status']='SAVED_VERIFIED__REMOTE_PUBLICATION_READBACK_PENDING'
    a['workbook_sha256']=sha
    a['master_workbook']='402 information rows, 430×16 saved values, J428/J430 common blue and J429 specialized amber, same 26-sheet workbook.'
    a['next']='STOP for separate owner Proceed: SO-2F-4 only, 72 frozen original source records.'
    save(SOURCE,src)
    old=(D/LEDGER).read_text(encoding='utf-8')
    need(old.endswith('  }\n}\n') and '"SO-2F-3"' not in old,'append to existing G4 ledger once')
    record={'status':a['status'],'source_manifest_file':SOURCE,'source_ids':[r['id'] for r in a['records']],
      'outcomes':a['outcomes'],'new_rows':[{'id':c['row_id'],'class':c['classification'],'evidence':len(c['evidence_ids'])} for c in a['proposed_candidates']],
      'source_contact':a['source_contact'],'information_rows':402,'grid_values':6880,
      'new_sosa_cells':['J428','J429','J430'],'workbook_sha256':sha,'holds':a['source_holds'],
      'next':'STOP before SO-2F-4 except separate owner Proceed'}
    out=old[:-6]+',\n    "SO-2F-3": '+json.dumps(record,indent=2,ensure_ascii=False).replace('\n','\n    ')+'\n  }\n}\n'
    need(len(json.loads(out)['SO2_source_opportunity_assessments'])==8,'seven prior packets plus third subpacket')
    (D/LEDGER).write_text(out,encoding='utf-8')
    p=(D/PITON).read_text(encoding='utf-8')
    p=p.replace('SO-2F-2 integrated checkpoint.','SO-2F-3 integrated checkpoint.')
    def section(head,end,body):
        nonlocal_p=None
        return head+body
    st=p.index('## Interrupted work');en=p.index('\n\n## Active scope and evidence',st)
    p=p[:st]+('## Interrupted work\n\nSO-2E through SO-2F-2 published and remotely verified. '
       'SO-2F-3 assessed 36 original C239 records and integrated three source-qualified, unadopted candidates '
       'in the same master/workbook. Saved-file verification passed; remote readback pending.')+p[en:]
    st=p.index('**SO-2F source checkpoint:**');en=p.index('\n\n## Master and workbook',st)
    p=p[:st]+('**SO-2F source checkpoint:** The frozen 581-ID manifest and SO-2F-1/2 dispositions remain in '+SOURCE+'. '
       'SO-2F-3 covers 36 original C239 §§13.2.7–13.2.10 records, PDF225–230: 24 support three '
       'maintenance-console, pin-overlay and memory-documentation candidates; four represented, six source-only, '
       'two held. Figure13.2.9-1 overview visually inspected, not its full pin routing. CoV may omit undocumented '
       'embedded nonvolatile memories; actual CoV/device, original VITA companions and restricted Appendix C '
       'remain unverified. SO-2F has 414 IDs left; next SO-2F-4 only (72).')+p[en:]
    p=p.replace('**399 information rows**, **427×16 = 6,832 values**, **679 source classifications: 571 colored/108 held**',
      '**402 information rows**, **430×16 = 6,880 values**, **682 source classifications: 574 colored/108 held**')
    p=p.replace('311 remaining rows have explicit unassessed/case-held standing.',
      '314 remaining rows have explicit unassessed/case-held standing.')
    p=p.replace('New SO-2F-2 amber SOSA cells J425:J427; prior J422:J424 and J413:J421 preserved;',
      'New SO-2F-3 common blue J428/J430 and specialized amber J429; prior J425:J427, J422:J424, J413:J421 preserved;')
    p=p.replace('Current workbook SHA-256 '+chr(96)+SHA2+chr(96)+'; prior SO-2F-1 SHA-256',
      'Current workbook SHA-256 '+chr(96)+sha+chr(96)+'; prior SO-2F-2 SHA-256 '+chr(96)+SHA2+chr(96)+'; earlier SO-2F-1 SHA-256')
    st=p.index('## Verification and publication');en=p.index('\n\n## Next action and stop',st)
    p=p[:st]+('## Verification and publication\n\nSO-2F-3 publisher checked 6,880 saved values, '
      'new common/specialized fills, prior 427 comparison rows, 21 untouched sheets and exact frozen ID/pointer '
      'membership. Earlier publisher/readback passed; remote SO-2F-3 readback pending. Original M00/M01 '
      'preserved; native Microsoft Excel clean reopening unverified. Five broader artifact/link errors '
      'remain unresolved in the partial checkout; no blanket repository success claim.')+p[en:]
    st=p.index('## Next action and stop');en=p.index('\n\n## History',st)
    p=p[:st]+('## Next action and stop\n\nSO-2F-3 source assessment and same-master/workbook integration '
      'saved and verified; **remote publication/readback pending**. STOP for Proceed. '
      '**Next owner Proceed authorizes SO-2F-4 only: 72 frozen source records.** '
      'No adoption, donor transition, client work or deployment.')+p[en:]
    need(len(p.split())<=1000 and 'SO-2F-4 only' in p,'recovery PITON budget and stop gate')
    (D/PITON).write_text(p,encoding='utf-8')

def verify3():
    m=load(MASTER);src=load(SOURCE);a=src['SO_2F_3']
    need(m['currentEvidenceCheckpoint']==CP3 and len(m['rows'])==402 and len(m['review_grid'])==430,'402 row/430 grid checkpoint')
    need(m['workbookSnapshot']['color_cell_count']==574 and m['workbookSnapshot']['mixed_source_cells_uncolored']==108,'same classification contract')
    old=json.loads(prior3(MASTER))
    need(m['rows'][:399]==old['rows'] and m['review_grid'][:427]==old['review_grid'],'prior 399 info rows and 427 grid rows unchanged')
    oldsrc=json.loads(prior3(SOURCE))
    need(src['source_manifest']==oldsrc['source_manifest'] and src['SO_2F_1']==oldsrc['SO_2F_1'] and src['SO_2F_2']==oldsrc['SO_2F_2'],'original 581 refs and previous source packets preserved')
    need(len(a['records'])==36 and sum(a['outcomes'].values())==36,'all 36 source records accounted')
    for j,c in enumerate(a['proposed_candidates']):
        row=m['rows'][399+j]
        need(row['row_id']==c['row_id'] and row['source_entry_ids']==c['evidence_ids'] and row['display']==m['review_grid'][427+j],'source-to-row/crosswalk link')
        need(all(bool(v.strip()) for v in row['display']),'new row has all 16 explicit values')
    sha=digest((D/BOOK).read_bytes())
    need(sha==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==a['workbook_sha256'],'published xlsx SHA256 equality')
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/f).open(encoding='utf-8',newline='') as h:need(list(csv.reader(h))==m['review_grid'],'complete mirror '+f)
    need((D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_bytes()==(D/'ISA_Correction_Review_07NOV2026.md').read_bytes(),'readable mirrors identical')
    with zipfile.ZipFile(io.BytesIO(prior3(BOOK))) as oldz,zipfile.ZipFile(D/BOOK) as z:
        need(z.testzip() is None and oldz.namelist()==z.namelist(),'original OOXML parts preserved')
        oldp=pub.old.sheetpaths(oldz);pp=pub.old.sheetpaths(z)
        need(len(pp)==len(oldp)==26 and pp==oldp,'same 26 original worksheets')
        affected={pp[x] for x in ('Master Crosswalk','DIM Register','Summary','Validation','Legend')}
        need(all(z.read(x)==oldz.read(x) for x in oldz.namelist() if x not in affected),'21 unaffected sheets and OOXML parts unchanged')
        q=pub.q
        root=ET.fromstring(z.read(pp['Master Crosswalk']))
        rows={int(v.get('r')):v for v in root.find(q('sheetData')).findall(q('row'))}
        for i,vv in enumerate(m['review_grid'],1):
            cc={x.get('r'):x for x in rows[i].findall(q('c'))}
            for j,v in enumerate(vv,1):
                key=letter(j)+str(i)
                if key in cc:need(pub.f3_cell_text(cc[key])==v,'saved XLSX comparison '+key)
                else:need(v=='','no missing nonempty cell '+key)
        def st(i):return next(x.get('s') for x in rows[i] if x.get('r')=='J'+str(i))
        need(st(428)==st(388) and st(429)==st(427) and st(430)==st(388),'two blue common and one amber specialized')
        root=ET.fromstring(z.read(pp['DIM Register']))
        rr={int(v.get('r')):v for v in root.find(q('sheetData')).findall(q('row'))}
        for j,c in enumerate(a['proposed_candidates']):
            n=401+j
            need(next(pub.f3_cell_text(x) for x in rr[n] if x.get('r')=='A'+str(n))==c['row_id'],'new register row '+str(n))
        for name in ('Summary','Validation','Legend'):
            root=ET.fromstring(z.read(pp[name]))
            need(any('SO-2F-3' in pub.f3_cell_text(x) for x in root.iter(q('c'))),'current '+name+' sheet')
    l=load(LEDGER)
    need(len(l['SO2_source_opportunity_assessments'])==8 and l['SO2_source_opportunity_assessments']['SO-2F-3']['workbook_sha256']==sha,'G4 source ledger linked')
    # Accept either historical SO-2F-4 routing or the owner-approved finite closeout.
    stop=(D/PITON).read_text().split('## Next action and stop',1)[-1].split('## History',1)[0]
    need(('SO-2F-4 only' in stop) or ('SO-2F-R' in stop and '414' in stop and 'STOP' in stop), 'explicit owner Proceed stop; old six-packet schedule is superseded')
    print('PASS SO-2F-3: 36 IDs, 24 source supports/4 represented/6 source-only/2 held; 402 rows, 430x16 values; J428/J430 blue, J429 amber; all prior 427 rows, 21 sheets and M00/M01 preserved.')
    print('LIMIT: original VITA companions, security Appendix C, actual CoV, full overlay pin routing, native Excel clean reopen and model adoption unverified.')

def apply3():
    m=load(MASTER);src=load(SOURCE)
    if m['currentEvidenceCheckpoint']==CP3:verify3();return
    cs=check_source3(m,src);new_rows3(m,src,cs)
    sha=workbook3(m,cs)
    m['currentWorkbookSha256']=sha;m['currentEvidenceCheckpoint']=CP3
    m['counts']['informationRows']=402;m['counts']['SOSA_SO2F3_new_candidate_rows']=3;m['counts']['SOSA_SO2F3_records_assessed']=36
    m['workbookSnapshot'].update(checkpoint=CP3,sha256=sha,information_rows=402,
      textInformationRows=402,text_grid_rows=430,saved_xlsx_grid_rows=430,
      color_cell_count=574,mixed_source_cells_uncolored=108,explicit_unassessed_rows=314,
      lag='ZERO: 430x16 saved values; J428/J430 blue and J429 amber; all earlier data preserved',
      textCheckpoint='SOSA_SO2F3_HARDWARE_MAINTENANCE_OVERLAY_MEMORY',
      validation_file=LEDGER+'#/SO2_source_opportunity_assessments/SO-2F-3')
    m['nextOwnerAction']='STOP for separate owner Proceed: SO-2F-4 only (72 frozen records); no adoption, donor transition, client work or deployment.'
    m['SOSA_SO2F3_opportunity_review']={'status':'SAVED_VERIFIED__REMOTE_PUBLICATION_READBACK_PENDING',
      'manifest':SOURCE,'retained_records':36,'added_candidate_rows':[c['row_id'] for c in cs],
      'new_cells':['J428','J429','J430'],'workbook_sha256':sha,'prior_holds_preserved':True}
    mirrors3(m);save(MASTER,m);routes3(src,sha);verify3()



# Consolidated SO-2F-R: one owner-authorized closeout, no six packet gates.
BASER='b207d95a3d83d88f62d52fc6480e599d051f8638'
SHAR0='687df7c71757641b937ba2671238138510691f8e2432e793f90eec41580efd0e'
CPR='SOSA_SO2FR_SAVED_VERIFIED'
NARRATIVE='Donor_Native_High_Level_Information_Groupings_Comparison.md'
KEY_R='SO-2F-R'

def priorR(name):
    return subprocess.check_output(['git','show',BASER+':'+str((D/name).relative_to(ROOT))],cwd=ROOT)

def source_preflightR(m,src):
    need(m['currentEvidenceCheckpoint']==CP3 and len(m['rows'])==402 and len(m['review_grid'])==430,'R frozen master 402/430')
    need(m['currentWorkbookSha256']==SHAR0==digest((D/BOOK).read_bytes()),'R unchanged verified SO2F3 XLSX')
    before=json.loads(priorR(MASTER))
    need(m['rows']==before['rows'] and m['review_grid']==before['review_grid'],'R prior 402 info rows and 430 grid rows')
    original=json.loads(priorR(SOURCE))
    need(src['source_manifest']==original['source_manifest'],'R original 581-ID manifest unchanged')
    for k in ('SO_2F_1','SO_2F_2','SO_2F_3'):
        need(src[k]==original[k],'R earlier published original outcomes unmodified '+k)
    a=src['SO_2F_R']
    need(a['status']=='SOURCE_ASSESSMENT_RECORDED__CANONICAL_INTEGRATION_NOT_DONE','R source research must be staged')
    need(a['prior_assessed']==167 and a['current_assessed']==414 and a['total_accounted']==581,'R exact overall accounting')
    need(a['group_counts']=={'PICP_PROFILE_AND_LEGACY':149,'AMPS_PROTOCOL_PROFILE_GRAMMAR':265},'R two meaning families')
    refs=src['source_manifest']['record_refs']
    selected={x[0]:x for x in refs if x[1] in ('SO-2F-4','SO-2F-5','SO-2F-6','SO-2F-7','SO-2F-8','SO-2F-9')}
    need(len(refs)==581 and len(selected)==414 and len(a['records'])==414 and set(selected)=={x['id'] for x in a['records']},'R all 414 unique frozen IDs')
    previousids={x[0] for x in refs if x[1] in ('SO-2F-1','SO-2F-2','SO-2F-3')}
    need(len(previousids)==167 and not (set(selected)&previousids),'R exact no-overlap prior/remaining')
    source_cache={}
    tally={}
    validrows={x['row_id'] for x in m['rows']}|{x['row_id'] for x in a['candidates']}
    for row in a['records']:
        id=row['id'];r=selected[id]
        need(r[1]==row['retained_prior_packet'] and r[2]==row['original_source_file'] and r[3]==row['original_json_pointer'] and r[4]==row['frozen_sha256'],'R original source record/ID/pointer/hash '+id)
        if r[2] not in source_cache:
            source_cache[r[2]]=load(r[2])['original_source_items']
        raw=source_cache[r[2]][int(r[3].split('/')[-1])]
        loc=raw.get('original_source_locator') or raw.get('source_locator') or 'ORIGINAL_PDF_PAGE_'+str(raw['original_pdf_page'])+'__SOURCE_ITEM_POINTER_ONLY'
        need(raw['id']==id and raw['native_kind']==row['native_kind'] and raw['normative_standing']==row['normative_standing'] and raw['original_pdf_page']==row['original_pdf_page'] and row['locator']==loc,'R native kind, source, location and normative standing '+id)
        need(bool(row['retained_original_contact']) and bool(row['native_meaning']) and bool(row['decision_rationale']) and bool(row['relation']) and all(t in validrows for t in row['closest_existing_rows']),'R documented qualified source outcome '+id)
        if row['outcome']=='HELD_EXACT_QUESTION':
            need(bool(row.get('exact_hold')),'R explicit original hold '+id)
        tally[row['outcome']]=tally.get(row['outcome'],0)+1
    need(tally==a['outcomes']=={'SOURCE_SPECIFIC_NO_NEW_ROW':83,'ADDITION_WARRANTED_PENDING_INTEGRATION':250,'HELD_EXACT_QUESTION':46,'ADEQUATELY_REPRESENTED':35},'R four evidenced outcomes reconcile')
    cs=a['candidates']
    need(len(cs)==2 and [x['row_id'] for x in cs]==['SOSA-SO2FR-HARDWARE-PROFILE','SOSA-SO2FR-PORT-PROTOCOL-ALLOCATION'],'R only two distinct new information needs')
    need(all(x['classification']=='SPECIALIZED_CANDIDATE' for x in cs),'R source-specific hardware specialized classification')
    addition={x['id'] for x in a['records'] if x['outcome']=='ADDITION_WARRANTED_PENDING_INTEGRATION'}
    allocated=[id for c in cs for id in c['evidence_ids']]
    need(set(allocated)==addition and len(allocated)==len(set(allocated))==250,'R each supporting source ID accounted exactly once')
    need(all(c['row_id'] not in {x['row_id'] for x in m['rows']} for c in cs),'R new stable IDs')
    return cs

def add_rowsR(m,src,cs):
    for candidate in cs:
        grididx=len(m['review_grid'])+1
        vals=['Not linked here — no case evidence established.']*4+['Not assessed here — no verified correspondence; not evidence of absence.']*11+['OPTIONAL information-need candidate: '+candidate['label'].removeprefix('Candidate — ')+' — NOT ADOPTED']
        need(len(vals)==16 and all(x.strip() for x in vals),'R explicit 16-cell design')
        vals[9]='[SPECIALIZED CANDIDATE] PARTIAL / NEW INFORMATION NEED: '+candidate['definition']+' [The Open Group SOSA C239 Ed1.1 §§13.2.11–13.3.5 PDF230–264, SO-2F-R, frozen original IDs; diagram/matrix and external ANSI/VITA evidence held.]'
        group=next(x['meaning_group'] for x in src['SO_2F_R']['records'] if x['id']==candidate['evidence_ids'][0])
        locs=sorted({x['locator'] for x in src['SO_2F_R']['records'] if x['id'] in candidate['evidence_ids']})
        mapping={'donor':'The Open Group SOSA C239 Edition 1.1 (2023)',
          'source_ids':candidate['evidence_ids'],'original_source_locators':locs,
          'native_meaning':candidate['definition'],'closest_prior_rows':candidate['closest_existing_rows'],
          'reason_for_separate_candidate':candidate['rationale'],
          'relation':'RELATED_BUT_DISTINCT_PUBLISHED_HARDWARE_PROFILE_OR_PORT_PROTOCOL_DESIGN_NOT_INSTALLED_OR_OBSERVED',
          'candidate_status':'SPECIALIZED_CANDIDATE',
          'classification_rationale':'Hardware card/slot/port design declaration, not cross-vendor required model information, live telemetry or API schema.',
          'fill':'#F9E6B8','cell':'J'+str(grididx),
          'DIM_Profile_adopted':False,'case_or_runtime_verified':False,'future_only':False,
          'original_ANSI_VITA_companions_read':False,'complete_matrix_pixel_geometry_verified':False,
          'source_manifest_file':SOURCE,'original_meaning_group':group}
        m['rows'].append({'row_id':candidate['row_id'],'label':candidate['label'],'display_row':grididx,
          'status':'SO-2F-R provisional specialized information-need candidate; NOT ADOPTED',
          'definition':candidate['definition'],'source_entry_ids':candidate['evidence_ids'],
          'evidence_records':candidate['evidence_ids'],
          'master_inclusion':'PROVISIONAL_NATIVE_SOSA_CANDIDATE',
          'dim_adoption':'NO_CONTENT_ADOPTION_DECISION_IN_THIS_UPDATE',
          'source_review_status':'SO2FR_C239_2023_RETAINED_NATIVE_TEXT_RECHECKED__MATRIX_AND_COMPANIONS_HELD',
          'display':vals,'SO2_source_correspondence':mapping})
        m['review_grid'].append(vals)
    need(len(m['rows'])==404 and len(m['review_grid'])==432 and len(m['review_sections'])==26,'R 404 rows, 432 grid rows and old dividers')

def workbookR(m,cs):
    q=pub.q
    previous=(D/BOOK).read_bytes()
    edited={}
    summaries={
     'Summary':{
      'A1':'CURRENT — SOSA SO-2F-R consolidated closeout, owner disposition pending',
      'B1':'404 information rows; same editable 26-sheet workbook, 11 source-qualified unadopted SO-2F candidates total. F3 accepted; SOSA bounded PARTIAL; AAS acceptance pending; M00/M01 preserved.',
      'B17':'SO-2F-R: 414 original IDs reconciled in two subject families, 149 PIC profiles/legacy and 265 AMPS. Added two specialized candidates for declared hardware profile identity and source-mapped hardware port/protocol assignments.',
      'B19':'404 information rows; 684 classified comparison cells: 576 colored and 108 held. 581 SO-2F original IDs individually accounted; 60 original-source held dispositions separate from classification holds.',
      'B21':'C239 Ed1.1 original PDF230–264 text/tables reviewed/reused; matrix pixel geometry and original ANSI/VITA companions unresolved. No installed hardware or client runtime proof.',
      'B22':'Two source-scoped optional design needs, not 414 new DIM requirements. Legacy standing and depth/cooling profiles reuse existing candidate rows.',
      'B23':'STOP for owner disposition: accept or request specific corrections to bounded-PARTIAL SO-2F-R closeout. No SO-2G, donor transition, model adoption or client development.',
      'B28':'6,912 saved grid values; two amber SOSA cells J431:J432; all 430 earlier grid rows, 21 unaffected worksheets and manual M00/M01 preserved.'},
     'Validation':{
      'A1':'CURRENT — SOSA SO-2F-R consolidated source/workbook verification',
      'B1':'404 rows, same 26-sheet source master. No content adoption.',
      'B17':'Original source outcomes 581 total = 375 support new candidate rows; 46 represented; 100 source-specific/no row; 60 held (SO-2F-1/2/3 + SO-2F-R).',
      'B19':'432×16 saved grid cells, 684 classified / 576 colored / 108 held. All preceding 430 grid rows preserved.',
      'B21':'2023 C239 original PDF230–264 source text; exact hardware matrices, unread external VITA and installed/case evidence held.',
      'B22':'11 SO-2F candidates across all four phases, none an adopted DIM/Profile SHALL.',
      'B23':'STOP for owner bounded-PARTIAL acceptance/disposition; no more source-count Proceed packets.',
      'B28':'21 untouched sheets, full saved grid parity, originals M00/M01; Microsoft Excel native reopen unverified.'},
     'Legend':{
      'A1':'CURRENT LEGEND — SOSA SO-2F-R; source classification not model adoption',
      'B23':'576 colored / 108 held source classifications. Added J431/J432 specialized amber. All 682 previous classifications intact.',
      'B24':'404 information rows; 432×16 complete comparison values; 26 original topic divider rows preserved.',
      'A28':'Finite SO-2F source-opportunity closeout',
      'B28':'581 frozen original records accounted: 167 previous and 414 consolidated. Two new specialized candidates; 60 exact original-source held dispositions retained. Owner disposition is next.'}}
    with zipfile.ZipFile(io.BytesIO(previous)) as z:
        paths=pub.old.sheetpaths(z);need(len(paths)==26,'R original 26 sheets')
        for name in ('Master Crosswalk','DIM Register'):
            path=paths[name];xml=ET.fromstring(z.read(path));sd=xml.find(q('sheetData'))
            rowmap={int(x.get('r')):x for x in sd.findall(q('row'))}
            template=rowmap[430 if name=='Master Crosswalk' else 403]
            specialstyle=None
            if name=='Master Crosswalk':
                specialstyle=next(x.get('s') for x in rowmap[429] if x.get('r')=='J429')
                need(bool(specialstyle),'R amber source style exists')
            for j,c in enumerate(cs):
                idx=431+j if name=='Master Crosswalk' else 404+j
                newrow=copy.deepcopy(template);newrow.set('r',str(idx));newrow.set('ht','330');newrow.set('customHeight','1')
                if name=='Master Crosswalk':vals=m['review_grid'][430+j];width=16
                else:
                    item=m['rows'][402+j];link=item['SO2_source_correspondence'];ids=', '.join(c['evidence_ids'])
                    vals=[item['row_id'],item['label'],item['definition'],item['status'],item['source_review_status'],
                      item['master_inclusion'],item['dim_adoption'],'Not assessed here','Not assessed here',ids,
                      link['relation']+'; '+link['reason_for_separate_candidate'],
                      'C239 Ed1.1 §§13.2.11–13.3.5 PDF230–264. VITA/figure/matrix original holds.',
                      'Not assessed here','Not assessed here','SPECIALIZED_CANDIDATE; '+c['definition'],
                      ids+'; '+SOURCE+'; '+', '.join(link['original_source_locators']),
                      'Not assessed here','Not assessed here — AAS equivalence unassessed.'];width=18
                need(len(vals)==width,'R original sheet width')
                cells={re.match('[A-Z]+',x.get('r')).group():x for x in newrow.findall(q('c'))}
                for colno,v in enumerate(vals):
                    a=letter(colno+1);cell=cells.get(a)
                    if cell is None:cell=ET.SubElement(newrow,q('c'),{'r':a+str(idx)})
                    cell.set('r',a+str(idx));pub.f3_put(cell,str(v))
                    if name=='Master Crosswalk' and a=='J':cell.set('s',specialstyle)
                sd.append(newrow)
            dim=xml.find(q('dimension'));need(dim is not None,'R original worksheet dimensions')
            dim.set('ref','A1:'+('P432' if name=='Master Crosswalk' else 'R405'))
            af=xml.find(q('autoFilter'))
            if af is not None:af.set('ref','A2:P432' if name=='Master Crosswalk' else 'A1:R405')
            edited[path]=ET.tostring(xml,encoding='utf-8',xml_declaration=True)
        for name,vals in summaries.items():
            xml=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in xml.iter(q('c'))}
            for address,value in vals.items():
                need(address in cells,'R existing guidance '+name+'!'+address)
                pub.f3_put(cells[address],value)
            edited[paths[name]]=ET.tostring(xml,encoding='utf-8',xml_declaration=True)
        target=io.BytesIO()
        with zipfile.ZipFile(target,'w') as out:
            for info in z.infolist():out.writestr(info,edited.get(info.filename,z.read(info.filename)))
    new=target.getvalue();need(new!=previous,'R updated OOXML')
    (D/BOOK).write_bytes(new)
    return digest(new)

def mirrorsR(m):
    text_mirrors(m)
    banner=('# Current comparison — SOSA SO-2F-R consolidated opportunity closeout\n\n'
      '404 rows, two new source-qualified specialized hardware/interface candidates, no model/Profile adoption. '
      'All previously published 402 rows and 682 classifications retained. '
      '581 frozen original IDs have evidenced dispositions in '+SOURCE+' under SO_2F_R, '
      'with G4 ledger routing and original held-source boundaries. STOP for owner disposition.\n\n')
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        p=D/f;old=p.read_text(encoding='utf-8');offset=old.find('<table>')
        need(offset>0,'R readable original table retained')
        p.write_text(banner+old[offset:],encoding='utf-8')

def narrativeR():
    p=D/NARRATIVE;original=p.read_text(encoding='utf-8')
    title='# SO-2F-R COMPLETE — Finite SOSA source-opportunity closeout (15 November 2026)'
    need(title not in original,'R do not duplicate narrative')
    body=(title+'\n\n'
      '## What was checked and why\n\n'
      'The original master began heavily populated from Integrated Sensor Architecture (ISA). This bounded corrective assessment asked whether already-reviewed '
      'The Open Group Sensor Open Systems Architecture (SOSA) C239 Edition 1.1 material included additional, genuinely different information needs. '
      'The complete frozen SO-2F inventory holds 581 distinct source IDs. The first 167 were assessed and published through SO-2F-1/2/3; '
      'this step accounted for all remaining 414 by two *meaning families*, not six more batches. Original C239 PDF230–264 and seven existing source ledgers are the evidence basis; '
      'details and exact source-ID/pointer dispositions remain in [the 581-ID manifest]('+SOURCE+').\n\n'
      '## What was learned — no 414 new data fields\n\n'
      'The first 149 remaining records describe 3U/6U plug-in cards, applicable physical slot/module profiles and variants, source-specific rules and legacy-profile status. '
      'These warrant **one specialized candidate** for the named, source-qualified hardware profile and its conditional dash/connector choice. '
      'Existing physical-component, mechanical/cooling, slot-identity and conformance rows do not preserve the source-declared *base profile identifier*. '
      'But the earlier ISA extension/standardization-standing row already captures the SOSA Legacy idea, so no new general legacy/status row is justified.\n\n'
      'The next 265 records describe Alternate Module Profile Scheme (AMPS) grammar, Alternate Naming Structure, port and lane protocol assignments, allowed alternatives and example strings. '
      'These warrant **one specialized candidate** for hardware-interface *protocol allocation and encoded profile declaration*. '
      'This is not the same as a network/API representation schema, a measured Ethernet throughput, actual installed wiring or a configured service. '
      'Individual protocol codes, depth/cooling/pitch examples and populated rows in original matrices are *values and supporting evidence*, not independent universal DIM requirements.\n\n'
      '## Source accounting and results\n\n'
      '| Outcome | Earlier SO-2F-1/2/3 | This SO-2F-R | Total frozen IDs |\n'
      '| --- | ---: | ---: | ---: |\n'
      '| Warranted additions, grouped as candidate support | 125 | 250 | **375** |\n'
      '| Adequately represented | 11 | 35 | **46** |\n'
      '| Source-specific / no separate information row | 17 | 83 | **100** |\n'
      '| Held for exact original-source question | 14 | 46 | **60** |\n'
      '| **Total** | **167** | **414** | **581** |\n\n'
      'The full SO-2F sequence added **11 unadopted candidate rows** (9 earlier plus 2 here). '
      'Counts reflect original records, *not* the number of distinct requirements or new data attributes. '
      'Two candidates in this closeout are specialized, with no automatic equivalence to other standards or vendor equipment.\n\n'
      '## Important limits and recommendation\n\n'
      'Some original C239 figures and dense port/protocol matrices were reviewed at text, table-label or selected image depth only. '
      'Original ANSI/VITA companions, exact legal port matrices and several publisher discrepancies remain held; source examples are not device certifications. '
      'No field-installed hardware, true port state, vendor conformance results, model/Profile adoption or runtime interoperability was verified.\n\n'
      '**Recommend owner acceptance as bounded-PARTIAL closure of the defined SOSA opportunity check.** '
      'Do not restart another indefinite source-by-source audit merely to remove these documented holds. '
      'Preserve their original locators for later precise questions, and separately authorize model/Profile synthesis when the owner chooses; '
      'no automatic donor transition, device implementation or deployment follows from this closeout.\n\n'
      '## Files and owner boundary\n\n'
      '[Canonical master](Master_Donor_Concept_to_DIM_Crosswalk.json), [same editable Excel](Master_Donor_Concept_to_DIM_Crosswalk.xlsx), '
      '[source evidence and 581-ID accountability]('+SOURCE+'), and [current PITON]('+PITON+'). '
      'All 26 sheets, M00/M01, other donor/case columns, source holds, and prior 402 information rows are retained. '
      '**STOP for owner disposition**; no automatic SO-2G or additional Proceed packets.\n\n---\n\n')
    p.write_text(body+original,encoding='utf-8')

def routesR(src,sha):
    a=src['SO_2F_R'];a['status']='SAVED_VERIFIED__REMOTE_PUBLICATION_READBACK_PENDING'
    a['workbook_sha256']=sha
    a['master_workbook']='404 information rows, 432×16 saved values, two new specialized amber J431:J432 cells, 26 original sheets, 21 unaffected parts.'
    a['next']='STOP for owner bounded-PARTIAL opportunity disposition; no more source-count Proceed packets.'
    save(SOURCE,src)
    old=(D/LEDGER).read_text(encoding='utf-8')
    need(old.endswith('  }\n}\n') and '"SO-2F-R"' not in old,'R append once to existing G4 ledger')
    record={'status':a['status'],'source_manifest_file':SOURCE,
      'source_ids':[r['id'] for r in a['records']],
      'group_counts':a['group_counts'],'outcomes':a['outcomes'],
      'source_qualified_rows':[{'row_id':v['row_id'],'supporting_source_ids':len(v['evidence_ids']),'classification':v['classification']} for v in a['candidates']],
      'frozen_total':581,'previously_assessed':167,'newly_accounted':414,
      'workbook_sha256':sha,'new_cells':['J431','J432'],
      'holds':a['source_holds'],'next':'STOP for owner disposition; no SO-2F-4/5/6/7/8/9 Proceed gate or SO-2G'}
    txt=old[:-6]+',\n    "SO-2F-R": '+json.dumps(record,indent=2,ensure_ascii=False).replace('\n','\n    ')+'\n  }\n}\n'
    parsed=json.loads(txt)
    need(len(parsed['SO2_source_opportunity_assessments'])==9,'R all prior eight opportunity entries retained')
    (D/LEDGER).write_text(txt,encoding='utf-8')
    p=(D/PITON).read_text(encoding='utf-8')
    p=p.replace('**No interrupted research or workbook delivery remains from SO-2F-3.** The current owner request corrects the execution method only. It does **not** authorize starting remaining SOSA research, changing candidate classifications, or modifying master/workbook cells in this turn.',
      '**SO-2F-R source assessment and two warranted master/workbook candidate rows are saved and locally verified.** No interrupted local research remains; remote publication/readback pending. This bounded step is owner-authorized.')
    st=p.index('## Active scope and evidence');en=p.index('\n\n## Master and workbook',st)
    p=p[:st]+('## Active scope and evidence\n\n'
      '[Approved finite source plan](PLAN_SOSA_Source_Coverage_Correction_v0.1_09NOV2026.md) governs, not old SO-2F-4…9 Proceed gates. '
      'The existing '+SOURCE+' retains 581 frozen original IDs and SO-2F-1/2/3 results. '
      'The new SO_2F_R section accounts for all 414 remaining IDs from seven source files, '
      '149 3U/6U physical profiles/legacy plus 265 AMPS grammar/protocol mapping. Outcomes: '
      '**250 support two specialized candidate meanings, 35 represented, 83 source-specific/no new row, 46 held**. '
      'Complete total: **375 supporting, 46 represented, 100 source-only, 60 source-held = 581**. '
      'Original C239 PDF230–264 text and retained source contact used; precise matrix pixels and original ANSI/VITA remain held. '
      'The [same native grouping document]('+NARRATIVE+') contains the plain-English result and owner recommendation.')+p[en:]
    p=p.replace('**402 information rows**, **430 × 16 = 6,880 comparison values, 682 classified cells (574 colored / 108 held)**',
      '**404 information rows**, **432 × 16 = 6,912 comparison values, 684 classified cells (576 colored / 108 held)**')
    p=p.replace('402 information rows, 430 × 16 = 6,880 comparison values, 682 classified cells (574 colored / 108 held)',
      '404 information rows, 432 × 16 = 6,912 comparison values, 684 classified cells (576 colored / 108 held)')
    p=p.replace('Current workbook SHA-256 '+chr(96)+SHAR0+chr(96)+'.',
      'Current workbook SHA-256 '+chr(96)+sha+chr(96)+'; earlier SO-2F-3 SHA-256 '+chr(96)+SHAR0+chr(96)+'.')
    p=p.replace('Latest SO-2F-3 cells J428/J430 common blue and J429 specialized amber; prior rows/holds preserved.',
      'New J431:J432 specialized amber; preceding J428/J430 common blue and J429 amber unchanged. Prior rows/holds preserved.')
    st=p.index('## Verification and publication');en=p.index('\n\n## Next action and stop',st)
    p=p[:st]+('## Verification and publication\n\n'
      'SO-2F-R publisher verified 581-ID reconciliation and 6,912 saved grid values, two specialized amber cells, '
      'all previous 430 grid rows, 21 unchanged sheets, 26-sheet ZIP inventory, M00/M01 and mirror parity. '
      'GitHub publisher and branch readback pending. Native Microsoft Excel reopening unverified. '
      'Five unrelated broader artifact/link errors remain pre-existing; no blanket repo success.')+p[en:]
    st=p.index('## Next action and stop');en=p.index('\n\n## History',st)
    p=p[:st]+('## Next action and stop\n\n'
      '**SO-2F-R 581-ID opportunity accounting and same-workbook integration saved/verified; remote publication pending.** '
      '**STOP for owner disposition.** Recommend owner accept as **bounded PARTIAL** with explicit originals/figure/VITA/case holds. '
      'No automatic SO-2G, further source-count Proceed loop, model/Profile adoption, donor transition, client work or deployment.')+p[en:]
    need(len(p.split())<=1000 and '581-ID opportunity accounting' in p and 'STOP for owner disposition' in p,'R PITON compact stop and status')
    (D/PITON).write_text(p,encoding='utf-8')

def verifyR():
    m=load(MASTER);src=load(SOURCE);a=src['SO_2F_R']
    need(m['currentEvidenceCheckpoint']==CPR and len(m['rows'])==404 and len(m['review_grid'])==432,'R final 404/432 grid')
    need(m['workbookSnapshot']['color_cell_count']==576 and m['workbookSnapshot']['mixed_source_cells_uncolored']==108,'R 684 source color/held statuses')
    base=json.loads(priorR(MASTER))
    need(m['rows'][:402]==base['rows'] and m['review_grid'][:430]==base['review_grid'],'R all prior 402 rows and 430 grid records byte-equivalent JSON')
    baseline=json.loads(priorR(SOURCE))
    need(src['source_manifest']==baseline['source_manifest'] and all(src[k]==baseline[k] for k in ('SO_2F_1','SO_2F_2','SO_2F_3')),'R 581 original frozen and first 167 unchanged')
    need(len(a['records'])==414 and a['total_accounted']==581 and sum(a['outcomes'].values())==414,'R source record outcomes complete')
    for j,c in enumerate(a['candidates']):
        r=m['rows'][402+j];idx=431+j
        need(r['row_id']==c['row_id'] and r['source_entry_ids']==c['evidence_ids'] and r['SO2_source_correspondence']['cell']=='J'+str(idx),'R 2 IDs source-qualified and correctly placed')
        need(r['display']==m['review_grid'][430+j] and len(r['display'])==16 and all(bool(x.strip()) for x in r['display']),'R explicit completed row cells')
    sha=digest((D/BOOK).read_bytes())
    need(sha==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==a['workbook_sha256'],'R workbook source/master hash parity')
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/f).open(encoding='utf-8',newline='') as inp:need(list(csv.reader(inp))==m['review_grid'],'R complete saved CSV '+f)
    need((D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_bytes()==(D/'ISA_Correction_Review_07NOV2026.md').read_bytes(),'R readable mirror full parity')
    with zipfile.ZipFile(io.BytesIO(priorR(BOOK))) as before,zipfile.ZipFile(D/BOOK) as after:
        need(after.testzip() is None and before.namelist()==after.namelist(),'R OOXML original files and crc')
        oldpaths=pub.old.sheetpaths(before);paths=pub.old.sheetpaths(after)
        need(len(oldpaths)==len(paths)==26 and oldpaths==paths,'R same 26 original worksheets')
        changed={paths[x] for x in ('Master Crosswalk','DIM Register','Summary','Validation','Legend')}
        need(all(before.read(n)==after.read(n) for n in before.namelist() if n not in changed),'R all 21 unrelated sheets and OOXML components preserved')
        q=pub.q
        root=ET.fromstring(after.read(paths['Master Crosswalk']))
        rows={int(x.get('r')):x for x in root.find(q('sheetData')).findall(q('row'))}
        for i,values in enumerate(m['review_grid'],1):
            cc={x.get('r'):x for x in rows[i].findall(q('c'))}
            for j,v in enumerate(values,1):
                addr=letter(j)+str(i)
                if addr in cc:need(pub.f3_cell_text(cc[addr])==v,'R saved grid cell '+addr)
                else:need(v=='','R no empty mapped nonblank '+addr)
        def style(i):return next(x.get('s') for x in rows[i] if x.get('r')=='J'+str(i))
        need(style(431)==style(429)==style(432),'R both new candidates specialized amber')
        reg=ET.fromstring(after.read(paths['DIM Register']))
        regrows={int(x.get('r')):x for x in reg.find(q('sheetData')).findall(q('row'))}
        for j,c in enumerate(a['candidates']):
            idx=404+j;need(next(pub.f3_cell_text(v) for v in regrows[idx] if v.get('r')=='A'+str(idx))==c['row_id'],'R register row')
        for name in ('Summary','Validation','Legend'):
            root=ET.fromstring(after.read(paths[name]))
            need(any('SO-2F-R' in pub.f3_cell_text(c) for c in root.iter(q('c'))),'R summary '+name)
    led=load(LEDGER)
    need(len(led['SO2_source_opportunity_assessments'])==9 and led['SO2_source_opportunity_assessments']['SO-2F-R']['workbook_sha256']==sha,'R G4 ledger source/workbook snapshot')
    p=(D/PITON).read_text(encoding='utf-8')
    need('STOP for owner disposition' in p and '581-ID' in p and len(p.split())<=1000,'R proper compact owner stop')
    need('# SO-2F-R COMPLETE' in (D/NARRATIVE).read_text(encoding='utf-8'),'R plain English result published in existing comparison')
    print('PASS SO-2F-R: 581 IDs accounted, new 414=250 supporting/35 represented/83 source-only/46 held. 404 rows, 432x16 saved comparisons, J431:J432 amber; 684 classifications, all previous 402 rows/21 untouched sheets/26-sheet workbook/M00-M01 retained.')
    print('LIMIT: external ANSI/VITA, dense figure/matrix legal cells, installed devices, native Microsoft Excel clean reopening and adoption unverified.')

def applyR():
    m=load(MASTER);src=load(SOURCE)
    if m['currentEvidenceCheckpoint']==CPR:
        verifyR();print('R already saved; idempotent.');return
    cs=source_preflightR(m,src)
    add_rowsR(m,src,cs)
    sha=workbookR(m,cs)
    m['currentWorkbookSha256']=sha;m['currentEvidenceCheckpoint']=CPR
    m['counts']['informationRows']=404;m['counts']['SOSA_SO2FR_new_candidate_rows']=2
    m['counts']['SOSA_SO2FR_remaining_original_records_accounted']=414
    m['counts']['SOSA_SO2F_total_original_records_accounted']=581
    m['workbookSnapshot'].update(checkpoint=CPR,sha256=sha,information_rows=404,
      textInformationRows=404,text_grid_rows=432,saved_xlsx_grid_rows=432,
      color_cell_count=576,mixed_source_cells_uncolored=108,explicit_unassessed_rows=316,
      lag='ZERO: 432x16 saved values, two specialized amber J431:J432, all prior records unchanged',
      textCheckpoint='SOSA_SO2FR_FULL_581_SOURCE_OPPORTUNITY_CLOSEOUT',
      validation_file=LEDGER+'#/SO2_source_opportunity_assessments/SO-2F-R')
    m['nextOwnerAction']='STOP for owner bounded-PARTIAL SOSA opportunity disposition; source first complete to frozen 581. No new Proceed/source packet or automatic adoption.'
    m['SOSA_SO2FR_opportunity_closeout']={'status':'SAVED_VERIFIED__REMOTE_PUBLICATION_READBACK_PENDING','source_manifest':SOURCE,
      'source_records_assessed_here':414,'full_581_ids_accounted':True,
      'specialized_rows':[c['row_id'] for c in cs],'new_cells':['J431','J432'],
      'workbook_sha256':sha,'SOSA_bounded_partial_holds_preserved':True}
    mirrorsR(m);save(MASTER,m);narrativeR();routesR(src,sha);verifyR()



# The owner-authorized G-J continuation uses the same publisher and saved-file gates.
BASE_GJ='49ba4a4a2e6ebbedccc667a881bb94ce1d052395'
CP_GJ='SOSA_SO2GJ_SAVED_VERIFIED'
PACKETS_GJ={'SO-2G':348,'SO-2H':427,'SO-2I':609,'SO-2J':262}
OUTCOMES_GJ={'ADEQUATELY_REPRESENTED','ADDITION_WARRANTED',
             'SOURCE_SPECIFIC_NO_NEW_ROW','HELD_EXACT_QUESTION'}
def prior_gj(name):
    return subprocess.check_output(['git','show',BASE_GJ+':'+str((D/name).relative_to(ROOT))],cwd=ROOT)
def json_pointer(value,pointer):
    need(pointer.startswith('#/'),'GJ original pointer')
    for token in pointer[2:].split('/'):
        token=token.replace('~1','/').replace('~0','~')
        value=value[int(token)] if isinstance(value,list) else value[token]
    return value
def opportunity_ids(entry):
    if 'records' in entry:
        return [r.get('source_id',r.get('id')) for r in entry['records']]
    return entry.get('source_ids',[])
def preflight_gj(ledger):
    base=json.loads(prior_gj(LEDGER))
    need(ledger['SO1_existing_findings_opportunity_inventory']==base['SO1_existing_findings_opportunity_inventory'],
         'GJ frozen original inventory unchanged')
    for key,value in base['SO2_source_opportunity_assessments'].items():
        need(ledger['SO2_source_opportunity_assessments'][key]==value,'GJ preserve previous assessment '+key)
    for key,value in base.items():
        if key!='SO2_source_opportunity_assessments':
            need(ledger[key]==value,'GJ preserve original ledger key '+key)
    frozen={r['source_id']:r for r in ledger['SO1_existing_findings_opportunity_inventory']['records']
            if r.get('proposed_packet') in PACKETS_GJ}
    need(len(frozen)==1646,'GJ frozen exact scope')
    files={}; records=[]; seen=set()
    close=ledger['SO2_remaining_scope_closeout']
    candidates=close['candidates']; candidate_ids={c['row_id'] for c in candidates}
    need(len(candidates)==len(candidate_ids),'GJ unique candidate IDs')
    old_master=json.loads(prior_gj(MASTER)); existing={r['row_id'] for r in old_master['rows']}
    need(not existing.intersection(candidate_ids),'GJ candidate IDs new')
    for packet,count in PACKETS_GJ.items():
        entry=ledger['SO2_source_opportunity_assessments'][packet]
        expected={k for k,v in frozen.items() if v['proposed_packet']==packet}
        rows=entry['records']
        need(len(rows)==count and {r['source_id'] for r in rows}==expected,'GJ exact '+packet+' IDs')
        need(entry['record_count']==len(rows),'GJ packet count '+packet)
        need(entry['outcomes']=={k:sum(r['outcome']==k for r in rows) for k in OUTCOMES_GJ
                                if any(r['outcome']==k for r in rows)},'GJ packet outcomes '+packet)
        groups={g['group_id']:g for g in entry['groups']}
        need(len(groups)==len(entry['groups']),'GJ unique groups '+packet)
        for r in rows:
            rid=r['source_id']; f=frozen[rid]
            need(rid not in seen,'GJ no duplicate ID');seen.add(rid)
            need(r['outcome'] in OUTCOMES_GJ,'GJ evidenced outcome '+rid)
            need(r['original_records']==f['original_records'],'GJ original pointers/hashes '+rid)
            need(r['retained_contact_tier']==f['contact_tier'],'GJ retained actual contact '+rid)
            need(r['group_id'] in groups and rid in groups[r['group_id']]['source_ids'],'GJ member/group '+rid)
            need(bool(r['original_locator']) and bool(r['original_standing']) and bool(r['rationale']),'GJ source grade/rationale '+rid)
            need(set(r.get('existing_row_ids',[]))<=existing,'GJ existing links '+rid)
            need(set(r.get('candidate_row_ids',[]))<=candidate_ids,'GJ candidate links '+rid)
            if r['outcome']=='ADDITION_WARRANTED':need(bool(r.get('candidate_row_ids')),'GJ addition has candidate '+rid)
            if r['outcome']=='ADEQUATELY_REPRESENTED':need(bool(r.get('existing_row_ids')),'GJ represented meaning has row '+rid)
            if r['outcome']=='HELD_EXACT_QUESTION':need(bool(r.get('exact_hold')),'GJ exact held question '+rid)
            for source in r['original_records']:
                if source['file'] not in files:files[source['file']]=load(source['file'])
                native=json_pointer(files[source['file']],source['pointer'])
                actual=digest(json.dumps(native,ensure_ascii=False,sort_keys=True).encode())
                need(actual==source['record_sha256'],'GJ original source record hash '+rid)
            records.append(r)
        for group in groups.values():
            members=[r['source_id'] for r in rows if r['group_id']==group['group_id']]
            need(set(members)==set(group['source_ids']) and len(members)==len(group['source_ids']),'GJ exact group members')
            need(bool(group['rationale']),'GJ group source-based rationale')
    need(seen==set(frozen),'GJ no missing or extra original IDs')
    actual_outcomes={key:sum(r['outcome']==key for r in records) for key in OUTCOMES_GJ}
    need(close['counts']['outcomes']==actual_outcomes,'GJ outcomes reconcile to all original records')
    index={r['source_id']:r for r in records}
    for c in candidates:
        need(c['classification'] in ('COMMON_CANDIDATE','SPECIALIZED_CANDIDATE'),'GJ qualified class')
        need(bool(c['definition']) and bool(c['classification_rationale']) and bool(c['rationale']),'GJ candidate rationale')
        need(set(c['closest_existing_rows'])<=existing,'GJ closest prior meanings')
        ids=c['evidence_ids'];need(ids and len(ids)==len(set(ids)),'GJ candidate source IDs')
        for rid in ids:
            need(rid in index and c['row_id'] in index[rid]['candidate_row_ids'],'GJ supported candidate '+rid)
        actual={r['source_id'] for r in records if c['row_id'] in r.get('candidate_row_ids',[])}
        need(actual==set(ids),'GJ candidate support exactly reconciled')
    all_ids=[]
    for entry in ledger['SO2_source_opportunity_assessments'].values():all_ids+=opportunity_ids(entry)
    expected_all={r['source_id'] for r in ledger['SO1_existing_findings_opportunity_inventory']['records']
                  if r['inventory_outcome']=='RESIDUAL_OPPORTUNITY_ASSESSMENT_REQUIRED'}
    need(len(all_ids)==len(set(all_ids))==3755 and set(all_ids)==expected_all,'GJ complete 3755 opportunity inventory')
    need(close['counts']['remaining_records']==1646 and close['counts']['total_opportunity_records']==3755,
         'GJ truthful completion counts')
    need(close['counts']['new_candidate_rows']==len(candidates),'GJ candidate count')
    need(close['counts']['candidate_classifications']=={
        k:sum(c['classification']==k for c in candidates)
        for k in ('COMMON_CANDIDATE','SPECIALIZED_CANDIDATE')},'GJ classification counts')
    return candidates,records

def add_gj_rows(m,candidates):
    need(len(m['rows'])==404 and len(m['review_grid'])==432,'GJ original master dimensions')
    for c in candidates:
        n=len(m['review_grid'])+1
        vals=['Not linked here — no case evidence established.']*4+[
            'Not assessed here — no verified correspondence; not evidence of absence.']*11+[
            'OPTIONAL information-need candidate: '+c['label'].removeprefix('Candidate — ')+' — NOT ADOPTED']
        vals[9]='['+c['classification'].replace('_',' ')+'] PARTIAL / NEW INFORMATION NEED: '+c['definition']+' ['+c['source_summary']+'; SO-2GJ; exact original IDs and limits in the source ledger.]'
        mapping={'donor':c['donor_edition'],'source_ids':c['evidence_ids'],
          'original_source_locators':c['original_source_locators'],'native_meaning':c['definition'],
          'closest_prior_rows':c['closest_existing_rows'],'reason_for_separate_candidate':c['rationale'],
          'relation':c['relation'],'candidate_status':c['classification'],
          'classification_rationale':c['classification_rationale'],
          'fill':'#D9EAF8' if c['classification']=='COMMON_CANDIDATE' else '#F9E6B8',
          'cell':'J'+str(n),'DIM_Profile_adopted':False,'case_or_runtime_verified':False,
          'source_contact':c['source_contact'],'source_limits':c['source_limits'],
          'source_ledger':LEDGER+'#/SO2_remaining_scope_closeout/candidates'}
        r={'row_id':c['row_id'],'label':c['label'],'display_row':n,
          'status':'SO-2GJ provisional source-qualified information-need candidate; NOT ADOPTED',
          'definition':c['definition'],'source_entry_ids':c['evidence_ids'],'evidence_records':c['evidence_ids'],
          'master_inclusion':'PROVISIONAL_NATIVE_SOSA_CANDIDATE',
          'dim_adoption':'NO_CONTENT_ADOPTION_DECISION_IN_THIS_UPDATE','source_review_status':c['source_contact'],
          'display':vals,'SO2_source_correspondence':mapping}
        need(len(vals)==16 and all(str(x).strip() for x in vals),'GJ explicit new cells')
        m['rows'].append(r);m['review_grid'].append(vals)

def workbook_gj(m,candidates,close):
    olddata=(D/BOOK).read_bytes();q=pub.q;edited={}
    n=len(m['rows']);ng=len(m['review_grid']);nc=len(candidates)
    outcomes=close['counts']['outcomes']
    overview=f'{n} information rows; SAME 26-sheet workbook. {nc} new source-qualified candidates; no DIM/Profile adoption. F3 accepted; AAS acceptance separate; M00/M01 preserved.'
    brief=f'1,646 remaining records accounted: {outcomes["ADDITION_WARRANTED"]} candidate support; {outcomes["ADEQUATELY_REPRESENTED"]} represented; {outcomes["SOURCE_SPECIFIC_NO_NEW_ROW"]} source-specific/no row; {outcomes["HELD_EXACT_QUESTION"]} held.'
    summary={'A1':'CURRENT — SOSA remaining opportunity assessment completed',
      'B1':overview,
      'B13':'Earlier SOSA bounded-PARTIAL standing accepted; this completed opportunity continuation awaits owner disposition. Nine original source-hold families retained.',
      'B17':brief,
      'B19':f'{ng} × 16 = {ng*16:,} saved comparison values; {684+nc} classified cells, {576+nc} colored / 108 held. Source holds and comparison classifications are separate counts.',
      'B21':close['source_contact_summary'],
      'B22':close['candidate_summary'],
      'B23':'STOP for owner disposition. All 3,755 frozen opportunities accounted for at recorded source depth. AAS acceptance remains separate; next planned donor OPC UA Devices requires authorization.',
      'B28':'All prior 404 information rows and 432 grid rows, 21 unaffected sheets and protected M00/M01 preserved. Native Microsoft Excel clean reopening remains unverified.'}
    sheets={'Summary':summary,'Validation':dict(summary),
      'Legend':{'A1':'CURRENT LEGEND — SOSA SO-2GJ; candidate classification is not adoption',
      'B23':f'{576+nc} colored / 108 held classifications. {nc} additional source-qualified candidate cells; all 684 preceding classifications retained.',
      'B24':f'{n} information rows; {ng} × 16 complete comparison values; 26 original divider rows.',
      'A28':'Finite SOSA remaining-scope completion',
      'B28':'2,109 prior + 1,646 remaining = 3,755 opportunity IDs. Exact source holds remain; candidate rows do not prove actual device support or conformance.'}}
    with zipfile.ZipFile(io.BytesIO(olddata)) as z:
        paths=pub.old.sheetpaths(z);need(len(paths)==26,'GJ same sheets')
        for name in ('Master Crosswalk','DIM Register'):
            path=paths[name];root=ET.fromstring(z.read(path));sd=root.find(q('sheetData'))
            rm={int(r.get('r')):r for r in sd.findall(q('row'))}
            template=rm[432 if name=='Master Crosswalk' else 405]
            styles={}
            if name=='Master Crosswalk':
                styles={kind:next(c.get('s') for c in rm[idx] if c.get('r')=='J'+str(idx))
                        for kind,idx in [('COMMON_CANDIDATE',428),('SPECIALIZED_CANDIDATE',431)]}
            for j,c in enumerate(candidates):
                idx=433+j if name=='Master Crosswalk' else 406+j
                rr=copy.deepcopy(template);rr.set('r',str(idx));rr.set('ht','330');rr.set('customHeight','1')
                item=m['rows'][404+j]
                source_trace=', '.join(c['evidence_ids'][:5])+f'; {len(c["evidence_ids"])} exact supporting IDs in '+LEDGER+'#/SO2_remaining_scope_closeout/candidates/'+str(j)
                if name=='Master Crosswalk':values=item['display']
                else:
                    values=[item['row_id'],item['label'],item['definition'],item['status'],item['source_review_status'],
                      item['master_inclusion'],item['dim_adoption'],'Not assessed here','Not assessed here',source_trace,
                      c['relation']+'; '+c['rationale'],c['source_summary'],'Not assessed here','Not assessed here',
                      c['classification']+'; '+c['classification_rationale'],
                      source_trace+'; '+c['source_limits'],'Not assessed here',
                      'Not assessed here — AAS equivalence unassessed.']
                cells={re.match('[A-Z]+',x.get('r')).group():x for x in rr.findall(q('c'))}
                for k,value in enumerate(values,1):
                    col=letter(k);cell=cells.get(col)
                    if cell is None:cell=ET.SubElement(rr,q('c'),{'r':col+str(idx)})
                    cell.set('r',col+str(idx));pub.f3_put(cell,str(value))
                    if name=='Master Crosswalk' and col=='J':cell.set('s',styles[c['classification']])
                sd.append(rr)
            last=('P'+str(ng)) if name=='Master Crosswalk' else ('R'+str(n+1))
            root.find(q('dimension')).set('ref','A1:'+last)
            af=root.find(q('autoFilter'))
            if af is not None:af.set('ref',('A2:' if name=='Master Crosswalk' else 'A1:')+last)
            edited[path]=ET.tostring(root,encoding='utf-8',xml_declaration=True)
        for name,values in sheets.items():
            root=ET.fromstring(z.read(paths[name]));cells={c.get('r'):c for c in root.iter(q('c'))}
            for address,value in values.items():
                need(address in cells,'GJ existing guidance '+name+'!'+address)
                pub.f3_put(cells[address],value)
            if name in ('Summary','Validation'):
                r13=next(r for r in root.find(q('sheetData')).findall(q('row')) if r.get('r')=='13')
                r13.set('ht','64');r13.set('customHeight','1')
            edited[paths[name]]=ET.tostring(root,encoding='utf-8',xml_declaration=True)
        buf=io.BytesIO()
        with zipfile.ZipFile(buf,'w') as out:
            for info in z.infolist():out.writestr(info,edited.get(info.filename,z.read(info.filename)))
    (D/BOOK).write_bytes(buf.getvalue())
    return digest(buf.getvalue())

def verify_gj():
    m=load(MASTER);l=load(LEDGER);c=l['SO2_remaining_scope_closeout']
    cs,records=preflight_gj(l);n=len(cs);base=json.loads(prior_gj(MASTER))
    need(m['currentEvidenceCheckpoint']==CP_GJ,'GJ checkpoint')
    need(len(m['rows'])==404+n and len(m['review_grid'])==432+n,'GJ dimensions')
    need(m['rows'][:404]==base['rows'] and m['review_grid'][:432]==base['review_grid'],'GJ every prior information row unchanged')
    for key in ('columns','review_sections','manualWorkbookMilestones','caseEvidence','priorHolds'):
        need(m[key]==base[key],'GJ preserve '+key)
    sha=digest((D/BOOK).read_bytes())
    need(sha==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==c['workbook_sha256'],'GJ workbook hashes')
    need(m['workbookSnapshot']['color_cell_count']==576+n and m['workbookSnapshot']['mixed_source_cells_uncolored']==108,'GJ classification counts')
    for j,candidate in enumerate(cs):
        row=m['rows'][404+j]
        need(row['row_id']==candidate['row_id'] and row['display']==m['review_grid'][432+j],'GJ added row links')
        need(all(str(v).strip() for v in row['display']),'GJ no blanks in completed row')
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/f).open(encoding='utf-8',newline='') as inp:need(list(csv.reader(inp))==m['review_grid'],'GJ CSV '+f)
    need((D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_bytes()==(D/'ISA_Correction_Review_07NOV2026.md').read_bytes(),'GJ readable parity')
    with zipfile.ZipFile(io.BytesIO(prior_gj(BOOK))) as old,zipfile.ZipFile(D/BOOK) as new:
        need(new.testzip() is None and new.namelist()==old.namelist(),'GJ original ZIP inventory')
        op=pub.old.sheetpaths(old);np=pub.old.sheetpaths(new)
        need(op==np and len(np)==26,'GJ same original 26 sheets')
        changed={np[k] for k in ('Master Crosswalk','DIM Register','Summary','Validation','Legend')}
        need(all(old.read(f)==new.read(f) for f in old.namelist() if f not in changed),'GJ all unrelated parts/21 sheets byte-identical')
        q=pub.q;root=ET.fromstring(new.read(np['Master Crosswalk']))
        rows={int(r.get('r')):r for r in root.find(q('sheetData')).findall(q('row'))}
        need(list(rows)==sorted(rows) and len(rows)==len(m['review_grid']),'GJ ordered unique worksheet rows')
        for i,values in enumerate(m['review_grid'],1):
            cells={c.get('r'):c for c in rows[i].findall(q('c'))}
            need(len(cells)==len(rows[i].findall(q('c'))),'GJ unique cells')
            for j,value in enumerate(values,1):
                cell=cells.get(letter(j)+str(i))
                need((pub.f3_cell_text(cell) if cell is not None else '')==value,'GJ saved cell '+letter(j)+str(i))
                if cell is not None:need(cell.get('t')!='e','GJ no error cell')
        oldrows={int(r.get('r')):r for r in ET.fromstring(old.read(op['Master Crosswalk'])).find(q('sheetData')).findall(q('row'))}
        for i in range(1,433):
            need(ET.tostring(rows[i])==ET.tostring(oldrows[i]),'GJ prior saved row/fill preserved '+str(i))
        styles={kind:next(c.get('s') for c in rows[idx] if c.get('r')=='J'+str(idx))
                for kind,idx in [('COMMON_CANDIDATE',428),('SPECIALIZED_CANDIDATE',431)]}
        reg={int(r.get('r')):r for r in ET.fromstring(new.read(np['DIM Register'])).find(q('sheetData')).findall(q('row'))}
        for j,candidate in enumerate(cs):
            addr='J'+str(433+j);cell=next(c for c in rows[433+j] if c.get('r')==addr)
            need(cell.get('s')==styles[candidate['classification']],'GJ saved source fill '+addr)
            need(next(pub.f3_cell_text(v) for v in reg[406+j] if v.get('r')=='A'+str(406+j))==candidate['row_id'],'GJ register row')
        for name in ('Summary','Validation','Legend'):
            text=' '.join(pub.f3_cell_text(c) for c in ET.fromstring(new.read(np[name])).iter(q('c')))
            need('1,646' in text and '3,755' in text,'GJ current summary '+name)
    print(f'PASS SO-2GJ: all1646 original IDs/pointers/hashes and 3755 total opportunities; {n} new candidates; {404+n} rows, {(432+n)*16} saved values; prior404 rows, 21 unaffected sheets, 26-sheet workbook and M00/M01 preserved.')
    print('LIMIT: retained source grades and exact holds remain; native Microsoft Excel reopen and model/Profile adoption unverified.')

def apply_gj():
    m=load(MASTER);l=load(LEDGER)
    if m['currentEvidenceCheckpoint']==CP_GJ:
        verify_gj();return
    cs,records=preflight_gj(l);close=l['SO2_remaining_scope_closeout']
    need(m['currentEvidenceCheckpoint']==CPR,'GJ expected published F-R')
    need(digest((D/BOOK).read_bytes())==m['currentWorkbookSha256']==digest(prior_gj(BOOK)),'GJ baseline workbook')
    add_gj_rows(m,cs);sha=workbook_gj(m,cs,close);n=len(cs);ng=432+n
    m['currentEvidenceCheckpoint']=CP_GJ;m['currentWorkbookSha256']=sha
    m['counts'].update(informationRows=404+n,SOSA_SO2GJ_new_candidate_rows=n,
      SOSA_SO2GJ_original_records_accounted=1646,SOSA_SO2_total_opportunity_records_accounted=3755)
    m['workbookSnapshot'].update(checkpoint=CP_GJ,sha256=sha,information_rows=404+n,textInformationRows=404+n,
      text_grid_rows=ng,saved_xlsx_grid_rows=ng,color_cell_count=576+n,mixed_source_cells_uncolored=108,
      explicit_unassessed_rows=316+n,lag=f'ZERO: {ng}x16 saved values; {n} new candidate cells; all prior rows/fills preserved',
      textCheckpoint='SOSA_SO2GJ_FULL_REMAINDER_CLOSEOUT',
      gate_metadata_note='All 3,755 frozen SOSA opportunity IDs accounted; STOP for owner disposition. AAS acceptance separate. Historical source counters retain their recorded scopes.',
      validation_file=LEDGER+'#/SO2_remaining_scope_closeout')
    m['nextOwnerAction']='STOP for owner disposition of completed bounded-PARTIAL SOSA opportunity assessment. AAS acceptance separate; donor research remains; no automatic DIM/Profile development.'
    m['SOSA_SO2GJ_opportunity_closeout']={'status':'SAVED_VERIFIED__REMOTE_READBACK_PENDING','source_ledger':LEDGER,
      'remaining_source_records_accounted':1646,'total_opportunity_records_accounted':3755,
      'new_candidate_rows':[c['row_id'] for c in cs],'workbook_sha256':sha,'all_original_holds_preserved':True}
    close.update(status='SAVED_VERIFIED__REMOTE_READBACK_PENDING',workbook_sha256=sha,
      information_rows=404+n,grid_values=ng*16,classified_cells=684+n,colored_cells=576+n,held_comparisons=108)
    for packet in PACKETS_GJ:
        l['SO2_source_opportunity_assessments'][packet]['status']='SAVED_VERIFIED__REMOTE_READBACK_PENDING'
    text_mirrors(m)
    banner=f'# Current comparison — SOSA remaining opportunity assessment completed\n\n{404+n} information rows; {n} new source-qualified candidates. All 1,646 remaining and 3,755 total frozen opportunities accounted at recorded source depth. Prior404 rows and684 classifications preserved. See {LEDGER}#/SO2_remaining_scope_closeout for exact outcomes and holds. STOP for owner disposition; AAS acceptance separate; donor research continues before later model decisions.\n\n'
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.md','ISA_Correction_Review_07NOV2026.md'):
        p=D/f;txt=p.read_text();p.write_text(banner+txt[txt.index('<table>'):],encoding='utf-8')
    save(MASTER,m);save(LEDGER,l);verify_gj()
    close['verification'].update(all_original_record_hashes=True,
      same_workbook_saved_value_fill_parity=True,
      exact_remaining_and_total_opportunity_reconciliation=True,
      both_CSV_and_readable_mirrors=True,
      all_prior_master_rows_and_21_unaffected_sheets_preserved=True,
      M00_M01_preserved=True)
    save(LEDGER,l)

SAP11_LEDGER='SAP01_Original_Corpus_Coverage_12NOV2026.json'
SAP11_KEY='SAP11_current_master_reconciliation'
SAP11_BASE='ec29e583792ea5d799dea0417417961ee115524c'
SAP11_CP='SAPIENT_SAP11_SAVED_VERIFIED'

def sap11_prior(name):
    return subprocess.check_output(['git','show',SAP11_BASE+':'+str((D/name).relative_to(ROOT))],cwd=ROOT)

def verify_sap11():
    """Verify the finite SAPIENT follow-through and preservation of its accepted baseline."""
    m=load(MASTER);ledger=load(SAP11_LEDGER);scope=ledger[SAP11_KEY]
    base=json.loads(sap11_prior(MASTER));oldledger=json.loads(sap11_prior(SAP11_LEDGER))
    expected={'SAP02-N04','SAP02-N06','SAP03A-N06','SAP03A-N10','SAP03A-N11','SAP03B-N01',
              'SAP03B-N09','SAP03B-N10','SAP04-N09','SAP04-N15','SAP06-N14'}
    need(m['currentEvidenceCheckpoint']==SAP11_CP,'SAP11 checkpoint')
    need(len(scope['records'])==11 and {r['native_finding_id'] for r in scope['records']}==expected,'SAP11 frozen eleven IDs')
    need(all(ledger[k]==v for k,v in oldledger.items()),'SAP11 all prior source/acceptance records unchanged')
    findings={r['native_finding_id']:r for r in oldledger['F2_3_native_candidate_opportunity']['source_records']}
    rowids={r['row_id'] for r in m['rows']}
    for r in scope['records']:
        raw=json.dumps(findings[r['native_finding_id']],sort_keys=True,ensure_ascii=False).encode()
        need(digest(raw)==r['prior_F2_record_sha256'],'SAP11 original finding hash '+r['native_finding_id'])
        need(r['rationale'] and set(r['target_row_ids'])<=rowids,'SAP11 explicit supported targets')
    cs=scope['candidates'];changes={r['row_id']:r for r in scope['cell_changes']}
    need(len(cs)==7 and len(changes)==13,'SAP11 seven additions/thirteen clarified cells')
    need(sum(r['outcome']=='ADDITION_WARRANTED' for r in scope['records'])==7,'SAP11 complete outcomes')
    need(sum(c['classification']=='COMMON_CANDIDATE' for c in cs)==4,'SAP11 classification distribution')
    need(len(m['rows'])==432 and len(m['review_grid'])==460 and len(rowids)==432,'SAP11 unique dimensions')
    need([r['row_id'] for r in m['rows'][:425]]==[r['row_id'] for r in base['rows']],'SAP11 prior stable ID order')
    for old,row in zip(base['rows'],m['rows'][:425]):
        if row['row_id'] not in changes: need(row==old,'SAP11 untouched row '+row['row_id']);continue
        ch=changes[row['row_id']];rest=copy.deepcopy(row);rest.pop('SAP11_source_correspondence')
        rest['display'][7]=old['display'][7]
        need(rest==old and row['display'][7]==ch['current_value'] and old['display'][7]==ch['previous_value'],'SAP11 exact allowed change '+row['row_id'])
    allowed={c['grid_row']:c['current_value'] for c in changes.values()}
    for i,(old,new) in enumerate(zip(base['review_grid'],m['review_grid'][:453]),1):
        expect=old.copy()
        if i in allowed:expect[7]=allowed[i]
        need(new==expect,'SAP11 preserve prior grid except named H cells '+str(i))
    for key in ('columns','review_sections','manualWorkbookMilestones','caseEvidence','priorHolds','SOSA_SO2GJ_opportunity_closeout','AAS_O7_reconciliation'):
        need(m[key]==base[key],'SAP11 preserve '+key)
    for c,r in zip(cs,m['rows'][425:]):
        need(r['row_id']==c['row_id'] and r['SAP11_source_correspondence']['DIM_Profile_adopted'] is False,'SAP11 new candidate provenance')
        need(r['display']==m['review_grid'][r['display_row']-1] and all(v.strip() for v in r['display']),'SAP11 explicit complete candidate cells')
    sha=digest((D/BOOK).read_bytes())
    need(sha==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256']==scope['workbook_sha256'],'SAP11 workbook hash')
    for f in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/f).open(encoding='utf-8',newline='') as h:need(list(csv.reader(h))==m['review_grid'],'SAP11 CSV parity')
    need((D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_bytes()==(D/'ISA_Correction_Review_07NOV2026.md').read_bytes(),'SAP11 readable parity')
    with zipfile.ZipFile(io.BytesIO(sap11_prior(BOOK))) as old,zipfile.ZipFile(D/BOOK) as new:
        need(new.testzip() is None and new.namelist()==old.namelist(),'SAP11 ZIP integrity and original parts')
        op=pub.old.sheetpaths(old);np=pub.old.sheetpaths(new)
        need(op==np and len(np)==26,'SAP11 original26 worksheets')
        edited={np[n] for n in scope['workbook_edits']}
        need(all(old.read(f)==new.read(f) for f in old.namelist() if f not in edited),'SAP11 21 unaffected sheets and all unrelated parts byte-identical')
        def sheetrows(z,p):return {int(r.get('r')):r for r in ET.fromstring(z.read(p)).find(pub.q('sheetData')).findall(pub.q('row'))}
        mr=sheetrows(new,np['Master Crosswalk']);omr=sheetrows(old,op['Master Crosswalk'])
        need(len(mr)==460 and list(mr)==sorted(mr),'SAP11 ordered unique master rows')
        styles={kind:next(c.get('s') for c in omr[idx] if c.get('r')=='J'+str(idx)) for kind,idx in [('COMMON_CANDIDATE',428),('SPECIALIZED_CANDIDATE',431)]}
        for i,values in enumerate(m['review_grid'],1):
            cells={c.get('r'):c for c in mr[i]}
            need(len(cells)==len(mr[i]),'SAP11 no duplicate cells')
            for j,v in enumerate(values,1):
                c=cells.get(letter(j)+str(i));need((pub.f3_cell_text(c) if c is not None else '')==v,'SAP11 saved grid '+letter(j)+str(i))
                if c is not None:need(c.get('t')!='e','SAP11 no error cells')
        for name,edit in scope['workbook_edits'].items():
            oldrows=sheetrows(old,op[name]);newrows=sheetrows(new,np[name])
            for n,rr in oldrows.items():
                clean=copy.deepcopy(newrows[n]);cells={c.get('r'):c for c in clean}
                if str(n) in edit.get('row_heights',{}):
                    need(float(clean.get('ht'))==edit['row_heights'][str(n)],'SAP11 fitted affected row')
                    clean.attrib.clear();clean.attrib.update(rr.attrib)
                for oc in rr:
                    addr=oc.get('r')
                    if addr in edit['cells']:
                        nc=cells[addr];need(pub.f3_cell_text(nc)==edit['cells'][addr],'SAP11 saved edit '+name+'!'+addr)
                        if addr in edit['fills']:need(nc.get('s')==styles['COMMON_CANDIDATE'],'SAP11 common fill '+addr)
                        clean.remove(nc);clean.insert(list(rr).index(oc),copy.deepcopy(oc))
                need(ET.tostring(clean)==ET.tostring(rr),'SAP11 unrelated cells/row attributes preserved '+name+' '+str(n))
            for added in edit['append']:
                rr=newrows[added['number']];cells={c.get('r'):c for c in rr}
                for i,v in enumerate(added['values'],1):need(pub.f3_cell_text(cells[letter(i)+str(added['number'])])==v,'SAP11 appended value')
        for c,r in zip(cs,m['rows'][425:]):
            cell=next(x for x in mr[r['display_row']] if x.get('r')=='H'+str(r['display_row']))
            need(cell.get('s')==styles[c['classification']],'SAP11 source candidate fill')
        need(all(m['rows'][i]['display'][7].strip() for i in range(432)),'SAP11 no blank SAPIENT information cells')
    need(scope['counts']['classified_cells']==715 and m['workbookSnapshot']['color_cell_count']==607 and m['workbookSnapshot']['mixed_source_cells_uncolored']==108,'SAP11 current count metadata')
    print('PASS SAP11: 11/11 outcomes; 7 new candidates, 13 clarified cells; 432 rows / 7,360 saved values; CSV/readable parity; source holds and prior425 IDs preserved; 26 sheets, 21 unaffected sheets/other parts and M00/M01 unchanged.')
    print('LIMIT: selected original-source depth, source conflicts and native Microsoft Excel reopen limitations retained; no model adoption or donor transition.')

OPCDI_CP='OPCDI_SAVED_VERIFIED'
OPCDI_LEDGER='OPC_UA_Devices_Source_Coverage.json'
OPCDI_BASE='7d965e2a174190a39e3b0e3506da467c5c3cc50e'

def verify_opcdi():
    """Verify the fixed Devices corpus dispositions and exact authorized workbook delta."""
    m=load(MASTER);l=load(OPCDI_LEDGER)
    def prior(name):return subprocess.check_output(['git','show',OPCDI_BASE+':'+str((D/name).relative_to(ROOT))],cwd=ROOT)
    base=json.loads(prior(MASTER));rowids={r['row_id'] for r in m['rows']}
    need(m['currentEvidenceCheckpoint']==OPCDI_CP,'Devices checkpoint')
    need(len(m['rows'])==454 and len(rowids)==454 and len(m['review_grid'])==482,'Devices dimensions/unique IDs')
    need(len(l['native_findings'])==33 and len(l['candidates'])==22 and len(l['row_comparisons'])==432,'Devices finite representation inventory')
    need(len(l['section_inventory'])==286 and len({x['id'] for x in l['section_inventory']})==286,'Devices section accounting')
    need(len(l['model_node_inventory'])==507 and len({x['id'] for x in l['model_node_inventory']})==507,'Devices model accounting')
    need(len(l['source_manifest']['files'])==21 and len(l['figure_contact'])==84,'Devices source manifest/figure inventory including logo')
    need(sum(x['contact']=='VISUALLY_INSPECTED' for x in l['figure_contact'])==83,'Devices actual figure contact')
    need(all(x.get('native_finding_ids') for x in l['model_node_inventory']),'Devices all nodes have semantic family disposition')
    need(all(x['status']=='ACCOUNTED_FOR_AT_RECORDED_DEPTH' for x in l['source_manifest']['files']),'Devices no unread support file silently complete')
    need(len(l['holds'])==12 and l['completion_limits'],'Devices precise limitations retained')
    for f in l['native_findings']:
        need(f['mapping_outcome']!='PENDING_CURRENT_MASTER_COMPARISON','Devices no pending finding')
        need(set(f['existing_row_targets']+f['candidate_row_targets'])<=rowids,'Devices finding targets exist')
    comparisons={c['row_id']:c for c in l['row_comparisons']}
    need(sum(c['classification']=='COMMON_CANDIDATE' for c in comparisons.values())==73,'Devices existing correspondence count')
    need(sum(c['classification']=='UNCOLORED' for c in comparisons.values())==359,'Devices explicit no-correspondence count')
    need(sum(c['classification']=='COMMON_CANDIDATE' for c in l['candidates'])==17,'Devices new classification')
    need([r['row_id'] for r in m['rows'][:432]]==[r['row_id'] for r in base['rows']],'Devices preserves prior row order')
    for old,new in zip(base['rows'],m['rows'][:432]):
        copyrow=copy.deepcopy(new);copyrow.pop('OPCDI_source_correspondence');copyrow['display'][5]=old['display'][5]
        need(copyrow==old,'Devices only F evidence added to prior row '+old['row_id'])
        need(new['display'][5]==comparisons[old['row_id']]['current_value'],'Devices comparison text parity')
    for k in ('columns','review_sections','manualWorkbookMilestones','caseEvidence','priorHolds','SOSA_SO2GJ_opportunity_closeout','AAS_O7_reconciliation','SAPIENT_SAP11_reconciliation'):
        need(m[k]==base[k],'Devices prior decisions/evidence preserved '+k)
    for k in base:
        if k.endswith('Evidence'):need(m[k]==base[k],'Devices prior donor evidence untouched '+k)
    allowed={c['grid_row']:c['current_value'] for c in comparisons.values()}
    for i,(old,new) in enumerate(zip(base['review_grid'],m['review_grid'][:460]),1):
        expect=old.copy()
        if i in allowed:expect[5]=allowed[i]
        need(new==expect,'Devices prior grid delta '+str(i))
    for c,r in zip(l['candidates'],m['rows'][432:]):
        need(c['row_id']==r['row_id'] and r['OPCDI_source_correspondence']['DIM_Profile_adopted'] is False,'Devices candidate provenance')
        need(r['display']==m['review_grid'][r['display_row']-1] and all(v.strip() for v in r['display']),'Devices explicit candidate cells')
        need(c['addition_rationale'] and set(c['nearest_existing_rows'])<=rowids,'Devices reconsidered nearest existing meanings')
    sha=digest((D/BOOK).read_bytes());need(sha==l['workbook_sha256']==m['currentWorkbookSha256']==m['workbookSnapshot']['sha256'],'Devices saved hash')
    for name in ('Master_Donor_Concept_to_DIM_Crosswalk.csv','ISA_Correction_Review_07NOV2026.csv'):
        with (D/name).open(newline='',encoding='utf-8') as h:need(list(csv.reader(h))==m['review_grid'],'Devices CSV parity')
    need((D/'Master_Donor_Concept_to_DIM_Crosswalk.md').read_bytes()==(D/'ISA_Correction_Review_07NOV2026.md').read_bytes(),'Devices readable mirror parity')
    with zipfile.ZipFile(io.BytesIO(prior(BOOK))) as old,zipfile.ZipFile(D/BOOK) as new:
        need(new.testzip() is None and new.namelist()==old.namelist(),'Devices ZIP and original part list')
        op=pub.old.sheetpaths(old);np=pub.old.sheetpaths(new);need(op==np and len(np)==26,'Devices same26 sheets')
        changed={np[name] for name in l['workbook_edits']}
        need(all(old.read(f)==new.read(f) for f in old.namelist() if f not in changed),'Devices21 unaffected sheets and all unrelated parts byte-identical')
        def rows(z,path):return {int(r.get('r')):r for r in ET.fromstring(z.read(path)).find(pub.q('sheetData'))}
        omr=rows(old,op['Master Crosswalk']);mr=rows(new,np['Master Crosswalk'])
        styles={kind:next(c.get('s') for c in omr[n] if c.get('r')=='J'+str(n)) for kind,n in [('COMMON_CANDIDATE',428),('SPECIALIZED_CANDIDATE',431)]}
        need(len(mr)==482,'Devices master saved rows')
        for i,vals in enumerate(m['review_grid'],1):
            cells={c.get('r'):c for c in mr[i]};need(len(cells)==len(mr[i]),'Devices unique cell addresses')
            for j,v in enumerate(vals,1):
                c=cells.get(letter(j)+str(i));need((pub.f3_cell_text(c) if c is not None else '')==v,'Devices saved value '+letter(j)+str(i))
                if c is not None:need(c.get('t')!='e','Devices no cell errors')
        for name,ed in l['workbook_edits'].items():
            ors=rows(old,op[name]);nrs=rows(new,np[name])
            for n,rr in ors.items():
                clean=copy.deepcopy(nrs[n]);cells={c.get('r'):c for c in clean}
                if str(n) in ed['row_heights']:
                    need(float(clean.get('ht'))==ed['row_heights'][str(n)],'Devices fitted affected height');clean.attrib.clear();clean.attrib.update(rr.attrib)
                for oc in rr:
                    addr=oc.get('r')
                    if addr in ed['cells']:
                        nc=cells[addr];need(pub.f3_cell_text(nc)==ed['cells'][addr],'Devices saved edit '+name+'!'+addr)
                        if addr in ed['fills']:need(nc.get('s')==styles['COMMON_CANDIDATE'],'Devices existing common fill')
                        clean.remove(nc);clean.insert(list(rr).index(oc),copy.deepcopy(oc))
                oldaddrs={x.get('r') for x in rr}
                for addr in ed['cells']:
                    if addr not in oldaddrs and addr in cells:
                        need(pub.f3_cell_text(cells[addr])==ed['cells'][addr],'Devices newly explicit cell')
                        clean.remove(cells[addr])
                need(ET.tostring(clean)==ET.tostring(rr),'Devices unaffected old cells/styles '+name+' '+str(n))
            for item in ed['append']:
                cells={c.get('r'):c for c in nrs[item['number']]}
                for j,v in enumerate(item['values'],1):need(pub.f3_cell_text(cells[letter(j)+str(item['number'])])==v,'Devices appended register/grid')
        neutral=next(c.get('s') for c in omr[460] if c.get('r')=='F460')
        for c,r in zip(l['candidates'],m['rows'][432:]):
            cells={re.match('[A-Z]+',x.get('r')).group():x for x in mr[r['display_row']]}
            need(cells['F'].get('s')==styles[c['classification']],'Devices candidate fill')
            need(all(cells[col].get('s')==neutral for col in 'EGHIJKLMNO'),'Devices no inherited other-donor classification')
    need(all(r['display'][5].strip() for r in m['rows']),'Devices completed column no blanks')
    print('PASS Devices:33 finding groups,286 section entries,507 nodes,83 inspected images;22 candidates/73 existing correspondences/359 explicit nonmatches;454 rows and7,712 saved values; exact mirrors/fills;432 prior IDs,26 sheets,21 unaffected sheets and other ZIP parts/M00/M01 preserved.')
    print('LIMIT:12 exact source limits retained; controlling-document parity, external profile detail, runtime/certification and native Microsoft Excel reopening not claimed.')

if __name__=='__main__':
    need(len(sys.argv)==2 and sys.argv[1] in ('--apply','--verify'),'use --apply or --verify')
    current=load(MASTER)['currentEvidenceCheckpoint']
    if current==OPCDI_CP:
        verify_opcdi();sys.exit(0)
    if current==SAP11_CP:
        verify_sap11();sys.exit(0)
    if current==CP_GJ or 'SO2_remaining_scope_closeout' in load(LEDGER):
        if sys.argv[1]=='--verify':verify_gj()
        else:apply_gj()
        sys.exit(0)
    if sys.argv[1]=='--verify':
        if current==CPR:verifyR()
        elif current==CP3:verify3()
        elif current==CP2:packet2_verify()
        else:verify()
    elif current==CPR:
        verifyR();print('Previously saved SO2FR is unchanged.')
    elif current==CP3:
        applyR()
    else:
        need(False,'SO2FR publisher requires expected SO2F3 prior checkpoint, got '+str(current))
