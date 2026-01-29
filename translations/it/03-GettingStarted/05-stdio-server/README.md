# Server MCP con trasporto stdio

> **⚠️ Aggiornamento Importante**: A partire dalla specifica MCP del 18-06-2025, il trasporto SSE (Server-Sent Events) standalone è stato **deprecato** e sostituito dal trasporto "Streamable HTTP". La specifica MCP attuale definisce due meccanismi di trasporto principali:
> 1. **stdio** - Input/output standard (raccomandato per server locali)
> 2. **Streamable HTTP** - Per server remoti che possono utilizzare SSE internamente
>
> Questa lezione è stata aggiornata per concentrarsi sul **trasporto stdio**, che rappresenta l'approccio raccomandato per la maggior parte delle implementazioni di server MCP.

Il trasporto stdio consente ai server MCP di comunicare con i client attraverso i flussi di input e output standard. Questo è il meccanismo di trasporto più comunemente utilizzato e raccomandato nella specifica MCP attuale, offrendo un modo semplice ed efficiente per costruire server MCP facilmente integrabili con varie applicazioni client.

## Panoramica

Questa lezione copre come costruire e utilizzare server MCP utilizzando il trasporto stdio.

## Obiettivi di apprendimento

Alla fine di questa lezione, sarai in grado di:

- Costruire un server MCP utilizzando il trasporto stdio.
- Effettuare il debug di un server MCP utilizzando l'Inspector.
- Utilizzare un server MCP con Visual Studio Code.
- Comprendere i meccanismi di trasporto MCP attuali e perché il trasporto stdio è raccomandato.

## Trasporto stdio - Come funziona

Il trasporto stdio è uno dei due tipi di trasporto supportati nella specifica MCP attuale (18-06-2025). Ecco come funziona:

- **Comunicazione semplice**: Il server legge i messaggi JSON-RPC dall'input standard (`stdin`) e invia messaggi all'output standard (`stdout`).
- **Basato su processi**: Il client avvia il server MCP come sottoprocesso.
- **Formato dei messaggi**: I messaggi sono richieste, notifiche o risposte JSON-RPC individuali, delimitati da nuove righe.
- **Logging**: Il server PUÒ scrivere stringhe UTF-8 sull'errore standard (`stderr`) per scopi di logging.

### Requisiti principali:
- I messaggi DEVONO essere delimitati da nuove righe e NON DEVONO contenere nuove righe incorporate.
- Il server NON DEVE scrivere nulla su `stdout` che non sia un messaggio MCP valido.
- Il client NON DEVE scrivere nulla su `stdin` del server che non sia un messaggio MCP valido.

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

- Importiamo la classe `Server` e `StdioServerTransport` dall'SDK MCP.
- Creiamo un'istanza del server con configurazione e capacità di base.

### Python

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Create server instance
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

- Creiamo un'istanza del server utilizzando l'SDK MCP.
- Definiamo gli strumenti utilizzando i decoratori.
- Utilizziamo il gestore di contesto `stdio_server` per gestire il trasporto.

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

La differenza principale rispetto a SSE è che i server stdio:

- Non richiedono configurazione di server web o endpoint HTTP.
- Vengono avviati come sottoprocessi dal client.
- Comunicano tramite flussi stdin/stdout.
- Sono più semplici da implementare e fare il debug.

## Esercizio: Creare un server stdio

Per creare il nostro server, dobbiamo tenere a mente due cose:

- Dobbiamo utilizzare un server web per esporre gli endpoint per connessione e messaggi.

## Laboratorio: Creare un semplice server MCP stdio

In questo laboratorio, creeremo un semplice server MCP utilizzando il trasporto stdio raccomandato. Questo server esporrà strumenti che i client possono chiamare utilizzando il protocollo Model Context.

### Prerequisiti

- Python 3.8 o successivo.
- SDK MCP per Python: `pip install mcp`.
- Comprensione di base della programmazione asincrona.

