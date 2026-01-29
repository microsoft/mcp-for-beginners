# नमूना चलाएं

## डिपेंडेंसी इंस्टॉल करें

```sh
npm install
```

## इसे बनाएं

```sh
npm run build
```

## इसे चलाएं

```sh
npm start
```

आपको यह टेक्स्ट दिखाई देना चाहिए:

```text
Registering tools...
Starting server...
```

बहुत बढ़िया, इसका मतलब है कि यह सही तरीके से शुरू हो रहा है।

## सर्वर का परीक्षण करें

निम्नलिखित कमांड के साथ क्षमताओं का परीक्षण करें:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

यह इंस्पेक्टर टूल के वेब इंटरफेस को शुरू कर देना चाहिए।

### CLI मोड में परीक्षण करें

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

आपको निम्नलिखित आउटपुट दिखाई देना चाहिए:

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

एक टूल चलाएं:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

आपको इस तरह का प्रतिक्रिया दिखाई देना चाहिए:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

ऐसा टूल "add2" का परीक्षण करें जो मौजूद नहीं है, इस कमांड के साथ:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

अब आपको यह संदेश दिखाई देना चाहिए जो दिखाता है कि आपका वैलिडेशन काम कर रहा है:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

इसके अलावा, एक पैरामीटर `c` भेजने की कोशिश करें जिसे स्कीमा द्वारा अस्वीकार किया जाना चाहिए, इस तरह:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

अब आपको "अमान्य तर्क" त्रुटि दिखाई देनी चाहिए:

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

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।