# Ushtrime - 12 temat

## Tema 1 - Të dhënat dhe validimi
1. Një eksperiment ka 20 matje për secilin prej 30 mostrave fizike. Shpjegoni pse ndarja e rreshtave në mënyrë të rastësishme mund të japë vlerësim optimist dhe propozoni skemë më të drejtë.
2. Jepni një shembull të rrjedhjes së informacionit gjatë standardizimit.
3. Ndërtoni një baseline për klasifikim kur klasa pozitive është 8%.
4. Shpjegoni dallimin midis parametrit, hiperparametrit dhe madhësisë së matur.

## Tema 2 - Regresioni linear
1. Derivoni ekuacionet normale nga minimizimi i shumës së mbetjeve katrore.
2. Për $F=kx+b$, llogaritni $k,b$ nga një tabelë me katër matje dhe kontrolloni mbetjet.
3. Tregoni gjeometrikisht pse mbetja OLS është ortogonale me hapësirën e kolonave të $X$.
4. Diskutoni çfarë ndryshon kur pasiguria e çdo pike është e ndryshme.

## Tema 3 - Regresioni polinomial dhe regularizimi
1. Ndërtoni matricën e dizajnit për polinom të shkallës 4.
2. Shpjegoni pse kolonat $x,x^2,x^3$ mund të krijojnë kushtëzim të dobët.
3. Derivoni zgjidhjen Ridge.
4. Krahasoni konceptualisht Ridge dhe Lasso kur dy veçori janë fort të korreluara.

## Tema 4 - Klasifikimi dhe regresioni logjistik
1. Derivoni gradientin e binary cross-entropy për modelin logjistik.
2. Ndërtoni confusion matrix nga 100 ngjarje me TP=18, FP=6, FN=2, TN=74 dhe llogaritni metrikat kryesore.
3. Jepni një rast ku accuracy është metrikë mashtruese.
4. Shpjegoni pse zgjedhja e pragut është problem vendimmarrjeje dhe jo pjesë e vetë probabilitetit.

## Tema 5 - k-NN
1. Implementoni votimin e shumicës për $k=3$ pa përdorur sklearn.
2. Tregoni me një shembull numerik pse standardizimi ndryshon distancat.
3. Diskutoni kompromisin për $k$ të vogël dhe të madh.
4. Shtoni 20 veçori zhurme dhe studioni performancën.

## Tema 6 - Pemët dhe ansamblet
1. Llogaritni Gini për një nyje me 7 mostra të klasës A dhe 3 të klasës B.
2. Krahasoni dy ndarje të mundshme përmes fitimit në impurity.
3. Shpjegoni pse bagging ul variancën.
4. Krahasoni impurity importance me permutation importance.

## Tema 7 - SVM
1. Për dy hiperplane ndarëse, gjeni cili ka margjinën më të madhe.
2. Shpjegoni rolin e $C$ në soft-margin SVM.
3. Shpjegoni intuitivisht kernel trick pa përdorur formalizëm RKHS.
4. Studioni bashkë efektin e $C$ dhe $\gamma$ në RBF-SVM.

## Tema 8 - PCA
1. Llogaritni matricën e kovariancës për tre pika dy-dimensionale të qendërzuara.
2. Gjeni vlerat dhe vektorët vetjakë dhe projektoni pikat mbi komponentin e parë.
3. Shpjegoni pse shenja e një komponenti PCA nuk është unike.
4. Diskutoni kur standardizimi para PCA është i përshtatshëm dhe kur mund të fshehë kuptimin fizik.

## Tema 9 - Grupimi
1. Kryeni me dorë dy iteracione të k-means për gjashtë pika.
2. Shpjegoni pse inicializimi mund të ndryshojë zgjidhjen.
3. Interpretoni një dendrogramë dhe dy prerje të ndryshme të saj.
4. Jepni një shembull gjeometrik ku k-means pritet të dështojë.

## Tema 10 - Krahasimi, pasiguria dhe interpretimi
1. Projektoni një benchmark të drejtë të pesë klasifikuesve.
2. Përshkruani bootstrap-in e AUC.
3. Jepni një test stresi për domain shift.
4. Shpjegoni pse modeli me score më të lartë nuk është domosdoshmërisht modeli shkencërisht më i mirë.

## Tema 11 - Zbritja e gradientit
1. Për $L(\theta)=a\theta^2/2$, gjeni intervalin e learning rate që garanton konvergjencë.
2. Derivoni gradientin e MSE për regresion linear matricor.
3. Krahasoni batch, zbritjen stokastike dhe mini-batch.
4. Shpjegoni lidhjen midis kushtëzimit të Hessian-it dhe shpejtësisë së konvergjencës.

## Tema 12 - Perceptroni
1. Ekzekutoni me dorë tre përditësime perceptroni në një dataset të vogël.
2. Përmblidhni provën e teoremës së konvergjencës.
3. Tregoni pse XOR nuk është linearisht i ndashëm.
4. Krahasoni perceptronin, regresionin logjistik dhe SVM sipas objektivit, probabilitetit dhe margjinës.
