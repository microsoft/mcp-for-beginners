# இந்த மாதிரியை இயக்கவும்

> [!NOTE]
> இந்த மாதிரி நீங்கள் GitHub Codespaces instance-ஐ பயன்படுத்துகிறீர்கள் என்று கருதுகிறது. இதை உள்ளூரில் இயக்க விரும்பினால், GitHub-ல் ஒரு தனிப்பட்ட அணுகல் டோக்கன் (PAT) அமைக்க வேண்டும்.
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

## நூலகங்களை நிறுவவும்

```sh
dotnet restore
```

கீழ்க்கண்ட நூலகங்களை நிறுவ வேண்டும்: Azure AI Inference, Azure Identity, Microsoft.Extension, Model.Hosting, ModelContextProtocol 

## இயக்கவும்

```sh 
dotnet run
```

நீங்கள் இதற்குச் சமமான ஒரு வெளியீட்டை காணலாம்:

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

வெளியீட்டில் பெரும்பாலானவை டிபகிங் தகவல்களாக இருக்கும், ஆனால் முக்கியமானது MCP Server-இல் இருந்து கருவிகளை பட்டியலிடுவது, அவற்றை LLM கருவிகளாக மாற்றுவது, மற்றும் MCP client response "Sum 6" ஆக முடிவடைவது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் நோக்கம் துல்லியமாக இருக்க வேண்டும் என்பதுதான், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.