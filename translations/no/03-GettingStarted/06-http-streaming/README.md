# HTTPS streaming med Model Context Protocol (MCP)

Dette kapitlet gir en omfattende guide til å implementere sikker, skalerbar og sanntidsstrømming med Model Context Protocol (MCP) ved bruk av HTTPS. Det dekker motivasjonen for strømming, tilgjengelige transportmekanismer, hvordan man implementerer strømmbar HTTP i MCP, sikkerhetsbeste praksis, migrering fra SSE, og praktisk veiledning for å bygge egne strømmende MCP-applikasjoner. 

> [!WARNING]
> Implementeringseksemplene i denne leksjonen retter seg mot **MCP-spesifikasjonen
> `2025-11-25`** og demonstrerer den legacy `initialize`-håndtrykkprotokollen,
> `Mcp-Session-Id`, GET event stream og resumabilitetsmodellen. MCP `2026-07-28`
> fjerner disse funksjonene. Nåværende strømmende HTTP-forespørsler er selvstendige
> POST-forespørsler med headerne `MCP-Protocol-Version` og `Mcp-Method`, samt
> `Mcp-Name` der det kreves. Se
> [Hva er endret i MCP: Spesifikasjonen 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28.md)
> før du bruker disse eksemplene i en ny implementering.

## Transportmekanismer og strømming i MCP

Denne seksjonen utforsker de forskjellige transportmekanismene tilgjengelig i MCP og deres rolle i å muliggjøre strømmemuligheter for sanntidskommunikasjon mellom klienter og servere.

### Hva er en transportmekanisme?

En transportmekanisme definerer hvordan data utveksles mellom klient og server. MCP støtter flere transporttyper for å passe forskjellige miljøer og krav:

- **stdio**: Standard inn/ut, egnet for lokale og CLI-baserte verktøy. Enkelt men ikke egnet for web eller sky.
- **HTTP+SSE**: Den gamle fjerntransporten, utrangert i MCP `2025-03-26`
    og erstattet av Strømmbar HTTP. Ikke bruk den for nye implementeringer.
- **Strømmbar HTTP**: Moderne HTTP-basert strømmetransport, som støtter varsler og bedre skalerbarhet. Anbefales for de fleste produksjons- og skyscenarier.

### Sammenligningstabell

Ta en titt på sammenligningstabellen under for å forstå forskjellene mellom disse transportmekanismene:

| Transport | Status | Varsler | Typisk bruk |
|---|---|---|---|
| stdio | Nåværende | Ja | Lokale underprosesser |
| HTTP+SSE | Utrangert | Ja | Eldre fjernimplementeringer |
| Strømmbar HTTP | Nåværende | Ja | Fjern- og skyservere |

> **Tips:** Valg av riktig transport påvirker ytelse, skalerbarhet og brukeropplevelse. **Strømmbar HTTP** anbefales for moderne, skalerbare og skyklare applikasjoner.

De standard transportene er stdio og Strømmbar HTTP. HTTP+SSE forekommer kun i
eldre eksempler.

## Strømming: Konsepter og motivasjon

Å forstå de grunnleggende konseptene og motivasjonene bak strømming er essensielt for å implementere effektive systemer for sanntidskommunikasjon.

**Strømming** er en teknikk i nettverksprogrammering som tillater data å sendes og mottas i små, håndterbare deler eller som en sekvens av hendelser, i stedet for å vente på at hele responsen skal være klar. Dette er spesielt nyttig for:

- Store filer eller datasett.
- Sanntidsoppdateringer (f.eks. chat, fremdriftsindikatorer).
- Langvarige beregninger hvor man ønsker å holde brukeren informert.

Her er hva du trenger å vite om strømming på et overordnet nivå:

- Data leveres gradvis, ikke alt på en gang.
- Klienten kan behandle data etter hvert som den ankommer.
- Reduserer opplevd ventetid og forbedrer brukeropplevelsen.

### Hvorfor bruke strømming?

Årsakene til å bruke strømming er følgende:

- Brukere får tilbakemelding umiddelbart, ikke bare i slutten
- Muliggjør sanntidsapplikasjoner og responsive brukergrensesnitt
- Mer effektiv bruk av nettverk og beregningsressurser

