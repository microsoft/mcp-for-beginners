# AGENTS.md

## Prosjektoversikt

**MCP for nybegynnere** er en åpen kildekode utdanningsplan for læring av Model Context Protocol (MCP) - en standardisert rammeverk for interaksjoner mellom AI-modeller og klientapplikasjoner. Dette depotet gir omfattende læringsmateriell med praktiske kodeeksempler på flere programmeringsspråk.

### Viktige teknologier

- **Programmeringsspråk**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Rammeverk & SDK-er**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databaser**: PostgreSQL med pgvector-utvidelse
- **Skyplattformer**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Byggeverktøy**: npm, Maven, pip, Cargo
- **Dokumentasjon**: Markdown med automatisert flerspråklig oversettelse (48+ språk)

### Arkitektur

- **11 kjernermoduler (00-11)**: Sekvensiell læringssti fra grunnleggende til avanserte emner
- **Praktiske laboratorier**: Praktiske øvelser med komplett løsningskode i flere språk
- **Eksempelprosjekter**: Funksjonelle MCP-server- og klientimplementeringer
- **Oversettelsessystem**: Automatisert GitHub Actions arbeidsflyt for flerspråklig støtte
- **Bildeelementer**: Sentral katalog for bilder med oversatte versjoner

## Oppsettkommandoer

Dette er et depot fokusert på dokumentasjon. Mesteparten av oppsett skjer i individuelle eksempelprosjekter og laboratorier.

### Oppsett av depot

```bash
# Klon depotet
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Arbeide med eksempelprosjekter

Eksempelprosjekter finnes i:
- `03-GettingStarted/samples/` - Språkspecifikke eksempler
- `03-GettingStarted/01-first-server/solution/` - Første serverimplementeringer
- `03-GettingStarted/02-client/solution/` - Klientimplementeringer
- `11-MCPServerHandsOnLabs/` - Omfattende laboratorier for databaseintegrasjon

Hvert eksempelprosjekt inneholder egne oppsettinstruksjoner:

#### TypeScript/JavaScript-prosjekter
```bash
cd <project-directory>
npm install
npm start
```

#### Python-prosjekter
```bash
cd <project-directory>
pip install -r requirements.txt
# eller
pip install -e .
python main.py
```

#### Java-prosjekter
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Utviklingsarbeidsflyt

### MCP 7-28 Forberedelse

#### Sjekkliste for repo-forberedelse

- [x] **Ny bidragsyter klarhet**: Denne filen definerer depotets formål,
  struktur, retningslinjer for bidrag og oppsettveier for eksempler.
- [x] **Bygge/teste/lint-kommandoer med eksakte flagg**:
  - Lint av depotdokumentasjon:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Gjennomgang av lenkemønster i depotdokumentasjon:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validering av TypeScript-eksempler:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validering av Python-eksempler:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validering av Java-eksempler:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Én realistisk arbeidsflyt som kan bli et MCP-verktøy**:
  `validate_curriculum_change`
- [x] **Inndata/utdata er eksplisitte** (se spesifikasjon nedenfor).
- [x] **Tillatelser og feilmåter er dokumentert** (se spesifikasjon nedenfor).
- [x] **CI-testbarhet er eksplisitt** (deterministiske kommandoer, eksplisitte
  avslutningskoder og maskinlesbare utdata).

#### Kandidat MCP-verktøy arbeidsflyt: `validate_curriculum_change`

##### Mål

Validere dokumentasjonsendringer i læreplan og representativ eksempelkode
tilstand før sammenslåing.

##### Inndata

- `changed_paths: string[]` (obligatorisk) - relative baner endret i PR.
- `run_docs_lint: boolean` (standard `true`)
- `run_links_audit: boolean` (standard `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (standard alle `false`)

##### Utdata

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Tillatelser

- Bare les arbeidsområdefiler og skriv verktøy-genererte artefakter (f.eks. lint
  rapporter, testlogger); ikke skriv til `translations/` eller
  `translated_images/`.
- Utfør lokale shell-kommandoer.
- Valgfri nettverkstilgang kun for pakke-gjenoppretting (`npm ci`,
  `python -m pip install`, `mvn` avhengighetsoppløsning).
- Ingen tillatelse til å pushe, merge eller redigere `translations/` eller
  `translated_images/`.

##### Feilmoduser

- `E_NO_INPUT_PATHS`: `changed_paths` tom.
- `E_INVALID_PATH`: inndata-bane går utenfor depotrot.
- `E_LINT_FAILED`: markdown lint avslutter med feil.
- `E_LINK_AUDIT_FAILED`: lenkegjennomgang kommando avslutter med feil.
- `E_SAMPLE_TEST_FAILED`: eksempeltest/bygg avslutter med feil.
- `E_TIMEOUT`: kommando overskred konfigurert tidsavbrudd.

