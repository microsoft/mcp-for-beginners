# stdio ट्रान्सपोर्टसहित MCP सर्भर

> **⚠️ महत्त्वपूर्ण अपडेट**: MCP विशिष्टता 2025-06-18 अनुसार, स्टैंडअलोन SSE (सर्भर-सेन्ट इभेन्ट्स) ट्रान्सपोर्टलाई **बेहोस** गरिएको छ र "Streamable HTTP" ट्रान्सपोर्टले प्रतिस्थापन गरेको छ। हालको MCP विशिष्टताले दुई मुख्य ट्रान्सपोर्ट तन्त्रहरू परिभाषित गर्छ:
> 1. **stdio** - मानक इनपुट/आउटपुट (स्थानीय सर्भरहरूका लागि सिफारिस गरिएको)
> 2. **Streamable HTTP** - रिमोट सर्भरहरूका लागि जुन आन्तरिक रूपमा SSE प्रयोग गर्न सक्छन्
>
> यो पाठ अब **stdio ट्रान्सपोर्ट**मा केन्द्रित छ, जुन अधिकांश MCP सर्भर कार्यन्वयनहरूको लागि सिफारिस गरिएको विधि हो।

stdio ट्रान्सपोर्टले MCP सर्भरहरूलाई क्लाइन्टहरूसँग मानक इनपुट र आउटपुट स्ट्रिमहरूको माध्यमबाट संवाद गर्न अनुमति दिन्छ। यो हालको MCP विशिष्टतामा सबैभन्दा बढी प्रयोग हुने र सिफारिस गरिएको ट्रान्सपोर्ट मेकानिजम हो जसले विभिन्न क्लाइन्ट एप्लिकेसनहरूसँग सजिलै एकीकृत गर्न सकिने सरल र प्रभावकारी तरिका प्रदान गर्दछ।

## अवलोकन

यस पाठले stdio ट्रान्सपोर्ट प्रयोग गरी MCP सर्भरहरू कसरी बनाउन र उपयोग गर्न सकिन्छ भन्ने विषय समेट्छ।

## सिकाइ उद्देश्यहरू

यस पाठको अन्त्यसम्म, तपाईं सक्षम हुनुहुनेछ:

- stdio ट्रान्सपोर्ट प्रयोग गरी MCP सर्भर बनाउनु।
- Inspector प्रयोग गरी MCP सर्भर डिबग गर्नु।
- Visual Studio Code मार्फत MCP सर्भर उपभोग गर्नु।
- हालका MCP ट्रान्सपोर्ट मेकानिजमहरू बुझ्नु र किन stdio सिफारिस गरिएको छ बुझ्नु।

## stdio ट्रान्सपोर्ट - यो कसरी काम गर्छ

stdio ट्रान्सपोर्ट MCP विशिष्टता (2025-06-18) अन्तर्गत समर्थित दुई ट्रान्सपोर्ट प्रकारहरूमध्ये एउटा हो। यसले यसरी काम गर्छ:

- **साधारण संवाद**: सर्भरले JSON-RPC सन्देशहरू मानक इनपुट (`stdin`) बाट पढ्छ र मानक आउटपुट (`stdout`) मा सन्देशहरू पठाउँछ।
- **प्रोसेस-आधारित**: क्लाइन्टले MCP सर्भरलाई subprocess को रूपमा सुरु गर्छ।
- **सन्देश ढाँचा**: सन्देशहरू व्यक्तिगत JSON-RPC अनुरोधहरू, सूचना वा प्रतिक्रियाहरू हुन्छन् र नयाँ लाइनले छुट्याइएका हुन्छन्।
- **लगिङ**: सर्भरले लगिङको लागि मानक त्रुटि (`stderr`) मा UTF-8 स्ट्रिङ लेख्न सक्छ।

### मुख्य आवश्यकताहरू:
- सन्देशहरू newline द्वारा छुट्याइएका हुनुपर्छ र सन्देशमा embedded newlines हुनुहुँदैन
- सर्भरले `stdout` मा मान्य MCP सन्देश बाहेक अरु केही लेख्नु हुँदैन
- क्लाइन्टले सर्भरको `stdin` मा मान्य MCP सन्देश बाहेक अरु केही लेख्नु हुँदैन

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

