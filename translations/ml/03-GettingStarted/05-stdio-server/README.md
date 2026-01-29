# MCP സെർവർ stdio ട്രാൻസ്പോർട്ടുമായി

> **⚠️ പ്രധാന അപ്ഡേറ്റ്**: MCP സ്പെസിഫിക്കേഷൻ 2025-06-18 മുതൽ, സ്റ്റാൻഡ്എലോൺ SSE (സെർവർ-സെന്റ് ഇവന്റ്സ്) ട്രാൻസ്പോർട്ട് **ഡിപ്രിക്കേറ്റുചെയ്തു** "Streamable HTTP" ട്രാൻസ്പോർട്ടിലൂടെ മാറ്റി. നിലവിലെ MCP സ്പെസിഫിക്കേഷൻ രണ്ട് പ്രധാന ട്രാൻസ്പോർട്ട് മെക്കാനിസങ്ങൾ നിർവചിക്കുന്നു:
> 1. **stdio** - സ്റ്റാൻഡേർഡ് ഇൻപുട്ട്/ഔട്ട്പുട്ട് (പ്രാദേശിക സെർവറുകൾക്കായി ശുപാർശ ചെയ്യുന്നു)
> 2. **Streamable HTTP** - SSE ഉൾക്കൊള്ളുന്ന ദൂരസർവറുകൾക്കായി
>
> ഈ പാഠം **stdio ട്രാൻസ്പോർട്ടിൽ** കേന്ദ്രീകരിച്ച് അപ്ഡേറ്റ് ചെയ്തിരിക്കുന്നു, ഇത് MCP സെർവർ നടപ്പാക്കലുകൾക്കായി ശുപാർശ ചെയ്യപ്പെടുന്ന സമീപനമാണ്.

stdio ട്രാൻസ്പോർട്ട് MCP സെർവറുകൾക്ക് ക്ലയന്റുകളുമായി സ്റ്റാൻഡേർഡ് ഇൻപുട്ട്, ഔട്ട്പുട്ട് സ്ട്രീമുകൾ വഴി ആശയവിനിമയം നടത്താൻ അനുവദിക്കുന്നു. ഇത് നിലവിലെ MCP സ്പെസിഫിക്കേഷനിൽ ഏറ്റവും സാധാരണവും ശുപാർശ ചെയ്യപ്പെട്ട ട്രാൻസ്പോർട്ട് മെക്കാനിസമാണ്, വിവിധ ക്ലയന്റ് ആപ്ലിക്കേഷനുകളുമായി എളുപ്പത്തിൽ സംയോജിപ്പിക്കാൻ സാധിക്കുന്ന ലളിതവും കാര്യക്ഷമവുമായ MCP സെർവർ നിർമ്മാണ മാർഗമാണ്.

## അവലോകനം

stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സെർവർ നിർമ്മിക്കുകയും ഉപയോഗിക്കുകയും ചെയ്യുന്നതിനെക്കുറിച്ച് ഈ പാഠം വിശദീകരിക്കുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ പാഠം അവസാനിക്കുമ്പോൾ, നിങ്ങൾക്ക് സാധിക്കും:

- stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സെർവർ നിർമ്മിക്കുക.
- MCP സെർവർ ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് ഡീബഗ് ചെയ്യുക.
- Visual Studio Code ഉപയോഗിച്ച് MCP സെർവർ ഉപഭോഗം ചെയ്യുക.
- നിലവിലെ MCP ട്രാൻസ്പോർട്ട് മെക്കാനിസങ്ങൾ മനസിലാക്കുക, stdio ശുപാർശ ചെയ്യപ്പെടുന്നതിന്റെ കാരണം അറിയുക.

## stdio ട്രാൻസ്പോർട്ട് - ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു

stdio ട്രാൻസ്പോർട്ട് നിലവിലെ MCP സ്പെസിഫിക്കേഷനിൽ (2025-06-18) പിന്തുണയ്ക്കുന്ന രണ്ട് ട്രാൻസ്പോർട്ട് തരംകളിൽ ഒന്നാണ്. ഇത് എങ്ങനെ പ്രവർത്തിക്കുന്നു:

- **ലളിതമായ ആശയവിനിമയം**: സെർവർ സ്റ്റാൻഡേർഡ് ഇൻപുട്ട് (`stdin`) വഴി JSON-RPC സന്ദേശങ്ങൾ വായിക്കുകയും സ്റ്റാൻഡേർഡ് ഔട്ട്പുട്ട് (`stdout`) വഴി സന്ദേശങ്ങൾ അയയ്ക്കുകയും ചെയ്യുന്നു.
- **പ്രോസസ് അടിസ്ഥാനമാക്കിയുള്ളത്**: ക്ലയന്റ് MCP സെർവർ subprocess ആയി ആരംഭിക്കുന്നു.
- **സന്ദേശ ഫോർമാറ്റ്**: സന്ദേശങ്ങൾ വ്യക്തിഗത JSON-RPC അഭ്യർത്ഥനകൾ, അറിയിപ്പുകൾ, അല്ലെങ്കിൽ പ്രതികരണങ്ങൾ ആണ്, പുതിയ വരികളാൽ വേർതിരിച്ചിരിക്കുന്നു.
- **ലോഗിംഗ്**: സെർവർ ലോഗിംഗിനായി സ്റ്റാൻഡേർഡ് എറർ (`stderr`) UTF-8 സ്ട്രിംഗുകൾ എഴുതാം.

### പ്രധാന ആവശ്യകതകൾ:
- സന്ദേശങ്ങൾ പുതിയ വരികളാൽ വേർതിരിക്കണം, ഉൾക്കൊള്ളുന്ന പുതിയ വരികൾ ഉണ്ടായിരിക്കരുത്
- സെർവർ `stdout`-ലേക്ക് സാധുവായ MCP സന്ദേശമല്ലാത്ത ഒന്നും എഴുതരുത്
- ക്ലയന്റ് സെർവറിന്റെ `stdin`-ലേക്ക് സാധുവായ MCP സന്ദേശമല്ലാത്ത ഒന്നും എഴുതരുത്

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

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- MCP SDK-യിൽ നിന്ന് `Server` ക്ലാസ്, `StdioServerTransport` ഇറക്കുമതി ചെയ്യുന്നു
- അടിസ്ഥാന കോൺഫിഗറേഷൻ, കഴിവുകൾ ഉപയോഗിച്ച് സെർവർ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുന്നു

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# സെർവർ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക
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

മുൻകൂട്ടി നൽകിയ കോഡിൽ:

- MCP SDK ഉപയോഗിച്ച് സെർവർ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുന്നു
- ഡെക്കറേറ്ററുകൾ ഉപയോഗിച്ച് ടൂളുകൾ നിർവചിക്കുന്നു
- stdio_server കോൺടെക്സ്റ്റ് മാനേജർ ഉപയോഗിച്ച് ട്രാൻസ്പോർട്ട് കൈകാര്യം ചെയ്യുന്നു

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

SSE-യിൽ നിന്നുള്ള പ്രധാന വ്യത്യാസം stdio സെർവർ:

- വെബ് സെർവർ സെറ്റപ്പ് അല്ലെങ്കിൽ HTTP എൻഡ്‌പോയിന്റുകൾ ആവശ്യമില്ല
- ക്ലയന്റ് subprocess ആയി സെർവർ ആരംഭിക്കുന്നു
- stdin/stdout സ്ട്രീമുകൾ വഴി ആശയവിനിമയം നടത്തുന്നു
- ലളിതമായി നടപ്പിലാക്കാനും ഡീബഗ് ചെയ്യാനും കഴിയും

## അഭ്യാസം: stdio സെർവർ സൃഷ്ടിക്കൽ

നമ്മുടെ സെർവർ സൃഷ്ടിക്കാൻ, രണ്ട് കാര്യങ്ങൾ ശ്രദ്ധിക്കണം:

- കണക്ഷനും സന്ദേശങ്ങൾക്കും എൻഡ്‌പോയിന്റുകൾ വെബ് സെർവർ ഉപയോഗിച്ച് തുറക്കണം.

## ലാബ്: ലളിതമായ MCP stdio സെർവർ സൃഷ്ടിക്കൽ

ഈ ലാബിൽ, ശുപാർശ ചെയ്ത stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് ലളിതമായ MCP സെർവർ സൃഷ്ടിക്കും. ഈ സെർവർ ക്ലയന്റുകൾക്ക് സ്റ്റാൻഡേർഡ് മോഡൽ കോൺടെക്സ്റ്റ് പ്രോട്ടോക്കോൾ ഉപയോഗിച്ച് വിളിക്കാവുന്ന ടൂളുകൾ തുറക്കും.

### മുൻകൂട്ടി ആവശ്യമായവ

- Python 3.8 അല്ലെങ്കിൽ അതിനുശേഷം
- MCP Python SDK: `pip install mcp`
- അസിങ്ക്രൺ പ്രോഗ്രാമിംഗ് അടിസ്ഥാന അറിവ്

നമ്മുടെ ആദ്യ MCP stdio സെർവർ സൃഷ്ടിക്കാം:

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

## ഡിപ്രിക്കേറ്റുചെയ്ത SSE സമീപനത്തിൽ നിന്നുള്ള പ്രധാന വ്യത്യാസങ്ങൾ

**Stdio Transport (നിലവിലെ സ്റ്റാൻഡേർഡ്):**
- ലളിതമായ subprocess മോഡൽ - ക്ലയന്റ് സെർവർ ചൈൽഡ് പ്രോസസായി ആരംഭിക്കുന്നു
- JSON-RPC സന്ദേശങ്ങൾ ഉപയോഗിച്ച് stdin/stdout വഴി ആശയവിനിമയം
- HTTP സെർവർ സെറ്റപ്പ് ആവശ്യമില്ല
- മെച്ചപ്പെട്ട പ്രകടനം, സുരക്ഷ
- എളുപ്പത്തിൽ ഡീബഗ് ചെയ്യാനും വികസിപ്പിക്കാനും കഴിയും

**SSE Transport (MCP 2025-06-18 മുതൽ ഡിപ്രിക്കേറ്റുചെയ്തത്):**
- SSE എൻഡ്‌പോയിന്റുകളുള്ള HTTP സെർവർ ആവശ്യമായിരുന്നു
- വെബ് സെർവർ ഇൻഫ്രാസ്ട്രക്ചർ ഉപയോഗിച്ച് കൂടുതൽ സങ്കീർണ്ണമായ സെറ്റപ്പ്
- HTTP എൻഡ്‌പോയിന്റുകൾക്കുള്ള അധിക സുരക്ഷാ പരിഗണനകൾ
- വെബ് അടിസ്ഥാന സാഹചര്യങ്ങൾക്ക് Streamable HTTP-ൽ മാറ്റം

### stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് സെർവർ സൃഷ്ടിക്കൽ

stdio സെർവർ സൃഷ്ടിക്കാൻ:

1. **ആവശ്യമായ ലൈബ്രറികൾ ഇറക്കുമതി ചെയ്യുക** - MCP സെർവർ ഘടകങ്ങളും stdio ട്രാൻസ്പോർട്ടും
2. **സെർവർ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക** - കഴിവുകൾ നിർവചിച്ച് സെർവർ നിർമിക്കുക
3. **ടൂളുകൾ നിർവചിക്കുക** - തുറക്കേണ്ട ഫംഗ്ഷണാലിറ്റി ചേർക്കുക
4. **ട്രാൻസ്പോർട്ട് ക്രമീകരിക്കുക** - stdio ആശയവിനിമയം ക്രമീകരിക്കുക
5. **സെർവർ പ്രവർത്തിപ്പിക്കുക** - സെർവർ ആരംഭിച്ച് സന്ദേശങ്ങൾ കൈകാര്യം ചെയ്യുക

