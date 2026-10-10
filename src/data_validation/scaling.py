import numpy as np
class StandardScalerManual:
    def fit(self, X):
        X = np.asarray(X, dtype=float)
        self.mean_ = X.mean(axis=0)
        self.scale_ = X.std(axis=0)
        self.scale_[self.scale_ == 0] = 1.0
        return self
    def transform(self, X):
        return (np.asarray(X, dtype=float) - self.mean_) / self.scale_
    def fit_transform(self, X):
        return self.fit(X).transform(X)
