from pathlib import Path
import nbformat as nbf

ROOT=Path('/mnt/data/Machine_Learning_Physics')
NB=ROOT/'notebooks'
NB.mkdir(exist_ok=True)

COMMON_IMPORT='''from pathlib import Path
import sys, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_validate, StratifiedKFold, KFold, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso, Perceptron, SGDRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
DATA = Path("../datasets/synthetic")
SRC = Path("../src").resolve()
if str(SRC.parent) not in sys.path:
    sys.path.insert(0, str(SRC.parent))
np.set_printoptions(precision=4, suppress=True)
RANDOM_STATE = 42
'''

def md(t): return nbf.v4.new_markdown_cell(t)
def code(t): return nbf.v4.new_code_cell(t)
def make(name,title,context,objectives,cells):
    nb=nbf.v4.new_notebook()
    nb['metadata']['kernelspec']={'display_name':'Python 3','language':'python','name':'python3'}
    nb['metadata']['language_info']={'name':'python','version':'3'}
    header=f'''# {title}

## Konteksti dhe problemi shkencor

{context}

### Objektivat e të nxënit

{objectives}

> **Parimi i laboratorit:** matematikë → implementim nga parimet e para → implementim me bibliotekë → krahasim numerik → interpretim fizik.
'''
    nb['cells']=[md(header),code(COMMON_IMPORT)]+cells
    nbf.write(nb,NB/name)

# 1 Foundations
cells=[
md(r'''## 1. Nga pyetja fizike te tabela e të dhënave

Një problem ML nuk fillon me `sklearn`, por me një pyetje. Në këtë notebook përdorim pulse sintetike detektori. Çdo rresht është një ngjarje; amplituda dhe gjerësia janë **veçori (features)**, ndërsa `class_signal` është **etiketa (label)**.'''),
code("df=pd.read_csv(DATA/'detector_pulses.csv'); df.head()"),
code("df.describe(include='all')"),
md(r'''## 2. Vizualizimi fillestar dhe kontrolli fizik

Shikojmë shpërndarjet para se të modelojmë. Një ndarje e dukshme në dy dimensione na jep intuitë, por nuk duhet të përdoret si zëvendësim për validimin.'''),
code("plt.figure(figsize=(6,4.5)); plt.scatter(df.amplitude,df.width_us,c=df.class_signal,s=15,alpha=.6); plt.xlabel('Amplituda'); plt.ylabel('Gjerësia [μs]'); plt.show()"),
md(r'''## 3. Trajnim dhe provë

Përdorim një model të thjeshtë vetëm për të studiuar procedurën. Në këtë temë modeli është dytësor; fokusi është ndarja, standardizimi dhe rrjedhja e informacionit.'''),
code("from sklearn.linear_model import LogisticRegression\nX=df[['amplitude','width_us']]; y=df.class_signal\nX_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,stratify=y,random_state=RANDOM_STATE)\npipe=make_pipeline(StandardScaler(),LogisticRegression())\npipe.fit(X_train,y_train)\nprint('train=',pipe.score(X_train,y_train),'test=',pipe.score(X_test,y_test))"),
md(r'''## 4. Validimi i kryqëzuar

Një split i vetëm është vetëm një realizim. Në $K$-fold cross-validation raportojmë mesataren **dhe** variabilitetin.'''),
code("cv=StratifiedKFold(5,shuffle=True,random_state=RANDOM_STATE)\nr=cross_validate(pipe,X,y,cv=cv,return_train_score=True)\npd.DataFrame(r)[['train_score','test_score']]"),
code("print(f\"CV: {r['test_score'].mean():.3f} ± {r['test_score'].std():.3f}\")"),
md(r'''## 5. Eksperiment: rrjedhje informacioni

Krijojmë një shembull ku standardizimi kryhet gabimisht para cross-validation. Në këtë dataset efekti mund të jetë i vogël; pikërisht kjo e bën gabimin të rrezikshëm: kodi duket i rregullt dhe rezultati mund të ndryshojë vetëm pak. Parimi mbetet i gabuar.'''),
code("from sklearn.model_selection import cross_val_score\nsc=StandardScaler(); X_leaky=sc.fit_transform(X)\nscore_bad=cross_val_score(LogisticRegression(),X_leaky,y,cv=cv)\nscore_good=cross_val_score(pipe,X,y,cv=cv)\nprint('gabim:',score_bad.mean(), 'pipeline:',score_good.mean())"),
md(r'''## 6. Eksperiment më i fortë: përzgjedhje veçorish para ndarjes

Shtojmë shumë veçori zhurme dhe zgjedhim veçoritë më të korreluara me etiketën duke përdorur **të gjithë** dataset-in. Kjo krijon rrjedhje më të dukshme.'''),
code("rng=np.random.default_rng(3); Z=rng.normal(size=(len(y),200)); tmp=pd.DataFrame(Z); corr=np.abs(np.corrcoef(np.c_[Z,y],rowvar=False)[-1,:-1]); idx=np.argsort(corr)[-8:]; X_bad=Z[:,idx]\nprint('CV pas përzgjedhjes së gabuar:',cross_val_score(LogisticRegression(max_iter=2000),X_bad,y,cv=cv).mean())"),
md(r'''## 7. Interpretim

Në një eksperiment real, ``rreshti'' mund të mos jetë njësi e pavarur. Pulse nga i njëjti run, spektra nga i njëjti kampion ose dritare të mbivendosura nga e njëjta seri kohore duhet të ndahen sipas grupeve, jo rastësisht.'''),
md(r'''## 8. Ushtrim studenti

1. Ndryshoni `test_size` dhe studioni variabilitetin e rezultatit.
2. Përsëritni 30 train/test split-e me fara të ndryshme dhe vizatoni histogramin e accuracy.
3. Shpjegoni me fjalët tuaja ndryshimin midis parametrit dhe hiperparametrit.
4. Propozoni një ndarje korrekte për matje të marra në 10 ditë eksperimentale.'''),
md(r'''## 9. Shembull i plotë i punuar

Ndërtoni një pipeline, bëni 5-fold CV, pastaj rezervoni 20% si test final dhe raportoni score-n vetëm një herë. Shënoni qartë cilat vendime u morën para se të hapej testi.'''),
code("X_dev,X_final,y_dev,y_final=train_test_split(X,y,test_size=.2,stratify=y,random_state=11)\nprint('CV development:',cross_val_score(pipe,X_dev,y_dev,cv=5).mean())\npipe.fit(X_dev,y_dev); print('Final test:',pipe.score(X_final,y_final))"),
md(r'''## 10. Playground

Eksperimentoni me një veçori të tretë zhurme, me `MinMaxScaler`, ose me një ndarje ku 90% e klasës 1 futet në trajnim dhe diskutoni pse rezultati nuk është i krahasueshëm.''')]
make('01_hyrje_te_dhenat_dhe_validimi.ipynb','01 — Hyrje, të dhënat dhe validimi','Do të ndërtojmë një eksperiment të vogël klasifikimi me pulse detektori për të kuptuar strukturën e një workflow-je ML pa e ngatërruar metodologjinë me algoritmin.','- të dalloni veçoritë, etiketat, parametrat dhe hiperparametrat;\n- të përdorni train/validation/test dhe cross-validation;\n- të dalloni rrjedhjen e informacionit;\n- të përdorni pipeline për preprocessing.',cells)

