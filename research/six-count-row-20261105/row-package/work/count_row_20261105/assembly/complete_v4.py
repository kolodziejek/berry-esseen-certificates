"""Admit one complete original row only by three fresh unchanged V4 executions.

The original acquisition remains a premise. No stored success flag is read.
"""
from pathlib import Path,PurePosixPath
from fractions import Fraction as F
import argparse,hashlib,json,subprocess,sys,time,platform
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
MANIFEST_SHA='ffa814c525fceaafe39e47e9352b544557ffb83d3225f5329ceba55180474589'
DOMAIN_PATH='work/count_row_20261105/domain/domain.json'
DOMAIN_SHA='7808638d276d78f858ba64fb3124f088bf131f39c44729bb2e0a254e4c117154'
CONTRACT_SHA='2b3f626ba3a9e954e4700bf206cf7a364f44958bb901b463198249dda2f37e48'
READER_FILES={'model.py','model_v4.py','accept_v4.py','native/quartic_sturm.py','native/quartic_global.py','native/finite_binomial_core.py','native/contract.json'}
P=['19/50','39/100'];NOISE=['0','7687/25000']
CLIPPED={1:['-222258117249/1000000000000','1/2'],2:['-1/2','1/2'],3:['-1/2','72258117249/1000000000000']}

def need(ok,msg):
 if not ok:raise ValueError(msg)
def unique(pairs):
 out={}
 for k,v in pairs:need(k not in out,'duplicate JSON key');out[k]=v
 return out
def invalid(s):raise ValueError('nonfinite JSON '+s)
def loads(b):return json.loads(b,object_pairs_hook=unique,parse_constant=invalid)
def read(p):return loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p):return {'bytes':p.stat().st_size,'sha256':sha(p)}
def same(a,b):return json.dumps(a,sort_keys=True,separators=(',',':'),allow_nan=False)==json.dumps(b,sort_keys=True,separators=(',',':'),allow_nan=False)
def ordinary(p):need(p.is_file() and not p.is_symlink(),'regular nonsymlink file '+str(p))
def relative_path(s):
 need(type(s)is str and s and '\\'not in s and '\0'not in s,'relative path string')
 p=PurePosixPath(s);need(not p.is_absolute() and '..'not in p.parts and str(p)==s,'canonical workspace path')
 result=ROOT/s;ordinary(result);need(result.resolve().is_relative_to(ROOT),'workspace containment');return result

def source_state():
 manifest=HERE/'READER_SOURCES_V4.json';ordinary(manifest);need(sha(manifest)==MANIFEST_SHA,'reviewed reader manifest')
 m=read(manifest);need(m['schema']=='PINNED_UNCHANGED_N5_BN38_V4_READER_V1' and m['entry']=='accept_v4.py' and set(m['files'])==READER_FILES,'exact reader closure')
 reader=ROOT/m['reader_root'];need(reader.is_dir() and reader.resolve().is_relative_to(ROOT),'reader root')
 for name,item in m['files'].items():
  path=reader/name;ordinary(path);need(pin(path)==item,'unchanged V4 source '+name)
 need({str(p.relative_to(reader))for p in (reader/'native').glob('*.py')}=={x for x in READER_FILES if x.startswith('native/')and x.endswith('.py')},'no unknown native Python dependency')
 domain=ROOT/DOMAIN_PATH;ordinary(domain);need(sha(domain)==DOMAIN_SHA,'reviewed original threshold projection')
 d=read(domain);need(d['source']['sha256']==CONTRACT_SHA and m['files']['native/contract.json']['sha256']==CONTRACT_SHA,'same original contract')
 for name,item in d['source_pins'].items():
  path=relative_path(name);need(pin(path)==item,'unchanged original source projection '+name)
 return m,reader

