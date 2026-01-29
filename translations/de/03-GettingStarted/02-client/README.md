# Erstellen eines Clients

Clients sind benutzerdefinierte Anwendungen oder Skripte, die direkt mit einem MCP-Server kommunizieren, um Ressourcen, Tools und Eingabeaufforderungen anzufordern. Im Gegensatz zur Verwendung des Inspektor-Tools, das eine grafische Benutzeroberfläche für die Interaktion mit dem Server bietet, ermöglicht das Schreiben eines eigenen Clients programmatische und automatisierte Interaktionen. Dies erlaubt es Entwicklern, MCP-Funktionen in ihre eigenen Workflows zu integrieren, Aufgaben zu automatisieren und maßgeschneiderte Lösungen für spezifische Anforderungen zu erstellen.

## Überblick

Diese Lektion führt in das Konzept von Clients innerhalb des Model Context Protocol (MCP)-Ökosystems ein. Sie lernen, wie Sie Ihren eigenen Client schreiben und diesen mit einem MCP-Server verbinden.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Zu verstehen, was ein Client leisten kann.
- Ihren eigenen Client zu schreiben.
- Den Client mit einem MCP-Server zu verbinden und zu testen, um sicherzustellen, dass dieser wie erwartet funktioniert.

## Was gehört zum Schreiben eines Clients?

Um einen Client zu schreiben, müssen Sie Folgendes tun:

- **Die richtigen Bibliotheken importieren**. Sie verwenden dieselbe Bibliothek wie zuvor, jedoch mit anderen Konstrukten.
- **Einen Client instanziieren**. Dies beinhaltet das Erstellen einer Client-Instanz und das Verbinden mit der gewählten Transportmethode.
- **Entscheiden, welche Ressourcen aufgelistet werden sollen**. Ihr MCP-Server bietet Ressourcen, Tools und Eingabeaufforderungen. Sie müssen entscheiden, welche davon aufgelistet werden sollen.
- **Den Client in eine Hostanwendung integrieren**. Sobald Sie die Fähigkeiten des Servers kennen, müssen Sie diesen in Ihre Hostanwendung integrieren, sodass bei Eingabe einer Eingabeaufforderung oder eines Befehls durch den Benutzer die entsprechende Serverfunktion aufgerufen wird.

Nachdem wir nun auf hoher Ebene verstanden haben, was wir tun werden, schauen wir uns als Nächstes ein Beispiel an.

### Ein Beispiel-Client

Werfen wir einen Blick auf diesen Beispiel-Client:

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

Im obigen Code haben wir:

- Die Bibliotheken importiert.
- Eine Instanz eines Clients erstellt und diese mithilfe von stdio für den Transport verbunden.
- Eingabeaufforderungen, Ressourcen und Tools aufgelistet und alle aufgerufen.

Da haben Sie es, ein Client, der mit einem MCP-Server kommunizieren kann.

Nehmen wir uns Zeit im nächsten Übungsabschnitt, um jeden Codeausschnitt aufzuschlüsseln und zu erklären, was vor sich geht.

## Übung: Schreiben eines Clients

Wie oben erwähnt, nehmen wir uns Zeit, um den Code zu erklären, und Sie können gerne parallel dazu programmieren.

### -1- Die Bibliotheken importieren

Importieren wir die benötigten Bibliotheken. Wir benötigen Referenzen zu einem Client und zu unserem gewählten Transportprotokoll, stdio. stdio ist ein Protokoll für Dinge, die auf Ihrem lokalen Rechner ausgeführt werden sollen. SSE ist ein weiteres Transportprotokoll, das wir in zukünftigen Kapiteln zeigen werden, aber das ist Ihre andere Option. Für den Moment machen wir jedoch mit stdio weiter.

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

Für Java erstellen Sie einen Client, der sich mit dem MCP-Server aus der vorherigen Übung verbindet. Verwenden Sie die gleiche Java Spring Boot-Projektstruktur aus [Erste Schritte mit MCP-Server](../../../../03-GettingStarted/01-first-server/solution/java), erstellen Sie eine neue Java-Klasse namens `SDKClient` im Ordner `src/main/java/com/microsoft/mcp/sample/client/` und fügen Sie die folgenden Importe hinzu:

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

Sie müssen die folgenden Abhängigkeiten zu Ihrer `Cargo.toml`-Datei hinzufügen.

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

Von dort aus können Sie die notwendigen Bibliotheken in Ihrem Client-Code importieren.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Fahren wir mit der Instanziierung fort.

