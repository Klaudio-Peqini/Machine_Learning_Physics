import numpy as np
def bootstrap_statistic(x,statistic=np.mean,n_boot=1000,seed=42):
    x=np.asarray(x); rng=np.random.default_rng(seed)
    return np.array([statistic(x[rng.integers(0,len(x),size=len(x))]) for _ in range(n_boot)])
