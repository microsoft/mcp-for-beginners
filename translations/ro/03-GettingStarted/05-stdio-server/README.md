# Server MCP cu transport stdio

> **⚠️ Actualizare importantă**: Începând cu specificația MCP 2025-06-18, transportul standalone SSE (Server-Sent Events) a fost **înlocuit** cu transportul "Streamable HTTP". Specificația MCP curentă definește două mecanisme principale de transport:
> 1. **stdio** - Input/output standard (recomandat pentru servere locale)
> 2. **Streamable HTTP** - Pentru servere remote care pot folosi SSE intern
>
> Această lecție a fost actualizată pentru a se concentra pe **transportul stdio**, care este metoda recomandată pentru majoritatea implementărilor serverelor MCP.

Transportul stdio permite serverelor MCP să comunice cu clienții prin fluxurile standard de intrare și ieșire. Acesta este cel mai utilizat și recomandat mecanism de transport în specificația MCP curentă, oferind o modalitate simplă și eficientă de a construi servere MCP care pot fi integrate ușor cu diverse aplicații client.

## Prezentare generală

Această lecție acoperă modul de construire și consumare a serverelor MCP folosind transportul stdio.

## Obiective de învățare

La sfârșitul acestei lecții, vei fi capabil să:

- Construiești un server MCP folosind transportul stdio.
- Depanezi un server MCP folosind Inspectorul.
- Consumii un server MCP folosind Visual Studio Code.
- Înțelegi mecanismele curente de transport MCP și de ce stdio este recomandat.

## Transportul stdio - Cum funcționează

Transportul stdio este unul dintre cele două tipuri de transport suportate în specificația MCP actuală (2025-06-18). Iată cum funcționează:

- **Comunicare simplă**: serverul citește mesaje JSON-RPC de la intrarea standard (`stdin`) și trimite mesaje către ieșirea standard (`stdout`).
- **Bazat pe proces**: clientul lansează serverul MCP ca un proces copil.
- **Formatul mesajelor**: mesajele sunt cereri, notificări sau răspunsuri JSON-RPC individuale, delimitate prin linii noi.
- **Jurnalizare**: serverul POATE scrie șiruri UTF-8 către ieșirea de eroare standard (`stderr`) pentru logare.

### Cerințe cheie:
- Mesajele TREBUIE să fie delimitate prin linii noi și NU TREBUIE să conțină linii noi în interior
- Serverul NU TREBUIE să scrie nimic pe `stdout` care să nu fie un mesaj MCP valid
- Clientul NU TREBUIE să scrie nimic către `stdin` al serverului care să nu fie un mesaj MCP valid

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

În codul precedent:

- Importăm clasa `Server` și `StdioServerTransport` din MCP SDK
- Creăm o instanță de server cu configurație și capabilități de bază

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Creează o instanță de server
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

În codul precedent:

- Creăm o instanță de server folosind MCP SDK
- Definim unelte folosind decoratori
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

- Nu necesită configurare de server web sau endpoint-uri HTTP
- Sunt lansate ca procese copil de către client
- Comunică prin fluxurile stdin/stdout
- Sunt mai simple de implementat și de depanat

## Exercițiu: Crearea unui server stdio

Pentru a crea serverul nostru, trebuie să ținem cont de două aspecte:

- Trebuie să folosim un server web pentru a expune endpoint-uri pentru conexiune și mesaje.

## Laborator: Crearea unui server MCP simplu cu stdio

În acest laborator, vom crea un server MCP simplu folosind transportul stdio recomandat. Acest server va expune unelte pe care clienții le pot apela folosind protocolul standard Model Context Protocol.

### Precondiții

- Python 3.8 sau versiune mai nouă
- MCP Python SDK: `pip install mcp`
- Înțelegere de bază a programării asincrone

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
    # Folosește transportul stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```


## Diferențe cheie față de abordarea SSE depreciată

