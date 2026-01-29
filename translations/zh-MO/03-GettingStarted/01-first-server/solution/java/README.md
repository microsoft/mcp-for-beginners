# 基本計算器 MCP 服務

此服務透過 Model Context Protocol (MCP) 並使用 Spring Boot 搭配 WebFlux 傳輸，提供基本的計算器運算功能。它是為初學者學習 MCP 實作而設計的簡單範例。

欲了解更多資訊，請參閱 [MCP Server Boot Starter](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-server-boot-starter-docs.html) 參考文件。

## 使用服務

此服務透過 MCP 協議公開以下 API 端點：

- `add(a, b)`：將兩個數字相加
- `subtract(a, b)`：從第一個數字中減去第二個數字
- `multiply(a, b)`：將兩個數字相乘
- `divide(a, b)`：將第一個數字除以第二個數字（含零值檢查）
- `power(base, exponent)`：計算數字的冪次方
- `squareRoot(number)`：計算平方根（含負數檢查）
- `modulus(a, b)`：計算除法的餘數
- `absolute(number)`：計算絕對值

## 依賴項目

此專案需要以下主要依賴：

```xml
<dependency>
    <groupId>org.springframework.ai</groupId>
    <artifactId>spring-ai-starter-mcp-server-webflux</artifactId>
</dependency>
```

## 建置專案

使用 Maven 建置專案：
```bash
./mvnw clean install -DskipTests
```

## 啟動伺服器

### 使用 Java

```bash
java -jar target/calculator-server-0.0.1-SNAPSHOT.jar
```

### 使用 MCP Inspector

MCP Inspector 是一個方便與 MCP 服務互動的工具。使用此計算器服務時，請依照以下步驟：

1. **安裝並啟動 MCP Inspector**，在新的終端機視窗中執行：
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **透過應用程式顯示的網址（通常是 http://localhost:6274）存取網頁介面**

3. **設定連線**：
   - 將傳輸類型設為「SSE」
   - 將網址設定為您正在執行的伺服器 SSE 端點：`http://localhost:8080/sse`
   - 點擊「Connect」

4. **使用工具**：
   - 點擊「List Tools」查看可用的計算器操作
   - 選擇工具後點擊「Run Tool」執行操作

![MCP Inspector Screenshot](../../../../../../translated_images/zh-MO/tool.40e180a7b0d0fe2067cf96435532b01f63f7f8619d6b0132355a04b426b669ac.png)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。