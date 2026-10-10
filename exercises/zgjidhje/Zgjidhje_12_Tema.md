# Udhëzime dhe zgjidhje - 12 temat

Ky dokument jep boshtin e zgjidhjes. Për ushtrimet numerike, studentët duhet të paraqesin edhe llogaritjet, figurat dhe interpretimin.

## Tema 1
1. Matjet e së njëjtës mostër nuk janë të pavarura; përdoret GroupKFold sipas mostrës. 2. Nëse mesatarja/devijimi llogaritet para ndarjes, prova ndikon transformimin; scaler duhet të jetë brenda pipeline-it. 3. Baseline: `DummyClassifier` me prior ose klasën më të shpeshtë, raportuar me balanced accuracy/PR sipas qëllimit. 4. Parametri mësohet nga të dhënat; hiperparametri zgjidhet nga procedura e validimit; madhësia e matur është variabël fizike e dataset-it.

## Tema 2
1. Nga $S=(y-X\beta)^T(y-X\beta)$, vendosja e gradientit $-2X^T(y-X\beta)=0$ jep $X^TX\hat\beta=X^Ty$. 2. Pjerrësia është vlerësimi i $k$; mbetjet duhet të kontrollohen për strukturë. 3. Ekuacionet normale japin $X^Tr=0$. 4. Me varianca të njohura përdoret WLS me $W=\mathrm{diag}(1/\sigma_i^2)$.

## Tema 3
1. Rreshti është $[1,x,x^2,x^3,x^4]$. 2. Fuqitë mund të jenë fort të korreluara dhe të prodhojnë vlera singulare të vogla. 3. Ridge: $(X^TX+\lambda I)^{-1}X^Ty$ (me kujdes ndaj interceptit). 4. Ridge i tkurr së bashku; Lasso mund të zgjedhë një prej veçorive të korreluara dhe të jetë jo stabil.

## Tema 4
1. Për $p=\sigma(Xw)$, gradienti mesatar është $X^T(p-y)/N$. 2. Accuracy=0.92, precision=0.75, recall=0.90; specifika=74/80=0.925; $F_1\approx0.818$. 3. Në klasë shumë të rrallë, parashikimi gjithmonë negativ mund të ketë accuracy të lartë. 4. Pragu kodon kostot/objektivin; probabiliteti është dalje e modelit.

## Tema 5
1. Llogarit distancat, merr tre indekset më të vogla dhe voton. 2. Një kolonë me amplitudë numerike shumë më të madhe dominon normën Euklidiane. 3. $k$ i vogël: variancë e lartë; $k$ i madh: bias i lartë. 4. Pritet degradim për shkak të mallkimit të dimensionalitetit.

## Tema 6
1. $G=1-(0.7^2+0.3^2)=0.42$. 2. Zgjidhet ndarja me uljen më të madhe të impurity të ponderuar. 3. Mesatarizimi i estimatorëve të pakorreluar ul variancën. 4. Impurity importance mund të favorizojë veçori me shumë ndarje; permutation lidhet me rënien e performancës jashtë mostrës.

## Tema 7
1. Margjina është distanca minimale nga hiperplani te pikat më të afërta; zgjidhet maksimumi. 2. $C$ i madh penalizon shkeljet fort; $C$ i vogël regularizon më shumë. 3. Kerneli llogarit ngjashmëri që korrespondon me produkt skalar në një përfaqësim më të pasur pa e ndërtuar atë shprehimisht. 4. $\gamma$ i madh jep ndikim lokal; tuning bëhet bashkë me $C$.

## Tema 8
1-2. Qendërzohet matrica, llogaritet $C=X^TX/(N-1)$, diagonalizohet dhe projektohet $z=Xv_1$. 3. Nëse $v$ është vektor vetjak, edhe $-v$ është; projekcioni ndryshon shenjë, jo informacionin. 4. Standardizimi është i dobishëm kur njësitë/shkallët janë arbitrare; mund të jetë i gabuar kur amplitudat absolute kanë kuptim fizik që duhet ruajtur.

## Tema 9
1. Caktim te centroidi më i afërt, pastaj mesatarja e pikave të grupit; përsëritet. 2. Objektivi nuk është konveks globalisht ndaj centroidëve dhe etiketave së bashku. 3. Prerja lart jep pak makro-grupe; më poshtë jep nënstruktura. 4. Dy hëna, unaza koncentrike ose dendësi shumë të ndryshme janë raste tipike të papërshtatshme.

## Tema 10
1. Të njëjtat split-e/fold-e, preprocessing në pipeline, tuning i brendshëm, test i paprekur. 2. Rimarrje me zëvendësim e test set dhe llogaritje e AUC për secilën rimarrje. 3. Zhvendos një veçori sipas drift-it instrumental ose teston një sesion tjetër. 4. Duhet peshuar stabiliteti, kalibrimi, interpretueshmëria, kostoja dhe robustësia.

## Tema 11
1. $|1-a\eta|<1\Rightarrow0<\eta<2/a$. 2. $\nabla L=2X^T(X\beta-y)/N$. 3. Batch ka gradient të saktë por hap të kushtueshëm; stokastiku është i lirë e me variancë; mini-batch kompromis. 4. Raporti i vlerave vetjake të Hessian-it përcakton anisotropinë dhe zigzag-un.

## Tema 12
1. Për çdo gabim: $w\leftarrow w+\eta yx$, $b\leftarrow b+\eta y$. 2. Projekcioni mbi ndarësin ideal rritet të paktën $\gamma$ për gabim, ndërsa norma rritet jo më shpejt se $R\sqrt M$, prandaj $M\le(R/\gamma)^2$. 3. Klasat alternohen në cepat e katrorit; nuk ka një vijë ndarëse. 4. Perceptroni: rregull gabimi dhe dalje e fortë; logjistiku: likelihood/cross-entropy dhe probabilitet; SVM: margjinë maksimale dhe hinge loss.
