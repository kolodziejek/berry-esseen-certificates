"""Exact acceptance of the negative-inner compound-Poisson comparison.

Only this checker accepts the closed-box certificate. Discovery scripts and
their floating output are not mathematical inputs. All n>=42 are covered by
the proved separate concavity in eta=1/n, not by sampling n.
"""
from fractions import Fraction as F
from pathlib import Path
from math import comb,factorial
from functools import lru_cache
import itertools,json,hashlib,sys,time,copy
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')

ROOT=Path(__file__).resolve().parent
EVALUATOR_SHA='f23d657e0bc10b1d3334feeb65ccd43dd2d8b415e4a26fb0e6f7c3ddc853e582'
raw=(ROOT/'compound-evaluator.py').read_bytes()
assert hashlib.sha256(raw).hexdigest()==EVALUATOR_SHA
engine={'__name__':'pinned_compound_evaluator','__file__':str(ROOT/'compound-evaluator.py')}
exec(compile(raw,str(ROOT/'compound-evaluator.py'),'exec'),engine)
exp_bounds=engine['exp_bounds'];centered_tail=engine['centered_tail'];infinite_tail=engine['infinite_incoming_tail']
A=F(3,5);d=F(9,125);Xi=F(231,250);cv=F(5,2);v=F(6,25)
N=F(42);eta_hi=1/N;U=F(3,40);K0=F(79,25)

def rational(s):
    if not isinstance(s,str):raise ValueError('Canonical rational string required')
    x=F(s)
    if str(x)!=s:raise ValueError('Noncanonical rational representation')
    return x

def validate(document):
    if set(document)!={'format','domain','cells'} or document['format']!='compound-negative-inner-v12-1':raise ValueError('Unknown certificate schema')
    if document['domain']!=[['3/100','3/40'],['0','3/20'],['0','1']]:raise ValueError('Changed domain')
    if not isinstance(document['cells'],list) or not 1<=len(document['cells'])<=2000:raise ValueError('Cell limit or missing cells')
    cells=[]
    for row in document['cells']:
        if set(row)!={'box','method','alpha','hinge','later_anchors'}:raise ValueError('Malformed cell fields')
        if not isinstance(row['box'],list) or len(row['box'])!=6:raise ValueError('Malformed box')
        box=tuple(rational(x) for x in row['box'])
        l,L,rl,rh,wl,wh=box
        if not (F(3,100)<=l<L<=U and 0<=rl<rh<=F(3,20) and 0<=wl<wh<=1):raise ValueError('Box outside domain or degenerate')
        y=rational(row['hinge'])
        if not 0<=y<1+rl:raise ValueError('Hinge not admissible on complete box')
        if row['method']=='quartic':
            alpha=rational(row['alpha'])
            if alpha<=0:raise ValueError('Nonpositive quartic scale')
        elif row['method']=='cantelli':
            if row['alpha'] is not None:raise ValueError('Unexpected Cantelli parameter')
            alpha=None
        else:raise ValueError('Unknown own-count method')
        js=row['later_anchors']
        if not isinstance(js,list) or len(js)!=2 or any(not isinstance(j,int) or isinstance(j,bool) or j<2 for j in js):raise ValueError('Invalid later hinges')
        cells.append((box,alpha,y,tuple(js)))
    order=[c[0] for c in cells]
    if order!=sorted(set(order)):raise ValueError('Unsorted or duplicate boxes')
    # Common endpoint refinement verifies exact closed-domain coverage. Every
    # elementary open interior is covered once; closed faces come from cells.
    axes=[sorted({b[j] for b in order}|{b[j+1] for b in order}) for j in (0,2,4)]
    if [(a[0],a[-1]) for a in axes]!=[(F(3,100),U),(F(0),F(3,20)),(F(0),F(1))]:raise ValueError('Missing exterior face')
    index=[{x:i for i,x in enumerate(a)} for a in axes];covered=set()
    for box in order:
        intervals=[range(index[j][box[2*j]],index[j][box[2*j+1]]) for j in range(3)]
        for key in itertools.product(*intervals):
            if key in covered:raise ValueError('Overlapping interiors')
            covered.add(key)
    if len(covered)!=(len(axes[0])-1)*(len(axes[1])-1)*(len(axes[2])-1):raise ValueError('Uncovered elementary cell')
    return cells,len(covered)

