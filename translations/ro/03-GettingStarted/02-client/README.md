# Crearea unui client

Clienții sunt aplicații personalizate sau scripturi care comunică direct cu un server MCP pentru a solicita resurse, unelte și prompturi. Spre deosebire de utilizarea instrumentului inspector, care oferă o interfață grafică pentru interacțiunea cu serverul, scrierea propriului client permite interacțiuni programatice și automatizate. Acest lucru le permite dezvoltatorilor să integreze capabilitățile MCP în propriile fluxuri de lucru, să automatizeze sarcini și să construiască soluții personalizate adaptate nevoilor specifice.

## Prezentare generală

Această lecție introduce conceptul de clienți în ecosistemul Model Context Protocol (MCP). Vei învăța cum să scrii propriul client și să-l conectezi la un server MCP.

## Obiective de învățare

Până la sfârșitul acestei lecții, vei putea:

- Înțelege ce poate face un client.
- Scrie propriul client.
- Conecta și testa clientul cu un server MCP pentru a te asigura că acesta funcționează conform așteptărilor.

## Ce implică scrierea unui client?

Pentru a scrie un client, va trebui să faci următoarele:

- **Importă bibliotecile corecte**. Vei folosi aceeași bibliotecă ca înainte, doar construcții diferite.
- **Instanțiază un client**. Acest lucru va implica crearea unei instanțe de client și conectarea acesteia la metoda de transport aleasă.
- **Decide ce resurse să listezi**. Serverul MCP vine cu resurse, unelte și prompturi, iar tu trebuie să decizi pe care să le listezi.
- **Integrează clientul într-o aplicație gazdă**. Odată ce cunoști capabilitățile serverului, trebuie să integrezi acest client în aplicația gazdă astfel încât, dacă un utilizator introduce un prompt sau o altă comandă, funcționalitatea corespunzătoare a serverului să fie invocată.

Acum că înțelegem la un nivel general ce urmează să facem, să analizăm un exemplu.

### Un exemplu de client

Să aruncăm o privire asupra acestui exemplu de client:

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

În codul precedent am:

- Importat bibliotecile.
- Creat o instanță de client și am conectat-o folosind stdio pentru transport.
- Listat prompturi, resurse și unelte și le-am invocat pe toate.

Iată-l, un client care poate comunica cu un server MCP.

Să ne alocăm timp în secțiunea următoare de exerciții pentru a descompune fiecare fragment de cod și a explica ce se întâmplă.

## Exercițiu: Scrierea unui client

Așa cum am spus mai sus, să ne alocăm timp pentru a explica codul, și, desigur, poți scrie codul în paralel dacă dorești.

### -1- Importarea bibliotecilor

Să importăm bibliotecile de care avem nevoie. Vom avea nevoie de referințe la un client și la protocolul de transport ales, stdio. stdio este un protocol pentru lucruri care rulează pe mașina ta locală. SSE este un alt protocol de transport pe care îl vom prezenta în capitolele viitoare, dar acesta este cealaltă opțiune. Deocamdată, să continuăm cu stdio.

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

Pentru Java, vei crea un client care se conectează la serverul MCP din exercițiul anterior. Folosind aceeași structură de proiect Java Spring Boot din [Introducere în MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), creează o nouă clasă Java numită `SDKClient` în folderul `src/main/java/com/microsoft/mcp/sample/client/` și adaugă următoarele importuri:

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

Va trebui să adaugi următoarele dependențe în fișierul tău `Cargo.toml`.

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

De acolo, poți importa bibliotecile necesare în codul clientului.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Să trecem la instanțiere.

### -2- Instanțierea clientului și transportului

Va trebui să creăm o instanță a transportului și una a clientului nostru:

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

În codul precedent am:

- Creat o instanță de transport stdio. Observă cum specifică comanda și argumentele pentru a găsi și porni serverul, deoarece acesta este un lucru pe care va trebui să-l facem pe măsură ce creăm clientul.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instanțiat un client oferindu-i un nume și o versiune.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Conectat clientul la transportul ales.

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

În codul precedent am:

- Importat bibliotecile necesare.
- Instanțiat un obiect de parametri ai serverului, deoarece îl vom folosi pentru a rula serverul astfel încât să ne putem conecta la el cu clientul nostru.
- Definit o metodă `run` care, la rândul său, apelează `stdio_client`, care pornește o sesiune de client.
- Creat un punct de intrare unde oferim metoda `run` lui `asyncio.run`.

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

În codul precedent am:

- Importat bibliotecile necesare.
- Creat un transport stdio și un client `mcpClient`. Acesta din urmă este ceva ce vom folosi pentru a lista și invoca funcționalități pe serverul MCP.

Notă: În "Arguments", poți indica fie fișierul *.csproj*, fie executabilul.

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

În codul precedent am:

- Creat o metodă principală care configurează un transport SSE indicând către `http://localhost:8080`, unde serverul nostru MCP va rula.
- Creat o clasă client care ia transportul ca parametru al constructorului.
- În metoda `run`, am creat un client MCP sincron folosind transportul și am inițializat conexiunea.
- Folosit transportul SSE (Server-Sent Events), care este potrivit pentru comunicarea bazată pe HTTP cu serverele MCP Java Spring Boot.

#### Rust

Acest client Rust presupune că serverul este un proiect frate numit "calculator-server" în același director. Codul de mai jos va porni serverul și se va conecta la el.

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

### -3- Listarea funcționalităților serverului

Acum avem un client care se poate conecta dacă programul este rulat. Totuși, acesta nu listează efectiv funcționalitățile, așa că să facem asta în continuare:

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

Aici listăm resursele disponibile, `list_resources()` și uneltele, `list_tools`, și le afișăm.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Mai sus este un exemplu despre cum putem lista uneltele de pe server. Pentru fiecare unealtă, afișăm apoi numele acesteia.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

În codul precedent am:

- Apelat `listTools()` pentru a obține toate uneltele disponibile de pe serverul MCP.
- Folosit `ping()` pentru a verifica dacă conexiunea la server funcționează.
- `ListToolsResult` conține informații despre toate uneltele, inclusiv numele, descrierile și schemele de intrare ale acestora.

Minunat, acum am capturat toate funcționalitățile. Întrebarea este: când le folosim? Ei bine, acest client este destul de simplu, în sensul că va trebui să apelăm explicit funcționalitățile atunci când le dorim. În capitolul următor, vom crea un client mai avansat care are acces la propriul model de limbaj mare (LLM). Deocamdată, să vedem cum putem invoca funcționalitățile de pe server:

#### Rust

În funcția principală, după inițializarea clientului, putem inițializa serverul și lista câteva dintre funcționalitățile sale.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocarea funcționalităților

Pentru a invoca funcționalitățile, trebuie să ne asigurăm că specificăm argumentele corecte și, în unele cazuri, numele a ceea ce încercăm să invocăm.

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

În codul precedent am:

- Citit o resursă, apelând resursa cu `readResource()` specificând `uri`. Iată cum ar arăta cel mai probabil pe partea de server:

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

    Valoarea noastră `uri` `file://example.txt` corespunde cu `file://{name}` pe server. `example.txt` va fi mapat la `name`.

- Apelat o unealtă, specificând `name` și `arguments` astfel:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Obținut un prompt, apelând `getPrompt()` cu `name` și `arguments`. Codul serverului arată astfel:

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

    și codul clientului rezultat arată astfel pentru a se potrivi cu ceea ce este declarat pe server:

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

În codul precedent am:

- Apelat o resursă numită `greeting` folosind `read_resource`.
- Invocat o unealtă numită `add` folosind `call_tool`.

#### .NET

1. Să adăugăm cod pentru a apela o unealtă:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Pentru a afișa rezultatul, iată un cod care să gestioneze acest lucru:

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

În codul precedent am:

- Apelat mai multe unelte de calculator folosind metoda `callTool()` cu obiecte `CallToolRequest`.
- Fiecare apel de unealtă specifică numele uneltei și un `Map` de argumente necesare pentru acea unealtă.
- Uneltele serverului așteaptă nume de parametri specifici (cum ar fi "a", "b" pentru operațiuni matematice).
- Rezultatele sunt returnate ca obiecte `CallToolResult` care conțin răspunsul de la server.

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

### -5- Rularea clientului

Pentru a rula clientul, tastează următoarea comandă în terminal:

#### TypeScript

Adaugă următoarea intrare în secțiunea "scripts" din *package.json*:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Apelează clientul cu următoarea comandă:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Mai întâi, asigură-te că serverul MCP rulează pe `http://localhost:8080`. Apoi rulează clientul:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativ, poți rula proiectul complet al clientului furnizat în folderul de soluții `03-GettingStarted\02-client\solution\java`:

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

## Temă

În această temă, vei folosi ceea ce ai învățat pentru a crea un client propriu.

Iată un server pe care îl poți folosi și pe care trebuie să-l apelezi prin codul clientului tău. Vezi dacă poți adăuga mai multe funcționalități serverului pentru a-l face mai interesant.

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

