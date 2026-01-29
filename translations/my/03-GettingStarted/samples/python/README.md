# MCP Calculator Server (Python)

Python ဖြင့် ရိုးရှင်းသော Model Context Protocol (MCP) server ကို ဖန်တီးထားပြီး အခြေခံ ကိန်းဂဏန်းတွက်ချက်မှုများကို ပံ့ပိုးပေးပါသည်။

## တပ်ဆင်ခြင်း

လိုအပ်သော dependencies များကို တပ်ဆင်ပါ။

```bash
pip install -r requirements.txt
```

သို့မဟုတ် MCP Python SDK ကို တိုက်ရိုက်တပ်ဆင်ပါ:

```bash
pip install mcp>=1.18.0
```

## အသုံးပြုခြင်း

### Server ကို အလုပ်လုပ်စေခြင်း

Server ကို MCP clients (ဥပမာ Claude Desktop) မှ အသုံးပြုရန် ဖန်တီးထားပါသည်။ Server ကို စတင်ရန်:

```bash
python mcp_calculator_server.py
```

**မှတ်ချက်**: Terminal မှ တိုက်ရိုက် run လုပ်သောအခါ JSON-RPC validation error များကို တွေ့ရပါမည်။ ဒါဟာ သာမန်အခြေအနေဖြစ်ပြီး - Server သည် MCP client message များကို စောင့်နေပါသည်။

### Function များကို စမ်းသပ်ခြင်း

Calculator function များ အလုပ်လုပ်မှုမှန်ကန်ကြောင်း စမ်းသပ်ရန်:

```bash
python test_calculator.py
```

## ပြဿနာများကို ဖြေရှင်းခြင်း

### Import Errors

`ModuleNotFoundError: No module named 'mcp'` ဟု error တွေ့ပါက MCP Python SDK ကို တပ်ဆင်ပါ:

```bash
pip install mcp>=1.18.0
```

### JSON-RPC Errors ကို တိုက်ရိုက် Run လုပ်သောအခါ

Server ကို တိုက်ရိုက် run လုပ်သောအခါ "Invalid JSON: EOF while parsing a value" ကဲ့သို့ error များကို တွေ့ရပါမည်။ Server သည် MCP client message များကို လိုအပ်ပြီး တိုက်ရိုက် terminal input မဟုတ်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားလည်မှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။