def normal_gates():
    D=Xi+F(3,20);Z=lambda z:F(5,8)*z+F(3,8)+z**3/N
    gates={
      'sqrt_variance':F(251,500)**2-F(1,4)-U/N,
      'threshold':Xi-F(46,25)*F(251,500),
      'count_fraction_lower':F(2,5)-D/N-F(9,25),
      'count_fraction_upper':F(23,40)-F(53,100)-D/N,
      'interior_lower':N*F(2,5)-D-1,
      'interior_upper':N*F(47,100)-D-1,
      'stirling_variance':F(9,25)*F(16,25)-F(23,100),
      'stirling_entropy':6-F(7,25)/F(23,100)**2,
      'stirling_prefactor':F(5,4)-F(7,25)/F(23,100),
      'stirling_remainder':F(3,8)-1/(12*F(23,100)),
      'phi_lower':1-F(19943,50000)**2*F(44,7),
      'mode_mass':F(17,20)**2*v*(1-Z(1)/N)**2-F(2,5)**2,
      'normal_s_variation':N*v-D**2,
      'incoming_sign':1-Xi,
      'later_binomial_factors':2-F(53,100)-D,
      'own_count_frequencies':1-cv*D/N,
      'normal_repair':F(7,4)**2*v**3-F(1,5)**2,
      'cubic_coefficient':F(2,5)-K0*F(251,500)**3,
      'raw_cubic_difference':F(6,5)-d-F(39,50)-F(13,16)*U/N,
      'unit_cubic_gain':F(2,5)*(F(87,250)-F(13,16)*U/N)-F(251,500)**3,
      'quartic_minorant':F(11**2-36*3),
      'factorial_tail_ratio':6-F(5,2)*U/A**2,
      'cantelli_repair_sign':F(7,4)*Xi-1,
    }
    assert all(x>0 for x in gates.values()),{k:str(x) for k,x in gates.items() if x<=0}
    return gates

@lru_cache(maxsize=None)
def bernstein_matrix(lo,hi):
    return [[sum(F(comb(k,j)*comb(i,j),comb(4,j))*lo**(k-j)*(hi-lo)**j for j in range(min(i,k)+1)) for k in range(5)] for i in range(5)]

def context(box,y,anchors):
    l,L,rl,rh,wl,wh=box;D=Xi+rh
    Z=F(5,8)*D+F(3,8)+D**3/N
    mlo=2*F(19943,50000)*(1-(D*D/(2*v)+Z)/N)
    R=1+max(F(0),F(53,100)+D-1)/(N*v-F(3,5)*max(F(0),D-1))
    P=(2*Xi*rh+rh*rh)/(2*v)+Z
    _,eupper=exp_bounds(P/N);E=N*(eupper-1)
    # For negative phases delta=xi+r and xi>-Xi>-1. Thus the negative
    # group shrinks at every incoming count; only the positive group grows.
    T=L*(1+cv*(D+1)*eta_hi*wh)
    first=centered_tail(T,wl,1+rl,y)
    tail=first+infinite_tail(L,rl,first=4)
    for i,j in zip((2,3),anchors):
        mu=min(F(5,2)*L,L*(1+cv*(D+i)*eta_hi))/A**2
        denominator=(i+rl)/A+mu-j
        if denominator<=0:raise ValueError('Later hinge inadmissible')
        tail+=mu**(j+1)/(factorial(j+1)*denominator**2)
    assert 0<mlo<F(17,20) and R>0 and E>=0 and tail>=0
    return D,mlo,R,E,tail

