# Review of the comparison union and witness mapping

No mathematical gap was found in the union or normalization argument.
Two wording changes were requested: distinguish the **inherited full-count
grid** from the new 291-cell certificate, and mark the table's inward bounds
explicitly as upper bounds. Both have been applied. The reviewed final union source is
`31645628932501a0265959123b5d452b09116b77792fc2401c6a18eacdbb754a`.

This review was made in `research/union-review-v12-20261028`, starting from
`a69dda8e8ca78c01ed5fe2a7bdf1a4dd1149dfe1`, with only new review outputs.
**Independence disclosure:** this reviewer constructed the negative-inner
compound component and the earlier right .02/.03 components. This is an
independent review of the coordinator's union, mapping, other-component
hypotheses and dependency claims. It is not a second independent proof of
those self-constructed components. Their mathematical verification is
provided by the separately assigned reviewers.

| Item | Mathematical status | Execution status |
|---|---|---|
| Union of LEFT-01, old right .03, right outer and right negative-inner domains | Independently derived from their exact printed hypotheses | Exact common-refinement checks, including all edges, PASS |
| Conversion from acquired standardized witness to Bernoulli-coordinate noise | Independently derived by conditional means and total variance | 12 actual marginal scaling controls PASS |
| Target constant in both coefficient ranges | Elementary exact bound, independently checked | Rational Machin-series / squared radical bounds PASS |
| Conditional support and raw threshold mapping | Literal source-to-theorem implication, with acquisition hypotheses retained | Source locations and source hashes checked; no acquisition campaign rerun |
| Reflection and zero noise | Independently checked event identities and exact zero-variance implication | Atom control rejects equality under reflection; zero noise is handled analytically |
| Component comparison inequalities | Stated theorem inputs to this review; separate component reviews apply | Not represented as reverified by this union checker |
| Full conjecture, finite base through 41, larger-noise coverage | Not established by this union | No claim or new generation campaign |

## Exact joins

The left theorem (`leftcount.tex:24`) assumes n>=42, p in [1/4,2/5],
U0 in [-.7,a0], U1 in [-a1,.7], a0+a1<=.068, conditional centering,
raw |H|<=1.84, 0<lambda<=.01 and C in [.4095,.41]. Its phase is
[-109/500,391/500]=[-.218,.782], and its conclusion is
Delta_C<−lambda/100.

The old right theorem (`counts-v11.tex:10`) assumes n>=42,
p in [.4,.53], common amplitude .6, inward sum<=.072, conditional centering,
raw |H|<=1.84, 0<lambda<=.03 and C>=.4. It covers the complete shifted
phase interval [-34/125,91/125] and proves Delta_C<−lambda/100.
The older v10 theorem for 0<lambda<=.02 and every C>=0 is a separate,
unchanged statement; the union does not silently replace its coefficient
range by C>=.4.

On .03<=lambda<=.075 the negative-inner component covers
u in [-.15,0]. The outer component (`outer.tex:16`) covers
u in [-.272,-.15] union [0,.728], in fact for every 0<lambda<=.075.
All remaining premises and the definition of Delta_C agree exactly.
The union is therefore the whole interval [-.272,.728]. The shared
endpoints -.15 and 0 occur in both adjoining components; lambda=.03
occurs in both old and new noise intervals. The extended right statement
is Delta_C<0, because the negative-inner component does not claim the
stronger −lambda/100 margin. The union preserves that distinction.

Both phase intervals have length exactly one. For any real
x=np+H*sqrt(v+s), choosing k=floor(x-lower_phase) puts the phase in
[lower_phase,upper_phase); the closed endpoint versions only add choices.
Elementary bounds also make k interior throughout each row. Consequently
this is an all-threshold anchor construction under the raw H premise, not
a sampled phase selection. The review checker verifies the common
refinement strata: endpoint incidence, rather than positivity sampled at
midpoints, is what certifies the interval cover.

At p=.4 the probability domains overlap. They need not choose the same
integer anchor, nor need a law satisfying the weaker .7 strip satisfy the
.6 strip. Each row asserts its own implication with its own support and
coefficient premises. The Bernoulli bound is valid at every integer
anchor, so either available row excludes the witness. The overlap creates
no gap and licenses no inference from the weaker strip to the stronger one.

## The normalization preserves the actual marginal

Let Z be the original mean-zero, variance-one witness. Write
m0=E(Z|B=0), m1=E(Z|B=1), ell=m1−m0>0 and p=P(B=1).
Mean zero gives m0=−p*ell and m1=(1−p)*ell. For
U=(Z−m_B)/ell, conditional centering is exact and
Y=B+U=(Z−m0)/ell. If theta=E(Z−m_B)^2, total variance gives

`1 = theta + p(1-p)*ell^2`.

Thus s=E U^2=theta/ell^2 and v+s=1/ell^2. Positivity of ell then
makes (Y−p)/sqrt(v+s)=Z pointwise, not merely in distribution.
It follows that lambda=ns=n*theta/ell^2. All conditional product laws
are the actual conditional laws of this same marginal.

