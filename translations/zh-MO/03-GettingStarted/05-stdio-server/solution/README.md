# MCP stdio 伺服器解決方案

> **⚠️ 重要**：這些解決方案已更新為使用 **stdio 傳輸**，根據 MCP 規範 2025-06-18 的建議。原本的 SSE（伺服器推送事件）傳輸已被棄用。

以下是使用 stdio 傳輸在各個執行環境中建構 MCP 伺服器的完整解決方案：

- [TypeScript](../../../../../03-GettingStarted/05-stdio-server/solution/typescript) - 完整的 stdio 伺服器實作
- [Python](../../../../../03-GettingStarted/05-stdio-server/solution/python) - 使用 asyncio 的 Python stdio 伺服器
- [.NET](../../../../../03-GettingStarted/05-stdio-server/solution/dotnet) - 使用相依性注入的 .NET stdio 伺服器

每個解決方案展示了：
- 設置 stdio 傳輸
- 定義伺服器工具
- 正確處理 JSON-RPC 訊息
- 與 MCP 客戶端（如 Claude）的整合

所有解決方案均遵循最新的 MCP 規範，並使用建議的 stdio 傳輸以達到最佳效能與安全性。

---

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解讀概不負責。