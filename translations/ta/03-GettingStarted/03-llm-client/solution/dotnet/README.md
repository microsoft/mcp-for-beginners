# இந்த உதாரணத்தை இயக்கவும்

> [!NOTE]
> Microsoft Foundry-இல் `gpt-5.1` போன்ற செயல்பாட்டிலுள்ள ஒரு மாதிரியை வழங்கி
> அதன் endpoint, API key மற்றும் deployment name-ஐ அமைக்கவும்.
>
> ```bash
> # zsh/bash
> export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
> export AZURE_OPENAI_API_KEY="<api-key>"
> export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
> ```
>
> ```powershell
> # PowerShell
> $env:AZURE_OPENAI_ENDPOINT = "https://<resource-name>.openai.azure.com"
> $env:AZURE_OPENAI_API_KEY = "<api-key>"
> $env:AZURE_OPENAI_DEPLOYMENT = "gpt-5.1"
> ```

## நூலகங்களை நிறுவுக

```sh
dotnet restore
```

இது OpenAI .NET கிளையன்டையும் Model Context Protocol SDK-ஐயும் நிறுவும்.

## இயக்கவும்

```sh 
dotnet run
```

உங்களுக்கு இதுபோன்ற ஒரு வெளியீடு காணப்படும்:

```text
Setting up stdio transport
Listing tools
Connected to server with tools: Add
Tool description: Adds two numbers
Tool parameters: {"title":"Add","description":"Adds two numbers","type":"object","properties":{"a":{"type":"integer"},"b":{"type":"integer"}},"required":["a","b"]}
Tool definition: OpenAI.Chat.ChatTool
MCP Tools def: 0: OpenAI.Chat.ChatTool
Tool call 0: Add with arguments {"a":2,"b":4}
Sum 6
```

பல வெளியீடுகள் வெறும் டிபக்கிங் தகவல்களே இருக்கும்; ஆனால் முக்கியமானது நீங்கள் MCP Server-இருந்து கருவிகளை பட்டியலிடுகிறீர்கள், அவற்றை LLM கருவிகளாக மாற்றுகிறீர்கள், பின்னர் MCP கிளையன்ட் பதிலாக நீங்கள் "Sum 6" என்பதை பெறுவீர்கள்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->