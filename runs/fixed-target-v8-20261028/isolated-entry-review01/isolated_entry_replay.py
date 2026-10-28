#!/usr/bin/env python3
"""Isolated reproduction of one frozen v7 entry, preserving its source bytes.

This is not a general proof acceptor and does not reprove analytic premises.
Only the fixed acceptor, fixed proof and its literal source manifests are copied
into a new directory. A trusted isolated Python/stdlib executes that clean copy.
"""
from pathlib import Path,PurePosixPath
from hashlib import sha256
import argparse,ast,json,subprocess,sys,tempfile,time
ROOT=Path(__file__).resolve().parents[3]
ACCEPT='mathematics/fixed-target-v7/2026-10-27/accept_entry.py'
PROOF='mathematics/fixed-target-v7/2026-10-27/entry-proof.json'
ACCEPT_SHA='fe8197d6943c4decb7421bd1c162d7ec24045fdb3ea1215356249b4be620d69d'
PROOF_SHA='61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae'
BOOTSTRAP="import runpy,sys; from pathlib import Path; p=Path(sys.argv[1]); q=sys.argv[2]; sys.path.insert(0,str(p.parent)); sys.argv=[str(p),q]; runpy.run_path(str(p),run_name='__main__')"
def need(ok,why):
 if not ok:raise ValueError(why)
def unique(pairs):
 out={}
 for k,v in pairs:need(k not in out,'duplicate JSON key');out[k]=v
 return out
def manifest(accept_bytes):
 need(sha256(accept_bytes).hexdigest()==ACCEPT_SHA,'fixed reviewed acceptor before AST parse')
 tree=ast.parse(accept_bytes);found={}
 for n in tree.body:
  if isinstance(n,ast.Assign):
   for t in n.targets:
    if isinstance(t,ast.Name)and t.id in ('PINS','PRELOAD_PINS'):
     need(t.id not in found,'unique literal manifest');found[t.id]=ast.literal_eval(n.value)
 need(set(found)=={'PINS','PRELOAD_PINS'},'both source manifests')
 pins={ACCEPT:ACCEPT_SHA,PROOF:PROOF_SHA}
 for kind,d in found.items():
  need(type(d)is dict,'literal source map')
  for p,h in d.items():
   need(type(p)is str and type(h)is str and len(h)==64 and all(c in '0123456789abcdef'for c in h),'source pin shape')
   rel=str(PurePosixPath(ACCEPT).parent/p)if kind=='PINS'else p
   path=PurePosixPath(rel);need(not path.is_absolute()and '..'not in path.parts and str(path)==rel,'relative source path')
   need(rel not in pins,'distinct source paths');pins[rel]=h
 need(len(pins)==13,'fixed complete allowlist')
 return pins
