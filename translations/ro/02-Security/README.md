# Securitatea MCP: Protecție cuprinzătoare pentru sistemele AI

[![Cele mai bune practici de securitate MCP](../../../translated_images/ro/03.175aed6dedae133f.webp)](https://youtu.be/88No8pw706o)

_(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul lecției)_

Securitatea este fundamentală pentru proiectarea sistemelor AI, motiv pentru care o prioritizăm ca a doua noastră secțiune. Aceasta este în concordanță cu principiul Microsoft **Secure by Design** din cadrul [Inițiativei Viitorului Securizat](https://www.microsoft.com/security/blog/2025/04/17/microsofts-secure-by-design-journey-one-year-of-success/).

Protocolul Model Context (MCP) aduce capacități puternice aplicațiilor conduse de AI, introducând totodată provocări unice de securitate care depășesc riscurile tradiționale ale software-ului. Sistemele MCP se confruntă atât cu preocupări de securitate deja stabilite (programare sigură, principiul privilegiului minim, securitatea lanțului de aprovizionare), cât și cu amenințări specifice AI, incluzând injecția de prompt, otrăvirea instrumentelor, deturnarea sesiunilor, atacurile „confused deputy”, vulnerabilitățile la trecerea token-urilor și modificarea dinamică a capabilităților.

Această lecție explorează cele mai critice riscuri de securitate în implementările MCP — acoperind autentificarea, autorizarea, permisiunile excesive, injecția indirectă de prompt, securitatea sesiunii, problemele „confused deputy”, gestionarea token-urilor și vulnerabilitățile lanțului de aprovizionare. Veți învăța controale și practici recomandate ce pot fi aplicate pentru a atenua aceste riscuri, valorificând soluțiile Microsoft precum Prompt Shields, Azure Content Safety și GitHub Advanced Security pentru a întări implementarea MCP.

## Obiective de învățare

La sfârșitul acestei lecții, veți putea:

- **Identifica amenințările specifice MCP**: Recunoaște riscurile de securitate unice ale sistemelor MCP, inclusiv injecția de prompt, otrăvirea instrumentelor, permisiunile excesive, deturnarea sesiunilor, problemele „confused deputy”, vulnerabilitățile la trecerea token-urilor și riscurile lanțului de aprovizionare
- **Aplica controale de securitate**: Implementa mitigații eficiente, inclusiv autentificare robustă, acces la privilegiul minim, gestionarea sigură a token-urilor, controale de securitate a sesiunii și verificarea lanțului de aprovizionare
- **Valorifica soluțiile Microsoft pentru securitate**: Înțelege și implementa Microsoft Prompt Shields, Azure Content Safety și GitHub Advanced Security pentru protecția încărcăturii de muncă MCP
- **Valida securitatea instrumentelor**: Recunoaște importanța validării metadatelor instrumentelor, monitorizării modificărilor dinamice și apărării împotriva atacurilor de injecție de prompt indirectă
- **Integra cele mai bune practici**: Combină fundamentele securității stabilite (programare sigură, întărirea serverelor, zero trust) cu controale specifice MCP pentru protecție cuprinzătoare

# Arhitectura și controalele de securitate MCP

Implementările moderne MCP necesită abordări de securitate stratificate care să abordeze atât securitatea tradițională a software-ului, cât și amenințările specifice AI. Specificația MCP în continuă evoluție maturizează controalele de securitate, facilitând o mai bună integrare cu arhitecturile de securitate enterprise și cele mai bune practici consacrate.

Cercetările din [Raportul Microsoft Digital Defense](https://aka.ms/mddr) demonstrează că **98% din breșele raportate puteau fi prevenite printr-o igienă solidă de securitate**. Strategia cea mai eficientă de protecție combină practici fundamentale de securitate cu controale specifice MCP — măsurile de securitate de bază dovedite rămân cele mai impactante în reducerea riscului general de securitate.

## Peisajul actual al securității

> **Notă:** Acest capitol combină controalele de securitate MCP stabilite cu
> ghidajul curent de autorizare din **Specificatia MCP 2026-07-28**. Consultați întotdeauna
> [Specificatia MCP](https://modelcontextprotocol.io/specification/2026-07-28/),
> [depozitul GitHub MCP](https://github.com/modelcontextprotocol) și
> [documentația celor mai bune practici de securitate](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
> la implementarea codului sensibil la securitate.

> **Actualizare autorizare:** MCP `2026-07-28` solicită clienților să valideze
> parametrul `iss` în răspunsurile de autorizare (RFC 9207) și să asocieze acreditările înregistrate
> cu serverul de autorizare emitent. Înregistrarea dinamică a clientului
> este depreciată; noile implementări trebuie să utilizeze Documente Metadata pentru ID-ul Clientului.
> Consultați [Ce s-a schimbat în MCP: Specificația 2026-07-28](../01-CoreConcepts/mcp-2026-07-28.md)
> pentru lista completă a modificărilor în autorizare.

## 🏔️ Atelierul MCP Security Summit (Sherpa)

Pentru **instruire practică în securitate**, recomandăm cu tărie **Atelierul MCP Security Summit** (Sherpa) — o expediție ghidată cuprinzătoare pentru securizarea serverelor MCP în Microsoft Azure.

### Prezentare generală a atelierului

[Atelierul MCP Security Summit](https://azure-samples.github.io/sherpa/) oferă instruire practică și aplicabilă în securitate printr-o metodologie dovedită „vulnerabil → exploatat → reparat → validat”. Veți:

- **Învăța prin spargere**: Experimenta vulnerabilitățile direct, exploatând servere intenționat nesigure
- **Utiliza securitate nativă Azure**: Valorifica Azure Entra ID, Key Vault, API Management și AI Content Safety
- **Respecta apărarea în profunzime**: Progres prin tabere construind straturi cuprinzătoare de securitate
- **Aplica standardele OWASP**: Fiecare tehnică este corelată cu [Ghidul de securitate MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/)
- **Obține cod de producție**: Pleacă cu implementări funcționale și testate

### Traseul expediției

| Tabără | Focalizare | Riscuri OWASP abordate |
|------|-----------|---------------------|
| **Tabăra de bază** | Fundamente MCP & vulnerabilități autentificare | MCP01, MCP07 |
| **Tabăra 1: Identitate** | OAuth 2.1, Identitate gestionată Azure, Key Vault | MCP01, MCP02, MCP07 |
| **Tabăra 2: Gateway** | API Management, puncte finale private, guvernanță | MCP02, MCP06, MCP07, MCP09 |
| **Tabăra 3: Securitate I/O** | Injecția de prompt, protecția PII, siguranța conținutului | MCP03, MCP05, MCP06, MCP10 |
| **Tabăra 4: Monitorizare** | Log Analytics, dashboard-uri, detectarea amenințărilor | MCP04, MCP08 |
| **Summitul** | Test de integrare Red Team / Blue Team | Toate |

**Începe acum**: [https://azure-samples.github.io/sherpa/](https://azure-samples.github.io/sherpa/)

## Top 10 riscuri de securitate OWASP MCP

[Ghidul de securitate MCP Azure OWASP](https://microsoft.github.io/mcp-azure-security-guide/) detaliază zece cele mai critice riscuri de securitate pentru implementările MCP:

| Risc | Descriere | Măsuri de atenuare Azure |
|------|-----------|--------------------------|
| **MCP01** | Gestionare defectuoasă a token-urilor & expunerea secretelor | Azure Key Vault, Identitate gestionată |
| **MCP02** | Escaladare a privilegiilor prin extinderea domeniului | RBAC, Acces condiționat |
| **MCP03** | Otrăvirea instrumentului | Validarea instrumentului, verificarea integrității |
| **MCP04** | Atacuri ale lanțului de aprovizionare software & manipularea dependențelor | GitHub Advanced Security, scanare dependențe |
| **MCP05** | Injecție și execuție comenzi | Validarea intrărilor, izolarea (sandboxing) |
| **MCP06** | Subversiunea fluxului de intenție | Azure AI Content Safety, Prompt Shields |
| **MCP07** | Autentificare & autorizare insuficiente | Azure Entra ID, OAuth 2.1 cu PKCE |
| **MCP08** | Lipsa auditului și telemetriei | Azure Monitor, Application Insights |
| **MCP09** | Servere MCP fantomă | Guvernanță API Center, izolare rețea |
| **MCP10** | Injecția contextului & expunerea excesivă | Clasificarea datelor, expunere minimă |

### Evoluția autentificării MCP

Specificația MCP a evoluat semnificativ în abordarea autentificării și autorizării:

- **Abordarea inițială**: Specificațiile timpurii solicitau dezvoltatorilor să implementeze servere de autentificare personalizate, serverele MCP acționând ca Servere de autorizare OAuth 2.0 gestionând direct autentificarea utilizatorilor
- **Standardul actual (`2026-07-28`)**: Serverele MCP pot delega autentificarea
  către furnizori externi de identitate precum Microsoft Entra ID. Clienții trebuie să aplice și
  cerințele actuale de validare a emițătorului și asociere a acreditărilor.
- **Securitatea stratului de transport**: Suport îmbunătățit pentru mecanisme de transport securizate cu modele adecvate de autentificare, atât pentru conexiuni locale (STDIO), cât și la distanță (Streamable HTTP)

## Securitatea autentificării și autorizării

### Provocările curente de securitate

Implementările moderne MCP se confruntă cu mai multe provocări legate de autentificare și autorizare:

### Riscuri și vectori de amenințare

- **Logică de autorizare configurată greșit**: Implementarea defectuoasă a autorizării în serverele MCP poate expune date sensibile și aplica eronat controale de acces
- **Compromiterea token-urilor OAuth**: Furarea token-urilor serverului MCP local permite atacatorilor să se deghizeze în servere și să acceseze servicii în aval
- **Vulnerabilități la trecerea token-urilor**: Manipularea incorectă a token-urilor creează ocoliri ale controalelor de securitate și lacune în responsabilitate
- **Permisiuni excesive**: Serverele MCP cu privilegii prea largi încalcă principiile privilegiului minim și extind suprafețele de atac

#### Trecerea token-urilor: un antipattern critic

**Trecerea token-urilor este interzisă explicit** în specificația curentă de autorizare MCP datorită implicațiilor grave de securitate:

##### Ocolirea controalelor de securitate
- Serverele MCP și API-urile în aval implementează controale critice de securitate (limitarea ratei, validarea cererii, monitorizarea traficului) care depind de validarea corectă a token-ului
- Utilizarea directă a token-urilor client către API ocolește aceste protecții esențiale, subminând arhitectura de securitate

##### Probleme de responsabilitate și audit  
- Serverele MCP nu pot distinge între clienții care folosesc token-uri emise upstream, perturbând traseele de audit
- Jurnalele serverului resursă în aval arată origini eronate ale cererilor în locul intermedierii reale a serverelor MCP
- Investigarea incidentelor și auditul de conformitate devin mult mai dificile

##### Riscuri de exfiltrare a datelor
- Afirmările nevalidate din token-uri permit actorilor malițioși cu token-uri furate să utilizeze serverele MCP ca proxy pentru exfiltrarea datelor
- Încălcările graniței de încredere permit modele neautorizate de acces care ocolesc controalele de securitate intenționate

##### Vectori de atac multi-serviciu
- Token-urile compromise acceptate de mai multe servicii permit mișcări laterale între sisteme conectate
- Presupozițiile de încredere între servicii pot fi încălcate dacă originea token-urilor nu poate fi verificată

### Controale și mitigări de securitate

**Cerințe critice de securitate:**

> **OBLIGATORIU**: Serverele MCP **NU TREBUIE** să accepte token-uri care nu au fost emise explicit pentru serverul MCP

#### Controale de autentificare și autorizare

- **Revizuirea riguroasă a autorizării**: Realizați audituri comprehensive ale logicii de autorizare a serverului MCP pentru a asigura acces doar pentru utilizatorii și clienții intenționați la resurse sensibile
  - **Ghid de implementare**: [Azure API Management ca poartă de autentificare pentru serverele MCP](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
  - **Integrare identitate**: [Utilizarea Microsoft Entra ID pentru autentificarea serverului MCP](https://den.dev/blog/mcp-server-auth-entra-id-session/)

- **Gestionarea sigură a token-urilor**: Implementați [cele mai bune practici Microsoft pentru validarea token-urilor și ciclul lor de viață](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
  - Validați afirmațiile privind audiența token-ului pentru a corespunde identității serverului MCP
  - Implementați politici corespunzătoare de rotație și expirare a token-urilor
  - Preveniți atacurile de redare a token-urilor și utilizarea neautorizată

- **Stocare protejată a token-urilor**: Stocare sigură a token-urilor cu criptare atât la repaus, cât și în tranzit
  - **Cele mai bune practici**: [Ghid de stocare sigură și criptare a token-urilor](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

#### Implementarea controlului accesului

- **Principiul privilegiului minim**: Acordați serverelor MCP doar permisiunile minime necesare pentru funcționalitatea dorită
  - Revizuiri și actualizări regulate ale permisiunilor pentru a preveni extinderea privilegiilor
  - **Documentația Microsoft**: [Acces securizat cu privilegiu minim](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)

- **Controlul accesului bazat pe rol (RBAC)**: Implementați asignări de roluri detaliate
  - Restringeți rolurile strict la resurse și acțiuni specifice
  - Evitați permisiunile largi sau inutile care extind suprafețele de atac

- **Monitorizarea continuă a permisiunilor**: Implementați audit și monitorizare continuă a accesului
  - Monitorizați tiparele de utilizare a permisiunilor pentru anomalii
  - Remediați prompt privilegiile excesive sau neutilizate

## Amenințări specifice securității AI

### Atacuri cu injecție de prompt & manipulare a instrumentelor

Implementările moderne MCP se confruntă cu vectori de atac sofisticați specifici AI pe care măsurile tradiționale de securitate nu-i pot adresa complet:

#### **Injecția indirectă de prompt (Injecția de prompt cross-domain)**

**Injecția indirectă de prompt** reprezintă una dintre cele mai critice vulnerabilități în sistemele AI activate prin MCP. Atacatorii încorporează instrucțiuni malițioase în conținut extern — documente, pagini web, emailuri sau surse de date — pe care sistemele AI le procesează ulterior ca comenzi legitime.

**Scenarii de atac:**
- **Injecție bazată pe documente**: Instrucțiuni malițioase ascunse în documente procesate care declanșează acțiuni AI neintenționate
- **Exploatarea conținutului web**: Pagini web compromise care conțin prompturi încorporate ce manipulează comportamentul AI la extragere
- **Atacuri prin email**: Prompturi malițioase în emailuri ce determină asistenții AI să divulge informații sau să execute acțiuni neautorizate
- **Contaminarea surselor de date**: Baze de date sau API-uri compromise care oferă conținut contaminat către sistemele AI

**Impact în lumea reală**: Aceste atacuri pot conduce la exfiltrarea datelor, încălcări ale confidențialității, generarea de conținut dăunător și manipularea interacțiunilor utilizatorilor. Pentru o analiză detaliată, consultați [Injecția de prompt în MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/).

![Diagrama atacului de injecție de prompt](../../../translated_images/ro/prompt-injection.ed9fbfde297ca877.webp)

#### **Atacuri de otrăvire a instrumentelor**

**Otrăvirea instrumentelor** vizează metadatele care definesc instrumentele MCP, exploatând modul în care modelele LLM interpretează descrierile și parametrii instrumentelor pentru a lua decizii de execuție.

**Mecanisme de atac:**
- **Manipularea metadatelor**: Atacatorii injectează instrucțiuni malițioase în descrierile instrumentelor, definițiile parametrilor sau exemplele de utilizare
- **Instrucțiuni invizibile**: Prompturi ascunse în metadatele instrumentelor care sunt procesate de modelele AI, dar invizibile utilizatorilor umani
- **Modificarea dinamică a instrumentelor ("Rug Pulls")**: Instrumente aprobate de utilizatori sunt modificate ulterior pentru a executa acțiuni malițioase fără știrea utilizatorului
- **Injecția de parametri**: Conținut malițios încorporat în schemele parametrilor instrumentului care influențează comportamentul modelului


**Riscuri ale Serverelor Gazduite**: Serverele MCP la distanță prezintă riscuri ridicate deoarece definițiile instrumentelor pot fi actualizate după aprobarea inițială a utilizatorului, creând scenarii în care instrumentele anterior sigure devin malițioase. Pentru o analiză completă, consultați [Atacuri de intoxicare a instrumentelor (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).

![Diagramă atac de injectare a instrumentelor](../../../translated_images/ro/tool-injection.3b0b4a6b24de6bef.webp)

#### **Vectori suplimentari de atac AI**

- **Injectarea prompturilor cross-domain (XPIA)**: Atacuri sofisticate care folosesc conținut din mai multe domenii pentru a ocoli controalele de securitate
- **Modificarea dinamică a capacităților**: Schimbări în timp real ale capacităților instrumentelor care scapă evaluărilor inițiale de securitate
- **Intoxicarea ferestrei de context**: Atacuri care manipulează ferestre mari de context pentru a ascunde instrucțiuni malițioase
- **Atacuri de confuzie a modelului**: Exploatarea limitărilor modelului pentru a crea comportamente imprevizibile sau nesigure


### Impactul riscurilor de securitate AI

**Consecințe cu impact ridicat:**
- **Exfiltrarea datelor**: Acces neautorizat și furt de date sensibile ale întreprinderilor sau ale persoanelor
- **Încălcări ale intimității**: Expunerea informațiilor personale identificabile (PII) și a datelor de afaceri confidențiale  
- **Manipularea sistemelor**: Modificări neintenționate ale sistemelor și fluxurilor de lucru critice
- **Furt de acreditări**: Compromiterea tokenurilor de autentificare și a acreditărilor serviciilor
- **Mișcare laterală**: Folosirea sistemelor AI compromise ca puncte pivot pentru atacuri mai ample în rețea

### Soluții Microsoft pentru securitatea AI

#### **Scuturi AI Prompt: Protecție avansată împotriva atacurilor prin injectare**

Microsoft **AI Prompt Shields** oferă o apărare completă împotriva atacurilor directe și indirecte de injectare a prompturilor prin multiple straturi de securitate:

##### **Mecanisme principale de protecție:**

1. **Detectare și filtrare avansată**
   - Algoritmi de învățare automată și tehnici NLP detectează instrucțiuni malițioase în conținut extern
   - Analiză în timp real a documentelor, paginilor web, emailurilor și surselor de date pentru amenințări integrate
   - Înțelegere contextuală a tiparelor legitime vs. malițioase de prompturi

2. **Tehnici de evidențiere**  
   - Distinge între instrucțiunile de sistem de încredere și intrările externe potențial compromise
   - Metode de transformare a textului care sporesc relevanța modelului izolând în același timp conținutul malițios
   - Ajută sistemele AI să mențină o ierarhie corectă a instrucțiunilor și să ignore comenzile injectate

3. **Sisteme de delimitare și marcaj al datelor**
   - Definirea explicită a limitelor între mesajele de sistem de încredere și textul de intrare extern
   - Marcaje speciale evidențiază granițele între sursele de date de încredere și cele neîncredere
   - Separarea clară previne confuzia instrucțiunilor și executarea neautorizată a comenzilor

4. **Informații continue despre amenințări**
   - Microsoft monitorizează continuu modele emergente de atac și actualizează mecanismele de apărare
   - Căutare proactivă a amenințărilor pentru tehnici noi de injectare și vectori de atac
   - Actualizări regulate ale modelelor de securitate pentru a menține eficacitatea împotriva amenințărilor în evoluție

5. **Integrare Azure Content Safety**
   - Parte a suitei comprensive Azure AI Content Safety
   - Detectare suplimentară pentru tentative de jailbreak, conținut dăunător și încălcări ale politicilor de securitate
   - Controale de securitate unificate în toate componentele aplicațiilor AI

**Resurse de implementare**: [Documentația Microsoft Prompt Shields](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)

![Protecția Microsoft Prompt Shields](../../../translated_images/ro/prompt-shield.ff5b95be76e9c78c.webp)


## Amenințări avansate de securitate MCP

### Vulnerabilități la deturnarea sesiunilor

**Deturnarea sesiunii** reprezintă un vector critic de atac în implementările MCP cu stare, unde părțile neautorizate obțin și abuzează identificatori legitimi de sesiune pentru a se deghiza în clienți și a executa acțiuni neautorizate.

#### **Scenarii de atac și riscuri**

- **Injectare prompt de deturnare a sesiunii**: Atacatorii cu ID-uri de sesiune furate injectează evenimente malițioase în servere care împart starea sesiunii, declanșând potențial acțiuni dăunătoare sau acces la date sensibile
- **Impersonare directă**: ID-urile de sesiune furate permit apeluri directe către serverul MCP care ocolesc autentificarea, tratând atacatorii ca utilizatori legitimi
- **Fluxuri reluabile compromise**: Atacatorii pot încheia prematur cererile, cauzând reluarea de către clienții legitimi cu conținut potențial malițios

#### **Controale de securitate pentru gestionarea sesiunilor**

**Cerințe critice:**
- **Verificarea autorizării**: Serverele MCP care implementează autorizare **TREBUIE** să verifice TOATE cererile primite și **NU TREBUIE** să se bazeze pe sesiuni pentru autentificare
- **Generare securizată a sesiunilor**: Utilizați ID-uri de sesiune criptografic sigure, nedeterministe, generate cu generatoare sigure de numere aleatoare
- **Legarea specifică utilizatorului**: Leagați ID-urile sesiunilor la informații specifice utilizatorului folosind formate precum `<user_id>:<session_id>` pentru a preveni abuzul între utilizatori
- **Gestionarea ciclului de viață al sesiunii**: Implementați expirare, rotație și invalidare corectă pentru a limita ferestrele de vulnerabilitate
- **Securitatea transportului**: HTTPS obligatoriu pentru toate comunicațiile pentru a preveni interceptarea ID-urilor de sesiune

### Problema deputatului confuz

Problema **deputatului confuz** apare când serverele MCP acționează ca proxy-uri de autentificare între clienți și servicii terțe, creând oportunități pentru ocoliirea autorizării prin exploatarea ID-urilor client statice.

#### **Mecanici de atac și riscuri**

- **Ocolirea consimțământului bazat pe cookie-uri**: Autentificarea anterioară a utilizatorilor creează cookie-uri de consimțământ pe care atacatorii le exploatează prin cereri de autorizare malițioase cu URI-uri de redirecționare create
- **Furtul codului de autorizare**: Cookie-urile existente de consimțământ pot determina serverele de autorizare să evite ecranele de consimțământ, trimițând coduri către puncte de control controlate de atacatori  
- **Acces API neautorizat**: Codurile de autorizare furate permit schimb de tokenuri și impersonare fără aprobări explicite

#### **Strategii de mitigare**

**Controale obligatorii:**
- **Cerințe explicite de consimțământ**: Proxy-urile MCP care utilizează ID-uri client statice **TREBUIE** să obțină consimțământul utilizatorului pentru fiecare client înregistrat dinamic
- **Implementarea securității OAuth 2.1**: Urmați cele mai bune practici de securitate OAuth actuale, inclusiv PKCE (Proof Key for Code Exchange) pentru toate cererile de autorizare
- **Validare strictă a clientului**: Implementați o validare riguroasă a URI-urilor de redirecționare și a identificatorilor client pentru a preveni exploatarea

### Vulnerabilități la transmiterea tokenurilor  

**Transmiterea tokenurilor** reprezintă un anti-pattern explicit unde serverele MCP acceptă tokenuri client fără validare adecvată și le redirecționează către API-uri în aval, încălcând specificațiile de autorizare MCP.

#### **Implicări de securitate**

- **Ocolirea controalelor**: Utilizarea directă a tokenurilor client către API ocolește controalele critice de limitare a ratei, validare și monitorizare
- **Coruperea traseului de audit**: Tokenurile emise în sus fac imposibilă identificarea clientului, spargând capacitățile de investigare a incidentelor
- **Exfiltrarea datelor prin proxy**: Tokenurile nevalidate permit actorilor malițioși să folosească serverele ca proxy-uri pentru acces neautorizat la date
- **Încălcarea graniței de încredere**: Serviciile din aval pot vedea încălcări ale ipotezelor de încredere când originea tokenurilor nu poate fi verificată
- **Extinderea atacurilor multi-serviciu**: Tokenurile compromise acceptate în mai multe servicii permit mișcarea laterală

#### **Controale de securitate necesare**

**Cerințe de netrecut cu vederea:**
- **Validarea tokenurilor**: Serverele MCP **NU TREBUIE** să accepte tokenuri care nu sunt emise explicit pentru serverul MCP
- **Verificarea audienței**: Validați întotdeauna revendicările audienței tokenului pentru a corespunde identității serverului MCP
- **Ciclul de viață corect al tokenului**: Implementați tokenuri de acces cu durată scurtă și practici sigure de rotație


## Securitatea lanțului de aprovizionare pentru sistemele AI

Securitatea lanțului de aprovizionare a evoluat dincolo de dependențele tradiționale de software pentru a cuprinde întregul ecosistem AI. Implementările moderne MCP trebuie să verifice și să monitorizeze riguros toate componentele legate de AI, deoarece fiecare introduce vulnerabilități potențiale ce pot compromite integritatea sistemului.

### Componente extinse ale lanțului de aprovizionare AI

**Dependențe tradiționale de software:**
- Biblioteci și cadre open-source
- Imagini container și sisteme de bază  
- Instrumente de dezvoltare și pipeline-uri de construire
- Componente și servicii de infrastructură

**Elemente specifice lanțului de aprovizionare AI:**
- **Modele fundamentale**: Modele pre-antrenate de la diverși furnizori ce necesită verificarea provenienței
- **Servicii de embedding**: Servicii externe de vectorizare și căutare semantică
- **Furnizori de context**: Surse de date, baze de cunoștințe și depozite de documente  
- **API-uri terțe**: Servicii AI externe, pipeline-uri ML și puncte finale de procesare a datelor
- **Artefacte ale modelului**: Greutăți, configurații și variante de model fine-tunate
- **Surse de date pentru antrenament**: Seturi de date folosite pentru antrenarea și fine-tuning-ul modelului

### Strategie cuprinzătoare pentru securitatea lanțului de aprovizionare

#### **Verificarea și încrederea componentelor**
- **Validarea provenienței**: Verificați originea, licențierea și integritatea tuturor componentelor AI înainte de integrare
- **Evaluarea securității**: Efectuați scanări de vulnerabilități și revizuiri de securitate pentru modele, surse de date și servicii AI
- **Analiza reputației**: Evaluați istoricul de securitate și practicile furnizorilor de servicii AI
- **Verificarea conformității**: Asigurați-vă că toate componentele respectă cerințele de securitate și reglementare ale organizației

#### **Pipeline-uri de implementare securizate**  
- **Securitate CI/CD automatizată**: Integrați scanări de securitate în întregul pipeline automatizat de implementare
- **Integritatea artefactelor**: Implementați verificarea criptografică pentru toate artefactele implementate (cod, modele, configurații)
- **Implementare etapizată**: Folosiți strategii progresive de implementare cu validare de securitate la fiecare etapă
- **Depozite de artefacte de încredere**: Implementați doar din registre și depozite de artefacte verificate și securizate

#### **Monitorizare și răspuns continuu**
- **Scanare de dependențe**: Monitorizarea continuă a vulnerabilităților pentru toate dependențele software și componente AI
- **Monitorizarea modelelor**: Evaluare continuă a comportamentului modelului, deriva performanței și anomaliilor de securitate
- **Urmărirea sănătății serviciilor**: Monitorizați serviciile AI externe pentru disponibilitate, incidente de securitate și schimbări de politică
- **Integrarea informațiilor despre amenințări**: Includeți fluxuri de amenințări specifice riscurilor de securitate AI și ML

#### **Controlul accesului și principiul privilegiului minim**
- **Permisiuni la nivel de componentă**: Restricționați accesul la modele, date și servicii pe baza necesității de afaceri
- **Gestionarea conturilor de serviciu**: Implementați conturi de serviciu dedicate cu permisiuni minime necesare
- **Segmentarea rețelei**: Izolați componentele AI și limitați accesul rețelei între servicii
- **Controale ale API Gateway**: Folosiți gateway-uri API centralizate pentru a controla și monitoriza accesul la serviciile externe AI

#### **Răspuns și recuperare în caz de incident**
- **Proceduri rapide de răspuns**: Procese stabilite pentru patch-uri sau înlocuiri ale componentelor AI compromise
- **Rotația acreditărilor**: Sisteme automatizate pentru rotirea secretelor, cheilor API și acreditărilor serviciilor
- **Capabilități de revenire**: Capacitatea de a reveni rapid la versiuni anterioare cunoscute ca fiind bune ale componentelor AI
- **Recuperare după încălcarea lanțului de aprovizionare**: Proceduri specifice pentru răspuns în cazul compromisurilor serviciilor AI din amonte

### Unelte și integrare Microsoft pentru securitate

**GitHub Advanced Security** oferă protecție cuprinzătoare a lanțului de aprovizionare, inclusiv:
- **Scanarea secretelor**: Detectarea automată a acreditărilor, cheilor API și tokenurilor în depozite
- **Scanarea dependențelor**: Evaluarea vulnerabilităților pentru dependențele și bibliotecile open-source
- **Analiza CodeQL**: Analiză statică a codului pentru vulnerabilități de securitate și probleme de codare
- **Informații asupra lanțului de aprovizionare**: Vizibilitate asupra stării de sănătate și securitate a dependențelor

**Integrare Azure DevOps & Azure Repos:**
- Integrare perfectă a scanării de securitate în platformele Microsoft de dezvoltare
- Verificări automate de securitate în Azure Pipelines pentru sarcini de lucru AI
- Aplicarea politicilor pentru implementarea sigură a componentelor AI

**Practici interne Microsoft:**
Microsoft implementează practici extinse de securitate a lanțului de aprovizionare în toate produsele. Aflați despre abordările dovedite în [Călătoria spre securizarea lanțului de aprovizionare software la Microsoft](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/).


## Cele mai bune practici de securitate fundamentale

Implementările MCP moștenesc și construiesc peste postura de securitate existentă a organizației dvs. Consolidarea practicilor de securitate fundamentale îmbunătățește semnificativ securitatea generală a sistemelor AI și a implementărilor MCP.

### Fundamente de securitate esențiale

#### **Practici de dezvoltare securizată**
- **Respectarea OWASP**: Protejați împotriva vulnerabilităților web din [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- **Proprietăți specifice AI**: Implementați controale pentru [OWASP Top 10 pentru LLM-uri](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- **Gestionarea sigură a secretelor**: Folosiți seifuri dedicate pentru tokenuri, chei API și date sensibile de configurare
- **Criptare end-to-end**: Implementați comunicații securizate în toate componentele aplicațiilor și fluxurile de date
- **Validarea inputului**: Validare riguroasă a tuturor intrărilor utilizatorilor, parametrilor API și surselor de date

#### **Întărirea infrastructurii**
- **Autentificare multifactor**: MFA obligatorie pentru toate conturile administrative și de serviciu
- **Gestionarea patch-urilor**: Aplicare automată și în timp util a patch-urilor pentru sisteme de operare, cadre și dependențe  
- **Integrarea furnizorului de identitate**: Administrare centralizată a identității prin furnizori de identitate enterprise (Microsoft Entra ID, Active Directory)
- **Segmentarea rețelei**: Izolare logică a componentelor MCP pentru limitarea potențialului de mișcare laterală
- **Principiul privilegiului minim**: Permisiuni minime necesare pentru toate componentele și conturile sistemelor

#### **Monitorizare și detectare a securității**
- **Jurnalizare cuprinzătoare**: Logare detaliată a activităților aplicațiilor AI, inclusiv a interacțiunilor client-server MCP
- **Integrarea SIEM**: Management centralizat al informațiilor și evenimentelor de securitate pentru detectarea anomaliilor
- **Analitică comportamentală**: Monitorizare alimentată de AI pentru detectarea tiparelor neobișnuite în comportamentul sistemului și utilizatorilor
- **Informații despre amenințări**: Integrarea fluxurilor externe de amenințări și indicatori de compromitere (IOCs)
- **Răspuns la incidente**: Proceduri bine definite pentru detectarea, răspunsul și recuperarea post-incident de securitate

#### **Arhitectura Zero Trust**
- **Nu avea niciodată încredere, verifică mereu**: Verificare continuă a utilizatorilor, dispozitivelor și conexiunilor de rețea
- **Micro-segmentare**: Controale granulate de rețea care izolează sarcinile și serviciile individuale
- **Securitate centrată pe identitate**: Politici de securitate bazate pe identități verificate, nu pe locația în rețea
- **Evaluare continuă a riscurilor**: Evaluare dinamică a posturii de securitate în funcție de contextul și comportamentul curent
- **Acces condiționat**: Controale de acces care se adaptează pe baza factorilor de risc, locației și încrederii în dispozitiv

### Modele de integrare în mediul enterprise

#### **Integrarea ecosistemului Microsoft Security**
- **Microsoft Defender for Cloud**: Management cuprinzător al posturii de securitate cloud
- **Azure Sentinel**: Capacități native cloud SIEM și SOAR pentru protecția sarcinilor de lucru AI
- **Microsoft Entra ID**: Management enterprise al identității și accesului cu politici de acces condiționat
- **Azure Key Vault**: Gestionare centralizată a secretelor cu modul hardware de securitate (HSM)
- **Microsoft Purview**: Guvernanță și conformitate pentru sursele de date și fluxurile de lucru AI

#### **Conformitate și guvernanță**
- **Aliniere la reglementări**: Asigurați-vă că implementările MCP respectă cerințele de conformitate specifice industriei (GDPR, HIPAA, SOC 2)

- **Clasificarea datelor**: Categorisirea și gestionarea corectă a datelor sensibile procesate de sistemele AI
- **Jurnale de audit**: Înregistrare cuprinzătoare pentru conformitate reglementară și investigații criminalistice
- **Controale de confidențialitate**: Implementarea principiilor de confidențialitate-by-design în arhitectura sistemelor AI
- **Gestionarea schimbărilor**: Procese formale pentru revizuirea securității modificărilor sistemelor AI

Aceste practici fundamentale creează o bază solidă de securitate care îmbunătățește eficacitatea controalelor de securitate specifice MCP și oferă protecție cuprinzătoare aplicațiilor alimentate de AI.

## Aspecte cheie privind securitatea

- **Abordare stratificată a securității**: Combină practici fundamentale de securitate (codare sigură, privilegiul minim, verificarea lanțului de aprovizionare, monitorizare continuă) cu controale specifice AI pentru protecție completă

- **Peisajul amenințărilor specifice AI**: Sistemele MCP se confruntă cu riscuri unice inclusiv injectarea de prompturi, otrăvirea uneltelor, deturnarea sesiunilor, problemele delegate confuze, vulnerabilitățile de transmitere a tokenurilor și permisiunile excesive care necesită măsuri specializate

- **Excelență în autentificare și autorizare**: Implementează autentificare robustă folosind furnizori externi de identitate (Microsoft Entra ID), aplică validarea corectă a tokenurilor și nu accepta niciodată tokenuri care nu sunt emise explicit pentru serverul tău MCP

- **Prevenirea atacurilor AI**: Folosește Microsoft Prompt Shields și Azure Content Safety pentru a apăra împotriva injecției indirecte de prompturi și atacurilor de otrăvire a uneltelor, în timp ce validezi metadatele uneltelor și monitorizezi schimbările dinamice

- **Securitatea sesiunilor și transportului**: Utilizează ID-uri de sesiune criptografic securizate, nedeterministe, legate de identitățile utilizatorilor, implementează gestionarea corectă a ciclului de viață al sesiunii și nu folosi niciodată sesiuni pentru autentificare

- **Cele mai bune practici de securitate OAuth**: Previne atacurile delegate confuze prin consimțământ explicit al utilizatorului pentru clienții înregistrați dinamic, implementarea corectă a OAuth 2.1 cu PKCE și validarea strictă a URI-urilor de redirecționare  

- **Principii de securitate pentru tokenuri**: Evită antipattern-urile de transmitere a tokenurilor, validează revendicările de audiență ale tokenului, implementează tokenuri cu durată scurtă și rotație securizată și menține limite clare de încredere

- **Securitate cuprinzătoare a lanțului de aprovizionare**: Tratează toate componentele ecosistemului AI (modele, încorporări, furnizori de context, API-uri externe) cu același nivel riguros de securitate ca și dependențele software tradiționale

- **Evoluție continuă**: Fii la curent cu specificațiile MCP în continuă evoluție rapidă, contribuie la standardele comunității de securitate și menține posturi adaptive de securitate pe măsură ce protocolul avansează

- **Integrarea securității Microsoft**: Profită de ecosistemul cuprinzător de securitate Microsoft (Prompt Shields, Azure Content Safety, GitHub Advanced Security, Entra ID) pentru protecția îmbunătățită a implementărilor MCP

## Resurse cuprinzătoare

### **Documentația oficială de securitate MCP**
- [MCP Specification (Current: 2026-07-28)](https://modelcontextprotocol.io/specification/2026-07-28/)
- [MCP Security Best Practices](https://modelcontextprotocol.io/specification/2026-07-28/basic/security_best_practices)
- [MCP Authorization Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)

### **Resursele OWASP MCP pentru securitate**
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/) - OWASP MCP Top 10 detaliat cu ghid de implementare pe Azure
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) - Riscurile oficiale de securitate OWASP MCP
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) - Training practic de securitate pentru MCP pe Azure

### **Standarde de securitate și cele mai bune practici**
- [OAuth 2.0 Security Best Practices (RFC 9700)](https://datatracker.ietf.org/doc/html/rfc9700)
- [OWASP Top 10 Web Application Security](https://owasp.org/www-project-top-ten/)
- [OWASP Top 10 for Large Language Models](https://genai.owasp.org/download/43299/?tmstv=1731900559)
- [Microsoft Digital Defense Report](https://aka.ms/mddr)

### **Cercetare și analiză în securitatea AI**
- [Prompt Injection in MCP (Simon Willison)](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)
- [Tool Poisoning Attacks (Invariant Labs)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks)
- [MCP Security Research Briefing (Wiz Security)](https://www.wiz.io/blog/mcp-security-research-briefing#remote-servers-22)

### **Soluții de securitate Microsoft**
- [Microsoft Prompt Shields Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection)
- [Azure Content Safety Service](https://learn.microsoft.com/azure/ai-services/content-safety/)
- [Microsoft Entra ID Security](https://learn.microsoft.com/entra/identity-platform/secure-least-privileged-access)
- [Azure Token Management Best Practices](https://learn.microsoft.com/entra/identity-platform/access-tokens)
- [GitHub Advanced Security](https://github.com/security/advanced-security)

### **Ghiduri de implementare și tutoriale**
- [Azure API Management as MCP Authentication Gateway](https://techcommunity.microsoft.com/blog/integrationsonazureblog/azure-api-management-your-auth-gateway-for-mcp-servers/4402690)
- [Microsoft Entra ID Authentication with MCP Servers](https://den.dev/blog/mcp-server-auth-entra-id-session/)
- [Secure Token Storage and Encryption (Video)](https://youtu.be/uRdX37EcCwg?si=6fSChs1G4glwXRy2)

### **DevOps și securitatea lanțului de aprovizionare**
- [Azure DevOps Security](https://azure.microsoft.com/products/devops)
- [Azure Repos Security](https://azure.microsoft.com/products/devops/repos/)
- [Microsoft Supply Chain Security Journey](https://devblogs.microsoft.com/engineering-at-microsoft/the-journey-to-secure-the-software-supply-chain-at-microsoft/)

## **Documentație suplimentară de securitate**

Pentru ghidare de securitate cuprinzătoare, consultă aceste documente specializate din această secțiune:

- **[CIMD and DCR Authorization Sample](./samples/cimd-dcr-auth/README.md)** - Server resursă MCP `2026-07-28` în TypeScript, executabil, comparând documentele preferate Client ID Metadata cu fallback-ul înregistrării dinamice a clientului
- **[MCP Security Best Practices](./mcp-security-best-practices.md)** - Cele mai complete practici de securitate pentru implementările MCP
- **[Azure Content Safety Implementation](./azure-content-safety-implementation.md)** - Exemple practice de implementare pentru integrarea Azure Content Safety  
- **[MCP Security Controls](./mcp-security-controls.md)** - Cele mai recente controale și tehnici de securitate pentru implementările MCP
- **[MCP Best Practices Quick Reference](./mcp-best-practices.md)** - Ghid rapid de referință pentru practicile esențiale de securitate MCP
- **[BlueHat 2026: Securing the future of AI: Securing MCP with defense in depth patterns](https://www.youtube.com/watch?v=cVWB58kEt-Y)** - Modele de apărare în profunzime de la Microsoft Security Response Center (MSRC)

### **Training practic de securitate**

- **[MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)** - Atelier practic complet pentru securizarea serverelor MCP pe Azure cu tabere progresive de la Base Camp la Summit
- **[OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)** - Arhitectură de referință și ghid de implementare pentru toate riscurile OWASP MCP Top 10

---

## Ce urmează

Următorul: [Capitolul 3: Începem](../03-GettingStarted/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->