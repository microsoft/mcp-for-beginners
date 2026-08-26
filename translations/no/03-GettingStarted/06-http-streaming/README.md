# HTTPS-strømming med Model Context Protocol (MCP)

Dette kapitlet gir en omfattende veiledning for å implementere sikker, skalerbar og sanntidsstrømming med Model Context Protocol (MCP) ved hjelp av HTTPS. Det dekker motivasjonen for strømming, tilgjengelige transportmekanismer, hvordan implementere strømmbar HTTP i MCP, sikkerhetsbeste praksis, migrering fra SSE, og praktisk veiledning for å bygge dine egne strømmende MCP-applikasjoner.

> **Ser fremover:** denne leksjonen beskriver Strømmbar HTTP under **MCP-spesifikasjon 2025-11-25**, hvor en økt etableres under `initialize` og festes med en `Mcp-Session-Id` header. Release-kandidaten `2026-07-28` fjerner helt håndtrykket og økt-ID, noe som gjør at hver forespørsel er selvstendig og kan rutes til hvilken som helst serverinstans uten sticky sessions. Se [Hva som endres i MCP: Release-kandidaten 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) for detaljer.

## Transportmekanismer og strømming i MCP

Denne seksjonen utforsker de forskjellige transportmekanismene som er tilgjengelige i MCP, og deres rolle i å muliggjøre strømming for sanntidskommunikasjon mellom klienter og servere.

### Hva er en transportmekanisme?

En transportmekanisme definerer hvordan data utveksles mellom klient og server. MCP støtter flere transporttyper for å tilpasse seg ulike miljøer og krav:

- **stdio**: Standard inn/ut, egnet for lokale og CLI-baserte verktøy. Enkelt men ikke egnet for web eller sky.
- **SSE (Server-Sent Events)**: Lar servere sende sanntidsoppdateringer til klienter over HTTP. Bra for webgrensesnitt, men begrenset i skalerbarhet og fleksibilitet. Fra MCP-spesifikasjon 2025-06-18 er den frittstående SSE-transporten (Server-Sent Events) avviklet og erstattet av "Strømmbar HTTP" transport.
- **Strømmbar HTTP**: Moderne HTTP-basert strømmingstransport, støtter notifikasjoner og bedre skalerbarhet. Anbefales for de fleste produksjons- og sky-scenarioer.

### Sammenligningstabell

Ta en titt på sammenligningstabellen nedenfor for å forstå forskjellene mellom disse transportmekanismene:

| Transport         | Sanntidsoppdateringer | Strømming | Skalerbarhet | Brukstilfelle           |
|-------------------|-----------------------|-----------|--------------|-------------------------|
| stdio             | Nei                   | Nei       | Lav          | Lokale CLI-verktøy      |
| SSE               | Ja                    | Ja        | Middels      | Web, sanntidsoppdateringer |
| Strømmbar HTTP   | Ja                    | Ja        | Høy          | Sky, multi-klient       |

> **Tips:** Valg av riktig transport påvirker ytelse, skalerbarhet og brukeropplevelse. **Strømmbar HTTP** anbefales for moderne, skalerbare og skyklare applikasjoner.

Merk deg transportene stdio og SSE som du ble vist i forrige kapitler, og hvordan strømmbar HTTP er transporten som dekkes i dette kapitlet.

## Strømming: Konsepter og motivasjon

Å forstå de grunnleggende konseptene og motivasjonene bak strømming er essensielt for å implementere effektive sanntidskommunikasjonssystemer.

**Strømming** er en teknikk innen nettverksprogrammering som tillater at data sendes og mottas i små, håndterbare biter eller som en sekvens av hendelser, snarere enn å vente på at hele svaret er ferdig. Dette er spesielt nyttig for:

- Store filer eller datasett.
- Sanntidsoppdateringer (f.eks. chat, fremdriftslinjer).
- Langvarige beregninger hvor du vil holde brukeren informert.

Her er hva du trenger å vite om strømming på et overordnet nivå:

- Data leveres progressivt, ikke alt på en gang.
- Klienten kan prosessere data etter hvert som de kommer.
- Reduserer opplevd latens og forbedrer brukeropplevelse.

### Hvorfor bruke strømming?

Årsakene til å bruke strømming er følgende:

- Brukere får umiddelbar tilbakemelding, ikke bare på slutten
- Muliggjør sanntidsapplikasjoner og responsive UI-er
- Mer effektiv bruk av nettverks- og beregningsressurser

### Enkel eksempel: HTTP-strømmeserver og klient

Her er et enkelt eksempel på hvordan strømming kan implementeres:

#### Python

**Server (Python, bruker FastAPI og StreamingResponse):**

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

**Klient (Python, bruker requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Dette eksempelet demonstrerer en server som sender en serie meldinger til klienten etter hvert som de blir tilgjengelige, i stedet for å vente på at alle meldinger skal være klare.

**Hvordan det fungerer:**

- Serveren gir hver melding etter hvert som den er klar.
- Klienten mottar og skriver ut hver bit etter hvert som den ankommer.

**Krav:**

- Serveren må bruke en strømmerespons (f.eks. `StreamingResponse` i FastAPI).
- Klienten må prosessere responsen som en strøm (`stream=True` i requests).
- Content-Type er vanligvis `text/event-stream` eller `application/octet-stream`.

#### Java

**Server (Java, bruker Spring Boot og Server-Sent Events):**

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

**Klient (Java, bruker Spring WebFlux WebClient):**

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

**Notater om Java-implementasjonen:**

- Bruker Spring Boot sin reaktive stack med `Flux` for strømming
- `ServerSentEvent` tilbyr strukturert hendelsesstrømming med hendelsestyper
- `WebClient` med `bodyToFlux()` muliggjør reaktiv konsumering av strømming
- `delayElements()` simulerer behandlingstid mellom hendelser
- Hendelser kan ha typer (`info`, `result`) for bedre klienthåndtering

### Sammenligning: Klassisk streaming vs MCP streaming

Forskjellene mellom hvordan strømming fungerer på en "klassisk" måte vs i MCP kan framstilles slik:

| Funksjon               | Klassisk HTTP-strømming       | MCP-strømming (Notifikasjoner)   |
|------------------------|-------------------------------|----------------------------------|
| Hovedrespons           | Delt opp i biter              | Enkelt, til slutt                |
| Fremdriftsoppdateringer | Sendt som databit             | Sendt som notifikasjoner         |
| Klientkrav             | Må prosessere strømmen        | Må implementere meldingsbehandler |
| Brukstilfelle          | Store filer, AI-token-strømmer | Fremdrift, logger, sanntids tilbakemelding |

### Viktige observerte forskjeller

I tillegg er her noen viktige forskjeller:

- **Kommunikasjonsmønster:**
  - Klassisk HTTP-strømming: Bruker enkel chunked transfer encoding for å sende data i biter
  - MCP-strømming: Bruker et strukturert notifikasjonssystem med JSON-RPC-protokoll

- **Meldingsformat:**
  - Klassisk HTTP: Ren tekst i biter med linjeskift
  - MCP: Strukturerte LoggingMessageNotification-objekter med metadata

- **Klientimplementering:**
  - Klassisk HTTP: Enkel klient som prosesserer strømmingsrespons
  - MCP: Mer sofistikert klient med en meldingsbehandler for å prosessere ulike meldings-typer

- **Fremdriftsoppdateringer:**
  - Klassisk HTTP: Fremdriften er del av hovedstrømmen
  - MCP: Fremdrift sendes via separate notifikasjonsmeldinger mens hovedresponsen kommer til slutt

### Anbefalinger

Det er noen ting vi anbefaler når det kommer til valg mellom å implementere klassisk strømming (som en endepunkt vi viste deg ovenfor med `/stream`) versus å velge strømming via MCP.

- **For enkle strømmingsbehov:** Klassisk HTTP-strømming er enklere å implementere og tilstrekkelig for grunnleggende strømming.

- **For komplekse, interaktive applikasjoner:** MCP-strømming gir en mer strukturert tilnærming med rikere metadata og separasjon mellom notifikasjoner og endelige resultater.

- **For AI-applikasjoner:** MCPs notifikasjonssystem er spesielt nyttig for langvarige AI-oppgaver hvor du vil holde brukere informert om fremdrift.

## Strømming i MCP

Ok, så du har sett noen anbefalinger og sammenligninger så langt på forskjellen mellom klassisk strømming og strømming i MCP. La oss gå i detalj på nøyaktig hvordan du kan utnytte strømming i MCP.

Å forstå hvordan strømming fungerer innenfor MCP-rammeverket er viktig for å bygge responsive applikasjoner som gir sanntids tilbakemelding til brukere under langvarige operasjoner.

I MCP handler ikke strømming om å sende hovedresponsen i biter, men om å sende **notifikasjoner** til klienten mens et verktøy behandler en forespørsel. Disse notifikasjonene kan inkludere fremdriftsoppdateringer, logger eller andre hendelser.

### Hvordan det fungerer

Hovedresultatet sendes fortsatt som en enkel respons. Imidlertid kan notifikasjoner sendes som separate meldinger under behandling og dermed oppdatere klienten i sanntid. Klienten må kunne håndtere og vise disse notifikasjonene.

## Hva er en notifikasjon?

Vi sa "notifikasjon", hva betyr det i MCP-sammenheng?

En notifikasjon er en melding sendt fra server til klient for å informere om fremdrift, status eller andre hendelser under en langvarig operasjon. Notifikasjoner forbedrer åpenhet og brukeropplevelse.

For eksempel skal en klient sende en notifikasjon når det innledende håndtrykket med serveren er fullført.

En notifikasjon ser slik ut som en JSON-melding:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notifikasjoner tilhører et tema i MCP referert til som ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Avviklingsvarsel:** MCP-spesifikasjonens release-kandidat `2026-07-28` markerer Logging-primitivet som avviklet til fordel for `stderr` for stdio-transporter og OpenTelemetry for strukturert observabilitet. Logging fortsetter å fungere i `2025-11-25` og i minst ett år etter en formell avvikling. Se [Hva som endres i MCP: Release-kandidaten 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

For å få logging til å fungere, må serveren aktivere det som en funksjon/egenskap slik:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Avhengig av SDK-en som brukes, kan logging være aktivert som standard, eller du må eksplisitt aktivere det i serverkonfigurasjonen din.

Det finnes forskjellige typer notifikasjoner:

| Nivå      | Beskrivelse                   | Eksempel brukstilfelle         |
|-----------|-------------------------------|-------------------------------|
| debug     | Detaljerte feilsøkingsinformasjon | Funksjonsinngang-/utgangspunkter |
| info      | Generelle informasjonsmeldinger | Oppdateringer om fremdrift    |
| notice    | Normale men betydningsfulle hendelser | Konfigurasjonsendringer    |
| warning   | Advarsler                    | Bruk av utrangert funksjonalitet |
| error     | Feil                       | Operasjonsfeil                |
| critical  | Kritiske forhold              | Systemkomponentfeil           |
| alert     | Umiddelbar handling kreves   | Datakorrupt oppdaget          |
| emergency | Systemet er ubrukelig         | Total systemfeil              |

## Implementering av notifikasjoner i MCP

For å implementere notifikasjoner i MCP må du sette opp både server- og klientsiden for å håndtere sanntidsoppdateringer. Dette gjør at applikasjonen din kan gi umiddelbar tilbakemelding til brukere under langvarige operasjoner.

### Serverside: Sende notifikasjoner

La oss starte med serversiden. I MCP definerer du verktøy som kan sende notifikasjoner mens de behandler forespørsler. Serveren bruker kontekstobjektet (vanligvis `ctx`) for å sende meldinger til klienten.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

I det foregående eksempelet sender `process_files`-verktøyet tre notifikasjoner til klienten mens det behandler hver fil. Metoden `ctx.info()` brukes for å sende informasjonsmeldinger.

I tillegg, for å aktivere notifikasjoner, må serveren bruke en strømmetransport (som `streamable-http`) og klienten må implementere en meldingsbehandler for å prosessere notifikasjoner. Slik setter du opp serveren til å bruke `streamable-http` transport:

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

I dette .NET-eksempelet er `ProcessFiles`-verktøyet dekorert med `Tool`-attributtet og sender tre notifikasjoner til klienten mens det behandler hver fil. `ctx.Info()` brukes for å sende informasjonsmeldinger.

For å aktivere notifikasjoner i din .NET MCP-server, sørg for at du bruker en strømmetransport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klientside: Motta notifikasjoner

Klienten må implementere en meldingsbehandler for å prosessere og vise notifikasjoner etter hvert som de kommer.

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

I koden ovenfor sjekker `message_handler`-funksjonen om den innkommende meldingen er en notifikasjon. Hvis den er det, skriver den ut notifikasjonen; ellers prosesseres den som en vanlig servermelding. Merk også hvordan `ClientSession` initieres med `message_handler` for å håndtere innkommende notifikasjoner.

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

I dette .NET-eksempelet sjekker `MessageHandler`-funksjonen om den innkommende meldingen er en notifikasjon. Hvis den er det, skriver den ut notifikasjonen; ellers prosesseres den som en vanlig servermelding. `ClientSession` initieres med meldingsbehandleren via `ClientSessionOptions`.

For å aktivere notifikasjoner, sørg for at serveren din bruker en strømmetransport (som `streamable-http`) og at klienten implementerer en meldingsbehandler for å prosessere notifikasjoner.

## Fremdriftsnotifikasjoner & scenarioer

Denne seksjonen forklarer konseptet med fremdriftsnotifikasjoner i MCP, hvorfor de er viktige, og hvordan du kan implementere dem ved bruk av Strømmbar HTTP. Du finner også en praktisk oppgave for å styrke forståelsen din.

Fremdriftsnotifikasjoner er sanntidsmeldinger sendt fra server til klient under langvarige operasjoner. I stedet for å vente til hele prosessen er ferdig, holder serveren klienten oppdatert om gjeldende status. Dette forbedrer åpenhet, brukeropplevelse og gjør feilsøking enklere.

**Eksempel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Hvorfor bruke fremdriftsnotifikasjoner?

Fremdriftsnotifikasjoner er viktige av flere grunner:

- **Bedre brukeropplevelse:** Brukere ser oppdateringer mens arbeidet pågår, ikke bare på slutten.
- **Sanntids tilbakemelding:** Klienter kan vise fremdriftslinjer eller logger, noe som gjør applikasjonen mer responsiv.
- **Enklere feilsøking og overvåking:** Utviklere og brukere kan se hvor en prosess kan være treg eller satt fast.

### Hvordan implementere fremdriftsnotifikasjoner

Slik kan du implementere fremdriftsnotifikasjoner i MCP:

- **På serveren:** Bruk `ctx.info()` eller `ctx.log()` for å sende notifikasjoner etter hvert som hvert element behandles. Dette sender en melding til klienten før hovedresultatet er klart.
- **På klienten:** Implementer en meldingsbehandler som lytter etter og viser notifikasjoner etter hvert som de kommer. Denne handleren skiller mellom notifikasjoner og det endelige resultatet.

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

## Sikkerhetshensyn

Sikkerhet bør være en høy prioritet når man implementerer enhver server, spesielt når man bruker HTTP-baserte transport som Streamable HTTP i MCP.

Når man implementerer MCP-servere med HTTP-baserte transport, blir sikkerhet et avgjørende fokusområde som krever nøye oppmerksomhet til flere angrepsvektorer og beskyttelsesmekanismer.

### Oversikt

Sikkerhet er kritisk når man eksponerer MCP-servere over HTTP. Streamable HTTP introduserer nye angrepsflater og krever nøye konfigurasjon.

Her er noen viktige sikkerhetshensyn:

- **Validering av Origin-header**: Alltid valider `Origin`-headeren for å forhindre DNS-rebinding-angrep.
- **Binding til localhost**: For lokal utvikling, bind serverne til `localhost` for å unngå å eksponere dem for det offentlige internett.
- **Autentisering**: Implementer autentisering (f.eks. API-nøkler, OAuth) for produksjonsdistribusjoner.
- **CORS**: Konfigurer Cross-Origin Resource Sharing (CORS) policyer for å begrense tilgang.
- **HTTPS**: Bruk HTTPS i produksjon for å kryptere trafikk.

### Beste praksis

I tillegg er det noen beste praksiser å følge når du implementerer sikkerhet i din MCP-streamingserver:

- Stol aldri på innkommende forespørsler uten validering.
- Loggfør og overvåk all tilgang og feil.
- Oppdater regelmessig avhengigheter for å tette sikkerhetshull.

### Utfordringer

Du vil møte noen utfordringer når du implementerer sikkerhet i MCP-streamingservere:

- Balanse mellom sikkerhet og utviklingskomfort
- Sikre kompatibilitet med ulike klientmiljøer


## Oppgradering fra SSE til Streamable HTTP

For applikasjoner som bruker Server-Sent Events (SSE) i dag, gir migrering til Streamable HTTP forbedrede muligheter og bedre langsiktig bærekraft for dine MCP-implementeringer.

### Hvorfor oppgradere?

Det er to overbevisende grunner til å oppgradere fra SSE til Streamable HTTP:

- Streamable HTTP tilbyr bedre skalerbarhet, kompatibilitet og rikere støtte for varsler enn SSE.
- Det er den anbefalte transporten for nye MCP-applikasjoner.

### Migrasjonstrinn

Slik kan du migrere fra SSE til Streamable HTTP i dine MCP-applikasjoner:

- **Oppdater serverkoden** til å bruke `transport="streamable-http"` i `mcp.run()`.
- **Oppdater klientkoden** til å bruke `streamablehttp_client` i stedet for SSE-klient.
- **Implementer en meldingsbehandler** i klienten for å behandle varsler.
- **Test for kompatibilitet** med eksisterende verktøy og arbeidsflyter.

### Oppretthold kompatibilitet

Det anbefales å opprettholde kompatibilitet med eksisterende SSE-klienter under migrasjonsprosessen. Her er noen strategier:

- Du kan støtte både SSE og Streamable HTTP ved å kjøre begge transportene på forskjellige endepunkter.
- Migrer gradvis klienter til den nye transporten.

### Utfordringer

Pass på å håndtere følgende utfordringer under migrering:

- Sikre at alle klienter oppdateres
- Håndtere forskjeller i leveringen av varsler

### Oppgave: Bygg din egen streaming MCP-app

**Scenario:**
Bygg en MCP-server og klient der serveren prosesserer en liste med elementer (f.eks. filer eller dokumenter) og sender et varsel for hvert behandlet element. Klienten skal vise hvert varsel etter hvert som det kommer inn.

**Trinn:**

1. Implementer et serververktøy som prosesserer en liste og sender varsler for hvert element.
2. Implementer en klient med en meldingsbehandler for å vise varsler i sanntid.
3. Test implementeringen ved å kjøre både server og klient, og observer varslingene.

[Løsning](./solution/README.md)

## Videre lesning & Hva nå?

For å fortsette reisen med MCP-streaming og utvide kunnskapen din, tilbyr denne delen ekstra ressurser og foreslåtte neste steg for å bygge mer avanserte applikasjoner.

### Videre lesning

- [Microsoft: Introduksjon til HTTP-streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS i ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Hva nå?

- Prøv å bygge mer avanserte MCP-verktøy som bruker streaming for sanntidsanalyse, chat eller samarbeidende redigering.
- Utforsk integrering av MCP-streaming med frontend-rammeverk (React, Vue, osv.) for live UI-oppdateringer.
- Neste: [Bruke AI Toolkit for VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->