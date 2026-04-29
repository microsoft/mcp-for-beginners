# stdio ट्रांसपोर्ट के साथ MCP सर्वर

> **⚠️ महत्वपूर्ण अपडेट**: MCP विनिर्देशन 2025-06-18 के अनुसार, standalone SSE (Server-Sent Events) ट्रांसपोर्ट को **अप्रचलित** घोषित किया गया है और इसे "Streamable HTTP" ट्रांसपोर्ट द्वारा प्रतिस्थापित किया गया है। वर्तमान MCP विनिर्देशन दो प्रमुख ट्रांसपोर्ट तंत्रों को परिभाषित करता है:
> 1. **stdio** - स्टैण्डर्ड इनपुट/आउटपुट (स्थानीय सर्वरों के लिए अनुशंसित)
> 2. **Streamable HTTP** - रिमोट सर्वरों के लिए जो आंतरिक रूप से SSE का उपयोग कर सकते हैं
>
> इस पाठ को अपडेट किया गया है ताकि यह **stdio ट्रांसपोर्ट** पर केंद्रित हो, जो अधिकांश MCP सर्वर कार्यान्वयनों के लिए अनुशंसित तरीका है।

stdio ट्रांसपोर्ट MCP सर्वरों को क्लाइंट के साथ स्टैण्डर्ड इनपुट और आउटपुट स्ट्रीम के माध्यम से संवाद करने की अनुमति देता है। यह वर्तमान MCP विनिर्देशन में सबसे आम और अनुशंसित ट्रांसपोर्ट तंत्र है, जो MCP सर्वरों को सरल और प्रभावी तरीके से बनाने की सुविधा प्रदान करता है जिन्हें विभिन्न क्लाइंट अनुप्रयोगों के साथ आसानी से जोड़ा जा सकता है।

## अवलोकन

यह पाठ stdio ट्रांसपोर्ट का उपयोग करके MCP सर्वर बनाने और उपयोग करने को कवर करता है।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- stdio ट्रांसपोर्ट का उपयोग करके MCP सर्वर बनाना।
- Inspector का उपयोग करके MCP सर्वर को डिबग करना।
- Visual Studio Code का उपयोग करके MCP सर्वर को उपभोग करना।
- वर्तमान MCP ट्रांसपोर्ट तंत्रों को समझना और यह क्यों stdio अनुशंसित है।

## stdio ट्रांसपोर्ट - यह कैसे काम करता है

stdio ट्रांसपोर्ट वर्तमान MCP विनिर्देशन (2025-06-18) में समर्थित दो ट्रांसपोर्ट प्रकारों में से एक है। यह इस तरह काम करता है:

- **सरल संचार**: सर्वर स्टैण्डर्ड इनपुट (`stdin`) से JSON-RPC संदेश पढ़ता है और स्टैण्डर्ड आउटपुट (`stdout`) पर संदेश भेजता है।
- **प्रक्रिया-आधारित**: क्लाइंट MCP सर्वर को एक subprocess के रूप में लॉन्च करता है।
- **संदेश प्रारूप**: संदेश व्यक्तिगत JSON-RPC अनुरोध, सूचनाएं, या प्रतिक्रियाएँ होती हैं, जिन्हें नए लाइन से अलग किया जाता है।
- **लॉगिंग**: सर्वर लॉगिंग के लिए स्टैण्डर्ड एरर (`stderr`) पर UTF-8 स्ट्रिंग्स लिख सकता है।

### मुख्य आवश्यकताएँ:
- संदेश नव-पंक्तियों द्वारा सीमांकित होने चाहिए और उनमें एम्बेडेड नई पंक्तियाँ नहीं होनी चाहिए
- सर्वर `stdout` पर केवल मान्य MCP संदेश लिखे, अन्य कुछ नहीं
- क्लाइंट सर्वर के `stdin` पर केवल मान्य MCP संदेश लिखे, अन्य कुछ नहीं

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

पिछले कोड में:

- हमने MCP SDK से `Server` क्लास और `StdioServerTransport` इम्पोर्ट किया
- हमने बुनियादी कॉन्फ़िगरेशन और क्षमताओं के साथ सर्वर इंस्टेंस बनाया
- हमने एक `StdioServerTransport` इंस्टेंस बनाया और सर्वर को उससे जोड़ा, जिससे stdin/stdout के माध्यम से संचार सक्षम हुआ

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# सर्वर उदाहरण बनाएँ
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

पिछले कोड में हमने:

- MCP SDK का उपयोग करके सर्वर इंस्टेंस बनाया
- डेकोरेटर्स का उपयोग कर उपकरण परिभाषित किए
- stdio_server context manager का उपयोग करके ट्रांसपोर्ट संभाला

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

SSE से मुख्य अंतर यह है कि stdio सर्वर:

- वेब सर्वर सेटअप या HTTP एंडपॉइंट की आवश्यकता नहीं रखते
- क्लाइंट द्वारा subprocess के रूप में लॉन्च होते हैं
- stdin/stdout स्ट्रीम के माध्यम से संवाद करते हैं
- सरलता से लागू और डिबग किए जा सकते हैं

## अभ्यास: stdio सर्वर बनाना

हमारा सर्वर बनाने के लिए हमें दो बातों का ध्यान रखना होगा:

- हमें कनेक्शन और संदेशों के लिए एंडपॉइंट्स खोलने हेतु वेब सर्वर की आवश्यकता है।
## लैब: एक सरल MCP stdio सर्वर बनाना

इस लैब में, हम अनुशंसित stdio ट्रांसपोर्ट का उपयोग करके एक सरल MCP सर्वर बनाएंगे। यह सर्वर उपकरणों को उजागर करेगा जिन्हें क्लाइंट मानक Model Context Protocol का उपयोग करके कॉल कर सकते हैं।

### आवश्यकताएँ

- Python 3.8 या बाद का संस्करण
- MCP Python SDK: `pip install mcp`
- Async प्रोग्रामिंग की बुनियादी समझ

आइए अपना पहला MCP stdio सर्वर बनाना शुरू करते हैं:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# लॉगिंग कॉन्फ़िगर करें
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# सर्वर बनाएं
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
    # stdio ट्रांसपोर्ट का उपयोग करें
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## अप्रचलित SSE विधि से मुख्य अंतर

**Stdio Transport (वर्तमान स्टैण्डर्ड):**
- सरल subprocess मॉडल - क्लाइंट सर्वर को चाइल्ड प्रोसेस के रूप में लॉन्च करता है
- JSON-RPC संदेशों का उपयोग करके stdin/stdout से संचार
- HTTP सर्वर सेटअप की आवश्यकता नहीं
- बेहतर प्रदर्शन और सुरक्षा
- डिबगिंग और विकास आसान

**SSE Transport (MCP 2025-06-18 के बाद अप्रचलित):**
- SSE एंडपॉइंट्स के साथ HTTP सर्वर की आवश्यकता
- वेब सर्वर इंफ्रास्ट्रक्चर के साथ अधिक जटिल सेटअप
- HTTP एंडपॉइंट्स के लिए अतिरिक्त सुरक्षा विचार
- वेब-आधारित परिदृश्यों के लिए अब Streamable HTTP से प्रतिस्थापित

### stdio ट्रांसपोर्ट के साथ सर्वर बनाना

हमारा stdio सर्वर बनाने के लिए हमें:

1. **आवश्यक लाइब्रेरी इम्पोर्ट करें** - MCP सर्वर कंपोनेंट्स और stdio ट्रांसपोर्ट चाहिए
2. **सर्वर इंस्टेंस बनाएं** - इसकी क्षमताओं को परिभाषित करें
3. **टूल्स परिभाषित करें** - हम जो कार्यक्षमता उजागर करना चाहते हैं जोड़ें
4. **ट्रांसपोर्ट सेटअप करें** - stdio संचार कॉन्फ़िगर करें
5. **सर्वर चलाएं** - सर्वर शुरू करें और संदेशों को संभालें

आइए इसे चरणबद्ध तरीके से बनाएं:

### चरण 1: एक बुनियादी stdio सर्वर बनाएं

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# लॉगिंग कॉन्फ़िगर करें
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# सर्वर बनाएँ
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

### चरण 2: अधिक टूल जोड़ें

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

### चरण 3: सर्वर चलाएं

कोड को `server.py` के रूप में सहेजें और कमांड लाइन से चलाएं:

```bash
python server.py
```

सर्वर शुरू होगा और stdin से इनपुट का इंतजार करेगा। यह stdio ट्रांसपोर्ट के माध्यम से JSON-RPC संदेशों का उपयोग करता है।

### चरण 4: Inspector के साथ परीक्षण

आप MCP Inspector का उपयोग करके अपने सर्वर का परीक्षण कर सकते हैं:

1. Inspector इंस्टॉल करें: `npx @modelcontextprotocol/inspector`
2. Inspector चलाएं और इसे अपने सर्वर की ओर इंगित करें
3. अपने बनाए टूल्स का परीक्षण करें

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## अपने stdio सर्वर को डिबग करना

### MCP Inspector का उपयोग करना

MCP Inspector MCP सर्वरों का डिबगिंग और परीक्षण करने के लिए एक मूल्यवान उपकरण है। इसे अपने stdio सर्वर के साथ उपयोग करने के तरीके इस प्रकार हैं:

1. **Inspector इंस्टॉल करें**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector चलाएं**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **अपने सर्वर का परीक्षण करें**: Inspector एक वेब इंटरफ़ेस प्रदान करता है जहां आप:
   - सर्वर क्षमताओं को देख सकते हैं
   - विभिन्न पैरामीटर के साथ टूल्स का परीक्षण कर सकते हैं
   - JSON-RPC संदेश मॉनिटर कर सकते हैं
   - कनेक्शन समस्याओं का डिबग कर सकते हैं

### VS Code का उपयोग करना

आप VS Code में सीधे अपने MCP सर्वर का डिबग भी कर सकते हैं:

1. `.vscode/launch.json` में एक लॉन्च कॉन्फ़िगरेशन बनाएं:
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

2. अपने सर्वर कोड में ब्रेकपॉइंट सेट करें
3. डिबगर चलाएं और Inspector के साथ परीक्षण करें

### सामान्य डिबगिंग टिप्स

- लॉगिंग के लिए `stderr` का उपयोग करें - कभी भी `stdout` पर न लिखें क्योंकि यह MCP संदेशों के लिए आरक्षित है
- सभी JSON-RPC संदेश newline से सीमांकित हों
- पहले सरल टूल्स के साथ परीक्षण करें, फिर जटिल कार्यक्षमता जोड़ें
- संदेश प्रारूप सत्यापित करने के लिए Inspector का उपयोग करें

## VS Code में अपने stdio सर्वर का उपयोग करना

एक बार जब आप अपना MCP stdio सर्वर बना लेते हैं, तो आप इसे VS Code के साथ एकीकृत कर सकते हैं ताकि इसे Claude या अन्य MCP-समर्थित क्लाइंट्स के साथ उपयोग किया जा सके।

### कॉन्फ़िगरेशन

1. Windows पर `%APPDATA%\Claude\claude_desktop_config.json` या Mac पर `~/Library/Application Support/Claude/claude_desktop_config.json` पर एक MCP कॉन्फ़िगरेशन फ़ाइल बनाएँ:

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

2. **Claude को पुनरारंभ करें**: Claude को बंद करें और फिर से खोलें ताकि नया सर्वर कॉन्फ़िगरेशन लोड हो सके।

3. **कनेक्शन का परीक्षण करें**: Claude के साथ बातचीत शुरू करें और अपने सर्वर के टूल्स का उपयोग करने का प्रयास करें:
   - "क्या आप greeting tool का उपयोग करके मुझसे अभिवादन कर सकते हैं?"
   - "15 और 27 का योगफल गणना करें"
   - "सर्वर जानकारी क्या है?"

### TypeScript stdio सर्वर उदाहरण

संदर्भ के लिए यहाँ एक पूरा TypeScript उदाहरण है:

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

// उपकरण जोड़ें
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

### .NET stdio सर्वर उदाहरण

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

इस अपडेट किए गए पाठ में, आपने सीखा:

- वर्तमान **stdio ट्रांसपोर्ट** (अनुशंसित तरीका) का उपयोग करके MCP सर्वर बनाना
- SSE ट्रांसपोर्ट अप्रचलित क्यों हुआ और stdio तथा Streamable HTTP को क्यों प्राथमिकता दी गई
- MCP क्लाइंट्स द्वारा कॉल किए जाने वाले टूल बनाना
- MCP Inspector का उपयोग करके अपने सर्वर को डिबग करना
- VS Code और Claude के साथ अपने stdio सर्वर को एकीकृत करना

stdio ट्रांसपोर्ट अप्रचलित SSE दृष्टिकोण की तुलना में MCP सर्वर बनाने के लिए एक सरल, अधिक सुरक्षित, और बेहतर प्रदर्शन वाली विधि प्रदान करता है। यह अधिकांश MCP सर्वर कार्यान्वयनों के लिए 2025-06-18 विनिर्देशन के अनुसार अनुशंसित ट्रांसपोर्ट है।

### .NET

1. आइए पहले कुछ टूल बनाते हैं, इसके लिए हम *Tools.cs* नामक फाइल बनाएंगे, जिसमें निम्न सामग्री होगी:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## अभ्यास: अपने stdio सर्वर का परीक्षण करना

अब जब आपने अपना stdio सर्वर बना लिया है, तो आइए इसका परीक्षण करें कि यह सही तरीके से काम करता है या नहीं।

### आवश्यकताएँ

1. सुनिश्चित करें कि आपके पास MCP Inspector इंस्टॉल है:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. आपका सर्वर कोड सहेजा हुआ हो (जैसे `server.py`)

### Inspector के साथ परीक्षण

1. **अपने सर्वर के साथ Inspector शुरू करें**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **वेब इंटरफ़ेस खोलें**: Inspector एक ब्राउज़र विंडो खोलेगा जो आपके सर्वर की क्षमताएँ दिखाएगा।

