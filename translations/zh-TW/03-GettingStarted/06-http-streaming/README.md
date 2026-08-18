# 使用模型上下文協議（MCP）的 HTTPS 串流

本章節提供使用 HTTPS 透過模型上下文協議（MCP）實現安全、可擴展且即時串流的完整指南。內容涵蓋串流的動機、可用的傳輸機制、如何在 MCP 中實現可串流的 HTTP、安全最佳實踐、從 SSE 遷移以及構建您自己的串流 MCP 應用程式的實務指導。

> **展望未來：** 本課程說明了基於 **MCP 2025-11-25 規範** 下的可串流 HTTP，其中會在 `initialize` 階段建立會話，並以 `Mcp-Session-Id` 標頭釘住會話。`2026-07-28` 發行候選版本完全移除握手及會話 ID，使每個請求皆為自包含且可路由至任何伺服器實例，無需粘性會話。詳情請參見 [MCP 變更：2026-07-28 發行候選版本](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)。

## MCP 中的傳輸機制與串流

本節探討 MCP 中可用的不同傳輸機制及其在實現用戶端與伺服器間即時通訊串流功能的重要性。

### 什麼是傳輸機制？

傳輸機制定義了資料如何在用戶端與伺服器間交換。MCP 支援多種傳輸類型以符合不同環境與需求：

- **stdio**：標準輸入/輸出，適用於本地與 CLI 工具。簡單但不適合網路或雲端使用。
- **SSE（伺服器推送事件）**：允許伺服器通過 HTTP 推送即時更新給用戶端。適合 Web UI，但在可擴展性與彈性方面有限。自 MCP 2025-06-18 規範起，獨立 SSE 傳輸已被棄用，改為使用「可串流 HTTP」傳輸。
- **可串流 HTTP**：現代 HTTP 基礎的串流傳輸，支援通知及更佳的可擴展性。建議用於大多數生產與雲端場景。

### 比較表

請參考以下比較表了解這些傳輸機制之間的差異：

| 傳輸             | 即時更新         | 串流         | 可擴展性     | 使用案例                   |
|------------------|-----------------|-------------|------------|----------------------------|
| stdio            | 否              | 否          | 低          | 本地 CLI 工具               |
| SSE              | 是              | 是          | 中          | 網頁，即時更新              |
| 可串流 HTTP      | 是              | 是          | 高          | 雲端，多用戶                |

> **提示：** 選擇正確的傳輸影響效能、可擴展性和用戶體驗。**可串流 HTTP** 是現代、可擴展且適合雲端應用的推薦選項。

請注意您在前面章節看到的 stdio 和 SSE 傳輸，以及本章涵蓋的可串流 HTTP 傳輸。

## 串流：概念與動機

理解串流的基本概念與動機對於實現有效的即時通訊系統至關重要。

<strong>串流</strong> 是一種網路程式設計技術，允許資料以小而可管理的區塊或事件序列傳送與接收，而非等待整個回應準備好。這對以下情況尤其有用：

- 大型檔案或資料集。
- 即時更新（例如聊天、進度條）。
- 長時間運算，且希望持續通知使用者。

以下是您對串流需要了解的重點：

- 資料是逐步送達，而非一次傳完。
- 用戶端可一邊接收一邊處理資料。
- 減少感知延遲，提升用戶體驗。

### 為什麼使用串流？

使用串流的原因包括：

- 使用者能立即獲得回饋，而非僅在結束時。
- 支援即時應用與回應快速的 UI。
- 更有效率利用網路與計算資源。

### 簡單範例：HTTP 串流伺服器與客戶端

以下為一個如何實作串流的簡單範例：

#### Python

**伺服器（Python，使用 FastAPI 與 StreamingResponse）：**

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

**客戶端（Python，使用 requests）：**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

這個範例示範伺服器在有訊息可用時，逐一發送給用戶端，而非等待所有訊息準備好。

**運作方式：**

- 伺服器一有消息即產生。
- 用戶端收到並即時印出每個區塊。

**需求：**

