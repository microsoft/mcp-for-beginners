# Visual Studio Code အတွက် AI Toolkit Extension မှ Server ကို အသုံးပြုခြင်း

AI Agent တစ်ခုကို တည်ဆောက်တဲ့အခါမှာ၊ ရှင်းလင်းတဲ့ အဖြေတွေကို ဖန်တီးပေးရုံသာမက၊ Agent ကို လုပ်ဆောင်နိုင်စွမ်းပေးဖို့လည်း အရေးကြီးပါတယ်။ Model Context Protocol (MCP) က ဒီအပိုင်းမှာ အထောက်အကူပေးနိုင်ပါတယ်။ MCP က Agent တွေကို အပြင် Tools နဲ့ Services တွေကို တစ်စည်းတစ်လုံးနဲ့ အဆင်ပြေပြေ အသုံးပြုနိုင်အောင် လုပ်ပေးပါတယ်။ ဒါကို Agent ကို အသုံးပြုနိုင်တဲ့ Toolbox တစ်ခုလို ထင်ရပါတယ်။

ဥပမာအားဖြင့် Calculator MCP Server ကို Agent နဲ့ ချိတ်ဆက်လိုက်မယ်ဆိုရင်၊ Agent က “47 ကို 89 နဲ့ မကြိမ်ဘူး?” ဆိုတဲ့ Prompt ရုံနဲ့ Math Operations တွေကို လုပ်ဆောင်နိုင်ပါပြီ။ Logic တွေကို Hardcode လုပ်ရတာမလိုတော့ဘဲ၊ Custom APIs တွေကို တည်ဆောက်ရတာလည်း မလိုတော့ပါဘူး။

## အကျဉ်းချုပ်

