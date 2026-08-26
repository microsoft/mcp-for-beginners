# 計算器 LLM 用戶端

一個 Java 應用程式，示範如何使用 LangChain4j 通過 MiniMax 相容 OpenAI 的 API 連接 MCP（模型上下文協議）計算服務。

## 前置條件

- Java 21 或更高版本
- Maven 3.6+（或使用內建的 Maven 包裝器）
- 一個 MiniMax API 金鑰
- 一個在 `http://localhost:8080` 運行的 MCP 計算器服務

## 獲取 API 金鑰

此應用程式使用 MiniMax 相容 OpenAI 的 API。請按照以下步驟獲取您的金鑰和端點：

### 1. 選擇端點
1. 全球端點請使用 `https://api.minimax.io/v1`
2. 中國端點請使用 `https://api.minimaxi.com/v1`

### 2. 建立 API 金鑰
1. 從您的 MiniMax 帳戶建立 MiniMax API 金鑰
2. 將金鑰妥善保存

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

## 設置與安裝

1. <strong>複製或切換至專案目錄</strong>

2. <strong>安裝相依</strong>
   ```cmd
   mvnw clean install
   ```
   或者如果您已全域安裝 Maven：
   ```cmd
   mvn clean install
   ```

3. <strong>設定環境變數</strong>（參閱上方「獲取 API 金鑰」部分）

4. **啟動 MCP 計算器服務**：
   確保您已啟動第 1 章的 MCP 計算器服務，地址是 `http://localhost:8080/sse`。啟動用戶端前此服務應持續運行。

## 執行應用程式

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 應用程式功能

此應用程式示範與計算器服務的三大互動：

1. <strong>加法</strong>：計算 24.5 和 17.3 的和
2. <strong>平方根</strong>：計算 144 的平方根
3. <strong>幫助</strong>：顯示可用的計算器功能

## 預期輸出

成功運行時，您應該看到類似的輸出：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 疑難排解

### 常見問題

1. **「OPENAI_API_KEY 環境變數未設定」**
   - 請確認您已設定 `OPENAI_API_KEY` 環境變數
   - 設定變數後重啟您的終端機／命令提示字元

2. **「連線被拒於 localhost:8080」**
   - 確認 MCP 計算器服務正在使用 8080 埠口
   - 檢查是否有其他服務佔用 8080 埠口

3. **「身份驗證失敗」**
   - 驗證您的 API 金鑰是否有效
   - 確認 `OPENAI_BASE_URL` 與您欲使用的端點相符

4. **Maven 建置錯誤**
   - 確認您使用的是 Java 21 或以上版本：`java -version`
   - 試著清理建置：`mvnw clean`

### 偵錯

執行時若要啟用除錯日誌，可加上以下 JVM 參數：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 配置

應用程式預設設定為：
- 預設使用 MiniMax-M3，當設定 `MINIMAX_MODEL_ID` 時則使用 MiniMax-M2.7
- 若設定了 `OPENAI_BASE_URL`，則連接該地址；否則當 `MINIMAX_REGION=cn_zh` 使用 `https://api.minimaxi.com/v1`，預設使用 `https://api.minimax.io/v1`
- 連接 MCP 服務地址為 `http://localhost:8080/sse`
- 請求超時時間設定為 60 秒

## 相依套件

專案中使用的關鍵相依：
- **LangChain4j**：用於 AI 整合及工具管理
- **LangChain4j MCP**：用於 Model Context Protocol 支援
- **LangChain4j OpenAI official**：用於 MiniMax 相容 OpenAI API 整合
- **Spring Boot**：用於應用框架及依賴注入

## 授權條款

本專案採用 Apache License 2.0 授權，詳見 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 檔案。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->