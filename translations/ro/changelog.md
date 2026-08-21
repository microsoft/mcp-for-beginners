# Jurnal de modificări: Curriculum MCP pentru Începători

Acest document servește ca înregistrare a tuturor modificărilor semnificative realizate în curriculumul Model Context Protocol (MCP) pentru Începători. Modificările sunt documentate în ordine cronologică inversă (cele mai noi modificări primele).

## 29 iulie 2026

### Noul modul companion 08: Reliability Sidecars și retry-uri sigure

A fost adăugată o lecție companion neutră din punct de vedere al furnizorului pentru uneltele MCP care creează efecte în lumea reală,
aliniată cu specificația finală `2026-07-28`.

- **Nou**: Lecția companion [reliability sidecar][reliability-sidecar]
  folosește o poveste cu un tichet de suport, două diagrame Mermaid și un flux de decizie pentru retry
  pentru a explica cheile unei operațiuni stabile, admiterea atomică a duplicatelor,
  reconcilierea, dovezile și limita extensiei Tasks.
- **Nou**: Un exercițiu de injecție de eșec folosind biblioteca standard Python și SQLite
  folosește depozite separate pentru operațiuni și tichete pentru a demonstra o răspuns pierdut
  după ce un efect extern s-a angajat. Șase teste deterministe acoperă duplicarea naivă,
  recuperarea protejată prin restart, conflictele de sarcină, rezultatele în cache,
  revendicările active și admiterea concurentă a duplicatelor.
- **Actualizat**: Modulul 08 leagă acum lecția companion, identifică
  modelul final `2026-07-28` de cerere fără stare, distinge observabilitatea OpenTelemetry
  de funcția de logging MCP învechită și limitează exemplul generic de retry
  la operațiuni doar de citire.
- **Opțional**: Lecția mapează conceptele portabile într-o implementare comunitară etichetată
  fără a face ca serviciul găzduit sau un apel de rețea să facă parte
  din exercițiu.

[reliability-sidecar]: ./08-BestPractices/reliability-sidecars/README.md

## 2 iulie 2026

### Lecție nouă: Candidatul la lansare specificație MCP 2026-07-28

A fost adăugată acoperirea candidatului la lansare a specificației MCP `2026-07-28` (anunțat pe 21 mai 2026; lansarea finală programată pentru 28 iulie 2026), rezumat din [postarea oficială de anunț](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/). Baza curriculumului rămâne **MCP Specification 2025-11-25** până la lansarea noii versiuni, așadar aceasta este prezentată ca o ghidare orientată spre viitor și nu o rescriere a lecțiilor existente.

- **Nou**: [01-CoreConcepts/mcp-2026-07-28-release-candidate.md](./01-CoreConcepts/mcp-2026-07-28-release-candidate.md) — o lecție completă care acoperă nucleul protocolului fără stare (eliminarea handshake-ului `initialize` și `Mcp-Session-Id`), noile headere de rutare `Mcp-Method`/`Mcp-Name`, metadatele pentru cache `ttlMs`/`cacheScope`, W3C Trace Context în `_meta`, cadrul formal de Extensii (Aplicațiile MCP și noua extensie Tasks), șase SEPs pentru întărirea autorizării, învechirea Roots/Sampling/Logging și trecerea la JSON Schema 2020-12 complet pentru schemele uneltelor.
- **Actualizat** cu anunțuri orientate spre viitor legate de noua lecție:
  - [01-CoreConcepts/README.md](./01-CoreConcepts/README.md): notă despre versiunea protocolului, secțiunile Sampling/Roots/Logging/Tasks, și „Ce urmează”

  - [02-Security/README.md](./02-Security/README.md): apel de întărire a autorizării
  - [03-GettingStarted/06-http-streaming/README.md](./03-GettingStarted/06-http-streaming/README.md): apel despre transport fără stare
  - [03-GettingStarted/14-sampling/README.md](./03-GettingStarted/14-sampling/README.md): apel privind eliminarea Sampling
  - [05-AdvancedTopics/mcp-protocol-features/README.md](./05-AdvancedTopics/mcp-protocol-features/README.md): apel privind eliminarea înregistrării și extensia Tasks
  - [05-AdvancedTopics/mcp-transport/README.md](./05-AdvancedTopics/mcp-transport/README.md): apel despre transport fără stare/redirecționare sesiune
  - [README.md](./README.md): notă „Privind în perspectivă” în secțiunea specificației și o nouă intrare `1.1` în tabelul modulului de curriculum
  - [study_guide.md](./study_guide.md): punct privind perspectivele în secțiunea Prezentare generală concepte de bază și o notă adițională datată
  - [03-GettingStarted/11-simple-auth/README.md](./03-GettingStarted/11-simple-auth/README.md): apel despre harta de transport `mcp-session-id` înaintea modelului de solicitare fără stare
  - [05-AdvancedTopics/README.md](./05-AdvancedTopics/README.md): apel de prezentare generală a modulului despre Contexturile Rădăcină/Eliminările Sampling și extensia Tasks
  - [05-AdvancedTopics/mcp-security/README.md](./05-AdvancedTopics/mcp-security/README.md): apel de întărire a autorizării

## 24 iunie 2026

### Lecție nouă: Utilizarea MCP în aplicația Copilot

- [Secțiunea Tooling](./12-tooling/README.md) Secțiune tooling adăugată.
- [MCP în aplicația Copilot](./12-tooling/01-copilot-app/README.md)

## 16 iunie 2026

### Alinierea specificației MCP & Validarea exemplarelor

Am validat curriculumul față de **Specificația MCP 2025-11-25** curentă și cele mai recente SDK-uri oficiale, apoi am corectat referințele învechite către specificație și am confirmat că exemplarele de bază încă se compilează și rulează.

#### Corecții versiune specificație (2025-06-18 / 2025-03-26 → 2025-11-25)

Am actualizat conținutul în engleză unde încă se afirma că o revizuire mai veche a specificației este standardul *curent/ultimul*, și am redirecționat linkurile către rutele canonice `modelcontextprotocol.io` ale specificației:
- **05-AdvancedTopics/mcp-security/README.md**: Am actualizat bannerul „Standard Curent”, introducerea, titlul principiilor esențiale de securitate, titlul cerințelor obligatorii, secțiunea Microsoft Entra ID, linkurile din Referințe & Resurse, și nota finală de securitate (8 referințe) către 2025-11-25
- **05-AdvancedTopics/mcp-transport/README.md**: Am actualizat linkul către Resurse suplimentare din specificație și bannerul „Standard Curent” la 2025-11-25
- **05-AdvancedTopics/mcp-realtimesearch/README.md**: Am înlocuit linkul învechit `2025-03-26` pentru securitate și încredere cu pagina actuală de bune practici de securitate 2025-11-25

- **03-GettingStarted/14-sampling/README.md**: Actualizat linkul oficial al documentației de sampling la 2025-11-25

- **03-GettingStarted/05-stdio-server/README.md**: Actualizat referința în prezent la "specificația MCP curentă" și linkul către specificația Resurselor Suplimentare la 2025-11-25 (note istorice privind deprecarea SSE lăsate intacte pentru acuratețe)

#### Validarea Exemplului Față de SDK-urile Curente

