# Creazione di un client

I client sono applicazioni personalizzate o script che comunicano direttamente con un MCP Server per richiedere risorse, strumenti e prompt. A differenza dell'uso dello strumento inspector, che fornisce un'interfaccia grafica per interagire con il server, scrivere un proprio client permette interazioni programmatiche e automatizzate. Ciò consente agli sviluppatori di integrare le capacità di MCP nei propri flussi di lavoro, automatizzare attività e costruire soluzioni personalizzate su misura per esigenze specifiche.

## Panoramica

Questa lezione introduce il concetto di client all'interno dell'ecosistema del Model Context Protocol (MCP). Imparerai come scrivere il tuo client e farlo connettere a un MCP Server.

## Obiettivi di apprendimento

Al termine di questa lezione, sarai in grado di:

- Comprendere cosa può fare un client.
- Scrivere il proprio client.
- Connettere e testare il client con un server MCP per assicurarti che funzioni come previsto.

## Cosa comporta scrivere un client?

Per scrivere un client, dovrai fare quanto segue:

- **Importare le librerie corrette**. Userai la stessa libreria di prima, solo costrutti diversi.
- **Istanziare un client**. Questo comporterà la creazione di un'istanza client e la connessione al metodo di trasporto scelto.
- **Decidere quali risorse elencare**. Il tuo server MCP dispone di risorse, strumenti e prompt; devi decidere quali elencare.
- **Integrare il client in un'applicazione host**. Una volta conosciute le capacità del server, devi integrare tutto nella tua applicazione host affinché se un utente digita un prompt o un altro comando venga invocata la funzione corrispondente del server.

Ora che abbiamo una visione generale di ciò che stiamo per fare, diamo un'occhiata a un esempio successivamente.

### Un esempio di client

Diamo un'occhiata a questo esempio di client:

### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);

// Elenca i prompt
const prompts = await client.listPrompts();

// Ottieni un prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Elenca le risorse
const resources = await client.listResources();

// Leggi una risorsa
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Chiama uno strumento
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Nel codice precedente abbiamo:

- Importato le librerie
- Creato un'istanza di un client e connesso usando stdio come trasporto.
- Elencato prompt, risorse e strumenti e invocati tutti.

Ecco fatto, un client che può comunicare con un MCP Server.

Prendiamoci il nostro tempo nella prossima sezione esercizi per analizzare ogni frammento di codice e spiegare cosa succede.

## Esercizio: Scrivere un client

Come detto sopra, prendiamoci il nostro tempo per spiegare il codice e, se vuoi, scrivilo tu stesso insieme a noi.

### -1- Importare le librerie

Importiamo le librerie di cui abbiamo bisogno, ci serviranno riferimenti a un client e al nostro protocollo di trasporto scelto, stdio. stdio è un protocollo per cose che devono girare sulla tua macchina locale. SSE è un altro protocollo di trasporto che mostreremo nei capitoli futuri ma questa è l'altra opzione. Per ora però continuiamo con stdio.

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
```

#### .NET

```csharp
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
```

#### Java

Per Java, creerai un client che si connette al server MCP dall'esercizio precedente. Usando la stessa struttura del progetto Java Spring Boot di [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), crea una nuova classe Java chiamata `SDKClient` nella cartella `src/main/java/com/microsoft/mcp/sample/client/` e aggiungi le seguenti importazioni:

```java
import java.util.Map;
import org.springframework.web.reactive.function.client.WebClient;
import io.modelcontextprotocol.client.McpClient;
import io.modelcontextprotocol.client.transport.WebFluxSseClientTransport;
import io.modelcontextprotocol.spec.McpClientTransport;
import io.modelcontextprotocol.spec.McpSchema.CallToolRequest;
import io.modelcontextprotocol.spec.McpSchema.CallToolResult;
import io.modelcontextprotocol.spec.McpSchema.ListToolsResult;
```

#### Rust

Dovrai aggiungere le seguenti dipendenze al tuo file `Cargo.toml`.

```toml
[package]
name = "calculator-client"
version = "0.1.0"
edition = "2024"

[dependencies]
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

Da lì puoi importare le librerie necessarie nel codice del tuo client.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Passiamo all'istanza.

### -2- Istanziare client e trasporto

Dovremo creare un'istanza del trasporto e una del nostro client:

#### TypeScript

```typescript
const transport = new StdioClientTransport({
  command: "node",
  args: ["server.js"]
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

await client.connect(transport);
```

