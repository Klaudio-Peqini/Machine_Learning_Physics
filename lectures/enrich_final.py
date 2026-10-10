from pathlib import Path
p=Path('/mnt/data/ML_Leksione_Final_Refined/Machine_Learning_Leksione.tex')
s=p.read_text()
s=s.replace('\\usepackage{graphicx}', '\\usepackage{graphicx}\n\\graphicspath{{figures/}}')

intro = {
'Hyrje, të dhënat dhe validimi': r'''
Ky kapitull vendos gjuhën dhe disiplinën metodologjike të gjithë kursit. Në praktikë, gabimet më serioze në një analizë të nxënies automatike nuk lindin domosdoshmërisht nga zgjedhja e një algoritmi të dobët, por nga formulimi i pasaktë i pyetjes, nga përzierja e informacionit të trajnimit me atë të provës, nga trajtimi mekanik i të dhënave ose nga interpretimi i një metrike jashtë kontekstit të saj. Prandaj, përpara se të flasim për regresion, klasifikim apo grupim, duhet të kuptojmë si ndërtohet një eksperiment numerik që mund të mbrojë një përfundim shkencor.

Për një student të Fizikës, kjo mënyrë të menduari është e afërt me laboratorin: matja ka procedurë, instrumenti ka kufizime, të dhënat kanë pacaktueshmëri dhe rezultati duhet të kontrollohet ndaj një hipoteze. Nxënia automatike shton një hallkë të re në këtë zinxhir, por nuk e zëvendëson metodën shkencore. Në kapitujt që pasojnë, çdo algoritëm do të trajtohet si pjesë e këtij procesi dhe jo si një objekt i shkëputur matematikor.''',
'Regresioni linear': r'''
Regresioni linear është një nga shembujt më të pastër ku statistika, algjebra lineare dhe interpretimi fizik takohen në një formulim të vetëm. Edhe kur modeli përfundimtar i një problemi është shumë më kompleks, ideja e përshtatjes së parametrave duke minimizuar një masë gabimi mbetet qendrore. Për këtë arsye, regresioni linear nuk duhet parë si një metodë ``elementare'' që kalohet shpejt, por si një model referencë për të kuptuar vlerësimin e parametrave, rezidualet, kondicionimin numerik dhe pacaktueshmërinë.

Në fizikë, një vijë e përshtatur shpesh ka domethënie të drejtpërdrejtë: pjerrësia mund të jetë një konstante elastike, një shpejtësi, një koeficient transporti ose një parametër kalibrimi. Në fusha të tjera, e njëjta strukturë matematikore mund të përdoret për të lidhur konsumin e energjisë me temperaturën, pagën me përvojën ose një tregues ekonomik me kohën. Metoda është e njëjtë; ajo që ndryshon është interpretimi dhe vlefshmëria e supozimeve.''',
'Regresioni polinomial dhe regularizimi': r'''
Modelet reale rrallë mbeten lineare në të gjithë diapazonin e vëzhgimit. Megjithatë, kalimi nga një model linear në një model më fleksibël sjell menjëherë një pyetje më të thellë: sa kompleksitet është i justifikuar nga të dhënat? Ky kapitull e përdor regresionin polinomial si laborator konceptual për të parë se si një model mund të përshtatet gjithnjë e më mirë me të dhënat e trajnimit dhe, njëkohësisht, të bëhet më pak i besueshëm për të dhëna të reja.

Regularizimi shfaqet këtu jo si një truk numerik, por si një mënyrë për të formalizuar preferencën ndaj zgjidhjeve më të qëndrueshme. Në analizën fizike kjo lidhet natyrshëm me problemet inverse dhe me faktin se të dhënat e zhurmshme nuk justifikojnë gjithmonë liri të pakufizuara në model. Në aplikime të tjera, e njëjta ide mbron kundër modeleve që reagojnë tepër fort ndaj luhatjeve të rastësishme të tregut, sjelljes së konsumatorit ose sinjaleve biologjike.''',
'Klasifikimi dhe regresioni logjistik': r'''
Klasifikimi ndryshon natyrën e pyetjes: nuk kërkojmë më një madhësi të vazhdueshme, por një vendim midis dy ose më shumë mundësive. Kjo e bën të domosdoshëm dallimin midis probabilitetit që prodhon modeli dhe vendimit që merret mbi bazën e tij. Regresioni logjistik është veçanërisht i dobishëm sepse e bën këtë dallim të dukshëm dhe ruan një lidhje të qartë me modelet lineare të kapitujve të mëparshëm.

Në një detektor grimcash, për shembull, mund të kërkojmë të dallojmë sinjalin nga sfondi duke përdorur amplitudën, gjerësinë e impulsit dhe energjinë e depozituar. Në një bankë, i njëjti formalizëm mund të përdoret për të vlerësuar probabilitetin e vonesës së një kredie. Në të dyja rastet modeli jep një probabilitet; pragu me të cilin ky probabilitet shndërrohet në vendim duhet të lidhet me koston dhe rrezikun e gabimeve.''',
'$k$ fqinjët më të afërt': r'''
Metoda e fqinjëve më të afërt ofron një këndvështrim të ndryshëm nga modelet parametrike: në vend që të përmbledhë të dhënat në një numër të vogël koeficientësh, ajo ruan shembujt dhe vendos sipas afërsisë lokale. Pikërisht për këtë arsye, metoda është jashtëzakonisht intuitive, por edhe shumë e ndjeshme ndaj mënyrës se si maten distancat dhe ndaj numrit të dimensioneve.

Në fizikë kjo qasje është e natyrshme kur regjimet e një sistemi kanë nënshkrime të ngjashme në një hapësirë veçorish. Jashtë fizikës, një shembull klasik është njohja e modeleve të shkrimit të dorës: një simbol i ri krahasohet me shembuj të etiketuar dhe merr klasën e shumicës së fqinjëve. Thjeshtësia e algoritmit nuk duhet të fshehë pyetjet e rëndësishme mbi shkallëzimin, densitetin e pikave dhe kuptimin e metrikës së zgjedhur.''',
'Pemët e vendimit dhe ansamblet': r'''
Pemët e vendimit përkthejnë një problem shumëpërmasor në një varg pyetjesh lokale. Kjo i bën ato të lexueshme dhe shpesh tërheqëse në aplikime ku përdoruesi duhet të kuptojë pse u mor një vendim. Megjithatë, një pemë e vetme mund të ndryshojë ndjeshëm edhe kur të dhënat ndryshojnë pak; kjo paqëndrueshmëri është arsyeja pse metodat ansambël, veçanërisht pylli i rastësishëm, kanë një rol kaq të rëndësishëm.

Në fizikën e materialeve një pemë mund të ndajë faza sipas temperaturës, presionit dhe disa observablave mikroskopikë. Në sigurime, një pemë mund të përdorë moshën, historikun e dëmeve dhe karakteristika të policës për të ndarë profile rreziku. Në të dyja rastet është thelbësore të dallojmë interpretueshmërinë e një ndarjeje nga një pretendim shkakësor: fakti që një veçori përdoret lart në pemë nuk provon se ajo shkakton rezultatin.''',
'Makinat me vektorë mbështetës (SVM)': r'''
Makinat me vektorë mbështetës sjellin një ide gjeometrike të fuqishme: në vend që të kërkojnë vetëm një kufi që ndan klasat, ato kërkojnë një kufi me margjinë sa më të madhe. Kjo formulë e vendos përgjithësimin në vetë ndërtimin e klasifikuesit dhe tregon pse disa pika të veçanta, vektorët mbështetës, mund të përcaktojnë zgjidhjen e plotë.

Në analizën e një sistemi dinamik, dy regjime mund të bëhen të ndashme në një hapësirë të formuar nga energjia, frekuenca karakteristike dhe një tregues i jolinearitetit. Në klasifikimin e dokumenteve, veçoritë mund të jenë peshat e fjalëve ose të temave. Edhe pse natyra e të dhënave ndryshon shumë, interpretimi gjeometrik i margjinës mbetet i njëjtë dhe ndihmon për të kuptuar se kur një kufi është i qëndrueshëm ndaj zhurmës.''',
'Analiza e komponentëve kryesorë (PCA)': r'''
PCA është një nga pikat ku formimi fizik i studentit jep një avantazh të drejtpërdrejtë. Ideja e diagonalizimit të një matrice kovariance dhe e përzgjedhjes së drejtimeve kryesore është e afërt me boshtet kryesore të inercisë, modat normale dhe problemet vetjake të mekanikës kuantike. Ndryshimi është se këtu matrica përmbledh variacionin statistikor të të dhënave dhe vektorët vetjakë përcaktojnë kombinime lineare të veçorive.

Në spektroskopi, mijëra pika të një spektri mund të përmbajnë vetëm disa modele kryesore ndryshimi. Në analiza socio-ekonomike, dhjetëra tregues mund të reduktohen në disa drejtime që përmbledhin pjesën më të madhe të variacionit. PCA nuk zbulon domosdoshmërisht ``shkaqe''; ajo zbulon drejtime lineare të variacionit dhe interpretimi i tyre kërkon njohuri të problemit.''',
'Grupimi i të dhënave': r'''
Grupimi është një nga detyrat ku duhet të jemi më të kujdesshëm me gjuhën. Algoritmi mund të gjejë grupe sipas një distance të caktuar, por kjo nuk do të thotë automatikisht se këto grupe përfaqësojnë faza fizike, kategori biologjike ose segmente sociale reale. Kuptimi i grupimit lind vetëm kur struktura numerike përputhet me një argument të pavarur shkencor ose praktik.

Në meteorologji, ditët mund të grupohen sipas temperaturës, lagështisë, presionit dhe erës për të identifikuar regjime atmosferike. Në tregti, klientët mund të grupohen sipas shpeshtësisë së blerjeve, vlerës mesatare dhe kategorive të produkteve. Në të dyja rastet, shkallëzimi i veçorive dhe zgjedhja e numrit të grupeve mund të ndryshojnë përfundimin në mënyrë thelbësore.''',
'Krahasimi i modeleve dhe pasiguria': r'''
Një kurs i mirë i nxënies automatike nuk duhet të përfundojë me pyetjen ``cili algoritëm dha saktësinë më të lartë?''. Pyetja shkencore është më e gjerë: sa i qëndrueshëm është rezultati, si ndryshon nga një ndarje e të dhënave në tjetrën, sa varet nga hiperparametrat, a është i kalibruar dhe a mbetet i besueshëm kur të dhënat ndryshojnë pak? Këtu krahasimi i modeleve bëhet pjesë e metodologjisë së eksperimentit.

Në fizikën eksperimentale, një përmirësim shumë i vogël i saktësisë mund të mos justifikojë një model shumë më të ndërlikuar nëse ai është i paqëndrueshëm ose i vështirë për t'u interpretuar. Në një proces industrial apo financiar, një model pak më pak i saktë mund të jetë i preferueshëm nëse reagimi i tij ndaj të dhënave jashtë shpërndarjes së trajnimit është më i kontrolluar. Kjo është arsyeja pse pasiguria dhe robustësia duhet të lexohen bashkë me metrikat mesatare.''',
'Zbritja e gradientit dhe optimizimi': r'''
Zbritja e gradientit lidh drejtpërdrejt nxënien automatike me metodat numerike. Në vend që të kemi një zgjidhje të mbyllur, ndërtojmë një varg të përafërt zgjidhjesh dhe përdorim informacionin lokal të gradientit për të ulur funksionin objektiv. Sjellja e algoritmit varet jo vetëm nga forma e funksionit, por edhe nga shkallëzimi i koordinatave, kondicionimi dhe zgjedhja e hapit.

Në një problem fizik kjo mund të nënkuptojë përshtatjen iteruese të parametrave të një modeli jo linear ndaj matjeve. Në një problem ekonomik ose të marketingut, e njëjta procedurë mund të minimizojë humbjen e një modeli që parashikon kërkesën ose probabilitetin e një reagimi. Pavarësisht aplikimit, analiza e konvergjencës dhe diagnostika numerike janë pjesë e problemit, jo detaje implementimi.''',
'Perceptroni dhe zhvillimet e mëtejshme': r'''
Perceptroni është pika e fundit e trajtimit formal të këtij kursi dhe një urë natyrore drejt rrjetave nervore. Ai kombinon një shumë të ponderuar, një prag vendimi dhe një rregull të thjeshtë përditësimi. Kjo thjeshtësi e bën të mundur që të kuptojmë qartë çfarë mëson algoritmi, kur konvergon dhe pse dështon për probleme që nuk janë linearisht të ndashme.

Në një problem fizik dy klasa ngjarjesh mund të ndahen nga një kombinim linear i dy observablave. Në filtrimin e mesazheve, një model i ngjashëm mund të përdorë pesha të lidhura me praninë e fjalëve ose shenjave të caktuara. Për studentin, vlera kryesore e perceptronit është se hap rrugën për të kuptuar se rrjetat moderne nuk janë magji: ato ndërtojnë kompozime shumë më të pasura të të njëjtës ide bazë, me funksione aktivizimi të ndryshme dhe trajnim me gradient.'''
}

