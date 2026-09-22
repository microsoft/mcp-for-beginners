# AGENTS.md

## Prosjektoversikt

**MCP for nybegynnere** er et åpen kildekode utdanningsopplegg for å lære Model Context Protocol (MCP) - en standardisert ramme for interaksjoner mellom AI-modeller og klientapplikasjoner. Dette depotet tilbyr omfattende læringsmateriell med praktiske kodeeksempler på flere programmeringsspråk.

### Viktige teknologier

- **Programmeringsspråk**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Rammeverk og SDKer**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databaser**: PostgreSQL med pgvector-utvidelse
- **Skyplattformer**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Byggeverktøy**: npm, Maven, pip, Cargo
- **Dokumentasjon**: Markdown med automatisert flerspråklig oversettelse (48+ språk)

### Arkitektur

- **11 kjernemoduler (00-11)**: Sekvensiell læringssti fra grunnleggende til avanserte emner
- **Hands-on-labber**: Praktiske øvelser med komplett løsningskode i flere språk
- **Eksempelprosjekter**: Funksjonelle MCP-server- og klientimplementasjoner
- **Oversettelsessystem**: Automatisert GitHub Actions-arbeidsflyt for flerspråklig støtte
- **Bilde-ressurser**: Sentralisert bildekatalog med oversatte versjoner

## Oppsettkommandoer

Dette er et dokumentasjonsfokusert depot. Det meste av oppsett skjer i individuelle eksempelprosjekter og labber.

### Depotoppsett

```bash
# Klon depotet
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Arbeide med eksempelprosjekter

Eksempelprosjekter finnes i:
- `03-GettingStarted/samples/` - språkspesifikke eksempler
- `03-GettingStarted/01-first-server/solution/` - Første serverimplementasjoner
- `03-GettingStarted/02-client/solution/` - Klientimplementasjoner
- `11-MCPServerHandsOnLabs/` - Omfattende databasintegrasjonslabber

Hvert eksempelprosjekt har egne oppsettinstruksjoner:

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

### MCP 7-28 klarhet

#### Sjekkliste for depotklarhet

- [x] **Klarhet for nye bidragsytere**: Denne filen definerer depotets formål,
  struktur, bidragsregler og eksempeloppsettstier.
- [x] **Kommandoer for bygg/test/lint med nøyaktige flagg**:
  - Depotdokumentasjonslint:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Revisjon av lenkemønster i depotdokumentasjon:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validering av TypeScript-eksempler:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validering av Python-eksempler:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validering av Java-eksempler:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **En realistisk arbeidsflyt som kan bli et MCP-verktøy**:
  `validate_curriculum_change`
- [x] **Inndata/utdata er eksplisitte** (se spesifikasjon nedenfor).
- [x] **Tillatelser og feilmoduser er dokumentert** (se spesifikasjon nedenfor).
- [x] **CI-testbarhet er eksplisitt** (deterministiske kommandoer, eksplisitte
  avslutningskoder og maskinlesbare utdata).

#### Kandidat MCP-verktøysarbeidsflyt: `validate_curriculum_change`

##### Mål

Validere endringer i læreplanens dokumentasjon og representativ eksempelkodeskikk
før fletting.

##### Inndata

- `changed_paths: string[]` (påkrevd) - relative stier som er endret i PR.
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

- Les arbeidsromfiler og skriv bare verktøygenererte artefakter (f.eks. lint
  rapporter, testlogger); ikke skriving til `translations/` eller
  `translated_images/`.
- Utfør lokale shell-kommandoer.
- Valgfri nettverkstilgang kun for pakkegjenoppretting (`npm ci`,
  `python -m pip install`, `mvn` avhengighetsoppløsning).
- Ingen tillatelse til å pushe, merge eller endre `translations/` eller
  `translated_images/`.

##### Feilmoduser

- `E_NO_INPUT_PATHS`: `changed_paths` er tom.
- `E_INVALID_PATH`: inndatasti går utenfor depotrot.
- `E_LINT_FAILED`: markdown lint returnerer ikke-null.
- `E_LINK_AUDIT_FAILED`: lenke-revisjonskommando returnerer ikke-null.
- `E_SAMPLE_TEST_FAILED`: prøve/test bygdkommando returnerer ikke-null.
- `E_TIMEOUT`: kommando oversteg konfigurert tidsavbrudd.

##### Anbefalt CI-kontrakt

For å automatisere validering, sett opp en CI-jobb som:

- Utløses ved pull requests som berører `*.md`, eksempelkode eller denne filen.
- Kjører de eksakte kommandoene som listet ovenfor.
- Bevarer logger som artefakter.
- Feiler jobben ved enhver ikke-null avslutningskode.

#### Hvis du leverer en MCP-server fra dette depotet

- [ ] Les den endelige MCP `2026-07-28` endringsloggen:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Verifiser at valgt SDK-utgivelse støtter MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Fjern antakelser om sesjon og håndtrykk; behandle hver forespørsel som
  selvstendig:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Send `Mcp-Method` og `Mcp-Name`-headere for rå HTTP-forespørsler:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Revider hardkodede feilkoder (`missing resource` flyttet fra `-32002` til `-32602`).
- [ ] Migrer fra utgåtte Roots, Sampling, Logging og Dynamic Client
  Registration:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrer bort fra eksperimentelle `2025-11-25` Tasks API:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Gå gjennom autorisasjon for OAuth og OpenID Connect-forsterkning:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Dokumentasjonsstruktur

- **Moduler 00-11**: Kjerneinnhold i læreplanen i sekvensiell rekkefølge
- **translations/**: Språkspesifikke versjoner (automatisk generert, ikke rediger direkte)
- **translated_images/**: Lokaliserte bildeversjoner (automatisk generert)
- **images/**: Kildebilder og diagrammer

### Gjøre endringer i dokumentasjonen

1. Rediger kun de engelske markdown-filene i roten til modulkatalogene (00-11)
2. Oppdater bilder i `images/` katalogen ved behov
3. co-op-translator GitHub Action genererer automatisk oversettelser
4. Oversettelser regenereres ved push til hovedgrenen

### Arbeide med oversettelser

- **Automatisert oversettelse**: GitHub Actions-arbeidsflyt håndterer alle oversettelser
- **Ikke rediger manuelt** filer i `translations/`-katalogen
- Oversettelsesmetadata er innebygd i hver oversatt fil
- Støttede språk: 48+ språk inkludert arabisk, kinesisk, fransk, tysk, hindi, japansk, koreansk, portugisisk, russisk, spansk og mange flere

## Testinstruksjoner

### Dokumentasjonsvalidering

Siden dette først og fremst er et dokumentasjonsdepot, fokuserer testingen på:

1. **Lenkemønster-revisjon**: List ut Markdown-lenker for gjennomgang

   ```bash
   # List opp Markdown-lenker (mønsterrevisjon)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validering av kodeeksempler**: Test at kodeeksemplene kompilerer/kjører

   ```bash
   # Naviger til spesifikt prøveeksempel og kjør testene dens
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown-linting**: Sjekk formateringskonsistens

   ```bash
   # Bruk markdownlint om nødvendig
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Test av eksempelprosjekter

