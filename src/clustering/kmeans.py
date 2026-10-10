import numpy as np
class KMeansFromScratch:
    def __init__(self,n_clusters=3,max_iter=300,tol=1e-6,seed=42):
        self.n_clusters,self.max_iter,self.tol,self.seed=n_clusters,max_iter,tol,seed
    def fit(self,X):
        X=np.asarray(X,float)
        rng=np.random.default_rng(self.seed)
        centers=X[rng.choice(len(X),self.n_clusters,replace=False)].copy()
        for it in range(self.max_iter):
            d2=((X[:,None,:]-centers[None,:,:])**2).sum(axis=2)
            labels=d2.argmin(axis=1)
            new=np.array([X[labels==k].mean(axis=0) if np.any(labels==k) else centers[k] for k in range(self.n_clusters)])
            if np.linalg.norm(new-centers)<self.tol:
                centers=new; break
            centers=new
        self.cluster_centers_,self.labels_,self.n_iter_=centers,labels,it+1
        self.inertia_=((X-centers[labels])**2).sum()
        return self
    def predict(self,X):
        X=np.asarray(X,float)
        return ((X[:,None,:]-self.cluster_centers_[None,:,:])**2).sum(axis=2).argmin(axis=1)
