# 使用模型上下文協議 (MCP) 的 HTTPS 串流

本章提供了使用 HTTPS 實現安全、可擴展和實時串流的全面指南，並基於模型上下文協議 (MCP)。內容涵蓋了串流的動機、可用的傳輸機制、如何在 MCP 中實現可串流的 HTTP、安全最佳實踐、從 SSE 遷移的過程，以及構建您自己的 MCP 串流應用的實用指導。

## MCP 中的傳輸機制與串流

本節探討 MCP 中可用的不同傳輸機制及其在實現客戶端與伺服器之間實時通信中的作用。

### 什麼是傳輸機制？

傳輸機制定義了客戶端與伺服器之間數據交換的方式。MCP 支援多種傳輸類型，以適應不同的環境和需求：

- **stdio**：標準輸入/輸出，適用於本地和基於 CLI 的工具。簡單但不適合網頁或雲端環境。
- **SSE (伺服器推送事件)**：允許伺服器通過 HTTP 向客戶端推送實時更新。適合網頁 UI，但在可擴展性和靈活性方面有限。
- **可串流 HTTP**：基於現代 HTTP 的串流傳輸，支援通知並具有更好的可擴展性。推薦用於大多數生產和雲端場景。

### 比較表

以下是這些傳輸機制的比較表，幫助您了解它們之間的差異：

| 傳輸方式          | 實時更新       | 串流       | 可擴展性     | 使用場景                 |
|-------------------|---------------|-----------|-------------|-------------------------|
| stdio             | 否            | 否        | 低          | 本地 CLI 工具           |
| SSE               | 是            | 是        | 中          | 網頁、實時更新          |
| 可串流 HTTP       | 是            | 是        | 高          | 雲端、多客戶端          |

> **提示：** 選擇合適的傳輸方式會影響性能、可擴展性和用戶體驗。**可串流 HTTP** 是現代、可擴展和雲端就緒應用的推薦選擇。

請注意，前幾章中提到的 stdio 和 SSE 傳輸方式，而本章將重點介紹可串流 HTTP。

## 串流：概念與動機

理解串流的基本概念和動機是實現有效實時通信系統的關鍵。

**串流** 是一種網絡編程技術，允許數據以小塊或事件序列的形式發送和接收，而不是等待整個響應準備好後再傳輸。這在以下情況中特別有用：

- 大型文件或數據集。
- 實時更新（例如聊天、進度條）。
- 長時間運算，需向用戶提供即時信息。

以下是關於串流的一些高層次要點：

- 數據是逐步傳遞的，而不是一次性全部傳輸。
- 客戶端可以在數據到達時即時處理。
- 減少感知延遲，提升用戶體驗。

### 為什麼使用串流？

使用串流的原因如下：

- 用戶能立即獲得反饋，而不是等到最後。
- 支援實時應用和響應式 UI。
- 更高效地利用網絡和計算資源。

### 簡單示例：HTTP 串流伺服器與客戶端

以下是一個實現串流的簡單示例：

#### Python

**伺服器（使用 FastAPI 和 StreamingResponse）：**

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

**客戶端（使用 requests）：**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

此示例展示了伺服器在消息可用時即時發送給客戶端，而不是等待所有消息準備好後再發送。

**工作原理：**

- 伺服器在每條消息準備好時即時傳輸。
- 客戶端在每個數據塊到達時即時接收並打印。

**需求：**

- 伺服器必須使用串流響應（例如 FastAPI 中的 `StreamingResponse`）。
- 客戶端必須將響應作為串流處理（`stream=True`）。
- Content-Type 通常為 `text/event-stream` 或 `application/octet-stream`。

#### Java

**伺服器（使用 Spring Boot 和伺服器推送事件）：**

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

**客戶端（使用 Spring WebFlux WebClient）：**

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

**Java 實現注意事項：**

- 使用 Spring Boot 的反應式堆棧，通過 `Flux` 實現串流。
- `ServerSentEvent` 提供結構化的事件串流，支持事件類型。
- `WebClient` 的 `bodyToFlux()` 支援反應式串流消費。
- `delayElements()` 模擬事件之間的處理時間。
- 事件可以包含類型（如 `info`、`result`），便於客戶端處理。

