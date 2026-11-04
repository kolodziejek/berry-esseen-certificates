# Construction is separate from acceptance

These are copies of the construction programs, outside the proof's trusted
acceptance path. The manuscript's small-noise proof uses explicit quartic,
Cantelli and zero witnesses. The scale `.4784` and split parameters `5/3,6/5`
were proposed during exploration; exact acceptance is what establishes their
adequacy on complete domains.

`build_proposal.py` computes the uniform four polynomial targets and converts
them to Bernstein coefficients by the forward formula. It can propose
subdivision trees, but the accepted object needs no subdivision. To rerun it,
make a fresh disposable copy of `../../certificates/joint-count/tiny/`, place
this script in that copy, and pass a nonexistent output JSON path. Run the
copy's `accept.py` on the resulting candidate separately.

`build_finite.py` likewise belongs in a fresh disposable copy of
`../../certificates/joint-count/finite/`. It tries intermediate losses in the
order `.1,.05,0,-.05,-.1`, retaining the unchanged final target and allowance.
For each row it chooses the first loss whose four exact coefficient arrays
and final gate pass. Its output still requires the independent
`accept_finite.py` inverse-basis checks. Both small-noise builders use only
the standard library and create their output rather than overwriting it.

`discover_mid.py` is the optional intermediate-noise floating LP search.
It needs NumPy and SciPy; these are unnecessary for certificate verification.
It takes a fresh output directory. `build_mid.py` and `mid_math.py` then
rationalize the returned `RESULT.json`, add a fixed constant margin, and
propose exact interval/ray Bernstein trees in a second fresh directory.
The separate `mid/accept_mid.py`, source-bound normalizer and controls accept
the resulting global proof object. Every accepted ray is checked on its whole
half-line. The earlier far-left failure explains why sampled optimization
alone is insufficient.

The final accepted data and checkers are in `certificates/joint-count/`;
no construction program, convergence claim or optimizer success flag is
needed to use them. All finite polynomial identities and continuous-domain
licenses are specified independently of the discovery process.
