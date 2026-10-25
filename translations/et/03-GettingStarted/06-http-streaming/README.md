# HTTPS-voogesitus Model Context Protocoli (MCP)

See peatükk annab põhjaliku juhendi, kuidas rakendada turvalist, skaleeruvat ja reaalajas toimivat voogesitust Model Context Protocoli (MCP) kaudu, kasutades HTTPS-i. See käsitleb voogesituse motivatsiooni, saadaolevaid transpordimehhanisme, kuidas MCP-s rakendada Streamable HTTP-d, turvalisuse parimaid tavasid, üleminekut SSE-lt ning praktilisi juhiseid oma voogesituse MCP-rakenduste ehitamiseks. 

> [!WARNING]
> Selle õppetunni rakenduse näited on suunatud **MCP Specification
> `2025-11-25`** ja demonstreerivad pärandilist `initialize` handshake,
> `Mcp-Session-Id`, GET sündmuste voog ja taaskäivitatavuse mudel. MCP `2026-07-28`
> eemaldab need funktsioonid. Praegused Streamable HTTP päringud on iseseisvad
> POST päringud koos `MCP-Protocol-Version` ja `Mcp-Method` päistega, pluss
> `Mcp-Name` kui vajalik. Vaata
> [Mis MCP-s on muutunud: 2026-07-28 spetsifikatsioon](../../01-CoreConcepts/mcp-2026-07-28.md)
> enne nende näidete kasutamist uues rakenduses.

## Transpordimehhanismid ja voogesitus MCP-s

See jaotis uurib MCP-s saadaolevaid erinevaid transpordimehhanisme ja nende rolli voogesituse võimaldamisel reaalajas suhtluseks klientide ja serverite vahel.

### Mis on transpordimehhanism?

Transpordimehhanism määratleb, kuidas andmeid kliendi ja serveri vahel vahetatakse. MCP toetab mitut transporditüüpi, mis sobivad erinevatesse keskkondadesse ja nõuetesse:

- **stdio**: Standardne sisend/väljund, sobib kohalikeks ja CLI-põhisteks tööriistadeks. Lihtne, kuid ei sobi veebiks ega pilvekeskkondadeks.
- **HTTP+SSE**: Pärandiline kaugtransport, deprekeeritud MCP `2025-03-26`
    ja asendatud Streamable HTTP-ga. Ära kasuta seda uutes rakendustes.
- **Streamable HTTP**: Moodne HTTP-põhine voogesitustransport, mis toetab teavitusi ja paremat skaleeritavust. Soovitatav enamikuks tootmis- ja pilveolukordadeks.

### Comparison Table

Vaata allolevat võrdlustabelit, et mõista nende transpordimehhanismide erinevusi:

| Transport | Staatus | Teavitused | Tavapärane kasutus |
|---|---|---|---|
| stdio | Praegune | Jah | Kohalikud alamprotsessid |
| HTTP+SSE | Vananenud | Jah | Pärandilised kaugrakendused |
| Streamable HTTP | Praegune | Jah | Kaug- ja pilveserverid |

> **Vihje:** Õige transpordi valik mõjutab jõudlust, skaleeritavust ja kasutajakogemust. **Streamable HTTP** on soovitatav kaasaegsete, skaleeritavate ja pilvevalmis rakenduste jaoks.

Standardtransporditüübid on stdio ja Streamable HTTP. HTTP+SSE esineb
vaid vanemates näidetes.

## Voogesitus: kontseptsioonid ja motivatsioon

Voogesituse põhimõistete ja motivatsiooni mõistmine on oluline tõhusa reaalajas suhtlussüsteemi rakendamiseks.

**Voogesitus** on võrguprogrammeerimise tehnika, mis võimaldab andmete saatmist ja vastuvõtmist väikeste, hallatavate tükkidena või sündmuste jadas, selle asemel et oodata kogu vastuse valmisolekut. See on eriti kasulik:

- Suured failid või andmekogumid.
- Reaalajas uuendused (nt vestlus, edenemisribad).
- Pikaajalised arvutused, kus soovite kasutajat kursis hoida.

