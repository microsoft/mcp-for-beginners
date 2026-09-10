# 計算器 LLM 客戶端

一個示範如何使用 LangChain4j 通過 MiniMax 兼容 OpenAI API 連接至 MCP（模型上下文協議）計算器服務的 Java 應用程式。

## 先決條件

- Java 21 或更高版本
- Maven 3.6+（或使用隨附的 Maven 包裝器）
- MiniMax API 金鑰
- 運行在 `http://localhost:8080` 的 MCP 計算器服務

## 取得 API 金鑰

本應用使用 MiniMax 兼容 OpenAI 的 API。請按照以下步驟取得您的金鑰和端點：

### 1. 選擇端點
1. 全球端點使用 `https://api.minimax.io/v1`
2. 中國端點使用 `https://api.minimaxi.com/v1`

### 2. 建立 API 金鑰
1. 從您的 MiniMax 帳戶創建 MiniMax API 金鑰
2. 將金鑰妥善保存

### 3. 設置環境變數

#### 在 Windows（命令提示字元）：
```cmd
set OPENAI_API_KEY=your_minimax_api_key_here
set OPENAI_BASE_URL=https://api.minimax.io/v1
set MINIMAX_MODEL_ID=MiniMax-M3
```

#### 在 Windows（PowerShell）：
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

## 安裝與設定

1. <strong>克隆或切換至專案目錄</strong>

2. <strong>安裝依賴</strong>：
   ```cmd
   mvnw clean install
   ```
   或者如果您有全域安裝 Maven：
   ```cmd
   mvn clean install
   ```

3. <strong>設定環境變數</strong>（請參考上方「取得 API 金鑰」部分）

4. **啟動 MCP 計算器服務**：
   請確保第 1 章的 MCP 計算器服務在 `http://localhost:8080/sse` 運行。啟動客戶端前需先啟動此服務。

## 執行應用程式

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 應用程式功能說明

本應用展示與計算器服務三種主要互動：

1. <strong>加法</strong>：計算 24.5 與 17.3 的和
2. <strong>平方根</strong>：計算 144 的平方根
3. <strong>說明</strong>：顯示可用的計算器函式

## 預期輸出

成功執行時，您應會看到類似以下輸出：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 疑難排解

### 常見問題

1. **「未設定 OPENAI_API_KEY 環境變數」**
   - 請確定已設定 `OPENAI_API_KEY` 環境變數
   - 設定後請重新啟動終端機或命令提示字元

2. **「連線被拒絕，無法連接 localhost:8080」**
   - 確認 MCP 計算器服務是否在 8080 埠運行
   - 檢查是否有其他服務佔用 8080 埠

3. **「認證失敗」**
   - 驗證您的 API 金鑰是否有效
   - 確認 `OPENAI_BASE_URL` 是否對應您想使用的端點

4. **Maven 建置錯誤**
   - 確認使用 Java 21 或更高版本：`java -version`
   - 試著清除建置：`mvnw clean`

### 除錯

若要啟用除錯日誌，執行時加入以下 JVM 參數：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 配置

本應用程式配置為：
- 預設使用 MiniMax-M3；透過設定 `MINIMAX_MODEL_ID` 選擇 `MiniMax-M3` 或 `MiniMax-M2.7`
- 當設定了 `OPENAI_BASE_URL` 時連接該端點；否則當 `MINIMAX_REGION=cn_zh` 時使用 `https://api.minimaxi.com/v1`，預設則使用 `https://api.minimax.io/v1`
- 連接 MCP 服務位於 `http://localhost:8080/sse`
- 請求使用 60 秒超時

## 依賴套件

專案中使用的主要依賴：
- **LangChain4j**：用於 AI 整合與工具管理
- **LangChain4j MCP**：用於模型上下文協議支援
- **LangChain4j OpenAI official**：用於 MiniMax 兼容 OpenAI API 整合
- **Spring Boot**：應用框架與依賴注入

## 授權條款

本專案採 Apache 許可證 2.0 授權 - 詳情請見 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 文件。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->