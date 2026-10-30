# Fourier-to-code audit, 30 October 2026

## Finding and scope

The Fourier estimates in Appendix A are valid under their displayed support,
moment and actual-event hypotheses. The selected `kernel.sixth` and installed
`high_window_core` implement rational upper enclosures of those estimates.
Their evaluation at the floor \(N=42\) is valid for every \(n\ge42\), including
varying laws and varying raw thresholds. No defect was found in this edge.

This is a mathematical audit, not a claim that execution alone proves the
reduction to supported contact witnesses. The support/moment/event acquisition
is audited separately in `coarse-audit.md` and `signed-audit.md`. Once those
inputs and the acceptance trace are established, **the Fourier part needs no
additional conditional assumption or formalization**. The full Berry--Esseen
conjecture and finite indices not covered by the manuscript are not claimed.

| Result | Mathematical status | Execution status |
|---|---|---|
| Compensated inversion | Locally derived and checked for every stated signed measure and threshold | Analytic proof; no numerical integration used |
| LOW, including sharper fifth coefficient | Locally derived and checked under actual support and moment ceilings | Runtime formula correspondence checked below |
| All six HIGH pieces and floor evaluation | Locally derived and checked under an actual iid-copy event and displayed gates | Runtime formula correspondence checked below |
| Acquisition of the support/moment/event inputs | Separate mathematical edge | See coarse/signed audits and parent acceptance replay |

Audited snapshot: repository
`work/manuscript_revision_20261029`, commit
`77d7b4b2510a6ce5b2d8e162bd2a78ecbecec1b5`.
No pinned source or manuscript was edited for this audit.

## Exact sources and runtime route

- `manuscript/compact-v16/appendices/fixed-fourier.tex`, especially propositions
  `v9:fourier:low`, `v9:fourier:high`, and conclusion `v9:fourier:conclusion`.
- `mathematics/fixed-target-v5/2026-10-27/cell-sources/kernel.py`:
  `roots`, `exphi`, `constants`, `sixth`, and `universal_high`.
- `mathematics/fixed-target-v5/2026-10-27/cell-sources/high_window_core.py`:
  `install`, its returned `one` and `best`.
- `mathematics/fixed-target-v5/2026-10-27/cell_check.py`: `run`.
- `mathematics/fixed-target-v6/2026-10-27/signed-two-pass-check.py`: ancestor
  replay using the same initial LOW/HIGH coefficients.
- `mathematics/fixed-target-v7/2026-10-27/signed_core.py`: `init` and `stage`.
- `mathematics/fixed-target-v7/2026-10-27/accept_entry.py`: replay and source pins.

`cell_check.run` installs the HIGH implementation before any Fourier use and
sets `kernel.RADIUS=96/25`. Each signed `stage` first calls `init(p)`, setting
`kernel.RADIUS=p['radius']`, recomputing `K4,K5`, and checking constants. The
acceptor recomputes that radius using `support.cell_radius` and requires exact
agreement with the stored radius before passing it to `stage`. Thus LOW uses
the already acquired support radius for the same cell; no stale radius is used.

The original `kernel.high` is replaced by `high_window_core.install`; it is not
the implementation accepted here. The numerous other exploratory functions in
`kernel.py` were not treated as dependencies simply because they share its file.

## 1. Compensated inversion and normalization

For a finite signed measure \(\mu\) with mass and first moment zero and finite
absolute second moment, the scalar identity

\[
\int_0^\infty [ty-\sin(ty)]t^{-3}\,dt=\pi y|y|/4
\]

has an integrand of constant sign for each fixed \(y\). Its absolute integral
is therefore \(\pi y^2/4\). Applying it with \(y=x-H\) makes the double integral
against \(d|\mu|(x)\) finite. Absolute Fubini is justified, and the linear term
vanishes by the two cancellations. This proves the manuscript's inversion,
including absolute convergence. It does not need continuity at \(H\), a density
for the sum, a fixed law as \(n\) varies, or a limiting operation.

