# Changelog: Curriculum MCP pentru Începători

Acest document servește ca un registru al tuturor modificărilor semnificative făcute curriculumului Model Context Protocol (MCP) pentru Începători. Modificările sunt documentate în ordine cronologică inversă (cele mai noi modificări primele).

## 11 aprilie 2026

### Lecție Nouă, Corecturi în Documentație și Actualizări de Dependențe

#### Conținut Nou Adăugat în Curriculum

**Modul 05 - Subiecte Avansate**  
- **Lecția 5.17: Raționamentul Multi-Agent Adversarial cu MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ghid cuprinzător nou despre pattern-ul de dezbatere adversarială pentru sisteme multi-agent
  - Diagramă de arhitectură Mermaid: doi agenți → server MCP partajat → transcrierea dezbaterii → judecător → verdict  
  - Server de unelte MCP partajate (`web_search` + `run_python`) implementat în Python și TypeScript  
  - Prompturi sistem opozante (PENTRU / ÎMPOTRIVĂ / Judecător) cu cerințe explicite de utilizare a uneltelor  
  - Orchestrator pentru dezbateri în Python, TypeScript și C#, care gestionează runde și rutarea argumentelor  
  - Conectare MCP `ClientSession` pentru orchestrator la apelurile reale ale uneltei  
  - Tabel de cazuri de utilizare (detecția halucinațiilor, modelare de amenințări, revizuirea design-ului API, verificare factuală, selecția tehnologică)  
  - Considerații de securitate: execuție sandboxată, validarea apelurilor unelte, limitare de rată, jurnalizare pentru audit  
  - Exercițiu structurat cu trei scenarii practice (revizuirea codului, decizie arhitecturală, moderare de conținut)  

#### Corecturi de Documentație

**Modul 03 - Început**  
- **05-stdio-server/README.md**: Corectat exemplul incomplet TypeScript pentru server stdio — adăugat instanțierea lipsă a transportului (`new StdioServerTransport()`) și apelul `server.connect(transport)` pentru a corespunde cu exemplele Python și .NET din aceeași secțiune  
- **14-sampling/README.md**: Corectată greșeală tipografică — corectat `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`  

#### Actualizări Curriculum

**README.md Principal**  
- Adăugat intrarea 5.17 (Raționamentul Multi-Agent Adversarial cu MCP) în tabelul curriculumului cu link direct către lecția nouă

**05-AdvancedTopics/README.md**  
- Adăugat rând Lecția 5.17 în tabelul lecțiilor  

**study_guide.md**  
- Adăugat subiectul Raționament Multi-Agent Adversarial în harta mentală și descrierea în text a Subiectelor Avansate  

#### Corecturi de Cod și Securitate

**Modul 05 - Agenți Adversariale (`mcp-adversarial-agents`)**  
- **Corectură securitate — injectare comandă**: Înlocuită interpolarea shell `execSync` cu `execFile` + `promisify` în unealta TypeScript `run_python`, eliminând suprafața de injecție comandă (codul controlat de LLM este acum transmis literal ca element argv fără implicarea shell-ului)  
- **Conectare ciclu unealtă MCP**: Actualizat orchestratorul Python al dezbaterii să folosească clientul `AsyncAnthropic` (înlocuind blocantul sincron `Anthropic`), să transmită `ClientSession` live direct fiecărei runde de agent, să preia definițiile uneltelor prin `session.list_tools()` la fiecare rundă, și să dispună blocurile `tool_use` prin `session.call_tool()` într-un ciclu până când modelul emite un răspuns final text  

#### Actualizări de Dependențe

- Actualizat `hono` la versiunea 4.12.12 în mai multe pachete (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)  
- Actualizat `@hono/node-server` de la 1.19.11 la 1.19.13 în pachetele TypeScript  
- Actualizat `cryptography` de la 46.0.5 la 46.0.7 în pachetele Python (laboratoarele 3 și 4 din 10-StreamliningAIWorkflows)  
- Actualizat `lodash` de la 4.17.23 la 4.18.1 în inspectorul 10-StreamliningAIWorkflows  

#### Traduceri

- Sincronizate traducerile pentru peste 48 de limbi cu ultimele modificări sursă (actualizare i18n)  

---

## 5 februarie 2026

### Validare și îmbunătățiri de navigare la nivel de repository

#### Conținut Nou Adăugat în Curriculum

**Modul 03 - Început**  
- **12-mcp-hosts/README.md**: Ghid cuprinzător nou pentru configurarea gazdelor MCP  
  - Exemple de configurare pentru Claude Desktop, VS Code, Cursor, Cline, Windsurf  
  - Șabloane JSON de configurare pentru toate gazdele majore  
  - Tabel comparativ al tipurilor de transport (stdio, SSE/HTTP, WebSocket)  
  - Depanarea problemelor comune de conectare  
  - Cele mai bune practici de securitate pentru configurarea gazdelor  

- **13-mcp-inspector/README.md**: Ghid nou de depanare pentru MCP Inspector  
  - Metode de instalare (npx, npm global, din sursă)  
  - Conectarea la servere prin stdio și HTTP/SSE  
  - Testarea uneltelor, resurselor și fluxurilor de prompturi  
  - Integrare VS Code cu MCP Inspector  
  - Scenarii comune de depanare cu soluții  

**Modul 04 - Implementare Practică**  
- **pagination/README.md**: Ghid nou de implementare a paginării  
  - Pattern-uri de paginare bazate pe cursor în Python, TypeScript, Java  
  - Gestionarea paginării pe client  
  - Strategii de proiectare a cursorilor (opac vs. structurat)  
  - Recomandări pentru optimizarea performanței  

