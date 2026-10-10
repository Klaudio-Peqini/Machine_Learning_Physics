import numpy as np
def sigmoid(z):
    z = np.asarray(z, dtype=float)
    return 1.0/(1.0+np.exp(-np.clip(z, -500, 500)))

class LogisticRegressionGD:
    def __init__(self, lr=0.1, n_iter=2000, l2=0.0):
        self.lr, self.n_iter, self.l2 = lr, n_iter, l2
    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        if X.ndim == 1: X = X[:,None]
        A = np.column_stack([np.ones(len(X)), X])
        y = np.asarray(y, dtype=float)
        w = np.zeros(A.shape[1])
        self.loss_history_ = []
        for _ in range(self.n_iter):
            p = sigmoid(A@w)
            reg = self.l2*w; reg[0] = 0.0
            w -= self.lr * (A.T@(p-y)/len(y) + reg/len(y))
            eps = 1e-12
            self.loss_history_.append(-(y*np.log(p+eps)+(1-y)*np.log(1-p+eps)).mean())
        self.weights_, self.intercept_, self.coef_ = w, w[0], w[1:]
        return self
    def predict_proba(self, X):
        X = np.asarray(X, dtype=float)
        if X.ndim == 1: X = X[:,None]
        A = np.column_stack([np.ones(len(X)), X])
        p1 = sigmoid(A@self.weights_)
        return np.c_[1-p1, p1]
    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X)[:,1] >= threshold).astype(int)
