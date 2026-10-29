# Independent review of the four-phase extension through lambda = .075

No mathematical blocker was found in the stated local theorem. The proof
covers `u in [-.272,-.15] union [0,.728]`, every `0<lambda<=.075`, every
integer `n>=42`, `p in [.4,.53]`, amplitude `.6`, inward sum at most `.072`,
raw `|H|<=1.84`, and `C>=.4`. It does not cover `-.15<u<0`, acquire the
conditional representation, or prove a complete Berry–Esseen theorem.

This independent review starts at
`a69dda8e8ca78c01ed5fe2a7bdf1a4dd1149dfe1` on
`research/outer-review-v12-20261028`. It adds review/evidence files only.

| Item | Mathematical status | Execution status |
|---|---|---|
| Exact conditioning identity, including collisions | Independently rederived | Source read; no unverified event relaxation used |
| Uniform finite-n normalizations and count ratios | Independently rederived using explicit finite Stirling remainder | All independent rational gates PASS; 893 actual binomial ratio controls |
| Favorable cubic gain `C(rho-rhoB)>lambda/n` | Independently rederived on the extended noise range | Positive exact margin `21198861/1750000000` |
| Complete incoming factorial tail | Valid local consequence of external quadratic-Poisson comparison | Denominators and geometric ratios checked; false index-1 version rejected in separate compound review |
| Negative outer and two positive outer intervals | Derived by monotonicity/concavity and five endpoint tests | Five independent exact margins strictly exceed `.0017` |
| Positive inner interval | Polynomial inequality over one closed square | All 144 Bernstein coefficients independently reconstructed by interpolation:142 positive and two origin zeros |
| Missing negative-inner interval | Outside this review | No claim made |

Final source bindings:

- `outer.tex`: `72ff7ae27bdbecfa0a535dd62e52417de9bab370b7004af8b86e9e99f491facc`.
- `outer-check.py`: `2ab32c0bd1c07e4b6ac64ed7dceb8fd1ed999c0309fb580f28c3a4b79f8dcafb`.

The independent checker imports or executes neither source. It evaluates the
original rational inequalities, reconstructs their coefficients by a different
method, and compares the resulting array with the saved constructor artifact.
The artifact is treated as data, not as a certificate of its own correctness.
Final evidence is `runs/outer-review-v12-20261028/check01/`.

## Analytic rederivation

Write `xi=H sqrt(v+s)`, `delta=k-np=xi-u`, `v=pq`, and
`m=sqrt(n)*pi_k`. The own count loses exactly
`pi_k P(W_k>u)` from the Bernoulli CDF at `k`; counts above `k` add
closed incoming probabilities, while all other outgoing terms are
nonpositive. Subtract the actual normal increment at fixed `delta`, then
subtract `C(rho-rhoB)`. This gives the displayed master inequality in the
source, with the same marginal conditional laws at every count. An atom at
`W_k=u` belongs to the incoming CDF and not to the strict own loss.

The exact scalar gate gives `sqrt(v+s)<.502`, so
`|xi|<Xi=1.84*.502` and `|delta|<Xi+|u|`. The global choice
`D=1.652` leaves margin `1/3125`; the own count is interior and
`k/n` lies in `(.36,.575)`. Both `p` and the entire interpolation segment
between `p` and `k/n` lie in this interval.

For `z=k/n`, the binary relative entropy satisfies

`n D(z||p)=delta^2/(2nv)+error`, with `|error|<|delta|^3/n^2`,

because the third derivative has absolute value less than 6 on that
segment. Half the logarithmic prefactor changes by at most
`5|delta|/(8n)`. The factorial remainder has absolute value below
`3/(8n)`: separately bound its positive side by `1/(12n)` and its
negative side by `1/[12n z(1-z)]`, using `z(1-z)>.23`.
This proves the source's finite remainder

`n|e|<Z(D)=5D/8+3/8+D^3/42`.

In particular, `m=phi(0)/sqrt(v) exp(-delta^2/(2nv)+e)` gives the
mass bounds through `exp(-x)>=1-x`; no fixed-law asymptotic limit is used.
The elementary constants `.39886<phi(0)<.4` are adequate. The independent
checker also verifies the lower one using the classical rational upper bound
`pi<355/113` (the existing Machin/Taylor proof supplies a still sharper bound).

For the normal increment, keep the actual `delta` fixed when integrating:

`log f'(t)=-.5 log(1+s/v)+delta^2/(2nv)-(delta+t)^2/[2n(v+s)]-e`.

The variance-only part, multiplied by `n`, has absolute value at most
`lambda[1/(2v)+D^2/(2nv^2)]<(8/3)lambda`. The absolute threshold
part is at most `(2Db+b^2)/(2v_*)`. For positive phases use the sharper
one-sided bound: with `delta=xi-u` and `0<=t<=u`, the convex quadratic
`2delta*t+t^2` is at most `max(0,2Xi*u-u^2)`. This is increasing on the
entire positive interval because `.728<Xi`. The derivation fixes the actual
phase `u`; it does not replace `delta` while differentiating. It gives all
four slope bounds in the table.

The binomial step ratio is exactly

`pi_(k+j)/pi_(k+j-1)=1+(p-delta-j)/(nv+q(delta+j))`.

For the first three phase intervals, factors after the first are at most
one. In the far interval only the first two can exceed one. The first
denominator is at least `42v_*-.6(D-1)`, and the second is at least
`42v_*`, because `delta+2>0`. These prove the source's constants
`1.06,1.08,1.07,1.143`. The actual binomial controls exercise endpoints in
`p`, nearby counts, and `n=42,43,100`; the algebra, not those finite controls,
extends the result to all `n>=42`.

