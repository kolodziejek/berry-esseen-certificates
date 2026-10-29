#!/usr/bin/env python3
"""128 fixed closed boxes with freshly reproduced same-cell phase resources.

The new output is not old INITIAL42 or LOCAL42 acceptance. The source-bound
last-stage replay remains conditional on the accepted v7 ancestors and the
analytic Fourier/contact premises. No stored success status is accepted.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from copy import deepcopy
import importlib.util,json,sys,subprocess,time,argparse,ast
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
SOURCES=HERE/'phase-confinement-sources'
MANIFEST_SHA='a3fcce0cf41c76fe02027e143e50adee521d297eb0938eebd89c21c46f12870e'
BASE_SHA='2ef7e9c9eb28482af904ad502ebd5044e612d364a449e42f89a44a7586ff4bce'
C0,C1=F('.4097321837023'),F('.4097321837025')

def need(ok,why):
 if not ok:raise ValueError(why)
def unique(pairs):
 d={}
 for k,v in pairs:need(k not in d,'duplicate JSON key');d[k]=v
 return d
def decode(x):
 if isinstance(x,str):
  try:return F(x)
  except ValueError:return x
 if isinstance(x,dict):return {k:decode(v)for k,v in x.items()}
 if isinstance(x,list):return [decode(v)for v in x]
 return x
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encode(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v)for v in x]
 return x

def source_bound_replay(evidence):
 need(__debug__ and not sys.flags.optimize,'unoptimized interpreter')
 blob=(SOURCES/'manifest.json').read_bytes();need(sha256(blob).hexdigest()==MANIFEST_SHA,'frozen manifest')
 pins=json.loads(blob,object_pairs_hook=unique)
 for name,digest in pins.items():need(sha256((SOURCES/name).read_bytes()).hexdigest()==digest,'source/object pin '+name)
 verify_instrumentation()
 base=HERE/'confinement_check.py';need(sha256(base.read_bytes()).hexdigest()==BASE_SHA,'reviewed confinement source')
 spec=importlib.util.spec_from_file_location('confinement_base',base);C=importlib.util.module_from_spec(spec);spec.loader.exec_module(C)
 replay=SOURCES/'replay-root/mathematics/fixed-target-v8/2026-10-28/phase_probe.py'
 args=[sys.executable,'-B',str(replay)];start=time.time();p=subprocess.run(args,capture_output=True)
 (evidence/'producer-stdout.json').write_bytes(p.stdout);(evidence/'producer-stderr.txt').write_bytes(p.stderr)
 receipt=dict(argv=args,cwd=str(Path.cwd()),returncode=p.returncode,elapsed_seconds=time.time()-start,
  source_manifest_sha256=MANIFEST_SHA,stdout_sha256=sha256(p.stdout).hexdigest(),stderr_sha256=sha256(p.stderr).hexdigest())
 (evidence/'producer-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
 need(p.returncode==0,'fresh source-bound final-stage replay')
 saved=json.loads((SOURCES/'phase-coefficients.json').read_text(),object_pairs_hook=unique)
 fresh=json.loads(p.stdout,object_pairs_hook=unique)
 validate_replay(saved,fresh)
 return C,decode(fresh),pins,receipt

def verify_instrumentation():
 root=SOURCES/'replay-root'
 code=(root/'mathematics/fixed-target-v8/2026-10-28/build_phase_core.py').read_text()
 assignments=[n for n in ast.parse(code).body if isinstance(n,ast.Assign)
              and any(isinstance(t,ast.Name) and t.id=='patches' for t in n.targets)]
 need(len(assignments)==1,'literal producer patch list')
 patches=ast.literal_eval(assignments[0].value)
 source=(root/'mathematics/fixed-target-v7/2026-10-27/signed_core.py').read_text()
 result=source
 for before,after in patches:
  need(result.count(before)==1,'unique forward producer edit');result=result.replace(before,after)
 need(result==(root/'mathematics/fixed-target-v8/2026-10-28/phase_core.py').read_text(),'export-only producer reconstruction')
 for before,after in reversed(patches):
  need(result.count(after)==1,'unique reverse producer edit');result=result.replace(after,before)
 need(result==source,'original producer recovered byte-for-byte')

def validate_replay(saved,fresh):
 for name in ('source_proof_sha256','total_cells','active_cells','rows','phase_cells'):
  need(saved[name]==fresh[name],'recomputed phase field '+name)
 need(fresh['total_cells']==2048 and fresh['active_cells']==len(fresh['phase_cells'])==682,'complete final-stage census')


def validate_coefficients(cells):
 source=json.loads((SOURCES/'replay-root/mathematics/fixed-target-v7/2026-10-27/entry-proof.json').read_text(),object_pairs_hook=unique)
 prior={1+F(3361*i,96000):F(r['raw'])for i,r in enumerate(source['steps'][2])if not r.get('prior_excluded')}
 for cell in cells:
  rl,rh=cell['rho'];gl,gu=cell['gamma'];pl,pu=cell['pl'],cell['pu']
  need(1<=rl<rh and 0<pl<=pu<1 and cell['H']>=0,'moment/phase domains')
  need(len(cell['quadratics'])==2 and [q['c']for q in cell['quadratics']]==[C0,C1],'both fixed-target endpoints')
  need(cell['density']==[F(997,2500)*(1-prior[rl]/(42*C0*rl)),F(2,5)],'ordered density license')
  need(cell['eta']==(C0*rl-cell['raw']/42)/2>0 and 0<=cell['raw']<=prior[rl],'same-cell phase price')
  for q in cell['quadratics']:
   c=q['c'];vals=[c*k+v*w for k in cell['K1']for v in cell['density']for w in cell['W']]
   need(q['B']==cell['Fourier']+c*cell['A'],'constant reconstruction')
   need(q['plus']==max(vals)+cell['slope']and q['minus']==-min(vals)+cell['slope'],'signed linear reconstruction')
   need(q['absolute']==max(abs(x)for x in vals)+cell['slope'],'absolute reference reconstruction')
   need(q['Q']==c*rl+min(v*gl/2 for v in cell['density'])+cell['eta']>0,'resource curvature reconstruction')
   need(q['plus']<=q['absolute']and q['minus']<=q['absolute'],'signed bound fits original')
 return len(cells)*2


def rectangle_resource(C,cells,hl,hh,ll,lh,sign):
 """Max over every possibly incident cell, then every actual phase in it."""
 need(0<=hl<=hh and 0<=ll<=lh and sign in (-1,1),'closed rectangle domain')
 vl,vh=C.vl,C.vh;theta=lh/(C.N*vl+lh)
 ml=C.sqrt_lo(vl*vl/(vl+lh/C.N));mu=C.sqrt_hi(vh)
 beta_lo=1-2*C.h-2*(1-C.l)*theta;beta_hi=1-2*C.l+2*C.h*theta
 eligible=[];selected='plus'if sign==1 else'minus'
 for i,cell in enumerate(cells):
  if cell['pu']<C.l or cell['pl']>C.h or cell['H']<hl:continue
  if cell['m'][1]<ml or cell['m'][0]>mu or cell['beta'][1]<beta_lo or cell['beta'][0]>beta_hi:continue
  end=min(hh,cell['H']);need(hl<=end,'clipped nonempty phase interval')
  maxima=[]
  for q in cell['quadratics']:
   B,f,Q=q['B'],q[selected],q['Q'];need(Q>0,'strict concavity')
   values=[B+f*x-Q*x*x for x in (hl,end)]
   vertex=f/(2*Q)
   if hl<=vertex<=end:values.append(B+f*vertex-Q*vertex*vertex)
   maxima.append(max(values))
  eligible.append((min(cell['raw'],max(maxima)),i))
 if not eligible:return dict(empty=True,cells=0)
 ceiling,winner=max(eligible)
 return dict(empty=False,cells=len(eligible),U=ceiling,winner=winner,m_range=[ml,mu],beta_range=[beta_lo,beta_hi],theta_upper=theta)

def diagnostic(moment,cells,C):
 """Independent exact evaluation of the parameterized retained inequalities."""
 need(0<d0<R0<SIGMA and 1-SIGMA-2*d0>0,'initial strip geometry')
 need(d0+2*TAU<R0 and 1-d0-TAU>0 and 1-2*d0-2*TAU>0,'upper interval geometry')
 buffer=F(1,100000)
 need(SIGMA+d0<1-d0 and SIGMA+d0-TAU-buffer<1-d0,'strict lower interval widths')
 need(24**2*vl**3>(3*(1-l)+SIGMA)**2,'conditional cubic coefficient')
 fd=F(1037,1000)
 need(fd*fd>max(F(N,N-1)**3,F(N,N-2)),'two deleted-index factors')
 rL=l-(1-l)/(N-2);rR=h+h/(N-2)
 need(0<rL<rR<1,'binomial modes')
 vs=min(rL*(1-rL),rR*(1-rR))
 M=sqrt_hi(F(4,25)/(vs*(1-F(1,12*(N-2)))**2))
 cp=2*F('5.16')*E*E*(1-h-d0)**2
 cm=2*F('7.16')*E*E*(l-d0)**2
 bs=min(3*F('4.16')*E*(1-h-d0),3*F('6.16')*E*(l-d0))
 alpha=min(cp*l*E,cm*(1-h)*E)
 need(min(cp,cm,bs,alpha)>0,'single resource coefficients')
 eta_phase=(CL-T/N)/2
 need(eta_phase>0,'raw Gaussian license and phase price')
 f=F(2,5)*FL;Bstar=F(6,5)
 need(Bstar*Bstar>(1-l)/l,'positive half-line physical endpoint')
 a_e=fd*M*(1/l+1/(1-h))/2
 g=1-SIGMA-2*d0
 records=[]
 for sign in (1,-1):
  for j in range(8):
   hl,hh=HMAX*F(j,8),HMAX*F(j+1,8)
   for k in range(8):
    ll,lh=LAMBDA*F(k,8),LAMBDA*F(k+1,8)
    rhostar=min(rho0,moment['skeleton_rho_upper']+24*lh/N)
    bm,bp=moment['beta_lower'],moment['beta_upper']
    philo=F('0.39886')*(1-hh*hh/(2*N));need(philo>0,'density lower bound')
    vplus=F(2,5)*hh if sign==1 else -philo*hl
    need(vplus+3*CU*rhostar>0,'negative-side square-completion direction')
    minus=FL*pos((vplus+3*CU*rhostar)**2/(12*CL)-3*CL*bm)
    plus=FL*pos(F(2,5)*hh*Bstar+3*CU*Bstar*(Bstar-1)-3*CL*bm)
    Lgap=E*philo-max(minus,plus)/N
    Uplus=f+FL/N*(3*CU*bp+(F(2,5)*hh+3*CU*rhostar)**2/(12*CL))
    tstar=-E*(l+TAU+buffer)
    vertex=min(tstar,-rhostar/2)
    Bmin=bm+rhostar*vertex+vertex*vertex
    vertex2=min(tstar,-(vplus+3*CL*rhostar)/(6*CL))
    qmin=3*CL*(bm+rhostar*vertex2+vertex2*vertex2)+vplus*vertex2+3*(CU-CL)*min(F(0),Bmin)
    L=E*philo-FL*pos(-qmin)/N
    need(L>0 and Lgap>0 and Uplus>0,'slope positivity')
    resource=rectangle_resource(C,cells,hl,hh,ll,lh,sign)
    base=dict(sign=sign,phase=[hl,hh],noise=[ll,lh],phase_resource=resource)
    if resource['empty']:
     records.append(dict(**base,resource_excluded=True,reason='no incident actual moment cell'));continue
    budget=resource['U']
    if budget<0:
     records.append(dict(**base,resource_excluded=True,reason='negative whole-rectangle joint resource'));continue
    remaining=budget/KAPPA-bs*E*E*ll
    base['budget']=budget
    if remaining<0:
     records.append(dict(**base,resource_excluded=True,reason='noise cost exceeds joint resource'));continue
    G=remaining/alpha
    bad=min(lh/(lh+N*l*TAU*TAU),G/(N*TAU+G))
    sides=[]
    for side in ('lower','upper'):
     if side=='lower':
      vH=-hl/FL if sign==1 else hh/E
      DI=pos(vH-l-TAU-buffer);DJ=pos(vH+1-l-buffer)
      ad,aJ=L,1/g;lhs=L*(R0-TAU-buffer)
     else:
      DI=pos(d0+TAU+hh/E-l);DJ=pos(1+d0+2*TAU+hh/E-l)
      ad,aJ=Lgap+Uplus,1/TAU;lhs=Lgap-SIGMA*Uplus
     AA=fd*M*(DI/l+DJ/(1-h));BB=fd*M
     z=max((ad/l+2*a_e)/(E*cp),(ad/(1-h)+2*a_e)/(E*cm),KAPPA*aJ/(1-TH))
     need(z*remaining+AA>0,'inverse-index sign')
     errors=[(z*remaining+AA)/N+BB*bad]
     vertices=[((ad/l+2*a_e)/(E*cp)*remaining/N,remaining/(E*cp*l)),
               ((ad/(1-h)+2*a_e)/(E*cm)*remaining/N,remaining/(E*cm*(1-h))),
               (KAPPA*aJ/(1-TH)*remaining/N,F(0))]
     for kk in range(11):
      tangent=F(kk,10)*G
      slope=N*TAU/(N*TAU+tangent)**2;intercept=tangent*tangent/(N*TAU+tangent)**2
      errors.append(AA/N+max(v+BB*slope*w for v,w in vertices)+BB*intercept)
     error=min(errors)
     sides.append(dict(side=side,lhs=lhs,error=error,margin=lhs-error,passed=lhs>error))
    records.append(dict(**base,resource_excluded=False,sides=sides))
 all_sides=[dict(sign=z['sign'],phase=z['phase'],noise=z['noise'],**s) for z in records if not z['resource_excluded'] for s in z['sides']]
 worst=min(all_sides,key=lambda s:s['margin'])
 failed=sum(not s['passed'] for s in all_sides)
 return dict(target_amplitude=R0,phase_cells=8,noise_cells=8,signs=2,boxes=len(records),
     resource_excluded=sum(z['resource_excluded'] for z in records),ray_gates=len(all_sides),failed_ray_gates=failed,
     complete_confinement_pass=(failed==0),worst=worst,records=records,
     scope='Same-cell resource diagnostic only; a failed sufficient bound is not a counterexample.')


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--evidence',type=Path,required=True);args=ap.parse_args()
 args.evidence.mkdir(parents=True,exist_ok=True)
 need(not(args.evidence/'producer-stdout.json').exists(),'distinct evidence identifier')
 C,data,pins,producer=source_bound_replay(args.evidence)
 # Existing small analytic component is reused, not represented as an independent review.
 for name in ('N','SL','CL','CU','l','h','vl','vh','D','TH0','TH','d0','R','rho0','E','FL','SIGMA','R0','TAU','T','HMAX','LAMBDA','KAPPA','sqrt_hi','pos'):
  globals()[name]=getattr(C,name)
 cells=data['phase_cells'];coefficient_checks=validate_coefficients(cells)
 moment=C.moment_chain();C.heat_boundary(F(9,5),-moment['beta_lower']);C.heat_boundary(F(93,40),moment['beta_upper'])
 out=diagnostic(moment,cells,C)
 need(out['boxes']==128 and out['phase_cells']==out['noise_cells']==8 and out['signs']==2,'fixed full rectangle cover')
 controls=[]
 def reject(name,fn):
  try:fn()
  except (ValueError,KeyError):controls.append(name)
  else:raise ValueError('invalid object accepted '+name)
 saved=json.loads((SOURCES/'phase-coefficients.json').read_text(),object_pairs_hook=unique)
 fresh=json.loads((args.evidence/'producer-stdout.json').read_text(),object_pairs_hook=unique)
 bad=deepcopy(saved);bad['phase_cells'].pop();reject('missing active box',lambda:validate_replay(bad,fresh))
 bad=deepcopy(saved);bad['phase_cells'][1]=bad['phase_cells'][0];reject('duplicate active box',lambda:validate_replay(bad,fresh))
 bad=deepcopy(saved);bad['phase_cells'].reverse();reject('reordered active boxes',lambda:validate_replay(bad,fresh))
 bad=deepcopy(cells);q=next(x['quadratics'][0]for x in bad if x['quadratics'][0]['plus']!=x['quadratics'][0]['minus']);q['plus'],q['minus']=q['minus'],q['plus'];reject('swapped phase signs',lambda:validate_coefficients(bad))
 bad=deepcopy(cells);bad[0]['quadratics'][0]['Q']+=1;reject('changed curvature',lambda:validate_coefficients(bad))
 bad=deepcopy(cells);bad[0]['eta']=F(0);reject('unlicensed phase price',lambda:validate_coefficients(bad))
 reject('reversed phase interval',lambda:rectangle_resource(C,cells,F(2),F(1),F(0),F(1),1))
 reject('negative noise ceiling',lambda:rectangle_resource(C,cells,F(0),F(1),F(-1),F(-1),1))
 reject('duplicate JSON key',lambda:json.loads('{"a":1,"a":2}',object_pairs_hook=unique))
 if out['failed_ray_gates']:reject('false whole-panel half-amplitude pass',lambda:need(out['complete_confinement_pass'],'remaining strict gates'))
 print(json.dumps(encode(dict(status='PASS_RESOURCE_JOIN_DIAGNOSTIC'if not out['complete_confinement_pass']else'PASS_CONDITIONAL_PANEL_HALF_AMPLITUDE',
  mathematical_status='Conditional on fixed-target contact, sharp predecessor, accepted v7 ancestors and analytic raw Fourier bounds; no global or finite-base theorem.',
  coefficient_reconstructions=coefficient_checks,source_manifest_sha256=MANIFEST_SHA,base_source_sha256=BASE_SHA,
  fresh_producer=producer,negative_controls=controls,diagnostic=out)),indent=2,sort_keys=True))
if __name__=='__main__':main()
