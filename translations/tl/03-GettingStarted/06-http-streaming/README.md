# HTTPS Streaming gamit ang Model Context Protocol (MCP)

Ang kabanatang ito ay nagbibigay ng detalyadong gabay sa pag-implement ng ligtas, scalable, at real-time na streaming gamit ang Model Context Protocol (MCP) sa pamamagitan ng HTTPS. Saklaw nito ang motibasyon para sa streaming, ang mga magagamit na transport mechanisms, kung paano mag-implement ng streamable HTTP sa MCP, mga pinakamahusay na kasanayan sa seguridad, paglipat mula sa SSE, at praktikal na gabay para sa paggawa ng sarili mong streaming MCP applications.

## Transport Mechanisms at Streaming sa MCP

Ang seksyong ito ay tumatalakay sa iba't ibang transport mechanisms na magagamit sa MCP at ang kanilang papel sa pagpapagana ng streaming capabilities para sa real-time na komunikasyon sa pagitan ng mga kliyente at server.

### Ano ang Transport Mechanism?

Ang transport mechanism ay tumutukoy kung paano ipinapasa ang data sa pagitan ng kliyente at server. Sinusuportahan ng MCP ang iba't ibang uri ng transport upang umangkop sa iba't ibang kapaligiran at pangangailangan:

- **stdio**: Standard input/output, angkop para sa lokal at CLI-based na tools. Simple ngunit hindi angkop para sa web o cloud.
- **SSE (Server-Sent Events)**: Pinapayagan ang mga server na mag-push ng real-time updates sa mga kliyente gamit ang HTTP. Maganda para sa web UIs, ngunit limitado sa scalability at flexibility.
- **Streamable HTTP**: Modernong HTTP-based streaming transport, sumusuporta sa notifications at mas mahusay na scalability. Inirerekomenda para sa karamihan ng production at cloud scenarios.

### Talahanayan ng Paghahambing

Tingnan ang talahanayan ng paghahambing sa ibaba upang maunawaan ang mga pagkakaiba sa pagitan ng mga transport mechanisms:

| Transport         | Real-time Updates | Streaming | Scalability | Gamit                  |
|-------------------|------------------|-----------|-------------|-------------------------|
| stdio             | Hindi            | Hindi     | Mababa      | Lokal na CLI tools      |
| SSE               | Oo               | Oo        | Katamtaman  | Web, real-time updates  |
| Streamable HTTP   | Oo               | Oo        | Mataas      | Cloud, multi-client     |

> **Tip:** Ang tamang pagpili ng transport ay nakakaapekto sa performance, scalability, at user experience. **Streamable HTTP** ang inirerekomenda para sa modernong, scalable, at cloud-ready na applications.

Tandaan ang transports na stdio at SSE na tinalakay sa mga nakaraang kabanata at kung paano ang streamable HTTP ang transport na saklaw sa kabanatang ito.

## Streaming: Mga Konsepto at Motibasyon

Ang pag-unawa sa mga pangunahing konsepto at motibasyon sa likod ng streaming ay mahalaga para sa pag-implement ng epektibong real-time na communication systems.

**Streaming** ay isang teknik sa network programming na nagpapahintulot sa data na maipadala at matanggap sa maliliit na bahagi o bilang isang serye ng mga event, sa halip na hintayin ang buong response na maging handa. Ito ay partikular na kapaki-pakinabang para sa:

- Malalaking file o datasets.
- Real-time updates (hal., chat, progress bars).
- Mahabang computations kung saan nais mong panatilihing updated ang user.

Narito ang mga dapat mong malaman tungkol sa streaming sa mataas na antas:

- Ang data ay naihahatid nang paunti-unti, hindi sabay-sabay.
- Ang kliyente ay maaaring magproseso ng data habang ito ay dumarating.
- Binabawasan ang perceived latency at pinapabuti ang user experience.

### Bakit gumamit ng streaming?

Narito ang mga dahilan para gumamit ng streaming:

- Agad na nakakatanggap ng feedback ang mga user, hindi lamang sa dulo.
- Pinapagana ang real-time applications at responsive UIs.
- Mas epektibong paggamit ng network at compute resources.

### Simpleng Halimbawa: HTTP Streaming Server at Client

Narito ang isang simpleng halimbawa kung paano ma-implement ang streaming:

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

Ang halimbawang ito ay nagpapakita ng server na nagpapadala ng serye ng mga mensahe sa kliyente habang ang mga ito ay nagiging available, sa halip na hintayin ang lahat ng mensahe na maging handa.

**Paano ito gumagana:**

