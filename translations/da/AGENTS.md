# AGENTS.md

## Projektoversigt

**MCP for Beginners** er en open-source uddannelsesplan til læring af Model Context Protocol (MCP) - en standardiseret ramme for interaktioner mellem AI-modeller og klientapplikationer. Dette repository indeholder omfattende læringsmaterialer med praktiske kodeeksempler på flere programmeringssprog.

### Centrale teknologier

- **Programmeringssprog**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databaser**: PostgreSQL med pgvector udvidelse
- **Cloud-platforme**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Buildværktøjer**: npm, Maven, pip, Cargo
- **Dokumentation**: Markdown med automatiseret flersproget oversættelse (48+ sprog)

### Arkitektur

- **11 kerne-moduler (00-11)**: Sekventiel læringssti fra grundlæggende til avancerede emner
- **Hands-on laboratorier**: Praktiske øvelser med komplet løsningskode på flere sprog
- **Eksempelprojekter**: Funktionsdygtige MCP server- og klientimplementeringer
- **Oversættelsessystem**: Automatiseret GitHub Actions workflow til flersproget support
- **Billedressourcer**: Centraliseret billedmappe med oversatte versioner

## Opsætningskommandoer

Dette er et dokumentationsfokuseret repository. Mest opsætning sker i de enkelte eksempelprojekter og laboratorier.

### Repository opsætning

```bash
# Klon arkivet
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Arbejde med eksempelprojekter

Eksempelprojekter findes i:
- `03-GettingStarted/samples/` - Sprog-specifikke eksempler
- `03-GettingStarted/01-first-server/solution/` - Første serverimplementeringer
- `03-GettingStarted/02-client/solution/` - Klientimplementeringer
- `11-MCPServerHandsOnLabs/` - Omfattende databaseintegrationslaboratorier

Hvert eksempelprojekt indeholder egne opsætningsinstruktioner:

#### TypeScript/JavaScript projekter
```bash
cd <project-directory>
npm install
npm start
```

#### Python projekter
```bash
cd <project-directory>
pip install -r requirements.txt
# eller
pip install -e .
python main.py
```

#### Java projekter
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Udviklingsworkflow

### MCP 7-28 Klarhed

#### Tjekliste for repository klarhed

- [x] **Klarhed for nye bidragydere**: Denne fil definerer repository formål,
  struktur, bidragsregler og eksempelopsætningsstier.
- [x] **Build/test/lint-kommandoer med præcise flags**:
  - Repository dokumentations lint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Repository dokumentations linkmønster revision:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript eksempelvalidering:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python eksempelvalidering:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java eksempelvalidering:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **En realistisk workflow, som kan blive et MCP-værktøj**:
  `validate_curriculum_change`
- [x] **Input/output er eksplicitte** (se specifikation nedenfor).
- [x] **Tilladelser og fejltilstande er dokumenterede** (se specifikation nedenfor).
- [x] **CI testbarhed er eksplicit** (deterministiske kommandoer, eksplicitte
  exit-koder og maskinlæsbare output).

#### Kandidat MCP værktøjsworkflow: `validate_curriculum_change`

##### Mål

Valider ændringer i læreplansdokumentationen og sundheden i repræsentativ eksempelkode
før sammenfletning.

##### Input

- `changed_paths: string[]` (påkrævet) - relativt ændrede stier i PR.
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

- Læs arbejdsområdefiler og skriv kun værktøjsgenererede artefakter (fx lint
  rapporter, testlogs); ingen skrivning til `translations/` eller
  `translated_images/`.
- Eksekver lokale shell-kommandoer.
- Valgfri netværksadgang kun til pakke-gendannelse (`npm ci`,
  `python -m pip install`, `mvn` afhængighedsløsning).
- Ingen tilladelse til at pushe, merge eller ændre `translations/` eller
  `translated_images/`.

##### Fejltilstande

- `E_NO_INPUT_PATHS`: `changed_paths` tom.
- `E_INVALID_PATH`: inputsti går uden for repository-roden.
- `E_LINT_FAILED`: markdown lint afsluttede med ikke-nul exit.
- `E_LINK_AUDIT_FAILED`: link revision kommando afsluttede med ikke-nul exit.
- `E_SAMPLE_TEST_FAILED`: eksempel test/build afsluttede med ikke-nul exit.
- `E_TIMEOUT`: kommando overskred konfigureret timeout.

##### Anbefalet CI kontrakt

For at automatisere validering, konfigurer et CI job som:

- Udløses ved pull requests, der påvirker `*.md`, eksempelkode eller denne fil.
- Kører de præcise kommandoer listet ovenfor.
- Gemmer logs som artefakter.
- Fejler jobbet ved enhver ikke-nul exit-kode.

#### Hvis du leverer en MCP server fra dette repo

- [ ] Læs udkast til ændringslog for MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Test din server mod SDK betas:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Fjern session- og håndtrykantagelser; behandl hver anmodning som
  selvstændig:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Send `Mcp-Method` og `Mcp-Name` headers for rå HTTP-anmodninger:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Revider hardkodede fejlkoder (`missing resource` flyttet fra `-32002` til `-32602`).
- [ ] Marker og planlæg migration for udfasede rødder, sampling og
  logging:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrer fra den eksperimentelle `2025-11-25` Tasks API:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Gennemgå godkendelse for OAuth og OpenID Connect forstærkning:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Dokumentationsstruktur

- **Moduler 00-11**: Kerneindhold i læreplanen i sekventiel rækkefølge
- **translations/**: Sprog-specifikke versioner (automatisk genereret, må ikke redigeres direkte)
- **translated_images/**: Lokaliserede billedversioner (automatisk genereret)
- **images/**: Kildebilleder og diagrammer

### Foretage dokumentationsændringer

1. Rediger kun de engelske markdown-filer i rodkatalogerne for modulerne (00-11)
2. Opdater billeder i `images/` mappen om nødvendigt
3. GitHub Actions co-op-translator genererer automatisk oversættelser
4. Oversættelser genopbygges ved push til main branch

### Arbejde med oversættelser

- **Automatiseret oversættelse**: GitHub Actions workflow håndterer alle oversættelser
- **Rediger IKKE manuelt** filer i `translations/` mappen
- Oversættelsesmetadata er indlejret i hver oversat fil
- Understøttede sprog: 48+ sprog inklusive arabisk, kinesisk, fransk, tysk, hindi, japansk, koreansk, portugisisk, russisk, spansk og mange flere

## Testinstruktioner

### Dokumentationsvalidering

Da dette primært er et dokumentationsrepo, fokuserer testen på:

1. **Linkmønsterrevision**: List Markdown links til gennemsyn

   ```bash
   # List over Markdown-links (mønsterrevision)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validering af kodeeksempler**: Test at kodeeksempler kan kompileres/køres

   ```bash
   # Naviger til en specifik prøve og kør dens tests
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown Linting**: Kontroller formateringskonsistens

   ```bash
   # Brug markdownlint hvis det er nødvendigt
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Test af eksempelprojekter

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

