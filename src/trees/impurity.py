import numpy as np
def _p(y):
    _, c = np.unique(y, return_counts=True)
    return c/c.sum()
def gini_impurity(y):
    p = _p(np.asarray(y)); return 1-np.sum(p*p)
def entropy(y):
    p = _p(np.asarray(y)); return -np.sum(p*np.log2(p+1e-15))
def information_gain(parent,left,right,criterion="entropy"):
    f = entropy if criterion=="entropy" else gini_impurity
    n=len(parent)
    return f(parent)-len(left)/n*f(left)-len(right)/n*f(right)
