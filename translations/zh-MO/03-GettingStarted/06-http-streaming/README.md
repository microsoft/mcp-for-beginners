# 使用模型上下文協議 (MCP) 的 HTTPS 串流

本章提供使用 HTTPS 實作安全、可擴展且即時串流的全面指南，採用模型上下文協議 (MCP)。內容涵蓋串流的動機、可用的傳輸機制、如何在 MCP 中實現可串流的 HTTP、安全最佳實踐、從 SSE 的遷移，以及建立您自己的串流 MCP 應用程式的實用指引。

> **展望未來：** 本課程說明在 **MCP 規範 2025-11-25** 中的可串流 HTTP，其中會在 `initialize` 過程中建立一個會話，並附帶 `Mcp-Session-Id` 標頭。`2026-07-28` 發行候選版本則完全移除握手和會話 ID，使每個請求都是自包含且可路由到任何伺服器實例，無需黏性會話。詳情請參閱 [MCP 的變更：2026-07-28 發行候選版本](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)。

## MCP 中的傳輸機制與串流

本節探討 MCP 中可用的不同傳輸機制，以及它們在實現客戶端與伺服器之間即時通訊串流功能中的角色。

### 什麼是傳輸機制？

傳輸機制定義客戶端與伺服器之間交換資料的方式。MCP 支援多種傳輸類型，以滿足不同環境和需求：

- **stdio**：標準輸入/輸出，適用於本地和命令列介面工具。簡單但不適合網頁或雲端。
- **SSE (伺服器推送事件)**：允許伺服器經由 HTTP 向客戶端推送即時更新。適合網頁用戶介面，但可擴展性和彈性有限。根據 MCP 規範 2025-06-18，獨立的 SSE 傳輸已被棄用，改以「可串流 HTTP」傳輸取代。
- **可串流 HTTP**：現代基於 HTTP 的串流傳輸，支援通知與更佳的可擴展性。建議用於大多數生產和雲端場景。

### 比較表

請參閱下方比較表，了解這些傳輸機制的差異：

| 傳輸機制           | 即時更新           | 串流            | 可擴展性       | 適用場景                |
|-------------------|------------------|-----------|-------------|-------------------------|
| stdio             | 否               | 否        | 低          | 本地 CLI 工具            |
| SSE               | 是               | 是        | 中          | 網頁，即時更新           |
| 可串流 HTTP       | 是               | 是        | 高          | 雲端，多客戶端           |

> **提示：** 選擇合適的傳輸機制會影響效能、可擴展性及用戶體驗。**可串流 HTTP** 是現代、可擴展且適合雲端應用的推薦選擇。

請注意前幾章所介紹的 stdio 和 SSE 傳輸，以及本章介紹的可串流 HTTP 傳輸。

## 串流：概念與動機

理解串流背後的基本概念與動機，對於實作高效的即時通訊系統至關重要。

<strong>串流</strong> 是網路程式設計中的一種技術，允許資料以小批次或事件序列的方式傳送與接收，而非等待完整回應準備好。這在以下場合特別有用：

- 大型檔案或資料集。
- 即時更新（例如聊天、進度條）。
- 長時間運算中持續告知使用者狀態。

以下是對串流的高層次認識：

- 資料逐步傳送，而非一次推出。
- 客戶端可隨到即處理資料。
- 降低感知延遲，提升用戶體驗。

### 為什麼使用串流？

使用串流的原因如下：

- 使用者可立即得到回饋，而非僅在結束時。
- 促成即時應用與反應迅速的界面。
- 更有效率地使用網路與計算資源。

### 簡單範例：HTTP 串流伺服器與客戶端

以下是一個簡單示範如何實作串流：

#### Python

**伺服器 (Python, 使用 FastAPI 與 StreamingResponse)：**

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

**客戶端 (Python, 使用 requests)：**

```python
import requests

with requests.get("http://localhost:8000/stream", stream=True) as r:
    for line in r.iter_lines():
        if line:
            print(line.decode())
```

此範例演示伺服器如何在訊息可用時即時送出一系列訊息給客戶端，而非等全部準備完成後才送出。

**工作原理：**

- 伺服器逐一產生每一條可用訊息。
- 客戶端接收並立即列印每個區塊。

**需求：**

- 伺服器必須使用串流回應（例如 FastAPI 的 `StreamingResponse`）。
- 客戶端必須能以串流方式處理回應（requests 中設定為 `stream=True`）。
- Content-Type 通常為 `text/event-stream` 或 `application/octet-stream`。