for ch, txt in intro.items():
    # locate exact chapter command by long title
    import re
    pat=re.compile(r'(\\chapter(?:\[[^\]]*\])?\{'+re.escape(ch)+r'\})')
    s,n=pat.subn(r'\1\n'+txt, s, count=1)
    if n!=1: print('intro miss', ch, n)

# Rich application blocks inserted before final section of each chapter.
blocks = {
'Hyrje, të dhënat dhe validimi': r'''
\paragraph{Dy probleme tipike që e bëjnë metodologjinë konkrete.}
Në fizikë, konsiderojmë një sistem monitorimi ku një sensor regjistron temperaturën, presionin dhe amplitudën e një sinjali, ndërsa objektivi është të paralajmërojë një regjim jo normal. Para se të zgjedhim klasifikuesin, duhet të vendosim çfarë quhet regjim jo normal, në cilin interval kohor llogariten veçoritë dhe nëse matjet e së ardhmes kanë hyrë pa dashje në përpunimin e së kaluarës. Nëse standardizimi llogaritet mbi të gjithë të dhënat përpara ndarjes, bashkësia e provës ndikon tashmë te modeli dhe vlerësimi është optimist.

Një problem analog jashtë fizikës është filtrimi i mesazheve të padëshiruara. Veçoritë mund të jenë frekuenca e fjalëve, gjatësia e mesazhit dhe numri i lidhjeve; etiketa është ``spam'' ose ``jo spam''. Edhe këtu, nëse fjalori ose përzgjedhja e veçorive ndërtohet duke përdorur të gjithë korpusin, përfshi mesazhet e provës, kemi rrjedhje informacioni. Shembujt janë të ndryshëm, por rregulli metodologjik është identik.

\paragraph{Ilustrim me kod.}
Një tubacion ruan rendin e saktë të përpunimit brenda çdo ndarjeje të validimit:
\begin{lstlisting}
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

model = make_pipeline(StandardScaler(),
                      LogisticRegression(max_iter=2000))
scores = cross_val_score(model, X, y, cv=5, scoring="f1")
print(scores.mean(), scores.std())
\end{lstlisting}
Ky fragment është i shkurtër, por përmban një ide metodologjike të madhe: standardizuesi përshtatet vetëm me të dhënat e trajnimit të secilës palosje dhe jo me bashkësinë e plotë.
''',
'Regresioni linear': r'''
\paragraph{Problem tipik në fizikë: përcaktimi i një konstante elastike.}
Për një sustë që punon në regjimin linear, ligji i Hukut jep $F=kx$. Nëse forca dhe zgjatja maten me zhurmë, pjerrësia e drejtës së përshtatur vlerëson $k$. Këtu regresioni nuk është thjesht një mjet parashikimi: koeficienti ka njësi dhe kuptim fizik. Rezidualet tregojnë nëse gabimi është në përputhje me zhurmën ose nëse shfaqet një devijim sistematik, për shembull sepse susta po del nga regjimi elastik.

\paragraph{Problem tipik jashtë fizikës: konsumi i energjisë së një ndërtese.}
Në një interval të kufizuar temperaturash, konsumi ditor për ngrohje mund të afrohet me një marrëdhënie lineare me temperaturën e jashtme. Një pjerrësi më e madhe në madhësi mund të sinjalizojë izolim më të dobët. Megjithatë, nëse modeli përdoret jashtë diapazonit të temperaturave të trajnimit, ekstrapolimi mund të dështojë sepse sistemi i ngrohjes hyn në regjim tjetër ose sepse sjellja e banorëve ndryshon.

\begin{figure}[H]\centering
\includegraphics[width=.72\textwidth]{fig_regresion_linear_pd.png}
\caption{Ideja gjeometrike e regresionit linear. Rivizatim i përshtatur nga figura \emph{Linear regression.svg}, Sewaqu, Wikimedia Commons, domen publik. Burimi i lirë: \url{https://commons.wikimedia.org/wiki/File:Linear_regression.svg}.}
\end{figure}

\paragraph{Ilustrim me kod.}
\begin{lstlisting}
import numpy as np
X1 = np.c_[np.ones(len(x)), x]
beta = np.linalg.solve(X1.T @ X1, X1.T @ F)
F_hat = X1 @ beta
residuals = F - F_hat
print("k =", beta[1], "N/m")
\end{lstlisting}
Përdorimi i \texttt{solve} është numerikisht më i përshtatshëm se llogaritja e drejtpërdrejtë e inversit. Në laborator, kjo zgjidhje krahasohet me \texttt{LinearRegression}, por interpretimi fizik i koeficientit duhet të mbetet i njëjtë.
''',
'Regresioni polinomial dhe regularizimi': r'''
\paragraph{Problem tipik në fizikë: kalibrimi jolinear i një sensori.}
Një sensor mund të ketë përgjigje afërsisht lineare pranë pikës së punës, por jolineare në të gjithë diapazonin. Një polinom i shkallës së dytë ose të tretë mund ta përshkruajë mirë kalibrimin. Nëse shkalla rritet shumë, modeli fillon të ndjekë zhurmën e pikave të kalibrimit dhe prodhon luhatje jo fizike midis tyre. Ridge e zbut këtë sjellje duke penalizuar koeficientët e mëdhenj.

\paragraph{Problem tipik jashtë fizikës: parashikimi i kërkesës.}
Kërkesa për energji, transport ose një produkt mund të ndryshojë jolinearisht me temperaturën, orën e ditës ose çmimin. Polinomet dhe veçoritë e zgjeruara japin fleksibilitet, por pa regularizim mund të krijojnë një model të paqëndrueshëm që reagon fort ndaj të dhënave të reja. Në këtë kontekst, parametri $\lambda$ kontrollon sa shumë i besojmë fleksibilitetit të modelit krahasuar me stabilitetin.

\paragraph{Ilustrim me kod.}
\begin{lstlisting}
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline

model = make_pipeline(PolynomialFeatures(6, include_bias=False),
                      StandardScaler(), Ridge(alpha=1.0))
model.fit(x[:, None], y)
\end{lstlisting}
Ky fragment duhet lexuar si përkthim i formulimit matematikor: gjenerohen veçori polinomiale, shkallëzohen dhe më pas koeficientët përcaktohen me penalizim $L_2$.
''',
'Klasifikimi dhe regresioni logjistik': r'''
\paragraph{Problem tipik në fizikë: sinjal kundrejt sfondit.}
Supozoni se çdo impuls i një detektori përshkruhet nga energjia e depozituar dhe koha e ngritjes. Ngjarjet e sinjalit priren të zënë një zonë të caktuar të kësaj hapësire, por mbivendosen me sfondin. Regresioni logjistik nuk jep vetëm etiketën; ai jep një vlerësim të probabilitetit që ngjarja t'i përkasë klasës së sinjalit. Kjo lejon që pragu të zgjidhet në varësi të faktit nëse eksperimenti penalizon më fort pozitivët e rremë apo humbjen e sinjaleve reale.

\paragraph{Problem tipik jashtë fizikës: rreziku i mospagimit.}
Në një aplikim financiar, veçoritë mund të përfshijnë raportin borxh/të ardhura, historikun e pagesave dhe kohëzgjatjen e punësimit. Modeli prodhon një probabilitet mospagimi. Këtu një prag $0.5$ nuk ka ndonjë status të veçantë; ai duhet të zgjidhet sipas kostos së vendimeve dhe politikave të institucionit. Ky shembull e bën të qartë pse klasifikimi probabilistik dhe vendimi final janë dy hapa të ndryshëm.

\begin{figure}[H]\centering
\includegraphics[width=.68\textwidth]{fig_logistike_cc0.png}
\caption{Funksioni logjistik dhe kalimi nga një madhësi reale $z$ te një vlerë në intervalin $(0,1)$. Rivizatim i përshtatur nga \emph{Logistische Funktion.svg}, Stefan Pohl, Wikimedia Commons, CC0. \url{https://commons.wikimedia.org/wiki/File:Logistische_Funktion.svg}.}
\end{figure}

\paragraph{Ilustrim me kod.}
\begin{lstlisting}
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

p = sigmoid(X @ w + b)
y_hat = (p >= threshold).astype(int)
\end{lstlisting}
Ndryshimi i \texttt{threshold} nuk ritrajnon modelin; ai ndryshon vetëm rregullin e vendimit. Ky dallim është thelbësor kur lexohen kurbat ROC dhe precision--recall.
''',
'$k$ fqinjët më të afërt': r'''
\paragraph{Problem tipik në fizikë: identifikimi i regjimeve dinamike.}
Nga një seri kohore mund të nxirren veçori të tilla si energjia mesatare, frekuenca dominante dhe një masë e çrregullsisë. Nëse simulime të mëparshme kanë etiketa për regjime periodike dhe kaotike, një vrojtim i ri mund të klasifikohet sipas fqinjëve më të afërt. Pyetja kryesore është nëse distanca në këtë hapësirë veçorish ka kuptim fizik; nëse një veçori matet në një shkallë shumë më të madhe, ajo mund të dominojë vendimin.

\paragraph{Problem tipik jashtë fizikës: njohja e karaktereve të shkruara me dorë.}
Çdo imazh mund të paraqitet si një vektor pikselash ose veçorish. Një karakter i ri klasifikohet duke parë karakteret më të ngjashme në bashkësinë e trajnimit. Metoda funksionon mirë kur shembujt e ngjashëm ndodhen afër, por bëhet e kushtueshme kur numri i shembujve është i madh dhe më pak informative kur dimensioni rritet shumë.

\begin{figure}[H]\centering
\includegraphics[width=.64\textwidth]{fig_knn_cc0_adapted.png}
\caption{Interpretim lokal i fqinjëve më të afërt. Rivizatim i përshtatur nga materiale të lira mbi grafët e fqinjit më të afërt, David Eppstein, Wikimedia Commons, CC0. \url{https://commons.wikimedia.org/wiki/File:Nearest_neighbor_graph.svg}.}
\end{figure}

\begin{lstlisting}
d = np.sqrt(((X_train - x_new)**2).sum(axis=1))
idx = np.argsort(d)[:k]
pred = np.bincount(y_train[idx]).argmax()
\end{lstlisting}
Këto tri rreshta përmbajnë të gjithë bërthamën e algoritmit. Çdo zgjerim praktik --- peshimi sipas distancës, kërkimi efikas ose zgjedhja e metrikës --- ndërtohet mbi këtë ide lokale.
''',
'Pemët e vendimit dhe ansamblet': r'''
\paragraph{Problem tipik në fizikë: klasifikimi i fazave të një materiali.}
Një bashkësi simulimesh mund të përshkruhet nga temperatura, magnetizimi, susceptibiliteti dhe energjia. Një pemë vendimi kërkon pragje që ndajnë hapësirën në rajone gjithnjë e më homogjene. Nëse pema bëhet shumë e thellë, mund të mësojë luhatje statistikore të simulimeve individuale; një pyll i rastësishëm e redukton këtë variancë duke mesatarizuar shumë pemë të ndryshme.

\paragraph{Problem tipik jashtë fizikës: vlerësimi i rrezikut të një kërkese sigurimi.}
Një pemë mund të bëjë pyetje të tipit ``a ka pasur dëme të mëparshme?'', ``është vlera e pronës mbi një prag?'' ose ``sa është kohëzgjatja e policës?''. Struktura është e kuptueshme për një ekspert, por kjo nuk duhet ngatërruar me shkakësi. Ansambli përmirëson stabilitetin, ndërsa interpretimi zhvendoset nga një pemë e vetme te rëndësia mesatare e veçorive dhe analiza e parashikimeve.

\begin{figure}[H]\centering
\includegraphics[width=.78\textwidth]{fig_peme_vendimi_pd_adapted.png}
\caption{Struktura bazë e një peme vendimi. Rivizatim i përshtatur nga \emph{Decision tree model.png}, T-kita, Wikimedia Commons, domen publik. \url{https://commons.wikimedia.org/wiki/File:Decision_tree_model.png}.}
\end{figure}

\begin{lstlisting}
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

tree = DecisionTreeClassifier(max_depth=4, random_state=0)
forest = RandomForestClassifier(n_estimators=300,
                                max_features="sqrt",
                                random_state=0)
\end{lstlisting}
Këtu hiperparametri \texttt{max_depth} kontrollon drejtpërdrejt kompleksitetin e pemës, ndërsa pylli e shpërndan vendimin në shumë pemë të trajnuara mbi versione të ndryshme të të dhënave.
''',
'Makinat me vektorë mbështetës (SVM)': r'''
\paragraph{Problem tipik në fizikë: dy regjime në hapësirën e fazës.}
Nëse një sistem dinamik përshkruhet nga dy veçori të nxjerra nga trajektorja, pikat mund të formojnë dy re të ndara. SVM zgjedh jo një ndarje arbitrare, por atë që maksimizon margjinën. Pikat që prekin ose afrohen me kufijtë e margjinës janë vektorët mbështetës dhe janë pikërisht ato që mbajnë informacionin vendimtar për pozicionin e hiperplanit.

\paragraph{Problem tipik jashtë fizikës: klasifikimi i dokumenteve.}
Një dokument mund të paraqitet në një hapësirë me shumë dimensione, ku secila veçori lidhet me një fjalë ose komponent tematik. Edhe pse dimensioni është i madh, një SVM linear mund të jetë shumë efikas sepse kufiri varet nga kombinimi linear i këtyre veçorive. Kernelët bëhen të dobishëm kur ndarja kërkon një gjeometri jolineare, por zgjedhja e tyre duhet validuar dhe jo bërë mekanikisht.

\begin{figure}[H]\centering
\includegraphics[width=.62\textwidth]{fig_svm_pd_adapted.png}
\caption{Hiperplani ndarës dhe margjinat në një SVM. Rivizatim i përshtatur nga \emph{SVM margins.svg}, DJGulp3, Wikimedia Commons, domen publik. \url{https://commons.wikimedia.org/wiki/File:SVM_margins.svg}.}
\end{figure}

\begin{lstlisting}
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

svm = make_pipeline(StandardScaler(),
                    SVC(C=2.0, kernel="rbf", gamma="scale"))
svm.fit(X_train, y_train)
\end{lstlisting}
Shkallëzimi është pjesë e modelit, sepse margjina dhe kerneli varen nga distancat. Për këtë arsye ai vendoset brenda tubacionit dhe jo si hap i kryer një herë mbi të gjithë bashkësinë.
''',
'Analiza e komponentëve kryesorë (PCA)': r'''
\paragraph{Problem tipik në fizikë: kompresimi i spektrave.}
Mendojmë $N$ spektre, secili i matur në qindra gjatësi vale. Vlerat fqinjë janë fort të korreluara dhe shumë nga dimensionet janë të tepërta. PCA ndërton kombinime lineare të pikave spektrale që kapin variacionin kryesor. Komponenti i parë mund të përfaqësojë një ndryshim të përgjithshëm të intensitetit, ndërsa komponentë të tjerë mund të lidhen me zhvendosje ose ndryshim të formës së vijave.

\paragraph{Problem tipik jashtë fizikës: përmbledhja e treguesve socio-ekonomikë.}
Një grup vendesh mund të përshkruhet nga të ardhurat, arsimi, jetëgjatësia, punësimi dhe tregues të tjerë. Shumë prej tyre janë të korreluar. PCA mund të krijojë disa drejtime që përmbledhin pjesën më të madhe të variacionit, duke ndihmuar vizualizimin. Megjithatë, emërtimi i komponentit si ``zhvillim'' ose ``mirëqenie'' është interpretim njerëzor dhe duhet justifikuar nga peshat e veçorive, jo vetëm nga grafiku.

\begin{figure}[H]\centering
\includegraphics[width=.62\textwidth]{fig_pca_free_adapted.png}
\caption{Re pikash dhe drejtimet kryesore të variacionit. Rivizatim i përshtatur nga figura e lirë \emph{GaussianScatterPCA}, Ben FrantzDale, Wikimedia Commons, CC BY-SA 3.0/GFDL. \url{https://commons.wikimedia.org/wiki/File:GaussianScatterPCA.png}.}
\end{figure}

\begin{lstlisting}
Xc = X - X.mean(axis=0)
C = np.cov(Xc, rowvar=False)
vals, vecs = np.linalg.eigh(C)
order = np.argsort(vals)[::-1]
W = vecs[:, order[:2]]
Z = Xc @ W
\end{lstlisting}
Ky është PCA nga parimet e para: qendërzim, kovariancë, diagonalizim, renditje e vlerave vetjake dhe projeksion. Implementimi i bibliotekës duhet të japë të njëjtën nënhapësirë, deri në shenjën arbitrare të vektorëve vetjakë.
''',
'Grupimi i të dhënave': r'''
\paragraph{Problem tipik në fizikë: regjime atmosferike.}
Çdo ditë mund të përshkruhet nga temperatura, presioni, lagështia, era dhe një ose dy tregues të stabilitetit. Në mungesë të etiketave, $k$-means mund të propozojë grupe të ditëve me karakteristika të ngjashme. Këto grupe nuk duhet të quhen menjëherë ``regjime meteorologjike''; ato bëhen fizikisht kuptimplota vetëm pasi kontrollohen ndaj hartave sinoptike, stinëve dhe variablave të pavarura.

\paragraph{Problem tipik jashtë fizikës: segmentimi i klientëve.}
Një biznes mund të përmbledhë sjelljen e klientëve me numrin e blerjeve, shpenzimin mesatar dhe kohën nga blerja e fundit. Grupimi propozon segmente me sjellje të ngjashme. Rezultati varet shumë nga shkalla e variablave dhe nga zgjedhja e $k$; për këtë arsye silhouette score dhe analiza e stabilitetit janë ndihmë, jo zëvendësim për arsyetimin e domenit.

\begin{figure}[H]\centering
\includegraphics[width=.62\textwidth]{fig_kmeans_free_adapted.png}
\caption{Parimi i $k$-means: pikat caktohen te qendra më e afërt dhe qendrat ripërllogariten. Rivizatim i përshtatur nga seria \emph{K Means Example}, Weston.pace, Wikimedia Commons (licencë e lirë GFDL/CC sipas faqes së skedarit). \url{https://commons.wikimedia.org/wiki/File:K_Means_Example_Step_1.svg}.}
\end{figure}

\begin{lstlisting}
for _ in range(max_iter):
    d2 = ((X[:, None, :] - centroids[None, :, :])**2).sum(axis=2)
    labels = d2.argmin(axis=1)
    new = np.vstack([X[labels == j].mean(axis=0) for j in range(k)])
    if np.allclose(new, centroids):
        break
    centroids = new
\end{lstlisting}
Kodi e bën të dukshme natyrën alternative të algoritmit: hapi i caktimit dhe hapi i përditësimit përsëriten derisa qendrat të stabilizohen.
''',
'Krahasimi i modeleve dhe pasiguria': r'''
\paragraph{Problem tipik në fizikë: zgjedhja e klasifikuesit për një detektor.}
Supozoni se pesë modele japin saktësi të ngjashme për ndarjen sinjal--sfond. Një pyll i rastësishëm mund të fitojë me pak përqindje, por një regresion logjistik mund të jetë më i kalibruar dhe më i lehtë për t'u kontrolluar. Një SVM mund të jetë më i qëndrueshëm ndaj një kufiri të caktuar, por më i vështirë për interpretim. Vendimi shkencor kërkon të shohim shpërndarjen e rezultateve në validim, jo vetëm një numër të vetëm.

\paragraph{Problem tipik jashtë fizikës: parashikimi i largimit të klientëve.}
Në një kompani shërbimesh, një model mund të parashikojë cilët klientë kanë gjasa të largohen. Një model me AUC pak më të lartë mund të jetë më pak i dobishëm nëse probabilitetet e tij janë të pakalibruara ose nëse performanca ndryshon shumë nga një segment i popullsisë te tjetri. Këtu pasiguria, kalibrimi dhe interpretimi lidhen drejtpërdrejt me vendimin operacional.

\begin{lstlisting}
from sklearn.model_selection import StratifiedKFold, cross_validate
cv = StratifiedKFold(5, shuffle=True, random_state=7)
result = cross_validate(model, X, y, cv=cv,
                        scoring=["accuracy", "f1", "roc_auc"],
                        return_train_score=True)
\end{lstlisting}
Tabela që del nga ky eksperiment duhet lexuar si një shpërndarje performancash. Mesatarja pa devijimin standard humbet një pjesë të rëndësishme të informacionit mbi stabilitetin e modelit.
''',
'Zbritja e gradientit dhe optimizimi': r'''
\paragraph{Problem tipik në fizikë: përshtatja e një modeli jolinear.}
Nëse amplituda e një oscilatori të zbehur përshkruhet nga $A(t)=A_0e^{-\gamma t}$, parametrat $A_0$ dhe $\gamma$ mund të përcaktohen duke minimizuar shumën e katrorëve të rezidualeve. Kur modeli zgjerohet me parametra të tjerë ose kur zgjidhja analitike nuk është e leverdishme, zbritja e gradientit bëhet një mjet i drejtpërdrejtë për të lëvizur në hapësirën e parametrave.

\paragraph{Problem tipik jashtë fizikës: optimizimi i një modeli të kërkesës.}
Një model logjistik mund të parashikojë probabilitetin që një përdorues t'i përgjigjet një oferte. Koeficientët përcaktohen duke minimizuar entropinë e kryqëzuar. Nëse numri i të dhënave është shumë i madh, zbritja stokastike ose me minibashkësi shmang llogaritjen e gradientit mbi të gjithë bashkësinë në çdo hap. Kjo lidh drejtpërdrejt optimizimin numerik me shkallëzueshmërinë llogaritëse.

\begin{lstlisting}
theta = theta0.copy()
for step in range(n_steps):
    grad = gradient(theta, X, y)
    theta -= eta * grad
    if np.linalg.norm(grad) < tol:
        break
\end{lstlisting}
Ky kod është i thjeshtë, por diagnostika duhet të jetë më e pasur: duhet të ruhet humbja, norma e gradientit dhe, kur është e mundur, trajektorja e parametrave. Vetëm kështu mund të dallojmë konvergjencën nga stagnimi ose paqëndrueshmëria.
''',
'Perceptroni dhe zhvillimet e mëtejshme': r'''
\paragraph{Problem tipik në fizikë: ndarja e dy familjeve të ngjarjeve.}
Marrim dy observabla, për shembull energjinë dhe një tregues të formës së impulsit. Nëse dy klasat ndahen nga një vijë, perceptroni mund të mësojë një kombinim linear të tyre. Kur një pikë klasifikohet gabim, pesha lëviz në drejtimin që e afron kufirin me një ndarje të saktë. Nëse klasat nuk janë linearisht të ndashme, rregulli vazhdon të përditësohet pa gjetur një zgjidhje perfekte; ky dështim është informacion mbi kapacitetin e modelit.

\paragraph{Problem tipik jashtë fizikës: filtrimi i mesazheve.}
Një paraqitje shumë e thjeshtë mund të përdorë veçori binare që tregojnë praninë e fjalëve ose strukturave të caktuara. Perceptroni ndërton një peshë për secilën veçori dhe merr vendim sipas shenjës së shumës së ponderuar. Ky shembull tregon se neuroni artificial është fillimisht një klasifikues linear; kompleksiteti i rrjetave të mëvonshme lind nga kombinimi i shumë njësive dhe jo nga ndryshimi i parimit bazë të peshimit.

\begin{figure}[H]\centering
\includegraphics[width=.78\textwidth]{fig_perceptron_cc0_adapted.png}
\caption{Skema e një perceptroni me hyrje, pesha, shumën e ponderuar dhe funksionin e aktivizimit. Rivizatim i përshtatur nga figura e lirë \emph{Perceptron-unit.svg}, Wikimedia Commons, CC0. \url{https://commons.wikimedia.org/wiki/File:Perceptron-unit.svg}.}
\end{figure}

\begin{lstlisting}
for x_i, y_i in zip(X, y):
    pred = 1 if (x_i @ w + b) >= 0 else -1
    if pred != y_i:
        w += eta * y_i * x_i
        b += eta * y_i
\end{lstlisting}
Rregulli i përditësimit është i lexueshëm pikërisht sepse modeli është i thjeshtë. Kjo transparencë e bën perceptronin një fund të përshtatshëm për kursin Bachelor dhe një pikënisje të mirë për rrjetat nervore në ciklin Master.
'''
}

