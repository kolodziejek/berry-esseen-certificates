"""Stdlib-only exact acceptance of the single source-bound sharp39 pilot."""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import tangent_pilot as t
def main():
 t.m.need(__debug__ and not sys.flags.optimize and len(sys.argv)==3,'ordinary Python OBJECT NEW_OUTPUT')
 objpath=Path(sys.argv[1]);out=Path(sys.argv[2]);t.m.need(not out.exists(),'fresh output')
 def unique(items):
  d={}
  for k,v in items:t.m.need(k not in d,'duplicate key');d[k]=v
  return d
 obj=json.loads(objpath.read_text(),object_pairs_hook=unique);t.m.need(set(obj)=={'q','theta'},'exact candidate fields')
 pins=json.loads((HERE/'TANGENT_SOURCE_PINS.json').read_text())
 for rel,h in pins.items():t.m.need(t.m.sha(HERE/rel)==h,'pinned source '+rel)
 c=t.m.context(39,True);r=t.check(c,obj);r.update(object_sha256=t.m.sha(objpath),source_sha256=pins,reader_sha256=t.m.sha(__file__),scope='One fixed p/phase original sharp39 contract implication; no complete row or acquisition replay.')
 out.mkdir();(out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'n':39,'p':'77/200','k':15,'u':'0','global_rays':r['global_rays'],'vertices':r['vertices'],'cdf_margin':r['cdf_margin']}))
if __name__=='__main__':main()
