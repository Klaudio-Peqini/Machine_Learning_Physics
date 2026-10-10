import numpy as np
def centroid(X): return np.asarray(X,float).mean(axis=0)
def centroid_linkage(A,B): return np.linalg.norm(centroid(A)-centroid(B))
