"""Independent interpolation and actual-law controls for the v13 geometry.

No constructor module, coefficient array or discovery output is imported.
Bernstein coefficients are recovered from exact values by linear equations.
"""
from fractions import Fraction as F
from math import comb,isqrt
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
S=F('3.162277660');T=F('3.162277661');B=F('32.20665378');d=F('.068')
assert S*S<10<T*T
def lo(x):
    den=10**12;k=isqrt(x.numerator*den**2//x.denominator);a=F(k,den)
    assert a*a<=x<(a+F(1,den))**2
    return a
def Q(p,s):return (s+1)*p*p+(s-1)*(1-p)**2-6*p*(1-p)
def solve(a,b):
    z=[list(row)+[val]for row,val in zip(a,b)];n=len(b)
    for j in range(n):
        k=next(k for k in range(j,n)if z[k][j]);z[j],z[k]=z[k],z[j]
        c=z[j][j];z[j]=[v/c for v in z[j]]
        for k in range(n):
            if k==j:continue
            c=z[k][j];z[k]=[x-c*y for x,y in zip(z[k],z[j])]
    assert all(z[i][j]==(i==j)for i in range(n)for j in range(n))
    return [row[-1]for row in z]
def bernstein_by_values(fn,degree,a,b):
    points=[F(i,degree)for i in range(degree+1)]
    mat=[[F(comb(degree,j))*t**j*(1-t)**(degree-j)for j in range(degree+1)]for t in points]
    values=[fn(a+(b-a)*t)for t in points];co=solve(mat,values)
    for t in [F(1,7),F(2,5),F(11,13)]:
        assert fn(a+(b-a)*t)==sum(co[j]*comb(degree,j)*t**j*(1-t)**(degree-j)for j in range(degree+1))
    return co
targets=[('global',F('.25'),F('.54'),F('.36')),('left',F('.25'),F('.4'),F('.32')),
         ('below_third',F('.25'),F(1,3),F('.25')),('below_three_tenths',F('.25'),F('.3'),F(1,6))]
records=[];count=0
for name,a,b,L in targets:
    for side in [0,1]:
        def z(p):return p if side==0 else 1-p
        C=6*(1-d)*(S+1 if side==0 else S-1)
        ya=2*lo(C*z(a));yb=2*lo(C*z(b))
        def y(p):
            affine=3*(S+3 if side==0 else S+1)*z(p)-(T+7 if side==0 else T+5)*d
            return affine+ya+(yb-ya)*(p-a)/(b-a)
        def base(p):return 42*p*(1-p)*Q(p,S)+L*y(p)
        def squared(p):return 42**3*base(p)**2-B*B*(42*p*(1-p)+L)**3
        bc=bernstein_by_values(base,4,a,b);assert min(bc)>0;count+=len(bc)
        pieces=4 if(name,side)==('global',1)else 1
        margins=[]
        for j in range(pieces):
            left=a+(b-a)*F(j,pieces);right=a+(b-a)*F(j+1,pieces)
            bc=bernstein_by_values(squared,8,left,right);assert min(bc)>0;count+=len(bc)
            margins.append(str(min(bc)))
        records.append({'domain':name,'allocation':side,'minimum_coefficients':margins})
assert count==139
# Independently checked derivative signs and near-critical localization constant.
assert 30*(1-F('.616')/(42*2*F(3,16)))-3*F('.36')/(2*F(3,16))>0
assert B/(2*(6+2*S))<F(23,20)**2
cutoffs=[]
for p,N in [(F('.30'),84),(F(1,3),168),(F('.35'),262),(F('.375'),657),(F('.39'),1530),(F('.40'),3598)]:
    assert Q(p,S)>0 and (N+1)**2*Q(p,S)**2>B*B*p*(1-p)
    cutoffs.append([str(p),N])
def law(a,b):
    return {F(0):F(1)}if not a or not b else {-a:b/(a+b),b:a/(a+b)}
actual=0;equalities=0
for p in [F(1,4),F(1,3),F(2,5),F(1,2),F(27,50)]:
    for a0,a1 in [(F(0),F('.02')),(F('.02'),F(0)),(F('.01'),F('.025'))]:
        u0=law(F('.6'),a0);u1=law(a1,F('.7'))
        s0=sum(x*x*w for x,w in u0.items());s1=sum(x*x*w for x,w in u1.items())
        c0=sum(x**3*w for x,w in u0.items());c1=sum(x**3*w for x,w in u1.items())
        if a0:assert a0*s0-c0-s0*s0/a0==0;equalities+=1
        else:assert s0==c0==0
        if a1:assert a1*s1+c1-s1*s1/a1==0;equalities+=1
        else:assert s1==c1==0
        atoms={}
        for x,w in u0.items():atoms[x-p]=(1-p)*w
        for x,w in u1.items():atoms[x+1-p]=p*w
        v=p*(1-p);rho=sum(abs(x)**3*w for x,w in atoms.items());gamma=sum(x**3*w for x,w in atoms.items())
        support=sorted(atoms)
        J=sum(sum(x*w for x,w in atoms.items()if x>=b)*(b-a)**2 for a,b in zip(support,support[1:]))
        Jo=v*((1-a0-a1)**2+a0*a0+a1*a1)+(1-p)*(p+2*a0)*s0+p*(1-p+2*a1)*s1-(1-p)*c0+p*c1
        assert Jo>=J
        for sigma in [F(0),F(1)]:
            expanded=v*Q(p,sigma)+6*v*((a0+a1)*(1-a0-a1)+a0*a1)
            expanded+=(3*(sigma+3)*p-6*a0)*(1-p)*s0+(3*(sigma+1)*(1-p)-6*a1)*p*s1
            expanded-=(sigma+1)*(1-p)*c0;expanded+=(sigma-1)*p*c1
            assert expanded==(3+sigma)*rho-gamma-3*Jo
        actual+=1
# Negative control: replacing the sqrt chord by its tangent can reverse the required bound.
x=F(13,40);assert (1+(x-1)/2)**2>x
here=Path(__file__).resolve();proof=here.with_name('geometry-noise.tex')
print(json.dumps({'status':'PASS_INDEPENDENT_INWARD_GEOMETRY','scope':'Independently reconstructed all continuous scalar certificates and raw actual-law algebra; analytic acquisition remains a premise',
                  'Bernstein_coefficients':count,'actual_laws':actual,'sharp_cubic_equalities':equalities,
                  'coefficient_margins':records,'index_cutoffs':cutoffs,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest()if proof.exists()else None,
                  'python':sys.version},indent=2))
