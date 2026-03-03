# Crearea unui client

Clienții sunt aplicații sau scripturi personalizate care comunică direct cu un Server MCP pentru a solicita resurse, unelte și solicitări. Spre deosebire de utilizarea instrumentului inspector, care oferă o interfață grafică pentru interacțiunea cu serverul, scrierea propriului client permite interacțiuni programatice și automatizate. Aceasta le permite dezvoltatorilor să integreze capacitățile MCP în fluxurile lor de lucru, să automatizeze sarcini și să construiască soluții personalizate adaptate nevoilor specifice.

## Prezentare generală

Această lecție introduce conceptul de clienți în cadrul ecosistemului Model Context Protocol (MCP). Vei învăța cum să scrii propriul client și să-l conectezi la un Server MCP.

## Obiective de învățare

La finalul acestei lecții vei putea să:

- Înțelegi ce poate face un client.
- Scrii propriul tău client.
- Conectezi și testezi clientul cu un server MCP pentru a verifica dacă acesta funcționează așa cum te aștepți.

## Ce implică scrierea unui client?

Pentru a scrie un client, trebuie să faci următoarele:

- **Importă bibliotecile corecte**. Vei folosi aceeași bibliotecă ca și înainte, doar cu constructe diferite.
- **Instanțiază un client**. Aceasta va implica crearea unei instanțe de client și conectarea acesteia la metoda de transport aleasă.
- **Decide ce resurse să listezi**. Serverul MCP vine cu resurse, unelte și solicitări, trebuie să decizi pe care dintre acestea să le listezi.
- **Integrează clientul într-o aplicație gazdă**. Odată ce știi capabilitățile serverului, trebuie să integrezi asta în aplicația gazdă astfel încât, dacă un utilizator tastează o solicitare sau altă comandă, să fie invocată funcționalitatea corespunzătoare a serverului.

Acum că înțelegem la nivel înalt ce urmează să facem, să vedem următorul exemplu.

### Un exemplu de client

Să aruncăm o privire la acest exemplu de client:

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

// Listează prompturi
const prompts = await client.listPrompts();

// Obține un prompt
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Listează resurse
const resources = await client.listResources();

// Citește o resursă
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Apelează un instrument
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

În codul de mai sus am:

- Importat bibliotecile
- Creat o instanță de client și l-am conectat folosind stdio ca transport.
- Listat solicitările, resursele și uneltele și le-am invocat pe toate.

Iată un client care poate comunica cu un Server MCP.

Vom lua timpul necesar în următoarea secțiune de exerciții pentru a descompune fiecare fragment de cod și a explica ce se întâmplă.

## Exercițiu: Scrierea unui client

După cum am spus mai sus, să luăm tot timpul necesar pentru a explica codul, și bineînțeles, poți scrie codul alături dacă dorești.

### -1- Importarea bibliotecilor

Să importăm bibliotecile de care avem nevoie, vom avea nevoie de referințe către un client și către protocolul de transport ales, stdio. stdio este un protocol pentru lucruri menite să ruleze pe mașina ta locală. SSE este un alt protocol de transport pe care îl vom arăta în capitolele viitoare, dar aceasta este cealaltă opțiune. Pentru acum, însă, să continuăm cu stdio.

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

Pentru Java, vei crea un client care se conectează la serverul MCP din exercițiul anterior. Folosind aceeași structură de proiect Java Spring Boot din [Începerea cu MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), creează o nouă clasă Java numită `SDKClient` în folderul `src/main/java/com/microsoft/mcp/sample/client/` și adaugă următoarele importuri:

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

De acolo, poți importa bibliotecile necesare în codul clientului tău.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Să continuăm cu instanțierea.

### -2- Instanțierea clientului și transportului

Trebuie să creăm o instanță a transportului și o instanță a clientului nostru:

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

În codul de mai sus am:

- Creat o instanță de transport stdio. Observă cum specifică comanda și argumentele pentru cum să găsească și să pornească serverul deoarece asta trebuie să facem în timp ce creăm clientul.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Instanțiat un client dându-i un nume și o versiune.

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

