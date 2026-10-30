# HTTPS Streaming wit Model Context Protocol (MCP)

Dis chapter dey give complete guide on how to implement secure, scalable, an real-time streaming wit Model Context Protocol (MCP) using HTTPS. E dey cover wetin make streaming important, di transport options wey dey, how to implement streamable HTTP for MCP, security best practices, migration from SSE, an practical advice to build your own streaming MCP applications. 

> [!WARNING]
> The implementation examples for dis lesson dey target **MCP Specification
> `2025-11-25`** an demonstrate di legacy `initialize` handshake,
> `Mcp-Session-Id`, GET event stream, an resumability model. MCP `2026-07-28`
> e don remove those features. Current Streamable HTTP requests are self-contained
> POST requests wey get `MCP-Protocol-Version` and `Mcp-Method` headers, plus
> `Mcp-Name` where e required. See
> [Wetin don change for MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md)
> before you use dem examples for new implementation.

## Transport Mekanizms an Streaming in MCP

Dis section go explore di different transport mekanizms wey dey for MCP an wetin dem dey do to make streaming possible for real-time communication between clients an servers.

### What is a Transport Mechanism?

A transport mechanism na how data dey change hand between the client and server. MCP dey support multiple transport types to fit different environments an requirements:

- **stdio**: Standard input/output, fine for local an CLI-based tools. Simple but no good for web or cloud.
- **HTTP+SSE**: Na legacy remote transport, deprecated for MCP `2025-03-26`
    an e don replace by Streamable HTTP. No use am for new implementations.
- **Streamable HTTP**: Modern HTTP-based streaming transport, e support notifications an get better scalability. We recommend am for most production an cloud scenarios.

### Comparison Table

Look di comparison table below to sabi di differences between these transport mekanizms:

| Transport | Status | Notifications | Typical use |
|---|---|---|---|
| stdio | Current | Yes | Local subprocesses |
| HTTP+SSE | Deprecated | Yes | Legacy remote implementations |
| Streamable HTTP | Current | Yes | Remote and cloud servers |

> **Tip:** Choose correct transport go affect performance, scalability, an user experience. **Streamable HTTP** na recommended for modern, scalable, an cloud-ready applications.

Di standard transports na stdio an Streamable HTTP. HTTP+SSE dey only for older examples.


## Streaming: Concepts an Motivation

To sabi di fundamental concepts an motivations behind streaming important if you wan implement effective real-time communication systems.

**Streaming** na technique for network programming wey make data fit dey send an receive small small chunks or sequence of events, instead of waiting make whole response ready. Dis one especially useful for:

- Big files or datasets.
- Real-time updates (e.g., chat, progress bars).
- Long-running computations wey you wan keep user informed.

Na wetin you need sabi about streaming for high level:

- Data dey come small small, no come all at once.
- Client fit process data as e dey arrive.
- E dey reduce how slow e feel (perceived latency) an improve user experience.

### Why use streaming?

Di reasons for using streaming na dem:

- Users go get feedback immediately, no wait reach end
- E enable real-time applications an responsive UIs
- E make network an compute resources use more efficient

### Simple Example: HTTP Streaming Server & Client

Na simple example below how streaming fit implement:

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

Dis example dey show server wey dey send series of messages to client as dem dey available, instead of waiting for all messages make dem ready.

**How e dey work:**

- Server go yield each message as e ready.
- Client go receive an print each chunk as e arrive.

**Requirements:**

- Server must use streaming response (e.g., `StreamingResponse` for FastAPI).
- Client must process response as stream (`stream=True` in requests).
- Content-Type is usually `text/event-stream` or `application/octet-stream`.

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

- E dey use Spring Boot reactive stack with `Flux` for streaming
- `ServerSentEvent` dey provide structured event streaming wit event types
- `WebClient` with `bodyToFlux()` enable reactive streaming consumption
- `delayElements()` dey simulate processing time between events
- Events fit get types (`info`, `result`) to make client handling better

### Comparison: Classic Streaming vs MCP Streaming

Di differences between how streaming dey work for 'classical' way and how e dey work for MCP fit show like dis:

| Feature                | Classic HTTP Streaming         | MCP Streaming (Notifications)      |
|------------------------|-------------------------------|-------------------------------------|
| Main response          | Chunked                       | Single, at end                      |
| Progress updates       | Sent as data chunks           | Sent as notifications               |
| Client requirements    | Must process stream           | Must implement message handler      |
| Use case               | Large files, AI token streams | Progress, logs, real-time feedback  |

### Key Differences Observed

Plus, here be some key differences:

- **Communication Pattern:**
  - Classic HTTP streaming: E dey use simple chunked transfer encoding to send data small small
  - MCP streaming: E dey use structured notification system wit JSON-RPC protocol

- **Message Format:**
  - Classic HTTP: Plain text chunks with newlines
  - MCP: Structured LoggingMessageNotification objects with metadata

- **Client Implementation:**
  - Classic HTTP: Simple client that processes streaming responses
  - MCP: More sophisticated client with a message handler to process different types of messages

