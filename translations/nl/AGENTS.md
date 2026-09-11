# AGENTS.md

## Projectoverzicht

**MCP voor Beginners** is een open-source onderwijsprogramma om het Model Context Protocol (MCP) te leren - een gestandaardiseerd kader voor interacties tussen AI-modellen en clientapplicaties. Deze repository biedt uitgebreide leermaterialen met praktische codevoorbeelden in meerdere programmeertalen.

### Belangrijke Technologieën

- **Programmeertalen**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDK's**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databases**: PostgreSQL met pgvector-extensie
- **Cloud Platforms**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Build Tools**: npm, Maven, pip, Cargo
- **Documentatie**: Markdown met automatische vertaling in meerdere talen (48+ talen)

### Architectuur

- **11 Kernmodules (00-11)**: Opeenvolgende leerlijn van basis tot gevorderde onderwerpen
- **Hands-on Labs**: Praktische oefeningen met complete oplossingscode in meerdere talen
- **Voorbeeldprojecten**: Werkende MCP-server en client implementaties
- **Vertalingssysteem**: Geautomatiseerde GitHub Actions workflow voor meertalige ondersteuning
- **Afbeeldingsbronnen**: Gecentraliseerde afbeeldingsdirectory met vertaalde versies

## Setup Commando's

Dit is een documentatiegerichte repository. De meeste setup vindt plaats binnen individuele voorbeeldprojecten en labs.

### Repository Setup

```bash
# Kloneer de repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Werken met Voorbeeldprojecten

Voorbeeldprojecten bevinden zich in:
- `03-GettingStarted/samples/` - Taal-specifieke voorbeelden
- `03-GettingStarted/01-first-server/solution/` - Eerste server implementaties
- `03-GettingStarted/02-client/solution/` - Client implementaties
- `11-MCPServerHandsOnLabs/` - Uitgebreide database integratie labs

Elk voorbeeldproject bevat zijn eigen setup-instructies:

#### TypeScript/JavaScript Projecten
```bash
cd <project-directory>
npm install
npm start
```

#### Python Projecten
```bash
cd <project-directory>
pip install -r requirements.txt
# of
pip install -e .
python main.py
```

#### Java Projecten
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Ontwikkelworkflow

### MCP 7-28 Gereedheid

#### Repo gereedheid checklist

- [x] **Duidelijkheid voor nieuwe bijdragers**: Dit bestand definieert repository-doel,
  structuur, bijdragenregels en voorbeeld setup-paden.
- [x] **Build/test/lint commando's met exacte flags**:
  - Documentatie lint van de repository:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Controle patroon links in repository docs:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - Validatie TypeScript voorbeelden:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Validatie Python voorbeelden:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Validatie Java voorbeelden:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Een realistische workflow die een MCP-tool kan worden**:
  `validate_curriculum_change`
- [x] **Inputs/outputs zijn expliciet** (zie specificatie hieronder).
- [x] **Rechten en faalwijzen zijn gedocumenteerd** (zie specificatie hieronder).
- [x] **CI testbaarheid is expliciet** (deterministische commando’s, expliciete
  exitcodes, en machine-leesbare outputs).

#### Kandidaten workflow MCP-tool: `validate_curriculum_change`

##### Doel

Valideren van curriculum documentatie veranderingen en representatieve voorbeeldcode
gezondheid voor samenvoeging.

##### Inputs

- `changed_paths: string[]` (verplicht) - relatieve paden gewijzigd in PR.
- `run_docs_lint: boolean` (standaard `true`)
- `run_links_audit: boolean` (standaard `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (standaard alle `false`)

##### Outputs

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Rechten

- Alleen lezen van workspace-bestanden en schrijven van toolgegenereerde artefacten (bijv. lint
  rapporten, testlogs); geen schrijfrechten in `translations/` of
  `translated_images/`.
- Uitvoeren van lokale shellcommando’s.
- Optioneel netwerktoegang alleen voor pakketherstel (`npm ci`,
  `python -m pip install`, `mvn` afhankelijkheid resolutie).
- Geen toestemming om te pushen, samen te voegen, of aan te passen in `translations/` of
  `translated_images/`.

##### Faalwijzen

- `E_NO_INPUT_PATHS`: `changed_paths` is leeg.
- `E_INVALID_PATH`: invoerpad ontsnapt aan root van repository.
- `E_LINT_FAILED`: markdown lint keert met niet-nul exitcode.
- `E_LINK_AUDIT_FAILED`: link-audit commando keert met niet-nul exitcode.
- `E_SAMPLE_TEST_FAILED`: sample test/build keert met niet-nul exitcode.
- `E_TIMEOUT`: commando overschreed ingestelde timeout.

##### Aanbevolen CI-contract

Om validatie te automatiseren, configureer een CI-job die:

- Activeert bij pull requests die `*.md`, voorbeeldcode of dit bestand aanraken.
- Voert de exacte hierboven genoemde commando’s uit.
- Bewaart logs als artefacten.
- Faalt de job bij elke niet-nul exitcode.

#### Als je een MCP-server uit deze repo oplevert

- [ ] Lees de definitieve MCP `2026-07-28` changelog:
  <https://modelcontextprotocol.io/specification/2026-07-28/changelog>
- [ ] Verifieer dat de geselecteerde SDK-release MCP `2026-07-28` ondersteunt:
  <https://modelcontextprotocol.io/docs/sdk>
- [ ] Verwijder sessie- en handshake-aanames; behandel iedere aanvraag als
  op zichzelf staand:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/lifecycle>
- [ ] Stuur `Mcp-Method` en `Mcp-Name` headers voor ruwe HTTP-aanvragen:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http>
- [ ] Controleer hardcoded foutcodes (`missing resource` verplaatst van `-32002` naar `-32602`).
- [ ] Migreer verouderde Roots, Sampling, Logging, en Dynamische Client
  Registratie:
  <https://modelcontextprotocol.io/specification/2026-07-28/deprecated>
- [ ] Migreer van de experimentele `2025-11-25` Tasks API:
  <https://modelcontextprotocol.io/extensions/tasks>
- [ ] Beoordeel autorisatie voor OAuth en OpenID Connect beveiliging:
  <https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization>

### Documentatiestructuur

