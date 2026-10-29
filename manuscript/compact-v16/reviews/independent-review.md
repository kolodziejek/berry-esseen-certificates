# Independent mathematical review of the selected revisions

Target: `manuscript/compact-v16`, based on commit
`cd10654222f4b63d50f9d8f108597b140d263ec5`. Review date: 29 October 2026.
The external Markdown plan is a source of proposed changes, not evidence
that those changes are correct. Original formulas were read directly from
the pinned Git object before comparison with the revised source.

| Item | Mathematical status | Execution status |
|---|---|---|
| Exponential-tail bound by a two-dimensional quadratic form | Independently derived below; same domain and same `L(x)` as the original | Fresh exact coefficient checks pass |
| Narrow enclosure of `C_E` | Directed analytic enclosure plus exact comparisons | Fresh rational comparisons pass |
| Global minorant with `alpha=1/2` and its phase rectangle | Independently derived below; same law domain | Fresh polynomial and endpoint checks pass |
| Common error envelope and one final quartic | Independently derived from the two original envelopes | Fresh coefficient identity and endpoint checks pass |
| Joint gap budget, probability distance and support rays | Independently derived below; original hypotheses retained | Fresh exact scalar checks and seven actual-law diagnostics pass |
| Contact/off-contact split | Formula-by-formula comparison and sign derivation below; no lost residual or endpoint term found | Source review; no claim that arithmetic proves this identity |
| Entry certificate, global finite base, full conjecture | Outside this review's verification scope | Not established by these checks |

The new acceptance program is `tools/check_revision_foundation_constants.py`.
It uses only integers and `fractions.Fraction`, refuses optimized Python, and
reconstructs the compared expressions from their rational definitions. The
analytic reasons why endpoints suffice remain in the manuscript and here.
It does not infer a continuous-domain claim from its actual-law examples.

## 1. Fourier tail: independent derivation

For `a,b,n>0`, set `x=nab²`. The change of variable
`v=na(t²-b²)` gives

\[
\sqrt n\int_b^\infty e^{-na t^2}t^{-3}\,dt
=\frac{\sqrt n e^{-x}}{2b^2}
\int_0^\infty \frac{x e^{-v}}{(x+v)^2}\,dv.
\]

Integration by parts turns the last integral into
`1-x E[1/(x+U)]=E[U/(x+U)]` for a unit exponential `U`.
All integrands are integrable because `x>0` and exponential moments of
every nonnegative integer order are finite.

For `q(U)=c₁+c₂U`, expansion of a nonnegative square gives

\[
0\le E\frac{[1-(x+U)q(U)]^2}{x+U}
=J_x-2(1,1)c+c^TGc,
\quad G=\begin{pmatrix}x+1&x+2\\x+2&2x+6\end{pmatrix}.
\]

Its leading diagonal entry is positive and its determinant is
`x²+4x+2>0`. Minimization is therefore legitimate. The adjugate quadratic
form is `(x+1)+(2x+6)-2(x+2)=x+3`, whence

\[
J_x\ge\frac{x+3}{x^2+4x+2},\qquad
E\frac U{x+U}\le\frac{x+2}{x^2+4x+2}.
\]

This is exactly the original tail function, with no change in `a,b,n`.
The six high-frequency terms, all optional conditions, all-index decrease,
and the comparator tail were left intact. In particular, this replacement
does not remove the nearly lattice nonzero-cell contribution.

## 2. The narrow target enclosure

The existing normalization appendix proves Machin's identity with the
correct tangent branch. Integrating the finite geometric expansion of
`1/(1+t²)` gives alternating arctangent bounds: an even number of terms is
lower, an odd number upper, for `0<x<1`. Consequently

\[
16s_{10}(1/5)-4s_5(1/239)<\pi
<16s_9(1/5)-4s_4(1/239).
\]

The reversed term choices at `1/239` are necessary because its coefficient
is negative. Both rational endpoints are positive. The rational numbers
`3162277660168379/10^15` and `3162277660168380/10^15` enclose `sqrt(10)`
by integer squaring. Since

\[
C_E^2=\frac{19+6\sqrt{10}}{72\pi},
\]

using the lower numerator with the upper denominator gives a lower bound,
and the opposite pair gives an upper bound. Exact comparison proves
`4097321837023/10^13<C_E<4097321837025/10^13`.
This is a reproducible precision specification; it does not change any
entry certificate constant.

## 3. Small-noise replacement

The proposed polynomial is

\[
h(x)=\frac45x(1-x)(2x+1)^2
=\frac{-16x^4+12x^2+4x}{5}.
\]

