# Independent review of fixed-target scalar-schedule transport

**Recommendation: accept the narrowed conditional transport theorem for
integration, without accepting a complete LOCAL42 theorem or any numerical
schedule.** The new multiplier can be fixed at c=C_E in the inspected raw
scalar bounds. Its actual score must remain `C_act=c+a/rho`. No blocking
algebraic error was found in this transfer after the explicit qualifications
listed below were added.

This is an independent review of the excess construction, not a self-review
of my Opus audit or earlier finite-appendix exposition. I read the full draft
`strategy-v4-excess/mathematics/strategy-v4/2026-10-27/excess.tex` and rederived
the transfer substitutions, then checked the source inequalities listed here.
I did not accept the conclusion merely from the constructor's checks.
The constructor subsequently committed this reviewed source as `f082ef7`.
The exact reviewed draft SHA-256 is
`a7105d57f4f353a7fcdd32947b1feae044b3df5dc29558afb48c575e9ea4a2d0`.
Source hashes and separate bounded execution evidence are preserved in
`runs/strategy-v4-20261027/transport-review01/`.

| Item | Mathematical status | Execution status |
|---|---|---|
| New contact coefficient and conserved excess | Independently read/rederived at the displayed hypotheses; no ratio-maximizer substitution | No native proof program run |
| Formal-multiplier specialization of inspected raw boxes | Valid conditional implication | No complete scalar schedule or certificate replay |
| New count identity | Independently derived identity | Fresh formal polynomial comparison, exit 0 |
| Strictness, negative gains, old-left-side substitution | Necessary distinctions retained; false substitutions rejected | Fresh bounded controls, exit 0 |
| All rows, all index gates, every Fourier envelope and complete coverage | Remain separate inputs | Not freshly accepted by this review |
| Removing the entry recurrence from a new complete route | Conditional on a fully established transported exclusion | No current production dependency removed |

## 1. Qualifications found during review and now explicit

The reviewed transport theorem is now at `excess.tex:391–423` and explicitly
sets c=C_E, N>=3. The c=C_E specialization is necessary for the displayed
nonnegative physical-defect resource and Corollary `v4excess:cor:weight`;
the earlier attainment/contact results allow arbitrary c>0 but do not make
that particular resource formula valid at arbitrary c. I raised this
specialization independently; the coordinator also requested N>=3 so both
deleted indices are positive.

The positive-noise leaves now explicitly require a separately established
C_B<=c (`excess.tex:417–418`). This is needed in the last contradiction,
in addition to the separately strict zero-noise binomial bound. A merely
nonpositive comparison cannot exclude the equality boundary a=0,C_B=c.

## 2. Three quantities that must not be identified

At an excess maximizer,

\[
 a=\sqrt n(F-\Phi(H/\sqrt n))-c\rho,\qquad
 C_{\rm act}=c+a/\rho.
\]

The contact coefficient is c; the deleted-convolution bounds concern the
separate global constants C_(n-1),C_(n-2). Repeating raw contamination while
holding the raw event fixed yields the derivative with coefficient c in
`excess.tex:115–126`, not C_act. Its support equation gains `-na` after a
predecessor bound C_(n-1)<=c. For a>=0 this extra term can be discarded in
the favorable direction.

The moment caps from a universal bound on an individual law's score can use
C_act>=c. Caps whose only justification is ratio-optimality cannot be imported
on that basis. The transport theorem correctly assumes a new ordered
acquisition of all subsequent moment and support bounds for this same law.
No claim here transfers a statement merely because its old label contains
“extremal” or its coefficients occur in a stored table.

## 3. Raw box bounds really permit a formal multiplier

The relevant first-stage statements are the raw remainder definition and
first inequality of `manuscript/arxiv-v1/appendices/fourier-analysis.tex:2370–2440`
(`entry-remainder`, `entry-cell-theorem`, `entry-four-corners`). Their raw
remainder has the form

\[
 R_t=t A_0+H(tK_1+\varphi U)-H^2(t\rho+\gamma\varphi/2)+E_n.
\]