**Transport stdio (Standard curent):**
- Model simplu de proces copil - clientul lansează serverul ca proces copil
- Comunicare prin stdin/stdout folosind mesaje JSON-RPC
- Nu este necesară configurarea unui server HTTP
- Performanță și securitate mai bune
- Debugging și dezvoltare mai ușoare

**Transport SSE (depreciat începând cu MCP 2025-06-18):**
- Necesita server HTTP cu endpoint-uri SSE
- Configurare mai complexă cu infrastructură web
- Considerații suplimentare de securitate pentru endpoint-uri HTTP
- A fost înlocuit de Streamable HTTP pentru scenarii web

### Crearea serverului cu transport stdio

Pentru a crea serverul nostru stdio, trebuie să:

1. **Importăm bibliotecile necesare** - avem nevoie de componentele server MCP și transportul stdio
2. **Creăm o instanță de server** - definim serverul cu capabilitățile sale
3. **Definim unelte** - adăugăm funcționalitatea pe care dorim să o expunem
4. **Configurăm transportul** - setăm comunicarea prin stdio
5. **Pornim serverul** - lansăm serverul și gestionăm mesajele

Hai să construim pas cu pas:

### Pasul 1: Crearea unui server stdio de bază

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configurează jurnalizarea
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


### Pasul 2: Adăugarea de unelte suplimentare

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


### Pasul 3: Pornirea serverului

Salvează codul ca `server.py` și rulează-l din linia de comandă:

```bash
python server.py
```

Serverul va porni și va aștepta input de la stdin. Comunică folosind mesaje JSON-RPC prin transportul stdio.

### Pasul 4: Testarea cu Inspectorul

Poți testa serverul tău folosind MCP Inspector:

1. Instalează Inspectorul: `npx @modelcontextprotocol/inspector`
2. Rulează Inspectorul și direcționează-l către serverul tău
3. Testează uneltele pe care le-ai creat

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## Depanarea serverului stdio

### Folosirea MCP Inspector

MCP Inspector este un instrument valoros pentru depanarea și testarea serverelor MCP. Iată cum să îl folosești cu serverul stdio:

1. **Instalează Inspectorul**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Rulează Inspectorul**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testează serverul**: Inspectorul oferă o interfață web unde poți:
   - Vizualiza capabilitățile serverului
   - Testa uneltele cu parametri diferiți
   - Monitoriza mesajele JSON-RPC
   - Depana probleme de conexiune

### Folosirea VS Code

Poți depana serverul MCP direct în VS Code:

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

2. Setează breakpoint-uri în codul serverului
3. Rulează debuggerul și testează cu Inspectorul

### Sfaturi comune de depanare

- Folosește `stderr` pentru logare - nu scrie niciodată pe `stdout` deoarece este rezervat mesajelor MCP
- Asigură-te că toate mesajele JSON-RPC sunt delimitate prin linii noi
- Testează mai întâi cu unelte simple înainte de a adăuga funcționalități complexe
- Folosește Inspectorul pentru a verifica formatul mesajelor

## Consumarea serverului stdio în VS Code

Odată ce ai construit serverul MCP stdio, îl poți integra cu VS Code pentru a-l folosi cu Claude sau alți clienți compatibili MCP.

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

2. **Repornește Claude**: Închide și redeschide Claude pentru a încărca noua configurație de server.

3. **Testează conexiunea**: Pornește o conversație cu Claude și încearcă să folosești uneltele serverului tău:
   - "Poți să mă saluți folosind unealta de salut?"
   - "Calculează suma lui 15 și 27"
   - "Care este informația despre server?"

### Exemplu TypeScript de server stdio

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

// Adaugă unelte
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


### Exemplu .NET de server stdio

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

- Construiești servere MCP folosind transportul curent **stdio** (metoda recomandată)
- Înțelegi de ce transportul SSE a fost înlocuit cu stdio și Streamable HTTP
- Creezi unelte care pot fi apelate de clienții MCP
- Depanezi serverul folosind MCP Inspector
- Integrezi serverul stdio cu VS Code și Claude

