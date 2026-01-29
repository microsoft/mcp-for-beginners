# MCP Java Client - 計算機示範

此專案示範如何建立一個 Java 用戶端，連接並與 MCP（Model Context Protocol）伺服器互動。在本範例中，我們將連接到第 01 章的計算機伺服器，並執行各種數學運算。

## 先決條件

在執行此用戶端之前，您需要：

1. **啟動第 01 章的計算機伺服器**：
   - 進入計算機伺服器目錄：`03-GettingStarted/01-first-server/solution/java/`
   - 建置並執行計算機伺服器：
     ```cmd
     cd ..\01-first-server\solution\java
     .\mvnw clean install -DskipTests
     java -jar target\calculator-server-0.0.1-SNAPSHOT.jar
     ```
   - 伺服器應該在 `http://localhost:8080` 運行

2. 您的系統需安裝 **Java 21 或以上版本**
3. **Maven**（透過 Maven Wrapper 已包含）

## 什麼是 SDKClient？

`SDKClient` 是一個 Java 應用程式，示範如何：
- 使用 Server-Sent Events (SSE) 傳輸連接 MCP 伺服器
- 列出伺服器上可用的工具
- 遠端呼叫各種計算機功能
- 處理回應並顯示結果

## 運作原理

此用戶端使用 Spring AI MCP 框架來：

1. **建立連線**：建立 WebFlux SSE 用戶端傳輸，連接計算機伺服器
2. **初始化用戶端**：設定 MCP 用戶端並建立連線
3. **發現工具**：列出所有可用的計算機操作
4. **執行操作**：使用範例資料呼叫各種數學函式
5. **顯示結果**：展示每次計算的結果

## 專案結構

```
src/
└── main/
    └── java/
        └── com/
            └── microsoft/
                └── mcp/
                    └── sample/
                        └── client/
                            └── SDKClient.java    # Main client implementation
```

## 主要依賴

此專案使用以下主要依賴：

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

此依賴提供：
- `McpClient` - 主要用戶端介面
- `WebFluxSseClientTransport` - 用於網頁通訊的 SSE 傳輸
- MCP 協定的結構與請求/回應類型

## 建置專案

使用 Maven Wrapper 建置專案：

```cmd
.\mvnw clean install
```

## 執行用戶端

```cmd
java -jar .\target\calculator-client-0.0.1-SNAPSHOT.jar
```

**注意**：執行這些指令前，請確保計算機伺服器已在 `http://localhost:8080` 運行。

## 用戶端功能說明

執行用戶端時，它會：

1. **連接** 到 `http://localhost:8080` 的計算機伺服器
2. **列出工具** - 顯示所有可用的計算機操作
3. **執行計算**：
   - 加法：5 + 3 = 8
   - 減法：10 - 4 = 6
   - 乘法：6 × 7 = 42
   - 除法：20 ÷ 4 = 5
   - 次方：2^8 = 256
   - 開根號：√16 = 4
   - 絕對值：|-5.5| = 5.5
   - 幫助：顯示可用操作

## 預期輸出

```
Available Tools = ListToolsResult[tools=[Tool[name=add, description=Add two numbers together, ...], ...]]
Add Result = CallToolResult[content=[TextContent[text="5,00 + 3,00 = 8,00"]], isError=false]
Subtract Result = CallToolResult[content=[TextContent[text="10,00 - 4,00 = 6,00"]], isError=false]
Multiply Result = CallToolResult[content=[TextContent[text="6,00 * 7,00 = 42,00"]], isError=false]
Divide Result = CallToolResult[content=[TextContent[text="20,00 / 4,00 = 5,00"]], isError=false]
Power Result = CallToolResult[content=[TextContent[text="2,00 ^ 8,00 = 256,00"]], isError=false]
Square Root Result = CallToolResult[content=[TextContent[text="√16,00 = 4,00"]], isError=false]
Absolute Result = CallToolResult[content=[TextContent[text="|-5,50| = 5,50"]], isError=false]
Help = CallToolResult[content=[TextContent[text="Basic Calculator MCP Service\n\nAvailable operations:\n1. add(a, b) - Adds two numbers\n2. subtract(a, b) - Subtracts the second number from the first\n..."]], isError=false]
```

**注意**：結尾可能會看到 Maven 關於殘留執行緒的警告，這是反應式應用程式的正常現象，並不代表錯誤。

## 了解程式碼

### 1. 傳輸設定
```java
var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
```
這段程式碼建立一個 SSE（Server-Sent Events）傳輸，連接到計算機伺服器。

### 2. 用戶端建立
```java
var client = McpClient.sync(this.transport).build();
client.initialize();
```
建立同步 MCP 用戶端並初始化連線。

### 3. 呼叫工具
```java
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
```
呼叫 "add" 工具，參數為 a=5.0 和 b=3.0。

## 疑難排解

### 伺服器未啟動
若出現連線錯誤，請確認第 01 章的計算機伺服器已啟動：
```
Error: Connection refused
```
**解決方案**：先啟動計算機伺服器。

### 埠號已被佔用
若 8080 埠號被佔用：
```
Error: Address already in use
```
**解決方案**：停止其他使用 8080 埠號的應用程式，或修改伺服器使用其他埠號。

### 建置錯誤
若遇到建置錯誤：
```cmd
.\mvnw clean install -DskipTests
```

## 進一步學習

- [Spring AI MCP 文件](https://docs.spring.io/spring-ai/reference/api/mcp/)
- [Model Context Protocol 規範](https://modelcontextprotocol.io/)
- [Spring WebFlux 文件](https://docs.spring.io/spring-framework/docs/current/reference/html/web-reactive.html)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。