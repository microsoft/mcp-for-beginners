# HTTPS Streaming med Model Context Protocol (MCP)

Dette kapitel giver en omfattende vejledning i at implementere sikker, skalerbar og realtidsstreaming med Model Context Protocol (MCP) ved hjælp af HTTPS. Det dækker motivationen for streaming, de tilgængelige transportmekanismer, hvordan man implementerer streambart HTTP i MCP, sikkerhedsprincipper, migration fra SSE og praktisk vejledning til at bygge dine egne MCP-streamingapplikationer.

## Transportmekanismer og streaming i MCP

Denne sektion udforsker de forskellige transportmekanismer, der er tilgængelige i MCP, og deres rolle i at muliggøre streamingfunktioner til realtidskommunikation mellem klienter og servere.

### Hvad er en transportmekanisme?

En transportmekanisme definerer, hvordan data udveksles mellem klient og server. MCP understøtter flere transporttyper for at imødekomme forskellige miljøer og krav:

- **stdio**: Standard input/output, velegnet til lokale og CLI-baserede værktøjer. Simpelt, men ikke egnet til web eller cloud.
- **SSE (Server-Sent Events)**: Tillader servere at sende realtidsopdateringer til klienter over HTTP. Godt til web-UI'er, men begrænset i skalerbarhed og fleksibilitet.
- **Streambart HTTP**: Moderne HTTP-baseret streamingtransport, der understøtter notifikationer og bedre skalerbarhed. Anbefales til de fleste produktions- og cloud-scenarier.

### Sammenligningstabel

Se sammenligningstabellen nedenfor for at forstå forskellene mellem disse transportmekanismer:

| Transport         | Realtidsopdateringer | Streaming | Skalerbarhed | Anvendelsesscenarie     |
|-------------------|----------------------|-----------|--------------|-------------------------|
| stdio             | Nej                  | Nej        | Lav          | Lokale CLI-værktøjer    |
| SSE               | Ja                   | Ja         | Medium       | Web, realtidsopdateringer |
| Streambart HTTP   | Ja                   | Ja         | Høj          | Cloud, multi-klient      |

> **Tip:** Valget af den rigtige transport påvirker ydeevne, skalerbarhed og brugeroplevelse. **Streambart HTTP** anbefales til moderne, skalerbare og cloud-klare applikationer.

Bemærk transporterne stdio og SSE, som blev gennemgået i de tidligere kapitler, og hvordan streambart HTTP er den transport, der dækkes i dette kapitel.

## Streaming: Koncepter og motivation

At forstå de grundlæggende koncepter og motivationen bag streaming er afgørende for at implementere effektive realtidskommunikationssystemer.

**Streaming** er en teknik inden for netværksprogrammering, der gør det muligt at sende og modtage data i små, håndterbare bidder eller som en sekvens af hændelser, i stedet for at vente på, at hele svaret er klar. Dette er især nyttigt til:

- Store filer eller datasæt.
- Realtidsopdateringer (f.eks. chat, statusbjælker).
- Langvarige beregninger, hvor man ønsker at holde brugeren informeret.

Her er, hvad du skal vide om streaming på et højt niveau:

- Data leveres gradvist, ikke alt på én gang.
- Klienten kan behandle data, efterhånden som de ankommer.
- Reducerer opfattet ventetid og forbedrer brugeroplevelsen.

### Hvorfor bruge streaming?

Årsagerne til at bruge streaming er følgende:

- Brugere får øjeblikkelig feedback, ikke kun til sidst.
- Muliggør realtidsapplikationer og responsive brugergrænseflader.
- Mere effektiv brug af netværks- og computerressourcer.

### Simpelt eksempel: HTTP-streaming server og klient

Her er et simpelt eksempel på, hvordan streaming kan implementeres:

#### Python

**Server (Python, ved hjælp af FastAPI og StreamingResponse):**

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

