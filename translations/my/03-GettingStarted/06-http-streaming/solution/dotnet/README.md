# ဒီနမူနာကို အလုပ်လုပ်စေခြင်း

## -1- လိုအပ်သောအရာများကို ထည့်သွင်းပါ

```bash
dotnet restore
```

## -2- နမူနာကို အလုပ်လုပ်စေပါ

```bash
dotnet run
```

## -3- နမူနာကို စမ်းသပ်ပါ

အောက်ပါကို အလုပ်လုပ်စေမီ သီးခြား terminal တစ်ခုကို စတင်ပါ (server သည် အလုပ်လုပ်နေဆဲဖြစ်ရမည်ကို သေချာစေပါ)။

Server ကို terminal တစ်ခုတွင် အလုပ်လုပ်နေစဉ်၊ အခြား terminal တစ်ခုကို ဖွင့်ပြီး အောက်ပါ command ကို run လုပ်ပါ:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

ဤသည်သည် visual interface ပါသော web server ကို စတင်ပေးမည်ဖြစ်ပြီး နမူနာကို စမ်းသပ်နိုင်မည်ဖြစ်သည်။

> **Streamable HTTP** ကို transport type အဖြစ် ရွေးချယ်ထားပြီး URL သည် `http://localhost:3001/mcp` ဖြစ်ရမည်ကို သေချာစေပါ။

Server သို့ ချိတ်ဆက်ပြီးနောက်:

- tools များကို စစ်ဆေးပြီး `add` ကို args 2 နှင့် 4 ဖြင့် run လုပ်ပါ၊ ရလဒ်တွင် 6 ကို တွေ့ရမည်။
- resources နှင့် resource template သို့ သွားပြီး "greeting" ကို ခေါ်ပါ၊ နာမည်တစ်ခုကို ရိုက်ထည့်ပါ၊ သင်ရိုက်ထည့်သော နာမည်နှင့် greeting ကို တွေ့ရမည်။

### CLI mode တွင် စမ်းသပ်ခြင်း

CLI mode တွင် တိုက်ရိုက် စတင်နိုင်ရန် အောက်ပါ command ကို run လုပ်ပါ:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

ဤသည်သည် server တွင် ရရှိနိုင်သော tools များအားလုံးကို စာရင်းပြုစုပေးမည်။ သင်သည် အောက်ပါ output ကို တွေ့ရမည်:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
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
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

သင်သည် အောက်ပါ output ကို တွေ့ရမည်:

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
> CLI mode တွင် inspector ကို run လုပ်ခြင်းသည် browser တွင် run လုပ်ခြင်းထက် အများအားဖြင့် ပိုမြန်သည်။
> Inspector အကြောင်းပိုမိုဖတ်ရှုရန် [ဒီမှာ](https://github.com/modelcontextprotocol/inspector) ကို သွားပါ။

---

**ဝက်ဘ်ဆိုက်မှတ်ချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားနေပါသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်ဆိုမှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို ကျေးဇူးပြု၍ သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတည်သော ရင်းမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များမှ ဘာသာပြန်ဆိုမှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်ကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပါယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။