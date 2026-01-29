# နမူနာကို အလုပ်လုပ်စေပါ

ဒီနမူနာက Middleware တစ်ခုပါဝင်တဲ့ MCP Server ကို စတင်ပြီး Authorization header မှန်ကန်မှုကို စစ်ဆေးပေးပါသည်။

## လိုအပ်သော Dependencies များကို ထည့်သွင်းပါ

```bash
pip install "mcp[cli]" 
```

## Server ကို စတင်ပါ

```bash
python server.py
```

အခြား terminal မှာ client ကို စတင်ပါ

```bash
python client.py
```

သင်ရရှိမည့် ရလဒ်သည် အောက်ပါအတိုင်း ဖြစ်ရမည်:

```text
2025-09-30 13:25:54 - mcp_client - INFO - Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-09-30T13:25:54.311900",\n  "timezone": "UTC",\n  "timestamp": 1759238754.3119,\n  "formatted": "2025-09-30 13:25:54"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-09-30T13:25:54.311900', 'timezone': 'UTC', 'timestamp': 1759238754.3119, 'formatted': '2025-09-30 13:25:54'} isError=False
```

ဒါက credential ကို ပေးပို့ခြင်းအားဖြင့် ခွင့်ပြုထားသည်ကို ဆိုလိုသည်။

`client.py` ထဲမှာ credential ကို "secret-token2" အဖြစ် ပြောင်းလဲကြည့်ပါ၊ ထို့နောက် သင်ရရှိမည့် response မှာ အောက်ပါစာသား ပါဝင်ရမည်:

```text
2025-09-30 13:27:44 - httpx - INFO - HTTP Request: POST http://localhost:8000/mcp "HTTP/1.1 403 Forbidden"
```

ဒါက သင် authentication လုပ်ပြီး (credential ရှိသည်) ဖြစ်ပေမယ့် credential မှားနေသည်ကို ဆိုလိုသည်။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။