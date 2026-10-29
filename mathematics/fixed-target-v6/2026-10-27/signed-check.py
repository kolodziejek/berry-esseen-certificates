#!/usr/bin/env python3
"""Bounded exact acceptance of new sign-coherent moment coefficients.

Imports no inherited numerical program. Reads the pinned prior 24-row output
only as source data, then reconstructs all moment caps used by this check.
Fourier constants and complete resource bounds are outside this contract.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import platform
import sys

ROOT = Path(__file__).resolve().parents[3]
PRIOR = "runs/fixed-target-v5-20261027/cell02/check.stdout.json"
PRIOR_SHA = "7525713bd06a30b9c13693d01949d4f186890128eed3432771953ef9eafef082"
R = F(96, 25)


def need(ok, message):
    if not ok:
        raise ValueError(message)


def root_upper(x):
    need(x >= 0, "nonnegative radicand")
    scale = 10**8
    k = isqrt(x.numerator*scale**2//x.denominator)
    lo, hi = F(k, scale), F(k+1, scale)
    need(lo*lo <= x <= hi*hi, "outward root")
    return hi


def ev(p, x):
    return sum(c*x**j for j, c in enumerate(p))


def quadratic_max(p, lo, hi):
    need(lo <= hi, "ordered closed interval")
    sites = [lo, hi]
    if p[2] < 0:
        vertex = -p[1]/(2*p[2])
        if lo <= vertex <= hi:
            sites.append(vertex)
    return max(ev(p, x) for x in sites), sites


def beta_gate(u, b):
    # (1+b^2)/sqrt(1-b^2)>=u: f is strictly increasing in b>=0.
    need(u >= 1 and 0 <= b < 1, "beta cap domain")
    need((1+b*b)**2 >= u*u*(1-b*b), "valid sign-moment beta cap")


def signed_cap(l, u, b):
    need(1 <= l <= u <= R, "rho/support domain")
    beta_gate(u, b)
    h = 1+b
    # Supremum over all real delta, before imposing delta>=h^2.
    p = [3*b+h*R*R/8, R-3*h*R/4, -F(3, 2)+9*h/8]
    unconstrained, sites = quadratic_max(p, l, u)
    # On the constrained branch the derivative in h is concave.
    a_low, a_high = (3*l-R)/2, (3*u-R)/2
    h_derivative = 3+2*a_low*h-3*h*h/2
    rho_derivative = R-3*u+3*h*h/2
    use_strong = h >= a_high and h_derivative >= 0 and rho_derivative >= 0
    strong = None
    if use_strong:
        strong = R*u-3*u*u/2-3+3*h+a_high*h*h-h**3/2
        need(strong >= 0, "nonnegative absolute upper bound")
    result = min(unconstrained, strong) if strong is not None else unconstrained
    return dict(unconstrained_cap=unconstrained, quadratic_sites=sites,
                h_upper=h, h_derivative_gate=h_derivative,
                rho_derivative_gate=rho_derivative, h_above_a_gate=h-a_high,
                strong_gate_passed=use_strong, constrained_cap=strong,
                new_K_abs=result)


def ceiling(x, digits=6):
    scale = 10**digits
    return F(-((-x.numerator*scale)//x.denominator), scale)


def moments(xs, ps):
    E = lambda f: sum(w*f(x) for x, w in zip(xs, ps))
    need(len(xs) == len(ps) and max(map(abs, xs)) <= R, "actual support bound")
    need(sum(ps) == 1 and min(ps) >= 0 and E(lambda x: x) == 0
         and E(lambda x: x*x) == 1, "actual standardized law")
    rho, beta, gamma = E(lambda x: abs(x)**3), E(lambda x: x*abs(x)), E(lambda x: x**3)
    M4, M5, zeta = E(lambda x: x**4), E(lambda x: abs(x)**5), E(lambda x: x*abs(x)**3)
    K1 = zeta-3*beta-3*rho*gamma/2
    for sign in (1, -1):
        h, delta = 1-sign*beta, rho-sign*gamma
        need(h > 0 and delta >= h*h, "same-law sign constraint")
        upper = R*rho-3*rho*rho/2-3+3*h+(3*rho-R)*delta/2-delta*delta/(2*h)
        need(sign*K1 <= upper, "signed Cauchy K1 envelope")
    need(rho*M4/2-M5/4 <= rho**3/4, "fifth moment square bound")
    return dict(xs=xs, ps=ps, rho=rho, beta=beta, gamma=gamma, K1=K1,
                fifth_square_slack=M5-2*rho*M4+rho**3)


def encode(x):
    if isinstance(x, F): return str(x)
    if isinstance(x, dict): return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)): return [encode(v) for v in x]
    return x


def main():
    need(__debug__ and not sys.flags.optimize, "unoptimized Python required")
    raw = (ROOT/PRIOR).read_bytes()
    need(sha256(raw).hexdigest() == PRIOR_SHA, "prior table source binding")
    prior = json.loads(raw)["rows"]
    need(len(prior) == 24, "exact 24-cell coverage")
    rows = []
    for i, old in enumerate(prior):
        l, u = 1+F(3361*i, 96000), 1+F(3361*(i+1), 96000)
        need(old["index"] == i and F(old["rho_lower"]) == l
             and F(old["rho_upper"]) == u, "ordered source cell endpoints")
        M = min(F(111, 10), R*u, 1+(R+1)**2/(R+F(1, 2))*(u-1))
        g = min(F(37, 20), u, root_upper(M-1))
        b = root_upper((u*root_upper(u*u+8)-u*u-2)/2)
        need(M == F(old["M4"]) and g == F(old["gamma_abs"])
             and b == F(old["beta_abs"]), "independently reconstructed moment caps")
        radial = R*(R+2-3*l/2)/(R+F(1, 2))
        need(radial >= F(31, 40), "retained radial negative-part gate")
        retained_K = min(3*u*b+radial*(u-1), 6*u-3*u*u/2+3*b,
                         R*u/2+max(abs(R/2-3*r/2) for r in (l, u))*g+3*b)
        need(retained_K == F(old["K_abs"]), "retained scalar K formula")
        cap = signed_cap(l, u, b)
        # Gamma is a retained gap coefficient; its analytic validity is not
        # proved here. The algebraic A improvement is conditional on that edge.
        Gamma = F(old["Gamma"])
        need(Gamma >= 0, "nonnegative retained gap charge")
        A1 = 3*b*(2*u+1)/2+3*Gamma*u+3*u*u*(u+1)/8+8*u**3/27-l/2
        A2 = 3*b*(2*u+1)/2+2*u*M-l/2
        need(min(A1, A2) == F(old["A"]), "retained constant formula")
        A_new = min(A1-F(5, 108)*u**3, A2)
        effective = min(retained_K, cap["new_K_abs"])
        rows.append(dict(index=i, rho_lower=l, rho_upper=u, beta_abs=b,
                         retained_K_abs=retained_K, effective_K_abs=effective,
                         safe_K_decimal=ceiling(effective), retained_A=min(A1,A2),
                         new_A=A_new, safe_A_decimal=ceiling(A_new), **cap))
    need(rows[-1]["rho_upper"] == F(7361, 4000), "final endpoint")
    need(rows[-1]["constrained_cap"] < F(397, 100), "last-cell 3.97 bound")
    controls = []
    def reject(name, action):
        try: action()
        except ValueError: controls.append(name)
        else: raise ValueError("negative control accepted: "+name)
    reject("reversed cell", lambda: signed_cap(F(2), F(1), F(1, 2)))
    reject("invalid beta cap", lambda: beta_gate(F(7361,4000), F(1,10)))
    reject("understated last-cell target", lambda: need(rows[-1]["constrained_cap"] < F(396,100), "target"))
    reject("missing rho cell", lambda: need(len(rows[:-1]) == 24, "complete cover"))
    reject("forced monotonicity on cell one", lambda: need(rows[1]["h_derivative_gate"] >= 0, "monotonicity"))
    actual = [moments([F(-1), F(1)], [F(1,2), F(1,2)]),
              moments([F(-1,2), F(2)], [F(4,5), F(1,5)]),
              moments([F(-46,25), F(0), F(46,25)], [F(625,4232), F(1491,2116), F(625,4232)]),
              moments([F(-96,25), F(-1,2), F(37,25)], [F(325,22211), F(11708,16533), F(3650,13167)])]
    counter = actual[-1]
    need(rows[-1]["rho_lower"] < counter["rho"] < rows[-1]["rho_upper"], "counterexample in last rho cell")
    need(abs(counter["K1"]) < rows[-1]["constrained_cap"], "actual law within new bound")
    need(actual[2]["fifth_square_slack"] == 0, "sharp fifth-moment control with a zero atom")
    reject("assume beta gamma nonnegative", lambda: need(counter["beta"]*counter["gamma"] >= 0, "signed moments"))
    reject("tiny atoms beyond acquired support", lambda: moments(
        [F(-4), F(0), F(4)], [F(1,32), F(15,16), F(1,32)]))
    output = dict(status="PASS_SIGNED_MOMENT_COEFFICIENTS_V1", python=platform.python_version(),
                  scope="Universal moment inequalities and 24 closed scalar cells; no Fourier, resource, support acquisition or local exclusion acceptance",
                  rows=rows, actual_laws=actual, rejected_controls=controls,
                  input_sha256={PRIOR: PRIOR_SHA,
                      str(Path(__file__).relative_to(ROOT)): sha256(Path(__file__).read_bytes()).hexdigest()})
    print(json.dumps(encode(output), indent=2))


if __name__ == "__main__":
    main()
