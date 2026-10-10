import numpy as np

def kmeans(X,k=3,n_iter=100,seed=0):
    X=np.asarray(X,float); rng=np.random.default_rng(seed)
    centers=X[rng.choice(len(X),size=k,replace=False)].copy(); history=[centers.copy()]
    for _ in range(n_iter):
        dist=((X[:,None,:]-centers[None,:,:])**2).sum(axis=2)
        labels=dist.argmin(axis=1)
        new=np.vstack([X[labels==j].mean(axis=0) if np.any(labels==j) else centers[j] for j in range(k)])
        history.append(new.copy())
        if np.allclose(new,centers): centers=new; break
        centers=new
    return labels,centers,history
