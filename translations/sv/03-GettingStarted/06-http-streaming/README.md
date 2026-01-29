# HTTPS-strömning med Model Context Protocol (MCP)

Detta kapitel ger en omfattande guide till att implementera säker, skalbar och realtidsströmning med Model Context Protocol (MCP) via HTTPS. Det täcker motivationen för strömning, tillgängliga transportmekanismer, hur man implementerar strömningsbar HTTP i MCP, säkerhetsbästa praxis, migrering från SSE och praktiska råd för att bygga egna MCP-strömningsapplikationer.

## Transportmekanismer och strömning i MCP

Denna sektion utforskar de olika transportmekanismer som finns tillgängliga i MCP och deras roll i att möjliggöra strömningsfunktioner för realtidskommunikation mellan klienter och servrar.

### Vad är en transportmekanism?

En transportmekanism definierar hur data utbyts mellan klient och server. MCP stöder flera transporttyper för att passa olika miljöer och krav:

- **stdio**: Standard in-/utmatning, lämplig för lokala och CLI-baserade verktyg. Enkel men inte lämplig för webb eller moln.
- **SSE (Server-Sent Events)**: Gör det möjligt för servrar att skicka realtidsuppdateringar till klienter över HTTP. Bra för webbgränssnitt, men begränsad i skalbarhet och flexibilitet.
- **Strömningsbar HTTP**: Modern HTTP-baserad strömningstransport som stöder aviseringar och bättre skalbarhet. Rekommenderas för de flesta produktions- och molnscenarier.

### Jämförelsetabell

Se jämförelsetabellen nedan för att förstå skillnaderna mellan dessa transportmekanismer:

| Transport         | Realtidsuppdateringar | Strömning | Skalbarhet | Användningsfall          |
|-------------------|-----------------------|-----------|------------|--------------------------|
| stdio             | Nej                   | Nej        | Låg        | Lokala CLI-verktyg       |
| SSE               | Ja                    | Ja         | Medel      | Webb, realtidsuppdateringar |
| Strömningsbar HTTP| Ja                    | Ja         | Hög        | Moln, flera klienter     |

> **Tips:** Valet av rätt transport påverkar prestanda, skalbarhet och användarupplevelse. **Strömningsbar HTTP** rekommenderas för moderna, skalbara och molnklara applikationer.

Notera transporterna stdio och SSE som du såg i de tidigare kapitlen och hur strömningsbar HTTP är den transport som behandlas i detta kapitel.

## Strömning: Koncept och motivation

Att förstå de grundläggande koncepten och motivationen bakom strömning är avgörande för att implementera effektiva realtidskommunikationssystem.

**Strömning** är en teknik inom nätverksprogrammering som gör det möjligt att skicka och ta emot data i små, hanterbara delar eller som en sekvens av händelser, istället för att vänta på att hela svaret ska vara klart. Detta är särskilt användbart för:

- Stora filer eller dataset.
- Realtidsuppdateringar (t.ex. chatt, framstegsbalkar).
- Långvariga beräkningar där användaren vill hållas informerad.

Här är vad du behöver veta om strömning på hög nivå:

- Data levereras successivt, inte allt på en gång.
- Klienten kan bearbeta data när den anländer.
- Minskar upplevd latens och förbättrar användarupplevelsen.

### Varför använda strömning?

Skälen till att använda strömning är följande:

- Användare får omedelbar feedback, inte bara i slutet.
- Möjliggör realtidsapplikationer och responsiva gränssnitt.
- Effektivare användning av nätverks- och beräkningsresurser.

### Enkelt exempel: HTTP-strömningsserver och klient

Här är ett enkelt exempel på hur strömning kan implementeras:

#### Python

**Server (Python, med FastAPI och StreamingResponse):**

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

