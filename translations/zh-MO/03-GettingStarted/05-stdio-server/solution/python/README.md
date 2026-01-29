# MCP stdio Server - Python 解決方案

> **⚠️ 重要**：此解決方案已更新為使用 **stdio 傳輸**，根據 MCP 規範 2025-06-18 的建議。原本的 SSE 傳輸已被棄用。

## 概述

此 Python 解決方案展示了如何使用目前的 stdio 傳輸來構建 MCP 伺服器。相比於已棄用的 SSE 方法，stdio 傳輸更簡單、更安全，且性能更佳。

## 先決條件

- Python 3.8 或更新版本
- 建議安裝 `uv` 進行套件管理，請參閱 [說明](https://docs.astral.sh/uv/#highlights)

## 設置指南

### 步驟 1：建立虛擬環境

```bash
python -m venv venv
```

### 步驟 2：啟用虛擬環境

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 步驟 3：安裝依賴項

```bash
pip install mcp
```

## 啟動伺服器

stdio 伺服器的運行方式與舊版 SSE 伺服器不同。它不啟動網頁伺服器，而是通過 stdin/stdout 進行通信：

```bash
python server.py
```

**重要**：伺服器看起來會卡住——這是正常的！它正在等待來自 stdin 的 JSON-RPC 消息。

## 測試伺服器

### 方法 1：使用 MCP Inspector（推薦）

```bash
npx @modelcontextprotocol/inspector python server.py
```

此方法將：
1. 將伺服器作為子進程啟動
2. 打開一個網頁界面進行測試
3. 允許您交互式測試所有伺服器工具

### 方法 2：直接進行 JSON-RPC 測試

您也可以直接發送 JSON-RPC 消息進行測試：

1. 啟動伺服器：`python server.py`
2. 發送 JSON-RPC 消息（範例）：

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. 伺服器將回應可用的工具

### 可用工具

伺服器提供以下工具：

- **add(a, b)**：將兩個數字相加
- **multiply(a, b)**：將兩個數字相乘  
- **get_greeting(name)**：生成個性化問候語
- **get_server_info()**：獲取伺服器資訊

### 使用 Claude Desktop 進行測試

若要在 Claude Desktop 中使用此伺服器，請將以下配置添加到您的 `claude_desktop_config.json`：

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## 與 SSE 的主要差異

**stdio 傳輸（目前使用）：**
- ✅ 設置更簡單——不需要網頁伺服器
- ✅ 更高的安全性——無需 HTTP 端點
- ✅ 基於子進程的通信
- ✅ 通過 stdin/stdout 使用 JSON-RPC
- ✅ 性能更佳

**SSE 傳輸（已棄用）：**
- ❌ 需要設置 HTTP 伺服器
- ❌ 需要網頁框架（Starlette/FastAPI）
- ❌ 路由和會話管理更複雜
- ❌ 額外的安全性考量
- ❌ 已於 MCP 2025-06-18 棄用

## 除錯提示

- 使用 `stderr` 進行日誌記錄（切勿使用 `stdout`）
- 使用 Inspector 進行視覺化除錯
- 確保所有 JSON 消息以換行符分隔
- 確認伺服器啟動時無錯誤

此解決方案遵循最新的 MCP 規範，並展示了 stdio 傳輸實現的最佳實踐。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。