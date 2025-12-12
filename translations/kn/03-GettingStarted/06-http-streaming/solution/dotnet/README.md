<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "dde4e32e4b55ef4962c411b39d2340a7",
  "translation_date": "2025-12-11T13:27:39+00:00",
  "source_file": "03-GettingStarted/06-http-streaming/solution/dotnet/README.md",
  "language_code": "kn"
}
-->
# ಈ ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡುವುದು

## -1- ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```bash
dotnet restore
```

## -2- ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡು

```bash
dotnet run
```

## -3- ಮಾದರಿಯನ್ನು ಪರೀಕ್ಷಿಸಿ

ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಚಾಲನೆ ಮಾಡುವ ಮೊದಲು ಬೇರೆ ಟರ್ಮಿನಲ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಿ (ಸರ್ವರ್ ಇನ್ನೂ ಚಾಲನೆ ಆಗಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ).

ಒಂದು ಟರ್ಮಿನಲ್‌ನಲ್ಲಿ ಸರ್ವರ್ ಚಾಲನೆ ಆಗಿರುವಾಗ, ಮತ್ತೊಂದು ಟರ್ಮಿನಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಚಾಲನೆ ಮಾಡಿ:

```bash
npx @modelcontextprotocol/inspector http://localhost:3001
```

ಇದು ಮಾದರಿಯನ್ನು ಪರೀಕ್ಷಿಸಲು ದೃಶ್ಯಾತ್ಮಕ ಇಂಟರ್ಫೇಸ್ ಹೊಂದಿರುವ ವೆಬ್ ಸರ್ವರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಬೇಕು.

> **Streamable HTTP** ಅನ್ನು ಸಾರಣಿಯ ಪ್ರಕಾರವಾಗಿ ಆಯ್ಕೆಮಾಡಲಾಗಿದೆ ಮತ್ತು URL `http://localhost:3001/mcp` ಆಗಿದೆ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

ಸರ್ವರ್ ಸಂಪರ್ಕಗೊಂಡ ನಂತರ:

- ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡಿ ಮತ್ತು `add` ಅನ್ನು 2 ಮತ್ತು 4 ಎಂಬ ಆರ್ಗ್ಯುಮೆಂಟ್‌ಗಳೊಂದಿಗೆ ಚಾಲನೆ ಮಾಡಿ, ಫಲಿತಾಂಶದಲ್ಲಿ 6 ಕಾಣಿಸಬೇಕು.
- ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಸಂಪನ್ಮೂಲ ಟೆಂಪ್ಲೇಟ್ಗೆ ಹೋಗಿ "greeting" ಅನ್ನು ಕರೆ ಮಾಡಿ, ಒಂದು ಹೆಸರು ಟೈಪ್ ಮಾಡಿ ಮತ್ತು ನೀವು ನೀಡಿದ ಹೆಸರಿನೊಂದಿಗೆ ಒಂದು ಸ್ವಾಗತ ಸಂದೇಶವನ್ನು ಕಾಣಬೇಕು.

### CLI ಮೋಡ್‌ನಲ್ಲಿ ಪರೀಕ್ಷೆ

ನೀವು ಕೆಳಗಿನ ಆಜ್ಞೆಯನ್ನು ಚಾಲನೆ ಮಾಡುವ ಮೂಲಕ ನೇರವಾಗಿ CLI ಮೋಡ್‌ನಲ್ಲಿ ಅದನ್ನು ಪ್ರಾರಂಭಿಸಬಹುದು:

```bash 
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/list
```

ಇದು ಸರ್ವರ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಎಲ್ಲಾ ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುತ್ತದೆ. ನೀವು ಕೆಳಗಿನ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಕಾಣಬೇಕು:

```text
{
  "tools": [
    {
      "name": "AddNumbers",
      "description": "Add two numbers together.",
      "inputSchema": {
        "type": "object",
        "properties": {
          "a": {
            "description": "The first number",
            "type": "integer"
          },
          "b": {
            "description": "The second number",
            "type": "integer"
          }
        },
        "title": "AddNumbers",
        "description": "Add two numbers together.",
        "required": [
          "a",
          "b"
        ]
      }
    }
  ]
}
```

ಉಪಕರಣವನ್ನು ಕರೆ ಮಾಡಲು ಟೈಪ್ ಮಾಡಿ:

```bash
npx @modelcontextprotocol/inspector --cli http://localhost:3001 --method tools/call --tool-name AddNumbers --tool-arg a=1 --tool-arg b=2
```

ನೀವು ಕೆಳಗಿನ ಔಟ್‌ಪುಟ್ ಅನ್ನು ಕಾಣಬೇಕು:

```text
{
  "content": [
    {
      "type": "text",
      "text": "3"
    }
  ],
  "isError": false
}
```

> [!TIP]
> ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಹೋಲಿಸಿದರೆ CLI ಮೋಡ್‌ನಲ್ಲಿ ಇನ್ಸ್ಪೆಕ್ಟರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡುವುದು ಸಾಮಾನ್ಯವಾಗಿ ಬಹಳ ವೇಗವಾಗಿದೆ.
> ಇನ್ಸ್ಪೆಕ್ಟರ್ ಬಗ್ಗೆ ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗಾಗಿ [ಇಲ್ಲಿ](https://github.com/modelcontextprotocol/inspector) ಓದಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->