def preflight(selection):
 m,reader=source_state()
 need(type(selection)is dict and set(selection)=={'schema','contract_sha256','domain_sha256','reader_manifest_sha256','roots'},'selection schema')
 need(selection['schema']=='EXACT_N5_BN38_THREE_ROOT_SELECTION_V1' and selection['contract_sha256']==CONTRACT_SHA and selection['domain_sha256']==DOMAIN_SHA and selection['reader_manifest_sha256']==MANIFEST_SHA,'original source and reviewed reader bindings')
 roots=selection['roots'];need(type(roots)is list and len(roots)==3,'exactly three original threshold roots')
 seen=set();paths=set();jobs=[]
 for z in roots:
  need(type(z)is dict and set(z)=={'k','domain','object','object_sha256'},'root selector fields')
  k=z['k'];need(type(k)is int and k in CLIPPED and k not in seen,'unique exact nearest count');seen.add(k)
  need(z['domain']in('clipped','full'),'explicit approved phase-root policy')
  u=CLIPPED[k]if z['domain']=='clipped'else['-1/2','1/2']
  objpath=relative_path(z['object']);need(z['object']not in paths,'no reused object path');paths.add(z['object'])
  need(type(z['object_sha256'])is str and len(z['object_sha256'])==64 and sha(objpath)==z['object_sha256'],'object identity')
  obj=read(objpath)
  need(type(obj)is dict and set(obj)=={'schema','contract_sha256','n','k','p','u','noise','tree'},'exact V4 proof-object header')
  need(obj['schema']=='N5_BN38_SIX_COUNT_CELL_V4'and obj['contract_sha256']==CONTRACT_SHA,'V4 object target')
  need(type(obj['n'])is int and obj['n']==5 and type(obj['k'])is int and obj['k']==k,'object actual count binding')
  need(same(obj['p'],P) and same(obj['u'],u) and same(obj['noise'],NOISE),'whole externally fixed probability/phase/noise root')
  jobs.append({'k':k,'domain':z['domain'],'u':u,'object_path':objpath,'object_sha256':z['object_sha256']})
 need(seen=={1,2,3},'complete original nearest-count census')
 return m,reader,sorted(jobs,key=lambda j:j['k'])