# 2 linear regression
cells=[
md(r'''## 1. Problemi fizik: ligji i Hukut

Përdorim $F=kx+F_0+\epsilon$. Synimi nuk është vetëm të parashikojmë $F$, por të vlerësojmë $k$ dhe të kuptojmë rezidualet.'''),
code("df=pd.read_csv(DATA/'hooke_measurements.csv'); x=df.zgjatja_m.to_numpy(); y=df.forca_N.to_numpy(); plt.scatter(x,y); plt.xlabel('x [m]'); plt.ylabel('F [N]'); plt.show()"),
md(r'''## 2. Derivimi i OLS

Me $A=[\mathbf 1, x]$ minimizojmë $\|A\beta-y\|^2$. Kushti $A^T(A\beta-y)=0$ jep
$$\hat\beta=(A^TA)^{-1}A^Ty.$$
Numerikisht përdorim `solve` ose pseudoinversin, jo invers të formuar pa nevojë.'''),
code("A=np.c_[np.ones(len(x)),x]; beta=np.linalg.solve(A.T@A,A.T@y); beta"),
code("yhat=A@beta; resid=y-yhat; print('F0=',beta[0],'k=',beta[1]); print('MSE=',np.mean(resid**2))"),
md(r'''## 3. Kontrolli gjeometrik

Reziduali duhet të jetë ortogonal me kolonat e matricës së dizajnit.'''),
code("A.T@resid"),
md(r'''## 4. Implementim nga moduli i kursit dhe krahasim me scikit-learn'''),
code("from src.regression.manual import ols_fit,predict_linear\nfrom sklearn.linear_model import LinearRegression\nb_manual=ols_fit(x,y); sk=LinearRegression().fit(x[:,None],y); print(b_manual, [sk.intercept_,sk.coef_[0]])"),
code("xp=np.linspace(0,.105,200); plt.scatter(x,y,label='matje'); plt.plot(xp,predict_linear(xp,b_manual),label='manual'); plt.plot(xp,sk.predict(xp[:,None]),'--',label='sklearn'); plt.legend(); plt.show()"),
md(r'''## 5. Rezidualet si instrument diagnostik'''),
code("plt.axhline(0,linewidth=.8); plt.scatter(x,resid); plt.xlabel('x [m]'); plt.ylabel('reziduali [N]'); plt.show()"),
md(r'''## 6. Pasiguria e koeficientëve

Për modelin klasik, $\hat\sigma^2=RSS/(N-p)$ dhe $Cov(\hat\beta)=\hat\sigma^2(A^TA)^{-1}$.'''),
code("p=A.shape[1]; sigma2=(resid@resid)/(len(y)-p); cov=sigma2*np.linalg.inv(A.T@A); se=np.sqrt(np.diag(cov)); print('beta=',beta,'SE=',se)"),
md(r'''## 7. Shembull i dytë: matja e $g$ nga rënia e lirë

Nga $s=\frac12gt^2$ mund të regresojmë $s$ ndaj $t^2$. Ky transformim vjen nga fizika, jo nga kërkim arbitrar i veçorive.'''),
code("rng=np.random.default_rng(12); t=np.linspace(.1,1.2,40); s=.5*9.81*t**2+rng.normal(0,.04,len(t)); m=LinearRegression(fit_intercept=True).fit((t**2)[:,None],s); print('g_hat=',2*m.coef_[0])"),
md(r'''## 8. Rast dështimi: marrëdhënie jolineare'''),
code("ycurved=18*x+50*x**2+np.random.default_rng(0).normal(0,.03,len(x)); lin=LinearRegression().fit(x[:,None],ycurved); r=ycurved-lin.predict(x[:,None]); plt.scatter(x,r); plt.axhline(0); plt.show()"),
md(r'''## 9. Ushtrime

- Implementoni regresion të ponderuar kur $\sigma_i$ rritet me $x$.
- Shtoni një matje të largët dhe krahasoni MSE me MAE.
- Krijoni dy kolona pothuajse identike dhe llogaritni `np.linalg.cond(A.T@A)`.
- Shpjegoni pse koeficienti mund të jetë i paqëndrueshëm edhe kur parashikimet janë të mira.'''),
md(r'''## 10. Shembull i plotë

Raportoni $k\pm SE_k$, interceptin, MSE dhe një grafik rezidualesh në formën e një mini-raporti laboratorik.'''),
md(r'''## 11. Playground

Ndryshoni zhurmën, numrin e matjeve dhe diapazonin e $x$. Vëzhgoni si ndryshon pasiguria e $k$.''')]
make('02_regresioni_linear.ipynb','02 — Regresioni linear dhe vlerësimi i parametrave','Ligji i Hukut dhe rënia e lirë na lejojnë të lidhim regresionin me vlerësimin e parametrave fizikë, jo vetëm me parashikimin.','- të derivoni OLS;\n- të implementoni regresionin linear;\n- të analizoni rezidualet dhe pasigurinë;\n- të kuptoni kondicionimin numerik.',cells)

# 3 polynomial/Ridge/Lasso
cells=[md(r'''## 1. Kalibrim sensori me përgjigje jolineare'''),code("df=pd.read_csv(DATA/'sensor_calibration.csv'); x=df.temperature_C.to_numpy(); y=df.voltage_V.to_numpy(); plt.scatter(x,y,s=18); plt.show()"),
md(r'''## 2. Matrica polinomiale nga parimet e para'''),code("from src.regression.manual import polynomial_design\nfor d in [1,2,5]: print(d,polynomial_design(x[:3],d))"),
md(r'''## 3. OLS për disa shkallë'''),code("from sklearn.metrics import mean_squared_error\nfrom sklearn.model_selection import train_test_split\nxt,xv,yt,yv=train_test_split(x,y,test_size=.3,random_state=0)\nrows=[]\nfor d in range(1,11):\n    pt=PolynomialFeatures(d,include_bias=False); Xt=pt.fit_transform(xt[:,None]); Xv=pt.transform(xv[:,None]); m=LinearRegression().fit(Xt,yt); rows.append((d,mean_squared_error(yt,m.predict(Xt)),mean_squared_error(yv,m.predict(Xv))))\npd.DataFrame(rows,columns=['degree','train_MSE','valid_MSE'])"),
code("rr=pd.DataFrame(rows,columns=['degree','train_MSE','valid_MSE']); plt.plot(rr.degree,rr.train_MSE,marker='o',label='train'); plt.plot(rr.degree,rr.valid_MSE,marker='o',label='valid'); plt.yscale('log'); plt.legend(); plt.show()"),
md(r'''## 4. Ridge nga formula e mbyllur'''),code("d=8; P=PolynomialFeatures(d,include_bias=False); X=P.fit_transform(x[:,None]); mu=X.mean(0); sd=X.std(0); Xs=(X-mu)/sd\nA=np.c_[np.ones(len(Xs)),Xs]\ndef ridge_closed(alpha):\n    I=np.eye(A.shape[1]); I[0,0]=0; return np.linalg.solve(A.T@A+alpha*I,A.T@y)\nfor a in [0,0.01,1,100]: print(a,np.linalg.norm(ridge_closed(a)[1:]))"),
md(r'''## 5. Krahasim me Ridge dhe Lasso në pipeline'''),code("from sklearn.linear_model import Ridge,Lasso\nfrom sklearn.model_selection import cross_val_score\nfor model in [LinearRegression(),Ridge(alpha=1),Lasso(alpha=.001,max_iter=20000)]:\n    p=make_pipeline(PolynomialFeatures(6,include_bias=False),StandardScaler(),model)\n    s=-cross_val_score(p,x[:,None],y,cv=5,scoring='neg_mean_squared_error')\n    print(model.__class__.__name__,s.mean(),s.std())"),
md(r'''## 6. Rrugët e regularizimit'''),code("alphas=np.logspace(-4,3,40); norms=[]\nXp=PolynomialFeatures(8,include_bias=False).fit_transform(x[:,None]); Xp=StandardScaler().fit_transform(Xp)\nfor a in alphas: norms.append(np.linalg.norm(Ridge(alpha=a).fit(Xp,y).coef_))\nplt.semilogx(alphas,norms); plt.xlabel('alpha'); plt.ylabel('||coef||'); plt.show()"),
md(r'''## 7. Ndërveprime fizike

Jo çdo term polinomial është i arsyeshëm. Në probleme me disa madhësi, produkte si $VT$, $B^2$ ose $xv$ mund të kenë motivim fizik. Ndërtimi i veçorive duhet të udhëhiqet nga mekanizmi, jo vetëm nga score.'''),
md(r'''## 8. Rast dështimi: ekstrapolimi'''),code("train=df[df.temperature_C<55]; test=np.linspace(55,120,120);\nfor d in [2,8]:\n p=make_pipeline(PolynomialFeatures(d,include_bias=False),LinearRegression()).fit(train[['temperature_C']],train.voltage_V); plt.plot(test,p.predict(test[:,None]),label=f'd={d}')\nplt.legend(); plt.title('Ekstrapolimi jashtë diapazonit'); plt.show()"),
md(r'''## 9. Ushtrime

1. Derivoni Ridge nga funksioni i humbjes.
2. Krahasoni shkallët 1–12 me nested CV.
3. Ndryshoni standardizimin dhe vëzhgoni Lasso.
4. Ndërtoni një problem me dy veçori të korreluara dhe studioni stabilitetin e Lasso.'''),
md(r'''## 10. Shembull i plotë i punuar

Zgjidhni shkallën dhe alpha vetëm me të dhënat e zhvillimit; hapni testin final në fund. Raportoni kurbën e validimit dhe justifikoni zgjedhjen.'''),
md(r'''## 11. Playground

Ndryshoni zhurmën, shkallën reale të polinomit dhe numrin e pikave. Kur fillon overfitting? A ndryshon përgjigjja me madhësinë e mostrës?''')]
make('03_regresioni_polinomial_ridge_lasso.ipynb','03 — Regresioni polinomial, Ridge dhe Lasso','Kalibrimi i një sensori tregon si rritja e fleksibilitetit sjell mbipërshtatje dhe si regularizimi e stabilizon problemin.','- të ndërtoni veçori polinomiale;\n- të dalloni kompleksitetin nga lineariteti në parametra;\n- të implementoni Ridge;\n- të përdorni cross-validation për regularizimin.',cells)