Here A_0,K_1,U,gamma,rho and E_n refer to the same actual law. The Fourier
remainder E_n is independent of t. The coefficient estimates use actual-law
moment, gap, support and Fourier bounds, positivity of t, and the supplied
parameter rectangle. For fixed H,rho the scalar upper envelope is convex
in t; at fixed endpoint t>0 it is convex in rho. These arguments use no
identity `t=C_act`. Thus, if the primitive estimates and their domains
are established, the same corner maximum bounds R_c when c belongs to the
formal multiplier interval. Endpoint coordinates need not represent actual
laws; they bound the outer parameter rectangle.

The coarse unsigned formula at Fourier lines 2545–2586 likewise requires
`q_*>0`, `k>=0`, `A_*>0` before using the upper multiplier. Those gates
remain requirements. A law-dependent old score cap can be used as a formal
endpoint only after verifying that the resulting endpoint interval contains
c on the entire cell. “The old law had a cap” is not that verification.

The feedback conclusion of the old lemma is not obtained by merely renaming
its C. It can, however, be rederived as an optional output: the new identity
and nonnegative resources give `(n+H^2)a<=R_c`. If `R_c/rho<V`, then

\[
 C_{\rm act}<c+\frac{V}{n+H^2}\le c+\frac VN.
\]

This posterior bound is not a prerequisite for the first uncharged raw box.
Confusing an output with an entry condition would reintroduce the recurrence
unnecessarily.

## 4. Initial raw ceiling, phase pricing and charged corners

Before removing Gaussian weights, one must establish an uncharged raw bound
`R_c<=r_0<2N/5`. This is explicit in `excess.tex:343–378` and corresponds to
`sections/05b-conserved.tex:290–336`; Fourier line 2586 also keeps this
licensing requirement. The argument is not allowed to use a density floor,
a phase improvement, or a final charged budget that itself depends on weight
removal to establish that first bound.

From the new identity,

\[
 (n+H^2)a+nc\rho(1-e^{-w})+
 n\phi(0)e^{-w}D/6+n^{3/2}L=R_c,
\]

all displayed terms are nonnegative at c=C_E,a>=0,D>=0. The initial ceiling
makes `c rho-phi(0)D/6>0`, which licenses the unweighted defect bound. The
extra phase price uses this same remaining quantity once. With nD<=N d_D,
n>=N gives D<=d_D, and the retained positive coefficient produces the same
lower quadratic phase price. There is no missing negative term from a;
its coefficient is n+H^2, so dropping it only weakens the bound.

For the two-interval construction (`sections/06-resources.tex:15–52`), the
required convex G is a supremum of affine-in-t chord quadratics with positive
Q. Since `C_0<c<chi`,

\[
 G(c)\le\max(G(C_0),G(\chi))\le B_*.
\]

The high-interval charged endpoint may therefore remain in the old maximum
without an actual-score upper bound. The central rounded endpoint treatment
at lines 89–100 still needs its outward enclosures and proof that c belongs
to the formal interval. It is not an acceptance of the exported numeric rows.

The six-corner construction at Fourier lines 2894–2941 bounds a formal
piecewise charged envelope with `chi(t)=n(t-0.40974)_+`. The subtraction
preserves separate convexity on each side of the kink. At t=c<0.40974 its
charge is zero, so that corner maximum bounds R_c itself after the stated
phase improvement. There is no need to infer `C_act<=0.40974`. Conversely,
a positive barrier K rho cannot be subtracted unless proved for the excess
maximizer; a>=0 alone supplies no positive K.

## 5. Confinement preserves separate coefficient and deletion roles

Fourier lines 3103–3149 explicitly separate:

1. the majorant derivative, using a multiplier in `(0.4,0.4253]`;
2. concentration bounds for both actual deleted sums, with global caps;
3. one strict common phase budget.

The derivative of the new Q_c has exactly the same shape with multiplier c.
The first-failure bounds C_(n-1),C_(n-2)<=c<0.4253 provide the two separate
concentration caps. The slope estimates, including the negative quadratic
case on the lower ray (lines 3298–3370), only vary the multiplier over its
interval. They do not use C_act=C_n elsewhere.

