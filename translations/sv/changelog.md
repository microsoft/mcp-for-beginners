# Ändringslogg: MCP för Nybörjare Kursplan

Detta dokument tjänar som en inspelning av alla betydande ändringar som gjorts i Model Context Protocol (MCP) för Nybörjare kursplan. Ändringar dokumenteras i omvänd kronologisk ordning (nyaste ändringarna först).

## 11 april 2026

### Ny Lektion, Dokumentationsfixar och Uppdateringar av Beroenden

#### Nytt Kursinnehåll Tillagt

**Modul 05 - Avancerade Ämnen**
- **Lektion 5.17: Adversarial Multi-Agent Reasoning med MCP** (`05-AdvancedTopics/mcp-adversarial-agents/README.md`): Ny omfattande guide som täcker det adversariella debattmönstret för multi-agent system
  - Mermaid-arkitekturdiagram: två agenter → delad MCP-server → debattutskrift → domare → utslag
  - Delad MCP verktygsserver (`web_search` + `run_python`) implementerad i Python och TypeScript
  - Motstående systempromptar (FÖR / EMOT / Domare) med uttryckliga verktygsanvändningskrav
  - Debatt-orchestrator i Python, TypeScript och C# som hanterar rundor och dirigerar argument
  - MCP `ClientSession` koppling för orchestratorn till verkliga verktygsanrop
  - Användarfalls-tabell (hallucinationsupptäckt, hotmodellering, API-designgranskning, faktakontroll, teknikval)
  - Säkerhetsöverväganden: sandboxad körning, validering av verktygsanrop, hastighetsbegränsning, auditloggning
  - Strukturerad övning med tre praktiska scenarier (kodgranskning, arkitekturval, innehållsmoderering)

#### Dokumentationsfixar

**Modul 03 - Komma Igång**
- **05-stdio-server/README.md**: Fixade ofullständigt TypeScript stdio-serverexempel — lade till saknad transportinstansiering (`new StdioServerTransport()`) och `server.connect(transport)` anrop för att matcha Python och .NET exemplen i samma avsnitt
- **14-sampling/README.md**: Fixade stavfel — rättade `"Sampling is an davanced features"` → `"Sampling is an advanced feature"`

#### Kursplanuppdateringar

**Huvud README.md**
- Lade till post 5.17 (Adversarial Multi-Agent Reasoning med MCP) i kursplanstabellen med direktlänk till nya lektionen

**05-AdvancedTopics/README.md**
- Lade till Lektion 5.17 rad i lektionstabellen

**study_guide.md**
- Lade till ämnet Adversarial Multi-Agent Reasoning till tankekartan och prosabeskrivningen av Avancerade Ämnen

#### Kod- och Säkerhetsfixar

**Modul 05 - Adversarial Agents (`mcp-adversarial-agents`)**
- **Säkerhetsfix — kommandoinjektion**: Ersatte `execSync` shell-interpolering med `execFile` + `promisify` i TypeScript `run_python`-verktyget, vilket eliminerar kommandoinjektionsytan (LLM-styrd kod skickas nu som ett bokstavligt argv-element utan shells involvering)
- **MCP verktygsloppskoppling**: Uppdaterade Python debatt-orchestratorn till att använda `AsyncAnthropic` klient (ersätter blockerande synkrona `Anthropic`), passera en live `ClientSession` direkt till varje agentvarv, hämta verktygsdefinitioner via `session.list_tools()` varje varv, och skicka `tool_use` block via `session.call_tool()` i en loop tills modellen ger ett slutligt textsvar

#### Uppdateringar av Beroenden

- Uppgraderade `hono` till 4.12.12 i flera paket (03-GettingStarted, 04-PracticalImplementation, 10-StreamliningAIWorkflows)
- Uppgraderade `@hono/node-server` från 1.19.11 till 1.19.13 i TypeScript-paket
- Uppgraderade `cryptography` från 46.0.5 till 46.0.7 i Python-paket (10-StreamliningAIWorkflows labbar 3 och 4)
- Uppgraderade `lodash` från 4.17.23 till 4.18.1 i 10-StreamliningAIWorkflows inspector

#### Översättningar

- Synkroniserade översättningar för 48+ språk med de senaste källändringarna (i18n-uppdatering)

---

## 5 februari 2026

### Repository-omfattande Validering och Navigeringsförbättringar

#### Nytt Kursinnehåll Tillagt

**Modul 03 - Komma Igång**
- **12-mcp-hosts/README.md**: Ny omfattande guide för att sätta upp MCP-hosts
  - Exempel på konfiguration för Claude Desktop, VS Code, Cursor, Cline, Windsurf
  - JSON-konfigurationmallar för alla stora hosts
  - Jämförelsetabell för transporstyper (stdio, SSE/HTTP, WebSocket)
  - Felsökning av vanliga anslutningsproblem
  - Säkerhetsbästa praxis för hostkonfiguration

- **13-mcp-inspector/README.md**: Ny felsökningsguide för MCP Inspector
  - Installationsmetoder (npx, npm globalt, från källkod)
  - Anslutning till servrar via stdio och HTTP/SSE
  - Testningsverktyg, resurser och promptarbetsflöden
  - VS Code integration med MCP Inspector
  - Vanliga felsökningsscenarier med lösningar

**Modul 04 - Praktisk Implementation**
- **pagination/README.md**: Ny guide för implementering av paginering
  - Paginering med cursor-baserade mönster i Python, TypeScript, Java
  - Hantering av paginering på klientsidan
  - Strategier för cursor-design (opakt vs strukturerat)
  - Rekommendationer för prestationsoptimering

