# MCP stdio Server - Python Solution

> **⚠️ အရေးကြီး**: ဒီဖြေရှင်းနည်းကို MCP Specification 2025-06-18 မှအကြံပြုထားတဲ့ **stdio transport** ကိုအသုံးပြုဖို့အတွက် update လုပ်ထားပါတယ်။ အရင် SSE transport ကို အသုံးမပြုတော့ပါ။

## အကျဉ်းချုပ်

ဒီ Python ဖြေရှင်းနည်းက stdio transport ကိုအသုံးပြုပြီး MCP server တစ်ခုကို ဘယ်လိုတည်ဆောက်ရမယ်ဆိုတာကို ပြသထားပါတယ်။ stdio transport က ပိုရိုးရှင်းပြီး ပိုလုံခြုံသလို၊ SSE နည်းလမ်းထက် ပိုမိုကောင်းမွန်တဲ့ performance ကိုပေးစွမ်းနိုင်ပါတယ်။

## လိုအပ်ချက်များ

- Python 3.8 သို့မဟုတ် အထက်
- `uv` ကို package management အတွက် install လုပ်ဖို့ အကြံပြုပါတယ်၊ [instructions](https://docs.astral.sh/uv/#highlights) ကိုကြည့်ပါ။

## Setup လုပ်နည်းများ

### အဆင့် ၁: Virtual environment တစ်ခုဖန်တီးပါ

```bash
python -m venv venv
```

### အဆင့် ၂: Virtual environment ကို activate လုပ်ပါ

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### အဆင့် ၃: လိုအပ်တဲ့ dependencies တွေကို install လုပ်ပါ

```bash
pip install mcp
```

## Server ကို run လုပ်ခြင်း

stdio server က အရင် SSE server နဲ့ မတူပါဘူး။ Web server ကို start လုပ်တာမဟုတ်ဘဲ stdin/stdout မှတဆင့် ဆက်သွယ်ပါတယ်:

```bash
python server.py
```

**အရေးကြီး**: Server က hang ဖြစ်နေသလိုပဲ မြင်ရပါမယ် - ဒါက normal ပါ! Server က stdin မှ JSON-RPC messages ကို စောင့်နေပါတယ်။

## Server ကို စမ်းသပ်ခြင်း

### နည်းလမ်း ၁: MCP Inspector ကို အသုံးပြုခြင်း (အကြံပြု)

```bash
npx @modelcontextprotocol/inspector python server.py
```

ဒီနည်းလမ်းက:
1. သင့် server ကို subprocess အနေနဲ့ run လုပ်ပါမယ်
2. စမ်းသပ်ဖို့ web interface ကို ဖွင့်ပါမယ်
3. Server tools အားလုံးကို interactive အနေနဲ့ စမ်းသပ်နိုင်ပါမယ်

### နည်းလမ်း ၂: JSON-RPC ကို တိုက်ရိုက် စမ်းသပ်ခြင်း

သင် JSON-RPC messages ကို တိုက်ရိုက်ပို့ပြီး စမ်းသပ်နိုင်ပါတယ်:

1. Server ကို start လုပ်ပါ: `python server.py`
2. JSON-RPC message တစ်ခုကို ပို့ပါ (ဥပမာ):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Server က အသုံးပြုနိုင်တဲ့ tools တွေကို ပြန်လည်တုံ့ပြန်ပါမယ်

### အသုံးပြုနိုင်တဲ့ Tools

Server က ဒီ tools တွေကို ပေးစွမ်းပါတယ်:

- **add(a, b)**: နံပါတ်နှစ်ခုကို ပေါင်းပါ
- **multiply(a, b)**: နံပါတ်နှစ်ခုကို မျိုးပါ  
- **get_greeting(name)**: အမည်ကို အသုံးပြုပြီး အထူးကြိုဆိုစကားကို ဖန်တီးပါ
- **get_server_info()**: Server အကြောင်းအရာကို ရယူပါ

### Claude Desktop နဲ့ စမ်းသပ်ခြင်း

ဒီ server ကို Claude Desktop နဲ့ အသုံးပြုဖို့ `claude_desktop_config.json` မှာ ဒီ configuration ကို ထည့်ပါ:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## SSE နဲ့ stdio transport အကြား အဓိကကွာခြားချက်များ

**stdio transport (လက်ရှိ):**
- ✅ Setup ရိုးရှင်း - web server မလိုအပ်
- ✅ ပိုလုံခြုံ - HTTP endpoints မရှိ
- ✅ Subprocess-based communication
- ✅ stdin/stdout မှ JSON-RPC
- ✅ ပိုမိုကောင်းမွန်တဲ့ performance

**SSE transport (မသုံးတော့):**
- ❌ HTTP server setup လိုအပ်
- ❌ Web framework (Starlette/FastAPI) လိုအပ်
- ❌ Routing နဲ့ session management ပိုရှုပ်
- ❌ လုံခြုံရေးအတွက် ထပ်မံစဉ်းစားရ
- ❌ MCP 2025-06-18 မှာ မသုံးတော့ဘူး

## Debugging အကြံပြုချက်များ

- Logging အတွက် `stderr` ကို အသုံးပြုပါ (`stdout` ကို မသုံးပါနဲ့)
- Visual debugging အတွက် Inspector ကို စမ်းသပ်ပါ
- JSON messages အားလုံးကို newline-delimited ဖြစ်စေပါ
- Server က error မရှိဘဲ စတင်နိုင်တာကို စစ်ဆေးပါ

ဒီဖြေရှင်းနည်းက လက်ရှိ MCP specification ကို လိုက်နာပြီး stdio transport implementation အတွက် အကောင်းဆုံးနည်းလမ်းများကို ပြသထားပါတယ်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါရှိနိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအချော်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။