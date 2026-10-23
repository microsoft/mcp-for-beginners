# HTTPS Streaming met Model Context Protocol (MCP)

Dit hoofdstuk biedt een uitgebreide gids voor het implementeren van veilige, schaalbare en realtime streaming met het Model Context Protocol (MCP) via HTTPS. Het behandelt de motivatie voor streaming, de beschikbare transportmechanismen, hoe je streamable HTTP in MCP implementeert, best practices voor beveiliging, migratie van SSE, en praktische richtlijnen voor het bouwen van je eigen streaming MCP-toepassingen.

> [!WARNING]
> De implementatievoorbeelden in deze les zijn gericht op **MCP Specification
> `2025-11-25`** en demonstreren het legacy `initialize` handshaking,
> `Mcp-Session-Id`, GET-eventstream en het hervattingsmodel. MCP `2026-07-28`
> verwijdert deze functies. Huidige Streamable HTTP-verzoeken zijn zelfstandige
> POST-verzoeken met `MCP-Protocol-Version`- en `Mcp-Method`-headers, plus
> `Mcp-Name` waar nodig. Zie
> [Wat is veranderd in MCP: De specificatie van 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> voordat je deze voorbeelden gebruikt in een nieuwe implementatie.

## Transportmechanismen en streaming in MCP

Deze sectie onderzoekt de verschillende beschikbare transportmechanismen in MCP en hun rol bij het mogelijk maken van streamingfunctionaliteiten voor realtime communicatie tussen clients en servers.

### Wat is een transportmechanisme?

Een transportmechanisme definieert hoe data wordt uitgewisseld tussen de client en server. MCP ondersteunt meerdere transporttypen om aan verschillende omgevingen en vereisten te voldoen:

- **stdio**: Standaard input/output, geschikt voor lokale en CLI-gebaseerde tools. Eenvoudig maar niet geschikt voor web of cloud.
- **HTTP+SSE**: Het legacy remote transport, uitgefaseerd in MCP `2025-03-26`
    en vervangen door Streamable HTTP. Gebruik dit niet voor nieuwe implementaties.
- **Streamable HTTP**: Modern HTTP-gebaseerd streamingtransport, ondersteunt notificaties en betere schaalbaarheid. Aanbevolen voor de meeste productie- en cloudscenario’s.

### Vergelijkingstabel

Bekijk de vergelijkingstabel hieronder om de verschillen tussen deze transportmechanismen te begrijpen:

| Transport | Status | Notificaties | Typisch gebruik |
|---|---|---|---|
| stdio | Actueel | Ja | Lokale subprocessen |
| HTTP+SSE | Uitgefaseerd | Ja | Legacy remote implementaties |
| Streamable HTTP | Actueel | Ja | Remote en cloud servers |

> **Tip:** De keuze van het juiste transport beïnvloedt prestaties, schaalbaarheid en gebruikerservaring. **Streamable HTTP** wordt aanbevolen voor moderne, schaalbare en cloud-klare toepassingen.

De standaardtransports zijn stdio en Streamable HTTP. HTTP+SSE verschijnt alleen in
oudere voorbeelden.

## Streaming: Concepten en motivatie

Het begrijpen van de fundamentele concepten en motivaties achter streaming is essentieel voor het implementeren van effectieve realtime communicatiesystemen.

**Streaming** is een techniek in netwerkprogrammering die het mogelijk maakt data in kleine beheersbare stukken of als een reeks gebeurtenissen te verzenden en ontvangen, in plaats van te wachten tot een compleet antwoord gereed is. Dit is vooral nuttig voor:

- Grote bestanden of datasets.
- Realtime updates (bijv. chat, voortgangsbalken).
- Langdurige berekeningen waarbij je de gebruiker geïnformeerd wilt houden.

Dit is wat je op hoog niveau moet weten over streaming:

- Data wordt stapsgewijs geleverd, niet allemaal tegelijk.
- De client kan data verwerken zodra die binnenkomt.
- Vermindert waargenomen latency en verbetert gebruikerservaring.

### Waarom streaming gebruiken?

De redenen om streaming te gebruiken zijn de volgende:

- Gebruikers krijgen direct feedback, niet pas aan het einde
- Maakt realtime toepassingen en responsieve UI’s mogelijk
- Efficiënter gebruik van netwerk- en verwerkingsmiddelen

### Simpel voorbeeld: HTTP-streaming server & client

Hier is een eenvoudig voorbeeld van hoe streaming geïmplementeerd kan worden:

#### Python

**Server (Python, gebruik makend van FastAPI en StreamingResponse):**

```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

async def event_stream():
    for i in range(1, 6):
        yield f"data: Message {i}\n\n"
        time.sleep(1)

@app.get("/stream")
def stream():
    return StreamingResponse(event_stream(), media_type="text/event-stream")
```

**Client (Python, met requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Dit voorbeeld demonstreert een server die een reeks berichten naar de client stuurt zodra ze beschikbaar zijn, in plaats van te wachten tot alle berichten klaar zijn.

**Hoe het werkt:**

- De server levert elk bericht op zodra het klaar is.
- De client ontvangt en print elk stuk zodra het binnenkomt.

**Vereisten:**

- De server moet een streaming response gebruiken (bijv. `StreamingResponse` in FastAPI).
- De client moet de response als een stream verwerken (`stream=True` in requests).
- Content-Type is meestal `text/event-stream` of `application/octet-stream`.

#### Java

**Server (Java, met Spring Boot en Server-Sent Events):**

```java
@RestController
public class CalculatorController {

    @GetMapping(value = "/calculate", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<ServerSentEvent<String>> calculate(@RequestParam double a,
                                                   @RequestParam double b,
                                                   @RequestParam String op) {
        
        double result;
        switch (op) {
            case "add": result = a + b; break;
            case "sub": result = a - b; break;
            case "mul": result = a * b; break;
            case "div": result = b != 0 ? a / b : Double.NaN; break;
            default: result = Double.NaN;
        }

        return Flux.<ServerSentEvent<String>>just(
                    ServerSentEvent.<String>builder()
                        .event("info")
                        .data("Calculating: " + a + " " + op + " " + b)
                        .build(),
                    ServerSentEvent.<String>builder()
                        .event("result")
                        .data(String.valueOf(result))
                        .build()
                )
                .delayElements(Duration.ofSeconds(1));
    }
}
```

**Client (Java, met Spring WebFlux WebClient):**

```java
@SpringBootApplication
public class CalculatorClientApplication implements CommandLineRunner {

    private final WebClient client = WebClient.builder()
            .baseUrl("http://localhost:8080")
            .build();

    @Override
    public void run(String... args) {
        client.get()
                .uri(uriBuilder -> uriBuilder
                        .path("/calculate")
                        .queryParam("a", 7)
                        .queryParam("b", 5)
                        .queryParam("op", "mul")
                        .build())
                .accept(MediaType.TEXT_EVENT_STREAM)
                .retrieve()
                .bodyToFlux(String.class)
                .doOnNext(System.out::println)
                .blockLast();
    }
}
```

**Java Implementatie Notities:**

- Gebruikt Spring Boot's reactieve stack met `Flux` voor streaming
- `ServerSentEvent` biedt gestructureerde event streaming met event types
- `WebClient` met `bodyToFlux()` maakt reactieve streaming consumptie mogelijk
- `delayElements()` simuleert verwerkingstijd tussen events
- Events kunnen types hebben (`info`, `result`) voor betere client verwerking

### Vergelijking: Klassieke Streaming vs MCP Streaming

De verschillen tussen hoe streaming op een "klassieke" manier werkt tegenover hoe het werkt in MCP kunnen als volgt worden weergegeven:

| Kenmerk                | Klassieke HTTP Streaming         | MCP Streaming (Notificaties)      |
|------------------------|-------------------------------|-------------------------------------|
| Hoofd response          | Gestukt                       | Enkel, aan het einde              |
| Voortgangsupdates       | Verstuurd als datastukken       | Verstuurd als notificaties        |
| Client vereisten        | Moet stream verwerken          | Moet berichthandler implementeren |
| Toepassing             | Grote bestanden, AI token streams | Voortgang, logs, realtime feedback  |

### Belangrijke Verschillen Geconstateerd

Hier zijn daarnaast enkele belangrijke verschillen:

- **Communicatiepatroon:**
  - Klassieke HTTP streaming: gebruikt eenvoudige chunked transfer encoding om data in stukken te verzenden
  - MCP streaming: gebruikt een gestructureerd notificatiesysteem met JSON-RPC protocol

- **Berichtformaat:**
  - Klassieke HTTP: platte tekst stukken met nieuwe regels
  - MCP: Gestructureerde LoggingMessageNotification objecten met metadata

- **Client Implementatie:**
  - Klassieke HTTP: simpele client die streaming responses verwerkt
  - MCP: meer geavanceerde client met een berichtenhandler voor verwerking van verschillende soorten berichten

- **Voortgangsupdates:**
  - Klassieke HTTP: de voortgang is onderdeel van de hoofd response stream
  - MCP: voortgang wordt via aparte notificatieberichten verstuurd terwijl de hoofd response aan het einde komt

### Aanbevelingen

Er zijn enkele dingen die we aanbevelen bij de keuze tussen klassieke streaming implementeren (zoals een endpoint dat we hierboven toonden met `/stream`) of kiezen voor streaming via MCP.

- **Voor eenvoudige streamingbehoeften:** Klassieke HTTP streaming is eenvoudiger te implementeren en voldoende voor basis streaming behoeften.

- **Voor complexe, interactieve applicaties:** MCP streaming biedt een meer gestructureerde aanpak met rijkere metadata en scheiding tussen notificaties en eindresultaten.

- **Voor AI-applicaties:** MCP's notificatiesysteem is vooral nuttig voor langdurige AI taken waarbij je gebruikers wilt informeren over voortgang.

## Streaming in MCP

Oké, je hebt tot nu toe enkele aanbevelingen en vergelijkingen gezien over het verschil tussen klassieke streaming en streaming in MCP. Laten we gedetailleerd ingaan op hoe je streaming in MCP kunt benutten.

Begrijpen hoe streaming werkt binnen het MCP-framework is essentieel voor het bouwen van responsieve applicaties die realtime feedback aan gebruikers geven tijdens langdurige operaties.

In MCP gaat streaming niet over het hoofdantwoord in stukken sturen, maar over het sturen van **notificaties** naar de client terwijl een tool een verzoek verwerkt. Deze notificaties kunnen voortgangsupdates, logs of andere gebeurtenissen bevatten.

### Hoe het werkt

Het hoofdresultaat wordt nog steeds als één enkele response gestuurd. Echter, notificaties kunnen tijdens de verwerking als aparte berichten worden verzonden en zo de client realtime updaten. De client moet deze notificaties kunnen verwerken en tonen.

### Optionele oefening: verbinden met een gehoste MCP server

Je kunt ook Streamable HTTP gebruiken zonder een lokale server te draaien. Dit voorbeeld
maakt verbinding met [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
ontdekt zijn tools, en zoekt naar openbare MCP-documentatie met dezelfde
Python SDK als de [lokale client](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Parallel’s anonieme endpoint vereist geen account of API-sleutel. Gratis toegang is
rate gelimiteerd. Het draaien van dit script stuurt de zoekopdrachten, doelstelling en een
willekeurige sessie-ID naar Parallel. De dienst biedt ook `web_fetch`,
die gevraagde URL's en eventuele meegeleverde context naar Parallel stuurt. Gebruik openbare
informatie voor deze oefening; zie de [voorwaarden](https://parallel.ai/customer-terms)
en [privacybeleid](https://parallel.ai/privacy-policy).

Met Python 3.10 of nieuwer en een geactiveerde virtuele omgeving, installeer de SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Sla dit op als `hosted_search.py` en voer uit met `python hosted_search.py`:

```python
import asyncio
from uuid import uuid4

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main() -> None:
    session_id = str(uuid4())
    async with streamablehttp_client("https://search.parallel.ai/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            result = await session.call_tool(
                "web_search",
                {
                    "objective": "Find the official MCP Streamable HTTP documentation",
                    "search_queries": ["MCP Streamable HTTP documentation"],
                    "session_id": session_id,
                },
            )
            if result.isError:
                raise RuntimeError(f"Search tool failed: {result.content}")
            for block in result.content:
                if block.type == "text":
                    print(block.text)


async def run() -> None:
    await asyncio.wait_for(main(), timeout=60)


if __name__ == "__main__":
    asyncio.run(run())
```

Verwacht dat discovery `web_search` en `web_fetch` bevat, gevolgd door een zoek
response met bron-URL's en fragmenten. Resultaten kunnen variëren of leeg zijn.
Het script controleert `isError` omdat een tool kan falen zelfs als de HTTP-aanvraag
slaagt. Als de toegang rate gelimiteerd is, wacht dan voordat je het opnieuw probeert. Hergebruik dezelfde
`session_id` als je het script uitbreidt met gerelateerde zoek- of fetch-aanroepen.

Streamable HTTP staat zowel JSON als SSE responses toe; deze server kan een
compleet JSON resultaat teruggeven zonder voortgangsnotificaties. De SDK regelt het
transport. Ga verder met het lokale voorbeeld hieronder om meer te leren over notificaties.
Dit optionele script doet één expliciete zoekopdracht en sluit de verbinding wanneer
het klaar is. Als je deze tools later via een agent exposeert, kan de agent
ze aanroepen tijdens zijn werk; behandel opgehaalde webteksten als onbetrouwbare data.

## Wat is een Notificatie?

We zeiden "Notificatie", wat betekent dat in de context van MCP?

Een notificatie is een JSON-RPC bericht dat geen `id` heeft en geen
antwoord ontvangt. MCP gebruikt notificaties voor voortgang, annulering en
andere eenrichtingsgebeurtenissen.

In MCP `2025-11-25` stuurt een client `notifications/initialized` na de
initialisatie-handshake. MCP `2026-07-28` heeft geen initialisatie-handshake, dus
is deze notificatie legacy-gedrag.

Een notificatie ziet er zo uit als JSON-bericht:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Logging is één feature die notificaties gebruikt; notificaties zelf zijn een
algemeen JSON-RPC berichttype.

> **Afgeschaft in MCP `2026-07-28`:** de Logging feature blijft beschikbaar
> voor compatibiliteit maar komt mogelijk te vervallen in de eerste specificatie-
> herziening uitgebracht op of na 28 juli 2027. Nieuwe implementaties dienen
> `stderr` te gebruiken met stdio of OpenTelemetry voor gestructureerde observatie.

Voor een legacy `2025-11-25` implementatie, zet de server Logging
functie als volgt aan:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Afhankelijk van de gebruikte SDK is logging mogelijk standaard ingeschakeld, of moet je het expliciet aanzetten in je serverconfiguratie.

Er bestaan verschillende soorten notificaties:

| Niveau     | Beschrijving                 | Voorbeeld Gebruik              |
|-----------|-----------------------------|-------------------------------|
| debug     | Gedetailleerde debug informatie | Functie binnenkomst/vertrek  |
| info      | Algemene informatieve berichten | Voortgangsupdates operatie   |
| notice    | Normale maar significante gebeurtenissen | Configuratie wijzigingen     |
| warning   | Waarschuwingscondities       | Gebruik van verouderde feature |
| error     | Foutcondities               | Foutmeldingen operatie         |
| critical  | Kritieke condities          | Falen systeemcomponent         |
| alert     | Directe actie vereist       | Gegevenscorruptie gedetecteerd |
| emergency | Systeem ontoegankelijk      | Volledig systeemfaal           |

## Notificaties implementeren in MCP

Om notificaties te implementeren in MCP, moet je zowel server- als clientzijde opzetten om realtime updates te verwerken. Dit stelt je applicatie in staat directe feedback aan gebruikers te geven tijdens langdurige operaties.

### Serverzijde: Notificaties verzenden

Laten we beginnen met de serverzijde. In MCP definieer je tools die notificaties kunnen sturen tijdens het verwerken van verzoeken. De server gebruikt het context-object (meestal `ctx`) om berichten naar de client te sturen.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

In het voorgaande voorbeeld stuurt de `process_files` tool drie notificaties naar de client terwijl hij elk bestand verwerkt. De `ctx.info()` methode wordt gebruikt om informatieve berichten te verzenden.

Daarnaast, om notificaties mogelijk te maken, zorg dat je server een streaming transport gebruikt (zoals `streamable-http`) en dat je client een message handler implementeert om notificaties te verwerken. Zo stel je de server in om het `streamable-http` transport te gebruiken:

```python
mcp.run(transport="streamable-http")
```

#### .NET

```csharp
[Tool("A tool that sends progress notifications")]
public async Task<TextContent> ProcessFiles(string message, ToolContext ctx)
{
    await ctx.Info("Processing file 1/3...");
    await ctx.Info("Processing file 2/3...");
    await ctx.Info("Processing file 3/3...");
    return new TextContent
    {
        Type = "text",
        Text = $"Done: {message}"
    };
}
```

In dit .NET voorbeeld is de `ProcessFiles` tool voorzien van het `Tool` attribuut en stuurt drie notificaties naar de client terwijl ieder bestand verwerkt wordt. De `ctx.Info()` methode wordt gebruikt voor informatieve berichten.

Om notificaties in je .NET MCP-server mogelijk te maken, zorg dat je een streaming transport gebruikt:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Clientzijde: Notificaties ontvangen

De client moet een message handler implementeren om notificaties te verwerken en te tonen zodra ze binnenkomen.

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)

async with ClientSession(
   read_stream, 
   write_stream,
   logging_callback=logging_collector,
   message_handler=message_handler,
) as session:
```

In de voorafgaande code controleert de functie `message_handler` of het inkomende bericht een notificatie is. Als dat zo is, print het de notificatie; anders verwerkt het het als een regulier serverbericht. Merk ook op hoe de `ClientSession` wordt geïnitialiseerd met de `message_handler` om inkomende notificaties af te handelen.

#### .NET

```csharp
// Define a message handler
void MessageHandler(IJsonRpcMessage message)
{
    if (message is ServerNotification notification)
    {
        Console.WriteLine($"NOTIFICATION: {notification}");
    }
    else
    {
        Console.WriteLine($"SERVER MESSAGE: {message}");
    }
}

// Create and use a client session with the message handler
var clientOptions = new ClientSessionOptions
{
    MessageHandler = MessageHandler,
    LoggingCallback = (level, message) => Console.WriteLine($"[{level}] {message}")
};

using var client = new ClientSession(readStream, writeStream, clientOptions);
await client.InitializeAsync();

// Now the client will process notifications through the MessageHandler
```

In dit .NET-voorbeeld controleert de functie `MessageHandler` of het inkomende bericht een notificatie is. Als dat zo is, print het de notificatie; anders verwerkt het het als een regulier serverbericht. De `ClientSession` wordt geïnitialiseerd met de berichtverwerker via de `ClientSessionOptions`.

Om notificaties mogelijk te maken, zorg ervoor dat je server een streamingtransport gebruikt (zoals `streamable-http`) en dat je client een berichtverwerker implementeert om notificaties te verwerken.

## Voortgangsnotificaties & Scenario's

Deze sectie legt het concept van voortgangsnotificaties in MCP uit, waarom ze belangrijk zijn en hoe je ze implementeert met Streamable HTTP. Ook vind je een praktische opdracht om je begrip te versterken.

Voortgangsnotificaties zijn realtime berichten die door de server naar de client worden gestuurd tijdens langdurige bewerkingen. In plaats van te wachten tot het hele proces is voltooid, houdt de server de client op de hoogte van de huidige status. Dit verbetert de transparantie, gebruikerservaring en maakt debugging gemakkelijker.

**Voorbeeld:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Waarom Voortgangsnotificaties Gebruiken?

Voortgangsnotificaties zijn essentieel om verschillende redenen:

- **Betere gebruikerservaring:** Gebruikers zien updates terwijl het werk vordert, niet alleen aan het einde.
- **Realtime feedback:** Clients kunnen voortgangsbalken of logboeken weergeven, waardoor de app responsiever aanvoelt.
- **Gemakkelijkere debugging en monitoring:** Ontwikkelaars en gebruikers kunnen zien waar een proces traag is of vastloopt.

### Hoe Voortgangsnotificaties Implementeren

Zo kun je voortgangsnotificaties in MCP implementeren:

- **Op de server:** Gebruik `ctx.info()` of `ctx.log()` om notificaties te sturen zodra elk item is verwerkt. Dit stuurt een bericht naar de client voordat het hoofdresultaat gereed is.
- **Op de client:** Implementeer een berichtverwerker die notificaties beluistert en weergeeft zodra ze aankomen. Deze verwerker onderscheidt tussen notificaties en het eindresultaat.

**Servervoorbeeld:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Clientvoorbeeld:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Beveiligingsoverwegingen

Beveiliging moet een topprioriteit zijn bij het implementeren van elke server, vooral bij het gebruik van HTTP-gebaseerde transports zoals Streamable HTTP in MCP.

Bij het implementeren van MCP-servers met HTTP-gebaseerde transports wordt beveiliging een cruciale zorg die aandacht vereist voor meerdere aanvalsvectoren en beschermingsmechanismen.

### Overzicht

Beveiliging is cruciaal bij het blootstellen van MCP-servers via HTTP. Streamable HTTP introduceert nieuwe aanvalsvectoren en vereist zorgvuldige configuratie.

Hier zijn enkele belangrijke beveiligingsoverwegingen:

- **Validatie van Origin-header**: Valideer altijd de `Origin`-header om DNS-rebinding-aanvallen te voorkomen.
- **Binding aan localhost**: Voor lokale ontwikkeling, bind servers aan `localhost` om blootstelling aan het openbare internet te vermijden.
- **Authenticatie**: Implementeer authenticatie (bijv. API-sleutels, OAuth) voor productie-implementaties.
- **CORS**: Configureer Cross-Origin Resource Sharing (CORS)-beleid om toegang te beperken.
- **HTTPS**: Gebruik HTTPS in productie om verkeer te versleutelen.

### Best Practices

Daarnaast hier enkele best practices voor het implementeren van beveiliging in je MCP-streamingserver:

- Vertrouw nooit op binnenkomende verzoeken zonder validatie.
- Log en monitor alle toegang en fouten.
- Werk afhankelijkheden regelmatig bij om beveiligingslekken te dichten.

### Uitdagingen

Je zult enkele uitdagingen tegenkomen bij het implementeren van beveiliging in MCP-streamingservers:

- Het balanceren van beveiliging met ontwikkelgemak
- Het waarborgen van compatibiliteit met diverse clientomgevingen


## Upgraden van SSE naar Streamable HTTP

Voor applicaties die momenteel Server-Sent Events (SSE) gebruiken, biedt migratie naar Streamable HTTP verbeterde mogelijkheden en betere duurzaamheid op lange termijn voor je MCP-implementaties.

### Waarom upgraden?

Er zijn twee overtuigende redenen om te upgraden van SSE naar Streamable HTTP:

- Streamable HTTP biedt betere schaalbaarheid, compatibiliteit en rijkere notificatie-ondersteuning dan SSE.
- Het is het aanbevolen transport voor nieuwe MCP-applicaties.

### Migratiestappen

Zo kun je migreren van SSE naar Streamable HTTP in je MCP-applicaties:

- **Werk servercode bij** om `transport="streamable-http"` in `mcp.run()` te gebruiken.
- **Werk clientcode bij** om `streamablehttp_client` in plaats van SSE-client te gebruiken.
- **Implementeer een berichtverwerker** in de client om notificaties te verwerken.
- **Test op compatibiliteit** met bestaande tools en workflows.

### Compatibiliteit behouden

Het wordt aanbevolen om compatibiliteit met bestaande SSE-clients te behouden tijdens het migratieproces. Hier zijn enkele strategieën:

- Je kunt zowel SSE als Streamable HTTP ondersteunen door beide transports via verschillende eindpunten aan te bieden.
- Migreer clients geleidelijk naar het nieuwe transport.

### Uitdagingen

Zorg dat je de volgende uitdagingen adresseert tijdens de migratie:

- Zorgen dat alle clients worden bijgewerkt
- Omgaan met verschillen in notificatie-levering

### Opdracht: Bouw je eigen streaming MCP-app

**Scenario:**
Bouw een MCP-server en client waarbij de server een lijst van items verwerkt (bijv. bestanden of documenten) en voor elk verwerkt item een notificatie verzendt. De client moet elke notificatie weergeven zodra die binnenkomt.

**Stappen:**

1. Implementeer een servertool die een lijst verwerkt en voor elk item notificaties verstuurt.
2. Implementeer een client met een berichtverwerker die notificaties in realtime weergeeft.
3. Test je implementatie door zowel server als client te draaien en de notificaties te observeren.

[Oplossing](./solution/README.md)

## Verder lezen & Wat Nu?

Om je reis met MCP-streaming voort te zetten en je kennis uit te breiden, biedt deze sectie aanvullende bronnen en voorgestelde volgende stappen om geavanceerdere applicaties te bouwen.

### Verder lezen

- [Microsoft: Introductie tot HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Wat nu?

- Probeer geavanceerdere MCP-tools te bouwen die streaming gebruiken voor realtime analytics, chat of collaboratieve bewerking.
- Verken het integreren van MCP-streaming met frontend-frameworks (React, Vue, enz.) voor live UI-updates.
- Volgende: [Using Microsoft Foundry Toolkit for Visual Studio Code](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->