# MCP सर्व्हर stdio ट्रान्सपोर्टसह

> **⚠️ महत्त्वाचे अपडेट**: MCP स्पेसिफिकेशन 2025-06-18 नुसार, स्वतंत्र SSE (Server-Sent Events) ट्रान्सपोर्ट **निष्क्रिय** करण्यात आले आहे आणि त्याऐवजी "Streamable HTTP" ट्रान्सपोर्टचा वापर करण्यात येतो. सध्याच्या MCP स्पेसिफिकेशनमध्ये दोन मुख्य ट्रान्सपोर्ट यंत्रणा परिभाषित केल्या आहेत:
> 1. **stdio** - स्थानिक सर्व्हरसाठी शिफारस केलेले (स्टँडर्ड इनपुट/आउटपुट)
> 2. **Streamable HTTP** - दूरस्थ सर्व्हरसाठी जे अंतर्गत SSE वापरू शकतात
>
> या धड्याचा फोकस **stdio ट्रान्सपोर्ट**वर आहे, जो बहुतेक MCP सर्व्हर अंमलबजावणीसाठी शिफारस केलेला दृष्टिकोन आहे.

stdio ट्रान्सपोर्ट MCP सर्व्हरना क्लायंटसोबत स्टँडर्ड इनपुट आणि आउटपुट स्ट्रीमद्वारे संवाद साधण्याची परवानगी देते. सध्याच्या MCP स्पेसिफिकेशनमध्ये हा सर्वात सामान्यतः वापरला जाणारा आणि शिफारस केलेला ट्रान्सपोर्ट यंत्रणा आहे, जो MCP सर्व्हर तयार करण्याचा सोपा आणि कार्यक्षम मार्ग प्रदान करतो, जो विविध क्लायंट अनुप्रयोगांसह सहजपणे समाकलित केला जाऊ शकतो.

## आढावा

या धड्यात stdio ट्रान्सपोर्ट वापरून MCP सर्व्हर तयार करणे आणि वापरणे यावर चर्चा केली आहे.

## शिकण्याची उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही खालील गोष्टी करू शकाल:

- stdio ट्रान्सपोर्ट वापरून MCP सर्व्हर तयार करा.
- MCP सर्व्हरचे निरीक्षण करून डिबग करा.
- Visual Studio Code वापरून MCP सर्व्हर वापरा.
- सध्याच्या MCP ट्रान्सपोर्ट यंत्रणांची समज आणि stdio का शिफारस केली जाते हे समजून घ्या.

## stdio ट्रान्सपोर्ट - कसे कार्य करते

stdio ट्रान्सपोर्ट सध्याच्या MCP स्पेसिफिकेशन (2025-06-18) मध्ये समर्थित दोन ट्रान्सपोर्ट प्रकारांपैकी एक आहे. हे कसे कार्य करते:

- **सोपे संवाद**: सर्व्हर स्टँडर्ड इनपुट (`stdin`) वरून JSON-RPC संदेश वाचतो आणि स्टँडर्ड आउटपुट (`stdout`) वर संदेश पाठवतो.
- **प्रक्रिया-आधारित**: क्लायंट MCP सर्व्हरला उपप्रक्रिया म्हणून सुरू करते.
- **संदेश स्वरूप**: संदेश हे स्वतंत्र JSON-RPC विनंत्या, सूचना किंवा प्रतिसाद असतात, जे नवीन ओळींनी विभाजित केले जातात.
- **लॉगिंग**: सर्व्हर UTF-8 स्ट्रिंग्स स्टँडर्ड एरर (`stderr`) वर लॉगिंगसाठी लिहू शकतो.

### मुख्य आवश्यकता:
- संदेश नवीन ओळींनी विभाजित केले गेले पाहिजेत आणि त्यात अंतर्गत नवीन ओळी असू नयेत.
- सर्व्हरने `stdout` वर MCP संदेश नसलेले काहीही लिहू नये.
- क्लायंटने सर्व्हरच्या `stdin` वर MCP संदेश नसलेले काहीही लिहू नये.

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
```

वरील कोडमध्ये:

- आम्ही MCP SDK मधून `Server` वर्ग आणि `StdioServerTransport` आयात करतो.
- आम्ही मूलभूत कॉन्फिगरेशन आणि क्षमता असलेला सर्व्हर तयार करतो.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

वरील कोडमध्ये:

- आम्ही MCP SDK वापरून सर्व्हर तयार करतो.
- डेकोरेटर्स वापरून टूल्स परिभाषित करतो.
- stdio_server संदर्भ व्यवस्थापक वापरून ट्रान्सपोर्ट हाताळतो.

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;

var builder = Host.CreateApplicationBuilder(args);

builder.Services
    .AddMcpServer()
    .WithStdioTransport()
    .WithTools<Tools>();

builder.Services.AddLogging(logging => logging.AddConsole());

var app = builder.Build();
await app.RunAsync();
```

