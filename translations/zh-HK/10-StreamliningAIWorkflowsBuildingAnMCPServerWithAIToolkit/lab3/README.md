# 🔧 模組 3：使用 Microsoft Foundry Toolkit 進行進階 MCP 開發

> [!NOTE]
> 本實驗中的 Inspector URL 使用舊版 `/sse` 端點，並鎖定 MCP SDK `1.9.3` 與 Inspector `0.14.0` 依賴套件。這些並非最新的 `2026-07-28` Streamable HTTP 範例。
> 
> 

![Duration](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![Microsoft Foundry Toolkit](https://img.shields.io/badge/Microsoft_Foundry_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 學習目標

完成本實驗後，您將能夠：

- ✅ 使用 Microsoft Foundry Toolkit 建立自訂 MCP 伺服器
- ✅ 配置並使用最新的 MCP Python SDK （v1.9.3）
- ✅ 設置並運用 MCP Inspector 進行除錯
- ✅ 在 Agent Builder 與 Inspector 環境中除錯 MCP 伺服器
- ✅ 了解進階 MCP 伺服器開發工作流程

## 📋 先決條件

- 完成實驗 2（MCP 基礎）
- 已安裝 Microsoft Foundry Toolkit 擴充功能的 VS Code
- Python 3.10+ 環境
- 用於 Inspector 設定的 Node.js 與 npm

## 🏗️ 你將建構的內容

在本實驗中，您將建立一個 **天氣 MCP 伺服器**，展示：
- 自訂 MCP 伺服器實作
- 與 Microsoft Foundry Toolkit Agent Builder 整合
- 專業除錯工作流程
- 現代 MCP SDK 使用模式

---

## 🔧 核心元件總覽

### 🐍 MCP Python SDK
Model Context Protocol Python SDK 提供建立自訂 MCP 伺服器的基礎。您將使用增強除錯功能的 1.9.3 版本。

### 🔍 MCP Inspector
一款強大的除錯工具，提供：
- 即時伺服器監控
- 工具執行視覺化
- 網路請求/回應檢查
- 互動式測試環境

---

## 📖 一步步實作

### 步驟 1：在 Agent Builder 建立 WeatherAgent

1. **透過 Microsoft Foundry Toolkit 擴充功能，於 VS Code 啟動 Agent Builder**
2. <strong>建立新的代理人</strong>，設定如下：
   - 代理人名稱：`WeatherAgent`

![Agent Creation](../../../../translated_images/zh-HK/Agent.c9c33f6a412b4cde.webp)

### 步驟 2：初始化 MCP 伺服器專案

1. **在 Agent Builder 中，前往 Tools → Add Tool**
2. **從可選項目中選擇「MCP Server」**
3. **選擇「Create A new MCP Server」**
4. **選擇 `python-weather` 範本**
5. **設定你的伺服器名稱：** `weather_mcp`

![Python Template Selection](../../../../translated_images/zh-HK/Pythontemplate.9d0a2913c6491500.webp)

### 步驟 3：打開並檢查專案

1. **在 VS Code 打開產生的專案**
2. **檢查專案結構：**
   ```
   weather_mcp/
   ├── src/
   │   ├── __init__.py
   │   └── server.py
   ├── inspector/
   │   ├── package.json
   │   └── package-lock.json
   ├── .vscode/
   │   ├── launch.json
   │   └── tasks.json
   ├── pyproject.toml
   └── README.md
   ```

### 步驟 4：升級至最新 MCP SDK

> **🔍 為什麼要升級？** 我們希望使用最新的 MCP SDK（v1.9.3）及 Inspector 服務（0.14.0），以獲得更強的功能與更佳的除錯能力。

#### 4a. 更新 Python 依賴套件

**編輯 `pyproject.toml`：** 更新 [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)


#### 4b. 更新 Inspector 配置

**編輯 `inspector/package.json`：** 更新 [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. 更新 Inspector 依賴

**編輯 `inspector/package-lock.json`：** 更新 [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 注意：** 此檔案包含完整依賴定義，下方僅示範主要結構 - 完整內容可確保依賴關係正確解析。


> **⚡ 完整套件鎖定檔：** 完整的 package-lock.json 約有 3000 行依賴定義，上述僅顯示重點結構 - 請使用提供的檔案以完整解析依賴。

### 步驟 5：配置 VS Code 除錯

*注意：請將指定路徑中的檔案複製替換對應本地檔案*

#### 5a. 更新啟動配置

**編輯 `.vscode/launch.json`：**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to Local MCP",
      "type": "debugpy",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 5678
      },
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen",
      "postDebugTask": "Terminate All Tasks"
    },
    {
      "name": "Launch Inspector (Edge)",
      "type": "msedge",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    },
    {
      "name": "Launch Inspector (Chrome)",
      "type": "chrome",
      "request": "launch",
      "url": "http://localhost:6274?timeout=60000&serverUrl=http://localhost:3001/sse#tools",
      "cascadeTerminateToConfigurations": [
        "Attach to Local MCP"
      ],
      "presentation": {
        "hidden": true
      },
      "internalConsoleOptions": "neverOpen"
    }
  ],
  "compounds": [
    {
      "name": "Debug in Agent Builder",
      "configurations": [
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Open Agent Builder",
    },
    {
      "name": "Debug in Inspector (Edge)",
      "configurations": [
        "Launch Inspector (Edge)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    },
    {
      "name": "Debug in Inspector (Chrome)",
      "configurations": [
        "Launch Inspector (Chrome)",
        "Attach to Local MCP"
      ],
      "preLaunchTask": "Start MCP Inspector",
      "stopAll": true
    }
  ]
}
```

**編輯 `.vscode/tasks.json`：**

```
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Start MCP Server",
      "type": "shell",
      "command": "python -m debugpy --listen 127.0.0.1:5678 src/__init__.py sse",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}",
        "env": {
          "PORT": "3001"
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": ".*",
          "endsPattern": "Application startup complete|running"
        }
      }
    },
    {
      "label": "Start MCP Inspector",
      "type": "shell",
      "command": "npm run dev:inspector",
      "isBackground": true,
      "options": {
        "cwd": "${workspaceFolder}/inspector",
        "env": {
          "CLIENT_PORT": "6274",
          "SERVER_PORT": "6277",
        }
      },
      "problemMatcher": {
        "pattern": [
          {
            "regexp": "^.*$",
            "file": 0,
            "location": 1,
            "message": 2
          }
        ],
        "background": {
          "activeOnStart": true,
          "beginsPattern": "Starting MCP inspector",
          "endsPattern": "Proxy server listening on port"
        }
      },
      "dependsOn": [
        "Start MCP Server"
      ]
    },
    {
      "label": "Open Agent Builder",
      "type": "shell",
      "command": "echo ${input:openAgentBuilder}",
      "presentation": {
        "reveal": "never"
      },
      "dependsOn": [
        "Start MCP Server"
      ],
    },
    {
      "label": "Terminate All Tasks",
      "command": "echo ${input:terminate}",
      "type": "shell",
      "problemMatcher": []
    }
  ],
  "inputs": [
    {
      "id": "openAgentBuilder",
      "type": "command",
      "command": "ai-mlstudio.agentBuilder",
      "args": {
        "initialMCPs": [ "local-server-weather_mcp" ],
        "triggeredFrom": "vsc-tasks"
      }
    },
    {
      "id": "terminate",
      "type": "command",
      "command": "workbench.action.tasks.terminate",
      "args": "terminateAll"
    }
  ]
}
```


---

## 🚀 執行並測試您的 MCP 伺服器

### 步驟 6：安裝依賴

進行配置更改後，執行以下指令：

**安裝 Python 依賴：**
```bash
uv sync
```

**安裝 Inspector 依賴：**
```bash
cd inspector
npm install
```

### 步驟 7：透過 Agent Builder 除錯

1. **按 F5** 或使用 **「Debug in Agent Builder」** 配置
2. <strong>從除錯面板中選擇複合配置</strong>
3. **等待伺服器啟動及 Agent Builder 開啟**
4. **使用自然語言查詢測試您的天氣 MCP 伺服器**

輸入提示如下

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Debug Result](../../../../translated_images/zh-HK/Result.6ac570f7d2b1d538.webp)

### 步驟 8：透過 MCP Inspector 除錯

1. **使用「Debug in Inspector」配置（Edge 或 Chrome）**
2. **開啟 Inspector 介面，網址為 `http://localhost:6274`**
3. **探索互動式測試環境：**
   - 檢視可用工具
   - 測試工具執行
   - 監控網路請求
   - 除錯伺服器回應

