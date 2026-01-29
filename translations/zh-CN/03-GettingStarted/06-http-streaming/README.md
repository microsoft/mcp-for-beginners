# 使用模型上下文协议 (MCP) 的 HTTPS 流式传输

本章提供了使用 HTTPS 实现安全、可扩展和实时流式传输的全面指南，基于模型上下文协议 (MCP)。内容涵盖了流式传输的动机、可用的传输机制、如何在 MCP 中实现可流式的 HTTP、安全最佳实践、从 SSE 的迁移，以及构建您自己的 MCP 流式应用程序的实用指导。

## MCP 中的传输机制与流式传输

本节探讨了 MCP 中可用的不同传输机制及其在实现客户端与服务器之间实时通信中的作用。

### 什么是传输机制？

传输机制定义了客户端与服务器之间数据交换的方式。MCP 支持多种传输类型，以满足不同环境和需求：

- **stdio**：标准输入/输出，适用于本地和基于命令行工具的场景。简单但不适合 Web 或云环境。
- **SSE (服务器发送事件)**：允许服务器通过 HTTP 向客户端推送实时更新。适合 Web 界面，但在可扩展性和灵活性方面有限。
- **可流式 HTTP**：基于现代 HTTP 的流式传输机制，支持通知并具有更好的可扩展性。推荐用于大多数生产环境和云场景。

### 对比表

以下是这些传输机制的对比表：

| 传输方式           | 实时更新       | 流式传输 | 可扩展性 | 使用场景                 |
|-------------------|--------------|---------|---------|-------------------------|
| stdio             | 否           | 否      | 低       | 本地 CLI 工具            |
| SSE               | 是           | 是      | 中       | Web，实时更新            |
| 可流式 HTTP        | 是           | 是      | 高       | 云，多客户端             |

> **提示：** 选择合适的传输方式会影响性能、可扩展性和用户体验。**可流式 HTTP** 是现代、可扩展和云就绪应用程序的推荐选择。

注意，在前面的章节中介绍了 stdio 和 SSE，而本章将重点介绍可流式 HTTP。

## 流式传输：概念与动机

理解流式传输的基本概念和动机是实现有效实时通信系统的关键。

**流式传输** 是一种网络编程技术，允许数据以小块或事件序列的形式发送和接收，而不是等待整个响应准备好后再发送。这种技术特别适用于以下场景：

- 大型文件或数据集。
- 实时更新（例如聊天、进度条）。
- 长时间运行的计算任务，用户需要实时了解进展。

以下是流式传输的一些核心特点：

- 数据是逐步传递的，而不是一次性全部发送。
- 客户端可以在数据到达时立即处理。
- 减少感知延迟，提升用户体验。

### 为什么使用流式传输？

使用流式传输的原因包括：

- 用户可以立即获得反馈，而不是等到操作结束。
- 支持实时应用程序和响应式用户界面。
- 更高效地利用网络和计算资源。

### 简单示例：HTTP 流式服务器与客户端

以下是一个流式传输实现的简单示例：

#### Python

**服务器端（使用 FastAPI 和 StreamingResponse）：**

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

**客户端（使用 requests）：**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

此示例展示了服务器如何在消息准备好时逐条发送给客户端，而不是等待所有消息准备好后再发送。

**工作原理：**

- 服务器在每条消息准备好时生成并发送。
- 客户端在每个数据块到达时接收并打印。

**要求：**

- 服务器必须使用流式响应（例如 FastAPI 中的 `StreamingResponse`）。
- 客户端必须将响应作为流处理（`stream=True`）。
- Content-Type 通常为 `text/event-stream` 或 `application/octet-stream`。

#### Java

**服务器端（使用 Spring Boot 和服务器发送事件）：**

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

**客户端（使用 Spring WebFlux WebClient）：**

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

**Java 实现注意事项：**

