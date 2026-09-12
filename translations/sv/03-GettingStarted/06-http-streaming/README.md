# HTTPS Streaming med Model Context Protocol (MCP)

Detta kapitel ger en omfattande guide för att implementera säker, skalbar och realtidsströmning med Model Context Protocol (MCP) via HTTPS. Det täcker motivationen för strömning, tillgängliga transportmekanismer, hur man implementerar strömbar HTTP i MCP, säkerhets bästa praxis, migrering från SSE och praktiska vägledningar för att bygga egna strömmande MCP-applikationer.

> [!WARNING]
> Implementeringsexemplen i denna lektion riktar sig till **MCP-specifikationen
> `2025-11-25`** och demonstrerar den äldre `initialize`-handshaken,
> `Mcp-Session-Id`, GET-eventström och återupptagningsmodellen. MCP `2026-07-28`
> tar bort dessa funktioner. Nuvarande strömmande HTTP-förfrågningar är självständiga
> POST-förfrågningar med `MCP-Protocol-Version` och `Mcp-Method`-huvuden, plus
> `Mcp-Name` där det krävs. Se
> [Vad som har ändrats i MCP: Specifikationen 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> innan du använder dessa exempel i en ny implementation.

## Transportmekanismer och Strömning i MCP

Denna sektion utforskar de olika transportmekanismerna som finns i MCP och deras roll i att möjliggöra strömningsegenskaper för realtidskommunikation mellan klienter och servrar.

### Vad är en transportmekanism?

En transportmekanism definierar hur data utbyts mellan klient och server. MCP stödjer flera transporttyper för att passa olika miljöer och krav:

- **stdio**: Standard in- och utdata, lämpligt för lokala och CLI-baserade verktyg. Enkelt men inte lämpligt för webben eller molnet.
- **HTTP+SSE**: Den äldre fjärrtransporten, avvecklad i MCP `2025-03-26`
    och ersatt av Streamable HTTP. Använd inte detta för nya implementationer.
- **Streamable HTTP**: Modern HTTP-baserad strömningstransport, stöd för notifieringar och bättre skalbarhet. Rekommenderas för de flesta produktions- och molnscenarier.

### Jämförelsetabell

Ta en titt på jämförelsetabellen nedan för att förstå skillnaderna mellan dessa transportmekanismer:

| Transport | Status | Notifieringar | Typisk användning |
|---|---|---|---|
| stdio | Aktuell | Ja | Lokala underprocesser |
| HTTP+SSE | Avvecklad | Ja | Äldre fjärrimplementationer |
| Streamable HTTP | Aktuell | Ja | Fjärr- och molnservrar |

> **Tips:** Valet av rätt transport påverkar prestanda, skalbarhet och användarupplevelse. **Streamable HTTP** rekommenderas för moderna, skalbara och molnklara applikationer.

Standardtransporterna är stdio och Streamable HTTP. HTTP+SSE förekommer endast i
äldre exempel.

## Strömning: Koncept och Motivation

Att förstå de grundläggande koncepten och motiven bakom strömning är viktigt för att implementera effektiva realtidskommunikationssystem.

**Strömning** är en teknik inom nätverksprogrammering som möjliggör att data skickas och tas emot i små, hanterbara bitar eller som en sekvens av händelser, istället för att vänta på att ett helt svar ska bli klart. Detta är särskilt användbart för:

- Stora filer eller dataset.
- Realtidsuppdateringar (t.ex. chatt, förloppsindikatorer).
- Långvariga beräkningar där man vill hålla användaren informerad.

Här är vad du behöver veta om strömning på hög nivå:

- Data levereras stegvis, inte allt på en gång.
- Klienten kan bearbeta data allteftersom det anländer.
- Minskar upplevd fördröjning och förbättrar användarupplevelsen.

### Varför använda strömning?

Skälen till att använda strömning är följande:

- Användare får omedelbar återkoppling, inte bara i slutet
- Möjliggör realtidsapplikationer och responsiva användargränssnitt
- Mer effektiv användning av nätverks- och beräkningsresurser

### Enkelt exempel: HTTP strömningsserver & klient

Här är ett enkelt exempel på hur strömning kan implementeras:

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

Detta exempel demonstrerar en server som skickar en serie meddelanden till klienten när de blir tillgängliga, istället för att vänta tills alla meddelanden är klara.

**Hur det fungerar:**

- Servern yieldar varje meddelande när det är klart.
- Klienten tar emot och skriver ut varje bit när den anländer.

**Krav:**

- Servern måste använda ett strömningssvar (t.ex. `StreamingResponse` i FastAPI).
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

**Java implementeringsanteckningar:**

- Använder Spring Boots reaktiva stack med `Flux` för strömning
- `ServerSentEvent` ger strukturerad händelseströmning med händelsetyper
- `WebClient` med `bodyToFlux()` möjliggör reaktiv strömningskonsumtion
- `delayElements()` simulerar behandlingstid mellan händelser
- Händelser kan ha typer (`info`, `result`) för bättre klienthantering

### Jämförelse: Klassisk strömning vs MCP-strömning

Skillnaderna mellan hur strömning fungerar på ett "klassiskt" sätt jämfört med hur det fungerar i MCP kan illustreras så här:

| Funktion                | Klassisk HTTP-strömning        | MCP-strömning (Notifieringar)      |
|------------------------|-------------------------------|-------------------------------------|
| Huvudsvar               | Delat i bitar                 | Enkelt, i slutet                    |
| Förloppsuppdateringar   | Skickas som databitars        | Skickas som notifieringar          |
| Klientkrav              | Måste bearbeta strömmen       | Måste implementera meddelandehanterare |
| Användningsfall         | Stora filer, AI-tokenströmmar | Förlopp, loggar, realtidsfeedback  |

### Viktiga observerade skillnader

Dessutom finns några nyckelskillnader:

- **Kommunikationsmönster:**
  - Klassisk HTTP-strömning: Använder enkel bitöverföring för att skicka data i bitar
  - MCP-strömning: Använder ett strukturerat notifikationssystem med JSON-RPC-protokoll

- **Meddelandformat:**
  - Klassisk HTTP: Vanlig textdelar med radbrytningar
  - MCP: Strukturerade LoggingMessageNotification-objekt med metadata

- **Klientimplementation:**
  - Klassisk HTTP: Enkel klient som bearbetar strömningssvar
  - MCP: Mer avancerad klient med meddelandehanterare för att bearbeta olika meddelandetyper

- **Förloppsuppdateringar:**
  - Klassisk HTTP: Förloppet är del av huvudsvarsströmmen
  - MCP: Förlopp skickas via separata notifieringsmeddelanden medan huvudsvar kommer i slutet

### Rekommendationer

Det finns några saker vi rekommenderar när det gäller valet mellan att implementera klassisk strömning (som en slutpunkt vi visade ovan med `/stream`) jämfört med strömning via MCP.

- **För enkla strömningsbehov:** Klassisk HTTP-strömning är enklare att implementera och tillräcklig för grundläggande strömningsbehov.


- **För komplexa, interaktiva applikationer:** MCP-strömning erbjuder en mer strukturerad metod med rikare metadata och separation mellan notifikationer och slutgiltiga resultat.

- **För AI-applikationer:** MCP:s notifikationssystem är särskilt användbart för långvariga AI-uppgifter där du vill hålla användarna informerade om framstegen.

## Strömning i MCP

Okej, så du har sett några rekommendationer och jämförelser hittills om skillnaden mellan klassisk strömning och strömning i MCP. Låt oss gå in på detaljer om exakt hur du kan utnyttja strömning i MCP.

Att förstå hur strömning fungerar inom MCP-ramverket är avgörande för att bygga responsiva applikationer som ger realtidsfeedback till användare under långvariga operationer.

I MCP handlar strömning inte om att skicka huvudsvaret i delar, utan om att skicka **notifikationer** till klienten medan ett verktyg bearbetar en begäran. Dessa notifikationer kan inkludera uppdateringar om framsteg, loggar eller andra händelser.

### Hur det fungerar

Huvudresultatet skickas fortfarande som ett enskilt svar. Dock kan notifikationer skickas som separata meddelanden under bearbetningen och därmed uppdatera klienten i realtid. Klienten måste kunna hantera och visa dessa notifikationer.

### Valfri övning: anslut till en hostad MCP-server

Du kan också använda Streamable HTTP utan att köra en lokal server. Detta exempel
ansluter till [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
upptäcker dess verktyg och söker efter offentlig MCP-dokumentation med samma
Python SDK som [den lokala klienten](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Parallels anonyma endpoint kräver inget konto eller API-nyckel. Fri åtkomst är
hastighetsbegränsad. Att köra detta skript skickar sökfrågorna, målet och en
slumpmässig sessionsidentifierare till Parallel. Tjänsten erbjuder också `web_fetch`,
som skickar begärda URL:er och eventuell angiven kontext till Parallel. Använd offentlig
information för denna övning; se dess [villkor](https://parallel.ai/customer-terms)
och [integritetspolicy](https://parallel.ai/privacy-policy).

Med Python 3.10 eller nyare och en aktiverad virtuell miljö, installera SDK:n:

```sh
python -m pip install "mcp>=1.10,<2"
```

Spara detta som `hosted_search.py` och kör `python hosted_search.py`:

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

Förvänta dig att upptäckten inkluderar `web_search` och `web_fetch`, följt av ett sök
svar innehållande käll-URL:er och utdrag. Resultaten kan variera eller vara tomma.
Skriptet kontrollerar `isError` eftersom ett verktyg kan misslyckas även om HTTP-begäran
lyckas. Om åtkomsten är hastighetsbegränsad, vänta innan du försöker igen. Återanvänd
samma `session_id` om du förlänger skriptet med relaterade sök- eller hämtanrop.

Streamable HTTP tillåter både JSON- och SSE-svar; denna server kan returnera ett
komplett JSON-resultat utan framstegsnotifikationer. SDK:n hanterar
transporten. Fortsätt med det lokala exemplet nedan för att lära dig om notifikationer.
Detta valfria skript gör en explicit sökning och stänger sin anslutning när
den är klar. Om du senare exponerar dessa verktyg för en agent kan agenten anropa
dem under sitt arbete; behandla hämtad webtext som opålitliga data.

## Vad är en Notifikation?

Vi sade "Notifikation", vad betyder det i MCP:s kontext?

En notifikation är ett JSON-RPC-meddelande som inte har ett `id` och inte
får något svar. MCP använder notifikationer för framsteg, avbokning och
andra envägs-händelser.

I MCP `2025-11-25` skickar klienten `notifications/initialized` efter
initialeringshandskakningen. MCP `2026-07-28` har ingen initialeringshandshake, så
denna notifikation är ett äldre beteende.

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

Loggning är en funktion som använder notifikationer; notifikationer är i sig själva en
generell JSON-RPC-meddelandetyp.

> **Föråldrat i MCP `2026-07-28`:** Loggningsfunktionen är fortfarande tillgänglig
> för kompatibilitet men kan tas bort i den första specifikations-
> revideringen som släpps den 28 juli 2027 eller senare. Nya implementationer bör använda
> `stderr` med stdio eller OpenTelemetry för strukturerad observerbarhet.

För en äldre `2025-11-25`-implementation aktiverar servern loggnings-
möjligheten på följande sätt:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Beroende på vilken SDK som används kan loggning vara aktiverad som standard, eller så måste du uttryckligen aktivera den i din serverkonfiguration.

Det finns olika typer av notifikationer:

| Nivå      | Beskrivning                   | Exempelanvändning              |
|-----------|-------------------------------|---------------------------------|
| debug     | Detaljerad felsökningsinformation | Funktionsstart-/slutpunkter      |
| info      | Allmänna informationsmeddelanden | Uppdateringar om operationens framsteg |
| notice    | Normala men viktiga händelser  | Konfigurationsändringar         |
| warning   | Varningsförhållanden           | Användning av föråldrad funktion |
| error     | Fel-förhållanden               | Funktionsfel                   |
| critical  | Kritiska förhållanden          | Systemkomponentfel             |
| alert     | Åtgärd måste vidtas omedelbart | Datakorruption upptäckt        |
| emergency | Systemet är oanvändbart        | Fullständigt systemfel         |

## Implementera Notifikationer i MCP

För att implementera notifikationer i MCP behöver du konfigurera både server- och klientsidan för att hantera realtidsuppdateringar. Detta gör att din applikation kan ge omedelbar feedback till användare under långvariga operationer.

### Serversidan: Skicka Notifikationer

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

I föregående exempel skickar verktyget `process_files` tre notifikationer till klienten medan det bearbetar varje fil. `ctx.info()`-metoden används för att skicka informationsmeddelanden.

Dessutom, för att aktivera notifikationer, se till att din server använder en strömmande transport (som `streamable-http`) och att din klient implementerar en meddelandehanterare för att bearbeta notifikationer. Så här kan du ställa in servern att använda `streamable-http`-transporten:

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

I detta .NET-exempel är verktyget `ProcessFiles` dekorerat med attributet `Tool` och skickar tre notifikationer till klienten medan det bearbetar varje fil. `ctx.Info()`-metoden används för att skicka informationsmeddelanden.

För att aktivera notifikationer i din .NET MCP-server, säkerställ att du använder en strömmande transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klientsidan: Ta emot Notifikationer

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

I föregående kod kontrollerar funktionen `message_handler` om det inkommande meddelandet är en notifikation. Om så är fallet, skrivs notifikationen ut; annars behandlas den som ett vanligt servermeddelande. Notera också hur `ClientSession` initieras med `message_handler` för att hantera inkommande notifikationer.

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


I detta .NET-exempel kontrollerar funktionen `MessageHandler` om det inkommande meddelandet är en notifikation. Om det är det skriver den ut notifikationen; annars behandlas det som ett vanligt servermeddelande. `ClientSession` initieras med meddelandehanteraren via `ClientSessionOptions`.

För att aktivera notifikationer, se till att din server använder en strömmande transport (som `streamable-http`) och att din klient implementerar en meddelandehanterare för att behandla notifikationer.

## Status-Notifikationer & Scenarier

Den här sektionen förklarar begreppet status-notifikationer i MCP, varför de är viktiga och hur man implementerar dem med Streamable HTTP. Du hittar också en praktisk uppgift för att stärka din förståelse.

Status-notifikationer är realtidsmeddelanden som skickas från servern till klienten under långvariga operationer. Istället för att vänta tills hela processen är klar håller servern klienten uppdaterad om aktuell status. Detta förbättrar transparens, användarupplevelse och gör felsökning enklare.

**Exempel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Varför använda status-notifikationer?

Status-notifikationer är viktiga av flera skäl:

- **Bättre användarupplevelse:** Användare ser uppdateringar i takt med att arbetet fortskrider, inte bara i slutet.
- **Feedback i realtid:** Klienter kan visa progressionsindikatorer eller loggar, vilket gör att appen känns lyhörd.
- **Enklare felsökning och övervakning:** Utvecklare och användare kan se var en process kan vara långsam eller fastna.

### Så implementerar du status-notifikationer

Så här kan du implementera status-notifikationer i MCP:

- **På servern:** Använd `ctx.info()` eller `ctx.log()` för att skicka notifikationer medan varje objekt behandlas. Detta skickar ett meddelande till klienten innan huvudresultatet är färdigt.
- **På klienten:** Implementera en meddelandehanterare som lyssnar efter och visar notifikationer när de kommer. Denna hanterare skiljer mellan notifikationer och slutresultatet.

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

## Säkerhetsaspekter

Säkerhet bör vara en hög prioritet när man implementerar vilken server som helst, särskilt när man använder HTTP-baserade transportprotokoll som Streamable HTTP i MCP.

När man implementerar MCP-servrar med HTTP-baserade transporter blir säkerheten ett avgörande bekymmer som kräver noggrann uppmärksamhet på flera attackvektorer och skyddsmekanismer.

### Översikt

Säkerheten är kritisk när MCP-servrar exponeras över HTTP. Streamable HTTP introducerar nya attackytor och kräver noggrann konfiguration.

Här är några nyckelaspekter för säkerheten:

- **Validering av Origin-header:** Validera alltid `Origin`-headern för att förhindra DNS-rebinding-attacker.
- **Bindning till localhost:** För lokal utveckling, bind servrar till `localhost` för att undvika exponering mot det offentliga nätet.
- **Autentisering:** Implementera autentisering (t.ex. API-nycklar, OAuth) för produktionsmiljöer.
- **CORS:** Konfigurera Cross-Origin Resource Sharing (CORS)-regler för att begränsa åtkomst.
- **HTTPS:** Använd HTTPS i produktion för att kryptera trafiken.

### Bästa praxis

Dessutom följer här några bästa metoder att uppfylla när du implementerar säkerheten i din MCP-strömmande server:

- Lita aldrig på inkommande förfrågningar utan validering.
- Logga och övervaka all åtkomst och fel.
- Uppdatera regelbundet beroenden för att åtgärda säkerhetssårbarheter.

### Utmaningar

Du kommer att möta vissa utmaningar när du implementerar säkerhet i MCP-strömmande servrar:

- Att balansera säkerhet med enkel utveckling
- Säkerställa kompatibilitet med olika klientmiljöer


## Uppgradering från SSE till Streamable HTTP

För applikationer som för närvarande använder Server-Sent Events (SSE) ger migrering till Streamable HTTP förbättrade möjligheter och bättre långsiktig hållbarhet för dina MCP-implementationer.

### Varför uppgradera?

Det finns två starka skäl att uppgradera från SSE till Streamable HTTP:

- Streamable HTTP erbjuder bättre skalbarhet, kompatibilitet och rikare notifikationsstöd än SSE.
- Det är den rekommenderade transporten för nya MCP-applikationer.

### Migreringssteg

Så här kan du migrera från SSE till Streamable HTTP i dina MCP-applikationer:

- **Uppdatera serverkoden** till att använda `transport="streamable-http"` i `mcp.run()`.
- **Uppdatera klientkoden** till att använda `streamablehttp_client` istället för SSE-klient.
- **Implementera en meddelandehanterare** i klienten för att behandla notifikationer.
- **Testa kompatibilitet** med befintliga verktyg och arbetsflöden.

### Behålla kompatibilitet

Det rekommenderas att bibehålla kompatibilitet med befintliga SSE-klienter under migreringsprocessen. Här är några strategier:

- Du kan stödja både SSE och Streamable HTTP genom att köra båda transporterna på olika ändpunkter.
- Migrera klienter successivt till den nya transporten.

### Utmaningar

Se till att ta itu med följande utmaningar under migreringen:

- Säkerställa att alla klienter uppdateras
- Hantera skillnader i leverans av notifikationer

### Uppgift: Bygg din egen strömmande MCP-app

**Scenario:**
Bygg en MCP-server och klient där servern bearbetar en lista med objekt (t.ex. filer eller dokument) och skickar en notifikation för varje objekt som behandlas. Klienten ska visa varje notifikation när den kommer.

**Steg:**

1. Implementera ett serververktyg som bearbetar en lista och skickar notifikationer för varje objekt.
2. Implementera en klient med en meddelandehanterare för att visa notifikationer i realtid.
3. Testa din implementation genom att köra både server och klient och observera notifikationerna.

[Lösning](./solution/README.md)

## Vidare läsning & Vad händer härnäst?

För att fortsätta din resa med MCP-streaming och utöka din kunskap, ger denna sektion ytterligare resurser och föreslagna nästa steg för att bygga mer avancerade applikationer.

### Vidare läsning

- [Microsoft: Introduktion till HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS i ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Strömmande förfrågningar](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Vad händer härnäst?

- Försök bygga mer avancerade MCP-verktyg som använder streaming för realtidsanalys, chatt eller samarbetsredigering.
- Utforska integration av MCP-streaming med frontend-ramverk (React, Vue, etc.) för live UI-uppdateringar.
- Nästa: [Utnyttja AI Toolkit för VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->