Transportul stdio oferă o modalitate mai simplă, mai sigură și mai performantă pentru construire servere MCP comparativ cu abordarea SSE depreciată. Este transportul recomandat pentru majoritatea implementărilor serverelor MCP începând cu specificația 2025-06-18.

### .NET

1. Hai să creăm mai întâi niște unelte, pentru asta vom crea un fișier *Tools.cs* cu următorul conținut:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```


## Exercițiu: Testarea serverului stdio

Acum că ai construit serverul stdio, să îl testăm să vedem dacă funcționează corect.

### Precondiții

1. Asigură-te că ai instalat MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Codul serverului tău ar trebui salvat (de exemplu ca `server.py`)

### Testarea cu Inspectorul

1. **Pornește Inspectorul cu serverul tău**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Deschide interfața web**: Inspectorul va deschide o fereastră în browser care arată capabilitățile serverului tău.

3. **Testează uneltele**:
   - Încearcă unealta `get_greeting` cu nume diferite
   - Testează unelta `calculate_sum` cu diverse numere
   - Apelează unealta `get_server_info` pentru a vedea metadatele serverului

4. **Monitorizează comunicarea**: Inspectorul arată mesajele JSON-RPC care sunt schimbate între client și server.

### Ce ar trebui să vezi

Când serverul tău pornește corect, ar trebui să vezi:
- Capabilitățile serverului listate în Inspector
- Unelte disponibile pentru testare
- Mesaje JSON-RPC schimbate cu succes
- Răspunsuri ale uneltelor afișate în interfață

### Probleme frecvente și soluții

**Serverul nu pornește:**
- Verifică dacă toate dependențele sunt instalate: `pip install mcp`
- Verifică sintaxa și indentarea Python
- Caută mesaje de eroare în consolă

**Uneltele nu apar:**
- Asigură-te că decoratoarele `@server.tool()` sunt prezente
- Verifică ca funcțiile uneltelor să fie definite înainte de `main()`
- Asigură-te că serverul este configurat corect

**Probleme de conectare:**
- Verifică că serverul folosește corect transportul stdio
- Asigură-te că niciun alt proces nu interferează
- Verifică sintaxa comenzii Inspectorului

## Temă

Încearcă să extinzi serverul cu mai multe capabilități. Vezi [această pagină](https://api.chucknorris.io/) pentru a adăuga, de exemplu, o unealtă care apelează un API. Tu decizi cum va arăta serverul. Distracție plăcută :)

## Soluție

[Solution](./solution/README.md) Iată o posibilă soluție cu cod funcțional.

## Puncte cheie

Punctele cheie ale acestui capitol sunt următoarele:

- Transportul stdio este mecanismul recomandat pentru servere MCP locale.
- Transportul stdio permite comunicare neîntreruptă între serverele MCP și clienți folosind fluxurile standard de intrare și ieșire.
- Poți folosi atât Inspectorul cât și Visual Studio Code pentru a consuma serverele stdio direct, ceea ce face depanarea și integrarea foarte simple.

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

- **Următorul**: [HTTP Streaming cu MCP (Streamable HTTP)](../06-http-streaming/README.md) - Află despre celălalt mecanism de transport suportat pentru servere remote
- **Avansat**: [Bune practici de securitate MCP](../../02-Security/README.md) - Implementează securitate în serverele tale MCP
- **Producție**: [Strategii de implementare](../09-deployment/README.md) - Publică serverele pentru utilizare în producție

## Resurse suplimentare

- [Specificația MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Specificația oficială
- [Documentația MCP SDK](https://github.com/modelcontextprotocol/sdk) - Referințe SDK pentru toate limbajele
- [Exemple comunitare](../../06-CommunityContributions/README.md) - Mai multe exemple de servere din comunitate

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->