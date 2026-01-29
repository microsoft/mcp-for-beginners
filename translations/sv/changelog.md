# Ändringslogg: MCP för nybörjare läroplan

Detta dokument fungerar som en redogörelse för alla betydande ändringar som gjorts i Model Context Protocol (MCP) för nybörjare läroplanen. Ändringar dokumenteras i omvänd kronologisk ordning (nyaste ändringar först).

## 18 december 2025

### Uppdatering av säkerhetsdokumentation - MCP-specifikation 2025-11-25

#### MCP Security Best Practices (02-Security/mcp-best-practices.md) - Uppdatering av specifikationsversion
- **Protokollversionsuppdatering**: Uppdaterad för att referera till senaste MCP-specifikation 2025-11-25 (släppt 25 november 2025)
  - Uppdaterade alla versionsreferenser från 2025-06-18 till 2025-11-25
  - Uppdaterade dokumentdatumreferenser från 18 augusti 2025 till 18 december 2025
  - Verifierade att alla specifikations-URL:er pekar till aktuell dokumentation
- **Innehållsvalidering**: Omfattande validering av säkerhetsbästa praxis mot senaste standarder
  - **Microsoft Security Solutions**: Verifierade aktuell terminologi och länkar för Prompt Shields (tidigare "Jailbreak risk detection"), Azure Content Safety, Microsoft Entra ID och Azure Key Vault
  - **OAuth 2.1 Security**: Bekräftade överensstämmelse med senaste OAuth säkerhetsbästa praxis
  - **OWASP-standarder**: Validerade att OWASP Top 10 för LLMs-referenser är aktuella
  - **Azure-tjänster**: Verifierade alla Microsoft Azure-dokumentationslänkar och bästa praxis
- **Standardanpassning**: Alla refererade säkerhetsstandarder bekräftade som aktuella
  - NIST AI Risk Management Framework
  - ISO 27001:2022
  - OAuth 2.1 Security Best Practices
  - Azure säkerhets- och efterlevnadsramverk
- **Implementeringsresurser**: Validerade alla länkar och resurser för implementeringsguider
  - Azure API Management autentiseringsmönster
  - Microsoft Entra ID integrationsguider
  - Azure Key Vault hemlighetshantering
  - DevSecOps pipelines och övervakningslösningar

### Dokumentationskvalitetssäkring
- **Specifikationsöverensstämmelse**: Säkerställde att alla obligatoriska MCP-säkerhetskrav (MÅSTE/MÅSTE INTE) överensstämmer med senaste specifikation
- **Resursaktualitet**: Verifierade alla externa länkar till Microsoft-dokumentation, säkerhetsstandarder och implementeringsguider
- **Täckt bästa praxis**: Bekräftade omfattande täckning av autentisering, auktorisering, AI-specifika hot, leverantörskedjesäkerhet och företagsmönster

## 6 oktober 2025

### Utökning av Kom igång-sektionen – Avancerad serveranvändning & Enkel autentisering

#### Avancerad serveranvändning (03-GettingStarted/10-advanced)
- **Nytt kapitel tillagt**: Introducerade en omfattande guide till avancerad MCP-serveranvändning, som täcker både vanliga och låg-nivå serverarkitekturer.
  - **Vanlig vs. låg-nivå server**: Detaljerad jämförelse och kodexempel i Python och TypeScript för båda tillvägagångssätten.
  - **Handler-baserad design**: Förklaring av handler-baserad verktyg/resurs/prompt-hantering för skalbara, flexibla serverimplementationer.
  - **Praktiska mönster**: Verkliga scenarier där låg-nivå servermönster är fördelaktiga för avancerade funktioner och arkitektur.

#### Enkel autentisering (03-GettingStarted/11-simple-auth)
- **Nytt kapitel tillagt**: Steg-för-steg-guide för att implementera enkel autentisering i MCP-servrar.
  - **Autentiseringskoncept**: Tydlig förklaring av autentisering vs. auktorisering och hantering av referenser.
  - **Grundläggande autentiseringsimplementering**: Middleware-baserade autentiseringsmönster i Python (Starlette) och TypeScript (Express), med kodexempel.
  - **Utveckling till avancerad säkerhet**: Vägledning för att börja med enkel autentisering och gå vidare till OAuth 2.1 och RBAC, med referenser till avancerade säkerhetsmoduler.

