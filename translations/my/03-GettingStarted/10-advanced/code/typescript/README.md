# နမူနာကို အလုပ်လုပ်စေပါ

## လိုအပ်သောအရာများကို ထည့်သွင်းပါ

```sh
npm install
```

## တည်ဆောက်ပါ

```sh
npm run build
```

## အလုပ်လုပ်စေပါ

```sh
npm start
```

သင့်အနေနဲ့ အောက်ပါစာသားကို မြင်ရပါမည်-

```text
Registering tools...
Starting server...
```

အလွန်ကောင်းပါပြီ၊ ဒါက သင့်စနစ်မှန်ကန်စွာ စတင်နေသည်ကို ဆိုလိုသည်။

## Server ကို စမ်းသပ်ပါ

အောက်ပါ command ကို အသုံးပြုပြီး စွမ်းဆောင်ရည်များကို စမ်းသပ်ပါ-

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

ဒါက inspector tool ရဲ့ web interface ကို စတင်ဖွင့်လှစ်ပေးပါမည်။

### CLI mode မှာ စမ်းသပ်ပါ

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

သင့်အနေနဲ့ အောက်ပါ output ကို မြင်ရပါမည်-

```json
{
  "tools": [
    {
      "name": "add",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "rawSchema": {
        "_def": {
          "unknownKeys": "strip",
          "catchall": {
            "_def": {
              "typeName": "ZodNever"
            },
            "~standard": {
              "version": 1,
              "vendor": "zod"
            }
          },
          "typeName": "ZodObject"
        },
        "~standard": {
          "version": 1,
          "vendor": "zod"
        },
        "_cached": null
      }
    },
    {
      "name": "subtract",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "type": "number"
          },
          "b": {
            "type": "number"
          }
        },
        "required": [
          "a",
          "b"
        ],
        "additionalProperties": false,
        "$schema": "http://json-schema.org/draft-07/schema#"
      },
      "rawSchema": {
        "_def": {
          "unknownKeys": "strip",
          "catchall": {
            "_def": {
              "typeName": "ZodNever"
            },
            "~standard": {
              "version": 1,
              "vendor": "zod"
            }
          },
          "typeName": "ZodObject"
        },
        "~standard": {
          "version": 1,
          "vendor": "zod"
        },
        "_cached": null
      }
    }
  ]
}
```

Tool တစ်ခုကို အလုပ်လုပ်စေပါ-

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

သင့်အနေနဲ့ အောက်ပါနမူနာ output ကို မြင်ရပါမည်-

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

"add2" လို tool မရှိတဲ့အရာကို စမ်းသပ်ကြည့်ပါ၊ အောက်ပါ command ကို အသုံးပြုပါ-

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

အခု သင့် validation မှန်ကန်နေသည်ကို ပြသတဲ့ message ကို မြင်ရပါမည်-

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

Schema ကနေ ပယ်ချသင့်တဲ့ `c` parameter ကို ပေးပို့ကြည့်ပါ၊ အောက်ပါအတိုင်းလုပ်ပါ-

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

အခု "invalid arguments" error ကို မြင်ရပါမည်-

```text
{
  "content": [],
  "error": {
    "code": "invalid_arguments",
    "message": "Invalid arguments for tool add: [\n  {\n    \"code\": \"invalid_type\",\n    \"expected\": \"number\",\n    \"received\": \"undefined\",\n    \"path\": [\n      \"b\"\n    ],\n    \"message\": \"Required\"\n  }\n]"
  }
}
```

---

**အကြောင်းကြားချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းဘာသာစကားဖြင့် ရေးသားထားသော စာရွက်စာတမ်းကို အာဏာတရ အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူက ဘာသာပြန်မှုကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားများ သို့မဟုတ် အဓိပ္ပါယ်မှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။