# HTTPS pretakanje s protokolom konteksta modela (MCP)

To poglavje ponuja celovit vodnik za implementacijo varnega, razširljivega in pretočnega pretakanja v realnem času s protokolom konteksta modela (MCP) s pomočjo HTTPS. Obravnava motivacijo za pretakanje, razpoložljive transportne mehanizme, kako implementirati pretočni HTTP v MCP, varnostne najboljše prakse, migracijo iz SSE in praktična navodila za izdelavo lastnih aplikacij za pretakanje MCP. 

> **Poglejmo naprej:** ta lekcija opisuje pretočni HTTP pod **MCP specifikacijo 2025-11-25**, kjer se seja vzpostavi med `initialize` in je pritrjena z glavo `Mcp-Session-Id`. Kandidat za izdajo `2026-07-28` popolnoma odstrani rokovanje in ID seje, zaradi česar je vsak zahtevek samostojen in usmerljiv na katerikoli primer strežnika brez lepljivih sej. Za podrobnosti glejte [Kaj se spreminja v MCP: Kandidat za izdajo 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Transportni mehanizmi in pretakanje v MCP

Ta razdelek raziskuje različne transportne mehanizme, ki so na voljo v MCP, in njihovo vlogo pri omogočanju pretočnih zmogljivosti za komunikacijo v realnem času med odjemalci in strežniki.

### Kaj je transportni mehanizem?

Transportni mehanizem določa, kako se podatki izmenjujejo med odjemalcem in strežnikom. MCP podpira več vrst transporta, da ustreza različnim okoljem in zahtevam:

- **stdio**: Standardni vhod/izhod, primeren za lokalna orodja in orodja na ukazni vrstici. Preprosto, vendar ni primerno za splet ali oblak.
- **SSE (Server-Sent Events)**: Omogoča strežnikom, da potisnejo posodobitve v realnem času do odjemalcev prek HTTP. Dobro za spletne uporabniške vmesnike, vendar omejeno v razširljivosti in prilagodljivosti. Od MCP specifikacije 2025-06-18 je samostojen SSE transport zastarel in ga je nadomestil "Streamable HTTP" transport.
- **Streamable HTTP**: Sodobni pretočni transport na osnovi HTTP, ki podpira obvestila in boljšo razširljivost. Priporočljiv za večino proizvodnih in oblačnih scenarijev.

### Primerjalna tabela

Oglejte si spodnjo primerjalno tabelo, da razumete razlike med temi transportnimi mehanizmi:

| Transport         | Posodobitve v realnem času | Pretakanje | Razširljivost | Primer uporabe          |
|-------------------|----------------------------|------------|---------------|-------------------------|
| stdio             | Ne                         | Ne         | Nizka         | Lokalna orodja CLI      |
| SSE               | Da                         | Da         | Srednja       | Splet, posodobitve v realnem času  |
| Streamable HTTP   | Da                         | Da         | Visoka        | Oblačno, več odjemalcev |

> **Namig:** Izbira pravega transporta vpliva na zmogljivost, razširljivost in uporabniško izkušnjo. **Streamable HTTP** je priporočljiv za sodobne, razširljive in oblačne aplikacije.

Upoštevajte transporte stdio in SSE, ki so vam bili prikazani v prejšnjih poglavjih, ter kako je pretočni HTTP transport, ki ga obravnavamo v tem poglavju.

## Pretakanje: koncepti in motivacija

Razumevanje osnovnih konceptov in motivacij za pretakanje je ključnega pomena za implementacijo učinkovitih sistemov za komunikacijo v realnem času.

**Pretakanje** je tehnika v mrežnem programiranju, ki omogoča pošiljanje in prejemanje podatkov v majhnih, obvladljivih odsekih ali kot zaporedje dogodkov, namesto da bi čakali, da je celoten odgovor pripravljen. To je še posebej uporabno za:

- Velike datoteke ali podatkovne sklope.
- Posodobitve v realnem času (npr. klepet, vrstica napredka).
- Dolgotrajne izračune, kjer želite uporabnika obveščati o poteku.

Tukaj je, kar morate vedeti o pretakanju na visoki ravni:

- Podatki se dostavljajo postopoma, ne vsi naenkrat.
- Odjemalec lahko obdela podatke sproti, ko prispejo.
- Zmanjšuje zaznano zakasnitev in izboljšuje uporabniško izkušnjo.

### Zakaj uporabljati pretakanje?

Razlogi za uporabo pretakanja so naslednji:

- Uporabniki dobijo povratne informacije takoj, ne samo na koncu
- Omogoča aplikacije v realnem času in odzivne uporabniške vmesnike
- Učinkovitejša raba omrežnih in računalniških virov

### Preprost primer: strežnik in odjemalec za HTTP pretakanje

Tukaj je enostaven primer, kako lahko implementirate pretakanje:

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

Ta primer prikazuje strežnik, ki pošilja serijo sporočil odjemalcu, ko so na voljo, namesto da bi čakal, da so vsa sporočila pripravljena.

**Kako deluje:**

- Strežnik po vrsti pošilja vsako sporočilo, ko je pripravljeno.
- Odjemalec prejme in izpiše vsak delček sproti, ko prispe.

**Pogoji:**

- Strežnik mora uporabiti pretočni odgovor (npr. `StreamingResponse` v FastAPI).
- Odjemalec mora obdelovati odgovor kot tok (`stream=True` v requests).
- Vsebinski tip je običajno `text/event-stream` ali `application/octet-stream`.

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

- Uporablja reaktivni sklad Spring Boota s `Flux` za pretakanje
- `ServerSentEvent` omogoča strukturirano pretakanje dogodkov s tipi dogodkov
- `WebClient` z `bodyToFlux()` omogoča reaktivno porabo pretoka
- `delayElements()` simulira čas obdelave med dogodki
- Dogodki lahko imajo tipe (`info`, `result`) za boljšo obdelavo na odjemalcu

### Primerjava: klasično pretakanje proti MCP pretakanju

Razlike med klasičnim načinom pretakanja in MCP pretakanjem so prikazane takole:

| Lastnost               | Klasično HTTP pretakanje       | MCP pretakanje (obvestila)          |
|------------------------|-------------------------------|-------------------------------------|
| Glavni odgovor         | V delčkih                    | En sam, na koncu                    |
| Posodobitve poteka     | Poslane kot podatkovni delčki  | Poslane kot obvestila               |
| Zahteve odjemalca      | Mora obdelati tok             | Mora implementirati upravljalnik sporočil |
| Primer uporabe         | Velike datoteke, AI tokovi    | Napredek, dnevniki, povratne informacije v realnem času |

### Opazne ključne razlike

Poleg tega so tukaj nekatere ključne razlike:

- **Vzorec komunikacije:**
  - Klasično HTTP pretakanje: Uporablja preprosto kodiranje prenosa v delčkih za pošiljanje podatkov v delčkih
  - MCP pretakanje: Uporablja strukturiran sistem obvestil s protokolom JSON-RPC

- **Format sporočila:**
  - Klasično HTTP: Navadni tekstovni delčki z novimi vrsticami
  - MCP: Strukturirani objekti LoggingMessageNotification z metapodatki

- **Implementacija odjemalca:**
  - Klasično HTTP: Preprost odjemalec, ki obdeluje pretočne odgovore
  - MCP: Bolj sofisticiran odjemalec z upravljalnikom sporočil za obdelavo različnih vrst sporočil

- **Posodobitve poteka:**
  - Klasično HTTP: Napredek je del glavnega toka odgovora
  - MCP: Napredek se pošilja prek ločenih obvestil, medtem ko glavni odgovor pride na koncu

### Priporočila

Obstajajo določene stvari, ki jih priporočamo pri izbiri med klasično implementacijo pretakanja (kot je endpoint, ki smo ga prikazali zgoraj z `/stream`) in pretakanjem preko MCP.

- **Za preproste potrebe pretakanja:** Klasično HTTP pretakanje je lažje za implementacijo in zadostuje za osnovne potrebe.

- **Za zapletene, interaktivne aplikacije:** MCP pretakanje nudi bolj strukturiran pristop z bogatejšimi metapodatki in ločitvijo med obvestili in končnimi rezultati.

- **Za AI aplikacije:** MCP sistem obvestil je posebej uporaben za dolgotrajne AI naloge, kjer želite uporabnike obveščati o napredku.

## Pretakanje v MCP

Okej, do sedaj ste videli nekaj priporočil in primerjav glede razlik med klasičnim pretakanjem in pretakanjem v MCP. Poglejmo podrobno, kako lahko natančno izkoristite pretakanje v MCP.

Razumevanje, kako pretakanje deluje znotraj okvira MCP, je ključno za gradnjo odzivnih aplikacij, ki uporabnikom zagotavljajo povratne informacije v realnem času med dolgotrajnimi opravili.

V MCP pretakanje ni pošiljanje glavnega odgovora v delčkih, ampak pošiljanje **obvestil** odjemalcu med procesiranjem zahteve. Ta obvestila lahko vključujejo posodobitve o napredku, dnevnike ali druge dogodke.

### Kako deluje

Glavni rezultat je še vedno poslan kot en odgovor. Kljub temu pa se obvestila lahko pošiljajo kot ločena sporočila med procesiranjem in tako posodabljajo odjemalca v realnem času. Odjemalec mora biti sposoben upravljati in prikazati ta obvestila.

## Kaj je obvestilo?

Rekli smo "obvestilo", kaj to pomeni v kontekstu MCP?

Obvestilo je sporočilo, poslano od strežnika do odjemalca, da ga obvesti o napredku, statusu ali drugih dogodkih med dolgotrajnim opravilom. Obvestila izboljšujejo preglednost in uporabniško izkušnjo.

Na primer, odjemalec bi moral poslati obvestilo, ko je začetno rokovanje s strežnikom opravljeno.

Obvestilo izgleda takole kot JSON sporočilo:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Obvestila spadajo pod temo v MCP, imenovano ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Obvestilo o zastarelosti:** kandidat za izdajo MCP specifikacije `2026-07-28` označuje primitivno Logging kot zastarelo v prid `stderr` za stdio transporte in OpenTelemetry za strukturirano opazovanje. Beleženje ostaja funkcionalno v `2025-11-25` in še vsaj eno leto po formalni zastarelosti. Za podrobnosti glejte [Kaj se spreminja v MCP: Kandidat za izdajo 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Da bi logging deloval, mora strežnik omogočiti to funkcijo/zmožnost takole:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Glede na uporabljeni SDK je logging lahko privzeto omogočen, ali pa ga boste morali eksplicitno omogočiti v konfiguraciji strežnika.

Obstajajo različne vrste obvestil:

| Stopnja    | Opis                         | Primer uporabe                  |
|-----------|------------------------------|--------------------------------|
| debug     | Podrobne informacije za odpravljanje napak | Točke vhoda/izhoda funkcij    |
| info      | Splošna informativna sporočila | Posodobitve napredka          |
| notice    | Normalni, a pomembni dogodki  | Spremembe konfiguracije        |
| warning   | Opozorilna stanja            | Uporaba zastarelih funkcij     |
| error     | Napake                      | Napake pri izvajanju           |
| critical  | Kritična stanja             | Okvare sistemskih komponent    |
| alert     | Takojšnja ukrepanja          | Zaznana poškodba podatkov      |
| emergency | Sistem neuporaben            | Popolna okvara sistema         |

## Implementacija obvestil v MCP

Za implementacijo obvestil v MCP morate nastaviti tako strežniški kot odjemalski del za obdelavo posodobitev v realnem času. To omogoča vaši aplikaciji, da uporabnikom zagotovi takojšnje povratne informacije med dolgotrajnimi operacijami.

### Na strani strežnika: pošiljanje obvestil

Začnimo s strežniško stranjo. V MCP definirate orodja, ki lahko pošiljajo obvestila med procesiranjem zahtev. Strežnik uporablja objekt konteksta (običajno `ctx`) za pošiljanje sporočil odjemalcu.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

V prejšnjem primeru orodje `process_files` pošlje tri obvestila odjemalcu med obdelavo vsake datoteke. Metoda `ctx.info()` se uporablja za pošiljanje informativnih sporočil.

Poleg tega, da omogočite obvestila, zagotovite, da strežnik uporablja pretočni transport (kot je `streamable-http`) in da je na odjemalcu implementiran upravljalnik sporočil za obdelavo obvestil. Tako lahko nastavite strežnik za uporabo `streamable-http` transporta:

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

V tem .NET primeru je orodje `ProcessFiles` označeno z atributom `Tool` in pošilja tri obvestila odjemalcu med obdelavo vsake datoteke. Metoda `ctx.Info()` se uporablja za pošiljanje informativnih sporočil.

Za omogočanje obvestil na vašem .NET MCP strežniku poskrbite, da uporabljate pretočni transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Na strani odjemalca: prejemanje obvestil

Odjemalec mora implementirati upravljalnika sporočil za obdelavo in prikazovanje obvestil ob njihovem prihodu.

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

V zgornji kodi funkcija `message_handler` preveri, ali je prihajajoče sporočilo obvestilo. Če je, ga izpiše; sicer ga obdela kot običajno sporočilo strežnika. Prav tako opazite, kako se `ClientSession` inicializira z `message_handler` za upravljanje prihajajočih obvestil.

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

V tem .NET primeru funkcija `MessageHandler` preveri, ali je prihajajoče sporočilo obvestilo. Če je, ga izpiše; sicer ga obdela kot običajno sporočilo strežnika. `ClientSession` se inicializira z upravljalnikom sporočil preko `ClientSessionOptions`.

Za omogočanje obvestil zagotovite, da vaš strežnik uporablja pretočni transport (kot je `streamable-http`) in da odjemalec implementira upravljalnika sporočil za obdelavo obvestil.

## Obvestila o napredku in scenariji

Ta razdelek pojasnjuje koncept obvestil o napredku v MCP, zakaj so pomembna in kako jih implementirati z uporabo Streamable HTTP. Prav tako boste našli praktično nalogo za utrditev razumevanja.

Obvestila o napredku so sporočila v realnem času, poslana s strežnika do odjemalca med dolgotrajnimi operacijami. Namesto da bi čakali, da se celoten proces konča, strežnik uporabniku posreduje trenutno stanje. To izboljšuje preglednost, uporabniško izkušnjo in olajša odpravljanje napak.

**Primer:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Zakaj uporabljati obvestila o napredku?

Obvestila o napredku so pomembna zaradi več razlogov:

- **Boljša uporabniška izkušnja:** uporabniki vidijo posodobitve med potekom dela, ne samo na koncu.
- **Povratne informacije v realnem času:** odjemalci lahko prikazujejo napredne vrstice ali dnevnike, kar aplikaciji daje občutek odzivnosti.
- **Lažje odpravljanje in spremljanje:** razvijalci in uporabniki lahko vidijo, kje je postopek morda počasen ali zataknjen.

### Kako implementirati obvestila o napredku

Tako lahko implementirate obvestila o napredku v MCP:

- **Na strežniku:** Uporabite `ctx.info()` ali `ctx.log()` za pošiljanje obvestil vsakič, ko je element obdelan. To pošlje sporočilo odjemalcu pred glavnim rezultatom.
- **Na odjemalcu:** Implementirajte upravljalnika sporočil, ki posluša in prikazuje obvestila sproti. Ta upravljalnik loči med obvestili in končnim rezultatom.

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

Varnost bi morala biti največja prioriteta pri implementaciji katerega koli strežnika, posebej pri uporabi prenosov na osnovi HTTP, kot je Streamable HTTP v MCP.

Pri implementaciji MCP strežnikov s prenosom na osnovi HTTP varnost postane ključna skrb, ki zahteva previdno obravnavo različnih napadalnih vektorjev in zaščitnih mehanizmov.

### Pregled

Varnost je ključnega pomena pri izpostavljanju MCP strežnikov prek HTTP. Streamable HTTP prinaša nove možnosti za napade in zahteva skrbno konfiguracijo.

Tu je nekaj ključnih varnostnih vidikov:

- **Preverjanje glave Origin**: Vedno preverite glavo `Origin`, da preprečite DNS ponovni vezavi.
- **Povezava na localhost**: Za lokalni razvoj povežite strežnike na `localhost`, da jih ne izpostavite javnemu internetu.
- **Avtentikacija**: Implementirajte avtentikacijo (npr. API ključi, OAuth) za produkcijska okolja.
- **CORS**: Konfigurirajte politike za Cross-Origin Resource Sharing (CORS), da omejite dostop.
- **HTTPS**: V produkciji uporabljajte HTTPS za šifriranje prometa.

### Najboljše prakse

Prav tako tukaj sledi nekaj najboljših praks za varnost pri implementaciji MCP strežniškega prenosa:

- Nikoli ne zaupajte dohodnim zahtevam brez preverjanja.
- Beležite in spremljajte vse dostope in napake.
- Redno posodabljajte odvisnosti, da zaprete varnostne ranljivosti.

### Izzivi

Pri implementaciji varnosti v streaming strežnikih MCP se boste srečali z nekaterimi izzivi:

- Uravnoteženje med varnostjo in enostavnostjo razvoja
- Zagotavljanje združljivosti z različnimi odjemalskimi okolji


## Nadgradnja s SSE na Streamable HTTP

Za aplikacije, ki trenutno uporabljajo Server-Sent Events (SSE), migracija na Streamable HTTP omogoča izboljšane funkcionalnosti in boljšo dolgoročno vzdržnost za vaše MCP implementacije.

### Zakaj nadgradnja?

Obstajata dva pomembna razloga za nadgradnjo s SSE na Streamable HTTP:

- Streamable HTTP ponuja boljšo skalabilnost, združljivost in bogatejšo podporo za obvestila kot SSE.
- To je priporočen prenos za nove MCP aplikacije.

### Koraki migracije

Tako lahko migrirate s SSE na Streamable HTTP v svojih MCP aplikacijah:

- **Posodobite strežniško kodo** tako, da uporabite `transport="streamable-http"` v `mcp.run()`.
- **Posodobite odjemalsko kodo** tako, da uporabite `streamablehttp_client` namesto SSE odjemalca.
- **Implementirajte upravljalec sporočil** v odjemalcu za predelavo obvestil.
- **Preizkusite združljivost** z obstoječimi orodji in delovnimi procesi.

### Ohranjanje združljivosti

Priporočljivo je ohraniti združljivost z obstoječimi SSE odjemalci med postopkom migracije. Tukaj je nekaj strategij:

- Podpirajte tako SSE kot Streamable HTTP z zagonom obeh prenosov na različnih končnih točkah.
- Postopoma migrirajte odjemalce na nov prenos.

### Izzivi

Med migracijo morate rešiti naslednje izzive:

- Zagotavljanje, da so vsi odjemalci posodobljeni
- Obvladovanje razlik v dostavi obvestil

### Naloga: Zgradite svojo streaming MCP aplikacijo

**Scenarij:**
Zgradite MCP strežnik in odjemalca, kjer strežnik predeluje seznam elementov (npr. datotek ali dokumentov) in pošlje obvestilo za vsak predelan element. Odjemalec naj prikazuje vsako obvestilo takoj, ko prispe.

**Koraki:**

1. Implementirajte strežniško orodje, ki obdela seznam in pošlje obvestila za vsak element.
2. Implementirajte odjemalca z upravljalcem sporočil za prikaz obvestil v realnem času.
3. Preizkusite implementacijo z zagonom strežnika in odjemalca ter opazujte obvestila.

[Rešitev](./solution/README.md)

## Nadaljnje branje in kaj sledi?

Za nadaljevanje vaše poti z MCP streamingom in širjenje znanja ta razdelek ponuja dodatne vire in predlagane naslednje korake za gradnjo bolj naprednih aplikacij.

### Nadaljnje branje

- [Microsoft: Uvod v HTTP streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS v ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Kaj sledi?

- Poskusite zgraditi bolj napredna MCP orodja, ki uporabljajo streaming za analitiko v realnem času, klepet ali sodelovalno urejanje.
- Raziskujte integracijo MCP streaminga z ogrodji za frontend (React, Vue itd.) za žive posodobitve vmesnika.
- Naslednje: [Uporaba AI orodij za VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->