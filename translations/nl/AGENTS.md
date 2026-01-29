# AGENTS.md

## Projectoverzicht

**MCP voor Beginners** is een open-source educatief curriculum voor het leren van het Model Context Protocol (MCP) - een gestandaardiseerd raamwerk voor interacties tussen AI-modellen en clienttoepassingen. Deze repository biedt uitgebreide leermaterialen met praktische codevoorbeelden in meerdere programmeertalen.

### Belangrijke technologieën

- **Programmeertalen**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Frameworks & SDK's**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databases**: PostgreSQL met pgvector-extensie
- **Cloudplatforms**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Buildtools**: npm, Maven, pip, Cargo
- **Documentatie**: Markdown met geautomatiseerde meertalige vertaling (48+ talen)

### Architectuur

- **11 Kernmodules (00-11)**: Een stapsgewijze leerroute van basisprincipes tot geavanceerde onderwerpen
- **Praktische Labs**: Praktische oefeningen met volledige oplossingscode in meerdere talen
- **Voorbeeldprojecten**: Werkende MCP-server- en clientimplementaties
- **Vertalingssysteem**: Geautomatiseerde GitHub Actions-workflow voor meertalige ondersteuning
- **Afbeeldingsbestanden**: Gecentraliseerde afbeeldingsmap met vertaalde versies

## Setupcommando's

Dit is een documentatiegerichte repository. De meeste setup vindt plaats binnen individuele voorbeeldprojecten en labs.

### Repository Setup

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Werken met voorbeeldprojecten

Voorbeeldprojecten zijn te vinden in:
- `03-GettingStarted/samples/` - Taal-specifieke voorbeelden
- `03-GettingStarted/01-first-server/solution/` - Eerste serverimplementaties
- `03-GettingStarted/02-client/solution/` - Clientimplementaties
- `11-MCPServerHandsOnLabs/` - Uitgebreide labs voor database-integratie

Elk voorbeeldproject bevat eigen setupinstructies:

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
# or
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

### Documentatiestructuur