- **TypeScript (03-GettingStarted/01-first-server/solution/typescript)**: `npm install` a rezolvat `@modelcontextprotocol/sdk@1.29.0`; `tsc --noEmit` a trecut fără erori de tip — API-urile existente `McpServer`/`StdioServerTransport` rămân valide
- **Python (03-GettingStarted/01-first-server/solution/python)**: Validat într-un `.venv` izolat cu `mcp[cli]` (1.27.2); `py_compile` a trecut și `FastMCP.list_tools()` a returnat corect uneltele `add` și `subtract`
- Confirmat că toate intervalele de versiuni pentru `@modelcontextprotocol/sdk` (`>=1.26.0` / `^1.26.0` / `^1.27.0`) se rezolvă curat la versiunea curentă `1.29.0` fără schimbări de API care să strice compatibilitatea

#### Alinierea Pin-urilor Dependențelor (închiderea decalajelor de versiune)

Actualizat pin-urile SDK învechite astfel încât fiecare exemplu să urmărească versiunea curentă MCP, conform convenției din tot repo-ul:
- **03-GettingStarted/05-stdio-server/solution/typescript/package.json**: Actualizat `@modelcontextprotocol/sdk` de la `^1.8.0` → `>=1.26.0` și descrierea învechită a pachetului `"updated for MCP 2025-06-18"` la `"aligned with MCP Specification 2025-11-25"`
- **10-StreamliningAIWorkflows.../lab3/code/weather_mcp/pyproject.toml** și **lab4/code/github_mcp_server/pyproject.toml**: Actualizat pin-ul exact `mcp==1.23.0` → `mcp>=1.26.0`; regenerate ambele fișiere `uv.lock` (`uv lock`) astfel încât lockfile-urile să se rezolve la `mcp 1.27.2` curent și să rămână sincronizate cu manifestele

#### Analiza Golurilor Curriculum — Acoperirea Funcționalităților din Specificația Ultimă

Verificat că curriculum-ul acoperă deja toate primitivele introduse/extinse în MCP 2025-11-25, deci nu mai există goluri de conținut:
- **Sampling**: Lecția 03-GettingStarted/14-sampling plus 05-AdvancedTopics/mcp-sampling
- **Elicitation (incl. modul URL)**: Documentat în 01-CoreConcepts și 05-AdvancedTopics/mcp-protocol-features
- **Roots**: Documentat în 00-Introduction, 01-CoreConcepts, și 05-AdvancedTopics/mcp-root-contexts
- **Tasks (operațiuni experimentale de durată lungă)**: Documentat în 01-CoreConcepts și 05-AdvancedTopics/mcp-protocol-features
- **Anotări pentru Unelte** (`readOnlyHint` / `destructiveHint`): Documentat în 01-CoreConcepts și 05-AdvancedTopics/mcp-protocol-features

### Întărirea Securității & Remedierea Vulnerabilităților la Dependențe

Am efectuat o trecere completă de securitate prin fiecare manifest de dependențe și codul sursă al exemplului, apoi am remediat toate avertismentele npm raportate și o constatare la nivel de cod. După remediere, `npm audit` raportat **0 vulnerabilități** în fiecare director verificat.

#### Vulnerabilități ale dependențelor npm (transitive) — Remediate

Auditat toate cele 15 fișiere `package-lock.json` comise. Vulnerabilitățile erau limitate la dependențe transitive aduse de uneltele de dezvoltare MCP Inspector, clientul OpenAI și SDK-ul MCP; toate sunt acum rezolvate fără a distruge funcționalitățile exemplelor:
- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/inspector** și **lab3/code/weather_mcp/inspector**: Actualizat `@modelcontextprotocol/inspector` (`0.16.6` / `0.14.1` → `0.22.0`), ceea ce a eliminat alertările legate de `ajv`, `brace-expansion`, `diff`, `path-to-regexp` și `ws` incluse. Adăugat un entry npm `overrides` forțând patch-ul `shell-quote@1.8.4` pentru a elimina alerta critică rămasă în `concurrently`; regenerate ambele lockfile-uri (acum 0 vulnerabilități)
- **03-GettingStarted/samples/typescript**: `npm audit fix` a actualizat dependența tranzitivă `qs` (moderată) la o versiune reparată
- **03-GettingStarted/samples/javascript**: `npm audit fix` a actualizat dependența tranzitivă `hono` (moderată) la o versiune reparată
- **03-GettingStarted/03-llm-client/solution/typescript**: `npm audit fix` a actualizat dependența tranzitivă `form-data` (ridicată) la o versiune reparată
- **03-GettingStarted/11-simple-auth/solution/typescript**: Generat fișierul lipsă `package-lock.json` astfel încât proiectul să fie reproducibil și auditat (0 vulnerabilități)

#### Remediere de securitate la nivel de cod (OWASP A03: Injecție)

- **10-StreamliningAIWorkflows.../lab4/code/github_mcp_server/src/server.py**: Eliminat `shell=True` din unealta `open_in_vscode`. Apelul anterior `subprocess.run(["start", "", vscode_path, folder_path], shell=True)` permitea ca metacaractere shell din calea folderului să fie interpretate de `cmd.exe` (vector de injecție de comenzi). Acum lansează direct executabilul `Code.exe` rezolvat cu folderul ca argument — fără shell — ceea ce este funcțional echivalent și sigur

#### Audit al Dependențelor Python

- Auditat fiecare set de cerințe Python cu `pip-audit`. `05-AdvancedTopics` și `03-GettingStarted/samples/python` nu au raportat **vulnerabilități cunoscute** (intervalele lor pentru `mcp` / `httpx` / `pydantic` / `python-dotenv` rezolvă la versiuni curente patch-uite)
- **09-CaseStudy/docs-mcp/solution/python/requirements.txt**: `pip-audit` a identificat dependența tranzitivă **`werkzeug` 3.1.1** cu trei avertismente DoS legate de `safe_join` pe nume de dispozitiv Windows — `CVE-2025-66221`, `CVE-2026-21860`, și `CVE-2026-27199` (toate remediate în 3.1.6). Adăugat pin explicit de securitate `werkzeug>=3.1.6` astfel încât să se rezolve versiunea patch-uită; verificat că restricția se rezolvă curat cu stiva `chainlit` / `mcp` / `semantic-kernel`

### Rebranding-ul Numele Produsului

Actualizat tot conținutul curriculum-ului pentru a reflecta rebranding-ul produselor Microsoft:


#### Azure AI Foundry → Microsoft Foundry
- **SUPPORT.md**: Link-ul comunității Discord actualizat

- **AGENTS.md**: Referință server Discord actualizată  
- **README.md**: Referințe actualizate ale ecosistemului tehnologic  
- **study_guide.md**: Referințe actualizate ale studiului de caz  
- **05-AdvancedTopics/README.md**: Titlu și descriere actualizate pentru Modulul 5.13  
- **05-AdvancedTopics/mcp-integration/README.md**: Antet și descriere secțiune actualizate  
- **05-AdvancedTopics/mcp-foundry-agent-integration/README.md**: Titlu complet al modulului și conținut actualizate  
- **05-AdvancedTopics/mcp-security-entra/README.md**: Link de referință încrucișată actualizat  
- **07-LessonsfromEarlyAdoption/README.md**: Referințe actualizate ale studiului de caz  
- **07-LessonsfromEarlyAdoption/microsoft-mcp-servers.md**: Antet Secțiunea 9, insigne și capabilități actualizate  
- **08-BestPractices/README.md**: Link comunitate Discord actualizat  
- **09-CaseStudy/docs-mcp/solution/scenario3/README.md**: Referință actualizată canal Discord  
- **09-CaseStudy/docs-mcp/solution/python/README.md**: Referință actualizată pentru implementarea modelului  
- **11-MCPServerHandsOnLabs/00-Introduction/README.md**: Tabel servicii AI actualizat  
- **11-MCPServerHandsOnLabs/03-Setup/README.md**: Referințe resurse actualizate  

