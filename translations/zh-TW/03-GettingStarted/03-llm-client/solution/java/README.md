# 計算器 LLM 用戶端

一個展示如何使用 LangChain4j 通過 MiniMax OpenAI 相容 API 連接 MCP（模型上下文協議）計算器服務的 Java 應用程式。

## 前置條件

- Java 21 或以上版本
- Maven 3.6+（或使用附帶的 Maven 包裝器）
- 一個 MiniMax API 金鑰
- 一個在 `http://localhost:8080` 運行的 MCP 計算器服務

## 取得 API 金鑰

此應用程式使用 MiniMax OpenAI 相容 API。請依照以下步驟取得您的金鑰和端點：

### 1. 選擇端點
1. 全球端點使用 `https://api.minimax.io/v1`
2. 中國端點使用 `https://api.minimaxi.com/v1`

### 2. 創建 API 金鑰
1. 從您的 MiniMax 帳號創建一個 MiniMax API 金鑰
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

## 設定與安裝

1. <strong>複製或進入專案目錄</strong>

2. <strong>安裝相依套件</strong>：
   ```cmd
   mvnw clean install
   ```
   或者如果您已全域安裝 Maven：
   ```cmd
   mvn clean install
   ```

3. <strong>設定環境變數</strong>（參見上方「取得 API 金鑰」章節）

4. **啟動 MCP 計算器服務**：
   確保您已啟動第一章的 MCP 計算器服務，並運行在 `http://localhost:8080/sse`。必須先啟動該服務，然後再啟動用戶端。

## 執行應用程式

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 應用程式功能說明

該應用程式示範了與計算器服務的三種主要互動：

1. <strong>加法</strong>：計算 24.5 與 17.3 的和
2. <strong>平方根</strong>：計算 144 的平方根
3. <strong>說明</strong>：顯示可用的計算器功能

## 預期輸出

成功執行時，您應該會看到類似如下的輸出：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 問題排解

### 常見問題

1. **「OPENAI_API_KEY 環境變數尚未設定」**
   - 確認您已設定 `OPENAI_API_KEY` 環境變數
   - 設定完變數後重新啟動您的終端機/命令提示字元

2. **「連接 localhost:8080 被拒絕」**
   - 確保 MCP 計算器服務正在 8080 埠口運行
   - 檢查是否有其他服務佔用了 8080 埠口

3. **「認證失敗」**
   - 驗證您的 API 金鑰是否有效
   - 檢查 `OPENAI_BASE_URL` 是否與您預期使用的端點相符

4. **Maven 建置錯誤**
   - 確認您使用的是 Java 21 或以上版本：`java -version`
   - 嘗試清除建置：`mvnw clean`

### 除錯

若要啟用除錯日誌，執行時加入以下 JVM 參數：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 配置

此應用程式配置為：
- 預設使用 MiniMax-M3；可透過設定 `MINIMAX_MODEL_ID` 選擇 `MiniMax-M3` 或 `MiniMax-M2.7`
- 設定時連接 `OPENAI_BASE_URL`；若未設定，當 `MINIMAX_REGION=cn_zh` 使用 `https://api.minimaxi.com/v1`，否則預設使用 `https://api.minimax.io/v1`
- 連接 MCP 服務於 `http://localhost:8080/sse`
- 請求超時時間設為 60 秒

## 相依套件

專案中使用的主要相依套件：
- **LangChain4j**：用於 AI 整合與工具管理
- **LangChain4j MCP**：用於模型上下文協議支援
- **LangChain4j OpenAI 官方**：用於 MiniMax OpenAI 相容 API 整合
- **Spring Boot**：用於應用框架與相依注入

## 授權條款

本專案採用 Apache License 2.0 授權 - 詳情請參閱 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 檔案。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->