For sums, sum Z_i<=H is exactly sum Y_i<=np+H/ell.
The original raw threshold H is unchanged. Its normal term is
Phi(H/sqrt(n)); H itself is not a standardized threshold for the sum.
The checker includes 12 actual three/four-point marginals and shows that
replacing s by theta fails on each. The universal identities above,
not those examples, prove the mapping.

For sign-labelled acquired witnesses, the actual central gap has endpoints
−A_minus and A_plus and no atom at zero. Then

`a0=p−A_minus/ell`, `a1=(1−p)−A_plus/ell`,

are nonnegative by conditional-mean ordering, and their sum is the actual
inward displacement d. The v11 left support proposition
(`leftpanels.tex:9`, especially lines 86–99) gives
−.6<U0<=a0 and −a1<=U1<.7 with d<.068. These imply LEFT-01's
closed common .7 strip and inward upper bound. The v10 connection
proposition (`geometry.tex:321`) gives both .6 rays on all thirteen
closed panels40–52. Together with the global d<.068<.072, it gives
the right row's support premises. The stronger strict acquired bounds
may be relaxed to the closed comparison bounds.

The raw bound |H|<=1.83605680 comes from the retained four-pass export
(`manuscript/arxiv-v1/sections/04-fixed-entry.tex:862`), and is strictly
below 1.84. It is not derived from the new count theorem. Those support
and raw-threshold inputs retain the actual index, attained fixed-target
contact, coarse-entry and sharp-predecessor hypotheses. This review does
not treat a table of bounds or a historical PASS as an independent proof
of that acquisition chain.

## Coefficient, Bernoulli and reflection scopes

C_E=(3+sqrt(10))/(6sqrt(2pi)) satisfies .4095<C_E<.41, hence also C_E>.4.
The checker independently encloses pi using Machin's identity and finite
alternating arctangent sums, checks rational enclosing squares for sqrt(10),
and bounds C_E squared. The left upper restriction C<=.41 must remain:
the left joint cubic estimate uses it in endpoint guards, and rho>=rho_B
is false on the whole left probability interval. The union does not infer
that false inequality or extrapolate LEFT-01 to all larger penalties.

For the chosen anchor define
B_k=sqrt(n)[F_B(k)−Phi((k−np)/sqrt(nv))]−C_E*rho_B.
The external strict finite-n Bernoulli theorem gives B_k<0 at every anchor.
Delta_CE is exactly the witness's fixed-target excess minus B_k. Thus
Delta_CE<0 makes that excess negative. No uniform Bernoulli reserve or
sharper formula outside its probability domain is required.
At s=0, E U^2=0 implies U=0 almost surely. The law is then itself the
standardized Bernoulli law, so the external theorem applies directly.
There is no limiting argument that loses strictness at zero noise.

For a negative closed-CDF discrepancy, reflection gives

`P(−S<=−H)−Phi(−H/sqrt(n)) = Phi(H/sqrt(n))−P(S<H)`

which is at least Phi(H/sqrt(n))−P(S<=H), with possible strict inequality
at an atom. Equality of the two expressions must not be assumed. The
retained fixed-target reflection/attainment proof is at
`manuscript/arxiv-v1/sections/02-fixed-target.tex:92`.
The reflected law must acquire its own oriented hypotheses; the probability
range [.25,.53] is not invariant under p->1−p. The final union explicitly
retains reflection and acquisition instead of claiming a two-sided theorem
from a single signed branch.

## Dependency wording and what remains

The revised phrase “inherited full-count grid” correctly distinguishes the
old count proof from the new 291-cell rational cover. Within the union rows,
no downstream half-amplitude confinement, harmonic/fractional-part gain,
marked crossing or count-curvature module is used by the direct comparison.
This is a local DAG replacement after acquisition; it is not permission to
delete these modules wherever other arguments still use them.

The union correctly retains the external quadratic-hinge theorem,
finite normalization, exact count conditioning and small executable
inequalities. The own-count/cubic reserve on the left is of order s=lambda/n,
not lambda. The normalizations and same-law definitions match all components.
Neither a moment-relaxation optimizer nor a fixed-law limit enters the join.

Larger noise still reaches beyond these comparison ranges: the retained
geometry gives only lambda<77/125=.616 globally. The old 11,264 nominal
signed-box entry remains an ancestor, as does the independent finite base
through 41 required for the least-failure argument. The union asserts no
unrestricted propagation theorem or full-conjecture proof. Its final
preservation paragraph and explicit open ranges keep this limitation clear.

## Reproduce and source binding

`union-review-check.py` imports no constructor program. Run:

```
python3 -I -B mathematics/simplification-v12/2026-10-28/union-review-check.py CONSTRUCTOR_REPO_ROOT
```

Fresh output and return code are saved under
`runs/union-review-v12-20261028/check02/`. The checker binds ten reviewed
sources by SHA256 before performing any checks. This report concerns those
exact sources. Hash agreement is integrity evidence, not a mathematical
proof. Full final pins are in the run output. The earlier check01 binds the
pre-clarification source and is preserved as such; check02 binds the final
union source and all component sources. It checks 28 exact refinement strata
and the 12 marginal controls. No root proof or inherited file was edited by
this reviewer.
