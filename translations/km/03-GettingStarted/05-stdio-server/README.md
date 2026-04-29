# MCP ម៉ាស៊ីនមេជាមួយផ្លូវសារទំនាក់ទំនង stdio

> **⚠️ ព័ត៌មានចាស់សំខាន់**: កាលពី MCP Specification 2025-06-18, ផ្លូវសារទំនាក់ទំនង SSE (Server-Sent Events) ដាច់ដោយឡែកត្រូវបាន **យកចេញ** ហើយជំនួសដោយ ផ្លូវសារទំនាក់ទំនង "Streamable HTTP"។ បញ្ជាក់ MCP ប្រក្រតីបច្ចុប្បន្នកំណត់ពីរប្រភេទផ្លូវសារ​សំខាន់ៗ៖
> ១. **stdio** - ព្រមទាំងបញ្ចូល/បញ្ចេញស្តង់ដារ (បានផ្តល់អនុសាសន៍សម្រាប់ម៉ាស៊ីនមេក្នុងតំបន់)
> ២. **Streamable HTTP** - សម្រាប់ម៉ាស៊ីនមេរំកិលដែលអាចប្រើ SSE ក្នុងខាងក្នុង
>
> មេរៀននេះត្រូវបានធ្វើបច្ចុប្បន្នភាពដើម្បីផ្តោតលើ **stdio transport** ដែលជា វិធីសាស្ត្រផ្តល់អនុសាសន៍សម្រាប់ការអនុវត្តម៉ាស៊ីនមេ MCP ច្រើន។

ផ្លូវសារទំនាក់ទំនង stdio អនុញ្ញាតឲ្យម៉ាស៊ីនមេ MCP និយាយគ្នាជាមួយឧបករណ៍អតិថិជនតាមរយៈច្រាសបញ្ចូល និងច្រាសបញ្ចេញស្តង់ដារ។ នេះគឺជាមាស៊ីនផ្លូវសារទំនាក់ទំនងដែលគេស្គាល់ និងផ្តល់អនុសាសន៍ច្រើនបំផុត​នៅក្នុង MCP Specification បច្ចុប្បន្ន ដែលផ្តល់វិធីសាស្ត្រងាយ និងមានប្រសិទ្ធភាពក្នុងការជួបប្រទៈម៉ាស៊ីនមេ MCP ដែលអាចផ្សំចូលគ្នាក្នុងកម្មវិធីអតិថិជនគ្មានបញ្ហា។

## ទិដ្ឋភាពទូទៅ

មេរៀននេះគ្របដណ្តប់ពីរបៀបបង្កើត និងប្រើប្រាស់ម៉ាស៊ីនមេ MCP ដោយប្រើផ្លូវសារទំនាក់ទំនង stdio។

## គោលបំណងការសិក្សា

បន្ទាប់ពីបញ្ចប់មេរៀននេះ អ្នកនឹងអាច៖

- បង្កើតម៉ាស៊ីនមេ MCP ដោយប្រើ stdio សម្រាប់ផ្លូវសារទំនាក់ទំនង។
- កែតម្រូវបញ្ហាម៉ាស៊ីនមេ MCP ដោយប្រើ Inspector។
- ប្រើម៉ាស៊ីនមេ MCP ដោយប្រើ Visual Studio Code។
- យល់ដឹងពីផ្លូវសារបច្ចុប្បន្ន MCP និងមូលហេតុដែល stdio ត្រូវបានផ្តល់អនុសាសន៍។

## ផ្លូវសារទំនាក់ទំនង stdio - វាធ្វើការយ៉ាងដូចម្តេច

ផ្លូវសារទំនាក់ទំនង stdio គឺជាតែប្រភេទផ្លូវសារមួយក្នុងពីរប្រភេទដែលគាំទ្រនៅក្នុង MCP specification បច្ចុប្បន្ន (2025-06-18)។ វាធ្វើការយ៉ាងដូចខាងក្រោម៖

