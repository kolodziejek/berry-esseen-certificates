"""Source-bound, canonical-data full four-strip rectangle entry point."""
from pathlib import Path
import sys,json
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import strict_object
import check_tangent_rectangle as original
def main():
 need=original.m.need
 need(__debug__ and not sys.flags.optimize and len(sys.argv)==3,'ordinary Python OBJECT NEW_OUTPUT')
 path=Path(sys.argv[1]);out=Path(sys.argv[2]);need(not out.exists(),'fresh output')
 obj=strict_object.read(path);fixed=strict_object.read(HERE/'N39_TANGENT_CANDIDATE.json');need(obj==fixed,'this fixed candidate and explicit bounded rectangle')
 pins=json.loads((HERE/'PUBLIC_SOURCE_PINS.json').read_text())
 for rel,h in pins.items():need(original.m.sha(HERE/rel)==h,'current source byte '+rel)
 # Preserve the entire already reviewed numerical routine; it reads these same
 # canonical fixed coefficients and reconstructs every domain and inequality.
 argv=sys.argv;sys.argv=[str(Path(original.__file__)),str(out)]
 try:original.main()
 finally:sys.argv=argv
 for rel,h in pins.items():need(original.m.sha(HERE/rel)==h,'stable source byte '+rel)
 record={'scope':'Full original four-strip continuous rectangle arithmetic, current canonical proof-data entry.','input_sha256':original.m.sha(path),'source_sha256':pins,'reader_sha256':original.m.sha(__file__),'result_sha256':original.m.sha(out/'RESULT.json'),'source_unchanged':True,'canonical_object':True}
 (out/'SOURCE_BINDING.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'status':'PASS_CANONICAL_SOURCE_BOUND_CONTINUOUS_RECTANGLE','result_sha256':record['result_sha256']}))
if __name__=='__main__':main()
