import numpy as np
def polynomial_design_matrix(x, degree, include_bias=True):
    x = np.asarray(x, dtype=float).reshape(-1)
    start = 0 if include_bias else 1
    return np.column_stack([x**p for p in range(start, degree+1)])

class RidgeRegression:
    def __init__(self, alpha=1.0, fit_intercept=True):
        self.alpha, self.fit_intercept = float(alpha), fit_intercept
    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        if X.ndim == 1: X = X[:, None]
        A = np.column_stack([np.ones(len(X)), X]) if self.fit_intercept else X
        P = np.eye(A.shape[1])
        if self.fit_intercept: P[0,0] = 0.0
        self.beta_ = np.linalg.solve(A.T@A + self.alpha*P, A.T@np.asarray(y, dtype=float))
        self.intercept_ = self.beta_[0] if self.fit_intercept else 0.0
        self.coef_ = self.beta_[1:] if self.fit_intercept else self.beta_
        return self
    def predict(self, X):
        X = np.asarray(X, dtype=float)
        if X.ndim == 1: X = X[:, None]
        A = np.column_stack([np.ones(len(X)), X]) if self.fit_intercept else X
        return A @ self.beta_