- Ang server ay naglalabas ng bawat mensahe habang ito ay handa na.
- Ang kliyente ay tumatanggap at nagpi-print ng bawat chunk habang ito ay dumarating.

**Mga Pangangailangan:**

- Ang server ay dapat gumamit ng streaming response (hal., `StreamingResponse` sa FastAPI).
- Ang kliyente ay dapat magproseso ng response bilang stream (`stream=True` sa requests).
- Ang Content-Type ay karaniwang `text/event-stream` o `application/octet-stream`.

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

- Gumagamit ng reactive stack ng Spring Boot gamit ang `Flux` para sa streaming.
- Ang `ServerSentEvent` ay nagbibigay ng structured event streaming na may event types.
- Ang `WebClient` na may `bodyToFlux()` ay nagpapagana ng reactive streaming consumption.
- Ang `delayElements()` ay nagsisimula ng processing time sa pagitan ng mga event.
- Ang mga event ay maaaring magkaroon ng types (`info`, `result`) para sa mas mahusay na handling ng kliyente.

### Paghahambing: Classic Streaming vs MCP Streaming

Ang mga pagkakaiba sa pagitan ng kung paano gumagana ang streaming sa "klasikal" na paraan kumpara sa kung paano ito gumagana sa MCP ay maaaring ilarawan tulad nito:

| Tampok                | Classic HTTP Streaming         | MCP Streaming (Notifications)      |
|------------------------|-------------------------------|-------------------------------------|
| Pangunahing response   | Chunked                       | Single, sa dulo                    |
| Progress updates       | Ipinapadala bilang data chunks | Ipinapadala bilang notifications   |
| Pangangailangan ng kliyente | Dapat magproseso ng stream | Dapat mag-implement ng message handler |
| Gamit                  | Malalaking file, AI token streams | Progress, logs, real-time feedback |

### Mga Napansing Pagkakaiba

Dagdag pa, narito ang ilang pangunahing pagkakaiba:

- **Pattern ng Komunikasyon:**
  - Classic HTTP streaming: Gumagamit ng simpleng chunked transfer encoding para magpadala ng data sa chunks.
  - MCP streaming: Gumagamit ng structured notification system na may JSON-RPC protocol.

- **Format ng Mensahe:**
  - Classic HTTP: Plain text chunks na may newlines.
  - MCP: Structured LoggingMessageNotification objects na may metadata.

- **Implementasyon ng Kliyente:**
  - Classic HTTP: Simpleng kliyente na nagpoproseso ng streaming responses.
  - MCP: Mas sopistikadong kliyente na may message handler para magproseso ng iba't ibang uri ng mensahe.

- **Progress Updates:**
  - Classic HTTP: Ang progress ay bahagi ng pangunahing response stream.
  - MCP: Ang progress ay ipinapadala sa pamamagitan ng hiwalay na notification messages habang ang pangunahing response ay dumarating sa dulo.

### Mga Rekomendasyon

Narito ang ilang rekomendasyon pagdating sa pagpili sa pagitan ng pag-implement ng klasikong streaming (bilang endpoint na ipinakita sa iyo sa itaas gamit ang `/stream`) kumpara sa pagpili ng streaming sa pamamagitan ng MCP.

- **Para sa simpleng pangangailangan sa streaming:** Ang klasikong HTTP streaming ay mas simple i-implement at sapat para sa mga basic na pangangailangan sa streaming.

- **Para sa mas kumplikado at interactive na applications:** Ang MCP streaming ay nagbibigay ng mas structured na approach na may mas mayamang metadata at paghihiwalay sa pagitan ng notifications at final results.

- **Para sa AI applications:** Ang notification system ng MCP ay partikular na kapaki-pakinabang para sa mahahabang AI tasks kung saan nais mong panatilihing updated ang mga user tungkol sa progress.

## Streaming sa MCP

Ok, nakita mo na ang ilang rekomendasyon at paghahambing tungkol sa pagkakaiba ng klasikong streaming at streaming sa MCP. Tingnan natin nang mas detalyado kung paano mo magagamit ang streaming sa MCP.

Ang pag-unawa kung paano gumagana ang streaming sa loob ng MCP framework ay mahalaga para sa paggawa ng responsive applications na nagbibigay ng real-time feedback sa mga user habang may mahahabang operasyon.

Sa MCP, ang streaming ay hindi tungkol sa pagpapadala ng pangunahing response sa chunks, kundi tungkol sa pagpapadala ng **notifications** sa kliyente habang ang isang tool ay nagpoproseso ng request. Ang mga notifications na ito ay maaaring maglaman ng progress updates, logs, o iba pang events.

