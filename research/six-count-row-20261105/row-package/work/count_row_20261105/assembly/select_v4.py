"""Create only a three-root object selection; this is not score acceptance."""
from pathlib import Path
import argparse,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import complete_v4 as c

def main():
 c.need(__debug__ and not sys.flags.optimize,'unoptimized selector')
 ap=argparse.ArgumentParser();ap.add_argument('output',type=Path)
 for k in (1,2,3):ap.add_argument('--k'+str(k),required=True,type=Path)
 a=ap.parse_args();roots=[]
 for k,path in [(k,getattr(a,'k'+str(k)).resolve())for k in (1,2,3)]:
  c.ordinary(path);c.need(path.is_relative_to(c.ROOT),'workspace proof object');obj=c.read(path)
  policy='clipped'if c.same(obj.get('u'),c.CLIPPED[k])else'full'if c.same(obj.get('u'),['-1/2','1/2'])else None
  c.need(policy is not None,'approved complete phase root')
  roots.append({'k':k,'domain':policy,'object':str(path.relative_to(c.ROOT)),'object_sha256':c.sha(path)})
 selected={'schema':'EXACT_N5_BN38_THREE_ROOT_SELECTION_V1','contract_sha256':c.CONTRACT_SHA,'domain_sha256':c.DOMAIN_SHA,'reader_manifest_sha256':c.MANIFEST_SHA,'roots':roots}
 c.preflight(selected)
 with a.output.open('x')as f:json.dump(selected,f,indent=2);f.write('\n')
 print(json.dumps({'status':'CREATED_SOURCE_BOUND_SELECTION_NOT_ACCEPTED','sha256':c.sha(a.output),'output':str(a.output)}))
if __name__=='__main__':main()
