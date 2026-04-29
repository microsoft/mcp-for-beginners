# stdio ट्रान्सपोर्टसह MCP सर्व्हर

> **⚠️ महत्त्वाचे अद्यतन**: MCP स्पेसिफिकेशन 2025-06-18 नुसार, स्वतंत्र SSE (सर्व्हर-सेंट इव्हेंट्स) ट्रान्सपोर्ट **डिप्रिकेट** करण्यात आला असून "स्ट्रीमबल HTTP" ट्रान्सपोर्टने त्याचा बदल केला आहे. वर्तमान MCP स्पेसिफिकेशन दोन प्राथमिक ट्रान्सपोर्ट मेकॅनिझम्स परिभाषित करते:
> 1. **stdio** - स्टँडर्ड इनपुट/आउटपुट (स्थानिक सर्व्हरसाठी शिफारस)
> 2. **Streamable HTTP** - रिमोट सर्व्हरसाठी जे इंटरनली SSE वापरू शकतात
>
> हा धडा अद्यतनित करून **stdio ट्रान्सपोर्ट** वर लक्ष केंद्रित करण्यात आला आहे, ज्याला बहुतेक MCP सर्व्हर अंमलबजावणींसाठी शिफारस केली जाते.

stdio ट्रान्सपोर्ट MCP सर्व्हर्सना क्लायंटशी स्टँडर्ड इनपुट आणि आउटपुट स्ट्रीमद्वारे संवाद साधण्याची परवानगी देतो. हे सध्याच्या MCP स्पेसिफिकेशनमध्ये सर्वाधिक वापरले जाणारे व शिफारस केलेले ट्रान्सपोर्ट मेकॅनिझम आहे, जे विविध क्लायंट ऍप्लिकेशन्ससह सहज जोडता येण्याजोगे MCP सर्व्हर्स तयार करण्याचा साधा आणि प्रभावी मार्ग प्रदान करतो.

## आढावा

हा धडा stdio ट्रान्सपोर्ट वापरून MCP सर्व्हर्स कसे तयार करायचे आणि वापरायचे यावर प्रकाश टाकतो.

## शिकण्याचे उद्दिष्ट

या धड्याच्या शेवटी आपण सक्षम असाल:

- stdio ट्रान्सपोर्ट वापरून MCP सर्व्हर तयार करणे.
- Inspector वापरून MCP सर्व्हर डिबग करणे.
- Visual Studio Code वापरून MCP सर्व्हर वापरणे.
- वर्तमान MCP ट्रान्सपोर्ट मेकॅनिझम्स समजून घेणे आणि का stdio शिफारस केले जाते ते जाणून घेणे.

## stdio ट्रान्सपोर्ट - ते कसे कार्य करते

stdio ट्रान्सपोर्ट ही वर्तमान MCP स्पेसिफिकेशन (2025-06-18) मधील दोन समर्थित ट्रान्सपोर्ट प्रकारांपैकी एक आहे. हे कसे कार्य करते ते येथे दिले आहे:

- **सोपे संवाद**: सर्व्हर स्टँडर्ड इनपुट (`stdin`) वरून JSON-RPC संदेश वाचतो आणि स्टँडर्ड आउटपुट (`stdout`) वर संदेश पाठवतो.
- **प्रक्रिया आधारित**: क्लायंट MCP सर्व्हर एक subprocess म्हणून सुरू करतो.
- **संदेश स्वरूप**: संदेश वैयक्तिक JSON-RPC विनंत्या, नोटिफिकेशन्स किंवा प्रतिसाद असतात, नवीन ओळीने विभक्त केलेले.
- **लॉगिंग**: सर्व्हर संभाव्यतेने लॉगिंगसाठी स्टँडर्ड त्रुटी (`stderr`) वर UTF-8 स्ट्रिंग लिहू शकतो.

### मुख्य आवश्यकता:
- संदेश नवीन ओळीने विभक्त केलेले असले पाहिजेत आणि समांतर नवीन ओळींसह नसले पाहिजेत.
- सर्व्हर `stdout` वर वैध MCP संदेश नसलेली कोणतीही माहिती लिहू नये.
- क्लायंट सर्व्हरच्या `stdin` वर वैध MCP संदेश नसलेली कोणतीही माहिती लिहू नये.

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

वरील कोडमध्ये:

- आम्ही MCP SDK मधून `Server` क्लास आणि `StdioServerTransport` आयात करतो
- एक सर्व्हर उदाहरण मूलभूत कॉन्फिगरेशन आणि क्षमतांसह तयार करतो
- `StdioServerTransport` चे उदाहरण तयार करून सर्व्हर त्याला जोडतो, ज्यामुळे stdin/stdout वरून संप्रेषण सक्षम होते

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# सर्व्हर उदाहरण तयार करा
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

