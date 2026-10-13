# NOTEBOOK_GUIDE — Machine Learning in Physics

Notebooks are the operational heart of the course; lecture notes are the deeper theoretical reference.

| # | Notebook | Live core | Full work | Main focus | Common misconception |
|---|---|---:|---:|---|---|
| 1 | Hyrje, të dhënat dhe validimi | 55 min | 100 min | split, scaling, leakage, CV | test set may be used repeatedly |
| 2 | Regresioni linear | 55 min | 100 min | OLS, residuals, uncertainty | best fit = physical truth |
| 3 | Polynomial/Ridge/Lasso | 60 min | 110 min | complexity, regularization | lower training error is always better |
| 4 | Logistic regression | 60 min | 120 min | threshold, ROC, PR | 0.5 is universally optimal |
| 5 | k-NN | 50 min | 95 min | distance, k, scaling | features' units do not matter |
| 6 | Trees/ensembles | 60 min | 110 min | impurity, depth, RF | feature importance = causality |
| 7 | SVM | 55 min | 100 min | margin, C, kernels | kernel is a magic nonlinear model |
| 8 | PCA | 60 min | 120 min | covariance, eigenvectors | PCA components are physical causes |
| 9 | Clustering | 55 min | 110 min | k-means, silhouette, dendrogram | clusters are objectively real |
| 10 | Model comparison | 60 min | 130 min | CV, uncertainty, robustness | one metric defines the winner |
| 11 | Gradient descent | 55 min | 105 min | geometry, learning rate, SGD | gradient descent is only for NNs |
| 12 | Perceptron | 55 min | 105 min | linear separability, convergence, XOR | failure on XOR means bad training |

## How to teach from them

- Cover the sections marked **CORE** during class.
- The marker **“Deri këtu: materiali bazë për orën mësimore”** is the natural stopping point.
- Use **EXTENDED** as homework, optional discussion, or material for faster groups.
- Use **PLAYGROUND** as student-led experimentation.
- Instructor notebooks are fully executable.
- Student notebooks keep the same conceptual flow and include open-ended tasks.

## Prerequisites

Calculus, linear algebra, probability/statistics, numerical methods, basic Python/NumPy/Matplotlib.

## Recommended rhythm

1. 5–10 min: motivating problem and mathematical object.
2. 10–15 min: first-principles implementation.
3. 10 min: visualization.
4. 10 min: professional-library comparison.
5. 10 min: interpretation/failure case.
6. 5 min: assign playground.

## Links to lecture chapters

Notebook number = lecture chapter number. This one-to-one mapping is intentional.


## Revision: rich-context edition

Every computational cell is now preceded by a contextual explanation in academic Albanian. Crucial code lines carry comments that identify their methodological role. The intended teaching sequence is: question → reason for the step → code → observation → scientific interpretation. In class, code should be executed only after students have stated what they expect to see.
