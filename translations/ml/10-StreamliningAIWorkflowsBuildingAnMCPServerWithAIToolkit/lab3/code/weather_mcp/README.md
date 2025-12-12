<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "999c5e7623c1e2d5e5a07c2feb39eb67",
  "translation_date": "2025-12-11T17:02:55+00:00",
  "source_file": "10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/README.md",
  "language_code": "ml"
}
-->
# Weather MCP Server

Python-ൽ weather tools mock responses ഉപയോഗിച്ച് നടപ്പിലാക്കിയ ഒരു സാമ്പിൾ MCP Server ആണ് ഇത്. നിങ്ങളുടെ സ്വന്തം MCP Server-നായി scaffold ആയി ഇത് ഉപയോഗിക്കാം. ഇതിൽ താഴെപ്പറയുന്ന സവിശേഷതകൾ ഉൾക്കൊള്ളുന്നു:

- **Weather Tool**: നൽകിയ സ്ഥലത്തിന്റെ അടിസ്ഥാനത്തിൽ mock ചെയ്ത കാലാവസ്ഥാ വിവരങ്ങൾ നൽകുന്ന ഒരു ടൂൾ.
- **Agent Builder-ലേക്ക് കണക്ട് ചെയ്യുക**: MCP server-നെ Agent Builder-ലേക്ക് ടെസ്റ്റിംഗിനും ഡീബഗിംഗിനും കണക്ട് ചെയ്യാനുള്ള സവിശേഷത.
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector) ഉപയോഗിച്ച് ഡീബഗ് ചെയ്യുക**: MCP Inspector ഉപയോഗിച്ച് MCP Server ഡീബഗ് ചെയ്യാനുള്ള സവിശേഷത.

## Weather MCP Server ടെംപ്ലേറ്റുമായി തുടങ്ങുക

