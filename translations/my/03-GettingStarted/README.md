## စတင်ခြင်း  

[![Build Your First MCP Server](../../../translated_images/my/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(ဤသင်ခန်းစာရုပ်သံကိုကြည့်ရန် အပေါ်ဖော်ပြထားသော ပုံကိုနှိပ်ပါ)_

ဤပိုင်းတွင် သင်ခန်းစာများစွာပါဝင်သည်။

- **1 သင့်ပထမဆုံး server**, ဤပထမဆုံးသင်ခန်းစာတွင် သင့်ပထမဆုံး server ကိုဖန်တီးပြီး inspector ကိရိယာဖြင့် စစ်ဆေးနည်းကို သင်ယူပါမည်။ ၎င်းသည် သင့် server ကို စမ်းသပ်ပြီး အမှားရှာဖွေရန် အကောင်းဆုံးနည်းလမ်းဖြစ်သည်။ [သင်ခန်းစာသို့](01-first-server/README.md)

- **2 Client**, ဤသင်ခန်းစာတွင် သင့် server နှင့် ချိတ်ဆက်နိုင်သော client ရေးသားနည်းကို သင်ယူပါမည်။ [သင်ခန်းစာသို့](02-client/README.md)

- **3 LLM ပါသော Client**, client ကို နောက်ထပ်ကောင်းမွန်စေရန် LLM ထည့်သွင်းကာ server နှင့် "ညှိနှိုင်း" ပြုလုပ်နိုင်စေရန်နည်းလမ်းဖြစ်သည်။ [သင်ခန်းစာသို့](03-llm-client/README.md)

- **4 Visual Studio Code တွင် GitHub Copilot Agent အဖွဲ့အဖြစ် server အသုံးပြုခြင်း**။ ဤနေရာတွင် MCP Server ကို Visual Studio Code အတွင်းမှ ရရှိထားသည့်နည်းလမ်းဖြစ်သည်။ [သင်ခန်းစာသို့](04-vscode/README.md)

- **5 stdio Transport Server** stdio ပေးပို့မှုသည် MCP server-client များအတွက် တိုက်ရိုက် ထိန်းသိမ်းမှုဖြစ်ပြီး လုံခြုံသော subprocess-based ဆက်သွယ်မှုနှင့် process isolation ပါဝင်သည်။ [သင်ခန်းစာသို့](05-stdio-server/README.md)

- **6 MCP ဖြင့် HTTP Streaming (Streamable HTTP)**. [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) တွင် ဖော်ပြထားသော စံပြ ပို့ဆောင်မှုနည်းလမ်းနှင့် လွန်ခဲ့သော session-based implementation အားလေ့လာနိုင်သည်။ [သင်ခန်းစာသို့](06-http-streaming/README.md)
	
	
	

- **7 VSCode အတွက် AI Toolkit အသုံးပြုခြင်း** MCP Clients နှင့် Servers များကို စမ်းသပ်နှင့် စိစစ်ရန် [သင်ခန်းစာသို့](07-aitk/README.md)

- **8 စမ်းသပ်ခြင်း**. server နှင့် client များကို မတူညီသောနည်းလမ်းများဖြင့် စမ်းသပ်နည်းကို အဓိကထားသည်။ [သင်ခန်းစာသို့](08-testing/README.md)

- **9 တပ်ဆင်ခြင်း**. MCP ဖြေရှင်းချက်များကို တပ်ဆင်ခြင်းနည်းလမ်းများကို လေ့လာပါမည်။ [သင်ခန်းစာသို့](09-deployment/README.md)

- **10 Server အသုံးပြုမှု အဆင့်မြင့်**. server အသုံးပြုမှု အဆင့်မြင့်နည်းလမ်းများကိုလေ့ကျင့်ပါမည်။ [သင်ခန်းစာသို့](./10-advanced/README.md)

- **11 Auth**. အခြေခံ auth မှ JWT နှင့် RBAC အသုံးပြုမှု အထိ auth ဖြည့်သွင်းနည်းကို လေ့လာပါ။ အဆင့်မြင့်ခေါင်းစဉ်များနှင့် လုံခြုံရေးပိုင်း အကြံပြုချက်များကို ဤနေရာမှ စတင်ပြီး လေ့လာရန် အကြံပြုသည်။ [သင်ခန်းစာသို့](./11-simple-auth/README.md)

- **12 MCP Hosts**. Claude Desktop, Cursor, Cline, နှင့် Windsurf အပါအဝင် လူကြိုက်များသော MCP host client များကို တပ်ဆင်အသုံးပြုပြီး ပို့ဆောင်မှုအမျိုးအစားများနှင့် ပြဿနာရှာဖွေရေးနည်းများကို လေ့လာပါ။ [သင်ခန်းစာသို့](./12-mcp-hosts/README.md)

- **13 MCP Inspector**. MCP inspector ကိရိယာဖြင့် သင့် MCP servers များကို ကျယ်ပြန့်စွာ စမ်းသပ်နှင့် အမှားရှာဖွေရန်အတွက် လေ့ကျင့်ပါ။ ကိရိယာ၊ အရင်းအမြစ်များ နှင့် protocol message များကို လေ့လာပါ။ [သင်ခန်းစာသို့](./13-mcp-inspector/README.md)

- **14 Sampling**. `2025-11-25` သက်တမ်းကုန်သည့် legacy Sampling primitive နှင့် များ ပြောင်းရွှေ့ခြင်း အတွက် လုပ်ငန်းစဉ်အသစ်များကို သင်ယူပါ။ Sampling သည် MCP `2026-07-28` တွင် ရုပ်သိမ်းထားသည်။ [သင်ခန်းစာသို့](./14-sampling/README.md)
	
	

- **15 MCP Apps**. UI ညွှန်ကြားချက်များဖြင့် တုံ့ပြန်သော MCP Servers ဖန်တီးပါ။ [သင်ခန်းစာသို့](./15-mcp-apps/README.md)

Model Context Protocol (MCP) သည် application များအနေဖြင့် LLM များကို context ပေးပို့ရန် စံနမူနာ protocol တစ်ခုဖြစ်သည်။ MCP ကို AI application များအတွက် USB-C port တစ်ခုလို့ ထင်ပါ။ ၎င်းသည် AI မော်ဒယ်များကို မတူညီသော ဒေတာများနှင့် ကိရိယာများထဲသို့ ချိတ်ဆက်ပေးသည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာ အပြီးတွင် သင် အောက်ပါအရာများကို ပြုလုပ်နိုင်မည်ဖြစ်သည်။

- MCP အတွက် C#, Java, Python, TypeScript, နှင့် JavaScript ဖြင့် ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်များ တပ်ဆင်ခြင်း
- ရိုးရှင်းသည့် custom features (resources, prompts, tools) ဖြင့် MCP server များ တည်ဆောက်ပြီး တပ်ဆင်ခြင်း
- MCP servers နှင့် ချိတ်ဆက်သည့် host application များ ဖန်တီးခြင်း
- MCP အသုံးပြုမှုများ စမ်းသပ်ပြီး အမှားရှာဖွေခြင်း
- ပုံမှန် တပ်ဆင်မှု အခြေအနေများနှင့် ဖြေရှင်းနည်းများကို နားလည်ခြင်း
- လူကြိုက်များသော LLM လုပ်ငန်းများနှင့် MCP implementation များ ချိတ်ဆက်ခြင်း

## သင့် MCP ပတ်ဝန်းကျင် တပ်ဆင်ခြင်း

MCP နှင့်အလုပ်လုပ်ရန်မတိုင်မီ ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်ကို အဆင်သင့်ပြင်ဆင်ထားပြီး အခြေခံ workflow ကို နားလည်ထားခြင်း အရေးကြီးပါသည်။ ဤပိုင်းတွင် MCP အခြေခံ စတင်တပ်ဆင်ခြင်း လမ်းညွှန်သွားမည်။

### လိုအပ်ချက်များ

MCP ဖွံ့ဖြိုးရေးထဲကို ဝင်မည်မတိုင်မီ အောက်ပါအရာများကို ထည့်သွင်းစဉ်းစားပါ။

- **ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင်**: သင်ရွေးချယ်ထားသည့် ဘာသာစကား(C#, Java, Python, TypeScript, သို့မဟုတ် JavaScript)
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm, သို့မဟုတ် ဤကာလအတွက်အသုံးပြုသော စာရေးကိရိယာ မည်သည့်မျိုး
- **Package Managers**: NuGet, Maven/Gradle, pip, သို့မဟုတ် npm/yarn
- **API Keys**: သင့် host applications တွင် အသုံးပြုရန် ရည်မှန်းထားသော AI ဝန်ဆောင်မှုများအတွက်


### တရားဝင် SDK များ

လာမည့်အခန်းများတွင် Python, TypeScript, Java နှင့် .NET အသုံးပြု၍ ဖန်တီးထားသော ဖြေရှင်းချက်များကို တွေ့မြင်ရမည်။ အောက်တွင် တရားဝင် SDK များကို ဖော်ပြပါသည်။


MCP `2026-07-28` အတွက် SDK အထောက်အပံ့သည် ဘာသာစကားအလိုက် တစ်ခုချင်း စတင်လျက်ရှိသည်။
ဥပမာကို လည်ပတ်ရန်မတိုင်မီ၊ ၎င်း၏ package version နှင့် SDK ထုတ်ပြန်ချက်မှတ်တမ်းများကို စစ်ဆေးပါ။

[တရားဝင် SDK စာရင်း](https://modelcontextprotocol.io/docs/sdk):
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft နှင့် ပူးပေါင်းထိန်းသိမ်းထားသည်
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI နှင့် ပူးပေါင်းထိန်းသိမ်းထားသည်
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - တရားဝင် TypeScript implementation
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - တရားဝင် Python implementation (FastMCP)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - တရားဝင် Kotlin implementation
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI နှင့် ပူးပေါင်းထိန်းသိမ်းထားသည်
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - တရားဝင် Rust implementation
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - တရားဝင် Go implementation

## အဓိက သင်ယူချက်များ

- MCP ဖွံ့ဖြိုးရေးပတ်ဝန်းကျင် တပ်ဆင်ခြင်းမှာ ဘာသာစကားအလိုက် SDK များဖြင့် လွယ်ကူသည်
- MCP servers တည်ဆောက်ရာတွင် မျက်မှောက် schema ဖော်ပြခြင်းနှင့် ကိရိယာများထည့်သွင်းခြင်းလိုအပ်သည်
- MCP clients များသည် server များနှင့် မော်ဒယ်များကို ချိတ်ဆက်ပြီး စွမ်းဆောင်ရည်များပိုမို အသုံးချသည်
- စမ်းသပ်ခြင်းနှင့် အမှားရှာဖွေရေးသည် MCP implementation များအတွက် အရေးကြီးသည်
- တပ်ဆင်သည့် နည်းလမ်းများအအလယ်အလတ်မှ ကြိုးမဲ့ဖြန့်ဖြူးမှုအထိ ရွေးချယ်နိုင်သည်

## လေ့ကျင့်ခြင်း

ဤပိုင်းရှိ အခန်းခေါင်းစဉ်အားလုံးတွင် မြင်တွေ့ရမည့် လေ့ကျင့်ခန်းများနှင့်ကိုက်ညီသည့် နမူနာများရှိသည်။ အပိုင်းတစ်ခုစီတွင်လည်း မိမိ၏ လေ့ကျင့်ခန်းများနှင့် အပ်ဆုံးများ ပါရှိသည်။

- [Java Calculator](./samples/java/calculator/README.md)
- [.NET Calculator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](../../../03-GettingStarted/samples/python)

## အပိုဆောင်း သတင်းအချက်အလက်များ

- [Azure တွင် Model Context Protocol ဖြင့် Agent များတည်ဆောက်ခြင်း](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Node.js/TypeScript/JavaScript ဖြင့် Azure Container Apps မှ Remote MCP](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## နောက်တစ်ဆင့်

ပထမဆုံးသင်ခန်းစာဖြင့် စတင်ပါ: [သင့် ပထမ MCP Server ဖန်တီးခြင်း](01-first-server/README.md)

ဤအပိုင်းအဆုံးသ reached ၏နောက်တွင်: [Module 4: Practical Implementation](../04-PracticalImplementation/README.md) သို့ ဆက်လက်ဆောင်ရွက်ပါ။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->