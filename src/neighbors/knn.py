import numpy as np
class KNNClassifier:
    def __init__(self, k=5): self.k = int(k)
    def fit(self, X, y):
        self.X_, self.y_ = np.asarray(X, dtype=float), np.asarray(y)
        return self
    def predict_one(self, x):
        d = np.linalg.norm(self.X_ - np.asarray(x, dtype=float), axis=1)
        idx = np.argsort(d)[:self.k]
        labels, counts = np.unique(self.y_[idx], return_counts=True)
        return labels[np.argmax(counts)]
    def predict(self, X):
        return np.array([self.predict_one(x) for x in np.asarray(X, dtype=float)])