**Modul 05 - Avancerade Ämnen**
- **mcp-protocol-features/README.md**: Djupdykning i nya protokollfunktioner
  - Implementering av progress-notifikationer
  - Mönster för avbokning av förfrågningar
  - Resursmallar med URI-mönster
  - Hantering av serverns livscykel
  - Kontroll av loggnivåer
  - Felhanteringsmönster med JSON-RPC-koder

#### Navigeringsfixar (24+ filer uppdaterade)

**Huvudmodulens README-filer**
 Nu länkar till både första lektionen OCH nästa modul

**02-Säkerhet Underdokument**
- Alla 5 kompletterande säkerhetsdokument har nu "Vad är nästa" navigering:

**09-CaseStudy-filer**
- Alla case study-filer har nu sekventiell navigering:

**10-StreamliningAI Labs**
Lade till "Vad är nästa"-sektion i Modul 10 översikt och Modul 11

#### Kod- och Innehållsfixar

**SDK och Beroendeuppdateringar**
Fixade tomma openai-version till `^4.95.0`
Uppdaterade SDK från `^1.8.0` till `>=1.26.0`
Uppdaterade MCP versionspinnar till `>=1.26.0`

**Kodfixar**
Fixade ogiltig modell `gpt-4o-mini` till `gpt-4.1-mini`

**Innehållsfixar**
Fixade bruten länk `READMEmd` → `README.md`, fixade kursplanrubrik `Module 1-3` → `Module 0-3`, fixade skiftlägeskänslig sökväg
Borttagen korrupt duplicerad innehåll för Case Study 5

**Förbättringar för Nybörjare**
Lade till ordentlig introduktion, lärandemål och förkunskaper för nybörjare

#### Kursplanuppdateringar

**Huvud README.md**
- Lade till poster 3.12 (MCP Hosts), 3.13 (MCP Inspector), 4.1 (Paginering), 5.16 (Protokollfunktioner) till kursplanstabellen

**Modulens README-filer**
 Lade till lektioner 12 och 13 till lektionslistan
 Lade till Praktiska Guider sektion med pagineringlänk
 Lade till lektioner 5.15 (Anpassad Transport) och 5.16 (Protokollfunktioner)

**study_guide.md**
- Uppdaterade tankekartan med alla nya ämnen: MCP Hosts Setup, MCP Inspector, Pagineringstrategier, Protokollfunktioners djupdykning

## 28 januari 2026

### MCP Specifikation 2025-11-25 Överensstämmelsegranskning

#### Kärnkonceptförbättring (01-CoreConcepts/)
- **Ny Klientprimitiv - Roots**: Lade till omfattande dokumentation om Roots klientprimitiv, som möjliggör för servrar att förstå filsystemgränser och åtkomsträttigheter
- **Verktygsannoteringar**: Lade till dokumentation om verktygsbeteendeannoteringar (`readOnlyHint`, `destructiveHint`) för bättre beslut vid verktygskörning
- **Verktygsanrop i Sampling**: Uppdaterade Sampling-dokumentationen för att inkludera `tools` och `toolChoice` parametrar för modellstyrd verktygsväljning under sampling
- **URL-läge Framkallning**: Lade till dokumentation för URL-baserad framkallning för serverinitierade externa webbinteraktioner
- **Uppgifter (Experimentellt)**: Tillagt nytt avsnitt som dokumenterar den experimentella Uppgifts-funktionen för uthålliga exekveringswraprar och uppskjuten resultathämtning
- **Icon-stöd**: Noterat att verktyg, resurser, resursmallar och promptar nu kan inkludera ikoner som ytterligare metadata

#### Dokumentationsuppdateringar
- **README.md**: Lade till MCP Specifikation 2025-11-25 versionsreferens och datum-baserad versioneringförklaring
- **study_guide.md**: Uppdaterade kursplanens karta för att inkludera Uppgifter och Verktygsannoteringar i Kärnkonceptavsnittet; uppdaterade dokumentets tidsstämpel

#### Specifikationsöverensstämmelse Verifiering
- **Protokollversion**: Verifierade att all dokumentation refererar aktuella MCP Specifikation 2025-11-25
- **Arkitekturaligning**: Bekräftade tvålagsarkitektur (Dataskikt + Transportskikt) dokumentationsnoggrannhet
- **Primitiver Dokumentation**: Validerade serverprimitiver (Resurser, Prompter, Verktyg) och klientprimitiver (Sampling, Framkallning, Loggning, Roots)
- **Transportmekanismer**: Verifierade STDIO- och Streamable HTTP-transportsdokumentationsnoggrannhet
- **Säkerhetsvägledning**: Bekräftade överensstämmelse med aktuell MCP Säkerhetsbästa praxis dokumentation

#### Viktiga MCP 2025-11-25 Funktioner Dokumenterade
- **OpenID Connect Discovery**: Auth-serverupptäckt via OIDC
- **OAuth Klient-ID Metadata Dokument**: Rekommenderad klientregistreringsmekanism
- **JSON Schema 2020-12**: Standarddialekt för MCP skadesigneringar
- **SDK Tiering System**: Formaliserade krav för SDK-funktionsstöd och underhåll
- **Styrningsstruktur**: Formaliserade arbetsgrupper och intressegrupper i MCP styrning

### Säkerhetsdokumentation Större Uppdatering (02-Security/)

