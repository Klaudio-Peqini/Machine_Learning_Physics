import numpy as np

def add_intercept(X):
    X=np.asarray(X,float)
    if X.ndim==1: X=X[:,None]
    return np.c_[np.ones(len(X)),X]

def ols_fit(X,y):
    A=add_intercept(X); y=np.asarray(y,float)
    beta=np.linalg.pinv(A)@y
    return beta

def predict_linear(X,beta):
    return add_intercept(X)@np.asarray(beta)

def ridge_fit(X,y,alpha=1.0):
    A=add_intercept(X); y=np.asarray(y,float)
    I=np.eye(A.shape[1]); I[0,0]=0
    return np.linalg.solve(A.T@A+alpha*I,A.T@y)

def polynomial_design(x,degree):
    x=np.asarray(x,float).ravel()
    return np.column_stack([x**p for p in range(1,degree+1)])
