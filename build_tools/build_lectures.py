from pathlib import Path
ROOT=Path('/mnt/data/Machine_Learning_Physics')
L=ROOT/'lectures'

def esc(s): return s

preamble=r'''\documentclass[11pt,a4paper,oneside]{book}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{microtype}
\usepackage{amsmath,amssymb,mathtools,bm}
\usepackage{graphicx}
\usepackage{booktabs,longtable,array,tabularx}
\usepackage{enumitem}
\usepackage{geometry}
\usepackage{setspace}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{caption}
\usepackage{float}
\usepackage{siunitx}
\usepackage{listings}
\usepackage{titlesec}
\geometry{margin=2.35cm,headheight=14pt}
\setstretch{1.08}
\hypersetup{colorlinks=true,linkcolor=black,urlcolor=blue,citecolor=black}
\setcounter{secnumdepth}{2}
\setcounter{tocdepth}{1}
\setlist[itemize]{topsep=4pt,itemsep=2pt}
\pagestyle{fancy}\fancyhf{}\fancyhead[L]{Nxënia automatike për Fizikë}\fancyhead[R]{\leftmark}\fancyfoot[C]{\thepage}
\titleformat{\chapter}[display]{\bfseries\Large}{\filright\MakeUppercase{Tema \thechapter}}{0.7ex}{\titlerule\vspace{1ex}\Huge}
\newcommand{\term}[2]{\textbf{#1} (\textit{#2})}
\newcommand{\R}{\mathbb{R}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\Var}{\operatorname{Var}}
\newcommand{\argmin}{\operatorname*{arg\,min}}
\lstset{basicstyle=\ttfamily\small,breaklines=true,frame=single,showstringspaces=false}
\begin{document}
\frontmatter
\begin{titlepage}
\centering
\vspace*{2cm}
{\Huge\bfseries NXËNIA AUTOMATIKE\\[0.4cm] PËR FIZIKË\par}
\vspace{0.8cm}
{\Large Leksione për studentët Bachelor në Fizikë dhe Shkenca Kompjuterike\par}
\vfill
{\large Material mësimor: 12 tema themelore, me trajtim matematik, numerik dhe fizik\par}
\vspace{0.5cm}
{\large Botim pune për kursin universitar\par}
\vfill
\end{titlepage}
\chapter*{Si të përdoret ky material}
Ky tekst është menduar si manual mësimor dhe si referencë për studime të mëtejshme. Në orën e leksionit trajtohet bërthama e çdo teme; derivimet më të gjata, diskutimet mbi kufizimet dhe shembujt shtesë shërbejnë për studim individual dhe për përgatitjen e laboratorëve. Qasja e kursit është që një problem i nxënies automatike të fillojë nga pyetja fizike dhe jo nga emri i algoritmit. Të dhënat, modeli matematik, algoritmi numerik, validimi dhe interpretimi fizik formojnë një zinxhir të vetëm arsyetimi.

Për çdo metodë kërkohet të kuptohet së pari formulimi matematik dhe vetëm pastaj implementimi. Në laborator, algoritmet kryesore ndërtohen fillimisht nga parimet e para dhe më pas krahasohen me implementimet profesionale të \texttt{scikit-learn}. Kjo ndarje e bën të dukshme diferencën midis kuptimit të një metode dhe përdorimit korrekt të një biblioteke.

Termat teknikë paraqiten në shqip, të ndjekur nga termi standard në anglisht në paraqitjen e parë. Në tekst përdoret forma \emph{stokastik/stokastike/stokasticitet}.
\tableofcontents
'''

glossary = r'''
\chapter*{Fjalorth themelor}\addcontentsline{toc}{chapter}{Fjalorth themelor}
\small
\begin{longtable}{p{0.27\textwidth}p{0.25\textwidth}p{0.42\textwidth}}
\toprule
\textbf{Termi në shqip} & \textbf{English term} & \textbf{Përkufizim / shpjegim i shkurtër}\\
\midrule\endfirsthead
\toprule\textbf{Termi në shqip} & \textbf{English term} & \textbf{Përkufizim / shpjegim i shkurtër}\\\midrule\endhead
Nxënia automatike & Machine learning & Familje metodash që ndërtojnë rregulla parashikuese ose përshkruese nga të dhënat, pa specifikuar në mënyrë të drejtpërdrejtë çdo rregull vendimmarrjeje.\\
Nxënia e mbikëqyrur & Supervised learning & Nxënie nga çifte hyrje--objektiv, ku për secilin shembull trajnimi njihet vlera që duhet parashikuar.\\
Nxënia e pambikëqyrur & Unsupervised learning & Nxënie nga të dhëna pa etiketa, me synim zbulimin e strukturës, grupeve ose përfaqësimeve me dimension më të ulët.\\
Shembull / vrojtim & Sample / observation & Një matje, ngjarje ose objekt i vetëm në bashkësinë e të dhënave.\\
Veçori & Feature & Madhësi e matur ose e ndërtuar që përdoret si hyrje e modelit.\\
Vektor veçorish & Feature vector & Vektori $\mathbf{x}$ që përmbledh veçoritë e një shembulli.\\
Ndryshore objektiv & Target variable & Madhësia që modeli përpiqet të parashikojë në një problem të mbikëqyrur.\\
Etiketë & Label & Kategori diskrete që i bashkëngjitet një shembulli në klasifikim.\\
Parametër modeli & Model parameter & Madhësi që përcaktohet nga të dhënat gjatë trajnimit, p.sh. koeficientët e regresionit.\\
Hiperparametër & Hyperparameter & Madhësi e zgjedhur jashtë procesit të përshtatjes së parametrave, p.sh. $k$ te k-NN ose $C$ te SVM.\\
Bashkësi trajnimi & Training set & Pjesa e të dhënave që përdoret për përcaktimin e parametrave të modelit.\\
Bashkësi validimi & Validation set & Të dhëna të mbajtura veç për përzgjedhjen e modelit ose të hiperparametrave.\\
Bashkësi prove & Test set & Të dhëna të papërdorura gjatë zgjedhjes së modelit, që shërbejnë për vlerësimin përfundimtar.\\
Validim i kryqëzuar & Cross-validation & Procedurë që përsërit ndarjen trajnim/validim për të vlerësuar performancën dhe variabilitetin e saj.\\
Rrjedhje informacioni & Data leakage & Futje e paqëllimshme e informacionit nga prova/validimi në trajnim, duke dhënë rezultate tepër optimiste.\\
Përgjithësim & Generalization & Aftësia e modelit për të funksionuar mirë në të dhëna të reja nga i njëjti mekanizëm gjenerues.\\
Mbipërshtatje & Overfitting & Gjendje ku modeli përshtat edhe luhatjet rastësore të trajnimit dhe humbet performancë në të dhëna të reja.\\
Nënpërshtatje & Underfitting & Gjendje ku modeli është tepër i thjeshtë për të përfaqësuar strukturën relevante të problemit.\\
Anshmëri & Bias & Gabim sistematik i shkaktuar nga kufizimet ose supozimet e modelit.\\
Variancë & Variance & Ndjeshmëria e modelit ndaj ndryshimeve në bashkësinë e trajnimit.\\
Kompromisi anshmëri--variancë & Bias--variance trade-off & Ekuilibër midis thjeshtësisë së modelit dhe ndjeshmërisë së tij ndaj të dhënave.\\
Funksion humbjeje & Loss function & Madhësi që mat mospërputhjen midis parashikimit dhe objektivit për një ose më shumë shembuj.\\
Rrezik empirik & Empirical risk & Mesatarja e humbjes mbi të dhënat e vëzhguara.\\
Regularizim & Regularization & Modifikim i kriterit të përshtatjes për të kufizuar kompleksitetin dhe për të përmirësuar përgjithësimin.\\
Regresion & Regression & Parashikim i një madhësie të vazhdueshme.\\
Klasifikim & Classification & Parashikim i një kategorie diskrete.\\
Kufi vendimi & Decision boundary & Sipërfaqja që ndan rajonet e hapësirës së veçorive të cilave modeli u jep klasa të ndryshme.\\
Matrica e konfuzionit & Confusion matrix & Tabelë që numëron parashikimet e sakta dhe të gabuara për secilën klasë.\\
Saktësi & Accuracy & Pjesa e përgjithshme e parashikimeve të sakta.\\
Precizion & Precision & Pjesa e parashikimeve pozitive që janë vërtet pozitive.\\
Ndjeshmëri / rikujtim & Recall / sensitivity & Pjesa e rasteve pozitive reale që identifikohen nga modeli.\\
Specifikë & Specificity & Pjesa e rasteve negative reale që identifikohen saktë.\\
F1 & F1 score & Mesatare harmonike e precizionit dhe rikujtimit.\\
Kurba ROC & ROC curve & Varësia e ndjeshmërisë nga norma e pozitivëve të rremë kur ndryshohet pragu i vendimit.\\
AUC & Area under the ROC curve & Sipërfaqja nën kurbën ROC; masë e renditjes së shembujve pozitivë kundrejt negativëve.\\
Shkallëzim & Scaling & Transformim i veçorive në shkallë numerike të krahasueshme.\\
Standardizim & Standardization & Transformim tipik $z=(x-\mu)/\sigma$.\\
Tubacion & Pipeline & Zinxhir i përcaktuar i përpunimit dhe modelimit që përsëritet në mënyrë identike brenda validimit.\\
Fqinjët më të afërt & Nearest neighbours & Shembujt e trajnimit që minimizojnë një metrikë distance ndaj pikës së re.\\
Mallkimi i dimensionalitetit & Curse of dimensionality & Degradim i kuptimit të distancës dhe rritje e të dhënave të nevojshme kur dimensioni rritet.\\
Pemë vendimi & Decision tree & Model që ndan hapësirën e veçorive me pyetje të njëpasnjëshme.\\
Papastërti Gini & Gini impurity & Masë e përzierjes së klasave në një nyje të pemës.\\
Entropi & Entropy & Masë informacioni që përdoret për të matur heterogjenitetin e klasave.\\
Ansambël & Ensemble & Kombinim i disa modeleve bazë për të përmirësuar stabilitetin ose saktësinë.\\
Bagging & Bagging & Trajnim i modeleve mbi mostra bootstrap dhe kombinim i parashikimeve të tyre.\\
Pyll i rastësishëm & Random forest & Ansambël pemësh me bootstrap dhe zgjedhje të rastësishme të veçorive në ndarje.\\
Boosting & Boosting & Ndërtim sekuencial i modeleve që korrigjojnë gabimet e modeleve të mëparshme.\\
Makinë me vektorë mbështetës & Support Vector Machine & Klasifikues që maksimizon margjinën midis klasave, me regularizim për raste jo të ndashme.\\
Margjinë & Margin & Distanca gjeometrike midis kufirit të vendimit dhe shembujve më të afërt relevantë.\\
Vektor mbështetës & Support vector & Shembull trajnimi që përcakton zgjidhjen e SVM-së.\\
Bërthamë & Kernel & Funksion që llogarit produkte skalare në një hapësirë të transformuar pa e ndërtuar atë shprehimisht.\\
Analiza e komponentëve kryesorë & Principal Component Analysis & Transformim linear që gjen drejtimet ortogonale me variancën më të madhe.\\
Komponent kryesor & Principal component & Drejtim i hapësirës së veçorive i përcaktuar nga një vektor vetjak i kovariancës.\\
Variancë e shpjeguar & Explained variance & Pjesa e variancës totale e kapur nga një komponent ose grup komponentësh.\\
Grupim & Clustering & Ndarje e të dhënave pa etiketa në grupe sipas një kriteri ngjashmërie.\\
Qendër grupi & Centroid & Mesatarja vektoriale e pikave të një grupi në k-means.\\
Dendrogramë & Dendrogram & Paraqitje pemore e bashkimeve në grupimin hierarkik.\\
Bootstrap & Bootstrap & Rimostrim me zëvendësim për të studiuar variabilitetin e një vlerësuesi.\\
Pasiguri aleatorike & Aleatoric uncertainty & Variabilitet që buron nga rastësia e procesit ose matjes dhe nuk hiqet thjesht me më shumë të dhëna.\\
Pasiguri epistemike & Epistemic uncertainty & Pasiguri e lidhur me njohurinë e kufizuar për modelin ose parametrat, që mund të zvogëlohet me të dhëna më informative.\\
Kalibrim & Calibration & Përputhja midis probabiliteteve të parashikuara dhe frekuencave empirike.\\
Interpretueshmëri & Interpretability & Aftësia për të lidhur sjelljen e modelit me veçori, shembuj ose mekanizma të kuptueshëm.\\
Zbritje e gradientit & Gradient descent & Algoritëm optimizimi që lëviz parametrat në drejtimin e kundërt të gradientit të humbjes.\\
Shpejtësi e të nxënit & Learning rate & Madhësia e hapit në një metodë iteruese të optimizimit.\\
Zbritje stokastike e gradientit & Stochastic gradient descent & Variant ku gradienti vlerësohet nga një shembull ose minibashkësi e rastësishme.\\
Perceptron & Perceptron & Klasifikues linear me rregull përditësimi të peshave kur një shembull klasifikohet gabim.\\
Ndashmëri lineare & Linear separability & Ekzistenca e një hiperplani që ndan pa gabime klasat në hapësirën e veçorive.\\
\bottomrule
\end{longtable}
\normalsize
'''

