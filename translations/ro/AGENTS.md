# AGENTS.md

## Prezentare Generală a Proiectului

**MCP pentru Începători** este un curriculum educațional open-source pentru învățarea Model Context Protocol (MCP) - un cadru standardizat pentru interacțiunile dintre modelele AI și aplicațiile client. Acest depozit oferă materiale de învățare cuprinzătoare, incluzând exemple de cod practice în mai multe limbaje de programare.

### Tehnologii Cheie

- **Limbaje de Programare**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Framework-uri & SDK-uri**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Baze de Date**: PostgreSQL cu extensia pgvector
- **Platforme Cloud**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Instrumente de Build**: npm, Maven, pip, Cargo
- **Documentație**: Markdown cu traducere automată în mai multe limbi (48+ limbi)

### Arhitectură

- **11 Module de Bază (00-11)**: Parcurs de învățare secvențial de la fundamente la subiecte avansate
- **Laboratoare Practice**: Exerciții practice cu cod soluție complet în mai multe limbaje
- **Proiecte Exemple**: Implementări funcționale de server și client MCP
- **Sistem de Traducere**: Flux de lucru automatizat GitHub Actions pentru suport multilingv
- **Resurse Vizuale**: Director centralizat de imagini cu versiuni traduse

## Comenzi de Configurare

Acesta este un depozit axat pe documentație. Majoritatea configurărilor se fac în cadrul proiectelor și laboratoarelor individuale.

### Configurarea Depozitului

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Lucrul cu Proiecte Exemple

Proiectele exemple sunt localizate în:
- `03-GettingStarted/samples/` - Exemple specifice limbajului
- `03-GettingStarted/01-first-server/solution/` - Implementări ale primului server
- `03-GettingStarted/02-client/solution/` - Implementări ale clientului
- `11-MCPServerHandsOnLabs/` - Laboratoare cuprinzătoare de integrare a bazei de date

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
# or
pip install -e .
python main.py
```

#### Proiecte Java
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Flux de Lucru pentru Dezvoltare

### Structura Documentației

- **Module 00-11**: Conținutul curriculumului de bază în ordine secvențială
- **translations/**: Versiuni specifice limbilor (generate automat, nu editați direct)
- **translated_images/**: Versiuni localizate ale imaginilor (generate automat)
- **images/**: Imagini sursă și diagrame

### Modificarea Documentației

1. Editați doar fișierele markdown în limba engleză din directoarele modulelor de bază (00-11)
2. Actualizați imaginile în directorul `images/` dacă este necesar
3. Acțiunea GitHub co-op-translator va genera automat traduceri
4. Traducerile sunt regenerate la fiecare push către ramura principală

### Lucrul cu Traducerile

- **Traducere Automată**: Fluxul de lucru GitHub Actions gestionează toate traducerile
- **NU editați manual** fișierele din directorul `translations/`
- Metadatele traducerilor sunt încorporate în fiecare fișier tradus
- Limbi suportate: 48+ limbi, inclusiv arabă, chineză, franceză, germană, hindi, japoneză, coreeană, portugheză, rusă, spaniolă și multe altele

## Instrucțiuni de Testare

### Validarea Documentației

Deoarece acesta este în principal un depozit de documentație, testarea se concentrează pe:

1. **Validarea Link-urilor**: Asigurați-vă că toate link-urile interne funcționează
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validarea Exemplelor de Cod**: Testați dacă exemplele de cod se compilează/rulează
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Linting Markdown**: Verificați consistența formatării
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testarea Proiectelor Exemple

Fiecare exemplu specific limbajului include propria abordare de testare:

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

## Ghiduri de Stil pentru Cod

### Stilul Documentației

- Folosiți un limbaj clar, prietenos pentru începători
- Includeți exemple de cod în mai multe limbaje, acolo unde este aplicabil
- Respectați cele mai bune practici pentru markdown:
  - Folosiți anteturi de tip ATX (`#` sintaxă)
  - Folosiți blocuri de cod delimitate cu identificatori de limbaj
  - Includeți text descriptiv pentru imaginile alt
  - Mențineți lungimea liniilor rezonabilă (fără limită strictă, dar fiți sensibili)

### Stilul Exemplelor de Cod

#### TypeScript/JavaScript
- Folosiți module ES (`import`/`export`)
- Respectați convențiile modului strict TypeScript
- Includeți adnotări de tip
- Țintiți ES2022

#### Python
- Respectați ghidurile de stil PEP 8
- Folosiți indicii de tip acolo unde este potrivit
- Includeți docstrings pentru funcții și clase
- Folosiți caracteristici moderne ale Python (3.8+)

#### Java
- Respectați convențiile Spring Boot
- Folosiți caracteristici Java 21
- Respectați structura standard a proiectului Maven
- Includeți comentarii Javadoc

### Organizarea Fișierelor

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

## Build și Implementare

### Implementarea Documentației

Depozitul folosește GitHub Pages sau similar pentru găzduirea documentației (dacă este aplicabil). Modificările aduse ramurii principale declanșează:

1. Fluxul de lucru pentru traducere (`.github/workflows/co-op-translator.yml`)
2. Traducerea automată a tuturor fișierelor markdown în limba engleză
3. Localizarea imaginilor, dacă este necesar

### Nu Este Necesar Procesul de Build

Acest depozit conține în principal documentație markdown. Nu este necesar niciun pas de compilare sau build pentru conținutul curriculumului de bază.

### Implementarea Proiectelor Exemple

Proiectele exemple individuale pot avea instrucțiuni de implementare:
- Consultați `03-GettingStarted/09-deployment/` pentru ghidul de implementare a serverului MCP
- Exemple de implementare Azure Container Apps în `11-MCPServerHandsOnLabs/`

## Ghiduri pentru Contribuție

### Procesul de Pull Request

1. **Fork și Clone**: Faceți fork depozitului și clonați fork-ul local
2. **Creați o Ramură**: Folosiți nume descriptive pentru ramuri (ex.: `fix/typo-module-3`, `add/python-example`)
3. **Faceți Modificări**: Editați doar fișiere markdown în limba engleză (nu traducerile)
4. **Testați Local**: Verificați dacă markdown-ul se redă corect
5. **Trimiteți PR**: Folosiți titluri și descrieri clare pentru PR
6. **CLA**: Semnați Acordul de Licență pentru Contribuitori Microsoft când vi se solicită

### Formatul Titlului PR

Folosiți titluri clare, descriptive:
- `[Module XX] Descriere scurtă` pentru modificări specifice modulelor
- `[Samples] Descriere` pentru modificări ale codului exemplu
- `[Docs] Descriere` pentru actualizări generale ale documentației

### Ce să Contribuiți

- Corecturi de erori în documentație sau exemple de cod
- Noi exemple de cod în limbaje suplimentare
- Clarificări și îmbunătățiri ale conținutului existent
- Studii de caz noi sau exemple practice
- Raportarea problemelor pentru conținut neclar sau incorect

### Ce NU Trebuie Să Faceți

- Nu editați direct fișierele din directorul `translations/`
- Nu editați directorul `translated_images/`
- Nu adăugați fișiere binare mari fără discuție
- Nu modificați fișierele fluxului de lucru pentru traducere fără coordonare

## Note Suplimentare

### Întreținerea Depozitului

- **Changelog**: Toate modificările semnificative sunt documentate în `changelog.md`
- **Ghid de Studiu**: Folosiți `study_guide.md` pentru o prezentare generală a navigării în curriculum
- **Șabloane de Probleme**: Folosiți șabloanele de probleme GitHub pentru raportarea erorilor și cererile de funcționalități
- **Cod de Conduită**: Toți contribuitorii trebuie să respecte Codul de Conduită Open Source Microsoft

### Parcurs de Învățare

Urmați modulele în ordine secvențială (00-11) pentru o învățare optimă:
1. **00-02**: Fundamente (Introducere, Concepte de Bază, Securitate)
2. **03**: Începeți cu implementarea practică
3. **04-05**: Implementare practică și subiecte avansate
4. **06-10**: Comunitate, cele mai bune practici și aplicații reale
5. **11**: Laboratoare cuprinzătoare de integrare a bazei de date (13 laboratoare secvențiale)

### Resurse de Suport

- **Documentație**: https://modelcontextprotocol.io/
- **Specificație**: https://spec.modelcontextprotocol.io/
- **Comunitate**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Serverul Discord Microsoft Azure AI Foundry
- **Cursuri Asemănătoare**: Consultați README.md pentru alte parcursuri de învățare Microsoft

### Rezolvarea Problemelor Comune

**Î: PR-ul meu eșuează la verificarea traducerii**
R: Asigurați-vă că ați editat doar fișiere markdown în limba engleză din directoarele modulelor de bază, nu versiunile traduse.

**Î: Cum adaug o limbă nouă?**
R: Suportul pentru limbi este gestionat prin fluxul de lucru co-op-translator. Deschideți o problemă pentru a discuta adăugarea de limbi noi.

**Î: Exemplele de cod nu funcționează**
R: Asigurați-vă că ați urmat instrucțiunile de configurare din README-ul specific exemplului. Verificați că aveți instalate versiunile corecte ale dependențelor.

**Î: Imaginile nu se afișează**
R: Verificați că căile imaginilor sunt relative și folosesc slash-uri înainte. Imaginile ar trebui să fie în directorul `images/` sau `translated_images/` pentru versiuni localizate.

### Considerații de Performanță

- Fluxul de lucru pentru traducere poate dura câteva minute pentru a se finaliza
- Imaginile mari ar trebui optimizate înainte de a fi comise
- Mențineți fișierele markdown individuale concentrate și de dimensiuni rezonabile
- Folosiți link-uri relative pentru o portabilitate mai bună

### Guvernanța Proiectului

Acest proiect urmează practicile open source Microsoft:
- Licență MIT pentru cod și documentație
- Cod de Conduită Open Source Microsoft
- CLA necesar pentru contribuții
- Probleme de securitate: Urmați ghidurile din SECURITY.md
- Suport: Consultați SUPPORT.md pentru resurse de ajutor

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.