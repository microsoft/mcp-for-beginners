# MCP സെർവർ stdio ട്രാൻസ്പോർട്ടുമായി

> **⚠️ പ്രധാന അപ്‌ഡേറ്റ്**: MCP സ്പെസിഫിക്കേഷൻ 2025-06-18 മുതൽ, സ്റ്റാൻഡ്എലോൺ SSE (സർവർ-സെന്റ് ഇവന്റ്സ്) ട്രാൻസ്പോർട്ട് **അപ്രസക്തമാക്കി** മാറ്റി "Streamable HTTP" ട്രാൻസ്പോർട്ടിലൂടെ മാറ്റിയിട്ടുണ്ട്. നിലവിലെ MCP സ്പെസിഫിക്കേഷനിൽ രണ്ടു പ്രധാന ട്രാൻസ്പോർട്ട് മെക്കാനിസങ്ങളും നിർവചിച്ചിരിക്കുന്നു:
> 1. **stdio** - സ്റ്റാൻഡേർഡ് ഇൻപുട്ട്/ഔട്ട്‌പുട്ട് (വലൂർവൻ സർവറുകൾക്കായി ശുപാർശ ചെയ്യപ്പെടുന്നു)
> 2. **Streamable HTTP** - SSE ഉൾക്കൊള്ളുന്ന റിമോട്ട് സർവറുകൾക്കായി
>
> ഈ പാഠം നിലവിൽ ശുപാർശിക്കുന്ന **stdio ട്രാൻസ്പോർട്ടിൽ** കേന്ദ്രീകരിച്ചാണ് അപ്ഡേറ്റ് ചെയ്‌തിരിക്കുന്നത്, ഇത് MCP സെർവർ ഇംപ്ലിമെൻറേഷനുകളിൽ ഏറ്റവും ശുപാർശ ചെയ്യപ്പെടുന്ന മാർഗം ആണ്.

stdio ട്രാൻസ്പോർട്ട് MCP സർവറുകൾക്ക് സ്റ്റാൻഡേർഡ് ഇൻപുട്ട്-ഔട്ട്‌പുട്ട് സ്ട്രീമുകൾ മുഖേന ക്ലയന്റുക്കളുമായി സംവദിക്കാനുള്ള വഴി അനുവദിക്കുന്നു. ഇത് പുതിയ MCP സ്പെസിഫിക്കേഷനിൽ ഏറ്റവും വ്യാപകമായി ഉപയോഗിക്കുന്ന, ശുപാർശചെയ്‌ത ട്രാൻസ്പോർട്ട് സംവിധാനമാണ്, വ്യത്യസ്ത ക്ലയന്റ് ആപ്ലിക്കേഷനുകളുമായി എളുപ്പത്തിൽ ഇന്റഗ്രേറ്റ് ചെയ്യാവുന്ന സിംപിൾ, ഫലപ്രദമായ MCP സെർവർ നിർമാണം അനുവദിക്കുന്നു.

## അവലോകനം

ഈ പാഠത്തിൽ stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സെർവറുകൾ എങ്ങനെ നിർമ്മിക്കാമെന്നും ഉപയോഗിക്കാമെന്നും നോക്കാം.

## പഠനലക്‌ഷ്യങ്ങൾ

ഈ പാഠം പൂർത്തിയാകുമ്പോൾ, നിങ്ങൾക്ക് സാധിക്കുമെന്നും:

- stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് MCP സെർവർ നിർമ്മിക്കുക.
- MCP സെർവർ ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് ഡീബഗ് ചെയ്യുക.
- MCP സെർവർ Visual Studio Code ഉപയോഗിച്ച് ഉപയോഗിക്കുക.
- MCP ട്രാൻസ്പോർട്ട് മെക്കാനിസങ്ങൾ മനസ്സിലാക്കുക, stdio എന്തുകൊണ്ടാണ് ശുപാർശ ചെയ്യപ്പെടുന്നത് എന്നത് അറിയുക.

## stdio ട്രാൻസ്പോർട്ട് - പ്രവർത്തനവിധി

stdio ട്രാൻസ്പോർട്ട് MCP സ്പെസിഫിക്കേഷൻ (2025-06-18) പ്രകാരം പിന്തുണയുള്ള രണ്ട് ട്രാൻസ്പോർട്ട് ടൈപ്പുകളിൽ ഒന്നാണ്. ഇത് പ്രവർത്തിക്കുന്നത് ഇങ്ങനെ ആണ്:

- **സിംപിൾ കമ്മ്യൂണിക്കേഷൻ**: സെർവർ സ്റ്റാൻഡേർഡ് ഇൻപുട്ടിൽ (`stdin`) നിന്നും JSON-RPC സന്ദേശങ്ങൾ വായിച്ച്, സ്റ്റാൻഡേർഡ് ഔട്ട്‌പുട്ടിൽ (`stdout`) സന്ദേശങ്ങൾ അയയ്ക്കുന്നു.
- **പ്രോസസ്സ് അടിസ്ഥാനമായ**: ക്ലയന്റ് MCP സെർവർ subprocess ആയി ആരംഭിക്കുന്നു.
- **സന്ദേശ ഫോർമാറ്റ്**: സന്ദേശങ്ങൾ ഓരോ JSON-RPC അഭ്യർത്ഥനകൾ, നോട്ടിഫിക്കേഷനുകള്‍, മറുപടികൾ ഇവയും ഉൾക്കൊള്ളുന്നവ, newline-ലൂടെ വേർതിരிக்கப்பட்டവ.
- **ലോഗിംഗ്**: സെർവർ ലോഗിംഗിനായി സ്റ്റാൻഡേർഡ് എററിൽ (`stderr`) UTF-8 സ്റ്റ്രിങുകൾ എഴുതി.

### പ്രധാന ആവശ്യകതകൾ:
- സന്ദേശങ്ങൾ newline-ലൂടെ വേർതിരിക്കണം, ഇണഞ്ഞ് newline-കൾ ഉള്ളത് അംഗീകരിക്കില്ല
- സാധുവായ MCP സന്ദേശം അല്ലാത്തത് `stdout`-ലേക്ക് സെർവർ എഴുതി മതിയാവില്ല
- സാധുവായ MCP സന്ദേശം അല്ലാത്തത് ക്ലയന്റ് സെർവർ `stdin`-ലേക്ക് എഴുതി മതിയാവില്ല

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

മീതെ കോഡിൽ:

- MCP SDK-യിൽ നിന്ന് `Server` ക്ലാസ്, `StdioServerTransport` ഇംപോർട്ട് ചെയ്യുന്നു
- അടിസ്ഥാന കോൺഫിഗറേഷനും ശേഷിപ്പും ഉപയോഗിച്ച് സെർവർ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുന്നു

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# സർവർ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക
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

മീതെ കോഡിൽ:

- MCP SDK ഉപയോഗിച്ച് സെർവർ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുന്നു
- ഡെക്കറേറ്ററുകൾ ഉപയോഗിച്ച് ടൂൾസ് നിർവചിക്കുന്നു
- stdio_server context manager വഴി ട്രാൻസ്പോർട്ട് കൈകാര്യം ചെയ്യുന്നു

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

SSE-ലയുള്ള പ്രധാന വ്യത്യാസം stdio സെർവറുകളിൽ:

- വെബ് സർവർ സെറ്റ് അപ്പ് അല്ലെങ്കിൽ HTTP എൻഡ്പോയിന്റ് ആവശ്യമില്ല
- ക്ലയന്റ് subprocess ആയി സെർവർ ആരംഭിക്കുന്നു
- stdin/stdout സ്ട്രീമുകളിലൂടെ ആശയവിനിമയം നടക്കുന്നു
- ഡെവലപ്‌മെൻറും ഡീബഗ്ഗിംഗും ലളിതം

## അഭ്യാസം: stdio സെർവർ സൃഷ്ടിക്കൽ

സെർവർ സൃഷ്ടിക്കാൻ താഴെ രണ്ട് കാര്യങ്ങൾ ശ്രദ്ധിക്കുക:

- കണക്ഷനും സന്ദേശങ്ങൾക്കും എൻഡ്പോയിന്റുകൾ വെബ്ബ് സർവർ ഉപയോഗിച്ച് പുറത്തുവിടേണ്ടതുണ്ട്.

## ലാബ്: സിമ്പിൾ MCP stdio സെർവർ സൃഷ്ടിക്കൽ

ഈ ലാബിൽ, ശുപാർശചെയ്‌ത stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് ഒരു ലളിതമായ MCP സെർവർ സൃഷ്ടിക്കും. ഈ സെർവർ ക്ലയന്റുകൾക്ക് സ്റ്റാൻഡേർഡ് മോഡൽ കോൺടെക്‌സ്്റ്റ് പ്രോട്ടോക്കോൾ ഉപയോഗിച്ച് വിളിക്കാവുന്ന ടൂൾസ് പുറത്ത് വെക്കും.

