import numpy as np, math, itertools
from scipy.special import ndtr, gammaln
exec(open('experiments.py').read().split('# ---------------------------------------------------------------- experiment 1')[0])
def total_score(vals, probs, n):
    return scores(vals, probs, n)[1]
def skeleton_score(vals, probs, n):
    vals=np.asarray(vals,float); probs=np.asarray(probs,float)
    mu=(vals*probs).sum(); sd=math.sqrt(((vals-mu)**2*probs).sum()); x=(vals-mu)/sd
    p=probs[x>1e-12].sum()
    if p<=0 or p>=1: return None
    q=1-p; return total_score([-math.sqrt(p/q), math.sqrt(q/p)],[q,p],n)
rng=np.random.default_rng(7)
for n in [1,2,3,5,10,20,42]:
    viol=0; worst=-1; worst_score=0; best_viol_score=0; N=600 if n<=10 else 250
    for _ in range(N):
        m=rng.integers(3,6) if n<=20 else 3
        vals=np.sort(rng.normal(size=m)*rng.uniform(0.3,2)); probs=rng.dirichlet(np.ones(m)*rng.uniform(0.3,3))
        if probs.min()<1e-4: continue
        s=total_score(vals,probs,n); sk=skeleton_score(vals,probs,n)
        if sk is None: continue
        if s>sk+1e-12:
            viol+=1; best_viol_score=max(best_viol_score,s)
            if s-sk>worst: worst=s-sk
    print(f"n={n:3d}: {N} random 3-5 point laws; laws beating their own skeleton: {viol}; "
          f"largest excess {max(worst,0):.4f}; highest score among those laws {best_viol_score:.4f} (C_E={CE:.4f})")
