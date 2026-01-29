# MCP Server with stdio Transport

> **⚠️ महत्त्वपूर्ण अपडेट**: MCP Specification 2025-06-18 अनुसार, standalone SSE (Server-Sent Events) transport **अप्रचलित** भइसकेको छ र यसको स्थानमा "Streamable HTTP" transport आएको छ। हालको MCP specification ले दुई मुख्य transport विधिहरू परिभाषित गर्दछ:
> 1. **stdio** - स्थानीय सर्भरहरूको लागि सिफारिस गरिएको (Standard input/output)
> 2. **Streamable HTTP** - टाढाका सर्भरहरूको लागि, जसले आन्तरिक रूपमा SSE प्रयोग गर्न सक्छ
>
> यो पाठ stdio transport मा केन्द्रित छ, जुन अधिकांश MCP सर्भर कार्यान्वयनहरूको लागि सिफारिस गरिएको विधि हो।

stdio transport ले MCP सर्भरहरूलाई standard input र output stream मार्फत क्लाइन्टहरूसँग संवाद गर्न अनुमति दिन्छ। यो हालको MCP specification मा सबैभन्दा सामान्य र सिफारिस गरिएको transport विधि हो, जसले विभिन्न क्लाइन्ट एप्लिकेसनहरूसँग सजिलै एकीकृत गर्न सकिने सरल र प्रभावकारी तरिका प्रदान गर्दछ।

## अवलोकन

यो पाठले stdio transport प्रयोग गरेर MCP सर्भर निर्माण र उपभोग गर्ने तरिका समेट्छ।

## सिकाइ उद्देश्यहरू

यो पाठको अन्त्यसम्म, तपाईं सक्षम हुनुहुनेछ:

- stdio transport प्रयोग गरेर MCP सर्भर निर्माण गर्न।
- Inspector प्रयोग गरेर MCP सर्भर डिबग गर्न।
- Visual Studio Code प्रयोग गरेर MCP सर्भर उपभोग गर्न।
- हालको MCP transport विधिहरू बुझ्न र किन stdio सिफारिस गरिएको हो भन्ने कुरा बुझ्न।

## stdio Transport - यो कसरी काम गर्छ

stdio transport हालको MCP specification (2025-06-18) मा समर्थित दुई transport प्रकारहरू मध्ये एक हो। यसले निम्न तरिकाले काम गर्छ:

- **सरल संवाद**: सर्भरले standard input (`stdin`) बाट JSON-RPC सन्देशहरू पढ्छ र standard output (`stdout`) मा सन्देशहरू पठाउँछ।
- **प्रक्रिया-आधारित**: क्लाइन्टले MCP सर्भरलाई subprocess को रूपमा सुरु गर्छ।
- **सन्देश ढाँचा**: सन्देशहरू व्यक्तिगत JSON-RPC अनुरोधहरू, सूचनाहरू, वा प्रतिक्रियाहरू हुन्, जुन नयाँ लाइनले छुट्याइएको हुन्छ।
- **लगिङ**: सर्भरले UTF-8 स्ट्रिङहरू standard error (`stderr`) मा लगिङको लागि लेख्न सक्छ।

### मुख्य आवश्यकताहरू:
- सन्देशहरू नयाँ लाइनले छुट्याइएको हुनुपर्छ र embedded नयाँ लाइनहरू समावेश गर्न हुँदैन।
- सर्भरले `stdout` मा कुनै पनि कुरा लेख्न हुँदैन जुन मान्य MCP सन्देश होइन।
- क्लाइन्टले सर्भरको `stdin` मा कुनै पनि कुरा लेख्न हुँदैन जुन मान्य MCP सन्देश होइन।

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

उपरोक्त कोडमा:

- हामीले MCP SDK बाट `Server` class र `StdioServerTransport` आयात गरेका छौं।
- हामीले आधारभूत कन्फिगरेसन र क्षमताहरूको साथ सर्भर इन्स्ट्यान्स सिर्जना गरेका छौं।

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

