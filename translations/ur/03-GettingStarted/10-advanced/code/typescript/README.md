# نمونہ چلائیں

## ضروریات انسٹال کریں

```sh
npm install
```

## اسے بنائیں

```sh
npm run build
```

## اسے چلائیں

```sh
npm start
```

آپ کو یہ متن نظر آنا چاہیے:

```text
Registering tools...
Starting server...
```

زبردست، اس کا مطلب ہے کہ یہ صحیح طریقے سے شروع ہو رہا ہے۔

## سرور کی جانچ کریں

درج ذیل کمانڈ کے ساتھ صلاحیتوں کو آزمائیں:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

یہ انسپکٹر ٹول کے ویب انٹرفیس کو شروع کر دے گا۔

### CLI موڈ میں جانچ کریں

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

آپ کو درج ذیل آؤٹ پٹ نظر آنا چاہیے:

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

ایک ٹول چلائیں:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

آپ کو اس کے جیسا جواب نظر آنا چاہیے:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

ایسا ٹول آزمائیں جو موجود نہ ہو جیسے "add2" اس کمانڈ کے ساتھ:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

اب آپ کو یہ پیغام نظر آنا چاہیے جو ظاہر کرتا ہے کہ آپ کی توثیق کام کر رہی ہے:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

اس کے علاوہ ایک پیرامیٹر `c` بھیجنے کی کوشش کریں جو اسکیمہ کے ذریعے مسترد ہونا چاہیے، اس طرح:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

اب آپ کو "غلط دلائل" کی خرابی نظر آنا چاہیے:

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

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا غیر درستیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