**Modul 05 - Subiecte Avansate**  
- **mcp-protocol-features/README.md**: Analiză aprofundată a funcțiilor protocolului  
  - Implementarea notificărilor de progres  
  - Modele de anulare a cererilor  
  - Șabloane de resurse cu modele URI  
  - Managementul ciclului de viață al serverului  
  - Controlul nivelului de jurnalizare  
  - Modele de tratare a erorilor cu coduri JSON-RPC  

#### Corecturi de Navigare (peste 24 de fișiere actualizate)

**READMEs principale de modul**  
- Acum conțin link atât spre prima lecție, cât și spre modulul următor  

**Sub-fișiere 02-Security**  
- Toate cele 5 documente suplimentare de securitate au acum navigare „Ce Urmează”  

**Fișiere 09-CaseStudy**  
- Toate fișierele de studii de caz au acum navigare secvențială  

**Laboratoare 10-StreamliningAI**  
- Adăugat secțiunea Ce Urmează în prezentarea Modulului 10 și Modulului 11  

#### Corecturi de Cod și Conținut

**Actualizări SDK și Dependențe**  
- Corectat versiunea goală openai la `^4.95.0`  
- Actualizat SDK de la `^1.8.0` la `>=1.26.0`  
- Actualizat versiunile MCP la `>=1.26.0`  

**Corecturi de Cod**  
- Corectat model invalid `gpt-4o-mini` la `gpt-4.1-mini`  

**Corecturi de Conținut**  
- Corectat link spart `READMEmd` → `README.md`, corectat antet curriculum `Module 1-3` → `Module 0-3`, corectat cale cu sensibilitate la majuscule  
- Eliminat conținut duplicat corupt din Studiul de Caz 5  

**Îmbunătățiri pentru Începători**  
- Adăugate introducere adecvată, obiective de învățare și prerechizite pentru începători  

#### Actualizări Curriculum

**README.md Principal**  
- Adăugate intrările 3.12 (Gazdele MCP), 3.13 (MCP Inspector), 4.1 (Paginare), 5.16 (Funcții Protocol) în tabelul curriculumului  

**READMEs de Modul**  
- Adăugate lecțiile 12 și 13 în lista lecțiilor  
- Adăugată secțiunea Ghiduri Practice cu link pentru paginare  
- Adăugate lecțiile 5.15 (Transport Personalizat) și 5.16 (Funcții Protocol)  

**study_guide.md**  
- Actualizată harta mentală cu toate subiectele noi: Configurare Gazde MCP, MCP Inspector, Strategii de Paginare, Analiză Funcții Protocol  

## 28 ianuarie 2026

### Revizuire de Conformitate MCP Specificația 2025-11-25

#### Îmbunătățiri Concepte de Bază (01-CoreConcepts/)  
- **Primitiv Client Nou - Roots**: Documentație cuprinzătoare despre primitivul de client Roots, care permite serverelor să înțeleagă limitele sistemului de fișiere și permisiunile de acces  
- **Anotări Unealtă**: Documentație despre anotările comportamentale ale uneltelor (`readOnlyHint`, `destructiveHint`) pentru decizii mai bune de execuție a uneltelor  
- **Apelul Unealtelor în Sampling**: Documentația Sampling actualizată pentru a include parametrii `tools` și `toolChoice` pentru invocarea uneltelor controlată de model în cererile de sampling  
- **Elicitarea în Mod URL**: Documentație despre elicitarea bazată pe URL pentru interacțiuni web externe inițiate de server  
- **Sarcini (Experimental)**: Secțiune nouă documentând funcționalitatea experimentală de Sarcini pentru înfășurări durabile de execuție și recuperare amânată a rezultatelor  
- **Suport pentru Iconițe**: Notificat că uneltele, resursele, șabloanele de resurse și prompturile pot include acum iconițe ca metadate suplimentare  

#### Actualizări Documentație  
- **README.md**: Adăugat referința versiunii MCP Specificația 2025-11-25 și explicația versionării bazate pe dată  
- **study_guide.md**: Actualizată harta curriculumului pentru a include Sarcini și Anotări Unealtă în secțiunea Concepte de Bază; actualizat timestamp-ul documentului  

#### Verificarea Conformității Specificației  
- **Versiunea Protocolului**: Verificat că întreaga documentație face referire la actuala Specificație MCP 2025-11-25  
- **Alinierea Arhitecturii**: Confirmată exactitatea documentației arhitecturii în două straturi (Stratul de Date + Stratul de Transport)  
- **Documentația Primitivelor**: Validat primitivii server (Resurse, Prompturi, Unelte) și client (Sampling, Elicitare, Jurnalizare, Roots)  
- **Mecanisme de Transport**: Verificat corectitudinea documentației transportului STDIO și HTTP Streamabil  
- **Ghid de Securitate**: Confirmată alinierea cu cele mai noi Practici de Securitate MCP  

#### Funcționalități Cheie MCP 2025-11-25 Documentate  
- **Descoperirea OpenID Connect**: Descoperire server de autentificare prin OIDC  
- **Documente Metadate OAuth Client ID**: Mecanism recomandat de înregistrare client  
- **JSON Schema 2020-12**: Dialect implicit pentru definiții schema MCP  
- **Sistem de Nivelare SDK**: Cerințe formalizate pentru suport și mentenanță funcții SDK  
- **Structura Guvernanței**: Grupuri de lucru și grupuri de interes formalizate în guvernanța MCP  

### Actualizare Majoră Documentație Securitate (02-Security/)

