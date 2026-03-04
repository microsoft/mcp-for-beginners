# stdio ट्रान्सपोर्टसह MCP सर्व्हर

> **⚠️ महत्त्वाचा अपडेट**: MCP Specification 2025-06-18 नुसार, स्वतंत्र SSE (Server-Sent Events) ट्रान्सपोर्ट **डिप्रिकेटेड** केला गेला आहे आणि त्याऐवजी "Streamable HTTP" ट्रान्सपोर्ट वापरला जातो. चालू MCP स्पेसिफिकेशन दोन प्रमुख ट्रान्सपोर्ट यंत्रणा परिभाषित करते:
> 1. **stdio** - स्टँडर्ड इनपुट/आउटपुट (स्थानिक सर्व्हरसाठी शिफारस केलेले)
> 2. **Streamable HTTP** - रिमोट सर्व्हरसाठी जे अंतर्गत SSE वापरू शकतात
>
> हा धडा stdio ट्रान्सपोर्टवर लक्ष केंद्रित करण्यासाठी अपडेट केला आहे, जो बहुसंख्य MCP सर्व्हर इम्प्लिमेंटेशन्ससाठी शिफारसीय आहे.

stdio ट्रान्सपोर्ट MCP सर्व्हर्सना क्लायंट्सशी स्टँडर्ड इनपुट आणि आउटपुट स्ट्रीम्सद्वारे संवाद साधण्यास परवानगी देतो. हा सध्याच्या MCP स्पेसिफिकेशनमध्ये सर्वात सामान्य आणि शिफारस केलेला ट्रान्सपोर्ट यंत्रणा आहे, ज्यामुळे विविध क्लायंट अॅप्लिकेशन्ससह सहजपणे एकत्रित करता येणारे सोपे आणि कार्यक्षम MCP सर्व्हर तयार करता येतात.

## आढावा

हा धडा stdio ट्रान्सपोर्ट वापरून MCP सर्व्हर कसे तयार आणि वापरायचे हे स्पष्ट करतो.

## शिकण्याची उद्दिष्टे

या धड्याच्या शेवटी, तुम्ही खालील गोष्टी करू शकाल:

- stdio ट्रान्सपोर्ट वापरून MCP सर्व्हर तयार करणे.
- Inspector वापरून MCP सर्व्हर डिबग करणे.
- Visual Studio Code वापरून MCP सर्व्हर वापरणे.
- MCP च्या चालू ट्रान्सपोर्ट यंत्रणांचा समज प्राप्त करणे आणि stdio का शिफारस केला जातो हे समजून घेणे.

## stdio ट्रान्सपोर्ट - ते कसे कार्य करते

stdio ट्रान्सपोर्ट हा चालू MCP स्पेसिफिकेशन (2025-06-18) मध्ये समर्थित दोन ट्रान्सपोर्टपैकी एक आहे. ते असे कार्य करते:

- **साधा संवाद**: सर्व्हर JSON-RPC संदेश `stdin` वरून वाचतो आणि `stdout` वर संदेश पाठवतो.
- **प्रोसेस-आधारित**: क्लायंट MCP सर्व्हरला सबप्रोसेस म्हणून सुरू करतो.
- **संदेशाचा फॉर्मॅट**: संदेश स्वतंत्र JSON-RPC विनंत्या, सूचना किंवा प्रतिसाद असतात, ज्यांचे विभाजन नवीन ओळींनी केलेले असते.
- **लॉगिंग**: सर्व्हर `stderr` वर UTF-8 स्ट्रिंग लिहू शकतो लॉगिंगसाठी.

### मुख्य आवश्यकता:
- संदेश नवीन ओळींनी विभाजित केलेले असले पाहिजेत आणि संदेशात अंतर्निहित नवीन ओळी नसाव्यात
- सर्व्हरने `stdout` वर वैध MCP संदेशाशिवाय काहीही लिहिलेले असू नये
- क्लायंटने सर्व्हरच्या `stdin` वर वैध MCP संदेशाशिवाय काहीही लिहिलेले असू नये

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

- आम्ही MCP SDK मधून `Server` क्लास आणि `StdioServerTransport` आयात करतो
- मूलभूत कॉन्फिगरेशन आणि क्षमता वापरून सर्व्हरची उदाहरण तयार करतो

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

वरील कोडमध्ये:

- MCP SDK वापरून सर्व्हरची उदाहरण तयार करतो
- डेकोरेटर्स वापरून टूल्स परिभाषित करतो
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