# 4 logistic
cells=[md(r'''## 1. Diskriminimi sinjal–sfond'''),code("df=pd.read_csv(DATA/'detector_pulses.csv'); X=df[['amplitude','width_us']].to_numpy(); y=df.class_signal.to_numpy(); plt.scatter(X[:,0],X[:,1],c=y,s=15); plt.show()"),
md(r'''## 2. Sigmoidi dhe cross-entropy'''),code("z=np.linspace(-8,8,300); sig=1/(1+np.exp(-z)); plt.plot(z,sig); plt.axhline(.5,ls='--'); plt.show()"),
md(r'''Për $p_i=\sigma(w^Tx_i+b)$ minimizojmë $$-\frac1N\sum_i[y_i\log p_i+(1-y_i)\log(1-p_i)].$$'''),
md(r'''## 3. Implementim manual me gradient descent'''),code("from src.classification.manual import logistic_fit_gd,logistic_predict_proba\nsc=StandardScaler(); Xs=sc.fit_transform(X); w,h=logistic_fit_gd(Xs,y,lr=.15,n_iter=1500,l2=.001); print(w); plt.plot(h); plt.yscale('log'); plt.show()"),
code("p=logistic_predict_proba(Xs,w); pred=(p>=.5).astype(int); print('accuracy manual=',np.mean(pred==y))"),
md(r'''## 4. Krahasim me scikit-learn'''),code("from sklearn.linear_model import LogisticRegression\nsk=LogisticRegression(C=1000).fit(Xs,y); print(sk.intercept_,sk.coef_); print(sk.score(Xs,y))"),
md(r'''## 5. Kufiri i vendimit'''),code("xx,yy=np.meshgrid(np.linspace(X[:,0].min()-.1,X[:,0].max()+.1,250),np.linspace(X[:,1].min()-.05,X[:,1].max()+.05,250)); grid=np.c_[xx.ravel(),yy.ravel()]; zz=sk.predict_proba(sc.transform(grid))[:,1].reshape(xx.shape); plt.scatter(X[:,0],X[:,1],c=y,s=12,alpha=.5); plt.contour(xx,yy,zz,levels=[.5]); plt.show()"),
md(r'''## 6. Matrica e konfuzionit dhe pragjet'''),code("from sklearn.metrics import confusion_matrix,classification_report,roc_curve,roc_auc_score,precision_recall_curve\nXtr,Xte,ytr,yte=train_test_split(X,y,test_size=.3,stratify=y,random_state=0); pipe=make_pipeline(StandardScaler(),LogisticRegression()).fit(Xtr,ytr); prob=pipe.predict_proba(Xte)[:,1]\nfor th in [.3,.5,.7]: print(th,confusion_matrix(yte,(prob>=th).astype(int)).tolist())"),
md(r'''## 7. ROC dhe Precision–Recall'''),code("fpr,tpr,_=roc_curve(yte,prob); pr,rc,_=precision_recall_curve(yte,prob); fig,ax=plt.subplots(); ax.plot(fpr,tpr,label=f'ROC AUC={roc_auc_score(yte,prob):.3f}'); ax.plot([0,1],[0,1],'--'); ax.legend(); plt.show(); plt.figure(); plt.plot(rc,pr); plt.xlabel('recall'); plt.ylabel('precision'); plt.show()"),
md(r'''## 8. Rast i rrallë: pse accuracy dështon'''),code("yr=np.r_[np.zeros(990,dtype=int),np.ones(10,dtype=int)]; pred0=np.zeros_like(yr); print('accuracy e modelit absurd=',np.mean(pred0==yr))"),
md(r'''## 9. Kalibrimi'''),code("from sklearn.calibration import calibration_curve\nfrac,mean=calibration_curve(yte,prob,n_bins=8); plt.plot(mean,frac,marker='o'); plt.plot([0,1],[0,1],'--'); plt.xlabel('p e parashikuar'); plt.ylabel('frekuenca reale'); plt.show()"),
md(r'''## 10. Ushtrime

- Derivoni gradientin.
- Zgjidhni pragun kur FN kushton 5 herë më shumë se FP.
- Krahasoni ROC-AUC dhe PR-AUC kur klasa pozitive bëhet 5%.
- Shtoni regularizim dhe interpretoni ndryshimin e koeficientëve.'''),
md(r'''## 11. Shembull i plotë

Shkruani një raport sinjal/sfond ku zgjidhni pragun sipas një objektivi shkencor të deklaruar, jo sipas accuracy.'''),
md(r'''## 12. Playground

Ndryshoni mbivendosjen e klasave duke shtuar zhurmë dhe vëzhgoni si deformohen ROC, precision-recall dhe kufiri i vendimit.''')]
make('04_klasifikimi_dhe_regresioni_logjistik.ipynb','04 — Klasifikimi dhe regresioni logjistik','Pulse detektori përdoren për të lidhur probabilitetin, kufirin linear, metrikat dhe zgjedhjen e pragut me një problem shkencor.','- të implementoni regresionin logjistik;\n- të përdorni confusion matrix, ROC dhe calibration;\n- të kuptoni pragun e vendimit;\n- të interpretoni koeficientët me kujdes.',cells)