> **ആവശ്യമായ മുൻകൂർ നിബന്ധനകൾ**
>
> നിങ്ങളുടെ ലോക്കൽ ഡെവ് മെഷീനിൽ MCP Server ഓടിക്കാൻ, നിങ്ങൾക്ക് ആവശ്യമായവ:
>
> - [Python](https://www.python.org/)
> - (*ഐച്ഛികം - uv ഇഷ്ടപ്പെടുന്നവർക്ക്*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## പരിസ്ഥിതി ഒരുക്കുക

ഈ പ്രോജക്ടിനായി പരിസ്ഥിതി സജ്ജമാക്കാൻ രണ്ട് മാർഗ്ഗങ്ങളുണ്ട്. നിങ്ങളുടെ ഇഷ്ടാനുസരണം ഏതെങ്കിലും ഒരു മാർഗ്ഗം തിരഞ്ഞെടുക്കാം.

> കുറിപ്പ്: വിർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിച്ചതിന് ശേഷം VSCode അല്ലെങ്കിൽ ടെർമിനൽ റീലോഡ് ചെയ്ത് വിർച്വൽ എൻവയോൺമെന്റ് പൈത്തൺ ഉപയോഗിക്കുന്നതായി ഉറപ്പാക്കുക.

| മാർഗ്ഗം | ഘട്ടങ്ങൾ |
| -------- | ----- |
| `uv` ഉപയോഗിച്ച് | 1. വിർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക: `uv venv` <br>2. VSCode കമാൻഡ് "***Python: Select Interpreter***" ഓടിച്ച് സൃഷ്ടിച്ച വിർച്വൽ എൻവയോൺമെന്റിലെ പൈത്തൺ തിരഞ്ഞെടുക്കുക <br>3. ഡിപ്പൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുക (ഡെവ് ഡിപ്പൻഡൻസികൾ ഉൾപ്പെടെ): `uv pip install -r pyproject.toml --extra dev` |
| `pip` ഉപയോഗിച്ച് | 1. വിർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക: `python -m venv .venv` <br>2. VSCode കമാൻഡ് "***Python: Select Interpreter***" ഓടിച്ച് സൃഷ്ടിച്ച വിർച്വൽ എൻവയോൺമെന്റിലെ പൈത്തൺ തിരഞ്ഞെടുക്കുക<br>3. ഡിപ്പൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുക (ഡെവ് ഡിപ്പൻഡൻസികൾ ഉൾപ്പെടെ): `pip install -e .[dev]` | 

പരിസ്ഥിതി സജ്ജമാക്കിയ ശേഷം, Agent Builder-നെ MCP Client ആയി ഉപയോഗിച്ച് നിങ്ങളുടെ ലോക്കൽ ഡെവ് മെഷീനിൽ സർവർ ഓടിക്കാം:
1. VS Code Debug പാനൽ തുറക്കുക. `Debug in Agent Builder` തിരഞ്ഞെടുക്കുക അല്ലെങ്കിൽ MCP server ഡീബഗ് ചെയ്യാൻ `F5` അമർത്തുക.
2. AI Toolkit Agent Builder ഉപയോഗിച്ച് [ഈ പ്രോംപ്റ്റ്](../../../../../../../../../../../../open_prompt_builder) ഉപയോഗിച്ച് സർവർ ടെസ്റ്റ് ചെയ്യുക. സർവർ സ്വയം Agent Builder-ലേക്ക് കണക്ട് ചെയ്യും.
3. പ്രോംപ്റ്റ് ഉപയോഗിച്ച് സർവർ ടെസ്റ്റ് ചെയ്യാൻ `Run` ക്ലിക്ക് ചെയ്യുക.

**അഭിനന്ദനങ്ങൾ**! Agent Builder-നെ MCP Client ആയി ഉപയോഗിച്ച് നിങ്ങളുടെ ലോക്കൽ ഡെവ് മെഷീനിൽ Weather MCP Server വിജയകരമായി ഓടിച്ചു.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## ടെംപ്ലേറ്റിൽ ഉൾപ്പെടുത്തിയിരിക്കുന്നവ

| ഫോൾഡർ / ഫയൽ| ഉള്ളടക്കം                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | ഡീബഗിംഗിനുള്ള VSCode ഫയലുകൾ                   |
| `.aitk`      | AI Toolkit-നുള്ള കോൺഫിഗറേഷനുകൾ                |
| `src`        | weather mcp server-ന്റെ സോഴ്‌സ് കോഡ്   |

## Weather MCP Server എങ്ങനെ ഡീബഗ് ചെയ്യാം

> കുറിപ്പുകൾ:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) MCP server-കൾ ടെസ്റ്റ് ചെയ്യാനും ഡീബഗ് ചെയ്യാനും ഉപയോഗിക്കുന്ന ഒരു ദൃശ്യ ഡെവലപ്പർ ടൂൾ ആണ്.
> - എല്ലാ ഡീബഗ് മോഡുകളും ബ്രേക്ക്പോയിന്റുകൾ പിന്തുണയ്ക്കുന്നു, അതിനാൽ ടൂൾ ഇംപ്ലിമെന്റേഷൻ കോഡിൽ ബ്രേക്ക്പോയിന്റുകൾ ചേർക്കാം.

| ഡീബഗ് മോഡ് | വിവരണം | ഡീബഗ് ചെയ്യാനുള്ള ഘട്ടങ്ങൾ |
| ---------- | ----------- | --------------- |
| Agent Builder | AI Toolkit വഴി Agent Builder-ൽ MCP server ഡീബഗ് ചെയ്യുക. | 1. VS Code Debug പാനൽ തുറക്കുക. `Debug in Agent Builder` തിരഞ്ഞെടുക്കുകയും MCP server ഡീബഗ് ചെയ്യാൻ `F5` അമർത്തുകയും ചെയ്യുക.<br>2. AI Toolkit Agent Builder ഉപയോഗിച്ച് [ഈ പ്രോംപ്റ്റ്](../../../../../../../../../../../../open_prompt_builder) ഉപയോഗിച്ച് സർവർ ടെസ്റ്റ് ചെയ്യുക. സർവർ സ്വയം Agent Builder-ലേക്ക് കണക്ട് ചെയ്യും.<br>3. പ്രോംപ്റ്റ് ഉപയോഗിച്ച് സർവർ ടെസ്റ്റ് ചെയ്യാൻ `Run` ക്ലിക്ക് ചെയ്യുക. |
| MCP Inspector | MCP Inspector ഉപയോഗിച്ച് MCP server ഡീബഗ് ചെയ്യുക. | 1. [Node.js](https://nodejs.org/) ഇൻസ്റ്റാൾ ചെയ്യുക<br> 2. Inspector സജ്ജമാക്കുക: `cd inspector` && `npm install` <br> 3. VS Code Debug പാനൽ തുറക്കുക. `Debug SSE in Inspector (Edge)` അല്ലെങ്കിൽ `Debug SSE in Inspector (Chrome)` തിരഞ്ഞെടുക്കുക. ഡീബഗ് ആരംഭിക്കാൻ F5 അമർത്തുക.<br> 4. MCP Inspector ബ്രൗസറിൽ തുറന്നപ്പോൾ, ഈ MCP server-നെ കണക്ട് ചെയ്യാൻ `Connect` ബട്ടൺ ക്ലിക്ക് ചെയ്യുക.<br> 5. തുടർന്ന് `List Tools` ചെയ്യുക, ഒരു ടൂൾ തിരഞ്ഞെടുക്കുക, പാരാമീറ്ററുകൾ നൽകുക, `Run Tool` ക്ലിക്ക് ചെയ്ത് സർവർ കോഡ് ഡീബഗ് ചെയ്യുക.<br> |

## ഡീഫോൾട്ട് പോർട്ടുകളും കസ്റ്റമൈസേഷനുകളും

| ഡീബഗ് മോഡ് | പോർട്ടുകൾ | നിർവചനങ്ങൾ | കസ്റ്റമൈസേഷനുകൾ | കുറിപ്പ് |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | മുകളിൽ പറയുന്ന പോർട്ടുകൾ മാറ്റാൻ [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) എഡിറ്റ് ചെയ്യുക. | പ്രയോഗിക്കാനില്ല |
| MCP Inspector | 3001 (സർവർ); 5173, 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | മുകളിൽ പറയുന്ന പോർട്ടുകൾ മാറ്റാൻ [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) എഡിറ്റ് ചെയ്യുക.| പ്രയോഗിക്കാനില്ല |

## പ്രതികരണം

ഈ ടെംപ്ലേറ്റിനായി നിങ്ങളുടെ അഭിപ്രായങ്ങൾ അല്ലെങ്കിൽ നിർദ്ദേശങ്ങൾ ഉണ്ടെങ്കിൽ, ദയവായി [AI Toolkit GitHub റിപ്പോസിറ്ററിയിൽ](https://github.com/microsoft/vscode-ai-toolkit/issues) ഒരു ഇഷ്യൂ തുറക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->