# Creează parametrii serverului pentru conexiunea stdio
server_params = StdioServerParameters(
    command="mcp",  # Executabil
    args=["run", "server.py"],  # Argumente opționale din linia de comandă
    env=None,  # Variabile de mediu opționale
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Inițializează conexiunea
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

În codul de mai sus am:

- Importat bibliotecile necesare
- Instanțiat un obiect de parametri server deoarece îl vom folosi pentru a rula serverul ca să ne putem conecta la el cu clientul nostru.
- Definit o metodă `run` care la rândul ei apelează `stdio_client` care pornește o sesiune de client.
- Creat un punct de intrare unde îi oferim metoda `run` către `asyncio.run`.

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

În codul de mai sus am:

- Importat bibliotecile necesare.
- Creat un transport stdio și un client `mcpClient`. Acesta din urmă îl vom folosi pentru a lista și invoca funcționalități pe Serverul MCP.

Notă, în "Argumente", poți indica fie către *.csproj* fie către executabil.

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
        
        // Logica clientului tău merge aici
    }
}
```

În codul de mai sus am:

- Creat o metodă principală care configurează un transport SSE indicând spre `http://localhost:8080` unde serverul nostru MCP va rula.
- Creat o clasă client care primește transportul ca parametru în constructor.
- În metoda `run`, creăm un client MCP sincron folosind transportul și inițializăm conexiunea.
- Am folosit transportul SSE (Server-Sent Events) care este potrivit pentru comunicații HTTP cu servere MCP Java Spring Boot.

#### Rust

Reține că acest client Rust presupune că serverul este un proiect frate numit "calculator-server" în același director. Codul de mai jos va porni serverul și se va conecta la el.

```rust
async fn main() -> Result<(), RmcpError> {
    // Presupune că serverul este un proiect frate numit "calculator-server" în același director
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

    // TODO: Inițializează

    // TODO: Listează uneltele

    // TODO: Apelează unealta add cu argumentele = {"a": 3, "b": 2}

    client.cancel().await?;
    Ok(())
}
```

### -3- Listarea funcționalităților serverului

Acum avem un client care se poate conecta dacă programul este rulat. Totuși, acesta nu listează efectiv funcționalitățile, așa că să facem asta acum:

#### TypeScript

```typescript
// Listează prompturile
const prompts = await client.listPrompts();

// Listează resursele
const resources = await client.listResources();

// listează uneltele
const tools = await client.listTools();
```

#### Python

```python
# Listează resursele disponibile
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Listează uneltele disponibile
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Aici listăm resursele disponibile, `list_resources()` și uneltele, `list_tools` și le afișăm.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Mai sus este un exemplu despre cum putem lista uneltele de pe server. Pentru fiecare unealtă, afișăm apoi numele său.

#### Java

```java
// Listează și demonstrează uneltele
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Poți, de asemenea, să trimiți un ping serverului pentru a verifica conexiunea
client.ping();
```

În codul de mai sus am:

- Apelat `listTools()` pentru a obține toate uneltele disponibile de pe serverul MCP.
- Folosit `ping()` pentru a verifica dacă conexiunea către server funcționează.
- `ListToolsResult` conține informații despre toate uneltele inclusiv numele, descrierile și schemele de intrare.

Groza, acum am capturat toate funcționalitățile. Acum întrebarea este când le folosim? Ei bine, acest client este destul de simplu, simplu în sensul că trebuie să apelăm explicit funcționalitățile când le dorim. În capitolul următor, vom crea un client mai avansat care are acces la propriul model mare de limbaj, LLM. Pentru acum, hai să vedem cum putem invoca funcționalitățile pe server:

#### Rust

În funcția principală, după inițializarea clientului, putem inițializa serverul și lista unele din funcțiile sale.

```rust
// Inițializează
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Listează uneltele
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Invocarea funcționalităților

Pentru a invoca funcționalitățile trebuie să ne asigurăm că specificăm argumentele corecte și în unele cazuri numele a ceea ce încercăm să invocăm.

