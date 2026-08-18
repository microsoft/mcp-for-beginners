# HTTPS Streaming wit Model Context Protocol (MCP)

Dis chapter dey provide beta guide gbas to how to build secure, scalable, and real-time streaming wit Model Context Protocol (MCP) wey use HTTPS. E cover why streaming dey important, transport methods wey dey available, how to use streamable HTTP for MCP, security best practices, how to waka from SSE, plus how to build your own streaming MCP applications practically.

> **Looking ahead:** dis lesson dey explain how Streamable HTTP go work under **MCP Specification 2025-11-25**, where session dey start during `initialize` and e dey pinned wit `Mcp-Session-Id` header. For `2026-07-28` release candidate, dem remove handshake plus session ID complete, so every request fit stand on e own and fit go any server instance without sticky sessions. Check [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) for details.

## Transport Mechanisms and Streaming for MCP

Dis part go explore the different transport ways wey MCP get and how dem dey help streaming work well for real-time talk between clients and servers.

### Wetin be Transport Mechanism?

Transport mechanism na how data go dey waka between client and server. MCP fit support plenti transport types wey go fit different environment and needs:

- **stdio**: Standard input/output, good for local CLI tools. Simple but no good for web or cloud.
- **SSE (Server-Sent Events)**: Make server fit push real-time updates reach client via HTTP. Good for web UIs, but e get limit for scalability and flexibility. Since MCP Specification 2025-06-18, standalone SSE transport don stop and dem don change am to "Streamable HTTP" transport.
- **Streamable HTTP**: Modern HTTP streaming transport, fit support notifications and better scalability. Dem recommend for production and cloud environment.

### Comparison Table

Look the comparison table below to sabi the difference between these transport mechanisms:

| Transport         | Real-time Updates | Streaming | Scalability | Use Case                |
|-------------------|------------------|-----------|-------------|-------------------------|
| stdio             | No               | No        | Low         | Local CLI tools         |
| SSE               | Yes              | Yes       | Medium      | Web, real-time updates  |
| Streamable HTTP   | Yes              | Yes       | High        | Cloud, multi-client     |

> **Tip:** Choosing the right transport go affect how e go perform, how e go scale, and how user experience go be. **Streamable HTTP** na correct choice for modern, scalable, and cloud-ready apps.

Make you note the transports stdio and SSE wey we show you for previous chapters and how streaming HTTP na the transport wey this chapter get.

## Streaming: Concepts and Why E Dey Important

To sabi the basic concepts and why streaming dey important go help you build strong real-time systems wey fit communicate better.

**Streaming** na network programming way wey data go dey sent and received for small, manageable parts or like a series of events, no wait to get whole response finish. E good for:

- Big files or big data sets.
- Real-time updates (like chat, progress bars).
- Long work wey need to keep user dey updated.

Dis na wetin you need sabi about streaming for high level:

- Data dey come small small, no come finish at once.
- Client fit process data as e dey reach.
- E reduce delay and make user experience better.

### Why make we use streaming?

Reasons why people dey use streaming na:

- Users go dey get feedback quick quick, no go wait till end.
- E fit enable real-time apps and fast user interfaces.
- E dey use network and computing resources well well.

### Simple Example: HTTP Streaming Server & Client

Dis na simple example wey show how streaming fit work:

#### Python

**Server (Python, using FastAPI and StreamingResponse):**

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

**Client (Python, using requests):**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

Dis example dey show server dey send messages one by one to client as messages ready, no wait all messages finish before sending.

**How e dey work:**

- Server go dey output each message as e ready.
- Client go dey receive and show each message part as e land.

**Requirements:**

- Server must use streaming response (e.g., `StreamingResponse` inside FastAPI).
- Client must process response as stream (`stream=True` inside requests).
- Content-Type usually `text/event-stream` or `application/octet-stream`.

#### Java

**Server (Java, using Spring Boot and Server-Sent Events):**

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

**Client (Java, using Spring WebFlux WebClient):**

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

**Java Implementation Notes:**

- E dey use Spring Boot reactive stack wit `Flux` for streaming
- `ServerSentEvent` dey provide structured event streaming with event types
- `WebClient` wit `bodyToFlux()` dey enable reactive streaming consumption
- `delayElements()` dey mimic time between processing events
- Events fit get types (`info`, `result`) for better client handling

### Comparison: Classic Streaming vs MCP Streaming

Wetin make classic streaming different from streaming inside MCP fit be like dis:

| Feature                | Classic HTTP Streaming         | MCP Streaming (Notifications)      |
|------------------------|-------------------------------|-------------------------------------|
| Main response          | Chunked                       | Single, at end                      |
| Progress updates       | Sent as data chunks           | Sent as notifications               |
| Client requirements    | Must process stream           | Must implement message handler      |
| Use case               | Big files, AI token streams   | Progress, logs, real-time feedback  |

### Key Differences Observed

Plus, here be some key differences:

- **Communication Pattern:**
  - Classic HTTP streaming: Use simple chunked transfer encoding to send data for chunks
  - MCP streaming: Use structured notification system with JSON-RPC protocol

- **Message Format:**
  - Classic HTTP: Plain text chunks wit newlines
  - MCP: Structured LoggingMessageNotification objects wit metadata

- **Client Implementation:**
  - Classic HTTP: Simple client wey fit process streaming responses
  - MCP: More advance client wit message handler to process different types messages

- **Progress Updates:**
  - Classic HTTP: Progress dey part of main response stream
  - MCP: Progress dey sent separately as notification messages while main response come at end

### Recommendations

For wetin to choose between classical streaming (like endpoint `/stream` we show you before) and MCP streaming, here be some advice:

- **For simple streaming ones:** Classic HTTP streaming dey easy to build and e good for simple streaming work.

- **For complex, interactive apps:** MCP streaming get better structured approach wit richer metadata and dem separate notifications from final result.

- **For AI apps:** MCP notification system dey important especially for long-run AI tasks where you need to keep users informed of progress.

## Streaming inside MCP

So you don see recommendations and comparisons on how classical streaming different from streaming inside MCP. Now make we enter detail on how you fit use streaming for MCP.

Make you understand how streaming dey work inside MCP framework na key for building responsive apps wey fit give feedback quick quick during long run jobs.

For MCP, streaming no be to send main response for chunks but na to send **notifications** to client while tool dey process request. These notifications fit include progress updates, logs, or other events.

### How e dey work

Main result still dey sent as one single response. But notifications fit dey sent as separate messages during process to keep client update real time. Client gots fit handle and display these notifications.

## Wetin be Notification?

We talk "Notification", wetin that mean for MCP matter?

Notification na message wey server send to client to talk about progress, status, or other events during long run work. Notification dey help make things clear and improve user experience.

For example, client suppose send notification after the initial handshake with server don happen.

Notification fit look like dis as JSON message:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notifications dey belong to topic for MCP wey dem dey call ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

> **Deprecation notice:** the `2026-07-28` MCP specification release candidate dey mark Logging primitive as deprecated to favor `stderr` for stdio transports and OpenTelemetry for better structured observability. Logging go still work for `2025-11-25` and for at least one year after official deprecation. See [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md).

To make logging work, server need enable am as feature/capability like dis:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Depending on the SDK wey you use, logging fit dey enabled by default or you fit need enable am by hand for your server config.

Different kinds of notifications be:

| Level     | Description                    | Example Use Case                |
|-----------|-------------------------------|---------------------------------|
| debug     | Detailed debugging information | Function entry/exit points      |
| info      | General informational messages | Operation progress updates      |
| notice    | Normal but significant events  | Configuration changes           |
| warning   | Warning conditions             | Deprecated feature usage        |
| error     | Error conditions               | Operation failures              |
| critical  | Critical conditions            | System component failures       |
| alert     | Action must be taken immediately | Data corruption detected      |
| emergency | System is unusable             | Complete system failure         |

## How to Implement Notifications for MCP

To implement notifications for MCP, you gots set server and client side to handle real-time updates. Dis go allow your app give users immediate feedback during long run jobs.

### Server side: Sending Notifications

Make we start for server side. For MCP, you define tools wey fit send notifications while dem dey process requests. Server go use context object (normally `ctx`) to send messages to client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

For the example before, the `process_files` tool dey send three notifications to client as e dey process each file. `ctx.info()` method dey send informational messages.

Plus, to enable notifications, make sure your server dey use streaming transport (like `streamable-http`) and your client get message handler to process notifications. See how to set server to use `streamable-http` transport:

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

For dis .NET example, `ProcessFiles` tool get `Tool` attribute plus e go send three notifications to client as e dey process each file. `ctx.Info()` method dey send informational messages.

To enable notifications on your .NET MCP server, make sure say you dey use streaming transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Client side: Receiving Notifications

Client gots implement message handler to process and show notifications as e dey arrive.

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

For the code before, `message_handler` function check if incoming message na notification. If na so, e print the notification; if no, e process am as normal server message. Also, `ClientSession` dey initialized with `message_handler` to handle arriving notifications.

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

