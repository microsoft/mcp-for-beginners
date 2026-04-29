# MCP सर्भर stdio ट्रान्सपोर्टसहित

> **⚠️ महत्वपूर्ण अपडेट**: MCP विनिर्देशन 2025-06-18 अनुसार, स्वतन्त्र SSE (सर्भर-सेंट इभेन्ट्स) ट्रान्सपोर्टलाई **अवमूल्यन** गरिएको छ र यसको सट्टा "Streamable HTTP" ट्रान्सपोर्ट प्रयोग गर्नुपर्ने व्यवस्था गरिएको छ। हालको MCP विनिर्देशनले दुई प्रमुख ट्रान्सपोर्ट तन्त्रहरू परिभाषित गर्दछन्:
> 1. **stdio** - मानक इनपुट/आउटपुट (स्थानीय सर्भरहरूका लागि सिफारिस गरिएको)
> 2. **Streamable HTTP** - रिमोट सर्भरहरूका लागि जुन भित्र SSE प्रयोग गर्न सक्छन्
>
> यो पाठ stdio ट्रान्सपोर्टमा केन्द्रित छ, जुन अधिकांश MCP सर्भर कार्यान्वयनहरूका लागि सिफारिस गरिएको तरिका हो।

stdio ट्रान्सपोर्टले MCP सर्भरहरूलाई क्लाइन्टहरूसँग मानक इनपुट र आउटपुट स्ट्रिमहरू मार्फत संचार गर्न अनुमति दिन्छ। यो हालको MCP विनिर्देशनमा सबैभन्दा धेरै प्रयोग गरिने र सिफारिस गरिएको ट्रान्सपोर्ट मेकानिजम हो, जसले सरल र प्रभावकारी तरिकाले MCP सर्भरहरू निर्माण गर्न सहयोग गर्दछ र विभिन्न क्लाइन्ट अनुप्रयोगहरूसँग सजिलै एकीकरण गर्न सकिन्छ।

## अवलोकन

यो पाठले stdio ट्रान्सपोर्ट प्रयोग गरी कसरी MCP सर्भरहरू बनाउन र उपयोग गर्न सकिन्छ त्यो समेट्छ।

## सिकाइ लक्ष्यहरू

यस पाठको अन्त्यसम्म, तपाईंले सक्नुहुनेछ:

- stdio ट्रान्सपोर्ट प्रयोग गरी MCP सर्भर बनाउने।
- Inspector प्रयोग गरी MCP सर्भर डिबग गर्ने।
- Visual Studio Code मार्फत MCP सर्भर उपभोग गर्ने।
- वर्तमान MCP ट्रान्सपोर्ट मेकानिज्महरू बुझ्ने र किन stdio सिफारिस गरिएको हो बुझ्ने।

## stdio ट्रान्सपोर्ट - यो कसरी काम गर्छ

stdio ट्रान्सपोर्ट हालको MCP विनिर्देशन (2025-06-18) मा समर्थन गरिएका दुई ट्रान्सपोर्ट मध्ये एक हो। यसले यसरी काम गर्छ:

- **सरल संचार**: सर्भरले JSON-RPC सन्देशहरू मानक इनपुट (`stdin`) बाट पढ्छ र मानक आउटपुट (`stdout`) मा सन्देशहरू पठाउँछ।
- **प्रोसेस-आधारित**: क्लाइन्टले MCP सर्भरलाई सबप्रोसेसको रूपमा सुरू गर्छ।
- **सन्देश ढाँचा**: सन्देशहरू व्यक्तिगत JSON-RPC अनुरोध, सूचना वा प्रतिक्रिया हुन्छन्, जुन नयाँ लाइन द्वारा छुट्टाइएका हुन्छन्।
- **लगिङ**: सर्भरले लगिङका लागि मानक त्रुटि (`stderr`) मा UTF-8 स्ट्रिङहरू लेख्न सक्छ।

### मुख्य आवश्यकताहरू:
- सन्देशहरू नयाँ लाइनले छुट्टिएका हुनुपर्छ र सन्देश भित्र कुनै पनि नयाँ लाइन हुन सक्दैन
- सर्भरले `stdout` मा MCP सन्देश बाहेक केही लेख्नु हुँदैन
- क्लाइन्टले सर्भरको `stdin` मा वैध MCP सन्देश बाहेक केही पठाउनुहुँदैन

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

