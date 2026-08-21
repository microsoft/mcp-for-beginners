# Visual Studio Code အတွက် AI Toolkit extension မှ server ကို စားသုံးခြင်း

AI agent တစ်ခုကို တည်ဆောက်သောအခါ၊ အမှန်တကယ် စမတ်ဖြေကြားချက်များ ရှိခြင်းသာမက၊ သင့် agent ကို လှုပ်ရှားနိုင်စွမ်း ပေးခြင်းလည်း အရေးကြီးသည်။ ဒီမှာ Model Context Protocol (MCP) က အရေးပါတယ်။ MCP က agent တွေကို အပြင် tools နဲ့ services ကို အဆင်ပြေစွာ ရယူအသုံးပြုခွင့် ပေးပါတယ်။ သင်၏ agent ကို အသုံးပြုနိုင်မယ့် toolbox တစ်ခုနဲ့ ချိတ်ဆက်ထားသလို ထင်နိုင်ပါစေ။

သင့်ရဲ့ agent ကို calculator MCP server နဲ့ ချိတ်ဆက်မယ်ဆိုရင်၊ “47 times 89 ဘယ်လောက်လဲ?” ဆိုတဲ့ prompt တစ်ခုရလို့ math operation တွေကို လွယ်ကူစွာ ကျင့်ကြံနိုင်မှာ ဖြစ်ပါတယ်။ logic ကိုအတော်လောက် hardcode လုပ်ဖို့ မလိုတော့ပါဘူး၊ custom API တွေတည်ဆောက်ဖို့လည်းမလိုတော့ပါဘူး။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာတော့ Visual Studio Code အတွက် [AI Toolkit](https://aka.ms/AIToolkit) extension ကို သုံးပြီး calculator MCP server ကို agent နဲ့ ချိတ်ဆက်ခြင်း၊ သင့် agent က ရိုးရိုးဘာသာစကားနဲ့ တွက်ချက်မှု operation တွေပြုလုပ်နိုင်အောင် သွားစေမယ့်နည်းလမ်းတွေကို ရှင်းပြပါလိမ့်မယ်။

AI Toolkit သည် Visual Studio Code အတွက် agent ဖန်တီးရာမှာ အလွန်အစွမ်းထက်သော extension ဖြစ်ပြီး AI Engineer များအတွက် locally သို့မဟုတ် cloud မှာ generative AI model များ ဖန်တီး၊ စမ်းသပ်ရန် အဆင်ပြေစေပါသည်။ ဒီ extension သည် ပေါ်ပြူလာ generative model များ အများစုကို အထောက်အပံ့ ပေးထားပါသည်။

*မှတ်ချက်* - AI Toolkit သည် လတ်တလောတွင် Python နှင့် TypeScript များကိုပင် အထောက်အပံ့ ပေးနေပါသည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာပြီးဆုံးချိန်မှာ သင်မှာဖြစ်နိုင်ပါမယ် -

- AI Toolkit ဖြင့် MCP server ကို စားသုံးနိုင်ခြင်း။
- MCP server က tools တွေကို agent configuration မှတဆင့် ရှာဖွေပြီး အသုံးပြုနိုင်အောင် စီစဉ်ရေးဆွဲနိုင်ခြင်း။
- ရိုးရိုးဘာသာစကားဖြင့် MCP tools များကို အသုံးပြုနိုင်ခြင်း။

## နည်းလမ်း

အထက်တန်းမှာ လုပ်ဆောင်ပုံကို ဒီအတိုင်းဆောင်ရွက်ရမယ်

- Agent တစ်ခု ဖန်တီးပြီး system prompt ကို သတ်မှတ်ခြင်း။
- calculator tools များပါရှိတဲ့ MCP server တစ်ခု ဖန်တီးခြင်း။
- Agent Builder ကို MCP server နဲ့ ချိတ်ဆက်ခြင်း။
- ရိုးရိုးဘာသာစကားဖြင့် agent အကိရိယာ အသုံးပြုမှု စမ်းသပ်ခြင်း။

ကောင်းပြီ၊ လမ်းကြောင်းနားလည်သွားပြီဆိုရင် MCP ကနေ အပြင် tools တွေ သုံးပြီး AI agent ကို အသုံးချဆိုတာ configure လုပ်ကြရအောင်၊ ၎င်းအား ကောင်းမွန်စေဖို့!

## လိုအပ်ချက်များ

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code အတွက် AI Toolkit](https://aka.ms/AIToolkit)

## လေ့ကျင့်မှု - server စားသုံးခြင်း

> [!WARNING]
> macOS အသုံးပြုသူများအတွက် သတိပေးချက်။ macOS system တွင် dependency install ပြဿနာတစ်ခုရှိနေသည်။ ဒါကြောင့် macOS အသုံးပြုသူများက ဒီသင်ခန်းစာကို အချိန်အခါ၊ အဆင်မပြေပါဘူး။ ပြဿနာပြင်ဆင်ချက် ထွက်လာလိုက်ပြီ ကျွန်ုပ်တို့ ပြန်လည်အသစ်ပြောင်းလဲ ပြင်ဆင်ချက်များကို update လုပ်ပါမယ်။ သင့်ညှိနှိုင်းမှုနှင့် နားလည်မှုအတွက် ကျေးဇူးတင်ပါသည်။

ဒီလေ့ကျင့်မှုမှာ Visual Studio Code အတွင်း AI Toolkit အသုံးပြုပြီး MCP server ထဲက tools တွေနဲ့ AI agent တစ်ခုကို တည်ဆောက်၊ ပြေးဆွဲ၊ တိုးတက်မြှင့်တင်လုပ်ဆောင်ပါလိမ့်မယ်။

### -0- Prestep၊ My Models ထဲသို့ OpenAI GPT-4o model ထည့်ခြင်း

ကျောင်းပြောင်းမတိုင်မီ **GPT-4o** model ကို **My Models** ထဲ ထည့်ထားရပါမည်။

![Visual Studio Code ရဲ့ AI Toolkit extension မှ model ရွေးချယ်မှု အင်တာဖေ့(စ်)၏ Screenshot ဖြစ်ပြီး ခေါင်းစဉ်မှာ "Find the right model for your AI Solution" ဟုပြထားသည်။ subtitle တွင် AI model များကို ရှာဖွေ၊ စမ်းသပ်၊ ထုတ်လွှင့်ရန် ဆွဲဆောင်သည်။ "Popular Models" ကဏ္ဍအောက်တွင် DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), DeepSeek-R1 (Ollama-hosted) စသည်တို့ပါဝင်ပြီး နောက်ခံတွင် "Add" နဲ့ "Try in Playground" ရွေးချယ်စရာများ ပါဝင်သည်။](../../../../translated_images/my/aitk-model-catalog.2acd38953bb9c119.webp)