उपरोक्त कोडमा:

- हामीले MCP SDK प्रयोग गरेर सर्भर इन्स्ट्यान्स सिर्जना गरेका छौं।
- डेकोरेटरहरू प्रयोग गरेर टूलहरू परिभाषित गरेका छौं।
- stdio_server context manager प्रयोग गरेर transport ह्यान्डल गरेका छौं।

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

SSE बाट stdio सर्भरको मुख्य भिन्नता:

- वेब सर्भर सेटअप वा HTTP endpoints आवश्यक पर्दैन।
- क्लाइन्टले subprocess को रूपमा सर्भर सुरु गर्छ।
- stdin/stdout stream मार्फत संवाद गर्छ।
- कार्यान्वयन र डिबग गर्न सजिलो छ।

## अभ्यास: stdio सर्भर निर्माण गर्नुहोस्

हाम्रो सर्भर निर्माण गर्न, हामीले दुई कुरामा ध्यान दिनुपर्छ:

- हामीले कनेक्शन र सन्देशहरूको लागि endpoints प्रदान गर्न वेब सर्भर प्रयोग गर्नुपर्छ।
## प्रयोगशाला: सरल MCP stdio सर्भर निर्माण गर्नुहोस्

यस प्रयोगशालामा, हामी stdio transport प्रयोग गरेर एक सरल MCP सर्भर निर्माण गर्नेछौं। यो सर्भरले standard Model Context Protocol प्रयोग गरेर क्लाइन्टहरूले कल गर्न सक्ने टूलहरू प्रदान गर्नेछ।

### पूर्वापेक्षाहरू

- Python 3.8 वा पछिल्लो संस्करण
- MCP Python SDK: `pip install mcp`
- async प्रोग्रामिङको आधारभूत ज्ञान

आउनुहोस्, हाम्रो पहिलो MCP stdio सर्भर निर्माण गरौं:

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

## SSE विधिबाट stdio विधिको मुख्य भिन्नता

**Stdio Transport (हालको मानक):**
- सरल subprocess मोडेल - क्लाइन्टले सर्भरलाई child process को रूपमा सुरु गर्छ।
- stdin/stdout मार्फत JSON-RPC सन्देशहरू प्रयोग गरेर संवाद।
- HTTP सर्भर सेटअप आवश्यक छैन।
- राम्रो प्रदर्शन र सुरक्षा।
- डिबग र विकास गर्न सजिलो।

**SSE Transport (MCP 2025-06-18 अनुसार अप्रचलित):**
- HTTP सर्भर र SSE endpoints आवश्यक थियो।
- वेब सर्भर संरचनासँग जटिल सेटअप।
- HTTP endpoints को लागि अतिरिक्त सुरक्षा विचारहरू।
- वेब-आधारित परिदृश्यहरूको लागि Streamable HTTP ले प्रतिस्थापन गरेको।

### stdio transport प्रयोग गरेर सर्भर निर्माण गर्नुहोस्

हाम्रो stdio सर्भर निर्माण गर्न, हामीले निम्न कार्यहरू गर्नुपर्छ:

1. **आवश्यक लाइब्रेरीहरू आयात गर्नुहोस्** - MCP सर्भर कम्पोनेन्टहरू र stdio transport आवश्यक छ।
2. **सर्भर इन्स्ट्यान्स सिर्जना गर्नुहोस्** - सर्भरको क्षमताहरू परिभाषित गर्नुहोस्।
3. **टूलहरू परिभाषित गर्नुहोस्** - हामीले प्रदान गर्न चाहेको कार्यक्षमता थप्नुहोस्।
4. **transport सेटअप गर्नुहोस्** - stdio संवाद कन्फिगर गर्नुहोस्।
5. **सर्भर चलाउनुहोस्** - सन्देशहरू ह्यान्डल गर्दै सर्भर सुरु गर्नुहोस्।

आउनुहोस्, यसलाई चरणबद्ध रूपमा निर्माण गरौं:

### चरण 1: आधारभूत stdio सर्भर सिर्जना गर्नुहोस्

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

### चरण 2: थप टूलहरू थप्नुहोस्

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

### चरण 3: सर्भर चलाउनुहोस्

कोडलाई `server.py` को रूपमा सुरक्षित गर्नुहोस् र कमाण्ड लाइनबाट चलाउनुहोस्:

```bash
python server.py
```

सर्भर सुरु हुनेछ र stdin बाट इनपुटको प्रतीक्षा गर्नेछ। यो stdio transport मार्फत JSON-RPC सन्देशहरू प्रयोग गरेर संवाद गर्छ।

### चरण 4: Inspector प्रयोग गरेर परीक्षण गर्नुहोस्

तपाईं आफ्नो सर्भर MCP Inspector प्रयोग गरेर परीक्षण गर्न सक्नुहुन्छ:

1. Inspector स्थापना गर्नुहोस्: `npx @modelcontextprotocol/inspector`
2. Inspector चलाउनुहोस् र आफ्नो सर्भरमा पोइन्ट गर्नुहोस्।
3. तपाईंले सिर्जना गरेका टूलहरू परीक्षण गर्नुहोस्।

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## आफ्नो stdio सर्भर डिबग गर्नुहोस्

### MCP Inspector प्रयोग गरेर

MCP Inspector MCP सर्भरहरू डिबग र परीक्षण गर्नको लागि मूल्यवान उपकरण हो। यसलाई आफ्नो stdio सर्भरसँग प्रयोग गर्ने तरिका यहाँ छ:

1. **Inspector स्थापना गर्नुहोस्**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector चलाउनुहोस्**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **सर्भर परीक्षण गर्नुहोस्**: Inspector वेब इन्टरफेस प्रदान गर्दछ जहाँ तपाईं:
   - सर्भर क्षमताहरू हेर्न सक्नुहुन्छ।
   - विभिन्न प्यारामिटरहरूसँग टूलहरू परीक्षण गर्न सक्नुहुन्छ।
   - JSON-RPC सन्देशहरू अनुगमन गर्न सक्नुहुन्छ।
   - कनेक्शन समस्याहरू डिबग गर्न सक्नुहुन्छ।

### VS Code प्रयोग गरेर

तपाईं आफ्नो MCP सर्भरलाई VS Code मा सिधै डिबग गर्न सक्नुहुन्छ:

1. `.vscode/launch.json` मा लन्च कन्फिगरेसन सिर्जना गर्नुहोस्:
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

2. आफ्नो सर्भर कोडमा ब्रेकप्वाइन्ट सेट गर्नुहोस्।
3. डिबगर चलाउनुहोस् र Inspector प्रयोग गरेर परीक्षण गर्नुहोस्।

### सामान्य डिबगिङ सुझावहरू

- `stderr` मा लगिङ प्रयोग गर्नुहोस् - `stdout` मा कहिल्यै लेख्नुहोस्, किनकि यो MCP सन्देशहरूको लागि आरक्षित छ।
- सुनिश्चित गर्नुहोस् कि सबै JSON-RPC सन्देशहरू नयाँ लाइनले छुट्याइएको छन्।
- जटिल कार्यक्षमता थप्नु अघि सरल टूलहरूसँग परीक्षण गर्नुहोस्।
- सन्देश ढाँचाहरू प्रमाणित गर्न Inspector प्रयोग गर्नुहोस्।

## आफ्नो stdio सर्भरलाई VS Code मा उपभोग गर्नुहोस्

एकपटक तपाईंले आफ्नो MCP stdio सर्भर निर्माण गरेपछि, तपाईं यसलाई Claude वा अन्य MCP-संगत क्लाइन्टहरूसँग प्रयोग गर्न VS Code मा एकीकृत गर्न सक्नुहुन्छ।

### कन्फिगरेसन

