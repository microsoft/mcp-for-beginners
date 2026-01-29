# HTTPS Streaming met Model Context Protocol (MCP)

Dit hoofdstuk biedt een uitgebreide handleiding voor het implementeren van veilige, schaalbare en realtime streaming met het Model Context Protocol (MCP) via HTTPS. Het behandelt de motivatie voor streaming, de beschikbare transportmechanismen, hoe streambare HTTP in MCP te implementeren, beveiligingsrichtlijnen, migratie van SSE en praktische tips voor het bouwen van je eigen streaming MCP-toepassingen.

## Transportmechanismen en Streaming in MCP

In deze sectie worden de verschillende transportmechanismen in MCP besproken en hun rol in het mogelijk maken van realtime communicatie tussen clients en servers.

### Wat is een transportmechanisme?

Een transportmechanisme definieert hoe gegevens worden uitgewisseld tussen de client en de server. MCP ondersteunt meerdere transporttypen om aan verschillende omgevingen en vereisten te voldoen:

- **stdio**: Standaard invoer/uitvoer, geschikt voor lokale en CLI-gebaseerde tools. Eenvoudig, maar niet geschikt voor web of cloud.
- **SSE (Server-Sent Events)**: Hiermee kunnen servers realtime updates naar clients pushen via HTTP. Geschikt voor web-interfaces, maar beperkt in schaalbaarheid en flexibiliteit.
- **Streambare HTTP**: Modern HTTP-gebaseerd streamingtransport, dat meldingen ondersteunt en beter schaalbaar is. Aanbevolen voor de meeste productie- en cloudscenario's.

### Vergelijkingstabel

Bekijk de onderstaande vergelijkingstabel om de verschillen tussen deze transportmechanismen te begrijpen:

| Transport         | Realtime Updates | Streaming | Schaalbaarheid | Gebruiksscenario         |
|-------------------|------------------|-----------|----------------|--------------------------|
| stdio             | Nee              | Nee       | Laag           | Lokale CLI-tools         |
| SSE               | Ja               | Ja        | Gemiddeld      | Web, realtime updates    |
| Streambare HTTP   | Ja               | Ja        | Hoog           | Cloud, multi-client      |

> **Tip:** Het kiezen van het juiste transport heeft invloed op prestaties, schaalbaarheid en gebruikerservaring. **Streambare HTTP** wordt aanbevolen voor moderne, schaalbare en cloud-ready toepassingen.

Let op de transporten stdio en SSE die in de vorige hoofdstukken zijn besproken en hoe streambare HTTP het transport is dat in dit hoofdstuk wordt behandeld.

## Streaming: Concepten en Motivatie

Het begrijpen van de fundamentele concepten en motivaties achter streaming is essentieel voor het implementeren van effectieve realtime communicatiesystemen.

**Streaming** is een techniek in netwerkprogrammering waarmee gegevens in kleine, beheersbare stukjes of als een reeks gebeurtenissen kunnen worden verzonden en ontvangen, in plaats van te wachten tot een volledige respons gereed is. Dit is vooral nuttig voor:

- Grote bestanden of datasets.
- Realtime updates (bijv. chat, voortgangsbalken).
- Langdurige berekeningen waarbij je de gebruiker op de hoogte wilt houden.

Hier is wat je op hoog niveau moet weten over streaming:

- Gegevens worden progressief geleverd, niet alles in één keer.
- De client kan gegevens verwerken zodra deze binnenkomen.
- Vermindert waargenomen latentie en verbetert de gebruikerservaring.

### Waarom streaming gebruiken?

De redenen om streaming te gebruiken zijn de volgende:

- Gebruikers krijgen direct feedback, niet pas aan het einde.
- Maakt realtime toepassingen en responsieve interfaces mogelijk.
- Efficiënter gebruik van netwerk- en computerbronnen.

### Eenvoudig voorbeeld: HTTP Streaming Server & Client

Hier is een eenvoudig voorbeeld van hoe streaming kan worden geïmplementeerd:

#### Python

**Server (Python, met FastAPI en StreamingResponse):**

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

Dit voorbeeld toont een server die een reeks berichten naar de client stuurt zodra ze beschikbaar zijn, in plaats van te wachten tot alle berichten gereed zijn.

