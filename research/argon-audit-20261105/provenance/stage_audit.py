"""Publish only completed audit evidence; preserve the supplied proof package."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[3]
DEST=ROOT/'work/manuscript_revision_20261029/research/argon-audit-20261105'
WORK=ROOT/'work/argon_audit_20261105';RUN=ROOT/'runs/argon_audit_20261105'
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def copy(p,q):
 need(p.is_file()and not p.is_symlink()and not q.exists(),'regular new output');q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);need(sha(p)==sha(q),'identical audit bytes')
review=RUN/'review_corrected01';result=read(review/'checked/RESULT.json');process=read(review/'PROCESS.json')
need(process['returncode']==0,'actual corrected review process')
need(result['status']=='PASS_CORRECTED_INDEPENDENT_ALL_TAYLOR_POLYNOMIAL_AUDIT','corrected review complete')
c=result['counts'];need((c['rows'],c['roots'],c['leaves'],c['priced_leaves'],c['psd'],c['score'],c['dual'])==(7,20,63,1,1953,121500,486000),'complete selected source audit')
need(result['source_sha256_before']==result['source_sha256_after'],'stable review inputs')
for rel,name in [('analytic/REVIEW.md','ANALYTIC_REVIEW.md'),('analytic/SOURCE_PINS.json','analytic-source-pins.json'),('coverage/REVIEW.md','COVERAGE_REVIEW.md'),('coverage/audit_data.py','coverage/audit_data.py'),('coverage/FILES.json','coverage/FILES.json'),('review/AUDIT.md','INDEPENDENT_REVIEW.md'),('review/ORIGINAL_REVIEW_FINDINGS.md','ORIGINAL_REVIEW_FINDINGS.md'),('review/STATIC_SOURCE_AUDIT.json','STATIC_SOURCE_AUDIT.json')]:copy(WORK/rel,DEST/name)
for name in ['check_all_taylor_v2.py','independent_polys.py','SOUNDNESS.md','README.md']:
 copy(WORK/'review/corrected01'/name,DEST/'corrected01'/name)
copy(WORK/'review/FILES.json',DEST/'review-files.json')
copy(WORK/'review/ZERO_PRICE_COROLLARY.json',DEST/'ZERO_PRICE_COROLLARY.json')
for name in ['snapshot01','replay01','controls01','coverage_data01','review_corrected01']:
 for p in sorted((RUN/name).rglob('*')):
  if p.is_file():copy(p,DEST/'evidence'/name/p.relative_to(RUN/name))
copy(WORK/'root/snapshot.py',DEST/'provenance/snapshot.py')
copy(Path(__file__),DEST/'provenance/stage_audit.py')
native=read(RUN/'replay01/accepted/RESULT.json');np=read(RUN/'replay01/capture/PROCESS.json');control=read(RUN/'controls01/capture/PROCESS.json')
need(np['returncode']==0 and np['inputs_unchanged']and control['returncode']==0 and control['inputs_unchanged'],'fresh native arithmetic and controls')
record=dict(status='AUDITED_ARGON_CONTINUATION',external_commit='6ebda7f5f54c8a2a56391ade39db982f537f02e4',mathematical_status='Locally derived and checked original acquired positive closed-score implications; no analytic or selected-coverage defect found.',execution_status='Fresh native seven-row replay, supplied43controls, independent295original/20root/63leaf coverage, corrected polynomial audit PASS.',counts=c,native_result_sha256=sha(RUN/'replay01/accepted/RESULT.json'),native_seconds=np['seconds'],corrected_audit_result_sha256=sha(review/'checked/RESULT.json'),corrected_audit_seconds=process['seconds'],coverage_result_sha256=sha(RUN/'coverage_data01/checked/RESULT.json'),priced_leaf_checks=result['priced_leaf_checks'],isolated_curvature_control=result['isolated_curvature_control'],source_package_manifest_sha256='b950e3f7457f66305d6626badaed26886cfb37b72bf8aa50575ac8aafdc3de27',external_publication_manifest_sha256='9c7cf55a7611c51c9a264c5c428e6a69010b60038833c06db60ed14516038b0c',manuscript_unchanged=True,manuscript_pages=86,all_295_rows_proved=False,original_acquisition_replayed=False,external_originals_changed=False)
(DEST/'RESULTS.json').write_text(json.dumps(record,indent=2)+'\n')
files={str(p.relative_to(DEST)):{'bytes':p.stat().st_size,'sha256':sha(p)}for p in sorted(DEST.rglob('*'))if p.is_file()}
need(not(DEST/'FILES.json').exists(),'new final inventory');(DEST/'FILES.json').write_text(json.dumps(dict(schema='ARGON_AUDIT_PUBLICATION_V1',files=files),indent=2)+'\n')
out=RUN/'publication_stage01';out.mkdir(exist_ok=False);r=dict(status='STAGED_AUDIT',files=len(files)+1,manifest_sha256=sha(DEST/'FILES.json'),bytes=sum(z['bytes']for z in files.values())+(DEST/'FILES.json').stat().st_size)
(out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
