# Server MCP con trasporto stdio

> **⚠️ Aggiornamento Importante**: A partire dalla specifica MCP 2025-06-18, il trasporto SSE (Server-Sent Events) standalone è stato **deprecato** e sostituito dal trasporto "Streamable HTTP". La specifica MCP attuale definisce due principali meccanismi di trasporto:
> 1. **stdio** - Input/output standard (consigliato per server locali)
> 2. **Streamable HTTP** - Per server remoti che possono utilizzare SSE internamente
>
> Questa lezione è stata aggiornata per concentrarsi sul **trasporto stdio**, che è l'approccio raccomandato per la maggior parte delle implementazioni di server MCP.

Il trasporto stdio consente ai server MCP di comunicare con i client tramite flussi di input e output standard. Questo è il meccanismo di trasporto più comunemente utilizzato e raccomandato nella specifica MCP attuale, offrendo un modo semplice ed efficiente per costruire server MCP che possono essere facilmente integrati con varie applicazioni client.

## Panoramica

Questa lezione tratta come costruire e utilizzare Server MCP usando il trasporto stdio.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:

- Costruire un Server MCP usando il trasporto stdio.
- Eseguire il debug di un Server MCP usando l'Inspector.
- Utilizzare un Server MCP con Visual Studio Code.
- Comprendere i meccanismi di trasporto MCP attuali e perché stdio è raccomandato.


## Trasporto stdio - Come funziona

Il trasporto stdio è uno dei due trasporti standard nella Specifica MCP
`2026-07-28`. Ecco come funziona:

- **Comunicazione semplice**: Il server legge messaggi JSON-RPC da input standard (`stdin`) e invia messaggi su output standard (`stdout`).
- **Basato su processo**: Il client avvia il server MCP come processo figlio.
- **Formato messaggi**: I messaggi sono richieste, notifiche o risposte JSON-RPC individuali, delimitati da newline.
- **Logging**: Il server PUÒ scrivere stringhe UTF-8 su errore standard (`stderr`) per scopi di logging.

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

- Importiamo la classe `Server` e `StdioServerTransport` dal MCP SDK
- Creiamo un'istanza del server con configurazione e funzionalità base
- Creiamo un'istanza di `StdioServerTransport` e colleghiamo il server ad essa, abilitando la comunicazione su stdin/stdout

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

- Creiamo un'istanza del server usando MCP SDK
- Definiamo gli strumenti usando i decoratori
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

La differenza principale rispetto a SSE è che i server stdio:

- Non richiedono la configurazione di un server web o endpoint HTTP
- Vengono avviati come processi figli dal client
- Comunicano tramite flussi stdin/stdout
- Sono più semplici da implementare e fare debug

## Esercizio: Creare un server stdio

Per creare il nostro server, dobbiamo tenere a mente due cose:

- Dobbiamo usare un server web per esporre endpoint per connessioni e messaggi.
## Laboratorio: Creare un semplice server MCP stdio

In questo laboratorio, creeremo un semplice server MCP usando il trasporto stdio raccomandato. Questo server esporrà strumenti che i client possono chiamare usando il Model Context Protocol standard.

### Prerequisiti

- Python 3.8 o superiore
- MCP Python SDK: `pip install mcp`
- Conoscenza base della programmazione asincrona

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

## Differenze chiave rispetto all'approccio SSE deprecato

**Trasporto Stdio (Standard Attuale):**
- Modello semplice di processo figlio - il client avvia il server come processo figlio
- Comunicazione tramite stdin/stdout usando messaggi JSON-RPC
- Nessuna configurazione di server HTTP richiesta
- Migliori performance e sicurezza
- Debug e sviluppo più semplici

**Trasporto SSE (Deprecato da MCP 2025-06-18):**
- Richiedeva un server HTTP con endpoint SSE
- Configurazione più complessa con infrastruttura server web
- Ulteriori considerazioni sulla sicurezza per endpoint HTTP
- Ora sostituito da Streamable HTTP per scenari basati su web

### Creare un server con trasporto stdio

Per creare il nostro server stdio, dobbiamo:

1. **Importare le librerie necessarie** - Abbiamo bisogno dei componenti server MCP e del trasporto stdio
2. **Creare un'istanza del server** - Definire il server con le sue funzionalità
3. **Definire gli strumenti** - Aggiungere le funzionalità che vogliamo esporre
4. **Configurare il trasporto** - Configurare la comunicazione stdio
5. **Eseguire il server** - Avviare il server e gestire i messaggi

Costruiamo questo passo dopo passo:

### Passo 1: Creare un server stdio base

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

### Passo 2: Aggiungere altri strumenti

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

### Passo 3: Esecuzione del server

Salva il codice come `server.py` ed eseguilo da linea di comando:

```bash
python server.py
```

Il server si avvierà e attenderà input da stdin. Comunica usando messaggi JSON-RPC sul trasporto stdio.

### Passo 4: Test con l'Inspector

Puoi testare il tuo server usando l'MCP Inspector:

1. Installa l'Inspector: `npx @modelcontextprotocol/inspector`
2. Avvia l'Inspector e punta al tuo server
3. Testa gli strumenti che hai creato

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```
## Debug del tuo server stdio

### Usare l'MCP Inspector

L'MCP Inspector è uno strumento prezioso per il debug e il test di server MCP. Ecco come usarlo con il tuo server stdio:

1. **Installa l'Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Esegui l'Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testa il tuo server**: L'Inspector fornisce un'interfaccia web dove puoi:
   - Vedere le capacità del server
   - Testare gli strumenti con parametri diversi
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

2. Imposta breakpoints nel tuo codice server
3. Avvia il debugger e testa con l'Inspector

### Consigli comuni per il debugging

- Usa `stderr` per il logging - non scrivere mai su `stdout` poiché è riservato ai messaggi MCP
- Assicurati che tutti i messaggi JSON-RPC siano delimitati da newline
- Testa prima con strumenti semplici prima di aggiungere funzionalità complesse
- Usa l'Inspector per verificare i formati dei messaggi

## Utilizzare il tuo server stdio in VS Code


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

2. **Riavvia Claude**: Chiudi e riapri Claude per caricare la nuova configurazione del server.

3. **Testa la connessione**: Avvia una conversazione con Claude e prova a usare gli strumenti del tuo server:
   - "Puoi salutarmi usando lo strumento saluto?"
   - "Calcola la somma di 15 e 27"
   - "Quali sono le informazioni del server?"

### Esempio di server stdio in TypeScript

Ecco un esempio completo in TypeScript per riferimento:

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

## Sommario

In questa lezione aggiornata, hai imparato a:

- Costruire server MCP usando il trasporto **stdio** attuale (approccio consigliato)
- Capire perché il trasporto SSE è stato deprecato a favore di stdio e Streamable HTTP
- Creare strumenti richiamabili dai client MCP
- Eseguire il debug del server usando l’MCP Inspector
- Integrare il server stdio con VS Code e Claude

Il trasporto stdio fornisce un modo più semplice, sicuro e performante per costruire server MCP rispetto all’approccio SSE deprecato. È il trasporto consigliato per la maggior parte delle implementazioni di server MCP dalla specifica del 18-06-2025.


### .NET

1. Prima creiamo alcuni strumenti, per questo creeremo un file *Tools.cs* con il seguente contenuto:

  ```csharp
  using System.ComponentModel;
  using System.Text.Json;
  using ModelContextProtocol.Server;
  ```

## Esercizio: Testare il server stdio

Ora che hai costruito il server stdio, testiamolo per assicurarci che funzioni correttamente.

### Prerequisiti

1. Assicurati di avere installato MCP Inspector:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Il codice del server deve essere salvato (es. come `server.py`)

### Test con l’Inspector

1. **Avvia l’Inspector insieme al server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Apri l’interfaccia web**: L’Inspector aprirà una finestra del browser mostrando le capacità del server.

3. **Testa gli strumenti**: 
   - Prova lo strumento `get_greeting` con nomi diversi
   - Prova lo strumento `calculate_sum` con numeri vari
   - Chiama lo strumento `get_server_info` per vedere i metadati del server

4. **Monitora la comunicazione**: L’Inspector mostra i messaggi JSON-RPC scambiati tra client e server.

### Cosa dovresti vedere

Quando il server parte correttamente, dovresti vedere:
- Le capacità del server elencate nell’Inspector
- Strumenti disponibili per il test
- Scambi di messaggi JSON-RPC avvenuti con successo
- Risposte degli strumenti visualizzate nell’interfaccia

### Problemi comuni e soluzioni

**Il server non si avvia:**
- Controlla che tutte le dipendenze siano installate: `pip install mcp`
- Verifica la sintassi e l’indentazione Python
- Cerca messaggi di errore nella console

**Gli strumenti non compaiono:**
- Assicurati che i decoratori `@server.tool()` siano presenti
- Verifica che le funzioni dello strumento siano definite prima di `main()`
- Controlla che il server sia configurato correttamente

**Problemi di connessione:**
- Assicurati che il server usi correttamente il trasporto stdio
- Verifica che nessun altro processo interferisca
- Controlla la sintassi del comando dell’Inspector

## Compito

Prova ad ampliare il tuo server con più funzionalità. Vedi [questa pagina](https://api.chucknorris.io/) per esempio per aggiungere uno strumento che chiama un’API. Decidi tu come deve essere il server. Divertiti :)
## Soluzione

[Soluzione](./solution/README.md) Ecco una possibile soluzione con codice funzionante.

## Punti chiave

I punti chiave di questo capitolo sono i seguenti:

- Il trasporto stdio è il meccanismo raccomandato per i server MCP locali.
- Il trasporto stdio permette una comunicazione fluida tra server e client MCP usando gli standard input e output.
- Puoi usare sia l’Inspector sia Visual Studio Code per consumare direttamente i server stdio, rendendo semplice il debug e l’integrazione.

## Esempi 

- [Calcolatrice Java](../samples/java/calculator/README.md)
- [Calcolatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calcolatrice JavaScript](../samples/javascript/README.md)
- [Calcolatrice TypeScript](../samples/typescript/README.md)
- [Calcolatrice Python](../../../../03-GettingStarted/samples/python) 

## Risorse aggiuntive

- [SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

## Cosa c’è dopo

## Prossimi passi

Ora che hai imparato a costruire server MCP con il trasporto stdio, puoi esplorare argomenti più avanzati:

- **Successivo**: [Streaming HTTP con MCP (Streamable HTTP)](../06-http-streaming/README.md) - Scopri l’altro meccanismo di trasporto supportato per server remoti
- **Avanzato**: [Best Practice di Sicurezza MCP](../../02-Security/README.md) - Implementa la sicurezza nei tuoi server MCP
- **Produzione**: [Strategie di Deploy](../09-deployment/README.md) - Distribuisci i tuoi server per uso in produzione

## Risorse aggiuntive

- [Specifiche MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/) - Specifica attuale
- [Documentazione SDK MCP](https://github.com/modelcontextprotocol/sdk) - Riferimenti SDK per tutti i linguaggi
- [Esempi dalla comunità](../../06-CommunityContributions/README.md) - Altri esempi di server dalla comunità

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->