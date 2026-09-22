# AGENTS.md

## Prezentare generală a proiectului

**MCP pentru Începători** este un curriculum educațional open-source pentru învățarea Model Context Protocol (MCP) - un cadru standardizat pentru interacțiunile între modele AI și aplicațiile client. Acest depozit oferă materiale de învățare cuprinzătoare cu exemple practice de cod în mai multe limbaje de programare.

### Tehnologii cheie

- **Limbaje de programare**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework-uri și SDK-uri**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Baze de date**: PostgreSQL cu extensia pgvector
- **Platforme cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Instrumente de construcție**: npm, Maven, pip, Cargo
- **Documentație**: Markdown cu traducere automată multilingvă (peste 48 de limbi)

### Arhitectură

- **11 Module de bază (00-11)**: Parcurs de învățare secvențial de la elementele fundamentale la subiecte avansate
- **Laboratoare practice**: Exerciții practice cu cod complet de soluție în mai multe limbaje
- **Proiecte demonstrative**: Implementări funcționale server și client MCP
- **Sistem de traducere**: Flux de lucru automatizat GitHub Actions pentru suport multilingv
- **Resurse imagine**: Director centralizat cu imagini cu versiuni traduse

## Comenzi de configurare

Acesta este un depozit focalizat pe documentație. Cele mai multe configurări se fac în proiectele și laboratoarele demonstrative individuale.

### Configurarea depozitului

```bash
# Clonează depozitul
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Lucrul cu proiectele demonstrative

Proiectele demonstrative se găsesc în:
- `03-GettingStarted/samples/` - Exemple specifice limbajului
- `03-GettingStarted/01-first-server/solution/` - Primele implementări de server
- `03-GettingStarted/02-client/solution/` - Implementări client
- `11-MCPServerHandsOnLabs/` - Laboratoare cu integrare completă a bazei de date

Fiecare proiect demonstrativ conține propriile instrucțiuni de configurare:

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

## Flux de lucru în dezvoltare

### Pregătirea MCP 7-28

#### Lista de verificare pentru pregătirea depozitului

- [x] **Claritate pentru contribuitori noi**: Acest fișier definește scopul depozitului,
  structura, regulile de contribuție și căile de configurare pentru exemple.
- [x] **Comenzi build/test/lint cu flag-uri exacte**:
  - Lint pentru documentația din depozit:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit model link-uri documentare:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validare exemplu TypeScript:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validare exemplu Python:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validare exemplu Java:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Un flux de lucru realist care poate deveni un instrument MCP**:
  `validate_curriculum_change`
- [x] **Intrările/ieșirile sunt explicite** (vezi specificația mai jos).
- [x] **Permisiunile și modurile de eșec sunt documentate** (vezi specificația mai jos).
- [x] **Testabilitatea în CI este explicită** (comenzi deterministe, coduri de ieșire explicite,
  și ieșiri lizibile de mașină).

#### Flux de lucru candidat pentru instrument MCP: `validate_curriculum_change`

##### Scop

Validarea modificărilor documentației curriculumului și sănătatea codului demonstrativ reprezentativ
înainte de fuziune.

##### Intrări

- `changed_paths: string[]` (obligatoriu) - căi relative modificate în PR.
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

- Citire fișiere din workspace și scriere artefacte generate de instrument (ex. rapoarte lint,
  jurnale de test), fără scrieri în `translations/` sau
  `translated_images/`.
- Execuție comenzi shell locale.
- Acces opțional la rețea doar pentru restaurarea pachetelor (`npm ci`,
  `python -m pip install`, rezolvarea dependențelor `mvn`).
- Fără permisiune de push, merge, sau modificare în `translations/` sau
  `translated_images/`.

##### Moduri de eșec

- `E_NO_INPUT_PATHS`: `changed_paths` este gol.
- `E_INVALID_PATH`: calea de intrare iese din rădăcina depozitului.
- `E_LINT_FAILED`: comanda markdown lint se termină cu cod diferit de zero.
- `E_LINK_AUDIT_FAILED`: comanda audit link-uri se termină cu cod diferit de zero.
- `E_SAMPLE_TEST_FAILED`: test/build exemplu se termină cu cod diferit de zero.
- `E_TIMEOUT`: comanda a depășit timpul maxim configurat.

##### Contract recomandat CI

Pentru automatizarea validării, configurați un job CI care:

- Se declanșează la pull request-uri ce modifică `*.md`, cod demonstrativ sau acest fișier.
- Rulează comenzile exacte enumerate mai sus.
- Păstrează jurnalele ca artefacte.
- Eșuează job-ul la orice cod de ieșire diferit de zero.

#### Dacă lansați un server MCP din acest depozit

- [ ] Citiți changelog-ul final MCP `2026-07-28`:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Verificați dacă versiunea SDK aleasă suportă MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Elimină presupunerile despre sesiune și handshake; tratează fiecare cerere ca
  pe cont propriu:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Trimite anteturile `Mcp-Method` și `Mcp-Name` pentru cereri HTTP brute:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Auditați codurile de eroare hardcodate (`missing resource` mutat de la `-32002` la `-32602`).
- [ ] Migrați din Roots, Sampling, Logging și Dynamic Client
  Registration învechite:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrați de pe API-ul experimental al sarcinilor `2025-11-25`:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Revizuiți autorizarea pentru întărirea OAuth și OpenID Connect:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Structura documentației

- **Modulele 00-11**: Conținutul de bază al curriculumului în ordine secvențială
- **translations/**: Versiuni specifice limbajelor (generate automat, să nu se editeze direct)
- **translated_images/**: Versiuni localizate ale imaginilor (generate automat)
- **images/**: Imagini sursă și diagrame

### Modificarea documentației

1. Editați doar fișierele markdown în limba engleză din directoarele modulelor rădăcină (00-11)
2. Actualizați imaginile din directorul `images/` dacă este necesar
3. Workflow-ul GitHub Action co-op-translator va genera automat traducerile
4. Traducerile sunt regenerate la push pe ramura principală

### Lucrul cu traducerile

- **Traducere automată**: Workflow-ul GitHub Actions gestionează toate traducerile
- **Nu editați manual** fișierele din directorul `translations/`
- Metadatele traducerii sunt încorporate în fiecare fișier tradus
- Limbaje suportate: peste 48, inclusiv arabă, chineză, franceză, germană, hindi, japoneză, coreeană, portugheză, rusă, spaniolă și multe altele

## Instrucțiuni de testare

### Validarea documentației

Deoarece este în principal un depozit de documentație, testarea se concentrează pe:

1. **Audit model link-uri**: Listează link-urile Markdown pentru revizuire

   ```bash
   # Listează link-urile Markdown (audit șablon)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validare exemple de cod**: Testează dacă exemplele de cod compilează/funcționează

   ```bash
   # Navigați la un eșantion specific și rulați testele acestuia
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown linting**: Verifică consistența formatării

   ```bash
   # Folosește markdownlint dacă este necesar
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testarea proiectelor demonstrative

