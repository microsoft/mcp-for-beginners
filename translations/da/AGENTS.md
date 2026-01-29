# AGENTS.md

## Projektoversigt

**MCP for Begyndere** er en open-source uddannelsesplan til at lære Model Context Protocol (MCP) - en standardiseret ramme for interaktioner mellem AI-modeller og klientapplikationer. Dette repository tilbyder omfattende læringsmaterialer med praktiske kodeeksempler på tværs af flere programmeringssprog.

### Nøgleteknologier

- **Programmeringssprog**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDK'er**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databaser**: PostgreSQL med pgvector-udvidelse
- **Cloud-platforme**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build-værktøjer**: npm, Maven, pip, Cargo
- **Dokumentation**: Markdown med automatiseret oversættelse til flere sprog (48+ sprog)

### Arkitektur

- **11 Kerne Moduler (00-11)**: Sekventiel læringssti fra grundlæggende til avancerede emner
- **Praktiske Labs**: Øvelser med komplette løsningskoder på flere sprog
- **Eksempelprojekter**: Fungerende MCP-server og klientimplementeringer
- **Oversættelsessystem**: Automatiseret GitHub Actions workflow til flersproget support
- **Billedressourcer**: Centraliseret billedmappe med oversatte versioner

## Opsætningskommandoer

Dette er et dokumentationsfokuseret repository. De fleste opsætninger sker inden for individuelle eksempelprojekter og labs.

### Repository Opsætning

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Arbejde med Eksempelprojekter

Eksempelprojekter findes i:
- `03-GettingStarted/samples/` - Sprog-specifikke eksempler
- `03-GettingStarted/01-first-server/solution/` - Første serverimplementeringer
- `03-GettingStarted/02-client/solution/` - Klientimplementeringer
- `11-MCPServerHandsOnLabs/` - Omfattende databaseintegrationslabs

Hvert eksempelprojekt indeholder sine egne opsætningsinstruktioner:

#### TypeScript/JavaScript Projekter
```bash
cd <project-directory>
npm install
npm start
```

#### Python Projekter
```bash
cd <project-directory>
pip install -r requirements.txt
# or
pip install -e .
python main.py
```

#### Java Projekter
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Udviklingsworkflow

### Dokumentationsstruktur

