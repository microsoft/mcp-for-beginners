<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6d6315e03f591fb5a39be91da88585dc",
  "translation_date": "2025-12-11T12:57:33+00:00",
  "source_file": "03-GettingStarted/03-llm-client/solution/typescript/README.md",
  "language_code": "kn"
}
-->
# ಈ ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡುವುದು

ಈ ಮಾದರಿಯಲ್ಲಿ ಕ್ಲೈಂಟ್‌ನಲ್ಲಿ LLM ಇರಬೇಕು. LLM ನಿಮಗೆ ಇದನ್ನು Codespaces ನಲ್ಲಿ ಚಾಲನೆ ಮಾಡಲು ಅಥವಾ GitHub ನಲ್ಲಿ ವೈಯಕ್ತಿಕ ಪ್ರವೇಶ ಟೋಕನ್ ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಲು ಅಗತ್ಯವಿದೆ.

## -1- ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```bash
npm install
```

## -3- ಸರ್ವರ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ


```bash
npm run build
```

## -4- ಕ್ಲೈಂಟ್ ಅನ್ನು ಚಾಲನೆ ಮಾಡಿ

```sh
npm run client
```

ನೀವು ಈ ರೀತಿಯ ಫಲಿತಾಂಶವನ್ನು ನೋಡಬಹುದು:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->