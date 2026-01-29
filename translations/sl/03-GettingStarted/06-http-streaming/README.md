# HTTPS pretakanje z Model Context Protocol (MCP)

To poglavje ponuja celovit vodnik za implementacijo varnega, skalabilnega in realnočasovnega pretakanja z Model Context Protocol (MCP) prek HTTPS. Pokriva motivacijo za pretakanje, razpoložljive transportne mehanizme, kako implementirati pretakanje HTTP v MCP, najboljše prakse za varnost, migracijo iz SSE ter praktične smernice za gradnjo lastnih aplikacij za pretakanje MCP.

## Transportni mehanizmi in pretakanje v MCP

Ta razdelek raziskuje različne transportne mehanizme, ki so na voljo v MCP, in njihovo vlogo pri omogočanju zmogljivosti pretakanja za realnočasovno komunikacijo med odjemalci in strežniki.

### Kaj je transportni mehanizem?

Transportni mehanizem določa, kako se podatki izmenjujejo med odjemalcem in strežnikom. MCP podpira več vrst transporta, da ustreza različnim okoljem in zahtevam:

- **stdio**: Standardni vhod/izhod, primeren za lokalna orodja in orodja CLI. Enostaven, vendar ni primeren za splet ali oblak.
- **SSE (Server-Sent Events)**: Omogoča strežnikom, da prek HTTP pošiljajo realnočasovne posodobitve odjemalcem. Dobro za spletne uporabniške vmesnike, vendar omejeno glede skalabilnosti in prilagodljivosti.
- **Streamable HTTP**: Sodobni transport na osnovi HTTP za pretakanje, ki podpira obvestila in boljšo skalabilnost. Priporočljivo za večino produkcijskih in oblačnih scenarijev.

### Primerjalna tabela

Oglejte si primerjalno tabelo spodaj, da razumete razlike med temi transportnimi mehanizmi:

| Transport         | Realnočasovne posodobitve | Pretakanje | Skalabilnost | Primer uporabe          |
|-------------------|--------------------------|------------|-------------|-------------------------|
| stdio             | Ne                       | Ne         | Nizka       | Lokalna orodja CLI      |
| SSE               | Da                       | Da         | Srednja     | Splet, realnočasovne posodobitve |
| Streamable HTTP   | Da                       | Da         | Visoka      | Oblak, več odjemalcev   |

> **Nasvet:** Izbira pravega transporta vpliva na zmogljivost, skalabilnost in uporabniško izkušnjo. **Streamable HTTP** je priporočljiv za sodobne, skalabilne in oblačne aplikacije.

Opazite transporte stdio in SSE, ki so bili predstavljeni v prejšnjih poglavjih, ter kako je streamable HTTP transport, ki ga pokriva to poglavje.

## Pretakanje: Koncepti in motivacija

Razumevanje temeljnih konceptov in motivacije za pretakanje je ključno za implementacijo učinkovitih sistemov za realnočasovno komunikacijo.

**Pretakanje** je tehnika v omrežnem programiranju, ki omogoča pošiljanje in prejemanje podatkov v majhnih, obvladljivih delih ali kot zaporedje dogodkov, namesto da bi čakali, da je celoten odgovor pripravljen. To je še posebej uporabno za:

- Velike datoteke ali nabore podatkov.
- Realnočasovne posodobitve (npr. klepet, napredovalne vrstice).
- Dolgotrajne izračune, kjer želite obveščati uporabnika.

Tukaj je, kaj morate vedeti o pretakanju na visoki ravni:

- Podatki se dostavljajo postopoma, ne naenkrat.
- Odjemalec lahko obdeluje podatke, ko prispejo.
- Zmanjšuje zaznano zakasnitev in izboljšuje uporabniško izkušnjo.

### Zakaj uporabljati pretakanje?

Razlogi za uporabo pretakanja so naslednji:

- Uporabniki dobijo povratne informacije takoj, ne šele na koncu.
- Omogoča realnočasovne aplikacije in odzivne uporabniške vmesnike.
- Bolj učinkovita uporaba omrežnih in računalniških virov.

### Preprost primer: HTTP strežnik za pretakanje in odjemalec

Tukaj je preprost primer, kako lahko implementirate pretakanje:

#### Python

