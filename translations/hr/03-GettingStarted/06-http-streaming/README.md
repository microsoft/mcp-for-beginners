# HTTPS Streaming s Model Context Protocolom (MCP)

Ovaj je poglavlje sveobuhvatan vodič za implementaciju sigurnog, skalabilnog i prijenosa u stvarnom vremenu pomoću Model Context Protokola (MCP) korištenjem HTTPS-a. Obuhvaća motivaciju za streaming, dostupne transportne mehanizme, kako implementirati streamabilni HTTP u MCP-u, najbolje sigurnosne prakse, migraciju sa SSE-a i praktične smjernice za izgradnju vlastitih streaming MCP aplikacija.

> **Pogled unaprijed:** ova lekcija opisuje Streamable HTTP pod **MCP specifikacijom 2025-11-25**, gdje se sesija uspostavlja tijekom `initialize` i fiksira s `Mcp-Session-Id` zaglavljem. Kandidat za izdanje `2026-07-28` potpuno uklanja rukovanje i ID sesije, čineći svaki zahtjev samostalnim i usmjerenim na bilo koju instancu poslužitelja bez "sticky" sesija. Za detalje pogledajte [Što se mijenja u MCP-u: Kandidat za izdanje 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Transportni mehanizmi i streaming u MCP-u

Ovaj odjeljak istražuje različite dostupne transportne mehanizme u MCP-u i njihovu ulogu u omogućavanju streaming mogućnosti za komunikaciju u stvarnom vremenu između klijenata i poslužitelja.

### Što je transportni mehanizam?

Transportni mehanizam definira kako se podaci razmjenjuju između klijenta i poslužitelja. MCP podržava više vrsta transporta prilagođenih različitim okruženjima i zahtjevima:

- **stdio**: Standardni ulaz/izlaz, prikladan za lokalne i CLI alate. Jednostavan, ali nije prikladan za web ili oblak.
- **SSE (Server-Sent Events)**: Omogućuje poslužiteljima da šalju ažuriranja u stvarnom vremenu klijentima preko HTTP-a. Dobro za web korisnička sučelja, ali ograničeno u skalabilnosti i fleksibilnosti. Od MCP specifikacije 2025-06-18, samostalni SSE transport je zastario i zamijenjen "Streamable HTTP" transportom.
- **Streamable HTTP**: Moderni HTTP-based streaming transport, podržava obavijesti i bolju skalabilnost. Preporuča se za većinu proizvodnih i cloud scenarija.

### Usporedna tablica

Pogledajte usporednu tablicu ispod da biste razumjeli razlike između ovih transportnih mehanizama:

| Transport         | Ažuriranja u stvarnom vremenu | Streaming | Skalabilnost | Primjena                |
|-------------------|------------------------------|-----------|-------------|-------------------------|
| stdio             | Ne                           | Ne        | Niska       | Lokalni CLI alati        |
| SSE               | Da                           | Da        | Srednja     | Web, ažuriranja u stvarnom vremenu  |
| Streamable HTTP   | Da                           | Da        | Visoka      | Oblak, višekorisnički    |

> **Savjet:** Odabir pravog transporta utječe na performanse, skalabilnost i korisničko iskustvo. **Streamable HTTP** se preporučuje za moderne, skalabilne i cloud-pripremljene aplikacije.

Primijetite transporte stdio i SSE koje smo pokazali u prethodnim poglavljima i kako je streamabilni HTTP transport obrađen u ovom poglavlju.

## Streaming: Koncepti i motivacija

Razumijevanje osnovnih koncepata i motivacije iza streaminga ključno je za implementaciju učinkovitih sustava komunikacije u stvarnom vremenu.

**Streaming** je tehnika u mrežnom programiranju koja omogućuje slanje i primanje podataka u malim, upravljivim dijelovima ili kao niz događaja, umjesto čekanja da cijeli odgovor bude spreman. To je posebno korisno za:

- Velike datoteke ili skupove podataka.
- Ažuriranja u stvarnom vremenu (npr., chat, trake napretka).
- Dugotrajne izračune gdje želite informirati korisnika.

Evo što trebate znati o streaming-u na visokoj razini:

- Podaci se dostavljaju postupno, ne odjednom.
- Klijent može obrađivati podatke čim stignu.
- Smanjuje percipiranu latenciju i poboljšava korisničko iskustvo.

### Zašto koristiti streaming?

Razlozi za korištenje streaminga su sljedeći:

- Korisnici odmah dobivaju povratnu informaciju, ne samo na kraju
- Omogućuje aplikacijama u stvarnom vremenu i responzivna korisnička sučelja
- Učinkovitije korištenje mrežnih i računalnih resursa

### Jednostavan primjer: HTTP streaming poslužitelj i klijent

Evo jednostavnog primjera kako se streaming može implementirati:

#### Python

**Poslužitelj (Python, koristeći FastAPI i StreamingResponse):**

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

**Klijent (Python, koristeći requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Ovaj primjer demonstrira poslužitelj koji šalje niz poruka klijentu čim postanu dostupne, umjesto da čeka da sve poruke budu spremne.

**Kako to radi:**

- Poslužitelj isporučuje svaku poruku čim je spremna.
- Klijent prima i ispisuje svaki dio čim stigne.

**Zahtjevi:**

- Poslužitelj mora koristiti streaming odgovor (npr., `StreamingResponse` u FastAPI).
- Klijent mora obrađivati odgovor kao stream (`stream=True` u requests).
- Content-Type je obično `text/event-stream` ili `application/octet-stream`.

#### Java

**Poslužitelj (Java, koristeći Spring Boot i Server-Sent Events):**

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

**Klijent (Java, koristeći Spring WebFlux WebClient):**

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

**Napomene o Java implementaciji:**

- Koristi Spring Boot reaktivni sloj s `Flux` za streaming
- `ServerSentEvent` omogućuje strukturirani streaming događaja s tipovima događaja
- `WebClient` s `bodyToFlux()` omogućuje reaktivnu konzumaciju streama
- `delayElements()` simulira vrijeme obrade između događaja
- Događaji mogu imati tipove (`info`, `result`) za bolju obradu na klijentu

### Usporedba: Klasični streaming vs MCP streaming

Razlike između klasičnog streaminga i MCP streaminga mogu se prikazati ovako:

| Značajka             | Klasični HTTP streaming         | MCP streaming (obavijesti)    |
|----------------------|--------------------------------|------------------------------|
| Glavni odgovor       | Izrezan                       | Jedan, na kraju              |
| Ažuriranja napretka  | Poslano kao dijelovi podataka | Poslano kao obavijesti       |
| Zahtjevi klijenta    | Mora obraditi stream          | Mora implementirati rukovatelja poruka |
| Primjena             | Velike datoteke, AI token streami | Napredak, zapisi, povratne informacije u stvarnom vremenu |

### Ključne uočene razlike

Nadalje, evo nekih ključnih razlika:

- **Obrazac komunikacije:**
  - Klasični HTTP streaming: koristi jednostavan chunked prijenos za slanje podataka u dijelovima
  - MCP streaming: koristi strukturirani sustav obavijesti s JSON-RPC protokolom

- **Format poruke:**
  - Klasični HTTP: Čisti tekstualni dijelovi s novim redovima
  - MCP: Strukturirani LoggingMessageNotification objekti s metapodacima

- **Implementacija klijenta:**
  - Klasični HTTP: Jednostavan klijent koji obrađuje streaming odgovore
  - MCP: Složeniji klijent s rukovateljem poruka za obradu različitih tipova poruka

- **Ažuriranja napretka:**
  - Klasični HTTP: Napredak je dio glavnog streama odgovora
  - MCP: Napredak se šalje putem zasebnih obavijesti, dok glavni odgovor dolazi na kraju

### Preporuke

Postoje neke preporuke pri odabiru između implementacije klasičnog streaminga (kao što smo prikazali gore korištenjem `/stream`) i streaminga putem MCP-a.

- **Za jednostavne potrebe streaminga:** Klasični HTTP streaming je jednostavniji za implementaciju i dovoljan za osnovne zahtjeve.

- **Za složene, interaktivne aplikacije:** MCP streaming pruža strukturirani pristup s bogatijim metapodacima i razdvajanjem između obavijesti i konačnih rezultata.

- **Za AI aplikacije:** MCP-ov sustav obavijesti posebno je koristan za dugotrajne AI zadatke kada želite korisnike držati informiranima o napretku.

## Streaming u MCP-u

Dakle, vidjeli ste neke preporuke i usporedbe do sada o razlici između klasičnog streaminga i streaminga u MCP-u. Detaljno ćemo objasniti kako točno možete iskoristiti streaming u MCP-u.

Razumijevanje kako streaming funkcionira unutar MCP okvira ključno je za izgradnju responzivnih aplikacija koje pružaju povratne informacije u stvarnom vremenu korisnicima tijekom dugotrajnih operacija.

U MCP-u, streaming nije o slanju glavnog odgovora u dijelovima, već o slanju **obavijesti** klijentu dok alat obrađuje zahtjev. Te obavijesti mogu uključivati ažuriranja napretka, zapise ili druge događaje.

### Kako to radi

Glavni rezultat se i dalje šalje kao jedan odgovor. Međutim, obavijesti se mogu slati kao zasebne poruke tijekom obrade i time ažurirati klijenta u stvarnom vremenu. Klijent mora moći primati i prikazivati te obavijesti.

## Što je obavijest?

Rekli smo "Obavijest", što to znači u kontekstu MCP-a?

Obavijest je poruka poslana s poslužitelja klijentu da informira o napretku, statusu ili drugim događajima tijekom dugotrajne operacije. Obavijesti poboljšavaju transparentnost i korisničko iskustvo.

Na primjer, klijent se očekuje poslati obavijest nakon početnog handshakea s poslužiteljem.

Obavijest izgleda ovako kao JSON poruka:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Obavijesti pripadaju temi u MCP-u nazvanoj ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Obavijest o zastarijevanju:** kandidat za izdanje specifikacije MCP `2026-07-28` označava Logging primitiv kao zastario u korist `stderr` za stdio transporte i OpenTelemetry za strukturiranu opažljivost. Logging i dalje radi u `2025-11-25` i najmanje godinu dana nakon bilo kakvog formalnog zastarijevanja. Pogledajte [Što se mijenja u MCP-u: Kandidat za izdanje 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Da biste omogućili logging, poslužitelj treba omogućiti tu funkcionalnost značajkom/kapacitetom ovako:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Ovisno o korištenom SDK-u, logging može biti omogućen prema zadanim postavkama ili ga morate eksplicitno omogućiti u konfiguraciji poslužitelja.

Postoje različite vrste obavijesti:

| Razina     | Opis                          | Primjer primjene              |
|-----------|-------------------------------|-----------------------------|
| debug     | Detaljne informacije za otklanjanje grešaka | Ulaz/izlaz funkcija        |
| info      | Opće informacijske poruke      | Ažuriranja napretka operacije|
| notice    | Normalni, ali značajni događaji | Promjene konfiguracije      |
| warning   | Upozoravajuće uvjete           | Korištenje zastarjele značajke|
| error     | Uvjeti pogreške                | Neuspjesi u radu operacije  |
| critical  | Kritični uvjeti                | Otkaži sustava komponente    |
| alert     | Potrebna je hitna akcija       | Otkrivena korupcija podataka|
| emergency | Sustav neupotrebljiv           | Potpuni kvar sustava        |

## Implementacija obavijesti u MCP-u

Za implementaciju obavijesti u MCP-u, morate postaviti i poslužiteljsku i klijentsku stranu da podrže ažuriranja u stvarnom vremenu. To omogućuje vašoj aplikaciji pružanje trenutnih povratnih informacija korisnicima tijekom dugotrajnih operacija.

### Poslužiteljska strana: slanje obavijesti

Počnimo s poslužiteljskom stranom. U MCP-u definirate alate koji mogu slati obavijesti dok obrađuju zahtjeve. Poslužitelj koristi kontekstni objekt (obično `ctx`) za slanje poruka klijentu.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

U prethodnom primjeru, alat `process_files` šalje tri obavijesti klijentu dok obrađuje svaku datoteku. Metoda `ctx.info()` se koristi za slanje informativnih poruka.

Dodatno, za omogućavanje obavijesti, osigurajte da vaš poslužitelj koristi streaming transport (kao što je `streamable-http`) i da vaš klijent implementira rukovatelja poruka za obradu obavijesti. Evo kako postaviti poslužitelj za korištenje `streamable-http` transporta:

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

U ovom .NET primjeru, alat `ProcessFiles` je označen atributom `Tool` i šalje tri obavijesti klijentu dok obrađuje svaku datoteku. Metoda `ctx.Info()` se koristi za slanje informativnih poruka.

Za omogućavanje obavijesti u vašem .NET MCP poslužitelju, osigurajte da koristite streaming transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Klijentska strana: primanje obavijesti

Klijent mora implementirati rukovatelja poruka za obradu i prikaz obavijesti čim stignu.

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

U prethodnom kodu, funkcija `message_handler` provjerava je li primljena poruka obavijest. Ako jest, ispisuje obavijest; inače je obrađuje kao redovitu poruku poslužitelja. Također primijetite kako je `ClientSession` inicijaliziran s `message_handler` za rukovanje dolaznim obavijestima.

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

U ovom .NET primjeru, funkcija `MessageHandler` provjerava je li primljena poruka obavijest. Ako jest, ispisuje obavijest; inače ju obrađuje kao redovitu poruku poslužitelja. `ClientSession` je inicijaliziran s rukovateljem poruka putem `ClientSessionOptions`.

Za omogućavanje obavijesti, osigurajte da vaš poslužitelj koristi streaming transport (kao što je `streamable-http`) i da vaš klijent implementira rukovatelja poruka za obradu obavijesti.

## Obavijesti o napretku i scenariji

Ovaj odjeljak objašnjava koncept obavijesti o napretku u MCP-u, zašto su važni i kako ih implementirati koristeći Streamable HTTP. Također ćete naći praktični zadatak za učvršćivanje razumijevanja.

Obavijesti o napretku su poruke u stvarnom vremenu koje poslužitelj šalje klijentu tijekom dugotrajnih operacija. Umjesto čekanja završetka procesa, poslužitelj stalno obavještava klijenta o trenutnom statusu. To poboljšava transparentnost, korisničko iskustvo i olakšava otklanjanje pogrešaka.

**Primjer:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Zašto koristiti obavijesti o napretku?

Obavijesti o napretku su bitne iz više razloga:

- **Bolje korisničko iskustvo:** Korisnici vide ažuriranja dok rad traje, ne samo na kraju.
- **Povratne informacije u stvarnom vremenu:** Klijenti mogu prikazivati trake napretka ili zapise, čineći aplikaciju responzivnom.
- **Lakše otklanjanje pogrešaka i praćenje:** Programeri i korisnici mogu vidjeti gdje je proces usporen ili zapetljan.

### Kako implementirati obavijesti o napretku

Evo kako implementirati obavijesti o napretku u MCP-u:

- **Na poslužitelju:** Koristite `ctx.info()` ili `ctx.log()` za slanje obavijesti čim se svaki element obradi. Ovo šalje poruku klijentu prije nego što glavni rezultat postane spreman.
- **Na klijentu:** Implementirajte rukovatelja poruka koji sluša i prikazuje obavijesti čim stignu. Taj rukovatelj razlikuje obavijesti i konačni rezultat.

**Primjer poslužitelja:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Primjer klijenta:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Sigurnosne napomene

Sigurnost bi trebala biti glavni prioritet pri implementaciji svakog poslužitelja, posebno pri korištenju HTTP transporta poput Streamable HTTP u MCP-u.

Kod implementacije MCP poslužitelja s HTTP transportom, sigurnost postaje ključni faktor koji zahtijeva pažnju na više napadačkih vektora i zaštitnih mehanizama.

### Pregled

Sigurnost je kritična prilikom izlaganja MCP poslužitelja preko HTTP-a. Streamable HTTP uvodi nove površine za napade i zahtijeva pažljivu konfiguraciju.

Evo nekoliko ključnih sigurnosnih razmatranja:

- **Validacija zaglavlja Origin**: Uvijek validirajte `Origin` zaglavlje kako biste spriječili DNS rebinding napade.
- **Povezivanje na localhost**: Za lokalni razvoj, vežite poslužitelje na `localhost` kako biste spriječili njihovo izlaganje javnom internetu.
- **Autentikacija**: Implementirajte autentikaciju (npr. API ključeve, OAuth) za produkcijska okruženja.
- **CORS**: Konfigurirajte politike Cross-Origin Resource Sharing (CORS) za ograničavanje pristupa.
- **HTTPS**: Koristite HTTPS u produkciji za enkripciju prometa.

### Najbolje prakse

Također, evo nekoliko najboljih praksi koje treba slijediti prilikom implementacije sigurnosti u vašem MCP streaming poslužitelju:

- Nikada ne vjerujte dolaznim zahtjevima bez provjere.
- Zapisujte i pratite sav pristup i pogreške.
- Redovito ažurirajte ovisnosti radi zakrpa sigurnosnih propusta.

### Izazovi

Susrest ćete se s nekim izazovima prilikom implementacije sigurnosti u MCP streaming poslužiteljima:

- Uravnoteženje sigurnosti i jednostavnosti razvoja
- Osiguravanje kompatibilnosti s različitim okruženjima klijenata


## Nadogradnja s SSE na Streamable HTTP

Za aplikacije koje trenutno koriste Server-Sent Events (SSE), migracija na Streamable HTTP pruža poboljšane mogućnosti i bolju dugoročnu održivost za vaše MCP implementacije.

### Zašto nadograditi?

Postoje dva uvjerljiva razloga za nadogradnju sa SSE na Streamable HTTP:

- Streamable HTTP nudi bolju skalabilnost, kompatibilnost i bogatiju podršku za obavijesti nego SSE.
- To je preporučeni transport za nove MCP aplikacije.

### Koraci migracije

Evo kako možete migrirati sa SSE na Streamable HTTP u vašim MCP aplikacijama:

- **Ažurirajte kod poslužitelja** da koristi `transport="streamable-http"` u `mcp.run()`.
- **Ažurirajte kod klijenta** da koristi `streamablehttp_client` umjesto SSE klijenta.
- **Implementirajte handler poruka** u klijentu za obradu obavijesti.
- **Testirajte kompatibilnost** s postojećim alatima i radnim tokovima.

### Održavanje kompatibilnosti

Preporučuje se održavanje kompatibilnosti s postojećim SSE klijentima tijekom procesa migracije. Evo nekih strategija:

- Možete podržavati i SSE i Streamable HTTP istovremeno pokretanjem oba transporta na različitim krajnjim točkama.
- Postupno migrirajte klijente na novi transport.

### Izazovi

Pazite na sljedeće izazove tijekom migracije:

- Osiguravanje da su svi klijenti ažurirani
- Rukovanje razlikama u isporuci obavijesti

### Zadatak: Izgradite vlastitu Streaming MCP aplikaciju

**Scenarij:**
Izgradite MCP poslužitelj i klijent gdje poslužitelj obrađuje popis stavki (npr. datoteke ili dokumente) i šalje obavijest za svaku obrađenu stavku. Klijent bi trebao prikazivati svaku obavijest čim stigne.

**Koraci:**

1. Implementirajte poslužiteljski alat koji obrađuje popis i šalje obavijesti za svaku stavku.
2. Implementirajte klijenta s handlerom poruka koji prikazuje obavijesti u stvarnom vremenu.
3. Testirajte svoju implementaciju pokretanjem poslužitelja i klijenta te promatranjem obavijesti.

[Rješenje](./solution/README.md)

## Daljnje čitanje i što dalje?

Da nastavite svoje putovanje s MCP streamingom i proširite svoje znanje, ovaj odjeljak pruža dodatne resurse i prijedloge sljedećih koraka za izgradnju naprednijih aplikacija.

### Daljnje čitanje

- [Microsoft: Uvod u HTTP streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS u ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Što dalje?

- Pokušajte izgraditi naprednije MCP alate koji koriste streaming za analitiku u stvarnom vremenu, chat ili kolaborativno uređivanje.
- Istražite integraciju MCP streaminga s frontend frameworkima (React, Vue i sl.) za živo ažuriranje korisničkog sučelja.
- Sljedeće: [Korištenje AI Toolkit za VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->