#### AI Toolkit / AITK → Microsoft Foundry Toolkit Extension pentru VS Code  
- **README.md**: Referințe principale ale curriculumului actualizate  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md**: Titlu modul, prezentare generală și toate antetele modulului actualizate  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab1/README.md**: Titlu, obiective de învățare, instrucțiuni de configurare și resurse actualizate  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab2/README.md**: Titlu, obiective de învățare, tabel gazde MCP și referințe încrucișate actualizate  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/README.md**: Titlu, insigne, prerechizite și resurse actualizate  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md**: Referințe la Agent Builder și link feedback actualizate  
- **10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/README.md**: Prerechizite și referințe de extensie actualizate  

---

## 11 Aprilie 2026  

### Lecție nouă, corecturi de documentație și actualizări de dependențe  

#### Conținut nou adăugat în curriculum  

**Modulul 05 - Subiecte Avansate**  
- **Lecția 5.17: Raționament Multi-Agent Adversarial cu MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ghid cuprinzător nou acoperind modelul de dezbatere adversarială pentru sisteme multi-agent  
  - Diagramă de arhitectură Mermaid: doi agenți → server MCP partajat → transcrierea dezbaterii → judecător → verdict  
  - Server comun de instrumente MCP (`web_search` + `run_python`) implementat în Python și TypeScript  
  - Prompts sistemice opuse (PENTRU / CONTRA / Judecător) cu cerințe explicite de utilizare a instrumentelor  
  - Orchestrator de dezbatere în Python, TypeScript și C# care gestionează runde și trasează argumentele  
  - Conectare MCP `ClientSession` pentru orchestrator la apeluri reale de instrumente  
  - Tabel de cazuri de utilizare (detectare halucinații, modelare amenințări, revizuire design API, verificare factuală, selecție tehnologică)  
  - Considerații de securitate: execuție izolată, validarea apelurilor de instrumente, limitarea ratei, jurnalizare audit  
  - Exercițiu structurat cu trei scenarii practice (revizuire cod, decizie arhitectură, moderare conținut)  

#### Corecturi de documentație  

**Modulul 03 - Început**  
- **05-stdio-server/README.md**: Exemplu incomplet de server stdio TypeScript corectat — adăugată instanțierea transportului lipsă (`new StdioServerTransport()`) și apelul `server.connect(transport)` pentru a corespunde exemplelor Python și .NET din aceeași secțiune  
- **14-sampling/README.md**: Corectură de typo — corectat `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`  

#### Actualizări curriculum  

**README.md principal**  
- Adăugat intrarea 5.17 (Raționament Multi-Agent Adversarial cu MCP) în tabelul curriculumului cu link direct către lecția nouă  

**05-AdvancedTopics/README.md**  
- Adăugat rândul pentru Lecția 5.17 în tabelul lecțiilor  

**study_guide.md**  
- Adăugat subiectul Raționament Multi-Agent Adversarial în harta mentală și descrierea prozei pentru Subiecte Avansate  

#### Corecturi de cod și securitate  

**Modulul 05 - Agenți Adversariale (`mcp-adversarial-agents`)**  
- **Corectură securitate — injecție de comandă**: Înlocuit interpolarea în shell a `execSync` cu `execFile` + `promisify` în instrumentul TypeScript `run_python`, eliminând suprafața de injecție de comenzi (codul controlat de LLM este acum transmis ca un element literal argv fără implicare shell)  
- **Conectare buclă instrument MCP**: Actualizat orchestratorul de dezbatere Python să utilizeze clientul `AsyncAnthropic` (înlocuind `Anthropic` sincron blocant), să transmită un `ClientSession` live direct pentru fiecare tură a agentului, să preia definițiile instrumentelor prin `session.list_tools()` la fiecare tură și să trimită blocurile `tool_use` prin `session.call_tool()` în buclă până când modelul emite un răspuns text final  

#### Actualizări de dependențe  

- Actualizat `hono` la versiunea 4.12.12 în mai multe pachete (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)  
- Actualizat `@hono/node-server` de la 1.19.11 la 1.19.13 în pachetele TypeScript  
- Actualizat `cryptography` de la 46.0.5 la 46.0.7 în pachetele Python (laburile 3 și 4 din 10-StreamliningAIWorkflows)  
- Actualizat `lodash` de la 4.17.23 la 4.18.1 în inspectorul 10-StreamliningAIWorkflows  

#### Traduceri  

- Sincronizat traduceri pentru peste 48 de limbi cu ultimele modificări sursă (actualizare i18n)  

---

## 5 Februarie 2026  

### Îmbunătățiri generale de validare și navigare în întregul depozit  

#### Conținut nou adăugat în curriculum  

**Modulul 03 - Început**  
- **12-mcp-hosts/README.md**: Ghid cuprinzător nou pentru configurarea gazdelor MCP  
  - Exemple de configurare pentru Claude Desktop, VS Code, Cursor, Cline, Windsurf  
  - Șabloane JSON pentru configurări pentru toate gazdele majore  
  - Tabel comparativ tipuri de transport (stdio, SSE/HTTP, WebSocket)  
  - Depanare a problemelor comune de conexiune  
  - Practici recomandate de securitate pentru configurarea gazdelor  

- **13-mcp-inspector/README.md**: Ghid nou de depanare pentru MCP Inspector  
  - Metode de instalare (npx, npm global, din sursă)  
  - Conectare la servere prin stdio și HTTP/SSE  
  - Testare unelte, resurse și fluxuri de lucru pentru prompts  
  - Integrare VS Code cu MCP Inspector  
  - Scenarii comune de depanare cu soluții  

**Modulul 04 - Implementare Practică**  
- **pagination/README.md**: Ghid nou de implementare a paginării  
  - Modele de paginare cu cursor în Python, TypeScript, Java  
  - Gestionare paginare la client  
  - Strategii de design de cursor (opac vs. structurat)  
  - Recomandări pentru optimizarea performanței  

**Modulul 05 - Subiecte Avansate**  
- **mcp-protocol-features/README.md**: Analiză detaliată a caracteristicilor protocolului  
  - Implementare notificări de progres  
  - Modele de anulare a cererilor  
  - Șabloane de resurse cu pattern-uri URI  
  - Gestionarea ciclului de viață al serverului  
  - Control nivel jurnalizare  
  - Modele de gestionare erori cu coduri JSON-RPC  

#### Corecturi navigare (peste 24 fișiere actualizate)  

**README-urile principale ale modulelor**  
 Acum link-uri atât către prima lecție, cât și către modulul următor  

**Sub-fișiere 02-Security**  
- Toate cele 5 documente suplimentare de securitate au acum navigare „Ce urmează”:  

**Fișiere 09-CaseStudy**  
- Toate fișierele de studii de caz au acum navigare secvențială:  

**Lab-uri 10-StreamliningAI**  
Adăugat secțiunea Ce urmează în prezentarea Modul 10 și Modul 11  

#### Corecturi cod și conținut  

**Actualizări SDK și dependențe**  
Corectat versiune openai goală la `^4.95.0`  
Actualizat SDK de la `^1.8.0` la `>=1.26.0`  
Actualizate versiunile mcp la `>=1.26.0`  

**Corecturi cod**  
Corectat model invalid `gpt-4o-mini` la `gpt-4.1-mini`  

**Corecturi conținut**  
Corectat link spart `READMEmd` → `README.md`, corectat antet curriculum `Module 1-3` → `Module 0-3`, corectat cale case-sensitive  
Eliminat conținut duplicat corupt al Studiului de Caz 5  

**Îmbunătățiri pentru ghidarea începătorilor**  
Adăugat introducere corectă, obiective de învățare și prerechizite pentru începători  