chapters=[]

def ch(title, sections):
    body='\\chapter{'+title+'}\n'
    for st,txt in sections:
        body+='\\section{'+st+'}\n'+txt+'\n'
    return body

chapters.append(ch('Hyrje në nxënien automatike, të dhënat dhe validimi',[
('Nga pyetja fizike te problemi i nxënies automatike',r'''
Në fizikë, një algoritëm nuk është pika e nisjes. Pika e nisjes është një pyetje që mund të formulohet qartë: a mund të vlerësojmë një parametër të panjohur nga matje të zhurmshme; a mund të dallojmë sinjalin nga sfondi në një detektor; a ekzistojnë regjime të ndryshme në një seri matjesh pa pasur etiketa paraprake? Vetëm pasi pyetja fizike është bërë e matshme, mund të vendosim nëse problemi kërkon \term{regresion}{regression}, \term{klasifikim}{classification}, \term{grupim}{clustering} ose \term{reduktim dimensionaliteti}{dimensionality reduction}. Kjo disiplinë e formulimit është thelbësore: një model shumë i saktë që zgjidh pyetjen e gabuar nuk ka vlerë shkencore.

Le të shkruajmë bashkësinë e të dhënave të mbikëqyrura si
\[
\mathcal D=\{(\mathbf{x}_i,y_i)\}_{i=1}^{N},
\]
ku $\mathbf{x}_i\in\R^d$ është \term{vektori i veçorive}{feature vector}, ndërsa $y_i$ është ndryshorja objektiv. Një model parametrik paraqitet si $\hat y=f(\mathbf{x};\boldsymbol\theta)$. Procesi i të nxënit kërkon parametra që minimizojnë një kriter të matshëm,
\[
\boldsymbol\theta^*=\argmin_{\boldsymbol\theta}\;\mathcal L(\boldsymbol\theta;\mathcal D).
\]
Kjo shprehje do të rishfaqet në regresionin linear, regresionin logjistik dhe optimizimin numerik; në metoda të tjera, si pemët ose k-NN, ideja e minimizimit është më pak e dukshme por pyetja mbi performancën jashtë trajnimit mbetet e njëjtë.

Në një eksperiment real, veçoritë nuk janë numra abstraktë. Ato mund të jenë energjia e depozituar, amplituda e një impulsi, temperatura, lagështia, një koeficient spektral ose një madhësi e nxjerrë nga një trajektore. Përzgjedhja e tyre duhet të respektojë fiziken dhe procedurën e matjes. Një veçori që përmban informacion të disponueshëm vetëm pas ngjarjes që duam të parashikojmë krijon \term{rrjedhje informacioni}{data leakage}, edhe nëse numerikisht jep rezultate mbresëlënëse.
'''),
('Përfaqësimi i të dhënave dhe përpunimi paraprak',r'''
Matrica e të dhënave shkruhet zakonisht $X\in\R^{N\times d}$, ku rreshtat janë shembuj dhe kolonat janë veçori. Para modelimit duhet të kontrollohen njësitë, vlerat e munguara, matjet jashtë diapazonit fizik dhe dublikimet. Në laboratorin shkencor kjo fazë nuk mund të trajtohet si ``pastrim'' mekanik: një pikë e largët mund të jetë gabim instrumenti, por mund të jetë po aq mirë një ngjarje e rrallë me rëndësi fizike.

Shumë algoritme varen nga distanca ose nga madhësia e koeficientëve dhe, për këtë arsye, nga shkalla numerike e veçorive. \term{Standardizimi}{standardization}
\[
z_j=\frac{x_j-\mu_j}{s_j}
\]
zhvendos mesataren rreth zeros dhe e mat çdo veçori në njësi të devijimit standard. Kjo është veçanërisht e rëndësishme për k-NN, SVM me kernel radial, regresionin e regularizuar dhe metodat me gradient. Parametrat $\mu_j$ dhe $s_j$ duhet të llogariten vetëm nga të dhënat e trajnimit. Nëse standardizimi kryhet mbi gjithë bashkësinë përpara ndarjes, informacioni nga prova hyn në model në mënyrë indirekte.

Një \term{tubacion}{pipeline} formalizon pikërisht këtë disiplinë. Çdo transformim që mëson diçka nga të dhënat -- shkallëzim, imputim, përzgjedhje veçorish, PCA -- duhet të përshtatet brenda secilës palë trajnim/validim. Ky parim, i theksuar fort në praktikat moderne të scikit-learn, është më i rëndësishëm se shumë detaje algoritmike sepse mbron integritetin e eksperimentit numerik.
'''),
('Ndarja trajnim--validim--provë',r'''
Nëse i njëjti grup të dhënash përdoret për të përshtatur modelin dhe për të gjykuar cilësinë e tij, rezultati mat aftësinë për të rikrijuar të dhënat e njohura, jo për të \term{përgjithësuar}{generalize}. Për këtë arsye të dhënat ndahen në bashkësi trajnimi, validimi dhe prove. Trajnimi përcakton parametrat; validimi ndihmon në zgjedhjen e hiperparametrave; prova përdoret vetëm në fund, pasi vendimet metodologjike janë mbyllur.

Kur të dhënat janë të kufizuara, \term{validimi i kryqëzuar}{cross-validation} shfrytëzon më mirë informacionin. Në $K$-fold cross-validation, bashkësia ndahet në $K$ pjesë. Modeli trajnohet $K$ herë, çdo herë duke lënë jashtë një pjesë për vlerësim. Marrim jo vetëm mesataren e një metrike, por edhe shpërndarjen e saj. Në një problem fizik, diferenca midis dy modeleve ka kuptim vetëm nëse është e madhe krahasuar me këtë variabilitet.

Struktura e të dhënave mund të kërkojë ndarje më të kujdesshme. Matjet e marra nga i njëjti sensor, i njëjti pacient, e njëjta ditë ose i njëjti simulim nuk janë domosdoshmërisht të pavarura. Në këto raste duhet validim sipas grupeve ose sipas kohës. Ndarja e rastësishme e mostrave të korreluara mund të japë një vlerësim tepër optimist të performancës, sepse prova përmban shembuj pothuajse identikë me ata të trajnimit.
'''),
('Përgjithësimi, mbipërshtatja dhe kompromisi anshmëri--variancë',r'''
\term{Mbipërshtatja}{overfitting} shfaqet kur modeli përdor fleksibilitetin e tij për të përshkruar jo vetëm strukturën e sinjalit, por edhe luhatjet rastësore të mostrës. E kundërta, \term{nënpërshtatja}{underfitting}, ndodh kur klasa e modeleve është tepër e varfër për të përfaqësuar varësinë relevante. Diferenca shihet duke krahasuar gabimin e trajnimit me gabimin e validimit: model shumë i thjeshtë ka gabim të lartë në të dyja; model i mbipërshtatur mund të ketë gabim pothuajse zero në trajnim dhe shumë më të madh në validim.

Në regresion, një formulim klasik e ndan gabimin e pritshëm në anshmëri, variancë dhe zhurmë të pakthyeshme. Në mënyrë skematike,
\[
\E[(Y-\hat f(X))^2]=\text{Bias}^2+\text{Variance}+\sigma_\epsilon^2.
\]
Modeli i thjeshtë ka zakonisht anshmëri më të lartë por variancë më të ulët; modeli shumë fleksibël ka të kundërtën. Ky nuk është ligj i fortë për çdo algoritëm, por është një mënyrë shumë e dobishme për të kuptuar pse përmirësimi i përshtatjes në trajnim nuk është objektivi përfundimtar.

Në fizikë, modelimi i përgjithësueshëm kërkon gjithashtu kontroll të \emph{domenit të vlefshmërisë}. Një model i trajnuar me temperatura midis $0$ dhe $40^\circ$C nuk duhet të përdoret pa kujdes në $-50^\circ$C. Ekstrapolimi është veçanërisht i rrezikshëm për algoritme fleksibël që nuk përmbajnë ligjet fizike si kufizime të shprehura.
'''),
('Metrikat dhe eksperimentimi numerik',r'''
Metrika duhet të pasqyrojë pyetjen shkencore. Për regresion, gabimi kuadratik mesatar
\[
\mathrm{MSE}=\frac1N\sum_{i=1}^{N}(y_i-\hat y_i)^2
\]
penalizon fort gabimet e mëdha; gabimi absolut mesatar është më robust ndaj pikave të largëta. Për klasifikim, saktësia mund të jetë mashtruese kur një klasë është e rrallë. Në kërkimin e ngjarjeve të rralla fizike, një klasifikues që parashikon gjithmonë ``sfond'' mund të ketë saktësi të lartë dhe megjithatë të jetë shkencërisht i pavlefshëm.

Një eksperiment i mirë numerik kontrollon një ndryshore në një kohë. Kur studiojmë ndikimin e standardizimit, mbajmë të pandryshuar algoritmin dhe ndarjen e të dhënave. Kur studiojmë hiperparametrin $k$, përdorim të njëjtën skemë validimi për çdo vlerë. Kjo e bën rezultatin të interpretueshëm dhe të riprodhueshëm. Farat e gjeneratorëve të numrave të rastësishëm dokumentohen, por nuk duhet të keqpërdoren për të ``zgjedhur'' ndarjen që jep rezultatin më të mirë.

Kursi do të trajtojë bibliotekën \texttt{scikit-learn} si mjet eksperimental, jo si kuti magjike. Një API e qëndrueshme -- \texttt{fit}, \texttt{predict}, \texttt{transform}, \texttt{score} -- lejon që vëmendja të zhvendoset te pyetja metodologjike. Por çdo përdorim i bibliotekës do të lidhet me modelin matematik dhe me një implementim nga parimet e para kur kjo është pedagogjikisht e arsyeshme.
'''),
('Shembull udhëzues dhe pyetje për studim',r'''
Mendojmë një sensor që regjistron një sinjal elektrik dhe synojmë të dallojmë ngjarje fizike nga zhurma. Para çdo algoritmi duhet të përcaktojmë: cilat veçori janë të disponueshme në kohën e vendimit; çfarë do të thotë etiketë e besueshme; a vijnë shumë pulse nga i njëjti regjistrim; cilat gabime janë më të kushtueshme; si do të ndahet prova për të imituar përdorimin real. Vetëm pas këtyre vendimeve ka kuptim të krahasojmë regresionin logjistik, k-NN, pemët ose SVM.

\textbf{Pyetje për studim.} (i) Jepni një shembull fizik ku ndarja e rastësishme e çdo rreshti në trajnim dhe provë do të krijonte rrjedhje informacioni. (ii) Shpjegoni pse standardizimi duhet të jetë brenda validimit të kryqëzuar. (iii) Ndërtoni një shembull ku saktësia është metrikë e papërshtatshme. (iv) Cili është dallimi midis parametrit dhe hiperparametrit? (v) Si ndryshon kuptimi i ``të dhënave të reja'' në një eksperiment laboratorik dhe në një seri kohore?
''')]))