Hvert språkspesifikt eksempel inkluderer sin egen testmetode:

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

## Retningslinjer for kodestil

### Dokumentasjonsstil

- Bruk klart og nybegynnervennlig språk
- Inkluder kodeeksempler i flere språk der det er relevant
- Følg beste praksis for markdown:
  - Bruk ATX-style overskrifter (`#`-syntaks)
  - Bruk gjerde-kodeblokker med språkindikatorer
  - Inkluder beskrivende alt-tekst for bilder
  - Hold linjelengder fornuftige (ingen hard grense, men vær rimelig)

### Stil for kodeeksempler

#### TypeScript/JavaScript
- Bruk ES-moduler (`import`/`export`)
- Følg TypeScript striktemodus-konvensjoner
- Inkluder typeannotasjoner
- Målrett mot ES2022

#### Python
- Følg PEP 8 stilretningslinjer
- Bruk typehint der det er relevant
- Inkluder docstrings for funksjoner og klasser
- Bruk moderne Python-funksjoner (3.8+)

#### Java
- Følg Spring Boot konvensjoner
- Bruk Java 21-funksjoner
- Følg standard Maven-prosjektstruktur
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

## Bygging og distribusjon

### Distribusjon av dokumentasjon

Depotet bruker GitHub Pages eller lignende for dokumentasjonsvert (dersom aktuelt). Endringer til hovedgrenen utløser:

1. Oversettelsesarbeidsflyt (`.github/workflows/co-op-translator.yml`)
2. Automatisk oversettelse av alle engelske markdown-filer
3. Bildeflokalisering ved behov

### Ikke nødvendig med byggprosess

Dette depotet inneholder først og fremst markdown-dokumentasjon. Ingen kompilering eller byggesteg er nødvendig for kjernelæreinnholdet.

