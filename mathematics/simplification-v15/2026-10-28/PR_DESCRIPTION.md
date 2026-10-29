This PR retains the manuscript and the acquisition, scalar and executable audits, and adds shorter analytic replacements for count-comparison arguments. The latest **v15** method uses **five neighboring counts and four centered replacements**. It proves the full signed local comparison on the right from **n=200** and on the left from **n=700**, under the exact support, noise and threshold assumptions below. **The full sharp iid Berry–Esseen conjecture remains open.**

## Latest mathematical advance

For one actual iid marginal, write `Y=B+U`, `E(U|B)=0`, `v=p(1-p)`, `s=EU²`, `lambda=ns`, `X=(Y-p)/sqrt(v+s)` and `rho=E|X|³`. Both new theorems prove

`sqrt(n){P(X1+...+Xn<=H)-Phi(H/sqrt(n))}-C_E rho < -lambda/100`

for every raw `|H|<=1.84`, every phase and all threshold atoms:

| Row | Index | p | Conditional supports | Inward sum | lambda |
|---|---|---|---|---|---|
| Right | n>=200 | [.4,.53] | -.6<=U0<=a0; -a1<=U1<=.6 | a0+a1<=.072 | [.075,.36] |
| Left | n>=700 | [1/3,.4] | -.7<=U0<=a0; -a1<=U1<=.7 | a0+a1<=.068 | [.01,.32] |

The conditional laws are centered and `a0,a1>=0`. Neither new local theorem assumes a geometric budget, contact, a predecessor theorem, or `d<=3/n`. Those premises remain where needed to acquire its hypotheses for an extremal witness.

The exact crossing identity expresses the actual CDF as a linear interpolation of two binomial CDF values, plus signed curvature, minus nonnegative losses. A compact sine-square function lies below the crossing kernel. Grouping its translated supports allows four centered replacements to compare five actual conditional counts, at a variance cost. One fourth moment controls all omitted translates. Finite Stirling supplies the five weights; explicit curvature, signed normal and actual cubic corrections complete the comparison. Two concave quartics reduce each noise interval to four rational endpoints.

This removes the earlier selected-count transport/displacement argument and 21-count window **within these larger-noise domains**, and improves the prior right local threshold from 6000 to 200. The new left comparison uses only Schulz's all-p binomial theorem, without its sharper middle-p reserve. No new parameter grid, count-tail proof object or expensive generation campaign was needed.

The complete new notes are `mathematics/simplification-v15/2026-10-28/loss-direct.pdf`, `right-direct.pdf`, and `geometry-left.pdf`, four pages each. These are component lengths, not a claimed length for the complete paper.

## Domain union and exact limitation

The retained v12 comparisons cover smaller positive noise; zero noise is Bernoulli. The resulting local unions cover `0<=lambda<=.36` on the right at n>=200 and `0<=lambda<=.32` on the left at n>=700. Their integer comparison anchors may differ by noise regime.

The geometric theorem supplies those noise ceilings and excludes p<=1/3 at n>=169. The upper probability end follows either from retained acquisition panels or from the checked geometric exclusion of p>=.53 at n>=106. With all named acquisition premises, no acquired nonnegative signed witness remains at n>=700.

**This is not an unconditional cutoff at 700.** With a genuine BASE41 and the named attainment/reflection/acquisition implications at a least failing index, any first failure must lie in 42,...,699. An unresolved earlier failure can invalidate the sharp-predecessor premise at a later row. A genuine base through 699, or a separate proof covering 42–699, is still needed for that least-failure induction.

`join-review.md` separates the local theorem, conditional acquired-witness theorem and first-failure corollary. It checks the actual marginal normalization, all noise/phase endpoints, the p=.4 seam, both coefficient ranges, and reflected closed-CDF atoms. The reflected law needs its own acquisition; its probability interval is not assumed invariant.

## Counterexample and retained dependencies

`counts-phase.pdf` gives an exact actual-law counterexample to always using floor(t) at tiny noise. At n=42, p=1/2, a rare conditional jump moves a common atom just below 21. The floor anchor 20 gives a positive comparison greater than 1/250, while anchor 21 gives a strict negative comparison. The retained shifted-anchor theorem selects 21 and is unaffected. This is an intermediate-lemma counterexample, not a counterexample to Berry–Esseen. The note also proves an optional first-absolute-moment curvature bound.