- 使用 Spring Boot 的响应式栈，通过 `Flux` 实现流式传输。
- `ServerSentEvent` 提供了带有事件类型的结构化事件流。
- `WebClient` 的 `bodyToFlux()` 支持响应式流式消费。
- `delayElements()` 模拟事件之间的处理时间。
- 事件可以包含类型（如 `info`、`result`），以便客户端更好地处理。

### 对比：经典流式传输与 MCP 流式传输

经典 HTTP 流式传输与 MCP 流式传输的区别如下：

| 特性                  | 经典 HTTP 流式传输            | MCP 流式传输（通知）          |
|----------------------|-----------------------------|-----------------------------|
| 主响应               | 分块传输                     | 最终单一响应                 |
| 进度更新             | 作为数据块发送               | 作为通知发送                 |
| 客户端要求           | 必须处理流式响应             | 必须实现消息处理器           |
| 使用场景             | 大型文件、AI 令牌流          | 进度、日志、实时反馈         |

### 观察到的主要差异

此外，还有以下关键差异：

- **通信模式：**
  - 经典 HTTP 流式传输：使用简单的分块传输编码发送数据块。
  - MCP 流式传输：使用 JSON-RPC 协议的结构化通知系统。

- **消息格式：**
  - 经典 HTTP：纯文本块，使用换行符分隔。
  - MCP：带有元数据的结构化 `LoggingMessageNotification` 对象。

- **客户端实现：**
  - 经典 HTTP：简单的客户端处理流式响应。
  - MCP：更复杂的客户端，需要消息处理器来处理不同类型的消息。

- **进度更新：**
  - 经典 HTTP：进度是主响应流的一部分。
  - MCP：进度通过单独的通知消息发送，而主响应在最后返回。

### 推荐建议

在选择实现经典流式传输（如前面展示的 `/stream` 端点）还是 MCP 流式传输时，我们有以下建议：

- **对于简单的流式需求：** 经典 HTTP 流式传输更易于实现，适合基本的流式需求。
- **对于复杂的交互式应用程序：** MCP 流式传输提供了更结构化的方法，具有更丰富的元数据，并将通知与最终结果分离。
- **对于 AI 应用程序：** MCP 的通知系统特别适合长时间运行的 AI 任务，能够实时向用户提供进度更新。

## MCP 中的流式传输

好了，您已经看到了经典流式传输与 MCP 流式传输的对比和建议。接下来，我们将详细介绍如何在 MCP 中利用流式传输。

在 MCP 框架中，流式传输的重点不是将主响应分块发送，而是在工具处理请求时向客户端发送**通知**。这些通知可以包括进度更新、日志或其他事件。

### 工作原理

主结果仍然作为单一响应发送。然而，在处理过程中，通知可以作为单独的消息发送，从而实时更新客户端。客户端必须能够处理并显示这些通知。

## 什么是通知？

我们提到“通知”，那么在 MCP 中它具体指什么？

通知是服务器在长时间运行的操作期间发送给客户端的消息，用于告知进度、状态或其他事件。通知提高了透明度和用户体验。

例如，在客户端与服务器完成初始握手后，服务器应发送一条通知。

通知的 JSON 消息格式如下：

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

通知属于 MCP 中称为 ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) 的主题。

要启用日志记录，服务器需要像这样将其作为功能/能力启用：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 根据所使用的 SDK，日志记录可能默认启用，也可能需要在服务器配置中显式启用。

通知有不同的类型：

| 级别       | 描述                         | 示例使用场景                   |
|-----------|-----------------------------|-------------------------------|
| debug     | 详细的调试信息               | 函数入口/退出点               |
| info      | 一般信息性消息               | 操作进度更新                  |
| notice    | 正常但重要的事件             | 配置更改                     |
| warning   | 警告条件                     | 使用已弃用的功能              |
| error     | 错误条件                     | 操作失败                     |
| critical  | 严重条件                     | 系统组件故障                  |
| alert     | 必须立即采取行动             | 检测到数据损坏                |
| emergency | 系统不可用                   | 完全系统故障                  |