The cubic expansion uses fixed signs, valid since `.072<p,q`. It yields

`(v+s)^(3/2)(rho-rhoB)>=s(.348-13s/16)`.

Indeed the linear contribution is at least `3min(p,q)-.072`, and
`(1+s/v)^(3/2)<=1+3s/(2v)+3s^2/(8v^2)` bounds the normalizer.
Multiplication by `.4` and the `.502` variance cap gives a strict gain above
`s=lambda/n` throughout the extended range. The normal-variance term is
at most `(7/4)delta_+s`, by differentiation in its variance. The repair
is therefore strictly below `(7D/4-1)lambda/n`. The `1/n` is preserved;
this is not a gain of order `lambda`.

## Incoming tail and outer endpoint reductions

For each legal count, `Var W_j<=n max(v0,v1)<=2.5lambda`. Thus the
Poisson comparison can use one common variance for every remaining count.
With `mu=2.5lambda/A^2`, the integer hinge at `i>=2` gives

`P(W_(k+i)<=u-i)<=mu^(i+1)/[(i+1)!(i(1/A-1)-u/A+mu)^2]`.

The factorial inequality `(l-i)_+^2<=binom(l,i+1)` is valid for `i>=2`.
The denominators increase in `i`, and the ratio of successive majorants is
at most `mu/(i+2)`. The resulting geometric majorant includes all omitted
legal counts. The comparison theorem permits a variance upper bound,
so replacing variances by their noise-endpoint values does not require a
separate monotonicity assertion about a Poisson quotient.

The first incoming hinge is used only where `(1-u)/A-1+mu>0`.
Its numerator bound follows from the exact identity
`E(P_mu-1)_+^2=mu^2-mu+1-exp(-mu)` and the cubic Taylor lower bound for
`exp(-mu)`. On the far positive interval this first hinge need not be
admissible, and the proof correctly uses Cantelli instead. Its second
incoming count uses hinge index 2, whose denominator is strictly positive
through `u=.728`.

For the negative interval, replace the own variance by
`T=(15/14)*.075` and study `r^2/(T+r^2)-1.08r` on `[.15,.272]`.
Its derivative is positive at `.15`. Its derivative first increases and
then decreases, since its next derivative has the sign of `T-3r^2`.
It has no interior local minimum after the left endpoint. Endpoint minima
therefore suffice. The incoming bound decreases with `r`, so its upper
bound is taken at `.15`.

For the two outer positive intervals, the subtracted reciprocal-square
terms are convex in `u`. The far first Cantelli term is also convex there,
because `3(1-.728)^2>(7/6)*.075`. Thus the two margins are concave and
can be checked at their endpoints. Every endpoint inequality also makes
`O-RT` positive before the lower bound for `m` is substituted.

The smallest of the five exact outer margins is

`130415386177086480523/74821464040487875200000 > .0017`,

at the far positive interval's left endpoint `.15`. Removing the cubic unit
gain makes that same sufficient inequality fail. Inflating the repair and
desired margin to their values at `.075` is conservative for every smaller
positive noise.

## Independent positive-inner polynomial verification

Expansion of the strict quartic minorant at `W_k-u` gives

`L(t,u)=[(3alpha^2-A^2)t-3t^2-4Aut-6u^2t-u^4+3alpha^2u^2-2alpha^3u]/(5alpha^4)+.96u`,

where `alpha=.64`. In particular the cubic contribution is `-4Aut` in
this positive-phase lower bound. The expression is concave in the actual
own variance `t`, whose entire interval is
`[(79/84)lambda,(89/84)lambda]`. No conditional allocation shortcut is used.

At each endpoint the original inequality is multiplied by
`6d1^2*d2^2*d3`, with the three positive affine denominators specified in
`outer.tex`. This is a polynomial of degree at most 7 in `lambda` and 8
in `u`: the own term has respective degrees 2 and 4, while the common
denominator has respective degrees 5 and 4. The tail numerators fit within
those same bounds.

The independent implementation evaluates this original rational expression
on an `8 by 9` rational interpolation grid in `[0,.075]^2`. It solves the
two exact Bernstein evaluation systems by rational Gaussian elimination.
Distinct nodes make those systems invertible; the audited degree bound
makes the reconstruction an identity on the whole rectangle, not sampled
positivity. Four additional rational off-grid identities per polynomial
are arithmetic controls. This differs from the constructor's power-basis
expansion and monomial-to-Bernstein transform.

All 144 coefficients match the supplied array exactly. In each polynomial
only the `(0,0)` coefficient vanishes; the remaining 71 are strictly positive.
Bernstein basis functions are nonnegative and sum to one, so the inequality
is strict off the origin. In particular it is strict at every `lambda>0`,
including `u=0` and all closed edges. There is no hidden lower bound on
positive noise. The shared positive endpoints `.075` and `.15` are covered
by both adjacent arguments; the interval `(-.15,0)` is explicitly omitted.

## Reproduce and retain scope

```sh
python3 -I -B mathematics/simplification-v12/2026-10-28/outer-review-check.py CONSTRUCTOR_REPO_ROOT
```

This binds the reviewed source bytes. To save a new run, use
`outer-review-run.py NEW_ID CONSTRUCTOR_REPO_ROOT`. The final check uses
exact rational arithmetic only. The inherited Pinelis theorem and finite
Stirling inequality are retained mathematical inputs, not newly formally
verified results. This review concerns the printed component and the scalar
arithmetic; no manuscript or original certificate is removed.