Dessa tillägg ger praktisk, handgriplig vägledning för att bygga mer robusta, säkra och flexibla MCP-serverimplementationer, som binder samman grundläggande koncept med avancerade produktionsmönster.

## 29 september 2025

### MCP Server Database Integration Labs - Omfattande praktisk lärandeväg

#### 11-MCPServerHandsOnLabs - Ny komplett databasintegrationsläroplan
- **Fullständig 13-labbars lärandeväg**: Lagt till omfattande praktisk läroplan för att bygga produktionsklara MCP-servrar med PostgreSQL-databasintegration
  - **Verklig implementering**: Zava Retail analytics användningsfall som demonstrerar företagsklassmönster
  - **Strukturerad lärandeprogression**:
    - **Labbar 00-03: Grunder** - Introduktion, kärnarkitektur, säkerhet & multi-tenancy, miljöuppsättning
    - **Labbar 04-06: Bygga MCP-servern** - Databasdesign & schema, MCP-serverimplementation, verktygsutveckling  
    - **Labbar 07-09: Avancerade funktioner** - Semantisk sökintegration, testning & felsökning, VS Code-integration
    - **Labbar 10-12: Produktion & bästa praxis** - Driftsättningsstrategier, övervakning & observabilitet, bästa praxis & optimering
  - **Företagsteknologier**: FastMCP-ramverk, PostgreSQL med pgvector, Azure OpenAI-embeddingar, Azure Container Apps, Application Insights
  - **Avancerade funktioner**: Row Level Security (RLS), semantisk sökning, multi-tenant dataåtkomst, vektorembeddingar, realtidsövervakning

#### Terminologistandardisering - Modul till labb-konvertering
- **Omfattande dokumentationsuppdatering**: Systematiskt uppdaterat alla README-filer i 11-MCPServerHandsOnLabs för att använda "Labb" terminologi istället för "Modul"
  - **Avsnittsrubriker**: Uppdaterade "What This Module Covers" till "What This Lab Covers" i alla 13 labbar
  - **Innehållsbeskrivning**: Ändrade "This module provides..." till "This lab provides..." i hela dokumentationen
  - **Lärandemål**: Uppdaterade "By the end of this module..." till "By the end of this lab..."
  - **Navigeringslänkar**: Konverterade alla "Module XX:" referenser till "Lab XX:" i korsreferenser och navigation
  - **Slutförandespårning**: Uppdaterade "After completing this module..." till "After completing this lab..."
  - **Bevarade tekniska referenser**: Behöll Python-modulreferenser i konfigurationsfiler (t.ex. `"module": "mcp_server.main"`)

#### Förbättring av studieguide (study_guide.md)
- **Visuell läroplansöversikt**: Lagt till nytt avsnitt "11. Database Integration Labs" med omfattande labbstrukturvisualisering
- **Repositorystruktur**: Uppdaterad från tio till elva huvudavsnitt med detaljerad beskrivning av 11-MCPServerHandsOnLabs
- **Vägledning för lärandeväg**: Förbättrade navigeringsinstruktioner för att täcka avsnitt 00-11
- **Teknologitäckning**: Lagt till detaljer om FastMCP, PostgreSQL, Azure-tjänsters integration
- **Läranderesultat**: Betoning på produktionsklar serverutveckling, databasintegrationsmönster och företagsäkerhet

#### Förbättring av huvud-README-struktur
- **Labb-baserad terminologi**: Uppdaterade huvud-README.md i 11-MCPServerHandsOnLabs för att konsekvent använda "Labb"-struktur
- **Organisation av lärandeväg**: Tydlig progression från grundläggande koncept till avancerad implementering och produktionsdrift
- **Verklighetsfokus**: Betoning på praktiskt, handgripligt lärande med företagsklassmönster och teknologier

