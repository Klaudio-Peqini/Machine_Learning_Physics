import numpy as np
def train_valid_test_split(X, y, train_size=0.6, valid_size=0.2, seed=42):
    X, y = np.asarray(X), np.asarray(y)
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(X))
    n_train = int(round(train_size * len(X)))
    n_valid = int(round(valid_size * len(X)))
    i1, i2 = n_train, n_train + n_valid
    return (X[idx[:i1]], y[idx[:i1]], X[idx[i1:i2]], y[idx[i1:i2]], X[idx[i2:]], y[idx[i2:]])
