# MCP stdio Server - TypeScript Solution

> **⚠️ အရေးကြီး**: ဒီဖြေရှင်းနည်းကို MCP Specification 2025-06-18 မှအကြံပြုထားတဲ့ **stdio transport** ကိုအသုံးပြုဖို့အတွက် အပ်ဒိတ်လုပ်ထားပါတယ်။ အရင် SSE transport ကို အသုံးမပြုတော့ပါ။

## အကျဉ်းချုပ်

ဒီ TypeScript ဖြေရှင်းနည်းက stdio transport ကိုအသုံးပြုပြီး MCP server တစ်ခုကို ဘယ်လိုတည်ဆောက်ရမယ်ဆိုတာကို ပြသထားပါတယ်။ stdio transport က ပိုရိုးရှင်းပြီး ပိုလုံခြုံသလို SSE နည်းလမ်းထက် ပိုမိုကောင်းမွန်တဲ့ စွမ်းဆောင်ရည်ကိုပေးစွမ်းနိုင်ပါတယ်။

## လိုအပ်ချက်များ

- Node.js 18+ သို့မဟုတ် နောက်ဆုံးဗားရှင်း
- npm သို့မဟုတ် yarn package manager

## Setup လုပ်နည်း

### အဆင့် ၁: Dependencies တွေကို Install လုပ်ပါ

```bash
npm install
```

### အဆင့် ၂: Project ကို Build လုပ်ပါ

```bash
npm run build
```

## Server ကို Run လုပ်ခြင်း

stdio server က အရင် SSE server နဲ့ မတူဘဲ stdin/stdout မှတဆင့် ဆက်သွယ်ပါတယ်။ Web server တစ်ခုကို စတင်မလုပ်ပါဘူး။

```bash
npm start
```

**အရေးကြီး**: Server က ရပ်နေသလိုပဲ မြင်ရပါမယ် - ဒါက သာမန်ပါ! JSON-RPC messages ကို stdin မှစောင့်နေပါတယ်။

## Server ကို စမ်းသပ်ခြင်း

### နည်းလမ်း ၁: MCP Inspector ကို အသုံးပြုခြင်း (အကြံပြုထားသည်)

```bash
npm run inspector
```

ဒီနည်းလမ်းက:
1. သင့် server ကို subprocess အနေနဲ့ စတင်မည်
2. စမ်းသပ်ဖို့ web interface ကို ဖွင့်မည်
3. Server tools အားလုံးကို interactive အနေနဲ့ စမ်းသပ်နိုင်မည်

### နည်းလမ်း ၂: Command Line မှတဆင့် တိုက်ရိုက်စမ်းသပ်ခြင်း

Inspector ကို တိုက်ရိုက်စတင်ပြီး စမ်းသပ်နိုင်ပါတယ်။

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### ရရှိနိုင်သော Tools များ

Server က အောက်ပါ tools များကို ပေးစွမ်းပါသည်:

- **add(a, b)**: နံပါတ်နှစ်ခုကို ပေါင်းခြင်း
- **multiply(a, b)**: နံပါတ်နှစ်ခုကို မျိုးခြင်း  
- **get_greeting(name)**: ကိုယ်ပိုင်အမည်နှင့် greeting message တစ်ခုကို ဖန်တီးခြင်း
- **get_server_info()**: Server အကြောင်းအရာကို ရယူခြင်း

### Claude Desktop ဖြင့် စမ်းသပ်ခြင်း

Claude Desktop ကို အသုံးပြုရန် `claude_desktop_config.json` ထဲမှာ ဒီ configuration ကို ထည့်ပါ:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## Project ဖွဲ့စည်းပုံ

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## SSE နှင့် stdio transport အကြား အဓိကကွာခြားချက်များ

**stdio transport (လက်ရှိ):**
- ✅ Setup လုပ်ရတာ ပိုရိုးရှင်း - HTTP server မလိုအပ်
- ✅ ပိုလုံခြုံ - HTTP endpoints မရှိ
- ✅ Subprocess-based communication
- ✅ JSON-RPC ကို stdin/stdout မှတဆင့်
- ✅ ပိုမိုကောင်းမွန်တဲ့ စွမ်းဆောင်ရည်

**SSE transport (မသုံးတော့):**
- ❌ Express server setup လိုအပ်
- ❌ Routing နဲ့ session management ရှုပ်ထွေးမှုများ
- ❌ Dependencies ပိုများ (Express, HTTP handling)
- ❌ လုံခြုံရေးအတွက် ထပ်မံစဉ်းစားရမည်
- ❌ MCP 2025-06-18 မှာ မသုံးတော့ဘူး

## ဖွံ့ဖြိုးရေးအကြံပြုချက်များ

- Logging အတွက် `console.error()` ကို အသုံးပြုပါ (`console.log()` ကို အသုံးမပြုပါနဲ့၊ stdout ကို ရေးသားမည်)
- စမ်းသပ်မည့်အခါ `npm run build` ဖြင့် build လုပ်ပါ
- Visual debugging အတွက် Inspector ကို အသုံးပြုပါ
- JSON messages အားလုံးကို မှန်ကန်စွာ format လုပ်ပါ
- Server က SIGINT/SIGTERM ရရှိတဲ့အခါ အလိုအလျောက် graceful shutdown ကို handle လုပ်ပါ

ဒီဖြေရှင်းနည်းက လက်ရှိ MCP specification ကို လိုက်နာပြီး TypeScript ဖြင့် stdio transport ကို အကောင်းဆုံးအသုံးပြုဖို့ နည်းလမ်းများကို ပြသထားပါတယ်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် ရှုလေ့ရှိသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။