अघिल्लो कोडमा:

- हामीले MCP SDK बाट `Server` क्लास र `StdioServerTransport` आयात गरेका छौं
- हामीले साधारण कन्फिगरेशन र क्षमता सहित सर्भर instance बनाएका छौं

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

अघिल्लो कोडमा हामीले:

- MCP SDK प्रयोग गरेर सर्भर instance सिर्जना गरेका छौं
- डेकोरेटरहरू प्रयोग गरी उपकरणहरू परिभाषित गरेका छौं
- stdio_server context manager प्रयोग गरी ट्रान्सपोर्ट सम्हालेका छौं

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

SSE बाट मुख्य भिन्नता stdio सर्भरहरूमाः

- वेब सर्भर सेटअप वा HTTP endpoints आवश्यक छैन
- क्लाइन्टले subprocess को रूपमा सुरु गर्छ
- stdin/stdout स्ट्रिम मार्फत संवाद गर्छ
- लागू र डिबग गर्न सजिलो

## अभ्यास: stdio सर्भर सिर्जना गर्नुहोस्

हामीले सर्भर बनाउन दुई कुराहरू ध्यानमा राख्नु पर्छ:

- जडान र सन्देशहरूको लागि एन्डपोइन्टहरू प्रदान गर्न वेब सर्भर आवश्यक छ।

## प्रयोगशाला: साधारण MCP stdio सर्भर सिर्जना

यस प्रयोगशालामा, हामीले सिफारिस गरिएको stdio ट्रान्सपोर्ट प्रयोग गरी एक सरल MCP सर्भर बनाउनेछौं। यो सर्भरले उपकरणहरू प्रदान गर्नेछ जुन क्लाइन्टहरूले मानक Model Context Protocol प्रयोग गरी कल गर्न सक्छन्।

### आवश्यकताहरू

- Python 3.8 वा पछि संस्करण
- MCP Python SDK: `pip install mcp`
- async प्रोग्रामिङ्गको आधारभूत बुझाइ

पहिलो MCP stdio सर्भर बनाउँदै सुरु गरौं:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# लगिङ कन्फिगर गर्नुहोस्
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# सर्भर बनाउनुहोस्
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
    # stdio यातायात प्रयोग गर्नुहोस्
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## SSE दृष्टिकोणबाट मुख्य भिन्नताहरू

**Stdio Transport (हालको मापदण्ड):**
- सरल subprocess मोडेल - क्लाइन्टले सर्भरलाई छोरो प्रोसेसको रूपमा सुरु गर्छ
- stdin/stdout मार्फत JSON-RPC सन्देशहरूसँग संवाद
- HTTP सर्भर सेटअप आवश्यक छैन
- उत्कृष्ट प्रदर्शन र सुरक्षा
- सजिलो डिबगिङ र विकास

**SSE Transport (MCP 2025-06-18 देखि बेहोस गरिएको):**
- HTTP सर्भर र SSE एन्डप्वाइन्टहरू आवश्यक पर्थ्यो
- वेब सर्भर पूर्वाधार सहित जटिल सेटअप
- HTTP एन्डप्वाइन्टहरूको लागि थप सुरक्षा विचारहरू
- वेब आधारित परिदृश्यहरूका लागि Streamable HTTP द्वारा प्रतिस्थापित

### stdio ट्रान्सपोर्टसहित सर्भर सिर्जना

हामीले हाम्रो stdio सर्भर बनाउन आवश्यक छ:

1. **आवश्यक पुस्तकालयहरू आयात गर्नुहोस्** - MCP सर्भर कम्पोनेन्ट र stdio ट्रान्सपोर्ट आवश्यक छ
2. **सर्भर instance सिर्जना गर्नुहोस्** - क्षमता सहित सर्भर परिभाषित गर्नुहोस्
3. **उपकरणहरू परिभाषित गर्नुहोस्** - हामीले खोल्न चाहेका कार्यहरू थप्नुहोस्
4. **ट्रान्सपोर्ट सेटअप गर्नुहोस्** - stdio संवाद कन्फिगर गर्नुहोस्
5. **सर्भर चलाउनुहोस्** - सर्भर सुरु गरी सन्देशहरू सम्हाल्नुहोस्