# insert block before the 6th section of each chapter; identify chapters boundaries and sixth section within
import re
for ch, block in blocks.items():
    # find chapter start then next chapter
    m=re.search(r'\\chapter(?:\[[^\]]*\])?\{'+re.escape(ch)+r'\}', s)
    if not m:
        print('block no chapter', ch); continue
    nextm=re.search(r'\\chapter(?:\[[^\]]*\])?\{', s[m.end():])
    end = m.end()+nextm.start() if nextm else len(s)
    chunk=s[m.start():end]
    secs=list(re.finditer(r'\\section\{', chunk))
    if len(secs)<6:
        print('too few sections', ch, len(secs)); continue
    pos=m.start()+secs[5].start()
    s=s[:pos]+block+'\n'+s[pos:]

# add a short prose-oriented guidance in front matter
needle='Për çdo metodë kërkohet të kuptohet së pari formulimi matematik dhe vetëm pastaj implementimi.'
add=r'''Për çdo metodë kërkohet të kuptohet së pari formulimi matematik dhe vetëm pastaj implementimi. Leximi është menduar të jetë i vazhdueshëm: formulat nuk paraqiten si objekte të izoluara, por shoqërohen me shpjegimin e madhësive, me interpretimin e rezultatit dhe me shembuj ku shihet çfarë fiton ose humbet modeli. Në pjesët ku një ide bëhet më e qartë përmes llogaritjes, fragmente të shkurtra Python vendosen pranë diskutimit teorik; ato nuk zëvendësojnë notebook-ët, por krijojnë urën e menjëhershme midis formulës dhe eksperimentit numerik.

Për çdo metodë kërkohet të kuptohet së pari formulimi matematik dhe vetëm pastaj implementimi.'''
s=s.replace(needle, add, 1)

