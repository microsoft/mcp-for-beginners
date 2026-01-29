# HTTPS Streaming with Model Context Protocol (MCP)

This chapter provides a detailed guide on implementing secure, scalable, and real-time streaming with the Model Context Protocol (MCP) using HTTPS. It explains the motivation for streaming, available transport mechanisms, how to implement streamable HTTP in MCP, security best practices, migration from SSE, and practical advice for building your own streaming MCP applications.

## Transport Mechanisms and Streaming in MCP

This section discusses the various transport mechanisms available in MCP and their role in enabling real-time communication between clients and servers.

### What is a Transport Mechanism?

A transport mechanism defines how data is exchanged between the client and server. MCP supports multiple transport types to meet different environments and requirements:

- **stdio**: Standard input/output, suitable for local and CLI-based tools. Simple but not ideal for web or cloud scenarios.
- **SSE (Server-Sent Events)**: Enables servers to push real-time updates to clients over HTTP. Useful for web UIs but limited in scalability and flexibility.
- **Streamable HTTP**: A modern HTTP-based streaming transport that supports notifications and offers better scalability. Recommended for most production and cloud environments.

### Comparison Table

Below is a comparison table to highlight the differences between these transport mechanisms:

| Transport         | Real-time Updates | Streaming | Scalability | Use Case                |
|-------------------|------------------|-----------|-------------|-------------------------|
| stdio             | No               | No        | Low         | Local CLI tools         |
| SSE               | Yes              | Yes       | Medium      | Web, real-time updates  |
| Streamable HTTP   | Yes              | Yes       | High        | Cloud, multi-client     |

> **Tip:** Choosing the right transport affects performance, scalability, and user experience. **Streamable HTTP** is recommended for modern, scalable, and cloud-ready applications.

Note the transports stdio and SSE discussed in previous chapters, and how streamable HTTP is the focus of this chapter.

## Streaming: Concepts and Motivation

Understanding the core concepts and motivations behind streaming is crucial for implementing effective real-time communication systems.

**Streaming** is a network programming technique that allows data to be sent and received in small, manageable chunks or as a sequence of events, rather than waiting for the entire response to be ready. This is particularly useful for:

- Large files or datasets.
- Real-time updates (e.g., chat, progress bars).
- Long-running computations where users need to stay informed.

Key aspects of streaming:

- Data is delivered progressively, not all at once.
- The client processes data as it arrives.
- Reduces perceived latency and enhances user experience.

### Why use streaming?

Reasons for using streaming include:

- Immediate feedback for users, rather than waiting until the end.
- Enables real-time applications and responsive user interfaces.
- Efficient use of network and computing resources.

### Simple Example: HTTP Streaming Server & Client

Here’s a basic example of implementing streaming:

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

This example shows a server sending a series of messages to the client as they become available, rather than waiting for all messages to be ready.

**How it works:**

- The server yields each message as it becomes ready.
- The client receives and processes each chunk as it arrives.

**Requirements:**

- The server must use a streaming response (e.g., `StreamingResponse` in FastAPI).
- The client must process the response as a stream (`stream=True` in requests).
- Content-Type is typically `text/event-stream` or `application/octet-stream`.

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

- Uses Spring Boot’s reactive stack with `Flux` for streaming.
- `ServerSentEvent` provides structured event streaming with event types.
- `WebClient` with `bodyToFlux()` enables reactive streaming consumption.
- `delayElements()` simulates processing time between events.
- Events can include types (`info`, `result`) for better client handling.

### Comparison: Classic Streaming vs MCP Streaming

The differences between classic streaming and MCP streaming can be summarized as follows:

| Feature                | Classic HTTP Streaming         | MCP Streaming (Notifications)      |
|------------------------|-------------------------------|-------------------------------------|
| Main response          | Chunked                       | Single, at end                      |
| Progress updates       | Sent as data chunks           | Sent as notifications               |
| Client requirements    | Must process stream           | Must implement message handler      |
| Use case               | Large files, AI token streams | Progress, logs, real-time feedback  |

### Key Differences Observed

Additional differences include:

- **Communication Pattern:**
  - Classic HTTP streaming: Uses chunked transfer encoding to send data in chunks.
  - MCP streaming: Uses a structured notification system with JSON-RPC protocol.