- **ការទំនាក់ទំនងសាមញ្ញ**៖ ម៉ាស៊ីនមេអានសារប្រភេទ JSON-RPC ពីបញ្ចូលស្តង់ដារ (`stdin`) ហើយផ្ញើសារទៅបញ្ចេញស្តង់ដារ (`stdout`)។
- **ផ្អែកលើដំណើរការ**៖ អតិថិជនចាប់ផ្តើមម៉ាស៊ីនមេ MCP ជាដំណើរការដោះស្រាយជាជើងក្រោម។
- **ទ្រង់ទ្រាយសារ**៖ សារជាការស្នើសុំ JSON-RPC មួយៗ ព័ត៌មានជូនដំណឹង ឬចម្លើយ ដែលបំបែកដោយ ថ្មីជួរ។
- **ការចុះបញ្ជី**៖ ម៉ាស៊ីនមេអាចសរសេរស្រមោល UTF-8 ទៅកាន់កំហុសស្តង់ដារ (`stderr`) សម្រាប់គោលបំណងចុះបញ្ជី។

### តម្រូវការសំខាន់៖
- សារត្រូវតែបំបែកដោយថ្មីជួរនិងមិនអាចមានថ្មីជួរបន្ទាប់ក្នុងសារប្រភេទ JSON-RPC
- ម៉ាស៊ីនមេមិនត្រូវសរសេរអ្វីទៅ `stdout` ដែលពុំមែនសារពិត MCP
- អតិថិជនមិនត្រូវសរសេរអ្វីទៅ `stdin` របស់ម៉ាស៊ីនមេដែលមិនមែនសារពិត MCP

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

នៅក្នុងកូដខាងលើ៖

- យើងនាំចូល `Server` និង `StdioServerTransport` ពី MCP SDK
- បង្កើតម៉ាស៊ីនមេមួយជាមួយកំណត់រចនាសម្ព័ន្ធ និងសមត្ថភាពមូលដ្ឋាន
- បង្កើត `StdioServerTransport` មួយហើយភ្ជាប់ម៉ាស៊ីនមេទៅវា ឲ្យអាចនិយាយតាមផ្លូវ stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# បង្កើតឧបករណ៍ម៉ាស៊ីនមេ
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

នៅក្នុងកូដខាងលើ យើងបាន៖

- បង្កើតម៉ាស៊ីនមេមួយដោយប្រើ MCP SDK
- កំណត់ឧបករណ៍ដោយប្រើ decorators
- ប្រើបរិបទ stdio_server ដើម្បីគ្រប់គ្រងផ្លូវសារ

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

ភាពខុសគ្នាសំខាន់ពី SSE គឺ stdio servers:

- មិនតម្រូវការការរៀបចំម៉ាស៊ីនបម្រើវេបឬចំណុចចូល HTTP
- ត្រូវបានចាប់ផ្តើមជាដំណើរការដោះស្រាយដោយអតិថិជន
- ទំនាក់ទំនងតាមស្ទ្រីម stdin/stdout
- ងាយស្រួលក្នុងការអនុវត្តន៍ និងកែតម្រូវកំហុស

## អនុវត្តន៍៖ បង្កើតម៉ាស៊ីនមេ stdio

ដើម្បីបង្កើតម៉ាស៊ីនមេ យើងត្រូវកត់សម្គាល់រឿងពីរនេះ៖

- យើងត្រូវប្រើម៉ាស៊ីនបម្រើវេបដើម្បីបង្ហាញចំណុចចូលសម្រាប់ការតភ្ជាប់ និងសារ។

## 实验室៖ បង្កើតម៉ាស៊ីនមេ MCP stdio ងាយៗ

នៅក្នុងមេរៀននេះ យើងនឹងបង្កើតម៉ាស៊ីនមេ MCP ងាយៗ ដែលប្រើ stdio ផ្លូវសារទំនាក់ទំនងដែលបានផ្តល់អនុសាសន៍។ ម៉ាស៊ីនមេនេះ នឹងបង្ហាញឧបករណ៍ដែលអតិថិជនអាចហៅបាន ដោយប្រើ Model Context Protocol មូលដ្ឋាន។

### តម្រូវការមុន

- Python 3.8 ឬក្រោយជាងនេះ
- MCP Python SDK: `pip install mcp`
- យល់ដឹងពីកម្មវិធី async ជាមូលដ្ឋាន

ដោយយើងចាប់ផ្ដើមបង្កើតម៉ាស៊ីនមេ MCP stdio លើកដំបូង៖

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# កំណត់រចនាសម្ព័ន្ធការចុះបញ្ជី
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# បង្កើតម៉ាស៊ីនមេ
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
    # ប្រើការដឹកជញ្ជូន stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## ភាពខុសគ្នាសំខាន់ពីវិធី SSE ដែលបានយកចេញ

