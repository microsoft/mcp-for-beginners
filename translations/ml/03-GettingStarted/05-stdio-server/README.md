# stdio ട്രാൻസ്പോർട്ടോടുള്ള MCP സർവർ

> **⚠️ 중요한 업데이트**: MCP സവിശേഷത 2025-06-18 മുതൽ, സ്റ്റാൻഡ്എലോൺ SSE (Server-Sent Events) ട്രാൻസ്പോർട്ട് **നിരാക്കുകയായി** മാറുകയും "Streamable HTTP" ട്രാൻസ്പോർട്ടിൻറൊൽ പകരം വന്നിട്ടുണ്ട്. നിലവിലെ MCP സവിശേഷത രണ്ട് പ്രധാന ട്രാൻസ്പോർട്ട് മെക്കാനിസങ്ങൾ നിർവ്വചിക്കുന്നു:
> 1. **stdio** - സ്റ്റാൻഡേർഡ് ഇൻപുട്ട്/ഔട്ട്പുട്ട് (പ്രാദേശിക സർവറുകൾക്ക് ശുപാർശ ചെയ്യുന്നു)
> 2. **Streamable HTTP** - SSE ഉൾക്കൊള്ളുന്ന ദൂരം ഭേദമായ സർവറുകൾക്കായി
>
> ഈ പാഠം **stdio ട്രാൻസ്പോർട്ട്**-നെയായി പുതുക്കിയിരിക്കുന്നു, ഇത് MCP സർവർ നടപ്പിലാക്കലുകളിൽ ഏറ്റവും ശുപാർശ ചെയ്യുന്ന സമീപനമാണ്.

stdio ട്രാൻസ്പോർട്ട് MCP സർവറുകൾക്ക് ക്ലയന്റുകളുമായി സ്റ്റാൻഡേർഡ് ഇൻപുട്ടും ഔട്ട്പുട്ടും സ്ട്രീമുകളിലൂടെ ആശയവിനിമയം നടത്താൻ അനുവദിക്കുന്നു. ഇത് നിലവിലെ MCP സവിശേഷതയിൽ ഏറ്റവും വ്യാപകമായി ഉപയോഗിക്കുകയും ശുപാർശ ചെയ്യപ്പെടുകയും ചെയ്യുന്ന ട്രാൻസ്പോർട്ട് സംവിധാനമാണ്. ഓട്ടം ലളിതവും കാര്യക്ഷമവുമായ രീതിയിൽ MCP സർവർ നിർമ്മിക്കാൻ സഹായിക്കുന്നു, വിവിധ ക്ലയന്റ് അപേക്ഷകളുമായി എളുപ്പത്തിൽ സംയോജിപ്പിക്കാവുന്നതുമായി.

## അവലോകനം

stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സർവറുകൾ എങ്ങനെ നിർമ്മിക്കാമെന്നും ഉപയോഗിക്കാമെന്നും ഈ പാഠം സ്ലന്തിക്കും.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം കഴിഞ്ഞാൽ നിങ്ങൾ താഴെ പറയുന്നവ കഴിയും:

- stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സർവർ നിർമ്മിക്കുക.
- Inspector ഉപയോഗിച്ച് MCP സർവർ ഡീബഗ് ചെയ്യുക.
- Visual Studio Code ഉപയോഗിച്ച് MCP സർവർ ഉപയോഗിക്കുക.
- നിലവിലുള്ള MCP ട്രാൻസ്പോർട്ട് മെക്കാനിസങ്ങൾ മനസിലാക്കുക, stdio എന്തുകൊണ്ടും ശുപാർശ ചെയ്യപ്പെടുന്നത് എന്തുകൊണ്ട് എന്നറിയുക.

## stdio ട്രാൻസ്പോർട്ട് - പ്രവർത്തിപ്പിക്കുന്ന വിധം

stdio ട്രാൻസ്പോർട്ട് MCP സവിശേഷതയിലെ (2025-06-18) രണ്ട് പിന്തുണയുള്ള ട്രാൻസ്പോർട്ടുകളിൽ ഒന്നാണ്. ഇത് പ്രവർത്തിക്കുന്നത് ഇങ്ങനെ:

- **ലളിതമായ ആശയവിനിമയം**: സർവർ JSON-RPC സന്ദേശങ്ങൾ സ്റ്റാൻഡേർഡ് ഇൻപുട്ട് (`stdin`) ഇല നിന്ന് വായിക്കുകയും സ്റ്റാൻഡേർഡ് ഔട്ട്പുട്ട് (`stdout`) വഴിയേ സന്ദേശങ്ങൾ അയയ്ക്കുകയും ചെയ്യുന്നു.
- **പ്രോസസ്-അടിസ്ഥാനമായ**: ക്ലയന്റ് MCP സർവറെ ഉപപ്രക്രിയയായി ആരംഭിക്കുന്നു.
- **സന്ദേശ ഫോർമാറ്റ്**: ഓരോ സന്ദേശവും JSON-RPC individual അഭ്യർത്ഥനകൾ, അറിയിപ്പുകൾ, അല്ലെങ്കിൽ പ്രതികരണങ്ങളായി newline-ൽ വേർതിരിച്ചിട്ടുള്ളതാണ്.
- **ലോഗിംഗ്**: ലോഗിംഗിന് സർവർ UTF-8 സ്ട്രിംഗ്‌കൾ സ്റ്റാൻഡേർഡ് എറർ (`stderr`)എഴുതാം.

### പ്രധാന ആവശ്യകതകൾ:
- സന്ദേശങ്ങൾ newline-കൾ കൊണ്ട് വേർതിരിക്കപ്പെട്ടിരിക്കണം, കൂടാതെ embedded newline-കൾ ഉള്ളതല്ലായിരിക്കുക
- സർവർ `stdout`-യിൽ ഒരു സാധുവായ MCP സന്ദേശമല്ലാത്ത ഏതെങ്കിലും എഴുതരുത്
- ക്ലയന്റ് MCP സന്ദേശമല്ലാത്ത ഏതെങ്കിലും `stdin`-ലേക്ക് എഴുതരുത്

### ടൈപ്‌സ്‌ക്രിപ്റ്റ്

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

മുകളിലെ കോഡിൽ:

- MCP SDK-യിൽ നിന്ന് `Server` ക്ലാസ്, `StdioServerTransport` ഇറക്കുമതി ചെയ്യുന്നു
- അടിസ്ഥാന കോൺഫിഗറേഷൻ, കഴിവുകൾ ഉപയോഗിച്ച് ഒരു സർവർ ഉദാഹരണമുണ്ടാക്കുന്നു
- ഒരു `StdioServerTransport` ഉദാഹരണം സൃഷ്ടിച്ച് സർവറെ അതോടു ബന്ധിപ്പിക്കുന്നു, stdin/stdout വഴിയുള്ള ആശയവിനിമയം സാധ്യമാക്കുന്നു

### പൈതൺ

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# സെർവർ ഇൻസ്റ്റൻസ് സൃഷ്‌ടിക്കുക
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

മുകളില്‍ കാണിച്ച കോഡില്‍:

- MCP SDK ഉപയോഗിച്ച് ഒരു സർവർ ഉദാഹരണം സൃഷ്ടിക്കുന്നു
- ഡെക്കറേറ്ററുകൾ ഉപയോഗിച്ച് ടൂൾസ് നിർവ്വചിക്കുന്നു
- ട്രാൻസ്പോർട്ട് കൈകാര്യം ചെയ്യാൻ stdio_server കോൺടെക്സ്‌റ്റ് മാനേജർ ഉപയോഗിക്കുന്നു

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

SSE-യിൽ നിന്നുള്ള പ്രധാന വ്യത്യാസങ്ങൾ stdio സർവറുകൾ:

- വെബ് സർവറുളള സെറ്റ് അപ്പ് അല്ലെങ്കിൽ HTTP എന്റ്പോയിന്റുകൾ ആവശ്യമില്ല
- ക്ലയന്റ് ഇവ ഉപപ്രക്രിയയായി ആരംഭിക്കുന്നു
- stdin/stdout സ്ട്രീമുകൾ വഴി ആശയവിനിമയം നടത്തുന്നു
- സിമ്പിളും ഡീബഗിംഗും എളുപ്പവുമാണ്

## അഭ്യാസം: stdio സർവർ സൃഷ്ടിക്കൽ

