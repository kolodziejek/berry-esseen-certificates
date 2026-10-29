# Direct count comparison up to ns = 1/50

This note records a new conditional theorem, not a global Berry–Esseen proof.
The branch starts at `00ba714897f2e09995d78354ac3c8931e257cd05`; no inherited
source, certificate, or manuscript was edited.

## Result and scope

Theorem 1 in `moderate-noise.tex:11` establishes, for every nonnegative
penalty C, a strict comparison with the matching Bernoulli count:

    sqrt(n)[P(S_n <= H) - Phi(H/sqrt(n))] - C rho
      - sqrt(n)[F_B(k) - Phi((k-np)/sqrt(n p q))] + C rho_B
        < -lambda/100.

Its exact hypotheses are n >= 42; p in [2/5,53/100]; Y=B+U with
E(U|B)=0; both conditional noises bounded in absolute value by 3/5;
U_0 <= a_0, U_1 >= -a_1, a_0,a_1 >= 0, a_0+a_1 <= 9/125;
0 < lambda = n E U² <= 1/50; |H| <= 46/25; and the always available
count anchor with phase in [-34/125,91/125]. The standardized summands are
X=(Y-p)/sqrt(pq+E U²). Independent copies use one common marginal.

This extends the separately reviewed `small-noise.tex` theorem from
lambda <= 1/500 to lambda <= 1/50. It includes arbitrarily small positive
noise; no positive lower cutoff or additive noise-independent error is used.
At lambda=0 the law is Bernoulli and the separate sharp Bernoulli theorem
applies. Taking C to be the sharp Bernoulli constant gives the intended
fixed-target exclusion.

| Result | Mathematical status | Execution status |
|---|---|---|
| Conditional comparison for all 0 < lambda <= 1/50 | Locally derived; full analytic proof; independent review reported no blocker | Fresh PASS of all 62 exact rational gates |
| Quadratic-hinge Poisson comparison with variance upper bound | External theorem: Pinelis Proposition 2.8 / Corollary 2.11 | Primary source read; no numerical computation needed |
| Quartic own-count inequality on continuous rectangles | Locally proved by concavity and exact quadratic minimization; independently rechecked using full tensor Bernstein coefficients | Fresh PASS; 40 independent Bernstein coefficients reported by reviewer |
| Extensions to lambda <= .03, .05, .075 | .03 heuristic only; .05 and .075 fail the tested sufficient envelope | Bounded floating discovery; explicitly not acceptance |
| A global acquisition theorem or full conjecture | Not established by this note | Not claimed |

## Why the argument is shorter

Conditioning gives an exact count identity. Drop all outgoing counts except
the own count k. A quartic polynomial below the strict half-line indicator
controls that own count; Cantelli covers phases farther from zero. The incoming
counts use one standard Poisson comparison. Their infinite tail is summed by
an elementary factorial-moment inequality and a geometric series. Four closed
phase intervals finish the comparison.

The accepted check has 62 scalar inequalities, with no parameter grid,
large-n cutoff, sampled derivative calculation, stored polynomial coefficient
array, or generated count certificate. Most gates merely verify the finite
Stirling normalization already used in the manuscript. The complete proof,
including that normalization and explicit constants, compiles to six pages.
This is the length of a research note, not a predicted manuscript page saving.

## Dependency map and proposed removals

1. Actual iid conditional representation and the 3/5 strip imply the exact
   conditioning identity (`moderate-noise.tex:44`) and moment bounds.
   Acquiring this representation and strip remains a separate dependency.
2. Finite Stirling, the count displacement, and elementary Gaussian calculus
   give normalization and repair bounds (`moderate-noise.tex:72`). The finite
   Stirling proof is retained at
   `manuscript/arxiv-v1/appendices/count-comparison.tex:131`. Its old surrounding
   restriction p < 1/2 is not reused: the new proof explicitly bounds the
   absolute entropy derivatives on [9/25,23/40], across 1/2.
3. Conditional centering plus absolute support 3/5 give third/fourth moment
   bounds. The one-sided support restrictions give rho >= rho_B; no assumption
   on the sign of p-1/2 is used (`moderate-noise.tex:142`).