- 伺服器需使用串流回應（如 FastAPI 中的 `StreamingResponse`）。
- 用戶端需以串流方式處理回應（requests 的 `stream=True`）。
- Content-Type 通常為 `text/event-stream` 或 `application/octet-stream`。

#### Java

**伺服器（Java，使用 Spring Boot 與 Server-Sent Events）：**

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

**客戶端（Java，使用 Spring WebFlux WebClient）：**

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

**Java 實作說明：**

- 使用 Spring Boot 反應式棧與 `Flux` 進行串流
- `ServerSentEvent` 提供結構化事件串流與事件類型
- `WebClient` 搭配 `bodyToFlux()` 支援反應式串流消費
- `delayElements()` 用於模擬事件間的處理延遲
- 事件可帶類型（`info`，`result`），便於用戶端處理

### 比較：傳統串流 vs MCP 串流

傳統串流與 MCP 串流的運作差異可示如下：

| 功能                 | 傳統 HTTP 串流              | MCP 串流（通知）                |
|-----------------------|-----------------------------|---------------------------------|
| 主要回應             | 分塊傳送                    | 單一回應於末端                  |
| 進度更新             | 作為資料區塊傳送            | 作為通知傳送                    |
| 用戶端需求           | 必須處理串流                | 必須實作訊息處理器              |
| 使用案例             | 大型檔案、AI 令牌串流        | 進度、日誌、即時回饋            |

### 觀察到的主要差異

此外，還有一些主要差異：

- **通訊模式：**
  - 傳統 HTTP 串流：利用簡易的區塊傳輸編碼分塊送出資料
  - MCP 串流：使用結構化通知系統，以 JSON-RPC 協議傳遞

- **訊息格式：**
  - 傳統 HTTP：純文字區塊帶換行符
  - MCP：結構化 LoggingMessageNotification 物件帶有元數據

- **用戶端實作：**
  - 傳統 HTTP：簡單用戶端處理串流回應
  - MCP：較複雜用戶端用訊息處理器處理不同訊息類型

- **進度更新：**
  - 傳統 HTTP：進度為主回應串流的一部分
  - MCP：進度透過獨立通知訊息傳送，主回應則在最後

### 建議事項

在選擇實作傳統串流（作為我們前面示範用 `/stream` 的端點）或 MCP 串流時，我們建議：

- **簡單串流需求：** 傳統 HTTP 串流實作較為簡單，足以滿足基本串流需求。

- **複雜互動應用：** MCP 串流提供結構化方法，帶有豐富元數據，可區分通知和最終結果。

- **AI 應用：** MCP 的通知系統尤其適用於長時間執行的 AI 任務，方便持續向用戶通報進度。

## MCP 中的串流

好的，您已經看到有關傳統串流與 MCP 串流的建議與比較。接下來讓我們深入了解如何在 MCP 中利用串流。

理解 MCP 框架內串流的運作對構建可在長時間操作中即時回饋用戶的響應式應用至關重要。

在 MCP 中，串流不是把主要回應分塊傳送，而是向用戶端發送<strong>通知</strong>，同時工具在處理請求。這些通知可包含進度更新、日誌或其他事件。

### 運作原理

主要結果依然以單一回應送出，但通知可在處理過程中以獨立訊息發送，從而實時更新客戶端。用戶端必須能處理並顯示這些通知。

## 什麼是通知？

我們說「通知」，在 MCP 中是什麼意思？

通知是伺服器向用戶端發送的訊息，用以通報進度、狀態或長時間操作中的其他事件。通知提升透明度與用戶體驗。

例如，用戶端應在與伺服器完成初始握手後發送通知。

通知的 JSON 訊息格式如下：

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