हामी यो क्रमशः बनाउने छौं:

### चरण १: आधारभूत stdio सर्भर सिर्जना

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

### चरण २: थप उपकरणहरू थप्नुहोस्

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

### चरण ३: सर्भर चलाउनुहोस्

कोडलाई `server.py` नाममा बचत गरी कमाण्ड लाइनबाट चलाउनुहोस्:

```bash
python server.py
```

सर्भर सुरु हुनेछ र stdin बाट इनपुटको लागि पर्खिनेछ। यसले stdio ट्रान्सपोर्टबाट JSON-RPC सन्देशहरू मार्फत संवाद गर्छ।

### चरण ४: Inspector सँग परीक्षण

तपाईं आफ्नो सर्भर Inspector प्रयोग गरेर परीक्षण गर्न सक्नुहुन्छ:

1. Inspector स्थापना गर्नुहोस्: `npx @modelcontextprotocol/inspector`
2. Inspector चलाएर आफ्नो सर्भरमा संकेत गर्नुहोस्
3. तपाईंले बनाएको उपकरणहरू परीक्षण गर्नुहोस्

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## तपाइँको stdio सर्भर डिबग गर्नुहोस्

### MCP Inspector प्रयोग गरेर

MCP Inspector MCP सर्भरहरू डिबग र परीक्षण गर्न एक उपयोगी उपकरण हो। यो stdio सर्भरसँग कसरी प्रयोग गर्ने:

1. **Inspector स्थापना गर्नुहोस्**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector चलाउनुहोस्**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **तपाईंको सर्भर परीक्षण गर्नुहोस्**: Inspector ले वेब इन्टरफेस प्रदान गर्दछ जहाँ तपाइँले:
   - सर्भर क्षमता हेर्न सक्नुहुन्छ
   - फरक प्यारामिटरसहित उपकरणहरू परीक्षण गर्नुहोस्
   - JSON-RPC सन्देशहरू अनुगमन गर्नुहोस्
   - जडान समस्याहरू डिबग गर्नुहोस्

### VS Code प्रयोग गरेर

तपाईंले आफ्नो MCP सर्भर VS Code भित्रै डिबग गर्न सक्नुहुन्छ:

1. `.vscode/launch.json` मा एउटा लन्च कन्फिगरेसन बनाउनुहोस्:
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

2. सर्भर कोडमा ब्रेकप्वाइन्टहरू सेट गर्नुहोस्
3. डिबगर चलाएर Inspector सँग परीक्षण गर्नुहोस्

### सामान्य डिबगिङ टिप्स

- लगिङका लागि `stderr` प्रयोग गर्नुहोस् - MCP सन्देशहरूको लागि `stdout` सदैव आरक्षित राख्नुहोस्
- सबै JSON-RPC सन्देशहरू newline delimit हुनु आवश्यक छ
- सरल उपकरणहरूबाट परीक्षण सुरु गर्नुहोस्, जटिल कार्यक्षमता थप्नु अघि
- सन्देश ढाँचाहरू प्रमाणित गर्न Inspector प्रयोग गर्नुहोस्

## VS Code मा तपाइँको stdio सर्भर उपभोग

तपाईंले आफ्नो MCP stdio सर्भर बनाएपछि, यसलाई VS Code सँग एकीकृत गरेर Claude वा अन्य MCP-संगत क्लाइन्टहरूले प्रयोग गर्न सक्नुहुन्छ।

### कन्फिगरेसन