#### Integrarea Workshop-ului MCP Security Summit (Sherpa)  
- **Resursă nouă de instruire practică**: Adăugată integrare cuprinzătoare cu [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) în toate documentele de securitate  
- **Acoperirea traseului expediției**: Documentat parcursul complet de la tabăra de bază la vârf  
- **Aliniere OWASP**: Toate ghidurile de securitate corespunzător mapate riscurilor OWASP MCP Azure Security Guide  

#### Integrarea OWASP MCP Top 10  
- **Secțiune nouă**: Adăugat tabelul riscurilor de securitate OWASP MCP Top 10 cu atenuări Azure în README-ul principal de securitate  
- **Documentație bazată pe risc**: Actualizat mcp-security-controls-2025.md cu referințe riscuri OWASP MCP pentru fiecare domeniu de securitate  
- **Arhitectură de referință**: Legat la arhitectura de referință OWASP MCP Azure Security Guide și pattern-uri de implementare  

#### Fișiere Securitate Actualizate  
- **README.md**: Adăugat prezentarea workshop-ului Sherpa, tabela traseului expediției, rezumat riscuri OWASP MCP Top 10 și secțiune de instruire practică  
- **mcp-security-controls-2025.md**: Antet actualizat la februarie 2026, adăugate referințe riscuri OWASP MCP (MCP01-MCP08), corectată inconsistență versiune specificație  
- **mcp-security-best-practices-2025.md**: Secțiune resurse Sherpa și OWASP adăugată, timestamp actualizat  
- **mcp-best-practices.md**: Secțiune instruire practică cu link-uri Sherpa și OWASP adăugate  
- **azure-content-safety-implementation.md**: Referință OWASP MCP06, aliniere Sherpa Tabără 3 și secțiune resurse suplimentare  

#### Linkuri Resurse Noi Adăugate  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)  
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)  
- Pagini individuale ale riscurilor OWASP MCP (MCP01-MCP10)  

### Alinierea Curriculumului cu MCP Specificația 2025-11-25

#### Modul 03 - Început  
- **Documentație SDK**: Adăugat Go SDK în lista oficială SDK; actualizate toate referințele SDK pentru conformitate cu MCP Specification 2025-11-25  
- **Clarificare Transport**: Actualizate descrierile transport STDIO și HTTP Streaming cu referințe specifice explicite  

#### Modul 04 - Implementare Practică  
- **Actualizări SDK**: Adăugat Go SDK; actualizată lista SDK cu referință la versiunea specificației  
- **Specificația Autorizației**: Actualizat linkul specificației MCP Autorizație la versiunea curentă 2025-11-25  

#### Modul 05 - Subiecte Avansate  
- **Funcționalități Noi**: Adăugată notă privind noile funcții MCP Specification 2025-11-25 (Sarcini, Anotări Unealtă, Elicitarea Mod URL, Roots)  
- **Resurse Securitate**: Adăugat link-uri OWASP MCP Top 10 și workshop Sherpa în referințe suplimentare  

#### Modul 06 - Contribuții Comunitare  
- **Listă SDK**: Adăugat SDK-uri Swift și Rust; actualizat link-ul specificației la 2025-11-25  
- **Referință Spec**: Actualizat link-ul spre specificația directă MCP  

#### Modul 07 - Lecții din Adoptarea Timpurie  
- **Actualizări Resurse**: Adăugat link MCP Specification 2025-11-25 și OWASP MCP Top 10 în resurse suplimentare  

#### Modul 08 - Cele Mai Bune Practici  
- **Versiune Spec**: Actualizat referința MCP Specification la 2025-11-25  
- **Resurse Securitate**: Adăugat OWASP MCP Top 10 și workshop Sherpa în referințe suplimentare  

#### Modul 10 - Optimizarea Fluxurilor AI  
- **Actualizare Insignă**: Schimbat insigna versiune MCP de la versiunea SDK (1.9.3) la versiunea specificației (2025-11-25)  
- **Link-uri Resurse**: Actualizat link MCP Specification; adăugat OWASP MCP Top 10  

#### Modul 11 - Laboratoare Practice MCP Server  
- **Referință Spec**: Actualizat link MCP Specification la versiunea 2025-11-25  
- **Resurse Securitate**: Adăugat OWASP MCP Top 10 în resurse oficiale  

## 18 decembrie 2025
### Actualizare Documentație Securitate - Specificația MCP 2025-11-25

#### Practici Recomandate de Securitate MCP (02-Security/mcp-best-practices.md) - Actualizare Versiune Specificație
- **Actualizare Versiune Protocol**: Actualizat pentru a face referire la cea mai recentă Specificație MCP 2025-11-25 (lansată pe 25 noiembrie 2025)
  - Actualizate toate referințele la versiunea specificației de la 2025-06-18 la 2025-11-25
  - Actualizate referințele la datele documentelor de la 18 august 2025 la 18 decembrie 2025
  - Verificat ca toate URL-urile specificației să pointeze către documentația curentă
- **Validarea Conținutului**: Validare completă a celor mai bune practici de securitate conform celor mai recente standarde
  - **Soluții de Securitate Microsoft**: Verificată terminologia și link-urile curente pentru Prompt Shields (anterior „Detectarea riscului Jailbreak”), Azure Content Safety, Microsoft Entra ID, și Azure Key Vault
  - **Securitate OAuth 2.1**: Confirmată alinierea la cele mai recente practici recomandate de securitate OAuth
  - **Standardele OWASP**: Validare că referințele OWASP Top 10 pentru LLM-uri rămân actuale
  - **Servicii Azure**: Verificate toate link-urile documentației Microsoft Azure și cele mai bune practici