### Enkelt eksempel: HTTP streamingserver og -klient

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

Dette eksemplet demonstrerer en server som sender en serie meldinger til klienten etter hvert som de blir tilgjengelige, i stedet for å vente på at alle meldinger skal være klare.

**Hvordan det fungerer:**

- Serveren sender hver melding etter hvert som den er klar.
- Klienten mottar og skriver ut hver del etter hvert som den ankommer.

**Krav:**

- Serveren må bruke en strømmerespons (f.eks. `StreamingResponse` i FastAPI).
- Klienten må behandle responsen som en strøm (`stream=True` i requests).
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

**Java-implementasjonsnotater:**

- Bruker Spring Boots reaktive stabel med `Flux` for strømming
- `ServerSentEvent` gir strukturert hendelsesstrømming med hendelsestyper
- `WebClient` med `bodyToFlux()` muliggjør reaktiv strømforbruk
- `delayElements()` simulerer behandlingstid mellom hendelser
- Hendelser kan ha typer (`info`, `result`) for bedre klienthåndtering

### Sammenligning: Klassisk strømming vs MCP strømming

Forskjellene mellom hvordan strømming fungerer på en "klassisk" måte versus hvordan det fungerer i MCP kan fremstilles slik:

| Egenskap                | Klassisk HTTP Strømming         | MCP Strømming (Varsler)      |
|------------------------|-------------------------------|-------------------------------------|
| Hovedrespons           | Delt opp i biter               | Enkel, på slutten                      |
| Fremdriftsoppdateringer | Sendes som databit             | Sendes som varsler                    |
| Klientkrav             | Må behandle strøm              | Må implementere meldingshåndterer     |
| Bruksområde            | Store filer, AI token-strømmer | Fremdrift, logger, sanntids tilbakemelding |

### Viktige observerte forskjeller

I tillegg, her er noen viktige forskjeller:

- **Kommunikasjonsmønster:**
  - Klassisk HTTP strømming: Bruker enkel overføringskoding med oppdeling i biter for å sende data
  - MCP strømming: Bruker et strukturert varslingssystem med JSON-RPC-protokoll

- **Meldingsformat:**
  - Klassisk HTTP: Vanlige tekstbiter med linjeskift
  - MCP: Strukturert LoggingMessageNotification-objekter med metadata

- **Klientimplementasjon:**
  - Klassisk HTTP: Enkelt klient som behandler strømmende responser
  - MCP: Mer sofistikert klient med meldingshåndterer for å behandle forskjellige meldingstyper

- **Fremdriftsoppdateringer:**
  - Klassisk HTTP: Fremdriften er en del av hovedstrømmen
  - MCP: Fremdriften sendes via separate varslingsmeldinger mens hovedresponsen kommer til slutt

### Anbefalinger

Det er noen ting vi anbefaler når det gjelder valg mellom å implementere klassisk strømming (som et endepunkt vi viste deg over med `/stream`) versus å velge strømming via MCP.

- **For enkle strømmingsbehov:** Klassisk HTTP strømming er enklere å implementere og tilstrekkelig for grunnleggende strømming.

- **For komplekse, interaktive apper:** MCP strømming gir en mer strukturert tilnærming med rikere metadata og separasjon mellom varsler og endelige resultater.

- **For AI-applikasjoner:** MCP sitt varslingssystem er spesielt nyttig for langvarige AI-oppgaver hvor man ønsker å holde brukerne informert om fremdrift.

## Strømming i MCP

Ok, så du har sett noen anbefalinger og sammenligninger så langt på forskjellen mellom klassisk strømming og strømming i MCP. La oss gå i detalj på hvordan du kan utnytte strømming i MCP.

Å forstå hvordan strømming fungerer innenfor MCP-rammeverket er viktig for å bygge responsive applikasjoner som gir sanntids tilbakemelding til brukere under langvarige operasjoner.

I MCP handler strømming ikke om å sende hovedresponsen i biter, men om å sende **varsler** til klienten mens et verktøy behandler en forespørsel. Disse varslene kan inkludere fremdriftsoppdateringer, logger eller andre hendelser.

### Hvordan det fungerer

Hovedresultatet sendes fortsatt som en enkelt respons. Men varsler kan sendes som separate meldinger under prosessering og dermed oppdatere klienten i sanntid. Klienten må kunne håndtere og vise disse varslene.

