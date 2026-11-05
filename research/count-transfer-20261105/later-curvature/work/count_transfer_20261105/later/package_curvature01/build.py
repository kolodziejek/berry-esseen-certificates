"""Create-only standalone curvature supplement; old package remains unchanged."""
from pathlib import Path
import hashlib,json,subprocess,sys,time,runpy
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;ROOT=BASE.parents[2]
OUT=BASE/'portable_curvature01';RUN=ROOT/'runs/count_transfer_20261105/later_curvature_portable01'
def need(x,m):
    if not x:raise ValueError(m)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def pin(p):return dict(bytes=p.stat().st_size,sha256=sha(p))
def main():
    need(__debug__ and not sys.flags.optimize,'ordinary Python')
    manifest=BASE/'FILES04.json';selected=json.loads(manifest.read_text())['files']
    selected[str(manifest.relative_to(ROOT))]=pin(manifest)
    for rel,v in selected.items():
        p=ROOT/rel;need(p.is_file()and not p.is_symlink()and pin(p)==v,'selected stopped bytes '+rel)
    OUT.mkdir(exist_ok=False)
    for rel,v in sorted(selected.items()):
        dst=OUT/rel;dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes((ROOT/rel).read_bytes());need(pin(dst)==v,'exact copied bytes')
    # Reuse the already inspected inventory runner without changing its algorithm.
    old=BASE/'portable_later01/replay.py';source=old.read_text()
    need(source.count('gaussian_taylor01/check_wide_phase.py')==1,'unique old reader path')
    source=source.replace('gaussian_taylor01/check_wide_phase.py','gaussian_curvature01/check_two_cells.py').replace('The bounded selected sharp39 wider-phase rectangle only.','The source-bound sharp39 full-p/narrow-phase two-cell rectangle only; not the full row.')
    (OUT/'replay.py').write_text(source)
    (OUT/'README.md').write_text('''# Sharp39 full-probability, narrow-phase certificate

This additive package proves the original acquired sharp39 panel38 positive closed-score implication on n=39, k=15, p∈[.38,.39], u∈[-.01,.01], and 0≤lambda≤.185. It retains the original same-law/resource/support hypotheses. Other phases and nearest-count roots remain open for this replacement method; this is not a complete original-row or sharp39 proof, and original acquisition was not replayed.

Run the complete exact check using ordinary Python and a fresh external output:

```sh
python3 -I -B -S replay.py /absolute/NEW_OUTPUT
```

Acceptance needs only the standard library. The public wrapper verifies the complete byte inventory, calls the unchanged source-bound reader and preserves actual exit/stdout/stderr. It does not trust stored PASS records. The two fixed closed probability cells meet at .385; every phase/noise point in the stated rectangle is covered, including atoms and zero noise. The unchanged forty countwise quartics are checked globally on both rays. The score and Hessian checks use exact rationals and complete Bernstein arrays.

Proofs are under work/count_transfer_20261105/later/: GENERAL_N_SOUNDNESS.md, TANGENT_PRICE.md, gaussian_taylor01/SOUNDNESS.md and gaussian_curvature01/{SOUNDNESS.md,TWO_CELL_RESULT.md}. The last two distinguish the failed one-cell sufficient test from the successful fixed two-cell cover. Curvature correction removes the negative-numerator restriction from the variance-vertex argument. The source-bound original contracts are under selected/ in that same later directory. This package contains that mathematical replay closure, not the complete original acquisition archive.

The independent review is work/count_transfer_20261105/review/CURVATURE_COVER_REVIEW.md. It re-derived the scalar argument and compared all 54 corrected Hessian arrays and 3,006 inverse coefficients against an independent expansion. Independent review drivers and historical captures retain their original path provenance; the supported portable command is the public entry above. No formal verification or external-referee claim is made.

All stopped failure/control/success records selected for this epoch are included under runs/. The original one-cell failure and the initial control-harness result-serialization error remain preserved. The latter was repaired additively without changing mathematical checks. No accepted arithmetic used Python optimization. FILES.json inventories every package file except itself; hashes establish integrity, not correctness.
''')
    # Run unchanged native entry once in the relocated minimal source hierarchy.
    RUN.mkdir(exist_ok=False);reader=OUT/'work/count_transfer_20261105/later/gaussian_curvature01/check_two_cells.py'
    before={rel:pin(OUT/rel)for rel in selected};cmd=[sys.executable,'-I','-B','-S',str(reader),str(RUN/'accepted')];t=time.monotonic();p=subprocess.run(cmd,capture_output=True)
    (RUN/'stdout.txt').write_bytes(p.stdout);(RUN/'stderr.txt').write_bytes(p.stderr)
    obs=dict(command=cmd,returncode=p.returncode,seconds=time.monotonic()-t,stdout_sha256=sha(RUN/'stdout.txt'),stderr_sha256=sha(RUN/'stderr.txt'),selected_source_unchanged=all(pin(OUT/rel)==v for rel,v in before.items()),scope='Complete relocated two-cell comparison only; original acquisition and full row not replayed.')
    (RUN/'PROCESS.json').write_text(json.dumps(obs,indent=2)+'\n')
    need(p.returncode==0 and not p.stderr and obs['selected_source_unchanged'],'actual relocated exact result')
    result=json.loads((RUN/'accepted/RESULT.json').read_text())
    need(result['p']==['19/50','39/100']and result['u']==['-1/100','1/100']and result['score_coefficients']==11880 and result['psd_coefficients']==3006 and result['global_rays']==160,'exact accepted scope/census')
    for p in sorted(RUN.rglob('*')):
        if p.is_file():dst=OUT/p.relative_to(ROOT);dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(p.read_bytes())
    completion=dict(status='PRESERVED_TWO_CELL_CURVATURE_PROOF_WITH_FULL_RELOCATED_PASS',mathematical_scope='Original sharp39 acquired-row implication, n39/k15/p[.38,.39]/u±.01/noise[0,.185].',full_original_row=False,original_acquisition_replayed=False,relocated_result_sha256=sha(RUN/'accepted/RESULT.json'))
    (OUT/'COMPLETION.json').write_text(json.dumps(completion,indent=2)+'\n')
    files={str(p.relative_to(OUT)):pin(p)for p in sorted(OUT.rglob('*'))if p.is_file()}
    (OUT/'FILES.json').write_text(json.dumps(dict(files=files),indent=2)+'\n')
    need(runpy.run_path(str(OUT/'replay.py'))['verify']()==sha(OUT/'FILES.json'),'published complete inventory reader')
    final=dict(status='PASS_PORTABLE_CURVATURE_SUPPLEMENT',package=str(OUT.relative_to(ROOT)),files=len(files)+1,bytes=sum(v['bytes']for v in files.values())+(OUT/'FILES.json').stat().st_size,manifest_sha256=sha(OUT/'FILES.json'),relocated_result_sha256=sha(RUN/'accepted/RESULT.json'),full_original_row=False)
    (RUN/'PACKAGE_RESULT.json').write_text(json.dumps(final,indent=2)+'\n');print(json.dumps(final))
if __name__=='__main__':main()
