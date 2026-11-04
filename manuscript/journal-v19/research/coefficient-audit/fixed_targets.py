"""Externally fixed semantic targets, independently derived from integrands.

This file, not the submitted proof object, defines the accepted family.
It contains no certificate-supplied expressions or executable data.
"""
from fractions import Fraction as F
from poly import add, const, derivative, integral, mul, power, scale, substitute, variable

x, a, b, r, t, u, v, g = [variable(s) for s in ("x", "a", "b", "r", "t", "u", "v", "g")]


def targets():
    # Central integrals: J2 uses t|t|, so its negative half has opposite sign.
    p1 = integral(mul(add(x, a), x), "x", scale(a, -1), b)
    p2 = add(integral(scale(mul(add(x, a), power(x, 2)), -1), "x", scale(a, -1), const(0)),
             integral(mul(add(x, a), power(x, 2)), "x", const(0), b))
    central = add(mul(r, p1), scale(p2, -1))
    at_r = substitute(central, {"b": r})
    q3 = add(x, scale(a, 2))
    q4 = add(power(x, 2), scale(mul(a, x), 2), scale(power(a, 2), 3))
    signed = add(q4, const(-3), scale(mul(t, q3), -F(3, 2)))
    out = {"P1": p1, "P2": p2, "G": central,
           "P1_A": derivative(p1, "a"), "P1_B": derivative(p1, "b"),
           "P2_A": derivative(p2, "a"), "P2_B": derivative(p2, "b"),
           "G_B": derivative(central, "b"), "G_at_B_rho": at_r,
           "G_at_B_rho_A": derivative(at_r, "a"),
           "G_at_B_rho_rhorho": derivative(derivative(at_r, "r"), "r"),
           "F": signed, "F_x": derivative(signed, "x"),
           "F_a": derivative(signed, "a"), "F_t": derivative(signed, "t"),
           "F_xx": derivative(derivative(signed, "x"), "x"),
           "F_xa": derivative(derivative(signed, "x"), "a"),
           "F_aa": derivative(derivative(signed, "a"), "a")}
    out["F_stationary"] = substitute(signed, {"x": scale(t, F(3, 8)), "a": scale(t, F(3, 8))})
    out["F_hessian_form"] = add(mul(out['F_xx'],power(u,2)),scale(mul(out['F_xa'],u,v),2),mul(out['F_aa'],power(v,2)))
    # Complete-square witnesses; rhs is independently expanded from the inequality.
    out["outer_positive_square"] = add(power(add(r, scale(a, -1)), 2),
                                         scale(mul(add(x, scale(a, -1)), add(r, scale(x, -1))), -4))
    out["outer_negative_square"] = add(power(add(b, scale(r, -1)), 2),
                                         scale(mul(add(b, scale(x, -1)), add(x, scale(r, -1))), -4))
    # The common Gram determinant after eliminating X and |X|.
    out["projection_determinant"] = add(mul(add(const(1), scale(power(b, 2), -1)), u),
                                         scale(power(r, 2), -1), scale(power(g, 2), -1), scale(mul(b, r, g), 2))
    out["projection_square_form"] = add(mul(add(const(1), scale(power(b, 2), -1)), add(u, scale(power(r, 2), -1))),
                                         scale(power(add(g, scale(mul(r, b), -1)), 2), -1))
    # Conditional identities are checked with their linear term retained.
    for j in (2, 3, 4, 5):
        out["conditional" + str(j)] = add(power(x, j), scale(power(a, j), -1),
                                          scale(mul(power(a, j - 1), add(x, scale(a, -1))), -j))
    return out


MATRICES = ("H0", "H1", "H2", "H3", "L0", "L1", "L2")


def matrix_weight(name):
    k = int(name[1])
    return power(x, k) if name[0] == "H" else mul(power(x, k), add(r, scale(x, -1)))


def bernstein_basis(i, j):
    from math import comb
    return scale(mul(power(x, i), power(add(const(1), scale(x, -1)), 4 - i),
                     power(a, j), power(add(const(1), scale(a, -1)), 4 - j)),
                 comb(4, i) * comb(4, j))


def factorizations():
    return {
      'P1_A':[const(F(1,2)),add(b,scale(a,-1)),add(b,a)],
      'P1_B':[b,add(a,b)],
      'P2_A':[const(F(1,3)),add(b,scale(a,-1)),add(power(b,2),mul(a,b),power(a,2))],
      'P2_B':[power(b,2),add(a,b)],
      'G_B':[b,add(a,b),add(r,scale(b,-1))],
      'G_at_B_rho_A':[const(F(1,6)),add(r,scale(a,-1)),add(r,scale(a,-1)),add(r,scale(a,2))],
      'G_at_B_rho_rhorho':[r,add(r,a)],
      'F_t':[const(-F(3,2)),add(x,scale(a,2))]}
