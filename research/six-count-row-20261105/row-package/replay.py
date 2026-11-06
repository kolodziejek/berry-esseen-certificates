"""Verify byte inventory, then execute every actual source-bound V4 root anew."""
from pathlib import Path,PurePosixPath
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
def need(x,m):
 if not x:raise ValueError(m)
def unique(xs):
 d={}
 for k,v in xs:need(k not in d,'duplicate key');d[k]=v
 return d
def verify():
 m=json.loads((HERE/'FILES.json').read_text(),object_pairs_hook=unique);expected=set(m['files'])|{'FILES.json'};actual=set()
 for p in HERE.rglob('*'):
  need(not p.is_symlink(),'no symlink in package')
  if p.is_file():actual.add(str(p.relative_to(HERE)))
 need(actual==expected,'complete package inventory')
 for name,v in m['files'].items():
  p=PurePosixPath(name);need(not p.is_absolute()and '..'not in p.parts and str(p)==name and '\\'not in name,'safe inventory name');f=HERE/name
  need(f.stat().st_size==v['bytes']and hashlib.sha256(f.read_bytes()).hexdigest()==v['sha256'],'byte integrity '+name)
 return hashlib.sha256((HERE/'FILES.json').read_bytes()).hexdigest()
if __name__=='__main__':
 need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'usage: ordinary Python replay.py NEW_EXTERNAL_OUTPUT')
 out=Path(sys.argv[1]).resolve();need(not out.exists()and not out.is_relative_to(HERE),'fresh external output');before=verify()
 cmd=[sys.executable,'-I','-B','-S',str(HERE/'work/count_row_20261105/assembly/complete_v4.py'),str(HERE/'runs/count_row_20261105/SELECTED_COMPLETE_V4.json'),str(out)]
 p=subprocess.run(cmd,cwd=HERE);need(verify()==before,'stable package');raise SystemExit(p.returncode)