- **Alinierea la Standardele**: Confirmate toate standardele de securitate referențiate ca fiind curente
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Best Practices Securitate OAuth 2.1
  - Framework-uri de securitate și conformitate Azure
- **Resurse de Implementare**: Validat toate link-urile și resursele din ghidurile de implementare
  - Modele de autentificare Azure API Management
  - Ghiduri de integrare Microsoft Entra ID
  - Gestionarea secretelor Azure Key Vault
  - Pipeline-uri și soluții de monitorizare DevSecOps

### Asigurarea Calității Documentației
- **Conformitate cu Specificația**: Asigurate toate cerințele obligatorii de securitate MCP (TREBUIE / NU TREBUIE) aliniate la cea mai recentă specificație
- **Actualitatea Resurselor**: Verificat ca toate link-urile externe către documentația Microsoft, standardele de securitate și ghidurile de implementare să fie actuale
- **Acoperire a celor Mai Bune Practici**: Confirmată acoperirea completă a autentificării, autorizării, amenințărilor specifice AI, securității lanțului de aprovizionare și modelelor enterprise

## 6 octombrie 2025

### Extinderea Secțiunii „Începeți” – Utilizare Avansată a Serverului & Autentificare Simplă

#### Utilizare Avansată a Serverului (03-GettingStarted/10-advanced)
- **Capitol Nou Adăugat**: Ghid complet pentru utilizarea avansată a serverului MCP, acoperind arhitecturi atât regulate, cât și de nivel jos.
  - **Server Regulat vs. Nivel Jos**: Comparație detaliată și exemple de cod în Python și TypeScript pentru ambele abordări.
  - **Design Bazat pe Handler**: Explicație privind managementul instrumentelor/resurselor/Prompturilor bazate pe handler pentru implementări de server scalabile și flexibile.
  - **Modele Practice**: Scenarii din viața reală unde modelele pentru server de nivel jos sunt benefice pentru caracteristici avansate și arhitectură.

#### Autentificare Simplă (03-GettingStarted/11-simple-auth)
- **Capitol Nou Adăugat**: Ghid pas cu pas pentru implementarea autentificării simple în serverele MCP.
  - **Concepte de Autentificare**: Explicație clară a autentificării vs. autorizării și gestionarea acreditărilor.
  - **Implementare Basic Auth**: Modele de autentificare bazate pe middleware în Python (Starlette) și TypeScript (Express), cu exemple de cod.
  - **Progresie către Securitate Avansată**: Orientări pentru începerea cu autentificare simplă și avansarea către OAuth 2.1 și RBAC, cu referințe la module avansate de securitate.

Aceste adăugiri oferă ghid practica și aplicabilă pentru construirea unor implementări server MCP mai robuste, sigure și flexibile, făcând legătura între conceptele fundamentale și modelele de producție avansate.

## 29 septembrie 2025

### Laboratoare de Integrare a Bazei de Date MCP Server - Curs Complet Practic

#### 11-MCPServerHandsOnLabs - Curriculum Complet pentru Integrare Bază de Date
- **Traseu Complet de Învățare cu 13 Laboratoare**: Adăugat curriculum practic complet pentru construirea serverelor MCP gata pentru producție cu integrare PostgreSQL
  - **Implementare din Viața Reală**: Caz de utilizare Zava Retail analytics demonstrând modele enterprise
  - **Progresie Structurată de Învățare**:
    - **Laboratoare 00-03: Fundamente** - Introducere, Arhitectură de Bază, Securitate & Multi-Tenant, Configurare Mediu
    - **Laboratoare 04-06: Construirea Serverului MCP** - Proiectare & Schema Bazei de Date, Implementarea Server MCP, Dezvoltarea Instrumentelor
    - **Laboratoare 07-09: Funcționalități Avansate** - Integrare Căutare Semantică, Testare & Debugging, Integrare VS Code
    - **Laboratoare 10-12: Producție & Practici Optime** - Strategii de Deploy, Monitorizare & Observabilitate, Practici & Optimizări
  - **Tehnologii Enterprise**: Framework FastMCP, PostgreSQL cu pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Caracteristici Avansate**: Securitate pe nivel de rând (RLS), căutare semantică, acces multi-tenant la date, vector embeddings, monitorizare în timp real

#### Standardizarea Terminologiei - Convertire Modul în Laborator
- **Actualizare Completă Documentație**: Actualizat sistematic toate fișierele README din 11-MCPServerHandsOnLabs pentru a folosi terminologia „Laborator” în loc de „Modul”
  - **Antete de Secțiune**: Actualizat „What This Module Covers” la „What This Lab Covers” în toate cele 13 laboratoare
  - **Descriere Conținut**: Modificat „This module provides...” în „This lab provides...” în toată documentația
  - **Obiective de Învățare**: Actualizat „By the end of this module...” în „By the end of this lab...”
  - **Linkuri de Navigare**: Convertit toate referințele „Module XX:” în „Lab XX:” în cross-references și navigație
  - **Urmărirea Finalizării**: Actualizat „After completing this module...” în „After completing this lab...”
  - **Referințe Tehnice Păstrate**: Menținute referințele tehnice de Python modul în fișierele de configurare (ex: `"module": "mcp_server.main"`)

#### Îmbunătățirea Ghidului de Studiu (study_guide.md)
- **Harta Vizuală a Curriculumului**: Adăugată noua secțiune „11. Database Integration Labs” cu vizualizarea structurii laboratoarelor
- **Structura Repozitoriului**: Actualizat de la zece la unsprezece secțiuni principale cu descriere detaliată 11-MCPServerHandsOnLabs
- **Orientări în Traseul de Învățare**: Instrucțiuni de navigare extinse acoperind secțiunile 00-11
- **Acoperirea Tehnologică**: Adăugate detalii despre FastMCP, PostgreSQL, integrarea serviciilor Azure
- **Rezultate de Învățare**: Accent pe dezvoltarea serverelor gata pentru producție, modele de integrare baze de date și securitate enterprise

