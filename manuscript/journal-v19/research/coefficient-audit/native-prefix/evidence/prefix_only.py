"""Exact rational local signed-moment entry covers with full [0,1] p panels.
No target selection or file I/O. New HIGH_WINDOW50 scope; frozen barrier
kernels remain unchanged.

All covers use one common actual law. A fixed external acceptor supplies the
ordered invariants and named theorem; this module alone makes no cutoff claim.
"""
from fractions import Fraction as F
import kernel as k
import high_window_core
high_window_core.install(k)
ZERO = F(0)
ONE = F(1)
HALF = F(1, 2)

def lo(x):
    return k.down(x)

def hi(x):
    return k.up(x)

def sl(x):
    return k.roots(x)[0]

def su(x):
    return k.roots(x)[1]

def pos(x):
    return max(ZERO, x)

def init(p):
    k.RADIUS = p['radius']
    r = k.RADIUS
    k.K4 = (r + 1) ** 2 / (r + HALF)
    k.K5 = (r ** 3 + 2 * r * r + 3 * r + F(3, 2)) / (r + HALF)
    k.constants()
    k.need(type(p['n']) is int and 3 <= p['n'] <= p['nmax'], 'index band')
    k.need(0 <= p['barrier'] < 3 and F('.4095') <= p['cap'] <= F('.469'), 'score scope')
    for x in p['grid']:
        k.need(type(x) is int and x > 0, 'positive integer cover grid')

def stage(p, raw=None, d=None):
    init(p)
    n, R, K, cap = (p['n'], p['radius'], p['barrier'], p['cap'])
    nr, nb, ng, nm = p['grid']
    k.need((raw is None) == (d is None), 'ordered raw and defect invariants')
    if raw is not None:
        k.need(0 < raw < F(2, 5) * n and 0 < d < 4, 'feedback initialization')
    c0 = F('.4095') + K / p['nmax']
    rhomax = min(F('1.85'), F('.3031') * F('.646') / (c0 - F('.3031')), F('.3322') * F('.429') / (c0 - F('.3322')))
    peakR = F(-1)
    peakD = F(-1)
    active = excluded = 0
    reasons = {}
    panels = [dict(pl=F(j, 100), pu=F(j + 1, 100), raw=F(-1), D=F(-1), theta=ZERO, rho=ONE, beta=ZERO, H=ZERO, cells=0) for j in range(100)]
    moments = dict(rho=ONE, beta=ZERO, theta=ZERO, H=ZERO, pl=ONE, pu=ZERO)

    def drop(count, reason):
        nonlocal excluded
        excluded += count
        reasons[reason] = reasons.get(reason, 0) + count
    for ir in range(nr):
        rl = 1 + (rhomax - 1) * F(ir, nr)
        rh = 1 + (rhomax - 1) * F(ir + 1, nr)
        M = min(F('11.1'), R * rh, 1 + k.K4 * (rh - 1))
        eta = min(R * M, 1 + k.K5 * (rh - 1))
        ga = min(F('1.85'), rh, su(M - 1))
        ba = su((rh * su(rh * rh + 8) - rh * rh - 2) / 2)
        Gamma = k.negative_gap_coefficient(R, rl)
        k.need(0 < ba < 1, 'signed beta cover')
        for ib in range(nb):
            bl = -ba + 2 * ba * F(ib, nb)
            bu = -ba + 2 * ba * F(ib + 1, nb)
            bmin = ZERO if bl <= 0 <= bu else min(abs(bl), abs(bu))
            mU = HALF * min(su(1 - bmin * bmin), min(((R - rl + 2 * a + R * a * a) / (a * (2 * R + a)) for a in [F(j, 10) for j in range(2, 13)])))
            gl = max(-ga, sl((1 + bl) ** 3 / (1 - bl)) - rh)
            gu = min(ga, rh - sl((1 - bu) ** 3 / (1 + bu)))
            if d is not None:
                gl = max(gl, k.SL * rl - 6 * mU - d)
            gl, gu = (lo(gl), hi(gu))
            if gl > gu:
                drop(ng * nm, 'empty signed third interval')
                continue
            for ig in range(ng):
                l = gl + (gu - gl) * F(ig, ng)
                h = gl + (gu - gl) * F(ig + 1, ng)
                ds = [g - r * b for g in (l, h) for r in (rl, rh) for b in (bl, bu)]
                dist = max(ZERO, min(ds), -max(ds))
                den = 1 - bmin * bmin
                if rl * rl + dist * dist / den > M:
                    drop(nm, 'fourth projection')
                    continue
                asl = [(1 + bl) / 2, (1 - bu) / 2]
                asu = [(1 + bu) / 2, (1 - bl) / 2]
                bsl = [pos((rl + l) / 2), pos((rl - h) / 2)]
                bsu = [(rh + h) / 2, (rh - l) / 2]
                if min(bsu) <= 0:
                    drop(nm, 'positive third sign moments')
                    continue
                ml = max((1 + bmin * bmin) / (2 * rh), *(a * a / b for a, b in zip(asl, bsu)))
                if ml > mU:
                    drop(nm, 'common first moment interval')
                    continue
                DU = [R * a - b for a, b in zip(asu, bsl)]
                if min(DU) < 0:
                    drop(nm, 'negative support deficit')
                    continue

                def fmean(t):
                    return 2 * t + sum((pos(R * t - a) ** 2 / z for a, z in zip(asu, DU) if z > 0))
                if fmean(ml) > R:
                    drop(nm, 'sign probabilities exceed one')
                    continue
                mu = mU
                if fmean(mu) > R:
                    zl = ml
                    for _ in range(32):
                        zm = (zl + mu) / 2
                        if fmean(zm) > R:
                            mu = zm
                        else:
                            zl = zm
                mlo, mhi = (lo(ml), min(mU, hi(mu)))
                k.need(0 < mlo <= mhi, 'rounded mean cover')
                for im in range(nm):
                    ml = mlo + (mhi - mlo) * F(im, nm)
                    mu = mlo + (mhi - mlo) * F(im + 1, nm)
                    denm = [R * mu - a for a in asl]
                    DL = [pos(R * a - b) for a, b in zip(asl, bsu)]
                    if min(denm) < 0 or any((z == 0 and q > 0 for z, q in zip(denm, DL))):
                        drop(1, 'first support deficit')
                        continue
                    corrections = [q * q / z if z > 0 else ZERO for q, z in zip(DL, denm)]
                    c4u = [hi(R * b - q) for b, q in zip(bsu, corrections)]
                    Mc = min(M, hi(R * rh - sum(corrections)))
                    etac = min(eta, hi(R * Mc - sum((pos(R * b - c) ** 2 / z for b, c, z in zip(bsl, c4u, DU) if z > 0))))
                    if min(c4u) < 0 or Mc < 1 or etac < 1 or (rl * rl + dist * dist / den > Mc):
                        drop(1, 'bounded-support moment feasibility')
                        continue
                    dlower = max(ZERO, k.SL * rl - h - 6 * mu)
                    if d is not None and dlower > d:
                        drop(1, 'compulsory gap defect')
                        continue
                    g = min(max(abs(l), abs(h)), su(Mc - 1))
                    capture(locals())
                    active += 1
                    continue
    k.need(active + excluded == nr * nb * ng * nm, 'complete PREFIX grid cardinality')
    return dict(prefix_active=active, prefix_excluded=excluded, reasons=reasons, total=nr * nb * ng * nm)
