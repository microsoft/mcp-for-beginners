# Server MCP con trasporto stdio

> **⚠️ Aggiornamento Importante**: A partire dalla specifica MCP 2025-06-18, il trasporto standalone SSE (Server-Sent Events) è stato **deprecato** e sostituito dal trasporto "Streamable HTTP". La specifica MCP attuale definisce due principali meccanismi di trasporto:
> 1. **stdio** - input/output standard (consigliato per server locali)
> 2. **Streamable HTTP** - per server remoti che possono usare SSE internamente
>
> Questa lezione è stata aggiornata per concentrarsi sul **trasporto stdio**, che è l'approccio consigliato per la maggior parte delle implementazioni di server MCP.

Il trasporto stdio permette ai server MCP di comunicare con i client tramite i flussi di input e output standard. Questo è il meccanismo di trasporto più comunemente usato e raccomandato nella specifica MCP attuale, offrendo un modo semplice ed efficiente per costruire server MCP facilmente integrabili con varie applicazioni client.

## Panoramica

Questa lezione tratta come costruire e utilizzare server MCP usando il trasporto stdio.

## Obiettivi di apprendimento

Al termine di questa lezione, sarai in grado di:

- Costruire un server MCP utilizzando il trasporto stdio.
- Eseguire il debug di un server MCP usando l’Inspector.
- Utilizzare un server MCP in Visual Studio Code.
- Comprendere i meccanismi di trasporto MCP attuali e perché stdio è consigliato.

## Trasporto stdio - Come funziona

Il trasporto stdio è uno dei due tipi di trasporto supportati nella specifica MCP attuale (2025-06-18). Ecco come funziona:

- **Comunicazione semplice**: il server legge messaggi JSON-RPC dallo standard input (`stdin`) e invia messaggi allo standard output (`stdout`).
- **Basato su processo**: il client avvia il server MCP come sottoprocesso.
- **Formato messaggi**: messaggi sono singole richieste JSON-RPC, notifiche o risposte, separate da nuove linee.
- **Logging**: il server PUÒ scrivere stringhe UTF-8 sull’errore standard (`stderr`) per scopi di log.

### Requisiti chiave:
- I messaggi DEVONO essere delimitati da nuove linee e NON DEVONO contenere nuove linee incorporate
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
```

Nel codice precedente:

- Importiamo la classe `Server` e `StdioServerTransport` dall’SDK MCP
- Creiamo un'istanza server con configurazione e capacità di base

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

- Creiamo un’istanza server usando l’SDK MCP
- Definiamo strumenti usando decoratori
- Usiamo il gestore di contesto stdio_server per gestire il trasporto

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

La differenza principale dagli SSE è che i server stdio:

- Non necessitano di configurazione web server o endpoint HTTP
- Sono avviati come sottoprocessi dal client
- Comunicano tramite flussi stdin/stdout
- Sono più semplici da implementare e debug

## Esercizio: Creare un server stdio

Per creare il nostro server, dobbiamo tenere a mente due cose:

- Dobbiamo usare un server web per esporre endpoint per connessione e messaggi.

## Laboratorio: Creare un semplice server stdio MCP

In questo laboratorio, creeremo un semplice server MCP usando il trasporto stdio raccomandato. Questo server esporrà strumenti che i client possono chiamare usando il Model Context Protocol standard.

### Prerequisiti

- Python 3.8 o successivo
- MCP Python SDK: `pip install mcp`
- Conoscenza base di programmazione async

Iniziamo creando il nostro primo server MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configura il logging
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

## Differenze chiave rispetto all’approccio SSE deprecato

**Trasporto Stdio (Standard attuale):**
- Modello semplice con sottoprocesso - il client avvia il server come processo figlio
- Comunicazione via stdin/stdout usando messaggi JSON-RPC
- Nessuna configurazione server HTTP richiesta
- Migliore performance e sicurezza
- Debug e sviluppo più semplici

**Trasporto SSE (Deprecato dal MCP 2025-06-18):**
- Richiedeva un server HTTP con endpoint SSE
- Setup più complesso con infrastruttura web server
- Considerazioni di sicurezza aggiuntive per endpoint HTTP
- Ora sostituito da Streamable HTTP per scenari web-based

### Creare un server con trasporto stdio

Per creare il nostro server stdio, dobbiamo:

1. **Importare le librerie necessarie** - Ci servono i componenti server MCP e il trasporto stdio
2. **Creare un’istanza server** - Definire il server con le sue capacità
3. **Definire gli strumenti** - Aggiungere la funzionalità da esporre
4. **Configurare il trasporto** - Configurare la comunicazione stdio
5. **Avviare il server** - Iniziare il server e gestire i messaggi

Costruiamo questo passo dopo passo:

### Passo 1: Creare un server stdio di base

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configura il logging
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

### Passo 2: Aggiungere più strumenti

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

### Passo 3: Avviare il server

Salva il codice come `server.py` e avvialo da linea di comando:

```bash
python server.py
```

Il server partirà e aspetterà input da stdin. Comunica usando messaggi JSON-RPC tramite il trasporto stdio.

### Passo 4: Test con l’Inspector

Puoi testare il tuo server usando il MCP Inspector:

1. Installa l’Inspector: `npx @modelcontextprotocol/inspector`
2. Avvia l’Inspector e indirizzalo al tuo server
3. Prova gli strumenti che hai creato

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```