For `x<=0` and `x>=1`, the first factor product is nonpositive. On `(0,1)`,

\[
h'(x)=-\frac45(2x+1)(8x^2-4x-1),
\]

so the only internal critical point is `(1+sqrt(3))/4`. Its value is
`(9+6sqrt(3))/20<1`, because `3<(11/6)²`. The endpoint values vanish.
Thus `h<=1_(0,infinity)` on the whole line, including the strict-event
threshold. There is no assumption that the conditional sum lies in
`[-3/5,3/5]`.

Let `EW=0`, `EW²=t`, `|EW³|<=At`, and `EW⁴<=A²t+3t²`.
Expansion at `W+epsilon*r`, with `r=zt`, bounds the fourth moment term by

\[
-E(W+\varepsilon r)^4
\ge-A^2t-3t^2-4rAt-6r^2t-r^4.
\]

The quadratic and linear terms have expectations `t+r²` and `epsilon*r`.
Dividing by `t>0` gives exactly the displayed `F_(epsilon,b)` with
`alpha=1/2`, denominator `5/16`, and the appropriate normal correction
`b*z`. The proof extends the polynomial continuously to `t=0` only to
bound the rectangle; it does not divide by zero for the actual law.

For fixed `z>=0`,

\[
\partial_t^2F=-\frac{12z^2+6tz^4}{5/16}\le0.
\]

Therefore the minimum over `0<=t<=101/10000` occurs at one of the two
endpoints. On `0<=z<=3/2`, the inequality `z⁴<=(9/4)z²` gives a lower
quadratic. Its quadratic coefficient is nonnegative at both t-endpoints.
The negative-phase derivative is strictly negative even at `z=3/2`;
the positive-phase derivative is positive already at `z=0`. The four
exact minima, computed from these coefficients, are

\[
\frac{933}{1000},\quad
\frac{3849022385619}{5000000000000},\quad
\frac{156}{125},\quad\frac{3597}{3125},
\]

all greater than `3/5`. This validates the same own-count estimate.
The subsequent Cantelli, tail, normalization, and final-margin arguments
are not replaced by this calculation.

## 4. One error envelope and one quartic

Starting from the two *original* envelope formulas, subtraction cancels
the common `T/4`, `5M4/3`, and constant normal-interpolation terms. After
multiplication by `V_*`, the result is

\[
\beta_0\bar c(\tfrac15+\tfrac52\lambda)
+\beta_0\frac{27M_4}{256}\frac{5\bar c}{4}
+\phi_+\xi(\tfrac18-\tfrac12\lambda).
\]

The constant coefficient is `7889/100000` and the coefficient of lambda
apart from the M4 contribution is `1751/8000`. Since M4 has nonnegative
coefficients and no constant term, the difference is strictly positive
for every nonnegative lambda. Thus `E_+<=E_-` with no new sign or domain
assumption. The two separate normal-correction arguments are still needed
to reach these envelopes.

`E_-` is a nonnegative convex quadratic. Direct differentiation of W gives

\[
W''=-\eta m_*\left\{\frac{z^2}{4}[(z\lambda-1)^2+1]
+\frac{3b^2}{8}\right\}<0.
\]

Consequently `P=W-E_-/700-lambda/100` is strictly concave. Direct rational
evaluation gives

\[
P(1/100)=\frac{19409025049390417531054861}{8386908849900000000000000000}
>0.002314,
\]
\[
P(7/20)=\frac{16788798784733560132189}{273858248160000000000000}
>0.061304.
\]

These two checks suffice on the closed interval. The condition `n>=700`
can replace `E_-/n` by `E_-/700` because `E_->=0`. No conclusion for tiny
positive lambda follows from this polynomial: `W(0)=0<E_-(0)/n`.
The small-noise proof remains indispensable to the selected argument.

## 5. Geometry and rays

Let the central gap be `(-A,B)` with `A,B>0`. There is therefore no zero
atom, and all conditional means and residuals have the stated signs.
The sum of outer-gap bounds is

\[
J\le m(A+B)^2+M_{3,+}-2BM_{2,+}+B^2m
+M_{3,-}-2AM_{2,-}+A^2m.
\]

Substitution in D yields

\[
D\ge(\sigma-1)M_{3,+}+(\sigma+1)M_{3,-}
+6BM_{2,+}+6AM_{2,-}-6m(A^2+AB+B^2).
\]

For the positive class, expanding around its conditional mean gives
`M2+=m*barB+E[W²;X>0]` and
`M3+=m*barB²+E[(X+2barB)W²;X>0]`; the linear residual terms vanish by
conditional centering. The negative counterpart uses `-X,barA`.
Substituting `A=ell(p-a0)`, `B=ell(q-a1)` and `m=pq*ell` gives the
deterministic coefficient

