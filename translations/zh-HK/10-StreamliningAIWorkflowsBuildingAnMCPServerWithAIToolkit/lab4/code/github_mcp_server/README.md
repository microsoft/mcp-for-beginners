# Weather MCP Server

這是一個使用 Python 實現的範例 MCP Server，提供天氣工具的模擬回應。它可以作為您自己的 MCP Server 的基礎。此範例包含以下功能：

- **天氣工具**：根據指定位置提供模擬的天氣資訊。
- **Git 克隆工具**：將 Git 儲存庫克隆到指定的資料夾。
- **VS Code 開啟工具**：在 VS Code 或 VS Code Insiders 中開啟資料夾。
- **連接到 Agent Builder**：允許您將 MCP Server 連接到 Agent Builder 進行測試和除錯。
- **在 [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 中除錯**：使用 MCP Inspector 對 MCP Server 進行除錯。

## 開始使用 Weather MCP Server 範本

> **先決條件**
>
> 要在本地開發機器上運行 MCP Server，您需要：
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/)（Git 克隆工具所需）
> - [VS Code](https://code.visualstudio.com/) 或 [VS Code Insiders](https://code.visualstudio.com/insiders/)（VS Code 開啟工具所需）
> - （*可選 - 如果您偏好使用 uv*）[uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## 準備環境

有兩種方法可以為此專案設置環境。您可以根據自己的偏好選擇其中一種。

> 注意：在建立虛擬環境後，請重新載入 VS Code 或終端機以確保使用虛擬環境中的 Python。

| 方法 | 步驟 |
| ---- | ---- |
| 使用 `uv` | 1. 建立虛擬環境：`uv venv` <br>2. 執行 VS Code 指令 "***Python: Select Interpreter***"，選擇剛建立的虛擬環境中的 Python <br>3. 安裝依賴項（包括開發依賴項）：`uv pip install -r pyproject.toml --extra dev` |
| 使用 `pip` | 1. 建立虛擬環境：`python -m venv .venv` <br>2. 執行 VS Code 指令 "***Python: Select Interpreter***"，選擇剛建立的虛擬環境中的 Python <br>3. 安裝依賴項（包括開發依賴項）：`pip install -e .[dev]` |

設置環境後，您可以通過 Agent Builder 作為 MCP Client 在本地開發機器上運行伺服器以開始使用：
1. 打開 VS Code 除錯面板。選擇 `Debug in Agent Builder` 或按 `F5` 開始除錯 MCP Server。
2. 使用 AI Toolkit Agent Builder 測試伺服器，使用[此提示](../../../../../../../../../../../open_prompt_builder)。伺服器將自動連接到 Agent Builder。
3. 點擊 `Run` 使用提示測試伺服器。

**恭喜您**！您已成功通過 Agent Builder 作為 MCP Client 在本地開發機器上運行 Weather MCP Server。
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## 範本中包含的內容

| 資料夾 / 檔案 | 內容                                     |
| ------------ | ---------------------------------------- |
| `.vscode`    | 用於除錯的 VS Code 檔案                 |
| `.aitk`      | AI Toolkit 的配置檔案                   |
| `src`        | Weather MCP Server 的原始碼             |

## 如何除錯 Weather MCP Server

> 注意：
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) 是一個用於測試和除錯 MCP Server 的視覺化開發工具。
> - 所有除錯模式都支持斷點，您可以在工具實現程式碼中添加斷點。

## 可用工具

### 天氣工具
`get_weather` 工具提供指定位置的模擬天氣資訊。

| 參數 | 類型 | 描述 |
| ---- | ---- | ---- |
| `location` | string | 要獲取天氣的地點（例如城市名稱、州或座標） |

### Git 克隆工具
`git_clone_repo` 工具將 Git 儲存庫克隆到指定資料夾。

| 參數 | 類型 | 描述 |
| ---- | ---- | ---- |
| `repo_url` | string | 要克隆的 Git 儲存庫 URL |
| `target_folder` | string | 儲存庫應克隆到的資料夾路徑 |

工具返回一個 JSON 物件，包含：
- `success`：表示操作是否成功的布林值
- `target_folder` 或 `error`：克隆的儲存庫路徑或錯誤訊息

### VS Code 開啟工具
`open_in_vscode` 工具在 VS Code 或 VS Code Insiders 應用程式中開啟資料夾。

| 參數 | 類型 | 描述 |
| ---- | ---- | ---- |
| `folder_path` | string | 要開啟的資料夾路徑 |
| `use_insiders` | boolean（可選） | 是否使用 VS Code Insiders 而非普通 VS Code |

工具返回一個 JSON 物件，包含：
- `success`：表示操作是否成功的布林值
- `message` 或 `error`：確認訊息或錯誤訊息

| 除錯模式 | 描述 | 除錯步驟 |
| -------- | ---- | -------- |
| Agent Builder | 通過 AI Toolkit 的 Agent Builder 除錯 MCP Server。 | 1. 打開 VS Code 除錯面板。選擇 `Debug in Agent Builder` 並按 `F5` 開始除錯 MCP Server。<br>2. 使用 AI Toolkit Agent Builder 測試伺服器，使用[此提示](../../../../../../../../../../../open_prompt_builder)。伺服器將自動連接到 Agent Builder。<br>3. 點擊 `Run` 使用提示測試伺服器。 |
| MCP Inspector | 使用 MCP Inspector 除錯 MCP Server。 | 1. 安裝 [Node.js](https://nodejs.org/)<br> 2. 設置 Inspector：`cd inspector` && `npm install` <br> 3. 打開 VS Code 除錯面板。選擇 `Debug SSE in Inspector (Edge)` 或 `Debug SSE in Inspector (Chrome)`。按 F5 開始除錯。<br> 4. 當 MCP Inspector 在瀏覽器中啟動時，點擊 `Connect` 按鈕連接此 MCP Server。<br> 5. 然後您可以 `List Tools`，選擇工具，輸入參數，並 `Run Tool` 來除錯您的伺服器程式碼。 |

## 預設端口及自訂

| 除錯模式 | 端口 | 定義 | 自訂 | 注意 |
| -------- | ---- | ---- | ---- | ---- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | 編輯 [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)、[\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) 以更改上述端口。 | N/A |
| MCP Inspector | 3001（伺服器）；5173 和 3000（Inspector） | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | 編輯 [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json)、[tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json)、[\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py)、[mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) 以更改上述端口。 | N/A |

## 意見反饋

如果您對此範本有任何意見或建議，請在 [AI Toolkit GitHub 儲存庫](https://github.com/microsoft/vscode-ai-toolkit/issues) 上提交問題。

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。