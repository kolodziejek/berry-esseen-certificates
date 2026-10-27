# Independent review of the revised narrative and conserved identity

27 October 2026. Reviewer worktree: `manuscript-v2-literature`, branch
`manuscript/v2-literature-20261027`. Reviewed the root revision in
`../manuscript-v2` and the promoted conserved-resource candidate in
`../manuscript-v2-conserved`. This report changes neither source tree.

**Recommendation:** integrate the promoted identity and zero-defect corollary.
No blocking mathematical finding was identified in the reviewed statements.
The resource bounds remain conditional on complete remainder and moment
enclosures; the global theorem remains conditional on the sharp finite base
and equality-inclusive local exclusion. The small integration observations
below should be resolved before the final compilation.

## Scope and evidence

| Item | Mathematical status from this review | Execution status |
|---|---|---|
| Two evaluations of the contact slack and conserved identity | Independently rederived under the displayed contact hypotheses | No numerical test required or run |
| Compensated hinge inversion | Independently checked with absolute Fubini under finite absolute second moment | No external Fourier program run |
| Removal of Gaussian weight and phase price | Valid conditional implications; all sign gates retained | No remainder enclosure or certificate evaluated |
| Oriented zero-defect classification | Independently checked for compactly supported standardized laws | No numerical optimization run |
| Exact recurrence and first contrary index | Order, constants, and least-index logic checked against the displayed proof | No fresh replay of earlier arithmetic scripts |
| Abstract, introduction, guide and diagram | Consistent with conditional theorem scope, subject to the editorial notes | No PDF render or full compilation performed in this review |

I did not review all numerical atlases, all finite providers, or every
appendix in this pass. The reference to independently rederived algebra is
not an acceptance of the certificate conditions appearing later.

## Independent derivation of the promoted argument

The candidate's hypotheses explicitly require one centered variance-one
iid marginal, `n>=2`, the raw threshold `H`, positive score `C`, and
`h_P<=Q_H` with equality on the **closed** support. Because `C>0`, the
piecewise cubic grows to infinity in both directions. Contact with a
function taking values in `[0,1]` therefore implies bounded support before
fourth and fifth moments are used. This order avoids a hidden high-moment
assumption.

I checked the coefficients by first clearing all factors of `sqrt(n)`:

\[
 n^{3/2}Q_H(y)=n^{3/2}F+\frac{H\varphi+C\rho}{2}
 -(n\varphi+3C\beta)y
 -\frac{H\varphi+3C\rho}{2}y^2+C|y|^3.
\]

For `nu=Law(H-S_{n-1})`, `h_P(y)=nu([y,infinity))`. On a gap `(a,b)`,
contact at both endpoints gives
`nu([a,b))=Q_H(a)-Q_H(b)`. Integrating from the upper endpoint yields

