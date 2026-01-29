# Calculator LLM Client

一個示範如何使用 LangChain4j 連接帶有 GitHub Models 整合的 MCP（Model Context Protocol）計算器服務的 Java 應用程式。

## 先決條件

- Java 21 或以上版本
- Maven 3.6+（或使用內建的 Maven wrapper）
- 擁有可使用 GitHub Models 的 GitHub 帳號
- 在 `http://localhost:8080` 運行中的 MCP 計算器服務

## 取得 GitHub Token

此應用程式使用 GitHub Models，需要 GitHub 個人存取權杖。請依照以下步驟取得您的權杖：

### 1. 存取 GitHub Models
1. 前往 [GitHub Models](https://github.com/marketplace/models)
2. 使用您的 GitHub 帳號登入
3. 若尚未取得，請申請使用 GitHub Models 的權限

### 2. 建立個人存取權杖
1. 前往 [GitHub 設定 → 開發者設定 → 個人存取權杖 → 權杖（經典）](https://github.com/settings/tokens)
2. 點選「Generate new token」→「Generate new token (classic)」
3. 為您的權杖命名（例如：「MCP Calculator Client」）
4. 設定過期時間（視需求而定）
5. 選擇以下權限範圍：
   - `repo`（若需存取私人倉庫）
   - `user:email`
6. 點選「Generate token」
7. **重要**：請立即複製權杖，之後無法再次查看！

### 3. 設定環境變數

#### 在 Windows（命令提示字元）：
```cmd
set GITHUB_TOKEN=your_github_token_here
```

#### 在 Windows（PowerShell）：
```powershell
$env:GITHUB_TOKEN="your_github_token_here"
```

#### 在 macOS/Linux：
```bash
export GITHUB_TOKEN=your_github_token_here
```

## 設定與安裝

1. **複製或切換到專案目錄**

2. **安裝相依套件**：
   ```cmd
   mvnw clean install
   ```
   或者如果您已全域安裝 Maven：
   ```cmd
   mvn clean install
   ```

3. **設定環境變數**（請參考上方「取得 GitHub Token」章節）

4. **啟動 MCP 計算器服務**：
   請確保您已啟動第一章的 MCP 計算器服務，並在 `http://localhost:8080/sse` 運行。啟動客戶端前必須先啟動此服務。

## 執行應用程式

```cmd
mvnw clean package
java -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 應用程式功能說明

此應用程式示範與計算器服務的三種主要互動：

1. **加法**：計算 24.5 與 17.3 的和
2. **平方根**：計算 144 的平方根
3. **幫助**：顯示可用的計算器功能

## 預期輸出

成功執行時，您應該會看到類似以下的輸出：

```
The sum of 24.5 and 17.3 is 41.8.
The square root of 144 is 12.
The calculator service provides the following functions: add, subtract, multiply, divide, sqrt, power...
```

## 疑難排解

### 常見問題

1. **「GITHUB_TOKEN 環境變數未設定」**
   - 確認您已設定 `GITHUB_TOKEN` 環境變數
   - 設定後請重新啟動終端機或命令提示字元

2. **「連線被拒絕 localhost:8080」**
   - 確認 MCP 計算器服務已在 8080 埠口運行
   - 檢查是否有其他服務佔用 8080 埠口

3. **「驗證失敗」**
   - 確認您的 GitHub 權杖有效且擁有正確權限
   - 確認您有權限使用 GitHub Models

4. **Maven 建置錯誤**
   - 確認您使用的是 Java 21 或以上版本：`java -version`
   - 嘗試清理建置：`mvnw clean`

### 除錯

若要啟用除錯日誌，執行時加入以下 JVM 參數：
```cmd
java -Dlogging.level.dev.langchain4j=DEBUG -jar target\calculator-llm-client-0.0.1-SNAPSHOT.jar
```

## 設定

應用程式設定為：
- 使用 GitHub Models，模型為 `gpt-4.1-nano`
- 連接 MCP 服務位址為 `http://localhost:8080/sse`
- 請求逾時時間為 60 秒
- 啟用請求/回應日誌以利除錯

## 相依套件

本專案主要使用的相依套件：
- **LangChain4j**：用於 AI 整合與工具管理
- **LangChain4j MCP**：支援 Model Context Protocol
- **LangChain4j GitHub Models**：整合 GitHub Models
- **Spring Boot**：應用程式框架與依賴注入

## 授權條款

本專案採用 Apache License 2.0 授權，詳情請參閱 [LICENSE](../../../../../../03-GettingStarted/03-llm-client/solution/java/LICENSE) 檔案。

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋負責。