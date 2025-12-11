<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b4662e0a75e645f3eeb4e69e5ba905f4",
  "translation_date": "2025-12-11T13:39:36+00:00",
  "source_file": "03-GettingStarted/10-advanced/code/typescript/README.md",
  "language_code": "kn"
}
-->
# ಮಾದರಿ ಚಾಲನೆ

## ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```sh
npm install
```

## ಅದನ್ನು ನಿರ್ಮಿಸಿ

```sh
npm run build
```

## ಅದನ್ನು ಚಾಲನೆ ಮಾಡಿ

```sh
npm start
```

ನೀವು ಈ ಪಠ್ಯವನ್ನು ನೋಡಬೇಕು:

```text
Registering tools...
Starting server...
```

ಉತ್ತಮ, ಅಂದರೆ ಅದು ಸರಿಯಾಗಿ ಪ್ರಾರಂಭವಾಗುತ್ತಿದೆ.

## ಸರ್ವರ್ ಅನ್ನು ಪರೀಕ್ಷಿಸಿ

ಕೆಳಗಿನ ಆಜ್ಞೆಯೊಂದಿಗೆ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ:

```sh
npx @modelcontextprotocol/inspector node build/app.js
```

ಇದು ಇನ್ಸ್ಪೆಕ್ಟರ್ ಟೂಲ್‌ನ ವೆಬ್ ಇಂಟರ್ಫೇಸ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಬೇಕು.

### CLI ಮೋಡ್‌ನಲ್ಲಿ ಪರೀಕ್ಷಿಸಿ

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/list
```

ನೀವು ಕೆಳಗಿನ ಔಟ್‌ಪುಟ್ ಅನ್ನು ನೋಡಬೇಕು:

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

ಒಂದು ಟೂಲ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg b=2
```

ನೀವು ಹೀಗೊಂದು ಪ್ರತಿಕ್ರಿಯೆಯನ್ನು ನೋಡಬೇಕು:

```text
{
  "content": [
    {
      "type": "text",
      "text": "Tool add called with arguments: {\"a\":1,\"b\":2}, result: {\"content\":[{\"type\":\"text\",\"text\":\"3\"}]}"
    }
  ]
```

"add2" ಎಂಬ ಅಸ್ತಿತ್ವದಲ್ಲಿಲ್ಲದ ಟೂಲ್ ಅನ್ನು ಈ ಆಜ್ಞೆಯೊಂದಿಗೆ ಪರೀಕ್ಷಿಸಿ:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add2 --tool-arg a=1 --tool-arg b=2
```

ನೀವು ಈಗ ನಿಮ್ಮ ಮಾನ್ಯತೆ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿದೆ ಎಂದು ತೋರಿಸುವ ಈ ಸಂದೇಶವನ್ನು ನೋಡಬೇಕು:

```text
{
  "content": [],
  "error": {
    "code": "tool_not_found",
    "message": "Tool add2 not found."
  }
```

ಹಾಗೂ `c` ಎಂಬ ಪರಿಮಾಣವನ್ನು schema ಮೂಲಕ ನಿರಾಕರಿಸಬೇಕಾದಂತೆ ಕಳುಹಿಸುವುದನ್ನು ಪ್ರಯತ್ನಿಸಿ:

```sh
npx @modelcontextprotocol/inspector --cli node ./build/app.js --method tools/call --tool-name add --tool-arg a=1 --tool-arg c=2
```

ನೀವು ಈಗ "ಅಮಾನ್ಯವಾದ ವಾದಗಳು" ದೋಷವನ್ನು ನೋಡಬೇಕು:

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
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->