### 比較：傳統串流與 MCP 串流

傳統 HTTP 串流與 MCP 串流的工作方式差異如下：

| 特性                  | 傳統 HTTP 串流               | MCP 串流（通知）               |
|-----------------------|-----------------------------|--------------------------------|
| 主響應               | 分塊傳輸                   | 單一響應，於最後傳輸           |
| 進度更新             | 作為數據塊發送             | 作為通知發送                   |
| 客戶端需求           | 必須處理串流               | 必須實現消息處理器             |
| 使用場景             | 大型文件、AI token 串流    | 進度、日誌、實時反饋           |

### 觀察到的主要差異

此外，以下是一些主要差異：

- **通信模式：**
  - 傳統 HTTP 串流：使用簡單的分塊傳輸編碼發送數據。
  - MCP 串流：使用結構化的通知系統，基於 JSON-RPC 協議。

- **消息格式：**
  - 傳統 HTTP：純文本數據塊，使用換行符分隔。
  - MCP：結構化的 `LoggingMessageNotification` 對象，包含元數據。

- **客戶端實現：**
  - 傳統 HTTP：簡單的客戶端處理串流響應。
  - MCP：更複雜的客戶端，需實現消息處理器以處理不同類型的消息。

- **進度更新：**
  - 傳統 HTTP：進度是主響應流的一部分。
  - MCP：進度通過單獨的通知消息發送，而主響應在最後傳輸。

### 推薦建議

在選擇實現傳統串流（如上述 `/stream` 端點）與 MCP 串流時，我們有以下建議：

- **對於簡單的串流需求：** 傳統 HTTP 串流實現更簡單，適合基本的串流需求。
- **對於複雜的交互式應用：** MCP 串流提供更結構化的方法，具有更豐富的元數據，並將通知與最終結果分離。
- **對於 AI 應用：** MCP 的通知系統特別適合長時間運行的 AI 任務，能夠即時向用戶提供進度更新。

## MCP 中的串流

好了，您已經了解了傳統串流與 MCP 串流的差異和建議。接下來，我們將詳細介紹如何在 MCP 中利用串流。

在 MCP 框架中，串流並不是將主響應分塊發送，而是指在工具處理請求時向客戶端發送**通知**。這些通知可以包括進度更新、日誌或其他事件。

### 工作原理

主結果仍然作為單一響應發送。然而，在處理過程中，通知可以作為單獨的消息發送，從而實時更新客戶端。客戶端必須能夠處理並顯示這些通知。

## 什麼是通知？

我們提到的「通知」，在 MCP 中是什麼意思？

通知是伺服器在長時間運行操作期間向客戶端發送的消息，用於告知進度、狀態或其他事件。通知提升了透明度和用戶體驗。

例如，客戶端應在與伺服器完成初始握手後發送通知。

通知是一條 JSON 消息，格式如下：

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

通知屬於 MCP 中稱為 ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging) 的主題。

要啟用日誌記錄，伺服器需要像這樣啟用該功能/能力：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 根據所使用的 SDK，日誌記錄可能默認啟用，也可能需要在伺服器配置中顯式啟用。

通知有不同的類型：

| 等級       | 描述                          | 示例使用場景                     |
|-----------|-------------------------------|---------------------------------|
| debug     | 詳細的調試信息                | 函數進入/退出點                 |
| info      | 一般信息性消息                | 操作進度更新                   |
| notice    | 正常但重要的事件              | 配置更改                       |
| warning   | 警告條件                      | 使用已棄用的功能               |
| error     | 錯誤條件                      | 操作失敗                       |
| critical  | 嚴重條件                      | 系統組件故障                   |
| alert     | 必須立即採取行動              | 檢測到數據損壞                 |
| emergency | 系統不可用                    | 完全系統故障                   |

## 在 MCP 中實現通知

要在 MCP 中實現通知，您需要在伺服器端和客戶端設置處理實時更新的功能。這使您的應用能夠在長時間運行操作期間向用戶提供即時反饋。

### 伺服器端：發送通知