Nel codice precedente abbiamo:

- Creato un'istanza di trasporto stdio. Nota come specifica comando e argomenti per trovare e avviare il server, cosa che dovremo fare mentre creiamo il client.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Istantato un client dandogli un nome e una versione.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Connesso il client al trasporto scelto.

    ```typescript
    await client.connect(transport);
    ```

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Crea parametri del server per la connessione stdio
server_params = StdioServerParameters(
    command="mcp",  # Eseguibile
    args=["run", "server.py"],  # Argomenti della riga di comando opzionali
    env=None,  # Variabili d'ambiente opzionali
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inizializza la connessione
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Nel codice precedente abbiamo:

- Importato le librerie necessarie
- Istantato un oggetto parametri server poiché lo useremo per avviare il server in modo da poterci connettere con il nostro client.
- Definito un metodo `run` che a sua volta chiama `stdio_client` che avvia una sessione client.
- Creato un punto di ingresso dove passiamo il metodo `run` a `asyncio.run`.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;

var builder = Host.CreateApplicationBuilder(args);

builder.Configuration
    .AddEnvironmentVariables()
    .AddUserSecrets<Program>();



var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "dotnet",
    Arguments = ["run", "--project", "path/to/file.csproj"],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

Nel codice precedente abbiamo:

- Importato le librerie necessarie.
- Creato un trasporto stdio e creato un client `mcpClient`. Quest'ultimo è qualcosa che useremo per elencare e invocare funzionalità sul MCP Server.

Nota, in "Arguments", puoi indicare sia il *.csproj* sia l'eseguibile.

#### Java

```java
public class SDKClient {
    
    public static void main(String[] args) {
        var transport = new WebFluxSseClientTransport(WebClient.builder().baseUrl("http://localhost:8080"));
        new SDKClient(transport).run();
    }
    
    private final McpClientTransport transport;

    public SDKClient(McpClientTransport transport) {
        this.transport = transport;
    }

    public void run() {
        var client = McpClient.sync(this.transport).build();
        client.initialize();
        
        // La logica del tuo client va qui
    }
}
```

Nel codice precedente abbiamo:

- Creato un metodo main che imposta un trasporto SSE puntato su `http://localhost:8080` dove il nostro MCP server sarà attivo.
- Creato una classe client che prende il trasporto come parametro del costruttore.
- Nel metodo `run` creiamo un client MCP sincrono usando il trasporto e inizializziamo la connessione.
- Usato il trasporto SSE (Server-Sent Events) che è adatto per comunicazioni HTTP con server MCP Java Spring Boot.

#### Rust

Nota che questo client Rust assume che il server sia un progetto fratello chiamato "calculator-server" nella stessa directory. Il codice sottostante avvierà il server e si connetterà ad esso.

```rust
async fn main() -> Result<(), RmcpError> {
    // Si presume che il server sia un progetto fratello chiamato "calculator-server" nella stessa directory
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .expect("failed to locate workspace root")
        .join("calculator-server");

    let client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: Inizializzare

    // TODO: Elencare gli strumenti

    // TODO: Chiamare lo strumento add con argomenti = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Elencare le funzionalità del server

Ora abbiamo un client che può connettersi se il programma viene eseguito. Tuttavia, non elenca le sue funzionalità, facciamolo adesso:

#### TypeScript

```typescript
// Elenca i prompt
const prompts = await client.listPrompts();

// Elenca le risorse
const resources = await client.listResources();

// elenca gli strumenti
const tools = await client.listTools();
```

#### Python

```python
# Elenca le risorse disponibili
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Elenca gli strumenti disponibili
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Qui elenchiamo le risorse disponibili, `list_resources()` e gli strumenti, `list_tools`, e li stampiamo.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Sopra un esempio di come elencare gli strumenti sul server. Per ogni strumento stampiamo poi il nome.

#### Java

```java
// Elenca e dimostra gli strumenti
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Puoi anche eseguire il ping del server per verificare la connessione
client.ping();
```

Nel codice precedente abbiamo:

- Chiamato `listTools()` per ottenere tutti gli strumenti disponibili dal server MCP.
- Usato `ping()` per verificare che la connessione al server funzioni.
- Il `ListToolsResult` contiene informazioni su tutti gli strumenti, inclusi nomi, descrizioni e schemi di input.

Ottimo, ora abbiamo acquisito tutte le funzionalità. Ora la domanda è: quando le usiamo? Questo client è piuttosto semplice, nel senso che dovremo chiamare esplicitamente le funzionalità quando le vogliamo. Nel prossimo capitolo, creeremo un client più avanzato che ha accesso a un proprio modello linguistico grande, LLM. Per ora però vediamo come possiamo invocare le funzionalità sul server:

#### Rust

Nella funzione main, dopo aver inizializzato il client, possiamo inizializzare il server ed elencare alcune delle sue caratteristiche.

```rust
// Inizializzare
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Elencare gli strumenti
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocare le funzionalità

Per invocare le funzionalità dobbiamo assicurarci di specificare gli argomenti corretti e in alcuni casi il nome di ciò che stiamo cercando di invocare.

#### TypeScript

```typescript

// Leggi una risorsa
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Chiama uno strumento
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// chiama prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Nel codice precedente abbiamo:

- Letto una risorsa, la chiamiamo usando `readResource()` specificando `uri`. Ecco come dovrebbe apparire il lato server:

    ```typescript
    server.resource(
        "readFile",
        new ResourceTemplate("file://{name}", { list: undefined }),
        async (uri, { name }) => ({
          contents: [{
            uri: uri.href,
            text: `Hello, ${name}!`
          }]
        })
    );
    ```

    Il nostro valore `uri` `file://example.txt` corrisponde a `file://{name}` sul server. `example.txt` sarà mappato a `name`.

- Chiamato uno strumento, lo invochiamo specificando il suo `name` e i suoi `arguments` così:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Ottenuto un prompt, per ottenerlo chiami `getPrompt()` con `name` e `arguments`. Il codice del server è così:

    ```typescript
    server.prompt(
        "review-code",
        { code: z.string() },
        ({ code }) => ({
            messages: [{
            role: "user",
            content: {
                type: "text",
                text: `Please review this code:\n\n${code}`
            }
            }]
        })
    );
    ```

    e quindi il codice risultante del client sarà così per corrispondere a quanto dichiarato sul server:

    ```typescript
    const promptResult = await client.getPrompt({
        name: "review-code",
        arguments: {
            code: "console.log(\"Hello world\")"
        }
    })
    ```

#### Python

```python
# Leggi una risorsa
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Chiama uno strumento
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Nel codice precedente abbiamo:

- Chiamato una risorsa chiamata `greeting` usando `read_resource`.
- Invocato uno strumento chiamato `add` usando `call_tool`.

#### .NET

1. Aggiungiamo un po’ di codice per chiamare uno strumento:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Per stampare il risultato, ecco un codice per gestirlo:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Chiama vari strumenti della calcolatrice
CallToolResult resultAdd = client.callTool(new CallToolRequest("add", Map.of("a", 5.0, "b", 3.0)));
System.out.println("Add Result = " + resultAdd);

CallToolResult resultSubtract = client.callTool(new CallToolRequest("subtract", Map.of("a", 10.0, "b", 4.0)));
System.out.println("Subtract Result = " + resultSubtract);

CallToolResult resultMultiply = client.callTool(new CallToolRequest("multiply", Map.of("a", 6.0, "b", 7.0)));
System.out.println("Multiply Result = " + resultMultiply);

CallToolResult resultDivide = client.callTool(new CallToolRequest("divide", Map.of("a", 20.0, "b", 4.0)));
System.out.println("Divide Result = " + resultDivide);

CallToolResult resultHelp = client.callTool(new CallToolRequest("help", Map.of()));
System.out.println("Help = " + resultHelp);
```

Nel codice precedente abbiamo:

- Chiamato più strumenti di calcolatrice usando il metodo `callTool()` con oggetti `CallToolRequest`.
- Ogni chiamata specifica il nome dello strumento e una `Map` di argomenti necessari a quello strumento.
- Gli strumenti del server si aspettano nomi di parametri specifici (come "a", "b" per operazioni matematiche).
- I risultati sono restituiti come oggetti `CallToolResult` contenenti la risposta del server.

#### Rust

```rust
// Chiama lo strumento add con argomenti = {"a": 3, "b": 2}
let a = 3;
let b = 2;
let tool_result = client
    .call_tool(CallToolRequestParam {
        name: "add".into(),
        arguments: serde_json::json!({ "a": a, "b": b }).as_object().cloned(),
    })
    .await?;
println!("Result of {:?} + {:?}: {:?}", a, b, tool_result);
```

### -5- Eseguire il client

Per eseguire il client, digita il comando seguente nel terminale:

#### TypeScript

Aggiungi la seguente voce nella sezione "scripts" in *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Esegui il client con il seguente comando:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Prima assicurati che il tuo MCP server sia attivo su `http://localhost:8080`. Poi esegui il client:

```bash
# Costruisci il tuo progetto
./mvnw clean compile

# Esegui il client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

In alternativa, puoi eseguire il progetto client completo fornito nella cartella solution `03-GettingStarted\02-client\solution\java`:

```bash
# Navigare alla directory della soluzione
cd 03-GettingStarted/02-client/solution/java

# Compilare ed eseguire il JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Assegnazione

In questo esercizio, utilizzerai ciò che hai imparato per creare un client, ma creerai un client tutto tuo.

Ecco un server che puoi usare e che devi chiamare tramite il codice del client, vedi se riesci ad aggiungere più funzionalità al server per renderlo più interessante.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Crea un server MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Aggiungi uno strumento di addizione
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Aggiungi una risorsa di saluto dinamico
server.resource(
  "greeting",
  new ResourceTemplate("greeting://{name}", { list: undefined }),
  async (uri, { name }) => ({
    contents: [{
      uri: uri.href,
      text: `Hello, ${name}!`
    }]
  })
);

// Inizia a ricevere messaggi su stdin e inviare messaggi su stdout

async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCPServer started on stdin/stdout");
}

