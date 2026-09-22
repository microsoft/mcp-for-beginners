# Einen Client erstellen

Clients sind benutzerdefinierte Anwendungen oder Skripte, die direkt mit einem MCP-Server kommunizieren, um Ressourcen, Tools und Prompts anzufordern. Im Gegensatz zum Verwendung des Inspektor-Tools, das eine grafische Benutzeroberfläche für die Interaktion mit dem Server bietet, ermöglicht das Schreiben Ihres eigenen Clients programmatische und automatisierte Interaktionen. Dies ermöglicht Entwicklern, MCP-Funktionen in ihre eigenen Arbeitsabläufe zu integrieren, Aufgaben zu automatisieren und maßgeschneiderte Lösungen für spezifische Bedürfnisse zu erstellen.

## Überblick

Diese Lektion führt in das Konzept von Clients im Model Context Protocol (MCP)-Ökosystem ein. Sie lernen, wie Sie Ihren eigenen Client schreiben und ihn mit einem MCP-Server verbinden.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Zu verstehen, was ein Client tun kann.
- Ihren eigenen Client zu schreiben.
- Den Client mit einem MCP-Server zu verbinden und zu testen, um sicherzustellen, dass dieser wie erwartet funktioniert.

## Was gehört zum Schreiben eines Clients?

Um einen Client zu schreiben, müssen Sie Folgendes tun:

- **Importieren Sie die richtigen Bibliotheken**. Sie verwenden dieselbe Bibliothek wie zuvor, nur andere Konstrukte.
- **Instanziieren Sie einen Client**. Dies beinhaltet das Erstellen einer Client-Instanz und deren Verknüpfung mit der gewählten Transportschicht.
- **Entscheiden Sie, welche Ressourcen aufgelistet werden sollen**. Ihr MCP-Server bietet Ressourcen, Tools und Prompts; Sie müssen entscheiden, welche davon Sie auflisten möchten.
- **Integrieren Sie den Client in eine Host-Anwendung**. Sobald Sie die Fähigkeiten des Servers kennen, müssen Sie diese in Ihre Host-Anwendung integrieren, so dass bei Eingabe eines Prompts oder Befehls die entsprechende Serverfunktion aufgerufen wird.

Jetzt, da wir auf hoher Ebene verstanden haben, was wir tun werden, schauen wir uns als Nächstes ein Beispiel an.

### Ein Beispiel-Client

Schauen wir uns diesen Beispiel-Client an:

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

// Prompts auflisten
const prompts = await client.listPrompts();

// Einen Prompt abrufen
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Ressourcen auflisten
const resources = await client.listResources();

// Eine Ressource lesen
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Ein Werkzeug aufrufen
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Im obigen Code haben wir:

- Die Bibliotheken importiert
- Eine Client-Instanz erstellt und mit stdio als Transport verbunden.
- Prompts, Ressourcen und Tools aufgelistet und alle aufgerufen.

Da haben Sie es, einen Client, der mit einem MCP-Server kommunizieren kann.

Nehmen wir uns im nächsten Übungsteil Zeit, jeden Codeabschnitt zu analysieren und zu erklären, was genau passiert.

## Übung: Einen Client schreiben

Wie oben erwähnt, nehmen wir uns Zeit, den Code zu erklären, und programmieren Sie gern mit, wenn Sie möchten.

### -1- Bibliotheken importieren

Importieren wir die benötigten Bibliotheken; wir brauchen Verweise auf einen Client und das ausgewählte Transportprotokoll stdio. stdio ist ein Protokoll für Dinge, die auf Ihrem lokalen Rechner laufen sollen. SSE ist ein weiteres Transportprotokoll, das wir in zukünftigen Kapiteln zeigen werden, aber das ist Ihre zweite Option. Für den Moment machen wir weiter mit stdio.

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

