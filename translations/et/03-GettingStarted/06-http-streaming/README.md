# HTTPS voogedastus Model Context Protocoliga (MCP)

See peatükk annab põhjaliku juhendi turvalise, skaleeritava ja reaalajas voogedastuse rakendamiseks Model Context Protokolli (MCP) abil HTTPS-i kaudu. See käsitleb voogedastuse motivatsiooni, olemasolevaid transpordimehhanisme, voogedastatava HTTP rakendamist MCP-s, turvalisuse parimaid tavasid, migratsiooni SSE-st ning praktilisi juhiseid oma voogedastavate MCP rakenduste loomiseks.

> **Vaatame ette:** see õppetund kirjeldab voogedastatavat HTTP-d **MCP spetsifikatsiooni 2025-11-25** all, kus sessioon luuakse `initialize` ajal ja kinnitatakse `Mcp-Session-Id` päisega. `2026-07-28` versiooni kandidaadis eemaldatakse käepigistus ja sessiooni ID täielikult, muutes iga päringu iseseisvaks ja suunatavaks mis tahes serveri instantsile ilma püsisessioonideta. Lisateavet leiate failist [Mis muutub MCP-s: 2026-07-28 versiooni kandidaat](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## Transpordimehhanismid ja voogedastus MCP-s

Selles jaotises uuritakse erinevaid MCP-s saadaval olevaid transpordimehhanisme ja nende rolli voogedastuse võimaldamisel reaalajas suhtluses klientide ja serverite vahel.

### Mis on transpordimehhanism?

Transpordimehhanism määrab, kuidas andmeid klientide ja serverite vahel vahetatakse. MCP toetab mitut transpordi tüüpi, et sobituda erinevate keskkondade ja nõuetega:

- **stdio**: Standardne sisend/väljund, sobilik kohalikuks kasutamiseks ja käsureatööriistadele. Lihtne, kuid mitte sobiv veebis või pilves.
- **SSE (Server-Sent Events)**: Võimaldab serveritel saata klientidele reaalajas värskendusi HTTP üle. Sobib hästi veebiliidestele, kuid on piiratud skaleeritavuse ja paindlikkusega. Alates MCP spetsifikatsioonist 2025-06-18 on eraldiseisev SSE transpordimehhanism aegunud ja asendatud "voogedastatava HTTP-ga".
- **Voogedastatav HTTP**: Kaasaegne HTTP-põhine voogedastuse transpordimehhanism, mis toetab teavitusi ja paremat skaleeritavust. Soovitatav enamiku tootmis- ja pilvesituatsioonide jaoks.

### Võrdlustabel

Vaata allolevat võrdlustabelit, et mõista nende transpordimehhanismide erinevusi:

| Transport         | Reaalajas värskendused | Voogedastus | Skaleeritavus | Kasutusjuhtum           |
|-------------------|------------------------|-------------|---------------|-------------------------|
| stdio             | Ei                     | Ei          | Madal         | Kohalikud käsureatööriistad |
| SSE               | Jah                    | Jah         | Keskmine      | Veeb, reaalajas värskendused |
| Voogedastatav HTTP| Jah                    | Jah         | Kõrge         | Pilv, mitme kliendi toetus   |

> **Vihje:** Õige transpordi valik mõjutab jõudlust, skaleeritavust ja kasutajakogemust. **Voogedastatav HTTP** on soovitatav kaasaegsete, skaleeritavate ja pilvevalmis rakenduste jaoks.

Pange tähele transportide stdio ja SSE-st, mida näidati eelmistel peatükkidel, ning seda, kuidas voogedastatav HTTP on selle peatüki käsitletav transpordimehhanism.

## Voogedastus: mõisted ja motivatsioon

Mõistmine voogedastuse põhikontseptsioonidest ja motivatsioonist on oluline tõhusate reaalajas suhtlussüsteemide rakendamiseks.

**Voogedastus** on võrguprogrammeerimise tehnika, mis võimaldab andmeid saata ja vastu võtta väikeste, hallatavate osadena või sündmuste jada kaupa, selle asemel et oodata kogu vastuse valmimist. See on eriti kasulik:

- Suurte failide või andmekogumite puhul.
- Reaalajas värskenduste (nt vestlusrakendused, edenemisriba) korral.
- Pikaajaliste arvutuste puhul, kus soovite hoida kasutajat kursis.

Siin on ülevaatlik teave voogedastuse kohta:

- Andmed edastatakse järk-järgult, mitte korraga.
- Klient saab andmeid töödelda kohe, kui need saabuvad.
- Vähendab tajutavat latentsust ja parandab kasutajakogemust.

### Miks kasutada voogedastust?

Voogedastuse kasutamise põhjused on järgmised:

- Kasutajad saavad kohe tagasisidet, mitte alles lõpus.
- Võimaldab reaalajas rakendusi ja reageerivaid kasutajaliideseid.
- Võrgus ja arvutusressursside tõhusam kasutamine.

### Lihtne näide: HTTP voogedastuse server ja klient

Siin on lihtne näide, kuidas voogedastust saab rakendada:

#### Python

**Server (Python, kasutades FastAPI-d ja StreamingResponse'i):**

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

**Klient (Python, kasutades requests'i):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

See näide demonstreerib serverit, mis saadab klientidele sõnumite jada kohe, kui need on saadaval, selle asemel et oodata kõigi sõnumite valmimist.

**Kuidas see töötab:**

- Server edastab iga sõnumi kohe, kui see on valmis.
- Klient võtab vastu ja prindib iga osa kohe, kui see saabub.

**Nõuded:**

- Server peab kasutama voogedastusvastust (nt `StreamingResponse` FastAPI-s).
- Klient peab töötlema vastust voona (`stream=True` requests'is).
- Sisu tüüp on tavaliselt `text/event-stream` või `application/octet-stream`.

#### Java

**Server (Java, kasutades Spring Booti ja Server-Sent Events):**

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

**Klient (Java, kasutades Spring WebFlux WebClienti):**

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

**Java rakendamise märkused:**

- Kasutab Spring Boot reactive stack'i `Flux`-iga voogedastuseks
- `ServerSentEvent` pakub struktureeritud sündmuste voogedastust sündmuste tüüpidega
- `WebClient` koos `bodyToFlux()` võimaldab reaktiivset voogedastuse tarbimist
- `delayElements()` simuleerib töötlemisaega sündmuste vahel
- Sündmustel võivad olla tüübid (`info`, `result`), mis parandavad kliendi käsitlemist

### Võrdlus: Klasikaline voogedastus vs MCP voogedastus

Voogedastuse erinevusi traditsioonilisel viisil ja MCP-s saab näidata järgmiselt:

| Omadus                | Klasikaline HTTP voogedastus  | MCP voogedastus (teavitused)     |
|------------------------|-----------------------------|---------------------------------|
| Peamine vastus         | Jagatud tükid                | Üksik vastus lõpus              |
| Edenemise värskendused | Saadetakse andmetükkidena    | Saadetakse teavitustena         |
| Kliendi nõuded         | Peaks töötlema voogu          | Peab rakendama sõnumite töötleja |
| Kasutusjuhtum          | Suured failid, AI tokeni vood| Edenemine, logid, reaalajas tagasiside |

### Täheldatud peamised erinevused

Lisaks on mõned peamised erinevused:

- **Kommunikatsioonimuster:**
  - Klasikaline HTTP voogedastus: kasutab lihtsat tükeldatud edastust, et saata andmeid osadena
  - MCP voogedastus: kasutab struktureeritud teavitussüsteemi JSON-RPC protokolliga

- **Sõnumi formaat:**
  - Klassikaline HTTP: lihttekst tükid reavahetustega
  - MCP: struktureeritud LoggingMessageNotification objektid metaga

- **Kliendi rakendamine:**
  - Klasikaline HTTP: lihtne klient, mis töötleb voogedastusvastuseid
  - MCP: keerukam klient sõnumite töötlejaga, mis töötleb erinevaid sõnumitüüpe

- **Edenemise värskendused:**
  - Klasikaline HTTP: edenemine on osa peamisest vastuse voost
  - MCP: edenemine saadetakse eraldiseisvate teavitustena, peamine vastus tuleb lõpus

### Soovitused

Mõned soovitused klassikalise voogedastuse (nagu eespool näidatud lõpp-punkt `/stream`) ja MCP voogedastuse vahel valimisel:

- **Lihtsate voogedastusvajaduste puhul:** Klassikaline HTTP voogedastus on lihtsam rakendada ja piisab põhiliste vajaduste jaoks.

- **Keerukate, interaktiivsete rakenduste puhul:** MCP voogedastus pakub struktureeritumat lähenemist, rikkalikuma metainfoga ja teavituste ning lõplike tulemuste eristamisega.

- **AI rakenduste jaoks:** MCP teavitussüsteem on eriti kasulik pikkade AI ülesannete puhul, kus soovite kasutajat hoida kursis edenemisega.

## Voogedastus MCP-s

Nüüd, kui oled näinud mõned soovitused ja võrdlused klassikalise voogedastuse ja MCP voogedastuse vahe kohta, vaatame detailselt, kuidas saad MCP voogedastust kasutada.

Mõistmine, kuidas voogedastus MCP raamistiku sees toimib, on oluline reageerivate rakenduste loomiseks, mis pakuvad reaalajas tagasisidet kasutajatele pikkade toimingute ajal.

MCP-s ei ole voogedastus seotud peamise vastuse tükeldamisega, vaid **teavituste** saatmisega kliendile, kui tööriist töötleb päringut. Need teavitused võivad sisaldada edenemise värskendusi, logisid või muid sündmusi.

### Kuidas see töötab

Peamine tulemus saadetakse ikkagi ühe vastusena. Kuid teavitusi võib töötlemise ajal saata eraldiseisvate sõnumitena ja sellega värskendada klienti reaalajas. Klient peab olema võimeline neid teavitusi vastu võtma ja kuvama.

## Mis on teavitus?

Me ütlesime „Teavitus“, mida see MCP kontekstis tähendab?

Teavitus on serveri poolt kliendile saadetud sõnum, mis informeerib edenemise, oleku või muude sündmuste kohta pikaajalise toimingu jooksul. Teavitused parandavad läbipaistvust ja kasutajakogemust.

Näiteks peaks klient saatma teavituse, kui algne käepigistus serveriga on tehtud.

Teavitus näeb JSON sõnumina välja selline:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Teavitused kuuluvad MCP teemasse nimega ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Aegumise teade:** MCP spetsifikatsiooni 2026-07-28 versiooni kandidaat märgib Logging algfunktsiooni aegunuks ning soovitab kasutada `stderr` stdio transpordile ja OpenTelemetry-d struktureeritud jälgimiseks. Logging töötab edasi 2025-11-25 versioonis ja vähemalt aasta pärast igasugust ametlikku aegumist. Vaata lähemalt [Mis muutub MCP-s: 2026-07-28 versiooni kandidaat](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Logimise tööle saamiseks peab server selle lubama kui funktsiooni/omadust järgmiselt:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Sõltuvalt kasutatavast SDK-st võib logimine olla vaikimisi lubatud või vajada serveri konfiguratsioonis eksplicitset lubamist.

Erinevat tüüpi teavitused:

| Tase       | Kirjeldus                      | Näide kasutusjuhtumist       |
|-----------|-------------------------------|------------------------------|
| debug     | Üksikasjalik silumisinfo       | Funktsiooni sisenemis-/väljapääsupunktid |
| info      | Üldised informatiivsed sõnumid | Toimingu edenemise värskendused |
| notice    | Tavalised, kuid olulised sündmused | Konfiguratsiooni muudatused  |
| warning   | Hoiatused                    | Aegunud funktsionaalsuse kasutamine |
| error     | Veatingimused                 | Toimingu ebaõnnestumised     |
| critical  | Kriitilised tingimused        | Süsteemi komponentide tõrked |
| alert     | Toiming tuleb viivitamatult võtta | Andmete rikkumise tuvastamine |
| emergency | Süsteem ei ole kasutatav       | Täielik süsteemi rike       |

## Teavituste rakendamine MCP-s

Teavituste rakendamiseks MCP-s pead seadistama nii serveri kui ka kliendi pool, et töödelda reaalajas värskendusi. See võimaldab sinu rakendusel pakkuda kasutajatele viivitamatut tagasisidet pikkade toimingute ajal.

### Serveripool: teavituste saatmine

Alustame serveripoolest. MCP-s määratled tööriistad, mis saadavad teavitusi päringute töötlemise ajal. Server kasutab konteksti objekti (tavaliselt `ctx`), et saata kliendile sõnumeid.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Eelmises näites saadab tööriist `process_files` kliendile kolm teavitust, kui ta töötleb iga faili. `ctx.info()` meetodit kasutatakse informatiivsete sõnumite saatmiseks.

Lisaks, et lubada teavitusi, veendu, et server kasutab voogedastustransporti (nt `streamable-http`) ja klient rakendab sõnumite töötleja teavituste töötlemiseks. Siin on, kuidas seadistada server `streamable-http` transpordi kasutamiseks:

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

Selles .NET näites on `ProcessFiles` tööriist märgistatud `Tool` atribuudiga ja saadab kolm teavitust kliendile iga faili töötlemisel. `ctx.Info()` meetodit kasutatakse informatiivsete sõnumite saatmiseks.

Teavituste lubamiseks oma .NET MCP serveris veendu, et kasutad voogedastustransporti:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Kliendipool: teavituste vastuvõtt

Klient peab rakendama sõnumite töötleja, et töödelda ja kuvada saabuvate teavituste sisu.

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

Eelnevas koodis kontrollib `message_handler` funktsioon, kas saabuvat sõnumit on teavitus. Kui on, siis prindib teavituse, muidu töötleb seda tavalise serveri sõnumina. Märka, kuidas `ClientSession` on algatatud `message_handler`-iga saabuvate teavituste käsitlemiseks.

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

Selles .NET näites kontrollib `MessageHandler` funktsioon, kas saabuvat sõnumit on teavitus. Kui on, siis prindib teavituse, muidu töötleb seda tavalise serveri sõnumina. `ClientSession` on algatatud sõnumite töötlejaga `ClientSessionOptions` kaudu.

Teavituste lubamiseks veendu, et server kasutab voogedastustransporti (nt `streamable-http`) ja klient võtab kasutusele sõnumite töötleja teavituste töötlemiseks.

## Edenemise teavitused ja stsenaariumid

See jaotis selgitab edenemise teavituste mõistet MCP-s, miks need on olulised ja kuidas neid rakendada streamable HTTP abil. Leiad ka praktilise ülesande oma mõistmise süvendamiseks.

Edenemise teavitused on reaalajas sõnumid, mida server saadab kliendile pikkade toimingute kestel. Selle asemel, et oodata protsessi lõpuni, hoiab server klienti kursis praeguse olekuga. See parandab läbipaistvust, kasutajakogemust ja lihtsustab silumist.

**Näide:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Miks kasutada edenemise teavitusi?

Edenemise teavitused on olulised mitmel põhjusel:

- **Parem kasutajakogemus:** Kasutajad näevad värskendusi töö edenemisel, mitte ainult lõpus.
- **Reaalajas tagasiside:** Kliendid saavad kuvada edenemisribasid või logisid, muutes rakenduse tundelt reageerivaks.
- **Lihtsam silumine ja monitooring:** Arendajad ja kasutajad näevad, kus protsess võib olla aeglane või kinni jäänud.

### Kuidas rakendada edenemise teavitusi

Siin on, kuidas saad edenemise teavitusi MCP-s rakendada:

- **Serveris:** Kasuta `ctx.info()` või `ctx.log()` teavituste saatmiseks iga üksuse töötlemisel. See saadab sõnumi kliendile enne peamise tulemuse valmimist.
- **Klientides:** Rakenda sõnumite töötleja, mis kuulab saabuvad teavitused ja kuvab need. Töötleja eristab teavitusi ja lõplikku tulemust.

**Serveri näide:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Kliendi näide:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Turvalisuse kaalutlused

Turvalisus peaks olema kõrgeim prioriteet mis tahes serveri rakendamisel, eriti HTTP-põhiste transpordimehhanismide nagu MCP Streamable HTTP kasutamisel.

MCP serverite rakendamisel HTTP-põhiste transpordimehhanismidega muutub turvalisus ülioluliseks küsimuseks, mis nõuab hoolikat tähelepanu mitmetele ründepindadele ja kaitsemehhanismidele.

### Ülevaade

Turvalisus on kriitiline MCP serverite HTTP kaudu avalikustamisel. Streamable HTTP toob kaasa uusi ründepindasid ja vajab hoolikat seadistamist.

Siin on mõned peamised turvalisuse kaalutlused:

- **Origin päise valideerimine**: Kontrolli alati `Origin` päist, et vältida DNS-i ümberseadistamise rünnakuid.
- **Localhosti sidumine**: Kohalikuks arenduseks seo serverid `localhost`-iga, et vältida nende avalikku internetti avalikustamist.
- **Autentimine**: Rakenda tootmiskeskkonnas autentimine (nt API võtmed, OAuth).
- **CORS**: Sea sisse Cross-Origin Resource Sharing (CORS) poliitikad juurdepääsu piiramiseks.
- **HTTPS**: Kasuta tootmiskeskkonnas HTTPS-i, et krüpteerida liiklust.

### Parimad tavad

Lisaks on siin mõned parimad tavad, mida järgida turvalisuse rakendamisel MCP voogedastusteenuses:

- Ära kunagi usalda sissetulevaid päringuid ilma valideerimiseta.
- Logi ja jälgi kogu juurdepääsu ja vead.
- Uuenda regulaarselt sõltuvusi, et parandada turvaauke.

### Väljakutsed

MCP voogedastusteenuste turvalisuse rakendamisel seisad silmitsi mõningate väljakutsetega:

- Turvalisuse ja arendamise lihtsuse tasakaalustamine
- Mitmesuguste kliendi keskkondadega ühilduvuse tagamine


## Üleminek SSE-st Streamable HTTP-le

Rakendustele, mis kasutavad praegu Server-Sent Events (SSE), pakub Streamable HTTP suuremaid võimalusi ja paremat pikaajalist jätkusuutlikkust MCP lahendustele.

### Miks uuendada?

Olemas on kaks veenvat põhjust SSE-st Streamable HTTP-le üleminekuks:

- Streamable HTTP pakub paremat skaleeritavust, ühilduvust ja rikkalikumat teavitustuge kui SSE.
- See on soovitatav transpordimeetod uutele MCP rakendustele.

### Ülemineku sammud

Siin on, kuidas saate oma MCP rakendustes SSE-st üle minna Streamable HTTP-le:

- **Uuenda serveri koodi**, kasutades `transport="streamable-http"` funktsioonis `mcp.run()`.
- **Uuenda kliendi koodi**, kasutades `streamablehttp_client` asemel SSE klienti.
- **Rakenda sõnumi käitleja** kliendis teavituste töötlemiseks.
- **Testi ühilduvust** olemasolevate tööriistade ja töövoogudega.

### Ühilduvuse säilitamine

Soovitatav on säilitada olemasolevate SSE klientidega ühilduvus ülemineku ajal. Siin on mõned strateegiad:

- Saate toetada nii SSE kui ka Streamable HTTP-d, kasutades mõlemaid transpordimeetodeid erinevatel lõpp-punktidel.
- Migreeri kliente järk-järgult uuele transpordile.

### Väljakutsed

Tagage järgmiste väljakutsetega tegelemine migratsiooni ajal:

- Kõikide klientide uuendamine
- Erinevuste haldamine teavituste edastamises

### Ülesanne: Ehita oma voogedastuse MCP rakendus

**Stsenaarium:**
Koosta MCP server ja klient, kus server töötleb üksuste (nt failide või dokumentide) loendit ja saadab teavituse iga töödeldud üksuse kohta. Klient kuvab iga saabunud teavituse reaalajas.

**Sammud:**

1. Rakenda serveri tööriist, mis töötleb loendit ja saadab teavitusi iga üksuse kohta.
2. Rakenda klient koos sõnumi käitlejaga teavituste reaalajas kuvamiseks.
3. Testi oma rakendust, käivitades nii serveri kui ka kliendi ning jälgi teavitusi.

[Lahendus](./solution/README.md)

## Edasine lugemine ja järgmised sammud

MCP voogedastuse teekonnal edasi liikudes ja teadmisi laiendades pakub see jaotis lisavahendeid ja soovitusi keerukamate rakenduste loomiseks.

### Edasine lugemine

- [Microsoft: Sissejuhatus HTTP voogedastusse](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ASP.NET Core-s](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Voogedastusega päringud](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Järgmised sammud

- Proovi ehitada keerukamaid MCP tööriistu, mis kasutavad voogedastust reaalajas analüütika, vestluse või koostöötoimetamise jaoks.
- Uuri MCP voogedastuse integreerimist frontend raamistikudega (React, Vue jne) elavate kasutajaliidese uuenduste jaoks.
- Järgmine: [AI tööriistakomplekti kasutamine VSCode’is](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->