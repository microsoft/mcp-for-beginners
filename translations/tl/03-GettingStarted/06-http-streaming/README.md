# HTTPS Streaming gamit ang Model Context Protocol (MCP)

Ang kabanatang ito ay nagbibigay ng komprehensibong gabay sa pagpapatupad ng ligtas, scalable, at real-time na streaming gamit ang Model Context Protocol (MCP) gamit ang HTTPS. Sinasaklaw nito ang motibasyon para sa streaming, mga available na mekanismo sa transportasyon, kung paano mag-implement ng streamable HTTP sa MCP, mga pinakamahusay na kasanayan sa seguridad, migrasyon mula sa SSE, at praktikal na gabay para sa pagbuo ng sarili mong streaming MCP na mga aplikasyon.

> **Tumingin sa hinaharap:** inilalarawan ng araling ito ang Streamable HTTP sa ilalim ng **MCP Specification 2025-11-25**, kung saan ang isang sesyon ay itinatag sa panahon ng `initialize` at naka-pin gamit ang `Mcp-Session-Id` header. Ang `2026-07-28` release candidate ay nag-aalis ng handshake at session ID nang tuluyan, na ginagawa ang bawat request na self-contained at maaaring i-route sa anumang server instance nang walang sticky sessions. Tingnan ang [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) para sa mga detalye.

## Mga Mekanismo sa Transportasyon at Streaming sa MCP

Tinutuklas ng seksyong ito ang iba't ibang mekanismo sa transportasyon na available sa MCP at ang kanilang papel sa pagpapahintulot ng streaming capabilities para sa real-time na komunikasyon sa pagitan ng mga kliyente at server.

### Ano ang Mekanismo sa Transportasyon?

Ang mekanismo sa transportasyon ay naglalarawan kung paano ipinagpapalitan ang data sa pagitan ng kliyente at server. Sinusuportahan ng MCP ang maraming uri ng transportasyon upang umangkop sa iba't ibang kapaligiran at pangangailangan:

- **stdio**: Standard input/output, angkop para sa lokal at CLI-based na mga tool. Simple ngunit hindi angkop para sa web o cloud.
- **SSE (Server-Sent Events)**: Pinapayagan ang mga server na mag-push ng real-time na updates sa mga kliyente sa ibabaw ng HTTP. Maganda para sa mga web UI, ngunit limitado sa scalability at flexibility. Simula sa MCP Specification 2025-06-18, ang standalone na SSE (Server-Sent Events) transport ay pinalitan at itinigil na, pinalitan ng "Streamable HTTP" transport.
- **Streamable HTTP**: Modernong HTTP-based streaming transport, sumusuporta sa notifications at mas mahusay na scalability. Inirerekomenda para sa karamihan ng produksyon at cloud scenarios.

### Talaan ng Pagkukumpara

Tingnan ang talahanayan ng pagkukumpara sa ibaba upang maunawaan ang mga pagkakaiba sa pagitan ng mga mekanismong ito ng transportasyon:

| Transport         | Real-time Updates | Streaming | Scalability | Use Case                |
|-------------------|------------------|-----------|-------------|-------------------------|
| stdio             | Hindi            | Hindi     | Mababa      | Lokal na CLI tools       |
| SSE               | Oo               | Oo        | Katamtaman  | Web, real-time updates  |
| Streamable HTTP   | Oo               | Oo        | Mataas      | Cloud, multi-client     |

> **Tip:** Ang pagpili ng tamang transport ay nakakaapekto sa performance, scalability, at karanasan ng user. Inirerekomenda ang **Streamable HTTP** para sa mga modern, scalable, at cloud-ready na mga aplikasyon.

Tandaan ang mga transport na stdio at SSE na ipinakita sa iyo sa mga nakaraang kabanata at kung paano ang streamable HTTP ang transport na tinalakay sa kabanatang ito.

## Streaming: Mga Konsepto at Motibasyon

Mahalagang maunawaan ang mga pangunahing konsepto at motibasyon sa likod ng streaming para sa epektibong pagpapatupad ng mga real-time na sistema ng komunikasyon.