通知屬於 MCP 中稱為「[Logging](https://modelcontextprotocol.io/specification/draft/server/utilities/logging)」的主題。

> **棄用公告：** 2026-07-28 MCP 規範發行候選版本標記 Logging 原語為棄用，改用 stdio 傳輸的 `stderr` 與結構化可觀測性的 OpenTelemetry。Logging 在 2025-11-25 版本及任何正式棄用後至少一年內仍可使用。詳見 [MCP 變更：2026-07-28 發行候選版本](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)。

要啟用 Logging，伺服器需像以下啟用此功能/能力：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 依您使用的 SDK，Logging 可能預設開啟，或需在伺服器設定中明確啟用。

不同類型的通知：

| 等級       | 描述                         | 範例使用情況                   |
|-----------|-----------------------------|------------------------------|
| debug     | 詳細調試資訊                 | 函數進入/離開點               |
| info      | 一般資訊訊息                 | 操作進度更新                 |
| notice    | 正常且重要事件               | 設定變更                     |
| warning   | 警告狀況                     | 過時功能使用                 |
| error     | 錯誤狀況                     | 操作失敗                     |
| critical  | 關鍵狀況                     | 系統組件故障                 |
| alert     | 必須立即採取行動             | 偵測到資料損壞               |
| emergency | 系統無法使用                 | 完整系統故障                 |

## 在 MCP 中實作通知

要在 MCP 中實作通知，您需在伺服器與用戶端兩邊設置處理即時更新的機制。如此您的應用能在長時間操作時立即回饋用戶。

### 伺服器端：發送通知

從伺服器端開始。在 MCP 中，您定義工具可在處理請求時發送通知。伺服器使用上下文物件（通常為 `ctx`）向用戶端發送訊息。

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

在上述範例中，`process_files` 工具在處理每個檔案時向用戶端發送三次通知。`ctx.info()` 方法用於發送資訊訊息。

此外，為啟用通知，請確保您的伺服器使用串流傳輸（如 `streamable-http`），且用戶端實作訊息處理器用以處理通知。以下示範如何設置伺服器以使用 `streamable-http` 傳輸：

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

在此 .NET 範例中，`ProcessFiles` 工具以 `Tool` 屬性標註，並在處理每個檔案時向用戶端發送三次通知。`ctx.Info()` 方法用以發送資訊訊息。

若要在您的 .NET MCP 伺服器啟用通知，請確保您使用串流傳輸：

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### 用戶端：接收通知

用戶端必須實作訊息處理器，以便接收並顯示通知。

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

在上述程式碼中，`message_handler` 函式會檢查進入訊息是否為通知，若是則印出通知，否則視為一般伺服器訊息處理。注意 `ClientSession` 是如何以 `message_handler` 初始化來處理接收通知。

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

在此 .NET 範例中，`MessageHandler` 函式亦會檢查進入訊息是否為通知，若是則印出通知，否則視為一般伺服器訊息處理。`ClientSession` 透過 `ClientSessionOptions` 初始化並設定訊息處理器。

為開啟通知功能，請確認您的伺服器使用串流傳輸（如 `streamable-http`），且用戶端已實作訊息處理器處理通知。

## 進度通知與場景

本節說明 MCP 中的進度通知概念、其重要性，以及如何利用可串流 HTTP 實作。並提供實作練習以加深理解。

進度通知指的是伺服器在長時間操作過程中，向用戶端發送的即時訊息。伺服器不需等待整個流程結束，便能持續更新當前狀態，提升透明度、使用者體驗，同時方便除錯。

**範例：**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### 為何使用進度通知？

進度通知之所以重要，原因如下：

- **更佳用戶體驗：** 使用者能隨著工作的進行即時看到更新，不必只等待結束。
- **即時回饋：** 用戶端能顯示進度條或日誌，使用起來更順暢。
- **更易除錯與監控：** 開發者與使用者能看出流程的瓶頸或停滯處所。

### 如何實作進度通知

以下為您在 MCP 中實作進度通知的方法：

- **伺服器端：** 使用 `ctx.info()` 或 `ctx.log()` 當每項目處理完成時發送通知。這會在主要結果準備好前向用戶端發送訊息。
- **用戶端：** 實作訊息處理器監聽並顯示收到的通知。該處理器能區分通知與最終結果。

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

**客戶端範例:**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## 安全性考量

在實作任何伺服器時，安全性應該是首要考量，尤其是使用像 MCP 中的可串流 HTTP 這類基於 HTTP 的傳輸時。

在使用基於 HTTP 的傳輸實作 MCP 伺服器時，安全性成為一個極其重要的議題，需要仔細注意多種攻擊向量與防護機制。

### 概覽

當暴露 MCP 伺服器於 HTTP 上時，安全性至關重要。可串流 HTTP 引入新的攻擊面，需謹慎配置。

以下是一些主要的安全性考量：

- **Origin 標頭驗證**：務必驗證 `Origin` 標頭，以防止 DNS 重綁定攻擊。
- <strong>本地主機綁定</strong>：本地開發時，將伺服器綁定至 `localhost`，避免將伺服器暴露於公共網路。
- <strong>認證</strong>：在正式部署時實作認證（例如 API 金鑰、OAuth）。
- **CORS**：配置跨來源資源共享 (CORS) 政策以限制存取。
- **HTTPS**：在正式環境中使用 HTTPS 加密流量。

### 最佳實踐

此外，以下是在實作 MCP 串流伺服器安全性時應遵循的一些最佳實踐：

- 不要輕信任何未經驗證的傳入請求。
- 記錄並監控所有存取和錯誤。
- 定期更新相依套件，以修補安全漏洞。

### 挑戰

在 MCP 串流伺服器中實作安全性時，將會面臨一些挑戰：

- 在安全性與開發便捷性間取得平衡
- 確保與多樣化客戶端環境相容


## 從 SSE 升級到可串流 HTTP

對於目前使用 Server-Sent Events (SSE) 的應用程式，遷移到可串流 HTTP 可以為您的 MCP 實作帶來更強的功能與更好的長期可維護性。

### 為何要升級？

有兩個令人信服的理由促使您從 SSE 升級到可串流 HTTP：

- 可串流 HTTP 在擴展性、相容性和通知支援上都優於 SSE。
- 它是為新 MCP 應用程式推薦的傳輸方式。

### 遷移步驟

以下是在您的 MCP 應用中從 SSE 遷移到可串流 HTTP 的方法：

- <strong>更新伺服器程式碼</strong>，在 `mcp.run()` 中使用 `transport="streamable-http"`。
- <strong>更新客戶端程式碼</strong>，使用 `streamablehttp_client` 取代 SSE 客戶端。
- <strong>實作訊息處理器</strong>，於客戶端處理通知。
- <strong>測試相容性</strong>，確保與現有工具和工作流程兼容。

### 維持相容性

建議在遷移過程中維持與現有 SSE 客戶端的相容性。以下是一些策略：

- 可通過在不同端點啟用 SSE 和可串流 HTTP 兩種傳輸方式來同時支持兩者。
- 逐步將客戶端遷移到新傳輸。

### 挑戰

在遷移過程中，請確實解決以下挑戰：

- 確保所有客戶端均已更新
- 處理通知傳遞上的差異

### 作業：自行構建串流 MCP 應用

**情境：**
建立一個 MCP 伺服器與客戶端，伺服器可處理一組項目（例如檔案或文件），並在處理每個項目時發送通知。客戶端應即時顯示每條通知。

**步驟：**

1. 實作伺服器工具以處理清單並針對每個項目發送通知。
2. 實作具備訊息處理器的客戶端，實時顯示通知。
3. 執行伺服器及客戶端測試，觀察通知現況。

[解答](./solution/README.md)

## 延伸閱讀與後續步驟

繼續您的 MCP 串流之旅並擴展知識，本節提供額外資源和建議的後續步驟，以建構更進階的應用。

### 延伸閱讀

- [Microsoft：HTTP 串流介紹](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft：Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft：ASP.NET Core 中的 CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests：串流請求](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 後續步驟

- 嘗試建構更進階的 MCP 工具，利用串流實現即時分析、聊天或協同編輯。
- 探索將 MCP 串流整合到前端框架 (React、Vue 等)，實作即時 UI 更新。
- 下一步：[利用 VSCode 的 AI 工具包](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->