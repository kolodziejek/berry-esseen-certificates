# Analytic replacement of the right small-noise certificate

Baseline: `fb9e918bef3b0a932fb44bf1dae8d3e4a589f932`. Branch: `research/counts-v16-20261029`. All outputs are new; no existing proof, manuscript or certificate was edited. The result is a replacement sufficient for the latest right local union, not a reproof of the old n>=42 anchor theorem at its entire scope.

| Result | Mathematical status | Execution status |
|---|---|---|
| Full positive signed excess <−lambda/100, n>=200, p∈[.4,.53], lambda∈[.03,.36], amplitude .6, inward sum .072, raw abs(H)<=1.84 | Locally derived from the retained crossing, five-count and summable-curvature lemmas; coordinator/independent review pending | 30 exact scalar gates, four endpoints and coefficientwise global concavity PASS |
| Full right union for 0<lambda<=.36 | New theorem plus the existing v11 all-phase comparison at lambda<=.03 and Schulz's theorem | Exact endpoint/phase join checks PASS; no new acquisition claim |
| Compound-Poisson subtree unnecessary in this selected n>=200 union | Dependency removal proved by the overlapping new domain | No certificate generation or 291-cell replay needed |
| Original n>=42, C>=.4 anchor comparison | Preserved; not replaced at n42..199 | Not rerun |
| Acquired n>=700 union, global finite base, reflection and eventual cutoff | Existing conditional composition remains separate; no new unrestricted cutoff | Not claimed by this component |

## The new inequality

The v15 sufficient negative-sign polynomial used `sqrt(lambda)<=lambda+1/4`. At lambda=.03 and n=200 its exact residual is negative. Replace it by

`sqrt(lambda) <= (5/3)lambda + 3/20`,

which is exactly `(sqrt(lambda)-3/10)^2>=0`. Since `T=(100/47)lambda`, this gives

`sqrt(T) <= J(lambda)=(5/2)lambda+9/40`.

Every other v15 right constant stays fixed. The gain W is the same quartic. The new errors E− and E+ are convex quadratics, with E+ unchanged. With `P±=W−E±/200−lambda/100`,

`W''=−(13/50){z²[(z lambda−1)²+1]/4+3b²/8}<0`,

so four exact endpoints prove the whole interval. The margins exceed .000461, .000885, .004654 and .011247 respectively. This is neither sampled positivity nor a new parameter cover.

The theorem uses the full signed excess, not Delta relative to the old chosen integer anchor. This distinction is necessary and sufficient: the latest union needs the full excess, and the strict binomial theorem bounds both interpolation anchors. The v11 small-noise comparison may retain a different shifted anchor. At lambda=0 use the strict binomial theorem directly. At positive noise the entire right union now retains the margin −lambda/100.

## Retained source locations and hypotheses

All paths below are repository-relative; all sources are byte-pinned in `counts-check.py`.

- `mathematics/simplification-v13/2026-10-28/crossing.tex:112`: weighted crossing identity. Requires separated centered conditional supports and interior raw crossing; bounded support supplies finite moments. The new theorem checks the interior inequalities explicitly.
- `mathematics/simplification-v15/2026-10-28/loss-direct.tex:35`: five-count reserve. Sections starting at lines 68,114,166 prove the smooth minorant, four centered swaps, physical variance, Fourier reserve and complete omitted-translate tail. None requires lambda>=.075.
- `mathematics/simplification-v14/2026-10-28/geometry-slack.tex:78`: summable-curvature lemma. The actual conditional variance is bounded only on increasing binomial weights; here T=lambda/q<=100lambda/47. Its c<=1 premise is satisfied by c<.46.
- `mathematics/simplification-v15/2026-10-28/right-direct.tex`: Section 1 gives the five binomial masses; Section 2 gives the right mode coefficient, signed normal interpolation and cubic sign. These bounds require lambda<=.36 and n>=200, not the old lower noise endpoint.
- `mathematics/simplification-v11/2026-10-28/counts-v11.tex:11`: all-phase comparison for n>=42, C>=.4, 0<lambda<=.03 with the same right strip and raw threshold. Its phase interval has length one. This still uses a scalar one-jump Poisson bound; the present removal does not eliminate every Poisson theorem from the whole proof.
- Schulz, *The optimal Berry–Esseen constant in the binomial case*, Theorem 1, printed p.1: strict binomial bound for all p and n. Source already independently verified in the v15 review: https://d-nb.info/1197702695/34.

## Exact removed edges

`mathematics/simplification-v15/2026-10-28/join-review.md:39` previously used three constituents below .075: v11 through .03; v12 outer on the outer/positive phases; v12 compound on negative inner phases. Replace that phase split by v11 through .03 and the new all-phase theorem from .03. The shared boundary is closed.

Consequently the selected n>=200 right union no longer depends on:

- `mathematics/simplification-v12/2026-10-28/compound-proof.tex`, its first theorem and Sections 2–4;
- `compound-certificate.json` and its 291 closed boxes/480 elementary coverage cells;
- `compound-accept.py`, `compound-evaluator.py`, the two-jump quadratic-hinge comparison, its physical-allocation endpoint relaxation and complete compound-Poisson tails;
- `mathematics/simplification-v12/2026-10-28/outer.tex`, the complementary phase theorem.

The n>=700 acquired-witness route uses only n>=200 for the right local row, so it inherits this removal without a change of its index qualification. No claim is made that these ancestors are unnecessary for retained statements below n=200 or for any other branch. Their bytes and historical acceptance evidence are preserved.

The left branch, coarse 11264-cell Fourier entry, actual-gap geometry, support acquisition, raw-threshold export, attainment/reflection, sharp predecessor and genuine finite base remain outside this component. In particular the simplification does not turn the conditional n>=700 statement into an unconditional cutoff.

## Reproduction and adversarial tests

Run `python3 -I -B mathematics/simplification-v16/2026-10-29/counts-run.py NEWID` with a fresh alphanumeric ID. The runner records source bytes/hashes, interpreter, exact commands, return codes, stdout/stderr and elapsed times. Acceptance uses `Fraction` and imports no constructor program. All retained source hashes are validated before checking the scalar formulas. Five changed-source variants and one missing-source variant reject through the actual validator.

`counts-actual.py` checks five actual iid laws at n200/201 with exact rational marginal moments and complete sum distributions. It checks 45 raw-threshold events, including 15 exact atoms and the two neighboring sides; nine events lie in the old negative-inner interval. Laws include one rare noisy conditional, common symmetric four-point noise with exact collisions, and unequal four-point noise. Full CDF normal enclosures reuse the disclosed source-pinned v10 kernel; this is regression evidence, not independent verification or domain coverage.

Three exact negative controls show the limits of the sufficient polynomials: the old tangent fails at .03/n200; the new polynomial fails at zero noise; a more aggressive tangent at sqrt(lambda)=1/4 fails at the upper endpoint .36. None is claimed as a counterexample to Berry–Esseen.

Fresh `check01` passed: scalar 0.061 seconds, actual-law checks 10.431 seconds. Final source differs from its snapshot only by a paragraph-layout wrapper; final replay is in `check02`. The initial build's two overfull path lines are preserved in `build01`; `build02` compiles cleanly to four pages. All four rendered pages were visually inspected: equations, theorem domain, endpoint table and dependency paths are readable and within margins. No manuscript file was compiled or changed.

The current proof source is `counts-analytic.tex`, SHA-256 `b6aabeb75a3c9bbcc28beb4e6bc8b259ba2ff5aee793877fbb5b92dfbc94cb5f`.
