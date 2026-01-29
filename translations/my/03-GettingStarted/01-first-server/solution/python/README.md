# ဒီနမူနာကို အလုပ်လုပ်စေခြင်း

`uv` ကို install လုပ်ဖို့ အကြံပေးထားပေမယ့် မဖြစ်မဖြစ်လိုအပ်တာမဟုတ်ပါဘူး၊ [လမ်းညွှန်ချက်များ](https://docs.astral.sh/uv/#highlights) ကိုကြည့်ပါ။

## -0- Virtual Environment တစ်ခုဖန်တီးပါ

```bash
python -m venv venv
```

## -1- Virtual Environment ကို အလုပ်လုပ်စေပါ

```bash
venv\Scripts\activate
```

## -2- လိုအပ်သော Dependencies များကို Install လုပ်ပါ

```bash
pip install "mcp[cli]"
```

## -3- နမူနာကို အလုပ်လုပ်စေပါ

```bash
mcp run server.py
```

## -4- နမူနာကို စမ်းသပ်ပါ

Server ကို terminal တစ်ခုမှာ အလုပ်လုပ်နေစဉ်၊ အခြား terminal တစ်ခုဖွင့်ပြီး အောက်ပါ command ကို run လုပ်ပါ:

```bash
mcp dev server.py
```

ဒီဟာက visual interface ပါတဲ့ web server တစ်ခုကို စတင်စေပြီး နမူနာကို စမ်းသပ်နိုင်ပါမယ်။

Server ကို ချိတ်ဆက်ပြီးနောက်:

- tools များကို list လုပ်ပြီး `add` ကို run လုပ်ပါ၊ arguments 2 နှင့် 4 ကိုထည့်ပါ၊ ရလဒ်မှာ 6 ဖြစ်သင့်ပါတယ်။

- resources နှင့် resource template ကိုသွားပြီး `get_greeting` ကိုခေါ်ပါ၊ နာမည်တစ်ခုရိုက်ထည့်ပြီး သင့်ရိုက်ထည့်ထားတဲ့နာမည်နဲ့ greeting ကိုမြင်ရပါမယ်။

### CLI mode မှာ စမ်းသပ်ခြင်း

သင့်ရဲ့ inspector က အမှန်တကယ် Node.js app ဖြစ်ပြီး `mcp dev` က wrapper တစ်ခုဖြစ်ပါတယ်။

CLI mode မှာ တိုက်ရိုက် launch လုပ်နိုင်ဖို့ အောက်ပါ command ကို run လုပ်ပါ:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/list
```

ဒီဟာက Server မှာ ရရှိနိုင်တဲ့ tools အားလုံးကို list လုပ်ပါမယ်။ သင့်ရဲ့ output မှာ အောက်ပါအတိုင်းမြင်ရပါမယ်:

```text
{
  "tools": [
    {
      "name": "add",
      "description": "Add two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "title": "A",
            "type": "integer"
          },
          "b": {
            "title": "B",
            "type": "integer"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "title": "addArguments"
      }
    }
  ]
}
```

Tool တစ်ခုကို invoke လုပ်ဖို့:

```bash
npx @modelcontextprotocol/inspector --cli mcp run server.py --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

သင့်ရဲ့ output မှာ အောက်ပါအတိုင်းမြင်ရပါမယ်:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> Browser မှာ inspector ကို run လုပ်တာထက် CLI mode မှာ run လုပ်တာ ပုံမှန်အားဖြင့် အလွန်လျင်မြန်ပါတယ်။
> Inspector အကြောင်းပိုမိုဖတ်ရှုရန် [ဒီမှာ](https://github.com/modelcontextprotocol/inspector) ကြည့်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။