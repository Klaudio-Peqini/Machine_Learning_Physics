import numpy as np

def accuracy(y,p):
    y=np.asarray(y); p=np.asarray(p); return float(np.mean(y==p))
