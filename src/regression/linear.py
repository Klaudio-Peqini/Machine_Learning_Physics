import numpy as np
class LinearRegressionOLS:
    def __init__(self, fit_intercept=True):
        self.fit_intercept = fit_intercept
    def _design(self, X):
        X = np.asarray(X, dtype=float)
        if X.ndim == 1: X = X[:, None]
        return np.column_stack([np.ones(len(X)), X]) if self.fit_intercept else X
    def fit(self, X, y):
        A = self._design(X)
        beta, *_ = np.linalg.lstsq(A, np.asarray(y, dtype=float), rcond=None)
        self.beta_ = beta
        self.intercept_ = beta[0] if self.fit_intercept else 0.0
        self.coef_ = beta[1:] if self.fit_intercept else beta
        return self
    def predict(self, X):
        return self._design(X) @ self.beta_
    def residuals(self, X, y):
        return np.asarray(y, dtype=float) - self.predict(X)
