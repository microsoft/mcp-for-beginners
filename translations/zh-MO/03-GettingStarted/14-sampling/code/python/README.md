# 執行範例

> [!WARNING]
> 此範例使用已棄用的 Sampling 及舊版 HTTP+SSE 端點。
> 保留以供 MCP `2025-11-25` 相容使用。新的實作應直接呼叫
> LLM 供應商並使用可串流的 HTTP 處理遠端 MCP 流量。

## 建立虛擬環境

```sh
python -m venv venv
source ./venv/bin/activate
```

## 安裝相依套件

```sh
pip install "mcp[cli]"
```

## 啟動伺服器

```sh
uvicorn server:app --port 8000
```

## 使用 GitHub Copilot 及 VS Code 測試伺服器

在 mcp.json 中加入以下條目：

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

確定你點選了伺服器上的「start」。

在 GitHub Copilot 貼上以下提示：

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

第一次你會被詢問是否接受 Sampling 動作，接著會請你接受執行工具 "create_blog"。你應該會看到類似的回應：

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->