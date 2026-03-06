# stdio ट्रांसपोर्ट के साथ MCP सर्वर

> **⚠️ महत्वपूर्ण अपडेट**: MCP विनिर्देश 2025-06-18 के अनुसार, स्टैंडअलोन SSE (सर्वर-सेंट ईवेंट्स) ट्रांसपोर्ट को **अप्रचलित** घोषित कर दिया गया है और इसे "स्ट्रीम करने योग्य HTTP" ट्रांसपोर्ट द्वारा प्रतिस्थापित किया गया है। वर्तमान MCP विनिर्देश दो प्रमुख ट्रांसपोर्ट मैकेनिज्म को परिभाषित करता है:
> 1. **stdio** - स्टैंडर्ड इनपुट/आउटपुट (स्थानीय सर्वरों के लिए अनुशंसित)
> 2. **Streamable HTTP** - रिमोट सर्वरों के लिए जो आंतरिक रूप से SSE का उपयोग कर सकते हैं
>
> इस पाठ को अपडेट करके **stdio ट्रांसपोर्ट** पर केंद्रित किया गया है, जो अधिकांश MCP सर्वर कार्यान्वयनों के लिए अनुशंसित तरीका है।

stdio ट्रांसपोर्ट MCP सर्वरों को क्लाइंट्स के साथ मानक इनपुट और आउटपुट स्ट्रीम्स के माध्यम से संवाद करने की अनुमति देता है। यह वर्तमान MCP विनिर्देश में सबसे सामान्य रूप से उपयोग किया जाने वाला और अनुशंसित ट्रांसपोर्ट मैकेनिज्म है, जो विभिन्न क्लाइंट एप्लिकेशन के साथ आसानी से एकीकृत किए जा सकने वाले MCP सर्वर बनाने का एक सरल और प्रभावी तरीका प्रदान करता है।

## अवलोकन

यह पाठ stdio ट्रांसपोर्ट का उपयोग करके MCP सर्वरों का निर्माण और उपभोग कैसे करें के बारे में है।

## सीखने के उद्देश्य

इस पाठ के अंत तक, आप सक्षम होंगे:

- stdio ट्रांसपोर्ट का उपयोग करके MCP सर्वर बनाना।
- Inspector का उपयोग करके MCP सर्वर डिबग करना।
- Visual Studio Code का उपयोग करके MCP सर्वर उपभोग करना।
- वर्तमान MCP ट्रांसपोर्ट मैकेनिज्म को समझना और क्यों stdio अनुशंसित है।

## stdio ट्रांसपोर्ट - यह कैसे काम करता है

stdio ट्रांसपोर्ट वर्तमान MCP विनिर्देश (2025-06-18) में समर्थित दो ट्रांसपोर्ट प्रकारों में से एक है। यह इस प्रकार काम करता है:

- **सरल संचार**: सर्वर मानक इनपुट (`stdin`) से JSON-RPC संदेश पढ़ता है और मानक आउटपुट (`stdout`) पर संदेश भेजता है।
- **प्रक्रिया आधारित**: क्लाइंट MCP सर्वर को एक उपप्रक्रिया के रूप में लॉन्च करता है।
- **संदेश प्रारूप**: संदेश व्यक्तिगत JSON-RPC अनुरोध, सूचनाएं, या प्रतिक्रियाएं होते हैं, जो नई लाइनों से सीमाबद्ध होते हैं।
- **लॉगिंग**: सर्वर लॉगिंग उद्देश्यों के लिए मानक त्रुटि (`stderr`) में UTF-8 स्ट्रिंग्स लिख सकता है।

### मुख्य आवश्यकताएँ:
- संदेश नई लाइनों से सीमाबद्ध होने चाहिए और उनमें अंदरूनी नई लाइनें नहीं होनी चाहिए
- सर्वर को `stdout` में केवल मान्य MCP संदेश ही लिखना चाहिए
- क्लाइंट को सर्वर के `stdin` में केवल मान्य MCP संदेश ही लिखना चाहिए

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

पिछले कोड में:

- हम MCP SDK से `Server` क्लास और `StdioServerTransport` आयात करते हैं
- हम बेसिक कॉन्फ़िगरेशन और क्षमताओं के साथ एक सर्वर उदाहरण बनाते हैं

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

- MCP SDK का उपयोग करके सर्वर उदाहरण बनाया
- डेकोरेटर का उपयोग करके टूल्स परिभाषित किए
- ट्रांसपोर्ट को संभालने के लिए stdio_server संदर्भ प्रबंधक का उपयोग किया

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

