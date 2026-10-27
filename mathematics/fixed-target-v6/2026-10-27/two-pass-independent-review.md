# Independent review of the shorter two-pass entry

**Recommendation:** use this quadratic route for the conditional initial-gap
statement; retain the degree-six phase route as an optional stronger result.
No blocking issue was found. The two-pass construction closes the actual-gap
gate on all 24 initial rho cells without invoking the higher-degree phase
lemma, a prior central gap, or a `D<2` hypothesis.

Reviewed constructor commit:
`c22eece58612f708ceb765b00af2412970130370`. I did not author C's two-pass
construction. I did author the v5 first-cover and v6 circle components and
previously reviewed the signed coefficients; this report independently checks
the new two-pass composition, not those components' authorship independence.
The original support/contact and complete Fourier inputs remain premises.

| Item | Mathematical status | Execution status |
|---|---|---|
| Simple phase price and legal raw/resource minima | Independently checked from the conserved identity | Exact order and gate reconstruction on all 48 passes |
| Two quadratic passes, same-law coefficient updates and full coverage | Independently checked composition, conditional on retained analytic inputs | Fresh independent rational verification of 96 endpoint quadratics |
| Final defect and actual-gap gates | Verified conditional conclusion | `D<=3.5746638454`; all 24 strict gap margins positive |
| Later small-defect/probability/noise/local comparison and global theorem | Separate obligations | Not accepted or run |

## Exact verified result

| Pass | max raw T | max resource U | max D | Actual-gap cells |
|---|---:|---:|---:|---:|
| 1 | 13.2818901598 | 10.9330610254 | 3.9164138937 | 23 |
| 2 | 11.5164967977 | 9.9790315907 | 3.5746638454 | 24 |

After pass 2, `nD<=150.1358815051`. For each cell `[l,u]`, the verified
strict margin is

\[
 (\sigma_l-1)l-d\ge526024602543/1600000000000
 =0.328765376589375>0,
 \qquad\sigma_l=3.162277660<\sqrt{10}.
\]

Pass 1's minimum margin is negative,
`-20775474737/1600000000000`; it is correctly not presented as an all-cell
gap acquisition. The reviewer check recomputes these conclusions from rows,
not from the producer's summary counts.

## Why the simple phase argument suffices

The source proof `signed-two-pass-proof/signed-two-pass.tex:42–65` uses the
actual conserved identity at fixed `c=CE`, with nonnegative excess `a`, loss
`L` and conserved defect `D`. A valid raw bound `R_c<=T<N*c_-*l` implies

\[
 e(c\rho-\phi_0D/6)
 =(1+H^2/n)a+c\rho+\sqrt nL-R_c/n
 \ge c\rho-T/n>0.
\]

Multiplying `exp(w)-1>=w`, with `w=H^2/(2n)`, by this positive product gives

\[
 n(1-e)(c\rho-\phi_0D/6)
 \ge\tfrac12H^2(c\rho-T/n)
 \ge\eta H^2,
 \qquad\eta=(c_-l-T/N)/2>0.
\]

Hence the unweighted conserved resource S satisfies
`S<=R_c-eta*H^2<=R_c<=T`. This justifies the minimum with the raw bound in
the resource update. It does **not** justify replacing a raw bound by a resource
bound when forming a density floor; the code never does that.

Here any already valid raw upper bound may be used in eta, including a minimum
of separately proved bounds. This is valid because `S<=R_c-eta*H^2` concerns
the actual remainder, after which any valid quadratic upper envelope can be
inserted. In contrast, the optional exponential Taylor argument needs the
chosen polynomial itself to lie below `N*b` before reversing its exponential
multiplier. That stronger polynomial-specific condition is not silently
imported or dropped in this quadratic route; the argument is different and
requires only the actual raw license displayed above.

## Correct order, domains and endpoint reduction

The code at `signed-two-pass-check.py:57–102` uses no central-gap quantities in
either pass. Pass 1 uses the gap-free signed K1 cap, quarter constant and
`q(c)=c*l-g/5`. Pass 2 uses only pass 1's certified raw and defect ceilings
for its density and circle constraint. The conserved defect is the actual
`(3+sqrt(10))*rho-gamma-3J`; the compulsory lower bound involving m remains
an inequality. The sign of gamma is retained in the minimum of its two density
endpoint products.

