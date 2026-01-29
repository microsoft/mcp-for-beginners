# MCP Security: Protecție cuprinzătoare pentru sistemele AI

[![MCP Security Best Practices](../../../translated_images/ro/03.175aed6dedae133f9d41e49cefd0f0a9a39c3317e1eaa7ef7182696af7534308.png)](https://youtu.be/88No8pw706o)

_(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

Securitatea este fundamentală pentru proiectarea sistemelor AI, motiv pentru care o prioritizăm ca a doua noastră secțiune. Acest lucru se aliniază cu principiul Microsoft **Secure by Design** din [Inițiativa Secure Future](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Protocolul Model Context (MCP) aduce capabilități noi și puternice aplicațiilor conduse de AI, introducând în același timp provocări unice de securitate care depășesc riscurile tradiționale ale software-ului. Sistemele MCP se confruntă atât cu preocupări de securitate consacrate (codare sigură, principiul privilegiului minim, securitatea lanțului de aprovizionare), cât și cu noi amenințări specifice AI, inclusiv injecția de prompturi, otrăvirea uneltelor, deturnarea sesiunii, atacurile de tip confused deputy, vulnerabilitățile de token passthrough și modificarea dinamică a capabilităților.

Această lecție explorează cele mai critice riscuri de securitate în implementările MCP—acoperind autentificarea, autorizarea, permisiunile excesive, injecția indirectă de prompturi, securitatea sesiunii, problemele confused deputy, gestionarea tokenurilor și vulnerabilitățile lanțului de aprovizionare. Veți învăța controale acționabile și cele mai bune practici pentru a atenua aceste riscuri, folosind soluții Microsoft precum Prompt Shields, Azure Content Safety și GitHub Advanced Security pentru a întări implementarea MCP.

## Obiective de învățare

La finalul acestei lecții, veți putea:

- **Identifica amenințările specifice MCP**: Recunoaște riscurile unice de securitate în sistemele MCP, inclusiv injecția de prompturi, otrăvirea uneltelor, permisiunile excesive, deturnarea sesiunii, problemele confused deputy, vulnerabilitățile token passthrough și riscurile lanțului de aprovizionare
- **Aplica controale de securitate**: Implementa atenuări eficiente, inclusiv autentificare robustă, acces cu privilegiu minim, gestionare sigură a tokenurilor, controale de securitate a sesiunii și verificarea lanțului de aprovizionare
- **Valorifica soluțiile de securitate Microsoft**: Înțelege și implementa Microsoft Prompt Shields, Azure Content Safety și GitHub Advanced Security pentru protecția încărcăturilor MCP
- **Valida securitatea uneltelor**: Recunoaște importanța validării metadatelor uneltelor, monitorizării modificărilor dinamice și apărării împotriva atacurilor indirecte de injecție de prompturi
- **Integra cele mai bune practici**: Combina fundamentele securității consacrate (codare sigură, întărirea serverului, zero trust) cu controale specifice MCP pentru o protecție cuprinzătoare

# Arhitectura și controalele de securitate MCP

Implementările moderne MCP necesită abordări de securitate stratificate care să abordeze atât securitatea tradițională a software-ului, cât și amenințările specifice AI. Specificația MCP, în continuă evoluție rapidă, își maturizează controalele de securitate, permițând o integrare mai bună cu arhitecturile de securitate enterprise și cele mai bune practici consacrate.

Cercetările din [Microsoft Digital Defense Report](https://aka.ms/mddr) demonstrează că **98% din breșele raportate ar fi prevenite printr-o igienă robustă a securității**. Strategia de protecție cea mai eficientă combină practicile fundamentale de securitate cu controale specifice MCP—măsurile de securitate de bază dovedite rămân cele mai impactante în reducerea riscului general de securitate.

## Peisajul actual al securității

> **Notă:** Aceste informații reflectă standardele de securitate MCP la data de **18 decembrie 2025**. Protocolul MCP continuă să evolueze rapid, iar implementările viitoare pot introduce noi modele de autentificare și controale îmbunătățite. Consultați întotdeauna [Specificația MCP](https://spec.modelcontextprotocol.io/), [repository-ul MCP GitHub](https://github.com/modelcontextprotocol) și [documentația celor mai bune practici de securitate](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices) pentru cele mai recente recomandări.

### Evoluția autentificării MCP

Specificația MCP a evoluat semnificativ în abordarea autentificării și autorizării:

- **Abordarea originală**: Specificațiile timpurii cereau dezvoltatorilor să implementeze servere de autentificare personalizate, serverele MCP acționând ca servere OAuth 2.0 de autorizare care gestionau autentificarea utilizatorilor direct
- **Standardul curent (2025-11-25)**: Specificația actualizată permite serverelor MCP să delege autentificarea către furnizori externi de identitate (cum ar fi Microsoft Entra ID), îmbunătățind postura de securitate și reducând complexitatea implementării
- **Securitatea nivelului de transport**: Suport îmbunătățit pentru mecanisme de transport securizate cu modele corecte de autentificare atât pentru conexiuni locale (STDIO), cât și pentru cele la distanță (Streamable HTTP)

## Securitatea autentificării și autorizării

### Provocări actuale de securitate

Implementările moderne MCP se confruntă cu mai multe provocări legate de autentificare și autorizare:

### Riscuri și vectori de amenințare

- **Logică de autorizare configurată greșit**: Implementarea defectuoasă a autorizării în serverele MCP poate expune date sensibile și poate aplica incorect controalele de acces
- **Compromiterea tokenurilor OAuth**: Furtul tokenurilor de pe serverele MCP locale permite atacatorilor să se deghizeze în servere și să acceseze servicii downstream
- **Vulnerabilități token passthrough**: Gestionarea necorespunzătoare a tokenurilor creează ocoliri ale controalelor de securitate și lacune de responsabilitate
- **Permisiuni excesive**: Serverele MCP cu privilegii prea mari încalcă principiul privilegiului minim și extind suprafețele de atac

#### Token passthrough: un anti-pattern critic

**Token passthrough este explicit interzis** în specificația curentă de autorizare MCP din cauza implicațiilor grave de securitate:

##### Ocolirea controalelor de securitate
- Serverele MCP și API-urile downstream implementează controale critice de securitate (limitarea ratei, validarea cererilor, monitorizarea traficului) care depind de validarea corectă a tokenurilor
- Utilizarea directă a tokenurilor client-API ocolește aceste protecții esențiale, subminând arhitectura de securitate

##### Provocări de responsabilitate și audit  
- Serverele MCP nu pot distinge între clienții care folosesc tokenuri emise upstream, perturbând traseele de audit
- Jurnalele serverelor de resurse downstream arată origini ale cererilor înșelătoare, nu intermediarii reali MCP
- Investigarea incidentelor și auditul conformității devin mult mai dificile

##### Riscuri de exfiltrare a datelor
- Afirmările nevalidate ale tokenurilor permit actorilor rău intenționați cu tokenuri furate să folosească serverele MCP ca proxy-uri pentru exfiltrarea datelor
- Încălcări ale limitelor de încredere permit modele de acces neautorizat care ocolesc controalele de securitate intenționate

##### Vectori de atac multi-serviciu
- Tokenurile compromise acceptate de mai multe servicii permit mișcări laterale între sisteme conectate
- Presupunerile de încredere între servicii pot fi încălcate când originea tokenurilor nu poate fi verificată

### Controale și atenuări de securitate

**Cerințe critice de securitate:**

> **OBLIGATORIU**: Serverele MCP **NU TREBUIE** să accepte niciun token care nu a fost emis explicit pentru serverul MCP

#### Controale de autentificare și autorizare

- **Revizuire riguroasă a autorizării**: Efectuați audituri cuprinzătoare ale logicii de autorizare a serverului MCP pentru a asigura că doar utilizatorii și clienții intenționați pot accesa resurse sensibile
  - **Ghid de implementare**: [Azure API Management ca gateway de autentificare pentru serverele MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrare identitate**: [Utilizarea Microsoft Entra ID pentru autentificarea serverului MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Gestionare sigură a tokenurilor**: Implementați [cele mai bune practici Microsoft pentru validarea și ciclul de viață al tokenurilor](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validați afirmațiile audienței tokenului să corespundă identității serverului MCP
  - Implementați politici corecte de rotație și expirare a tokenurilor
  - Preveniți atacurile de redare a tokenurilor și utilizarea neautorizată

- **Stocare protejată a tokenurilor**: Asigurați stocarea tokenurilor cu criptare atât în repaus, cât și în tranzit
  - **Cele mai bune practici**: [Ghiduri pentru stocarea și criptarea sigură a tokenurilor](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementarea controlului accesului

- **Principiul privilegiului minim**: Acordați serverelor MCP doar permisiunile minime necesare pentru funcționalitatea intenționată
  - Revizuiri și actualizări regulate ale permisiunilor pentru a preveni creșterea privilegiilor
  - **Documentație Microsoft**: [Acces securizat cu privilegiu minim](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Controlul accesului bazat pe roluri (RBAC)**: Implementați atribuiri de roluri detaliate
  - Limitați rolurile strict la resurse și acțiuni specifice
  - Evitați permisiunile largi sau inutile care extind suprafețele de atac

- **Monitorizarea continuă a permisiunilor**: Implementați audit și monitorizare continuă a accesului
  - Monitorizați tiparele de utilizare a permisiunilor pentru anomalii
  - Remediați prompt privilegiile excesive sau neutilizate

## Amenințări specifice securității AI

### Atacuri de injecție de prompturi și manipulare a uneltelor

Implementările moderne MCP se confruntă cu vectori de atac sofisticați specifici AI pe care măsurile tradiționale de securitate nu îi pot aborda complet:

#### **Injecția indirectă de prompturi (Injecție cross-domain de prompturi)**

**Injecția indirectă de prompturi** reprezintă una dintre cele mai critice vulnerabilități în sistemele AI activate MCP. Atacatorii încorporează instrucțiuni malițioase în conținut extern—documente, pagini web, emailuri sau surse de date—pe care sistemele AI le procesează ulterior ca comenzi legitime.

**Scenarii de atac:**
- **Injecție bazată pe documente**: Instrucțiuni malițioase ascunse în documente procesate care declanșează acțiuni AI neintenționate
- **Exploatarea conținutului web**: Pagini web compromise care conțin prompturi încorporate ce manipulează comportamentul AI când sunt extrase
- **Atacuri prin email**: Prompturi malițioase în emailuri care determină asistenții AI să divulge informații sau să execute acțiuni neautorizate
- **Contaminarea surselor de date**: Baze de date sau API-uri compromise care servesc conținut contaminat sistemelor AI

**Impact în lumea reală**: Aceste atacuri pot duce la exfiltrarea datelor, încălcări ale confidențialității, generarea de conținut dăunător și manipularea interacțiunilor utilizatorilor. Pentru o analiză detaliată, vedeți [Injecția de prompturi în MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Prompt Injection Attack Diagram](../../../translated_images/ro/prompt-injection.ed9fbfde297ca877c15bc6daa808681cd3c3dc7bf27bbbda342ef1ba5fc4f52d.png)

#### **Atacuri de otrăvire a uneltelor**

**Otrăvirea uneltelor** vizează metadatele care definesc uneltele MCP, exploatând modul în care LLM-urile interpretează descrierile și parametrii uneltelor pentru a lua decizii de execuție.

**Mecanisme de atac:**
- **Manipularea metadatelor**: Atacatorii injectează instrucțiuni malițioase în descrierile uneltelor, definițiile parametrilor sau exemplele de utilizare
- **Instrucțiuni invizibile**: Prompturi ascunse în metadatele uneltelor care sunt procesate de modelele AI, dar invizibile utilizatorilor umani
- **Modificarea dinamică a uneltelor („Rug Pulls”)**: Uneltele aprobate de utilizatori sunt modificate ulterior pentru a executa acțiuni malițioase fără știrea utilizatorului
- **Injecția de parametri**: Conținut malițios încorporat în schemele parametrilor uneltelor care influențează comportamentul modelului

**Riscuri pentru serverele găzduite**: Serverele MCP la distanță prezintă riscuri ridicate deoarece definițiile uneltelor pot fi actualizate după aprobarea inițială a utilizatorului, creând scenarii în care uneltele anterior sigure devin malițioase. Pentru o analiză completă, vedeți [Atacuri de otrăvire a uneltelor (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Tool Injection Attack Diagram](../../../translated_images/ro/tool-injection.3b0b4a6b24de6befe7d3afdeae44138ef005881aebcfc84c6f61369ce31e3640.png)

#### **Vectori suplimentari de atac AI**

- **Injecția cross-domain de prompturi (XPIA)**: Atacuri sofisticate care folosesc conținut din mai multe domenii pentru a ocoli controalele de securitate
- **Modificarea dinamică a capabilităților**: Schimbări în timp real ale capabilităților uneltelor care scapă evaluărilor inițiale de securitate
- **Otrăvirea ferestrei de context**: Atacuri care manipulează ferestre mari de context pentru a ascunde instrucțiuni malițioase
- **Atacuri de confuzie a modelului**: Exploatarea limitărilor modelului pentru a crea comportamente imprevizibile sau nesigure

### Impactul riscurilor de securitate AI

**Consecințe cu impact ridicat:**
- **Exfiltrarea datelor**: Acces neautorizat și furt de date sensibile enterprise sau personale
- **Încălcări ale confidențialității**: Expunerea informațiilor personale identificabile (PII) și a datelor confidențiale de afaceri  
- **Manipularea sistemelor**: Modificări neintenționate ale sistemelor și fluxurilor de lucru critice
- **Furtul de acreditări**: Compromiterea tokenurilor de autentificare și a acreditărilor serviciilor
- **Mișcare laterală**: Utilizarea sistemelor AI compromise ca pivot pentru atacuri mai largi în rețea

### Soluții Microsoft pentru securitatea AI

#### **AI Prompt Shields: Protecție avansată împotriva atacurilor de injecție**

Microsoft **AI Prompt Shields** oferă o apărare cuprinzătoare împotriva atacurilor de injecție de prompturi directe și indirecte prin mai multe straturi de securitate:

##### **Mecanisme principale de protecție:**

1. **Detectare și filtrare avansată**
   - Algoritmi de învățare automată și tehnici NLP detectează instrucțiuni malițioase în conținutul extern
   - Analiză în timp real a documentelor, paginilor web, emailurilor și surselor de date pentru amenințări încorporate
   - Înțelegere contextuală a tiparelor legitime vs. malițioase de prompturi

2. **Tehnici de evidențiere**  
   - Distinge între instrucțiunile de sistem de încredere și intrările externe potențial compromise
   - Metode de transformare a textului care sporesc relevanța modelului, izolând conținutul malițios
   - Ajută sistemele AI să mențină ierarhia corectă a instrucțiunilor și să ignore comenzile injectate

3. **Sisteme de delimitare și marcare a datelor**
   - Definirea explicită a limitelor între mesajele de sistem de încredere și textul de intrare extern
   - Marcatori speciali evidențiază granițele dintre sursele de date de încredere și cele neîncredere
   - Separare clară care previne confuzia instrucțiunilor și execuția neautorizată a comenzilor

4. **Inteligență continuă asupra amenințărilor**
   - Microsoft monitorizează continuu modelele emergente de atac și actualizează apărarea
   - Vânătoare proactivă de amenințări pentru noi tehnici de injecție și vectori de atac
   - Actualizări regulate ale modelelor de securitate pentru a menține eficacitatea împotriva amenințărilor în evoluție

5. **Integrare Azure Content Safety**
   - Parte a suitei cuprinzătoare Azure AI Content Safety
   - Detectare suplimentară pentru încercări de jailbreak, conținut dăunător și încălcări ale politicilor de securitate
   - Controale de securitate unificate în toate componentele aplicațiilor AI

**Resurse de implementare**: [Documentația Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Microsoft Prompt Shields Protection](../../../translated_images/ro/prompt-shield.ff5b95be76e9c78c6ec0888206a4a6a0a5ab4bb787832a9eceef7a62fe0138d1.png)


## Amenințări avansate de securitate MCP

### Vulnerabilități de deturnare a sesiunii

**Deturnarea sesiunii** reprezintă un vector critic de atac în implementările MCP stateful, unde părți neautorizate obțin și abuzează identificatori legitimi de sesiune pentru a se deghiza în clienți și a efectua acțiuni neautorizate.

#### **Scenarii și riscuri de atac**

- **Injecție de prompturi prin deturnarea sesiunii**: Atacatorii cu ID-uri de sesiune furate injectează evenimente malițioase în servere care partajează starea sesiunii, declanșând potențial acțiuni dăunătoare sau accesând date sensibile
- **Impersonare directă**: ID-urile de sesiune furate permit apeluri directe către serverul MCP care ocolesc autentificarea, tratând atacatorii ca utilizatori legitimi
- **Fluxuri reluabile compromise**: Atacatorii pot întrerupe cererile prematur, determinând clienții legitimi să reia cu conținut potențial malițios

#### **Controale de securitate pentru gestionarea sesiunii**

**Cerințe critice:**
- **Verificarea autorizării**: Serverele MCP care implementează autorizarea **TREBUIE** să verifice TOATE cererile primite și **NU TREBUIE** să se bazeze pe sesiuni pentru autentificare
- **Generarea securizată a sesiunilor**: Folosiți ID-uri de sesiune criptografic sigure, nedeterministe, generate cu generatoare de numere aleatoare securizate
- **Legarea specifică utilizatorului**: Legați ID-urile de sesiune de informații specifice utilizatorului folosind formate precum `<user_id>:<session_id>` pentru a preveni abuzul sesiunilor între utilizatori
- **Gestionarea ciclului de viață al sesiunii**: Implementați expirarea, rotația și invalidarea corespunzătoare pentru a limita ferestrele de vulnerabilitate
- **Securitatea transportului**: HTTPS obligatoriu pentru toată comunicarea pentru a preveni interceptarea ID-urilor de sesiune

### Problema deputatului confuz

**Problema deputatului confuz** apare atunci când serverele MCP acționează ca proxy-uri de autentificare între clienți și servicii terțe, creând oportunități pentru ocolirea autorizării prin exploatarea ID-urilor statice ale clientului.

#### **Mecanismele atacului și riscuri**

- **Ocolirea consimțământului bazată pe cookie-uri**: Autentificarea anterioară a utilizatorului creează cookie-uri de consimțământ pe care atacatorii le exploatează prin cereri de autorizare malițioase cu URI-uri de redirecționare construite
- **Furtul codului de autorizare**: Cookie-urile de consimțământ existente pot determina serverele de autorizare să sară peste ecranele de consimțământ, redirecționând codurile către endpoint-uri controlate de atacator  
- **Acces neautorizat la API**: Codurile de autorizare furate permit schimbul de token-uri și impersonarea utilizatorului fără aprobare explicită

#### **Strategii de atenuare**

**Controale obligatorii:**
- **Cereri explicite de consimțământ**: Serverele proxy MCP care folosesc ID-uri statice ale clientului **TREBUIE** să obțină consimțământul utilizatorului pentru fiecare client înregistrat dinamic
- **Implementarea securității OAuth 2.1**: Urmați cele mai bune practici actuale de securitate OAuth, inclusiv PKCE (Proof Key for Code Exchange) pentru toate cererile de autorizare
- **Validare strictă a clientului**: Implementați o validare riguroasă a URI-urilor de redirecționare și a identificatorilor clientului pentru a preveni exploatarea

### Vulnerabilități de tip token passthrough  

**Token passthrough** reprezintă un anti-pattern explicit în care serverele MCP acceptă token-uri ale clientului fără validare corespunzătoare și le transmit către API-urile downstream, încălcând specificațiile de autorizare MCP.

#### **Implicații de securitate**

- **Ocolirea controlului**: Utilizarea directă a token-urilor client către API ocolește controalele critice de limitare a ratei, validare și monitorizare
- **Coruperea traseului de audit**: Token-urile emise upstream fac imposibilă identificarea clientului, afectând capacitatea de investigare a incidentelor
- **Exfiltrarea datelor prin proxy**: Token-urile nevalidate permit actorilor malițioși să folosească serverele ca proxy-uri pentru acces neautorizat la date
- **Încălcarea limitelor de încredere**: Serviciile downstream pot avea încălcate presupunerile de încredere când originea token-urilor nu poate fi verificată
- **Extinderea atacurilor multi-serviciu**: Token-urile compromise acceptate pe mai multe servicii permit mișcarea laterală

#### **Controale de securitate necesare**

**Cerințe de netrecut cu vederea:**
- **Validarea token-urilor**: Serverele MCP **NU TREBUIE** să accepte token-uri care nu sunt emise explicit pentru serverul MCP
- **Verificarea audienței**: Verificați întotdeauna că revendicările audienței token-ului corespund identității serverului MCP
- **Ciclul de viață corect al token-ului**: Implementați token-uri de acces cu durată scurtă și practici sigure de rotație


## Securitatea lanțului de aprovizionare pentru sistemele AI

Securitatea lanțului de aprovizionare a evoluat dincolo de dependențele software tradiționale pentru a cuprinde întregul ecosistem AI. Implementările moderne MCP trebuie să verifice și să monitorizeze riguros toate componentele legate de AI, deoarece fiecare introduce potențiale vulnerabilități care ar putea compromite integritatea sistemului.

### Componente extinse ale lanțului de aprovizionare AI

**Dependențe software tradiționale:**
- Biblioteci și cadre open-source
- Imagini de container și sisteme de bază  
- Unelte de dezvoltare și pipeline-uri de build
- Componente și servicii de infrastructură

**Elemente specifice lanțului de aprovizionare AI:**
- **Modele fundamentale**: Modele pre-antrenate de la diverși furnizori care necesită verificarea provenienței
- **Servicii de embedding**: Servicii externe de vectorizare și căutare semantică
- **Furnizori de context**: Surse de date, baze de cunoștințe și depozite de documente  
- **API-uri terțe**: Servicii AI externe, pipeline-uri ML și endpoint-uri de procesare a datelor
- **Artefacte de model**: Greutăți, configurații și variante de modele fine-tunate
- **Surse de date pentru antrenament**: Seturi de date folosite pentru antrenarea și fine-tuning-ul modelelor

### Strategie cuprinzătoare de securitate a lanțului de aprovizionare

#### **Verificarea componentelor și încrederea**
- **Validarea provenienței**: Verificați originea, licențierea și integritatea tuturor componentelor AI înainte de integrare
- **Evaluarea securității**: Efectuați scanări de vulnerabilități și revizuiri de securitate pentru modele, surse de date și servicii AI
- **Analiza reputației**: Evaluați istoricul de securitate și practicile furnizorilor de servicii AI
- **Verificarea conformității**: Asigurați-vă că toate componentele respectă cerințele organizaționale de securitate și reglementare

#### **Pipeline-uri de implementare securizate**  
- **Securitate CI/CD automatizată**: Integrați scanarea de securitate în pipeline-urile automate de implementare
- **Integritatea artefactelor**: Implementați verificarea criptografică pentru toate artefactele implementate (cod, modele, configurații)
- **Implementare etapizată**: Folosiți strategii progresive de implementare cu validare de securitate la fiecare etapă
- **Depozite de artefacte de încredere**: Implementați doar din registre și depozite de artefacte verificate și securizate

#### **Monitorizare continuă și răspuns**
- **Scanarea dependențelor**: Monitorizare continuă a vulnerabilităților pentru toate dependențele software și componentele AI
- **Monitorizarea modelelor**: Evaluare continuă a comportamentului modelului, derapajului performanței și anomaliilor de securitate
- **Urmărirea sănătății serviciilor**: Monitorizați serviciile AI externe pentru disponibilitate, incidente de securitate și schimbări de politică
- **Integrarea informațiilor despre amenințări**: Încorporați fluxuri de amenințări specifice riscurilor de securitate AI și ML

#### **Controlul accesului și principiul privilegiului minim**
- **Permisiuni la nivel de componentă**: Restricționați accesul la modele, date și servicii pe baza necesității de afaceri
- **Gestionarea conturilor de serviciu**: Implementați conturi de serviciu dedicate cu permisiuni minime necesare
- **Segmentarea rețelei**: Izolați componentele AI și limitați accesul în rețea între servicii
- **Controale API Gateway**: Folosiți gateway-uri API centralizate pentru a controla și monitoriza accesul la serviciile AI externe

#### **Răspuns la incidente și recuperare**
- **Proceduri rapide de răspuns**: Procese stabilite pentru patch-uri sau înlocuirea componentelor AI compromise
- **Rotația acreditărilor**: Sisteme automate pentru rotația secretelor, cheilor API și acreditărilor de serviciu
- **Capabilități de rollback**: Posibilitatea de a reveni rapid la versiuni anterioare cunoscute ca fiind bune ale componentelor AI
- **Recuperarea după breșe în lanțul de aprovizionare**: Proceduri specifice pentru răspuns la compromiterea serviciilor AI upstream

### Instrumente și integrare Microsoft pentru securitate

**GitHub Advanced Security** oferă protecție cuprinzătoare a lanțului de aprovizionare, inclusiv:
- **Scanarea secretelor**: Detectare automată a acreditărilor, cheilor API și token-urilor în depozite
- **Scanarea dependențelor**: Evaluarea vulnerabilităților pentru dependențele și bibliotecile open-source
- **Analiza CodeQL**: Analiză statică a codului pentru vulnerabilități de securitate și probleme de codare
- **Informații despre lanțul de aprovizionare**: Vizibilitate asupra sănătății și stării de securitate a dependențelor

**Integrarea Azure DevOps & Azure Repos:**
- Integrare fără întreruperi a scanării de securitate pe platformele Microsoft de dezvoltare
- Verificări automate de securitate în Azure Pipelines pentru sarcini AI
- Aplicarea politicilor pentru implementarea securizată a componentelor AI

**Practici interne Microsoft:**
Microsoft implementează practici extinse de securitate a lanțului de aprovizionare în toate produsele. Aflați despre abordările dovedite în [The Journey to Secure the Software Supply Chain at Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Cele mai bune practici de securitate fundamentale

Implementările MCP moștenesc și construiesc pe baza posturii de securitate existente a organizației dvs. Consolidarea practicilor fundamentale de securitate îmbunătățește semnificativ securitatea generală a sistemelor AI și a implementărilor MCP.

### Fundamentele de bază ale securității

#### **Practici de dezvoltare securizată**
- **Conformitate OWASP**: Protecție împotriva vulnerabilităților web din [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Protecții specifice AI**: Implementați controale pentru [OWASP Top 10 pentru LLM-uri](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Gestionarea securizată a secretelor**: Folosiți seifuri dedicate pentru token-uri, chei API și date sensibile de configurare
- **Criptare end-to-end**: Implementați comunicații securizate în toate componentele aplicației și fluxurile de date
- **Validarea inputurilor**: Validare riguroasă a tuturor intrărilor utilizatorilor, parametrilor API și surselor de date

#### **Întărirea infrastructurii**
- **Autentificare multi-factor**: MFA obligatorie pentru toate conturile administrative și de serviciu
- **Gestionarea patch-urilor**: Aplicarea automată și la timp a patch-urilor pentru sisteme de operare, cadre și dependențe  
- **Integrarea furnizorului de identitate**: Management centralizat al identității prin furnizori enterprise (Microsoft Entra ID, Active Directory)
- **Segmentarea rețelei**: Izolare logică a componentelor MCP pentru a limita potențialul de mișcare laterală
- **Principiul privilegiului minim**: Permisiuni minime necesare pentru toate componentele și conturile sistemului

#### **Monitorizare și detectare a securității**
- **Logare cuprinzătoare**: Înregistrare detaliată a activităților aplicațiilor AI, inclusiv interacțiunile client-server MCP
- **Integrare SIEM**: Management centralizat al informațiilor și evenimentelor de securitate pentru detectarea anomaliilor
- **Analiză comportamentală**: Monitorizare asistată de AI pentru detectarea tiparelor neobișnuite în comportamentul sistemului și utilizatorilor
- **Informații despre amenințări**: Integrarea fluxurilor externe de amenințări și indicatori de compromitere (IOC-uri)
- **Răspuns la incidente**: Proceduri bine definite pentru detectarea, răspunsul și recuperarea în caz de incidente de securitate

#### **Arhitectura Zero Trust**
- **Niciodată nu ai încredere, verifică întotdeauna**: Verificare continuă a utilizatorilor, dispozitivelor și conexiunilor de rețea
- **Micro-segmentare**: Controale granulare de rețea care izolează sarcinile și serviciile individuale
- **Securitate centrată pe identitate**: Politici de securitate bazate pe identități verificate, nu pe locația în rețea
- **Evaluare continuă a riscurilor**: Evaluarea dinamică a posturii de securitate bazată pe contextul și comportamentul curent
- **Acces condiționat**: Controale de acces care se adaptează în funcție de factori de risc, locație și încrederea dispozitivului

### Modele de integrare enterprise

#### **Integrarea ecosistemului Microsoft Security**
- **Microsoft Defender for Cloud**: Management cuprinzător al posturii de securitate în cloud
- **Azure Sentinel**: Capacități native cloud SIEM și SOAR pentru protecția sarcinilor AI
- **Microsoft Entra ID**: Management enterprise al identității și accesului cu politici de acces condiționat
- **Azure Key Vault**: Management centralizat al secretelor cu suport hardware security module (HSM)
- **Microsoft Purview**: Guvernanță și conformitate a datelor pentru sursele și fluxurile de lucru AI

#### **Conformitate și guvernanță**
- **Aliniere la reglementări**: Asigurați-vă că implementările MCP respectă cerințele de conformitate specifice industriei (GDPR, HIPAA, SOC 2)
- **Clasificarea datelor**: Categorizare și gestionare adecvată a datelor sensibile procesate de sistemele AI
- **Trasee de audit**: Logare cuprinzătoare pentru conformitate reglementară și investigații judiciare
- **Controale de confidențialitate**: Implementarea principiilor privacy-by-design în arhitectura sistemelor AI
- **Managementul schimbărilor**: Procese formale pentru revizuiri de securitate ale modificărilor sistemelor AI

Aceste practici fundamentale creează o bază solidă de securitate care sporește eficacitatea controalelor specifice MCP și oferă protecție cuprinzătoare pentru aplicațiile bazate pe AI.

## Concluzii cheie privind securitatea

- **Abordare stratificată a securității**: Combinați practicile fundamentale de securitate (codare securizată, privilegiu minim, verificarea lanțului de aprovizionare, monitorizare continuă) cu controale specifice AI pentru protecție cuprinzătoare

- **Peisaj de amenințări specific AI**: Sistemele MCP se confruntă cu riscuri unice, inclusiv injecția de prompturi, otrăvirea uneltelor, deturnarea sesiunilor, problema deputatului confuz, vulnerabilități token passthrough și permisiuni excesive care necesită atenuări specializate

- **Excelență în autentificare și autorizare**: Implementați autentificare robustă folosind furnizori externi de identitate (Microsoft Entra ID), aplicați validarea corectă a token-urilor și nu acceptați niciodată token-uri care nu sunt emise explicit pentru serverul MCP

- **Prevenirea atacurilor AI**: Implementați Microsoft Prompt Shields și Azure Content Safety pentru a apăra împotriva injecției indirecte de prompturi și atacurilor de otrăvire a uneltelor, validând metadatele uneltelor și monitorizând schimbările dinamice

- **Securitatea sesiunii și transportului**: Folosiți ID-uri de sesiune criptografic sigure, nedeterministe, legate de identitățile utilizatorilor, implementați gestionarea corectă a ciclului de viață al sesiunii și nu folosiți niciodată sesiuni pentru autentificare

- **Cele mai bune practici OAuth**: Preveniți atacurile deputatului confuz prin consimțământ explicit al utilizatorului pentru clienții înregistrați dinamic, implementarea corectă OAuth 2.1 cu PKCE și validarea strictă a URI-urilor de redirecționare  

- **Principii de securitate a token-urilor**: Evitați anti-pattern-urile token passthrough, validați revendicările audienței token-urilor, implementați token-uri cu durată scurtă și rotație securizată și mențineți limite clare de încredere

- **Securitate cuprinzătoare a lanțului de aprovizionare**: Tratați toate componentele ecosistemului AI (modele, embedding-uri, furnizori de context, API-uri externe) cu aceeași rigoare de securitate ca dependențele software tradiționale

- **Evoluție continuă**: Rămâneți la curent cu specificațiile MCP în rapidă evoluție, contribuiți la standardele comunității de securitate și mențineți posturi de securitate adaptive pe măsură ce protocolul se maturizează

- **Integrarea securității Microsoft**: Valorificați ecosistemul cuprinzător de securitate Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) pentru protecție sporită a implementărilor MCP

## Resurse cuprinzătoare

### **Documentație oficială de securitate MCP**
- [Specificația MCP (Actual: 2025-11-25)](https://spec.modelcontextprotocol.io/specification/2025-11-25/)
- [Cele mai bune practici de securitate MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/security_best_practices)
- [Specificația de autorizare MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [Depozitul GitHub MCP](https://github.com/modelcontextprotocol)

### **Standarde și cele mai bune practici de securitate**
- [Cele mai bune practici de securitate OAuth 2.0 (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 pentru securitatea aplicațiilor web](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 pentru modele de limbaj mari](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Raportul Microsoft Digital Defense](https://aka.ms/mddr)

### **Cercetare și analiză în securitatea AI**
- [Injecția de prompturi în MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Atacuri de otrăvire a uneltelor (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [Informare de Cercetare în Securitate MCP (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Soluții de Securitate Microsoft**
- [Documentație Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Serviciul Azure Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Securitate Microsoft Entra ID](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Cele mai bune practici pentru gestionarea token-urilor Azure](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Ghiduri de Implementare & Tutoriale**
- [Azure API Management ca Poartă de Autentificare MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Autentificare Microsoft Entra ID cu servere MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Stocare și criptare sigură a token-urilor (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **Securitate DevOps & Lanț de Aprovizionare**
- [Securitate Azure DevOps](https://azure.microsoft.com/products/devops)
- [Securitate Azure Repos](https://azure.microsoft.com/products/devops/repos/)
- [Călătoria Microsoft pentru Securitatea Lanțului de Aprovizionare](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Documentație Suplimentară de Securitate**

Pentru ghiduri complete de securitate, consultați aceste documente specializate din această secțiune:

- **[Cele mai bune practici de securitate MCP 2025](./mcp-security-best-practices-2025.md)** - Cele mai complete practici de securitate pentru implementările MCP
- **[Implementarea Azure Content Safety](./azure-content-safety-implementation.md)** - Exemple practice de implementare pentru integrarea Azure Content Safety  
- **[Controale de securitate MCP 2025](./mcp-security-controls-2025.md)** - Cele mai noi controale și tehnici de securitate pentru implementările MCP
- **[Referință rapidă pentru cele mai bune practici MCP](./mcp-best-practices.md)** - Ghid de referință rapidă pentru practicile esențiale de securitate MCP

---

## Ce urmează

Următorul: [Capitolul 3: Începutul](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->