1. **Activity Bar** မှ **AI Toolkit** extension ကိုဖွင့်ပါ။
1. **Catalog** အကွက်မှာ **Models** ကိုရွေးပါ။ **Models** ကိုရွေးလိုက်ရင် **Model Catalog** ကို editor tab အသစ်မှာ ဖွင့်စေပါလိမ့်မယ်။
1. **Model Catalog** ရှာဖွေရေးနယ်မှာ **OpenAI GPT-4o** ရိုက်ထည့်ပါ။
1. **+ Add** ကိုနှိပ်ပြီး model ကို **My Models** စာရင်းထဲထည့်ပါ။ GitHub မှာ host ထားတဲ့ model ကို ရွေးချယ်ထားဖို့သေချာပါစေ။
1. **Activity Bar** မှာ **OpenAI GPT-4o** model ကို စာရင်းထဲ တွေ့ရမည်။

### -1- Agent တစ်ယောက် ဖန်တီးခြင်း

**Agent (Prompt) Builder** က သင့်အတွက် ရုပ်သိမ်းထက် agent များကို ဖန်တီး ပြင်ဆင်နိုင်စေသည်။ ဒီအပိုင်းမှာ agent အသစ်တစ်ယောက် ဖန်တီးပြီး စကားပြောဆိုမှုအတွက် အသုံးပြုမယ့် model ကို သတ်မှတ်ပေးပါမယ်။

![Visual Studio Code ၏ AI Toolkit extension မှ "Calculator Agent" builder interface မှာ၊ ဘက်စင်ပANEL တွင် "OpenAI GPT-4o (via GitHub)" model ရွေးထားသည်။ system prompt တွင် "You are a professor in university teaching math" ဟုပြထားပြီး user prompt မှာ "Explain to me the Fourier equation in simple terms." ဟုပြထားသည်။ Tools ထည့်ရန် ခလုတ်၊ MCP Server ဖွင့်ရန် သုံးစွဲခလုတ် နှင့် အစီအစဉ်အပေါ် output format ရွေးချယ်မှုများပါဝင်သည်။ Run ခလုတ်နီက အောက်ဖက်၌တည်ရှိသည်။ ညာဘက် ၊ "Get Started with Examples" အောက်မှာ Web Developer (MCP Server နဲ့ Second-Grade Simplifier နဲ့ Dream Interpreter လည်း ပါထည့်ထားသောตัวอย่าง Agent များ) တွေကို ဖော်ပြထားသည်။](../../../../translated_images/my/aitk-agent-builder.901e3a2960c3e477.webp)