- **Modules 00-11**: Kerncurriculum inhoud in stapsgewijze volgorde
- **translations/**: Taal-specifieke versies (automatisch gegenereerd, niet direct bewerken)
- **translated_images/**: Gelokaliseerde afbeeldingsversies (automatisch gegenereerd)
- **images/**: Bronafbeeldingen en diagrammen

### Wijzigingen in documentatie aanbrengen

1. Bewerk alleen de Engelse markdown-bestanden in de hoofdmodulemappen (00-11)
2. Werk afbeeldingen bij in de map `images/` indien nodig
3. De co-op-translator GitHub Action genereert automatisch vertalingen
4. Vertalingen worden opnieuw gegenereerd bij een push naar de hoofdbranch

### Werken met vertalingen

- **Geautomatiseerde vertaling**: GitHub Actions-workflow verzorgt alle vertalingen
- **NIET handmatig bewerken** van bestanden in de map `translations/`
- Vertalingsmetadata is ingebed in elk vertaald bestand
- Ondersteunde talen: 48+ talen, waaronder Arabisch, Chinees, Frans, Duits, Hindi, Japans, Koreaans, Portugees, Russisch, Spaans en vele anderen

## Testinstructies

### Validatie van documentatie

Aangezien dit voornamelijk een documentatierepository is, richt testen zich op:

1. **Linkvalidatie**: Zorg ervoor dat alle interne links werken
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validatie van codevoorbeelden**: Test of codevoorbeelden compileren/uitvoeren
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown-linting**: Controleer op consistentie in opmaak
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testen van voorbeeldprojecten

Elk taal-specifiek voorbeeld heeft zijn eigen testaanpak:

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

## Richtlijnen voor codestijl

### Documentatiestijl

- Gebruik duidelijke, beginnersvriendelijke taal
- Voeg codevoorbeelden toe in meerdere talen waar van toepassing
- Volg best practices voor markdown:
  - Gebruik ATX-stijl headers (`#`-syntax)
  - Gebruik afgebakende codeblokken met taalidentificatie
  - Voeg beschrijvende alt-tekst toe voor afbeeldingen
  - Houd de lengte van regels redelijk (geen harde limiet, maar wees verstandig)

### Stijl van codevoorbeelden

#### TypeScript/JavaScript
- Gebruik ES-modules (`import`/`export`)
- Volg TypeScript-strict mode-conventies
- Voeg typeannotaties toe
- Richt op ES2022

#### Python
- Volg PEP 8-stijlrichtlijnen
- Gebruik type hints waar passend
- Voeg docstrings toe voor functies en klassen
- Gebruik moderne Python-functies (3.8+)

#### Java
- Volg Spring Boot-conventies
- Gebruik Java 21-functies
- Volg standaard Maven-projectstructuur
- Voeg Javadoc-commentaar toe

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

## Build en implementatie

### Implementatie van documentatie

De repository gebruikt GitHub Pages of een vergelijkbare service voor het hosten van documentatie (indien van toepassing). Wijzigingen in de hoofdbranch activeren:

1. Vertalingsworkflow (`.github/workflows/co-op-translator.yml`)
2. Geautomatiseerde vertaling van alle Engelse markdown-bestanden
3. Lokalisatie van afbeeldingen indien nodig

### Geen buildproces vereist

Deze repository bevat voornamelijk markdown-documentatie. Er is geen compilatie- of buildstap nodig voor de kerncurriculuminhoud.

### Implementatie van voorbeeldprojecten

Individuele voorbeeldprojecten kunnen implementatie-instructies bevatten:
- Zie `03-GettingStarted/09-deployment/` voor richtlijnen voor MCP-serverimplementatie
- Voorbeelden van implementatie in Azure Container Apps in `11-MCPServerHandsOnLabs/`

## Richtlijnen voor bijdragen

### Pull Request-proces

1. **Fork en Clone**: Fork de repository en clone je fork lokaal
2. **Maak een branch**: Gebruik beschrijvende branchnamen (bijv. `fix/typo-module-3`, `add/python-example`)
3. **Breng wijzigingen aan**: Bewerk alleen Engelse markdown-bestanden (geen vertalingen)
4. **Test lokaal**: Controleer of markdown correct wordt weergegeven
5. **Dien PR in**: Gebruik duidelijke PR-titels en beschrijvingen
6. **CLA**: Onderteken de Microsoft Contributor License Agreement wanneer daarom wordt gevraagd

### Formaat PR-titel

Gebruik duidelijke, beschrijvende titels:
- `[Module XX] Korte beschrijving` voor module-specifieke wijzigingen
- `[Samples] Beschrijving` voor wijzigingen in voorbeeldcode
- `[Docs] Beschrijving` voor algemene documentatie-updates

### Wat bij te dragen

- Bugfixes in documentatie of codevoorbeelden
- Nieuwe codevoorbeelden in extra talen
- Verduidelijkingen en verbeteringen van bestaande inhoud
- Nieuwe casestudy's of praktische voorbeelden
- Probleemrapporten voor onduidelijke of onjuiste inhoud

### Wat NIET te doen

- Bewerk geen bestanden direct in de map `translations/`
- Bewerk geen bestanden in de map `translated_images/`
- Voeg geen grote binaire bestanden toe zonder overleg
- Wijzig geen bestanden van de vertalingsworkflow zonder coördinatie

## Aanvullende opmerkingen

### Onderhoud van de repository

- **Changelog**: Alle belangrijke wijzigingen worden gedocumenteerd in `changelog.md`
- **Studiegids**: Gebruik `study_guide.md` voor een overzicht van het curriculum
- **Probleemsjablonen**: Gebruik GitHub-probleemsjablonen voor bugrapporten en functieverzoeken
- **Gedragscode**: Alle bijdragers moeten de Microsoft Open Source Code of Conduct volgen

### Leerroute

Volg modules in stapsgewijze volgorde (00-11) voor optimaal leren:
1. **00-02**: Basisprincipes (Introductie, Kernconcepten, Beveiliging)
2. **03**: Aan de slag met praktische implementatie
3. **04-05**: Praktische implementatie en geavanceerde onderwerpen
4. **06-10**: Gemeenschap, best practices en toepassingen in de praktijk
5. **11**: Uitgebreide labs voor database-integratie (13 opeenvolgende labs)

### Ondersteuningsbronnen

- **Documentatie**: https://modelcontextprotocol.io/
- **Specificatie**: https://spec.modelcontextprotocol.io/
- **Gemeenschap**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord-server
- **Gerelateerde cursussen**: Zie README.md voor andere Microsoft-leerroutes

### Veelvoorkomende problemen oplossen

**Vraag: Mijn PR faalt bij de vertalingscontrole**
Antwoord: Zorg ervoor dat je alleen Engelse markdown-bestanden in de hoofdmodulemappen hebt bewerkt, niet de vertaalde versies.

**Vraag: Hoe voeg ik een nieuwe taal toe?**
Antwoord: Taalondersteuning wordt beheerd via de co-op-translator-workflow. Open een issue om het toevoegen van nieuwe talen te bespreken.

**Vraag: Codevoorbeelden werken niet**
Antwoord: Zorg ervoor dat je de setupinstructies in de specifieke README van het voorbeeld hebt gevolgd. Controleer of je de juiste versies van afhankelijkheden hebt geïnstalleerd.

**Vraag: Afbeeldingen worden niet weergegeven**
Antwoord: Controleer of afbeeldingspaden relatief zijn en gebruik forward slashes. Afbeeldingen moeten zich bevinden in de map `images/` of `translated_images/` voor gelokaliseerde versies.

### Prestatieoverwegingen

- De vertalingsworkflow kan enkele minuten duren
- Grote afbeeldingen moeten worden geoptimaliseerd voordat ze worden gecommit
- Houd individuele markdown-bestanden gefocust en redelijk van omvang
- Gebruik relatieve links voor betere draagbaarheid

### Projectbeheer

Dit project volgt Microsoft open source-praktijken:
- MIT-licentie voor code en documentatie
- Microsoft Open Source Code of Conduct
- CLA vereist voor bijdragen
- Beveiligingsproblemen: Volg de richtlijnen in SECURITY.md
- Ondersteuning: Zie SUPPORT.md voor hulpbronnen

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.