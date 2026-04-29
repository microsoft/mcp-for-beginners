# Server MCP con trasporto stdio

> **⚠️ Aggiornamento importante**: A partire dalla specifica MCP 2025-06-18, il trasporto SSE (Server-Sent Events) autonomo è stato **deprecato** e sostituito dal trasporto "Streamable HTTP". L'attuale specifica MCP definisce due meccanismi di trasporto principali:
> 1. **stdio** - input/output standard (consigliato per server locali)
> 2. **Streamable HTTP** - per server remoti che possono utilizzare internamente SSE
>
> Questa lezione è stata aggiornata per concentrarsi sul **trasporto stdio**, che è l'approccio raccomandato per la maggior parte delle implementazioni di server MCP.

Il trasporto stdio consente ai server MCP di comunicare con i client tramite i flussi di input e output standard. Questo è il meccanismo di trasporto più comunemente utilizzato e consigliato nella specifica MCP attuale, fornendo un modo semplice ed efficiente per costruire server MCP che possono essere facilmente integrati con diverse applicazioni client.

## Panoramica

Questa lezione tratta come costruire e consumare server MCP utilizzando il trasporto stdio.

## Obiettivi di apprendimento

Alla fine di questa lezione, sarai in grado di:

- Costruire un server MCP usando il trasporto stdio.
- Eseguire il debug di un server MCP usando l'Inspector.
- Consumare un server MCP utilizzando Visual Studio Code.
- Comprendere i meccanismi di trasporto MCP attuali e perché il trasporto stdio è raccomandato.


## Trasporto stdio - Come funziona

Il trasporto stdio è uno dei due tipi di trasporto supportati nella specifica MCP attuale (2025-06-18). Ecco come funziona:

- **Comunicazione semplice**: il server legge messaggi JSON-RPC dall'input standard (`stdin`) e invia messaggi all'output standard (`stdout`).
- **Basato su processo**: il client avvia il server MCP come sottoprocesso.
- **Formato messaggi**: i messaggi sono singole richieste, notifiche o risposte JSON-RPC, delimitate da newline.
- **Logging**: il server PUÒ scrivere stringhe UTF-8 sull'errore standard (`stderr`) per scopi di logging.

### Requisiti chiave:
- I messaggi DEVONO essere delimitati da newline e NON DEVONO contenere newline incorporati
- Il server NON DEVE scrivere nulla su `stdout` che non sia un messaggio MCP valido
- Il client NON DEVE scrivere nulla su `stdin` del server che non sia un messaggio MCP valido

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

Nel codice precedente:

- Importiamo la classe `Server` e `StdioServerTransport` dal SDK MCP
- Creiamo un'istanza di server con configurazione e capacità di base
- Creiamo un'istanza `StdioServerTransport` e colleghiamo il server ad essa, abilitando la comunicazione su stdin/stdout

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Crea istanza del server
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

Nel codice precedente:

- Creiamo un'istanza di server usando il SDK MCP
- Definiamo strumenti usando i decorator
- Usiamo il context manager stdio_server per gestire il trasporto

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

La differenza chiave rispetto a SSE è che i server stdio:

- Non richiedono configurazione di server web o endpoint HTTP
- Sono avviati come sottoprocesso dal client
- Comunicano tramite i flussi stdin/stdout
- Sono più semplici da implementare e debug

## Esercizio: Creare un server stdio

Per creare il nostro server, dobbiamo tenere a mente due cose:

- Dobbiamo usare un server web per esporre endpoint per la connessione e i messaggi.
## Laboratorio: Creare un semplice server MCP stdio

In questo laboratorio, creeremo un semplice server MCP utilizzando il trasporto stdio consigliato. Questo server esporrà strumenti che i client possono chiamare usando lo standard Model Context Protocol.

### Prerequisiti

- Python 3.8 o successivo
- MCP Python SDK: `pip install mcp`
- Conoscenze base di programmazione asincrona

Iniziamo creando il nostro primo server MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configura la registrazione
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crea il server
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
    # Usa il trasporto stdio
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Differenze chiave rispetto all'approccio SSE deprecato

