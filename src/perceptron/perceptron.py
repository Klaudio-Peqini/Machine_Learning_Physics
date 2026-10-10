import numpy as np
class PerceptronFromScratch:
    def __init__(self,lr=1.0,max_epochs=1000,shuffle=True,seed=42):
        self.lr,self.max_epochs,self.shuffle,self.seed=lr,max_epochs,shuffle,seed
    def fit(self,X,y):
        X=np.asarray(X,float); y=np.asarray(y)
        yt=np.where(y>0,1.0,-1.0)
        self.coef_=np.zeros(X.shape[1]); self.intercept_=0.0
        rng=np.random.default_rng(self.seed)
        self.mistakes_per_epoch_=[]
        for _ in range(self.max_epochs):
            order=np.arange(len(X))
            if self.shuffle: rng.shuffle(order)
            mistakes=0
            for i in order:
                if yt[i]*(X[i]@self.coef_+self.intercept_)<=0:
                    self.coef_+=self.lr*yt[i]*X[i]
                    self.intercept_+=self.lr*yt[i]
                    mistakes+=1
            self.mistakes_per_epoch_.append(mistakes)
            if mistakes==0: break
        self.n_iter_=len(self.mistakes_per_epoch_)
        return self
    def decision_function(self,X):
        return np.asarray(X,float)@self.coef_+self.intercept_
    def predict(self,X):
        return (self.decision_function(X)>=0).astype(int)
