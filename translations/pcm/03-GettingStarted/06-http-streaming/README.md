# HTTPS Streaming wit Model Context Protocol (MCP)

Dis chapter go show you beta guide on how to do secure, scalable, and real-time streaming wit Model Context Protocol (MCP) using HTTPS. E go talk about why streaming dey important, di transport mechanisms wey dey, how to do streamable HTTP for MCP, security best practices, how to move from SSE, and practical tips to build your own streaming MCP apps.

## Transport Mechanisms and Streaming for MCP

Dis section go explain di different transport mechanisms wey MCP get and how dem dey help for real-time communication between client and server.

### Wetin be Transport Mechanism?

Transport mechanism na di way data dey waka between client and server. MCP get different transport types wey fit work for different environments and needs:

- **stdio**: Standard input/output, e dey good for local and CLI tools. E simple but no fit work well for web or cloud.
- **SSE (Server-Sent Events)**: E allow server dey push real-time updates to client through HTTP. E good for web UIs, but e no too scale well and e no too flexible.
- **Streamable HTTP**: Na modern HTTP-based streaming transport wey dey support notifications and e dey scale well. E dey recommended for production and cloud scenarios.

### Comparison Table

Check di table below to sabi di difference between di transport mechanisms:

| Transport         | Real-time Updates | Streaming | Scalability | Use Case                |
|-------------------|------------------|-----------|-------------|-------------------------|
| stdio             | No               | No        | Low         | Local CLI tools         |
| SSE               | Yes              | Yes       | Medium      | Web, real-time updates  |
| Streamable HTTP   | Yes              | Yes       | High        | Cloud, multi-client     |

> **Tip:** Di transport wey you choose go affect performance, scalability, and user experience. **Streamable HTTP** na di best for modern, scalable, and cloud-ready apps.

Remember di stdio and SSE transports wey dem don show you before, and how dis chapter go focus on streamable HTTP.

## Streaming: Concepts and Motivation

To sabi how to do real-time communication well, you need to understand di basic idea and why streaming dey important.

**Streaming** na way wey data dey waka for network programming. Instead of waiting for di whole response to ready, e dey send data small small or as events. E dey useful for:

- Big files or datasets.
- Real-time updates (e.g., chat, progress bars).
- Long processes wey you wan dey update user as e dey go.

Wetin you need to sabi about streaming:

- Data dey come small small, no be once.
- Client fit process di data as e dey arrive.
- E dey reduce delay and e dey make user experience better.

### Why you go use streaming?

Reasons why streaming dey important:

- Users go dey see updates immediately, no be only for di end.
- E dey make real-time apps and UIs dey sharp.
- E dey use network and compute resources well.

### Simple Example: HTTP Streaming Server & Client

See simple example of how streaming fit work:

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

Dis example show how server fit dey send messages to client as dem ready, instead of waiting for all di messages to ready.

**How e dey work:**

- Server go dey send each message as e ready.
- Client go dey receive and show each chunk as e arrive.

**Requirements:**

- Server go use streaming response (e.g., `StreamingResponse` for FastAPI).
- Client go process di response as stream (`stream=True` for requests).
- Content-Type go be `text/event-stream` or `application/octet-stream`.

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

- E dey use Spring Boot reactive stack wit `Flux` for streaming.
- `ServerSentEvent` dey provide structured event streaming wit event types.
- `WebClient` wit `bodyToFlux()` dey enable reactive streaming consumption.
- `delayElements()` dey simulate processing time between events.
- Events fit get types (`info`, `result`) to help client handle am better.

### Comparison: Classic Streaming vs MCP Streaming

See di difference between "classic" streaming and MCP streaming:

| Feature                | Classic HTTP Streaming         | MCP Streaming (Notifications)      |
|------------------------|-------------------------------|-------------------------------------|
| Main response          | Chunked                       | Single, at end                      |
| Progress updates       | Sent as data chunks           | Sent as notifications               |
| Client requirements    | Must process stream           | Must implement message handler      |
| Use case               | Large files, AI token streams | Progress, logs, real-time feedback  |

### Key Differences Observed

Some key differences:

- **Communication Pattern:**
  - Classic HTTP streaming: E dey use chunked transfer encoding to send data small small.
  - MCP streaming: E dey use structured notification system wit JSON-RPC protocol.