**ផ្លូវសារទំនាក់ទំនង Stdio (ស្តង់ដារបច្ចុប្បន្ន):**
- ម៉ូឌែលដំណើរការជាសំណុំរង - អតិថិជនចាប់ផ្តើមម៉ាស៊ីនមេជារង
- ទំនាក់ទំនងតាម stdin/stdout ប្រើសារប្រភេទ JSON-RPC
- មិនតម្រូវការរៀបចំម៉ាស៊ីនបម្រើ HTTP
- ប្រសិទ្ធិភាព និងសុវត្ថិភាពល្អជាង
- ងាយស្រួលក្នុងការកែតម្រូវកំហុស និងអភិវឌ្ឍន៍

**ផ្លូវសារទំនាក់ទំនង SSE (បានយកចេញពី MCP 2025-06-18):**
- តម្រូវម៉ាស៊ីនបម្រើ HTTP និងចំណុចចូល SSE
- រៀបចំស្មុគស្មាញជាមួយហេតុផលម៉ាស៊ីនបម្រើវេប
- ការពិចារណាសុវត្ថិភាពបន្ថែមសម្រាប់ចំណុចចូល HTTP
- ចំនួននេះត្រូវបានជំនួសដោយ Streamable HTTP សម្រាប់សถานการณ์វេប

### បង្កើតម៉ាស៊ីនមេដោយ stdio transport

ដើម្បីបង្កើតម៉ាស៊ីនមេ stdio, យើងត្រូវ:

១. **នាំចូលបណ្ណាល័យត្រូវការ** - ត្រូវការផ្នែកម៉ាស៊ីនមេ MCP និង stdio transport
២. **បង្កើតម៉ាស៊ីនមេ** - កំណត់ម៉ាស៊ីនមេជាមួយសមត្ថភាពរបស់វា
៣. **កំណត់ឧបករណ៍** - បន្ថែមមុខងារដែលយើងចង់បង្ហាញ
៤. **កំណត់ផ្លូវសារ** - កំណត់ stdio ដើម្បីប្រើទំនាក់ទំនង
៥. **រត់ម៉ាស៊ីនមេ** - ចាប់ផ្តើមម៉ាស៊ីនមេ និងដោះស្រាយសារ

យើងសាងសង់វាដោយជំហាន៖

### ជំហាន ១៖ បង្កើតម៉ាស៊ីនមេ stdio មូលដ្ឋាន

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# កំណត់ការចុះបញ្ជីភាពឡុក
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# បង្កើតម៉ាស៊ីនបម្រើ
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

### ជំហាន ២៖ បន្ថែមឧបករណ៍បន្ថែម

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

### ជំហាន ៣៖ រត់ម៉ាស៊ីនមេ

រក្សារកូដជា `server.py` ហើយរត់វាពីបញ្ជារបញ្ជា៖

```bash
python server.py
```

ម៉ាស៊ីនមេនឹងចាប់ផ្តើម និងរង់ចាំការបញ្ចូលពី stdin។ វានិយាយដោយប្រើសារប្រភេទ JSON-RPC លើផ្លូវ stdio។

### ជំហាន ៤៖ សាកល្បងជាមួយ Inspector

អ្នកអាចសាកល្បងម៉ាស៊ីនមេរបស់អ្នកដោយប្រើ MCP Inspector៖

១. ដំឡើង Inspector៖ `npx @modelcontextprotocol/inspector`
២. រត់ Inspector ហើយបញ្ជូនវាទៅម៉ាស៊ីនមេរបស់អ្នក
៣. សាកល្បងឧបករណ៍ដែលអ្នកបានបង្កើត

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## ការកែតម្រូវកំហុសម៉ាស៊ីនមេ stdio របស់អ្នក

### ប្រើ MCP Inspector

MCP Inspector ជាឧបករណ៍មានតម្លៃសម្រាប់កែតម្រូវកំហុស និងសាកល្បងម៉ាស៊ីនមេ MCP។ វិធីប្រើជាមួយម៉ាស៊ីនមេ stdio របស់អ្នក៖

១. **ដំឡើង Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

២. **រត់ Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

