# HTTPS Streaming wit Model Context Protocol (MCP)

Dis chapter provide beta guide to implement secure, scalable, and real-time streaming wit di Model Context Protocol (MCP) using HTTPS. E cover di motivation for streaming, di transport mechanisms wey dey available, how to implement streamable HTTP inside MCP, beta security practices, migration from SSE, and practical guide for build your own streaming MCP apps.

> **Looking ahead:** dis lesson dey describe Streamable HTTP under **MCP Specification 2025-11-25**, wey session dey establish during `initialize` and e dey pinned wit an `Mcp-Session-Id` header. Di `2026-07-28` release candidate remove di handshake and session ID completely, e make every request self-contained and e fit route go any server instance without sticky sessions. See [What's Changing in MCP: The 2026-07-28 Release Candidate](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md) for details.

## Transport Mechanisms and Streaming inside MCP

Dis section go explore di different transport mechanisms wey dey inside MCP and di role dem play to enable streaming capability for real-time communication between clients and servers.

### Wetin be Transport Mechanism?

Transport mechanism na wetin define how data go dey exchange between client and server. MCP support plenti transport types to match different environment and requirements:

- **stdio**: Standard input/output, beta for local and CLI-based tools. Simple but no beta for web or cloud.
- **SSE (Server-Sent Events)**: Allow servers push real-time updates to clients over HTTP. Good for web UIs, but e limited in scalability and flexibility. As per MCP Specification 2025-06-18, standalone SSE (Server-Sent Events) transport don deprecated and replace by "Streamable HTTP" transport.
- **Streamable HTTP**: Modern HTTP-based streaming transport, e support notifications and better scalability. Dem recommend am for most production and cloud scenario.

### Comparison Table

Make you check di comparison table below to sabi di difference between dis transport mechanisms:

| Transport         | Real-time Updates | Streaming | Scalability | Use Case                |
|-------------------|------------------|-----------|-------------|-------------------------|
| stdio             | No               | No        | Low         | Local CLI tools         |
| SSE               | Yes              | Yes       | Medium      | Web, real-time updates  |
| Streamable HTTP   | Yes              | Yes       | High        | Cloud, multi-client     |

> **Tip:** Choosing di correct transport fit affect performance, scalability, and user experience. **Streamable HTTP** na di beta choice for modern, scalable, and cloud-ready application.

Make you note di transports stdio and SSE wey dem show you for previous chapters and how streamable HTTP na di transport wey this chapter talk about.

## Streaming: Concepts and Motivation

To understand di fundamental concepts and reasons behind streaming na important to implement beta real-time communication systems.

**Streaming** na technique inside network programming wey allow data to dey send and receive small, manageable chunks or as series of events, instead of waiting for whole response to ready. Dis one beta for:

- Large files or datasets.
- Real-time updates (like chat, progress bars).
- Long-running computations wey you wan keep user dey informed.

This one na watin you suppose sabi about streaming at top level:

- Data dey deliver bit by bit, no be all at once.
- Client fit process data as e land.
- E reduce perceived latency and beta user experience.

### Why you go use streaming?

Reasons to use streaming be say:

- Users go get feedback sharp sharp, no be only for end
- E enable real-time apps and beta response for UI dem
- Network and compute resources go dey use well well

### Simple Example: HTTP Streaming Server & Client

Dis na simple example how streaming fit implement:

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

Dis example show how server dey send messages in series to client as dem ready, no dey wait make dem finish all messages before e start.

**How e dey work:**

- Di server dey yield each message as e ready.
- Di client dey receive and print chunk as e show.

**Requirements:**

- Di server must use streaming response (like `StreamingResponse` for FastAPI).
- Di client must process response as stream (`stream=True` for requests).
- Content-Type na usually `text/event-stream` or `application/octet-stream`.

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
- `delayElements()` dey simulate processing time between events
- Events fit get types (`info`, `result`) for beta client handling

### Comparison: Classic Streaming vs MCP Streaming

Differences between how streaming dey work classically versus how e work inside MCP fit show like this:

| Feature                | Classic HTTP Streaming         | MCP Streaming (Notifications)      |
|------------------------|-------------------------------|-------------------------------------|
| Main response          | Chunked                       | Single, at end                      |
| Progress updates       | Sent as data chunks           | Sent as notifications               |
| Client requirements    | Must process stream           | Must implement message handler      |
| Use case               | Large files, AI token streams | Progress, logs, real-time feedback  |

### Key Differences Observed

Additionally, here be some key differences:

- **Communication Pattern:**
  - Classic HTTP streaming: E dey use simple chunked transfer encoding to send data chunks
  - MCP streaming: E dey use structured notification system with JSON-RPC protocol

- **Message Format:**
  - Classic HTTP: Plain text chunks wit newlines
  - MCP: Structured LoggingMessageNotification objects wit metadata

- **Client Implementation:**
  - Classic HTTP: Simple client wey fit process streaming responses
  - MCP: Beta client wit message handler to process different types of messages

- **Progress Updates:**
  - Classic HTTP: Progress na part of main response stream
  - MCP: Progress dey send through separate notification messages while main response dey end

### Recommendations

Some tins wey we recommend when you wan choose between classical streaming (like di endpoint we show you with `/stream`) and MCP streaming:

- **For simple streaming:** Classic HTTP streaming na easier to implement and e good for basic streaming needs.

- **For complex, interactive apps:** MCP streaming dey offer structured approach wit richer metadata and separation between notifications and final result.

- **For AI apps:** MCP notification system beta well well for long-running AI tasks where you want keep users informed of progress.

## Streaming inside MCP

Ok, so you don see some recommendations and comparisons so far about difference between classical streaming and MCP streaming. Make we go into detail how streaming fit leverage inside MCP.

To sabi how streaming dey work inside MCP framework na key for build responsive apps wey go provide real-time feedback to users during long-running operation.

For MCP, streaming no be about sending main response in chunks, but na about sending **notifications** to client while tool dey process request. Dem notifications fit include progress updates, logs, or other events.

### How e dey work

Main result still dey sent as single response. But notifications fit dey send as separate messages during processing to update client for real time. Di client must fit handle and show these notifications.

## Wetin be Notification?

We talk "Notification", wetin e mean for MCP context?

Notification na message wey server dey send go client to inform progress, status, or other events wey dey happen during long-running operation. Notifications dey improve transparency and user experience.

Example, client suppose send notification once initial handshake with server don happen.

Notification fit be like this for JSON message:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notifications belong to topic for MCP wey dem call ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

To make logging work, server need enable am as feature/capability like this:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Depending on SDK wey you use, logging fit don enabled by default, or you fit need enable am explicit for your server configuration.

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

## How to Implement Notifications inside MCP

To implement notifications inside MCP, you need set up both server and client side to handle real-time updates. E allow your app to provide immediate feedback to users during long-running tasks.

### Server-side: Sending Notifications

Make we start wit server side. For MCP, you define tools wey fit send notifications while dem dey process requests. Server dey use context object (usually `ctx`) to send message to client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

For example above, di `process_files` tool dey send three notifications to client as e dey process each file. Di `ctx.info()` method dey used to send informational messages.

Also, to enable notifications, make sure your server dey use streaming transport (like `streamable-http`) and your client implement message handler to process notifications. Here be how you fit set server to use `streamable-http` transport:

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

For dis .NET example, di `ProcessFiles` tool get `Tool` attribute and e dey send three notifications to client as e dey process each file. Di `ctx.Info()` method na to send informational messages.

To enable notifications for your .NET MCP server, make sure say you dey use streaming transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Client-side: Receiving Notifications

Di client must implement message handler to process and display notifications as dem reach.

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

For di code before, di `message_handler` function dey check whether message wey land na notification. If na, e print am; if no be, e process as regular server message. Also note how `ClientSession` dey initialize wit `message_handler` to handle incoming notifications.

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

For dis .NET example, di `MessageHandler` function dey check whether message wey come na notification. If na, e print am; if no be, e process am as regular server message. `ClientSession` dey initialize wit message handler through `ClientSessionOptions`.

To enable notifications, make sure your server dey use streaming transport (like `streamable-http`) and your client implement message handler to process notifications.

## Progress Notifications & Scenarios

Dis section go explain di meaning of progress notifications inside MCP, why e important, and how you fit implement am using Streamable HTTP. You go still find practical assignment to help you understand better.

Progress notifications na real-time messages wey server dey send go client during long-running task dem. Instead of waiting for whole process to finish, server dey keep client update about current status. Dis one improve transparency, user experience, and e make debugging easier.

**Example:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Why You Go Use Progress Notifications?

Progress notifications dey necessary for many reasons:

- **Better user experience:** Users go see update as work dey happen, no be only for end.
- **Real-time feedback:** Clients fit display progress bars or logs, e make app feel responsive.
- **Easy debugging and monitoring:** Developers and users fit see where process dey slow or e dey stuck.

### How to Implement Progress Notifications

Dis na how you go implement progress notifications inside MCP:

- **For the server:** Use `ctx.info()` or `ctx.log()` to send notifications as you dey process each item. Dis one send message to client before main result go ready.
- **For the client:** Implement message handler wey go listen and show notifications as dem land. This handler go sabi separate notifications from final result.

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

When you dey implement MCP servers wey use HTTP-based transports, security na paramount concern wey need beta attention to plenti attack vectors and protection mechanisms.

### Overview

Security na important thing when you dey expose MCP servers over HTTP. Streamable HTTP dey introduce new attack surfaces and require careful configuration.

### Key Points
- **Origin Header Validation**: Always check di `Origin` header make e no allow DNS rebinding attack dem.
- **Localhost Binding**: For local development, make sure say di server dey bind for `localhost` so e no go show for public internet.
- **Authentication**: Use authentication (like API keys, OAuth) for production deployments.
- **CORS**: Arrange Cross-Origin Resource Sharing (CORS) policy wey go restrict who fit access.
- **HTTPS**: Use HTTPS for production to encrypt di traffic.

### Best Practices

- No trust any request wey no get validation.
- Log and monitor all access and error dem.
- Always update your dependencies to fix security wahala dem.

### Challenges

- How to balance security with easy development
- How to make am work well with different client environments

## Upgrading from SSE to Streamable HTTP

For applications wey dey use Server-Sent Events (SSE) now, to move go Streamable HTTP go give better power and better long-term support for your MCP implementations.

### Why Upgrade?

Two important reasons dey why you suppose upgrade from SSE to Streamable HTTP:

- Streamable HTTP dey offer better scalability, compatibility, and better notification support pass SSE.
- Na di recommended transport for new MCP applications.

### Migration Steps

Dis na how you fit migrate from SSE to Streamable HTTP for your MCP applications:

- **Update server code** make e use `transport="streamable-http"` inside `mcp.run()`.
- **Update client code** make e use `streamablehttp_client` instead of SSE client.
- **Implement a message handler** for the client wey go process notifications.
- **Test for compatibility** with tools and workflows wey you dey use.

### Maintaining Compatibility

E good to keep am say your new system still fit work with old SSE clients during the migration. Here be some ways to do am:

- You fit run both SSE and Streamable HTTP for different endpoints.
- Slowly move clients go the new transport.

### Challenges

Make sure say you solve this challenges when you dey migrate:

- Make sure all clients don update
- Handle difference for how notifications dey deliver

## Security Considerations

Security na very important thing when you dey implement any server, especially if you dey use HTTP-based transports like Streamable HTTP for MCP. 

When you dey implement MCP servers with HTTP-based transports, security na serious matter wey need to watch multiple attack ways and protection tools carefully.

### Overview

Security dey very important when you expose MCP servers over HTTP. Streamable HTTP bring new ways wey attackers fit use and e need proper configuration.

Here are some important security considerations:

- **Origin Header Validation**: Always check di `Origin` header make e no allow DNS rebinding attack dem.
- **Localhost Binding**: For local development, make e bind to `localhost` so e no go show for public internet.
- **Authentication**: Use authentication (like API keys, OAuth) for production deployments.
- **CORS**: Arrange Cross-Origin Resource Sharing (CORS) wey go limit who fit access.
- **HTTPS**: Use HTTPS for production to encrypt traffic.

### Best Practices

Also, here be some best practices to follow when you dey implement security for your MCP streaming server:

- No trust any request wey no get validation.
- Log and monitor all access and errors dem.
- Always update dependencies to patch security holes.

### Challenges

You go face some challenges when you dey implement security for MCP streaming servers:

- Balancing security with easy development
- Making sure e work well with different client environments

### Assignment: Build Your Own Streaming MCP App

**Scenario:**
Build MCP server and client where server dey process list of items (like files or documents) and e go send notification for every item wey e process. The client go show every notification as e reach.

**Steps:**

1. Build server tool wey go process list and send notification for each item.
2. Build client wey get message handler to show notifications for real time.
3. Test your work by running both server and client, observe all notifications.

[Solution](./solution/README.md)

## Further Reading & What Next?

To continue your MCP streaming journey and learn more, this section get more resources and suggested next steps for building advanced applications.

### Further Reading

- [Microsoft: Introduction to HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### What Next?

- Try build more advanced MCP tools wey use streaming for real-time analytics, chat, or collaborative editing.
- Explore how to join MCP streaming with frontend frameworks (React, Vue, etc.) for live UI updates.
- Next: [Utilising AI Toolkit for VSCode](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->