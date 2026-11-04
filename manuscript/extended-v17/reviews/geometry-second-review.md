# Independent review of the geometry substitutions

Reviewed `sections/05-geometry-counts.tex`,
`sections/07-direct-acquisition.tex`, the contact/heat formulas in
`sections/04-fixed-entry.tex`, and
`tools/check_revision_geometry_constants.py`. I did not use the geometry
constructor's review note. This review rederived the changed formulas from
the conditional-mean decomposition and the manuscript's contact inequality.

**Conclusion:** no mathematical defect was found in the joint budget,
its corollary, the single probability-endpoint exclusion, or the revised
radial monotonicity proof. One inherited explanatory sentence needs a small
scope correction, recorded below. This is a review of these replacements,
not an independent audit of every unchanged entry or acquisition estimate.

| Item | Mathematical status | Execution status |
|---|---|---|
| Joint defect budget (G) | Independently derived below, including unbounded support with finite third moment | Fresh independent formal polynomial expansion had zero residual |
| Old simultaneous-gap bound as corollary | Independently derived from the pointwise kernels | Algebraic derivation; no separate numerical condition needed |
| Single probability-endpoint exclusion | Independently derived from the inherited `D>=Q/sqrt(pq)` bound | Fresh rational substitution reproduces positive surplus `336011/1600000000` |
| Two-ray monotonicity | Independently derived from actual Gaussian derivative bound and contact | Six strict boundary comparisons rechecked from expanded polynomial coefficients |
| Constructor's scalar checker | Read and found to reconstruct meaningful rational expressions | Not rerun by this reviewer; constructor's execution remains separately reported |

## 1. Joint budget derived from the actual law

Assume `P in mathcal P` and the central complementary interval is
`(-A,B)`, with `A,B>0`. Then there is no zero atom. Write
`p=P(X>0)`, `q=1-p`, `m=E X_+=E X_-`,
`bar A=m/q=ell p`, `bar B=m/p=ell q`, and
`W=X-E(X|B_0)`. These are quantities of the original marginal.

For a positive outer gap `(a,b)`, `a>=B`, and

\[
(b-a)^2\le 2\int_a^b(t-B)\,dt.
\]

The density `tau` is constant on that gap. Summing and using Tonelli gives

\[
J_o^+\le2\int_B^\infty(t-B)\tau(t)\,dt
=E[X_+(X_+-B)^2].
\]

The analogous negative-side expression holds in magnitude. Together with
the central contribution `m(A+B)^2`, this implies

\[
D\ge(\sigma-1)M_{3,+}+(\sigma+1)M_{3,-}
+6BM_{2,+}+6AM_{2,-}-6m(A^2+AB+B^2).
\]

Conditional centering yields

\[
M_{2,+}=m\bar B+E[W^2;X>0],\qquad
M_{3,+}=m\bar B^2+E[(X+2\bar B)W^2;X>0].
\]

For example, expansion of the right-hand cubic expression reduces to
`E[X^3;X>0]` because `p bar B=m`. The corresponding negative identity
uses `-X` and `bar A`. Consequently the variance kernels are exactly

\[
(\sigma-1)(X+2\bar B)+6B,
\qquad
(\sigma+1)(-X+2\bar A)+6A.
\]

For the deterministic terms put `A=ell(p-a_0)`, `B=ell(q-a_1)`,
`d=a_0+a_1`, and `w=pq ell^2=1-theta`. The factor outside is
`m ell^2=ell w`. The relevant elementary identity, with `p+q=1`, is

\[
\begin{split}
&(q-a_1)q+(p-a_0)p
-\{(p-a_0)^2+(p-a_0)(q-a_1)+(q-a_1)^2\}+pq\\
&\hspace{2cm}=d-d^2+a_0a_1.
\end{split}
\]

This gives exactly `ell w{Q+6[d(1-d)+a_0a_1]}`. I checked the identity
again by a small formal polynomial expansion in `p,a_0,a_1`; every
coefficient of the difference vanished. Since the conditional means lie
beyond the inner endpoints, `a_0,a_1>=0`, while
`1-d=(A+B)/ell>0`. The squared expression for `Q` and positivity of both
kernels prove every claimed nonnegativity.

Compact support is unnecessary for this lemma: the gap integrands are
nonnegative, and the kernels times `W^2` grow at most cubically. Finite
third absolute moment therefore supplies integrability, and Tonelli or
monotone convergence justifies the countable gap sum. Endpoint atoms do
not change these Lebesgue integrals. This argument does not change the
closed-CDF conventions in the separate contact argument.

## 2. Recovery of the previous simultaneous-gap inequality

On the positive support, `X>=B` and `bar B>=B`, so its variance kernel
is at least `3(sigma-1)B+6B=3(sigma+1)B`. On the negative support the
bound is `3(sigma+1)A+6A=3(sigma+3)A`. Their integrals are the old
`theta_+` and `theta_-` terms. Further,

\[
\ell wQ=\frac{w^{3/2}}{\sqrt{pq}}(6+2\sigma)(p-p_*)^2,
\]
\[
6\ell w[d(1-d)+a_0a_1]
=6m\{(A+B)(\Delta_A+\Delta_B)+\Delta_A\Delta_B\}.
\]