chapters.append(ch('Regresioni linear dhe vlerësimi i parametrave',[
('Problemi fizik i vlerësimit',r'''
Regresioni linear është një nga pikat më të mira për të kuptuar marrëdhënien midis një modeli fizik dhe një modeli statistikor. Në ligjin e Hukut, $F=kx$, parametri $k$ ka kuptim të drejtpërdrejtë fizik. Matjet reale mund të përmbajnë gjithashtu një zhvendosje të zeros, prandaj modeli i të dhënave bëhet $F=\beta_0+\beta_1 x+\epsilon$. Koeficienti $\beta_1$ vlerëson konstanten elastike, ndërsa $\beta_0$ mund të sinjalizojë një offset instrumental.

Në formën shumëdimensionale shkruajmë
\[
\mathbf y=X\boldsymbol\beta+\boldsymbol\epsilon,
\]
ku kolona e parë e $X$ mund të jetë njësh për interceptin dhe kolonat e tjera përmbajnë veçoritë. Ky formulim i përmbledhur është i rëndësishëm sepse lidh regresionin me algjebrën lineare dhe e bën të qartë se ``trajnimi'' është vlerësim parametrash.
'''),
('Katrorët më të vegjël dhe derivimi matricor',r'''
Kriteri i katrorëve më të vegjël minimizon shumën e katrorëve të rezidualeve,
\[
S(\boldsymbol\beta)=\|\mathbf y-X\boldsymbol\beta\|_2^2.
\]
Zgjerimi jep
\[
S=\mathbf y^T\mathbf y-2\boldsymbol\beta^T X^T\mathbf y+\boldsymbol\beta^T X^T X\boldsymbol\beta.
\]
Duke marrë gradientin sipas $\boldsymbol\beta$ dhe duke e barazuar me zero,
\[
\nabla_{\boldsymbol\beta}S=-2X^T\mathbf y+2X^TX\boldsymbol\beta=0,
\]
arrijmë te ekuacionet normale
\[
X^TX\hat{\boldsymbol\beta}=X^T\mathbf y,
\]
dhe, kur $X^TX$ është e invertueshme,
\[
\hat{\boldsymbol\beta}=(X^TX)^{-1}X^T\mathbf y.
\]
Kjo formulë është e rëndësishme teorikisht, por në llogaritje numerike nuk rekomandohet të formohet inversi shprehimisht. Zgjidhësit me QR ose SVD janë më të qëndrueshëm, sidomos kur kolonat e $X$ janë pothuajse linearisht të varura.

Interpretimi gjeometrik është po aq i dobishëm. Vektori $X\hat{\boldsymbol\beta}$ është projeksioni ortogonal i $\mathbf y$ në hapësirën e kolonave të $X$. Reziduali $\mathbf r=\mathbf y-X\hat{\boldsymbol\beta}$ është ortogonal me çdo kolonë: $X^T\mathbf r=0$. Kjo lidh regresionin me konceptin e projeksionit që studentët njohin nga algjebra lineare.
'''),
('Rezidualet, supozimet dhe pasiguria e parametrave',r'''
Një vijë që kalon afër pikave nuk mjafton për një analizë shkencore. Duhet të studiojmë \term{rezidualet}{residuals}. Në modelin klasik supozohet $\E[\epsilon_i]=0$, variancë konstante $\Var(\epsilon_i)=\sigma^2$ dhe, për inferencë të thjeshtë, pavarësi. Normaliteti nuk është i nevojshëm për vetë vlerësuesin e katrorëve më të vegjël, por përdoret shpesh për intervale besimi ekzakte në mostra të vogla.

Vlerësimi i variancës së zhurmës është
\[
\hat\sigma^2=\frac{\|\mathbf r\|^2}{N-p},
\]
ku $p$ është numri i parametrave. Në kushtet klasike,
\[
\operatorname{Cov}(\hat{\boldsymbol\beta})=\sigma^2(X^TX)^{-1}.
\]
Kjo formulë tregon drejtpërdrejt se kolineariteti i veçorive rrit pasigurinë e koeficientëve. Në një eksperiment fizik, një koeficient i madh por me pasiguri edhe më të madhe nuk duhet të interpretohet si efekt i vendosur.

Kur pasiguria e pikave ndryshon, p.sh. matjet në skajet e diapazonit janë më të zhurmshme, përdoret regresion i ponderuar me matricë peshash $W$:
\[
\hat{\boldsymbol\beta}=(X^TWX)^{-1}X^TW\mathbf y.
\]
Peshat duhet të vijnë nga modeli i pasigurisë eksperimentale dhe jo të zgjidhen për të përmirësuar artificialisht përshtatjen.
'''),
('Kondicionimi numerik dhe shkallëzimi',r'''
Edhe një problem statistikisht i thjeshtë mund të jetë numerikisht i vështirë. Nëse dy veçori kanë shkallë shumë të ndryshme ose janë pothuajse të varura linearisht, numri i kondicionimit i $X^TX$ rritet dhe koeficientët bëhen të ndjeshëm ndaj zhurmës së rrumbullakimit dhe ndaj ndryshimeve të vogla në të dhëna. Kjo është arsyeja pse formulimi me SVD është i vlefshëm: ai ekspozon drejtimet me vlera singulare të vogla dhe, rrjedhimisht, me informacion të dobët.

Në modelet lineare pa regularizim, standardizimi nuk ndryshon hapësirën e parashikimeve kur të gjitha transformimet përkthehen saktë te koeficientët; megjithatë, ai lehtëson krahasimin e koeficientëve dhe është pothuajse i domosdoshëm kur kalojmë te Ridge, Lasso ose gradient descent. Një analizë e mirë raporton njësitë fizike të koeficientëve pas transformimit mbrapsht në shkallën origjinale.
'''),
('Shembull: matja e konstantës elastike',r'''
Figura~\ref{fig:hooke} tregon një seri sintetike matjesh të forcës dhe zgjatjes. Përshtatja lineare nuk duhet parë vetëm si një vijë estetike; pjerrësia ka njësi $\mathrm{N/m}$ dhe përfaqëson një vlerësim të $k$. Intercepti teston nëse ekziston një zhvendosje sistematike e zeros. Një grafik i rezidualeve ndaj $x$ mund të zbulojë lakim, heteroskedasticitet ose një ndryshim regjimi ku ligji linear nuk është më i vlefshëm.
\begin{figure}[H]\centering\includegraphics[width=.75\textwidth]{figures/fig_regresioni_hooke.pdf}\caption{Regresion linear për një eksperiment të tipit të ligjit të Hukut.}\label{fig:hooke}\end{figure}
Në notebook do të implementohen si zgjidhja me ekuacionet normale, ashtu edhe \texttt{LinearRegression}. Krahasimi duhet të përfshijë koeficientët, MSE, rezidualet dhe kohën e llogaritjes. Për të ilustruar stabilitetin numerik, një ushtrim shton një veçori pothuajse identike me $x$ dhe studion ndryshimin e koeficientëve.
'''),
('Ushtrime dhe zgjerime',r'''
\textbf{1.} Derivoni ekuacionet normale për modelin me intercept dhe një veçori duke përdorur derivime skalare. \textbf{2.} Tregoni se rezidualet janë ortogonale me kolonat e $X$. \textbf{3.} Për një eksperiment me pasiguri të njohura $\sigma_i$, shpjegoni pse peshat natyrore janë proporcionalisht $1/\sigma_i^2$. \textbf{4.} Krahasoni zgjidhjen nga inversi, \texttt{np.linalg.solve}, QR dhe pseudoinversi në një matricë keq të kondicionuar. \textbf{5.} Diskutoni dallimin midis pasigurisë së koeficientit dhe gabimit të parashikimit për një matje të re.
''')]))