##### Anbefalt CI-kontrakt

For å automatisere validering, konfigurer et CI-jobb som:

- Trigger på pull requests som berører `*.md`, eksempelkode eller denne filen.
- Kjører de nøyaktige kommandoene listet ovenfor.
- Lagre logger som artefakter.
- Feiler jobben ved alle ikke-null avkastningskoder.

#### Hvis du leverer en MCP-server fra dette depotet

- [ ] Les utkastet til endringslogg for MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Kjør serveren din med SDK-betaer:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Fjern sesjons- og håndtrykksantakelser; behandle hver forespørsel som
  selvstendig:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Send `Mcp-Method` og `Mcp-Name` headers for rå HTTP-forespørsler:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Gjennomgå hardkodede feilkoder (`missing resource` flyttet fra `-32002` til `-32602`).
- [ ] Flagge og planlegge migrasjon for utdatert røtter, sampling og
  logging:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrer bort fra den eksperimentelle `2025-11-25` Tasks API:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Gjennomgå autorisasjon for OAuth og OpenID Connect-forsterkning:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Dokumentasjonsstruktur

- **Moduler 00-11**: Kjernekursinnhold i sekvensiell rekkefølge
- **translations/**: Språkspesifikke versjoner (automatisk genererte, ikke rediger direkte)
- **translated_images/**: Lokalisert bildeversjoner (automatisk generert)
- **images/**: Kildebilder og diagrammer

### Gjøre endringer i dokumentasjonen

1. Rediger kun de engelske markdown-filene i rotmodulmappene (00-11)
2. Oppdater bilder i `images/`-katalogen om nødvendig
3. co-op-translator GitHub Action genererer automatisk oversettelser
4. Oversettelser regenereres ved push til main branch

### Arbeide med oversettelser

- **Automatisk oversettelse**: GitHub Actions arbeidsflyt håndterer alle oversettelser
- Ikke rediger filer manuelt i `translations/`-katalogen
- Oversettelsesmetadata er innebygd i hver oversatt fil
- Støttede språk: 48+ språk inkludert arabisk, kinesisk, fransk, tysk, hindi, japansk, koreansk, portugisisk, russisk, spansk, og flere

## Testinstruksjoner

### Validering av dokumentasjon

Siden dette først og fremst er et dokumentasjonsdepot, fokuserer testing på:

1. **Lenkemønster-gjennomgang**: List Markdown-lenker til gjennomgang

   ```bash
   # List Markdown-lenker (mønsterrevisjon)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validering av kodeeksempler**: Test at kodeeksempler kompileres/ kjøres

   ```bash
   # Naviger til en spesifikk prøve og kjør testene dens
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown linting**: Sjekk formateringskonsistens

   ```bash
   # Bruk markdownlint om nødvendig
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testing av eksempelprosjekter

Hvert språkspesifikke eksempel inkluderer egen testmetode:

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

## Kodestil-retningslinjer

### Dokumentasjonsstil

- Bruk klart, nybegynnervennlig språk
- Inkluder kodeeksempler i flere språk der det er relevant
- Følg markdown beste praksis:
  - Bruk ATX-stil overskrifter (`#` syntaks)
  - Bruk gjerdekoder med språkindikatorer
  - Inkluder beskrivende alt-tekst for bilder
  - Hold linjelengder rimelige (ingen hard grense, men vær fornuftig)

### Stil for kodeeksempler

#### TypeScript/JavaScript
- Bruk ES-moduler (`import`/`export`)
- Følg streng TypeScript-modus konvensjoner
- Inkluder typerdeklarasjoner
- Målrett ES2022

#### Python
- Følg PEP 8 stilretningslinjer
- Bruk type hints der passende
- Inkluder docstrings for funksjoner og klasser
- Bruk moderne Python-funksjoner (3.8+)

#### Java
- Følg Spring Boot-konvensjoner
- Bruk Java 21-funksjoner
- Følg standard Maven prosjektstruktur
- Inkluder Javadoc-kommentarer

### Filer og organisering

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

## Bygg og distribusjon

### Dokumentasjonsdistribusjon

Depotet bruker GitHub Pages eller lignende for hosting av dokumentasjon (hvis aktuelt). Endringer i main branch utløser:

1. Oversettelsesarbeidsflyt (`.github/workflows/co-op-translator.yml`)
2. Automatisert oversettelse av alle engelske markdown-filer
3. Bildeflokalisering etter behov

### Ingen byggprosess nødvendig

Dette depotet inneholder primært markdown-dokumentasjon. Ingen kompilering eller byggeprosess kreves for kjernelæreplaninnholdet.

### Distribusjon av eksempelprosjekter

Enkelte eksempelprosjekter kan ha distribusjonsinstruksjoner:
- Se `03-GettingStarted/09-deployment/` for veiledning i MCP-serverdistribusjon
- Eksempler på distribusjon til Azure Container Apps i `11-MCPServerHandsOnLabs/`

## Retningslinjer for bidrag

### Pull Request-prosess

1. **Fork og klon**: Fork depotet og klon din fork lokalt
2. **Lag en gren**: Bruk beskrivende grennavn (f.eks. `fix/typo-module-3`, `add/python-example`)
3. **Gjør endringer**: Rediger kun engelske markdown-filer (ikke oversettelser)
4. **Test lokalt**: Verifiser at markdown rendres riktig
5. **Send inn PR**: Bruk klare PR-titler og beskrivelser
6. **CLA**: Signer Microsoft Contributor License Agreement ved forespørsel

### PR-tittelformat

Bruk klare, beskrivende titler:
- `[Module XX] Kort beskrivelse` for modulspecifikke endringer
- `[Samples] Beskrivelse` for endringer i eksempelkode
- `[Docs] Beskrivelse` for generelle dokumentasjonsoppdateringer

### Hva man kan bidra med

- Feilrettinger i dokumentasjon eller kodeeksempler
- Nye kodeeksempler i flere språk
- Klargjøringer og forbedringer i eksisterende innhold
- Nye casestudier eller praktiske eksempler
- Feilrapporter for uklart eller feil innhold

### Hva man IKKE skal gjøre

- Ikke rediger filer direkte i `translations/`-katalogen
- Ikke rediger `translated_images/`-katalogen
- Ikke legg til store binærfiler uten diskusjon
- Ikke endre oversettelsesarbeidsflyt-filer uten koordinering

## Tilleggsnotater

### Vedlikehold av depot

- **Endringslogg**: Alle betydelige endringer dokumenteres i `changelog.md`
- **Studieveiledning**: Bruk `study_guide.md` for oversikt over læreplannavigasjon
- **Issue-maler**: Bruk GitHub-issue-maler for feilrapporter og funksjonsforespørsler
- **Oppførselskode**: Alle bidragsytere må følge Microsoft Open Source Code of Conduct

### Læringssti

Følg moduler i sekvensiell rekkefølge (00-11) for optimal læring:
1. **00-02**: Grunnleggende (Introduksjon, kjernekonsepter, sikkerhet)
2. **03**: Kom i gang med praktisk implementering
3. **04-05**: Praktisk implementering og avanserte emner
4. **06-10**: Fellesskap, beste praksis, og virkelige applikasjoner
5. **11**: Omfattende laboratorier for databaseintegrasjon (13 sekvensielle laboratorier)

### Støtteressurser

- **Dokumentasjon**: https://modelcontextprotocol.io/
- **Spesifikasjon**: https://spec.modelcontextprotocol.io/
- **Fellesskap**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord-server
- **Relaterte kurs**: Se README.md for andre Microsoft læringsstier

### Vanlige feilsøkingstips

**Q: Min PR feiler oversettelsessjekken**
A: Sørg for at du kun redigerte engelske markdown-filer i rotmodul-mappene, ikke oversatte versjoner.

**Q: Hvordan legger jeg til et nytt språk?**
A: Språkstøtte håndteres gjennom co-op-translator-arbeidsflyten. Åpne en issue for å diskutere nye språk.

**Q: Kodeeksempler fungerer ikke**

Svar: Sørg for at du har fulgt oppsettinstruksjonene i README-filen til det spesifikke eksempelet. Sjekk at du har riktige versjoner av avhengigheter installert.

**Spørsmål: Bilder vises ikke**
Svar: Kontroller at bildefilene har relative stier og bruker skråstreker. Bildene bør være i `images/`-katalogen eller `translated_images/` for lokaliserte versjoner.

### Ytelseshensyn

- Oversettelsesarbeidsflyten kan ta flere minutter å fullføre
- Store bilder bør optimaliseres før innsending
- Hold individuelle markdown-filer fokuserte og rimelig store
- Bruk relative lenker for bedre portabilitet

### Prosjektstyring

Dette prosjektet følger Microsofts praksiser for åpen kildekode:
- MIT-lisens for kode og dokumentasjon
- Microsofts åpen kildekode-atferdskodeks
- CLA kreves for bidrag
- Sikkerhetsproblemer: Følg retningslinjene i SECURITY.md
- Support: Se SUPPORT.md for hjelperessurser

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->