"""Add immutable completed BN39 package to the publication staging area."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[3]
DEST=ROOT/'work/manuscript_revision_20261029/research/count-transfer-20261105'
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def copy(p,q):
 need(p.is_file()and not p.is_symlink()and not q.exists(),'regular new copy');q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);need(sha(p)==sha(q),'same bytes')
src=ROOT/'work/count_transfer_20261105/portable_bn39_01'
need(sha(src/'FILES.json')=='b715beb899db4dc0bd6e5e2b7f294cfcb0c09e92fc62a38ceac533e5041a6409','frozen full BN39')
mf=json.loads((src/'FILES.json').read_text());names=set()
for z in mf['files']:
 p=src/z['path'];need(z['path']not in names,'unique inventory');names.add(z['path']);need(p.stat().st_size==z['size']and sha(p)==z['sha256'],'source inventory')
need({str(p.relative_to(src))for p in src.rglob('*')if p.is_file()}==names|{'FILES.json'},'complete source package')
for rel in sorted(names|{'FILES.json'}):copy(src/rel,DEST/'n5-bn39'/rel)
for run in ['construct_BN39_portable_verify01','construct_BN39_portable_controls01','construct_BN39_portable_smoke01','construct_BN39_portable_stage01','root_stage01']:
 base=ROOT/'runs/count_transfer_20261105'/run;need(base.is_dir(),'actual completed evidence '+run)
 for p in base.rglob('*'):
  if p.is_file():copy(p,DEST/'delivery-evidence'/p.relative_to(ROOT))
for rel in ['runs/count_transfer_20261105/CONSTRUCTION_DELIVERY02.json','work/count_transfer_20261105/construct/FINAL_STATUS.md']:
 copy(ROOT/rel,DEST/'delivery-evidence'/rel)
copy(Path(__file__),DEST/'delivery-evidence/stage_complete.py')
out=ROOT/'runs/count_transfer_20261105/root_stage02';out.mkdir(exist_ok=False)
record=dict(status='COPIED_COMPLETE_BN39_BYTES',files=len(names)+1,inventory_sha256=sha(src/'FILES.json'),actual_result_sha256='8f8752d58b5b630d0090980667465c7665122d6a5ffd458be252412b3946ee96')
(out/'RESULT.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