Vezi acest proiect pentru a învăța cum să [adaugi prompturi și resurse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

De asemenea, verifică acest link pentru a învăța cum să invoci [prompturi și resurse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

În [secțiunea anterioară](../../../../03-GettingStarted/01-first-server), ai învățat cum să creezi un server MCP simplu cu Rust. Poți continua să construiești pe acesta sau să verifici acest link pentru mai multe exemple de servere MCP bazate pe Rust: [Exemple de servere MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Soluție

Folderul **solution** conține implementări complete, gata de rulare, ale clienților care demonstrează toate conceptele acoperite în acest tutorial. Fiecare soluție include cod pentru client și server organizat în proiecte separate și independente.

### 📁 Structura soluției

Directorul soluției este organizat pe limbaje de programare:

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

### 🚀 Ce include fiecare soluție

Fiecare soluție specifică limbajului oferă:

- **Implementare completă a clientului** cu toate funcționalitățile din tutorial.
- **Structură de proiect funcțională** cu dependențe și configurații corecte.
- **Scripturi de construire și rulare** pentru configurare și execuție ușoară.
- **README detaliat** cu instrucțiuni specifice limbajului.
- **Exemple de gestionare a erorilor** și procesare a rezultatelor.

### 📖 Utilizarea soluțiilor

1. **Navighează la folderul limbajului preferat**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Urmează instrucțiunile din README** din fiecare folder pentru:
   - Instalarea dependențelor.
   - Construirea proiectului.
   - Rularea clientului.

3. **Exemplu de ieșire** pe care ar trebui să-l vezi:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Pentru documentație completă și instrucțiuni pas cu pas, vezi: **[📖 Documentația soluției](./solution/README.md)**

## 🎯 Exemple complete

Am furnizat implementări complete și funcționale ale clienților pentru toate limbajele de programare acoperite în acest tutorial. Aceste exemple demonstrează funcționalitatea completă descrisă mai sus și pot fi utilizate ca implementări de referință sau puncte de plecare pentru propriile proiecte.

### Exemple complete disponibile

| Limbaj | Fișier | Descriere |
|--------|--------|-----------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Client Java complet folosind transport SSE cu gestionare cuprinzătoare a erorilor |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Client C# complet folosind transport stdio cu pornire automată a serverului |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Client TypeScript complet cu suport complet pentru protocolul MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Client Python complet folosind modele async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Client Rust complet folosind Tokio pentru operațiuni asincrone |
Fiecare exemplu complet include:

- ✅ **Stabilirea conexiunii** și gestionarea erorilor
- ✅ **Descoperirea serverului** (unelte, resurse, sugestii unde este cazul)
- ✅ **Operațiuni ale calculatorului** (adunare, scădere, înmulțire, împărțire, ajutor)
- ✅ **Procesarea rezultatelor** și afișarea formatată
- ✅ **Gestionarea completă a erorilor**
- ✅ **Cod curat, documentat** cu comentarii pas cu pas

### Începeți cu exemple complete

1. **Alegeți limba preferată** din tabelul de mai sus
2. **Revizuiți fișierul de exemplu complet** pentru a înțelege implementarea integrală
3. **Rulați exemplul** urmând instrucțiunile din [`complete_examples.md`](./complete_examples.md)
4. **Modificați și extindeți** exemplul pentru cazul dumneavoastră specific

Pentru documentație detaliată despre rularea și personalizarea acestor exemple, consultați: **[📖 Documentația Exemplului Complet](./complete_examples.md)**

### 💡 Soluție vs. Exemple Complete

| **Folder Soluție** | **Exemple Complete** |
|--------------------|--------------------- |
| Structură completă de proiect cu fișiere de build | Implementări într-un singur fișier |
| Gata de rulat cu toate dependențele | Exemple de cod concentrate |
| Configurație asemănătoare producției | Referință educațională |
| Unelte specifice limbajului | Comparație între limbaje |

Ambele abordări sunt valoroase - utilizați **folderul soluție** pentru proiecte complete și **exemplele complete** pentru învățare și referință.

## Concluzii Cheie

Concluziile cheie pentru acest capitol despre clienți sunt următoarele:

- Pot fi folosiți atât pentru a descoperi, cât și pentru a invoca funcționalități pe server.
- Pot porni un server în timp ce se inițiază (ca în acest capitol), dar clienții se pot conecta și la servere deja pornite.
- Reprezintă o modalitate excelentă de a testa capabilitățile serverului, alături de alternative precum Inspectorul, descris în capitolul anterior.

## Resurse Suplimentare

- [Construirea clienților în MCP](https://modelcontextprotocol.io/quickstart/client)

## Exemple

- [Calculator Java](../samples/java/calculator/README.md)
- [Calculator .Net](../../../../03-GettingStarted/samples/csharp)
- [Calculator JavaScript](../samples/javascript/README.md)
- [Calculator TypeScript](../samples/typescript/README.md)
- [Calculator Python](../../../../03-GettingStarted/samples/python)
- [Calculator Rust](../../../../03-GettingStarted/samples/rust)

## Ce Urmează

- Următorul: [Crearea unui client cu un LLM](../03-llm-client/README.md)

**Declinarea responsabilității**:  
Acest document a fost tradus utilizând serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.