### മുൻകൂട്ടി ആവശ്യമായത്

- Python 3.8 അല്ലെങ്കിൽ അതിലധികം വേർഷൻ  
- MCP Python SDK: `pip install mcp`  
- async പ്രോഗ്രാമിംഗിന്റെ അടിസ്ഥാന ധാരണ

നമുക്കു് ആദ്യ MCP stdio സെർവർ സൃഷ്ടിക്കുക:

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

## സ്ഥിരം SSE സമീപനത്തിൽ നിന്നുള്ള പ്രധാന വ്യത്യാസങ്ങൾ

**Stdio ട്രാൻസ്പോർട്ട് (ഇപ്പോഴത്തെ സ്റ്റാൻഡേർഡ്):**  
- ലളിതമായ subprocess മോഡൽ - ക്ലയന്റ് സെർവർ subprocess ആയി ആരംഭിക്കുന്നു  
- JSON-RPC സന്ദേശങ്ങൾ ഉപയോഗിച്ച് stdin/stdout സന്ദേശം കൈമാറ്റം  
- HTTP സെർവർ സെറ്റ് അപ് ആവശ്യമില്ല  
- മെച്ചപ്പെട്ട പ്രകടനം, സുരക്ഷ  
- സുഗമമായ ഡീബഗ്ഗും ഡെവലപ്‌മെൻറും  

**SSE ട്രാൻസ്പോർട്ട് (MCP 2025-06-18 ന് അപ്രസക്തമാക്കി):**  
- SSE എൻഡ്പോയിന്റുകളുള്ള HTTP സെർവർ ആവശ്യമാണ്  
- കൂടുതൽ സങ്കീര്‍ണമായ വെബ് സർവർ ഇൻഫ്രാസ്റ്റ്രുക്ചർ  
- HTTP എൻഡ്പോയിന്റുകള്ക്ക് അധിക സുരക്ഷാ പരിഗണനകൾ  
- വെബ് അധിഷ്ഠിത സാഹചര്യങ്ങൾക്ക് Streamable HTTP-ൽ പുനഃസ്ഥാപിച്ചു

### stdio ട്രാൻസ്പോർട്ട് ഉപയോഗിച്ച് സെർവർ സൃഷ്ടിക്കൽ

stdio സെർവർ സൃഷ്ടിക്കാൻ:

1. ആവശ്യമായ ലൈബ്രറികൾ ഇംപോർട്ട് ചെയ്യുക - MCP സെർവർ ഘടകങ്ങളും stdio ട്രാൻസ്പോർട്ടും  
2. സെർവർ ഇൻസ്റ്റൻസ് സൃഷ്ടിക്കുക - ശേഷിപ്പുകളുമായി സെർവർ നിർവചിക്കുക  
3. ടൂൾസ് നിർവചിക്കുക - പുറത്ത് വെക്കാനുള്ള ഫംഗ്ഷനാലിറ്റി കൂടി കൂട്ടിച്ചേർക്കുക  
4. ട്രാൻസ്പോർട്ട് സജ്ജമാക്കുക - stdio കമ്മ്യൂണിക്കേഷൻ കോൺഫിഗർ ചെയ്യുക  
5. സെർവർ റൺ ചെയ്യുക - സെർവർ ആരംഭിച്ച് സന്ദേശങ്ങൾ കൈകാര്യം ചെയ്യുക  

നമുക്ക് പടിയടിയായി നിർമാണം നടത്താം:

### ഘട്ടം 1: അടിസ്ഥാന stdio സെർവർ സൃഷ്ടിക്കൽ

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

### ഘട്ടം 3: സെർവർ റൺ ചെയ്യൽ

കോഡ് `server.py` എന്നായി സേവ് ചെയ്ത് കമാൻഡ് ലൈൻ വഴി പ്രവർത്തിപ്പിക്കുക:

```bash
python server.py
```

സെർവർ ആരംഭിച്ച് stdin നിന്നുള്ള ഇൻപുട്ടിനായി കാത്തിരിക്കും. stdio ട്രാൻസ്പോർട്ട് വഴി JSON-RPC സന്ദേശങ്ങൾ ഉപയോഗിച്ച് ആശയവിനിമയം നടത്തുന്നു.