- **Message Format:**
  - Classic HTTP: Plain text chunks with newlines.
  - MCP: Structured LoggingMessageNotification objects with metadata.

- **Client Implementation:**
  - Classic HTTP: Simple client that processes streaming responses.
  - MCP: More advanced client with a message handler to process different types of messages.

- **Progress Updates:**
  - Classic HTTP: Progress is part of the main response stream.
  - MCP: Progress is sent via separate notification messages, while the main response arrives at the end.

### Recommendations

When deciding between classic streaming and MCP streaming:

- **For simple streaming needs:** Classic HTTP streaming is easier to implement and sufficient for basic use cases.
- **For complex, interactive applications:** MCP streaming offers a more structured approach with richer metadata and separation between notifications and final results.
- **For AI applications:** MCP’s notification system is particularly useful for long-running AI tasks where users need progress updates.

## Streaming in MCP

Now that you’ve seen recommendations and comparisons, let’s dive into how streaming works in MCP.

In MCP, streaming doesn’t involve sending the main response in chunks. Instead, it focuses on sending **notifications** to the client during request processing. These notifications can include progress updates, logs, or other events.

### How it works

The main result is sent as a single response. Notifications are sent as separate messages during processing, providing real-time updates to the client. The client must handle and display these notifications.

## What is a Notification?

In MCP, a notification is a message sent from the server to the client to provide updates on progress, status, or other events during a long-running operation. Notifications enhance transparency and user experience.

For example, a client should send a notification after completing the initial handshake with the server.

A notification is represented as a JSON message:

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

Notifications belong to a topic in MCP called ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging).

To enable logging, the server must activate it as a feature/capability:

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> Depending on the SDK used, logging may be enabled by default, or you may need to explicitly enable it in your server configuration.

Types of notifications:

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

To implement notifications in MCP, both the server and client must be set up to handle real-time updates. This allows applications to provide immediate feedback during long-running operations.

### Server-side: Sending Notifications

On the server side, MCP tools can send notifications during request processing. The server uses the context object (usually `ctx`) to send messages to the client.

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

In this example, the `process_files` tool sends three notifications to the client as it processes each file. The `ctx.info()` method is used to send informational messages.

To enable notifications, ensure the server uses a streaming transport (like `streamable-http`) and the client implements a message handler to process notifications. Here’s how to configure the server for `streamable-http` transport:

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

In this .NET example, the `ProcessFiles` tool sends three notifications to the client as it processes each file. The `ctx.Info()` method is used to send informational messages.

To enable notifications in a .NET MCP server, ensure the use of a streaming transport:

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### Client-side: Receiving Notifications

The client must implement a message handler to process and display notifications as they arrive.

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

In this example, the `message_handler` function checks if the incoming message is a notification. If it is, it prints the notification; otherwise, it processes it as a regular server message. The `ClientSession` is initialized with the `message_handler` to handle incoming notifications.

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

In this .NET example, the `MessageHandler` function checks if the incoming message is a notification. If it is, it prints the notification; otherwise, it processes it as a regular server message. The `ClientSession` is initialized with the message handler via the `ClientSessionOptions`.

To enable notifications, ensure the server uses a streaming transport (like `streamable-http`) and the client implements a message handler to process notifications.

## Progress Notifications & Scenarios

This section explains progress notifications in MCP, their importance, and how to implement them using Streamable HTTP. A practical assignment is included to reinforce understanding.

Progress notifications are real-time messages sent from the server to the client during long-running operations. Instead of waiting for the entire process to finish, the server keeps the client updated on the current status, improving transparency, user experience, and debugging.

**Example:**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### Why Use Progress Notifications?

Progress notifications are important for several reasons:

- **Improved user experience:** Users see updates as work progresses, not just at the end.
- **Real-time feedback:** Clients can display progress bars or logs, making the app feel responsive.
- **Simplified debugging and monitoring:** Developers and users can identify slow or stuck processes.

### How to Implement Progress Notifications

To implement progress notifications in MCP:

- **On the server:** Use `ctx.info()` or `ctx.log()` to send notifications as each item is processed. This sends messages to the client before the main result is ready.
- **On the client:** Implement a message handler to listen for and display notifications as they arrive. The handler distinguishes between notifications and the final result.

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

When implementing MCP servers with HTTP-based transports, security is a critical concern that requires attention to multiple attack vectors and protection mechanisms.