1. **Activity Bar** မှ **AI Toolkit** extension ကို ဖွင့်ပါ။
1. **Tools** အကွက်မှာ **Agent (Prompt) Builder** ကိုရွေးပါ။ **Agent (Prompt) Builder** ကိုရွေးလိုက်ရင် editor tab အသစ်တွင် ဖွင့်ပါလိမ့်မယ်။
1. **+ New Agent** ခလုတ်ကို နှိပ်ပါ။ နောက်ထပ် **Command Palette** မှ setup wizard သည် အလိုအလျောက် ဖွင့်လာပါလိမ့်မယ်။
1. အမည်အနေဖြင့် **Calculator Agent** ဟု ရိုက်ထည့်ပြီး **Enter** ကိုနှိပ်ပါ။
1. **Agent (Prompt) Builder** မှာ **Model** အကွက်တွင် **OpenAI GPT-4o (via GitHub)** model ကို ရွေးချယ်ပါ။

### -2- Agent အတွက် system prompt တစ်ခု တည်ဆောက်ခြင်း

agent ကို မျှော်မှန်းထားသည့် ထုံးစံနှင့် ရည်ရွယ်ချက်ကို သတ်မှတ်ရန်အချိန် ရောက်ပါပြီ။ ဒီအပိုင်းမှာ **Generate system prompt** လုပ်ဆောင်ချက်ကို အသုံးပြုပြီး calculator agent အဖြစ် သတ်မှတ်ခြင်းနှင့် system prompt ကို model ကိုယ်တိုင် ရေးပေးရန် လုပ်ဆောင်ပါမည်။

![Visual Studio Code အတွက် AI Toolkit တွင် "Calculator Agent" interface မှ screenshot; "Generate a prompt" ဟု ခေါင်းစဉ်ထားသော modal window ဖြင့် ဖွင့်ထားသည်။ အညွှန်းမှာ prompt template တစ်ခုကို အခြေခံအချက်အလက် ဖြန့်ဝေပြီး ဖန်တီးနိုင်ကြောင်း ရှင်းပြသည်။ စာရိုက်ခြင်းအတွင်း "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." ဟု စာသားထည့်ထားသည်။ "Close" နှင့် "Generate" ခလုတ်များပါဝင်သည်။ နောက်ခံတွင် agent configuration ၏ အစိတ်အပိုင်းတချို့ပါဝင်ပြီး "OpenAI GPT-4o (via GitHub)" model ရွေးထားခြင်း၊ system နှင့် user prompts အကွက်များ ပါဝင်သည်။](../../../../translated_images/my/aitk-generate-prompt.ba9e69d3d2bbe2a2.webp)