## 在 MCP 中实现通知

要在 MCP 中实现通知，您需要在服务器端和客户端设置处理实时更新的功能。这使您的应用程序能够在长时间运行的操作期间向用户提供即时反馈。

### 服务器端：发送通知

从服务器端开始。在 MCP 中，您可以定义工具，在处理请求时发送通知。服务器使用上下文对象（通常是 `ctx`）向客户端发送消息。

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

在上述示例中，`process_files` 工具在处理每个文件时向客户端发送三条通知。`ctx.info()` 方法用于发送信息性消息。

此外，为了启用通知，请确保您的服务器使用流式传输（如 `streamable-http`），并且客户端实现了消息处理器来处理通知。以下是设置服务器使用 `streamable-http` 传输的方法：

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

在此 .NET 示例中，`ProcessFiles` 工具通过 `Tool` 属性定义，并在处理每个文件时向客户端发送三条通知。`ctx.Info()` 方法用于发送信息性消息。

要在 .NET MCP 服务器中启用通知，请确保您使用流式传输：

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### 客户端：接收通知

客户端必须实现消息处理器，以便在通知到达时处理并显示。

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

在上述代码中，`message_handler` 函数检查传入消息是否为通知。如果是，则打印通知；否则将其作为常规服务器消息处理。此外，注意如何使用 `message_handler` 初始化 `ClientSession` 来处理传入通知。

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

在此 .NET 示例中，`MessageHandler` 函数检查传入消息是否为通知。如果是，则打印通知；否则将其作为常规服务器消息处理。通过 `ClientSessionOptions` 将消息处理器与 `ClientSession` 一起初始化。

为了启用通知，请确保您的服务器使用流式传输（如 `streamable-http`），并且客户端实现了消息处理器来处理通知。

## 进度通知与场景

本节解释了 MCP 中进度通知的概念、重要性，以及如何使用可流式 HTTP 实现它们。您还将找到一个实践任务来巩固您的理解。

进度通知是服务器在长时间运行的操作期间发送给客户端的实时消息。服务器在整个过程完成之前向客户端更新当前状态。这提高了透明度、用户体验，并使调试更容易。

**示例：**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### 为什么使用进度通知？

进度通知的重要性体现在以下几个方面：

- **更好的用户体验：** 用户可以在操作进行时看到更新，而不是等到结束。
- **实时反馈：** 客户端可以显示进度条或日志，使应用程序更具响应性。
- **更容易调试和监控：** 开发者和用户可以看到流程可能变慢或卡住的地方。

### 如何实现进度通知

以下是如何在 MCP 中实现进度通知：

- **在服务器端：** 使用 `ctx.info()` 或 `ctx.log()` 在每个项目处理时发送通知。这会在主结果准备好之前向客户端发送消息。
- **在客户端：** 实现一个消息处理器，监听并显示到达的通知。该处理器需要区分通知和最终结果。

**服务器示例：**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**客户端示例：**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## 安全注意事项

在使用基于 HTTP 的传输实现 MCP 服务器时，安全性是一个需要仔细关注的关键问题，涉及多个攻击向量和保护机制。

### 概述

当通过 HTTP 暴露 MCP 服务器时，安全性至关重要。可流式 HTTP 引入了新的攻击面，需要仔细配置。

### 关键点

- **Origin 头验证**：始终验证 `Origin` 头以防止 DNS 重绑定攻击。
- **绑定到 localhost**：在本地开发中，将服务器绑定到 `localhost`，以避免暴露到公共互联网。
- **认证**：在生产环境中实现认证（例如 API 密钥、OAuth）。
- **CORS**：配置跨域资源共享 (CORS) 策略以限制访问。
- **HTTPS**：在生产环境中使用 HTTPS 加密流量。

### 最佳实践

- 不要信任未经验证的传入请求。
- 记录并监控所有访问和错误。
- 定期更新依赖项以修补安全漏洞。

### 挑战

