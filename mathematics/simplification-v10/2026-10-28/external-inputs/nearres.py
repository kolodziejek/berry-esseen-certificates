import math, numpy as np
exec(open('experiments.py').read().split('# ---------------------------------------------------------------- experiment 1')[0])
src=open('experiments.py').read()
exec(src[src.index('def noise_test'):src.index('print(f"C_E =')])
p=PSTAR
for n in [42,100]:
    print(f"--- n={n}, p=p*: outward rare jumps on the NEGATIVE class (toward -A-ell), double precision")
    for d in [0.5,0.8,0.9,0.95]:
        for eps in [0.005,0.02]:
            noise_test(n,p,[(-d,eps),(eps*d/(1-eps),1-eps)],[(0,1)],f"neg jump {d} rate {eps}")