#### Java

**伺服器 (Java, 使用 Spring Boot 與伺服器推送事件)：**

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

**客戶端 (Java, 使用 Spring WebFlux 的 WebClient)：**

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

- 使用 Spring Boot 的反應式堆疊，搭配 `Flux` 進行串流
- `ServerSentEvent` 提供結構化事件串流及事件類型
- `WebClient` 搭配 `bodyToFlux()` 支援反應式串流消費
- `delayElements()` 用於模擬事件間的處理時間
- 事件可標示類型（如 `info`, `result`）以便客戶端更好處理

### 比較：經典串流 vs MCP 串流

對比「經典」串流與 MCP 中串流的運作方式，如下表所示：

| 功能                   | 經典 HTTP 串流                 | MCP 串流（通知）                 |
|------------------------|-------------------------------|---------------------------------|
| 主要回應               | 分塊傳輸                      | 單一，最後傳送                   |
| 進度更新               | 作為資料塊傳送                | 以通知訊息送出                   |
| 客戶端需求             | 必須處理串流                  | 必須實作訊息處理器               |
| 使用場景               | 大檔案、AI 代幣串流           | 進度、日誌、即時回饋             |

### 觀察到的主要差異

此外，還有幾個關鍵差異：

- **通訊模式：**
  - 經典 HTTP 串流：採用簡單的分塊傳輸編碼逐塊送資料
  - MCP 串流：使用結構化的通知系統，搭配 JSON-RPC 協議

- **訊息格式：**
  - 經典 HTTP：純文字分塊，以換行分隔
  - MCP：結構化 LoggingMessageNotification 物件，帶有元資料

- **客戶端實作：**
  - 經典 HTTP：簡單客戶端處理串流回應
  - MCP：較複雜的客戶端，具備訊息處理器以處理不同類型訊息

- **進度更新：**
  - 經典 HTTP：進度包含於主回應串流中
  - MCP：進度透過獨立通知訊息發送，主回應於最後送出

### 推薦事項

在選擇實現經典串流（如上例使用的 `/stream` 端點）或 MCP 串流時，有以下建議：

- **針對簡單串流需求：** 經典 HTTP 串流實作較簡單，適合基本串流需求。

- **針對複雜、互動式應用：** MCP 串流提供更結構化方法，包含豐富元資料及通知與最終結果的分離。

- **針對 AI 應用：** MCP 的通知系統對於長時間運算的 AI 任務非常有用，能持續告知使用者進度。

## MCP 中的串流

好的，到目前為止您已看到經典串流與 MCP 串流的比較與建議。下面深入說明如何在 MCP 中利用串流。

理解 MCP 框架內串流的運作，對構建具有即時反饋能力的應用程式非常重要，尤其是在長時間執行的操作中。

在 MCP 中，串流不是指將主回應拆塊送出，而是針對工具處理請求時向客戶端發送<strong>通知</strong>。這些通知可包含進度更新、日誌或其他事件。

### 運作方式

主結果仍然以單一回應送出，但處理過程可傳送獨立通知訊息，令客戶端能實時更新。客戶端必須能夠處理並顯示這些通知訊息。

## 什麼是通知？

我們提到「通知」，在 MCP 中這是什麼意思？

通知是由伺服器發送給客戶端的訊息，用於告知執行長時間操作的進度、狀態或其他事件。通知提升透明度與使用者體驗。

例如，客戶端應在與伺服器完成初始握手後發送通知。

通知以 JSON 訊息之形式如下：

