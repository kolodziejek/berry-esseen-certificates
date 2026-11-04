# v20 local comparison replacement

This is a bounded review of the new small-noise argument and its integration,
not a new audit of every analytic or acquired-data ancestor of the theorem.

## Mathematical and execution status

The joint-count implication is locally derived and checked: for the actual
conditional iid law, inward spacing `c=1-d0>1/2`, legal count `1<=k<=n-1`,
`|u|<=1/2`, and the original incoming-mass bound, it gives

`E G(R)-f(u) <= -O + R0*t*(A^2+3t)/(c-u)^4`,

where `O<=P(W_k>u)+f(u)` and `t=E W_k^2`. This is Lemma
`j:local:joint-count-moments`. The cutoff uses one common family of independent
conditional variables; the independent binomial selector reproduces the
actual conditional sum at each count. There is no product-law relaxation.

The new uniform numerical implication has fresh acceptance for all 83 acquired
rows (`construction_all83_01/RESULT.json`). The finite replacement has fresh
acceptance for all 267 rows (`construction_finite_capture02/RESULT.json`), with
17,115 regenerated native normalization gates and 65,148 inverse-checked
Bernstein coefficients. These are local implications under their recorded
same-law acquired premises, including the original finite binomial reserves
and positive-39 allowance. They do not generate those premises anew.

## Proof checks

* Every increment of `j+W_j` is at least `c`. Thus `R=i>=1` implies
  `W_k<=u-ci<0`, and `x/(cx-u)^4` decreases for `x>=1` because
  `3cx+u>0`. This proves the complete staircase bound
  `R_+<=W_k^4/(c-u)^4`, including exterior counts.
* `W_k>u` is the strict outgoing event, whereas the cutoff is defined by a
  closed event. Atoms at either boundary are preserved.
* Independence and centering give `E W_k^4<=A^2 t+3t^2`. The already printed
  shifted-quartic minorant, Cantelli, and the zero minorant give the four
  outgoing witnesses; no new unproved probabilistic comparison is invoked.
* The four domains meet at `r=z_-t`, `r=z_+t`, and `u=0`; `z_±T<1/2`
  makes their closed union the whole phase interval. Near domains divide by
  positive `t`, and clear `(c-u)^4`. The negative far domain also clears
  `t+r^2`. Zero noise is a separate Bernoulli case; no division at zero occurs.
* For signed eta, the exact admissible lower score coefficient is
  `J_eta=min(m*eta*omega_lo, eta*omega_hi)`. Negative eta needs the upper
  variance and upper mass. Positive-39 retains
  `J_eta-repair/39+K/(39*max(.05,Lambda))>0`. The left40–42 cases retain the
  original positive binomial reserve; a nonpositive eta is not described as
  a loss relative to the Bernoulli score.
* Positive-39 has normalization noise ceiling `.05` even when the acquired
  `Lambda` is smaller (18 rows). The text explicitly uses that normalization
  ceiling to construct `T`; actual applicability remains
  `0<lambda<=min(.05,Lambda)`. Other finite families use that minimum in both
  places. This matches the literal native polynomial targets.

## Removed and retained dependencies

The whole old scaled-quartic/relative-Poisson/relative-Bennett small-noise
paragraph is removed. Its three private labels (`scaledown`, `tinynegative`,
`tinypositive`, with prefix `j:local:shortloc:`) have no remaining references.
The common cutoff definition is moved once and retains its original label.
No MID polynomial-majorant research lemma is inserted.

The common tail lemma and its finite evaluations remain necessary for the
existing MID and marked-deletion LOW comparisons. Their analytic proofs and
closed noise/phase covers remain. The shifted quartic is proved once, then
reused. The whole-count curvature, marked crossing, harmonic reserve and
finite signed inverse-index rules remain unchanged except for references to
the moved cutoff. The 83 uniform and 267 finite TINY cells replace their old
small-noise witnesses; no acquired support, normalization or binomial theorem
is removed.

## Tests and limitations

Previously completed exact actual-coupling tests are preserved at
`analytic_actual01/checked/RESULT.json`: 23,920 coupled paths, 90 iid CDF
identities, and atom/spacing mutation rejection. The new finite acceptance
has 16 object, 3 source and 3 scalar-domain rejection controls, duplicate-JSON
rejection, and a negative-eta counterexample to the incorrect lower-variance
rule. These tests support the implementation; they do not replace the
displayed proof.

The local source was edited only in `journal-v20/sections/local.tex`.
The saved before-copy remains byte-identical to journal-v19. Initial full
builds were 100 pages, compared with the prior 98-page v19. The analytic
argument is conceptually simpler but no net page reduction is claimed.
Final source/PDF pins and the exact bounded visual-inspection scope are in
the additive integration manifest and layout receipt, not in this narrative.

The full theorem still depends on the established attainment/contact,
Fourier, acquisition, confinement, finite-base, MID/LOW and composition
arguments at their original scopes. This replacement makes no formal-proof
or external-human-referee claim.
