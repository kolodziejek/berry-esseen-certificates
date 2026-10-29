# Experiments behind the "Version 3: shorter argument" review

All scores are computed exactly for discrete laws (sum laws by count-vector
enumeration, CDF and normal comparison in double precision). Numerical
evidence only; nothing here is a certificate.

- `experiments.py` — (1) n = 42, p = p*: two-point law plus mean-zero noise of
  several shapes; exact score, loss below the Bernoulli skeleton, and the
  first-order prediction sqrt(n) pi_k E frac(u - V_k). (2) For n = 1..41: best
  two-point score versus the best 3-point law found by random-start
  Nelder-Mead. Runtime: a few minutes.
- `contact_test.py` — for n = 1..100: the contact function I(y) of Lemma 2.2 at
  the best two-point law, on [-6, 6] including both sides of every jump.
  Reports sup I (zero up to rounding, attained at the atoms).
- `skeleton_test.py` — random 3- to 5-point laws: how often a law beats its own
  Bernoulli skeleton, and the highest score among those that do. Imports the
  helper functions from `experiments.py`; run it from the same directory.

Requires numpy and scipy.
