"""Bounded algebra/application checks; no certificate replay or coverage claim."""
from fractions import Fraction as F
from collections import defaultdict


def add(*polynomials):
    result = defaultdict(int)
    for polynomial in polynomials:
        for powers, coefficient in polynomial.items():
            result[powers] += coefficient
    return {k: v for k, v in result.items() if v}


def scale(polynomial, coefficient):
    return {k: v * coefficient for k, v in polynomial.items() if v * coefficient}


def multiply(left, right):
    result = defaultdict(int)
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            result[(i + k, j + l)] += a * b
    return {k: v for k, v in result.items() if v}


def expectation(polynomial):
    # Monomials in x,t become monomials in t,mu4,mu5,mu6 after
    # E1=1, EX=0, EX^2=1 and EX^3=t. No numerical moment sampling.
    result = defaultdict(int)
    for (i, j), coefficient in polynomial.items():
        assert 0 <= i <= 6
        if i == 1:
            continue
        powers = [j, 0, 0, 0]
        if i == 3:
            powers[0] += 1
        elif i >= 4:
            powers[i - 3] = 1
        result[tuple(powers)] += coefficient
    return {k: v for k, v in result.items() if v}


x = {(1, 0): 1}
t = {(0, 1): 1}
one = {(0, 0): 1}
x2, t2 = multiply(x, x), multiply(t, t)
q = add(x2, scale(multiply(t, x), -1), scale(one, -1))
q2 = multiply(q, q)
expected = [
    {(0, 1, 0, 0): 1, (0, 0, 0, 0): -1, (2, 0, 0, 0): -1},
    {(0, 0, 1, 0): 1, (3, 0, 0, 0): -1, (1, 0, 0, 0): -2},
    {(0, 0, 0, 1): 1, (0, 0, 0, 0): -1, (2, 0, 0, 0): -3, (4, 0, 0, 0): -1},
]
actual = [
    expectation(q2),
    expectation(multiply(q2, add(x, scale(t, 2)))),
    expectation(multiply(q2, add(multiply(add(x, t), add(x, t)), scale(t2, 2), scale(one, 2)))),
]
assert actual == expected
print("Pearson identities: all three exact formal expansions agree.")

a, b = F(1661, 5000), F(429, 1000)
assert (a * (1 + b / 2)) ** 2 < F(8, 49)
assert a * (1 + b / F(15, 8)) == F(159456, 390625)
assert F(159456, 390625) ** 2 < 3 * F(59, 250) ** 2
print("Both contrary-witness structural cutoffs: exact positive-square comparisons agree.")

law = [(F(3, 2), F(4, 13)), (F(-2, 3), F(9, 13))]
mu = lambda k: sum(p * x ** k for x, p in law)
assert mu(1) == 0 and mu(2) == 1
z120, old = 10 * mu(3) - mu(5), F(951, 160)
assert z120 == F(1315, 216) > old
print("Required R<2g counterexample: true120z=", z120,
      "old bound=", old, "shortfall=", z120 - old)

rho = sum(p * abs(x) ** 3 for x, p in law)
beta = sum(p * x * abs(x) for x, p in law)
m = sum(p * max(x, 0) for x, p in law)
eta5 = sum(p * abs(x) ** 5 for x, p in law)
lhs, delta = rho * mu(4) / 2 - eta5 / 4, mu(3) - rho * beta
rhs = rho ** 3 / 4 - delta ** 2 / (8 * m)
assert lhs == rhs
bad_rhs = rho ** 3 / 4 - delta ** 2 / (4 * m)
assert lhs > bad_rhs
print("Signed-loss two-point equality exact; doubled penalty negative control rejected by margin",
      lhs - bad_rhs)
