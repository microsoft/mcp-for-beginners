# 設置流行的 MCP 主機客戶端

> [!NOTE]
> 指向 `/sse` 的主機配置是 MCP `2025-11-25` 的舊版 HTTP+SSE 範例。對於 MCP `2026-07-28`，請在支持的主機中選擇可串流的 HTTP，並使用服務器配置的端點。
> 
>

本指南涵蓋如何使用流行的 AI 主機應用程序配置及使用 MCP 服務器。每個主機都有自己的配置方法，但配置完成後，它們均通過標準化協議與 MCP 服務器通信。

## 什麼是 MCP 主機？

**MCP 主機** 是能連接到 MCP 服務器以擴展功能的 AI 應用程序。可以把它想像成用戶互動的「前端」，而 MCP 服務器提供「後端」工具和數據。

```mermaid
flowchart LR
    User[👤 使用者] --> Host[🖥️ MCP 主機]
    Host --> S1[MCP 伺服器 A]
    Host --> S2[MCP 伺服器 B]
    Host --> S3[MCP 伺服器 C]
    
    subgraph "熱門主機"
        H1[Claude 桌面版]
        H2[VS Code]
        H3[Cursor]
        H4[Cline]
        H5[Windsurf]
    end
```

## 前置條件

- 需要連接的 MCP 服務器（參見 [Module 3.1 - 第一個服務器](../01-first-server/README.md)）
- 安裝在系統上的主機應用程式
- 對 JSON 配置文件的基本認識

---

## 1. Claude Desktop

**Claude Desktop** 是 Anthropic 官方桌面應用程式，原生支援 MCP。

### 安裝