All moment inputs are fixed before maximizing over formal coefficients c.
The two alternatives in q have identical slope l, so q is affine in c.
The simple phase price eta is held constant across the two c endpoints.
The raw and resource quadratic expressions are therefore affine in c before
maximization over `|H|`. Their two c endpoints and exact square completion
cover the entire CE enclosure and all real raw thresholds. Positive curvature
and nonnegative linear coefficient are checked at each endpoint.

The final proof explicitly rounds the circle-derived gamma bound downward
(`signed-two-pass.tex:75–100`) and rounds upper ceilings upward to `10^-10`.
Every pass checks the raw license before obtaining its phase price and resource.
Only that resource yields new defect and weighted `nD` bounds. No new defect
is used to prove itself, and no cell is excluded because its relaxation is
inconsistent. All 24 closed cells and both shared endpoints are retained.

The actual-gap inference at `signed-two-pass.tex:138–151` has the correct
scope. If zero were in the closed support, there would be no central crossing
gap and the gap integral bound gives `J<=rho`. Since `gamma<=rho`, this forces
`D>=(sqrt(10)-1)*rho`, contradicting the cell's strict margin. Both signs of
support exist for a centered nondegenerate law; the closed support then has
nearest endpoints of a genuine central gap. No two-point-law conclusion is
being inferred.

## Independent arithmetic and source binding

I read the complete final constructor code and proof. My separate
`two_pass_review_check.py` imports no constructor, Fourier, circle, signed or
phase module. It reads pinned coefficient data as conditional inputs and
independently reconstructs every coefficient, circle conversion, density,
curvature, rounding step and retained minimum in all 48 passes.
For every quadratic it verifies the coefficient identity

\[
 (B+f^2/(4q))-(B+fh-qh^2)=q(h-f/(2q))^2,
\]

and repeats it with curvature `q+eta`. Thus the recorded maxima are checked
over the full continuous threshold domain, not by sampling. The already
reviewed signed coefficient table supplies K; its source is pinned separately.
No Fourier integral is reevaluated in this independent review.

Six mutations are rejected: missing cell, reversed pass order, raw replaced
by resource, understated resource, false first-pass gap claim, and altered
signed curvature. The fixed run uses Python 3.9.6 without optimization.
Command actually run from this separate worktree:

```sh
python3 mathematics/fixed-target-v6/2026-10-27/two_pass_review_check.py ../signed-response-v6
```

The successful receipt, exact stdout and empty stderr are under
`runs/fixed-target-v6-20261027/two-pass-review02/`. An earlier attempt rejected
the proof hash while C was making its final rounding/table clarification;
that failed attempt and checker snapshot remain in `two-pass-review01`.
I reread the final proof before updating its pin. Its formulas and numerical
output did not change during that final clarification.

Final pins:

- Constructor: `a2b9309998191c2d7e4477a969cd55ecb516440f56dfa3cf97df5ccddac1e76d`.
- Proof: `ce1ef706ccf4c134d194a1b13bee96ded0d296a629715e8d68cb8ef7a6fab074`.
- `signed-two-pass02/stdout.json`: `c52122bea63beaed83de741a347863a39fb0faeaa34dec5dc4b2741a0a88594a`.

## Exact proof-shortening consequence

For this initial-gap conclusion, the degree-six phase theorem, its index
endpoint argument, global concavity gate and polynomial stationary-point
certificates are unnecessary: the two explicit quadratic passes establish
the stated target with a larger positive gap margin. This is a dependency
removal in the **new conditional initial-gap proof**, not authorization to
delete existing certificates or the optional stronger result.

An additional exact output check shows no strict raw or resource minimum is
active in any of the 48 recorded passes: each retained result equals the
upward-rounded fresh quadratic ceiling. Therefore, for these fixed inputs,
the earlier raw ceiling values need not be a logical premise if the new
quadratic maxima are directly checked against their licenses. Their complete
Fourier/moment coefficients and analytic justification remain necessary. No
existing runner was edited on that basis.

This result acquires an actual gap and a weighted defect bound. Fourteen cells
still lack `D<2`, and the much smaller defect, noise and complete probability
panel hypotheses needed by later local comparisons are not supplied here.
The shorter entry proof alone therefore makes no existing local certificate
family dispensable.
