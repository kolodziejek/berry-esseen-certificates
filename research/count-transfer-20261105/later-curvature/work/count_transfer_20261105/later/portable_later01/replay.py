from pathlib import Path,PurePosixPath
import hashlib,json,subprocess,sys,time
HERE=Path(__file__).resolve().parent
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unique(items):
 d={}
 for k,v in items:need(k not in d,'duplicate key');d[k]=v
 return d
def verify():
 obj=json.loads((HERE/'FILES.json').read_text(),object_pairs_hook=unique);actual=set()
 for p in HERE.rglob('*'):
  need(not p.is_symlink(),'ordinary package files')
  if p.is_file():actual.add(str(p.relative_to(HERE)))
 need(actual==set(obj['files'])|{'FILES.json'},'complete byte inventory')
 for rel,r in obj['files'].items():
  q=PurePosixPath(rel);need(not q.is_absolute()and '..'not in q.parts and str(q)==rel and '\\'not in rel,'safe inventory path')
  p=HERE/rel;need(p.stat().st_size==r['bytes']and sha(p)==r['sha256'],'exact selected byte '+rel)
 return sha(HERE/'FILES.json')
def main():
 need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'ordinary Python replay.py NEW_OUTPUT')
 out=Path(sys.argv[1]).resolve();need(not out.exists()and not out.is_relative_to(HERE),'fresh external output');before=verify();out.mkdir(parents=True)
 reader=HERE/'work/count_transfer_20261105/later/gaussian_taylor01/check_wide_phase.py';cmd=[sys.executable,'-I','-B','-S',str(reader),str(out/'accepted')];tt=time.monotonic();p=subprocess.run(cmd,capture_output=True)
 (out/'stdout.txt').write_bytes(p.stdout);(out/'stderr.txt').write_bytes(p.stderr)
 r={'command':cmd,'returncode':p.returncode,'seconds':time.monotonic()-tt,'stdout_sha256':sha(out/'stdout.txt'),'stderr_sha256':sha(out/'stderr.txt'),'manifest_sha256':before,'package_unchanged':verify()==before,'scope':'The bounded selected sharp39 wider-phase rectangle only.'};(out/'PROCESS.json').write_text(json.dumps(r,indent=2)+'\n');need(r['package_unchanged'],'stable package');print(json.dumps(r));raise SystemExit(p.returncode)
if __name__=='__main__':main()
