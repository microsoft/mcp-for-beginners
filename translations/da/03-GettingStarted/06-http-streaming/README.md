# HTTPS Streaming med Model Context Protocol (MCP)

Dette kapitel giver en omfattende vejledning i implementering af sikker, skalerbar og realtidsstreaming med Model Context Protocol (MCP) ved brug af HTTPS. Det dækker motivationen for streaming, de tilgængelige transportmekanismer, hvordan man implementerer streambar HTTP i MCP, sikkerhedspraksis, migration fra SSE og praktisk vejledning til at bygge dine egne streaming MCP-applikationer.

> [!WARNING]
> Implementeringseksemplerne i denne lektion er målrettet **MCP Specification
> `2025-11-25`** og demonstrerer det ældre `initialize` handshake,
> `Mcp-Session-Id`, GET event stream og gendannelsesmodel. MCP `2026-07-28`
> fjerner disse funktioner. Nuværende Streamable HTTP-forespørgsler er selvstændige
> POST-forespørgsler med `MCP-Protocol-Version` og `Mcp-Method` headers samt
> `Mcp-Name` hvor påkrævet. Se
> [Hvad er ændret i MCP: Specifikation 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> før du bruger disse eksempler i en ny implementering.

## Transportmekanismer og Streaming i MCP

Dette afsnit udforsker de forskellige transportmekanismer tilgængelige i MCP og deres rolle i at muliggøre streamingfunktioner til realtidskommunikation mellem klienter og servere.

### Hvad er en Transportmekanisme?

En transportmekanisme definerer, hvordan data udveksles mellem klienten og serveren. MCP understøtter flere transporttyper, der passer til forskellige miljøer og krav:

- **stdio**: Standard input/output, egnet til lokale og CLI-baserede værktøjer. Simpel men ikke egnet til web eller cloud.
- **HTTP+SSE**: Den ældre fjerntransport, udfaset i MCP `2025-03-26`
    og erstattet af Streamable HTTP. Brug den ikke til nye implementeringer.
- **Streamable HTTP**: Moderne HTTP-baseret streamingtransport, der understøtter notifikationer og bedre skalerbarhed. Anbefales til de fleste produktions- og cloud-scenarier.

### Sammenligningstabel

Se sammenligningstabellen nedenfor for at forstå forskellene mellem disse transportmekanismer:

| Transport | Status | Notifikationer | Typisk anvendelse |
|---|---|---|---|
| stdio | Aktuel | Ja | Lokale underprocesser |
| HTTP+SSE | Udfaset | Ja | Ældre fjernimplementeringer |
| Streamable HTTP | Aktuel | Ja | Fjern- og cloudservere |

> **Tip:** Valget af den rigtige transport påvirker ydeevne, skalerbarhed og brugeroplevelse. **Streamable HTTP** anbefales til moderne, skalerbare og cloud-klare applikationer.

De standardtransporter, der anvendes, er stdio og Streamable HTTP. HTTP+SSE forekommer kun i
ældre eksempler.

## Streaming: Koncepter og Motivation

Forståelse af de grundlæggende koncepter og motivation bag streaming er afgørende for at implementere effektive realtidskommunikationssystemer.

**Streaming** er en teknik inden for netværksprogrammering, der tillader data at blive sendt og modtaget i små, håndterbare bidder eller som en række begivenheder, i stedet for at vente på, at hele svaret er klar. Dette er især nyttigt til:

- Store filer eller datasæt.
- Realtidsopdateringer (f.eks. chat, statusbjælker).
- Langvarige beregninger, hvor du ønsker at holde brugeren informeret.

Her er det, du skal vide om streaming på et overordnet niveau:

- Data leveres gradvist, ikke alt på én gang.
- Klienten kan behandle data, efterhånden som de ankommer.
- Reducerer opfattet latenstid og forbedrer brugeroplevelsen.

### Hvorfor bruge streaming?

Årsagerne til at bruge streaming er følgende:

- Brugere får øjeblikkelig feedback, ikke kun ved slutningen
- Muliggør realtidsapplikationer og responsive brugergrænseflader
- Mere effektiv udnyttelse af netværks- og computerressourcer

### Simpelt eksempel: HTTP Streaming Server & Klient

Her er et simpelt eksempel på, hvordan streaming kan implementeres:

#### Python

**Server (Python, brug af FastAPI og StreamingResponse):**

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

**Klient (Python, brug af requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Dette eksempel demonstrerer en server, der sender en række beskeder til klienten, efterhånden som de bliver tilgængelige, i stedet for at vente på, at alle beskeder er klar.

**Sådan fungerer det:**

- Serveren afgiver hver besked, når den er klar.
- Klienten modtager og udskriver hver del, når den ankommer.

**Krav:**

- Serveren skal bruge et streaming-svar (f.eks. `StreamingResponse` i FastAPI).
- Klienten skal behandle svaret som en streaming (`stream=True` i requests).
- Content-Type er normalt `text/event-stream` eller `application/octet-stream`.

#### Java

**Server (Java, brug af Spring Boot og Server-Sent Events):**

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

**Klient (Java, brug af Spring WebFlux WebClient):**

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

**Java Implementeringsnoter:**

- Bruger Spring Boots reaktive stak med `Flux` til streaming
- `ServerSentEvent` giver struktureret event-streaming med event-typer
- `WebClient` med `bodyToFlux()` muliggør reaktiv streamingforbrug
- `delayElements()` simulerer behandlingstid mellem events
- Events kan have typer (`info`, `result`) for bedre klienthåndtering

### Sammenligning: Klassisk Streaming vs MCP Streaming

Forskellene mellem, hvordan streaming fungerer på en "klassisk" måde versus hvordan det fungerer i MCP, kan illustreres således:

| Funktion                | Klassisk HTTP Streaming       | MCP Streaming (Notifikationer)   |
|------------------------|-------------------------------|---------------------------------|
| Hovedrespons            | Chunked                       | Én enkelt, til sidst            |
| Progressionsopdateringer| Sendes som data chunks         | Sendes som notifikationer       |
| Klientkrav              | Skal behandle stream          | Skal implementere beskedhandler |
| Anvendelsestilfælde     | Store filer, AI token streams | Fremdrift, logs, realtidsfeedback|

### Vigtigste Observerede Forskelle

Derudover er her nogle nøgleforskelle:

- **Kommunikationsmønster:**
  - Klassisk HTTP streaming: Bruger simpel chunked transfer encoding til at sende data i bidder
  - MCP streaming: Bruger et struktureret notifikationssystem med JSON-RPC protokol

- **Beskedformat:**
  - Klassisk HTTP: Almindelige tekstbidder med linjeskift
  - MCP: Strukturerede LoggingMessageNotification objekter med metadata

- **Klientimplementering:**
  - Klassisk HTTP: Simpel klient som behandler streaming-svar
  - MCP: Mere sofistikeret klient med en beskedhandler til at behandle forskellige beskedtyper

- **Progressionopdateringer:**
  - Klassisk HTTP: Progression er en del af hovedresponsen
  - MCP: Progression sendes via separate notifikationsbeskeder, mens hovedresponsen sendes til sidst

### Anbefalinger

Der er nogle ting, vi anbefaler, når det kommer til valg mellem implementering af klassisk streaming (som et endepunkt vist ovenfor med `/stream`) kontra streaming via MCP.

- **Til simple streamingbehov:** Klassisk HTTP streaming er enklere at implementere og tilstrækkeligt til grundlæggende streamingbehov.

- **Til komplekse, interaktive applikationer:** MCP streaming giver en mere struktureret tilgang med rigere metadata og adskillelse mellem notifikationer og endelige resultater.

- **Til AI-applikationer:** MCP’s notifikationssystem er særligt nyttigt til langvarige AI-opgaver, hvor du ønsker at holde brugere informeret om fremdrift.

## Streaming i MCP

Ok, så du har set nogle anbefalinger og sammenligninger indtil nu omkring forskellen mellem klassisk streaming og streaming i MCP. Lad os komme i detaljer med, hvordan du præcist kan udnytte streaming i MCP.

Forståelse af, hvordan streaming fungerer inden for MCP-rammen, er afgørende for at bygge responsive applikationer, der giver realtidsfeedback til brugere under langvarige operationer.

I MCP handler streaming ikke om at sende hovedresponsen i bidder, men om at sende **notifikationer** til klienten, mens et værktøj behandler en anmodning. Disse notifikationer kan inkludere fremdriftsopdateringer, logs eller andre begivenheder.

### Sådan fungerer det

Hovedresultatet sendes stadig som et enkelt svar. Notifikationer kan dog sendes som separate beskeder under behandlingen og dermed opdatere klienten i realtid. Klienten skal kunne håndtere og vise disse notifikationer.

### Valgfri øvelse: tilslut til en hostet MCP-server

Du kan også bruge Streamable HTTP uden at køre en lokal server. Dette eksempel
forbinder til [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
opdager dets værktøjer og søger efter offentlig MCP-dokumentation med den samme
Python SDK som [den lokale klient](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Parallels anonyme endepunkt kræver hverken konto eller API-nøgle. Gratis adgang er
ratebegrænset. Når du kører dette script, sendes søgeforespørgsler, mål og et
tilfældigt sessions-id til Parallel. Tjenesten tilbyder også `web_fetch`,
som sender anmodede URL'er og enhver angivet kontekst til Parallel. Brug offentlig
information til denne øvelse; se dens [vilkår](https://parallel.ai/customer-terms)
og [datapolitik](https://parallel.ai/privacy-policy).

Med Python 3.10 eller nyere og en aktiveret virtual environment, installer SDK'en:

```sh
python -m pip install "mcp>=1.10,<2"
```

Gem dette som `hosted_search.py` og kør `python hosted_search.py`:

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

Forvent, at opdagelsen inkluderer `web_search` og `web_fetch`, efterfulgt af en søgning
svar indeholdende kilde-URL'er og uddrag. Resultater kan variere eller være tomme.
Skriptet tjekker `isError` fordi et værktøj kan fejle, selv når HTTP-anmodningen
lykkes. Hvis adgang er ratebegrænset, vent før du prøver igen. Genbrug den samme
`session_id` hvis du udvider scriptet med relaterede søge- eller hentekald.

Streamable HTTP tillader både JSON- og SSE-svar; denne server kan returnere et
komplet JSON-resultat uden fremdriftsmeddelelser. SDK'en håndterer
transporten. Fortsæt med det lokale eksempel nedenfor for at lære om notifikationer.
Dette valgfrie script foretager en eksplicit søgning og lukker sin forbindelse, når
det afsluttes. Hvis du senere eksponerer disse værktøjer for en agent, kan agenten kalde
dem under sit arbejde; behandl hentet webtekst som utroværdige data.

## Hvad er en Notifikation?

Vi sagde "Notifikation", hvad betyder det i MCP-konteksten?

En notifikation er en JSON-RPC-besked, der ikke har en `id` og ikke
modtager et svar. MCP bruger notifikationer til fremdrift, annullering og
andre envejsbegivenheder.

I MCP `2025-11-25` sender en klient `notifications/initialized` efter
initialiserings-håndtryk. MCP `2026-07-28` har ikke noget initialiserings-håndtryk, så
denne notifikation er et gammelt adfærdsmønster.

En notifikation ser sådan ud som en JSON-besked:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Logging er en funktion, der bruger notifikationer; notifikationer er i sig selv en
generel JSON-RPC-beskedtype.

> **Udfaset i MCP `2026-07-28`:** Loggingfunktionen forbliver tilgængelig
> for kompatibilitet, men kan fjernes i den første specifikations-
> revision udgivet den 28. juli 2027 eller senere. Nye implementeringer bør bruge
> `stderr` med stdio eller OpenTelemetry til struktureret observerbarhed.

For en gammel `2025-11-25`-implementering aktiverer serveren Logging
kapabiliteten som følger:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Afhængig af hvilket SDK der bruges, kan logging være aktiveret som standard, eller du skal eksplicit aktivere det i din serverkonfiguration.

Der findes forskellige typer notifikationer:

| Niveau    | Beskrivelse                   | Eksempel på brug               |
|-----------|------------------------------|-------------------------------|
| debug     | Detaljeret fejlfindingsinfo   | Funktion ind-/udgangspunkter   |
| info      | Generelle informationsbeskeder| Fremdriftsopdateringer        |
| notice    | Normale men betydelige begivenheder | Konfigurationsændringer   |
| warning   | Advarselsbetingelser          | Brug af forældet funktion      |
| error     | Fejltilstande                 | Driftsfejl                    |
| critical  | Kritiske tilstande            | Systemkomponentfejl           |
| alert     | Handling skal udføres straks  | Data korruption opdaget        |
| emergency | Systemet er ubrugeligt        | Totalt systemnedbrud          |

## Implementering af notifikationer i MCP

For at implementere notifikationer i MCP skal du sætte både server- og klient-sider op til at håndtere realtidsopdateringer. Dette gør det muligt for din applikation at give øjeblikkelig feedback til brugere under langvarige operationer.

### Serverside: Afsendelse af notifikationer

Lad os starte med serversiden. I MCP definerer du værktøjer, der kan sende notifikationer, mens de behandler anmodninger. Serveren bruger kontekstobjektet (normalt `ctx`) til at sende beskeder til klienten.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

I det foregående eksempel sender `process_files`-værktøjet tre notifikationer til klienten, mens det behandler hver fil. `ctx.info()`-metoden bruges til at sende informationsbeskeder.

Derudover, for at aktivere notifikationer, skal du sikre, at din server bruger en streamingtransport (som `streamable-http`), og at din klient implementerer en beskedbehandler til at behandle notifikationer. Her er hvordan du kan opsætte serveren til at bruge `streamable-http`-transporten:

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

I dette .NET-eksempel er `ProcessFiles`-værktøjet dekoreret med `Tool`-attributten og sender tre notifikationer til klienten, mens det behandler hver fil. `ctx.Info()`-metoden bruges til at sende informationsbeskeder.

For at aktivere notifikationer i din .NET MCP-server skal du sikre, at du bruger en streamingtransport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klientside: Modtagelse af notifikationer

Klienten skal implementere en beskedbehandler til at behandle og vise notifikationer, efterhånden som de ankommer.

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

I den forrige kode kontrollerer funktionen `message_handler`, om den indkommende besked er en notifikation. Hvis det er tilfældet, udskriver den notifikationen; ellers behandler den den som en almindelig serverbesked. Bemærk også, hvordan `ClientSession` initialiseres med `message_handler` for at håndtere indkommende notifikationer.

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

I dette .NET-eksempel kontrollerer funktionen `MessageHandler`, om den indkommende besked er en notifikation. Hvis det er tilfældet, udskriver den notifikationen; ellers behandler den den som en almindelig serverbesked. `ClientSession` initialiseres med beskedhåndteringen via `ClientSessionOptions`.

For at aktivere notifikationer skal du sikre, at din server bruger en streamingtransport (som `streamable-http`), og at din klient implementerer en beskedhandler til at behandle notifikationer.

## Fremdriftsnotifikationer og scenarier

Dette afsnit forklarer konceptet med fremdriftsnotifikationer i MCP, hvorfor de er vigtige, og hvordan man implementerer dem ved hjælp af Streamable HTTP. Du vil også finde en praktisk opgave til at styrke din forståelse.

Fremdriftsnotifikationer er realtidsbeskeder, der sendes fra serveren til klienten under langvarige operationer. I stedet for at vente på, at hele processen er færdig, holder serveren klienten opdateret om den aktuelle status. Dette forbedrer gennemsigtighed, brugeroplevelse og gør fejlfinding lettere.

**Eksempel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Hvorfor bruge fremdriftsnotifikationer?

Fremdriftsnotifikationer er vigtige af flere grunde:

- **Bedre brugeroplevelse:** Brugere ser opdateringer, mens arbejdet skrider frem, ikke kun til sidst.
- **Realtidsfeedback:** Klienter kan vise fremdriftsbjælker eller logfiler, hvilket gør appen mere responsiv.
- **Nemmere fejlfinding og overvågning:** Udviklere og brugere kan se, hvor en proces muligvis er langsom eller sidder fast.

### Hvordan implementeres fremdriftsnotifikationer

Sådan kan du implementere fremdriftsnotifikationer i MCP:

- **På serveren:** Brug `ctx.info()` eller `ctx.log()` til at sende notifikationer, efterhånden som hvert element behandles. Dette sender en besked til klienten, før hovedresultatet er klart.
- **På klienten:** Implementer en beskedhandler, der lytter efter og viser notifikationer, når de ankommer. Denne handler skelner mellem notifikationer og det endelige resultat.

**Servereksempel:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Klienteksempel:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Sikkerhedsovervejelser

Sikkerhed bør være en topprioritet, når du implementerer enhver server, især når du bruger HTTP-baserede transports som Streamable HTTP i MCP.

Når du implementerer MCP-servere med HTTP-baserede transports, bliver sikkerhed en altafgørende bekymring, der kræver omhyggelig opmærksomhed på flere angrebsvektorer og beskyttelsesmekanismer.

### Oversigt

Sikkerhed er kritisk, når MCP-servere eksponeres over HTTP. Streamable HTTP introducerer nye angrebsoverflader og kræver omhyggelig konfiguration.

Her er nogle vigtige sikkerhedsovervejelser:

- **Validering af Origin-header:** Valider altid `Origin`-headeren for at forhindre DNS-rebinding-angreb.
- **Binding til localhost:** Til lokal udvikling, bind servere til `localhost` for at undgå, at de eksponeres til det offentlige internet.
- **Autentifikation:** Implementer autentifikation (f.eks. API-nøgler, OAuth) til produktionsmiljøer.
- **CORS:** Konfigurer Cross-Origin Resource Sharing (CORS) politikker for at begrænse adgang.
- **HTTPS:** Brug HTTPS i produktion for at kryptere trafik.

### Bedste praksis

Derudover er her nogle bedste praksisser at følge, når du implementerer sikkerhed i din MCP streaming-server:

- Stol aldrig på indkommende forespørgsler uden validering.
- Log og overvåg al adgang og fejl.
- Opdater regelmæssigt afhængigheder for at lukke sikkerhedshuller.

### Udfordringer

Du vil møde nogle udfordringer, når du implementerer sikkerhed i MCP streaming-servere:

- Balancering af sikkerhed med udviklingsvenlighed
- Sikring af kompatibilitet med forskellige klientmiljøer


## Opgradering fra SSE til Streamable HTTP

For applikationer, der aktuelt bruger Server-Sent Events (SSE), giver migrering til Streamable HTTP forbedrede muligheder og bedre langsigtet bæredygtighed for dine MCP-implementeringer.

### Hvorfor opgradere?

Der er to overbevisende grunde til at opgradere fra SSE til Streamable HTTP:

- Streamable HTTP tilbyder bedre skalerbarhed, kompatibilitet og rigere notifikationssupport end SSE.
- Det er den anbefalede transport for nye MCP-applikationer.

### Trin for migrering

Sådan kan du migrere fra SSE til Streamable HTTP i dine MCP-applikationer:

- **Opdater serverkoden** til at bruge `transport="streamable-http"` i `mcp.run()`.
- **Opdater klientkoden** til at bruge `streamablehttp_client` i stedet for SSE-klienten.
- **Implementer en beskedhandler** i klienten til at behandle notifikationer.
- **Test for kompatibilitet** med eksisterende værktøjer og arbejdsgange.

### Opretholdelse af kompatibilitet

Det anbefales at opretholde kompatibilitet med eksisterende SSE-klienter under migreringsprocessen. Her er nogle strategier:

- Du kan understøtte både SSE og Streamable HTTP ved at køre begge transports på forskellige endepunkter.
- Migrer gradvist klienter til den nye transport.

### Udfordringer

Sørg for at adressere følgende udfordringer under migrering:

- At sikre, at alle klienter opdateres
- Håndtering af forskelle i notifikationslevering

### Opgave: Byg din egen streaming MCP-app

**Scenario:**
Byg en MCP-server og -klient, hvor serveren behandler en liste af elementer (f.eks. filer eller dokumenter) og sender en notifikation for hvert behandlede element. Klienten skal vise hver notifikation, efterhånden som den ankommer.

**Trin:**

1. Implementer et serverværktøj, der behandler en liste og sender notifikationer for hvert element.
2. Implementer en klient med en beskedhandler, der viser notifikationer i realtid.
3. Test din implementering ved at køre både server og klient og observere notifikationerne.

[Løsning](./solution/README.md)

## Yderligere læsning og hvad nu?

For at fortsætte din rejse med MCP streaming og udvide din viden, tilbyder dette afsnit yderligere ressourcer og foreslåede næste skridt til at bygge mere avancerede applikationer.

### Yderligere læsning

- [Microsoft: Introduktion til HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS i ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Hvad nu?

- Prøv at bygge mere avancerede MCP-værktøjer, der bruger streaming til realtidsanalyse, chat eller samarbejdende redigering.
- Udforsk integration af MCP streaming med frontend-rammer (React, Vue osv.) for live UI-opdateringer.
- Næste: [Brug af Microsoft Foundry Toolkit til Visual Studio Code](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->