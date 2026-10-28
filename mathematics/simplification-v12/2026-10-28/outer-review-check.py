"""Independent exact reconstruction of the four-phase larger-noise proof.

Evaluate the original rational inequalities and interpolate in Bernstein bases.
No constructor source is imported or executed. The final coefficients can be
compared to the saved constructor artifact as an untrusted array.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:raise RuntimeError('Assertions required')
A=F(3,5);V=F(6,25);U=F(3,40);N=42;XI=F(46,25)*F(251,500)

def matrix_inverse(a):
    n=len(a);z=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if z[i][j])
        z[j],z[pivot]=z[pivot],z[j]
        v=z[j][j];z[j]=[x/v for x in z[j]]
        for i in range(n):
            if i!=j:
                v=z[i][j];z[i]=[x-v*y for x,y in zip(z[i],z[j])]
    assert all(z[i][j]==F(i==j) for i in range(n) for j in range(n))
    return [row[n:] for row in z]

def basis(n,i,x):return F(comb(n,i))*x**i*(1-x)**(n-i)
def inverse_evaluation(n):return matrix_inverse([[basis(n,j,F(i,n)) for j in range(n+1)] for i in range(n+1)])

def J(mu,u,m):
    denominator=m*(1/A-1)-u/A+mu
    assert denominator>0 and 0<=mu<m+2
    return mu**(m+1)/(factorial(m+1)*denominator**2*(1-mu/F(m+2)))
def Q(mu,u):
    denominator=(1-u)/A-1+mu
    assert denominator>0 and mu>=0
    return mu**2*(F(1,2)+mu/6)/denominator**2

def original_inner(lam,u,c):
    alpha=F(16,25);M=5*alpha**4;t=c*lam
    own=((3*alpha**2-A*A)*t-3*t*t-4*A*u*t-6*u*u*t-u**4+3*alpha**2*u*u-2*alpha**3*u)/M+F(24,25)*u
    mu1=F(9,8)*lam/A**2;mug=F(5,2)*lam/A**2
    d1=(1-u)/A-1+mu1;d2=2*(1/A-1)-u/A+mug;d3=1-mug/4
    assert d1>0 and d2>0 and d3>0
    denominator=6*d1*d1*d2*d2*d3
    # Inner repair is .75 lambda/n, after the cubic unit gain.
    margin=F(73,100)*(own-F(53,50)*(Q(mu1,u)+J(mug,u,2)))-(F(3,168)+F(1,100))*lam
    return margin*denominator

def interpolated_coefficients(c):
    nx,ny=7,8;lx=inverse_evaluation(nx);ly=inverse_evaluation(ny)
    grid=[[original_inner(U*F(i,nx),U*F(j,ny),c) for j in range(ny+1)] for i in range(nx+1)]
    first=[[sum(lx[i][k]*grid[k][j] for k in range(nx+1)) for j in range(ny+1)] for i in range(nx+1)]
    beta=[[sum(ly[j][l]*first[i][l] for l in range(ny+1)) for j in range(ny+1)] for i in range(nx+1)]
    # Verification at off-interpolation rational points, separate from solving.
    for x,y in [(F(1,13),F(2,17)),(F(7,11),F(4,9)),(F(1),F(1,2)),(F(0),F(1,3))]:
        reconstructed=sum(beta[i][j]*basis(nx,i,x)*basis(ny,j,y) for i in range(nx+1) for j in range(ny+1))
        assert reconstructed==original_inner(U*x,U*y,c)
    return [(i,j,beta[i][j]) for i in range(nx+1) for j in range(ny+1)]

def normalize_gates():
    g={}
    def put(k,x):g[k]=x
    D=F(413,250)
    put('raw_sd_cap',F(251,500)**2-F(1,4)-U/N)
    put('global_count_offset',D-XI-F(91,125))
    # The interval [9/25,23/40] contains both p and k/n.
    put('count_left',F(2,5)-D/N-F(9,25));put('count_right',F(23,40)-F(53,100)-D/N)
    put('stirling_product_left',F(9,25)*F(16,25)-F(23,100));put('stirling_product_right',F(23,40)*F(17,40)-F(23,100))
    put('entropy_third_derivative',6-F(7,25)/F(23,100)**2)
    put('log_prefactor_derivative',F(5,4)-F(7,25)/F(23,100))
    put('factorial_remainder',F(3,8)-1/(12*F(23,100)))
    put('log_variance_part',F(8,3)-1/(2*V)-D*D/(2*N*V*V))
    put('normal_variance_derivative',F(7,4)**2*V**3-F(1,5)**2)
    put('phi_lower_using_pi_upper',1-2*F(355,113)*F(19943,50000)**2)
    put('unit_cubic_gain',F(2,5)*(F(87,250)-F(13,16)*U/N)-F(251,500)**3)
    for label,d,b,m,R,slope,upper in [
        ('inner',F(1),F(3,40),F(73,100),F(53,50),F(24,25),False),
        ('negative',F(6,5),F(34,125),F(71,100),F(27,25),F(27,25),True),
        ('near',F(43,40),F(3,20),F(73,100),F(107,100),F(19,20),False),
        ('far',D,F(91,125),F(13,20),F(1143,1000),F(9,10),False)]:
        Z=F(5,8)*d+F(3,8)+d**3/N
        put(label+'_offset',d-XI-b)
        put(label+'_mass',2*F(19943,50000)*(1-(d*d/(2*V)+Z)/N)-m)
        ratio=1+(F(53,100)+d-1)/(N*V-F(3,5)*max(d-1,0))
        if label=='far':ratio*=1+(F(53,100)+d-2)/(N*V)
        put(label+'_ratio',R-ratio)
        put(label+'_remaining_ratios',F(3 if label=='far' else 2)-F(53,100)-d)
        term=(2*d*b+b*b) if label in ('inner','negative') else 2*XI*b-b*b
        E=(F(8,3)*U+term/(2*V)+Z)/N
        put(label+'_slope',slope*(1-E)-1 if upper else 1-E-slope)
    put('positive_signed_phase',XI-F(91,125))
    put('inner_first_count',F(9,8)-1-F(5,2)*2/N)
    put('near_first_count',F(9,8)-1-F(5,2)*(F(43,40)+1)/N)
    put('negative_first_count',F(8,7)-1-F(5,2)*(F(6,5)+1)/N)
    put('far_first_count',F(7,6)-1-F(5,2)*(D+1)/N)
    return g

def outer_margins(gain=F(1)):
    mug=F(5,2)*U/A**2;T=F(15,14)*U;r0=F(3,20);r1=F(34,125)
    own=min(r*r/(T+r*r)-F(27,25)*r for r in [r0,r1])
    tail=Q(F(8,7)*U/A**2,-r0)+J(mug,-r0,2)
    out={'negative':F(71,100)*(own-F(27,25)*tail)-(F(7,4)*F(6,5)-gain)*U/N-U/100}
    for u in [F(3,40),F(3,20)]:
        out['near_'+str(u)]=F(73,100)*(F(19,20)*u-F(107,100)*(Q(F(9,8)*U/A**2,u)+J(mug,u,2)))-(F(7,4)*F(43,40)-gain)*U/N-U/100
    d=F(413,250);T1=F(7,6)*U;mu2=(1+F(5,2)*(d+2)/N)*U/A**2
    for u in [F(3,20),F(91,125)]:
        second=mu2**3/(6*((2-u)/A-2+mu2)**2)
        out['far_'+str(u)]=F(13,20)*(F(9,10)*u-F(1143,1000)*(T1/(T1+(1-u)**2)+second+J(mug,u,3)))-(F(7,4)*d-gain)*U/N-U/100
    return out

def main():
    g=normalize_gates();assert all(x>0 for x in g.values()),{k:str(x)for k,x in g.items() if x<=0}
    assert F(15,14)==1+F(5,2)*F(6,5)/N
    T=F(15,14)*U;r0=F(3,20)
    assert 2*T*r0/(T+r0*r0)**2>F(27,25)
    assert 3*(1-F(91,125))**2>F(7,6)*U
    assert (2-F(91,125))/A-2>0
    assert 1/A-1-F(3,20)/A>0
    margins=outer_margins();assert all(v>F(17,10000) for v in margins.values())
    no_gain=outer_margins(F(0));assert any(v<=0 for v in no_gain.values())
    coefficients=[]
    for c in [F(79,84),F(89,84)]:
        rows=interpolated_coefficients(c)
        assert rows[0]==(0,0,F(0)) and all(v>0 for _,_,v in rows[1:])
        coefficients.append({'t_over_lambda':str(c),'rows':[[i,j,str(v)]for i,j,v in rows], 'minimum_positive':str(min(v for _,_,v in rows[1:]))})
    ratio_checks=0
    for n in [42,43,100]:
      for p in [F(2,5),F(1,2),F(53,100)]:
       for k in range(1,n):
        if abs(k-n*p)<=F(413,250):
         ratio=F(1)
         for j in range(k+1,n+1):
          ratio*=F(n-j+1,j)*p/(1-p)
          assert ratio<F(1143,1000);ratio_checks+=1
    report={'status':'PASS_INDEPENDENT_FOUR_PHASE_REVIEW','scope':'u in [-.272,-.15] union [0,.728], lambda in (0,.075]; remaining theorem premises retained',
       'interpolated_coefficient_count':144,'strict_coefficients':142,'zero_coefficients':2,
       'normalization_gates':{k:str(v)for k,v in g.items()},'outer_margins':{k:str(v)for k,v in margins.items()},
       'gain_removal_rejected_at':[k for k,v in no_gain.items() if v<=0], 'actual_binomial_ratio_controls':ratio_checks,
       'bernstein':coefficients}
    if len(sys.argv)>1:
        root=Path(sys.argv[1]).resolve();rel='mathematics/simplification-v12/2026-10-28/'
        report['reviewed_sources']={rel+x:hashlib.sha256((root/rel/x).read_bytes()).hexdigest() for x in ['outer.tex','outer-check.py']}
        assert report['reviewed_sources']=={rel+'outer.tex':'72ff7ae27bdbecfa0a535dd62e52417de9bab370b7004af8b86e9e99f491facc', rel+'outer-check.py':'2ab32c0bd1c07e4b6ac64ed7dceb8fd1ed999c0309fb580f28c3a4b79f8dcafb'}, 'Reviewed source changed'
        artifact=root/'runs/simplification-v12-20261028/outer01/stdout.json'
        if artifact.exists():
            data=json.loads(artifact.read_text());expected=data['bernstein']
            assert len(expected)==2
            for got,want in zip(coefficients,expected):
                assert got['t_over_lambda']==want['t_over_lambda'] and got['rows']==want['rows']
            report['constructor_array_comparison']='all144 match independently interpolated rational coefficients'
            report['constructor_array_sha256']=hashlib.sha256(artifact.read_bytes()).hexdigest()
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__=='__main__':main()