\[
\ell w\{(\sigma+1)p^2+(\sigma-1)q^2-6pq
+6[d(1-d)+a_0a_1]\}.
\]

This proves the new joint budget. Here `0<=d<1` follows from
`A+B=ell(1-d)>0`, so all its displayed terms are nonnegative. On the
positive class `X,barB>=B`, making its kernel at least `3(sigma+1)B`;
on the negative class it is at least `3(sigma+3)A`. This recovers the
original simultaneous-gap inequality, with its exact displacement term.
No higher moment is used. Tonelli handles countably many gaps, and the
expectations are bounded by constants times `1+|X|³`.

For probability localization, once the original bootstrap has proved
`D>=Q(p)/sqrt(pq)`, use `sqrt(pq)<=1/2`. Directed root comparisons give
`3/8<p_*<21/50`, and `21/50` is the midpoint of the desired probability
interval. Every point outside that open interval is at least as far from
`p_*` as `3/8`. The exact lower endpoint test is

\[
Q_-(3/8)=\frac{37936011}{1600000000}>\frac{47}{2000}.
\]

The original bootstrap is still needed to reach `D>=Q/sqrt(pq)`.

For the two rays, the exact six scalar boundary comparisons were computed
independently using the original `h,Q_b,g` definitions. At the respective
boundaries `t²>3`, so h is nonnegative. Also
`L''=2/5-6(819/2000)=-2057/1000<0`; the negative boundary values of L and
L' persist outward. Since g is positive,
`Q_b'=(L-g)/c0<0`, and the negative boundary value of `h+c0 Q_b` implies
`Q_b<0` there and thereafter. Finally `C_E>c0` makes both the actual
boundary upper expression and its derivative negative. This rules out
contact on each entire closed ray, without differentiating h's absolute
value. The original threshold-uniform bounds on H_n and its derivative
remain prerequisites.

Seven exact atomic-law diagnostics cover symmetric/skew Bernoulli,
nearby three/four atoms, a tiny distant atom, an exact support collision,
and a five-atom law with a nonzero outer-gap surplus. The first six have
zero gap-estimate surplus and the last has surplus `72/25`; this checks
the actual gap computation rather than merely repeating a symbolic zero.
They are diagnostics only. The general proof is the preceding derivation.

## 6. Conservation restructuring audit

The revised contact proof removes exactly the residual terms that vanish
on the closed support. The original gap calculation adds the support
residual to A, whereas the first-moment calculation changes
`M+phi` by `-sqrt(n)*xi`. In the expression for `sqrt(n)*A`, the latter
becomes `+H*sqrt(n)*xi`. Equating the two evaluations and multiplying by n
therefore gives precisely

\[
\text{conserved left side}=\mathcal R_c+n^{3/2}(R_{\rm supp}-H\xi).
\]

The off-contact appendix keeps both the Lebesgue integral over K and the
right-endpoint residual sum. Its uniform-law counterexample checks why
the integral cannot be discarded. The half-open leakage interval `[u,v)`
and zero weight of a left-endpoint atom are preserved. Definitions of
`z,F,beta,gamma` remain in the fixed-target section. The new contact proof
uses the same q_z pointwise identity; its bracket is zero at an atom
at the threshold, so no continuity has been introduced.

During review, the moved resource proof temporarily omitted the local
definition `w=H²/(2n)` before using `e^w`; this was reported to the
coordinator for repair. This is a source-restructuring issue, not a new
mathematical assumption. A duplicate capitalized “Let” in the remainder
definition was also reported. The final assembly must contain the repair.

## 7. Negative controls and limits

The exact checker rejects: a CE lower endpoint raised beyond the proven
upper value; an upper endpoint lowered below the lower value; an altered
Fourier numerator; the false lower claim `F>4/5` at its worst endpoint;
an overstated quartic margin `P(1/100)>0.003`; and the false probability
endpoint claim `Q_-(3/8)>0.024`. These are acceptance-predicate controls,
not malformed entry-certificate tests. The existing certificate's parser,
coverage, and mutation controls were not replaced or audited by this script.

No speculative alternative from the external plan was used as a premise.
In particular, a linear moment theorem does not reduce the nonlinear iid
CDF problem to finitely many atoms, a fixed-law limit is not a uniform
remainder, and a larger index does not by itself remove lattice peaks.
This review does not prove the finite base through 699, formally verify
the Python runtime, or certify every inherited analytical lemma.