Still retained: the v12 **291-cell negative-inner certificate**, the **11264-cell coarse Fourier entry**, actual-gap geometry for noise acquisition, support/contact/attainment/reflection/sharp-predecessor hypotheses, and an independently established finite base. General unequal-noise right indices 42–199 and the surviving left region below 700 remain open beyond the proved small-noise and geometric exclusions. Independent C4/BASE41 is not inferred from historical success headings.

No existing certificate or proof was deleted, and no theorem target was weakened. The previous n1000 transport candidate was left on its separate branch after scalar exploration; it is not an accepted ancestor of the new proof.

## Checks actually performed and review outcome

**Nine bounded integration jobs passed** with the final source versions. Evidence: `runs/simplification-v15-20261028/integration01/receipt.json`, including commands, Python version, source hashes, stdout/stderr and return codes.

- Five-count constructor: **519 exact checks**, 97 actual law/threshold cases and 5 rejecting controls.
- Right constructor: **32 scalar gates**, including all endpoint margins; **45 outward-rational full signed events** from five actual n=200/201 iid laws, with atoms and neighboring thresholds.
- Left constructor: **40 scalar gates**, 35 pointwise kernel controls including 5 collisions, 12 exact product-swap controls, 35 independent streaming-CDF smoke checks, and **12 full signed events** from four actual n=700 iid laws.
- Independent five-count/right review: separately derives the kernel minorant, four replacements, full omitted tail, physical variance, normal signs and cubic correction. It reconstructs both quartics by rational interpolation, verifies the global concavity identity and all four endpoint margins, and uses a separate Machin/Taylor enclosure for **58 kernel and 20 actual swap controls**. Eight actual-law examples refute deleting the replacement cost. Missing and mutated proof sources are rejected.
- The coordinator independently derived the left adaptation and read its exact checker, rather than treating constructor agreement as proof.
- Independent domain review: **240 checks, 28 exact phase/noise strata, 12 actual marginal mappings and 17 rejecting controls**. It distinguishes arithmetic coverage from conditional acquisition.
- Anchor counterexample and optional curvature: exact rational acceptance, including **270 curvature checks on 45 actual cases**. Floating phase diagnostics remain discovery only.
- All four final proof notes compiled and their rendered pages were inspected. Two literal strictness signs at vanishing endpoints were corrected to weak inequalities; no theorem conclusion or numerical constant changed. Initial development failures remain recorded.
- All **2748 original baseline entries** are preserved: 182 materialized byte checks and 2566 sparse tree/index bindings. All **85 tracked manuscript files** remain unchanged. Some outward normal helpers are reused with explicit source pins; that reuse is not described as independent arithmetic verification. No full Fourier replay or Lean build was performed this round.

Independent reviews found **no remaining blocker within these stated scopes**. The coordinator read every accepted proof and reconciled the joins. Hashes establish identity, not correctness; finite actual-law controls supplement the continuum arguments.

## Merge recommendation and reading order

**Keep this PR draft for author review.** The scoped research package has passed its internal independent reviews. I recommend reviewing it as a rigorous, delimited advance, and not merging it as a completed proof of the conjecture. Human review of the analytic reductions and remaining premises is still needed. No merge is requested or performed.

Start with `mathematics/simplification-v15/2026-10-28/README.md`. Full proofs, `coordinator-review.md`, `counts-direct-review.md`, `join-review.md`, source manifests, bounded runners and state files are alongside it.

```sh
python3 -I -B mathematics/simplification-v15/2026-10-28/run_checks.py NEWID
```

## Earlier manuscript and audit work retained

The 89-page manuscript remains at `manuscript/arxiv-v1/main.pdf`, with authors **Bartosz Kołodziejek and Kacper Rodziewicz**, no affiliations/emails/ORCIDs, and explicit AI-assistance disclosure. It has not been rewritten to incorporate this research round.

Earlier acquisition, scalar and executable audits remain, including the four-pass coarse entry, actual-law geometric budget, scalar cosine replacements, finite-base witness localization, and the cached-bytecode/source-binding defect with its repaired workflow. Localization does not establish the finite base. The v12 small-noise proofs and v13 crossing/geometric reductions remain ancestors.

Other retained v14 results include the all-n independent-noise subclass theorem, the left geometric-reserve exclusion, and the two central asymmetric families. They are preserved with their original scopes and evidence; the latest larger-noise route does not require all of them. Prior READMEs and receipts preserve the full audit history.

Work is confined to **kolodziejek/berry-esseen-certificates**. Reference baseline `6346fc1b4432bc5982822aa696eb566ed9e1e1ee` is preserved. No main push, force-push, branch deletion, merge or upstream modification.
