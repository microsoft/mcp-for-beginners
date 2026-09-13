# stdio ट्रांसपोर्ट के साथ MCP सर्वर

> **⚠️ महत्वपूर्ण अपडेट**: MCP विनिर्देशन 2025-06-18 से, स्टैंडअलोन SSE (सर्वर-सेन्ट इवेंट्स) ट्रांसपोर्ट को **डिप्रिकेटेड** घोषित कर दिया गया है और इसे "Streamable HTTP" ट्रांसपोर्ट द्वारा प्रतिस्थापित किया गया है। वर्तमान MCP विनिर्देशन दो प्राथमिक ट्रांसपोर्ट तंत्रों को परिभाषित करता है:
> 1. **stdio** - स्टैंडर्ड इनपुट/आउटपुट (स्थानीय सर्वरों के लिए अनुशंसित)
> 2. **Streamable HTTP** - दूरस्थ सर्वरों के लिए जो आंतरिक रूप से SSE का उपयोग कर सकते हैं
>
> इस पाठ को **stdio ट्रांसपोर्ट** पर केंद्रित करते हुए अपडेट किया गया है, जो अधिकांश MCP सर्वर कार्यान्वयन के लिए अनुशंसित तरीका है।

stdio ट्रांसपोर्ट MCP सर्वरों को मानक इनपुट और आउटपुट स्ट्रीम के माध्यम से क्लाइंट्स के साथ संवाद करने की अनुमति देता है। यह वर्तमान MCP विनिर्देशन में सबसे अधिक उपयोग किया जाने वाला और अनुशंसित ट्रांसपोर्ट तंत्र है, जो विभिन्न क्लाइंट अनुप्रयोगों के साथ आसानी से एकीकृत किया जा सकने वाला एक सरल और कुशल तरीका प्रदान करता है।

## अवलोकन

यह पाठ stdio ट्रांसपोर्ट का उपयोग करके MCP सर्वर कैसे बनाएं और उपभोग करें, इस पर चर्चा करता है।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- stdio ट्रांसपोर्ट का उपयोग करके MCP सर्वर बनाना।
- Inspector का उपयोग करके MCP सर्वर का डिबग करना।
- Visual Studio Code का उपयोग करके MCP सर्वर का उपभोग करना।
- वर्तमान MCP ट्रांसपोर्ट तंत्रों को समझना और क्यों stdio अनुशंसित है।


## stdio ट्रांसपोर्ट - यह कैसे काम करता है

stdio ट्रांसपोर्ट MCP विनिर्देशन
`2026-07-28` के दो मानक ट्रांसपोर्ट में से एक है। यह इस प्रकार काम करता है:

- **सरल संचार**: सर्वर JSON-RPC संदेशों को स्टैण्डर्ड इनपुट (`stdin`) से पढ़ता है और संदेश स्टैण्डर्ड आउटपुट (`stdout`) पर भेजता है।
- **प्रोसेस-आधारित**: क्लाइंट MCP सर्वर को एक subprocess के रूप में लॉन्च करता है।
- **संदेश स्वरूप**: संदेश व्यक्तिगत JSON-RPC अनुरोध, सूचनाएं, या प्रतिक्रियाएं होती हैं, जिन्हें नई लाइनों द्वारा सीमांकित किया जाता है।
- **लॉगिंग**: सर्वर UTF-8 स्ट्रिंग्स को स्टैण्डर्ड एरर (`stderr`) पर लॉगिंग के लिए लिख सकता है।

### मुख्य आवश्यकताएँ:
- संदेश नई लाइनों द्वारा सीमांकित होने चाहिए और अंदर एम्बेडेड नई लाइनें नहीं होनी चाहिए
- सर्वर को `stdout` पर वैध MCP संदेश के अलावा कुछ भी नहीं लिखना चाहिए
- क्लाइंट को सर्वर के `stdin` पर वैध MCP संदेश के अलावा कुछ भी नहीं लिखना चाहिए

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

उपरोक्त कोड में:

- हम MCP SDK से `Server` क्लास और `StdioServerTransport` आयात करते हैं
- हम बुनियादी विन्यास और क्षमताओं के साथ एक सर्वर इंस्टेंस बनाते हैं
- हम एक `StdioServerTransport` इंस्टेंस बनाते हैं और सर्वर को इसके साथ जोड़ते हैं, जिससे stdin/stdout के माध्यम से संचार सक्षम होता है

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# सर्वर इंस्टेंस बनाएँ
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

उपरोक्त कोड में हम:

- MCP SDK का उपयोग करके एक सर्वर इंस्टेंस बनाते हैं
- डेकोरेटर्स का उपयोग करके टूल्स को परिभाषित करते हैं
- ट्रांसपोर्ट को संभालने के लिए stdio_server context manager का उपयोग करते हैं

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

- वेब सर्वर सेटअप या HTTP एंडपॉइंट्स की आवश्यकता नहीं रखते
- क्लाइंट द्वारा subprocesses के रूप में लॉन्च किए जाते हैं
- stdin/stdout स्ट्रीम के माध्यम से संचार करते हैं
- कार्यान्वयन और डिबगिंग में सरल हैं

## अभ्यास: stdio सर्वर बनाना

अपने सर्वर को बनाने के लिए, हमें दो बातें ध्यान में रखनी होंगी:

- कनेक्शन और संदेशों के लिए एंडपॉइंट्स को एक्सपोज़ करने के लिए हमें वेब सर्वर का उपयोग करना होगा।
## लैब: एक सरल MCP stdio सर्वर बनाना

इस लैब में, हम अनुशंसित stdio ट्रांसपोर्ट का उपयोग करके एक सरल MCP सर्वर बनाएंगे। यह सर्वर ऐसे टूल्स को एक्सपोज़ करेगा जिन्हें क्लाइंट्स मानक Model Context Protocol के माध्यम से कॉल कर सकते हैं।

### पूर्वापेक्षाएँ

- Python 3.8 या बाद का संस्करण
- MCP Python SDK: `pip install mcp`
- async प्रोग्रामिंग की बुनियादी समझ

चलिए अपना पहला MCP stdio सर्वर बनाना शुरू करते हैं:

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

## डिप्रिकेटेड SSE तरीकों से मुख्य अंतर

**Stdio ट्रांसपोर्ट (वर्तमान मानक):**
- सरल subprocess मॉडल - क्लाइंट सर्वर को चाइल्ड प्रोसेस के रूप में लॉन्च करता है
- JSON-RPC संदेशों का उपयोग करके stdin/stdout के माध्यम से संचार
- HTTP सर्वर सेटअप की आवश्यकता नहीं
- बेहतर प्रदर्शन और सुरक्षा
- आसान डिबगिंग और विकास

**SSE ट्रांसपोर्ट (MCP 2025-06-18 से डिप्रिकेटेड):**
- SSE एंडपॉइंट्स के साथ HTTP सर्वर आवश्यक था
- वेब सर्वर इन्फ्रास्ट्रक्चर के साथ अधिक जटिल सेटअप
- HTTP एंडपॉइंट्स के लिए अतिरिक्त सुरक्षा विचार
- अब वेब-आधारित परिदृश्यों के लिए Streamable HTTP द्वारा प्रतिस्थापित

### stdio ट्रांसपोर्ट के साथ सर्वर बनाना

अपने stdio सर्वर को बनाने के लिए, हमें:

1. **आवश्यक पुस्तकालय आयात करें** - MCP सर्वर घटक और stdio ट्रांसपोर्ट की आवश्यकता होती है
2. **सर्वर इंस्टेंस बनाएं** - सर्वर को इसकी क्षमताओं के साथ परिभाषित करें
3. **टूल्स परिभाषित करें** - वह कार्यक्षमता जोड़ें जो आप एक्सपोज़ करना चाहते हैं
4. **ट्रांसपोर्ट सेट करें** - stdio संचार कॉन्फ़िगर करें
5. **सर्वर चलाएं** - सर्वर शुरू करें और संदेशों को हैंडल करें

चलिए इसे एक-एक करके बनाते हैं:

### चरण 1: एक बेसिक stdio सर्वर बनाएं

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

### चरण 2: और टूल्स जोड़ें

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

### चरण 3: सर्वर चलाना

कोड को `server.py` के रूप में सेव करें और कमांड लाइन से चलाएं:

```bash
python server.py
```

सर्वर शुरू होगा और stdin से इनपुट का इंतजार करेगा। यह stdio ट्रांसपोर्ट के माध्यम से JSON-RPC संदेशों का उपयोग करके संवाद करता है।

### चरण 4: Inspector के साथ परीक्षण

आप MCP Inspector का उपयोग करके अपने सर्वर का परीक्षण कर सकते हैं:

1. Inspector स्थापित करें: `npx @modelcontextprotocol/inspector`
2. Inspector चलाएं और इसे अपने सर्वर की ओर निर्देशित करें
3. आपने जो टूल बनाए हैं, उनका परीक्षण करें

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## अपने stdio सर्वर को डिबग करना

