"""Verify bn-band-20261106 publication bytes only; this is not certificate acceptance."""
from pathlib import Path,PurePosixPath
import hashlib,json,sys
ROOT=Path(__file__).resolve().parent
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unique(items):
 d={}
 for k,v in items:need(k not in d,'duplicate JSON key');d[k]=v
 return d
def main():
 need(__debug__ and not sys.flags.optimize and len(sys.argv)==1,'ordinary Python; no arguments')
 manifest=ROOT/'FILES.json';obj=json.loads(manifest.read_text(),object_pairs_hook=unique)
 need(obj['schema']=='BN_BAND_PUBLICATION_V1','fixed schema');files=obj['files'];actual=set()
 for p in ROOT.rglob('*'):
  need(not p.is_symlink(),'ordinary files only')
  if p.is_file():actual.add(str(p.relative_to(ROOT)))
 need(actual==set(files)|{'FILES.json'},'complete file census')
 for rel,z in files.items():
  p=PurePosixPath(rel);need(not p.is_absolute()and '..'not in p.parts and str(p)==rel and '\\'not in rel,'safe relative path')
  f=ROOT/rel;need(f.stat().st_size==z['bytes']and sha(f)==z['sha256'],'exact bytes: '+rel)
 print(json.dumps(dict(status='PASS_BN_BAND_PUBLICATION_BYTE_INVENTORY',files=len(files)+1,manifest_sha256=sha(manifest),mathematical_verification=False)))
if __name__=='__main__':main()
