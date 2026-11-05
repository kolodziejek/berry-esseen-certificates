"""Disposable malformed-root/source tests plus actual unchanged reader rejection."""
from pathlib import Path
from copy import deepcopy
import argparse,json,sys,subprocess
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import complete_v4 as c

def write(p,z):p.write_text(json.dumps(z,indent=2)+'\n')
def main():
 c.need(__debug__ and not sys.flags.optimize,'unoptimized controls')
 ap=argparse.ArgumentParser();ap.add_argument('output',type=Path);a=ap.parse_args();out=a.output.resolve();out.mkdir(parents=True,exist_ok=False)
 pins={str(p):c.sha(p)for p in [Path(__file__),HERE/'complete_v4.py',HERE/'select_v4.py',HERE/'READER_SOURCES_V4.json']}
 objects=out/'fixtures';objects.mkdir();roots=[]
 for k in (1,2,3):
  obj={'schema':'N5_BN38_SIX_COUNT_CELL_V4','contract_sha256':c.CONTRACT_SHA,'n':5,'k':k,'p':c.P,'u':c.CLIPPED[k],'noise':c.NOISE,'tree':{'failed':{'status':'DELIBERATELY_INCOMPLETE_CONTROL'}}}
  p=objects/f'k{k}.json';write(p,obj);roots.append({'k':k,'domain':'clipped','object':str(p.relative_to(c.ROOT)),'object_sha256':c.sha(p)})
 sel={'schema':'EXACT_N5_BN38_THREE_ROOT_SELECTION_V1','contract_sha256':c.CONTRACT_SHA,'domain_sha256':c.DOMAIN_SHA,'reader_manifest_sha256':c.MANIFEST_SHA,'roots':roots}
 # This is header preflight only; its deliberately failed leaves cannot accept.
 _,_,jobs=c.preflight(sel);c.need([j['k']for j in jobs]==[1,2,3],'canonical baseline preflight')
 reorder=deepcopy(sel);reorder['roots'].reverse();_,_,jj=c.preflight(reorder);c.need([j['k']for j in jj]==[1,2,3],'harmless selector order invariance')
 full=deepcopy(sel)
 for r in full['roots']:
  p=objects/f'full-k{r["k"]}.json';z=c.read(c.ROOT/r['object']);z['u']=['-1/2','1/2'];write(p,z);r.update(domain='full',object=str(p.relative_to(c.ROOT)),object_sha256=c.sha(p))
 c.preflight(full)
 mutants=[]
 def add(name,change):
  s=deepcopy(sel);change(s);mutants.append((name,s))
 add('missing root',lambda s:s['roots'].pop())
 add('duplicate count',lambda s:s['roots'].__setitem__(1,deepcopy(s['roots'][0])))
 add('wrong nearest count',lambda s:s['roots'][0].update(k=0))
 add('boolean count',lambda s:s['roots'][0].update(k=True))
 add('wrong ID/object association',lambda s:s['roots'][0].update(object=s['roots'][1]['object'],object_sha256=s['roots'][1]['object_sha256']))
 add('wrong object digest',lambda s:s['roots'][0].update(object_sha256='0'*64))
 add('wrong reader epoch',lambda s:s.update(reader_manifest_sha256='0'*64))
 add('wrong contract',lambda s:s.update(contract_sha256='0'*64))
 add('wrong domain pin',lambda s:s.update(domain_sha256='0'*64))
 add('arbitrary unlicensed root policy',lambda s:s['roots'][0].update(domain='tiny'))
 add('unexpected status authority',lambda s:s.update(status='PASS'))
 add('parent path traversal',lambda s:s['roots'][0].update(object='../fake.json'))
 add('absolute object path',lambda s:s['roots'][0].update(object=str(c.ROOT/s['roots'][0]['object'])))
 for name,fn in [('narrow probability',lambda o:o.update(p=['77/200','39/100'])),('noise omitted',lambda o:o.update(noise=['0','1/100'])),('wrong object schema',lambda o:o.update(schema='N5_BN38_SIX_COUNT_CELL_V3')),('missing phase face',lambda o:o.update(u=['-1/5','1/2'])),('false declared n',lambda o:o.update(n=6))]:
  s=deepcopy(sel);p=objects/(name.replace(' ','_')+'.json');obj=c.read(c.ROOT/s['roots'][0]['object']);fn(obj);write(p,obj);s['roots'][0].update(object=str(p.relative_to(c.ROOT)),object_sha256=c.sha(p));mutants.append((name,s))
 rejected=[];oldrun=c.subprocess.run
 def forbidden(*args,**kwargs):raise AssertionError('invalid preflight attempted a subprocess')
 c.subprocess.run=forbidden
 try:
  for i,(name,s)in enumerate(mutants):
   selection=objects/f'mutant{i}.json';write(selection,s);target=out/f'mutant-output{i}'
   try:c.execute(selection,target)
   except ValueError:pass
   else:raise ValueError('accepted corrupt selection '+name)
   c.need(not target.exists(),'rejected before output creation');rejected.append(name)
  oldhash=c.MANIFEST_SHA;c.MANIFEST_SHA='0'*64
  try:
   try:c.preflight(sel)
   except ValueError:rejected.append('source manifest changed')
   else:raise ValueError('altered source manifest accepted')
  finally:c.MANIFEST_SHA=oldhash
 finally:c.subprocess.run=oldrun
 try:c.loads('{"roots":[],"roots":[]}')
 except ValueError:rejected.append('duplicate JSON key')
 else:raise ValueError('duplicate key accepted')
 # Actual unchanged native reader must reject the deliberate failed tree even
 # when a neighboring artifact asserts success. No mocked numerical acceptance.
 selection=out/'INVALID_SELECTION.json';write(selection,sel)
 write(objects/'RESULT.json',{'status':'PASS_CONTROL_LIE_NOT_EVIDENCE','scope':'Deliberate untrusted fixture'})
 actualout=out/'actual-invalid-attempt';rc=c.execute(selection,actualout)
 c.need(rc==1 and not(actualout/'RESULT.json').exists()and(actualout/'FAILED.json').is_file(),'no complete-row result on actual failure')
 observation=c.read(actualout/'k1/PROCESS.json');c.need(observation['returncode']!=0 and not(actualout/'k2').exists(),'actual fail closed stops later roots')
 c.need(not(actualout/'k1/accepted').exists(),'no native success result')
 # Verify -O rejection through a real fresh wrapper invocation.
 command=[sys.executable,'-O','-I','-B','-S',str(HERE/'complete_v4.py'),str(selection),str(out/'optimized-output')]
 proc=subprocess.run(command,capture_output=True);(out/'optimized.stdout').write_bytes(proc.stdout);(out/'optimized.stderr').write_bytes(proc.stderr)
 c.need(proc.returncode!=0 and not(out/'optimized-output').exists(),'optimized execution fails before output');rejected.append('optimized Python')
 c.need(all(c.sha(Path(p))==h for p,h in pins.items()),'unchanged wrapper controls sources');c.source_state()
 result={'status':'PASS_BOUNDED_COMPLETE_ROW_WRAPPER_REJECTION_CONTROLS','scope':'Header/source/closed-root controls and actual unchanged V4 rejection of a synthetic incomplete tree; no real score object or full row admitted.',
  'preflight_baseline':'Three complete externally fixed root headers only, deliberately invalid numerical leaves','selector_order_invariant':True,'explicit_full_phase_enlargement_preflight':True,'rejected':rejected,'actual_invalid_reader_returncode':observation['returncode'],'actual_invalid_observation_sha256':c.sha(actualout/'k1/PROCESS.json'),'optimized_actual_returncode':proc.returncode,'source_pins':pins,'full_row_claimed':False}
 write(out/'RESULT.json',result);print(json.dumps({'status':result['status'],'rejections':len(rejected),'actual_native_rejection':observation['returncode'],'result_sha256':c.sha(out/'RESULT.json')}))
if __name__=='__main__':main()
