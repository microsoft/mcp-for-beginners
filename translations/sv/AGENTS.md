# AGENTS.md

## Projektöversikt

**MCP för nybörjare** är en öppen utbildningsplan för att lära sig Model Context Protocol (MCP) - ett standardiserat ramverk för interaktioner mellan AI-modeller och klientapplikationer. Detta arkiv erbjuder omfattande utbildningsmaterial med praktiska kodexempel på flera programmeringsspråk.

### Viktiga teknologier

- **Programmeringsspråk**: C#, Java, JavaScript, TypeScript, Python, Rust
- **Ramverk & SDKs**: 
  - MCP SDK (`@modelcontextprotocol/sdk`)
  - Spring Boot (Java)
  - FastMCP (Python)
  - LangChain4j (Java)
- **Databaser**: PostgreSQL med pgvector-tillägg
- **Molnplattformar**: Azure (Container Apps, OpenAI, Content Safety, Application Insights)
- **Byggverktyg**: npm, Maven, pip, Cargo
- **Dokumentation**: Markdown med automatiserad översättning till flera språk (48+ språk)

### Arkitektur

- **11 kärnmoduler (00-11)**: Sekventiell utbildningsväg från grunder till avancerade ämnen
- **Praktiska övningar**: Praktiska uppgifter med kompletta lösningskoder på flera språk
- **Exempelprojekt**: Fungerande MCP-server och klientimplementeringar
- **Översättningssystem**: Automatiserat GitHub Actions-arbetsflöde för flerspråkigt stöd
- **Bildresurser**: Centraliserad bildkatalog med översatta versioner

## Installationskommandon

Detta är ett dokumentationsfokuserat arkiv. De flesta installationer sker inom individuella exempelprojekt och övningar.

### Arkivinstallation

```bash
# Clone the repository
git clone https://github.com/microsoft/mcp-for-beginners.git
cd mcp-for-beginners
```

### Arbeta med exempelprojekt

Exempelprojekt finns i:
- `03-GettingStarted/samples/` - Språkspecifika exempel
- `03-GettingStarted/01-first-server/solution/` - Första serverimplementeringar
- `03-GettingStarted/02-client/solution/` - Klientimplementeringar
- `11-MCPServerHandsOnLabs/` - Omfattande databasintegrationsövningar

Varje exempelprojekt innehåller sina egna installationsinstruktioner:

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
# or
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

### Dokumentationsstruktur

- **Moduler 00-11**: Kärninnehåll i sekventiell ordning
- **translations/**: Språkspecifika versioner (automatiskt genererade, redigera inte direkt)
- **translated_images/**: Lokaliserade bildversioner (automatiskt genererade)
- **images/**: Källbilder och diagram

### Göra ändringar i dokumentationen

1. Redigera endast de engelska markdown-filerna i rotmodulkatalogerna (00-11)
2. Uppdatera bilder i katalogen `images/` vid behov
3. GitHub Action "co-op-translator" genererar automatiskt översättningar
4. Översättningar genereras om vid push till huvudgrenen

### Arbeta med översättningar

- **Automatiserad översättning**: GitHub Actions-arbetsflöde hanterar alla översättningar
- **Redigera INTE** filer i katalogen `translations/`
- Översättningsmetadata är inbäddade i varje översatt fil
- Stödda språk: 48+ språk inklusive arabiska, kinesiska, franska, tyska, hindi, japanska, koreanska, portugisiska, ryska, spanska och många fler

## Testinstruktioner

### Dokumentationsvalidering

Eftersom detta främst är ett dokumentationsarkiv fokuserar testningen på:

1. **Länkvalidering**: Kontrollera att alla interna länkar fungerar
```bash
# Check for broken markdown links
find . -name "*.md" -type f | xargs grep -n "\[.*\](../../.*)"
```

2. **Kodexempelvalidering**: Testa att kodexempel kompilerar/körs
```bash
# Navigate to specific sample and run its tests
cd 03-GettingStarted/samples/typescript
npm install && npm test
```

3. **Markdown-lintning**: Kontrollera formatkonsistens
```bash
# Use markdownlint if needed
npx markdownlint-cli2 "**/*.md" "#node_modules"
```

### Testning av exempelprojekt

Varje språkspecifikt exempel har sin egen testmetod:

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

## Kodstilsguider

### Dokumentationsstil

- Använd tydligt, nybörjarvänligt språk
- Inkludera kodexempel på flera språk där det är tillämpligt
- Följ bästa praxis för markdown:
  - Använd ATX-stilrubriker (`#` syntax)
  - Använd avgränsade kodblock med språkidentifierare
  - Inkludera beskrivande alt-text för bilder
  - Håll rimliga linjelängder (ingen hård gräns, men var förnuftig)

### Kodexempelstil

#### TypeScript/JavaScript
- Använd ES-moduler (`import`/`export`)
- Följ TypeScript-strikta lägeskonventioner
- Inkludera typannoteringar
- Sikta på ES2022

#### Python
- Följ PEP 8-stilguider
- Använd typanvisningar där det är lämpligt
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

