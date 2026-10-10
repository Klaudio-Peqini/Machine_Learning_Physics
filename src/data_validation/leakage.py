import numpy as np
def center_using_train(X_train, X_other):
    mu = np.asarray(X_train, dtype=float).mean(axis=0)
    return np.asarray(X_other, dtype=float) - mu, mu
