# 範例：基本 Host

一個參考實作，展示如何建立一個 MCP host 應用程式，連接至 MCP 伺服器並在安全沙盒中渲染工具 UI。

此基本 host 也可用於本地開發期間測試 MCP 應用程式。

## 主要檔案

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI host，包含工具選擇、參數輸入與 iframe 管理
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - 外層 iframe 代理，具有安全驗證和雙向訊息中繼
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - 核心邏輯：伺服器連接、工具呼叫與 AppBridge 設定

## 快速開始

```bash
npm install
npm run start
# 打開 http://localhost:8080
```

預設情況下，host 應用程式會嘗試連接到 `http://localhost:3001/mcp` 的 MCP 伺服器。您可以透過設定 `SERVERS` 環境變數為伺服器 URL 的 JSON 陣列來自訂此行為：

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## 架構介紹

此範例使用雙 iframe 沙盒模式來確保 UI 隔離的安全性：

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**為什麼使用兩個 iframes？**

- 外層 iframe 運行於不同的來源（8081 埠），防止直接存取 host
- 內層 iframe 透過 `srcdoc` 接收 HTML，受 sandbox 屬性限制
- 訊息經由外層 iframe 驗證並雙向中繼傳遞

此架構確保即使工具 UI 程式碼帶有惡意，也無法存取 host 應用程式的 DOM、cookie 或 JavaScript 執行環境。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。如因使用本翻譯內容而產生任何誤解或曲解，我們不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->