**Hoe het werkt:**

- De server levert elk bericht zodra het gereed is.
- De client ontvangt en verwerkt elk stukje zodra het binnenkomt.

**Vereisten:**

- De server moet een streamingrespons gebruiken (bijv. `StreamingResponse` in FastAPI).
- De client moet de respons als een stream verwerken (`stream=True` in requests).
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

**Java Implementatienotities:**

- Gebruikt Spring Boot's reactieve stack met `Flux` voor streaming.
- `ServerSentEvent` biedt gestructureerde eventstreaming met evenementtypen.
- `WebClient` met `bodyToFlux()` maakt reactieve streamingconsumptie mogelijk.
- `delayElements()` simuleert verwerkingstijd tussen gebeurtenissen.
- Gebeurtenissen kunnen typen hebben (`info`, `result`) voor betere clientverwerking.

### Vergelijking: Klassieke Streaming vs MCP Streaming

De verschillen tussen hoe streaming werkt op een "klassieke" manier versus hoe het werkt in MCP kunnen als volgt worden weergegeven:

| Kenmerk              | Klassieke HTTP Streaming       | MCP Streaming (Meldingen)         |
|----------------------|-------------------------------|-----------------------------------|
| Hoofdrespons         | In stukken                    | Enkel, aan het einde              |
| Voortgangsupdates    | Verzonden als datastukken      | Verzonden als meldingen           |
| Clientvereisten      | Moet stream verwerken          | Moet berichtverwerker implementeren |
| Gebruiksscenario     | Grote bestanden, AI-tokenstreams | Voortgang, logs, realtime feedback |

### Waargenomen Belangrijke Verschillen

Hier zijn enkele belangrijke verschillen:

- **Communicatiepatroon:**
  - Klassieke HTTP-streaming: Gebruikt eenvoudige chunked transfer encoding om gegevens in stukken te verzenden.
  - MCP-streaming: Gebruikt een gestructureerd meldingssysteem met JSON-RPC-protocol.

- **Berichtformaat:**
  - Klassieke HTTP: Platte tekststukken met nieuwe regels.
  - MCP: Gestructureerde `LoggingMessageNotification`-objecten met metadata.

- **Clientimplementatie:**
  - Klassieke HTTP: Eenvoudige client die streamingresponsen verwerkt.
  - MCP: Meer geavanceerde client met een berichtverwerker om verschillende soorten berichten te verwerken.

- **Voortgangsupdates:**
  - Klassieke HTTP: De voortgang maakt deel uit van de hoofdresponsstream.
  - MCP: Voortgang wordt verzonden via afzonderlijke meldingsberichten terwijl de hoofdrespons aan het einde komt.

### Aanbevelingen

Er zijn enkele aanbevelingen bij het kiezen tussen het implementeren van klassieke streaming (zoals een endpoint dat hierboven is getoond met `/stream`) en streaming via MCP.

- **Voor eenvoudige streamingbehoeften:** Klassieke HTTP-streaming is eenvoudiger te implementeren en voldoende voor basisstreamingbehoeften.
- **Voor complexe, interactieve toepassingen:** MCP-streaming biedt een meer gestructureerde aanpak met rijkere metadata en scheiding tussen meldingen en eindresultaten.
- **Voor AI-toepassingen:** Het meldingssysteem van MCP is bijzonder nuttig voor langdurige AI-taken waarbij je gebruikers op de hoogte wilt houden van de voortgang.

## Streaming in MCP

Oké, je hebt enkele aanbevelingen en vergelijkingen gezien over het verschil tussen klassieke streaming en streaming in MCP. Laten we in detail bekijken hoe je streaming in MCP kunt benutten.

Het begrijpen van hoe streaming werkt binnen het MCP-framework is essentieel voor het bouwen van responsieve toepassingen die realtime feedback aan gebruikers bieden tijdens langdurige operaties.

In MCP gaat streaming niet over het verzenden van de hoofdrespons in stukken, maar over het verzenden van **meldingen** naar de client terwijl een tool een verzoek verwerkt. Deze meldingen kunnen voortgangsupdates, logs of andere gebeurtenissen bevatten.