chapters.append(ch('Regresioni polinomial, kompleksiteti dhe regularizimi',[
('Nga lineariteti në parametra te jolineariteti në veçori',r'''
Një model mund të jetë linear në parametra pa qenë vijë e drejtë në ndryshoren fizike. Regresioni polinomial i shkallës $m$ shkruhet
\[
\hat y=\beta_0+\beta_1x+\beta_2x^2+\cdots+\beta_mx^m.
\]
Duke ndërtuar matricën e dizajnit me kolonat $1,x,x^2,\ldots,x^m$, problemi mbetet regresion linear në koeficientë. Ky vëzhgim është i rëndësishëm sepse e ndan \emph{përfaqësimin} e veçorive nga algoritmi i përshtatjes.

Në kalibrimin e një sensori, një term kuadratik mund të përfaqësojë jolinearitet të butë të përgjigjes. Por shtimi mekanik i fuqive gjithnjë e më të larta mund ta bëjë modelin shumë fleksibël. Në këtë kapitull kompleksiteti nuk trajtohet si koncept abstrakt: ai shihet në ndryshimin e gabimit të trajnimit dhe validimit kur rritet shkalla e polinomit.
'''),
('Mbipërshtatja si fenomen i matshëm',r'''
Nëse kemi $N$ pika dhe përdorim një polinom me shumë parametra, modeli mund të kalojë shumë afër çdo pike trajnimi. Kjo nuk do të thotë se kemi zbuluar ligjin fizik. Shumë nga kthesat e vogla mund të jenë përgjigje ndaj zhurmës. Kur matjet përsëriten, kthesat ndryshojnë fort: ky është manifestim i variancës së lartë.

Figura~\ref{fig:poly} krahason tre shkallë. Modeli i shkallës së parë ka anshmëri të dukshme; shkalla e dytë përputhet me mekanizmin gjenerues; shkalla e tetë është mjaft fleksibël për të ndjekur luhatje lokale. Vlerësimi duhet bërë me validim të kryqëzuar, jo duke zgjedhur modelin që duket më bukur në të njëjtat pika.
\begin{figure}[H]\centering\includegraphics[width=.77\textwidth]{figures/fig_regresioni_polinomial.pdf}\caption{Kompleksiteti i modelit në një problem kalibrimi.}\label{fig:poly}\end{figure}
'''),
('Ridge: regularizim me normën $L_2$',r'''
Regresioni Ridge minimizon
\[
\mathcal L(\boldsymbol\beta)=\|\mathbf y-X\boldsymbol\beta\|_2^2+\lambda\|\boldsymbol\beta\|_2^2,
\]
zakonisht pa penalizuar interceptin. Zgjidhja është
\[
\hat{\boldsymbol\beta}_{\rm Ridge}=(X^TX+\lambda I)^{-1}X^T\mathbf y.
\]
Termi $\lambda I$ stabilizon drejtimet ku $X^TX$ ka vlera vetjake të vogla. Kështu Ridge nuk është vetëm mjet statistik për mbipërshtatjen; është edhe regularizim numerik i një problemi inverse.

Hiperparametri $\lambda$ kontrollon kompromisin. Për $\lambda=0$ marrim OLS; për vlera shumë të mëdha koeficientët shtypen drejt zeros dhe modeli nënpërshtatet. Përzgjedhja e $\lambda$ duhet bërë brenda validimit, dhe nëse veçoritë kanë njësi shumë të ndryshme, standardizimi është thelbësor sepse penaliteti vepron mbi madhësinë numerike të koeficientëve.
'''),
('Lasso: sparsiteti dhe kufijtë e interpretimit',r'''
Lasso zëvendëson normën kuadratike me normën $L_1$,
\[
\mathcal L(\boldsymbol\beta)=\|\mathbf y-X\boldsymbol\beta\|_2^2+\lambda\sum_j|\beta_j|.
\]
Gjeometria e penalitetit lejon që koeficientë të bëhen ekzaktësisht zero. Për këtë arsye Lasso përdoret shpesh edhe për përzgjedhje veçorish. Megjithatë, ``koeficient zero'' nuk do të thotë domosdoshmërisht ``madhësi fizikisht e parëndësishme''. Kur veçoritë janë fort të korreluara, Lasso mund të zgjedhë njërën në mënyrë jo stabile.

Në një problem fizik duhet të dallojmë interpretueshmërinë statistikore nga kauzaliteti. Një koeficient mund të jetë i dobishëm për parashikim pa përfaqësuar mekanizëm shkakor. Regularizimi është vendim mbi modelin dhe stabilitetin e tij, jo provë për ligj fizik.
'''),
('Krahasimi me pipeline dhe validim të kryqëzuar',r'''
Një procedurë e pastër për polinome dhe regularizim është: krijim i veçorive polinomiale, standardizim, model Ridge/Lasso, dhe pastaj validim i kryqëzuar i gjithë zinxhirit. Nëse polinomet krijohen ose shkallëzohen duke parë gjithë bashkësinë, validimi nuk simulon më një eksperiment me të dhëna të panjohura.

Në notebook do të ndërtohet manualisht matrica Vandermonde, do të krahasohen OLS dhe Ridge për disa $\lambda$, dhe më pas do të përdoret \texttt{Pipeline}. Një kurbë validimi do të paraqesë gabimin ndaj shkallës së polinomit ose forcës së regularizimit. Ky është një shembull ku vizualizimi është mjet për të arsyetuar mbi kompromisin anshmëri--variancë.
'''),
('Ushtrime',r'''
\textbf{1.} Derivoni zgjidhjen e Ridge. \textbf{2.} Tregoni me dekompozim në vektorë vetjakë si regularizimi zvogëlon kontributin e drejtimeve të dobëta. \textbf{3.} Shpjegoni pse Lasso kërkon algoritëm iterativ ndërsa Ridge ka zgjidhje të mbyllur. \textbf{4.} Në një kalibrim sensori, krahasoni shkallët $1,2,4,8$ me të njëjtat fold-e. \textbf{5.} Jepni një shembull fizik ku ndërveprimi $x_1x_2$ është më i justifikuar se fuqitë e larta të një veçorie të vetme.
''')]))

chapters.append(ch('Klasifikimi dhe regresioni logjistik',[
('Nga parashikimi i një madhësie te vendimi midis klasave',r'''
Në klasifikim ndryshorja objektiv është diskrete. Një shembull tipik në fizikën eksperimentale është dallimi midis sinjalit dhe sfondit. Për çdo ngjarje mund të masim amplitudën, kohën e ngritjes, gjerësinë e impulsit dhe energjinë. Objektivi $y\in\{0,1\}$ shënon klasën. Një model i mirë nuk duhet të prodhojë vetëm një etiketë; shpesh është më e dobishme të prodhojë një rezultat të vazhdueshëm që mund të interpretohet si probabilitet ose si rangim.

Regresioni logjistik modelon log-raportin e gjasave si funksion linear,
\[
\log\frac{p}{1-p}=\mathbf w^T\mathbf x+b,
\]
prandaj
\[
p(y=1\mid\mathbf x)=\sigma(\mathbf w^T\mathbf x+b),\qquad \sigma(z)=\frac{1}{1+e^{-z}}.
\]
Kufiri $p=0.5$ është hiperplan linear, por pragu nuk është detyrimisht 0.5; ai duhet të lidhet me kostot e gabimeve dhe me objektivin shkencor.
'''),
('Maksimumi i gjasës dhe entropia e kryqëzuar',r'''
Për shembuj të pavarur Bernoulli, gjasa është
\[
L(\mathbf w,b)=\prod_i p_i^{y_i}(1-p_i)^{1-y_i}.
\]
Maksimizimi i log-gjasës është ekuivalent me minimizimin e humbjes logaritmike
\[
\mathcal L=-\sum_i\left[y_i\log p_i+(1-y_i)\log(1-p_i)\right].
\]
Kjo \term{entropi e kryqëzuar}{cross-entropy} penalizon fort parashikimet shumë të sigurta dhe të gabuara. Ndryshe nga regresioni linear, nuk ka zgjidhje të thjeshtë të mbyllur për $\mathbf w$; përdoren metoda iterative si gradient descent, Newton ose zgjidhës të tjerë konveksë.

Regularizimi $L_2$ shton zakonisht $\lambda\|\mathbf w\|^2$ dhe ndihmon kur veçoritë janë të shumta ose të korreluara. Në \texttt{scikit-learn}, parametrizimi shpesh përdor $C$, afërsisht invers të forcës së regularizimit: $C$ i madh do të thotë penalitet më i dobët.
'''),
('Metrikat e klasifikimit',r'''
Matrica e konfuzionit ndan rezultatet në pozitivë të vërtetë, negativë të vërtetë, pozitivë të rremë dhe negativë të rremë. Prej saj llogariten
\[
\mathrm{precision}=\frac{TP}{TP+FP},\qquad
\mathrm{recall}=\frac{TP}{TP+FN},
\]
si dhe specifika $TN/(TN+FP)$. Metrika $F_1$ është mesatarja harmonike e precision dhe recall.

Në fizikën e ngjarjeve të rralla, këto madhësi kanë interpretim operacional. Rritja e ndjeshmërisë mund të rrisë kontaminimin nga sfondi. Nuk ka prag universal: zgjedhja duhet lidhur me analizën që do të bëhet pas klasifikimit. Kur rezultati i modelit është i vazhdueshëm, kurba ROC paraqet kompromisin midis ndjeshmërisë dhe normës së pozitivëve të rremë për të gjitha pragjet. AUC mat aftësinë e renditjes, jo cilësinë e kalibrimit të probabiliteteve.
'''),
('Kufiri i vendimit, shkallëzimi dhe interpretimi',r'''
Koeficientët $w_j$ japin drejtimin e ndryshimit të log-odds për një rritje njësi të veçorisë $x_j$, duke mbajtur të tjerat konstante. Ky interpretim është i ndjeshëm ndaj njësive; standardizimi e bën më të lehtë krahasimin numerik të koeficientëve, por interpretimi fizik duhet kthyer në njësitë origjinale.

Në dy dimensione kufiri i vendimit mund të vizatohet drejtpërdrejt. Figura~\ref{fig:logdet} tregon dy veçori të impulsit të një detektori. Vija e modelit është kompromis statistikor; mbivendosja e klasave tregon se asnjë hiperplan nuk mund të ndajë çdo ngjarje pa gabim. Kjo është një situatë më realiste se shembujt artificialisht të ndashëm.
\begin{figure}[H]\centering\includegraphics[width=.67\textwidth]{figures/fig_logistic_detector.pdf}\caption{Regresion logjistik për diskriminim sinjal--sfond.}\label{fig:logdet}\end{figure}
'''),
('ROC, kalibrimi dhe pragjet',r'''
Figura~\ref{fig:roc} tregon një kurbë ROC për të njëjtin problem. Pika optimale nuk përcaktohet vetëm nga gjeometria e kurbës: ajo varet nga prevalenca e klasave dhe nga kostoja shkencore e gabimeve. Në një eksperiment kërkimi, mund të preferohet një prerje që ruan shumicën e sinjalit edhe me më shumë sfond; në një sistem alarmi mund të jetë e kundërta.
\begin{figure}[H]\centering\includegraphics[width=.62\textwidth]{figures/fig_roc_detector.pdf}\caption{Kurba ROC për klasifikimin e pulseve.}\label{fig:roc}\end{figure}
Kalibrimi është pyetje tjetër: ndër ngjarjet të cilave modeli u jep probabilitet rreth 0.8, a janë afërsisht 80\% vërtet pozitive? Një model mund të ketë AUC të mirë por probabilitete të pakalibruara. Kjo dallim është i rëndësishëm kur probabilitetet futen në analiza të mëtejshme ose në vendime me kosto të ndryshme.
'''),
('Ushtrime',r'''
\textbf{1.} Derivoni gradientin e cross-entropy për regresionin logjistik. \textbf{2.} Për një matricë konfuzioni të dhënë, llogaritni accuracy, precision, recall, specificity dhe $F_1$. \textbf{3.} Jepni një problem ku AUC është e përshtatshme dhe një tjetër ku kalibrimi është më i rëndësishëm. \textbf{4.} Shpjegoni pse ndryshimi i pragut nuk ndryshon AUC. \textbf{5.} Ndërtoni një pipeline me standardizim dhe regresion logjistik dhe tregoni se standardizimi jashtë cross-validation krijon rrjedhje të vogël por reale informacioni.
''')]))

