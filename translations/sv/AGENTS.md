# AGENTS.md

## Projektöversikt

**MCP för nybörjare** är en öppen källkodsutbildning för att lära sig Model Context Protocol (MCP) - en standardiserad ram för interaktioner mellan AI-modeller och klientapplikationer. Detta arkiv tillhandahåller omfattande lärandematerial med praktiska kodexempel på flera programmeringsspråk.

### Nyckelteknologier

- **Programmeringsspråk**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Ramverk & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databaser**: PostgreSQL med pgvector-tillägg
- **Molnplattformar**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Byggverktyg**: npm, Maven, pip, Cargo
- **Dokumentation**: Markdown med automatiserad flerspråkig översättning (48+ språk)

### Arkitektur

- **11 kärnmoduler (00-11)**: Sekventiell inlärningsväg från grunder till avancerade ämnen
- **Praktiska labbar**: Praktiska övningar med komplett lösningskod på flera språk
- **Exempelprojekt**: Fungerande MCP-server och klientimplementationer
- **Översättningssystem**: Automatiserat GitHub Actions-arbetsflöde för flerspråkigt stöd
- **Bildresurser**: Centraliserad bildmapp med översatta versioner

## Kommandon för installation

Detta är ett dokumentationsfokuserat arkiv. Den mesta installationen sker inom individuella exempelprojekt och labbar.

### Arkivinrättning

```bash
# Klona förrådet
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

## Utvecklingsflöde

### MCP 7-28 Förberedelse

#### Checklista för arkivförberedelse

- [x] **Tydlighet för nya bidragsgivare**: Denna fil definierar arkivets syfte,
  struktur, bidragsregler och exempel på installationsvägar.
- [x] **Bygg/test/lint-kommandon med exakta flaggor**:
  - Lintning av arkivets dokumentation:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Revision av länkstruktur i dokumentationen:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validering av TypeScript-exempel:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validering av Python-exempel:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validering av Java-exempel:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Ett realistiskt arbetsflöde som kan bli ett MCP-verktyg**:
  `validate_curriculum_change`
- [x] **In- och utdata är tydliga** (se specifikation nedan).
- [x] **Behörigheter och felhanteringslägen är dokumenterade** (se specifikation nedan).
- [x] **CI-testbarhet är tydlig** (deterministiska kommandon, tydliga
  avbrottskoder och maskinläsbara utdata).

#### Kandidat till MCP-verktygsarbetsflöde: `validate_curriculum_change`

##### Mål

Validera hälsotillståndet för dokumentationsändringar i kursmaterialet och representativ exempel kod
innan sammanslagning.

##### Indata

- `changed_paths: string[]` (obligatoriskt) - relativa sökvägar ändrade i PR.
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
- Utföra lokala shell-kommandon.
- Valfritt nätverksåtkomst endast för paketåterställning (`npm ci`,
  `python -m pip install`, `mvn` beroendehantering).
- Ingen behörighet att pusha, slå ihop eller ändra `translations/` eller
  `translated_images/`.

##### Felhanteringslägen

- `E_NO_INPUT_PATHS`: `changed_paths` är tom.
- `E_INVALID_PATH`: indata-sökväg går utanför arkivets rot.
- `E_LINT_FAILED`: markdown lint avslutas med icke-noll.
- `E_LINK_AUDIT_FAILED`: länkrevisionskommando avslutas med icke-noll.
- `E_SAMPLE_TEST_FAILED`: test/bygg av exempel avslutas med icke-noll.
- `E_TIMEOUT`: kommando överskred konfigurerad timeout.

##### Rekommenderat CI-kontrakt

För att automatisera validering, konfigurera en CI-jobb som:

- Triggas vid pull-förfrågningar som berör `*.md`, exempel kod eller denna fil.
- Kör de exakta kommandon som anges ovan.
- Sparar loggar som artefakter.
- Skickar jobb vid vilken icke-noll avbrottskod som helst.

#### Om du levererar en MCP-server från detta arkiv

- [ ] Läs utkast till ändringslogg för MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Kör din server mot SDK-betaversioner:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Ta bort antaganden om session och handskakning; behandla varje förfrågan som
  självständig:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Skicka `Mcp-Method` och `Mcp-Name` headers för råa HTTP-förfrågningar:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Revidera hårdkodade felkoder (`missing resource` flyttad från `-32002` till `-32602`).

- [ ] Flagga och planera migrering för föråldrade rötter, sampling och
  loggning:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migrera bort från den experimentella `2025-11-25` Tasks API:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Granska auktorisation för OAuth och OpenID Connect förstärkning:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Dokumentationsstruktur

- **Moduler 00-11**: Kärninnehåll i kursplan, i sekventiell ordning
- **translations/**: Språkspecifika versioner (automatiskt genererade, redigera inte direkt)
- **translated_images/**: Lokala bildversioner (automatiskt genererade)
- **images/**: Originalbilder och diagram

### Göra dokumentationsändringar

1. Redigera endast de engelska markdown-filerna i root-modulkatalogerna (00-11)
2. Uppdatera bilder i katalogen `images/` om det behövs
3. GitHub Action co-op-translator genererar automatiskt översättningar
4. Översättningar regenereras vid push till main-branchen

### Arbeta med översättningar

- **Automatiserad översättning**: GitHub Actions workflow hanterar alla översättningar
- Redigera INTE manuellt filer i katalogen `translations/`
- Översättningsmetadata är inbäddad i varje översatt fil
- Stödda språk: 48+ språk inklusive arabiska, kinesiska, franska, tyska, hindi, japanska, koreanska, portugisiska, ryska, spanska med flera

## Testinstruktioner

### Dokumentationsvalidering

Eftersom detta huvudsakligen är ett dokumentationsförråd fokuserar testning på:

1. **Länkgranskning**: Lista Markdown-länkar för granskning

   ```bash
   # Lista Markdown-länkar (mönsterrevision)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Kodexempelvalidering**: Testa att kodexempel kompileras/körs

   ```bash
   # Navigera till specifikt prov och kör dess tester
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown-lintning**: Kontrollera formateringskonsekvens

   ```bash
   # Använd markdownlint vid behov
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testning av exempelprojekt