3. **टूल्स का परीक्षण करें**: 
   - विभिन्न नामों के साथ `get_greeting` टूल आज़माएं
   - विभिन्न संख्याओं के साथ `calculate_sum` टूल का परीक्षण करें
   - सर्वर मेटाडेटा देखने के लिए `get_server_info` टूल कॉल करें

4. **संचार की निगरानी करें**: Inspector JSON-RPC संदेश दिखाता है जो क्लाइंट और सर्वर के बीच आदान-प्रदान हो रहे हैं।

### आप क्या देखेंगे

जब आपका सर्वर सही से शुरू हो जाता है, तो आप देखेंगे:
- Inspector में सर्वर क्षमताएँ सूचीबद्ध
- परीक्षण के लिए उपलब्ध टूल्स
- सफल JSON-RPC संदेश विनिमय
- इंटरफ़ेस में टूल प्रतिक्रियाएँ प्रदर्शित

### सामान्य समस्याएं और समाधान

**सर्वर शुरू नहीं हो रहा:**
- सुनिश्चित करें कि सभी निर्भरताएं इंस्टॉल हैं: `pip install mcp`
- Python सिंटेक्स और इंडेंटेशन जांचें
- कंसोल में त्रुटि संदेशों को देखें

**टूल्स दिखाई नहीं दे रहे:**
- सुनिश्चित करें कि `@server.tool()` डेकोरेटर्स मौजूद हैं
- टूल फ़ंक्शन `main()` से पहले परिभाषित हों
- सर्वर ठीक से कॉन्फ़िगर हो

**कनेक्शन समस्याएँ:**
- सुनिश्चित करें कि सर्वर stdio ट्रांसपोर्ट का सही उपयोग कर रहा है
- जांचें कि अन्य प्रक्रियाएं व्यवधान नहीं डाल रही हैं
- Inspector कमांड सिंटैक्स सत्यापित करें

## असाइनमेंट

अपने सर्वर को और अधिक क्षमताओं के साथ बनाएं। उदाहरण के लिए, [यहाँ](https://api.chucknorris.io/) देखें, एक ऐसा टूल जोड़ें जो एक API को कॉल करता हो। आप तय करें कि सर्वर कैसा दिखना चाहिए। मज़े करें :)

## समाधान

[समाधान](./solution/README.md) यहाँ एक संभावित समाधान है जिसमें कार्यशील कोड है।

## मुख्य बातें

इस अध्याय से मुख्य निष्कर्ष निम्नलिखित हैं:

- stdio ट्रांसपोर्ट स्थानीय MCP सर्वरों के लिए अनुशंसित तंत्र है।
- stdio ट्रांसपोर्ट MCP सर्वरों और क्लाइंट्स के बीच स्टैण्डर्ड इनपुट और आउटपुट स्ट्रीम का उपयोग करके निर्बाध संचार प्रदान करता है।
- आप सीधे Inspector और Visual Studio Code दोनों का उपयोग करके stdio सर्वरों का उपभोग कर सकते हैं, जिससे डिबगिंग और एकीकरण सरल हो जाता है।

## नमूने

- [Java कैलकुलेटर](../samples/java/calculator/README.md)
- [.Net कैलकुलेटर](../../../../03-GettingStarted/samples/csharp)
- [JavaScript कैलकुलेटर](../samples/javascript/README.md)
- [TypeScript कैलकुलेटर](../samples/typescript/README.md)
- [Python कैलकुलेटर](../../../../03-GettingStarted/samples/python)

## अतिरिक्त संसाधन

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## आगे क्या है

## अगले कदम

अब जब आपने stdio ट्रांसपोर्ट के साथ MCP सर्वर बनाना सीख लिया है, तो आप अधिक उन्नत विषयों का पता लगा सकते हैं:

- **अगला**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - रिमोट सर्वरों के लिए दूसरे समर्थित ट्रांसपोर्ट तंत्र के बारे में जानें
- **उन्नत**: [MCP सुरक्षा सर्वोत्तम प्रथाएं](../../02-Security/README.md) - अपने MCP सर्वरों में सुरक्षा लागू करें
- **उत्पादन**: [तैनाती रणनीतियाँ](../09-deployment/README.md) - अपने सर्वर का उत्पादन उपयोग के लिए तैनात करें

## अतिरिक्त संसाधन

- [MCP विनिर्देशन 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - आधिकारिक विनिर्देशन
- [MCP SDK प्रलेखन](https://github.com/modelcontextprotocol/sdk) - सभी भाषाओं के लिए SDK संदर्भ
- [समुदाय के उदाहरण](../../06-CommunityContributions/README.md) - समुदाय से और सर्वर उदाहरण

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या गलतियां हो सकती हैं। मूल दस्तावेज़ उसकी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->