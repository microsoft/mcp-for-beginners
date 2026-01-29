# ဒီနမူနာကို အလုပ်လုပ်စေခြင်း

`uv` ကို install လုပ်ဖို့ အကြံပြုထားပေမယ့် မဖြစ်မဖြစ်လိုအပ်တာမဟုတ်ပါဘူး၊ [ညွှန်ကြားချက်များ](https://docs.astral.sh/uv/#highlights) ကိုကြည့်ပါ။

## -1- လိုအပ်သော dependencies များကို install လုပ်ပါ

```bash
npm install
```

## -3- နမူနာကို run လုပ်ပါ

```bash
npm run build
```

## -4- နမူနာကို စမ်းသပ်ပါ

Server ကို terminal တစ်ခုမှာ run လုပ်ထားပြီးနောက်၊ အခြား terminal တစ်ခုကိုဖွင့်ပြီး အောက်ပါ command ကို run လုပ်ပါ:

```bash
npm run inspector
```

ဒါက visual interface ပါဝင်တဲ့ web server ကိုစတင်ပေးပြီး နမူနာကို စမ်းသပ်နိုင်ပါမယ်။

Server ကိုချိတ်ဆက်ပြီးနောက်:

- tools များကို list လုပ်ပြီး `add` ကို run လုပ်ပါ၊ arguments အနေနဲ့ 2 နဲ့ 4 ကိုထည့်ပါ၊ ရလဒ်မှာ 6 ကိုတွေ့ရပါမယ်။
- resources နဲ့ resource template ကိုသွားပြီး "greeting" ကိုခေါ်ပါ၊ နာမည်တစ်ခုကိုရိုက်ထည့်ပြီး သင့်ရိုက်ထည့်ထားတဲ့နာမည်နဲ့ greeting ကိုတွေ့ရပါမယ်။

### CLI mode မှာ စမ်းသပ်ခြင်း

သင့်ရဲ့ inspector က အမှန်တကယ် Node.js app ဖြစ်ပြီး `mcp dev` က wrapper တစ်ခုဖြစ်ပါတယ်။

CLI mode မှာတိုက်ရိုက် run လုပ်နိုင်ဖို့ အောက်ပါ command ကို run လုပ်ပါ:

```bash
npx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/list
```

ဒါက server မှာရရှိနိုင်တဲ့ tools များကို list လုပ်ပေးပါမယ်။ အောက်ပါ output ကိုတွေ့ရပါမယ်:

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

Tool တစ်ခုကို invoke လုပ်ဖို့အတွက်:

```bash
nnpx @modelcontextprotocol/inspector --cli node ./build/index.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

အောက်ပါ output ကိုတွေ့ရပါမယ်:

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
> CLI mode မှာ inspector ကို run လုပ်တာ browser မှာ run လုပ်တာထက် အများကြီးလျင်မြန်ပါတယ်။
> Inspector အကြောင်းပိုမိုဖတ်ရှုရန် [ဒီမှာ](https://github.com/modelcontextprotocol/inspector) ကိုကြည့်ပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရ အရင်းအမြစ်အဖြစ် ရှုလေ့လာသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွဲအမှားအမှားများ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။