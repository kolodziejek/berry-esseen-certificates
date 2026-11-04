# Independent review of the count exposition

Reviewed the current `sections/08-direct-comparison.tex` and its diff against HEAD, deriving the new explanatory inequalities directly before consulting the constructor's report. No TeX was changed during this review. Scope is the newly exposed four lemmas, the new zero-threshold orientation estimate, the phase-uniform sine explanation, notation, and preservation of the existing formulas and atom conventions; it is not a new proof of the external finite-binomial theorem.

## Outcome

The mathematical changes reviewed are valid under the displayed common-strip hypotheses. The four lemma statements retain the former proof's actual assumptions, formulas, and numerical constants. No new theorem gap was found. One new roadmap sentence called the small-noise anchor the “nearest” count; the allowed phase interval `[-3/10,7/10]` does not require that. The coordinator changed it to “one nearby count”. A resulting minor “the a count” typo in the opening paragraph was also reported for removal.

## Independent derivations

### Zero-threshold orientation estimate

For a centered nonzero-variance random variable `W` with variance `t`, centering gives `E W_+=E|W|/2`. Cauchy–Schwarz gives

`(E W_+)² <= P(W>0) E(W_+)² <= P(W>0)t`.

Hölder applied to `|W|²=|W|^(2/3)|W|^(4/3)` gives

`t <= (E|W|)^(2/3)(E W^4)^(1/3)`.

Combining gives `P(W>0)>=t²/(4 E W^4)`. The small-noise hypotheses guarantee `t=t_0>0`. Independence, centering and bounded summands give `E W^4<=A²t+3t²`. Since `A=3/5` and `t<=101/10000`, the coefficient exceeds `16/25`; its exact smallest margin is `52/97575>0`. The event is strictly positive, so an atom at zero is handled correctly. The paragraph is explicitly explanatory and does not replace the subsequent shifted-threshold argument.

### Nearby-count lemma

The quartic remains a global minorant of `1_(0,infinity)`, with value zero at zero; it is not applied only on the range of an individual summand. The previously established fourth and third moment bounds apply to the whole conditional sum. Exposing the conclusion as a lemma does not change the rectangle, switch, derivative signs, or Cantelli cases. At `u<0`, Cantelli is applied to the closed failure event `W<=-r`, so the resulting bound is for the required strict outgoing event `W>-r`. The endpoint `u=0` and the phase switch remain included.

### Kernel and phase-uniform sine loss

For `x<1-a_1`, the second positive part and closed CDF term vanish, so `chi(x)=E(x-U_0)_+>=0`. For `x>=1-a_1>a_0`, centering and put–call parity give

`chi(x)=P(1+U_1>x)-E(1+U_1-x)_+`.

Since `x>=1-d>A`, each positive overshoot is less than one; this proves nonnegativity, including collisions at the lower endpoint. The displayed stronger comparison on `[1-a_1,1]` follows from bounding the overshoot by `1+A-x`, Jensen's lower bound `1-x`, and the stated scalar sine inequality. The use of the strict tail in this rewritten expression is forced by the closed CDF in the definition; it has been preserved.

For every real random variable `V`, without any moment assumption,

`E sin²(pi(u-V)) = [1-Re{exp(2pi i u) E exp(-2pi iV)}]/2 >= [1-|E exp(2pi iV)|]/2`.

This proves the asserted uniformity in the phase `u`; no averaging over `u` occurs. The five translated compact bumps have disjoint open supports. Each adjacent pair has a derivative with the same Lipschitz bound `2pi²`, because both derivatives vanish at the joins. The two grouped changes on each side amount to four centered replacements, each costing at most `pi²(s_0+s_1)`. A coupling is needed only for each replacement; the manuscript correctly does not assert independence of the neighboring count sums.

An omitted nonzero translate forces `|V|>2` when `0<=u<1`; equality collisions contribute zero because the bump vanishes at its endpoints. Thus the omitted part is at most `E V^4/16`. The fixed sum has `n-1` independent terms and variance

`sigma_V²=lambda-(delta+1)s_0+delta s_1`.

