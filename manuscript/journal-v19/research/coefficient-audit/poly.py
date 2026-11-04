"""Small coefficient ring for the fixed signed-coefficient family: Q[x,a,b,r,t,u,v,g]."""
from fractions import Fraction as F
from math import comb

NAMES = ("x", "a", "b", "r", "t", "u", "v", "g")
ZERO = (0,) * len(NAMES)


def const(c):
    c = F(c)
    return {} if not c else {ZERO: c}


def variable(name):
    e = list(ZERO)
    e[NAMES.index(name)] = 1
    return {tuple(e): F(1)}


def clean(p):
    return {e: c for e, c in p.items() if c}


def add(*items):
    out = {}
    for p in items:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return clean(out)


def scale(p, c):
    return clean({e: F(c) * a for e, a in p.items()})


def mul(*items):
    out = const(1)
    for p in items:
        nxt = {}
        for e, c in out.items():
            for f, d in p.items():
                ef = tuple(i + j for i, j in zip(e, f))
                nxt[ef] = nxt.get(ef, F(0)) + c * d
        out = clean(nxt)
    return out


def power(p, n):
    out = const(1)
    for _ in range(n):
        out = mul(out, p)
    return out


def derivative(p, name):
    j = NAMES.index(name)
    out = {}
    for e, c in p.items():
        if e[j]:
            f = list(e)
            f[j] -= 1
            out[tuple(f)] = e[j] * c
    return clean(out)


def substitute(p, replacements):
    out = {}
    for e, c in p.items():
        term = const(c)
        for name, degree in zip(NAMES, e):
            term = mul(term, power(replacements.get(name, variable(name)), degree))
        out = add(out, term)
    return out


def integral(p, name, low, high):
    j = NAMES.index(name)
    antiderivative = {}
    for e, c in p.items():
        f = list(e)
        f[j] += 1
        antiderivative[tuple(f)] = c / f[j]
    return add(substitute(antiderivative, {name: high}),
               scale(substitute(antiderivative, {name: low}), -1))


def evaluate(p, **values):
    out = F(0)
    for e, c in p.items():
        term = c
        for name, degree in zip(NAMES, e):
            if degree:
                term *= F(values[name]) ** degree
        out += term
    return out


def encode(p):
    return [[list(e), str(c)] for e, c in sorted(p.items())]


def decode(rows):
    if type(rows) is not list or len(rows) > 1000:
        raise ValueError("bounded polynomial list")
    out = {}
    previous = None
    for row in rows:
        if type(row) is not list or len(row) != 2:
            raise ValueError("polynomial row")
        e, c = row
        if type(e) is not list or len(e) != len(NAMES) or any(type(i) is not int or not 0 <= i <= 12 for i in e):
            raise ValueError("fixed nonnegative exponents")
        e = tuple(e)
        if previous is not None and not previous < e:
            raise ValueError("unique ordered polynomial terms")
        if type(c) is not str or len(c) > 80:
            raise ValueError("rational string")
        q = F(c)
        if str(q) != c or not q:
            raise ValueError("canonical nonzero rational")
        out[e] = q
        previous = e
    return out
