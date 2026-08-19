# 使用模型上下文协议（MCP）的 HTTPS 流式传输

本章提供了使用 HTTPS 和模型上下文协议 (MCP) 实现安全、可扩展且实时流式传输的全面指南。涵盖了流媒体的动机、可用的传输机制、如何在 MCP 中实现支持流的 HTTP、最佳安全实践、从 SSE 迁移的方案，以及构建自己流式 MCP 应用的实用指导。

> **前瞻：** 本课描述了在 **MCP 规范 2025-11-25** 下的可流式 HTTP，其中会在 `initialize` 时建立会话，并通过 `Mcp-Session-Id` 头进行绑定。2026-07-28 版本候选将完全移除握手和会话 ID，使每个请求自包含且可路由至任何服务器实例，无需粘滞会话。详情见 [MCP 的变更：2026-07-28 版本候选](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)。

## MCP 中的传输机制和流式传输

本节探讨 MCP 中的不同传输机制及其在实现客户端与服务器之间实时通信流式传输功能中的作用。

### 什么是传输机制？

传输机制定义了客户端和服务器之间数据的交换方式。MCP 支持多种传输类型以适应不同的环境和需求：

- **stdio**：标准输入/输出，适用于本地和基于命令行的工具，简单但不适合 Web 或云环境。
- **SSE（服务器发送事件）**：允许服务器通过 HTTP 向客户端推送实时更新，适合 Web UI，但在可扩展性和灵活性方面有限。根据 MCP 规范 2025-06-18，独立的 SSE 传输已被弃用，替换为“可流式 HTTP”传输。
- **可流式 HTTP**：基于现代 HTTP 的流式传输，支持通知和更好的可扩展性。推荐用于大多数生产和云场景。

### 对比表

请参见下表，了解这些传输机制之间的区别：

| 传输方式          | 实时更新     | 流式传输    | 可扩展性   | 使用场景                |
|-------------------|--------------|-------------|-----------|-------------------------|
| stdio             | 不支持       | 不支持      | 低        | 本地命令行工具          |
| SSE               | 支持         | 支持        | 中        | Web，实时更新           |
| 可流式 HTTP       | 支持         | 支持        | 高        | 云，多客户端            |

> **提示：** 选择合适的传输方式会影响性能、可扩展性和用户体验。**可流式 HTTP** 推荐用于现代、可扩展且云就绪的应用。

请注意前几章介绍的 stdio 和 SSE 传输，以及本章所讲的流式 HTTP 传输。

## 流式传输：概念与动机

理解流式传输的基本概念和动机，对于实现高效的实时通信系统至关重要。

<strong>流式传输</strong> 是一种网络编程技术，允许以小块数据或事件序列的形式发送和接收数据，而不必等待整个响应准备完毕。这对于以下情形尤其有用：

- 大型文件或数据集。
- 实时更新（如聊天、进度条）。
- 长时间计算过程中保持用户信息更新。

高层次你需要了解的流式传输特性：

- 数据是渐进式传递的，而不是一次性发送。
- 客户端可以实时处理到达的数据。
- 减少感知延迟，提升用户体验。

### 为什么使用流式传输？

使用流式传输的原因包括：

- 用户能立即获得反馈，而不仅仅是在操作结束时。
- 支持实时应用和响应式 UI。
- 更高效地利用网络和计算资源。

### 简单示例：HTTP 流式服务器与客户端

以下是一个简单的流式实现示例：

#### Python

**服务器（Python，使用 FastAPI 和 StreamingResponse）：**

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

**客户端（Python，使用 requests）：**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

该示例展示服务器在消息就绪后逐条发送给客户端，而不是等待所有消息准备完成。

**工作原理：**

- 服务器在消息准备好时逐条生成（yield）。
- 客户端接收并打印每个接收到的数据块。

**要求：**

- 服务器必须使用流式响应（如 FastAPI 中的 `StreamingResponse`）。
- 客户端须将响应作为流处理（requests 中需要 `stream=True`）。
- Content-Type 通常为 `text/event-stream` 或 `application/octet-stream`。

#### Java

**服务器（Java，使用 Spring Boot 和服务器发送事件 SSE）：**

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

**客户端（Java，使用 Spring WebFlux WebClient）：**

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

**Java 实现说明：**

- 使用 Spring Boot 的响应式栈和 `Flux` 进行流式处理
- `ServerSentEvent` 提供结构化事件流及事件类型支持
- `WebClient` 通过 `bodyToFlux()` 实现响应式流消费
- `delayElements()` 模拟事件之间处理时间
- 事件可带类型（如 `info`、`result`）以便客户端更好处理

### 对比：经典流式传输 vs MCP 流式传输

经典流式传输和 MCP 流式传输的不同工作方式如下表所示：

| 特性                  | 经典 HTTP 流式传输           | MCP 流式传输（通知）            |
|----------------------|-----------------------------|--------------------------------|
| 主要响应              | 分块传输                    | 单次响应，尾部发送              |
| 进度更新              | 作为数据块发送              | 作为通知发送                    |
| 客户端要求            | 必须处理流式数据            | 必须实现消息处理器              |
| 使用场景              | 大文件，AI 令牌流            | 进度，日志，实时反馈            |