**Strežnik (Python, z uporabo FastAPI in StreamingResponse):**

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

**Odjemalec (Python, z uporabo requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Ta primer prikazuje strežnik, ki pošilja serijo sporočil odjemalcu, ko postanejo na voljo, namesto da bi čakal, da so vsa sporočila pripravljena.

**Kako deluje:**

- Strežnik pošilja vsako sporočilo, ko je pripravljeno.
- Odjemalec prejme in natisne vsak del, ko prispe.

**Zahteve:**

- Strežnik mora uporabljati pretakanje odgovorov (npr. `StreamingResponse` v FastAPI).
- Odjemalec mora obdelovati odgovor kot tok (`stream=True` v requests).
- Content-Type je običajno `text/event-stream` ali `application/octet-stream`.

#### Java

**Strežnik (Java, z uporabo Spring Boot in Server-Sent Events):**

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

**Odjemalec (Java, z uporabo Spring WebFlux WebClient):**

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

**Opombe o implementaciji v Javi:**

- Uporablja reaktivni sklad Spring Boot z `Flux` za pretakanje.
- `ServerSentEvent` omogoča strukturirano pretakanje dogodkov z vrstami dogodkov.
- `WebClient` z `bodyToFlux()` omogoča reaktivno porabo pretakanja.
- `delayElements()` simulira čas obdelave med dogodki.
- Dogodki lahko imajo vrste (`info`, `result`) za boljše ravnanje odjemalca.

### Primerjava: Klasično pretakanje vs. MCP pretakanje

Razlike med tem, kako pretakanje deluje na "klasičen" način, in tem, kako deluje v MCP, so prikazane tako:

| Značilnost          | Klasično HTTP pretakanje         | MCP pretakanje (Obvestila)         |
|---------------------|----------------------------------|------------------------------------|
| Glavni odgovor      | Razdeljen na dele               | Enoten, na koncu                  |
| Posodobitve napredka| Poslane kot podatkovni deli      | Poslane kot obvestila             |
| Zahteve odjemalca   | Mora obdelovati tok             | Mora implementirati obdelovalnik sporočil |
| Primer uporabe      | Velike datoteke, AI tokovi      | Napredek, dnevniki, realnočasovne povratne informacije |

### Opazne razlike

Dodatno, tukaj so ključne razlike:

- **Vzorec komunikacije:**
  - Klasično HTTP pretakanje: Uporablja preprosto kodiranje prenosa v delih za pošiljanje podatkov v delih.
  - MCP pretakanje: Uporablja strukturiran sistem obvestil z JSON-RPC protokolom.

- **Oblika sporočila:**
  - Klasično HTTP: Navadno besedilo v delih z novimi vrsticami.
  - MCP: Strukturirani objekti LoggingMessageNotification z metapodatki.

- **Implementacija odjemalca:**
  - Klasično HTTP: Preprost odjemalec, ki obdeluje pretakajoče odgovore.
  - MCP: Bolj sofisticiran odjemalec z obdelovalnikom sporočil za obdelavo različnih vrst sporočil.

- **Posodobitve napredka:**
  - Klasično HTTP: Napredek je del glavnega toka odgovora.
  - MCP: Napredek je poslan prek ločenih obvestilnih sporočil, medtem ko glavni odgovor pride na koncu.

### Priporočila

Obstajajo nekatera priporočila glede izbire med implementacijo klasičnega pretakanja (kot prikazano zgoraj z uporabo `/stream`) in izbiro pretakanja prek MCP.

- **Za preproste potrebe pretakanja:** Klasično HTTP pretakanje je enostavnejše za implementacijo in zadostuje za osnovne potrebe pretakanja.

- **Za kompleksne, interaktivne aplikacije:** MCP pretakanje ponuja bolj strukturiran pristop z bogatejšimi metapodatki in ločitvijo med obvestili in končnimi rezultati.

- **Za AI aplikacije:** MCP-jev sistem obvestil je še posebej uporaben za dolgotrajne AI naloge, kjer želite uporabnike obveščati o napredku.

## Pretakanje v MCP

Ok, videli ste nekaj priporočil in primerjav glede razlike med klasičnim pretakanjem in pretakanjem v MCP. Poglejmo podrobno, kako lahko izkoristite pretakanje v MCP.

Razumevanje, kako pretakanje deluje znotraj MCP okvira, je ključno za gradnjo odzivnih aplikacij, ki uporabnikom zagotavljajo realnočasovne povratne informacije med dolgotrajnimi operacijami.

V MCP pretakanje ne pomeni pošiljanja glavnega odgovora v delih, temveč pošiljanje **obvestil** odjemalcu medtem ko orodje obdeluje zahtevo. Ta obvestila lahko vključujejo posodobitve napredka, dnevnike ali druge dogodke.

### Kako deluje

Glavni rezultat je še vedno poslan kot enoten odgovor. Vendar pa se obvestila lahko pošiljajo kot ločena sporočila med obdelavo in s tem v realnem času posodabljajo odjemalca. Odjemalec mora biti sposoben obdelovati in prikazovati ta obvestila.

## Kaj je obvestilo?

Rekli smo "obvestilo", kaj to pomeni v kontekstu MCP?

Obvestilo je sporočilo, ki ga strežnik pošlje odjemalcu, da ga obvesti o napredku, statusu ali drugih dogodkih med dolgotrajno operacijo. Obvestila izboljšajo transparentnost in uporabniško izkušnjo.

Na primer, odjemalec mora poslati obvestilo, ko je začetni stisk roke s strežnikom opravljen.

Obvestilo izgleda kot JSON sporočilo:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Obvestila spadajo v temo v MCP, imenovano ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Da bi dnevniki delovali, mora strežnik omogočiti to funkcijo/zmožnost, kot sledi:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Odvisno od uporabljenega SDK-ja so dnevniki morda privzeto omogočeni ali pa jih morate izrecno omogočiti v konfiguraciji strežnika.

Obstajajo različne vrste obvestil:

| Raven     | Opis                          | Primer uporabe                  |
|-----------|-------------------------------|---------------------------------|
| debug     | Podrobne informacije za odpravljanje napak | Vstopne/izstopne točke funkcij |
| info      | Splošna informativna sporočila | Posodobitve napredka operacije |
| notice    | Normalni, a pomembni dogodki  | Spremembe konfiguracije         |
| warning   | Opozorilni pogoji             | Uporaba zastarele funkcije      |
| error     | Pogoji napake                 | Neuspehi operacije              |
| critical  | Kritični pogoji               | Neuspehi sistemskih komponent   |
| alert     | Takoj je treba ukrepati       | Zaznana poškodba podatkov       |
| emergency | Sistem ni uporaben            | Popolna odpoved sistema         |

## Implementacija obvestil v MCP

Za implementacijo obvestil v MCP morate nastaviti tako strežniško kot odjemalsko stran za obdelavo realnočasovnih posodobitev. To omogoča vaši aplikaciji, da med dolgotrajnimi operacijami zagotavlja takojšnje povratne informacije uporabnikom.

### Strežniška stran: Pošiljanje obvestil

Začnimo s strežniško stranjo. V MCP definirate orodja, ki lahko pošiljajo obvestila med obdelavo zahtev. Strežnik uporablja objekt konteksta (običajno `ctx`) za pošiljanje sporočil odjemalcu.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

V zgornjem primeru orodje `process_files` pošlje tri obvestila odjemalcu, ko obdeluje vsako datoteko. Metoda `ctx.info()` se uporablja za pošiljanje informativnih sporočil.

Poleg tega, da omogočite obvestila, poskrbite, da vaš strežnik uporablja transport za pretakanje (kot je `streamable-http`) in vaš odjemalec implementira obdelovalnik sporočil za obdelavo obvestil. Tukaj je, kako lahko nastavite strežnik za uporabo transporta `streamable-http`:

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

V tem .NET primeru je orodje `ProcessFiles` označeno z atributom `Tool` in pošlje tri obvestila odjemalcu, ko obdeluje vsako datoteko. Metoda `ctx.Info()` se uporablja za pošiljanje informativnih sporočil.

Za omogočanje obvestil v vašem .NET MCP strežniku poskrbite, da uporabljate transport za pretakanje:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Odjemalska stran: Sprejemanje obvestil

Odjemalec mora implementirati obdelovalnik sporočil za obdelavo in prikaz obvestil, ko prispejo.

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

V zgornji kodi funkcija `message_handler` preveri, ali je dohodno sporočilo obvestilo. Če je, natisne obvestilo; sicer ga obdeluje kot običajno strežniško sporočilo. Prav tako opazite, kako je `ClientSession` inicializiran z `message_handler`, da obravnava dohodna obvestila.

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

V tem .NET primeru funkcija `MessageHandler` preveri, ali je dohodno sporočilo obvestilo. Če je, natisne obvestilo; sicer ga obdeluje kot običajno strežniško sporočilo. `ClientSession` je inicializiran z obdelovalnikom sporočil prek `ClientSessionOptions`.

Za omogočanje obvestil poskrbite, da vaš strežnik uporablja transport za pretakanje (kot je `streamable-http`) in vaš odjemalec implementira obdelovalnik sporočil za obdelavo obvestil.

## Posodobitve napredka in scenariji

Ta razdelek pojasnjuje koncept posodobitev napredka v MCP, zakaj so pomembne in kako jih implementirati z uporabo Streamable HTTP. Prav tako boste našli praktično nalogo za utrditev vašega razumevanja.

Posodobitve napredka so realnočasovna sporočila, ki jih strežnik pošlje odjemalcu med dolgotrajnimi operacijami. Namesto da bi čakali, da se celoten proces zaključi, strežnik obvešča odjemalca o trenutnem statusu. To izboljša transparentnost, uporabniško izkušnjo in olajša odpravljanje napak.

**Primer:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Zakaj uporabljati posodobitve napredka?

Posodobitve napredka so ključne iz več razlogov:

- **Boljša uporabniška izkušnja:** Uporabniki vidijo posodobitve, ko delo napreduje, ne šele na koncu.
- **Realnočasovne povratne informacije:** Odjemalci lahko prikazujejo napredovalne vrstice ali dnevnike, kar aplikacijo naredi odzivno.
- **Lažje odpravljanje napak in spremljanje:** Razvijalci in uporabniki lahko vidijo, kje je proces morda počasen ali zataknjen.

### Kako implementirati posodobitve napredka

Tukaj je, kako lahko implementirate posodobitve napredka v MCP:

- **Na strežniku:** Uporabite `ctx.info()` ali `ctx.log()` za pošiljanje obvestil, ko se vsak element obdeluje. To pošlje sporočilo odjemalcu pred pripravo glavnega rezultata.
- **Na odjemalcu:** Implementirajte obdelovalnik sporočil, ki posluša in prikazuje obvestila, ko prispejo. Ta obdelovalnik razlikuje med obvestili in končnim rezultatom.

**Primer strežnika:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Primer odjemalca:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Varnostni vidiki

Pri implementaciji MCP strežnikov z transporti na osnovi HTTP postane varnost ključna skrb, ki zahteva pozornost na več vektorjev napadov in zaščitne mehanizme.

### Pregled

Varnost je ključna pri izpostavljanju MCP strežnikov prek HTTP. Streamable HTTP uvaja nove površine napadov in zahteva skrbno konfiguracijo.

### Ključne točke

- **Validacija glave Origin**: Vedno validirajte glavo `Origin`, da preprečite napade DNS rebinding.
- **Vezava na localhost**: Za lokalni razvoj vežite strežnike na `localhost`, da jih ne izpostavljate javnemu internetu.
- **Avtentikacija**: Implementirajte avtentikacijo (npr. API ključi, OAuth) za produkcijske namestitve.
- **CORS**: Konfigurirajte politike Cross-Origin Resource Sharing (CORS) za omejitev dostopa.
- **HTTPS**: Uporabljajte HTTPS v produkciji za šifriranje prometa.

### Najboljše pr
Obstajata dva prepričljiva razloga za nadgradnjo iz SSE na Streamable HTTP:

- Streamable HTTP ponuja boljšo razširljivost, združljivost in bogatejšo podporo za obvestila kot SSE.
- Priporočen je kot transport za nove MCP aplikacije.

### Koraki migracije

Tukaj je opisano, kako lahko migrirate iz SSE na Streamable HTTP v svojih MCP aplikacijah:

- **Posodobite strežniško kodo**, da uporabite `transport="streamable-http"` v `mcp.run()`.
- **Posodobite odjemalsko kodo**, da uporabite `streamablehttp_client` namesto SSE odjemalca.
- **Implementirajte obdelovalnik sporočil** v odjemalcu za obdelavo obvestil.
- **Preverite združljivost** z obstoječimi orodji in delovnimi procesi.

### Ohranitev združljivosti

Priporočljivo je ohraniti združljivost z obstoječimi SSE odjemalci med procesom migracije. Tukaj je nekaj strategij:

- Podpirate lahko tako SSE kot Streamable HTTP, tako da oba transporta zaženete na različnih končnih točkah.
- Postopoma migrirajte odjemalce na nov transport.

### Izzivi

Poskrbite, da boste med migracijo obravnavali naslednje izzive:

- Zagotoviti, da so vsi odjemalci posodobljeni
- Obvladovanje razlik v dostavi obvestil

## Varnostni vidiki

Varnost mora biti glavna prioriteta pri implementaciji katerega koli strežnika, še posebej pri uporabi transportov na osnovi HTTP, kot je Streamable HTTP v MCP.

Pri implementaciji MCP strežnikov z transporti na osnovi HTTP postane varnost ključna skrb, ki zahteva pozornost na več vektorjev napadov in zaščitne mehanizme.

### Pregled

Varnost je ključna pri izpostavljanju MCP strežnikov prek HTTP. Streamable HTTP uvaja nove površine za napade in zahteva skrbno konfiguracijo.

Tukaj je nekaj ključnih varnostnih vidikov:

- **Validacija glave Origin**: Vedno validirajte glavo `Origin`, da preprečite napade DNS rebinding.
- **Povezava na localhost**: Za lokalni razvoj povežite strežnike na `localhost`, da jih ne izpostavite javnemu internetu.
- **Avtentikacija**: Implementirajte avtentikacijo (npr. API ključe, OAuth) za produkcijske namestitve.
- **CORS**: Konfigurirajte politike Cross-Origin Resource Sharing (CORS) za omejitev dostopa.
- **HTTPS**: Uporabljajte HTTPS v produkciji za šifriranje prometa.

### Najboljše prakse

Poleg tega sledite najboljšim praksam pri implementaciji varnosti v vašem MCP strežniku za pretakanje:

- Nikoli ne zaupajte dohodnim zahtevam brez validacije.
- Beležite in spremljajte ves dostop in napake.
- Redno posodabljajte odvisnosti za odpravo varnostnih ranljivosti.

### Izzivi

Pri implementaciji varnosti v MCP strežnikih za pretakanje se boste soočili z nekaterimi izzivi:

- Iskanje ravnovesja med varnostjo in enostavnostjo razvoja
- Zagotavljanje združljivosti z različnimi odjemalskimi okolji

### Naloga: Zgradite svojo aplikacijo za pretakanje MCP

**Scenarij:**
Zgradite MCP strežnik in odjemalca, kjer strežnik obdela seznam elementov (npr. datotek ali dokumentov) in pošlje obvestilo za vsak obdelan element. Odjemalec naj prikaže vsako obvestilo takoj, ko prispe.

**Koraki:**

1. Implementirajte strežniško orodje, ki obdela seznam in pošlje obvestila za vsak element.
2. Implementirajte odjemalca z obdelovalnikom sporočil za prikaz obvestil v realnem času.
3. Preizkusite svojo implementacijo tako, da zaženete strežnik in odjemalca ter opazujete obvestila.

[Rešitev](./solution/README.md)

## Nadaljnje branje in kaj sledi?

Za nadaljevanje vaše poti z MCP pretakanjem in razširitev vašega znanja ta razdelek ponuja dodatne vire in predlagane naslednje korake za gradnjo naprednejših aplikacij.

### Nadaljnje branje

- [Microsoft: Uvod v HTTP pretakanje](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS v ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Pretakanje zahtev](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Kaj sledi?

- Poskusite zgraditi naprednejša MCP orodja, ki uporabljajo pretakanje za analitiko v realnem času, klepet ali sodelovalno urejanje.
- Raziščite integracijo MCP pretakanja s frontend ogrodji (React, Vue itd.) za sprotne posodobitve uporabniškega vmesnika.
- Naslednje: [Uporaba AI orodij za VSCode](../07-aitk/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.