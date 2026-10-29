"""Exact scalar gates for the direct comparison on 0<lambda<=3/100.

Mathematical reduction and complete coverage are in counts-v11.tex.
No discovery grid is imported into these acceptance checks.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
if not __debug__ or sys.flags.optimize:
    raise RuntimeError('Optimization disables proof obligations')

def evaluate(U=F(3,100),cubic_gain=F(1),negative_h=F(0)):
    # Reuse the unchanged reviewed finite normalization inequalities, then
    # replace the inner-phase and final inequalities for the present theorem.
    base=Path(__file__).resolve().parents[2]/'simplification-v10/2026-10-28/moderate_noise_check.py'
    raw=base.read_bytes()
    assert hashlib.sha256(raw).hexdigest()=='13c4c27a66cb692a5ac480a986e8240a8ab38b59c066cb3f24d81d9676a13f11'
    namespace={'__name__':'pinned_v10_normalization','__file__':str(base)}
    exec(compile(raw,str(base),'exec'),namespace)
    previous=namespace['evaluate'](U)
    retained=('global_threshold_delta','sqrt_variance_upper',
      'count_fraction_lower','count_fraction_upper','interior_lower','interior_upper',
      'stirling_variance','stirling_E','stirling_L','stirling_R','log_variance_B0',
      'global_lower_derivative','global_upper_derivative','near_delta',
      'near_lower_derivative','positive_G_monotone','positive_lower_derivative',
      'global_mass','inner_mass','mode_mass_squared','mode_own_ratio',
      'inner_ratio','inner_second_ratio','inner_count_variance','global_count_variance',
      'global_own_variance','cubic_repair_nonnegative','normal_repair_squared')
    checks={k:previous[k] for k in retained}
    def gate(name,value):checks[name]=value
    A=F(3,5);N=F(42);v=F(6,25);d=F(9,125)
    inner=F(3,40);lower=-F(34,125);upper=F(91,125);D=F(33,20)
    Z=lambda x:F(5,8)*x+F(3,8)+x**3/N
    xi=F(46,25)*F(501,1000)
    eps=(F(8,3)*U+(2*inner+inner**2)/(2*v)+Z(1))/N
    gate('new_inner_delta',1-xi-inner)
    gate('new_inner_lower_derivative',1-eps-F(24,25))
    gate('new_inner_upper_derivative',F(26,25)*(1-eps)-1)
    B=F(6,5)-F(3,2)*(1-2*v)-d-F(3,8)*(1-2*v)*U/(N*v)
    gate('unit_cubic_gain',F(2,5)*B-cubic_gain*F(501,1000)**3)
    gate('inner_repair_nonstrict',F(3,4)-(F(7,4)-cubic_gain))
    gate('global_repair',2-(F(7,4)*D-cubic_gain))
    gate('quartic_majorant',F(11**2-36*3))
    alpha=F(13,25);den=5*alpha**4;T=F(89,84)*U
    def quadratic_min(c0,c1,c2,z):
        vals=[c0,c0+c1*z+c2*z*z]
        if c2>0 and 0<-c1/(2*c2)<z:vals.append(c0-c1*c1/(4*c2))
        return min(vals)
    def scaled(sig,b,z):
        ans=[]
        for t in [F(0),T]:
            c0=(3*alpha**2-A**2-3*t)/den
            c1=2*sig/(5*alpha)+b-4*A*t/den
            c2=(3*alpha**2*t-6*t*t-t**3*z*z)/den
            ans.append(quadratic_min(c0,c1,c2,z))
        return min(ans)
    z=F(3,2);cm=F(37,100);cp=F(19,20)
    gate('negative_quartic',scaled(1,-F(26,25),z)-cm)
    gate('positive_quartic',scaled(-1,F(24,25),z)-cp)
    gate('negative_cantelli_start',z*z/(1+z*z*T)-F(26,25)*z-cm)
    gate('negative_cantelli_slope',2*z/(1+z*z*T)**2-F(26,25))
    gate('negative_cantelli_endpoint',inner**2/(T+inner**2)-F(26,25)*inner-cm*T)
    gate('switch_inside',inner-z*T)
    gate('positive_linear_switch',F(24,25)*z-cp)
    def rest(mu,h):
        b=1/A-1-h/(2*A)
        return mu**3/(3*(b+mu)**2*(1-3*mu))
    def alltail(mu,h):
        a=(1-h)/A-1
        return mu**2*(F(1,2)+mu/6)/(a+mu)**2+rest(mu,h)
    mui=F(9,8)*U/A**2;mug=F(7,6)*U/A**2
    for name,mu,h in [('inner_neg',mui,negative_h),('inner_pos',mui,inner),('outer_neg',mug,F(0)),('near',mug,F(1,10)),('middle',mug,F(1,5)),('far',mug,upper)]:
        gate(name+'_geometric_ratio',1-3*mu)
        gate(name+'_rest_denominator',1/A-1-h/(2*A))
    gate('negative_first_monotonicity',(1-negative_h)/A-1-mui)
    gate('positive_first_monotonicity',(1-inner)/A-1-mui)
    neg_inner=cm*F(79,84)-F(53,50)*alltail(mui,negative_h)/U
    pos_inner=cp*F(79,84)-F(53,50)*alltail(mui,inner)/U
    for name,br in [('inner_negative',neg_inner),('inner_positive',pos_inner)]:
        gate(name+'_bracket',br)
        gate(name+'_final',F(73,100)*br-(F(7,4)-cubic_gain)/N-F(1,100))
    Tg=F(11,10)*U
    ownneg=min(r*r/(Tg+r*r)-F(5,4)*r for r in [inner,-lower])
    gate('negative_outer_initial_slope',2*inner*Tg/(Tg+inner**2)**2-F(5,4))
    br=ownneg-F(3,2)*alltail(mug,0)
    gate('outer_negative_bracket',br)
    gate('outer_negative_final',F(13,20)*br-2*U/N-U/100)
    tin=F(7,6)*U
    near=F(19,20)*inner-F(3,2)*(tin/(tin+F(9,10)**2)+rest(mug,F(1,10)))
    gate('positive_near_bracket',near)
    gate('positive_near_final',F(13,20)*near-2*U/N-U/100)
    gate('positive_cantelli_convexity',3*(1-upper)**2-tin)
    for name,lo,hi in [('middle',F(1,10),F(1,5)),('far',F(1,5),upper)]:
        br=min(F(9,10)*x-F(3,2)*tin/(tin+(1-x)**2) for x in [lo,hi])-F(3,2)*rest(mug,hi)
        gate('positive_'+name+'_bracket',br)
        gate('positive_'+name+'_final',F(13,20)*br-2*U/N-U/100)
    return checks

if __name__=='__main__':
    def failed(values):
        return [k for k,v in values.items() if (v<0 if k.endswith('_nonstrict') else v<=0)]
    ans=evaluate();assert not failed(ans),{k:str(ans[k]) for k in failed(ans)}
    controls={
      'remove_cubic_gain':failed(evaluate(cubic_gain=F(0))),
      'reverse_cubic_gain':failed(evaluate(cubic_gain=F(-1))),
      'omit_cubic_factor_1_over_n':failed(evaluate(cubic_gain=F(42))),
      'reuse_positive_phase_tail_for_negative':failed(evaluate(negative_h=F(3,40))),
      'unproved_expansion_to_point04':failed(evaluate(U=F(1,25)))}
    assert all(controls.values())
    cover=[(-F(34,125),-F(3,40)),(-F(3,40),F(0)),(F(0),F(3,40)),
      (F(3,40),F(1,10)),(F(1,10),F(1,5)),(F(1,5),F(91,125))]
    def covers_closed(intervals):
        return bool(intervals) and intervals[0][0]==-F(34,125) and intervals[-1][1]==F(91,125) and all(a<b for a,b in intervals) and all(intervals[i][1]==intervals[i+1][0] for i in range(len(intervals)-1))
    assert covers_closed(cover)
    bad_gap=cover[:];bad_gap[2]=(F(1,1000),bad_gap[2][1])
    assert not covers_closed(bad_gap)
    assert not covers_closed(cover[:1]+cover[2:])
    assert not covers_closed([cover[1],cover[0]]+cover[2:])
    assert not covers_closed(cover[:2]+[cover[1]]+cover[2:])
    # The stronger own-count coefficient 1/2 is actually false for this
    # polynomial at the eligible point t=T*, z=3/2.
    t=F(89,2800);z=F(3,2);a=F(13,25);A=F(3,5);den=5*a**4
    point=(3*a*a-A*A-3*t)/den+(2/(5*a)-F(26,25)-4*A*t/den)*z
    point+=(3*a*a*t-6*t*t)*z*z/den-t**3*z**4/den
    assert F(37,100)<point<F(1,2)
    print(json.dumps({'status':'PASS_UNIFORM_COMPARISON_LAMBDA_LE_3_OVER_100','gate_count':len(ans),'scope':'n>=42,p in [.4,.53],.6 strip,d<=.072,|H|<=1.84,0<lambda<=.03,C>=.4; analytic reduction and external P2 theorem documented separately','gates':{k:str(v) for k,v in ans.items()},'terminal_margins':{k:str(v) for k,v in ans.items() if k.endswith('_final')},'closed_phase_cover':[[str(a),str(b)] for a,b in cover],'coverage_negative_controls':['gap','missing_interval','reordering','duplicate_interval'],'own_coefficient_negative_control':{'actual_polynomial_value':str(point),'rejected_coefficient':'1/2'},'negative_controls':controls,'python':sys.version},indent=2))
