import numpy as np, pandas as pd, matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import roc_curve, roc_auc_score

ROOT=Path('/mnt/data/Machine_Learning_Physics')
D=ROOT/'datasets'/'synthetic'; F=ROOT/'lectures'/'figures'
D.mkdir(parents=True,exist_ok=True); F.mkdir(parents=True,exist_ok=True)
rng=np.random.default_rng(42)

# 1 Hooke data
x=np.linspace(0.005,0.10,45); k=18.0
force=k*x+rng.normal(0,0.045,size=x.size)
pd.DataFrame({'zgjatja_m':x,'forca_N':force}).to_csv(D/'hooke_measurements.csv',index=False)
model=LinearRegression().fit(x[:,None],force)
xx=np.linspace(0,0.105,150)
plt.figure(figsize=(6.6,4.2)); plt.scatter(x,force,s=24,label='Matje'); plt.plot(xx,model.predict(xx[:,None]),label='Përshtatja lineare'); plt.xlabel('Zgjatja x [m]'); plt.ylabel('Forca F [N]'); plt.legend(); plt.tight_layout(); plt.savefig(F/'fig_regresioni_hooke.pdf'); plt.close()

# 2 polynomial sensor calibration
T=np.linspace(-20,80,90); V=0.42+0.017*T+0.00042*T**2+rng.normal(0,0.055,len(T))
pd.DataFrame({'temperature_C':T,'voltage_V':V}).to_csv(D/'sensor_calibration.csv',index=False)
plt.figure(figsize=(6.6,4.2)); plt.scatter(T,V,s=18,label='Kalibrim eksperimental')
for deg in [1,2,8]:
    X=PolynomialFeatures(deg,include_bias=False).fit_transform(T[:,None]); m=LinearRegression().fit(X,V)
    xp=np.linspace(T.min(),T.max(),300); Xp=PolynomialFeatures(deg,include_bias=False).fit_transform(xp[:,None])
    plt.plot(xp,m.predict(Xp),label=f'shkalla {deg}')
plt.xlabel('Temperatura [°C]'); plt.ylabel('Sinjali [V]'); plt.legend(); plt.tight_layout(); plt.savefig(F/'fig_regresioni_polinomial.pdf'); plt.close()