៣. **សាកល្បងម៉ាស៊ីនមេរបស់អ្នក**៖ Inspector ផ្តល់ផ្ទាំងវេបដែលអ្នកអាច៖
   - មើលសមត្ថភាពម៉ាស៊ីនមេ
   - សាកល្បងឧបករណ៍ជាមួយប៉ារ៉ាម៉ែត្រផ្សេងៗ
   - តាមដានសារ JSON-RPC
   - កែតម្រូវបញ្ហាក្នុងការតភ្ជាប់

### ប្រើ VS Code

អ្នកអាចកែតម្រូវកំហុសម៉ាស៊ីនមេ MCP របស់អ្នកផ្ទាល់ក្នុង VS Code ដោយ៖

១. បង្កើតការកំណត់ភ្ជាប់ក្នុង `.vscode/launch.json`:
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

២. កំណត់ចំណុចបំបែកកំហុសក្នុងកូដម៉ាស៊ីនមេរបស់អ្នក
៣. រត់ភស្ដុតាង និងសាកល្បងជាមួយ Inspector

### សេចក្តីផ្តល់បច្ចេកទេសកែតម្រូវកំហុសទូទៅ

- ប្រើ `stderr` សម្រាប់ចុះបញ្ជី - មិនធ្វើការសរសេរទៅ `stdout` ដែលលំនាំជាសម្រាប់សារម៉ាស៊ីនមេ MCP
- ប្រាកដថាសារប្រភេទ JSON-RPC ទាំងអស់ត្រូវបំបែកដោយថ្មីជួរ
- សាកល្បងជាមួយឧបករណ៍សាមញ្ញមុនពេលបន្ថែមមុខងារលំបាក
- ប្រើ Inspector ដើម្បីផ្ទៀងផ្ទាត់ទ្រង់ទ្រាយសារ

## ប្រើម៉ាស៊ីនមេ stdio របស់អ្នកក្នុង VS Code

បន្ទាប់ពីអ្នកបានបង្កើតម៉ាស៊ីនមេ MCP stdio រួច អ្នកអាចភ្ជាប់វាមួយ VS Code ដើម្បីប្រើជាមួយ Claude ឬអតិថិជន MCP ផ្សេងទៀត។

### កំណត់រចនាសម្ព័ន្ធ

១. **បង្កើតឯកសារកំណត់រចនាសម្ព័ន្ធ MCP** នៅ `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ឬ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

២. **ចាប់ផ្តើមឡើងវិញ Claude**៖ បិទបិទ និងបើកឡើងវិញ Claude ដើម្បីផ្ទុកកំណត់រចនាសម្ព័ន្ធម៉ាស៊ីនមេថ្មី។

៣. **សាកល្បងការតភ្ជាប់**៖ ចាប់ផ្តើមការពិភាក្សាជាមួយ Claude ហើយសាកល្បងប្រើឧបករណ៍ម៉ាស៊ីនមេរបស់អ្នក៖
   - "អាចស្វាគមន៍ខ្ញុំតាមឧបករណ៍ស្វាគមន៍បានទេ?"
   - "គណនាចំនួនរួមនៃ 15 និង 27"
   - "តើព័ត៌មានម៉ាស៊ីនមេចង់ដឹងអ្វីខ្លះ?"

### ឧទាហរណ៍ម៉ាស៊ីនមេ stdio TypeScript

នេះជាឧទាហរណ៍ TypeScript ពេញលេញសម្រាប់យោង៖

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

// បន្ថែមឧបករណ៍
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

### ឧទាហរណ៍ម៉ាស៊ីនមេ stdio .NET

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


## សង្ខេប

ក្នុងមេរៀនធ្វើបច្ចុប្បន្នភាពនេះ អ្នកបានរៀន៖

- បង្កើតម៉ាស៊ីនមេ MCP ដោយប្រើ **stdio transport** បច្ចុប្បន្ន (វិធីសាស្ត្រផ្តល់អនុសាសន៍)
- យល់ដោយហេតុអ្វីផ្លូវសារទំនាក់ទំនង SSE ត្រូវបានយកចេញជំនួសដោយ stdio និង Streamable HTTP
- បង្កើតឧបករណ៍ដែលអាចហៅដោយអតិថិជន MCP
- កែតម្រូវកំហុសម៉ាស៊ីនមេដោយប្រើ MCP Inspector
- ភ្ជាប់ម៉ាស៊ីនមេ stdio របស់អ្នកជាមួយ VS Code និង Claude

ផ្លូវសារទំនាក់ទំនង stdio ផ្តល់វិធីសាស្ត្រងាយស្រួលជាង មានសុវត្ថិភាព និងប្រសិទ្ធភាពល្អក្នុងការបង្កើតម៉ាស៊ីនមេ MCP បើប្រៀបធៀបនឹង SSE ដែលបានយកចេញ។ វាជាវិធីសាស្ត្រផ្តល់អនុសាសន៍សម្រាប់អនុវត្ត MCP ច្រើនបំផុត ចាប់ពីកាលបរិច្ឆេទ 2025-06-18។

### .NET

១. យើងចាប់ផ្តើមបង្កើតឧបករណ៍មួយចំនួនសិន សម្រាប់នេះ យើងនឹងបង្កើតឯកសារ *Tools.cs* ជាមួយមាតិកាដូចតទៅ៖

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```