#### MCP Security Summit Workshop (Sherpa) Integration
- **Ny Praktisk Träningsresurs**: Lagt till omfattande integration med [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/) i all säkerhetsdokumentation
- **Expeditionsrutt-täckning**: Dokumenterade hela camp-till-camp framstegen från Basläger till Summit
- **OWASP Anpassning**: All säkerhetsvägledning mappas nu till OWASP MCP Azure Security Guide risker

#### OWASP MCP Topp 10 Integration
- **Nytt Avsnitt**: Lagt till OWASP MCP Topp 10 säkerhetsrisker tabell med Azure-mitigeringar i huvudsäkerhets-README
- **Riskbaserad Dokumentation**: Uppdaterade mcp-security-controls-2025.md med OWASP MCP riskreferenser för varje säkerhetsdomän
- **Referensarkitektur**: Länkade till OWASP MCP Azure Security Guide referensarkitektur och implementationsmönster

#### Uppdaterade Säkerhetsfiler
- **README.md**: Lagt till Sherpa Workshop översikt, expeditionsrutttabell, OWASP MCP Topp 10 risker sammanfattning och praktisk träningssektion
- **mcp-security-controls-2025.md**: Uppdaterat rubrik till februari 2026, lagt till OWASP riskreferenser (MCP01-MCP08), fixade specifikationsversionsinkonsekvens
- **mcp-security-best-practices-2025.md**: Lagt till Sherpa och OWASP resurser sektion, uppdaterad tidsstämpel
- **mcp-best-practices.md**: Lagt till praktisk träningssektion med Sherpa och OWASP länkar
- **azure-content-safety-implementation.md**: Lagt till OWASP MCP06 referens, Sherpa Camp 3 anpassning och ytterligare resurser sektion