# 3 detector pulses classification
n=700
amp0=rng.normal(1.00,0.16,n//2); width0=rng.normal(0.42,0.07,n//2)
amp1=rng.normal(1.33,0.17,n//2); width1=rng.normal(0.61,0.08,n//2)
X=np.c_[np.r_[amp0,amp1],np.r_[width0,width1]]; y=np.r_[np.zeros(n//2,dtype=int),np.ones(n//2,dtype=int)]
pd.DataFrame({'amplitude':X[:,0],'width_us':X[:,1],'class_signal':y}).to_csv(D/'detector_pulses.csv',index=False)
sc=StandardScaler(); Xs=sc.fit_transform(X); log=LogisticRegression().fit(Xs,y)
xx,yy=np.meshgrid(np.linspace(X[:,0].min()-.1,X[:,0].max()+.1,250),np.linspace(X[:,1].min()-.05,X[:,1].max()+.05,250)); grid=np.c_[xx.ravel(),yy.ravel()]
zz=log.predict_proba(sc.transform(grid))[:,1].reshape(xx.shape)
plt.figure(figsize=(6.2,5)); plt.scatter(X[:,0],X[:,1],c=y,s=14,alpha=.6); plt.contour(xx,yy,zz,levels=[.5]); plt.xlabel('Amplituda relative'); plt.ylabel('Gjerësia e impulsit [μs]'); plt.tight_layout(); plt.savefig(F/'fig_logistic_detector.pdf'); plt.close()

# 4 kNN dynamics regimes
n=450
freq=np.r_[rng.normal(.8,.11,n//3),rng.normal(1.35,.10,n//3),rng.normal(1.9,.13,n//3)]
damp=np.r_[rng.normal(.10,.025,n//3),rng.normal(.22,.035,n//3),rng.normal(.38,.05,n//3)]
yk=np.repeat([0,1,2],n//3); Xk=np.c_[freq,damp]
pd.DataFrame({'frekuenca_Hz':freq,'zbehja':damp,'regjimi':yk}).to_csv(D/'dynamical_regimes.csv',index=False)
knn=KNeighborsClassifier(7).fit(StandardScaler().fit_transform(Xk),yk)
plt.figure(figsize=(6.2,4.7)); plt.scatter(freq,damp,c=yk,s=18); plt.xlabel('Frekuenca dominante [Hz]'); plt.ylabel('Koeficienti i zbehjes'); plt.tight_layout(); plt.savefig(F/'fig_knn_regjime.pdf'); plt.close()

# 5 materials for trees
n=600
density=rng.normal(5.2,1.1,n); cond=rng.lognormal(mean=2.0,sigma=.65,size=n); hardness=1.6+0.55*density+0.015*cond+rng.normal(0,.5,n)
phase=((hardness>4.4)&(cond>6.5)).astype(int); phase[(density<4.4)&(cond<6.0)]=2
Xm=np.c_[density,cond,hardness]
pd.DataFrame({'densitet_g_cm3':density,'perçueshmëri':cond,'fortësi':hardness,'fazë':phase}).to_csv(D/'material_phases.csv',index=False)
rf=RandomForestClassifier(n_estimators=200,random_state=0).fit(Xm,phase)
plt.figure(figsize=(6.2,4.2)); plt.bar(['densitet','përçueshmëri','fortësi'],rf.feature_importances_); plt.ylabel('Rëndësia e veçorisë'); plt.tight_layout(); plt.savefig(F/'fig_random_forest_importances.pdf'); plt.close()

# 6 SVM nonlinear orbits
n=500
r=np.sqrt(rng.uniform(.2,2.2,n)); th=rng.uniform(0,2*np.pi,n)
Xs=np.c_[r*np.cos(th),r*np.sin(th)]; ys=(r>1.05).astype(int)
Xs+=rng.normal(0,.06,Xs.shape)
pd.DataFrame({'x_phase':Xs[:,0],'v_phase':Xs[:,1],'regjimi':ys}).to_csv(D/'phase_space_svm.csv',index=False)
sv=SVC(kernel='rbf',C=3,gamma='scale').fit(Xs,ys)
xx,yy=np.meshgrid(np.linspace(-1.7,1.7,250),np.linspace(-1.7,1.7,250)); zz=sv.decision_function(np.c_[xx.ravel(),yy.ravel()]).reshape(xx.shape)
plt.figure(figsize=(5.5,5)); plt.scatter(Xs[:,0],Xs[:,1],c=ys,s=15); plt.contour(xx,yy,zz,levels=[0]); plt.xlabel('x'); plt.ylabel('v'); plt.tight_layout(); plt.savefig(F/'fig_svm_phase.pdf'); plt.close()

# 7 synthetic spectra for PCA
lam=np.linspace(400,800,120)
basis1=np.exp(-.5*((lam-520)/28)**2); basis2=np.exp(-.5*((lam-650)/45)**2); basis3=(lam-lam.mean())/np.ptp(lam)
coef=rng.normal(size=(280,3)); spectra=2+coef[:,0,None]*basis1+0.7*coef[:,1,None]*basis2+0.4*coef[:,2,None]*basis3+rng.normal(0,.08,(280,len(lam)))
pd.DataFrame(spectra,columns=[f'I_{w:.1f}' for w in lam]).to_csv(D/'synthetic_spectra.csv',index=False)
pca=PCA().fit(spectra)
plt.figure(figsize=(6.3,4.2)); plt.plot(np.arange(1,11),np.cumsum(pca.explained_variance_ratio_[:10]),marker='o'); plt.ylim(0,1.02); plt.xlabel('Numri i komponentëve'); plt.ylabel('Varianca e shpjeguar kumulative'); plt.tight_layout(); plt.savefig(F/'fig_pca_variance.pdf'); plt.close()

# 8 clustering regimes atmospheric
n=540
centers=np.array([[5,70,1018],[20,45,1012],[31,30,1004]])
rows=[]; labels=[]
for i,c in enumerate(centers):
    arr=rng.normal(c,[3.0,7.5,4.0],size=(n//3,3)); rows.append(arr); labels.extend([i]*len(arr))
Xa=np.vstack(rows); labels=np.array(labels)
pd.DataFrame({'temperatura_C':Xa[:,0],'RH_pct':Xa[:,1],'presioni_hPa':Xa[:,2],'regjim_i_fshehtë':labels}).to_csv(D/'atmospheric_regimes.csv',index=False)
km=KMeans(n_clusters=3,n_init=20,random_state=0).fit(StandardScaler().fit_transform(Xa))
plt.figure(figsize=(6,4.7)); plt.scatter(Xa[:,0],Xa[:,1],c=km.labels_,s=16); plt.xlabel('Temperatura [°C]'); plt.ylabel('Lagështia relative [%]'); plt.tight_layout(); plt.savefig(F/'fig_kmeans_atmosfera.pdf'); plt.close()

# 9 model comparison dataset based detector + nuisance
n=1200
E=rng.uniform(.1,5,n); rise=rng.normal(.5+.08*E,.09,n); decay=rng.normal(1.2-.08*E,.12,n); noise=rng.normal(0,1,n)
score=1.2*E+2.6*rise-1.7*decay+0.45*np.sin(2*E)+rng.normal(0,.7,n)
yc=(score>np.median(score)).astype(int); Xc=np.c_[E,rise,decay,noise]
pd.DataFrame({'energy_MeV':E,'rise_us':rise,'decay_us':decay,'noise_feature':noise,'signal':yc}).to_csv(D/'physics_model_comparison.csv',index=False)

# 10 gradient data
xg=np.linspace(-2.4,2.6,100); yg=1.7*xg-0.6+rng.normal(0,.5,len(xg))
pd.DataFrame({'x':xg,'y':yg}).to_csv(D/'gradient_regression.csv',index=False)

# 11 perceptron separable + XOR
Xp=np.r_[rng.normal([-1,-.8],[.35,.35],(100,2)),rng.normal([1,.9],[.35,.35],(100,2))]; yp=np.r_[np.zeros(100,dtype=int),np.ones(100,dtype=int)]
pd.DataFrame({'x1':Xp[:,0],'x2':Xp[:,1],'class':yp}).to_csv(D/'perceptron_separable.csv',index=False)
xor=np.array([[0,0],[0,1],[1,0],[1,1]],float); xor_y=np.array([0,1,1,0])
pd.DataFrame({'x1':xor[:,0],'x2':xor[:,1],'class':xor_y}).to_csv(D/'xor.csv',index=False)

# Summary panel-like figures for optimization and validation
eta_vals=[0.01,0.08,0.35]; x0=4.5
plt.figure(figsize=(6.3,4.2))
for eta in eta_vals:
    vals=[x0]; q=x0
    for _ in range(18): q=q-eta*2*q; vals.append(q)
    plt.plot(vals,marker='o',ms=2.5,label=f'η={eta}')
plt.axhline(0,linewidth=.8); plt.xlabel('Iteracioni'); plt.ylabel('Parametri θ'); plt.legend(); plt.tight_layout(); plt.savefig(F/'fig_gradient_convergence.pdf'); plt.close()

# ROC from detector
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.3,random_state=0,stratify=y)
pipe_sc=StandardScaler(); Xtr_s=pipe_sc.fit_transform(Xtr); Xte_s=pipe_sc.transform(Xte); lr=LogisticRegression().fit(Xtr_s,ytr); pr=lr.predict_proba(Xte_s)[:,1]
fpr,tpr,_=roc_curve(yte,pr); auc=roc_auc_score(yte,pr)
plt.figure(figsize=(5.5,4.5)); plt.plot(fpr,tpr,label=f'AUC={auc:.3f}'); plt.plot([0,1],[0,1],'--'); plt.xlabel('Norma e pozitivëve të rremë'); plt.ylabel('Ndjeshmëria'); plt.legend(); plt.tight_layout(); plt.savefig(F/'fig_roc_detector.pdf'); plt.close()
print('assets built')
