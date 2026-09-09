# 計算機 LLM 用戶端

一個示範如何使用 LangChain4j 透過 MiniMax OpenAI 相容 API 連接到 MCP（模型上下文協議）計算機服務的 Java 應用程式。

## 先決條件

- Java 21 或以上版本
- Maven 3.6+（或使用內建的 Maven 包裝器）
- 一個 MiniMax API 金鑰
- 一個在 `http://localhost:8080` 運行中的 MCP 計算機服務

## 取得 API 金鑰

本應用程式使用 MiniMax OpenAI 相容 API。請按照以下步驟取得您的金鑰和端點：

### 1. 選擇端點
1. 使用 `https://api.minimax.io/v1` 作為全球端點
2. 使用 `https://api.minimaxi.com/v1` 作為中國端點

### 2. 創建 API 金鑰
1. 從您的 MiniMax 帳戶創建一組 MiniMax API 金鑰
2. 將金鑰妥善保存於安全處

### 3. 設定環境變數

#### 在 Windows（命令提示字元）中：
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### 在 Windows（PowerShell）中：
```powershell
$env:OPENAI_API_KEY="your_minimax_api_key_here"
$env:OPENAI_BASE_URL="https://api.minimax.io/v1"
$env:MINIMAX_MODEL_ID="MiniMax-M3"
```

#### 在 macOS/Linux 中：
```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

## 安裝與設定

1. <strong>克隆或導航至專案目錄</strong>

2. <strong>安裝依賴套件</strong>：
   ```cmd
   mvnw clean install
   ```
   或者如果您已全局安裝 Maven：
   ```cmd
   mvn clean install
   ```

3. <strong>設定環境變數</strong>（參見上方「取得 API 金鑰」章節）

4. **啟動 MCP 計算機服務**：
   請確保您已啟動第 1 章中的 MCP 計算機服務，並在 `http://localhost:8080/sse` 運行。這需在啟動用戶端之前完成。

## 執行應用程式

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 應用程式功能說明

本應用示範與計算機服務的三種主要互動：

1. <strong>加法</strong>：計算 24.5 與 17.3 的和
2. <strong>平方根</strong>：計算 144 的平方根
3. <strong>幫助</strong>：顯示可用的計算機功能

## 預期輸出

成功執行時，您應該會看到類似的輸出：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 疑難排解

### 常見問題

1. **「OPENAI_API_KEY 環境變數未設定」**
   - 請確認您已設定 `OPENAI_API_KEY` 環境變數
   - 設定後請重新啟動終端機／命令提示字元

2. **「連線被拒絕 localhost:8080」**
   - 確認 MCP 計算機服務有在 8080 埠口運行
   - 檢查是否有其他服務佔用 8080 埠口

3. **「驗證失敗」**
   - 驗證您的 API 金鑰是否有效
   - 檢查 `OPENAI_BASE_URL` 是否與您想用的端點匹配

4. **Maven 建置錯誤**
   - 確認您使用的 Java 版本為 21 或以上：`java -version`
   - 試試清理建置：`mvnw clean`

### 除錯

若要啟用除錯日誌，執行時加入以下 JVM 參數：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 設定

本應用配置如下：
- 預設使用 MiniMax-M3，當設定 `MINIMAX_MODEL_ID` 使用 MiniMax-M2.7
- 連線到 `OPENAI_BASE_URL`（若有設定）；未設定時，當 `MINIMAX_REGION=cn_zh` 則用 `https://api.minimaxi.com/v1`，否則預設用 `https://api.minimax.io/v1`
- 連線 MCP 服務於 `http://localhost:8080/sse`
- 請求逾時時間設定為 60 秒

## 依賴套件

專案中主要用到的依賴：
- **LangChain4j**：用於 AI 整合與工具管理
- **LangChain4j MCP**：支援模型上下文協議
- **LangChain4j OpenAI 官方套件**：整合 MiniMax OpenAI 相容 API
- **Spring Boot**：應用程式框架與依賴注入

## 授權

本專案採用 Apache License 2.0 授權 - 詳見 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 檔案說明。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->