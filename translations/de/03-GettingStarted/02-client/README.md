# Einen Client erstellen

Clients sind benutzerdefinierte Anwendungen oder Skripte, die direkt mit einem MCP-Server kommunizieren, um Ressourcen, Tools und Eingabeaufforderungen anzufordern. Im Gegensatz zur Verwendung des Inspektor-Tools, das eine grafische Schnittstelle für die Interaktion mit dem Server bietet, ermöglicht das Schreiben eines eigenen Clients programmatische und automatisierte Interaktionen. Dadurch können Entwickler die MCP-Fähigkeiten in ihre eigenen Arbeitsabläufe integrieren, Aufgaben automatisieren und maßgeschneiderte Lösungen für spezifische Bedürfnisse erstellen.

## Übersicht

Diese Lektion führt in das Konzept von Clients im Model Context Protocol (MCP) Ökosystem ein. Du lernst, wie du deinen eigenen Client schreibst und ihn mit einem MCP-Server verbindest.

## Lernziele

Am Ende dieser Lektion wirst du in der Lage sein:

- Zu verstehen, was ein Client tun kann.
- Deinen eigenen Client zu schreiben.
- Den Client mit einem MCP-Server zu verbinden und zu testen, um sicherzustellen, dass dieser wie erwartet funktioniert.

## Was gehört zum Schreiben eines Clients?

Zum Schreiben eines Clients musst du Folgendes tun:

- **Die richtigen Bibliotheken importieren**. Du verwendest dieselbe Bibliothek wie zuvor, nur mit anderen Konstrukten.
- **Einen Client instanziieren**. Dabei erstellst du eine Client-Instanz und verbindest sie mit der gewählten Transportmethode.
- **Entscheiden, welche Ressourcen aufgelistet werden sollen**. Dein MCP-Server stellt Ressourcen, Tools und Eingabeaufforderungen bereit, du musst entscheiden, welche davon aufgelistet werden sollen.
- **Den Client in eine Host-Anwendung integrieren**. Sobald du die Fähigkeiten des Servers kennst, musst du den Client in deine Host-Anwendung integrieren, damit bei Eingabe einer Eingabeaufforderung oder eines anderen Befehls das entsprechende Server-Feature aufgerufen wird.

Nachdem wir nun auf hoher Ebene verstanden haben, was wir vorhaben, schauen wir uns als Nächstes ein Beispiel an.

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

// Listen Sie Aufforderungen auf
const prompts = await client.listPrompts();

// Holen Sie sich eine Aufforderung
const prompt = await client.getPrompt({
  name: "example-prompt",
  arguments: {
    arg1: "value"
  }
});

// Listen Sie Ressourcen auf
const resources = await client.listResources();

// Lesen Sie eine Ressource
const resource = await client.readResource({
  uri: "file:///example.txt"
});