### Förbättringar av dokumentationskvalitet & konsekvens
- **Praktiskt lärandefokus**: Förstärkt praktiskt, labb-baserat tillvägagångssätt i hela dokumentationen
- **Företagsmönsterfokus**: Framlyft produktionsklara implementationer och företagsäkerhetsaspekter
- **Teknologiintegration**: Omfattande täckning av moderna Azure-tjänster och AI-integrationsmönster
- **Lärandeprogression**: Tydlig, strukturerad väg från grundläggande koncept till produktionsdrift

## 26 september 2025

### Förbättring av fallstudier - GitHub MCP Registry-integration

#### Fallstudier (09-CaseStudy/) - Fokus på ekosystemutveckling
- **README.md**: Stor utökning med omfattande GitHub MCP Registry-fallstudie
  - **GitHub MCP Registry-fallstudie**: Ny omfattande fallstudie som undersöker GitHubs MCP Registry-lansering i september 2025
    - **Problemanalys**: Detaljerad granskning av fragmenterade MCP-serverupptäckts- och driftsättningsutmaningar
    - **Lösningsarkitektur**: GitHubs centraliserade registermetod med en-klicks VS Code-installation
    - **Affärspåverkan**: Mätbara förbättringar i utvecklarintroduktion och produktivitet
    - **Strategiskt värde**: Fokus på modulär agentdriftsättning och tvärverktygsinteroperabilitet
    - **Ekosystemutveckling**: Positionering som grundläggande plattform för agentisk integration
  - **Förbättrad fallstudiestruktur**: Uppdaterade alla sju fallstudier med konsekvent formatering och omfattande beskrivningar
    - Azure AI Travel Agents: Fokus på multi-agent orkestrering
    - Azure DevOps Integration: Fokus på arbetsflödesautomatisering
    - Realtidsdokumenthämtning: Python-konsolklientimplementation
    - Interaktiv studieplansgenerator: Chainlit konversationswebbapp
    - In-Editor-dokumentation: VS Code och GitHub Copilot-integration
    - Azure API Management: Företags-API-integrationsmönster
    - GitHub MCP Registry: Ekosystemutveckling och communityplattform
  - **Omfattande slutsats**: Omskriven slutsatssektion som lyfter fram sju fallstudier som täcker flera MCP-implementeringsdimensioner
    - Företagsintegration, multi-agent orkestrering, utvecklarproduktivitet
    - Ekosystemutveckling, utbildningsapplikationer kategorisering
    - Fördjupade insikter i arkitekturmönster, implementeringsstrategier och bästa praxis
    - Betoning på MCP som mogen, produktionsklar protokoll

#### Uppdateringar av studieguide (study_guide.md)
- **Visuell läroplansöversikt**: Uppdaterad mindmap för att inkludera GitHub MCP Registry i Fallstudier-sektionen
- **Fallstudiebeskrivning**: Förbättrad från generiska beskrivningar till detaljerad genomgång av sju omfattande fallstudier
- **Repositorystruktur**: Uppdaterat avsnitt 10 för att spegla omfattande fallstudietäckning med specifika implementationsdetaljer
- **Ändringsloggsintegration**: Lagt till 26 september 2025-post som dokumenterar GitHub MCP Registry-tillägg och fallstudieförbättringar
- **Datumuppdateringar**: Uppdaterat sidfots-tidsstämpel för att spegla senaste revision (26 september 2025)

### Förbättringar av dokumentationskvalitet
- **Konsekvensförbättring**: Standardiserad fallstudieformatering och struktur över alla sju exempel
- **Omfattande täckning**: Fallstudier täcker nu företags-, utvecklarproduktivitet- och ekosystemutvecklingsscenarier
- **Strategisk positionering**: Förstärkt fokus på MCP som grundläggande plattform för agentiska systemdriftsättningar
- **Resursintegration**: Uppdaterade ytterligare resurser för att inkludera GitHub MCP Registry-länk

## 15 september 2025

### Utökning av avancerade ämnen - Anpassade transportlager & Context Engineering

