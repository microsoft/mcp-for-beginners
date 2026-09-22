# 使用 MCP Inspector 進行除錯

> [!NOTE]
> 使用 `--sse` 的指令及以 `/sse` 結尾的 URL 是測試舊版 HTTP+SSE 傳輸。針對新的 MCP `2026-07-28` 伺服器，請使用支援 Streamable HTTP 的 Inspector 版本，並選擇該傳輸方式。

> 支援 Streamable HTTP 的 Inspector 版本，並選擇該傳輸方式。

**MCP Inspector** 是一款必不可少的除錯工具，讓你能夠互動式測試和除錯 MCP 伺服器，而不需要完整的 AI 主機應用程式。它就像 MCP 的「Postman」— 提供視覺化介面來發送請求、查看回應，並了解伺服器的行為。

## 為什麼使用 MCP Inspector？

在建立 MCP 伺服器時，你經常會遇到如下挑戰：

- **「我的伺服器有在運行嗎？」** — Inspector 顯示連線狀態
- **「我的工具有正確註冊嗎？」** — Inspector 列出所有可用工具
- **「回應格式是什麼？」** — Inspector 顯示完整 JSON 回應
- **「為什麼這個工具不工作？」** — Inspector 顯示詳細錯誤訊息

## 前置條件

- 已安裝 Node.js 18+
- npm（隨 Node.js 附帶）
- 一個 MCP 伺服器以供測試（參見 [Module 3.1 - First Server](../01-first-server/README.md)）

## 安裝

### 選項 1：使用 npx 執行（建議快速測試）

```bash
npx @modelcontextprotocol/inspector
```

### 選項 2：全域安裝

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### 選項 3：加入你的專案

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

加入 `package.json`：
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## 連接到你的伺服器

### stdio 伺服器（本地程序）

適用於透過標準輸入/輸出通訊的伺服器：

```bash
# Python 伺服器
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js 伺服器
npx @modelcontextprotocol/inspector node ./build/index.js

# 使用環境變數
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP 伺服器（網路）

適用於作為 HTTP 服務運行的伺服器：

1. 首先啟動你的伺服器：
   ```bash
   python server.py  # 伺服器正在 http://localhost:8080 運行
   ```

2. 啟動 Inspector 並連接：
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Inspector 介面概覽

啟動 Inspector 時，你將看到一個網頁介面（通常位於 `http://localhost:5173`）：

```
┌─────────────────────────────────────────────────────────────┐
│  MCP Inspector                              [Connected ✅]   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │   🔧 Tools  │  │ 📄 Resources│  │ 💬 Prompts  │         │
│  │    (3)      │  │    (2)      │  │    (1)      │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  📋 Message Log                                       │ │
│  │  ─────────────────────────────────────────────────── │ │
│  │  → initialize                                         │ │
│  │  ← initialized (server info)                          │ │
│  │  → tools/list                                         │ │
│  │  ← tools (3 tools)                                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 測試工具

### 列出可用工具

1. 點選 **Tools** 標籤
2. Inspector 會自動呼叫 `tools/list`
3. 你會看到所有註冊的工具，包含：
   - 工具名稱
   - 描述
   - 入參模式（參數）

### 呼叫工具

1. 從列表中選擇一個工具
2. 在表單中填入所需參數
3. 點選 **Run Tool**
4. 在結果面板查看回應

**範例：測試一個計算器工具**

```
Tool: add
Parameters:
  a: 25
  b: 17

Response:
{
  "content": [
    {
      "type": "text",
      "text": "42"
    }
  ]
}
```

### 除錯工具錯誤

當工具失敗時，Inspector 會顯示：

```
Error Response:
{
  "error": {
    "code": -32602,
    "message": "Invalid params: 'b' is required"
  }
}
```

常見錯誤代碼：
| 代碼 | 意義 |
|------|---------|
| -32700 | 解析錯誤（無效 JSON） |
| -32600 | 無效請求 |
| -32601 | 找不到方法 |
| -32602 | 無效參數 |
| -32603 | 內部錯誤 |

---

## 測試資源

### 列出資源

1. 點選 **Resources** 標籤
2. Inspector 呼叫 `resources/list`
3. 你會看到：
   - 資源 URI
   - 名稱與描述
   - MIME 類型

### 讀取資源

1. 選擇一個資源
2. 點選 **Read Resource**
3. 查看回傳的內容

**範例輸出：**

```
Resource: file:///config/settings.json
Content-Type: application/json