Für Java erstellen Sie einen Client, der eine Verbindung zum MCP-Server aus der vorigen Übung herstellt. Verwenden Sie die gleiche Java Spring Boot-Projektstruktur aus [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), erstellen Sie eine neue Java-Klasse namens `SDKClient` im Ordner `src/main/java/com/microsoft/mcp/sample/client/` und fügen Sie folgende Importe hinzu:

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

Danach können Sie in Ihrem Client-Code die notwendigen Bibliotheken importieren.

```rust
use rmcp::{
    RmcpError,
    model::CallToolRequestParam,
    service::ServiceExt,
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use tokio::process::Command;
```

Kommen wir zur Instanziierung.

### -2- Client und Transport instanziieren

Wir müssen eine Instanz des Transports und eine unseres Clients erstellen:

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

- Eine stdio-Transportinstanz erstellt. Beachten Sie, wie Kommandos und Argumente definiert werden, um den Server zu finden und zu starten, da dies notwendig ist, wenn wir den Client erstellen.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Eine Client-Instanz erzeugt, der ein Name und eine Version gegeben wurde.

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

# Serverparameter für stdio-Verbindung erstellen
server_params = StdioServerParameters(
    command="mcp",  # Ausführbare Datei
    args=["run", "server.py"],  # Optionale Befehlszeilenargumente
    env=None,  # Optionale Umgebungsvariablen
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Verbindung initialisieren
            await session.initialize()

          

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
```

Im obigen Code haben wir:

- Die benötigten Bibliotheken importiert
- Eine Objektinstanz für Serverparameter erzeugt, da wir den Server ausführen müssen, um uns mit unserem Client zu verbinden.
- Eine Methode `run` definiert, die wiederum `stdio_client` aufruft, um eine Clientsitzung zu starten.
- Einen Einstiegspunkt erstellt, wo wir die `run`-Methode an `asyncio.run` übergeben.

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

Im obigen Code haben wir:

- Die notwendigen Bibliotheken importiert.
- Einen stdio-Transport erstellt und einen Client `mcpClient` erstellt. Letzterer wird verwendet, um Funktionen auf dem MCP-Server aufzulisten und aufzurufen.

Hinweis: Bei "Arguments" können Sie entweder auf die *.csproj* oder auf die ausführbare Datei verweisen.

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
        
        // Ihre Client-Logik geht hier hin
    }
}
```

Im obigen Code haben wir:

- Eine main-Methode erstellt, die einen SSE-Transport konfiguriert, der auf `http://localhost:8080` zeigt, wo unser MCP-Server läuft.
- Eine Clientklasse erstellt, die den Transport im Konstruktor erhält.
- In der `run`-Methode einen synchronen MCP-Client mit dem Transport erstellt und die Verbindung initialisiert.
- Den SSE (Server-Sent Events) Transport verwendet, der für HTTP-basierte Kommunikation mit Java Spring Boot MCP-Servern geeignet ist.

#### Rust

Beachten Sie, dass dieser Rust-Client annimmt, dass der Server ein Schwesterprojekt namens "calculator-server" im gleichen Verzeichnis ist. Der unten stehende Code startet den Server und verbindet sich mit ihm.

```rust
async fn main() -> Result<(), RmcpError> {
    // Gehen Sie davon aus, dass der Server ein Schwesterprojekt mit dem Namen "calculator-server" im gleichen Verzeichnis ist
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

    // TODO: Initialisieren

    // TODO: Werkzeuge auflisten

    // TODO: Rufen Sie das Werkzeug "add" mit den Argumenten = {"a": 3, "b": 2} auf

    client.cancel().await?;
    Ok(())
}
```

### -3- Serverfeatures auflisten

Nun haben wir einen Client, der sich verbinden kann, wenn das Programm ausgeführt wird. Allerdings listet er seine Features nicht auf, also machen wir das jetzt:

#### TypeScript

```typescript
// Eingabeaufforderungen auflisten
const prompts = await client.listPrompts();

// Ressourcen auflisten
const resources = await client.listResources();

// Werkzeuge auflisten
const tools = await client.listTools();
```

#### Python

```python
# Verfügbare Ressourcen auflisten
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Verfügbare Werkzeuge auflisten
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
```

Hier listen wir die verfügbaren Ressourcen `list_resources()` und Tools `list_tools` auf und drucken diese aus.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Oben ein Beispiel, wie man die Tools auf dem Server auflisten kann. Für jedes Tool drucken wir den Namen aus.

#### Java

```java
// Werkzeuge auflisten und demonstrieren
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Sie können den Server auch anpingen, um die Verbindung zu überprüfen
client.ping();
```

Im obigen Code haben wir:

- `listTools()` aufgerufen, um alle verfügbaren Tools vom MCP-Server zu erhalten.
- `ping()` verwendet, um zu prüfen, ob die Verbindung zum Server funktioniert.
- Das Objekt `ListToolsResult` enthält Informationen über alle Tools, inklusive Name, Beschreibung und Eingabeschemata.

Großartig, jetzt haben wir alle Features erfasst. Die Frage ist, wann verwenden wir sie? Dieser Client ist ziemlich einfach, im Sinne davon, dass wir die Features explizit aufrufen müssen, wenn wir sie wollen. Im nächsten Kapitel erstellen wir einen fortgeschritteneren Client, der Zugang zu seinem eigenen großen Sprachmodell (LLM) hat. Für jetzt sehen wir, wie man die Serverfeatures aufruft:

#### Rust

In der main-Funktion können wir nach der Initialisierung des Clients den Server starten und einige Features auflisten.

```rust
// Initialisieren
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Werkzeuge auflisten
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Features aufrufen

Um Features aufzurufen, müssen wir sicherstellen, dass wir die richtigen Argumente angeben und in manchen Fällen auch den Namen dessen, was wir aufrufen möchten.

#### TypeScript

```typescript

// Eine Ressource lesen
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Ein Werkzeug aufrufen
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});

