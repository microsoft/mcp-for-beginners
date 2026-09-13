# AGENTS.md

## Projektöversikt

**MCP för nybörjare** är en öppen källkodsutbildningsplan för att lära sig Model Context Protocol (MCP) - en standardiserad ram för interaktioner mellan AI-modeller och klientapplikationer. Detta förvar erbjuder omfattande lärmaterial med praktiska kodexempel i flera programmeringsspråk.

### Viktiga teknologier

- **Programmeringsspråk**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Ramar & SDK:er**:
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databaser**: PostgreSQL med pgvector-tillägg
- **Molnplattformar**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Byggverktyg**: npm, Maven, pip, Cargo
- **Dokumentation**: Markdown med automatiserad flerspråkig översättning (48+ språk)

### Arkitektur

- **11 kärnmoduler (00-11)**: Sekventiell lärandeväg från grundläggande till avancerade ämnen
- **Praktiska labbar**: Praktiska övningar med fullständig lösningskod i flera språk
- **Exempelprojekt**: Fungerande MCP server- och klientimplementationer
- **Översättningssystem**: Automatiserat GitHub Actions-flöde för flerspråkigt stöd
- **Bildresurser**: Centraliserad bildmapp med översatta versioner

## Konfigurationskommandon

Detta är ett dokumentationsinriktat repo. Det mesta av installationen sker inom de enskilda exempelprojekten och labbarna.

### Reposetup

```bash
# Klona arkivet
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Arbeta med exempelprojekt

Exempelprojekt finns i:
- `03-GettingStarted/samples/` - Språkspecifika exempel
- `03-GettingStarted/01-first-server/solution/` - Första serverimplementationer
- `03-GettingStarted/02-client/solution/` - Klientimplementationer
- `11-MCPServerHandsOnLabs/` - Omfattande databasintegrationslabbar

Varje exempelprojekt innehåller egna installationsinstruktioner:

#### TypeScript/JavaScript-projekt
```bash
cd <project-directory>
npm install
npm start
```

#### Python-projekt
```bash
cd <project-directory>
pip install -r requirements.txt
# eller
pip install -e .
python main.py
```

#### Java-projekt
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Utvecklingsarbetsflöde

### MCP 7-28 beredskap

#### Checklista för reposberedskap

- [x] **Tydlighet för nya bidragsgivare**: Denna fil definierar repo-ändamål,
  struktur, regler för bidrag, och exempelvägar för setup.
- [x] **Bygg/test/lint-kommandon med exakta flaggor**:
  - Lint för repodokumentation:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Repos dokumentations länkgranskningskommando:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript-exempelvalidering:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python-exempelvalidering:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java-exempelvalidering:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Ett realistiskt arbetsflöde som kan bli ett MCP-verktyg**:
  `validate_curriculum_change`
- [x] **Indata/utdata är explicit** (se specifikationen nedan).
- [x] **Behörigheter och felhanteringslägen dokumenteras** (se specifikationen nedan).
- [x] **CI-testbarhet är explicit** (deterministiska kommandon, explicita
  exitkoder, och maskinläsbara utdata).

#### Kandidat MCP-verktygsarbetsflöde: `validate_curriculum_change`

##### Mål

Validera ändringar i kursdokumentation och representativ exempelkod
hälsa före sammanslagning.

##### Indata

- `changed_paths: string[]` (obligatorisk) - relativa sökvägar ändrade i PR.
- `run_docs_lint: boolean` (standard `true`)
- `run_links_audit: boolean` (standard `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (standard alla `false`)

##### Utdata

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Behörigheter

- Läsa arbetsytans filer och skriva verktyggenererade artefakter (t.ex. lint-
  rapporter, testloggar) endast; inga skrivningar till `translations/` eller
  `translated_images/`.
- Exekvera lokala shell-kommandon.
- Valfri nätverksåtkomst endast för paketåterställning (`npm ci`,
  `python -m pip install`, `mvn` beroendeupplösning).
- Ingen behörighet att pusha, merga eller modifiera `translations/` eller
  `translated_images/`.

##### Felhanteringslägen

- `E_NO_INPUT_PATHS`: `changed_paths` tom.
- `E_INVALID_PATH`: indata sökväg går utanför repots rot.
- `E_LINT_FAILED`: markdown lint avslutas med annat än noll.
- `E_LINK_AUDIT_FAILED`: länkgranskning kommandot avslutas med annat än noll.
- `E_SAMPLE_TEST_FAILED`: exempeltest/bygge avslutas med annat än noll.
- `E_TIMEOUT`: kommando överskred konfigurerad timeout.