- 在开发便利性与安全性之间取得平衡。
- 确保与各种客户端环境的兼容性。

## 从 SSE 升级到可流式 HTTP

对于当前使用服务器发送事件 (SSE) 的应用程序，迁移到可流式 HTTP 可以增强功能并为 MCP 实现提供更好的长期可持续性。

### 为什么要升级？
从 SSE 升级到 Streamable HTTP 有两个重要原因：

- Streamable HTTP 比 SSE 提供更好的可扩展性、兼容性以及更丰富的通知支持。
- 它是新 MCP 应用程序推荐的传输方式。

### 迁移步骤

以下是如何在 MCP 应用程序中从 SSE 迁移到 Streamable HTTP 的方法：

- **更新服务器代码**，在 `mcp.run()` 中使用 `transport="streamable-http"`。
- **更新客户端代码**，使用 `streamablehttp_client` 替代 SSE 客户端。
- **在客户端实现消息处理器**，以处理通知。
- **测试与现有工具和工作流的兼容性**。

### 保持兼容性

建议在迁移过程中保持与现有 SSE 客户端的兼容性。以下是一些策略：

- 可以通过在不同的端点上运行两种传输方式来同时支持 SSE 和 Streamable HTTP。
- 逐步将客户端迁移到新的传输方式。

### 挑战

在迁移过程中需要解决以下挑战：

- 确保所有客户端都已更新
- 处理通知传递方式的差异

## 安全性考虑

在实现任何服务器时，安全性应是首要任务，尤其是在 MCP 中使用基于 HTTP 的传输方式（如 Streamable HTTP）时。

在使用基于 HTTP 的传输方式实现 MCP 服务器时，安全性成为一个至关重要的问题，需要仔细关注多个攻击向量和保护机制。

### 概述

当通过 HTTP 暴露 MCP 服务器时，安全性至关重要。Streamable HTTP 引入了新的攻击面，需要谨慎配置。

以下是一些关键的安全性考虑：

- **Origin Header 验证**：始终验证 `Origin` 头以防止 DNS 重绑定攻击。
- **绑定到 Localhost**：在本地开发时，将服务器绑定到 `localhost`，以避免暴露到公共互联网。
- **认证**：在生产环境中实现认证（例如 API 密钥、OAuth）。
- **CORS**：配置跨域资源共享（CORS）策略以限制访问。
- **HTTPS**：在生产环境中使用 HTTPS 加密流量。

### 最佳实践

此外，以下是实现 MCP 流服务器安全性时应遵循的一些最佳实践：

- 不要信任未经验证的传入请求。
- 记录并监控所有访问和错误。
- 定期更新依赖项以修复安全漏洞。

### 挑战

在实现 MCP 流服务器的安全性时，可能会面临以下挑战：

- 在安全性与开发便利性之间找到平衡
- 确保与各种客户端环境的兼容性

### 任务：构建自己的流式 MCP 应用程序

**场景：**
构建一个 MCP 服务器和客户端，服务器处理一个项目列表（例如文件或文档），并为每个处理的项目发送通知。客户端应实时显示每个到达的通知。

**步骤：**

1. 实现一个服务器工具，处理项目列表并为每个项目发送通知。
2. 实现一个客户端，使用消息处理器实时显示通知。
3. 通过运行服务器和客户端测试你的实现，并观察通知。

[解决方案](./solution/README.md)

## 进一步阅读与下一步

为了继续学习 MCP 流技术并扩展知识，本节提供了额外资源和建议的下一步，以构建更高级的应用程序。

### 进一步阅读

- [Microsoft: HTTP 流简介](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET Core 中的 CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: 流式请求](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 下一步

- 尝试构建更高级的 MCP 工具，使用流技术实现实时分析、聊天或协作编辑。
- 探索将 MCP 流与前端框架（React、Vue 等）集成，以实现实时 UI 更新。
- 下一步：[利用 VSCode 的 AI 工具包](../07-aitk/README.md)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。