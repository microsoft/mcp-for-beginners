# MCP Roots（舊版功能）

> [!WARNING]
> Roots 從 MCP `2026-07-28` 起已被棄用。它們在此版本中保留以維持相容性，並且有可能在 2027 年 7 月 28 日或之後發佈的首個規範版本中被移除。新的實作應透過工具參數、資源 URI 或伺服器設定傳遞目錄或檔案。
> 兼容性並且適合於或之後發布的首個規範版本中移除。新實作應該透過工具參數、資源 URI 或伺服器配置傳遞目錄或檔案。
> 目錄或檔案透過工具參數、資源 URI 或伺服器配置進行傳遞。
> 透過工具參數、資源 URI 或伺服器配置傳遞目錄或檔案。


## 概覽

Roots 讓 MCP 用戶端告訴伺服器哪些檔案系統位置與當前請求相關。root 包含必需的 `file://` URI 及可選的易讀名稱。
與當前請求相關。root 包含必需的 `file://` URI 及可選的易讀名稱。






## 學習目標

完成本課程後，您將能夠：

- 解釋 MCP Roots 代表什麼以及不代表什麼。
- 辨認目前的 `roots/list` 多回合流程。
- 獨立於 Roots 應用安全控管。
- 將新實作移轉到受支持的替代方案。

## Root 資料

用戶端以 `file://` URI 返回每個 root，並可附帶顯示名稱：

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

用戶端應僅暴露用戶授權的位置。伺服器應將結果視為相關檔案的指引，不等同授權證明。






處理客戶端請求時，伺服器可返回包含 `roots/list` 輸入請求的 `InputRequiredResult`：

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

在 MCP `2025-11-25` 中，用戶端於初始化時宣告 Roots。伺服器可直接發出 `roots/list` 請求，用戶端可在 roots 改變時發送 `notifications/roots/list_changed`。

該生命週期為舊版行為。請勿將其初始化或通知範例與 `2026-07-28` 實作混用。




## 推薦替代方案

### 工具參數

在工具架構中明確指定需要的目錄或檔案：

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

當伺服器能透過穩定的 URI 暴露相關檔案時，使用 MCP 資源。這使得發現和存取更明確。







## 安全要求

無論選擇哪種替代方案：

- 暴露檔案系統位置前取得用戶同意。
- 對路徑進行正規化並驗證以防止遍歷。
- 獨立於 root 值實施授權和沙盒機制。
- 在檔案存取時重新檢查權限，而非僅在列表時。
- 避免在日誌或錯誤訊息中返回敏感路徑。

## 主要心得

- Roots 描述相關檔案系統位置；它們不儲存對話狀態。
- Roots 是指引，非存取控制界線。
- MCP `2026-07-28` 持有每次請求的能力並使用 `InputRequiredResult` 處理 `roots/list`。
- 新實作應改用工具參數、資源 URI 或伺服器配置。




## 額外資源

- [MCP 2026-07-28 中的 Roots](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [棄用功能登記](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [MCP 變更內容：2026-07-28 規範](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->