def decimal(s):
 # All externally fixed endpoints terminate. Decimal spelling avoids argparse's
 # interpreting a negative rational such as -1/2 as a new option.
 value=F(s);den=value.denominator
 while den%2==0:den//=2
 while den%5==0:den//=5
 need(den==1,'terminating fixed endpoint')
 power=1;places=0
 while power%value.denominator:power*=10;places+=1
 num=value.numerator*(power//value.denominator);sign='-'if num<0 else'';num=abs(num)
 if not places:return sign+str(num)
 return sign+str(num//power)+'.'+str(num%power).zfill(places)

def execute(selection_path,out):
 need(__debug__ and not sys.flags.optimize,'unoptimized parent');selection_path=selection_path.resolve();ordinary(selection_path)
 raw=selection_path.read_bytes();selection=loads(raw);m,reader,jobs=preflight(selection)
 out=out.resolve();need(not out.exists() and not out.is_relative_to(reader),'fresh output outside frozen reader')
 out.mkdir(parents=True,exist_ok=False)
 (out/'SELECTION.json').write_bytes(raw)
 (out/'READER_SOURCES_V4.json').write_bytes((HERE/'READER_SOURCES_V4.json').read_bytes())
 (out/'DOMAIN.json').write_bytes((ROOT/DOMAIN_PATH).read_bytes())
 start={'schema':'ACTUAL_N5_BN38_COMPLETE_ROW_ATTEMPT_V1','wrapper_sha256':sha(Path(__file__)),'selection_sha256':hashlib.sha256(raw).hexdigest(),'reader_manifest_sha256':MANIFEST_SHA,'domain_sha256':DOMAIN_SHA,'python':sys.version,'executable':sys.executable,'resolved_executable':str(Path(sys.executable).resolve()),'executable_sha256':sha(Path(sys.executable).resolve()),'platform':platform.platform(),'jobs':[{'k':j['k'],'u':j['u'],'object':str(j['object_path'].relative_to(ROOT)),'object_sha256':j['object_sha256']}for j in jobs]}
 (out/'STARTED.json').write_text(json.dumps(start,indent=2)+'\n');completed=[]
 for job in jobs:
  source_state();need(sha(selection_path)==start['selection_sha256'],'unchanged selection')
  need(all(sha(j['object_path'])==j['object_sha256']for j in jobs),'unchanged selected objects before actual execution')
  task=out/('k'+str(job['k']));task.mkdir(exist_ok=False);candidate=task/'proof_object.json';candidate.write_bytes(job['object_path'].read_bytes())
  command=[sys.executable,'-I','-B','-S',str(reader/'accept_v4.py'),str(candidate),str(task/'accepted'),'--k',str(job['k']),'--p',*map(decimal,P),'--u',*map(decimal,job['u']),'--noise',*map(decimal,NOISE)]
  started={'command':command,'object_sha256':job['object_sha256'],'reader_manifest_sha256':MANIFEST_SHA,'k':job['k'],'p':P,'u':job['u'],'noise':NOISE}
  (task/'STARTED.json').write_text(json.dumps(started,indent=2)+'\n')
  t=time.monotonic();process=subprocess.run(command,cwd=ROOT,capture_output=True);elapsed=time.monotonic()-t
  (task/'stdout.txt').write_bytes(process.stdout);(task/'stderr.txt').write_bytes(process.stderr)
  obs={**started,'returncode':process.returncode,'seconds':elapsed,'stdout_sha256':hashlib.sha256(process.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(process.stderr).hexdigest(),'result_path':'accepted/RESULT.json'if(task/'accepted/RESULT.json').exists()else None}
  (task/'PROCESS.json').write_text(json.dumps(obs,indent=2)+'\n')
  source_state();need(sha(Path(__file__))==start['wrapper_sha256']and sha(selection_path)==start['selection_sha256'],'stable wrapper/selection')
  need(sha(candidate)==job['object_sha256']and all(sha(j['object_path'])==j['object_sha256']for j in jobs),'stable exact inputs')
  if process.returncode!=0:
   failure={'status':'REJECTED_INCOMPLETE_ROW_ATTEMPT','failed_k':job['k'],'actual_returncode':process.returncode,'completed_roots':completed,'complete_row_score_claimed':False,'observation_sha256':sha(task/'PROCESS.json')}
   (out/'FAILED.json').write_text(json.dumps(failure,indent=2)+'\n');print(json.dumps(failure));return 1
  need(not process.stderr,'successful native stderr must be empty')
  result=read(task/'accepted/RESULT.json');packet=loads(process.stdout)
  need(same(packet,{key:value for key,value in result.items()if key!='leaves'}),'complete native stdout/result identity')
  need(result['status']=='PASS_EXACT_COMPLETE_CLOSED_RECTANGLE'and type(result['n'])is int and result['n']==5 and type(result['k'])is int and result['k']==job['k'],'actual exact completed root')
  need(same(result['p'],P)and same(result['u'],job['u'])and same(result['noise'],NOISE),'actual full source-bound rectangle')
  need(result['beta']==['-15293/500000','307221/1000000']and result['rho_lower']=='11/10','original signed moment/score scope')
  need(result['object_sha256']==job['object_sha256']and same(result['source_sha256'],{name:v['sha256']for name,v in m['files'].items()}),'entire actual source/object binding')
  need(type(result['leaves'])is list and result['leaves']and type(result['nodes'])is int and result['nodes']==2*len(result['leaves'])-1,'complete finite binary tree')
  need(result['rays']==12*len(result['leaves'])and all(F(z['cleared_margin'])>0 for z in result['leaves']),'complete strict numerical leaf results')
  completed.append({'k':job['k'],'p':P,'u':job['u'],'noise':NOISE,'actual_returncode':0,'result_sha256':sha(task/'accepted/RESULT.json'),'observation_sha256':sha(task/'PROCESS.json'),'object_sha256':job['object_sha256'],'leaves':len(result['leaves']),'rays':result['rays'],'tensor_coefficients':result['tensor_coefficients']})
 need([x['k']for x in completed]==[1,2,3],'all three roots actually accepted')
 report={'status':'PASS_FRESH_COMPLETE_ORIGINAL_N5_BN38_ROW_COMPARISON_V4','mathematical_status':'Exact positive closed-score implication on the whole original acquired n5 BN/p38 row; original acquisition/contact/threshold bounds remain premises. No whole n5 or all-law theorem.',
  'execution_status':'Three fresh unchanged V4 exact reader processes completed; no stored PASS admitted.','n':5,'band':'BN','index':38,'K':'0','p':P,'noise':NOISE,'source_contract_sha256':CONTRACT_SHA,'domain_sha256':DOMAIN_SHA,'reader_manifest_sha256':MANIFEST_SHA,'wrapper_sha256':start['wrapper_sha256'],'selection_sha256':start['selection_sha256'],'completed_roots':completed,'total_leaves':sum(x['leaves']for x in completed),'total_rays':sum(x['rays']for x in completed),'total_tensor_coefficients':sum(x['tensor_coefficients']for x in completed),'original_acquisition_rerun':False,'full_n5_claimed':False}
 (out/'RESULT.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':report['status'],'result_sha256':sha(out/'RESULT.json'),'roots':3,'leaves':report['total_leaves']}));return 0
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('selection',type=Path);ap.add_argument('out',type=Path);a=ap.parse_args();raise SystemExit(execute(a.selection,a.out))
