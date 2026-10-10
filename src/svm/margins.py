import numpy as np
def decision_function(X,w,b=0.0):
    return np.asarray(X,float)@np.asarray(w,float)+b
def signed_distance(X,w,b=0.0):
    w=np.asarray(w,float)
    return decision_function(X,w,b)/np.linalg.norm(w)
def geometric_margin(X,y,w,b=0.0):
    return np.min(np.asarray(y,float)*signed_distance(X,w,b))
def hinge_loss(y_true,scores):
    return np.maximum(0.0,1.0-np.asarray(y_true,float)*np.asarray(scores,float))
