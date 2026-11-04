"""Floating discovery only: fixed quartic on each closed phase interval."""
from pathlib import Path
import hashlib,json,platform,sys,time
import numpy as np
import scipy
from scipy.optimize import linprog

C=.9819; A=.425; R0=1.06842; LF=.86879; HF=1.13121
TLO=.91595*.05; THI=1.08405*.08; J=9

def target(w,b):
    if w<b-J*C:return R0*(b-w)/C
    if w>b:return -1.
    return R0*max(0,int(np.floor((b-w)/C+1e-12)))

def solve(a,b):
    # Variables q0,...,q4,abs(q3),s. Minimize the worst loss divided by t.
    points=sorted(set(np.linspace(-10,10,401))|{b-j*C for j in range(J+1)}|{0.})
    flo=LF*a if a>=0 else HF*a
    for iteration in range(60):
        lhs=[[-1.,-w,-w*w,-w**3,-w**4,0.,0.] for w in points]
        rhs=[-target(w,b) for w in points]
        lhs += [[0,0,0,1,0,-1,0],[0,0,0,-1,0,-1,0]];rhs += [0.,0.]
        for t in (TLO,THI):
            lhs.append([1.,0.,t,0.,t*(A*A+3*t),A*t,-t]);rhs.append(flo)
        ans=linprog([0]*6+[1],A_ub=lhs,b_ub=rhs,
                    bounds=[(None,None)]*4+[(.001,None),(0,None),(None,None)],method='highs')
        if not ans.success:raise RuntimeError((a,b,ans.message))
        q=ans.x[:5];d=np.array([i*q[i] for i in range(1,5)])
        extra=[];minimum=0.
        for z in np.polynomial.polynomial.polyroots(d):
            if abs(z.imag)<1e-8 and z.real>=b-J*C:
                w=float(z.real);gap=np.polynomial.polynomial.polyval(w,q)-target(w,b)
                minimum=min(minimum,gap)
                if gap < -1e-6:extra.append(w)
        d[0]+=R0/C
        for z in np.polynomial.polynomial.polyroots(d):
            if abs(z.imag)<1e-8 and z.real<b-J*C:
                w=float(z.real);gap=np.polynomial.polynomial.polyval(w,q)-R0*(b-w)/C
                minimum=min(minimum,gap)
                if gap < -1e-6:extra.append(w)
        if not extra:
            return {'phase':[a,b],'q':q.tolist(),'sample_bound':float(ans.x[-1]),
                    'stationary_gap':float(minimum),'iterations':iteration+1}
        points.extend(extra)
    raise RuntimeError(('iteration limit',a,b))

def main():
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=False)
    start=time.monotonic()
    results=[]
    for i in range(200):
        results.append(solve((i-100)/200,(i-99)/200))
        if i%25==24:print(json.dumps({'completed':i+1,'worst':max(x['sample_bound'] for x in results)}),flush=True)
    result={'schema':'MID_QUARTIC_DISCOVERY_V1','scope':'FLOATING DISCOVERY ONLY',
      'constants':{'c':C,'A':A,'R0':R0,'lf':LF,'hf':HF,'t':[TLO,THI],'J':J},
      'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'results':results,'seconds':time.monotonic()-start}
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'worst_sample_bound':max(x['sample_bound'] for x in results)}))
if __name__=='__main__':main()
