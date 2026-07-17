# AGENTS.md

## Prezentare generală a proiectului

**MCP pentru Începători** este un curriculum educațional open-source pentru învățarea Model Context Protocol (MCP) - un cadru standardizat pentru interacțiunile între modelele AI și aplicațiile client. Acest depozit oferă materiale de învățare cuprinzătoare, cu exemple practice de cod în mai multe limbaje de programare.

### Tehnologii cheie

- **Limbaje de programare**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework-uri & SDK-uri**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Baze de date**: PostgreSQL cu extensia pgvector
- **Platforme Cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Unelte de build**: npm, Maven, pip, Cargo
- **Documentație**: Markdown cu traducere automată multi-limbaj (peste 48 de limbi)

### Arhitectură

- **11 Module de bază (00-11)**: Parcurs de învățare secvențial de la elementele fundamentale la subiecte avansate
- **Laboratoare practice**: Exerciții practice cu cod complet de soluție în mai multe limbaje
- **Proiecte exemplu**: Implementări funcționale de server și client MCP
- **Sistem de traducere**: Flux de lucru automatizat GitHub Actions pentru suport multi-limbaj
- **Resurse de imagini**: Director centralizat cu imagini și versiuni traduse

## Comenzi de configurare

Acesta este un depozit axat pe documentație. Majoritatea configurărilor se realizează în proiectele exemplu și laboratoare individuale.

### Configurarea depozitului

```bash
# Clonează depozitul
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Lucrul cu proiecte exemplu

Proiectele exemplu se află în:
- `03-GettingStarted/samples/` - Exemple specifice limbajelor
- `03-GettingStarted/01-first-server/solution/` - Implementări server inițiale
- `03-GettingStarted/02-client/solution/` - Implementări client
- `11-MCPServerHandsOnLabs/` - Laboratoare cu integrare completă a bazei de date

Fiecare proiect exemplu conține propriile instrucțiuni de configurare:

#### Proiecte TypeScript/JavaScript
```bash
cd <project-directory>
npm install
npm start
```

#### Proiecte Python
```bash
cd <project-directory>
pip install -r requirements.txt
# sau
pip install -e .
python main.py
```

#### Proiecte Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Flux de lucru pentru dezvoltare

### Pregătire pentru MCP 7-28

#### Lista de verificare pentru pregătirea depozitului

- [x] **Claritate pentru contributori noi**: Acest fișier definește scopul depozitului,
  structura, regulile de contribuție și căile de configurare exemple.
- [x] **Comenzi exacte pentru build/test/lint**:
  - Lint pentru documentația depozitului:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit pentru tiparele linkurilor în documentație:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validare exemple TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validare exemple Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validare exemple Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Un flux de lucru realist care poate deveni un instrument MCP**:
  `validate_curriculum_change`
- [x] **Intrările/ieșirile sunt explicite** (vezi specificația mai jos).
- [x] **Permisiunile și modurile de eșec sunt documentate** (vezi specificația mai jos).
- [x] **Testabilitatea CI este explicită** (comenzi determinate, coduri de ieșire explicite,
  și ieșiri lizibile de mașină).

#### Flux de lucru candidat pentru instrument MCP: `validate_curriculum_change`

##### Scop

Validarea modificărilor documentației curriculumului și starea codului exemplar reprezentativ
înainte de îmbinare.

##### Intrări

- `changed_paths: string[]` (obligatoriu) - căile relative modificate în PR.
- `run_docs_lint: boolean` (implicit `true`)
- `run_links_audit: boolean` (implicit `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (implicit toate `false`)

##### Ieșiri

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Permisiuni

- Citește fișierele din spațiul de lucru și scrie artefacte generate de unelte (ex: rapoarte lint,
  jurnale de test), doar atât; nu scrie în `translations/` sau
  `translated_images/`.
- Execută comenzi shell locale.
- Acces opțional la rețea doar pentru restaurarea pachetelor (`npm ci`,
  `python -m pip install`, rezolvarea dependențelor `mvn`).
- Fără permisiunea de a face push, merge sau modifica `translations/` sau
  `translated_images/`.

##### Moduri de eșec

- `E_NO_INPUT_PATHS`: `changed_paths` este gol.
- `E_INVALID_PATH`: calea de intrare iese din rădăcina depozitului.
- `E_LINT_FAILED`: lint markdown termină cu cod non-zero.
- `E_LINK_AUDIT_FAILED`: comanda audit link termină cu cod non-zero.
- `E_SAMPLE_TEST_FAILED`: testul/build-ul exemplului termină cu cod non-zero.
- `E_TIMEOUT`: comanda a depășit timpul de așteptare configurat.

##### Contract CI recomandat

Pentru automatizarea validării, configurează un job CI care:

- Se declanșează la pull request-uri care ating `*.md`, cod exemplu sau acest fișier.
- Rulează comenzile exacte de mai sus.
- Păstrează jurnalele ca artefacte.
- Eșuează job-ul la orice cod de ieșire non-zero.

#### Dacă livrezi un server MCP din acest depozit

- [ ] Citește changelog-ul draft pentru MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Rulează serverul tău cu SDK betas:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Elimină presupunerile de sesiune și handshake; tratează fiecare cerere ca
  fiind independentă:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Trimite headerele `Mcp-Method` și `Mcp-Name` pentru cererile HTTP brute:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Auditează codurile de eroare hardcodate (`missing resource` mutat de la `-32002` la `-32602`).
- [ ] Marchează și planifică migrarea pentru rădăcini, eșantionare și
  jurnalizare învechite:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrează de pe API-ul experimental `2025-11-25` Tasks:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Revizuiește autorizarea pentru întăriri OAuth și OpenID Connect:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Structura documentației

- **Module 00-11**: Conținutul principal al curriculumului în ordine secvențială
- **translations/**: Versiuni specifice limbajelor (generate automat, nu edita direct)
- **translated_images/**: Versiuni localizate ale imaginilor (generate automat)
- **images/**: Imagini și diagrame sursă

### Cum să faci modificări în documentație

1. Editează doar fișierele markdown în limba engleză din directoarele modulelor rădăcină (00-11)
2. Actualizează imaginile din directorul `images/` dacă este nevoie
3. Acțiunea GitHub co-op-translator va genera automat traducerile
4. Traducerile sunt regenerate la push pe ramura main

### Lucrul cu traducerile

- **Traducere automată**: Fluxul de lucru GitHub Actions gestionează toate traducerile
- **Nu edita manual** fișierele din directorul `translations/`
- Metadatele traducerii sunt încorporate în fiecare fișier tradus
- Limbi suportate: peste 48 de limbi, inclusiv arabă, chineză, franceză, germană, hindi, japoneză, coreeană, portugheză, rusă, spaniolă și multe altele

## Instrucțiuni de testare

### Validarea documentației

Deoarece acesta este în principal un depozit de documentație, testarea se concentrează pe:

1. **Audit pentru tiparele de link**: Listează linkurile Markdown pentru revizuire

   ```bash
   # Listează linkuri Markdown (audit de tipar)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validarea exemplelor de cod**: Testează că exemplele de cod compilează/rulează

   ```bash
   # Navighează la un eșantion specific și rulează testele acestuia
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Linting Markdown**: Verifică consistența formatării

   ```bash
   # Folosește markdownlint dacă este necesar
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testarea proiectelor exemplu

Fiecare exemplu specific limbajului include propria abordare pentru testare:

#### TypeScript/JavaScript
```bash
npm test
npm run build
```

#### Python
```bash
pytest
python -m pytest tests/
```

#### Java
```bash
mvn test
mvn verify
```

## Ghid stil cod

### Stil documentație

- Folosește un limbaj clar, prietenos pentru începători
- Include exemple de cod în mai multe limbaje, unde este cazul
- Urmează cele mai bune practici pentru markdown:
  - Folosește antete stil ATX (`#`)
  - Folosește blocuri de cod delimitate cu identificatori de limbaj
  - Include text alternativ descriptiv pentru imagini
  - Menține lungimea liniilor rezonabilă (fără limită rigidă, dar cu bun simț)

### Stil exemple cod

#### TypeScript/JavaScript
- Folosește module ES (`import`/`export`)
- Respectă convențiile modului strict TypeScript
- Include adnotări de tip
- Țintește ES2022

#### Python
- Urmează liniile de stil PEP 8
- Folosește indicii de tip acolo unde este cazul
- Include docstring-uri pentru funcții și clase
- Folosește funcționalități moderne Python (3.8+)

#### Java
- Urmează convențiile Spring Boot
- Folosește facilitățile Java 21
- Urmează structura standard a proiectului Maven
- Include comentarii Javadoc

### Organizarea fișierelor

```
<module-number>-<ModuleName>/
├── README.md              # Main module content
├── samples/               # Code examples (if applicable)
│   ├── typescript/
│   ├── python/
│   ├── java/
│   └── ...
└── solution/              # Complete working solutions
    └── <language>/
```

## Build și implementare

### Implementarea documentației

Depozitul folosește GitHub Pages sau similare pentru găzduirea documentației (dacă este cazul). Modificările în ramura main declanșează:

1. Fluxul de lucru de traducere (`.github/workflows/co-op-translator.yml`)
2. Traducerea automată a tuturor fișierelor markdown în engleză
3. Localizarea imaginilor după cum este necesar

### Nu este necesar procesul de build

Acest depozit conține în principal documentație markdown. Nu este necesar pas de compilare sau build pentru conținutul principal al curriculumului.

### Implementarea proiectelor exemplu

Proiectele exemplu individuale pot avea instrucțiuni de implementare:
- Vezi `03-GettingStarted/09-deployment/` pentru ghidaj de implementare server MCP
- Exemple de implementare Azure Container Apps în `11-MCPServerHandsOnLabs/`

## Ghid de contribuție

### Procesul pull request-ului

1. **Fork și clonează**: Fork-ează depozitul și clonează fork-ul local
2. **Creează o ramură**: Folosește nume descriptive de ramură (ex: `fix/typo-module-3`, `add/python-example`)
3. **Fă modificări**: Editează doar fișierele markdown în limba engleză (nu traducerile)
4. **Testează local**: Verifică dacă markdown-ul se redă corect
5. **Trimite PR**: Folosește titluri și descrieri clare pentru PR
6. **CLA**: Semnează Microsoft Contributor License Agreement când ți se solicită

### Format de titlu PR

Folosește titluri clare și descriptive:
- `[Module XX] Descriere scurtă` pentru modificări specifice modulului
- `[Samples] Descriere` pentru schimbările de cod exemplar
- `[Docs] Descriere` pentru actualizări generale ale documentației

### Ce să contribuiți

- Corecturi de bug-uri în documentație sau exemple cod
- Exemple noi de cod în limbaje suplimentare
- Clarificări și îmbunătățiri ale conținutului existent
- Studii de caz noi sau exemple practice
- Raportări de probleme pentru conținut neclar sau incorect

### Ce să NU faceți

- Nu edita direct fișierele din directorul `translations/`
- Nu edita directorul `translated_images/`
- Nu adăuga fișiere binare mari fără discuție prealabilă
- Nu modifica fișierele fluxului de traducere fără coordonare

## Note suplimentare

### Întreținerea depozitului

- **Changelog**: Toate schimbările semnificative sunt documentate în `changelog.md`
- **Ghid de studiu**: Folosește `study_guide.md` pentru navigarea curriculumului
- **Șabloane pentru issue-uri**: Folosește șabloanele GitHub pentru raportarea bug-urilor și cereri de funcționalități
- **Cod de conduită**: Toți contribuitorii trebuie să respecte Codul de conduită Microsoft Open Source

### Parcurs de învățare

Urmează modulele în ordine secvențială (00-11) pentru învățare optimă:
1. **00-02**: Fundamente (Introducere, Concepe de bază, Securitate)
2. **03**: Început cu implementare practică
3. **04-05**: Implementare practică și subiecte avansate
4. **06-10**: Comunitate, cele mai bune practici și aplicații reale
5. **11**: Laboratoare complexe de integrare a bazei de date (13 laboratoare secvențiale)

### Resurse de suport

- **Documentație**: https://modelcontextprotocol.io/
- **Specificare**: https://spec.modelcontextprotocol.io/
- **Comunitate**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Serverul Discord Microsoft Foundry
- **Cursuri conexe**: Vezi README.md pentru alte trasee de învățare Microsoft

### Probleme frecvente

**Î: PR-ul meu eșuează la verificarea traducerii**
R: Asigură-te că ai editat doar fișierele markdown în limba engleză din directoarele modulului rădăcină, nu versiunile traduse.

**Î: Cum adaug o limbă nouă?**
R: Suportul pentru limbi este administrat prin fluxul de lucru co-op-translator. Deschide un issue pentru a discuta adăugarea de limbi noi.

**Î: Exemplele de cod nu funcționează**

R: Asigură-te că ai urmărit instrucțiunile de configurare din README-ul exemplului specific. Verifică că ai instalate versiunile corecte ale dependențelor.

**Î: Imaginile nu se afișează**
R: Verifică dacă căile către imagini sunt relative și folosesc slash-uri înainte. Imaginile trebuie să fie în directorul `images/` sau în `translated_images/` pentru versiunile localizate.

### Considerații privind performanța

- Fluxul de lucru pentru traducere poate dura câteva minute pentru a se finaliza
- Imaginile mari trebuie optimizate înainte de a fi comise
- Păstrează fișierele markdown individuale concentrate și de dimensiuni rezonabile
- Folosește legături relative pentru o portabilitate mai bună

### Guvernanța proiectului

Acest proiect urmează practicile open source Microsoft:
- Licență MIT pentru cod și documentație
- Codul de conduită Open Source Microsoft
- CLA necesară pentru contribuții
- Probleme de securitate: Urmează ghidurile din SECURITY.md
- Suport: Consultă SUPPORT.md pentru resurse de ajutor

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->