For the Edgeworth signed Gaussian density,
\(\phi(x)[1+\gamma(x^3-3x)/(6\sqrt n)]\), mass is one and first moment zero.
With convention \(f(t)=\mathbb E e^{itX}\), its transform after scaling by
\(\sqrt n\) is exactly
\(e_n(t)=e^{-nt^2/2}(1-in\gamma t^3/6)\).
The distributional identity \(q_z'''=4\delta_z\), where

\[q_z(x)=(x-z)|x-z|,\]

gives the positive correction \(2\gamma\phi(z)/(3\sqrt n)\).
Scaling \(q_{H/\sqrt n}\) contributes \(1/n\); multiplying the resulting error
by \(-n^{3/2}/2\) gives precisely

\[ |E_n|\le (2\sqrt n/\pi)(I_0(H)+I_\infty). \]

Both the sign and the normalization match the displayed manuscript formulas.

## 2. LOW: derivation of the implemented coefficients

Let \(h(t)=\exp(-t^2/2-i\gamma t^3/6)\). For \(0\le t\le1/2\), expansion through
degree five gives

\[
f-h=-at^4-izt^5+r_6,
\quad a=(3-\mu_4)/24,
\quad z=(10\gamma-\mathbb EX^5)/120.
\]

The coefficient of \(it^5\) in \(h\) is \(+\gamma/12\), so the displayed sign
of \(z\) is correct. For \(w=-t^2/2-i\gamma t^3/6\),

\[
|w|\le t^2(1/2+g^2/144)<1/6,
\quad |e^w-1-w-w^2/2|\le |w|^3/5.
\]

The degree-six term in \(w^2/2\) contributes \(g^2t^6/72\), and the true
characteristic-function Taylor remainder contributes \(M_6t^6/720\). Thus

\[
E=M_6/720+g^2/72+(1/2+g^2/144)^3/5,
\quad |r_6|\le Et^6,
\quad |f-h|\le Bt^4,
\quad B=A+Z/2+E/4.
\]

Symmetrization and the global cosine quartic upper bound give

\[
|f|^2\le1-t^2+(M+3)t^4/12
       \le1-(45-M)t^2/48.
\]

Both \(f,h\), and their joining segment, are bounded in modulus by
\(e^{-(45-M)t^2/96}\). Taylor's formula for \(v^n\) therefore bounds its second
remainder by

\[
\tfrac12 n(n-1)B^2t^8e^{-(n-2)(45-M)t^2/96}.
\]

Integration after division by \(t^3\) gives
\(E/(2a_0^2n)+B^2/(2b_0^3n)\), with precisely the manuscript's \(a_0,b_0\).
The imaginary part of the two leading terms gives

\[
\frac{\lambda_N}{\sqrt n}(Z+A|H|+Ag/2),
\quad
\lambda_N=\sqrt{\pi/2}\{N/(N-1)\}^{3/2}.
\]

Finally, the sine/cosine remainders of \(h^n-e_n\) give respectively
\(5\sqrt{\pi/2}g^3/(432\sqrt n)\) and
\(\sqrt{\pi/2}g^2|H|/(24\sqrt n)\). Using
\(\sqrt{\pi/2}<251/200\) yields exactly \(251/17280\) and \(251/4800\).
These calculations establish the entire LOW triple, not separately selected
components from unrelated estimates.

In `sixth(N,M,g,eta)`, actual support gives \(M_6=R\eta\), and
\(A=\max(2,M-3)/24\) follows from \(1\le\mu_4\le M\\).
The code's square-root upper enclosure of \((22/7)/(16a_0^3)\) exceeds
\(\lambda_N\), since this radicand is
\((22/7)/2\cdot[N/(N-1)]^3\). Its half is the required second coefficient.
All three returned quantities match the derivation.

### The sharper fifth coefficient is justified

For \(Q=X^2-\gamma X-1\), direct expansion gives

\[
\mathbb EQ^2=\mu_4-1-\gamma^2,
\qquad
\mathbb EX^5=\gamma^3+2\gamma+\mathbb E[Q^2(X+2\gamma)].
\]

Reflect the auxiliary calculation to \(t=|\gamma|\ge0\). For
\(r\ge\max(R,2g)\), the two signs of the fifth-coefficient numerator are at
most

\[
P_r(t)=r(M-1)+(10-2M)t-rt^2+t^3,
\quad Q_r(t)=r(M-1)+(2M-10)t-rt^2-t^3.
\]

The replacement of \(\mu_4\) by \(M\) is legal because its coefficients are
\(r-2t,r+2t\ge0\). For \(M\le5\), \(P_r\ge Q_r\), and replacing \(t^3\) by
\(gt^2\) gives the concave quadratic maximized at the clipped vertex in the
code. For \(M>5\), \(P_r\le r(M-1)\), while dropping \(-t^3\) from \(Q_r\)
gives the other clipped quadratic. The separately used \(r=6\) is legal
because \(R\le6\) and \(2g<4\). Its increasing-endpoint branch follows from
\(P_6''=-12+6t<0\); its remaining branches are unrestrained quadratic upper
bounds. Taking the minimum with the triangle bound \(\eta+10g\), then dividing
by \(120\), is valid. All branches in `sixth` match these formulas.

## 3. HIGH: all frequency sets are covered

The hypotheses require one event for independent copies from the same
marginal, with probability at least \(\alpha>0\), distance at least \(d>0\),
and conditional squared distance at most \(M_E\). Symmetrization and convex
Jensen give

\[
|f(t)|^n\le e^{-n\mathbb E\sin^2(t(X-X')/2)}
\le\mathbb E[e^{-n\alpha\sin^2(tD/2)}\mid\mathcal E].
\]

This inequality uses the actual event; it does not replace the law by an
optimizer of a relaxation. Positive Tonelli permits a separate partition for
each possible \(D>0\). With \(\ell=2\pi/D\), the zero cell and nonzero cells
cover the entire positive axis; atom locations in \(D\) do not affect this.

The six terms have the following exact provenance:

1. On \([1/2,9/10]\), the concave quartic exponent has its minimum at one
   of the two endpoints. The integral of \(t^{-3}\) is less than \(2\).
2. In nonzero-cell cores, the sine lower bound is \(h|v|\). Symmetric Taylor
   averaging gives \(j^{-3}+6(j-r)^{-5}v^2\). Its Gaussian moments and the
   Jacobian \(D^2/(4\pi^2)\) give exactly the displayed \(T_2\), including
   the coefficient \(3/(n\alpha h^2)\).
3. Nonzero-cell wings have sine at least \(hr\). Their total weight is at
   most \(D^2/(2\pi^2)\), yielding \(T_3\).
4. On the small-angle part of the zero cell,
   \(\sin(tD/2)\ge(23/48)td\). Extending to \([9/10,\infty)\) gives \(T_4\).
5. The remaining zero-cell part has sine at least \(23/48\) and total
   weight at most \(1/[2(9/10)^2]\), giving \(T_5\).
6. The entire comparator tail \([1/2,\infty)\) is retained. Its Gaussian
   part uses the rational tail bound below; its cubic part uses
   \(int_{1/2}^\infty e^{-nt^2/2}dt\le2e^{-n/8}/n\) and Pearson's
   \(\gamma^2\le M-1\), yielding exactly \(T_6\).

All extensions enlarge nonnegative integrals. No sign orthant, endpoint,
lattice peak, or comparator contribution is dropped.

### Optional rational tail improvement

For \(U\sim\operatorname{Exp}(1)\), substitution and integration by parts give

\[
\sqrt n\int_b^\infty e^{-na t^2}t^{-3}dt
=\frac{\sqrt n e^{-x}}{2b^2}\mathbb E\frac{U}{x+U},\quad x=nab^2.
\]

The positive weighted-square inequality for a linear polynomial in \(U\) has
Gram matrix

\[G=\begin{pmatrix}x+1&x+2\\x+2&2x+6\end{pmatrix}.\]

Its determinant is \(x^2+4x+2>0\), and minimizing the square gives
\(\mathbb E[1/(x+U)]\ge(x+3)/(x^2+4x+2)\). Therefore
\(\mathbb E[U/(x+U)]\le L(x)=(x+2)/(x^2+4x+2)\).
This proves the optional zero-cell estimate directly.

The first-piece improvement follows from the exact nonnegative chord residual

\[
c(u)-c_q-s(u-1/4)
=(M+3)(u-1/4)(81/100-u)/24.
\]

When \(s>0\), extending the chord majorant to infinity and using the same tail
bound yields precisely \(2\sqrt n e^{-nc_q}L(ns/4)\).

### Why evaluating at 42 is valid

The gates in `one` assert positivity and \(2Nc'>1\) for all terms of the form
\(\sqrt n e^{-nc'}\). Terms \(n^{-1}\) and \(n^{-1/2}e^{-nc'}\) decrease without
that extra restriction. The rational tail function has \(L'<0\). The optional
first term has its own \(2Nc_q>1\) test. The derivative sign of
\(\sqrt x e^{-x}L(x)\) is the sign of

\[4-10x-22x^2-13x^3-2x^4.\]

It is negative at \(1/4\) and strictly decreasing thereafter. Accordingly the
optional zero-cell term is used only when \(N\kappa b^2\ge1/4\). The comparator
decreases for \(n\ge5\). These are inequalities for scalar majorants, not claims
that characteristic functions of different laws decrease in \(n\).

`best` evaluates complete six-term sums at each allowed window and takes their
minimum. Each `one` checks all its gates; there is no acceptance of an invalid
window with a silently missing term. The per-term optional minima are also
valid because each option bounds the same respective contribution.

## 4. Directed arithmetic and the final budget

- `down` is the exact rational floor to its grid, including negative inputs;
  `up=-down(-x)` is the corresponding ceiling.
- `roots(x)` obtains \(k=\lfloor\sqrt{x s^2}\rfloor\) by integer square root
  and checks \( (k/s)^2\le x\le((k+1)/s)^2\).
- `exphi(x)` puts \(y=\lfloor\min(x,64)\rfloor_{10^{-6}}\le x\), then uses
  \(1/\sum_{j=0}^{64}y^j/j!\ge e^{-y}\ge e^{-x}\), rounded upward. The
  truncation and the cap at \(64\) weaken the bound in the safe direction.
- HIGH uses lower enclosures for \(\pi,\sqrt\pi,\sqrt\alpha,\sqrt N\) in
  denominators and upper enclosures for square roots in numerators. All
  relevant coefficients and terms are positive. The constants are verified
  using the explicit Machin identity and positive-integral bound in the
  manuscript; no floating-point value of \(\pi\) is assumed.
- LOW uses a square-root upper bound for its normal factor. Combining its
  triple with HIGH and the inversion factor gives exactly
  \(K_F=(16/25)(L_0+K_H+L_2/\sqrt N)\) and slope \((16/25)L_H\), with the
  denominator (sqrt N) rounded downward. This uses \(2/\pi<16/25\).

The rounded algorithms themselves need not be monotone in \(N\). The proof
establishes monotonicity of the real majorants and then rounds their value
at \(N=42\) upward, which is sufficient.

## 5. Reproduction and adversarial controls

The companion `fourier_runtime_audit.py` installs in-memory wrappers around
the selected LOW/HIGH functions while leaving their files and behavior
unchanged. It calls the full entry acceptor, reconstructs every encountered
LOW triple and every complete candidate HIGH sum from the formulas above
using a separately written rational evaluator, and requires exact equality.
It also records all radii and the minimum margins of every mandatory gate.
Its input hashes, Python version, counts, runtime, and acceptor summary are in
`runs/certificate_discharge_20261030/fourier/runtime-audit.stdout.json`; stderr
is retained alongside it. This is a formula-correspondence diagnostic, not
independent verification of the common analytic hypotheses.

Fresh result: **PASS**, return code 0, Python 3.9.6 without optimization,
110.168432375 seconds. The diagnostic checked 5,316 LOW calls (2,455 distinct
parameter tuples), 144 direct complete HIGH calls, and 10,512 HIGH minimum
calls (29,934 distinct complete window tuples). All exact equalities and
mandatory gate margins passed. Nineteen actual radii ranged from \(5/2\) to
\(96/25\). The full entry replay returned
`PASS_INITIAL42_FIXED_TARGET_COARSE_V7`, with 11,264 signed cells, 100 panels,
raw ceiling \(10997587/5000000\), and defect ceiling \(76682509/100000000\).

The already supplied `fourier-check.py` was read before execution. Its exact
identities include the Taylor sign, chord residual, tail derivative, and
rational constant identities. Its adversarial controls show that removing
the damping gate or the quarter gate can invalidate monotonicity, changing
the fifth-coefficient sign is wrong, and losing first-moment cancellation
breaks compensated inversion. Symmetric and skew Bernoulli laws (including
reflection), a three-point law, a zero atom, and distant symmetric atoms
check the moment identities and coefficient bounds. Its finite parameter
grid is explicitly diagnostic; the universal inequalities are proved above.
Its fresh result was `PASS_BOUNDED_FOURIER_IDENTITIES_AND_CONTROLS`, return
code 0, with seven identity groups, six actual laws, 1,394 scalar diagnostic
points, and all six initial window gates. The source repository remained
clean after these runs. `execution-record.json` records commands, exit codes,
and source/output hashes for both runs.

## 6. Remaining edges and suggested manuscript action

No additional Fourier computation is needed beyond the accepted full trace
and the verified support/moment/event acquisitions. Cite Appendix A as a
proved estimate rather than list it as an unresolved analytic premise. In
the certificate theorem, retain its explicit hypotheses on actual witnesses,
then discharge those hypotheses with the support and signed/coarse lemmas.
The acceptor's historical string saying “conditional on ... premises” reports
its modular scope; it does not invalidate a later proof of those premises.

This audit does not independently establish attainment/contact, the scalar
resource inequality, the predecessor entry ceiling, the signed continuous
cell cover, later local comparison, or finite-base coverage. Those are actual
separate edges. They must be reconciled by the parent audit before changing
the global theorem's status. Absence of a proof-assistant formalization is
not among the remaining mathematical obligations.
