# ម៉ាស៊ីនបម្រើ MCP ជាមួយការដឹកជញ្ជូន stdio

> **⚠️ បច្ចុប្បន្នភាពសំខាន់**៖ ចាប់តាំងពីការបញ្ជាក់ MCP ថ្ងៃទី 2025-06-18, ការដឹកជញ្ជូន SSE (Server-Sent Events) ដាច់ដោយឡែកត្រូវបាន **លើកលែង** ហើយបានជំនួសដោយ "Streamable HTTP" ដឹកជញ្ជូន។ ការបញ្ជាក់ MCP បច្ចុប្បន្នកំណត់អង្គភាពដឹកជញ្ជូនសំខាន់ពីរជា៖
> 1. **stdio** - បញ្ចូល/បញ្ចេញស្តង់ដារ (ផ្ដល់អនុសាសន៍សម្រាប់ម៉ាស៊ីនបម្រើក្នុងតំបន់)
> 2. **Streamable HTTP** - សម្រាប់ម៉ាស៊ីនបម្រើពីចម្ងាយដែលអាចប្រើ SSE ក្នុងខ្លួន
>
> មេរៀននេះបានបច្ចុប្បន្នភាពដើម្បីផ្ដោតលើការដឹកជញ្ជូន **stdio** ដែលជាវិធីសាស្រ្តដែលផ្ដល់អនុសាសន៍សម្រាប់ការអនុវត្តម៉ាស៊ីនបម្រើ MCP ផ្ទាល់ខ្លួនភាគច្រើន។

ការដឹកជញ្ជូន stdio អនុញ្ញาตឲ្យម៉ាស៊ីនបម្រើ MCP ទំនាក់ទំនងជាមួយអតិថិជនតាមរយៈចរន្តបញ្ចូល និងចរន្តបញ្ចេញស្តង់ដារ។ វាជាវិធីសាស្រ្តដែលមានប្រើប្រាស់ច្រើនបំផុត និងផ្ដល់អនុសាសន៍ក្នុងការដឹកជញ្ជូនបច្ចុប្បន្នរបស់ MCP ដែលផ្តល់វិធីសាស្រ្តសាមញ្ញ និងមានប្រសិទ្ធភាពសម្រាប់បង្កើតម៉ាស៊ីនបម្រើ MCP ដែលអាចបង្រួមជាមួយកម្មវិធីអតិថិជនផ្សេងៗបានយ៉ាងងាយស្រួល។

## ទិដ្ឋភាពទូទៅ

មេរៀននេះគ្របដណ្ដប់ពីរបៀបបង្កើត និងប្រើប្រាស់ម៉ាស៊ីនបម្រើ MCP ដោយប្រើការដឹកជញ្ជូន stdio។

## គោលបំណងការរៀន

នៅចុងបញ្ចប់មេរៀននេះ អ្នកនឹងអាច៖

- បង្កើតម៉ាស៊ីនបម្រើ MCP ដោយប្រើការដឹកជញ្ជូន stdio។
- បញ្ហាទោសម៉ាស៊ីនបម្រើ MCP ដោយប្រើ Inspector។
- ប្រើម៉ាស៊ីនបម្រើ MCP ដោយប្រើ Visual Studio Code។
- យល់ដឹងពីអង្គភាពដឹកជញ្ជូន MCP បច្ចុប្បន្ន និងហេតុអ្វីបានជាការដឹកជញ្ជូន stdio ត្រូវបានផ្ដល់អនុសាសន៍។


## ការដឹកជញ្ជូន stdio - វាដំណើរការយ៉ាងដូចម្តេច

ការដឹកជញ្ជូន stdio គឺជា១ក្នុងពីរពីររបៀបដឹកជញ្ជូនស្តង់ដារដែលមាននៅក្នុងការបញ្ជាក់ MCP
`2026-07-28`។ វាដំណើរការយ៉ាងដូចខាងក្រោម៖

