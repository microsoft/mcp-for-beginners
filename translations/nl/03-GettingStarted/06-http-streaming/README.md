# HTTPS Streaming met Model Context Protocol (MCP)

Dit hoofdstuk biedt een uitgebreide handleiding voor het implementeren van veilige, schaalbare en realtime streaming met het Model Context Protocol (MCP) via HTTPS. Het behandelt de motivatie voor streaming, de beschikbare transportmechanismen, hoe streamable HTTP in MCP te implementeren, beste beveiligingspraktijken, migratie van SSE, en praktische richtlijnen voor het bouwen van je eigen streaming MCP-toepassingen.

> **Vooruitblik:** deze les beschrijft Streamable HTTP onder **MCP Specificatie 2025-11-25**, waarbij een sessie wordt opgezet tijdens `initialize` en vastgezet met een `Mcp-Session-Id` header. De release candidate van `2026-07-28` verwijdert de handshake en sessie-ID volledig, waardoor elke aanvraag zelfvoorzienend is en naar elke serverinstantie kan worden gerouteerd zonder sticky sessions. Zie [Wat verandert er in MCP: De release kandidaat van 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) voor details.

## Transportmechanismen en Streaming in MCP

Dit gedeelte onderzoekt de verschillende beschikbare transportmechanismen in MCP en hun rol bij het mogelijk maken van streamingfunctionaliteiten voor realtime communicatie tussen clients en servers.

### Wat is een transportmechanisme?

Een transportmechanisme definieert hoe data wordt uitgewisseld tussen client en server. MCP ondersteunt meerdere transporttypes om aan verschillende omgevingen en vereisten te voldoen:

- **stdio**: Standaard invoer/uitvoer, geschikt voor lokale en CLI-gebaseerde tools. Simpel maar niet geschikt voor web of cloud.
- **SSE (Server-Sent Events)**: Hiermee kunnen servers realtime updates naar clients pushen via HTTP. Goed voor web-UIs, maar beperkt in schaalbaarheid en flexibiliteit. Vanaf MCP Specificatie 2025-06-18 is het standalone SSE (Server-Sent Events) transport afgeschaft en vervangen door "Streamable HTTP" transport.
- **Streamable HTTP**: Modern HTTP-gebaseerd streaming transport, ondersteunt notificaties en betere schaalbaarheid. Aanbevolen voor de meeste productie- en cloudscenario's.

### Vergelijkingstabel

Bekijk de onderstaande vergelijkingstabel om de verschillen tussen deze transportmechanismen te begrijpen:

| Transport         | Real-time Updates | Streaming | Schaalbaarheid | Gebruiksscenario         |
|-------------------|------------------|-----------|---------------|-------------------------|
| stdio             | Nee              | Nee       | Laag          | Lokale CLI-tools        |
| SSE               | Ja               | Ja        | Gemiddeld     | Web, realtime updates   |
| Streamable HTTP   | Ja               | Ja        | Hoog          | Cloud, multi-client     |

> **Tip:** De juiste keuze van transport heeft impact op prestaties, schaalbaarheid en gebruikerservaring. **Streamable HTTP** wordt aanbevolen voor moderne, schaalbare en cloud-ready applicaties.

Let op de transports stdio en SSE die in voorgaande hoofdstukken werden getoond en hoe streaming HTTP het transport is dat in dit hoofdstuk behandeld wordt.

## Streaming: Concepten en Motivatie

Het begrijpen van de fundamentele concepten en motivaties achter streaming is essentieel voor het implementeren van effectieve realtime communicatiesystemen.

**Streaming** is een techniek in netwerkprogrammering waarmee data in kleine, beheersbare stukjes of als een reeks evenementen wordt verzonden en ontvangen, in plaats van te wachten tot een volledige respons gereed is. Dit is vooral nuttig voor:

- Grote bestanden of datasets.
- Realtime updates (bijv. chat, voortgangsbalken).
- Langlopende berekeningen waarbij je de gebruiker op de hoogte wilt houden.

