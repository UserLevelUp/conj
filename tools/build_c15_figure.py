"""Analytic C15 figure; no random data or fitted trading parameters."""
import hashlib
import json
import math
from pathlib import Path
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.c15_bounds import gaussian_max_cdf, gumbel_normalizers, simultaneous_quantile


def main():
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                         'figure.facecolor': '#101d30', 'axes.facecolor': '#101d30',
                         'text.color': '#eef5fc', 'axes.labelcolor': '#d4e1ee',
                         'xtick.color': '#c1d2e2', 'ytick.color': '#c1d2e2',
                         'axes.edgecolor': '#506578', 'svg.hashsalt': 'conj-c15-v020'})
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))
    fig.subplots_adjust(left=.075, right=.97, bottom=.22, top=.77, wspace=.27)
    fig.suptitle('C15 | What complete observation lets us prove', fontsize=20, x=.075, ha='left', y=.965)
    fig.text(.075, .865, 'Exact finite uncertainty, a limiting law, and a visible cost for searching more candidates', color='#a6bfce')
    x = np.linspace(-2, 4, 220)
    for n, color in ((10, '#f7b267'), (100, '#73b7ed'), (10000, '#65dbc1')):
        a, b = gumbel_normalizers(n)
        axes[0].plot(x, [gaussian_max_cdf(b+v/a, n) for v in x], label=f'n = {n:,}', color=color)
    axes[0].plot(x, np.exp(-np.exp(-x)), '--', color='#ffffff', label='Gumbel limit', linewidth=1.5)
    axes[0].set(xlabel='Normalized maximum error x', ylabel='Cumulative probability', ylim=(0, 1), title='Finite distributions approach the limit')
    axes[0].legend(facecolor='#101d30', labelcolor='#eef5fc', edgecolor='#506578', loc='lower right', fontsize=9)
    sizes = sorted(set(np.geomspace(1, 10000, 100).astype(int)))
    axes[1].plot(sizes, [simultaneous_quantile(int(n), .05) for n in sizes], color='#65dbc1', linewidth=2.5)
    axes[1].axhline(simultaneous_quantile(1, .05), color='#f7b267', linestyle='--', label='One candidate')
    axes[1].set(xscale='log', xlabel='Number of candidates n', ylabel=r'Radius in units of $\sigma/\sqrt{r}$', title='95% simultaneous confidence')
    axes[1].legend(facecolor='#101d30', labelcolor='#eef5fc', edgecolor='#506578', fontsize=9)
    for ax in axes:
        ax.grid(alpha=.15)
        ax.spines[['top', 'right']].set_visible(False)
    fig.text(.075, .065, 'Analytic Gaussian model • known noise scale • independent errors • p = 1\nThese curves contain no market data and establish no investment signal.', color='#a6bfce', fontsize=10)
    out = ROOT/'assets/c15-subset'
    fig.savefig(out.with_suffix('.png'), dpi=160)
    fig.savefig(out.with_suffix('.svg'), metadata={'Date': None})
    svg = out.with_suffix('.svg')
    svg.write_bytes(('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines())+'\n').encode('utf-8'))
    plt.close(fig)
    sources = ['tools/build_c15_figure.py', 'tools/c15_bounds.py']
    artifacts = ['assets/c15-subset.png', 'assets/c15-subset.svg']
    manifest = dict(method='Analytic formulas, no random data', matplotlib=matplotlib.__version__,
                    source_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
                    artifact_sha256={p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in artifacts})
    (ROOT/'assets/c15-subset.manifest.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    print('Wrote C15 subset PNG/SVG and provenance manifest')


if __name__ == '__main__':
    main()