SSE पासून मुख्य फरक म्हणजे stdio सर्व्हर:

- वेब सर्व्हर सेटअप किंवा HTTP एंडपॉइंट्सची आवश्यकता नाही.
- क्लायंटद्वारे उपप्रक्रिया म्हणून सुरू केले जातात.
- stdin/stdout स्ट्रीमद्वारे संवाद साधतात.
- अंमलबजावणी आणि डिबग करणे सोपे आहे.

## व्यायाम: stdio सर्व्हर तयार करणे

आपला सर्व्हर तयार करण्यासाठी, आपल्याला दोन गोष्टी लक्षात ठेवाव्या लागतील:

- आम्हाला कनेक्शन आणि संदेशांसाठी एंडपॉइंट्स उघडण्यासाठी वेब सर्व्हर वापरावा लागेल.

## प्रयोगशाळा: साधा MCP stdio सर्व्हर तयार करणे

या प्रयोगशाळेत, आम्ही stdio ट्रान्सपोर्ट वापरून एक साधा MCP सर्व्हर तयार करू. हा सर्व्हर टूल्स उघडेल ज्यांना क्लायंट स्टँडर्ड मॉडेल कॉन्टेक्स्ट प्रोटोकॉल वापरून कॉल करू शकतात.

### पूर्वतयारी

- Python 3.8 किंवा त्याहून अधिक
- MCP Python SDK: `pip install mcp`
- async प्रोग्रामिंगची मूलभूत समज

चला आपला पहिला MCP stdio सर्व्हर तयार करूया:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## SSE दृष्टिकोनापासून मुख्य फरक

**Stdio ट्रान्सपोर्ट (सध्याचा मानक):**
- सोपा उपप्रक्रिया मॉडेल - क्लायंट सर्व्हरला चाइल्ड प्रोसेस म्हणून सुरू करतो.
- JSON-RPC संदेश वापरून stdin/stdout द्वारे संवाद.
- HTTP सर्व्हर सेटअप आवश्यक नाही.
- चांगली कार्यक्षमता आणि सुरक्षा.
- डिबगिंग आणि विकास सोपे.

**SSE ट्रान्सपोर्ट (MCP 2025-06-18 पासून निष्क्रिय):**
- HTTP सर्व्हरसह SSE एंडपॉइंट्स आवश्यक होते.
- वेब सर्व्हर पायाभूत सुविधांसह अधिक जटिल सेटअप.
- HTTP एंडपॉइंट्ससाठी अतिरिक्त सुरक्षा विचार.
- वेब-आधारित परिस्थितीसाठी Streamable HTTP ने बदलले.

### stdio ट्रान्सपोर्टसह सर्व्हर तयार करणे

stdio सर्व्हर तयार करण्यासाठी, आपल्याला हे करणे आवश्यक आहे:

1. **आवश्यक लायब्ररी आयात करा** - MCP सर्व्हर घटक आणि stdio ट्रान्सपोर्ट आवश्यक आहे.
2. **सर्व्हर उदाहरण तयार करा** - सर्व्हर त्याच्या क्षमतांसह परिभाषित करा.
3. **टूल्स परिभाषित करा** - आपण उघडू इच्छित कार्यक्षमता जोडा.
4. **ट्रान्सपोर्ट सेट करा** - stdio संवाद कॉन्फिगर करा.
5. **सर्व्हर चालवा** - सर्व्हर सुरू करा आणि संदेश हाताळा.

चला हे टप्प्याटप्प्याने तयार करूया:

### टप्पा 1: साधा stdio सर्व्हर तयार करा

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

### टप्पा 3: सर्व्हर चालवणे

कोड `server.py` म्हणून सेव्ह करा आणि कमांड लाइनवरून चालवा:

```bash
python server.py
```

सर्व्हर सुरू होईल आणि stdin वरून इनपुटची वाट पाहील. तो stdio ट्रान्सपोर्टवर JSON-RPC संदेश वापरून संवाद साधतो.

### टप्पा 4: निरीक्षकासह चाचणी करणे

आपण MCP निरीक्षक वापरून आपला सर्व्हर चाचणी करू शकता:

1. निरीक्षक स्थापित करा: `npx @modelcontextprotocol/inspector`
2. निरीक्षक चालवा आणि आपल्या सर्व्हरकडे निर्देश करा.
3. आपण तयार केलेल्या टूल्सची चाचणी करा.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## आपल्या stdio सर्व्हरचे डिबगिंग