SSE पेक्षा मुख्य फरक म्हणजे stdio सर्व्हर:

- वेब सर्व्हर सेटअप किंवा HTTP एंडपॉइंटची गरज नाही
- क्लायंटने त्यांना सबप्रोसेस म्हणून लॉन्च करतो
-stdin/stdout स्ट्रीमद्वारे संवाद साधतात
- अमलात आणणे आणि डिबग करणे सोपे आहे

## सराव: stdio सर्व्हर तयार करणे

सर्व्हर तयार करताना दोन गोष्टी लक्षात ठेवणे आवश्यक आहे:

- कनेक्शन आणि संदेशांसाठी एंडपॉइंट्स उघडण्यासाठी वेब सर्व्हरची गरज आहे.
## प्रयोगशाळा: एक सोपा MCP stdio सर्व्हर तयार करणे

या प्रयोगशाळेत, आपण शिफारसीय stdio ट्रान्सपोर्ट वापरून एक सोपा MCP सर्व्हर तयार करू. हा सर्व्हर टूल्स उघडेल जे क्लायंट्स Model Context Protocol वापरून कॉल करू शकतात.

### आवश्यक गोष्टी

- Python 3.8 किंवा नंतरचा
- MCP Python SDK: `pip install mcp`
- असिंक्रोनस प्रोग्रामिंगचा मूलभूत समज

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

**Stdio ट्रान्सपोर्ट (चालू मानक):**
- सोपी सबप्रोसेस मॉडेल - क्लायंट सर्व्हरला चाइल्ड प्रोसेस म्हणून लॉन्च करतो
- stdin/stdout वापरून JSON-RPC संदेशांद्वारे संवाद
- कोणतीही HTTP सर्व्हर सेटअपची गरज नाही
- चांगली कार्यक्षमता आणि सुरक्षा
- डिबगिंग आणि विकास सुलभ

**SSE ट्रान्सपोर्ट (MCP 2025-06-18 नुसार डिप्रिकेटेड):**
- SSE एंडपॉइंटसह HTTP सर्व्हरची आवश्यकता होती
- वेब सर्व्हर इन्फ्रास्ट्रक्चरसह अधिक कॉम्प्लेक्स सेटअप
- HTTP एंडपॉइंटसाठी अतिरिक्त सुरक्षा विचार
- वेब-आधारित परिस्थितीसाठी Streamable HTTP ने प्रतिस्थापित केला

### stdio ट्रान्सपोर्टसह सर्व्हर तयार करणे

stdio सर्व्हर तयार करण्यासाठी, आपल्याला:

1. **आवश्यक लायब्ररी आयात करा** - MCP सर्व्हर घटक आणि stdio ट्रान्सपोर्ट आवश्यक आहेत
2. **सर्व्हरची उदाहरण तयार करा** - सर्व्हर आणि त्याच्या क्षमतांचा निर्धार करा
3. **टूल्स परिभाषित करा** - आपण उघडू इच्छित कार्यक्षमता जोडा
4. **ट्रान्सपोर्ट सेटअप करा** - stdio कम्युनिकेशन कॉन्फिगर करा
5. **सर्व्हर चालू करा** - सर्व्हर सुरू करा आणि संदेश हाताळा

चला टप्प्याटप्प्याने तयार करूया:

### टप्पा 1: मूलभूत stdio सर्व्हर तयार करा

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# लॉगिंग सेट करा
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

कोड `server.py` म्हणून जतन करा आणि कमांड लाइनमधून चालवा:

```bash
python server.py
```

सर्व्हर सुरु होईल आणि stdin कडून इनपुटची वाट पाहेल. तो stdio ट्रान्सपोर्टवर JSON-RPC संदेशांचा वापर करून संवाद साधतो.

### टप्पा 4: Inspector वापरून चाचणी करा

आपण आपल्या सर्व्हरची चाचणी MCP Inspector वापरून करू शकता:

1. Inspector इन्स्टॉल करा: `npx @modelcontextprotocol/inspector`
2. Inspector चालवा आणि आपला सर्व्हर निवडा
3. आपण तयार केलेले टूल्स चाचणी करा

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## stdio सर्व्हर डिबगिंग

### MCP Inspector वापरणे

MCP Inspector हा MCP सर्व्हर्स डिबगिंग आणि चाचणीसाठी उपयुक्त साधन आहे. आपला stdio सर्व्हर वापरताना तो कसा वापरायचा हे येथे दिले आहे:

1. **Inspector इन्स्टॉल करा**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector चालवा**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **आपला सर्व्हर चाचणी करा**: Inspector वेब इंटरफेस प्रदान करतो जिथे आपण:
   - सर्व्हर क्षमता पाहू शकता
   - विविध पॅरामीटर्ससह टूल्सची चाचणी करू शकता
   - JSON-RPC संदेश निरीक्षण करू शकता
   - कनेक्शन समस्यांचा डिबग करू शकता

### VS Code वापरणे

VS Code मध्ये देखील आपण आपल्या MCP सर्व्हरला थेट डिबग करू शकता:

1. `.vscode/launch.json` मध्ये लॉन्च कन्फिगरेशन तयार करा:
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

- लॉगिंगसाठी `stderr` वापरा - `stdout` वर काहीही लिहू नका कारण तो MCP संदेशांसाठी राखीव आहे
- सर्व JSON-RPC संदेश नवीन ओळीने विभाजित केलेले असावेत याची खात्री करा
- जटिल फंक्शनॅलिटी जोडण्यापूर्वी साध्या टूल्ससह चाचणी करा
- संदेश फॉर्मॅटची खात्री करण्यासाठी Inspector वापरा

## VS Code मध्ये stdio सर्व्हर वापरणे

एकदा आपण MCP stdio सर्व्हर तयार केल्यानंतर, आपण तो VS Code सोबत एकत्रित करू शकता, ज्यामुळे तुम्ही Claude किंवा इतर MCP-सुसंगत क्लायंट्ससोबत वापरू शकता.

### कॉन्फिगरेशन