- **Moduler 00-11**: Kerneindhold i sekventiel rækkefølge
- **translations/**: Sprog-specifikke versioner (auto-genereret, må ikke redigeres direkte)
- **translated_images/**: Lokaliserede billedversioner (auto-genereret)
- **images/**: Kildebilleder og diagrammer

### Ændringer i Dokumentation

1. Rediger kun de engelske markdown-filer i rodmoduldirektorierne (00-11)
2. Opdater billeder i `images/`-mappen, hvis nødvendigt
3. GitHub Action co-op-translator genererer automatisk oversættelser
4. Oversættelser regenereres ved push til hovedbranch

### Arbejde med Oversættelser

- **Automatiseret Oversættelse**: GitHub Actions workflow håndterer alle oversættelser
- **Må IKKE manuelt redigere** filer i `translations/`-mappen
- Oversættelsesmetadata er indlejret i hver oversat fil
- Understøttede sprog: 48+ sprog, herunder arabisk, kinesisk, fransk, tysk, hindi, japansk, koreansk, portugisisk, russisk, spansk og mange flere

## Testinstruktioner

### Dokumentationsvalidering

Da dette primært er et dokumentationsrepository, fokuserer test på:

1. **Linkvalidering**: Sørg for, at alle interne links fungerer
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Kodeeksempelvalidering**: Test, at kodeeksempler kan kompileres/køres
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown-linting**: Tjek formateringskonsistens
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Test af Eksempelprojekter

Hvert sprog-specifikke eksempel inkluderer sin egen testtilgang:

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

## Kodestilretningslinjer

### Dokumentationsstil

- Brug klart, begyndervenligt sprog
- Inkluder kodeeksempler på flere sprog, hvor det er relevant
- Følg bedste praksis for markdown:
  - Brug ATX-stil overskrifter (`#` syntaks)
  - Brug indhegnede kodeblokke med sprogidentifikatorer
  - Inkluder beskrivende alt-tekst for billeder
  - Hold linjelængder rimelige (ingen hård grænse, men vær fornuftig)

### Kodestil for Eksempler

#### TypeScript/JavaScript
- Brug ES-moduler (`import`/`export`)
- Følg TypeScript-strenge tilstandskonventioner
- Inkluder typeannoteringer
- Mål ES2022

#### Python
- Følg PEP 8-stilretningslinjer
- Brug type hints, hvor det er passende
- Inkluder docstrings for funktioner og klasser
- Brug moderne Python-funktioner (3.8+)

#### Java
- Følg Spring Boot-konventioner
- Brug Java 21-funktioner
- Følg standard Maven-projektstruktur
- Inkluder Javadoc-kommentarer

### Filorganisering

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

## Build og Udrulning

### Dokumentationsudrulning

Repositoryet bruger GitHub Pages eller lignende til dokumentationshosting (hvis relevant). Ændringer i hovedbranch udløser:

1. Oversættelsesworkflow (`.github/workflows/co-op-translator.yml`)
2. Automatiseret oversættelse af alle engelske markdown-filer
3. Billedlokalisering efter behov

### Ingen Build-proces Påkrævet

Dette repository indeholder primært markdown-dokumentation. Ingen kompilering eller build-trin er nødvendigt for kerneindholdet.

### Udrulning af Eksempelprojekter

Individuelle eksempelprojekter kan have udrulningsinstruktioner:
- Se `03-GettingStarted/09-deployment/` for MCP-serverudrulningsvejledning
- Eksempler på Azure Container Apps-udrulning i `11-MCPServerHandsOnLabs/`

## Retningslinjer for Bidrag

### Pull Request Proces

1. **Fork og Clone**: Fork repositoryet og klon din fork lokalt
2. **Opret en Branch**: Brug beskrivende branch-navne (f.eks. `fix/typo-module-3`, `add/python-example`)
3. **Foretag Ændringer**: Rediger kun engelske markdown-filer (ikke oversættelser)
4. **Test Lokalt**: Verificer, at markdown gengives korrekt
5. **Indsend PR**: Brug klare PR-titler og beskrivelser
6. **CLA**: Underskriv Microsoft Contributor License Agreement, når du bliver bedt om det

### PR Titel Format

Brug klare, beskrivende titler:
- `[Module XX] Kort beskrivelse` for modul-specifikke ændringer
- `[Samples] Beskrivelse` for ændringer i kodeeksempler
- `[Docs] Beskrivelse` for generelle dokumentationsopdateringer

### Hvad du kan Bidrage med

- Fejlrettelser i dokumentation eller kodeeksempler
- Nye kodeeksempler på yderligere sprog
- Klargørelser og forbedringer af eksisterende indhold
- Nye casestudier eller praktiske eksempler
- Rapportering af problemer med uklart eller forkert indhold

### Hvad du IKKE skal gøre

- Rediger ikke direkte filer i `translations/`-mappen
- Rediger ikke `translated_images/`-mappen
- Tilføj ikke store binære filer uden diskussion
- Ændr ikke oversættelsesworkflow-filer uden koordinering

## Yderligere Noter

### Repository Vedligeholdelse

- **Changelog**: Alle væsentlige ændringer dokumenteres i `changelog.md`
- **Studieguide**: Brug `study_guide.md` til oversigt over læringsplanen
- **Issue Templates**: Brug GitHub issue templates til fejlrapporter og funktionsanmodninger
- **Adfærdskodeks**: Alle bidragydere skal følge Microsoft Open Source Code of Conduct

### Læringssti

Følg modulerne i sekventiel rækkefølge (00-11) for optimal læring:
1. **00-02**: Grundlæggende (Introduktion, Kernekoncepter, Sikkerhed)
2. **03**: Kom godt i gang med praktisk implementering
3. **04-05**: Praktisk implementering og avancerede emner
4. **06-10**: Fællesskab, bedste praksis og virkelige applikationer
5. **11**: Omfattende databaseintegrationslabs (13 sekventielle labs)

### Supportressourcer

- **Dokumentation**: https://modelcontextprotocol.io/
- **Specifikation**: https://spec.modelcontextprotocol.io/
- **Fællesskab**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord-server
- **Relaterede Kurser**: Se README.md for andre Microsoft-læringsstier

### Almindelig Fejlfinding

**Q: Min PR fejler oversættelseskontrollen**
A: Sørg for, at du kun har redigeret engelske markdown-filer i rodmoduldirektorierne, ikke oversatte versioner.

**Q: Hvordan tilføjer jeg et nyt sprog?**
A: Sprogsupport administreres gennem co-op-translator workflow. Åbn en issue for at diskutere tilføjelse af nye sprog.

**Q: Kodeeksempler virker ikke**
A: Sørg for, at du har fulgt opsætningsinstruktionerne i det specifikke eksempels README. Tjek, at du har de korrekte versioner af afhængigheder installeret.

**Q: Billeder vises ikke**
A: Verificer, at billedstier er relative og bruger skråstreger. Billeder skal være i `images/`-mappen eller `translated_images/` for lokaliserede versioner.

### Ydelseshensyn

- Oversættelsesworkflow kan tage flere minutter at fuldføre
- Store billeder bør optimeres før commit
- Hold individuelle markdown-filer fokuserede og rimeligt størrelsesmæssige
- Brug relative links for bedre portabilitet

### Projektstyring

Dette projekt følger Microsofts open source-praksis:
- MIT-licens for kode og dokumentation
- Microsoft Open Source Code of Conduct
- CLA påkrævet for bidrag
- Sikkerhedsproblemer: Følg retningslinjerne i SECURITY.md
- Support: Se SUPPORT.md for hjælpressourcer

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.