import numpy as np
def confusion_counts(y_true,y_pred):
    y_true=np.asarray(y_true).astype(int); y_pred=np.asarray(y_pred).astype(int)
    return dict(tp=int(np.sum((y_true==1)&(y_pred==1))),
                tn=int(np.sum((y_true==0)&(y_pred==0))),
                fp=int(np.sum((y_true==0)&(y_pred==1))),
                fn=int(np.sum((y_true==1)&(y_pred==0))))
def accuracy(y_true,y_pred):
    c=confusion_counts(y_true,y_pred); return (c["tp"]+c["tn"])/sum(c.values())
def precision(y_true,y_pred):
    c=confusion_counts(y_true,y_pred); return c["tp"]/max(1,c["tp"]+c["fp"])
def recall(y_true,y_pred):
    c=confusion_counts(y_true,y_pred); return c["tp"]/max(1,c["tp"]+c["fn"])
def specificity(y_true,y_pred):
    c=confusion_counts(y_true,y_pred); return c["tn"]/max(1,c["tn"]+c["fp"])
def f1_score(y_true,y_pred):
    p,r=precision(y_true,y_pred),recall(y_true,y_pred)
    return 2*p*r/max(1e-15,p+r)
