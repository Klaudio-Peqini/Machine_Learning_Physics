import numpy as np
def majority_vote(predictions):
    P=np.asarray(predictions)
    out=[]
    for j in range(P.shape[1]):
        labels,counts=np.unique(P[:,j], return_counts=True)
        out.append(labels[np.argmax(counts)])
    return np.asarray(out)
def bootstrap_indices(n_samples, seed=None):
    rng=np.random.default_rng(seed)
    return rng.integers(0,n_samples,size=n_samples)
