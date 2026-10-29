# Coordinator's mathematical review

**Review outcome: no unresolved blocker found within the stated local and
conditional scopes.** The independent acquisition/composition review,
independent small-noise review, and independent generic-comparison review
are complete and bound to the final sources. The coordinator reconciled
their hypotheses and read their checkers. This is internal research review,
not external refereeing or formal verification.

The accepted scope is the local common-strip theorem and the explicitly
conditional acquired-witness implication in `composition.tex`. The coordinator
read all four component proofs and their finite checkers. The elementary
small-noise proof and the composition were constructed by the coordinator;
their independent review is supplied separately. Acquisition and the generic
five-count theorem were constructed on different branches and cross-reviewed
by workers who did not construct the theorem being reviewed. Agreement is not
used as mathematical evidence; the derivations and exact hypotheses below are.

## 1. Direct acquisition

The defect is the actual signed quantity `(3+sqrt(10))*rho-gamma-3J`. It is
not replaced by an unweighted gap sum or a third-moment defect. When zero is
in the support, every gap is one-sided and `(b-a)^2<=2 integral_a^b |t|dt`.
Tonelli then gives `J<=rho`, contradicting `D<.047`. Compactness supplies
an actual open central gap, not just absence of an atom at zero.

I checked the expansion of the central gap plus the outer-gap integral
bound at `acquisition-direct.tex:73`. Its constant part is
`ell*w*(Q+6d(1-d)+6a0a1)`. The residual kernels are positive on the
actual conditional supports; no signed residual measure occurs. Thus all
subsequent discards have the required direction. The first broad interval
comes from the gap product lower bound, before using any numerical panel.

The transition at `:125` deserves particular care. At fixed theta, both
branches increase in d on the already established d<.2,theta<.006 domain.
Only after setting d=0 in this lower bound is theta monotonicity used to
obtain `D>=Q/sqrt(v)`. Dropping noise directly from a denominator would not
justify this inequality. The right probability endpoint is excluded by
`Q(.465)>.047/2` and `sqrt(v)<=1/2`, without assuming a false monotonicity
of Q/sqrt(v) to the left of 1/2. This produces p in (.375,.465).

For the noise bound at `:177`, the reciprocal cubic terms use the same
conditional second moments as the inward cost. Pairing each with its own
inward endpoint gives the displayed AM–GM prices Y0,Y1. There is no
independent variance allocation or replacement law. The case a_j=0 is
separate: centering then forces that conditional noise to vanish.

The support conclusion at `:209` is conditional on the actual contact and
retained heat lemma. At each boundary, Q,Q',Q'' and the contact upper bound
are negative; the derivative majorant plus c0 Q' and its first two
derivatives are also negative. Their decreasing derivatives extend the
inequality over the full ray. One differentiates the actual heat function,
not the absolute-value polynomial used only at the boundary. The signed
beta bounds are used differently on the two rays. Dividing a negative
support bound by the actual ell>1.996 gives the stated U0 bound with the
correct inequality direction.

The constructor's rare U0=-.8 law satisfies the defect budget and old
radius bound but violates amplitude .6. It confirms that contact is an
essential extra input to the second theorem. This defect-budget theorem
does not justify dropping contact, even though it no longer needs an
exported numerical radius or probability panel.

## 2. Unified five-count proof

At `unified-comparison.tex:129`, conditional convolution is performed on
one common iid marginal. The auxiliary increasing mesh exists because
its adjacent difference is at least 1-a0-a1. Finite summation by parts
gives the weighted crossing identity, with the actual closed CDF at each
count. Its residual kernel is nonnegative everywhere, including at atoms.

The sine-square minorant has derivative zero at its endpoints. Its five
translates have disjoint interiors, so grouping adjacent translates keeps
the derivative Lipschitz constant unchanged. Four centered replacements
then cost at most `4*pi²*(s0+s1)` before the factor 2/5; this is a variance
cost and remains proportional to lambda. No independence between different
count sums is assumed. Omitted translates require |V|>2 and are bounded
by the complete fourth moment divided by 16. This is an infinite-tail
argument, not a 5-count truncation.

The actual frozen variance has n-1 summands. The bound
`(1-c_minus/n)lambda<=tau<=(1+3/n)lambda` follows from its exact count
coefficients. The characteristic-function bound uses the conditional
diameter A+d, not merely a moment bound. Finite Stirling supplies all five
binomial weights. The exact exponential reserve is first reduced to n=N;
only then is it replaced by a quartic, so no unjustified monotonicity of
the quartic in n is required.