// Rufen Sie ein Werkzeug auf
const result = await client.callTool({
  name: "example-tool",
  arguments: {
    arg1: "value"
  }
});
```

Im obigen Code haben wir:

- Die Bibliotheken importiert
- Eine Instanz eines Clients erstellt und diese mit stdio als Transport verbunden.
- Eingabeaufforderungen, Ressourcen und Tools aufgelistet und sie alle aufgerufen.

Da hast du es, ein Client, der mit einem MCP-Server kommunizieren kann.

Nimm dir in der nächsten Übungssektion Zeit, um jeden Codeausschnitt zu analysieren und zu erklären, was passiert.

## Übung: Einen Client schreiben

Wie oben gesagt, nehmen wir uns Zeit, um den Code zu erklären, und gerne kannst du auch mitprogrammieren.

### -1- Bibliotheken importieren

Importieren wir die benötigten Bibliotheken. Wir benötigen Verweise auf einen Client und unseren gewählten Transportprotokollstdio. stdio ist ein Protokoll für Dinge, die auf deinem lokalen Rechner laufen sollen. SSE ist ein weiteres Transportprotokoll, das wir in zukünftigen Kapiteln zeigen werden, aber das ist deine andere Option. Für den Moment machen wir mit stdio weiter.

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

Für Java erstellst du einen Client, der sich mit dem MCP-Server aus der vorherigen Übung verbindet. Verwende dieselbe Java Spring Boot Projektstruktur wie in [Getting Started with MCP Server](../../../../03-GettingStarted/01-first-server/solution/java), erstelle eine neue Java-Klasse namens `SDKClient` im Ordner `src/main/java/com/microsoft/mcp/sample/client/` und füge folgende Importe hinzu:

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

Du musst die folgenden Abhängigkeiten zu deiner `Cargo.toml` Datei hinzufügen.

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

Von dort aus kannst du die notwendigen Bibliotheken in deinem Client-Code importieren.

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

- Eine stdio-Transportinstanz erstellt. Beachte, wie hier Kommando und Argumente angegeben sind, um zu definieren, wie der Server gefunden und gestartet wird, da das etwas ist, das wir tun müssen, wenn wir den Client erstellen.

    ```typescript
    const transport = new StdioClientTransport({
        command: "node",
        args: ["server.js"]
    });
    ```

- Einen Client instanziiert, indem wir ihm einen Namen und eine Version gegeben haben.

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
- Ein Serverparameter-Objekt instanziiert, da wir es verwenden, um den Server zu starten, sodass wir uns mit unserem Client verbinden können.
- Eine Methode `run` definiert, die wiederum `stdio_client` aufruft, welches eine Client-Sitzung startet.
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

- Die benötigten Bibliotheken importiert.
- Einen stdio-Transport erstellt und einen Client `mcpClient` erzeugt. Letzteren verwenden wir, um Features auf dem MCP-Server aufzulisten und aufzurufen.

Hinweis: Bei den "Arguments" kannst du entweder auf die *.csproj* Datei oder auf die ausführbare Datei zeigen.

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

- Eine main-Methode erstellt, die einen SSE-Transport auf `http://localhost:8080` setzt, wo unser MCP-Server läuft.
- Eine Client-Klasse erstellt, die den Transport als Konstruktorparameter erhält.
- In der `run`-Methode einen synchronen MCP-Client mit dem Transport erzeugt und die Verbindung initialisiert.
- Den SSE (Server-Sent Events) Transport verwendet, der für HTTP-basierte Kommunikation mit Java Spring Boot MCP-Servern geeignet ist.

#### Rust

Beachte, dass dieser Rust-Client annimmt, dass der Server ein Schwesterprojekt namens "calculator-server" im gleichen Verzeichnis ist. Der folgende Code startet den Server und verbindet sich mit ihm.

```rust
async fn main() -> Result<(), RmcpError> {
    // Gehen Sie davon aus, dass der Server ein Schwesterprojekt namens "calculator-server" im selben Verzeichnis ist
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

    // TODO: Rufen Sie das Hinzufügen-Werkzeug mit Argumenten = {"a": 3, "b": 2} auf

    client.cancel().await?;
    Ok(())
}
```

### -3- Die Serverfunktionen auflisten

Jetzt haben wir einen Client, der sich verbinden kann, wenn das Programm ausgeführt wird. Allerdings listet er seine Features nicht auf, das machen wir jetzt:

#### TypeScript

```typescript
// Liste der Eingabeaufforderungen
const prompts = await client.listPrompts();

// Liste der Ressourcen
const resources = await client.listResources();

// Liste der Werkzeuge
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

Hier listen wir die verfügbaren Ressourcen mit `list_resources()` und Tools mit `list_tools` auf und geben sie aus.

#### .NET

```dotnet
foreach (var tool in await client.ListToolsAsync())
{
    Console.WriteLine($"{tool.Name} ({tool.Description})");
}
```

Oben ein Beispiel, wie wir die Tools auf dem Server auflisten können. Für jedes Tool geben wir dann den Namen aus.

#### Java

```java
// Werkzeuge auflisten und demonstrieren
ListToolsResult toolsList = client.listTools();
System.out.println("Available Tools = " + toolsList);

