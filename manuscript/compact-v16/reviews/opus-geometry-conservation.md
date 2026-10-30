# Geometry and conservation revisions: decisions and evidence

Reviewed the external plan as proposed advice, against the current manuscript and its actual hypotheses. Scope: `sections/05-geometry-counts.tex`, `sections/03-conservation.tex`, and `sections/07-direct-acquisition.tex`. This report records the component before the coordinator's final notation and integration edits.

## Accepted changes

1. **One exact normalization.** The sign decomposition now introduces `s=E U²` before use and collects the pointwise formula for `X`, conditional centering, variance decomposition, and `v+s=ell^{-2}` in one standard `subequations` group. The original labels `ms:bernoulli-coordinates`, `revision:canonical-decomposition`, and `short:acq:normalization` are retained as the group label and two row labels. The acquisition conclusion refers to this block. Ordinary labels following an equation do not reliably refer to that equation; a minimal compilation test confirmed they instead receive the section number. No amsmath internal-label workaround remains.

2. **Stable geometric notation.** Central-gap endpoints are `(-A_-,A_+)`, conditional mean magnitudes are `bar A_-`, `bar A_+`, and their inward displacements are `Delta_-`, `Delta_+`. The probability polynomial remains `mathcal Q`; its acquisition-section duplicate definition is removed. This is a local notation change, with the original identities and zero-atom assignment retained.

3. **The lattice consequence (`opus:lattice-gap`).** A new corollary explains what `J` means for a lattice law and derives `J>=h` and `|gamma|+3h <= (3+sqrt(10))rho`. Equality in the second inequality is precisely the extremal Bernoulli law and its reflection. If successive support points are all separated by `h`, then `J=h`. The corollary does not assert equality for every law of maximal lattice span `h`.

4. **An accessible finite-n identity (`opus:excess-identity`).** The conservation equation is solved for the excess:

   `a=[R_c-n C_E rho(1-e)-n phi(0)e D/6-n^(3/2)L]/(n+H²)`.

   The preceding table identifies the distinct terms. The proof has four numbered stages, preserving the identities and symbol scope rather than creating four artificial lemmas. Leakage `L>=0` follows directly from a positive measure and nonnegative gap weights; it does not use a predecessor estimate.

5. **Quantified consequences, with scope.** For a contact pair at `C_E` with `a>=0`, `n>=N>=2`, `R_c<=T`, and `|H|<=H_0`, the text gives

   `D <= 6 T exp(H_0²/(2N))/(n phi(0))`.

   This follows from dropping the other nonnegative terms and using `e>=exp(-H_0²/(2N))`. The fixed-target coarse localization theorem supplies uniform `T,H_0` under its stated hypotheses. No unqualified `R_c=O(1)` or unspecified metric of proximity to a Bernoulli law is claimed.

6. **Readable acquisition sequence.** Five stages explain the progression from a central gap to probability bounds, inward displacements, the final noise bound, remaining moment bounds, and total count variance. The existing variance-weighted-measure form of the joint budget is retained and explicitly identified with the earlier inequality. It is useful for the kernel argument and preserves its label. The text explains why a bound for `theta` alone does not control `lambda=n theta/ell²`, and why the one-sided cubic bound and AM–GM supply the required linear cost.

7. **Endpoint and ray provenance.** The ray step states its contact/predecessor assumptions explicitly and distinguishes differentiation of the actual heat function from evaluating its majorant at the two boundaries. Local ray auxiliaries now avoid collisions with earlier `h` and leakage `L`. No certificate assumptions change.

## Independent mathematical derivations

### Lattice support, including infinite support

A lattice support is contained in a translate of `h Z`, hence is closed, discrete, and has Lebesgue measure zero. Each bounded complementary interval `g` between successive support points has length `k_g h`, `k_g` a positive integer. The zero-bias density is constant there, with value `tau_g`, and vanishes outside the convex hull of the support. Thus nonnegative integration gives

`sum_g tau_g k_g h = integral tau = 1`,

`J=sum_g tau_g k_g² h² >= h sum_g tau_g k_g h = h`.

