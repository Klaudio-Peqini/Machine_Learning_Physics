import numpy as np

def sigmoid(z):
    z=np.clip(np.asarray(z,float),-40,40)
    return 1/(1+np.exp(-z))

def logistic_fit_gd(X,y,lr=0.05,n_iter=3000,l2=0.0):
    X=np.asarray(X,float); y=np.asarray(y,float)
    A=np.c_[np.ones(len(X)),X]
    w=np.zeros(A.shape[1]); hist=[]
    for _ in range(n_iter):
        p=sigmoid(A@w)
        grad=A.T@(p-y)/len(y)
        grad[1:]+=l2*w[1:]
        w-=lr*grad
        eps=1e-12
        hist.append(float(-np.mean(y*np.log(p+eps)+(1-y)*np.log(1-p+eps))))
    return w,np.array(hist)

def logistic_predict_proba(X,w):
    X=np.asarray(X,float); A=np.c_[np.ones(len(X)),X]
    return sigmoid(A@w)
