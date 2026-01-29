# HTTPS voogedastus Model Context Protocoli (MCP) abil

See peatükk pakub põhjalikku juhendit turvalise, skaleeritava ja reaalajas voogedastuse rakendamiseks Model Context Protocoli (MCP) abil, kasutades HTTPS-i. Käsitletakse voogedastuse motivatsiooni, saadaolevaid transpordimehhanisme, voogedastatava HTTP rakendamist MCP-s, turvalisuse parimaid tavasid, üleminekut SSE-lt ja praktilisi juhiseid oma MCP voogedastusrakenduste loomiseks.

## Transpordimehhanismid ja voogedastus MCP-s

See jaotis uurib erinevaid MCP-s saadaolevaid transpordimehhanisme ja nende rolli reaalajas suhtluse voogedastuse võimaldamisel klientide ja serverite vahel.

### Mis on transpordimehhanism?

Transpordimehhanism määratleb, kuidas andmeid kliendi ja serveri vahel vahetatakse. MCP toetab mitut transporditüüpi, et vastata erinevatele keskkondadele ja nõuetele:

- **stdio**: Standardne sisend/väljund, sobib kohalike ja CLI-põhiste tööriistade jaoks. Lihtne, kuid mitte sobiv veebis või pilves kasutamiseks.
- **SSE (Server-Sent Events)**: Võimaldab serveritel saata reaalajas värskendusi klientidele HTTP kaudu. Hea veebiliideste jaoks, kuid piiratud skaleeritavuse ja paindlikkusega.
- **Voogedastatav HTTP**: Kaasaegne HTTP-põhine voogedastuse transport, mis toetab teavitusi ja paremat skaleeritavust. Soovitatav enamiku tootmis- ja pilvesituatsioonide jaoks.

### Võrdlustabel

Vaadake allolevat võrdlustabelit, et mõista nende transpordimehhanismide erinevusi:

| Transport         | Reaalajas värskendused | Voogedastus | Skaleeritavus | Kasutusjuhtum              |
|-------------------|------------------------|-------------|---------------|---------------------------|
| stdio             | Ei                     | Ei          | Madal         | Kohalikud CLI tööriistad   |
| SSE               | Jah                    | Jah         | Keskmine      | Veeb, reaalajas värskendused |
| Voogedastatav HTTP| Jah                    | Jah         | Kõrge         | Pilv, mitme kliendi tugi   |

> **Näpunäide:** Õige transpordi valik mõjutab jõudlust, skaleeritavust ja kasutajakogemust. **Voogedastatav HTTP** on soovitatav kaasaegsete, skaleeritavate ja pilvevalmis rakenduste jaoks.

Pange tähele transpordimehhanisme stdio ja SSE, mida käsitleti eelnevates peatükkides, ning kuidas voogedastatav HTTP on transpordimehhanism, mida käsitletakse selles peatükis.

## Voogedastus: Kontseptsioonid ja motivatsioon

Voogedastuse põhimõtete ja motivatsioonide mõistmine on oluline tõhusate reaalajas suhtlussüsteemide rakendamiseks.

**Voogedastus** on võrguprogrammeerimise tehnika, mis võimaldab andmeid saata ja vastu võtta väikeste, hallatavate osadena või sündmuste jadana, mitte oodata kogu vastuse valmimist. See on eriti kasulik:

- Suurte failide või andmekogumite puhul.
- Reaalajas värskenduste jaoks (nt vestlus, edenemisribad).
- Pikaajaliste arvutuste puhul, kus soovite kasutajat kursis hoida.

Siin on, mida peate voogedastuse kohta kõrgel tasemel teadma:

- Andmed edastatakse järk-järgult, mitte kõik korraga.
- Klient saab andmeid töödelda nende saabumisel.
- Vähendab tajutavat latentsust ja parandab kasutajakogemust.

### Miks kasutada voogedastust?

Voogedastuse kasutamise põhjused on järgmised:

- Kasutajad saavad kohe tagasisidet, mitte ainult protsessi lõpus.
- Võimaldab reaalajas rakendusi ja reageerivaid kasutajaliideseid.
- Tõhusam võrgu- ja arvutusressursside kasutamine.

### Lihtne näide: HTTP voogedastuse server ja klient

Siin on lihtne näide, kuidas voogedastust rakendada:

#### Python

**Server (Python, kasutades FastAPI ja StreamingResponse):**

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