#### Actualizări curriculum  

**README.md principal**  
- Adăugate intrări 3.12 (Gazde MCP), 3.13 (Inspector MCP), 4.1 (Paginare), 5.16 (Caracteristici Protocol) în tabelul curriculumului  

**README-urile modulelor**  
Adăugate lecțiile 12 și 13 în lista de lecții  
Adăugată secțiunea Ghiduri Practice cu link la paginare  
Adăugate lecțiile 5.15 (Transport Personalizat) și 5.16 (Caracteristici Protocol)  

**study_guide.md**  
- Actualizată harta mentală cu toate subiectele noi: Configurare Gazde MCP, Inspector MCP, Strategii de Paginare, Analiză Detaliată Caracteristici Protocol  

## 28 ianuarie 2026  

### Revizuire conformitate specificații MCP 2025-11-25  

#### Îmbunătățiri Concepte de Bază (01-CoreConcepts/)  
- **Nouă primitivă Client - Roots**: Adăugat documentație cuprinzătoare despre primitiva client Roots, permițând serverelor să înțeleagă limitele sistemului de fișiere și permisiunile de acces  
- **Anotări pentru Unelte**: Adăugată documentație despre anotările de comportament ale uneltelor (`readOnlyHint`, `destructiveHint`) pentru decizii mai bune legate de execuția uneltelor  
- **Apelare unelte în Sampling**: Actualizată documentația Sampling pentru a include parametrii `tools` și `toolChoice` pentru invocarea uneltelor dictată de model în timpul cererilor de sampling  
- **Mod elicitation URL**: Adăugată documentație despre elicitația bazată pe URL pentru interacțiuni externe web inițiate de server  
- **Taskuri (Experimental)**: Nouă secțiune documentând caracteristica experimentală Tasks pentru înveliri de execuție durabilă și recuperare întârziată a rezultatelor  
- **Suport Iconițe**: Menționat că uneltele, resursele, șabloanele de resurse și prompts pot include acum iconițe ca metadate suplimentare  

#### Actualizări documentație  
- **README.md**: Adăugat referință la versiunea MCP Specification 2025-11-25 și explicație despre versionarea bazată pe dată  
- **study_guide.md**: Actualizat harta curriculum pentru a include Taskuri și Anotări Unelte în secțiunea Concepte de Bază; actualizat timestamp document  

#### Verificarea conformității Specificației  
- **Versiune protocol**: Verificat ca toate documentațiile referă corect MCP Specification 2025-11-25  
- **Aliniere arhitectură**: Confirmată acuratețea documentației pentru arhitectură în două straturi (Stratul de Date + Stratul de Transport)  
- **Documentația de primitive**: Validat primitivele serverului (Resurse, Prompts, Unelte) și primitivele clientului (Sampling, Elicitation, Logging, Roots)  
- **Mecanisme transport**: Verificat acuratețea documentației pentru transport STDIO și Streamable HTTP  
- **Ghid de securitate**: Confirmată alinierea cu cele mai bune practici MCP Security actuale  

#### Caracteristici-cheie MCP 2025-11-25 Documentate  
- **Descoperire OpenID Connect**: Descoperire server autentificare prin OIDC  
- **Metadate Client OAuth ID**: Mecanism recomandat pentru înregistrarea clientului  
- **JSON Schema 2020-12**: Dialect implicit pentru definițiile schemelor MCP  
- **Sistem de nivelare SDK**: Cerințe formalizate pentru suport și mentenanță a caracteristicilor SDK  
- **Structura guvernanței**: Grupuri de lucru și grupuri de interes formalizate în guvernanța MCP  

### Actualizare majoră documentație securitate (02-Security/)  

#### Integrare MCP Security Summit Workshop (Sherpa)  
- **Nouă resursă de training practică**: Adăugată integrare cuprinzătoare cu [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) în toate documentele de securitate  
- **Acoperire traseu expediție**: Documentat progresul complet de la Base Camp la Summit  
- **Aliniere OWASP**: Toate recomandările de securitate mapate acum pe riscurile OWASP MCP Azure Security Guide  

#### Integrare OWASP MCP Top 10  
- **Secțiune nouă**: Adăugat tabel cu primele 10 riscuri de securitate OWASP MCP cu atenuări Azure în README-ul principal de securitate  
- **Documentație bazată pe risc**: Actualizat mcp-security-controls-2025.md cu referințe la riscurile OWASP MCP pentru fiecare domeniu de securitate  
- **Arhitectură de referință**: Legături către arhitectura de referință OWASP MCP Azure Security Guide și modele de implementare  

#### Fișiere securitate actualizate  
- **README.md**: Adăugat prezentare Sherpa Workshop, tabel traseu expediție, sumar riscuri OWASP MCP Top 10 și secțiune training practic  
- **mcp-security-controls-2025.md**: Header actualizat februarie 2026, adăugat referințe riscuri OWASP (MCP01-MCP08), corectată inconsistență versiune specificație  
- **mcp-security-best-practices-2025.md**: Adăugate secțiuni resurse Sherpa și OWASP, actualizat timestamp  
- **mcp-best-practices.md**: Adăugată secțiune training practic cu linkuri Sherpa și OWASP  
- **azure-content-safety-implementation.md**: Adăugat referință OWASP MCP06, aliniere Sherpa Camp 3 și secțiune resurse suplimentare  

#### Linkuri noi de resurse adăugate  
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)  