SSE से मुख्य अंतर है कि stdio सर्वर:

- वेब सर्वर सेटअप या HTTP एंडपॉइंट की आवश्यकता नहीं है
- क्लाइंट द्वारा उपप्रक्रिया के रूप में लॉन्च किए जाते हैं
- stdin/stdout स्ट्रीम्स के माध्यम से संवाद करते हैं
- लागू करना और डिबग करना आसान है

## व्यायाम: stdio सर्वर बनाना

हमारा सर्वर बनाने के लिए, हमें दो बातों का ध्यान रखना होगा:

- हमें कनेक्शन और संदेशों के लिए एंडपॉइंट दिखाने के लिए वेब सर्वर का उपयोग करना होगा।

## प्रयोगशाला: एक सरल MCP stdio सर्वर बनाना

इस प्रयोगशाला में, हम अनुशंसित stdio ट्रांसपोर्ट का उपयोग करके एक सरल MCP सर्वर बनाएंगे। यह सर्वर वह टूल्स दिखाएगा जिन्हें क्लाइंट मानक Model Context Protocol का उपयोग करके कॉल कर सकते हैं।

### पूर्वनियम

- Python 3.8 या उससे अधिक
- MCP Python SDK: `pip install mcp`
- असिंक्रोनस प्रोग्रामिंग की बुनियादी समझ

आइए अपना पहला MCP stdio सर्वर बनाना शुरू करें:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# लॉगिंग कॉन्फ़िगर करें
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# सर्वर बनाएँ
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

## अप्रचलित SSE दृष्टिकोण से मुख्य भेद

**Stdio ट्रांसपोर्ट (वर्तमान मानक):**
- सरल उपप्रक्रिया मॉडल - क्लाइंट सर्वर को चाइल्ड प्रक्रिया के रूप में लॉन्च करता है
- JSON-RPC संदेशों के साथ stdin/stdout के माध्यम से संचार
- HTTP सर्वर सेटअप की आवश्यकता नहीं
- बेहतर प्रदर्शन और सुरक्षा
- डिबगिंग और विकास आसान

**SSE ट्रांसपोर्ट (MCP 2025-06-18 के अनुसार अप्रचलित):**
- HTTP सर्वर आवश्यक था जिसमें SSE एंडपॉइंट थे
- वेब सर्वर इंफ्रास्ट्रक्चर के साथ अधिक जटिल सेटअप
- HTTP एंडपॉइंट के लिए अतिरिक्त सुरक्षा विचार
- वेब आधारित परिदृश्यों के लिए अब Streamable HTTP से प्रतिस्थापित

### stdio ट्रांसपोर्ट के साथ सर्वर बनाना

अपना stdio सर्वर बनाने के लिए, हमें:

1. **आवश्यक पुस्तकालय आयात करना** - हमें MCP सर्वर घटक और stdio ट्रांसपोर्ट चाहिए
2. **सर्वर उदाहरण बनाना** - क्षमताओं के साथ सर्वर परिभाषित करें
3. **टूल्स परिभाषित करना** - वह कार्यक्षमता जोड़ें जिसे हम प्रदर्शित करना चाहते हैं
4. **ट्रांसपोर्ट सेटअप करना** - stdio संचार कॉन्फ़िगर करें
5. **सर्वर चलाना** - सर्वर शुरू करें और संदेशों को संभालें

आइए इसे चरण दर चरण बनाएं:

### चरण 1: एक मूल stdio सर्वर बनाएं

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# लॉगिंग कॉन्फ़िगर करें
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# सर्वर बनाएं
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

कोड को `server.py` के रूप में सहेजें और कमांड लाइन से चलाएं:

```bash
python server.py
```

सर्वर शुरू होगा और stdin से इनपुट का इंतजार करेगा। यह stdio ट्रांसपोर्ट के माध्यम से JSON-RPC संदेशों का उपयोग करके संवाद करता है।

### चरण 4: Inspector के साथ परीक्षण

आप MCP Inspector का उपयोग करके अपने सर्वर का परीक्षण कर सकते हैं:

1. Inspector इंस्टॉल करें: `npx @modelcontextprotocol/inspector`
2. Inspector चलाएं और इसे अपने सर्वर से कनेक्ट करें
3. आपने जो टूल बनाए हैं उनका परीक्षण करें

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## अपने stdio सर्वर को डिबग करना

### MCP Inspector का उपयोग

