# மாதிரியை இயக்கவும்

> [!WARNING]
> இந்த மாதிரி பழைய Sampling மற்றும் மரபு HTTP+SSE தொடுப்பை பயன்படுத்துகிறது. இது MCP `2025-11-25` உடன் பொருந்துவதற்கு பாதுகாக்கப்பட்டுள்ளது. புதிய செயலாக்கங்கள் நேரடியாக LLM வழங்குநரை அழைக்க மற்றும் தொலை MCP போக்குவரத்துக்கு Streamable HTTP ஐ பயன்படுத்த வேண்டும்.
> 
> 

## மெய்நிகர் சூழலை உருவாக்கவும்

```sh
python -m venv venv
source ./venv/bin/activate
```

## சார்புகளைக் நிறுவவும்

```sh
pip install "mcp[cli]"
```

## சேவையகத்தை இயக்கவும்

```sh
uvicorn server:app --port 8000
```

## GitHub Copilot மற்றும் VS Code உடன் சேவையகத்தை பரிசோதிக்கவும்

mcp.jsonக்கு பதிவு இதுபோல் சேர்க்கவும்:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

சேவையகத்தில் "start" கிளிக் செய்யவேண்டும் என்பதனை உறுதிப்படுத்தவும்.

GitHub Copilot இல் கீழ்க்கண்ட முன்மொழிவை ஒட்டவும்:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

முதன்முறையாக நீங்கள் Sampling செயலை ஏற்றுக்கொள்ள வேண்டும் என்று கேட்கப்படுவீர்கள், அதன் பின்னர் "create_blog" என்ற கருவியை இயக்க ஒப்புக்கொள்ள வேண்டும். இதற்கு கீழ் போன்ற பதில் காண்பீர்கள்:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**மறுப்பு**:
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சி செய்துள்ளோம், ஆனால் தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கலாம் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் தாய்மொழியில் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கத்திற்கும் நாங்கள் பொறுப்பில்வில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->