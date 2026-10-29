# Independent composition review of the negative-inner comparison

The full local implication in `compound-proof.tex` passes this independent
analytic and arithmetic review. It proves **`Delta_C<0`** for
`lambda in [.03,.075]`, phase `u=-r in [-.15,0]`, every integer `n>=42`,
`p in [.4,.53]`, the stated centered conditional laws with amplitude `.6`
and inward sum at most `.072`, raw `|H|<=1.84`, and `C>=.4`.
It does not assert `Delta_C<-lambda/100`. Acquisition of its conditional
support and threshold premises remains a separate obligation.

This review starts at `a69dda8e8ca78c01ed5fe2a7bdf1a4dd1149dfe1` on
`research/compound-composition-review-v12-20261028`. No constructor source,
manuscript, old certificate or remote branch is changed.

| Result | Mathematical status | Execution status |
|---|---|---|
| Count identity and same-law cubic/fourth-moment join | Independently rederived with exact conditional counts | Full proof and acceptance source read |
| Uniform normal normalization and exponential chord in `eta=1/n` | Independently rederived; no fixed-law limit | 21 independent rational preflight gates PASS |
| Groupwise Poisson comparison and variance/allocation monotonicity | Derived component using the stated external Pinelis theorem | Prior independent comparator proof and exact controls retained |
| Complete first and later incoming bounds | Reconstructed with an independent pgf evaluator and rational exponential series | All 291 cell contexts and admissibility conditions PASS |
| Quartic margins and all-sample-size reduction | Separate concavity and support-price arguments audited | All 200 cells independently reconstructed; 7,592 deduplicated variance/mass corners |
| Cantelli margins | Variance bound, derivative license, mass sign and repair audited | All 91 cells independently reconstructed |
| Entire certificate arithmetic | Independent implementation, no constructor import or execution | 291 positive margins; minimum `256695813/10^12` |
| Full domain coverage and malformed-object behavior | Separately reviewed by the geometry agent using disjointness/volume, not constructor refinement | See `compound-cover-review.md`; not inferred from this margin replay |
| Full sharp Berry–Esseen theorem | Not established by this component | Not claimed |

The final independent run is
`runs/compound-composition-review-v12-20261028/check02/`. It took about
13 seconds on the recorded interpreter and retained stdout, stderr, source
hashes, return code and command. The positive minimum agrees with the
constructor after rounding down to `10^-12`; **every one of the 291 rounded
cell margins agrees**, although the independent transcendental enclosures
and coefficient construction differ. Agreement is a check, not a premise.

The exact source bindings are:

| File | SHA256 |
|---|---|
| `compound-proof.tex` | `5b9d8428b6aa10bc3fff44114cd26c482b88692f76dd624b841c79d5b4a753fa` |
| `compound-accept.py` | `f98de164169fae176644737b8b68b72044837db2a19dbba26602cea279c3d611` |
| `compound-evaluator.py` | `f23d657e0bc10b1d3334feeb65ccd43dd2d8b415e4a26fb0e6f7c3ddc853e582` |
| `compound-certificate.json` | `e3baf63f96f5f7fd6e7f9c6dae1e75448f9f588524e164fdf8c0b2e770ea6a0c` |

## The analytic join

For an actual marginal, define `w=p*v1/s`, `Lambda0=lambda(1-w)`,
`Lambda1=lambda*w`, `eta=1/n`, and `delta=k-np=xi+r`, where
`xi=H sqrt(v+s)` and `|xi|<Xi=.924`. The exact own-count variances are

`T0=Lambda0*(1-delta*eta/q)` and `T1=Lambda1*(1+delta*eta/p)`.

This is the physical count transport. The false substitution
`T0=(1-w)t,T1=w*t` is never used. A zero conditional variance gives a
zero corresponding term directly, so the argument does not divide by that
variance or exclude a boundary allocation.

The exact CDF identity subtracts all outgoing counts with strict events
`W_(k-i)>-r+i`, and adds all incoming counts with closed events
`W_(k+i)<=-r-i`. Keeping only the own outgoing count is a valid lower
bound on the loss. The normal increment is formed at fixed actual `delta`.
It follows that positivity of the displayed local margin suffices for
`Delta_C<0`, including all atom collisions.

