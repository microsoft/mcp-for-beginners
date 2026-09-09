# 計算機 LLM 用戶端

一個 Java 應用程式，展示如何使用 LangChain4j 透過 MiniMax OpenAI 相容 API 連接到 MCP (模型上下文協議) 計算機服務。

## 前置條件

- Java 21 或以上版本
- Maven 3.6+（或使用內置的 Maven wrapper）
- MiniMax API 金鑰
- 一個運行於 `http://localhost:8080` 的 MCP 計算機服務

## 獲取 API 金鑰

此應用程式使用 MiniMax OpenAI 相容 API。請按以下步驟獲取您的金鑰及端點：

### 1. 選擇端點
1. 使用 `https://api.minimax.io/v1` 作為全球端點
2. 使用 `https://api.minimaxi.com/v1` 作為中國端點

### 2. 建立 API 金鑰
1. 從您的 MiniMax 帳號建立一個 MiniMax API 金鑰
2. 將金鑰妥善保存

### 3. 設置環境變量

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

## 設置與安裝

1. <strong>克隆或進入專案目錄</strong>

2. <strong>安裝依賴</strong>：
   ```cmd
   mvnw clean install
   ```
   或如果您已全域安裝 Maven：
   ```cmd
   mvn clean install
   ```

3. <strong>設定環境變量</strong>（請參閱以上「獲取 API 金鑰」章節）

4. **啟動 MCP 計算機服務**：
   請確保您已啟動第一章的 MCP 計算機服務，並運行於 `http://localhost:8080/sse`。這應該在啟動客戶端前運行。

## 執行應用程式

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 應用程式功能說明

此應用程式展示了三種主要的與計算機服務的互動：

1. <strong>加法</strong>：計算 24.5 與 17.3 的和
2. <strong>平方根</strong>：計算 144 的平方根
3. <strong>幫助</strong>：顯示可用的計算機函數

## 預期輸出

成功執行時，您應該見到類似以下輸出：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 疑難排解

### 常見問題

1. **「OPENAI_API_KEY 環境變量未設置」**
   - 請確定您已設置 `OPENAI_API_KEY` 環境變量
   - 設置變量後請重新啟動終端機/命令提示字元

2. **「拒絕連接 localhost:8080」**
   - 確保 MCP 計算機服務正運行於 8080 埠口
   - 檢查是否有其他服務佔用 8080 埠口

3. **「認證失敗」**
   - 驗證您的 API 金鑰是否有效
   - 確認 `OPENAI_BASE_URL` 是否與您欲使用的端點相符

4. **Maven 建置錯誤**
   - 確保您使用的是 Java 21 或以上版本：`java -version`
   - 嘗試清理建置：`mvnw clean`

### 偵錯

執行時，加入以下 JVM 參數以開啟偵錯日誌：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 配置

應用程式配置如下：
- 預設使用 MiniMax-M3；可設置 `MINIMAX_MODEL_ID` 選擇 `MiniMax-M3` 或 `MiniMax-M2.7`
- 設定時，連接 `OPENAI_BASE_URL`；否則在 `MINIMAX_REGION=cn_zh` 時使用 `https://api.minimaxi.com/v1`，預設使用 `https://api.minimax.io/v1`
- 連接 MCP 服務於 `http://localhost:8080/sse`
- 請求超時設定為 60 秒

## 相依套件

此專案使用的主要相依套件：
- **LangChain4j**：用於 AI 整合與工具管理
- **LangChain4j MCP**：用於模型上下文協議支援
- **LangChain4j OpenAI official**：用於 MiniMax OpenAI 相容 API 整合
- **Spring Boot**：用於應用框架與依賴注入

## 授權條款

本專案採用 Apache License 2.0 授權，詳細內容請見 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 檔案。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->