def validate(blobs,pins):
 need(type(blobs)is dict and set(blobs)==set(pins),'exact copied allowlist')
 for p,h in pins.items():need(type(blobs[p])is bytes and sha256(blobs[p]).hexdigest()==h,'pinned copied bytes '+p)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--source-root',type=Path,default=ROOT);ap.add_argument('--output-dir',type=Path,required=True);a=ap.parse_args()
 need(__debug__ and not sys.flags.optimize,'unoptimized wrapper')
 output=a.output_dir.resolve();need(not output.exists(),'new distinct evidence directory');output.mkdir(parents=True)
 accept_bytes=(a.source_root/ACCEPT).read_bytes();pins=manifest(accept_bytes)
 blobs={p:accept_bytes if p==ACCEPT else(a.source_root/p).read_bytes()for p in pins};validate(blobs,pins)
 controls=[]
 def reject(name,fn):
  try:fn()
  except (ValueError,TypeError):controls.append(name)
  else:raise ValueError('wrapper control accepted '+name)
 bad=dict(blobs);bad.pop(PROOF);reject('missing fixed proof',lambda:validate(bad,pins))
 bad=dict(blobs);bad[PROOF]+=b' ';reject('altered fixed proof bytes',lambda:validate(bad,pins))
 bad=dict(blobs);bad[ACCEPT]+=b'\n';reject('altered acceptor before parsing',lambda:manifest(bad[ACCEPT]))
 bad=dict(blobs);bad['unlisted.py']=b'raise RuntimeError()';reject('unlisted executable in copied tree',lambda:validate(bad,pins))
 bad=dict(blobs);key=next(p for p in pins if p.endswith('/kernel.py'));bad[key]+=b'\n';reject('mutated inherited kernel',lambda:validate(bad,pins))
 t=time.monotonic()
 with tempfile.TemporaryDirectory(prefix='fixed-entry-source-')as td:
  base=Path(td);tree=base/'tree';cache=base/'cache';tree.mkdir();cache.mkdir()
  for p,b in blobs.items():
   target=tree/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(b)
  need({str(p.relative_to(tree))for p in tree.rglob('*')if p.is_file()}==set(pins),'no extra copied files')
  validate({p:(tree/p).read_bytes()for p in pins},pins)
  cmd=[sys.executable,'-I','-B','-X','pycache_prefix='+str(cache),'-c',BOOTSTRAP,str(tree/ACCEPT),str(tree/PROOF)]
  result=subprocess.run(cmd,cwd=tree,capture_output=True,timeout=180)
  (output/'stdout.json').write_bytes(result.stdout);(output/'stderr.txt').write_bytes(result.stderr)
  need(not any(cache.rglob('*')),'fresh bytecode prefix stays empty')
  need({str(p.relative_to(tree))for p in tree.rglob('*')if p.is_file()}==set(pins),'replay writes no project files')
  validate({p:(tree/p).read_bytes()for p in pins},pins)
 receipt={'command':['python3','-I','-B','-X','pycache_prefix=<fresh-empty-directory>','-c',BOOTSTRAP,'<copied-root>/'+ACCEPT,'<copied-root>/'+PROOF],
  'returncode':result.returncode,'elapsed_seconds':time.monotonic()-t,'python':sys.version,'optimization':sys.flags.optimize,'wrapper_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
  'source_pins':pins,'stdout_sha256':sha256(result.stdout).hexdigest(),'stderr_sha256':sha256(result.stderr).hexdigest(),'copied_file_count':len(pins),'empty_cache_after_replay':True,'copied_source_bytes_unchanged':True}
 (output/'receipt.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
 need(result.returncode==0,'isolated v7 replay returns success')
 out=json.loads(result.stdout,object_pairs_hook=unique)
 need(out['status']=='PASS_INITIAL42_FIXED_TARGET_COARSE_V7'and out['proof_sha256']==PROOF_SHA,'fixed entry outcome')
 s=out['summary'];need(type(s['signed_cells'])is int and s['signed_cells']==11264,'all four signed-stage calls')
 need(s['probability_panels']==100 and s['nonempty_probability_panels']==30 and s['remaining_rho_cells']==14,'complete final probability census')
 need(type(out['rejected_controls'])is list and len(out['rejected_controls'])==len(set(out['rejected_controls']))==19,'all inherited rejecting controls')
 summary={'status':'PASS_ISOLATED_REPRODUCTION_FIXED_ENTRY_V7','mathematical_status':'Same conditional fixed-target theorem as the frozen v7 acceptor; no new analytic or finite-base acceptance.',
 'execution_status':'Fresh allowlist-copy isolated replay of the two-quadratic ancestor and all four selected signed passes.',
 'proof_sha256':PROOF_SHA,'signed_cells':11264,'probability_panels':100,'nonempty_probability_panels':30,'inherited_rejected_controls':19,'wrapper_rejected_controls':controls,'trusted_stack':'Python interpreter and standard library, OS/filesystem, SHA256; no concurrent hostile modification of the fresh private directory.'}
 (output/'summary.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n');print(json.dumps(summary,sort_keys=True))
if __name__=='__main__':main()
