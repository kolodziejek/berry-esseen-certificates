# Independent review of the unified five-count comparison

**Outcome: no mathematical blocker found at the recorded source.** The
common criterion proves its three stated local rows, and its Compact row
matches the new acquisition theorem without a missing phase, probability,
noise, or normalization condition.

This is an independent review of the comparison's analytic reduction and
finite scalar checks, not a proof of the Fourier acquisition, small-noise
comparison, finite base, or full conjecture. I constructed the new acquisition
component and the older v15 left comparison. Here I independently rederived
the generic comparison's formulas and scalar inequalities; the independent
review of acquisition is assigned separately. This disclosure matters for
the claimed independence of the different components.

| Item | Mathematical status | Execution status |
|---|---|---|
| Generic crossing, five kernels, mass, curvature, normal and cubic argument | Independently rederived from the actual marginal and displayed assumptions | New exact controls and coefficient reconstruction PASS |
| All three rows and four endpoints per row | Independently checked on the exact closed domains | 83 scalar/interface checks PASS |
| Full weighted crossing identity | Independently derived and checked against actual product probabilities | 64 exact controls, including16 exact atom cases, PASS |
| Summable signed curvature | Independently rederived, including full infinite mesh tail | 64 exact actual-law curvature checks PASS |
| Compact acquisition-to-comparison interface | Exact mapping of the stated theorem contracts | Fresh exact joins PASS |
| Small-noise theorem and zero-noise branch | Separate obligations, not supplied by this generic positive-noise criterion | Not accepted in this review |
| Unconditional cutoff / finite base | Not proved | Not claimed |

## Sources and independence of the arithmetic

Reviewed proof:
`../unified-v16/mathematics/simplification-v16/2026-10-29/unified-comparison.tex`,
SHA-256 `2be0dc58973a281accb66cf3c8dffd7209592e68278ef4c0c46805708e374938`.
The receipt records the exact constructor checker and actual-control bytes
read alongside it. No constructor function or generated coefficient array
is imported by `unified-review-check.py`.

The independent checker evaluates the displayed W and E functions at exact
integer arguments and solves their rational interpolation systems. It thus
reconstructs each quartic and quadratic using a different computational path
from the constructor's direct coefficient assembly. The completed-square
identity for W'' is checked as an identity of quadratic polynomials at three
distinct arguments. These equality checks are not sampled positivity: the
degrees are already established algebraically. Positivity uses the exact
four endpoints and the analytic global concavity proof.

The small product checker convolves actual finite atoms independently. It
computes the full iid CDF, its conditional-binomial mixture, and the weighted
crossing reconstruction separately, then requires exact equality. Its curvature
checks use the actual conditional second/fourth moments and a valid crude mode
coefficient at the small test indices; they are controls of the general lemma,
not claimed n700 exhaustive coverage.

## Analytic reconstruction

### 1. Conditional mixture, endpoints and crossing weights

The actual conditional convolution at count j is T_j. The original iid CDF
therefore equals the binomial mixture of its closed CDFs, regardless of the
auxiliary joint coupling used to place these sums on a common increasing mesh.
This is the correct place to use independence; the selected crossing count is
never asserted independent of the noise.

The phase guard gives `|t-np|<xi<1`, and `N(r-d)>xi` ensures the two mesh
endpoints. Hence L_0(t)=t, L_n(t)=0 and P(T_0<=t)=1. Independence of the
omitted coordinate gives exactly

```
g_i = L_(i-1)(t) - L_i(t) - P(T_i<=t).
```

Multiplying by pi_i and summing by parts leaves
`pi_0 + pi_1*t + sum_(j=1)^(n-1)(pi_(j+1)-pi_j)L_j` minus the weighted losses.
Replacing L_j by (t-j)_+ and telescoping again gives the linear interpolation
of F_B(k) and F_B(k+1), with u=t-floor(t). Thus no atom mass is missing.
The strict survival probability in the upper kernel is exactly complementary
to its closed CDF. In the independent controls, changing the actual closed
CDF to the strict one at a positive jump breaks the identity, as expected.

### 2. Kernel and four centered replacements

