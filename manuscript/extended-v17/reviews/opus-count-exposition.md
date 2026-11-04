# Count-comparison revision review

Date: 2026-10-30. Source reviewed: the external `manuscript_revision_plan(1).md`, chiefly P§3.8, A5–A7, P§6 item 13, and the corresponding notation/prose proposals. Its suggestions were treated as proposals, not as verified instructions.

## Scope and status

Only `sections/08-direct-comparison.tex` was edited in this subtask. The statement of its principal theorem is byte-for-byte unchanged from the starting source. Every one of the 22 original labels remains; four new lemma labels were added. No support, probability, threshold, sample-size, or noise-variance domain was enlarged. The complete incoming tails, strict losses, closed gains, shared endpoint at `lambda=1/100`, and the zero-noise case remain.

| Item | Mathematical status | Execution status |
|---|---|---|
| Existing count-comparison proof and its old scalar constants | Supplied proof retained; locally reviewed while reorganizing | Existing exact count checker freshly passed |
| Added zero-threshold moment explanation | Locally derived below; valid for any centered nonzero finite-fourth-moment variable | Exact coefficient calculation plus five atomic-law diagnostics passed |
| Added sine-average explanation | Exact trigonometric identity and modulus inequality | Source/typesetting checked; no numerical approximation needed |
| Small-noise final margin | Exact rational identity | Fresh `Fraction` check passed |
| New theorem/lemma organization and notation | No change to claims or hypotheses | Old labels checked, theorem statement byte comparison passed |
| Full manuscript, external Schulz theorem, and global theorem dependencies | Outside this subtask; no promotion of conditional results | Parent/external audit required |

An arithmetic PASS checks the stated scalar obligations. It does not independently prove the analytic reduction, every inequality in the count argument, or the global theorem.

## Changes accepted

1. **P§3.8(a): explicit conditioning and strategy.** The section now defines `K`, the conditional count noise `W_j`, and the threshold `t=np+H sqrt(v+s)` before the estimates. It explains the comparison with the binomial CDF, outgoing losses, all incoming gains, normal correction, and third-moment correction. The two noise regimes have distinct error structures, so their division is mathematically motivated.
2. **P§3.8(b): selected lemma boundaries.** Four substantive interfaces are now named: loss at a nearby count threshold; nonnegative crossing kernel; five-count crossing loss; variation of binomial weights. The old crossing identity lemma remains. Splitting every normalization/table/normal correction into a separate lemma would interrupt a single calculation without adding useful interfaces, so the proposed nine-lemma fragmentation was not adopted.
3. **P§3.8(c), A6: explain the quartic.** A Cauchy–Schwarz/Hölder bound now shows why variance produces a linear crossing loss. The quartic remains necessary for shifted thresholds and the normal increment. Its global validity is explicit; the count sum may exceed the bound on each summand.
4. **P§3.8(c): explain the sine bump.** The phase-uniform expectation identity is displayed before the five-count lemma. The proof then separately handles centered replacements, omitted translates, and the characteristic-function estimate. Neighboring count sums share unchanged variables; only the summands within each sum are independent.
5. **P§3.8(f): exact atom convention.** The text derives strict losses and closed gains directly from the closed event, preserving threshold atoms.
6. **P§3.8(d), P§6 item 13: useful local renamings.** Binomial masses are `b_j`, ratio bounds are `r_max`, normal increments are `g_k`, the small cutoff is `lambda_s`, and the comparison floor is `n_0=700`. Positive-part expectations and their Jensen gaps are `mathcal L_j` and `mathcal B_j`, avoiding collisions with `B`. The kernel/loss is `chi,chi_i`, the bump is `psi`, the fixed variance is `sigma_V^2`, and the lower-loss/final polynomials are `mathcal W,Pi`. The variance-floor constant is `c_var`; the second use of alpha and z was removed in favor of `kappa_0`. Numerical pi and the correction `mathcal R` retain distinct meanings.
7. **P§7–8: local prose.** Exact purpose statements replace vague reserve terminology. The final paragraph explains why rational endpoints plus concavity cover the full interval and why the tail bounds include all entering counts.

The small-noise anchor is still an integer with `u in [-3/10,7/10]`, explicitly not necessarily the floor. The larger-noise anchor is the floor with `u in [0,1)`. The source does not conflate these phase conventions.

## Corrections and suggestions not adopted

- The proposed sentence “`W_k` is not bounded, although its summands are” is false for this finite sum. It is bounded by `nA`, but generally not by `A=3/5`. The revised sentence says exactly that the sum can exceed the bound on a summand.
- The proposal that every small-noise error is `O(lambda/n)` or `O(lambda^2)` is too strong: the bound for the entire incoming tail is linear in `lambda`. The revised overview says that loss and errors are proportional to `lambda`, which is what the proof needs and proves.
- The quartic was not described as simply giving a “better constant” than the orientation inequality: `3/5` after accounting for phase displacement and the normal increment is not numerically larger than `2500/3903`. It proves the stronger shifted assertion.
- A generic moment-problem citation was not inserted merely to brand an elementary, explicitly factored minorant as conventional. The factorization and expectation calculation suffice here.
- The brief self-contained Stirling remainder proof was retained. Robbins' bound is a possible bibliographic addition after external verification, but replacing these few lines adds a dependency without materially clarifying this section.
- Remaining proposed symbol changes were not applied mechanically. Scoped constants that have no live collision in this section were retained, and the principal theorem's notation and statement were preserved.
- A second schematic was not added: the exact conditioning identity, explicit crossing interpretation, and four lemma interfaces carry the local explanation; the parent revision supplies a global dependency figure.
- The proposed non-strict-Schulz robustness remark was not inserted, for the reason and conditional derivation below.