**Klient (Python, kasutades requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

See näide demonstreerib, kuidas server saadab kliendile sõnumite jada nende valmimisel, mitte ei oota kõigi sõnumite valmimist.

**Kuidas see töötab:**

- Server edastab iga sõnumi selle valmimisel.
- Klient võtab vastu ja kuvab iga saabunud osa.

**Nõuded:**

- Server peab kasutama voogedastuse vastust (nt `StreamingResponse` FastAPI-s).
- Klient peab töötlema vastust voona (`stream=True` requests-is).
- Content-Type on tavaliselt `text/event-stream` või `application/octet-stream`.

#### Java

**Server (Java, kasutades Spring Boot ja Server-Sent Events):**

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

**Klient (Java, kasutades Spring WebFlux WebClient):**

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

**Java rakenduse märkused:**

- Kasutab Spring Booti reaktiivset stacki koos `Flux`-iga voogedastuseks.
- `ServerSentEvent` pakub struktureeritud sündmuste voogedastust koos sündmuste tüüpidega.
- `WebClient` koos `bodyToFlux()` võimaldab reaktiivset voogedastuse tarbimist.
- `delayElements()` simuleerib töötlemisaega sündmuste vahel.
- Sündmustel võivad olla tüübid (`info`, `result`) paremaks kliendipoolseks käsitlemiseks.

### Võrdlus: Klassikaline voogedastus vs MCP voogedastus

Erinevused klassikalise voogedastuse ja MCP voogedastuse vahel on järgmised:

| Funktsioon            | Klassikaline HTTP voogedastus | MCP voogedastus (teavitused)       |
|------------------------|------------------------------|------------------------------------|
| Peamine vastus         | Tükeldatud                   | Üksik, lõpus                      |
| Edenemise värskendused | Saadetakse andmeosadena       | Saadetakse teavitustena           |
| Kliendi nõuded         | Peab töötlema voogu          | Peab rakendama sõnumikäsitlejat   |
| Kasutusjuhtum          | Suured failid, AI token vood | Edenemine, logid, reaalajas tagasiside |

### Täheldatud peamised erinevused

Lisaks on mõned peamised erinevused:

- **Suhtlusmuster:**
  - Klassikaline HTTP voogedastus: Kasutab lihtsat tükeldatud edastuskodeeringut andmete saatmiseks osadena.
  - MCP voogedastus: Kasutab struktureeritud teavitussüsteemi koos JSON-RPC protokolliga.

- **Sõnumi formaat:**
  - Klassikaline HTTP: Lihttekstiosad koos reavahetustega.
  - MCP: Struktureeritud LoggingMessageNotification objektid koos metaandmetega.

- **Kliendi rakendus:**
  - Klassikaline HTTP: Lihtne klient, mis töötleb voogedastuse vastuseid.
  - MCP: Täiustatud klient, millel on sõnumikäsitleja erinevate sõnumitüüpide töötlemiseks.

- **Edenemise värskendused:**
  - Klassikaline HTTP: Edenemine on osa peamisest vastuse voost.
  - MCP: Edenemine saadetakse eraldi teavitussõnumitena, samal ajal kui peamine vastus saabub lõpus.

### Soovitused

Mõned soovitused klassikalise voogedastuse (nagu näidatud ülaltoodud `/stream` lõpp-punkti näites) ja MCP voogedastuse vahel valimiseks:

- **Lihtsate voogedastusvajaduste jaoks:** Klassikaline HTTP voogedastus on lihtsam rakendada ja piisav põhiliste voogedastusvajaduste jaoks.
- **Komplekssete, interaktiivsete rakenduste jaoks:** MCP voogedastus pakub struktureeritumat lähenemist rikkalike metaandmete ja teavituste ning lõpptulemuste eraldamisega.
- **AI rakenduste jaoks:** MCP teavitussüsteem on eriti kasulik pikaajaliste AI ülesannete jaoks, kus soovite kasutajaid edenemise kohta kursis hoida.

## Voogedastus MCP-s

Okei, olete näinud mõningaid soovitusi ja võrdlusi klassikalise voogedastuse ja MCP voogedastuse vahel. Vaatame nüüd täpsemalt, kuidas MCP-s voogedastust kasutada.

MCP raamistiku sees voogedastuse toimimise mõistmine on oluline reageerivate rakenduste loomiseks, mis pakuvad kasutajatele reaalajas tagasisidet pikaajaliste toimingute ajal.

MCP-s ei tähenda voogedastus peamise vastuse saatmist osadena, vaid **teavituste** saatmist kliendile tööriista päringu töötlemise ajal. Need teavitused võivad sisaldada edenemise värskendusi, logisid või muid sündmusi.

### Kuidas see töötab

Peamine tulemus saadetakse endiselt ühe vastusena. Kuid teavitusi saab saata eraldi sõnumitena töötlemise ajal, pakkudes kliendile reaalajas värskendusi. Klient peab olema võimeline neid teavitusi käsitlema ja kuvama.

## Mis on teavitus?

Me mainisime "teavitust", mida see MCP kontekstis tähendab?

Teavitus on sõnum, mille server saadab kliendile, et teavitada edenemisest, olekust või muudest sündmustest pikaajalise toimingu ajal. Teavitused parandavad läbipaistvust ja kasutajakogemust.

Näiteks peab klient saatma teavituse pärast esialgset käepigistust serveriga.

Teavitus näeb välja nagu JSON-sõnum:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Teavitused kuuluvad MCP-s teemasse nimega ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Logimise tööle saamiseks peab server selle lubama funktsiooni/võimekusena järgmiselt:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Sõltuvalt kasutatavast SDK-st võib logimine olla vaikimisi lubatud või peate selle serveri konfiguratsioonis selgesõnaliselt lubama.

Teavitustel on erinevad tüübid:

| Tase      | Kirjeldus                     | Näide kasutusjuhtumist          |
|-----------|-------------------------------|---------------------------------|
| debug     | Üksikasjalik silumisinfo      | Funktsiooni sisenemis-/väljumispunktid |
| info      | Üldised informatiivsed sõnumid| Toimingu edenemise värskendused |
| notice    | Tavalised, kuid olulised sündmused | Konfiguratsiooni muutused      |
| warning   | Hoiatusolukorrad              | Aegunud funktsiooni kasutamine |
| error     | Veatingimused                 | Toimingu ebaõnnestumised       |
| critical  | Kriitilised tingimused        | Süsteemi komponendi tõrked     |
| alert     | Kohene tegevus vajalik       | Andmete rikkumise tuvastamine  |
| emergency | Süsteem ei ole kasutatav      | Täielik süsteemi tõrge         |

## Teavituste rakendamine MCP-s

Teavituste rakendamiseks MCP-s peate seadistama nii serveri kui ka kliendi poole, et käsitleda reaalajas värskendusi. See võimaldab teie rakendusel pakkuda kasutajatele kohest tagasisidet pikaajaliste toimingute ajal.

### Serveri pool: Teavituste saatmine

Alustame serveri poolega. MCP-s määratlete tööriistad, mis saavad teavitusi saata päringute töötlemise ajal. Server kasutab kontekstiobjekti (tavaliselt `ctx`), et saata sõnumeid kliendile.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Eelnevas näites saadab `process_files` tööriist kliendile kolm teavitust iga faili töötlemise ajal. `ctx.info()` meetodit kasutatakse informatiivsete sõnumite saatmiseks.

Lisaks, et teavitused oleksid lubatud, veenduge, et teie server kasutab voogedastuse transporti (nt `streamable-http`) ja teie klient rakendab sõnumikäsitlejat teavituste töötlemiseks. Siin on, kuidas seadistada serverit kasutama `streamable-http` transporti:

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

Selles .NET näites saadab `ProcessFiles` tööriist, mis on märgistatud `Tool` atribuudiga, kliendile kolm teavitust iga faili töötlemise ajal. `ctx.Info()` meetodit kasutatakse informatiivsete sõnumite saatmiseks.

Teavituste lubamiseks oma .NET MCP serveris veenduge, et kasutate voogedastuse transporti:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Kliendi pool: Teavituste vastuvõtmine

Klient peab rakendama sõnumikäsitleja, et töödelda ja kuvada teavitusi nende saabumisel.

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

Eelnevas koodis kontrollib `message_handler` funktsioon, kas saabuv sõnum on teavitus. Kui see on, prinditakse teavitus; vastasel juhul töödeldakse seda tavalise serveri sõnumina. Samuti pange tähele, kuidas `ClientSession` on algatatud `message_handler`-iga, et käsitleda saabuvaid teavitusi.

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

Selles .NET näites kontrollib `MessageHandler` funktsioon, kas saabuv sõnum on teavitus. Kui see on, prinditakse teavitus; vastasel juhul töödeldakse seda tavalise serveri sõnumina. `ClientSession` on algatatud sõnumikäsitlejaga `ClientSessionOptions` kaudu.

Teavituste lubamiseks veenduge, et teie server kasutab voogedastuse transporti (nt `streamable-http`) ja teie klient rakendab sõnumikäsitlejat teavituste töötlemiseks.

## Edenemise teavitused ja stsenaariumid

See jaotis selgitab edenemise teavituste kontseptsiooni MCP-s, miks need on olulised ja kuidas neid rakendada voogedastatava HTTP abil. Samuti leiate praktilise ülesande oma arusaama tugevdamiseks.

Edenemise teavitused on reaalajas sõnumid, mida server saadab kliendile pikaajaliste toimingute ajal. Selle asemel, et oodata kogu protsessi lõppu, hoiab server klienti kursis praeguse olekuga. See parandab läbipaistvust, kasutajakogemust ja muudab silumise lihtsamaks.

**Näide:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Miks kasutada edenemise teavitusi?

Edenemise teavitused on olulised mitmel põhjusel:

- **Parem kasutajakogemus:** Kasutajad näevad värskendusi töö edenemise ajal, mitte ainult lõpus.
- **Reaalajas tagasiside:** Kliendid saavad kuvada edenemisribasid või logisid, muutes rakenduse reageerivaks.
- **Lihtsam silumine ja jälgimine:** Arendajad ja kasutajad näevad, kus protsess võib olla aeglane või kinni.

### Kuidas rakendada edenemise teavitusi

Siin on, kuidas edenemise teavitusi MCP-s rakendada:

- **Serveris:** Kasutage `ctx.info()` või `ctx.log()`, et saata teavitusi iga üksuse töötlemise ajal. See saadab sõnumi kliendile enne peamise tulemuse valmimist.
- **Kliendis:** Rakendage sõnumikäsitleja, mis kuulab ja kuvab teavitusi nende saabumisel. See käsitleja eristab teavitusi ja lõpptulemust.

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

MCP serverite rakendamisel HTTP-põhiste transpordimehhanismidega muutub turvalisus oluliseks küsimuseks, mis nõuab hoolikat tähelepanu mitmetele rünnakuvektoritele ja kaitsemehhanismidele.

### Ülevaade

Turvalisus on kriitiline MCP serverite HTTP kaudu avaldamisel. Voogedastatav HTTP tutvustab uusi rünnakupindu ja nõuab hoolikat konfigureerimist.

### Olulised punktid

- **Origin päise valideerimine**: Kontrollige alati `Origin` päist, et vältida DNS-i uuesti sidumise rünnakuid.
- **Localhost sidumine**: Kohaliku arenduse jaoks siduge serverid `localhost`-iga, et vältida nende avalikku internetti avaldamist.
- **Autentimine**: Rakendage autentimist (nt API võtmed, OAuth) tootmiskeskkonnas.
- **CORS**: Konfigureerige Cross-Origin Resource Sharing (CORS) poliitikad, et piirata juurdepääsu.
- **HTTPS**: Kasutage tootmiskeskkonnas HTTPS-i, et liiklust krüpteerida.

### Parimad tavad

- Ärge kunagi usaldage sissetulevaid päringuid ilma valideerimiseta.
- Logige ja jälgige kõ
## Üleminek SSE-lt voogedastatavale HTTP-le

Rakenduste jaoks, mis praegu kasutavad Server-Sent Events (SSE), pakub üleminek voogedastatavale HTTP-le paremaid võimalusi ja pikaajalist jätkusuutlikkust MCP rakenduste jaoks.

### Miks uuendada?

SSE-lt voogedastatavale HTTP-le üleminekuks on kaks veenvat põhjust:

- Voogedastatav HTTP pakub paremat skaleeritavust, ühilduvust ja rikkalikumat teavituste tuge kui SSE.
- See on soovitatav transpordimeetod uute MCP rakenduste jaoks.

### Ülemineku sammud

Siin on juhised, kuidas oma MCP rakendustes SSE-lt voogedastatavale HTTP-le üle minna:

- **Uuenda serveri koodi**, et kasutada `transport="streamable-http"` funktsioonis `mcp.run()`.
- **Uuenda kliendi koodi**, et kasutada `streamablehttp_client` SSE kliendi asemel.
- **Rakenda sõnumite töötleja** kliendis teavituste töötlemiseks.
- **Testi ühilduvust** olemasolevate tööriistade ja töövoogudega.

### Ühilduvuse säilitamine

Soovitatav on säilitada ühilduvus olemasolevate SSE klientidega ülemineku ajal. Siin on mõned strateegiad:

- Võid toetada nii SSE-d kui ka voogedastatavat HTTP-d, käivitades mõlemad transpordimeetodid erinevatel lõpp-punktidel.
- Migreeri kliendid järk-järgult uuele transpordimeetodile.

### Väljakutsed

Veendu, et tegeled järgmiste väljakutsetega ülemineku ajal:

- Kõigi klientide uuendamine
- Erinevuste käsitlemine teavituste edastamisel

## Turvalisuse kaalutlused

Turvalisus peaks olema esmatähtis iga serveri rakendamisel, eriti HTTP-põhiste transpordimeetodite, nagu voogedastatav HTTP, kasutamisel MCP-s.

HTTP-põhiste transpordimeetoditega MCP serverite rakendamisel muutub turvalisus ülioluliseks, nõudes hoolikat tähelepanu mitmetele rünnakuvektoritele ja kaitsemehhanismidele.

### Ülevaade

Turvalisus on kriitiline MCP serverite HTTP kaudu avalikustamisel. Voogedastatav HTTP avab uusi rünnakupindu ja nõuab hoolikat konfigureerimist.

Siin on mõned olulised turvalisuse kaalutlused:

- **Origin päise valideerimine**: Kontrolli alati `Origin` päist, et vältida DNS-i uuesti sidumise rünnakuid.
- **Localhosti sidumine**: Kohaliku arenduse jaoks seo serverid `localhost`-iga, et vältida nende avalikku internetti sattumist.
- **Autentimine**: Rakenda autentimist (nt API võtmed, OAuth) tootmiskeskkonnas.
- **CORS**: Konfigureeri Cross-Origin Resource Sharing (CORS) poliitikad juurdepääsu piiramiseks.
- **HTTPS**: Kasuta tootmiskeskkonnas HTTPS-i liikluse krüpteerimiseks.

### Parimad tavad

Lisaks on siin mõned parimad tavad MCP voogedastava serveri turvalisuse rakendamisel:

- Ära usalda sissetulevaid päringuid ilma valideerimiseta.
- Logi ja jälgi kogu juurdepääsu ja vigu.
- Uuenda regulaarselt sõltuvusi, et parandada turvaauke.

### Väljakutsed

MCP voogedastavate serverite turvalisuse rakendamisel seisad silmitsi mõningate väljakutsetega:

- Turvalisuse tasakaalustamine arendamise lihtsusega
- Ühilduvuse tagamine erinevate kliendikeskkondadega

### Ülesanne: Ehita oma voogedastav MCP rakendus

**Stsenaarium:**
Ehita MCP server ja klient, kus server töötleb nimekirja üksustest (nt failid või dokumendid) ja saadab teavituse iga töödeldud üksuse kohta. Klient peaks kuvama iga teavituse reaalajas.

**Sammud:**

1. Rakenda serveri tööriist, mis töötleb nimekirja ja saadab teavitusi iga üksuse kohta.
2. Rakenda klient koos sõnumite töötlejaga, et kuvada teavitusi reaalajas.
3. Testi oma rakendust, käivitades nii serveri kui ka kliendi, ja jälgi teavitusi.

[Solution](./solution/README.md)

## Lisalugemine ja järgmised sammud

MCP voogedastamisega edasi liikumiseks ja oma teadmiste laiendamiseks pakub see jaotis täiendavaid ressursse ja soovitatud järgmisi samme keerukamate rakenduste loomiseks.

### Lisalugemine

- [Microsoft: HTTP voogedastamise sissejuhatus](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ASP.NET Core'is](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Voogedastavad päringud](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Mis edasi?

- Proovi luua keerukamaid MCP tööriistu, mis kasutavad voogedastust reaalajas analüütika, vestluse või koostööredigeerimise jaoks.
- Uuri MCP voogedastuse integreerimist esipaneeli raamistikesse (React, Vue jne) reaalajas kasutajaliidese uuenduste jaoks.
- Järgmine: [AI tööriistakomplekti kasutamine VSCode'is](../07-aitk/README.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.