For this .NET example, `MessageHandler` function check if incoming message be notification. If yes, e print am; else e process am like normal server message. `ClientSession` get message handler from `ClientSessionOptions`.

To enable notifications, make sure say your server dey use streaming transport (like `streamable-http`) and your client get message handler wey fit process notifications.

## Progress Notifications & Scenarios

Dis section explain wetin progress notifications for MCP mean, why e matter, and how to implement am use Streamable HTTP. You go also find practical assignment to help you sabi am well.

Progress notifications na real-time messages wey server dey send to client during long running jobs. Instead of waiting the whole process finish, server go dey update client about current status. Dis one improve transparency, user experience, plus e make debugging easier.

**Example:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Why Use Progress Notifications?

Progress notifications dey important for plenti reasons:

- **Better user experience:** Users go dey see updates as work dey go, no go wait till end.
- **Real-time feedback:** Clients fit show progress bars or logs, e go make app feel responsive.
- **Easier debugging and monitoring:** Developers and users fit see where e fit slow or stuck.

### How to Implement Progress Notifications

See how you fit do progress notifications inside MCP:

- **For server:** Use `ctx.info()` or `ctx.log()` to send notifications as each item dey processed. E dey send message to client before main result ready.
- **For client:** Implement message handler wey go listen and show notifications when dem land. Dis handler go fit tell the difference between notifications and final result.

**Server Example:**


#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**Client Example:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## Security Considerations

Security suppose be top priority when you dey implement any server, especially wen you dey use HTTP-based transports like Streamable HTTP for MCP.

When you dey implement MCP servers with HTTP-based transports, security dey very important wey need proper attention to many attack ways and protection mechanisms.

### Overview

Security na critical thing wen you dey expose MCP servers over HTTP. Streamable HTTP bring new attack problem dem and e need careful setup.

Here be some key security things for mind:

- **Origin Header Validation**: Always check di `Origin` header to stop DNS rebinding attacks.
- **Localhost Binding**: For local development, make servers bind to `localhost` so nobody for outside internet fit see am.
- **Authentication**: Use authentication (like API keys, OAuth) for production place.
- **CORS**: Set Cross-Origin Resource Sharing (CORS) rules to limit access.
- **HTTPS**: Use HTTPS for production to encrypt di traffic.

### Best Practices

Plus, here be some best ways to follow wen you dey do security for your MCP streaming server:

- No ever believe any incoming request without checking am.
- Log and watch all access and error dem.
- Always update dependencies regularly to patch security matter.

### Challenges

You go face some wahala wen you dey do security for MCP streaming servers:

- Balance security with ease to develop
- Make sure e go work well for many client environments


## Upgrading from SSE to Streamable HTTP

For apps wey dey use Server-Sent Events (SSE) now, to move go Streamable HTTP go give better capacity and better sustainability for your MCP things.

### Why Upgrade?

Two big reasons dey to upgrade from SSE to Streamable HTTP:

- Streamable HTTP get better scalability, compatibility, and better notification support pass SSE.
- E be the recommended transport for new MCP apps.

### Migration Steps

Dis na how you fit shift from SSE to Streamable HTTP for your MCP apps:

- **Update server code** to use `transport="streamable-http"` inside `mcp.run()`.
- **Update client code** to use `streamablehttp_client` instead of SSE client.
- **Implement a message handler** for the client to handle notifications.
- **Test for compatibility** with the tools and workflow wey dey already.

### Maintaining Compatibility

E good make you keep compatibility wit old SSE clients as you dey migrate. Here be some ways:

- You fit run both SSE and Streamable HTTP for different endpoints.
- Make clients shift slowly to the new transport.

### Challenges

Make sure you solve these wahala during migration:

- Make sure all clients don update
- Handle difference wey dey for how notifications dey deliver

### Assignment: Build Your Own Streaming MCP App

**Scenario:**
Build MCP server and client wey di server go process list of items (like files or documents) and notify for every item wey e process. The client suppose show each notification as e dey come.

**Steps:**

1. Build server tool wey go process list and send notifications for each item.
2. Build client with message handler wey fit show notifications for real time.
3. Test your work by running both server and client, make you watch the notifications.

[Solution](./solution/README.md)

## Further Reading & What Next?

To continue your journey wit MCP streaming and to sabi more, dis section get extra resources and next steps for building more advanced apps.

### Further Reading

- [Microsoft: Introduction to HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### What Next?

- Try build more better MCP tools wey dey use streaming for real-time analytics, chat, or collaborative editing.
- Try join MCP streaming with frontend frameworks (React, Vue, etc.) to get live UI updates.
- Next: [Utilising AI Toolkit for VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->