## Kode stil retningslinjer

### Dokumentationsstil

- Brug klart og begynder-venligt sprog
- Inkluder kodeeksempler på flere sprog hvor det er relevant
- Følg bedste praksis for markdown:
  - Brug ATX-stil overskrifter (`#` syntaks)
  - Brug afgrænsede kodeblokke med sprogidentifikatorer
  - Inkluder beskrivende alternativ tekst til billeder
  - Hold linjelængder rimelige (ingen hård grænse, men vær fornuftig)

### Kodeeksempel stil

#### TypeScript/JavaScript
- Brug ES-moduler (`import`/`export`)
- Følg TypeScript's strict mode konventioner
- Inkluder typeannoteringer
- Målret ES2022

#### Python
- Følg PEP 8 stilretningslinjer
- Brug type hints hvor passende
- Inkluder docstrings for funktioner og klasser
- Brug moderne Python-funktioner (3.8+)

#### Java
- Følg Spring Boot konventioner
- Brug Java 21 funktioner
- Følg standard Maven projektstruktur
- Inkluder Javadoc kommentarer

### Filorganisation

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

Repository'et bruger GitHub Pages eller lignende til hostning af dokumentation (hvis relevant). Ændringer til main branch udløser:

1. Oversættelsesworkflow (`.github/workflows/co-op-translator.yml`)
2. Automatiseret oversættelse af alle engelske markdown-filer
3. Billedlokalisering efter behov

### Ingen build-proces nødvendig

Dette repository indeholder primært markdown dokumentation. Ingen kompilering eller build-trin er nødvendig for kernematerialet i læreplanen.

