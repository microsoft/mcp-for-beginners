# 執行範例

> [!WARNING]
> 此範例使用已棄用的 Sampling 和舊版 HTTP+SSE 端點。它
> 保留以供 MCP `2025-11-25` 相容性使用。新的實作應直接呼叫
> LLM 供應商並使用可串流 HTTP 進行遠端 MCP 流量。

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

## 透過 GitHub Copilot 和 VS Code 測試伺服器

將條目加入 mcp.json 如下：

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

請確定您有點選伺服器上的「啟動」。

在 GitHub Copilot 中貼上以下提示：

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

第一次會詢問您是否接受 Sampling 動作，接著會請您接受執行「create_blog」工具。您應該會看到類似的回應：

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->