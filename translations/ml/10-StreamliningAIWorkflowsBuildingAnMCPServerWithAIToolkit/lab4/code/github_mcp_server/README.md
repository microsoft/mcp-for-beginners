<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9a6a4d3497921d2f6d9699f0a6a1890c",
  "translation_date": "2025-12-11T17:06:29+00:00",
  "source_file": "10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/README.md",
  "language_code": "ml"
}
-->
# Weather MCP Server

Python-ൽ മോക്ക് പ്രതികരണങ്ങളോടുകൂടിയ കാലാവസ്ഥാ ഉപകരണങ്ങൾ നടപ്പിലാക്കുന്ന ഒരു സാമ്പിൾ MCP സെർവർ ആണ് ഇത്. നിങ്ങളുടെ സ്വന്തം MCP സെർവറിനായി ഇത് ഒരു സ്കാഫോൾഡ് ആയി ഉപയോഗിക്കാം. ഇതിൽ താഴെപ്പറയുന്ന സവിശേഷതകൾ ഉൾപ്പെടുന്നു:

- **Weather Tool**: നൽകിയ സ്ഥലത്തിന്റെ അടിസ്ഥാനത്തിൽ മോക്ക് ചെയ്ത കാലാവസ്ഥാ വിവരങ്ങൾ നൽകുന്ന ഒരു ഉപകരണം.
- **Git Clone Tool**: ഒരു git റിപോസിറ്ററി നിശ്ചിത ഫോൾഡറിലേക്ക് ക്ലോൺ ചെയ്യാനുള്ള ഉപകരണം.
- **VS Code Open Tool**: ഒരു ഫോൾഡർ VS Code അല്ലെങ്കിൽ VS Code Insiders-ൽ തുറക്കാനുള്ള ഉപകരണം.
- **Connect to Agent Builder**: MCP സെർവറെ Agent Builder-hez ബന്ധിപ്പിച്ച് ടെസ്റ്റിംഗിനും ഡീബഗിംഗിനും ഉപയോഗിക്കുന്ന സവിശേഷത.
- **Debug in [MCP Inspector](https://github.com/modelcontextprotocol/inspector)**: MCP Inspector ഉപയോഗിച്ച് MCP സെർവർ ഡീബഗ് ചെയ്യാനുള്ള സവിശേഷത.

## Weather MCP Server ടെംപ്ലേറ്റുമായി ആരംഭിക്കുക

> **ആവശ്യമായ കാര്യങ്ങൾ**
>
> നിങ്ങളുടെ ലോക്കൽ ഡെവ് മെഷീനിൽ MCP സെർവർ പ്രവർത്തിപ്പിക്കാൻ നിങ്ങൾക്ക് ആവശ്യമായവ:
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (git_clone_repo ടൂളിനായി ആവശ്യമാണ്)
> - [VS Code](https://code.visualstudio.com/) അല്ലെങ്കിൽ [VS Code Insiders](https://code.visualstudio.com/insiders/) (open_in_vscode ടൂളിനായി ആവശ്യമാണ്)
> - (*ഐച്ഛികം - uv ഇഷ്ടപ്പെടുന്നവർക്ക്*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## പരിസ്ഥിതി ഒരുക്കുക

ഈ പ്രോജക്ടിനായി പരിസ്ഥിതി സജ്ജമാക്കാൻ രണ്ട് മാർഗ്ഗങ്ങൾ ഉണ്ട്. നിങ്ങളുടെ ഇഷ്ടാനുസരണം ഏതെങ്കിലും ഒരു മാർഗ്ഗം തിരഞ്ഞെടുക്കാം.

> കുറിപ്പ്: വിർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിച്ചതിന് ശേഷം VSCode അല്ലെങ്കിൽ ടെർമിനൽ റീലോഡ് ചെയ്യുക, വിർച്വൽ എൻവയോൺമെന്റിലെ Python ഉപയോഗിക്കുന്നതായി ഉറപ്പാക്കാൻ.

| മാർഗ്ഗം | ഘട്ടങ്ങൾ |
| -------- | ----- |
| `uv` ഉപയോഗിച്ച് | 1. വിർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക: `uv venv` <br>2. VSCode കമാൻഡ് "***Python: Select Interpreter***" ഓടിച്ച് സൃഷ്ടിച്ച വിർച്വൽ എൻവയോൺമെന്റിലെ Python തിരഞ്ഞെടുക്കുക <br>3. ഡിപ്പൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുക (ഡെവ് ഡിപ്പൻഡൻസികൾ ഉൾപ്പെടെ): `uv pip install -r pyproject.toml --extra dev` |
| `pip` ഉപയോഗിച്ച് | 1. വിർച്വൽ എൻവയോൺമെന്റ് സൃഷ്ടിക്കുക: `python -m venv .venv` <br>2. VSCode കമാൻഡ് "***Python: Select Interpreter***" ഓടിച്ച് സൃഷ്ടിച്ച വിർച്വൽ എൻവയോൺമെന്റിലെ Python തിരഞ്ഞെടുക്കുക<br>3. ഡിപ്പൻഡൻസികൾ ഇൻസ്റ്റാൾ ചെയ്യുക (ഡെവ് ഡിപ്പൻഡൻസികൾ ഉൾപ്പെടെ): `pip install -e .[dev]` | 

പരിസ്ഥിതി സജ്ജമാക്കിയ ശേഷം, Agent Builder-നെ MCP ക്ലയന്റ് ആയി ഉപയോഗിച്ച് നിങ്ങളുടെ ലോക്കൽ ഡെവ് മെഷീനിൽ സെർവർ ഓടിക്കാം:
1. VS Code ഡീബഗ് പാനൽ തുറക്കുക. `Debug in Agent Builder` തിരഞ്ഞെടുക്കുക അല്ലെങ്കിൽ MCP സെർവർ ഡീബഗ് ചെയ്യാൻ `F5` അമർത്തുക.
2. AI Toolkit Agent Builder ഉപയോഗിച്ച് [ഈ പ്രോംപ്റ്റ്](../../../../../../../../../../../../open_prompt_builder) ഉപയോഗിച്ച് സെർവർ ടെസ്റ്റ് ചെയ്യുക. സെർവർ സ്വയം Agent Builder-hez ബന്ധിപ്പിക്കും.
3. പ്രോംപ്റ്റ് ഉപയോഗിച്ച് സെർവർ ടെസ്റ്റ് ചെയ്യാൻ `Run` ക്ലിക്ക് ചെയ്യുക.

**അഭിനന്ദനങ്ങൾ**! നിങ്ങൾ വിജയകരമായി Agent Builder-നെ MCP ക്ലയന്റ് ആയി ഉപയോഗിച്ച് നിങ്ങളുടെ ലോക്കൽ ഡെവ് മെഷീനിൽ Weather MCP Server ഓടിച്ചു.
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## ടെംപ്ലേറ്റിൽ ഉൾപ്പെടുത്തിയിരിക്കുന്നവ

| ഫോൾഡർ / ഫയൽ| ഉള്ളടക്കം                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | ഡീബഗിംഗിനുള്ള VSCode ഫയലുകൾ                   |
| `.aitk`      | AI Toolkit-നുള്ള കോൺഫിഗറേഷനുകൾ                |
| `src`        | weather mcp സെർവറിന്റെ സോഴ്‌സ് കോഡ്   |

## Weather MCP Server എങ്ങനെ ഡീബഗ് ചെയ്യാം

> കുറിപ്പുകൾ:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) MCP സെർവറുകൾ ടെസ്റ്റ് ചെയ്യാനും ഡീബഗ് ചെയ്യാനും ഉപയോഗിക്കുന്ന ഒരു ദൃശ്യ ഡെവലപ്പർ ടൂൾ ആണ്.
> - എല്ലാ ഡീബഗ് മോഡുകളും ബ്രേക്ക്പോയിന്റുകൾ പിന്തുണയ്ക്കുന്നു, അതിനാൽ ടൂൾ നടപ്പിലാക്കൽ കോഡിൽ ബ്രേക്ക്പോയിന്റുകൾ ചേർക്കാം.

## ലഭ്യമായ ടൂളുകൾ

### Weather Tool
`get_weather` ടൂൾ നൽകിയ സ്ഥലത്തിനായി മോക്ക് ചെയ്ത കാലാവസ്ഥാ വിവരങ്ങൾ നൽകുന്നു.

| പാരാമീറ്റർ | തരം | വിവരണം |
| --------- | ---- | ----------- |
| `location` | string | കാലാവസ്ഥ അറിയാൻ വേണ്ട സ്ഥലം (ഉദാ: നഗരം, സംസ്ഥാനo, അല്ലെങ്കിൽ കോഓർഡിനേറ്റുകൾ) |

### Git Clone Tool
`git_clone_repo` ടൂൾ ഒരു git റിപോസിറ്ററി നിശ്ചിത ഫോൾഡറിലേക്ക് ക്ലോൺ ചെയ്യുന്നു.

| പാരാമീറ്റർ | തരം | വിവരണം |
| --------- | ---- | ----------- |
| `repo_url` | string | ക്ലോൺ ചെയ്യേണ്ട git റിപോസിറ്ററിയുടെ URL |
| `target_folder` | string | റിപോസിറ്ററി ക്ലോൺ ചെയ്യേണ്ട ഫോൾഡറിന്റെ പാത |

ടൂൾ ഒരു JSON ഒബ്ജക്റ്റ് റിട്ടേൺ ചെയ്യുന്നു:
- `success`: ഓപ്പറേഷൻ വിജയിച്ചോ എന്ന് സൂചിപ്പിക്കുന്ന ബൂളിയൻ
- `target_folder` അല്ലെങ്കിൽ `error`: ക്ലോൺ ചെയ്ത റിപോസിറ്ററിയുടെ പാത അല്ലെങ്കിൽ ഒരു പിശക് സന്ദേശം

### VS Code Open Tool
`open_in_vscode` ടൂൾ ഒരു ഫോൾഡർ VS Code അല്ലെങ്കിൽ VS Code Insiders ആപ്ലിക്കേഷനിൽ തുറക്കുന്നു.

| പാരാമീറ്റർ | തരം | വിവരണം |
| --------- | ---- | ----------- |
| `folder_path` | string | തുറക്കേണ്ട ഫോൾഡറിന്റെ പാത |
| `use_insiders` | boolean (ഐച്ഛികം) | സാധാരണ VS Code-ന്റെ പകരം VS Code Insiders ഉപയോഗിക്കണോ എന്നത് |

ടൂൾ ഒരു JSON ഒബ്ജക്റ്റ് റിട്ടേൺ ചെയ്യുന്നു:
- `success`: ഓപ്പറേഷൻ വിജയിച്ചോ എന്ന് സൂചിപ്പിക്കുന്ന ബൂളിയൻ
- `message` അല്ലെങ്കിൽ `error`: സ്ഥിരീകരണ സന്ദേശം അല്ലെങ്കിൽ പിശക് സന്ദേശം

| ഡീബഗ് മോഡ് | വിവരണം | ഡീബഗ് ചെയ്യാനുള്ള ഘട്ടങ്ങൾ |
| ---------- | ----------- | --------------- |
| Agent Builder | AI Toolkit വഴി Agent Builder-ൽ MCP സെർവർ ഡീബഗ് ചെയ്യുക. | 1. VS Code ഡീബഗ് പാനൽ തുറക്കുക. `Debug in Agent Builder` തിരഞ്ഞെടുക്കുകയും MCP സെർവർ ഡീബഗ് ചെയ്യാൻ `F5` അമർത്തുകയും ചെയ്യുക.<br>2. AI Toolkit Agent Builder ഉപയോഗിച്ച് [ഈ പ്രോംപ്റ്റ്](../../../../../../../../../../../../open_prompt_builder) ഉപയോഗിച്ച് സെർവർ ടെസ്റ്റ് ചെയ്യുക. സെർവർ സ്വയം Agent Builder-hez ബന്ധിപ്പിക്കും.<br>3. പ്രോംപ്റ്റ് ഉപയോഗിച്ച് സെർവർ ടെസ്റ്റ് ചെയ്യാൻ `Run` ക്ലിക്ക് ചെയ്യുക. |
| MCP Inspector | MCP Inspector ഉപയോഗിച്ച് MCP സെർവർ ഡീബഗ് ചെയ്യുക. | 1. [Node.js](https://nodejs.org/) ഇൻസ്റ്റാൾ ചെയ്യുക<br> 2. Inspector സജ്ജമാക്കുക: `cd inspector` && `npm install` <br> 3. VS Code ഡീബഗ് പാനൽ തുറക്കുക. `Debug SSE in Inspector (Edge)` അല്ലെങ്കിൽ `Debug SSE in Inspector (Chrome)` തിരഞ്ഞെടുക്കുക. ഡീബഗ് ആരംഭിക്കാൻ F5 അമർത്തുക.<br> 4. MCP Inspector ബ്രൗസറിൽ തുറന്നപ്പോൾ, ഈ MCP സെർവറുമായി ബന്ധിപ്പിക്കാൻ `Connect` ബട്ടൺ ക്ലിക്ക് ചെയ്യുക.<br> 5. തുടർന്ന് `List Tools` ചെയ്യാം, ഒരു ടൂൾ തിരഞ്ഞെടുക്കാം, പാരാമീറ്ററുകൾ നൽകാം, `Run Tool` ക്ലിക്ക് ചെയ്ത് സെർവർ കോഡ് ഡീബഗ് ചെയ്യാം.<br> |

## ഡീഫോൾട്ട് പോർട്ടുകളും കസ്റ്റമൈസേഷനുകളും

| ഡീബഗ് മോഡ് | പോർട്ടുകൾ | നിർവചനങ്ങൾ | കസ്റ്റമൈസേഷനുകൾ | കുറിപ്പ് |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | മുകളിൽ പറയുന്ന പോർട്ടുകൾ മാറ്റാൻ [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) എഡിറ്റ് ചെയ്യുക. | പ്രയോഗയോഗ്യമല്ല |
| MCP Inspector | 3001 (സെർവർ); 5173, 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | മുകളിൽ പറയുന്ന പോർട്ടുകൾ മാറ്റാൻ [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) എഡിറ്റ് ചെയ്യുക.| പ്രയോഗയോഗ്യമല്ല |

## പ്രതികരണം

ഈ ടെംപ്ലേറ്റിനായി നിങ്ങൾക്ക് എന്തെങ്കിലും അഭിപ്രായങ്ങൾ അല്ലെങ്കിൽ നിർദ്ദേശങ്ങൾ ഉണ്ടെങ്കിൽ, ദയവായി [AI Toolkit GitHub റിപോസിറ്ററിയിൽ](https://github.com/microsoft/vscode-ai-toolkit/issues) ഒരു ഇഷ്യൂ തുറക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->