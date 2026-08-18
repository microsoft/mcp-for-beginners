# 使用 Model Context Protocol (MCP) 的 HTTPS 串流

本章提供有關使用 HTTPS 透過 Model Context Protocol (MCP) 實作安全、可擴展以及即時串流的完整指南。涵蓋串流動機、可用的傳輸機制、如何在 MCP 中實作可串流 HTTP、安全最佳實踐、從 SSE 的遷移，以及構建您自己的串流 MCP 應用程式的實用指導。

> **前瞻提示：** 本課程描述了依據 **MCP 規格 2025-11-25** 的可串流 HTTP，其中會在 `initialize` 期間建立會話並以 `Mcp-Session-Id` 標頭加以綁定。`2026-07-28` 的發行候選版本將完全移除握手和會話 ID，使每個請求皆為自包含且可路由至任何伺服器實例，無需粘性會話。詳情請參閱 [MCP 的變更：2026-07-28 發行候選版本](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)。

## MCP 中的傳輸機制與串流

本節探討 MCP 中可用的不同傳輸機制及其在促進用戶端和伺服器之間即時通信串流功能中的角色。

### 什麼是傳輸機制？

傳輸機制定義資料在客戶端與伺服器之間如何交換。MCP 支援多種傳輸類型，以適應不同環境和需求：

- **stdio**：標準輸入/輸出，適合本地及 CLI 基礎工具。簡單但不適合網路或雲端。
- **SSE（伺服器傳送事件）**：允許伺服器透過 HTTP 推送即時更新給客戶端。適用於 Web UI，但可擴展性和彈性有限。根據 MCP 規格 2025-06-18，獨立的 SSE 傳輸已被棄用並被「可串流 HTTP」傳輸所取代。
- **可串流 HTTP**：基於現代 HTTP 的串流傳輸，支援通知與更佳的可擴展性。推薦用於大多數生產和雲端場景。

### 比較表

請參考下方比較表以了解這些傳輸機制之間的差異：

| 傳輸           | 即時更新        | 串流       | 可擴展性     | 使用案例                |
|----------------|-----------------|------------|--------------|-------------------------|
| stdio          | 否              | 否         | 低           | 本地 CLI 工具           |
| SSE            | 是              | 是         | 中           | 網頁，即時更新          |
| 可串流 HTTP    | 是              | 是         | 高           | 雲端，多客戶端          |

> **提示：** 選擇正確的傳輸會影響性能、可擴展性及使用者體驗。**可串流 HTTP** 推薦用於現代、可擴展且雲端準備的應用。

請注意先前章節中展示的 stdio 和 SSE 傳輸，以及本章涉及的可串流 HTTP 傳輸。

## 串流：概念與動機

理解串流的基本概念和動機對於實作有效的即時通信系統至關重要。

<strong>串流</strong> 是網絡編程中的一種技術，允許資料以小而可管理的區塊或連續事件序列傳送和接收，而不是等待整個回應準備好後一次傳送。這在以下情況特別有用：

- 大型檔案或資料集。
- 即時更新（例如聊天、進度條）。
- 長時間運算中需要持續向使用者回報狀態。

以下是您需要了解的串流高層次概念：

- 資料是漸進式遞送，而非一次傳完。
- 客戶端可在資料抵達時即時處理。
- 降低感知延遲並改善使用者體驗。

### 為什麼使用串流？

使用串流的理由包括：

- 使用者能立即獲得回饋，而不必等待最終結果。
- 支援即時應用及回應式 UI。
- 更有效利用網路和運算資源。

### 簡單示例：HTTP 串流伺服器與客戶端

以下是串流如何實作的簡單範例：

#### Python

**伺服器（Python，使用 FastAPI 和 StreamingResponse）：**

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

此範例展示伺服器隨著訊息可用即發送消息給客戶端，而非等所有訊息準備好才一次傳送。

**運作原理：**

- 伺服器在每則消息準備好時即發布。
- 客戶端在每個區塊抵達時接收並輸出。

**需求：**