### MCP निरीक्षक वापरणे

MCP निरीक्षक MCP सर्व्हरचे डिबगिंग आणि चाचणीसाठी एक मौल्यवान साधन आहे. आपल्या stdio सर्व्हरसह ते कसे वापरायचे:

1. **निरीक्षक स्थापित करा**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **निरीक्षक चालवा**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **आपला सर्व्हर चाचणी करा**: निरीक्षक वेब इंटरफेस प्रदान करतो जिथे आपण:
   - सर्व्हर क्षमता पाहू शकता.
   - विविध पॅरामीटर्ससह टूल्स चाचणी करू शकता.
   - JSON-RPC संदेशांचे निरीक्षण करू शकता.
   - कनेक्शन समस्यांचे डिबग करू शकता.

### VS Code वापरणे

आपण आपला MCP सर्व्हर थेट VS Code मध्ये डिबग करू शकता:

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

2. आपल्या सर्व्हर कोडमध्ये ब्रेकपॉइंट्स सेट करा.
3. डिबगर चालवा आणि निरीक्षकासह चाचणी करा.

### सामान्य डिबगिंग टिप्स

- लॉगिंगसाठी `stderr` वापरा - MCP संदेशांसाठी `stdout` राखीव आहे.
- सर्व JSON-RPC संदेश नवीन ओळींनी विभाजित असल्याची खात्री करा.
- जटिल कार्यक्षमता जोडण्यापूर्वी सोप्या टूल्ससह चाचणी करा.
- संदेश स्वरूप सत्यापित करण्यासाठी निरीक्षक वापरा.

## VS Code मध्ये आपला stdio सर्व्हर वापरणे

आपण आपला MCP stdio सर्व्हर तयार केल्यानंतर, आपण Claude किंवा इतर MCP-सुसंगत क्लायंटसह वापरण्यासाठी तो VS Code मध्ये समाकलित करू शकता.

### कॉन्फिगरेशन

1. **MCP कॉन्फिगरेशन फाइल तयार करा** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) किंवा `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Claude पुन्हा सुरू करा**: नवीन सर्व्हर कॉन्फिगरेशन लोड करण्यासाठी Claude बंद करा आणि पुन्हा उघडा.

3. **कनेक्शन चाचणी करा**: Claude सोबत संभाषण सुरू करा आणि आपल्या सर्व्हरच्या टूल्स वापरण्याचा प्रयत्न करा:
   - "ग्रीटिंग टूल वापरून मला अभिवादन करू शकता का?"
   - "15 आणि 27 ची बेरीज काढा."
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

// Add tools
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
    .WithStdioTransport()
    .WithTools<Tools>();

var app = builder.Build();
await app.RunAsync();

public class Tools
{
    [Description("Get a personalized greeting")]
    public string GetGreeting(string name)
    {
        return $"Hello, {name}! Welcome to MCP stdio server.";
    }

    [Description("Calculate the sum of two numbers")]
    public int CalculateSum(int a, int b)
    {
        return a + b;
    }
}
```

## सारांश

या अद्यतनित धड्यात, आपण शिकले:

- सध्याच्या **stdio ट्रान्सपोर्ट** (शिफारस केलेला दृष्टिकोन) वापरून MCP सर्व्हर तयार करणे.
- SSE ट्रान्सपोर्ट stdio आणि Streamable HTTP च्या फायद्यासाठी का निष्क्रिय केले गेले हे समजून घेणे.
- MCP क्लायंटद्वारे कॉल करता येणारी टूल्स तयार करणे.
- MCP निरीक्षक वापरून आपला सर्व्हर डिबग करणे.
- आपला stdio सर्व्हर VS Code आणि Claude सह समाकलित करणे.

stdio ट्रान्सपोर्ट निष्क्रिय SSE दृष्टिकोनाच्या तुलनेत MCP सर्व्हर तयार करण्याचा सोपा, अधिक सुरक्षित आणि अधिक कार्यक्षम मार्ग प्रदान करते. 2025-06-18 स्पेसिफिकेशननुसार बहुतेक MCP सर्व्हर अंमलबजावणीसाठी हा शिफारस केलेला ट्रान्सपोर्ट आहे.

### .NET

1. प्रथम काही टूल्स तयार करूया, यासाठी आम्ही *Tools.cs* नावाची फाइल तयार करू:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## व्यायाम: आपला stdio सर्व्हर चाचणी करणे

आता आपण आपला stdio सर्व्हर तयार केला आहे, चला त्याची चाचणी करूया.

### पूर्वतयारी

1. MCP निरीक्षक स्थापित असल्याची खात्री करा:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. आपला सर्व्हर कोड सेव्ह केला पाहिजे (उदा., `server.py` म्हणून).