#### MCP Custom Transports (05-AdvancedTopics/mcp-transport/) - Ny avancerad implementeringsguide
- **README.md**: Komplett implementeringsguide för anpassade MCP-transportmekanismer
  - **Azure Event Grid Transport**: Omfattande serverlös händelsedriven transportimplementation
    - Exempel i C#, TypeScript och Python med Azure Functions-integration
    - Händelsedrivna arkitekturmönster för skalbara MCP-lösningar
    - Webhook-mottagare och push-baserad meddelandehantering
  - **Azure Event Hubs Transport**: Höggenomströmning streaming-transportimplementation
    - Realtidsstreamingmöjligheter för låg-latensscenarier
    - Partitioneringsstrategier och checkpoint-hantering
    - Meddelandebatchning och prestandaoptimering
  - **Företagsintegrationsmönster**: Produktionsklara arkitektur-exempel
    - Distribuerad MCP-bearbetning över flera Azure Functions
    - Hybridtransportarkitekturer som kombinerar flera transporttyper
    - Meddelandets hållbarhet, tillförlitlighet och felhanteringsstrategier
  - **Säkerhet & övervakning**: Azure Key Vault-integration och observabilitetsmönster
    - Hanterad identitetsautentisering och principen om minsta privilegium
    - Application Insights telemetri och prestandaövervakning
    - Strömbrytare och felmotståndsmönster
  - **Testningsramverk**: Omfattande teststrategier för anpassade transporter
    - Enhetstestning med testdubbler och mocking-ramverk
    - Integrationstestning med Azure Test Containers
    - Prestanda- och belastningstestningsöverväganden

#### Context Engineering (05-AdvancedTopics/mcp-contextengineering/) - Framväxande AI-disciplin
- **README.md**: Omfattande utforskning av context engineering som ett framväxande område
  - **Kärnprinciper**: Komplett kontextdelning, medvetenhet om handlingsbeslut och hantering av kontextfönster
  - **MCP-protokollanpassning**: Hur MCP-design adresserar context engineering-utmaningar
    - Begränsningar i kontextfönster och progressiv laddningsstrategi
    - Relevansbestämning och dynamisk kontexthämtning
    - Multimodal kontexthantering och säkerhetsaspekter
  - **Implementeringsmetoder**: Entrådad vs. multi-agentarkitektur
    - Kontextuppdelning och prioriteringstekniker
    - Progressiv kontextladdning och komprimeringsstrategier
    - Lager-på-lager kontextmetoder och optimering av hämtning
  - **Mätningsramverk**: Framväxande mätvärden för utvärdering av kontexteffektivitet
    - Indataeffektivitet, prestanda, kvalitet och användarupplevelse
    - Experimentella tillvägagångssätt för kontextoptimering
    - Felanalys och förbättringsmetodiker

#### Uppdateringar av läroplansnavigation (README.md)
- **Förbättrad modulstruktur**: Uppdaterad läroplanstabell för att inkludera nya avancerade ämnen
  - Tillagt Context Engineering (5.14) och Custom Transport (5.15)
  - Konsekvent formatering och navigeringslänkar över alla moduler
  - Uppdaterade beskrivningar för att spegla aktuellt innehållsomfång

### Förbättringar av katalogstruktur
- **Namngivningsstandardisering**: Omdöpt "mcp transport" till "mcp-transport" för konsekvens med andra avancerade ämnesmappar
- **Innehållsorganisation**: Alla 05-AdvancedTopics-mappar följer nu konsekvent namngivningsmönster (mcp-[ämne])

### Förbättringar av dokumentationskvalitet
- **MCP-specifikationsanpassning**: Allt nytt innehåll refererar till aktuell MCP-specifikation 2025-06-18
- **Fler språkexempel**: Omfattande kodexempel i C#, TypeScript och Python
- **Företagsfokus**: Produktionsklara mönster och Azure-molnintegration genomgående
- **Visuell dokumentation**: Mermaid-diagram för arkitektur- och flödesvisualisering

## 18 augusti 2025

### Omfattande dokumentationsuppdatering - MCP 2025-06-18 standarder

