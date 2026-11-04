# Fixed-phase polynomial witnesses and the enlarged normalizer

This supplements `EXPECTATION_RULE.md`; it does not change the recorded sources or captures of that theorem. In its quartic proof, the displayed derivative and maximum are those of the **numerator** `s(2a-s)(s+a)^2`; division by the positive `Ka^4` gives the stated minorant.

## A finite certificate on one phase and noise rectangle

Retain the actual coupled process and the inward spacing `c>1/2`. Fix a closed phase interval `[a,b]` inside `[-1/2,1/2]`, a uniform incoming ratio `R0`, and a real polynomial

\[
 q(w)=q_0+q_1w+q_2w^2+q_3w^3+q_4w^4,\qquad q_4\ge0.
\]

Define the exact staircase payoff

\[
 \psi(w,u)=-\mathbf1_{\{w>u\}}
       +R_0\left\lfloor\frac{u-w}{c}\right\rfloor_+.
\]

For fixed `w`, this function is nondecreasing in `u`, including its jumps. If `q(w)>=psi(w,b)` for every real `w`, then `G(R)<=q(W_k)` for every actual phase `u` in `[a,b]`. This uses the pathwise bound proved in the preceding note; it does not assume the process is determined by its own-count distribution.

Here is a complete finite soundness interface for the global majorant. Choose an integer `M>=1` and verify:

\[
\begin{array}{ll}
 q(w)+1\ge0& (w\ge b),\\
 q(b-cx)-R_0m\ge0& (x\in[m,m+1],\ m=0,\ldots,M-1),\\
 q(b-cx)-R_0x\ge0& (x\ge M).
\end{array} \tag{1}
\]

At an integer staircase knot, the interval beginning at that knot supplies its correct larger value. The last knot is supplied by the ray. The first finite interval includes `x=0`, so `q(b)>=0`; the strict outgoing event has not been closed by mistake. Each finite-interval claim can be proved by a Bernstein expansion on that entire interval. For a ray polynomial `P(s)` of degree at most `d`, substitute `s=y/(1-y)` and check

\[
 (1-y)^dP\left(\frac y{1-y}\right)\ge0\qquad(0\le y\le1).
 \tag{2}
\]

For the right ray take `s=w-b`; for the left ray take `s=x-M`. A nonnegative Bernstein expansion in (2) is sufficient and is exact rational algebra when all inputs are rational. The endpoint `y=1` verifies the leading asymptotic coefficient; division back is made only for `y<1`, which corresponds to every finite point of the ray. Positive leading coefficient and sampled stationary values alone are not the certificate format asserted here.

Let `t=E W_k^2`. The actual same-law moment identities and `|U_j|<=A` give

\[
 E q(W_k)\le q_0+(q_2+A|q_3|+A^2q_4)t+3q_4t^2. \tag{3}
\]

The sign restriction `q4>=0` is essential to this particular substitution of an upper fourth-moment bound. The coefficient `q1` vanishes by centering; no independent optimization of the conditional moments is performed.

If the original phase normalization gives `f(0)=0` and `0<lf<=f'<=hf`, put

\[
 L_f(a)=\begin{cases}l_fa,&a\ge0,\\h_fa,&a\le0.\end{cases}
\]

Then `f(u)>=L_f(a)` for every `u` in `[a,b]`. This bound is uniform over the actual normalizing parameters; one must not substitute a literal value `f(a)` computed using a different count displacement. Combining the inequalities gives

\[
 E G(R)-f(u)\le B(t):=
 q_0-L_f(a)+(q_2+A|q_3|+A^2q_4)t+3q_4t^2. \tag{4}
\]

For `0<=T_L<=t<=T_U`, an exact check

\[
 B(T_L)+\eta T_L\le0,\qquad B(T_U)+\eta T_U\le0 \tag{5}
\]

proves `EG-f<=-eta*t` on the whole interval: `B(t)+eta*t` is convex because `q4>=0`, so it lies below the chord joining its endpoint values. With `t>=omega_minus*lambda`, the existing strict normalization gate from equation (16) of the preceding note gives the unchanged target. If a noise band is specified in `lambda`, use the containing actual-variance interval `[omega_minus*L,omega_plus*U]`; do not identify `t` and `lambda`.

Thus (1), exact polynomial identities proving the Bernstein expansions, the moment-sign gates, (5), and the final score gate are a complete finite certificate for this cell. They replace both the incoming-tail and whole-count expectation calculations **on cells where all these checks succeed**. Full coverage of the manuscript's domains is a separate obligation.

## Why fixed phase cells cannot cover arbitrarily small noise at zero

There is a precise limitation of this particular interface, not of the theorem.

If `a<0<=b`, the majorant requires `q(0)>=psi(0,b)=0`, whereas `L_f(a)<0`. Hence `B(0)>0`, and `B(t)/t` tends to positive infinity. No fixed polynomial accepted by this rule can establish a negative reserve proportional to `t` all the way to zero on such a cell.

Even for a one-sided cell `[0,b]` with `b>0`, `psi(w,b)=0` in a neighborhood of `w=0` because `b<c`. A continuous polynomial majorant with `q(0)=0` therefore has a local minimum there: `q1=0` and `q2>=0`. Under `q4>=0`, the coefficient `q2+A|q3|+A²q4` in (4) is nonnegative. If instead `q(0)>0`, the constant term already obstructs the desired noise-relative bound. Thus this moment-envelope interface cannot produce the strict negative reserve on a fixed positive-width phase cell touching zero as `t` tends to zero.

This is why the explicit scaled cells `u=zt` in the TINY construction are mathematically useful. A fixed-phase certificate above a positive noise floor is compatible with a separate scaled certificate below it. Merely increasing the degree or sampling smaller positive variances does not remove the constant-term obstruction for the fixed-phase lower bound used in (4).

## Exact normalization extensions

The old `tiny47wide_normalization.py` has been copied unchanged as `normalization_source.py`, with SHA-256

`f1e2606359e321d17db11c7240467a597f00094d1747d40ed4f69ceae18d4b71`.

`recompute_normalizer.py` constructs two newly named parameter scopes, `0<lambda<=2/25` and `0<lambda<=9/100`. It keeps the same `n>=47`, `p in [.304,.47]`, `|H|<=1.393`, `theta<=.0154`, inward bound `.0181`, and amplitude `.425`. It recomputes, with exact outward rational rounding, only the log ceiling/exponential multiplier, derivative bounds, cubic multiplier, and repair affected by the larger noise ceiling. The original 41 gate formulas are evaluated unchanged in the new interpreter process.

| Noise ceiling | Derivative lower | Derivative upper | Nonnegative repair coefficient |
|---|---:|---:|---:|
| `.08` | `.86879` | `1.13121` | `2.38196` |
| `.09` | `.86806` | `1.13194` | `2.38276` |

The mass lower bound `.7105`, own-variance factors `.91595` and `1.08405`, incoming ratio `1.06842`, inward support, and all phase/count segment parameters are unchanged. The complete rational configurations and all positive gate values are in `runs/joint_count_20261104/analytic_normalization01/checked/RESULT.json`. The process returned zero. A negative control retaining the old constants while changing only the noise ceiling to `.08` rejected at the log-ceiling gate, as it should.

This establishes the exact arithmetic side of the same analytic normalization inequalities on the two larger explicit noise ranges. It does not establish acquisition, a global polynomial majorant, closed phase coverage, or the strict comparison on either range. Those remain separate certificate obligations.