- 伺服器必須使用串流回應（例如 FastAPI 的 `StreamingResponse`）。
- 客戶端必須將回應視為串流處理（requests 中需 `stream=True`）。
- Content-Type 通常為 `text/event-stream` 或 `application/octet-stream`。

#### Java

**伺服器（Java，使用 Spring Boot 和 Server-Sent Events）：**

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

- 使用 Spring Boot 反應式堆疊，透過 `Flux` 實現串流
- `ServerSentEvent` 提供帶有事件類型的結構化事件串流
- 透過 `WebClient` 的 `bodyToFlux()` 支援反應式串流消費
- `delayElements()` 用於模擬事件間處理時間
- 事件可帶有類型（`info`、`result`）供客戶端更佳處理

### 比較：經典串流 vs MCP 串流

MCP 串流與「經典」串流的運作差異如下所示：

| 特徵               | 經典 HTTP 串流              | MCP 串流（通知）               |
|--------------------|-----------------------------|-------------------------------|
| 主要回應           | 區塊傳送                     | 單一，於末尾傳送              |
| 進度更新           | 作為資料區塊傳送             | 作為通知訊息傳送              |
| 客戶端需求         | 必須處理串流                 | 必須實現訊息處理器            |
| 使用情境           | 大型檔案、AI 代幣串流        | 進度、日誌、即時回饋          |

### 觀察到的主要差異

此外，還有以下一些主要差異：

- **通信模式：**
  - 經典 HTTP 串流：使用簡單的分塊傳輸編碼分塊傳送資料
  - MCP 串流：使用基於 JSON-RPC 協議的結構化通知系統

- **訊息格式：**
  - 經典 HTTP：帶換行符的純文字區塊
  - MCP：帶元資料的結構化 LoggingMessageNotification 物件

- **客戶端實作：**
  - 經典 HTTP：簡單客戶端處理串流回應
  - MCP：更複雜的客戶端實現，含訊息處理器處理多種訊息類型

- **進度更新：**
  - 經典 HTTP：進度是主要回應串流的一部分
  - MCP：進度以獨立通知訊息傳送，主回應於末尾送出

### 建議

關於選擇實作經典串流（上述以 `/stream` 端點示範）或 MCP 串流，有以下建議：

- **簡單串流需求：** 經典 HTTP 串流較易實作，適用基本串流需求。

- **複雜互動應用：** MCP 串流提供更結構化的方法，附帶更豐富元資料及通知與最終結果分離。

- **AI 應用：** MCP 的通知系統對長時間 AI 任務特別有用，可持續向使用者報告進度。

## MCP 中的串流

好了，您已了解經典串流與 MCP 串流的比較和建議，接下來詳細說明如何在 MCP 中利用串流。

了解 MCP 框架中的串流運作方式，對於建構在長時間運作中向使用者提供即時反饋的回應型應用尤為重要。

MCP 中的串流不在於將主要回應分塊傳出，而是透過在工具處理請求時，向客戶端傳送 <strong>通知</strong>。這些通知可包含進度更新、日誌或其他事件。

### 運作方式

主要結果仍以單一回應送出。但處理期間可發送多則獨立通知訊息，即時更新客戶端。客戶端必須能處理並顯示這些通知。

## 什麼是通知？

剛提到「通知」，在 MCP 中這是什麼意思？

通知是伺服器發送給客戶端的訊息，用以告知長時間操作中進度、狀態或其他事件。通知提升透明度和使用者體驗。

例如，客戶端應在與伺服器完成初始握手後發送通知。

通知的 JSON 訊息範例如下：

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

