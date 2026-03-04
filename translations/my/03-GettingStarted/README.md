## စတင်လိုက်ပါ  

[![Build Your First MCP Server](../../../translated_images/my/04.0ea920069efd979a.webp)](https://youtu.be/sNDZO9N4m9Y)

_(ဤသင်ခန်းစာ၏ ဗီဒီယိုကို ကြည့်ရန် အပေါ်တွင်ရှိသော ပုံကို နှိပ်ပါ)_

ဤအပိုင်းတွင် သင်ခန်းစာ အချို့ ပါဝင်သည် -

- **1 သင့်ပထမဆုံး ဆာဗာ**, ဤပထမအတန်း၌ သင်သည် သင့်ပထမဆုံး ဆာဗာကို မည်သို့ ဖန်တီးရမည်နှင့် inspector tool ဖြင့် စစ်ဆေးရမည်ကို သင်ယူမည်ဖြစ်ပြီး၊ ၎င်းသည် သင့်ဆာဗာကို စမ်းသပ်ရန်နှင့် debug ပြုလုပ်ရန် အထောက်အကူဖြစ်ပါသည်၊ [သို့ သွားရန်](01-first-server/README.md)

- **2 Client**, ဤသင်ခန်းစာတွင် သင့်ဆာဗာနှင့် ချိတ်ဆက်နိုင်သည့် client ရေးသားနည်းကို လေ့လာမည်၊ [သို့ သွားရန်](02-client/README.md)

- **3 Client with LLM**, client ကို ပိုမိုကောင်းမွန်စွာရေးသားရန် LLM ကိုဖြည့်စွက်ခြင်းဖြင့် သင့်ဆာဗာနှင့် "ညှိနှိုင်း" ပြုလုပ်နိုင်စေရန်၊ [သို့ သွားရန်](03-llm-client/README.md)

- **4 Consuming a server GitHub Copilot Agent mode in Visual Studio Code**. ဤနေရာတွင် Visual Studio Code မှာ MCP Server ကို မည်သို့ လည်ပတ်စေနိုင်သည်ကို ကြည့်ရှုပြပါမည်၊ [သို့ သွားရန်](04-vscode/README.md)

- **5 stdio Transport Server** stdio transport သည်နေရာဒေသခံ MCP ဆာဗာမှ client သို့ ညိနှိုင်းဆက်သွယ်မှုအတွက် အကြံပြုထားသော စံချိန်စံညွှန်းဖြစ်ပြီး subprocess ကို အခြေခံသော လုံခြုံသော ဆက်သွယ်မှုနှင့် processes ခွဲခြားထားမှု ပါရှိသည် [သို့ သွားရန်](05-stdio-server/README.md)

- **6 HTTP Streaming with MCP (Streamable HTTP)**. ခေတ်မီ HTTP streaming transport (အဝေးမှ MCP ဆာဗာများအတွက် အကြံပြုသည့်နည်းလမ်း [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/basic/transports/#streamable-http))၊ တိုးတက်မှု အကြောင်းကြားချက်များနှင့် Streamable HTTP ဖြင့် တိုးတက်၍ အချိန်နှင့် တပြိုင်နက်နေ MCP ဆာဗာနှင့် client များ ဖန်တီးနည်းကို လေ့လာပါ။ [သို့ သွားရန်](06-http-streaming/README.md)

- **7 Utilising AI Toolkit for VSCode** သင့် MCP Clients နှင့် Servers များ စမ်းသပ်နှင့် အသုံးပြုရန် [သို့ သွားရန်](07-aitk/README.md)

- **8 Testing**. ဤနေရာတွင် သင့်ဆာဗာနှင့် client များကို အမျိုးမျိုးသောနည်းလမ်းများဖြင့် စမ်းသပ်နည်းကို အထူးထားပြောပြမည်၊ [သို့ သွားရန်](08-testing/README.md)

- **9 Deployment**. သင်၏ MCP ဖြေရှင်းချက်များကို ပုံစံအမျိုးမျိုးဖြင့် စီစဉ်ထုတ်လုပ်နည်းကို လေ့လာရန်၊ [သို့ သွားရန်](09-deployment/README.md)

- **10 Advanced server usage**. ဆာဗာကို အဆင့်မြင့် အသုံးပြုနည်းများ၊ [သို့ သွားရန်](./10-advanced/README.md)

- **11 Auth**. စတင်ပါက Basic Auth မှ JWT နှင့် RBAC အသုံးပြုခြင်းအထိ ရိုးရှင်းသော ခွင့်ပြုခြင်း (auth) ထည့်သွင်းနည်း၊ ဤနေရာမှ စတင်၍ နောက်ထပ် အဆင့်မြင့် ချက်များကို Chapter 5 တွင် လေ့လာပြီး Chapter 2 တွင် အကြံပြုထားသော လုံခြုံမှု ပြုပြင်မှုများ ပြုလုပ်ရန် အကြံပြုပါသည်၊ [သို့ သွားရန်](./11-simple-auth/README.md)

- **12 MCP Hosts**. Claude Desktop, Cursor, Cline နှင့် Windsurf တို့ကဲ့သို့ လူကြိုက်များသော MCP host client များအား တပ်ဆင်အသုံးပြုနည်း၊ စနစ်တက်စနစ်ရောနှောနည်းနှင့် ပြဿနာရှာဖွေရေးနည်းများ၊ [သို့ သွားရန်](./12-mcp-hosts/README.md)

- **13 MCP Inspector**. MCP ဆာဗာများကို MCP Inspector tool အသုံးပြု၍ အပြန်အလှန် ဒီဘတ်နှင့် စမ်းသပ်နိုင်သည်။ troubleshooting tool များ၊ သတင်းအချက်အလက်များနှင့် ပရိုတိုကောညွှန်ကြားချက်များကို လေ့လာပါ၊ [သို့ သွားရန်](./13-mcp-inspector/README.md)

- **14 Sampling**. LLM ဆိုင်ရာ တာဝန်များတွင် MCP Clients နှင့် ပူးပေါင်းဆောင်ရွက်သည့် MCP Servers များ ဖန်တီးပါ၊ [သို့ သွားရန်](./14-sampling/README.md)

- **15 MCP Apps**. UI ညွှန်ကြားချက်များဖြင့် တုံ့ပြန်သော MCP Servers များ တည်ဆောက်ပါ၊ [သို့ သွားရန်](./15-mcp-apps/README.md)

Model Context Protocol (MCP) သည် applications များ LLM များအား context ပေးပို့မှုကို စံပြုတည်ဆောက်ထားသည့် ဖွင့်လင်းပရိုတိုကောဖြစ်သည်။ MCP ကို AI applications များအတွက် USB-C ပေါက်ကဲ့သို့ စိတ်ကူးယဥ်နိုင်ပြီး AI မော်ဒယ်များကို အမျိုးမျိုးသော ဒေတာရင်းမြစ်များနှင့် ကိရိယာများအား ချိတ်ဆက်ရန် စံပြုနည်းလမ်းဖြစ်သည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဤသင်ခန်းစာပြီးဆုံးသည့်အချိန်တွင် -

- C#, Java, Python, TypeScript နှင့် JavaScript များအတွက် MCP ဖန်တီးရေးသည့် အခြေခံဝန်းကျင်များပြင်ဆင်နည်း
- လိုအပ်သည့် function များ (resources, prompts, tools) ဖြင့် MCP ဆာဗာများ ဖန်တီးပြီး တပ်ဆင်နည်း
- MCP ဆာဗာများနှင့် ချိတ်ဆက်သည့် host application များ ဖန်တီးနည်း
- MCP ဆော့ဖ်ဝဲများ စမ်းသပ်၍ ဒီဘတ် ပြုလုပ်နည်း
- setup ကြုံတွေ့နိုင်သည့် ဖိအားများနှင့် ဖြေရှင်းနည်းလမ်းများ နားလည်ခြင်း
- လူကြိုက်များသော LLM ဝန်ဆောင်မှုများနှင့် MCP implementations များ ချိတ်ဆက်နည်း

## MCP ဖန်တီးရေး ချိတ်ဆက်ရေး ပတ်ဝန်းကျင် တပ်ဆင်ခြင်း

MCP တွင် အလုပ်လုပ်ရန် မတိုင်မီ ဖန်တီးရေးပတ်ဝန်းကျင်ကို ပြင်ဆင်ထားခြင်းနှင့် အခြေခံ workflow ကို နားလည်ထားခြင်းမှာ အရေးကြီးပါသည်။ ဤအပိုင်းတွင် MCP ဒါရွေ့မှု ချက်များကို မပြတ်တောက်စွာ စတင်ဖို့ လမ်းညွှန်မည်။

###လိုအပ်ချက်များ

MCP ဖန်တီးရေးတွင် စကားဝိုင်းဝင်ရန် အောက်ပါအချက်များရှိပါစေ။

- **ဖန်တီးရေးပတ်ဝန်းကျင်**: အသုံးပြုမည့် programming language (C#, Java, Python, TypeScript, JavaScript) အတွက်
- **IDE/Editor**: Visual Studio, Visual Studio Code, IntelliJ, Eclipse, PyCharm သို့မဟုတ် ခေတ်မီ code editor များ
- **Package Managers**: NuGet, Maven/Gradle, pip, npm/yarn
- **API Key များ**: သင်၏ host application များတွင် သုံးမည့် AI ဝန်ဆောင်မှုများအတွက်

### တရားဝင် SDK များ

နောက်ကွယ်တွင် ပါဝင်သော အခန်းများတွင် Python, TypeScript, Java နှင့် .NET ကို အသုံးပြု၍ ဖြေရှင်းချက်များကို ရှုမည်ဖြစ်ပြီး၊ တရားဝင် ထောက်ပံ့ထားသော SDK များမှာ အောက်ပါအတိုင်း ဖြစ်သည်-

MCP သည် ဘာသာစကား အမျိုးမျိုးအတွက်တရားဝင် SDK များ ( [MCP Specification 2025-11-25](https://spec.modelcontextprotocol.io/specification/2025-11-25/) အတိုင်း) ပံ့ပိုးပေးသည် -
- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk) - Microsoft နှင့် ပူးပေါင်းထိန်းသိမ်းထားသည်
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) - Spring AI ဖြင့် ပူးပေါင်းထိန်းသိမ်းထားသည်
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) - တရားဝင် TypeScript အကောင်အထည်ဖော်မှု
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) - တရားဝင် Python အကောင်အထည်ဖော်မှု (FastMCP)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk) - တရားဝင် Kotlin အကောင်အထည်ဖော်မှု
- [Swift SDK](https://github.com/modelcontextprotocol/swift-sdk) - Loopwork AI နှင့်ပူးပေါင်းထိန်းသိမ်းထားသည်
- [Rust SDK](https://github.com/modelcontextprotocol/rust-sdk) - တရားဝင် Rust အကောင်အထည်ဖော်မှု
- [Go SDK](https://github.com/modelcontextprotocol/go-sdk) - တရားဝင် Go အကောင်အထည်ဖော်မှု

## အဓိကကျသော အချက်များ

- ဘာသာစကားအလိုက် SDK များဖြင့် MCP ဖန်တီးရေး ပတ်ဝန်းကျင် တပ်ဆင်ရန် လွယ်ကူသည်
- MCP ဆာဗာများ ဖန်တီးရာတွင် ပုံသေရှိသော schemas ဖြင့် tools များ ဖန်တီး၍ မှတ်ပုံတင်ရမည်
- MCP client များသည် ဆာဗာနှင့် မော်ဒယ်များကို ချိတ်ဆက်၍ စွမ်းဆောင်ရည်မြှင့်တင်နိုင်သည်
- စမ်းသပ်ခြင်းနှင့် ဒီဘတ်လုပ်ခြင်းသည် MCP အကောင်အထည်ဖော်မှုများယုံကြည်စိတ်ချရအောင် လိုအပ်သည်
- တပ်ဆင်မှုရွေးချယ်စရာများမှာ ဒေသခံ ဖန်တီးမှုမှ cloud ဝန်ဆောင်မှုအထိဖြစ်သည်

## လေ့ကျင့်သင်ယူခြင်း

ဒီအပိုင်း၏ အခန်းတိုင်းတွင် တွေ့ရမည့် လေ့ကျင့်ခန်းများနှင့် ကိုက်ညီသော နမူနာများရှိသည်။ အပိုင်းတိုင်းမှာလည်း ကိုယ်ပိုင် လေ့ကျင့်ခန်းများနှင့် အပ်ငွေများပါဝင်သည်။

- [Java Calculator](./samples/java/calculator/README.md)
- [.Net Calculator](../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](./samples/javascript/README.md)
- [TypeScript Calculator](./samples/typescript/README.md)
- [Python Calculator](../../../03-GettingStarted/samples/python)

## နောက်ထပ် အရင်းအမြစ်များ

- [Build Agents using Model Context Protocol on Azure](https://learn.microsoft.com/azure/developer/ai/intro-agents-mcp)
- [Remote MCP with Azure Container Apps (Node.js/TypeScript/JavaScript)](https://learn.microsoft.com/samples/azure-samples/mcp-container-ts/mcp-container-ts/)
- [.NET OpenAI MCP Agent](https://learn.microsoft.com/samples/azure-samples/openai-mcp-agent-dotnet/openai-mcp-agent-dotnet/)

## နောက်တစ်ဆင့်

ပထမဆုံး သင်ခန်းစာဖြင့် စတင်ပါ: [သင့်ပထမဆုံး MCP ဆာဗာ ဖန်းတီးခြင်း](01-first-server/README.md)

ဤ module အပြီးတွင် ဆက်လက် လေ့လာပါ: [Module 4: Practical Implementation](../04-PracticalImplementation/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ဝန်ခံချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်မှု ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုကို ကြိုးစားပါသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် မွားယွင်းချက်များ သို့မဟုတ် မှန်ကန်မှု မရှိမှုများ ဖြစ်ပေါ်နိုင်ပါကြောင်း သတိပြုပါရန် ခြုံငုံ သတိပေးပါသည်။ မူလစာတမ်းကို မူလဘာသာဖြင့်သာ အတည်ပြု မှတ်ယူရန် သင့်တော်ပါသည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် မူရင်းလူ့ဘာသာပြန်သူမှ ဘာသာပြန်မှုကို သင့်တော်ပြီး အကောင်းဆုံးဖြစ်ပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် အဓိပ္ပာယ်လွဲမှားသည့်အခြေအနေများအတွက် ကျွန်ုပ်တို့သည် တာဝန် မထမ်းဆောင်ပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->