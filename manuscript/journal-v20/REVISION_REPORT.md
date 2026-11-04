# Revision report: a genuine moment reduction, no page saving

The old small-noise comparison treated the own-count loss and infinitely many
incoming tails separately. It needed Poisson/Bennett estimates and a proof
that the tail bounds divided by noise were monotone down to zero.

The new proof uses the actual monotone coupling of all conditional sums.
If its count increments are at least `c>1/2`, its last threshold count `R`
satisfies

`G(R) <= -1{W_k>u} + R0 R_+`, with `R_+ <= W_k^4/(c-u)^4`.

The strict outgoing event is preserved, including at atoms. Independence and
centering give `E W_k^4<=A^2 t+3t^2`, with `t=E W_k^2`. Combining this with
the existing quartic, Cantelli and zero lower bounds gives four exact
polynomial tests. Scaled near-phase coordinates preserve a bound relative
to arbitrarily small positive noise. Zero noise remains Bernoulli.

## Implemented manuscript changes

Sections 1 and 4 explain the new idea, construction and acceptance. Section 7.5
proves the coupled-count bound and the four complete polynomial domains,
replacing the old relative-tail argument. The coupling is now proved once
and reused by the whole-count comparison. The uniform parameter example
gives the exact strict reserve. The finite applications retain their actual
index ranges, score caps, row ceilings, positive allowance and binomial reserve.
Section 6's cover descriptions now identify the replacement correctly.

For a possibly negative intermediate loss `eta`, the correct coefficient is
`min(m*eta*omega_minus,eta*omega_plus)`. In the finite family, 244 rows use
`eta=.1`, 12 use zero, and 11 use `eta=-.05`. The latter two groups are in
the left40–42 family and consume part of its already accepted binomial reserve.
They do not weaken the final target. The positive39 normalizer retains its
conservative noise ceiling `.05` even when a row's actual ceiling is smaller.

The new objects replace every retained small-noise application identified in
this part of the manuscript: 83 uniform and 267 finite rows. Larger-noise
MID/LOW comparisons, their common tail lemma, marked-deletion argument,
harmonic estimate and signed corrections remain necessary.

## Scope and execution evidence

| Result | Mathematical status | Fresh execution |
|---|---|---|
| Coupled-count fourth-moment rule | Locally derived and independently reviewed under actual same-law support/centering | Exact joint-path, atom, expectation and false-variant controls |
| Uniform small noise | Original strict target on all 83 acquired rows, every n>=47, full phase and 0<lambda<=min(.05,row cap) | Four polynomial identities, 244 nonnegative Bernstein coefficients, 41 normalization gates and full input census |
| Finite small noise | Original targets on all 267 rows at 39, 40–42 and 42–48; original allowances/reserves retained | 65,148 coefficients, 17,115 original normalization gates, full input joins and corruption/sign controls |
| Independent finite review | Separate derivation/source review; no new acquisition or binomial-reserve proof | 12,816 direct formula comparisons across every row and loss sign; 11 corruption/sign controls |
| Optional intermediate-noise comparison | Conditional alternative on uniform `[.05,.08]`, outside the required proof graph | 200 phase cells, 2,200 global polynomial targets, 4,243 Bernstein leaves, 21,215 coefficients; both rays and 71 nonempty / 12 empty row domains checked |
| Complete manuscript | Same overall proof-candidate scope as v19, with the new local replacement | 100-page build, no overfull equations or unresolved references; separate visual reviews |

Primary bounded reviews and their fresh process records are in
`review/joint-count/`. The numerical packages include portable acceptance
and corruption controls. The unchanged upstream arithmetic is inherited from
the completed selected v17 campaign. Exact arithmetic, independent formula
checks and software execution are different evidence from a human review of
the whole mathematical argument.

## Preserved failures and limitations

The same four explicit small-noise witnesses fail on larger proposed noise
ceilings `.06` and `.08`, even after the normalization is correctly enlarged.
Exact negative rational values are retained. These refute those sufficient
witnesses, not the probability theorem. The optional direct staircase
quartics use a different witness and do pass `.05`–`.08`.

The first floating staircase discovery also produced a polynomial that failed
on the far-left ray. Exact acceptance rejected it. The revised construction
was accepted only after complete rational checks of both infinite rays and
every finite interval. Optimizer success and sampled margins were not used
as a proof.

The measured PDF grew from **98 to 100 pages**. No essential analytic text was
moved to an uncounted supplement, and no typography was compressed to claim
a saving. The simpler expectation argument is useful for understanding and
further research, but it does not meet the approximately 60-page objective.
The next experiment must remove a larger dependency, preferably by proving
a comparison on coarser acquired supports that also avoids confinement.
Its precise scope and stop rules are in [SIMPLIFICATION_NEXT.md](SIMPLIFICATION_NEXT.md).