# 5 knn
cells=[md(r'''## 1. Regjime dinamike si problem lokal'''),code("df=pd.read_csv(DATA/'dynamical_regimes.csv'); X=df[['frekuenca_Hz','zbehja']].to_numpy(); y=df.regjimi.to_numpy(); plt.scatter(X[:,0],X[:,1],c=y,s=16); plt.show()"),
md(r'''## 2. Distanca dhe implementimi manual'''),code("from src.neighbors.manual import knn_predict\nXtr,Xte,ytr,yte=train_test_split(X,y,test_size=.3,stratify=y,random_state=0); sc=StandardScaler().fit(Xtr); Xtrs=sc.transform(Xtr); Xtes=sc.transform(Xte); pred=knn_predict(Xtrs,ytr,Xtes,k=5); print(np.mean(pred==yte))"),
md(r'''## 3. Krahasim me bibliotekën'''),code("from sklearn.neighbors import KNeighborsClassifier\nsk=KNeighborsClassifier(5).fit(Xtrs,ytr); print(np.mean(sk.predict(Xtes)==pred),sk.score(Xtes,yte))"),
md(r'''## 4. Zgjedhja e k me cross-validation'''),code("ks=range(1,41,2); means=[]; stds=[]\nfor k in ks:\n p=make_pipeline(StandardScaler(),KNeighborsClassifier(k)); s=cross_val_score(p,X,y,cv=5); means.append(s.mean()); stds.append(s.std())\nplt.errorbar(list(ks),means,yerr=stds,marker='o'); plt.xlabel('k'); plt.ylabel('CV accuracy'); plt.show()"),
md(r'''## 5. Efekti i shkallëzimit'''),code("X_bad=X.copy(); X_bad[:,0]*=1000; print('pa scaling',cross_val_score(KNeighborsClassifier(7),X_bad,y,cv=5).mean()); print('me scaling',cross_val_score(make_pipeline(StandardScaler(),KNeighborsClassifier(7)),X_bad,y,cv=5).mean())"),
md(r'''## 6. Mallkimi i dimensionalitetit'''),code("rng=np.random.default_rng(1); vals=[]\nfor q in [0,2,5,10,30,80]:\n Xq=np.c_[X,rng.normal(size=(len(X),q))] if q else X\n vals.append((q,cross_val_score(make_pipeline(StandardScaler(),KNeighborsClassifier(7)),Xq,y,cv=5).mean()))\npd.DataFrame(vals,columns=['noise_features','cv_accuracy'])"),
md(r'''## 7. Kufiri i vendimit'''),code("pipe=make_pipeline(StandardScaler(),KNeighborsClassifier(7)).fit(X,y); xx,yy=np.meshgrid(np.linspace(X[:,0].min()-.2,X[:,0].max()+.2,250),np.linspace(X[:,1].min()-.08,X[:,1].max()+.08,250)); zz=pipe.predict(np.c_[xx.ravel(),yy.ravel()]).reshape(xx.shape); plt.contourf(xx,yy,zz,alpha=.25); plt.scatter(X[:,0],X[:,1],c=y,s=12); plt.show()"),
md(r'''## 8. Kostoja e parashikimit'''),code("for n in [100,1000,5000]:\n rng=np.random.default_rng(2); Xt=rng.normal(size=(n,15)); yt=rng.integers(0,2,n); z=rng.normal(size=(200,15)); m=KNeighborsClassifier(5).fit(Xt,yt); t=time.perf_counter(); m.predict(z); print(n,time.perf_counter()-t)"),
md(r'''## 9. Ushtrime

- Implementoni votim të ponderuar me $1/(d+\epsilon)$.
- Krahasoni Manhattan dhe Euclidean.
- Shtoni veçori zhurme derisa accuracy të bjerë nën 0.8.
- Gjeni shembuj testimi dhe listoni fqinjët që prodhuan vendimin.'''),
md(r'''## 10. Shembull i plotë

Zgjidhni k me CV vetëm në development set, pastaj raportoni testin final dhe shpjegoni pse scaling është pjesë e pipeline.'''),
md(r'''## 11. Playground

Krijoni një regjim të katërt që mbivendoset fort me të dytin. A ndihmon k më i madh apo më i vogël?''')]
make('05_knn.ipynb','05 — k-NN: të nxënit nga fqinjët','Regjimet e një sistemi të zbehur përdoren për të eksploruar distancën, shkallëzimin, parametrin k dhe dimensionin.','- të implementoni k-NN;\n- të kuptoni rolin e distancës dhe scaling;\n- të shihni bias–variance përmes k;\n- të demonstroni mallkimin e dimensionalitetit.',cells)

# 6 trees ensembles
cells=[md(r'''## 1. Faza materialesh'''),code("df=pd.read_csv(DATA/'material_phases.csv'); X=df[['densitet_g_cm3','perçueshmëri','fortësi']]; y=df['fazë']; df.head()"),
md(r'''## 2. Gini nga parimet e para'''),code("from src.trees.manual import gini,split_gain\nprint('Gini root=',gini(y)); mask=X['fortësi']<4.5; print('gain=',split_gain(y,mask))"),
md(r'''## 3. Kërkim manual i një ndarjeje'''),code("candidates=np.quantile(X['fortësi'],np.linspace(.05,.95,40)); gains=[split_gain(y,X['fortësi']<t) for t in candidates]; best=candidates[np.argmax(gains)]; print(best,max(gains)); plt.plot(candidates,gains); plt.show()"),
md(r'''## 4. Pemë scikit-learn dhe thellësia'''),code("from sklearn.tree import DecisionTreeClassifier,plot_tree\nfor d in [1,2,4,None]:\n m=DecisionTreeClassifier(max_depth=d,random_state=0); print(d,cross_val_score(m,X,y,cv=5).mean())"),
code("m=DecisionTreeClassifier(max_depth=3,random_state=0).fit(X,y); plt.figure(figsize=(14,7)); plot_tree(m,feature_names=X.columns,filled=False,fontsize=8); plt.show()"),
md(r'''## 5. Bagging minimal dhe Random Forest'''),code("from sklearn.ensemble import BaggingClassifier,RandomForestClassifier\nbag=BaggingClassifier(estimator=DecisionTreeClassifier(),n_estimators=100,random_state=0); rf=RandomForestClassifier(n_estimators=250,random_state=0); print('tree',cross_val_score(DecisionTreeClassifier(random_state=0),X,y,cv=5).mean()); print('bag',cross_val_score(bag,X,y,cv=5).mean()); print('rf',cross_val_score(rf,X,y,cv=5).mean())"),
md(r'''## 6. Feature importance dhe permutation importance'''),code("from sklearn.inspection import permutation_importance\nXtr,Xte,ytr,yte=train_test_split(X,y,test_size=.3,stratify=y,random_state=0); rf.fit(Xtr,ytr); imp=pd.Series(rf.feature_importances_,index=X.columns); perm=permutation_importance(rf,Xte,yte,n_repeats=20,random_state=0); pd.DataFrame({'impurity':imp,'permutation':perm.importances_mean},index=X.columns)"),
md(r'''## 7. Boosting: vetëm ideja praktike'''),code("from sklearn.ensemble import HistGradientBoostingClassifier\nhgb=HistGradientBoostingClassifier(max_iter=100,random_state=0); print(cross_val_score(hgb,X,y,cv=5).mean())"),
md(r'''## 8. Rast dështimi: pemë shumë e thellë'''),code("tr=[]; te=[]; depths=range(1,16)\nfor d in depths:\n m=DecisionTreeClassifier(max_depth=d,random_state=0).fit(Xtr,ytr); tr.append(m.score(Xtr,ytr)); te.append(m.score(Xte,yte))\nplt.plot(depths,tr,label='train'); plt.plot(depths,te,label='test'); plt.legend(); plt.show()"),
md(r'''## 9. Ushtrime

- Llogaritni entropinë dhe krahasojeni me Gini.
- Ndërtoni manualisht një stump me një ndarje.
- Krahasoni `max_features` te random forest.
- Shtoni veçori zhurme dhe krahasoni dy llojet e importance.'''),
md(r'''## 10. Shembull i plotë

Krahasoni pemën e cekët, pemën e thellë dhe random forest me të njëjtat split-e; argumentoni kompromisin interpretueshmëri–performancë.'''),
md(r'''## 11. Playground

Ndryshoni rregullin sintetik që krijon fazat. Kur rregulli bëhet diagonal ose i lakuar, si ndryshon numri i ndarjeve të nevojshme?''')]
make('06_pemet_dhe_metodat_ansambel.ipynb','06 — Pemët e vendimit dhe ansamblet','Klasifikimi i fazave të materialit demonstron ndarjet, papastërtinë, overfitting, bagging dhe random forest.','- të llogaritni Gini dhe fitimin;\n- të kontrolloni thellësinë;\n- të kuptoni bagging/random forest;\n- të përdorni interpretueshmërinë me kujdes.',cells)

