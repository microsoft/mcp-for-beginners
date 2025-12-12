<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "999c5e7623c1e2d5e5a07c2feb39eb67",
  "translation_date": "2025-12-11T17:04:02+00:00",
  "source_file": "10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md",
  "language_code": "kn"
}
-->
# ಹವಾಮಾನ MCP ಸರ್ವರ್

ಇದು ಹವಾಮಾನ ಸಾಧನಗಳನ್ನು ನಕಲಿ ಪ್ರತಿಕ್ರಿಯೆಗಳೊಂದಿಗೆ ಅನುಷ್ಠಾನಗೊಳಿಸುವ ಪೈಥಾನ್‌ನಲ್ಲಿ ಒಂದು ಮಾದರಿ MCP ಸರ್ವರ್ ಆಗಿದೆ. ನಿಮ್ಮ ಸ್ವಂತ MCP ಸರ್ವರ್‌ಗೆ ಇದು ಒಂದು ತಳಹದಿಯಾಗಿ ಬಳಸಬಹುದು. ಇದರಲ್ಲಿ ಕೆಳಗಿನ ವೈಶಿಷ್ಟ್ಯಗಳು ಸೇರಿವೆ:

- **ಹವಾಮಾನ ಸಾಧನ**: ನೀಡಲಾದ ಸ್ಥಳದ ಆಧಾರದ ಮೇಲೆ ನಕಲಿ ಹವಾಮಾನ ಮಾಹಿತಿಯನ್ನು ಒದಗಿಸುವ ಸಾಧನ.
- **ಏಜೆಂಟ್ ಬಿಲ್ಡರ್‌ಗೆ ಸಂಪರ್ಕ**: ಪರೀಕ್ಷೆ ಮತ್ತು ಡಿಬಗ್ ಮಾಡಲು MCP ಸರ್ವರ್ ಅನ್ನು ಏಜೆಂಟ್ ಬಿಲ್ಡರ್‌ಗೆ ಸಂಪರ್ಕಿಸುವ ವೈಶಿಷ್ಟ್ಯ.
- **[MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್](https://github.com/modelcontextprotocol/inspector) ನಲ್ಲಿ ಡಿಬಗ್ ಮಾಡುವುದು**: MCP ಸರ್ವರ್ ಅನ್ನು MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬಳಸಿ ಡಿಬಗ್ ಮಾಡಲು ಅವಕಾಶ ನೀಡುವ ವೈಶಿಷ್ಟ್ಯ.

## ಹವಾಮಾನ MCP ಸರ್ವರ್ ಟೆಂಪ್ಲೇಟ್ನೊಂದಿಗೆ ಪ್ರಾರಂಭಿಸಿ

> **ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು**
>
> ನಿಮ್ಮ ಸ್ಥಳೀಯ ಡೆವ್ ಯಂತ್ರದಲ್ಲಿ MCP ಸರ್ವರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಲು, ನಿಮಗೆ ಬೇಕಾಗುವುದು:
>
> - [Python](https://www.python.org/)
> - (*ಐಚ್ಛಿಕ - ನೀವು uv ಅನ್ನು ಇಷ್ಟಪಡಿಸಿದರೆ*) [uv](https://github.com/astral-sh/uv)
> - [Python ಡಿಬಗರ್ ವಿಸ್ತರಣೆ](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## ಪರಿಸರವನ್ನು ಸಿದ್ಧಪಡಿಸಿ

ಈ ಯೋಜನೆಗೆ ಪರಿಸರವನ್ನು ಸಿದ್ಧಪಡಿಸಲು ಎರಡು ವಿಧಾನಗಳಿವೆ. ನಿಮ್ಮ ಇಚ್ಛೆಯ ಪ್ರಕಾರ ಯಾವುದಾದರೂ ಒಂದು ಆಯ್ಕೆ ಮಾಡಬಹುದು.

> ಟಿಪ್ಪಣಿ: ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿದ ನಂತರ, ವರ್ಚುವಲ್ ಪರಿಸರದ ಪೈಥಾನ್ ಬಳಸಲಾಗುತ್ತಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಲು VSCode ಅಥವಾ ಟರ್ಮಿನಲ್ ಅನ್ನು ಮರುಲೋಡ್ ಮಾಡಿ.

| ವಿಧಾನ | ಹಂತಗಳು |
| -------- | ----- |
| `uv` ಬಳಸಿ | 1. ವರ್ಚುವಲ್ ಪರಿಸರ ರಚಿಸಿ: `uv venv` <br>2. VSCode ಕಮಾಂಡ್ "***Python: Select Interpreter***" ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ ಮತ್ತು ರಚಿಸಿದ ವರ್ಚುವಲ್ ಪರಿಸರದ ಪೈಥಾನ್ ಆಯ್ಕೆಮಾಡಿ <br>3. ಅವಲಂಬನೆಗಳನ್ನು (ಡೆವ್ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿ) ಸ್ಥಾಪಿಸಿ: `uv pip install -r pyproject.toml --extra dev` |
| `pip` ಬಳಸಿ | 1. ವರ್ಚುವಲ್ ಪರಿಸರ ರಚಿಸಿ: `python -m venv .venv` <br>2. VSCode ಕಮಾಂಡ್ "***Python: Select Interpreter***" ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ ಮತ್ತು ರಚಿಸಿದ ವರ್ಚುವಲ್ ಪರಿಸರದ ಪೈಥಾನ್ ಆಯ್ಕೆಮಾಡಿ<br>3. ಅವಲಂಬನೆಗಳನ್ನು (ಡೆವ್ ಅವಲಂಬನೆಗಳನ್ನು ಸೇರಿಸಿ) ಸ್ಥಾಪಿಸಿ: `pip install -e .[dev]` |

ಪರಿಸರವನ್ನು ಸಿದ್ಧಪಡಿಸಿದ ನಂತರ, ನೀವು Agent Builder ಮೂಲಕ MCP ಕ್ಲೈಂಟ್ ಆಗಿ ನಿಮ್ಮ ಸ್ಥಳೀಯ ಡೆವ್ ಯಂತ್ರದಲ್ಲಿ ಸರ್ವರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಬಹುದು:
1. VS Code ಡಿಬಗ್ ಪ್ಯಾನೆಲ್ ತೆರೆಯಿರಿ. `Debug in Agent Builder` ಆಯ್ಕೆಮಾಡಿ ಅಥವಾ MCP ಸರ್ವರ್ ಡಿಬಗ್ ಮಾಡಲು `F5` ಒತ್ತಿ.
2. AI Toolkit Agent Builder ಬಳಸಿ [ಈ ಪ್ರಾಂಪ್ಟ್](../../../../../../../../../../../../open_prompt_builder) ಮೂಲಕ ಸರ್ವರ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿ. ಸರ್ವರ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಏಜೆಂಟ್ ಬಿಲ್ಡರ್‌ಗೆ ಸಂಪರ್ಕ ಹೊಂದುತ್ತದೆ.
3. ಪ್ರಾಂಪ್ಟ್ ಬಳಸಿ ಸರ್ವರ್ ಪರೀಕ್ಷಿಸಲು `Run` ಕ್ಲಿಕ್ ಮಾಡಿ.

**ಅಭಿನಂದನೆಗಳು**! ನೀವು ಯಶಸ್ವಿಯಾಗಿ Agent Builder ಮೂಲಕ MCP ಕ್ಲೈಂಟ್ ಆಗಿ ನಿಮ್ಮ ಸ್ಥಳೀಯ ಡೆವ್ ಯಂತ್ರದಲ್ಲಿ ಹವಾಮಾನ MCP ಸರ್ವರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿದ್ದೀರಿ.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## ಟೆಂಪ್ಲೇಟ್ನಲ್ಲಿ ಏನು ಸೇರಿದೆ

| ಫೋಲ್ಡರ್ / ಫೈಲ್| ವಿಷಯಗಳು                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | ಡಿಬಗ್ ಮಾಡಲು VSCode ಫೈಲ್‌ಗಳು                   |
| `.aitk`      | AI Toolkit ಗಾಗಿ ಸಂರಚನೆಗಳು                |
| `src`        | ಹವಾಮಾನ MCP ಸರ್ವರ್‌ನ ಮೂಲ ಕೋಡ್   |

## ಹವಾಮಾನ MCP ಸರ್ವರ್ ಅನ್ನು ಹೇಗೆ ಡಿಬಗ್ ಮಾಡುವುದು

> ಟಿಪ್ಪಣಿಗಳು:
> - [MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್](https://github.com/modelcontextprotocol/inspector) MCP ಸರ್ವರ್‌ಗಳನ್ನು ಪರೀಕ್ಷಿಸಲು ಮತ್ತು ಡಿಬಗ್ ಮಾಡಲು ದೃಶ್ಯ ಡೆವಲಪರ್ ಸಾಧನ.
> - ಎಲ್ಲಾ ಡಿಬಗ್ ಮೋಡ್‌ಗಳು ಬ್ರೇಕ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಬೆಂಬಲಿಸುತ್ತವೆ, ಆದ್ದರಿಂದ ನೀವು ಸಾಧನ ಅನುಷ್ಠಾನ ಕೋಡ್‌ಗೆ ಬ್ರೇಕ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಸೇರಿಸಬಹುದು.

| ಡಿಬಗ್ ಮೋಡ್ | ವಿವರಣೆ | ಡಿಬಗ್ ಮಾಡಲು ಹಂತಗಳು |
| ---------- | ----------- | --------------- |
| ಏಜೆಂಟ್ ಬಿಲ್ಡರ್ | AI Toolkit ಮೂಲಕ ಏಜೆಂಟ್ ಬಿಲ್ಡರ್‌ನಲ್ಲಿ MCP ಸರ್ವರ್ ಅನ್ನು ಡಿಬಗ್ ಮಾಡಿ. | 1. VS Code ಡಿಬಗ್ ಪ್ಯಾನೆಲ್ ತೆರೆಯಿರಿ. `Debug in Agent Builder` ಆಯ್ಕೆಮಾಡಿ ಮತ್ತು MCP ಸರ್ವರ್ ಡಿಬಗ್ ಮಾಡಲು `F5` ಒತ್ತಿ.<br>2. AI Toolkit Agent Builder ಬಳಸಿ [ಈ ಪ್ರಾಂಪ್ಟ್](../../../../../../../../../../../../open_prompt_builder) ಮೂಲಕ ಸರ್ವರ್ ಪರೀಕ್ಷಿಸಿ. ಸರ್ವರ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಏಜೆಂಟ್ ಬಿಲ್ಡರ್‌ಗೆ ಸಂಪರ್ಕ ಹೊಂದುತ್ತದೆ.<br>3. ಪ್ರಾಂಪ್ಟ್ ಬಳಸಿ ಸರ್ವರ್ ಪರೀಕ್ಷಿಸಲು `Run` ಕ್ಲಿಕ್ ಮಾಡಿ. |
| MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ | MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬಳಸಿ MCP ಸರ್ವರ್ ಅನ್ನು ಡಿಬಗ್ ಮಾಡಿ. | 1. [Node.js](https://nodejs.org/) ಅನ್ನು ಸ್ಥಾಪಿಸಿ<br> 2. ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಸಿದ್ಧಪಡಿಸಿ: `cd inspector` && `npm install` <br> 3. VS Code ಡಿಬಗ್ ಪ್ಯಾನೆಲ್ ತೆರೆಯಿರಿ. `Debug SSE in Inspector (Edge)` ಅಥವಾ `Debug SSE in Inspector (Chrome)` ಆಯ್ಕೆಮಾಡಿ. ಡಿಬಗ್ ಪ್ರಾರಂಭಿಸಲು F5 ಒತ್ತಿ.<br> 4. MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಪ್ರಾರಂಭವಾದಾಗ, ಈ MCP ಸರ್ವರ್‌ಗೆ ಸಂಪರ್ಕಿಸಲು `Connect` ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ.<br> 5. ನಂತರ ನೀವು `List Tools` ಮಾಡಿ, ಸಾಧನ ಆಯ್ಕೆಮಾಡಿ, ಪ್ಯಾರಾಮೀಟರ್‌ಗಳನ್ನು ನಮೂದಿಸಿ ಮತ್ತು `Run Tool` ಮೂಲಕ ನಿಮ್ಮ ಸರ್ವರ್ ಕೋಡ್ ಅನ್ನು ಡಿಬಗ್ ಮಾಡಬಹುದು.<br> |

## ಡೀಫಾಲ್ಟ್ ಪೋರ್ಟ್‌ಗಳು ಮತ್ತು ಕಸ್ಟಮೈಜೇಶನ್‌ಗಳು

| ಡಿಬಗ್ ಮೋಡ್ | ಪೋರ್ಟ್‌ಗಳು | ವ್ಯಾಖ್ಯಾನಗಳು | ಕಸ್ಟಮೈಜೇಶನ್‌ಗಳು | ಟಿಪ್ಪಣಿ |
| ---------- | ----- | ------------ | -------------- |-------------- |
| ಏಜೆಂಟ್ ಬಿಲ್ಡರ್ | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | ಮೇಲಿನ ಪೋರ್ಟ್‌ಗಳನ್ನು ಬದಲಾಯಿಸಲು [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) ಸಂಪಾದಿಸಿ. | ಅನ್ವಯಿಸುವುದಿಲ್ಲ |
| MCP ಇನ್ಸ್‌ಪೆಕ್ಟರ್ | 3001 (ಸರ್ವರ್); 5173 ಮತ್ತು 3000 (ಇನ್ಸ್‌ಪೆಕ್ಟರ್) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | ಮೇಲಿನ ಪೋರ್ಟ್‌ಗಳನ್ನು ಬದಲಾಯಿಸಲು [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) ಸಂಪಾದಿಸಿ.| ಅನ್ವಯಿಸುವುದಿಲ್ಲ |

## ಪ್ರತಿಕ್ರಿಯೆ

ನೀವು ಈ ಟೆಂಪ್ಲೇಟಿಗೆ ಯಾವುದೇ ಪ್ರತಿಕ್ರಿಯೆ ಅಥವಾ ಸಲಹೆಗಳಿದ್ದರೆ, ದಯವಿಟ್ಟು [AI Toolkit GitHub ರೆಪೊ](https://github.com/microsoft/vscode-ai-toolkit/issues) ನಲ್ಲಿ ಒಂದು ಇಶ್ಯೂ ತೆರೆಯಿರಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->