The upper part of h is `P(D>x)-E(D-x)+`, where D=1+U1. The guard A+d<1
makes x-A positive when x>=1-a1. In the interval below1, its lower bound is
`[(1-A-d)/(A+d)]*(1-x)`. Since 1-x<=a1<=d, the displayed high-kernel guard
really implies the sine-square minorant. The zero and one endpoints require
weak inequalities and are handled as such.

Each replacement consists of two independent centered insertions around the
same remaining sum. Taylor's integral remainder therefore costs
pi²(s0+s1). The regrouped adjacent translates have disjoint open supports and
zero derivatives at their shared boundaries, so their sum still has derivative
Lipschitz constant2pi². Two replacements on each side give four, not six.
This argument works for unequal conditional laws and does not pool them.

The omitted coordinate matters: the frozen variance is

```
tau = (nq-delta-1)*s0 + (np+delta)*s1,  delta=k-np.
```

Its lower bounds follow from `c_minus*r>=1+xi`; its upper bounds follow from
xi<1 and p,q>=1/3. These justify `(1-c_minus/n)lambda <= tau <= (1+3/n)lambda`.
The fourth moment uses independence and |U_j|<=A, which follows from d<=A.
All omitted nonzero bump translates have |V|>2, including the zero bump
values at integer boundaries. Their entire sum is therefore bounded by
E V^4/16. No infinite count tail or missing boundary allocation remains.

The cosine bound is applied to the difference of independent copies of one
conditional noise, whose diameter is at most A+d. It yields characteristic
modulus at most exp(-kappa Var). Only the independent frozen summands are then
multiplied. The conditional diameter is a genuine premise: the kappa=3 bound
fails at displacement3/4 and at1, so it cannot be extrapolated to the left
row without its separate kappa=7/5 calculation.

### 3. Binomial masses and the order of the n reduction

For the five counts, |i-np|<xi+3<4; N>=42 and p,q>=1/3 keep them interior.
Every entropy Taylor segment lies in the expanded probability interval with
variance product above zeta. The entropy cost is at most8/(n zeta), and the
factorial remainder costs at most1/(12n zeta). Finite Stirling then gives the
stated lower mass. The proof uses an explicit finite remainder, not a local
central limit approximation.

The exact exponential reserve increases with n at fixed lambda. Replacing n
by N **before** applying the quartic exponential lower bound is valid. It is
not necessary, and would be unjustified without a check, to assert that the
quartic approximation itself increases with n.

Since every g_i>=0, discarding the remaining weights and replacing the five
remaining normalized masses by m is valid even if an intermediate numerical
reserve happened to be negative. The final endpoint checks ensure a positive
usable reserve after all corrections.

### 4. Curvature, including the small-noise bend and the full tail

The exact adjacent-binomial identity has numerator np-q-j. After discarding
only its nonpositive terms, this is at most (a+c)_+, with a=t-j and
c=(np-q-t)+. With c<1, at most one mesh point occurs in each of (-c,0) and
[0,1). Their combined bound is `c*sqrt(T)+T/4`; the linear square-root term
has not been lost.

For positive a, Cauchy gives a B_j<=T/4. The quartic inequality follows from
`27x^4-256x+256=(3x-4)^2(3x^2+8x+16)`; the last quadratic is positive for
all real x. This gives the stop-loss tail27M/(256|a|^3). The complete tail sums
are bounded by5/3 and5/4. The latter is strict even though the finite
rational sum plus the chosen integral equals5/4, because the decreasing
integrand strictly exceeds the discrete tail on intervals of positive length.

The mode estimate with beta=.41 is uniform on[1/3,2/3]: a mode displacement
has absolute value<=2/3, yielding `z(1-z)>=v*(1-1/M-2/M²)>39v/40` for M>=43.
Finite Stirling and exp(1/516)<516/515 give the required constant. The
increasing-mass counts satisfy j<np, so their actual variance is at most
lambda/q, not lambda. The affine J bound is justified by its square-root
majorant guard. This completes the full curvature bound without a truncated
mesh or allocation relaxation.

### 5. Normal interpolation and the actual cubic correction

Schulz's all-p finite-n strict theorem applies at each of the two integer
anchors. Linear interpolation preserves its strict bound; no restricted-p
quantitative Bernoulli reserve is used.