## អនុវត្តន៍៖ សាកល្បងម៉ាស៊ីនមេ stdio របស់អ្នក

ឥឡូវនេះអ្នកបានបង្កើតម៉ាស៊ីនមេ stdio រួច ហើយ យើងនឹងសាកល្បងវាដើម្បីធានាថាវាដំណើរការត្រឹមត្រូវ។

### តម្រូវការមុន

១. ប្រាកដថាអ្នកបានដំឡើង MCP Inspector៖
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

២. កូដម៉ាស៊ីនមេចាស់របស់អ្នកត្រូវបានរក្សាទុក (ឧទាហរណ៍ជា `server.py`)

### សាកល្បងជាមួយ Inspector

១. **ចាប់ផ្តើម Inspector ជាមួយម៉ាស៊ីនមេរបស់អ្នក**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

២. **បើកផ្ទាំងវេប**៖ Inspector នឹងបើកបង្ហាញផ្ទាំងរាវម៉ាស៊ីនមេរបស់អ្នក។

៣. **សាកល្បងឧបករណ៍**:
   - សាកល្បងឧបករណ៍ `get_greeting` ជាមួយឈ្មោះផ្សេងៗ
   - សាកល្បងឧបករណ៍ `calculate_sum` ជាមួយលេខផ្សេងគ្នា
   - ហៅឧបករណ៍ `get_server_info` ដើម្បីមើលព័ត៌មានម៉ាស៊ីនមេ

៤. **តាមដានការទំនាក់ទំនង**៖ Inspector បង្ហាញសារប្រភេទ JSON-RPC ផ្លាស់ប្ដូររវាងអតិថិជន និងម៉ាស៊ីនមេ។

### អ្វីដែលអ្នកគួរមើលឃើញ

ពេលម៉ាស៊ីនមេរបស់អ្នកចាប់ផ្តើមបានត្រឹមត្រូវ អ្នកគួរមើលឃើញ៖
- សមត្ថភាពម៉ាស៊ីនមេបង្ហាញនៅក្នុង Inspector
- ឧបករណ៍មានសម្រាប់សាកល្បង
- ការប្ដូរសារប្រភេទ JSON-RPC ជោគជ័យ
- ចម្លើយឧបករណ៍បង្ហាញនៅក្នុងផ្ទាំង

### បញ្ហាទូទៅ និងដំណោះស្រាយ

**ម៉ាស៊ីនមេមិនចាប់ផ្តើម:**
- ពិនិត្យថា dependencies ទាំងអស់បានដំឡើង៖ `pip install mcp`
- ពិនិត្យរូបមន្ត Python និងការសង្ស័យ
- មើលសារកំហុសក្នុងកុងសូល

**ឧបករណ៍មិនបង្ហាញ:**
- ប្រាកដថា `@server.tool()` decorators មានស្រាប់
- ពិនិត្យមើលថា function ឧបករណ៍បានកំណត់មុន `main()`
- ធានាថាម៉ាស៊ីនមេចួបប្រទះបានត្រឹមត្រូវ

**បញ្ហា​តភ្ជាប់:**
- ពិនិត្យថា ម៉ាស៊ីនមេប្រើ stdio transport ត្រឹមត្រូវ
- មើលថាមិនមានដំណើរការផ្សេងដែលរំខាន
- ត្រួតពិនិត្យណែនាំកំណត់ Inspector

## ការដាក់ចេញ