4. Pinelis, [On the Bennett–Hoeffding inequality](https://arxiv.org/abs/0902.4058),
   Proposition 2.8 and Corollary 2.11, printed p. 9, supplies the quadratic-hinge
   moment comparison (`moderate-noise.tex:167`). Its hypothesis is total variance
   **at most** the stated value, licensing inflation before selecting a hinge.
   Applying the hinge to -W gives the closed incoming tail, so atom collisions
   require no limiting convention. The external theorem is also consistent with
   [Bentkus–Juškevičius, Remark 1.6, equation (1.19)](https://arxiv.org/abs/1111.6358).
5. The elementary own-count proof (`moderate-noise.tex:238`) and rational
   infinite-tail bound (`moderate-noise.tex:198`) replace marked crossings,
   fractional-part smoothing and count curvature on the theorem's domain.
6. Four explicit phase intervals (`moderate-noise.tex:296`) provide continuous
   coverage. There is no inference of coverage from sampled positivity.

Consequently, **within n >= 42, p in [.4,.53], 0 < lambda <= .02 and the
stated acquired strip/threshold hypotheses**, the downstream comparison no
longer needs a half-amplitude acquisition step, harmonic smoothing, marked
first/double crossings, discrete count curvature, or their computational
verification. The only incoming support bound needed is 3/5.

This does **not** remove those dependencies for .02 < lambda <= .075, for
other probability panels, or from any other theorem that uses them. It does
not remove the acquisition of the 3/5 strip, the threshold bound, the finite
Stirling argument, or the Bernoulli endpoint theorem. No existing certificate
has been deleted or relabelled.

## Checks, evidence and limitations

Acceptance command, from this worktree:

    python3 mathematics/simplification-v10/2026-10-28/moderate_noise_check.py

Fresh evidence: `runs/moderate-noise-v10-20261028/check01/`. The receipt records
the command, interpreter, return code, and input hash. Exact terminal margins
above the desired lambda/100 allowance are:

| Phase interval | Margin |
|---|---:|
| [-1/20,1/20], after division by lambda | 113307367/16930513600 |
| [-34/125,-1/20], using the upper noise endpoint | 95575595137/4788968940000 |
| [1/20,1/10], using the upper noise endpoint | 8209/4872000 |
| [1/10,91/125], using the upper noise endpoint | 389390249/17290880250 |

The proof checks positive brackets before multiplying by a lower count mass.
The small-noise rectangle includes t=0 for the divided polynomial, and its
positive margin persists as lambda tends to zero. All geometric-tail
denominators and all hinge-admissibility conditions are strictly positive.
The first incoming term uses hinge 1 only where admissible; positive outer
phases use Cantelli instead.

The independent reviewer `/root/primitives_v10` rederived the probability
reduction, conditional variance, normalization, third-moment repair, Poisson
hinge conditions, and closed interval coverage. It also checked the full
quartic on both rectangles using 40 tensor Bernstein coefficients, without
the constructor's quadratic truncation, and reported 36 actual centered,
variance-normalized marginal laws with 144 exact own-count checks including
collisions and one vanished noise sign. Its separate report and evidence are committed in
`4bf84d90b7bd25736a04cf02d09439e07e252bda` on the independent review branch
and should accompany integration; agreement alone is not the proof. The
review pins the final TeX SHA-256
`bda129c029de36bac7a8455ec3f1e7f7726cea9b21bf89671be7e9095f775074` and
checker SHA-256
`13c4c27a66cb692a5ac480a986e8240a8ab38b59c066cb3f24d81d9676a13f11`.

The exploratory script `moderate-noise-discovery.py` tested only 1,407
floating points. Full fresh metadata is in
`runs/moderate-noise-v10-20261028/discovery02/`; `discovery01/` preserves the
earlier identical output. The sampled envelope was positive through .03,
but at .05 it failed at five phase points (worst near -.067), and at .075
at eighteen (worst near -.097). At the latter point its own-count lower
bound was about .00534, while the incoming bound was about .02621 before
the count-ratio multiplier. That identifies the loss near negative phase
of order lambda; it is not a counterexample to the underlying theorem.

There is also an exact, admissible sufficient-bound obstruction to extending
the **same** quartic constants unchanged: at t=lambda=r=1/20, z=r/t=1,
alpha=1/2, the scaled negative-phase lower bound is 257/1250 < 3/8,
with deficit 847/5000. These variance/phase values are possible for n=42,
p=1/2, conditional U=+-1/sqrt(840), independently of B; its one-sided
slack is 2/sqrt(840) < 9/125. The actual probability may satisfy a much
stronger inequality. The checker rejects enlarging U to both 1/20 and 3/40;
some additional normalization gates also fail there.

The TeX compilation first found one escaping typo (preserved as failed
`build01/`), then passed cleanly in `build02/`. No mathematical alteration
was needed for compilation. Source and PDF hashes are in the build receipt. All six pages were rendered
and visually inspected; the final log contains no warnings or overfull boxes.
No expensive optimization or certificate generation was performed.

## Remaining research question

The accepted result stops at .02. Extending to .03 may be possible with
better phase-local constants, but the present four-interval proof does not
establish it. Reaching .075 appears to need a substantially stronger own-count
lower bound, more use of the favorable third-moment gain, or keeping some
neighboring outgoing counts. A larger discovery grid would not resolve that
analytic bottleneck by itself.
