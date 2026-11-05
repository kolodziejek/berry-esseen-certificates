"""Canonical n6 data entry; original exact fixed-location arithmetic unchanged."""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import pilot as m
import strict_object
def main():
 m.need(__debug__ and not sys.flags.optimize and len(sys.argv)==3,'ordinary Python OBJECT NEW_OUTPUT')
 path=Path(sys.argv[1]);out=Path(sys.argv[2]);m.need(not out.exists(),'fresh output');obj=strict_object.read(path,6)
 pins=json.loads((HERE/'PUBLIC_SOURCE_PINS.json').read_text())
 for rel,h in pins.items():m.need(m.sha(HERE/rel)==h,'current source byte '+rel)
 r=m.check(m.context(6,False),obj['q'],obj['theta'])
 for rel,h in pins.items():m.need(m.sha(HERE/rel)==h,'stable source byte '+rel)
 r.update(input_sha256=m.sha(path),source_sha256=pins,reader_sha256=m.sha(__file__),canonical_object=True)
 out.mkdir();(out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'n':6,'canonical_object':True,'global_rays':14}))
if __name__=='__main__':main()
