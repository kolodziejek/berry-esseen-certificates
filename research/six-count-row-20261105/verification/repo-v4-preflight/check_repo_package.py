"""Bounded repository relocation check; never repeats the full arithmetic."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,runpy,sys
ap=argparse.ArgumentParser();ap.add_argument('package',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args()
assert __debug__ and not sys.flags.optimize
p=a.package.resolve();out=a.out.resolve();assert not out.exists()
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
expected='51d78e86cd3e6422eb2bebded20e730fd1c0cabbc47931b3deb37145222d7045'
assert sha(p/'FILES.json')==expected
namespace=runpy.run_path(str(p/'replay.py'));assert namespace['verify']()==expected
path=p/'work/count_row_20261105/assembly/complete_v4.py'
s=importlib.util.spec_from_file_location('reviewed_row_collector',path)
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
_,_,jobs=m.preflight(m.read(p/'runs/count_row_20261105/SELECTED_COMPLETE_V4.json'))
assert [j['k']for j in jobs]==[1,2,3]
assert namespace['verify']()==expected
result={'status':'PASS_REPOSITORY_INVENTORY_AND_ALL_ROOT_PREFLIGHT',
 'scope':'Byte integrity and actual source/header preflight after repository relocation; no additional full arithmetic replay.',
 'package':str(p),'manifest_sha256':expected,'collector_sha256':sha(path),
 'root_object_sha256':{str(j['k']):j['object_sha256']for j in jobs},
 'python':sys.version,'script_sha256':sha(Path(__file__))}
out.mkdir(parents=True,exist_ok=False)
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
