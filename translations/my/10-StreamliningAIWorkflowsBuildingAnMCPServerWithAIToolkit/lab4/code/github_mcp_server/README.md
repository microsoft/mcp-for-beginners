# ရာသီဥတု MCP Server

ဒီဟာက Python မှာ ရေးသားထားတဲ့ ရာသီဥတု tools တွေကို mock response တွေနဲ့ အကောင်အထည်ဖော်ထားတဲ့ sample MCP Server တစ်ခုဖြစ်ပါတယ်။ သင့်ရဲ့ MCP Server ကို ဖန်တီးဖို့အတွက် scaffold အနေနဲ့ အသုံးပြုနိုင်ပါတယ်။ အောက်ပါ feature တွေပါဝင်ပါတယ်-

- **ရာသီဥတု Tool**: ပေးထားတဲ့ location အပေါ်မူတည်ပြီး mock ရာသီဥတုအချက်အလက်တွေကို ပေးတဲ့ tool တစ်ခု။
- **Git Clone Tool**: git repository ကို သတ်မှတ်ထားတဲ့ folder ထဲ clone လုပ်ပေးတဲ့ tool တစ်ခု။
- **VS Code Open Tool**: folder တစ်ခုကို VS Code သို့မဟုတ် VS Code Insiders မှာ ဖွင့်ပေးတဲ့ tool တစ်ခု။
- **Agent Builder နဲ့ ချိတ်ဆက်မှု**: MCP server ကို Agent Builder နဲ့ testing နဲ့ debugging အတွက် ချိတ်ဆက်နိုင်တဲ့ feature တစ်ခု။
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector) မှာ Debug လုပ်ခြင်း**: MCP Server ကို MCP Inspector အသုံးပြုပြီး debug လုပ်နိုင်တဲ့ feature တစ်ခု။

## ရာသီဥတု MCP Server template ကို စတင်အသုံးပြုခြင်း