## Derivations added or checked

### Zero-threshold orientation

For centered `W` with `t=E W^2>0` and finite fourth moment, write `m=E|W|`. Centering gives `E W_+=m/2`. Cauchy–Schwarz gives

`m^2/4 = (E W_+)^2 <= P(W>0) E W_+^2 <= P(W>0)t`.

Hölder, applied to `|W|^(2/3)|W|^(4/3)`, gives

`t <= m^(2/3)(E W^4)^(1/3)`.

Consequently `P(W>0) >= t^2/(4 E W^4)`. Independence and centering of summands bounded by `A` give

`E W^4 = sum E Z_i^4 + 6 sum_{i<j} E Z_i^2 E Z_j^2 <= A^2 t + 3t^2`.

Thus `P(W>0) >= t/[4(A^2+3t)]`. With `A=3/5` and `0<t<=101/10000`, its coefficient is at least

`1/[4((3/5)^2+3(101/10000))] = 2500/3903 > 16/25`.

In the small-noise argument `t=t_0>=.99 lambda>0`, so division is justified. This is an explanation only; it does not replace the quartic/Cantelli proof for shifted thresholds.

### Phase-uniform sine average

For any real random variable `V`,

`E sin^2(pi(u-V)) = (1-Re(e^(2pi i u) E e^(-2pi i V)))/2 >= (1-|E e^(2pi i V)|)/2`.

The equality is pointwise trigonometry followed by expectation; the inequality is `Re z<=|z|`. Independence factorizes the characteristic function of the fixed sum. The inherited proof verifies the variance bound for each conditional noise and then pays explicitly for four centered replacements and all omitted translates. No independence between different conditional count sums is used.

### Small-noise final margin

The exact calculation is

`(3/4)(59/100-(51/50)(53/100))-2/700 = 4787/140000 > 1/100`.

The original large-noise endpoint lower bounds are retained. The exact checker independently constructs the rational polynomials and verifies both endpoints, including the final `lambda/100` subtraction. The original complete-series bounds were retained; no incoming-tail truncation or sampled positivity was substituted.

## Conditional non-strict-Schulz variant — not inserted

Suppose only the non-strict signed binomial inequality were available, with the same normalization, domain and closed-CDF convention. Keep all structural, acquisition, finite-condition and finite-base hypotheses used in the original composition argument.

- For `0<lambda<=1/100`, the small-noise calculation proves `Delta_CE<-lambda/100` before invoking the binomial baseline. A nonpositive baseline therefore still gives strictly negative actual excess, with the same displayed noise margin.
- For `1/100<=lambda<=7/20`, the crossing/interpolation estimates give an actual excess at most `-mathcal W(lambda)+E(lambda)/n` if strictness of the baseline is unavailable. Since `Pi=mathcal W-E/n_0-lambda/100>0`, `n>=n_0`, and `E>=0`, this is strictly less than `-lambda/100`.
- At `lambda=0`, the same change gives only nonpositive excess, not the strict zero-noise conclusion of the current count theorem.
- In a proof by a least index with `C_n>CE`, attainment produces a strictly positive excess; nonpositive excess in the zero-noise case still contradicts it, assuming all entry/acquisition/predecessor edges remain available with the stated non-strict hypotheses. This would establish the corresponding non-strict global upper bound, with a separately justified lower bound supplying an equality for the supremum.

This variant does not preserve the current strict count-theorem statement or automatically establish `C_n<CE`. It therefore should not be presented as a drop-in simplification. No version of it is added to the manuscript without reconciling every dependent strict statement and verifying the precise external theorem. The external-source agent/parent owns that decision.

## Fresh evidence and remaining integration

Run directory: `/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/manuscript_opus_20261030/count/`.

Final source SHA-256: `4599414d6435247cc435904d44d5cc96ec0ab91105da0d0344b9013a94972dfa`.

- `check_and_build_delivery.py`: reproducible component check/build wrapper, executed with assertions enabled.
- `explanation-check-final.json`: exact rational coefficient/margin checks, principal theorem byte comparison, all original labels preserved, and five diagnostic atomic laws (symmetric, skew, tiny noise, remote atom, atom at zero). These diagnostics supplement the proof, rather than replace it.
- `count-check-final.stdout.json`: fresh `PASS_REVISION_COUNT_CONSTANTS`; 32 atomic-event diagnostics and eight intentionally corrupted scalar/minorant cases rejected. The original checker was not edited.
- `receipt-final.json`: input/output hashes, commands, return codes, actual timings, and Python version.
- `build04/`: three successful `pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex` passes, nine component pages, no overfull boxes. All nine rendered pages were visually inspected in three contact sheets; equations and lemma boundaries fit.
- The isolated wrapper omits the bibliography, so its one Schulz citation remains unresolved by design. Its benign epstopdf shell-escape warning is also retained. The parent must compile the integrated manuscript to resolve bibliography and global numbering.
- `build01/` preserves an initial wrapper working-directory failure; `build02/` preserves the first successful compile with a one-point overflow; `build03/` and `build04/` preserve subsequent corrected stages. No failed record was presented as a successful run.

No commit, publication, or edit to immutable reference/history files was made by this subtask.
