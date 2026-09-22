# 使用 MCP Inspector 進行除錯

> [!NOTE]
> 使用 `--sse` 的指令和以 `/sse` 結尾的 URL 是測試舊版 HTTP+SSE
> 傳輸。對於新的 MCP `2026-07-28` 服務器，請使用支援 Streamable HTTP 的 Inspector 版本
> 並選擇該傳輸方式。

**MCP Inspector** 是一個重要的除錯工具，讓您能夠直觀地測試和診斷您的 MCP 服務器，而無需完整的 AI 主機應用程序。可以將其視為 MCP 的「Postman」——它提供一個視覺化界面來發送請求、查看回應，並了解服務器的行為。

## 為什麼使用 MCP Inspector？

在建立 MCP 服務器時，您常會遇到以下挑戰：

- **「我的服務器到底有沒有在運行？」** - Inspector 顯示連線狀態
- **「我的工具有正確註冊嗎？」** - Inspector 列出所有可用工具
- **「回應的格式是什麼？」** - Inspector 顯示完整的 JSON 回應
- **「這個工具為什麼無法使用？」** - Inspector 顯示詳細的錯誤訊息

## 先決條件

- 已安裝 Node.js 18 以上版本
- npm（Node.js 內建）
- 一個可供測試的 MCP 服務器（參見 [Module 3.1 - 第一個服務器](../01-first-server/README.md)）

## 安裝

### 選項 1：用 npx 執行（建議用於快速測試）

```bash
npx @modelcontextprotocol/inspector
```

### 選項 2：全球安裝

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

### 選項 3：加入您的專案

```bash
cd your-mcp-server-project
npm install --save-dev @modelcontextprotocol/inspector
```

加入到 `package.json`：
```json
{
  "scripts": {
    "inspector": "mcp-inspector"
  }
}
```

---

## 連線到您的服務器

### stdio 服務器（本地進程）

對於透過標準輸入/輸出通訊的服務器：

```bash
# Python 伺服器
npx @modelcontextprotocol/inspector python -m your_server_module

# Node.js 伺服器
npx @modelcontextprotocol/inspector node ./build/index.js

# 使用環境變數
OPENAI_API_KEY=xxx npx @modelcontextprotocol/inspector python server.py
```

### SSE/HTTP 服務器（網路）

對於運行為 HTTP 服務的服務器：

1. 先啟動您的服務器：
   ```bash
   python server.py  # 伺服器運行於 http://localhost:8080
   ```

2. 啟動 Inspector 並連線：
   ```bash
   npx @modelcontextprotocol/inspector --sse http://localhost:8080/sse
   ```

---

## Inspector 介面總覽

啟動 Inspector 後，您會看到一個網頁介面（通常在 `http://localhost:5173`）：

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
3. 您會看到所有註冊的工具，包括：
   - 工具名稱
   - 說明
   - 輸入架構（參數）

### 呼叫工具

1. 從清單選擇一個工具
2. 在表單中填入所需參數
3. 點擊 **Run Tool**
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
| 代碼 | 含義 |
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
3. 您會看到：
   - 資源 URI
   - 名稱與說明
   - MIME 類型

### 讀取資源


1. 選擇一個資源
2. 點擊 <strong>讀取資源</strong>
3. 查看返回的內容

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

## 測試提示語

### 列出提示語

1. 點擊 <strong>提示語</strong> 分頁
2. Inspector 呼叫 `prompts/list`
3. 查看可用的提示語範本

### 獲取提示語

1. 選擇一個提示語
2. 填入任何必要的引數
3. 點擊 <strong>取得提示語</strong>
4. 查看呈現出的提示訊息

---

## 訊息日誌分析

訊息日誌顯示所有 MCP 協議訊息。以下筆錄來自一個
舊版 `2025-11-25` 伺服器，包括已移除的 `initialize` 握手流程。一個
`2026-07-28` 伺服器則使用自含請求元資料和 `server/discover`
替代。

```
14:32:01 → {"jsonrpc":"2.0","id":1,"method":"initialize",...}
14:32:01 ← {"jsonrpc":"2.0","id":1,"result":{"protocolVersion":"2025-11-25",...}}
14:32:02 → {"jsonrpc":"2.0","id":2,"method":"tools/list"}
14:32:02 ← {"jsonrpc":"2.0","id":2,"result":{"tools":[...]}}
14:32:05 → {"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"add",...}}
14:32:05 ← {"jsonrpc":"2.0","id":3,"result":{"content":[...]}}
```