> **လိုအပ်ချက်များ**
>
> MCP Server ကို သင့်ရဲ့ local development machine မှာ run လုပ်ဖို့အတွက် အောက်ပါအရာတွေလိုအပ်ပါတယ်-
>
> - [Python](https://www.python.org/)
> - [Git](https://git-scm.com/) (git_clone_repo tool အတွက်လိုအပ်သည်)
> - [VS Code](https://code.visualstudio.com/) သို့မဟုတ် [VS Code Insiders](https://code.visualstudio.com/insiders/) (open_in_vscode tool အတွက်လိုအပ်သည်)
> - (*Optional - uv ကို သင်နှစ်သက်လျှင်*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## Environment ကို ပြင်ဆင်ခြင်း

ဒီ project အတွက် environment ကို ပြင်ဆင်ဖို့အတွက် နည်းလမ်းနှစ်ခုရှိပါတယ်။ သင့်ရဲ့နှစ်သက်မှုအပေါ်မူတည်ပြီး တစ်ခုကို ရွေးချယ်နိုင်ပါတယ်။

> မှတ်ချက်: virtual environment ကို ဖန်တီးပြီးနောက် VSCode သို့မဟုတ် terminal ကို reload လုပ်ပါ၊ virtual environment python ကို အသုံးပြုနိုင်ရန်။

| နည်းလမ်း | လုပ်ဆောင်ရန်အဆင့်များ |
| -------- | ----------------------- |
| `uv` အသုံးပြုခြင်း | 1. virtual environment ဖန်တီးပါ: `uv venv` <br>2. VSCode Command "***Python: Select Interpreter***" ကို run လုပ်ပြီး ဖန်တီးထားတဲ့ virtual environment မှ python ကို ရွေးချယ်ပါ <br>3. dependencies (dev dependencies အပါအဝင်) ကို install လုပ်ပါ: `uv pip install -r pyproject.toml --extra dev` |
| `pip` အသုံးပြုခြင်း | 1. virtual environment ဖန်တီးပါ: `python -m venv .venv` <br>2. VSCode Command "***Python: Select Interpreter***" ကို run လုပ်ပြီး ဖန်တီးထားတဲ့ virtual environment မှ python ကို ရွေးချယ်ပါ<br>3. dependencies (dev dependencies အပါအဝင်) ကို install လုပ်ပါ: `pip install -e .[dev]` | 

Environment ကို ပြင်ဆင်ပြီးနောက် MCP Client အနေနဲ့ Agent Builder မှာ server ကို run လုပ်နိုင်ပါတယ်-
1. VS Code Debug panel ကို ဖွင့်ပါ။ `Debug in Agent Builder` ကို ရွေးချယ်ပါ သို့မဟုတ် `F5` ကို နှိပ်ပြီး MCP server ကို debugging စတင်ပါ။
2. AI Toolkit Agent Builder ကို အသုံးပြုပြီး [ဒီ prompt](../../../../../../../../../../../open_prompt_builder) နဲ့ server ကို စမ်းသပ်ပါ။ Server ကို Agent Builder နဲ့ auto-connected ဖြစ်စေပါမည်။
3. `Run` ကို နှိပ်ပြီး prompt နဲ့ server ကို စမ်းသပ်ပါ။

**ဂုဏ်ပြုပါတယ်**! သင့်ရဲ့ local development machine မှာ MCP Client အနေနဲ့ Agent Builder ကို အသုံးပြုပြီး ရာသီဥတု MCP Server ကို အောင်မြင်စွာ run လုပ်ပြီးပါပြီ။
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## Template ထဲမှာ ပါဝင်တဲ့အရာများ

| Folder / File| ပါဝင်မှုများ                                     |
| ------------ | -------------------------------------------- |
| `.vscode`    | debugging အတွက် VSCode files                   |
| `.aitk`      | AI Toolkit အတွက် configurations                |
| `src`        | ရာသီဥတု MCP server အတွက် source code          |

## ရာသီဥတု MCP Server ကို Debug လုပ်နည်း

> မှတ်ချက်များ:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) က MCP server တွေကို စမ်းသပ်ခြင်းနဲ့ debug လုပ်ခြင်းအတွက် visual developer tool တစ်ခုဖြစ်ပါတယ်။
> - Debugging modes အားလုံးမှာ breakpoints တွေကို support လုပ်ပါတယ်၊ tool implementation code မှာ breakpoints တွေ ထည့်နိုင်ပါတယ်။

## အသုံးပြုနိုင်တဲ့ Tools

### ရာသီဥတု Tool
`get_weather` tool က သတ်မှတ်ထားတဲ့ location အတွက် mock ရာသီဥတုအချက်အလက်တွေကို ပေးပါတယ်။

| Parameter | Type | ဖော်ပြချက် |
| --------- | ---- | ----------- |
| `location` | string | ရာသီဥတုကို သိလိုတဲ့ location (ဥပမာ- မြို့နာမည်၊ ပြည်နယ်၊ သို့မဟုတ် ကိန်းဂဏန်း) |

### Git Clone Tool
`git_clone_repo` tool က git repository ကို သတ်မှတ်ထားတဲ့ folder ထဲ clone လုပ်ပေးပါတယ်။

| Parameter | Type | ဖော်ပြချက် |
| --------- | ---- | ----------- |
| `repo_url` | string | clone လုပ်လိုတဲ့ git repository ရဲ့ URL |
| `target_folder` | string | repository ကို clone လုပ်မယ့် folder ရဲ့ လမ်းကြောင်း |

Tool က JSON object တစ်ခု return ပြန်ပါမည်-
- `success`: operation အောင်မြင်မှုကို ဖော်ပြတဲ့ Boolean
- `target_folder` သို့မဟုတ် `error`: clone လုပ်ထားတဲ့ repository ရဲ့ လမ်းကြောင်း သို့မဟုတ် error message

### VS Code Open Tool
`open_in_vscode` tool က folder တစ်ခုကို VS Code သို့မဟုတ် VS Code Insiders application မှာ ဖွင့်ပေးပါတယ်။

| Parameter | Type | ဖော်ပြချက် |
| --------- | ---- | ----------- |
| `folder_path` | string | ဖွင့်လိုတဲ့ folder ရဲ့ လမ်းကြောင်း |
| `use_insiders` | boolean (optional) | VS Code Insiders ကို အသုံးပြုမလား regular VS Code ကို အသုံးပြုမလား |

Tool က JSON object တစ်ခု return ပြန်ပါမည်-
- `success`: operation အောင်မြင်မှုကို ဖော်ပြတဲ့ Boolean
- `message` သို့မဟုတ် `error`: အတည်ပြုချက် message သို့မဟုတ် error message

| Debug Mode | ဖော်ပြချက် | Debug လုပ်နည်း |
| ---------- | ----------- | --------------- |
| Agent Builder | MCP server ကို AI Toolkit မှာ Agent Builder နဲ့ debug လုပ်ပါ။ | 1. VS Code Debug panel ကို ဖွင့်ပါ။ `Debug in Agent Builder` ကို ရွေးချယ်ပြီး `F5` ကို နှိပ်ပါ။ MCP server ကို debugging စတင်ပါ။<br>2. AI Toolkit Agent Builder ကို အသုံးပြုပြီး [ဒီ prompt](../../../../../../../../../../../open_prompt_builder) နဲ့ server ကို စမ်းသပ်ပါ။ Server ကို Agent Builder နဲ့ auto-connected ဖြစ်စေပါမည်။<br>3. `Run` ကို နှိပ်ပြီး prompt နဲ့ server ကို စမ်းသပ်ပါ။ |
| MCP Inspector | MCP server ကို MCP Inspector အသုံးပြုပြီး debug လုပ်ပါ။ | 1. [Node.js](https://nodejs.org/) ကို install လုပ်ပါ<br> 2. Inspector ကို ပြင်ဆင်ပါ: `cd inspector` && `npm install` <br> 3. VS Code Debug panel ကို ဖွင့်ပါ။ `Debug SSE in Inspector (Edge)` သို့မဟုတ် `Debug SSE in Inspector (Chrome)` ကို ရွေးချယ်ပါ။ F5 ကို နှိပ်ပြီး debugging စတင်ပါ။<br> 4. MCP Inspector ကို browser မှာ ဖွင့်ပါ။ MCP server ကို ချိတ်ဆက်ဖို့ `Connect` button ကို နှိပ်ပါ။<br> 5. `List Tools` ကို ရွေးချယ်ပြီး tool တစ်ခုကို ရွေးပါ၊ parameter တွေကို input လုပ်ပြီး `Run Tool` ကို နှိပ်ပါ။ server code ကို debug လုပ်နိုင်ပါမည်။<br> |

## Default Ports နဲ့ customization

| Debug Mode | Ports | ဖော်ပြချက် | Customizations | မှတ်ချက် |
| ---------- | ----- | ------------ | -------------- |-------------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) ကို edit လုပ်ပြီး ports တွေကို ပြောင်းနိုင်သည်။ | N/A |
| MCP Inspector | 3001 (Server); 5173 နဲ့ 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab4/code/github_mcp_server/.aitk/mcp.json) ကို edit လုပ်ပြီး ports တွေကို ပြောင်းနိုင်သည်။| N/A |

## အကြံပြုချက်

ဒီ template အတွက် အကြံပြုချက် သို့မဟုတ် အဆိုပြုချက်များရှိပါက [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues) မှာ issue တစ်ခုဖွင့်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။