從伺服器端開始。在 MCP 中，您可以定義工具，在處理請求時發送通知。伺服器使用上下文對象（通常是 `ctx`）向客戶端發送消息。

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

在上述示例中，`process_files` 工具在處理每個文件時向客戶端發送三條通知。使用 `ctx.info()` 方法發送信息性消息。

此外，為啟用通知，請確保您的伺服器使用串流傳輸（如 `streamable-http`），並且客戶端實現消息處理器以處理通知。以下是設置伺服器使用 `streamable-http` 傳輸的方法：

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

在此 .NET 示例中，`ProcessFiles` 工具使用 `Tool` 屬性進行裝飾，並在處理每個文件時向客戶端發送三條通知。使用 `ctx.Info()` 方法發送信息性消息。

要在 .NET MCP 伺服器中啟用通知，請確保您使用的是串流傳輸：

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### 客戶端：接收通知

客戶端必須實現消息處理器，以在通知到達時處理並顯示。

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

在上述代碼中，`message_handler` 函數檢查傳入消息是否為通知。如果是，則打印通知；否則將其作為普通伺服器消息處理。此外，請注意如何使用 `message_handler` 初始化 `ClientSession` 以處理傳入通知。

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

在此 .NET 示例中，`MessageHandler` 函數檢查傳入消息是否為通知。如果是，則打印通知；否則將其作為普通伺服器消息處理。通過 `ClientSessionOptions` 將消息處理器初始化到 `ClientSession`。

要啟用通知，請確保您的伺服器使用串流傳輸（如 `streamable-http`），並且客戶端實現消息處理器以處理通知。

## 進度通知與場景

本節解釋 MCP 中進度通知的概念、重要性，以及如何使用可串流 HTTP 實現它們。您還將找到一個實用的練習來加深理解。

進度通知是伺服器在長時間運行操作期間向客戶端發送的實時消息。伺服器在整個過程完成之前，持續向客戶端更新當前狀態。這提升了透明度、用戶體驗，並使調試更容易。

**示例：**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### 為什麼使用進度通知？

進度通知至關重要，原因如下：

- **更好的用戶體驗：** 用戶能在工作進行中看到更新，而不是僅在結束時。
- **實時反饋：** 客戶端可以顯示進度條或日誌，使應用更具響應性。
- **更容易調試和監控：** 開發者和用戶可以看到過程中可能緩慢或卡住的地方。

### 如何實現進度通知

以下是如何在 MCP 中實現進度通知：

- **伺服器端：** 使用 `ctx.info()` 或 `ctx.log()` 在處理每個項目時發送通知。在主結果準備好之前，這些通知會先發送給客戶端。
- **客戶端：** 實現一個消息處理器，監聽並顯示到達的通知。該處理器需區分通知與最終結果。

**伺服器示例：**

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    for i in range(1, 11):
        await ctx.info(f"Processing document {i}/10")
    await ctx.info("Processing complete!")
    return TextContent(type="text", text=f"Done: {message}")
