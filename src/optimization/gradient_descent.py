import numpy as np
def gradient_descent(theta0,grad,lr=0.01,n_iter=1000,tol=1e-10):
    theta=np.asarray(theta0,float).copy()
    history=[theta.copy()]
    for _ in range(n_iter):
        new=theta-lr*np.asarray(grad(theta),float)
        history.append(new.copy())
        if np.linalg.norm(new-theta)<tol:
            theta=new; break
        theta=new
    return theta,np.asarray(history)