MCP Inspector MCP सर्वरों का डिबग और परीक्षण करने के लिए एक महत्वपूर्ण टूल है। इसे अपने stdio सर्वर के साथ उपयोग करने का तरीका इस प्रकार है:

1. **Inspector इंस्टॉल करें**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Inspector चलाएं**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **सर्वर का परीक्षण करें**: Inspector एक वेब इंटरफेस प्रदान करता है जहाँ आप:
   - सर्वर क्षमताएं देख सकते हैं
   - विभिन्न पैरामीटर के साथ टूल टेस्ट कर सकते हैं
   - JSON-RPC संदेशों की निगरानी कर सकते हैं
   - कनेक्शन समस्याओं को डिबग कर सकते हैं

### VS Code का उपयोग

आप अपने MCP सर्वर को सीधे VS Code में भी डिबग कर सकते हैं:

1. `.vscode/launch.json` में लॉन्च विन्यास बनाएं:
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

- लॉगिंग के लिए `stderr` का उपयोग करें - `stdout` में कभी कुछ न लिखें क्योंकि यह MCP संदेशों के लिए आरक्षित है
- सभी JSON-RPC संदेश नई लाइन से सीमाबद्ध होने चाहिए
- पहले सरल टूल्स के साथ परीक्षण करें, फिर जटिल कार्यक्षमता जोड़ें
- संदेश प्रारूप सत्यापित करने के लिए Inspector का उपयोग करें

## VS Code में अपने stdio सर्वर का उपयोग करना

एक बार जब आप अपना MCP stdio सर्वर बना लेते हैं, तो आप इसे VS Code के साथ एकीकृत कर सकते हैं ताकि इसे Claude या अन्य MCP-समर्थित क्लाइंट्स के साथ उपयोग किया जा सके।

### विन्यास

1. %APPDATA%\Claude\claude_desktop_config.json (Windows) या ~/Library/Application Support/Claude/claude_desktop_config.json (Mac) पर एक MCP विन्यास फ़ाइल बनाएँ:

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

2. **Claude पुनः प्रारंभ करें**: Claude को बंद करें और फिर से खोलें ताकि नए सर्वर कॉन्फ़िगरेशन को लोड किया जा सके।

3. **कनेक्शन का परीक्षण करें**: Claude के साथ बातचीत शुरू करें और अपने सर्वर के टूल्स का उपयोग करके देखिए:
   - "क्या आप ग्रीटिंग टूल का उपयोग करके मुझे अभिवादन कर सकते हैं?"
   - "15 और 27 का योग कैलकुलेट करें"
   - "सर्वर की जानकारी क्या है?"

### TypeScript stdio सर्वर उदाहरण

संदर्भ के लिए यहां पूर्ण TypeScript उदाहरण है:

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
- क्यों SSE ट्रांसपोर्ट को stdio और Streamable HTTP के पक्ष में अप्रचलित किया गया
- MCP क्लाइंट्स द्वारा कॉल किए जा सकने वाले टूल बनाना
- MCP Inspector का उपयोग करके अपने सर्वर का डिबग करना
- अपने stdio सर्वर को VS Code और Claude के साथ एकीकृत करना

stdio ट्रांसपोर्ट अप्रचलित SSE दृष्टिकोण की तुलना में MCP सर्वरों को बनाना सरल, अधिक सुरक्षित, और अधिक प्रदर्शनक्षम बनाता है। यह 2025-06-18 विनिर्देश के अनुसार अधिकांश MCP सर्वर कार्यान्वयनों के लिए अनुशंसित ट्रांसपोर्ट है।

### .NET

1. पहले कुछ टूल बनाएं, इसके लिए हम *Tools.cs* नामक एक फ़ाइल बनाएंगे जिसमें निम्नलिखित सामग्री होगी:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## व्यायाम: अपने stdio सर्वर का परीक्षण

अब जब आपने अपना stdio सर्वर बना लिया है, तो चलिए इसे परीक्षण करते हैं कि यह सही ढंग से काम करता है या नहीं।

### पूर्वनियम

1. सुनिश्चित करें कि आपके पास MCP Inspector इंस्टॉल है:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. आपका सर्वर कोड सहेजा हुआ होना चाहिए (जैसे `server.py`)

### Inspector के साथ परीक्षण

1. **अपने सर्वर के साथ Inspector शुरू करें**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **वेब इंटरफेस खोलें**: Inspector ब्राउज़र विंडो खोलेगा जो आपके सर्वर की क्षमताएं दिखाएगा।