1. **MCP कन्फिगरेसन फाइल सिर्जना गर्नुहोस्** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) वा `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) मा:

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

2. **Claude पुनः सुरु गर्नुहोस्**: नयाँ सर्भर कन्फिगरेसन लोड गर्न Claude बन्द र पुनः खोल्नुहोस्।

3. **कनेक्शन परीक्षण गर्नुहोस्**: Claude सँग कुराकानी सुरु गर्नुहोस् र आफ्नो सर्भरका टूलहरू प्रयोग गरेर प्रयास गर्नुहोस्:
   - "ग्रीटिङ टूल प्रयोग गरेर मलाई अभिवादन गर्न सक्नुहुन्छ?"
   - "१५ र २७ को योग गणना गर्नुहोस्।"
   - "सर्भर जानकारी के हो?"

### TypeScript stdio सर्भर उदाहरण

यहाँ एक पूर्ण TypeScript उदाहरण सन्दर्भको लागि छ:

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

यस अपडेट गरिएको पाठमा, तपाईंले सिक्नुभयो:

- हालको **stdio transport** (सिफारिस गरिएको विधि) प्रयोग गरेर MCP सर्भर निर्माण गर्न।
- किन SSE transport लाई stdio र Streamable HTTP ले प्रतिस्थापन गरियो भन्ने कुरा बुझ्न।
- MCP क्लाइन्टहरूले कल गर्न सक्ने टूलहरू सिर्जना गर्न।
- MCP Inspector प्रयोग गरेर आफ्नो सर्भर डिबग गर्न।
- आफ्नो stdio सर्भरलाई VS Code र Claude सँग एकीकृत गर्न।

stdio transport ले अप्रचलित SSE विधिको तुलनामा सरल, सुरक्षित, र प्रभावकारी तरिका प्रदान गर्दछ। यो 2025-06-18 specification अनुसार अधिकांश MCP सर्भर कार्यान्वयनहरूको लागि सिफारिस गरिएको transport हो।

### .NET

1. सुरुमा केही टूलहरू सिर्जना गरौं, यसका लागि हामी *Tools.cs* नामक फाइल निम्न सामग्रीको साथ सिर्जना गर्नेछौं:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## अभ्यास: आफ्नो stdio सर्भर परीक्षण गर्नुहोस्

अब तपाईंले आफ्नो stdio सर्भर निर्माण गर्नुभएको छ, यसलाई सही रूपमा काम गर्छ कि गर्दैन भनेर परीक्षण गरौं।

### पूर्वापेक्षाहरू

1. सुनिश्चित गर्नुहोस् कि तपाईंले MCP Inspector स्थापना गर्नुभएको छ:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. तपाईंको सर्भर कोड सुरक्षित गरिएको हुनुपर्छ (जस्तै, `server.py` को रूपमा)

### Inspector प्रयोग गरेर परीक्षण

1. **Inspector आफ्नो सर्भरसँग सुरु गर्नुहोस्**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **वेब इन्टरफेस खोल्नुहोस्**: Inspector ब्राउजर विन्डो खोल्नेछ जहाँ तपाईं आफ्नो सर्भरका क्षमताहरू देख्न सक्नुहुन्छ।

3. **टूलहरू परीक्षण गर्नुहोस्**: 
   - `get_greeting` टूल विभिन्न नामहरूसँग प्रयास गर्नुहोस्।
   - `calculate_sum` टूल विभिन्न संख्याहरूको साथ परीक्षण गर्नुहोस्।
   - `get_server_info` टूल कल गरेर सर्भर मेटाडाटा हेर्नुहोस्।

4. **संवाद अनुगमन गर्नुहोस्**: Inspector ले क्लाइन्ट र सर्भर बीच आदानप्रदान गरिएका JSON-RPC सन्देशहरू देखाउँछ।

### तपाईंले के देख्नुपर्छ

जब तपाईंको सर्भर सही रूपमा सुरु हुन्छ, तपाईंले देख्नुपर्छ:
- Inspector मा सर्भर क्षमताहरू सूचीबद्ध।
- परीक्षणका लागि उपलब्ध टूलहरू।
- सफल JSON-RPC सन्देश आदानप्रदान।
- इन्टरफेसमा टूल प्रतिक्रियाहरू देखाइएको।

### सामान्य समस्या र समाधान

**सर्भर सुरु हुँदैन:**
- सुनिश्चित गर्नुहोस् कि सबै निर्भरता स्थापना गरिएको छ: `pip install mcp`
- Python syntax र indentation प्रमाणित गर्नुहोस्।
- कन्सोलमा त्रुटि सन्देशहरू हेर्नुहोस्।

**टूलहरू देखिँदैनन्:**
- सुनिश्चित गर्नुहोस् कि `@server.tool()` डेकोरेटरहरू उपस्थित छन्।
- टूल कार्यहरू `main()` भन्दा पहिले परिभाषित गरिएको छ।
- सर्भर सही रूपमा कन्फिगर गरिएको छ भन्ने कुरा प्रमाणित गर्नुहोस्।

**कनेक्शन समस्या:**
- सुनिश्चित गर्नुहोस् कि सर्भरले stdio transport सही रूपमा प्रयोग गरिरहेको छ।
- अन्य प्रक्रियाहरूले हस्तक्षेप गरिरहेको छैन भन्ने कुरा जाँच गर्नुहोस्।
- Inspector कमाण्ड syntax प्रमाणित गर्नुहोस्।

## असाइनमेन्ट

आफ्नो सर्भरलाई थप क्षमताहरूको साथ निर्माण गर्ने प्रयास गर्नुहोस्। [यो पृष्ठ](https://api.chucknorris.io/) हेर्नुहोस्, उदाहरणका लागि, API कल गर्ने टूल थप्न। तपाईंले सर्भर कस्तो देखिनुपर्छ भन्ने निर्णय गर्नुहोस्। रमाइलो गर्नुहोस् :)

## समाधान

[Solution](./solution/README.md) यहाँ कार्यरत कोडको साथ सम्भावित समाधान छ।

## मुख्य कुरा

यस अध्यायका मुख्य कुरा निम्न छन्:

- stdio transport स्थानीय MCP सर्भरहरूको लागि सिफारिस गरिएको विधि हो।
- stdio transport ले standard input र output stream प्रयोग गरेर MCP सर्भरहरू र क्लाइन्टहरू बीच सहज संवादको अनुमति दिन्छ।
- तपाईं Inspector र Visual Studio Code दुवै प्रयोग गरेर stdio सर्भरहरू सिधै उपभोग गर्न सक्नुहुन्छ, जसले डिबग र एकीकरणलाई सरल बनाउँछ।

## नमूनाहरू 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## थप स्रोतहरू

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## अब के गर्ने

## आगामी कदमहरू

अब तपाईंले stdio transport प्रयोग गरेर MCP सर्भर निर्माण गर्ने तरिका सिक्नुभएको छ, तपाईं थप उन्नत विषयहरू अन्वेषण गर्न सक्नुहुन्छ:

- **अगाडि**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - टाढाका सर्भरहरूको लागि समर्थित अर्को transport विधि सिक्नुहोस्।
- **उन्नत**: [MCP Security Best Practices](../../02-Security/README.md) - आफ्नो MCP सर्भरहरूमा सुरक्षा कार्यान्वयन गर्नुहोस्।
- **उत्पादन**: [Deployment Strategies](../09-deployment/README.md) - उत्पादन प्रयोगको लागि आफ्नो सर्भरहरू तैनाथ गर्नुहोस्।

## थप स्रोतहरू

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - आधिकारिक स्पेसिफिकेसन।
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - सबै भाषाहरूको लागि SDK सन्दर्भहरू।
- [Community Examples](../../06-CommunityContributions/README.md) - समुदायबाट थप सर्भर उदाहरणहरू।

---

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको छ। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छ। यसको मूल भाषा मा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।