### -2- Client und Transport instanziieren

Wir müssen eine Instanz des Transports und eine des Clients erstellen:

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

Im obigen Code haben wir:

- Eine stdio-Transportinstanz erstellt. Beachten Sie, wie sie Befehl und Argumente angibt, um den Server zu finden und zu starten, da wir dies tun müssen, wenn wir den Client erstellen.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Einen Client instanziiert, indem wir ihm einen Namen und eine Version geben.

    ```typescript
    const client = new Client(
    {
        name: "example-client",
        version: "1.0.0"
    });
    ```

- Den Client mit dem gewählten Transport verbunden.

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

Im obigen Code haben wir:

- Die benötigten Bibliotheken importiert.
- Ein Server-Parameterobjekt instanziiert, da wir diesen verwenden werden, um den Server zu starten, damit wir uns mit unserem Client verbinden können.
- Eine Methode `run` definiert, die wiederum `stdio_client` aufruft, um eine Client-Sitzung zu starten.
- Einen Einstiegspunkt erstellt, an dem wir die `run`-Methode an `asyncio.run` übergeben.

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

Im obigen Code haben wir:

- Die benötigten Bibliotheken importiert.
- Einen stdio-Transport erstellt und einen Client `mcpClient` erstellt. Letzterer wird verwendet, um Funktionen auf dem MCP-Server aufzulisten und aufzurufen.

Beachten Sie, dass Sie in "Arguments" entweder auf die *.csproj*-Datei oder auf die ausführbare Datei verweisen können.

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

Im obigen Code haben wir:

- Eine Hauptmethode erstellt, die einen SSE-Transport einrichtet, der auf `http://localhost:8080` verweist, wo unser MCP-Server ausgeführt wird.
- Eine Client-Klasse erstellt, die den Transport als Konstruktorparameter übernimmt.
- In der Methode `run` einen synchronen MCP-Client mithilfe des Transports erstellt und die Verbindung initialisiert.
- SSE (Server-Sent Events)-Transport verwendet, der für HTTP-basierte Kommunikation mit Java Spring Boot MCP-Servern geeignet ist.

#### Rust

Dieser Rust-Client geht davon aus, dass der Server ein Schwesterprojekt namens "calculator-server" im selben Verzeichnis ist. Der folgende Code startet den Server und verbindet sich mit ihm.

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

### -3- Serverfunktionen auflisten

Nun haben wir einen Client, der sich verbinden kann, wenn das Programm ausgeführt wird. Allerdings listet er noch keine Funktionen auf, also machen wir das als Nächstes:

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

Hier listen wir die verfügbaren Ressourcen mit `list_resources()` und Tools mit `list_tools` auf und geben sie aus.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Oben sehen Sie ein Beispiel, wie wir die Tools auf dem Server auflisten können. Für jedes Tool geben wir dann seinen Namen aus.

#### Java

```java
// List and demonstrate tools
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// You can also ping the server to verify connection
client.ping();
```

Im obigen Code haben wir:

- `listTools()` aufgerufen, um alle verfügbaren Tools vom MCP-Server abzurufen.
- `ping()` verwendet, um zu überprüfen, ob die Verbindung zum Server funktioniert.
- `ListToolsResult` enthält Informationen über alle Tools, einschließlich ihrer Namen, Beschreibungen und Eingabeschemata.

Super, jetzt haben wir alle Funktionen erfasst. Nun stellt sich die Frage, wann wir sie verwenden. Dieser Client ist ziemlich einfach, in dem Sinne, dass wir die Funktionen explizit aufrufen müssen, wenn wir sie benötigen. Im nächsten Kapitel erstellen wir einen fortschrittlicheren Client, der Zugriff auf sein eigenes großes Sprachmodell (LLM) hat. Für den Moment sehen wir uns jedoch an, wie wir die Funktionen auf dem Server aufrufen können:

#### Rust

Im Hauptprogramm, nach der Initialisierung des Clients, können wir den Server initialisieren und einige seiner Funktionen auflisten.

```rust
// Initialize
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// List tools
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funktionen aufrufen

Um die Funktionen aufzurufen, müssen wir sicherstellen, dass wir die richtigen Argumente und in einigen Fällen den Namen dessen, was wir aufrufen möchten, angeben.

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

Im obigen Code haben wir:

- Eine Ressource gelesen, indem wir `readResource()` mit `uri` aufgerufen haben. So sieht das wahrscheinlich auf der Serverseite aus:

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

    Unser `uri`-Wert `file://example.txt` entspricht `file://{name}` auf dem Server. `example.txt` wird auf `name` abgebildet.

