# Coordinator review of the v14 component proofs

This review concerns proofs constructed by the count and common-noise workers.
The coordinator constructed `large-index.tex`; independent review of that file
is recorded separately and is not claimed here. All conclusions below are
mathematical deductions with explicit hypotheses, not consequences of agent
agreement or of executable PASS labels.

Reviewed immutable sources:

- `counts-pair.tex`: `931fb88565922d525726ba264a867e2b0774051a4e56267d9f9d65f3142b01f4`.
- `loss-closure.tex`: `83494e6fa485557df38acdb1b9b50084530fbc3c470f8f482bb020d4a58af80b`.
- The supplementary `loss-common.tex` is bound by `reviewed-sources.json`.
- The retained crossing theorem: v13 `crossing.tex`,
  `0dda285adb9aaa24277fdc1d74843c20bc6100b2a64a0cd5ae34bb696a68a6ec`.

## Independent noise: all sample sizes and thresholds

Let B be Bernoulli(p), p in [1/4,3/4], and U be independent, centered, with
support diameter at most 1/5. Write v=p(1-p), s=E U² and
X=(B-p+U)/sqrt(v+s). The conclusion is

`sqrt(n) sup_H |P(sum X_i<=H)-Phi(H/sqrt(n))|`
`<= C_E rho - 3s/(1000 v^(3/2))`

for every positive integer n. There is no upper bound on ns and no
extremizer/acquisition premise. I independently checked these edges:

