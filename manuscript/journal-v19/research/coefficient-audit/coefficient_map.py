"""Exact rational maps licensed by the fixed algebraic family.

Every interval is a premise about the SAME law; this module does not acquire it.
There is one outer budget, one conditional variance budget, and no Fourier call.
"""
from fractions import Fraction as F
from itertools import product
from poly import add, const, decode, evaluate, substitute, scale, variable
from accept_objects import load, need, verify


def interval(value, positive=False):
    need(type(value)in(list,tuple) and len(value)==2,'two interval endpoints')
    lo,hi=map(F,value);need(lo<=hi and (not positive or lo>0),'ordered interval domain')
    return lo,hi


def product_interval(*intervals):
    values=[]
    for endpoints in product(*intervals):
        p=F(1)
        for x in endpoints:p*=x
        values.append(p)
    return min(values),max(values)


def rounded_up(x,scale=10**8):
    x=F(x)
    return F(-((-x.numerator*scale)//x.denominator),scale)


def zero_safe_quotient(numerator,denominator):
    """Schur lower correction; zero/zero is zero, positive/zero is impossible."""
    need(numerator>=0 and denominator>=0,'nonnegative Schur inputs')
    if not denominator:
        need(not numerator,'zero diagonal forces zero cross term')
        return F(0)
    return numerator*numerator/denominator


def sign_contraction(radius,first,second,third):
    R=F(radius);ml,mu=interval(first,True);al,au=interval(second,True);bl,bu=interval(third,True)
    need(R>0,'positive sign-specific radius')
    # Weight x(R-x): [Rm-a,Ra-b;Ra-b,Rb-c] is PSD.
    den=R*mu-al;cross=max(F(0),R*al-bu)
    correction=zero_safe_quotient(cross,den)
    c_upper=R*bu-correction;c_lower=bl*bl/au
    need(c_upper>=c_lower>=0,'nonempty fourth-moment interval')
    # Weight x^2(R-x), with the independently proved c upper endpoint.
    den5=R*au-bl;cross5=max(F(0),R*bl-c_upper)
    f_upper=R*c_upper-zero_safe_quotient(cross5,den5)
    need(f_upper>=0,'nonnegative fifth-moment ceiling')
    return {'c_lower':c_lower,'c_upper':c_upper,'f_upper':f_upper,
            'fourth_correction':correction,'fifth_correction':R*c_upper-f_upper}


def native_psd_prefix(row):
    """Independent re-derivation of native c4u/Mc/etac, with its exact rounding.

    Inputs read: R,M,eta,rh,mu,asl,asu,bsl,bsu. In particular no supplied
    DU,DL,denm,corrections,c4u,Mc or etac is used to compute the result.
    """
    R,M,eta,rh,mu=(F(row[k])for k in('R','M','eta','rh','mu'))
    asl,asu,bsl,bsu=([F(v)for v in row[k]]for k in('asl','asu','bsl','bsu'))
    need(all(len(z)==2 for z in(asl,asu,bsl,bsu)),'two sign classes')
    need(R>0 and mu>0 and all(0<a<=b for a,b in zip(asl,asu)) and
         all(0<=a<=b for a,b in zip(bsl,bsu)),'prefix moment interval domain')
    corrections=[]
    for al,bu in zip(asl,bsu):
        corrections.append(zero_safe_quotient(max(F(0),R*al-bu),R*mu-al))
    c4u=[rounded_up(R*b-q)for b,q in zip(bsu,corrections)]
    Mc=min(M,rounded_up(R*rh-sum(corrections)))
    fifth=[]
    for al,bl,cu in zip(asu,bsl,c4u):
        den=R*al-bl;cross=max(F(0),R*bl-cu)
        # Native code skips den=0; validity needs the PSD zero-row implication.
        fifth.append(zero_safe_quotient(cross,den))
    etac=min(eta,rounded_up(R*Mc-sum(fifth)))
    return {'c4u':c4u,'Mc':Mc,'etac':etac,'corrections':corrections}


class Family:
    def __init__(self,path):
        self.object=load(path);self.acceptance=verify(self.object)
        self.polys={z['id']:decode(z['coefficients'])for z in self.object['polynomials']}
        self.transform={tuple(z['index']):[(k,h,F(c))for k,h,c in z['weights']]
                        for z in self.object['central_transform']}

    def val(self,name,**values):
        return evaluate(self.polys[name],**values)

    def central(self,A,B,m,rho):
        al,au=interval(A,True);bl,bu=interval(B,True);ml,mu=interval(m,True);rho=F(rho)
        need(rho>=0,'nonnegative actual absolute third moment')
        x,y=variable('x'),variable('a')
        power=substitute(self.polys['G'],{'a':add(const(al),scale(x,au-al)),
                                           'b':add(const(bl),scale(y,bu-bl)),'r':const(rho)})
        coefficients={}
        for e,c in power.items():
            need(not any(e[2:]),'central polynomial only on closed unit square')
            coefficients[e[:2]]=c
        bernstein=[sum((c*coefficients.get((k,h),F(0))for k,h,c in self.transform[i,j]),F(0))
                   for i in range(5)for j in range(5)]
        upper=max(bound*z for z in bernstein for bound in(ml,mu))
        def p_bounds(name):
            low=min(self.val(name,a=a,b=bl)for a in(al,au))
            clipped=min(au,max(al,bu))
            high=self.val(name,a=clipped,b=bu)
            return product_interval((ml,mu),(low,high))
        return {'G_upper':upper,'bernstein25':bernstein,
                'J1_interval':p_bounds('P1'),'J2_interval':p_bounds('P2')}

    def quadratic_extrema(self,x_interval,a_interval,t):
        xl,xu=interval(x_interval);al,au=interval(a_interval);t=F(t)
        need(xl>=0 and al>=0,'nonnegative support magnitude and conditional mean')
        q=lambda x,a:self.val('F',x=x,a=a,t=t)
        clip=lambda z,l,u:min(u,max(l,z))
        corners=[q(x,a)for x in(xl,xu)for a in(al,au)]
        values=list(corners)
        for x in(xl,xu):values.append(q(x,clip(t/2-x/3,al,au)))
        for a in(al,au):values.append(q(clip(3*t/4-a,xl,xu),a))
        stationary=3*t/8
        if xl<=stationary<=xu and al<=stationary<=au:values.append(q(stationary,stationary))
        return min(values),max(corners)

    def conditional_k(self,positive_support,negative_support,positive_mean,negative_mean,
                      rho,gamma_V,theta):
        rl,ru=interval(rho,True);gl,gu=interval(gamma_V);theta=F(theta)
        need(0<=theta<1,'one conditional variance budget')
        pl=self.quadratic_extrema(positive_support,positive_mean,ru+gu)[0]
        pu=self.quadratic_extrema(positive_support,positive_mean,rl+gl)[1]
        nl=-self.quadratic_extrema(negative_support,negative_mean,rl-gu)[1]
        nu=-self.quadratic_extrema(negative_support,negative_mean,ru-gl)[0]
        return theta*min(F(0),pl,nl),theta*max(F(0),pu,nu)


def outer_bounds(radius_plus,radius_minus,B_lower,rho,budget):
    """A single positive-measure budget, with individual caps intersected."""
    need(type(budget)is dict and set(budget)=={'amount','plus_price','minus_price','plus_cap','minus_cap'},'one complete outer budget')
    Rplus,Rminus,B,rho=map(F,(radius_plus,radius_minus,B_lower,rho))
    amount,cp,cm,tp,tm=(F(budget[k])for k in('amount','plus_price','minus_price','plus_cap','minus_cap'))
    need(Rplus>0 and Rminus>0 and 0<=B<=Rplus and rho>=0,'outer support domain')
    need(amount>=0 and cp>0 and cm>0 and tp>=0 and tm>=0,'nonnegative shared resource and positive prices')
    tp=min(tp,amount/cp);tm=min(tm,amount/cm)
    gp=max(F(0),rho-B)**2;gm=max(F(0),Rminus-rho)**2
    charge=F(3,8)*min(gp*tp+gm*tm,amount*max(gp/cp,gm/cm))
    return {'J1_interval':(-Rminus*tm/2,Rplus*tp/2),'three_G_upper':charge,
            'plus_cap':tp,'minus_cap':tm,'budget_used_once':True}


def coherent_coefficients(family,cell,rho):
    """Conditional theorem: all cell fields must enclose the SAME actual law."""
    need(type(cell)is dict and set(cell)=={'radii','m','a_plus','a_minus','b_plus','b_minus','rho','beta','gamma','A','B','mu4_upper','eta5_upper','outer'},'fixed coherent-cell fields')
    rp,rm=map(F,cell['radii']);rho=F(rho);rl,ru=interval(cell['rho'],True)
    need(rl<=rho<=ru and rl>=1,'actual rho point in its proved cell')
    beta=interval(cell['beta']);gamma=interval(cell['gamma'])
    need(-1<beta[0]<=beta[1]<1,'strict signed second-moment domain')
    plus=sign_contraction(rp,cell['m'],cell['a_plus'],cell['b_plus'])
    minus=sign_contraction(rm,cell['m'],cell['a_minus'],cell['b_minus'])
    delta=(gamma[0]-rho*beta[1],gamma[1]-rho*beta[0]);distance=max(F(0),delta[0],-delta[1])
    beta_min=F(0)if beta[0]<=0<=beta[1]else min(abs(x)for x in beta)
    gram_lower=rho*rho+distance*distance/(1-beta_min*beta_min)
    m4lo=max(plus['c_lower']+minus['c_lower'],gram_lower)
    m4hi=min(F(cell['mu4_upper']),plus['c_upper']+minus['c_upper'])
    eta_hi=min(F(cell['eta5_upper']),plus['f_upper']+minus['f_upper'])
    need(m4lo<=m4hi and eta_hi>=0,'nonempty simultaneous moment bounds')
    signed4=(plus['c_lower']-minus['c_upper'],plus['c_upper']-minus['c_lower'])
    k1=(signed4[0]-3*beta[1]-F(3,2)*rho*gamma[1],signed4[1]-3*beta[0]-F(3,2)*rho*gamma[0])
    central=family.central(cell['A'],cell['B'],cell['m'],rho)
    outer=outer_bounds(rp,rm,F(cell['B'][0]),rho,cell['outer'])
    u=(central['J1_interval'][0]+outer['J1_interval'][0]+(m4lo-3)/6,
       central['J1_interval'][1]+outer['J1_interval'][1]+(m4hi-3)/6)
    projection_penalty=distance**4/(4*rho*(1-beta_min*beta_min)**2)
    sign_penalty=(max(F(0),rho+gamma[0])*max(F(0),delta[0])**2/(8*(1+beta[1])**2)
                  +max(F(0),rho-gamma[1])*max(F(0),-delta[1])**2/(8*(1-beta[0])**2))
    penalty=max(projection_penalty,sign_penalty)
    cross=product_interval(beta,gamma)[1]
    negative_kq=rho**3/4-penalty+F(3,2)*cross-rho/2
    return {'mu4':(m4lo,m4hi),'eta5_upper':eta_hi,'signed_fourth':signed4,
            'K1':k1,'U':u,'three_G_upper':3*central['G_upper']+outer['three_G_upper'],
            'negative_Kq_upper':negative_kq,'projection_penalty':projection_penalty,
            'sign_penalty':sign_penalty,'common_outer_budget':cell['outer']}