- **ការទំនាក់ទំនងសាមញ្ញ**៖ ម៉ាស៊ីនបម្រើអានសារជាសារ JSON-RPC ពីបញ្ចូលស្តង់ដារ (`stdin`) ហើយផ្ញើសារទៅកាន់បញ្ចេញស្តង់ដារ (`stdout`)។
- **មូលដ្ឋានប្រតិបត្តិការ**៖ អតិថិជនចាប់ផ្ដើមម៉ាស៊ីនបម្រើ MCP ជាប្រតិបត្តការជា subprocess។
- **ទ្រង់ទ្រាយសារ**៖ សារជារឿងសំណើ JSON-RPC ផ្ដល់ដំណឹងឬចម្លើយដែលបែងចែកដោយខ្សែបន្ទាត់ថ្មី។
- **ការចុះសំគាល់**៖ ម៉ាស៊ីនបម្រើអាចសរសេរលេខសញ្ញា UTF-8 ទៅកាន់កំហុសស្តង់ដារ (`stderr`) សម្រាប់ការចុះសំគាល់។

### អ្វីដែលត្រូវការសំខាន់
- សារត្រូវតែលាតត្រដាងដោយខ្សែបន្ទាត់ថ្មី ហើយមិនត្រូវមានខ្សែបន្ទាត់ថ្មីចម្លងនៅក្នុងទេ
- ម៉ាស៊ីនបម្រើមិនត្រូវសរសេរអ្វីទៅ `stdout` ដែលមិនមែនសារអង្គភាព MCP ត្រឹមត្រូវ
- អតិថិជនមិនត្រូវសរសេរអ្វីទៅ `stdin` របស់ម៉ាស៊ីនបម្រើដែលមិនមែនសារអង្គភាព MCP ត្រឹមត្រូវ

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

ក្នុងកូដខាងលើ៖

- យើងនាំចូលថ្នាក់ `Server` និង `StdioServerTransport` ពី MCP SDK
- យើងបង្កើតម៉ាស៊ីនបម្រើជាមួយការកំណត់ និងសមត្ថភាពមូលដ្ឋាន
- យើងបង្កើតឧបករណ៍ `StdioServerTransport` ហើយភ្ជាប់ម៉ាស៊ីនបម្រើជាមួយវា ដើម្បីអនុញ្ញាតការទំនាក់ទំនងតាមរយៈ stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# បង្កើតវេទិកាសែលវើរ
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

ក្នុងកូដខាងលើ យើងបាន៖

- បង្កើតម៉ាស៊ីនបម្រើដោយប្រើ MCP SDK
- កំណត់ឧបករណ៍ដោយប្រើ decorators
- ប្រើ stdio_server context manager ដើម្បីគ្រប់គ្រងការដឹកជញ្ជូន

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

ភាពខុសគ្នាសំខាន់ពី SSE គឺម៉ាស៊ីនបម្រើ stdio:

- មិនទាមទារការតំឡើងម៉ាស៊ីនបម្រើវែបឬចំណុចចូល HTTP
- ត្រូវបានចាប់ផ្ដើមជាប្រតិបត្តកម្មជាឧបករណ៍ក្រោមរបស់អតិថិជន
- ទំនាក់ទំនងតាមរយៈចរន្ត stdin/stdout
- មានភាពសាមញ្ញក្នុងការអនុវត្ត និងកំណត់បញ្ហា

## លំហាត់៖ បង្កើតម៉ាស៊ីនបម្រើ stdio

ដើម្បីបង្កើតម៉ាស៊ីនបម្រើរបស់យើង អ្នកត្រូវចងចាំពីរប្រភេទ៖

- អ្នកត្រូវប្រើម៉ាស៊ីនបម្រើវែបដើម្បីបង្ហាញចំណុចចូលសម្រាប់ការតភ្ជាប់ និងសារ។
## មន្ទីរ​សិក្សា៖ បង្កើតម៉ាស៊ីនបម្រើ MCP stdio សាមញ្ញ

នៅក្នុងមន្ទីរនេះ យើងនឹងបង្កើតម៉ាស៊ីនបម្រើ MCP សាមញ្ញមួយដោយប្រើការដឹកជញ្ជូន stdio ដែលផ្ដល់អនុសាសន៍។ ម៉ាស៊ីនបម្រើនេះនឹងបង្ហាញឧបករណ៍ដែលអតិថិជនអាចហៅបានដោយប្រើ Model Context Protocol ស្តង់ដារ។

### គ្រឿងចាំបាច់

- Python 3.8 ឬថ្មីជាងនេះ
- MCP Python SDK: `pip install mcp`
- ការយល់ដឹងមូលដ្ឋានអំពីកម្មវិធី async