## Debug del tuo server stdio

### Usare il MCP Inspector

Il MCP Inspector è uno strumento prezioso per fare debug e testare i server MCP. Ecco come usarlo con il tuo server stdio:

1. **Installa l’Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Avvia l’Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testa il tuo server**: L’Inspector fornisce un’interfaccia web dove puoi:
   - Vedere le capacità del server
   - Testare gli strumenti con parametri diversi
   - Monitorare i messaggi JSON-RPC
   - Debuggare problemi di connessione

### Usare VS Code

Puoi anche fare debug del tuo server MCP direttamente in VS Code:

1. Crea una configurazione di lancio in `.vscode/launch.json`:
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

2. Imposta breakpoint nel codice server
3. Avvia il debugger e testa con l’Inspector

### Consigli comuni per il debug

- Usa `stderr` per logging - non scrivere mai su `stdout` che è riservato ai messaggi MCP
- Assicurati che tutti i messaggi JSON-RPC siano delimitati da nuove linee
- Testa prima con strumenti semplici prima di aggiungere funzionalità complesse
- Usa l’Inspector per verificare il formato dei messaggi

## Usare il tuo server stdio in VS Code

Una volta creato il server MCP stdio, puoi integrarlo con VS Code per usarlo con Claude o altri client compatibili MCP.

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

3. **Testa la connessione**: Avvia una conversazione con Claude e prova a usare gli strumenti del tuo server:
   - "Puoi salutarmi usando lo strumento saluto?"
   - "Calcola la somma di 15 e 27"
   - "Quali sono le informazioni del server?"

### Esempio server stdio TypeScript

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

### Esempio server stdio .NET

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

## Riassunto

In questa lezione aggiornata, hai imparato a:

- Costruire server MCP usando l’attuale **trasporto stdio** (approccio consigliato)
- Capire perché il trasporto SSE è stato deprecato a favore di stdio e Streamable HTTP
- Creare strumenti chiamabili dai client MCP
- Fare debug del server usando il MCP Inspector
- Integrare il server stdio con VS Code e Claude

Il trasporto stdio fornisce un modo più semplice, sicuro e performante per costruire server MCP rispetto all’approccio SSE deprecato. È il trasporto consigliato per la maggior parte delle implementazioni server MCP come da specifica 2025-06-18.

### .NET

1. Creiamo prima alcuni strumenti, per questo creeremo un file *Tools.cs* con il seguente contenuto:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Esercizio: Testare il tuo server stdio