### निरीक्षकासह चाचणी करणे

1. **आपल्या सर्व्हरसह निरीक्षक सुरू करा**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **वेब इंटरफेस उघडा**: निरीक्षक ब्राउझर विंडो उघडेल ज्यामध्ये आपला सर्व्हर क्षमता दर्शवेल.

3. **टूल्स चाचणी करा**:
   - `get_greeting` टूल विविध नावांसह वापरून पहा.
   - `calculate_sum` टूल विविध संख्यांसह चाचणी करा.
   - `get_server_info` टूल कॉल करून सर्व्हर मेटाडेटा पहा.

4. **संवादाचे निरीक्षण करा**: निरीक्षक क्लायंट आणि सर्व्हर दरम्यान विनिमय होणारे JSON-RPC संदेश दर्शवतो.

### तुम्हाला काय दिसले पाहिजे

आपला सर्व्हर योग्यरित्या सुरू झाल्यावर, आपल्याला दिसेल:
- निरीक्षकामध्ये सर्व्हर क्षमता सूचीबद्ध.
- चाचणीसाठी उपलब्ध टूल्स.
- यशस्वी JSON-RPC संदेश विनिमय.
- इंटरफेसमध्ये टूल प्रतिसाद प्रदर्शित.

### सामान्य समस्या आणि उपाय

**सर्व्हर सुरू होत नाही:**
- सर्व अवलंबित्व स्थापित आहेत याची खात्री करा: `pip install mcp`
- Python सिंटॅक्स आणि इंडेंटेशन सत्यापित करा.
- कन्सोलमध्ये त्रुटी संदेश शोधा.

**टूल्स दिसत नाहीत:**
- `@server.tool()` डेकोरेटर्स उपस्थित आहेत याची खात्री करा.
- टूल फंक्शन्स `main()` च्या आधी परिभाषित आहेत याची खात्री करा.
- सर्व्हर योग्यरित्या कॉन्फिगर आहे याची खात्री करा.

**कनेक्शन समस्या:**
- सर्व्हर stdio ट्रान्सपोर्ट योग्यरित्या वापरत आहे याची खात्री करा.
- इतर प्रक्रिया हस्तक्षेप करत नाहीत याची खात्री करा.
- निरीक्षक कमांड सिंटॅक्स सत्यापित करा.

## असाइनमेंट

आपल्या सर्व्हरमध्ये अधिक क्षमता जोडण्याचा प्रयत्न करा. [या पृष्ठावर](https://api.chucknorris.io/) पहा, उदाहरणार्थ, API कॉल करणारे टूल जोडा. सर्व्हर कसा दिसावा हे तुम्ही ठरवा. मजा करा :)

## समाधान

[समाधान](./solution/README.md) येथे कार्यरत कोडसह संभाव्य समाधान आहे.

## मुख्य मुद्दे

या अध्यायातील मुख्य मुद्दे खालीलप्रमाणे आहेत:

- stdio ट्रान्सपोर्ट स्थानिक MCP सर्व्हरसाठी शिफारस केलेली यंत्रणा आहे.
- stdio ट्रान्सपोर्ट MCP सर्व्हर आणि क्लायंट दरम्यान स्टँडर्ड इनपुट आणि आउटपुट स्ट्रीम वापरून सहज संवाद साधण्याची परवानगी देते.
- निरीक्षक आणि Visual Studio Code वापरून stdio सर्व्हर थेट वापरता येतो, ज्यामुळे डिबगिंग आणि समाकलन सोपे होते.

## नमुने

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## अतिरिक्त संसाधने

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## पुढे काय

## पुढील पावले

आता आपण stdio ट्रान्सपोर्टसह MCP सर्व्हर तयार करणे शिकले आहे, आपण अधिक प्रगत विषय एक्सप्लोर करू शकता:

- **पुढे**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - दूरस्थ सर्व्हरसाठी समर्थित दुसऱ्या ट्रान्सपोर्ट यंत्रणेबद्दल जाणून घ्या.
- **प्रगत**: [MCP Security Best Practices](../../02-Security/README.md) - आपल्या MCP सर्व्हरमध्ये सुरक्षा अंमलात आणा.
- **उत्पादन**: [Deployment Strategies](../09-deployment/README.md) - उत्पादनासाठी आपल्या सर्व्हरचे वितरण करा.

## अतिरिक्त संसाधने

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - अधिकृत स्पेसिफिकेशन.
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - सर्व भाषांसाठी SDK संदर्भ.
- [Community Examples](../../06-CommunityContributions/README.md) - समुदायाकडून अधिक सर्व्हर उदाहरणे.

---

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.