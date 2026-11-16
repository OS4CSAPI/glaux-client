#!/usr/bin/env python3
"""Complete source-qualified SO-2F-1 in the existing master and 26-sheet workbook.
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


if __name__=='__main__':
    need(len(sys.argv)==2 and sys.argv[1] in ('--apply','--verify'),'use --apply or --verify')
    current=load(MASTER)['currentEvidenceCheckpoint']
    if sys.argv[1]=='--verify':
        if current==CP3:verify3()
        elif current==CP2:packet2_verify()
        else:verify()
    elif current==CP3:
        verify3();print('Already saved: no duplicate SO2F3 mutation.')
    elif current==CP2:
        apply3()
    else:need(False,'SO2F3 publisher refuses unexpected checkpoint '+str(current))