Ora che hai costruito il server stdio, testiamolo per assicurarci che funzioni correttamente.

### Prerequisiti

1. Assicurati di avere installato il MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Il codice del tuo server dovrebbe essere salvato (es. come `server.py`)

### Test con l’Inspector

1. **Avvia l’Inspector con il tuo server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Apri l’interfaccia web**: L’Inspector aprirà una finestra browser mostrando le capacità del server.

3. **Testa gli strumenti**:
   - Prova lo strumento `get_greeting` con nomi diversi
   - Testa lo strumento `calculate_sum` con numeri vari
   - Chiama lo strumento `get_server_info` per vedere i metadata del server

4. **Monitora la comunicazione**: L’Inspector mostra i messaggi JSON-RPC scambiati tra client e server.

### Cosa dovresti vedere

Quando il server parte correttamente, dovresti vedere:
- Capacità del server elencate nell’Inspector
- Strumenti disponibili per i test
- Scambi di messaggi JSON-RPC riusciti
- Risposte degli strumenti visualizzate nell’interfaccia

### Problemi comuni e soluzioni

**Il server non parte:**
- Controlla che tutte le dipendenze siano installate: `pip install mcp`
- Verifica sintassi e indentazione Python
- Controlla eventuali messaggi di errore in console

**Strumenti non visibili:**
- Assicurati che i decoratori `@server.tool()` siano presenti
- Controlla che le funzioni degli strumenti siano definite prima di `main()`
- Verifica che il server sia configurato correttamente

**Problemi di connessione:**
- Assicurati che il server usi correttamente il trasporto stdio
- Controlla che nessun altro processo interferisca
- Verifica sintassi del comando dell’Inspector

## Compito

Prova a sviluppare il tuo server con più funzionalità. Dai un’occhiata a [questa pagina](https://api.chucknorris.io/) per esempio per aggiungere uno strumento che chiama un’API. Decidi tu come deve essere il server. Buon divertimento :)

## Soluzione

[Soluzione](./solution/README.md) Ecco una possibile soluzione con codice funzionante.

## Punti chiave

I punti chiave di questo capitolo sono i seguenti:

- Il trasporto stdio è il meccanismo consigliato per server MCP locali.
- Il trasporto stdio permette una comunicazione fluida tra server MCP e client usando i flussi di input e output standard.
- Puoi usare sia Inspector che Visual Studio Code per consumare direttamente i server stdio, rendendo semplice il debug e l’integrazione.

## Esempi

- [Calcolatrice Java](../samples/java/calculator/README.md)
- [Calcolatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calcolatrice JavaScript](../samples/javascript/README.md)
- [Calcolatrice TypeScript](../samples/typescript/README.md)
- [Calcolatrice Python](../../../../03-GettingStarted/samples/python)

## Risorse aggiuntive

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Cosa viene dopo

## Prossimi passi

Ora che hai imparato a costruire server MCP con il trasporto stdio, puoi esplorare argomenti più avanzati:

- **Successivo**: [HTTP Streaming con MCP (Streamable HTTP)](../06-http-streaming/README.md) - Scopri l’altro meccanismo di trasporto supportato per server remoti
- **Avanzato**: [Best Practice di Sicurezza MCP](../../02-Security/README.md) - Implementa la sicurezza nei tuoi server MCP
- **Produzione**: [Strategie di Deployment](../09-deployment/README.md) - Distribuisci i tuoi server in produzione

## Risorse aggiuntive

- [Specifiche MCP 2025-06-18](https://spec.modelcontextprotocol.io/specification/) - Specifica ufficiale
- [Documentazione MCP SDK](https://github.com/modelcontextprotocol/sdk) - Riferimenti SDK per tutti i linguaggi
- [Esempi dalla community](../../06-CommunityContributions/README.md) - Ulteriori esempi di server dalla community

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avvertenza**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione umana professionale. Non ci assumiamo alcuna responsabilità per malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->