ចាប់ផ្តើមដោយបង្កើតម៉ាស៊ីនបម្រើ MCP stdio នាលើកដំបូងរបស់យើង៖

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

## ភាពខុសគ្នាចម្បងពីវិធី SSE ដែលបានលើកលែង

**ការដឹកជញ្ជូន Stdio (ស្តង់ដារបច្ចុប្បន្ន):**
- ម៉ូដែល subprocess ងាយស្រួល - អតិថិជនចាប់ផ្ដើមម៉ាស៊ីនបម្រើជាកូន
- ទំនាក់ទំនងតាម(stdin/stdout) ប្រើសារ JSON-RPC
- មិនត្រូវការតំឡើងម៉ាស៊ីនបម្រើ HTTP
- មានការប្រសើរលើសមត្ថភាព និងសុវត្ថិភាព
- ง่ายក្នុងការបញ្ហាទោស និងអភិវឌ្ឍ

**ការដឹកជញ្ជូន SSE (បានលើកលែងចាប់ពី MCP 2025-06-18):**
- ត្រូវការម៉ាស៊ីនបម្រើ HTTP ជាមួយចំណុចចូល SSE
- ការតំឡើងស្មុគស្មាញជាមួយស្ថាបត្យកម្មម៉ាស៊ីនបម្រើវែប
- មានការគិតគូរពិសេសវិសេសសម្រាប់សុវត្ថិភាពចំណុចចូល HTTP
- ឥឡូវបានជំនួសជាមួយ Streamable HTTP សម្រាប់ស្ថានការណ៍ផ្អែកលើវែប

### បង្កើតម៉ាស៊ីនបម្រើជាមួយការដឹកជញ្ជូន stdio

ដើម្បីបង្កើតម៉ាស៊ីនបម្រើ stdio របស់យើង ត្រូវការធ្វើ៖

1. **នាំចូលបណ្ណាល័យដែលត្រូវការ** - យើងត្រូវការចំពោះធាតុម៉ាស៊ីនបម្រើ MCP និងការដឹកជញ្ជូន stdio
2. **បង្កើតម៉ាស៊ីនបម្រើមួយ** - កំណត់ម៉ាស៊ីនបម្រើជាមួយសមត្ថភាពរបស់វា
3. **កំណត់ឧបករណ៍** - បន្ថែមមុខងារដែលយើងចង់បង្ហាញ
4. **កំណត់ការដឹកជញ្ជូន** - កំណត់ការទំនាក់ទំនង stdio
5. **បើកម៉ាស៊ីនបម្រើ** - ចាប់ផ្តើមម៉ាស៊ីនបម្រើ និងគ្រប់គ្រងសារ

អរុណសួរពីរបៀបដំណើរការនេះបន្តិចៗ៖

### ជំហានទី១៖ បង្កើតម៉ាស៊ីនបម្រើ stdio មូលដ្ឋាន

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# កំណត់ការចុះបញ្ជី
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

### ជំហានទី២៖ បន្ថែមឧបករណ៍បន្ថែម

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

### ជំហានទី៣៖ ដំណើរការម៉ាស៊ីនបម្រើ

រក្សាទុកកូដជាឯកសារ `server.py` ហើយរត់វាពីបន្ទាត់បញ្ជា៖

```bash
python server.py
```

ម៉ាស៊ីនបម្រើនឹងចាប់ផ្ដើម និងរងចាំការបញ្ចូលពី stdin។ វាទំនាក់ទំនងដោយប្រើសារ JSON-RPC តាមរយៈការដឹកជញ្ជូន stdio។

### ជំហានទី៤៖ សាកល្បងជាមួយ Inspector

អ្នកអាចសាកល្បងម៉ាស៊ីនបម្រើរបស់អ្នកដោយប្រើ MCP Inspector៖

1. ដំឡើង Inspector៖ `npx @modelcontextprotocol/inspector`
2. រត់ Inspector ហើយបញ្ជាក់ទៅម៉ាស៊ីនបម្រើរបស់អ្នក
3. សាកល្បងឧបករណ៍ដែលអ្នកបានបង្កើត

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## កំណត់បញ្ហាម៉ាស៊ីនបម្រើ stdio របស់អ្នក

### ប្រើ MCP Inspector