- Ein Tool aufgerufen, indem wir seinen `name` und seine `arguments` wie folgt angegeben haben:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Eine Eingabeaufforderung abgerufen, indem wir `getPrompt()` mit `name` und `arguments` aufgerufen haben. Der Servercode sieht so aus:

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

    Und Ihr resultierender Clientcode sieht daher so aus, um das zu entsprechen, was auf dem Server deklariert ist:

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

Im obigen Code haben wir:

- Eine Ressource namens `greeting` mit `read_resource` aufgerufen.
- Ein Tool namens `add` mit `call_tool` aufgerufen.

#### .NET

1. Fügen wir etwas Code hinzu, um ein Tool aufzurufen:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Um das Ergebnis auszugeben, hier ein Code, um dies zu handhaben:

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

Im obigen Code haben wir:

- Mehrere Rechner-Tools mit der Methode `callTool()` und `CallToolRequest`-Objekten aufgerufen.
- Jeder Tool-Aufruf gibt den Toolnamen und eine `Map` der für dieses Tool erforderlichen Argumente an.
- Die Server-Tools erwarten spezifische Parameternamen (wie "a", "b" für mathematische Operationen).
- Ergebnisse werden als `CallToolResult`-Objekte zurückgegeben, die die Antwort des Servers enthalten.

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

### -5- Den Client ausführen

Um den Client auszuführen, geben Sie den folgenden Befehl im Terminal ein:

#### TypeScript

Fügen Sie den folgenden Eintrag in den Abschnitt "scripts" in *package.json* hinzu:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Rufen Sie den Client mit folgendem Befehl auf:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Stellen Sie zunächst sicher, dass Ihr MCP-Server unter `http://localhost:8080` läuft. Führen Sie dann den Client aus:

```bash
# Build you project
./mvnw clean compile

# Run the client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativ können Sie das vollständige Clientprojekt im Lösungsordner `03-GettingStarted\02-client\solution\java` ausführen:

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

## Aufgabe

In dieser Aufgabe verwenden Sie das, was Sie über das Erstellen eines Clients gelernt haben, um einen eigenen Client zu erstellen.

Hier ist ein Server, den Sie verwenden können und den Sie über Ihren Client-Code aufrufen müssen. Versuchen Sie, dem Server weitere Funktionen hinzuzufügen, um ihn interessanter zu machen.

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

Sehen Sie sich dieses Projekt an, um zu erfahren, wie Sie [Eingabeaufforderungen und Ressourcen hinzufügen](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Sehen Sie sich auch diesen Link an, um zu erfahren, wie Sie [Eingabeaufforderungen und Ressourcen aufrufen](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Im [vorherigen Abschnitt](../../../../03-GettingStarted/01-first-server) haben Sie gelernt, wie Sie einen einfachen MCP-Server mit Rust erstellen. Sie können darauf aufbauen oder diesen Link für weitere MCP-Server-Beispiele in Rust überprüfen: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Lösung

Der **Lösungsordner** enthält vollständige, ausführbare Client-Implementierungen, die alle in diesem Tutorial behandelten Konzepte demonstrieren. Jede Lösung enthält sowohl Client- als auch Servercode, organisiert in separaten, eigenständigen Projekten.

### 📁 Lösungsstruktur

Das Lösungsverzeichnis ist nach Programmiersprache organisiert:

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

### 🚀 Was jede Lösung enthält

Jede sprachspezifische Lösung bietet:

- **Vollständige Client-Implementierung** mit allen Funktionen aus dem Tutorial.
- **Funktionierende Projektstruktur** mit den richtigen Abhängigkeiten und Konfigurationen.
- **Build- und Ausführungsskripte** für einfache Einrichtung und Ausführung.
- **Detaillierte README** mit sprachspezifischen Anweisungen.
- **Beispiele für Fehlerbehandlung** und Ergebnisverarbeitung.

### 📖 Verwendung der Lösungen

1. **Navigieren Sie zu Ihrem bevorzugten Sprachordner**:

   ```bash
   cd solution/typescript/    # For TypeScript
   cd solution/java/          # For Java
   cd solution/python/        # For Python
   cd solution/dotnet/        # For .NET
   ```

2. **Befolgen Sie die README-Anweisungen** in jedem Ordner für:
   - Installation der Abhängigkeiten.
   - Erstellen des Projekts.
   - Ausführen des Clients.

3. **Beispielausgabe**, die Sie sehen sollten:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Für vollständige Dokumentation und Schritt-für-Schritt-Anweisungen siehe: **[📖 Lösungsdokumentation](./solution/README.md)**

## 🎯 Vollständige Beispiele

Wir haben vollständige, funktionierende Client-Implementierungen für alle in diesem Tutorial behandelten Programmiersprachen bereitgestellt. Diese Beispiele demonstrieren die vollständige Funktionalität, die oben beschrieben wurde, und können als Referenzimplementierungen oder Ausgangspunkte für Ihre eigenen Projekte verwendet werden.

### Verfügbare vollständige Beispiele

| Sprache   | Datei                              | Beschreibung                                                                 |
|-----------|------------------------------------|-----------------------------------------------------------------------------|
| **Java**  | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Vollständiger Java-Client mit SSE-Transport und umfassender Fehlerbehandlung |
| **C#**    | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Vollständiger C#-Client mit stdio-Transport und automatischem Serverstart    |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Vollständiger TypeScript-Client mit vollständiger MCP-Protokollunterstützung |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Vollständiger Python-Client mit async/await-Mustern                          |
| **Rust**  | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs)     | Vollständiger Rust-Client mit Tokio für asynchrone Operationen               |
Jedes vollständige Beispiel umfasst:

- ✅ **Verbindungsaufbau** und Fehlerbehandlung  
- ✅ **Server-Erkennung** (Tools, Ressourcen, Eingabeaufforderungen, wo zutreffend)  
- ✅ **Rechneroperationen** (addieren, subtrahieren, multiplizieren, dividieren, Hilfe)  
- ✅ **Ergebnisverarbeitung** und formatierte Ausgabe  
- ✅ **Umfassende Fehlerbehandlung**  
- ✅ **Sauberer, dokumentierter Code** mit Schritt-für-Schritt-Kommentaren  

### Einstieg mit vollständigen Beispielen

1. **Wählen Sie Ihre bevorzugte Sprache** aus der obigen Tabelle  
2. **Überprüfen Sie die vollständige Beispieldatei**, um die gesamte Implementierung zu verstehen  
3. **Führen Sie das Beispiel aus**, indem Sie den Anweisungen in [`complete_examples.md`](./complete_examples.md) folgen  
4. **Passen Sie das Beispiel an** und erweitern Sie es für Ihren spezifischen Anwendungsfall  

Für detaillierte Dokumentation zum Ausführen und Anpassen dieser Beispiele, siehe: **[📖 Dokumentation zu vollständigen Beispielen](./complete_examples.md)**  

### 💡 Lösung vs. vollständige Beispiele

| **Lösungsordner** | **Vollständige Beispiele** |  
|--------------------|--------------------- |  
| Vollständige Projektstruktur mit Build-Dateien | Implementierungen in einer einzigen Datei |  
| Bereit zur Ausführung mit Abhängigkeiten | Fokus auf Code-Beispiele |  
| Produktionsähnliches Setup | Pädagogische Referenz |  
| Sprachspezifische Tools | Sprachübergreifender Vergleich |  

Beide Ansätze sind wertvoll - verwenden Sie den **Lösungsordner** für vollständige Projekte und die **vollständigen Beispiele** für Lernen und Referenz.  

## Wichtige Erkenntnisse  

Die wichtigsten Erkenntnisse für dieses Kapitel über Clients sind:  

- Können sowohl zur Erkennung als auch zur Nutzung von Funktionen auf dem Server verwendet werden.  
- Können einen Server starten, während sie selbst starten (wie in diesem Kapitel), aber Clients können auch mit laufenden Servern verbunden werden.  
- Sind eine großartige Möglichkeit, Serverfähigkeiten zu testen, neben Alternativen wie dem Inspector, wie im vorherigen Kapitel beschrieben.  

## Zusätzliche Ressourcen  

- [Clients in MCP erstellen](https://modelcontextprotocol.io/quickstart/client)  

## Beispiele  

- [Java-Rechner](../samples/java/calculator/README.md)  
- [.Net-Rechner](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript-Rechner](../samples/javascript/README.md)  
- [TypeScript-Rechner](../samples/typescript/README.md)  
- [Python-Rechner](../../../../03-GettingStarted/samples/python)  
- [Rust-Rechner](../../../../03-GettingStarted/samples/rust)  

## Was kommt als Nächstes  

- Weiter: [Einen Client mit einem LLM erstellen](../03-llm-client/README.md)  

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.