Hier is wat je op hoofdlijnen moet weten over streaming:

- Data wordt geleidelijk geleverd, niet allemaal tegelijk.
- De client kan data verwerken zodra deze binnenkomt.
- Vermindert de waargenomen latentie en verbetert de gebruikerservaring.

### Waarom streaming gebruiken?

De redenen om streaming te gebruiken zijn:

- Gebruikers krijgen direct feedback, niet alleen aan het einde.
- Maakt realtime applicaties en responsieve UIs mogelijk.
- Efficiënter gebruik van netwerk- en rekencapaciteiten.

### Eenvoudig voorbeeld: HTTP Streaming Server & Client

Hier een eenvoudig voorbeeld van hoe streaming kan worden geïmplementeerd:

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

Dit voorbeeld toont een server die een reeks berichten naar de client stuurt zodra ze beschikbaar zijn, in plaats van te wachten tot alle berichten klaar zijn.

**Hoe het werkt:**

- De server levert elk bericht zodra het gereed is.
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

**Java Implementatienotities:**

- Gebruikt Spring Boot's reactieve stack met `Flux` voor streaming
- `ServerSentEvent` biedt gestructureerde event streaming met eventtypes
- `WebClient` met `bodyToFlux()` maakt reactieve streamingconsumptie mogelijk
- `delayElements()` simuleert verwerkingstijd tussen events
- Events kunnen types hebben (`info`, `result`) voor betere clientafhandeling

### Vergelijking: Klassieke Streaming vs MCP Streaming

De verschillen tussen klassieke streaming en streaming in MCP kunnen als volgt worden weergegeven:

| Kenmerk               | Klassieke HTTP Streaming       | MCP Streaming (Notificaties)      |
|-----------------------|-------------------------------|----------------------------------|
| Hoofdresponse          | Gefragmenteerd (chunked)       | Enkelvoudig, aan het einde        |
| Voortgangsupdates     | Verstuurd als datastukken      | Verstuurd als notificaties        |
| Clientvereisten       | Moet stream verwerken          | Moet een berichthandler implementeren |
| Gebruiksscenario      | Grote bestanden, AI token streams | Voortgang, logs, realtime feedback |

### Belangrijkste Verschillen Geobserveerd

Daarnaast zijn hier enkele belangrijke verschillen:

- **Communicatiepatroon:**
  - Klassieke HTTP streaming: Gebruikt eenvoudige chunked transfer encoding om data in stukjes te verzenden
  - MCP streaming: Gebruikt een gestructureerd notificatiesysteem met JSON-RPC protocol

- **Berichtformaat:**
  - Klassieke HTTP: Platte tekst chunks met nieuwe regels
  - MCP: Gestructureerde LoggingMessageNotification-objecten met metadata

- **Clientimplementatie:**
  - Klassieke HTTP: Simpele client die streaming responses verwerkt
  - MCP: Meer geavanceerde client met een berichthandler om verschillende typen berichten te verwerken

- **Voortgangsupdates:**
  - Klassieke HTTP: Voortgang maakt deel uit van de hoofdresponsestream
  - MCP: Voortgang wordt via aparte notificatieberichten gestuurd terwijl de hoofdrespons aan het eind komt

### Aanbevelingen

Er zijn enkele aanbevelingen bij het kiezen tussen klassieke streaming (zoals het endpoint dat je hierboven hebt gezien met `/stream`) en streaming via MCP.

- **Voor eenvoudige streamingbehoeften:** Klassieke HTTP streaming is eenvoudiger te implementeren en voldoende voor basisbehoeften.

- **Voor complexe, interactieve applicaties:** MCP streaming biedt een meer gestructureerde aanpak met rijkere metadata en scheiding tussen notificaties en definitieve resultaten.

- **Voor AI-toepassingen:** Het notificatiesysteem van MCP is bijzonder nuttig voor langlopende AI taken waarin je gebruikers op de hoogte wilt houden van voortgang.

