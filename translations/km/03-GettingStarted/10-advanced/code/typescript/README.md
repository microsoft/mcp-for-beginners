# ដំណើរការឧទាហរណ៍

## តំឡើងការគាំទ្រ

```sh
npm install
```

## សង់វា

```sh
npm run build
```

## ដំណើរការ​វា

```sh
npm start
```

អ្នកគួរតែឃើញអក្សរ៖

```text
Registering tools...
Starting server...
```

ល្អណាស់ នេះមានន័យថាវាកំពុងចាប់ផ្តើមបានត្រឹមត្រូវ។

## សាកល្បងម៉ាស៊ីនបម្រើ

សាកល្បងគ្រប់សមត្ថភាពជាមួយពាក្យបញ្ជាដូចខាងក្រោម៖

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

នេះគួរតែផ្តើមផ្ទាំងបណ្ដាញនៃឧបករណ៍សួរត្រួតពិនិត្យ។

### សាកល្បងនៅម៉ូដ CLI

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

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

ដំណើរការ​ឧបករណ៍មួយ៖

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

អ្នកគួរតែឃើញចម្លើយស្រដៀងនឹង៖

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

សាកល្បងឧបករណ៍មួយដែលមិនមានដូចជា "add2" ជាមួយពាក្យបញ្ជានេះ៖

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

ឥឡូវនេះអ្នកគួរតែឃើញសារនេះបង្ហាញថាការត្រួតពិនិត្យរបស់អ្នកដំណើរការបាន៖

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

សាកល្បងផ្ញើប៉ារ៉ាម៉ែត្រ `c` ដែលគួរត្រូវបានបដិសេធដោយស្កីម៉ាដូចនេះ៖

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

ឥឡូវនេះអ្នកគួរតែឃើញប្រាប់កំហុស "អាគុយម៉ង់មិនត្រឹមត្រូវ"៖

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
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងដើម្បីបានភាពត្រឹមត្រូវ សូមយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬការខុសគ្នា។ ឯកសារដើមជាភាសាទំនើបគួរត្រូវបានគេពិចារណាជាមូលដ្ឋានព័ត៌មានដែលមានអំណាច។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញមនុស្សត្រូវបានផ្តល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំពីអ្នកឬការបកប្រែខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->