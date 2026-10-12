"""Rebuild the public mathematical atlas. All synthetic panels are labeled.

Seeded toy constructions illustrate definitions, not asymptotic evidence.
C17 and C24 alone plot the saved experimental observations.
"""
from pathlib import Path
from collections import deque
from functools import lru_cache
import hashlib
import html
import json
import math
import textwrap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
ATLAS = ROOT / 'docs' / 'atlas'
CATALOG = json.loads((ROOT / 'tools/catalog.json').read_text(encoding='utf-8'))
OBS = json.loads((ROOT / 'main.conjectures.analysis.observations.json').read_text())
BG, PANEL, INK, MUTED = '#101724', '#182337', '#edf4f7', '#acbcd0'
MINT, BLUE, GOLD, PURPLE, RED = '#63e6c5', '#77b7ff', '#ffca7a', '#b4a4ff', '#ff8686'
CMAP = LinearSegmentedColormap.from_list('conj', [PANEL, '#365b80', MINT])
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
    'text.color': INK, 'axes.labelcolor': MUTED, 'xtick.color': MUTED,
    'ytick.color': MUTED, 'axes.edgecolor': '#455469', 'axes.facecolor': BG,
    'figure.facecolor': BG, 'savefig.facecolor': BG, 'axes.titlecolor': INK,
    'svg.hashsalt': 'conj-atlas-20261012', 'svg.fonttype': 'none',
    'axes.spines.top': False, 'axes.spines.right': False})


def axis(fig, rect=(.08, .25, .85, .49), off=False):
    ax = fig.add_axes(rect)
    if off:
        ax.set_axis_off()
    else:
        ax.tick_params(labelsize=9)
        ax.grid(alpha=.1, color=MUTED)
        ax.set_axisbelow(True)
    return ax


def figure(item):
    fig = plt.figure(figsize=(12, 6.6))
    fig.text(.065, .92, item['id'] + '  /  ' + item['area'].upper(),
             color=MINT, fontsize=10, weight='bold')
    fig.text(.065, .84, item['title'], fontsize=23, weight='bold')
    fig.text(.935, .922, item['status'].upper(), fontsize=8, color=GOLD, ha='right')
    fig.text(.065, .065, '\n'.join(textwrap.wrap(item['visual'], 132)),
             color=MUTED, fontsize=9, linespacing=1.6)
    fig.text(.935, .025, 'CONJ  /  A PUBLIC MATHEMATICAL NOTEBOOK',
             ha='right', color=MUTED, fontsize=7)
    return fig


def save(fig, name, description):
    fig.savefig(ASSETS / (name + '.png'), dpi=140,
                metadata={'Description': description})
    fig.savefig(ASSETS / (name + '.svg'),
                metadata={'Date': None, 'Description': description})
    svg = ASSETS / (name + '.svg')
    svg.write_bytes(('\n'.join(line.rstrip() for line in svg.read_text(encoding='utf-8').splitlines()).rstrip()+'\n').encode('utf-8'))
    plt.close(fig)


def ring(n):
    t = np.arange(n) * 2 * np.pi / n + np.pi / 2
    return np.c_[np.cos(t), np.sin(t)]


def graph(ax, pos, edges, active=None, highlights=(), labels=False):
    active = set(range(len(pos))) if active is None else set(active)
    h = {tuple(sorted(e)) for e in highlights}
    for i, j in edges:
        alive = i in active and j in active
        highlight = tuple(sorted((i, j))) in h
        ax.plot(pos[[i, j], 0], pos[[i, j], 1],
                color=GOLD if highlight else BLUE if alive else '#2a3547',
                lw=3 if highlight else 1.1, alpha=1 if highlight else .55, zorder=1)
    for i, p in enumerate(pos):
        ax.scatter(*p, s=120, color=MINT if i in active else '#384052', zorder=3)
        if labels:
            ax.text(*(p * 1.2), str(i), fontsize=9, ha='center', va='center')
    ax.set_aspect('equal'); ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.35, 1.35)
    ax.set_axis_off()


