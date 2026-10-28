# Common-noise closure and quantitative crossing loss

Baseline: 656232ea8d9561a3f47aefa083ead4f6ba4206ca.
Worktree/branch: loss-v14, research/loss-v14-20261028.
Only new proof, check and evidence files are added. No manuscript, old
certificate, reference or remote branch is changed.

| Result | Mathematical status | Execution status |
|---|---|---|
| Sharp Berry–Esseen bound for Bernoulli plus small independent noise, with explicit margin | Locally derived using the external Schulz theorem; independent review pending | Fresh exact checks and outward CDF controls PASS |
| Common-noise crossing bound g >=119 lambda/[44(1+17lambda)] | Locally proved under common-law, independence, width and threshold premises | Fresh exact constants and actual count controls PASS |
| Positive gain above the noiseless phase | Refuted by actual four-point iid laws, including moderate noise | Exact rejecting controls PASS |
| General unequal-noise closure or complete finite base | Open | Not claimed or certified |

## Selected theorem

Let B~Bern(p), 1/4<=p<=3/4. Let U be centered, independent of B, with
support in an interval of width at most 1/5. Put v=p(1-p), s=E U²,
X=(B-p+U)/sqrt(v+s) and rho=E|X|³. For every integer n>=1,

    √n sup_H |P(sum X_i<=H)-Phi(H/√n)| <= C_E rho - 3s/(1000 v^(3/2)).

The complete three-page proof is loss-closure.tex. There is no noise ceiling,
count cutoff or threshold restriction. The margin is relative to the actual
per-summand noise variance and remains valid for arbitrarily small defects.

The argument has three exact edges:

1. Independence permits conditioning on the noise sum and applying Schulz's
   binomial theorem at every resulting real threshold, including atoms.
2. Replacing the n noises by matching Gaussians costs at most
   phi(0)(E|U|³+sqrt(8/pi)*s^(3/2))/(6√n v^(3/2)).
   This is a finite Taylor argument with a global third-derivative bound.
3. The support width preserves the signs of B-p+U. Its exact absolute
   third moment is v(1-2v)+6vs+(2p-1)E U³.
   Thus rho-rho_B >=(27/400)s/v^(3/2), whereas the normalized smooth error
   is at most (3/125)s/v^(3/2). Since C_E>2/5, the stated margin remains.

This is a sharp-bound theorem for a subclass. It does not assert negative
direct comparison against the discrepancy at every selected Bernoulli anchor.

## Exact dependency removal

When acquired conditional laws U0 and U1 coincide, B is independent of U.
The common support lies in [-a1,a0], of width at most .072 on the right or
.068 on the left. These are below 1/5, and the acquired p-domain is inside
[1/4,3/4].

For precisely this subclass, the theorem supplies strict exclusion of a
contrary sharp-bound witness at every positive noise level. Count/Poisson
and weighted-crossing comparison computations are unnecessary there.
Acquisition and contact are not used in the theorem itself; they remain
relevant to identifying a general witness. Nothing currently forces its
conditional noise laws to coincide.

The theorem does not depend on loss-common.tex or the v13 crossing theorem.
Unequal noise, independent C4/BASE41 and the global conjecture remain open.
Existing certificates are retained.

## External theorem checked

The single external probability input is Jona Schulz, *The optimal
Berry–Esseen constant in the binomial case* (2016), Theorem 1, printed page 1
(PDF page 11), [primary dissertation](https://d-nb.info/1197702695/34).
The statement was read directly on 28 October 2026. It bounds the absolute
closed-CDF error over all real thresholds, every p∈(0,1) and every positive
integer n by C_E(p²+(1-p)²)/sqrt(np(1-p)), strictly.
The stronger separate bound restricted to [1/3,2/3] is not used.
This task did not reprove the dissertation's theorem.

## Supplementary crossing result and failed shortcut

For a common centered noise law of width at most .072, provided
n*a0<=t<n*(1-a1), the exact identity g_n(t)=E{t-sum U_i} gives

    g_n(t)>=119 lambda/[44(1+17lambda)].

Hence g>=3lambda/8 for lambda<=.36 and g>=2lambda/5 for lambda<=.32.
The proof uses 1-|phi_U(2pi)|²>=34 Var(U), independence, and a fractional-part
minorant. It applies to arbitrary common noise, not just symmetric noise.
It is unweighted and does not by itself absorb weighted curvature or repairs.

Positive excess above the noiseless phase is false. For n=42, p=1/2,
common U=±1/100 and phase 3/4,

    g-3/4 = -151229281/4398046511104 < 0.

Here lambda=21/5000 and H=75/sqrt(2501)<1.84. At phase 1/2 the same
positive-noise law has exactly zero excess. Moderate-noise counterexamples
are n=512, p=1/2, U=±1/40, lambda=.32 and n=160, p=7/20, the same noise,
lambda=.1. Their phase-3/4 excess is strictly negative. Both raw thresholds
and all stated strip bounds are legal. Contact is not asserted. These
examples refute an implication from the stated noise/threshold hypotheses,
not Berry–Esseen.

## Bounded reproduction and trusted arithmetic

Run from the repository root with a fresh identifier:

    python3 -I -B mathematics/simplification-v14/2026-10-28/loss-run.py NEWID

The final proof-bound run is runs/loss-v14-20261028/check02:
507 checks, 40 actual moment cases, 120 iid-product/conditional-mixture
identities, 156 outward rational closed/left-limit CDF events and six
rejecting controls. The original check01 remains intact; the only later
proof edit clarified signed and absolute third-moment definitions.

Probabilities use exact Python integers/Fractions. Direct iid product
enumeration is compared with an independently assembled binomial/noise
convolution. Actual controls include zero noise, both p endpoints, skew
and reflected two-point noises, nearby four-point noises, a rare remote
atom within the width cap, and small/large threshold atoms.
The CDF controls use integer square-root enclosures, the Machin arctangent
identity with alternating rational bounds, and an alternating integrated
Gaussian series. Every enclosure points outward. These selected event
checks are not substituted for the analytic all-threshold proof.

Rejecting controls cover positive excess, strictly positive excess at every
positive noise, omission of iid independence, extending the moment-payment
claim outside the p-domain, ignoring sign changes outside the support width,
and pooling unequal conditional laws as independent noise. At p=.1 an
actual small common symmetric noise decreases rho; this refutes the extended
moment lemma, not the main conjecture.

Both notes compile cleanly to three pages. Final builds are
loss-closure-build02 and loss-common-build01; every page was rendered and
inspected. Receipts contain source hashes, commands, versions and return
codes. Arithmetic PASS is not a proof of Schulz's theorem or of the
remaining structural reduction.
