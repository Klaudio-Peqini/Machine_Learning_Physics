import numpy as np
class PCAFromScratch:
    def __init__(self,n_components=None): self.n_components=n_components
    def fit(self,X):
        X=np.asarray(X,float)
        self.mean_=X.mean(axis=0)
        Xc=X-self.mean_
        self.covariance_=np.cov(Xc,rowvar=False)
        vals,vecs=np.linalg.eigh(self.covariance_)
        idx=np.argsort(vals)[::-1]
        vals,vecs=vals[idx],vecs[:,idx]
        n=self.n_components or X.shape[1]
        self.eigenvalues_=vals
        self.components_=vecs[:,:n].T
        self.explained_variance_ratio_=vals[:n]/vals.sum()
        return self
    def transform(self,X):
        return (np.asarray(X,float)-self.mean_)@self.components_.T
    def inverse_transform(self,Z):
        return np.asarray(Z)@self.components_+self.mean_
    def fit_transform(self,X):
        return self.fit(X).transform(X)
