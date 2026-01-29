# Weather MCP Server

ਇਹ ਪਾਇਥਨ ਵਿੱਚ ਇੱਕ ਨਮੂਨਾ MCP ਸਰਵਰ ਹੈ ਜੋ ਮੌਸਮ ਦੇ ਟੂਲਾਂ ਨੂੰ ਮੌਕ ਜਵਾਬਾਂ ਨਾਲ ਲਾਗੂ ਕਰਦਾ ਹੈ। ਇਹ ਤੁਹਾਡੇ ਆਪਣੇ MCP ਸਰਵਰ ਲਈ ਇੱਕ ਢਾਂਚੇ ਵਜੋਂ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਹੇਠ ਲਿਖੇ ਫੀਚਰ ਸ਼ਾਮਲ ਹਨ:

- **Weather Tool**: ਇੱਕ ਟੂਲ ਜੋ ਦਿੱਤੇ ਗਏ ਸਥਾਨ ਦੇ ਅਧਾਰ 'ਤੇ ਮੌਕ ਮੌਸਮ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।
- **Git Clone Tool**: ਇੱਕ ਟੂਲ ਜੋ ਇੱਕ ਗਿਟ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਨਿਰਧਾਰਿਤ ਫੋਲਡਰ ਵਿੱਚ ਕਲੋਨ ਕਰਦਾ ਹੈ।
- **VS Code Open Tool**: ਇੱਕ ਟੂਲ ਜੋ VS Code ਜਾਂ VS Code Insiders ਵਿੱਚ ਫੋਲਡਰ ਖੋਲ੍ਹਦਾ ਹੈ।
- **Agent Builder ਨਾਲ ਕਨੈਕਟ ਕਰੋ**: ਇੱਕ ਫੀਚਰ ਜੋ MCP ਸਰਵਰ ਨੂੰ Agent Builder ਨਾਲ ਟੈਸਟ ਅਤੇ ਡੀਬੱਗ ਕਰਨ ਲਈ ਕਨੈਕਟ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ਵਿੱਚ ਡੀਬੱਗ ਕਰੋ**: ਇੱਕ ਫੀਚਰ ਜੋ MCP ਸਰਵਰ ਨੂੰ MCP Inspector ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਡੀਬੱਗ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

## Weather MCP Server ਟੈਂਪਲੇਟ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋ

> **Prerequisites**
>
> ਆਪਣੇ ਲੋਕਲ ਡਿਵ ਮਸ਼ੀਨ 'ਤੇ MCP ਸਰਵਰ ਚਲਾਉਣ ਲਈ, ਤੁਹਾਨੂੰ ਲੋੜ ਹੋਵੇਗੀ:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (git_clone_repo ਟੂਲ ਲਈ ਲਾਜ਼ਮੀ)
> - [VS Code](https://code.visualstudio.com/) ਜਾਂ [VS Code Insiders](https://code.visualstudio.com/insiders/) (open_in_vscode ਟੂਲ ਲਈ ਲਾਜ਼ਮੀ)
> - (*ਵਿਕਲਪਿਕ - ਜੇ ਤੁਸੀਂ uv ਨੂੰ ਤਰਜੀਹ ਦਿੰਦੇ ਹੋ*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## ਵਾਤਾਵਰਣ ਤਿਆਰ ਕਰੋ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਲਈ ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰਨ ਦੇ ਦੋ ਤਰੀਕੇ ਹਨ। ਤੁਸੀਂ ਆਪਣੀ ਪਸੰਦ ਦੇ ਅਨੁਸਾਰ ਕੋਈ ਵੀ ਚੁਣ ਸਕਦੇ ਹੋ।

> ਨੋਟ: ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਉਣ ਤੋਂ ਬਾਅਦ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਪਾਇਥਨ ਵਰਤਿਆ ਜਾ ਰਿਹਾ ਹੈ, VSCode ਜਾਂ ਟਰਮੀਨਲ ਨੂੰ ਰੀਲੋਡ ਕਰੋ।

| ਤਰੀਕਾ | ਕਦਮ |
| -------- | ----- |
| `uv` ਦੀ ਵਰਤੋਂ | 1. ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ: `uv venv` <br>2. VSCode ਕਮਾਂਡ "***Python: Select Interpreter***" ਚਲਾਓ ਅਤੇ ਬਣਾਏ ਗਏ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਤੋਂ ਪਾਇਥਨ ਚੁਣੋ <br>3. Dependencies (dev dependencies ਸਮੇਤ) ਇੰਸਟਾਲ ਕਰੋ: `uv pip install -r pyproject.toml --extra dev` |
| `pip` ਦੀ ਵਰਤੋਂ | 1. ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ: `python -m venv .venv` <br>2. VSCode ਕਮਾਂਡ "***Python: Select Interpreter***" ਚਲਾਓ ਅਤੇ ਬਣਾਏ ਗਏ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਤੋਂ ਪਾਇਥਨ ਚੁਣੋ <br>3. Dependencies (dev dependencies ਸਮੇਤ) ਇੰਸਟਾਲ ਕਰੋ: `pip install -e .[dev]` |

ਵਾਤਾਵਰਣ ਸੈਟਅਪ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਆਪਣੇ ਲੋਕਲ ਡਿਵ ਮਸ਼ੀਨ 'ਤੇ Agent Builder ਦੇ ਜ਼ਰੀਏ MCP Client ਵਜੋਂ ਸਰਵਰ ਚਲਾ ਸਕਦੇ ਹੋ:
1. VS Code ਡੀਬੱਗ ਪੈਨਲ ਖੋਲ੍ਹੋ। `Debug in Agent Builder` ਚੁਣੋ ਜਾਂ `F5` ਦਬਾਓ MCP ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰਨ ਲਈ।
2. AI Toolkit Agent Builder ਦੀ ਵਰਤੋਂ ਕਰਕੇ [ਇਸ ਪ੍ਰੋਮਪਟ](../../../../../../../../../../../open_prompt_builder) ਨਾਲ ਸਰਵਰ ਟੈਸਟ ਕਰੋ। ਸਰਵਰ ਆਟੋ-ਕਨੈਕਟ ਹੋ ਜਾਵੇਗਾ Agent Builder ਨਾਲ।
3. `Run` 'ਤੇ ਕਲਿਕ ਕਰੋ ਪ੍ਰੋਮਪਟ ਨਾਲ ਸਰਵਰ ਟੈਸਟ ਕਰਨ ਲਈ।

**ਮੁਬਾਰਕਾਂ**! ਤੁਸੀਂ ਸਫਲਤਾਪੂਰਵਕ Weather MCP Server ਨੂੰ ਆਪਣੇ ਲੋਕਲ ਡਿਵ ਮਸ਼ੀਨ 'ਤੇ Agent Builder ਦੇ ਜ਼ਰੀਏ MCP Client ਵਜੋਂ ਚਲਾ ਲਿਆ ਹੈ।
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## ਟੈਂਪਲੇਟ ਵਿੱਚ ਕੀ ਸ਼ਾਮਲ ਹੈ

| ਫੋਲਡਰ / ਫਾਈਲ | ਸਮੱਗਰੀ |
| ------------ | -------------------------------------------- |
| `.vscode`    | VSCode ਫਾਈਲਾਂ ਡੀਬੱਗਿੰਗ ਲਈ |
| `.aitk`      | AI Toolkit ਲਈ ਕਨਫਿਗਰੇਸ਼ਨ |
| `src`        | Weather MCP Server ਲਈ ਸਰੋਤ ਕੋਡ |

## Weather MCP Server ਨੂੰ ਡੀਬੱਗ ਕਰਨ ਦਾ ਤਰੀਕਾ

> ਨੋਟ:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) ਇੱਕ ਵਿਜ਼ੂਅਲ ਡਿਵੈਲਪਰ ਟੂਲ ਹੈ MCP ਸਰਵਰਾਂ ਨੂੰ ਟੈਸਟ ਅਤੇ ਡੀਬੱਗ ਕਰਨ ਲਈ।
> - ਸਾਰੇ ਡੀਬੱਗ ਮੋਡ ਬ੍ਰੇਕਪੋਇੰਟਸ ਨੂੰ ਸਪੋਰਟ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ ਤੁਸੀਂ ਟੂਲ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਕੋਡ ਵਿੱਚ ਬ੍ਰੇਕਪੋਇੰਟਸ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ।

## ਉਪਲਬਧ ਟੂਲ

### Weather Tool
`get_weather` ਟੂਲ ਦਿੱਤੇ ਗਏ ਸਥਾਨ ਲਈ ਮੌਕ ਮੌਸਮ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।

| ਪੈਰਾਮੀਟਰ | ਕਿਸਮ | ਵੇਰਵਾ |
| --------- | ---- | ----------- |
| `location` | string | ਮੌਸਮ ਜਾਣਨ ਲਈ ਸਥਾਨ (ਜਿਵੇਂ ਸ਼ਹਿਰ ਦਾ ਨਾਮ, ਰਾਜ, ਜਾਂ ਕੋਆਰਡੀਨੇਟਸ) |

### Git Clone Tool
`git_clone_repo` ਟੂਲ ਇੱਕ ਗਿਟ ਰਿਪੋਜ਼ਟਰੀ ਨੂੰ ਨਿਰਧਾਰਿਤ ਫੋਲਡਰ ਵਿੱਚ ਕਲੋਨ ਕਰਦਾ ਹੈ।

| ਪੈਰਾਮੀਟਰ | ਕਿਸਮ | ਵੇਰਵਾ |
| --------- | ---- | ----------- |
| `repo_url` | string | ਕਲੋਨ ਕਰਨ ਲਈ ਗਿਟ ਰਿਪੋਜ਼ਟਰੀ ਦਾ URL |
| `target_folder` | string | ਫੋਲਡਰ ਦਾ ਪਾਥ ਜਿੱਥੇ ਰਿਪੋਜ਼ਟਰੀ ਕਲੋਨ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ |

ਟੂਲ ਇੱਕ JSON ਆਬਜੈਕਟ ਵਾਪਸ ਕਰਦਾ ਹੈ:
- `success`: Boolean ਜੋ ਦੱਸਦਾ ਹੈ ਕਿ ਕਾਰਵਾਈ ਸਫਲ ਹੋਈ ਜਾਂ ਨਹੀਂ
- `target_folder` ਜਾਂ `error`: ਕਲੋਨ ਕੀਤੇ ਗਏ ਰਿਪੋਜ਼ਟਰੀ ਦਾ ਪਾਥ ਜਾਂ ਇੱਕ ਗਲਤੀ ਸੁਨੇਹਾ

### VS Code Open Tool
`open_in_vscode` ਟੂਲ VS Code ਜਾਂ VS Code Insiders ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਫੋਲਡਰ ਖੋਲ੍ਹਦਾ ਹੈ।

| ਪੈਰਾਮੀਟਰ | ਕਿਸਮ | ਵੇਰਵਾ |
| --------- | ---- | ----------- |
| `folder_path` | string | ਫੋਲਡਰ ਦਾ ਪਾਥ ਜੋ ਖੋਲ੍ਹਣਾ ਹੈ |
| `use_insiders` | boolean (ਵਿਕਲਪਿਕ) | ਕੀ ਰੈਗੂਲਰ VS Code ਦੀ ਬਜਾਏ VS Code Insiders ਦੀ ਵਰਤੋਂ ਕਰਨੀ ਹੈ |

ਟੂਲ ਇੱਕ JSON ਆਬਜੈਕਟ ਵਾਪਸ ਕਰਦਾ ਹੈ:
- `success`: Boolean ਜੋ ਦੱਸਦਾ ਹੈ ਕਿ ਕਾਰਵਾਈ ਸਫਲ ਹੋਈ ਜਾਂ ਨਹੀਂ
- `message` ਜਾਂ `error`: ਪੁਸ਼ਟੀ ਸੁਨੇਹਾ ਜਾਂ ਇੱਕ ਗਲਤੀ ਸੁਨੇਹਾ

| ਡੀਬੱਗ ਮੋਡ | ਵੇਰਵਾ | ਡੀਬੱਗ ਕਰਨ ਦੇ ਕਦਮ |
| ---------- | ----------- | --------------- |
| Agent Builder | AI Toolkit ਦੇ ਜ਼ਰੀਏ Agent Builder ਵਿੱਚ MCP ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰੋ। | 1. VS Code ਡੀਬੱਗ ਪੈਨਲ ਖੋਲ੍ਹੋ। `Debug in Agent Builder` ਚੁਣੋ ਅਤੇ `F5` ਦਬਾਓ MCP ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰਨ ਲਈ।<br>2. AI Toolkit Agent Builder ਦੀ ਵਰਤੋਂ ਕਰਕੇ [ਇਸ ਪ੍ਰੋਮਪਟ](../../../../../../../../../../../open_prompt_builder) ਨਾਲ ਸਰਵਰ ਟੈਸਟ ਕਰੋ। ਸਰਵਰ ਆਟੋ-ਕਨੈਕਟ ਹੋ ਜਾਵੇਗਾ Agent Builder ਨਾਲ।<br>3. `Run` 'ਤੇ ਕਲਿਕ ਕਰੋ ਪ੍ਰੋਮਪਟ ਨਾਲ ਸਰਵਰ ਟੈਸਟ ਕਰਨ ਲਈ। |
| MCP Inspector | MCP Inspector ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰੋ। | 1. [Node.js](https://nodejs.org/) ਇੰਸਟਾਲ ਕਰੋ<br> 2. Inspector ਸੈਟਅਪ ਕਰੋ: `cd inspector` && `npm install` <br> 3. VS Code ਡੀਬੱਗ ਪੈਨਲ ਖੋਲ੍ਹੋ। `Debug SSE in Inspector (Edge)` ਜਾਂ `Debug SSE in Inspector (Chrome)` ਚੁਣੋ। F5 ਦਬਾਓ ਡੀਬੱਗ ਕਰਨ ਲਈ।<br> 4. ਜਦੋਂ MCP Inspector ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਲਾਂਚ ਹੁੰਦਾ ਹੈ, `Connect` ਬਟਨ 'ਤੇ ਕਲਿਕ ਕਰੋ ਇਸ MCP ਸਰਵਰ ਨੂੰ ਕਨੈਕਟ ਕਰਨ ਲਈ।<br> 5. ਫਿਰ ਤੁਸੀਂ `List Tools`, ਟੂਲ ਚੁਣੋ, ਪੈਰਾਮੀਟਰ ਇਨਪੁਟ ਕਰੋ, ਅਤੇ `Run Tool` 'ਤੇ ਕਲਿਕ ਕਰੋ ਆਪਣੇ ਸਰਵਰ ਕੋਡ ਨੂੰ ਡੀਬੱਗ ਕਰਨ ਲਈ।<br> |

## ਡੀਫਾਲਟ ਪੋਰਟਸ ਅਤੇ ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ

| ਡੀਬੱਗ ਮੋਡ | ਪੋਰਟਸ | ਪਰਿਭਾਸ਼ਾਵਾਂ | ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ | ਨੋਟ |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) ਨੂੰ ਸੋਧੋ ਉਪਰੋਕਤ ਪੋਰਟਸ ਨੂੰ ਬਦਲਣ ਲਈ। | N/A |
| MCP Inspector | 3001 (Server); 5173 ਅਤੇ 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) ਨੂੰ ਸੋਧੋ ਉਪਰੋਕਤ ਪੋਰਟਸ ਨੂੰ ਬਦਲਣ ਲਈ।| N/A |

## ਫੀਡਬੈਕ

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਇਸ ਟੈਂਪਲੇਟ ਲਈ ਕੋਈ ਫੀਡਬੈਕ ਜਾਂ ਸੁਝਾਅ ਹਨ, ਤਾਂ [AI Toolkit GitHub ਰਿਪੋਜ਼ਟਰੀ](https://github.com/microsoft/vscode-ai-toolkit/issues) 'ਤੇ ਇੱਕ ਇਸ਼ੂ ਖੋਲ੍ਹੋ।

---

**ਅਸਵੀਕਾਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਨਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜੋ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੈ, ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।