# 7 SVM
cells=[md(r'''## 1. Hapësira e fazës dhe kufiri jolinear'''),code("df=pd.read_csv(DATA/'phase_space_svm.csv'); X=df[['x_phase','v_phase']].to_numpy(); y=df.regjimi.to_numpy(); plt.scatter(X[:,0],X[:,1],c=y,s=14); plt.axis('equal'); plt.show()"),
md(r'''## 2. Margjina lineare në një dataset të thjeshtë'''),code("rng=np.random.default_rng(0); Xa=np.r_[rng.normal([-1,-1],.35,(80,2)),rng.normal([1,1],.35,(80,2))]; ya=np.r_[np.zeros(80),np.ones(80)]; from sklearn.svm import SVC; lin=SVC(kernel='linear',C=10).fit(Xa,ya); print('support vectors=',lin.support_vectors_.shape[0])"),
code("w=lin.coef_[0]; b=lin.intercept_[0]; xx=np.linspace(-2,2,200); boundary=-(w[0]*xx+b)/w[1]; margin1=-(w[0]*xx+b-1)/w[1]; margin2=-(w[0]*xx+b+1)/w[1]; plt.scatter(Xa[:,0],Xa[:,1],c=ya,s=14); plt.plot(xx,boundary); plt.plot(xx,margin1,'--'); plt.plot(xx,margin2,'--'); plt.scatter(lin.support_vectors_[:,0],lin.support_vectors_[:,1],facecolors='none',edgecolors='k',s=90); plt.show()"),
md(r'''## 3. Roli i C'''),code("for C in [.05,.5,5,500]:\n m=SVC(kernel='linear',C=C).fit(Xa,ya); print(C,len(m.support_),m.score(Xa,ya))"),
md(r'''## 4. RBF për regjimet rrethore'''),code("for kernel in ['linear','rbf']:\n p=make_pipeline(StandardScaler(),SVC(kernel=kernel,C=3,gamma='scale')); print(kernel,cross_val_score(p,X,y,cv=5).mean())"),
md(r'''## 5. Harta C–gamma'''),code("Cs=np.logspace(-1,2,5); gs=np.logspace(-2,1,5); mat=np.zeros((len(Cs),len(gs)))\nfor i,C in enumerate(Cs):\n for j,g in enumerate(gs): mat[i,j]=cross_val_score(make_pipeline(StandardScaler(),SVC(C=C,gamma=g)),X,y,cv=4).mean()\nplt.imshow(mat,origin='lower',aspect='auto'); plt.xticks(range(len(gs)),[f'{g:.2g}' for g in gs]); plt.yticks(range(len(Cs)),[f'{c:.2g}' for c in Cs]); plt.xlabel('gamma'); plt.ylabel('C'); plt.colorbar(label='CV accuracy'); plt.show()"),
md(r'''## 6. Vizualizimi i kufirit RBF'''),code("p=make_pipeline(StandardScaler(),SVC(C=3,gamma='scale')).fit(X,y); xx,yy=np.meshgrid(np.linspace(-1.8,1.8,250),np.linspace(-1.8,1.8,250)); zz=p.predict(np.c_[xx.ravel(),yy.ravel()]).reshape(xx.shape); plt.contourf(xx,yy,zz,alpha=.25); plt.scatter(X[:,0],X[:,1],c=y,s=12); plt.show()"),
md(r'''## 7. Rast dështimi: scaling'''),code("Xbad=X.copy(); Xbad[:,0]*=10000; print('no scaling',cross_val_score(SVC(),Xbad,y,cv=5).mean()); print('pipeline',cross_val_score(make_pipeline(StandardScaler(),SVC()),Xbad,y,cv=5).mean())"),
md(r'''## 8. Interpretimi i support vectors'''),code("m=make_pipeline(StandardScaler(),SVC(C=3,gamma='scale')).fit(X,y); svc=m[-1]; print('support vectors per class=',svc.n_support_)"),
md(r'''## 9. Ushtrime

- Derivoni gjerësinë $2/||w||$.
- Studioni numrin e support vectors ndaj C.
- Krahasoni linear, polynomial dhe RBF.
- Shpjegoni pse grid search duhet të jetë brenda development data.'''),
md(r'''## 10. Shembull i plotë

Zgjidhni C dhe gamma me GridSearchCV në development set; pastaj vlerësoni një test final të paprekur.'''),
code("Xdev,Xtest,ydev,ytest=train_test_split(X,y,test_size=.2,stratify=y,random_state=7); gs=GridSearchCV(make_pipeline(StandardScaler(),SVC()),{'svc__C':[.1,1,10,100],'svc__gamma':['scale',.1,1,10]},cv=5); gs.fit(Xdev,ydev); print(gs.best_params_,gs.best_score_,gs.score(Xtest,ytest))"),
md(r'''## 11. Playground

Shtoni outliers afër qendrës dhe studioni si ndryshon kufiri për C të vogël dhe të madh.''')]
make('07_svm.ipynb','07 — Makinat me vektorë mbështetës','Regjimet në hapësirën e fazës krijojnë një problem ku margjina dhe kerneli RBF kanë interpretim gjeometrik të qartë.','- të kuptoni margjinën dhe support vectors;\n- të eksploroni C dhe gamma;\n- të përdorni kernelin RBF;\n- të diagnostikoni scaling dhe overfitting.',cells)

