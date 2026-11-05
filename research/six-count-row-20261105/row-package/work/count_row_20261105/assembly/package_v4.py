"""Build additive minimal replay package only after actual three-root acceptance."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
OUT=HERE/'portable_v4_01';RUN=ROOT/'runs/count_row_20261105/analytic_v4_package01'
ACCEPT=ROOT/'runs/count_row_20261105/analytic_complete_row_v4_01'
CAPTURE=ROOT/'runs/count_row_20261105/analytic_complete_row_v4_capture01'

def need(ok,msg):
 if not ok:raise ValueError(msg)
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p):return {'bytes':p.stat().st_size,'sha256':sha(p)}

def main():
 need(__debug__ and not sys.flags.optimize,'unoptimized package check')
 observation=read(CAPTURE/'PROCESS.json');need(type(observation['returncode'])is int and observation['returncode']==0 and observation['source_unchanged']is True,'complete actual outer execution')
 for c in ['stdout','stderr']:need(sha(CAPTURE/(c+'.txt'))==observation[c+'_sha256'],'actual complete stream')
 result=read(ACCEPT/'RESULT.json');packet=json.loads((CAPTURE/'stdout.txt').read_text())
 need(result['status']=='PASS_FRESH_COMPLETE_ORIGINAL_N5_BN38_ROW_COMPARISON_V4'and packet['result_sha256']==sha(ACCEPT/'RESULT.json'),'whole actual result bound in stdout')
 need([r['k']for r in result['completed_roots']]==[1,2,3]and all(r['actual_returncode']==0 for r in result['completed_roots']),'three actual completed roots')
 selected={}
 def add(p):
  p=Path(p);need(p.is_file()and not p.is_symlink()and p.is_relative_to(ROOT),'ordinary workspace file');rel=str(p.relative_to(ROOT));v=pin(p)
  need(rel not in selected or selected[rel]==v,'consistent selected epoch');selected[rel]=v
 def tree(p):
  for f in sorted(p.rglob('*')):
   need(not f.is_symlink(),'no source/evidence symlinks')
   if f.is_file():add(f)
 # Frozen reviewed protocol and bounded controls, without mutable work notes.
 for manifest in [HERE/'FILES.json',ROOT/'work/count_row_20261105/domain/MANIFEST.json']:
  z=read(manifest)
  for rel,v in z['files'].items():need(pin(ROOT/rel)==v,'unchanged reviewed input');add(ROOT/rel)
  add(manifest)
 domain=read(ROOT/'work/count_row_20261105/domain/domain.json')
 for rel,v in domain['source_pins'].items():need(pin(ROOT/rel)==v,'complete original source projection');add(ROOT/rel)
 mr=read(HERE/'READER_SOURCES_V4.json');reader=ROOT/mr['reader_root']
 for name,v in mr['files'].items():need(pin(reader/name)==v,'exact V4 runtime closure');add(reader/name)
 for name in ['model_v3.py','accept_v3.py','native/PROVENANCE.json']:add(reader/name)
 for item in read(reader/'native/PROVENANCE.json'):
  need(sha(ROOT/item['source'])==item['sha256'],'original mathematical source alias');add(ROOT/item['source'])
 selection=ROOT/'runs/count_row_20261105/SELECTED_COMPLETE_V4.json';add(selection)
 for root in read(selection)['roots']:
  need(sha(ROOT/root['object'])==root['object_sha256'],'exact selected candidate');add(ROOT/root['object'])
 tree(ACCEPT);tree(CAPTURE);add(Path(__file__));add(HERE/'CURRENT_HANDOFF.md')
 OUT.mkdir(exist_ok=False)
 for rel,v in sorted(selected.items()):
  f=OUT/rel;f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes((ROOT/rel).read_bytes());need(pin(f)==v,'byte-exact package copy')
 (OUT/'README.md').write_text('''# Complete original n5 BN/panel38 comparison (V4)

This package preserves one complete source-bound **conditional** positive closed-score comparison: n=5, p in[19/50,39/100], rho in[11/10,23/20], the original full acquired noise/beta/support/mean domain, and every licensed threshold. It is not a new all-law n5 proof, the whole Berry–Esseen theorem, or a replacement of original acquisition.

From this directory, use an unoptimized Python with only its standard library:

```sh
python3 -I -B -S replay.py /absolute/path/to/NEW_OUTPUT
```

The output must not exist and must be outside this package. This command verifies the package inventory and runs the unchanged exact V4 reader anew on all three whole source-bound roots. It does not use stored success markers or execute numerical discovery. A complete attempt can take several minutes. All actual per-root exit codes, full streams, input/source/object hashes and result files are preserved in the new output. Nonzero exit or an incomplete tree rejects.

Read work/count_row_20261105/domain/SOUNDNESS.md for the original-domain reduction and work/count_row_20261105/assembly/MATHEMATICAL_REVIEW.md for the Gaussian/cubic-price and V4 mean/sign refinements. The first may retain its earlier no-score-yet historical status; current numerical completion is recorded in COMPLETION.json and the selected actual capture. Their analytic scopes are unchanged. The candidate source and object bytes are preserved with their original workspace hierarchy.

The original acquisition, contact and predecessor assumptions remain external analytic/numerical dependencies. This minimal package includes the exact original row and its source projection/readback records, not all historical acquisition proof objects or an executable acquisition campaign. Native source copies included for provenance are not alternative replay entry points. The supported command is replay.py above. The historical check_assembly_v4.py includes a deliberately optimized startup-rejection probe and must not be rerun; see work/count_row_20261105/assembly/CURRENT_HANDOFF.md. All actual numerical acceptance uses ordinary unoptimized Python.

Historical runs under runs/ contain absolute paths and machine/runtime identities from the executions that actually happened. They are immutable evidence, not portable launchers. The original workspace whole-row run completed all three roots. Packaging performed only a fresh source/preflight relocation and a three-leaf k3 smoke; it did not repeat the full k1/k2 arithmetic again. The public command above does perform all three.

FILES.json inventories every packaged file except itself. Byte hashes establish integrity, not analytic correctness or formal verification. The package has no proof-assistant formalization and does not claim an independent second implementation.
''')
 replay='''"""Verify byte inventory, then execute every actual source-bound V4 root anew."""
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
  p=PurePosixPath(name);need(not p.is_absolute()and '..'not in p.parts and str(p)==name and '\\\\'not in name,'safe inventory name');f=HERE/name
  need(f.stat().st_size==v['bytes']and hashlib.sha256(f.read_bytes()).hexdigest()==v['sha256'],'byte integrity '+name)
 return hashlib.sha256((HERE/'FILES.json').read_bytes()).hexdigest()
if __name__=='__main__':
 need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'usage: ordinary Python replay.py NEW_EXTERNAL_OUTPUT')
 out=Path(sys.argv[1]).resolve();need(not out.exists()and not out.is_relative_to(HERE),'fresh external output');before=verify()
 cmd=[sys.executable,'-I','-B','-S',str(HERE/'work/count_row_20261105/assembly/complete_v4.py'),str(HERE/'runs/count_row_20261105/SELECTED_COMPLETE_V4.json'),str(out)]
 p=subprocess.run(cmd,cwd=HERE);need(verify()==before,'stable package');raise SystemExit(p.returncode)
'''
 (OUT/'replay.py').write_text(replay)
 # Bounded clean-root check; the whole workspace three-root run is above.
 RUN.mkdir(parents=True,exist_ok=False);check_script=OUT/'work/count_row_20261105/assembly/complete_v4.py'
 code="import importlib.util,json; from pathlib import Path; p=Path("+repr(str(check_script))+"); s=importlib.util.spec_from_file_location('fresh_assembly',p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); _,_,j=m.preflight(m.read(m.ROOT/'runs/count_row_20261105/SELECTED_COMPLETE_V4.json')); assert [v['k'] for v in j]==[1,2,3]; print('PASS_RELOCATED_COMPLETE_ROOT_SOURCE_PREFLIGHT')"
 pre=subprocess.run([sys.executable,'-I','-B','-S','-c',code],capture_output=True);(RUN/'preflight.stdout').write_bytes(pre.stdout);(RUN/'preflight.stderr').write_bytes(pre.stderr)
 need(pre.returncode==0 and not pre.stderr,'relocated full source/header preflight')
 k3=next(x for x in read(selection)['roots']if x['k']==3);candidate=OUT/k3['object'];acceptor=OUT/mr['reader_root']/'accept_v4.py'
 cmd=[sys.executable,'-I','-B','-S',str(acceptor),str(candidate),str(RUN/'k3-smoke'),'--k','3','--p','.38','.39','--u','-0.5','0.072258117249','--noise','0','0.30748']
 before={rel:pin(OUT/rel)for rel in selected};t=time.monotonic();smoke=subprocess.run(cmd,capture_output=True);elapsed=time.monotonic()-t
 (RUN/'stdout.txt').write_bytes(smoke.stdout);(RUN/'stderr.txt').write_bytes(smoke.stderr)
 obs={'command':cmd,'returncode':smoke.returncode,'seconds':elapsed,'preflight_returncode':pre.returncode,'stdout_sha256':hashlib.sha256(smoke.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(smoke.stderr).hexdigest(),'source_unchanged':before=={rel:pin(OUT/rel)for rel in selected},'scope':'Relocated complete-source/root preflight plus actual k3 three-leaf smoke only; no extra full-row replay.'}
 (RUN/'PROCESS.json').write_text(json.dumps(obs,indent=2)+'\n');need(smoke.returncode==0 and not smoke.stderr and obs['source_unchanged'],'actual clean-root k3 smoke')
 sr=read(RUN/'k3-smoke/RESULT.json');need(sr['status']=='PASS_EXACT_COMPLETE_CLOSED_RECTANGLE'and sr['k']==3 and len(sr['leaves'])==3,'exact actual smoke scope')
 for f in RUN.rglob('*'):
  if f.is_file():q=OUT/f.relative_to(ROOT);q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(f.read_bytes())
 completion={'status':'PRESERVED_COMPLETE_CONDITIONAL_ROW_V4_WITH_RELOCATED_K3_SMOKE','mathematical_scope':result['mathematical_status'],'original_full_row_result':str((ACCEPT/'RESULT.json').relative_to(ROOT)),'original_full_row_result_sha256':sha(ACCEPT/'RESULT.json'),'original_outer_actual_returncode':0,'completed_roots':[1,2,3],'total_leaves':result['total_leaves'],'total_rays':result['total_rays'],'total_tensor_coefficients':result['total_tensor_coefficients'],'relocation_scope':obs['scope'],'relocated_smoke_result_sha256':sha(RUN/'k3-smoke/RESULT.json'),'original_acquisition_rerun':False,'full_n5_claimed':False}
 (OUT/'COMPLETION.json').write_text(json.dumps(completion,indent=2)+'\n')
 files={str(f.relative_to(OUT)):pin(f)for f in sorted(OUT.rglob('*'))if f.is_file()}
 (OUT/'FILES.json').write_text(json.dumps({'scope':'Minimal complete-row replay closure and preserved actual evidence, with explicit original acquisition boundary.','files':files},indent=2)+'\n')
 need(all(pin(OUT/rel)==v for rel,v in files.items()),'whole package byte readback')
 final={'status':'PASS_COMPLETE_V4_PACKAGE_BYTE_CLOSURE_AND_BOUNDED_RELOCATION','package':str(OUT.relative_to(ROOT)),'manifest_sha256':sha(OUT/'FILES.json'),'files':len(files)+1,'logical_bytes':sum(v['bytes']for v in files.values())+(OUT/'FILES.json').stat().st_size,'original_complete_result_sha256':sha(ACCEPT/'RESULT.json'),'relocated_k3_result_sha256':sha(RUN/'k3-smoke/RESULT.json'),'full_portable_replay_performed':False,'builder_sha256':sha(Path(__file__))}
 (RUN/'PACKAGE_RESULT.json').write_text(json.dumps(final,indent=2)+'\n');print(json.dumps(final))
if __name__=='__main__':main()
