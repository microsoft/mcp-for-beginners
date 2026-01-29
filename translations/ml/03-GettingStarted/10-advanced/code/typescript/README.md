# സാമ്പിൾ പ്രവർത്തിപ്പിക്കുക

## ആശ്രിതങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```sh
npm install
```

## ഇത് നിർമ്മിക്കുക

```sh
npm run build
```

## ഇത് പ്രവർത്തിപ്പിക്കുക

```sh
npm start
```

നിങ്ങൾക്ക് താഴെ കാണുന്ന വാചകം കാണിക്കണം:

```text
Registering tools...
Starting server...
```

ശ്രേഷ്ഠം, അതായത് ഇത് ശരിയായി ആരംഭിക്കുന്നു.

## സെർവർ പരിശോധിക്കുക

താഴെ കാണുന്ന കമാൻഡ് ഉപയോഗിച്ച് കഴിവുകൾ പരിശോധിക്കുക:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

ഇത് ഇൻസ്പെക്ടർ ടൂളിന്റെ വെബ് ഇന്റർഫേസ് ആരംഭിക്കണം.

### CLI മോഡിൽ പരിശോധിക്കുക

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

നിങ്ങൾക്ക് താഴെ കാണുന്ന ഔട്ട്പുട്ട് കാണിക്കണം:

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

ഒരു ടൂൾ പ്രവർത്തിപ്പിക്കുക:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

നിങ്ങൾക്ക് ഇതുപോലുള്ള പ്രതികരണം കാണിക്കണം:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

"add2" പോലുള്ള നിലവിലില്ലാത്ത ഒരു ടൂൾ പരിശോധിക്കാൻ ഈ കമാൻഡ് ഉപയോഗിക്കുക:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

ഇപ്പോൾ നിങ്ങളുടെ പരിശോധന പ്രവർത്തിക്കുന്നതായി കാണിക്കുന്ന ഈ സന്ദേശം നിങ്ങൾക്ക് കാണിക്കണം:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

പിന്നീട് സ്കീമയിൽ നിരസിക്കപ്പെടേണ്ട `c` എന്ന പാരാമീറ്റർ അയയ്ക്കാൻ ശ്രമിക്കുക:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

ഇപ്പോൾ "അസാധുവായ വാദങ്ങൾ" എന്ന പിശക് നിങ്ങൾക്ക് കാണിക്കണം:

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
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->