Fiecare exemplu specific limbajului include propria strategie de testare:

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

## Ghid de stil pentru cod

### Stil documentație

- Folosiți un limbaj clar, prietenos cu începătorii
- Includeți exemple de cod în mai multe limbaje unde este cazul
- Urmați cele mai bune practici Markdown:
  - Folosiți antete stil ATX (`#` sintaxă)
  - Folosiți blocuri de cod delimitate cu identificatori de limbaj
  - Includeți texte alternative descriptive pentru imagini
  - Mențineți lungimile liniilor rezonabile (fără limită strictă, dar fiți rezonabili)

### Stil pentru exemple de cod

#### TypeScript/JavaScript
- Folosiți module ES (`import`/`export`)
- Urmați convențiile modului strict TypeScript
- Includeți adnotări de tip
- Țintiți ES2022

#### Python
- Urmați ghidul de stil PEP 8
- Folosiți sugestii de tip unde este cazul
- Includeți docstring-uri pentru funcții și clase
- Folosiți caracteristici moderne Python (3.8+)

#### Java
- Urmați convențiile Spring Boot
- Folosiți facilități Java 21
- Urmați structura standard de proiect Maven
- Includeți comentarii Javadoc

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

Depozitul folosește GitHub Pages sau similar pentru găzduirea documentației (dacă este cazul). Modificările pe ramura principală declanșează:

1. Fluxul de traducere (`.github/workflows/co-op-translator.yml`)
2. Traducerea automată a tuturor fișierelor markdown în limba engleză
3. Localizarea imaginilor după necesitate

### Nu este necesar proces de build

Acest depozit conține în principal documentație markdown. Nu este necesar niciun pas de compilare sau build pentru conținutul de bază al curriculumului.

### Implementarea proiectelor demonstrative

