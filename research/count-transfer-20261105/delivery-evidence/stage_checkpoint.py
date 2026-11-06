"""Create-only byte-preserving publication staging for completed components."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[3]
DEST=ROOT/'work/manuscript_revision_20261029/research/count-transfer-20261105'
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def entries(p):
 obj=json.loads(p.read_text())['files']
 if type(obj)is list:return {z['path']:{'bytes':z['size'],'sha256':z['sha256']}for z in obj}
 return obj
def verify(root,records,extra):
 actual=set()
 for p in root.rglob('*'):
  need(not p.is_symlink(),'no symlinks')
  if p.is_file():actual.add(str(p.relative_to(root)))
 need(actual==set(records)|extra,'complete package census')
 for rel,v in records.items():
  p=root/rel;need(p.stat().st_size==v['bytes']and sha(p)==v['sha256'],'pinned package '+rel)
def copy(src,dst):
 need(src.is_file()and not src.is_symlink(),'regular source');dst.parent.mkdir(parents=True,exist_ok=True);need(not dst.exists(),'no overwrite')
 shutil.copyfile(src,dst);need(sha(src)==sha(dst),'byte-identical copy')
DEST.mkdir(exist_ok=False)
components=[('work/count_transfer_20261105/portable01','n5-two-rows','894d520661d986b975bb6bfdb04cfe03f6144069fd12f12d894b53f2f67bcfaf'),('work/count_transfer_20261105/later/portable_later01','later-index','2b0a4878276ff4c6a133c754ae50c4b91280f1f4799273a6f36eec70e136990d')]
for rel,name,pin in components:
 src=ROOT/rel;need(sha(src/'FILES.json')==pin,'frozen component inventory');records=entries(src/'FILES.json');verify(src,records,{'FILES.json'})
 for path in sorted(set(records)|{'FILES.json'}):copy(src/path,DEST/name/path)
 verify(DEST/name,records,{'FILES.json'})
review=ROOT/'work/count_transfer_20261105/review/FILES02.json'
need(sha(review)=='40da890dd0209ff8ecb05ec49355c321b7873d71f697408a8bb7a9f10792e799','frozen independent review')
obj=json.loads(review.read_text())
for rel,v in obj['files'].items():
 src=ROOT/rel;need(sha(src)==v['sha256']and src.stat().st_size==v['bytes'],'review source');copy(src,DEST/'review'/rel)
copy(review,DEST/'review/work/count_transfer_20261105/review/FILES02.json')
for run in obj['fresh_own_evidence_roots']:
 for src in (ROOT/run).rglob('*'):
  if src.is_file():copy(src,DEST/'review'/src.relative_to(ROOT))
copy(ROOT/'work/count_row_20261105/review/capture.py',DEST/'review/work/count_row_20261105/review/capture.py')
copy(ROOT/'work/count_transfer_20261105/root/gaussian_endpoint.tex',DEST/'gaussian_endpoint.tex')
copy(ROOT/'runs/count_transfer_20261105/root_build04/build/gaussian_endpoint.pdf',DEST/'gaussian_endpoint.pdf')
for run in ['root_build04','root_visual04','construct_portable_verify01','construct_portable_controls01','construct_portable_smoke01','later_portable_replay01']:
 for src in (ROOT/'runs/count_transfer_20261105'/run).rglob('*'):
  if not src.is_file()or src.suffix in('.png','.gz','.aux','.fls','.fdb_latexmk','.pdf'):continue
  copy(src,DEST/'delivery-evidence'/src.relative_to(ROOT))
copy(Path(__file__),DEST/'delivery-evidence/stage_checkpoint.py')
files={str(p.relative_to(DEST)):{'bytes':p.stat().st_size,'sha256':sha(p)}for p in sorted(DEST.rglob('*'))if p.is_file()}
out=ROOT/'runs/count_transfer_20261105/root_stage01';out.mkdir(exist_ok=False)
result={'status':'COPIED_COMPLETED_COMPONENTS','destination':str(DEST),'files':len(files),'bytes':sum(v['bytes']for v in files.values()),'component_manifests':{name:pin for _,name,pin in components},'claim':'Two complete n5 rows and bounded n39 rectangle; BN39 full mixed replay still separate.'}
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
