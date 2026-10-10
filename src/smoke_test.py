import sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from regression.linear import LinearRegressionOLS
from classification.logistic import LogisticRegressionGD
from neighbors.knn import KNNClassifier
from trees.impurity import gini_impurity
from pca.pca_from_scratch import PCAFromScratch
from clustering.kmeans import KMeansFromScratch
from optimization.gradient_descent import gradient_descent
from perceptron.perceptron import PerceptronFromScratch

x=np.arange(5.0); y=2*x+1
assert np.allclose(LinearRegressionOLS().fit(x,y).predict(x),y)
X=np.array([[0.],[1.],[2.],[3.]]); yy=np.array([0,0,1,1])
assert (LogisticRegressionGD(lr=0.2,n_iter=2500).fit(X,yy).predict(X)==yy).mean()>=0.75
assert np.array_equal(KNNClassifier(1).fit(X,yy).predict(X),yy)
assert abs(gini_impurity([0,0,1,1])-0.5)<1e-12
assert PCAFromScratch(1).fit_transform(np.array([[0.,0.],[1.,1.],[2.,2.]])).shape==(3,1)
assert len(np.unique(KMeansFromScratch(2,seed=0).fit(np.array([[0.,0.],[0.,1.],[10.,10.],[10.,11.]])).labels_))==2
theta,_=gradient_descent([0.0],lambda th:2*(th-np.array([3.0])),lr=0.1,n_iter=500)
assert abs(theta[0]-3.0)<1e-6
Xp=np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]]); yp=np.array([0,0,0,1])
assert np.array_equal(PerceptronFromScratch(max_epochs=100).fit(Xp,yp).predict(Xp),yp)
print("Të gjitha provat bazë kaluan me sukses.")
