#!/usr/bin/env python3
"""Exact actual-law obstruction to replacing conditional span by small moments.

Fixed bounded invocation only: four three-point laws, two Bernoulli controls,
104 conditional-sum states, and explicit mutation controls. No Fourier engine,
native acceptor, source archive, floating search, or constructor import runs.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
N, K = 42, 17
SL, SU = F('3.162277660168379331'), F('3.162277660168379332')
TABLE = 'runs/fixed-target-v6-20261027/signed-two-pass02/stdout.json'
PINS = {
 TABLE:'c52122bea63beaed83de741a347863a39fb0faeaa34dec5dc4b2741a0a88594a',
 'manuscript/arxiv-v1/sections/05c-counts.tex':'bcb3417380015e75d19ad6dc799b8fc2f403c3f2f8727471fbba83bc8e27d632',
 'manuscript/arxiv-v1/appendices/fourier-analysis.tex':'0274a491a12fec13d87a391ce88184cc7229210168fc72bc88974e5382670a1f',
 'manuscript/arxiv-v1/appendices/local42-refinements.tex':'a2ea8efdee5f7316aea51dfc3284df01b31c2536a9ea5b3f2b3cdd32a5d60b8f',
 'mathematics/fixed-target-v5/2026-10-27/count-cost.tex':'653464a3d72866309bfe03c5310e7a9b0d868ba13cf8747f93898e2085ecf51b',
 'mathematics/fixed-target-v5/2026-10-27/response-proof/response.tex':'274c9f75df734313cdbd34b62eb74629988bb981f3ba83e376a0b682a1a9aa1b',
 'mathematics/fixed-target-v5/2026-10-27/cell-sources/accept_initial42.py':'aa759c74fbd9ad39618264ef51b961f13c7833faa77a7f7b33309c27a7cee032',
 'mathematics/simplification/2026-10-27/uniform42.md':'7a5117b321e30b3159e5ca04f429ac55a63bb59c543442119ed9b523ecf9d977',
}


def need(ok, why):
    if not ok:
        raise ValueError(why)


def unique(pairs):
    out = {}
    for key, value in pairs:
        need(key not in out, 'duplicate input key')
        out[key] = value
    return out


def pinned(blob, digest):
    need(sha256(blob).hexdigest() == digest, 'source bytes changed')


def moments(law):
    need(len(law) >= 2 and all(w > 0 for x,w in law), 'positive atom weights')
    need(all(law[i][0] < law[i+1][0] for i in range(len(law)-1)), 'ordered distinct atoms')
    need(sum(w for x,w in law) == 1, 'probability mass')
    need(sum(x*w for x,w in law) == 0, 'centering')
    need(sum(x*x*w for x,w in law) == 1, 'unit variance')
    need(max(abs(x) for x,w in law) <= F(96,25), 'actual support radius')
    rho = sum(abs(x)**3*w for x,w in law)
    gamma = sum(x**3*w for x,w in law)
    beta = sum(x*abs(x)*w for x,w in law)
    gaps = []
    for (u,_),(v,_) in zip(law,law[1:]):
        tau = sum(x*w for x,w in law if x >= v)
        need(tau > 0, 'actual gap weight')
        gaps.append(dict(left=u,right=v,tau=tau,J=tau*(v-u)**2))
    J = sum(g['J'] for g in gaps)
    dlo, dhi = (3+SL)*rho-gamma-3*J, (3+SU)*rho-gamma-3*J
    need(0 <= dlo <= dhi, 'defect enclosure')
    return dict(rho=rho,gamma=gamma,beta=beta,J=J,D_lower=dlo,D_upper=dhi,gaps=gaps)


def table_cover(rows):
    need(len(rows) == 24, 'complete table')
    for i,row in enumerate(rows):
        need(row['index'] == i and F(row['rho_lower']) == 1+F(3361*i,96000)
             and F(row['rho_upper']) == 1+F(3361*(i+1),96000), 'ordered closed table')


def family(eps, t):
    need(0 < eps < F(1,2) and t > 0, 'positive perturbation domain')
    q = (1+eps-eps*eps)/(1+t*t)
    p, scale = 1-q, t*q
    need(eps < p < 1 and scale > 0, 'correct sign classes')
    need(scale*scale == q*(p+eps*(1-eps)), 'rational standardization')
    law = [((eps-1-p)/scale,q*eps),((eps-p)/scale,q*(1-eps)),((1-p)/scale,p)]
    return law,p,q,scale


def proper_span(width):
    need(0 < width < 1, 'strict nonresonant span')


def mark_feasible(cost, gain, cap):
    """Existence of 0<z<=cap with z+cost/z<gain; fixed scalar cell only."""
    need(cost >= 0 and cap > 0, 'mark scalar domain')
    if cost == 0:
        return gain > 0
    if cap*cap >= cost:
        return gain > 0 and gain*gain > 4*cost
    return cap+cost/cap < gain


def run():
    need(__debug__ and not sys.flags.optimize, 'unoptimized interpreter')
    need(SL > 0 and SL*SL < 10 < SU*SU, 'directed square-root enclosure')
    blobs = {name:(ROOT/name).read_bytes() for name in PINS}
    for name,blob in blobs.items():
        pinned(blob,PINS[name])
    rows = json.loads(blobs[TABLE],object_pairs_hook=unique)['rows']
    table_cover(rows)
    results,states = [],0
    for eps,t in [(F(1,100),F(21,25)),(F(1,1000),F(21,25)),
                  (F(1,10**6),F(21,25)),(F(1,10**9),F(849,1000))]:
        law,p,q,scale = family(eps,t)
        data = moments(law)
        rho = data['rho']
        hits = [z for z in rows if F(z['rho_lower']) <= rho <= F(z['rho_upper'])]
        need(len(hits) == 1, 'one containing open-cell example')
        row = hits[0]
        d = F(row['passes'][1]['defect'])
        need(data['D_upper'] < d and N*data['D_upper'] < F(row['passes'][1]['weighted_nD']),
             'actual law meets its recorded defect and weighted bound')
        need(data['D_upper'] < (SL-1)*F(row['rho_lower']), 'actual law passes strict gap criterion')
        need(data['D_upper'] < F('.784'), 'actual law meets old defect target')
        m = sum(x*w for x,w in law if x > 0)
        ell = m/(p*q)
        need(ell == 1/scale, 'same-law scale dictionary')
        cond = [(law[0][0]/ell+p,eps),(law[1][0]/ell+p,1-eps)]
        need(cond == [(eps-1,eps),(eps,1-eps)], 'actual negative conditional residual')
        need(law[2][0]/ell+p-1 == 0, 'actual positive conditional residual')
        need(sum(x*w for x,w in cond) == 0, 'conditional centering')
        lam = N*q*eps*(1-eps)
        ownvar = (N-K)*eps*(1-eps)
        # V_k=(n-k)eps-Bin(n-k,eps); no trigonometric arithmetic is needed.
        w = (N-K)*eps
        distribution = [(w-j,F(comb(N-K,j))*eps**j*(1-eps)**(N-K-j)) for j in range(N-K+1)]
        need(sum(a for v,a in distribution) == 1, 'actual conditional convolution mass')
        need(sum(v*a for v,a in distribution) == 0, 'actual conditional convolution centering')
        need(sum(v*v*a for v,a in distribution) == ownvar > 0, 'positive own-count variance')
        for v,a in distribution:
            need(a > 0 and (w-v).denominator == 1, 'exact atom collisions modulo one')
            states += 1
        fractional = sum(((w-v)-((w-v).numerator//(w-v).denominator))*a for v,a in distribution)
        need(fractional == 0, 'zero fractional-part gain')
        u = eta = w/2
        need(0 < eta <= 1 and abs(u) <= F(1,2) and 1 <= K <= N-1, 'legal marked phase')
        need((N+1)*p-K < 2, 'curvature chi gate')
        results.append(dict(epsilon=eps,t=t,law=law,p=p,scale=scale,
          **data,table_row=row['index'],recorded_D=d,lambda_value=lam,
          conditional_span=F(1),conditional_amplitude=1-eps,inward_gap=eps,count_increment=1-eps,
          k=K,u=u,eta=eta,w=w,own_count_variance=ownvar,fractional_gain=fractional,
          weighted_nD_upper=N*data['D_upper'],states=len(distribution)))
    need(results[-1]['D_upper'] < F(1,10**7) and results[-1]['lambda_value'] < F(1,10**7),
         'tiny defect and noise do not remove resonance')
    controls = []
    def reject(name,action):
        try:
            action()
        except ValueError:
            controls.append(name)
        else:
            raise ValueError('bad control accepted: '+name)
    law = results[0]['law']
    reject('missing atom',lambda:moments(law[:-1]))
    reject('reordered atoms',lambda:moments(list(reversed(law))))
    reject('changed weight',lambda:moments([(law[0][0],law[0][1]+F(1,10000)),*law[1:]]))
    reject('wrong variance',lambda:moments([(2*x,w) for x,w in law]))
    reject('zero noise mislabelled positive',lambda:family(F(0),F(21,25)))
    reject('wrong sign class',lambda:family(F(1,10),F(1,10)))
    reject('span equality wrongly accepted',lambda:proper_span(F(1)))
    reject('span above one wrongly accepted',lambda:proper_span(F(101,100)))
    reject('source byte corruption',lambda:pinned(blobs[TABLE]+b' ',PINS[TABLE]))
    reject('missing table row',lambda:table_cover(rows[:-1]))
    reject('reordered table',lambda:table_cover(list(reversed(rows))))
    reject('duplicate input key',lambda:json.loads('{"x":1,"x":2}',object_pairs_hook=unique))
    reject('positive gain at resonance',lambda:need(results[0]['fractional_gain'] > 0,'false extension'))
    reject('negative mark cost',lambda:mark_feasible(F(-1),F(3),F(1)))
    reject('zero mark cap',lambda:mark_feasible(F(1),F(3),F(0)))
    barrier_cases = []
    for cost,gain,cap,expected in [
        (F(1),F(3),F(2),True),(F(1),F(3),F(1,2),True),
        (F(1),F(2),F(2),False),(F(1),F(21,10),F(1,2),False),
        (F(0),F(1,10),F(1),True),(F(0),F(0),F(1),False),
        (F(1),F(-3),F(2),False)]:
        result = mark_feasible(cost,gain,cap)
        need(result == expected, 'exact scalar barrier boundary')
        barrier_cases.append(dict(cost=cost,gain=gain,cap=cap,feasible=result))
    # Actual symmetric and skew Bernoulli controls: noise is exactly zero.
    binary = []
    for t in (F(1),F(21,25)):
        q,p = 1/(1+t*t),t*t/(1+t*t)
        z = moments([(-t,q),(1/t,p)])
        need(z['J'] == t+1/t, 'two-point gap identity')
        binary.append(dict(t=t,**z,conditional_noise=F(0)))
    proper_span(F(3,4))
    # sin^2(3*pi/4)=1/2 gives this exact positive admissible rate.
    rate_at_three_quarters = F(1)/F(3,4)**2
    need(rate_at_three_quarters == F(16,9), 'new-domain exact rate example')
    return dict(status='PASS_EXACT_RESONANCE_OBSTRUCTION_AND_DOMAIN_CHECKS',
       mathematical_scope='Actual standardized iid laws refute moment-only positive fractional gain; the analytic span extension is proved in exclusion.tex. No maximizing-contact or score claim.',
       laws=results,conditional_sum_states=states,bernoulli_controls=binary,
       new_domain_example=dict(span=F(3,4),rate=rate_at_three_quarters,unconditional_scalar_constant=8),
       scalar_barrier_cases=barrier_cases,
       rejected_controls=controls,source_sha256=PINS,
       checker_sha256=sha256(Path(__file__).read_bytes()).hexdigest())


if __name__ == '__main__':
    print(json.dumps(run(),default=lambda x:str(x) if isinstance(x,F) else x,sort_keys=True,indent=2))
