# AGENTS.md

## Projectoverzicht

**MCP voor Beginners** is een open-source educatief curriculum om het Model Context Protocol (MCP) te leren - een gestandaardiseerd raamwerk voor interacties tussen AI-modellen en clientapplicaties. Deze repository biedt uitgebreide leermaterialen met praktische codevoorbeelden in meerdere programmeertalen.

### Kerntechnologieën

- **Programmeertalen**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDK's**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databases**: PostgreSQL met pgvector-extensie
- **Cloudplatforms**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Bouwtools**: npm, Maven, pip, Cargo
- **Documentatie**: Markdown met geautomatiseerde vertaling in meerdere talen (48+ talen)

### Architectuur

- **11 Kernmodules (00-11)**: Opeenvolgend leertraject van fundamenten tot gevorderde onderwerpen
- **Hands-on Labs**: Praktische oefeningen met volledige oplossing in meerdere talen
- **Voorbeeldprojecten**: Werkende MCP-server en clientimplementaties
- **Vertalingssysteem**: Geautomatiseerde GitHub Actions workflow voor meertalige ondersteuning
- **Beeldassets**: Gecentraliseerde afbeeldingsmap met vertaalde versies

## Setup-opdrachten

Dit is een documentatiegerichte repository. De meeste setup vindt plaats binnen individuele voorbeeldprojecten en labs.

### Repository setup

```bash
# Maak een kloon van de repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Werken met voorbeeldprojecten

Voorbeeldprojecten bevinden zich in:
- `03-GettingStarted/samples/` - Taal-specifieke voorbeelden
- `03-GettingStarted/01-first-server/solution/` - Eerste serverimplementaties
- `03-GettingStarted/02-client/solution/` - Clientimplementaties
- `11-MCPServerHandsOnLabs/` - Uitgebreide databankintegratielabs

Elk voorbeeldproject bevat eigen setup-instructies:

#### TypeScript/JavaScript-projecten
```bash
cd <project-directory>
npm install
npm start
```

#### Python-projecten
```bash
cd <project-directory>
pip install -r requirements.txt
# of
pip install -e .
python main.py
```

#### Java-projecten
```bash
cd <project-directory>
mvn clean install
mvn spring-boot:run
```

## Ontwikkelworkflow

### MCP 7-28 Gereedheid

#### Checklist gereedheid repo

- [x] **Duidelijkheid voor nieuwe bijdragers**: Dit bestand definieert het doel van de repository, 
  structuur, bijdrage regels en voorbeeld setup paden.
- [x] **Build/test/lint opdrachten met exacte vlaggen**:
  - Markdown lint voor de repository docs:
    `npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"`
  - Audit linkpatroon voor repository docs:
    `find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"`
  - TypeScript voorbeeldvalidatie:
    `cd 03-GettingStarted/samples/typescript && npm ci && npm test && npm run build`
  - Python voorbeeldvalidatie:
    `cd 10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp && python -m pip install -e . && pytest -q`
  - Java voorbeeldvalidatie:
    `cd 03-GettingStarted/samples/java/calculator && mvn -B -ntp test verify`
- [x] **Één realistische workflow die een MCP-tool kan worden**:
  `validate_curriculum_change`
- [x] **Inputs/outputs zijn expliciet** (zie specificatie hieronder).
- [x] **Rechten en faalwijzen zijn gedocumenteerd** (zie specificatie hieronder).
- [x] **CI testbaarheid is expliciet** (deterministische opdrachten, expliciete
  exit codes en machine-leesbare outputs).

#### Kandidaat MCP tool workflow: `validate_curriculum_change`

##### Doel

Valideer documentatie wijzigingen in het curriculum en representatieve voorbeeldcode
gezondheid vóór samenvoeging.

##### Inputs

- `changed_paths: string[]` (verplicht) - relatieve paden gewijzigd in PR.
- `run_docs_lint: boolean` (standaard `true`)
- `run_links_audit: boolean` (standaard `true`)
- `run_samples: { typescript?: boolean, python?: boolean, java?: boolean }`
  (standaard alles `false`)

##### Outputs

- `status: "ok" | "failed"`
- `checks: Array<{ name: string, command: string, exit_code: number,
  summary: string }>`
- `artifacts: Array<{ type: "log" | "report", path: string }>`
- `failed_checks: string[]`

##### Rechten

- Alleen leesrechten voor workspace-bestanden en schrijfrechten voor toolgegenereerde artefacten (bijv. lint
  rapporten, testlogs); geen schrijfrechten voor `translations/` of
  `translated_images/`.
- Voer lokale shell-commando's uit.
- Optionele netwerktoegang alleen voor pakket herstel (`npm ci`,
  `python -m pip install`, `mvn` dependency-resolutie).
- Geen toestemming om te pushen, mergen of wijzigen in `translations/` of
  `translated_images/`.

##### Faalwijzen

