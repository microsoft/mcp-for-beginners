# MCP stdio Server - .NET Solution

> **⚠️ အရေးကြီး**: ဒီ solution ကို MCP Specification 2025-06-18 အတိုင်း **stdio transport** ကို အသုံးပြုရန် update လုပ်ပြီးဖြစ်ပါသည်။ အရင် SSE transport ကို အသုံးမပြုတော့ပါ။

## အကျဉ်းချုပ်

ဒီ .NET solution က stdio transport အသုံးပြုပြီး MCP server တစ်ခုကို ဘယ်လိုတည်ဆောက်ရမလဲဆိုတာကို ပြသထားပါတယ်။ stdio transport က ပိုရိုးရှင်းပြီး ပိုလုံခြုံသလို၊ SSE နည်းလမ်းထက် ပိုမိုကောင်းမွန်တဲ့ စွမ်းဆောင်ရည်ကို ပေးစွမ်းနိုင်ပါတယ်။

## လိုအပ်ချက်များ

- .NET 9.0 SDK သို့မဟုတ် အထက်တန်း
- .NET dependency injection အခြေခံနားလည်မှု

## Setup လုပ်နည်း

### အဆင့် ၁: Dependency များကို Restore လုပ်ပါ

```bash
dotnet restore
```

### အဆင့် ၂: Project ကို Build လုပ်ပါ

```bash
dotnet build
```

## Server ကို Run လုပ်ခြင်း

stdio server က အရင် HTTP-based server နဲ့ မတူပါဘူး။ Web server တစ်ခုကို စတင်မလုပ်ဘဲ stdin/stdout မှတဆင့် ဆက်သွယ်ပါတယ်။

```bash
dotnet run
```

**အရေးကြီး**: Server က ရပ်နေသလိုပဲ ထင်ရပါမယ် - ဒါက သာမန်ပါ! JSON-RPC messages ကို stdin မှ စောင့်နေပါတယ်။

## Server ကို စမ်းသပ်ခြင်း

### နည်းလမ်း ၁: MCP Inspector အသုံးပြုခြင်း (အကြံပြုထားသည်)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

ဒီနည်းလမ်းက:
1. သင့် server ကို subprocess အနေနဲ့ စတင်မည်
2. စမ်းသပ်ရန် web interface ကို ဖွင့်မည်
3. Server tools အားလုံးကို interactive အနေနဲ့ စမ်းသပ်နိုင်မည်

### နည်းလမ်း ၂: Command Line မှ တိုက်ရိုက် စမ်းသပ်ခြင်း

Inspector ကို တိုက်ရိုက် စတင်ပြီး စမ်းသပ်နိုင်ပါတယ်။

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### အသုံးပြုနိုင်သော Tools

Server က ဒီ tools များကို ပေးစွမ်းပါသည်။

- **AddNumbers(a, b)**: နံပါတ်နှစ်ခုကို ပေါင်းပါ
- **MultiplyNumbers(a, b)**: နံပါတ်နှစ်ခုကို မျိုးပါ  
- **GetGreeting(name)**: ကိုယ်ပိုင် greeting တစ်ခုကို ဖန်တီးပါ
- **GetServerInfo()**: Server အကြောင်းအရာကို ရယူပါ

### Claude Desktop ဖြင့် စမ်းသပ်ခြင်း

Claude Desktop နှင့် ဒီ server ကို အသုံးပြုရန် `claude_desktop_config.json` ထဲမှာ ဒီ configuration ကို ထည့်ပါ:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Project ဖွဲ့စည်းပုံ

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## HTTP/SSE နှင့် stdio transport အကြား အဓိက ကွာခြားချက်များ

**stdio transport (လက်ရှိ):**
- ✅ Setup ရိုးရှင်း - web server မလိုအပ်
- ✅ လုံခြုံမှု ပိုကောင်း - HTTP endpoints မရှိ
- ✅ `Host.CreateApplicationBuilder()` ကို အသုံးပြု
- ✅ `WithStdioTransport()` ကို အသုံးပြု
- ✅ Console application အနေနဲ့ run လုပ်
- ✅ စွမ်းဆောင်ရည် ပိုကောင်း

**HTTP/SSE transport (မသုံးတော့):**
- ❌ ASP.NET Core web server လိုအပ်
- ❌ `app.MapMcp()` routing setup လိုအပ်
- ❌ Configuration နဲ့ Dependency များ ပိုရှုပ်
- ❌ လုံခြုံရေးအတွက် ပိုမိုစဉ်းစားရ
- ❌ MCP 2025-06-18 မှာ မသုံးတော့

## Development Features

- **Dependency Injection**: Service နဲ့ logging အတွက် DI အပြည့်အဝ ပံ့ပိုးမှု
- **Structured Logging**: `ILogger<T>` ကို အသုံးပြုပြီး stderr မှာ logging ပြုလုပ်
- **Tool Attributes**: `[McpServerTool]` attributes ကို အသုံးပြုပြီး tool ကို ရှင်းလင်းစွာ သတ်မှတ်
- **Async Support**: Tools အားလုံး async operations ကို ပံ့ပိုး
- **Error Handling**: Error များကို သေချာစွာ ကိုင်တွယ်ပြီး logging ပြုလုပ်

## Development Tips

- Logging အတွက် `ILogger` ကို အသုံးပြုပါ (stdout ကို တိုက်ရိုက် မရေးပါနှင့်)
- စမ်းသပ်မည်ဆိုရင် `dotnet build` ဖြင့် build လုပ်ပါ
- Visual debugging အတွက် Inspector ကို အသုံးပြုပါ
- Logging အားလုံး stderr ကို automatic ပို့ပါမည်
- Server က shutdown signals ကို သေချာ handle လုပ်ပါသည်

ဒီ solution က လက်ရှိ MCP specification ကို လိုက်နာပြီး stdio transport ကို အသုံးပြုသည့် .NET implementation အတွက် အကောင်းဆုံးနည်းလမ်းများကို ပြသထားပါသည်။

---

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူလဘာသာစကားဖြင့် အာဏာတည်သောရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပြန်ဆိုမှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပါယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။