The finite Stirling estimate applies uniformly on the segment between `p`
and `k/n`, contained in `(.36,.575)`. Its entropy, prefactor and factorial
remainders give `n|e|<=Z(D)=5D/8+3/8+D^3/42`. With
`D=Xi+r_+`, this yields the stated cell lower mass `m_-`. The upper mass
bound is obtained at a binomial mode, whose displacement from `np` is at
most one. The source's rational square test proves `m<=.85`. The first
binomial ratio is bounded by the displayed `R`, and all later step ratios
are at most one because `.53+D<2`.

The improved negative normal slope is justified without losing a factor
of `1/n`. At fixed `delta`,

`d/ds log f'(t)=[(delta+t)^2-n(v+s)]/[2n(v+s)^2]<0`

for `-r<=t<=0`, since `|delta+t|<=Xi+r` and `42v_*>(Xi+.15)^2`.
Thus its upper bound is obtained at `s=0`. There,
`-2delta*t-t^2<=2Xi*r+r^2`, giving

`log f'(t)<=eta*P(r)`, where `P(r)=(2Xi*r+r^2)/(2v_*)+Z(Xi+r)`.

Since `P` is increasing on the nonnegative phase interval, use `P(r_+)`.
The exponential is convex in `eta`, and its chord from `0` to `1/42`
gives `exp(eta P)<=1+E eta`, with the outward upper enclosure defining
`E`. Consequently `f(-r)>=-r(1+E eta)`. This is a finite inequality
for the actual law. The endpoint `eta=0` used later is algebraic, not a
fixed-law limit replacing uniformity.

For the cubic penalty, expanding the same conditional third moments gives

`n(v+s)^(3/2)(rho-rhoB)>=3p Lambda0+3q Lambda1+M1-M0-.78lambda-(13/16)lambda^2 eta`,

where `M0=nq E U0^3` and `M1=np E U1^3`. Its entire right side is
positive because it is at least
`lambda[1.2-.072-.78-(13/16)lambda eta]`. Only after establishing
this sign may the coefficient `C/(v+s)^(3/2)` be reduced to `K0=3.16`.
The separate weaker gain above `lambda eta` is also valid and is used in
Cantelli cells. The proof never reduces coefficients in isolated signed
pieces of the cubic expansion.

Apply the quartic minorant to `W_k+r`, retaining the same third moments
in the cubic penalty. The endpoint prices for squared conditional
variables are

`m*g0*(x^2+4rx)/(5alpha^4)+K0 eta*x` on `[-A,d]`,

and

`m*g1*(x^2+4rx)/(5alpha^4)-K0 eta*x` on `[-d,A]`.

Each is convex in `x`, because the own-count factor is positive. Their
endpoint maxima therefore bound the integrated prices. The favorable
`3 sum Var(Z_j)^2` term is dropped; retaining it without further work
would spoil the later concavity reduction. The relaxed inward endpoints
`d,d` are bounds on the two conditional supports, not an assumption that
the original inward sum equals `2d`.

This yields the source's quartic local margin with the original two
transport factors. Bounds `3p>=1.2`, `3q>=1.41` and `v>=.24` remove
the remaining `p` dependence in a conservative direction; there is no
unreported grid over `p` or over a law.

## First incoming count and the full tail

For every incoming count, `delta+i=xi+r+i>0`, since `Xi<1`.
The negative conditional group therefore shrinks: its variance is at most
`Lambda0`. The positive group variance is at most
`Lambda1*[1+2.5(Xi+r+i)eta]`. For the first incoming count, the inflated
comparator has small-jump fraction at least `w` and total variance at most
`L*[1+(5/84)(Xi+r_++1)w_+]`.

The independently proved centered-hinge monotonicity now has the correct
direction: use this total-variance upper endpoint and `w_-`, then use
`1+r_-` in the tail threshold. The hinge is fixed across the cell and
strictly below that threshold. The theorem permits variance inflation
before the hinge is applied. No convexity in allocation is assumed; that
shortcut was independently refuted in `compound-review.tex`.

The independent evaluator sets `A=25h`, `d=3h`, `h=3/125`. It computes
the lower-complement coefficients from

`c0=1`, `j*c_j=25mu*c_(j-25)+3nu*c_(j-3)`.

It then subtracts the entire finite lower complement from the exact full
second moment of `25Pois(mu)+3Pois(nu)`. A lower enclosure of
`exp(-mu-nu)` supplies an upper hinge bound. In contrast with the
constructor's double sum and scaling/squaring, this replay uses the pgf
recurrence and a direct positive Taylor series with a geometric remainder.
All endpoints remain rational. Zero intensities and rational hinge anchors
are included; no upper Poisson tail is truncated.

