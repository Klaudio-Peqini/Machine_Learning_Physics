import numpy as np

def linear_gd(X,y,lr=0.05,n_iter=1000):
    X=np.asarray(X,float); y=np.asarray(y,float); A=np.c_[np.ones(len(X)),X]
    w=np.zeros(A.shape[1]); hist=[]
    for _ in range(n_iter):
        r=A@w-y; loss=np.mean(r*r); hist.append(loss)
        grad=2*A.T@r/len(y); w-=lr*grad
    return w,np.array(hist)
