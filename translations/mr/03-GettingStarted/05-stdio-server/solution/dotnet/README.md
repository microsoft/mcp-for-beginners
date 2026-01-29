# MCP stdio Server - .NET समाधान

> **⚠️ महत्त्वाचे**: MCP Specification 2025-06-18 नुसार **stdio transport** वापरण्यासाठी हे समाधान अद्यतनित केले गेले आहे. मूळ SSE transport आता कालबाह्य झाले आहे.

## आढावा

हे .NET समाधान सध्याच्या stdio transport वापरून MCP सर्व्हर कसे तयार करायचे याचे उदाहरण देते. stdio transport अधिक सोपे, अधिक सुरक्षित आणि कालबाह्य SSE पद्धतीपेक्षा चांगली कार्यक्षमता प्रदान करते.

## पूर्वतयारी

- .NET 9.0 SDK किंवा त्यानंतरचे
- .NET dependency injection ची मूलभूत समज

## सेटअप सूचना

### चरण 1: Dependencies पुनर्संचयित करा

```bash
dotnet restore
```

### चरण 2: प्रकल्प तयार करा

```bash
dotnet build
```

## सर्व्हर चालवणे

stdio सर्व्हर जुन्या HTTP-आधारित सर्व्हरपेक्षा वेगळ्या प्रकारे चालतो. वेब सर्व्हर सुरू करण्याऐवजी, तो stdin/stdout च्या माध्यमातून संवाद साधतो:

```bash
dotnet run
```

**महत्त्वाचे**: सर्व्हर थांबलेला दिसेल - हे सामान्य आहे! तो stdin वरून JSON-RPC संदेशांची वाट पाहत आहे.

## सर्व्हर चाचणी करणे

### पद्धत 1: MCP Inspector वापरणे (शिफारस केलेले)

```bash
npx @modelcontextprotocol/inspector dotnet run
```

यामुळे:
1. तुमचा सर्व्हर subprocess म्हणून सुरू होईल
2. चाचणीसाठी वेब इंटरफेस उघडेल
3. सर्व्हर टूल्स परस्पर चाचणी करण्याची परवानगी देईल

### पद्धत 2: थेट कमांड लाइन चाचणी

तुम्ही Inspector थेट सुरू करून देखील चाचणी करू शकता:

```bash
npx @modelcontextprotocol/inspector dotnet run --project .
```

### उपलब्ध टूल्स

सर्व्हर खालील टूल्स प्रदान करतो:

- **AddNumbers(a, b)**: दोन संख्या एकत्र करा
- **MultiplyNumbers(a, b)**: दोन संख्या गुणाकार करा  
- **GetGreeting(name)**: वैयक्तिक अभिवादन तयार करा
- **GetServerInfo()**: सर्व्हरची माहिती मिळवा

### Claude Desktop सह चाचणी करणे

Claude Desktop सह हा सर्व्हर वापरण्यासाठी, तुमच्या `claude_desktop_config.json` मध्ये खालील कॉन्फिगरेशन जोडा:

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

## प्रकल्प संरचना

```
dotnet/
├── Program.cs           # Main server setup and configuration
├── Tools.cs            # Tool implementations
├── server.csproj       # Project file with dependencies
├── server.sln         # Solution file
├── Properties/         # Project properties
└── README.md          # This file
```

## HTTP/SSE पासून मुख्य फरक

**stdio transport (सध्याचे):**
- ✅ सोपी सेटअप - वेब सर्व्हरची गरज नाही
- ✅ चांगली सुरक्षा - HTTP endpoints नाहीत
- ✅ `Host.CreateApplicationBuilder()` चा वापर `WebApplication.CreateBuilder()` ऐवजी
- ✅ `WithStdioTransport()` चा वापर `WithHttpTransport()` ऐवजी
- ✅ Console application वेब application ऐवजी
- ✅ चांगली कार्यक्षमता

**HTTP/SSE transport (कालबाह्य):**
- ❌ ASP.NET Core वेब सर्व्हर आवश्यक
- ❌ `app.MapMcp()` routing सेटअप आवश्यक
- ❌ अधिक जटिल कॉन्फिगरेशन आणि dependencies
- ❌ अतिरिक्त सुरक्षा विचार
- ❌ MCP 2025-06-18 मध्ये आता कालबाह्य

## विकास वैशिष्ट्ये

- **Dependency Injection**: सेवांसाठी आणि लॉगिंगसाठी पूर्ण DI समर्थन
- **Structured Logging**: `ILogger<T>` वापरून stderr वर योग्य लॉगिंग
- **Tool Attributes**: `[McpServerTool]` attributes वापरून स्वच्छ टूल परिभाषा
- **Async Support**: सर्व टूल्स async ऑपरेशन्सला समर्थन देतात
- **Error Handling**: सौम्य त्रुटी हाताळणी आणि लॉगिंग

## विकास टिप्स

- लॉगिंगसाठी `ILogger` वापरा (कधीही stdout वर थेट लिहू नका)
- चाचणीपूर्वी `dotnet build` वापरून तयार करा
- दृश्यात्मक डीबगिंगसाठी Inspector सह चाचणी करा
- सर्व लॉगिंग आपोआप stderr वर जाते
- सर्व्हर सौम्य shutdown सिग्नल हाताळतो

हे समाधान सध्याच्या MCP specification चे पालन करते आणि .NET वापरून stdio transport अंमलबजावणीसाठी सर्वोत्तम पद्धती दाखवते.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरे त्रुटी किंवा अचूकतेच्या अभावाने युक्त असू शकतात. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.