പടിപടിയായി നിർമ്മിക്കാം:

### ഘട്ടം 1: ലളിതമായ stdio സെർവർ സൃഷ്ടിക്കുക

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# ലോഗിംഗ് ക്രമീകരിക്കുക
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# സെർവർ സൃഷ്ടിക്കുക
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

### ഘട്ടം 2: കൂടുതൽ ടൂളുകൾ ചേർക്കുക

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

### ഘട്ടം 3: സെർവർ പ്രവർത്തിപ്പിക്കൽ

കോഡ് `server.py` എന്ന പേരിൽ സേവ് ചെയ്ത് കമാൻഡ് ലൈൻ നിന്ന് പ്രവർത്തിപ്പിക്കുക:

```bash
python server.py
```

സെർവർ ആരംഭിച്ച് stdin-ൽ നിന്ന് ഇൻപുട്ടിനായി കാത്തിരിക്കും. stdio ട്രാൻസ്പോർട്ട് വഴി JSON-RPC സന്ദേശങ്ങൾ ഉപയോഗിച്ച് ആശയവിനിമയം നടത്തുന്നു.

### ഘട്ടം 4: ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് പരിശോധന

നിങ്ങളുടെ സെർവർ MCP ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് പരിശോധിക്കാം:

1. ഇൻസ്പെക്ടർ ഇൻസ്റ്റാൾ ചെയ്യുക: `npx @modelcontextprotocol/inspector`
2. ഇൻസ്പെക്ടർ പ്രവർത്തിപ്പിച്ച് നിങ്ങളുടെ സെർവറിലേക്ക് പോയിന്റ് ചെയ്യുക
3. നിങ്ങൾ സൃഷ്ടിച്ച ടൂളുകൾ പരീക്ഷിക്കുക

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## നിങ്ങളുടെ stdio സെർവർ ഡീബഗ് ചെയ്യൽ

### MCP ഇൻസ്പെക്ടർ ഉപയോഗിച്ച്

MCP ഇൻസ്പെക്ടർ MCP സെർവർ ഡീബഗിംഗിനും പരിശോധനയ്ക്കും വിലപ്പെട്ട ഉപകരണം ആണ്. stdio സെർവറുമായി ഇത് എങ്ങനെ ഉപയോഗിക്കാമെന്ന് കാണാം:

1. **ഇൻസ്പെക്ടർ ഇൻസ്റ്റാൾ ചെയ്യുക**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **ഇൻസ്പെക്ടർ പ്രവർത്തിപ്പിക്കുക**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **സെർവർ പരീക്ഷിക്കുക**: ഇൻസ്പെക്ടർ വെബ് ഇന്റർഫേസ് നൽകുന്നു, ഇവിടെ നിങ്ങൾക്ക്:
   - സെർവർ കഴിവുകൾ കാണാം
   - വ്യത്യസ്ത പാരാമീറ്ററുകളോടെ ടൂളുകൾ പരീക്ഷിക്കാം
   - JSON-RPC സന്ദേശങ്ങൾ നിരീക്ഷിക്കാം
   - കണക്ഷൻ പ്രശ്നങ്ങൾ ഡീബഗ് ചെയ്യാം

### VS Code ഉപയോഗിച്ച്

നിങ്ങളുടെ MCP സെർവർ നേരിട്ട് VS Code-ൽ ഡീബഗ് ചെയ്യാം:

1. `.vscode/launch.json`-ൽ ലാഞ്ച് കോൺഫിഗറേഷൻ സൃഷ്ടിക്കുക:
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

2. സെർവർ കോഡിൽ ബ്രേക്ക്പോയിന്റുകൾ സജ്ജമാക്കുക
3. ഡീബഗർ പ്രവർത്തിപ്പിച്ച് ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് പരീക്ഷിക്കുക