वरील कोडमध्ये आम्ही:

- MCP SDK वापरून एक सर्व्हर उदाहरण तयार करतो
- डेकोरेटर वापरून टूल्स परिभाषित करतो
- stdio_server संदर्भ व्यवस्थापक वापरून ट्रान्सपोर्ट हाताळतो

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

SSE पासून मुख्य फरक म्हणजे stdio सर्व्हर्स:

- वेब सर्व्हर सेटअप किंवा HTTP एंडपॉइंट्सची गरज नाही
- क्लायंट सबप्रोसेस म्हणून सुरू करतो
- stdin/stdout स्ट्रीमसद्वारे संवाद करतात
- आणखी सोपे अंमलात आणणे आणि डिबग करणे

## व्यायाम: stdio सर्व्हर तयार करणे

आमचा सर्व्हर तयार करण्यासाठी दोन गोष्टी लक्षात ठेवणे आवश्यक आहेत:

- कनेक्शन आणि संदेशांसाठी एंडपॉइंट्स प्रदर्शित करण्यासाठी वेब सर्व्हर वापरणे आवश्यक आहे.

## प्रयोगशाळा: एक सोपा MCP stdio सर्व्हर तयार करणे

या प्रयोगशाळेत, आपण शिफारस केलेल्या stdio ट्रान्सपोर्टचा वापर करून एक सोपा MCP सर्व्हर तयार करू. हा सर्व्हर टूल्स प्रदर्शित करेल जे क्लायंट्स स्टँडर्ड Model Context Protocol वापरून कॉल करू शकतात.

### पूर्व-आवश्यकता

- Python 3.8 किंवा नंतरचा
- MCP Python SDK: `pip install mcp`
- async प्रोग्रामिंगची मूलभूत समज

आता आपला पहिला MCP stdio सर्व्हर तयार करूया:

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

## डिप्रिकेट केलेल्या SSE दृष्टिकोनापासून मुख्य फरक

**Stdio ट्रान्सपोर्ट (सध्याचा मानक):**
- सोपा सबप्रोसेस मॉडेल - क्लायंट सर्व्हर चाइल्ड प्रोसेस म्हणून सुरू करतो
- JSON-RPC संदेशांसाठी stdin/stdout वापरून संवाद
- HTTP सर्व्हर सेटअपची गरज नाही
- चांगली कार्यक्षमता आणि सुरक्षा
- सोपे डिबगिंग आणि विकास

**SSE ट्रान्सपोर्ट (MCP 2025-06-18 पासून डिप्रिकेटेड):**
- SSE एंडपॉइंट्ससह HTTP सर्व्हर आवश्यक
- वेब सर्व्हर इन्फ्रास्ट्रक्चरसह अधिक क्लिष्ट सेटअप
- HTTP एंडपॉइंट्ससाठी अतिरिक्त सुरक्षा विचार
- वेब-आधारित परिस्थितींसाठी आता Streamable HTTP ने बदलले आहे

### stdio ट्रान्सपोर्टसह सर्व्हर तयार करणे

आमचा stdio सर्व्हर तयार करण्यासाठी आम्हाला:

1. **आवश्यक लायब्ररी्स आयात करा** - MCP सर्व्हर घटक आणि stdio ट्रान्सपोर्टची आवश्यकता आहे
2. **एक सर्व्हर उदाहरण तयार करा** - सर्व्हर त्याच्या क्षमता परिभाषित करा
3. **टूल्स परिभाषित करा** - आपण ज्या कार्यांची पूर्तता करू इच्छिता ती जोडा
4. **ट्रान्सपोर्ट सेट करा** - stdio संप्रेषण कॉन्फिगर करा
5. **सर्व्हर चालवा** - सर्व्हर सुरू करा आणि संदेश हाताळा

चला हे टप्प्याटप्प्याने तयार करूया:

### टप्पा 1: मूलभूत stdio सर्व्हर तयार करा

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

### टप्पा 3: सर्व्हर चालवा

कोड `server.py` म्हणून जतन करा आणि कमांड लाइनवरून चालवा:

```bash
python server.py
```

सर्व्हर सुरू होईल आणि stdin कडून इनपुटची प्रतीक्षा करेल. तो stdio ट्रान्सपोर्टद्वारे JSON-RPC संदेशांचा वापर करून संवाद साधतो.

### टप्पा 4: Inspector सह चाचणी

आपण MCP Inspector वापरून आपला सर्व्हर चाचणी करू शकता:

1. Inspector इन्स्टॉल करा: `npx @modelcontextprotocol/inspector`
2. Inspector चालवा आणि आपला सर्व्हर त्याकडे निर्देशित करा
3. तयार केलेले टूल्स चाचणी करा

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## आपला stdio सर्व्हर डिबग करणे

### MCP Inspector वापरणे

MCP Inspector हे MCP सर्व्हर्सचे डिबगिंग आणि चाचणी करण्याचे उपयुक्त उपकरण आहे. आपला stdio सर्व्हर वापरून ते कसे वापरायचे:

1. **Inspector इन्स्टॉल करा**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector चालवा**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **आपला सर्व्हर चाचणी करा**: Inspector एक वेब इंटरफेस प्रदान करतो जिथे आपण:
   - सर्व्हर क्षमतांचा आढावा घेऊ शकता
   - विभिन्न पॅरामीटर्ससह टूल्स चाचणी करू शकता
   - JSON-RPC संदेश निरीक्षण करू शकता
   - कनेक्शन संबंधी समस्या डिबग करू शकता

### VS Code वापरणे

आपण आपल्या MCP सर्व्हरला थेट VS Code मध्ये देखील डिबग करू शकता:

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

2. सर्व्हर कोडमध्ये ब्रेकपॉइंट्स सेट करा
3. डिबगर चालवा आणि Inspector सह चाचणी करा

### सामान्य डिबगिंग टिप्स

- लॉगिंगसाठी `stderr` वापरा - `stdout` कधीही वापरू नका कारण ते MCP संदेशांसाठी राखीव आहे
- सर्व JSON-RPC संदेश नवीन ओळीने विभक्त असावेत याची खात्री करा
- प्रथम सोपे टूल्स वापरून चाचणी करा आणि मग गुंतागुंतीची कार्यक्षमता जोडा
- संदेश स्वरूप तपासण्यासाठी Inspector वापरा

## VS Code मध्ये आपला stdio सर्व्हर वापरणे

एकदा आपण आपला MCP stdio सर्व्हर तयार केल्यानंतर, आपण तो VS Code सोबत क्लॉड किंवा अन्य MCP-सुसंगत क्लायंट्ससाठी इंटीग्रेट करू शकता.

### कॉन्फिगरेशन

1. Windows मध्ये `%APPDATA%\Claude\claude_desktop_config.json` किंवा Mac मध्ये `~/Library/Application Support/Claude/claude_desktop_config.json` येथे MCP कॉन्फिगरेशन फाईल तयार करा:

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

2. **Claude पुन्हा सुरू करा**: नवीन सर्व्हर कॉन्फिगरेशन लोड करण्यासाठी Claude बंद करून पुन्हा उघडा.

3. **कनेक्शन चाचणी करा**: Claude सोबत संभाषण सुरू करा आणि आपल्या सर्व्हरच्या टूल्स वापरून पाहा:
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### TypeScript stdio सर्व्हर उदाहरण

दुवा संदर्भासाठी येथे संपूर्ण TypeScript उदाहरण आहे:

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

या अद्यतनित धड्यात, आपण शिकलात:

- वर्तमान **stdio ट्रान्सपोर्ट** (शिफारस केलेला मार्ग) वापरून MCP सर्व्हर तयार करणे
- का SSE ट्रान्सपोर्ट डिप्रिकेट केले गेले आणि stdio व Streamable HTTP कडे वळले याचे कारण समजून घेणे
- MCP क्लायंट्सद्वारे कॉल करण्यासाठी टूल्स तयार करणे
- MCP Inspector वापरून सर्व्हर डिबग करणे
- VS Code आणि Claude सह आपला stdio सर्व्हर एकत्रित करणे

stdio ट्रान्सपोर्ट डिप्रिकेट झालेल्या SSE च्या तुलनेत MCP सर्व्हर तयार करण्याचा अधिक सोपा, सुरक्षित आणि कार्यक्षम मार्ग प्रदान करतो. 2025-06-18 च्या स्पेसिफिकेशननुसार हे बहुतेक MCP सर्व्हर अंमलबजावणींसाठी शिफारस केलेले ट्रान्सपोर्ट आहे.

### .NET

1. आम्ही आधी काही टूल्स तयार करूया, यासाठी *Tools.cs* नावाची फाईल तयार करू ज्यात खालील सामग्री असेल:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## व्यायाम: आपला stdio सर्व्हर चाचणी करणे

आपण आपला stdio सर्व्हर तयार केल्यानंतर, तो योग्य प्रकारे कार्य करतो का हे तपासूया.

### पूर्व-आवश्यकता

1. MCP Inspector इंस्टॉल असल्याची खात्री करा:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. आपला सर्व्हर कोड जतन केला आहे (उदा. `server.py`)

### Inspector सह चाचणी

