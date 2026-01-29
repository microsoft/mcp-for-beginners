# নমুনা চালান

## নির্ভরতা ইনস্টল করুন

```sh
npm install
```

## এটি তৈরি করুন

```sh
npm run build
```

## এটি চালান

```sh
npm start
```

আপনার দেখা উচিত এই লেখা:

```text
Registering tools...
Starting server...
```

দারুণ, এর মানে এটি সঠিকভাবে শুরু হচ্ছে।

## সার্ভার পরীক্ষা করুন

নিম্নলিখিত কমান্ড দিয়ে ক্ষমতাগুলি পরীক্ষা করুন:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

এটি পরিদর্শক টুলের ওয়েব ইন্টারফেস চালু করবে।

### CLI মোডে পরীক্ষা করুন

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

আপনার দেখা উচিত নিম্নলিখিত আউটপুট:

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

একটি টুল চালান:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

আপনার দেখা উচিত একটি প্রতিক্রিয়া যা এরকম:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

"add2" এর মতো একটি টুল যা নেই তা পরীক্ষা করার চেষ্টা করুন এই কমান্ড দিয়ে:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

এখন আপনি এই বার্তাটি দেখতে পাবেন যা দেখায় যে আপনার যাচাইকরণ কাজ করছে:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

এছাড়াও একটি প্যারামিটার `c` পাঠানোর চেষ্টা করুন যা স্কিমা দ্বারা প্রত্যাখ্যাত হওয়া উচিত, যেমন:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

এখন আপনি "অবৈধ আর্গুমেন্ট" ত্রুটি দেখতে পাবেন:

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

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকব না।