### Udrulning af eksempelprojekter

Individuelle eksempelprojekter kan have udrulningsinstruktioner:
- Se `03-GettingStarted/09-deployment/` for MCP server udrulningsvejledning
- Azure Container Apps udrulningseksempler i `11-MCPServerHandsOnLabs/`

## Bidragsretningslinjer

### Pull Request proces

1. **Fork og Clone**: Fork repository og clone din fork lokalt
2. **Opret en branch**: Brug beskrivende branchnavne (fx `fix/typo-module-3`, `add/python-example`)
3. **Lav ændringer**: Rediger kun engelske markdown filer (ikke oversættelser)
4. **Test lokalt**: Verificer at markdown renders korrekt
5. **Indsend PR**: Brug klare PR titler og beskrivelser
6. **CLA**: Underskriv Microsoft Contributor License Agreement når det bliver bedt om det

### PR titel format

Brug klare, beskrivende titler:
- `[Module XX] Kort beskrivelse` for modul-specifikke ændringer
- `[Samples] Beskrivelse` for ændringer i eksempel kode
- `[Docs] Beskrivelse` for generelle opdateringer af dokumentation

### Hvad man skal bidrage med

- Fejlrettelser i dokumentation eller kodeeksempler
- Nye kodeeksempler på yderligere sprog
- Klargørelser og forbedringer af eksisterende indhold
- Nye casestudier eller praktiske eksempler
- Fejlrapporter for uklart eller forkert indhold

### Hvad man IKKE skal gøre

- Rediger ikke filer direkte i `translations/` mappen
- Rediger ikke `translated_images/` mappen
- Tilføj ikke store binære filer uden diskussion
- Ændr ikke oversættelsesworkflow-filer uden koordinering

## Yderligere noter

### Repository vedligeholdelse

- **Ændringslog**: Alle væsentlige ændringer dokumenteres i `changelog.md`
- **Studieguide**: Brug `study_guide.md` til læreplannavigation overview
- **Issue templates**: Brug GitHub issue templates til fejlrapporter og feature forespørgsler
- **Adfærdskodeks**: Alle bidragydere skal følge Microsoft Open Source Code of Conduct

### Læringssti

Følg moduler i sekventiel rækkefølge (00-11) for optimal læring:
1. **00-02**: Grundlæggende (Introduktion, kernebegreber, sikkerhed)
2. **03**: Kom godt i gang med praktisk implementering
3. **04-05**: Praktisk implementering og avancerede emner
4. **06-10**: Fællesskab, bedste praksis og anvendelser i praksis
5. **11**: Omfattende databaseintegrationslaboratorier (13 sekventielle laboratorier)

### Support ressourcer

- **Dokumentation**: https://modelcontextprotocol.io/
- **Specifikation**: https://spec.modelcontextprotocol.io/
- **Fællesskab**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord server
- **Relaterede kurser**: Se README.md for andre Microsoft læringsstier

### Almindelig fejlsøgning

**Q: Min PR fejler oversættelsestjek**
A: Sørg for kun at have redigeret engelske markdown-filer i rodkatalogerne for moduler, ikke oversatte versioner.

**Q: Hvordan tilføjer jeg et nyt sprog?**
A: Sprogunderstøttelse styres gennem co-op-translator workflow. Opret en issue for at diskutere tilføjelse af nye sprog.

**Q: Kodeeksempler virker ikke**

Svar: Sørg for, at du har fulgt opsætningsinstruktionerne i den specifikke eksempels README. Tjek, at du har de korrekte versioner af afhængigheder installeret.

**Spørgsmål: Billeder vises ikke**
Svar: Bekræft, at billedstierne er relative og bruger skråstreger fremad. Billeder skal være i `images/` mappen eller `translated_images/` for lokaliserede versioner.

### Ydelsesovervejelser

- Oversættelsesarbejdsgangen kan tage flere minutter at fuldføre
- Store billeder bør optimeres før commit
- Hold individuelle markdown-filer fokuserede og rimeligt store
- Brug relative links for bedre portabilitet

### Projektstyring

Dette projekt følger Microsofts open source praksis:
- MIT-licens for kode og dokumentation
- Microsoft Open Source Code of Conduct
- CLA kræves for bidrag
- Sikkerhedsproblemer: Følg retningslinjerne i SECURITY.md
- Support: Se SUPPORT.md for hjælpemidler

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->