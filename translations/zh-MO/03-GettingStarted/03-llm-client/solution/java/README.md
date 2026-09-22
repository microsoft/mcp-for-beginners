# 計算機 LLM 用戶端

> [!NOTE]
> 此解決方案連接到課程的傳統 HTTP+SSE 計算機服務，
> 並針對 MCP `2025-11-25` SDK API。它不是 `2026-07-28` Streamable HTTP
> 範例。

一個 Java 應用程式，演示如何使用 LangChain4j 通過 MiniMax 相容 OpenAI 的 API 連接到 MCP（模型上下文協議）計算機服務。

## 前置需求

- Java 21 或更高版本
- Maven 3.6+（或使用附帶的 Maven 包裝器）
- MiniMax API 金鑰
- MCP 計算機服務在 `http://localhost:8080` 運行中

## 取得 API 金鑰

此應用程式使用 MiniMax 相容 OpenAI 的 API。請遵照以下步驟取得你的金鑰與端點：

### 1. 選擇端點
1. 使用 `https://api.minimax.io/v1` 作為全球端點
2. 使用 `https://api.minimaxi.com/v1` 作為中國端點

### 2. 建立 API 金鑰
1. 從你的 MiniMax 帳戶建立 MiniMax API 金鑰
2. 將金鑰妥善保管

### 3. 設定環境變數

#### 在 Windows (命令提示字元)：
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### 在 Windows (PowerShell)：
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### 在 macOS/Linux：
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## 設定與安裝

1. <strong>複製或切換到專案目錄</strong>

2. <strong>安裝依賴</strong>：
   ```cmd
   mvnw clean install
   ```
   或者如果你已安裝全局 Maven：
   ```cmd
   mvn clean install
   ```

3. <strong>設定環境變數</strong>（參見上述「取得 API 金鑰」章節）

4. **啟動 MCP 計算機服務**：
   確保你已啟動第一章的 MCP 計算機服務且正在 `http://localhost:8080/sse` 運行。啟動用戶端前須先啟動服務。

## 執行應用程式

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 應用程式功能

此應用程式示範與計算機服務的三種主要互動：

1. <strong>加法</strong>：計算 24.5 與 17.3 的總和
2. <strong>平方根</strong>：計算 144 的平方根
3. <strong>幫助</strong>：顯示可用的計算機功能

## 預期輸出

成功執行時，你應該會看到類似以下的輸出：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 疑難排解

### 常見問題

1. **"OPENAI_API_KEY 環境變數未設定"**
   - 請確認你已設定 `OPENAI_API_KEY` 環境變數
   - 設定完畢後重新啟動你的終端機/命令提示字元

2. **"連線被拒絕到 localhost:8080"**
   - 確認 MCP 計算機服務已在 8080 埠口運行
   - 檢查是否有其他服務佔用 8080 埠口

3. **"驗證失敗"**
   - 驗證你的 API 金鑰是否有效
   - 確認 `OPENAI_BASE_URL` 是否與你意圖使用的端點相符

4. **Maven 建置錯誤**
   - 確認你使用的 Java 版本為 21 或更高版本：`java -version`
   - 嘗試清理建置：`mvnw clean`

### 除錯

若要啟用除錯日誌，執行時加入以下 JVM 參數：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 設定

此應用程式設定為：
- 預設使用 MiniMax-M3；透過設定 `MINIMAX_MODEL_ID` 來選擇 `MiniMax-M3` 或 `MiniMax-M2.7`
- 當設定了 `OPENAI_BASE_URL` 則連接該網址；否則，當 `MINIMAX_REGION=cn_zh` 使用 `https://api.minimaxi.com/v1`，預設使用 `https://api.minimax.io/v1`
- 連接 MCP 服務於 `http://localhost:8080/sse`
- 請求使用 60 秒超時

## 依賴

專案中主要使用的依賴：
- **LangChain4j**：用於 AI 集成與工具管理
- **LangChain4j MCP**：用於模型上下文協議支援
- **LangChain4j OpenAI official**：用於 MiniMax 相容 OpenAI API 集成
- **Spring Boot**：應用框架與依賴注入

## 授權

本專案以 Apache 授權條款 2.0 為授權方式 - 詳細內容請參見 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 文件。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->