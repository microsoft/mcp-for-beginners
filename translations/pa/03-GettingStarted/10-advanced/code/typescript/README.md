# ਨਮੂਨਾ ਚਲਾਓ

## Dependencies ਇੰਸਟਾਲ ਕਰੋ

```sh
npm install
```

## ਇਸਨੂੰ ਬਣਾਓ

```sh
npm run build
```

## ਇਸਨੂੰ ਚਲਾਓ

```sh
npm start
```

ਤੁਹਾਨੂੰ ਇਹ ਟੈਕਸਟ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:

```text
Registering tools...
Starting server...
```

ਵਧੀਆ, ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਇਹ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਸ਼ੁਰੂ ਹੋ ਰਿਹਾ ਹੈ।

## ਸਰਵਰ ਦੀ ਜਾਂਚ ਕਰੋ

ਹੇਠਾਂ ਦਿੱਤੇ ਕਮਾਂਡ ਨਾਲ ਸਮਰੱਥਾਵਾਂ ਦੀ ਜਾਂਚ ਕਰੋ:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

ਇਸ ਨਾਲ ਇੰਸਪੈਕਟਰ ਟੂਲ ਦੇ ਵੈੱਬ ਇੰਟਰਫੇਸ ਨੂੰ ਸ਼ੁਰੂ ਕਰਨਾ ਚਾਹੀਦਾ ਹੈ।

### CLI ਮੋਡ ਵਿੱਚ ਜਾਂਚ ਕਰੋ

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

ਤੁਹਾਨੂੰ ਹੇਠਾਂ ਦਿੱਤਾ ਆਉਟਪੁੱਟ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:

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

ਇੱਕ ਟੂਲ ਚਲਾਓ:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

ਤੁਹਾਨੂੰ ਇਸਦੇ ਸਮਾਨ ਇੱਕ ਜਵਾਬ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

"add2" ਵਰਗੇ ਮੌਜੂਦ ਨਾ ਹੋਣ ਵਾਲੇ ਟੂਲ ਦੀ ਜਾਂਚ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ ਇਸ ਕਮਾਂਡ ਨਾਲ:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

ਹੁਣ ਤੁਹਾਨੂੰ ਇਹ ਸੁਨੇਹਾ ਦੇਖਣਾ ਚਾਹੀਦਾ ਹੈ ਜੋ ਦਿਖਾਉਂਦਾ ਹੈ ਕਿ ਤੁਹਾਡੀ ਵੈਧਤਾ ਸਹੀ ਕੰਮ ਕਰ ਰਹੀ ਹੈ:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

ਇੱਕ ਪੈਰਾਮੀਟਰ `c` ਭੇਜਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰੋ ਜੋ ਸਕੀਮਾ ਦੁਆਰਾ ਰੱਦ ਕੀਤਾ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ, ਇਸ ਤਰ੍ਹਾਂ:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

ਹੁਣ ਤੁਹਾਨੂੰ "ਅਵੈਧ ਦਲੀਲਾਂ" ਦੀ ਗਲਤੀ ਦੇਖਣੀ ਚਾਹੀਦੀ ਹੈ:

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

**ਅਸਵੀਕਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਹਾਲਾਂਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਾਰੂਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦਸਤਾਵੇਜ਼ ਦਾ ਮੂਲ ਰੂਪ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।