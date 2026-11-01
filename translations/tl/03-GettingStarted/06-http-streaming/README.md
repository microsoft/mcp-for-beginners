# HTTPS Streaming gamit ang Model Context Protocol (MCP)

Ang kabanatang ito ay nagbibigay ng komprehensibong gabay sa pagpapatupad ng secure, scalable, at real-time na streaming gamit ang Model Context Protocol (MCP) sa pamamagitan ng HTTPS. Tinutugunan nito ang motibasyon para sa streaming, ang mga available na mekanismo ng transportasyon, kung paano ipinatupad ang streamable HTTP sa MCP, mga best practice sa seguridad, migrasyon mula sa SSE, at praktikal na gabay para sa paggawa ng sarili mong streaming MCP na mga aplikasyon.

> [!WARNING]
> Ang mga halimbawa ng pagpapatupad sa araling ito ay nakatuon sa **MCP Specification
> `2025-11-25`** at nagpapakita ng legacy `initialize` handshake,
> `Mcp-Session-Id`, GET event stream, at resumability model. Ang MCP `2026-07-28`
> ay nag-aalis ng mga tampok na iyon. Ang kasalukuyang Streamable HTTP requests ay self-contained
> POST requests na may `MCP-Protocol-Version` at `Mcp-Method` headers, pati na rin
> `Mcp-Name` kung kinakailangan. Tingnan ang
> [What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md)
> bago gamitin ang mga halimbawa sa bagong pagpapatupad.

## Mga Mekanismo ng Transportasyon at Streaming sa MCP

Pinag-aaralan ng seksyong ito ang iba't ibang mekanismo ng transportasyon na available sa MCP at ang kanilang papel sa pagpapagana ng mga kakayahan sa streaming para sa real-time na komunikasyon sa pagitan ng mga kliyente at server.

### Ano ang Mekanismo ng Transportasyon?

Ang mekanismo ng transportasyon ay tumutukoy kung paano ipinagpapalitan ang data sa pagitan ng kliyente at server. Sinusuportahan ng MCP ang maraming uri ng transport upang umayon sa iba't ibang kapaligiran at pangangailangan:

- **stdio**: Standard input/output, angkop para sa lokal at CLI-based na mga tool. Simple ngunit hindi angkop para sa web o cloud.
- **HTTP+SSE**: Ang legacy remote transport, deprecated sa MCP `2025-03-26`
    at pinalitan ng Streamable HTTP. Huwag gamitin ito para sa mga bagong pagpapatupad.
- **Streamable HTTP**: Modernong HTTP-based streaming transport, sumusuporta sa notifications at mas mahusay na scalability. Inirerekomenda para sa karamihan ng mga production at cloud scenarios.

### Talahanayan ng Paghahambing

Tingnan ang talahanayan ng paghahambing sa ibaba upang maunawaan ang mga pagkakaiba sa pagitan ng mga mekanismo ng transportasyong ito:

| Transport | Status | Notifications | Typical use |
|---|---|---|---|
| stdio | Kasalukuyan | Oo | Lokal na subprocesses |
| HTTP+SSE | Deprecated | Oo | Mga legacy remote implementations |
| Streamable HTTP | Kasalukuyan | Oo | Remote at cloud servers |

> **Tip:** Ang pagpili ng tamang transport ay nakakaapekto sa performance, scalability, at karanasan ng gumagamit. Ang **Streamable HTTP** ay inirerekomenda para sa mga modern, scalable, at cloud-ready na mga aplikasyon.

Ang mga standard na transport ay stdio at Streamable HTTP. Ang HTTP+SSE ay lumilitaw lamang sa
mga lumang halimbawa.

## Streaming: Mga Konsepto at Motibasyon

Mahalagang maunawaan ang mga pangunahing konsepto at motibasyon sa likod ng streaming para sa epektibong pagpapatupad ng mga real-time na sistema ng komunikasyon.

Ang **Streaming** ay isang teknik sa network programming na nagpapahintulot na maipadala at matanggap ang data nang paunti-unti o bilang isang sunud-sunod na mga kaganapan, sa halip na maghintay na ang buong tugon ay maging handa. Ito ay lalong kapaki-pakinabang para sa:

- Malalaking file o dataset.
- Real-time na mga update (hal., chat, progress bars).
- Mahahabang computations kung saan nais mong panatilihing informed ang gumagamit.