#### MCP Security Best Practices (02-Security/) - Fullständig modernisering
- **MCP-SECURITY-BEST-PRACTICES-2025.md**: Fullständig omskrivning i linje med MCP-specifikation 2025-06-18
  - **Obligatoriska krav**: Lagt till uttryckliga MÅSTE/MÅSTE INTE-krav från officiell specifikation med tydliga visuella indikatorer
  - **12 kärnsäkerhetspraxis**: Omstrukturerad från 15-punktslista till omfattande säkerhetsdomäner
    - Token-säkerhet & autentisering med integration av extern identitetsleverantör
    - Sessionshantering & transportssäkerhet med kryptografiska krav
    - AI-specifikt hotsskydd med Microsoft Prompt Shields-integration
    - Åtkomstkontroll & behörigheter med principen om minsta privilegium
    - Innehållssäkerhet & övervakning med Azure Content Safety-integration
    - Leverantörskedjesäkerhet med omfattande komponentverifiering
    - OAuth-säkerhet & förhindrande av förväxlad ombud med PKCE-implementering
    - Incidenthantering & återställning med automatiserade funktioner
    - Efterlevnad & styrning med regulatorisk anpassning
    - Avancerade säkerhetskontroller med zero trust-arkitektur
    - Microsofts säkerhetsekosystemintegration med omfattande lösningar
    - Kontinuerlig säkerhetsevolution med adaptiva metoder
  - **Microsofts säkerhetslösningar**: Förbättrad integrationsvägledning för Prompt Shields, Azure Content Safety, Entra ID och GitHub Advanced Security
  - **Implementeringsresurser**: Kategoriserade omfattande resurslänkar efter Officiell MCP-dokumentation, Microsofts säkerhetslösningar, säkerhetsstandarder och implementeringsguider

#### Avancerade säkerhetskontroller (02-Security/) - Företagsimplementering
- **MCP-SECURITY-CONTROLS-2025.md**: Fullständig översyn med säkerhetsramverk i företagsklass
  - **9 omfattande säkerhetsdomäner**: Utökade från grundläggande kontroller till detaljerat företagsramverk
    - Avancerad autentisering & auktorisering med Microsoft Entra ID-integration
    - Token-säkerhet & anti-passthrough-kontroller med omfattande validering
    - Sessionssäkerhetskontroller med förebyggande av kapning
    - AI-specifika säkerhetskontroller med skydd mot promptinjektion och verktygsförgiftning
    - Förhindrande av förväxlad ombud-attack med OAuth-proxy-säkerhet
    - Verktygsexekveringssäkerhet med sandboxing och isolering
    - Leverantörskedjesäkerhetskontroller med beroendeverifiering
    - Övervaknings- & detektionskontroller med SIEM-integration
    - Incidenthantering & återställning med automatiserade funktioner
  - **Implementeringsexempel**: Lagt till detaljerade YAML-konfigurationsblock och kodexempel
  - **Microsoft-lösningsintegration**: Omfattande täckning av Azure-säkerhetstjänster, GitHub Advanced Security och företagsidentitetshantering

#### Avancerade ämnen säkerhet (05-AdvancedTopics/mcp-security/) - Produktionsfärdig implementering
- **README.md**: Fullständig omskrivning för företags säkerhetsimplementering
  - **Aktuell specifikationsanpassning**: Uppdaterad till MCP Specification 2025-06-18 med obligatoriska säkerhetskrav
  - **Förbättrad autentisering**: Microsoft Entra ID-integration med omfattande .NET- och Java Spring Security-exempel
  - **AI-säkerhetsintegration**: Microsoft Prompt Shields och Azure Content Safety-implementering med detaljerade Python-exempel
  - **Avancerad hotmitigering**: Omfattande implementeringsexempel för
    - Förhindrande av förväxlad ombud-attack med PKCE och användarsamtyckesvalidering
    - Förhindrande av token-passthrough med publikumsvalidering och säker tokenhantering
    - Förhindrande av sessionkapning med kryptografisk bindning och beteendeanalys
  - **Företagssäkerhetsintegration**: Azure Application Insights-övervakning, hotdetektionspipelines och leverantörskedjesäkerhet
  - **Implementeringschecklista**: Tydliga obligatoriska kontra rekommenderade säkerhetskontroller med fördelar från Microsofts säkerhetsekosystem

