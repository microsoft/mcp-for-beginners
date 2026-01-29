# MCP stdio Server - .NET 解決方案

> **⚠️ 重要**：此解決方案已更新為使用 **stdio 傳輸**，根據 MCP 規範 2025-06-18 的建議。原本的 SSE 傳輸已被棄用。

## 概述

此 .NET 解決方案展示如何使用目前的 stdio 傳輸來建立 MCP 伺服器。相比已棄用的 SSE 方法，stdio 傳輸更簡單、更安全，且性能更佳。

## 先決條件

- .NET 9.0 SDK 或更新版本
- 基本了解 .NET 的依賴注入

## 設置指引

### 步驟 1：還原依賴項

```bash
dotnet restore
```

### 步驟 2：建置專案

```bash
dotnet build
```

## 啟動伺服器

stdio 伺服器的運行方式與舊的基於 HTTP 的伺服器不同。它通過標準輸入/輸出進行通信，而不是啟動一個網頁伺服器：

```bash
dotnet run
```

**重要**：伺服器看起來像是卡住了——這是正常的！它正在等待來自標準輸入的 JSON-RPC 消息。

## 測試伺服器

### 方法 1：使用 MCP Inspector（推薦）

```bash
npx @modelcontextprotocol/inspector dotnet run
```

這將：
1. 將伺服器作為子進程啟動
2. 開啟一個網頁介面進行測試
3. 讓您可以互動式測試所有伺服器工具

### 方法 2：直接使用命令行測試

您也可以直接啟動 Inspector 進行測試：

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### 可用工具

伺服器提供以下工具：

- **AddNumbers(a, b)**：將兩個數字相加
- **MultiplyNumbers(a, b)**：將兩個數字相乘  
- **GetGreeting(name)**：生成個性化問候語
- **GetServerInfo()**：獲取伺服器資訊

### 使用 Claude Desktop 測試

若要在 Claude Desktop 中使用此伺服器，請在您的 `claude_desktop_config.json` 中添加以下配置：

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## 專案結構

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## 與 HTTP/SSE 的主要差異

**stdio 傳輸（目前使用）：**
- ✅ 設置更簡單——不需要網頁伺服器
- ✅ 更高的安全性——無需 HTTP 端點
- ✅ 使用 `Host.CreateApplicationBuilder()` 而非 `WebApplication.CreateBuilder()`
- ✅ 使用 `WithStdioTransport()` 而非 `WithHttpTransport()`
- ✅ 主控台應用程式而非網頁應用程式
- ✅ 性能更佳

**HTTP/SSE 傳輸（已棄用）：**
- ❌ 需要 ASP.NET Core 網頁伺服器
- ❌ 需要 `app.MapMcp()` 路由設置
- ❌ 配置和依賴項更複雜
- ❌ 額外的安全性考量
- ❌ 在 MCP 2025-06-18 中已被棄用

## 開發功能

- **依賴注入**：全面支持服務和日誌的 DI
- **結構化日誌**：使用 `ILogger<T>` 正確記錄到標準錯誤輸出
- **工具屬性**：使用 `[McpServerTool]` 屬性清晰定義工具
- **異步支持**：所有工具支持異步操作
- **錯誤處理**：優雅的錯誤處理和日誌記錄

## 開發提示

- 使用 `ILogger` 進行日誌記錄（切勿直接寫入標準輸出）
- 在測試前使用 `dotnet build` 進行建置
- 使用 Inspector 進行視覺化調試
- 所有日誌自動記錄到標準錯誤輸出
- 伺服器能夠處理優雅的關閉信號

此解決方案遵循最新的 MCP 規範，並展示了使用 .NET 實現 stdio 傳輸的最佳實踐。

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。