# Praktisk implementation

[![How to Build, Test, and Deploy MCP Apps with Real Tools and Workflows](../../../translated_images/sv/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Klicka på bilden ovan för att se video av denna lektion)_

Praktisk implementation är där kraften i Model Context Protocol (MCP) blir påtaglig. Medan förståelsen av teorin och arkitekturen bakom MCP är viktig, uppstår det verkliga värdet när du tillämpar dessa koncept för att bygga, testa och distribuera lösningar som löser verkliga problem. Detta kapitel överbryggar gapet mellan konceptuell kunskap och praktisk utveckling och guidar dig genom processen att ge liv åt MCP-baserade applikationer.

Oavsett om du utvecklar intelligenta assistenter, integrerar AI i affärsflöden eller bygger specialanpassade verktyg för databehandling, erbjuder MCP en flexibel grund. Dess språkoberoende design och officiella SDK:er för populära programmeringsspråk gör det tillgängligt för en bred krets utvecklare. Genom att utnyttja dessa SDK:er kan du snabbt prototypa, iterera och skala dina lösningar över olika plattformar och miljöer.

I följande avsnitt hittar du praktiska exempel, kodexempel och distributionsstrategier som visar hur du implementerar MCP i C#, Java med Spring, TypeScript, JavaScript och Python. Du kommer också lära dig hur du felsöker och testar dina MCP-servrar, hanterar API:er och distribuerar lösningar till molnet med Azure. Dessa praktiska resurser är utformade för att påskynda din inlärning och hjälpa dig att tryggt bygga robusta, produktionsklara MCP-applikationer.

## Översikt

Denna lektion fokuserar på praktiska aspekter av MCP-implementation över flera programmeringsspråk. Vi kommer att utforska hur du använder MCP SDK:er i C#, Java med Spring, TypeScript, JavaScript och Python för att bygga robusta applikationer, felsöka och testa MCP-servrar samt skapa återanvändbara resurser, prompts och verktyg.

## Lärandemål

I slutet av denna lektion kommer du att kunna:

- Implementera MCP-lösningar med officiella SDK:er i olika programmeringsspråk  
- Felsöka och testa MCP-servrar systematiskt  
- Skapa och använda serverfunktioner (Resurser, Prompts och Verktyg)  
- Designa effektiva MCP-arbetsflöden för komplexa uppgifter  
- Optimera MCP-implementationer för prestanda och tillförlitlighet  

## Officiella SDK-resurser

Model Context Protocol erbjuder officiella SDK:er för flera språk (i linje med [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java med Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Obs:** kräver beroende av [Project Reactor](https://projectreactor.io). (Se [diskussionsfråga 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Arbeta med MCP SDK:er

Detta avsnitt ger praktiska exempel på att implementera MCP med flera programmeringsspråk. Du kan hitta kodexempel i `samples`-katalogen organiserad efter språk.

### Tillgängliga exempel

Förrådet inkluderar [exempelimplementationer](../../../04-PracticalImplementation/samples) i följande språk:

- [C#](./samples/csharp/README.md)
- [Java med Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Varje exempel demonstrerar nyckelbegrepp och implementationsmönster för MCP för det specifika språket och ekosystemet.

### Praktiska guider

Ytterligare guider för praktisk MCP-implementation:

- [Pagination and Large Result Sets](./pagination/README.md) - Hantera kursorbasserad paginering för verktyg, resurser och stora dataset

## Kärnfunktioner för servern

MCP-servrar kan implementera en kombination av dessa funktioner:

### Resurser

Resurser ger kontext och data för användaren eller AI-modellen att använda:

- Dokumentförråd  
- Kunskapsbaser  
- Strukturerade datakällor  
- Filsystem  

### Prompts

Prompts är mallade meddelanden och arbetsflöden för användare:

- Fördefinierade konversationsmallar  
- Vägledda interaktionsmönster  
- Specialiserade dialogstrukturer  

### Verktyg

Verktyg är funktioner för AI-modellen att exekvera:

- Databehandlingsverktyg  
- Integrationer med externa API:er  
- Beräkningsmöjligheter  
- Sökmöjligheter  

## Exempelimplementationer: C# Implementation

Det officiella C# SDK-förrådet innehåller flera exempelimplementationer som demonstrerar olika aspekter av MCP:

- **Grundläggande MCP-klient**: Enkel exempel som visar hur man skapar en MCP-klient och anropar verktyg  
- **Grundläggande MCP-server**: Minimal serverimplementering med grundläggande verktygsregistrering  
- **Avancerad MCP-server**: Fullfjädrad server med verktygsregistrering, autentisering och felhantering  
- **ASP.NET-integration**: Exempel som demonstrerar integration med ASP.NET Core  
- **Verktygsimplementeringsmönster**: Olika mönster för att implementera verktyg med olika komplexitetsnivåer  

MCP C# SDK är i förhandsversion och API:erna kan förändras. Vi kommer att kontinuerligt uppdatera denna blogg i takt med att SDK utvecklas.

### Nyckelfunktioner

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)  
- Bygg din [första MCP-server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).  

För kompletta C# implementationsexempel, besök det [officiella C# SDK-exempelförrådet](https://github.com/modelcontextprotocol/csharp-sdk)

## Exempelimplementation: Java med Spring Implementation

Java med Spring SDK erbjuder robusta MCP-implementationsalternativ med företagsklassfunktioner.

### Nyckelfunktioner

- Integration med Spring Framework  
- Stark typ-säkerhet  
- Stöd för reaktiv programmering  
- Omfattande felhantering  

För en komplett Java med Spring implementation, se [Java med Spring-exempel](samples/java/containerapp/README.md) i exempel-katalogen.

## Exempelimplementation: JavaScript Implementation

JavaScript SDK ger ett lättviktigt och flexibelt tillvägagångssätt för MCP-implementation.

### Nyckelfunktioner

- Stöd för Node.js och webbläsare  
- Promise-baserat API  
- Enkel integration med Express och andra ramverk  
- WebSocket-stöd för strömning  

För ett komplett JavaScript-implementationsprov, se [JavaScript-exempel](samples/javascript/README.md) i exempel-katalogen.

## Exempelimplementation: Python Implementation

Python SDK erbjuder ett pythoniskt tillvägagångssätt för MCP-implementation med utmärkta ML-ramverksintegrationer.

### Nyckelfunktioner

- Async/await-stöd med asyncio  
- FastAPI-integration  
- Enkel verktygsregistrering  
- Naturlig integration med populära ML-bibliotek  

För ett komplett Python-implementationsprov, se [Python-exempel](samples/python/README.md) i exempel-katalogen.

## API-hantering

Azure API Management är ett utmärkt svar på hur vi kan säkra MCP-servrar. Idén är att sätta en Azure API Management-instans framför din MCP-server och låta den hantera funktioner du sannolikt vill ha som:

- begränsning av antal anrop  
- token-hantering  
- övervakning  
- lastbalansering  
- säkerhet  

### Azure-exempel

Här är ett Azure-exempel som gör precis det, dvs [skapar en MCP-server och säkrar den med Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Se hur auktoriseringsflödet sker i bilden nedan:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

I bilden ovan sker följande:

- Autentisering/Auktorisering sker med Microsoft Entra.  
- Azure API Management agerar som en gateway och använder policies för att styra och hantera trafik.  
- Azure Monitor loggar alla förfrågningar för vidare analys.  

#### Auktoriseringsflöde

Låt oss titta närmare på auktoriseringsflödet:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP auktoriseringsspecifikation

Läs mer om [MCP Authorization specification](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Distribuera Remote MCP Server till Azure

Låt oss se om vi kan distribuera exemplet vi nämnde tidigare:

1. Klona förrådet

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registrera `Microsoft.App`-resursleverantör.

   - Om du använder Azure CLI, kör `az provider register --namespace Microsoft.App --wait`.  
   - Om du använder Azure PowerShell, kör `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Kör sedan `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` efter en stund för att kontrollera om registreringen är klar.

1. Kör detta [azd](https://aka.ms/azd)-kommando för att provisionera API Management-tjänsten, funktionsappen (med kod) och alla andra nödvändiga Azure-resurser

    ```shell
    azd up
    ```

    Detta kommando bör distribuera alla molnresurser på Azure

### Testa din server med MCP Inspector

1. I ett **nytt terminalfönster**, installera och kör MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Du bör se ett gränssnitt som liknar:

    ![Connect to Node inspector](../../../translated_images/sv/connect.141db0b2bd05f096.webp)

1. CTRL-klicka för att ladda MCP Inspector webbappen från den URL som visas av appen (t.ex. [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))  
1. Ställ in transporttypen till `SSE`  
1. Ange URL:en till din körande API Management SSE-endpoint som visas efter `azd up` och **Anslut**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Lista verktyg**. Klicka på ett verktyg och **Kör verktyg**.  

Om alla steg fungerat bör du nu vara ansluten till MCP-servern och ha kunnat anropa ett verktyg.

## MCP-servrar för Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Denna uppsättning förråd är snabbstartsmallar för att bygga och distribuera anpassade fjärr-MCP (Model Context Protocol) servrar med Azure Functions med Python, C# .NET eller Node/TypeScript.

Exemplen erbjuder en komplett lösning som låter utvecklare:

- Bygga och köra lokalt: Utveckla och felsöka en MCP-server på en lokal maskin  
- Distribuera till Azure: Enkel distribution till molnet med ett enkelt `azd up`-kommando  
- Ansluta från klienter: Anslut till MCP-servern från olika klienter inklusive VS Code:s Copilot agentläge och MCP Inspector-verktyget  

### Nyckelfunktioner

- Säkerhet som standard: MCP-servern är säkrad med nycklar och HTTPS  
- Autentiseringsalternativ: Stöder OAuth med inbyggd auth och/eller API Management  
- Nätverksisolering: Tillåter nätverksisolering med Azure Virtual Networks (VNET)  
- Serverless-arkitektur: Utnyttjar Azure Functions för skalbar, händelsedriven körning  
- Lokal utveckling: Omfattande stöd för lokal utveckling och felsökning  
- Enkel distribution: Strömlinjeformad distributionsprocess till Azure  

Förrådet innehåller alla nödvändiga konfigurationsfiler, källkod och infrastrukturbeskrivningar för att snabbt komma igång med en produktionsklar MCP-serverimplementation.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Exempelimplementation av MCP med Azure Functions och Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Exempelimplementation av MCP med Azure Functions och C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Exempelimplementation av MCP med Azure Functions och Node/TypeScript.

## Viktiga lärdomar

- MCP SDK:er erbjuder språk-specifika verktyg för att implementera robusta MCP-lösningar  
- Felsöknings- och testprocessen är avgörande för pålitliga MCP-applikationer  
- Återanvändbara promptmallar möjliggör konsekventa AI-interaktioner  
- Väl utformade arbetsflöden kan orkestrera komplexa uppgifter med flera verktyg  
- Implementering av MCP-lösningar kräver hänsyn till säkerhet, prestanda och felhantering  

## Övning

Designa ett praktiskt MCP-arbetsflöde som adresserar ett verkligt problem inom ditt område:

1. Identifiera 3-4 verktyg som skulle vara användbara för att lösa detta problem  
2. Skapa ett arbetsflödesdiagram som visar hur dessa verktyg interagerar  
3. Implementera en grundläggande version av ett av verktygen med ditt föredragna språk  
4. Skapa en promptmall som hjälper modellen att effektivt använda ditt verktyg  

## Ytterligare resurser

---

## Vad är nästa

Nästa: [Avancerade ämnen](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->