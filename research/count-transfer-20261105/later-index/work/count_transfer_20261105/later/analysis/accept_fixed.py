"""Stdlib-only exact readback of the bounded n6 fixed-location candidate."""
from pathlib import Path
import hashlib,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import pilot as m
def unique(items):
 d={}
 for k,v in items:m.need(k not in d,'duplicate JSON key');d[k]=v
 return d
def main():
 m.need(__debug__ and not sys.flags.optimize and len(sys.argv)==3,'ordinary exact invocation: OBJECT NEW_OUTPUT')
 objpath=Path(sys.argv[1]);out=Path(sys.argv[2]);m.need(not out.exists(),'fresh output')
 obj=json.loads(objpath.read_text(),object_pairs_hook=unique)
 m.need(set(obj)=={'q','theta'},'only candidate coefficients and common price')
 pins=json.loads((HERE/'FIXED_SOURCE_PINS.json').read_text())
 for rel,h in pins.items():m.need(m.sha(HERE/rel)==h,'fixed mathematical source '+rel)
 c=m.context(6,False);r=m.check(c,obj['q'],obj['theta'])
 r.update(input_sha256=m.sha(objpath),source_sha256=pins,acceptor_sha256=m.sha(__file__),
  scope='Conditional n6 BN/p38 at fixed p77/200,k2,u0 only; all actual source-licensed noise at this p. Original acquisition not replayed; no full p/phase row.')
 out.mkdir();(out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
if __name__=='__main__':main()