```

**客戶端示例：**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## 安全考量

在使用基於 HTTP 的傳輸實現 MCP 伺服器時，安全性是需要仔細關注的首要問題，涉及多個攻擊向量和保護機制。

### 概述

當通過 HTTP 暴露 MCP 伺服器時，安全性至關重要。可串流 HTTP 引入了新的攻擊面，需謹慎配置。

### 關鍵要點

- **Origin 標頭驗證**：始終驗證 `Origin` 標頭以防止 DNS 重綁定攻擊。
- **本地主機綁定**：在本地開發中，將伺服器綁定到 `localhost`，避免暴露到公網。
- **身份驗證**：在生產環境中實現身份驗證（例如 API 金鑰、OAuth）。
- **CORS**：配置跨域資源共享（CORS）策略以限制訪問。
- **HTTPS**：在生產環境中使用 HTTPS 加密流量。

### 最佳實踐

- 不要信任未經驗證的傳入請求。
- 記錄並監控所有訪問和錯誤。
- 定期更新依賴項以修補安全漏洞。

### 挑戰

- 在安全性與開發便利性之間取得平衡。
- 確保與各種客戶端環境的兼容性。

## 從 SSE 升級到可串流 HTTP

對於目前使用伺服器推送事件 (SSE) 的應用，遷移到可串流 HTTP 可提供增強的功能和更好的長期可持續性，適用於您的 MCP 實現。

### 為什麼要升級？


有兩個令人信服的理由從 SSE 升級到 Streamable HTTP：

- Streamable HTTP 提供比 SSE 更好的可擴展性、兼容性以及更豐富的通知支持。
- 它是新 MCP 應用程式的推薦傳輸方式。

### 遷移步驟

以下是如何在您的 MCP 應用程式中從 SSE 遷移到 Streamable HTTP：

- **更新伺服器代碼**，在 `mcp.run()` 中使用 `transport="streamable-http"`。
- **更新客戶端代碼**，使用 `streamablehttp_client` 替代 SSE 客戶端。
- **在客戶端實現消息處理器**，以處理通知。
- **測試與現有工具和工作流程的兼容性**。

### 保持兼容性

建議在遷移過程中保持與現有 SSE 客戶端的兼容性。以下是一些策略：

- 您可以通過在不同的端點上運行 SSE 和 Streamable HTTP 來支持兩種傳輸方式。
- 逐步將客戶端遷移到新的傳輸方式。

### 挑戰

在遷移過程中，確保解決以下挑戰：

- 確保所有客戶端都已更新
- 處理通知傳遞方式的差異

## 安全考量

在實現任何伺服器時，安全性應該是首要任務，特別是當使用基於 HTTP 的傳輸方式（如 Streamable HTTP）於 MCP 中時。

當使用基於 HTTP 的傳輸方式實現 MCP 伺服器時，安全性成為一個至關重要的問題，需要仔細考慮多種攻擊向量和保護機制。

### 概述

當通過 HTTP 暴露 MCP 伺服器時，安全性至關重要。Streamable HTTP 引入了新的攻擊面，並需要謹慎配置。

以下是一些關鍵的安全考量：

- **Origin Header 驗證**：始終驗證 `Origin` 標頭以防止 DNS 重綁定攻擊。
- **本地主機綁定**：在本地開發時，將伺服器綁定到 `localhost`，以避免暴露於公共互聯網。
- **身份驗證**：在生產環境中實現身份驗證（例如 API 密鑰、OAuth）。
- **CORS**：配置跨來源資源共享（CORS）策略以限制訪問。
- **HTTPS**：在生產環境中使用 HTTPS 加密流量。

### 最佳實踐

此外，以下是實現 MCP 流式伺服器安全性時應遵循的一些最佳實踐：

- 不要信任未經驗證的傳入請求。
- 記錄並監控所有訪問和錯誤。
- 定期更新依賴項以修補安全漏洞。

### 挑戰

在實現 MCP 流式伺服器的安全性時，您可能會面臨以下挑戰：

- 在安全性與開發便利性之間取得平衡
- 確保與各種客戶端環境的兼容性

### 任務：構建您自己的流式 MCP 應用程式

**場景：**  
構建一個 MCP 伺服器和客戶端，其中伺服器處理一個項目列表（例如文件或文檔），並為每個處理的項目發送通知。客戶端應在通知到達時即時顯示。

**步驟：**

1. 實現一個伺服器工具，處理列表並為每個項目發送通知。
2. 實現一個客戶端，帶有消息處理器以即時顯示通知。
3. 通過運行伺服器和客戶端測試您的實現，並觀察通知。

[解決方案](./solution/README.md)

## 進一步閱讀與下一步？

為了繼續學習 MCP 流式傳輸並擴展您的知識，本節提供了額外的資源和建議的下一步，用於構建更高級的應用程式。

### 進一步閱讀

- [Microsoft: HTTP 流式傳輸簡介](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: 伺服器發送事件 (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET Core 中的 CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: 流式請求](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 下一步？

- 嘗試構建更多使用流式傳輸的高級 MCP 工具，例如即時分析、聊天或協作編輯。
- 探索將 MCP 流式傳輸與前端框架（React、Vue 等）集成，用於即時 UI 更新。
- 下一步：[利用 VSCode 的 AI 工具包](../07-aitk/README.md)

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。