Thus the old bound is recovered without losing its full statement. It is
correct to change its environment from lemma to corollary while keeping
the source label. The new bound is stronger because it keeps the actual
support-dependent noise prices used later in acquisition.

## 3. Probability endpoint exclusion

The change begins only after the retained bootstrap and derivative
argument have established `D>=Q(p)/sqrt(pq)`. Since `sqrt(pq)<=1/2`,
`D>=2Q(p)`. Put `l=3/8`, `r=93/200`. The inequalities
`l<p_*<(l+r)/2=21/50` imply

\[
p\notin(l,r)\quad\Longrightarrow\quad
|p-p_*|\ge p_*-l.
\]

Because `Q=(6+2sigma)(p-p_*)^2`, both outside rays are excluded by the
single left endpoint. Replacing `sigma` by its lower bound in the
expanded polynomial decreases `Q`, since its coefficient is `p^2+q^2>0`.
My exact rational evaluation gave

\[
Q_-(3/8)=37936011/1600000000,
\qquad Q_-(3/8)-47/2000=336011/1600000000>0.
\]

Therefore `D>D_0` outside the open interval, contradicting the retained
strict bound `D<D_0=.047`. Both endpoints are excluded strictly. No
derivative claim about `Q/sqrt(pq)` is needed. The preceding bootstrap
interval remains necessary for the earlier derivative argument and has
correctly been retained.

## 4. Whole-ray monotonicity

For a support point of radial magnitude `t`, the original contact formula
has the cubic expression

\[
-t^3+\tfrac32\rho t^2+3\beta(\pm t)+\rho e_n.
\]

The acquired `rho<9/8` and `.066148<beta<.2527`, together with
`e_n<eta=8/875`, give the stated upper `Q_b`: use the lower beta bound
with a negative sign on the negative ray, and the upper beta bound on the
positive ray. The discarded excess term is nonpositive. All coefficients
replaced by upper bounds have the required sign.

The heat bound supplies `H_n(t_0)<=h(t_0)` and the exact radial Gaussian
derivative satisfies `H_n'(t)<=g(t)`. Set `c_0=819/2000` and

\[
L(t)=\left(\tfrac15-3c_0\right)t^2
+3c_0rt+\tfrac15+\tfrac25\eta+3c_0b.
\]

This expanded polynomial follows directly from `g+c_0Q_b'`. Its constant
second derivative is `-2057/1000`. I independently substituted the two
rational boundaries in this polynomial and in `h+c_0Q_b`; all six
displayed conservative bounds held strictly. In particular the positive
surpluses against the bounds on `L'` were `52663/2500000` and
`974859/12500000`, respectively.

Negative `L''` and the boundary value `L'<0` keep `L'` negative throughout
each outward ray. The boundary `L<0` then keeps `L<0`. Since `g>0`,
`Q_b'=(L-g)/c_0<0`. At each boundary `t_0^2>3`, so all terms in `h(t_0)`
are nonnegative. The boundary test `h+c_0Q_b<0` therefore gives `Q_b<0`,
and `Q_b'<0` propagates that sign. Finally `C_E>c_0` gives

\[
H_n(t_0)+C_EQ_b(t_0)<0,\qquad
H_n'(t)+C_EQ_b'(t)\le g(t)+c_0Q_b'(t)=L(t)<0.
\]

The actual contact upper expression remains negative on the whole closed
ray. This rules out boundary atoms as well as exterior support points.
The proof never differentiates the absolute value in `h`. Its conversion
back to `U_0>-.6`, `U_1<.6` uses the strict bounds on `ell`, `p` with the
correct signs. The claimed uniformity in raw `H` follows from the
all-threshold heat and derivative estimates, not from sampling thresholds.

## 5. Checker assessment and one prose correction

The checker evaluates the rational formulas for `Q`, `h`, `Q_b`, `L` and
`L'`, including the required sqrt(10) enclosure and distance comparisons.
It does not merely compare stored results with themselves. The finite-law
routine directly reconstructs `J` from consecutive atom gaps after
centering, and separates the coefficients of `1` and `sqrt(10)` in the
budget. The calculation is homogeneous of degree three, so dividing all
cubic quantities by `variance^(3/2)` would give the standardized statement;
using rational unnormalized coordinates is sound here. Those examples and
the five predicate controls are correctly labelled as diagnostics, not
continuous-domain proof. The scalar checker does not rerun the unchanged
bootstrap or contact/Fourier analysis; the separate historical suite and
analytic argument remain their evidence.

**Small inherited prose issue:** the sign-split subsection says, “Higher
moments are used only for extremal laws, which have compact support”. The
local comparison theorem also uses higher moments for arbitrary laws
satisfying its explicit support assumptions. Prefer: “Higher moments are
used only after a support bound is available: compactness for an attained
extremal law, or the explicit conditional-support assumptions of the local
comparison theorem.” This is a clarification of existing scope, not a
mathematical gap in either proof.
