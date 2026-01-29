# 完整的 MCP 客戶端範例

此目錄包含用不同程式語言編寫的完整且可運行的 MCP 客戶端範例。每個客戶端都展示了主 README.md 教學中描述的全部功能。

## 可用的客戶端

### 1. Java 客戶端 (`client_example_java.java`)

- **傳輸方式**: SSE（伺服器推送事件）透過 HTTP
- **目標伺服器**: `http://localhost:8080`
- **功能**:
  - 建立連線與 Ping
  - 工具清單
  - 計算機操作（加法、減法、乘法、除法、幫助）
  - 錯誤處理與結果提取

**執行方式:**

```bash
# Ensure your MCP server is running on localhost:8080
javac client_example_java.java
java client_example_java
```

### 2. C# 客戶端 (`client_example_csharp.cs`)

- **傳輸方式**: Stdio（標準輸入/輸出）
- **目標伺服器**: 本地 .NET MCP 伺服器，透過 dotnet run 啟動
- **功能**:
  - 透過 Stdio 傳輸自動啟動伺服器
  - 工具與資源清單
  - 計算機操作
  - JSON 結果解析
  - 全面的錯誤處理

**執行方式:**

```bash
dotnet run
```

### 3. TypeScript 客戶端 (`client_example_typescript.ts`)

- **傳輸方式**: Stdio（標準輸入/輸出）
- **目標伺服器**: 本地 Node.js MCP 伺服器
- **功能**:
  - 完整的 MCP 協議支援
  - 工具、資源與提示操作
  - 計算機操作
  - 資源讀取與提示執行
  - 強健的錯誤處理

**執行方式:**

```bash
# First compile TypeScript (if needed)
npm run build

# Then run the client
npm run client
# or
node client_example_typescript.js
```

### 4. Python 客戶端 (`client_example_python.py`)

- **傳輸方式**: Stdio（標準輸入/輸出）  
- **目標伺服器**: 本地 Python MCP 伺服器
- **功能**:
  - 使用 Async/Await 模式進行操作
  - 工具與資源探索
  - 測試計算機操作
  - 資源內容讀取
  - 基於類別的組織結構

**執行方式:**

```bash
python client_example_python.py
```

## 所有客戶端的共同特性

每個客戶端的實現都展示了以下功能：

1. **連線管理**
   - 與 MCP 伺服器建立連線
   - 處理連線錯誤
   - 正確的清理與資源管理

2. **伺服器探索**
   - 列出可用的工具
   - 列出可用的資源（若支援）
   - 列出可用的提示（若支援）

3. **工具調用**
   - 基本的計算機操作（加法、減法、乘法、除法）
   - 幫助指令以獲取伺服器資訊
   - 正確的參數傳遞與結果處理

4. **錯誤處理**
   - 連線錯誤
   - 工具執行錯誤
   - 優雅的失敗處理與用戶回饋

5. **結果處理**
   - 從回應中提取文字內容
   - 格式化輸出以提高可讀性
   - 處理不同的回應格式

## 先決條件

在運行這些客戶端之前，請確保您已完成以下事項：

1. **對應的 MCP 伺服器正在運行**（位於 `../01-first-server/`）
2. **安裝了所選語言的必要依賴項**
3. **具備正確的網路連接**（適用於基於 HTTP 的傳輸）

## 各實現之間的主要差異

| 語言       | 傳輸方式   | 伺服器啟動方式 | 非同步模型   | 關鍵函式庫           |
|------------|-----------|----------------|-------------|---------------------|
| Java       | SSE/HTTP  | 外部啟動       | 同步        | WebFlux, MCP SDK    |
| C#         | Stdio     | 自動啟動       | Async/Await | .NET MCP SDK        |
| TypeScript | Stdio     | 自動啟動       | Async/Await | Node MCP SDK        |
| Python     | Stdio     | 自動啟動       | AsyncIO     | Python MCP SDK      |
| Rust       | Stdio     | 自動啟動       | Async/Await | Rust MCP SDK, Tokio |

## 下一步

在探索這些客戶端範例後，您可以：

1. **修改客戶端**以添加新功能或操作
2. **創建自己的伺服器**並使用這些客戶端進行測試
3. **嘗試不同的傳輸方式**（SSE 與 Stdio）
4. **構建更複雜的應用程式**，整合 MCP 功能

## 疑難排解

### 常見問題

1. **連線被拒絕**: 確保 MCP 伺服器正在預期的埠/路徑上運行
2. **找不到模組**: 安裝所需語言的 MCP SDK
3. **權限被拒絕**: 檢查 Stdio 傳輸的檔案權限
4. **找不到工具**: 驗證伺服器是否實現了預期的工具

### 偵錯提示

1. **啟用 MCP SDK 的詳細日誌記錄**
2. **檢查伺服器日誌**以獲取錯誤訊息
3. **驗證工具名稱與簽名**是否在客戶端與伺服器之間匹配
4. **先使用 MCP Inspector 測試**以驗證伺服器功能

## 相關文件

- [主要客戶端教學](./README.md)
- [MCP 伺服器範例](../../../../03-GettingStarted/01-first-server)
- [MCP 與 LLM 整合](../../../../03-GettingStarted/03-llm-client)
- [官方 MCP 文件](https://modelcontextprotocol.io/)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。