ဒီသင်ခန်းစာမှာ Calculator MCP Server ကို Visual Studio Code ရဲ့ [AI Toolkit](https://aka.ms/AIToolkit) Extension နဲ့ Agent နဲ့ ချိတ်ဆက်ပေးပြီး၊ Natural Language ကို အသုံးပြုကာ အပေါင်း၊ အနုတ်၊ အမြှောက်၊ အခွဲ စတဲ့ Math Operations တွေကို လုပ်ဆောင်နိုင်အောင် လုပ်ပေးမယ်။

AI Toolkit က Visual Studio Code အတွက် အင်အားကြီးတဲ့ Extension တစ်ခုဖြစ်ပြီး Agent Development ကို လွယ်ကူစေပါတယ်။ AI Engineers တွေက Generative AI Models တွေကို Local မှာဖြစ်စေ၊ Cloud မှာဖြစ်စေ တည်ဆောက်ပြီး စမ်းသပ်နိုင်ပါတယ်။ ဒီ Extension က ယနေ့မှာ ရရှိနိုင်တဲ့ Generative Models အများစုကို Support လုပ်ပေးပါတယ်။

*မှတ်ချက်*: AI Toolkit က Python နဲ့ TypeScript ကို Support လုပ်ပါတယ်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာအဆုံးမှာ သင်တတ်မြောက်မည့်အရာများမှာ:

- AI Toolkit ကို အသုံးပြုကာ MCP Server ကို အသုံးချနိုင်ခြင်း။
- MCP Server မှ Tools တွေကို ရှာဖွေပြီး အသုံးပြုနိုင်အောင် Agent Configuration ကို Configure လုပ်ခြင်း။
- Natural Language ကို အသုံးပြုကာ MCP Tools တွေကို အသုံးချနိုင်ခြင်း။

## လုပ်ဆောင်ရန် နည်းလမ်း

အထွေထွေ အဆင့်မြင့်နည်းလမ်းအနေနဲ့ ဒီလိုလုပ်ဆောင်ရပါမယ်:

- Agent တစ်ခုကို ဖန်တီးပြီး System Prompt ကို သတ်မှတ်ပါ။
- Calculator Tools တွေပါဝင်တဲ့ MCP Server တစ်ခုကို ဖန်တီးပါ။
- Agent Builder ကို MCP Server နဲ့ ချိတ်ဆက်ပါ။
- Natural Language ကို အသုံးပြုကာ Agent ရဲ့ Tool Invocation ကို စမ်းသပ်ပါ။

အိုကေ၊ အခုတော့ Flow ကို နားလည်ပြီးပြီဆိုရင်၊ MCP ကို အသုံးပြုကာ AI Agent ရဲ့ လုပ်ဆောင်နိုင်စွမ်းတွေကို တိုးမြှင့်ဖို့ Configure လုပ်လိုက်ရအောင်!

## မလိုမုန်းလိုအပ်ချက်များ

- [Visual Studio Code](https://code.visualstudio.com/)
- [Visual Studio Code အတွက် AI Toolkit](https://aka.ms/AIToolkit)

## လေ့ကျင့်ခန်း: Server ကို အသုံးပြုခြင်း

> [!WARNING]
> macOS အသုံးပြုသူများအတွက် မှတ်ချက်။ Dependency Installation ကို ထိခိုက်စေတဲ့ ပြဿနာတစ်ခုကို လေ့လာနေဆဲဖြစ်ပါတယ်။ ဒီအကြောင်းကြောင့် macOS အသုံးပြုသူများသည် ဒီ Tutorial ကို လက်ရှိအချိန်မှာ ပြီးမြောက်စွာ လုပ်ဆောင်နိုင်မှာ မဟုတ်ပါဘူး။ ပြဿနာကို ဖြေရှင်းပြီး Instruction တွေကို Update လုပ်သွားမယ်။ သင့်ရဲ့ သည်းခံမှုနဲ့ နားလည်မှုအတွက် ကျေးဇူးတင်ပါတယ်။

ဒီလေ့ကျင့်ခန်းမှာ သင် AI Agent တစ်ခုကို MCP Server မှ Tools တွေကို အသုံးပြုကာ Visual Studio Code ရဲ့ AI Toolkit မှာ Build, Run, နဲ့ Enhance လုပ်ပါမယ်။

### -0- Prestep, OpenAI GPT-4o Model ကို My Models မှာ ထည့်ပါ

ဒီလေ့ကျင့်ခန်းမှာ **GPT-4o** Model ကို အသုံးပြုပါမယ်။ Agent ကို ဖန်တီးမီ **My Models** မှာ Model ကို ထည့်ထားရပါမယ်။

![Visual Studio Code ရဲ့ AI Toolkit Extension မှ Model Selection Interface ရဲ့ Screenshot။ Heading က "Find the right model for your AI Solution" လို့ ရေးထားပြီး Subtitle က "Discover, test, and deploy AI models" လို့ ရေးထားပါတယ်။ Popular Models အောက်မှာ DeepSeek-R1 (GitHub-hosted), OpenAI GPT-4o, OpenAI GPT-4.1, OpenAI o1, Phi 4 Mini (CPU - Small, Fast), နဲ့ DeepSeek-R1 (Ollama-hosted) Model Cards ၆ ခုကို ပြထားပါတယ်။ Model Card တစ်ခုစီမှာ "Add" နဲ့ "Try in Playground" Options တွေ ပါဝင်ပါတယ်။](../../../../translated_images/my/aitk-model-catalog.2acd38953bb9c119aa629fe74ef34cc56e4eed35e7f5acba7cd0a59e614ab335.png)

1. **Activity Bar** မှ **AI Toolkit** Extension ကို ဖွင့်ပါ။
1. **Catalog** အပိုင်းမှာ **Models** ကို ရွေးပြီး **Model Catalog** ကို ဖွင့်ပါ။ **Models** ကို ရွေးလိုက်တာနဲ့ **Model Catalog** ကို Editor Tab အသစ်မှာ ဖွင့်ပါမယ်။
1. **Model Catalog** ရဲ့ Search Bar မှာ **OpenAI GPT-4o** လို့ ရိုက်ထည့်ပါ။
1. **+ Add** ကို Click လုပ်ပြီး Model ကို **My Models** List မှာ ထည့်ပါ။ **Hosted by GitHub** Model ကို ရွေးထားတာကို သေချာပါစေ။
1. **Activity Bar** မှာ **OpenAI GPT-4o** Model က List မှာ ပါဝင်နေတဲ့အကြောင်းကို အတည်ပြုပါ။

### -1- Agent တစ်ခုကို ဖန်တီးပါ

**Agent (Prompt) Builder** က သင့်ကို AI-powered Agent ကို ဖန်တီးပြီး Customize လုပ်နိုင်စေပါတယ်။ ဒီအပိုင်းမှာ သင် Agent အသစ်တစ်ခုကို ဖန်တီးပြီး Conversation ကို အင်အားပေးမယ့် Model ကို Assign လုပ်ပါမယ်။

![Visual Studio Code ရဲ့ AI Toolkit Extension မှ Calculator Agent Builder Interface ရဲ့ Screenshot။ ဘယ် Panel မှာ "OpenAI GPT-4o (via GitHub)" Model ကို ရွေးထားပြီး System Prompt က "You are a professor in university teaching math" လို့ ရေးထားပါတယ်။ User Prompt က "Explain to me the Fourier equation in simple terms" လို့ ရေးထားပါတယ်။ Tools ထည့်ရန် Button, MCP Server Enable လုပ်ရန် Option, Structured Output ရွေးရန် Option တွေ ပါဝင်ပါတယ်။ အောက်ဆုံးမှာ Blue Color ရဲ့ “Run” Button တစ်ခုရှိပါတယ်။ ညာ Panel မှာ "Get Started with Examples" အောက်မှာ Web Developer, Second-Grade Simplifier, နဲ့ Dream Interpreter ဆိုတဲ့ Sample Agents ၃ ခုကို ဖော်ပြထားပြီး အတိုင်းအတာဖော်ပြချက်တွေ ပါဝင်ပါတယ်။](../../../../translated_images/my/aitk-agent-builder.901e3a2960c3e4774b29a23024ff5bec2d4232f57fae2a418b2aaae80f81c05f.png)

1. **Activity Bar** မှ **AI Toolkit** Extension ကို ဖွင့်ပါ။
1. **Tools** အပိုင်းမှာ **Agent (Prompt) Builder** ကို ရွေးပါ။ **Agent (Prompt) Builder** ကို ရွေးလိုက်တာနဲ့ **Agent (Prompt) Builder** ကို Editor Tab အသစ်မှာ ဖွင့်ပါမယ်။
1. **+ New Agent** Button ကို Click လုပ်ပါ။ Extension က **Command Palette** မှာ Setup Wizard ကို Launch လုပ်ပါမယ်။
1. **Calculator Agent** ဆိုတဲ့ နာမည်ကို ရိုက်ထည့်ပြီး **Enter** ကို နှိပ်ပါ။
1. **Agent (Prompt) Builder** မှာ **Model** Field အတွက် **OpenAI GPT-4o (via GitHub)** Model ကို ရွေးပါ။

### -2- Agent အတွက် System Prompt တစ်ခုကို ဖန်တီးပါ

Agent ကို Scaffold လုပ်ပြီးပြီဆိုရင်၊ အခုတော့ Personality နဲ့ ရည်ရွယ်ချက်ကို သတ်မှတ်ရမယ်။ ဒီအပိုင်းမှာ **Generate system prompt** Feature ကို အသုံးပြုကာ Calculator Agent ရဲ့ အပြုအမူကို ဖော်ပြတဲ့ System Prompt ကို Model ကို အသုံးပြုပြီး Generate လုပ်ပါမယ်။

![Visual Studio Code ရဲ့ AI Toolkit မှ Calculator Agent Interface ရဲ့ Screenshot။ Modal Window တစ်ခုဖွင့်ထားပြီး Title က "Generate a prompt" လို့ ရေးထားပါတယ်။ Modal Window မှာ Prompt Template ကို Generate လုပ်ဖို့ Basic Details တွေကို Share လုပ်ဖို့ ရေးထားပြီး Text Box မှာ "You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result." ဆိုတဲ့ Sample System Prompt ရေးထားပါတယ်။ Text Box အောက်မှာ "Close" နဲ့ "Generate" Buttons တွေ ပါဝင်ပါတယ်။ Background မှာ Agent Configuration ရဲ့ အစိတ်အပိုင်းတစ်ခုကို ဖော်ပြထားပြီး Selected Model က "OpenAI GPT-4o (via GitHub)" ဖြစ်ပါတယ်။](../../../../translated_images/my/aitk-generate-prompt.ba9e69d3d2bbe2a26444d0c78775540b14196061eee32c2054e9ee68c4f51f3a.png)

1. **Prompts** အပိုင်းအတွက် **Generate system prompt** Button ကို Click လုပ်ပါ။ ဒီ Button က Prompt Builder ကို ဖွင့်ပြီး Agent အတွက် System Prompt ကို Generate လုပ်ပေးမယ်။
1. **Generate a prompt** Window မှာ အောက်ပါကို ရိုက်ထည့်ပါ: `You are a helpful and efficient math assistant. When given a problem involving basic arithmetic, you respond with the correct result.`
1. **Generate** Button ကို Click လုပ်ပါ။ Prompt ကို Generate လုပ်နေတဲ့အကြောင်းကို အောက်ခြေ Right Corner မှာ Notification တစ်ခု ပေါ်လာပါမယ်။ Prompt Generation ပြီးဆုံးတာနဲ့ Prompt ကို **Agent (Prompt) Builder** ရဲ့ **System prompt** Field မှာ ပြပါမယ်။
1. **System prompt** ကို ပြန်လည်ကြည့်ပြီး လိုအပ်ပါက ပြင်ဆင်ပါ။

### -3- MCP Server တစ်ခုကို ဖန်တီးပါ

Agent ရဲ့ System Prompt ကို သတ်မှတ်ပြီးပြီ—Agent ရဲ့ အပြုအမူနဲ့ အဖြေတွေကို လမ်းညွှန်ပေးတဲ့အခါ—အခုတော့ Agent ကို လက်တွေ့အသုံးချနိုင်စွမ်းတွေ ပေးဖို့ အချိန်ရောက်ပါပြီ။ ဒီအပိုင်းမှာ Addition, Subtraction, Multiplication, နဲ့ Division Calculations တွေကို လုပ်ဆောင်နိုင်တဲ့ Tools တွေပါဝင်တဲ့ Calculator MCP Server တစ်ခုကို ဖန်တီးပါမယ်။ ဒီ Server က Natural Language Prompts တွေကို ဖြေရှင်းဖို့ Agent ကို အချိန်နှင့်တပြေးညီ Math Operations တွေ လုပ်ဆောင်နိုင်စေပါမယ်။

![Visual Studio Code ရဲ့ AI Toolkit Extension မှ Calculator Agent Interface ရဲ့ Screenshot။ Tools နဲ့ Structure Output ဆိုတဲ့ Expandable Menus တွေကို ပြထားပြီး “Choose output format” Dropdown Menu ကို “text” အဖြစ် ရွေးထားပါတယ်။ MCP Server ထည့်ရန် Button ကို “+ MCP Server” လို့ Label လုပ်ထားပြီး Tools Section အပေါ်မှာ Image Icon Placeholder တစ်ခုကို ပြထားပါတယ်။](../../../../translated_images/my/aitk-add-mcp-server.9742cfddfe808353c0caf9cc0a7ed3e80e13abf4d2ebde315c81c3cb02a2a449.png)

AI Toolkit မှ Templates တွေကို အသုံးပြုကာ MCP Server ကို လွယ်ကူစွာ ဖန်တီးနိုင်ပါတယ်။ Calculator MCP Server ကို ဖန်တီးဖို့ Python Template ကို အသုံးပြုပါမယ်။

*မှတ်ချက်*: AI Toolkit က Python နဲ့ TypeScript ကို Support လုပ်ပါတယ်။

1. **Agent (Prompt) Builder** ရဲ့ **Tools** အပိုင်းမှာ **+ MCP Server** Button ကို Click လုပ်ပါ။ Extension က **Command Palette** မှာ Setup Wizard ကို Launch လုပ်ပါမယ်။
1. **+ Add Server** ကို ရွေးပါ။
1. **Create a New MCP Server** ကို ရွေးပါ။
1. Template အတွက် **python-weather** ကို ရွေးပါ။
1. Template ကို Save လုပ်ဖို့ **Default folder** ကို ရွေးပါ။
1. Server အတွက် အောက်ပါနာမည်ကို ရိုက်ထည့်ပါ: **Calculator**
1. Visual Studio Code Window အသစ်တစ်ခု ဖွင့်ပါမယ်။ **Yes, I trust the authors** ကို ရွေးပါ။
1. **Terminal** (**Terminal** > **New Terminal**) ကို အသုံးပြုကာ Virtual Environment တစ်ခုကို ဖန်တီးပါ: `python -m venv .venv`
1. **Terminal** ကို အသုံးပြုကာ Virtual Environment ကို Activate လုပ်ပါ:
    1. Windows - `.venv\Scripts\activate`
    1. macOS/Linux - `source .venv/bin/activate`
1. **Terminal** ကို အသုံးပြုကာ Dependencies တွေကို Install လုပ်ပါ: `pip install -e .[dev]`
1. **Activity Bar** ရဲ့ **Explorer** View မှာ **src** Directory ကို Expand လုပ်ပြီး **server.py** ကို ရွေးကာ File ကို Editor မှာ ဖွင့်ပါ။
1. **server.py** File ရဲ့ Code ကို အောက်ပါ Code နဲ့ Replace လုပ်ပြီး Save လုပ်ပါ:

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

### -4- Calculator MCP Server နဲ့ Agent ကို Run လုပ်ပါ

Agent ရဲ့ Tools တွေကို အသုံးပြုဖို့ အချိန်ရောက်ပါပြီ! ဒီအပိုင်းမှာ Agent ကို Prompt တွေ ပေးပြီး Calculator MCP Server မှ Tools တွေကို အသုံးပြုနိုင်မလား စမ်းသပ်ပါမယ်။

![Visual Studio Code ရဲ့ AI Toolkit Extension မှ Calculator Agent Interface ရဲ့ Screenshot။ ဘယ် Panel မှာ Tools အောက်မှာ local-server-calculator_server ဆိုတဲ့ MCP Server တစ်ခုကို ထည့်ထားပြီး Tools ၄ ခု (add, subtract, multiply, divide) ကို ပြထားပါတယ်။ Tools ၄ ခု Active ဖြစ်နေတဲ့အကြောင်းကို Badge တစ်ခုနဲ့ ပြထားပါတယ်။ Structure Output Section ကို Collapse လုပ်ထားပြီး Blue Color ရဲ့ “Run” Button တစ်ခုရှိပါတယ်။ ညာ Panel မှာ Model Response အောက်မှာ Agent က multiply နဲ့ subtract Tools တွေကို {"a": 3, "b": 25} နဲ့ {"a": 75, "b": 20} Inputs တွေဖြင့် Invoke လုပ်ထားပါတယ်။ နောက်ဆုံး Tool Response က 75.0 ဖြစ်ပါတယ်။ အောက်ဆုံးမှာ “View Code” Button တစ်ခုရှိပါတယ်။](../../../../translated_images/my/aitk-agent-response-with-tools.e7c781869dc8041a25f9903ed4f7e8e0c7e13d7d94f6786a6c51b1e172f56866.png)

သင့် Local Dev Machine မှ Calculator MCP Server ကို **Agent Builder** မှ MCP Client အဖြစ် Run လုပ်ပါမယ်။

1. MCP Server ကို Debugging စတင်ဖို့ `F5` ကို နှိပ်ပါ။ **Agent (Prompt) Builder** ကို Editor Tab အသစ်မှာ ဖွင့်ပါမယ်။ Server ရဲ့ Status ကို Terminal မှာ မြင်နိုင်ပါမယ်။
1. **Agent (Prompt) Builder** ရဲ့ **User prompt** Field မှာ အောက်ပါ Prompt ကို ရိုက်ထည့်ပါ: `I bought 3 items priced at $25 each, and then used a $20 discount. How much did I pay?`
1. **Run** Button ကို Click လုပ်ပြီး Agent ရဲ့ Response ကို Generate လုပ်ပါ။
1. Agent Output ကို ပြန်လည်ကြည့်ပါ။ Model က သင့်အတွက် **$55** ပေးခဲ့တယ်လို့ အတည်ပြုသင့်ပါတယ်။
1. အောက်ပါအတိုင်း ဖြစ်ရပါမယ်:
    - Agent က Calculation အတွက် **multiply** နဲ့ **subtract** Tools တွေကို ရွေးချယ်ပါမယ်။
    - **multiply** Tool အတွက် `a` နဲ့ `b` Values တွေကို Assign လုပ်ပါမယ်။
    - **subtract** Tool အတွက် `a` နဲ့ `b` Values တွေကို Assign လုပ်ပါမယ်။
    - Tool Response တစ်ခုစီကို **Tool Response** Section မှာ ပြပါမယ်။
    - Model Response ကို **Model Response** Section မှာ ပြပါမယ်။
1. Agent ကို ထပ်မံစမ်းသပ်ဖို့ Prompt အသစ်တွေကို Submit လုပ်ပါ။ **User prompt** Field မှာ ရှိတဲ့ Prompt ကို Click လုပ်ပြီး အစားထိုးပါ။
1. Agent ကို စမ်းသပ်ပြီးပြီဆိုရင် Server ကို **Terminal** မှာ **CTRL/CMD+C** ရိုက်ထည့်ကာ Quit လုပ်နိုင်ပါတယ်။

## လုပ်ဆောင်ရန်

**server.py** File မှာ Tool Entry အသစ်တစ်ခု (ဥပမာ: နံပါတ်တစ်ခုရဲ့ Square Root ကို Return ပြန်ပေးခြင်း) ထည့်ဖို့ ကြိုးစားပါ။ Agent ကို သင့် Tool အသစ် (သို့) ရှိပြီးသား Tools တွေကို အသုံးပြုဖို့ လိုအပ်တဲ့ Prompt တွေကို Submit လုပ်ပါ။ Tools အသစ်တွေကို Load လုပ်ဖို့ Server ကို Restart လုပ်ဖို့ မမေ့ပါနှင့်။

## ဖြေရှင်းချက်

[Solution](./solution/README.md)

## အဓိက Takeaways

ဒီ Chapter ရဲ့ Takeaways တွေမှာ အောက်ပါအရာတွေ ပါဝင်ပါတယ်:

- AI Toolkit Extension က MCP Servers နဲ့ Tools တွေကို အသုံးပြုနိုင်တဲ့ Client အလွန်ကောင်းတစ်ခုဖြစ်ပါတယ်။
- MCP Servers မှ Tools အသစ်တွေကို ထည့်နိုင်ပြီး Agent ရဲ့ လုပ်ဆောင်နိုင်စွမ်းတွေကို တိုးမြှင့်နိုင်ပါတယ်။
- AI Toolkit မှ Templates (ဥပမာ: Python MCP Server Templates) တွေက Custom Tools တွေကို ဖန်တီးဖို့ လွယ်ကူစေပါတယ်။

## အပိုဆောင်း Resources

- [AI Toolkit docs](https://aka.ms/AIToolkit/doc)

## အခုန

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပြန်ဆိုမှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပါယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။