### Paano ito gumagana

Ang pangunahing resulta ay ipinapadala pa rin bilang isang single response. Gayunpaman, ang mga notifications ay maaaring ipadala bilang hiwalay na mga mensahe habang nagpoproseso, kaya't na-update ang kliyente nang real-time. Ang kliyente ay dapat na may kakayahang mag-handle at mag-display ng mga notifications na ito.

## Ano ang Notification?

Sinabi naming "Notification", ano ang ibig sabihin nito sa konteksto ng MCP?

Ang notification ay isang mensahe na ipinapadala mula sa server patungo sa kliyente upang magbigay ng impormasyon tungkol sa progress, status, o iba pang events habang may mahahabang operasyon. Ang notifications ay nagpapabuti sa transparency at user experience.

Halimbawa, ang kliyente ay dapat magpadala ng notification kapag ang initial handshake sa server ay nagawa na.

Ang notification ay ganito ang hitsura bilang JSON message:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Ang notifications ay kabilang sa isang topic sa MCP na tinatawag na ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

Para gumana ang logging, kailangang i-enable ng server ito bilang feature/capability tulad nito:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Depende sa SDK na ginagamit, maaaring naka-enable na ang logging bilang default, o maaaring kailangan mong i-enable ito nang tahasan sa iyong server configuration.

May iba't ibang uri ng notifications:

| Level     | Deskripsyon                  | Halimbawa ng Gamit              |
|-----------|-------------------------------|---------------------------------|
| debug     | Detalyadong debugging information | Function entry/exit points      |
| info      | Pangkalahatang impormasyon    | Operation progress updates      |
| notice    | Normal ngunit mahalagang events | Configuration changes           |
| warning   | Mga kondisyon ng babala       | Deprecated feature usage        |
| error     | Mga kondisyon ng error        | Operation failures              |
| critical  | Mga kritikal na kondisyon     | System component failures       |
| alert     | Kailangang agad na aksyon     | Data corruption detected        |
| emergency | Hindi magagamit ang sistema   | Complete system failure         |

## Pag-implement ng Notifications sa MCP

Para mag-implement ng notifications sa MCP, kailangan mong i-set up ang parehong server at client sides upang mag-handle ng real-time updates. Pinapayagan nito ang iyong application na magbigay ng agarang feedback sa mga user habang may mahahabang operasyon.

### Server-side: Pagpapadala ng Notifications

Simulan natin sa server side. Sa MCP, nagde-define ka ng tools na maaaring magpadala ng notifications habang nagpoproseso ng requests. Ang server ay gumagamit ng context object (karaniwang `ctx`) para magpadala ng mga mensahe sa kliyente.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

Sa naunang halimbawa, ang `process_files` tool ay nagpapadala ng tatlong notifications sa kliyente habang nagpoproseso ng bawat file. Ang `ctx.info()` method ay ginagamit para magpadala ng informational messages.

Dagdag pa, para ma-enable ang notifications, tiyakin na ang iyong server ay gumagamit ng streaming transport (tulad ng `streamable-http`) at ang iyong kliyente ay nag-implement ng message handler para magproseso ng notifications. Narito kung paano mo ma-set up ang server para gumamit ng `streamable-http` transport:

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

Sa .NET na halimbawa, ang `ProcessFiles` tool ay may dekorasyon na `Tool` attribute at nagpapadala ng tatlong notifications sa kliyente habang nagpoproseso ng bawat file. Ang `ctx.Info()` method ay ginagamit para magpadala ng informational messages.

Para ma-enable ang notifications sa iyong .NET MCP server, tiyakin na gumagamit ka ng streaming transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Client-side: Pagtanggap ng Notifications

Ang kliyente ay dapat mag-implement ng message handler para magproseso at mag-display ng notifications habang dumarating ang mga ito.

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

Sa naunang code, ang `message_handler` function ay nagche-check kung ang incoming message ay notification. Kung ito ay notification, ipinapakita ito; kung hindi, pinoproseso ito bilang regular na server message. Pansinin din kung paano ang `ClientSession` ay na-initialize gamit ang `message_handler` para mag-handle ng incoming notifications.

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

Sa .NET na halimbawa, ang `MessageHandler` function ay nagche-check kung ang incoming message ay notification. Kung ito ay notification, ipinapakita ito; kung hindi, pinoproseso ito bilang regular na server message. Ang `ClientSession` ay na-initialize gamit ang message handler sa pamamagitan ng `ClientSessionOptions`.