- **Modules 00-11**: Kerninhoud van het curriculum in opeenvolgende volgorde
- **translations/**: Taal-specifieke versies (automatisch gegenereerd, niet rechtstreeks bewerken)
- **translated_images/**: Gelokaliseerde afbeeldingversies (automatisch gegenereerd)
- **images/**: Bronafbeeldingen en diagrammen

### Documentatiewijzigingen maken

1. Bewerk alleen de Engelse markdownbestanden in de root module mappen (00-11)
2. Werk afbeeldingen in de `images/` directory bij indien nodig
3. De co-op-translator GitHub Action genereert automatisch vertalingen
4. Vertalingen worden opnieuw gegenereerd bij push naar de main branch

### Werken met Vertalingen

- **Automatische Vertaling**: GitHub Actions workflow regelt alle vertalingen
- **Bewerk bestanden in `translations/` directory NIET handmatig**
- Vertaalmetadata is ingebed in elk vertaald bestand
- Ondersteunde talen: 48+ talen waaronder Arabisch, Chinees, Frans, Duits, Hindi, Japans, Koreaans, Portugees, Russisch, Spaans, en veel meer

## Testinstructies

### Documentatie-validatie

Omdat dit voornamelijk een documentatie-repository is, ligt de focus van testen op:

1. **Linkpatroon Controle**: Lijst Markdown-links voor controle

   ```bash
   # Markdown-links opsommen (patrooncontrole)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Validatie Codevoorbeelden**: Test dat codevoorbeelden compileren/runnen

   ```bash
   # Navigeer naar een specifiek voorbeeld en voer de tests uit
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown Linting**: Controleer formatteerconsistentie

   ```bash
   # Gebruik markdownlint indien nodig
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testen Voorbeeldprojecten

Elk taal-specifiek voorbeeld bevat een eigen testaanpak:

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

## Code Style Richtlijnen

### Documentatiestijl

- Gebruik duidelijke, voor beginners begrijpelijke taal
- Voeg codevoorbeelden in meerdere talen toe waar van toepassing
- Volg markdown beste praktijken:
  - Gebruik ATX-stijl headers (`#` syntax)
  - Gebruik fenced code blocks met taalidentificaties
  - Voeg beschrijvende alt-tekst toe voor afbeeldingen
  - Houd regellengtes redelijk (geen harde limiet, maar wees redelijk)

### Stijl Codevoorbeelden

#### TypeScript/JavaScript
- Gebruik ES modules (`import`/`export`)
- Volg TypeScript strict mode conventies
- Voeg type-annotaties toe
- Richt op ES2022

#### Python
- Volg PEP 8 stijlrichtlijnen
- Gebruik type hints waar passend
- Voeg docstrings toe voor functies en klassen
- Gebruik moderne Python features (3.8+)

#### Java
- Volg Spring Boot conventies
- Gebruik Java 21 features
- Volg standaard Maven projectstructuur
- Voeg Javadoc commentaar toe

### Bestandsorganisatie

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

## Build en Deploy

### Documentatie Deployment

De repository gebruikt GitHub Pages of vergelijkbaar voor hosting van documentatie (indien van toepassing). Wijzigingen in de main branch triggeren:

1. Vertaalworkflow (`.github/workflows/co-op-translator.yml`)
2. Geautomatiseerde vertaling van alle Engelse markdownbestanden
3. Lokalisatie van afbeeldingen indien nodig

### Geen Build Proces Nodig

Deze repository bevat voornamelijk markdown documentatie. Geen compilatie of build stap is nodig voor de kerninhoud van het curriculum.

### Voorbeeldproject Deployment

Individuele voorbeeldprojecten kunnen deployment-instructies hebben:
- Zie `03-GettingStarted/09-deployment/` voor MCP-server deployment richtlijnen
- Azure Container Apps deployment voorbeelden in `11-MCPServerHandsOnLabs/`

## Bijdrager Richtlijnen

### Pull Request Proces

1. **Fork en Clone**: Fork de repository en clone je fork lokaal
2. **Maak een Branch aan**: Gebruik beschrijvende branchnamen (bijv. `fix/typo-module-3`, `add/python-example`)
3. **Maak Wijzigingen**: Bewerk alleen Engelse markdownbestanden (niet vertalingen)
4. **Test Lokaal**: Controleer dat markdown correct wordt weergegeven
5. **Dien PR in**: Gebruik duidelijke PR-titels en beschrijvingen
6. **CLA**: Onderteken de Microsoft Contributor License Agreement wanneer gevraagd

### PR Titel Formaat

Gebruik duidelijke, beschrijvende titels:
- `[Module XX] Korte beschrijving` voor modulespecifieke wijzigingen
- `[Samples] Beschrijving` voor wijzigingen in voorbeeldcode
- `[Docs] Beschrijving` voor algemene documentatie-updates

### Wat bij te dragen

- Bugfixes in documentatie of codevoorbeelden
- Nieuwe codevoorbeelden in aanvullende talen
- Verduidelijkingen en verbeteringen van bestaande inhoud
- Nieuwe casestudy’s of praktische voorbeelden
- Foutmeldingen voor onduidelijke of incorrecte inhoud

### Wat NIET te doen

- Bewerk bestanden in `translations/` directory niet rechtstreeks
- Bewerk de `translated_images/` directory niet
- Voeg geen grote binaire bestanden toe zonder overleg
- Wijzig vertaalworkflowbestanden niet zonder coördinatie

## Aanvullende Notities

### Repository Onderhoud

- **Changelog**: Alle belangrijke wijzigingen zijn gedocumenteerd in `changelog.md`
- **Studiegids**: Gebruik `study_guide.md` voor een overzicht van curriculumnavigatie
- **Issue Templates**: Gebruik GitHub issue templates voor bugrapporten en functieverzoeken
- **Gedragscode**: Alle bijdragers moeten de Microsoft Open Source Gedragscode naleven

### Leerpad

Volg modules in volgorde (00-11) voor optimaal leren:
1. **00-02**: Grondslagen (Introductie, Kernconcepten, Beveiliging)
2. **03**: Aan de slag met praktische implementatie
3. **04-05**: Praktische implementatie en gevorderde onderwerpen
4. **06-10**: Gemeenschap, best practices, en toepassingen in de praktijk
5. **11**: Uitgebreide database integratie labs (13 opeenvolgende labs)

### Ondersteuningsbronnen

- **Documentatie**: https://modelcontextprotocol.io/
- **Specificatie**: https://modelcontextprotocol.io/specification/2026-07-28/
- **Gemeenschap**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord-server
- **Gerelateerde Cursussen**: Zie README.md voor andere Microsoft leerpaden

### Veelvoorkomende Problemen Oplossen

**V: Mijn PR faalt de vertaalcontrole**
A: Zorg dat je alleen Engelse markdownbestanden in root module mappen hebt bewerkt, niet de vertaalde versies.

**V: Hoe voeg ik een nieuwe taal toe?**
A: Taalondersteuning wordt beheerd via de co-op-translator workflow. Open een issue om nieuwe talen toe te voegen te bespreken.

**V: Codevoorbeelden werken niet**
A: Zorg dat je de setup-instructies in de specifieke README van het voorbeeld gevolgd hebt. Controleer of je de juiste versies van afhankelijkheden hebt geïnstalleerd.

**V: Afbeeldingen worden niet weergegeven**

A: Verifieer of afbeeldingspaden relatief zijn en schuine strepen naar voren gebruiken. Afbeeldingen moeten in de `images/` map staan of `translated_images/` voor gelokaliseerde versies.

### Prestaties Overwegingen

- Vertaalworkflow kan enkele minuten duren om te voltooien
- Grote afbeeldingen moeten geoptimaliseerd worden voordat ze worden gecommit
- Houd individuele markdown-bestanden gefocust en redelijk van formaat
- Gebruik relatieve links voor betere draagbaarheid

### Projectbeheer

Dit project volgt Microsoft open source praktijk:
- MIT-licentie voor code en documentatie
- Microsoft Open Source Gedragscode
- CLA vereist voor bijdragen
- Beveiligingsproblemen: Volg de richtlijnen in SECURITY.md
- Ondersteuning: Zie SUPPORT.md voor hulpbronnen

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->