- **Message Format:**
  - Classic HTTP: Plain text chunks wit newlines.
  - MCP: Structured LoggingMessageNotification objects wit metadata.

- **Client Implementation:**
  - Classic HTTP: Simple client wey dey process streaming responses.
  - MCP: More advanced client wey get message handler to process different message types.

- **Progress Updates:**
  - Classic HTTP: Progress dey inside di main response stream.
  - MCP: Progress dey come as separate notification messages, di main response go come last.

### Recommendations

When you wan choose between classic streaming and MCP streaming:

- **For simple streaming needs:** Classic HTTP streaming dey easy to do and e fit basic streaming needs.
- **For complex, interactive apps:** MCP streaming dey structured wit better metadata and e dey separate notifications from final results.
- **For AI apps:** MCP notification system dey useful for long AI tasks wey you wan dey update users.

## Streaming in MCP

You don see di difference between classic streaming and MCP streaming. Now, make we talk how you fit use streaming for MCP.

For MCP, streaming no mean say di main response go dey come small small. E mean say server go dey send **notifications** to client while e dey process request. Dis notifications fit be progress updates, logs, or other events.

### How e dey work

Di main result go still come as one response. But notifications go dey come as separate messages during processing to update di client real-time. Di client go sabi handle and show di notifications.

## Wetin be Notification?

We talk "Notification", wetin e mean for MCP?

Notification na message wey server dey send to client to tell am about progress, status, or other events during long process. E dey make everything clear and e dey improve user experience.

For example, client fit send notification after e don handshake wit server.

Notification dey look like dis as JSON message:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notifications dey under one topic for MCP wey dem dey call ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

To make logging work, server go enable am as feature/capability like dis:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Depending on di SDK wey you dey use, logging fit don already dey enabled, or you go need enable am for your server config.

Different types of notifications dey:

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

## How to Do Notifications for MCP

To do notifications for MCP, you go set up di server and client to handle real-time updates. Dis go make your app dey give users immediate feedback during long processes.

### Server-side: Sending Notifications

Make we start wit di server side. For MCP, you go define tools wey fit send notifications while dem dey process requests. Server go use context object (e.g., `ctx`) to send messages to client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

For di example above, di `process_files` tool dey send three notifications to client as e dey process each file. Di `ctx.info()` method dey send di messages.

To enable notifications, make sure your server dey use streaming transport (like `streamable-http`) and your client get message handler to process notifications. Set up server like dis:

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

For dis .NET example, di `ProcessFiles` tool dey send three notifications to client as e dey process each file. Di `ctx.Info()` method dey send di messages.

To enable notifications for your .NET MCP server, make sure you dey use streaming transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Client-side: Receiving Notifications

Client go need message handler to process and show notifications as dem dey arrive.

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

For di code above, di `message_handler` function go check if di message wey dey come na notification. If yes, e go print di notification; if no, e go process am as normal server message. Di `ClientSession` dey initialized wit di `message_handler` to handle notifications.

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

For dis .NET example, di `MessageHandler` function dey check if di message wey dey come na notification. If yes, e go print di notification; if no, e go process am as normal server message. Di `ClientSession` dey initialized wit di message handler through `ClientSessionOptions`.

To enable notifications, make sure your server dey use streaming transport (like `streamable-http`) and your client get message handler to process notifications.

## Progress Notifications & Scenarios

Dis section go explain wetin progress notifications mean for MCP, why dem dey important, and how to do dem using Streamable HTTP. You go also see practical assignment to help you understand am well.

Progress notifications na real-time messages wey server dey send to client during long processes. Instead of waiting for di whole process to finish, server go dey update client about wetin dey happen. E dey make everything clear, improve user experience, and e dey help debugging.

**Example:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Why Progress Notifications dey Important?

Reasons why progress notifications dey important:

- **Better user experience:** Users go dey see updates as work dey go, no be only for di end.
- **Real-time feedback:** Clients fit show progress bars or logs, make app dey sharp.
- **Easier debugging and monitoring:** Developers and users fit see where process dey slow or stuck.

### How to Do Progress Notifications

How you fit do progress notifications for MCP:

- **For server:** Use `ctx.info()` or `ctx.log()` to send notifications as you dey process each item. E go send message to client before di main result ready.
- **For client:** Do message handler wey go dey listen and show notifications as dem dey arrive. Di handler go sabi di difference between notifications and di final result.

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