main().catch((error) => {
  console.error("Fatal error: ", error);
  process.exit(1);
});
```

### Python

```python
# server.py
from mcp.server.fastmcp import FastMCP

# Crea un server MCP
mcp = FastMCP("Demo")


# Aggiungi uno strumento di addizione
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Aggiungi una risorsa di saluto dinamica
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

```

### .NET

```csharp
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using ModelContextProtocol.Server;
using System.ComponentModel;

var builder = Host.CreateApplicationBuilder(args);
builder.Logging.AddConsole(consoleLogOptions =>
{
    // Configure all logs to go to stderr
    consoleLogOptions.LogToStandardErrorThreshold = LogLevel.Trace;
});

builder.Services
    .AddMcpServer()
    .WithStdioServerTransport()
    .WithToolsFromAssembly();
await builder.Build().RunAsync();

[McpServerToolType]
public static class CalculatorTool
{
    [McpServerTool, Description("Adds two numbers")]
    public static string Add(int a, int b) => $"Sum {a + b}";
}
```

Vedi questo progetto per come puoi [aggiungere prompt e risorse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Inoltre, controlla questo link per come invocare [prompt e risorse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Nella [sezione precedente](../../../../03-GettingStarted/01-first-server), hai imparato come creare un server MCP semplice con Rust. Puoi continuare a costruire su quello o controllare questo link per ulteriori esempi di server MCP basati su Rust: [Esempi Server MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Soluzione

La **cartella solution** contiene implementazioni complete e pronte all’uso di client che mostrano tutti i concetti trattati in questo tutorial. Ogni soluzione include sia il codice client che server organizzati in progetti separati e autonomi.

### 📁 Struttura della Soluzione

La directory della soluzione è organizzata per linguaggio di programmazione:

```text
solution/
├── typescript/          # TypeScript client with npm/Node.js setup
│   ├── package.json     # Dependencies and scripts
│   ├── tsconfig.json    # TypeScript configuration
│   └── src/             # Source code
├── java/                # Java Spring Boot client project
│   ├── pom.xml          # Maven configuration
│   ├── src/             # Java source files
│   └── mvnw             # Maven wrapper
├── python/              # Python client implementation
│   ├── client.py        # Main client code
│   ├── server.py        # Compatible server
│   └── README.md        # Python-specific instructions
├── dotnet/              # .NET client project
│   ├── dotnet.csproj    # Project configuration
│   ├── Program.cs       # Main client code
│   └── dotnet.sln       # Solution file
├── rust/                # Rust client implementation
|  ├── Cargo.lock        # Cargo lock file
|  ├── Cargo.toml        # Project configuration and dependencies
|  ├── src               # Source code
|  │   └── main.rs       # Main client code
└── server/              # Additional .NET server implementation
    ├── Program.cs       # Server code
    └── server.csproj    # Server project file
