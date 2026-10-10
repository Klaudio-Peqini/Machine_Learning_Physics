import numpy as np

def fit_perceptron(X,y,lr=1.0,epochs=100,seed=0):
    X=np.asarray(X,float); y=np.asarray(y); yy=np.where(y>0,1,-1)
    w=np.zeros(X.shape[1]); b=0.0; mistakes=[]; rng=np.random.default_rng(seed)
    for _ in range(epochs):
        m=0
        for i in rng.permutation(len(X)):
            if yy[i]*(X[i]@w+b)<=0:
                w+=lr*yy[i]*X[i]; b+=lr*yy[i]; m+=1
        mistakes.append(m)
        if m==0: break
    return w,b,np.asarray(mistakes)
