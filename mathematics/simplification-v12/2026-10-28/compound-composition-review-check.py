"""Independent reconstruction of all negative-inner certificate margins.

No constructor is imported or executed. Hinge expectations use a pgf
recurrence; degree-four Bernstein functionals use exact interpolation; the
support endpoints are minimized analytically coefficient by coefficient.
Coverage/schema have a separate independent geometry review. This program
checks the pinned domain, canonical box data and exact total volume only.
"""
from fractions import Fraction as F
from math import comb, factorial
from functools import lru_cache
from pathlib import Path
import hashlib,itertools,json,sys,time
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
A=F(3,5);d=F(9,125);h=F(3,125);XI=F(231,250);N=42;V=F(6,25);K0=F(79,25)
PINS={'compound-proof.tex':'5b9d8428b6aa10bc3fff44114cd26c482b88692f76dd624b841c79d5b4a753fa',
'compound-accept.py':'f98de164169fae176644737b8b68b72044837db2a19dbba26602cea279c3d611',
'compound-evaluator.py':'f23d657e0bc10b1d3334feeb65ccd43dd2d8b415e4a26fb0e6f7c3ddc853e582',
'compound-certificate.json':'e3baf63f96f5f7fd6e7f9c6dae1e75448f9f588524e164fdf8c0b2e770ea6a0c'}