```

### 🚀 Cosa Include Ogni Soluzione

Ogni soluzione specifica per linguaggio fornisce:

- **Implementazione client completa** con tutte le funzionalità del tutorial
- **Struttura di progetto funzionante** con dipendenze e configurazioni corrette
- **Script di build e esecuzione** per configurazione e avvio facilitati
- **README dettagliato** con istruzioni specifiche per il linguaggio
- **Esempi di gestione errori** e processo di risultati

### 📖 Utilizzo delle Soluzioni

1. **Naviga nella cartella del linguaggio preferito**:

   ```bash
   cd solution/typescript/    # Per TypeScript
   cd solution/java/          # Per Java
   cd solution/python/        # Per Python
   cd solution/dotnet/        # Per .NET
   ```

2. **Segui le istruzioni nel README** in ogni cartella per:
   - Installare dipendenze
   - Compilare il progetto
   - Eseguire il client

3. **Output di esempio** che dovresti vedere:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Per documentazione completa e istruzioni passo passo, vedi: **[📖 Documentazione della Soluzione](./solution/README.md)**

## 🎯 Esempi Completi

Abbiamo fornito implementazioni complete e funzionanti dei client per tutti i linguaggi di programmazione trattati in questo tutorial. Questi esempi dimostrano tutta la funzionalità descritta sopra e possono essere usati come implementazioni di riferimento o punti di partenza per i tuoi progetti.

### Esempi Completi Disponibili

| Linguaggio | File | Descrizione |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Client Java completo che utilizza trasporto SSE con gestione completa degli errori |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Client C# completo con trasporto stdio e avvio automatico del server |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Client TypeScript completo con pieno supporto al protocollo MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Client Python completo che usa pattern async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Client Rust completo che utilizza Tokio per operazioni asincrone |

Ogni esempio completo include:

- ✅ **Stabilimento della connessione** e gestione degli errori
- ✅ **Scoperta del server** (strumenti, risorse, prompt dove applicabile)
- ✅ **Operazioni calcolatrice** (somma, sottrazione, moltiplicazione, divisione, aiuto)
- ✅ **Elaborazione dei risultati** e output formattato
- ✅ **Gestione completa degli errori**

- ✅ **Codice pulito e documentato** con commenti passo-passo

### Iniziare con esempi completi

1. **Scegli la tua lingua preferita** dalla tabella sopra
2. **Esamina il file di esempio completo** per comprendere l’implementazione completa
3. **Esegui l’esempio** seguendo le istruzioni in [`complete_examples.md`](./complete_examples.md)
4. **Modifica e amplia** l’esempio per il tuo caso d’uso specifico

Per una documentazione dettagliata sull’esecuzione e la personalizzazione di questi esempi, vedi: **[📖 Documentazione degli esempi completi](./complete_examples.md)**

### 💡 Soluzione vs esempi completi

| **Cartella Soluzione** | **Esempi Completi** |
|----------------------|--------------------- |
| Struttura completa del progetto con file di build | Implementazioni in singolo file |
| Pronto per l’esecuzione con dipendenze | Esempi di codice mirati |
| Configurazione simile a produzione | Riferimento educativo |
| Tooling specifico per lingua | Confronto tra linguaggi diversi |

Entrambi gli approcci sono validi - usa la **cartella soluzione** per progetti completi e gli **esempi completi** per apprendimento e riferimento.

## Punti chiave

I punti chiave di questo capitolo riguardo i client sono i seguenti:

- Possono essere usati sia per scoprire che per invocare funzionalità sul server.
- Possono avviare un server mentre si avviano (come in questo capitolo), ma i client possono anche connettersi a server già in esecuzione.
- Sono un ottimo modo per testare le capacità del server accanto ad alternative come l’Inspector, come descritto nel capitolo precedente.

## Risorse aggiuntive

- [Costruire client in MCP](https://modelcontextprotocol.io/quickstart/client)

## Esempi

- [Calcolatrice Java](../samples/java/calculator/README.md)
- [Calcolatrice .NET](../../../../03-GettingStarted/samples/csharp)
- [Calcolatrice JavaScript](../samples/javascript/README.md)
- [Calcolatrice TypeScript](../samples/typescript/README.md)
- [Calcolatrice Python](../../../../03-GettingStarted/samples/python)
- [Calcolatrice Rust](../../../../03-GettingStarted/samples/rust)

## Cosa segue

- Successivo: [Creare un client con un LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->