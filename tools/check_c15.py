"""Generate deterministic C15 observations or verify their source fingerprints."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.c15_bounds import gaussian_max_cdf, gumbel_normalizers, simultaneous_quantile, simultaneous_radius

SOURCES = [
    'main.conjectures.c15.education-attention-alignment.current.md',
    'main.conjectures.analysis.c15.subset.complete.md',
    'tools/c15_bounds.py', 'tools/check_c15.py', 'tests/test_c15_bounds.py',
    'tools/build_c15_figure.py',
]


def fingerprints():
    return {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCES}


def calculate():
    coverage = []
    for n in (1, 10, 100, 10000, 10**12):
        q = simultaneous_quantile(n, 0.05)
        coverage.append(dict(n=n, alpha=0.05, quantile=q, coverage=gaussian_max_cdf(q, n)))
    limits = []
    for n in (10, 100, 10000, 10**8):
        a, b = gumbel_normalizers(n)
        for x in (-1, 0, 1, 2):
            exact = gaussian_max_cdf(b+x/a, n)
            limit = math.exp(-math.exp(-x))
            limits.append(dict(n=n, x=x, exact=exact, limit=limit, difference=exact-limit))
    radius = simultaneous_radius(10, 25, 1, 0.05)
    return dict(exact_coverage=coverage, gumbel_comparisons=limits,
                context_correlation_counterexample=dict(
                    n=10, r=25, nominal_coverage=0.95,
                    actual_coverage=gaussian_max_cdf(radius, 10),
                    model='Independent rows; all errors within each row equal one standard normal'))


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--output', type=Path)
    group.add_argument('--verify', type=Path)
    args = parser.parse_args()
    if args.verify:
        record = json.loads(args.verify.read_text(encoding='utf-8'))
        assert record['source_sha256'] == fingerprints(), 'Stale C15 source fingerprints'
        # Check selected numerical invariants independent of JSON formatting/platform.
        for row in record['observations']['exact_coverage']:
            assert abs(row['coverage']-(1-row['alpha'])) < 1e-12
            assert abs(row['quantile']-simultaneous_quantile(row['n'], row['alpha'])) < 1e-12
        actual = record['observations']['context_correlation_counterexample']['actual_coverage']
        assert actual < 0.01
        assert abs(actual-calculate()['context_correlation_counterexample']['actual_coverage']) < 1e-12
        for row in record['observations']['gumbel_comparisons']:
            a, b = gumbel_normalizers(row['n'])
            assert abs(row['exact']-gaussian_max_cdf(b+row['x']/a, row['n'])) < 1e-12
            assert abs(row['limit']-math.exp(-math.exp(-row['x']))) < 1e-12
            assert abs(row['difference']-(row['exact']-row['limit'])) < 1e-12
        print('PASS: C15 source fingerprints and recorded numerical invariants')
        return
    record = dict(trace_id='main.conjectures.analysis.c15.checks',
                  method='Deterministic analytic formulas; no random samples or market data',
                  command='python tools/check_c15.py --output docs/c15-checks.json',
                  python=platform.python_version(), source_sha256=fingerprints(),
                  observations=calculate(),
                  limits='Checks illustrate formulas, not asymptotic proof or prospective market calibration')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    print(f'Wrote {args.output}')


if __name__ == '__main__':
    main()