माथिको कोडमा:

- हामीले MCP SDK बाट `Server` क्लास र `StdioServerTransport` आयात गरेका छौं
- आधारभूत कन्फिगरेसन र क्षमतासहित सर्भरको एक उदाहरण बनाएका छौं
- `StdioServerTransport` को उदाहरण बनाएर सर्भरलाई यो संग जडान गरेका छौं, जसले stdin/stdout मार्फत सञ्चार सक्षम गर्छ

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# सर्भर उदाहरण सिर्जना गर्नुहोस्
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

माथिको कोडमा हामीले:

- MCP SDK प्रयोग गरी सर्भर उदाहरण बनाए
- डेकोरेटर प्रयोग गरी उपकरणहरू परिभाषित गर्‍यौं
- ट्रान्सपोर्ट ह्यान्डल गर्न stdio_server कन्स्टेक्स्ट म्यानेजर प्रयोग गर्‍यौं

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

SSE बाट मुख्य अन्तर stdio सर्भरहरू:

- वेब सर्भर सेटअप वा HTTP endpoints चाहिन्न
- क्लाइन्टले सबप्रोसेसको रूपमा सर्भर सुरू गर्छ
- stdin/stdout स्ट्रिमहरू मार्फत सञ्चार हुन्छ
- कार्यान्वयन र डिबग गर्न सजिलो हुन्छ

## अभ्यास: stdio सर्भर सिर्जना गर्दै

हाम्रो सर्भर बनाउनका लागि दुई कुराहरू ध्यानमा राख्नु पर्छ:

- जडान र सन्देशहरूका लागि HTTP endpoint खुलाउन वेब सर्भर चाहिन्छ।

## प्रयोगशाला: सरल MCP stdio सर्भर सिर्जना गर्दै

यस प्रयोगशालामा, हामी सिफारिस गरिएको stdio ट्रान्सपोर्ट प्रयोग गरी सरल MCP सर्भर बनाउनेछौं। यो सर्भरले ग्राहकहरूले सामान्य Model Context Protocol मार्फत कल गर्न सक्ने उपकरणहरू सार्वजनिक गर्दछ।

### पूर्वआवश्यकताहरू

- Python 3.8 वा पछि
- MCP Python SDK: `pip install mcp`
- async प्रोग्रामिङको आधारभूत बुझाई

हाम्रो पहिलो MCP stdio सर्भर सिर्जना गर्दै सुरु गरौं:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# लगिङ कन्फिगर गर्नुहोस्
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# सर्भर सिर्जना गर्नुहोस्
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
    # stdio ट्रान्सपोर्ट प्रयोग गर्नुहोस्
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## अवमूल्यन गरिएका SSE तरिकाबाट मुख्य फरकहरू

**Stdio ट्रान्सपोर्ट (हालको मानक):**
- सरल सबप्रोसेस मोडेल - क्लाइन्टले सर्भरलाई छोरो प्रोसेसको रूपमा चलाउँछ
- stdin/stdout मार्फत JSON-RPC सन्देशहरूको सञ्चार
- HTTP सर्भर सेटअप आवश्यक छैन
- सुधारिएको प्रदर्शन र सुरक्षा
- सजिलो डिबगिङ र विकास

**SSE ट्रान्सपोर्ट (MCP 2025-06-18 देखि अवमूल्यित):**
- SSE endpoints सहित HTTP सर्भर आवश्यक थियो
- वेब सर्भर इन्फ्रास्ट्रक्चर सहित जटिल सेटअप
- HTTP endpoints को थप सुरक्षा सम्बन्धी विचारहरू
- वेब आधारित केसहरूका लागि अब Streamable HTTP द्वारा प्रतिस्थापित

### stdio ट्रान्सपोर्ट प्रयोग गरी सर्भर सिर्जना गर्दै

हामीले stdio सर्भर बनाउनका लागि:

1. **आवश्यक पुस्तकालयहरू आयात गर्ने** - MCP सर्भर कम्पोनेन्ट र stdio ट्रान्सपोर्ट चाहिन्छ
2. **सर्भर उदाहरण बनाउने** - क्षमताहरू सहित सर्भर परिभाषित गर्ने
3. **उपकरणहरू परिभाषित गर्ने** - हामीले सार्वजनिक गर्न चाहेका फङ्सनालिटीहरू थप्ने
4. **ट्रान्सपोर्ट सेटअप गर्ने** - stdio सञ्चार कन्फिगर गर्ने
5. **सर्भर चलाउने** - सर्भर सुरू गरेर सन्देशहरू ह्यान्डल गर्ने

चरणबद्ध रूपमा बनाऔं:

### चरण १: आधारभूत stdio सर्भर सिर्जना गर्ने

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# लगिङ कन्फिगर गर्नुहोस्
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# सर्भर सिर्जना गर्नुहोस्
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

### चरण २: थप उपकरणहरू थप्ने

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

### चरण ३: सर्भर चलाउने

`server.py` नामक फाइलमा कोड सुरक्षित गरी कमाण्ड लाइनबाट चलाउनुहोस्:

```bash
python server.py
```

सर्भर सुरु हुनेछ र stdin बाट इनपुटको लागि पर्खनेछ। यो stdio ट्रान्सपोर्ट मार्फत JSON-RPC सन्देशहरूले सञ्चार गर्छ।

### चरण ४: Inspector सँग परीक्षण गर्ने

तपाईं MCP Inspector प्रयोग गरेर आफ्नो सर्भर परीक्षण गर्न सक्नुहुन्छ:

1. Inspector स्थापना गर्नुहोस्: `npx @modelcontextprotocol/inspector`
2. Inspector चलाउनुहोस् र सर्भरमा पोइन्ट गर्नुहोस्
3. तपाईंले सिर्जना गरेका उपकरणहरू परीक्षण गर्नुहोस्

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## तपाईंको stdio सर्भर डिबग गर्दै

### MCP Inspector प्रयोग गर्दै

MCP Inspector MCP सर्भरहरू डिबग र परीक्षण गर्ने महत्वपूर्ण उपकरण हो। तपाईं यसलाई आफ्नो stdio सर्भरमा यसरी प्रयोग गर्न सक्नुहुन्छ:

1. **Inspector स्थापना गर्नुहोस्**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector चलाउनुहोस्**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **तपाईंको सर्भर परीक्षण गर्नुहोस्**: Inspector ले वेब इंटरफेस उपलब्ध गराउँछ जहाँ तपाईं:
   - सर्भर क्षमताहरू हेर्न सक्नुहुन्छ
   - विभिन्न प्यारामिटरहरू सहित उपकरणहरू परीक्षण गर्न सक्नुहुन्छ
   - JSON-RPC सन्देशहरू मनिटर गर्न सक्नुहुन्छ
   - जडान समस्याहरू डिबग गर्न सक्नुहुन्छ

### VS Code प्रयोग गर्दै

तपाईं आफ्नो MCP सर्भरलाई VS Code मा पनि सिधै डिबग गर्न सक्नुहुन्छ:

1. `.vscode/launch.json` मा एक लन्च कन्फिगरेसन बनाउनुहोस्:
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

2. सर्भर कोडमा ब्रेकपोइन्टहरू सेट गर्नुहोस्
3. डिबगर चलाउनुहोस् र Inspector सँग परीक्षण गर्नुहोस्

### सामान्य डिबगिङ सुझावहरू

- लगिङका लागि `stderr` प्रयोग गर्नुहोस् - `stdout` मा कहिल्यै लेख्नु हुँदैन किनकि त्यहाँ MCP सन्देश आरक्षित हुन्छ
- सबै JSON-RPC सन्देशहरू नयाँ लाइनले छुट्टिएका हुनुपर्छ
- पहिला सरल उपकरणहरू परीक्षण गरी त्यसपछि जटिल फङ्सनालिटी थप्नुहोस्
- सन्देश ढाँचा प्रमाणित गर्न Inspector प्रयोग गर्नुहोस्

## VS Code मा तपाईंको stdio सर्भर उपभोग गर्दै

जब तपाईंले MCP stdio सर्भर निर्माण गर्नु भयो, तपाईं यसलाई VS Code सँग संयुक्त गरेर Claude वा अन्य MCP-समर्थित क्लाइन्टहरूमा प्रयोग गर्न सक्नुहुन्छ।

