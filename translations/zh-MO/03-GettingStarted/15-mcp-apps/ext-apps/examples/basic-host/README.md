# Example: Basic Host

一個參考實作，展示如何建立一個 MCP host 應用程式，該應用程式連接至 MCP 伺服器並在安全的沙盒環境中呈現工具 UI。

此基本 host 亦可用於本地開發期間測試 MCP Apps。

## 主要檔案

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI host，具備工具選擇、參數輸入及 iframe 管理功能
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - 外層 iframe 代理，包含安全驗證與雙向訊息中繼
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - 核心邏輯：伺服器連線、工具呼叫及 AppBridge 設定

## 快速開始

```bash
npm install
npm run start
# 開啟 http://localhost:8080
```

預設情況下，host 應用程式會嘗試連接至位於 `http://localhost:3001/mcp` 的 MCP 伺服器。您可以透過設定 `SERVERS` 環境變數（其內容為伺服器 URL 的 JSON 陣列）來配置這個行為：

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## 架構

此範例採用雙 iframe 沙盒模式，以確保 UI 的安全隔離：

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**為什麼需要兩個 iframe？**

- 外層 iframe 運行於不同的來源（8081 埠口），防止直接存取 host
- 內層 iframe 透過 `srcdoc` 接收 HTML，並受沙盒屬性限制
- 訊息經由外層 iframe 傳遞，且由外層 iframe 進行驗證及雙向中繼

此架構確保即使工具 UI 程式碼為惡意，也無法存取 host 應用程式的 DOM、Cookie 或 JavaScript 環境。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。儘管我們致力於確保準確性，請注意自動翻譯可能包含錯誤或不準確之處。原文文件應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯而引致之任何誤解或誤譯概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->