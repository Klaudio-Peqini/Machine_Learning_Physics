import numpy as np

def gini(y):
    y=np.asarray(y)
    if len(y)==0: return 0.0
    _,c=np.unique(y,return_counts=True); p=c/c.sum()
    return float(1-(p*p).sum())

def split_gain(y,left_mask):
    y=np.asarray(y); left_mask=np.asarray(left_mask,bool)
    parent=gini(y); nl=left_mask.sum(); nr=len(y)-nl
    if nl==0 or nr==0: return 0.0
    child=(nl*gini(y[left_mask])+nr*gini(y[~left_mask]))/len(y)
    return parent-child
