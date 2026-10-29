#!/usr/bin/env python3
"""Exact complete replay acceptance for the v8 signed phase export."""
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
from fractions import Fraction as F
import sys,json,subprocess,argparse
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
PINS={
 'mathematics/fixed-target-v8/2026-10-28/phase_probe.py':'fe59af3964c7cb6800d7f667c1ffd958ecf2bf7ae42728129999d6914b523fc8',
 'mathematics/fixed-target-v8/2026-10-28/phase_core.py':'c9cc7e5a0e5637faafc912882cdb9bcd28bda5fa9982304ede2ab412c724ee7a',
 'mathematics/fixed-target-v8/2026-10-28/build_phase_core.py':'f39b10eed0da60f35b37393cd046f72dd2d45bd58afd60cf3e82b339de113bdd',
 'mathematics/fixed-target-v7/2026-10-27/accept_entry.py':'fe8197d6943c4decb7421bd1c162d7ec24045fdb3ea1215356249b4be620d69d',
 'mathematics/fixed-target-v7/2026-10-27/entry-proof.json':'61b7ad43e20046d7cbf7157e3feb61696331731e7be418f6a5fa535c2eee8bae',
 'mathematics/fixed-target-v7/2026-10-27/signed_core.py':'1f40ccb90eb58a7f84dc61a0a5dd9bf6e6eb4e341aa6c9c6d049d08451f5211b',
 'mathematics/fixed-target-v7/2026-10-27/signed_support.py':'eecb06e65d8520d7cc06fc34217e06e1c0b1840dd8d687621e6828923769a4c4',
 'mathematics/fixed-target-v5/2026-10-27/cell-sources/kernel.py':'d71f58b7527c3cf6d2146d816e5d124f6f331d1b153e5aaedee5182707647f12',
 'mathematics/fixed-target-v5/2026-10-27/cell-sources/high_window_core.py':'53e181be63852e21abc3f44191cce7237c46d9e9d7868d3b6b94fccb606c7232'}
def need(ok,why):
 if not ok:raise ValueError(why)
def unique(pairs):
 d={}
 for k,v in pairs:need(k not in d,'duplicate JSON key');d[k]=v
 return d
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)
def match(candidate,replayed):need(canonical(candidate)==canonical(replayed),'complete deterministic phase export')
def main():
 ap=argparse.ArgumentParser();ap.add_argument('proof',type=Path);args=ap.parse_args()
 need(__debug__ and not sys.flags.optimize,'unoptimized interpreter')
 for p,h in PINS.items():need(sha256((ROOT/p).read_bytes()).hexdigest()==h,'pinned source before execution '+p)
 blob=args.proof.read_bytes();obj=json.loads(blob,object_pairs_hook=unique)
 cmd=[sys.executable,'-B',str(HERE/'phase_probe.py')]
 r=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True,timeout=120)
 need(r.returncode==0,'fresh full phase replay');actual=json.loads(r.stdout,object_pairs_hook=unique)
 need(actual['total_cells']==2048 and actual['active_cells']==len(actual['phase_cells'])==682,'replayed full fourth pass')
 match(obj,actual)
 controls=[]
 def reject(name,fn):
  try:fn()
  except (ValueError,TypeError):controls.append(name)
  else:raise ValueError('invalid phase proof accepted: '+name)
 changes=[('missing phase cell',lambda z:z['phase_cells'].pop()),
  ('duplicated phase cell',lambda z:z['phase_cells'].__setitem__(1,z['phase_cells'][0])),
  ('reordered phase cells',lambda z:z['phase_cells'].reverse()),
  ('missing rho row',lambda z:z['rows'].pop()),
  ('wrong census',lambda z:z.update(total_cells=2047)),
  ('boolean census',lambda z:z.update(active_cells=True)),
  ('floating census',lambda z:z.update(active_cells=682.0)),
  ('false parent proof',lambda z:z.update(source_proof_sha256='0'*64)),
  ('false signed coefficient',lambda z:z['phase_cells'][0]['quadratics'][0].update(plus='0')),
  ('false raw ceiling',lambda z:z['phase_cells'][0].update(raw='0')),
  ('changed probability seam',lambda z:z['phase_cells'][0].update(pl='0')),
  ('unknown field',lambda z:z.update(extra=0))]
 for name,change in changes:
  bad=deepcopy(obj);change(bad);reject(name,lambda:match(bad,actual))
 reject('duplicate JSON key',lambda:json.loads('{"x":0,"x":1}',object_pairs_hook=unique))
 print(json.dumps(dict(status='PASS_COMPLETE_SIGNED_PHASE_EXPORT_V8',total_cells=2048,active_cells=682,
  proof_sha256=sha256(blob).hexdigest(),replay_stdout_sha256=sha256(r.stdout.encode()).hexdigest(),
  replay_command=cmd,source_sha256=PINS,rejected_controls=controls,
  mathematical_scope='Complete signed quadratic export from the accepted v7 fourth pass. Analytic resource implications and inherited premises are separate; no full confinement/count/base acceptance.'),indent=2))
if __name__=='__main__':main()