#### Îmbunătățirea Structurii README Principal
- **Terminologie Bazată pe Laboratoare**: Actualizat README.md principal din 11-MCPServerHandsOnLabs pentru a folosi consistent structura „Laborator”
- **Organizarea Traseului de Învățare**: Progres clar de la concepte fundamentale până la implementări avansate și producție
- **Accent pe Practică și Realitate**: Accent pe învățare practică, hands-on cu modele și tehnologii enterprise

### Îmbunătățiri Calitate & Consistență Documentație
- **Accent pe Învățare Practică**: Consolidată abordarea practică, bazată pe laboratoare în toată documentația
- **Focus pe Modele Enterprise**: Evidențiată importanța implementărilor gata pentru producție și considerentele de securitate enterprise
- **Integrare Tehnologică**: Acoperire completă a modernelor servicii Azure și modele de integrare AI
- **Progresie Clară**: Traseu structurat și clar de la concepte de bază la deploy în producție

## 26 septembrie 2025

### Îmbunătățiri Cazuri de Studiu - Integrare GitHub MCP Registry

#### Cazuri de Studiu (09-CaseStudy/) - Focus pe Dezvoltarea Ecosistemului
- **README.md**: Extindere majoră cu caz de studiu complet despre GitHub MCP Registry
  - **Caz de Studiu GitHub MCP Registry**: Noul caz complet examinând lansarea MCP Registry de GitHub în septembrie 2025
    - **Analiza Problemei**: Examinare detaliată a fragmentării descoperirii și depanării serverelor MCP
    - **Arhitectura Soluției**: Abordarea centralizată a registrului GitHub cu instalare VS Code cu un singur click
    - **Impactul în Afaceri**: Îmbunătățiri măsurabile în onboarding-ul și productivitatea dezvoltatorilor
    - **Valoare Strategică**: Focus pe deploy modular de agenți și interoperabilitate între instrumente
    - **Dezvoltare Ecosistem**: Poziționarea ca platformă fundamentală pentru integrarea agenților
  - **Structură Îmbunătățită Cazuri de Studiu**: Actualizate toate cele șapte cazuri cu format constant și descrieri cuprinzătoare
    - Agenți de Călătorie Azure AI: Accent pe orchestrarea multi-agent
    - Integrare Azure DevOps: Focus pe automatizarea workflow-ului
    - Recuperare Documentație în Timp Real: Implementare client consolă Python
    - Generator Plan Studii Interactiv: Aplicație web conversatională Chainlit
    - Documentație în Editor: Integrare VS Code și GitHub Copilot
    - Azure API Management: Modele de integrare API enterprise
    - GitHub MCP Registry: Dezvoltare ecosistem și platformă comunitară
  - **Concluzie Cuprinzătoare**: Secțiune rescrisă evidențiind cele șapte cazuri acoperind multiple dimensiuni ale implementării MCP
    - Integrare Enterprise, Orchestrare Multi-Agent, Productivitate Dezvoltatori
    - Dezvoltare Ecosistem, Categorii de Aplicații Educaționale
    - Perspective avansate privind modele arhitecturale, strategii de implementare și practici optime
    - Accent pe MCP ca protocol matur și gata de producție

#### Actualizări Ghid de Studiu (study_guide.md)
- **Hartă Curriculum Vizuală**: Actualizat mindmap pentru includerea GitHub MCP Registry în secțiunea Cazuri de Studiu
- **Descriere Cazuri de Studiu**: Detaliat de la descrieri generice la analiza aprofundată a celor șapte cazuri complete
- **Structura Repozitoriului**: Actualizată secțiunea 10 pentru a reflecta acoperirea completă a cazurilor de studiu cu detalii specifice
- **Integrare Schimbări**: Adăugată intrarea din 26 septembrie 2025 pentru documentarea adăugării GitHub MCP Registry și îmbunătățirilor cazurilor de studiu
- **Actualizare Dată**: Actualizat timestamp-ul în footer la cea mai recentă revizie (26 septembrie 2025)

### Îmbunătățiri Calitate Documentație
- **Consistență**: Standardizat formatul și structura cazurilor de studiu în toate cele șapte exemple
- **Acoperire Completă**: Cazurile acoperă acum enterprise, productivitate dezvoltatori și scenarii de dezvoltare ecosistem
- **Poziționare Strategică**: Accent lărgit pe MCP ca platformă fundamentală pentru deploy de sisteme agentice
- **Integrare Resurse**: Actualizat resursele suplimentare să includă link-ul GitHub MCP Registry

## 15 septembrie 2025

### Extindere Subiecte Avansate - Transporturi Personalizate & Inginerie Contextuală