### Overview

Security is essential when exposing MCP servers over HTTP. Streamable HTTP introduces new attack surfaces and requires careful configuration.

### Key Points

- **Origin Header Validation**: Always validate the `Origin` header to prevent DNS rebinding attacks.
- **Localhost Binding**: For local development, bind servers to `localhost` to avoid public exposure.
- **Authentication**: Use authentication methods (e.g., API keys, OAuth) for production deployments.
- **CORS**: Configure Cross-Origin Resource Sharing (CORS) policies to restrict access.
- **HTTPS**: Use HTTPS in production to encrypt traffic.

### Best Practices

- Validate all incoming requests.
- Log and monitor access and errors.
- Regularly update dependencies to address security vulnerabilities.

### Challenges

- Balancing security with development ease.
- Ensuring compatibility across client environments.

## Upgrading from SSE to Streamable HTTP

For applications currently using Server-Sent Events (SSE), migrating to Streamable HTTP offers enhanced capabilities and better long-term sustainability for MCP implementations.

### Why Upgrade?
There are two compelling reasons to upgrade from SSE to Streamable HTTP:

- Streamable HTTP offers better scalability, compatibility, and richer notification support than SSE.
- It is the recommended transport for new MCP applications.

### Migration Steps

Here's how you can migrate from SSE to Streamable HTTP in your MCP applications:

- **Update server code** to use `transport="streamable-http"` in `mcp.run()`.
- **Update client code** to use `streamablehttp_client` instead of SSE client.
- **Implement a message handler** in the client to process notifications.
- **Test for compatibility** with existing tools and workflows.

### Maintaining Compatibility

It's recommended to maintain compatibility with existing SSE clients during the migration process. Here are some strategies:

- You can support both SSE and Streamable HTTP by running both transports on different endpoints.
- Gradually migrate clients to the new transport.

### Challenges

Ensure you address the following challenges during migration:

- Ensuring all clients are updated
- Handling differences in notification delivery

## Security Considerations

Security should be a top priority when implementing any server, especially when using HTTP-based transports like Streamable HTTP in MCP. 

When implementing MCP servers with HTTP-based transports, security becomes a paramount concern that requires careful attention to multiple attack vectors and protection mechanisms.

### Overview

Security is critical when exposing MCP servers over HTTP. Streamable HTTP introduces new attack surfaces and requires careful configuration.

Here are some key security considerations:

- **Origin Header Validation**: Always validate the `Origin` header to prevent DNS rebinding attacks.
- **Localhost Binding**: For local development, bind servers to `localhost` to avoid exposing them to the public internet.
- **Authentication**: Implement authentication (e.g., API keys, OAuth) for production deployments.
- **CORS**: Configure Cross-Origin Resource Sharing (CORS) policies to restrict access.
- **HTTPS**: Use HTTPS in production to encrypt traffic.

### Best Practices

Additionally, here are some best practices to follow when implementing security in your MCP streaming server:

- Never trust incoming requests without validation.
- Log and monitor all access and errors.
- Regularly update dependencies to patch security vulnerabilities.

### Challenges

You will face some challenges when implementing security in MCP streaming servers:

- Balancing security with ease of development
- Ensuring compatibility with various client environments

### Assignment: Build Your Own Streaming MCP App

**Scenario:**
Build an MCP server and client where the server processes a list of items (e.g., files or documents) and sends a notification for each item processed. The client should display each notification as it arrives.

**Steps:**

1. Implement a server tool that processes a list and sends notifications for each item.
2. Implement a client with a message handler to display notifications in real time.
3. Test your implementation by running both server and client, and observe the notifications.

[Solution](./solution/README.md)

## Further Reading & What Next?

To continue your journey with MCP streaming and expand your knowledge, this section provides additional resources and suggested next steps for building more advanced applications.

### Further Reading

- [Microsoft: Introduction to HTTP Streaming](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: CORS in ASP.NET Core](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: Streaming Requests](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### What Next?

- Try building more advanced MCP tools that use streaming for real-time analytics, chat, or collaborative editing.
- Explore integrating MCP streaming with frontend frameworks (React, Vue, etc.) for live UI updates.
- Next: [Utilising AI Toolkit for VSCode](../07-aitk/README.md)

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.