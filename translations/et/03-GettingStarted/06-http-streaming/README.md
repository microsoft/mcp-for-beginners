# HTTPS voogedastus mudelikonteksti protokolliga (MCP)

See peatükk annab põhjaliku juhendi turvalise, skaleeritava ja reaalajas voogedastuse rakendamiseks mudelikonteksti protokolli (MCP) abil, kasutades HTTPS-i. Käsitletakse voogedastuse motivatsiooni, saadaolevaid transpordimehhanisme, kuidas MCP-s voogedastatavat HTTP-d rakendada, turvalisuse parimaid tavasid, üleminekut SSE-st ning praktilisi juhiseid oma voogedastavate MCP-rakenduste ehitamiseks.

> **Vaatame ette:** see õppetund kirjeldab voogedastatavat HTTP-d MCP spetsifikatsiooni **2025-11-25** alusel, kus sessioon luuakse `initialize` ajal ja jäädvustatakse `Mcp-Session-Id` päisega. Väljalaske kandidaatversioon `2026-07-28` eemaldab tervitusisendi ja sessiooni ID täielikult, tehes iga päringu iseseisvaks ja suunatavaks mis tahes serveri eksemplarile ilma staatiliste sessioonideta. Täpsemate üksikasjade jaoks vaadake [Mis MCP-s muutub: 2026-07-28 väljalaske kandidaatversioon](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

## MCP transpordimehhanismid ja voogedastus

Selles jaotises uuritakse MCP-s saadaolevaid erinevaid transpordimehhanisme ja nende rolli voogedastuse võimaldamisel klientide ja serverite vahel realoa suhtluses.

### Mis on transpordimehhanism?

Transpordimehhanism määrab, kuidas andmeid vahetatakse kliendi ja serveri vahel. MCP toetab mitut transporditüüpi, et sobituda erinevate keskkondade ja nõuetega:

- **stdio**: Standardne sisend/väljund, sobib kohalikeks ja käsureapõhisteks tööriistadeks. Lihtne, kuid ei sobi veebi ega pilve jaoks.
- **SSE (Server-Sent Events)**: Võimaldab serveritel saata HTTP kaudu klientidele reaalajas värskendusi. Sobib veebi kasutajaliidestele, kuid on piiratud skaleeritavuse ja paindlikkusega. Alates MCP spetsifikatsiooni 2025-06-18 on iseseisev SSE transpordimehhanism kasutusest kõrvaldatud ja asendatud "voogedastatava HTTP" transpordiga.
- **Voogedastatav HTTP**: Kaasaegne HTTP-põhine voogedastus, mis toetab teavitusi ja paremat skaleeritavust. Soovitatav enamusele tootmis- ja pilvesituatsioonidele.

### Võrdlustabel

Vaadake allolevat võrdlustabelit, et mõista erinevusi nende transpordimehhanismide vahel:

| Transport         | Reaalajas värskendused | Voogedastus | Skaleeritavus | Kasutusjuhtum          |
|-------------------|------------------------|-------------|---------------|-----------------------|
| stdio             | Ei                     | Ei          | Madal         | Kohalikud CLI tööriistad |
| SSE               | Jah                    | Jah         | Keskmine      | Veeb, reaalajas värskendused |
| Voogedastatav HTTP| Jah                    | Jah         | Kõrge         | Pilv, mitme kliendi tugi |

> **Vihje:** Õige transpordimehhanismi valik mõjutab jõudlust, skaleeritavust ja kasutajakogemust. **Voogedastatav HTTP** on soovitatav kaasaegsete, skaleeritavate ja pilvevalmis rakenduste jaoks.

Pöörake tähelepanu transpordidele stdio ja SSE, mida teile varasemates peatükkides tutvustati, ning sellele, kui voogedastatav HTTP on selle peatüki käsitlemise transpordimehhanism.

## Voogedastus: mõisted ja motivatsioon

Voogedastuse põhikontseptsioonide ja motivatsiooni mõistmine on oluline tõhusate reaalaja suhtlussüsteemide rakendamiseks.

**Voogedastus** on võrkude programmeerimise tehnik, mis võimaldab andmeid saata ja vastu võtta väikeste, hallatavate tükkidena või sündmuste jada kujul, mitte oodata kogu vastuse valmimist. See on eriti kasulik:

- Suurte failide või andmebaaside puhul.
- Reaalajas värskenduste jaoks (nt vestlus, edenemisribad).
- Pikaajaliste arvutuste puhul, kus soovite kasutajat informeerida.

Siin on ülevaade voogedastusest kõrgemas plaanis:

- Andmed edastatakse järk-järgult, mitte korraga.
- Klient saab andmeid töötlema hakata kohe, kui need saabuvad.
- Vähendab tajutavat latentsust ja parandab kasutajakogemust.

### Miks kasutada voogedastust?

Põhjused voogedastuse kasutamiseks on järgmised:

- Kasutajad saavad kohe tagasisidet, mitte alles lõpus.
- Võimaldab reaalajas rakendusi ja reageerivaid kasutajaliideseid.
- Võrgu- ja arvutusressursside tõhusam kasutamine.

### Lihtne näide: HTTP voogedastuse server ja klient

Siin on lihtne näide, kuidas voogedastust saab rakendada:

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

See näide demonstreerib serveri saatmist sõnumite jada klienti, kui need on kättesaadavad, mitte ootamist kõikide sõnumite valmimiseni.

**Kuidas see töötab:**

- Server annab iga sõnumi välja kohe, kui see valmis saab.
- Klient võtab iga osa vastu ja prindib selle kohe.

**Nõuded:**

- Server peab kasutama voogedastavat vastust (nt `StreamingResponse` FastAPI-s).
- Klient peab vastust töötlema voonena (`stream=True` requests-is).
- Sisutüübiks on tavaliselt `text/event-stream` või `application/octet-stream`.

#### Java

**Server (Java, kasutades Spring Boot ja serveripoolseid sündmusi):**

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

**Klient (Java, kasutades Spring WebFlux WebClient-i):**

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

**Java rakendusmärkused:**

- Kasutab Spring Boot reaktiivset virna koos `Flux`-iga voogedastuseks
- `ServerSentEvent` võimaldab struktureeritud sündmuste voogedastust sündmuse tüüpidega
- `WebClient` koos `bodyToFlux()` lubab reaktiivset voo tarbimist
- `delayElements()` simuleerib töötlemisaja viivitust sündmuste vahel
- Sündmustel võivad olla tüübid (`info`, `result`) paremaks kliendikäitlemiseks

### Võrdlus: klassikaline voogedastus vs MCP voogedastus

Erinevused klassikalise voogedastuse ja MCP voogedastuse vahel saab esitada järgmiselt:

| Funktsioon             | Klassikaline HTTP voogedastus | MCP voogedastus (teavitused)     |
|------------------------|-------------------------------|----------------------------------|
| Peamine vastus         | Jagatud tükkidena              | Üks vastus lõpus                 |
| Edenemisuuendused      | Saadetakse andmetükkidena      | Saadetakse teavitustena          |
| Kliendi nõuded         | Peab töötlema voogu            | Peab rakendama sõnumikäitlejat   |
| Kasutusjuhtum          | Suured failid, tehisintellekti tokeni vood | Edenemine, logid, reaalajas tagasiside |

### Täheldatud olulisemad erinevused

Lisaks mõned võtmeaspektid:

- **Suhtlemismudel:**
  - Klassikaline HTTP voogedastus: kasutab lihtsat killustatud ülekandekodeerimist andmete saatmiseks tükkidena
  - MCP voogedastus: kasutab struktureeritud teavitussüsteemi JSON-RPC protokolliga

- **Sõnumi vorming:**
  - Klassikaline HTTP: pelgalt lihttekstiga tükid reavahedega
  - MCP: struktureeritud LoggingMessageNotification objektid metaandmetega

- **Kliendi rakendus:**
  - Klassikaline HTTP: lihtne klient, mis töötleb voogedastusvastuseid
  - MCP: keerukam klient, millel on sõnumikäitleja erinevat tüüpi sõnumite töötlemiseks

- **Edenemisuuendused:**
  - Klassikaline HTTP: edenemine on osa põhivoo vastusest
  - MCP: edenemist saadetakse eraldi teavitussõnumitena, põhivastus saabub alles lõpus

### Soovitused

Soovitusi klassikalise voogedastuse (nagu näidatud `/stream` endpoint) ja MCP voogedastuse vahel valimisel:

- **Lihtsate voogedastuse vajaduste korral:** Klassikaline HTTP voogedastus on lihtsam rakendada ja piisav põhilistele vajadustele.

- **Komplekssete, interaktiivsete rakenduste jaoks:** MCP voogedastus pakub struktureeritumat lähenemist rikkalike metaandmete ja teavituste ning lõpptulemuse eraldamisega.

- **Tehisintellekti rakenduste jaoks:** MCP teavitussüsteem on eriti kasulik pikkade jooksuaegadega AI ülesannete puhul, kus soovite kasutajaid edenemisest hoida kursis.

## Voogedastus MCP-s

Nüüd, kui olete näinud mõned soovitused ja võrdlused klassikalise voogedastuse ja MCP voogedastuse erinevuse kohta, uurime täpsemalt, kuidas MCP-s voogedastust rakendada.

Mõistmine, kuidas voogedastus MCP raamistiku sees töötab, on oluline reageerivate rakenduste loomiseks, mis annavad reaalajas tagasisidet kasutajatele pikkade operatsioonide ajal.

MCP-s ei saadeta põhivastust tükkidena, vaid **teavitusi** kliendile selle asemel, et tööriist saadab sõnumeid taustal päringu töötlemise ajal. Need teavitused võivad sisaldada edenemisuuendusi, logisid või muid sündmusi.

### Kuidas see töötab

Peamine vastus saadetakse ikkagi ühe vastusena. Kuid teavitusi saab saata eraldi sõnumitena töötlemise ajal, et värskendada klienti reaalajas. Klient peab suutma need teavitused vastu võtta ja kuvada.

## Mis on teavitus?

Mainisime "teavitus", mida see MCP kontekstis tähendab?

Teavitus on sõnum, mille server saadab kliendile, et informeerida edenemisest, olekust või muust sündmusest pikaajalise toimingu jooksul. Teavitused parandavad läbipaistvust ja kasutajakogemust.

Näiteks peab klient saatma teavituse vahetult pärast esialgse käepigistuse sooritamist serveriga.

Teavitus näeb välja selline JSON sõnumina:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Teavitused kuuluvad MCP teemasse, mida nimetatakse ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Logimise tööle saamiseks peab server selle lubama kui funktsiooni/omaduse järgnevalt:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Sõltuvalt kasutatavast SDK-st võib logimine olla vaikimisi lubatud või peate selle oma serveri konfiguratsioonis selgesõnaliselt aktiveerima.

On mitut tüüpi teavitusi:

| Tase       | Kirjeldus                     | Näide kasutusjuhtum           |
|------------|-------------------------------|------------------------------|
| debug      | Detailne silumisinfo           | Funktsiooni sisenemine/väljaminek |
| info       | Üldised informatiivsed sõnumid | Operatsiooni edenemise uuendused |
| notice     | Tavapärased kuid olulised sündmused | Konfiguratsioonimuudatused  |
| warning    | Hoiatusolukorrad              | Kasutatud aegunud funktsioonid |
| error      | Vigade teated                 | Operatsioonitehted kukkusid läbi |
| critical   | Kriitilised olukorrad         | Süsteemi komponendi rikete teated |
| alert      | Kohene tegevus on kohustuslik | Andmete rikkumise tuvastamine |
| emergency  | Süsteem kasutuskõlbmatu       | Täielik süsteemi rike        |

## Teavituste rakendamine MCP-s

Teavituste rakendamiseks MCP-s peate seadistama nii serveri kui kliendi poole, et töödelda reaalajas uuendusi. See võimaldab teie rakendusel pakkuda kasutajatele viivitamatut tagasisidet pikkade toimingute jooksul.

### Serveripoolne: teavituste saatmine

Alustame serveripoolsest. MCP-s määratlete tööriistad, mis saavad saata teavitusi päringute töötlemise ajal. Server kasutab konteksti objekti (tavaliselt `ctx`), et saata sõnumeid kliendile.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Eelnevas näites saadab tööriist `process_files` kliendile kolm teavitust iga faili töötlemisel. Metoodikat `ctx.info()` kasutatakse informatiivsete sõnumite saatmiseks.

Lisaks veenduge, et teie server kasutab voogedastuslikku transporti (näiteks `streamable-http`) ja teie klient rakendab sõnumikäitlejat teavituste töötlemiseks. Siin on, kuidas seadistada server, et kasutada `streamable-http` transporti:

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

Selles .NET näites on tööriist `ProcessFiles` märgistatud atribuudi `Tool` abil ja saadab kliendile kolm teavitust iga faili töötlemisel. `ctx.Info()` meetodiga saadetakse informatiivseid sõnumeid.

Teavituste lubamiseks oma .NET MCP serveris veenduge, et kasutate voogedastuslikku transporti:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Kliendipoolne: teavituste vastuvõtmine

Klient peab rakendama sõnumikäitleja teavituste töötlemiseks ja kuvamiseks nende saabumisel.

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

Eelnevas koodis kontrollib funktsioon `message_handler`, kas saabuv sõnum on teavitus. Kui on, siis prindib selle välja, vastasel korral töötleb seda kui tavapärast serveri sõnumit. Samuti märgake, kuidas `ClientSession` initsialiseeritakse koos `message_handler`-iga saabuvate teavituste töötlemiseks.

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

Selles .NET näites kontrollib funktsioon `MessageHandler`, kas saabuv sõnum on teavitus. Kui on, siis prindib selle välja, vastasel korral töötleb seda tavapärase serveri sõnumina. `ClientSession` initsialiseeritakse sõnumikäitlejaga läbi `ClientSessionOptions`.

Teavituste lubamiseks veenduge, et teie server kasutab voogedastuslikku transporti (nt `streamable-http`) ja klient rakendab sõnumikäitlejat teavituste vastuvõtmiseks.

## Edenemisuuendused & stsenaariumid

Selles jaotises selgitatakse edenemisuuenduste mõistet MCP-s, miks need on olulised ja kuidas neid implementeerida kasutades voogedastatavat HTTP-d. Samuti on seal praktiline ülesanne teie mõistmise kinnistamiseks.

Edenemisuuendused on reaalajas sõnumid, mis server saadab kliendile pikaajaliste toimingute jooksul. Selle asemel, et oodata kogu protsessi lõpulejõudmist, hoiab server klienti kursis hetkeolukorraga. See parandab läbipaistvust, kasutajakogemust ja lihtsustab silumist.

**Näide:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Miks kasutada edenemisuuendusi?

Edenemisuuendused on olulised mitmel põhjusel:

- **Parem kasutajakogemus:** Kasutajad näevad uuendusi töö edenemise käigus, mitte ainult lõpus.
- **Reaalajas tagasiside:** Klient saab kuvada edenemisribasid või logisid, muutes rakenduse tajutavalt reageerivaks.
- **Lihtsam silumine ja jälgimine:** Arendajad ja kasutajad näevad, kus protsess võib aeglustuda või kinni jääda.

### Kuidas edenemisuuendusi rakendada

Selline on edenemisuuenduste rakendamise viis MCP-s:

- **Serveripoolselt:** Kasutage `ctx.info()` või `ctx.log()`, et saata teavitusi iga töödeldava üksuse kohta. See saadab sõnumi kliendile enne lõpptulemust.
- **Kliendipoolselt:** Rakendage sõnumikäitleja, mis kuulab teavitusi ja kuvab neid pärast saabumist. Käitleja eristab teavitusi ja lõpptulemust.

**Serverinäide:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Kliendinäide:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Turvaküsimused

MCP serverite HTTP-põhiste transpordide rakendamisel muutub turvalisus kriitiliseks teemaks, mis nõuab hoolikat tähelepanu mitmete ründevektorite ja kaitsmehhanismide vastu.

### Ülevaade

Turvalisus on oluline MCP serverite HTTP kaudu kättesaadavaks tegemisel. Voogedastatav HTTP avab uusi ründevektoreid ja nõuab hoolikat konfigureerimist.

### Olulised punktid
- **Päritolu päise valideerimine**: Alati valideeri `Origin` päist, et vältida DNS-i taaskasutusrünnakuid.
- **Localhosti sidumine**: Kohaliku arenduse jaoks seo serverid `localhost`-iga, et vältida nende avalikku internetti avamist.
- **Autentimine**: Loo tootmiskeskkonna juurutusteks autentimine (näiteks API võtmed, OAuth).
- **CORS**: Sea sisse Cross-Origin Resource Sharing (CORS) poliitikad juurdepääsu piiramiseks.
- **HTTPS**: Kasuta tootmises HTTPS-i, et liiklust krüptida.

### Head tavad

- Ära kunagi usalda saabuvate päringute valideerimisteta.
- Logi ja jälgi kõiki juurdepääse ja vigu.
- Uuenda regulaarselt sõltuvusi, et parandada turvavigu.

### Väljakutsed

- Turvalisuse ja arendamise lihtsuse tasakaalustamine
- Ühilduvuse tagamine erinevate kliendikeskkondadega

## Üleminek SSE-st Streamable HTTP-le

Rakenduste jaoks, mis hetkel kasutavad Server-Sent Events (SSE), annab üleminek Streamable HTTP-le täiustatud võimalused ja parema pikaajalise jätkusuutlikkuse MCP lahendustele.

### Miks uuendada?

On kaks mõjuvat põhjust SSE-st Streamable HTTP-le üleminekuks:

- Streamable HTTP pakub paremat skaleeritavust, ühilduvust ja rikkalikumat teavitustuge kui SSE.
- See on soovitatud transport uusimate MCP rakenduste jaoks.

### Migratsiooni sammud

Siin on, kuidas sa saad oma MCP rakendustes SSE-st Streamable HTTP-le üle minna:

- **Uuenda serveri koodi**, et kasutada `transport="streamable-http"` `mcp.run()`-is.
- **Uuenda kliendi koodi**, kasutades SSE kliendi asemel `streamablehttp_client`-i.
- **Rakenda sõnumikäitleja** kliendis, et töödelda teavitusi.
- **Testi ühilduvust** olemasolevate tööriistade ja töövoogudega.

### Ühilduvuse säilitamine

Soovitatav on säilitada ühilduvus olemasolevate SSE klientidega migratsiooni ajal. Mõned strateegiad:

- Võid toetada nii SSE-d kui ka Streamable HTTP-d, käivitades mõlemad transpordid erinevatel lõpp-punktidel.
- Migreeri kliente järk-järgult uuele transpordile.

### Väljakutsed

Tagada tuleb järgmiste probleemide lahendamine migratsiooni ajal:

- Kõigi klientide uuendamine
- Teavituste edastamise erinevuste käsitlemine

## Turvalisuse kaalutlused

Turvalisus peab olema kõrgeim prioriteet iga serveri juurutamisel, eriti HTTP-põhiste transpordide puhul nagu Streamable HTTP MCP-s.

MCP serverite juurutamisel HTTP-põhiste transpordidega muutub turvalisus ülitähtsaks küsimuseks, mis nõuab põhjalikku tähelepanu erinevatele rünnete vektoritele ja kaitsemehhanismidele.

### Ülevaade

Turvalisus on hädavajalik, kui MCP servereid eksponeerida HTTP kaudu. Streamable HTTP toob kaasa uued rünnetekohad ja nõuab hoolikat seadistust.

Siin on mõned peamised turvalisuse kaalutlused:

- **Päritolu päise valideerimine**: Alati valideeri `Origin` päist, et vältida DNS-i taaskasutusrünnakuid.
- **Localhosti sidumine**: Kohaliku arenduse jaoks seo serverid `localhost`-iga, et vältida nende avalikku internetti avamist.
- **Autentimine**: Loo tootmiskeskkonna juurutusteks autentimine (näiteks API võtmed, OAuth).
- **CORS**: Sea sisse Cross-Origin Resource Sharing (CORS) poliitikad juurdepääsu piiramiseks.
- **HTTPS**: Kasuta tootmises HTTPS-i, et liiklust krüptida.

### Head tavad

Lisaks on siin mõned head tavad MCP voogesitusserveri turvalise juurutamise tagamiseks:

- Ära kunagi usalda saabuvate päringute valideerimisteta.
- Logi ja jälgi kõiki juurdepääse ja vigu.
- Uuenda regulaarselt sõltuvusi, et parandada turvavigu.

### Väljakutsed

Turvaelementide juurutamisel MCP voogedastusserverites tuleb ette järgmisi väljakutseid:

- Turvalisuse ja arendamise lihtsuse tasakaalustamine
- Ühilduvuse tagamine erinevate kliendikeskkondadega

### Ülesanne: Ehita oma voogedastav MCP rakendus

**Stsenaarium:**
Ehita MCP server ja klient, kus server töötleb esemete (nt failide või dokumentide) nimekirja ja saadab teavituse iga töödeldud üksuse kohta. Klient kuvab iga saabuvat teavitust reaalajas.

**Sammud:**

1. Loo serveritööriist, mis töötleb nimekirja ja saadab teavitusi iga üksuse kohta.
2. Loo klient sõnumikäitlejaga, mis kuvab teavitusi reaalajas.
3. Testi oma lahendust, käivitades nii serveri kui ka kliendi, ning jälgi teavitusi.

[Lahendus](./solution/README.md)

## Täiendav lugemine ja mis edasi?

Järgmiste sammude ja põhjalikuma MCP voogedastuse tundmaõppimise abi saamiseks pakub see sektsioon lisamaterjale ja soovitatud teemasid keerukamate rakenduste ehitamiseks.

### Täiendav lugemine

- [Microsoft: Tutvustus HTTP voogedastusele](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ASP.NET Core’s](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Voogedastuse päringud](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Mis edasi?

- Proovi ehitada keerukamaid MCP tööriistu, mis kasutavad voogedastust reaalajas analüütika, jutuvestluse või koostöötoimetamise jaoks.
- Uuri MCP voogedastuse integreerimist frontend raamistikudega (React, Vue jne) elavaks liidese uuendamiseks.
- Järgmine: [AI tööriistakomplekti kasutamine VSCode’is](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->