This argument applies to one-sided or two-sided unbounded supports: the bounded gaps are countable, and their nonnegative integrals increase to the full integral. The existing gap inequality gives finiteness of `J`. Its terms show that `J` is a weighted average of the gap lengths, with weights `tau_g |g|` summing to one. Reflection replaces `tau(t)` by `tau(-t)` almost everywhere, preserves `rho,J,h`, and negates `gamma`. Apply the existing sharp gap lemma to the orientation with nonnegative third moment. Equality in the lattice inequality forces equality in the sharp gap inequality, hence the extremal Bernoulli law; conversely its two-point support has one gap of length `h`, so it attains equality.

### The discarded displacement terms

The step improving `theta` has a positive displacement cost and a signed noise correction. They may be discarded together because their combined coefficient is `6w(1-d)-theta b_pm`, positive throughout the already-established domain. An exact lower margin is

`2939585167017/500000000000 > 0`.

Discarding the negative correction by itself would be invalid. The revised prose makes the combined operation explicit.

### Remainder order and predecessor use

The contact identity first needs an independent ceiling on `R_c`. That gives positivity of `M_c`, then a lower bound on `e`; only afterward may the nonnegative threshold cost be subtracted to bound `U`. The resulting ceiling on `U` is not a new ceiling on `R_c`. A predecessor theorem is used to bound contact support, enabling the moment/Fourier bounds which supply the ceiling. Neither `L>=0` nor the algebraic identity requires it.

## Suggestions corrected or declined

- The joint defect budget is a **lower bound by a sum of costs**, not an exact decomposition of `D` into those costs.
- The sample-size floor `700` gives `B_*/700<.047` in acquisition, but the count comparison also uses `n>=700` in its error estimates. Its role is not limited to the first inequality.
- The plan's claim that several acquisition margins are all about one percent is inaccurate. The preliminary probability-bound squared test has a substantially larger relative margin. Exact margins are saved as diagnostics; no misleading numerical summary was added.
- No fixed-law limit is substituted for the uniform contact estimates, no law-distance conclusion is asserted without a metric, and no speculative certificate-free proof replaces the current hypotheses.
- A bulky duplicated step table and wholesale global notation renames were not adopted. Numbered proof stages and purpose statements retain the necessary mathematical detail.

## Evidence and limits

Evidence directory: `/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/manuscript_opus_20261030/geometry/`.

| Item | Mathematical status | Execution status |
|---|---|---|
| Lattice corollary | Locally derived as above from the existing sharp gap lemma | Seven exact diagnostic lattice examples freshly pass |
| Solved conservation identity and conditional defect bound | Exact rearrangement and positivity argument | Twelve rational algebra tuples freshly pass; these are diagnostics, not extremizers |
| Six acquisition numerical comparisons | Existing targets, checked with exact fractions | Fresh PASS in `notes.stdout.json` |
| Retained geometry constants | Existing exact arithmetic checks, targets unchanged | Fresh PASS in `retained-geometry.stdout.json` |
| Three changed sections | Component LaTeX structure and rendering | Three fresh pdfLaTeX passes; no overfull, undefined-reference, or multiply-defined-label warnings |

The diagnostic includes symmetric and skew Bernoulli laws, a zero atom, nearby three-point laws, a tiny far atom, and lattice support with holes. Uniform mass on `{-2,-1,1,2}` has raw variance `5/2`, maximal raw span `1`, and raw gap functional `4`; the positive difference `4-5/2` rejects the false identity `J=h` for every lattice law. Finite examples do not prove the continuous or unbounded-support statements; the analytic derivations above do.

`receipt.json` records source hashes, commands, return codes, runtime version, and output hashes. `compile-source03/main.pdf` is the final component build: HEAD baseline plus the three edited files, with the guide's duplicate label removed only in that scratch copy. Earlier failed label experiments are retained separately and are not claimed as acceptance evidence. Rendered pages 7–19, containing the edited normalization, lattice corollary, conservation proof/table, acquisition steps and contact rays, were visually inspected in `sheet-07.png`, `sheet-11.png`, `sheet-15.png`, and `sheet-19.png`; no collisions or truncation were visible. This does not replace the coordinator's final integrated compilation and page inspection.

The independent count agent found one inherited wording issue: the phrase “before bounding these two cubics” precedes an expression that already uses their lower bounds. The coordinator was asked to change it to “with these two cubic bounds inserted”. No mathematical defect was found in that independent geometry review. No finite-base result, numerical induction threshold, or full conjecture is claimed here.
