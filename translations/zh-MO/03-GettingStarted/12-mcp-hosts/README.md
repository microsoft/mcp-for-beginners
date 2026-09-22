# 設置熱門 MCP 主機客戶端

> [!NOTE]
> 指向 `/sse` 的主機配置是 MCP `2025-11-25` 的舊版 HTTP+SSE 範例。對於 MCP `2026-07-28`，請在支援的主機中選擇 Streamable HTTP 並使用伺服器配置的端點。
> MCP `2026-07-28`，請在支援它的主機中選擇 Streamable HTTP 並使用伺服器配置的端點。
> 支援它並使用伺服器配置的端點。

本指南涵蓋如何使用熱門 AI 主機應用程式配置和使用 MCP 伺服器。每個主機都有其自己的配置方式，但設置完成後，均使用標準化的協議與 MCP 伺服器通信。

## 什麼是 MCP 主機？

**MCP 主機** 是可以連接至 MCP 伺服器來擴展其功能的 AI 應用程式。您可以將其視為用戶互動的「前端」，而 MCP 伺服器則提供「後端」工具和數據。

```mermaid
flowchart LR
    User[👤 使用者] --> Host[🖥️ MCP 主機]
    Host --> S1[MCP 伺服器 A]
    Host --> S2[MCP 伺服器 B]
    Host --> S3[MCP 伺服器 C]
    
    subgraph 「熱門主機」
        H1[Claude 桌面版]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## 先決條件

- 需有一台可連接的 MCP 伺服器（參見 [模組 3.1 - 第一台伺服器](../01-first-server/README.md)）
- 已安裝的主機應用程式
- 基本的 JSON 配置文件熟悉度

---

## 1. Claude Desktop

**Claude Desktop** 是 Anthropic 官方桌面應用程式，原生支援 MCP。

### 安裝

1. 從 [claude.ai/download](https://claude.ai/download) 下載 Claude Desktop
2. 安裝並使用您的 Anthropic 帳號登入

### 配置

Claude Desktop 使用 JSON 配置文件來定義 MCP 伺服器。

**配置文件位置：**
- **macOS**：`~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**：`%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**：`~/.config/Claude/claude_desktop_config.json`

**配置範例：**

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
| `command` | 要執行的可執行檔 | `"python"`, `"node"`, `"npx"` |
| `args` | 命令列參數 | `["-m", "my_server"]` |
| `env` | 環境變數 | `{"API_KEY": "xxx"}` |
| `cwd` | 工作目錄 | `"/path/to/server"` |

### 測試您的設定

1. 儲存配置文件
2. 完全重新啟動 Claude Desktop（退出並重新開啟）
3. 開啟新對話
4. 檢查是否出現 🔌 圖標表示伺服器已連接
5. 嘗試讓 Claude 使用其中一個工具

### Claude Desktop 疑難排解

**伺服器未顯示：**
- 使用 JSON 驗證器檢查配置文件語法
- 確認命令路徑正確
- 查看 Claude Desktop 日誌：幫助 → 顯示日誌

**啟動時伺服器崩潰：**
- 先在終端機手動測試伺服器
- 檢查環境變數是否正確設置
- 確保所有依賴項均已安裝

---

## 2. VS Code 與 GitHub Copilot

VS Code 透過 GitHub Copilot Chat 擴充功能支援 MCP。

### 先決條件

1. 已安裝 VS Code 1.99+
2. 已安裝 GitHub Copilot 擴充功能
3. 已安裝 GitHub Copilot Chat 擴充功能

### 配置

VS Code 使用工作區或使用者設定中的 `.vscode/mcp.json`。

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

<strong>使用者設定</strong>（`settings.json`）：

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

### 在 VS Code 使用 MCP

1. 開啟 Copilot Chat 面板（Ctrl+Shift+I / Cmd+Shift+I）
2. 輸入 `@` 查看可用的 MCP 工具
3. 使用自然語言調用工具：「使用計算器計算 25 * 48」

### VS Code 疑難排解

**MCP 伺服器無法載入：**
- 檢查輸出面板 → 「MCP」的錯誤日誌
- 重新載入視窗：Ctrl+Shift+P → 「開發者：重新載入視窗」
- 確認伺服器能獨立運行

---

## 3. Cursor

**Cursor** 是一款以 AI 為主的程式碼編輯器，內建 MCP 支援。

### 安裝

1. 從 [cursor.sh](https://cursor.sh) 下載 Cursor
2. 安裝並登入

### 配置

Cursor 使用與 Claude Desktop 類似的配置格式。

**配置文件位置：**
- **macOS**：`~/.cursor/mcp.json`
- **Windows**：`%USERPROFILE%\.cursor\mcp.json`
- **Linux**：`~/.cursor/mcp.json`

**配置範例：**

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

### 在 Cursor 使用 MCP

1. 開啟 Cursor 的 AI 聊天（Ctrl+L / Cmd+L）
2. MCP 工具會自動出現在建議中
3. 讓 AI 使用連接的伺服器執行任務

---

## 4. Cline（終端機）

**Cline** 是一款基於終端機的 MCP 客戶端，非常適合命令行工作流程。

### 安裝

```bash
npm install -g @anthropic/cline
```

### 配置

Cline 使用環境變數和命令列參數配置。

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
# 開始一個互動環節
cline

# 使用MCP嘅單一查詢
cline "Calculate the square root of 144 using the calculator"

# 列出可用嘅工具
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** 是另一款支援 MCP 的 AI 驅動程式碼編輯器。

### 安裝

1. 從 [codeium.com/windsurf](https://codeium.com/windsurf) 下載 Windsurf
2. 安裝並建立帳號

### 配置

Windsurf 配置透過設定 UI 管理：

1. 開啟設定（Ctrl+, / Cmd+,）
2. 搜尋「MCP」
3. 點擊「在 settings.json 編輯」

**配置範例：**

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

**stdio**（標準輸入/輸出）：最適合主機本地啟動的伺服器
**SSE/HTTP**：最適合遠端伺服器或多客戶端共用的伺服器

---

## 常見疑難排解

### 伺服器無法啟動

1. **先手動測試伺服器：**
   ```bash
   # 用於 Python
   python -m your_server_module
   
   # 用於 Node.js
   node /path/to/server/index.js
   ```

2. **檢查命令路徑：**
   - 儘可能使用絕對路徑
   - 確認可執行檔已在您的 PATH 中

3. **確認依賴：**
   ```bash
   # Python
   pip list | grep mcp
   
   # Node.js
   npm list @modelcontextprotocol/sdk
   ```

### 伺服器已連接但工具無法使用

1. <strong>檢查伺服器日誌</strong> - 多數主機提供日誌功能
2. <strong>確認工具註冊</strong> - 使用 MCP Inspector 測試
3. <strong>檢查權限</strong> - 部分工具需要檔案/網路存取權限

### 環境變數未傳遞

- 某些主機會淨化環境變數
- 明確使用 `env` 配置欄位
- 避免在配置文件中放置敏感資料（使用秘密管理）

---

## 安全最佳實踐

1. **切勿將 API 金鑰提交到配置文件**
2. <strong>將敏感資料放在環境變數中</strong>
3. <strong>限制伺服器權限於必要範圍</strong>
4. <strong>授權系統存取前先審核伺服器程式碼</strong>
5. <strong>對檔案系統及網路存取使用允許清單</strong>

---

## 接下來的步驟

- [3.13 - 使用 MCP Inspector 除錯](../13-mcp-inspector/README.md)
- [3.1 - 建立您的第一個 MCP 伺服器](../01-first-server/README.md)
- [模組 5 - 進階主題](../../05-AdvancedTopics/README.md)

---

## 其他資源

- [Claude Desktop MCP 文件](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP 擴充功能](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP 規範 - 傳輸](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [官方 MCP 伺服器登錄](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->