### Hoe het werkt

Het hoofdresultaat wordt nog steeds als een enkele respons verzonden. Meldingen kunnen echter als afzonderlijke berichten tijdens de verwerking worden verzonden en de client in realtime bijwerken. De client moet in staat zijn om deze meldingen te verwerken en weer te geven.

## Wat is een melding?

We zeiden "melding", wat betekent dat in de context van MCP?

Een melding is een bericht dat van de server naar de client wordt verzonden om te informeren over voortgang, status of andere gebeurtenissen tijdens een langdurige operatie. Meldingen verbeteren transparantie en gebruikerservaring.

Bijvoorbeeld, een client moet een melding sturen zodra de initiële handshake met de server is gemaakt.

Een melding ziet er als volgt uit als een JSON-bericht:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Meldingen behoren tot een onderwerp in MCP dat wordt aangeduid als ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Om logging te laten werken, moet de server het inschakelen als functie/capaciteit zoals hieronder:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Afhankelijk van de gebruikte SDK kan logging standaard zijn ingeschakeld, of moet je het expliciet inschakelen in je serverconfiguratie.

Er zijn verschillende soorten meldingen:

| Niveau     | Beschrijving                  | Voorbeeldgebruiksscenario       |
|------------|-------------------------------|----------------------------------|
| debug      | Gedetailleerde debuginformatie | Functie-invoer/uitvoerpunten    |
| info       | Algemene informatieve berichten | Voortgangsupdates               |
| notice     | Normale maar significante gebeurtenissen | Configuratiewijzigingen       |
| warning    | Waarschuwingscondities         | Gebruik van verouderde functies |
| error      | Foutcondities                  | Mislukkingen van operaties      |
| critical   | Kritieke condities             | Falen van systeemcomponenten    |
| alert      | Onmiddellijke actie vereist    | Geconstateerde gegevenscorruptie|
| emergency  | Systeem is onbruikbaar         | Volledige systeemuitval         |

## Meldingen implementeren in MCP

Om meldingen in MCP te implementeren, moet je zowel de server- als clientzijde instellen om realtime updates te verwerken. Hierdoor kan je toepassing directe feedback geven aan gebruikers tijdens langdurige operaties.

### Serverzijde: Meldingen verzenden

Laten we beginnen met de serverzijde. In MCP definieer je tools die meldingen kunnen verzenden tijdens het verwerken van verzoeken. De server gebruikt het contextobject (meestal `ctx`) om berichten naar de client te sturen.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

In het bovenstaande voorbeeld stuurt de `process_files`-tool drie meldingen naar de client terwijl elk bestand wordt verwerkt. De methode `ctx.info()` wordt gebruikt om informatieve berichten te verzenden.

Daarnaast, om meldingen in te schakelen, zorg ervoor dat je server een streamingtransport gebruikt (zoals `streamable-http`) en je client een berichtverwerker implementeert om meldingen te verwerken. Hier is hoe je de server kunt instellen om het `streamable-http`-transport te gebruiken:

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

In dit .NET-voorbeeld is de `ProcessFiles`-tool voorzien van het `Tool`-attribuut en stuurt drie meldingen naar de client terwijl elk bestand wordt verwerkt. De methode `ctx.Info()` wordt gebruikt om informatieve berichten te verzenden.

Om meldingen in je .NET MCP-server in te schakelen, zorg ervoor dat je een streamingtransport gebruikt:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Clientzijde: Meldingen ontvangen

De client moet een berichtverwerker implementeren om meldingen te verwerken en weer te geven zodra ze binnenkomen.

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

In de bovenstaande code controleert de functie `message_handler` of het binnenkomende bericht een melding is. Als dat zo is, wordt de melding afgedrukt; anders wordt het verwerkt als een regulier serverbericht. Merk ook op hoe de `ClientSession` is geïnitialiseerd met de `message_handler` om binnenkomende meldingen te verwerken.

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

In dit .NET-voorbeeld controleert de functie `MessageHandler` of het binnenkomende bericht een melding is. Als dat zo is, wordt de melding afgedrukt; anders wordt het verwerkt als een regulier serverbericht. De `ClientSession` is geïnitialiseerd met de berichtverwerker via de `ClientSessionOptions`.

