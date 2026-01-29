# Utiririshaji wa HTTPS na Itifaki ya Model Context (MCP)

Sura hii inatoa mwongozo wa kina wa kutekeleza utiririshaji salama, unaoweza kupanuka, na wa wakati halisi kwa kutumia Itifaki ya Model Context (MCP) kupitia HTTPS. Inashughulikia motisha ya utiririshaji, mifumo ya usafirishaji inayopatikana, jinsi ya kutekeleza HTTP inayoweza kutiririka katika MCP, mbinu bora za usalama, uhamishaji kutoka SSE, na mwongozo wa vitendo wa kujenga programu zako za utiririshaji za MCP.

## Mifumo ya Usafirishaji na Utiririshaji katika MCP

Sehemu hii inachunguza mifumo tofauti ya usafirishaji inayopatikana katika MCP na jukumu lake katika kuwezesha uwezo wa utiririshaji kwa mawasiliano ya wakati halisi kati ya wateja na seva.

### Mfumo wa Usafirishaji ni Nini?

Mfumo wa usafirishaji hufafanua jinsi data inavyobadilishwa kati ya mteja na seva. MCP inaunga mkono aina nyingi za usafirishaji ili kukidhi mazingira na mahitaji tofauti:

- **stdio**: Ingizo/utoaji wa kawaida, inayofaa kwa zana za ndani na CLI. Rahisi lakini haifai kwa wavuti au wingu.
- **SSE (Matukio Yanayotumwa na Seva)**: Inaruhusu seva kusukuma masasisho ya wakati halisi kwa wateja kupitia HTTP. Nzuri kwa UI za wavuti, lakini ina mipaka katika upanuzi na kubadilika.
- **HTTP inayoweza kutiririka**: Usafirishaji wa kisasa unaotegemea HTTP, unaounga mkono arifa na upanuzi bora. Inapendekezwa kwa hali nyingi za uzalishaji na wingu.

### Jedwali la Ulinganisho

Angalia jedwali la ulinganisho hapa chini ili kuelewa tofauti kati ya mifumo hii ya usafirishaji:

| Usafirishaji       | Masasisho ya Wakati Halisi | Utiririshaji | Upanuzi | Matumizi                  |
|--------------------|---------------------------|--------------|---------|--------------------------|
| stdio              | Hapana                    | Hapana       | Chini    | Zana za CLI za ndani     |
| SSE                | Ndio                      | Ndio         | Kati    | Wavuti, masasisho ya wakati halisi |
| HTTP inayoweza kutiririka | Ndio              | Ndio         | Juu     | Wingu, wateja wengi      |

> **Kidokezo:** Kuchagua usafirishaji sahihi kunaathiri utendaji, upanuzi, na uzoefu wa mtumiaji. **HTTP inayoweza kutiririka** inapendekezwa kwa programu za kisasa, zinazoweza kupanuka, na tayari kwa wingu.

Kumbuka mifumo ya usafirishaji stdio na SSE ambayo ulionyeshwa katika sura zilizopita na jinsi HTTP inayoweza kutiririka ndiyo usafirishaji unaoshughulikiwa katika sura hii.

## Utiririshaji: Dhana na Motisha

Kuelewa dhana za msingi na motisha nyuma ya utiririshaji ni muhimu kwa kutekeleza mifumo bora ya mawasiliano ya wakati halisi.

**Utiririshaji** ni mbinu katika programu za mtandao inayoruhusu data kutumwa na kupokelewa kwa vipande vidogo, vinavyoweza kudhibitiwa au kama mfululizo wa matukio, badala ya kusubiri majibu yote kuwa tayari. Hii ni muhimu hasa kwa:

- Faili kubwa au seti za data.
- Masasisho ya wakati halisi (mfano, mazungumzo, upau wa maendeleo).
- Mahesabu ya muda mrefu ambapo unataka kumjulisha mtumiaji.