# 8 PCA
cells=[md(r'''## 1. Spektra me shumë gjatësi vale'''),code("df=pd.read_csv(DATA/'synthetic_spectra.csv'); X=df.to_numpy(); wavelengths=np.array([float(c.split('_')[1]) for c in df.columns]); plt.plot(wavelengths,X[:12].T,alpha=.6); plt.xlabel('λ'); plt.ylabel('I'); plt.show()"),
md(r'''## 2. Qendrimi dhe kovarianca'''),code("mean=X.mean(0); Xc=X-mean; C=np.cov(Xc,rowvar=False); print(C.shape, np.allclose(C,C.T))"),
md(r'''## 3. PCA manuale me vlera vetjake'''),code("vals,vecs=np.linalg.eigh(C); idx=np.argsort(vals)[::-1]; vals=vals[idx]; vecs=vecs[:,idx]; ratio=vals/vals.sum(); print(ratio[:8],ratio[:3].sum())"),
code("Z=Xc@vecs[:,:3]; plt.scatter(Z[:,0],Z[:,1],s=14); plt.xlabel('PC1'); plt.ylabel('PC2'); plt.show()"),
md(r'''## 4. Loadings si forma spektrale'''),code("for j in range(3): plt.plot(wavelengths,vecs[:,j],label=f'PC{j+1}'); plt.legend(); plt.xlabel('λ'); plt.show()"),
md(r'''## 5. Rindërtimi dhe gabimi'''),code("errs=[]\nfor q in [1,2,3,5,10,20]:\n V=vecs[:,:q]; rec=(Xc@V)@V.T+mean; errs.append((q,np.mean((X-rec)**2)))\npd.DataFrame(errs,columns=['q','MSE_reconstruction'])"),
md(r'''## 6. Krahasim me scikit-learn'''),code("from sklearn.decomposition import PCA\np=PCA(n_components=5).fit(X); print(np.allclose(p.explained_variance_ratio_,ratio[:5])); print(np.abs(np.diag(p.components_@vecs[:,:5])))"),
md(r'''Shenja e komponentit është arbitrare; për këtë arsye krahasojmë produktin skalar në vlerë absolute.'''),
md(r'''## 7. SVD direkt'''),code("U,S,Vt=np.linalg.svd(Xc,full_matrices=False); print(np.allclose(S**2/(len(X)-1),vals))"),
md(r'''## 8. Rast dështimi: shkallët e ndryshme'''),code("Xmix=np.c_[Z[:,:2],10000*np.random.default_rng(1).normal(size=len(X))]; p1=PCA(2).fit(Xmix); p2=make_pipeline(StandardScaler(),PCA(2)).fit(Xmix); print('pa scaling',p1.explained_variance_ratio_)"),
md(r'''## 9. Ushtrime

- Derivoni problemin e maksimizimit $v^TCv$.
- Zgjidhni q për 95% variancë.
- Krahasoni reconstruction error me explained variance.
- Interpretoni fizikisht maksimumet e tre loadings të para.'''),
md(r'''## 10. Shembull i plotë

Kompresoni 120 kanale në q komponentë, rindërtoni spektrat dhe raportoni raportin e kompresimit dhe gabimin.'''),
md(r'''## 11. Playground

Ndryshoni amplitudat e bazave spektrale në gjenerator dhe kontrolloni si ndryshon renditja e eigenvalues.''')]
make('08_pca.ipynb','08 — PCA dhe reduktimi dimensional','Spektrat janë shembull natyror i të dhënave me shumë kolona të korreluara. PCA lidhet drejtpërdrejt me kovariancën, vlerat vetjake dhe SVD.','- të implementoni PCA manualisht;\n- të kuptoni explained variance dhe reconstruction;\n- të interpretoni loadings;\n- të dalloni kur scaling është i nevojshëm.',cells)

# 9 clustering
cells=[md(r'''## 1. Regjime atmosferike pa etiketa'''),code("df=pd.read_csv(DATA/'atmospheric_regimes.csv'); X=df[['temperatura_C','RH_pct','presioni_hPa']].to_numpy(); plt.scatter(X[:,0],X[:,1],s=14); plt.xlabel('T'); plt.ylabel('RH'); plt.show()"),
md(r'''## 2. k-means manual'''),code("from src.clustering.manual import kmeans\nXs=StandardScaler().fit_transform(X); labels,centers,history=kmeans(Xs,3,seed=0); print(centers)"),
code("plt.scatter(X[:,0],X[:,1],c=labels,s=14); plt.show()"),
md(r'''## 3. Trajektorja e qendrave'''),code("H=np.array(history); plt.scatter(Xs[:,0],Xs[:,1],c=labels,s=8,alpha=.25);\nfor j in range(3): plt.plot(H[:,j,0],H[:,j,1],marker='o'); plt.show()"),
md(r'''## 4. Krahasim me KMeans dhe k-means++'''),code("from sklearn.cluster import KMeans\nfor seed in range(5):\n m=KMeans(n_clusters=3,n_init=1,init='random',random_state=seed).fit(Xs); print(seed,m.inertia_)\nprint('kmeans++',KMeans(n_clusters=3,n_init=20,random_state=0).fit(Xs).inertia_)"),
md(r'''## 5. Zgjedhja e K'''),code("from sklearn.metrics import silhouette_score\nrows=[]\nfor k in range(2,8):\n m=KMeans(k,n_init=20,random_state=0).fit(Xs); rows.append((k,m.inertia_,silhouette_score(Xs,m.labels_)))\nr=pd.DataFrame(rows,columns=['k','inertia','silhouette']); r"),
code("fig,ax=plt.subplots(); ax.plot(r.k,r.inertia,marker='o'); ax.set_xlabel('k'); ax.set_ylabel('inertia'); plt.show(); plt.plot(r.k,r.silhouette,marker='o'); plt.xlabel('k'); plt.ylabel('silhouette'); plt.show()"),
md(r'''## 6. Grupimi hierarkik'''),code("from scipy.cluster.hierarchy import linkage,dendrogram\nZ=linkage(Xs[:120],method='ward'); plt.figure(figsize=(10,4)); dendrogram(Z,no_labels=True); plt.show()"),
md(r'''## 7. Rast dështimi: forma jo-sferike'''),code("from sklearn.datasets import make_moons\nXm,ym=make_moons(500,noise=.06,random_state=0); km=KMeans(2,n_init=20,random_state=0).fit(Xm); plt.scatter(Xm[:,0],Xm[:,1],c=km.labels_,s=12); plt.title('k-means mbi gjysmëhëna'); plt.show()"),
md(r'''## 8. Standardizimi si zgjedhje modeli'''),code("m1=KMeans(3,n_init=20,random_state=0).fit(X); m2=KMeans(3,n_init=20,random_state=0).fit(Xs); print('silhouette raw=',silhouette_score(StandardScaler().fit_transform(X),m1.labels_),'scaled=',silhouette_score(Xs,m2.labels_))"),
md(r'''## 9. Ushtrime

- Provoni 20 inicializime manuale.
- Krahasoni `single`, `complete`, `average`, `ward`.
- Hiqni presionin dhe shihni nëse grupet mbeten.
- Jepni një argument fizik pse tre cluster-e mund të jenë artefakt.'''),
md(r'''## 10. Shembull i plotë

Ndërtoni një raport të grupimit pa përdorur etiketën e fshehtë: zgjedhni k, analizoni stabilitetin dhe përshkruani çdo grup në njësitë fizike origjinale.'''),
md(r'''## 11. Playground

Vetëm në fund përdorni kolonën `regjim_i_fshehtë` për të parë sa përputhet struktura numerike me mekanizmin që gjeneroi të dhënat. Diskutoni pse kjo nuk do të ishte e disponueshme në një problem real unsupervised.''')]
make('09_grupimi.ipynb','09 — Grupimi dhe zbulimi i strukturës','Të dhënat atmosferike përdoren për të treguar se clustering zbulon strukturë sipas një kriteri, jo ``etiketa të vërteta'' automatikisht.','- të implementoni k-means;\n- të studioni inicializimin dhe K;\n- të përdorni silhouette dhe dendrogram;\n- të njihni rastet ku k-means dështon.',cells)