സർവർ സൃഷ്ടിക്കാനായി ശ്രദ്ധിക്കേണ്ട രണ്ട് കാര്യങ്ങൾ:

- കണക്ഷനും സന്ദേശങ്ങൾക്കും എന്റ്പോയിന്റുകൾ വെബ്സർവർ ഉപയോഗിച്ച് വെളിപ്പെടുത്തണം.
## ലാബ്: ലളിതമായ MCP stdio സർവർ സൃഷ്ടിക്കൽ

ഈ ലാബിൽ, ശുപാർശ ചെയ്ത stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് ലളിതമായ MCP സർവർ നിർമ്മിക്കും. ഈ സർവർ ക്ലയന്റുകൾക്ക് സ്റ്റാൻഡേർഡ് മോഡൽ കോൺടെക്‌സ്‌റ്റ് പ്രോട്ടോക്കോൾ ഉപയോഗിച്ച് വിളിക്കാവുന്ന ടൂൾസ് വെളിപ്പെടുത്തും.

### മുൻകൂട്ടി ആവശ്യങ്ങൾ

- Python 3.8 അല്ലെങ്കിൽ അതിനേതിലധികം
- MCP Python SDK: `pip install mcp`
- അസിങ്ക് പ്രോഗ്രാമിംഗിന്റെ അടിസ്ഥാന ബോധം

നമുക്ക് ആദ്യം MCP stdio സർവർ നിർമ്മിക്കാം:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# ലോഗിംഗ് ക്രമീകരിക്കുക
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# സെർവർ സൃഷ്ടിക്കുക
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
    # stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിക്കുക
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## SSE നിരാകരണത്തിൽ നിന്നുള്ള പ്രധാന വ്യത്യാസങ്ങൾ

**Stdio Transport (നിലവിലെ സ്റ്റാൻഡേർഡ്):**
- ലളിതമായ ഉപപ്രക്രിയ മാതൃക - ക്ലയന്റ് സർവറെ ഒരു ചൈൽഡ് പ്രോസസ്സായി ആരംഭിക്കുന്നു
- stdin/stdout വഴിയുള്ള JSON-RPC സന്ദേശങ്ങൾ വഴി ആശയവിനിമയം
- HTTP സർവർ സെറ്റ്-അപ്പ് ആവശ്യമില്ല
- മികച്ച പ്രകടനം, സുരക്ഷ
- എളുപ്പത്തിലുള്ള ഡീബഗ്, വികസനം

**SSE Transport (MCP 2025-06-18 മുതൽ നിരಾಕരിച്ചത്):**
- SSE എൻഡ്‌പോയിന്റുകളുള്ള HTTP സർവർ ആവശ്യമായിരുന്നു
- വെബ് സർവർ കുപ്പങ്ങളിൽ ജടിലമായ ക്രമീകരണം
- HTTP എൻഡ്‌പോയിന്റുകളിൽ അധിക സുരക്ഷാ പരിഗണനകൾ
- ഇപ്പോൾ Streamable HTTP-നോടെ മാറ്റി

### stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് സർവർ സൃഷ്ടിക്കൽ

stdio സർവർ സൃഷ്ടിക്കാൻ:

1. **ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്യുക** - MCP സർവർ ഘടകങ്ങളും stdio ട്രാൻസ്പോർട്ടും
2. **സർവർ ഉദാഹരണം сделать** - അതിന്റെ കഴിവുകൾ നിർവ്വചിക്കുക
3. **ടൂളുകൾ നിർവചിക്കുക** - വെളിപ്പെടുത്തേണ്ട പ്രവർത്തനങ്ങൾ ചേർക്കുക
4. **ട്രാൻസ്പോർട്ട് ക്രമീകരിക്കുക** - stdio ആശയവിനിമയം സജ്ജമാക്കുക
5. **സർവർ പ്രവർത്തിപ്പിക്കുക** - സർവർ ആരംഭിച്ച് സന്ദേശങ്ങൾ കൈകാര്യം ചെയ്യുക

നാം ഘട്ടം ഘട്ടമായി നിർമ്മിക്കാം:

### ഘട്ടം 1: ഒരു ലളിതമായ stdio സർവർ നിർമ്മിക്കുക

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ലോഗിംഗ് ക്രമീകരിക്കുക
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# സെർവർ സൃഷ്‌ടിക്കുക
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

### ഘട്ടം 2: കൂടുതൽ ടൂൾസ് ചേർക്കുക

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

### ഘട്ടം 3: സർവർ പ്രവർത്തിപ്പിക്കൽ

കോഡ് `server.py` എന്ന പേരിൽ സേവ് ചെയ്ത് കമാൻഡ് ലൈനിൽ നിന്ന് റൺ ചെയ്യുക:

```bash
python server.py
```

സർവർ തുടങ്ങുകയും stdin-ൽ നിന്ന് ഇൻപുട്ടിന് കാത്തിരിക്കുകയും ചെയ്യും. stdio ട്രാൻസ്പോർട്ട് വഴി JSON-RPC സന്ദേശങ്ങൾ ഉപയോഗിച്ച് ആശയവിനിമയം നടത്തുന്നു.

### ഘട്ടം 4: Inspector ഉപയോഗിച്ച് പരിശോധന

നിങ്ങളുടെ സർവർ MCP Inspector ഉപയോഗിച്ച് പരീക്ഷിക്കാം:

1. ഇൻസ്പെക്ടർ ഇൻസ്റ്റാൾ ചെയ്യുക: `npx @modelcontextprotocol/inspector`
2. ഇൻസ്പെക്ടർ റൺ ചെയ്ത് നിങ്ങളുടെ സർവറിലേക്ക് പോയിന്റ് ചെയ്യുക
3. നിങ്ങൾ സൃഷ്ടിച്ച ടൂളുകൾ പരീക്ഷിക്കുക

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## നിങ്ങളുടെ stdio സർവർ ഡീബഗ് ചെയ്യുക

### MCP Inspector ഉപയോഗിച്ച്

MCP Inspector MCP സർവറുകൾ ഡീബഗിംഗിനും പരീക്ഷണത്തിനും ഉപയോഗിക്കാൻ വലിയ ടൂൾ ആണ്. stdio സർവർ ഉപയോഗിക്കുന്ന വിധം:

1. **ഇൻസ്പെക്ടർ ഇൻസ്റ്റാൾ ചെയ്യുക**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **ഇൻസ്പെക്ടർ റൺ ചെയ്യുക**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **സർവർ പരീക്ഷിക്കുക**: ഇൻസ്പെക്ടർ സൃഷ്ടിച്ച ഒരു വെബ് ഇന്റർഫേസ് നൽകുന്നു, അതിൽ നിങ്ങൾക്ക്:
   - സർവർ കഴിവുകൾ കാണാം
   - വ്യത്യസ്ത പാരാമീറ്ററുകളോടെ ടൂളുകൾ പരീക്ഷിക്കാം
   - JSON-RPC സന്ദേശങ്ങൾ നിരീക്ഷിക്കാം
   - കണക്ഷൻ പ്രശ്നങ്ങൾ ഡീബഗ് ചെയ്യാം

### VS Code ഉപയോഗിച്ച്

VS Code-ൽ നേരിട്ട് MCP സർവർ ഡീബഗ് ചെയ്യാം:

1. `.vscode/launch.json` എന്നിൽ ലോഞ്ച് കോൺഫിഗറേഷൻ സൃഷ്ടിക്കുക:
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

2. സർവർ കോഡിൽ ബ്രേക്ക്പോയിന്റുകൾ സജ്ജമാക്കുക
3. ഡീബഗർ റൺ ചെയ്ത് ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് പരീക്ഷിക്കുക

### സാധാരണ ഡീബഗ് ടിപ്പുകൾ

- ലോഗിംഗിന് `stderr` ഉപയോഗിക്കുന്നതു മാത്രം, MCP സന്ദേശങ്ങൾക്ക് `stdout` ഒരിക്കൽ മുട്ടരുത്
- എല്ലാ JSON-RPC സന്ദേശങ്ങൾ newline-ൽ വേർതിരിച്ചിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക
- മുൻപ് ലളിതമായ ടൂളുകൾ പരീക്ഷിച്ച് ശേഷം സങ്കീർണ്ണ പ്രവർത്തനങ്ങൾ ചേർക്കുക
- സന്ദേശ ഫോർമാറ്റ് ശരിയാണെന്ന് ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് സ്ഥിരീകരിക്കുക