### कन्फिगरेसन

1. Windows मा `%APPDATA%\Claude\claude_desktop_config.json` वा Mac मा `~/Library/Application Support/Claude/claude_desktop_config.json` मा MCP कन्फिगरेसन फाइल बनाउनुहोस्:

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

2. **Claude पुनः सुरु गर्नुहोस्**: नयाँ सर्भर कन्फिगरेसन लोड गर्न Claude बन्द गरी पुनः खोल्नुहोस्।

3. **जडान परीक्षण गर्नुहोस्**: Claude सँग संवाद सुरु गरी तपाईंकै सर्भरका उपकरण प्रयोग गरेर प्रयास गर्नुहोस्:
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### TypeScript stdio सर्भर उदाहरण

सन्दर्भको लागि पूर्ण TypeScript उदाहरण यहाँ छ:

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

// उपकरणहरू थप्नुहोस्
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

### .NET stdio सर्भर उदाहरण

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

यो अद्यावधिक पाठमा तपाईंले सिक्नुभयो:

- हालको **stdio ट्रान्सपोर्ट** (सिफारिस गरिएको तरिका) प्रयोग गरी MCP सर्भर बनाउने
- SSE ट्रान्सपोर्ट किन stdio र Streamable HTTP बाट अवमूल्यन गरिएको बुझ्ने
- MCP क्लाइन्टहरूले कल गर्न सक्ने उपकरणहरू सिर्जना गर्ने
- MCP Inspector प्रयोग गरी सर्भर डिबग गर्ने
- stdio सर्भरलाई VS Code र Claude सँग एकीकृत गर्ने

stdio ट्रान्सपोर्टले अवमूल्यन गरिएका SSE तरिकाको तुलनामा सरल, सुरक्षित, र राम्रो प्रदर्शन प्रदान गर्ने तरिका हो। 2025-06-18 विनिर्देशन अनुसार यो अधिकांश MCP सर्भर कार्यान्वयनहरूको लागि सिफारिस गरिएको ट्रान्सपोर्ट हो।

### .NET

1. सुरूमा हामी केही उपकरणहरू बनाउँछौं, यसका लागि हामी *Tools.cs* नामक फाइल निम्न सामग्रीसहित तयार गर्नेछौं:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## अभ्यास: तपाईंको stdio सर्भर परीक्षण गर्दै

अब तपाईंले stdio सर्भर निर्माण गर्नुभयो, यसलाई सही रूपमा काम गर्छ कि हामी परीक्षण गरौं।

### पूर्वआवश्यकताहरू

1. सुनिश्चित गर्नुहोस् कि तपाईंले MCP Inspector स्थापना गर्नुभएको छ:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. तपाईंको सर्भर कोड सुरक्षित (जस्तै `server.py` मा)

### Inspector सँग परीक्षण

1. **आफ्नो सर्भरसँग Inspector सुरु गर्नुहोस्**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **वेब इंटरफेस खोल्नुहोस्**: Inspector ले ब्राउजर विन्डो खोल्नेछ जसले तपाईंको सर्भरको क्षमताहरू देखाउनेछ।

3. **उपकरणहरू परीक्षण गर्नुहोस्**: 
   - विभिन्न नामका साथ `get_greeting` उपकरण प्रयोग गर्नुहोस्
   - विभिन्न सङ्ख्याहरू प्रयोग गरी `calculate_sum` उपकरण परीक्षण गर्नुहोस्
   - सर्भर मेटाडाटाका लागि `get_server_info` उपकरण कल गर्नुहोस्

4. **सञ्चार अनुगमन गर्नुहोस्**: Inspector ले क्लाइन्ट र सर्भरबीचको JSON-RPC सन्देशहरू देखाउँछ।

### तपाईंले के देख्नु पर्ने हो

तपाईंको सर्भर ठीकसँग सुरु हुँदा तपाईंले देख्नु हुनेछ:
- Inspector मा सर्भर क्षमताहरू सूचीबद्ध
- परीक्षणका लागि उपकरणहरू उपलब्ध
- सफल JSON-RPC सन्देश आदान-प्रदान
- उपकरण प्रतिक्रियाहरू इंटरफेसमा देखा पर्ने

