# MCP stdio 伺服器 - TypeScript 解決方案

> **⚠️ 重要**：此解決方案已更新為使用 **stdio 傳輸**，根據 MCP 規範 2025-06-18 的建議。原本的 SSE 傳輸已被棄用。

## 概述

此 TypeScript 解決方案展示了如何使用目前的 stdio 傳輸來建立 MCP 伺服器。相比於已棄用的 SSE 方法，stdio 傳輸更簡單、更安全，且性能更佳。

## 先決條件

- Node.js 18 或更新版本
- npm 或 yarn 套件管理工具

## 設置指南

### 步驟 1：安裝依賴項

```bash
npm install
```

### 步驟 2：建置專案

```bash
npm run build
```

## 啟動伺服器

stdio 伺服器的運行方式與舊版 SSE 伺服器不同。它不啟動網頁伺服器，而是通過 stdin/stdout 進行通信：

```bash
npm start
```

**重要**：伺服器看起來像是卡住了——這是正常的！它正在等待來自 stdin 的 JSON-RPC 消息。

## 測試伺服器

### 方法 1：使用 MCP Inspector（推薦）

```bash
npm run inspector
```

這將：
1. 將伺服器作為子進程啟動
2. 開啟一個網頁介面進行測試
3. 讓您可以互動式測試所有伺服器工具

### 方法 2：直接使用命令列測試

您也可以直接啟動 Inspector 進行測試：

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### 可用工具

伺服器提供以下工具：

- **add(a, b)**：將兩個數字相加
- **multiply(a, b)**：將兩個數字相乘  
- **get_greeting(name)**：生成個性化問候語
- **get_server_info()**：獲取伺服器資訊

### 使用 Claude Desktop 進行測試

若要在 Claude Desktop 中使用此伺服器，請在 `claude_desktop_config.json` 中添加以下配置：

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## 專案結構

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## 與 SSE 的主要差異

**stdio 傳輸（目前使用）：**
- ✅ 設置更簡單 - 不需要 HTTP 伺服器
- ✅ 更高的安全性 - 無需 HTTP 端點
- ✅ 基於子進程的通信
- ✅ 通過 stdin/stdout 使用 JSON-RPC
- ✅ 性能更佳

**SSE 傳輸（已棄用）：**
- ❌ 需要設置 Express 伺服器
- ❌ 需要複雜的路由和會話管理
- ❌ 更多依賴項（Express、HTTP 處理）
- ❌ 額外的安全性考量
- ❌ MCP 2025-06-18 中已棄用

## 開發提示

- 使用 `console.error()` 進行日誌記錄（切勿使用 `console.log()`，因為它會寫入 stdout）
- 在測試之前使用 `npm run build` 進行建置
- 使用 Inspector 進行視覺化除錯
- 確保所有 JSON 消息格式正確
- 伺服器會在接收到 SIGINT/SIGTERM 時自動處理平滑關閉

此解決方案遵循最新的 MCP 規範，並展示了使用 TypeScript 實現 stdio 傳輸的最佳實踐。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。