## VS Code-ൽ നിങ്ങളുടെ stdio സർവർ ഉപയോഗിക്കുക

stdio MCP സർവർ നിർമ്മിച്ചതിന് ശേഷം, ഇത് VS Code-സഹിതം സംയോജിപ്പിച്ച് Claude അല്ലെങ്കിൽ മറ്റ് MCP-സഹോദര ക്ലയന്റുകളുമായി ഉപയോഗിക്കാം.

### ക്രമീകരണം

1. MCP ക്രമീകരണ ഫയൽ `%APPDATA%\Claude\claude_desktop_config.json` (Windows) അല്ലെങ്കിൽ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) ൽ സൃഷ്ടിക്കുക:

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

2. Claude പുനരാരംഭിക്കുക: പുതിയ സെർവർ ക്രമീകരണം ലോഡ് ചെയ്യാൻ Claude വീണ്ടും തുറക്കുക.

3. കണക്ഷൻ പരിശോധിക്കുക: Claude-യോട് സംഭാഷണം തുടങ്ങി നിങ്ങളുടെ സർവറിന്റെ ടൂളുകൾ പരീക്ഷിക്കുക:
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### ടൈപ്‌സ്‌ക്രിപ്റ്റ് stdio സർവർ ഉദാഹരണം

കൂടുതൽ റഫറൻസിനായി പൂർണ്ണ ടൈപ്‌സ്‌ക്രിപ്റ്റ് ഉദാഹരണം:

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

// ഉപകരണങ്ങൾ ചേർക്കുക
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

### .NET stdio സർവർ ഉദാഹരണം

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

## സംഗ്രഹം

ഈ പുതുക്കിയ പാഠത്തിൽ നിങ്ങൾ പഠിച്ചത്:

- നിലവിലെ **stdio ട്രാൻസ്പോർട്ട്** ഉപയോഗിച്ച് MCP സർവറുകൾ നിർമ്മിക്കാൻ (ശുപാർശ ചെയ്യപ്പെടുന്ന സമീപനം)
- SSE ട്രാൻസ്പോർട്ട് stdio, Streamable HTTP-നോടുള്ള അവസാനിച്ചു പോയതിന്റെ കാരണം മനസിലാക്കാൻ
- MCP ക്ലയന്റുകൾ വിളിക്കാൻ കഴിവുള്ള ടൂളുകൾ സൃഷ്ടിക്കാൻ
- MCP Inspector ഉപയോഗിച്ച് സർവർ ഡീബഗ് ചെയ്യാൻ
- stdio സർവർ VS Code, Claude-യുമായി സംയോജിപ്പിക്കാം

stdio ട്രാൻസ്പോർട്ട് പഴയ SSE സമീപനത്തോടു താരതമ്യമായും ലളിതവും സുരക്ഷിതവുമും കൂടുതൽ കാര്യക്ഷമവുമാണ് MCP സർവർ നിർമ്മിക്കാൻ. 2025-06-18 സവിശേഷത പ്രകാരം MCP സർവർ നടപ്പിലാക്കലുകളുടെ ഭാഗമായി ഇതാണ് ശുപാർശ.

### .NET

1. ആദ്യം നാം ചില ടൂളുകൾ സൃഷ്ടിക്കാം, ഇതിന് *Tools.cs* എന്ന ഫയലിൽ താഴെയുള്ള ഉള്ളടക്കം ചേർക്കുക:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## അഭ്യാസം: നിങ്ങളുടെ stdio സർവർ പരീക്ഷിക്കൽ

ഇപ്പോൾ നിങ്ങൾ നിർമ്മിച്ച stdio സർവർ ശരിയായി പ്രവർത്തിക്കുന്നുണ്ടോ എന്നും പരിശോധിക്കാം.

### മുൻകൂട്ടി ആവശ്യങ്ങൾ

1. MCP Inspector ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. നിങ്ങളുടെ സർവർ കോഡ് സേവ് ചെയ്തിട്ടുണ്ടാകണം (ഉദാ., `server.py`)

### ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് പരിശോധന

