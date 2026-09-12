# stdio ट्रान्सपोर्टसह MCP सर्व्हर

> **⚠️ महत्त्वाचे अपडेट**: MCP स्पेसिफिकेशन 2025-06-18 पासून, स्वतंत्र SSE (सर्व्हर-सेंट इव्हेंट्स) ट्रान्सपोर्ट **डिप्रिकेटेड** करण्यात आली आहे आणि त्याऐवजी "Streamable HTTP" ट्रान्सपोर्ट लागू करण्यात आली आहे. सध्याच्या MCP स्पेसिफिकेशनमध्ये दोन मुख्य ट्रान्सपोर्ट यंत्रणा आहेत:
> 1. **stdio** - स्टँडर्ड इनपुट/आउटपुट (स्थानिक सर्व्हर्ससाठी शिफारस केली जाते)
> 2. **Streamable HTTP** - दूरच्या सर्व्हर्ससाठी जे अंतर्गत SSE वापरू शकतात
>
> ह्या धड्यात stdio ट्रान्सपोर्टवर भर दिला आहे, जे बहुसंख्य MCP सर्व्हर अंमलबजावणीसाठी शिफारस केलेले मार्ग आहे.

stdio ट्रान्सपोर्ट MCP सर्व्हर्सना क्लायंट्सशी स्टँडर्ड इनपुट आणि आउटपुट प्रवाहाद्वारे संवाद साधण्याची परवानगी देतो. हे सध्याच्या MCP स्पेसिफिकेशन मधील सर्वाधिक वापरलेले आणि शिफारस केलेले ट्रान्सपोर्ट आहे, जे सुलभ आणि कार्यक्षम मार्गाने MCP सर्व्हर तयार करण्यास मदत करतो जे विविध क्लायंट अ‍ॅप्लिकेशन्सशी सहजपणे एकत्र करता येतो.

## आढावा

हा धडा stdio ट्रान्सपोर्ट वापरून MCP सर्व्हर कसे तयार करायचे आणि वापरायचे हे समजावतो.

## शिकण्याचे उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:

- stdio ट्रान्सपोर्ट वापरून MCP सर्व्हर तयार करा.
- Inspector वापरून MCP सर्व्हर डिबग करा.
- Visual Studio Code वापरून MCP सर्व्हर वापरा.
- सध्याचे MCP ट्रान्सपोर्ट यंत्रणा समजून घ्या आणि stdio का शिफारस केली जाते हे समजून घ्या.


## stdio ट्रान्सपोर्ट - ते कसे कार्य करते

stdio ट्रान्सपोर्ट हा MCP स्पेसिफिकेशनच्या दोन मुख्य ट्रान्सपोर्टपैकी एक आहे
`2026-07-28`. ते कसे कार्य करते ते खाली आहे:

- **सोपे संवाद**: सर्व्हर JSON-RPC संदेश स्टँडर्ड इनपुट (`stdin`) पासून वाचतो आणि संदेश स्टँडर्ड आउटपुट (`stdout`) कडे पाठवतो.
- **प्रक्रिया-आधारित**: क्लायंट MCP सर्व्हर सबप्रॉसेस म्हणून लॉन्च करतो.
- **संदेश स्वरूप**: संदेश स्वतंत्र JSON-RPC विनंत्या, सूचनां किंवा प्रतिसाद असतात, आणि ते नवीन ओळीने विभक्त केलेले असतात.
- **लॉगिंग**: सर्व्हर लॉगिंगसाठी स्टँडर्ड एरर (`stderr`) वर UTF-8 स्ट्रिंग लिहू शकतो.

### मुख्य आवश्यकता:
- संदेशांना नवीन ओळीने विभक्त करणे आवश्यक आहे आणि त्यात अंतर्भूत नवीन ओळी नसाव्यात
- सर्व्हरने `stdout` वर केवळ वैध MCP संदेशच लिहावे
- क्लायंटने सर्व्हरच्या `stdin` वर केवळ वैध MCP संदेशच लिहावे