1. **एक MCP कन्फिगरेसन फाइल सिर्जना गर्नुहोस्** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) वा `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) मा:

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

2. **Claude पुनः सुरु गर्नुहोस्**: नयाँ सर्भर कन्फिगरेशन लोड गर्न Claude बन्द गरी पुन: खोल्नुहोस्।

3. **जोड परीक्षण गर्नुहोस्**: Claude सँग संवाद आरम्भ गरेर आफ्नो सर्भर उपकरणहरू प्रयोग गरेर प्रयास गर्नुहोस्:
   - "तपाईंले अभिवादन उपकरण प्रयोग गरेर मलाई अभिवादन गर्न सक्नुहुन्छ?"
   - "१५ र २७ को योगफल निकाल्नुहोस्"
   - "सर्भर जानकारी के हो?"

### TypeScript stdio सर्भर उदाहरण

संकेतका लागि पूर्ण TypeScript उदाहरण:

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

यस अपडेट गरिएको पाठमा, तपाईंले कसरी:

- हालको **stdio ट्रान्सपोर्ट** प्रयोग गरी MCP सर्भरहरू बनाउन (सिफारिस गरिने तरिका)
- SSE ट्रान्सपोर्ट किन बेहोस गरियो र stdio तथा Streamable HTTP किन सिफारिस गरिन्छ बुझ्न
- MCP क्लाइन्टहरूले कल गर्न सक्ने उपकरणहरू सिर्जना गर्न
- MCP Inspector प्रयोग गरी सर्भर डिबग गर्न
- आफ्नो stdio सर्भरलाई VS Code र Claude सँग एकीकृत गर्न

सिक्नुभयो।

stdio ट्रान्सपोर्टले बेहोस गरिएको SSE दृष्टिकोणको तुलनामा MCP सर्भरहरू बनाउन सरल, सुरक्षित र उच्च प्रदर्शन गर्ने तरिका प्रदान गर्दछ। यो 2025-06-18 मिति विशिष्टताको अनुसार अधिकांश MCP सर्भर कार्यन्वयनहरूको लागि सिफारिस गरिने ट्रान्सपोर्ट हो।


### .NET

1. सुरुमा हामी केही उपकरणहरू बनाउँछौं, यसको लागि हामीले *Tools.cs* फाइल बनाउने छौं जसमा तलको सामग्री हुनेछ:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## अभ्यास: तपाइँको stdio सर्भर परीक्षण

अब जब तपाईंले stdio सर्भर बनाइसक्नुभयो, त्यसलाई सही तरिकाले काम गर्छ कि गर्दैन जाँचौं।

### आवश्यकताहरू

1. सुनिश्चित गर्नुहोस् कि MCP Inspector स्थापना भइसकेको छ:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. आफ्नो सर्भर कोड सुरक्षित गरिएको छ (जस्तै, `server.py`)

### Inspector सँग परीक्षण

1. **तपाईंको सर्भरसहित Inspector सुरु गर्नुहोस्**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **वेब इन्टरफेस खोल्नुहोस्**: Inspector ले तपाईंको सर्भर क्षमताहरू देखाउने ब्राउजर विन्डो खोल्नेछ।

3. **उपकरणहरू परीक्षण गर्नुहोस्**:
   - फरक नामहरू सहित `get_greeting` उपकरण प्रयास गर्नुहोस्
   - विभिन्न नम्बरहरूसँग `calculate_sum` परीक्षण गर्नुहोस्
   - सर्भर मेटाडाटा हेर्न `get_server_info` कल गर्नुहोस्

4. **संवाद अनुगमन गर्नुहोस्**: Inspector मा क्लाइन्ट र सर्भरबीच आदानप्रदान भइरहेका JSON-RPC सन्देशहरू देखिन्छन्।

### तपाईंले के देख्नु पर्छ

जब सर्भर सफलतापूर्वक सुरु हुन्छ, तपाईंले देख्नु पर्ने कुरा:
- Inspector मा सर्भर क्षमताहरू सूचीबद्ध
- परीक्षणका लागि उपलब्ध उपकरणहरू
- सफल JSON-RPC सन्देशहरूका आदानप्रदान
- इन्टरफेसमा उपकरण प्रतिक्रियाहरू देखापर्नु

### सामान्य समस्या र समाधान

**सर्भर सुरु हुँदैन:**
- सबै निर्भरताहरू स्थापना गरिसकेको छ कि छैन जाँच गर्नुहोस्: `pip install mcp`
- Python syntax र इन्डेन्टेशन जाँच्नुहोस्
- कन्सोलमा त्रुटि सन्देश हेर्नुहोस्

**उपकरणहरू देखिंदैनन्:**
- सुनिश्चित गर्नुहोस् `@server.tool()` डेकोरेटरहरू छन्
- मुख्य() अघि उपकरण कार्यहरू परिभाषित गरिएको छ कि छैन जाँच्नुहोस्
- सर्भर सही रूपमा कन्फिगर गरिएको छ कि छैन

**जडान समस्याहरू:**
- सर्भर stdio ट्रान्सपोर्ट सही प्रयोग गरिरहेको छ कि छैन जाँच्नुहोस्
- अरू कुनै प्रक्रिया हस्तक्षेप गर्दैछ कि छैन जांच गर्नुहोस्
- Inspector कमाण्ड सिन्ट्याक्स सही छ कि छैन

## असाइनमेन्ट

तपाईंको सर्भरमा थप क्षमताहरू बनाउने प्रयास गर्नुहोस्। उदाहरणको लागि [यस पेज](https://api.chucknorris.io/) हेर्नुहोस्, API कल गर्ने उपकरण थप्न सक्नुहुन्छ। सर्भर कस्तो देखिनुपर्छ भन्ने चयन तपाईंको हो। रमाइलो गर्नुहोस् :)

## समाधान

[समाधान](./solution/README.md) यहाँ एक सम्भावित समाधान छ जागरूक कोड सहित।

## मुख्य निष्कर्षहरू

यस अध्यायका मुख्य निष्कर्षहरू:

- stdio ट्रान्सपोर्ट स्थानीय MCP सर्भरहरूको लागि सिफारिस गरिने तन्त्र हो।
- stdio ट्रान्सपोर्टले MCP सर्भर र क्लाइन्टबीच मानक इनपुट/आउटपुट स्ट्रिममार्फत सहज संवाद प्रदान गर्दछ।
- Inspector र Visual Studio Code दुबै stdio सर्भरलाई सिधै उपभोग गर्न सकिन्छ, जसले डिबगिङ र एकीकरणलाई सहज बनाउँछ।

## नमूनाहरू 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## थप स्रोतहरू

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## अब के?

## आगामी कदमहरू

अब जब तपाईंले stdio ट्रान्सपोर्टको साथ MCP सर्भरहरू बनाउने तरिका सिक्नुभयो, तपाईं थप उन्नत विषयहरू अनुसन्धान गर्न सक्नुहुन्छ:

- **अर्को**: [MCP सँग HTTP स्ट्रिमिङ (Streamable HTTP)](../06-http-streaming/README.md) - रिमोट सर्भरहरूको लागि समर्थित अर्को ट्रान्सपोर्ट मेकानिजम सिक्नुहोस्
- **उन्नत**: [MCP सुरक्षा उत्तम अभ्यासहरू](../../02-Security/README.md) - आफ्नो MCP सर्भरहरूमा सुरक्षा लागू गर्नुहोस्
- **उत्पादन**: [डिप्लोयमेन्ट रणनीतिहरू](../09-deployment/README.md) - उत्पादन प्रयोगका लागि सर्भरहरू डिप्लोय गर्नुहोस्

## थप स्रोतहरू

- [MCP विशिष्टता 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - आधिकारिक विशिष्टता
- [MCP SDK दस्तावेज](https://github.com/modelcontextprotocol/sdk) - सबै भाषाहरूका SDK सन्दर्भहरू
- [समुदाय उदाहरणहरू](../../06-CommunityContributions/README.md) - समुदायबाट थप सर्भर उदाहरणहरू

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं भने पनि, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोतको रूपमा मानिनुपर्छ। महत्वपूर्ण सूचनाहरुको लागि व्यावसायिक मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा त्रुटिप्रति हामी उत्तरदायी छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->