### सामान्य समस्याहरू र समाधानहरू

**सर्भर सुरु हुँदैन:**
- सबै निर्भरता स्थापना भएको छ कि जाँच्नुहोस्: `pip install mcp`
- Python सिन्ट्याक्स र इन्डेण्टेशन जाँच्नुहोस्
- कन्सोलमा त्रुटि सन्देशहरू खोज्नुहोस्

**उपकरणहरू देखिदैनन्:**
- सुनिश्चित गर्नुहोस् कि `@server.tool()` डेकोरेटरहरू छन्
- उपकरण कार्यहरू `main()` भन्दा पहिले परिभाषित छन् कि छैनन् जाँच्नुहोस्
- सर्भर ठीकसँग कन्फिगर गरिएको छ कि छैन जाँच्नुहोस्

**जडान समस्याहरू:**
- सर्भर stdio ट्रान्सपोर्ट सही प्रयोग गर्दैछ कि छैन जाँच्नुहोस्
- अन्य प्रक्रिया अवरोध पु¥याइरहेका छैनन् जाँच्नुहोस्
- Inspector कमाण्ड सिन्ट्याक्स सही छ कि छैन जाँच्नुहोस्

## असाइनमेन्ट

तपाईंको सर्भरमा थप क्षमताहरू बनाउन प्रयास गर्नुहोस्। उदाहरणका लागि API कल गर्ने उपकरण थप्न [यो पृष्ठ](https://api.chucknorris.io/) हेर्नुहोस्। तपाईंले सर्भर कस्तो देखिनु पर्छ भन्नुहोस्। रमाइलो गर्नुहोस् :)

## समाधान

[समाधान](./solution/README.md) यहाँ सम्भावित समाधान र काम गर्ने कोड छ।

## मुख्य अवधारणाहरू

यस अध्यायका मुख्य बुँदाहरू:

- stdio ट्रान्सपोर्ट स्थानीय MCP सर्भरहरूका लागि सिफारिस गरिएको मेकानिजम हो।
- stdio ट्रान्सपोर्टले MCP सर्भरहरू र क्लाइन्टहरू बीच मानक इनपुट र आउटपुट स्ट्रिमहरू प्रयोग गरी सहज संचार अनुमति दिन्छ।
- तपाईं Inspector र Visual Studio Code दुवै प्रयोग गरी सीधा stdio सर्भर उपभोग गर्न सक्नुहुन्छ, जसले डिबगिङ र एकीकरण सरल बनाउँछ।

## नमूनाहरू

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## थप स्रोतहरू

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## अर्को के छ

## अर्को चरणहरू

अब तपाईंले stdio ट्रान्सपोर्ट प्रयोग गरी MCP सर्भर बनाउन सिक्नुभयो, तपाईं थप उन्नत विषयहरू अन्वेषण गर्न सक्नुहुन्छ:

- **अगाडि**: [MCP सँग HTTP स्ट्रीमिङ (Streamable HTTP)](../06-http-streaming/README.md) - रिमोट सर्भरहरूको लागि अर्को समर्थित ट्रान्सपोर्ट मेकानिजम सिक्नुहोस्
- **उन्नत**: [MCP सुरक्षा सर्वोत्तम अभ्यास](../../02-Security/README.md) - तपाईंका MCP सर्भरहरूमा सुरक्षा कार्यान्वयन गर्नुहोस्
- **उत्पादन**: [डिप्लोयमेन्ट रणनीतिहरू](../09-deployment/README.md) - उत्पादनका लागि सर्भरहरू डिप्लोय गर्नुहोस्

## थप स्रोतहरू

- [MCP विनिर्देशन 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - आधिकारिक विनिर्देशन
- [MCP SDK डकुमेन्टेसन](https://github.com/modelcontextprotocol/sdk) - सबै भाषाहरूका लागि SDK सन्दर्भहरू
- [कम्युनिटी उदाहरणहरू](../../06-CommunityContributions/README.md) - कम्युनिटीबाट थप सर्भर उदाहरणहरू

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यस दस्तावेजलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी सटीकतामा प्रयासरत छौं, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। मूल दस्तावेज यसको मूल भाषामै आधिकारिक स्रोत मानिनु पर्छ। गम्भीर जानकारीका लागि पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याहरूको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->