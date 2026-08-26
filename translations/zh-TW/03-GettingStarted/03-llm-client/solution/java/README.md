# 計算器 LLM 客戶端

一個 Java 應用程式，演示如何使用 LangChain4j 通過 MiniMax 相容 OpenAI API 連接至 MCP（模型上下文協議）計算器服務。

## 預備條件

- Java 21 或以上版本
- Maven 3.6+（或使用包含的 Maven 包裝器）
- MiniMax API 金鑰
- 在 `http://localhost:8080` 運行的 MCP 計算器服務

## 取得 API 金鑰

本應用使用 MiniMax 相容 OpenAI API。請按照以下步驟取得您的金鑰和端點：

### 1. 選擇端點
1. 使用 `https://api.minimax.io/v1` 作為全球端點
2. 使用 `https://api.minimaxi.com/v1` 作為中國端點

### 2. 建立 API 金鑰
1. 從您的 MiniMax 帳號建立 MiniMax API 金鑰
2. 將金鑰妥善保管

### 3. 設定環境變數

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

1. <strong>克隆或進入專案目錄</strong>

2. <strong>安裝依賴</strong>：
   ```cmd
   mvnw clean install
   ```
   或者您已全域安裝 Maven：
   ```cmd
   mvn clean install
   ```

3. <strong>設定環境變數</strong>（請參閱上述「取得 API 金鑰」章節）

4. **啟動 MCP 計算器服務**：
   確保您已經在 `http://localhost:8080/sse` 運行第一章的 MCP 計算器服務。在啟動客戶端前需先啟動此服務。

## 執行應用

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 應用功能介紹

本應用展示了與計算器服務的三種主要互動：

1. <strong>加法</strong>：計算 24.5 與 17.3 的和
2. <strong>平方根</strong>：計算 144 的平方根
3. <strong>幫助</strong>：顯示可用的計算器函數

## 預期輸出

執行成功時，您應該會看到類似以下的輸出：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 疑難排解

### 常見問題

1. **「OPENAI_API_KEY 環境變數未設定」**
   - 確認您已設定 `OPENAI_API_KEY` 環境變數
   - 設定環境變數後重新啟動終端機/命令提示字元

2. **「連線被拒絕 localhost:8080」**
   - 確認 MCP 計算器服務是否正在 8080 埠上執行
   - 檢查是否有其他服務佔用 8080 埠

3. **「認證失敗」**
   - 驗證您的 API 金鑰是否有效
   - 檢查 `OPENAI_BASE_URL` 是否與您預期端點相符

4. **Maven 編譯錯誤**
   - 確認您使用的是 Java 21 或更高版本：`java -version`
   - 試著清理編譯：`mvnw clean`

### 除錯

若要啟用除錯日誌，執行時加入以下 JVM 參數：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 配置

本應用設定為：
- 預設使用 MiniMax-M3，當設定 `MINIMAX_MODEL_ID` 時使用 MiniMax-M2.7
- 連接至設定的 `OPENAI_BASE_URL`；若未設定，則根據 `MINIMAX_REGION=cn_zh` 使用 `https://api.minimaxi.com/v1`，預設使用 `https://api.minimax.io/v1`
- 連接至 MCP 服務位址 `http://localhost:8080/sse`
- 請求使用 60 秒逾時

## 依賴項

本專案使用的主要依賴：
- **LangChain4j**：用於 AI 整合與工具管理
- **LangChain4j MCP**：用於模型上下文協議支援
- **LangChain4j OpenAI official**：用於 MiniMax 相容 OpenAI API 整合
- **Spring Boot**：用於應用框架和依賴注入

## 授權條款

本專案採用 Apache License 2.0 授權 - 詳情請參閱 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 文件。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->