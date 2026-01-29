# MCP stdio 伺服器 - .NET 解決方案

> **⚠️ 重要**：此解決方案已更新為使用 **stdio 傳輸**，根據 MCP 規範 2025-06-18 的建議。原本的 SSE 傳輸已被棄用。

## 概述

此 .NET 解決方案展示了如何使用目前的 stdio 傳輸來構建 MCP 伺服器。相比於已棄用的 SSE 方法，stdio 傳輸更簡單、更安全，且效能更佳。

## 先決條件

- .NET 9.0 SDK 或更新版本
- 基本的 .NET 相依性注入知識

## 設置說明

### 步驟 1：還原相依性

```bash
dotnet restore
```

### 步驟 2：建置專案

```bash
dotnet build
```

## 啟動伺服器

stdio 伺服器的運行方式與舊的基於 HTTP 的伺服器不同。它不啟動網頁伺服器，而是通過 stdin/stdout 進行通信：

```bash
dotnet run
```

**重要**：伺服器看起來會像是卡住了——這是正常的！它正在等待來自 stdin 的 JSON-RPC 訊息。

## 測試伺服器

### 方法 1：使用 MCP Inspector（推薦）

```bash
npx @modelcontextprotocol/inspector dotnet run
```

這將會：
1. 將伺服器作為子程序啟動
2. 開啟一個網頁介面進行測試
3. 讓您可以互動式測試所有伺服器工具

### 方法 2：直接使用命令列測試

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

若要在 Claude Desktop 中使用此伺服器，請將以下配置新增到您的 `claude_desktop_config.json`：

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

**stdio 傳輸（目前）：**
- ✅ 設置更簡單——不需要網頁伺服器
- ✅ 更高的安全性——無需 HTTP 端點
- ✅ 使用 `Host.CreateApplicationBuilder()` 而非 `WebApplication.CreateBuilder()`
- ✅ 使用 `WithStdioTransport()` 而非 `WithHttpTransport()`
- ✅ 主控台應用程式而非網頁應用程式
- ✅ 更佳的效能

**HTTP/SSE 傳輸（已棄用）：**
- ❌ 需要 ASP.NET Core 網頁伺服器
- ❌ 需要 `app.MapMcp()` 路由設置
- ❌ 配置和相依性更複雜
- ❌ 額外的安全性考量
- ❌ 已於 MCP 2025-06-18 棄用

## 開發功能

- **相依性注入**：完整支援服務和日誌的 DI
- **結構化日誌**：使用 `ILogger<T>` 將日誌正確記錄到 stderr
- **工具屬性**：使用 `[McpServerTool]` 屬性清晰定義工具
- **非同步支援**：所有工具支援非同步操作
- **錯誤處理**：優雅的錯誤處理和日誌記錄

## 開發提示

- 使用 `ILogger` 進行日誌記錄（切勿直接寫入 stdout）
- 在測試前使用 `dotnet build` 進行建置
- 使用 Inspector 進行視覺化除錯
- 所有日誌會自動記錄到 stderr
- 伺服器會處理優雅的關閉信號

此解決方案遵循最新的 MCP 規範，並展示了使用 .NET 實現 stdio 傳輸的最佳實踐。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。