# மாதிரி இயக்கவும்

## தேவையான பொருட்களை நிறுவவும்

```sh
npm install
```

## கட்டமைக்கவும்

```sh
npm run build
```

## இயக்கவும்

```sh
npm start
```

நீங்கள் இந்த உரையை காண வேண்டும்:

```text
Registering tools...
Starting server...
```

அற்புதம், இது சரியாக தொடங்குகிறது என்பதைக் குறிக்கிறது.

## சர்வரை சோதிக்கவும்

கீழே உள்ள கட்டளையைப் பயன்படுத்தி திறன்களை சோதிக்கவும்:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

இது ஆய்வாளர் கருவியின் வலை இடைமுகத்தைத் தொடங்க வேண்டும்.

### CLI முறையில் சோதிக்கவும்

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

நீங்கள் கீழே உள்ள வெளியீட்டை காண வேண்டும்:

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

ஒரு கருவியை இயக்கவும்:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

நீங்கள் இதற்கு ஒத்த பதிலைப் பெற வேண்டும்:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

"add2" போன்ற ஒரு இல்லாத கருவியை சோதிக்க முயற்சிக்கவும், இந்த கட்டளையைப் பயன்படுத்தி:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

இப்போது உங்கள் சரிபார்ப்பு வேலை செய்கிறது என்பதை காட்டும் இந்த செய்தியை நீங்கள் காண வேண்டும்:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

மேலும், `c` என்ற ஒரு அளவுருவை அனுப்ப முயற்சிக்கவும், இது திட்டவட்டமாக நிராகரிக்கப்பட வேண்டும், இதைப் போல:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

இப்போது "தவறான வாதங்கள்" பிழையை நீங்கள் காண வேண்டும்:

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

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.