**Klient (Python, ved hjælp af requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Dette eksempel demonstrerer en server, der sender en række beskeder til klienten, efterhånden som de bliver tilgængelige, i stedet for at vente på, at alle beskeder er klar.

**Sådan fungerer det:**

- Serveren leverer hver besked, når den er klar.
- Klienten modtager og udskriver hver del, efterhånden som den ankommer.

**Krav:**

- Serveren skal bruge et streamingrespons (f.eks. `StreamingResponse` i FastAPI).
- Klienten skal behandle svaret som en stream (`stream=True` i requests).
- Content-Type er normalt `text/event-stream` eller `application/octet-stream`.

#### Java

**Server (Java, ved hjælp af Spring Boot og Server-Sent Events):**

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

**Klient (Java, ved hjælp af Spring WebFlux WebClient):**

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

**Bemærkninger til Java-implementering:**

- Bruger Spring Boots reaktive stack med `Flux` til streaming.
- `ServerSentEvent` giver struktureret hændelsesstreaming med hændelsestyper.
- `WebClient` med `bodyToFlux()` muliggør reaktiv streamingforbrug.
- `delayElements()` simulerer behandlingstid mellem hændelser.
- Hændelser kan have typer (`info`, `result`) for bedre klienthåndtering.

### Sammenligning: Klassisk streaming vs MCP-streaming

Forskellene mellem, hvordan streaming fungerer på en "klassisk" måde, og hvordan det fungerer i MCP, kan beskrives som følger:

| Funktion              | Klassisk HTTP-streaming        | MCP-streaming (notifikationer)     |
|-----------------------|-------------------------------|------------------------------------|
| Hovedrespons          | Chunked                       | Enkel, til sidst                   |
| Fremskridtsopdateringer | Sendt som databidder         | Sendt som notifikationer           |
| Klientkrav            | Skal behandle stream          | Skal implementere beskedhåndtering |
| Anvendelsesscenarie   | Store filer, AI-tokenstreams  | Fremskridt, logs, realtidsfeedback |

### Observerede nøgleforskelle

Yderligere nøgleforskelle inkluderer:

- **Kommunikationsmønster:**
  - Klassisk HTTP-streaming: Bruger simpel chunked transfer encoding til at sende data i bidder.
  - MCP-streaming: Bruger et struktureret notifikationssystem med JSON-RPC-protokol.

- **Beskedformat:**
  - Klassisk HTTP: Almindelige tekstbidder med linjeskift.
  - MCP: Strukturerede LoggingMessageNotification-objekter med metadata.

- **Klientimplementering:**
  - Klassisk HTTP: Simpel klient, der behandler streamingresponser.
  - MCP: Mere sofistikeret klient med en beskedhåndtering til at behandle forskellige typer beskeder.

- **Fremskridtsopdateringer:**
  - Klassisk HTTP: Fremskridtet er en del af hovedstreamen.
  - MCP: Fremskridt sendes via separate notifikationsbeskeder, mens hovedsvaret kommer til sidst.

### Anbefalinger

Her er nogle anbefalinger, når det gælder valget mellem at implementere klassisk streaming (som et endpoint vi viste dig ovenfor ved brug af `/stream`) og at vælge streaming via MCP.

- **Til simple streamingbehov:** Klassisk HTTP-streaming er lettere at implementere og tilstrækkelig til basale streamingbehov.
- **Til komplekse, interaktive applikationer:** MCP-streaming giver en mere struktureret tilgang med rigere metadata og adskillelse mellem notifikationer og endelige resultater.
- **Til AI-applikationer:** MCP's notifikationssystem er særligt nyttigt til langvarige AI-opgaver, hvor du vil holde brugerne informeret om fremskridt.

## Streaming i MCP

Okay, så du har set nogle anbefalinger og sammenligninger indtil videre om forskellen mellem klassisk streaming og streaming i MCP. Lad os gå i detaljer med, hvordan du kan udnytte streaming i MCP.

At forstå, hvordan streaming fungerer inden for MCP-rammen, er afgørende for at bygge responsive applikationer, der giver realtidsfeedback til brugerne under langvarige operationer.

I MCP handler streaming ikke om at sende hovedsvaret i bidder, men om at sende **notifikationer** til klienten, mens et værktøj behandler en anmodning. Disse notifikationer kan inkludere fremskridtsopdateringer, logs eller andre hændelser.

### Hvordan det fungerer

Hovedresultatet sendes stadig som et enkelt svar. Notifikationer kan dog sendes som separate beskeder under behandlingen og dermed opdatere klienten i realtid. Klienten skal kunne håndtere og vise disse notifikationer.

## Hvad er en notifikation?

Vi nævnte "notifikation", men hvad betyder det i MCP's kontekst?

En notifikation er en besked sendt fra serveren til klienten for at informere om fremskridt, status eller andre hændelser under en langvarig operation. Notifikationer forbedrer gennemsigtighed og brugeroplevelse.

For eksempel skal en klient sende en notifikation, når den indledende håndtryk med serveren er udført.

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

Notifikationer hører til et emne i MCP kaldet ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

For at få logging til at fungere skal serveren aktivere det som en funktion/kapabilitet som følger:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Afhængigt af den anvendte SDK kan logging være aktiveret som standard, eller du skal muligvis eksplicit aktivere det i din serverkonfiguration.

Der findes forskellige typer notifikationer:

| Niveau     | Beskrivelse                   | Eksempel på anvendelse          |
|------------|-------------------------------|----------------------------------|
| debug      | Detaljeret fejlsøgningsinfo   | Funktionens indgang/udgangspunkter |
| info       | Generelle informationsbeskeder | Fremskridtsopdateringer         |
| notice     | Normale, men betydelige hændelser | Konfigurationsændringer        |
| warning    | Advarselsbetingelser          | Brug af forældede funktioner    |
| error      | Fejlbetingelser               | Fejl i operationer              |
| critical   | Kritiske betingelser          | Fejl i systemkomponenter        |
| alert      | Handling kræves straks        | Opdagelse af datakorruption     |
| emergency  | Systemet er ubrugeligt        | Fuldstændigt systemnedbrud      |

## Implementering af notifikationer i MCP

For at implementere notifikationer i MCP skal du opsætte både server- og klientsiden til at håndtere realtidsopdateringer. Dette giver din applikation mulighed for at give øjeblikkelig feedback til brugerne under langvarige operationer.

### Server-side: Afsendelse af notifikationer

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

I det foregående eksempel sender `process_files`-værktøjet tre notifikationer til klienten, mens det behandler hver fil. Metoden `ctx.info()` bruges til at sende informationsbeskeder.

Derudover skal du for at aktivere notifikationer sikre, at din server bruger en streamingtransport (som `streamable-http`), og at din klient implementerer en beskedhåndtering til at behandle notifikationer. Her er, hvordan du kan opsætte serveren til at bruge `streamable-http`-transporten:

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

I dette .NET-eksempel er `ProcessFiles`-værktøjet dekoreret med attributten `Tool` og sender tre notifikationer til klienten, mens det behandler hver fil. Metoden `ctx.Info()` bruges til at sende informationsbeskeder.

For at aktivere notifikationer i din .NET MCP-server skal du sikre, at du bruger en streamingtransport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klient-side: Modtagelse af notifikationer

Klienten skal implementere en beskedhåndtering til at behandle og vise notifikationer, efterhånden som de ankommer.

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

I den foregående kode kontrollerer funktionen `message_handler`, om den indkommende besked er en notifikation. Hvis den er, udskriver den notifikationen; ellers behandles den som en almindelig serverbesked. Bemærk også, hvordan `ClientSession` initialiseres med `message_handler` for at håndtere indkommende notifikationer.

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

I dette .NET-eksempel kontrollerer funktionen `MessageHandler`, om den indkommende besked er en notifikation. Hvis den er, udskriver den notifikationen; ellers behandles den som en almindelig serverbesked. `ClientSession` initialiseres med beskedhåndteringen via `ClientSessionOptions`.

For at aktivere notifikationer skal du sikre, at din server bruger en streamingtransport (som `streamable-http`), og at din klient implementerer en beskedhåndtering til at behandle notifikationer.

## Fremskridtsnotifikationer og scenarier

Denne sektion forklarer konceptet med fremskridtsnotifikationer i MCP, hvorfor de er vigtige, og hvordan man implementerer dem ved hjælp af Streamable HTTP. Du vil også finde en praktisk opgave for at styrke din forståelse.

Fremskridtsnotifikationer er realtidsbeskeder sendt fra serveren til klienten under langvarige operationer. I stedet for at vente på, at hele processen er færdig, holder serveren klienten opdateret om den aktuelle status. Dette forbedrer gennemsigtighed, brugeroplevelse og gør fejlfinding lettere.

**Eksempel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Hvorfor bruge fremskridtsnotifikationer?

Fremskridtsnotifikationer er vigtige af flere grunde:

- **Bedre brugeroplevelse:** Brugere ser opdateringer, mens arbejdet skrider frem, ikke kun til sidst.
- **Realtidsfeedback:** Klienter kan vise fremskridtsbjælker eller logs, hvilket gør appen mere responsiv.
- **Lettere fejlfinding og overvågning:** Udviklere og brugere kan se, hvor en proces måske er langsom eller sidder fast.

### Hvordan implementerer man fremskridtsnotifikationer?

Sådan implementerer du fremskridtsnotifikationer i MCP:

- **På serveren:** Brug `ctx.info()` eller `ctx.log()` til at sende notifikationer, efterhånden som hvert element behandles. Dette sender en besked til klienten, før hovedresultatet er klar.
- **På klienten:** Implementer en beskedhåndtering, der lytter efter og viser notifikationer, efterhånden som de ankommer. Denne håndtering skelner mellem notifikationer og det endelige resultat.

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

Når du implementerer MCP-servere med HTTP-baserede transporter, bliver sikkerhed en altafgørende bekymring, der kræver omhyggelig opmærksomhed på flere angrebsvektorer og beskyttelsesmekanismer.

### Oversigt

Sikkerhed er kritisk, når MCP-servere eksponeres over HTTP. Streamable HTTP introducerer nye angrebsflader og kræver omhyggelig konfiguration.

### Nøglepunkter

- **Origin Header-validering**: Valider altid `Origin`-headeren for at forhindre DNS-rebinding-angreb.
- **Localhost-binding**: Til lokal udvikling skal servere bindes til `localhost` for at undgå eksponering på det offentlige internet.
- **Autentifikation**: Implementer autentifikation (f.eks. API-nøgler, OAuth) til produktionsudrulninger.
- **CORS**: Konfigurer Cross-Origin Resource Sharing (CORS)-politikker for at begrænse adgang.
- **HTTPS**: Brug HTTPS i produktion for at kryptere trafik.

### Bedste praksis

- Stol aldrig på indkommende anmodninger uden validering.
- Log og overvåg al adgang og fejl.
- Opdater regelmæssigt afhængigheder for at rette sikkerhedssårbarheder.

### Udfordringer

- At balancere sikkerhed med udviklingsvenlighed.
- At sikre kompatibilitet med forskellige klientmiljøer.

## Opgradering fra SSE til Streamable HTTP

For applikationer, der i øjeblikket bruger Server-Sent Events (SSE), giver migration til Streamable HTTP forbedrede funktioner og bedre langsigtet bæredygtighed for dine MCP-implementeringer.

### Hvorfor opgradere?
Der er to overbevisende grunde til at opgradere fra SSE til Streamable HTTP:

- Streamable HTTP tilbyder bedre skalerbarhed, kompatibilitet og mere avanceret understøttelse af notifikationer end SSE.
- Det er den anbefalede transport til nye MCP-applikationer.

### Migrationsskridt

Sådan kan du migrere fra SSE til Streamable HTTP i dine MCP-applikationer:

- **Opdater serverkoden** til at bruge `transport="streamable-http"` i `mcp.run()`.
- **Opdater klientkoden** til at bruge `streamablehttp_client` i stedet for SSE-klient.
- **Implementer en meddelelseshåndtering** i klienten til at behandle notifikationer.
- **Test for kompatibilitet** med eksisterende værktøjer og arbejdsgange.

### Opretholdelse af kompatibilitet

Det anbefales at opretholde kompatibilitet med eksisterende SSE-klienter under migrationsprocessen. Her er nogle strategier:

- Du kan understøtte både SSE og Streamable HTTP ved at køre begge transporter på forskellige endpoints.
- Gradvist migrere klienter til den nye transport.

### Udfordringer

Sørg for at håndtere følgende udfordringer under migrationen:

- Sikre, at alle klienter bliver opdateret
- Håndtere forskelle i notifikationslevering

## Sikkerhedsovervejelser

Sikkerhed bør være en topprioritet, når du implementerer en server, især når du bruger HTTP-baserede transporter som Streamable HTTP i MCP.

Når du implementerer MCP-servere med HTTP-baserede transporter, bliver sikkerhed en afgørende faktor, der kræver omhyggelig opmærksomhed på flere angrebsvektorer og beskyttelsesmekanismer.

### Oversigt

Sikkerhed er kritisk, når MCP-servere eksponeres over HTTP. Streamable HTTP introducerer nye angrebsflader og kræver omhyggelig konfiguration.

Her er nogle vigtige sikkerhedsovervejelser:

- **Validering af Origin-header**: Valider altid `Origin`-headeren for at forhindre DNS-rebinding-angreb.
- **Binding til localhost**: Til lokal udvikling skal servere bindes til `localhost` for at undgå eksponering på det offentlige internet.
- **Autentifikation**: Implementer autentifikation (f.eks. API-nøgler, OAuth) til produktionsmiljøer.
- **CORS**: Konfigurer Cross-Origin Resource Sharing (CORS)-politikker for at begrænse adgang.
- **HTTPS**: Brug HTTPS i produktion for at kryptere trafikken.

### Bedste praksis

Her er yderligere bedste praksis, du bør følge, når du implementerer sikkerhed i din MCP-streamingserver:

- Stol aldrig på indgående anmodninger uden validering.
- Log og overvåg al adgang og fejl.
- Opdater regelmæssigt afhængigheder for at rette sikkerhedssårbarheder.

### Udfordringer

Du vil møde nogle udfordringer, når du implementerer sikkerhed i MCP-streamingservere:

- At balancere sikkerhed med nem udvikling
- At sikre kompatibilitet med forskellige klientmiljøer

### Opgave: Byg din egen streaming MCP-app

**Scenario:**
Byg en MCP-server og -klient, hvor serveren behandler en liste over elementer (f.eks. filer eller dokumenter) og sender en notifikation for hvert behandlet element. Klienten skal vise hver notifikation, når den modtages.

**Trin:**

1. Implementer et serverværktøj, der behandler en liste og sender notifikationer for hvert element.
2. Implementer en klient med en meddelelseshåndtering til at vise notifikationer i realtid.
3. Test din implementering ved at køre både server og klient, og observer notifikationerne.

[Solution](./solution/README.md)

## Yderligere læsning og hvad nu?

For at fortsætte din rejse med MCP-streaming og udvide din viden giver dette afsnit yderligere ressourcer og foreslåede næste skridt til at bygge mere avancerede applikationer.

### Yderligere læsning

- [Microsoft: Introduktion til HTTP-streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS i ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Hvad nu?

- Prøv at bygge mere avancerede MCP-værktøjer, der bruger streaming til realtidsanalyse, chat eller samarbejdsredigering.
- Udforsk integration af MCP-streaming med frontend-rammer (React, Vue osv.) for live UI-opdateringer.
- Næste: [Udnyttelse af AI Toolkit til VSCode](../07-aitk/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.