# ဒီနမူနာကို အလုပ်လုပ်စေခြင်း

## -1- လိုအပ်သောအရာများကို ထည့်သွင်းပါ

```bash
dotnet restore
```

## -3- နမူနာကို အလုပ်လုပ်စေပါ

```bash
dotnet run
```

## -4- နမူနာကို စမ်းသပ်ပါ

Server ကို terminal တစ်ခုမှာ အလုပ်လုပ်နေစဉ်၊ အခြား terminal တစ်ခုကို ဖွင့်ပြီး အောက်ပါ command ကို run လုပ်ပါ:

```bash
npx @modelcontextprotocol/inspector dotnet run
```

ဒါက visual interface ပါဝင်တဲ့ web server ကို စတင်စေပြီး နမူနာကို စမ်းသပ်နိုင်ပါမည်။

Server ချိတ်ဆက်ပြီးနောက်:

- tools များကို စမ်းသပ်ပြီး `add` ကို run လုပ်ပါ၊ arguments 2 နှင့် 4 ကို ထည့်သွင်းပါ၊ ရလဒ်မှာ 6 ဖြစ်ရမည်။
- resources နှင့် resource template ကို သွားပြီး "greeting" ကို ခေါ်ပါ၊ နာမည်တစ်ခုကို ရိုက်ထည့်ပြီး သင့်ရိုက်ထည့်ထားသော နာမည်နှင့် greeting ကို မြင်ရမည်။

### CLI mode မှာ စမ်းသပ်ခြင်း

CLI mode မှာ တိုက်ရိုက် စတင်နိုင်ရန် အောက်ပါ command ကို run လုပ်ပါ:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/list
```

ဒါက server မှာ ရရှိနိုင်တဲ့ tools အားလုံးကို ပြသပါမည်။ အောက်ပါ output ကို မြင်ရမည်:

```text
{
  "tools": [
    {
      "name": "Add",
      "description": "Adds two numbers",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "integer"
          },
          "b": {
            "type": "integer"
          }
        },
        "title": "Add",
        "description": "Adds two numbers",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

Tool တစ်ခုကို ခေါ်ရန်:

```bash
npx @modelcontextprotocol/inspector --cli dotnet run --method tools/call --tool-name Add --tool-arg a=1 --tool-arg b=2
```

အောက်ပါ output ကို မြင်ရမည်:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Sum 3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> CLI mode မှာ inspector ကို run လုပ်ခြင်းက browser မှာ run လုပ်ခြင်းထက် အများအားဖြင့် ပိုမြန်တတ်သည်။
> Inspector အကြောင်းကို [ဒီမှာ](https://github.com/modelcontextprotocol/inspector) ဖတ်ရှုပါ။

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းကို ၎င်း၏ မူရင်းဘာသာစကားဖြင့် အာဏာတရားရှိသော အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော အလွဲအလွတ်များ သို့မဟုတ် အနားလွဲမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။