1. Conditioning on all U_i leaves an actual Bin(n,p) at the random threshold.
   The external input is the closed-CDF absolute inequality in Schulz,
   *The optimal Berry–Esseen constant in the binomial case* (2016), Theorem1,
   printed p.1 (PDF page11, zero-based10), [original thesis](https://d-nb.info/1197702695/34).
   I opened the primary source and checked its all-p, all-n scope. Its sharper
   middle-p formula is not needed here.
2. Replacing one U_i by an independent Gaussian of variance s cancels the
   degree0,1,2 Taylor terms. The uniform third-derivative norm is
   phi(0)/(nv)^(3/2), because the maximum of |(x²-1)phi(x)| is phi(0).
   Adding n replacements yields the exact stated bound proportional to
   `(E|U|³+sqrt(8/pi)s^(3/2))/(sqrt(n)v^(3/2))`.
   The Gaussian convolution then has variance n(v+s). This is finite
   replacement, uniform over every threshold and varying law; no limiting
   remainder or Fourier inversion is hidden in the step.
3. The support and centering give |U|<=1/5 and s<=1/100. Since
   min(p,1-p)>=1/4, neither conditional support crosses the origin after
   centering Y. Direct expansion gives
   `E|B-p+U|³=v(1-2v)+6vs+(2p-1)E U³`.
   Subtracting the quadratic upper Taylor bound for (1+s/v)^(3/2) leaves
   at least `(3/16-1/10-1/80)s=3s/40` before normalization.
   The normalization ratio exceeds9/10, giving
   `rho-rho_B>=27s/(400v^(3/2))`.
4. The smoothing error is at most3s/(125v^(3/2)); multiplication of the
   moment gain by C_E>2/5 gives27s/(1000v^(3/2)). Their difference is the
   claimed3s/(1000v^(3/2)). At s=0 all corrections vanish and the external
   Bernoulli theorem supplies the conclusion. Taking a supremum introduces
   no atom problem because the conditional CDF bound already holds for
   every real threshold with a uniform right side.

No blocker found. The proof has a real restriction: U must be independent of
B. Equal conditional noise laws imply exactly this independence; pooling two
unequal laws does not. In an acquired strip their common support is contained
in [-a1,a0], so the width condition follows immediately. Count and Poisson
computations can be omitted for this entire subclass, but this supplies no
reason that a general maximizing witness belongs to it.

The constructor checker was read. Its independent product enumeration and
conditional convolution are different implementations. Its normal bounds use
rational alternating expansions and outward square-root enclosures. The
finite test events support implementation checks only; the all-n theorem is
the preceding analytic argument. No second run is called an independent proof.

## Paired crossing kernels and the two central families

Adding the k and k+1 local crossing identities and using put–call parity gives
exactly

`g_k+g_(k+1)=u+P(W_k>u)+E(W_(k-1)-u-1)_+`
`-E[(u-W_(k+1))1{W_(k+1)<=u-1}]`.

The incoming equality has weight one and must be included. The two nonnegative
kernels permit a lower bound using min(pi_k,pi_(k+1)); all other kernels may
then be discarded. This is not a relaxation with independently chosen laws.

For the proposed hinge, dividing `(u+z)` by `(z-y)²` for z>=b=1-u
has derivative with sign `-(z+y+2u)`. The hypothesis y>=-1-u makes it
nonincreasing, proving the bound by its boundary value. Its expectation is
a weighted tail and cannot be clipped at one. The recorded Z=±3 example
correctly refutes that shortcut.

The central family theorem requires n>=42, p in [.4,.53], np integer,
H=0, and exactly one noisy conditional law with outer atom magnitude3/5.
Writing lambda=(9/25)mu, 0<mu<=1, I checked:

- The central mass estimate follows by adding independent uniform noise to
  an integer-valued variable, applying the density-cap variance inequality,
  and using the exact adjacent-binomial ratio k/(k+1). This gives normalized
  minimum mass>1/2 without Stirling or a local limit theorem.
- For rare negative jumps, the own positive-noise event is no jumps, with
  probability>exp(-mu)>=exp(-1)>1/3. Below mu=2/5 the incoming event requires
  at least two jumps, with weighted expectation at most(3/5)mu². Above2/5 it
  requires at least three jumps. Dividing by j(j-1) and using the second
  factorial moment gives at most1/5. The rational monotonicity argument in
  m and mu is valid, including mu=1 and m=20. The reserve is>2/15.
- For rare positive jumps, the own event has probability>=mu/(1+mu)>=mu/2.
  The incoming conditional sum cannot reach its boundary, because its
  maximal negative displacement is at most54/85<1. Its weighted tail is zero.
- The central normal terms cancel. The retained signed curvature costs less
  than lambda/(4*(6/25)*6). The moment correction has the favorable sign
  under these right-strip hypotheses. The resulting strict margins are
  1/240 and25lambda/48 respectively, as claimed.

The first margin need not vanish as lambda goes to zero: a positive small
noise shifts an atom across the fixed closed threshold. This is consistent
with the discontinuity of a CDF at that threshold. Zero noise is excluded
from the family theorem and must not be inserted by continuity.

The selected-bias proof is also valid. The leave-pair residuals decrease by
at least zeta=1-a0-a1. Under the extra strict width hypotheses, at most one
lies in each active truncated-mean interval. The upper endpoint contributes
zero by centering and the lower endpoint is included. This gives the stated
a0,a1 caps without incorrectly treating the selected sum as centered.

No blocker found within these family and support scopes. The theorem does
not remove count work at general thresholds, noninteger np, or general
conditional noise distributions.

## Supplementary common-noise crossing bound

Using a common shift W for every conditional count preserves the relevant
conditional marginals. The endpoint condition then gives
`g=E{t-W}` exactly. The diameter bound and independent-copy cosine estimate
yield `1-|phi_U(2pi)|²>=34s`, hence
`|phi_U(2pi)|^n<=1/(1+17ns)`.
The inequality sin²(pi x)<=pi x on [0,1] gives
`g>=119lambda/[44(1+17lambda)]`.
This is unweighted and is not used in the all-n independent-noise theorem.

The symmetric floor calculation and exact42-summand example correctly
refute a positive gain over the noiseless phase. The supplied dependent-noise
example refutes dropping independence. Neither is a counterexample to the
Berry–Esseen conjecture.

## Review boundary

Mathematical status: locally derived proofs, independently checked as above,
with the external binomial theorem and retained crossing/curvature inputs
explicit. Execution status: fresh constructor controls are preserved; bounded
integrated replay is recorded separately in the integration receipt.

No finite-base, attainment, contact or general-acquisition theorem is proved
by these components. No existing certificate is deleted. Human author/referee
review remains appropriate before presenting these as a completed paper.
