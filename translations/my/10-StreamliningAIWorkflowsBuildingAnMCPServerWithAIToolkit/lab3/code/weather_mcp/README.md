# Weather MCP Server

Python ဖြင့်ရေးသားထားသော weather tools များကို mock response များဖြင့် အကောင်အထည်ဖော်ထားသည့် MCP Server နမူနာဖြစ်သည်။ သင့်ရဲ့ MCP Server ကို တည်ဆောက်ရာတွင် အခြေခံအဖြစ် အသုံးပြုနိုင်သည်။ အောက်ပါ လုပ်ဆောင်ချက်များ ပါဝင်သည်။

- **Weather Tool**: ပေးထားသော တည်နေရာအပေါ် အခြေခံ၍ မော်ကွန်းထားသော ရာသီဥတု အချက်အလက်များကို ပေးသော ကိရိယာ။
- **Agent Builder နှင့် ချိတ်ဆက်ခြင်း**: MCP server ကို Agent Builder နှင့် ချိတ်ဆက်၍ စမ်းသပ်ခြင်းနှင့် အမှားရှာဖွေရေးလုပ်ဆောင်နိုင်စေရန် လုပ်ဆောင်ချက်။
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector) တွင် Debug ပြုလုပ်ခြင်း**: MCP Inspector ကို အသုံးပြု၍ MCP Server ကို debug ပြုလုပ်နိုင်ခြင်း။

## Weather MCP Server နမူနာဖြင့် စတင်အသုံးပြုခြင်း