// Eingabeaufforderung aufrufen
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Im obigen Code haben wir:

- Eine Ressource gelesen, wir rufen die Ressource durch `readResource()` mit Angabe von `uri` auf. So sieht das wahrscheinlich auf der Serverseite aus:

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

    Unser `uri` Wert `file://example.txt` entspricht `file://{name}` auf dem Server. `example.txt` wird auf `name` gemappt.

- Ein Tool aufgerufen, wir rufen es durch Angabe von `name` und `arguments` wie folgt auf:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Einen Prompt erhalten, um einen Prompt zu bekommen, rufen Sie `getPrompt()` mit `name` und `arguments` auf. Der Servercode sieht so aus:

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

    Und Ihr resultierender Client-Code sieht also so aus, um dem auf dem Server Deklarierten zu entsprechen:

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
# Eine Ressource lesen
print("READING RESOURCE")
content, mime_type = await session.read_resource("greeting://hello")

# Ein Werkzeug aufrufen
print("CALL TOOL")
result = await session.call_tool("add", arguments={"a": 1, "b": 7})
print(result.content)
```

Im obigen Code haben wir:

- Eine Ressource namens `greeting` mit `read_resource` aufgerufen.
- Ein Tool namens `add` mit `call_tool` aufgerufen.

#### .NET

1. Fügen wir Code hinzu, um ein Tool aufzurufen:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Um das Ergebnis auszudrucken, hier etwas Code zur Handhabung:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Rufen Sie verschiedene Taschenrechner-Tools auf
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

- Mehrere Rechner-Tools mit der Methode `callTool()` und `CallToolRequest` Objekten aufgerufen.
- Jeder Toolaufruf spezifiziert den Toolnamen und eine `Map` von Argumenten, die das Tool benötigt.
- Die Server-Tools erwarten bestimmte Parameter-Namen (z.B. "a", "b" für mathematische Operationen).
- Ergebnisse werden als `CallToolResult` Objekte mit der Antwort vom Server zurückgegeben.

#### Rust

```rust
// Rufe das Addier-Werkzeug mit den Argumenten = {"a": 3, "b": 2} auf
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