MCP Inspector គឺជាឧបករណ៍មានតម្លៃសម្រាប់កំណត់បញ្ហា និងសាកល្បងម៉ាស៊ីនបម្រើ MCP។ វាដំណើរការជាមួយម៉ាស៊ីនបម្រើ stdio របស់អ្នកដូចខាងក្រោម៖

1. **ដំឡើង Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **រត់ Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **សាកល្បងម៉ាស៊ីនបម្រើ**: Inspector ផ្ដល់ឱ្យអ្នកនូវចំណុចចូលវែប ដែលអ្នកអាច៖
   - មើលសមត្ថភាពម៉ាស៊ីនបម្រើ
   - សាកល្បងឧបករណ៍ជាមួយប៉ារ៉ាម៉ែត្រផ្សេងៗ
   - ត្រួតពិនិត្យសារ JSON-RPC
   - កំណត់បញ្ហា វិលវល់ការតភ្ជាប់

### ប្រើ VS Code

អ្នកក៏អាចកំណត់បញ្ហាម៉ាស៊ីនបម្រើ MCP របស់អ្នកដោយផ្ទាល់ក្នុង VS Code ផងដែរ៖

1. បង្កើតកំណត់រចនាសម្ព័ន្ធបើកនាវិត្រួតពិនិត្យនៅ `.vscode/launch.json`:
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

2. កំណត់ចំណុចកំណត់ដំណើរការ (breakpoints) ក្នុងកូដម៉ាស៊ីនបម្រើរបស់អ្នក
3. រត់ debugger និងសាកល្បងជាមួយ Inspector

### ការណែនាំកំណត់បញ្ហារឹតត្បិត

- ប្រើ `stderr` សម្រាប់ការចុះសំគាល់ - មិនត្រូវសរសេរទៅ `stdout` ពីព្រោះវាគឺបានរក្សាសម្រាប់សារ MCP
- ធានាថាសារទាំងអស់ JSON-RPC ត្រូវបានបែងចែកដោយខ្សែបន្ទាត់ថ្មី
- សាកល្បងជាមួយឧបករណ៍សាមញ្ញ ជាមុនមុនពេលបន្ថែមមុខងារលំបាក
- ប្រើ Inspector ដើម្បីត្រួតពិនិត្យទ្រង់ទ្រាយសារ

## ប្រើម៉ាស៊ីនបម្រើ stdio របស់អ្នកក្នុង VS Code


នៅពេលដែលអ្នកបានបង្កើតម៉ាស៊ីនបម្រើ MCP stdio រួចហើយ អ្នកអាចបញ្ចូលវាជាមួយ VS Code ដើម្បីប្រើវាជាមួយ Claude ឬអតិថិជន MCP ដែលសមស្របផ្សេងទៀត។

### ការកំណត់រចនាសម្ព័ន្ធ

1. **បង្កើតឯកសារកំណត់រចនាសម្ព័ន្ធ MCP** នៅ `%APPDATA%\Claude\claude_desktop_config.json` (Windows) ឬ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac)៖

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

2. **ចាប់ផ្តើមឡើងវិញ Claude**: បិទហើយបើកឡើងវិញ Claude ដើម្បីផ្ទុកកំណត់រចនាសម្ព័ន្ធម៉ាស៊ីនបម្រើថ្មី។

3. **សាកល្បងការតភ្ជាប់**: ចាប់ផ្តើមការសន្ទនាជាមួយ Claude ហើយសាកល្បងប្រើឧបករណ៍ម៉ាស៊ីនបម្រើរបស់អ្នក៖
   - "តើអ្នកអាចស្វាគមន៍ខ្ញុំដោយប្រើឧបករណ៍ស្វាគមន៍ទេ?"
   - "គណនាតម្លៃបូករបស់ 15 និង 27"
   - "តើព័ត៌មានម៉ាស៊ីនបម្រើជាអ្វី?"

### ឧទាហរណ៍ម៉ាស៊ីនបម្រើ stdio ប្រភេទ TypeScript

នេះគឺជា ឧទាហរណ៍ TypeScript ពេញលេញសម្រាប់យោង៖

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

### ឧទាហរណ៍ម៉ាស៊ីនបម្រើ stdio ប្រភេទ .NET

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

នៅក្នុងមេរៀនដែលបានបរិច្ឆេទថ្មីនេះ អ្នកបានរៀនពីរបៀប៖

