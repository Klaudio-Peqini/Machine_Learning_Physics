import numpy as np
def roc_curve_manual(y_true,scores):
    y_true=np.asarray(y_true).astype(int); scores=np.asarray(scores,float)
    thresholds=np.r_[np.inf,np.sort(np.unique(scores))[::-1],-np.inf]
    fpr=[]; tpr=[]
    for t in thresholds:
        pred=scores>=t
        tp=np.sum((y_true==1)&pred); fn=np.sum((y_true==1)&~pred)
        fp=np.sum((y_true==0)&pred); tn=np.sum((y_true==0)&~pred)
        tpr.append(tp/max(1,tp+fn)); fpr.append(fp/max(1,fp+tn))
    return np.asarray(fpr),np.asarray(tpr),thresholds
