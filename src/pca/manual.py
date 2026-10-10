import numpy as np

def pca_fit(X,n_components=None):
    X=np.asarray(X,float); mean=X.mean(axis=0); Xc=X-mean
    C=np.cov(Xc,rowvar=False)
    vals,vecs=np.linalg.eigh(C); idx=np.argsort(vals)[::-1]
    vals,vecs=vals[idx],vecs[:,idx]
    if n_components is not None: vals,vecs=vals[:n_components],vecs[:,:n_components]
    return mean, vals, vecs

def transform(X,mean,vecs): return (np.asarray(X,float)-mean)@vecs