> **လိုအပ်ချက်များ**
>
> သင့်ရဲ့ ဒေဗလပ်မင့်စက်တွင် MCP Server ကို လည်ပတ်ရန် အောက်ပါအရာများ လိုအပ်ပါသည်။
>
> - [Python](https://www.python.org/)
> - (*Optional - uv ကို သဘောကျပါက*) [uv](https://github.com/astral-sh/uv)
> - [Python Debugger Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)

## ပတ်ဝန်းကျင် ပြင်ဆင်ခြင်း

ဤပရောဂျက်အတွက် ပတ်ဝန်းကျင် ပြင်ဆင်ရာတွင် နည်းလမ်း နှစ်မျိုး ရှိသည်။ သင့်စိတ်ကြိုက် တစ်ခုကို ရွေးချယ်နိုင်ပါသည်။

> မှတ်ချက် - virtual environment ဖန်တီးပြီးနောက် VSCode သို့မဟုတ် terminal ကို ပြန်လည်ဖွင့်၍ virtual environment ထဲမှ python ကို အသုံးပြုနေကြောင်း သေချာစေရန်။

| နည်းလမ်း | အဆင့်များ |
| -------- | --------- |
| `uv` အသုံးပြုခြင်း | 1. virtual environment ဖန်တီးရန်: `uv venv` <br>2. VSCode Command "***Python: Select Interpreter***" ကို ဖွင့်ပြီး ဖန်တီးထားသော virtual environment ထဲမှ python ကို ရွေးချယ်ပါ <br>3. လိုအပ်သော dependencies (dev dependencies ပါဝင်သည်) ကို ထည့်သွင်းရန်: `uv pip install -r pyproject.toml --extra dev` |
| `pip` အသုံးပြုခြင်း | 1. virtual environment ဖန်တီးရန်: `python -m venv .venv` <br>2. VSCode Command "***Python: Select Interpreter***" ကို ဖွင့်ပြီး ဖန်တီးထားသော virtual environment ထဲမှ python ကို ရွေးချယ်ပါ <br>3. လိုအပ်သော dependencies (dev dependencies ပါဝင်သည်) ကို ထည့်သွင်းရန်: `pip install -e .[dev]` |

ပတ်ဝန်းကျင် ပြင်ဆင်ပြီးနောက်၊ Agent Builder ကို MCP Client အဖြစ် အသုံးပြု၍ သင့်ဒေဗလပ်မင့်စက်တွင် server ကို လည်ပတ်နိုင်ပါသည်။
1. VS Code Debug panel ကို ဖွင့်ပါ။ `Debug in Agent Builder` ကို ရွေးချယ်၍ သို့မဟုတ် `F5` ကို နှိပ်ကာ MCP server ကို debug စတင်ပါ။
2. AI Toolkit Agent Builder ကို အသုံးပြု၍ [ဤ prompt](../../../../../../../../../../open_prompt_builder) ဖြင့် server ကို စမ်းသပ်ပါ။ Server သည် Agent Builder နှင့် အလိုအလျောက် ချိတ်ဆက်ထားပါလိမ့်မည်။
3. `Run` ကို နှိပ်ကာ prompt ဖြင့် server ကို စမ်းသပ်ပါ။

**ဂုဏ်ယူပါတယ်**! Agent Builder ကို MCP Client အဖြစ် အသုံးပြု၍ သင့်ဒေဗလပ်မင့်စက်တွင် Weather MCP Server ကို အောင်မြင်စွာ လည်ပတ်နိုင်ပါပြီ။
![DebugMCP](https://raw.githubusercontent.com/microsoft/windows-ai-studio-templates/refs/heads/dev/mcpServers/mcp_debug.gif)

## နမူနာတွင် ပါဝင်သော အရာများ

| ဖိုလ်ဒါ / ဖိုင် | အကြောင်းအရာ |
| -------------- | ------------- |
| `.vscode`      | Debugging အတွက် VSCode ဖိုင်များ |
| `.aitk`        | AI Toolkit အတွက် ဖွဲ့စည်းမှုများ |
| `src`          | weather mcp server အတွက် source code |

## Weather MCP Server ကို ဘယ်လို debug ပြုလုပ်မလဲ

> မှတ်ချက်များ:
> - [MCP Inspector](https://github.com/modelcontextprotocol/inspector) သည် MCP server များကို စမ်းသပ်ခြင်းနှင့် debug ပြုလုပ်ရာတွင် အသုံးပြုသော visual developer ကိရိယာဖြစ်သည်။
> - Debugging mode အားလုံးတွင် breakpoint များ ထည့်သွင်းနိုင်ပြီး tool implementation code တွင် breakpoint ထည့်နိုင်ပါသည်။

| Debug Mode | ဖော်ပြချက် | Debug ပြုလုပ်ရန် အဆင့်များ |
| ---------- | ---------- | --------------------------- |
| Agent Builder | AI Toolkit မှတဆင့် Agent Builder တွင် MCP server ကို debug ပြုလုပ်ခြင်း | 1. VS Code Debug panel ကို ဖွင့်ပါ။ `Debug in Agent Builder` ကို ရွေးချယ်ပြီး `F5` ကို နှိပ်ကာ MCP server ကို debug စတင်ပါ။<br>2. AI Toolkit Agent Builder ကို အသုံးပြု၍ [ဤ prompt](../../../../../../../../../../open_prompt_builder) ဖြင့် server ကို စမ်းသပ်ပါ။ Server သည် Agent Builder နှင့် အလိုအလျောက် ချိတ်ဆက်ထားပါလိမ့်မည်။<br>3. `Run` ကို နှိပ်ကာ prompt ဖြင့် server ကို စမ်းသပ်ပါ။ |
| MCP Inspector | MCP Inspector ကို အသုံးပြု၍ MCP server ကို debug ပြုလုပ်ခြင်း | 1. [Node.js](https://nodejs.org/) ကို ထည့်သွင်းပါ<br>2. Inspector ကို ပြင်ဆင်ရန်: `cd inspector` && `npm install` <br>3. VS Code Debug panel ကို ဖွင့်ပါ။ `Debug SSE in Inspector (Edge)` သို့မဟုတ် `Debug SSE in Inspector (Chrome)` ကို ရွေးချယ်ပြီး `F5` ကို နှိပ်ကာ debug စတင်ပါ။<br>4. MCP Inspector သည် browser တွင် ဖွင့်လာသောအခါ `Connect` ခလုတ်ကို နှိပ်ကာ MCP server နှင့် ချိတ်ဆက်ပါ။<br>5. ထို့နောက် `List Tools` ကို နှိပ်၍ ကိရိယာတစ်ခုကို ရွေးချယ်၊ parameter များ ထည့်သွင်းပြီး `Run Tool` ဖြင့် server code ကို debug ပြုလုပ်နိုင်ပါသည်။<br> |

## ပုံမှန် Port များနှင့် စိတ်ကြိုက်ပြင်ဆင်မှုများ

| Debug Mode | Port များ | ဖော်ပြချက်များ | စိတ်ကြိုက်ပြင်ဆင်မှုများ | မှတ်ချက် |
| ---------- | --------- | ------------- | ------------------------- | -------- |
| Agent Builder | 3001 | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) တွင် အထက်ဖော်ပြထားသော port များ ပြောင်းလဲနိုင်သည်။ | N/A |
| MCP Inspector | 3001 (Server); 5173 နှင့် 3000 (Inspector) | [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json) | [launch.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/launch.json), [tasks.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.vscode/tasks.json), [\_\_init\_\_.py](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/src/__init__.py), [mcp.json](../../../../../../10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/lab3/code/weather_mcp/.aitk/mcp.json) တွင် အထက်ဖော်ပြထားသော port များ ပြောင်းလဲနိုင်သည်။ | N/A |

## တုံ့ပြန်ချက်

ဤနမူနာအတွက် တုံ့ပြန်ချက် သို့မဟုတ် အကြံပြုချက်များ ရှိပါက [AI Toolkit GitHub repository](https://github.com/microsoft/vscode-ai-toolkit/issues) တွင် issue တစ်ခု ဖွင့်ပေးပါ။

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ အတည်ပြုရမည့် အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မရှိပါ။