### ഘട്ടം 4: ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് ടെസ്റ്റിങ്

MCP ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് നിങ്ങളുടെ സെർവർ പരീക്ഷിക്കാം:

1. ഇൻസ്പെക്ടർ ഇൻസ്റ്റോൾ ചെയ്യുക: `npx @modelcontextprotocol/inspector`  
2. ഇൻസ്പെക്ടർ റൺ ചെയ്ത് സെർവറെപoin്റ് ചെയ്യുക  
3. നിങ്ങൾ സൃഷ്ടിച്ച ടൂളുകൾ ടെസ്റ്റ് ചെയ്യുക

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## നിങ്ങളുടെ stdio സെർവർ ഡീബഗ് ചെയ്യൽ

### MCP ഇൻസ്പെക്ടർ ഉപയോഗിച്ച്

MCP ഇൻസ്പെക്ടർ MCP സെർവറുകളുടെ ഡീബഗും ടെസ്റ്റിംഗും നടത്താൻ ഒരു വിലപ്പെട്ട ടૂલാണ്. നിങ്ങളുടെ stdio സെർവറുമായി ഇത് എങ്ങനെ ഉപയോഗിക്കാമെന്ന് ഇവിടെ കാണാം:

1. **ഇൻസ്പെക്ടർ ഇൻസ്റ്റാൾ ചെയ്യുക**:  
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **ഇൻസ്പെക്ടർ റൺ ചെയ്യുക**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **സെർവർ ടെസ്റ്റ് ചെയ്യുക**: ഇൻസ്പെക്ടർ വെബ് ഇന്റർഫേസിന് താഴെ നൽകുന്നു:  
   - സെർവർ ശേഷിപ്പുകൾ കാണുക  
   - വ്യത്യസ്ത പാരാമീറ്ററുകൾ ഉപയോഗിച്ച് ടൂളുകൾ പരീക്ഷിക്കുക  
   - JSON-RPC സന്ദേശങ്ങൾ നിരീക്ഷിക്കുക  
   - കണക്ഷൻ പ്രശ്നങ്ങൾ ഡീബഗ് ചെയ്യുക  

### VS Code ഉപയോഗിച്ച്

നിങ്ങളുടെ MCP സെർവർ നേരിട്ട് VS Code-ൽ ഡീബഗ് ചെയ്യാം:

1. `.vscode/launch.json`-ൽ ലോഞ്ച് കോൺഫിഗറേഷൻ നിർമ്മിക്കുക:  
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
3. ഡീബഗ്ഗർ റൺ ചെയ്ത് ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് ടെസ്റ്റ് ചെയ്യുക

### പൊതുവായ ഡീബഗ്ഗിംഗ് സഹായങ്ങൾ

- ലോഗിംഗിന് `stderr` ഉപയോഗിക്കുക - `stdout` MCP സന്ദേശങ്ങൾക്കാണ് സംരക്ഷിച്ചത്  
- എല്ലാ JSON-RPC സന്ദേശങ്ങളും newline-ലൂടെ വേർതിരിച്ചിരിക്കണം  
- സങ്കീർണ്ണമായ ഫംഗ്ഷനാലിറ്റി ചേർക്കുന്നതിന് മുൻപ് ലളിതമായ ടൂളുകളുമായി പരീക്ഷിക്കുക  
- സന്ദേശ ഫോർമാറ്റ് ഉറപ്പാക്കാൻ ഇൻസ്പെക്ടർ ഉപയോഗിക്കുക

## VS Code-ൽ stdio സെർവർ ഉപയോഗിക്കൽ

MCP stdio സെർവർ സൃഷ്ടിച്ചതിനു ശേഷം, ഇത് VS Code-യുമായി ഇന്റഗ്രേറ്റ് ചെയ്ത് ക്ലോഡ് അല്ലെങ്കിൽ മറ്റ് MCP കമ്പാറ്റിബിൾ ക്ലയന്റുകൾ ഉപയോഗിക്കാം.

### കോൺഫിഗറേഷൻ

1. MCP കോൺഫിഗറേഷൻ ഫയൽ സൃഷ്ടിക്കുക Windows-ൽ `%APPDATA%\Claude\claude_desktop_config.json` അല്ലെങ്കിൽ Mac-ൽ `~/Library/Application Support/Claude/claude_desktop_config.json` :

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

