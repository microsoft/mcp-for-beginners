# HTTPS Streaming gamit ang Model Context Protocol (MCP)

Nagbibigay ang kabanatang ito ng komprehensibong gabay sa pagpapatupad ng secure, scalable, at real-time na streaming gamit ang Model Context Protocol (MCP) sa pamamagitan ng HTTPS. Saklaw nito ang motibasyon para sa streaming, ang mga magagamit na mekanismo ng transportasyon, kung paano ipatupad ang streamable HTTP sa MCP, mga best practices sa seguridad, paglipat mula sa SSE, at praktikal na gabay para sa pagbuo ng sarili mong streaming MCP na mga aplikasyon.

> [!WARNING]
> Ang mga halimbawa ng implementasyon sa araling ito ay target ang **MCP Specification
> `2025-11-25`** at nagpapakita ng legacy na `initialize` handshake,
> `Mcp-Session-Id`, GET event stream, at resumability model. Inaalis ng MCP `2026-07-28`
> ang mga feature na ito. Ang kasalukuyang Streamable HTTP requests ay mga self-contained
> POST requests na may `MCP-Protocol-Version` at `Mcp-Method` headers, pati na rin
> ang `Mcp-Name` kung kinakailangan. Tingnan ang
> [Ano ang mga Pagbabago sa MCP: Ang 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md)
> bago gamitin ang mga halimbawa na ito sa bagong implementasyon.

## Mga Mekanismo ng Transportasyon at Streaming sa MCP

Tinutuklas ng seksyong ito ang iba't ibang mekanismo ng transportasyon na magagamit sa MCP at ang kanilang papel sa pagpapa-enable ng kakayahan sa streaming para sa real-time na komunikasyon sa pagitan ng mga kliyente at server.

### Ano ang Mekanismo ng Transportasyon?

Ang mekanismo ng transportasyon ay tumutukoy kung paano ipinagpapalitan ang data sa pagitan ng kliyente at server. Sinusuportahan ng MCP ang maraming uri ng transportasyon upang umangkop sa iba't ibang kapaligiran at pangangailangan:

- **stdio**: Standard input/output, angkop para sa mga lokal at CLI-based na tools. Simple ngunit hindi angkop para sa web o cloud.
- **HTTP+SSE**: Ang legacy remote transport, deprecated sa MCP `2025-03-26`
    at pinalitan ng Streamable HTTP. Huwag gamitin sa mga bagong implementasyon.
- **Streamable HTTP**: Modernong HTTP-based streaming transport, sumusuporta sa mga notipikasyon at mas mahusay na scalability. Inirerekomenda para sa karamihan ng mga production at cloud na scenario.

### Talahanayan ng Paghahambing

Tingnan ang talahanayan ng paghahambing sa ibaba upang maunawaan ang mga pagkakaiba sa pagitan ng mga mekanismong ito ng transportasyon:

| Transport | Status | Mga Notipikasyon | Karaniwang gamit |
|---|---|---|---|
| stdio | Kasalukuyan | Oo | Mga lokal na subprocess |
| HTTP+SSE | Deprecated | Oo | Mga legacy na remote implementations |
| Streamable HTTP | Kasalukuyan | Oo | Mga remote at cloud na server |

> **Tip:** Ang pagpili ng tamang transport ay nakakaapekto sa performance, scalability, at karanasan ng gumagamit. Inirerekomenda ang **Streamable HTTP** para sa mga modernong, scalable, at cloud-ready na mga aplikasyon.

Ang mga standard na transport ay stdio at Streamable HTTP. Lumalabas ang HTTP+SSE sa
mga lumang halimbawa lamang.

## Streaming: Mga Konsepto at Motibasyon

Mahalaga ang pag-unawa sa mga pangunahing konsepto at motibasyon sa likod ng streaming para sa epektibong pagpapatupad ng mga sistema ng real-time na komunikasyon.

**Streaming** ay isang teknik sa network programming na nagpapahintulot sa pagpapadala at pagtanggap ng data sa maliliit, manageable na piraso o bilang isang sunod-sunod ng mga pangyayari, sa halip na maghintay na ang buong tugon ay maging handa na. Ito ay partikular na kapaki-pakinabang para sa:

- Malalaking files o datasets.
- Real-time na mga update (hal., chat, progress bars).
- Mga long-running na computations kung saan nais mong panatilihing may alam ang gumagamit.

Narito ang mga dapat mong malaman tungkol sa streaming sa mataas na antas:

- Ang data ay naihahatid nang progresibo, hindi sabay-sabay.
- Ang kliyente ay maaaring magproseso ng data habang dumarating ito.
- Nakababawas ng perceived latency at nagpapabuti sa karanasan ng gumagamit.

### Bakit gumamit ng streaming?

Ang mga dahilan para gamitin ang streaming ay ang mga sumusunod:

- Nakakakuha agad ng feedback ang mga gumagamit, hindi lamang sa huli
- Nagpapagana ng mga real-time na aplikasyon at responsive na UI
- Mas epektibong paggamit ng network at compute resources

### Simpleng Halimbawa: HTTP Streaming Server at Client

Narito ang simpleng halimbawa kung paano maipapatupad ang streaming:

#### Python

**Server (Python, gamit ang FastAPI at StreamingResponse):**

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

**Client (Python, gamit ang requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Ipinapakita ng halimbawang ito ang isang server na nagpapadala ng serye ng mga mensahe sa client habang ito ay nagiging available, sa halip na maghintay na lahat ng mga mensahe ay handa na.

**Paano ito gumagana:**

- Ang server ay inilalabas ang bawat mensahe kapag handa na.
- Ang client ay tumatanggap at ini-imprenta ang bawat bahagi habang dumarating.

**Mga Kinakailangan:**

- Dapat gumamit ang server ng streaming response (hal., `StreamingResponse` sa FastAPI).
- Dapat iproseso ng client ang response bilang stream (`stream=True` sa requests).
- Karaniwang Content-Type ay `text/event-stream` o `application/octet-stream`.

#### Java

**Server (Java, gamit ang Spring Boot at Server-Sent Events):**

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

**Client (Java, gamit ang Spring WebFlux WebClient):**

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

**Mga Tala sa Implementasyon ng Java:**

- Gumagamit ng reactive stack ng Spring Boot gamit ang `Flux` para sa streaming
- Nagbibigay ang `ServerSentEvent` ng structured event streaming na may mga uri ng event
- Nagpapagana ang `WebClient` gamit ang `bodyToFlux()` ng reactive streaming consumption
- Sinisimulate ng `delayElements()` ang processing time sa pagitan ng mga event
- Maaaring magkaroon ng mga uri ng event (`info`, `result`) para sa mas mahusay na paghawak ng client

### Paghahambing: Classic Streaming vs MCP Streaming

Ang mga pagkakaiba sa pagitan kung paano gumagana ang streaming sa isang "classical" na paraan kumpara sa kung paano ito gumagana sa MCP ay maaaring ipakita nang ganito:

| Katangian                | Classic HTTP Streaming         | MCP Streaming (Mga Notipikasyon)      |
|------------------------|-------------------------------|-------------------------------------|
| Pangunahing tugon      | Chunked                       | Isa lang, sa dulo                 |
| Mga update ng progreso | Pinapadala bilang mga data chunk | Pinapadala bilang mga notipikasyon    |
| Mga kinakailangan ng client | Dapat iproseso ang stream          | Dapat magpatupad ng message handler     |
| Gamit                   | Malalaking files, AI token streams | Progreso, mga log, real-time na feedback |

### Mga Pangunahing Pagkakaiba na Napansin

Bukod dito, narito ang ilang mga pangunahing pagkakaiba:

- **Pattern ng Komunikasyon:**
  - Classic HTTP streaming: Gumagamit ng simple chunked transfer encoding para magpadala ng data sa mga bahagi
  - MCP streaming: Gumagamit ng structured notification system gamit ang JSON-RPC protocol

- **Format ng Mensahe:**
  - Classic HTTP: Plain text chunks na may mga newline
  - MCP: Structured LoggingMessageNotification objects na may metadata

- **Implementasyon ng Client:**
  - Classic HTTP: Simple client na nagpoproseso ng streaming response
  - MCP: Mas sopistikadong client na may message handler para iproseso ang iba't ibang uri ng mensahe

- **Mga Update sa Progreso:**
  - Classic HTTP: Ang progreso ay bahagi ng pangunahing response stream
  - MCP: Ang progreso ay ipinapadala sa pamamagitan ng hiwalay na notification messages habang ang pangunahing tugon ay dumarating sa huli

### Mga Rekomendasyon

May ilang mga bagay na nirerekomenda namin pagdating sa pagpili sa pagitan ng pagpapatupad ng classical streaming (bilang isang endpoint na ipinakita namin sa itaas gamit ang `/stream`) kumpara sa pagpili ng streaming sa pamamagitan ng MCP.

- **Para sa simpleng pangangailangan sa streaming:** Mas madali ipatupad ang Classic HTTP streaming at sapat na para sa mga basic na pangangailangan sa streaming.


- **Para sa mga kumplikado, interaktibong aplikasyon:** Nagbibigay ang MCP streaming ng mas organisadong paraan na may mas mayamang metadata at paghihiwalay sa pagitan ng mga notification at panghuling mga resulta.

- **Para sa mga AI na aplikasyon:** Partikular na kapaki-pakinabang ang notification system ng MCP para sa mga mahahabang AI na gawain kung saan nais mong panatilihing napapaalalahanan ang mga gumagamit tungkol sa progreso.

## Streaming sa MCP

Okay, kaya nakita mo na ang ilang mga rekomendasyon at paghahambing tungkol sa pagkakaiba ng klasikong streaming at streaming sa MCP. Tingnan natin nang detalyado kung paano mo magagamit ang streaming sa MCP.

Mahalaga ang pag-unawa kung paano gumagana ang streaming sa loob ng balangkas ng MCP para makabuo ng mga tumutugong aplikasyon na nagbibigay ng real-time na feedback sa mga gumagamit habang may mahahabang operasyon.

Sa MCP, ang streaming ay hindi tungkol sa pagpapadala ng pangunahing tugon ng pira-piraso, kundi tungkol sa pagpapadala ng **mga notification** sa kliyente habang ang isang tool ay pinoproseso ang isang kahilingan. Ang mga notification na ito ay maaaring maglaman ng mga update sa progreso, mga log, o iba pang mga pangyayari.

### Kung paano ito gumagana

Ang pangunahing resulta ay ipinapadala pa rin bilang isang tugon lamang. Ngunit, ang mga notification ay maaaring ipadala bilang hiwalay na mga mensahe habang isinasagawa ang pagpoproseso at sa gayon ay ina-update ang kliyente sa real time. Dapat kayang hawakan at ipakita ng kliyente ang mga notification na ito.

### Opsyonal na pagsasanay: kumonekta sa isang hosted MCP server

Maaari mo ring gamitin ang Streamable HTTP nang hindi nagpapatakbo ng lokal na server. Ang halimbawa na ito
ay kumokonekta sa [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
natutuklasan ang mga tool nito, at naghahanap ng pampublikong dokumentasyon ng MCP gamit ang parehong
Python SDK tulad ng [lokal na kliyente](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Ang anonymous endpoint ng Parallel ay hindi nangangailangan ng account o API key. Ang libreng access ay
may rate limiter. Ang pagpapatakbo ng script na ito ay nagpapadala ng mga query sa paghahanap, layunin, at isang
random na session identifier sa Parallel. Nag-aalok din ang serbisyo ng `web_fetch`,
na nagpapadala ng mga hinihinging URL at anumang ibinigay na konteksto sa Parallel. Gumamit ng pampublikong
impormasyon para sa pagsasanay na ito; tingnan ang mga [terms](https://parallel.ai/customer-terms)
at [privacy policy](https://parallel.ai/privacy-policy).

Sa Python 3.10 o mas bago at may naka-activate na virtual environment, i-install ang SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

I-save ito bilang `hosted_search.py` at patakbuhin ang `python hosted_search.py`:

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

Inaasahan na tatakpan ng discovery ang `web_search` at `web_fetch`, kasunod ng tugon sa paghahanap
na naglalaman ng mga source URL at mga sipi. Puwedeng mag-iba o walang laman ang mga resulta.
Sinusuri ng script ang `isError` dahil maaaring mabigo ang isang tool kahit matagumpay ang HTTP request.
Kung ang access ay may rate limit, maghintay bago subukang muli. Gamitin muli ang parehong
`session_id` kung palalawakin mo ang script sa mga kaugnay na tawag sa paghahanap o fetch.

Pinapayagan ng Streamable HTTP ang parehong JSON at SSE na mga tugon; maaaring magbalik ang server na ito ng
kumpletong JSON na resulta nang walang mga notification ng progreso. Pinangangasiwaan ng SDK ang
transport. Magpatuloy sa lokal na halimbawa sa ibaba para matuto tungkol sa mga notification.
Ang opsyonal na script na ito ay gumagawa ng isang malinaw na paghahanap at nagsasara ng koneksyon kapag
natapos. Kung kalaunan ay ipalalabas mo ang mga tool na ito sa isang ahente, maaaring tawagin sila ng ahente habang
nagtatrabaho; tratuhin ang nakuha na tekstong web bilang hindi pinagkakatiwalaang datos.

## Ano ang Notification?

Sinabi namin na "Notification", ano ang ibig sabihin noon sa konteksto ng MCP?

Ang notification ay isang JSON-RPC na mensahe na walang `id` at hindi
tumatanggap ng tugon. Ginagamit ng MCP ang mga notification para sa progreso, pagkansela, at
iba pang one-way na mga pangyayari.

Sa MCP `2025-11-25`, nagpapadala ang kliyente ng `notifications/initialized` pagkatapos ng
initialization handshake. Walang initialization handshake ang MCP `2026-07-28`, kaya
ito ay legacy na asal na notification.

Ganito ang hitsura ng notification bilang isang JSON na mensahe:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Ang pag-log ay isang tampok na gumagamit ng mga notification; ang mga notification mismo ay isang
pangkalahatang URI ng mensahe sa JSON-RPC.

> **Hindi na ginagamit sa MCP `2026-07-28`:** nananatiling magagamit ang tampok na Pag-log
> para sa pagiging tugma ngunit maaaring alisin sa unang pagrebisa ng pagtutukoy
> na ilalabas sa o pagkatapos ng Hulyo 28, 2027. Dapat gumamit ang mga bagong implementasyon ng
> `stderr` gamit ang stdio o OpenTelemetry para sa estrukturadong observability.

Para sa legacy na implementasyon na `2025-11-25`, pinapagana ng server ang kakayahan sa Pag-log
tulad ng sumusunod:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Depende sa ginamit na SDK, maaaring naka-enable na ang pag-log bilang default, o kailangan mo itong hayagang enable sa iyong server configuration.

May iba't ibang uri ng mga notification:

| Level     | Paglalarawan                  | Halimbawa ng Paggamit           |
|-----------|-------------------------------|---------------------------------|
| debug     | Detalyadong impormasyon sa pag-debug | Mga punto ng pagpasok/exit ng function |
| info      | Pangkalahatang mensahe ng impormasyon | Mga update sa progreso ng operasyon |
| notice    | Normal ngunit mahalagang mga pangyayari | Mga pagbabago sa configuration |
| warning   | Mga kundisyon na babala       | Paggamit ng deprecated na tampok |
| error     | Mga kundisyon ng error        | Kabiguan sa operasyon           |
| critical  | Kritikal na mga kundisyon     | Kabiguan ng bahagi ng sistema   |
| alert     | Kailangang gumawa ng aksyon agad | Nadiskubre ang korapsyon ng data |
| emergency | Hindi magamit ang sistema     | Kumpletong kabiguan ng sistema  |

## Pagpapatupad ng Mga Notification sa MCP

Para magpatupad ng mga notification sa MCP, kailangan mong i-setup ang parehong server at client na mga bahagi upang hawakan ang mga real-time na update. Pinapayagan nito ang iyong aplikasyon na magbigay ng agarang feedback sa mga gumagamit habang may mahahabang operasyon.

### Server-side: Pagpapadala ng Mga Notification

Simulan natin sa server side. Sa MCP, nagde-define ka ng mga tool na maaaring magpadala ng notification habang pinoproseso ang mga kahilingan. Ginagamit ng server ang context object (karaniwang `ctx`) upang magpadala ng mga mensahe sa kliyente.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Sa naunang halimbawa, ang tool na `process_files` ay nagpapadala ng tatlong notification sa kliyente habang pinoproseso ang bawat file. Ginagamit ang `ctx.info()` na metodo upang magpadala ng mga impormal na mensahe.

Bukod dito, upang paganahin ang mga notification, tiyakin na gumagamit ang iyong server ng streaming transport (tulad ng `streamable-http`) at mayroong message handler ang iyong client upang maproseso ang mga notification. Ganito mo ise-set up ang server para gamitin ang `streamable-http` transport:

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

Sa halimbawang ito sa .NET, ang tool na `ProcessFiles` ay may attribute na `Tool` at nagpapadala ng tatlong notification sa kliyente habang pinoproseso ang bawat file. Ginagamit ang `ctx.Info()` na metodo upang magpadala ng mga impormal na mensahe.

Upang paganahin ang mga notification sa iyong .NET MCP server, tiyakin na gumagamit ka ng streaming transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Client-side: Pagtanggap ng Mga Notification

Dapat may implementasyon ang client ng message handler upang maproseso at maipakita ang mga notification pagdating nila.

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

Sa naunang code, sinusuri ng `message_handler` na function kung ang papasok na mensahe ay isang notification. Kung oo, ipi-print nito ang notification; kung hindi, pinoproseso ito bilang regular na mensahe mula sa server. Tandaan din kung paano ini-initialize ang `ClientSession` gamit ang `message_handler` upang hawakan ang mga paparating na notification.

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


Sa halimbawa ng .NET na ito, sinusuri ng function na `MessageHandler` kung ang papasok na mensahe ay isang notification. Kung oo, ipinapakita nito ang notification; kung hindi, pinoproseso ito bilang karaniwang mensahe mula sa server. Ang `ClientSession` ay ini-initialize kasama ang message handler sa pamamagitan ng `ClientSessionOptions`.

Upang paganahin ang mga notification, tiyaking gumagamit ang iyong server ng streaming transport (tulad ng `streamable-http`) at ang iyong client ay nag-implementa ng message handler upang iproseso ang mga notification.

## Mga Notification ng Progreso at mga Sitwasyon

Ipinaliwanag sa seksyong ito ang konsepto ng mga notification ng progreso sa MCP, kung bakit mahalaga ang mga ito, at kung paano ito i-implementa gamit ang Streamable HTTP. Makakakita ka rin ng praktikal na takdang-aralin upang palalimin ang iyong pag-unawa.

Ang mga notification ng progreso ay mga real-time na mensahe na ipinapadala mula sa server papunta sa client habang isinasagawa ang mga proseso na matagal matapos. Sa halip na maghintay na matapos ang buong proseso, pinananatili ng server ang client na updated tungkol sa kasalukuyang status. Pinapabuti nito ang transparency, karanasan ng gumagamit, at nagpapadali sa pag-debug.

**Halimbawa:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Bakit Gumamit ng Mga Notification ng Progreso?

Mahalaga ang mga notification ng progreso para sa ilang mga dahilan:

- **Mas mahusay na karanasan ng gumagamit:** Nakikita ng mga gumagamit ang mga update habang nagpapatuloy ang gawain, hindi lang sa dulo.
- **Real-time na feedback:** Maaaring ipakita ng mga client ang mga progress bar o log, na nagpaparamdam na responsive ang app.
- **Mas madaling pag-debug at pagmamanman:** Nakikita ng mga developer at gumagamit kung saan maaaring mabagal o maipit ang proseso.

### Paano Mag-Implementa ng Mga Notification ng Progreso

Ganito mo maaaring i-implementa ang mga notification ng progreso sa MCP:

- **Sa server:** Gamitin ang `ctx.info()` o `ctx.log()` para magpadala ng mga notification sa bawat item na pinoproseso. Nagpapadala ito ng mensahe sa client bago maging handa ang pangunahing resulta.
- **Sa client:** Mag-implementa ng message handler na nakikinig at nagpapakita ng mga notification habang dumadating ang mga ito. Nakikilala ng handler na ito ang pagkakaiba ng mga notification at ang panghuling resulta.

**Halimbawa ng Server:**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Halimbawa ng Client:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Mga Pagsasaalang-alang sa Seguridad

Dapat unahin ang seguridad kapag nag-implementa ng anumang server, lalo na kapag gumagamit ng mga HTTP-based na transport tulad ng Streamable HTTP sa MCP.

Kapag nag-implementa ng MCP servers na gumagamit ng HTTP-based na mga transport, ang seguridad ay nagiging isang pangunahing alalahanin na nangangailangan ng maingat na pagtutok sa iba't ibang mga attack vectors at mga mekanismo ng proteksyon.

### Pangkalahatang-ideya

Kritikal ang seguridad kapag inia-expose ang mga MCP server sa HTTP. Nagdadala ang Streamable HTTP ng mga bagong attack surface at nangangailangan ng maingat na pagsasaayos.

Narito ang ilang mahahalagang pagsasaalang-alang sa seguridad:

- **Pagsusuri ng Origin Header**: Laging i-validate ang `Origin` header upang maiwasan ang DNS rebinding attacks.
- **Localhost Binding**: Para sa local development, i-bind ang mga server sa `localhost` upang hindi ito ma-expose sa pampublikong internet.
- **Authentication**: Mag-implementa ng authentication (hal., API keys, OAuth) para sa production deployments.
- **CORS**: Isaayos ang mga polisiya ng Cross-Origin Resource Sharing (CORS) upang limitahan ang access.
- **HTTPS**: Gumamit ng HTTPS sa production para i-encrypt ang traffic.

### Mga Pinakamahusay na Praktis

Bukod pa rito, narito ang ilang pinakamahusay na praktis na dapat sundin kapag nag-implementa ng seguridad sa iyong MCP streaming server:

- Huwag pagkatiwalaan ang mga papasok na request nang walang pagsusuri.
- I-log at i-monitor ang lahat ng access at mga error.
- Regular na i-update ang mga dependencies upang maisara ang mga security vulnerabilities.

### Mga Hamon

Mararanasan mo ang ilang mga hamon kapag nag-implementa ng seguridad sa mga MCP streaming server:

- Pagbabalanse ng seguridad at kadalian sa pag-develop
- Pagtiyak ng compatibility sa iba't ibang mga client environment


## Pag-upgrade mula SSE patungong Streamable HTTP

Para sa mga aplikasyon na kasalukuyang gumagamit ng Server-Sent Events (SSE), ang paglipat sa Streamable HTTP ay nagbibigay ng mas pinahusay na mga kakayahan at mas magandang pangmatagalang katatagan para sa iyong mga implementasyon ng MCP.

### Bakit Mag-upgrade?

Dalawang mahahalagang dahilan para mag-upgrade mula SSE patungong Streamable HTTP:

- Nag-aalok ang Streamable HTTP ng mas mahusay na scalability, compatibility, at mas mayamang suporta sa notification kaysa SSE.
- Ito ang inirerekomendang transport para sa mga bagong aplikasyon ng MCP.

### Mga Hakbang sa Migrasyon

Ganito mo maaaring i-migrate ang iyong MCP applications mula SSE patungong Streamable HTTP:

- **I-update ang code ng server** upang gamitin ang `transport="streamable-http"` sa `mcp.run()`.
- **I-update ang code ng client** upang gamitin ang `streamablehttp_client` sa halip na SSE client.
- **Mag-implementa ng message handler** sa client upang iproseso ang mga notification.
- **Subukan ang compatibility** gamit ang mga umiiral na tool at workflow.

### Pagpapanatili ng Compatibility

Inirerekomenda na panatilihin ang compatibility sa mga umiiral na SSE client habang ginagawa ang migrasyon. Narito ang ilang mga estratehiya:

- Maaari mong suportahan ang parehong SSE at Streamable HTTP sa pamamagitan ng pagpapatakbo ng parehong mga transport sa iba't ibang mga endpoint.
- Unti-unting i-migrate ang mga client sa bagong transport.

### Mga Hamon

Tiyaking matutugunan mo ang mga sumusunod na hamon habang ginagawa ang migrasyon:

- Pagtiyak na ang lahat ng mga client ay na-update
- Paghahandle ng mga pagkakaiba sa delivery ng notification

### Takdang-Aralin: Gumawa ng Sariling Streaming MCP App

**Sitwasyon:**
Gumawa ng MCP server at client kung saan pinoproseso ng server ang isang listahan ng mga item (hal., file o mga dokumento) at nagpapadala ng notification para sa bawat item na naproseso. Dapat ipakita ng client ang bawat notification habang dumarating ito.

**Mga Hakbang:**

1. Mag-implementa ng tool sa server na nagpoproceso ng listahan at nagpapadala ng mga notification para sa bawat item.
2. Mag-implementa ng client na may message handler upang ipakita ang mga notification nang real time.
3. Subukan ang iyong implementasyon sa pamamagitan ng pagpapatakbo ng parehong server at client, at obserbahan ang mga notification.

[Solution](./solution/README.md)

## Karagdagang Pagbasa at Ano ang Susunod?

Upang ipagpatuloy ang iyong paglalakbay sa MCP streaming at palawakin ang iyong kaalaman, nagbibigay ang seksyong ito ng dagdag na mga mapagkukunan at mga mungkahing susunod na hakbang para sa paggawa ng mas advanced na mga aplikasyon.

### Karagdagang Pagbasa

- [Microsoft: Introduction to HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Ano ang Susunod?

- Subukan ang paggawa ng mas advanced na MCP tools na gumagamit ng streaming para sa real-time analytics, chat, o collaborative editing.
- Suriin ang pagsasama ng MCP streaming sa mga frontend framework (React, Vue, atbp.) para sa live na update ng UI.
- Susunod: [Utilising AI Toolkit for VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->