## Streaming in MCP

Oké, je hebt tot nu toe enkele aanbevelingen en vergelijkingen gezien over het verschil tussen klassieke streaming en streaming in MCP. Laten we nu in detail bekijken hoe je streaming precies kunt benutten in MCP.

Het begrijpen van hoe streaming werkt binnen het MCP-framework is essentieel voor het bouwen van responsieve applicaties die realtime feedback geven aan gebruikers tijdens langlopende bewerkingen.

In MCP gaat streaming niet over het verzenden van de hoofdresponse in stukjes, maar over het sturen van **notificaties** naar de client terwijl een tool een verzoek verwerkt. Deze notificaties kunnen voortgangsupdates, logs of andere gebeurtenissen omvatten.

### Hoe het werkt

Het hoofdzakelijke resultaat wordt nog steeds als één response verzonden. Echter, notificaties kunnen als afzonderlijke berichten worden verstuurd tijdens de verwerking en zo de client realtime bijwerken. De client moet deze notificaties kunnen afhandelen en weergeven.

## Wat is een notificatie?

We zeiden "notificatie", wat betekent dat in de context van MCP?

Een notificatie is een bericht dat van de server naar de client wordt gestuurd om te informeren over voortgang, status of andere gebeurtenissen tijdens een langlopende operatie. Notificaties verbeteren transparantie en gebruikerservaring.

Bijvoorbeeld, een client dient een notificatie te sturen zodra de initiële handshake met de server is voltooid.

Een notificatie ziet er zo uit als een JSON-bericht:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notificaties behoren tot een onderwerp in MCP dat ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) wordt genoemd.

