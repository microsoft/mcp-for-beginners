# இந்த மாதிரியை இயக்குதல்

இது LLM கிளையன்ட் எடுத்துக்காட்டிற்கான Rust தீர்வு. உங்கள் கணினியில் Rust டூல்செயின் நிறுவப்பட்டிருக்க வேண்டும்; [அதிகாரபூர்வ நிறுவல் வழிகாட்டியை](https://www.rust-lang.org/tools/install) பார்க்கவும்.

கிளையன்ட் Azure OpenAI வழியாக வெளியிடப்பட்ட Microsoft Foundry
மாடலை v1 endpoint மூலம் அழைக்கிறது.

> [!NOTE]
> கொடுக்கப்பட்ட மதிப்பு `model` என்பது உங்கள் Foundry டெப்ளாய்மெண்ட் பெயர்,
> அது அவசியமாய் அடிப்படை மாதிரி பெயர் ஆக இருக்காது.

## -0- Microsoft Foundry ஐ அமைக்கவும்

```bash
# zsh/bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

```powershell
# PowerShell
$env:AZURE_OPENAI_ENDPOINT = "https://<resource-name>.openai.azure.com"
$env:AZURE_OPENAI_API_KEY = "<api-key>"
$env:AZURE_OPENAI_DEPLOYMENT = "gpt-5.1"
```

## -1- மாதிரியை கட்டமைக்கவும்

```bash
cargo build
```

## -2- மாதிரியை இயக்கவும்

```bash
cargo run
```

கிளையன்ட் calculator MCP சர்வரை துவக்கி, அதன் கருவி பட்டியலை பெற்று, மற்றும்
ஒப்படைக்கப்பட்ட மாதிரியை பயன்படுத்தி `add` கருவியை அழைக்கிறது. நீங்கள் வெளியீட்டில்
கருவி அழைப்பு (உதாரணமாக, "Calling tool: add") மற்றும் அதன் அழைப்பின் முடிவை காணலாம்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->