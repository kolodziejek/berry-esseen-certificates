This PR retains the manuscript and the acquisition, scalar and executable audits, and adds shorter analytic replacements for several count-comparison regions. The latest **v14** result is a complete local comparison for all laws in the stated right strip at **n>=6000**, together with an all-n theorem for independent Bernoulli noise and a new left-side exclusion. **The full sharp iid Berry–Esseen conjecture remains open.**

## Main advance: the weighted comparison closes at large indices

For one actual iid marginal, use the conditional Bernoulli coordinates
`Y=B+U`, `E(U|B)=0`, `v=p(1-p)`, `s=E U²`, and `lambda=ns`.
The new theorem assumes:

- n>=6000 and p in[.4,.53];
- `-.6<=U0<=a0`, `-a1<=U1<=.6`, and `d=a0+a1<=min(.072,3/n)`;
- `.075<=lambda<=.36` and raw `|H|<=1.84`.

It proves the complete direct comparison `Delta_C<-lambda/200` for every C>=0, with Delta defined precisely in the theorem. The actual-gap budget `nD<=129/4` supplies `nd<3` for an acquired witness. The previous v12 comparison covers the remaining positive noise below .075; zero noise is Bernoulli.

The proof uses the v13 exact crossing identity, an elementary characteristic-function bound, transport from the selected count to a fixed count, a window of21 counts and a complete fourth-moment tail. Finite Stirling restores the binomial weights. Explicit phase, variance and cubic repairs then close the estimate. There is no new parameter grid, Poisson-tail certificate, local-limit approximation or expensive generation campaign.

Read **mathematics/simplification-v14/2026-10-28/large-index.pdf**: five pages, including the precise acquisition join. This is a local theorem under stated premises, **not an unconditional numerical cutoff for the conjecture**.

## Other v14 results

- **All-n independent-noise theorem.** If B is Bernoulli(p), p in[1/4,3/4], and U is independent, centered and supported on an interval of width<=1/5, the sharp absolute Berry–Esseen bound holds at every n and threshold, with margin `3s/(1000v^(3/2))`. Conditioning applies Schulz's binomial theorem; a finite Taylor replacement is paid for by the increase in the third absolute moment. No bound on ns or acquisition premise is needed. The proof is three pages in `loss-closure.pdf`. Equal conditional noise laws give this subclass; unequal laws cannot simply be pooled.
- **Whole left-region exclusion.** Under the stated acquired left-strip/budget premises, p in[1/3,.4] and `nQ(p)/sqrt(pq)>=24` imply signed excess `<-1/(10n)`, for every phase and admissible noise. The four-page `geometry-slack.pdf` uses a new summable curvature bound and the reserve in Schulz's middle-p theorem. Combined with the earlier result below1/3, an acquired contrary witness with p<=.4 must have n<=2681. The quantitative binomial reserve is not extrapolated below1/3.
- **Two central asymmetric families.** A paired crossing-kernel identity gives complete comparisons through lambda=.36 for two conditional two-point families, n>=42, np integer and H=0. `counts-pair.pdf` is four pages. It also proves selected-bias caps under explicit support-width hypotheses. It does not cover general phases or general noise laws.

These results remove count/Poisson computations **only in their proved domains**. The larger-noise right proof still uses the analytic crossing and signed-curvature lemmas. Existing certificates are preserved; no theorem has been weakened.

## Checks actually performed and independent review

**Fresh integrated suite: nine bounded jobs, all PASS**, with pinned sources, commands, Python version, stdout/stderr and return codes in `runs/simplification-v14-20261028/integration01/receipt.json`.