通知屬於 MCP 中被稱為「[Logging](https://modelcontextprotocol.io/specification/draft/server/utilities/logging)」的主題。

> **棄用通知：** 2026-07-28 MCP 規格發行候選版本將 Logging 原語標示為棄用，改用 stdio 傳輸的 `stderr` 和結構化可觀測性的 OpenTelemetry。Logging 在 2025-11-25 版本及至少正式棄用後的一年內仍可正常運作。詳見 [MCP 的變更：2026-07-28 發行候選版本](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)。

若要啟用日誌功能，伺服器需將其設為功能/能力，方式如下：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 依所使用的 SDK 不同，日誌可能預設啟用，亦或您需要在伺服器配置中明確啟用。

通知類型多元：

| 等級       | 描述                         | 範例使用情境                |
|-----------|------------------------------|-----------------------------|
| debug     | 詳細除錯資訊                 | 函數入口/出口               |
| info      | 一般資訊訊息                 | 操作進度更新               |
| notice    | 正常但重要事件             | 配置變更                   |
| warning   | 警告狀況                   | 棄用功能使用               |
| error     | 錯誤狀況                   | 操作失敗                   |
| critical  | 危急狀況                   | 系統元件失效               |
| alert     | 必須立即採取行動           | 偵測到資料損毀             |
| emergency | 系統無法使用               | 完全系統故障               |

## 在 MCP 中實作通知

若要於 MCP 中實作通知，您需設置伺服器和客戶端兩端以處理即時更新，讓應用程式能在長時間操作期間即時回饋使用者。

### 伺服器端：傳送通知

從伺服器端開始。在 MCP 中，您會定義可在處理請求時傳送通知的工具。伺服器透過上下文物件（通常為 `ctx`）向客戶端發訊息。

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

前述範例中，`process_files` 工具在處理每個檔案時向客戶端傳送三則通知。`ctx.info()` 方法用於發送資訊訊息。

此外，為啟用通知，請確保伺服器使用串流傳輸（如 `streamable-http`），且客戶端實作訊息處理器來處理通知。以下示範如何設置伺服器使用 `streamable-http` 傳輸：

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

此 .NET 範例中，`ProcessFiles` 工具有 `Tool` 屬性修飾，且在處理每個檔案時向客戶端傳送三則通知。`ctx.Info()` 方法用於發送資訊訊息。

若要在您的 .NET MCP 伺服器中啟用通知，請確保使用串流傳輸：

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### 客戶端：接收通知

客戶端必須實作訊息處理器，在通知抵達時及時處理並顯示。

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

在上述程式碼中，`message_handler` 函數判斷傳入訊息是否為通知，若是則列印通知；否則當作一般伺服器訊息處理。另注意 `ClientSession` 使用此 `message_handler` 初始化以處理進入通知。

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

此 .NET 範例中，`MessageHandler` 函數判斷傳入訊息是否為通知，若是則列印通知，否則當作一般伺服器訊息處理。`ClientSession` 透過 `ClientSessionOptions` 使用該訊息處理器初始化。

若要啟用通知，請確保伺服器使用串流傳輸（如 `streamable-http`），且客戶端實作訊息處理器來處理通知。

## 進度通知及場景

本節說明 MCP 中的進度通知概念、其重要性及如何使用可串流 HTTP 實作。內含實務練習以加深理解。

進度通知是在長時間運作中由伺服器向客戶端發送的即時訊息，無需等待整個流程結束，即可持續向客戶端回報目前狀態。此作法提升透明度、使用者體驗及除錯便利性。

**示例：**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### 為什麼使用進度通知？

進度通知有多項關鍵理由：

- **改善用戶體驗：** 使用者能隨工序推進即時看到更新，而非僅在結束時。
- **即時反饋：** 客戶端可顯示進度條或日誌，讓應用更具回應感。
- **更易除錯及監控：** 開發者與使用者能了解流程卡頓或緩慢位置。

### 如何實作進度通知

以下是在 MCP 中實作進度通知的方法：

- **伺服器端：** 使用 `ctx.info()` 或 `ctx.log()` 隨每項目處理時發送通知，於主要結果準備好前向客戶端發訊。
- **客戶端：** 實作訊息處理器監聽並即時顯示通知，該處理器能區分通知與最終結果。

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

**客戶端範例：**

#### Python

```python
async def message_handler(message):
    if isinstance(message, types.ServerNotification):
        print("NOTIFICATION:", message)
    else:
        print("SERVER MESSAGE:", message)
```

## 安全性考量

在實作任何伺服器時，安全性應當是首要考量，特別是使用像 MCP 中的可串流 HTTP 這類基於 HTTP 的傳輸方式。

在使用基於 HTTP 的傳輸方式實作 MCP 伺服器時，安全性成為一個極為重要的議題，需要仔細注意多個攻擊向量及防護機制。

### 概觀

在透過 HTTP 曝露 MCP 伺服器時，安全性非常關鍵。可串流 HTTP 引入新的攻擊面，需謹慎配置。

以下是一些主要的安全性考量：

- **Origin 標頭驗證**：務必驗證 `Origin` 標頭以防止 DNS 重綁定攻擊。
- <strong>本機綁定</strong>：在本機開發時，將伺服器綁定到 `localhost`，避免公開暴露於網際網路。
- <strong>驗證機制</strong>：針對正式佈署實作身份驗證（例如 API 金鑰、OAuth）。
- **CORS**：配置跨來源資源共享（CORS）政策以限制存取。
- **HTTPS**：正式環境務必使用 HTTPS 加密流量。

### 最佳實踐

此外，實作 MCP 串流伺服器安全性時，以下是一些建議的最佳實踐：

- 永遠不要在未驗證的情況下信任來自外部的請求。
- 記錄並監控所有存取與錯誤。
- 定期更新相依套件以修補安全漏洞。

### 挑戰

在實作 MCP 串流伺服器的安全性時會遇到一些挑戰：

- 在安全性與開發便利性之間取得平衡
- 確保與各類客戶端環境相容


## 從 SSE 升級至可串流 HTTP

對於目前使用 Server-Sent Events (SSE) 的應用程式來說，遷移到可串流 HTTP 可帶來更強大的功能與更佳的長期維護性，適用於 MCP 實作。

### 為什麼要升級？

由 SSE 遷移到可串流 HTTP 有兩個主要誘因：

- 可串流 HTTP 提供比 SSE 更佳的擴展性、相容性以及更豐富的通知支持。
- 它是新 MCP 應用程式推薦使用的傳輸方式。

### 遷移步驟

以下是你在 MCP 應用程式中從 SSE 遷移到可串流 HTTP 的步驟：

- <strong>更新伺服器程式碼</strong>，在 `mcp.run()` 中使用 `transport="streamable-http"`。
- <strong>更新客戶端程式碼</strong>，改用 `streamablehttp_client` 取代 SSE 客戶端。
- <strong>實作訊息處理器</strong> ，處理客戶端的通知。
- <strong>測試相容性</strong>，確保與現有工具和工作流程相容。

### 維持相容性

建議在遷移過程中維持與現有 SSE 客戶端的相容性。以下是一些策略：

- 可同時支援 SSE 和可串流 HTTP，透過於不同端點運行兩種傳輸。
- 逐步遷移客戶端至新傳輸機制。

### 挑戰

確保在遷移過程中處理以下挑戰：

- 確保所有客戶端均已更新
- 處理通知傳送的差異

### 作業：自己動手打造串流 MCP 應用

**情境：**
建置一個 MCP 伺服器與客戶端，伺服器會處理一份項目清單（例如檔案或文件），對每個處理過的項目發送通知。客戶端應該在通知到達時即時顯示。

**步驟：**

1. 實作一個伺服器工具，處理清單並對每項目發送通知。
2. 實作一個客戶端，包含訊息處理器用以即時顯示通知。
3. 執行並測試伺服器與客戶端，觀察通知狀況。

[解答](./solution/README.md)

## 延伸閱讀與後續步驟

繼續探索 MCP 串流技術並擴展你的知識，本節提供更多資源及建議的後續建置方向，以打造更進階的應用程式。

### 延伸閱讀

- [Microsoft: HTTP 串流介紹](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft: Server-Sent Events (SSE)](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft: ASP.NET Core 中的 CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests: 串流請求](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 接下來做什麼？

- 嘗試建立更進階的 MCP 工具，使用串流實現即時分析、聊天室或協作編輯。
- 探索結合 MCP 串流與前端框架（React、Vue 等）實現即時 UI 更新。
- 下一步：[在 VSCode 使用 AI 工具包](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->