When you dey do MCP servers wit HTTP-based transports, security na big matter wey you go need handle well to avoid attack.

### Overview

Security dey very important when you dey expose MCP servers through HTTP. Streamable HTTP dey bring new risks, so you go need configure am well.

### Key Points

- **Origin Header Validation**: Always check di `Origin` header to stop DNS rebinding attacks.
- **Localhost Binding**: For local dev, bind servers to `localhost` to stop public exposure.
- **Authentication**: Use authentication (e.g., API keys, OAuth) for production.
- **CORS**: Set Cross-Origin Resource Sharing (CORS) policies to limit access.
- **HTTPS**: Use HTTPS for production to secure traffic.

### Best Practices

- No trust any request wey dey come without validation.
- Dey log and monitor all access and errors.
- Dey update dependencies to fix security issues.

### Challenges

- Balancing security and easy development.
- Making sure e dey work well for different client environments.
## Upgrading from SSE to Streamable HTTP

If your app dey use Server-Sent Events (SSE), to move go Streamable HTTP go give you better features and e go make your MCP setup last well well.

### Why You Go Upgrade?

Two strong reasons dey why you go wan move from SSE go Streamable HTTP:

- Streamable HTTP dey scale well, e dey work better with different systems, and e fit support richer notifications pass SSE.
- Na di transport wey dem recommend for new MCP apps.

### Migration Steps

Na so you fit move from SSE go Streamable HTTP for your MCP apps:

- **Change server code** to use `transport="streamable-http"` inside `mcp.run()`.
- **Change client code** to use `streamablehttp_client` instead of SSE client.
- **Add message handler** for di client to process notifications.
- **Test am** make sure say e dey work well with di tools and workflows wey you dey use.

### How to Keep Compatibility

E good make you still dey support di SSE clients wey dey already dey while you dey move go Streamable HTTP. Na di way wey you fit do am:

- You fit run both SSE and Streamable HTTP for different endpoints.
- Move di clients small small go di new transport.

### Challenges

Make sure say you handle di wahala wey fit show during di migration:

- Make sure say all di clients don update.
- Manage di difference wey dey for how notification dey deliver.

## Security Considerations

Security na di main thing wey you go focus on when you dey set up any server, especially if you dey use HTTP-based transport like Streamable HTTP for MCP.

When you dey set up MCP servers with HTTP-based transport, you go need pay attention to di different ways wey attack fit happen and how you go protect am.

### Overview

Security na big deal when you dey expose MCP servers through HTTP. Streamable HTTP dey open new ways wey attack fit happen, so you go need configure am well.

Di main security things wey you go look:

- **Origin Header Validation**: Always check di `Origin` header to stop DNS rebinding attack.
- **Localhost Binding**: For local development, make sure say server dey bind to `localhost` so e no go dey open for di public internet.
- **Authentication**: Add authentication (like API keys, OAuth) for production setup.
- **CORS**: Set Cross-Origin Resource Sharing (CORS) policy to limit access.
- **HTTPS**: Use HTTPS for production to make sure say traffic dey encrypted.

### Best Practices

Follow dis best practices when you dey set up security for your MCP streaming server:

- No trust any request wey dey come without checking am.
- Dey log and monitor all di access and errors.
- Dey update dependencies regularly to fix security wahala.

### Challenges

You go face some wahala when you dey set up security for MCP streaming servers:

- How you go balance security with easy development.
- Make sure say e dey work well with different client setups.

### Assignment: Build Your Own Streaming MCP App

**Scenario:**
Build MCP server and client wey go process list of items (like files or documents) and send notification for each item wey e process. Di client go dey show di notification as e dey come.

**Steps:**

1. Build server tool wey go process di list and send notification for each item.
2. Build client wey get message handler to show di notifications as e dey happen.
3. Test di setup by running di server and client, then check di notifications.

[Solution](./solution/README.md)

## Further Reading & What Next?

If you wan sabi more about MCP streaming and how you fit build better apps, dis section get resources and next steps wey you fit follow.

### Further Reading

- [Microsoft: Introduction to HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### What Next?

- Try build more advanced MCP tools wey go use streaming for real-time analytics, chat, or collaborative editing.
- Check how you fit connect MCP streaming with frontend frameworks (React, Vue, etc.) for live UI updates.
- Next: [Utilising AI Toolkit for VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say machine transleshion fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->