Narito ang dapat mong malaman tungkol sa streaming sa mataas na antas:

- Ang data ay naihahatid nang paunti-unti, hindi sabay-sabay.
- Ang kliyente ay maaaring iproseso ang data habang ito ay dumarating.
- Binabawasan ang perceived latency at pinapabuti ang karanasan ng gumagamit.

### Bakit gamitin ang streaming?

Ang mga dahilan para gamitin ang streaming ay ang mga sumusunod:

- Agad nakakatanggap ng feedback ang mga gumagamit, hindi lamang sa dulo
- Nagpapahintulot ng real-time applications at responsive UIs
- Mas epektibong paggamit ng network at compute resources

### Simpleng Halimbawa: HTTP Streaming Server & Client

Narito ang isang simpleng halimbawa kung paano maaaring ipatupad ang streaming:

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

Ipinapakita ng halimbawang ito ang pagsesend ng server ng serye ng mga mensahe sa kliyente habang nagiging available ang mga ito, sa halip na maghintay na lahat ng mensahe ay maging handa.

**Paano ito gumagana:**

- Nagbibigay ang server ng bawat mensahe kapag ito ay handa.
- Tumatanggap at ipiniprint ng kliyente ang bawat bahagi kapag dumating.

**Mga Kinakailangan:**

- Dapat gumamit ang server ng streaming response (hal., `StreamingResponse` sa FastAPI).
- Dapat iproseso ng kliyente ang tugon bilang stream (`stream=True` sa requests).
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

**Mga Tala sa Pagpapatupad sa Java:**

- Ginagamit ang reactive stack ng Spring Boot gamit ang `Flux` para sa streaming
- Nagbibigay ang `ServerSentEvent` ng structured event streaming na may mga uri ng event
- Pinapagana ng `WebClient` gamit ang `bodyToFlux()` ang reactive streaming consumption
- Ginagaya ng `delayElements()` ang processing time sa pagitan ng mga event
- Maaaring magkaroon ng mga uri ang mga event (`info`, `result`) para sa mas mahusay na paghawak ng kliyente

### Paghahambing: Classic Streaming vs MCP Streaming

Ang mga pagkakaiba kung paano gumagana ang streaming sa "classical" na paraan kumpara sa MCP ay maaaring ipakita ng ganito:

| Tampok                | Classic HTTP Streaming         | MCP Streaming (Notifications)      |
|------------------------|-------------------------------|-------------------------------------|
| Pangunahing tugon       | Chunked                       | Isa, sa dulo                      |
| Mga update sa progreso  | Ipinapadala bilang data chunks | Ipinapadala bilang notifications               |
| Mga kinakailangan sa kliyente | Dapat iproseso ang stream           | Dapat magpatupad ng message handler      |
| Gamitin                 | Malalaking file, AI token streams | Progreso, logs, real-time feedback  |

### Mga Pangunahing Pagkakaiba na Napansin

Bukod pa rito, narito ang ilang pangunahing pagkakaiba:

- **Pattern ng Komunikasyon:**
  - Classic HTTP streaming: Gumagamit ng simpleng chunked transfer encoding para magpadala ng data sa chunks
  - MCP streaming: Gumagamit ng structured notification system gamit ang JSON-RPC protocol

- **Format ng Mensahe:**
  - Classic HTTP: Plain text na mga chunk na may newlines
  - MCP: Structured LoggingMessageNotification objects na may metadata

- **Pagpapatupad ng Kliyente:**
  - Classic HTTP: Simple client na nagpoproseso ng streaming responses
  - MCP: Mas sopistikadong client na may message handler para iproseso ang iba't ibang uri ng mensahe

- **Mga Update sa Progreso:**
  - Classic HTTP: Kasama ang progreso sa pangunahing response stream
  - MCP: Ipinapadala ang progreso sa pamamagitan ng hiwalay na mga notification message habang ang pangunahing tugon ay dumarating sa dulo

### Mga Rekomendasyon

May mga bagay na inirerekomenda namin kapag pumipili sa pagitan ng pagpapatupad ng klasikong streaming (bilang endpoint na ipinakita namin sa itaas gamit ang `/stream`) kumpara sa pagpili ng streaming sa pamamagitan ng MCP.

- **Para sa simpleng pangangailangan sa streaming:** Ang Classic HTTP streaming ay mas simple ipatupad at sapat na para sa mga basic na pangangailangan sa streaming.