\[
 \int_a^b(Q_H-h_P)
 =\int_a^b(t-a)(-Q_H'(t))\,dt
  -\int_{[a,b)}(t-a)\,d\nu(t).
\]

The lower endpoint has zero weight; the upper endpoint must be excluded.
Substitution of the cleared coefficients gives exactly

\[
 \mathcal A=\frac{\varphi J}{2\sqrt n}
 +\frac{3C\beta J/2+(H\varphi+3C\rho)J_1-3CJ_2}{n^{3/2}}-L.
\]

This agrees with candidate `first-slack`, line 90. The bounds on the gap
sums are sufficient: `J<=2R`, `|J_1|<=RJ/2`, `|J_2|<=R^2J/2`, and
`L<=2R`. Half-open gaps are disjoint even when an isolated support point
is an endpoint of two gaps.

The signwise identity
`integral tau(t) g'(t) dt = E[X(g(X)-g(0))]`
gives the zero-bias moments `gamma/2`, `M_4/3`, and `M_5/4` used in the
second evaluation. Replacing one summand by an independent zero-biased
copy gives the zero-bias law of `Z=S_n/sqrt(n)` by exchangeability.
Its CDF is

\[
 T=\mathbb E[(Z^2-zZ)\mathbf1_{\{Z\le z\}}],\qquad z=H/\sqrt n.
\]

The factor multiplying an endpoint atom is zero. Integrating the cleared
polynomial with the three moments verifies `second-slack`, line 126,
including the signs `-rho M_4/2` and `-3 beta gamma/2` in `K_q`.
Separately, multiplying contact equality by `X` gives

\[
 n(M+\varphi)=-H\gamma\varphi/2+CK_1,
 \quad M=\mathbb E[Z\mathbf1_{\{Z\le z\}}],
\]

which verifies `truncated-first`, line 141. Here `E[X|X|^3]` in `K_1`
is a signed fourth-order moment, not `M_4`.

For a finite signed measure of zero mass and first moment, the scalar
identity

\[
 \int_0^\infty\frac{ty-\sin(ty)}{t^3}\,dt=\frac\pi4y|y|
\]

has absolute integral `pi y^2/4`. Integrating against total variation
therefore proves absolute Fubini from the stated second-moment assumption,
including after translation by `H`. Cancellation of the linear term
leaves the candidate's **negative** `-4/pi` imaginary-part formula. No
regularity of the law or convention for averaging a CDF jump is needed.

The Gaussian correction has transform
`exp(-nt^2/2)(1-i n gamma t^3/6)`: the characteristic-function convention
is `exp(itx)`, so the cubic term is negative imaginary. The distributional
identity `((x-z)|x-z|)'''=4 delta_z` gives the hinge correction
`2 gamma phi(z)/(3 sqrt(n))`. Scaling a quadratic hinge by `sqrt(n)`
multiplies it by `n`; hence the candidate's
`epsilon=-4/(pi n) integral Im(exp(-itH)V_n(t))/t^3 dt` has the correct
normalization.

Finally, the elementary quadratic-hinge decomposition gives

\[
 T-\Phi(z)=-\tfrac12\{\mathbb E q_z(Z)-\mathbb E q_z(Z_0)\}
 +z(M+\varphi)-z^2(F-\Phi(z)).
\]

Substitution produces
`sqrt(n) A=C rho-gamma varphi/6+P_0/n+sqrt(n) epsilon/2`.
Equating the two slack evaluations thus gives

\[
 C\rho+\sqrt nL=\frac{\varphi}{6}(\gamma+3J)
 +\frac{G-P_0}{n}-\frac{\sqrt n\varepsilon}{2}.
\]

Inserting `gamma+3J=(3+sqrt(10))rho-D` proves every term and sign in
`conserved`, line 211. In particular `E_n=-n^(3/2) epsilon/2`, and its
complete integral bound has factor **`2 sqrt(n)/pi`**. The infinite
high-frequency interval remains part of the error ledger.

## Sign gates and a counterexample to omitting one

The exact unweighted coefficient is

\[
 C_E\rho-\phi(0)D/6=\phi(0)(\gamma+3J)/6.
\]

It is not nonnegative merely because `D>=0`. The candidate correctly first
assumes a complete raw remainder bound `R<=r_0<2N/5`, with `n>=N` and
`C>=C_E`. The preceding identity then gives
`varphi(gamma+3J)/6 > C rho-2/5>0`.
Only after this gate can the Gaussian weight be removed. Since the original
four left-hand costs are nonnegative, an actual witness also forces every
valid upper bound `r` to be nonnegative. Consequently
`exp(-w)>=1-5r/(2n)` and `nD<=15000r/997` have the stated directions.

As an adversarial analytic check, let `V` have density `2v` on `[0,1]`
and let `X=sqrt(18)(V-2/3)`. Direct integration gives
`E V=2/3`, `Var(V)=1/18`, and third central moment `-1/135`.
The standardized law has interval support, `J=0`, and
`gamma=-2 sqrt(2)/5`. Thus the coefficient above is negative. This
refutes the tempting gate-free variant, not the candidate: this law has
not been shown to satisfy contact or the required small raw remainder.

The phase-resource corollary, line 332, additionally needs the **weighted**
bound `nD<=N d_D`, a pointwise raw quadratic envelope, `r<2N/5`, and
`0.4095 rho-d_D/15>0`. Its use of `D<=d_D` is legitimate because an
actual witness forces `d_D>=0` and `n>=N`. Combining the density floor
with `1-exp(-w)>=w exp(-w)` yields exactly

\[
 q_{\rm extra}=\frac{1-5r/(2N)}2
                   (0.4095\rho-d_D/15).
\]

Subtracting this cost adds it to the curvature. The score charge remains
on the left. The candidate explicitly prevents charging it twice, and
does not declare the necessary Fourier bounds to have passed.

## Equality, least-index logic, and narrative scope

The new zero-defect corollary at `05-geometry-counts.tex:131` is correct.
If zero lies in the support then `D>0`. Otherwise `D=0` forces both
nonnegative outer moment residuals to vanish, so each sign class consists
of its inner endpoint. Centering and unit variance give `pB=qA` and
`AB=1`. The remaining square gives
`p/q=A/B=(sqrt(10)-1)/3`, hence `p=(4-sqrt(10))/2`.
Conversely that oriented law makes every term vanish. Reflection is
excluded: its defect equals twice the positive third moment of the
displayed extremizer. The statement properly fixes the orientation.

The guide reproduces the exact smoothing recurrence. Its first additive
term is asymptotic to `1/(15n)` and the second to `2/(25n^(3/2))`;
the asserted combined order `1/n` is correct. The estimate
`n(C_n-C_E)<3003/10250` uses only a sharp predecessor, `n>=42`, and
the displayed rational Gaussian bounds. A weak base through 41 covers
both deleted indices at the first possible index 42. Choosing the first
`C_n>=C_E`, rather than the first strict failure, correctly preserves the
strong conclusion `C_n<C_E` after an equality-inclusive exclusion.

The guide's description of `J` as the expected gap length under the
zero-bias density is correct: integrate the gap length on each gap, and
put it equal to zero on the support. The conditional-count identity does
not by itself prove a bound relative to arbitrarily small noise; the
guide now says explicitly that those estimates are separate steps.

The diagram's dashed boxes identify the base, valid Fourier/moment
inputs, and complete local cover. Its solid arrows should be understood
as the **schematic order of the proposed conditional route**, not as a
certificate-level DAG or a record that every displayed input is proved.
The caption and reference to the status section provide that distinction.
The abstract and final scope paragraph do not claim the full conjecture.

## Nonblocking integration observations sent to the editor

1. In the guide's count-mixture display, specify that `W_j` is a sum of
   **count-scale `U` noises**. The earlier `W` denotes physical noise,
   so “conditional noises” alone leaves the units implicit.
2. The Shiganov historical account is on p. 2 of `Tyurin2009`; the
   current introduction cites `Tyurin2010` in that sentence. Use the
   former for that corroboration, while retaining the latter for the
   published 0.4785 theorem.
3. The inspected root `main.tex` bibliography line has not yet included
   `references-added`, although the introduction uses its new keys.
4. In the candidate's support paragraph, `Q_H` is a *piecewise cubic
   function*, not a polynomial on all of `R`. Its growth argument is
   unaffected. The guide already uses the more precise description.

## Reviewed file fingerprints

These identify the files read, not mathematical correctness. Later editorial
changes require checking the diff before transferring this review to a new
snapshot. No source or certificate modification accompanied this review.

| Tree and relative path under `manuscript/arxiv-v1` | SHA-256 |
|---|---|
| `manuscript-v2/main.tex` | `6dcf35df9174eafb57d716c0486a581f44357d75aca5d8613ee28d6e81b1dd4b` |
| `manuscript-v2/sections/01-introduction.tex` | `0eab2b2dc5727d67943a33b5b9ed705e4561bdcf4413541df0d8aa3894029265` |
| `manuscript-v2/sections/01b-guide.tex` | `1fe307126da6c1cdd5b67451a712905f138f3a26169f84f5056cb2420b538c72` |
| `manuscript-v2/sections/05-geometry-counts.tex` | `5c1d875c59eb695b26119d8792bf09533f46176426367bd159f7c2df5d9dd5cc` |
| `manuscript-v2/sections/03-smoothing.tex` | `055af795fbb68a351c6eb66f470bf03479be478888f9a1b7105e26b5600af7ad` |
| `manuscript-v2-conserved/sections/05b-conserved.tex` | `1b2630ac26717284a989cd7ec81bc30f453278af497d4fa6ed8399357fd3a777` |
