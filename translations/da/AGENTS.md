# AGENTS.md

## Projektoversigt

**MCP for Beginners** er en open-source uddannelsesplan til læring af Model Context Protocol (MCP) - en standardiseret ramme for interaktioner mellem AI-modeller og klientapplikationer. Dette repository indeholder omfattende læringsmaterialer med praktiske kodeeksempler på tværs af flere programmeringssprog.

### Centrale teknologier

- **Programmeringssprog**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDK'er**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databaser**: PostgreSQL med pgvector-udvidelse
- **Cloud-platforme**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build-værktøjer**: npm, Maven, pip, Cargo
- **Dokumentation**: Markdown med automatiseret flersproget oversættelse (48+ sprog)

### Arkitektur

- **11 kerne-moduler (00-11)**: Sekventiel læringssti fra fundament til avancerede emner
- **Hands-on labs**: Praktiske øvelser med komplet løsningskode i flere sprog
- **Eksempelprojekter**: Fungerende MCP-server og klient-implementeringer
- **Oversættelsessystem**: Automatiseret GitHub Actions-workflow til flersproget support
- **Billedressourcer**: Centraliseret billedmappe med oversatte versioner

## Opsætningskommandoer

Dette er et dokumentationsfokuseret repository. Det meste opsætning sker indenfor individuelle eksempelprojekter og labs.

### Repository-opsætning

```bash
# Klon arkivet
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Arbejde med eksempelprojekter

Eksempelprojekter findes i:
- `03-GettingStarted/samples/` - Sprog-specifikke eksempler
- `03-GettingStarted/01-first-server/solution/` - Første server-implementeringer
- `03-GettingStarted/02-client/solution/` - Klient-implementeringer
- `11-MCPServerHandsOnLabs/` - Omfattende databaseintegrationslabs

Hvert eksempelprojekt indeholder sine egne opsætningsinstruktioner:

#### TypeScript/JavaScript-projekter
```bash
cd <project-directory>
npm install
npm start
```

#### Python-projekter
```bash
cd <project-directory>
pip install -r requirements.txt
# eller
pip install -e .
python main.py
```

#### Java-projekter
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Udviklingsworkflow

### MCP 7-28 Forberedelse

#### Repo klarheds-tjekliste

- [x] **Ny bidragyder klarhed**: Denne fil definerer repository-formål,
  struktur, bidragsregler og eksempelopsætningsstier.
- [x] **Build/test/lint-kommandoer med præcise flag**:
  - Repository dokumentslint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Repository dokuments link-mønsterrevision:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript eksempelvalidering:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python eksempelvalidering:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java eksempelvalidering:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Én realistisk workflow, der kan blive et MCP-værktøj**:
  `validate_curriculum_change`
- [x] **Input/output er eksplicitte** (se specifikationen nedenfor).
- [x] **Tilladelser og fejlsituationer er dokumenterede** (se specifikationen nedenfor).
- [x] **CI-testbarhed er eksplicit** (deterministiske kommandoer, eksplicitte
  exit-koder og maskinlæsbart output).

#### Kandidat MCP værktøjsworkflow: `validate_curriculum_change`

##### Mål

Validér tilstandsændringer i curriculumsdokumentation og repræsentativ eksempelcode
før merge.

##### Input

- `changed_paths: string[]` (påkrævet) - relative stier ændret i PR.
- `run_docs_lint: boolean` (standard `true`)
- `run_links_audit: boolean` (standard `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (standard alle `false`)

##### Output

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Tilladelser

- Læse arbejdsområdefiler og skrive værktøjs-genererede artefakter (f.eks. lint-
  rapporter, testlogs) kun; ingen skrivning til `translations/` eller
  `translated_images/`.
- Udføre lokale shell-kommandoer.
- Valgfri netværksadgang kun for pakke-gendannelse (`npm ci`,
  `python -m pip install`, `mvn` afhængighedsopløsning).
- Ingen tilladelse til at pushe, merge eller ændre `translations/` eller
  `translated_images/`.

##### Fejlsituationer

- `E_NO_INPUT_PATHS`: `changed_paths` er tom.
- `E_INVALID_PATH`: inputsti krydser repository-roden.
- `E_LINT_FAILED`: markdown lint afslutter med ikke-nul kode.
- `E_LINK_AUDIT_FAILED`: link revisions-kommando afslutter med ikke-nul kode.
- `E_SAMPLE_TEST_FAILED`: eksempel test/build afslutter med ikke-nul kode.
- `E_TIMEOUT`: kommando overskredet konfigureret timeout.