def quartic_margin(box,alpha,ctx):
    l,L,rl,rh,wl,wh=box;D,mlo,R,E,tail=ctx
    M=5*alpha**4;matrix=bernstein_matrix(rl,rh);minimum=None
    for lam,w,eta,m,s0,s1,x0,x1 in itertools.product([l,L],[wl,wh],[F(0),eta_hi],[mlo,F(17,20)],[-1,1],[-1,1],[-A,d],[-d,A]):
        t0=lam*(1-w)*(1+s0*cv*Xi*eta);b0=lam*(1-w)*s0*cv*eta
        t1=lam*w*(1+s1*cv*Xi*eta);b1=lam*w*s1*cv*eta
        t=t0+t1;b=b0+b1;c=[F(0)]*5
        for x,tt,bb in [(x0,t0,b0),(x1,t1,b1)]:
            z=3*alpha**2-x*x
            c[0]+=z*tt;c[1]+=z*bb-4*x*tt
            c[2]+=-4*x*bb-6*tt;c[3]+=-6*bb
        c[0]-=3*t*t;c[1]-=6*t*b;c[2]-=3*b*b
        c[1]+=2*alpha**3;c[2]+=3*alpha**2;c[4]-=1
        c=[z*m/M for z in c]
        c[0]+=-m*R*tail+K0*eta*lam*(F(6,5)*(1-w)+F(141,100)*w-x0*(1-w)+x1*w-F(39,50)-F(13,16)*lam*eta)-F(7,4)*Xi*lam*eta
        c[1]+=-m*(1+E*eta)-F(7,4)*lam*eta
        bound=min(sum(a*z for a,z in zip(row,c)) for row in matrix)
        minimum=bound if minimum is None else min(minimum,bound)
    return minimum

def cantelli_margin(box,ctx):
    l,L,rl,rh,wl,wh=box;D,mlo,R,E,tail=ctx
    T=L*(1+cv*D/N);hf=1+E/N
    if rl<=0 or 2*rl*T/(T+rl*rl)**2<=hf:raise ValueError('Cantelli endpoint reduction not licensed')
    own=min(r*r/(T+r*r)-hf*r for r in (rl,rh))
    bracket=own-R*tail;m=mlo if bracket>=0 else F(17,20)
    return m*bracket-(F(7,4)*D-1)*L/N

def test_mutations(doc):
    bad=[]
    q=copy.deepcopy(doc);q['cells'].pop();bad.append(q)
    q=copy.deepcopy(doc);q['cells'].insert(0,q['cells'][0]);bad.append(q)
    q=copy.deepcopy(doc);q['cells'][0],q['cells'][1]=q['cells'][1],q['cells'][0];bad.append(q)
    q=copy.deepcopy(doc);q['cells'][0]['hinge']=str(1+F(q['cells'][0]['box'][2]));bad.append(q)
    q=copy.deepcopy(doc);q['cells'][0]['later_anchors'][0]=True;bad.append(q)
    q=copy.deepcopy(doc);q['cells'][0]['box'][0]='0.03';bad.append(q)
    q=copy.deepcopy(doc);q['cells'][0].pop('alpha');bad.append(q)
    for q in bad:
        try:validate(q)
        except (ValueError,KeyError,TypeError):pass
        else:raise AssertionError('Malformed certificate accepted')
    assert hashlib.sha256(raw+b'\n').hexdigest()!=EVALUATOR_SHA
    return len(bad)+1

if __name__=='__main__':
    certificate=ROOT/'compound-certificate.json';doc=json.loads(certificate.read_text())
    cells,elementary=validate(doc);gates=normal_gates();mutations=test_mutations(doc)
    start=time.monotonic();results=[]
    for i,(box,alpha,y,anchors) in enumerate(cells):
        ctx=context(box,y,anchors)
        margin=cantelli_margin(box,ctx) if alpha is None else quartic_margin(box,alpha,ctx)
        assert margin>0,{'cell':i,'box':[str(x) for x in box],'margin':str(margin)}
        rounded=F(margin.numerator*10**12//margin.denominator,10**12)
        assert rounded>0
        results.append({'cell':i,'margin_lower':str(rounded)})
        if (i+1)%32==0:print(json.dumps({'accepted':i+1,'total':len(cells),'elapsed_seconds':time.monotonic()-start}),file=sys.stderr,flush=True)
    print(json.dumps({'status':'PASS_UNIFORM_NEGATIVE_INNER_COMPOUND_COMPARISON','scope':'n>=42,p in [.4,.53], .6 strip,d<=.072,|H|<=1.84,C>=.4,lambda in [.03,.075],phase in [-.15,0]; exact physical variance allocation retained. Other phases require separate proved joins.','cell_count':len(cells),'elementary_coverage_cells':elementary,'normal_gates':{k:str(x) for k,x in gates.items()},'negative_controls':mutations,'evaluator_sha256':EVALUATOR_SHA,'certificate_sha256':hashlib.sha256(certificate.read_bytes()).hexdigest(),'minimum_margin_lower':str(min(F(x['margin_lower']) for x in results)),'cell_margins':results,'elapsed_seconds':time.monotonic()-start,'python':sys.version},indent=2))
