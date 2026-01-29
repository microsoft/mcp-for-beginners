# MCP stdio Server - .NET தீர்வு

> **⚠️ முக்கியம்**: இந்த தீர்வு **stdio transport** பயன்படுத்துவதற்கு மேம்படுத்தப்பட்டுள்ளது, MCP Specification 2025-06-18 பரிந்துரைக்கப்பட்டபடி. முதன்மை SSE transport இப்போது நீக்கப்பட்டுள்ளது.

## கண்ணோட்டம்

இந்த .NET தீர்வு தற்போதைய stdio transport பயன்படுத்தி MCP server உருவாக்குவது எப்படி என்பதை விளக்குகிறது. stdio transport எளிமையானது, பாதுகாப்பானது மற்றும் நீக்கப்பட்ட SSE முறையை விட சிறந்த செயல்திறனை வழங்குகிறது.

## முன் தேவைகள்

- .NET 9.0 SDK அல்லது அதற்கு மேல்
- .NET dependency injection பற்றிய அடிப்படை அறிவு

## அமைப்பு வழிமுறைகள்

### படி 1: Dependencies மீட்டெடுக்கவும்

```bash
dotnet restore
```

### படி 2: Project ஐ Build செய்யவும்

```bash
dotnet build
```

## Server ஐ இயக்குதல்

stdio server பழைய HTTP அடிப்படையிலான server ஐ விட வேறுபட்ட முறையில் இயங்குகிறது. இது web server ஐ தொடங்குவதற்குப் பதிலாக stdin/stdout வழியாக தொடர்பு கொள்கிறது:

```bash
dotnet run
```

**முக்கியம்**: Server Hang ஆகும் போல தோன்றும் - இது சாதாரணம்! இது stdin மூலம் JSON-RPC செய்திகளை காத்திருக்கிறது.

## Server ஐ சோதனை செய்வது

### முறை 1: MCP Inspector பயன்படுத்துதல் (பரிந்துரைக்கப்படுகிறது)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

இது:
1. உங்கள் server ஐ subprocess ஆக தொடங்கும்
2. சோதனைக்கான web interface ஐ திறக்கும்
3. அனைத்து server tools ஐ interactive முறையில் சோதிக்க அனுமதிக்கும்

### முறை 2: நேரடி command line சோதனை

Inspector ஐ நேரடியாக தொடங்குவதன் மூலம் நீங்கள் சோதிக்கலாம்:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### கிடைக்கக்கூடிய Tools

Server கீழ்கண்ட tools ஐ வழங்குகிறது:

- **AddNumbers(a, b)**: இரண்டு எண்களை சேர்க்கவும்
- **MultiplyNumbers(a, b)**: இரண்டு எண்களை பெருக்கவும்  
- **GetGreeting(name)**: தனிப்பட்ட வரவேற்பை உருவாக்கவும்
- **GetServerInfo()**: Server பற்றிய தகவலை பெறவும்

### Claude Desktop உடன் சோதனை

இந்த server ஐ Claude Desktop உடன் பயன்படுத்த, உங்கள் `claude_desktop_config.json` இல் இந்த configuration ஐ சேர்க்கவும்:

```json
{
  "mcpServers": {
    "example-stdio-server": {
      "command": "dotnet",
      "args": ["run", "--project", "path/to/server.csproj"]
    }
  }
}
```

## Project அமைப்பு

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## HTTP/SSE உடன் உள்ள முக்கிய வேறுபாடுகள்

**stdio transport (தற்போதைய):**
- ✅ எளிய அமைப்பு - web server தேவையில்லை
- ✅ சிறந்த பாதுகாப்பு - HTTP endpoints தேவையில்லை
- ✅ `Host.CreateApplicationBuilder()` பயன்படுத்துகிறது `WebApplication.CreateBuilder()` க்கு பதிலாக
- ✅ `WithStdioTransport()` பயன்படுத்துகிறது `WithHttpTransport()` க்கு பதிலாக
- ✅ Console application, web application க்கு பதிலாக
- ✅ சிறந்த செயல்திறன்

**HTTP/SSE transport (நீக்கப்பட்டது):**
- ❌ ASP.NET Core web server தேவை
- ❌ `app.MapMcp()` routing அமைப்பு தேவை
- ❌ அதிக சிக்கலான configuration மற்றும் dependencies
- ❌ கூடுதல் பாதுகாப்பு கவனிக்க வேண்டியவை
- ❌ MCP 2025-06-18 இல் இப்போது நீக்கப்பட்டுள்ளது

## மேம்பாட்டு அம்சங்கள்

- **Dependency Injection**: Services மற்றும் logging க்கான முழுமையான DI ஆதரவு
- **Structured Logging**: `ILogger<T>` பயன்படுத்தி stderr க்கு சரியான logging
- **Tool Attributes**: `[McpServerTool]` attributes பயன்படுத்தி சுத்தமான tool வரையறை
- **Async Support**: அனைத்து tools க்கும் async செயல்பாடுகள் ஆதரவு
- **Error Handling**: மிருதுவான error handling மற்றும் logging

## மேம்பாட்டு குறிப்புகள்

- Logging க்காக `ILogger` ஐ பயன்படுத்தவும் (stdout க்கு நேரடியாக எழுத வேண்டாம்)
- சோதனைக்கு முன் `dotnet build` மூலம் build செய்யவும்
- Inspector ஐ visual debugging க்காக சோதிக்கவும்
- அனைத்து logging stderr க்கு தானாகவே செல்கிறது
- Server மிருதுவான shutdown signals ஐ கையாளுகிறது

இந்த தீர்வு தற்போதைய MCP specification ஐ பின்பற்றுகிறது மற்றும் .NET பயன்படுத்தி stdio transport செயல்படுத்துவதற்கான சிறந்த நடைமுறைகளை விளக்குகிறது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையைப் பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரச்செயல்முறையை உறுதிப்படுத்த முயற்சிக்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.