For incoming counts 2 and 3, both the global variance bound `2.5L` and
the local count-inflation bound are valid, so their minimum is valid.
The certificate's integer hinge need not equal the incoming count index,
but it must be at least 2 and strictly admissible. Every such denominator
is checked before division. The factorial inequality
`(P-j)_+^2<=binom(P,j+1)` then gives the displayed bound. For all
remaining counts, use variance `2.5L` and hinge index `i`; the numerator
ratios are at most `mu/6` from index 4. The geometric continuation
includes the full infinite numerical majorant. Adding its terms beyond
legal counts only enlarges the bound.

## Why the finite endpoints cover every sample size and law

At fixed `r`, the true `g0,g1` lie inside the independent rectangle
`[1-2.5(Xi+r)eta,1+2.5(Xi+r)eta]`. It remains positive over the
entire domain. The margin is separately concave in these two factors,
so the four rectangle corners suffice. Their failure to correspond to a
common marginal is harmless: the corners test a larger relaxation.

After that substitution, the expression is separately concave in each of
`lambda,w,eta`. In any single variable, `t=T0+T1` is affine and its
square enters with a negative coefficient. The other nonaffine contribution
is `-(13/16)K0 lambda^2 eta^2`, also concave in each variable separately.
All remaining contributions are affine in the variable being reduced.
The expression is affine in `m`; both mass endpoints must be checked
without making a sign assumption. Repeated one-variable endpoint
reductions therefore justify the source's complete corner list. This
argument does not assert joint concavity.

Each corner leaves a quartic in `r`. The independent implementation obtains
the degree-four Bernstein functionals by inverting the exact five-point
Bernstein evaluation matrix, then applying those functionals to the original
moment expression. It does not use the constructor's coefficient-expansion
code or its monomial transform.

For each coefficient, the two support prices are independently maximized
over their respective two endpoints. This computes exactly the minimum of
that coefficient over the four support choices. It does **not** assume
that a minimum of incoming bounds is convex. Duplicate variance corners
at `eta=0` or a zero group are omitted. The replay checks 7,592 remaining
variance/mass corners, five coefficients per corner, for all 200 quartic
cells. Every coefficient is positive.

For each of the 91 Cantelli cells, the replay checks the strict left
endpoint derivative license. The derivative of
`r^2/(T+r^2)-h_f*r` first increases then decreases, so a positive
left derivative permits only an interior maximum. The minimum is at an
endpoint. If the resulting bracket is negative the upper mass is used;
otherwise the lower mass is used. The positive repair coefficient is
inflated to `L/42` only after applying the cubic unit gain. All these
margins are positive.

The exact coverage argument and malformed-certificate tests are supplied
by the separate independent `compound-cover-review.md`. This replay
independently checks the pinned domain, canonical rational boxes, sorting,
method counts and total volume; total volume alone is not used to infer
coverage. All margin estimates hold on closed boxes. Thus, with the
separate disjointness/coverage proof, no faces, allocation boundaries,
phase endpoints or sample sizes are omitted.

## Outcome and reproduction

No blocker remains within the printed local scope. The separately recorded
coverage review is complete at commit
`460790c8d84fd7c9b4543ffe867886ba244818e1`, with the same four source pins.
I read its coverage derivation and recorded checks: the 291 closed boxes
have pairwise disjoint interiors and exact total volume `27/4000`. Their
finite union is closed, so any missing target point would leave a relative
open neighborhood of positive volume, contradicting volume equality. This
accounts for exterior faces as well as interiors. The previous `.03` theorem covers smaller positive
noise on the same right-panel strip. The independently reviewed outer-phase
theorem covers the remaining phases through `.075`. Their common boundaries
are included, so their combination supplies a full-phase strict comparison
in that conditional right-panel domain. The conclusion remains local to the
acquired strip and noise cap; it does not remove dependencies used outside it.

Reproduce the independent arithmetic from the integrated checkout:

```sh
python3 -I -B mathematics/simplification-v12/2026-10-28/compound-composition-review-check.py CONSTRUCTOR_REPO_ROOT
```

For a new saved receipt use `compound-composition-review-run.py NEW_ID
CONSTRUCTOR_REPO_ROOT`. Existing run directories are refused. Source hashes
must match the reviewed bytes before any certificate is consumed. The
published Pinelis theorem, finite Stirling inequality, and the analytic
reduction are not certified merely by an arithmetic PASS.
