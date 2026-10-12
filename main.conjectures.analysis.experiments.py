"""Bounded experiments for C16/C17 and C24; numerical evidence is not proof."""
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
import numpy as np
import scipy
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

parser = argparse.ArgumentParser()
parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent)
parser.add_argument('--output', type=Path)
args = parser.parse_args()
ROOT = args.root.resolve()
SEED = 20261012
rng = np.random.default_rng(SEED)

def kernel(u, v):
    t = min(u, v)
    return 8*((1-math.exp(-2*t))/2
              -(math.exp(-u)+math.exp(-v))*(1-math.exp(-t))
              + t*math.exp(-u-v))

def sumsets(q, reps=1200):
    # This family satisfies q^2 m / log(1/q) -> infinity.
    m = math.ceil(4*math.log(1/q)**2/q**2)
    length = 1 << (2*m-2).bit_length()
    s = np.arange(m)
    prob = (1-q*q)**((s+1)//2) * np.where(s % 2 == 0, 1-q, 1.)
    us = [.5, 1., 2., 4.]
    bounds = [math.floor(2*u/q**2) for u in us]
    coeff = []
    means = []
    for bound in bounds:
        w = -q*prob[:bound+1]/(1-q*q)
        a = np.cumsum(w[::-1])[::-1]
        i = np.arange(bound//2+1)
        a[i] += -prob[2*i]/(1-q)-w[2*i]
        coeff.append(a)
        means.append(float(prob[:bound+1].sum()))
    z = np.empty((reps, len(us)))
    linear = np.empty_like(z)
    full = np.empty(reps)
    fronts = np.empty((reps, 2))
    full_mean = float(2*prob.sum()-prob[-1])
    # Independent direct sumset check of the FFT observable on small samples.
    for _ in range(20):
        a = rng.random(40) < q
        exact = {int(i+j) for i in np.flatnonzero(a) for j in np.flatnonzero(a)}
        fft = np.rint(np.fft.irfft(np.fft.rfft(a, 128)**2, 128)[:79]).astype(int)
        assert set(np.flatnonzero(fft)) == exact
    for j in range(reps):
        a = rng.random(m) < q
        sums = np.rint(np.fft.irfft(np.fft.rfft(a, length)**2, length)[:2*m-1])
        miss = sums == 0
        cumulative = np.cumsum(miss[:m])
        z[j] = q**1.5*(cumulative[bounds]-means)
        linear[j] = [q**1.5*float(c@(a[:len(c)]-q)) for c in coeff]
        full[j] = q**1.5*(miss.sum()-full_mean)
        left = np.flatnonzero(miss[:m])
        right = np.flatnonzero(miss[m:][::-1])
        fronts[j] = [q*q*(int(v[-1]) if len(v) else -1)/2-math.log(2/q**2)
                     for v in (left, right)]
    residual = z-linear
    thresholds = [-1., 0., 1., 2.]
    return dict(q=q, m=m, replicates=reps, u=us,
        exact_profile_means=means, exact_full_mean=full_mean,
        predicted_covariance=[[kernel(u,v) for v in us] for u in us],
        observed_covariance=np.cov(z,rowvar=False).tolist(),
        exact_projection_covariance=[[float(q**4*(1-q)*np.dot(a[:min(len(a),len(b))], b[:min(len(a),len(b))])) for b in coeff] for a in coeff],
        residual_scaled_variances=np.var(residual,axis=0,ddof=1).tolist(),
        full_scaled_mean=float(full.mean()), full_scaled_variance=float(full.var(ddof=1)),
        front_cdf_thresholds=thresholds,
        front_cdfs=[[float(np.mean(fronts[:,k]<=x)) for x in thresholds] for k in range(2)],
        gumbel_cdf=[math.exp(-math.exp(-x)) for x in thresholds],
        front_correlation=float(np.corrcoef(fronts.T)[0,1]),
        left_front_profile_correlations=[float(np.corrcoef(fronts[:,0],z[:,i])[0,1]) for i in range(len(us))],
        covariance_mc_relative_scale=math.sqrt(2/(reps-1)),
        limitations='Finite annealed simulations; correlations do not establish independence. No convergence tests or acceptance thresholds.')

def planar_gap(values, cap=10000):
    n = len(values)
    pred = [sum(1<<j for j in range(i) if values[j]<values[i]) for i in range(n)]
    states = []
    def visit(mask, seq):
        if len(states)>cap:
            raise OverflowError
        if len(seq)==n:
            states.append(tuple(seq)); return
        for i in range(n):
            if not (mask>>i)&1 and pred[i]&mask == pred[i]:
                visit(mask|(1<<i),seq+[i])
    try:
        visit(0,[])
    except OverflowError:
        return dict(permutation=list(map(int,values)), skipped='extension cap', cap=cap)
    if len(states)==1:
        return dict(permutation=list(map(int,values)),states=1,gap=1.,residual=0.)
    lookup = {s:i for i,s in enumerate(states)}
    rows=[]; cols=[]; data=[]
    c=1/(2*(n-1))
    for i, state in enumerate(states):
        degree=0
        for j in range(n-1):
            a,b=state[j:j+2]
            if not ((pred[b]>>a)&1 or (pred[a]>>b)&1):
                target=list(state); target[j],target[j+1]=b,a
                rows.append(i); cols.append(lookup[tuple(target)]); data.append(-c)
                degree+=1
        rows.append(i); cols.append(i); data.append(degree*c)
    lap=coo_matrix((data,(rows,cols)),shape=(len(states),len(states))).tocsr()
    assert abs(lap.sum(axis=1)).max()<1e-12
    assert (lap-lap.T).nnz==0
    if len(states)<5:
        vals,vecs=np.linalg.eigh(lap.toarray())
    else:
        vals,vecs=eigsh(lap,k=2,which='SM',tol=1e-10,v0=np.arange(1,len(states)+1,dtype=float))
        order=np.argsort(vals); vals=vals[order]; vecs=vecs[:,order]
    gap=float(vals[1]); residual=float(np.linalg.norm(lap@vecs[:,1]-gap*vecs[:,1]))
    assert gap>0 and residual<1e-8
    return dict(permutation=list(map(int,values)),states=len(states),gap=gap,n_cubed_gap=n**3*gap,residual=residual)

results={'date':'2026-10-12','seed':SEED,
 'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
 'scope':'finite experiments; no mathematical acceptance', 'sumsets':[], 'planar_gaps':{}}
for q in [.1,.05,.025]:
    result=sumsets(q)
    results['sumsets'].append(result)
    print(json.dumps({'q':q,'full_variance':result['full_scaled_variance'],
        'residual_variances':result['residual_scaled_variances']}),flush=True)
for n in [6,8,10]:
    rows=[planar_gap(rng.permutation(n)) for _ in range(24)]
    results['planar_gaps'][str(n)]=rows
    scaled=[r['n_cubed_gap'] for r in rows if 'n_cubed_gap' in r]
    print(json.dumps({'n':n,'samples':len(rows),'skipped':sum('skipped' in r for r in rows),
        'n3_gap_median':float(np.median(scaled))}),flush=True)
results['source_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in
 [Path(__file__).resolve(),*sorted(ROOT.glob('main.conjectures.c[0-9][0-9].*.current.md'))]}
out=args.output or ROOT/'main.conjectures.analysis.observations.json'
out.write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(str(out),flush=True)

# publish: main.conjectures.analysis.experiments bounded finite evidence producer
# consumer: main.conjectures.c16
# consumer: main.conjectures.c17
# consumer: main.conjectures.c24
