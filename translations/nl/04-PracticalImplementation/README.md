# Praktische Implementatie

[![Hoe MCP-apps te bouwen, testen en implementeren met echte tools en workflows](../../../translated_images/nl/05.64bea204e25ca891.webp)](https://youtu.be/vCN9-mKBDfQ)

_(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

Praktische implementatie is waar de kracht van het Model Context Protocol (MCP) tastbaar wordt. Hoewel het belangrijk is de theorie en architectuur achter MCP te begrijpen, ontstaat de echte waarde wanneer je deze concepten toepast om oplossingen te bouwen, testen en implementeren die echte problemen oplossen. Dit hoofdstuk overbrugt de kloof tussen conceptuele kennis en praktische ontwikkeling en begeleidt je bij het proces van het tot leven brengen van MCP-gebaseerde applicaties.

Of je nu intelligente assistenten ontwikkelt, AI integreert in bedrijfsworkflows of aangepaste tools bouwt voor gegevensverwerking, MCP biedt een flexibele basis. Het taalonafhankelijke ontwerp en officiële SDK's voor populaire programmeertalen maken het toegankelijk voor een breed scala aan ontwikkelaars. Door gebruik te maken van deze SDK's kun je snel prototypes maken, itereren en je oplossingen schalen over verschillende platforms en omgevingen.

In de volgende secties vind je praktische voorbeelden, voorbeeldcode en implementatiestrategieën die aantonen hoe MCP te implementeren in C#, Java met Spring, TypeScript, JavaScript en Python. Je leert ook hoe je MCP-servers debugt en test, API's beheert en oplossingen naar de cloud implementeert met Azure. Deze praktische middelen zijn ontworpen om je leerproces te versnellen en je te helpen robuuste en productieklare MCP-applicaties met vertrouwen te bouwen.

## Overzicht

Deze les richt zich op praktische aspecten van MCP-implementatie over meerdere programmeertalen. We onderzoeken hoe je MCP SDK's gebruikt in C#, Java met Spring, TypeScript, JavaScript en Python om robuuste applicaties te bouwen, MCP-servers te debuggen en testen, en herbruikbare resources, prompts en tools te creëren.

## Leerdoelen

Aan het einde van deze les kun je:

- MCP-oplossingen implementeren met behulp van officiële SDK's in verschillende programmeertalen
- MCP-servers systematisch debuggen en testen
- Serverfuncties creëren en gebruiken (Resources, Prompts en Tools)
- Effectieve MCP-workflows ontwerpen voor complexe taken
- MCP-implementaties optimaliseren voor prestaties en betrouwbaarheid

## Officiële SDK Resources

Het Model Context Protocol biedt officiële SDK's voor meerdere talen (in lijn met [MCP Specificatie 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/)):

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java met Spring SDK](https://github.com/modelcontextprotocol/java-sdk) **Let op:** vereist afhankelijkheid van [Project Reactor](https://projectreactor.io). (Zie [discussie issue 246](https://github.com/orgs/modelcontextprotocol/discussions/246).)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk)

## Werken met MCP SDK's

Deze sectie biedt praktische voorbeelden van MCP-implementatie in meerdere programmeertalen. Je vindt voorbeeldcode in de `samples` map, georganiseerd per taal.

### Beschikbare Voorbeelden

De repository bevat [voorbeeldimplementaties](../../../04-PracticalImplementation/samples) in de volgende talen:

- [C#](./samples/csharp/README.md)
- [Java met Spring](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Elk voorbeeld demonstreert kernconcepten en implementatiepatronen van MCP voor die specifieke taal en ecosysteem.

### Praktische Gidsen

Aanvullende gidsen voor praktische MCP-implementatie:

- [Paginering en grote resultaatsets](./pagination/README.md) - Omgaan met cursor-gebaseerde paginering voor tools, resources en grote datasets

## Kernserverfuncties

MCP-servers kunnen een combinatie van deze functies implementeren:

### Resources

Resources bieden context en data voor de gebruiker of AI-model om te gebruiken:

- Documentrepositories
- Kennisbanken
- Gestructureerde databronnen
- Bestandsystemen

### Prompts

Prompts zijn sjablonen voor berichten en workflows voor gebruikers:

- Vooraf gedefinieerde conversatiesjablonen
- Begeleide interactiepatronen
- Gespecialiseerde dialoogstructuren

### Tools

Tools zijn functies die het AI-model kan uitvoeren:

- Gegevensverwerkingshulpmiddelen
- Externe API-integraties
- Rekencapaciteiten
- Zoekfunctionaliteit

## Voorbeeldimplementaties: C# Implementatie

De officiële C# SDK repository bevat verschillende voorbeeldimplementaties die verschillende aspecten van MCP demonstreren:

- **Basis MCP Client**: Eenvoudig voorbeeld dat laat zien hoe je een MCP-client maakt en tools aanroept
- **Basis MCP Server**: Minimale serverimplementatie met basale tool-registratie
- **Geavanceerde MCP Server**: Volledige server met tool-registratie, authenticatie en foutafhandeling
- **ASP.NET Integratie**: Voorbeelden van integratie met ASP.NET Core
- **Patronen voor tool-implementatie**: Diverse patronen voor het implementeren van tools met verschillende complexiteitsniveaus

De MCP C# SDK is in preview en API's kunnen veranderen. We zullen deze blog continu bijwerken naarmate de SDK evolueert.

### Belangrijke Kenmerken

- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)
- Bouw je [eerste MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Voor complete C# implementatievoorbeelden, bezoek de [officiële C# SDK voorbeeldrepository](https://github.com/modelcontextprotocol/csharp-sdk)

## Voorbeeldimplementatie: Java met Spring Implementatie

De Java met Spring SDK biedt robuuste MCP-implementatieopties met enterprise-grade functionaliteiten.

### Belangrijke Kenmerken

- Integratie met Spring Framework
- Sterke typeveiligheid
- Ondersteuning voor reactief programmeren
- Uitgebreide foutafhandeling

Voor een complete Java met Spring implementatievoorbeeld, zie [Java met Spring voorbeeld](samples/java/containerapp/README.md) in de voorbeeldenmap.

## Voorbeeldimplementatie: JavaScript Implementatie

De JavaScript SDK biedt een lichte en flexibele aanpak voor MCP-implementatie.

### Belangrijke Kenmerken

- Ondersteuning voor Node.js en browser
- Promise-gebaseerde API
- Gemakkelijke integratie met Express en andere frameworks
- WebSocket ondersteuning voor streaming

Voor een compleet JavaScript-implementatievoorbeeld, zie [JavaScript voorbeeld](samples/javascript/README.md) in de voorbeeldenmap.

## Voorbeeldimplementatie: Python Implementatie

De Python SDK biedt een Pythonistische aanpak voor MCP-implementatie met uitstekende integraties voor ML-frameworks.

### Belangrijke Kenmerken

- Async/await ondersteuning met asyncio
- FastAPI integratie``
- Eenvoudige tool-registratie
- Natuurlijke integratie met populaire ML-bibliotheken

Voor een compleet Python-implementatievoorbeeld, zie [Python voorbeeld](samples/python/README.md) in de voorbeeldenmap.

## API-beheer

Azure API Management is een uitstekende oplossing om MCP-servers te beveiligen. Het idee is een Azure API Management instance voor je MCP-server te plaatsen en deze te laten zorgen voor functies die je waarschijnlijk wilt zoals:

- rate limiting
- tokenbeheer
- monitoring
- load balancing
- beveiliging

### Azure Voorbeeld

Hier is een Azure Voorbeeld die precies dat doet, dat wil zeggen [een MCP Server creëren en beveiligen met Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Zie hieronder hoe de autorisatiestroom verloopt:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

In de bovenstaande afbeelding vindt het volgende plaats:

- Authenticatie/Autorisatie vindt plaats via Microsoft Entra.
- Azure API Management fungeert als gateway en gebruikt beleidsregels om het verkeer te sturen en te beheren.
- Azure Monitor logt alle aanvragen voor verdere analyse.

#### Autorisatiestroom

Laten we de autorisatiestroom iets gedetailleerder bekijken:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP autorisatie specificatie

Leer meer over de [MCP Autorisatie specificatie](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/authorization/)

## Implementatie van Remote MCP Server naar Azure

Laten we kijken of we het eerder genoemde voorbeeld kunnen implementeren:

1. Clone de repo

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registreer de `Microsoft.App` resource provider.

   - Als je Azure CLI gebruikt, voer dan `az provider register --namespace Microsoft.App --wait` uit.
   - Als je Azure PowerShell gebruikt, voer dan `Register-AzResourceProvider -ProviderNamespace Microsoft.App` uit. Controleer daarna met `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` na enige tijd of de registratie is voltooid.

1. Voer dit [azd](https://aka.ms/azd) commando uit om de API management service, function app (met code) en alle vereiste Azure resources te provisioneren

    ```shell
    azd up
    ```

    Dit commando moet alle cloudresources op Azure implementeren

### Testen van je server met MCP Inspector

1. Open een **nieuw terminalvenster**, installeer en start MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Je zou een interface moeten zien die lijkt op:

    ![Connect to Node inspector](../../../translated_images/nl/connect.141db0b2bd05f096.webp)

1. CTRL klik om de MCP Inspector webapp te laden via de URL die de app toont (bijvoorbeeld [http://127.0.0.1:6274/#resources](http://127.0.0.1:6274/#resources))
1. Stel het transporttype in op `SSE`
1. Stel de URL in op je lopende API Management SSE-eindpunt, weergegeven na `azd up`, en **Verbind**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

1. **Lijst Tools**. Klik op een tool en **Voer Tool uit**.  

Als alle stappen zijn gelukt, ben je nu verbonden met de MCP-server en heb je een tool kunnen aanroepen.

## MCP-servers voor Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Deze set repositories is een snelstarttemplate om aangepaste remote MCP (Model Context Protocol) servers te bouwen en implementeren met Azure Functions met Python, C# .NET of Node/TypeScript.

De voorbeelden bieden een complete oplossing die ontwikkelaars in staat stelt om:

- Lokaal bouwen en draaien: ontwikkel en debug een MCP-server op een lokale machine
- Implementeren naar Azure: eenvoudig naar de cloud implementeren met een simpel azd up-commando
- Verbinden vanuit clients: verbinden met de MCP-server vanuit verschillende clients, waaronder VS Code’s Copilot agentmodus en de MCP Inspector tool

### Belangrijke Kenmerken

- Beveiliging by design: de MCP-server is beveiligd met sleutels en HTTPS
- Authenticatieopties: ondersteunt OAuth via ingebouwde authenticatie en/of API Management
- Netwerkisolatie: maakt netwerkisolatie mogelijk met Azure Virtual Networks (VNET)
- Serverless architectuur: gebruikt Azure Functions voor schaalbare, event-driven uitvoering
- Lokale ontwikkeling: uitgebreide ondersteuning voor lokale ontwikkeling en debugging
- Eenvoudige implementatie: gestroomlijnd implementatieproces naar Azure

De repository bevat alle benodigde configuratiebestanden, broncode en infrastructuurdefinities om snel te starten met een productieklare MCP-serverimplementatie.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Voorbeeldimplementatie van MCP met Azure Functions in Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Voorbeeldimplementatie van MCP met Azure Functions in C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Voorbeeldimplementatie van MCP met Azure Functions in Node/TypeScript.

## Belangrijkste Leerpunten

- MCP SDK's bieden taalspecifieke hulpmiddelen voor het implementeren van robuuste MCP-oplossingen
- Het debuggen en testen is cruciaal voor betrouwbare MCP-applicaties
- Herbruikbare promptsjablonen zorgen voor consistente AI-interacties
- Goed ontworpen workflows kunnen complexe taken orkestreren met meerdere tools
- Implementeren van MCP-oplossingen vereist aandacht voor beveiliging, prestaties en foutafhandeling

## Oefening

Ontwerp een praktische MCP-workflow die een probleem uit jouw vakgebied oplost:

1. Identificeer 3-4 tools die nuttig zouden zijn voor het oplossen van dit probleem
2. Maak een workflowdiagram waarin de interactie tussen deze tools wordt weergegeven
3. Implementeer een basisversie van één van de tools in je favoriete taal
4. Maak een promptsjabloon die het model helpt jouw tool effectief te gebruiken

## Aanvullende Bronnen

---

## Wat Nu

Volgende: [Geavanceerde Onderwerpen](../05-AdvancedTopics/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->