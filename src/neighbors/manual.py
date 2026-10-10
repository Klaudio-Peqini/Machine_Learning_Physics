import numpy as np

def knn_predict(X_train,y_train,X_test,k=5):
    X_train=np.asarray(X_train,float); X_test=np.asarray(X_test,float); y_train=np.asarray(y_train)
    out=[]
    for z in X_test:
        dist=np.sqrt(((X_train-z)**2).sum(axis=1))
        idx=np.argsort(dist)[:k]
        vals,counts=np.unique(y_train[idx],return_counts=True)
        out.append(vals[np.argmax(counts)])
    return np.asarray(out)