// Sie können auch den Server anpingen, um die Verbindung zu prüfen
client.ping();
```

Im obigen Code haben wir:

- `listTools()` aufgerufen, um alle verfügbaren Tools vom MCP-Server zu erhalten.
- `ping()` verwendet, um zu prüfen, ob die Verbindung zum Server funktioniert.
- Das `ListToolsResult` enthält Informationen zu allen Tools inklusive Namen, Beschreibungen und Eingabeschemata.

Ausgezeichnet, nun haben wir alle Features erfasst. Aber wann verwenden wir sie? Nun, dieser Client ist ziemlich einfach – einfach im Sinne davon, dass wir die Features explizit aufrufen müssen, wenn wir sie wollen. Im nächsten Kapitel erstellen wir einen fortgeschritteneren Client, der Zugang zu einem eigenen großen Sprachmodell, LLM, hat. Für jetzt aber schauen wir, wie man die Serverfunktionen aufruft:

#### Rust

In der main-Funktion, nachdem der Client initialisiert ist, können wir den Server starten und einige seiner Funktionen auflisten.

```rust
// Initialisieren
let server_info = client.peer_info();
println!("Server info: {:?}", server_info);

// Werkzeuge auflisten
let tools = client.list_tools(Default::default()).await?;
println!("Available tools: {:?}", tools);
```

### -4- Funktionen aufrufen

Um Funktionen aufzurufen, müssen wir sicherstellen, dass wir die korrekten Argumente angeben und in einigen Fällen den Namen des Aufzurufenden.

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

// Aufforderung aufrufen
const promptResult = await client.getPrompt({
    name: "review-code",
    arguments: {
        code: "console.log(\"Hello world\")"
    }
})
```

Im obigen Code haben wir:

- Eine Ressource gelesen, wir rufen die Ressource mit `readResource()` unter Angabe von `uri` auf. So sieht es wahrscheinlich auf der Serverseite aus:

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

    Unser `uri` Wert `file://example.txt` stimmt mit `file://{name}` auf dem Server überein. `example.txt` wird dann `name` zugeordnet.

- Ein Tool aufgerufen, wir rufen es durch Angabe von `name` und den `arguments` wie folgt auf:

    ```typescript
    const result = await client.callTool({
        name: "example-tool",
        arguments: {
            arg1: "value"
        }
    });
    ```

- Eine Eingabeaufforderung bekommen, um eine Eingabeaufforderung zu erhalten, rufst du `getPrompt()` mit `name` und `arguments` auf. Der Servercode sieht so aus:

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

    und dein daraus resultierender Clientcode sieht so aus, um mit dem Server übereinzustimmen:

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

1. Fügen wir etwas Code hinzu, um ein Tool aufzurufen:

  ```csharp
  var result = await mcpClient.CallToolAsync(
      "Add",
      new Dictionary<string, object?>() { ["a"] = 1, ["b"] = 3  },
      cancellationToken:CancellationToken.None);
  ```

1. Um das Ergebnis auszugeben, hier etwas Code zum Verarbeiten:

  ```csharp
  Console.WriteLine(result.Content.First(c => c.Type == "text").Text);
  // Sum 4
  ```

#### Java

```java
// Verschiedene Taschenrechner-Tools aufrufen
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

- Mehrere Rechner-Tools mit `callTool()` Methode und `CallToolRequest` Objekten aufgerufen.
- Jeder Toolaufruf spezifiziert den Toolnamen und eine `Map` mit den von dem Tool benötigten Argumenten.
- Die Server-Tools erwarten spezifische Parameternamen (wie "a", "b" für mathematische Operationen).
- Ergebnisse werden als `CallToolResult` Objekte zurückgegeben, die die Antwort vom Server enthalten.

#### Rust

```rust
// Rufe add tool mit Argumenten auf = {"a": 3, "b": 2}
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

Um den Client auszuführen, tippe folgenden Befehl im Terminal ein:

#### TypeScript

Füge den folgenden Eintrag in deine "scripts"-Sektion der *package.json* ein:

```json
"client": "tsc && node build/client.js"
```

```sh
npm run client
```

#### Python

Rufe den Client mit folgendem Befehl auf:

```sh
python client.py
```

#### .NET

```sh
dotnet run
```

#### Java

Stelle zuerst sicher, dass dein MCP-Server auf `http://localhost:8080` läuft. Dann führe den Client aus:

```bash
# Baue dein Projekt
./mvnw clean compile

# Führe den Client aus
./mvnw exec:java -Dexec.mainClass="com.microsoft.mcp.sample.client.SDKClient"
```

Alternativ kannst du das komplette Client-Projekt aus dem Lösungsordner `03-GettingStarted\02-client\solution\java` ausführen:

```bash
# Navigieren Sie zum Lösungsverzeichnis
cd 03-GettingStarted/02-client/solution/java

# Erstellen und ausführen der JAR-Datei
./mvnw clean package
java -jar target/calculator-client-0.0.1-SNAPSHOT.jar
```

#### Rust

```bash
cargo fmt
cargo run
```

## Aufgabe

In dieser Aufgabe nutzt du das Gelernte, um einen eigenen Client zu erstellen.

Hier ist ein Server, den du mit deinem Client-Code aufrufen kannst. Schau, ob du dem Server weitere Funktionen hinzufügen kannst, um ihn interessanter zu machen.

### TypeScript

```typescript
import { McpServer, ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Erstelle einen MCP-Server
const server = new McpServer({
  name: "Demo",
  version: "1.0.0"
});

// Füge ein Additionswerkzeug hinzu
server.tool("add",
  { a: z.number(), b: z.number() },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Füge eine dynamische Begrüßungsressource hinzu
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

// Beginne Nachrichten auf stdin zu empfangen und Nachrichten auf stdout zu senden

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

# Erstellen Sie einen MCP-Server
mcp = FastMCP("Demo")


# Fügen Sie ein Additionstool hinzu
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


# Fügen Sie eine dynamische Begrüßungsressource hinzu
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

Sieh dir dieses Projekt an, um zu sehen, wie du [Prompts und Ressourcen hinzufügen kannst](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/samples/EverythingServer/Program.cs).

Prüfe auch diesen Link, um zu sehen, wie man [Prompts und Ressourcen aufruft](https://github.com/modelcontextprotocol/csharp-sdk/blob/main/src/ModelContextProtocol/Client/).

### Rust

Im [vorherigen Abschnitt](../../../../03-GettingStarted/01-first-server) hast du gelernt, wie man einen einfachen MCP-Server mit Rust erstellt. Du kannst darauf aufbauen oder diesen Link für weitere MCP Server-Beispiele in Rust prüfen: [MCP Server Beispiele](https://github.com/modelcontextprotocol/rust-sdk/tree/main/examples/servers)

## Lösung

Der **Lösungsordner** enthält komplette, sofort ausführbare Client-Implementierungen, die alle im Tutorial behandelten Konzepte demonstrieren. Jede Lösung umfasst sowohl Client- als auch Server-Code, organisiert in getrennten, eigenständigen Projekten.

### 📁 Lösungsstruktur

Das Lösungsverzeichnis ist nach Programmiersprachen organisiert:

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

- **Vollständige Client-Implementierung** mit allen Funktionen aus dem Tutorial
- **Funktionierende Projektstruktur** mit richtigen Abhängigkeiten und Konfiguration
- **Build- und Ausführungsskripte** für einfache Einrichtung und Ausführung
- **Detaillierte README** mit sprachspezifischen Anleitungen
- **Fehlerbehandlung** und Beispiele zur Verarbeitung von Ergebnissen

### 📖 Nutzung der Lösungen

1. **Navigiere in deinen bevorzugten Sprachordner**:

   ```bash
   cd solution/typescript/    # Für TypeScript
   cd solution/java/          # Für Java
   cd solution/python/        # Für Python
   cd solution/dotnet/        # Für .NET
   ```

2. **Folge den README-Anweisungen** in jedem Ordner für:
   - Installation der Abhängigkeiten
   - Projekt bauen
   - Client ausführen

3. **Beispielausgabe**, die du sehen solltest:

   ```text
   Prompt: Please review this code: console.log("hello");
   Resource template: file
   Tool result: { content: [ { type: 'text', text: '9' } ] }
   ```

Für vollständige Dokumentation und Schritt-für-Schritt-Anleitungen siehe: **[📖 Lösungsdokumentation](./solution/README.md)**

## 🎯 Vollständige Beispiele

Wir haben vollständige, funktionierende Client-Implementierungen für alle in diesem Tutorial behandelten Programmiersprachen bereitgestellt. Diese Beispiele demonstrieren die volle oben beschriebene Funktionalität und können als Referenzimplementierungen oder Ausgangspunkt für deine eigenen Projekte verwendet werden.

### Verfügbare vollständige Beispiele

| Sprache  | Datei                           | Beschreibung                                                       |
|----------|--------------------------------|------------------------------------------------------------------|
| **Java** | [`client_example_java.java`](../../../../03-GettingStarted/02-client/client_example_java.java) | Vollständiger Java-Client mit SSE-Transport und umfassender Fehlerbehandlung |
| **C#**   | [`client_example_csharp.cs`](../../../../03-GettingStarted/02-client/client_example_csharp.cs) | Vollständiger C#-Client mit stdio-Transport und automatischem Serverstart |
| **TypeScript** | [`client_example_typescript.ts`](../../../../03-GettingStarted/02-client/client_example_typescript.ts) | Vollständiger TypeScript-Client mit voller MCP-Protokollunterstützung |
| **Python** | [`client_example_python.py`](../../../../03-GettingStarted/02-client/client_example_python.py) | Vollständiger Python-Client mit async/await-Pattern |
| **Rust** | [`client_example_rust.rs`](../../../../03-GettingStarted/02-client/client_example_rust.rs) | Vollständiger Rust-Client mit Tokio für asynchrone Operationen |

Jedes vollständige Beispiel beinhaltet:
- ✅ **Verbindungsaufbau** und Fehlerbehandlung  
- ✅ **Servererkennung** (Tools, Ressourcen, Eingabeaufforderungen, wo zutreffend)  
- ✅ **Rechenoperationen** (Addieren, Subtrahieren, Multiplizieren, Dividieren, Hilfe)  
- ✅ **Ergebnisverarbeitung** und formatierte Ausgabe  
- ✅ **Umfassende Fehlerbehandlung**  
- ✅ **Sauberer, dokumentierter Code** mit schrittweisen Kommentaren  

### Erste Schritte mit vollständigen Beispielen

1. **Wählen Sie Ihre bevorzugte Sprache** aus der obigen Tabelle  
2. **Überprüfen Sie die vollständige Beispieldatei**, um die vollständige Implementierung zu verstehen  
3. **Führen Sie das Beispiel aus** gemäß den Anweisungen in [`complete_examples.md`](./complete_examples.md)  
4. **Passen Sie das Beispiel an und erweitern Sie es** für Ihren spezifischen Anwendungsfall  

Für ausführliche Dokumentation zum Ausführen und Anpassen dieser Beispiele siehe: **[📖 Dokumentation vollständiger Beispiele](./complete_examples.md)**  

### 💡 Lösung vs. vollständige Beispiele

| **Lösungsordner** | **Vollständige Beispiele** |  
|-------------------|----------------------------|  
| Vollständige Projektstruktur mit Build-Dateien | Einzeldatei-Implementierungen |  
| Sofort lauffähig mit Abhängigkeiten | Fokusierte Codebeispiele |  
| Produktionsähnliche Einrichtung | Pädagogische Referenz |  
| Sprachspezifische Tools | Sprachübergreifender Vergleich |  

Beide Ansätze sind wertvoll – verwenden Sie den **Lösungsordner** für komplette Projekte und die **vollständigen Beispiele** zum Lernen und als Referenz.  

## Wichtige Erkenntnisse

Die wichtigsten Erkenntnisse dieses Kapitels bezüglich Clients sind:

- Können sowohl zur Entdeckung als auch zur Ausführung von Funktionen auf dem Server verwendet werden.  
- Können einen Server starten, während sie selbst gestartet werden (wie in diesem Kapitel), aber Clients können sich auch mit bereits laufenden Servern verbinden.  
- Sind eine großartige Möglichkeit, Serverfunktionen neben Alternativen wie dem Inspector zu testen, wie im vorherigen Kapitel beschrieben.  

## Zusätzliche Ressourcen

- [Clients in MCP erstellen](https://modelcontextprotocol.io/quickstart/client)  

## Beispiele

- [Java-Taschenrechner](../samples/java/calculator/README.md)  
- [.Net-Taschenrechner](../../../../03-GettingStarted/samples/csharp)  
- [JavaScript-Taschenrechner](../samples/javascript/README.md)  
- [TypeScript-Taschenrechner](../samples/typescript/README.md)  
- [Python-Taschenrechner](../../../../03-GettingStarted/samples/python)  
- [Rust-Taschenrechner](../../../../03-GettingStarted/samples/rust)  

## Was kommt als Nächstes

- Nächster Schritt: [Erstellen eines Clients mit einem LLM](../03-llm-client/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache ist die maßgebliche Quelle. Für wichtige Informationen wird eine professionelle, menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->