- Large-index constructor:39 exact scalar gates and4 rejecting controls. Independent analytic review rederives transport, characteristic gain, phase/cubic repairs and the actual-gap join;40 independent gates and150 exact small product-space controls pass, including atoms and nonzero selected means. These are internal-lemma controls, not n=6000 convolution coverage.
- A separate count-window review derives a different uniform finite-Stirling mass estimate, the complete discarded tail and the terminal margin. It adds27 exact binomial checks and genuine false-window/false-variance controls. Missing and modified proof sources are rejected.
- Left region:28 constructor gates,5 integer-index comparisons,216 actual-law curvature controls and15 outward-rational full signed events, including exact threshold atoms and neighboring thresholds. Its normal-enclosure helper is explicitly reused and pinned. Independent review reconstructs the analytic bounds and works in Q(sqrt(10)) for the index cutoffs:2638 checks,72 physical curvature cases and4 rejecting controls pass without constructor imports.
- Independent-noise theorem:507 checks,40 moment cases,120 direct-product/conditional-mixture identities,156 outward-rational CDF events and6 rejecting controls. The coordinator independently derived the analytic argument and checked the primary binomial theorem's scope.
- Paired family theorem:16 algebraic gates,28 actual laws,68 paired identities,2304 hinge points,6 direct-product bias controls and3 negative controls. The coordinator independently checked the proof, including closed incoming collisions and the discontinuity at zero noise.
- A separate52-law/8978-event floating diagnostic is retained as **discovery only**. It is not coverage or an acceptance premise.
- All five proof notes compile; rendered pages were inspected:5,3,4,4 pages for the selected components and3 for the optional common-noise note. These are component lengths, not a claimed complete-paper length.
- All2748 original baseline entries are preserved:182 materialized byte checks and2566 sparse tree/index bindings. All85 tracked manuscript files remain unchanged. No full Fourier replay, Lean build or expensive certificate generation was performed this round.

Independent reviews found no remaining blocker **within these scopes**. The coordinator read each accepted proof and reconciled its hypotheses. Agent agreement and hashes are not treated as mathematical proofs. Development failures and false intermediate claims remain recorded.

## Remaining obligations and merge recommendation

The general unequal-noise intermediate range42<=n<6000 remains open beyond the retained small-noise comparisons and newly excluded regions. Independent C4/BASE41, the retained11264-cell coarse Fourier entry, and the relevant attainment/contact/acquisition/sharp-predecessor hypotheses remain. Reflected discrepancies retain their own acquisition and atom conventions. No count result on(.53,.54] is added.

**Keep this PR draft for author review.** The scoped research package has passed its internal independent reviews, but it should not be merged or described as a completed proof of the sharp conjecture. Human review of the analytic reductions and unresolved premises is still needed. No merge is requested or performed.

## Reading and reproduction

Start with `mathematics/simplification-v14/2026-10-28/README.md`, which explains the proof and lists exact computation-removal scopes.

- `large-index.tex`, `loss-closure.tex`, `geometry-slack.tex`, `counts-pair.tex`: full proofs.
- `large-index-independent-review.md`, `counts-window-review.md`, `geometry-slack-review.md`, `coordinator-review.md`: independent derivations and source bindings.
- `reviewed-sources.json` and `run_checks.py`: bounded reproduction.
- `state/`: current status, dependency graph, next experiments and failed shortcuts; previous state is preserved in snapshots.

```sh
python3 -I -B mathematics/simplification-v14/2026-10-28/run_checks.py NEWID
```

## Earlier results retained in this PR

The89-page manuscript remains at `manuscript/arxiv-v1/main.pdf`, with authors Bartosz Kołodziejek and Kacper Rodziewicz, no affiliations/emails/ORCIDs, and explicit AI-assistance disclosure. It has not been rewritten to incorporate this research round.

The earlier acquisition, scalar and executable audits remain, including the four-pass coarse entry, same-law geometric budget, scalar cosine replacements and finite-base witness localization. The original cached-bytecode/source-binding defect and repaired acceptance workflow remain documented. Localization does not prove the finite base.

The retained v12 comparisons concern n>=42, raw |H|<=1.84 and centered conditional noise from one actual marginal:

| Region | p | Outer amplitude | Inward sum | Positive lambda | Conclusion |
|---|---|---|---|---|---|
| Left | [.25,.4] | .7 | <=.068 | <=.01 | Delta_C<-lambda/100, C in[.4095,.41] |
| Right | [.4,.53] | .6 | <=.072 | <=.075 | Delta_C<0, C>=.4 |

The right result includes291 independently reconstructed closed rational cells; earlier smaller-domain quantitative comparisons remain unchanged. The v13 geometric budget gives lambda<.36 globally and<.32 on the left, while its exact crossing identity is an ancestor of the new work. V13 also retains the exact n4 moment-endpoint counterexample and the conditional contact/collision reduction. See the v12 and v13 README files and their integrated14-check and11-check receipts for full evidence and prior limitations.

Work is confined to **kolodziejek/berry-esseen-certificates**. Baseline6346fc1b4432bc5982822aa696eb566ed9e1e1ee is preserved. No main push, force-push, branch deletion, merge or upstream modification.