```json
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

通知屬於 MCP 中的主題之一，稱為 ["Logging"](https://modelcontextprotocol.io/specification/draft/server/utilities/logging)。

> **廢止通知：** `2026-07-28` MCP 規範發行候選版本將 Logging 基元標記為棄用，改用 stdio 傳輸的 `stderr` 以及結構化觀測的 OpenTelemetry。Logging 在 `2025-11-25` 版本及官方廢止後至少一年仍然有效。詳見 [MCP 的變更：2026-07-28 發行候選版本](../../01-CoreConcepts/mcp-2026-07-28-release-candidate.md)。

為讓日誌功能運作，伺服器需啟用此功能/能力，如下示範：

```json
{
  "capabilities": {
    "logging": {}
  }
}
```

> [!NOTE]
> 依不同 SDK，日誌功能可能預設啟用，或需您明確在伺服器配置中開啟。

通知類型如下：

| 等級      | 說明                         | 範例使用情境                 |
|-----------|------------------------------|------------------------------|
| debug     | 詳細除錯資訊                 | 函式進入/離開點             |
| info      | 一般訊息                    | 操作進度更新                 |
| notice    | 正常但重要事件              | 配置變更                    |
| warning   | 警告狀況                    | 已廢止功能使用             |
| error     | 錯誤狀況                    | 操作失敗                    |
| critical  | 臨界狀況                    | 系統元件失效               |
| alert     | 必須立即採取行動             | 偵測到資料損壞             |
| emergency | 系統不可用                   | 完整系統故障               |

## 在 MCP 中實作通知

要在 MCP 實作通知，需安排伺服器與客戶端雙方處理即時更新。這讓應用能在長時間運算過程中即時回饋給使用者。

### 伺服器端：發送通知

先從伺服器端說起。MCP 裡您定義的工具能在處理請求時發送通知。伺服器透過上下文物件（通常為 `ctx`）將訊息送給客戶端。

#### Python

```python
@mcp.tool(description="A tool that sends progress notifications")
async def process_files(message: str, ctx: Context) -> TextContent:
    await ctx.info("Processing file 1/3...")
    await ctx.info("Processing file 2/3...")
    await ctx.info("Processing file 3/3...")
    return TextContent(type="text", text=f"Done: {message}")
```

剛才範例中 `process_files` 工具在處理每個檔案時發送三則通知。`ctx.info()` 方法用於發送資訊訊息。

同時，為啟用通知，請確保您的伺服器使用串流傳輸 (如 `streamable-http`)，且客戶端實作訊息處理器以處理通知。下面示範如何設定伺服器使用 `streamable-http` 傳輸：

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

在此 .NET 範例中，`ProcessFiles` 工具標註 `Tool` 屬性，在處理每個檔案時發送三則通知。`ctx.Info()` 方法用於發送資訊訊息。

要啟用 .NET MCP 伺服器的通知，請確保您使用串流傳輸：

```csharp
var builder = McpBuilder.Create();
await builder
    .UseStreamableHttp() // Enable streamable HTTP transport
    .Build()
    .RunAsync();
```

### 客戶端：接收通知

客戶端必須實作訊息處理器，在通知抵達時即時處理並顯示。

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

以上程式碼中，`message_handler` 函式會檢查接收到的訊息是否為通知。若是，則印出通知，否則當作一般伺服器訊息處理。另注意 `ClientSession` 初始化時傳入了 `message_handler` 用來處理收到的通知。

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

在此 .NET 範例中，`MessageHandler` 函式檢查接收到的訊息是否為通知。若是，即時列印通知，否則當作普通伺服器訊息處理。`ClientSession` 建構時透過 `ClientSessionOptions` 指定訊息處理器。

要啟用通知，請確保伺服器使用串流傳輸 (如 `streamable-http`)，且客戶端實作訊息處理器以處理通知。

## 進度通知與應用場景

本節說明 MCP 中的進度通知概念、其重要性以及如何使用可串流 HTTP 實作。同時提供實際作業以強化理解。

進度通知是在長時間運算過程中，伺服器即時傳送給客戶端的即時訊息。伺服器不需等待整個流程結束，即可持續更新客戶端當前狀態。此舉提升透明度、使用者體驗，且更易於除錯。

**範例：**

```text

"Processing document 1/10"
"Processing document 2/10"
...
"Processing complete!"

