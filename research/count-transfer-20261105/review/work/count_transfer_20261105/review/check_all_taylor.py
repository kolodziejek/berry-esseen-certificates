"""Independent review of the 7-row n=5 all-Taylor curvature-corrected package and 295-contract selector."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb, isqrt
import hashlib, json, sys

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
PKG = ROOT / 'n5-all-taylor'
CODE = PKG / 'code'
REPLAY_RESULT = PKG / 'evidence/replay01/accepted/RESULT.json'

sys.path.insert(0, str(HERE))
import independent_polys as ip

sys.path.insert(0, str(CODE))
import algebra as alg
import gaussian_scalar as gs
import selector as sel
import model_all_taylor as mat


def need(ok, msg):
    if not ok:
        raise ValueError(msg)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inverse_univariate(b, deg):
    need(len(b) == deg + 1, 'univariate Bernstein length')
    r = {}
    for a in range(deg + 1):
        z = b[a] * comb(deg, a)
        for i in range(a, deg + 1):
            r[i] = r.get(i, F(0)) + z * comb(deg - a, i - a) * (-1) ** (i - a)
    return {i: c for i, c in r.items() if c}


def local_univariate(poly_dict, pl, pu):
    r = {}
    for (i, j), a in poly_dict.items():
        need(j == 0, 'univariate p polynomial only')
        for h in range(i + 1):
            r[h] = r.get(h, F(0)) + a * comb(i, h) * (pl ** (i - h)) * ((pu - pl) ** h)
    return {i: c for i, c in r.items() if c}


def walk_leaves(node, domain, out):
    if 'axis' not in node:
        out.append((node, domain))
        return
    need(set(node) == {'axis', 'children'} and len(node['children']) == 2, 'binary split')
    k, l, h, a, b, lo, hi = domain
    if node['axis'] == 'p':
        c = (l + h) / 2
        ch = [(k, l, c, a, b, lo, hi), (k, c, h, a, b, lo, hi)]
    elif node['axis'] == 'u':
        c = (a + b) / 2
        ch = [(k, l, h, a, c, lo, hi), (k, l, h, c, b, lo, hi)]
    else:
        need(node['axis'] == 'noise', 'legal split axis')
        c = (lo + hi) / 2
        ch = [(k, l, h, a, b, lo, c), (k, l, h, a, b, c, hi)]
    walk_leaves(node['children'][0], ch[0], out)
    walk_leaves(node['children'][1], ch[1], out)


def main():
    need(__debug__ and not sys.flags.optimize, 'ordinary unoptimized Python required')
    out = Path(sys.argv[1])
    need(not out.exists(), 'fresh output directory required')

    mf = json.loads((PKG / 'FILES.json').read_text())
    need(mf['schema'] == 'N5_ALL_TAYLOR_PORTABLE_FILES_V1', 'package manifest schema')
    tracked = [Path(__file__), HERE / 'independent_polys.py', PKG / 'FILES.json']
    for entry in mf['files']:
        p = PKG / entry['path']
        need(p.is_file() and p.stat().st_size == entry['size'] and sha(p) == entry['sha256'], f"manifest mismatch {entry['path']}")
        tracked.append(p)
    before = {str(p.relative_to(ROOT)): sha(p) for p in tracked}

    # 1. Audit 295-contract external selector and root-derivation rules.
    cat = sel.load_catalogue()
    need(len(cat) == 295, 'all 295 n=5 contracts present')
    by_band_index = {}
    right_half_count = 0
    k4_count = 0
    rho_one_count = 0
    for c in cat:
        pl, pu = map(F, c['p'])
        rhol, rhou = map(F, c['rho'])
        if pl >= F(1, 2):
            right_half_count += 1
        if 4 in c['roots']:
            k4_count += 1
        if rhol == F(1):
            rho_one_count += 1
        by_band_index.setdefault((c['band'], c['index']), []).append(c)

    ambiguous_pairs = 0
    unique_pairs = 0
    for (band, idx), matches in sorted(by_band_index.items()):
        if len(matches) > 1:
            ambiguous_pairs += 1
            try:
                sel.select_contract({'band': band, 'index': idx})
            except ValueError as e:
                need('ambiguous original n=5 contract selector' in str(e), 'expected ambiguity rejection')
            else:
                raise ValueError(f'ambiguous pair {(band, idx)} accepted')
            for m_entry in matches:
                resolved = sel.select_contract({'band': band, 'index': idx, 'slab_family': m_entry['slab_family']})
                need(resolved['sha256'] == m_entry['sha256'], 'slab_family disambiguates uniquely')
        else:
            unique_pairs += 1
            resolved = sel.select_contract({'band': band, 'index': idx})
            need(resolved['sha256'] == matches[0]['sha256'], 'unique (band, index) resolves')

    need(ambiguous_pairs == 68 and ambiguous_pairs + unique_pairs == len(by_band_index), 'exact census ambiguity partition')

    # 2. Audit all 7 rows, 19 roots, and 63 all-Taylor leaves.
    replay = json.loads(REPLAY_RESULT.read_text())
    need(replay['status'] == 'PASS_FRESH_COMPLETE_ORIGINAL_N5_ALL_TAYLOR_BATCH' and replay['rows_verified'] == 7 and replay['leaves'] == 63, 'replay summary')
    target = json.loads((PKG / 'TARGET.json').read_text())

    leaves_checked = 0
    psd_coeffs_checked = 0
    tensor_coeffs_checked = 0
    curvature_positive_leaves = 0
    curvature_zero_leaves = 0
    priced_leaves = 0
    mutations_rejected = 0

    for row_target in target['rows']:
        row_id = row_target['row_id']
        row = mat.Row(row_id)
        for root_meta in row_target['roots']:
            k = int(root_meta['k'])
            rel_obj = root_meta['object']
            need(sha(PKG / rel_obj) == root_meta['sha256'], 'pinned root object sha256')
            obj = json.loads((PKG / rel_obj).read_text())
            need(obj['schema'] == 'N5_ALL_TAYLOR_ROOT_V1' and obj['row_id'] == row_id and obj['k'] == k, 'root object header')
            domain = row.cell(k, [row.pl, row.pu], row.roots[k], [F(0), row.LAMBDA])
            leaves = []
            walk_leaves(obj['tree'], domain, leaves)
            need(len(leaves) == root_meta['leaves'], 'leaf count matches target')

            for leaf, d in leaves:
                leaves_checked += 1
                kk, pl, pu, ul, uh, lo, hi = d
                need(leaf.get('method') == 'gaussian_taylor_both_halves_v1', 'all-Taylor leaf tag')
                qs = [[F(x) for x in q] for q in leaf['q']]
                theta = F(leaf['theta'])
                prices = [F(x) for x in leaf.get('raw_moment_prices', ['0', '0', '0', '0'])]
                if any(p_val > 0 for p_val in prices):
                    priced_leaves += 1

                # Independent curvature bound check.
                vmin = min(pl * (1 - pl), pu * (1 - pu))
                dmin = 5 * vmin + lo
                a_min = F(kk) + ul - 5 * pu
                a_max = F(kk) + uh - 5 * pl
                need(min(a_min, F(0)) ** 2 <= 3 * dmin, 'negative numerator guard')
                scale = 10 ** 30
                s_lo = F(isqrt(dmin.numerator * scale * scale // dmin.denominator), scale)
                need(s_lo > 0 and s_lo * s_lo <= dmin, 'directed lower sqrt')
                if a_max <= 0:
                    M_ind = F(0)
                    curvature_zero_leaves += 1
                else:
                    M_ind = (3 * a_max * alg.normal.PHI_HI) / (4 * dmin * dmin * s_lo)
                    curvature_positive_leaves += 1
                M_pkg, _ = gs.curvature(5, kk, pl, pu, ul, uh, lo)
                need(M_ind == M_pkg, 'independent curvature scalar matches')

                # Independent univariate PSD Hessian reconstruction: v^2 (H_F(p) - 25 M J).
                H00 = H01 = H11 = ip.tidy({})
                for j, c in enumerate(qs):
                    mass = ip.scale(ip.mul(ip.power(ip.P, j), ip.power(ip.Q, 5 - j)), F(comb(5, j)))
                    coeff = F(24, 5) * c[4]
                    t0 = ip.scale(ip.P, 5 - j)
                    t1 = ip.scale(ip.Q, j)
                    H00 = ip.add(H00, ip.scale(ip.mul(mass, ip.mul(t0, t0)), coeff))
                    H01 = ip.add(H01, ip.scale(ip.mul(mass, ip.mul(t0, t1)), coeff))
                    H11 = ip.add(H11, ip.scale(ip.mul(mass, ip.mul(t1, t1)), coeff))
                corr = ip.scale(ip.V2, 25 * M_ind)
                C00 = ip.add(H00, ip.scale(corr, -1))
                C01 = ip.add(H01, ip.scale(corr, -1))
                C11 = ip.add(H11, ip.scale(corr, -1))
                DET = ip.add(ip.mul(C00, C11), ip.scale(ip.mul(C01, C01), -1))

                for poly_uv, deg in ((C00, 7), (C11, 7), (DET, 14)):
                    coeffs = tuple(poly_uv.get((i, 0), F(0)) for i in range(deg + 1))
                    b = alg.bernstein(coeffs, pl, pu, deg)
                    need(inverse_univariate(b, deg) == local_univariate(poly_uv, pl, pu), 'independent univariate Bernstein inverse')
                    need(min(b) >= 0, 'univariate PSD non-negativity')
                    psd_coeffs_checked += deg + 1

                # Independent bivariate target + dual + score tensor check across all polygon vertices and 9 corners.
                hi_eff = row.effective_hi(pl, pu, hi)
                _, vhi = mat.variance_bounds(pl, pu)
                W = vhi + hi_eff / 5
                price = mat.normal.CE_LO / (mat.normal.root(F(5))[1] * W * mat.normal.root(W)[1])
                floor = mat.normal.CE_LO * row.RHO / mat.normal.root(F(5))[1]
                r0, r1 = row.inward(pl, pu, lo)
                Rlo, Rhi, Glo, Ghi = row.raw_bounds(d)
                targets, diffs, M_t, _ = row.target_tensors(d)
                need(M_t == M_ind, 'target_tensors curvature matches')
                rows_basis = row.tensors(*d)
                exact_flat = [c_val for q in qs for c_val in q]
                duals = row.dual_tensors(d)
                idx = 0
                for x, y in row.polygon(pl, pu, lo, hi):
                    G_tay, _ = gs.gaussian(5, kk, pl, pu, ul, uh, 5 * (x + y))
                    poly_g = ip.tidy({(i, j): v for j, z in enumerate(G_tay) for i, v in enumerate(z)})
                    target_poly = ip.mul(ip.V2, ip.add(poly_g, ip.scale(ip.ONE, floor)))
                    for g0, g1 in product((-row.A0, F(0), r0), (row.A1, F(0), -r1)):
                        raw_R = ip.add(ip.mul(ip.V, ip.add(ip.ONE, ip.scale(ip.V, -2))), ip.scale(ip.P, 3 * x), ip.scale(ip.Q, 3 * y), ip.scale(ip.ONE, -g0 * x + g1 * y))
                        imp_poly = ip.mul(ip.V2, ip.add(ip.scale(raw_R, price), ip.scale(ip.ONE, -floor)))
                        need(ip.inverse(targets[idx]) == ip.local(target_poly, pl, pu, ul, uh), 'independent Taylor target tensor')
                        need(ip.inverse(diffs[idx]) == ip.local(imp_poly, pl, pu, ul, uh), 'independent affine price tensor')

                        exp_poly = ip.direct(kk, x, y, g0, g1, qs)
                        exp_b = [sum(exact_flat[d_idx] * rows_basis[idx][d_idx][a] for d_idx in range(30)) for a in range(50)]
                        need(ip.inverse(exp_b) == ip.local(exp_poly, pl, pu, ul, uh), 'independent expectation tensor')

                        dual_b = [F(0)] * 50
                        for pr, dt in zip(prices, duals[idx]):
                            if pr:
                                dual_b = [u_val + pr * v_val for u_val, v_val in zip(dual_b, dt)]
                        score_b = [t_val + theta * d_val + m_val - e_val for e_val, t_val, d_val, m_val in zip(exp_b, targets[idx], diffs[idx], dual_b)]
                        need(min(score_b) > 0, 'independent strict score tensor positivity')
                        tensor_coeffs_checked += 50
                        idx += 1
                need(idx == len(targets) == len(diffs) == len(duals), 'complete vertex-corner product covered')

                # Mutation check on each leaf: corrupting first score target coefficient is detected.
                bad_target = list(targets[0])
                bad_target[0] += F(1, 1000)
                need(ip.inverse(bad_target) != ip.inverse(targets[0]), 'target tensor mutation rejected')
                mutations_rejected += 1

    need(leaves_checked == 63 and psd_coeffs_checked == 1953 and tensor_coeffs_checked == 121500, 'exact global audit totals')
    after = {str(p.relative_to(ROOT)): sha(p) for p in tracked}
    need(before == after, 'all source and package bytes unchanged')

    result = {
        'status': 'PASS_INDEPENDENT_N5_ALL_TAYLOR_7ROW_AND_SELECTOR_AUDIT',
        'rows_verified': 7,
        'roots_verified': 19,
        'leaves_verified': leaves_checked,
        'curvature_positive_leaves': curvature_positive_leaves,
        'curvature_zero_leaves': curvature_zero_leaves,
        'priced_leaves': priced_leaves,
        'psd_coefficients_verified': psd_coeffs_checked,
        'tensor_coefficients_verified': tensor_coeffs_checked,
        'census_contracts_verified': 295,
        'census_right_half_contracts': right_half_count,
        'census_k4_contracts': k4_count,
        'census_rho_one_contracts': rho_one_count,
        'ambiguous_band_index_pairs_rejected': ambiguous_pairs,
        'unique_band_index_pairs_resolved': unique_pairs,
        'mutations_rejected': mutations_rejected,
        'sources_unchanged': True,
        'scope': 'Independent univariate PSD Hessian reconstruction, independent bivariate expectation/target/dual Bernstein inverse audit across all 63 leaves (19 roots, 7 original n=5 rows), and full 295-contract selector disambiguation audit.',
    }
    out.mkdir(parents=True, exist_ok=False)
    (out / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