# Add figure-source note within bibliography chapter rather than a new chapter.
source_note=r'''
\section*{Burime të figurave të lira dhe përshtatjet grafike}
Figurat e jashtme të përdorura në tekst janë rivizatuar dhe përshtatur për terminologjinë e kursit, duke u mbështetur vetëm në burime me licenca të lira. Burimet kryesore janë: \emph{Linear regression.svg} (Sewaqu, domen publik), \emph{Logistische Funktion.svg} (Stefan Pohl, CC0), \emph{Nearest neighbor graph.svg} (David Eppstein, CC0), \emph{Decision tree model.png} (T-kita, domen publik), \emph{SVM margins.svg} (DJGulp3, domen publik), \emph{GaussianScatterPCA} (Ben FrantzDale, CC BY-SA 3.0/GFDL), seria \emph{K Means Example} (Weston.pace, licencë e lirë sipas Wikimedia Commons) dhe \emph{Perceptron-unit.svg} (CC0). Adresat e plota jepen në titujt e figurave për të ruajtur gjurmueshmërinë dhe atribuimin.
'''
# insert before bibliography text following Bibliografi chapter
idx=s.find('\\chapter[Bibliografi]')
if idx!=-1:
    pos=s.find('\n', idx)+1
    s=s[:pos]+source_note+s[pos:]

p.write_text(s)
print('written', p)
