"""Copy the supplied external publication exactly; never execute or edit it."""
from pathlib import Path,PurePosixPath
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[3]
SRC=Path('/Users/bkolodziejek/Documents/BerryEsseen/research/count-transfer-20261105')
DST=Path(__file__).resolve().parent/'snapshot/research/count-transfer-20261105'
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unique(items):
 d={}
 for k,v in items:need(k not in d,'duplicate key');d[k]=v
 return d
mf=SRC/'FILES.json';pin=sha(mf)
need(pin=='9c7cf55a7611c51c9a264c5c428e6a69010b60038833c06db60ed14516038b0c','external published inventory')
records=json.loads(mf.read_text(),object_pairs_hook=unique)['files']
actual=set()
for p in SRC.rglob('*'):
 need(not p.is_symlink(),'ordinary external files')
 if p.is_file():actual.add(str(p.relative_to(SRC)))
need(actual==set(records)|{'FILES.json'},'complete external file set')
for rel,z in records.items():
 r=PurePosixPath(rel);need(not r.is_absolute()and '..'not in r.parts and str(r)==rel and '\\'not in rel,'safe relative path')
 p=SRC/rel;need(p.stat().st_size==z['bytes']and sha(p)==z['sha256'],'external inventory '+rel)
DST.mkdir(parents=True,exist_ok=False)
for rel in sorted(actual):
 p=SRC/rel;q=DST/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);need(sha(p)==sha(q),'byte identical copy')
need(sha(mf)==pin and all(sha(SRC/p)==z['sha256']for p,z in records.items()),'external source stable')
run=ROOT/'runs/argon_audit_20261105/snapshot01';run.mkdir(parents=True,exist_ok=False)
result=dict(status='PASS_EXTERNAL_BYTE_SNAPSHOT',source=str(SRC),destination=str(DST),files=len(actual),inventory_sha256=pin,external_source_unchanged=True,mathematical_verification=False)
(run/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
