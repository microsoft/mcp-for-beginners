# ဒီနမူနာကို chạy လုပ်ခြင်း

`uv` ကို 설치 လုပ်ဖို့ အကြံပြုထားပေမယ့် မလိုအပ်ပါ၊ [ညွှန်ကြားချက်များ](https://docs.astral.sh/uv/#highlights) ကို ကြည့်ပါ။

## -0- virtual environment တစ်ခု ဖန်တီးပါ

```bash
python -m venv venv
```

## -1- virtual environment ကို ဖွင့်ပါ

```bash
venv\Scrips\activate
```

## -2- လိုအပ်သော dependencies များကို 설치 လုပ်ပါ

```bash
pip install "mcp[cli]"
```

## -3- နမူနာကို chạy လုပ်ပါ

```bash
python client.py
```

အောက်ပါအတိုင်း output ကို တွေ့ရပါမည်-

```text
LISTING RESOURCES
Resource:  ('meta', None)
Resource:  ('nextCursor', None)
Resource:  ('resources', [])
                    INFO     Processing request of type ListToolsRequest                                                                               server.py:534
LISTING TOOLS
Tool:  add
READING RESOURCE
                    INFO     Processing request of type ReadResourceRequest                                                                            server.py:534
CALL TOOL
                    INFO     Processing request of type CallToolRequest                                                                                server.py:534
[TextContent(type='text', text='8', annotations=None)]
```

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။