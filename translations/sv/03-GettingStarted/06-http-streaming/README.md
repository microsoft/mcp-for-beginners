# HTTPS Streaming med Model Context Protocol (MCP)

Detta kapitel ger en omfattande guide för att implementera säker, skalbar och realtidsstreaming med Model Context Protocol (MCP) via HTTPS. Det täcker motivationen för streaming, de tillgängliga transportmekanismerna, hur man implementerar streambar HTTP i MCP, säkerhetsbästa praxis, migration från SSE och praktisk vägledning för att bygga dina egna streaming-MCP-applikationer.

> **Framåt:** denna lektion beskriver Streambar HTTP under **MCP-specifikation 2025-11-25**, där en session etableras under `initialize` och fixeras med en `Mcp-Session-Id`-header. Releasekandidaten `2026-07-28` tar bort handskakningen och sessions-ID helt, vilket gör varje begäran självständig och routbar till vilken serverinstans som helst utan klibbiga sessioner. Se [Vad som ändras i MCP: Release-kandidat 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) för detaljer.

## Transportmekanismer och streaming i MCP

Denna sektion utforskar de olika tillgängliga transportmekanismerna i MCP och deras roll i att möjliggöra streamingfunktioner för realtidskommunikation mellan klienter och servrar.

### Vad är en transportmekanism?

En transportmekanism definierar hur data utbyts mellan klienten och servern. MCP stödjer flera transporttyper för att passa olika miljöer och krav:

- **stdio**: Standard in-/utgång, lämplig för lokala och CLI-baserade verktyg. Enkel men inte lämplig för webben eller molnet.
- **SSE (Server-Sent Events)**: Tillåter servrar att skicka realtidsuppdateringar till klienter över HTTP. Bra för webbgränssnitt, men begränsad i skalbarhet och flexibilitet. Från och med MCP-specifikation 2025-06-18 har den fristående SSE-transporten avvecklats och ersatts av "Streambar HTTP"-transport.
- **Streambar HTTP**: Modern HTTP-baserad streamingtransport som stöder notifikationer och bättre skalbarhet. Rekommenderas för de flesta produktions- och molnscenarier.

### Jämförelsetabell

Ta en titt på jämförelsetabellen nedan för att förstå skillnaderna mellan dessa transportmekanismer:

| Transport         | Realtidsuppdateringar | Streaming | Skalbarhet | Användningsfall             |
|-------------------|-----------------------|-----------|------------|----------------------------|
| stdio             | Nej                   | Nej       | Låg        | Lokala CLI-verktyg         |
| SSE               | Ja                    | Ja        | Medel      | Webb, realtidsuppdateringar|
| Streambar HTTP    | Ja                    | Ja        | Hög        | Moln, multi-klient         |

> **Tips:** Att välja rätt transport påverkar prestanda, skalbarhet och användarupplevelse. **Streambar HTTP** rekommenderas för moderna, skalbara och molnberedda applikationer.

Notera transporterna stdio och SSE som visades i tidigare kapitel och hur streambar HTTP är transporten som behandlas i detta kapitel.

## Streaming: Koncept och motivation

Att förstå de grundläggande koncepten och motivationerna bakom streaming är avgörande för att implementera effektiva realtidskommunikationssystem.

**Streaming** är en teknik inom nätverksprogrammering som tillåter att data skickas och tas emot i små, hanterbara bitar eller som en sekvens av händelser istället för att vänta på att hela svaret ska vara klart. Detta är särskilt användbart för:

- Stora filer eller dataset.
- Realtidsuppdateringar (t.ex. chatt, progressbarer).
- Långvariga beräkningar där du vill hålla användaren informerad.

Här är vad du behöver veta om streaming på hög nivå:

- Data levereras successivt, inte allt på en gång.
- Klienten kan bearbeta data när den anländer.
- Minskar upplevd latens och förbättrar användarupplevelsen.

### Varför använda streaming?

Anledningarna till att använda streaming är följande:

- Användare får feedback omedelbart, inte bara i slutet.
- Möjliggör realtidsapplikationer och responsiva UI:er.
- Mer effektiv användning av nätverks- och beräkningsresurser.

### Enkelt exempel: HTTP Streaming Server & Klient

Här är ett enkelt exempel på hur streaming kan implementeras:

#### Python

**Server (Python, använder FastAPI och StreamingResponse):**

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

