# Raport i kontrollit të cilësisë

## Manuali
- 12 kapituj kryesorë, saktësisht sipas 12 temave të kursit.
- Çdo kapitull ka 6 seksione ose më pak; në versionin aktual secili ka 6.
- Perceptroni është tema e fundit kryesore; zhvillimet e rrjetave nervore janë vetëm panoramë përshkruese.
- Glossar trekolonësh: termi shqip, termi anglisht, shpjegimi.
- Përdorim i terminologjisë `stokastik/stokastike/stokasticitet`.
- PDF kompilon me `pdflatex`; versioni aktual: 87 faqe A4.
- PDF u renderua në PNG për kontroll vizual të faqosjes.

## Notebook-et
- 12 notebook-e kryesore, një për temë.
- Të gjithë skedarët `.ipynb` janë JSON të vlefshëm dhe të gjitha qelizat Python kalojnë kontrollin sintaksor.
- Gjatë ndërtimit u krye ekzekutim teknik i notebook-eve për të kontrolluar rrjedhën e plotë; versionet e ekzekutuara nuk përfshihen në paketën përfundimtare për të shmangur dublikimet.
- Farat e rastësisë janë të kontrolluara në dataset-et/eksperimentet kryesore.
- Notebook 10 përdor të njëjtin dataset/fold-e për krahasimin Logistic Regression, k-NN, Decision Tree, Random Forest dhe SVM.

## Të dhënat dhe kodi
- Dataset-et sintetike janë fizikisht të motivuara dhe ruhen në `datasets/synthetic/`.
- Implementimet manuale të OLS/Ridge/polinomeve, regresionit logjistik, k-NN, Gini, PCA, k-means, gradient descent dhe perceptronit janë në `src/`.
- SVM dhe Random Forest përdorin solver-at e bibliotekës pas trajtimit matematik, sipas objektivit të nivelit Bachelor.

## Burimet
- Ekziston `SOURCE_INTEGRATION_MATRIX.md` për hartëzimin temë-burim.
- Ekziston `SOURCES_AND_INSPIRATION.md` për atribuim dhe dokumentimin e adaptimit.