## Bygg och distribution

### Dokumentationsdistribution

Arkivet använder GitHub Pages eller liknande för dokumentationshosting (om tillämpligt). Ändringar i huvudgrenen utlöser:

1. Översättningsarbetsflöde (`.github/workflows/co-op-translator.yml`)
2. Automatiserad översättning av alla engelska markdown-filer
3. Bildlokalisering vid behov

### Ingen byggprocess krävs

Detta arkiv innehåller främst markdown-dokumentation. Ingen kompilering eller byggsteg behövs för kärninnehållet.

### Distribution av exempelprojekt

Individuella exempelprojekt kan ha distributionsinstruktioner:
- Se `03-GettingStarted/09-deployment/` för MCP-serverdistributionsvägledning
- Exempel på Azure Container Apps-distribution i `11-MCPServerHandsOnLabs/`

## Riktlinjer för bidrag

### Pull Request-process

1. **Fork och klona**: Forka arkivet och klona din fork lokalt
2. **Skapa en gren**: Använd beskrivande gren-namn (t.ex. `fix/typo-module-3`, `add/python-example`)
3. **Gör ändringar**: Redigera endast engelska markdown-filer (inte översättningar)
4. **Testa lokalt**: Kontrollera att markdown renderas korrekt
5. **Skicka PR**: Använd tydliga PR-titlar och beskrivningar
6. **CLA**: Signera Microsoft Contributor License Agreement när du blir ombedd

### PR-titelformat

Använd tydliga, beskrivande titlar:
- `[Module XX] Kort beskrivning` för modulspecifika ändringar
- `[Samples] Beskrivning` för ändringar i exempelkod
- `[Docs] Beskrivning` för allmänna dokumentationsuppdateringar

### Vad du kan bidra med

- Bugfixar i dokumentation eller kodexempel
- Nya kodexempel på ytterligare språk
- Förtydliganden och förbättringar av befintligt innehåll
- Nya fallstudier eller praktiska exempel
- Rapportering av problem med otydligt eller felaktigt innehåll

### Vad du INTE ska göra

- Redigera inte filer i katalogen `translations/`
- Redigera inte katalogen `translated_images/`
- Lägg inte till stora binära filer utan diskussion
- Ändra inte översättningsarbetsflödesfiler utan samordning

## Ytterligare anteckningar

### Arkivunderhåll

- **Ändringslogg**: Alla betydande ändringar dokumenteras i `changelog.md`
- **Studieguide**: Använd `study_guide.md` för översikt över utbildningsplanen
- **Problemformulär**: Använd GitHub-problemformulär för buggrapporter och funktionsförfrågningar
- **Uppförandekod**: Alla bidragsgivare måste följa Microsoft Open Source Code of Conduct

### Utbildningsväg

Följ modulerna i sekventiell ordning (00-11) för optimal inlärning:
1. **00-02**: Grunder (Introduktion, Kärnkoncept, Säkerhet)
2. **03**: Kom igång med praktisk implementering
3. **04-05**: Praktisk implementering och avancerade ämnen
4. **06-10**: Gemenskap, bästa praxis och verkliga applikationer
5. **11**: Omfattande databasintegrationsövningar (13 sekventiella övningar)

### Supportresurser

- **Dokumentation**: https://modelcontextprotocol.io/
- **Specifikation**: https://spec.modelcontextprotocol.io/
- **Gemenskap**: https://github.com/orgs/modelcontextprotocol/discussions
- **Discord**: Microsoft Azure AI Foundry Discord-server
- **Relaterade kurser**: Se README.md för andra Microsoft-utbildningsvägar

### Vanliga felsökningsfrågor

**F: Min PR misslyckas med översättningskontrollen**  
S: Kontrollera att du endast redigerade engelska markdown-filer i rotmodulkatalogerna, inte översatta versioner.

**F: Hur lägger jag till ett nytt språk?**  
S: Språkstöd hanteras genom co-op-translator-arbetsflödet. Öppna ett ärende för att diskutera att lägga till nya språk.

**F: Kodexempel fungerar inte**  
S: Kontrollera att du följt installationsinstruktionerna i det specifika exemplets README. Kontrollera att du har rätt versioner av beroenden installerade.

**F: Bilder visas inte**  
S: Kontrollera att bildvägar är relativa och använder framåtsnedstreck. Bilder ska finnas i katalogen `images/` eller `translated_images/` för lokaliserade versioner.

### Prestandahänsyn

- Översättningsarbetsflödet kan ta flera minuter att slutföra
- Stora bilder bör optimeras innan de skickas in
- Håll individuella markdown-filer fokuserade och rimligt stora
- Använd relativa länkar för bättre portabilitet

### Projektstyrning

Detta projekt följer Microsofts öppen källkodspraxis:
- MIT-licens för kod och dokumentation
- Microsoft Open Source Code of Conduct
- CLA krävs för bidrag
- Säkerhetsproblem: Följ riktlinjerna i SECURITY.md
- Support: Se SUPPORT.md för hjälpresurser

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.