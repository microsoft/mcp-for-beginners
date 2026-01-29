# MCP stdio Server - Python Solution

> **⚠️ முக்கியம்**: இந்த தீர்வு **stdio transport** பயன்படுத்துவதற்கு மேம்படுத்தப்பட்டுள்ளது, MCP Specification 2025-06-18 பரிந்துரைப்படி. பழைய SSE transport தற்போது நீக்கப்பட்டுள்ளது.

## மேலோட்டம்

இந்த Python தீர்வு stdio transport பயன்படுத்தி MCP server உருவாக்குவது எப்படி என்பதை விளக்குகிறது. stdio transport எளிமையானது, பாதுகாப்பானது மற்றும் பழைய SSE முறையை விட சிறந்த செயல்திறனை வழங்குகிறது.

## முன் தேவைகள்

- Python 3.8 அல்லது அதற்கு மேல்
- `uv` package management க்காக நிறுவ பரிந்துரைக்கப்படுகிறது, [வழிமுறைகளை](https://docs.astral.sh/uv/#highlights) பார்க்கவும்

## அமைப்புக்கான வழிமுறைகள்

### படி 1: ஒரு virtual environment உருவாக்கவும்

```bash
python -m venv venv
```

### படி 2: virtual environment ஐ செயல்படுத்தவும்

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### படி 3: தேவையான dependencies ஐ நிறுவவும்

```bash
pip install mcp
```

## Server ஐ இயக்குவது

stdio server பழைய SSE server ஐ விட வேறுபட்ட முறையில் இயங்குகிறது. இது web server ஐ தொடங்குவதற்குப் பதிலாக stdin/stdout மூலம் தொடர்பு கொள்கிறது:

```bash
python server.py
```

**முக்கியம்**: Server hang ஆகும் போல தோன்றும் - இது சாதாரணம்! இது stdin மூலம் JSON-RPC messages க்காக காத்திருக்கிறது.

## Server ஐ சோதனை செய்வது

### முறை 1: MCP Inspector பயன்படுத்துவது (பரிந்துரைக்கப்படுகிறது)

```bash
npx @modelcontextprotocol/inspector python server.py
```

இது:
1. உங்கள் server ஐ subprocess ஆக தொடங்கும்
2. சோதனைக்கான ஒரு web interface ஐ திறக்கும்
3. அனைத்து server tools ஐ interactive ஆக சோதிக்க அனுமதிக்கும்

### முறை 2: நேரடி JSON-RPC சோதனை

நீங்கள் JSON-RPC messages ஐ நேரடியாக அனுப்பி சோதிக்கலாம்:

1. Server ஐ தொடங்கவும்: `python server.py`
2. JSON-RPC message ஐ அனுப்பவும் (உதாரணம்):

```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

3. Server கிடைக்கும் tools ஐ பதிலளிக்கும்

### கிடைக்கும் Tools

Server இந்த tools ஐ வழங்குகிறது:

- **add(a, b)**: இரண்டு எண்களை சேர்க்கவும்
- **multiply(a, b)**: இரண்டு எண்களை பெருக்கவும்  
- **get_greeting(name)**: தனிப்பட்ட வரவேற்பை உருவாக்கவும்
- **get_server_info()**: Server பற்றிய தகவலை பெறவும்

### Claude Desktop உடன் சோதனை செய்வது

இந்த server ஐ Claude Desktop உடன் பயன்படுத்த, உங்கள் `claude_desktop_config.json` இல் இந்த configuration ஐ சேர்க்கவும்:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "python",
      "args": ["path/to/server.py"]
    }
  }
}
```

## SSE உடன் முக்கிய வேறுபாடுகள்

**stdio transport (தற்போதைய):**
- ✅ எளிய அமைப்பு - web server தேவையில்லை
- ✅ சிறந்த பாதுகாப்பு - HTTP endpoints தேவையில்லை
- ✅ Subprocess அடிப்படையிலான தொடர்பு
- ✅ stdin/stdout மூலம் JSON-RPC
- ✅ சிறந்த செயல்திறன்

**SSE transport (நீக்கப்பட்டது):**
- ❌ HTTP server அமைப்பு தேவை
- ❌ Web framework (Starlette/FastAPI) தேவை
- ❌ Routing மற்றும் session management சிக்கலானது
- ❌ கூடுதல் பாதுகாப்பு கவனிக்க வேண்டியது
- ❌ MCP 2025-06-18 இல் தற்போது நீக்கப்பட்டது

## Debugging Tips

- `stderr` ஐ logging க்காக பயன்படுத்தவும் (`stdout` ஐ பயன்படுத்த வேண்டாம்)
- Visual debugging க்காக Inspector ஐ சோதிக்கவும்
- அனைத்து JSON messages newline-delimited ஆக உள்ளதா என்பதை உறுதிப்படுத்தவும்
- Server எந்தவிதமான பிழைகளும் இல்லாமல் தொடங்குகிறதா என்பதை சரிபார்க்கவும்

இந்த தீர்வு தற்போதைய MCP specification ஐ பின்பற்றுகிறது மற்றும் stdio transport செயல்பாட்டிற்கான சிறந்த நடைமுறைகளை விளக்குகிறது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சிக்கின்றோம், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறான தகவல்கள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளுங்கள். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.