**Streaming** ay isang teknik sa network programming na nagpapahintulot na maipadala at matanggap ang data sa maliliit, mahahawakang piraso o bilang isang sunod-sunod ng mga kaganapan, sa halip na maghintay na maging handa ang buong tugon. Ito ay kapaki-pakinabang lalo na para sa:

- Malalaking file o datasets.
- Real-time updates (hal., chat, progress bars).
- Mahahabang computations kung saan nais mong ipaalam sa user ang progreso.

Narito ang mga dapat mong malaman tungkol sa streaming sa mataas na antas:

- Ang data ay ipinapadala nang paunti-unti, hindi sabay-sabay.
- Maaaring iproseso ng kliyente ang data habang dumarating ito.
- Nakabawas sa perceived latency at nagpapabuti ng karanasan ng user.

### Bakit gamitin ang streaming?

Narito ang mga dahilan sa paggamit ng streaming:

- Nakakatanggap agad ang mga user ng feedback, hindi lamang sa dulo.
- Nagbibigay-daan sa mga real-time application at responsive UI.
- Mas epektibong paggamit ng network at compute resources.

### Simpleng Halimbawa: HTTP Streaming Server & Client

Narito ang isang simpleng halimbawa kung paano maaring maisagawa ang streaming:

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

Ipinapakita ng halimbawa na ito ang isang server na nagpapadala ng serye ng mga mensahe sa kliyente habang magagamit na ang mga ito, sa halip na maghintay na maging handa ang lahat ng mga mensahe.

**Paano ito gumagana:**

- Ang server ay nagbibigay ng bawat mensahe kapag handa na ito.
- Tinatanggap at ipiniprint ng kliyente ang bawat piraso habang dumarating.

**Mga Kinakailangan:**

- Dapat gumamit ang server ng streaming response (hal., `StreamingResponse` sa FastAPI).
- Dapat iproseso ng kliyente ang response bilang stream (`stream=True` sa requests).
- Karaniwang `Content-Type` ay `text/event-stream` o `application/octet-stream`.

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
- `ServerSentEvent` ay nagbibigay ng structured event streaming na may mga uri ng event
- `WebClient` gamit ang `bodyToFlux()` ay nagpapahintulot ng reactive streaming consumption
- `delayElements()` ay nagsusimulang ng processing time sa pagitan ng mga event
- Puwedeng magkaroon ng mga uri ang mga event (`info`, `result`) para sa mas mahusay na paghawak ng kliyente

### Paghahambing: Classic Streaming vs MCP Streaming

Ang mga pagkakaiba sa kung paano gumagana ang streaming sa "klasikong" paraan kumpara sa paraan ng MCP ay maaaring ilarawan ng ganito:

| Katangian             | Classic HTTP Streaming         | MCP Streaming (Mga Notipikasyon)   |
|-----------------------|-------------------------------|-------------------------------------|
| Pangunahing tugon      | Chunked                       | Isa lang, sa dulo                   |
| Mga update ng progreso | Ipinadala bilang mga piraso   | Ipinadala bilang mga notipikasyon   |
| Kinakailangan ng kliyente | Dapat iproseso ang stream     | Dapat mag-implement ng message handler |
| Gamitin para sa        | Malalaking files, AI token streams | Progreso, logs, real-time feedback  |

### Mga Pangunahing Pagkakaiba na Napansin

Bukod dito, narito ang ilang pangunahing mga pagkakaiba:

- **Pattern ng Komunikasyon:**
  - Classic HTTP streaming: Gumagamit ng simpleng chunked transfer encoding para magpadala ng data sa mga piraso
  - MCP streaming: Gumagamit ng structured notification system gamit ang JSON-RPC protocol

- **Format ng Mensahe:**
  - Classic HTTP: Plain text chunks na may mga bagong linya
  - MCP: Structured LoggingMessageNotification objects na may metadata

