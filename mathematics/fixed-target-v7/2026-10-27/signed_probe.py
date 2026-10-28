#!/usr/bin/env python3
"""Bounded exploratory signed cover. Targets are reported, not weakened."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,importlib.util,argparse
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sys.path.insert(0,str(ROOT/'mathematics/fixed-target-v6/2026-10-27'))

import signed_core as s
import signed_support as support

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [encode(v) for v in x]
    return x

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--steps',type=int,default=1);ap.add_argument('--beta',type=int,default=4);ap.add_argument('--gamma',type=int,default=4);ap.add_argument('--mean',type=int,default=1);ap.add_argument('--cell-support',action='store_true');ap.add_argument('--initial',choices=['quadratic','full-phase'],default='quadratic');args=ap.parse_args()
    s.k.need(__debug__ and 1<=args.steps<=6 and 1<=args.beta*args.gamma*args.mean<=128,'bounded probe size')
    states=[]
    if args.initial=='quadratic':
        path=ROOT/'mathematics/fixed-target-v6/2026-10-27/signed-two-pass-check.py'
        spec=importlib.util.spec_from_file_location('v7_simple_initial',path);ancestor=importlib.util.module_from_spec(spec);spec.loader.exec_module(ancestor)
        initial=ancestor.run(path.parent/'moment_check.py')
        for row in initial['rows']:
            z=row['passes'][-1];states.append(dict(index=row['index'],l=row['rho_lower'],u=row['rho_upper'],raw=z['raw'],d=z['defect'],empty=False))
    else:
        import gap_check as ancestor
        initial=ancestor.run()
        for row in initial['rows']:
            z=row['steps'][-1]['current'];states.append(dict(index=row['index'],l=row['rho_lower'],u=row['rho_upper'],raw=z['raw'],d=z['defect'],empty=False))
    history=[];c0,c1=F('.4097321837023'),F('.4097321837025')
    for j in range(args.steps):
        rows=[]
        for state in states:
            if state['empty']:
                rows.append(dict(index=state['index'],prior_excluded=True));continue
            radius,beta_support,support_gates=support.cell_radius(state['u']) if args.cell_support else (F(96,25),None,None)
            p=dict(n=42,nmax=42,radius=radius,barrier=F(0),cap=c1,c_lower=c0,c_upper=c1,
                grid=[1,args.beta,args.gamma,args.mean],rho_lower=state['l'],rho_upper=state['u'])
            out=s.stage(p,state['raw'],state['d'])
            rows.append(dict(index=state['index'],prior_raw=state['raw'],prior_defect=state['d'],radius=radius,beta_support=beta_support,support_gates=support_gates,output=out))
            if out['active']:
                state['raw']=min(state['raw'],s.hi(out['R']));state['d']=min(state['d'],s.hi(out['D']))
            else:state['empty']=True
        active=[z for z in states if not z['empty']]
        summary=dict(step=j+1,max_raw=max(z['raw'] for z in active),max_D=max(z['d'] for z in active),
            remaining_rho_cells=len(active),rho_upper=max(z['u'] for z in active),
            cells_below2=sum(z['d']<2 for z in active),cells_below_target=sum(z['d']<F('.784') for z in active),
            tested_signed_cells=sum(z.get('output',{}).get('total',0) for z in rows),
            active_signed_cells=sum(z.get('output',{}).get('active',0) for z in rows))
        print(json.dumps(encode(summary)),file=sys.stderr,flush=True)
        history.append(dict(summary=summary,rows=rows))
    print(json.dumps(encode(dict(name='BOUNDED_FIXED_C_SIGNED_PROBE_V1',parameters=vars(args),
      status='EXPLORATORY_CONDITIONAL_COMPUTATION_NOT_ACCEPTED',history=history,final_states=states,
      scope='New fixed-target scalar transport under retained analytic moment/Fourier premises; no old INITIAL42 or LOCAL42 acceptance.')),indent=2))
if __name__=='__main__':main()