#### Transporturi Personalizate MCP (05-AdvancedTopics/mcp-transport/) - Ghid Nou de Implementare Avansată
- **README.md**: Ghid complet pentru implementarea mecanismelor de transport MCP personalizate
  - **Transport Azure Event Grid**: Implementare completă serverless bazată pe evenimente
    - Exemple în C#, TypeScript și Python cu integrare Azure Functions
    - Modele arhitecturale bazate pe evenimente pentru soluții scalabile MCP
    - Receptori webhook și gestionarea mesajelor push
  - **Transport Azure Event Hubs**: Implementare transport streaming cu throughput ridicat
    - Capacități de streaming în timp real pentru scenarii cu latență redusă
    - Strategii de partiționare și management checkpoint
    - Batching mesaje și optimizarea performanței
  - **Modele Integrare Enterprise**: Exemple arhitecturale gata pentru producție
    - Procesare distribuită MCP pe mai multe Azure Functions
    - Arhitecturi hibride de transport combinând mai multe tipuri
    - Durabilitatea mesajelor, fiabilitate și strategii de gestionare erori
  - **Securitate & Monitorizare**: Integrare Azure Key Vault și modele de observabilitate
    - Autentificare identitate gestionată și acces cu privilegii minime
    - Telemetrie Application Insights și monitorizare performanță
    - Modele circuit breakers și toleranță la erori
  - **Framework-uri de Testare**: Strategii complete pentru testarea transporturilor personalizate
    - Testare unitară cu test doubles și mock frameworks
    - Testare integrată cu Azure Test Containers
    - Considerații pentru testare performanță și încărcare

#### Inginerie Contextuală (05-AdvancedTopics/mcp-contextengineering/) - Disciplina emergentă AI
- **README.md**: Explorare completă a ingineriei contextuale ca domeniu emergent
  - **Principii de Bază**: Partajarea completă a contextului, conștientizarea deciziilor acțiunii și gestionarea ferestrei contextuale
  - **Aliniere Protocol MCP**: Cum MCP tratează provocările ingineriei contextului
    - Limitări ale ferestrei contextuale și strategii de încărcare progresivă
    - Determinarea relevanței și recuperarea dinamică a contextului
    - Gestionarea contextului multi-modal și considerații de securitate
  - **Abordări de Implementare**: Arhitecturi single-threaded vs. multi-agent
    - Tehnici de fragmentare și prioritizare a contextului
    - Încărcare progresivă și strategii de compresie a contextului
    - Abordări stratificate și optimizări de recuperare
  - **Cadru de Măsurare**: Metrici emergente pentru evaluarea eficienței contextului
    - Eficiența inputului, performanță, calitate și experiența utilizatorului
    - Abordări experimentale de optimizare a contextului
    - Analiza eșecurilor și metodologii de îmbunătățire

#### Actualizări Navigare Curriculum (README.md)
- **Structură Modul Îmbunătățită**: Actualizată tabelul curriculum pentru a include subiectele avansate noi
  - Adăugate intrările Context Engineering (5.14) și Custom Transport (5.15)
  - Format consistent și linkuri de navigare peste toate modulele
  - Descrieri actualizate pentru a reflecta scopul actual al conținutului

### Îmbunătățiri Structură Director
- **Standardizare Denumire**: Redenumit „mcp transport” în „mcp-transport” pentru consistență cu celelalte foldere de subiecte avansate
- **Organizare Conținut**: Toate folderele 05-AdvancedTopics urmează acum modelul numelui consistent (mcp-[subiect])

### Îmbunătățiri Calitate Documentație
- **Aliniere la Specificația MCP**: Toate conținuturile noi referă specificația MCP 2025-06-18 curentă
- **Exemple Multi-Limbaj**: Exemple complete de cod în C#, TypeScript și Python
- **Focus Enterprise**: Modele gata pentru producție și integrare Azure cloud pe tot parcursul
- **Documentație Vizuală**: Diagrame Mermaid pentru vizualizarea arhitecturii și a fluxurilor

## 18 august 2025

### Actualizare Completă Documentație - Standarde MCP 2025-06-18

#### Practici Recomandate de Securitate MCP (02-Security/) - Modernizare Completă
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Rescriere completă aliniată cu Specificația MCP 2025-06-18  
  - **Cerințe Obligatorii**: Adăugate cerințe explicite TREBUIE/NU TREBUIE din specificația oficială cu indicatori vizuali clari  
  - **12 Practici de Securitate de Bază**: Restructurate de la o listă de 15 puncte la domenii cuprinzătoare de securitate  
    - Securitatea Tokenului & Autentificare cu integrare a furnizorului extern de identitate  
    - Managementul Sesiunii & Securitate Transport cu cerințe criptografice  
    - Protecție Specifică Amenințărilor AI cu integrare Microsoft Prompt Shields  
    - Controlul Accesului & Permisiuni cu principiul privilegiului minim  
    - Siguranța Conținutului & Monitorizare cu integrare Azure Content Safety  
    - Securitatea Lanțului de Aprovizionare cu verificare completă a componentelor  
    - Securitatea OAuth & Prevenirea Confuziei Înaltului cu implementare PKCE  
    - Răspuns la Incidente & Recuperare cu capabilități automatizate  
    - Conformitate & Guvernanță cu aliniere la reglementări  
    - Controale Avansate de Securitate cu arhitectură zero trust  
    - Integrarea Ecosistemului Microsoft de Securitate cu soluții cuprinzătoare  
    - Evoluția Continuă a Securității cu practici adaptive  
  - **Soluții Microsoft de Securitate**: Ghid de integrare îmbunătățit pentru Prompt Shields, Azure Content Safety, Entra ID și GitHub Advanced Security  
  - **Resurse de Implementare**: Linkuri organizate pe categorii de Documentație Oficială MCP, Soluții de Securitate Microsoft, Standarde de Securitate și Ghiduri de Implementare  