- **Implementasyon ng Kliyente:**
  - Classic HTTP: Simpleng kliyente na nagpoproseso ng streaming responses
  - MCP: Mas sopistikadong kliyente na may message handler para iproseso ang iba't ibang uri ng mensahe

- **Mga Update ng Progreso:**
  - Classic HTTP: Bahagi ng pangunahing stream ng tugon ang progreso
  - MCP: Ipinapadala ang progreso sa pamamagitan ng hiwalay na mga notification habang ang pangunahing tugon ay dumarating sa dulo

### Mga Rekomendasyon

Narito ang ilang bagay na inirerekomenda namin kapag pumipili sa pagitan ng pagpapatupad ng klasikong streaming (bilang isang endpoint na ipinakita namin sa itaas gamit ang `/stream`) kumpara sa pagpili ng streaming sa pamamagitan ng MCP.

- **Para sa simpleng pangangailangan sa streaming:** Mas madali ang Classic HTTP streaming i-implementa at sapat na para sa simpleng pangangailangan.

- **Para sa kumplikado, interactive na aplikasyon:** Nagbibigay ang MCP streaming ng mas structured na paraan na may mas mayamang metadata at paghihiwalay sa pagitan ng mga notipikasyon at mga huling resulta.

- **Para sa mga aplikasyon ng AI:** Lalo na kapaki-pakinabang ang sistema ng notipikasyon ng MCP para sa mga mahahabang AI tasks na nais mong ipaalam sa mga user ang progreso.

## Streaming sa MCP

Ok, nakita mo na ang ilang rekomendasyon at paghahambing tungkol sa pagkakaiba ng klasikong streaming at streaming sa MCP. Tingnan natin nang detalyado kung paano mo magagamit ang streaming sa MCP.

Mahalagang maunawaan kung paano gumagana ang streaming sa loob ng MCP framework upang makabuo ng mga responsive na aplikasyon na nagbibigay ng real-time na feedback sa mga user habang nagpapatakbo ng mahahabang operasyon.

Sa MCP, ang streaming ay hindi tungkol sa pagpapadala ng pangunahing tugon sa mga piraso, kundi tungkol sa pagpapadala ng **mga notipikasyon** sa kliyente habang nagpapatakbo ang isang tool ng request. Maaaring kasama sa mga notipikasyong ito ang mga update sa progreso, logs, o iba pang mga kaganapan.

### Paano ito gumagana

Ang pangunahing resulta ay ipinapadala pa rin bilang isang tugon. Gayunpaman, maaaring ipadala ang mga notipikasyon bilang hiwalay na mga mensahe habang nagpapatuloy ang pagproseso na nag-a-update sa kliyente sa real time. Dapat marunong mag-handle at mag-display ng mga notipikasyong ito ang kliyente.

## Ano ang Notipikasyon?

Sinabi nating "Notipikasyon", ano ang ibig sabihin nito sa konteksto ng MCP?

Ang notipikasyon ay isang mensahe na ipinapadala mula server papunta sa kliyente upang ipaalam ang progreso, status, o iba pang mga kaganapan habang nagpapatakbo ng mahahabang operasyon. Pinapabuti ng mga notipikasyon ang transparency at karanasan ng user.

Halimbawa, inaasahang magpadala ang kliyente ng notipikasyon kapag nagawa na ang initial handshake sa server.

