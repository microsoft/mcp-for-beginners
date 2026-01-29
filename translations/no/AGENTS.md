# AGENTS.md

## Prosjektoversikt

**MCP for Nybegynnere** er et åpen kildekode-opplæringsprogram for å lære Model Context Protocol (MCP) - et standardisert rammeverk for interaksjoner mellom AI-modeller og klientapplikasjoner. Dette repositoriet tilbyr omfattende læringsmateriale med praktiske kodeeksempler på flere programmeringsspråk.

### Viktige teknologier

- **Programmeringsspråk**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Rammeverk og SDK-er**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databaser**: PostgreSQL med pgvector-utvidelse
- **Skyplattformer**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Byggeverktøy**: npm, Maven, pip, Cargo
- **Dokumentasjon**: Markdown med automatisert oversettelse til flere språk (48+ språk)

### Arkitektur

- **11 Kjerne-moduler (00-11)**: Sekvensiell læringssti fra grunnleggende til avanserte emner
- **Praktiske laboratorier**: Øvelser med komplette løsningskoder på flere språk
- **Eksempelprosjekter**: Fungerende MCP-server og klientimplementasjoner
- **Oversettelsessystem**: Automatisert GitHub Actions-arbeidsflyt for støtte til flere språk
- **Bildefiler**: Sentralisert bildemappe med oversatte versjoner

## Oppsettskommandoer

Dette er et dokumentasjonsfokusert repositorium. Mesteparten av oppsettet skjer innenfor individuelle eksempelprosjekter og laboratorier.

### Repositorium-oppsett

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Arbeide med eksempelprosjekter

Eksempelprosjekter finnes i:
- `03-GettingStarted/samples/` - Språkspecifikke eksempler
- `03-GettingStarted/01-first-server/solution/` - Første serverimplementasjoner
- `03-GettingStarted/02-client/solution/` - Klientimplementasjoner
- `11-MCPServerHandsOnLabs/` - Omfattende laboratorier for databaseintegrasjon

Hvert eksempelprosjekt inneholder egne oppsettsinstruksjoner:

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
# or
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

### Dokumentasjonsstruktur