### 关键差异总结

另外，还有一些关键差异：

- **通信模式：**
  - 经典 HTTP 流式：用简单的分块编码以数据块形式发送数据
  - MCP 流式：使用 JSON-RPC 协议的结构化通知系统

- **消息格式：**
  - 经典 HTTP：纯文本块，带换行符
  - MCP：结构化 LoggingMessageNotification 对象，包含元数据

- **客户端实现：**
  - 经典 HTTP：简单客户端，直接处理流式响应
  - MCP：更复杂的客户端，包含消息处理器以处理不同消息类型

- **进度更新：**
  - 经典 HTTP：进度包含在主响应流中
  - MCP：通过独立通知消息发送进度，主响应最后发出

### 建议

对于选择经典流式（如上文 `/stream` 端点示例）还是 MCP 流式的选择，我们有以下建议：

- **简单流式需求：** 经典 HTTP 流式实现更简单，适合基础流式需求。

- **复杂、交互式应用：** MCP 流式提供更结构化的方案，拥有更丰富的元数据区分通知和最终结果。

- **AI 应用：** MCP 的通知系统非常适合长时间运行的 AI 任务，方便用户实时了解进度。

## MCP 中的流式传输

好的，到目前为止你已经看到了一些关于经典流式与 MCP 流式的推荐和对比。接下来详细介绍如何在 MCP 中利用流式传输。

理解 MCP 内流式传输的工作原理，对于构建响应式应用、在长时间操作中为用户提供实时反馈非常重要。

在 MCP 中，流式传输并不是将主响应分块传送，而是在工具处理请求时向客户端发送<strong>通知</strong>，这些通知可以包含进度更新、日志或其它事件。

### 工作原理

主结果仍作为单个响应发送。但通知会在处理过程中作为独立消息发送，从而实时更新客户端。客户端必须能够处理并显示这些通知。

## 什么是通知？

提到“通知”，在 MCP 的上下文中它指的是什么？

通知是服务器向客户端发送的消息，用于告知长时间运行操作中的进展、状态或其他事件。通知提升了透明度和用户体验。

例如，客户端应在与服务器完成初始握手后发送通知。

通知的 JSON 消息结构示例如下：

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

> **弃用通知：** 2026-07-28 MCP 规范版本候选标记 Logging 原语为弃用，推荐 stdio 传输使用 `stderr`，结构化可观测性使用 OpenTelemetry。Logging 在 2025-11-25 及至少一年内仍然有效。详见 [MCP 的变更：2026-07-28 版本候选](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)。

要启用记录，服务器需像下面这样开启该功能/能力：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 取决于所用 SDK，记录可能默认启用，或需在服务器配置中显式启用。

有多种类型的通知：

| 级别       | 描述                           | 示例用例                      |
|------------|--------------------------------|------------------------------|
| debug      | 详细调试信息                   | 函数入口/出口                |
| info       | 普通信息消息                   | 操作进度更新                |
| notice     | 正常但重要事件                 | 配置变更                    |
| warning    | 警告条件                       | 已弃用功能的使用            |
| error      | 错误条件                       | 操作失败                    |
| critical   | 严重条件                       | 系统组件故障                |
| alert      | 必须立即采取行动               | 检测到数据损坏              |
| emergency  | 系统不可用                     | 完整系统故障                |

## 在 MCP 中实现通知

要在 MCP 中实现通知，需要同时设置服务器端和客户端以处理实时更新。这允许应用在长时间运行操作期间为用户提供即时反馈。

### 服务器端：发送通知

从服务器端开始。在 MCP 中，你定义可在处理请求时发送通知的工具。服务器使用上下文对象（通常是 `ctx`）向客户端发送消息。

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

在上面的示例中，`process_files` 工具在处理每个文件时向客户端发送三条通知。使用 `ctx.info()` 方法发送信息性消息。

此外，为启用通知，请确保服务器使用流式传输（如 `streamable-http`），且客户端实现消息处理器处理通知。下面是服务器使用 `streamable-http` 传输的设置方法：

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

在此 .NET 示例中，`ProcessFiles` 工具使用了 `Tool` 特性并在处理每个文件时向客户端发送三条通知。`ctx.Info()` 用于发送信息性消息。

若要在你的 .NET MCP 服务器中启用通知，请确保你使用的是流式传输：

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### 客户端：接收通知

客户端必须实现消息处理器，能够在通知到达时进行处理和显示。

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

上述代码中，`message_handler` 函数检查接收到的消息是否为通知，是则打印，否则作为普通服务器消息处理。注意 `ClientSession` 初始化时传入了 `message_handler` 以处理接收的通知。

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

在此 .NET 示例中，`MessageHandler` 函数检查接收到的消息是否为通知，是则打印，否则作为普通服务器消息处理。`ClientSession` 通过 `ClientSessionOptions` 传入消息处理器进行初始化。

