# 🔧 Module 3：使用 AI Toolkit 進階 MCP 開發

![Duration](https://img.shields.io/badge/Duration-20_minutes-blue?style=flat-square)
![AI Toolkit](https://img.shields.io/badge/AI_Toolkit-Required-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=flat-square)
![MCP SDK](https://img.shields.io/badge/MCP_SDK-1.9.3-purple?style=flat-square)
![Inspector](https://img.shields.io/badge/MCP_Inspector-0.14.0-blue?style=flat-square)

## 🎯 學習目標

完成本實驗後，你將能夠：

- ✅ 使用 AI Toolkit 建立自訂 MCP 伺服器
- ✅ 配置並使用最新的 MCP Python SDK（v1.9.3）
- ✅ 設定並運用 MCP Inspector 進行除錯
- ✅ 在 Agent Builder 和 Inspector 環境中除錯 MCP 伺服器
- ✅ 理解進階 MCP 伺服器開發流程

## 📋 先決條件

- 完成 Lab 2（MCP 基礎）
- 已安裝 AI Toolkit 擴充功能的 VS Code
- Python 3.10+ 環境
- 用於 Inspector 設定的 Node.js 和 npm

## 🏗️ 你將會建立的內容

在本實驗中，你將建立一個 **Weather MCP Server**，示範：

- 自訂 MCP 伺服器實作
- 與 AI Toolkit Agent Builder 整合
- 專業除錯流程
- 現代 MCP SDK 使用模式

---

## 🔧 核心元件概覽

### 🐍 MCP Python SDK
Model Context Protocol Python SDK 是建立自訂 MCP 伺服器的基礎。你將使用具備強化除錯功能的 1.9.3 版本。

### 🔍 MCP Inspector
一款強大的除錯工具，提供：

- 即時伺服器監控
- 工具執行視覺化
- 網路請求/回應檢視
- 互動式測試環境

---

## 📖 逐步實作

### 第 1 步：在 Agent Builder 建立 WeatherAgent

1. **透過 AI Toolkit 擴充功能在 VS Code 啟動 Agent Builder**
2. **建立新代理人**，設定如下：
   - 代理人名稱：`WeatherAgent`

![Agent Creation](../../../../translated_images/zh-HK/Agent.c9c33f6a412b4cdedfb973fe5448bdb33de3f400055603111b875610e9b917ab.png)

### 第 2 步：初始化 MCP 伺服器專案

1. **在 Agent Builder 中前往 Tools → Add Tool**
2. **從選項中選擇 "MCP Server"**
3. **選擇 "Create A new MCP Server"**
4. **選擇 `python-weather` 範本**
5. **命名你的伺服器：** `weather_mcp`

![Python Template Selection](../../../../translated_images/zh-HK/Pythontemplate.9d0a2913c6491500bd673430f024dc44676af2808a27b5da9dcc0eb7063adc28.png)

### 第 3 步：開啟並檢視專案

1. **在 VS Code 中開啟產生的專案**
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

### 第 4 步：升級至最新 MCP SDK

> **🔍 為什麼要升級？** 我們希望使用最新的 MCP SDK（v1.9.3）和 Inspector 服務（0.14.0），以獲得更強大的功能和更佳的除錯體驗。

#### 4a. 更新 Python 依賴

**編輯 `pyproject.toml`：** 更新 [./code/weather_mcp/pyproject.toml](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/pyproject.toml)

#### 4b. 更新 Inspector 設定

**編輯 `inspector/package.json`：** 更新 [./code/weather_mcp/inspector/package.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package.json)

#### 4c. 更新 Inspector 依賴

**編輯 `inspector/package-lock.json`：** 更新 [./code/weather_mcp/inspector/package-lock.json](../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/inspector/package-lock.json)

> **📝 注意：** 此檔案包含大量依賴定義，下方為主要結構示意，完整內容確保依賴正確解析。

> **⚡ 完整的 package-lock.json：** 完整檔案約有 3000 行依賴定義，上述為關鍵結構，請使用提供的檔案以確保完整依賴解析。

### 第 5 步：配置 VS Code 除錯

*注意：請將指定路徑的檔案複製並覆蓋對應的本地檔案*

#### 5a. 更新啟動設定

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

## 🚀 執行與測試你的 MCP 伺服器

### 第 6 步：安裝依賴

完成設定變更後，執行以下指令：

**安裝 Python 依賴：**
```bash
uv sync
```

**安裝 Inspector 依賴：**
```bash
cd inspector
npm install
```

### 第 7 步：使用 Agent Builder 除錯

1. **按下 F5** 或使用 **"Debug in Agent Builder"** 設定
2. **從除錯面板選擇複合設定**
3. **等待伺服器啟動並開啟 Agent Builder**
4. **使用自然語言查詢測試你的 weather MCP 伺服器**

輸入提示如下

SYSTEM_PROMPT

```
You are my weather assistant
```

USER_PROMPT

```
How's the weather like in Seattle
```

![Agent Builder Debug Result](../../../../translated_images/zh-HK/Result.6ac570f7d2b1d5389c561ab0566970fe0f13e75bdd976b6a7f0270bc715d07f8.png)

### 第 8 步：使用 MCP Inspector 除錯

1. **使用 "Debug in Inspector" 設定（Edge 或 Chrome）**
2. **開啟 Inspector 介面，網址為 `http://localhost:6274`**
3. **探索互動式測試環境：**
   - 查看可用工具
   - 測試工具執行
   - 監控網路請求
   - 除錯伺服器回應

![MCP Inspector Interface](../../../../translated_images/zh-HK/Inspector.5672415cd02fe8731774586cc0a1083e3275d2f8491602aecc8ac4d61f2c0d57.png)

---

## 🎯 主要學習成果

完成本實驗後，你已經：

- [x] **使用 AI Toolkit 範本建立自訂 MCP 伺服器**
- [x] **升級至最新 MCP SDK**（v1.9.3）以增強功能
- [x] **配置 Agent Builder 與 Inspector 的專業除錯流程**
- [x] **設定 MCP Inspector 進行互動式伺服器測試**
- [x] **掌握 VS Code MCP 開發除錯設定**

## 🔧 探索的進階功能

| 功能 | 說明 | 使用情境 |
|---------|-------------|----------|
| **MCP Python SDK v1.9.3** | 最新協議實作 | 現代伺服器開發 |
| **MCP Inspector 0.14.0** | 互動式除錯工具 | 即時伺服器測試 |
| **VS Code 除錯** | 整合開發環境 | 專業除錯流程 |
| **Agent Builder 整合** | 直接連接 AI Toolkit | 端對端代理人測試 |

## 📚 其他資源

- [MCP Python SDK 文件](https://modelcontextprotocol.io/docs/sdk/python)
- [AI Toolkit 擴充功能指南](https://code.visualstudio.com/docs/ai/ai-toolkit)
- [VS Code 除錯文件](https://code.visualstudio.com/docs/editor/debugging)
- [Model Context Protocol 規範](https://modelcontextprotocol.io/docs/concepts/architecture)

---

**🎉 恭喜！** 你已成功完成 Lab 3，現在可以使用專業開發流程建立、除錯及部署自訂 MCP 伺服器。

### 🔜 繼續下一個模組

準備好將 MCP 技能應用於實務開發流程了嗎？繼續前往 **[Module 4：實務 MCP 開發 - 自訂 GitHub Clone 伺服器](../lab4/README.md)**，你將會：

- 建立可用於生產的 MCP 伺服器，自動化 GitHub 倉庫操作
- 實作透過 MCP 進行 GitHub 倉庫克隆功能
- 將自訂 MCP 伺服器整合至 VS Code 與 GitHub Copilot Agent Mode
- 在生產環境中測試與部署自訂 MCP 伺服器
- 學習開發者實務工作流程自動化

**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。