Ang isang notipikasyon ay ganito ang hitsura bilang isang JSON message:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Ang mga notipikasyon ay kabilang sa isang topic sa MCP na tinatawag na ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Paunawa sa Pagtigil:** Ang `2026-07-28` MCP specification release candidate ay nagmamarka na ng pagtigil sa primitive Logging pabor sa `stderr` para sa stdio transports at OpenTelemetry para sa structured observability. Patuloy na gagana ang Logging sa `2025-11-25` at sa loob ng hindi bababa sa isang taon matapos ang anumang pormal na pagtigil. Tingnan ang [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

Upang mapagana ang logging, kailangang i-enable ito ng server bilang feature o kakayahan tulad nito:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Depende sa SDK na ginamit, maaaring naka-enable na ang logging bilang default, o kinakailangan mong i-enable ito nang hayagan sa iyong server configuration.

May iba't ibang uri ng mga notipikasyon:

| Antas      | Paglalarawan                  | Halimbawa ng Paggamit          |
|------------|------------------------------|-------------------------------|
| debug      | Detalyadong impormasyon para sa debugging | Mga punto ng pagpasok/paglabas ng function |
| info       | Pangkalahatang impormasyong mensahe | Mga update sa progreso ng operasyon |
| notice     | Normal ngunit makabuluhang mga kaganapan | Mga pagbabago sa configuration |
| warning    | Kondisyon na nagbibigay babala | Paggamit ng deprecated na feature |
| error      | Kondisyon ng error            | Mga pagkabigo ng operasyon     |
| critical   | Kritikal na kondisyon         | Mga pagkabigo ng bahagi ng sistema |
| alert      | Kailangang kumilos agad       | Natuklasang corruption ng data |
| emergency  | Hindi na magamit ang sistema  | Kumpletong pagkasira ng sistema |

## Pagpapatupad ng Mga Notipikasyon sa MCP

Upang magpatupad ng mga notipikasyon sa MCP, kailangan mong isaayos ang parehong server at client na mga bahagi upang hawakan ang real-time updates. Pinapayagan ng ito ang iyong aplikasyon na magbigay ng agarang feedback sa mga user habang nagpapatakbo ng mahahabang operasyon.

### Sa server: Pagpapadala ng Mga Notipikasyon

Simulan natin sa bahagi ng server. Sa MCP, nagdedefine ka ng mga tool na maaaring magpadala ng mga notipikasyon habang pinoproseso ang mga request. Ginagamit ng server ang context object (karaniwang `ctx`) para magpadala ng mga mensahe sa kliyente.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Sa naunang halimbawa, ang tool na `process_files` ay nagpapadala ng tatlong notipikasyon sa kliyente habang pinoproseso ang bawat file. Ginagamit ang `ctx.info()` method para magpadala ng mga impormal na mensahe.

Bilang karagdagan, upang paganahin ang mga notipikasyon, siguraduhin na ang iyong server ay gumagamit ng streaming transport (tulad ng `streamable-http`) at ang iyong kliyente ay mayroong message handler para iproseso ang mga notipikasyon. Narito kung paano mo maaaring isaayos ang server para gamitin ang `streamable-http` na transport:

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

Sa halimbawang .NET na ito, ang tool na `ProcessFiles` ay may dekorasyon na `Tool` attribute at nagpapadala ng tatlong notipikasyon sa kliyente habang pinoproseso ang bawat file. Ginagamit ang `ctx.Info()` method upang magpadala ng mga impormal na mensahe.

Upang paganahin ang mga notipikasyon sa iyong .NET MCP server, siguraduhin na gumagamit ka ng streaming transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Sa kliyente: Pagtanggap ng Mga Notipikasyon

Dapat mag-implementa ang kliyente ng message handler upang iproseso at ipakita ang mga notipikasyon habang dumarating ang mga ito.

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

Sa code na ito, sinusuri ng `message_handler` function kung ang paparating na mensahe ay isang notipikasyon. Kung oo, ipiprint nito ang notipikasyon; kung hindi, ipoproseso ito bilang isang regular na mensahe mula sa server. Pansinin din kung paano ini-initialize ang `ClientSession` sa `message_handler` upang hawakan ang mga paparating na notipikasyon.

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

Sa halimbawang .NET na ito, sinusuri ng `MessageHandler` function kung ang paparating na mensahe ay isang notipikasyon. Kung oo, ipiprint nito ang notipikasyon; kung hindi, ipoproseso ito bilang isang regular na mensahe mula sa server. Ang `ClientSession` ay ini-initialize gamit ang message handler sa pamamagitan ng `ClientSessionOptions`.

Upang paganahin ang mga notipikasyon, siguraduhin na ang iyong server ay gumagamit ng streaming transport (tulad ng `streamable-http`) at ang iyong kliyente ay may message handler upang iproseso ang mga notipikasyon.

## Mga Notipikasyon ng Progreso at mga Scenario

Ipinaliwanag sa seksyong ito ang konsepto ng mga notipikasyon ng progreso sa MCP, bakit ito mahalaga, at kung paano ito ipinatutupad gamit ang Streamable HTTP. Makakakita ka rin ng isang praktikal na takdang-aralin upang palalimin ang iyong pag-unawa.

Ang mga notipikasyon ng progreso ay mga real-time na mensahe na ipinapadala mula server papunta sa kliyente habang nagpapatakbo ng mahahabang operasyon. Sa halip na maghintay na matapos ang buong proseso, inaalagaan ng server ang kliyente na updated tungkol sa kasalukuyang estado. Pinapabuti nito ang transparency, karanasan ng user, at nagpapadali sa pag-debug.

**Halimbawa:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Bakit Gamitin ang Mga Notipikasyon ng Progreso?

Mahalaga ang mga notipikasyon ng progreso para sa ilang kadahilanan:

- **Mas mahusay na karanasan ng user:** Nakikita ng mga user ang mga update habang umuusad ang trabaho, hindi lamang sa dulo.
- **Real-time na feedback:** Maaaring magpakita ang kliyente ng mga progress bar o logs, na nagpaparamdam na responsive ang app.
- **Mas madali ang debugging at monitoring:** Nakikita ng mga developer at user kung saan maaaring mabagal o maipit ang proseso.

### Paano Ipatupad ang Mga Notipikasyon ng Progreso

Narito kung paano mo maipapatupad ang mga notipikasyon ng progreso sa MCP:

- **Sa server:** Gumamit ng `ctx.info()` o `ctx.log()` para magpadala ng mga notipikasyon habang pinoproseso ang bawat item. Nagpapadala ito ng mensahe sa kliyente bago maging handa ang pangunahing resulta.
- **Sa kliyente:** Mag-implementa ng message handler na nakikinig at nagpapakita ng mga notipikasyon habang dumarating. Nakikilala ng handler na ito ang pagkakaiba ng mga notipikasyon at ng huling resulta.

**Halimbawa para sa Server:**


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

Ang seguridad ay dapat maging pangunahing prayoridad kapag nagpapatupad ng anumang server, lalo na kapag gumagamit ng mga HTTP-based na transport tulad ng Streamable HTTP sa MCP.

Kapag nagpapatupad ng mga MCP server na may HTTP-based na mga transport, ang seguridad ay nagiging napakahalagang alalahanin na nangangailangan ng maingat na atensyon sa maraming attack vectors at mga mekanismo ng proteksyon.

### Pangkalahatang Tanaw

Kritikal ang seguridad kapag inilalantad ang mga MCP server sa pamamagitan ng HTTP. Nagbibigay ang Streamable HTTP ng mga bagong attack surfaces at nangangailangan ng maingat na pagsasaayos.

Narito ang ilang mahahalagang pagsasaalang-alang sa seguridad:

- **Pag-validate ng Origin Header**: Laging pag-validate ng `Origin` header upang maiwasan ang DNS rebinding attacks.
- **Localhost Binding**: Para sa lokal na pag-develop, i-bind ang mga server sa `localhost` upang maiwasang ma-expose ang mga ito sa pampublikong internet.
- **Authentication**: Magpatupad ng authentication (hal., API keys, OAuth) para sa production deployments.
- **CORS**: Isaayos ang Cross-Origin Resource Sharing (CORS) policies upang limitahan ang access.
- **HTTPS**: Gumamit ng HTTPS sa production upang i-encrypt ang traffic.

### Mga Pinakamahuhusay na Gawain

Bukod pa rito, narito ang ilang pinakamahusay na gawain na sundin kapag nagpapatupad ng seguridad sa iyong MCP streaming server:

- Huwag kailanman pagkatiwalaan ang mga papasok na request nang walang pag-validate.
- I-log at imonitor ang lahat ng access at mga error.
- Regular na i-update ang dependencies upang mai-patch ang mga kahinaan sa seguridad.

### Mga Hamon

Makakaharap ka ng ilang hamon kapag nagpapatupad ng seguridad sa MCP streaming servers:

- Pagtutugma ng seguridad sa pagiging madali ng pag-develop
- Pagtiyak ng compatibility sa iba't ibang kapaligiran ng kliyente


## Pag-upgrade mula SSE papuntang Streamable HTTP

Para sa mga aplikasyon na kasalukuyang gumagamit ng Server-Sent Events (SSE), ang paglipat sa Streamable HTTP ay nagbibigay ng mas pinahusay na kakayahan at mas magandang pangmatagalang pangangalaga para sa iyong mga implementasyon ng MCP.

### Bakit Mag-upgrade?

May dalawang malakas na dahilan para mag-upgrade mula SSE papuntang Streamable HTTP:

- Nag-aalok ang Streamable HTTP ng mas mahusay na scalability, compatibility, at mas mayaman na suporta sa notipikasyon kaysa SSE.
- Ito ang inirerekomendang transport para sa mga bagong MCP applications.

### Mga Hakbang sa Migrasyon

Ganito mo maaaring ilipat mula SSE papuntang Streamable HTTP sa iyong MCP applications:

- **I-update ang server code** para gamitin ang `transport="streamable-http"` sa `mcp.run()`.
- **I-update ang client code** upang gamitin ang `streamablehttp_client` imbes na SSE client.
- **Magpatupad ng message handler** sa client para iproseso ang mga notipikasyon.
- **Subukan ang compatibility** gamit ang mga umiiral na tool at workflows.

### Pagpapanatili ng Compatibility

Inirerekomenda na panatilihin ang compatibility sa umiiral na mga SSE client habang isinasagawa ang migrasyon. Narito ang ilang mga estratehiya:

- Maaari mong suportahan ang parehong SSE at Streamable HTTP sa pamamagitan ng pagpapatakbo ng parehong transport sa magkahiwalay na mga endpoint.
- Unang unahin ang progresibong paglilipat ng mga client sa bagong transport.

### Mga Hamon

Tiyakin mong matugunan ang mga sumusunod na hamon habang ginagawa ang migrasyon:

- Pagtiyak na lahat ng client ay na-update
- Paghahandle sa mga pagkakaiba sa paghahatid ng notipikasyon

### Takdang-Aralin: Gumawa ng Sariling Streaming MCP App

**Eksena:**
Gumawa ng MCP server at client kung saan ang server ay nagpapatakbo ng isang listahan ng mga item (hal., mga files o dokumento) at nagpapadala ng notipikasyon para sa bawat item na naproseso. Dapat ipakita ng kliyente ang bawat notipikasyon habang dumadating ito.

**Mga Hakbang:**

1. Magpatupad ng tool sa server na nagpapatakbo ng listahan at nagpapadala ng notipikasyon para sa bawat item.
2. Magpatupad ng client na may message handler upang ipakita ang mga notipikasyon sa real time.
3. Subukan ang implementasyon sa pamamagitan ng pagpapatakbo ng parehong server at client, at tingnan ang mga notipikasyon.

[Solusyon](./solution/README.md)

## Karagdagang Pagbabasa & Ano ang Susunod?

Upang ipagpatuloy ang iyong paglalakbay sa MCP streaming at palawakin ang iyong kaalaman, nagbibigay ang seksyong ito ng karagdagang mga sanggunian at mga mungkahing susunod na hakbang para makabuo ng mas advanced na mga aplikasyon.

### Karagdagang Pagbabasa

- [Microsoft: Panimula sa HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS sa ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Ano ang Susunod?

- Subukang gumawa ng mas advanced na MCP tools na gumagamit ng streaming para sa real-time analytics, chat, o kolaboratibong pag-edit.
- Suriing maisama ang MCP streaming sa mga frontend framework (React, Vue, atbp.) para sa live UI updates.
- Susunod: [Paggamit ng AI Toolkit para sa VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->