# 10 comparison uncertainty
cells=[md(r'''## 1. Një dataset, pesë modele'''),code("df=pd.read_csv(DATA/'physics_model_comparison.csv'); X=df.drop(columns='signal'); y=df.signal; df.head()"),
md(r'''## 2. Test final i paprekur'''),code("Xdev,Xtest,ydev,ytest=train_test_split(X,y,test_size=.2,stratify=y,random_state=2026); print(len(Xdev),len(Xtest))"),
md(r'''## 3. Modelet dhe pipelines'''),code("from sklearn.linear_model import LogisticRegression\nfrom sklearn.neighbors import KNeighborsClassifier\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.svm import SVC\nmodels={'LogReg':make_pipeline(StandardScaler(),LogisticRegression(max_iter=3000)),'kNN':make_pipeline(StandardScaler(),KNeighborsClassifier(11)),'Tree':DecisionTreeClassifier(max_depth=5,random_state=0),'RF':RandomForestClassifier(n_estimators=250,random_state=0),'SVM':make_pipeline(StandardScaler(),SVC(probability=True,C=3))}"),
md(r'''## 4. Cross-validation me të njëjtat fold-e'''),code("from sklearn.metrics import make_scorer,roc_auc_score\ncv=StratifiedKFold(8,shuffle=True,random_state=1); rows=[]\nfor name,m in models.items():\n r=cross_validate(m,Xdev,ydev,cv=cv,scoring=['accuracy','roc_auc'],return_train_score=True); rows.append({'model':name,'train_acc':r['train_accuracy'].mean(),'cv_acc':r['test_accuracy'].mean(),'cv_acc_sd':r['test_accuracy'].std(),'cv_auc':r['test_roc_auc'].mean(),'fit_s':r['fit_time'].mean()})\nres=pd.DataFrame(rows).set_index('model'); res"),
md(r'''## 5. Nuk ka vetëm një fitues'''),code("res[['cv_acc','cv_acc_sd','cv_auc','fit_s']].plot.bar(figsize=(9,4)); plt.show()"),
md(r'''## 6. Ndjeshmëria ndaj scaling'''),code("for k in [3,11,31]: print(k,cross_val_score(KNeighborsClassifier(k),Xdev,ydev,cv=cv).mean(),cross_val_score(make_pipeline(StandardScaler(),KNeighborsClassifier(k)),Xdev,ydev,cv=cv).mean())"),
md(r'''## 7. Robustësia ndaj zhurmës'''),code("rng=np.random.default_rng(5); scales=[0,.1,.3,.6]; robust=[]\nfor s in scales:\n Xn=Xdev.copy(); Xn.iloc[:,:3]=Xn.iloc[:,:3]+rng.normal(0,s,Xn.iloc[:,:3].shape)*Xn.iloc[:,:3].std().to_numpy();\n for name,m in models.items(): robust.append((s,name,cross_val_score(m,Xn,ydev,cv=4).mean()))\nrb=pd.DataFrame(robust,columns=['noise','model','score']); rb.pivot(index='noise',columns='model',values='score').plot(marker='o'); plt.show()"),
md(r'''## 8. Interpretueshmëria'''),code("lr=models['LogReg'].fit(Xdev,ydev); coef=pd.Series(lr[-1].coef_[0],index=X.columns); print(coef.sort_values()); rf=models['RF'].fit(Xdev,ydev); print(pd.Series(rf.feature_importances_,index=X.columns).sort_values())"),
md(r'''## 9. Bootstrap i AUC në test final'''),code("best=models['LogReg'].fit(Xdev,ydev); prob=best.predict_proba(Xtest)[:,1]; rng=np.random.default_rng(0); aucs=[]\nfor _ in range(1000):\n idx=rng.integers(0,len(ytest),len(ytest)); yt=ytest.to_numpy()[idx]; pr=prob[idx]\n if len(np.unique(yt))==2: aucs.append(roc_auc_score(yt,pr))\nprint(np.mean(aucs),np.percentile(aucs,[2.5,97.5]))"),
md(r'''## 10. Data leakage demonstrim'''),code("# Përzgjedhja e një veçorie zhurme sipas të gjithë dataset-it do të ishte metodologjikisht e gabuar.\nprint('Kolona noise_feature është futur qëllimisht për kontroll interpretimi.')"),
md(r'''## 11. Testi final'''),code("for name,m in models.items(): m.fit(Xdev,ydev); print(name,m.score(Xtest,ytest))"),
md(r'''## 12. Ushtrime

- Kryeni tuning të secilit model me nested CV.
- Matni permutation importance.
- Ndryshoni klasën pozitive në 20% dhe përsëritni analizën.
- Shkruani një faqe ku zgjidhni modelin duke peshuar interpretueshmëri, stabilitet dhe performancë.'''),
md(r'''## 13. Shembull i plotë

Ky notebook është vetë shembulli i integruar. Plotësoni një tabelë vendimmarrjeje me kolonat: performancë, variabilitet, kosto, scaling, interpretueshmëri, robustësi.'''),
md(r'''## 14. Playground

Shtoni një veçori të re fizikisht informative dhe një tjetër zhurme. A i dallojnë modelet? Si ndryshojnë importance dhe koeficientët?''')]
make('10_krahasimi_i_modeleve_dhe_pasiguria.ipynb','10 — Krahasimi i modeleve, pasiguria dhe metodologjia','Një dataset i vetëm i ngjarjeve fizike përdoret për të krahasuar drejt pesë familje modelesh, duke përfshirë variabilitetin, robustësinë dhe interpretueshmërinë.','- të bëni krahasim me të njëjtat fold-e;\n- të raportoni variabilitet dhe bootstrap;\n- të testoni robustësinë;\n- të zgjidhni modelin mbi kritere shkencore.',cells)

# 11 gradient
cells=[md(r'''## 1. Një minimum kuadratik'''),code("def f(t): return t*t\ndef grad(t): return 2*t\nfor eta in [.01,.1,.8,1.1]:\n t=4.; hist=[t]\n for _ in range(25): t-=eta*grad(t); hist.append(t)\n plt.plot(hist,marker='o',ms=2,label=f'η={eta}')\nplt.legend(); plt.show()"),
md(r'''## 2. Kushti analitik

Për $L=\theta^2$, $\theta_{n+1}=(1-2\eta)\theta_n$. Konvergjenca kërkon $|1-2\eta|<1$.'''),
md(r'''## 3. Regresion linear me gradient descent'''),code("df=pd.read_csv(DATA/'gradient_regression.csv'); X=df[['x']].to_numpy(); y=df.y.to_numpy(); from src.optimization.manual import linear_gd; w,h=linear_gd(X,y,lr=.03,n_iter=1200); print(w); plt.plot(h); plt.yscale('log'); plt.show()"),
md(r'''## 4. Krahasim me OLS'''),code("m=LinearRegression().fit(X,y); print([m.intercept_,m.coef_[0]],w)"),
md(r'''## 5. Sipërfaqe e humbjes'''),code("bs=np.linspace(-2,1,120); ms=np.linspace(0,3,120); Z=np.empty((len(bs),len(ms)))\nfor i,b in enumerate(bs):\n for j,a in enumerate(ms): Z[i,j]=np.mean((b+a*X[:,0]-y)**2)\nplt.contour(ms,bs,Z,levels=25); plt.xlabel('slope'); plt.ylabel('intercept'); plt.show()"),
md(r'''## 6. Scaling dhe kondicionimi'''),code("rng=np.random.default_rng(0); X2=np.c_[rng.normal(size=500),1000*rng.normal(size=500)]; y2=2*X2[:,0]-.003*X2[:,1]+rng.normal(0,.2,500);\n# Përdorim SGDRegressor vetëm për të demonstruar ndjeshmërinë praktike.\nfrom sklearn.linear_model import SGDRegressor\nfor use_scale in [False,True]:\n mdl=make_pipeline(StandardScaler(),SGDRegressor(max_iter=3000,tol=1e-7,random_state=0)) if use_scale else SGDRegressor(max_iter=3000,tol=1e-7,random_state=0); mdl.fit(X2,y2); print(use_scale,mdl.score(X2,y2))"),
md(r'''## 7. Zbritja stokastike'''),code("rng=np.random.default_rng(1); A=np.c_[np.ones(len(X)),X]; ww=np.zeros(2); losses=[]\nfor epoch in range(30):\n for i in rng.permutation(len(X)):\n  r=A[i]@ww-y[i]; ww-=.01*2*r*A[i]\n losses.append(np.mean((A@ww-y)**2))\nprint(ww); plt.plot(losses,marker='o'); plt.show()"),
md(r'''## 8. Minibatch'''),code("def minibatch_gd(A,y,lr=.02,batch=16,epochs=100,seed=0):\n rng=np.random.default_rng(seed); w=np.zeros(A.shape[1]); hist=[]\n for _ in range(epochs):\n  for start in range(0,len(A),batch):\n   idx=rng.permutation(len(A))[start:start+batch]; r=A[idx]@w-y[idx]; w-=lr*2*A[idx].T@r/len(idx)\n  hist.append(np.mean((A@w-y)**2))\n return w,hist\nfor b in [1,8,32,len(A)]:\n _,hh=minibatch_gd(A,y,batch=b); plt.plot(hh,label=f'b={b}')\nplt.yscale('log'); plt.legend(); plt.show()"),
md(r'''## 9. Ushtrime

- Derivoni gradientin e MSE.
- Gjeni eta kritik për një funksion $a\theta^2/2$.
- Krahasoni batch sizes dhe kohën.
- Provoni schedule $\eta_t=\eta_0/(1+kt)$.'''),
md(r'''## 10. Shembull i plotë

Përshtatni të njëjtin regresion me OLS, full-batch GD dhe SGD; krahasoni koeficientët, kohën dhe trajektoren e humbjes.'''),
md(r'''## 11. Playground

Ndryshoni korelacionin e veçorive dhe vëzhgoni se si ndryshon kondicionimi dhe forma e kontureve të humbjes.''')]
make('11_zbritja_e_gradientit.ipynb','11 — Zbritja e gradientit dhe optimizimi numerik','Nga një funksion kuadratik te regresioni linear, studiojmë gradient descent si metodë të përgjithshme optimizimi dhe jo si teknikë ekskluzive e rrjetave nervore.','- të derivoni dhe implementoni gradient descent;\n- të kuptoni learning rate;\n- të lidhni scaling me kondicionimin;\n- të dalloni full-batch, SGD dhe minibatch.',cells)