### TypeScript

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server(
  {
    name: "example-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

मागील कोडमध्ये:

- MCP SDK मधून `Server` क्लास आणि `StdioServerTransport` आयात करतो
- मूळ कॉन्फिगरेशन आणि क्षमता सह सर्व्हरची उदाहरण तयार करतो
- `StdioServerTransport` चे उदाहरण तयार करतो आणि सर्व्हरशी कनेक्ट करतो, ज्यामुळे stdin/stdout द्वारे संवाद शक्य होतो

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# सर्व्हर इंस्टन्स तयार करा
server = Server("example-server")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

मागील कोडमध्ये आपण:

- MCP SDK वापरून सर्व्हरचे उदाहरण तयार केले
- डेकोरेटर्स वापरून टूल्स परिभाषित केली
- stdio_server संदर्भ व्यवस्थापक वापरून ट्रान्सपोर्ट हाताळला

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

SSE पेक्षा मुख्य फरक असा आहे की stdio सर्व्हर्स:

- वेब सर्व्हर सेटअप किंवा HTTP एंडपॉईंट्सची गरज नाही
- क्लायंटने सबप्रॉसेस म्हणून लॉन्च केले जातात
- stdin/stdout प्रवाहाद्वारे संवाद साधतात
- अधिक सोपे अंमलबजावणी आणि डिबगिंग सुलभ करतात

## सराव: stdio सर्व्हर तयार करणे

आपला सर्व्हर तयार करताना आपण दोन गोष्टी लक्षात ठेवूया:

- कनेक्शन आणि संदेशांसाठी एंडपॉईंट्स उघडण्यासाठी वेब सर्व्हर वापरणे आवश्यक आहे.
## प्रयोगशाळा: सोपा MCP stdio सर्व्हर तयार करणे

या प्रयोगशाळेत, आपण शिफारस केलेली stdio ट्रान्सपोर्ट वापरून एक सोपा MCP सर्व्हर तयार करू. हा सर्व्हर ग्राहक मुद्रित करु शकतील असा टूल्स उपलब्ध करेल, जो स्टँडर्ड मॉडेल कंटेक्स्ट प्रोटोकॉल वापरतो.

### आवश्यकताः

- Python 3.8 किंवा नंतरचे
- MCP Python SDK: `pip install mcp`
- async प्रोग्रामिंगचे मूलभूत ज्ञान

चला आपला पहिला MCP stdio सर्व्हर तयार करूया:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# लॉगिंग कॉन्फिगर करा
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# सर्व्हर तयार करा
server = Server("example-stdio-server")

@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool() 
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    # stdio ट्रान्सपोर्ट वापरा
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## डिप्रिकेटेड SSE पद्धतीपासून मुख्य फरक

**Stdio ट्रान्सपोर्ट (सध्याचा मानक):**
- साधा सबप्रॉसेस मॉडेल - क्लायंट सर्व्हरला चाइल्ड प्रोसेस म्हणून लॉन्च करतो
- stdin/stdout द्वारे JSON-RPC संदेशांसह संवाद साधणे
- HTTP सर्व्हर सेटअपची गरज नाही
- अधिक कार्यक्षमता आणि सुरक्षितता
- डिबगिंग आणि विकास सोपे

**SSE ट्रान्सपोर्ट (MCP 2025-06-18 पासून डिप्रिकेटेड):**
- SSE एंडपॉईंट्ससह HTTP सर्व्हर आवश्यक
- वेब सर्व्हर इन्फ्रास्ट्रक्चरसह अधिक क्लिष्ट सेटअप
- HTTP एंडपॉईंट्ससाठी अतिरिक्त सुरक्षा बाबी
- वेब आधारित परिस्थितीसाठी आत्ताच Streamable HTTP बरोबर बदलले गेले

### stdio ट्रान्सपोर्टसह सर्व्हर तयार करणे

stdio सर्व्हर तयार करण्यासाठी आपण:

1. **आवश्यक लायब्ररी आयात करा** - MCP सर्व्हर घटक आणि stdio ट्रान्सपोर्ट आवश्यक आहे
2. **सर्व्हरची उदाहरण तयार करा** - त्याच्या क्षमतांसह सर्व्हर परिभाषित करा
3. **टूल्स परिभाषित करा** - आपण जे कार्यक्षमता उघडायची आहे ती जोडा
4. **ट्रान्सपोर्ट सेटअप करा** - stdio संवाद सानुकूल करा
5. **सर्व्हर चालवा** - सर्व्हर सुरू करा आणि संदेश हाताळा

आपण ह्या टप्प्याटप्प्याने तयार करूया:

### टप्पा 1: एक मूलभूत stdio सर्व्हर तयार करा

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# लॉगिंग कॉन्फिगर करा
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# सर्व्हर तयार करा
server = Server("example-stdio-server")

@server.tool()
def get_greeting(name: str) -> str:
    """Generate a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP stdio server."

async def main():
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

### टप्पा 2: अधिक टूल्स जोडा

```python
@server.tool()
def calculate_sum(a: int, b: int) -> int:
    """Calculate the sum of two numbers"""
    return a + b

@server.tool()
def calculate_product(a: int, b: int) -> int:
    """Calculate the product of two numbers"""
    return a * b

@server.tool()
def get_server_info() -> dict:
    """Get information about this MCP server"""
    return {
        "server_name": "example-stdio-server",
        "version": "1.0.0",
        "transport": "stdio",
        "capabilities": ["tools"]
    }
```

### टप्पा 3: सर्व्हर चालविणे

कोड `server.py` म्हणून जतन करा आणि कमांड लाइनवरून चालवा:

```bash
python server.py
```

सर्व्हर सुरू होईल आणि stdin कडून इनपुटची प्रतीक्षा करेल. तो stdio ट्रान्सपोर्टवर JSON-RPC संदेशांच्या माध्यमातून संवाद साधतो.

### टप्पा 4: Inspector सह चाचणी करणे

आपण आपला सर्व्हर MCP Inspector वापरून टेस्ट करू शकता:

1. Inspector इंस्टॉल करा: `npx @modelcontextprotocol/inspector`
2. Inspector चालवा आणि आपल्या सर्व्हरकडे निर्देशित करा
3. आपण तयार केलेल्या टूल्सची चाचणी करा

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## आपल्या stdio सर्व्हरचे डिबगिंग

### MCP Inspector वापरून

MCP Inspector हा MCP सर्व्हर डिबग आणि टेस्टिंगसाठी मौल्यवान टूल आहे. आपल्या stdio सर्व्हरसाठी त्याचा वापर कसा करायचा ते येथे आहे:

1. **Inspector इंस्टॉल करा**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector चालवा**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **आपला सर्व्हर टेस्ट करा**: Inspector आपल्याला वेब इंटरफेस पुरवतो जिथे आपण:
   - सर्व्हर क्षमतांचे निरीक्षण करू शकता
   - वेगवेगळ्या पॅरामीटर्ससह टूल्सची चाचणी करू शकता
   - JSON-RPC संदेशांचे निरीक्षण करू शकता
   - कनेक्शन समस्यांचे डिबगिंग करू शकता

### VS Code वापरून

आपण आपल्या MCP सर्व्हरचे डिबगिंग थेट VS Code मध्ये करू शकता:

1. `.vscode/launch.json` मध्ये लॉन्च कॉन्फिगरेशन तयार करा:
   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug MCP Server",
         "type": "python",
         "request": "launch",
         "program": "server.py",
         "console": "integratedTerminal"
       }
     ]
   }
   ```

2. आपल्या सर्व्हर कोडमध्ये ब्रेकपॉइंट सेट करा
3. डिबगर चालवा आणि Inspector सह टेस्ट करा

### सामान्य डिबगिंग टिपा

- लॉगिंगसाठी `stderr` वापरा - `stdout` वर कधीही लिहू नका कारण ते MCP संदेशांसाठी राखीव आहे
- सर्व JSON-RPC संदेश नवीन ओळीने विभक्त असावेत याची खात्री करा
- आधी सोप्या टूल्ससह चाचणी करा नंतर गुंतागुंतीची कार्यक्षमता जोडा
- संदेश स्वरूप तपासण्यासाठी Inspector वापरा

## VS Code मध्ये आपला stdio सर्व्हर वापरणे


एकदा आपण आपला MCP stdio सर्व्हर तयार केला की, आपण त्याला VS Code सोबत एकत्र करू शकता जेणेकरून तो Claude किंवा इतर MCP-सुसंगत क्लायंट्ससोबत वापरता येईल.

### संरचना

1. **MCP संरचना फाइल तयार करा** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) किंवा `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) येथे:

   ```json
   {
     "mcpServers": {
       "example-stdio-server": {
         "command": "python",
         "args": ["path/to/your/server.py"]
       }
     }
   }
   ```

2. **Claude पुन्हा सुरू करा**: नवीन सर्व्हर संरचना लोड करण्यासाठी Claude बंद करा आणि पुन्हा उघडा.

3. **संवाद तपासा**: Claude सोबत एक संभाषण सुरू करा आणि आपल्या सर्व्हरचे टूल्स वापरून पहा:
   - "तुम्ही अभिवादन साधनाचा वापर करून माझं अभिवादन करू शकता का?"
   - "15 आणि 27 चे बेरजे काढा"
   - "सर्व्हर माहिती काय आहे?"

### TypeScript stdio सर्व्हर उदाहरण

संदर्भासाठी येथे एक संपूर्ण TypeScript उदाहरण आहे:

```typescript
#!/usr/bin/env node
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "example-stdio-server",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// साधने जोडा
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "get_greeting",
        description: "Get a personalized greeting",
        inputSchema: {
          type: "object",
          properties: {
            name: {
              type: "string",
              description: "Name of the person to greet",
            },
          },
          required: ["name"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "get_greeting") {
    return {
      content: [
        {
          type: "text",
          text: `Hello, ${request.params.arguments?.name}! Welcome to MCP stdio server.`,
        },
      ],
    };
  } else {
    throw new Error(`Unknown tool: ${request.params.name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
}

runServer().catch(console.error);
```

### .NET stdio सर्व्हर उदाहरण

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

[McpServerToolType]
public class Tools
{
    [McpServerTool, Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [McpServerTool, Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## सारांश

या अद्ययावत धड्यात, आपण शिकले कसे:

- वर्तमान **stdio ट्रान्सपोर्ट** वापरून MCP सर्व्हर तयार करायचे (शिफारस केलेली पद्धत)
- SSE ट्रान्सपोर्ट stdio आणि Streamable HTTP च्या प्राधान्यामुळे काढून टाकले गेले का हे समजून घ्यायचे
- MCP क्लायंट्सद्वारे कॉल करता येणार्या टूल्स तयार करायचे
- MCP Inspector वापरून आपल्या सर्व्हरचे डिबगिंग करायचे
- stdio सर्व्हरला VS Code आणि Claude सोबत एकत्रित करायचे

stdio ट्रान्सपोर्ट हे SSE च्या आतापर्यंत वापरल्या गेलेल्या पद्धतींपेक्षा सोपे, सुरक्षित आणि अधिक कामगिरी करणारे MCP सर्व्हर तयार करण्यासाठी एक चांगला मार्ग आहे. 2025-06-18 च्या स्पेसिफिकेशननुसार, हे बहुतेक MCP सर्व्हर अंमलबजावणींसाठी शिफारस केलेले ट्रान्सपोर्ट आहे.


### .NET

1. प्रथम काही टूल्स तयार करू, यासाठी आपण *Tools.cs* नावाची फाइल तयार करू ज्यामध्ये खालील सामग्री असेल:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## सराव: आपला stdio सर्व्हर तपासणी

आता आपण आपला stdio सर्व्हर तयार केलात, तर त्याची योग्य प्रकारे कामगिरी असून नाही हे तपासूया.

### पूर्वअटी

1. तपासा की MCP Inspector स्थापित आहे का:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. आपला सर्व्हर कोड जतन केला गेलेला असावा (उदा., `server.py`)

### Inspector सोबत तपासणी

1. **Inspector आपला सर्व्हर सह सुरू करा**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **वेब इंटरफेस उघडा**: Inspector आपला सर्व्हर क्षमतांना दर्शविणारी ब्राउझर विंडो उघडेल.

3. **टूल्स तपासा**:
   - `get_greeting` टूल वेगवेगळ्या नावांसह वापरून पहा
   - `calculate_sum` टूल वेगवेगळ्या संख्यांसह तपासा
   - `get_server_info` टूल कॉल करा आणि सर्व्हर माहिती पहा

4. **संवाद देखरेख करा**: Inspector JSON-RPC संदेशांची देवाण-घेवाण दर्शवतो जी क्लायंट आणि सर्व्हर दरम्यान होते.

### काय पहायला हवे

जेव्हा आपला सर्व्हर योग्यरित्या सुरू होतो, तेव्हा आपण हे पाहू शकता:
- Inspector मध्ये सर्व्हर क्षमतांची यादी
- तपासणीसाठी टूल्स उपलब्ध आहेत
- यशस्वी JSON-RPC संदेश देवाणघेवाण
- इंटरफेसमध्ये टूल प्रतिसाद प्रदर्शित

### सामान्य समस्या आणि उपाय

**सर्व्हर सुरू होत नाही:**
- तपासा की सर्व अवलंबन स्थापित आहेत: `pip install mcp`
- Python चे सिंटॅक्स आणि इंडेंटेशन तपासा
- कन्सोलमध्ये त्रुटी संदेश पहा

**टूल्स दिसत नाहीत:**
- तपासा की `@server.tool()` डेकोरेटर्स उपस्थित आहेत
- `main()` आधी टूल फंक्शन्स निश्चित आहेत का ते पहा
- सर्व्हर योग्यरित्या संरच्यत आहे का ते तपासा

**कनेक्शन समस्या:**
- सर्व्हर stdio ट्रान्सपोर्ट योग्य प्रकारे वापरत आहे का हे सुनिश्चित करा
- इतर प्रक्रिया अडथळा करून नाहीत याची खात्री करा
- Inspector आदेशाचे सिंटॅक्स सत्यापित करा

## कार्य

आपल्‍या सर्व्हरमध्ये अधिक क्षमता वाढवण्याचा प्रयत्न करा. उदाहरणार्थ, API कॉल करणारा टूल जोडण्यासाठी [ही पृष्ठ](https://api.chucknorris.io/) पहा. तुम्ही ठरवा सर्व्हर कसा दिसायला हवा. मजा करा :)
## समाधान

[उपाय](./solution/README.md) येथे एक शक्य समाधान आहे ज्यात काम करणारा कोड आहे.

## मुख्य मुद्दे

या प्रकरणातून मुख्य मुद्दे हे आहेत:

- stdio ट्रान्सपोर्ट हा स्थानिक MCP सर्व्हरांसाठी शिफारस केलेला मार्ग आहे.
- stdio ट्रान्सपोर्ट MCP सर्व्हर आणि क्लायंटच्या दरम्यान मानक इनपुट आणि आउटपुट स्ट्रीम्स वापरून अखंड संवाद साधण्याची परवानगी देतो.
- आपण Inspector आणि Visual Studio Code दोन्ही वापरून stdio सर्व्हर्स थेट वापरू शकता, ज्यामुळे डिबगिंग आणि एकत्रीकरण सोपे होते.

## नमुने

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## अतिरिक्त स्रोत

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## पुढे काय

## पुढील पावले

आता आपण stdio ट्रान्सपोर्टसह MCP सर्व्हर तयार करायला शिकलात, आपण अधिक प्रगत विषयांवर देखील अभ्यास करू शकता:

- **पुढे**: [MCP सह HTTP Streaming (Streamable HTTP)](../06-http-streaming/README.md) - दूरस्थ सर्व्हर साठी इतर समर्थन केलेल्या ट्रान्सपोर्टचा अध्याय
- **प्रगत**: [MCP सुरक्षा सर्वोत्तम पद्धती](../../02-Security/README.md) - आपल्या MCP सर्व्हरमध्ये सुरक्षा लागू करा
- **उत्पादनासाठी**: [तैनाती धोरणे](../09-deployment/README.md) - आपल्या सर्व्हरचे उत्पादन वापरासाठी तैनात करा

## अतिरिक्त स्रोत

- [MCP स्पेसिफिकेशन 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - सध्याची स्पेसिफिकेशन
- [MCP SDK दस्तऐवज](https://github.com/modelcontextprotocol/sdk) - सर्व भाषा साठी SDK संदर्भ
- [समुदाय उदाहरणे](../../06-CommunityContributions/README.md) - समुदायाकडून अधिक सर्व्हर उदाहरणे

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेची कमतरता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थलावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->