### -5- Client ausführen

Um den Client auszuführen, geben Sie folgenden Befehl im Terminal ein:

#### TypeScript

Fügen Sie den folgenden Eintrag in den Bereich "scripts" in *package.json* ein:

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

Stellen Sie zunächst sicher, dass Ihr MCP-Server unter `http://localhost:8080` läuft. Dann starten Sie den Client:

```bash
# Baue dein Projekt
./mvnw clean compile

# Starte den Client
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativ können Sie das vollständige Clientprojekt im Lösungsordner `03-GettingStarted\02-client\solution\java` ausführen:

```bash
# Navigiere zum Lösungsverzeichnis
cd 03-GettingStarted/02-client/solution/java

# Baue und starte das JAR
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Aufgabe

In dieser Aufgabe verwenden Sie das Gelernte, um einen eigenen Client zu erstellen.

Hier ist ein Server, den Sie verwenden können, den Sie über Ihren Client aufrufen müssen. Versuchen Sie, dem Server weitere Funktionen hinzuzufügen, um ihn interessanter zu machen.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Erstellen Sie einen MCP-Server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Fügen Sie ein Additionswerkzeug hinzu
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Fügen Sie eine dynamische Begrüßungsressource hinzu
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

// Beginnen Sie mit dem Empfangen von Nachrichten auf stdin und dem Senden von Nachrichten auf stdout

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

# Einen MCP-Server erstellen
mcp = FastMCP("Demo")


# Ein Werkzeug zur Addition hinzufügen
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Eine dynamische Begrüßungsressource hinzufügen
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