- បង្កើតម៉ាស៊ីនបម្រើ MCP ដោយប្រើ **stdio transport** បច្ចុប្បន្ន (វិធីសាស្រ្តណែនាំ)
- យល់ពីមូលហេតុដែល SSE transport ត្រូវបានលុបចោលក្នុងការជំនួសដោយ stdio និង Streamable HTTP
- បង្កើតឧបករណ៍ដែលអាចត្រូវបានគេហៅដោយអតិថិជន MCP
- បញ្ជាក់កំហុសម៉ាស៊ីនបម្រើរបស់អ្នកដោយប្រើ MCP Inspector
- សម្របសម្រួលម៉ាស់ឌឺ stdio របស់អ្នកជាមួយ VS Code និង Claude

ការដឹកជញ្ជូន stdio ផ្តល់ជាមធ្យោបាយសាមញ្ញ ជាអតិភាព និងមានសមត្ថភាពខ្ពស់ក្នុងការបង្កើតម៉ាស៊ីនបម្រើ MCP នៅលើវិធីសាស្រ្ត SSE ដែលត្រូវបានលុបចោល។ វាគឺជាវិធីសាស្រ្តណែនាំសម្រាប់អនុវត្តម៉ាស៊ីនបម្រើ MCP ភាគច្រើនសម្រាប់ព័ត៌មានបញ្ជាក់ 2025-06-18។


### .NET

1. យើងនឹងបង្កើតឧបករណ៍មួយចំនួនជាមុនសិន សម្រាប់នេះយើងនឹងបង្កើតឯកសារ *Tools.cs* ដែលមានមាតិកាដូចខាងក្រោម៖

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## អនុវត្តន៍ៈ សាកល្បងម៉ាស៊ីនបម្រើ stdio របស់អ្នក

ឥឡូវនេះអ្នកបានបង្កើតម៉ាស៊ីនបម្រើ stdio រួច សូមសាកល្បងវាដើម្បីប្រាកដថាវាដំណើរការត្រឹមត្រូវ។

### សេចក្ដីតម្រូវការ

1. ប្រាកដថាអ្នកបានដំឡើង MCP Inspector រួចហើយ៖
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. កូដម៉ាស៊ីនបម្រើរបស់អ្នកគួរត្រូវបានរក្សាទុក (ឧ។ `server.py`)

### សាកល្បងជាមួយ Inspector

1. **ចាប់ផ្តើម Inspector ជាមួយម៉ាស៊ីនបម្រើរបស់អ្នក**៖
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **បើកផ្ទាំងគេហទំព័រ**៖ Inspector នឹងបើកបង្ហាញផ្ទាំងក្រោយម៉ាស៊ីនបម្រើរបស់អ្នក។

3. **សាកល្បងឧបករណ៍**: 
   - សាកល្បងឧបករណ៍ `get_greeting` ជាមួយឈ្មោះផ្សេងៗ
   - សាកល្បងឧបករណ៍ `calculate_sum` ជាមួយលេខផ្សេងៗ
   - ហៅឧបករណ៍ `get_server_info` ដើម្បីមើលព័ត៌មានម៉ាស៊ីនបម្រើ

4. **តាមដានការទំនាក់ទំនង**: Inspector បង្ហាញសារចាប់ផ្តើម JSON-RPC ដែលប្តូរជាមួយរវាងអតិថិជន និងម៉ាស៊ីនបម្រើ។

### អ្វីដែលអ្នកគួរមើលឃើញ

នៅពេលម៉ាស៊ីនបម្រើរបស់អ្នកចាប់ផ្តើមបានត្រឹមត្រូវ អ្នកគួរមើលឃើញ៖
- សមត្ថភាពម៉ាស៊ីនបម្រើត្រូវបញ្ចេញនៅក្នុង Inspector
- ឧបករណ៍ដែលអាចប្រើសម្រាប់សាកល្បង
- ការប្តូរសារជោគជ័យ JSON-RPC
- ចម្លើយឧបករណ៍បង្ហាញនៅផ្ទាំង

### បញ្ហាទូទៅនិងដំណោះស្រាយ

**ម៉ាស៊ីនបម្រើមិនចាប់ផ្តើម:**
- ពិនិត្យមើលថាតម្លើងការបណ្តាំគ្រប់ចេញ: `pip install mcp`
- ពិនិត្យវេយ្យាករណ៍ Python និងការផ្ដោតអក្សរ
- ស្វែងរកសារបញ្ហានៅក្នុងកុងសូល