Varje språkspecifikt exempel inkluderar sin egen testmetod:

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

- Använd klar och nybörjarvänlig språkstil
- Inkludera kodexempel i flera språk där det är tillämpligt
- Följ markdowns bästa praxis:
  - Använd ATX-stil på rubriker (syntax med `#`)
  - Använd inhägnade kodblock med språkspecifika identifierare
  - Inkludera beskrivande alt-text för bilder
  - Håll radlängder rimliga (ingen hård gräns, men var förnuftig)

### Kodexempelstil

#### TypeScript/JavaScript
- Använd ES-moduler (`import`/`export`)
- Följ TypeScripts striktläges-konventioner
- Inkludera typannoteringar
- Rikta mot ES2022

#### Python
- Följ PEP 8 stilriktlinjer
- Använd typanteckningar där det är lämpligt
- Inkludera docstrings för funktioner och klasser
- Använd moderna Python-funktioner (3.8+)

#### Java
- Följ Spring Boot-konventioner
- Använd Java 21-funktioner
- Följ standard Maven-projektstruktur
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

## Kompilering och distribution

### Dokumentationsdistribution

Förtroendet använder GitHub Pages eller liknande för dokumentationshosting (om tillämpligt). Ändringar i main-branchen utlöser:

1. Översättningsarbetsflöde (`.github/workflows/co-op-translator.yml`)
2. Automatisk översättning av alla engelska markdown-filer
3. Lokaliseringsanpassning av bilder vid behov

### Ingen kompileringsprocess krävs

Detta förtroende innehåller huvudsakligen markdown-dokumentation. Ingen kompilerings- eller byggsteg behövs för kärnkurinnehållet.

### Exempelprojektsdistribution

Enskilda exempelprojekt kan ha distributionsinstruktioner:
- Se `03-GettingStarted/09-deployment/` för MCP-serverdistributionsanvisningar
- Exempel på Azure Container Apps-distribution i `11-MCPServerHandsOnLabs/`