要启用通知，请确保服务器使用流式传输（如 `streamable-http`），且客户端实现消息处理器处理通知。

## 进度通知与场景

本节讲解 MCP 中进度通知的概念、重要性，以及如何使用可流式 HTTP 实现。还有一个实践作业帮你巩固理解。

进度通知是服务器在长时间运行操作过程中向客户端发送的实时消息。服务器不必等待整个过程结束，而是持续更新客户端当前状态。这提升透明度、用户体验，并简化调试。

**示例：**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### 为什么使用进度通知？

使用进度通知的若干理由：

- **更好用户体验：** 用户可在操作进行中看到更新，而不仅仅在结束时。
- **实时反馈：** 客户端可显示进度条或日志，应用更显响应迅速。
- **便捷调试与监控：** 开发者和用户能看到过程哪个环节可能变慢或卡住。

### 如何实现进度通知

在 MCP 中实现进度通知的方法：

- **服务器端：** 使用 `ctx.info()` 或 `ctx.log()` 来发送通知，每处理完一项就发送一条消息，在主结果准备好前通知客户端。
- **客户端：** 实现消息处理器，监听并展示通知，消息处理器能区分通知和最终结果。

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

实现任何服务器时，安全应是首要考虑，尤其是在使用基于 HTTP 传输（如 MCP 中的可流式 HTTP）时。

在使用基于 HTTP 传输的 MCP 服务器实现时，安全成为至关重要的问题，需要仔细关注多种攻击向量和防护机制。

### 概述

通过 HTTP 公开 MCP 服务器时，安全非常关键。可流式 HTTP 引入了新的攻击面，需要细致配置。

以下是一些主要的安全注意事项：

- **Origin 头验证**：始终验证 `Origin` 头以防止 DNS 反绑定攻击。
- <strong>本地主机绑定</strong>：在本地开发时，将服务器绑定到 `localhost`，避免暴露在公共互联网。
- <strong>认证</strong>：在生产部署中实现认证（例如 API 密钥、OAuth）。
- **CORS**：配置跨域资源共享（CORS）策略以限制访问。
- **HTTPS**：生产环境中使用 HTTPS 进行流量加密。

### 最佳实践

此外，以下是在实现 MCP 流式服务器安全时应遵循的一些最佳实践：

- 切勿信任未经验证的传入请求。
- 记录并监控所有访问和错误。
- 定期更新依赖项以修补安全漏洞。

### 挑战

实施 MCP 流式服务器安全时将面临一些挑战：

- 在安全性与开发便利性之间取得平衡
- 确保与各种客户端环境兼容


## 从 SSE 升级到可流式 HTTP

对于当前使用服务端事件（SSE）的应用，迁移到可流式 HTTP 可为您的 MCP 实现提供更强的功能和更好的长期可持续性。

### 为什么升级？

有两个令人信服的理由从 SSE 升级到可流式 HTTP：

- 可流式 HTTP 提供比 SSE 更好的可扩展性、兼容性及更丰富的通知支持。
- 它是新 MCP 应用推荐的传输方式。

### 迁移步骤

以下是在 MCP 应用中从 SSE 迁移到可流式 HTTP 的步骤：

- <strong>更新服务器代码</strong>，在 `mcp.run()` 中使用 `transport="streamable-http"`。
- <strong>更新客户端代码</strong>，使用 `streamablehttp_client` 替代 SSE 客户端。
- <strong>在客户端实现消息处理器</strong> 处理通知。
- <strong>测试兼容性</strong>，确保与现有工具和工作流兼容。

### 维护兼容性

建议在迁移过程中保持与现有 SSE 客户端的兼容。以下是一些策略：

- 通过在不同端点运行 SSE 和可流式 HTTP 两种传输，实现双重支持。
- 逐步将客户端迁移到新传输。

### 挑战

迁移过程中需解决以下挑战：

- 确保所有客户端均已更新
- 处理通知传递中的差异

### 任务：构建您自己的流式 MCP 应用

**场景：**
构建一个 MCP 服务器和客户端，服务器处理一个项目列表（如文件或文档），并为每个已处理项目发送通知。客户端应实时显示每条通知。

**步骤：**

1. 实现一个服务器工具，处理列表并为每个项目发送通知。
2. 实现包含消息处理器的客户端，实时显示通知。
3. 通过同时运行服务器和客户端测试您的实现，观察通知。

[解决方案](./solution/README.md)

## 进一步阅读与下一步

为了继续您的 MCP 流式学习之旅并扩展知识，本节提供额外资源和建议的下一步，以构建更高级的应用。

### 进一步阅读

- [Microsoft：HTTP 流式介绍](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft：服务端事件（SSE）](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft：ASP.NET Core 中的 CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests：流式请求](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 下一步

- 尝试构建更高级的 MCP 工具，使用流式实现实时分析、聊天或协作编辑。
- 探索将 MCP 流式集成到前端框架（React、Vue 等）以实现实时 UI 更新。
- 下一节：[VSCode 的 AI 工具包使用](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->