# Independent fixed-target derivation

This derivation uses the definitions of the scores, rather than a success
record or an identity imported from a checking program.

Let `q=1-p`, `v=pq`, `s=q E U0²+p E U1²`, `w=v+s`, `δ=k-np`,
and `πk=P(Bin(n,p)=k)>0`. Use the positive closed event at `k+u` and put

```
F  = P(sum(Y_i) <= k+u),       FB = P(Bin(n,p) <= k),
G  = Phi((δ+u)/sqrt(nw)),      GB = Phi(δ/sqrt(nv)),
C  = sqrt(n)(F-G)/rho,        CB = sqrt(n)(FB-GB)/rhoB,
Q  = F-FB,                   b  = sqrt(n) pi_k.
```

For any **fixed** positive `T`, subtraction, with no inequality, gives

```
rho(T-C)
 = T rho - sqrt(n)(F-G)
 = rhoB(T-CB) + T(rho-rhoB)
   + sqrt(n)(G-GB) - sqrt(n)Q
 = rhoB(T-CB) + T(rho-rhoB) + N - b Q/pi_k.
```

Thus the direct comparison proves `C<T` if a lower bound for the final
right side is strictly positive. It neither requires `rho>=rhoB` nor
permits substituting the unknown attained score `C` for `T` in just one
term. The signed cube bound is multiplied by the actual positive number
`T/w^(3/2)`. If only `chi_lo<=T/w^(3/2)<=chi_hi` is known, checking both
endpoints is valid for either sign of the cube bound. A lower bound
`epsilon+K/n` for `T-CB` similarly uses the lower bound for `rhoB` when
nonnegative and the upper bound when negative.

For positive 39, `K=741/4000`, `n=39`, and
`T=CE+K/39=CE+19/4000`. Both occurrences of `T` are essential. Keeping
`K rhoB/39` in the binary reserve but using only `CE` for a possibly
negative `rho-rhoB` would not prove this identity's lower bound.

The acquired resource already paid the positive `K` charge. Dropping
another negative `K rho` term from a subsequent phase-resource upper
bound enlarges the budget and is safe; it does not turn that ancestor
into a zero-charge acquisition.

## Atoms, phase signs, and zero noise

For the common coupling, successive values `j+W_j` increase by at least
`c>0`. Loss of count `k` occurs exactly at `W_k>u`; incoming count `k+r`
can occur only at `W_k<=u-cr`. Hence

```
Q/pi_k <= E[-1{W_k>u} + R0 max(0,floor((u-W_k)/c))].
```

The outgoing event is strict and the incoming event is closed. At
`W_k=u` no outgoing mass is charged; at `W_k=u-cr` the incoming floor
includes the collision. Both nearest integers at `|u|=1/2` are covered.
Reflection, when needed to obtain the positive maximizing branch, must
be applied to the original CDF with its left limit at an atom; this is
the retained attainment theorem's convention.

When `s=0`, both centered conditional laws are zero almost surely. The
fixed-target identity still holds. For example, if `u<0`, its `Q` is
`-pi_k`, rather than zero; replacing the actual event by `FB(k)` would be
wrong. The finite polynomial gate handles this through the literal
evaluation `P(-u)` at zero conditional moments. The uniform theorem can
instead apply the strict binary theorem at the **actual** threshold.
No argument divides by noise at this boundary. The uniform positive-noise
estimate is proportional to `lambda`; it is used only for `lambda>0`.
