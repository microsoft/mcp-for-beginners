# Weather MCP Server

ਇਹ Python ਵਿੱਚ ਇੱਕ ਨਮੂਨਾ MCP Server ਹੈ ਜੋ ਮੌਸਮ ਦੇ ਟੂਲਾਂ ਨੂੰ ਮੌਕ ਜਵਾਬਾਂ ਨਾਲ ਲਾਗੂ ਕਰਦਾ ਹੈ। ਇਸਨੂੰ ਆਪਣੇ MCP Server ਲਈ ਇੱਕ ਢਾਂਚਾ ਵਜੋਂ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਹੇਠ ਲਿਖੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਸ਼ਾਮਲ ਹਨ:

- **Weather Tool**: ਇੱਕ ਟੂਲ ਜੋ ਦਿੱਤੇ ਗਏ ਸਥਾਨ ਦੇ ਆਧਾਰ 'ਤੇ ਮੌਸਮ ਦੀ ਮੌਕ ਜਾਣਕਾਰੀ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ।
- **Connect to Agent Builder**: ਇੱਕ ਵਿਸ਼ੇਸ਼ਤਾ ਜੋ ਤੁਹਾਨੂੰ MCP ਸਰਵਰ ਨੂੰ Agent Builder ਨਾਲ ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ ਲਈ ਜੋੜਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ।
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: ਇੱਕ ਵਿਸ਼ੇਸ਼ਤਾ ਜੋ MCP Inspector ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP Server ਨੂੰ ਡੀਬੱਗ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੀ ਹੈ।

## Weather MCP Server ਟੈਮਪਲੇਟ ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰੋ

> **Prerequisites**
>
> ਆਪਣੇ ਲੋਕਲ ਡਿਵ ਮਸ਼ੀਨ 'ਤੇ MCP Server ਚਲਾਉਣ ਲਈ, ਤੁਹਾਨੂੰ ਲੋੜ ਹੋਵੇਗੀ:
>
> - [Python](https://www.python.org/)
> - (*ਵਿਕਲਪਿਕ - ਜੇ ਤੁਸੀਂ uv ਪਸੰਦ ਕਰਦੇ ਹੋ*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## ਵਾਤਾਵਰਣ ਤਿਆਰ ਕਰੋ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਲਈ ਵਾਤਾਵਰਣ ਸੈੱਟਅਪ ਕਰਨ ਦੇ ਦੋ ਤਰੀਕੇ ਹਨ। ਤੁਸੀਂ ਆਪਣੀ ਪਸੰਦ ਅਨੁਸਾਰ ਕੋਈ ਵੀ ਇੱਕ ਚੁਣ ਸਕਦੇ ਹੋ।

> Note: ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਉਣ ਤੋਂ ਬਾਅਦ ਇਹ ਯਕੀਨੀ ਬਣਾਉਣ ਲਈ VSCode ਜਾਂ ਟਰਮੀਨਲ ਨੂੰ ਰੀਲੋਡ ਕਰੋ ਕਿ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਦਾ Python ਵਰਤਿਆ ਜਾ ਰਿਹਾ ਹੈ।

| ਤਰੀਕਾ | ਕਦਮ |
| -------- | ----- |
| `uv` ਦੀ ਵਰਤੋਂ ਕਰਕੇ | 1. ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ: `uv venv` <br>2. VSCode ਕਮਾਂਡ "***Python: Select Interpreter***" ਚਲਾਓ ਅਤੇ ਬਣਾਏ ਗਏ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਤੋਂ Python ਚੁਣੋ <br>3. ਡਿਪੈਂਡੈਂਸੀਜ਼ (ਡਿਵ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਸਮੇਤ) ਇੰਸਟਾਲ ਕਰੋ: `uv pip install -r pyproject.toml --extra dev` |
| `pip` ਦੀ ਵਰਤੋਂ ਕਰਕੇ | 1. ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ: `python -m venv .venv` <br>2. VSCode ਕਮਾਂਡ "***Python: Select Interpreter***" ਚਲਾਓ ਅਤੇ ਬਣਾਏ ਗਏ ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਤੋਂ Python ਚੁਣੋ<br>3. ਡਿਪੈਂਡੈਂਸੀਜ਼ (ਡਿਵ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਸਮੇਤ) ਇੰਸਟਾਲ ਕਰੋ: `pip install -e .[dev]` |

ਵਾਤਾਵਰਣ ਸੈੱਟਅਪ ਕਰਨ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ Agent Builder ਨੂੰ MCP Client ਵਜੋਂ ਵਰਤ ਕੇ ਆਪਣੇ ਲੋਕਲ ਡਿਵ ਮਸ਼ੀਨ 'ਤੇ ਸਰਵਰ ਚਲਾ ਸਕਦੇ ਹੋ:
1. VS Code ਡੀਬੱਗ ਪੈਨਲ ਖੋਲ੍ਹੋ। `Debug in Agent Builder` ਚੁਣੋ ਜਾਂ MCP ਸਰਵਰ ਡੀਬੱਗ ਕਰਨ ਲਈ `F5` ਦਬਾਓ।
2. AI Toolkit Agent Builder ਦੀ ਵਰਤੋਂ ਕਰਕੇ [ਇਸ ਪ੍ਰਾਂਪਟ](../../../../../../../../../../open_prompt_builder) ਨਾਲ ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰੋ। ਸਰਵਰ ਆਪਣੇ ਆਪ Agent Builder ਨਾਲ ਜੁੜ ਜਾਵੇਗਾ।
3. ਪ੍ਰਾਂਪਟ ਨਾਲ ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ `Run` 'ਤੇ ਕਲਿੱਕ ਕਰੋ।

**ਵਧਾਈਆਂ**! ਤੁਸੀਂ Agent Builder ਨੂੰ MCP Client ਵਜੋਂ ਵਰਤ ਕੇ ਆਪਣੇ ਲੋਕਲ ਡਿਵ ਮਸ਼ੀਨ 'ਤੇ Weather MCP Server ਸਫਲਤਾਪੂਰਵਕ ਚਲਾ ਲਿਆ ਹੈ।  
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## ਟੈਮਪਲੇਟ ਵਿੱਚ ਕੀ ਸ਼ਾਮਲ ਹੈ

| ਫੋਲਡਰ / ਫਾਇਲ | ਸਮੱਗਰੀ                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | ਡੀਬੱਗਿੰਗ ਲਈ VSCode ਫਾਇਲਾਂ                   |
| `.aitk`      | AI Toolkit ਲਈ ਸੰਰਚਨਾਵਾਂ                     |
| `src`        | weather mcp server ਲਈ ਸੋਰਸ ਕੋਡ                |

## Weather MCP Server ਨੂੰ ਕਿਵੇਂ ਡੀਬੱਗ ਕਰੀਏ

> ਨੋਟਸ:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) MCP ਸਰਵਰਾਂ ਦੀ ਟੈਸਟਿੰਗ ਅਤੇ ਡੀਬੱਗਿੰਗ ਲਈ ਇੱਕ ਵਿਜ਼ੂਅਲ ਡਿਵੈਲਪਰ ਟੂਲ ਹੈ।
> - ਸਾਰੇ ਡੀਬੱਗ ਮੋਡ ਬ੍ਰੇਕਪੌਇੰਟਸ ਨੂੰ ਸਹਿਯੋਗ ਦਿੰਦੇ ਹਨ, ਇਸ ਲਈ ਤੁਸੀਂ ਟੂਲ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ ਕੋਡ ਵਿੱਚ ਬ੍ਰੇਕਪੌਇੰਟਸ ਜੋੜ ਸਕਦੇ ਹੋ।

| ਡੀਬੱਗ ਮੋਡ | ਵੇਰਵਾ | ਡੀਬੱਗ ਕਰਨ ਦੇ ਕਦਮ |
| ---------- | ----------- | --------------- |
| Agent Builder | AI Toolkit ਰਾਹੀਂ Agent Builder ਵਿੱਚ MCP ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰੋ। | 1. VS Code ਡੀਬੱਗ ਪੈਨਲ ਖੋਲ੍ਹੋ। `Debug in Agent Builder` ਚੁਣੋ ਅਤੇ MCP ਸਰਵਰ ਡੀਬੱਗ ਕਰਨ ਲਈ `F5` ਦਬਾਓ।<br>2. AI Toolkit Agent Builder ਦੀ ਵਰਤੋਂ ਕਰਕੇ [ਇਸ ਪ੍ਰਾਂਪਟ](../../../../../../../../../../open_prompt_builder) ਨਾਲ ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰੋ। ਸਰਵਰ ਆਪਣੇ ਆਪ Agent Builder ਨਾਲ ਜੁੜ ਜਾਵੇਗਾ।<br>3. ਪ੍ਰਾਂਪਟ ਨਾਲ ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰਨ ਲਈ `Run` 'ਤੇ ਕਲਿੱਕ ਕਰੋ। |
| MCP Inspector | MCP Inspector ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਸਰਵਰ ਨੂੰ ਡੀਬੱਗ ਕਰੋ। | 1. [Node.js](https://nodejs.org/) ਇੰਸਟਾਲ ਕਰੋ।<br>2. Inspector ਸੈੱਟਅਪ ਕਰੋ: `cd inspector` && `npm install` <br>3. VS Code ਡੀਬੱਗ ਪੈਨਲ ਖੋਲ੍ਹੋ। `Debug SSE in Inspector (Edge)` ਜਾਂ `Debug SSE in Inspector (Chrome)` ਚੁਣੋ। ਡੀਬੱਗਿੰਗ ਸ਼ੁਰੂ ਕਰਨ ਲਈ `F5` ਦਬਾਓ।<br>4. ਜਦੋਂ MCP Inspector ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਲਾਂਚ ਹੋਵੇ, ਤਾਂ ਇਸ MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ `Connect` ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।<br>5. ਫਿਰ ਤੁਸੀਂ `List Tools` ਕਰ ਸਕਦੇ ਹੋ, ਇੱਕ ਟੂਲ ਚੁਣੋ, ਪੈਰਾਮੀਟਰ ਦਿਓ, ਅਤੇ `Run Tool` ਕਰਕੇ ਆਪਣੇ ਸਰਵਰ ਕੋਡ ਨੂੰ ਡੀਬੱਗ ਕਰੋ।<br> |

## ਡੀਫਾਲਟ ਪੋਰਟਸ ਅਤੇ ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ

| ਡੀਬੱਗ ਮੋਡ | ਪੋਰਟਸ | ਪਰਿਭਾਸ਼ਾਵਾਂ | ਕਸਟਮਾਈਜ਼ੇਸ਼ਨ | ਨੋਟ |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | ਉਪਰੋਕਤ ਪੋਰਟਸ ਬਦਲਣ ਲਈ [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) ਸੋਧੋ। | N/A |
| MCP Inspector | 3001 (Server); 5173 ਅਤੇ 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | ਉਪਰੋਕਤ ਪੋਰਟਸ ਬਦਲਣ ਲਈ [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) ਸੋਧੋ। | N/A |

## ਫੀਡਬੈਕ

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਇਸ ਟੈਮਪਲੇਟ ਲਈ ਕੋਈ ਫੀਡਬੈਕ ਜਾਂ ਸੁਝਾਅ ਹਨ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ [AI Toolkit GitHub ਰਿਪੋਜ਼ਟਰੀ](https://github.com/microsoft/vscode-ai-toolkit/issues) 'ਤੇ ਇੱਕ ਇਸ਼ੂ ਖੋਲ੍ਹੋ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਮਰਥਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਉਤਪੰਨ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।