1. **സർവറുമായി ഇൻസ്പെക്ടർ ആരംഭിക്കുക**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **വെബ് ഇന്റർഫേസ് തുറക്കുക**: ഇൻസ്പെക്ടർ നിങ്ങളുടെ സർവറിന്റെ കഴിവുകൾ കാണിക്കുന്ന ഒരു ബ്രൗസർ വിൻഡോ തുറക്കും.

3. **ടൂളുകൾ പരീക്ഷിക്കുക**: 
   - വ്യത്യസ്ത പേരുകളുമായി `get_greeting` ടൂൾ പരീക്ഷിക്കുക
   - വിവിധ സംഖ്യകളുമായി `calculate_sum` പരീക്ഷിക്കുക
   - `get_server_info` ടൂൾ വിളിച്ച് സർവർ മെറ്റാഡേറ്റ കാഴ്ചവെക്കുക

4. **ആശയവിനിമയം നിരീക്ഷിക്കുക**: ഇൻസ്പെക്ടർ ക്ലയന്റും സർവരും തമ്മിലുള്ള JSON-RPC സന്ദേശങ്ങൾ കാണിക്കും.

### നിങ്ങൾ കാണേണ്ടത്

സർവർ ശരിയായി തുടക്കമാകുമ്പോൾ നിങ്ങൾ കാണാൻ പോവുന്നത്:

- ഇൻസ്പെക്ടറിൽ സർവർ കഴിവുകൾ
- പരീക്ഷണങ്ങൾക്ക് ലഭ്യമായ ടൂളുകൾ
- വിജയകരമായ JSON-RPC സന്ദേശം എക്സ്‌ചേഞ്ചുകൾ
- ടൂൾ പ്രതികരണങ്ങൾ ഇന്റർഫേസിൽ പ്രദർശിപ്പിക്കൽ

### സാധാരണ പ്രശ്നങ്ങളും പരിഹാരങ്ങളും

**സർവർ തുടങ്ങുന്നില്ല:**
- എല്ലാ ആശ്രിതങ്ങളും ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് പരിശോധിക്കുക: `pip install mcp`
- Python വാക്യരീതി, ഇൻഡെന്റേഷൻ പരിശോധിക്കുക
- കൺസോൾ എറർ സന്ദേശങ്ങൾ നോക്കുക

**ടൂളുകൾ കാണിക്കുന്നില്ല:**
- `@server.tool()` ഡെക്കറേറ്ററുകൾ ഉള്ളതായി ഉറപ്പാക്കുക
- `main()` മുൻപ് ടൂൾ ഫങ്ഷനുകൾ നിർവചിച്ചിട്ടുണ്ടെന്നും പരിശോധിക്കുക
- സർവർ ശരിയായി കോൺഫിഗർ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക

**കണക്ഷൻ പ്രശ്നങ്ങൾ:**
- stdio ട്രാൻസ്പോർട്ട് ശരിയായി ഉപയോഗിക്കുന്നുണ്ടെന്ന് ഉറപ്പാക്കുക
- മറ്റ് പ്രോസസുകൾ തടസമാകാതെ പ്രവർത്തിക്കുന്നുണ്ടോ പരിശോധിക്കുക
- ഇൻസ്പെക്ടർ കമാൻഡ് വാക്ക് ശരിയാണെന്ന് ഉറപ്പാക്കുക

## അസൈൻമെന്റ്