This does not remove the floor-42 repairs. `appendices/uniform-bridge.tex:67–93`
requires the scale gate covering both 42/41 and 42/40 and an actual acquired
strip; its initial conditional cubic coefficient is 30, not an unproved 24.
The same-law contraction order and strict-gap widths remain necessary.
The resource uses weighted nD, and its displacement/noise/leak terms cannot
be allocated independently.

The strict envelope is essential at Fourier lines 3136–3149, 3400–3509 and
bridge lines 126–177. If `R-NP<=0`, a strict common budget excludes the cell;
a non-strict budget with zero residual does not. Positivity of `zR+A` is
still required before replacing 1/n by 1/N. At a=0, discarding the excess
creates no strictness. Hence the transport theorem's independently strict
raw/phase envelope premise must remain literal.

## 6. Signed repair and the final count comparison

The repair proof in `appendices/local42-refinements.tex:387–439` uses the
multiplier only through `A=t/(v+s)^(3/2)` and its lower/upper bounds. For a
negative cubic coefficient Q_*, the lower bound for A Q_* uses the **upper**
multiplier. Replacing t by c inside `(0.4,0.4226)` preserves both directions;
a bare lower multiplier does not. The normal variance comparison depends
on the same actual phase and conditional variance, not on ratio attainment.
The nonnegative clamp precedes any inverse-index substitution.

Let Q=F-F_B, let G_H be the actual normal CDF, G_B the binomial normal CDF,
and G_0 the normal CDF at the same count but actual variance. Then
`pi_k f=G_H-G_0`. Directly expanding both sides gives

\[
 a+\rho_B(c-C_B)=\sqrt n\pi_k(Q/\pi_k-f)
          +\sqrt n(G_B-G_0)+c(\rho_B-\rho).
\]

This proves the new identity without treating C_act as c. Retaining the old
left side instead gives a discrepancy: after multiplication by rho, the
old-minus-new left sides differ by `a(rho_B-rho)`, which is generally nonzero.
The bounded formal checker derives this defect as well as the correct identity.

The nearest-count proof at `sections/05c-counts.tex:78–117` needs positive
`D_0=O-R_0T` before replacing the binomial mass by its lower bound. The
whole-count proof needs B(lambda)<0 and the correctly clamped inverse-index
correction. The fuller version at Fourier lines 3544–3608 uses the same legal
counts, closed incoming events and strict outgoing events. These are identities
and right-side inequalities for the actual conditional law. After replacing
the repair multiplier they apply to the new left side, not the old one.

A strictly negative right side contradicts both a>=0 and C_B<=c. At zero
noise, the law is binomial; the penalty is independent of the threshold, so a
maximizing positive event occurs at an atom. A separately strict binomial
comparison then excludes it. Positive-noise strictness, zero-noise strictness
and full boundary coverage are distinct requirements.

## 7. What this review licenses

The fixed-target formulation genuinely changes the entry logic: if every
ordered primitive and numerical leaf is proved on the new domains, the above
conditional exclusion starts with a>=0 and needs no prior upper bound on
C_act or na/rho. Combined with a genuine finite base and least failure, that
new route would dispense with the score-excess entry recurrence.

This review does not prove every low/high-frequency envelope, the complete
zero-barrier schedule, every scalar endpoint enclosure, strict budget margin,
all positive-noise leaves, or a finite base. Existing wrappers requiring a
ratio optimizer or entry caps have not been changed or accepted for the new
problem. No existing certificate should be deleted. A later integration needs
a source-bound ordered transport map showing which universal scalar inputs
and exact predicates discharge each explicit premise.

The only executable in this review was the independently written
`runs/strategy-v4-20261027/transport-review01/check_review.py`, run once with
system Python 3.9.6 and optimization disabled. Its exact polynomial checks
and sign controls exited 0; stdout/stderr, command, source hashes and return
code are retained. These bounded arithmetic results support the displayed
algebra and rejected substitutions; they are not mathematical acceptance of
the full transport dependency graph or a native numerical PASS.