### സാധാരണ ഡീബഗിംഗ് ടിപ്പുകൾ

- ലോഗിംഗിനായി `stderr` ഉപയോഗിക്കുക - MCP സന്ദേശങ്ങൾക്ക് `stdout` ഉപയോഗിക്കണം, അതിൽ ഒന്നും എഴുതരുത്
- എല്ലാ JSON-RPC സന്ദേശങ്ങളും പുതിയ വരികളാൽ വേർതിരിച്ചിരിക്കണം
- സങ്കീർണ്ണമായ ഫംഗ്ഷണാലിറ്റി ചേർക്കുന്നതിന് മുമ്പ് ലളിതമായ ടൂളുകൾ പരീക്ഷിക്കുക
- സന്ദേശ ഫോർമാറ്റുകൾ പരിശോധിക്കാൻ ഇൻസ്പെക്ടർ ഉപയോഗിക്കുക

## VS Code-ൽ നിങ്ങളുടെ stdio സെർവർ ഉപഭോഗം

stdio MCP സെർവർ നിർമ്മിച്ചതിന് ശേഷം, ഇത് VS Code-യുമായി സംയോജിപ്പിച്ച് Claude അല്ലെങ്കിൽ മറ്റ് MCP-സഹജമായ ക്ലയന്റുകളുമായി ഉപയോഗിക്കാം.

### കോൺഫിഗറേഷൻ

