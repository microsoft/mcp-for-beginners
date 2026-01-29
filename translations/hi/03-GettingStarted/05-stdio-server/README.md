# MCP सर्वर stdio ट्रांसपोर्ट के साथ

> **⚠️ महत्वपूर्ण अपडेट**: MCP स्पेसिफिकेशन 2025-06-18 के अनुसार, स्टैंडअलोन SSE (Server-Sent Events) ट्रांसपोर्ट को **डिप्रिकेट** कर दिया गया है और इसे "Streamable HTTP" ट्रांसपोर्ट से बदल दिया गया है। वर्तमान MCP स्पेसिफिकेशन दो मुख्य ट्रांसपोर्ट मैकेनिज़्म को परिभाषित करता है:
> 1. **stdio** - स्टैंडर्ड इनपुट/आउटपुट (स्थानीय सर्वरों के लिए अनुशंसित)
> 2. **Streamable HTTP** - रिमोट सर्वरों के लिए जो आंतरिक रूप से SSE का उपयोग कर सकते हैं
>
> यह पाठ stdio ट्रांसपोर्ट पर केंद्रित है, जो अधिकांश MCP सर्वर इम्प्लीमेंटेशन के लिए अनुशंसित तरीका है।

stdio ट्रांसपोर्ट MCP सर्वरों को क्लाइंट्स के साथ स्टैंडर्ड इनपुट और आउटपुट स्ट्रीम्स के माध्यम से संवाद करने की अनुमति देता है। यह वर्तमान MCP स्पेसिफिकेशन में सबसे सामान्य और अनुशंसित ट्रांसपोर्ट मैकेनिज़्म है, जो MCP सर्वरों को विभिन्न क्लाइंट एप्लिकेशन के साथ आसानी से एकीकृत करने का एक सरल और कुशल तरीका प्रदान करता है।

## अवलोकन

यह पाठ stdio ट्रांसपोर्ट का उपयोग करके MCP सर्वर बनाने और उपयोग करने के तरीके को कवर करता है।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप:

- stdio ट्रांसपोर्ट का उपयोग करके MCP सर्वर बना सकेंगे।
- MCP सर्वर को Inspector का उपयोग करके डिबग कर सकेंगे।
- Visual Studio Code का उपयोग करके MCP सर्वर का उपभोग कर सकेंगे।
- वर्तमान MCP ट्रांसपोर्ट मैकेनिज़्म को समझ सकेंगे और जान सकेंगे कि stdio क्यों अनुशंसित है।

## stdio ट्रांसपोर्ट - यह कैसे काम करता है

stdio ट्रांसपोर्ट वर्तमान MCP स्पेसिफिकेशन (2025-06-18) में समर्थित दो ट्रांसपोर्ट प्रकारों में से एक है। यह इस प्रकार काम करता है:

- **सरल संवाद**: सर्वर स्टैंडर्ड इनपुट (`stdin`) से JSON-RPC संदेश पढ़ता है और स्टैंडर्ड आउटपुट (`stdout`) पर संदेश भेजता है।
- **प्रोसेस-आधारित**: क्लाइंट MCP सर्वर को एक सबप्रोसेस के रूप में लॉन्च करता है।
- **संदेश प्रारूप**: संदेश व्यक्तिगत JSON-RPC अनुरोध, सूचनाएं, या प्रतिक्रियाएं होते हैं, जो नई लाइनों द्वारा सीमांकित होते हैं।
- **लॉगिंग**: सर्वर लॉगिंग उद्देश्यों के लिए स्टैंडर्ड एरर (`stderr`) पर UTF-8 स्ट्रिंग्स लिख सकता है।

### मुख्य आवश्यकताएं:
- संदेश नई लाइनों द्वारा सीमांकित होने चाहिए और उनमें एम्बेडेड नई लाइनें नहीं होनी चाहिए।
- सर्वर को `stdout` पर ऐसा कुछ भी नहीं लिखना चाहिए जो वैध MCP संदेश न हो।
- क्लाइंट को सर्वर के `stdin` पर ऐसा कुछ भी नहीं लिखना चाहिए जो वैध MCP संदेश न हो।

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

उपरोक्त कोड में:

- हम MCP SDK से `Server` क्लास और `StdioServerTransport` को इम्पोर्ट करते हैं।
- हम बेसिक कॉन्फ़िगरेशन और क्षमताओं के साथ एक सर्वर इंस्टेंस बनाते हैं।

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

उपरोक्त कोड में:

- हम MCP SDK का उपयोग करके एक सर्वर इंस्टेंस बनाते हैं।
- डेकोरेटर्स का उपयोग करके टूल्स परिभाषित करते हैं।
- stdio_server कॉन्टेक्स्ट मैनेजर का उपयोग करके ट्रांसपोर्ट को हैंडल करते हैं।

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

SSE से stdio सर्वरों का मुख्य अंतर यह है कि:

- वे वेब सर्वर सेटअप या HTTP एंडपॉइंट्स की आवश्यकता नहीं रखते।
- क्लाइंट द्वारा सबप्रोसेस के रूप में लॉन्च किए जाते हैं।
- stdin/stdout स्ट्रीम्स के माध्यम से संवाद करते हैं।
- इन्हें लागू करना और डिबग करना आसान है।

## अभ्यास: stdio सर्वर बनाना

हमारे सर्वर को बनाने के लिए, हमें दो बातों का ध्यान रखना होगा:

- हमें कनेक्शन और संदेशों के लिए एंडपॉइंट्स को एक्सपोज़ करने के लिए एक वेब सर्वर का उपयोग करना होगा।

## लैब: एक सरल MCP stdio सर्वर बनाना

इस लैब में, हम अनुशंसित stdio ट्रांसपोर्ट का उपयोग करके एक सरल MCP सर्वर बनाएंगे। यह सर्वर ऐसे टूल्स को एक्सपोज़ करेगा जिन्हें क्लाइंट्स स्टैंडर्ड मॉडल कॉन्टेक्स्ट प्रोटोकॉल का उपयोग करके कॉल कर सकते हैं।

### आवश्यकताएं

- Python 3.8 या बाद का संस्करण
- MCP Python SDK: `pip install mcp`
- असिंक्रोनस प्रोग्रामिंग की बुनियादी समझ

आइए अपना पहला MCP stdio सर्वर बनाना शुरू करें:

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

## डिप्रिकेटेड SSE दृष्टिकोण से मुख्य अंतर

**Stdio ट्रांसपोर्ट (वर्तमान मानक):**
- सरल सबप्रोसेस मॉडल - क्लाइंट सर्वर को चाइल्ड प्रोसेस के रूप में लॉन्च करता है।
- JSON-RPC संदेशों का उपयोग करके stdin/stdout के माध्यम से संवाद।
- HTTP सर्वर सेटअप की आवश्यकता नहीं।
- बेहतर प्रदर्शन और सुरक्षा।
- डिबगिंग और विकास में आसानी।

**SSE ट्रांसपोर्ट (MCP 2025-06-18 से डिप्रिकेट):**
- HTTP सर्वर के साथ SSE एंडपॉइंट्स की आवश्यकता।
- वेब सर्वर इंफ्रास्ट्रक्चर के साथ अधिक जटिल सेटअप।
- HTTP एंडपॉइंट्स के लिए अतिरिक्त सुरक्षा विचार।
- अब वेब-आधारित परिदृश्यों के लिए Streamable HTTP द्वारा प्रतिस्थापित।

### stdio ट्रांसपोर्ट के साथ सर्वर बनाना

stdio सर्वर बनाने के लिए, हमें निम्नलिखित करना होगा:

1. **आवश्यक लाइब्रेरीज़ इम्पोर्ट करें** - हमें MCP सर्वर घटकों और stdio ट्रांसपोर्ट की आवश्यकता होगी।
2. **सर्वर इंस्टेंस बनाएं** - सर्वर को उसकी क्षमताओं के साथ परिभाषित करें।
3. **टूल्स परिभाषित करें** - वह कार्यक्षमता जोड़ें जिसे हम एक्सपोज़ करना चाहते हैं।
4. **ट्रांसपोर्ट सेट करें** - stdio संवाद को कॉन्फ़िगर करें।
5. **सर्वर चलाएं** - सर्वर शुरू करें और संदेशों को हैंडल करें।

आइए इसे चरण दर चरण बनाएं:

### चरण 1: एक बेसिक stdio सर्वर बनाएं

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

### चरण 2: अधिक टूल्स जोड़ें

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

सर्वर शुरू हो जाएगा और stdin से इनपुट की प्रतीक्षा करेगा। यह stdio ट्रांसपोर्ट पर JSON-RPC संदेशों का उपयोग करके संवाद करता है।

### चरण 4: Inspector के साथ परीक्षण

आप अपने सर्वर का परीक्षण MCP Inspector का उपयोग करके कर सकते हैं:

1. Inspector इंस्टॉल करें: `npx @modelcontextprotocol/inspector`
2. Inspector चलाएं और इसे अपने सर्वर की ओर इंगित करें।
3. आपने जो टूल्स बनाए हैं, उनका परीक्षण करें।

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## अपने stdio सर्वर को डिबग करना

### MCP Inspector का उपयोग करना

MCP Inspector MCP सर्वरों को डिबग और परीक्षण करने के लिए एक मूल्यवान उपकरण है। इसका उपयोग stdio सर्वर के साथ इस प्रकार करें:

1. **Inspector इंस्टॉल करें**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector चलाएं**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **अपने सर्वर का परीक्षण करें**: Inspector एक वेब इंटरफ़ेस प्रदान करता है जहां आप:
   - सर्वर क्षमताओं को देख सकते हैं।
   - विभिन्न पैरामीटर के साथ टूल्स का परीक्षण कर सकते हैं।
   - JSON-RPC संदेशों की निगरानी कर सकते हैं।
   - कनेक्शन समस्याओं को डिबग कर सकते हैं।

### VS Code का उपयोग करना

आप अपने MCP सर्वर को सीधे VS Code में भी डिबग कर सकते हैं:

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

2. अपने सर्वर कोड में ब्रेकपॉइंट सेट करें।
3. डिबगर चलाएं और Inspector के साथ परीक्षण करें।

### सामान्य डिबगिंग टिप्स

- लॉगिंग के लिए `stderr` का उपयोग करें - `stdout` पर कभी न लिखें क्योंकि यह MCP संदेशों के लिए आरक्षित है।
- सुनिश्चित करें कि सभी JSON-RPC संदेश नई लाइनों द्वारा सीमांकित हैं।
- पहले सरल टूल्स के साथ परीक्षण करें, फिर जटिल कार्यक्षमता जोड़ें।
- संदेश प्रारूपों को सत्यापित करने के लिए Inspector का उपयोग करें।

## अपने stdio सर्वर को VS Code में उपयोग करना

एक बार जब आपने अपना MCP stdio सर्वर बना लिया, तो आप इसे VS Code के साथ एकीकृत कर सकते हैं ताकि इसे Claude या अन्य MCP-संगत क्लाइंट्स के साथ उपयोग किया जा सके।

### कॉन्फ़िगरेशन

1. **एक MCP कॉन्फ़िगरेशन फ़ाइल बनाएं** `%APPDATA%\Claude\claude_desktop_config.json` (Windows) या `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) पर:

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

2. **Claude को पुनः प्रारंभ करें**: नए सर्वर कॉन्फ़िगरेशन को लोड करने के लिए Claude को बंद करें और पुनः खोलें।

3. **कनेक्शन का परीक्षण करें**: Claude के साथ बातचीत शुरू करें और अपने सर्वर के टूल्स का उपयोग करने का प्रयास करें:
   - "क्या आप ग्रीटिंग टूल का उपयोग करके मुझे अभिवादन कर सकते हैं?"
   - "15 और 27 का योग निकालें।"
   - "सर्वर की जानकारी क्या है?"

### TypeScript stdio सर्वर उदाहरण

यहां एक पूरा TypeScript उदाहरण संदर्भ के लिए दिया गया है:

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

इस अद्यतन पाठ में, आपने सीखा कि:

- वर्तमान **stdio ट्रांसपोर्ट** (अनुशंसित तरीका) का उपयोग करके MCP सर्वर कैसे बनाएं।
- SSE ट्रांसपोर्ट को stdio और Streamable HTTP के पक्ष में क्यों डिप्रिकेट किया गया।
- ऐसे टूल्स बनाएं जिन्हें MCP क्लाइंट्स द्वारा कॉल किया जा सके।
- MCP Inspector का उपयोग करके अपने सर्वर को डिबग करें।
- अपने stdio सर्वर को VS Code और Claude के साथ एकीकृत करें।

stdio ट्रांसपोर्ट डिप्रिकेटेड SSE दृष्टिकोण की तुलना में MCP सर्वर बनाने का एक सरल, अधिक सुरक्षित, और अधिक प्रदर्शनकारी तरीका प्रदान करता है। यह 2025-06-18 स्पेसिफिकेशन के अनुसार अधिकांश MCP सर्वर इम्प्लीमेंटेशन के लिए अनुशंसित ट्रांसपोर्ट है।

---

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता सुनिश्चित करने का प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।