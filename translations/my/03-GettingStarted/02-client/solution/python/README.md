# ဤနမူနာကို chạyခြင်း

သင့်အား `uv` ကို ထည့်သွင်းရန် အကြံပြုပါတယ်၊ သို့သော် မဖြစ်မနေ မလိုအပ်ပါ၊ [ညွှန်ကြားချက်များ](https://docs.astral.sh/uv/#highlights) ကို ကြည့်ပါ

## -0- သတိ virtual ပတ်ဝန်းကျင်တစ်ခုဖန်တီးပါ

```bash
python -m venv venv
```

## -1- virtual ပတ်ဝန်းကျင်ကို ဖွင့်ပါ

```bash
venv\Scripts\activate
```

## -2- မူလတည်ဆောက်ရန်ပစ္စည်းများ ထည့်သွင်းပါ

```bash
pip install "mcp[cli]"
```

## -3- နမူနာကို chạyပါ

```bash
python client.py
```

သင်သည် အောက်ပါကဲ့သို့သော အဖြေကို မြင်ရပါမည်-

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
INFO Processing request of type ListToolsRequest server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
INFO Processing request of type ReadResourceRequest server.py:534
CALL TOOL
INFO Processing request of type CallToolRequest server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပြောကြားချက်**
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ စက်ကိရိယာဘာသာပြန်ခြင်းများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် လိုအပ်ပါသည်။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ ယုံကြည်စိတ်ချရသော အချက်အလက်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသည့် သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်သူဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုကွာခြားမှုများ သို့မဟုတ် မမှန်ကန်သော အသုံးပြုမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->