chapters.append(ch('Metoda e $k$ fqinjëve më të afërt',[
('Ideja lokale e të nxënit',r'''
Metoda e \term{$k$ fqinjëve më të afërt}{$k$-nearest neighbours, k-NN} nuk ndërton një funksion parametrik global gjatë trajnimit. Ajo ruan shembujt dhe, për një pikë të re, kërkon $k$ pikat më të afërta sipas një metrike. Në klasifikim përdoret vota e shumicës; në regresion mesatarja ose një mesatare e ponderuar. Kjo e bën metodën konceptualisht të thjeshtë, por jo triviale: gjithçka varet nga çfarë do të thotë ``afër''.

Për distancën Euklidiane,
\[
d(\mathbf x,\mathbf z)=\sqrt{\sum_j(x_j-z_j)^2}.
\]
Nëse një veçori matet në mijëra njësi dhe një tjetër në të dhjetat, e para dominon distancën. Prandaj shkallëzimi është pjesë e modelit, jo një detaj kozmetik.
'''),
('Roli i $k$ dhe kompromisi lokal',r'''
Me $k=1$, kufiri i vendimit është shumë i ndjeshëm ndaj çdo pike trajnimi; varianca është e lartë. Me $k$ shumë të madh, modeli mesatarizon rajone të gjera dhe mund të humbasë strukturë lokale; anshmëria rritet. Zgjedhja e $k$ është prandaj një shembull i qartë i kompromisit anshmëri--variancë dhe duhet bërë me validim.

Në klasifikim mund të përdoren pesha $1/d$ që u japin më shumë ndikim fqinjëve shumë të afërt. Por kjo rrit ndjeshmërinë ndaj pikave jashtëzakonisht pranë për shkak të zhurmës. Zgjedhja e metrikës dhe e peshave duhet të lidhet me gjeometrinë e problemit fizik.
'''),
('Mallkimi i dimensionalitetit',r'''
Në dimension të lartë, vëllimi rritet aq shpejt sa që një mostër e fundme bëhet e rrallë. Distanca te fqinji më i afërt dhe te pikat e largëta bëhen relativisht më të ngjashme; nocioni i lokalitetit dobësohet. Kjo është një formë e \term{mallkimit të dimensionalitetit}{curse of dimensionality}.

Për fiziken kjo ka pasoja praktike: shtimi i çdo veçorie të mundshme nuk është domosdoshmërisht përmirësim. Veçoritë pa informacion mund të prishin distancat dhe të ulin performancën e k-NN. Reduktimi dimensional, përzgjedhja e veçorive ose ndërtimi i madhësive me kuptim fizik mund të jetë më i vlefshëm se rritja e kompleksitetit të klasifikuesit.
'''),
('Shembull fizik: regjimet e një sistemi të zbehur',r'''
Në bashkësinë sintetike të laboratorit çdo shembull përfaqëson një realizim të një sistemi oscilues dhe përshkruhet me frekuencën dominante dhe koeficientin e zbehjes. Tre regjime dinamike formojnë rajone të dallueshme, por me mbivendosje. Figura~\ref{fig:knn} e bën të dukshme pse një model lokal është i arsyeshëm.
\begin{figure}[H]\centering\includegraphics[width=.68\textwidth]{figures/fig_knn_regjime.pdf}\caption{Veçori të nxjerra nga regjime dinamike të ndryshme.}\label{fig:knn}\end{figure}
Notebook-u do të implementojë kërkimin manual të fqinjëve me NumPy, votimin dhe një kurbë të performancës ndaj $k$. Pastaj rezultatet krahasohen me \texttt{KNeighborsClassifier}. Një variant i ushtrimit shumëzon një nga veçoritë me 1000 për të demonstruar efektin e mungesës së standardizimit.
'''),
('Kostoja llogaritëse dhe kufijtë praktikë',r'''
Trajnimi i k-NN është pothuajse ruajtje e të dhënave, por parashikimi kërkon krahasim me shumë ose të gjitha pikat e trajnimit. Për $N$ të madh dhe dimension $d$, kjo mund të kushtojë $O(Nd)$ për shembull të ri. Struktura si k-d trees mund të ndihmojnë në dimension të ulët, por humbin efikasitet në dimension të lartë.

Përparësia është transparenca: mund të shohim fqinjët që prodhuan vendimin. Kjo është formë e interpretueshmërisë lokale. Kufizimi është se një fqinj i afërt numerikisht nuk është domosdoshmërisht i ngjashëm fizikisht nëse metrika nuk përfaqëson mirë problemin.
'''),
('Ushtrime',r'''
\textbf{1.} Implementoni k-NN pa \texttt{sklearn} dhe verifikoni barazinë e parashikimeve në një bashkësi të vogël. \textbf{2.} Studioni $k=1,3,5,15,50$ me të njëjtat fold-e. \textbf{3.} Shtoni pesë veçori zhurme dhe matni degradimin. \textbf{4.} Krahasoni distancën Euklidiane dhe Manhattan për një problem të shkallëzuar. \textbf{5.} Shpjegoni pse k-NN nuk ekstrapolon në kuptimin e zakonshëm të regresionit.
''')]))

chapters.append(ch('Pemët e vendimit dhe metodat ansambël',[
('Ndarje rekursive e hapësirës së veçorive',r'''
Një \term{pemë vendimi}{decision tree} ndërton rregulla të formës $x_j<t$ dhe ndan në mënyrë rekursive të dhënat. Rezultati është një ndarje pjesë-pjesë e hapësirës së veçorive. Ndryshe nga regresioni logjistik, kufiri nuk është domosdoshmërisht linear dhe shkallëzimi i veçorive zakonisht nuk është i nevojshëm.

Në çdo nyje kërkohet ndarja që ul më shumë papastërtinë. Për klasifikim binar, \term{papastërtia Gini}{Gini impurity} është
\[
G=1-\sum_k p_k^2,
\]
ndërsa entropia është $H=-\sum_k p_k\log p_k$. Ndarja e mirë prodhon nyje fëmijë më homogjene se nyja prind. Kjo procedurë greedy nuk garanton pemën globalisht optimale, por është efikase dhe interpretuese.
'''),
('Thellësia, krasitja dhe mbipërshtatja',r'''
Një pemë pa kufizime mund të vazhdojë ndarjet derisa gjethet të përmbajnë shumë pak pika. Gabimi i trajnimit bie, por varianca rritet. Hiperparametra si \texttt{max\_depth}, \texttt{min\_samples\_leaf} dhe krasitja me kosto-kompleksitet kontrollojnë këtë fleksibilitet.

Pemët janë një shembull i mirë për të parë se kompleksiteti nuk matet vetëm me numrin e parametrave. Struktura diskrete e ndarjeve dhe numri i gjetheve përcaktojnë sa forma të ndryshme mund të përfaqësojë modeli. Validimi i kryqëzuar duhet të përdoret për të zgjedhur thellësinë, jo grafiku i trajnimit.
'''),
('Bagging dhe pylli i rastësishëm',r'''
\term{Bagging}{bagging} ndërton shumë modele mbi mostra bootstrap dhe mesatarizon parashikimet. Nëse gabimet e pemëve individuale nuk janë plotësisht të korreluara, mesatarizimi ul variancën. \term{Pylli i rastësishëm}{random forest} shton një burim tjetër rastësie: në çdo ndarje konsiderohet vetëm një nënbashkësi e veçorive. Kjo de-korrelon pemët dhe shpesh përmirëson ansamblin.

Random forest është model i fuqishëm bazë për të dhëna tabelare: kap jolinearitete dhe ndërveprime pa kërkuar shkallëzim. Por interpretimi i ``rëndësisë së veçorive'' duhet bërë me kujdes. Importanca e bazuar në impurity mund të favorizojë veçori me shumë vlera të mundshme. Permutation importance jep një alternativë më të lidhur me humbjen e performancës kur një veçori prishet.
'''),
('Boosting si ndërtim sekuencial',r'''
Në boosting, modelet bazë ndërtohen sekuencialisht dhe fokusi zhvendoset te shembujt ose rezidualet që modeli aktual i shpjegon dobët. AdaBoost rrit peshën e shembujve të klasifikuar gabim; gradient boosting e interpreton procesin si zbritje gradienti në hapësirën e funksioneve.

Në këtë kurs boosting trajtohet konceptualisht dhe praktikisht, pa hyrë në të gjithë teorinë e optimizimit funksional. Qëllimi është të kuptohet dallimi midis ansambleve paralelë të tipit bagging dhe ndërtimit sekuencial të boosting, si dhe rreziku i hiperparametrave të shumtë në një kurs të shkurtër.
'''),
('Shembull: klasifikimi i fazave të materialit',r'''
Bashkësia sintetike përdor densitetin, përçueshmërinë dhe fortësinë për të dalluar tre faza. Një pemë e cekët prodhon rregulla të lexueshme; një random forest rrit stabilitetin. Figura~\ref{fig:rfimp} paraqet importancat e një pylli, por ato duhen parë si tregues të modelit, jo si prova kauzale.
\begin{figure}[H]\centering\includegraphics[width=.66\textwidth]{figures/fig_random_forest_importances.pdf}\caption{Rëndësi veçorish nga një random forest në një shembull materialesh.}\label{fig:rfimp}\end{figure}
Në notebook do të llogariten manualisht Gini dhe fitimi i një ndarjeje të vetme, pastaj do të përdoret \texttt{DecisionTreeClassifier}. Për random forest, implementimi i plotë manual nuk është objektiv pedagogjik; në vend të tij do të ndërtohet një bagging minimal me disa pemë dhe do të krahasohet me bibliotekën.
'''),
('Ushtrime',r'''
\textbf{1.} Llogaritni Gini para dhe pas një ndarjeje të propozuar. \textbf{2.} Shpjegoni pse një pemë nuk kërkon standardizim, ndërsa k-NN po. \textbf{3.} Vizualizoni gabimin trajnim/validim ndaj thellësisë. \textbf{4.} Krahasoni impurity importance dhe permutation importance. \textbf{5.} Shpjegoni pse bagging ul kryesisht variancën dhe jo domosdoshmërisht anshmërinë e modelit bazë.
''')]))

