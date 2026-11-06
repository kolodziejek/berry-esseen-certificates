"""Create-only portable later-index source/evidence selection and bounded replay."""
from pathlib import Path
import hashlib,json,subprocess,sys,time
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;ROOT=BASE.parents[2]
OUT=BASE/'portable_later01';RUN=ROOT/'runs/count_transfer_20261105/later_portable_replay01'
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def pin(p):return {'bytes':p.stat().st_size,'sha256':sha(p)}
def main():
 need(__debug__ and not sys.flags.optimize,'ordinary Python');selected={}
 for name in ['FILES01.json','FILES02.json','FILES03.json']:
  path=BASE/name;v=json.loads(path.read_text())
  for rel,rec in v['files'].items():
   p=ROOT/rel;need(p.is_file()and not p.is_symlink()and pin(p)==rec,'exact stopped selected epoch '+rel)
   need(rel not in selected or selected[rel]==rec,'consistent source identity');selected[rel]=rec
  selected[str(path.relative_to(ROOT))]=pin(path)
 OUT.mkdir(exist_ok=False)
 for rel,rec in sorted(selected.items()):
  p=OUT/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((ROOT/rel).read_bytes());need(pin(p)==rec,'byte exact package')
 reader=OUT/'work/count_transfer_20261105/later/gaussian_taylor01/check_wide_phase.py'
 RUN.mkdir(exist_ok=False);cmd=[sys.executable,'-I','-B','-S',str(reader),str(RUN/'accepted')];tt=time.monotonic()
 before={rel:pin(OUT/rel)for rel in selected};proc=subprocess.run(cmd,capture_output=True)
 (RUN/'stdout.txt').write_bytes(proc.stdout);(RUN/'stderr.txt').write_bytes(proc.stderr)
 obs={'command':cmd,'returncode':proc.returncode,'seconds':time.monotonic()-tt,'stdout_sha256':sha(RUN/'stdout.txt'),'stderr_sha256':sha(RUN/'stderr.txt'),'selected_source_unchanged':before=={rel:pin(OUT/rel)for rel in selected},'scope':'Full exact strongest wider-phase bounded rectangle from the relocated package, not a whole original row or acquisition campaign.'}
 (RUN/'PROCESS.json').write_text(json.dumps(obs,indent=2)+'\n');need(proc.returncode==0 and not proc.stderr and obs['selected_source_unchanged'],'actual relocated exact replay')
 result=json.loads((RUN/'accepted/RESULT.json').read_text());need(result['p']==['77/200','39/100']and result['u']==['-1/100','1/100']and result['score_coefficients']==5940 and result['psd_coefficients']==1503,'exact selected scope')
 for p in sorted(RUN.rglob('*')):
  if p.is_file():f=OUT/p.relative_to(ROOT);f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(p.read_bytes())
 (OUT/'README.md').write_text('''# Bounded later-index conditional-count progress

This package contains a general n+1 quartic moment criterion and exact tests on original acquired n6 and sharp39 inputs. The strongest wider-phase result is n39,k15,p∈[.385,.39],u∈[-.01,.01],lambda∈[0,.185], under the original same-law source-row assumptions. It is not the full original row, a new sharp39 theorem, or a replacement of original acquisition. A separate accepted rectangle p∈[.3847,.39],u∈[-.001,.001] is also preserved; do not infer their larger bounding rectangle.

The root entry point runs the entire strongest wider-phase check with standard-library-only, unoptimized Python and a fresh external output:

```sh
python3 -I -B -S replay.py /absolute/NEW_OUTPUT
```

It verifies every packaged byte, runs the unchanged exact source-bound reader, records the actual command/exit/stdout/stderr and preserves all generated results. It does not execute discovery or accept stored success markers. The check takes about five seconds in the recorded environment, CPython3.12.12. No SciPy/NumPy dependency is needed for acceptance.

Proofs are under work/count_transfer_20261105/later/: GENERAL_N_SOUNDNESS.md, TANGENT_PRICE.md, CONTINUOUS_RECTANGLE.md and gaussian_taylor01/{SOUNDNESS.md,WIDE_PHASE.md}. CURRENT_READERS.md gives the smaller earlier exact entry points. The generic mathematical rule retains one common conditional marginal across every count and the cubic price. The proof separately establishes global quartic domination, moment reduction, variance convexity, Gaussian lower polynomials and closed domain coverage.

Original source-selected contracts and their metadata are in work/count_transfer_20261105/later/selected/. This is a minimal mathematical replay closure, not the complete original acquisition archive. Domain projections identify the original acquisition/parent records; their historical flags and paths remain unchanged. Historical projection/audit drivers may refer to original workspace-only captures and are preserved as provenance, not offered as portable acquisition replay commands. The public command above is the supported final entry point.

All raw accepted/failing diagnostic evidence is preserved under runs/. The exact fixed-price normalization obstruction and coarse Gaussian-endpoint obstruction remain true at their stated scopes; they are not counterexamples to the theorem. The later tangent/Taylor improvements are distinct source epochs. Original full finite-base and acquisition campaigns were not rerun. Packaging did perform a complete relocated replay of the selected bounded wider-phase rectangle, including 80 global rays, 5,940 score coefficients and 1,503 PSD coefficients.

FILES.json inventories all files except itself. Hashes establish byte integrity, not analytic correctness or a formal proof. No whole-row, all-index, formalization or external-referee claim is made.
''')
 (OUT/'replay.py').write_text('''from pathlib import Path,PurePosixPath
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
  q=PurePosixPath(rel);need(not q.is_absolute()and '..'not in q.parts and str(q)==rel and '\\\\'not in rel,'safe inventory path')
  p=HERE/rel;need(p.stat().st_size==r['bytes']and sha(p)==r['sha256'],'exact selected byte '+rel)
 return sha(HERE/'FILES.json')
def main():
 need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'ordinary Python replay.py NEW_OUTPUT')
 out=Path(sys.argv[1]).resolve();need(not out.exists()and not out.is_relative_to(HERE),'fresh external output');before=verify();out.mkdir(parents=True)
 reader=HERE/'work/count_transfer_20261105/later/gaussian_taylor01/check_wide_phase.py';cmd=[sys.executable,'-I','-B','-S',str(reader),str(out/'accepted')];tt=time.monotonic();p=subprocess.run(cmd,capture_output=True)
 (out/'stdout.txt').write_bytes(p.stdout);(out/'stderr.txt').write_bytes(p.stderr)
 r={'command':cmd,'returncode':p.returncode,'seconds':time.monotonic()-tt,'stdout_sha256':sha(out/'stdout.txt'),'stderr_sha256':sha(out/'stderr.txt'),'manifest_sha256':before,'package_unchanged':verify()==before,'scope':'The bounded selected sharp39 wider-phase rectangle only.'};(out/'PROCESS.json').write_text(json.dumps(r,indent=2)+'\\n');need(r['package_unchanged'],'stable package');print(json.dumps(r));raise SystemExit(p.returncode)
if __name__=='__main__':main()
''')
 completion={'status':'PRESERVED_BOUNDED_LATER_RESULTS_WITH_FULL_RELOCATED_WIDE_RECTANGLE_PASS','original_wide_result':'runs/count_transfer_20261105/later_gaussian_wide01/checked/RESULT.json','relocated_wide_result':str((RUN/'accepted/RESULT.json').relative_to(ROOT)),'relocated_result_sha256':sha(RUN/'accepted/RESULT.json'),'actual_returncode':0,'full_original_row':False,'original_acquisitions_replayed':False}
 (OUT/'COMPLETION.json').write_text(json.dumps(completion,indent=2)+'\n')
 files={str(p.relative_to(OUT)):pin(p)for p in sorted(OUT.rglob('*'))if p.is_file()};(OUT/'FILES.json').write_text(json.dumps({'files':files},indent=2)+'\n')
 need(all(pin(OUT/rel)==v for rel,v in files.items()),'complete package readback')
 # Exercise the published inventory entry point without repeating arithmetic.
 import runpy
 need(runpy.run_path(str(OUT/'replay.py'))['verify']()==sha(OUT/'FILES.json'),'public inventory entry')
 final={'status':'PASS_EXACT_PORTABLE_LATER_PACKAGE','package':str(OUT.relative_to(ROOT)),'manifest_sha256':sha(OUT/'FILES.json'),'files':len(files)+1,'bytes':sum(x['bytes']for x in files.values())+(OUT/'FILES.json').stat().st_size,'relocated_result_sha256':sha(RUN/'accepted/RESULT.json'),'full_original_row':False}
 (RUN/'PACKAGE_RESULT.json').write_text(json.dumps(final,indent=2)+'\n');print(json.dumps(final))
if __name__=='__main__':main()