Hapa kuna unachohitaji kujua kuhusu utiririshaji kwa kiwango cha juu:

- Data inatolewa hatua kwa hatua, si yote mara moja.
- Mteja anaweza kuchakata data inavyowasili.
- Inapunguza ucheleweshaji unaoonekana na kuboresha uzoefu wa mtumiaji.

### Kwa nini utumie utiririshaji?

Sababu za kutumia utiririshaji ni zifuatazo:

- Watumiaji hupata maoni mara moja, si tu mwishoni.
- Inawezesha programu za wakati halisi na UI zinazojibika.
- Matumizi bora ya rasilimali za mtandao na kompyuta.

### Mfano Rahisi: Seva na Mteja wa Utiririshaji wa HTTP

Hapa kuna mfano rahisi wa jinsi utiririshaji unavyoweza kutekelezwa:

#### Python

**Seva (Python, kutumia FastAPI na StreamingResponse):**

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

**Mteja (Python, kutumia requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Mfano huu unaonyesha seva ikituma mfululizo wa ujumbe kwa mteja unavyopatikana, badala ya kusubiri ujumbe wote kuwa tayari.

**Jinsi inavyofanya kazi:**

- Seva inatoa kila ujumbe unavyokuwa tayari.
- Mteja hupokea na kuchapisha kila kipande kinapowasili.

**Mahitaji:**

- Seva lazima itumie majibu ya utiririshaji (mfano, `StreamingResponse` katika FastAPI).
- Mteja lazima uchakate majibu kama mkondo (`stream=True` katika requests).
- Aina ya Maudhui kawaida ni `text/event-stream` au `application/octet-stream`.

#### Java

**Seva (Java, kutumia Spring Boot na Matukio Yanayotumwa na Seva):**

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

**Mteja (Java, kutumia Spring WebFlux WebClient):**

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

**Vidokezo vya Utekelezaji wa Java:**

- Inatumia stack ya reactive ya Spring Boot na `Flux` kwa utiririshaji.
- `ServerSentEvent` hutoa utiririshaji wa matukio yaliyo na muundo na aina za matukio.
- `WebClient` na `bodyToFlux()` inawezesha matumizi ya utiririshaji wa reactive.
- `delayElements()` inasimulia muda wa usindikaji kati ya matukio.
- Matukio yanaweza kuwa na aina (`info`, `result`) kwa usindikaji bora wa mteja.

### Ulinganisho: Utiririshaji wa Kawaida vs Utiririshaji wa MCP

Tofauti kati ya jinsi utiririshaji unavyofanya kazi kwa njia ya "kawaida" dhidi ya jinsi unavyofanya kazi katika MCP zinaweza kuonyeshwa kama ifuatavyo:

| Kipengele              | Utiririshaji wa HTTP wa Kawaida | Utiririshaji wa MCP (Arifa)         |
|------------------------|--------------------------------|-------------------------------------|
| Majibu makuu           | Vipande                      | Moja, mwishoni                     |
| Masasisho ya maendeleo | Yanatumwa kama vipande vya data | Yanatumwa kama arifa               |
| Mahitaji ya mteja      | Lazima uchakate mkondo        | Lazima utekeleze mshughulikiaji wa ujumbe |
| Matumizi               | Faili kubwa, mitiririko ya token za AI | Maendeleo, magogo, maoni ya wakati halisi |

### Tofauti Muhimu Zilizogunduliwa

Zaidi ya hayo, hapa kuna tofauti muhimu:

- **Mfumo wa Mawasiliano:**
  - Utiririshaji wa HTTP wa Kawaida: Hutumia encoding rahisi ya uhamisho wa vipande kutuma data kwa vipande.
  - Utiririshaji wa MCP: Hutumia mfumo wa arifa uliopangwa na itifaki ya JSON-RPC.

- **Muundo wa Ujumbe:**
  - HTTP ya Kawaida: Vipande vya maandishi wazi na mistari mipya.
  - MCP: Vitu vya LoggingMessageNotification vilivyopangwa na metadata.

- **Utekelezaji wa Mteja:**
  - HTTP ya Kawaida: Mteja rahisi anayechakata majibu ya utiririshaji.
  - MCP: Mteja wa kisasa zaidi na mshughulikiaji wa ujumbe kuchakata aina tofauti za ujumbe.

- **Masasisho ya Maendeleo:**
  - HTTP ya Kawaida: Maendeleo ni sehemu ya mkondo wa majibu kuu.
  - MCP: Maendeleo yanatumwa kupitia ujumbe wa arifa tofauti huku majibu makuu yakija mwishoni.

### Mapendekezo

Kuna mambo tunapendekeza linapokuja suala la kuchagua kati ya kutekeleza utiririshaji wa kawaida (kama endpoint tuliyoonyesha hapo juu kwa kutumia `/stream`) dhidi ya kuchagua utiririshaji kupitia MCP.

- **Kwa mahitaji rahisi ya utiririshaji:** Utiririshaji wa HTTP wa kawaida ni rahisi kutekeleza na unatosha kwa mahitaji ya msingi ya utiririshaji.

- **Kwa programu changamano, za maingiliano:** Utiririshaji wa MCP hutoa mbinu iliyopangwa zaidi na metadata tajiri na mgawanyo kati ya arifa na matokeo ya mwisho.

- **Kwa programu za AI:** Mfumo wa arifa wa MCP ni muhimu hasa kwa kazi za AI za muda mrefu ambapo unataka kuwajulisha watumiaji kuhusu maendeleo.

## Utiririshaji katika MCP

Sawa, kwa hivyo umeona mapendekezo na ulinganisho hadi sasa kuhusu tofauti kati ya utiririshaji wa kawaida na utiririshaji katika MCP. Hebu tuingie kwa undani jinsi unavyoweza kutumia utiririshaji katika MCP.

Kuelewa jinsi utiririshaji unavyofanya kazi ndani ya mfumo wa MCP ni muhimu kwa kujenga programu zinazojibika ambazo hutoa maoni ya wakati halisi kwa watumiaji wakati wa operesheni za muda mrefu.

Katika MCP, utiririshaji si kuhusu kutuma majibu makuu kwa vipande, bali ni kuhusu kutuma **arifa** kwa mteja wakati zana inachakata ombi. Arifa hizi zinaweza kujumuisha masasisho ya maendeleo, magogo, au matukio mengine.

### Jinsi inavyofanya kazi

Matokeo makuu bado yanatumwa kama jibu moja. Hata hivyo, arifa zinaweza kutumwa kama ujumbe tofauti wakati wa usindikaji na hivyo kuhusisha mteja kwa wakati halisi. Mteja lazima aweze kushughulikia na kuonyesha arifa hizi.

## Arifa ni Nini?

Tulisema "Arifa", hiyo inamaanisha nini katika muktadha wa MCP?

Arifa ni ujumbe unaotumwa kutoka kwa seva kwenda kwa mteja ili kutoa taarifa kuhusu maendeleo, hali, au matukio mengine wakati wa operesheni ya muda mrefu. Arifa zinaboresha uwazi na uzoefu wa mtumiaji.

Kwa mfano, mteja anapaswa kutuma arifa mara tu mkono wa awali na seva umekamilika.

Arifa inaonekana kama ujumbe wa JSON:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Arifa zinahusiana na mada katika MCP inayojulikana kama ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Ili kupata magogo kufanya kazi, seva inahitaji kuiwezesha kama kipengele/uwezo kama ifuatavyo:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Kulingana na SDK inayotumika, magogo yanaweza kuwa yamewezeshwa kwa chaguo-msingi, au unaweza kuhitaji kuiwezesha waziwazi katika usanidi wa seva yako.

Kuna aina tofauti za arifa:

| Kiwango    | Maelezo                     | Mfano wa Matumizi               |
|------------|-----------------------------|---------------------------------|
| debug      | Taarifa za kina za urekebishaji | Sehemu za kuingia/kutoka za kazi |
| info       | Ujumbe wa taarifa za jumla  | Masasisho ya maendeleo ya operesheni |
| notice     | Matukio ya kawaida lakini muhimu | Mabadiliko ya usanidi           |
| warning    | Hali za onyo                | Matumizi ya kipengele kilichopitwa na wakati |
| error      | Hali za makosa              | Kushindwa kwa operesheni        |
| critical   | Hali muhimu                 | Kushindwa kwa sehemu ya mfumo   |
| alert      | Hatua lazima ichukuliwe mara moja | Kugunduliwa kwa ufisadi wa data |
| emergency  | Mfumo hauwezi kutumika      | Kushindwa kabisa kwa mfumo      |

## Kutekeleza Arifa katika MCP

Ili kutekeleza arifa katika MCP, unahitaji kusanidi pande zote za seva na mteja kushughulikia masasisho ya wakati halisi. Hii inaruhusu programu yako kutoa maoni ya haraka kwa watumiaji wakati wa operesheni za muda mrefu.

### Upande wa Seva: Kutuma Arifa

Hebu tuanze na upande wa seva. Katika MCP, unafafanua zana zinazoweza kutuma arifa wakati wa kuchakata maombi. Seva hutumia kitu cha muktadha (kawaida `ctx`) kutuma ujumbe kwa mteja.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Katika mfano uliotangulia, zana ya `process_files` inatuma arifa tatu kwa mteja inavyosindika kila faili. Njia ya `ctx.info()` inatumika kutuma ujumbe wa taarifa.

Zaidi ya hayo, ili kuwezesha arifa, hakikisha seva yako inatumia usafirishaji wa utiririshaji (kama `streamable-http`) na mteja wako anatekeleza mshughulikiaji wa ujumbe kushughulikia arifa. Hapa kuna jinsi unavyoweza kusanidi seva kutumia usafirishaji wa `streamable-http`:

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

Katika mfano huu wa .NET, zana ya `ProcessFiles` imepambwa na sifa ya `Tool` na inatuma arifa tatu kwa mteja inavyosindika kila faili. Njia ya `ctx.Info()` inatumika kutuma ujumbe wa taarifa.

Ili kuwezesha arifa katika seva yako ya MCP ya .NET, hakikisha unatumia usafirishaji wa utiririshaji:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Upande wa Mteja: Kupokea Arifa

Mteja lazima atekeleze mshughulikiaji wa ujumbe kushughulikia na kuonyesha arifa zinapowasili.

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

Katika msimbo uliotangulia, kazi ya `message_handler` inakagua ikiwa ujumbe unaoingia ni arifa. Ikiwa ni, inachapisha arifa; vinginevyo, inachakata kama ujumbe wa kawaida wa seva. Pia angalia jinsi `ClientSession` imeanzishwa na `message_handler` kushughulikia arifa zinazoingia.

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

Katika mfano huu wa .NET, kazi ya `MessageHandler` inakagua ikiwa ujumbe unaoingia ni arifa. Ikiwa ni, inachapisha arifa; vinginevyo, inachakata kama ujumbe wa kawaida wa seva. `ClientSession` imeanzishwa na mshughulikiaji wa ujumbe kupitia `ClientSessionOptions`.

Ili kuwezesha arifa, hakikisha seva yako inatumia usafirishaji wa utiririshaji (kama `streamable-http`) na mteja wako anatekeleza mshughulikiaji wa ujumbe kushughulikia arifa.

## Arifa za Maendeleo na Matukio

Sehemu hii inaelezea dhana ya arifa za maendeleo katika MCP, kwa nini ni muhimu, na jinsi ya kuzitekeleza kwa kutumia HTTP inayoweza kutiririka. Pia utapata kazi ya vitendo ili kuimarisha uelewa wako.

Arifa za maendeleo ni ujumbe wa wakati halisi unaotumwa kutoka kwa seva kwenda kwa mteja wakati wa operesheni za muda mrefu. Badala ya kusubiri mchakato mzima kumalizika, seva huendelea kumjulisha mteja kuhusu hali ya sasa. Hii inaboresha uwazi, uzoefu wa mtumiaji, na hufanya urekebishaji kuwa rahisi.

**Mfano:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Kwa nini Utumie Arifa za Maendeleo?

Arifa za maendeleo ni muhimu kwa sababu kadhaa:

- **Uzoefu bora wa mtumiaji:** Watumiaji huona masasisho kazi inavyosonga mbele, si tu mwishoni.
- **Maoni ya wakati halisi:** Wateja wanaweza kuonyesha upau wa maendeleo au magogo, na kufanya programu kuhisi kujibika.
- **Urekebishaji na ufuatiliaji rahisi:** Waendelezaji na watumiaji wanaweza kuona wapi mchakato unaweza kuwa polepole au umekwama.

### Jinsi ya Kutekeleza Arifa za Maendeleo

Hapa kuna jinsi unavyoweza kutekeleza arifa za maendeleo katika MCP:

- **Upande wa seva:** Tumia `ctx.info()` au `ctx.log()` kutuma arifa kila kipengee kinaposindika. Hii hutuma ujumbe kwa mteja kabla ya matokeo makuu kuwa tayari.
- **Upande wa mteja:** Tekeleza mshughulikiaji wa ujumbe unaosikiliza na kuonyesha arifa zinapowasili. Mshughulikiaji huyu hutofautisha kati ya arifa na matokeo ya mwisho.

**Mfano wa Seva:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Mfano wa Mteja:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Masuala ya Usalama

Wakati wa kutekeleza seva za MCP na usafirishaji unaotegemea HTTP, usalama unakuwa suala la msingi linalohitaji umakini wa kina kwa njia nyingi za mashambulizi na mifumo ya ulinzi.

### Muhtasari

Usalama ni muhimu wakati wa kufichua seva za MCP kupitia HTTP. HTTP inayoweza kutiririka inaleta nyuso mpya za mashambulizi na inahitaji usanidi wa makini.

### Vidokezo Muhimu

- **Uthibitishaji wa Kichwa cha Origin**: Kagua kichwa cha `Origin` kila wakati ili kuzuia mashambulizi ya DNS rebinding.
- **Kufunga kwa Localhost**: Kwa maendeleo ya ndani, fungia seva kwa `localhost` ili kuepuka kuzifichua kwa mtandao wa umma.
-
Kuna sababu mbili za kuvutia za kuboresha kutoka SSE hadi Streamable HTTP:

- Streamable HTTP inatoa uwezo bora wa kupanuka, utangamano, na msaada wa arifa tajiri zaidi kuliko SSE.
- Ni njia inayopendekezwa kwa programu mpya za MCP.

### Hatua za Kuhama

Hivi ndivyo unavyoweza kuhama kutoka SSE hadi Streamable HTTP katika programu zako za MCP:

- **Sasisha msimbo wa seva** ili kutumia `transport="streamable-http"` katika `mcp.run()`.
- **Sasisha msimbo wa mteja** ili kutumia `streamablehttp_client` badala ya mteja wa SSE.
- **Tekeleza mshughulikiaji wa ujumbe** katika mteja ili kushughulikia arifa.
- **Jaribu utangamano** na zana na mtiririko wa kazi uliopo.

### Kudumisha Utangamano

Inapendekezwa kudumisha utangamano na wateja wa SSE waliopo wakati wa mchakato wa kuhama. Hizi ni baadhi ya mikakati:

- Unaweza kusaidia SSE na Streamable HTTP kwa kuendesha njia zote mbili kwenye viingilio tofauti.
- Hamisha wateja hatua kwa hatua hadi njia mpya.

### Changamoto

Hakikisha unashughulikia changamoto zifuatazo wakati wa kuhama:

- Kuhakikisha wateja wote wamesasishwa
- Kushughulikia tofauti katika utoaji wa arifa

## Masuala ya Usalama

Usalama unapaswa kuwa kipaumbele cha juu unapotekeleza seva yoyote, hasa unapokuwa unatumia njia za HTTP kama Streamable HTTP katika MCP.

Unapotekeleza seva za MCP na njia za HTTP, usalama unakuwa suala muhimu linalohitaji umakini wa kina kwa vishawishi vya mashambulizi na mbinu za ulinzi.

### Muhtasari

Usalama ni muhimu unapofichua seva za MCP kupitia HTTP. Streamable HTTP inaleta nyuso mpya za mashambulizi na inahitaji usanidi wa makini.

Hizi ni baadhi ya masuala muhimu ya usalama:

- **Uthibitishaji wa Kichwa cha Origin**: Daima thibitisha kichwa cha `Origin` ili kuzuia mashambulizi ya DNS rebinding.
- **Kufunga kwa Localhost**: Kwa maendeleo ya ndani, fungia seva kwenye `localhost` ili kuepuka kuzifichua kwenye mtandao wa umma.
- **Uthibitishaji**: Tekeleza uthibitishaji (mfano, funguo za API, OAuth) kwa matumizi ya uzalishaji.
- **CORS**: Sanidi sera za Cross-Origin Resource Sharing (CORS) ili kuzuia ufikiaji.
- **HTTPS**: Tumia HTTPS katika uzalishaji ili kusimba trafiki.

### Mazoea Bora

Zaidi ya hayo, haya ni mazoea bora ya kufuata unapotekeleza usalama katika seva yako ya MCP ya mtiririko:

- Usiamini maombi yanayoingia bila uthibitishaji.
- Rekodi na fuatilia ufikiaji na makosa yote.
- Sasisha mara kwa mara utegemezi ili kuziba udhaifu wa usalama.

### Changamoto

Utakutana na changamoto kadhaa unapotekeleza usalama katika seva za MCP za mtiririko:

- Kuweka usawa kati ya usalama na urahisi wa maendeleo
- Kuhakikisha utangamano na mazingira mbalimbali ya wateja

### Kazi: Jenga Programu Yako ya MCP ya Mtiririko

**Hali:**
Jenga seva na mteja wa MCP ambapo seva inachakata orodha ya vitu (mfano, faili au nyaraka) na kutuma arifa kwa kila kipengee kilichochakatwa. Mteja anapaswa kuonyesha kila arifa inavyowasili.

**Hatua:**

1. Tekeleza zana ya seva inayochakata orodha na kutuma arifa kwa kila kipengee.
2. Tekeleza mteja na mshughulikiaji wa ujumbe ili kuonyesha arifa kwa wakati halisi.
3. Jaribu utekelezaji wako kwa kuendesha seva na mteja, na uangalie arifa.

[Solution](./solution/README.md)

## Kusoma Zaidi & Nini Cha Kufanya Baadaye?

Ili kuendelea na safari yako ya MCP ya mtiririko na kupanua maarifa yako, sehemu hii inatoa rasilimali za ziada na hatua zinazopendekezwa za kujenga programu za hali ya juu zaidi.

### Kusoma Zaidi

- [Microsoft: Utangulizi wa HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS katika ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Nini Cha Kufanya Baadaye?

- Jaribu kujenga zana za MCP za hali ya juu zinazotumia mtiririko kwa uchanganuzi wa wakati halisi, mazungumzo, au uhariri wa pamoja.
- Chunguza kuunganisha MCP ya mtiririko na mifumo ya mbele (React, Vue, nk.) kwa masasisho ya moja kwa moja ya UI.
- Ifuatayo: [Kutumia AI Toolkit kwa VSCode](../07-aitk/README.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma ya tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa maelewano mabaya au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.