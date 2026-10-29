#!/usr/bin/env python3
"""Three new coarse updates, with raw and conserved-resource bounds distinct."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json,sys
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
if sha256((HERE/'cell_check.py').read_bytes()).hexdigest()!='6827a67e64cfea5b89d823ffd34821fa942b3c3add702ee9721c89d65f443aa5':
    raise ValueError('fixed first-cover constructor hash')
import cell_check as base
N=42;PHILO=F(997,2500);PHIUP=F(2,5);SIGMA_LO=F(3162277660,10**9)
def rounded(x):return F(base.upper(x,10))
def gate(T,l,density,D):
    base.need(T>=0 and T<N*F(base.EXPECTED['c_lower'])*l,'raw Gaussian-weight license')
    base.need(0<density<PHIUP and D>=0,'density and defect directions')
def evaluate(row,T,U,D,c0,c1,update):
    l,u=row['rho_lower'],row['rho_upper'];g=row['gamma_abs'];b=row['beta_abs'];M=row['M4']
    density=PHILO*(1-T/(N*c0*l));gate(T,l,density,D)
    # D is a previously licensed upper bound. No generic-gap event,
    # local signed fourth improvement, or support update is used here.
    gamma_lower=max(-g,SIGMA_LO*l-3-D)
    base.need(gamma_lower<=g,'this bounded experiment does not discard empty cells')
    difference=min(2*u,(1-SIGMA_LO)*l+3+D)
    base.need(difference>=0,'nonnegative upper bound on rho-gamma')
    A=min(row['A'],F(3,2)*b*(2*u+1)+F(3,2)*row['Gamma']*difference+
          F(3,8)*u*u*(u+1)+F(8,27)*u**3-l/2)
    base.need(A>0,'positive constant envelope')
    def terms(t):
        q=max(t*l-g/5,t*l+min(density*gamma_lower,PHIUP*gamma_lower)/2)
        f=t*row['K_abs']+row['normal_H_coefficient']+row['slope']
        base.need(q>0 and f>=0,'refined raw quadratic gates')
        return q,f
    raw_exact=max(row['KF']+t*A+terms(t)[1]**2/(4*terms(t)[0]) for t in (c0,c1))
    raw_next=min(T,rounded(raw_exact))
    extra=(c0*l-raw_next/N)/2
    base.need(extra>0,'new conserved phase curvature')
    resource_exact=max(row['KF']+t*A+terms(t)[1]**2/(4*(terms(t)[0]+extra)) for t in (c0,c1))
    resource_next=min(U,rounded(resource_exact))
    defect_next=min(D,rounded(6*resource_next/(N*PHILO)))
    base.need(raw_next<=T and resource_next<=U and defect_next<=D,'ordered contraction')
    return {'step':update,'prior_raw':T,'prior_resource':U,'prior_defect':D,'density_lower':density,
      'gamma_lower':gamma_lower,'rho_minus_gamma_upper':difference,'A_refined':A,
      'raw_exact':raw_exact,'raw':raw_next,'extra_curvature':extra,
      'resource_exact':resource_exact,'resource':resource_next,'defect':defect_next,
      'weighted_nD_upper':6*resource_next/PHILO}
def run():
    base.need(__debug__ and not sys.flags.optimize,'no optimized Python')
    obj=json.loads((HERE/'cell-input.json').read_text(),object_pairs_hook=base.unique)
    blobs={name:(HERE/'cell-sources'/name).read_bytes() for name in base.PINS}
    first=base.run(obj,blobs) # recompute, never trust a supplied output receipt
    c0,c1=F(obj['c_lower']),F(obj['c_upper'])
    rows=[]
    for row in first['rows']:
        T=rounded(row['fixed_raw']);U=T;D=rounded(6*U/(N*PHILO));trace=[]
        for j in range(3):
            result=evaluate(row,T,U,D,c0,c1,j+1);trace.append(result)
            T,U,D=result['raw'],result['resource'],result['defect']
        rows.append({'index':row['index'],'rho_lower':row['rho_lower'],'rho_upper':row['rho_upper'],
          'initial_raw':rounded(row['fixed_raw']),'initial_defect':rounded(6*rounded(row['fixed_raw'])/(N*PHILO)),
          'steps':trace})
    summaries=[]
    for j in range(3):
        summaries.append({'step':j+1,'max_raw':max(r['steps'][j]['raw'] for r in rows),
         'max_normalized_raw':max(r['steps'][j]['raw']/r['rho_lower'] for r in rows),
         'max_resource':max(r['steps'][j]['resource'] for r in rows),
         'max_defect':max(r['steps'][j]['defect'] for r in rows),
         'max_weighted_nD':max(r['steps'][j]['weighted_nD_upper'] for r in rows),
         'cells_defect_below_2':sum(r['steps'][j]['defect']<2 for r in rows),
         'cells_defect_below_4':sum(r['steps'][j]['defect']<4 for r in rows)})
    controls=[]
    for name,args in [('unlicensed raw',(N*c0,F(1),PHILO,F(1))),
                      ('negative defect',(F(1),F(1),PHILO,F(-1))),
                      ('density above normal upper',(F(1),F(1),F(1),F(1)))]:
        try:gate(*args)
        except ValueError:controls.append(name)
        else:raise ValueError('invalid refinement gate accepted')
    return {'name':'FIXED_C_RAW_RESOURCE_THREE_COARSE_UPDATES_V1','iterations':3,
      'scope':'New scalar calculation conditional on fixed-target conserved phase lemma and retained Fourier/moment inequalities; no dense signed stage.',
      'rounding':'Each retained raw/resource/defect upper is rounded upward to 1e-10.',
      'rows':rows,'summaries':summaries,'rejected_controls':controls}
if __name__=='__main__':print(json.dumps(base.encode(run()),indent=2,sort_keys=True))