## Bidragsriktlinjer

### Process för pull requests

1. **Forka och Klona**: Forka förtroendet och klona din fork lokalt
2. **Skapa en gren**: Använd beskrivande grennamn (t.ex. `fix/typo-module-3`, `add/python-example`)
3. **Gör ändringar**: Redigera endast engelska markdown-filer (inte översättningar)
4. **Testa lokalt**: Verifiera att markdown renderas korrekt
5. **Skicka PR**: Använd tydliga PR-titlar och beskrivningar
6. **CLA**: Skriv under Microsoft Contributor License Agreement när det efterfrågas

### PR-titelformat

Använd tydliga, beskrivande titlar:
- `[Module XX] Kort beskrivning` för modulspecifika ändringar
- `[Samples] Beskrivning` för kodexempeländringar
- `[Docs] Beskrivning` för allmänna dokumentationsuppdateringar

### Vad att bidra med

- Buggfixar i dokumentation eller kodexempel
- Nya kodexempel på fler språk
- Förtydliganden och förbättringar av befintligt innehåll
- Nya fallstudier eller praktiska exempel
- Felrapporter för oklart eller felaktigt innehåll

### Vad man INTE ska göra

- Redigera inte filer direkt i katalogen `translations/`
- Redigera inte katalogen `translated_images/`
- Lägg inte till stora binära filer utan diskussion
- Ändra inte översättningsarbetsflödesfiler utan samordning

## Ytterligare anmärkningar

### Förtroendesunderhåll

- **Changelog**: Alla viktiga ändringar dokumenteras i `changelog.md`
- **Studieguide**: Använd `study_guide.md` för översikt av kursnavigering
- **Issue-mallar**: Använd GitHub issue-mallar för bugg- och funktionsförfrågningar
- **Uppförandekod**: Alla bidragsgivare måste följa Microsoft Open Source Code of Conduct

### Inlärningsväg

Följ moduler i sekventiell ordning (00-11) för optimal inlärning:
1. **00-02**: Grunderna (Introduktion, Kärnkoncept, Säkerhet)
2. **03**: Kom igång med praktisk implementation
3. **04-05**: Praktisk implementering och avancerade ämnen
4. **06-10**: Gemenskap, bästa praxis och realistiska tillämpningar
5. **11**: Omfattande databasintegrationslaborationer (13 sekventiella labbar)

### Supportresurser

- **Dokumentation**: https://modelcontextprotocol.io/
- **Specifikation**: https://spec.modelcontextprotocol.io/
- **Community**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord-server
- **Relaterade kurser**: Se README.md för andra Microsoft-inlärningsvägar

### Vanliga felsökningar

**F: Min PR misslyckas översättningskontrollen**
S: Kontrollera att du endast redigerat engelska markdown-filer i root-modulkataloger, inte översatta versioner.

**F: Hur lägger jag till ett nytt språk?**
S: Språkstöd hanteras via arbetsflödet co-op-translator. Öppna en issue för att diskutera tillägg av nya språk.

**F: Kodexempel fungerar inte**

Svar: Se till att du har följt installationsinstruktionerna i den specifika provfilens README. Kontrollera att du har rätt versioner av beroenden installerade.

**Fråga: Bilder visas inte**
Svar: Kontrollera att bildsökvägar är relativa och använder framåtslässtreck. Bilder ska finnas i mappen `images/` eller `translated_images/` för lokaliserade versioner.

### Prestandahänsyn

- Översättningsarbetsflödet kan ta flera minuter att slutföra
- Stora bilder bör optimeras innan de sparas
- Håll enskilda markdown-filer fokuserade och rimligt stora
- Använd relativa länkar för bättre portabilitet

### Projektstyrning

Detta projekt följer Microsofts öppna källkodsprinciper:
- MIT-licens för kod och dokumentation
- Microsofts uppförandekod för öppen källkod
- CLA krävs för bidrag
- Säkerhetsfrågor: Följ riktlinjerna i SECURITY.md
- Support: Se SUPPORT.md för hjälpresurser

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->