- `E_NO_INPUT_PATHS`: `changed_paths` is leeg.
- `E_INVALID_PATH`: inputpad ontsnapt aan de root van de repository.
- `E_LINT_FAILED`: markdown lint stopt met niet-nul exitcode.
- `E_LINK_AUDIT_FAILED`: link audit commando stopt met niet-nul exitcode.
- `E_SAMPLE_TEST_FAILED`: voorbeeld test/build stopt met niet-nul exitcode.
- `E_TIMEOUT`: commando overschreed ingestelde timeout.

##### Aanbevolen CI-contract

Om validatie te automatiseren, configureer een CI-taak die:

- Wordt geactiveerd door pull requests die `*.md`, voorbeeldcode, of dit bestand raken.
- Voert de exacte hierboven genoemde opdrachten uit.
- Bewaart logs als artefacten.
- Faalt de taak bij elke niet-nul exitcode.

#### Als je een MCP-server vanuit deze repo uitbrengt

- [ ] Lees de concept changelog voor MCP 7-28:
  <https://modelcontextprotocol.io/specification/draft/changelog>
- [ ] Test je server met SDK-bèta's:
  <https://blog.modelcontextprotocol.io/posts/sdk-betas-2026-07-28/>
- [ ] Verwijder sessie- en handshakemodellen; behandel elk verzoek als
  zelfstandige eenheid:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#a-stateless-protocol>
- [ ] Zend `Mcp-Method` en `Mcp-Name` headers voor raw HTTP-verzoeken:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#routable-cacheable-traceable>
- [ ] Audit hardcoded foutcodes (`missing resource` is verschoven van `-32002` naar `-32602`).
- [ ] Markeer en plan migratie voor verouderde roots, sampling, en
  logging:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#roots-sampling-and-logging-are-deprecated>
- [ ] Migreer van de experimentele `2025-11-25` Tasks API:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#tasks-graduates-to-an-extension>
- [ ] Bekijk autorisatie voor OAuth en OpenID Connect versterking:
  <https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/#authorization-hardening>

### Documentatiestructuur

- **Modules 00-11**: Kerninhoud curriculum in opeenvolgende volgorde
- **translations/**: Taal-specifieke versies (automatisch gegenereerd, niet direct bewerken)
- **translated_images/**: Gelokaliseerde afbeeldingsversies (automatisch gegenereerd)
- **images/**: Bronafbeeldingen en diagrammen

### Documentatiewijzigingen aanbrengen

1. Bewerk alleen de Engelse markdownbestanden in de root module mappen (00-11)
2. Werk afbeeldingen in de map `images/` bij indien nodig
3. De co-op-translator GitHub Action genereert automatisch vertalingen
4. Vertalingen worden opnieuw gegenereerd bij push naar main branch

### Werken met vertalingen

- **Geautomatiseerde vertaling**: GitHub Actions workflow verzorgt alle vertalingen
- **Bewerk NOOIT handmatig** bestanden in de map `translations/`
- Vertaal metadata is ingebed in elk vertaald bestand
- Ondersteunde talen: 48+ talen waaronder Arabisch, Chinees, Frans, Duits, Hindi, Japans, Koreaans, Portugees, Russisch, Spaans en nog veel meer

## Testinstructies

### Documentatievalidatie

Omdat dit vooral een documentatierepository is, richt testen zich op:

1. **Linkpatroon audit**: Markdown links om te controleren

   ```bash
   # Lijst Markdown links (patrooncontrole)
   find . -name "*.md" -not -path "*/node_modules/*" -not -path "./translations/*" -not -path "./translated_images/*" -print0 | xargs -0 grep -En "\[.*\]\(.*\)"
   ```

2. **Codevoorbeeldvalidatie**: Test dat codevoorbeelden compileren/uitvoeren

   ```bash
   # Navigeer naar specifieke sample en voer de tests ervan uit
   cd 03-GettingStarted/samples/typescript
   npm install && npm test
   ```

3. **Markdown linting**: Controleer op consistentie in opmaak

   ```bash
   # Gebruik markdownlint indien nodig
   npx --yes markdownlint-cli2 "**/*.md" "#node_modules" "#translations" "#translated_images"
   ```

### Testen van voorbeeldprojecten

Elke taal-specifieke sample bevat zijn eigen testaanpak:

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

## Code Stijlrichtlijnen

### Documentatiestijl

- Gebruik duidelijke, voor beginners begrijpelijke taal
- Voeg codevoorbeelden toe in meerdere talen waar van toepassing
- Volg beste markdownpraktijken:
  - Gebruik ATX-stijl headers (`#`-syntaxis)
  - Gebruik fenced code blocks met taalidentificaties
  - Voeg beschrijvende alt-tekst voor afbeeldingen toe
  - Houd regel lengtes redelijk (geen harde limiet, maar wees verstandig)

### Stijl codevoorbeelden

#### TypeScript/JavaScript
- Gebruik ES modules (`import`/`export`)
- Volg de strikte TypeScript conventies
- Voeg type-aanduidingen toe
- Richt op ES2022

#### Python
- Volg PEP 8-stijlgids
- Gebruik type hints waar passend
- Voeg docstrings toe voor functies en klassen
- Gebruik moderne Python-functies (3.8+)

#### Java
- Volg Spring Boot conventies
- Gebruik Java 21 functies
- Volg standaard Maven-projectstructuur
- Voeg Javadoc opmerkingen toe

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

