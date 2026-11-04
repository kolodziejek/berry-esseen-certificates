# Two acquired rows: a complete small-noise joint-count comparison

Mathematical status: a locally derived implication under the existing acquired
same-law hypotheses. Execution status: exact polynomial acceptance and
adversarial controls passed; full source-bound captures accompany this file.
No acquisition, integral, all-index theorem or whole-count LOW calculation is
newly accepted by this pilot.

The analytic premises include the actual signed score **`C≥2/5`**,
`Y=B+U`, `B~Bernoulli(p)`, `E(U|B)=0`, `|U_j|≤17/40`,
`U_0≤a0`, `U_1≥−a1`, `a0,a1≥0`, and `a0+a1≤181/10000`, together
with the acquired signed threshold, variance and finite-binomial conditions.
The constants in the repair use this score premise; checking a numerical
row does not establish it. Every sum and every count uses these same two
conditional laws. The result is an implication for laws satisfying all
these hypotheses, as the existing application requires.

The native central input is `conditional_input47.json`, index10,
`p∈[2/5,201/500]`. The native left input is
`left270_input47_table.json`, index28, `p∈[9/25,181/500]`.
`SELECTED_INPUTS.json` preserves both complete unchanged rows. Their acquired
supports, signed threshold bounds, moment bounds and shared resources remain
premises. The new proof uses a subset of them; it never selects a different
optimizer for a different count. Both rows lie inside the unchanged
`tiny47wide_normalization.py` contract.

For every integer `n≥47`, every `0<λ≤1/20` and every closed phase
`−1/2≤u≤1/2`, the new four polynomial witnesses give exactly the original
target `ρ_B(C−C_B)<−λ/1000`. They include both signs of the acquired threshold
`H`. Zero noise remains the separate Bernoulli case.

## The joint probabilistic improvement

Use the actual independent conditional variables and the monotone process
`j+W_j`, with every increment at least `c=1−d0`. Write `R` for its last
threshold count relative to `k`. The exact CDF identity is
`Q/π_k=E G(R)`. The established legal binomial ratios obey
`π_(k+i)/π_k≤R0`. Thus

`G(R)≤−1{W_k>u}+R0 R_+`.

If `R=i≥1`, then `W_k≤u−ci`. On the full phase interval,
`i/(ci−u)^4` decreases for `i≥1`, because its derivative has the sign
`−3ci−u<0`. Therefore, pathwise,

`R_+≤W_k^4/(c−u)^4`.

This single inequality bounds **all incoming counts using the same `W_k`**.
For `t=E W_k²`, independence and bounded summands imply
`E W_k^4≤A²t+3t²`; hence the entire incoming charge is at most
`R0 t(A²+3t)/(c−u)^4`. No exponential tail series or relative-tail
monotonicity is used. The strict outgoing event and closed incoming event
are preserved at atoms. The independent analytic derivation is in
`../analytic/EXPECTATION_RULE.md`.

Keep the original quartic
`h_a(w)=(-w⁴+3a²w²+2a³w)/(K a⁴)≤1{w>0}`,
with `a=.4784`, `K=9/(4*.4641)`. For `r=|u|`, its outgoing-plus-normal
lower bound is

`O=[(3a²−A²)t−3t²−4Art−6r²t−r⁴+3a²r²+2σa³r]/(K a⁴)+b r`,

where `(σ,b)=(1,−hf)` for `u=−r` and `(-1,lf)` for `u=r`.
The other two valid bounds are `r²/(t+r²)−hf r` at negative phase and
`lf r` at positive phase.

## Four closed domains, one fixed target

Set `T=(21681/20000)/20`, `η=1/10`, `z_−=5/3`, `z_+=6/5`.
The original normalizer gives `0<t≤T` and `t≥(18319/20000)λ`.

| Branch | Domain | Witness |
|---|---|---|
| Negative near | `r=z t`, `0≤z≤5/3` | shifted quartic |
| Negative far | `(5/3)t≤r≤1/2` | Cantelli |
| Positive near | `r=z t`, `0≤z≤6/5` | shifted quartic |
| Positive far | `(6/5)t≤r≤1/2` | nonnegative outgoing probability |

Each branch proves
`O−R0 t(A²+3t)/(c−u)^4≥η t`.
For the near branches, divide by `t>0` and clear `(c−u)^4`.
For the far negative branch also clear `t+r²>0`.
Use `t=T x`, `z=z_± y` in the near branches and
`r=z_±t+(1/2−z_±t)y` in the far branches.
All four domains are complete unit squares, and `z_±T<1/2`.
The resulting explicit polynomial expressions are independently derived in
`model.targets`; no candidate-supplied polynomial or target is trusted.

The four Bernstein coefficient arrays have dimensions `8×9`, `8×8`,
`8×9`, and `6×6`: **244 exact coefficients**, all nonnegative.
No subdivision was necessary. Acceptance expands their Bernstein basis
back into power coefficients and checks equality to the derived target.
The proposed coefficients were computed by the different forward transform.
The zero coefficients in the two far arrays are harmless: `t=0` is only the
closed polynomial boundary, never a point where a zero denominator is divided.

The unchanged normalizer gives `m=1421/2000`, `κ=59489/25000`, `N=47`.
Consequently the reserve beyond the original strict target is exactly

`m η (18319/20000)−κ/47−1/1000 = 252847053/18800000000 > 0`.

## What is replaced, and what remains

On these two complete TINY domains, one fourth-moment count bound replaces
the first incoming Poisson estimate, the infinite Bennett geometric tail,
their exponential/logarithmic arithmetic and both noise-relative
monotonicity arguments. Four polynomial checks replace the six incoming-tail
phase branches. The outgoing quartic/Cantelli/normal ingredients, finite
binomial normalization and signed cubic repair remain visible and unchanged.

This does not yet remove the common tail lemma from the full paper: MID and
LOW still use it. No page saving or full cover simplification is claimed
until those dependencies are addressed and a complete replacement is measured.

## Reproduction

From this directory, using an unused capture path:

```
python3 -I -B accept.py proof_objects.json
python3 -I -B controls.py /tmp/joint-count-controls-new
python3 -I -B capture.py /tmp/joint-count-capture-new
```

The standard library suffices. Never use `-O` or `-OO`. Discovery is separate;
its floating grid is explicitly not an acceptance criterion. The original
native tables and normalizer are byte-pinned, and every malformed, missing,
reordered or corrupted object is rejected by the fixed acceptance interface.
