# Server MCP cu transport stdio

> **⚠️ Actualizare Importantă**: Începând cu Specificația MCP 2025-06-18, transportul SSE (Server-Sent Events) independent a fost **învechit** și înlocuit cu transportul "Streamable HTTP". Specificația MCP curentă definește două mecanisme principale de transport:
> 1. **stdio** - Intrare/ieșire standard (recomandat pentru servere locale)
> 2. **Streamable HTTP** - Pentru servere la distanță care pot folosi SSE intern
>
> Această lecție a fost actualizată pentru a se concentra pe **transportul stdio**, care este abordarea recomandată pentru majoritatea implementărilor de server MCP.

Transportul stdio permite serverelor MCP să comunice cu clienții prin fluxurile standard de intrare și ieșire. Acesta este mecanismul de transport cel mai utilizat și recomandat în specificația MCP curentă, oferind o modalitate simplă și eficientă de a construi servere MCP care pot fi integrate cu ușurință în diverse aplicații client.

## Prezentare generală

Această lecție acoperă cum să construiești și să consumi servere MCP folosind transportul stdio.

## Obiectivele de învățare

Până la finalul acestei lecții, vei fi capabil să:

- Construiești un Server MCP folosind transportul stdio.
- Debugezi un Server MCP folosind Inspectorul.
- Consumii un Server MCP folosind Visual Studio Code.
- Înțelegi mecanismele curente de transport MCP și de ce stdio este recomandat.


## Transport stdio - Cum funcționează

Transportul stdio este unul dintre cele două transporturi standard în Specificația MCP
`2026-07-28`. Iată cum funcționează:

- **Comunicare simplă**: Serverul citește mesaje JSON-RPC de la intrarea standard (`stdin`) și trimite mesaje la ieșirea standard (`stdout`).
- **Bazat pe proces**: Clientul lansează serverul MCP ca un subprocess.
- **Formatul mesajelor**: Mesajele sunt cereri, notificări sau răspunsuri JSON-RPC individuale, delimitate de linii noi.
- **Logare**: Serverul POATE scrie șiruri UTF-8 către eroarea standard (`stderr`) pentru scopuri de logare.

### Cerințe cheie:
- Mesajele TREBUIE să fie delimitate de linii noi și NU TREBUIE să conțină linii noi încorporate
- Serverul NU TREBUIE să scrie nimic în `stdout` care să nu fie un mesaj MCP valid
- Clientul NU TREBUIE să scrie nimic în `stdin` al serverului care să nu fie un mesaj MCP valid

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

În codul precedent:

- Importăm clasa `Server` și `StdioServerTransport` din SDK-ul MCP
- Creăm o instanță de server cu o configurație și capabilități de bază
- Creăm o instanță `StdioServerTransport` și conectăm serverul la aceasta, permițând comunicarea prin stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Creează o instanță a serverului
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

În codul precedent noi:

- Creăm o instanță de server folosind SDK-ul MCP
- Definim uneltele folosind decoratori
- Folosim managerul de context stdio_server pentru a gestiona transportul

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

Diferența principală față de SSE este că serverele stdio:

- Nu necesită configurarea unui server web sau puncte finale HTTP
- Sunt lansate ca subprocessuri de client
- Comunicăm prin fluxurile stdin/stdout
- Sunt mai simple de implementat și debuggat

## Exercițiu: Crearea unui server stdio

Pentru a crea serverul nostru, trebuie să ținem cont de două lucruri:

- Trebuie să folosim un server web pentru a expune puncte finale pentru conexiune și mesaje.
## Laborator: Crearea unui server MCP simplu stdio

În acest laborator, vom crea un server MCP simplu folosind transportul stdio recomandat. Acest server va expune unelte pe care clienții le pot apela folosind Protocolul Model Context standard.

### Precondiții

- Python 3.8 sau o versiune ulterioară
- SDK MCP Python: `pip install mcp`
- Cunoștințe de bază despre programarea asincronă

Să începem prin a crea primul nostru server MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configurează jurnalizarea
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Creează serverul
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
    # Utilizează transportul stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Diferențe cheie față de abordarea SSE învechită

