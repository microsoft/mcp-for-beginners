# MCP 根目錄（舊版功能）

> [!WARNING]
> 根目錄自 MCP `2026-07-28` 起已被棄用。它們在此版本中保留以維持相容性，並有可能在
> 2027 年 7 月 28 日或之後發佈的第一個規範版本中被移除。新的實作應透過工具參數、
> 資源 URI 或伺服器配置傳遞目錄或檔案。
> 
> 

## 概述

根目錄讓 MCP 客戶端告訴伺服器哪些檔案系統位置與當前請求有關。根目錄包含一個必需的 `file://` URI 與可選的人類可讀名稱。







## 學習目標

到本課程結束時，您將能夠：

- 解釋 MCP 根目錄代表什麼與不代表什麼。
- 辨識目前的 `roots/list` 多回合流程。
- 獨立於根目錄運用安全控管。
- 將新實作遷移至受支援的替代方案。

## 根目錄資料

客戶端將每個根目錄回傳為一個帶可選顯示名稱的 `file://` URI：

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

客戶端應僅暴露使用者核准的位置。伺服器應將結果視為相關檔案的指引，而非授權證明。






在處理客戶端請求時，伺服器可以回傳包含 `roots/list` 輸入請求的 `InputRequiredResult`：

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```








## 舊版 2025-11-25 行為

在 MCP `2025-11-25`，客戶端初始化時會廣告根目錄。伺服器可直接發出 `roots/list` 請求，且根目錄變更時，客戶端會發送 `notifications/roots/list_changed`。






## 推薦替代方案

### 工具參數

在工具規格中明確指定所需目錄或檔案：

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### 資源 URI

當伺服器能透過穩定 URI 來暴露相關檔案時，使用 MCP 資源。這可讓發現和擷取變得明確。







## 安全要求

不論選用何種替代方案：

- 暴露檔案系統位置前須取得使用者同意。
- 標準化並驗證路徑，以防止路徑遍歷。
- 獨立於根目錄值實施授權和沙箱機制。
- 存取檔案時再次檢查權限，而非僅在列出時檢查。
- 避免在日誌或錯誤訊息中回傳敏感路徑。

## 重要重點

- 根目錄描述相關的檔案系統位置；它們不存儲對話狀態。
- 根目錄是指引，而非存取控制邊界。
- MCP `2026-07-28` 在每次請求攜帶能力，且使用
  `InputRequiredResult` 來處理 `roots/list`。
- 新實作應改用工具參數、資源 URI 或伺服器配置。



## 額外資源

- [MCP 2026-07-28 的根目錄](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [棄用功能註冊表](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [MCP 變更內容：2026-07-28 規範](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->