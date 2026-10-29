"""Exact actual-law controls for the inward-moment geometric budget.

Every bounded support gap and its weight are computed from the actual law.
The separate Schulz-domain negative control reuses a pinned rational normal
kernel; it does not import an unproved extrapolation of Schulz's theorem.
"""
from fractions import Fraction as F
from math import isqrt,comb
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
def root(x):
    scale=10**60;k=isqrt(x.numerator*scale*scale//x.denominator)
    bounds=F(k,scale),F(k+1,scale)
    assert bounds[0]**2<=x<bounds[1]**2
    return bounds
sl,su=root(F(10));dmax=F(17,250)
def noise(var,side):
    if var==0:return [(F(0),F(1))]
    A=F(3,5) if side==0 else F(7,10);a=var/A
    return [(-A,a/(A+a)),(a,A/(A+a))] if side==0 else [(-a,A/(A+a)),(A,a/(A+a))]
def actual(p,n,lam,w):
    q=1-p;v=p*q;s=lam/n;variances=[s*(1-w)/q,s*w/p]
    noises=[noise(variances[0],0),noise(variances[1],1)]
    a0=max(x for x,_ in noises[0]);a1=max(-x for x,_ in noises[1]);d=a0+a1
    atoms={}
    for side,zs in enumerate(noises):
        assert sum(m for _,m in zs)==1 and sum(x*m for x,m in zs)==0
        for x,m in zs:
            z=side+x-p;atoms[z]=atoms.get(z,F(0))+(q if side==0 else p)*m
    atoms=sorted(atoms.items());V=sum(z*z*m for z,m in atoms)
    assert sum(z*m for z,m in atoms)==0 and V==v+s
    M=sum(abs(z)**3*m for z,m in atoms);G=sum(z**3*m for z,m in atoms)
    J=sum(sum(z*m for z,m in atoms[j+1:])*(atoms[j+1][0]-atoms[j][0])**2 for j in range(len(atoms)-1))
    assert all(z!=0 for z,_ in atoms)
    return {'p':p,'q':q,'v':v,'s':s,'V':V,'M':M,'G':G,'J':J,
            'a0':a0,'a1':a1,'d':d,'atoms':atoms,'noises':noises,'vars':variances}
def Q(p,sigma):return (sigma+1)*p*p+(sigma-1)*(1-p)**2-6*p*(1-p)
def Yupper(p,d,branch):
    r=p if branch==0 else 1-p
    positive=3*(su+3 if branch==0 else su+1)*r
    negative=(sl+7 if branch==0 else sl+5)*d
    kk=6*(1-d)*(su+1 if branch==0 else su-1)*r
    return positive-negative+2*root(kk)[1]
records=[];reflected_records=[];excluded=[];zero_cases=0;budget_tests=0;minmargin=None
for n in [42,100]:
    for p in [F(1,4),F(3,10),F(1,3),F(2,5),F(41886117,10**8),F(1,2),F(27,50)]:
        for lam in [F(0),F(1,10**12),F(1,100),F(3,40),F(7,20),F(3,5)]:
            for w in ([F(0)] if lam==0 else [F(0),F(1,2),F(1)]):
                z=actual(p,n,lam,w)
                if z['d']>dmax:
                    excluded.append({'p':str(p),'n':n,'lambda':str(lam),'allocation':str(w),'d':str(z['d']),'reason':'outside inward cap'})
                    continue
                # The cubic inequality is an equality for each nondegenerate
                # two-point conditional law; zero-cap laws are degenerate.
                for side,zs in enumerate(z['noises']):
                    zz=[(x if side==0 else -x,m) for x,m in zs]
                    a=max(x for x,_ in zz);t=sum(x*x*m for x,m in zz)
                    if a==0:assert t==0
                    else:assert sum(x**3*m for x,m in zz)==a*t-t*t/a
                if lam==0:
                    # Exact equality in both coefficients of sqrt(10).
                    assert n*z['M']==n*z['v']*(p*p+(1-p)**2)
                    assert n*(3*z['M']-z['G']-3*z['J'])==n*z['v']*(p*p-(1-p)**2-6*z['v'])
                    zero_cases+=1;continue
                margins=[]
                for dbar in [dmax,z['d']]:
                    lhs=n*((3+sl)*z['M']-z['G']-3*z['J'])
                    rhs=n*z['v']*Q(p,su)+lam*((1-w)*Yupper(p,dbar,0)+w*Yupper(p,dbar,1))
                    margin=lhs-rhs
                    assert margin>0,(p,n,lam,w,dbar,margin)
                    rounded=F(margin.numerator*10**40//margin.denominator,10**40)
                    assert rounded>0
                    margins.append(str(rounded));budget_tests+=1
                    minmargin=rounded if minmargin is None else min(minmargin,rounded)
                records.append({'n':n,'p':str(p),'lambda':str(lam),'allocation':str(w),
                                'inward_sum':str(z['d']),'unscaled_margins_lower':margins})
                reflected=sorted((-x,m) for x,m in z['atoms'])
                rJ=sum(sum(x*m for x,m in reflected[j+1:])*(reflected[j+1][0]-reflected[j][0])**2 for j in range(len(reflected)-1))
                assert rJ==z['J']
                rmargins=[]
                for dbar in [dmax,z['d']]:
                    lhs=n*((3+sl)*z['M']+z['G']-3*rJ)
                    rhs=n*z['v']*Q(1-p,su)+lam*(w*Yupper(1-p,dbar,0)+(1-w)*Yupper(1-p,dbar,1))
                    margin=lhs-rhs
                    assert margin>0,('reflected',p,n,lam,w,dbar,margin)
                    rounded=F(margin.numerator*10**40//margin.denominator,10**40)
                    assert rounded>0
                    rmargins.append(str(rounded));budget_tests+=1
                    minmargin=min(minmargin,rounded)
                reflected_records.append({'n':n,'p':str(1-p),'lambda':str(lam),'allocation':str(1-w),
                    'inward_sum':str(z['d']),'unscaled_margins_lower':rmargins,
                    'scope':'Algebraic theorem; reflected probability may lie outside the acquired domain.'})

# Obstruction to trying to finish the left range from these necessary data.
p=F(3,10);n=42;lam=F(1,10);z=actual(p,n,lam,F(0));V=z['V']
rv=root(V);Dlo=n*((3+sl)*z['M']-z['G']-3*z['J'])/(V*rv[1])
Dhi=n*((3+su)*z['M']-z['G']-3*z['J'])/(V*rv[0])
assert z['a0']==F(5,882) and z['a1']==0
assert 26<Dlo<Dhi<27<F('32.20665378')
assert z['s']/V<F(7,125) and z['d']<dmax
assert z['M']/(V*rv[0])<F(713,500)
assert all(x*x<F(157,50)**2*V for x,_ in z['atoms'])
obstruction={'p':str(p),'n':n,'lambda':str(lam),'d':str(z['d']),
 'raw_centered_atoms':[[str(x),str(m)]for x,m in z['atoms']],
 'variance':str(V),'nD_interval':[str(Dlo),str(Dhi)],
 'scope':'Actual geometric/strip law; no maximizing contact or nonnegative excess claimed.'}
# Deleting the positive a*t term gives a false cubic inequality.
a=z['a0'];t=z['vars'][0];mu3=sum(x**3*m for x,m in z['noises'][0])
assert mu3>-t*t/a

# Reproduce the explicit warning example from Schulz, pp.26--27.
helper=Path(__file__).resolve().parents[2]/'simplification-v10/2026-10-28/actual_law_checks.py'
pin='351997e80de8895ac87b4e5dfeb33efc28e16c934bfef8f41ccf2af20ee59e07'
blob=helper.read_bytes();assert hashlib.sha256(blob).hexdigest()==pin
ns={'__name__':'geometry_Bernoulli_control','__file__':str(helper)}
exec(compile(blob,str(helper),'exec'),ns)
n=217;p=F(77,2604);v=p*(1-p);k=6
FB=sum(F(comb(n,j))*p**j*(1-p)**(n-j) for j in range(k+1))
norm=ns['Phi_interval'](ns['div'](ns['I'](k-n*p),ns['root'](n*v)))
claimed=ns['div'](ns['mul'](ns['PHI0'],ns['I']((4-2*p)/6)),ns['root'](n*v))
excess=ns['sub'](ns['sub'](ns['I'](FB),norm),claimed)
assert excess[0]>0
assert hashlib.sha256(helper.read_bytes()).hexdigest()==pin
here=Path(__file__).resolve()
print(json.dumps({'status':'PASS_INWARD_MOMENT_ACTUAL_LAWS','positive_noise_laws':len(records),
 'reflected_positive_noise_laws':len(reflected_records),
 'zero_noise_identities':zero_cases,'exact_budget_checks':budget_tests,
 'outside_cap_controls':excluded,'minimum_unscaled_margin_lower':str(minmargin),
 'laws':records,'reflected_laws':reflected_records,'geometric_obstruction':obstruction,
 'negative_controls':['deleting_a_times_variance_in_cubic_bound_is_false',
                      'geometric_inputs_do_not_force_p_at_least_one_third',
                      'geometric_inputs_do_not_force_lambda_at_most_point01'],
 'Schulz_extrapolation_control':{'n':n,'p':str(p),'anchor':k,
    'sharp_formula_excess_interval':[str(x)for x in excess],
    'outside_acquired_probability_domain':True,'normal_kernel_sha256':pin},
 'checker_sha256':hashlib.sha256(here.read_bytes()).hexdigest(),'python':sys.version,
 'scope':'Exact actual-marginal and atom/gap controls, not a sampled proof '
 'of the continuous geometric theorem or a claim that the obstruction is a contact witness.'},indent=2))