1. एक MCP कॉन्फिगरेशन फाइल तयार करा `%APPDATA%\Claude\claude_desktop_config.json` (Windows) किंवा `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. Claude पुनःप्रारंभ करा: नवीन सर्व्हर कॉन्फिगरेशन लोड करण्यासाठी Claude बंद करून पुन्हा उघडा.

3. कनेक्शनची चाचणी करा: Claude सोबत संभाषण सुरू करा आणि आपल्या सर्व्हरचे टूल्स वापरून पाहा:
   - "कृपया greeting tool वापरून मला अभिवादन करू शकता का?"
   - "15 आणि 27 चे बेरीज काढा"
   - "सर्व्हर माहिती काय आहे?"

### TypeScript stdio सर्व्हर उदाहरण

संदर्भासाठी पूर्ण TypeScript उदाहरण येथे आहे:

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

या अद्ययावत धड्यात, तुम्ही शिकले:

- चालू **stdio ट्रान्सपोर्ट** वापरून MCP सर्व्हर कसे तयार करायचे (शिफारसीय पद्धत)
- SSE ट्रान्सपोर्ट का डिप्रिकेटेड केला गेला आणि stdio व Streamable HTTP का वापरावे
- MCP क्लायंट्सद्वारे कॉल होणारे टूल्स कसे तयार करायचे
- MCP Inspector वापरून सर्व्हर कसे डिबग करायचे
- VS Code आणि Claude सोबत stdio सर्व्हर कसे इंटिग्रेट करायचे

stdio ट्रान्सपोर्ट डिप्रिकेटेड SSE पद्धतीच्या तुलनेत सोपी, अधिक सुरक्षित आणि अधिक कार्यक्षम आहे. 2025-06-18 स्पेसिफिकेशननुसार हा बहुसंख्य MCP सर्व्हर इम्प्लिमेंटेशन्ससाठी शिफारसीय ट्रान्सपोर्ट आहे.

### .NET

1. काही टूल्स प्रथम तयार करूया, यासाठी पुढील सामग्रीसह *Tools.cs* फाइल तयार करूया:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## सराव: आपला stdio सर्व्हर चाचणी करणे

आपण stdio सर्व्हर तयार केला आहे, आता त्याची योग्यरित्या कामगिरी होत असल्याची खात्री करण्यासाठी त्याची चाचणी करूया.

### आवश्यक गोष्टी

1. MCP Inspector इन्स्टॉल केले असल्याचे खात्री करा:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. आपला सर्व्हर कोड जतन केलेला असावा (उदा. `server.py`)

### Inspector वापरून चाचणी

1. **आपल्या सर्व्हरसह Inspector सुरू करा**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **वेब इंटरफेस उघडा**: Inspector ब्राउझर विंडो उघडेल जिथे आपल्या सर्व्हरच्या क्षमतांची माहिती दिसेल.

3. **टूल्स तपासा**:
   - `get_greeting` टूल विविध नावांसह वापरून पाहा
   - `calculate_sum` टूल विविध संख्यांसह चाचणी करा
   - `get_server_info` टूल कॉल करून सर्व्हर मेटाडेटा तपासा

4. **संवाद निरीक्षण करा**: Inspector क्लायंट आणि सर्व्हर यांच्यात होणारे JSON-RPC संदेश दर्शवतो.

### आपण काय पाहायला हवे

आपला सर्व्हर योग्यरित्या सुरू झाला असल्यास, आपल्याला खालील गोष्टी पाहायला मिळतील:
- Inspector मध्ये सर्व्हर क्षमता सूचीबद्ध
- टूल्स चाचणीसाठी उपलब्ध
- यशस्वी JSON-RPC संदेश देवाणघेवाण
- टूल प्रतिसाद इंटरफेसमध्ये प्रदर्शित

### सामान्य समस्या आणि उपाय

**सर्व्हर सुरू होत नाही:**
- सर्व आवश्यक डिपेंडेंसीज इंस्टॉल आहेत का तपासा: `pip install mcp`
- Python सिंटॅक्स आणि इंडेंटेशन तपासा
- कन्सोलमध्ये त्रुटी संदेश पहा

**टूल्स दिसत नाहीत:**
- `@server.tool()` डेकोरेटर्स आहेत का तपासा
- टूल फंक्शन्स `main()` आधी परिभाषित आहेत का तपासा
- सर्व्हर योग्यरित्या कॉन्फिगर केला आहे का खात्री करा

**कनेक्शन समस्या:**
- सर्व्हर stdio ट्रान्सपोर्ट योग्यरित्या वापरत आहे का तपासा
- कोणतेही इतर प्रोसेसेस अडथळा आणत नाहीत याची खात्री करा
- Inspector कमांड सिंटॅक्स योग्य आहे का तपासा

## असाइनमेंट

आपला सर्व्हर अधिक क्षमतांसह विकसित करण्याचा प्रयत्न करा. उदाहरणार्थ, [ही पृष्ठे](https://api.chucknorris.io/) पाहा आणि API कॉल करणारे टूल बनवा. तुम्ही ठरवा की सर्व्हर कसा असावा. मजा करा :)

## सोल्यूशन

[सोल्यूशन](./solution/README.md) येथे कार्यरत कोडसह एक शक्यतो सोल्यूशन आहे.

## मुख्य मुद्दे

या अध्यायातील मुख्य मुद्दे पुढीलप्रमाणे:

- stdio ट्रान्सपोर्ट स्थानिक MCP सर्व्हरसाठी शिफारसीय यंत्रणा आहे.
- stdio ट्रान्सपोर्ट MCP सर्व्हर आणि क्लायंट दरम्यान स्टँडर्ड इनपुट आणि आउटपुट स्ट्रीम वापरून अखंड संवाद साधण्याची परवानगी देतो.
- आपण stdio सर्व्हर्ससाठी थेट Inspector आणि Visual Studio Code वापरू शकता, जे डिबगिंग आणि इंटिग्रेशन सुलभ करते.

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

तुम्ही stdio ट्रान्सपोर्टसह MCP सर्व्हर तयार करायला शिकलात, आता तुम्ही अधिक प्रगत विषयांचा अभ्यास करू शकता:

- **पुढे:** [MCP सह HTTP स्ट्रीमिंग (Streamable HTTP)](../06-http-streaming/README.md) - रिमोट सर्व्हरसाठी दुसरा समर्थित ट्रान्सपोर्ट यंत्रणा समजून घ्या
- **प्रगत:** [MCP सुरक्षा उत्तम पद्धती](../../02-Security/README.md) - आपल्या MCP सर्व्हरमध्ये सुरक्षा अमलात आणा
- **उत्पादन:** [तैनाती धोरणे](../09-deployment/README.md) - उत्पादनासाठी आपल्या सर्व्हरची तैनात करा

## अतिरिक्त स्रोत

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - अधिकृत स्पेसिफिकेशन
- [MCP SDK दस्तऐवज](https://github.com/modelcontextprotocol/sdk) - सर्व भाषांसाठी SDK संदर्भ
- [समुदाय उदाहरणे](../../06-CommunityContributions/README.md) - समुदायाकडून अधिक सर्व्हर उदाहरणे

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवेद्वारे [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो परंतु कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हे अधिकारिक स्रोत मानले जावे. महत्त्वाची माहिती असल्यास, व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे निर्माण झालेल्या कोणत्याही गैरसमजुतीसाठी किंवा चुकीच्या अर्थ लावणीसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->