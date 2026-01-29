# HTTPS-strømming med Model Context Protocol (MCP)

Dette kapittelet gir en omfattende veiledning i hvordan man implementerer sikker, skalerbar og sanntidsstrømming med Model Context Protocol (MCP) ved bruk av HTTPS. Det dekker motivasjonen for strømming, tilgjengelige transportmekanismer, hvordan man implementerer strømbar HTTP i MCP, sikkerhetspraksis, migrasjon fra SSE og praktiske råd for å bygge dine egne MCP-strømmingsapplikasjoner.

## Transportmekanismer og strømming i MCP

Denne delen utforsker de ulike transportmekanismene som er tilgjengelige i MCP og deres rolle i å muliggjøre strømming for sanntidskommunikasjon mellom klienter og servere.

### Hva er en transportmekanisme?

En transportmekanisme definerer hvordan data utveksles mellom klient og server. MCP støtter flere transporttyper for å passe til ulike miljøer og krav:

- **stdio**: Standard input/output, egnet for lokale og CLI-baserte verktøy. Enkelt, men ikke egnet for web eller sky.
- **SSE (Server-Sent Events)**: Lar servere sende sanntidsoppdateringer til klienter over HTTP. Bra for webgrensesnitt, men begrenset i skalerbarhet og fleksibilitet.
- **Strømbar HTTP**: Moderne HTTP-basert strømmingstransport som støtter varsler og bedre skalerbarhet. Anbefales for de fleste produksjons- og skyløsninger.

### Sammenligningstabell

Se sammenligningstabellen nedenfor for å forstå forskjellene mellom disse transportmekanismene:

| Transport         | Sanntidsoppdateringer | Strømming | Skalerbarhet | Bruksområde              |
|-------------------|-----------------------|-----------|--------------|--------------------------|
| stdio             | Nei                  | Nei        | Lav          | Lokale CLI-verktøy       |
| SSE               | Ja                   | Ja         | Middels      | Web, sanntidsoppdateringer |
| Strømbar HTTP     | Ja                   | Ja         | Høy          | Sky, flere klienter      |

> **Tips:** Valg av riktig transport påvirker ytelse, skalerbarhet og brukeropplevelse. **Strømbar HTTP** anbefales for moderne, skalerbare og skyklare applikasjoner.

Merk transportene stdio og SSE som ble vist i tidligere kapitler, og hvordan strømbar HTTP er transporten som dekkes i dette kapittelet.

## Strømming: Konsepter og motivasjon

Å forstå de grunnleggende konseptene og motivasjonen bak strømming er essensielt for å implementere effektive sanntidskommunikasjonssystemer.

**Strømming** er en teknikk innen nettverksprogrammering som lar data sendes og mottas i små, håndterbare biter eller som en sekvens av hendelser, i stedet for å vente på at hele svaret skal være klart. Dette er spesielt nyttig for:

- Store filer eller datasett.
- Sanntidsoppdateringer (f.eks. chat, fremdriftsindikatorer).
- Langvarige beregninger der man ønsker å holde brukeren informert.

Her er det du trenger å vite om strømming på et overordnet nivå:

- Data leveres progressivt, ikke alt på en gang.
- Klienten kan behandle data etter hvert som det ankommer.
- Reduserer opplevd ventetid og forbedrer brukeropplevelsen.

### Hvorfor bruke strømming?

Årsakene til å bruke strømming er følgende:

- Brukere får umiddelbar tilbakemelding, ikke bare på slutten.
- Muliggjør sanntidsapplikasjoner og responsive brukergrensesnitt.
- Mer effektiv bruk av nettverks- og databehandlingsressurser.

### Enkelt eksempel: HTTP-strømming server og klient

Her er et enkelt eksempel på hvordan strømming kan implementeres:

#### Python

**Server (Python, ved bruk av FastAPI og StreamingResponse):**

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