- **Progress Updates:**
  - Classic HTTP: The progress is part of the main response stream
  - MCP: Progress is sent via separate notification messages while the main response comes at the end

### Recommendations

We get some things wey we recommend when you dey choose between implement classical streaming (like endpoint we show you above using `/stream`) or choose streaming via MCP.

- **For simple streaming needs:** Classic HTTP streaming easier to implement an e good enough for basic streaming needs.

- **For complex, interactive applications:** MCP streaming dey give more structured approach with richer metadata and separation between notifications an final results.

- **For AI applications:** MCP notification system especially useful for long-running AI tasks wey you wan keep users informed about progress.

## Streaming in MCP

Ok, so you don see some recommendations an comparisons so far about difference between classical streaming an streaming for MCP. Make we enter details exactly how you fit use streaming for MCP.

To understand how streaming dey work inside MCP framework na important to build responsive apps wey go give real-time feedback to users during long-running operations.

For MCP, streaming no mean to send di main response in chunks, na about to send **notifications** to the client while tool dey process request. These notifications fit include progress updates, logs, or other events.

### How it works

Di main result still dey send as single response. But notifications fit send as separate messages during processing and so dem go update client in real time. Client must fit handle an display these notifications.

### Optional exercise: connect to a hosted MCP server

You fit also use Streamable HTTP without running a local server. Dis example
connects to [Parallel Search MCP](https://docs.parallel.ai/integrations/mcp/search-mcp),
discovers its tools, and searches for public MCP documentation using the same
Python SDK as the [local client](../../../../03-GettingStarted/06-http-streaming/solution/python/client.py).

Parallel anonymous endpoint no need account or API key. Free access get
rate limited. Running this script go send the search queries, objective, an a
random session identifier to Parallel. The service also offers `web_fetch`,
which sends requested URLs and any supplied context to Parallel. Use public
information for this exercise; see its [terms](https://parallel.ai/customer-terms)
and [privacy policy](https://parallel.ai/privacy-policy).

If you get Python 3.10 or newer an virtual environment don active, install the SDK:

```sh
python -m pip install "mcp>=1.10,<2"
```

Save dis as `hosted_search.py` an run `python hosted_search.py`:

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

Expect say discovery go include `web_search` an `web_fetch`, followed by a search
response wey contain source URLs an excerpts. Results fit vary or be empty.
The script dey check `isError` because a tool fit fail even when the HTTP request
succeed. If access dey rate limited, wait before you try again. Reuse the same
`session_id` if you extend the script with related search or fetch calls.

Streamable HTTP allow both JSON and SSE responses; this server fit return a
complete JSON result without progress notifications. The SDK dey handle the
transport. Continue with the local example below to learn about notifications.
Dis optional script go do one explicit search an close its connection when
e finish. If you later expose these tools to an agent, the agent fit invoke
dem during im work; treat retrieved web text as untrusted data.

## Wetin be a Notification?

We tok "Notification", wetin e mean for MCP context?

A notification na JSON-RPC message wey no get `id` an e no
receive a response. MCP dey use notifications for progress, cancellation, and
other one-way events.

For MCP `2025-11-25`, a client sends `notifications/initialized` after the
initialization handshake. MCP `2026-07-28` no get initialization handshake, so
dis notification na legacy behavior.

Notification go look like dis as a JSON message:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Logging na one feature wey dey use notifications; notifications sef na a
general JSON-RPC message type.

> **Deprecated in MCP `2026-07-28`:** di Logging feature still dey available
> for compatibility but e fit get removal in the first specification
> revision wey dem release on or after July 28, 2027. New implementations suppose use
> `stderr` with stdio or OpenTelemetry for structured observability.

For a legacy `2025-11-25` implementation, server go enable the Logging
capability like dis:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Depending on di SDK wey you dey use, logging fit dey enabled by default, or you go need to explicitly enable am in your server configuration.

Dem get different types of notifications:

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

## Implementing Notifications in MCP

To implement notifications for MCP, you need set up both the server an client sides to handle real-time updates. Dis go allow your application give immediate feedback to users during long-running operations.

### Server-side: Sending Notifications

Make we start with server side. For MCP, you define tools wey fit send notifications while dem dey process requests. Server dey use context object (usually `ctx`) to send messages to client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

For di example wey pass, `process_files` tool dey send three notifications to client as e dey process each file. `ctx.info()` method dey use to send informational messages.

Also, to enable notifications, make sure say your server dey use streaming transport (like `streamable-http`) an your client implement message handler to process notifications. Na so you fit set up server to use `streamable-http` transport:

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

For dis .NET example, `ProcessFiles` tool get `Tool` attribute an e dey send three notifications to client as e dey process each file. `ctx.Info()` method dey use to send informational messages.

To enable notifications for your .NET MCP server, make sure you dey use a streaming transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Client-side: Receiving Notifications

Client must implement message handler to process an display notifications as dem arrive.

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

For the code wey come before, the `message_handler` function dey check if the incoming message na notification. If e be, e go print the notification; if no, e go process am as regular server message. Also note how the `ClientSession` dey initialized with the `message_handler` to handle incoming notifications.

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

For this .NET example, the `MessageHandler` function dey check if the incoming message na notification. If e be, e go print am; if no, e go process am as regular server message. The `ClientSession` dey initialized with the message handler via the `ClientSessionOptions`.

To enable notifications, make sure sey your server dey use a streaming transport (like `streamable-http`) and your client implement one message handler to process notifications.

## Progress Notifications & Scenarios

Dis section dey explain di idea of progress notifications for MCP, why dem matter, and how to implement dem using Streamable HTTP. You go also find one practical assignment wey go help solidify your understanding.

Progress notifications na real-time messages wey server dey send go client during long-running operations. Instead of make client wait until the whole process finish, the server go dey update the client about wetin dey happen now. This one dey improve transparency, user experience, and e make debugging easier.

**Example:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Why Use Progress Notifications?

Progress notifications dey important for plenty reasons:

- **Better user experience:** Users dey see updates as work dey progress, no be only for the end.
- **Real-time feedback:** Clients fit show progress bars or logs, make the app dey feel responsive.
- **Easier debugging and monitoring:** Developers and users fit see where a process fit dey slow or stuck.

### How You Go Implement Progress Notifications

Na so you fit implement progress notifications for MCP:

- **On the server:** Use `ctx.info()` or `ctx.log()` to send notifications as each item dey processed. This one go send message to the client before the main result ready.
- **On the client:** Implement message handler wey go listen and display notifications as dem show. This handler go sabi separate notifications from the final result.

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

Security suppose dey top priority when you dey implement any server, specially when you dey use HTTP-based transports like Streamable HTTP for MCP.

When you dey implement MCP servers with HTTP-based transports, security go become big concern wey need make you pay attention to different attack vectors and protection mechanisms.

### Overview

Security critical when you dey expose MCP servers over HTTP. Streamable HTTP dey introduce new attack surfaces and e need careful configuration.

Here are some key security considerations:

- **Origin Header Validation**: Make you always validate the `Origin` header to prevent DNS rebinding attacks.
- **Localhost Binding**: For local development, bind servers to `localhost` make dem no show for public internet.
- **Authentication**: Implement authentication (e.g., API keys, OAuth) for production deployments.
- **CORS**: Configure Cross-Origin Resource Sharing (CORS) policies to restrict access.
- **HTTPS**: Use HTTPS for production to encrypt traffic.

### Best Practices

Also, below na some best practices to follow when you dey implement security for your MCP streaming server:

- Never trust incoming requests without validation.
- Make you log and monitor all access and errors.
- Regularly update dependencies to fix security vulnerabilities.

### Challenges

You go face some challenges when you dey implement security for MCP streaming servers:

- Balancing security with ease of development
- Ensuring compatibility with different client environments


## Upgrading from SSE to Streamable HTTP

For apps wey dey use Server-Sent Events (SSE) now, to migrate go Streamable HTTP go give better capabilities and better long-term sustainability for your MCP implementations.

### Why Upgrade?

Two strong reasons dey to upgrade from SSE to Streamable HTTP:

- Streamable HTTP dey offer better scalability, compatibility, and richer notification support pass SSE.
- Na the recommended transport for new MCP applications.

### Migration Steps

Na so you fit migrate from SSE go Streamable HTTP for your MCP applications:

- **Update server code** to use `transport="streamable-http"` in `mcp.run()`.
- **Update client code** to use `streamablehttp_client` instead of SSE client.
- **Implement a message handler** in the client to process notifications.
- **Test for compatibility** with existing tools and workflows.

### Maintaining Compatibility

E recommended make you maintain compatibility with existing SSE clients during migration process. Below na some strategies:

- You fit support both SSE and Streamable HTTP by running both transports on different endpoints.
- Migrate clients small-small to the new transport.

### Challenges

Make sure sey you address the following challenges during migration:

- Make sure all clients dey updated
- Handling differences in notification delivery

### Assignment: Build Your Own Streaming MCP App

**Scenario:**
Build one MCP server and client wey server go process list of items (e.g., files or documents) and send notification for every item wey e process. The client suppose display each notification as e show.

**Steps:**

1. Implement one server tool wey go process list and send notifications for each item.
2. Implement client wey get message handler to display notifications for real time.
3. Test your implementation by running both server and client, and watch the notifications.

[Solution](./solution/README.md)

## Further Reading & What Next?

To continue your journey with MCP streaming and expand your knowledge, dis section go give additional resources and suggested next steps for building more advanced applications.

### Further Reading

- [Microsoft: Introduction to HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### What Next?

- Try build more advanced MCP tools wey dey use streaming for real-time analytics, chat, or collaborative editing.
- Try integrate MCP streaming with frontend frameworks (React, Vue, etc.) for live UI updates.
- Next: [Using Microsoft Foundry Toolkit for Visual Studio Code](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->