#### TypeScript

```typescript

// Citește o resursă
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Apelează un instrument
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// apelează promptul
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

În codul de mai sus am:

- Citit o resursă, o apelăm folosind `readResource()` specificând `uri`. Iată cum arată cel mai probabil pe partea de server:

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

- Apelat o unealtă, o apelăm specificând `name` și `arguments` astfel:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Obținut o solicitare, pentru a obține o solicitare, apelezi `getPrompt()` cu `name` și `arguments`. Codul serverului arată așa:

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

    și codul rezultat pentru client arată așa pentru a se potrivi cu ce este declarat pe server:

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
# Citește o resursă
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Apelează un instrument
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

În codul de mai sus am:

- Apelat o resursă numită `greeting` folosind `read_resource`.
- Invocat o unealtă numită `add` folosind `call_tool`.

#### .NET

1. Să adăugăm ceva cod pentru a apela o unealtă:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Pentru a afișa rezultatul, iată un cod pentru asta:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Apelează diverse instrumente de calculator
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

În codul de mai sus am:

- Apelat multiple unelte de calculator folosind metoda `callTool()` cu obiecte `CallToolRequest`.
- Fiecare apel al unei unelte specifică numele uneltei și un `Map` de argumente cerute de unealtă.
- Uneltele serverului așteaptă anumite nume de parametri (ca "a", "b" pentru operații matematice).
- Rezultatele sunt returnate ca obiecte `CallToolResult` care conțin răspunsul de la server.

#### Rust

```rust
// Apelare instrument add cu argumentele = {"a": 3, "b": 2}
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

Mai întâi, asigură-te că serverul MCP rulează la `http://localhost:8080`. Apoi rulează clientul:

```bash
# Compilează proiectul tău
./mvnw clean compile

# Rulează clientul
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativ, poți rula proiectul complet de client furnizat în folderul de soluții `03-GettingStarted\02-client\solution\java`:

```bash
# Navigați la directorul soluției
cd 03-GettingStarted/02-client/solution/java

# Compilați și rulați JAR-ul
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Tema de lucru

În această temă vei folosi ce ai învățat despre crearea unui client, dar vei crea propriul tău client.

Iată un server pe care îl poți folosi și pe care trebuie să-l apelezi prin codul clientului tău, vezi dacă poți adăuga mai multe funcționalități serverului ca să-l faci mai interesant.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Creează un server MCP
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Adaugă un instrument de adunare
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Adaugă o resursă dinamică de salut
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

// Începe să primești mesaje pe stdin și să trimiți mesaje pe stdout

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

# Creează un server MCP
mcp = FastMCP("Demo")


# Adaugă un instrument de adunare
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Adaugă o resursă de salut dinamică
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