##### Anbefalet CI-kontrakt

For at automatisere validering, konfigurer et CI-job der:

- Trigger på pull requests der berører `*.md`, eksempelcode eller denne fil.
- Kører de præcise kommandoer listet ovenfor.
- Gemmer logs som artefakter.
- Fejler jobbet ved enhver ikke-nul exit-kode.

#### Hvis du deployer en MCP-server fra dette repo

- [ ] Læs den endelige MCP `2026-07-28` changelog:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Bekræft at den valgte SDK-release understøtter MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Fjern session- og handshake-antagelser; behandle hver anmodning som
  selvstændig:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Send `Mcp-Method` og `Mcp-Name` headers for rå HTTP-anmodninger:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Revider hardkodede fejl-koder (`missing resource` flyttet fra `-32002` til `-32602`).
- [ ] Migrer fra forældede Roots, Sampling, Logging og Dynamisk Klient
  Registrering:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrer fra den eksperimentelle `2025-11-25` Tasks API:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Gennemgå autorisation for OAuth og OpenID Connect styrkelse:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Dokumentationsstruktur

- **Moduler 00-11**: Kerneindhold i curriculummet i sekventiel rækkefølge
- **translations/**: Sprog-specifikke versioner (auto-genereret, må ikke redigeres direkte)
- **translated_images/**: Lokaliserede billedversioner (auto-genereret)
- **images/**: Kildebilleder og diagrammer

### Ændring af dokumentation

1. Rediger kun de engelske markdown-filer i rodmodulmapperne (00-11)
2. Opdater billeder i `images/` mappen efter behov
3. Co-op-translator GitHub Action genererer automatisk oversættelser
4. Oversættelser regenereres ved push til main-branch

### Arbejde med oversættelser

- **Automatiseret oversættelse**: GitHub Actions workflow håndterer alle oversættelser
- **Må IKKE redigeres manuelt** filer i `translations/` mappen
- Oversættelsesmetadata er indlejret i hver oversat fil
- Understøttede sprog: 48+ sprog inklusiv arabisk, kinesisk, fransk, tysk, hindi, japansk, koreansk, portugisisk, russisk, spansk og mange flere

## Testinstruktioner

### Dokumentationsvalidering

Da dette primært er et dokumentationsrepository, fokuserer test på:

1. **Link-mønsterrevision**: Liste over Markdown-links til gennemgang

   ```bash
   # Liste over Markdown-links (mønsterrevision)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Kodeeksempelvalidering**: Test at kodeeksempler kompilerer/kører

   ```bash
   # Naviger til en specifik prøve og kør dens tests
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown-linting**: Tjek formateringens konsistens

   ```bash
   # Brug markdownlint hvis nødvendigt
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Eksempelprojekttest

Hver sprog-specifik prøve indeholder sin egen testmetode:

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

## Kode-stil retningslinjer

### Dokumentationsstil

- Brug klart, begyndervenligt sprog
- Inkluder kodeeksempler på flere sprog hvor relevant
- Følg markdown bedste praksis:
  - Brug ATX-type overskrifter (`#` syntaks)
  - Brug afgrænsede kodeblokke med sprogspecifikke identificeringsmærker
  - Inkluder beskrivende alternativ tekst for billeder
  - Hold linjelængder rimelige (ingen hård grænse, men vær fornuftig)

### Kodeeksempel-stil

#### TypeScript/JavaScript
- Brug ES-moduler (`import`/`export`)
- Følg TypeScript strikshedsregler
- Inkluder typeangivelser
- Målret ES2022

#### Python
- Følg PEP 8 stil retningslinjer
- Brug type hints hvor passende
- Inkluder docstrings for funktioner og klasser
- Brug moderne Python-funktioner (3.8+)

#### Java
- Følg Spring Boot konventioner
- Brug Java 21 funktioner
- Følg standard Maven-projektstruktur
- Inkluder Javadoc kommentarer

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

## Bygning og Udrulning

### Dokumentationsudrulning

Repositoryet bruger GitHub Pages eller lignende til dokumentationshosting (hvis relevant). Ændringer til main-branch udløser:

1. Oversættelsesworkflow (`.github/workflows/co-op-translator.yml`)
2. Automatiseret oversættelse af alle engelske markdown-filer
3. Billedlokalisering efter behov

### Ingen byggefase nødvendig

Dette repository indeholder primært markdown-dokumentation. Ingen kompilering eller byggeproces er nødvendig for kerneindholdet i curriculum.

### Eksempelprojektsudrulning

Individuelle eksempelprojekter kan have udrulningsinstruktioner:
- Se `03-GettingStarted/09-deployment/` for MCP server udrulningsvejledning
- Azure Container Apps udrulningseksempler i `11-MCPServerHandsOnLabs/`

## Bidragsretningslinjer

### Pull Request-proces

1. **Fork og klon**: Fork repository og klon din fork lokalt
2. **Opret en gren**: Brug beskrivende grennavne (f.eks. `fix/typo-module-3`, `add/python-example`)
3. **Foretag ændringer**: Rediger kun engelske markdown-filer (ikke oversættelser)
4. **Test lokalt**: Bekræft at markdown gengives korrekt
5. **Indsend PR**: Brug klare PR-titler og beskrivelser
6. **CLA**: Underskriv Microsoft Contributor License Agreement når det efterspørges

### PR-titelformat

Brug klare, beskrivende titler:
- `[Module XX] Kort beskrivelse` for modul-specifikke ændringer
- `[Samples] Beskrivelse` for ændringer i eksempelcode
- `[Docs] Beskrivelse` for generelle dokumentationsopdateringer

### Hvad bidrage med

- Fejlrettelser i dokumentation eller kodeeksempler
- Nye kodeeksempler på yderligere sprog
- Afklaringer og forbedringer af eksisterende indhold
- Nye casestudier eller praktiske eksempler
- Problemløsningsrapporter for uklart eller forkert indhold

### Hvad IKKE at gøre

- Rediger ikke filer direkte i `translations/` mappen
- Rediger ikke `translated_images/` mappen
- Tilføj ikke store binære filer uden forudgående diskussion
- Ændr ikke oversættelsesworkflowfiler uden koordination

## Yderligere noter

### Repository-vedligeholdelse

- **Changelog**: Alle væsentlige ændringer dokumenteres i `changelog.md`
- **Studieguide**: Brug `study_guide.md` til oversigt over curriculum-navigation
- **Issue-skabeloner**: Brug GitHub issue-skabeloner til fejlrapporter og funktions-forespørgsler
- **Adfærdskodeks**: Alle bidragydere skal følge Microsoft Open Source Adfærdskodeks

### Læringssti

Følg moduler i sekventiel rækkefølge (00-11) for optimal læring:
1. **00-02**: Grundlæggende (Introduktion, Kernekoncepter, Sikkerhed)
2. **03**: Kom godt i gang med hands-on implementering
3. **04-05**: Praktisk implementering og avancerede emner
4. **06-10**: Fællesskab, bedste praksis og virkelige anvendelser
5. **11**: Omfattende databaseintegrationslabs (13 sekventielle labs)

### Supportressourcer

- **Dokumentation**: https://modelcontextprotocol.io/
- **Specifikation**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Fællesskab**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord-server
- **Relaterede kurser**: Se README.md for andre Microsoft læringsstier

### Almindelig fejlfinding

**Q: Min PR fejler oversættelsestjekket**
A: Sørg for kun at have redigeret engelske markdown-filer i rodmodulmapper, ikke oversatte versioner.

**Q: Hvordan tilføjer jeg et nyt sprog?**
A: Sprogunderstøttelse styres via co-op-translator workflow. Opret en issue for at diskutere tilføjelse af nye sprog.

**Q: Kodeeksempler virker ikke**
A: Sørg for at have fulgt opsætningsinstruktionerne i det specifikke eksempel-README. Tjek at du har de korrekte versioner af afhængigheder installeret.

**Q: Billeder vises ikke**

A: Bekræft at billedstier er relative og bruger fremadskråstreger. Billeder bør være i `images/` mappen eller `translated_images/` for lokaliserede versioner.

### Ydelseshensyn

- Oversættelsesworkflow kan tage flere minutter at gennemføre
- Store billeder bør optimeres inden indsendelse
- Hold individuelle markdown-filer fokuserede og rimeligt størrelse
- Brug relative links for bedre portabilitet

### Projektstyring

Dette projekt følger Microsofts open source-praksis:
- MIT-licens for kode og dokumentation
- Microsoft Open Source Code of Conduct
- CLA kræves for bidrag
- Sikkerhedsproblemer: Følg retningslinjerne i SECURITY.md
- Support: Se SUPPORT.md for hjælperessourcer

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->