@lru_cache(maxsize=None)
def exp_positive(x):
    assert x>=0
    if not x:return F(1),F(1)
    degree=max(80,3*(x.numerator//x.denominator+1))
    t=F(1);total=t
    for j in range(1,degree+1):t*=x/j;total+=t
    omitted=t*x/(degree+1)
    return total,total+omitted/(1-x/F(degree+2))

@lru_cache(maxsize=None)
def hinge_upper(T,w,y):
    mu=T*(1-w)/A**2;nu=T*w/d**2;K=(y+A*mu+d*nu)/h
    assert mu>=0 and nu>=0 and K>=0
    coefficients=[F(1)]
    for j in range(1,K.numerator//K.denominator+1):
        coefficients.append(((25*mu*coefficients[j-25] if j>=25 else F(0))+
                             (3*nu*coefficients[j-3] if j>=3 else F(0)))/F(j))
    deficit=sum((K-j)**2*c for j,c in enumerate(coefficients))
    _,ehi=exp_positive(mu+nu)
    upper=625*mu+9*nu+(25*mu+3*nu-K)**2-deficit/ehi
    assert upper>=0
    return h*h*upper

@lru_cache(maxsize=None)
def context(box,y,anchors):
    l,L,rl,rh,wl,wh=box;D=XI+rh
    Z=F(5,8)*D+F(3,8)+D**3/N
    mlo=2*F(19943,50000)*(1-(D*D/(2*V)+Z)/N)
    R=1+max(F(0),F(53,100)+D-1)/(N*V-F(3,5)*max(F(0),D-1))
    P=(2*XI*rh+rh*rh)/(2*V)+Z
    _,exphi=exp_positive(P/N);E=N*(exphi-1)
    T=L*(1+F(5,2)*(D+1)*wh/N)
    assert 0<=y<1+rl
    tail=min(F(1),hinge_upper(T,wl,y)/(1+rl-y)**2)
    for i,j in zip([2,3],anchors):
        mu=min(F(5,2)*L,L*(1+F(5,2)*(D+i)/N))/A**2
        den=(i+rl)/A+mu-j
        assert j>=2 and den>0
        tail+=mu**(j+1)/(factorial(j+1)*den**2)
    mu=F(5,2)*L/A**2;den=4*(1/A-1)+rl/A+mu
    assert den>0 and mu<6
    tail+=mu**5/(120*den**2*(1-mu/6))
    assert 0<mlo<F(17,20) and R>0 and E>=0
    return mlo,R,E,tail

def inverse(a):
    n=len(a);z=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        i=next(i for i in range(j,n) if z[i][j]);z[j],z[i]=z[i],z[j]
        v=z[j][j];z[j]=[x/v for x in z[j]]
        for i in range(n):
            if i!=j:
                v=z[i][j];z[i]=[x-v*y for x,y in zip(z[i],z[j])]
    assert all(z[i][j]==F(i==j) for i in range(n) for j in range(n))
    return [row[n:] for row in z]

INV=inverse([[F(comb(4,j))*F(i,4)**j*(1-F(i,4))**(4-j) for j in range(5)] for i in range(5)])
@lru_cache(maxsize=None)
def functionals(rl,rh):
    nodes=[rl+(rh-rl)*F(j,4) for j in range(5)]
    return tuple(tuple(sum(INV[i][j]*nodes[j]**k for j in range(5)) for k in range(5)) for i in range(5))

def quartic(box,alpha,ctx):
    l,L,rl,rh,wl,wh=box;mlo,R,E,tail=ctx;M=5*alpha**4
    H=functionals(rl,rh);minimum=None;corners=0
    for lam,w,eta in itertools.product([l,L],[wl,wh],[F(0),F(1,N)]):
        lam0=lam*(1-w);lam1=lam*w
        # Collapse duplicate noise-factor corners at eta=0 or a zero group.
        variances=set()
        for sign0,sign1 in itertools.product([-1,1],repeat=2):
            a0=lam0*(1+sign0*F(5,2)*XI*eta);b0=lam0*sign0*F(5,2)*eta
            a1=lam1*(1+sign1*F(5,2)*XI*eta);b1=lam1*sign1*F(5,2)*eta
            variances.add((a0,b0,a1,b1))
        for a0,b0,a1,b1 in variances:
          a=a0+a1;b=b0+b1
          for m in [mlo,F(17,20)]:
            corners+=1
            for row in H:
                one,r,r2,r3,r4=row;assert one==1
                betaT0=a0+b0*r;betaT1=a1+b1*r
                betaRT0=a0*r+b0*r2;betaRT1=a1*r+b1*r2
                assert betaT0>=0 and betaT1>=0
                # Apply the coefficient functional to the original own-count
                # expectation before minimizing either support endpoint.
                base=3*alpha**2*(a+b*r)-6*(a*r2+b*r3)-3*(a*a+2*a*b*r+b*b*r2)-r4+3*alpha**2*r2+2*alpha**3*r
                total=m*base/M-m*R*tail-m*(1+E*eta)*r
                total+=K0*eta*lam*(F(6,5)*(1-w)+F(141,100)*w-F(39,50)-F(13,16)*lam*eta)
                total-=F(7,4)*lam*eta*(XI+r)
                price0=max(m*(x*x*betaT0+4*x*betaRT0)/M+K0*eta*lam0*x for x in [-A,d])
                price1=max(m*(x*x*betaT1+4*x*betaRT1)/M-K0*eta*lam1*x for x in [-d,A])
                bound=total-price0-price1
                minimum=bound if minimum is None else min(minimum,bound)
    return minimum,corners

def cantelli(box,ctx):
    l,L,rl,rh,wl,wh=box;mlo,R,E,tail=ctx;D=XI+rh
    T=L*(1+F(5,2)*D/N);slope=1+E/N
    assert rl>0 and 2*rl*T/(T+rl*rl)**2>slope
    own=min(r*r/(T+r*r)-slope*r for r in [rl,rh])
    bracket=own-R*tail
    m=mlo if bracket>=0 else F(17,20)
    return m*bracket-(F(7,4)*D-1)*L/N

def parse(root):
    source=root/'mathematics/simplification-v12/2026-10-28'
    for name,pin in PINS.items():assert hashlib.sha256((source/name).read_bytes()).hexdigest()==pin,name
    doc=json.loads((source/'compound-certificate.json').read_text())
    assert doc['format']=='compound-negative-inner-v12-1'
    assert doc['domain']==[['3/100','3/40'],['0','3/20'],['0','1']]
    cells=[];volume=F(0)
    for row in doc['cells']:
        box=tuple(F(x) for x in row['box']);assert [str(x) for x in box]==row['box']
        l,L,rl,rh,wl,wh=box
        assert F(3,100)<=l<L<=F(3,40) and 0<=rl<rh<=F(3,20) and 0<=wl<wh<=1
        volume+=(L-l)*(rh-rl)*(wh-wl)
        y=F(row['hinge']);anchors=tuple(row['later_anchors'])
        assert 0<=y<1+rl and len(anchors)==2 and all(type(j) is int and j>=2 for j in anchors)
        alpha=F(row['alpha']) if row['method']=='quartic' else None
        assert (alpha is not None and alpha>0) or (row['method']=='cantelli' and row['alpha'] is None)
        cells.append((box,alpha,y,anchors))
    assert len(cells)==291 and sum(c[1] is not None for c in cells)==200
    assert [c[0] for c in cells]==sorted(set(c[0] for c in cells))
    assert volume==(F(3,40)-F(3,100))*F(3,20)
    return cells

def preflight():
    U=F(3,40);D=XI+F(3,20);Z1=F(5,8)+F(3,8)+F(1,N)
    gates={
      'raw_variance_cap':F(251,500)**2-F(1,4)-U/N,
      'xi_cap':XI-F(46,25)*F(251,500),
      'count_fraction_left':F(2,5)-D/N-F(9,25),
      'count_fraction_right':F(23,40)-F(53,100)-D/N,
      'entropy_third_derivative':6-F(7,25)/F(23,100)**2,
      'log_prefactor_derivative':F(5,4)-F(7,25)/F(23,100),
      'factorial_remainder':F(3,8)-1/(12*F(23,100)),
      'phi_lower_from_pi_upper':1-2*F(355,113)*F(19943,50000)**2,
      'phi_upper_from_pi_lower':2*F(157,50)*F(2,5)**2-1,
      'mode_mass_upper':F(17,20)**2*V*(1-Z1/N)**2-F(2,5)**2,
      'normal_s_derivative_sign':N*V-D**2,
      'negative_incoming_group_shrinks':1-XI,
      'all_later_ratios_at_most_one':2-F(53,100)-D,
      'relaxed_g_factors_positive':1-F(5,2)*D/N,
      'normal_variance_repair':F(7,4)**2*V**3-F(1,5)**2,
      'cubic_coefficient_lower':F(2,5)-K0*F(251,500)**3,
      'raw_cubic_bracket_positive':F(6,5)-d-F(39,50)-F(13,16)*U/N,
      'unit_cubic_gain':F(2,5)*(F(87,250)-F(13,16)*U/N)-F(251,500)**3,
      'quartic_minorant':F(121-108),
      'factorial_tail_ratio':6-F(5,2)*U/A**2,
      'cantelli_repair_coefficient':F(7,4)*XI-1,
    }
    assert all(x>0 for x in gates.values()),{k:str(x) for k,x in gates.items() if x<=0}
    return gates

def main():
    if len(sys.argv)!=2:raise SystemExit('usage: compound-composition-review-check.py CONSTRUCTOR_REPO_ROOT')
    root=Path(sys.argv[1]).resolve();cells=parse(root);gates=preflight();start=time.monotonic();out=[];corners=0
    for i,(box,alpha,y,anchors) in enumerate(cells):
        ctx=context(box,y,anchors)
        if alpha is None:margin=cantelli(box,ctx)
        else:
            margin,count=quartic(box,alpha,ctx);corners+=count
        assert margin>0,{'cell':i,'margin':str(margin)}
        rounded=F(margin.numerator*10**12//margin.denominator,10**12)
        assert rounded>0
        out.append({'cell':i,'margin_lower':str(rounded)})
        if (i+1)%32==0:print(json.dumps({'independently_checked':i+1,'total':len(cells),'elapsed_seconds':time.monotonic()-start}),file=sys.stderr,flush=True)
    print(json.dumps({'status':'PASS_INDEPENDENT_COMPOUND_COMPOSITION_REPLAY','scope':'Negative phase [-.15,0],lambda in [.03,.075], all stated conditional-law premises; Delta_C<0, no lambda/100 rate claimed',
      'independent_preflight_gates':{k:str(v) for k,v in gates.items()},'cell_count':len(cells),'quartic_cells':200,'cantelli_cells':91,'deduplicated_variance_mass_corners':corners,
      'minimum_margin_lower':str(min(F(x['margin_lower']) for x in out)),'cell_margins':out,'reviewed_sources':PINS,
      'methods':{'hinge':'pgf recurrence with direct rational exponential series','polynomial':'five-point interpolation functionals applied to original moment expression','support':'separate exact endpoint-price maxima for each Bernstein coefficient','coverage':'pinned box sanity and exact total volume; full independent disjointness/coverage is the separate geometry review'},
      'elapsed_seconds':time.monotonic()-start,'python':sys.version},indent=2))

if __name__=='__main__':main()