നിങ്ങളുടെ സർവർ കൂടുതൽ കഴിവുകൾ വർദ്ധിപ്പിക്കാനായി ശ്രമിക്കുക. ഉദാ. ഒരു ടൂൾ API വിളിക്കുന്നതിലൂടെയുള്ള സൃഷ്ടികൾക്ക് [ ഈ പേജ്](https://api.chucknorris.io/) കാണുക. സർവർ എങ്ങനെയിരിക്കുമെന്ന് നിങ്ങൾ തീരുമാനിക്കുക. സന്തോഷമുള്ള പ്രവർത്തനം :)

## പരിഹാരം

[പരിഹാരം](./solution/README.md) പ്രവർത്തിക്കുന്ന കോഡോടെ ഒരു സാധ്യമായ പരിഹാരം ഇവിടെ ഉണ്ട്.

## പ്രധാന പഠനങ്ങൾ

ഈ അദ്ധ്യായത്തിൽ നിന്നുള്ള പ്രധാന പഠനങ്ങൾ:

- പ്രാദേശിക MCP സർവറുകൾക്ക് stdio ട്രാൻസ്പോർട്ട് ശുപാർശ ചെയ്യപ്പെടുന്ന മെക്കാനിസമാണ്.
- stdio ട്രാൻസ്പോർട്ട് MCP സർവറുകളും ക്ലയന്റുകളും സ്റ്റാൻഡേർഡ് ഇൻപുട്ടും ഔട്ട്പുട്ടും സ്ട്രീമുകൾ ഉപയോഗിച്ച് മന്ദഗതിയില്ലാതെ ആശയവിനിമയം അനുവദിക്കുന്നു.
- stdio സർവറുകൾ നേരിട്ട് ഉപയോഗിക്കാൻ Inspector, Visual Studio Code എന്നിവ ഉപയോഗിക്കാം, അതിനാൽ ഡീബഗ്, സംയോജനം എളുപ്പമാണ്.

## സാമ്പിൾസ്

- [ജാവ കാൽക്കുലേറ്റർ](../samples/java/calculator/README.md)
- [.Net കാൽക്കുലേറ്റർ](../../../../03-GettingStarted/samples/csharp)
- [ജാവാസ്ക്രിപ്റ്റ് കാൽക്കുലേറ്റർ](../samples/javascript/README.md)
- [ടൈപ്‌സ്‌ക്രിപ്റ്റ് കാൽക്കുലേറ്റർ](../samples/typescript/README.md)
- [പൈതൺ കാൽക്കുലേറ്റർ](../../../../03-GettingStarted/samples/python)

## അധിക ഉറവിടങ്ങൾ

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## അടുത്തത്

## അടുത്ത പടികൾ

ഇപ്പോള് stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സർവറുകൾ നിർമ്മിക്കാൻ പഠിച്ചതിനാൽ, കൂടുതൽ പുരോഗമന വിഷയങ്ങൾക്കായി:

- **അടുത്തത്**: [HTTP Streaming with MCP (Streamable HTTP)](../06-http-streaming/README.md) - ദൂരസർവറുകൾക്കായി പിന്തുണയ്‌ക്കുന്ന മറ്റു ട്രാൻസ്പോർട്ട് മെക്കാനിസത്തെ കുറിച്ച് പഠിക്കുക
- **അഡ്വാൻസ്**: [MCP Security Best Practices](../../02-Security/README.md) - MCP സർവറുകളിൽ സുരക്ഷ നടപ്പിലാക്കുക
- **പ്രൊഡക്ഷൻ**: [Deployment Strategies](../09-deployment/README.md) - നിങ്ങളുടെ സർവർകൾ പ്രൊഡക്ഷൻ ഉപയോഗത്തിനായി പ്രയോഗിക്കുക

## അധിക ഉറവിടങ്ങൾ

- [MCP സവിശേഷത 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - ഔദ്യോഗിക സവിശേഷത
- [MCP SDK ഡോക്യുമെന്റേഷൻ](https://github.com/modelcontextprotocol/sdk) - എല്ലാ ഭാഷകളുടെയും SDK റഫറൻസുകൾ
- [സമൂഹ ഉദാഹരണങ്ങൾ](../../06-CommunityContributions/README.md) - സമൂഹത്തിന്റെ കൂടുതൽ സർവർ ഉദാഹരണങ്ങൾ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസംബന്ധിത കുറിപ്പ്**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. നൂതനത്വത്തിനായി ഞങ്ങൾ ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയമേവമായ വിവർത്തനങ്ങളിൽ പിശകുകളും അശുദ്ധികളും ഉണ്ടാകാവുന്നതാണ്. മൂല ഭാഷയിലുള്ള പ്രധാന രേഖയാണ് സവിശേഷമായ ഉറപ്പ് ലഭിക്കുന്ന ഉറവിടം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം നിർദേശം ചെയ്യുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതൊരു തെറ്റിദ്ധാരണകൾക്കും അല്ലെങ്കിൽ തെറ്റായി വ്യാഖ്യാനിക്കുന്നതിനും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->