#### Nya Ressurslänkar Tillagda
- [MCP Security Summit Workshop (Sherpa)](https://azure-samples.github.io/sherpa/)
- [OWASP MCP Azure Security Guide](https://microsoft.github.io/mcp-azure-security-guide/)
- [OWASP MCP Topp 10](https://owasp.org/www-project-mcp-top-10/)
- Individuella OWASP MCP risk-sidor (MCP01-MCP10)

### Kursplan-Omfattande MCP Specifikation 2025-11-25 Anpassning

#### Modul 03 - Komma Igång
- **SDK Dokumentation**: Lade till Go SDK till den officiella SDK-listan; uppdaterade alla SDK-referenser för att överensstämma med MCP Specifikation 2025-11-25
- **Transportförtydligande**: Uppdaterade STDIO och HTTP Streaming transportbeskrivningar med uttryckliga specreferenser

#### Modul 04 - Praktisk Implementation
- **SDK Uppdateringar**: Lade till Go SDK; uppdaterade SDK-listan med specifikationsversionsreferens
- **Authorization Spec**: Uppdaterade MCP Authorization specifikationslänk till nuvarande 2025-11-25 version

#### Modul 05 - Avancerade Ämnen
- **Nya Funktioner**: Lade till notering om nya MCP Specifikation 2025-11-25 funktioner (Uppgifter, Verktygsannoteringar, URL Mode Framkallning, Roots)
- **Säkerhetsresurser**: Lade till OWASP MCP Topp 10 och Sherpa workshop länkar till ytterligare referenser

#### Modul 06 - Community Bidrag
- **SDK Lista**: Lade till Swift och Rust SDKs; uppdaterade specifikationslänk till 2025-11-25
- **Specifikationsreferens**: Uppdaterade MCP Specifikationslänk till direkt specifikations-URL

#### Modul 07 - Lektioner från Tidig Adaption
- **Resursuppdateringar**: Lade till MCP Specifikation 2025-11-25 länk och OWASP MCP Topp 10 till ytterligare resurser

#### Modul 08 - Bästa Praxis
- **Specversionsuppdatering**: Uppdaterade MCP Specifikationsreferens till 2025-11-25
- **Säkerhetsresurser**: Lade till OWASP MCP Topp 10 och Sherpa workshop till ytterligare referenser

#### Modul 10 - Effektivisering av AI Arbetsflöden
- **Badge Uppdatering**: Bytte MCP versionsmärke från SDK-version (1.9.3) till specifikationsversion (2025-11-25)
- **Resurslänkar**: Uppdaterade MCP Specifikationslänk; lade till OWASP MCP Topp 10

#### Modul 11 - MCP Server Hands-On Labs
- **Specifikationsreferens**: Uppdaterade MCP Specifikationslänk till 2025-11-25 version
- **Säkerhetsresurser**: Lade till OWASP MCP Topp 10 till officiella resurser

## 18 december 2025
### Säkerhetsdokumentationsuppdatering - MCP-specifikation 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Specifikationsversionsuppdatering
- **Protokollversionsuppdatering**: Uppdaterad för att referera till senaste MCP-specifikationen 2025-11-25 (släppt den 25 november 2025)
  - Uppdaterade alla versionsreferenser från 2025-06-18 till 2025-11-25
  - Uppdaterade dokumentdatumreferenser från 18 augusti 2025 till 18 december 2025
  - Verifierade att alla specifikations-URL:er pekar på aktuell dokumentation
- **Innehållsvalidering**: Omfattande validering av säkerhetsbästa praxis mot senaste standarder
  - **Microsoft Security Solutions**: Verifierade aktuell terminologi och länkar för Prompt Shields (tidigare "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID och Azure Key Vault
  - **OAuth 2.1 Security**: Bekräftade överensstämmelse med senaste OAuth-säkerhetsbästa praxis
  - **OWASP Standards**: Validerade att OWASP Top 10 för LLM-referenser är aktuella
  - **Azure Services**: Verifierade alla Microsoft Azure-dokumentationslänkar och bästa praxis
- **Standardanpassning**: Alla refererade säkerhetsstandarder bekräftade som aktuella
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure säkerhets- och efterlevnadsramverk
- **Implementeringsresurser**: Verifierade alla länkar till implementeringsguider och resurser
  - Azure API Management auktoriseringsmönster
  - Microsoft Entra ID integrationsguider
  - Azure Key Vault hantering av hemligheter
  - DevSecOps pipelines och övervakningslösningar

### Dokumentationskvalitetssäkring
- **Specifikationsöverensstämmelse**: Säkerställt att alla obligatoriska MCP-säkerhetskrav (MUST/MUST NOT) överensstämmer med senaste specifikationen
- **Resursaktualitet**: Verifierat att alla externa länkar till Microsoft-dokumentation, säkerhetsstandarder och implementeringsguider är aktuella
- **Täcket av bästa praxis**: Bekräftat omfattande täckning av autentisering, auktorisering, AI-specifika hot, leveranskedjesäkerhet och företagsmönster

## 6 oktober 2025

### Utökning av avsnittet Komma igång – Avancerad serveranvändning & Enkel autentisering

#### Avancerad serveranvändning (03-GettingStarted/10-advanced)
- **Nytt kapitel tillagt**: Införde en omfattande guide till avancerad MCP-serveranvändning som täcker både vanlig och låg nivå-serverarkitektur.
  - **Vanlig vs. låg nivå-server**: Detaljerad jämförelse och kodexempel i Python och TypeScript för båda metoderna.
  - **Hantera-baserad design**: Förklaring av hantering av verktyg/resurser/promptar baserat på handlers för skalbara, flexibla serverimplementationer.
  - **Praktiska mönster**: Verkliga scenarier där låg nivå-servermönster är fördelaktiga för avancerade funktioner och arkitektur.

#### Enkel autentisering (03-GettingStarted/11-simple-auth)
- **Nytt kapitel tillagt**: Steg-för-steg-guide för att implementera enkel autentisering i MCP-servrar.
  - **Autentiseringskoncept**: Klar förklaring av autentisering vs. auktorisering och hantering av referenser.
  - **Grundläggande Auth-implementering**: Middleware-baserade autentiseringsmönster i Python (Starlette) och TypeScript (Express) med kodexempel.
  - **Utveckling mot avancerad säkerhet**: Vägledning för att börja med enkel autentisering och gå vidare till OAuth 2.1 och RBAC, med referenser till avancerade säkerhetsmoduler.

Dessa tillägg ger praktisk, handgriplig vägledning för att bygga mer robusta, säkra och flexibla MCP-serverimplementationer som kopplar samman grundläggande koncept med avancerade produktionsmönster.

## 29 september 2025

### MCP-serverdatabasintegrationslabbar - Omfattande praktisk lärandebana

#### 11-MCPServerHandsOnLabs - Ny komplett kurs i databasintegration
- **Fullständig 13-labbs lärandebana**: Lade till en omfattande praktisk kurs för att bygga produktionsklara MCP-servrar med PostgreSQL-databasintegration
  - **Verklig implementering**: Zava Retail-analysfall som demonstrerar företagsklassmönster
  - **Strukturerad inlärningsprogression**:
    - **Labbar 00-03: Grunderna** – Introduktion, kärnarkitektur, säkerhet & flerkundsstöd, miljöuppsättning
    - **Labbar 04-06: Bygga MCP-servern** – Databasutformning & schema, MCP-serverimplementering, verktygsutveckling
    - **Labbar 07-09: Avancerade funktioner** – Semantisk sökintegration, testning & felsökning, VS Code-integration
    - **Labbar 10-12: Produktion & bästa praxis** – Distribueringsstrategier, övervakning & observabilitet, bästa praxis & optimering
  - **Företagsteknologier**: FastMCP-ramverk, PostgreSQL med pgvector, Azure OpenAI-embeddingar, Azure Container Apps, Application Insights
  - **Avancerade funktioner**: Radnivåsäkerhet (RLS), semantisk sökning, flerkundstillgång, vektorembeddingar, realtidsövervakning

#### Terminologistandardisering - Modul till labb-omvandling
- **Omfattande dokumentationsuppdatering**: Systematiskt ändrat alla README-filer i 11-MCPServerHandsOnLabs att använda "Labb" istället för "Modul"
  - **Avsnittsrubriker**: Uppdaterade "What This Module Covers" till "What This Lab Covers" i alla 13 labbar
  - **Innehållsbeskrivning**: Ändrade "This module provides..." till "This lab provides..." i hela dokumentationen
  - **Lärandemål**: Uppdaterade "By the end of this module..." till "By the end of this lab..."
  - **Navigationslänkar**: Omvandlade alla referenser "Module XX:" till "Lab XX:" i korsreferenser och navigation
  - **Avslutningsspårning**: Uppdaterade "After completing this module..." till "After completing this lab..."
  - **Bevarade tekniska referenser**: Behöll Python-modulreferenser i konfigurationsfiler (t.ex. `"module": "mcp_server.main"`)

#### Förbättring av studieguiden (study_guide.md)
- **Visuell kurskarta**: Tillagt nytt avsnitt "11. Database Integration Labs" med omfattande visualisering av labbstruktur
- **Repositoriestruktur**: Uppdaterat från tio till elva huvudsektioner med detaljerad beskrivning av 11-MCPServerHandsOnLabs
- **Lärandevägsriktlinjer**: Förbättrad navigationsinstruktion för att täcka sektioner 00-11
- **Teknologitäckning**: Lade till detaljer om FastMCP, PostgreSQL och Azure-tjänsters integration
- **Läranderesultat**: Betoning på produktionsfärdig serverutveckling, databasintegrationsmönster och företagsäkerhet

#### Förbättring av huvud-README-strukturen
- **Labb-baserad terminologi**: Uppdaterade huvud-README.md i 11-MCPServerHandsOnLabs för att konsekvent använda "Labb"-struktur
- **Organisation av lärandebana**: Tydlig progression från grundläggande koncept genom avancerad implementering till produktionsdistribution
- **Verklighetsfokus**: Betoning på praktiskt, handgripligt lärande med företagsmönster och teknologier

### Förbättringar av dokumentationskvalitet och konsekvens
- **Betoning på praktiskt lärande**: Förstärkt fokus på praktisk labb-baserad metod genom hela dokumentationen
- **Företagsmönsterfokus**: Framhävda produktionsklara implementationer och företagsäkerhetsaspekter
- **Teknologiintegration**: Omfattande täckning av moderna Azure-tjänster och AI-integrationsmönster
- **Lärandets progressionsstruktur**: Klar, strukturerad väg från grundläggande koncept till produktionsdistribution

## 26 september 2025

### Förbättring av fallstudier - GitHub MCP Registry-integrering

#### Fallstudier (09-CaseStudy/) - Fokus på ekosystemutveckling
- **README.md**: Större utökning med omfattande fallstudie av GitHub MCP Registry
  - **GitHub MCP Registry-fallstudie**: Ny omfattande fallstudie som undersöker GitHubs MCP Registry-lansering i september 2025
    - **Problemanalys**: Detaljerad granskning av fragmenterade MCP-serverupptäckts- och distributionsutmaningar
    - **Lösningsarkitektur**: GitHubs centraliserade registry-metod med en-klicks VS Code-installation
    - **Affärspåverkan**: Mätbara förbättringar i utvecklaronboarding och produktivitet
    - **Strategiskt värde**: Fokus på modulär agentdistribution och interoperabilitet över verktyg
    - **Ekosystemutveckling**: Positionering som grundläggande plattform för agentisk integration
  - **Förbättrad fallstudiestruktur**: Uppdaterade alla sju fallstudier med enhetlig formatering och omfattande beskrivningar
    - Azure AI Travel Agents: Fokus på multi-agent orkestrering
    - Azure DevOps Integration: Fokus på arbetsflödesautomatisering
    - Realtidsdokumenthämtning: Python-konsolklientimplementering
    - Interaktiv studieplansgenerator: Chainlit-konversationswebbapp
    - In-Editor Documentation: VS Code och GitHub Copilot-integration
    - Azure API Management: Företags-API-integrationsmönster
    - GitHub MCP Registry: Ekosystemutveckling och communityplattform
  - **Omfattande slutsats**: Omskrivet slutsavsnitt som lyfter fram sju fallstudier som täcker flera MCP-implementeringselement
    - Företagsintegration, multi-agent orkestrering, utvecklarproduktivitet
    - Ekosystemutveckling, utbildningsapplikationskategorisering
    - Fördjupade insikter om arkitekturmönster, implementeringsstrategier och bästa praxis
    - Betoning på MCP som mogen, produktionsfärdig protokoll

#### Uppdateringar i studieguiden (study_guide.md)
- **Visuell kurskarta**: Uppdaterad mindmap för att inkludera GitHub MCP Registry i sektionen Fallstudier
- **Beskrivning av fallstudier**: Förbättrad från generiska beskrivningar till detaljerad genomgång av sju omfattande fallstudier
- **Repositoriestruktur**: Uppdaterad sektion 10 för att spegla omfattande fallstudiedäckning med specifika implementationsdetaljer
- **Changelog-integration**: Tillagd post den 26 september 2025 som dokumenterar tillägget av GitHub MCP Registry och fallstudieförbättringar
- **Datumuppdateringar**: Uppdaterad sidfotsstämpel till senaste revision (26 september 2025)

### Förbättringar av dokumentationskvalitet
- **Konsekvensförbättring**: Standardiserad fallstudieformatering och struktur över alla sju exempel
- **Omfattande täckning**: Fallstudier som nu spänner över företags-, utvecklarproduktivitet- och ekosystemutvecklingsscenarier
- **Strategisk positionering**: Förstärkt fokus på MCP som grundläggande plattform för agentbaserad systemdistribution
- **Resursintegration**: Uppdaterade ytterligare resurser med länk till GitHub MCP Registry

## 15 september 2025

### Utökning av avancerade ämnen - Anpassade transporter & kontextteknik

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Ny avancerad implementeringsguide
- **README.md**: Komplett implementeringsguide för anpassade MCP-transportsätt
  - **Azure Event Grid Transport**: Omfattande serverlös händelsedriven transportimplementering
    - C#, TypeScript och Python-exempel med Azure Functions-integration
    - Händelsedrivna arkitekturmodeller för skalbara MCP-lösningar
    - Webhook-mottagare och push-baserad meddelandehantering
  - **Azure Event Hubs Transport**: Transportimplementering med hög genomströmning för strömmande data
    - Realtidsströmning för låg latens
    - Partitioneringsstrategier och checkpoint-hantering
    - Meddelandebatchning och prestandaoptimering
  - **Företagsintegrationsmönster**: Produktionsklara arkitekturexempel
    - Distribuerad MCP-bearbetning över flera Azure Functions
    - Hybridtransportarkitektur som kombinerar flera transporttyper
    - Meddelandetålighet, tillförlitlighet och felhanteringsstrategier
  - **Säkerhet & Övervakning**: Azure Key Vault-integration och observabilitetsmönster
    - Managed identity-autentisering och principen om minsta privilegium
    - Application Insights-telemetri och prestandaövervakning
    - Strömbrytare och felavhjälpningsmönster
  - **Testningsramverk**: Omfattande testningsstrategier för anpassade transporter
    - Enhetstestning med testdubbningar och mocking-ramverk
    - Integrationstestning med Azure Test Containers
    - Överväganden för prestanda- och belastningstester

#### Kontextteknik (05-AdvancedTopics/mcp-contextengineering/) - Framväxande AI-disciplin
- **README.md**: Omfattande utforskning av kontextteknik som ett framväxande område
  - **Kärnprinciper**: Komplett kontextdelning, handlingsbeslutsmedvetenhet och hantering av kontextfönster
  - **Anpassning till MCP-protokoll**: Hur MCP-design adresserar kontextteknikutmaningar
    - Begränsningar i kontextfönster och progressiv laddning
    - Relevansbedömning och dynamisk kontextåtkomst
    - Multimodal kontexthantering och säkerhetsaspekter
  - **Implementeringsmetoder**: Entrådad kontra multi-agentarkitektur
    - Kontextindelning och prioriteringstekniker
    - Progressiv kontextladdning och komprimeringsstrategier
    - Flerskiktskontextmetoder och optimering av åtkomst
  - **Mätningsramverk**: Pågående metrik för utvärdering av konstexteffektivitet
    - Inmatningseffektivitet, prestanda, kvalitet och användarupplevelse
    - Experimentella metoder för optimering av kontext
    - Analys av fel och förbättringsmetoder

#### Uppdatering av kursnavigering (README.md)
- **Förbättrad modulstruktur**: Uppdaterad kursöversiktstabell för att inkludera nya avancerade ämnen
  - Tillagd Context Engineering (5.14) och Custom Transport (5.15)
  - Konsekvent formatering och navigationslänkar i samtliga moduler
  - Uppdaterade beskrivningar för att återspegla nuvarande innehållsomfång

### Förbättringar av katalogstruktur
- **Namnstandardisering**: Omdöpt "mcp transport" till "mcp-transport" för enhetlighet med andra avancerade ämnesmappar
- **Innehållsorganisation**: Alla 05-AdvancedTopics-mappar följer nu konsekvent namngivningsmönster (mcp-[ämne])

### Förbättringar av dokumentationskvalitet
- **Anpassning till MCP-specifikation**: All ny innehåll refererar till aktuella MCP-specifikationen 2025-06-18
- **Exempel i flera språk**: Omfattande kodexempel i C#, TypeScript och Python
- **Företagsfokus**: Produktionsklara mönster och Azure-molnintegration genomgående
- **Visuell dokumentation**: Mermaid-diagram för arkitektur- och flödesvisualisering

## 18 augusti 2025

### Omfattande dokumentationsuppdatering - MCP 2025-06-18-standarder

#### MCP Security Best Practices (02-Security/) - Komplett modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Fullständig omskrivning i linje med MCP Specification 2025-06-18  
  - **Obligatoriska krav**: Tillagda explicita MÅSTE/MÅSTE INTE-krav från officiell specifikation med tydliga visuella indikatorer  
  - **12 kärnsäkerhetspraxis**: Omstrukturerade från 15-punktslista till omfattande säkerhetsdomäner  
    - Token-säkerhet & autentisering med integration av extern identitetsleverantör  
    - Sessionshantering & transportssäkerhet med kryptografiska krav  
    - AI-specifikt hotsskydd med Microsoft Prompt Shields-integration  
    - Åtkomstkontroll & behörigheter med principen om minsta privilegium  
    - Innehållssäkerhet & övervakning med Azure Content Safety-integration  
    - Leverantörskedjesäkerhet med omfattande komponentverifiering  
    - OAuth-säkerhet & Confused Deputy-förebyggande med PKCE-implementering  
    - Incidenthantering & återställning med automatiserade möjligheter  
    - Efterlevnad & styrning med regulatorisk anpassning  
    - Avancerade säkerhetskontroller med zero trust-arkitektur  
    - Microsofts säkerhetsekosystemintegration med omfattande lösningar  
    - Kontinuerlig säkerhetsevolution med adaptiva metoder  
  - **Microsoft säkerhetslösningar**: Förbättrad integrationsvägledning för Prompt Shields, Azure Content Safety, Entra ID och GitHub Advanced Security  
  - **Implementeringsresurser**: Kategoriserade omfattande resurslänkar efter Officiell MCP-dokumentation, Microsofts säkerhetslösningar, säkerhetsstandarder och implementeringsguider  

#### Avancerade säkerhetskontroller (02-Security/) - Företagsimplementering  
- **MCP-SECURITY-CONTROLS-2025.md**: Fullständig översyn med företagsnivå säkerhetsramverk  
  - **9 omfattande säkerhetsdomäner**: Utökade från grundläggande kontroller till detaljerat företagsramverk  
    - Avancerad autentisering & auktorisering med Microsoft Entra ID-integration  
    - Tokensäkerhet & anti-passthrough-kontroller med omfattande validering  
    - Sessionssäkerhetskontroller med hijacking-förebyggande  
    - AI-specifika säkerhetskontroller med förebyggande av prompt-injektion och verktygsförgiftning  
    - Förebyggande av Confused Deputy-attacker med OAuth proxy-säkerhet  
    - Verktygsexekveringssäkerhet med sandboxing och isolering  
    - Leverantörskedjesäkerhetskontroller med beroendeverifiering  
    - Övervakning & detektionskontroller med SIEM-integration  
    - Incidenthantering & återställning med automatiserade möjligheter  
  - **Implementeringsexempel**: Tillagda detaljerade YAML-konfigurationsblock och kodexempel  
  - **Microsoft lösningsintegration**: Omfattande täckning av Azure säkerhetstjänster, GitHub Advanced Security och företagsidentitetshantering  

#### Avancerade säkerhetsämnen (05-AdvancedTopics/mcp-security/) - Produktionsfärdig implementering  
- **README.md**: Fullständig omskrivning för företags säkerhetsimplementering  
  - **Aktuell specifikationsanpassning**: Uppdaterad till MCP Specification 2025-06-18 med obligatoriska säkerhetskrav  
  - **Förbättrad autentisering**: Microsoft Entra ID-integration med omfattande .NET- och Java Spring Security-exempel  
  - **AI-säkerhetsintegration**: Microsoft Prompt Shields och Azure Content Safety-implementering med detaljerade Python-exempel  
  - **Avancerad hotavhjälpning**: Omfattande implementeringsexempel för  
    - Förebyggande av Confused Deputy-attacker med PKCE och användarsamtyckesvalidering  
    - Förebyggande av token passthrough med publikumsvalidering och säker tokenhantering  
    - Förebyggande av session hijacking med kryptografisk bindning och beteendeanalys  
  - **Företagssäkerhetsintegration**: Azure Application Insights-övervakning, hotdetektionspipeline och leverantörskedjesäkerhet  
  - **Implementeringschecklista**: Tydliga obligatoriska kontra rekommenderade säkerhetskontroller med Microsoft säkerhetsekosystemfördelar  

### Dokumentationskvalitet & standardanpassning  
- **Specifikationsreferenser**: Uppdaterade alla referenser till aktuell MCP Specification 2025-06-18  
- **Microsoft säkerhetsekosystem**: Förbättrad integrationsvägledning genom all säkerhetsdokumentation  
- **Praktisk implementering**: Tillagda detaljerade kodexempel i .NET, Java och Python med företagsmönster  
- **Resursorganisation**: Omfattande kategorisering av officiell dokumentation, säkerhetsstandarder och implementeringsguider  
- **Visuella indikatorer**: Tydlig markering av obligatoriska krav kontra rekommenderade praxis  

#### Kärnbegrepp (01-CoreConcepts/) - Fullständig modernisering  
- **Protokollversionsuppdatering**: Uppdaterad för att referera till aktuell MCP Specification 2025-06-18 med datum-baserad versionering (ÅÅÅÅ-MM-DD-format)  
- **Arkitekturförfining**: Förbättrade beskrivningar av Hosts, Clients och Servers för att spegla aktuell MCP-arkitektur  
  - Hosts definierade tydligt som AI-applikationer som koordinerar flera MCP-klientanslutningar  
  - Clients beskrivna som protokollkopplingar som bibehåller en-till-en-serverrelationer  
  - Servers förbättrade med lokala kontra fjärrdriftscenarier  
- **Primitiv omstrukturering**: Fullständig översyn av server- och klientprimitiver  
  - Serverprimitiver: Resurser (datakällor), Prompter (mallar), Verktyg (exekverbara funktioner) med detaljerade förklaringar och exempel  
  - Klientprimitiver: Sampling (LLM-slutföranden), Elicitation (användarinmatning), Loggning (debugging/övervakning)  
  - Uppdaterade med aktuella upptäckts- (`*/list`), hämt- (`*/get`) och exekverings- (`*/call`) metodmönster  
- **Protokollarkitektur**: Introducerade tvåskiktsarkitektur  
  - Datalager: JSON-RPC 2.0-grund med livscykelhantering och primitiva funktioner  
  - Transportlager: STDIO (lokal) och Streamable HTTP med SSE (fjärr) transportmekanismer  
- **Säkerhetsramverk**: Omfattande säkerhetsprinciper inklusive explicit användarsamtycke, dataskydd, verktygsexekverings-säkerhet och transportsäkerhet  
- **Kommunikationsmönster**: Uppdaterade protokollmeddelanden som visar initiering, upptäckt, exekvering och notifieringsflöden  
- **Kodexempel**: Uppdaterade flerspråkiga exempel (.NET, Java, Python, JavaScript) för att spegla aktuella MCP SDK-mönster  

#### Säkerhet (02-Security/) - Omfattande säkerhetssynkronisering  
- **Standardanpassning**: Fullständig anpassning till MCP Specification 2025-06-18 säkerhetskrav  
- **Autentiseringsevolution**: Dokumenterad utveckling från egna OAuth-servrar till delegering till externa identitetsleverantörer (Microsoft Entra ID)  
- **AI-specifik hotanalys**: Förbättrad täckning av moderna AI-attackvektorer  
  - Detaljerade scenarier för prompt-injektionsattacker med verkliga exempel  
  - Verktygsförgiftning och "rug pull"-attackmönster  
  - Context window-förgiftning och modellförvirringsattacker  
- **Microsoft AI-säkerhetslösningar**: Omfattande täckning av Microsofts säkerhetsekosystem  
  - AI Prompt Shields med avancerad detektion, spotlighting och delimitertekniker  
  - Azure Content Safety integrationsmönster  
  - GitHub Advanced Security för skydd av leverantörskedjan  
- **Avancerad hotavhjälpning**: Detaljerade säkerhetskontroller för  
  - Session hijacking med MCP-specifika attackscenarier och kryptografiska sessions-ID-krav  
  - Confused deputy-problem i MCP proxy-scenarier med explicita samtyckeskrav  
  - Tokens passthrough-sårbarheter med obligatoriska valideringskontroller  
- **Leverantörskedjesäkerhet**: Utökat AI-leverantörskedjetäckning inklusive foundational models, embeddings-tjänster, context providers och tredjeparts-API:er  
- **Foundationssäkerhet**: Förbättrad integration med företags säkerhetsmönster inklusive zero trust-arkitektur och Microsoft säkerhetsekosystem  
- **Resursorganisation**: Kategoriserade omfattande resurslänkar efter typ (Officiella dokument, standarder, forskning, Microsoft-lösningar, implementeringsguider)  

### Förbättringar av dokumentationskvalitet  
- **Strukturerade lärandemål**: Förbättrade lärandemål med specifika, handlingsbara resultat  
- **Korsreferenser**: Tillagda länkar mellan relaterade säkerhets- och kärnbegreppsområden  
- **Aktuell information**: Uppdaterade alla datumsreferenser och specifikationslänkar till aktuella standarder  
- **Implementeringsvägledning**: Tillagda specifika, handlingsbara implementeringsanvisningar i båda sektionerna  

## 16 juli 2025  

### README och navigeringsförbättringar  
- Fullständigt omdesignad kursnavigering i README.md  
- Ersatte `<details>`-taggar med mer tillgängligt tabellformat  
- Skapade alternativa layoutalternativ i ny "alternative_layouts"-mapp  
- Tillagda navigeringsexempel med kortbaserat, flikformat och dragspelsformat  
- Uppdaterad avsnitt för repo-struktur med alla senaste filer  
- Förbättrat avsnitt "Hur man använder detta läroprogram" med tydliga rekommendationer  
- Uppdaterade MCP-specifikationslänkar till korrekta URL:er  
- Tillagda avsnitt om Context Engineering (5.14) i kursstrukturen  

### Uppdateringar av studiehandledning  
- Fullständigt reviderad studiehandledning för att överensstämma med aktuell repostruktur  
- Tillagda nya sektioner för MCP-klienter och verktyg samt populära MCP-servrar  
- Uppdaterad Visual Curriculum Map för att korrekt visa alla ämnen  
- Förbättrade beskrivningar av avancerade ämnen för att täcka alla specialområden  
- Uppdaterat Case Studies-avsnitt med verkliga exempel  
- Tillagd denna omfattande ändringslogg  

### Communitybidrag (06-CommunityContributions/)  
- Tillagd detaljerad information om MCP-servrar för bildgenerering  
- Tillagd omfattande sektion om användning av Claude i VSCode  
- Tillagd Cline terminalklient installations- och användningsinstruktioner  
- Uppdaterat MCP-klientavsnitt med alla populära klientalternativ  
- Förbättrade bidragsexempel med mer korrekta kodexempel  

### Avancerade ämnen (05-AdvancedTopics/)  
- Organiserade alla specialiserade ämnesmappar med konsekvent namngivning  
- Tillagda material och exempel för context engineering  
- Tillagd dokumentation för Foundry agent-integration  
- Förbättrad dokumentation för Entra ID-säkerhetsintegration  

## 11 juni 2025  

### Initial skapelse  
- Släppt första versionen av MCP för nybörjare-läroprogrammet  
- Skapade grundstruktur för alla 10 huvudsektioner  
- Implementerade Visual Curriculum Map för navigering  
- Tillagda initiala exempelprojekt i flera programmeringsspråk  

### Kom igång (03-GettingStarted/)  
- Skapade första serverimplementeringsexempel  
- Tillagd vägledning för klientutveckling  
- Inkluderade instruktioner för LLM-klientintegration  
- Tillagd dokumentation för VS Code-integration  
- Implementerade Server-Sent Events (SSE) serverexempel  

### Kärnbegrepp (01-CoreConcepts/)  
- Tillagd detaljerad förklaring av klient-server-arkitektur  
- Skapade dokumentation om nyckelkomponenter i protokollet  
- Dokumenterade meddelandemönster i MCP  

## 23 maj 2025  

### Repositorie-struktur  
- Initierade repository med grundläggande mappstruktur  
- Skapade README-filer för varje större sektion  
- Satte upp översättningsinfrastruktur  
- Tillagda bildresurser och diagram  

### Dokumentation  
- Skapade initial README.md med översikt av kursmaterial  
- Tillagda CODE_OF_CONDUCT.md och SECURITY.md  
- Satte upp SUPPORT.md med vägledning för hjälp  
- Skapade preliminär struktur för studiehandledning  

## 15 april 2025  

### Planering och ramverk  
- Initial planering för MCP för nybörjare-kursen  
- Definierade lärandemål och målgrupp  
- Skissade 10-sektions struktur för kursen  
- Utvecklade konceptuellt ramverk för exempel och fallstudier  
- Skapade initiala prototyp-exempel för centrala begrepp

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->