### Valgfri øvelse: koble til en hostet MCP-server

Du kan også bruke Strømmbar HTTP uten å kjøre en lokal server. Dette eksemplet
kobler til [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
oppdager dens verktøy, og søker etter offentlig MCP-dokumentasjon ved bruk av samme
Python SDK som den [lokale klienten](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Parallels anonyme endepunkt krever ingen konto eller API-nøkkel. Gratis tilgang er
rate-begrenset. Å kjøre dette skriptet sender søkespørringer, målsetning og en
tilfeldig sesjonsidentifikator til Parallel. Tjenesten tilbyr også `web_fetch`,
som sender forespurte URL-er og eventuell gitt kontekst til Parallel. Bruk offentlig
informasjon for denne øvelsen; se deres [vilkår](https://parallel.ai/customer-terms)
og [personvernpolicy](https://parallel.ai/privacy-policy).

Med Python 3.10 eller nyere og et virtuelt miljø aktivert, installer SDK-en:

```sh
python -m pip install "mcp>=1.10,<2"
```

Lagre dette som `hosted_search.py` og kjør `python hosted_search.py`:

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

Forvent at oppdagelsen inkluderer `web_search` og `web_fetch`, etterfulgt av et søke-
respons som inneholder kilde-URLer og utdrag. Resultater kan variere eller være tomme.
Skriptet sjekker `isError` fordi et verktøy kan feile selv om HTTP-forespørselen
lykkes. Dersom tilgang er rate-begrenset, vent før du prøver igjen. Gjenbruk den samme
`session_id` hvis du utvider skriptet med relaterte søke- eller hentekall.

Strømmbar HTTP tillater både JSON- og SSE-responser; denne serveren kan returnere et
komplett JSON-resultat uten fremdriftsvarsler. SDK-en håndterer
transporten. Fortsett med det lokale eksempelet under for å lære om varsler.
Dette valgfrie skriptet gjør ett eksplisitt søk og lukker forbindelsen når
det er ferdig. Hvis du senere eksponerer disse verktøyene for en agent, kan agenten kalle
dem under sitt arbeid; behandl hentet webtekst som ubetrodd data.

## Hva er et varsel?

Vi sa "varsel", hva betyr det i MCP-kontekst?

Et varsel er en JSON-RPC-melding som ikke har en `id` og ikke
mottar svar. MCP bruker varsler for fremdrift, kansellering og
andre enveis hendelser.

I MCP `2025-11-25` sender en klient `notifications/initialized` etter
initialiseringshåndtrykket. MCP `2026-07-28` har ikke initialiseringshåndtrykk, så
dette varselet er legacy-adferd.

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

Logging er en funksjon som bruker varsler; selve varsler er en
generell JSON-RPC-meldingstype.

> **Utrangert i MCP `2026-07-28`:** Logging-funksjonen forblir tilgjengelig
> for kompatibilitet men er kandidat for fjerning i første spesifikasjons-
> revisjon utgitt på eller etter 28. juli 2027. Nye implementeringer bør bruke
> `stderr` med stdio eller OpenTelemetry for strukturert observabilitet.

For en legacy `2025-11-25` implementering, aktiverer serveren Logging-
funksjonen som følger:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Avhengig av SDK brukt, kan logging være aktivert som standard, eller du må eksplisitt aktivere det i serverkonfigurasjonen.

Det finnes forskjellige typer varsler:

| Nivå      | Beskrivelse                   | Eksempel på bruk               |
|-----------|------------------------------|-------------------------------|
| debug     | Detaljert feilsøkingsinfo     | Funksjonsinngang/-utgang      |
| info      | Generelle informasjonsmeldinger | Fremdriftsoppdateringer       |
| notice    | Normale men viktige hendelser | Konfigurasjonsendringer       |
| warning   | Advarselsforhold              | Bruk av utdatert funksjon     |
| error     | Feilforhold                  | Operasjonsfeil                |
| critical  | Kritiske forhold             | Systemkomponentfeil           |
| alert     | Handling må utføres umiddelbart | Datakorrupsjon oppdaget      |
| emergency | Systemet er ubrukelig        | Fullstendig systemsvikt       |

## Implementering av varsler i MCP

For å implementere varsler i MCP må både server- og klientsiden settes opp til å håndtere sanntidsoppdateringer. Dette gjør at applikasjonen din kan gi umiddelbar tilbakemelding til brukere under langvarige operasjoner.

### Server-side: Sende varsler

La oss starte med serversiden. I MCP definerer du verktøy som kan sende varsler mens de behandler forespørsler. Serveren bruker kontekstobjektet (vanligvis `ctx`) for å sende meldinger til klienten.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

I det foregående eksempelet sender `process_files`-verktøyet tre varsler til klienten mens det behandler hver fil. Metoden `ctx.info()` brukes for å sende informasjonsmeldinger.

I tillegg, for å aktivere varsler, sørg for at serveren din bruker en strømmetransport (som `streamable-http`) og at klienten din implementerer en meldingshåndterer for å behandle varsler. Slik kan du sette opp serveren til å bruke `streamable-http` transporten:

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

I dette .NET-eksempelet er `ProcessFiles`-verktøyet dekorert med `Tool`-attributt og sender tre varsler til klienten mens det behandler hver fil. Metoden `ctx.Info()` brukes for å sende informasjonsmeldinger.

For å aktivere varsler i din .NET MCP-server, sørg for at du bruker en strømmetransport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klientside: Motta varsler

Klienten må implementere en meldingshåndterer for å behandle og vise varsler når de ankommer.

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

I den foregående koden sjekker `message_handler`-funksjonen om den innkommende meldingen er et varsel. Hvis den er det, skriver den ut varselet; ellers prosesseres den som en vanlig servermelding. Legg også merke til at `ClientSession` initialiseres med `message_handler` for å håndtere innkommende varsler.

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


I dette .NET-eksempelet sjekker `MessageHandler`-funksjonen om den innkommende meldingen er en varsling. Hvis det er en varsling, skriver den ut varslingen; ellers prosesserer den meldingen som en vanlig servermelding. `ClientSession` blir initialisert med meldingsbehandleren via `ClientSessionOptions`.

For å aktivere varslinger, sørg for at serveren din bruker en streaming-transport (som `streamable-http`) og at klienten din implementerer en meldingsbehandler for å prosessere varslinger.

## Fremdriftsvarsler og scenarier

Denne delen forklarer konseptet med fremdriftsvarsler i MCP, hvorfor de er viktige, og hvordan man kan implementere dem med Streamable HTTP. Du finner også en praktisk oppgave for å styrke forståelsen din.

Fremdriftsvarsler er sanntidsmeldinger som sendes fra serveren til klienten under langvarige operasjoner. I stedet for å vente til hele prosessen er ferdig, holder serveren klienten oppdatert om gjeldende status. Dette forbedrer transparens, brukeropplevelse og gjør feilsøking enklere.

**Eksempel:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Hvorfor bruke fremdriftsvarsler?

Fremdriftsvarsler er viktige av flere grunner:

- **Bedre brukeropplevelse:** Brukere ser oppdateringer mens arbeidet pågår, ikke bare når det er ferdig.
- **Sanntids tilbakemelding:** Klienter kan vise fremdriftslinjer eller logger, noe som gjør applikasjonen mer responsiv.
- **Enklere feilsøking og overvåking:** Utviklere og brukere kan se hvor en prosess kan være treg eller satt fast.

### Hvordan implementere fremdriftsvarsler

Slik kan du implementere fremdriftsvarsler i MCP:

- **På serveren:** Bruk `ctx.info()` eller `ctx.log()` for å sende varsler etter hvert som hvert element blir behandlet. Dette sender en melding til klienten før hovedresultatet er klart.
- **På klienten:** Implementer en meldingsbehandler som lytter etter og viser varsler etter hvert som de kommer inn. Denne behandleren skiller mellom varsler og endelig resultat.

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

Sikkerhet bør være en topp prioritet når man implementerer hvilken som helst server, spesielt når man bruker HTTP-baserte transporter som Streamable HTTP i MCP.

Når man implementerer MCP-servere med HTTP-baserte transporter, blir sikkerhet en svært viktig bekymring som krever nøye oppmerksomhet mot flere angrepsvektorer og beskyttelsesmekanismer.

### Oversikt

Sikkerhet er kritisk når MCP-servere eksponeres over HTTP. Streamable HTTP introduserer nye angrepsflater og krever nøye konfigurasjon.

Her er noen sentrale sikkerhetshensyn:

- **Validering av Origin-header**: Alltid valider `Origin`-headeren for å forhindre DNS-rebinding-angrep.
- **Binding til Localhost**: For lokal utvikling, bind servere til `localhost` for å unngå eksponering mot det offentlige nettet.
- **Autentisering**: Implementer autentisering (f.eks. API-nøkler, OAuth) for produksjonsdistribusjoner.
- **CORS**: Konfigurer Cross-Origin Resource Sharing (CORS)-politikker for å begrense tilgang.
- **HTTPS**: Bruk HTTPS i produksjon for å kryptere trafikken.

### Beste praksis

I tillegg er det noen beste praksiser å følge når du implementerer sikkerhet i din MCP streaming-server:

- Stol aldri på innkommende forespørsler uten validering.
- Loggfør og overvåk all tilgang og feil.
- Oppdater avhengigheter regelmessig for å tette sikkerhetssårbarheter.

### Utfordringer

Du vil møte noen utfordringer når du implementerer sikkerhet i MCP streaming-servere:

- Å balansere sikkerhet med enkel utvikling
- Å sikre kompatibilitet med forskjellige klientmiljøer


## Oppgradering fra SSE til Streamable HTTP

For applikasjoner som for øyeblikket bruker Server-Sent Events (SSE), gir migrasjon til Streamable HTTP økte muligheter og bedre langsiktig bærekraft for MCP-implementasjoner.

### Hvorfor oppgradere?

Det finnes to overbevisende grunner til å oppgradere fra SSE til Streamable HTTP:

- Streamable HTTP tilbyr bedre skalerbarhet, kompatibilitet og rikere støtten for varslinger enn SSE.
- Det er den anbefalte transporten for nye MCP-applikasjoner.

### Migrasjonstrinn

Slik kan du migrere fra SSE til Streamable HTTP i dine MCP-applikasjoner:

- **Oppdater serverkoden** til å bruke `transport="streamable-http"` i `mcp.run()`.
- **Oppdater klientkoden** til å bruke `streamablehttp_client` i stedet for SSE-klient.
- **Implementer en meldingsbehandler** i klienten for å behandle varslinger.
- **Test for kompatibilitet** med eksisterende verktøy og arbeidsflyter.

### Opprettholde kompatibilitet

Det anbefales å opprettholde kompatibilitet med eksisterende SSE-klienter under migrasjonsprosessen. Her er noen strategier:

- Du kan støtte både SSE og Streamable HTTP ved å kjøre begge transportene på forskjellige endepunkter.
- Migrer klienter gradvis til den nye transporten.

### Utfordringer

Sørg for at du håndterer følgende utfordringer under migrasjonen:

- Å sikre at alle klienter er oppdatert
- Å håndtere forskjeller i levering av varslinger

### Oppgave: Bygg din egen streaming MCP-app

**Scenario:**
Bygg en MCP-server og klient der serveren prosesserer en liste med elementer (for eksempel filer eller dokumenter) og sender en varsling for hvert element som behandles. Klienten skal vise hver varsling når den kommer inn.

**Trinn:**

1. Implementer et serververktøy som prosesserer en liste og sender varslinger for hvert element.
2. Implementer en klient med en meldingsbehandler for å vise varslinger i sanntid.
3. Test implementasjonen ved å kjøre både server og klient, og observer varslingene.

[Løsning](./solution/README.md)

## Videre lesning og hva nå?

For å fortsette reisen din med MCP-streaming og utvide kunnskapen din, gir denne seksjonen flere ressurser og foreslåtte neste steg for å bygge mer avanserte applikasjoner.

### Videre lesning

- [Microsoft: Introduksjon til HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS i ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Hva nå?

- Prøv å bygge mer avanserte MCP-verktøy som bruker streaming for sanntidsanalyse, chat eller samarbeid om redigering.
- Utforsk integrasjon av MCP-streaming med frontend-rammeverk (React, Vue, osv.) for levende UI-oppdateringer.
- Neste: [Bruke AI Toolkit for VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->