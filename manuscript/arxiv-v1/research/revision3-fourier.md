# Fourier appendix revision, third editorial round

Base: `6299d97`, branch `manuscript/v3-fourier-20261027`. Only the Fourier
appendix, this note and bounded check/build evidence are added or edited.
The supplied revision document was assessed as a proposal. Its assertions
that particular proofs were identical were checked against the sources;
they were not used as mathematical authority.

## Status

| Item | Mathematical status | Execution status |
|---|---|---|
| Duplicate-proof substitutions below | Hypothesis and notation matches checked against the cited main-text arguments; specialized statements and their conditions retained | Source/label preservation check passed |
| Directed rational comparisons for pi | Exact rational comparisons proved by cross multiplication; the analytic enclosure uses the retained Machin identity and alternating remainder proof | Fresh standard-library Fraction check passed |
| Scalar cosine Bernstein condition | Still an explicit finite certificate premise | Embedded program moved below, not executed |
| Unique Fourier, moment, confinement and marked-count arguments | Retained supplied proof material; this editorial task does not reverify the whole chain | No inherited certificate driver or generation campaign run |
| TeX source | One top-level Fourier appendix; all 193 previous labels retained | Local full TeXLive build passed; final shared ordering and heading style remain the coordinator's integration |

## Proof replacement ledger

Line locations in the first column refer to the base `6299d97` version of
`manuscript/arxiv-v1/appendices/fourier-analysis.tex`. The cited labels
identify the exact destination arguments independently of later line moves.

| Source | Replacement and hypothesis match | Material retained |
|---|---|---|
| 546–572, embedded Python | Move the literal program out of the mathematical article; the formulas `afcore:eq:bernstein-data` and `afcore:eq:bernstein-min` already specify the same 1,134 rational numbers and conditional minimum | Complete coefficient formula, grid including the last nonuniform interval, closed-cell Bernstein identity, and explicit certificate premise |
| 628–643, profile proof's Machin argument | Cite `ms:gaussian-constants` for `25/8 < pi < 22/7`; these are weaker than the rational bounds in that lemma's proof | Convexity, monotonicity, exact endpoint join and the rational trigonometric comparison remain in full |
| 786–801, repeated constants argument | Cite the same lemma for `phi(0)` and `C_E`; explicitly retain a rational comparison proving `pi > 333/106` | The longer A32/A10 alternating-sum recipe is retained and now explicitly bounds pi between 3.141592653589793 and 3.141592653589794. A bare citation to the shorter Gaussian bounds would be insufficient for the later directed coefficients |
| 1562–1619, central-gap decomposition and joint inequality proofs | Cite `ms:physical-defect`, `ms:defect-decomposition`, `ms:simultaneous-gap`, and `ms:simultaneous-gap-formula`. The law is compactly supported and standardized; its actual central endpoints, conditional means, signed variances, sigma=sqrt(10), and physical D are identical | Both labeled displayed formulas, the central-gap criterion, and all auxiliary consequences used later; the unique interval updates and weighted exports remain in full |
| 1676–1715, weighted joint-resource theorem proof | Apply `ms:joint-resource` with exactly n>=N>0, nD<=N d_D, theta<=Theta<1, pq<=v_*, positive S_* and K, and the same lower binary charge b | Full specialized theorem statement, negative/zero/positive residual cases, band restriction, outward intercept rounding, and weighted premise |
| 2399–2409, closed-box Bernstein proof | Cite the tensor Bernstein identity in `ms:certificates`, after affine maps from both closed intervals; coordinate degree four is stated | Old `re-bernstein` label, all 25 central-rectangle coefficient formulas, sign-aware multiplication by m endpoints, and convexity proof |
| 2799–2859 and first two proof lines after 2901, signed resource part (i) | Cite `ms:joint-resource` with its floor chosen as the **actual index n** and d_D=D_*. This is necessary because the appendix only assumes D<=D_*, rather than the floor-weighted premise | The affine formula is still derived from theta=lambda(1-theta)/(npq); all three coefficients, zero cases, intercepts, and full unique parts (ii) and (iii) remain |
| 3259–3288, antichain proof | Cite the random-chain proof in `ms:uniform-bridge`. Its combinatorial argument is independent of floor42 and applies to independent Bernoulli labels with increments at least c and diameter strictly below c | General strict-gap concentration lemma, independent-shift clause, actual conditional coupling, strict-diameter counterexample, and the complete separate floor47/J0=45 rational mode bound |
| 3596–3684, exact local identity and witness proof | Cite `ms:master-identity`, `ms:count-difference`, and `ms:local-witnesses` with V_j=W_j and m_0=m. The appendix requires legal interior k, same conditional laws/phase, lambda>0, B<0 and I>=0. Thus the main max(0,I)/N is exactly I/N here | Full definitions, support conditions, strict outgoing/closed incoming count formula, every original label, both explicit strict tests, and the specialized theorem statement |
| 3962–4001, cutoff/curvature/crossing proof | Cite `ms:whole-count-cutoff` through `ms:counts` and `ms:crossing-curvature`, using V_j=W_j, A_U=A, chi<2, zero extension, and abs(u)<=1/2. The acquired d<=d0 makes c=1-d0 a valid increment lower bound; the proof uses only that bound and 1/2<c<=1 | Coupling and cutoff definitions, all three displayed labeled formulas, and the full marked-crossing, deletion, tail, fractional-part and final scalar estimates that follow |
| 4184–4195, zero-noise threshold argument | Cite `ms:counts`: conditional centering and lambda=0 force both noises to vanish, then positive attained closed-CDF maximum occurs at an atom | Endpoint u=0, equality C=C_B, external Schulz theorem premise, and the full remaining local-composition conditions |

