# Utoaji wa HTTPS kwa Protokoli ya Muktadha wa Mfano (MCP)

Sura hii inatoa mwongozo wa kina wa kutekeleza uchezeshaji wa salama, unaoweza kupanuka, na wa wakati halisi kwa kutumia Protokoli ya Muktadha wa Mfano (MCP) kwa kutumia HTTPS. Inajumuisha motisha ya uchezeshaji, mifumo ya usafirishaji inayopatikana, jinsi ya kutekeleza HTTP inayoweza kuchezeshwa katika MCP, mbinu bora za usalama, uhamisho kutoka SSE, na mwongozo wa vitendo wa kujenga programu zako za uchezeshaji MCP.

> **Kuangalia mbele:** somo hili linaelezea HTTP Inayoweza Kuchezeshwa chini ya **MCP Specification 2025-11-25**, ambapo kikao kinaanzishwa wakati wa `initialize` na kimefungwa na kichwa cha `Mcp-Session-Id`. Kandidati wa toleo la `2026-07-28` huondoa kabisa mshikamano na kitambulisho cha kikao, na kufanya kila ombi liwe na maelezo kamili yenyewe na liweze kupangwa kwa seva yoyote bila vikao vya malka. Angalia [Mbali na Mabadiliko Katika MCP: Kandidati wa Toleo la 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) kwa maelezo zaidi.

## Mifumo ya Usafirishaji na Uchezeshaji katika MCP

Sehemu hii inachunguza mifumo tofauti ya usafirishaji inayopatikana katika MCP na jukumu lao katika kuruhusu uwezo wa uchezeshaji kwa mawasiliano ya wakati halisi kati ya wateja na seva.

### Nini ni Mfumo wa Usafirishaji?

Mfumo wa usafirishaji unaelezea jinsi data hubadilishwa kati ya mteja na seva. MCP inaunga mkono aina nyingi za usafirishaji ili kufaa mazingira na mahitaji tofauti:

- **stdio**: Ingizo/Toleo la kawaida, linalofaa kwa zana za eneo la kazi na zinazotumika kwa CLI. Rahisi lakini haifai kwa wavuti au wingu.
- **SSE (Matukio Yanayotumwa na Seva)**: Inaruhusu seva kusukuma masasisho ya wakati halisi kwa wateja kupitia HTTP. Inafaa kwa UI za wavuti, lakini ina mipaka katika kupanuka na kubadilika. Kuanzia MCP Specification 2025-06-18, usafirishaji wa SSE (Matukio Yanayotumwa na Seva) wa pekee umeachwa na kubadilishwa na usafirishaji wa "Streamable HTTP".
- **Streamable HTTP**: Usafirishaji wa kisasa wa kutumia HTTP ambao unaunga mkono arifa na upanuzi bora. Unapendekezwa kwa zaidi ya hali za uzalishaji na za wingu.

### Jedwali la Ulinganisho

Angalia jedwali la kulinganisha hapa chini ili kuelewa tofauti kati ya mifumo hii ya usafirishaji:

| Usafirishaji     | Masasisho ya Wakati Halisi | Uchezeshaji | Kupanuka | Matumizi               |
|-----------------|----------------------------|-------------|----------|------------------------|
| stdio           | Hapana                     | Hapana      | Chini    | Zana za eneo la kazi CLI|
| SSE             | Ndiyo                      | Ndiyo       | Kati     | Wavuti, masasisho ya wakati halisi|
| Streamable HTTP | Ndiyo                      | Ndiyo       | Juu      | Wingu, wateja wengi    |

> **Vidokezo:** Kuchagua usafirishaji sahihi kunaathiri utendaji, upanuzi, na uzoefu wa mtumiaji. **Streamable HTTP** inapendekezwa kwa programu za kisasa, zinazoweza kupanuka, na tayari kwa wingu.

Tambua mifumo ya usafirishaji stdio na SSE uliyoonyeshwa katika sura zilizopita na jinsi Streamable HTTP ni usafirishaji unaojadiliwa katika sura hii.