1. MCP കോൺഫിഗറേഷൻ ഫയൽ സൃഷ്ടിക്കുക `%APPDATA%\Claude\claude_desktop_config.json` (Windows) അല്ലെങ്കിൽ `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. Claude പുനരാരംഭിക്കുക: പുതിയ സെർവർ കോൺഫിഗറേഷൻ ലോഡ് ചെയ്യാൻ Claude അടച്ചു വീണ്ടും തുറക്കുക.

3. കണക്ഷൻ പരീക്ഷിക്കുക: Claude-യുമായി സംഭാഷണം ആരംഭിച്ച് നിങ്ങളുടെ സെർവർ ടൂളുകൾ ഉപയോഗിച്ച് ശ്രമിക്കുക:
   - "Can you greet me using the greeting tool?"
   - "Calculate the sum of 15 and 27"
   - "What's the server info?"

### TypeScript stdio സെർവർ ഉദാഹരണം

പരാമർശത്തിനായി സമ്പൂർണ്ണ TypeScript ഉദാഹരണം:

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

### .NET stdio സെർവർ ഉദാഹരണം

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

## സംഗ്രഹം

ഈ അപ്ഡേറ്റുചെയ്ത പാഠത്തിൽ, നിങ്ങൾ പഠിച്ചു:

- നിലവിലെ **stdio ട്രാൻസ്പോർട്ട്** ഉപയോഗിച്ച് MCP സെർവർ നിർമ്മിക്കുന്നത് (ശുപാർശ ചെയ്ത സമീപനം)
- SSE ട്രാൻസ്പോർട്ട് stdio, Streamable HTTP എന്നിവയ്ക്ക് പകരം ഡിപ്രിക്കേറ്റുചെയ്തതിന്റെ കാരണം
- MCP ക്ലയന്റുകൾ വിളിക്കാവുന്ന ടൂളുകൾ സൃഷ്ടിക്കുക
- MCP ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് സെർവർ ഡീബഗ് ചെയ്യുക
- VS Code, Claude എന്നിവയുമായി stdio സെർവർ സംയോജിപ്പിക്കുക

stdio ട്രാൻസ്പോർട്ട് ഡിപ്രിക്കേറ്റുചെയ്ത SSE സമീപനത്തേക്കാൾ ലളിതവും സുരക്ഷിതവുമായും കാര്യക്ഷമവുമായ MCP സെർവർ നിർമ്മാണ മാർഗമാണ്. 2025-06-18 സ്പെസിഫിക്കേഷനിൽ ഇത് MCP സെർവർ നടപ്പാക്കലുകൾക്കായി ശുപാർശ ചെയ്യപ്പെടുന്ന ട്രാൻസ്പോർട്ടാണ്.

### .NET

1. ആദ്യം ചില ടൂളുകൾ സൃഷ്ടിക്കാം, ഇതിന് *Tools.cs* എന്ന ഫയൽ താഴെപ്പറയുന്ന ഉള്ളടക്കത്തോടെ സൃഷ്ടിക്കുക:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## അഭ്യാസം: നിങ്ങളുടെ stdio സെർവർ പരീക്ഷിക്കൽ

stdio സെർവർ നിർമ്മിച്ചതിനുശേഷം, അത് ശരിയായി പ്രവർത്തിക്കുന്നുണ്ടോ എന്ന് പരിശോധിക്കാം.

### മുൻകൂട്ടി ആവശ്യമായവ

1. MCP ഇൻസ്പെക്ടർ ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. നിങ്ങളുടെ സെർവർ കോഡ് സേവ് ചെയ്തിട്ടുണ്ടാകണം (ഉദാ: `server.py`)

### ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് പരിശോധന

1. **സെർവറുമായി ഇൻസ്പെക്ടർ ആരംഭിക്കുക**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **വെബ് ഇന്റർഫേസ് തുറക്കുക**: ഇൻസ്പെക്ടർ ബ്രൗസർ വിൻഡോ തുറന്ന് സെർവറിന്റെ കഴിവുകൾ കാണിക്കും.

3. **ടൂളുകൾ പരീക്ഷിക്കുക**:
   - വ്യത്യസ്ത പേരുകളോടെ `get_greeting` ടൂൾ പരീക്ഷിക്കുക
   - വിവിധ സംഖ്യകളോടെ `calculate_sum` ടൂൾ പരീക്ഷിക്കുക
   - സെർവർ മെറ്റാഡേറ്റ കാണാൻ `get_server_info` ടൂൾ വിളിക്കുക

4. **ആശയവിനിമയം നിരീക്ഷിക്കുക**: ഇൻസ്പെക്ടർ ക്ലയന്റും സെർവറും തമ്മിലുള്ള JSON-RPC സന്ദേശങ്ങൾ കാണിക്കുന്നു.

### നിങ്ങൾ കാണേണ്ടത്

സെർവർ ശരിയായി ആരംഭിച്ചാൽ, നിങ്ങൾ കാണും:
- ഇൻസ്പെക്ടറിൽ സെർവർ കഴിവുകൾ പട്ടിക
- പരീക്ഷണത്തിന് ലഭ്യമായ ടൂളുകൾ
- വിജയകരമായ JSON-RPC സന്ദേശങ്ങൾ കൈമാറ്റം
- ഇന്റർഫേസിൽ ടൂൾ പ്രതികരണങ്ങൾ

### സാധാരണ പ്രശ്നങ്ങളും പരിഹാരങ്ങളും

**സെർവർ ആരംഭിക്കുന്നില്ല:**
- എല്ലാ ഡിപ്പൻഡൻസികളും ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് പരിശോധിക്കുക: `pip install mcp`
- Python സിന്റാക്സ്, ഇൻഡെന്റേഷൻ പരിശോധിക്കുക
- കൺസോളിൽ പിഴവ് സന്ദേശങ്ങൾ നോക്കുക

**ടൂളുകൾ കാണാനില്ല:**
- `@server.tool()` ഡെക്കറേറ്ററുകൾ ഉണ്ടെന്ന് ഉറപ്പാക്കുക
- ടൂൾ ഫംഗ്ഷനുകൾ `main()`-നു മുമ്പ് നിർവചിച്ചിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുക
- സെർവർ ശരിയായി കോൺഫിഗർ ചെയ്തിട്ടുണ്ടോ എന്ന് പരിശോധിക്കുക

**കണക്ഷൻ പ്രശ്നങ്ങൾ:**
- സെർവർ stdio ട്രാൻസ്പോർട്ട് ശരിയായി ഉപയോഗിക്കുന്നുണ്ടോ എന്ന് ഉറപ്പാക്കുക
- മറ്റ് പ്രോസസുകൾ തടസ്സം സൃഷ്ടിക്കുന്നില്ലെന്ന് പരിശോധിക്കുക
- ഇൻസ്പെക്ടർ കമാൻഡ് സിന്റാക്സ് ശരിയാണോ എന്ന് പരിശോധിക്കുക

## അസൈൻമെന്റ്

നിങ്ങളുടെ സെർവർ കൂടുതൽ കഴിവുകൾ ചേർത്ത് വികസിപ്പിക്കാൻ ശ്രമിക്കുക. ഉദാഹരണത്തിന്, [ഈ പേജ്](https://api.chucknorris.io/) കാണുക, ഒരു API വിളിക്കുന്ന ടൂൾ ചേർക്കാം. സെർവർ എങ്ങനെ കാണണം എന്ന് നിങ്ങൾ തീരുമാനിക്കുക. സന്തോഷത്തോടെ പ്രവർത്തിക്കുക :)

## പരിഹാരം

[പരിഹാരം](./solution/README.md) പ്രവർത്തനക്ഷമമായ കോഡോടുകൂടിയ ഒരു പരിഹാരമാണ്.

## പ്രധാന കാര്യങ്ങൾ

ഈ അധ്യായത്തിൽ നിന്നുള്ള പ്രധാന കാര്യങ്ങൾ:

- പ്രാദേശിക MCP സെർവറുകൾക്കായി stdio ട്രാൻസ്പോർട്ട് ശുപാർശ ചെയ്യപ്പെടുന്ന മെക്കാനിസമാണ്.
- stdio ട്രാൻസ്പോർട്ട് MCP സെർവറുകളും ക്ലയന്റുകളും സ്റ്റാൻഡേർഡ് ഇൻപുട്ട്, ഔട്ട്പുട്ട് സ്ട്രീമുകൾ ഉപയോഗിച്ച് സുതാര്യമായ ആശയവിനിമയം അനുവദിക്കുന്നു.
- stdio സെർവർ നേരിട്ട് ഉപഭോഗിക്കാൻ ഇൻസ്പെക്ടറും Visual Studio Code-ഉം ഉപയോഗിക്കാം, ഇത് ഡീബഗിംഗും സംയോജനവും എളുപ്പമാക്കുന്നു.

## സാമ്പിളുകൾ

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## അധിക വിഭവങ്ങൾ

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## അടുത്തത്

## അടുത്ത ഘട്ടങ്ങൾ

stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സെർവർ നിർമ്മിക്കുന്നത് പഠിച്ചതിനുശേഷം, കൂടുതൽ പ്രഗത്ഭ വിഷയങ്ങൾ അന്വേഷിക്കാം:

- **അടുത്തത്**: [MCP-യുമായി HTTP Streaming (Streamable HTTP)](../06-http-streaming/README.md) - ദൂരസർവറുകൾക്കായി പിന്തുണയ്ക്കുന്ന മറ്റൊരു ട്രാൻസ്പോർട്ട് മെക്കാനിസം പഠിക്കുക
- **പ്രഗത്ഭം**: [MCP സുരക്ഷാ മികച്ച പ്രാക്ടീസുകൾ](../../02-Security/README.md) - MCP സെർവറുകളിൽ സുരക്ഷ നടപ്പിലാക്കുക
- **പ്രൊഡക്ഷൻ**: [ഡിപ്ലോയ്മെന്റ് തന്ത്രങ്ങൾ](../09-deployment/README.md) - പ്രൊഡക്ഷൻ ഉപയോഗത്തിനായി സെർവർ ഡിപ്ലോയ് ചെയ്യുക

## അധിക വിഭവങ്ങൾ

- [MCP സ്പെസിഫിക്കേഷൻ 2025-06-18](https://spec.modelcontextprotocol.io/specification/) -

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->