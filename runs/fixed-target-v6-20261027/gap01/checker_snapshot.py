#!/usr/bin/env python3
"""Six bounded full-HIGH updates using an already certified actual central gap."""
from pathlib import Path
from fractions import Fraction as F
import sys,json,importlib.util
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import combined_check as c
base=c.base

def run():
    need=c.need
    obj=json.loads((base.HERE/'cell-input.json').read_text(),object_pairs_hook=base.unique)
    first=base.run(obj,{name:(base.HERE/'cell-sources'/name).read_bytes() for name in base.PINS})
    import kernel as k
    import high_window_core as hw
    one,_=hw.install(k)
    c.cover(first['rows']);c0,c1=F(obj['c_lower']),F(obj['c_upper'])
    windows=(F(1,8),F(4,25),F(9,50),F(1,5),F(11,50),F(1,4))
    rows=[]
    for original in first['rows']:
        row=dict(original);l,u=row['rho_lower'],row['rho_upper']
        prior=c.step(row,c0,c1);trace=[]
        need(prior['central_gap_margin']>0,'actual central gap acquired before HIGH use')
        for j in range(1,7):
            need(prior['central_gap_margin']>0,'previous actual gap gate')
            gap2=prior['central_gap_squared_lower'];d0=k.roots(gap2)[0]
            event=1/(2*u*u);event_m=2/event
            candidates=[]
            for w in windows:
                bound,terms=one(42,event,event_m,d0,row['M4'],w)
                need(len(terms)==6 and all(t>0 for t in terms),'all six HIGH terms')
                candidates.append((bound,w,terms))
            high,w,terms=min(candidates,key=lambda t:t[0])
            selected=min(original['HIGH_bound'],high)
            low=original['LOW_L0_LH_L2']
            KF=F(16,25)*(low[0]+selected+low[2]/k.roots(F(42))[0])
            row['KF']=min(row['KF'],KF)
            current=c.step(row,c0,c1,prior)
            trace.append(dict(update=j,prior=prior,actual_gap_squared_lower=gap2,d0=d0,
                event_probability_lower=event,event_conditional_second_upper=event_m,
                HIGH_candidate=high,HIGH_window=w,HIGH_six_terms=terms,selected_HIGH=selected,
                KF=row['KF'],current=current))
            prior=current
        rows.append(dict(index=row['index'],rho_lower=l,rho_upper=u,steps=trace))
    summaries=[]
    for j in range(6):
        states=[r['steps'][j]['current'] for r in rows]
        summaries.append(dict(update=j+1,max_raw=max(s['raw'] for s in states),max_U=max(s['resource'] for s in states),
            max_D=max(s['defect'] for s in states),max_nD=max(s['weighted_nD'] for s in states),
            cells_D_below2=sum(s['defect']<2 for s in states),
            cells_actual_HIGH_improved=sum(r['steps'][j]['HIGH_candidate']<first['rows'][r['index']]['HIGH_bound'] for r in rows)))
    return dict(name='ACTUAL_GAP_FULL_HIGH_SIX_COARSE_UPDATES_V1',rows=rows,summaries=summaries,
        scope='Conditional on retained LOW and full six-piece HIGH theorem; actual gap is acquired first, no dense/local acceptance.')
if __name__=='__main__':print(json.dumps(base.encode(run()),indent=2))
