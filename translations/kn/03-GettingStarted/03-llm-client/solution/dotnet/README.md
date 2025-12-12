<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c40c54fa74ded9c223bc0ebfc8a2de7c",
  "translation_date": "2025-12-11T12:58:22+00:00",
  "source_file": "03-GettingStarted/03-llm-client/solution/dotnet/README.md",
  "language_code": "kn"
}
-->
# ಈ ಮಾದರಿಯನ್ನು ಚಾಲನೆ ಮಾಡಿ

> [!NOTE]
> ಈ ಮಾದರಿ ನೀವು GitHub Codespaces ಉದಾಹರಣೆಯನ್ನು ಬಳಸುತ್ತಿರುವಿರಿ ಎಂದು ಊಹಿಸುತ್ತದೆ. ನೀವು ಇದನ್ನು ಸ್ಥಳೀಯವಾಗಿ ಚಾಲನೆ ಮಾಡಲು ಬಯಸಿದರೆ, GitHub ನಲ್ಲಿ ವೈಯಕ್ತಿಕ ಪ್ರವೇಶ ಟೋಕನ್ (PAT) ಅನ್ನು ಹೊಂದಿಸಬೇಕಾಗುತ್ತದೆ.
>
> ```bash
> # zsh/bash
> export GITHUB_TOKEN="{{YOUR_GITHUB_PAT}}"
> ```
>
> ```powershell
> # PowerShell
> $env:GITHUB_TOKEN = "{{YOUR_GITHUB_PAT}}"
> ```

## ಗ್ರಂಥಾಲಯಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```sh
dotnet restore
```

ಕೆಳಗಿನ ಗ್ರಂಥಾಲಯಗಳನ್ನು ಸ್ಥಾಪಿಸಬೇಕು: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtcol 

## ಚಾಲನೆ

```sh 
dotnet run
```

ನೀವು ಕೆಳಗಿನಂತೆಯೇ ಔಟ್‌ಪುಟ್ ನೋಡಬಹುದು:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: Azure.AI.Inference.ChatCompletionsToolDefinition
Properties: {"a":{"type":"integer"},"b":{"type":"integer"}}
MCP Tools def: 0: Azure.AI.Inference.ChatCompletionsToolDefinition
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

ಬಹುತೇಕ ಔಟ್‌ಪುಟ್ ಡಿಬಗ್ ಮಾಡಲು ಮಾತ್ರವಾಗಿದೆ ಆದರೆ ಮುಖ್ಯವಾದುದು ನೀವು MCP ಸರ್ವರ್‌ನಿಂದ ಉಪಕರಣಗಳನ್ನು ಪಟ್ಟಿ ಮಾಡುತ್ತಿದ್ದೀರಿ, ಅವುಗಳನ್ನು LLM ಉಪಕರಣಗಳಾಗಿ ಪರಿವರ್ತಿಸಿ ಮತ್ತು ನೀವು MCP ಕ್ಲೈಂಟ್ ಪ್ರತಿಕ್ರಿಯೆ "Sum 6" ಅನ್ನು ಪಡೆಯುತ್ತೀರಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕರಣ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->