Iniziamo creando il nostro primo server MCP stdio:

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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
    # Use stdio transport
    async with stdio_server(server) as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
```

## Differenze principali rispetto all'approccio SSE deprecato

**Trasporto stdio (Standard attuale):**
- Modello semplice basato su sottoprocessi - il client avvia il server come processo figlio.
- Comunicazione tramite stdin/stdout utilizzando messaggi JSON-RPC.
- Non è richiesta configurazione di server HTTP.
- Migliori prestazioni e sicurezza.
- Debug e sviluppo più semplici.

**Trasporto SSE (Deprecato dal 18-06-2025):**
- Richiedeva un server HTTP con endpoint SSE.
- Configurazione più complessa con infrastruttura server web.
- Considerazioni aggiuntive sulla sicurezza per gli endpoint HTTP.
- Ora sostituito da Streamable HTTP per scenari basati sul web.

### Creare un server con trasporto stdio

Per creare il nostro server stdio, dobbiamo:

1. **Importare le librerie necessarie** - Componenti del server MCP e trasporto stdio.
2. **Creare un'istanza del server** - Definire il server con le sue capacità.
3. **Definire gli strumenti** - Aggiungere le funzionalità che vogliamo esporre.
4. **Configurare il trasporto** - Configurare la comunicazione stdio.
5. **Eseguire il server** - Avviare il server e gestire i messaggi.

Costruiamo questo passo dopo passo:

### Passo 1: Creare un server stdio di base

```python
import asyncio
import logging
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the server
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

### Passo 3: Eseguire il server

Salva il codice come `server.py` ed eseguilo dalla riga di comando:

```bash
python server.py
```

Il server si avvierà e attenderà input da stdin. Comunica utilizzando messaggi JSON-RPC tramite il trasporto stdio.

### Passo 4: Testare con l'Inspector

Puoi testare il tuo server utilizzando l'MCP Inspector:

1. Installa l'Inspector: `npx @modelcontextprotocol/inspector`.
2. Avvia l'Inspector e puntalo al tuo server.
3. Testa gli strumenti che hai creato.

### .NET

```csharp
var builder = WebApplication.CreateBuilder(args);
builder.Services
    .AddMcpServer();
 ```

## Debug del tuo server stdio

### Utilizzare l'MCP Inspector

L'MCP Inspector è uno strumento prezioso per il debug e il test dei server MCP. Ecco come usarlo con il tuo server stdio:

1. **Installa l'Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector
   ```

2. **Avvia l'Inspector**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

3. **Testa il tuo server**: L'Inspector fornisce un'interfaccia web dove puoi:
   - Visualizzare le capacità del server.
   - Testare gli strumenti con diversi parametri.
   - Monitorare i messaggi JSON-RPC.
   - Effettuare il debug di problemi di connessione.

### Utilizzare VS Code

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

2. Imposta i breakpoint nel codice del server.
3. Avvia il debugger e testa con l'Inspector.

### Suggerimenti comuni per il debug

- Usa `stderr` per il logging - non scrivere mai su `stdout`, riservato ai messaggi MCP.
- Assicurati che tutti i messaggi JSON-RPC siano delimitati da nuove righe.
- Testa prima con strumenti semplici prima di aggiungere funzionalità complesse.
- Usa l'Inspector per verificare i formati dei messaggi.

## Utilizzare il tuo server stdio in VS Code

Una volta costruito il tuo server MCP stdio, puoi integrarlo con VS Code per usarlo con Claude o altri client compatibili con MCP.

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

3. **Testa la connessione**: Inizia una conversazione con Claude e prova a utilizzare gli strumenti del tuo server:
   - "Puoi salutarmi usando lo strumento di saluto?"
   - "Calcola la somma di 15 e 27."
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

// Add tools
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

## Riepilogo

In questa lezione aggiornata, hai imparato a:

- Costruire server MCP utilizzando il trasporto **stdio** (approccio raccomandato).
- Comprendere perché il trasporto SSE è stato deprecato a favore di stdio e Streamable HTTP.
- Creare strumenti che possono essere chiamati dai client MCP.
- Effettuare il debug del tuo server utilizzando l'MCP Inspector.
- Integrare il tuo server stdio con VS Code e Claude.

Il trasporto stdio offre un modo più semplice, sicuro e performante per costruire server MCP rispetto all'approccio SSE deprecato. È il trasporto raccomandato per la maggior parte delle implementazioni di server MCP a partire dalla specifica del 18-06-2025.

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

1. Assicurati di avere l'MCP Inspector installato:
   ```bash
   npm install -g @modelcontextprotocol/inspector
   ```

2. Il codice del tuo server dovrebbe essere salvato (ad esempio, come `server.py`).

### Testare con l'Inspector

1. **Avvia l'Inspector con il tuo server**:
   ```bash
   npx @modelcontextprotocol/inspector python server.py
   ```

2. **Apri l'interfaccia web**: L'Inspector aprirà una finestra del browser mostrando le capacità del tuo server.

3. **Testa gli strumenti**: 
   - Prova lo strumento `get_greeting` con nomi diversi.
   - Testa lo strumento `calculate_sum` con numeri vari.
   - Chiama lo strumento `get_server_info` per vedere i metadati del server.

4. **Monitora la comunicazione**: L'Inspector mostra i messaggi JSON-RPC scambiati tra client e server.

### Cosa dovresti vedere

Quando il tuo server si avvia correttamente, dovresti vedere:
- Le capacità del server elencate nell'Inspector.
- Strumenti disponibili per il test.
- Scambi di messaggi JSON-RPC riusciti.
- Risposte degli strumenti visualizzate nell'interfaccia.

### Problemi comuni e soluzioni

**Il server non si avvia:**
- Controlla che tutte le dipendenze siano installate: `pip install mcp`.
- Verifica la sintassi e l'indentazione di Python.
- Cerca messaggi di errore nella console.

**Gli strumenti non appaiono:**
- Assicurati che i decoratori `@server.tool()` siano presenti.
- Controlla che le funzioni degli strumenti siano definite prima di `main()`.
- Verifica che il server sia configurato correttamente.

**Problemi di connessione:**
- Assicurati che il server utilizzi correttamente il trasporto stdio.
- Controlla che nessun altro processo interferisca.
- Verifica la sintassi del comando dell'Inspector.

## Compito

Prova a espandere il tuo server con più capacità. Consulta [questa pagina](https://api.chucknorris.io/) per aggiungere, ad esempio, uno strumento che chiama un'API. Decidi tu come dovrebbe essere il server. Divertiti :)

## Soluzione

[Soluzione](./solution/README.md) Ecco una possibile soluzione con codice funzionante.

## Punti chiave

I punti chiave di questo capitolo sono i seguenti:

- Il trasporto stdio è il meccanismo raccomandato per i server MCP locali.
- Il trasporto stdio consente una comunicazione fluida tra server MCP e client utilizzando flussi di input e output standard.
- Puoi utilizzare sia l'Inspector che Visual Studio Code per consumare server stdio direttamente, rendendo il debug e l'integrazione semplici.

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

- **Prossimo**: [Streaming HTTP con MCP (Streamable HTTP)](../06-http-streaming/README.md) - Scopri l'altro meccanismo di trasporto supportato per server remoti.
- **Avanzato**: [Migliori pratiche di sicurezza MCP](../../02-Security/README.md) - Implementa la sicurezza nei tuoi server MCP.
- **Produzione**: [Strategie di distribuzione](../09-deployment/README.md) - Distribuisci i tuoi server per l'uso in produzione.

## Risorse aggiuntive

- [Specifiche MCP 18-06-2025](https://spec.modelcontextprotocol.io/specification/) - Specifica ufficiale.
- [Documentazione SDK MCP](https://github.com/modelcontextprotocol/sdk) - Riferimenti SDK per tutti i linguaggi.
- [Esempi della comunità](../../06-CommunityContributions/README.md) - Altri esempi di server dalla comunità.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.