![MCP Inspector Interface](../../../../translated_images/zh-HK/Inspector.5672415cd02fe873.webp)

---

## 🎯 主要學習成果

完成本實驗後，您已：

- [x] **使用 Microsoft Foundry Toolkit 範本建立自訂 MCP 伺服器**
- [x] **升級至最新 MCP SDK** (v1.9.3) 以增強功能
- [x] **配置 Agent Builder 與 Inspector 之專業除錯工作流程**
- [x] **設置 MCP Inspector 進行互動式伺服器測試**
- [x] **掌握 VS Code MCP 開發除錯配置**

## 🔧 探索的高級功能

| 功能 | 說明 | 使用案例 |
|---------|-------------|----------|
| **MCP Python SDK v1.9.3** | 最新協定實現 | 現代伺服器開發 |
| **MCP Inspector 0.14.0** | 互動除錯工具 | 即時伺服器測試 |
| **VS Code 除錯** | 整合開發環境 | 專業除錯工作流程 |
| **Agent Builder 整合** | 直通 Microsoft Foundry Toolkit 連結 | 端對端代理人測試 |

## 📚 附加資源

- [MCP Python SDK 文件](https://modelcontextprotocol.io/docs/sdk/python)
- [Microsoft Foundry Toolkit 擴充指南](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [VS Code 除錯文件](https://code.visualstudio.com/docs/editor/debugging)
- [Model Context Protocol 規範](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 恭喜！** 您已成功完成實驗 3，現在可以使用專業開發工作流程來建立、除錯與部署自訂 MCP 伺服器。

### 🔜 繼續至下一模組

準備將您的 MCP 技能應用於真實開發流程？請繼續閱讀 **[模組 4：實務 MCP 開發 - 自訂 GitHub 複製伺服器](../lab4/README.md)**，您將：
- 建立可投入生產的 MCP 伺服器，自動化 GitHub 倉庫操作
- 透過 MCP 實作 GitHub 倉庫複製功能
- 與 VS Code 及 GitHub Copilot Agent 模式整合自訂 MCP 伺服器
- 在生產環境中測試及部署自訂 MCP 伺服器
- 學習開發者實務工作流程自動化

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->