# နမူနာကို အလုပ်လုပ်စေပါ

## ပတ်ဝန်းကျင် ဖန်တီးရန်

```sh
python -m venv venv
source ./venv/bin/activate
```

## လိုအပ်သော dependencies များကို ထည့်သွင်းပါ

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Token ဖန်တီးပါ

Client က Server နဲ့ ဆက်သွယ်ဖို့အတွက် Token တစ်ခု ဖန်တီးဖို့ လိုအပ်ပါမယ်။

အောက်ပါအတိုင်း ခေါ်ပါ:

```sh
python util.py
```

## ကုဒ်ကို အလုပ်လုပ်စေပါ

အောက်ပါအတိုင်း ကုဒ်ကို အလုပ်လုပ်စေပါ:

```sh
python server.py
```

အခြား terminal တစ်ခုမှာ အောက်ပါအတိုင်း ရိုက်ပါ:

```sh
python client.py
```

Server terminal မှာ အောက်ပါအတိုင်း တူညီတဲ့ output ကို တွေ့ရပါမယ်:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Client window မှာ အောက်ပါအတိုင်း တူညီတဲ့ text ကို တွေ့ရပါမယ်:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

ဒါက အားလုံး အလုပ်လုပ်နေတယ် ဆိုတာကို ဆိုလိုပါတယ်။

### အချက်အလက်ကို ပြောင်းလဲပြီး အလုပ်မလုပ်တာကို စမ်းကြည့်ပါ

*server.py* မှာ အောက်ပါကုဒ်ကို ရှာပါ:

```python
 if not has_scope(has_header, "Admin.Write"):
```

ဒါကို "User.Write" လို့ ပြောင်းပါ။ သင့် token လက်ရှိမှာ အဲဒီ permission level မပါရှိတဲ့အတွက် Server ကို ပြန်စတင်ပြီး Client ကို ထပ်မံ အလုပ်လုပ်စေတဲ့အခါ Server terminal မှာ အောက်ပါအတိုင်း error တစ်ခုကို တွေ့ရပါမယ်:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

သင့် server code ကို ပြန်ပြောင်းလဲမယ်လို့ ဆုံးဖြတ်နိုင်ပါတယ်၊ ဒါမှမဟုတ် အပို scope ပါရှိတဲ့ token အသစ်ကို ဖန်တီးနိုင်ပါတယ်၊ သင့်စိတ်ကြိုက်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရားရှိသော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအမှားများ သို့မဟုတ် အနားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။