Siin on peamised punktid, mida voogesituse kohta teada:

- Andmed edastatakse järk-järgult, mitte kõik korraga.
- Klient saab andmeid töödelda kohe, kui need saabuvad.
- Vähendab tajutavat latentsust ja parandab kasutajakogemust.

### Miks kasutada voogesitust?

Voogesituse kasutamise põhjused on järgmised:

- Kasutajad saavad tagasisidet koheselt, mitte ainult lõpus
- Võimaldab reaalajas rakendusi ja reageerivaid kasutajaliideseid
- Võrgu- ja arvutusressursside tõhusam kasutamine

### Lihtne näide: HTTP-voogesituse server ja klient

Siin on lihtne näide sellest, kuidas voogesitust saab rakendada:

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

See näide näitab serverit, mis saadab kliendile sõnumite seeria kohe, kui need saadaval on, selle asemel et oodata kõigi sõnumite valmisolekut.

**Kuidas see töötab:**

- Server annab iga sõnumi edasi kohe, kui see valmis on.
- Klient võtab vastu ja väljastab iga osa, kui see saabub.

**Nõuded:**

- Server peab kasutama voogesituse vastust (nt `StreamingResponse` FastAPI-s).
- Klient peab vastust töötlema voona (`stream=True` requests'is).
- Content-Type on tavaliselt `text/event-stream` või `application/octet-stream`.

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

**Java implementatsiooni märkused:**

- Kasutab Spring Booti reaktiivset virna koos `Flux` voogesituseks
- `ServerSentEvent` pakub struktureeritud sündmuste voogesitust koos sündmustüüpidega
- `WebClient` koos `bodyToFlux()` võimaldab reaktiivset voogude tarbimist
- `delayElements()` simuleerib sündmustevahelist töötlemisaega
- Sündmustel võivad olla tüübid (`info`, `result`) et klient saaks neid paremini töödelda

### Võrdlus: klassikaline voogesitus vs MCP-voogesitus

Erinevused selles, kuidas voogesitus toimib 'klassikaliselt' võrreldes MCP-iga, on kujutatud järgmiselt:

| Omadus                | Klassikaline HTTP-voogesitus         | MCP-voogesitus (teavitused)      |
|------------------------|-------------------------------|-------------------------------------|
| Peamine vastus          | Tükeldatud                       | Üksik, lõpus                      |
| Edenemise uuendused       | Saadetakse andmetükkidena           | Saadetakse teavitustena               |
| Kliendi nõuded    | Peab töötlema voogu           | Peab rakendama sõnumikäsitlejat      |
| Kasutusjuhtum               | Suured failid, AI tokenite vood | Edenemine, logid, reaalajas tagasiside  |

### Olulised erinevused

Peale selle, siin on mõned peamised erinevused:

- **Kommunikatsioonimuster:**
  - Klassikaline HTTP-voogesitus: kasutab lihtsat tükeldatud ülekande kodeerimist andmete saatmiseks tükkidena
  - MCP-voogesitus: kasutab struktureeritud teavitussüsteemi koos JSON-RPC protokolliga

- **Sõnumi formaat:**
  - Klassikaline HTTP: lihttekstist tükid reavahetustega
  - MCP: Struktureeritud LoggingMessageNotification-objektid metaandmetega

- **Kliendi rakendus:**
  - Klassikaline HTTP: Lihtne klient, mis töötleb voogesituse vastuseid
  - MCP: Täiustatud klient, millel on sõnumikäsitleja erinevat tüüpi sõnumite töötlemiseks

- **Edenemise uuendused:**
  - Klassikaline HTTP: edenemine on osa peamise vastuse voost
  - MCP: Edenemist saadetakse eraldi teavitussõnumitena, samas kui peamine vastus jõuab lõpus

### Soovitused

Siin on mõned soovitused klassikalise voogesituse (nagu ülal näidatud otspunkt, kasutades `/stream`) implementeerimise ja MCP kaudu voogesituse valimise kohta.

- **Lihtsate voogesituse vajaduste puhul:** Klassikaline HTTP-voogesitus on lihtsam rakendada ja piisav põhiliste voogesituse vajaduste jaoks.

- **Komplekssete, interaktiivsete rakenduste jaoks:** MCP-voogesitus pakub struktureeritumat lähenemist rikkaliku metaandmete ja teavituste ning lõplike tulemuste eraldamisega.

- **AI-rakenduste jaoks:** MCP teavitussüsteem on eriti kasulik pikaajaliste AI-tööde puhul, kus soovite kasutajaid edenemisest informeerida.

## Voogesitus MCP-s

Nii et olete seni näinud mõningaid soovitusi ja võrdlusi klassikalise voogesituse ja MCP-voogesituse erinevuste kohta. Vaatame üksikasjalikult, kuidas saate MCP-is voogesitust ära kasutada.

MCP raamistikus voogesituse toimimise mõistmine on oluline reageerivate rakenduste ehitamiseks, mis annavad reaalajas tagasisidet kasutajatele pikaajaliste toimingute ajal.

MCP-s ei seisne voogesitus peamise vastuse tükeldamises, vaid klienti **teavituste** saatmises tööriista päringu töötlemise ajal. Need teavitused võivad sisaldada edenemise uuendusi, logisid või muid sündmusi.

### Kuidas see töötab

Peamine tulemus saadetakse ikkagi ühe vastusena. Siiski võidakse teavitusi saata eraldiseisvate sõnumitena töötlemise ajal ning sellega uuendada klienti reaalajas. Klient peab suutma neid teavitusi töödelda ja kuvada.

### Valiklik harjutus: ühendumine majutatud MCP-serveriga

Samuti saab kasutada Streamable HTTP-d ilma kohaliku serveri käivitamiseta. See näide
ühendub [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
avastab selle tööriistad ja otsib avalikku MCP-dokumentatsiooni, kasutades sama
Python SDK-d nagu [kohalik klient](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Paralleli anonüümne otspunkt ei nõua kontot ega API-võtit. Tasuta juurdepääs on
kiirusepiiranguga. Selle skripti käivitamine saadab otsingupäringud, eesmärgi ja
juhusliku sessiooni identifikaatori Parallelile. Teenus pakub ka `web_fetch`,
mis edastab taotletud URL-id ja kõik esitatud kontekstid Parallelile. Kasuta avalikku
teavet selle harjutuse jaoks; vaata selle [tingimusi](https://parallel.ai/customer-terms)
ja [privaatsuspoliitikat](https://parallel.ai/privacy-policy).

Python 3.10 või uuema ning aktiveeritud virtuaalkeskkonna olemasolul paigalda SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Salvesta see kui `hosted_search.py` ja käivita `python hosted_search.py`:

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

Eeldatavasti hõlmab avastamine `web_search` ja `web_fetch`, millele järgneb otsing
vastus, mis sisaldab allika URL-e ja lõike. Tulemused võivad erineda või olla tühjad.
Skript kontrollib `isError`, sest tööriist võib ebaõnnestuda isegi siis, kui HTTP-päring
õnnestub. Kui juurdepääs on kiirusepiiratud, oota enne uuesti proovimist. Kasuta sama
`session_id`, kui laiendad skripti seotud otsingu- või toomispäringutega.

Streamable HTTP võimaldab nii JSON- kui ka SSE-vastuseid; see server võib tagastada
täieliku JSON-tulemuse ilma edenemise teavitusteta. SDK käsitleb transporti.
Jätka alloleva kohaliku näitega, et õppida teavituste kohta.
See valikuline skript teeb ühe ekspliciitse otsingu ja sulgeb ühenduse, kui
see lõpeb. Kui hiljem eksponeerite neid tööriistu agendile, võib agent need tööle kutsuda
oma töö käigus; käsitle leitud veebitekste mitteusaldusväärse andmena.

## Mis on teavitus?

Ütlesime "Notification" — mida see MCP kontekstis tähendab?

Teavitus on JSON-RPC sõnum, millel puudub `id` ja mis ei
saa vastust. MCP kasutab teavitusi edenemise, tühistamise ja
muude ühesuunaliste sündmuste jaoks.

MCP `2025-11-25` puhul saadab klient `notifications/initialized` pärast
initsialiseerimiskäepigistust. MCP `2026-07-28` ei sisalda initsialiseerimiskäepigistust, seega
see teavitus on pärandkäitumine.

Teavitus näeb JSON-sõnumina välja järgmiselt:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Logimine on üks funktsioon, mis kasutab teavitusi;
teavitused ise on üldine JSON-RPC sõnumitüüp.

> **Deprekeeritud MCP `2026-07-28`:** logimisfunktsioon jääb kättesaadavaks
> ühilduvuse tagamiseks, kuid on kõrvaldamisele sobilik esimeses spetsifikatsiooni
> revisjonis, mis avaldatakse 28. juulil 2027 või hilisemal kuupäeval. Uued rakendused peaksid kasutama
> `stderr` koos stdio või OpenTelemetry'ga struktureeritud jälgitavuse jaoks.

Pärandilise `2025-11-25` rakenduse puhul lubab server logimise
võimaluse järgmiselt:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Sõltuvalt kasutatavast SDK-st võib logimine olla vaikimisi lubatud või peate selle serveri konfiguratsioonis selgesõnaliselt lubama.

On erinevat tüüpi teavitusi:

| Tase     | Kirjeldus                    | Näidis kasutusjuhtum                |
|-----------|-------------------------------|---------------------------------|
| debug     | Üksikasjalik silumisinfo | Funktsiooni sisenemis-/väljumispunktid      |
| info      | Üldised informatiivsed sõnumid | Operatsiooni edenemise uuendused      |
| notice    | Tavalised, kuid märkimisväärsed sündmused  | Konfiguratsiooni muudatused           |
| warning   | Hoiatusolukorrad             | Aegunud funktsioonide kasutus        |
| error     | Veaolukorrad               | Operatsiooni ebaõnnestumised              |
| critical  | Kriitilised olukorrad            | Süsteemi komponentide rikked       |
| alert     | Peab viivitamatult tegutsema | Andmete korruptsiooni tuvastamine      |
| emergency | Süsteem on kasutuskõlbmatu             | Täielik süsteemi rike         |

## Teavituste rakendamine MCP-s

Teavituste rakendamiseks MCP-s peate seadistama nii serveri kui kliendi poole, et töödelda reaalajas uuendusi. See võimaldab teie rakendusel anda kasutajatele kohest tagasisidet pikaajaliste toimingute ajal.

### Serveripool: teavituste saatmine

Alustame serveripoolest. MCP-s määratlete tööriistad, mis võivad päringu töötlemise ajal saata teavitusi. Server kasutab konteksti objekti (tavaliselt `ctx`), et saata sõnumeid kliendile.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Eelnevas näites saadab `process_files` tööriist kliendile kolm teavitust iga faili töötlemisel. Informatiivsete sõnumite saatmiseks kasutatakse meetodit `ctx.info()`.

Lisaks, teavituste võimaldamiseks veenduge, et teie server kasutab voogedastuslikku transporti (näiteks `streamable-http`) ja et teie klient implementeerib sõnumikäsitleja teavituste töötlemiseks. Siin on, kuidas server seadistada kasutama `streamable-http` transporti:

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

Selles .NET näites on `ProcessFiles` tööriist dekoreeritud atribuudiga `Tool` ning saadab kliendile kolm teavitust iga faili töötlemisel. Informatiivsete sõnumite saatmiseks kasutatakse meetodit `ctx.Info()`.

Teavituste lubamiseks oma .NET MCP-serveris veenduge, et kasutate voogedastuslikku transporti:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Kliendipool: teavituste vastuvõtmine

Klient peab implementeerima sõnumikäsitleja teavituste töötlemiseks ja kuvamiseks nende saabumisel.

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

Eelnevas koodis kontrollib funktsioon `message_handler`, kas sissetulev sõnum on teavitus. Kui on, siis kuvab ta teavituse; vastasel juhul töötleb seda tavalise serverisõnumina. Pange tähele ka, kuidas `ClientSession` on initsialiseeritud `message_handler`-ga, et käsitleda sissetulevaid teavitusi.

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

Selles .NET-i näites kontrollib funktsioon `MessageHandler`, kas sissetulev sõnum on teavitus. Kui on, siis kuvab ta teavituse; vastasel juhul töötleb seda tavalise serverisõnumina. `ClientSession` initsialiseeritakse sõnumikäitlejaga `ClientSessionOptions` kaudu.

Teavituste lubamiseks veenduge, et teie server kasutab voogedastustarnet (näiteks `streamable-http`) ja et teie klient rakendab sõnumikäitleja teavituste töötlemiseks.

## Edenemise teavitused ja stsenaariumid

Selles jaotises selgitatakse MCP-i edenemise teavituste mõistet, miks need on olulised ja kuidas neid rakendada kasutades Streamable HTTP-d. Leiate ka praktilise ülesande oma arusaama kinnistamiseks.

Edenemise teavitused on reaalajas sõnumid, mida server saadab kliendile pikkade toimingute käigus. Selle asemel, et oodata kogu protsessi lõppemist, hoiab server klienti kursis praeguse olekuga. See parandab läbipaistvust, kasutajakogemust ja teeb tõrkeotsingu lihtsamaks.

**Näide:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Miks kasutada edenemise teavitusi?

Edenemise teavitused on olulised mitmel põhjusel:

- **Parem kasutajakogemus:** Kasutajad näevad uuendusi töö edenemise jooksul, mitte ainult lõpus.
- **Reaalajas tagasiside:** Kliendid saavad kuvada edenemisriba või logisid, mis muudab rakenduse reageerivamaks.
- **Lihtsam tõrkeotsing ja jälgimine:** Arendajad ja kasutajad näevad, kus protsess võib olla aeglane või kinni jäänud.

### Kuidas rakendada edenemise teavitusi

Siin on, kuidas saate MCP-is rakendada edenemise teavitusi:

- **Serveris:** Kasutage `ctx.info()` või `ctx.log()`, et saata teavitusi iga üksuse töötlemisel. See saadab sõnumi kliendile enne peamise tulemuse valmimist.
- **Klientidel:** Rakendage sõnumikäitleja, mis kuulab ja kuvab saabuvad teavitused. See käitleja eristab teavitusi ja lõplikku tulemust.

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

## Turvakaalutlused

Turvalisus peaks olema esmatähtis iga serveri juurutamisel, eriti kui kasutatakse HTTP-põhiseid transpordimeetodeid nagu Streamable HTTP MCP-is.

MCP-serverite rakendamisel HTTP-põhiste transportidega muutub turvalisus esmatähtsaks probleemiks, mis nõuab hoolikat tähelepanu mitmetele ründevektoritele ja kaitsemehhanismidele.

### Ülevaade

Kui MCP-serverid avalikustatakse üle HTTP, on turvalisus ülioluline. Streamable HTTP lisab uusi ründepindu ja nõuab hoolikat konfigureerimist.

Siin on mõned olulised turvakaalutlused:

- **Origin päise valideerimine**: Alati valideerige `Origin` päis, et vältida DNS-i ümbersidumisrünnakuid.
- **Localhosti sidumine**: Kohalikuks arendamiseks siduge serverid aadressiga `localhost`, et vältida nende avalikuks internetis muutumist.
- **Autentimine**: Tootmiskeskkonnas rakendage autentimine (nt API-võtmed, OAuth).
- **CORS**: Konfigureerige Cross-Origin Resource Sharing (CORS) poliitikad juurdepääsu piiramiseks.
- **HTTPS**: Kasutage tootmises HTTPS-i, et liiklust krüpteerida.

### Parimad praktikad

Lisaks on siin mõned parimad praktikad, mida järgida MCP-voogesitusserveri turvalisuse rakendamisel:

- Ärge kunagi usaldage sissetulevaid päringuid ilma valideerimiseta.
- Logige ja jälgige kogu juurdepääsu ning vigu.
- Uuendage sõltuvusi regulaarselt, et parandada turvaauke.

### Väljakutsed

MCP-voogesitusserverite turvalisuse rakendamisel seisate silmitsi mõningate väljakutsetega:

- Turvalisuse ja arendamise lihtsuse tasakaalustamine
- Ühilduvuse tagamine erinevate kliendikeskkondadega


## Üleminek SSE-lt Streamable HTTP-ile

Rakenduste puhul, mis praegu kasutavad Server-Sent Events (SSE), pakub migratsioon Streamable HTTP-le täiendavaid võimalusi ja paremat pikaajalist jätkusuutlikkust teie MCP-i lahendustele.

### Miks uuendada?

SSE-lt Streamable HTTP-ile üleminemiseks on kaks veenvat põhjust:

- Streamable HTTP pakub paremat skaleeritavust, ühilduvust ja rikkalikumat teavitustuge kui SSE.
- See on soovitatav transport uutele MCP-rakendustele.

### Migratsiooni sammud

Siin on, kuidas saate oma MCP-rakendustes üle minna SSE-lt Streamable HTTP-ile:

- **Uuendage serveri koodi**, et kasutada `transport="streamable-http"`-i `mcp.run()`-s.
- **Uuendage kliendi koodi**, et kasutada `streamablehttp_client` SSE-kliendi asemel.
- **Rakendage kliendi poolel sõnumikäsitleja** teatiste töötlemiseks.
- **Testige ühilduvust** olemasolevate tööriistade ja töövoogudega.

### Ühilduvuse säilitamine

Soovitatav on migratsiooni käigus säilitada ühilduvus olemasolevate SSE-kliendidega. Siin on mõned strateegiad:

- Saate toetada nii SSE-d kui Streamable HTTP-d, käivitades mõlemad transpordid erinevatel lõpp-punktidel.
- Migreerige kliendid järk-järgult uuele transpordile.

### Väljakutsed

Veenduge, et käsitlete migratsiooni ajal järgmisi väljakutseid:

- Kõigi klientide uuendamise tagamine
- Teavituste kohaletoimetamise erinevuste käsitlemine

### Ülesanne: Ehita oma voogedastusega MCP-rakendus

**Stsenaarium:**
Ehita MCP-server ja klient, kus server töötleb üksuste loendit (nt faile või dokumente) ja saadab teate iga töödeldud üksuse kohta. Klient peaks kuvama iga saabuvat teadet.

**Sammud:**

1. Rakenda serveritööriist, mis töötleb loendit ja saadab teateid iga üksuse kohta.
2. Rakenda klient, millel on sõnumikäitleja, et kuvada teateid reaalajas.
3. Testi oma lahendust, käivitades nii serveri kui kliendi, ja jälgi teateid.

[Lahendus](./solution/README.md)

## Lisalugemine ja mis edasi?

Et jätkata oma teekonda MCP-voogedastuse alal ja laiendada oma teadmisi, annab see jaotis täiendavaid ressursse ja soovitatud järgmisi samme keerukamate rakenduste ehitamiseks.

### Lisalugemine

- [Microsoft: Sissejuhatus HTTP-voogedastusse](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Serveri saadetud sündmused (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS ASP.NET Core'is](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: voogedastuse päringud](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Mis järgmiseks?

- Proovi luua arenenumaid MCP-tööriistu, mis kasutavad voogedastust reaalaja analüütika, vestluse või ühise redigeerimise jaoks.
- Uuri, kuidas integreerida MCP-voogedastus front-end raamistikesse (React, Vue jne) reaalajas kasutajaliidese värskenduste jaoks.
- Järgmiseks: [Microsoft Foundry tööriistakomplekti kasutamine Visual Studio Code'i jaoks](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->