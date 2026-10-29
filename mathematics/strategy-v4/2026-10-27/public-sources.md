# Public proof routes checked on 27 October 2026

This is a source-level comparison, not a fresh Lean build or an audit of every transitive theorem. No public repository was modified.

## Eventual sharpness

The inspected revision of [UCLA-Trustworthy-AI-Lab/BerryEsseenLean](https://github.com/UCLA-Trustworthy-AI-Lab/BerryEsseenLean/tree/2b97fa7400dd85fc98b829224c89b0f986789395) is `2b97fa7400dd85fc98b829224c89b0f986789395`. Read the README, `docs/ASSUMPTIONS.md`, `BerryEsseen/StrictResults.lean`, `GeneralJitterGap.lean` and `ClusterConfinement.lean`.

The actual endpoint `strict_main_theorem` takes six named classical interfaces. The source separately proves its smoothing interface. Its conclusion is eventual sharpness, with an unspecified uniform threshold. The explicit endpoint has different inputs and the very large threshold stated in the README. Neither supplies LOCAL42 or the finite base through 41.

The useful alternative is jitter: sandwich the CDF between shifted smooth approximations, then obtain a local strict gain. `strict_gap_of_jitter_envelopes` requires **uniform** approximation of both envelopes and a positive local gap on every bounded threshold interval. Its elegant final proof does not establish those hypotheses. `extremizer_uniform_two_cluster_confinement` additionally uses attaining ratio maximizers, weak convergence to the Esseen law, vanishing scaled drop, bounded support and vanishing standardized thresholds. A fixed-target maximizer cannot be substituted without a new argument.

## Explicit uniform upper bounds

The inspected revision of [CoolRmal/BerryEsseen](https://github.com/CoolRmal/BerryEsseen/tree/bfb22608ad18b4fa9fda8dd9a1ed2c2b6fbc29e7) is `bfb22608ad18b4fa9fda8dd9a1ed2c2b6fbc29e7`. Read the README and `docs/UPPER_0423.md`. The documented theorem is the universal iid upper bound 0.423, with `native_decide` finite checks and a stated compiler trust boundary. The uniform part reduces frequency integrals using `L=(beta+eta)/sqrt(n)` and `h=1/sqrt(n)`. This suggests parameter reduction, but the finite budgets prove a different constant. They do not certify the Esseen target or its delicate small-noise comparison. The current manuscript already uses stricter acquired bounds in places, so substituting 0.423 throughout would not preserve those arguments.

## Stein-method infrastructure

The inspected revision of [Polarnova/ProbabilityApproximation](https://github.com/Polarnova/ProbabilityApproximation/tree/a2fc5bda874d9b69186c0ba165bf79f3b9897662) is `a2fc5bda874d9b69186c0ba165bf79f3b9897662`. The README describes a nonuniform scalar bound with an unspecified universal constant, plus multivariate approximation. This is relevant infrastructure for leave-one-out concentration and Stein equations, but supplies neither the sharp iid constant nor a defect-relative remainder at that constant. No dependency is removed on this basis.

## The binomial margin

The exact quadratic factorization is rederived in `geometry.tex`. The interval-specific binomial bound is also described in [Mattner--Shevtsova (2019), printed p. 493](https://alea.impa.br/articles/v16/16-19.pdf), citing Schulz's Theorem 1. Attempts to reopen the original dissertation at `https://d-nb.info/1197702695/34` timed out in this round. Accordingly the new note uses the non-strict envelope confirmed by the accessible paper and a **strict** comparison-error bound; it does not depend on the un-rechecked strictness of the stronger envelope. The all-parameter strict Schulz bound already cited in the manuscript is not changed.

No generic Edgeworth theorem, fixed-law asymptotic, or ordinary smooth-metric estimate supplies the near-lattice uniform, arbitrarily-small-defect bound by itself. This is the main obstruction shared by the alternative routes.