1. **Prompts** အပိုင်းတွင် **Generate system prompt** ခလုတ်ကို နှိပ်ပါ။ ဒီခလုတ်က AI ကို အသုံးပြု၍ system prompt တစ်ခု ဖန်တီးပေးမည့် prompt builder ကို ဖွင့်ပေးပါလိမ့်မယ်။
1. **Generate a prompt** ပြတင်းပေါ်တွင် အောက်ဖော်ပြပါစာသားကို ရိုက်ထည့်ပါ - `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. **Generate** ခလုတ်ကိုနှိပ်ပါ။ ဒဏ်ငွေပြုလုပ်မှု စတင်သည်ကို အောက်ညာခြမ်း မှာ သတိပေးချက်ပေါ်လာမည်။ ဖန်တီးမှုပြီးသွားပြီးနောက် system prompt သည် **Agent (Prompt) Builder** ၏ **System prompt** အကွက်တွင် ပေါ်လာပါလိမ့်မယ်။
1. **System prompt** ကို ပြန်လည်ဆန်းစစ်ပြီး လိုအပ်ရင် ပြင်ဆင်ပါ။

### -3- MCP server တစ်ခုတည်ဆောက်ခြင်း

agent ၏ system prompt ကို သတ်မှတ်ပြီးနောက် သုံးစွဲနိုင်မှုရှိအောင် နောက်ထပ်အင်အားဖွဲ့စည်းပေးရမည်။ ဒီအပိုင်းအတွင်း calculator MCP server တစ်ခုကို ဖန်တီးပြီး တွက်ချက်မှု tools တွေဖြင့် လုပ်ဆောင်ခွင့် ပေးမည်ဖြစ်သည်။ ဒီ server က ရိုးရှင်းသော arithmetic operations တွေကို ရိုးရိုးဘာသာစကား prompt များဖြင့် ချက်ချင်း ပြုလုပ်နိုင်အောင်ပြုလုပ်ပေးပါလိမ့်မယ်။

![Visual Studio Code ၏ AI Toolkit extension တွင် Calculator Agent interface ၏ အောက်ဆုံးပိုင်း screenshot ဖြစ်ပြီး “Tools” နှင့် “Structure output” ကို ဖြည့်ချင်သည့် ဆက်လက်အသေးစိတ်ဖွင့်လှစ်ရန် menu များ၊ “Choose output format” dropdown menu ကို “text” ဟု သတ်မှတ်ထားသည်။ ညာဘက်တွင် “+ MCP Server” ခလုတ်ပါရှိပြီး Model Context Protocol server ထည့်ရန် ဖြစ်သည်။ Tools အပေါ်တွင် ဓာတ်ပုံ icon placeholder ဖော်ပြထားသည်။](../../../../translated_images/my/aitk-add-mcp-server.9742cfddfe808353.webp)

AI Toolkit သည် သင့်အား MCP server ကို လုပ်ဆောင်ရန် templates အသုံးပြုရန် အဆင်ပြေပြီ။ calculator MCP server  ဖန်တီးရန် Python template ကို အသုံးပြုမည်။

*မှတ်ချက်* - AI Toolkit သည် လတ်တလောတွင် Python နှင့် TypeScript ကိုပင် အထောက်အပံ့ ပေးနေပါသည်။

1. **Agent (Prompt) Builder** ၏ **Tools** အပိုင်းမှာ **+ MCP Server** ခလုတ်ကိုနှိပ်ပါ။ **Command Palette** မှ setup wizard ကိုဖွင့်ပေးမည်။
1. **+ Add Server** ကိုရွေးပါ။
1. **Create a New MCP Server** ကိုရွေးပါ။
1. template အနေနဲ့ **python-weather** ကိုရွေးပါ။
1. MCP server template ကို သိမ်းထားမယ့် folder အနေဖြင့် **Default folder** ကိုရွေးပါ။
1. server အမည်အနေဖြင့် **Calculator** ဟူ၍ရိုက်ထည့်ပါ။
1. Visual Studio Code window အသစ် ဖွင့်ပါမည်။ **Yes, I trust the authors** ကိုရွေးပါ။
1. terminal တွင် virtual environment တည်ဆောက်ရန် `python -m venv .venv` ဟုရိုက်ပါ။
1. terminal က virtual environment ကို ဖွင့်ပါ -
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. terminal ကdependencies များ install လုပ်ပါ - `pip install -e .[dev]`
1. **Explorer** မှ **src** directory ကို ချဲ့ပြီး **server.py** ကို editor မှာ ဖွင့်ပါ။
1. **server.py** ဖိုင်၏ code ကို အောက်ပါအတိုင်းကူးပြောင်းပြီး သိမ်းပါ။

    ```python
    """
    Sample MCP Calculator Server implementation in Python.

    
    This module demonstrates how to create a simple MCP server with calculator tools
    that can perform basic arithmetic operations (add, subtract, multiply, divide).
    """
    
    from mcp.server.fastmcp import FastMCP
    
    server = FastMCP("calculator")
    
    @server.tool()
    def add(a: float, b: float) -> float:
        """Add two numbers together and return the result."""
        return a + b
    
    @server.tool()
    def subtract(a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    @server.tool()
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers together and return the result."""
        return a * b
    
    @server.tool()
    def divide(a: float, b: float) -> float:
        """
        Divide a by b and return the result.
        
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    ```

### -4- calculator MCP server နှင့် agent ကို run စမ်းသပ်ခြင်း

agent မှ tools များ ရှိပြီဖြစ်တာနဲ့ ချက်ချင်းအသုံးပြုနိုင်ပြီ! ဒီအပိုင်းမှာ agent ကို prompt ပေးပြီး calculator MCP server မှ tool ကို သုံးနိုင်မရုံသာမက စမ်းသပ် အတည်ပြုသွားပါမည်။

![Visual Studio Code ၏ AI Toolkit extension တွင် Calculator Agent interface မှ screenshot။ ဘက်စင်ပANEL မှာ “Tools” အောက်တွင် local-server-calculator_server MCP server တစ်ခု ပါရှိပြီး add, subtract, multiply, divide ဆိုတဲ့ tools ၄ ခု ထည့်ထားသည်၊ tool ၄ ခုလုံး လှုပ်ရှားသည်ဟူသော badge ပါဝင်သည်။ Structure output ကိုဖွင့်နေပြီး Run ခလုတ်ကအပေါ်ပါတာဖြစ်သည်။ ညာဘက် panel တွင် Model Response အောက်မှ agent သည် multiply နှင့် subtract tools များကို input {"a": 3, "b": 25} နှင့် {"a": 75, "b": 20} ဖြင့် အသုံးပြုလျက်ရှိသည်။ τελικό Tool Response ကို 75.0 ဟု ပြသထားသည်။ မူလ code ကြည့်ခြင်းခလုတ်ပုံစံ ပါဝင်သည်။](../../../../translated_images/my/aitk-agent-response-with-tools.e7c781869dc8041a.webp)

local development machine တွင် MCP client အနေဖြင့် **Agent Builder** ကို run လိုက်ပါမည်။

1. `F5` ကီးနှိပ်ပြီး MCP server ကို debugging အဖြစ် စတင်ပါ။ **Agent (Prompt) Builder** သည် editor tab အသစ်မှ ဖွင့်ပါလိမ့်မယ်။ terminal မှာ server status ကို ကြည့်ရှုနိုင်ပါသည်။
1. **Agent (Prompt) Builder** ၏ **User prompt** အကွက်တွင် နမူနာ prompt `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?` ဟု ရိုက်ထည့်ပါ။
1. **Run** ခလုတ်ကို နှိပ်၍ agent ၏ ပြန်လည်ဖြေကြားမှုကို ဖန်တီးပါ။
1. agent output ကို ပြန်လည်လေ့လာပါ။ model က သင် **$55** ပေးခဲ့တယ်ဟု သတ်မှတ်ရမည်။
1. ဖြစ်ပေါ်သင့်တာ တွေကို ခွဲခြမ်းစိတ်ဖြာပါ -
    - agent က **multiply** နှင့် **subtract** tools များကို အသုံးပြုမှုအတွက် ရွေးချယ်သည်။
    - **multiply** tool ၏ `a` နှင့် `b` အတူတကွ သတ်မှတ်သည်။
    - **subtract** tool ၏ `a` နှင့် `b` အတူတကွ သတ်မှတ်သည်။
    - တစ်ခုချင်းစီ tool မှ ပြန်လာသည့် output ကို **Tool Response** တွင် ပေးအပ်သည်။
    - model ၏ နောက်ဆုံး output ကို **Model Response** အတွင်း သာမာန်ပြသသည်။
1. agent ကို စမ်းသပ်ရန် ဒါထက်ပို prompt များ ပေးရန် ရွေးချယ်နိုင်ပြီး **User prompt** အကွက်အတွင်း ပြင်ဆင်နိုင်သည်။
1. စမ်းသပ်မှုများပြီးနောက် server ကို **terminal** မှ **CTRL/CMD+C** နှိပ်ကာ ရပ်တန့်နိုင်ပါသည်။

## တာဝန်ပေးချက်

**server.py** ဖိုင်ထဲ သို့ အသစ် tool တစ်ခု (ဥပမာ - ဂဏန်း တစ်ခု၏ စတုရန်းမွေး ထုတ်ရန်) ထပ်ထည့်ပါ။ tool အသစ် ကို အသုံးပြုရန် များ ပြုလုပ်သော prompt တွေ ပေးပြီး agent ကို စမ်းသပ်ပါ။ အသစ်ထည့်ထား tool များ load လုပ်ရန် server ကို ပြန်စတင်ရန် မမေ့ပါနှင့်။

## ဖြေရှင်းချက်

[ဖြေရှင်းချက်](./solution/README.md)

## အဓိက သင်ယူရမည့် အချက်များ

ဒီခန်းစာမှ သင်ယူရမည့် အချက်များမှာ -

- AI Toolkit extension သည် MCP Servers များနှင့် သူတို့ရဲ့ tools များကို စားသုံးနိုင်စေသော client ကြီးတစ်ခု ဖြစ်သည်။
- MCP servers များထဲသို့ အသစ် tools များထည့်ကာ agent ၏ စွမ်းဆောင်ရည်များအား တိုးမြှင့်နိုင်သည်။
- AI Toolkit တွင် (ဥပမာ - Python MCP server templates) ကဲ့သို့သော template များပါဝင်ပြီး custom tools ဖန်တီးမှုအတွက် လွယ်ကူစေပါသည်။

## ပိုမိုသိရှိလိုသည့်အရာများ

- [AI Toolkit စာရွက်စာတမ်းများ](https://aka.ms/AIToolkit/doc)

## ဘာတွေဖြစ်လာမလဲ
- နောက်တစ်ဆင့်: [စမ်းသပ်ခြင်း & ပြင်ဆင်ခြင်း](../08-testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->