សាកល្បងបន្ថែមសមត្ថភាពនៅលើម៉ាស៊ីនមេរបស់អ្នក។ ចូលទៅ [ទំព័រនេះ](https://api.chucknorris.io/) ដើម្បីបន្ថែមឧបករណ៍ដែលអាចហៅ API។ អ្នកជ្រើសរើសថាអ្វីដែលម៉ាស៊ីនមេគួរតែមាន។ រីករាយ :)

## ដំណោះស្រាយ

[ដំណោះស្រាយ](./solution/README.md) នេះជាដំណោះស្រាយដែលអាចអនុវត្តបានជាមួយកូដធ្វើការ។

## ចំណុចសំខាន់

ចំណុចសំខាន់ៗពីជំពូកនេះមានដូចខាងក្រោម៖

- ផ្លូវសារទំនាក់ទំនង stdio គឺជាវិធីសាស្ត្រផ្តល់អនុសាសន៍សម្រាប់ម៉ាស៊ីនមេ MCP ក្នុងតំបន់។
- ផ្លូវសារទំនាក់ទំនង stdio អនុញ្ញាតឲ្យមានការទំនាក់ទំនងរលូនរវាងម៉ាស៊ីនមេ MCP និងអតិថិជនតាមរយៈច្រាសបញ្ចូល និងច្រាសបញ្ចេញស្តង់ដារ។
- អ្នកអាចប្រើ Inspector និង Visual Studio Code ដើម្បីប្រើម៉ាស៊ីនមេ stdio ដោយផ្ទាល់ ហើយធ្វើការកែតម្រូវកំហុស និងភ្ជាប់ដោយអត្ថប្រយោជន៍។

## ឧទាហរណ៍

- [គណនី Java](../samples/java/calculator/README.md)
- [គណនី .Net](../../../../03-GettingStarted/samples/csharp)
- [គណនី JavaScript](../samples/javascript/README.md)
- [គណនី TypeScript](../samples/typescript/README.md)
- [គណនី Python](../../../../03-GettingStarted/samples/python) 

## របស់បន្ថែម

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## តើអ្វីទៅបន្ទាប់

## ជំហានបន្ទាប់

ឥឡូវនេះអ្នកបានរៀនរបៀបបង្កើតម៉ាស៊ីនមេ MCP ដោយប្រើ stdio transport អ្នកអាចស្វែងយល់ពីប្រធានបទកាន់តែជ្រាបជ្រៅ៖

- **បន្ទាប់**៖ [ការផ្ទុកស្ទ្រីម HTTP ជាមួយ MCP (Streamable HTTP)](../06-http-streaming/README.md)​ - រៀនអំពីផ្លូវសារទំនាក់ទំនងដទៃទៀតសម្រាប់ម៉ាស៊ីនមេចម្ងាយ
- **ជំនាញខ្ពស់**៖ [គោលការណ៍សុវត្ថិភាព MCP](../../02-Security/README.md) - អនុវត្តសុវត្ថិភាពនៅក្នុងម៉ាស៊ីនមេ MCP របស់អ្នក
- **ផលិតផល**៖ [យុទ្ធសាស្រ្តចេញផ្សាយ](../09-deployment/README.md) - ចេញផ្សាយម៉ាស៊ីនមេរបស់អ្នកសម្រាប់ការប្រើប្រាស់ក្នុងផលិតផល

## របស់បន្ថែម

- [MCP Specification 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - បញ្ជាក់ផ្លូវការជាផ្លូវការដោយ MCP
- [ឯកសារ MCP SDK](https://github.com/modelcontextprotocol/sdk) - ឯកសារយោង SDK សម្រាប់ភាសាទាំងអស់
- [ឧទាហរណ៍សហគមន៍](../../06-CommunityContributions/README.md) - ឧទាហរណ៍ម៉ាស៊ីនមេច្រើនទៀតពីសហគមន៍

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំសំរាប់ភាពត្រឹមត្រូវ សូមអ្នកយល់ដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិនេះអាចមានខុសច្រឡំនិងភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅក្នុងភាសាទូទៅគួរត្រូវបានយកទៅជាផ្នែកប្រភពដែលមានអំនាច។ សម្រាប់ព័ត៌មានសំខាន់ សូមប្រើការបកប្រែដោយអ្នកជំនាញមនុស្ស។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសផ្សេងណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->