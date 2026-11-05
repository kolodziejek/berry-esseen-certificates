"""Freeze the final additive review/package closure, never modify old components."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[3]
DEST=ROOT/'work/manuscript_revision_20261029/research/count-transfer-20261105'
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def copy(p,q):
 need(p.is_file()and not p.is_symlink(),'regular input')
 if q.exists():need(q.is_file()and sha(p)==sha(q),'preserve previous bytes');return
 q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);need(sha(p)==sha(q),'copy integrity')
src=ROOT/'work/count_transfer_20261105/later/portable_curvature01'
need(sha(src/'FILES.json')=='ab99d5abb3de42b5bcd72066ad1e295525d21b8c58c47f3a1d3e772f2f8fe3c0','frozen curvature inventory')
mf=json.loads((src/'FILES.json').read_text())['files']
need({str(p.relative_to(src))for p in src.rglob('*')if p.is_file()}==set(mf)|{'FILES.json'},'complete curvature files')
for rel,z in mf.items():
 p=src/rel;need(p.stat().st_size==z['bytes']and sha(p)==z['sha256'],'exact curvature input')
for rel in sorted(set(mf)|{'FILES.json'}):copy(src/rel,DEST/'later-curvature'/rel)
review=ROOT/'work/count_transfer_20261105/review/FILES03.json'
need(sha(review)=='2923d0399a3c3054c44eb6377398b545fcb0476fb960132b0efe02198cfac220','frozen latest independent review')
obj=json.loads(review.read_text())
for rel,z in obj['files'].items():
 p=ROOT/rel;need(p.stat().st_size==z['bytes']and sha(p)==z['sha256'],'review input');copy(p,DEST/'review'/rel)
copy(review,DEST/'review'/review.relative_to(ROOT))
for run in obj['fresh_own_evidence_roots']:
 for p in (ROOT/run).rglob('*'):
  if p.is_file():copy(p,DEST/'review'/p.relative_to(ROOT))
for run in ['later_curvature_package_launch01','later_curvature_portable01','root_stage02']:
 for p in (ROOT/'runs/count_transfer_20261105'/run).rglob('*'):
  if p.is_file():copy(p,DEST/'delivery-evidence'/p.relative_to(ROOT))
copy(Path(__file__),DEST/'delivery-evidence/stage_final.py')
out=ROOT/'runs/count_transfer_20261105/root_stage03';out.mkdir(exist_ok=False)
record=dict(status='ALL_COMPLETED_COMPONENTS_COPIED',files=sum(p.is_file()for p in DEST.rglob('*')),curvature_manifest_sha256=sha(src/'FILES.json'),review_manifest_sha256=sha(review),pending_arithmetic=False)
(out/'RESULT.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