The proof substitutions are narrower than the proposal's claim of verbatim
duplication. In particular, the antichain index-specific mode estimate,
unweighted-to-weighted specialization at the actual index, all auxiliary
joint-resource updates, and the numerical strict tests are retained.

## Structure, notation and presentation

The appendix now has one top-level section, `ms:fourier:appendix`; the
previous three sections are subsections, and deeper headings are demoted
one level. The coordinator will place this as Appendix A and give fourth-level
paragraph headings block formatting. New descriptive lemma labels are
`ms:fourier:laguerre` and `ms:fourier:window50`.

Raw source-comment headers are removed. Lemma titles and narrative replace
ROOT4, HIGH_LAGUERRE2, HIGH_WINDOW50, LOW/HIGH and TINY/MID identifiers with
mathematical descriptions. Implementation directions become hypotheses or
explicit operations without changing numerical choices. Expectations and
probabilities use the article's E and Pp macros. The symbol E denoting a
confinement scale or an event is deliberately not changed into an expectation.
No certificate coefficients, source archives or theorem targets are edited.

## Checks and limits

`runs/manuscript-fourier-v3-20261027/check01/check.py` checks all old labels,
absence of duplicate labels, the single top-level appendix and the continued
conditional cosine premise. It also compares 13 unique proof bodies with
the base, allowing only whitespace and the stated expectation/probability
notation changes. These include the complete signed Gaussian transfer,
the exact Gaussian-tail formula (not merely its upper bound), finite-window
transfer, and shifted-quartic/Poisson-tail proofs. The coefficient and
marked-crossing arguments outside the listed substitutions remain in the
article. A separate exact Fraction calculation verifies both coarse and
fine directed pi comparisons.

The result is `PASS_EDITORIAL_PRESERVATION_AND_DIRECTED_PI`, Python 3.9.6,
return code 0, with empty stderr. Negative controls detect a missing label,
a duplicate label, an incorrectly directed pi endpoint and a changed
Gaussian-transfer coefficient. The receipt records relative commands and
input SHA-256 hashes. This is a bounded editorial/rational check, not
acceptance of the old Bernstein programs or full proof chain.

The local full build used TeXLive via latexmk, produced 162 pages and had
no undefined references/citations or overfull boxes. It reported one mild
underfull box at the run-in heading “One budget, two error bounds”; the
coordinator's global block-heading format addresses the relevant layout.
Build receipt and source/PDF hashes are in `build01/receipt.json` and
`build01/validation.json`. The final coordinated version, with the new
appendix order and other agents' edits, still requires its own build.
Visual inspection at 100 dpi covered local PDF pages 49, 63, 68, 71,
93 and 95, including the new heading hierarchy, deduplicated geometry,
retained Gaussian-tail proof and the local comparison. No clipping,
overlaps or equation-number collisions were found. Page 93 illustrates
the run-in heading spacing that the shared block format will improve.

## Removed embedded program: preserved, not run

The following literal program is moved from the base appendix for
reproducibility. Its presence in this note is not a fresh execution or
an assertion that its coefficient claim is accepted.

```python
from fractions import Fraction as F
from math import comb, factorial
q = [F(0) for j in range(14)]
q[0] = F(62, 625)
for j in range(2, 9):
    q[2*j-3] = F((-1)**(j+1), factorial(2*j))
lower = F(2479189, 65585520000)
minimum = None
for r in range(81):
    a, b = ((F(r,16), F(r+1,16)) if r < 80
            else (F(5), F(625,124)))
    c = [sum(q[l]*comb(l,j)*a**(l-j)*(b-a)**j
             for l in range(j,14)) for j in range(14)]
    for k in range(14):
        value = sum(c[j]*F(comb(k,j),comb(13,j))
                    for j in range(k+1))
        assert value >= lower
        minimum = value if minimum is None else min(minimum,value)
assert minimum == lower
```