2. ക്ലോഡു പുനഃരാരംഭിക്കുക: പുതിയ സെർവർ കോൺഫിഗറേഷൻ ലോഡ് ചെയ്യാൻ ക്ലോഡു അടച്ച് വീണ്ടും തുറക്കുക.

3. കണക്ഷൻ ടെസ്റ്റ് ചെയ്യുക: ക്ലോഡുമായി സംഭാഷണം ആരംഭിച്ച് സെർവർ ടൂളുകൾ ഉപയോഗിച്ച് നോക്കുക:  
   - "ഗ്രീറ്റിംഗ് ടൂൾ ഉപയോഗിച്ച് എന്നെ ഗ്രീറ്റ് ചെയ്യാമോ?"  
   - "15-നും 27-നും കൂട്ടം കണക്കാക്കൂ"  
   - "സെർവർ വിവരങ്ങൾ എന്ത്?"

### TypeScript stdio സെർവർ ഉദാഹരണം

അറിയുതലിന് ഒരു പൂർണ്ണ TypeScript ഉദാഹരണം:

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

ഈ അപ്ഡേറ്റുചെയ്‌ത പാഠത്തിൽ നിങ്ങൾ പഠിച്ചത്:

- MCP സെർവർ stdio ട്രാൻസ്പോർട്ട് (ശുപാർശചെയ്‌ത മാർഗം) ഉപയോഗിച്ച് നിർമ്മിക്കുന്നത്  
- SSE ട്രാൻസ്പോർട്ട് stdio, Streamable HTTP എന്നിവയ്ക്ക് പകരം അപ്രസക്തമാക്കിയതീതിന് കാരണം  
- MCP ക്ലയന്റുകൾ വിളിക്കാവുന്ന ടൂളുകൾ സൃഷ്ടിക്കൽ  
- MCP ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് സെർവർ ഡീബഗ് ചെയ്യുക  
- VS Code, ക്ലോഡ് തുടങ്ങിയവയുമായി stdio സെർവർ ഇന്റഗ്രേറ്റ് ചെയ്യുക

stdio ട്രാൻസ്പോർട്ട് SSE നെ അപേക്ഷിച്ച് ലളിതം, കൂടുതൽ സുരക്ഷിതം, പ്രകടനത്തിൽ മെച്ചപ്പെട്ട മാർഗമാണ്. MCP സെർവർ നിർമാണങ്ങളുടെ പരിപാരിപാടിയിൽ 2025-06-18 സൂചിപ്പിക്കുന്നതുപോലെ ഇത് ഏറ്റവും ശുപാർശചെയ്ത ട്രാൻസ്പോർട്ടായി നിലനിൽക്കുന്നു.

### .NET

1. ആദ്യം ചില ടൂളുകൾ നമുക്ക് ഉണ്ടാക്കാം, ഇതിന് *Tools.cs* എന്ന ഫയൽ താഴെയുള്ള ഉള്ളടക്കത്തോടൊപ്പം ഉണ്ടാക്കും:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## അഭ്യാസം: നിങ്ങൾ സൃഷ്ടിച്ച stdio സെർവർ ടെസ്റ്റ് ചെയ്യൽ

stdio സെർവർ നിർമ്മിച്ചതിനുശേഷം, ഇത് നല്ല രീതിയിൽ പ്രവർത്തിക്കുന്നുണ്ടോ എന്ന് പരിശോധിക്കാം.

### മുൻകൂട്ടി ആവശ്യമായത്

1. MCP ഇൻസ്പെക്ടർ ഇൻസ്റ്റാൾ ചെയ്തിട്ടുണ്ടെന്ന് ഉറപ്പാക്കുക:  
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```
  
2. നിങ്ങളുടെ സെർവർ കോഡ് സേവ് ചെയ്തിട്ടുണ്ടാകണം (ഉദാഹരണം: `server.py`)

### ഇൻസ്പെക്ടർ ഉപയോഗിച്ച് ടെസ്റ്റിംഗ്

1. **ഇൻസ്പെക്ടർ നിങ്ങളുടെ സെർവറോടൊപ്പം ആരംഭിക്കുക**:  
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```
  
2. **വെബ് ഇന്റർഫേസ് തുറക്കുക**: ഇൻസ്പെക്ടർ മൊത്തം സെർവർ ശേഷിപ്പുകൾ കാണിക്കുന്ന ഒരു ബ്ര라우സർ വിൻഡോ തുറക്കും.