**Klient (Python, ved bruk av requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Dette eksempelet viser en server som sender en serie meldinger til klienten etter hvert som de blir tilgjengelige, i stedet for å vente til alle meldingene er klare.

**Hvordan det fungerer:**

- Serveren sender hver melding etter hvert som den er klar.
- Klienten mottar og skriver ut hver bit etter hvert som den ankommer.

**Krav:**

- Serveren må bruke et strømmerespons (f.eks. `StreamingResponse` i FastAPI).
- Klienten må behandle responsen som en strøm (`stream=True` i requests).
- Content-Type er vanligvis `text/event-stream` eller `application/octet-stream`.

#### Java

**Server (Java, ved bruk av Spring Boot og Server-Sent Events):**

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

**Klient (Java, ved bruk av Spring WebFlux WebClient):**

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

**Notater om Java-implementering:**

- Bruker Spring Boots reaktive stack med `Flux` for strømming.
- `ServerSentEvent` gir strukturert hendelsesstrømming med hendelsestyper.
- `WebClient` med `bodyToFlux()` muliggjør reaktiv strømmekonsumering.
- `delayElements()` simulerer behandlingstid mellom hendelser.
- Hendelser kan ha typer (`info`, `result`) for bedre klienthåndtering.

### Sammenligning: Klassisk strømming vs MCP-strømming

Forskjellene mellom hvordan strømming fungerer på en "klassisk" måte kontra hvordan det fungerer i MCP kan beskrives slik:

| Funksjon              | Klassisk HTTP-strømming       | MCP-strømming (Varsler)          |
|-----------------------|-------------------------------|----------------------------------|
| Hovedrespons          | Oppdelt                      | Enkel, på slutten               |
| Fremdriftsoppdateringer | Sendt som databiter          | Sendt som varsler               |
| Klientkrav            | Må behandle strømmen          | Må implementere meldingshåndterer |
| Bruksområde           | Store filer, AI-tokenstrømmer | Fremdrift, logger, sanntidsfeedback |

### Observerte nøkkelforskjeller

I tillegg er det noen nøkkelforskjeller:

- **Kommunikasjonsmønster:**
  - Klassisk HTTP-strømming: Bruker enkel oppdelt overføring for å sende data i biter.
  - MCP-strømming: Bruker et strukturert varslingssystem med JSON-RPC-protokoll.

- **Meldingsformat:**
  - Klassisk HTTP: Ren tekst i biter med linjeskift.
  - MCP: Strukturerte `LoggingMessageNotification`-objekter med metadata.

- **Klientimplementering:**
  - Klassisk HTTP: Enkel klient som behandler strømmeresponser.
  - MCP: Mer sofistikert klient med en meldingshåndterer for å behandle ulike typer meldinger.

- **Fremdriftsoppdateringer:**
  - Klassisk HTTP: Fremdriften er en del av hovedstrømmen.
  - MCP: Fremdrift sendes via separate varslingsmeldinger mens hovedresponsen kommer til slutt.

### Anbefalinger

Her er noen anbefalinger når det gjelder å velge mellom å implementere klassisk strømming (som en endpoint vi viste deg ovenfor ved bruk av `/stream`) kontra å velge strømming via MCP.

- **For enkle strømmingsbehov:** Klassisk HTTP-strømming er enklere å implementere og tilstrekkelig for grunnleggende strømmingsbehov.
- **For komplekse, interaktive applikasjoner:** MCP-strømming gir en mer strukturert tilnærming med rikere metadata og separasjon mellom varsler og endelige resultater.
- **For AI-applikasjoner:** MCPs varslingssystem er spesielt nyttig for langvarige AI-oppgaver der du vil holde brukerne informert om fremdriften.

## Strømming i MCP

Ok, så du har sett noen anbefalinger og sammenligninger så langt om forskjellen mellom klassisk strømming og strømming i MCP. La oss gå i detalj om hvordan du kan utnytte strømming i MCP.

Å forstå hvordan strømming fungerer innenfor MCP-rammeverket er essensielt for å bygge responsive applikasjoner som gir sanntidsfeedback til brukere under langvarige operasjoner.

I MCP handler strømming ikke om å sende hovedresponsen i biter, men om å sende **varsler** til klienten mens et verktøy behandler en forespørsel. Disse varslene kan inkludere fremdriftsoppdateringer, logger eller andre hendelser.

### Hvordan det fungerer

Hovedresultatet sendes fortsatt som en enkelt respons. Imidlertid kan varsler sendes som separate meldinger under behandlingen og dermed oppdatere klienten i sanntid. Klienten må kunne håndtere og vise disse varslene.

## Hva er et varsel?

Vi nevnte "varsel", hva betyr det i MCP-sammenheng?

Et varsel er en melding sendt fra serveren til klienten for å informere om fremdrift, status eller andre hendelser under en langvarig operasjon. Varsler forbedrer transparens og brukeropplevelse.

For eksempel skal en klient sende et varsel når den første håndtrykkingen med serveren er fullført.

Et varsel ser slik ut som en JSON-melding:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Varsler tilhører et emne i MCP referert til som ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

For å få logging til å fungere, må serveren aktivere det som en funksjon/kapasitet slik:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Avhengig av SDK som brukes, kan logging være aktivert som standard, eller du må eksplisitt aktivere det i serverkonfigurasjonen.

Det finnes ulike typer varsler:

| Nivå       | Beskrivelse                   | Eksempel på brukstilfelle       |
|------------|-------------------------------|----------------------------------|
| debug      | Detaljert feilsøkingsinformasjon | Funksjonsinngang/-utgang        |
| info       | Generelle informasjonsmeldinger | Oppdateringer om fremdrift      |
| notice     | Normale, men viktige hendelser | Endringer i konfigurasjon       |
| warning    | Advarselsforhold              | Bruk av utgåtte funksjoner      |
| error      | Feilforhold                   | Operasjonsfeil                  |
| critical   | Kritiske forhold              | Feil i systemkomponenter        |
| alert      | Umiddelbar handling nødvendig | Oppdaget datakorrupsjon         |
| emergency  | Systemet er ubrukelig         | Fullstendig systemsvikt         |

## Implementering av varsler i MCP

For å implementere varsler i MCP må du sette opp både server- og klientsiden for å håndtere sanntidsoppdateringer. Dette lar applikasjonen din gi umiddelbar tilbakemelding til brukere under langvarige operasjoner.

### Serverside: Sende varsler

La oss starte med serversiden. I MCP definerer du verktøy som kan sende varsler mens de behandler forespørsler. Serveren bruker kontektsobjektet (vanligvis `ctx`) for å sende meldinger til klienten.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

I eksempelet ovenfor sender `process_files`-verktøyet tre varsler til klienten mens det behandler hver fil. Metoden `ctx.info()` brukes til å sende informasjonsmeldinger.

I tillegg, for å aktivere varsler, må du sørge for at serveren din bruker en strømmetransport (som `streamable-http`) og at klienten din implementerer en meldingshåndterer for å behandle varsler. Slik kan du sette opp serveren til å bruke `streamable-http`-transport:

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

I dette .NET-eksempelet er `ProcessFiles`-verktøyet dekorert med `Tool`-attributtet og sender tre varsler til klienten mens det behandler hver fil. Metoden `ctx.Info()` brukes til å sende informasjonsmeldinger.

For å aktivere varsler i din .NET MCP-server, sørg for at du bruker en strømmetransport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klientside: Motta varsler

Klienten må implementere en meldingshåndterer for å behandle og vise varsler etter hvert som de ankommer.

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

I koden ovenfor sjekker funksjonen `message_handler` om den innkommende meldingen er et varsel. Hvis det er et varsel, skriver den ut varselet; ellers behandler den det som en vanlig servermelding. Merk også hvordan `ClientSession` initialiseres med `message_handler` for å håndtere innkommende varsler.

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

I dette .NET-eksempelet sjekker funksjonen `MessageHandler` om den innkommende meldingen er et varsel. Hvis det er et varsel, skriver den ut varselet; ellers behandler den det som en vanlig servermelding. `ClientSession` initialiseres med meldingshåndtereren via `ClientSessionOptions`.

For å aktivere varsler, sørg for at serveren din bruker en strømmetransport (som `streamable-http`) og at klienten din implementerer en meldingshåndterer for å behandle varsler.

## Fremdriftsvarsler og scenarier

Denne delen forklarer konseptet med fremdriftsvarsler i MCP, hvorfor de er viktige, og hvordan du implementerer dem ved hjelp av strømbar HTTP. Du finner også en praktisk oppgave for å styrke forståelsen din.

Fremdriftsvarsler er sanntidsmeldinger sendt fra serveren til klienten under langvarige operasjoner. I stedet for å vente til hele prosessen er ferdig, holder serveren klienten oppdatert om gjeldende status. Dette forbedrer transparens, brukeropplevelse og gjør feilsøking enklere.

**Eksempel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Hvorfor bruke fremdriftsvarsler?

Fremdriftsvarsler er essensielle av flere grunner:

- **Bedre brukeropplevelse:** Brukere ser oppdateringer mens arbeidet pågår, ikke bare på slutten.
- **Sanntidsfeedback:** Klienter kan vise fremdriftsindikatorer eller logger, noe som gjør appen mer responsiv.
- **Enklere feilsøking og overvåking:** Utviklere og brukere kan se hvor en prosess kan være treg eller fastlåst.

### Hvordan implementere fremdriftsvarsler

Slik implementerer du fremdriftsvarsler i MCP:

- **På serveren:** Bruk `ctx.info()` eller `ctx.log()` for å sende varsler etter hvert som hvert element behandles. Dette sender en melding til klienten før hovedresultatet er klart.
- **På klienten:** Implementer en meldingshåndterer som lytter etter og viser varsler etter hvert som de ankommer. Denne håndtereren skiller mellom varsler og det endelige resultatet.

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

Når du implementerer MCP-servere med HTTP-baserte transporter, blir sikkerhet en kritisk bekymring som krever nøye oppmerksomhet til flere angrepsflater og beskyttelsesmekanismer.

### Oversikt

Sikkerhet er avgjørende når MCP-servere eksponeres over HTTP. Strømbar HTTP introduserer nye angrepsflater og krever nøye konfigurasjon.

### Viktige punkter

- **Validering av Origin-header:** Valider alltid `Origin`-headeren for å forhindre DNS-rebinding-angrep.
- **Binding til localhost:** For lokal utvikling, bind servere til `localhost` for å unngå eksponering på det offentlige internettet.
- **Autentisering:** Implementer autentisering (f.eks. API-nøkler, OAuth) for produksjonsdistribusjoner.
- **CORS:** Konfigurer Cross-Origin Resource Sharing (CORS)-policyer for å begrense tilgang.
- **HTTPS:** Bruk HTTPS i produksjon for å kryptere trafikk.

### Beste praksis

- Stol aldri på innkommende forespørsler uten validering.
- Logg og overvåk all tilgang og feil.
- Oppdater regelmessig avhengigheter for å tette sikkerhetssårbarheter.

### Utfordringer

- Balansering av sikkerhet med enkel utvikling.
- Sikre kompatibilitet med ulike klientmiljøer.

## Oppgradering fra SSE til strømbar HTTP

For applikasjoner som for øyeblikket bruker Server-Sent Events (SSE), gir migrering til strømbar HTTP forbedrede muligheter og bedre langsiktig bærekraft for MCP-implementeringene dine.

### Hvorfor oppgradere?
Det er to overbevisende grunner til å oppgradere fra SSE til Streamable HTTP:

- Streamable HTTP tilbyr bedre skalerbarhet, kompatibilitet og rikere støtte for varsler enn SSE.
- Det er den anbefalte transporten for nye MCP-applikasjoner.

### Migreringstrinn

Slik kan du migrere fra SSE til Streamable HTTP i dine MCP-applikasjoner:

- **Oppdater serverkoden** til å bruke `transport="streamable-http"` i `mcp.run()`.
- **Oppdater klientkoden** til å bruke `streamablehttp_client` i stedet for SSE-klienten.
- **Implementer en meldingshåndterer** i klienten for å behandle varsler.
- **Test for kompatibilitet** med eksisterende verktøy og arbeidsflyter.

### Opprettholde kompatibilitet

Det anbefales å opprettholde kompatibilitet med eksisterende SSE-klienter under migreringsprosessen. Her er noen strategier:

- Du kan støtte både SSE og Streamable HTTP ved å kjøre begge transportene på forskjellige endepunkter.
- Gradvis migrere klienter til den nye transporten.

### Utfordringer

Sørg for å håndtere følgende utfordringer under migreringen:

- Sikre at alle klienter blir oppdatert
- Håndtere forskjeller i leveranse av varsler

## Sikkerhetsbetraktninger

Sikkerhet bør være en topp prioritet når du implementerer en server, spesielt når du bruker HTTP-baserte transporter som Streamable HTTP i MCP.

Når du implementerer MCP-servere med HTTP-baserte transporter, blir sikkerhet en avgjørende bekymring som krever nøye oppmerksomhet til flere angrepsvektorer og beskyttelsesmekanismer.

### Oversikt

Sikkerhet er kritisk når MCP-servere eksponeres over HTTP. Streamable HTTP introduserer nye angrepsflater og krever nøye konfigurasjon.

Her er noen viktige sikkerhetsbetraktninger:

- **Validering av Origin-header**: Valider alltid `Origin`-headeren for å forhindre DNS-rebinding-angrep.
- **Binding til localhost**: For lokal utvikling, bind servere til `localhost` for å unngå eksponering mot det offentlige internett.
- **Autentisering**: Implementer autentisering (f.eks. API-nøkler, OAuth) for produksjonsmiljøer.
- **CORS**: Konfigurer Cross-Origin Resource Sharing (CORS)-policyer for å begrense tilgang.
- **HTTPS**: Bruk HTTPS i produksjon for å kryptere trafikk.

### Beste praksis

I tillegg er her noen beste praksiser å følge når du implementerer sikkerhet i din MCP-strømmeserver:

- Stol aldri på innkommende forespørsler uten validering.
- Loggfør og overvåk all tilgang og feil.
- Oppdater regelmessig avhengigheter for å tette sikkerhetssårbarheter.

### Utfordringer

Du vil møte noen utfordringer når du implementerer sikkerhet i MCP-strømmeservere:

- Balansering av sikkerhet med enkel utvikling
- Sikre kompatibilitet med ulike klientmiljøer

### Oppgave: Bygg din egen strømmende MCP-app

**Scenario:**
Bygg en MCP-server og -klient der serveren behandler en liste over elementer (f.eks. filer eller dokumenter) og sender et varsel for hvert element som behandles. Klienten skal vise hvert varsel etter hvert som det ankommer.

**Trinn:**

1. Implementer et serververktøy som behandler en liste og sender varsler for hvert element.
2. Implementer en klient med en meldingshåndterer for å vise varsler i sanntid.
3. Test implementasjonen din ved å kjøre både server og klient, og observer varslene.

[Solution](./solution/README.md)

## Videre lesing og hva nå?

For å fortsette reisen din med MCP-strømming og utvide kunnskapen din, gir denne seksjonen ekstra ressurser og foreslåtte neste trinn for å bygge mer avanserte applikasjoner.

### Videre lesing

- [Microsoft: Introduksjon til HTTP-strømming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS i ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Strømmende forespørsler](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Hva nå?

- Prøv å bygge mer avanserte MCP-verktøy som bruker strømming for sanntidsanalyse, chat eller samarbeidende redigering.
- Utforsk integrering av MCP-strømming med frontend-rammeverk (React, Vue, etc.) for live UI-oppdateringer.
- Neste: [Bruke AI Toolkit for VSCode](../07-aitk/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.