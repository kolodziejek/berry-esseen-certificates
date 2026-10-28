import numpy as np, itertools, math, sys
from scipy.special import ndtr, gammaln
from scipy.optimize import minimize

CE = (3 + math.sqrt(10)) / (6 * math.sqrt(2 * math.pi))
PSTAR = (4 - math.sqrt(10)) / 2

def sum_law(vals, probs, n):
    """Exact law of the sum of n iid copies of a discrete law (count-vector enumeration)."""
    m = len(vals)
    vecs = [c for c in itertools.product(range(n + 1), repeat=m - 1) if sum(c) <= n]
    C = np.array([list(c) + [n - sum(c)] for c in vecs])
    logp = gammaln(n + 1) - gammaln(C + 1).sum(1) + (C * np.log(np.asarray(probs))).sum(1)
    x = C @ np.asarray(vals, float)
    order = np.argsort(x, kind='mergesort')
    x, pr = x[order], np.exp(logp[order])
    # merge equal values
    key = np.round(x, 10)
    ux, idx = np.unique(key, return_index=True)
    pr = np.add.reduceat(pr, idx)
    return ux, pr

def scores(vals, probs, n):
    """Standardize, then return (positive closed score, overall score, maximizing raw threshold)."""
    vals = np.asarray(vals, float); probs = np.asarray(probs, float)
    mu = (vals * probs).sum(); sd = math.sqrt(((vals - mu) ** 2 * probs).sum())
    x = (vals - mu) / sd
    rho = (np.abs(x) ** 3 * probs).sum()
    s, pr = sum_law(x, probs, n)
    F = np.cumsum(pr); Fm = F - pr
    G = ndtr(s / math.sqrt(n))
    closed = F - G; openneg = G - Fm
    i = int(np.argmax(closed))
    pos = math.sqrt(n) * closed[i] / rho
    tot = math.sqrt(n) * max(closed.max(), openneg.max()) / rho
    return pos, tot, s[i], rho, sd, mu

def binom_pmf(n, p):
    k = np.arange(n + 1)
    return np.exp(gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1) + k * np.log(p) + (n - k) * np.log(1 - p))

# ---------------------------------------------------------------- experiment 1
def noise_test(n, p, U0, U1, label):
    """U0, U1: lists of (value, prob) for the conditional noise in count units (mean zero)."""
    q = 1 - p
    vals = [u for u, _ in U0] + [1 + u for u, _ in U1]
    probs = [q * w for _, w in U0] + [p * w for _, w in U1]
    pos, tot, H, rho, sd, mu = scores(vals, probs, n)
    ell = 1 / sd
    w0 = sum(w * u * u for u, w in U0); w1 = sum(w * u * u for u, w in U1)
    lam = n * (q * w0 + p * w1)
    x = n * p + H / ell
    k = int(math.floor(x + 0.5)); u = x - k
    v = p * q; rhoB = (1 - 2 * v) / math.sqrt(v)
    pmf = binom_pmf(n, p); FB = np.cumsum(pmf)
    delta = k - n * p
    CB = math.sqrt(n) / rhoB * (FB[k] - ndtr(delta / math.sqrt(n * v)))
    lhs = rhoB * (pos - CB)
    # law of V_k: k copies of U1 and n-k copies of U0
    def conv_power(U, m):
        d = {0.0: 1.0}
        for _ in range(m):
            e = {}
            for a, pa in d.items():
                for b, pb in U:
                    key = round(a + b, 10); e[key] = e.get(key, 0) + pa * pb
            d = e
        return d
    Vk = {}
    A = conv_power(U1, k); B = conv_power(U0, n - k)
    for a, pa in A.items():
        for b, pb in B.items():
            key = round(a + b, 10); Vk[key] = Vk.get(key, 0) + pa * pb
    efrac = sum(pr * ((u - val) - math.floor(u - val + 1e-12)) for val, pr in Vk.items())
    pred = -math.sqrt(n) * pmf[k] * efrac
    bestB = max(math.sqrt(n) / rhoB * (FB[j] - ndtr((j - n * p) / math.sqrt(n * v))) for j in range(n + 1))
    print(f"{label:34s} lam={lam:7.4f} u={u:+.3f} C={pos:.5f} C_B(k)={CB:.5f} maxC_B={bestB:.5f} "
          f"lhs={lhs:+.5f} pred={pred:+.5f} ratio={lhs / pred if pred else float('nan'):.3f}")

print(f"C_E = {CE:.6f}, p* = {PSTAR:.6f}")
n = 42; p = PSTAR
print(f"--- experiment 1: n={n}, p=p*; noise in count units")
noise_test(n, p, [(0, 1)], [(0, 1)], "two-point (no noise)")
for d in [0.05, 0.1, 0.2, 0.3]:
    noise_test(n, p, [(0, 1)], [(-d, .5), (d, .5)], f"symmetric +-{d} on positive class")
for d, eps in [(0.4, 0.02), (0.6, 0.02), (0.8, 0.02), (0.6, 0.005)]:
    noise_test(n, p, [(0, 1)], [(d, eps), (-eps * d / (1 - eps), 1 - eps)], f"rare jump {d} (eps={eps}) positive")
for d in [0.05, 0.15]:
    noise_test(n, p, [(-d, .5), (d, .5)], [(-d, .5), (d, .5)], f"symmetric +-{d} both classes")
noise_test(n, p, [(0.3, 0.02), (-0.3 * 0.02 / 0.98, 0.98)], [(-0.3, 0.02), (0.3 * 0.02 / 0.98, 0.98)], "rare inward jumps 0.3 both")
sys.stdout.flush()

# ---------------------------------------------------------------- experiment 2
print("--- experiment 2: best Bernoulli score vs best 3-point score found, small n")
def bern_best(n):
    best = 0
    for p in np.linspace(0.02, 0.98, 961):
        q = 1 - p; v = p * q
        pmf = binom_pmf(n, p); F = np.cumsum(pmf); Fm = F - pmf
        k = np.arange(n + 1); H = (k - n * p) / math.sqrt(v)
        G = ndtr(H / math.sqrt(n))
        rho = (p * p + q * q) / math.sqrt(v)
        sc = math.sqrt(n) * max((F - G).max(), (G - Fm).max()) / rho
        best = max(best, sc)
    return best

rng = np.random.default_rng(1)
def three_point_best(n, starts=40):
    def f(z):
        y = np.array([z[0], z[0] + math.exp(z[1]), z[0] + math.exp(z[1]) + math.exp(z[2])])
        w = np.exp(z[3:6]); w = w / w.sum()
        if w.min() < 1e-6: return 0.0
        return -scores(y, w, n)[1]
    best = 0
    for _ in range(starts):
        z0 = np.concatenate([[rng.normal()], rng.normal(size=2) - 0.5, rng.normal(size=3)])
        r = minimize(f, z0, method='Nelder-Mead', options={'maxiter': 600, 'xatol': 1e-7, 'fatol': 1e-9})
        best = max(best, -r.fun)
    return best
for n in [1, 2, 3, 4, 5, 6, 8, 10, 15, 20, 30, 41]:
    b = bern_best(n)
    t = three_point_best(n, starts=25 if n <= 10 else 12)
    print(f"n={n:3d}  best Bernoulli {b:.5f}  best 3-point found {t:.5f}  margin to C_E {CE - max(b, t):.5f}")
    sys.stdout.flush()