```

### 為何使用進度通知？

使用進度通知有多項原因：

- **提升使用者體驗：** 使用者可隨著工作進度看到更新，而非僅在結束時才知道結果。
- **即時回饋：** 客戶端能顯示進度條或日誌，讓應用感覺更加反應迅速。
- **方便除錯與監控：** 開發者與使用者能清楚了解流程中可能緩慢或卡住的環節。

### 如何實作進度通知

以下說明在 MCP 中如何實作進度通知：

- **在伺服器端：** 利用 `ctx.info()` 或 `ctx.log()` 發送通知，在處理每個項目時即時通知客戶端。這會在主結果準備好前先發送訊息。
- **在客戶端：** 實作訊息處理器，監聽並顯示抵達的通知。此處理器能分辨通知與最終結果。

**伺服器範例：**


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

## 安全考量

實作任何伺服器時，安全性都應該是首要任務，尤其是在使用基於 HTTP 的傳輸方式，如 MCP 中的 Streamable HTTP 時。

在使用基於 HTTP 的傳輸方式實作 MCP 伺服器時，安全性成為極其重要的議題，需要細心考量多種攻擊向量與防護機制。

### 概覽

當 MCP 伺服器透過 HTTP 公開時，安全性非常關鍵。Streamable HTTP 引入新的攻擊面，需謹慎配置。

以下是一些主要的安全考量：

- **Origin 標頭驗證**：務必驗證 `Origin` 標頭以防止 DNS 重綁定攻擊。
- <strong>本地主機綁定</strong>：開發階段應將伺服器綁定到 `localhost`，避免暴露於公共網際網路。
- <strong>驗證機制</strong>：生產環境應實作驗證（如 API 金鑰、OAuth）。
- **CORS**：設定跨來源資源共享（CORS）政策以限制存取。
- **HTTPS**：生產環境使用 HTTPS 加密流量。

### 最佳實踐

此外，在實作 MCP 串流伺服器時，以下是一些推薦遵循的最佳實踐：

- 進來請求絕不盲信，必須進行驗證。
- 紀錄及監控所有存取與錯誤。
- 定期更新相依套件以修補安全漏洞。

### 挑戰

在實作 MCP 串流伺服器安全性時，會面臨一些挑戰：

- 在安全性與開發便利性間取得平衡
- 確保與多種客戶端環境相容


## 從 SSE 升級到 Streamable HTTP

對於目前使用伺服器傳送事件（SSE）的應用程式，遷移到 Streamable HTTP 可提供增強功能與 MCP 實作的長期可持續性。

### 為什麼要升級？

有兩個令人信服的理由讓你從 SSE 升級到 Streamable HTTP：

- Streamable HTTP 比 SSE 有更佳的擴充性、相容性和豐富的通知支援。
- 它是新 MCP 應用的推薦傳輸方式。

### 遷移步驟

以下是如何在 MCP 應用中從 SSE 遷移到 Streamable HTTP：

- <strong>更新伺服器程式碼</strong>，於 `mcp.run()` 使用 `transport="streamable-http"`。
- <strong>更新客戶端程式碼</strong>，使用 `streamablehttp_client` 取代 SSE 客戶端。
- <strong>實作訊息處理器</strong>於客戶端，用以處理通知。
- <strong>測試相容性</strong>確保支援現有工具與工作流程。

### 維持相容性

遷移過程中，建議維持與現有 SSE 客戶端的相容性。以下是一些策略：

- 可在不同端點同時執行 SSE 與 Streamable HTTP 兩種傳輸。
- 逐步將客戶端遷移至新傳輸。

### 挑戰

確保遷移期間解決以下挑戰：

- 確保所有客戶端皆已更新
- 處理通知傳遞上的差異

### 作業：建立你自己的串流 MCP 應用程式

**情境：**
建立一個 MCP 伺服器與客戶端，伺服器處理一份項目清單（如檔案或文件），並為每個已處理的項目發送通知。客戶端應即時顯示每則通知。

**步驟：**

1. 實作伺服器工具處理清單並發送通知。
2. 實作帶有訊息處理器的客戶端以即時顯示通知。
3. 執行伺服器與客戶端，測試並觀察通知狀況。

[解答](./solution/README.md)

## 進一步閱讀與後續建議？

若要繼續 MCP 串流的旅程並擴展知識，本節提供額外資源及建議下一步以建構更進階的應用程式。

### 進一步閱讀

- [Microsoft：HTTP 串流入門](https://learn.microsoft.com/aspnet/core/fundamentals/http-requests?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430#streaming)
- [Microsoft：伺服器傳送事件（SSE）](https://learn.microsoft.com/azure/application-gateway/for-containers/server-sent-events?tabs=server-sent-events-gateway-api&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Microsoft：ASP.NET Core 的 CORS](https://learn.microsoft.com/aspnet/core/security/cors?view=aspnetcore-8.0&WT.mc_id=%3Fwt.mc_id%3DMVP_452430)
- [Python requests：串流請求](https://requests.readthedocs.io/en/latest/user/advanced/#streaming-requests)

### 後續建議

- 嘗試建立使用串流的更進階 MCP 工具，如即時分析、聊天或協同編輯。
- 探索將 MCP 串流整合至前端框架（React、Vue 等）以進行即時 UI 更新。
- 下一步：[VSCode 的 AI 工具包應用](../07-aitk/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->