chapters.append(ch('Makinat me vektorë mbështetës',[
('Hiperplani dhe margjina',r'''
Për klasat $y_i\in\{-1,+1\}$ një klasifikues linear përdor shenjën e $f(\mathbf x)=\mathbf w^T\mathbf x+b$. Nëse të dhënat janë linearisht të ndashme, ka pafund hiperplane që i ndajnë. SVM zgjedh atë që maksimizon margjinën gjeometrike. Duke normalizuar kufizimet si $y_i(\mathbf w^T\mathbf x_i+b)\ge1$, gjerësia e margjinës është $2/\|\mathbf w\|$ dhe problemi bëhet
\[
\min_{\mathbf w,b}\frac12\|\mathbf w\|^2\quad\text{nën}\quad y_i(\mathbf w^T\mathbf x_i+b)\ge1.
\]
Vetëm pikat në ose brenda margjinës ndikojnë drejtpërdrejt në zgjidhje; këto janë \term{vektorët mbështetës}{support vectors}.
'''),
('Margjina e butë dhe hinge loss',r'''
Të dhënat reale zakonisht mbivendosen. Futim ndryshore slack $\xi_i\ge0$ dhe lejojmë shkelje të kufizimeve:
\[
\min \frac12\|\mathbf w\|^2+C\sum_i\xi_i,
\qquad y_if(\mathbf x_i)\ge1-\xi_i.
\]
Parametri $C$ kontrollon kompromisin midis margjinës së gjerë dhe penalizimit të gabimeve. Formulimi lidhet me \term{hinge loss} $\max(0,1-yf(\mathbf x))$.

$C$ i madh kërkon përshtatje të fortë të trajnimit dhe mund të rrisë variancën; $C$ i vogël lejon më shumë shkelje dhe regularizon. Ashtu si te Ridge, hiperparametri duhet zgjedhur me validim. Shkallëzimi i veçorive është thelbësor, sepse norma e $\mathbf w$ dhe distancat në hapësirën e veçorive varen nga njësitë.
'''),
('Ideja e kernelit',r'''
Kur kufiri linear në hapësirën origjinale nuk mjafton, mund të përdorim një transformim $\phi(\mathbf x)$ dhe një klasifikues linear në hapësirën e re. Formulimi dual i SVM varet nga produktet skalare $\phi(\mathbf x_i)^T\phi(\mathbf x_j)$. Nëse ekziston funksion $K(\mathbf x_i,\mathbf x_j)$ që llogarit këto produkte pa ndërtuar shprehimisht $\phi$, marrim \term{trukun e kernelit}{kernel trick}.

Kerneli radial RBF
\[
K(\mathbf x,\mathbf z)=\exp(-\gamma\|\mathbf x-\mathbf z\|^2)
\]
lejon kufij shumë jolinearë. Parametri $\gamma$ përcakton shkallën lokale të ngjashmërisë. $\gamma$ shumë i madh mund të krijojë kufi tepër të imët; shumë i vogël e bën modelin pothuajse linear.
'''),
('Interpretimi gjeometrik dhe lidhja me k-NN',r'''
SVM me RBF dhe k-NN përdorin në mënyra të ndryshme afërsinë. k-NN kufizon vendimin te disa fqinjë diskretë; kernel SVM ndërton kombinim të ponderuar të ngjashmërive me vektorët mbështetës. Ky krahasim është pedagogjikisht i dobishëm sepse tregon se algoritme të ndryshme mund të shprehin nocionin ``lokal'' në forma shumë të ndryshme.

Në interpretim, vektorët mbështetës identifikojnë shembujt më kritikë për kufirin. Kjo mund të jetë e dobishme në fizikë: inspektimi i tyre mund të zbulojë matje pranë tranzicionit midis regjimeve ose raste të paqarta që meritojnë analizë të veçantë.
'''),
('Shembull: ndarja e regjimeve në hapësirën e fazës',r'''
Figura~\ref{fig:svm} paraqet dy regjime që ndahen afërsisht sipas rrezes në një hapësirë faze. Një hiperplan linear nuk mund ta përfaqësojë mirë kufirin rrethor, ndërsa RBF SVM e bën këtë natyrshëm. Ky shembull duhet përdorur për të kuptuar gjeometrinë, jo për të krijuar idenë se kerneli radial është automatikisht zgjedhja më e mirë.
\begin{figure}[H]\centering\includegraphics[width=.62\textwidth]{figures/fig_svm_phase.pdf}\caption{Kufi jolinear me SVM RBF në një hapësirë faze sintetike.}\label{fig:svm}\end{figure}
Notebook-u do të krahasojë kernel linear dhe RBF, do të eksplorojë rrjetën $(C,\gamma)$ me cross-validation dhe do të vizualizojë numrin e vektorëve mbështetës.
'''),
('Ushtrime',r'''
\textbf{1.} Tregoni pse minimizimi i $\|\mathbf w\|$ maksimizon margjinën pas normalizimit të kufizimeve. \textbf{2.} Shpjegoni rolin e $C$ me fjalë dhe me grafik. \textbf{3.} Studioni efektin e $\gamma$ në RBF. \textbf{4.} Identifikoni vektorët mbështetës dhe interpretojini fizikisht në shembullin e hapësirës së fazës. \textbf{5.} Jepni një situatë ku linear SVM është më i preferueshëm se RBF edhe nëse ky i fundit jep saktësi pak më të madhe.
''')]))

chapters.append(ch('Analiza e komponentëve kryesorë dhe reduktimi dimensional',[
('Kovarianca dhe drejtimet e variacionit',r'''
Kur çdo shembull përshkruhet nga shumë madhësi të korreluara, është e dobishme të kërkojmë drejtimet kolektive përgjatë të cilave të dhënat ndryshojnë më shumë. Pas qendrimit të kolonave, matrica e kovariancës është
\[
C=\frac{1}{N-1}X^TX.
\]
Për një drejtim njësi $\mathbf v$, varianca e projeksioneve $X\mathbf v$ është $\mathbf v^TC\mathbf v$. Maksimizimi nën kufizimin $\|\mathbf v\|=1$ çon në ekuacionin e vlerave vetjake
\[
C\mathbf v=\lambda\mathbf v.
\]
Vektori vetjak me $\lambda$ më të madhe është komponenti i parë kryesor.
'''),
('Derivimi variacional dhe ortogonaliteti',r'''
Me shumëzues Lagrange, maksimizojmë $\mathbf v^TC\mathbf v-\lambda(\mathbf v^T\mathbf v-1)$. Derivimi jep $C\mathbf v=\lambda\mathbf v$. Komponenti i dytë maksimizon variancën nën kushtin shtesë të ortogonalitetit me të parin; për një matricë kovariance simetrike, vektorët vetjakë mund të zgjidhen ortonormalë.

Në praktikë PCA llogaritet shpesh me SVD të matricës së qendruar, e cila është numerikisht stabile dhe shmang formimin e $X^TX$ kur dimensioni është i madh. Vlerat singulare lidhen drejtpërdrejt me vlerat vetjake të kovariancës.
'''),
('Projeksioni, rindërtimi dhe varianca e shpjeguar',r'''
Duke mbajtur $q<d$ komponentë, projektojmë
\[
Z=XV_q,
\]
ku kolonat e $V_q$ janë vektorët vetjakë të zgjedhur. Rindërtimi afërsisht është $\hat X=ZV_q^T$. PCA ka edhe një interpretim si zgjedhja e nënhapësirës lineare me dimension $q$ që minimizon gabimin kuadratik të rindërtimit.

Pjesa e variancës së shpjeguar nga komponenti $j$ është $\lambda_j/\sum_k\lambda_k$. Një grafik kumulativ ndihmon në zgjedhjen e $q$, por nuk ka prag universal. Për kompresim mund të synojmë 95--99\%; për vizualizim zgjedhim dy ose tre komponentë edhe kur humbet më shumë informacion.
'''),
('Shkallëzimi dhe interpretimi fizik i loadings',r'''
Nëse veçoritë kanë njësi dhe varianca shumë të ndryshme, PCA mbi kovariancën mund të dominohet nga veçoria me shkallën më të madhe. Standardizimi përpara PCA është i arsyeshëm kur duam t'u japim veçorive peshë të krahasueshme; por nuk duhet bërë automatikisht nëse madhësia absolute e variancës ka kuptim fizik.

Koeficientët e vektorëve vetjakë quhen shpesh \emph{loadings}. Ata tregojnë si kombinohen veçoritë origjinale në komponent. Shenja e një vektori vetjak është arbitrare, ndaj interpretimi duhet të fokusohet te madhësitë relative dhe strukturat, jo te shenja absolute.
'''),
('Shembull: spektroskopi sintetike',r'''
Në një spektër me 120 gjatësi vale, kolonat fqinje janë fort të korreluara. PCA mund të përmbledhë shumicën e variacionit në pak komponentë që ngjajnë me forma spektrale bazë. Figura~\ref{fig:pca} tregon variancën kumulative të shpjeguar.
\begin{figure}[H]\centering\includegraphics[width=.67\textwidth]{figures/fig_pca_variance.pdf}\caption{Varianca e shpjeguar nga PCA për spektra sintetike.}\label{fig:pca}\end{figure}
Në notebook, PCA do të ndërtohet manualisht: qendrim, kovariancë, \texttt{eigh}, renditje, projeksion. Pastaj krahasohet me \texttt{sklearn.decomposition.PCA}. Do të kontrollohet se komponentët mund të kenë shenjë të kundërt por të përfaqësojnë të njëjtin drejtim.
'''),
('Ushtrime',r'''
\textbf{1.} Derivoni ekuacionin e vlerave vetjake nga maksimizimi i variancës. \textbf{2.} Tregoni lidhjen midis SVD dhe PCA. \textbf{3.} Krahasoni PCA me dhe pa standardizim në një bashkësi ku një veçori ka njësi shumë më të mëdha. \textbf{4.} Rindërtoni spektrat me 1, 2, 3 dhe 10 komponentë dhe matni gabimin. \textbf{5.} Shpjegoni pse PCA nuk është metodë për zbulimin e kauzalitetit.
''')]))

