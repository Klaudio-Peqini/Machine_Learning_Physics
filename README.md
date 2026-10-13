# Nxënia Automatike për Fizikë                                         

Kurs Bachelor (Fizikë dhe Shkenca Kompjuterike) i ndërtuar rreth 12 temave, nga formulimi i problemit dhe validimi deri te perceptroni. Rrjetat nervore përmenden vetëm në mënyrë përshkruese pas perceptronit; trajtimi i plotë lihet për ciklin Master.

## Filozofia

**Pyetje fizike → të dhëna → model matematik → algoritëm → implementim → validim → krahasim modelesh → interpretim fizik.**

Në laborator: **matematikë → implementim nga parimet e para → implementim me bibliotekë → krahasim numerik → interpretim shkencor.**

## Struktura

- `lectures/` - manuali LaTeX dhe PDF.
- `notebooks/` - 12 notebook-e, një për çdo temë.
- `datasets/` - të dhëna sintetike fizike të riprodhueshme.
- `src/` - implementime didaktike nga parimet e para.
- `exercises/` - ushtrime dhe zgjidhje.
- `projects/` - propozime projektesh.
- `SOURCE_INTEGRATION_MATRIX.md` - roli i secilit kurs burimor.
- `SOURCES_AND_INSPIRATION.md` - burimet, adaptimet dhe atribuimi.

## Instalimi

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
jupyter lab
```

## Rendi i notebook-eve

1. Hyrje, të dhëna dhe validim
2. Regresioni linear
3. Regresioni polinomial, Ridge, Lasso
4. Klasifikimi dhe regresioni logjistik
5. k-NN
6. Pemët dhe ansamblet
7. SVM
8. PCA
9. Grupimi
10. Krahasimi i modeleve dhe pasiguria
11. Zbritja e gradientit
12. Perceptroni

Notebook-et janë të menduara për rreth 1.5-2 orë laborator të udhëhequr plus punë individuale. Ato nuk janë tutoriale të shkurtra të `scikit-learn`: algoritmet kryesore implementohen fillimisht manualisht.

## Riprodhueshmëria

Dataset-et sintetike gjenerohen me fara të kontrolluara. Notebook-et përdorin pipeline kur ka preprocessing, dhe bashkësia e provës mbahet e paprekur deri në vlerësimin final. Versionet kryesore të varësive janë në `requirements.txt` dhe `environment.yml`.
