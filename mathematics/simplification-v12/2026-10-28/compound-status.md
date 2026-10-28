# Compound comparison, 28 October 2026

## Exact result and separate evidence columns

The new theorem proves `Delta_C < 0` for actual iid conditional-noise laws with
`n >= 42`, `p in [2/5,53/100]`, `U0 in [-3/5,a0]`,
`U1 in [-a1,3/5]`, conditional means zero, `a0+a1 <= 9/125`,
`|H| <= 46/25`, `C >= 2/5`, `lambda=ns in [3/100,3/40]`, and
negative phase `u=-r in [-3/20,0]`. This is a new scoped theorem; the stronger
v11 result `Delta_C < -lambda/100` for `lambda <= .03` is unchanged.

| Result | Mathematical status | Execution status |
|---|---|---|
| Quadratic-hinge Poisson comparison for centered independent upper-bounded summands and variance upper bound | External theorem: Pinelis 0902.4058, Proposition 2.8 / Corollary 2.11 | Primary source independently inspected by coordinator/reviewer; no rerun can prove this theorem |
| Two-group comparison; centered hinge increases with total variance and decreases with small-jump allocation | Locally derived analytic proof, independently reviewed comparator component `da19d3c` | Independent pgf recurrence / direction / collision controls in separate review branch |
| Complete two-Poisson quadratic hinge | Exact lower-complement identity, rational exponential enclosure | Fresh PASS: 72 moment cases, 11 malformed/warm-cache controls, `evaluator02` |
| Physical count transport and same-law cubic/own-count join | Locally derived; full composition review in progress | Fresh closed acceptance PASS, but arithmetic is not a substitute for its premises |
| Uniform negative-inner comparison | Locally derived computer-assisted candidate pending final independent composition review | Fresh PASS: 291 closed cells, 480 common-refinement elementary cells, 23 rational gates, 8 mutation controls, `accept01` |
| Seven-page proof note | Full analytic and computational derivation supplied | TeX Live compile PASS; all seven page renders inspected, no layout warnings |
| Other phases or global conjecture | Not established by this component | Separate outer-phase and acquisition results required |

The exact accepted margin is at least `256695813/10^12 > 0` on every cell.
The 291 cells consist of 200 quartic cells and 91 Cantelli cells. Each quartic
cell checks 256 finite endpoint combinations and five degree-four Bernstein
coefficients per combination. Sample size is reduced analytically through
`eta=1/n in [0,1/42]`; it is never sampled.

## Sources and dependency graph

All paths here are relative to this worktree.

- `mathematics/simplification-v12/2026-10-28/compound-proof.tex:20` states the theorem and exact hypotheses.
- `compound-proof.tex:50` proves the count identity and finite normalization.
- `compound-proof.tex:142` gives groupwise Poisson comparison, monotonicity and the first incoming bound.
- `compound-proof.tex:208` proves the finite complement and the rational exponential enclosure; no tail truncation occurs.
- `compound-proof.tex:231` bounds every later incoming count, including the entire infinite remainder.
- `compound-proof.tex:260` combines physical cubic moments with outgoing moments before support endpointing.
- `compound-proof.tex:329` proves all endpoint and Bernstein reductions, including continuous closed coverage.
- `compound-proof.tex:404` records scope and the two refuted shortcuts.
- `compound-accept.py:30` validates exact coverage and schema; `:68` checks normal gates; `:102` computes rigorous tails; `:122` checks quartics; `:142` checks Cantelli; `:150` exercises malformed objects.
- `compound-evaluator.py:20` encloses exponentials; `:42` evaluates the complete lower-complement identity; `:82` uses centered monotonicity; `:104` bounds the entire later-count tail.
- The retained finite Stirling proof is `manuscript/arxiv-v1/appendices/count-comparison.tex`, paragraph beginning “For completeness, the finite Stirling formula used here is”. The present note derives every new numerical application.

DAG:

1. Conditional strip + centering -> fixed signs for cubic expansion, bounded moments, two different upper jump caps for incoming variables.
2. Physical allocation `w=p*v1/s` + actual count -> `T0=(1-delta/(nq))*lambda*(1-w)` and `T1=(1+delta/(np))*lambda*w`.
3. Negative phase + `|xi|<.924<1` -> every incoming `delta+i>0` -> negative group shrinks and positive group grows.
4. Pinelis quadratic-hinge theorem + monotonicity lemma + finite complement -> whole-cell first incoming bound.
5. Same theorem + factorial moments + global variance `<=2.5*lambda` -> two later bounds and complete remainder.
6. Finite Stirling + exact binomial ratios + normal derivative -> mass, ratio, phase and normal repair bounds.
7. Same conditional third moments + raw positive cubic difference -> valid `K0` multiplier replacement -> joint convex support prices.
8. Own-count quartic + items 2, 5, 6, 7 -> separate concavity endpoints and degree-four phase polynomial.
9. Rational certificate with complete coverage -> `Delta_C<0` on the stated region.

The new result permits removal of half-amplitude confinement, marked crossings
and count curvature **only for this acquired region**. To remove the entire
selected right-panel low-noise branch, join this result to the separately
proved positive and outer-negative phase comparisons and the previous
`lambda <= .03` theorem. No dependency is removed in larger noise, other
probability panels, or acquisition lemmas. Existing sources/certificates have
not been edited or deleted.

## Fresh reproduction

From the worktree root:

```
python3 mathematics/simplification-v12/2026-10-28/compound-evaluator-check.py
python3 mathematics/simplification-v12/2026-10-28/compound-accept.py
```

Evidence: `runs/compound-v12-20261028/evaluator02/` and `accept01/`, with
stdout, stderr, return codes, Python version and input hashes. Acceptance took
73.06715075 seconds on the recorded Python 3.9.6 run. The trusted acceptance
stack is Python integers/Fraction, the displayed rational enclosure proof,
and the source-bound programs. No floating optimization or cached bytecode
is loaded by acceptance. The evaluator source bytes are SHA-pinned before
`compile`/`exec` in an isolated namespace.

Build and visual evidence: `runs/compound-v12-20261028/build01/`, including
seven PNG page renders, the PDF, compiler log and hash receipt.

Core pins:

- Proof: `5b9d8428b6aa10bc3fff44114cd26c482b88692f76dd624b841c79d5b4a753fa`.
- Acceptance: `f98de164169fae176644737b8b68b72044837db2a19dbba26602cea279c3d611`.
- Evaluator: `f23d657e0bc10b1d3334feeb65ccd43dd2d8b415e4a26fb0e6f7c3ddc853e582`.
- Certificate: `e3baf63f96f5f7fd6e7f9c6dae1e75448f9f588524e164fdf8c0b2e770ea6a0c`.

## Preserved failures and limitations

The floating discovery scripts are explicitly outside the acceptance DAG.
The first pilot did not close all tested boxes with a quartic-only bound;
Cantelli was then retained as an alternative on larger negative phases.
`plan01` tested only 294 cheap discovery boxes (288 initial and six children
from three splits) and proposed 291 leaves. No dense generation campaign was
run. The exact checker reconstructed all final inequalities independently of
those floating values.

Two earlier shortcuts are refuted, not adopted:

1. Reusing physical allocation as own-count allocation violates an actual
   centered two-group law at n=42, p=.5, k=22, r=.08, jumps -.6/.001 and
   their reflection, by exact margin `423903/2500000000` in the proposed
   fourth-moment bound. The accepted proof retains both count multipliers.
2. Centered compound-Poisson hinge convexity in allocation is false at
   T=1/40, w=1/4, y=1/5. The accepted proof uses the independently proved
   monotonicity direction, then freezes the incoming bound on each box.

The reviewer preserves their independent exact derivations and additional
actual-law controls. Neither defect affects the previously accepted .02/.03
proofs, which did not use the shortcuts.

## Next action

Complete the independent whole-comparison review, then integrate this local
component with the coordinator's outer-phase proof and actual-law event
controls. The coordinator must record the exact union and acquisition
hypotheses. No manuscript changes, pushes, merges or old certificate deletion
are part of this component.
