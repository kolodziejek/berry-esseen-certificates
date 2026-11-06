"""Additive canonical-object entry to the unchanged tangent arithmetic."""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import tangent_pilot as t
import strict_object
def main():
 t.m.need(__debug__ and not sys.flags.optimize and len(sys.argv)==3,'ordinary Python OBJECT NEW_OUTPUT')
 path=Path(sys.argv[1]);out=Path(sys.argv[2]);t.m.need(not out.exists(),'fresh output');obj=strict_object.read(path)
 pins=json.loads((HERE/'PUBLIC_SOURCE_PINS.json').read_text())
 for rel,h in pins.items():t.m.need(t.m.sha(HERE/rel)==h,'current pinned source '+rel)
 r=t.check(t.m.context(39,True),obj)
 for rel,h in pins.items():t.m.need(t.m.sha(HERE/rel)==h,'stable source '+rel)
 r.update(input_sha256=t.m.sha(path),source_sha256=pins,reader_sha256=t.m.sha(__file__),canonical_object=True)
 out.mkdir();(out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'canonical_object':True,'global_rays':80}))
if __name__=='__main__':main()