3. **ടൂളുകൾ ടെസ്റ്റ് ചെയ്യുക**:  
   - വ്യത്യസ്ത പേരുകളോടൊപ്പം `get_greeting` ടൂൾ പരിശോദിക്കുക  
   - വിവിധ സംഖ്യകളോടെ `calculate_sum` പരീക്ഷിക്കുക  
   - സെർവർ മെടാടേറ്റ ഡാറ്റ കാണാൻ `get_server_info` കോളുചെയ്യുക

4. **കമ്മ്യൂണിക്കേഷൻ നിരീക്ഷിക്കുക**: ഇൻസ്പെക്ടർ ക്ലയന്റ്, സെർവർ JSON-RPC സന്ദേശങ്ങൾ എങ്ങനെ കൈമാറ്റം ചെയ്യുമ്പോഴുള്ളത് കാണിക്കുന്നു.

### നിങ്ങൾ കാണേണ്ടത്

നിങ്ങളുടെ സെർവർ ശരിയായി ആരംഭിക്കുമ്പോൾ കാണുക:  
- ഇൻസ്പെക്ടറിൽ സെർവർ ശേഷിപ്പുകൾ ലിസ്റ്റ് ചെയ്യപ്പെട്ടിരിക്കും  
- പരീക്ഷണത്തിനുള്ള ടൂളുകൾ ലഭ്യമാണ്  
- JSON-RPC സന്ദേശങ്ങൾ വിജയകരമായി കൈമാറ്റം ചെയ്യുന്നു  
- ടൂൾ മറുപടികൾ ഇന്റർഫേസിൽ പ്രദർശിപ്പിക്കുന്നു

### സാധാരണപ്രശ്നങ്ങളും പരിഹാരങ്ങളും

**സെർവർ ആരംഭിക്കുന്നില്ലെങ്കിൽ:**  
- എല്ലാ ഡിപ്പൻഡൻസികളും ഇൻസ്റ്റാൾ ചെയ്‌തിട്ടുണ്ടോ പരിശോധിക്കുക: `pip install mcp`  
- Python സർവ്വ്വവാക്യം, ഇൻഡെൻറ്റേഷൻ ശരിയാണോ പരിശോധിക്കുക  
- കോൺസോൾയിൽ എറർ മെസ്സേജുകൾ പരിശോധിക്കുക

**ടൂളുകൾ കാണാനില്ലെങ്കിൽ:**  
- `@server.tool()` ഡെക്കറേറ്റർകൾ ഉൾപ്പെടുന്നതാണോ പരിശോധിക്കുക  
- `main()`-നു മുൻപ് ടൂൾ ഫംഗ്ഷനുകൾ ഡിഫൈൻ ചെയ്തിട്ടുണ്ടോ ഉറപ്പാക്കുക  
- സെർവർ ശരിയായി കോൺഫിഗർ ചെയ്‌തിരിക്കുന്നുണ്ടോ പരിശോധിക്കുക

**കണക്ഷൻ പ്രശ്നങ്ങൾ:**  
- stdio ട്രാൻസ്പോർട്ട് ശരിയായി ഉപയോഗിക്കുകയാണോ പരിശോധിക്കുക  
- മറ്റൊരു പ്രോസസ്സ് ഇടപെടുന്നുണ്ടോ പരിശോധിക്കുക  
- ഇൻസ്‌പെക്ടർ കമാൻഡ് സിന്താക്‌സുക്ഷിക്കുക

## അസൈൻമെന്റ്