**Klient (Python, med requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Detta exempel visar en server som skickar en serie meddelanden till klienten när de blir tillgängliga, istället för att vänta på att alla meddelanden ska vara klara.

**Hur det fungerar:**

- Servern skickar varje meddelande när det är klart.
- Klienten tar emot och skriver ut varje del när den anländer.

**Krav:**

- Servern måste använda ett strömningssvar (t.ex. `StreamingResponse` i FastAPI).
- Klienten måste bearbeta svaret som en ström (`stream=True` i requests).
- Content-Type är vanligtvis `text/event-stream` eller `application/octet-stream`.

#### Java

**Server (Java, med Spring Boot och Server-Sent Events):**

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

**Klient (Java, med Spring WebFlux WebClient):**

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

**Noteringar om Java-implementering:**

- Använder Spring Boots reaktiva stack med `Flux` för strömning.
- `ServerSentEvent` möjliggör strukturerad händelseströmning med händelsetyper.
- `WebClient` med `bodyToFlux()` möjliggör reaktiv konsumtion av strömning.
- `delayElements()` simulerar bearbetningstid mellan händelser.
- Händelser kan ha typer (`info`, `result`) för bättre hantering på klientsidan.

### Jämförelse: Klassisk strömning vs MCP-strömning

Skillnaderna mellan hur strömning fungerar på ett "klassiskt" sätt jämfört med hur det fungerar i MCP kan beskrivas så här:

| Funktion              | Klassisk HTTP-strömning       | MCP-strömning (Aviseringar)       |
|-----------------------|-------------------------------|-----------------------------------|
| Huvudsvar             | Uppdelat i delar             | Enkelt, i slutet                 |
| Framstegsuppdateringar| Skickas som datafragment     | Skickas som aviseringar          |
| Klientkrav            | Måste bearbeta strömmen      | Måste implementera meddelandehanterare |
| Användningsfall       | Stora filer, AI-tokenströmmar| Framsteg, loggar, realtidsfeedback|

### Observerade nyckelskillnader

Ytterligare några nyckelskillnader:

- **Kommunikationsmönster:**
  - Klassisk HTTP-strömning: Använder enkel chunked transfer encoding för att skicka data i delar.
  - MCP-strömning: Använder ett strukturerat avisering-system med JSON-RPC-protokoll.

- **Meddelandeformat:**
  - Klassisk HTTP: Oformaterade textfragment med radbrytningar.
  - MCP: Strukturerade `LoggingMessageNotification`-objekt med metadata.

- **Klientimplementering:**
  - Klassisk HTTP: Enkel klient som bearbetar strömningssvar.
  - MCP: Mer sofistikerad klient med en meddelandehanterare för att bearbeta olika typer av meddelanden.

- **Framstegsuppdateringar:**
  - Klassisk HTTP: Framstegen är en del av huvudströmmen.
  - MCP: Framsteg skickas via separata aviseringar medan huvudsvar kommer i slutet.

### Rekommendationer

Här är några rekommendationer när det gäller att välja mellan att implementera klassisk strömning (som ett slutpunkt vi visade ovan med `/stream`) och att välja strömning via MCP.

- **För enkla strömningsbehov:** Klassisk HTTP-strömning är enklare att implementera och tillräcklig för grundläggande strömningsbehov.
- **För komplexa, interaktiva applikationer:** MCP-strömning ger ett mer strukturerat tillvägagångssätt med rikare metadata och separation mellan aviseringar och slutresultat.
- **För AI-applikationer:** MCP:s aviseringssystem är särskilt användbart för långvariga AI-uppgifter där du vill hålla användarna informerade om framsteg.

## Strömning i MCP

Okej, så du har sett några rekommendationer och jämförelser hittills om skillnaden mellan klassisk strömning och strömning i MCP. Låt oss gå in i detalj på exakt hur du kan dra nytta av strömning i MCP.

Att förstå hur strömning fungerar inom MCP-ramverket är avgörande för att bygga responsiva applikationer som ger realtidsfeedback till användare under långvariga operationer.

I MCP handlar strömning inte om att skicka huvudsvar i delar, utan om att skicka **aviseringar** till klienten medan ett verktyg bearbetar en begäran. Dessa aviseringar kan inkludera framstegsuppdateringar, loggar eller andra händelser.

### Hur det fungerar

Huvudresultatet skickas fortfarande som ett enda svar. Aviseringar kan dock skickas som separata meddelanden under bearbetningen och därmed uppdatera klienten i realtid. Klienten måste kunna hantera och visa dessa aviseringar.

## Vad är en avisering?

Vi nämnde "avisering", vad betyder det i MCP:s sammanhang?

En avisering är ett meddelande som skickas från servern till klienten för att informera om framsteg, status eller andra händelser under en långvarig operation. Aviseringar förbättrar transparens och användarupplevelse.

Till exempel ska en klient skicka en avisering när den initiala handskakningen med servern har gjorts.

En avisering ser ut så här som ett JSON-meddelande:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Aviseringar tillhör ett ämne i MCP som kallas ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

För att få loggning att fungera måste servern aktivera det som en funktion/kapabilitet så här:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Beroende på vilken SDK som används kan loggning vara aktiverad som standard, eller så kan du behöva aktivera det explicit i din serverkonfiguration.

Det finns olika typer av aviseringar:

| Nivå       | Beskrivning                  | Exempel på användningsfall       |
|------------|-----------------------------|----------------------------------|
| debug      | Detaljerad felsökningsinfo  | Funktionens in-/utgångspunkter  |
| info       | Allmänna informationsmeddelanden | Framstegsuppdateringar         |
| notice     | Normala men viktiga händelser | Konfigurationsändringar        |
| warning    | Varningsförhållanden        | Användning av föråldrade funktioner |
| error      | Felvillkor                  | Misslyckade operationer         |
| critical   | Kritiska förhållanden       | Fel i systemkomponenter         |
| alert      | Omedelbar åtgärd krävs      | Upptäckt av datakorruption      |
| emergency  | Systemet är oanvändbart     | Fullständigt systemfel          |

## Implementering av aviseringar i MCP

För att implementera aviseringar i MCP måste du konfigurera både server- och klientsidan för att hantera realtidsuppdateringar. Detta gör det möjligt för din applikation att ge omedelbar feedback till användare under långvariga operationer.

### Serversidan: Skicka aviseringar

Låt oss börja med serversidan. I MCP definierar du verktyg som kan skicka aviseringar medan de bearbetar begäranden. Servern använder kontextobjektet (vanligtvis `ctx`) för att skicka meddelanden till klienten.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

I föregående exempel skickar verktyget `process_files` tre aviseringar till klienten medan det bearbetar varje fil. Metoden `ctx.info()` används för att skicka informationsmeddelanden.

Dessutom, för att aktivera aviseringar, se till att din server använder en strömningsbar transport (som `streamable-http`) och att din klient implementerar en meddelandehanterare för att bearbeta aviseringar. Här är hur du kan konfigurera servern för att använda transporten `streamable-http`:

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

I detta .NET-exempel är verktyget `ProcessFiles` dekorerat med attributet `Tool` och skickar tre aviseringar till klienten medan det bearbetar varje fil. Metoden `ctx.Info()` används för att skicka informationsmeddelanden.

För att aktivera aviseringar i din .NET MCP-server, se till att du använder en strömningsbar transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klientsidan: Ta emot aviseringar

Klienten måste implementera en meddelandehanterare för att bearbeta och visa aviseringar när de anländer.

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

I föregående kod kontrollerar funktionen `message_handler` om det inkommande meddelandet är en avisering. Om det är det, skriver den ut aviseringen; annars bearbetar den det som ett vanligt servermeddelande. Notera också hur `ClientSession` initieras med `message_handler` för att hantera inkommande aviseringar.

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

I detta .NET-exempel kontrollerar funktionen `MessageHandler` om det inkommande meddelandet är en avisering. Om det är det, skriver den ut aviseringen; annars bearbetar den det som ett vanligt servermeddelande. `ClientSession` initieras med meddelandehanteraren via `ClientSessionOptions`.

För att aktivera aviseringar, se till att din server använder en strömningsbar transport (som `streamable-http`) och att din klient implementerar en meddelandehanterare för att bearbeta aviseringar.

## Framstegsaviseringar och scenarier

Denna sektion förklarar konceptet med framstegsaviseringar i MCP, varför de är viktiga och hur man implementerar dem med strömningsbar HTTP. Du hittar också en praktisk uppgift för att förstärka din förståelse.

Framstegsaviseringar är realtidsmeddelanden som skickas från servern till klienten under långvariga operationer. Istället för att vänta på att hela processen ska slutföras, håller servern klienten uppdaterad om aktuell status. Detta förbättrar transparens, användarupplevelse och gör felsökning enklare.

**Exempel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Varför använda framstegsaviseringar?

Framstegsaviseringar är viktiga av flera skäl:

- **Bättre användarupplevelse:** Användare ser uppdateringar medan arbetet fortskrider, inte bara i slutet.
- **Realtidsfeedback:** Klienter kan visa framstegsbalkar eller loggar, vilket gör appen mer responsiv.
- **Enklare felsökning och övervakning:** Utvecklare och användare kan se var en process kan vara långsam eller fastna.

### Hur man implementerar framstegsaviseringar

Så här implementerar du framstegsaviseringar i MCP:

- **På servern:** Använd `ctx.info()` eller `ctx.log()` för att skicka aviseringar när varje objekt bearbetas. Detta skickar ett meddelande till klienten innan huvudresultatet är klart.
- **På klienten:** Implementera en meddelandehanterare som lyssnar på och visar aviseringar när de anländer. Denna hanterare skiljer mellan aviseringar och slutresultatet.

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

## Säkerhetsöverväganden

När du implementerar MCP-servrar med HTTP-baserade transporter blir säkerhet en avgörande fråga som kräver noggrann uppmärksamhet på flera attackvektorer och skyddsmekanismer.

### Översikt

Säkerhet är kritiskt när MCP-servrar exponeras över HTTP. Strömningsbar HTTP introducerar nya attackytor och kräver noggrann konfiguration.

### Viktiga punkter

- **Validering av Origin-header:** Validera alltid `Origin`-headern för att förhindra DNS-rebinding-attacker.
- **Bindning till localhost:** För lokal utveckling, bind servrar till `localhost` för att undvika exponering för det offentliga internet.
- **Autentisering:** Implementera autentisering (t.ex. API-nycklar, OAuth) för produktionsdistributioner.
- **CORS:** Konfigurera Cross-Origin Resource Sharing (CORS)-policyer för att begränsa åtkomst.
- **HTTPS:** Använd HTTPS i produktion för att kryptera trafik.

### Bästa praxis

- Lita aldrig på inkommande begäranden utan validering.
- Logga och övervaka all åtkomst och alla fel.
- Uppdatera regelbundet beroenden för att åtgärda säkerhetsbrister.

### Utmaningar

- Att balansera säkerhet med enkelhet i utveckling.
- Att säkerställa kompatibilitet med olika klientmiljöer.

## Uppgradering från SSE till strömningsbar HTTP

För applikationer som för närvarande använder Server-Sent Events (SSE), ger migrering till strömningsbar HTTP förbättrade funktioner och bättre långsiktig hållbarhet för dina MCP-implementeringar.

### Varför uppgradera?
Det finns två övertygande skäl att uppgradera från SSE till Streamable HTTP:

- Streamable HTTP erbjuder bättre skalbarhet, kompatibilitet och mer avancerat stöd för notifieringar än SSE.
- Det är den rekommenderade transporten för nya MCP-applikationer.

### Migreringssteg

Så här kan du migrera från SSE till Streamable HTTP i dina MCP-applikationer:

- **Uppdatera serverkoden** för att använda `transport="streamable-http"` i `mcp.run()`.
- **Uppdatera klientkoden** för att använda `streamablehttp_client` istället för SSE-klient.
- **Implementera en meddelandehanterare** i klienten för att bearbeta notifieringar.
- **Testa kompatibilitet** med befintliga verktyg och arbetsflöden.

### Bibehålla kompatibilitet

Det rekommenderas att bibehålla kompatibilitet med befintliga SSE-klienter under migreringsprocessen. Här är några strategier:

- Du kan stödja både SSE och Streamable HTTP genom att köra båda transporterna på olika slutpunkter.
- Migrera klienter gradvis till den nya transporten.

### Utmaningar

Se till att hantera följande utmaningar under migreringen:

- Säkerställa att alla klienter är uppdaterade
- Hantera skillnader i notifieringsleverans

## Säkerhetsaspekter

Säkerhet bör vara högsta prioritet vid implementering av en server, särskilt när du använder HTTP-baserade transporter som Streamable HTTP i MCP.

Vid implementering av MCP-servrar med HTTP-baserade transporter blir säkerhet en avgörande fråga som kräver noggrann uppmärksamhet på flera attackvektorer och skyddsmekanismer.

### Översikt

Säkerhet är kritiskt när MCP-servrar exponeras över HTTP. Streamable HTTP introducerar nya attackytor och kräver noggrann konfiguration.

Här är några viktiga säkerhetsaspekter:

- **Validering av Origin-header**: Validera alltid `Origin`-headern för att förhindra DNS-rebinding-attacker.
- **Bindning till localhost**: För lokal utveckling, bind servrar till `localhost` för att undvika exponering mot internet.
- **Autentisering**: Implementera autentisering (t.ex. API-nycklar, OAuth) för produktionsmiljöer.
- **CORS**: Konfigurera Cross-Origin Resource Sharing (CORS)-policys för att begränsa åtkomst.
- **HTTPS**: Använd HTTPS i produktion för att kryptera trafik.

### Bästa praxis

Dessutom, här är några bästa praxis att följa vid implementering av säkerhet i din MCP-streamingserver:

- Lita aldrig på inkommande förfrågningar utan validering.
- Logga och övervaka all åtkomst och alla fel.
- Uppdatera regelbundet beroenden för att åtgärda säkerhetsbrister.

### Utmaningar

Du kommer att möta vissa utmaningar vid implementering av säkerhet i MCP-streamingservrar:

- Balans mellan säkerhet och enkel utveckling
- Säkerställa kompatibilitet med olika klientmiljöer

### Uppgift: Bygg din egen streaming MCP-app

**Scenario:**
Bygg en MCP-server och klient där servern bearbetar en lista med objekt (t.ex. filer eller dokument) och skickar en notifiering för varje bearbetat objekt. Klienten ska visa varje notifiering när den anländer.

**Steg:**

1. Implementera ett serververktyg som bearbetar en lista och skickar notifieringar för varje objekt.
2. Implementera en klient med en meddelandehanterare för att visa notifieringar i realtid.
3. Testa din implementation genom att köra både server och klient och observera notifieringarna.

[Solution](./solution/README.md)

## Vidare läsning & Vad händer härnäst?

För att fortsätta din resa med MCP-streaming och utöka din kunskap, erbjuder denna sektion ytterligare resurser och föreslagna nästa steg för att bygga mer avancerade applikationer.

### Vidare läsning

- [Microsoft: Introduktion till HTTP-streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS i ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Vad händer härnäst?

- Försök att bygga mer avancerade MCP-verktyg som använder streaming för realtidsanalys, chatt eller samarbetsredigering.
- Utforska integration av MCP-streaming med frontend-ramverk (React, Vue, etc.) för live-uppdateringar i användargränssnittet.
- Nästa: [Använda AI Toolkit för VSCode](../07-aitk/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.