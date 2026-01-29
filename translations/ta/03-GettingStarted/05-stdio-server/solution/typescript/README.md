# MCP stdio Server - TypeScript தீர்வு

> **⚠️ முக்கியம்**: இந்த தீர்வு **stdio transport** பயன்படுத்துவதற்கு புதுப்பிக்கப்பட்டுள்ளது, MCP Specification 2025-06-18 பரிந்துரைப்படி. முதன்மை SSE transport தற்போது நீக்கப்பட்டுள்ளது.

## மேலோட்டம்

இந்த TypeScript தீர்வு stdio transport பயன்படுத்தி MCP server உருவாக்குவதற்கான முறையை விளக்குகிறது. stdio transport எளிமையானது, பாதுகாப்பானது மற்றும் SSE முறையை விட சிறந்த செயல்திறனை வழங்குகிறது.

## முன் தேவைகள்

- Node.js 18+ அல்லது அதற்கு மேல்
- npm அல்லது yarn package manager

## அமைப்புக்கான வழிமுறைகள்

### படி 1: தேவையான dependencies நிறுவவும்

```bash
npm install
```

### படி 2: திட்டத்தை உருவாக்கவும்

```bash
npm run build
```

## Server ஐ இயக்குதல்

stdio server பழைய SSE server ஐ விட வேறுபட்ட முறையில் இயங்குகிறது. ஒரு web server ஐ தொடங்குவதற்கு பதிலாக, இது stdin/stdout மூலம் தொடர்பு கொள்கிறது:

```bash
npm start
```

**முக்கியம்**: Server தடைபட்டது போல தோன்றும் - இது சாதாரணம்! இது stdin மூலம் JSON-RPC செய்திகளை காத்திருக்கிறது.

## Server ஐ சோதனை செய்வது

### முறை 1: MCP Inspector பயன்படுத்துதல் (பரிந்துரைக்கப்படுகிறது)

```bash
npm run inspector
```

இது:
1. உங்கள் server ஐ ஒரு subprocess ஆக தொடங்கும்
2. சோதனைக்கான ஒரு web interface ஐ திறக்கும்
3. அனைத்து server tools ஐ interactive முறையில் சோதிக்க அனுமதிக்கும்

### முறை 2: நேரடி command line சோதனை

Inspector ஐ நேரடியாக தொடங்குவதன் மூலம் நீங்கள் சோதனை செய்யலாம்:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

### கிடைக்கக்கூடிய Tools

Server கீழ்க்கண்ட tools ஐ வழங்குகிறது:

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
      "command": "node",
      "args": ["path/to/build/index.js"]
    }
  }
}
```

## திட்ட அமைப்பு

```
typescript/
├── src/
│   └── index.ts          # Main server implementation
├── build/                # Compiled JavaScript (generated)
├── package.json          # Project configuration
├── tsconfig.json         # TypeScript configuration
└── README.md            # This file
```

## SSE முறையிலிருந்து முக்கிய வேறுபாடுகள்

**stdio transport (தற்போதைய):**
- ✅ எளிய அமைப்பு - HTTP server தேவையில்லை
- ✅ சிறந்த பாதுகாப்பு - HTTP endpoints தேவையில்லை
- ✅ Subprocess அடிப்படையிலான தொடர்பு
- ✅ stdin/stdout மூலம் JSON-RPC
- ✅ சிறந்த செயல்திறன்

**SSE transport (நீக்கப்பட்டது):**
- ❌ Express server அமைப்பு தேவை
- ❌ சிக்கலான routing மற்றும் session மேலாண்மை தேவை
- ❌ கூடுதல் dependencies (Express, HTTP handling)
- ❌ கூடுதல் பாதுகாப்பு கவனிக்க வேண்டியது
- ❌ MCP 2025-06-18 இல் தற்போது நீக்கப்பட்டது

## மேம்பாட்டு குறிப்புகள்

- பதிவு செய்ய `console.error()` ஐ பயன்படுத்தவும் (`console.log()` ஐ பயன்படுத்த வேண்டாம், இது stdout இல் எழுதுகிறது)
- சோதனைக்கு முன் `npm run build` மூலம் build செய்யவும்
- Inspector ஐ visual debugging க்கு பயன்படுத்தவும்
- அனைத்து JSON செய்திகளும் சரியாக வடிவமைக்கப்பட்டுள்ளதை உறுதிப்படுத்தவும்
- Server SIGINT/SIGTERM இல் தானாகவே graceful shutdown ஐ கையாளும்

இந்த தீர்வு தற்போதைய MCP specification ஐ பின்பற்றுகிறது மற்றும் TypeScript பயன்படுத்தி stdio transport செயல்படுத்துவதற்கான சிறந்த நடைமுறைகளை விளக்குகிறது.

---

**அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது துல்லியக்குறைபாடுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் சொந்த மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்களுக்கும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பல்ல.