1. **आपल्या सर्व्हरसह Inspector सुरू करा**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **वेब इंटरफेस उघडा**: Inspector आपला सर्व्हरच्या क्षमता दर्शविणारी ब्राउझर विंडो उघडेल.

3. **टूल्स चाचणी करा**:
   - `get_greeting` टूल विविध नावांसह वापरून पहा
   - `calculate_sum` टूल विविध संख्या वापरून चाचणी करा
   - `get_server_info` टूल कॉल करून सर्व्हर मेटाडेटा पहा

4. **संवाद निरीक्षण करा**: Inspector क्लायंट आणि सर्व्हरमधील JSON-RPC संदेश दर्शवितो.

### आपल्याला काय दिसेल

आपला सर्व्हर योग्यरित्या सुरू झाल्यावर, आपल्याला असे दिसेल:
- Inspector मध्ये सर्व्हर क्षमता सूचीबद्ध
- चाचणीसाठी टूल्स उपलब्ध
- यशस्वी JSON-RPC संदेश देवाणघेवाण
- टूल प्रतिसाद इंटरफेसमध्ये प्रदर्शित

### सामान्य समस्या आणि उपाय

**सर्व्हर सुरू होत नाही:**
- सर्व अवलंबने इन्स्टॉल आहेत का तपासा: `pip install mcp`
- Python सिंटॅक्स आणि इंडेंटेशन तपासा
- कन्सोलमधील त्रुटी संदेश पहा

**टूल्स दिसत नाहीत:**
- `@server.tool()` डेकोरेटर्सची उपस्थिती तपासा
- `main()` आधी टूल फंक्शन्स परिभाषित करा
- सर्व्हर योग्य रीतीने कॉन्फिगर केला आहे का याची खात्री करा

**कनेक्शन समस्या:**
- सर्व्हर stdio ट्रान्सपोर्टचा योग्य वापर करत आहे का ते तपासा
- इतर प्रक्रिया अडथळा करत नाहीयेत ना ते पहा
- Inspector कमांड सिंटॅक्स योग्य आहे का तपासा

## असाइनमेंट

आपल्या सर्व्हरमध्ये अधिक क्षमता विकास करण्याचा प्रयत्न करा. यासाठी [ही पृष्ठं](https://api.chucknorris.io/) पहा जिथे आपण एखादा टूल API कॉल करतो असा तयार करू शकता. आपण ठरवा सर्व्हर कसा दिसायला हवा. मजा करा :)

## सोल्यूशन

[सोल्यूशन](./solution/README.md) येथे कार्यरत कोडसह शक्यतोचे समाधान दिले आहे.

## मुख्य मुद्दे

या अध्यायातील मुख्य मुद्दे खालीलप्रमाणे आहेत:

- stdio ट्रान्सपोर्ट स्थानिक MCP सर्व्हरसाठी शिफारस केलेला मेकॅनिझम आहे.
- stdio ट्रान्सपोर्ट स्टँडर्ड इनपुट आणि आउटपुट स्ट्रीम वापरून MCP सर्व्हर आणि क्लायंट दरम्यान अखंड संवाद सक्षम करतो.
- आपण Inspector आणि Visual Studio Code दोन्ही वापरून stdio सर्व्हर्स थेट वापरू शकता, ज्यामुळे डिबगिंग आणि इंटीग्रेशन सुलभ होते.

## नमुने

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## अतिरिक्त स्त्रोत

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## पुढे काय

## पुढील पावले

आता आपण stdio ट्रान्सपोर्ट सह MCP सर्व्हर तयार करायला शिकलात, आपण अधिक प्रगत विषयांचा शोध घेऊ शकता:

- **पुढील:** [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - दूरस्थ सर्व्हरसाठी दुसरा समर्थित ट्रान्सपोर्ट मेकॅनिझम जाणून घ्या
- **प्रगत:** [MCP Security Best Practices](../../02-Security/README.md) - आपले MCP सर्व्हरमध्ये सुरक्षा अंमलात आणा
- **उत्पादनासाठी:** [Deployment Strategies](../09-deployment/README.md) - उत्पादन वापरासाठी आपले सर्व्हर तैनात करा

## अतिरिक्त स्त्रोत

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - अधिकृत स्पेसिफिकेशन
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - सर्व भाषा साठी SDK संदर्भ
- [Community Examples](../../06-CommunityContributions/README.md) - समुदायाकडून अधिक सर्व्हर उदाहरणे

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**स्पष्टीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अपूर्णता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत सर्वाधिक अधिकारिणी स्त्रोत म्हणून मानला पाहिजे. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाचा वापर करून झालेल्या कोणत्याही गैरसमजुती किंवा गैरव्याख्यांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->