# Creazione di un client

I client sono applicazioni o script personalizzati che comunicano direttamente con un MCP Server per richiedere risorse, strumenti e prompt. A differenza dell'utilizzo dello strumento di ispezione, che fornisce un'interfaccia grafica per interagire con il server, scrivere il proprio client consente interazioni programmatiche e automatizzate. Questo permette agli sviluppatori di integrare le funzionalità MCP nei propri flussi di lavoro, automatizzare attività e creare soluzioni personalizzate su misura per esigenze specifiche.

## Panoramica

Questa lezione introduce il concetto di client all'interno dell'ecosistema del Model Context Protocol (MCP). Imparerai a scrivere il tuo client e a connetterlo a un MCP Server.

## Obiettivi di apprendimento

Alla fine di questa lezione, sarai in grado di:

- Comprendere cosa può fare un client.
- Scrivere il tuo client.
- Connettere e testare il client con un MCP Server per assicurarti che quest'ultimo funzioni come previsto.

## Cosa serve per scrivere un client?

Per scrivere un client, dovrai fare quanto segue:

- **Importare le librerie corrette**. Utilizzerai la stessa libreria di prima, ma con costrutti diversi.
- **Istanziare un client**. Questo comporterà la creazione di un'istanza del client e la connessione al metodo di trasporto scelto.
- **Decidere quali risorse elencare**. Il tuo MCP Server dispone di risorse, strumenti e prompt; devi decidere quali elencare.
- **Integrare il client in un'applicazione host**. Una volta conosciute le capacità del server, devi integrarle nella tua applicazione host in modo che, se un utente digita un prompt o un altro comando, venga invocata la funzione corrispondente del server.

Ora che abbiamo compreso a livello generale cosa stiamo per fare, vediamo un esempio.

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

// List prompts
const prompts = await client.listPrompts();

// Get a prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// List resources
const resources = await client.listResources();

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Nel codice precedente abbiamo:

- Importato le librerie.
- Creato un'istanza di un client e connesso utilizzando stdio come metodo di trasporto.
- Elencato prompt, risorse e strumenti e li abbiamo invocati tutti.

Ecco fatto, un client che può comunicare con un MCP Server.

Dedichiamo del tempo nella prossima sezione di esercizi per analizzare ogni frammento di codice e spiegare cosa sta succedendo.

## Esercizio: Scrivere un client

Come detto sopra, dedichiamo del tempo a spiegare il codice e, se vuoi, puoi seguirlo scrivendo il codice.

### -1- Importare le librerie

Importiamo le librerie necessarie; avremo bisogno di riferimenti a un client e al protocollo di trasporto scelto, stdio. Stdio è un protocollo per cose che devono essere eseguite sulla tua macchina locale. SSE è un altro protocollo di trasporto che mostreremo nei capitoli futuri, ma è l'altra opzione. Per ora, però, continuiamo con stdio.

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
using ModelContextProtocol.Protocol.Transport;
```

#### Java

Per Java, creerai un client che si connette al MCP Server dell'esercizio precedente. Utilizzando la stessa struttura del progetto Java Spring Boot di [Introduzione al MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), crea una nuova classe Java chiamata `SDKClient` nella cartella `src/main/java/com/microsoft/mcp/sample/client/` e aggiungi i seguenti import:

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

Dovrai aggiungere le seguenti dipendenze al file `Cargo.toml`.

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

Da lì, puoi importare le librerie necessarie nel codice del tuo client.

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

Dovremo creare un'istanza del trasporto e del nostro client:

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

- Creato un'istanza di trasporto stdio. Nota come specifica il comando e gli argomenti per trovare e avviare il server, poiché è qualcosa che dovremo fare mentre creiamo il client.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Istanziato un client fornendogli un nome e una versione.

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

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="mcp",  # Executable
    args=["run", "server.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initialize the connection
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Nel codice precedente abbiamo:

- Importato le librerie necessarie.
- Istanziato un oggetto di parametri del server, che utilizzeremo per eseguire il server in modo da poterci connettere con il nostro client.
- Definito un metodo `run` che a sua volta chiama `stdio_client`, avviando una sessione client.
- Creato un punto di ingresso in cui forniamo il metodo `run` a `asyncio.run`.

#### .NET

```dotnet
using Microsoft.Extensions.AI;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol.Transport;

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

await using var mcpClient = await McpClientFactory.CreateAsync(clientTransport);
```

Nel codice precedente abbiamo:

- Importato le librerie necessarie.
- Creato un trasporto stdio e un client `mcpClient`. Quest'ultimo è qualcosa che utilizzeremo per elencare e invocare le funzionalità sul MCP Server.

Nota che, in "Arguments", puoi puntare al file *.csproj* o all'eseguibile.

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
        
        // Your client logic goes here
    }
}
```

Nel codice precedente abbiamo:

- Creato un metodo principale che configura un trasporto SSE puntando a `http://localhost:8080`, dove il nostro MCP Server sarà in esecuzione.
- Creato una classe client che prende il trasporto come parametro del costruttore.
- Nel metodo `run`, abbiamo creato un client MCP sincrono utilizzando il trasporto e inizializzato la connessione.
- Utilizzato il trasporto SSE (Server-Sent Events), adatto per la comunicazione basata su HTTP con i server MCP Java Spring Boot.

#### Rust

Questo client Rust presuppone che il server sia un progetto fratello chiamato "calculator-server" nella stessa directory. Il codice seguente avvierà il server e si connetterà ad esso.

```rust
async fn main() -> Result<(), RmcpError> {
    // Assume the server is a sibling project named "calculator-server" in the same directory
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

    // TODO: Initialize

    // TODO: List tools

    // TODO: Call add tool with arguments = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Elencare le funzionalità del server

Ora abbiamo un client che può connettersi se il programma viene eseguito. Tuttavia, non elenca effettivamente le sue funzionalità, quindi facciamolo ora:

#### TypeScript

```typescript
// List prompts
const prompts = await client.listPrompts();

// List resources
const resources = await client.listResources();

// list tools
const tools = await client.listTools();
```

#### Python

```python
# List available resources
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# List available tools
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Qui elenchiamo le risorse disponibili, `list_resources()`, e gli strumenti, `list_tools`, e li stampiamo.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Sopra c'è un esempio di come possiamo elencare gli strumenti sul server. Per ogni strumento, stampiamo il suo nome.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Nel codice precedente abbiamo:

- Chiamato `listTools()` per ottenere tutti gli strumenti disponibili dal MCP Server.
- Utilizzato `ping()` per verificare che la connessione al server funzioni.
- Il `ListToolsResult` contiene informazioni su tutti gli strumenti, inclusi i loro nomi, descrizioni e schemi di input.

Ottimo, ora abbiamo catturato tutte le funzionalità. La domanda ora è: quando le utilizziamo? Bene, questo client è piuttosto semplice, nel senso che dovremo chiamare esplicitamente le funzionalità quando le vogliamo. Nel prossimo capitolo, creeremo un client più avanzato che avrà accesso al proprio modello linguistico di grandi dimensioni, LLM. Per ora, però, vediamo come possiamo invocare le funzionalità sul server:

#### Rust

Nella funzione principale, dopo aver inizializzato il client, possiamo inizializzare il server ed elencare alcune delle sue funzionalità.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocare le funzionalità

Per invocare le funzionalità, dobbiamo assicurarci di specificare gli argomenti corretti e, in alcuni casi, il nome di ciò che stiamo cercando di invocare.

#### TypeScript

```typescript

// Read a resource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Call a tool
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// call prompt
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Nel codice precedente abbiamo:

- Letto una risorsa, chiamandola con `readResource()` specificando `uri`. Ecco come appare probabilmente sul lato server:

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

- Chiamato uno strumento, specificandone il `name` e gli `arguments` come segue:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Ottenuto un prompt, chiamandolo con `getPrompt()` con `name` e `arguments`. Il codice del server appare così:

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

    e il codice risultante del client appare quindi così per corrispondere a quanto dichiarato sul server:

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
# Read a resource
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Call a tool
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Nel codice precedente abbiamo:

- Chiamato una risorsa chiamata `greeting` utilizzando `read_resource`.
- Invocato uno strumento chiamato `add` utilizzando `call_tool`.

#### .NET

1. Aggiungiamo del codice per chiamare uno strumento:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Per stampare il risultato, ecco del codice per gestirlo:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Call various calculator tools
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

- Chiamato più strumenti del calcolatore utilizzando il metodo `callTool()` con oggetti `CallToolRequest`.
- Ogni chiamata allo strumento specifica il nome dello strumento e una `Map` di argomenti richiesti da quello strumento.
- Gli strumenti del server si aspettano nomi di parametri specifici (come "a", "b" per operazioni matematiche).
- I risultati vengono restituiti come oggetti `CallToolResult` contenenti la risposta dal server.

#### Rust

```rust
// Call add tool with arguments = {"a": 3, "b": 2}
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

Per eseguire il client, digita il seguente comando nel terminale:

#### TypeScript

Aggiungi la seguente voce alla sezione "scripts" in *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Chiama il client con il seguente comando:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Prima, assicurati che il tuo MCP Server sia in esecuzione su `http://localhost:8080`. Poi esegui il client:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

In alternativa, puoi eseguire il progetto completo del client fornito nella cartella della soluzione `03-GettingStarted\02-client\solution\java`:

```bash
# Navigate to the solution directory
cd 03-GettingStarted/02-client/solution/java

# Build and run the JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Compito

In questo compito, utilizzerai ciò che hai imparato nella creazione di un client per crearne uno tuo.

Ecco un server che puoi utilizzare e che devi chiamare tramite il tuo codice client; vedi se riesci ad aggiungere più funzionalità al server per renderlo più interessante.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create an MCP server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Add an addition tool
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Add a dynamic greeting resource
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

// Start receiving messages on stdin and sending messages on stdout

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

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Add a dynamic greeting resource
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

Consulta questo progetto per vedere come puoi [aggiungere prompt e risorse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Consulta anche questo link per sapere come invocare [prompt e risorse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Nella [sezione precedente](../../../../03-GettingStarted/01-first-server), hai imparato a creare un semplice MCP Server con Rust. Puoi continuare a costruire su quello o consultare questo link per ulteriori esempi di server MCP basati su Rust: [Esempi di MCP Server](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Soluzione

La **cartella delle soluzioni** contiene implementazioni complete e pronte per l'uso del client che dimostrano tutti i concetti trattati in questo tutorial. Ogni soluzione include sia il codice del client che quello del server organizzati in progetti separati e autonomi.

### 📁 Struttura della soluzione

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

### 🚀 Cosa include ogni soluzione

Ogni soluzione specifica per linguaggio fornisce:

- **Implementazione completa del client** con tutte le funzionalità del tutorial.
- **Struttura del progetto funzionante** con dipendenze e configurazione adeguate.
- **Script di build ed esecuzione** per una configurazione e un'esecuzione facili.
- **README dettagliato** con istruzioni specifiche per il linguaggio.
- **Esempi di gestione degli errori** e elaborazione dei risultati.

### 📖 Utilizzo delle soluzioni

1. **Naviga nella cartella del linguaggio preferito**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Segui le istruzioni del README** in ogni cartella per:
   - Installare le dipendenze.
   - Compilare il progetto.
   - Eseguire il client.

3. **Esempio di output** che dovresti vedere:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Per la documentazione completa e le istruzioni passo-passo, consulta: **[📖 Documentazione della soluzione](./solution/README.md)**

## 🎯 Esempi completi

Abbiamo fornito implementazioni complete e funzionanti del client per tutti i linguaggi di programmazione trattati in questo tutorial. Questi esempi dimostrano la piena funzionalità descritta sopra e possono essere utilizzati come implementazioni di riferimento o punti di partenza per i tuoi progetti.

### Esempi completi disponibili

| Linguaggio | File | Descrizione |
|------------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Client Java completo che utilizza il trasporto SSE con gestione completa degli errori |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Client C# completo che utilizza il trasporto stdio con avvio automatico del server |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Client TypeScript completo con supporto completo al protocollo MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Client Python completo che utilizza pattern async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Client Rust completo che utilizza Tokio per operazioni asincrone |
Ogni esempio completo include:

- ✅ **Stabilire la connessione** e gestione degli errori
- ✅ **Scoperta del server** (strumenti, risorse, suggerimenti dove applicabile)
- ✅ **Operazioni della calcolatrice** (somma, sottrazione, moltiplicazione, divisione, aiuto)
- ✅ **Elaborazione dei risultati** e output formattato
- ✅ **Gestione completa degli errori**
- ✅ **Codice pulito e documentato** con commenti passo-passo

### Iniziare con Esempi Completi

1. **Scegli la tua lingua preferita** dalla tabella sopra
2. **Esamina il file dell'esempio completo** per comprendere l'implementazione completa
3. **Esegui l'esempio** seguendo le istruzioni in [`complete_examples.md`](./complete_examples.md)
4. **Modifica ed estendi** l'esempio per il tuo caso d'uso specifico

Per una documentazione dettagliata su come eseguire e personalizzare questi esempi, consulta: **[📖 Documentazione Esempi Completi](./complete_examples.md)**

### 💡 Soluzione vs. Esempi Completi

| **Cartella Soluzione** | **Esempi Completi** |
|------------------------|--------------------- |
| Struttura completa del progetto con file di build | Implementazioni in un singolo file |
| Pronto per l'esecuzione con dipendenze | Esempi di codice mirati |
| Configurazione simile a quella di produzione | Riferimento educativo |
| Strumenti specifici per linguaggio | Confronto tra linguaggi |

Entrambi gli approcci sono utili: utilizza la **cartella soluzione** per progetti completi e gli **esempi completi** per apprendimento e riferimento.

## Punti Chiave

I punti chiave di questo capitolo riguardano i client:

- Possono essere utilizzati sia per scoprire che per invocare funzionalità sul server.
- Possono avviare un server mentre si avviano (come in questo capitolo), ma i client possono anche connettersi a server già in esecuzione.
- Sono un ottimo modo per testare le capacità del server, accanto ad alternative come l'Inspector descritto nel capitolo precedente.

## Risorse Aggiuntive

- [Creare client in MCP](https://modelcontextprotocol.io/quickstart/client)

## Esempi

- [Calcolatrice Java](../samples/java/calculator/README.md)
- [Calcolatrice .Net](../../../../03-GettingStarted/samples/csharp)
- [Calcolatrice JavaScript](../samples/javascript/README.md)
- [Calcolatrice TypeScript](../samples/typescript/README.md)
- [Calcolatrice Python](../../../../03-GettingStarted/samples/python)
- [Calcolatrice Rust](../../../../03-GettingStarted/samples/rust)

## Cosa Viene Dopo

- Prossimo: [Creare un client con un LLM](../03-llm-client/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.