For `-1-xi<delta<xi`, the negative adjustment is at most `(1+xi)(s_0+s_1)`, and the positive adjustment at most `xi(s_0+s_1)`. Together with `s_0+s_1<=lambda/(nr)`, these imply the retained `1-6/n` and `1+3/n` bounds.

Finally `|Z-Z'|<=A+d<2/3`. The sine chord gives `1-cos(2pi x)>=3x²`, since `2(51/40)²-3=201/800>0`. Hence `1-|E exp(2pi iZ)|²>=6 Var Z`, and `sqrt(1-y)<=exp(-y/2)` gives the factor `exp(-3 Var Z)`. Independence of the fixed sum then proves the retained exponential reserve uniformly in the phase. All arguments cover zero-variance individual conditional laws.

### Variation-of-weights lemma

The Jensen gap has the stated expression in absolute values. Its second-moment bounds follow from `E|W|<=sqrt(T)` and `(x-a)_+<=x²/(4a)` for `a>0`. The factored quartic yields `(x-1)_+<=27x^4/256`, giving the fourth-moment bound on either side of the threshold by centering. Only indices with positive adjacent-mass difference need the hypotheses on `T,M_4`: all others have nonpositive contribution and are discarded. The positive numerator is bounded by `(a+c)_+`. The two near-threshold mesh intervals give the displayed `c sqrt(T)+T/4`; every remaining point is included in the complete inverse-square and inverse-cube sums. Thus splitting this calculation into a lemma did not introduce a truncation or require moment bounds at additional indices.

## Notation and preservation checks

- The main common-strip theorem's interval, sample-size floor, support assumptions, raw threshold, strict `-lambda/100` conclusion, and zero-noise branch are unchanged.
- `b_j` for binomial masses, `g_k` for the normal increment, `r_max` for the incoming mass ratio, `mathcal L_j` for the positive-part expectation, `mathcal B_j` for its Jensen gap, and `chi_i` for crossing losses are consistently substituted in the diff.
- The local constants and polynomial symbols `n_0,c_var,sigma_V²,kappa_0,mathcal W,Pi` are scoped in the larger-noise subsection. No old atom convention or equality was silently changed by the renaming.
- The interpolation identity still uses closed CDFs, while losses from counts below the anchor are strict and gains from counts above it are closed. The characteristic-function explanation and four newly named lemmas preserve these conventions.
- The numerical endpoint checks and final concavity reduction are unchanged except for notation and the exact displayed small-noise margin `4787/140000`.

## Fresh independent diagnostics

Evidence is in `/Users/bkolodziejek/Downloads/BE_Codex_Handoff/runs/manuscript_opus_20261030/geometry/`:

- `check_count_independent.py` independently reconstructs the finite crossing identity by exact rational convolution, rather than calling the existing checker.
- `count-independent.stdout.json` reports 25 exact cases, including zero conditional noises and threshold atoms. Sixteen cases reject the deliberate mutation replacing the kernel's closed CDF by a strict event.
- The same script checks the new orientation margin, the sine-chord scalar margin, and the printed final small-noise rational identity. `count-independent.stderr.txt` is empty; the command `/usr/bin/python3 -I -B .../check_count_independent.py` exited with code 0.
- The isolated summation diagnostics use `n=3`, where exact enumeration is small. They test the algebraic identity with its boundary conditions, **not** the common-strip theorem for `n>=700`. Finite examples do not prove the analytic uniform estimates above.

| Claim | Mathematical status | Execution status |
|---|---|---|
| New orientation inequality | Independently derived under its displayed moment assumptions | Exact scalar margin freshly passes |
| Uniformity in phase and five-count argument | Independently rederived with all support and independence hypotheses | Analytic review; no phase grid claimed |
| Crossing identity and atom conventions | Algebraically rederived | 25 fresh exact diagnostics; 16 strict-event mutants rejected |
| Existing endpoint constants | Preserved by the diff | Coordinator/constructor runs retained checker; not claimed as independent arithmetic verification here |

The diagnostic output records the reviewed manuscript and checker hashes. Final compilation and inspection of the integrated manuscript belong to the coordinator.