The normal interpolation remainder uses the positive part of G'' throughout
the unit interval. The negative-H case has favorable variance change and
curvature offset at most cbar. The positive-H case has zero offset and an
additional variance repair at most `phi0*w*s/(2*v^(3/2))` after multiplication
by sqrt(n). Substituting s=lambda/n produces exactly the displayed E_+/n.
This factor of n is present in both the proof and checker.

The support guard d<r keeps the two physical signs fixed. The raw absolute
third moment expands to

```
v(1-2v) + 3v(s0+s1) - q E U0³ + p E U1³.
```

Its increase is at least (3r-d)s. The upper Taylor bound for(1+s/v)^(3/2)
gives precisely `s(K0-K1*s)`, and the guard at U/N is strictly positive.
Thus rho-rho_B is favorable on every row. This is not extrapolated below
p=1/3; an exact p=.26 law in the independent checker reverses that assertion.

The error quadratics have nonnegative coefficients and positive second
derivative. W'' is the displayed negative completed square. Consequently
both comparison polynomials are concave on the whole real line, and their
four positive endpoint margins prove the entire closed noise interval.
No probability or phase grid is needed.

## Compact acquisition interface and unresolved joins

The acquisition theorem supplies strict p in(.375,.465), amplitude<.6,
inward sum<.004, lambda<.35 and raw|H|<=1.83605680. Weakening these to the
Compact row's closed domain is valid. Its normalization is exactly
`lambda=n theta/ell²=n E U²`, and the standardized marginal is the original
X pointwise. There is no change from the raw threshold H to H/sqrt(n).

Therefore the Compact row excludes every such acquired witness with
`.01<=lambda<.35` at n>=700. The noise interval is not all positive noise.
A separately proved common small-noise result is required on
`0<lambda<=.01`, and zero noise needs the strict Bernoulli theorem directly.
At lambda=.01 the closed theorems may overlap; they need not choose the same
integer anchor because their conclusions concern the same signed excess.

On the baseline route, the Right row's new lower endpoint.03 joins the old
all-phase v11 .03 theorem, avoiding the v12 outer and291-cell negative-inner
components for this right local union. The new Compact row is stronger for
an acquired n700 witness. Whether it removes every older small-noise component
from the *selected* complete route depends on acceptance of the separate
common small-noise theorem; this review does not assume that unfinished edge.

Acquisition itself still retains its stated contact, predecessor, coarse
Fourier and raw-threshold conditions. Reflection chooses an oriented positive
witness and must reacquire its signed budget. Neither this comparison nor the
acquired n700 exclusion establishes BASE41, a base through699, or an
unconditional large-n cutoff in the presence of a possible earlier failure.

## Finding and disposition

No formula, theorem-domain, or checker-coverage defect was found. One comment
in the actual-law checker originally said that the odd five-fold symmetric
noise has a zero atom at t=2. Its frozen four-fold noise does, while the
five-fold conditional law has the tested atoms at t=2±e. The constructor corrected the comment in commit
`6777b645fd24cd87fae49ba3d7e2e6a152afff4a`. The assertions and tested events were already
correct; this is an evidence-description correction, not a theorem repair.

Fresh evidence is under `runs/unified-review-v16-20261029/`. It contains source
pins, commands, exact outputs, stderr, interpreter and return code. The independent
checks preserve closed events and the whole curvature tail. The numerical
controls supplement the analytic derivation, not replace its continuous-domain
or same-law hypotheses.

Final accepted constructor pins:

- Proof: `2be0dc58973a281accb66cf3c8dffd7209592e68278ef4c0c46805708e374938`.
- Generic checker: `0f834fd4b7cf146e7eff1b0eb4fab35737f643fcf15251675b1b6f6dc25ee492`.
- Actual controls: `73c2a62c116234b7dfaeeec14217e315809d00556f5076e8f3898ebe097e4755`.

`check02` binds these final bytes. `check01` preserves the earlier comment-only
version of the actual controls; the mathematical proof/checker are unchanged.
Replay: `python3 mathematics/simplification-v16/2026-10-29/unified-review-check.py PATH_TO_UNIFIED_CONSTRUCTOR`.