##### Rekommenderat CI-kontrakt

För att automatisera validering, konfigurera ett CI-jobb som:

- Startar vid pull requests som berör `*.md`, exempel-kod, eller denna fil.
- Kör de exakta kommandon som listas ovan.
- Behåller loggar som artefakter.
- Fäller jobbet vid alla icke-noll exitkoder.

#### Om du levererar en MCP-server från detta repo

- [ ] Läs den slutliga MCP `2026-07-28` ändringsloggen:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Verifiera att vald SDK-release stödjer MCP `2026-07-28`:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Ta bort session- och handskakningsantaganden; behandla varje förfrågan som
  självständig:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Skicka `Mcp-Method` och `Mcp-Name` headers för råa HTTP-förfrågningar:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Granska hårdkodade felkoder (`missing resource` flyttades från `-32002` till `-32602`).
- [ ] Migrera bort deprecated Roots, Sampling, Logging, och Dynamic Client
  Registration:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migrera från experimentella `2025-11-25` Tasks API:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Granska auktorisering för OAuth och OpenID Connect-härdning:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Dokumentationsstruktur

- **Moduler 00-11**: Kärninnehåll för läroplan i sekventiell ordning
- **translations/**: Språkspecifika versioner (automatiskt genererade, redigera inte direkt)
- **translated_images/**: Lokaliserade bildversioner (automatiskt genererade)
- **images/**: Källbilder och diagram

### Göra dokumentationsändringar

1. Redigera endast de engelska markdown-filerna i rotmodulkatalogerna (00-11)
2. Uppdatera bilder i `images/`-katalogen vid behov
3. co-op-translator GitHub Action genererar automatiskt översättningar
4. Översättningar skapas på nytt vid push till main-branchen

### Arbeta med översättningar

- **Automatiserad översättning**: GitHub Actions-flödet hanterar alla översättningar
- **Redigera INTE manuellt** filer i `translations/`-katalogen
- Översättningsmetadata är inbäddad i varje översatt fil
- Stödda språk: 48+ språk inklusive arabiska, kinesiska, franska, tyska, hindi, japanska, koreanska, portugisiska, ryska, spanska, och många fler

## Testinstruktioner

### Dokumentationsvalidering

Eftersom detta huvudsakligen är ett dokumentationsrepo, fokuserar testningen på:

1. **Länkgranskningsrevisionslista**: Lista Markdown-länkar för granskning

   ```bash
   # Lista Markdown-länkar (mönsteraudit)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Kodexempelvalidering**: Testa att kodexempel kompileras/körs

   ```bash
   # Navigera till specifikt prov och kör dess tester
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown-linting**: Kontrollera formatkonsistens

   ```bash
   # Använd markdownlint vid behov
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testning av exempelprojekt

Varje språksspecifikt exempel har sin egen testmetod:

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

## Kodstilriktlinjer

### Dokumentationsstil

- Använd klart, nybörjarvänligt språk
- Inkludera kodexempel i flera språk där det är möjligt
- Följ markdown bästa praxis:
  - Använd ATX-stil rubriker (`#` syntax)
  - Använd fenced code blocks med språkindikatorer
  - Inkludera beskrivande alt-text för bilder
  - Håll radernas längd rimlig (ingen hård gräns, men var förnuftig)

### Kodexempelstil

#### TypeScript/JavaScript
- Använd ES-moduler (`import`/`export`)
- Följ TypeScript strict mode-konventioner
- Inkludera typanteckningar
- Rikta in mot ES2022

#### Python
- Följ PEP 8 stilriktlinjer
- Använd typindikatorer där lämpligt
- Inkludera docstrings för funktioner och klasser
- Använd moderna Python-funktioner (3.8+)

#### Java
- Följ Spring Boot-konventioner
- Använd Java 21-funktioner
- Följ standard Maven projektstruktur
- Inkludera Javadoc-kommentarer

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

## Bygg och distribution

### Dokumentationsdistribution

Reposet använder GitHub Pages eller liknande för dokumentationshosting (om tillämpligt). Ändringar i main-branchen triggar:

1. Översättningsarbetsflöde (`.github/workflows/co-op-translator.yml`)
2. Automatiserad översättning av alla engelska markdown-filer
3. Bildlokalisering vid behov

### Inget byggsteg krävs

Detta repo innehåller huvudsakligen markdown-dokumentation. Ingen kompilering eller byggsteg behövs för kärninnehållet i läroplanen.

### Exempelprojektdistribution

Enskilda exempelprojekt kan ha distributionsinstruktioner:
- Se `03-GettingStarted/09-deployment/` för MCP serverdistributionsvägledningar
- Exempel på Azure Container Apps-distribution i `11-MCPServerHandsOnLabs/`

## Bidragsriktlinjer

### Pull request-process

1. **Forka och klona**: Forka repot och klona din fork lokalt
2. **Skapa en gren**: Använd beskrivande grennamn (t.ex. `fix/typo-module-3`, `add/python-example`)
3. **Gör ändringar**: Redigera endast engelska markdown-filer (inte översättningar)
4. **Testa lokalt**: Verifiera att markdown renderas korrekt
5. **Skicka PR**: Använd tydliga PR-titlar och beskrivningar
6. **CLA**: Skriv under Microsoft Contributor License Agreement när du uppmanas

### PR-titelformat

Använd tydliga, beskrivande titlar:
- `[Module XX] Kort beskrivning` för modulspecifika ändringar
- `[Samples] Beskrivning` för ändringar i exempel-kod
- `[Docs] Beskrivning` för allmänna dokumentationsuppdateringar

### Vad att bidra med

- Buggfixar i dokumentation eller kodexempel
- Nya kodexempel i fler språk
- Förtydliganden och förbättringar av befintligt innehåll
- Nya fallstudier eller praktiska exempel
- Felrapporter för oklart eller felaktigt innehåll

### Vad att inte göra

- Redigera inte direkt filer i `translations/`-katalogen
- Redigera inte `translated_images/`-katalogen
- Lägg inte till stora binära filer utan diskussion
- Byt inte översättningsarbetsflödesfiler utan samordning

## Ytterligare anmärkningar

### Repositories underhåll

- **Ändringslogg**: Alla viktiga ändringar dokumenteras i `changelog.md`
- **Studieguide**: Använd `study_guide.md` för överblick av läroplansnavigering
- **Issue-mallar**: Använd GitHub issue-mallar för buggrapporter och funktionsförfrågningar
- **Uppförandekod**: Alla bidragsgivare måste följa Microsoft Open Source Code of Conduct

### Lärväg

Följ moduler i sekventiell ordning (00-11) för optimalt lärande:
1. **00-02**: Grundläggande (Introduktion, kärnkoncept, säkerhet)
2. **03**: Kom igång med praktisk implementation
3. **04-05**: Praktisk implementation och avancerade ämnen
4. **06-10**: Gemenskap, bästa praxis och verkliga tillämpningar
5. **11**: Omfattande databasintegrationslabbar (13 sekventiella labbar)

### Supportresurser

- **Dokumentation**: https://modelcontextprotocol.io/
- **Specifikation**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Gemenskap**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord-servern
- **Relaterade kurser**: Se README.md för andra Microsoft-lärvägar

### Vanliga felsökningsfrågor

**F: Min PR misslyckas översättningskontrollen**
S: Se till att du endast redigerat engelska markdown-filer i rotdirektorierna, inte översatta versioner.

**F: Hur lägger jag till ett nytt språk?**
S: Språkstöd hanteras via co-op-translator-flödet. Öppna ett issue för att diskutera nya språk.

**F: Kodexempel fungerar inte**
S: Säkerställ att du följt installationsinstruktionerna i specifika exempel-README. Kontrollera att du har rätt versioner av beroenden installerade.

**F: Bilder visas inte**

A: Verifiera att bildvägar är relativa och använder snedstreck framåt. Bilder ska finnas i katalogen `images/` eller `translated_images/` för lokaliserade versioner.

### Prestandahänsyn

- Översättningsflödet kan ta flera minuter att slutföra
- Stora bilder bör optimeras innan de läggs till i versionhanteringen
- Håll enskilda markdown-filer fokuserade och rimligt stora
- Använd relativa länkar för bättre portabilitet

### Projektstyrning

Detta projekt följer Microsofts öppna källkodsmetoder:
- MIT-licens för kod och dokumentation
- Microsofts öppna källkodsuppförandekod
- CLA krävs för bidrag
- Säkerhetsfrågor: Följ SECURITY.md-riktlinjer
- Support: Se SUPPORT.md för hjälpresurser

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->