#### Controale Avansate de Securitate (02-Security/) - Implementare Enterprise  
- **MCP-SECURITY-CONTROLS-2025.md**: Reevaluare completă cu cadru de securitate pentru mediul enterprise  
  - **9 Domenii Cuprinzătoare de Securitate**: Extindere de la controale de bază la un cadru detaliat enterprise  
    - Autentificare & Autorizare Avansată cu integrare Microsoft Entra ID  
    - Securitatea Tokenului & controale anti-passthrough cu validare completă  
    - Controale de Securitate ale Sesiunii cu prevenire a deturnării  
    - Controale de Securitate Specifice AI cu prevenire a injectării de prompturi și intoxicarea uneltelor  
    - Prevenirea Atacului Confused Deputy cu securitate proxy OAuth  
    - Securitatea Execuției Uneltelor cu sandboxing și izolare  
    - Controale pentru Securitatea Lanțului de Aprovizionare cu verificare a dependențelor  
    - Controale de Monitorizare & Detecție cu integrare SIEM  
    - Răspuns la Incidente & Recuperare cu capabilități automatizate  
  - **Exemple de Implementare**: Adăugate blocuri de configurație YAML detaliate și exemple de cod  
  - **Integrare Soluții Microsoft**: Acoperire cuprinzătoare a serviciilor Azure de securitate, GitHub Advanced Security și management identitate enterprise  

#### Securitate Subiecte Avansate (05-AdvancedTopics/mcp-security/) - Implementare Pregătită pentru Producție  
- **README.md**: Rescriere completă pentru implementare securitate enterprise  
  - **Aliniere la Specificația Curentă**: Actualizat conform Specificației MCP 2025-06-18 cu cerințe obligatorii de securitate  
  - **Autentificare Îmbunătățită**: Integrare Microsoft Entra ID cu exemple cuprinzătoare în .NET și Java Spring Security  
  - **Integrare Securitate AI**: Implementare Microsoft Prompt Shields și Azure Content Safety cu exemple detaliate în Python  
  - **Atenuarea Amenințărilor Avansate**: Exemple complete de implementare pentru  
    - Prevenirea atacului Confused Deputy cu PKCE și validarea consimțământului utilizatorului  
    - Prevenirea passthrough a tokenului cu validarea audienței și gestionarea sigură a tokenului  
    - Prevenirea deturnării sesiunii cu legare criptografică și analiză comportamentală  
  - **Integrare Securitate Enterprise**: Monitorizare Azure Application Insights, canale de detectare amenințări și securitatea lanțului de aprovizionare  
  - **Lista de Verificare a Implementării**: Control clar obligatoriu vs. recomandat cu beneficii din ecosistemul de securitate Microsoft  

### Calitatea Documentației & Alinierea la Standardele  
- **Referințe la Specificații**: Actualizate toate referințele la Specificația MCP 2025-06-18  
- **Ecosistemul Microsoft de Securitate**: Ghiduri de integrare îmbunătățite în toate documentele de securitate  
- **Implementare Practică**: Adăugate exemple de cod detaliate în .NET, Java și Python cu tipare enterprise  
- **Organizarea Resurselor**: Categorii cuprinzătoare de documentație oficială, standarde de securitate și ghiduri de implementare  
- **Indicatori Vizuali**: Marcaje clare pentru cerințe obligatorii vs. practici recomandate  

#### Concepte Centrale (01-CoreConcepts/) - Modernizare Completă  
- **Actualizare Versiune Protocol**: Referință actualizată la Specificația MCP 2025-06-18 cu versiune bazată pe dată (format YYYY-MM-DD)  
- **Rafinare Arhitectură**: Descrieri îmbunătățite pentru Hosts, Clienți și Servere reflectând tiparele actuale MCP  
  - Hosts definite clar ca aplicații AI ce coordonează multiple conexiuni client MCP  
  - Clienții descriși ca conectori de protocol menținând relații unu-la-unu cu serverele  
  - Serverele detaliate cu scenarii de implementare locală vs. remote  
- **Restructurare Primitive**: Overhaul complet al primitivelor server și client  
  - Primitive Server: Resurse (surse date), Prompturi (șabloane), Unelte (funcții executabile) cu explicații și exemple detaliate  
  - Primitive Client: Eșantionare (finalizări LLM), Solicitare (input utilizator), Logare (debugging/monitorizare)  
  - Actualizate metodele curente de descoperire (`*/list`), recuperare (`*/get`) și execuție (`*/call`)  
- **Arhitectură Protocol**: Model introdus cu două niveluri  
  - Nivel Date: bazat pe JSON-RPC 2.0 cu gestionarea ciclului de viață și primitive  
  - Nivel Transport: STDIO (local) și HTTP Streamabil cu SSE (remote)  
- **Cadrul de Securitate**: Principii cuprinzătoare de securitate inclusiv consimțământ explicit al utilizatorului, protecția confidențialității datelor, siguranța execuției uneltelor și securitatea nivelului transport  
- **Tipare de Comunicare**: Mesaje actualizate pentru inițializare, descoperire, execuție și notificare  
- **Exemple de Cod**: Exemple reîmprospătate multi-limbaj (.NET, Java, Python, JavaScript) reflectând tiparele MCP SDK curente  

#### Securitate (02-Security/) - Reevaluare Completă de Securitate  
- **Aliniere la Standarde**: Aliniere completă cu cerințele de securitate din Specificația MCP 2025-06-18  
- **Evoluția Autentificării**: Documentată evoluția de la servere OAuth custom la delegarea către furnizor extern de identitate (Microsoft Entra ID)  
- **Analiză Amenințări Specifice AI**: Acoperire extinsă a vectorilor moderni de atac AI  
  - Scenarii detaliate de atac prin injectare prompt cu exemple din lumea reală  
  - Mecanisme de intoxicare a uneltelor și tipare atac "rug pull"  
  - Intoxicare fereastră context și atacuri de confuzie a modelului  