നിങ്ങളുടെ സെർവർ അധിക ശേഷിപ്പുകൾക്കായി വികസിപ്പിക്കുക. ഉദാഹരണത്തിന്, [ഈ പേജ്](https://api.chucknorris.io/) സന്ദർശിച്ച് എങ്ങനെ API കോളുചെയ്യൂം ടൂൾ ചേർക്കാമെന്ന് നോക്കുക. സെർവർ എങ്ങനെയാണ് ആയിരിക്കണമെന്നതിൽ നിങ്ങൾ തീരുമാനിക്കുക. എളുപ്പത്തിൽ ആസ്വദിക്കുക :)

## പരിഹാരം

[Pariharam](./solution/README.md) പ്രവർത്തനക്ഷമമായ കോഡോടുകൂടിയ ഒരു നിർദ്ദേശ പരിഹാരമാണ്.

## പ്രധാന പാഠങ്ങൾ

ഈ അധ്യായത്തിൽ നിന്നുള്ള പ്രധാന പാഠങ്ങൾ:

- stdio ട്രാൻസ്പോർട്ട് പ്രാദേശിക MCP സെർവറുകളുടെ ശുപാർശ ചെയ്ത മാർഗമാണ്.  
- stdio ട്രാൻസ്പോർട്ട് MCP സെർവർ-ക്ലയന്റ് മാനദണ്ഡാസഹിതം സ്റ്റാൻഡേർഡ് ഇൻപുട്ട് ഔട്ട്‌പുട്ട് സ്ട്രീമുകൾ വഴി സൗകര്യപ്രദമായി ആശയവിനിമയം നൽകുന്നു.  
- ഇൻസ്പെക്ടറും Visual Studio Code-യും stdio സെർവറുകൾ നേരിട്ട് ഉപയോഗിക്കാൻ സഹായിക്കുന്നു, ഡീബഗ്, ഇന്റഗ്രേഷൻ എളുപ്പമാക്കുന്നു.

## സാമ്പിളുകൾ

- [Java Calculator](../samples/java/calculator/README.md)  
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript Calculator](../samples/javascript/README.md)  
- [TypeScript Calculator](../samples/typescript/README.md)  
- [Python Calculator](../../../../03-GettingStarted/samples/python)

## അധിക സ്രോതസുകൾ

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## അടുത്തത്

## അടുത്ത ഘട്ടങ്ങൾ

stdio ട്രാൻസ്പേർട്ട് ഉപയോഗിച്ച് MCP സെർവർ നിർമ്മിക്കേണ്ടത് പഠിച്ചതിനുശേഷം, കൂടുതൽ മുൻനിര വിഷയങ്ങൾ പരിശോധിക്കാം:

- **അടുത്തത്**: [MCP ഷ്റ്റ്രീമിംഗും HTTP-യിലൂടെ (Streamable HTTP)](../06-http-streaming/README.md) - പിന്നീടുള്ള റിമോട്ട് സർവർ ട്രാൻസ്പോർട്ട് മെക്കാനിസത്തെക്കുറിച്ച് जानാന്  
- **മുന്‍നിര**: [MCP സുരക്ഷയുടെ നല്ല പാലനങ്ങൾ](../../02-Security/README.md) - MCP സെർവറുകളിൽ സുരക്ഷ നടപ്പിലാക്കുക  
- **ഉത്പാദന**: [പ്രവർത്തന സ്കീമുകൾ](../09-deployment/README.md) - നിങ്ങളുടെ സർവറുകൾ പ്രൊഡക്ഷനിലേക്ക് ഡിപ്ലോയ്മെന്റ്

## അധിക സ്രോതസുകൾ

- [MCP സ്പെസിഫിക്കേഷൻ 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - ഔദ്യോഗിക സ്പെസിഫിക്കേഷൻ  
- [MCP SDK ഡോക്യുമെന്റേഷൻ](https://github.com/modelcontextprotocol/sdk) - എല്ലാ ഭാഷകളുടെയും SDK റഫറൻസുകൾ  
- [കമ്മ്യൂണിറ്റി ഉദാഹരണങ്ങൾ](../../06-CommunityContributions/README.md) - കമ്മ്യൂണിറ്റിയിൽ നിന്നുള്ള കൂടുതൽ സർവർ ഉദാഹരണങ്ങൾ

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ഡിസ്ക്ലെയിമർ**:  
ഈ ഡോക്യുമെന്റ് [Co-op Translator](https://github.com/Azure/co-op-translator) എന്ന എഐ വിവർത്തനസേവനം ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്‌ക്ക് ശ്രമിക്കുന്നെങ്കിലും, യാന്ത്രിക വിവർത്തനങ്ങളിൽ പിഴവുകളോ തട്ടിപ്പുകളോ ഉണ്ടാകാവുന്നതാണ്. അതിനാൽ, ഈ ഡോക്യുമെന്റിന്റെ യഥാർത്ഥ ഭാഷയിലെ മൂല രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്നും പരിഗണിക്കണം. പ്രധാന വിവരങ്ങൾക്കായി പ്രൊഫഷണൽ മനുഷ്യൻമാരായ വിവർത്തകരുടെ സേവനം സ്വീകരിക്കുക. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾക്ക്‌ ഞങ്ങൾക്ക് ഉത്തരവാദിത്വം ബാധകമല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->