{
  "config": {
    "debug": true,
    "maxConnections": 10
  }
}
```

---

## 測試提示詞

### 列出提示詞

1. 點選 **Prompts** 標籤
2. Inspector 呼叫 `prompts/list`
3. 查看可用的提示詞模板

### 取得提示詞

1. 選擇一個提示詞
2. 填寫所需的參數
3. 點選 **Get Prompt**
4. 查看呈現的提示詞訊息

---

## 訊息紀錄分析

訊息紀錄顯示了所有 MCP 協議訊息。以下記錄來自
已移除 `initialize` 握手的
傳統 `2025-11-25` 伺服器。`2026-07-28` 伺服器使用自包含請求元資料和 `server/discover`
。

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### 注意事項

- **請求/回應配對**：每個 `→` 應該有相對應的 `←`
- <strong>錯誤訊息</strong>：查看回應中的 `"error"`
- <strong>時間</strong>：過長間隔可能指示效能問題
- <strong>協議版本</strong>：確保伺服器與客戶端版本一致

---

## VS Code 整合

你可以直接從 VS Code 執行 Inspector：

### 使用 launch.json

新增至 `.vscode/launch.json`：

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Debug with MCP Inspector",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npx",
      "runtimeArgs": [
        "@modelcontextprotocol/inspector",
        "python",
        "${workspaceFolder}/server.py"
      ],
      "console": "integratedTerminal"
    },
    {
      "name": "Debug SSE Server with Inspector",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:5173",
      "preLaunchTask": "Start MCP Inspector"
    }
  ]
}
```

### 使用 Tasks

新增至 `.vscode/tasks.json`：

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npx @modelcontextprotocol/inspector node ${workspaceFolder}/build/index.js",
      "isBackground": true,
      "problemMatcher": {
        "pattern": {
          "regexp": "^$"
        },
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Inspector",
          "endsPattern": "listening"
        }
      }
    }
  ]
}
```

---

## 常見除錯情景

### 情景 1：伺服器無法連線

**症狀：** Inspector 顯示「Disconnected」或停留在「Connecting...」

**檢查清單：**
1. ✅ 伺服器指令是否正確？
2. ✅ 是否已安裝所有依賴？
3. ✅ 伺服器路徑是絕對路徑還是相對目前目錄？
4. ✅ 是否設定必要的環境變數？

**除錯步驟：**
```bash
# 先手動測試伺服器
python -c "import your_server_module; print('OK')"

# 檢查導入錯誤
python -m your_server_module 2>&1 | head -20

# 確認已安裝 MCP SDK
pip show mcp
```

### 情景 2：工具未出現

**症狀：** Tools 標籤顯示空清單

**可能原因：**
1. 伺服器初始化時未註冊工具
2. 伺服器啟動後崩潰
3. `tools/list` 處理程序回傳空陣列

**除錯步驟：**
1. 查看訊息紀錄中 `tools/list` 回應
2. 在工具註冊程式碼加入日誌
3. 確認有 `@mcp.tool()` 裝飾器（Python）

### 情景 3：工具回傳錯誤

**症狀：** 工具呼叫回傳錯誤回應

**除錯方式：**
1. 仔細閱讀錯誤訊息
2. 檢查參數型別是否符合規格
3. 加入 try/catch 並顯示詳細錯誤訊息
4. 查看伺服器日誌的堆疊追蹤

**範例改進的錯誤處理：**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # 這裡是工具邏輯
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### 情景 4：資源內容為空

**症狀：** 資源有回傳但內容為空或 null

**檢查清單：**
1. ✅ 檔案路徑或 URI 是否正確
2. ✅ 伺服器是否有權限讀取該資源
3. ✅ 資源內容是否正確回傳

---

## 進階 Inspector 功能

### 自訂 headers (SSE)

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### 詳細日誌

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### 記錄工作階段

Inspector 可匯出訊息日誌以供日後分析：
1. 在訊息面板點選 **Export Log**
2. 儲存 JSON 檔案
3. 與團隊成員共用以便除錯

---

## 最佳實務

1. <strong>及早且頻繁測試</strong> — 開發時就使用 Inspector，不要等問題出現才測試
2. <strong>從簡單開始</strong> — 先測試基本連線，再測試複雜工具呼叫
3. <strong>核對參數模式</strong> — 很多錯誤來源於參數類型不符
4. <strong>閱讀錯誤訊息</strong> — MCP 錯誤通常具描述性
5. **保持 Inspector 開啟** — 有助於你開發時及時發現問題

---

## 接下來

你已完成第 3 單元：入門！繼續你的學習：

- [Module 4: Practical Implementation](../../04-PracticalImplementation/README.md)

---

## 附加資源

- [MCP Inspector GitHub Repository](https://github.com/modelcontextprotocol/inspector)
- [MCP Specification - Protocol Messages](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 Specification](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->