# 12 perceptron
cells=[md(r'''## 1. Dataset linearisht i ndashëm'''),code("df=pd.read_csv(DATA/'perceptron_separable.csv'); X=df[['x1','x2']].to_numpy(); y=df['class'].to_numpy(); plt.scatter(X[:,0],X[:,1],c=y,s=18); plt.show()"),
md(r'''## 2. Rregulli i perceptronit

Me etiketa $y\in\{-1,+1\}$ përditësojmë vetëm kur $y(w^Tx+b)\le 0$:
$$w\leftarrow w+\eta yx,\qquad b\leftarrow b+\eta y.$$'''),
code("from src.perceptron.manual import fit_perceptron\nw,b,mist=fit_perceptron(X,y,epochs=100,seed=0); print(w,b,mist); plt.plot(mist,marker='o'); plt.xlabel('epoka'); plt.ylabel('gabime'); plt.show()"),
md(r'''## 3. Kufiri i vendimit'''),code("xx=np.linspace(X[:,0].min()-.5,X[:,0].max()+.5,200); yy=-(w[0]*xx+b)/w[1]; plt.scatter(X[:,0],X[:,1],c=y,s=18); plt.plot(xx,yy); plt.show()"),
md(r'''## 4. Krahasim me sklearn dhe regresion logjistik'''),code("from sklearn.linear_model import Perceptron,LogisticRegression\nsp=Perceptron(max_iter=1000,tol=1e-4,random_state=0).fit(X,y); lr=LogisticRegression().fit(X,y); print(sp.score(X,y),lr.score(X,y)); print('perceptron coef',sp.coef_,sp.intercept_); print('logistic',lr.coef_,lr.intercept_)"),
md(r'''## 5. Margjina dhe numri i gabimeve'''),code("# Afrojmë klasat duke zvogëluar distancën midis qendrave.\nrng=np.random.default_rng(1); rows=[]\nfor sep in [2.0,1.2,.7,.4]:\n Xs=np.r_[rng.normal([-sep/2,-sep/2],.25,(100,2)),rng.normal([sep/2,sep/2],.25,(100,2))]; ys=np.r_[np.zeros(100,dtype=int),np.ones(100,dtype=int)]; _,_,mi=fit_perceptron(Xs,ys,epochs=100,seed=0); rows.append((sep,mi.sum(),mi[-1],len(mi)))\npd.DataFrame(rows,columns=['separation','total_updates','last_mistakes','epochs'])"),
md(r'''## 6. XOR: kufiri i përfaqësimit'''),code("dx=pd.read_csv(DATA/'xor.csv'); Xx=dx[['x1','x2']].to_numpy(); yx=dx['class'].to_numpy(); wx,bx,mx=fit_perceptron(Xx,yx,epochs=40,seed=0); print('mistakes per epoch=',mx); plt.scatter(Xx[:,0],Xx[:,1],c=yx,s=150); plt.show()"),
md(r'''Rritja e epokave nuk e zgjidh XOR: problemi nuk është optimizimi por mungesa e një kufiri linear.'''),
md(r'''## 7. Një transformim veçorish'''),code("Phi=np.c_[Xx,Xx[:,0]*Xx[:,1]]; wp,bp,mp=fit_perceptron(Phi,yx,epochs=100,seed=0); print(wp,bp,mp[-10:])"),
md(r'''Ky transformim nuk është ende rrjet nervor; ai tregon se jolineariteti mund të futet në **përfaqësim**. Rrjetat me shtresa të fshehta mësojnë përfaqësime të tilla në mënyrë parametrike.'''),
md(r'''## 8. Teorema e konvergjencës: eksperiment numerik

Teorema jep kufirin $M\le(R/\gamma)^2$ kur të dhënat janë të ndashme me margjinë $\gamma$. Në notebook nuk provojmë vetëm formulën; ndryshojmë margjinën dhe shohim trendin e numrit të update-eve.'''),
md(r'''## 9. Çfarë vjen më tej — vetëm panoramë

Një shtresë e fshehtë llogarit $h=\phi(Wx+b)$. Kompozimi i shumë transformimeve jep MLP. Gradientët llogariten efikasisht me **prapapërhapje (backpropagation)**. CNN përdorin konvolucion; rrjetat rekurrente trajtojnë sekuenca; Transformer përdorin attention. Këto tema do të trajtohen rigorozisht në kursin pasues, jo këtu.'''),
md(r'''## 10. Ushtrime

- Implementoni perceptronin pa modul ndihmës.
- Provoni renditje të ndryshme të pikave dhe krahasoni numrin e update-eve.
- Krahasoni perceptronin me linear SVM.
- Shpjegoni me një skicë si dy njësi të fshehta mund të ndihmojnë XOR.'''),
md(r'''## 11. Shembull i plotë

Zgjidhni një dataset linearisht të ndashëm, trajnojeni manualisht, raportoni numrin e gabimeve, vizatoni kufirin dhe krahasoni me SVM dhe logistic regression.'''),
md(r'''## 12. Playground

Krijoni vetë dy klasa me margjina të ndryshme, outliers dhe zhurmë etiketash. Kur perceptroni nuk konvergon? Çfarë do të bënte SVM me margjinë të butë?''')]
make('12_perceptroni.ipynb','12 — Perceptroni dhe ura drejt rrjetave nervore','Perceptroni mbyll trajtimin formal të kursit: një klasifikues linear online me teoremë konvergjence dhe kufizim të qartë në XOR.','- të implementoni perceptronin;\n- të kuptoni konvergjencën dhe margjinën;\n- të demonstroni kufizimin XOR;\n- të kuptoni në mënyrë përshkruese rrugën drejt MLP dhe deep learning.',cells)

print('notebooks built',len(list(NB.glob('*.ipynb'))))