- **Moduler 00-11**: Kjerneinnhold i sekvensiell rekkefølge
- **translations/**: Språkspecifikke versjoner (automatisk generert, ikke rediger direkte)
- **translated_images/**: Lokaliserte bildeversjoner (automatisk generert)
- **images/**: Kildebilder og diagrammer

### Gjøre endringer i dokumentasjonen

1. Rediger kun de engelske markdown-filene i rotmodulens kataloger (00-11)
2. Oppdater bilder i `images/`-katalogen hvis nødvendig
3. GitHub Action "co-op-translator" genererer automatisk oversettelser
4. Oversettelser regenereres ved push til hovedgrenen

### Arbeide med oversettelser

- **Automatisk oversettelse**: GitHub Actions-arbeidsflyt håndterer alle oversettelser
- **IKKE rediger manuelt** filer i `translations/`-katalogen
- Oversettelsesmetadata er innebygd i hver oversatte fil
- Støttede språk: 48+ språk inkludert arabisk, kinesisk, fransk, tysk, hindi, japansk, koreansk, portugisisk, russisk, spansk og mange flere

## Testinstruksjoner

### Validering av dokumentasjon

Siden dette primært er et dokumentasjonsrepositorium, fokuserer testing på:

1. **Validering av lenker**: Sørg for at alle interne lenker fungerer
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Validering av kodeeksempler**: Test at kodeeksempler kompilerer/kjører
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown-linting**: Sjekk formatkonsistens
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testing av eksempelprosjekter

Hvert språkspecifikke eksempel inkluderer sin egen testtilnærming:

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

- Bruk klart, nybegynnervennlig språk
- Inkluder kodeeksempler på flere språk der det er relevant
- Følg beste praksis for markdown:
  - Bruk ATX-stil overskrifter (`#`-syntaks)
  - Bruk avgrensede kodeblokker med språkidentifikatorer
  - Inkluder beskrivende alt-tekst for bilder
  - Hold linjelengder rimelige (ingen hard grense, men vær fornuftig)

### Kodestil for eksempler

#### TypeScript/JavaScript
- Bruk ES-moduler (`import`/`export`)
- Følg TypeScript-strenge moduskonvensjoner
- Inkluder typeannotasjoner
- Målrett mot ES2022

#### Python
- Følg PEP 8-stilretningslinjer
- Bruk typehint der det er passende
- Inkluder docstrings for funksjoner og klasser
- Bruk moderne Python-funksjoner (3.8+)

#### Java
- Følg Spring Boot-konvensjoner
- Bruk Java 21-funksjoner
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

## Bygging og distribusjon

### Distribusjon av dokumentasjon

Repositoriet bruker GitHub Pages eller lignende for dokumentasjonsvert (hvis aktuelt). Endringer i hovedgrenen utløser:

1. Oversettelsesarbeidsflyt (`.github/workflows/co-op-translator.yml`)
2. Automatisk oversettelse av alle engelske markdown-filer
3. Lokaliserte bilder etter behov

### Ingen byggeprosess nødvendig

Dette repositoriet inneholder primært markdown-dokumentasjon. Ingen kompilering eller byggeprosess er nødvendig for kjerneinnholdet.

### Distribusjon av eksempelprosjekter

Individuelle eksempelprosjekter kan ha distribusjonsinstruksjoner:
- Se `03-GettingStarted/09-deployment/` for MCP-serverdistribusjonsveiledning
- Eksempler på distribusjon av Azure Container Apps i `11-MCPServerHandsOnLabs/`

## Retningslinjer for bidrag

### Prosess for pull requests

1. **Fork og klon**: Fork repositoriet og klon din fork lokalt
2. **Opprett en gren**: Bruk beskrivende gren-navn (f.eks. `fix/typo-module-3`, `add/python-example`)
3. **Gjøre endringer**: Rediger kun engelske markdown-filer (ikke oversettelser)
4. **Test lokalt**: Verifiser at markdown vises korrekt
5. **Send inn PR**: Bruk klare PR-titler og beskrivelser
6. **CLA**: Signer Microsoft Contributor License Agreement når du blir bedt om det

### Format for PR-titler

Bruk klare, beskrivende titler:
- `[Module XX] Kort beskrivelse` for modulspesifikke endringer
- `[Samples] Beskrivelse` for endringer i kodeeksempler
- `[Docs] Beskrivelse` for generelle dokumentasjonsoppdateringer

### Hva du kan bidra med

- Feilrettinger i dokumentasjon eller kodeeksempler
- Nye kodeeksempler på flere språk
- Klargjøringer og forbedringer av eksisterende innhold
- Nye casestudier eller praktiske eksempler
- Rapportering av problemer med uklart eller feilaktig innhold

### Hva du IKKE skal gjøre

- Ikke rediger filer direkte i `translations/`-katalogen
- Ikke rediger `translated_images/`-katalogen
- Ikke legg til store binærfiler uten diskusjon
- Ikke endre oversettelsesarbeidsflytfiler uten koordinering

## Ekstra notater

### Vedlikehold av repositoriet

- **Endringslogg**: Alle betydelige endringer dokumenteres i `changelog.md`
- **Studieguide**: Bruk `study_guide.md` for oversikt over opplæringsprogrammet
- **Problemmaler**: Bruk GitHub-malene for feilrapporter og funksjonsforespørsler
- **Adferdskodeks**: Alle bidragsytere må følge Microsoft Open Source Code of Conduct

### Læringssti

Følg modulene i sekvensiell rekkefølge (00-11) for optimal læring:
1. **00-02**: Grunnleggende (Introduksjon, Kjernekonsepter, Sikkerhet)
2. **03**: Kom i gang med praktisk implementering
3. **04-05**: Praktisk implementering og avanserte emner
4. **06-10**: Fellesskap, beste praksis og virkelige applikasjoner
5. **11**: Omfattende laboratorier for databaseintegrasjon (13 sekvensielle laboratorier)

### Støtteressurser

- **Dokumentasjon**: https://modelcontextprotocol.io/
- **Spesifikasjon**: https://spec.modelcontextprotocol.io/
- **Fellesskap**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord-server
- **Relaterte kurs**: Se README.md for andre Microsoft-læringsprogrammer

### Vanlige feilsøkingsspørsmål

**Spørsmål: Min PR feiler oversettelsessjekken**
Svar: Sørg for at du kun redigerte engelske markdown-filer i rotmodulens kataloger, ikke oversatte versjoner.

**Spørsmål: Hvordan legger jeg til et nytt språk?**
Svar: Språkstøtte administreres gjennom co-op-translator-arbeidsflyten. Åpne en sak for å diskutere å legge til nye språk.

**Spørsmål: Kodeeksempler fungerer ikke**
Svar: Sørg for at du har fulgt oppsettsinstruksjonene i den spesifikke eksemplets README. Sjekk at du har riktige versjoner av avhengigheter installert.

**Spørsmål: Bilder vises ikke**
Svar: Verifiser at bildefilbaner er relative og bruker skråstreker. Bilder skal være i `images/`-katalogen eller `translated_images/` for lokaliserte versjoner.

### Ytelseshensyn

- Oversettelsesarbeidsflyten kan ta flere minutter å fullføre
- Store bilder bør optimaliseres før de legges inn
- Hold individuelle markdown-filer fokuserte og rimelig størrelse
- Bruk relative lenker for bedre portabilitet

### Prosjektstyring

Dette prosjektet følger Microsofts praksis for åpen kildekode:
- MIT-lisens for kode og dokumentasjon
- Microsoft Open Source Code of Conduct
- CLA kreves for bidrag
- Sikkerhetsproblemer: Følg retningslinjene i SECURITY.md
- Støtte: Se SUPPORT.md for hjelperessurser

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.