### Dokumentationskvalitet & standardanpassning
- **Specifikationsreferenser**: Uppdaterade alla referenser till aktuella MCP Specification 2025-06-18
- **Microsofts säkerhetsekosystem**: Förbättrad integrationsvägledning i all säkerhetsdokumentation
- **Praktisk implementering**: Lagt till detaljerade kodexempel i .NET, Java och Python med företagsmönster
- **Resursorganisation**: Omfattande kategorisering av officiell dokumentation, säkerhetsstandarder och implementeringsguider
- **Visuella indikatorer**: Tydlig markering av obligatoriska krav kontra rekommenderade metoder


#### Kärnkoncept (01-CoreConcepts/) - Fullständig modernisering
- **Protokollversionsuppdatering**: Uppdaterad för att referera till aktuella MCP Specification 2025-06-18 med datum-baserad versionering (ÅÅÅÅ-MM-DD-format)
- **Arkitekturförfining**: Förbättrade beskrivningar av Hosts, Clients och Servers för att spegla aktuella MCP-arkitekturmodeller
  - Hosts definieras nu tydligt som AI-applikationer som koordinerar flera MCP-klientanslutningar
  - Clients beskrivs som protokollkopplingar som upprätthåller en-till-en-serverrelationer
  - Servers förbättrade med lokala kontra fjärrdistributionsscenarier
- **Primitiv omstrukturering**: Fullständig översyn av server- och klientprimitiver
  - Serverprimitiver: Resurser (datakällor), Prompter (mallar), Verktyg (exekverbara funktioner) med detaljerade förklaringar och exempel
  - Klientprimitiver: Sampling (LLM-kompletteringar), Elicitation (användarinmatning), Logging (felsökning/övervakning)
  - Uppdaterade med aktuella upptäckts- (`*/list`), hämt- (`*/get`) och exekverings- (`*/call`) metodmönster
- **Protokollarkitektur**: Infört tvålagers arkitekturmodell
  - Datalager: JSON-RPC 2.0-grund med livscykelhantering och primitiv
  - Transportlager: STDIO (lokal) och Streamable HTTP med SSE (fjärr) transportmekanismer
- **Säkerhetsramverk**: Omfattande säkerhetsprinciper inklusive uttryckligt användarsamtycke, dataskydd, verktygsexekveringssäkerhet och transportsäkerhet
- **Kommunikationsmönster**: Uppdaterade protokollmeddelanden för att visa initialisering, upptäckt, exekvering och notifieringsflöden
- **Kodexempel**: Uppdaterade flerspråkiga exempel (.NET, Java, Python, JavaScript) för att spegla aktuella MCP SDK-mönster

#### Säkerhet (02-Security/) - Omfattande säkerhetsöversyn  
- **Standardanpassning**: Fullständig anpassning till MCP Specification 2025-06-18 säkerhetskrav
- **Autentiseringsevolution**: Dokumenterad utveckling från egna OAuth-servrar till delegation via extern identitetsleverantör (Microsoft Entra ID)
- **AI-specifik hotanalys**: Förbättrad täckning av moderna AI-attackvektorer
  - Detaljerade scenarier för promptinjektionsattacker med verkliga exempel
  - Verktygsförgiftningsmekanismer och "rug pull"-attackmönster
  - Kontextfönsterförgiftning och modellförvirringsattacker
- **Microsoft AI-säkerhetslösningar**: Omfattande täckning av Microsofts säkerhetsekosystem
  - AI Prompt Shields med avancerad detektion, spotlighting och avgränsartekniker
  - Azure Content Safety-integrationsmönster
  - GitHub Advanced Security för leverantörskedjeskydd
- **Avancerad hotmitigering**: Detaljerade säkerhetskontroller för
  - Sessionkapning med MCP-specifika attackscenarier och kryptografiska sessions-ID-krav
  - Förväxlad ombud-problem i MCP-proxy-scenarier med uttryckliga samtyckeskrav
  - Token-passthrough-sårbarheter med obligatoriska valideringskontroller
- **Leverantörskedjesäkerhet**: Utökad AI-leverantörskedjetäckning inklusive grundmodeller, embeddings-tjänster, kontextleverantörer och tredjeparts-API:er
- **Grundläggande säkerhet**: Förbättrad integration med företags säkerhetsmönster inklusive zero trust-arkitektur och Microsofts säkerhetsekosystem
- **Resursorganisation**: Kategoriserade omfattande resurslänkar efter typ (Officiella dokument, standarder, forskning, Microsoft-lösningar, implementeringsguider)

