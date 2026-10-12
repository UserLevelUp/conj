"""Verify baseline input hashes and independently enumerate the C17 projection.

No third-party dependencies; does not overwrite the historical verification file.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import itertools
import json

ROOT = Path(__file__).resolve().parents[1]


def main():
    fingerprints = 0
    for name in ('main.conjectures.checks.json', 'main.conjectures.analysis.observations.json'):
        data = json.loads((ROOT/name).read_text())
        assert len(data['source_sha256']) == 26, name
        for path, expected in data['source_sha256'].items():
            assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == expected, path
            fingerprints += 1
    q=F(1,4); L=6
    prob=[(1-q*q)**((s+1)//2)*(1-q if s%2==0 else 1) for s in range(L+1)]
    w=[-q*p/(1-q*q) for p in prob]
    formula=[sum(w[i:])+(-prob[2*i]/(1-q)-w[2*i] if 2*i<=L else 0) for i in range(L+1)]
    enumerated=[F(0) for _ in range(L+1)]; mass=F(0); mean=F(0)
    for bits in itertools.product([0,1], repeat=L+1):
        a=[i for i,b in enumerate(bits) if b]; sums={i+j for i in a for j in a}
        missing=sum(s not in sums for s in range(L+1))
        weight=q**sum(bits)*(1-q)**(L+1-sum(bits)); mass+=weight; mean+=weight*missing
        for i in range(L+1): enumerated[i]+=weight*missing*(bits[i]-q)/(q*(1-q))
    assert mass==1 and mean==sum(prob) and enumerated==formula
    recorded=json.loads((ROOT/'main.conjectures.analysis.verification.json').read_text())
    assert recorded['exact_projection']['coefficients']==[str(x) for x in enumerated]
    print(f'PASS: {fingerprints} fingerprint checks; exact rational projection over 128 subsets.')
    print('These checks verify bounded evidence, not conjecture truth or novelty.')


if __name__=='__main__': main()

# publish: main.conjectures.publication.verification portable evidence verification
# consumer: main.conjectures.analysis.experiments