## Uchezeshaji: Dhana na Motisha

Kuelewa dhana za msingi na motisha nyuma ya uchezeshaji ni muhimu kwa kutekeleza mifumo madhubuti ya mawasiliano ya wakati halisi.

**Uchezeshaji** ni mbinu katika programu za mtandao inayoruhusu data kutumwa na kupokelewa kwa vipande vidogo vinavyoweza kudhibitiwa au kama mfululizo wa matukio, badala ya kusubiri jibu lote liwe tayari. Hii ni hasa muhimu kwa:

- Faili kubwa au seti kubwa za data.
- Masasisho ya wakati halisi (mfano: mazungumzo, sehemu za maendeleo).
- Hesabu za muda mrefu ambapo unataka mtumiaji ajulishwe.

Hapa ni kile unachohitaji kujua kuhusu uchezeshaji kwa kiwango cha juu:

- Data hutolewa kidogo kidogo, si yote kwa wakati mmoja.
- Mteja anaweza kuchakata data anapopokea.
- Kupunguza ucheleweshaji unaoonekana na kuboresha uzoefu wa mtumiaji.

### Kwa nini tumia uchezeshaji?

Sababu za kutumia uchezeshaji ni zifuatazo:

- Watumiaji hupata mrejesho mara moja, si mwisho tu.
- Inaruhusu matumizi ya wakati halisi na UI zinazojibu haraka.
- Matumizi bora ya rasilimali za mtandao na kompyuta.

### Mfano Rahisi: Seva na Mteja wa Utoaji wa HTTP

Huu ni mfano rahisi wa jinsi uchezeshaji unavyoweza kutekelezwa:

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

Mfano huu unaonyesha seva ikituma mfululizo wa ujumbe kwa mteja wakati unavyopatikana, badala ya kusubiri ujumbe wote uwe tayari.

**Inavyofanya kazi:**

- Seva hutolea kila ujumbe wakati uko tayari.
- Mteja anapokea na kuchapisha kila kipande anapokipata.

**Mahitajio:**

- Seva lazima itumie jibu la uchezeshaji (mfano, `StreamingResponse` katika FastAPI).
- Mteja lazima achakathe jibu kama mtiririko (`stream=True` katika requests).
- Aina ya yaliyomo kawaida ni `text/event-stream` au `application/octet-stream`.

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

**Maelezo ya Kutekeleza Java:**

- Inatumia rundo la Spring Boot la reactive na `Flux` kwa uchezeshaji
- `ServerSentEvent` hutoa uchezeshaji wa matukio yaliyo na muundo na aina za matukio
- `WebClient` na `bodyToFlux()` huwezesha matumizi ya uchezeshaji wa reactive
- `delayElements()` huiga muda wa usindikaji kati ya matukio
- Matukio yanaweza kuwa na aina (`info`, `result`) kwa usimamizi bora wa mteja

### Ulinganisho: Uchezeshaji wa Kawaida vs Uchezeshaji wa MCP

Tofauti kati ya jinsi uchezeshaji unavyofanya kazi kwa njia "kawaida" dhidi ya MCP inaweza kuonyeshwa kama ifuatavyo:

| Kipengele             | Uchezeshaji wa HTTP wa Kawaida | Uchezeshaji wa MCP (Arifa)        |
|-----------------------|---------------------------------|----------------------------------|
| Jibu kuu              | Vipande vya data                | Jibu moja mwishoni               |
| Masasisho ya maendeleo | Hutumwa kama vipande vya data   | Hutumwa kama arifa               |
| Mahitaji ya mteja     | Lazima achakathe mtiririko      | Lazima atekeleze mshughulikiaji wa jumbe |
| Matumizi              | Faili kubwa, michakato ya tokeni za AI | Maendeleo, kumbukumbu, mrejesho wa wakati halisi|

### Tofauti Muhimu Zinazoshuhudiwa

Zaidi ya hayo, hapa kuna tofauti kadhaa muhimu:

- **Mfuatano wa Mawasiliano:**
  - Uchezeshaji wa kawaida wa HTTP: Unatumia msimbo rahisi wa uhamisho wa vipande kutuma data kwa vipande
  - Uchezeshaji wa MCP: Unatumia mfumo wa arifa ulio na muundo kwa kutumia itifaki ya JSON-RPC

- **Muundo wa Ujumbe:**
  - HTTP wa kawaida: Vipande vya maandishi sawa na mistari mipya
  - MCP: Vitu vya LoggingMessageNotification vilivyo na metadata

- **Utekelezaji wa Mteja:**
  - HTTP wa kawaida: Mteja rahisi anayechakata majibu ya uchezeshaji
  - MCP: Mteja mtaalamu zaidi mwenye mshughulikiaji wa jumbe kwa ajili ya kuchakata aina tofauti za jumbe

- **Masasisho ya Maendeleo:**
  - HTTP wa kawaida: Maendeleo ni sehemu ya mtiririko mkuu wa jibu
  - MCP: Maendeleo hutumwa kupitia arifa tofauti huku jibu kuu likikuja mwishoni

### Mapendekezo

Kuna mambo tunayopendekeza wakati wa kuchagua kati ya kutekeleza uchezeshaji wa kawaida (kama tulivyoonyesha hapa juu kwa kutumia `/stream`) na uchezeshaji kupitia MCP.

- **Kwa mahitaji rahisi ya uchezeshaji:** Uchezeshaji wa HTTP wa kawaida ni rahisi kutekeleza na wa kutosha kwa mahitaji ya msingi ya uchezeshaji.

- **Kwa programu tata, zinazoweka mwingiliano:** Uchezeshaji wa MCP hutoa mbinu iliyo na muundo zaidi na metadata tajiri na utofauti kati ya arifa na matokeo ya mwisho.

- **Kwa programu za AI:** Mfumo wa arifa wa MCP ni maalum kwa ajili ya kazi za muda mrefu za AI ambapo unataka kuwahabarisha watumiaji kuhusu maendeleo.

## Uchezeshaji katika MCP

Sawa, umeona mapendekezo na ulinganisho hadi sasa kuhusu tofauti kati ya uchezeshaji wa kawaida na MCP. Hebu tuchunguze kwa kina jinsi unavyoweza kutumia uchezeshaji katika MCP.

Kuelewa jinsi uchezeshaji unavyofanya kazi ndani ya mfumo wa MCP ni muhimu kwa kujenga programu zinazojibu haraka na kutoa mrejesho wa wakati halisi kwa watumiaji wakati wa kazi za muda mrefu.

Katika MCP, uchezeshaji si kuhusu kutuma jibu kuu kwa vipande, bali ni kuhusu kutuma **arifa** kwa mteja wakati zana inachakata ombi. Arifa hizi zinaweza kujumuisha masasisho ya maendeleo, kumbukumbu, au matukio mengine.

### Inavyofanya kazi

Jibu kuu bado hutumwa kama jibu moja. Hata hivyo, arifa zinaweza kutumwa kama ujumbe tofauti wakati wa usindikaji na hivyo kusasisha mteja kwa wakati halisi. Mteja lazima aweze kushughulikia na kuonyesha arifa hizi.

## Nini ni Arifa?

Tuliambia "Arifa", maana yake ni nini katika muktadha wa MCP?

Arifa ni ujumbe unaotumwa kutoka seva kwa mteja ili kumjulisha kuhusu maendeleo, hali, au matukio mengine wakati wa operesheni ya muda mrefu. Arifa huongeza uwazi na uzoefu wa mtumiaji.

Kwa mfano, mteja anapaswa kutuma arifa mara baada ya mshikamano wa awali na seva kufanyika.

Arifa inaonekana kama ujumbe wa JSON kama ifuatavyo:

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