Para ma-enable ang notifications, tiyakin na ang iyong server ay gumagamit ng streaming transport (tulad ng `streamable-http`) at ang iyong kliyente ay nag-implement ng message handler para magproseso ng notifications.

## Progress Notifications at Scenarios

Ang seksyong ito ay nagpapaliwanag ng konsepto ng progress notifications sa MCP, kung bakit mahalaga ang mga ito, at kung paano ito i-implement gamit ang Streamable HTTP. Makakakita ka rin ng praktikal na assignment para mapalalim ang iyong pag-unawa.

Ang progress notifications ay real-time na mga mensahe na ipinapadala mula sa server patungo sa kliyente habang may mahahabang operasyon. Sa halip na hintayin ang buong proseso na matapos, pinapanatili ng server ang kliyente na updated tungkol sa kasalukuyang status. Pinapabuti nito ang transparency, user experience, at ginagawang mas madali ang debugging.

**Halimbawa:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Bakit Gumamit ng Progress Notifications?

Ang progress notifications ay mahalaga para sa ilang kadahilanan:

- **Mas magandang user experience:** Nakikita ng mga user ang updates habang nagpapatuloy ang trabaho, hindi lamang sa dulo.
- **Real-time feedback:** Maaaring mag-display ang mga kliyente ng progress bars o logs, na nagpaparamdam na responsive ang app.
- **Mas madaling debugging at monitoring:** Nakikita ng mga developer at user kung saan maaaring mabagal o ma-stuck ang proseso.

### Paano Mag-implement ng Progress Notifications

Narito kung paano mo ma-implement ang progress notifications sa MCP:

- **Sa server:** Gumamit ng `ctx.info()` o `ctx.log()` para magpadala ng notifications habang nagpoproseso ng bawat item. Ipinapadala nito ang mensahe sa kliyente bago maging handa ang pangunahing resulta.
- **Sa kliyente:** Mag-implement ng message handler na nakikinig at nagpapakita ng notifications habang dumarating ang mga ito. Ang handler na ito ay nagtatangi sa pagitan ng notifications at ng final result.

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

Kapag nag-implement ng MCP servers gamit ang HTTP-based transports, ang seguridad ay nagiging pangunahing alalahanin na nangangailangan ng maingat na pansin sa iba't ibang attack vectors at protection mechanisms.

### Overview

Ang seguridad ay kritikal kapag nag-e-expose ng MCP servers sa HTTP. Ang Streamable HTTP ay nagdadala ng bagong attack surfaces at nangangailangan ng maingat na configuration.

### Mga Pangunahing Punto

- **Origin Header Validation**: Palaging i-validate ang `Origin` header upang maiwasan ang DNS rebinding attacks.
- **Localhost Binding**: Para sa lokal na development, i-bind ang servers sa `localhost` upang maiwasan ang pag-expose sa public internet.
- **Authentication**: Mag-implement ng authentication (hal., API keys, OAuth) para sa production deployments.
- **CORS**: I-configure ang Cross-Origin Resource Sharing (CORS) policies upang limitahan ang access.
- **HTTPS**: Gumamit ng HTTPS sa production upang ma-encrypt ang traffic.

### Mga Pinakamahusay na Kasanayan

- Huwag kailanman magtiwala sa incoming requests nang walang validation.
- I-log at i-monitor ang lahat ng access at errors.
- Regular na i-update ang dependencies upang ma-patch ang security vulnerabilities.

### Mga Hamon

- Pagbabalanse ng seguridad at kadalian ng development.
- Pagtitiyak ng compatibility sa iba't ibang client environments.

## Pag-upgrade mula SSE patungo sa Streamable HTTP

Para sa mga applications na kasalukuyang gumagamit ng Server-Sent Events (SSE), ang paglipat sa Streamable HTTP ay nagbibigay ng mas pinahusay na capabilities at mas magandang pangmatagalang sustainability para sa iyong MCP implementations.

### Bakit Mag-upgrade?
Mayroong dalawang mahalagang dahilan para mag-upgrade mula SSE patungo sa Streamable HTTP:

- Ang Streamable HTTP ay nag-aalok ng mas mahusay na scalability, compatibility, at mas mayamang suporta sa notification kumpara sa SSE.
- Ito ang inirerekomendang transport para sa mga bagong MCP application.

### Mga Hakbang sa Paglipat

Narito kung paano mo maililipat ang iyong MCP application mula SSE patungo sa Streamable HTTP:

- **I-update ang server code** upang gamitin ang `transport="streamable-http"` sa `mcp.run()`.
- **I-update ang client code** upang gamitin ang `streamablehttp_client` sa halip na SSE client.
- **Magpatupad ng message handler** sa client upang iproseso ang mga notification.
- **Subukan ang compatibility** sa mga umiiral na tools at workflows.

### Pagpapanatili ng Compatibility

Inirerekomenda na panatilihin ang compatibility sa mga umiiral na SSE client habang nasa proseso ng paglipat. Narito ang ilang estratehiya:

- Maaari mong suportahan ang parehong SSE at Streamable HTTP sa pamamagitan ng pagpapatakbo ng parehong transport sa magkaibang endpoints.
- Dahan-dahang ilipat ang mga client sa bagong transport.

### Mga Hamon

Siguraduhing matugunan ang mga sumusunod na hamon sa panahon ng paglipat:

- Siguraduhing lahat ng client ay na-update
- Pag-handle ng mga pagkakaiba sa notification delivery

## Mga Pagsasaalang-alang sa Seguridad

Ang seguridad ay dapat maging pangunahing prayoridad kapag nag-iimplementa ng anumang server, lalo na kung gumagamit ng HTTP-based transports tulad ng Streamable HTTP sa MCP.

Kapag nag-iimplementa ng MCP servers gamit ang HTTP-based transports, ang seguridad ay nagiging mahalagang usapin na nangangailangan ng maingat na pagtuon sa iba't ibang attack vectors at mga mekanismo ng proteksyon.

### Pangkalahatang-ideya

Ang seguridad ay kritikal kapag ine-expose ang MCP servers sa HTTP. Ang Streamable HTTP ay nagdadala ng mga bagong attack surfaces at nangangailangan ng maingat na configuration.

Narito ang ilang mahahalagang pagsasaalang-alang sa seguridad:

- **Origin Header Validation**: Palaging i-validate ang `Origin` header upang maiwasan ang DNS rebinding attacks.
- **Localhost Binding**: Para sa lokal na development, i-bind ang mga server sa `localhost` upang maiwasan ang pag-expose sa public internet.
- **Authentication**: Magpatupad ng authentication (hal., API keys, OAuth) para sa production deployments.
- **CORS**: I-configure ang Cross-Origin Resource Sharing (CORS) policies upang limitahan ang access.
- **HTTPS**: Gumamit ng HTTPS sa production upang i-encrypt ang traffic.

### Mga Best Practices

Bukod dito, narito ang ilang best practices na dapat sundin kapag nag-iimplementa ng seguridad sa iyong MCP streaming server:

- Huwag magtiwala sa mga incoming requests nang walang validation.
- I-log at i-monitor ang lahat ng access at errors.
- Regular na i-update ang mga dependencies upang ma-patch ang mga security vulnerabilities.

### Mga Hamon

Makakaranas ka ng ilang hamon kapag nag-iimplementa ng seguridad sa MCP streaming servers:

- Pagbabalanse ng seguridad at kadalian ng development
- Pagtiyak ng compatibility sa iba't ibang client environments

### Assignment: Gumawa ng Sariling Streaming MCP App

**Scenario:**
Gumawa ng MCP server at client kung saan ang server ay nagpoproseso ng listahan ng mga item (hal., mga file o dokumento) at nagpapadala ng notification para sa bawat item na naproseso. Ang client ay dapat magpakita ng bawat notification habang ito ay dumarating.

**Mga Hakbang:**

1. Magpatupad ng server tool na nagpoproseso ng listahan at nagpapadala ng notification para sa bawat item.
2. Magpatupad ng client na may message handler upang magpakita ng mga notification nang real-time.
3. Subukan ang iyong implementation sa pamamagitan ng pagpapatakbo ng parehong server at client, at obserbahan ang mga notification.

[Solution](./solution/README.md)

## Karagdagang Pagbabasa at Ano ang Susunod?

Upang ipagpatuloy ang iyong paglalakbay sa MCP streaming at palawakin ang iyong kaalaman, ang seksyong ito ay nagbibigay ng karagdagang resources at mga mungkahing susunod na hakbang para sa paggawa ng mas advanced na mga application.

### Karagdagang Pagbabasa

- [Microsoft: Introduction to HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### Ano ang Susunod?

- Subukang gumawa ng mas advanced na MCP tools na gumagamit ng streaming para sa real-time analytics, chat, o collaborative editing.
- Tuklasin ang pag-integrate ng MCP streaming sa frontend frameworks (React, Vue, atbp.) para sa live UI updates.
- Susunod: [Utilising AI Toolkit for VSCode](../07-aitk/README.md)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.