def draw(item):
    k = int(item['id'][1:]); rng = np.random.default_rng(20261012 + k)
    fig = figure(item)
    if k == 1:
        ax = axis(fig, off=True); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        boxes = [('FEW QUERIES', 'Exact algorithm\nwith cost $R_0$'),
                 ('LITTLE LEVEL-ONE MASS', '$\\sum I_i^2 \\leq 2\\tau\\sqrt{R_0}$'),
                 ('NOISE SENSITIVITY', 'BKS criterion\ncorrelation vanishes')]
        for i, (title, body) in enumerate(boxes):
            x = .015 + i * .34
            ax.add_patch(Rectangle((x, .25), .285, .55, facecolor=PANEL, edgecolor=MINT, lw=1.3))
            ax.text(x+.142, .67, title, ha='center', fontsize=9, color=MINT, weight='bold')
            ax.text(x+.142, .47, body, ha='center', va='center', fontsize=13, linespacing=1.8)
            if i < 2:
                ax.add_patch(FancyArrowPatch((x+.292, .5), (x+.337, .5), arrowstyle='->', mutation_scale=20, color=GOLD))
        ax.text(.5, .06, 'An honest outcome: a candidate becomes a worked theorem consequence.', ha='center', color=MUTED)
    elif k == 2:
        ax = axis(fig, (.08, .23, .84, .53), off=True)
        nx, ny = 19, 9
        pos = np.array([(x + .5*(y%2), y*.866) for y in range(ny) for x in range(nx)])
        opened = rng.random(nx*ny)<.5
        opened[4*nx:5*nx] = True
        edges = [(i,j) for i in range(len(pos)) for j in range(i)
                 if abs(np.linalg.norm(pos[i]-pos[j])-1)<.002]
        adj = [[] for _ in pos]
        for i,j in edges:
            ax.plot(pos[[i,j],0], pos[[i,j],1], color='#29354a', lw=.6)
            if opened[i] and opened[j]: adj[i].append(j); adj[j].append(i)
        start=[i for i in range(len(pos)) if i%nx==0 and opened[i]]
        queue=deque(start); parent={i:None for i in start}; target=None
        while queue:
            i=queue.popleft()
            if i%nx==nx-1: target=i; break
            for j in adj[i]:
                if j not in parent: parent[j]=i; queue.append(j)
        path=[]
        while target is not None: path.append(target); target=parent[target]
        ax.scatter(pos[:,0], pos[:,1], c=[BLUE if v else '#263044' for v in opened], s=45)
        ax.plot(pos[path,0],pos[path,1], color=GOLD,lw=3,marker='o',ms=5)
        ax.set_aspect('equal'); ax.text(.5, -.11, 'OPEN SITES  /  SHORTEST LEFT–RIGHT WITNESS', transform=ax.transAxes, ha='center', color=GOLD, fontsize=10)
    elif k == 3:
        t=np.geomspace(.1,1000,220); c=.2*(1+t)**(-2/3)
        a=axis(fig,(.09,.27,.36,.46)); b=axis(fig,(.58,.27,.34,.46))
        a.loglog(t,c,color=BLUE,lw=3); a.set(xlabel='time t',ylabel='illustrative covariance')
        b.semilogx(t,t**(2/3)*c,color=MINT,lw=3); b.axhline(.2,color=GOLD,ls='--',lw=1.5)
        b.set(xlabel='time t',ylabel=r'$t^{2/3} C(t)$',ylim=(0,.23))
        b.text(.04,.95,'A finite, positive amplitude?',transform=b.transAxes,fontsize=10,color=GOLD)
    elif k == 4:
        x=np.linspace(-6,6,240); y=1/(1+np.exp(-x)); d=y*(1-y)
        a=axis(fig,(.09,.27,.36,.46)); b=axis(fig,(.58,.27,.34,.46))
        a.plot(x,y,color=MINT,lw=3); a.set(xlabel='near-critical parameter (toy)',ylabel='crossing-profile schematic')
        b.plot(x,d,color=BLUE,lw=2,label='first derivative'); b.plot(x,d*(1-2*y),color=GOLD,lw=2,label='second derivative')
        b.axhline(0,color=MUTED,lw=.5); b.set(xlabel='parameter',ylabel='toy derivatives'); b.legend(frameon=False,labelcolor=INK,fontsize=9)
    elif k == 5:
        n=32; h=rng.normal(size=(n,n))/np.sqrt(2*n); h=h+h.T; u=np.ones(n)/np.sqrt(n)
        x=np.linspace(0,2,110); val=[]; deriv=[]
        for w in x:
            e,v=np.linalg.eigh(h+w*np.outer(u,u)); val.append(e[-1]); deriv.append((v[:,-1]@u)**2)
        a=axis(fig,(.09,.27,.36,.46)); b=axis(fig,(.58,.27,.34,.46))
        a.plot(x,val,color=BLUE,lw=3); a.set(xlabel='spike strength',ylabel='top eigenvalue (one toy matrix)')
        b.plot(x,deriv,color=MINT,lw=3); b.set(xlabel='spike strength',ylabel='squared overlap / derivative')
    elif k == 6:
        a=axis(fig,(.1,.24,.31,.5),off=True); a.set(xlim=(-1.2,1.3),ylim=(-1.1,1.2)); a.set_aspect('equal')
        t=np.linspace(0,2*np.pi,160); a.plot(np.cos(t),np.sin(t),color='#42516a',lw=1)
        for angle,c,label in [(0,BLUE,'v(0)'),(.7,MINT,'v(s)'),(1.3,GOLD,'v(t)')]:
            p=np.array([np.cos(angle),np.sin(angle)])
            a.add_patch(FancyArrowPatch((0,0),p,arrowstyle='->',mutation_scale=22,color=c,lw=3))
            a.text(*(p*1.15),label,color=c,fontsize=12,ha='center')
        a.text(0,-1.2,r'$Q(s,t)=|\langle v(s),v(t)\rangle|^2$',ha='center',fontsize=13)
        b=axis(fig,(.53,.25,.34,.49)); t=np.linspace(0,1.6,80)
        im=b.imshow(np.cos(t[:,None]-t[None,:])**2,cmap=CMAP,origin='lower',extent=(0,1.6,0,1.6),vmin=0,vmax=1)
        b.grid(False); b.set(xlabel='time s (toy)',ylabel='time t (toy)'); fig.colorbar(im,ax=b,fraction=.045,pad=.04)
    elif k == 7:
        n=14; pos=ring(n); edges=sorted({tuple(sorted((i,(i+d)%n))) for i in range(n) for d in (1,4)})
        keep=[0,1,2,4,5,7,8,9,11,12,13]
        a=axis(fig,(.03,.27,.3,.47),off=True); b=axis(fig,(.34,.27,.3,.47),off=True)
        graph(a,pos,edges); graph(b,pos,edges,active=keep)
        a.set_title('A regular toy graph',fontsize=12); b.set_title('Retain vertices, recompute degrees',fontsize=11)
        A=np.zeros((len(keep),len(keep))); loc={v:i for i,v in enumerate(keep)}
        for i,j in edges:
            if i in loc and j in loc: A[loc[i],loc[j]]=A[loc[j],loc[i]]=1
        deg=A.sum(0); inv=np.divide(1,np.sqrt(deg),out=np.zeros_like(deg),where=deg>0)
        ev=np.linalg.eigvalsh(inv[:,None]*A*inv[None,:])
        c=axis(fig,(.71,.31,.22,.36)); c.axhline(0,color=MUTED,lw=1)
        c.scatter(ev,np.zeros_like(ev),color=BLUE,s=55); c.scatter([ev[0],ev[-2]],[0,0],color=GOLD,s=100)
        c.annotate('lower edge', (ev[0],0),xytext=(-1,.3),color=GOLD,fontsize=9,arrowprops={'arrowstyle':'->','color':GOLD})
        c.annotate('upper\nnontrivial', (ev[-2],0),xytext=(.08,-.44),color=GOLD,fontsize=9,arrowprops={'arrowstyle':'->','color':GOLD})
        c.text(ev[-1],.12,'1',ha='center',color=MUTED); c.set(xlim=(-1.1,1.15),ylim=(-.65,.65),yticks=[],xlabel='normalized spectrum')
    elif k == 8:
        a=rng.random((8,8))<.27; snapshots=[a.copy()]
        for _ in range(4):
            p=np.pad(a.astype(int),1); counts=p[:-2,1:-1]+p[2:,1:-1]+p[1:-1,:-2]+p[1:-1,2:]
            a=a|(counts>=2); snapshots.append(a.copy())
        for j,t in enumerate((0,2,4)):
            ax=axis(fig,(.07+j*.31,.26,.24,.48),off=True)
            ax.imshow(snapshots[t],cmap=ListedColormap([PANEL,MINT]),vmin=0,vmax=1)
            ax.set_title(f'toy step {t}',fontsize=12)
    elif k == 9:
        pos=ring(10); edges=[(i,(i+1)%10) for i in range(10)]+[(0,2),(2,6),(4,8)]
        a=axis(fig,(.07,.22,.4,.55),off=True); b=axis(fig,(.53,.22,.4,.55),off=True)
        graph(a,pos,edges,highlights=[(i,i+1) for i in range(9)]); a.set_title('One spanning tree',fontsize=12)
        graph(b,pos,edges,highlights=[(0,1),(1,2),(2,0)]); b.set_title('Condition on short-cycle information',fontsize=12)
    elif k == 10:
        a=axis(fig,(.13,.25,.74,.49)); x,y=rng.normal(size=(2,250))
        a.scatter(x,y,c=MINT,s=22,alpha=.55,edgecolors='none')
        a.axhline(0,color=MUTED,lw=.6); a.axvline(0,color=MUTED,lw=.6)
        a.set(xlabel='synthetic mixing residual',ylabel='synthetic tree-entropy residual',xlim=(-3.3,3.3),ylim=(-3.3,3.3))
        a.text(.02,.94,'THE PROPOSED PRODUCT LAW, ILLUSTRATED',transform=a.transAxes,color=GOLD,fontsize=9)
    elif k == 11:
        pos=ring(9)
        for j,count in enumerate((2,3)):
            a=axis(fig,(.08+j*.46,.24,.36,.5),off=True)
            graph(a,pos,[],active=range(3*count))
            for t in range(count): a.add_patch(Polygon(pos[3*t:3*t+3],facecolor=MINT,edgecolor=MINT,alpha=.3,lw=2))
            a.set_title('Before: isolated vertices' if count==2 else 'After: a perfect matching',fontsize=12)
        fig.text(.5,.2,'Do both events share the same clock?',ha='center',color=GOLD,fontsize=13)
    elif k == 12:
        pos=ring(3)
        for j in range(2):
            a=axis(fig,(.08+j*.46,.23,.36,.51),off=True)
            if j: a.add_patch(Polygon(pos,facecolor=MINT,alpha=.3))
            graph(a,pos,[(0,1),(1,2),(2,0)],highlights=[(0,1),(1,2),(2,0)])
            a.set_title('Cycle without a filling' if j==0 else 'A face fills this toy cycle',fontsize=12)
    elif k == 13:
        n=7; grid=(np.arange(n)[:,None]+np.arange(n)[None,:])%n
        a=axis(fig,(.1,.24,.43,.52)); a.imshow(grid,cmap=CMAP,vmin=-2,vmax=9); a.grid(False)
        for r in range(n):
            for c in range(n):
                a.text(c,r,str(grid[r,c]),ha='center',va='center',fontsize=13,color=INK)
            a.add_patch(Rectangle((r-.45,r-.45),.9,.9,fill=False,edgecolor=GOLD,lw=2.5))
            c=(r+1)%n; a.plot([c-.3,c+.3],[r-.3,r+.3],c=RED,lw=3); a.plot([c-.3,c+.3],[r+.3,r-.3],c=RED,lw=3)
        a.set(xlabel='column',ylabel='row',xticks=range(n),yticks=range(n))
        b=axis(fig,(.58,.27,.34,.43),off=True)
        b.text(0,.85,'7 ROWS  ·  7 COLUMNS  ·  7 SYMBOLS',color=MINT,fontsize=10,weight='bold')
        b.text(0,.59,'Gold: one surviving transversal\nRed: one deletion per coordinate',fontsize=13,linespacing=1.8)
        b.text(0,.15,'The challenge:\nevery allowed attack,\non a typical random square.',fontsize=16,linespacing=1.5,color=GOLD)
    elif k == 14:
        pos=np.array([(x,y) for x in (-1,1) for y in np.linspace(-1,1,5)])
        edges=[(i,5+j) for i in range(5) for j in (i,(i+1)%5,(i+2)%5)]
        a=axis(fig,(.07,.25,.4,.5),off=True); graph(a,pos,edges,highlights=[(0,5),(5,4),(4,6),(6,1)])
        b=axis(fig,(.57,.28,.34,.43),off=True)
        for i,(col,label) in enumerate([(BLUE,'left-side cover clock'),(GOLD,'right-side cover clock')]):
            y=.75-i*.45; b.plot([.05,.95],[y,y],color=col,lw=2)
            b.scatter([.18,.34,.52,.67,.87],[y]*5,color=col,s=[30,30,30,30,100])
            b.text(.05,y+.12,label,color=col,fontsize=12)
        b.text(.05,-.12,'Joint independence is the question.',fontsize=11,color=MUTED)
    elif k == 15:
        n,r=14,18; theta=np.linspace(-1,1,n); u=np.sin(np.arange(n)); v=np.cos(np.arange(r)); v-=v.mean()
        matrix=theta[:,None]+u[:,None]*v[None,:]; masked=np.ma.array(matrix,mask=rng.random((n,r))<.4)
        cm=CMAP.copy(); cm.set_bad('#32394a')
        a=axis(fig,(.08,.27,.4,.47)); a.imshow(masked,cmap=cm,aspect='auto'); a.grid(False)
        a.set(xlabel='observation contexts',ylabel='rows / subjects',xticks=[],yticks=[])
        a.set_title('Toy low-rank signal, 40% missing in expectation',fontsize=10)
        b=axis(fig,(.61,.27,.31,.47)); x=np.linspace(-3,5,200); b.plot(x,np.exp(-np.exp(-x)),color=MINT,lw=3)
        b.set(xlabel='normalized maximum error x',ylabel='proposed limiting CDF',ylim=(0,1.05))
        b.text(.45,.13,r'$\exp(-e^{-x})$',transform=b.transAxes,color=GOLD,fontsize=18)
    elif k == 16:
        n=60; chosen=np.sort(rng.choice(n,15,replace=False)); sums={int(i+j) for i in chosen for j in chosen}
        a=axis(fig,(.08,.29,.84,.41)); a.scatter(chosen,np.ones(len(chosen)),color=MINT,s=50)
        missing=[i for i in range(2*n-1) if i not in sums]
        a.scatter(sorted(sums),np.zeros(len(sums)),color=BLUE,s=25)
        a.scatter(missing,np.zeros(len(missing)),color=RED,s=32,marker='x')
        a.set(yticks=[0,1],yticklabels=['A + A','A'],ylim=(-.5,1.5),xlabel='integer position')
        a.text(.5,.88,'PRESENT SUMS / MISSING SUMS',transform=a.transAxes,color=MUTED,fontsize=10)
    elif k == 17:
        rows=OBS['sumsets']; labels=[str(r['q']) for r in rows]; x=np.arange(len(rows))
        a=axis(fig,(.09,.28,.36,.46)); b=axis(fig,(.59,.28,.33,.46))
        a.plot(x,[r['full_scaled_variance'] for r in rows],color=MINT,lw=2,marker='o',ms=9)
        a.axhline(8,color=GOLD,ls='--',label='proposed limit 8'); a.set(xticks=x,xticklabels=labels,ylim=(7.2,8.25),xlabel='inclusion probability q',ylabel=r'$q^3$ × sample variance of full deficit')
        a.legend(frameon=False,labelcolor=GOLD,fontsize=9,loc='lower left')
        b.bar(x,[r['residual_scaled_variances'][-1] for r in rows],color=BLUE,width=.5)
        b.set(xticks=x,xticklabels=labels,xlabel='inclusion probability q',ylabel='scaled projection residual variance at u=4')
        b.text(.97,.93,'1,200 samples / q',transform=b.transAxes,ha='right',color=MINT,fontsize=10)
    elif k == 18:
        p=17; chosen=np.array([0,1,3,6,8,11]); counts=np.zeros(p,dtype=int)
        for i in chosen:
            for j in chosen: counts[(i+j)%p]+=1
        a=axis(fig,(.09,.27,.61,.46)); a.bar(range(p),counts,color=BLUE,width=.65)
        a.set(xlabel='sum modulo 17',ylabel='ordered representation count',xticks=range(0,p,2))
        fig.text(.77,.56,'ENERGY',color=MINT,fontsize=12); fig.text(.77,.45,str(int(counts@counts)),fontsize=36,color=GOLD,weight='bold')
        fig.text(.77,.35,r'$\sum_s r(s)^2$',fontsize=20)
    elif k == 19:
        p=53; order=rng.permutation(p); arrivals={}
        for j in range(1,p+1):
            for z in order[:j-1]:
                d=int((order[j-1]-z)%p); d=min(d,p-d); arrivals.setdefault(d,j)
        x=np.array([arrivals[d] for d in range(1,(p+1)//2)])
        a=axis(fig,(.09,.27,.83,.46)); a.scatter(x,range(1,len(x)+1),c=MINT,s=45)
        for i,v in enumerate(x): a.plot([0,v],[i+1,i+1],color=BLUE,alpha=.25,lw=1)
        a.set(xlabel='number of inserted residues at first witness',ylabel='unoriented difference class',xlim=(0,max(x)+1))
    elif k == 20:
        p=101; a0=np.zeros(p,dtype=int); a0[rng.choice(p,30,replace=False)]=1
        d=np.arange(1,(p+1)//2); vals=np.array([a0@np.roll(a0,int(k)) for k in d]); peak=int(np.argmax(vals))
        a=axis(fig,(.09,.27,.83,.46)); a.bar(d,vals,color=BLUE,width=.65); a.bar(d[peak],vals[peak],color=GOLD,width=.75)
        a.set(xlabel='unoriented shift',ylabel='set overlap'); a.annotate('largest overlap',xy=(d[peak],vals[peak]),xytext=(d[peak]+3,vals[peak]+1),color=GOLD,arrowprops={'arrowstyle':'->','color':GOLD},fontsize=11)
        a.set_ylim(0,max(vals)+3)
    elif k in (21,22):
        p=np.array([2,7,3,9,5,1,8,4,6,10]); x=np.arange(len(p))
        if k==21:
            a=axis(fig,(.09,.27,.83,.46)); a.plot(x,p,color=BLUE,lw=1.5,marker='o',ms=8)
            peaks=[i for i in range(1,len(p)-1) if p[i]>p[i-1] and p[i]>p[i+1]]
            a.scatter(peaks,p[peaks],marker='^',color=GOLD,s=160,zorder=4)
            witness=[0,1,2]; a.plot(x[witness],p[witness],color=MINT,lw=3,alpha=.7)
            a.set(xlabel='position',ylabel='permutation value',xticks=x)
            a.text(.02,.96,'TRIANGLES: PEAKS   /   MINT: A 132 WITNESS',transform=a.transAxes,color=GOLD,fontsize=9)
        else:
            q=p.copy(); sites=[1,5,8]; q[sites]=q[sites[::-1]]
            for j,v in enumerate((p,q)):
                a=axis(fig,(.08+j*.46,.27,.37,.46)); a.plot(x,v,color=BLUE,lw=1,marker='o')
                desc=np.flatnonzero(v[:-1]>v[1:])
                for d in desc: a.plot(x[d:d+2],v[d:d+2],color=GOLD,lw=3)
                a.scatter(sites,v[sites],color=MINT,s=80,zorder=4)
                a.set(xlabel='position',ylabel='value',title='original' if j==0 else 'sparse reshuffle',xticks=[0,3,6,9])
    elif k == 23:
        p=np.array([2,5,0,4,1,6,3]); n=len(p)
        pred=[sum(1<<j for j in range(i) if p[j]<p[i]) for i in range(n)]
        @lru_cache(None)
        def count(mask):
            if mask==(1<<n)-1:return 1
            return sum(count(mask|(1<<i)) for i in range(n) if not(mask>>i&1) and pred[i]&mask==pred[i])
        a=axis(fig,(.09,.27,.51,.46)); a.scatter(range(n),p,color=MINT,s=110,zorder=4)
        for i in range(n):
            for j in range(i+1,n):
                if p[i]<p[j] and not any(p[i]<p[z]<p[j] for z in range(i+1,j)):
                    a.annotate('',(j,p[j]),(i,p[i]),arrowprops={'arrowstyle':'->','color':BLUE,'alpha':.6})
        a.set(xlabel='first coordinate',ylabel='second coordinate',xticks=range(n),yticks=range(n))
        fig.text(.68,.6,'LEGAL TOTAL ORDERS',color=MINT,fontsize=11)
        fig.text(.68,.45,str(count(0)),color=GOLD,fontsize=46,weight='bold')
        fig.text(.68,.31,'Exact enumeration\nof this seven-point example',color=MUTED,fontsize=12,linespacing=1.7)
    elif k == 24:
        a=axis(fig,(.1,.28,.8,.45)); samples=[]
        for j,(n,rows) in enumerate(OBS['planar_gaps'].items()):
            vals=[r['n_cubed_gap'] for r in rows if 'n_cubed_gap' in r]; samples.append(vals)
            jitter=rng.uniform(-.13,.13,len(vals)); a.scatter(j+jitter,vals,color=BLUE if n!='10' else GOLD,alpha=.8,s=30)
            a.plot([j-.2,j+.2],[np.median(vals)]*2,color=MINT,lw=3)
        a.set(xticks=[0,1,2],xticklabels=['n=6\n24 / 24','n=8\n24 / 24','n=10\n18 / 24 computed'],ylabel=r'$n^3$ × spectral gap',xlabel='actual random planar-order samples')
        a.text(.98,.94,'Mint bars: sample medians\nGold: censored size group',ha='right',va='top',transform=a.transAxes,color=MUTED,fontsize=10)
    elif k == 25:
        x=np.linspace(.015,1.985,220); t=x/2; lower=-2*(t*np.log(t)+(1-t)*np.log(1-t)); upper=2*x*(1-np.log(x))
        a=axis(fig,(.1,.27,.81,.46)); a.fill_between(x,lower,upper,color=BLUE,alpha=.2)
        a.plot(x,lower,color=MINT,lw=2.5,label='LIS witness lower bound'); a.plot(x,upper,color=GOLD,lw=2.5,label='first-moment upper bound')
        a.set(xlabel=r'target length parameter $\alpha$',ylabel='possible limiting entropy',xlim=(0,2),ylim=(0,2.25)); a.legend(frameon=False,labelcolor=INK,fontsize=10)
    save(fig,item['id'].lower(),item['visual'])


def hero():
    fig=plt.figure(figsize=(16,5.6)); ax=fig.add_axes([0,0,1,1]); ax.set_axis_off(); ax.set(xlim=(0,16),ylim=(0,5.6))
    rng=np.random.default_rng(25); points=np.c_[rng.uniform(9.3,15.5,25),rng.uniform(.65,4.9,25)]
    priority={2,5,6,12,14,16}
    for i,p in enumerate(points):
        near=np.argsort(np.linalg.norm(points-p,axis=1))[1:3]
        for j in near: ax.plot(points[[i,j],0],points[[i,j],1],color=BLUE,alpha=.19,lw=1.3)
    for i,p in enumerate(points):
        ax.scatter(*p,s=160 if i in priority else 60,color=GOLD if i in priority else MINT,alpha=.9,zorder=3)
        if i in priority: ax.text(p[0]+.13,p[1]+.16,f'C{i+1:02}',fontsize=9,color=GOLD)
    ax.text(.8,4.8,'A PUBLIC MATHEMATICAL NOTEBOOK',color=MINT,fontsize=13,weight='bold')
    ax.text(.72,2.8,'conj',fontsize=116,weight='bold')
    ax.text(.85,2.02,'25 questions. Bring a proof. Bring a counterexample.',fontsize=18)
    ax.text(.85,1.2,'Probability  /  Combinatorics  /  Spectra  /  Statistics',fontsize=12,color=MUTED)
    ax.text(.85,.57,'6 priority leads     ·     1 known consequence     ·     novelty under review',fontsize=11,color=GOLD)
    save(fig,'hero','25 candidate slots, with six research priorities; novelty and unresolved status require independent review.')


def cards(items, prefix=''):
    lines=['<table>']
    for start in range(0,len(items),2):
        lines.append('<tr>')
        for item in items[start:start+2]:
            ident=item['id']; doc=f'{prefix}docs/atlas/{ident.lower()}.md'; img=f'{prefix}assets/{ident.lower()}.png'
            lines.append(f'<td width="50%" valign="top"><a href="{doc}"><img src="{img}" alt="{html.escape(ident+": "+item["visual"],quote=True)}" width="480"></a><br><strong><a href="{doc}">{ident} · {html.escape(item["title"])}</a></strong><br>{html.escape(item["question"])}<br><sub>{html.escape(item["status"])}</sub></td>')
        if len(items[start:start+2])==1: lines.append('<td></td>')
        lines.append('</tr>')
    lines.append('</table>')
    return '\n'.join(lines)


def pages():
    atlas=['# The conjecture atlas','', 'Every card links to an introduction, an image, the exact statement, and the next review question.', '',
        '**Status:** C01 is a known-theorem consequence. The other 24 are unresolved in this project; none is certified novel. Illustrations have explicit provenance captions.', '',
        '[Back to the project](../../README.md)', '', '| ID | Question | Area | Review status |', '|---|---|---|---|']
    for item in CATALOG:
        ident=item['id']; source=next(ROOT.glob(f'main.conjectures.{ident.lower()}.*.current.md')).name
        atlas.append(f'| [{ident}]({ident.lower()}.md) | {item["title"]} | {item["area"]} | {item["status"]} |')
        extra=''
        if ident=='C01': extra='\n[Read the completed implication proof](../../main.conjectures.analysis.c01.complete.md).\n'
        if ident in ('C17','C24'): extra+='\n[Recorded data](../../main.conjectures.analysis.observations.json) · [Experiment producer](../../main.conjectures.analysis.experiments.py)\n'
        if ident=='C02': extra+='\nLiterature update: [chemical-metric scaling, arXiv:2604.14122](https://arxiv.org/abs/2604.14122). This is substantial overlap; an exact statement comparison remains necessary.\n'
        page=f'''# {ident} · {item['title']}

**{item['area']} · {item['status']}**

{item['question']}

![{item['visual']}](../../assets/{ident.lower()}.png)

*Figure provenance: {item['visual']}* [Vector version](../../assets/{ident.lower()}.svg).

{item['detail']}

**Next mathematical step:** {item['next']}

[Read the exact statement](../../{source}) · [Review notebook](../../main.conjectures.analysis.notes.current.md) · [Contribute](../../CONTRIBUTING.md)
{extra}
The exact hypotheses, definitions, quantifiers, and normalization are in the linked statement. This introduction does not replace them. A priority tag is an editorial judgment; unresolved means unresolved by this project, not verified open in the literature.

[All 25 candidates](README.md) · [Project home](../../README.md)

<!-- consumer: main.conjectures.{ident.lower()} -->
<!-- publish: main.conjectures.atlas.{ident.lower()} public illustrated introduction -->
'''
        (ATLAS/(ident.lower()+'.md')).write_text(page,encoding='utf-8')
    (ATLAS/'README.md').write_text('\n'.join(atlas)+'\n',encoding='utf-8')
    readme=ROOT/'README.md'
    if readme.exists():
        s=readme.read_text(encoding='utf-8')
        for name,items in [('PRIORITY',[c for c in CATALOG if c['status'].startswith('Priority')]),('OTHERS',[c for c in CATALOG if not c['status'].startswith('Priority')])]:
            begin=f'<!-- BEGIN {name} -->'; end=f'<!-- END {name} -->'
            before,rest=s.split(begin,1); _,after=rest.split(end,1)
            s=before+begin+'\n'+cards(items)+'\n'+end+after
        readme.write_text(s,encoding='utf-8')


def main():
    ASSETS.mkdir(exist_ok=True); ATLAS.mkdir(parents=True,exist_ok=True)
    hero()
    for item in CATALOG: draw(item)
    pages()
    inputs=['tools/build_atlas.py','tools/catalog.json','main.conjectures.analysis.observations.json']
    manifest={'seed_base':20261012,'matplotlib':matplotlib.__version__,'numpy':np.__version__,
              'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
              'figures':{c['id']:{'kind':'recorded finite data' if c['id'] in ('C17','C24') else 'illustration / analytic construction', 'caption':c['visual']} for c in CATALOG}}
    (ASSETS/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('Built 25 illustrated introductions, 26 PNG/SVG pairs, and their provenance manifest.')


if __name__=='__main__': main()

# publish: main.conjectures.atlas reproducible public visual atlas
# consumer: main.conjectures.analysis.experiments