> **Taarifa ya kuachwa matumizi:** Kandidati wa toleo la MCP `2026-07-28` unaashiria kuwa primitive ya Logging imeachwa kwa faida ya `stderr` kwa usafirishaji wa stdio na OpenTelemetry kwa uangalizi ulio na muundo. Logging inaendelea kufanya kazi katika `2025-11-25` na kwa mwaka angalau baada ya kuachwa matumizi rasmi. Angalia [Mbali na Mabadiliko Katika MCP: Kandidati wa Toleo la 2026-07-28](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Ili kufanya logging ifanye kazi, seva inahitaji kuiwezesha kama kipengele/uwezo kama ifuatavyo:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Kulingana na SDK inayotumika, logging inaweza kuwa imewezeshwa kwa default, au huenda ukahitaji kuiwezesha wazi katika usanidi wa seva yako.

Kuna aina tofauti za arifa:

| Kiwango    | Maelezo                      | Mfano wa Matumizi             |
|------------|------------------------------|-------------------------------|
| debug      | Maelezo ya kina ya ufuatiliaji | Sehemu za kuingia/kuondoka kwa kazi |
| info       | Ujumbe wa taarifa za jumla     | Masasisho ya maendeleo ya operesheni |
| notice     | Matukio ya kawaida lakini muhimu | Mabadiliko ya usanidi          |
| warning    | Masharti ya onyo              | Matumizi ya kipengele kilichotengwa |
| error      | Masharti ya hitilafu          | Kushindwa kwa operesheni       |
| critical   | Masharti ya hali kali          | Kushindwa kwa sehemu ya mfumo  |
| alert      | Hatua lazima zichukuliwe mara moja | Ugunduo wa uharibifu wa data  |
| emergency  | Mfumo hauwezi kutumika         | Kushindwa kabisa kwa mfumo    |

## Kutekeleza Arifa katika MCP

Kutekeleza arifa katika MCP, unahitaji kuandaa pande za seva na mteja kushughulikia masasisho ya wakati halisi. Hii inaruhusu programu yako kutoa mrejesho wa papo hapo kwa watumiaji wakati wa kazi za muda mrefu.

### Sehemu ya seva: Kutuma Arifa

Tuanzie sehemu ya seva. Katika MCP, unafafanua zana zinazoweza kutuma arifa wakati wa kuchakata maombi. Seva hutumia kipengele cha muktadha (kawaida `ctx`) kutuma ujumbe kwa mteja.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Katika mfano uliotangulia, zana ya `process_files` inatuma arifa tatu kwa mteja wakati inachakata kila faili. Mbinu ya `ctx.info()` inatumika kutuma ujumbe wa taarifa.

Zaidi ya hayo, ili kuwezesha arifa, hakikisha seva yako inatumia usafirishaji wa uchezeshaji (kama `streamable-http`) na mteja wako anatekeleza mshughulikiaji wa jumbe kuchakata arifa. Hapa ni jinsi unavyoweza kuandaa seva kutumia usafirishaji wa `streamable-http`:

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

Katika mfano huu wa .NET, zana ya `ProcessFiles` imewekwa sifa ya `Tool` na inatuma arifa tatu kwa mteja wakati inachakata kila faili. Mbinu ya `ctx.Info()` inatumika kutuma ujumbe wa taarifa.

Ili kuwezesha arifa katika seva yako ya MCP ya .NET, hakikisha unatumia usafirishaji wa uchezeshaji:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Sehemu ya mteja: Kupokea Arifa

Mteja lazima atekeleze mshughulikiaji wa jumbe ili kuchakata na kuonyesha arifa zinapowasili.

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

Katika msimbo uliotangulia, kazi ya `message_handler` inakagua kama ujumbe unaopokelewa ni arifa. Ikiwa ndio, inachapisha arifa; vinginevyo, inachakata kama ujumbe wa seva wa kawaida. Pia angalia jinsi `ClientSession` inavyoanzishwa na `message_handler` kushughulikia arifa zinazoingia.

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

Katika mfano huu wa .NET, kazi ya `MessageHandler` inakagua kama ujumbe unaopokelewa ni arifa. Ikiwa ndio, inachapisha arifa; vinginevyo, inachakata kama ujumbe wa seva wa kawaida. `ClientSession` inaanzishwa na mshughulikiaji wa jumbe kupitia `ClientSessionOptions`.

Ili kuwezesha arifa, hakikisha seva yako inatumia usafirishaji wa uchezeshaji (kama `streamable-http`) na mteja wako anatekeleza mshughulikiaji wa jumbe kushughulikia arifa.

## Arifa za Maendeleo na Hali za Matumizi

Sehemu hii inaelezea dhana ya arifa za maendeleo katika MCP, kwa nini ni muhimu, na jinsi ya kuzitekeleza kwa kutumia Streamable HTTP. Pia utapata zoezi la vitendo kuongeza uelewa wako.

Arifa za maendeleo ni ujumbe za wakati halisi zinazotumwa kutoka seva kwa mteja wakati wa kazi za muda mrefu. Badala ya kusubiri mchakato mzima ukamilike, seva inaendelea kusasisha mteja kuhusu hali ya sasa. Hii huongeza uwazi, uzoefu wa mtumiaji, na kufanya utatuzi wa hitilafu kuwa rahisi.

**Mfano:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Kwa nini Utumie Arifa za Maendeleo?

Arifa za maendeleo ni muhimu kwa sababu kadhaa:

- **Uzoefu bora wa mtumiaji:** Watumiaji wanaona masasisho wanapofanya kazi, si mwisho tu.
- **Mrejesho wa wakati halisi:** Wateja wanaweza kuonyesha sehemu za maendeleo au kumbukumbu, na kufanya programu ionekane jibu kwa haraka.
- **Utatuzi rahisi na ufuatiliaji:** Waendelezaji na watumiaji wanaweza kuona wapi mchakato unachelewa au umekwama.

### Jinsi ya Kutekeleza Arifa za Maendeleo

Hapa ni jinsi unavyoweza kutekeleza arifa za maendeleo katika MCP:

- **Kwenye seva:** Tumia `ctx.info()` au `ctx.log()` kutuma arifa kila kipengele kinapochakatwa. Hii inatuma ujumbe kwa mteja kabla jibu kuu liwe tayari.
- **Kwenye mteja:** Tekeleza mshughulikiaji wa jumbe anayesikiliza na kuonyesha arifa zinapowasili. Mshughulikiaji huyu hutofautisha kati ya arifa na jibu la mwisho.

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

## Mambo ya Usalama Kuzingatiwa

Usalama unapaswa kuwa kipaumbele cha juu wakati wa kutekeleza seva yoyote, hasa wakati wa kutumia usafirishaji unaotegemea HTTP kama Streamable HTTP katika MCP.

Unapotekeleza seva za MCP zinazotumia usafirishaji wa aina ya HTTP, usalama huwa jambo muhimu sana linalohitaji umakini wa makini juu ya mbinu mbalimbali za mashambulizi na mbinu za ulinzi.

### Muhtasari

Usalama ni muhimu wakati wa kufungua seva za MCP kupitia HTTP. Streamable HTTP huleta maeneo mapya ya mashambulizi na yanahitaji usanidi wa makini.

Hapa kuna mambo muhimu ya kuzingatia kuhusu usalama:

- **Uthibitishaji wa Kichwa cha Origin**: Kila mara thibitisha kichwa cha `Origin` ili kuzuia mashambulizi ya DNS rebinding.
- **Kuhusiana na Localhost**: Kwa maendeleo ya ndani, sanifu seva kwa kutumia `localhost` ili kuepuka kuziweka wazi kwenye mtandao wa umma.
- **Uthibitishaji**: Tekeleza uthibitishaji (kwa mfano, API keys, OAuth) kwa usambazaji wa uzalishaji.
- **CORS**: Sanifu sera za Kushirikiana Mipaka ya Asili (CORS) ili kupunguza ufikiaji.
- **HTTPS**: Tumia HTTPS katika uzalishaji ili kusimba trafiki.

### Mbinu Bora

Zaidi ya hayo, hapa kuna mbinu bora za kufuata wakati wa kutekeleza usalama kwenye seva zako za MCP za kutiririsha:

- Usiamini maombi yanayoingia bila uthibitisho.
- Rekodi na fuatilia ufikiaji wote na makosa.
- Sasisha mara kwa mara utegemezi ili kufunika dosari za usalama.

### Changamoto

Utakutana na changamoto fulani wakati wa kutekeleza usalama katika seva za MCP za kutiririsha:

- Kuweka sawa usalama na urahisi wa maendeleo
- Kuhakikisha ulinganifu na mazingira mbalimbali ya wateja


## Kuboresha kutoka SSE kwenda Streamable HTTP

Kwa programu zinazotumia Server-Sent Events (SSE), kuhama kwenda Streamable HTTP kunatoa uwezo ulioimarishwa na uendelevu bora kwa muda mrefu kwa utekelezaji wako wa MCP.

### Kwa Nini Kuboresha?

Kuna sababu mbili muhimu za kuboresha kutoka SSE kwenda Streamable HTTP:

- Streamable HTTP hutoa upanuzi bora, ulinganifu, na msaada bora wa arifa kuliko SSE.
- Ni usafirishaji unaopendekezwa kwa programu mpya za MCP.

### Hatua za Kuhama

Hivi ndivyo unavyoweza kuhama kutoka SSE kwenda Streamable HTTP katika programu zako za MCP:

- **Sasisha msimbo wa seva** kutumia `transport="streamable-http"` katika `mcp.run()`.
- **Sasisha msimbo wa mteja** kutumia `streamablehttp_client` badala ya mteja wa SSE.
- **Tekeleza msindikaji wa ujumbe** katika mteja kushughulikia arifa.
- **Jaribu ulinganifu** na zana na mitiririko ya kazi iliyopo.

### Kudumisha Ulinganifu

Inashauriwa kudumisha ulinganifu na wateja wa SSE waliopo wakati wa mchakato wa kuhama. Hapa kuna mbinu fulani:

- Unaweza kuunga mkono SSE na Streamable HTTP kwa kuendesha usafirishaji wote kwenye sehemu tofauti.
- Polepole hamisha wateja kwenda usafirishaji mpya.

### Changamoto

Hakikisha unashughulikia changamoto zifuatazo wakati wa mchakato wa kuhama:

- Kuhakikisha wateja wote wanasasishwa
- Kushughulikia tofauti katika utoaji wa arifa

### Kazi: Jenga Programu Yako ya Kutoa MCP

**Hali:**
Jenga seva na mteja wa MCP ambapo seva inashughulikia orodha ya vitu (kama faili au nyaraka) na kutuma arifa kwa kila kitu kinachoshughulikiwa. Mteja aonyeshe kila arifa inapofika.

**Hatua:**

1. Tekeleza chombo cha seva kinachoshughulikia orodha na kutuma arifa kwa kila kipengee.
2. Tekeleza mteja mwenye msindikaji wa ujumbe wa kuonyesha arifa kwa wakati halisi.
3. Thibitisha utekelezaji wako kwa kuendesha seva na mteja, na angalia arifa.

[Solution](./solution/README.md)

## Kusoma Zaidi & Nini Kufuata?

Kuendelea na safari yako na MCP wa kutiririsha na kuongeza maarifa yako, sehemu hii inatoa rasilimali za ziada na hatua zinazo pendekezwa za kujifunza programu za hali ya juu zaidi.

### Kusoma Zaidi

- [Microsoft: Utangulizi wa HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Nini Kufuata?

- Jaribu kujenga zana zaidi za MCP zinazotumia utiririshaji kwa uchambuzi wa wakati halisi, mazungumzo, au uhariri wa pamoja.
- Chunguza kuunganisha MCP streaming na mifumo ya mbele (React, Vue, n.k.) kwa masasisho ya UI ya moja kwa moja.
- Kufuata: [Kutumia AI Toolkit kwa VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->