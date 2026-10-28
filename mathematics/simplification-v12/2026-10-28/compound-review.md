# Independent review: two-jump Poisson comparison

The groupwise quadratic-Poisson comparison, exact finite complement and
variance/allocation monotonicity are valid under the hypotheses in
`compound-review.tex`. The old common-allocation own-count shortcut is false
for an actual admissible four-point law. Convexity in the allocation is also
false, even at a positive hinge anchor. Neither failure propagates to the
accepted `.002`/`.03` theorems or the local variance-aware moment lemma.
This review does not establish a new complete noise interval.

Worktree: `compound-review-v12`; branch
`research/compound-review-v12-20261028`; baseline
`a69dda8e8ca78c01ed5fe2a7bdf1a4dd1149dfe1`. Only new source and evidence are
added. The manuscript, reference/history, old certificates and remote branches
are unchanged.

| Result | Mathematical status | Execution status |
|---|---|---|
| Pinelis quadratic-hinge comparison with variance upper bound | External theorem; original Proposition 2.8/Corollary 2.11 checked directly | Primary PDF read, including function class and inequality direction |
| Two independent groups with different jump caps, translated hinges, closed event | Derived from the external theorem by conditioning twice; no moment-class enlargement | 16 exact actual conditional convolution controls PASS |
| Physical allocation transported across counts | Exact identity | 387 legal-count identities PASS |
| Old common-fraction own-count substitute | Refuted on an actual four-point marginal | Exact positive failure gap `423903/2500000000` |
| Corrected cubic endpoint prices using physical multipliers | Locally derived; full cubic bracket must be nonnegative before reducing its coefficient | 36 integrated moment/price controls PASS |
| Centered hinge increases with total variance and decreases with small-jump allocation | Proved by binomial approximation, uniform fourth-moment bound, convolution and Jensen | 36 strict outward-enclosed monotonicity controls PASS |
| Convexity of centered hinge in allocation | Refuted; no endpoint reduction follows from that claim | Exact negative second derivative at positive anchor `.2` |
| Complete lattice hinge from finite lower complement | Exact identity, including all upper tail and collisions | 328 independently reconstructed pgf coefficients PASS |
| Infinite incoming factorial tail starting at index at least 2 | Locally derived; constant total-variance upper bound and geometric ratio required | 160 controls PASS; false index-1 version rejected |
| A full closed-domain larger-noise count comparison | Not claimed by this component | Not run |

The final saved independent arithmetic run is
`runs/compound-review-v12-20261028/check03/receipt.json`. It records the exact
source hashes, interpreter, command, return code and stdout. The final proof
build is `build03`; all five rendered pages were inspected, with no warnings,
overfull boxes, or clipped displays. Earlier builds and checks remain separate.

## Dependency findings

1. **The two jump sizes need no extra probability theorem.**
   `compound-review.tex:40` conditions on the other group, applies the
   translated quadratic-hinge comparison, integrates, and repeats. The
   published premise permits separate variance upper bounds. Zero variances
   are deterministic and are handled without division. The incoming lower
   tail applies this to `-U0` and `-U1`, with upper caps `.6` and `.072`.
   The inward cap cannot replace `.6` for the first group.
2. **The physical allocation must be retained in the own count.**
   `compound-review.tex:68` gives
   `T0_i=lambda(1-w)(1-(delta+i)/(nq))` and
   `T1_i=lambda*w(1+(delta+i)/(np))`, where `w=p*v1/s`.
   The old discovery file uses a common inflated variance fraction for its
   incoming bounds at lines 36–38; that is a valid envelope. Its lines
   51–57 combine common own-count fractions with the marginal cubic repair,
   which does not represent the same law. The exact counterexample starts at
   `compound-review.tex:96`. It has `n=42,p=.5,k=22,lambda=.0252`, inward
   sum `.002`, and raw threshold below `1.84`.
3. **There is a genuine monotonic simplification, but no convexity shortcut.**
   `compound-review.tex:170` proves that, at fixed total variance, replacing
   small-jump variance by large-jump variance increases every quadratic
   hinge. The binomial approximants have fourth moments at most
   `d^2 V+3V^2`, so the limit is justified for these unbounded hinges.
   Valid group inflations with `omega1>=omega0` produce a comparator whose
   small-jump allocation is at least the physical `w`. Thus a rectangle can
   use its variance upper endpoint and allocation lower endpoint.
   `compound-review.tex:217` proves that convexity nevertheless fails at
   `T=.025,w=.25,y=.2`. Taking a pointwise minimum over hinge or tilt choices
   also supplies no missing convexity argument.
4. **A finite complement eliminates upper-tail truncation.**
   `compound-review.tex:240` uses
   `E(S-K)_+^2=E(S-K)^2-E(K-S)_+^2`, where
   `S=25Pois(mu)+3Pois(nu)`. The second term is a finite sum. The independent
   checker uses the pgf recurrence `j*c_j=25mu*c_(j-25)+3nu*c_(j-3)`;
   it does not import or execute the constructor. A lower enclosure for
   `exp(-mu-nu)` is needed when subtracting that sum.
5. **The remaining count tail need not inflate variance linearly with i.**
   `compound-review.tex:278` uses `Var(W_j)<=2.5lambda` for every legal
   count. The factorial/geometric continuation is valid from index 2.
   The false index-1 inequality fails at Poisson count 3 (`4>3`).

## Constructor inspection

The evaluator `compound-evaluator.py` in the separate `compound-v12`
worktree was read directly. The finite double sum, rational anchor, positive
exponential remainder, fixed-uncentered-anchor box bound, centered monotone
bound and factorial tail agree with the derivations here. At the inspected
bytes its SHA256 is
`f23d657e0bc10b1d3334feeb65ccd43dd2d8b415e4a26fb0e6f7c3ddc853e582`.
This is a source inspection, not an independent rerun of its implementation
and not a review of an unprovided continuous cover.

The initial cache decoration could bypass malformed-type checks after a
numerically equal exact argument had warmed the cache. The constructor was
notified and now uses `typed=True`; its regression file includes warm-cache
float and boolean controls. This defect affected the fail-closed interface
claim, not the already exact rational calculations. Subsequent constructor
edits or covers require their own source binding and review.

## Reproduction and limits

Run the independent checker from any integrated checkout containing these
files:

```sh
python3 -I -B mathematics/simplification-v12/2026-10-28/compound-review-check.py REPO_ROOT
```

To save a fresh receipt, use `compound-review-run.py NEW_RUN_ID`; existing
run directories are refused. The checker uses rational arithmetic and no
constructor import. Its small actual-law controls are adversarial checks,
not a proof by sampling. Its first development invocation exposed an
integer-zero division producing floating zero in the recurrence; the code
was corrected to divide Fractions, and all saved acceptance checks are exact.

The source theorem is [Pinelis, *On the Bennett–Hoeffding inequality*,
Proposition 2.8 and Corollary 2.11, printed p.9](https://arxiv.org/pdf/0902.4058).
The application retains independence, centering, genuine one-sided caps,
variance upper bounds, strict hinge admissibility and the same physical
marginal across counts. Global acquisition, raw-threshold entry, finite base,
and the remaining count ranges are separate obligations.
