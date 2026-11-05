"""One final fixed-coefficient wider-phase test; successful scope never inferred."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,time
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE));import check_broad as b
def main():
 b.m.need(__debug__ and not sys.flags.optimize and len(sys.argv)==2,'ordinary Python NEW_OUTPUT');out=Path(sys.argv[1]);b.m.need(not out.exists(),'fresh output')
 pins=json.loads((HERE/'WIDE_SOURCE_PINS.json').read_text())
 for name,h in pins.items():b.m.need(b.m.sha(HERE/name)==h,'pinned complete source closure')
 obj=b.strict_object.read(b.BASE/'N39_TANGENT_CANDIDATE.json');out.mkdir();tt=time.monotonic()
 try:r=b.check(obj,F(77,200),F(39,100),-F(1,100),F(1,100))
 except ValueError as e:
  (out/'FAILED.json').write_text(json.dumps({'status':'WIDER_PHASE_BOUND_NOT_ESTABLISHED','p':['77/200','39/100'],'u':['-1/100','1/100'],'reason':str(e),'unchanged_object_sha256':b.m.sha(b.BASE/'N39_TANGENT_CANDIDATE.json')},indent=2)+'\n');raise
 for name,h in pins.items():b.m.need(b.m.sha(HERE/name)==h,'stable whole source closure')
 r.update(source_sha256=pins,reader_sha256=b.m.sha(__file__),object_sha256=b.m.sha(b.BASE/'N39_TANGENT_CANDIDATE.json'),seconds=time.monotonic()-tt)
 (out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items()if k not in('source_sha256','gaussian_enclosures','psd_minima')}))
if __name__=='__main__':main()