- **Para sa komplikado, interactive na mga aplikasyon:** Ang MCP streaming ay nagbibigay ng mas istrukturadong paraan na may mas maraming metadata at paghahati sa pagitan ng notifications at final results.

- **Para sa AI na mga aplikasyon:** Ang notification system ng MCP ay partikular na kapaki-pakinabang para sa mga mahahabang AI tasks kung saan nais mong panatilihing updated ang mga gumagamit sa progreso.

## Streaming sa MCP

Sige, nakita mo na ang ilang rekomendasyon at paghahambing tungkol sa pagkakaiba ng klasikong streaming at streaming sa MCP. Tingnan natin nang mas detalyado kung paano mo magagamit ang streaming sa MCP.

Mahalaga ang pag-unawa kung paano gumagana ang streaming sa loob ng MCP framework para makabuo ng mga responsive na aplikasyon na nagbibigay ng real-time na feedback sa mga gumagamit habang tumatakbo ang mahahabang operasyon.

Sa MCP, hindi ito tungkol sa pagpapadala ng pangunahing tugon nang paunti-unti, kundi tungkol sa pagpapadala ng **notifications** sa kliyente habang ang isang tool ay nagpoproseso ng request. Ang mga notifications na ito ay maaaring maglaman ng mga update sa progreso, logs, o iba pang mga kaganapan.

### Paano ito gumagana

Ang pangunahing resulta ay ipinapadala pa rin bilang isang solong tugon. Gayunpaman, ang mga notifications ay maaaring ipadala bilang mga hiwalay na mensahe habang nagpapatuloy ang pagpoproseso at sa gayon ay ina-update ang kliyente sa real time. Dapat kayang hawakan at ipakita ng kliyente ang mga notifications na ito.

### Opsyonal na pagsasanay: kumonekta sa hosted na MCP server