### Förbättringar av dokumentationskvalitet
- **Strukturerade lärandemål**: Förbättrade lärandemål med specifika, handlingsbara resultat
- **Korsreferenser**: Lagt till länkar mellan relaterade säkerhets- och kärnkonceptämnen
- **Aktuell information**: Uppdaterade alla datumreferenser och specifikationslänkar till aktuella standarder
- **Implementeringsvägledning**: Lagt till specifika, handlingsbara implementeringsriktlinjer i båda sektionerna

## 16 juli 2025

### README och navigeringsförbättringar
- Fullständigt omdesignad kursnavigering i README.md
- Ersatte `<details>`-taggar med mer tillgängligt tabellformat
- Skapade alternativa layoutalternativ i ny mapp "alternative_layouts"
- Lagt till kortbaserade, flik-stil och dragspels-stil navigeringsexempel
- Uppdaterade avsnittet om repositorystruktur för att inkludera alla senaste filer
- Förbättrade avsnittet "Hur man använder denna kurs" med tydliga rekommendationer
- Uppdaterade MCP-specifikationslänkar för att peka på korrekta URL:er
- Lagt till avsnittet Context Engineering (5.14) i kursstrukturen

### Uppdateringar av studievägledning
- Fullständigt reviderad studievägledning för att stämma överens med aktuell repositorystruktur
- Lagt till nya avsnitt för MCP-klienter och verktyg samt populära MCP-servrar
- Uppdaterade den visuella kurskartan för att korrekt spegla alla ämnen
- Förbättrade beskrivningar av avancerade ämnen för att täcka alla specialiserade områden
- Uppdaterade fallstudieavsnittet för att spegla faktiska exempel
- Lagt till denna omfattande ändringslogg

### Communitybidrag (06-CommunityContributions/)
- Lagt till detaljerad information om MCP-servrar för bildgenerering
- Lagt till omfattande avsnitt om att använda Claude i VSCode
- Lagt till instruktioner för installation och användning av Cline terminalklient
- Uppdaterade MCP-klientavsnittet för att inkludera alla populära klientalternativ
- Förbättrade bidragsexempel med mer exakta kodexempel

### Avancerade ämnen (05-AdvancedTopics/)
- Organiserade alla specialiserade ämnesmappar med konsekvent namngivning
- Lagt till material och exempel för context engineering
- Lagt till dokumentation för Foundry-agentintegration
- Förbättrad dokumentation för Entra ID-säkerhetsintegration

## 11 juni 2025

### Initial skapelse
- Släppt första versionen av MCP för nybörjare-kursen
- Skapade grundstruktur för alla 10 huvudsektioner
- Implementerade visuell kurskarta för navigering
- Lagt till initiala exempelprojekt i flera programmeringsspråk

### Kom igång (03-GettingStarted/)
- Skapade första serverimplementeringsexempel
- Lagt till vägledning för klientutveckling
- Inkluderade instruktioner för LLM-klientintegration
- Lagt till dokumentation för VS Code-integration
- Implementerade Server-Sent Events (SSE) serverexempel

### Kärnkoncept (01-CoreConcepts/)
- Lagt till detaljerad förklaring av klient-server-arkitektur
- Skapade dokumentation om nyckelkomponenter i protokollet
- Dokumenterade meddelandemönster i MCP

## 23 maj 2025

### Repositorystruktur
- Initierade repository med grundläggande mappstruktur
- Skapade README-filer för varje huvudsektion
- Satt upp översättningsinfrastruktur
- Lagt till bildresurser och diagram

### Dokumentation
- Skapade initial README.md med kursöversikt
- Lagt till CODE_OF_CONDUCT.md och SECURITY.md
- Satt upp SUPPORT.md med vägledning för att få hjälp
- Skapade preliminär studievägledningsstruktur

## 15 april 2025

### Planering och ramverk
- Initial planering för MCP för nybörjare-kursen
- Definierade lärandemål och målgrupp
- Skissade 10-sektionsstruktur för kursen
- Utvecklade konceptuellt ramverk för exempel och fallstudier
- Skapade initiala prototyp-exempel för nyckelkoncept

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->