> **Afmeldingsbericht:** de `2026-07-28` MCP specificatie release kandidaat markeert de Logging primitief als verouderd ten gunste van `stderr` voor stdio transports en OpenTelemetry voor gestructureerde observability. Logging blijft werken in `2025-11-25` en minstens een jaar na eventuele formele afmelding. Zie [Wat verandert er in MCP: De release kandidaat van 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Om logging te laten werken moet de server het als feature/capability inschakelen zoals dit:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Afhankelijk van de gebruikte SDK kan logging standaard zijn ingeschakeld, of moet je het expliciet inschakelen in je serverconfiguratie.

Er zijn verschillende soorten notificaties:

| Niveau     | Beschrijving                   | Voorbeeld Gebruiksscenario      |
|-----------|-------------------------------|--------------------------------|
| debug     | Gedetailleerde debuginformatie | Functie aanroep/exitpunten       |
| info      | Algemene informatieve berichten | Voortgangsupdates van operatie  |
| notice    | Normale maar belangrijke gebeurtenissen | Configuratie wijzigingen    |
| warning   | Waarschuwingscondities         | Gebruik van verouderde functies  |
| error     | Foutcondities                 | Operationele fouten             |
| critical  | Kritieke condities             | Falen van systeemcomponenten     |
| alert     | Directe actie vereist           | Geconstateerde datacorruptie    |
| emergency | Systeem is onbruikbaar          | Volledig systeemfalen           |

## Implementatie van notificaties in MCP

Om notificaties in MCP te implementeren moet je zowel de server- als clientzijde inrichten om realtime updates te verwerken. Dit stelt je applicatie in staat om gebruikers direct feedback te geven tijdens langlopende operaties.

### Serverzijde: Notificaties verzenden

Laten we beginnen met de serverzijde. In MCP definieer je tools die notificaties kunnen verzenden tijdens de verwerking van verzoeken. De server gebruikt het context-object (meestal `ctx`) om berichten naar de client te sturen.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

In het voorgaande voorbeeld stuurt de `process_files` tool drie notificaties naar de client terwijl elk bestand wordt verwerkt. De `ctx.info()` methode wordt gebruikt om informatieve berichten te versturen.

Daarnaast, om notificaties mogelijk te maken, moet je server een streaming transport gebruiken (zoals `streamable-http`) en moet de client een berichthandler implementeren om notificaties te verwerken. Hieronder vind je hoe je de server kunt instellen om het `streamable-http` transport te gebruiken:

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

In dit .NET voorbeeld is de `ProcessFiles` tool voorzien van de `Tool` attribuut en stuurt drie notificaties naar de client tijdens het verwerken van elk bestand. De `ctx.Info()` methode wordt gebruikt om informatieve berichten te sturen.

Om notificaties in je .NET MCP server in te schakelen, zorg dat je een streaming transport gebruikt:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Clientzijde: Notificaties ontvangen

De client moet een berichthandler implementeren om notificaties te verwerken en weer te geven zodra ze binnenkomen.

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

In de bovenstaande code controleert de `message_handler` functie of het binnenkomende bericht een notificatie is. Zo ja, dan print het de notificatie; anders wordt het als een regulier serverbericht verwerkt. Let ook op hoe `ClientSession` wordt geïnitialiseerd met de `message_handler` om binnenkomende notificaties te verwerken.

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

In dit .NET voorbeeld controleert de `MessageHandler` functie of het binnenkomende bericht een notificatie is. Zo ja, print het de notificatie; anders verwerkt het het als een regulier serverbericht. `ClientSession` wordt geïnitialiseerd met de berichthandler via de `ClientSessionOptions`.

Om notificaties mogelijk te maken, zorg dat je server een streaming transport gebruikt (zoals `streamable-http`) en dat je client een berichthandler implementeert om notificaties te verwerken.

## Voortgangsnotificaties & Scenario's

Dit gedeelte legt het concept van voortgangsnotificaties in MCP uit, waarom ze belangrijk zijn en hoe je ze kunt implementeren met Streamable HTTP. Je vindt er ook een praktische opdracht om je begrip te versterken.

Voortgangsnotificaties zijn realtime berichten die van de server naar de client worden gestuurd tijdens langlopende operaties. In plaats van te wachten tot het hele proces klaar is, houdt de server de client op de hoogte van de huidige status. Dit verbetert transparantie, gebruikerservaring en maakt debugging eenvoudiger.

**Voorbeeld:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Waarom voortgangsnotificaties gebruiken?

Voortgangsnotificaties zijn om verschillende redenen essentieel:

- **Betere gebruikerservaring:** Gebruikers zien updates terwijl het werk vordert, niet alleen aan het einde.
- **Realtime feedback:** Clients kunnen voortgangsbalken of logs weergeven, waardoor de app responsief aanvoelt.
- **Makkelijkere debugging en monitoring:** Ontwikkelaars en gebruikers kunnen zien waar een proces traag is of vastloopt.

### Hoe voortgangsnotificaties implementeren

Zo kun je voortgangsnotificaties in MCP implementeren:

- **Aan de serverzijde:** Gebruik `ctx.info()` of `ctx.log()` om notificaties te sturen zodra elk item wordt verwerkt. Dit stuurt een bericht naar de client voordat het hoofduitkomst beschikbaar is.
- **Aan de clientzijde:** Implementeer een berichthandler die luistert naar en notificaties weergeeft zodra ze binnenkomen. Deze handler maakt onderscheid tussen notificaties en het eindresultaat.

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

Bij het implementeren van MCP-servers met HTTP-gebaseerde transports wordt beveiliging een belangrijke zorg die zorgvuldige aandacht vereist voor meerdere aanvalsvectoren en beschermingsmechanismen.

### Overzicht

Beveiliging is cruciaal bij het blootstellen van MCP-servers via HTTP. Streamable HTTP introduceert nieuwe aanvalsvlakken en vereist zorgvuldige configuratie.

Hier zijn enkele belangrijke beveiligingsoverwegingen:

- **Validatie van Origin-header**: Valideer altijd de `Origin`-header om DNS-rebinding-aanvallen te voorkomen.
- **Localhost-binding**: Voor lokale ontwikkeling, bind servers aan `localhost` om blootstelling aan het publieke internet te vermijden.
- **Authenticatie**: Implementeer authenticatie (bijv. API-sleutels, OAuth) voor productieomgevingen.
- **CORS**: Configureer Cross-Origin Resource Sharing (CORS)-beleid om toegang te beperken.
- **HTTPS**: Gebruik HTTPS in productie om het verkeer te versleutelen.

### Best Practices

Daarnaast zijn hier enkele best practices om te volgen bij het implementeren van beveiliging in uw MCP-streamingserver:

- Vertrouw nooit op binnenkomende verzoeken zonder validatie.
- Log en monitor alle toegang en fouten.
- Werk regelmatig afhankelijkheden bij om beveiligingskwetsbaarheden te verhelpen.

### Uitdagingen

U zult enkele uitdagingen tegenkomen bij het implementeren van beveiliging in MCP-streamingservers:

- Het balanceren van beveiliging met ontwikkelingsgemak
- Het garanderen van compatibiliteit met verschillende clientomgevingen


## Upgraden van SSE naar Streamable HTTP

Voor toepassingen die momenteel Server-Sent Events (SSE) gebruiken, biedt migratie naar Streamable HTTP verbeterde mogelijkheden en betere duurzaamheid op lange termijn voor uw MCP-implementaties.

### Waarom upgraden?

Er zijn twee overtuigende redenen om te upgraden van SSE naar Streamable HTTP:

- Streamable HTTP biedt betere schaalbaarheid, compatibiliteit en rijkere meldingsondersteuning dan SSE.
- Het is de aanbevolen transportmethode voor nieuwe MCP-toepassingen.

### Migratiestappen

Zo kunt u migreren van SSE naar Streamable HTTP in uw MCP-toepassingen:

- **Werk servercode bij** om `transport="streamable-http"` te gebruiken in `mcp.run()`.
- **Werk clientcode bij** om `streamablehttp_client` te gebruiken in plaats van de SSE-client.
- **Implementeer een berichtafhandelaar** in de client om meldingen te verwerken.
- **Test op compatibiliteit** met bestaande tools en workflows.

### Compatibiliteit behouden

Het wordt aanbevolen compatibiliteit te behouden met bestaande SSE-clients gedurende het migratieproces. Hier enkele strategieën:

- U kunt zowel SSE als Streamable HTTP ondersteunen door beide transports op verschillende eindpunten te draaien.
- Migreer clients geleidelijk naar de nieuwe transportmethode.

### Uitdagingen

Zorg ervoor dat u de volgende uitdagingen aanpakt tijdens de migratie:

- Garandeer dat alle clients worden bijgewerkt
- Omgaan met verschillen in meldingslevering

### Opdracht: Bouw je eigen streaming MCP-app

**Scenario:**
Bouw een MCP-server en client waarbij de server een lijst met items (bijv. bestanden of documenten) verwerkt en voor elk verwerkt item een melding verzendt. De client moet elke melding weergeven zodra deze binnenkomt.

**Stappen:**

1. Implementeer een server tool die een lijst verwerkt en meldingen verzendt voor elk item.
2. Implementeer een client met een berichtafhandelaar om meldingen in realtime weer te geven.
3. Test uw implementatie door zowel server als client te draaien en observeer de meldingen.

[Oplossing](./solution/README.md)

## Verder lezen & Wat nu?

Om uw reis met MCP-streaming voort te zetten en uw kennis uit te breiden, biedt deze sectie aanvullende bronnen en voorgestelde volgende stappen voor het bouwen van meer geavanceerde toepassingen.

### Verder lezen

- [Microsoft: Introductie tot HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Wat nu?

- Probeer meer geavanceerde MCP-tools te bouwen die streaming gebruiken voor realtime analytics, chat of collaboratieve bewerking.
- Verken het integreren van MCP-streaming met frontend-frameworks (React, Vue, etc.) voor live UI-updates.
- Volgende: [Het gebruiken van AI Toolkit voor VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->