### MCP Inspector का उपयोग करना

MCP Inspector MCP सर्वरों के डिबगिंग और परीक्षण के लिए एक मूल्यवान उपकरण है। इसे अपने stdio सर्वर के साथ उपयोग करने का तरीका यहाँ है:

1. **Inspector इंस्टॉल करें**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector चलाएं**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **अपने सर्वर का परीक्षण करें**: Inspector वेब इंटरफ़ेस प्रदान करता है जहाँ आप:
   - सर्वर की क्षमताएं देख सकते हैं
   - विभिन्न पैरामीटर के साथ टूल्स का परीक्षण कर सकते हैं
   - JSON-RPC संदेशों की निगरानी कर सकते हैं
   - कनेक्शन समस्याओं को डिबग कर सकते हैं

### VS Code का उपयोग करना

आप सीधे VS Code में भी अपने MCP सर्वर को डिबग कर सकते हैं:

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
- सुनिश्चित करें कि सभी JSON-RPC संदेश नई लाइनों से सीमांकित हों
- जटिल कार्यक्षमता जोड़ने से पहले सरल टूल्स के साथ परीक्षण करें
- संदेश स्वरूपों को सत्यापित करने के लिए Inspector का उपयोग करें

## VS Code में अपने stdio सर्वर का उपभोग करना


एक बार जब आप अपना MCP stdio सर्वर बना लेते हैं, तो आप इसे VS कोड के साथ एकीकृत कर सकते हैं ताकि इसे Claude या अन्य MCP-अनुकूल क्लाइंट्स के साथ उपयोग किया जा सके।

### कॉन्फ़िगरेशन