At `:292`, discard only the nonpositive adjacent-mass terms. For the others,
the exact Bin(n+1,p) identity and the stop-loss quartic majorant give a
summable curvature estimate. There are at most two exceptional near-origin
mesh points; the remaining reciprocal-square/cube tails are complete. The
conditional variance on that increasing-mass side is bounded by lambda/q,
which is valid in both possible orders of s0,s1.

The normal repairs at `:341` retain the sign of H. The variance correction
is favorable for H<=0; for H>=0 its cost contains lambda/n. The actual
absolute third moment increases relative to the Bernoulli value throughout
each row. Thus dropping the cubic correction is favorable. The resulting
E-minus and E-plus have nonnegative coefficients and are convex. The exact
identity for W'' is globally negative, proving that four endpoint tests
cover the full closed noise interval. The Compact row has substantially
larger margins than the wider Left row and uses exactly the new acquired
support assumptions.

The separate right-tangent note is a valid useful corollary: its affine
majorant follows from a square, and the new four endpoints are positive.
It preserves the old n>=42 theorem rather than replacing its smaller-index
scope by n>=200. The generic proof independently includes its row.

## 3. Small noise and the exact composition

The small-noise proof is new coordinator work, reviewed independently in
`small-review-report.md`. Its essential improvement is to retain the physical
count dependence `t_i=lambda+(delta+i)(s1-s0)`. A count-independent worst
variance would lose too much. The full fourth-moment incoming bound is
therefore linear in lambda after three convergent reciprocal-power sums.
The positive phase factor `(1-u)^(-4)` is indispensable, as an actual-law
counterexample in the review shows.

The quartic minorant is below the strict-event indicator also at zero.
The constructor reduces its rectangle by concavity and two quadratic
monotonicity tests. The independent reviewer instead checks all coefficients
of the original tensor Bernstein polynomial, without using that relaxation.
The outer Cantelli arguments have no interior minimum after the switch,
and the positive outer bound is concave. All three phase intervals are
closed and join exactly. The global binomial ratio uses a mode bound; only
the inner phase range uses decreasing subsequent adjacent ratios.

`composition.tex:30` uses the same common hypotheses in both noise
theorems, covering (0,.01] and [.01,.35]. At zero noise the strict external
Bernoulli theorem is applied directly. The shifted anchor in the small
range and the floor anchor in the larger range need not coincide, since
both statements concern the same signed excess. No small positive margin
is passed to a zero-noise limit.

The pointwise normalization at `composition.tex:61` is checked explicitly:
`1=v ell²+theta`, `s=theta/ell²`, `v+s=ell^-2` and
`X=ell(B+U-p)`. Hence it preserves the original iid law and raw threshold.
The proof uses lambda=n theta/ell², not n theta. Reflection is performed
before acquisition, with the closed-event atom inequality displayed at
`:94`. It does not preserve the signed budget or the new p interval.

## 4. Remaining inputs and meaning of the evidence

The complete coarse entry certificate and its analytic reduction are retained
inputs; they were not replayed or independently re-proved in this round.
The 11264 nominal signed boxes, the two coarse/four signed passes and the
old acceptor's internal 100-panel cover remain necessary under its existing
contract. The acquisition audit gives exact baseline source locations.
The retained heat/contact lemma, fixed-target attainment/reflection,
structural inequality, sharp predecessor and Schulz theorem also remain.

With those inputs the acquired-witness exclusion is complete at n>=700.
Without a genuine finite base it is not a proof of the conjecture or of an
unconditional cutoff. BASE41 plus least-failure acquisition confines a first
failure to42–699; it does not allow skipping that interval. Historical
optimistic logs are not substituted for a base.

Fresh scalar acceptance, actual-law tests and rejection controls are recorded
separately from the mathematical status. Small-noise actual-event checks
reuse the pinned v10 outward-normal helper; this is disclosed regression
evidence, not a second independent normal implementation. Constructor and
reviewer checks are not counted as independent where they share an ancestor.
No full Fourier replay, Lean build or expensive generation was performed.

All final TeX notes compile and have rendered-page inspection records. An
unbreakable slash phrase in the composition caused an initial overfull line;
it was rewritten without changing mathematics and the clean two-page result
was re-inspected. A test comment about odd-fold noise atoms was corrected:
the actual sum atoms are at 2 plus/minus e, while the frozen even-fold noise
has its atom at zero. The unchanged mathematical tests include both kinds.

Source pins and the final bounded-integration receipt bind this review to
the exact checked version. Hashes prove identity, not the mathematical claims.
The manuscript and all original baseline proof objects remain preserved.

The result is mature enough to incorporate into the manuscript. A further
open-ended search for smaller constants is not a prerequisite to that rewrite.
The eventual manuscript should present these three components as the selected
post-entry route and state its remaining certificate and finite-base premises
explicitly. Keep the review PR draft for the authors; no merge is performed.