**Transportul Stdio (Standardul curent):**
- Model simplu de subprocess - clientul lansează serverul ca proces fiu
- Comunicare prin stdin/stdout folosind mesaje JSON-RPC
- Nu este necesară configurarea unui server HTTP
- Performanță și securitate mai bune
- Debbugare și dezvoltare mai ușoară

**Transportul SSE (învechit din MCP 2025-06-18):**
- Necesită server HTTP cu puncte finale SSE
- Configurare mai complexă cu infrastructură server web
- Considerații suplimentare de securitate pentru punctele finale HTTP
- Acum înlocuit de Streamable HTTP pentru scenarii bazate pe web

### Crearea unui server cu transport stdio

Pentru a crea serverul nostru stdio, trebuie să:

1. **Importăm librăriile necesare** - Avem nevoie de componentele server MCP și transportul stdio
2. **Creăm o instanță de server** - Definim serverul cu capabilitățile sale
3. **Definim unelte** - Adăugăm funcționalitățile pe care dorim să le expunem
4. **Configurăm transportul** - Setăm comunicarea stdio
5. **Rulăm serverul** - Pornim serverul și gestionăm mesajele

Să construim pas cu pas:

### Pasul 1: Crearea unui server stdio de bază

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configurează înregistrarea
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Creează serverul
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

### Pasul 2: Adăugarea mai multor unelte

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

### Pasul 3: Rularea serverului

Salvați codul ca `server.py` și rulați-l din linia de comandă:

```bash
python server.py
```

Serverul va porni și va aștepta intrare de la stdin. Comunicarea se face folosind mesaje JSON-RPC peste transportul stdio.

### Pasul 4: Testarea cu Inspectorul

Puteți testa serverul folosind MCP Inspector:

1. Instalați Inspectorul: `npx @modelcontextprotocol/inspector`
2. Rulați Inspectorul și indicați-l către serverul dvs.
3. Testați uneltele create

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debbugare server stdio

### Folosind MCP Inspector

MCP Inspector este un instrument valoros pentru debuggare și testarea serverelor MCP. Iată cum să îl folosești cu serverul stdio:

1. **Instalați Inspectorul**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Rulați Inspectorul**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testați serverul**: Inspectorul oferă o interfață web unde poți:
   - Vizualiza capabilitățile serverului
   - Testa uneltele cu parametri diferiți
   - Monitoriza mesajele JSON-RPC
   - Debbuga probleme de conexiune

### Folosind VS Code

De asemenea, poți debuga serverul MCP direct în VS Code:

1. Creează o configurație de lansare în `.vscode/launch.json`:
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

2. Setează puncte de oprire în codul serverului
3. Rulează debuggerul și testează cu Inspectorul

### Sfaturi comune pentru debuggare

- Folosește `stderr` pentru logare - niciodată să nu scrii în `stdout`, deoarece este rezervat mesajelor MCP
- Asigură-te că toate mesajele JSON-RPC sunt delimitate prin linii noi
- Testează mai întâi cu unelte simple înainte să adaugi funcționalități complexe
- Folosește Inspectorul pentru a verifica formatele mesajelor

## Consumarea serverului stdio în VS Code

După ce ai construit serverul MCP stdio, îl poți integra cu VS Code pentru a-l folosi cu Claude sau alți clienți compatibili MCP.

### Configurare