Vezi acest proiect pentru a vedea cum poți [adăuga solicitări și resurse](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

De asemenea, verifică acest link pentru modul de invocare a [solicitărilor și resurselor](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

În [secțiunea precedentă](../../../../03-GettingStarted/01-first-server), ai învățat cum să creezi un server MCP simplu cu Rust. Poți continua să construiești pe această bază sau verifica acest link pentru mai multe exemple de servere MCP bazate pe Rust: [Exemple Server MCP](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Soluția

Folderul **soluției** conține implementări complete și gata de rulare ale clientului care demonstrează toate conceptele acoperite în acest tutorial. Fiecare soluție include atât codul clientului, cât și codul serverului organizate în proiecte separate, autonome.

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

- **Implementare completă a clientului** cu toate funcționalitățile din tutorial
- **Structură de proiect funcțională** cu dependențe și configurări corecte
- **Scripturi de construire și rulare** pentru configurare și execuție ușoară
- **README detaliat** cu instrucțiuni specifice limbajului
- **Exemple de tratare a erorilor** și procesare a rezultatelor

### 📖 Utilizarea soluțiilor

1. **Navighează în folderul limbajului preferat**:

   ```bash
   cd solution/typescript/    # Pentru TypeScript
   cd solution/java/          # Pentru Java
   cd solution/python/        # Pentru Python
   cd solution/dotnet/        # Pentru .NET
   ```

2. **Urmează instrucțiunile din README din fiecare folder pentru**:
   - Instalarea dependențelor
   - Construirea proiectului
   - Rularea clientului

3. **Exemplu de output** pe care ar trebui să-l vezi:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Pentru documentație completă și instrucțiuni pas cu pas, vezi: **[📖 Documentația soluției](./solution/README.md)**

## 🎯 Exemple complete

Am furnizat implementări complete și funcționale ale clientului pentru toate limbajele de programare acoperite în acest tutorial. Aceste exemple demonstrează funcționalitatea completă descrisă mai sus și pot fi folosite ca referințe sau puncte de plecare pentru propriile tale proiecte.

### Exemple complete disponibile

| Limbaj | Fișier | Descriere |
|--------|--------|-----------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Client Java complet folosind transport SSE cu tratare completă a erorilor |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Client C# complet folosind transport stdio cu pornire automată a serverului |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Client TypeScript complet cu suport complet pentru protocolul MCP |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Client Python complet folosind pattern-uri async/await |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Client Rust complet folosind Tokio pentru operațiuni asincrone |

Fiecare exemplu complet include:
- ✅ **Stabilirea conexiunii** și gestionarea erorilor  
- ✅ **Descoperirea serverului** (unelte, resurse, prompturi acolo unde este cazul)  
- ✅ **Operații calculator** (adunare, scădere, înmulțire, împărțire, ajutor)  
- ✅ **Procesarea rezultatelor** și afișare formatată  
- ✅ **Gestionare cuprinzătoare a erorilor**  
- ✅ **Cod curat, documentat** cu comentarii pas cu pas  

### Începeți cu exemple complete

1. **Alegeți limbajul preferat** din tabelul de mai sus  
2. **Consultați fișierul complet de exemplu** pentru a înțelege implementarea completă  
3. **Rulați exemplul** urmând instrucțiunile din [`complete_examples.md`](./complete_examples.md)  
4. **Modificați și extindeți** exemplul pentru cazul dumneavoastră specific  

Pentru documentație detaliată despre rularea și personalizarea acestor exemple, vezi: **[📖 Documentația Exemples Complete](./complete_examples.md)**  

### 💡 Soluție vs. Exemple Complete

| **Folderul Soluție**     | **Exemple Complete**    |
|------------------------|------------------------|
| Structura completă a proiectului cu fișiere de build | Implementări într-un singur fișier  |
| Pregătit de rulat cu dependențe  | Exemple de cod concentrate |
| Configurare asemănătoare mediului de producție | Referință educațională     |
| Unelte specifice limbajului      | Comparatie între limbaje  |

Ambele abordări sunt valoroase – folosiți **folderul soluție** pentru proiecte complete și **exemplele complete** pentru învățare și referință.

## Concluzii cheie

Concluziile cheie pentru acest capitol despre clienți sunt următoarele:

- Pot fi folosiți atât pentru descoperirea, cât și pentru invocarea funcționalităților serverului.  
- Pot porni un server în timp ce și ei înșiși pornesc (așa cum se arată în acest capitol), dar clienții pot să se conecteze și la servere deja în funcțiune.  
- Sunt o metodă excelentă pentru a testa capabilitățile serverului pe lângă alternative precum Inspector-ul descris în capitolul anterior.  

## Resurse suplimentare

- [Crearea de clienți în MCP](https://modelcontextprotocol.io/quickstart/client)  

## Mostre

- [Calculator Java](../samples/java/calculator/README.md)  
- [Calculator .Net](../../../../03-GettingStarted/samples/csharp)  
- [Calculator JavaScript](../samples/javascript/README.md)  
- [Calculator TypeScript](../samples/typescript/README.md)  
- [Calculator Python](../../../../03-GettingStarted/samples/python)  
- [Calculator Rust](../../../../03-GettingStarted/samples/rust)  

## Ce urmează

- Următorul: [Crearea unui client cu un LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să țineți cont că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm responsabilitatea pentru eventuale neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->