- [OWASP MCP Ghid de Securitate Azure](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- Pagini individuale de risc OWASP MCP (MCP01-MCP10)

### Aliniere la Specifica MCP pe Curriculum 2025-11-25

#### Modul 03 - Începutul
- **Documentație SDK**: Adăugat Go SDK la lista oficială de SDK-uri; actualizate toate referințele SDK pentru alinierea la Specificația MCP 2025-11-25
- **Clarificarea Transportului**: Actualizate descrierile transportului STDIO și HTTP Streaming cu referințe explicite la specificație

#### Modul 04 - Implementare Practică
- **Actualizări SDK**: Adăugat Go SDK; lista SDK actualizată cu referință la versiunea specificației
- **Specificația Autorizării**: Actualizat linkul specificației MCP Authorization la versiunea curentă 2025-11-25

#### Modul 05 - Subiecte Avansate
- **Caracteristici Noi**: Adăugat notă despre noile caracteristici MCP Specificația 2025-11-25 (Task-uri, Anotări pentru Unelte, Mod URL pentru Elicitație, Rădăcini)
- **Resurse de Securitate**: Adăugat linkuri către OWASP MCP Top 10 și atelierul Sherpa în referințele suplimentare

#### Modul 06 - Contribuții Comunitare
- **Lista SDK**: Adăugat SDK-urile Swift și Rust; actualizat linkul specficării la 2025-11-25
- **Referință Specificație**: Actualizat linkul Specificației MCP către URL-ul direct al specificației

#### Modul 07 - Lecții din Adoptarea Timpurie
- **Actualizări Resurse**: Adăugat linkul MCP Specificația 2025-11-25 și OWASP MCP Top 10 în resurse suplimentare

#### Modul 08 - Cele Mai Bune Practici
- **Versiune Specificație**: Actualizată referința MCP Specificației la 2025-11-25
- **Resurse de Securitate**: Adăugat OWASP MCP Top 10 și atelierul Sherpa în referințele suplimentare

#### Modul 10 - Eficientizarea Fluxurilor de Lucru AI
- **Actualizare Emblema**: Modificat badge-ul versiunii MCP de la versiunea SDK (1.9.3) la versiunea specificației (2025-11-25)
- **Linkuri Resurse**: Actualizat linkul MCP Specificației; adăugat OWASP MCP Top 10

#### Modul 11 - Laboratoare Practice MCP Server
- **Referință Specificație**: Actualizat linkul MCP Specificației la versiunea 2025-11-25
- **Resurse de Securitate**: Adăugat OWASP MCP Top 10 în resursele oficiale

## 18 Decembrie 2025

### Actualizare Documentație de Securitate - MCP Specificația 2025-11-25

#### Cele Mai Bune Practici de Securitate MCP (02-Security/mcp-best-practices.md) - Actualizare Versiune Specificație
- **Actualizare Versiune Protocol**: Actualizat să facă referire la cea mai recentă Specificație MCP 2025-11-25 (lansată pe 25 noiembrie 2025)
  - Actualizate toate referințele la versiunea specificației de la 2025-06-18 la 2025-11-25
  - Actualizate referințele de dată din document de la 18 august 2025 la 18 decembrie 2025
  - Verificat ca toate URL-urile specificației indică documentația curentă
- **Validare Conținut**: Validare cuprinzătoare a celor mai bune practici de securitate conform celor mai recente standarde
  - **Soluții de Securitate Microsoft**: Verificată terminologia și linkurile curente pentru Prompt Shields (anterior "Detectarea riscului de Jailbreak"), Azure Content Safety, Microsoft Entra ID și Azure Key Vault
  - **Securitate OAuth 2.1**: Confirmată alinierea cu cele mai recente bune practici de securitate OAuth
  - **Standarde OWASP**: Validat că referințele OWASP Top 10 pentru LLM rămân actualizate
  - **Servicii Azure**: Verificate toate linkurile documentației Microsoft Azure și cele mai bune practici
- **Alinierea la Standardele de Securitate**: Toate standardele de securitate referențiate confirmate ca fiind actuale
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - Cele mai bune practici de securitate OAuth 2.1
  - Cadrele de securitate și conformitate Azure
- **Resurse Implementare**: Verificat toate linkurile și resursele de ghid pentru implementare
  - Modele de autentificare Azure API Management
  - Ghiduri de integrare Microsoft Entra ID
  - Managementul secretelor Azure Key Vault
  - Pipeline-uri DevSecOps și soluții de monitorizare

### Asigurarea Calității Documentației
- **Conformitate Specificații**: Asigurate toate cerințele obligatorii de securitate MCP (MUST/MUST NOT) aliniate cu ultima specificație
- **Actualizarea Resurselor**: Verificat toate linkurile externe către documentația Microsoft, standarde de securitate și ghiduri de implementare
- **Acoperirea celor Mai Bune Practici**: Confirmată acoperire cuprinzătoare a autentificării, autorizării, amenințări specifice AI, securitate lanțului de aprovizionare și modele enterprise

## 6 Octombrie 2025

### Extinderea Secțiunii Început – Utilizare Avansată Server & Autentificare Simplă

#### Utilizare Avansată Server (03-GettingStarted/10-advanced)
- **Capitol Nou Adăugat**: Ghid cuprinzător pentru utilizarea avansată a serverului MCP, acoperind arhitecturi atât regulate cât și la nivel jos.
  - **Server Regulă vs. Nivel Jos**: Comparație detaliată și exemple de cod în Python și TypeScript pentru ambele abordări.
  - **Design Bazat pe Handler**: Explicație a gestionării uneltelor/resurselor/prompturilor folosind handleri pentru implementări scalabile și flexibile.
  - **Modele Practice**: Scenarii reale unde modelele serverului la nivel jos sunt benefice pentru funcții avansate și arhitectură.

#### Autentificare Simplă (03-GettingStarted/11-simple-auth)
- **Capitol Nou Adăugat**: Ghid pas cu pas pentru implementarea autentificării simple în serverele MCP.
  - **Concepte Auth**: Explicație clară a autentificării versus autorizării și gestionarea acreditărilor.
  - **Implementare Basic Auth**: Modele de autentificare bazate pe middleware în Python (Starlette) și TypeScript (Express), cu exemple de cod.
  - **Progresie către Securitate Avansată**: Ghidare pentru începerea cu autentificare simplă și avansarea către OAuth 2.1 și RBAC, cu referințe la module de securitate avansate.

Aceste completări oferă ghidaj practic, hands-on pentru construirea unor implementări MCP server mai robuste, sigure și flexibile, realizând puntea între conceptele fundamentale și modelele avansate de producție.

## 29 Septembrie 2025

### Laboratoare de Integrare Baze de Date MCP Server - Cale Completă de Învățare Practică

#### 11-MCPServerHandsOnLabs - Curricula completă pentru integrare bază de date
- **Cale Completă de 13 Laboratoare**: Adăugat curriculum practic complet pentru construirea serverelor MCP gata pentru producție cu integrare bază de date PostgreSQL
  - **Implementare Reală**: Caz de utilizare de analiză Zava Retail demonstrând modele de nivel enterprise
  - **Progresie Structurată a Învățării**:
    - **Laboratoare 00-03: Fundamente** - Introducere, Arhitectură de Bază, Securitate & Multi-Tenant, Configurare Mediu
    - **Laboratoare 04-06: Construirea Serverului MCP** - Design Bază de Date & Schematizare, Implementare Server MCP, Dezvoltare Unealtă  
    - **Laboratoare 07-09: Funcții Avansate** - Integrare Căutare Semantică, Testare & Debugging, Integrare VS Code
    - **Laboratoare 10-12: Producție & Cele Mai Bune Practici** - Strategii de Lansare, Monitorizare & Observabilitate, Optimizare și Practici Recomandate
  - **Tehnologii Enterprise**: Framework FastMCP, PostgreSQL cu pgvector, Azure OpenAI embeddings, Azure Container Apps, Application Insights
  - **Caracteristici Avansate**: Securitate pe Rând (RLS), căutare semantică, acces multi-tenant la date, vector embeddings, monitorizare în timp real

#### Standardizarea Terminologiei - Conversia Modul în Laborator
- **Actualizare Completă Documentație**: Actualizat sistematic toate fișierele README din 11-MCPServerHandsOnLabs pentru a folosi terminologia „Laborator” în loc de „Modul”
  - **Capitole Secțiune**: Actualizat „Ce acoperă acest modul” în „Ce acoperă acest laborator” în toate cele 13 laboratoare
  - **Descrierea Conținutului**: Modificat „Acest modul oferă...” în „Acest laborator oferă...” în tot cuprinsul documentației
  - **Obiective de Învățare**: Actualizat „La finalul acestui modul...” în „La finalul acestui laborator...”
  - **Link-uri de Navigare**: Convertit toate referințele „Modul XX:” în „Laborator XX:” în referințe încrucișate și navigație
  - **Urmărire Finalizare**: Actualizat „După finalizarea acestui modul...” în „După finalizarea acestui laborator...”
  - **Referințe Tehnice Păstrate**: Menținute referințele modulelor Python în fișierele de configurație (de ex. `"module": "mcp_server.main"`)

#### Îmbunătățire Ghid de Studiu (study_guide.md)
- **Hartă Vizuală a Curriculumului**: Adăugată noua secțiune „11. Laboratoare Integrare Bază de Date” cu vizualizare cuprinzătoare a structurii laboratoarelor
- **Structura Repozitorului**: Actualizat de la zece la unsprezece secțiuni principale cu descriere detaliată a 11-MCPServerHandsOnLabs
- **Ghidare pentru Calea de Învățare**: Îmbunătățit instrucțiunile de navigare pentru secțiunile 00-11
- **Acoperire Tehnologică**: Adăugate detalii despre FastMCP, PostgreSQL, integrare servicii Azure
- **Rezultate de Învățare**: Subliată dezvoltarea serverelor gata pentru producție, modele de integrare bază de date și securitate enterprise

#### Îmbunătățire Structură README Principal
- **Terminologie Bazată pe Laborator**: Actualizat README.md principal din 11-MCPServerHandsOnLabs pentru a folosi constant structura „Laborator”
- **Organizare Cale de Învățare**: Progresie clară de la concepte fundamentale la implementare avansată și lansare în producție
- **Focus pe Scenarii Reale**: Accent pe învățare practică hands-on cu modele și tehnologii de nivel enterprise

### Îmbunătățiri Calitate & Consistență Documentație
- **Accent pe Învățare Practică**: Consolidat abordarea practică, bazată pe laboratoare, în întreaga documentație
- **Focus pe Modele Enterprise**: Subliniate implementările gata pentru producție și considerațiile de securitate enterprise
- **Integrarea Tehnologiei**: Acoperire completă a serviciilor Azure moderne și modelelor de integrare AI
- **Progresie Învățare**: Cale clară și structurată de la concepte de bază la lansare în producție

## 26 Septembrie 2025

### Îmbunătățirea Studiilor de Caz - Integrarea Registrului MCP GitHub

#### Studii de Caz (09-CaseStudy/) - Focus pe Dezvoltarea Ecosistemului
- **README.md**: Extindere majoră cu studiu de caz cuprinzător al Registrului MCP GitHub
  - **Studiu de Caz Registru MCP GitHub**: Studiu de caz nou și detaliat examină lansarea Registrului MCP GitHub în septembrie 2025
    - **Analiza Problemei**: Examinare detaliată a provocărilor de descoperire și implementare fragmentate a serverelor MCP
    - **Arhitectura Soluției**: Abordarea centralizată a registrului GitHub cu instalare VS Code cu un singur clic
    - **Impact de Afaceri**: Îmbunătățiri măsurabile în onboarding-ul și productivitatea dezvoltatorilor
    - **Valoare Strategică**: Focus pe implementarea modulară a agenților și interoperabilitatea uneltelor
    - **Dezvoltarea Ecosistemului**: Poziționarea ca platformă fundamentală pentru integrare agentică
  - **Structură Îmbunătățită a Studiului de Caz**: Actualizate toate cele șapte studii de caz cu formatare consistentă și descrieri cuprinzătoare
    - Azure AI Travel Agents: Accent pe orchestrarea multi-agent
    - Integrare Azure DevOps: Focus pe automatizarea fluxurilor de lucru
    - Recuperare Documentație în Timp Real: Implementare client consolă Python
    - Generator Interactiv Plan de Studiu: Aplicație web conversațională Chainlit
    - Documentație în Editor: Integrare VS Code și GitHub Copilot
    - Azure API Management: Modele de integrare API enterprise
    - Registrul MCP GitHub: Dezvoltarea ecosistemului și platforma comunității
  - **Concluzie Cuprinzătoare**: Secțiunea de concluzie rescrisă subliniind cele șapte studii de caz ce acoperă multiple dimensiuni ale implementării MCP
    - Integrare Enterprise, Orchestrare Multi-Agent, Productivitatea Dezvoltatorilor
    - Dezvoltarea Ecosistemului, Categorii pentru Aplicații Educaționale
    - Perspective îmbunătățite asupra modelelor arhitecturale, strategiilor de implementare și celor mai bune practici
    - Accent pe MCP ca protocol matur, gata pentru producție

#### Actualizări Ghid Studiu (study_guide.md)
- **Hartă Vizuală Curriculum**: Actualizat mindmap-ul pentru a include Registrul MCP GitHub în secțiunea Studii de Caz
- **Descriere Studii de Caz**: Îmbunătățit de la descrieri generice la defalcări detaliate a celor șapte studii de caz cuprinzătoare
- **Structură Repozitoriu**: Actualizată secțiunea 10 pentru a reflecta acoperirea completă a studiilor de caz cu detalii specifice de implementare
- **Integrare Changelog**: Adăugat intrare 26 septembrie 2025 documentând adăugarea Registrului MCP GitHub și îmbunătățirile studiilor de caz
- **Actualizări Dată**: Actualizat timestamp-ul din footer pentru a reflecta ultima revizuire (26 septembrie 2025)

### Îmbunătățiri Calitate Documentație
- **Îmbunătățire Consistență**: Standardizat formatarea și structura studiilor de caz în toate cele șapte exemple
- **Acoperire Cuprinzătoare**: Studiile de caz acoperă acum scenarii enterprise, productivitatea dezvoltatorului și dezvoltarea ecosistemului
- **Poziționare Strategică**: Accent îmbunătățit pe MCP ca platformă fundamentală pentru implementarea sistemelor agentice
- **Integrare Resurse**: Actualizat resursele suplimentare pentru a include linkul Registrului MCP GitHub

## 15 Septembrie 2025

### Extindere Subiecte Avansate - Transporturi Personalizate & Inginerie Contextuală

#### Transporturi Personalizate MCP (05-AdvancedTopics/mcp-transport/) - Ghid Nou Implementare Avansată
- **README.md**: Ghid complet pentru implementarea mecanismelor personalizate de transport MCP
  - **Transport Azure Event Grid**: Implementare cuprinzătoare a transportului serverless bazat pe evenimente
    - Exemple în C#, TypeScript și Python cu integrare Azure Functions
    - Modele arhitecturale event-driven pentru soluții MCP scalabile
    - Receptori webhook și gestionare mesaje push
  - **Transport Azure Event Hubs**: Implementare transport streaming cu throughput ridicat
    - Capacități streaming în timp real pentru scenarii cu latență redusă
    - Strategii de partiționare și management checkpoint
    - Grupare mesaje și optimizare performanță
  - **Modele Integrare Enterprise**: Exemple arhitecturale gata pentru producție
    - Procesare MCP distribuită pe mai multe Azure Functions
    - Arhitecturi hibride de transport care combină mai multe tipuri de transport
    - Strategii de durabilitate, fiabilitate și tratare erori mesaje
  - **Securitate & Monitorizare**: Integrare Azure Key Vault și modele observabilitate
    - Autentificare identitate gestionată și acces cu privilegii minime
    - Telemetrie Application Insights și monitorizare performanță
    - Circuit breakers și modele de toleranță la defecțiuni
  - **Framework-uri Testare**: Strategii cuprinzătoare pentru testarea transporturilor personalizate
    - Testare unități cu test doubles și framework-uri mocking
    - Testare integrare cu Azure Test Containers
    - Considerații pentru testarea performanței și încărcării

#### Inginerie Contextuală (05-AdvancedTopics/mcp-contextengineering/) - Disciplină AI Emergenta
- **README.md**: Explorare cuprinzătoare a ingineriei contextului ca domeniu emergent
  - **Principii de Bază**: Partajarea completă a contextului, conștientizarea deciziilor acțiunilor și gestionarea ferestrei contextuale

  - **Alinierea Protocolului MCP**: Cum designul MCP abordează provocările ingineriei contextului  
    - Limitările ferestrei de context și strategiile de încărcare progresivă  
    - Determinarea relevanței și recuperarea dinamică a contextului  
    - Gestionarea contextului multimodal și considerații de securitate  
  - **Abordări de implementare**: Arhitecturi single-threaded vs. multi-agent  
    - Tehnici de fragmentare și prioritizare a contextului  
    - Strategii de încărcare progresivă și compresie a contextului  
    - Abordări stratificate de context și optimizarea recuperării  
  - **Cadrul de măsurare**: Metrici emergente pentru evaluarea eficienței contextului  
    - Considerații privind eficiența inputului, performanța, calitatea și experiența utilizatorului  
    - Abordări experimentale pentru optimizarea contextului  
    - Analiza eșecurilor și metodologii de îmbunătățire  

#### Actualizări Navigație Curriculum (README.md)  
- **Structură Modul Îmbunătățită**: Tabelul curriculumului actualizat pentru a include noi subiecte avansate  
  - Au fost adăugate intrările Inginerie Context (5.14) și Transport Personalizat (5.15)  
  - Formatare și linkuri de navigare consistente în toate modulele  
  - Descrieri actualizate pentru a reflecta sfera curentă a conținutului  

### Îmbunătățiri Structură Director  
- **Standardizare Denumiri**: Redenumit "mcp transport" în "mcp-transport" pentru consistență cu alte foldere de subiecte avansate  
- **Organizare Conținut**: Toate folderele 05-AdvancedTopics respectă acum un model consistent de denumire (mcp-[topic])  

### Îmbunătățiri Calitate Documentație  
- **Aliniere Specificații MCP**: Toate conținuturile noi fac referire la actuala Specificație MCP 2025-06-18  
- **Exemple Multilingve**: Exemple complete de cod în C#, TypeScript și Python  
- **Focus Enterprise**: Modele gata de producție și integrare cu cloud Azure pe parcursul întregului conținut  
- **Documentație Vizuală**: Diagrame Mermaid pentru arhitectură și vizualizarea fluxurilor  

## 18 august 2025  

### Actualizare Completă Documentație - Standardele MCP 2025-06-18  

#### Practici Optime de Securitate MCP (02-Security/) - Modernizare Completă  
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Rescriere completă aliniată cu Specificația MCP 2025-06-18  
  - **Cerințe Obligatorii**: Adăugate cerințe explicite TREBUIE/TREBUIE NU din specificația oficială cu indicatori vizuali clari  
  - **12 Practici de Securitate Esențiale**: Restructurate din listă de 15 puncte în domenii de securitate cuprinzătoare  
    - Securitatea Token-urilor & Autentificare cu integrare furnizor extern de identitate  
    - Managementul Sesiunii & Securitatea Transportului cu cerințe criptografice  
    - Protecție Specifică AI cu integrare Microsoft Prompt Shields  
    - Control Acces & Permisiuni cu principiul privilegiului minim  
    - Siguranța Conținutului & Monitorizare cu integrare Azure Content Safety  
    - Securitatea Lanțului de Aprovizionare cu verificare completă a componentelor  
    - Securitatea OAuth & Prevenirea Atacurilor Confused Deputy cu implementare PKCE  
    - Răspuns la Incidente & Recuperare cu capabilități automate  
    - Conformitate & Guvernanță cu aliniere reglementară  
    - Controale Avansate de Securitate cu arhitectură zero trust  
    - Integrarea Ecosistemului de Securitate Microsoft cu soluții cuprinzătoare  
    - Evoluția Continuă a Securității cu practici adaptative  
  - **Soluții Microsoft de Securitate**: Ghiduri îmbunătățite pentru integrarea Prompt Shields, Azure Content Safety, Entra ID și GitHub Advanced Security  
  - **Resurse de Implementare**: Linkuri detaliate categorisite în Documentație MCP Oficială, Soluții Microsoft de Securitate, Standardele de Securitate și Ghiduri de Implementare  

#### Controale Avansate de Securitate (02-Security/) - Implementare Enterprise  
- **MCP-SECURITY-CONTROLS-2025.md**: Reformulare completă cu cadru de securitate la nivel enterprise  
  - **9 Domenii Comprehensive de Securitate**: Extins de la controale de bază la cadru detaliat enterprise  
    - Autentificare & Autorizare Avansată cu integrare Microsoft Entra ID  
    - Securitatea Token-urilor & Controale Anti-Passthrough cu validare completă  
    - Controale de Securitate pentru Sesiune cu prevenirea preluării ilegale  
    - Controale specifice AI cu prevenirea injecției de prompturi și otrăvirii instrumentelor  
    - Prevenirea Atacului Confused Deputy cu securitate proxy OAuth  
    - Securitatea Execuției Instrumentelor cu sandboxing și izolare  
    - Controale de Securitate a Lanțului de Aprovizionare cu verificarea dependențelor  
    - Controale de Monitorizare & Detectare cu integrare SIEM  
    - Răspuns la Incidente & Recuperare cu capabilități automate  
  - **Exemple de Implementare**: Adăugate blocuri detaliate de configurații YAML și exemple de cod  
  - **Integrarea Soluțiilor Microsoft**: Acoperire cuprinzătoare a serviciilor de securitate Azure, GitHub Advanced Security și managementul identității enterprise  

#### Securitate Subiecte Avansate (05-AdvancedTopics/mcp-security/) - Implementare Gata pentru Producție  
- **README.md**: Rescriere completă pentru implementarea securității enterprise  
  - **Aliniere Specificație Curentă**: Actualizat la Specificația MCP 2025-06-18 cu cerințe obligatorii de securitate  
  - **Autentificare Îmbunătățită**: Integrare Microsoft Entra ID cu exemple detaliate pentru .NET și Java Spring Security  
  - **Integrare Securitate AI**: Implementare Microsoft Prompt Shields și Azure Content Safety cu exemple detaliate Python  
  - **Mitigare Avansată a Amenințărilor**: Exemple complete de implementare pentru  
    - Prevenirea Atacului Confused Deputy cu PKCE și validarea consimțământului utilizatorului  
    - Prevenirea Passthrough-ului Token-urilor cu validarea audienței și management securizat al token-urilor  
    - Prevenirea deturnării sesiunii cu legare criptografică și analiză comportamentală  
  - **Integrare Securitate Enterprise**: Monitorizare Azure Application Insights, pipeline-uri de detecție a amenințărilor și securitate lanț de aprovizionare  
  - **Checklist de Implementare**: Controale clare obligatorii vs recomandate și beneficii ale ecosistemului de securitate Microsoft  

### Calitatea Documentației & Alinierea Standardelor  
- **Referințe Specificații**: Actualizate toate referințele la Specificația MCP curentă 2025-06-18  
- **Ecosistem Securitate Microsoft**: Ghiduri îmbunătățite pentru integrarea în toate documentațiile de securitate  
- **Implementare Practică**: Adăugate exemple detaliate de cod în .NET, Java și Python cu modele enterprise  
- **Organizare Resurse**: Categorisire cuprinzătoare a documentației oficiale, standardelor de securitate și ghidurilor de implementare  
- **Indicatori Vizuali**: Marcaje clare ale cerințelor obligatorii vs practici recomandate  


#### Concepte de Bază (01-CoreConcepts/) - Modernizare Completă  
- **Actualizare Versiune Protocol**: Actualizat pentru a face referire la Specificația MCP curentă 2025-06-18 cu versiune bazată pe dată (format YYYY-MM-DD)  
- **Rafinare Arhitectură**: Descrieri îmbunătățite ale Host-urilor, Clienților și Serverelor pentru a reflecta modelele actuale MCP  
  - Host-urile definite clar acum ca aplicații AI care coordonează multiple conexiuni client MCP  
  - Clienții descriși ca conectori de protocol menținând relații unu-la-unu cu serverele  
  - Serverele îmbunătățite cu scenarii de implementare local vs. remote  
- **Restructurare Primitive**: Revizuire completă a primitivelor server și client  
  - Primitive Server: Resurse (surse de date), Prompturi (șabloane), Instrumente (funcții executabile) cu explicații și exemple detaliate  
  - Primitive Client: Eșantionare (completări LLM), Elicitare (input utilizator), Logare (debugging/monitorizare)  
  - Actualizate cu pattern-uri curente de descoperire (`*/list`), recuperare (`*/get`) și execuție (`*/call`)  
- **Arhitectură Protocol**: Introducerea modelului arhitectural în două straturi  
  - Strat Date: Baza JSON-RPC 2.0 cu managementul ciclului de viață și primitive  
  - Strat Transport: STDIO (local) și HTTP streamabil cu SSE (transport remote)  
- **Cadrul de Securitate**: Principii cuprinzătoare de securitate incluzând consimțământ explicit al utilizatorului, protecția confidențialității datelor, siguranța execuției instrumentelor și securitatea stratului de transport  
- **Pattern-uri de Comunicare**: Mesaje de protocol actualizate pentru a arăta fluxurile de inițializare, descoperire, execuție și notificare  
- **Exemple de Cod**: Exemple multi-limba (.NET, Java, Python, JavaScript) reîmprospătate pentru a reflecta pattern-urile curente MCP SDK  

#### Securitate (02-Security/) - Revizuire Completă a Securității  
- **Aliniere Standard**: Aliniere completă cu cerințele de securitate din Specificația MCP 2025-06-18  
- **Evoluție Autentificare**: Documentată tranziția de la servere OAuth custom la delegare prin furnizor extern de identitate (Microsoft Entra ID)  
- **Analiză Amenințări Specifice AI**: Acoperire îmbunătățită a vectorilor moderni de atac AI  
  - Scenarii detaliate de atac prin injecție de prompturi cu exemple din lumea reală  
  - Mecanisme de otrăvire a instrumentelor și modele de atac "rug pull"  
  - Otrăvirea ferestrei de context și atacuri de confuzie a modelului  
- **Soluții Microsoft AI Security**: Acoperire cuprinzătoare a ecosistemului de securitate Microsoft  
  - AI Prompt Shields cu detectare avansată, evidențiere și tehnici de delimiter  
  - Modele de integrare Azure Content Safety  
  - GitHub Advanced Security pentru protecția lanțului de aprovizionare  
- **Mitigare Amenințări Avansate**: Controale detaliate de securitate pentru  
  - Preluarea sesiunii (session hijacking) cu scenarii specifice MCP și cerințe criptografice pentru ID-ul sesiunii  
  - Probleme Confused Deputy în scenarii proxy MCP cu cerințe explicite de consimțământ  
  - Vulnerabilități Passthrough Token cu controale obligatorii de validare  
- **Securitatea Lanțului de Aprovizionare**: Acoperire extinsă a lanțului de aprovizionare AI inclusiv modele fundamentale, servicii de embeddings, furnizori de context și API-uri terțe  
- **Securitate Fundamentală**: Integrare îmbunătățită cu modele de securitate enterprise incluzând arhitectura zero trust și ecosistemul de securitate Microsoft  
- **Organizare Resurse**: Categorisire cuprinzătoare a linkurilor către resurse după tip (Documentație Oficială, Standarde, Cercetare, Soluții Microsoft, Ghiduri de Implementare)  

### Îmbunătățiri Calitate Documentație  
- **Obiective de Învățare Structurate**: Îmbunătățirea obiectivelor de învățare cu rezultate specifice și acționabile  
- **Referințe Înnodate**: Adăugate linkuri între subiecte de securitate și concepte de bază conexe  
- **Informații Curente**: Actualizate toate referințele de dată și linkurile de specificații la standardele curente  
- **Ghiduri de Implementare**: Adăugate instrucțiuni specifice și acționabile de implementare în ambele secțiuni  

## 16 iulie 2025  

### Îmbunătățiri README și Navigație  
- Remodelare completă a navigației curriculumului în README.md  
- Înlocuite tag-urile `<details>` cu format tabelar mai accesibil  
- Create opțiuni alternative de layout în noul folder "alternative_layouts"  
- Adăugate exemple de navigație pe bază de carduri, taburi și acordeon  
- Actualizată secțiunea structura depozitului pentru a include toate fișierele cele mai recente  
- Îmbunătățită secțiunea „Cum să folosești acest curriculum” cu recomandări clare  
- Actualizate linkurile de specificație MCP pentru a indica URL-urile corecte  
- Adăugat secțiunea Inginerie Context (5.14) în structura curriculumului  

### Actualizări Ghid de Studiu  
- Ghidul de studiu revizuit complet pentru a se alinia cu structura curentă a depozitului  
- Adăugate secțiuni noi pentru Clienți MCP și Instrumente, și Servere MCP populare  
- Actualizat Harta Vizuală a Curriculumului pentru a reflecta corect toate subiectele  
- Îmbunătățite descrierile subiectelor avansate pentru a acoperi toate domeniile specializate  
- Actualizată secțiunea Studii de Caz pentru a reflecta exemple reale  
- Adăugat acest jurnal extins al modificărilor  

### Contribuții Comunitare (06-CommunityContributions/)  
- Adăugate informații detaliate despre serverele MCP pentru generarea de imagini  
- Adăugată secțiune cuprinzătoare despre folosirea Claude în VSCode  
- Adăugate instrucțiuni pentru setup și utilizarea clientului terminal Cline  
- Actualizată secțiunea client MCP pentru a include toate opțiunile populare de client  
- Îmbunătățite exemplele de contribuție cu mostre de cod mai precise  

### Subiecte Avansate (05-AdvancedTopics/)  
- Organizate toate folderele de subiecte specializate cu denumire consistentă  
- Adăugate materiale și exemple de inginerie a contextului  
- Adăugată documentație pentru integrarea agentului Foundry  
- Îmbunătățită documentația de integrare a securității Entra ID  

## 11 iunie 2025  

### Creare Inițială  
- Lansată prima versiune a curriculumului MCP pentru Începători  
- Creată structura de bază pentru toate cele 10 secțiuni principale  
- Implementată Harta Vizuală a Curriculumului pentru navigare  
- Adăugate proiecte de exemplu inițiale în mai multe limbaje de programare  

### Început (03-GettingStarted/)  
- Crearea primelor exemple de implementare server  
- Adăugate ghiduri de dezvoltare client  
- Include instrucțiuni de integrare client LLM  
- Adăugată documentație de integrare VS Code  
- Implementate exemple de server Server-Sent Events (SSE)  

### Concepte de Bază (01-CoreConcepts/)  
- Adăugată explicație detaliată a arhitecturii client-server  
- Creată documentație despre componentele cheie ale protocolului  
- Documentate pattern-uri de mesagerie în MCP  

## 23 mai 2025  

### Structura Depozitului  
- Inițializat depozitul cu structura folderelor de bază  
- Create fișiere README pentru fiecare secțiune majoră  
- Configurat infrastructura de traducere  
- Adăugate resurse de imagini și diagrame  

### Documentație  
- Creat README.md inițial cu prezentarea curriculumului  
- Adăugat CODE_OF_CONDUCT.md și SECURITY.md  
- Configurat SUPPORT.md cu ghiduri pentru solicitarea de ajutor  
- Creat structura preliminară a ghidului de studiu  

## 15 aprilie 2025  

### Planificare și Cadrul de Lucru  
- Planificare inițială pentru curriculumul MCP pentru Începători  
- Definit obiectivele de învățare și audiența țintă  
- Schițată structura de 10 secțiuni a curriculumului  
- Dezvoltat cadru conceptual pentru exemple și studii de caz  
- Creat prototipuri inițiale pentru conceptele cheie  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->