### 注意事項

- **請求/回應配對**：每個 `→` 應有對應的 `←`
- <strong>錯誤訊息</strong>：在回應中尋找 `"error"`
- <strong>時間間隔</strong>：較長的空閒可能意味效能問題
- <strong>協議版本</strong>：確保伺服器與用戶端版本一致

---

## VS Code 整合

你可以直接從 VS Code 執行 Inspector：

### 使用 launch.json

新增到 `.vscode/launch.json`：

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

### 使用任務 (Tasks)

新增到 `.vscode/tasks.json`：

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

## 常見除錯情境

### 情境 1：伺服器無法連線

**症狀：** Inspector 顯示「已斷線」或停留在「連線中...」

**檢查清單：**
1. ✅ 伺服器指令是否正確？
2. ✅ 所有相依套件是否安裝？
3. ✅ 伺服器路徑是絕對路徑還是相對目前目錄？
4. ✅ 必要的環境變數是否已設定？

**除錯步驟：**
```bash
# 手動先測試伺服器
python -c "import your_server_module; print('OK')"

# 檢查導入錯誤
python -m your_server_module 2>&1 | head -20

# 確認已安裝 MCP SDK
pip show mcp
```

### 情境 2：工具未顯示

**症狀：** 工具分頁顯示空清單

**可能原因：**
1. 伺服器初始化時未註冊工具
2. 伺服器啟動後當機
3. `tools/list` 處理函式回傳空陣列

**除錯步驟：**
1. 檢查訊息日誌中的 `tools/list` 回應
2. 在工具註冊程式碼中新增紀錄
3. 確認存在 `@mcp.tool()` 裝飾器（Python）

### 情境 3：工具回傳錯誤

**症狀：** 工具呼叫回傳錯誤回應

**除錯方式：**
1. 仔細閱讀錯誤訊息
2. 檢查參數類型是否符合規格
3. 加入 try/catch 捕捉詳細錯誤訊息
4. 查看伺服器日誌中的堆疊追蹤

**優化錯誤處理範例：**

```python
@mcp.tool()
async def my_tool(param1: str, param2: int) -> str:
    try:
        # 工具邏輯在此
        result = process(param1, param2)
        return str(result)
    except ValueError as e:
        raise McpError(f"Invalid parameter: {e}")
    except Exception as e:
        raise McpError(f"Tool failed: {type(e).__name__}: {e}")
```

### 情境 4：資源內容為空

**症狀：** 資源回傳但內容為空或 null

**檢查清單：**
1. ✅ 檔案路徑或 URI 正確
2. ✅ 伺服器有權限讀取該資源
3. ✅ 資源內容確實被正確回傳

---

## 進階 Inspector 功能

### 自訂標頭（SSE）

```bash
npx @modelcontextprotocol/inspector \
  --sse http://localhost:8080/sse \
  --header "Authorization: Bearer your-token"
```

### 詳細日誌紀錄

```bash
DEBUG=mcp* npx @modelcontextprotocol/inspector python server.py
```

### 錄製會話

Inspector 可以匯出訊息日誌以便後續分析：
1. 點擊訊息面板中的 <strong>匯出日誌</strong>
2. 保存 JSON 檔案
3. 與團隊成員分享進行除錯

---


## 最佳實踐

1. <strong>盡早並經常測試</strong> - 在開發過程中使用 Inspector，而不僅僅是在出錯時使用
2. <strong>從簡單開始</strong> - 在進行複雜工具調用前先測試基本連接
3. <strong>檢查結構</strong> - 許多錯誤來自參數類型不匹配
4. <strong>閱讀錯誤訊息</strong> - MCP 錯誤通常描述詳盡
5. **保持 Inspector 開啟** - 它有助於在開發時捕捉問題

---

## 下一步

你已完成模組 3：入門！繼續你的學習：

- [模組 4：實務實現](../../04-PracticalImplementation/README.md)

---

## 額外資源

- [MCP Inspector GitHub 儲存庫](https://github.com/modelcontextprotocol/inspector)
- [MCP 規範 - 協議訊息](https://modelcontextprotocol.io/specification/2026-07-28/)
- [JSON-RPC 2.0 規範](https://www.jsonrpc.org/specification)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->