chapters.append(ch('Grupimi i të dhënave dhe zbulimi i strukturës',[
('Problemi i pambikëqyrur',r'''
Në \term{nxënien e pambikëqyrur}{unsupervised learning} nuk ekziston etiketë që të thotë nëse rezultati është ``i saktë''. Struktura që zbulojmë varet nga përkufizimi i ngjashmërisë dhe nga algoritmi. Kjo kërkon kujdes të veçantë në interpretim: një grup numerik nuk është automatikisht një fazë fizike.

k-means kërkon ndarje në $K$ grupe që minimizon
\[
J=\sum_{k=1}^K\sum_{\mathbf x_i\in C_k}\|\mathbf x_i-\boldsymbol\mu_k\|^2,
\]
ku $\boldsymbol\mu_k$ është qendra e grupit. Algoritmi alternon midis caktimit të çdo pike te qendra më e afërt dhe përditësimit të qendrave si mesatare e pikave të caktuara.
'''),
('Konvergjenca, inicializimi dhe minimumet lokale',r'''
Çdo hap i k-means nuk e rrit funksionin objektiv, prandaj procedura konvergon në një zgjidhje lokale pas një numri të fundëm konfigurimesh. Por rezultati varet nga inicializimi. k-means++ zgjedh qendrat fillestare në mënyrë që ato të jenë të shpërndara dhe zakonisht jep zgjidhje më të mira se zgjedhja plotësisht e rastësishme.

Për një analizë serioze përdoren disa nisje dhe studiohet stabiliteti. Nëse ndarja ndryshon fort nga një nisje te tjetra, struktura e pretenduar është e dobët ose kriteri Euklidian nuk është i përshtatshëm.
'''),
('Zgjedhja e numrit të grupeve',r'''
Inercia $J$ bie gjithmonë kur $K$ rritet, ndaj nuk mund të zgjedhim $K$ duke minimizuar thjesht $J$. Metoda e bërrylit kërkon pikën ku përfitimi marginal zvogëlohet, por është subjektive. \term{Silhouette score} krahason kohezionin brenda grupit me distancën ndaj grupit më të afërt dhe varion afërsisht nga $-1$ në 1.

Asnjë kriter nuk zëvendëson interpretimin fizik. Nëse një analizë atmosferike jep tre grupe, duhet të kontrollojmë nëse ato lidhen me regjime të njohura, stinët, pozicionin gjeografik ose ndonjë artefakt të instrumentit.
'''),
('Grupimi hierarkik',r'''
Grupimi hierarkik aglomerativ fillon me çdo pikë si grup më vete dhe bashkon gradualisht grupet sipas një rregulli lidhjeje. Single linkage përdor distancën minimale, complete linkage maksimalen, average linkage mesataren, ndërsa Ward minimizon rritjen e variancës brenda grupeve.

\term{Dendrograma}{dendrogram} paraqet historinë e bashkimeve dhe e bën të dukshme strukturën në disa shkallë. Kjo është përparësi ndaj k-means kur nuk duam të zgjedhim menjëherë një $K$ të vetëm. Megjithatë, kompleksiteti llogaritës rritet shpejt me numrin e pikave.
'''),
('Shembull: regjime atmosferike',r'''
Të dhënat sintetike për temperaturën, lagështinë relative dhe presionin përmbajnë tre regjime të fshehta. Figura~\ref{fig:kmeans} tregon projeksionin temperaturë--lagështi të grupeve të gjetura. Standardizimi është i domosdoshëm sepse presioni ka shkallë numerike shumë më të madhe.
\begin{figure}[H]\centering\includegraphics[width=.67\textwidth]{figures/fig_kmeans_atmosfera.pdf}\caption{Grupim k-means i regjimeve atmosferike sintetike.}\label{fig:kmeans}\end{figure}
Notebook-u do të implementojë k-means nga e para, do të paraqesë trajektoren e qendrave dhe do të krahasojë disa inicializime. Pastaj do të ndërtojë dendrogramë dhe do të diskutojë raste ku grupet janë jo sferike dhe k-means dështon.
'''),
('Ushtrime',r'''
\textbf{1.} Tregoni se qendra që minimizon shumën e distancave kuadratike brenda një grupi është mesatarja. \textbf{2.} Implementoni një iteracion të plotë të k-means. \textbf{3.} Studioni efektin e mosstandardizimit të presionit. \textbf{4.} Krahasoni Ward dhe single linkage. \textbf{5.} Ndërtoni një shembull me dy gjysmëhëna ku k-means është konceptualisht i papërshtatshëm.
''')]))

chapters.append(ch('Krahasimi i modeleve, pasiguria, interpretueshmëria dhe metodologjia',[
('Një eksperiment i drejtë krahasimi',r'''
Krahasimi i algoritmeve ka kuptim vetëm kur procedura është e njëjtë për të gjithë. Duhet të përdoren të njëjtat ndarje, të njëjtat metrika dhe preprocessing i përshtatur brenda çdo fold-i. Nëse SVM standardizohet por k-NN jo, nuk po krahasojmë algoritmet, por dy pipeline me cilësi metodologjike të ndryshme.

Një \term{model bazë}{baseline} i thjeshtë është i domosdoshëm. Për klasifikim mund të jetë parashikimi i klasës më të shpeshtë ose regresioni logjistik. Një metodë komplekse duhet të justifikojë kompleksitetin me përmirësim të qëndrueshëm, jo me një fitore të vogël në një ndarje të vetme.
'''),
('Variabiliteti i performancës dhe bootstrap',r'''
Një numër i vetëm si accuracy=0.91 fsheh pasigurinë. Rezultatet e cross-validation japin një shpërndarje të performancës ndaj ndarjeve. Diferenca 0.910 kundrejt 0.905 mund të jetë e parëndësishme nëse devijimi midis fold-eve është 0.02.

\term{Bootstrap}{bootstrap} rimostron me zëvendësim nga të dhënat dhe lejon vlerësimin empirik të shpërndarjes së koeficientëve, metrikave ose parashikimeve. Ai është mjet fleksibël, por duhet të respektojë strukturën e të dhënave; për seri kohore ose grupe të korreluara, bootstrap i pavarur i rreshtave mund të jetë i gabuar.
'''),
('Pasiguria aleatorike dhe epistemike',r'''
\term{Pasiguria aleatorike}{aleatoric uncertainty} buron nga rastësia e procesit dhe zhurma e matjes. Edhe modeli perfekt nuk mund ta eliminojë. \term{Pasiguria epistemike}{epistemic uncertainty} lidhet me mungesën e njohurive, të dhënave ose modelit adekuat. Kjo e fundit mund të zvogëlohet me matje të reja informative.

Në këtë kurs nuk ndërtojmë një teori të plotë probabilistike të pasigurisë. Synimi është që studentët të mos barazojnë parashikimin me të vërtetën. Në regresion përdorim rezidualet, intervalet e koeficientëve dhe bootstrap; në klasifikim studiojmë variabilitetin e metrikave, kalibrimin dhe stabilitetin ndaj perturbimeve.
'''),
('Interpretueshmëria pa pretendime të tepërta',r'''
Modelet lineare japin koeficientë, pemët japin rregulla, random forest mund të analizojë permutation importance, PCA jep loadings dhe SVM identifikon vektorë mbështetës. Këto janë dritare mbi sjelljen e modelit. Ato nuk provojnë kauzalitet.

Një kontroll i fuqishëm në fizikë është \emph{plausibiliteti}: nëse modeli pretendon se një veçori zhurme është më e rëndësishme se energjia e matur, duhet hetuar. Mund të ketë rrjedhje informacioni, bias të përzgjedhjes ose korrelacion instrumental. Interpretueshmëria është proces diagnostik, jo dekorim pas trajnimit.
'''),
('Shembull i integruar i krahasimit',r'''
Në bashkësinë e kursit për ngjarje detektori krahasohen regresioni logjistik, k-NN, pema, random forest dhe SVM. Vlerësohen accuracy dhe ROC-AUC, por edhe koha e trajnimit, stabiliteti i fold-eve, ndjeshmëria ndaj shkallëzimit dhe ndaj zhurmës. Një veçori zhurme është futur qëllimisht për të studiuar interpretimin e rëndësisë së veçorive.

Qëllimi nuk është të shpallet një ``kampion''. Nëse random forest fiton me 0.5 pikë përqindjeje por regresioni logjistik është shumë më i interpretuar dhe më stabil, zgjedhja mund të varet nga përdorimi. Në një analizë shkencore, transparenca dhe kontrolli sistematik mund të vlejnë më shumë se përmirësimi minimal i një metrike.
'''),
('Protokoll për një projekt të riprodhueshëm',r'''
Një projekt i mirë dokumenton: pyetjen shkencore; origjinën dhe njësitë e të dhënave; kriteret e përjashtimit; ndarjen e të dhënave; baseline; pipeline; hapësirën e hiperparametrave; metrikat; analizën e pasigurisë; kontrollet e robustësisë dhe kufijtë e vlefshmërisë. Rezultati final duhet të mund të riprodhohet nga një mjedis i specifikuar dhe fara të dokumentuara.

\textbf{Ushtrime.} (i) Krahasoni pesë modele me të njëjtat split-e. (ii) Kryeni bootstrap të AUC dhe raportoni intervalin 95\%. (iii) Shtoni zhurmë në çdo veçori dhe matni degradimin. (iv) Krahasoni feature importance me permutation importance. (v) Shkruani një paragraf ku argumentoni zgjedhjen e modelit pa përdorur vetëm fjalinë ``ka saktësinë më të lartë''.
''')]))

chapters.append(ch('Zbritja e gradientit dhe optimizimi numerik',[
('Optimizimi si problem i përgjithshëm',r'''
Shumë metoda të nxënies automatike përcaktojnë parametrat duke minimizuar një funksion humbjeje. Kur nuk kemi zgjidhje të mbyllur ose kur të dhënat janë shumë të mëdha, përdorim optimizim iterativ. \term{Zbritja e gradientit}{gradient descent} përditëson
\[
\boldsymbol\theta_{n+1}=\boldsymbol\theta_n-\eta\nabla \mathcal L(\boldsymbol\theta_n),
\]
ku $\eta$ është \term{shpejtësia e të nxënit}{learning rate}.

Gradienti jep drejtimin e rritjes më të shpejtë lokale; shenja minus lëviz në drejtimin e uljes. Ky është pohim lokal. Në funksione konvekse, kushtet janë të favorshme dhe minimumi global mund të arrihet; në funksione jokonvekse sjellja është më komplekse.
'''),
('Shembull kuadratik dhe konvergjenca',r'''
Për $\mathcal L(\theta)=\theta^2$, përditësimi është $\theta_{n+1}=(1-2\eta)\theta_n$. Konvergjenca kërkon $|1-2\eta|<1$, pra $0<\eta<1$. Ky shembull i thjeshtë tregon se hap shumë i madh mund të shkaktojë oscilacione ose divergjencë, ndërsa hap shumë i vogël jep konvergjencë të ngadaltë.

Figura~\ref{fig:gd} paraqet tre shpejtësi të nxënit. Qëllimi nuk është të memorizohet një vlerë optimale, por të kuptohet marrëdhënia midis lakimit të funksionit dhe madhësisë së hapit.
\begin{figure}[H]\centering\includegraphics[width=.67\textwidth]{figures/fig_gradient_convergence.pdf}\caption{Konvergjenca e zbritjes së gradientit për disa shpejtësi të nxënit.}\label{fig:gd}\end{figure}
'''),
('Gradienti për regresionin linear dhe logjistik',r'''
Për regresionin linear me MSE,
\[
\mathcal L(\boldsymbol\beta)=\frac1N\|X\boldsymbol\beta-\mathbf y\|^2,
\qquad
\nabla\mathcal L=\frac{2}{N}X^T(X\boldsymbol\beta-\mathbf y).
\]
Kjo na lejon të gjejmë numerikisht të njëjtën zgjidhje që më parë e morëm me ekuacionet normale. Ky krahasim është pedagogjikisht i fuqishëm: i njëjti problem ka zgjidhje analitike dhe iterative.

Për regresionin logjistik, gradienti i cross-entropy ka formën $X^T(\mathbf p-\mathbf y)/N$ (plus term regularizimi kur përdoret). Kështu gradient descent është urë midis regresionit klasik dhe klasifikimit probabilistik.
'''),
('Zbritja stokastike e gradientit',r'''
Në \term{zbritjen stokastike të gradientit}{stochastic gradient descent, SGD}, gradienti vlerësohet nga një shembull ose minibashkësi e rastësishme. Kostoja për përditësim bie dhe zhurma e gradientit mund të ndihmojë lëvizjen në hapësirën e parametrave. Por trajektorja bëhet më e çrregullt dhe kërkon menaxhim të shpejtësisë së të nxënit.

Termi \emph{stokastik} këtu ka kuptim të saktë: përditësimi varet nga një mostër rastësore e të dhënave. Në praktikë përdoren minibatches që kombinojnë efikasitetin e operacioneve vektoriale me variabilitetin e SGD. Ky koncept përmendet këtu si metodë e përgjithshme optimizimi, jo si pronë ekskluzive e rrjetave nervore.
'''),
('Kondicionimi, shkallëzimi dhe diagnostika',r'''
Nëse sipërfaqja e humbjes ka lakim shumë të ndryshëm në drejtime të ndryshme, gradient descent zigzagon dhe konvergon ngadalë. Standardizimi i veçorive e bën shpesh gjeometrinë më izotrope. Numri i kondicionimit i Hessianit në problem kuadratik është tregues i këtij vështirësimi.

Diagnoza praktike përfshin grafikun e humbjes ndaj iteracionit, normën e gradientit, ndryshimin e parametrave dhe performancën e validimit. Ndalimi nuk duhet bërë vetëm kur humbja e trajnimit vazhdon të ulet; për modele të fleksibël mund të monitorohet validimi.
'''),
('Ushtrime',r'''
\textbf{1.} Derivoni kushtin e konvergjencës për $\mathcal L=a\theta^2/2$. \textbf{2.} Implementoni gradient descent për regresion linear dhe krahasoni me OLS. \textbf{3.} Tregoni numerikisht efektin e standardizimit në numrin e iteracioneve. \textbf{4.} Implementoni SGD me batch=1 dhe minibatch=16. \textbf{5.} Shpjegoni pse një humbje që luhatet në SGD nuk nënkupton domosdoshmërisht dështim të optimizimit.
''')]))