## Build en Deployment

### Documentatie Deployment

De repository gebruikt GitHub Pages of vergelijkbaar voor hosting van documentatie (indien van toepassing). Wijzigingen aan de main branch activeren:

1. Vertaalworkflow (`.github/workflows/co-op-translator.yml`)
2. Geautomatiseerde vertaling van alle Engelse markdownbestanden
3. Lokalisatie van afbeeldingen waar nodig

### Geen buildproces vereist

Deze repository bevat hoofdzakelijk markdown documentatie. Er is geen compilatie- of bouwstap nodig voor de kerninhoud van het curriculum.

### Deployment van voorbeeldprojecten

Individuele voorbeeldprojecten kunnen deploymentinstructies bevatten:
- Zie `03-GettingStarted/09-deployment/` voor MCP server deployment richtlijnen
- Azure Container Apps deploymentvoorbeelden in `11-MCPServerHandsOnLabs/`

## Bijdrager richtlijnen

### Pull Request proces

1. **Fork en Clone**: Fork de repository en clone je fork lokaal
2. **Maak een tak aan**: Gebruik beschrijvende taknamen (bijv. `fix/typo-module-3`, `add/python-example`)
3. **Breng wijzigingen aan**: Bewerk alleen Engelse markdownbestanden (niet de vertalingen)
4. **Test lokaal**: Controleer dat markdown correct wordt weergegeven
5. **Verzend PR**: Gebruik duidelijke PR-titels en beschrijvingen
6. **CLA**: Onderteken de Microsoft Contributor License Agreement wanneer daarom gevraagd wordt

### PR Titel Formaat

Gebruik duidelijke, beschrijvende titels:
- `[Module XX] Korte beschrijving` voor modulespecifieke wijzigingen
- `[Samples] Beschrijving` voor wijzigingen in voorbeeldcode
- `[Docs] Beschrijving` voor algemene documentatie-updates

### Waarvoor bijdragen

- Foutoplossingen in documentatie of codevoorbeelden
- Nieuwe codevoorbeelden in extra talen
- Verduidelijkingen en verbeteringen van bestaande inhoud
- Nieuwe casestudy’s of praktische voorbeelden
- Issue-rapporten voor onduidelijke of incorrecte inhoud

### Wat NIET te doen

- Bewerk bestanden in de map `translations/` niet rechtstreeks
- Bewerk de map `translated_images/` niet
- Voeg geen grote binaire bestanden toe zonder overleg
- Wijzig vertaalworkflow-bestanden niet zonder afstemming

## Aanvullende opmerkingen

### Repositoryonderhoud

- **Changelog**: Alle significante wijzigingen worden gedocumenteerd in `changelog.md`
- **Studiegids**: Gebruik `study_guide.md` voor overzicht van curriculumnavigatie
- **Issue-templates**: Gebruik GitHub-issue-templates voor bug rapporten en feature-verzoeken
- **Gedragscode**: Alle bijdragers moeten de Microsoft Open Source Gedragscode volgen

### Leerpad

Volg modules in opeenvolgende volgorde (00-11) voor optimaal leren:
1. **00-02**: Fundamenten (Introductie, Kernconcepten, Beveiliging)
2. **03**: Aan de slag met hands-on implementatie
3. **04-05**: Praktische implementatie en gevorderde onderwerpen
4. **06-10**: Community, best practices en toepassingen in de praktijk
5. **11**: Uitgebreide databankintegratielabs (13 opeenvolgende labs)

### Ondersteuningsbronnen

- **Documentatie**: https://modelcontextprotocol.io/
- **Specificatie**: https://spec.modelcontextprotocol.io/
- **Community**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Foundry Discord-server
- **Gerelateerde cursussen**: Zie README.md voor andere Microsoft leerpaden

### Veelvoorkomende problemen oplossen

**Q: Mijn PR faalt de vertaalcheck**
A: Zorg dat je alleen Engelse markdownbestanden in de root module mappen hebt bewerkt, niet de vertaalde versies.

**Q: Hoe voeg ik een nieuwe taal toe?**
A: Taalondersteuning wordt beheerd via de co-op-translator workflow. Open een issue om nieuwe talen te bespreken.

**Q: Codevoorbeelden werken niet**

A: Zorg ervoor dat je de installatie-instructies in de README van het specifieke voorbeeld hebt gevolgd. Controleer of je de juiste versies van de afhankelijkheden hebt geïnstalleerd.

**V: Afbeeldingen worden niet weergegeven**
A: Controleer of de afbeeldingspaden relatief zijn en gebruik schuine strepen naar voren. Afbeeldingen moeten zich bevinden in de `images/` map of `translated_images/` voor gelokaliseerde versies.

### Prestatie-overwegingen

- De vertaalworkflow kan enkele minuten duren om te voltooien
- Grote afbeeldingen moeten worden geoptimaliseerd voordat ze worden gecommit
- Houd individuele markdown-bestanden gericht en redelijk van omvang
- Gebruik relatieve links voor betere draagbaarheid

### Projectbeheer

Dit project volgt Microsoft open source-praktijken:
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