1. 從 [claude.ai/download](https://claude.ai/download) 下載 Claude Desktop
2. 安裝並使用你的 Anthropic 帳號登入

### 配置

Claude Desktop 使用 JSON 配置文件定義 MCP 服務器。

**配置文件位置：**
- **macOS**：`~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**：`%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**：`~/.config/Claude/claude_desktop_config.json`

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
| `command` | 執行指令 | `"python"`, `"node"`, `"npx"` |
| `args` | 命令行參數 | `["-m", "my_server"]` |
| `env` | 環境變量 | `{"API_KEY": "xxx"}` |
| `cwd` | 工作目錄 | `"/path/to/server"` |

### 測試你的設置

1. 保存配置文件
2. 完全重啟 Claude Desktop（退出並重新開啟）
3. 打開新對話
4. 查看 🔌 圖示，確認已連接服務器
5. 嘗試請 Claude 使用其中一個工具

### Claude Desktop 疑難排解

**服務器未顯示：**
- 使用 JSON 驗證工具檢查配置文件語法
- 確保命令路徑正確
- 查看 Claude Desktop 日誌：幫助 → 顯示日誌

**服務器啟動時崩潰：**
- 先於終端手動測試服務器運行
- 檢查環境變量是否設定正確
- 確保所有依賴已安裝

---

## 2. VS Code 搭配 GitHub Copilot

VS Code 透過 GitHub Copilot Chat 擴充套件支持 MCP。

### 前置條件

1. 安裝 VS Code 1.99 或以上版本
2. 安裝 GitHub Copilot 擴充套件
3. 安裝 GitHub Copilot Chat 擴充套件

### 配置

VS Code 使用工作區或用戶設定中的 `.vscode/mcp.json`。

<strong>工作區配置</strong> (`.vscode/mcp.json`)：

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

<strong>用戶設定</strong> (`settings.json`)：

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

1. 打開 Copilot Chat 面板 (Ctrl+Shift+I / Cmd+Shift+I)
2. 輸入 `@` 查看可用的 MCP 工具
3. 使用自然語言調用工具：「使用計算機計算 25 * 48」

### VS Code 疑難排解

**MCP 服務器無法加載：**
- 查看輸出面板 → "MCP" 錯誤日誌
- 重新載入視窗：Ctrl+Shift+P → "Developer: Reload Window"
- 先驗證服務器本身能正常運行

---

## 3. Cursor

**Cursor** 是一款以 AI 為主的程式碼編輯器，內建 MCP 支援。

### 安裝

1. 從 [cursor.sh](https://cursor.sh) 下載 Cursor
2. 安裝並登入

### 配置

Cursor 使用類似 Claude Desktop 的配置格式。

**配置文件位置：**
- **macOS**：`~/.cursor/mcp.json`
- **Windows**：`%USERPROFILE%\.cursor\mcp.json`
- **Linux**：`~/.cursor/mcp.json`

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

1. 打開 Cursor 的 AI 聊天 (Ctrl+L / Cmd+L)
2. MCP 工具將自動出現在建議中
3. 請 AI 使用已連接的服務器執行任務

---

## 4. Cline (終端機版)

**Cline** 是基於終端機的 MCP 客戶端，非常適合命令列工作流程。

### 安裝

```bash
npm install -g @anthropic/cline
```

### 配置

Cline 使用環境變量與命令列參數。

**使用環境變量：**

```bash
export ANTHROPIC_API_KEY="your-api-key"
export MCP_SERVER_CALCULATOR="python -m mcp_calculator_server"
```

**使用命令行參數：**

```bash
cline --mcp-server "calculator:python -m mcp_calculator_server" \
      --mcp-server "weather:node /path/to/weather/index.js"
```

<strong>配置文件</strong> (`~/.clinerc`)：

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

# 使用MCP的單一查詢
cline "Calculate the square root of 144 using the calculator"

# 列出可用工具
cline --list-tools
```

---

## 5. Windsurf

**Windsurf** 是另一款支援 MCP 的 AI 驅動程式碼編輯器。

### 安裝

1. 從 [codeium.com/windsurf](https://codeium.com/windsurf) 下載 Windsurf
2. 安裝並建立帳號

### 配置

Windsurf 配置透過設定介面管理：

1. 打開設定 (Ctrl+, / Cmd+,)
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

不同主機支持不同的傳輸機制：

| 主機 | stdio | SSE/HTTP | WebSocket |
|------|-------|----------|-----------|
| Claude Desktop | ✅ | ❌ | ❌ |
| VS Code | ✅ | ✅ | ❌ |
| Cursor | ✅ | ✅ | ❌ |
| Cline | ✅ | ✅ | ❌ |
| Windsurf | ✅ | ✅ | ❌ |

**stdio**（標準輸入/輸出）：最適合由主機啟動的本地服務器
**SSE/HTTP**：最適合遠端服務器或多個客戶端共用的服務器

---

## 常見疑難排解

### 服務器無法啟動

1. **先手動測試服務器：**
   ```bash
   # 適用於 Python
   python -m your_server_module
   
   # 適用於 Node.js
   node /path/to/server/index.js
   ```

2. **檢查命令路徑：**
   - 盡可能使用絕對路徑
   - 確保可執行檔在你的 PATH 中

3. **確認依賴項：**
   ```bash
   # Python（蟒蛇程式語言）
   pip list | grep mcp
   
   # Node.js（節點.js）
   npm list @modelcontextprotocol/sdk
   ```

### 服務器已連接但工具無法使用

1. <strong>查看服務器日誌</strong> - 大多數主機有日誌選項
2. <strong>驗證工具註冊</strong> - 使用 MCP Inspector 測試
3. <strong>檢查權限</strong> - 某些工具需要檔案或網路存取權限

### 環境變量未傳遞

- 有些主機會清理環境變量
- 明確使用 `env` 配置欄位
- 避免在配置文件中放置敏感資料（使用秘密管理）

---

## 安全最佳實踐

1. **切勿將 API 金鑰提交至配置文件**
2. <strong>對敏感資料使用環境變量</strong>
3. <strong>限制服務器權限至必要範圍</strong>
4. <strong>授權前請審閱服務器代碼</strong>
5. <strong>對文件系統與網絡存取採用允許清單</strong>

---

## 下一步是什麼

- [3.13 - 使用 MCP Inspector 進行除錯](../13-mcp-inspector/README.md)
- [3.1 - 創建你的第一個 MCP 服務器](../01-first-server/README.md)
- [模組 5 - 進階主題](../../05-AdvancedTopics/README.md)

---

## 附加資源

- [Claude Desktop MCP 文件](https://docs.anthropic.com/en/docs/claude-desktop/mcp)
- [VS Code MCP 擴充套件](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-mcp)
- [MCP 規範 - 傳輸](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/)
- [官方 MCP 服務器註冊庫](https://github.com/modelcontextprotocol/servers)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->