chapters.append(ch('Perceptroni dhe ura drejt rrjetave nervore',[
('Klasifikuesi linear si neuron artificial',r'''
Perceptroni është pika e fundit e trajtimit formal të këtij kursi dhe një urë e natyrshme drejt rrjetave nervore. Ai llogarit një kombinim linear
\[
z=\mathbf w^T\mathbf x+b
\]
dhe merr vendim sipas shenjës së $z$. Në gjuhën e rrjetave, $\mathbf w$ quhen pesha, $b$ animi (bias) dhe funksioni i pragut është aktivizimi. Matematikisht, megjithatë, kemi ende një klasifikues linear.

Lidhja me regresionin logjistik është e drejtpërdrejtë: të dy përdorin të njëjtin $\mathbf w^T\mathbf x+b$, por regresioni logjistik e kalon në sigmoid dhe optimizon log-gjasën, ndërsa perceptroni përdor rregull përditësimi vetëm kur shembulli klasifikohet gabim.
'''),
('Rregulli i përditësimit',r'''
Me etiketa $y_i\in\{-1,+1\}$, nëse $y_i(\mathbf w^T\mathbf x_i+b)\le0$, bëjmë
\[
\mathbf w\leftarrow\mathbf w+\eta y_i\mathbf x_i,
\qquad b\leftarrow b+\eta y_i.
\]
Ky rregull e shtyn hiperplanin në drejtim që favorizon klasifikimin e saktë të shembullit. Në variantin klasik $\eta$ mund të merret 1; shkalla ndikon në madhësinë e peshave por jo në ekzistencën e ndarjes kur të dhënat janë linearisht të ndashme.

Algoritmi është online: shembujt përpunohen një nga një dhe parametrat ndryshojnë menjëherë. Kjo e bën historikisht të rëndësishëm për sistemet e hershme të të nxënit dhe konceptualisht të dobishëm për të kuptuar algoritmet stokastike.
'''),
('Teorema e konvergjencës',r'''
Supozoni se ekziston vektor njësi $\mathbf w^*$ që ndan shembujt me margjinë $\gamma>0$, pra $y_i\mathbf w^{*T}\mathbf x_i\ge\gamma$, dhe $\|\mathbf x_i\|\le R$. Teorema klasike e perceptronit tregon se numri i gabimeve është i kufizuar nga
\[
M\le\left(\frac{R}{\gamma}\right)^2.
\]
Ideja e provës ka dy hapa. Së pari, çdo përditësim rrit projeksionin $\mathbf w_t^T\mathbf w^*$ të paktën me $\gamma$, prandaj pas $M$ gabimeve ai është të paktën $M\gamma$. Së dyti, norma e $\mathbf w_t$ rritet jo më shpejt se $R\sqrt{M}$. Nga Cauchy--Schwarz, $M\gamma\le\|\mathbf w_M\|\le R\sqrt M$, prej nga del kufiri.

Teorema nuk thotë se perceptroni gjen kufirin me margjinën më të madhe, vetëm se do të gjejë një ndarje pas një numri të fundëm gabimesh kur ndarja ekziston. Kjo dallon qartë perceptronin nga SVM.
'''),
('Kufizimi themelor: XOR dhe jondashmëria lineare',r'''
Perceptroni i vetëm nuk mund të përfaqësojë funksionin XOR. Pikat $(0,0)$ dhe $(1,1)$ i përkasin një klase, ndërsa $(0,1)$ dhe $(1,0)$ tjetrës; nuk ekziston vijë që i ndajë. Rritja e numrit të epokave nuk zgjidh një problem përfaqësimi.

Ky shembull është shumë i rëndësishëm pedagogjikisht: dështimi nuk vjen nga optimizimi, por nga klasa e hipotezave. Një transformim i veçorive mund ta bëjë problemin të ndashëm; për shembull, veçoria $x_1x_2$ shton jolinearitet. Rrjetat me shtresa të fshehta automatizojnë në njëfarë mase ndërtimin e përfaqësimeve jolineare, por ky zhvillim i takon kursit pasues.
'''),
('Nga perceptroni te rrjetat moderne: panoramë përshkruese',r'''
Një \term{perceptron shumë-shtresor}{multilayer perceptron} kompozon transformime affine dhe funksione aktivizimi jolineare. Një shtresë mund të shkruhet
\[
\mathbf h=\phi(W\mathbf x+\mathbf b).
\]
Kompozimi i disa shtresave lejon kufij vendimi shumë më të pasur se një hiperplan. Parametrat përshtaten zakonisht me zbritje gradienti; \term{prapapërhapja}{backpropagation} është një mënyrë efikase për të zbatuar rregullin e zinxhirit dhe për të llogaritur gradientët. Në këtë kurs nuk e derivomë atë formalisht.

Rrjetat konvolucionale (CNN) shfrytëzojnë strukturën lokale dhe ndarjen e peshave në të dhëna hapësinore; rrjetat rekurrente modelojnë varësi sekuenciale; Transformer-at përdorin mekanizma attention dhe janë bërë arkitekturë qendrore për gjuhën dhe shumë probleme të tjera. Këto metoda nuk zëvendësojnë konceptet e këtij kursi. Përkundrazi, train/validation/test, regularizimi, optimizimi, rrjedhja e informacionit dhe interpretimi i metrikave bëhen edhe më të rëndësishme kur modelet rriten.
'''),
('Shembull, krahasim dhe ushtrime përfundimtare',r'''
Notebook-u për perceptronin do të përdorë fillimisht të dhëna fizikisht të interpretueshme dhe linearisht të ndashme. Algoritmi do të implementohet nga e para dhe do të regjistrohet numri i gabimeve në çdo epokë. Pastaj rezultati krahasohet me \texttt{sklearn.linear\_model.Perceptron} dhe me regresionin logjistik. Në fund përdoret XOR për të demonstruar kufirin e përfaqësimit.

\textbf{Ushtrime.} (i) Derivoni hapat kryesorë të teoremës së konvergjencës. (ii) Ndërtoni një bashkësi ku margjina zvogëlohet dhe vëzhgoni rritjen e numrit të gabimeve. (iii) Krahasoni kufirin e perceptronit me SVM në të njëjtat të dhëna. (iv) Shpjegoni pse sigmoid + cross-entropy jep interpretim probabilistik ndërsa perceptroni jo. (v) Shkruani me fjalë se çfarë problemi zgjidh një shtresë e fshehtë në rastin XOR, pa përdorur formalizmin e backpropagation.
''')]))

# Appendices
appendix=r'''
\appendix
\chapter{Përmbledhje e algjebrës lineare}
\section{Vektorë, norma dhe produkte skalare}
Për një vektor $\mathbf x\in\R^d$, norma Euklidiane është $\|\mathbf x\|_2=\sqrt{\mathbf x^T\mathbf x}$. Produkti skalar lidhet me këndin përmes $\mathbf x^T\mathbf z=\|\mathbf x\|\|\mathbf z\|\cos\theta$. Ortogonaliteti, projeksionet dhe bazat ortonormale janë qendrore për regresionin dhe PCA.
\section{Vlera vetjake dhe SVD}
Për matricë simetrike $C$, vlerat vetjake janë reale dhe ekziston bazë ortonormale vektorësh vetjakë. SVD shkruan $X=U\Sigma V^T$ dhe përdoret si mjet numerik stabil për katrorët më të vegjël dhe PCA.
\chapter{Përmbledhje probabiliteti dhe statistike}
\section{Mesatarja, varianca dhe kovarianca}
$\E[X]$ përshkruan qendrën e shpërndarjes, $\Var(X)=\E[(X-\E X)^2]$ shpërndarjen, ndërsa kovarianca mat bashkë-variacionin linear. Korelacioni është kovariancë e normalizuar dhe nuk nënkupton kauzalitet.
\section{Gjasat dhe vlerësimi}
Maksimumi i gjasës zgjedh parametrat që e bëjnë kampionin e vëzhguar më të mundshëm nën model. Regresioni logjistik dhe shumë metoda klasifikimi mund të kuptohen nga ky këndvështrim.
\chapter{Udhëzues i shkurtër për eksperimente të riprodhueshme}
Ruani konfigurimin e mjedisit, versionet e bibliotekave, farat e rastësisë dhe kodin që gjeneron çdo figurë. Mos ruani vetëm një notebook të ekzekutuar: siguroni që ai të mund të ekzekutohet nga fillimi në fund në një mjedis të pastër. Për të dhënat e jashtme dokumentoni origjinën, licencën, njësitë dhe çdo filtrim.
\chapter{Bibliografi e zgjedhur}
\begin{itemize}
\item James, G., Witten, D., Hastie, T., Tibshirani, R., Taylor, J. \emph{An Introduction to Statistical Learning}.
\item Hastie, T., Tibshirani, R., Friedman, J. \emph{The Elements of Statistical Learning}.
\item Bishop, C. M. \emph{Pattern Recognition and Machine Learning}.
\item Murphy, K. P. \emph{Probabilistic Machine Learning: An Introduction}.
\item MIT 6.036, \emph{Introduction to Machine Learning}, materiale publike të MIT Open Learning Library.
\item MIT 6.867, \emph{Machine Learning}, MIT OpenCourseWare.
\item Cornell CS 3780/4780, \emph{Introduction to Machine Learning}, materiale publike të leksioneve.
\item INRIA/scikit-learn MOOC, \emph{Machine Learning in Python with scikit-learn}, materiale CC BY 4.0.
\end{itemize}
'''

tex=preamble+glossary+'\n\\mainmatter\n'+''.join(chapters)+appendix+'\n\\end{document}\n'
(L/'Machine_Learning_Leksione.tex').write_text(tex,encoding='utf-8')
print('wrote',len(tex),'chars')
