#!/usr/bin/env python3
"""Exact endpoint certificate for a continuous, conditional low-noise lemma.

No project imports, input proof objects, sampling, Fourier/native replay, or
floating-point acceptance. The fixed invocation checks the displayed proof's
rational polynomial identities and monotonicity gates. It does not establish
contact, the incoming .6 strip, the inward gap, or the predecessor theorem.
"""
from fractions import Fraction as F
import json
import sys


def need(ok, why):
    if not ok:
        raise ValueError(why)


def add(*polys):
    out = [F(0)] * max(map(len, polys))
    for poly in polys:
        for i, value in enumerate(poly):
            out[i] += value
    return out


def scale(poly, value):
    return [value * x for x in poly]


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def derivative(poly, order=1):
    for _ in range(order):
        poly = [i * poly[i] for i in range(1, len(poly))]
    return poly


def value(poly, x):
    y = F(0)
    for a in reversed(poly):
        y = y * x + a
    return y


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [encode(v) for v in x]
    return x


def run():
    need(__debug__ and not sys.flags.optimize, 'ordinary unoptimized Python')
    theta, E, r = F(37, 5000), F(249, 125), F(221, 200)
    v, noise, sigma = F(6, 25), F(3, 40), F(3, 5)
    c, S, e = F(819, 2000), F(81, 80), F(8, 875)
    a, d = 2 * (1 - theta) / E, -2 + 3 * theta
    left, right = E * F(9, 10), E * F(11, 10)
    gates = {}

    def positive(name, x):
        need(x > 0, name)
        gates[name] = x

    def negative(name, x):
        positive(name, -x)

    positive('cubic_coefficient_squared_margin', 24**2 * v**3 - (3*sigma + sigma)**2)
    positive('theta_margin', theta - noise / (42*v + noise))
    positive('ell_squared_margin', 4*(1-theta) - E**2)
    positive('rho_remainder_positive', r - 24*noise/42)
    positive('rho_squared_margin', (r-24*noise/42)**2*v - (1-2*v)**2)
    positive('heat_scale_margin', S*S - F(42,41))
    positive('heat_radius_squared_margin', left**2 - 3)

    # Coefficients are ordered by increasing powers of u. b is the boundary
    # FAMILY b(u). It is held fixed when differentiating along a physical ray.
    x = [F(0), F(1)]
    x2, x3 = mul(x,x), mul(mul(x,x),x)
    x4, x5 = mul(x2,x2), mul(x2,x3)
    b = [d,a]
    h4 = add(x4,scale(x2,-6),[F(3)])
    A = scale(add(x3,scale(x,-3)),F(1,6))
    error = add(scale(x5,F(1,4100)),scale(x,F(3,820)),
                scale(add(scale(x2,3),[F(-2)]),F(17,78720)))
    Q = add(scale(x3,-1),scale(x2,3*r/2),scale(mul(b,x),3),[e*r])
    P = add(scale(add(A,scale(h4,F(-1,72))),F(2,5)*S**3),
            scale(error,S**3),scale(Q,c))
    explicit = [
        -F(2,5)*S**3/24 - S**3*F(34,78720) + c*e*r,
        -F(2,5)*S**3/2 + S**3*F(3,820) + 3*c*d,
        F(2,5)*S**3/12 + S**3*F(51,78720) + c*(3*r/2+3*a),
        F(2,5)*S**3/6-c, -F(2,5)*S**3/72, S**3/4100]
    need(P == explicit, 'exact quintic expansion')
    negative('quartic_at_right', value(h4,right))
    # H4' = 4u(u^2-3)>0, so H4 is negative on the full closed interval.
    positive('third_derivative_convexity', derivative(P,5)[0])
    negative('third_derivative_at_left', value(derivative(P,3),left))
    negative('third_derivative_at_right', value(derivative(P,3),right))
    positive('first_derivative_at_left', value(derivative(P),left))
    positive('first_derivative_at_right', value(derivative(P),right))
    negative('heat_at_right', value(P,right))

    # These Q derivatives are TOTAL derivatives of the boundary family.
    negative('Q_total_second_at_left', value(derivative(Q,2),left))
    positive('Q_total_first_at_right', value(derivative(Q),right))
    negative('Q_at_right', value(Q,right))

    # These polynomials are the FIXED-b ray derivatives, evaluated along the
    # family. Their subsequent derivatives only certify family monotonicity.
    Q1 = add(scale(x2,-3),scale(x,3*r),scale(b,3))
    Q2 = add(scale(x,-6),[3*r])
    L = add(scale(add(scale(x2,F(1,2)),[F(1,2)+e]),F(2,5)),scale(Q1,c))
    L1 = add(scale(x,F(2,5)),scale(Q2,c))
    L2 = F(2,5)-6*c
    for name, poly in [('Q1',Q1),('Q2',Q2),('L',L),('L1',L1)]:
        negative(name+'_at_left',value(poly,left))
        negative(name+'_family_derivative_at_left',value(derivative(poly),left))
        if len(poly) == 3:
            negative(name+'_family_second_derivative',derivative(poly,2)[0])
    negative('L2_constant',L2)

    controls = []
    def reject(name, fn):
        try:
            fn()
        except ValueError:
            controls.append(name)
        else:
            raise ValueError('false condition accepted: '+name)

    reject('false_P_second_derivative_negative_at_left',
           lambda: need(value(derivative(P,2),left)<0,'false concavity shortcut'))
    reject('ell_lower_2_unlicensed',lambda: need(4<4*(1-theta),'scale gate'))
    reject('cubic_coefficient_18_unlicensed',
           lambda: need(18**2*v**3>(3*sigma+sigma)**2,'cubic gate'))
    wrong = P.copy(); wrong[4] = -wrong[4]
    reject('sign_swapped_quartic_coefficient',lambda: need(wrong==explicit,'coefficient identity'))
    reject('missing_quintic_coefficient',lambda: need(P[:-1]==explicit,'coefficient identity'))
    reject('total_Q_derivative_as_held_beta_ray_derivative',
           lambda: need(derivative(Q)==Q1,'total/held derivative distinction'))
    return dict(status='PASS_CONDITIONAL_CONTINUOUS_LOW_NOISE_ENDPOINT_GATES',
        mathematical_scope='Conditional p in [2/5,3/5], all n>=42 and all raw H, lambda in [0,3/40], incoming |U|<3/5 and inward d<.072, fixed-target contact and sharp predecessor. Applied acquired entry only p in [.40,.53]. No global or high-noise claim.',
        constants=dict(theta=theta,ell_lower=E,rho_upper=r,noise_upper=noise,
                       c_lower=c,heat_scale=S,epsilon=e),
        interval=[left,right], beta_family=[d,a],
        polynomials=dict(P=P,Q_total_family=Q,Q1_held_beta_family=Q1,Q2_held_beta=Q2,
                         L_held_beta_family=L,L1_held_beta=L1,L2_held_beta=L2),
        strictly_positive_margins=gates,endpoint_gate_count=len(gates),
        heat_upper=value(P,right),false_second_derivative_shortcut=value(derivative(P,2),left),
        rejected_controls=controls,grid_cells=0,
        trusted_stack='Python standard-library Fraction integer arithmetic; exact polynomial operations and endpoint/convexity proof, no project imports or external proof objects.')


if __name__ == '__main__':
    print(json.dumps(encode(run()),indent=2,sort_keys=True))