**Trasporto Stdio (Standard attuale):**
- Modello semplice di sottoprocesso - il client avvia il server come processo figlio
- Comunicazione via stdin/stdout usando messaggi JSON-RPC
- Nessuna configurazione di server HTTP richiesta
- Migliore performance e sicurezza
- Debug e sviluppo facilitati

**Trasporto SSE (deprecato dal MCP 2025-06-18):**
- Richiedeva server HTTP con endpoint SSE
- Configurazione più complessa con infrastruttura web server
- Considerazioni di sicurezza aggiuntive per endpoint HTTP
- Ora sostituito da Streamable HTTP per scenari web

### Creare un server con trasporto stdio

Per creare il nostro server stdio, dobbiamo:

1. **Importare le librerie richieste** - Abbiamo bisogno dei componenti server MCP e del trasporto stdio
2. **Creare un'istanza server** - Definire il server con le sue capacità
3. **Definire gli strumenti** - Aggiungere le funzionalità da esporre
4. **Configurare il trasporto** - Configurare la comunicazione stdio
5. **Avviare il server** - Avviare il server e gestire i messaggi

Costruiamolo passo dopo passo:

### Step 1: Creare un server stdio base

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configura la registrazione
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crea il server
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

### Step 2: Aggiungere più strumenti

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

### Step 3: Avviare il server

Salva il codice come `server.py` ed eseguilo da linea di comando:

```bash
python server.py
```

Il server partirà e attenderà input da stdin. Comunica usando messaggi JSON-RPC sul trasporto stdio.

### Step 4: Testare con l'Inspector

Puoi testare il tuo server usando l'MCP Inspector:

1. Installa l'Inspector: `npx @modelcontextprotocol/inspector`
2. Avvia l'Inspector e puntalo sul tuo server
3. Testa gli strumenti che hai creato

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debug del tuo server stdio

### Usare l'MCP Inspector

L'MCP Inspector è uno strumento utile per il debug e il test dei server MCP. Ecco come usarlo con il tuo server stdio:

1. **Installa l'Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Avvia l'Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testa il tuo server**: L'Inspector fornisce un'interfaccia web dove puoi:
   - Visualizzare le capacità del server
   - Testare gli strumenti con diversi parametri
   - Monitorare i messaggi JSON-RPC
   - Fare debug di problemi di connessione

### Usare VS Code

Puoi anche fare il debug del tuo server MCP direttamente in VS Code:

1. Crea una configurazione di avvio in `.vscode/launch.json`:
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

2. Imposta breakpoint nel codice del server
3. Avvia il debugger e testa con l'Inspector

### Consigli comuni per il debug

- Usa `stderr` per il logging - non scrivere mai su `stdout` che è riservato ai messaggi MCP
- Assicurati che tutti i messaggi JSON-RPC siano delimitati da newline
- Testa prima con strumenti semplici prima di aggiungere funzionalità complesse
- Usa l'Inspector per verificare i formati dei messaggi

## Consumare il tuo server stdio in VS Code

Una volta costruito il tuo server MCP stdio, puoi integrarlo con VS Code per usarlo con Claude o altri client compatibili MCP.

### Configurazione

