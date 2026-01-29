# 執行範例

此範例啟動了一個 MCP Server，並使用中介軟體檢查是否有有效的 Authorization 標頭。

## 安裝依賴項目

```bash
pip install "mcp[cli]" 
```

## 啟動伺服器

```bash
python server.py
```

在另一個終端啟動客戶端

```bash
python client.py
```

你應該會看到類似以下的結果：

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

這表示傳遞的憑證已被允許。

嘗試將 `client.py` 中的憑證更改為 "secret-token2"，然後你應該會在回應中看到以下文字：

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

這表示你已被認證（你有憑證），但該憑證無效。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋不承擔責任。