Maaari mo ring gamitin ang Streamable HTTP nang hindi nagpapatakbo ng lokal na server. Ang halimbawang ito
ay kumokonekta sa [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
natutuklasan ang mga tool nito, at naghahanap ng pampublikong dokumentasyon ng MCP gamit ang parehong
Python SDK tulad ng [local client](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Ang anonymous endpoint ng Parallel ay hindi nangangailangan ng account o API key. Ang libreng access ay
rate limited. Ang pagpapatakbo ng script na ito ay nagsusumite ng mga query sa paghahanap, layunin, at isang
random session identifier sa Parallel. Nagbibigay din ang serbisyo ng `web_fetch`,
na nagsusumite ng mga hinihiling na URL at anumang ibinigay na konteksto sa Parallel. Gumamit ng pampublikong
impormasyon para sa pagsasanay na ito; tingnan ang mga [terms](https://parallel.ai/customer-terms)
at [privacy policy](https://parallel.ai/privacy-policy).

Sa Python 3.10 o mas bago at na-activate ang virtual environment, i-install ang SDK:

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

Asahan na kabilang sa natuklasan ang `web_search` at `web_fetch`, sinundan ng tugon sa paghahanap na naglalaman ng mga source URL at mga sipi. Maaaring magbago o maging walang laman ang mga resulta.
Sinusuri ng script ang `isError` dahil maaaring mabigo ang isang tool kahit matagumpay ang HTTP request.
Kung rate limited ang access, maghintay bago subukan muli. Gamitin muli ang parehong
`session_id` kung palalawigin mo ang script sa mga kaugnay na tawag sa paghahanap o pagkuha.


kumpletong JSON result nang walang mga notification sa progreso. Pinangangasiwaan ng SDK ang
transport. Magpatuloy sa lokal na halimbawa sa ibaba upang matutunan ang tungkol sa notifications.
Ginagawa ng opsyonal na script na ito ang isang malinaw na paghahanap at isinasara ang koneksyon kapag
natapos na. Kapag inilahad mo ang mga tool na ito sa isang ahente, maaaring gamitin ito ng ahente habang nagtatrabaho; ituring na hindi mapagkakatiwalaan ang nakuha na web text.

## Ano ang Notification?

Sinabi naming "Notification", ano ang ibig sabihin nito sa konteksto ng MCP?

Sinabi naming "Notification", ano ang ibig sabihin niyan sa konteksto ng MCP?

Ang isang notification ay isang JSON-RPC na mensahe na walang `id` at hindi
tumatanggap ng tugon. Ginagamit ng MCP ang mga notification para sa progreso, kanselasyon, at
iba pang one-way na mga pangyayari.

Sa MCP `2025-11-25`, ang client ay nagpapadala ng `notifications/initialized` pagkatapos ng
initialization handshake. Ang MCP `2026-07-28` ay walang initialization handshake, kaya
ang notification na ito ay legacy na pag-uugali.

Ang isang notification ay ganito ang hitsura bilang isang JSON na mensahe:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Ang logging ay isang tampok na gumagamit ng mga notification; ang mga notification mismo ay isang
pangkalahatang uri ng mensahe sa JSON-RPC.

> **Hindi na ginagamit sa MCP `2026-07-28`:** nananatiling available ang tampok ng Logging
> para sa pagiging compatible ngunit maaaring tanggalin sa unang rebisyon ng espesipikasyon
> na ilalabas sa o pagkatapos ng Hulyo 28, 2027. Ang mga bagong implementasyon ay dapat gumamit
> ng `stderr` kasama ang stdio o OpenTelemetry para sa structured na observability.

Para sa legacy na implementasyon ng `2025-11-25`, pinapagana ng server ang kakayahan ng Logging
bilang mga sumusunod:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Depende sa SDK na ginamit, maaaring awtomatikong naka-enable ang logging, o maaaring kailangan mong i-enable ito nang tahasan sa iyong server configuration.

May iba't ibang uri ng mga notification:

| Antas     | Paglalarawan                  | Halimbawa ng Paggamit          |
|-----------|------------------------------|-------------------------------|
| debug     | Detalyadong impormasyon para sa debugging | Mga entry/exit point ng function |
| info      | Pangkalahatang impormal na mga mensahe | Mga update sa progreso ng operasyon |
| notice    | Normal ngunit mahalagang mga pangyayari | Mga pagbabago sa configuration   |
| warning   | Mga kondisyon ng babala       | Paggamit ng deprecated na feature |
| error     | Mga kondisyon ng error        | Kabiguan sa operasyon           |
| critical  | Mga kritikal na kondisyon      | Kabiguan ng bahagi ng sistema   |
| alert     | Kailangang kumilos agad        | Natuklasan ang korapsyon ng data |
| emergency | Hindi magamit ang sistema      | Kumpletong kabiguan ng sistema  |

## Pagpapatupad ng Mga Notification sa MCP

Upang ipatupad ang mga notification sa MCP, kailangan mong ayusin ang parehong server at client upang humawak ng mga update sa real-time. Pinapayagan nito ang iyong aplikasyon na magbigay ng agarang tugon sa mga user habang tumatakbo ang mga mahahabang operasyon.

### Sa Panig ng Server: Pagpapadala ng Mga Notification

Magsimula tayo sa panig ng server. Sa MCP, nagtatakda ka ng mga kasangkapan na maaaring magpadala ng mga notification habang pinoproseso ang mga kahilingan. Ginagamit ng server ang context object (karaniwan ay `ctx`) upang magpadala ng mga mensahe sa client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Sa naunang halimbawa, ang kasangkapang `process_files` ay nagpapadala ng tatlong notification sa client habang pinoproseso ang bawat file. Ginagamit ang `ctx.info()` na pamamaraan para magpadala ng mga impormal na mensahe.

Dagdag pa rito, upang paganahin ang mga notification, siguraduhin na ang iyong server ay gumagamit ng streaming transport (tulad ng `streamable-http`) at ang iyong client ay may implementasyon ng message handler upang iproseso ang mga notification. Narito kung paano mo maitatakda ang server upang gamitin ang `streamable-http` na transport:

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

Sa halimbawang .NET na ito, ang kasangkapang `ProcessFiles` ay may dekorasyong `Tool` na attribute at nagpapadala ng tatlong notification sa client habang pinoproseso ang bawat file. Ginagamit ang pamamaraan na `ctx.Info()` para magpadala ng mga impormal na mensahe.

Upang paganahin ang mga notification sa iyong .NET MCP server, siguraduhin na gumagamit ka ng streaming transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Sa Panig ng Client: Pagtanggap ng Mga Notification

Dapat magpatupad ang kliyente ng isang tagapamahala ng mensahe upang iproseso at ipakita ang mga abiso habang dumarating ang mga ito.

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

Sa naunang code, sinusuri ng function na `message_handler` kung ang papasok na mensahe ay isang notification. Kung ito ay, ipi-print nito ang notification; kung hindi, ipoproseso ito bilang karaniwang mensahe mula sa server. Pansinin din kung paano ini-initialize ang `ClientSession` gamit ang `message_handler` upang hawakan ang mga papasok na notification.

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

Sa halimbawang ito sa .NET, sinusuri ng function na `MessageHandler` kung ang papasok na mensahe ay isang notification. Kung ito ay, ipi-print nito ang notification; kung hindi, ipoproseso ito bilang karaniwang mensahe mula sa server. Ang `ClientSession` ay ini-initialize gamit ang message handler sa pamamagitan ng `ClientSessionOptions`.

Upang paganahin ang mga notification, siguraduhing gumagamit ang iyong server ng streaming transport (tulad ng `streamable-http`) at ang iyong kliyente ay nagpatupad ng message handler para iproseso ang mga notification.

## Mga Notification ng Progreso at Mga Senaryo

Ipinaliwanag sa seksyong ito ang konsepto ng mga notification ng progreso sa MCP, bakit ito mahalaga, at paano ito ipinatutupad gamit ang Streamable HTTP. Makikita mo rin ang isang praktikal na gawain para palalimin ang iyong pag-unawa.

Ang mga notification ng progreso ay mga real-time na mensahe na ipinapadala mula sa server papunta sa kliyente habang may tumatakbong mga mahahabang operasyon. Sa halip na hintayin ang buong proseso na matapos, pinananatili ng server ang kliyente na na-update tungkol sa kasalukuyang kalagayan. Pinapabuti nito ang transparency, karanasan ng gumagamit, at ginagawang mas madali ang pag-debug.

**Halimbawa:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Bakit Gumamit ng Mga Notification ng Progreso?

Mahalagang gamitin ang mga notification ng progreso para sa mga sumusunod na dahilan:

- **Mas magandang karanasan ng gumagamit:** Nakikita ng mga gumagamit ang mga update habang nagpapatuloy ang trabaho, hindi lamang sa dulo.
- **Real-time na feedback:** Maaaring magpakita ang mga kliyente ng progress bar o log, na nagpaparamdam na responsive ang app.
- **Mas madaling pag-debug at pagmamanman:** Nakikita ng mga developer at gumagamit kung saan maaaring mabagal o ma-stuck ang isang proseso.

### Paano Magpatupad ng Mga Notification ng Progreso

Narito kung paano mo ipapatupad ang mga notification ng progreso sa MCP:

- **Sa server:** Gamitin ang `ctx.info()` o `ctx.log()` upang magpadala ng mga notification habang pinoproseso ang bawat item. Pinapadala nito ang mensahe sa kliyente bago handa ang pangunahing resulta.
- **Sa kliyente:** Magpatupad ng message handler na nakikinig at nagpapakita ng mga notification habang dumadaglat. Nakikilala ng handler na ito ang pagitan ng mga notification at ang panghuling resulta.

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

**Halimbawa ng Kliyente:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Mga Pagsasaalang-alang sa Seguridad

Dapat unahin ang seguridad kapag nagpapatupad ng anumang server, lalo na kung gumagamit ng HTTP-based transports tulad ng Streamable HTTP sa MCP.

Kapag nagpapatupad ng mga MCP server gamit ang HTTP-based transports, nagiging pangunahing alalahanin ang seguridad na nangangailangan ng maingat na pagtutok sa iba't ibang atake at mga mekanismo ng proteksyon.

### Pangkalahatang Pagsusuri

Kritikal ang seguridad kapag inilalantad ang mga MCP server sa HTTP. Nagdadala ang Streamable HTTP ng mga bagong surface ng atake at nangangailangan ng maingat na pagsasaayos.

Narito ang ilang mahahalagang pagsasaalang-alang sa seguridad:

- **Pagsusuri ng Origin Header**: Laging suriin ang `Origin` header upang maiwasan ang mga pag-atake sa DNS rebinding.
- **Localhost Binding**: Para sa lokal na pag-unlad, itali ang mga server sa `localhost` upang hindi ito maipakita sa pampublikong internet.
- **Authentication**: Magpatupad ng authentication (hal., API keys, OAuth) para sa mga production deployment.
- **CORS**: Isaayos ang mga polisiya sa Cross-Origin Resource Sharing (CORS) upang limitahan ang access.
- **HTTPS**: Gumamit ng HTTPS sa production upang i-encrypt ang trapiko.

### Mga Pinakamahusay na Kasanayan

Bukod dito, narito ang ilang pinakamahusay na kasanayan na dapat sundin kapag nagpapatupad ng seguridad sa iyong MCP streaming server:

- Huwag kailanman pagkatiwalaan ang mga papasok na kahilingan nang walang pagsusuri.
- Mag-log at subaybayan ang lahat ng pag-access at mga error.
- Regular na i-update ang mga dependency upang butasan ang mga kahinaan sa seguridad.

### Mga Hamon

Makakaharap ka ng ilang hamon kapag nagpapatupad ng seguridad sa mga MCP streaming server:

- Pagbabalanse ng seguridad at kadalian ng pag-develop
- Pagsisiguro ng compatibility sa iba't ibang mga client environment


## Pag-upgrade mula SSE patungong Streamable HTTP

Para sa mga aplikasyong kasalukuyang gumagamit ng Server-Sent Events (SSE), ang paglipat sa Streamable HTTP ay nagdudulot ng mas pinahusay na kakayahan at mas magandang pangmatagalang suporta para sa iyong mga implementasyon ng MCP.

### Bakit Mag-upgrade?

May dalawang malalakas na dahilan upang mag-upgrade mula SSE patungong Streamable HTTP:

- Nagbibigay ang Streamable HTTP ng mas mahusay na scalability, compatibility, at mas malawak na suporta sa notification kumpara sa SSE.
- Ito ang inirerekomendang transport para sa mga bagong MCP application.

### Mga Hakbang sa Migrasyon

Narito kung paano ka makakapag-migrate mula SSE patungong Streamable HTTP sa iyong mga MCP application:

- **I-update ang server code** upang gamitin ang `transport="streamable-http"` sa loob ng `mcp.run()`.
- **I-update ang client code** upang gamitin ang `streamablehttp_client` sa halip na SSE client.
- **Magpatupad ng message handler** sa kliyente para iproseso ang mga notification.
- **Subukan ang compatibility** gamit ang mga umiiral na tool at workflow.

### Pagpapanatili ng Compatibility

Inirerekomenda na panatilihin ang compatibility sa mga umiiral na SSE client habang isinasagawa ang migrasyon. Narito ang ilang estratehiya:

- Maaari mong suportahan ang parehong SSE at Streamable HTTP sa pamamagitan ng pagpapatakbo ng parehong transport sa magkaibang mga endpoint.
- Unti-unting i-migrate ang mga client sa bagong transport.

### Mga Hamon

Siguraduhing harapin ang mga sumusunod na hamon habang nagsasagawa ng migrasyon:

- Pagsisiguro na lahat ng client ay na-update
- Pagtugon sa pagkakaiba sa delivery ng notification

### Gawain: Gumawa ng Sariling Streaming MCP App

**Senaryo:**
Gumawa ng MCP server at client kung saan pinoproseso ng server ang listahan ng mga item (hal., mga file o dokumento) at nagpapadala ng notification para sa bawat item na naproseso. Dapat ipakita ng kliyente ang bawat notification habang dumarating ito.

**Mga Hakbang:**

1. Magpatupad ng tool sa server na nagpoproseso ng listahan at nagpapadala ng mga notification para sa bawat item.
2. Magpatupad ng client na may message handler upang ipakita ang mga notification nang real time.
3. Subukan ang iyong implementasyon sa pagpapatakbo ng parehong server at client, at obserbahan ang mga notification.

[Solution](./solution/README.md)

## Karagdagang Pagbabasa at Ano ang Susunod?

Upang ituloy ang iyong paglalakbay sa MCP streaming at palawakin pa ang iyong kaalaman, nagbibigay ang seksyong ito ng karagdagang mga mapagkukunan at mga mungkahing susunod na hakbang para sa paggawa ng mas advanced na mga aplikasyon.

### Karagdagang Pagbabasa

- [Microsoft: Panimula sa HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS sa ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Ano ang Susunod?

- Subukang gumawa ng mas advanced na MCP tools na gumagamit ng streaming para sa real-time analytics, chat, o collaborative editing.
- Tuklasin ang integrasyon ng MCP streaming sa mga frontend framework (React, Vue, atbp.) para sa mga live na update sa UI.
- Susunod: [Paggamit ng Microsoft Foundry Toolkit para sa Visual Studio Code](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->