1. **Crea un file di configurazione MCP** in `%APPDATA%\Claude\claude_desktop_config.json` (Windows) o `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac):

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

2. **Riavvia Claude**: Chiudi e riapri Claude per caricare la nuova configurazione server.

3. **Testa la connessione**: Avvia una conversazione con Claude e prova ad usare gli strumenti del tuo server:
   - "Puoi salutarmi usando lo strumento greeting?"
   - "Calcola la somma di 15 e 27"
   - "Quali sono le informazioni del server?"

### Esempio di server stdio in TypeScript

Ecco un esempio completo in TypeScript come riferimento:

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

// Aggiungi strumenti
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

### Esempio di server stdio in .NET

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

## Riepilogo

In questa lezione aggiornata, hai imparato a:

- Costruire server MCP usando l'attuale **trasporto stdio** (approccio consigliato)
- Capire perché il trasporto SSE è stato deprecato a favore di stdio e Streamable HTTP
- Creare strumenti richiamabili dai client MCP
- Effettuare debug del server usando l'MCP Inspector
- Integrare il server stdio con VS Code e Claude

Il trasporto stdio fornisce un modo più semplice, sicuro e performante per creare server MCP rispetto all'approccio SSE deprecato. È il trasporto consigliato per la maggior parte delle implementazioni MCP a partire dalla specifica 2025-06-18.


### .NET

1. Creiamo prima alcuni strumenti, per questo creeremo un file *Tools.cs* con il seguente contenuto:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Esercizio: Testare il tuo server stdio

Ora che hai costruito il tuo server stdio, testiamolo per assicurarci che funzioni correttamente.

### Prerequisiti

1. Assicurati di avere installato l'MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Il codice del tuo server dovrebbe essere salvato (esempio `server.py`)

### Test con l'Inspector

1. **Avvia l'Inspector con il tuo server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Apri l'interfaccia web**: L'Inspector aprirà una finestra del browser mostrando le capacità del tuo server.

3. **Testa gli strumenti**: 
   - Prova lo strumento `get_greeting` con nomi diversi
   - Testa lo strumento `calculate_sum` con numeri vari
   - Chiama lo strumento `get_server_info` per vedere i metadati del server

4. **Monitora la comunicazione**: L'Inspector mostra i messaggi JSON-RPC scambiati fra client e server.

### Cosa dovresti vedere

Quando il server parte correttamente, dovresti vedere:
- Capacità del server elencate nell'Inspector
- Strumenti disponibili per il test
- Scambi di messaggi JSON-RPC avvenuti con successo
- Risposte agli strumenti visualizzate nell'interfaccia

### Problemi comuni e soluzioni

**Il server non parte:**
- Controlla che tutte le dipendenze siano installate: `pip install mcp`
- Verifica la sintassi e l'indentazione di Python
- Cerca messaggi di errore in console

**Gli strumenti non compaiono:**
- Assicurati che i decorator `@server.tool()` siano presenti
- Verifica che le funzioni degli strumenti siano definite prima di `main()`
- Controlla che il server sia configurato correttamente

**Problemi di connessione:**
- Assicurati che il server stia usando correttamente il trasporto stdio
- Verifica che nessun altro processo interferisca
- Controlla la sintassi del comando per l'Inspector

## Compito

Prova a espandere il tuo server con più capacità. Consulta [questa pagina](https://api.chucknorris.io/) per esempio per aggiungere uno strumento che chiami un'API. Decidi tu come deve essere il server. Divertiti :)
## Soluzione

[Soluzione](./solution/README.md) Ecco una possibile soluzione con codice funzionante.

## Punti chiave

I punti chiave di questo capitolo sono i seguenti:

- Il trasporto stdio è il meccanismo raccomandato per i server MCP locali.
- Il trasporto stdio permette una comunicazione fluida tra server MCP e client usando flussi di input e output standard.
- Puoi usare sia Inspector che Visual Studio Code per consumare direttamente i server stdio, facilitando debug e integrazione.

## Esempi 

- [Calcolatrice Java](../samples/java/calculator/README.md)
- [Calcolatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calcolatrice JavaScript](../samples/javascript/README.md)
- [Calcolatrice TypeScript](../samples/typescript/README.md)
- [Calcolatrice Python](../../../../03-GettingStarted/samples/python) 

## Risorse aggiuntive

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Cosa c'è dopo

## Prossimi passi

Ora che hai imparato a costruire server MCP con il trasporto stdio, puoi esplorare argomenti più avanzati:

- **Successivo**: [HTTP Streaming con MCP (Streamable HTTP)](../06-http-streaming/README.md) - Scopri l'altro meccanismo di trasporto supportato per server remoti
- **Avanzato**: [Best Practices per la sicurezza MCP](../../02-Security/README.md) - Implementa la sicurezza nei tuoi server MCP
- **Produzione**: [Strategie di Deployment](../09-deployment/README.md) - Distribuisci i tuoi server per uso in produzione

## Risorse aggiuntive

- [Specifiche MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Specifica ufficiale
- [Documentazione MCP SDK](https://github.com/modelcontextprotocol/sdk) - Riferimenti SDK per tutti i linguaggi
- [Esempi dalla community](../../06-CommunityContributions/README.md) - Altri esempi di server dalla comunità

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci sforziamo di garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale umana. Non ci assumiamo alcuna responsabilità per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->