**ឧបករណ៍មិនបង្ហាញ:**
- ជាក់ច្បាស់ថាការតុបតែង `@server.tool()` មានស្រាប់
- ពិនិត្យឲ្យប្រាកដថាអនុគមន៍ឧបករណ៍បានកំណត់មុន `main()`
- ពិនិត្យម៉ាស៊ីនបម្រើបានកំណត់រចនាសម្ព័ន្ធត្រឹមត្រូវ

**បញ្ហាការតភ្ជាប់:**
- ធ្វើឲ្យប្រាកដថាម៉ាស៊ីនបម្រើប្រើ stdio transport ត្រឹមត្រូវ
- ពិនិត្យថាមានដំណើរការផ្សេងៗមិនរំខាន
- ពិនិត្យវេយ្យាករណ៍ពាក្យបញ្ជា Inspector

## ការប្រលង

សូមសាកល្បងបង្កើតម៉ាស៊ីនបម្រើរបស់អ្នកជាមួយសមត្ថភាពបន្ថែម។ មើល [ទំព័រនេះ](https://api.chucknorris.io/) ដើម្បីដាក់ឧបករណ៍ដែលហៅ API។ អ្នកជ្រើសរើសរូបរាងម៉ាស៊ីនបម្រើ។ រីករាយឡើង :)
## ដំណោះស្រាយ

[ដំណោះស្រាយ](./solution/README.md) នេះគឺជាដំណោះស្រាយដែលមានកូដដំណើរការ។

## ចំណុចសំខាន់

ចំណុចសំខាន់ពីមេរៀននេះមានដូចខាងក្រោម៖

- stdio transport គឺជាវិធីសាស្រ្តណែនាំសម្រាប់ម៉ាស៊ីនបម្រើ MCP មូលដ្ឋាន។
- stdio transport អនុញ្ញាតឲ្យមានការប្រាស្រ័យទាក់ទងឆ្លាតវៃរវាងម៉ាស៊ីនបម្រើ និងអតិថិជន MCP ដោយប្រើច្រកបញ្ចូល និងច្រកបញ្ចេញស្តង់ដារ។
- អ្នកអាចប្រើ Inspector និង Visual Studio Code ដើម្បីប្រើម៉ាស៊ីនបម្រើ stdio ដោយផ្ទាល់ ធ្វើឲ្យការទាញយកកំហុស និងសម្របសម្រួលកាន់តែងាយស្រួល។

## ឧទាហរណ៍

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## ធនធានបន្ថែម

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## តើបន្ទាប់មុខមានអ្វីខ្លះ

## ជំហានបន្ទាប់

ឥឡូវនេះដែលអ្នកបានរៀនពីរបៀបបង្កើតម៉ាស៊ីនបម្រើ MCP ជាមួយ stdio transport អ្នកអាចស្វែងយល់ពីប្រធានបទកាន់តែច្រើនជាងនេះ៖

- **បន្ទាប់**: [HTTP Streaming ជាមួយ MCP (Streamable HTTP)](../06-http-streaming/README.md) - រៀនអំពីប្រព័ន្ធដឹកជញ្ជូនផ្សេងទៀតសម្រាប់ម៉ាស៊ីនបម្រើចម្ងាយ
- **កម្រិតខ្ពស់**: [អនុស្សរណៈសុវត្ថិភាព MCP](../../02-Security/README.md) - អនុវត្តសុវត្ថិភាពក្នុងម៉ាស៊ីនបម្រើ MCP របស់អ្នក
- **ផលិតកម្ម**: [យុទ្ធសាស្រ្តចែកចាយ](../09-deployment/README.md) - ចែកចាយម៉ាស៊ីនបម្រើសម្រាប់ការប្រើប្រាស់ផលិតកម្ម

## ធនធានបន្ថែម

- [ការបញ្ជាក់ MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - ការបញ្ជាក់បច្ចុប្បន្ន
- [ឯកសារសម្រាប់ MCP SDK](https://github.com/modelcontextprotocol/sdk) - ការយោង SDK សម្រាប់ភាសាទាំងអស់
- [ឧទាហរណ៍ពីសហគមន៍](../../06-CommunityContributions/README.md) - ឧទាហរណ៍ម៉ាស៊ីនបម្រើបន្ថែមពីសហគមន៍

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->