Proiectele demonstrative individuale pot conține instrucțiuni de implementare:
- Vezi `03-GettingStarted/09-deployment/` pentru ghid de implementare server MCP
- Exemple de implementare Azure Container Apps în `11-MCPServerHandsOnLabs/`

## Ghid de contribuție

### Procesul pentru Pull Request

1. **Fork și clonare**: Fă fork la depozit și clonează-l local
2. **Creează o ramură**: Folosește nume descriptive ale ramurilor (ex. `fix/typo-module-3`, `add/python-example`)
3. **Fă modificări**: Editează doar fișierele markdown în limba engleză (nu traducerile)
4. **Testează local**: Verifică dacă markdown-ul se redă corect
5. **Trimite PR**: Folosește titluri și descrieri clare pentru PR
6. **CLA**: Semnează Acordul de Contribuitor Microsoft când ți se cere

### Formatul titlurilor PR

Folosește titluri clare și descriptive:
- `[Module XX] Descriere scurtă` pentru modificări specifice modulului
- `[Samples] Descriere` pentru modificări la codul demonstrativ
- `[Docs] Descriere` pentru actualizări generale ale documentației

### Ce să contribui

- Corecturi de erori în documentație sau cod demonstrativ
- Exemple noi de cod în alte limbaje
- Clarificări și îmbunătățiri ale conținutului existent
- Studii de caz noi sau exemple practice
- Raportări de probleme pentru conținut neclar sau incorect

### Ce să NU faci

- Nu edita direct fișierele din directorul `translations/`
- Nu edita directorul `translated_images/`
- Nu adăuga fișiere binare mari fără discuție prealabilă
- Nu modifica fișierele workflow-ului de traducere fără coordonare

## Note suplimentare

### Mentenanța depozitului

- **Changelog**: Toate schimbările importante sunt documentate în `changelog.md`
- **Ghid de studiu**: Folosește `study_guide.md` pentru o privire generală asupra navigării curriculumului
- **Șabloane pentru issue-uri**: Folosește șabloane GitHub pentru rapoarte de bug-uri și cereri de funcționalități
- **Cod de conduită**: Toți contribuitorii trebuie să respecte Codul de Conduită Open Source Microsoft

### Parcurs de învățare

Urmează modulele în ordine secvențială (00-11) pentru un învățământ optim:
1. **00-02**: Fundamente (Introducere, Concepte de bază, Securitate)
2. **03**: Introducere practică cu implementare directă
3. **04-05**: Implementare practică și subiecte avansate
4. **06-10**: Comunitate, bune practici și aplicații reale
5. **11**: Laboratoare complexe de integrare a bazei de date (13 laboratoare secvențiale)

### Resurse de suport

- **Documentație**: https://modelcontextprotocol.io/
- **Specificație**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Comunitate**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: serverul Microsoft Foundry Discord
- **Cursuri conexe**: Vezi README.md pentru alte parcursuri de învățare Microsoft

### Probleme frecvente

**Î: PR-ul meu eșuează la verificarea traducerii**
R: Asigură-te că ai editat doar fișierele markdown în limba engleză din directoarele modulelor rădăcină, nu versiunile traduse.

**Î: Cum adaug o limbă nouă?**
R: Suportul pentru limbaje este gestionat prin workflow-ul co-op-translator. Deschide un issue pentru a discuta adăugarea de limbi noi.

**Î: Exemplele de cod nu funcționează**
R: Asigură-te că ai urmat instrucțiunile de configurare din README-ul exemplului specific. Verifică dacă ai versiunile corecte ale dependențelor instalate.

**Î: Imaginile nu se afișează**

A: Verificați dacă căile imaginilor sunt relative și folosesc slash-uri înainte. Imaginile ar trebui să fie în directorul `images/` sau `translated_images/` pentru versiunile localizate.

### Considerații privind performanța

- Fluxul de lucru pentru traduceri poate dura câteva minute pentru a se finaliza
- Imaginile mari ar trebui optimizate înainte de a fi comise
- Păstrați fișierele markdown individuale concentrate și de dimensiuni rezonabile
- Folosiți legături relative pentru o portabilitate mai bună

### Guvernanța proiectului

Acest proiect urmează practicile Microsoft pentru sursă deschisă:
- Licență MIT pentru cod și documentație
- Codul de conduită Microsoft Open Source
- CLA necesar pentru contribuții
- Probleme de securitate: Urmați îndrumările din SECURITY.md
- Suport: Consultați SUPPORT.md pentru resurse de ajutor

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->