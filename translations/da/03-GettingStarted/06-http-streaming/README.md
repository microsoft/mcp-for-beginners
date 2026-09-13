# HTTPS Streaming med Model Context Protocol (MCP)

Dette kapitel giver en omfattende guide til implementering af sikker, skalerbar og realtids streaming med Model Context Protocol (MCP) ved hjælp af HTTPS. Det dækker motivationen for streaming, de tilgængelige transportmekanismer, hvordan man implementerer streambart HTTP i MCP, sikkerhedspraksis, migration fra SSE, og praktisk vejledning til at bygge dine egne streaming MCP applikationer.

> [!WARNING]
> Implementeringseksemplerne i denne lektion retter sig mod **MCP-specifikationen
> `2025-11-25`** og demonstrerer det legacy `initialize` handshake,
> `Mcp-Session-Id`, GET event stream og genoptagelsesmodellen. MCP `2026-07-28`
> fjerner disse funktioner. Nuvarande Streamable HTTP-forespørgsler er selvstændige
> POST-forespørgsler med `MCP-Protocol-Version` og `Mcp-Method` headers, plus
> `Mcp-Name` hvor det kræves. Se
> [Ændringer i MCP: Specifikationen 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> før du bruger disse eksempler i en ny implementering.

## Transportmekanismer og Streaming i MCP

Denne sektion udforsker de forskellige transportmekanismer tilgængelige i MCP og deres rolle i at muliggøre streamingfunktioner for realtidskommunikation mellem klienter og servere.

### Hvad er en Transportmekanisme?

En transportmekanisme definerer, hvordan data udveksles mellem klient og server. MCP understøtter flere transporttyper for at passe til forskellige miljøer og krav:

- **stdio**: Standard input/output, egnet til lokale og CLI-baserede værktøjer. Simpelt men ikke egnet til web eller cloud.
- **HTTP+SSE**: Den legacy fjerntransport, udfaset i MCP `2025-03-26`
    og erstattet af Streamable HTTP. Brug det ikke til nye implementeringer.
- **Streamable HTTP**: Moderne HTTP-baseret streamingtransport, understøtter notifikationer og bedre skalerbarhed. Anbefalet til de fleste produktions- og cloud-scenarier.

### Sammenligningstabel

Se på sammenligningstabellen nedenfor for at forstå forskellene mellem disse transportmekanismer:

| Transport | Status | Notifikationer | Typisk brug |
|---|---|---|---|
| stdio | Aktuel | Ja | Lokale underprocesser |
| HTTP+SSE | Udfaset | Ja | Legacy fjernimplementeringer |
| Streamable HTTP | Aktuel | Ja | Fjerne og cloud-servere |

> **Tip:** Valg af den rigtige transport påvirker ydelse, skalerbarhed og brugeroplevelse. **Streamable HTTP** anbefales til moderne, skalerbare og cloud-klar applikationer.

Standardtransporterne er stdio og Streamable HTTP. HTTP+SSE forekommer kun i
ældre eksempler.

## Streaming: Begreber og Motivation

Forståelse af de grundlæggende begreber og motivation bag streaming er essentielt for at implementere effektive realtidskommunikationssystemer.

**Streaming** er en teknik inden for netværksprogrammering, der tillader data at sendes og modtages i små, håndterbare bidder eller som en række af hændelser, i stedet for at vente på, at hele svaret er klar. Dette er især nyttigt for:

- Store filer eller datasæt.
- Real-time opdateringer (f.eks. chat, fremdriftsbjælker).
- Langvarige beregninger, hvor du ønsker at holde brugeren informeret.

Her er hvad du behøver at vide om streaming på et overordnet plan:

- Data leveres progressivt, ikke alt på én gang.
- Klienten kan behandle data, efterhånden som det ankommer.
- Reducerer oplevet forsinkelse og forbedrer brugeroplevelsen.

### Hvorfor bruge streaming?

Grunde til at bruge streaming er følgende:

- Brugere får feedback med det samme, ikke kun til sidst
- Muliggør realtidsapplikationer og responsive brugerflader
- Mere effektiv brug af netværks- og computerressourcer

### Simpelt eksempel: HTTP Streaming Server & Klient

Her er et simpelt eksempel på, hvordan streaming kan implementeres:

#### Python

**Server (Python, med FastAPI og StreamingResponse):**

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

Dette eksempel demonstrerer en server, der sender en serie beskeder til klienten, efterhånden som de bliver tilgængelige, i stedet for at vente, til alle beskeder er klar.

**Hvordan det virker:**

- Serveren sender hver besked, når den er klar.
- Klienten modtager og printer hver bid, efterhånden som den ankommer.

**Krav:**

- Serveren skal bruge et streaming-svar (f.eks. `StreamingResponse` i FastAPI).
- Klienten skal behandle svaret som en stream (`stream=True` i requests).
- Content-Type er normalt `text/event-stream` eller `application/octet-stream`.

#### Java

**Server (Java, med Spring Boot og Server-Sent Events):**

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

**Java implementeringsnoter:**

- Bruger Spring Boots reactive stack med `Flux` til streaming
- `ServerSentEvent` leverer struktureret event streaming med event-typer
- `WebClient` med `bodyToFlux()` muliggør reaktiv streaming-forbrug
- `delayElements()` simulerer behandlingstid mellem events
- Events kan have typer (`info`, `result`) for bedre klienthåndtering

### Sammenligning: Klassisk streaming vs MCP Streaming

Forskellene mellem, hvordan streaming fungerer på en "klassisk" måde versus hvordan det fungerer i MCP kan beskrives sådan:

| Funktion                | Klassisk HTTP Streaming        | MCP Streaming (Notifikationer)  |
|------------------------|-------------------------------|---------------------------------|
| Hovedsvar              | Opdelt i bidder               | Én gang til sidst               |
| Fremdriftsopdateringer | Sendes som datastykker         | Sendes som notifikationer       |
| Klientkrav             | Skal behandle stream          | Skal implementere beskedshåndtering |
| Brugsscenarie          | Store filer, AI token streams | Fremdrift, logs, realtids feedback|

### Centrale observerede forskelle

Derudover er her nogle nøgleforskelle:

- **Kommunikationsmønster:**
  - Klassisk HTTP streaming: Bruger simpel chunked transfer encoding til at sende data i bidder
  - MCP streaming: Bruger et struktureret notifikationssystem med JSON-RPC protokol

- **Beskedformat:**
  - Klassisk HTTP: Almindelige tekstbidder med nye linjer
  - MCP: Strukturerede LoggingMessageNotification objekter med metadata

- **Klientimplementering:**
  - Klassisk HTTP: Simpel klient, der behandler streaming-svar
  - MCP: Mere sofistikeret klient med beskedshåndtering til at bearbejde forskellige typer beskeder

- **Fremdriftsopdateringer:**
  - Klassisk HTTP: Fremdriften er del af hovedstrømmen
  - MCP: Fremdrift sendes via separate notifikationsbeskeder, mens hovedsvaret kommer til sidst

### Anbefalinger

Der er nogle ting, vi anbefaler, når det kommer til valg mellem at implementere klassisk streaming (som et endpoint, vi viste ovenfor med `/stream`) versus at vælge streaming via MCP.

- **For simple streamingbehov:** Klassisk HTTP streaming er nemmere at implementere og tilstrækkelig til basale streamingbehov.

- **For komplekse, interaktive applikationer:** MCP streaming giver en mere struktureret tilgang med rigere metadata og adskillelse mellem notifikationer og endelige resultater.

- **For AI-applikationer:** MCP’s notifikationssystem er særligt nyttigt for langvarige AI-opgaver, hvor du ønsker at holde brugerne informeret om fremskridt.

## Streaming i MCP

Ok, så du har set nogle anbefalinger og sammenligninger om forskellen mellem klassisk streaming og streaming i MCP. Lad os gå i detaljen med, hvordan du præcist kan udnytte streaming i MCP.

Forståelse af, hvordan streaming fungerer inden for MCP-rammen, er essentiel for at bygge responsive applikationer, der giver realtidsfeedback til brugere under langvarige processer.

I MCP handler streaming ikke om at sende hovedsvaret i bidder, men om at sende **notifikationer** til klienten, mens et værktøj behandler en forespørgsel. Disse notifikationer kan indeholde fremdriftsopdateringer, logs eller andre hændelser.

### Hvordan det virker

Hovedresultatet sendes stadig som et enkelt svar. Notifikationer kan dog sendes som separate beskeder under behandlingen og dermed opdatere klienten i realtid. Klienten skal kunne håndtere og vise disse notifikationer.

### Valgfrit øvelse: forbind til en hostet MCP-server

Du kan også bruge Streamable HTTP uden at køre en lokal server. Dette eksempel
forbinder til [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
finder dets værktøjer og søger efter offentlig MCP-dokumentation ved hjælp af samme
Python SDK som den [lokale klient](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Parallels anonyme endpoint kræver ingen konto eller API-nøgle. Gratis adgang er
ratebegrænset. Kørsel af dette script sender søgeforespørgsler, mål og en
tilfældig sessions-id til Parallel. Tjenesten tilbyder også `web_fetch`,
som sender anmodede URL’er og enhver leveret kontekst til Parallel. Brug offentlig
information til denne øvelse; se dens [vilkår](https://parallel.ai/customer-terms)
og [privatlivspolitik](https://parallel.ai/privacy-policy).

Med Python 3.10 eller nyere og et aktivt virtuelt miljø, installer SDK’en:

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

Forvent, at discovery inkluderer `web_search` og `web_fetch`, efterfulgt af et søgerespons
indeholdende kilde-URL’er og uddrag. Resultater kan variere eller være tomme.
Scriptet tjekker `isError`, fordi et værktøj kan fejle, selv om HTTP-forespørgslen
lykkes. Hvis adgangen er ratebegrænset, vent før du prøver igen. Genbrug samme
`session_id`, hvis du udvider scriptet med relaterede søge- eller fetch-kald.

Streamable HTTP tillader både JSON- og SSE-svar; denne server kan returnere et
komplet JSON-resultat uden fremdriftsnotifikationer. SDK’en håndterer
transporten. Fortsæt med det lokale eksempel nedenfor for at lære om notifikationer.
Dette valgfrie script laver en eksplicit søgning og lukker forbindelsen, når
den er færdig. Hvis du senere udsætter disse værktøjer til en agent, kan agenten kalde
dem under sit arbejde; behandl hentet webtekst som utroværdige data.

## Hvad er en Notifikation?

Vi sagde "Notifikation", hvad betyder det i MCP-kontekst?

En notifikation er en JSON-RPC besked, der ikke har et `id` og ikke
modtager et svar. MCP bruger notifikationer til fremdrift, afbrydelse og
andre envejs-hændelser.

I MCP `2025-11-25` sender en klient `notifications/initialized` efter
initialiseringshandshaket. MCP `2026-07-28` har intet initialiseringshandshake, så
denne notifikation er legacy-adfærd.

En notifikation ser således ud som en JSON-besked:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Logging er en funktion, der bruger notifikationer; notifikationer i sig selv er en
generel JSON-RPC beskedtype.

> **Udfaset i MCP `2026-07-28`:** Logging-funktionen forbliver tilgængelig
> for kompatibilitet, men kan fjernes i den første specifikationsrevision
> udgivet den 28. juli 2027 eller senere. Nye implementeringer bør bruge
> `stderr` med stdio eller OpenTelemetry for struktureret observabilitet.

For en legacy `2025-11-25` implementering aktiverer serveren Logging
funktionen som følger:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Afhængigt af SDK’en kan logging være aktiveret som standard, eller du skal eksplicit aktivere det i din serverkonfiguration.

Der findes forskellige typer notifikationer:

| Niveau     | Beskrivelse                    | Eksempelbrug                  |
|-----------|-------------------------------|------------------------------|
| debug     | Detaljeret fejlfinding          | Funktion indgang/udgang       |
| info      | Generelle informationsbeskeder  | Fremdriftsopdateringer         |
| notice    | Normale, men væsentlige hændelser| Konfigurationsændringer       |
| warning   | Advarselsbetingelser           | Brug af forældet funktion     |
| error     | Fejlbetingelser                | Driftsfejl                   |
| critical  | Kritiske betingelser           | Systemkomponentfejl           |
| alert     | Handling skal udføres øjeblikkeligt | Data korruption opdaget     |
| emergency | Systemet er ubrugeligt          | Total systemfejl             |

## Implementering af Notifikationer i MCP

For at implementere notifikationer i MCP skal du sætte både server- og klientsiden op til at håndtere realtidsopdateringer. Dette tillader din applikation at give øjeblikkelig feedback til brugere under langvarige processer.

### Serverside: Afsendelse af Notifikationer

Lad os starte med serversiden. I MCP definerer du værktøjer, der kan sende notifikationer under behandlingen af forespørgsler. Serveren bruger kontekstobjektet (normalt `ctx`) til at sende beskeder til klienten.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

I det foregående eksempel sender `process_files` værktøjet tre notifikationer til klienten, efterhånden som det behandler hver fil. Metoden `ctx.info()` bruges til at sende informationsbeskeder.

Derudover, for at aktivere notifikationer, sørg for, at din server bruger en streamingtransport (som `streamable-http`) og at din klient implementerer en beskedshåndtering for at behandle notifikationer. Her er hvordan du kan sætte serveren op til at bruge `streamable-http` transport:

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

I dette .NET eksempel er `ProcessFiles` værktøjet dekoreret med attributten `Tool` og sender tre notifikationer til klienten, mens hver fil behandles. Metoden `ctx.Info()` bruges til at sende informationsbeskeder.

For at aktivere notifikationer i din .NET MCP-server, sørg for du bruger en streamingtransport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klientside: Modtagelse af Notifikationer

Klienten skal implementere en beskedshåndtering for at behandle og vise notifikationer, når de ankommer.

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

I den foregående kode tjekker funktionen `message_handler`, om den indkommende besked er en notifikation. Hvis den er det, printer den notifikationen; ellers behandles den som en almindelig serverbesked. Bemærk også, hvordan `ClientSession` initialiseres med `message_handler` til at håndtere indkommende notifikationer.

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


I dette .NET-eksempel kontrollerer funktionen `MessageHandler`, om den indkommende besked er en notifikation. Hvis det er tilfældet, udskriver den notifikationen; ellers behandler den den som en almindelig serverbesked. `ClientSession` initialiseres med beskedhandleren via `ClientSessionOptions`.

For at aktivere notifikationer, skal du sikre, at din server bruger en streaming-transport (som `streamable-http`), og at din klient implementerer en beskedhandler til at behandle notifikationer.

## Statusnotifikationer & Scenarier

Dette afsnit forklarer konceptet med statusnotifikationer i MCP, hvorfor de er vigtige, og hvordan man implementerer dem ved hjælp af Streamable HTTP. Du finder også en praktisk opgave til at styrke din forståelse.

Statusnotifikationer er realtidsbeskeder sendt fra serveren til klienten under langvarige operationer. I stedet for at vente på, at hele processen er færdig, holder serveren klienten opdateret om den aktuelle status. Dette forbedrer gennemsigtigheden, brugeroplevelsen og gør fejlfinding nemmere.

**Eksempel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Hvorfor bruge statusnotifikationer?

Statusnotifikationer er vigtige af flere grunde:

- **Bedre brugeroplevelse:** Brugerne ser opdateringer, mens arbejdet skrider frem, ikke kun til sidst.
- **Realtidsfeedback:** Klienter kan vise statuslinjer eller logs, hvilket gør appen mere responsiv.
- **Lettere fejlfinding og overvågning:** Udviklere og brugere kan se, hvor en proces eventuelt er langsom eller hænger.

### Sådan implementeres statusnotifikationer

Sådan kan du implementere statusnotifikationer i MCP:

- **På serveren:** Brug `ctx.info()` eller `ctx.log()` til at sende notifikationer, efterhånden som hvert element behandles. Dette sender en besked til klienten, før hovedresultatet er klar.
- **På klienten:** Implementer en beskedhandler, der lytter efter og viser notifikationer, efterhånden som de modtages. Denne handler skelner mellem notifikationer og det endelige resultat.

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

Sikkerhed bør være en høj prioritet ved implementering af enhver server, især når der bruges HTTP-baserede transportmetoder som Streamable HTTP i MCP.

Når man implementerer MCP-servere med HTTP-baserede transportmetoder, bliver sikkerhed en altafgørende bekymring, der kræver nøje opmærksomhed på flere angrebsvinkler og beskyttelsesmekanismer.

### Oversigt

Sikkerhed er kritisk, når MCP-servere eksponeres over HTTP. Streamable HTTP introducerer nye angrebsoverflader og kræver omhyggelig konfiguration.

Her er nogle vigtige sikkerhedsovervejelser:

- **Validering af Origin-header:** Valider altid `Origin`-headeren for at forhindre DNS rebinding-angreb.
- **Lokalt binding:** Til lokal udvikling bind servere til `localhost` for at undgå eksponering mod det offentlige internet.
- **Autentificering:** Implementer autentificering (fx API-nøgler, OAuth) til produktionsmiljøer.
- **CORS:** Konfigurer Cross-Origin Resource Sharing (CORS)-politikker for at begrænse adgang.
- **HTTPS:** Brug HTTPS i produktion til at kryptere trafikken.

### Bedste praksis

Herudover er der nogle bedste praksis at følge ved implementering af sikkerhed i din MCP streaming-server:

- Stol aldrig på indkommende forespørgsler uden validering.
- Log og overvåg al adgang og fejl.
- Opdater regelmæssigt afhængigheder for at lukke sikkerhedshuller.

### Udfordringer

Du vil støde på nogle udfordringer ved implementering af sikkerhed i MCP streaming-servere:

- Afvejning mellem sikkerhed og udviklingsvenlighed
- Sikring af kompatibilitet med forskellige klientmiljøer


## Opgradering fra SSE til Streamable HTTP

For applikationer, der i øjeblikket bruger Server-Sent Events (SSE), giver en migration til Streamable HTTP forbedrede muligheder og bedre langsigtet bæredygtighed for dine MCP-implementeringer.

### Hvorfor opgradere?

Der er to væsentlige grunde til at opgradere fra SSE til Streamable HTTP:

- Streamable HTTP tilbyder bedre skalerbarhed, kompatibilitet og rigere notifikationssupport end SSE.
- Det er den anbefalede transport for nye MCP-applikationer.

### Migreringstrin

Sådan kan du migrere fra SSE til Streamable HTTP i dine MCP-applikationer:

- **Opdater serverkode** til at bruge `transport="streamable-http"` i `mcp.run()`.
- **Opdater klientkode** til at bruge `streamablehttp_client` i stedet for SSE-klient.
- **Implementer en beskedhandler** i klienten til at behandle notifikationer.
- **Test for kompatibilitet** med eksisterende værktøjer og arbejdsgange.

### Opretholdelse af kompatibilitet

Det anbefales at opretholde kompatibilitet med eksisterende SSE-klienter under migrationsprocessen. Her er nogle strategier:

- Du kan støtte både SSE og Streamable HTTP ved at køre begge transportmuligheder på forskellige endpoints.
- Migrer gradvist klienter til den nye transport.

### Udfordringer

Sørg for at håndtere følgende udfordringer under migrationen:

- Sikring af, at alle klienter opdateres
- Håndtering af forskelle i notifikationslevering

### Opgave: Byg din egen streaming MCP-app

**Scenario:**
Byg en MCP-server og -klient, hvor serveren behandler en liste af elementer (f.eks. filer eller dokumenter) og sender en notifikation for hvert behandlede element. Klienten skal vise hver notifikation, efterhånden som den modtages.

**Trin:**

1. Implementer et serverværktøj, der behandler en liste og sender notifikationer for hvert element.
2. Implementer en klient med en beskedhandler til at vise notifikationer i realtid.
3. Test din implementering ved at køre både server og klient og observere notifikationerne.

[Solution](./solution/README.md)

## Yderligere læsning & Hvad så nu?

For at fortsætte din rejse med MCP streaming og udvide din viden, giver dette afsnit ekstra ressourcer og foreslåede næste skridt til at bygge mere avancerede applikationer.

### Yderligere læsning

- [Microsoft: Introduktion til HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS i ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Hvad så nu?

- Prøv at bygge mere avancerede MCP-værktøjer, der bruger streaming til realtidsanalyse, chat eller samarbejdende redigering.
- Undersøg integration af MCP streaming med frontend-rammer (React, Vue osv.) for live UI-opdateringer.
- Næste: [Udnyttelse af AI Toolkit til VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->