1. **MCP कॉन्फ़िगरेशन फ़ाइल बनाएँ** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) या `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) पर:

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

2. **Claude को पुनः प्रारंभ करें**: नया सर्वर कॉन्फ़िगरेशन लोड करने के लिए Claude को बंद करें और फिर से खोलें।

3. **कनेक्शन का परीक्षण करें**: Claude के साथ एक वार्तालाप शुरू करें और अपने सर्वर के टूल्स का उपयोग करने का प्रयास करें:
   - "क्या आप अभिवादन टूल का उपयोग करके मेरा अभिवादन कर सकते हैं?"
   - "15 और 27 का योग निकालिए"
   - "सर्वर जानकारी क्या है?"

### TypeScript stdio सर्वर उदाहरण

संदर्भ के लिए यहां एक पूर्ण TypeScript उदाहरण है:

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

इस अद्यतन पाठ में, आपने सीखा कि कैसे:

- वर्तमान **stdio ट्रांसपोर्ट** (अनुशंसित तरीका) का उपयोग करके MCP सर्वर बनाना
- समझना कि SSE ट्रांसपोर्ट को stdio और Streamable HTTP के पक्ष में क्यों हटा दिया गया
- टूल्स बनाना जिन्हें MCP क्लाइंट कॉल कर सकते हैं
- MCP इंस्पेक्टर का उपयोग करके अपने सर्वर को डिबग करना
- अपने stdio सर्वर को VS Code और Claude के साथ एकीकृत करना

stdio ट्रांसपोर्ट MCP सर्वरों के निर्माण के लिए एक सरल, अधिक सुरक्षित, और बेहतर प्रदर्शन वाला तरीका प्रदान करता है, जो हटाए गए SSE तरीके की तुलना में बेहतर है। यह 2025-06-18 विनिर्देशन के अनुसार अधिकांश MCP सर्वर कार्यान्वयन के लिए अनुशंसित ट्रांसपोर्ट है।


### .NET

1. पहले कुछ टूल्स बनाते हैं, इसके लिए हम एक फ़ाइल *Tools.cs* बनाएंगे जिसका निम्नलिखित सामग्री होगी:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## अभ्यास: अपने stdio सर्वर का परीक्षण करना

अब जब आपने अपना stdio सर्वर बना लिया है, आइए इसे ठीक से काम करने के लिए परीक्षण करें।

### पूर्व आवश्यकताएँ

1. सुनिश्चित करें कि आपके पास MCP इंस्पेक्टर इंस्टॉल है:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. आपका सर्वर कोड सेव किया गया हो (जैसे, `server.py`)

### इंस्पेक्टर के साथ परीक्षण

1. **अपने सर्वर के साथ इंस्पेक्टर शुरू करें**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **वेब इंटरफ़ेस खोलें**: इंस्पेक्टर एक ब्राउज़र विंडो खोलेगा जो आपके सर्वर की क्षमताओं को दिखाएगा।

3. **टूल्स का परीक्षण करें**: 
   - `get_greeting` टूल को विभिन्न नामों के साथ आज़माएं
   - `calculate_sum` टूल को विभिन्न संख्याओं के साथ परीक्षण करें
   - सर्वर मेटाडेटा देखने के लिए `get_server_info` टूल कॉल करें

4. **संचार की निगरानी करें**: इंस्पेक्टर क्लाइंट और सर्वर के बीच आदान-प्रदान हो रहे JSON-RPC संदेश दिखाता है।

### आपको क्या देखना चाहिए

जब आपका सर्वर सही तरीके से शुरू होता है, तो आपको निम्नलिखित दिखाई देगा:
- इंस्पेक्टर में सर्वर क्षमताएं सूचीबद्ध
- परीक्षण के लिए उपलब्ध टूल्स
- सफल JSON-RPC संदेश आदान-प्रदान
- इंटरफ़ेस में टूल प्रतिक्रियाएँ प्रदर्शित

### आम समस्याएं और समाधान

**सर्वर शुरू नहीं हो रहा:**
- सुनिश्चित करें कि सभी निर्भरताएं स्थापित हैं: `pip install mcp`
- पायथन सिंटैक्स और इंडेंटेशन जांचें
- कंसोल में त्रुटि संदेशों को देखें

**टूल्स दिखाई नहीं दे रहे:**
- सुनिश्चित करें कि `@server.tool()` डेकोरेटर्स मौजूद हैं
- जांचें कि टूल फ़ंक्शन `main()` से पहले परिभाषित हैं
- सर्वर सही ढंग से कॉन्फ़िगर किया गया है यह जांचें

**कनेक्शन समस्याएं:**
- सुनिश्चित करें कि सर्वर stdio ट्रांसपोर्ट का सही उपयोग कर रहा है
- जांचें कि कोई अन्य प्रक्रिया बाधा नहीं डाल रही
- इंस्पेक्टर कमांड सिंटैक्स की पुष्टि करें

## असाइनमेंट

अपने सर्वर को अधिक क्षमताओं के साथ बनाने की कोशिश करें। उदाहरण के लिए, एक टूल जोड़ें जो किसी API को कॉल करता हो, देखें [this page](https://api.chucknorris.io/). आप तय करें कि सर्वर कैसा दिखना चाहिए। आनंद लें :)
## समाधान

[Solution](./solution/README.md) यहाँ एक संभव समाधान है जिसमें कार्यशील कोड है।

## मुख्य बिंदु

इस चैप्टर के मुख्य बिंदु निम्नलिखित हैं:

- stdio ट्रांसपोर्ट स्थानीय MCP सर्वरों के लिए अनुशंसित तरीका है।
- stdio ट्रांसपोर्ट MCP सर्वरों और क्लाइंट्स के बीच स्टैंडर्ड इनपुट और आउटपुट स्ट्रीम्स के माध्यम से सहज संचार की अनुमति देता है।
- आप सीधे stdio सर्वरों का उपयोग करने के लिए Inspector और Visual Studio Code दोनों का उपयोग कर सकते हैं, जिससे डिबगिंग और एकीकरण सरल हो जाता है।

## नमूने 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## अतिरिक्त संसाधन

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## आगे क्या है

## अगले कदम

अब जब आप stdio ट्रांसपोर्ट के साथ MCP सर्वर बनाना सीख चुके हैं, तो आप और उन्नत विषयों का अन्वेषण कर सकते हैं:

- **अगला**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - दूरस्थ सर्वरों के लिए समर्थित अन्य ट्रांसपोर्ट तंत्र के बारे में जानें
- **उन्नत**: [MCP Security Best Practices](../../02-Security/README.md) - अपने MCP सर्वरों में सुरक्षा लागू करें
- **प्रोडक्शन**: [Deployment Strategies](../09-deployment/README.md) - उत्पादन उपयोग के लिए अपने सर्वरों को तैनात करें

## अतिरिक्त संसाधन

- [MCP Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - वर्तमान विनिर्देशन
- [MCP SDK Documentation](https://github.com/modelcontextprotocol/sdk) - सभी भाषाओं के लिए SDK संदर्भ
- [Community Examples](../../06-CommunityContributions/README.md) - समुदाय से अधिक सर्वर उदाहरण

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->