Om meldingen in te schakelen, zorg ervoor dat je server een streamingtransport gebruikt (zoals `streamable-http`) en je client een berichtverwerker implementeert om meldingen te verwerken.

## Voortgangsmeldingen & Scenario's

Deze sectie legt het concept van voortgangsmeldingen in MCP uit, waarom ze belangrijk zijn en hoe je ze kunt implementeren met Streamable HTTP. Je vindt ook een praktische opdracht om je begrip te versterken.

Voortgangsmeldingen zijn realtime berichten die van de server naar de client worden verzonden tijdens langdurige operaties. In plaats van te wachten tot het hele proces is voltooid, houdt de server de client op de hoogte van de huidige status. Dit verbetert transparantie, gebruikerservaring en maakt debugging eenvoudiger.

**Voorbeeld:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Waarom voortgangsmeldingen gebruiken?

Voortgangsmeldingen zijn om verschillende redenen essentieel:

- **Betere gebruikerservaring:** Gebruikers zien updates terwijl het werk vordert, niet pas aan het einde.
- **Realtime feedback:** Clients kunnen voortgangsbalken of logs weergeven, waardoor de app responsief aanvoelt.
- **Eenvoudiger debugging en monitoring:** Ontwikkelaars en gebruikers kunnen zien waar een proces traag of vastloopt.

### Hoe voortgangsmeldingen implementeren

Hier is hoe je voortgangsmeldingen in MCP kunt implementeren:

- **Op de server:** Gebruik `ctx.info()` of `ctx.log()` om meldingen te verzenden terwijl elk item wordt verwerkt. Dit stuurt een bericht naar de client voordat het hoofdresultaat gereed is.
- **Op de client:** Implementeer een berichtverwerker die luistert naar en meldingen weergeeft zodra ze binnenkomen. Deze verwerker maakt onderscheid tussen meldingen en het eindresultaat.

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

Bij het implementeren van MCP-servers met HTTP-gebaseerde transporten is beveiliging een cruciale zorg die aandacht vereist voor meerdere aanvalsvectoren en beschermingsmechanismen.

### Overzicht

Beveiliging is van cruciaal belang bij het blootstellen van MCP-servers via HTTP. Streamable HTTP introduceert nieuwe aanvalsvectoren en vereist zorgvuldige configuratie.

### Belangrijke punten

- **Origin-header validatie**: Valideer altijd de `Origin`-header om DNS-rebindingaanvallen te voorkomen.
- **Localhost-binding**: Voor lokale ontwikkeling, bind servers aan `localhost` om te voorkomen dat ze worden blootgesteld aan het openbare internet.
- **Authenticatie**: Implementeer authenticatie (bijv. API-sleutels, OAuth) voor productie-implementaties.
- **CORS**: Configureer Cross-Origin Resource Sharing (CORS)-beleid om toegang te beperken.
- **HTTPS**: Gebruik HTTPS in productie om verkeer te versleutelen.

### Best practices

- Vertrouw nooit inkomende verzoeken zonder validatie.
- Log en monitor alle toegang en fouten.
- Werk regelmatig afhankelijkheden bij om beveiligingslekken te dichten.

### Uitdagingen

- Balans vinden tussen beveiliging en ontwikkelgemak.
- Compatibiliteit waarborgen met verschillende clientomgevingen.

## Upgraden van SSE naar Streamable HTTP

Voor toepassingen die momenteel Server-Sent Events (SSE) gebruiken, biedt migratie naar Streamable HTTP verbeterde mogelijkheden en betere duurzaamheid op lange termijn voor je MCP-implementaties.

### Waarom upgraden?
Er zijn twee overtuigende redenen om te upgraden van SSE naar Streamable HTTP:

- Streamable HTTP biedt betere schaalbaarheid, compatibiliteit en uitgebreidere notificatieondersteuning dan SSE.
- Het is de aanbevolen transportmethode voor nieuwe MCP-toepassingen.

### Migratiestappen

Hier is hoe je kunt migreren van SSE naar Streamable HTTP in je MCP-toepassingen:

- **Werk de servercode bij** om `transport="streamable-http"` te gebruiken in `mcp.run()`.
- **Werk de clientcode bij** om `streamablehttp_client` te gebruiken in plaats van de SSE-client.
- **Implementeer een berichtverwerker** in de client om notificaties te verwerken.
- **Test op compatibiliteit** met bestaande tools en workflows.

### Compatibiliteit behouden

Het wordt aanbevolen om compatibiliteit met bestaande SSE-clients te behouden tijdens het migratieproces. Hier zijn enkele strategieën:

- Je kunt zowel SSE als Streamable HTTP ondersteunen door beide transports op verschillende eindpunten te draaien.
- Migreer clients geleidelijk naar het nieuwe transport.

### Uitdagingen

Zorg ervoor dat je de volgende uitdagingen aanpakt tijdens de migratie:

- Zorgen dat alle clients worden bijgewerkt
- Omgaan met verschillen in notificatielevering

## Overwegingen voor beveiliging

Beveiliging moet een topprioriteit zijn bij het implementeren van een server, vooral bij het gebruik van HTTP-gebaseerde transports zoals Streamable HTTP in MCP.

Bij het implementeren van MCP-servers met HTTP-gebaseerde transports wordt beveiliging een cruciale zorg die aandacht vereist voor meerdere aanvalsvectoren en beschermingsmechanismen.

### Overzicht

Beveiliging is essentieel bij het blootstellen van MCP-servers via HTTP. Streamable HTTP introduceert nieuwe aanvalsvectoren en vereist zorgvuldige configuratie.

Hier zijn enkele belangrijke beveiligingsoverwegingen:

- **Validatie van de Origin-header**: Valideer altijd de `Origin`-header om DNS-rebindingaanvallen te voorkomen.
- **Binding aan localhost**: Voor lokale ontwikkeling, bind servers aan `localhost` om te voorkomen dat ze worden blootgesteld aan het openbare internet.
- **Authenticatie**: Implementeer authenticatie (bijv. API-sleutels, OAuth) voor productieomgevingen.
- **CORS**: Configureer Cross-Origin Resource Sharing (CORS)-beleid om toegang te beperken.
- **HTTPS**: Gebruik HTTPS in productie om verkeer te versleutelen.

### Best practices

Daarnaast zijn hier enkele best practices die je kunt volgen bij het implementeren van beveiliging in je MCP-streamingserver:

- Vertrouw nooit inkomende verzoeken zonder validatie.
- Log en monitor alle toegang en fouten.
- Werk regelmatig afhankelijkheden bij om beveiligingslekken te verhelpen.

### Uitdagingen

Je zult enkele uitdagingen tegenkomen bij het implementeren van beveiliging in MCP-streamingservers:

- Het balanceren van beveiliging met gebruiksgemak tijdens ontwikkeling
- Zorgen voor compatibiliteit met verschillende clientomgevingen

### Opdracht: Bouw je eigen streaming MCP-app

**Scenario:**
Bouw een MCP-server en -client waarbij de server een lijst met items (bijv. bestanden of documenten) verwerkt en een notificatie stuurt voor elk verwerkt item. De client moet elke notificatie weergeven zodra deze binnenkomt.

**Stappen:**

1. Implementeer een servertool die een lijst verwerkt en notificaties stuurt voor elk item.
2. Implementeer een client met een berichtverwerker om notificaties in realtime weer te geven.
3. Test je implementatie door zowel de server als de client uit te voeren en observeer de notificaties.

[Oplossing](./solution/README.md)

## Verdere lectuur & Wat nu?

Om je reis met MCP-streaming voort te zetten en je kennis uit te breiden, biedt deze sectie aanvullende bronnen en voorgestelde vervolgstappen voor het bouwen van meer geavanceerde toepassingen.

### Verdere lectuur

- [Microsoft: Introductie tot HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Wat nu?

- Probeer meer geavanceerde MCP-tools te bouwen die streaming gebruiken voor realtime analytics, chat of collaboratieve bewerking.
- Verken de integratie van MCP-streaming met frontend-frameworks (React, Vue, etc.) voor live UI-updates.
- Volgende: [AI Toolkit gebruiken voor VSCode](../07-aitk/README.md)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.