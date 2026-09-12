# 設定熱門 MCP 主機客戶端

> [!NOTE]
> 指向 `/sse` 的主機設定是 MCP `2025-11-25` 的舊版 HTTP+SSE 範例。對於 MCP `2026-07-28`，請在支援的主機中選擇 Streamable HTTP，並使用伺服器配置的端點。
> MCP `2026-07-28`，請在支援的主機中選擇 Streamable HTTP，並使用伺服器配置的端點。
> 支援的主機中選擇 Streamable HTTP，並使用伺服器配置的端點。

本指南介紹如何使用熱門 AI 主機應用程式配置及使用 MCP 伺服器。每個主機都有其獨特的配置方法，但一旦設定完成，都會使用標準化協議與 MCP 伺服器通訊。

## 什麼是 MCP 主機？

**MCP 主機** 是一個能連接 MCP 伺服器以擴展功能的 AI 應用程式。可將其視為用戶互動的「前端」，而 MCP 伺服器則提供「後端」工具和資料。

```mermaid
flowchart LR
    User[👤 用戶] --> Host[🖥️ MCP 主機]
    Host --> S1[MCP 服務器 A]
    Host --> S2[MCP 服務器 B]
    Host --> S3[MCP 服務器 C]
    
    subgraph 「熱門主機」
        H1[Claude 桌面]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## 前置條件

- 需要一台 MCP 伺服器可供連接（參見 [第 3.1 單元 - 第一次伺服器](../01-first-server/README.md)）
- 系統中已安裝主機應用程式
- 基本熟悉 JSON 配置文件

---

## 1. Claude Desktop

**Claude Desktop** 是 Anthropic 官方桌面應用程式，原生支援 MCP。

### 安裝

1. 從 [claude.ai/download](https://claude.ai/download) 下載 Claude Desktop
2. 安裝並使用你的 Anthropic 帳戶登入

### 配置

Claude Desktop 使用 JSON 配置文件來定義 MCP 伺服器。

**配置文件位置：**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**範例配置：**

```json
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"],
      "env": {
        "PYTHONPATH": "/path/to/your/server"
      }
    },
    "weather": {
      "command": "node",
      "args": ["/path/to/weather-server/build/index.js"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

### 配置選項

| 欄位 | 說明 | 範例 |
|-------|-------------|---------|
| `command` | 執行檔 | `"python"`, `"node"`, `"npx"` |
| `args` | 命令行參數 | `["-m", "my_server"]` |
| `env` | 環境變數 | `{"API_KEY": "xxx"}` |
| `cwd` | 工作目錄 | `"/path/to/server"` |

### 測試你的設定

1. 儲存配置文件
2. 完全重啟 Claude Desktop（退出並重新開啟）
3. 開啟新對話
4. 查看是否出現表示已連接伺服器的 🔌 圖示
5. 嘗試讓 Claude 使用你的工具之一

### Claude Desktop 疑難排解

**伺服器未出現：**
- 使用 JSON 驗證器檢查配置文件語法
- 確保命令路徑正確
- 檢查 Claude Desktop 日誌：幫助 → 顯示日誌

**伺服器啟動時崩潰：**
- 先在終端手動測試你的伺服器
- 檢查環境變數設定是否正確
- 確保所有依賴項已安裝

---

## 2. VS Code 與 GitHub Copilot

VS Code 透過 GitHub Copilot Chat 擴展支援 MCP。

### 前置條件

1. 已安裝 VS Code 1.99+ 版本
2. 已安裝 GitHub Copilot 擴充功能
3. 已安裝 GitHub Copilot Chat 擴充功能

### 配置

VS Code 使用工作區或用戶設定中的 `.vscode/mcp.json`。

<strong>工作區配置</strong>（`.vscode/mcp.json`）：

```json
{
  "servers": {
    "my-calculator": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    },
    "my-database": {
      "type": "sse",
      "url": "http://localhost:8080/sse"
    }
  }
}
```

<strong>用戶設定</strong>（`settings.json`）：

```json
{
  "mcp.servers": {
    "global-server": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-memory"]
    }
  },
  "mcp.enableLogging": true
}
```

### 在 VS Code 中使用 MCP

1. 打開 Copilot Chat 面板（Ctrl+Shift+I / Cmd+Shift+I）
2. 輸入 `@` 查看可用 MCP 工具
3. 使用自然語言呼叫工具：「使用計算機計算 25 * 48」

### VS Code 疑難排解

**MCP 伺服器未載入：**
- 檢查輸出面板 → "MCP" 錯誤日誌
- 重載視窗：Ctrl+Shift+P → "Developer: Reload Window"
- 確認伺服器先能獨立運行

---

## 3. Cursor

**Cursor** 是 AI 優先的程式碼編輯器，內建 MCP 支援。

### 安裝

1. 從 [cursor.sh](https://cursor.sh) 下載 Cursor
2. 安裝並登入

### 配置

Cursor 使用與 Claude Desktop 類似的配置格式。

**配置文件位置：**
- **macOS**: `~/.cursor/mcp.json`
- **Windows**: `%USERPROFILE%\.cursor\mcp.json`
- **Linux**: `~/.cursor/mcp.json`

**範例配置：**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "ghp_your_token_here"
      }
    }
  }
}
```

### 在 Cursor 中使用 MCP

1. 打開 Cursor 的 AI 聊天（Ctrl+L / Cmd+L）
2. MCP 工具會自動出現在建議中
3. 請 AI 使用已連接的伺服器執行任務

---

## 4. Cline（終端機為主）

**Cline** 是以終端機為主的 MCP 客戶端，適合命令列工作流程。

### 安裝

```bash
npm install -g @anthropic/cline
```

### 配置

Cline 使用環境變數和命令行參數。

**使用環境變數：**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**使用命令列參數：**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

<strong>配置文件</strong>（`~/.clinerc`）：

```json
{
  "apiKey": "your-api-key",
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["-m", "mcp_calculator_server"]
    }
  }
}
```

### 使用 Cline

```bash
# 開始互動式會話
cline

