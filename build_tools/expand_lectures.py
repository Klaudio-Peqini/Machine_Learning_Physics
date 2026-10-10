from pathlib import Path
p=Path('/mnt/data/Machine_Learning_Physics/lectures/Machine_Learning_Leksione.tex')
s=p.read_text(encoding='utf-8')
exp={
'Hyrje në nxënien automatike, të dhënat dhe validimi':r'''
\paragraph{Shembull i zgjeruar: nga eksperimenti te tabela.}
Mendojmë një eksperiment ku regjistrohen pulse nga një detektor, secili puls i përshkruar nga një seri kohore $V(t)$. Një tabelë për nxënie automatike nuk krijohet duke hedhur thjesht çdo mostër të serisë në kolonë. Së pari përcaktohen madhësitë që përmbledhin fenomenin: amplituda maksimale, integrali i pulsit, koha e ngritjes, gjerësia në gjysmëlartësi dhe një masë e zhurmës bazë. Këto veçori kanë kuptim fizik dhe mund të kontrollohen për njësi, diapazon dhe stabilitet. Nëse etiketa ``sinjal'' përcaktohet nga një procedurë tjetër matjeje, duhet të dokumentohet saktësia e asaj procedure; etiketa vetë mund të jetë e zhurmshme. Ky vëzhgim është i rëndësishëm: algoritmi nuk mëson ``të vërtetën'', por marrëdhënien midis hyrjeve dhe etiketave të disponueshme.

Në një run eksperimental mund të ketë mijëra pulse, por ato ndajnë të njëjtat kushte të aparaturës: temperaturë, fitim elektronik, tension furnizimi dhe gjendje kalibrimi. Nëse pulse nga i njëjti run shpërndahen rastësisht në trajnim dhe provë, modeli mund të shfrytëzojë karakteristika të veçanta të run-it dhe të duket më i mirë sesa do të ishte në një run të ri. Për këtë arsye njësia e ndarjes mund të jetë run-i dhe jo pulsi. Ky është një shembull tipik ku njohuria e eksperimentit përcakton procedurën statistikore.

\paragraph{Validimi si eksperiment numerik.}
Cross-validation nuk duhet parë si ritual me pesë fold-e. Pyetja është: çfarë lloj ndryshimi do të hasë modeli në përdorim? Nëse do të përdoret në ditë të ardhshme, një validim sipas kohës është më realist. Nëse do të përdoret në aparatura të tjera, ndarja sipas aparaturës është më informative. Kur mostra është e vogël, $K$ i madh jep më shumë të dhëna trajnimi në çdo iteracion por rezultate më të korreluara; $K$ i vogël jep fold-e më të mëdha prove por modele të trajnuara me më pak të dhëna. Zgjedhja duhet të balancojë koston llogaritëse dhe besueshmërinë e vlerësimit.

\paragraph{Një eksperiment me rrjedhjen e informacionit.}
Supozoni se kemi 200 veçori zhurme dhe, para cross-validation, zgjedhim tetë që kanë korelacionin më të madh me etiketën. Edhe pse të gjitha veçoritë janë zhurmë, për shkak të rastësisë disa prej tyre do të duken të korreluara në këtë mostër. Nëse përzgjedhja bëhet duke përdorur të gjithë dataset-in, fold-i i provës ka ndikuar në zgjedhjen e kolonave. Rezultati mund të jetë mbi nivelin e rastësisë. Në procedurën korrekte, përzgjedhja e veçorive vendoset në pipeline dhe përshtatet brenda çdo fold-i. Ky shembull është më i fortë pedagogjikisht se standardizimi, sepse tregon se rrjedhja e informacionit mund të krijojë strukturë aty ku nuk ka.

\paragraph{Pyetje për reflektim metodologjik.}
Në çdo analizë studentët duhet të jenë në gjendje t'u përgjigjen pesë pyetjeve: Cila është njësia statistikore e pavarur? Cili informacion është realisht i disponueshëm në momentin e parashikimit? Si është prodhuar etiketa? Cila ndryshim midis trajnimit dhe përdorimit është më i mundshëm? Çfarë lloj gabimi do të ishte shkencërisht më i dëmshëm? Përgjigjet e këtyre pyetjeve shpesh ndikojnë më shumë në cilësinë e projektit sesa kalimi nga një algoritëm në një tjetër.
''',
'Regresioni linear dhe vlerësimi i parametrave':r'''
\paragraph{Regresioni si problem inverse.}
Në shumë eksperimente fizike regresioni linear është një formë e thjeshtë e problemit inverse: matim një përgjigje dhe duam të nxjerrim parametrat e modelit që e prodhojnë. Nëse matrica $X$ përmban kolona që janë shumë të ngjashme, të dhënat nuk mund të dallojnë mirë kontributet e parametrave përkatës. Kjo është çështje identifikueshmërie, jo vetëm çështje numerike. Numri i madh i kondicionimit i $X^TX$ paralajmëron se ndryshime të vogla në matje mund të prodhojnë ndryshime të mëdha në koeficientë. Për një fizikan, kjo do të thotë se dizajni i eksperimentit mund të jetë i pamjaftueshëm për të ndarë efektet.

Një shembull i thjeshtë është modeli $y=\beta_1x+\beta_2(x+\delta z)$ me $\delta\ll1$. Dy kolonat e dizajnit janë pothuajse të njëjta. Kombinimi $\beta_1+\beta_2$ mund të përcaktohet mirë, ndërsa koeficientët individualë mund të kenë pasiguri të mëdha. Një algoritëm mund të japë numra me shumë shifra, por këto shifra nuk përfaqësojnë informacion real. Raportimi i kovariancës së parametrave dhe i numrit të kondicionimit është prandaj pjesë e interpretimit fizik.

\paragraph{Reziduali si test i modelit.}
Nëse rezidualet tregojnë strukturë sistematike -- për shembull, pozitive në skaje dhe negative në mes -- supozimi i linearitetit është i dyshimtë. Nëse amplituda e rezidualeve rritet me $x$, kemi heteroskedasticitet; nëse rezidualet pasuese janë të korreluara, supozimi i pavarësisë është i dobët. Një vlerë e mirë e $R^2$ nuk e zëvendëson këtë diagnostikë. Në fizikë shpesh është më e vlefshme të shohim një devijim sistematik të vogël nga modeli sesa të përmirësojmë një metrikë globale.

\paragraph{Shembull i punuar: rënia e lirë.}
Për $s(t)=s_0+v_0t+\tfrac12gt^2$, nëse $s_0$ dhe $v_0$ nuk janë zero, regresioni vetëm ndaj $t^2$ do të prodhojë vlerësim të anshëm të $g$. Matrica e dizajnit duhet të përmbajë kolonat $1,t,t^2$. Koeficienti i $t^2$ është $g/2$. Ky shembull tregon rëndësinë e përfshirjes së termave fizikisht të nevojshëm dhe dallimin midis ``modelit linear'' dhe ``funksionit linear të kohës''.

Nëse koha ka pasiguri jo të neglizhueshme, modeli klasik OLS, i cili supozon hyrje pa gabim, nuk është më plotësisht adekuat. Kjo hap derën drejt metodave të regresionit me gabime në të dyja boshtet, por për këtë kurs mjafton të kuptohet kufiri i supozimit. Një manual i mirë duhet të tregojë jo vetëm formulën që përdoret, por edhe kur ajo pushon së qeni e përshtatshme.

\paragraph{Nga vlerësimi te parashikimi.}
Intervali i besimit për mesataren e parashikuar në një $x_0$ dhe intervali i parashikimit për një matje të re nuk janë e njëjta gjë. I pari përfshin pasigurinë e koeficientëve; i dyti përfshin edhe zhurmën e një vrojtimi të ri. Kështu intervali i parashikimit është më i gjerë. Ky dallim është thelbësor kur modeli përdoret për të vlerësuar një parametër fizik kundrejt rastit kur përdoret për të parashikuar matjen e ardhshme.
''',
'Regresioni polinomial, kompleksiteti dhe regularizimi':r'''
\paragraph{Kompleksiteti nuk është sinonim i jolinearitetit.}
Një model kuadratik me tre parametra mund të jetë më i thjeshtë se një model pjesë-pjesë me dhjetëra parametra, edhe pse të dy janë jolinearë në $x$. Në nxënien automatike kompleksiteti lidhet me aftësinë e klasës së modeleve për të përshtatur shumë konfigurime të ndryshme të të dhënave. Polinomi i shkallës së lartë ka shumë liri dhe mund të prodhojë oscilacione midis pikave. Ky fenomen lidhet me bazën monomiale $1,x,x^2,\ldots$, e cila mund të jetë keq e kondicionuar në intervale të gjera.

Në praktikë mund të përdoren baza ortogonale, splines ose transformime të tjera më stabile. Për kursin hyrës, polinomet janë të vlefshme sepse e bëjnë të dukshëm kompromisin midis bias dhe variance. Studentët duhet të shohin se gabimi i trajnimit bie pothuajse monotonisht me shkallën, ndërsa gabimi i validimit ka zakonisht minimum të ndërmjetëm.

\paragraph{Ridge si filtrim spektral.}
Le të shkruajmë $X^TX=V\Lambda V^T$. OLS shumëzon komponentin përgjatë drejtimit $v_j$ me $1/\lambda_j$. Nëse $\lambda_j$ është shumë e vogël, zhurma amplifikohet. Ridge zëvendëson këtë faktor me $1/(\lambda_j+\lambda)$, duke shtypur drejtimet e dobëta. Kjo lidh regularizimin me problemet inverse të fizikës, ku zgjidhjet e paqëndrueshme stabilizohen duke penalizuar norma ose derivime.

Ky interpretim tregon edhe çmimin e regularizimit: futet anshmëri. Koeficientët shtypen drejt zeros edhe kur vlera e vërtetë nuk është zero. Përfitimi është ulja e variancës dhe shpesh ulja e gabimit në të dhëna të reja. Nuk ka kontradiktë: qëllimi i parashikimit nuk është domosdoshmërisht koeficienti i paanshëm në çdo drejtim.

\paragraph{Lasso dhe përzgjedhja e veçorive.}
Penaliteti $L_1$ favorizon zgjidhje sparse. Kjo është tërheqëse kur kemi shumë veçori dhe duam model kompakt. Por në prani të dy veçorive pothuajse ekuivalente, Lasso mund të zgjedhë njërën dhe të heqë tjetrën në mënyrë të ndjeshme ndaj mostrës. Për interpretim fizik duhet kontrolluar stabiliteti i përzgjedhjes me bootstrap ose me fold-e të ndryshme. Një veçori që zgjidhet vetëm në 40\% të rimostrimeve nuk duhet paraqitur si zbulim i fortë.

\paragraph{Shembull i punuar: kalibrim me saturim.}
Nëse sensori ka përgjigje që fillon lineare dhe më pas ngopet, një polinom mund të japë përshtatje të mirë brenda intervalit të kalibrimit por sjellje katastrofike jashtë tij. Ky është dallimi midis interpolimit dhe ekstrapolimit. Për parashikim jashtë intervalit duhet një model i motivuar nga fizika e sensorit ose të paktën kufizime që respektojnë saturimin. Cross-validation i zakonshëm, që lë jashtë pika të shpërndara brenda të njëjtit interval, nuk teston aftësinë e ekstrapolimit.

\paragraph{Zgjedhja e hiperparametrave.}
Nëse zgjedhim njëkohësisht shkallën e polinomit dhe $\lambda$, kemi një hapësirë dy-dimensionale hiperparametrash. Grid search mund të përdoret, por duhet kujdes: sa më shumë konfigurime provojmë, aq më shumë mund të përshtatemi me zhurmën e validimit. Në projekte të vogla është e dobishme të kufizohet hapësira duke përdorur arsyetim fizik dhe të ruhet një test final i paprekur. Nested cross-validation është zgjidhja më rigoroze kur duam vlerësim të paanshëm të gjithë procesit të përzgjedhjes.
''',
'Klasifikimi dhe regresioni logjistik':r'''
\paragraph{Probabiliteti si objekt modelimi.}
Regresioni logjistik nuk modelon drejtpërdrejt klasën; ai modelon probabilitetin kushtor. Ky dallim lejon që i njëjti model të përdoret me pragje të ndryshme sipas qëllimit. Në një eksperiment ku ngjarjet pozitive janë të rralla por shumë të vlefshme, mund të preferohet recall i lartë. Në një sistem ku çdo alarm i rremë kushton shumë kohë instrumenti, precision mund të jetë më kritik. Pragu $0.5$ është thjesht një konventë kur kostot janë simetrike dhe prevalenca e trajnimit është përfaqësuese.

Nëse prevalenca në përdorim ndryshon nga ajo në trajnim, probabilitetet mund të mos jenë më të kalibruara. Kjo është një formë e ndryshimit të shpërndarjes. Një klasifikues mund të ruajë aftësinë e renditjes (AUC) dhe megjithatë të kërkojë rikalibrim të probabiliteteve.

\paragraph{Nga odds te koeficientët.}
Koeficienti $w_j$ interpretohet përmes faktorëve të odds: një rritje me një njësi e $x_j$ shumëzon odds me $\exp(w_j)$, duke mbajtur veçoritë e tjera fikse. Ky interpretim është i dobishëm por duhet kujdes kur veçoritë janë të korreluara. ``Mbajtja fikse'' e një madhësie ndërsa ndryshon një tjetër mund të mos jetë fizikisht e realizueshme. Për shembull, në një puls detektori amplituda dhe integrali mund të jenë të lidhura fort.

\paragraph{Klasat e pabalancuara.}
Kur pozitivët janë 1\% e të dhënave, accuracy është pothuajse e pakuptimtë. ROC mund të duket optimiste sepse norma e pozitivëve të rremë normalizohet me numrin e madh të negativëve. Kur klasa pozitive është e rrallë, kurba precision--recall shpesh është më informative. Baseline për precision është afërsisht prevalenca e klasës pozitive. Një precision prej 0.20 mund të jetë i dobët në një problem të balancuar, por shumë i mirë kur prevalenca është 0.01.

Peshimi i klasave ndryshon funksionin e humbjes dhe mund të ndihmojë modelin të kushtojë më shumë vëmendje klasës së rrallë. Megjithatë, peshat nuk krijojnë informacion të ri. Nëse veçoritë nuk dallojnë klasat, asnjë peshim nuk e zgjidh problemin.

\paragraph{Shembull i punuar: zgjedhja e pragut.}
Supozoni se kemi 10000 ngjarje, 200 sinjal dhe 9800 sfond. Në pragun A marrim recall 0.90 dhe false positive rate 0.05: kjo jep 180 sinjale të ruajtura por rreth 490 ngjarje sfondi. Precision është $180/(180+490)\approx0.27$. Në një prag B me recall 0.65 dhe FPR 0.005, ruajmë 130 sinjale dhe 49 sfond, me precision rreth 0.73. Cili është më i mirë? Përgjigjja varet nga analiza pasuese: nëse kemi metodë të fuqishme për heqjen e sfondit, A mund të jetë i preferueshëm; nëse çdo ngjarje e ruajtur kërkon analizë të kushtueshme, B mund të jetë më praktik.

\paragraph{Kalibrimi dhe besueshmëria.}
Një diagram kalibrimi ndan probabilitetet në intervale dhe krahason probabilitetin mesatar me frekuencën reale. Devijimi sistematik nga diagonalia tregon overconfidence ose underconfidence. Për vendime shkencore ku probabiliteti përdoret si peshë, kalibrimi është më i rëndësishëm se kur përdorim vetëm renditjen e ngjarjeve. Kjo është arsyeja pse performanca e një klasifikuesi nuk mund të përmblidhet me një metrikë të vetme.
''',
'Metoda e $k$ fqinjëve më të afërt':r'''
\paragraph{Gjeometria e distancës.}
Distanca Euklidiane supozon se të gjitha drejtimet në hapësirën e veçorive janë të krahasueshme pas shkallëzimit. Por në fizikë mund të ketë korrelacione të forta. Nëse dy veçori lëvizin së bashku, një metrikë Mahalanobis, që përdor kovariancën, mund të jetë më e përshtatshme. Megjithatë, vlerësimi i kovariancës në dimension të lartë është vetë problem statistik. Për kursin hyrës, standardizimi + Euclidean është baseline i mirë, por studentët duhet të dinë se ``metrika'' është pjesë e modelit.

\paragraph{Pse dimensioni i lartë është i vështirë.}
Në një hiperkub njësi, vëllimi i një topi me rreze të vogël zë pjesë gjithnjë e më të vogël të hapësirës kur dimensioni rritet. Për të mbajtur të njëjtën pjesë të të dhënave brenda një lagjeje, rrezja duhet të rritet. Kështu ``lokaliteti'' bëhet më pak lokal. Një mënyrë empirike për ta parë është të llogaritet raporti $d_{\max}/d_{\min}$ për një pikë reference: në dimension të lartë ky raport afrohet me 1 për shumë shpërndarje.

Ky fenomen shpjegon pse shtimi i veçorive zhurme dëmton k-NN. Çdo dimension shton variacion të parëndësishëm në distancë dhe mund të mbulojë sinjalin e dimensioneve informative. Përzgjedhja e veçorive dhe PCA mund të ndihmojnë, por duhet bërë vetëm nga trajnimi.

\paragraph{k-NN në regresion.}
Për një objektiv të vazhdueshëm, parashikimi mund të jetë mesatarja e $y$ të $k$ fqinjëve. Me $k=1$ marrim një funksion pjesë-pjesë që kalon nëpër vlerat e trajnimit; me $k$ të madh marrim sipërfaqe më të lëmuar. Ky është analog i qartë i bias--variance. Peshat sipas distancës mund të japin lëmim më lokal.

Në një problem të kalibrimit, k-NN regression është i aftë të interpoljë forma jolineare pa specifikuar polinom. Por jashtë diapazonit të të dhënave ai nuk ka mekanizëm të besueshëm ekstrapolimi: parashikimi mbetet afër vlerave të fqinjëve më të afërt në skaj. Kjo duhet ta bëjë studentin të mendojë për domenin e përdorimit.

\paragraph{Shembull i punuar: klasifikimi i regjimeve.}
Supozoni se frekuenca dhe zbehja janë standardizuar. Për një pikë të re $z=(0.4,-0.2)$ në koordinata standarde, pesë fqinjët më të afërt kanë etiketa $[0,0,1,0,1]$. k-NN me $k=5$ jep klasën 0. Nëse dy fqinjët e klasës 1 janë shumë më afër se tre të klasës 0, votimi me peshë distance mund të ndryshojë rezultatin. Kjo tregon se rregulli i agregimit është hiperparametër po aq sa $k$.

\paragraph{Diagnostika praktike.}
Për k-NN duhet të kontrollohen: kurba e validimit ndaj $k$; ndikimi i scaling; ndikimi i veçorive zhurme; stabiliteti i rezultatit ndaj metrikës; dhe kostoja e parashikimit. Nëse modeli do të përdoret online me miliona shembuj trajnimi, një metodë tjetër mund të jetë më praktike edhe kur accuracy është pak më e ulët.
''',
'Pemët e vendimit dhe metodat ansambël':r'''
\paragraph{Si zgjidhet ndarja.}
Për çdo veçori numerike, algoritmi konsideron pragje midis vlerave të renditura. Për çdo prag llogaritet papastërtia e ponderuar e dy fëmijëve. Fitimi është papastërtia e prindit minus kjo mesatare. Kërkimi përsëritet në çdo nyje. Për shkak se procedura është greedy, një ndarje që duket më e mira lokalisht mund të mos jetë pjesë e pemës globalisht optimale; kërkimi i plotë do të ishte shumë i kushtueshëm.

Në një pemë klasifikimi, një gjethe ruan shpërndarjen e klasave të shembujve të trajnimit që arrijnë aty. Probabilitetet e prodhuara kështu mund të jenë të ashpra dhe të pakalibruara, veçanërisht kur gjethet janë të vogla. Kjo është një arsye tjetër për të kontrolluar `min_samples_leaf`.

\paragraph{Pse bagging funksionon.}
Mendojmë parashikime $f_1,\ldots,f_B$ me të njëjtën variancë $\sigma^2$ dhe korelacion mesatar $\rho$. Varianca e mesatares është afërsisht
\[
\rho\sigma^2+\frac{1-\rho}{B}\sigma^2.
\]
Rritja e $B$ ul pjesën e pakorreluar, por jo pjesën e përbashkët. Random forest synon pikërisht të ulë $\rho$ duke detyruar pemët të përdorin nënbashkësi të ndryshme veçorish. Ky argument i thjeshtë shpjegon pse shumë pemë të forta por identike nuk do të sillnin përfitim.

\paragraph{Out-of-bag dhe validimi.}
Në bootstrap, rreth 36.8\% e shembujve nuk përfshihen në një mostër të caktuar. Këto quhen out-of-bag dhe mund të përdoren për një vlerësim të brendshëm të performancës së random forest. Ky vlerësim është i dobishëm, por nuk zëvendëson domosdoshmërisht testin final, sidomos kur bëjmë tuning të hiperparametrave duke parë OOB në mënyrë të përsëritur.

\paragraph{Interpretimi i rëndësisë së veçorive.}
Impurity importance mbledh uljet e impurity të atribuara një veçorie në të gjitha pemët. Veçoritë me shumë vlera ose shumë pika të mundshme ndarjeje mund të favorizohen. Permutation importance mat rënien e një metrike kur vlerat e veçorisë permutohen në një bashkësi validimi. Edhe kjo ka kufizim: për veçori fort të korreluara, permutimi i njërës mund të duket pak i rëndësishëm sepse tjetra mban informacion të ngjashëm.

\paragraph{Shembull i punuar: rregull fizik me ndërveprime.}
Nëse faza e një materiali varet nga kombinimi ``fortësi e lartë DHE përçueshmëri e lartë'', një pemë e përfaqëson natyrshëm me dy ndarje. Regresioni logjistik pa term ndërveprimi mund të ketë vështirësi sepse kufiri është linear. Ky shembull tregon se avantazhi i pemës vjen nga struktura e hipotezës, jo nga një epërsi universale. Nëse e njëjta fazë ndahet nga një hiperplan, regresioni logjistik mund të jetë më i thjeshtë dhe më stabil.

\paragraph{Boosting dhe overfitting.}
Boosting ndërton korrigjime sekuenciale. Shkalla e të nxënit dhe numri i pemëve krijojnë një kompromis: hapa të vegjël me më shumë pemë shpesh japin përgjithësim më të mirë se hapa të mëdhenj. Megjithatë, ky kurs nuk synon tuning të thellë të gradient boosting. Ideja kryesore është të kuptohet se ansamblet mund të ulin bias ose variance duke kombinuar modele, dhe se kostoja është humbja e thjeshtësisë së interpretimit.
''',
'Makinat me vektorë mbështetës':r'''
\paragraph{Nga distanca gjeometrike te optimizimi konveks.}
Për një pikë $x$, distanca me hiperplanin $w^Tx+b=0$ është $|w^Tx+b|/\|w\|$. Duke shkallëzuar $w,b$ në mënyrë që pikat më të afërta të kenë $y_i(w^Tx_i+b)=1$, distanca e tyre është $1/\|w\|$ dhe gjerësia mes dy hiperplaneve mbështetëse është $2/\|w\|$. Kjo derivon objektivin $\tfrac12\|w\|^2$. SVM është prandaj shembull ku një kriter gjeometrik shndërrohet në problem optimizimi konveks.

\paragraph{Formulimi dual dhe support vectors.}
Pa zhvilluar të gjithë teorinë e shumëzuesve të Lagrange, është e vlefshme të shihet forma e vendimit
\[
f(x)=\sum_i\alpha_i y_i K(x_i,x)+b.
\]
Vetëm pikat me $\alpha_i>0$ janë support vectors. Kjo shpjegon pse modeli varet nga një nënbashkësi e të dhënave dhe pse kernel trick është i mundur: të dhënat hyjnë përmes produkteve skalare ose kernelit.

\paragraph{Roli i $C$ dhe $\gamma$.}
Në RBF SVM kemi dy shkallë kompleksiteti. $C$ vendos sa fort penalizohen shkeljet; $\gamma$ vendos sa lokale është ngjashmëria. $C$ i madh dhe $\gamma$ i madh mund të krijojnë kufij shumë të imët rreth pikave individuale. $C$ i vogël dhe $\gamma$ i vogël japin model të lëmuar dhe mund të nënpërshtatin. Harta e cross-validation në planin $(\log C,\log\gamma)$ është mënyrë e mirë për ta parë këtë ndërveprim.

\paragraph{Kerneli si zgjedhje e përfaqësimit.}
Kerneli polinomial korrespondon me ndërveprime polinomiale; RBF korrespondon me një hapësirë shumë të pasur funksionesh lokale. Në vend që ta shohim kernelin si ``magji'', duhet ta interpretojmë si mënyrë për të ndryshuar nocionin e ngjashmërisë. Në fizikë mund të ekzistojnë kernel-e të ndërtuara nga simetri ose invariante, por kjo i kalon objektivat e kursit hyrës.

\paragraph{Shembull i punuar: pika pranë tranzicionit.}
Në të dhënat e hapësirës së fazës, support vectors priren të jenë pranë kufirit midis regjimeve. Inspektimi i tyre mund të zbulojë se disa pika janë afër tranzicionit fizik, ndërsa të tjera mund të jenë outliers. Nëse heqja e pak pikave ndryshon fort kufirin, modeli është i ndjeshëm dhe duhet raportuar kjo. Support vectors janë kështu jo vetëm koncept matematik, por edhe mjet diagnostik.

\paragraph{Kur të mos përdoret SVM.}
Për miliona shembuj, kernel SVM mund të jetë e kushtueshme në memorie dhe kohë. Për interpretim të drejtpërdrejtë, një model linear ose pemë e cekët mund të jetë më e përshtatshme. Për probabilitete, SVM kërkon kalibrim shtesë. Zgjedhja e algoritmit duhet të peshojë dimensionin, madhësinë e mostrës, interpretueshmërinë dhe nevojën për probabilitete.
''',
'Analiza e komponentëve kryesorë dhe reduktimi dimensional':r'''
\paragraph{PCA si problem i projeksionit optimal.}
Për një komponent, kërkojmë një vektor njësi $v$ që maksimizon variancën $\|Xv\|^2/(N-1)$. Me shumëzues Lagrange marrim $Cv=\lambda v$. Për $q$ komponentë, zgjidhja optimale është nënhapësira e gjeneruar nga $q$ vektorët vetjakë me vlerat më të mëdha. E njëjta nënhapësirë minimizon shumën e katrorëve të distancave të pikave nga rindërtimi. Kjo dualitet midis ``maksimizimit të variancës'' dhe ``minimizimit të gabimit të rindërtimit'' është një nga arsyet pse PCA është kaq qendrore.

\paragraph{PCA dhe SVD.}
Nëse $X_c=U\Sigma V^T$, kolonat e $V$ janë drejtimet kryesore, ndërsa $\lambda_j=\sigma_j^2/(N-1)$. Koordinatat kryesore janë $U\Sigma=X_cV$. Ky formulim është praktik sepse bibliotekat numerike kanë implementime shumë të qëndrueshme të SVD dhe mund të trajtojnë edhe raste kur numri i veçorive është më i madh se numri i shembujve.

\paragraph{Qendrimi kundrejt standardizimit.}
Qendrimi është pjesë thelbësore e PCA standarde: pa të, komponenti i parë mund të ndjekë thjesht vektorin e mesatares. Standardizimi është vendim shtesë. Në spektra ku të gjitha kolonat kanë të njëjtën njësi dhe amplituda e variacionit është fizikisht informative, standardizimi i çdo gjatësi vale në variancë njësi mund të shtrembërojë pyetjen. Në të dhëna ku kolonat janë temperaturë, presion dhe shpejtësi ere me njësi të ndryshme, standardizimi mund të jetë i domosdoshëm.

\paragraph{Loadings dhe komponentët si modele fizike.}
Në spektroskopi, loading i parë mund të përfaqësojë ndryshim të përgjithshëm të intensitetit, i dyti një zhvendosje të pikut dhe i treti një ndryshim të gjerësisë. Por PCA nuk garanton që komponentët korrespondojnë me mekanizma të pavarur fizikë; ata janë drejtime ortogonale statistikore. Nëse mekanizmat fizikë nuk janë ortogonalë në hapësirën e matjeve, PCA mund t'i përziejë.

\paragraph{Shembull i punuar: kompresimi.}
Nëse 120 kanale spektrale kompresohen në 3 komponentë dhe këta shpjegojnë 98\% të variancës, raporti bruto i dimensionit është 40:1 për çdo spektër, por duhet të ruajmë edhe mesataren dhe tre vektorët loading. Për një numër të madh spektrash kjo kosto është e vogël. Gabimi i rindërtimit duhet të krahasohet me zhurmën instrumentale: nëse është më i vogël se zhurma, kompresimi ka humbur pak informacion të matshëm.

\paragraph{PCA para klasifikimit.}
PCA është e pambikëqyrur dhe nuk përdor etiketat. Drejtimi me variancë të madhe nuk është domosdoshmërisht drejtimi që ndan klasat. Prandaj PCA mund të heqë informacion diskriminues me variancë të vogël. Kur përdoret para klasifikimit, numri i komponentëve duhet të jetë hiperparametër i pipeline-it dhe të zgjidhet brenda cross-validation. Ky shembull përforcon parimin e rrjedhjes së informacionit dhe tregon pse preprocessing nuk mund të ndahet nga modeli.
''',
'Grupimi i të dhënave dhe zbulimi i strukturës':r'''
\paragraph{Çfarë do të thotë një cluster?}
Një cluster nuk është objekt i pavarur nga algoritmi. k-means kërkon grupe kompakte rreth centroidëve sipas distancës Euklidiane. Hierarchical clustering mund të prodhojë struktura të tjera sipas linkage. DBSCAN, që përmendet vetëm si perspektivë, kërkon rajone me densitet. Në të njëjtat të dhëna këto metoda mund të japin ndarje të ndryshme, secila e vlefshme sipas kriterit të vet.

Në fizikë duhet të shmanget rrëshqitja nga ``algoritmi gjeti tre grupe'' te ``ekzistojnë tre faza fizike''. Për të bërë pretendimin e dytë duhen kontrolle të jashtme: varësi nga temperatura, përputhje me teori, reproducibility në eksperimente të pavarura ose ndryshime të madhësive të tjera fizike.

\paragraph{Derivimi i centroidit.}
Për një grup fiks $C$, minimizojmë $\sum_{i\in C}\|x_i-\mu\|^2$. Derivimi sipas $\mu$ jep $-2\sum_i(x_i-\mu)=0$, prandaj $\mu$ është mesatarja. Ky rezultat shpjegon hapin e përditësimit të k-means dhe tregon pse algoritmi është i lidhur me humbjen kuadratike. Nëse përdorim distancën $L_1$, qendra optimale nuk është mesatarja por mediana komponent për komponent; kështu zgjedhja e metrikes ndryshon edhe përfaqësuesin natyror të cluster-it.

\paragraph{Stabiliteti si kriter.}
Përveç silhouette, mund të studiojmë sa të qëndrueshme janë grupet ndaj rimostrimit, zhurmës ose ndryshimit të inicializimit. Nëse të njëjtat pika kalojnë shpesh nga një cluster në tjetrin, kufiri midis grupeve është i pasigurt. Për analiza shkencore është e dobishme të raportohen këto zona të paqarta, jo vetëm një etiketë e fortë për çdo pikë.

\paragraph{Hierarkia dhe shkallët.}
Dendrograma nuk ka vetëm një prerje ``të saktë''. Në një lartësi mund të shohim dy makro-regjime, në një tjetër katër nënregjime. Kjo është veçanërisht e përshtatshme për sisteme ku struktura fizike është hierarkike, si klasifikime astronomike ose regjime meteorologjike. Linkage i ndryshëm mund të ndryshojë pemën dhe duhet interpretuar në lidhje me gjeometrinë e të dhënave.

\paragraph{Shembull i punuar: një veçori dominante.}
Në dataset-in atmosferik presioni është rreth 1000 hPa, temperatura rreth dhjetëra gradë dhe lagështia 0--100. Pa standardizim, ndryshimet e presionit mund të dominojnë distancën edhe nëse relativisht janë të vogla. Pas standardizimit, secila veçori kontribuon në njësi të devijimit standard. Por ky transformim supozon se një devijim standard temperature dhe një devijim standard presioni kanë peshë të krahasueshme për pyetjen tonë. Ky është supozim metodologjik, jo e vërtetë universale.

\paragraph{Kufijtë e k-means.}
Grupet jo-konvekse, madhësi shumë të ndryshme ose densitete të ndryshme mund të dështojnë. Shembulli i dy gjysmëhënave e bën këtë të dukshme: centroidët e ndajnë hapësirën në rajone Voronoi dhe nuk mund të ndjekin formën e lakuar. Studentët duhet të mësojnë të njohin dështimin e modelit, jo të kërkojnë vetëm një konfigurim që jep një figurë të bukur.
''',
'Krahasimi i modeleve, pasiguria, interpretueshmëria dhe metodologjia':r'''
\paragraph{Krahasimi si problem inferencial.}
Kur dy modele kanë mesatare cross-validation të afërta, nuk mjafton të renditen sipas shifrës së tretë dhjetore. Fold-et përdorin të njëjtat të dhëna dhe rezultatet janë të çiftuara. Diferencat fold-pas-fold-i japin informacion më të mirë se dy devijime standarde të raportuara veçmas. Për një kurs hyrës mjafton të vizatohen diferencat dhe intervalet bootstrap; testet statistikore formale për krahasimin e klasifikuesve mund të studiohen më vonë.

\paragraph{Nested cross-validation.}
Në cross-validation të zakonshëm, nëse përdorim të njëjtat fold-e për të zgjedhur hiperparametrin dhe për të raportuar performancën, vlerësimi mund të jetë optimist. Nested CV përdor një cikël të brendshëm për tuning dhe një cikël të jashtëm për vlerësim. Kjo është metodë e fuqishme kur dataset-i është i vogël dhe nuk duam të rezervojmë test të madh. Kostoja është llogaritëse dhe konceptuale, prandaj në kurs përdoret kryesisht si material i zgjeruar.

\paragraph{Domain shift dhe robustësia.}
Cross-validation supozon se trajnimi dhe përdorimi vijnë nga i njëjti shpërndarje. Në praktikë sensori plaket, klima ndryshon, aparatura kalibrohet ndryshe ose kampioni i ardhshëm ka përbërje të re. Një test robustësie mund të perturbjë veçoritë brenda pasigurive matëse, të ndryshojë prevalencën e klasave ose të vlerësojë modelin në një grup të mbajtur sipas kohës. Këto eksperimente janë shpesh më informative se një grid search shumë i gjerë.

\paragraph{Pasiguria e parashikimit.}
Për modelet lineare mund të llogariten intervale analitike në kushte të caktuara. Për modele të përgjithshme, bootstrap mund të përdoret për të trajnuar shumë kopje të modelit në rimostrime dhe për të parë shpërndarjen e parashikimit. Ky nuk është zëvendësim për një model probabilistik të plotë, por i mëson studentit se parashikimi ka variabilitet.

\paragraph{Interpretueshmëria dhe kontrollet negative.}
Një veçori zhurme e futur qëllimisht është kontroll negativ. Një model që i jep asaj rëndësi të lartë mund të jetë duke mbipërshtatur ose importance mund të jetë e paqëndrueshme. Në projekte reale mund të përdoren veçori që dihet se nuk duhet të kenë lidhje fizike për të testuar pipeline-in. Kjo qasje është e afërt me kontrollet negative në eksperiment dhe i jep ML një kulturë më shkencore.

\paragraph{Struktura e raportit final.}
Një raport i mirë nuk fillon me ``përdorëm Random Forest''. Ai fillon me pyetjen, dataset-in dhe kriterin e suksesit. Pastaj jep baseline, procedurën e validimit, modelet kandidate, tuning, performancën me pasiguri, interpretimin dhe kufijtë. Figura duhet të përgjigjet një pyetjeje: learning curve për sasinë e të dhënave; validation curve për hiperparametrin; residual plot për modelin e gabimit; calibration curve për probabilitetet. Kjo strukturë do të përdoret edhe në projektet e kursit.
''',
'Zbritja e gradientit dhe optimizimi numerik':r'''
\paragraph{Gradienti dhe lakimi.}
Gradienti përmban vetëm informacion të rendit të parë. Në një funksion kuadratik $L=\tfrac12\theta^TH\theta$, drejtimet vetjake të Hessianit $H$ kanë lakime të ndryshme. Stabiliteti i gradient descent kërkon që learning rate të lidhet me vlerën vetjake më të madhe; shpejtësia e konvergjencës varet edhe nga raporti $\lambda_{\max}/\lambda_{\min}$, pra numri i kondicionimit. Kjo lidh optimizimin me algjebrën lineare të kapitujve të mëparshëm.

Standardizimi ndryshon gjeometrinë e problemit. Në regresion me një veçori në intervalin $10^{-3}$ dhe një tjetër në $10^4$, konturet e humbjes janë shumë të zgjatura. Një learning rate që është i sigurt në drejtimin e pjerrët është tepër i vogël në drejtimin e sheshtë. Pas standardizimit, konturet bëhen më afër rrethore dhe konvergjenca përshpejtohet.

\paragraph{Stopping criteria.}
Mund të ndalojmë kur ndryshimi relativ i humbjes është i vogël, kur norma e gradientit bie nën prag, ose pas një numri maksimal iteracionesh. Për modele ku overfitting është i mundur përdoret early stopping mbi validimin: ruhet modeli në iteracionin me performancën më të mirë të validimit. Në regresion linear konveks kjo nuk është zakonisht e nevojshme si regularizim, por ideja përgatit studentin për metoda më të avancuara.

\paragraph{SGD si vlerësues i gradientit.}
Në full-batch gradient përdorim të gjitha $N$ pikat, prandaj gradienti është i saktë për rrezikun empirik. Në SGD përdorim një pikë të rastësishme; pritja e gradientit stokastik është gradienti i plotë nëse mostrimi është uniform. Minibatch zvogëlon variancën e këtij vlerësuesi dhe shfrytëzon mirë llogaritjen vektoriale. Kështu batch size krijon kompromis midis zhurmës, kostos për hap dhe efikasitetit hardware.

\paragraph{Shembull i punuar: dy learning rates.}
Në funksionin $L(\theta)=5\theta^2/2$, update është $\theta_{n+1}=(1-5\eta)\theta_n$. Me $\eta=0.1$, faktori është 0.5 dhe konvergjenca është monotone. Me $\eta=0.3$, faktori është $-0.5$ dhe kemi oscilacion që zvogëlohet. Me $\eta=0.5$, faktori $-1.5$ jep divergjencë. Ky shembull bën të qartë pse ``learning rate më i madh'' nuk do të thotë ``më shpejt''.

\paragraph{Nga optimizimi te perceptroni dhe rrjetat.}
Perceptroni përdor update online vetëm për gabime dhe nuk minimizon cross-entropy. Regresioni logjistik minimizon një humbje të lëmuar me gradient. Rrjetat nervore të ardhshme do të përdorin të njëjtin koncept të optimizimit në një hapësirë parametrash shumë më të madhe. Kjo është arsyeja pse gradient descent vendoset para perceptronit në këtë kurs: ai është koncept i përgjithshëm numerik.

\paragraph{Diagnostika numerike.}
Një loss curve pa shkallë logaritmike mund të fshehë fazën e fundit të konvergjencës. Grafiku i normës së gradientit, learning rate dhe validation loss jep pamje më të plotë. Gjithashtu duhet kontrolluar që humbja nuk prodhon `nan` nga overflow ose logaritme të zeros. Stabiliteti numerik -- p.sh. clipping i logits ose përdorimi i funksioneve log-sum-exp -- është pjesë e implementimit profesional.
''',
'Perceptroni dhe ura drejt rrjetave nervore':r'''
\paragraph{Perceptroni si algoritëm online.}
Në secilin gabim, update varet vetëm nga shembulli aktual. Kjo e bën perceptronin të përshtatshëm për të dhëna që vijnë në rrjedhë dhe historikisht e lidh me idenë e të nxënit online. Rendi i shembujve mund të ndryshojë trajektoren dhe zgjidhjen përfundimtare, edhe pse teorema garanton konvergjencë kur ka ndashmëri lineare. Për këtë arsye në notebook përdoret shuffle me farë të kontrolluar dhe studiohet variabiliteti i numrit të gabimeve.

\paragraph{Teorema e konvergjencës në më shumë detaj.}
Pas $M$ gabimeve, projeksioni mbi ndarësin ideal rritet të paktën $M\gamma$. Nga ana tjetër, në një update të gabuar kemi $y_t w_t^Tx_t\le0$, prandaj
\[
\|w_{t+1}\|^2=\|w_t\|^2+2y_tw_t^Tx_t+\|x_t\|^2\le\|w_t\|^2+R^2.
\]
Pas $M$ gabimeve, $\|w_M\|\le R\sqrt M$. Me Cauchy--Schwarz,
$M\gamma\le w_M^Tw^*\le\|w_M\|$, dhe rezulton $M\le(R/\gamma)^2$. Ky argument është shembull i bukur i lidhjes midis gjeometrisë dhe garancisë algoritmike.

\paragraph{Çfarë nuk garanton teorema.}
Nëse të dhënat nuk janë të ndashme, perceptroni mund të vazhdojë pafund duke cikluar. Nëse ndarja ekziston por margjina është shumë e vogël, kufiri teorik i gabimeve mund të jetë i madh. Dhe edhe kur konvergon, zgjidhja nuk është domosdoshmërisht ajo me margjinë më të madhe. Kjo motivon SVM, e cila e formulon margjinën si objektiv explicit.

\paragraph{XOR dhe përfaqësimi.}
XOR tregon se problemi nuk është mungesa e kohës së trajnimit. Në hapësirën $(x_1,x_2)$ klasat janë të alternuara në cepat e katrorit dhe nuk ka hiperplan. Nëse shtojmë veçorinë $x_1x_2$, pikat vendosen në një hapësirë ku ndarja mund të bëhet lineare. Kjo ide -- transformimi i përfaqësimit -- është themelore në nxënien e thellë. Rrjetat shumë-shtresore mësojnë transformime të ndërmjetme në vend që t'i përcaktojë njeriu të gjitha veçoritë.

\paragraph{Panorama e rrjetave nervore pa hyrë në kursin pasues.}
Në MLP, çdo shtresë bën $h^{(l)}=\phi(W^{(l)}h^{(l-1)}+b^{(l)})$. Pa funksion jolinear, kompozimi i shtresave do të ishte përsëri transformim linear dhe nuk do të zgjidhte XOR në mënyrë më të fuqishme. Jolinearitetet si ReLU e ndryshojnë klasën e funksioneve. Backpropagation llogarit gradientët me rregullin e zinxhirit, por derivimi i plotë lihet për kursin Master. CNN shtojnë strukturë lokale dhe sharing të peshave; Transformer përdorin attention për ndërveprime midis elementeve të sekuencës. Këto janë zhvillime të së njëjtës filozofi: përfaqësim + funksion humbjeje + optimizim + validim.

\paragraph{Çfarë duhet të marrë studenti nga kursi.}
Qëllimi nuk është që studenti të dalë me listë algoritmesh. Ai duhet të jetë në gjendje të shohë një problem të ri fizik dhe të pyesë: çfarë është objektivi; cilat veçori janë legjitime; si ndahet dataset-i; cili baseline është i arsyeshëm; a kërkon problemi model linear, lokal, pemë, kernel, reduktim dimensional ose clustering; si do të matet pasiguria; dhe çfarë kufizimesh ka interpretimi. Perceptroni mbyll kursin sepse tregon se konceptet e mësuara -- lineariteti, humbja, margjina, optimizimi, ndashmëria dhe përfaqësimi -- janë pikërisht themeli mbi të cilin ndërtohen rrjetat nervore.
'''
}
# Insert each block before next chapter or appendices
for title,block in exp.items():
    marker='\\chapter{'+title+'}'
    start=s.find(marker)
    if start<0:
        print('missing',title); continue
    # find next chapter or appendix after start
    next_ch=s.find('\\chapter{', start+len(marker))
    next_app=s.find('\\appendix', start+len(marker))
    candidates=[x for x in (next_ch,next_app) if x!=-1]
    end=min(candidates) if candidates else len(s)
    s=s[:end]+block+'\n'+s[end:]
# slightly more readable spacing
s=s.replace('\\setstretch{1.08}','\\setstretch{1.14}')
p.write_text(s,encoding='utf-8')
print('expanded')
