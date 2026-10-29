#!/usr/bin/env python3
"""Independent receipt/cover accounting, not a signed arithmetic reimplementation."""
import argparse
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

PINS = {
    'signed_core.py': '1f40ccb90eb58a7f84dc61a0a5dd9bf6e6eb4e341aa6c9c6d049d08451f5211b',
    'signed_probe.py': '1bec84b1d7be1046f02a5eded4242b253fc98ce040d5b94c5dbb1942c7166fd6',
    'signed_support.py': 'eecb06e65d8520d7cc06fc34217e06e1c0b1840dd8d687621e6828923769a4c4',
}


def need(ok, why):
    if not ok:
        raise ValueError(why)


def unique(pairs):
    d = {}
    for k, v in pairs:
        need(k not in d, 'duplicate JSON key')
        d[k] = v
    return d


def read(path):
    return json.loads(path.read_text(), object_pairs_hook=unique)


def ceiling(x):
    return F(-((-x.numerator*10**8)//x.denominator), 10**8)


def account(obj, parent):
    need(obj['parameters'] == dict(steps=6, beta=8, gamma=8, mean=2,
                                  cell_support=True, initial='quadratic'), 'selected invocation')
    need(len(parent['rows']) == 24, 'parent 24 rows')
    states = []
    for i, row in enumerate(parent['rows']):
        l, u = 1+F(3361*i,96000), 1+F(3361*(i+1),96000)
        need(row['index'] == i and F(row['rho_lower']) == l and F(row['rho_upper']) == u, 'parent cover')
        p = row['passes'][-1]
        states.append(dict(index=i, l=l, u=u, raw=F(p['raw']), d=F(p['defect']), empty=False))
    need(len(obj['history']) == 6, 'six passes')
    total = 0
    for j, step in enumerate(obj['history'], 1):
        need(len(step['rows']) == 24, 'all original rho rows accounted for')
        tested = active_cells = 0
        for i, row in enumerate(step['rows']):
            need(row['index'] == i, 'ordered rho identities')
            st = states[i]
            if st['empty']:
                need(row == dict(index=i, prior_excluded=True), 'excluded rows remain excluded')
                continue
            need(F(row['prior_raw']) == st['raw'] and F(row['prior_defect']) == st['d'], 'ordered parent invariants')
            out = row['output']
            need(out['total'] == 128 and out['active']+out['excluded'] == 128, 'signed cover census')
            need(sum(out['reasons'].values()) == out['excluded'], 'exclusion census')
            need(F(5,2) <= F(row['radius']) <= F(96,25), 'reviewed support radius interval')
            tested += out['total']; active_cells += out['active']
            if out['active']:
                R, D = F(out['R']), F(out['D'])
                need(0 <= R <= st['raw'] and 0 <= D <= st['d'], 'monotone output ceilings')
                st['raw'] = min(st['raw'], ceiling(R)); st['d'] = min(st['d'], ceiling(D))
            else:
                st['empty'] = True
        active = [s for s in states if not s['empty']]
        expected = dict(step=j, max_raw=max(s['raw'] for s in active), max_D=max(s['d'] for s in active),
                        remaining_rho_cells=len(active), rho_upper=max(s['u'] for s in active),
                        cells_below2=sum(s['d'] < 2 for s in active),
                        cells_below_target=sum(s['d'] < F(98,125) for s in active),
                        tested_signed_cells=tested, active_signed_cells=active_cells)
        need(step['summary'].keys() == expected.keys(), 'summary fields')
        need(all(F(step['summary'][k]) == v for k,v in expected.items()), 'reconstructed summary')
        total += tested
    need(len(obj['final_states']) == 24, 'all final identities')
    for st, stored in zip(states,obj['final_states']):
        need(stored.keys() == st.keys(), 'final fields')
        need(all((stored[k] == v if isinstance(v,bool) else F(stored[k]) == v) for k,v in st.items()), 'final state reconstruction')
    return expected, total


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--source-root', type=Path, default=Path('.')); args=ap.parse_args()
    root=args.source_root; source=root/'mathematics/fixed-target-v7/2026-10-27'
    run=root/'runs/fixed-target-v7-20261027/signed07'
    for f, h in PINS.items():
        need(sha256((source/f).read_bytes()).hexdigest() == h, 'reviewed live source')
        need(sha256((run/f).read_bytes()).hexdigest() == h, 'same source snapshot')
    receipt=read(run/'receipt.json'); need(receipt['returncode'] == 0 and receipt['optimization'] == 0, 'constructor process success')
    obj=read(run/'stdout.json'); parent_path=root/'runs/fixed-target-v6-20261027/signed-two-pass02/stdout.json'
    parent=read(parent_path); result,total=account(obj,parent)
    controls=[]
    for name, mutate in [
        ('missing rho row',lambda z:z['history'][0]['rows'].pop()),
        ('duplicate identity',lambda z:z['history'][0]['rows'][1].update(index=0)),
        ('wrong initial raw',lambda z:z['history'][0]['rows'][0].update(prior_raw='1')),
        ('false peak',lambda z:z['history'][-1]['summary'].update(max_D='0')),
        ('lost signed cells',lambda z:z['history'][0]['rows'][0]['output'].update(total=127)),
    ]:
        bad=deepcopy(obj); mutate(bad)
        try: account(bad,parent)
        except ValueError: controls.append(name)
        else: raise ValueError('mutation accepted: '+name)
    pins={str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in [run/'stdout.json',run/'receipt.json',parent_path]}
    def encode(x):
        if isinstance(x,F): return str(x)
        if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
        return x
    print(json.dumps(encode(dict(status='PASS_STRUCTURAL_ACCOUNTING_ONLY', final=result, signed_cells_accounted=total,
        rejected_controls=controls, source_pins=PINS, input_sha256=pins,
        limitations='No constructor imports, no numerical leaf reevaluation, no Fourier or BASE41 acceptance.')),indent=2,sort_keys=True))


if __name__ == '__main__': main()
