# Bounded paired-Fourier algebra checks

`check_identities.py` is a byte-identical copy of the script identified by
`evidence/checked/RESULT.json`. The preserved process returned zero and
checked eleven identities, four Gaussian coefficients and eight rejected
changed identities. It also checks that the old `43` damping specialization
is too strong at fourth-moment ceiling `5/2`; the manuscript retains the
correct general coefficient `45−M` there.

Run with unoptimized standard-library Python and a nonexistent output path:

```sh
python3 -I -B check_identities.py /tmp/paired-algebra-new
```

The printed proofs supply positivity domains, integrations and uniform
remainders. These bounded algebra checks accept no native numerical family.
Historical absolute paths in the verbatim receipts identify the original
execution; they are not required by this command.
