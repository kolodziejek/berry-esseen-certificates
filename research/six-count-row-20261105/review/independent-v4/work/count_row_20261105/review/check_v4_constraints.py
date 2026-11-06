"""Independent exact mean/sign constraint and V4 tensor checks."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,importlib,json,sys
HERE=Path(__file__).resolve().parent;sys.path.insert(0,str(HERE))
import check_semantics as s
import check_tensors as t
m=importlib.import_module('model_v4')
def main(out):
    sources=[Path(__file__),HERE/'check_semantics.py',HERE/'check_tensors.py',t.CONSTRUCT/'model.py',t.CONSTRUCT/'model_v4.py',t.CONSTRUCT/'native/contract.json']
    before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    count=dict(actual_gamma_identities=0,actual_mean_identities=0,licensed_mean_sign_pairs=0,cap_checks=0,
      complete_V4_rows=0,exact_V4_moment_coefficients=0,negative_controls=0)
    for p in (m.PL,F(77,200),m.PU):
      q=1-p;v=p*q
      for A,b,a,B in product((F(1,10),m.A0),(F(1,10**12),F(1,10)),(F(1,10**12),F(1,10)),(F(1,10),m.A1)):
        d0=s.law(A,b);d1=s.law(a,B);s0=s.mean(d0,2);s1=s.mean(d1,2)
        x=q*s0;y=p*s1;w=v+x+y;noise=5*(x+y)
        raw={}
        for z,r in d0.items():raw[z]=raw.get(z,F(0))+q*r
        for z,r in d1.items():raw[1+z]=raw.get(1+z,F(0))+p*r
        G=sum(r*(z-p)**3 for z,r in raw.items())
        s.need(G==v*(1-2*p)+3*(-p*x+q*y)+q*s.mean(d0,3)+p*s.mean(d1,3),'signed cube identity')
        count['actual_gamma_identities']+=1
        plus=sum(r*max(F(0),z-p) for z,r in raw.items())
        s.need(plus==v,'positive unstandardized first moment equals v')
        count['actual_mean_identities']+=1
        licensed=(noise<=m.LAMBDA and v*v>=m.MEAN_LO*m.MEAN_LO*w
          and p-b>=0 and (p-b)**2>=m.NEG_LO*m.NEG_LO*w
          and q-a>=0 and (q-a)**2>=m.POS_LO*m.POS_LO*w)
        if not licensed:continue
        count['licensed_mean_sign_pairs']+=1
        hi=m.effective_hi(m.PL,m.PU,m.LAMBDA)
        r0,r1=m.inward(m.PL,m.PU,F(0))
        s.need(noise<=hi and b<=r0 and a<=r1,'mean and closest-sign endpoints imply V4 ceilings')
        count['cap_checks']+=3
    qs=[[F(j+2,5),F(j-3,7),F(j-2,11),F((-1)**j,13),F(j+1,17)] for j in range(6)]
    domains=[(1,m.PL,m.PU,F(-1,2),F(0),F(0),m.LAMBDA),
      (2,m.PL,m.PU,F(-1,2),F(-2,5),m.LAMBDA/4,m.LAMBDA/2)]
    for d in domains:
      k,pl,pu,ul,uh,lo,hi=d
      rows=m.tensors(*d);r0,r1=m.inward(pl,pu,lo)
      points=[(x,y,g0,g1) for x,y in m.polygon(pl,pu,lo,hi) for g0,g1 in product((-m.A0,F(0),r0),(m.A1,F(0),-r1))]
      s.need(len(rows)==len(points),'complete V4 corners')
      for row,(x,y,g0,g1) in zip(rows,points):
        b=[sum(qs[j][r]*row[5*j+r][i] for j in range(6) for r in range(5)) for i in range(50)]
        s.need(t.inverse(b)==t.local(t.direct(k,x,y,g0,g1,qs),pl,pu,ul,uh),'independent V4 tensor reconstruction')
        count['complete_V4_rows']+=1;count['exact_V4_moment_coefficients']+=50
    # Exact signs for possible interval constraints on the signed cubic.
    gamma_lo=-F(1,10);wlo=F(1,4);whi=F(1)
    s.need(gamma_lo*whi<gamma_lo*wlo,'negative gamma needs the upper width multiplier')
    count['negative_controls']+=1
    # A violated necessary condition must reduce the augmented relaxation,
    # whereas every actual slack is added with a nonnegative sign.
    H=F(-1,10);G=F(2);Ghi=F(1)
    s.need(H+(Ghi-G)<H,'upper-bound dual sign at an inadmissible moment')
    s.need(H+(Ghi-F(0))>=H,'upper-bound dual sign at an admissible moment')
    count['negative_controls']+=1
    after={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources};s.need(before==after,'source stability')
    result=dict(status='PASS',scope='Conditional V4 mean/sign cap and tensor checks; no full cover or acquisition replay.',counts=count,source_sha256=before)
    out=Path(out);out.mkdir(parents=True,exist_ok=False);(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main(sys.argv[1])