Sehen Sie sich dieses Projekt an, um zu sehen, wie Sie [Prompts und Ressourcen hinzufügen](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Prüfen Sie auch diesen Link, wie Sie [Prompts und Ressourcen aufrufen](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Im [vorherigen Abschnitt](../../../../03-GettingStarted/01-first-server) haben Sie gelernt, wie man einen einfachen MCP-Server mit Rust erstellt. Sie können darauf aufbauen oder diesen Link für weitere Rust-basierte MCP-Server-Beispiele ansehen: [MCP Server Examples](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Lösung

Der **Lösungsordner** enthält vollständige, ausführbare Client-Implementierungen, die alle in diesem Tutorial behandelten Konzepte demonstrieren. Jede Lösung beinhaltet sowohl Client- als auch Servercode, organisiert in separaten, eigenständigen Projekten.

### 📁 Lösungstruktur

Das Lösungverzeichnis ist nach Programmiersprachen gegliedert:

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

### 🚀 Was jede Lösung beinhaltet

Jede sprachspezifische Lösung bietet:

- **Vollständige Client-Implementierung** mit allen Features aus dem Tutorial
- **Funktionierende Projektstruktur** mit korrekten Abhängigkeiten und Konfiguration
- **Build- und Ausführungsskripte** für einfache Einrichtung und Ausführung
- **Detaillierte README** mit sprachspezifischen Anweisungen
- **Fehlerbehandlung** und Beispiel für Ergebnisverarbeitung

### 📖 Benutzung der Lösungen

1. **Navigieren Sie zu Ihrem bevorzugten Sprachordner**:

   ```bash
   cd solution/typescript/    # Für TypeScript
   cd solution/java/          # Für Java
   cd solution/python/        # Für Python
   cd solution/dotnet/        # Für .NET
   ```

2. **Folgen Sie den README-Anweisungen** in jedem Ordner für:
   - Installation der Abhängigkeiten
   - Projektaufbau
   - Ausführen des Clients

3. **Beispielausgabe**, die Sie sehen sollten:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Für vollständige Dokumentation und Schritt-für-Schritt-Anweisungen siehe: **[📖 Lösungsdokumentation](./solution/README.md)**

## 🎯 Komplette Beispiele

Wir haben vollständige, funktionierende Client-Implementierungen für alle im Tutorial behandelten Programmiersprachen bereitgestellt. Diese Beispiele demonstrieren die volle Funktionalität wie oben beschrieben und können als Referenzimplementierungen oder Ausgangspunkte für eigene Projekte verwendet werden.

### Verfügbare komplette Beispiele

| Sprache | Datei | Beschreibung |
|----------|------|-------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Vollständiger Java-Client mit SSE-Transport und umfassender Fehlerbehandlung |
| **C#** | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Vollständiger C#-Client mit stdio-Transport und automatischem Serverstart |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Vollständiger TypeScript-Client mit vollständiger MCP-Protokollunterstützung |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Vollständiger Python-Client unter Verwendung von async/await-Mustern |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Vollständiger Rust-Client mit Tokio für asynchrone Operationen |

Jedes vollständige Beispiel enthält:

- ✅ **Verbindungsaufbau** und Fehlerbehandlung
- ✅ **Servererkennung** (Tools, Ressourcen, Prompts, falls zutreffend)
- ✅ **Rechenoperationen** (addieren, subtrahieren, multiplizieren, dividieren, Hilfe)
- ✅ **Ergebnisverarbeitung** und formatierte Ausgabe
- ✅ **Umfassende Fehlerbehandlung**

- ✅ **Sauberer, dokumentierter Code** mit Schritt-für-Schritt-Kommentaren

### Einstieg mit vollständigen Beispielen

1. **Wählen Sie Ihre bevorzugte Sprache** aus der obigen Tabelle
2. **Überprüfen Sie die vollständige Beispieldatei**, um die gesamte Implementierung zu verstehen
3. **Führen Sie das Beispiel aus** gemäß den Anweisungen in [`complete_examples.md`](./complete_examples.md)
4. **Passen Sie das Beispiel an und erweitern Sie es** für Ihren spezifischen Anwendungsfall

Für detaillierte Dokumentation zum Ausführen und Anpassen dieser Beispiele siehe: **[📖 Dokumentation der vollständigen Beispiele](./complete_examples.md)**

### 💡 Lösung vs. vollständige Beispiele

| **Lösungsordner** | **Vollständige Beispiele** |
|--------------------|--------------------- |
| Komplettprojektstruktur mit Build-Dateien | Ein-Datei-Implementierungen |
| Direkt lauffähig mit Abhängigkeiten | Fokus auf Codebeispiele |
| Produktionsähnliche Umgebung | Pädagogische Referenz |
| Sprachspezifische Werkzeuge | Sprachübergreifender Vergleich |

Beide Ansätze sind wertvoll – verwenden Sie den **Lösungsordner** für komplette Projekte und die **vollständigen Beispiele** zum Lernen und als Referenz.

## Wichtige Erkenntnisse

Die wichtigsten Erkenntnisse dieses Kapitels zum Thema Clients sind:

- Können verwendet werden, um Funktionen auf dem Server zu entdecken und aufzurufen.
- Können einen Server starten, während sie selbst starten (wie in diesem Kapitel), aber Clients können sich auch mit laufenden Servern verbinden.
- Sind ein hervorragendes Mittel, um Serverfunktionen neben Alternativen wie dem Inspector zu testen, wie im vorherigen Kapitel beschrieben.

## Zusätzliche Ressourcen

- [Clients in MCP erstellen](https://modelcontextprotocol.io/quickstart/client)

## Beispielprojekte

- [Java Rechner](../samples/java/calculator/README.md)
- [.NET Rechner](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Rechner](../samples/javascript/README.md)
- [TypeScript Rechner](../samples/typescript/README.md)
- [Python Rechner](../../../../03-GettingStarted/samples/python)
- [Rust Rechner](../../../../03-GettingStarted/samples/rust)

## Was kommt als Nächstes

- Nächstes: [Erstellen eines Clients mit einem LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->