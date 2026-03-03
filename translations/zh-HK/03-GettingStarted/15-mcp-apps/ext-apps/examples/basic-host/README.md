# 範例：基本 Host

一個參考實作，展示如何建立連接 MCP 伺服器並在安全沙盒中渲染工具 UI 的 MCP host 應用程式。

此基本 host 也可用於本地開發期間測試 MCP 應用。

## 主要檔案

- [`index.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/index.html) / [`src/index.tsx`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/index.tsx) - React UI host，具備工具選擇、參數輸入及 iframe 管理
- [`sandbox.html`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/sandbox.html) / [`src/sandbox.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/sandbox.ts) - 外層 iframe 代理，含安全驗證及雙向訊息中繼
- [`src/implementation.ts`](../../../../../../../03-GettingStarted/15-mcp-apps/ext-apps/examples/basic-host/src/implementation.ts) - 核心邏輯：伺服器連線、工具呼叫及 AppBridge 設定

## 快速開始

```bash
npm install
npm run start
# 開啟 http://localhost:8080
```

預設情況下，host 應用程式會嘗試連接至 `http://localhost:3001/mcp` 的 MCP 伺服器。您可以設定 `SERVERS` 環境變數，使用一個包含伺服器 URL 的 JSON 陣列來調整此行為：

```bash
SERVERS='["http://localhost:1234/mcp", "http://localhost:5678/mcp"]' npm run start
```

## 架構

此範例採用雙 iframe 沙盒模式以達到安全 UI 隔離：

```
Host (port 8080)
  └── Outer iframe (port 8081) - sandbox proxy
        └── Inner iframe (srcdoc) - untrusted tool UI
```

**為何使用兩層 iframe？**

- 外層 iframe 運行於不同來源（8081 埠），防止直接訪問 host
- 內層 iframe 透過 `srcdoc` 接收 HTML，並受到 sandbox 屬性限制
- 訊息透過外層 iframe 流動，由其驗證並雙向中繼

此架構確保即使工具 UI 程式碼具有惡意，也無法存取 host 應用的 DOM、cookies 或 JavaScript 環境。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->