3. **टूल्स का परीक्षण करें**: 
   - विभिन्न नामों के साथ `get_greeting` टूल आजमाएं
   - विभिन्न संख्याओं के साथ `calculate_sum` टूल का परीक्षण करें
   - सर्वर मेटाडेटा देखने के लिए `get_server_info` टूल कॉल करें

4. **संचार की निगरानी करें**: Inspector JSON-RPC संदेशों को दिखाता है जो क्लाइंट और सर्वर के बीच आदान-प्रदान हो रहे हैं।

### आपको क्या देखना चाहिए

जब आपका सर्वर सही ढंग से शुरू होता है, तो आपको दिखना चाहिए:
- Inspector में सर्वर क्षमताएं सूचीबद्ध
- परीक्षण के लिए उपलब्ध टूल्स
- सफल JSON-RPC संदेश आदान-प्रदान
- इंटरफेस में टूल प्रतिक्रियाएं

### सामान्य समस्याएं और समाधान

**सर्वर शुरू नहीं होता:**
- सुनिश्चित करें कि सभी निर्भरताएं स्थापित हैं: `pip install mcp`
- Python सिंटैक्स और इंडेंटेशन जांचें
- कंसोल में त्रुटि संदेश देखें

**टूल्स दिखाई नहीं देते:**
- सुनिश्चित करें कि `@server.tool()` डेकोरेटर मौजूद हैं
- जांचें कि टूल फ़ंक्शन `main()` से पहले परिभाषित हैं
- सुनिश्चित करें कि सर्वर ठीक से कॉन्फ़िगर किया गया है

**कनेक्शन समस्याएं:**
- सुनिश्चित करें कि सर्वर stdio ट्रांसपोर्ट का सही उपयोग कर रहा है
- जांचें कि कोई अन्य प्रक्रिया हस्तक्षेप नहीं कर रही
- Inspector कमांड सिंटैक्स सत्यापित करें

## असाइनमेंट

अपने सर्वर की और क्षमताएं बनाना आज़माएँ। उदाहरण के लिए एक ऐसा टूल जोड़ें जो API कॉल करता हो, आप [इस पृष्ठ](https://api.chucknorris.io/) को देख सकते हैं। आप तय करें कि सर्वर कैसा दिखना चाहिए। मज़े करें :)

## हल

[Solution](./solution/README.md) यहाँ एक संभव हल है जिसमें कार्यरत कोड है।

## मुख्य बातें

इस अध्याय से मुख्य बातें निम्नलिखित हैं:

- stdio ट्रांसपोर्ट स्थानीय MCP सर्वरों के लिए अनुशंसित मैकेनिज्म है।
- stdio ट्रांसपोर्ट मानक इनपुट और आउटपुट स्ट्रीम्स का उपयोग करके MCP सर्वरों और क्लाइंट्स के बीच निर्बाध संचार की अनुमति देता है।
- आप Inspector और Visual Studio Code दोनों का उपयोग करके stdio सर्वरों को सीधे उपभोग कर सकते हैं, जिससे डिबगिंग और एकीकरण सरल हो जाता है।

## नमूने 

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python) 

## अतिरिक्त संसाधन

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## अगला क्या है

## अगले कदम

अब जब आपने stdio ट्रांसपोर्ट के साथ MCP सर्वर बनाना सीख लिया है, तो आप अधिक उन्नत विषयों का अन्वेषण कर सकते हैं:

- **अगला**: [MCP के साथ HTTP स्ट्रीमिंग (Streamable HTTP)](../06-http-streaming/README.md) - रिमोट सर्वरों के लिए अन्य समर्थित ट्रांसपोर्ट मैकेनिज्म के बारे में जानें
- **उन्नत**: [MCP सुरक्षा सर्वश्रेष्ठ प्रथाएँ](../../02-Security/README.md) - अपने MCP सर्वरों में सुरक्षा लागू करें
- **प्रोडक्शन**: [तैनाती रणनीतियाँ](../09-deployment/README.md) - अपने सर्वरों को उत्पादन उपयोग के लिए तैनात करें

## अतिरिक्त संसाधन

- [MCP विनिर्देश 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - आधिकारिक विनिर्देश
- [MCP SDK दस्तावेज़](https://github.com/modelcontextprotocol/sdk) - सभी भाषाओं के लिए SDK संदर्भ
- [समुदाय उदाहरण](../../06-CommunityContributions/README.md) - समुदाय से अधिक सर्वर उदाहरण

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल भाषा में दस्तावेज़ को अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->