- **Soluții Microsoft de Securitate AI**: Acoperire cuprinzătoare a ecosistemului Microsoft  
  - AI Prompt Shields cu detecție avansată, evidențiere și tehnici de delimitare  
  - Modele de integrare Azure Content Safety  
  - GitHub Advanced Security pentru protecția lanțului de aprovizionare  
- **Atenuarea Amenințărilor Avansate**: Controale detaliate pentru  
  - Deturnarea sesiunii cu scenarii specifice MCP și cerințe criptografice pentru ID sesiunii  
  - Probleme Confused Deputy în scenarii proxy MCP cu cerințe explicite de consimțământ  
  - Vulnerabilități passthrough token cu controale obligatorii de validare  
- **Securitatea Lanțului de Aprovizionare**: Extindere acoperire pentru lanțul AI inclusiv modele fundamentale, servicii embeddings, furnizori context și API-uri terțe  
- **Securitatea Fundamentelor**: Integrare avansată cu tipare de securitate enterprise, inclusiv arhitectură zero trust și ecosistem de securitate Microsoft  
- **Organizarea Resurselor**: Linkuri cuprinzătoare organizate pe tipuri (Documentație Oficială, Standarde, Cercetare, Soluții Microsoft, Ghiduri Implementare)  

### Îmbunătățiri Calitate Documentație  
- **Obiective Structurate de Învățare**: Obiective îmbunătățite cu rezultate specifice și acționabile  
- **Referințe Încrucișate**: Adăugate linkuri între subiecte corelate de securitate și concepte centrale  
- **Informații Curente**: Actualizate toate referințele de dată și linkurile de specificație la standardele curente  
- **Ghiduri de Implementare**: Adăugate instrucțiuni specifice și acționabile pe tot parcursul ambelor secțiuni  

## 16 Iulie 2025  

### Îmbunătățiri README și Navigație  
- Redesign complet al navigației curriculare în README.md  
- Înlocuite etichetele `<details>` cu un format tabelar mai accesibil  
- Create opțiuni alternative de layout în noul folder "alternative_layouts"  
- Adăugate exemple de navigare bazate pe carduri, taburi și acordeon  
- Actualizat secțiunea structurii repository-ului să includă toate fișierele recente  
- Îmbunătățită secțiunea „Cum să folosești acest curriculum” cu recomandări clare  
- Actualizate linkurile de specificație MCP pentru a indica URL-urile corecte  
- Adăugată secțiunea Inginerie Context (5.14) în structura curriculului  

### Actualizări Ghid de Studiu  
- Revizuit complet ghidul de studiu pentru a se alinia cu structura curentă a repository-ului  
- Adăugate secțiuni noi pentru Clienți MCP și Unelte, și Servere MCP populare  
- Actualizat Harta Vizuală a Curriculumului pentru reflecția precisă a tuturor subiectelor  
- Îmbunătățite descrierile Temelor Avansate pentru a acoperi toate domeniile specializate  
- Actualizată secțiunea Studiilor de Caz pentru a reflecta exemple reale  
- Adăugat acest jurnal complet al modificărilor  

### Contribuții Comunitare (06-CommunityContributions/)  
- Adăugate informații detaliate despre serverele MCP pentru generarea de imagini  
- Secțiune detaliată despre utilizarea Claude în VSCode  
- Instrucțiuni pentru setarea și utilizarea clientului terminal Cline  
- Actualizată secțiunea client MCP cu toate opțiunile populare  
- Îmbunătățite exemplele de contribuții cu mostre de cod mai exacte  

### Subiecte Avansate (05-AdvancedTopics/)  
- Organizate toate folderele specializate cu denumiri consistente  
- Adăugate materiale și exemple de inginerie a contextului  
- Documentație de integrare agent Foundry adăugată  
- Documentație extinsă pentru integrarea securității Entra ID  

## 11 Iunie 2025  

### Creare Inițială  
- Lansată prima versiune a curriculumului MCP pentru începători  
- Creată structura de bază pentru toate cele 10 secțiuni principale  
- Implementată Harta Vizuală a Curriculumului pentru navigare  
- Adăugate proiecte exemplu inițiale în mai multe limbaje de programare  

### Începutul (03-GettingStarted/)  
- Creeate primele exemple de implementare a serverului  
- Adăugat ghid de dezvoltare client  
- Incluse instrucțiuni de integrare client LLM  
- Documentație pentru integrare VS Code adăugată  
- Exemple server cu Server-Sent Events (SSE) implementate  

### Concepte Centrale (01-CoreConcepts/)  
- Explicație detaliată a arhitecturii client-server adăugată  
- Documentație despre componente cheie ale protocolului  
- Documentate tipare de mesagerie în MCP  

## 23 Mai 2025  

### Structura Repository  
- Inițializat repository cu structura de bază a folderelor  
- Creat fișiere README pentru fiecare secțiune majoră  
- Configurat infrastructura de traducere  
- Adăugate resurse de imagini și diagrame  

### Documentație  
- Creat README.md inițial cu prezentarea curriculumului  
- Adăugat CODE_OF_CONDUCT.md și SECURITY.md  
- Configurat SUPPORT.md cu ghid pentru solicitarea ajutorului  
- Creată structura preliminară a ghidului de studiu  

## 15 Aprilie 2025  

### Planificare și Cadrul General  
- Planificare inițială pentru curriculumul MCP pentru începători  
- Definit obiective de învățare și audiență țintă  
- Conturată structura în 10 secțiuni a curriculumului  
- Dezvoltat cadru conceptual pentru exemple și studii de caz  
- Creat prototipuri inițiale de exemple pentru conceptele cheie

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertisment**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să oferim o traducere exactă, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->