### Distribusjon av eksempelprosjekt

Individuelle eksempelprosjekter kan ha distribusjonsinstruksjoner:
- Se `03-GettingStarted/09-deployment/` for veiledning om MCP-serverdistribusjon
- Eksempler på distribusjon av Azure Container Apps i `11-MCPServerHandsOnLabs/`

## Retningslinjer for bidrag

### Pull request-prosess

1. **Gaffel og klon**: Gaffel depotet og klon din gaffel lokalt
2. **Opprett en gren**: Bruk beskrivende grennavn (f.eks. `fix/typo-module-3`, `add/python-example`)
3. **Gjør endringer**: Rediger kun engelske markdown-filer (ikke oversettelser)
4. **Test lokalt**: Verifiser at markdown vises riktig
5. **Send PR**: Bruk klare PR-titler og beskrivelser
6. **CLA**: Signer Microsoft Contributor License Agreement når du blir bedt om det

### Format på PR-tittelen

Bruk klare, beskrivende titler:
- `[Module XX] Kort beskrivelse` for modulspesifikke endringer
- `[Samples] Beskrivelse` for endringer i eksempelkode
- `[Docs] Beskrivelse` for generelle dokumentasjonsoppdateringer

### Hva du kan bidra med

- Feilrettinger i dokumentasjon eller kodeeksempler
- Nye kodeeksempler i flere språk
- Presiseringer og forbedringer av eksisterende innhold
- Nye casestudier eller praktiske eksempler
- Rapporter om uklart eller feilaktig innhold

### Hva du ikke skal gjøre

- Ikke rediger direkte filer i `translations/`-katalogen
- Ikke rediger`translated_images/`-katalogen
- Ikke legg til store binærfiler uten diskusjon
- Ikke endre oversettelsesarbeidsflytfiler uten koordinering

## Tilleggsnotater

### Depotvedlikehold

- **Endringslogg**: Alle vesentlige endringer dokumenteres i `changelog.md`
- **Studieguide**: Bruk `study_guide.md` for oversikt over læreplannavigasjon
- **Issue-maler**: Bruk GitHub-issue-maler for feilrapporter og funksjonsforespørsler
- **Atferdskodeks**: Alle bidragsytere må følge Microsofts åpen kildekode atferdskodeks

### Læringssti

Følg moduler i sekvensiell rekkefølge (00-11) for optimal læring:
1. **00-02**: Grunnleggende (Introduksjon, kjernebegreper, sikkerhet)
2. **03**: Kom i gang med praktisk implementering
3. **04-05**: Praktisk implementering og avanserte temaer
4. **06-10**: Fellesskap, beste praksis og virkelige applikasjoner
5. **11**: Omfattende databasintegrasjonslabber (13 sekvensielle labber)

### Støtteressurser

- **Dokumentasjon**: https://modelcontextprotocol.io/
- **Spesifikasjon**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Fellesskap**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord-server
- **Relaterte kurs**: Se README.md for andre Microsoft læringsstier

### Vanlige feilsøkingsspørsmål

**Q: Min PR feiler oversettelsessjekken**
A: Sørg for at du kun redigerte engelske markdown-filer i rotmodulkatalogene, ikke oversatte versjoner.

**Q: Hvordan legger jeg til et nytt språk?**
A: Språkstøtte håndteres via co-op-translator-arbeidsflyten. Åpne en issue for å diskutere tillegg av nye språk.

**Q: Kodeeksempler fungerer ikke**
A: Sørg for at du har fulgt oppsettinstruksjonene i den spesifikke eksempel-READMEen. Kontroller at du har riktige versjoner av avhengigheter installert.

**Q: Bilder vises ikke**

A: Bekreft at bildefilstier er relative og bruker skråstreker. Bilder bør være i `images/`-katalogen eller `translated_images/` for lokaliserte versjoner.

### Ytelseshensyn

- Oversettelsesflyten kan ta flere minutter å fullføre
- Store bilder bør optimaliseres før innlevering
- Hold individuelle markdown-filer fokuserte og rimelig størrelsesmessig
- Bruk relative lenker for bedre portabilitet

### Prosjektstyring

Dette prosjektet følger Microsofts retningslinjer for åpen kildekode:
- MIT-lisens for kode og dokumentasjon
- Microsoft Open Source Code of Conduct
- CLA kreves for bidrag
- Sikkerhetsproblemer: Følg retningslinjene i SECURITY.md
- Støtte: Se SUPPORT.md for hjelperessurser

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->