**Klient (Python, använder requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Detta exempel visar en server som skickar en serie meddelanden till klienten när de blir tillgängliga, istället för att vänta på att alla meddelanden ska vara klara.

**Hur det fungerar:**

- Servern levererar varje meddelande när det är klart.
- Klienten tar emot och skriver ut varje delbit när den anländer.

**Krav:**

- Servern måste använda ett streaming-svar (t.ex. `StreamingResponse` i FastAPI).
- Klienten måste bearbeta svaret som en ström (`stream=True` i requests).
- Content-Type är vanligtvis `text/event-stream` eller `application/octet-stream`.

#### Java

**Server (Java, använder Spring Boot och Server-Sent Events):**

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

**Klient (Java, använder Spring WebFlux WebClient):**

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

**Java-implementeringsanteckningar:**

- Använder Spring Boots reaktiva stack med `Flux` för streaming
- `ServerSentEvent` tillhandahåller strukturerad eventstreaming med typ av event
- `WebClient` med `bodyToFlux()` möjliggör reaktiv streamingkonsumtion
- `delayElements()` simulerar behandlingstid mellan events
- Events kan ha typer (`info`, `result`) för bättre klienthantering

### Jämförelse: Klassisk streaming vs MCP streaming

Skillnaderna mellan hur streaming fungerar på klassiskt sätt jämfört med i MCP kan illustreras så här:

| Funktion               | Klassisk HTTP Streaming        | MCP Streaming (Notifikationer)   |
|------------------------|-------------------------------|---------------------------------|
| Huvudsvar              | Delat (chunked)                | Endast ett, i slutet             |
| Progressuppdateringar  | Skickas som databitars        | Skickas som notifikationer       |
| Klientkrav             | Måste bearbeta streamen        | Måste implementera meddelandehanterare |
| Användningsfall        | Stora filer, AI token-strömmar| Progress, loggar, realtidsfeedback|

### Viktiga observerade skillnader

Dessutom här är några kärnskillnader:

- **Kommunikationsmönster:**
  - Klassisk HTTP-streaming: Använder enkel chunked överföringskodning för att skicka data i bitar
  - MCP-streaming: Använder ett strukturerat notifikationssystem med JSON-RPC-protokoll

- **Meddelandesformat:**
  - Klassisk HTTP: Ren text i bitar med ny rad
  - MCP: Strukturerade LoggingMessageNotification-objekt med metadata

- **Klientimplementering:**
  - Klassisk HTTP: Enkel klient som bearbetar streaming-svar
  - MCP: Mer sofistikerad klient med meddelandehanterare för olika typer av meddelanden

- **Progressuppdateringar:**
  - Klassisk HTTP: Progress ingår i huvudsvarströmmen
  - MCP: Progress skickas via separata notifikationsmeddelanden medan huvudsvar kommer i slutet

### Rekommendationer

Det finns några saker vi rekommenderar vid val mellan klassisk streaming (som en endpoint vi visade tidigare med `/stream`) och streaming via MCP.

- **För enkla streamingbehov:** Klassisk HTTP-streaming är enklare att implementera och tillräcklig för grundläggande behov.

- **För komplexa, interaktiva applikationer:** MCP-streaming ger ett mer strukturerat tillvägagångssätt med rikare metadata och separation mellan notifikationer och slutresultat.

- **För AI-applikationer:** MCPs notifikationssystem är särskilt användbart för långvariga AI-uppgifter där du vill hålla användarna informerade om framsteg.

## Streaming i MCP

Okej, så du har sett några rekommendationer och jämförelser hittills om skillnaden mellan klassisk streaming och streaming i MCP. Låt oss gå på djupet hur du exakt kan dra nytta av streaming i MCP.

Att förstå hur streaming fungerar inom MCP-ramverket är avgörande för att bygga responsiva applikationer som ger realtidsfeedback till användare under långvariga operationer.

I MCP handlar streaming inte om att skicka huvudsvaren i bitar utan om att skicka **notifikationer** till klienten medan ett verktyg behandlar en förfrågan. Dessa notifikationer kan inkludera progressuppdateringar, loggar eller andra events.

### Hur det fungerar

Huvudresultatet skickas fortfarande som ett enda svar. Dock kan notifikationer skickas som separata meddelanden under bearbetningen och på så sätt uppdatera klienten i realtid. Klienten måste kunna hantera och visa dessa notifikationer.

## Vad är en notifikation?

Vi nämnde "Notifikation", vad betyder det i MCP-kontекст?

En notifikation är ett meddelande som skickas från servern till klienten för att informera om framsteg, status eller andra händelser under en långvarig operation. Notifikationer förbättrar transparens och användarupplevelse.

Till exempel ska en klient skicka en notifikation när den initiala handskakningen med servern är klar.

En notifikation ser ut så här som ett JSON-meddelande:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notifikationer hör till ett ämne i MCP som kallas ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Avvecklingsmeddelande:** MCP-specifikationsreleasekandidaten `2026-07-28` markerar Logging-primitive som avvecklad till förmån för `stderr` för stdio-transporter och OpenTelemetry för strukturerad observabilitet. Logging fortsätter att fungera i `2025-11-25` och i minst ett år efter formell avveckling. Se [Vad som ändras i MCP: Release-kandidat 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

För att få logging att fungera behöver servern aktivera det som en funktion/kapacitet så här:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Beroende på vilken SDK som används kan logging vara aktiverat som standard, eller så kan du behöva aktivera det explicit i serverns konfiguration.

Det finns olika typer av notifikationer:

| Nivå      | Beskrivning                   | Exempel på användningsfall     |
|-----------|------------------------------|-------------------------------|
| debug     | Detaljerad felsökningsinfo    | Funktionsin-/utträdespunkter  |
| info      | Allmänna informationsmeddelanden | Framstegsuppdateringar      |
| notice    | Normala men betydande händelser | Konfigurationsändringar      |
| warning   | Varningsförhållanden           | Användning av föråldrade funktioner |
| error     | Fel                           | Funktionsfel                  |
| critical  | Kritiska förhållanden          | Systemkomponentfel            |
| alert     | Åtgärd måste vidtas omedelbart | Upptäckt datakorruption      |
| emergency | Systemet är oanvändbart        | Fullständigt systemhaveri     |

## Implementera notifikationer i MCP

För att implementera notifikationer i MCP måste du konfigurera både server- och klientsidan för att hantera realtidsuppdateringar. Detta gör att din applikation kan ge omedelbar feedback till användare under långvariga operationer.

### Serversidan: Skicka notifikationer

Låt oss börja med serversidan. I MCP definierar du verktyg som kan skicka notifikationer medan de bearbetar förfrågningar. Servern använder kontextobjektet (vanligtvis `ctx`) för att skicka meddelanden till klienten.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

I det föregående exemplet skickar verktyget `process_files` tre notifikationer till klienten när varje fil behandlas. Metoden `ctx.info()` används för att skicka informationsmeddelanden.

Dessutom, för att aktivera notifikationer, se till att din server använder en streamingtransport (som `streamable-http`) och att din klient implementerar en meddelandehanterare för att bearbeta notifikationer. Så här kan du konfigurera servern att använda `streamable-http`-transporten:

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

I detta .NET-exempel är verktyget `ProcessFiles` dekorerat med attributet `Tool` och skickar tre notifikationer till klienten när varje fil behandlas. Metoden `ctx.Info()` används för att skicka informationsmeddelanden.

För att aktivera notifikationer i din .NET MCP-server, se till att du använder streamingtransport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klientsidan: Ta emot notifikationer

Klienten måste implementera en meddelandehanterare för att bearbeta och visa notifikationer när de anländer.

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

I det föregående exemplet kontrollerar funktionen `message_handler` om det inkommande meddelandet är en notifikation. Om så är fallet, skriver den ut notifikationen; annars bearbetas det som ett vanligt servermeddelande. Notera även hur `ClientSession` initieras med `message_handler` för att hantera inkommande notifikationer.

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

I detta .NET-exempel kontrollerar funktionen `MessageHandler` om det inkommande meddelandet är en notifikation. Om så är fallet, skriver den ut notifikationen; annars bearbetas det som ett vanligt servermeddelande. `ClientSession` initieras med meddelandehanteraren via `ClientSessionOptions`.

För att aktivera notifikationer, se till att din server använder streamingtransport (som `streamable-http`) och att din klient implementerar en meddelandehanterare för att bearbeta notifikationer.

## Progressnotifikationer & scenarion

Denna sektion förklarar konceptet progressnotifikationer i MCP, varför de är viktiga och hur man implementerar dem med Streambar HTTP. Du hittar även en praktisk uppgift för att förstärka din förståelse.

Progressnotifikationer är realtidsmeddelanden som skickas från servern till klienten under långvariga operationer. Istället för att vänta på att hela processen ska avslutas håller servern klienten uppdaterad om aktuell status. Detta förbättrar transparens, användarupplevelse och förenklar felsökning.

**Exempel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Varför använda progressnotifikationer?

Progressnotifikationer är viktiga av flera skäl:

- **Bättre användarupplevelse:** Användare ser uppdateringar medan arbetet pågår, inte bara i slutet.
- **Realtidsfeedback:** Klienter kan visa progressbarer eller loggar, vilket gör appen responsiv.
- **Enklare felsökning och övervakning:** Utvecklare och användare kan se var en process kan gå långsamt eller fastna.

### Hur man implementerar progressnotifikationer

Så här kan du implementera progressnotifikationer i MCP:

- **På servern:** Använd `ctx.info()` eller `ctx.log()` för att skicka notifikationer under bearbetning av varje del. Detta skickar ett meddelande till klienten innan huvudresultatet är klart.
- **På klienten:** Implementera en meddelandehanterare som lyssnar efter och visar notifikationer när de anländer. Denna handler skiljer på notifikationer och slutresultatet.

**Serverexempel:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Klientexempel:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Säkerhetshänsyn

Säkerhet bör vara en högsta prioritet vid implementering av vilken server som helst, särskilt när man använder HTTP-baserade transportmetoder som Streamable HTTP i MCP.

När man implementerar MCP-servrar med HTTP-baserade transportmetoder blir säkerhet en avgörande fråga som kräver noggrann uppmärksamhet på flera attackytor och skyddsmekanismer.

### Översikt

Säkerhet är avgörande när MCP-servrar exponeras över HTTP. Streamable HTTP introducerar nya angreppsyta och kräver noggrann konfiguration.

Här är några viktiga säkerhetshänsyn:

- **Validering av Origin Header**: Validera alltid `Origin`-headern för att förhindra DNS-rebinding-attacker.
- **Bindning till localhost**: För lokal utveckling, bind servrar till `localhost` för att undvika exponering mot det offentliga internet.
- **Autentisering**: Implementera autentisering (t.ex. API-nycklar, OAuth) för produktionsdistributioner.
- **CORS**: Konfigurera policyer för Cross-Origin Resource Sharing (CORS) för att begränsa åtkomst.
- **HTTPS**: Använd HTTPS i produktion för att kryptera trafiken.

### Bästa metoder

Dessutom är här några bästa metoder att följa när du implementerar säkerhet i din MCP-streamingserver:

- Lita aldrig på inkommande förfrågningar utan validering.
- Logga och övervaka all åtkomst och fel.
- Uppdatera regelbundet beroenden för att åtgärda säkerhetssårbarheter.

### Utmaningar

Du kommer att möta vissa utmaningar när du implementerar säkerhet i MCP-streamingservrar:

- Att balansera säkerhet med utvecklingsvänlighet
- Att säkerställa kompatibilitet med olika klientmiljöer


## Uppgradering från SSE till Streamable HTTP

För applikationer som för närvarande använder Server-Sent Events (SSE) ger en migration till Streamable HTTP förbättrade möjligheter och bättre långsiktig hållbarhet för dina MCP-implementationer.

### Varför uppgradera?

Det finns två starka skäl att uppgradera från SSE till Streamable HTTP:

- Streamable HTTP erbjuder bättre skalbarhet, kompatibilitet och rikare notifieringsstöd än SSE.
- Det är den rekommenderade transporten för nya MCP-applikationer.

### Migreringssteg

Så här kan du migrera från SSE till Streamable HTTP i dina MCP-applikationer:

- **Uppdatera serverkoden** för att använda `transport="streamable-http"` i `mcp.run()`.
- **Uppdatera klientkoden** för att använda `streamablehttp_client` istället för SSE-klienten.
- **Implementera en meddelandehanterare** i klienten för att bearbeta notifieringar.
- **Testa kompatibilitet** med befintliga verktyg och arbetsflöden.

### Bibehållen kompatibilitet

Det rekommenderas att bibehålla kompatibilitet med befintliga SSE-klienter under migrationsprocessen. Här är några strategier:

- Du kan stödja både SSE och Streamable HTTP genom att köra båda transportmetoderna på olika slutpunkter.
- Migrera gradvis klienter till den nya transporten.

### Utmaningar

Se till att hantera följande utmaningar under migreringen:

- Säkerställ att alla klienter är uppdaterade
- Hantera skillnader i notifieringsleverans

### Uppgift: Bygg din egen streaming-MCP-app

**Scenario:**
Bygg en MCP-server och klient där servern bearbetar en lista med objekt (t.ex. filer eller dokument) och skickar en notifiering för varje bearbetat objekt. Klienten ska visa varje notifiering när den anländer.

**Steg:**

1. Implementera ett serververktyg som bearbetar en lista och skickar notifieringar för varje objekt.
2. Implementera en klient med en meddelandehanterare för att visa notifieringar i realtid.
3. Testa din implementation genom att köra både server och klient, och observera notifieringarna.

[Lösning](./solution/README.md)

## Vidare läsning & Vad händer härnäst?

För att fortsätta din resa med MCP-streaming och utöka din kunskap, erbjuder detta avsnitt ytterligare resurser och föreslagna nästa steg för att bygga mer avancerade applikationer.

### Vidare läsning

- [Microsoft: Introduktion till HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS i ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Vad händer härnäst?

- Försök bygga mer avancerade MCP-verktyg som använder streaming för realtidsanalys, chatt eller samarbetande redigering.
- Utforska integration av MCP-streaming med frontend-ramverk (React, Vue, etc.) för live-UI-uppdateringar.
- Nästa: [Användning av AI Toolkit för VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->