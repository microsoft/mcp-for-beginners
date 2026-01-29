# నమూనా నడపండి

## ఆధారాలను ఇన్‌స్టాల్ చేయండి

```sh
npm install
```

## దీన్ని నిర్మించండి

```sh
npm run build
```

## దీన్ని నడపండి

```sh
npm start
```

మీకు ఈ వచనం కనిపించాలి:

```text
Registering tools...
Starting server...
```

చాలా బాగుంది, అంటే ఇది సరిగ్గా ప్రారంభమవుతోంది.

## సర్వర్‌ను పరీక్షించండి

క్రింది కమాండ్‌తో సామర్థ్యాలను పరీక్షించండి:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

ఇది ఇన్స్పెక్టర్ టూల్ యొక్క వెబ్ ఇంటర్‌ఫేస్‌ను ప్రారంభించాలి.

### CLI మోడ్‌లో పరీక్షించండి

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

మీకు క్రింది అవుట్పుట్ కనిపించాలి:

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

ఒక టూల్ నడపండి:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

మీకు ఈ విధమైన స్పందన కనిపించాలి:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

"add2" వంటి లేని టూల్‌ను ఈ కమాండ్‌తో పరీక్షించండి:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

ఇప్పుడు మీ వాలిడేషన్ పనిచేస్తుందని ఈ సందేశం కనిపిస్తుంది:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

అలాగే, స్కీమా తిరస్కరించాల్సిన `c` అనే పారామీటర్‌ను ఇలా పంపండి:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

ఇప్పుడు "అసమర్థమైన ఆర్గ్యుమెంట్లు" లోపం కనిపిస్తుంది:

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

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారుల బాధ్యత మేము తీసుకోము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->