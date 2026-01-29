## စတင်ခြင်း  

[![သင့်ရဲ့ ပထမဆုံး MCP Server တည်ဆောက်ခြင်း](../../../translated_images/my/04.0ea920069efd979a0b2dad51e72c1df7ead9c57b3305796068a6cee1f0dd6674.png)](https://youtu.be/sNDZO9N4m9Y)

_(အပေါ်ရှိ ပုံကို နှိပ်ပြီး ဒီသင်ခန်းစာရဲ့ ဗီဒီယိုကို ကြည့်ပါ)_

ဒီအပိုင်းမှာ သင်ခန်းစာအတော်များများ ပါဝင်ပါတယ်။

- **1 သင့်ရဲ့ ပထမဆုံး server**၊ ဒီပထမဆုံး သင်ခန်းစာမှာ သင်ရဲ့ ပထမဆုံး server ကို ဘယ်လိုတည်ဆောက်ရမယ်ဆိုတာ သင်ယူပြီး၊ server ကို စမ်းသပ်ခြင်းနှင့် အမှားရှာဖွေခြင်းအတွက် အသုံးဝင်တဲ့ inspector tool ကို အသုံးပြုပါမယ်။ [သင်ခန်းစာကို သွားရန်](01-first-server/README.md)

- **2 Client**၊ ဒီသင်ခန်းစာမှာ သင်ရဲ့ server ကို ချိတ်ဆက်နိုင်တဲ့ client ကို ဘယ်လိုရေးရမယ်ဆိုတာ သင်ယူပါမယ်။ [သင်ခန်းစာကို သွားရန်](02-client/README.md)

- **3 Client with LLM**၊ client ကို ပိုမိုကောင်းမွန်စွာရေးသားဖို့ LLM ကို ထည့်သွင်းပြီး server နဲ့ "ညှိနှိုင်း" လုပ်နိုင်အောင် ပြုလုပ်ပါမယ်။ [သင်ခန်းစာကို သွားရန်](03-llm-client/README.md)

- **4 Visual Studio Code မှာ GitHub Copilot Agent mode နဲ့ server ကို အသုံးပြုခြင်း**။ ဒီနေရာမှာ MCP Server ကို Visual Studio Code မှာ အလုပ်လုပ်အောင် ပြုလုပ်ပါမယ်။ [သင်ခန်းစာကို သွားရန်](04-vscode/README.md)

- **5 stdio Transport Server** stdio transport သည် MCP server-to-client ဆက်သွယ်မှုအတွက် လက်ရှိ specification မှာ အကြံပြုထားတဲ့ စံနည်းဖြစ်ပြီး subprocess-based ဆက်သွယ်မှုကို လုံခြုံစွာပေးစွမ်းပါသည်။ [သင်ခန်းစာကို သွားရန်](05-stdio-server/README.md)

- **6 MCP နဲ့ HTTP Streaming (Streamable HTTP)**။ ခေတ်မီ HTTP streaming, progress notifications, နှင့် Streamable HTTP ကို အသုံးပြုပြီး MCP servers နှင့် clients ကို scalable, real-time အဖြစ် တည်ဆောက်နည်းကို သင်ယူပါမယ်။ [သင်ခန်းစာကို သွားရန်](06-http-streaming/README.md)

- **7 VSCode အတွက် AI Toolkit ကို အသုံးပြုခြင်း** MCP Clients နှင့် Servers ကို စမ်းသပ်ရန်နှင့် အသုံးပြုရန် [သင်ခန်းစာကို သွားရန်](07-aitk/README.md)

- **8 စမ်းသပ်ခြင်း**။ ဒီနေရာမှာ server နှင့် client ကို အမျိုးမျိုးသောနည်းလမ်းများဖြင့် စမ်းသပ်နည်းကို အထူးအာရုံစိုက်ပါမယ်။ [သင်ခန်းစာကို သွားရန်](08-testing/README.md)

- **9 Deployment**။ ဒီအခန်းမှာ MCP solutions များကို တင်သွင်းနည်းလမ်းများကို လေ့လာပါမယ်။ [သင်ခန်းစာကို သွားရန်](09-deployment/README.md)

- **10 Server ကို အဆင့်မြင့်အသုံးပြုခြင်း**။ ဒီအခန်းမှာ server ကို အဆင့်မြင့်အသုံးပြုနည်းများကို လေ့လာပါမယ်။ [သင်ခန်းစာကို သွားရန်](./10-advanced/README.md)

- **11 Auth**။ ဒီအခန်းမှာ Basic Auth မှစပြီး JWT နှင့် RBAC ကို အသုံးပြုခြင်းအထိ ရိုးရှင်းသော auth ကို ထည့်သွင်းနည်းကို လေ့လာပါမယ်။ သင်ဦးစွာ ဒီနေရာမှာ စတင်ပြီး အခန်း 5 မှ Advanced Topics ကို ကြည့်ပါ။ အခန်း 2 မှ အကြံပြုချက်များကို အသုံးပြုပြီး လုံခြုံရေးကို ထပ်မံခိုင်မာစေပါ။ [သင်ခန်းစာကို သွားရန်](./11-simple-auth/README.md)

Model Context Protocol (MCP) သည် LLMs ကို context ပေးရန် application များအတွက် စံနည်းဖြစ်စေသော open protocol တစ်ခုဖြစ်သည်။ MCP ကို AI applications အတွက် USB-C port တစ်ခုလို စဉ်းစားပါ - ဒါဟာ AI models ကို အမျိုးမျိုးသော data sources နှင့် tools များနှင့် ချိတ်ဆက်ရန် စံနည်းဖြစ်စေသည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာအဆုံးမှာ သင်တတ်မြောက်မည့်အရာများမှာ -

- C#, Java, Python, TypeScript, နှင့် JavaScript အတွက် MCP development environments ကို စတင်တပ်ဆင်ခြင်း
- resources, prompts, နှင့် tools များကို custom features ဖြင့် MCP servers တည်ဆောက်ခြင်းနှင့် တင်သွင်းခြင်း
- MCP servers ကို ချိတ်ဆက်နိုင်သော host applications တည်ဆောက်ခြင်း
- MCP implementations များကို စမ်းသပ်ခြင်းနှင့် အမှားရှာဖွေခြင်း
- အများဆုံးတွေ့ရသော setup အခက်အခဲများနှင့် ၎င်းတို့၏ ဖြေရှင်းနည်းများကို နားလည်ခြင်း
- MCP implementations များကို လူကြိုက်များသော LLM services များနှင့် ချိတ်ဆက်ခြင်း

## MCP Environment ကို စတင်တပ်ဆင်ခြင်း

MCP နဲ့ အလုပ်လုပ်မည်မတိုင်မီ သင့် development environment ကို ပြင်ဆင်ပြီး အခြေခံ workflow ကို နားလည်ထားဖို့ အရေးကြီးပါတယ်။ ဒီအပိုင်းမှာ MCP နဲ့ စတင်အလုပ်လုပ်ဖို့ အဆင်ပြေစေဖို့ အစပိုင်း setup လုပ်ငန်းစဉ်များကို လမ်းညွှန်ပေးပါမယ်။

### လိုအပ်ချက်များ

MCP development ကို စတင်မည်မတိုင်မီ သင့်မှာ ရှိထားရမည့်အရာများ -

- **Development Environment**: သင့်ရွေးချယ်ထားသော programming language (C#, Java, Python, TypeScript, or JavaScript) အတွက်
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, သို့မဟုတ် ခေတ်မီ code editor များ
- **Package Managers**: NuGet, Maven/Gradle, pip, သို့မဟုတ် npm/yarn
- **API Keys**: သင့် host applications တွင် အသုံးပြုမည့် AI services များအတွက်

### တရားဝင် SDK များ

လာမည့်အခန်းများတွင် Python, TypeScript, Java နှင့် .NET ကို အသုံးပြုထားသော solutions များကို တွေ့ရပါမယ်။ ဒီမှာ တရားဝင်အားဖြင့် ပံ့ပိုးထားသော SDK များအားလုံးကို ဖော်ပြထားပါတယ်။

MCP သည် အမျိုးမျိုးသော programming languages အတွက် တရားဝင် SDK များကို ပံ့ပိုးပေးထားသည်။
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft နှင့် ပူးပေါင်း၍ ထိန်းသိမ်းထားသည်
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI နှင့် ပူးပေါင်း၍ ထိန်းသိမ်းထားသည်
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - တရားဝင် TypeScript implementation
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - တရားဝင် Python implementation
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - တရားဝင် Kotlin implementation
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI နှင့် ပူးပေါင်း၍ ထိန်းသိမ်းထားသည်
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - တရားဝင် Rust implementation

## အဓိကအချက်များ

- MCP development environment ကို language-specific SDK များဖြင့် တပ်ဆင်ရလွယ်ကူသည်
- MCP servers တည်ဆောက်ခြင်းသည် tool များကို ရှင်းလင်းသော schemas ဖြင့် register လုပ်ခြင်းကို ပါဝင်သည်
- MCP clients များသည် servers နှင့် models များကို ချိတ်ဆက်ပြီး တိုးတက်သောစွမ်းရည်များကို အသုံးပြုသည်
- MCP implementations များကို စမ်းသပ်ခြင်းနှင့် အမှားရှာဖွေခြင်းသည် ယုံကြည်စိတ်ချရသော MCP implementations အတွက် အရေးကြီးသည်
- Deployment ရွေးချယ်မှုများသည် local development မှ cloud-based solutions အထိ ကွဲပြားသည်

## လေ့ကျင့်ခြင်း

ဒီအပိုင်းရဲ့ အခန်းအားလုံးမှာ exercises နှင့် assignments များပါဝင်ပြီး၊ အပိုဆောင်းအနေနဲ့ လေ့ကျင့်ရန် sample များကိုလည်း ထည့်သွင်းထားပါတယ်။

- [Java Calculator](./samples/java/calculator/README.md)
- [.Net Calculator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](../../../03-GettingStarted/samples/python)

## အပိုဆောင်း အရင်းအမြစ်များ

- [Model Context Protocol ကို အသုံးပြုပြီး Azure မှာ Agents တည်ဆောက်ခြင်း](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Azure Container Apps (Node.js/TypeScript/JavaScript) နဲ့ Remote MCP](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## နောက်တစ်ခု

နောက်တစ်ခု: [သင့်ရဲ့ ပထမဆုံး MCP Server တည်ဆောက်ခြင်း](01-first-server/README.md)

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။