# 使用 MCP 的單次查詢
cline "Calculate the square root of 144 using the calculator"

# 列出可用工具
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** 是另一款具 MCP 支援的 AI 驅動程式碼編輯器。

### 安裝

1. 從 [codeium.com/windsurf](https://codeium.com/windsurf) 下載 Windsurf
2. 安裝並建立帳戶

### 配置

Windsurf 的配置透過設定介面管理：

1. 開啟設定（Ctrl+, / Cmd+,）
2. 搜尋 "MCP"
3. 點擊「在 settings.json 編輯」

**範例配置：**

```json
{
  "windsurf.mcp.servers": {
    "my-tools": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {}
    }
  },
  "windsurf.mcp.enabled": true
}
```

---

## 傳輸類型比較

不同主機支援不同的傳輸機制：

| 主機 | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio**（標準輸入/輸出）：最適合由主機啟動的本地伺服器
**SSE/HTTP**：最適合遠端伺服器或多個客戶端共享的伺服器

---

## 常見疑難排解

### 伺服器無法啟動

1. **先手動測試伺服器：**
   ```bash
   # 適用於 Python
   python -m your_server_module
   
   # 適用於 Node.js
   node /path/to/server/index.js
   ```

2. **檢查命令路徑：**
   - 盡可能使用絕對路徑
   - 確保執行檔在 PATH 中

3. **驗證依賴關係：**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### 伺服器已連接但工具無法使用

1. <strong>檢查伺服器日誌</strong> - 大多數主機有日誌選項
2. <strong>驗證工具註冊</strong> - 使用 MCP Inspector 測試
3. <strong>檢查權限</strong> - 部分工具需要文件/網絡訪問權限

### 環境變數未傳遞

- 部分主機會清理環境變數
- 明確使用 `env` 配置欄位
- 避免在配置文件中放入敏感資料（使用密碼管理）

---

## 安全最佳實踐

1. **切勿將 API 金鑰提交到配置文件**
2. **對於敏感資料，使用環境變數**
3. <strong>限制伺服器權限於必要範圍</strong>
4. **授權系統訪問前，審查伺服器代碼**
5. <strong>對文件系統和網絡訪問使用允許清單</strong>

---

## 下一步

- [3.13 - 使用 MCP Inspector 偵錯](../13-mcp-inspector/README.md)
- [3.1 - 建立你的第一個 MCP 伺服器](../01-first-server/README.md)
- [第 5 單元 - 進階主題](../../05-AdvancedTopics/README.md)

---

## 額外資源

- [Claude Desktop MCP 文件](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP 擴展](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP 規範 - 傳輸](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [官方 MCP 伺服器清單](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->