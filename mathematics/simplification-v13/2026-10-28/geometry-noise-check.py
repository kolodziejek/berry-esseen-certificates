"""Exact scalar acceptance for inward-moment geometric coercivity.

No inherited driver, count certificate or discovery output is executed.
The degree-eight inequalities follow from the displayed square-root chords
in geometry-noise.tex. All coefficients and divisions are rational.
"""
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
S=F(3162277660,10**9);Su=F(3162277661,10**9)
B=F('32.20665378');N=F(42);d=F(17,250)
oldU=F(77,125);vmin=F(3,16);Qmax=F(9,25);smax=oldU/N
checks={};roots=[]
def gate(name,value):
    assert name not in checks;checks[name]=F(value)
def add(a,b):return [(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))]
def scale(a,s):return [s*x for x in a]
def multiply(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c
def power(a,k):
    c=[F(1)]
    for _ in range(k):c=multiply(c,a)
    return c
def evaluate(a,x):
    y=F(0)
    for z in reversed(a):y=y*x+z
    return y
def bernstein(c,a,b):
    degree=len(c)-1
    return [sum((c[k]*sum((F(comb(k,j)*comb(i,j),comb(degree,j))*a**(k-j)*(b-a)**j for j in range(min(i,k)+1)),F(0)) for k in range(degree+1)),F(0)) for i in range(degree+1)]
def rootlo(x):
    unit=10**12;k=isqrt(x.numerator*unit**2//x.denominator)
    lo=F(k,unit);hi=F(k+1,unit)
    assert lo*lo<=x<hi*hi
    roots.append({'argument':str(x),'lower':str(lo),'upper':str(hi)})
    return lo
p=[F(0),F(1)];q=[F(1),F(-1)];v=multiply(p,q)
def Q(sigma):return add(add(scale(power(p,2),sigma+1),scale(power(q,2),sigma-1)),scale(v,-6))
ql=Q(S);qu=Q(Su)
gate('sqrt10_lower',10-S*S);gate('sqrt10_upper',Su*Su-10)
gate('d_below_one',1-d)
for x in [F(1,4),F(27,50)]:gate('Q_upper_at_'+str(x),Qmax-evaluate(qu,x))
assert smax==F(11,750)
for branch,problo in [(0,F(1,4)),(1,F(23,50))]:
    C=3*(S+3 if branch==0 else S+1)
    bb=Su+7 if branch==0 else Su+5
    kk=6*(1-d)*(S+1 if branch==0 else S-1)
    Y=C*problo-bb*d+2*rootlo(kk*problo)
    gate('H_lower_'+str(branch),Y-F(30,4))
gate('noise_monotonicity',30*(1-smax/(2*vmin))-3*Qmax/(2*vmin))
gate('critical_probability',F(16,5)-Su)
gate('near_critical_localization',F(23,20)**2*2*(6+2*S)-B)

def chord_polynomial(lam,branch,a,b):
    prob=p if branch==0 else q
    xa=a if branch==0 else 1-a;xb=b if branch==0 else 1-b
    kk=6*(1-d)*(S+1 if branch==0 else S-1)
    ya=2*rootlo(kk*xa);yb=2*rootlo(kk*xb)
    slope=(yb-ya)/(b-a);chord=[ya-slope*a,slope]
    yy=add(add(scale(prob,3*(S+3 if branch==0 else S+1)),
              [-(Su+7 if branch==0 else Su+5)*d]),chord)
    R=add(scale(multiply(v,ql),N),scale(yy,lam))
    P=add(scale(power(R,2),N**3),scale(power(add(scale(v,N),[lam]),3),-B**2))
    assert len(R)==5 and len(P)==9
    return R,P,chord

targets=[('global',F(1,4),F(27,50),F(9,25)),
         ('left',F(1,4),F(2,5),F(8,25)),
         ('below_third',F(1,4),F(1,3),F(1,4)),
         ('below_three_tenths',F(1,4),F(3,10),F(1,6))]
polynomials=[];coefficient_count=0;closed_cells=0
for name,a,b,lam in targets:
    for branch in [0,1]:
        R,P,chord=chord_polynomial(lam,branch,a,b)
        base=bernstein(R,a,b)
        assert min(base)>0
        coefficient_count+=len(base)
        pieces=4 if name=='global' and branch==1 else 1
        bounds=[a+(b-a)*F(i,pieces) for i in range(pieces+1)]
        assert bounds[0]==a and bounds[-1]==b and all(x<y for x,y in zip(bounds,bounds[1:]))
        data=[]
        for i,(x,y) in enumerate(zip(bounds,bounds[1:])):
            bc=bernstein(P,x,y);coefficient_count+=len(bc);closed_cells+=1
            assert min(bc)>0,(name,branch,i,min(bc))
            data.append({'interval':[str(x),str(y)],'coefficients':[str(z) for z in bc]})
        polynomials.append({'name':name,'branch':branch,'lambda_cap':str(lam),
            'probability_interval':[str(a),str(b)],'chord_coefficients':[str(z) for z in chord],
            'positive_base_coefficients':[str(z) for z in base],
            'squared_polynomial_coefficients':[str(z) for z in P], 'cells':data})

cutoffs=[]
for upper,maxn in [(F(3,10),84),(F(1,3),168),(F(7,20),262),
                   (F(3,8),657),(F(39,100),1530),(F(2,5),3598)]:
    qvalue=evaluate(ql,upper);vv=upper*(1-upper)
    gate('positive_Q_at_'+str(upper),qvalue)
    gate('index_cutoff_'+str(upper),(maxn+1)**2*qvalue*qvalue-B*B*vv)
    cutoffs.append({'p_at_most':str(upper),'n_at_most':maxn})

# Negative controls for important directions and scope.
x=F(13,40)
# A tangent is an upper, not lower, support for sqrt; its misuse rejects.
tangent=1+(x-1)/2
assert tangent>0 and tangent*tangent>x
# Geometric monotonicity cannot be extended to arbitrary positive noise.
assert 30*(1-F(1)/(2*vmin))-3*Qmax/(2*vmin)<0
assert all(x>0 for x in checks.values()),{k:str(x) for k,x in checks.items() if x<=0}
here=Path(__file__).resolve();proof=here.with_name('geometry-noise.tex')
print(json.dumps({'status':'PASS_INWARD_MOMENT_GEOMETRY','scalar_gate_count':len(checks),
 'positive_Bernstein_coefficients':coefficient_count,'closed_polynomial_intervals':closed_cells,
 'checks':{k:str(x) for k,x in checks.items()},'root_enclosures':roots,
 'polynomials':polynomials,'index_cutoffs':cutoffs,
 'negative_controls':['sqrt_tangent_has_wrong_direction','unrestricted_noise_monotonicity_rejected'],
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest() if proof.exists() else None,
 'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),'python':sys.version,
 'scope':'Exact scalar consequences of the analytic inward-moment budget. '
 'No count, Fourier, contact, finite-base or global conjecture acceptance.'},indent=2))