1. **Creează un fișier de configurare MCP** la `%APPDATA%\Claude\claude_desktop_config.json` (Windows) sau `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Repornește Claude**: Închide și redeschide Claude pentru a încărca noua configurare a serverului.

3. **Testează conexiunea**: Începe o conversație cu Claude și încearcă să folosești uneltele serverului tău:
   - "Poți să mă saluți folosind unealta de salut?"
   - "Calculează suma a 15 și 27"
   - "Care sunt informațiile despre server?"

### Exemplu de server stdio TypeScript

Iată un exemplu complet TypeScript pentru referință:

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

// Adaugă instrumente
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

### Exemplu de server stdio .NET

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

## Rezumat

În această lecție actualizată, ai învățat cum să:

- Construiești servere MCP folosind actualul **transport stdio** (abordarea recomandată)
- Înțelegi de ce transportul SSE a fost învechit în favoarea stdio și Streamable HTTP
- Creezi unelte care pot fi apelate de clienții MCP
- Debugezi serverul folosind MCP Inspector
- Integrezi serverul stdio cu VS Code și Claude

Transportul stdio oferă o modalitate mai simplă, mai sigură și mai performantă de a construi servere MCP în comparație cu abordarea SSE învechită. Este transportul recomandat pentru majoritatea implementărilor de server MCP din specificația din 2025-06-18.


### .NET

1. Să creăm mai întâi câteva unelte, pentru aceasta vom crea un fișier *Tools.cs* cu următorul conținut:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Exercițiu: Testarea serverului stdio

Acum că ai construit serverul stdio, să îl testăm pentru a ne asigura că funcționează corect.

### Precondiții

1. Asigură-te că ai instalat MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Codul serverului ar trebui să fie salvat (de exemplu, ca `server.py`)

### Testarea cu Inspectorul

1. **Pornește Inspectorul cu serverul tău**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Deschide interfața web**: Inspectorul va deschide o fereastră de browser care arată capabilitățile serverului tău.

3. **Testează uneltele**: 
   - Încearcă unealta `get_greeting` cu diferite nume
   - Testează unealta `calculate_sum` cu diverse numere
   - Apelează unealta `get_server_info` pentru a vedea meta-datele serverului

4. **Monitorizează comunicarea**: Inspectorul afișează mesajele JSON-RPC schimbate între client și server.

### Ce ar trebui să vezi

Când serverul tău pornește corect, ar trebui să vezi:
- Capabilitățile serverului listate în Inspector
- Unelte disponibile pentru testare
- Schimburi reușite de mesaje JSON-RPC
- Răspunsuri ale uneltelor afișate în interfață

### Probleme comune și soluții

**Serverul nu pornește:**
- Verifică dacă toate dependențele sunt instalate: `pip install mcp`
- Verifică sintaxa și indentarea Python
- Caută mesaje de eroare în consolă

**Uneltele nu apar:**
- Asigură-te că decoratorii `@server.tool()` sunt prezenți
- Verifică dacă funcțiile uneltelor sunt definite înainte de `main()`
- Asigură-te că serverul este configurat corect

**Probleme de conexiune:**
- Asigură-te că serverul folosește corect transportul stdio
- Verifică dacă nu există alte procese care interferează
- Verifică sintaxa comenzii Inspector

## Tema

Încearcă să extinzi serverul cu mai multe capabilități. Vezi [această pagină](https://api.chucknorris.io/) pentru a adăuga, de exemplu, o unealtă care apelează o API. Tu decizi cum ar trebui să arate serverul. Distracție plăcută :)
## Soluție

[Soluție](./solution/README.md) Iată o posibilă soluție cu cod funcțional.

## Puncte-cheie

Punctele-cheie din acest capitol sunt:

- Transportul stdio este mecanismul recomandat pentru serverele MCP locale.
- Transportul stdio permite comunicare transparentă între serverele MCP și clienți folosind fluxurile standard de intrare și ieșire.
- Poți folosi atât Inspectorul cât și Visual Studio Code pentru a consuma servere stdio direct, făcând debuggare și integrare simple.

## Exemple

- [Calculator Java](../samples/java/calculator/README.md)
- [Calculator .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculator JavaScript](../samples/javascript/README.md)
- [Calculator TypeScript](../samples/typescript/README.md)
- [Calculator Python](../../../../03-GettingStarted/samples/python) 

## Resurse suplimentare

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Ce urmează

## Pași următori

Acum că ai învățat cum să construiești servere MCP cu transportul stdio, poți explora subiecte mai avansate:

- **Următorul**: [HTTP Streaming cu MCP (Streamable HTTP)](../06-http-streaming/README.md) - Află despre celălalt mecanism de transport suportat pentru servere la distanță
- **Avansat**: [Cele mai bune practici de securitate MCP](../../02-Security/README.md) - Implementează securitatea în serverele MCP
- **Producție**: [Strategii de implementare](../09-deployment/README.md) - Pune serverele în producție

## Resurse suplimentare

- [Specificația MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Specificația curentă
- [Documentația SDK MCP](https://github.com/modelcontextprotocol/sdk) - Referințe SDK pentru toate limbajele
- [Exemple din comunitate](../../06-CommunityContributions/README.md) - Mai multe exemple de servere din comunitate

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->