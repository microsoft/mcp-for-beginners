# Erstellen eines Clients mit LLM

Bisher haben Sie gesehen, wie man einen Server und einen Client erstellt. Der Client konnte explizit den Server aufrufen, um seine Werkzeuge, Ressourcen und Eingabeaufforderungen aufzulisten. Das ist jedoch keine sehr praktische Vorgehensweise. Ihre Nutzer leben im Zeitalter der Agenten und erwarten, Eingabeaufforderungen zu verwenden und mit einem LLM zu kommunizieren. Sie interessiert es nicht, ob Sie MCP zur Speicherung Ihrer Fähigkeiten verwenden; sie erwarten einfach, mit natürlicher Sprache zu interagieren. Wie lösen wir das? Die Lösung besteht darin, dem Client ein LLM hinzuzufügen.

## Überblick

In dieser Lektion konzentrieren wir uns darauf, ein LLM zu Ihrem Client hinzuzufügen und zeigen, wie dies ein viel besseres Erlebnis für Ihre Nutzer bietet.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Einen Client mit einem LLM zu erstellen.
- Nahtlos mit einem MCP-Server unter Verwendung eines LLM zu interagieren.
- Eine bessere Endnutzererfahrung auf der Client-Seite bereitzustellen.

## Vorgehensweise

Lassen Sie uns versuchen, den notwendigen Ansatz zu verstehen. Ein LLM hinzuzufügen klingt einfach, aber wie machen wir das tatsächlich?

So interagiert der Client mit dem Server:

1. Verbindung zum Server aufbauen.

1. Fähigkeiten, Eingabeaufforderungen, Ressourcen und Werkzeuge auflisten und deren Schema speichern.

1. Ein LLM hinzufügen und die gespeicherten Fähigkeiten und deren Schema in einem vom LLM verstandenen Format übergeben.

1. Eine Benutzeranfrage bearbeiten, indem sie zusammen mit den vom Client aufgelisteten Werkzeugen an das LLM übergeben wird.

Großartig, jetzt verstehen wir auf hoher Ebene, wie wir vorgehen können, probieren wir es in der folgenden Übung aus.

## Übung: Erstellen eines Clients mit einem LLM

In dieser Übung lernen wir, wie man einem Client ein LLM hinzufügt.

### Authentifizierung mit GitHub Personal Access Token

Ein GitHub-Token zu erstellen ist ein unkomplizierter Prozess. So geht’s:

- Gehen Sie zu GitHub-Einstellungen – Klicken Sie oben rechts auf Ihr Profilbild und wählen Sie Einstellungen.
- Navigieren Sie zu Entwickler-Einstellungen – Scrollen Sie nach unten und klicken Sie auf Entwickler-Einstellungen.
- Wählen Sie Personal Access Tokens – Klicken Sie auf Fine-grained tokens und dann auf Generate new token.
- Konfigurieren Sie Ihr Token – Fügen Sie eine Notiz zur Referenz hinzu, setzen Sie ein Ablaufdatum und wählen Sie die notwendigen Bereiche (Berechtigungen). In diesem Fall stellen Sie sicher, dass Sie die Erlaubnis für Models hinzufügen.
- Generieren und kopieren Sie das Token – Klicken Sie auf Generate token und kopieren Sie es sofort, da Sie es danach nicht mehr sehen können.

### -1- Verbindung zum Server herstellen

Lassen Sie uns zuerst unseren Client erstellen:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importiere zod für die Schema-Validierung

class MCPClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", 
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }
}
```

Im vorstehenden Code haben wir:

- Die benötigten Bibliotheken importiert
- Eine Klasse mit zwei Mitgliedern erstellt, `client` und `openai`, die uns helfen, einen Client zu verwalten und mit einem LLM zu interagieren.
- Unsere LLM-Instanz konfiguriert, um GitHub Models zu verwenden, indem wir `baseUrl` so gesetzt haben, dass es auf die Inferenz-API zeigt.

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

Im vorstehenden Code haben wir:

- Die benötigten Bibliotheken für MCP importiert
- Einen Client erstellt

#### .NET

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using System.Text.Json;

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

await using var mcpClient = await McpClient.CreateAsync(clientTransport);
```

#### Java

Zuerst müssen Sie die LangChain4j-Abhängigkeiten zu Ihrer `pom.xml`-Datei hinzufügen. Fügen Sie diese Abhängigkeiten hinzu, um MCP-Integration und GitHub Models-Unterstützung zu ermöglichen:

```xml
<properties>
    <langchain4j.version>1.0.0-beta3</langchain4j.version>
</properties>

<dependencies>
    <!-- LangChain4j MCP Integration -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-mcp</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- OpenAI Official API Client -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-open-ai-official</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- GitHub Models Support -->
    <dependency>
        <groupId>dev.langchain4j</groupId>
        <artifactId>langchain4j-github-models</artifactId>
        <version>${langchain4j.version}</version>
    </dependency>
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

Erstellen Sie dann Ihre Java-Client-Klasse:

```java
import dev.langchain4j.mcp.McpToolProvider;
import dev.langchain4j.mcp.client.DefaultMcpClient;
import dev.langchain4j.mcp.client.McpClient;
import dev.langchain4j.mcp.client.transport.McpTransport;
import dev.langchain4j.mcp.client.transport.http.HttpMcpTransport;
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openaiofficial.OpenAiOfficialChatModel;
import dev.langchain4j.service.AiServices;
import dev.langchain4j.service.tool.ToolProvider;

import java.time.Duration;
import java.util.List;

public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        // Konfigurieren Sie das LLM zur Verwendung von GitHub-Modellen
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Erstellen Sie den MCP-Transport zum Verbinden mit dem Server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Erstellen Sie den MCP-Client
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```

Im vorstehenden Code haben wir:

- **LangChain4j-Abhängigkeiten hinzugefügt**: Erforderlich für MCP-Integration, offiziellen OpenAI-Client und GitHub Models-Unterstützung
- **Die LangChain4j-Bibliotheken importiert**: Für MCP-Integration und OpenAI-Chatmodell-Funktionalität
- **Einen `ChatLanguageModel` erstellt**: Konfiguriert zur Verwendung von GitHub Models mit Ihrem GitHub-Token
- **HTTP-Transport eingerichtet**: Mithilfe von Server-Sent Events (SSE), um eine Verbindung zum MCP-Server herzustellen
- **Einen MCP-Client erstellt**: Der die Kommunikation mit dem Server übernimmt
- **LangChain4j's integrierte MCP-Unterstützung verwendet**: Die die Integration zwischen LLMs und MCP-Servern vereinfacht

#### Rust

Dieses Beispiel setzt voraus, dass Sie einen auf Rust basierenden MCP-Server betreiben. Falls Sie noch keinen haben, schauen Sie zur vorherigen Lektion [01-first-server](../01-first-server/README.md) zurück, um den Server zu erstellen.

Sobald Sie Ihren Rust MCP-Server haben, öffnen Sie ein Terminal und wechseln in dasselbe Verzeichnis wie der Server. Führen Sie dann den folgenden Befehl aus, um ein neues LLM-Clientprojekt zu erstellen:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Fügen Sie die folgenden Abhängigkeiten zu Ihrer `Cargo.toml`-Datei hinzu:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Es gibt keine offizielle Rust-Bibliothek für OpenAI, jedoch ist die `async-openai`-Crate eine [community-gepflegte Bibliothek](https://platform.openai.com/docs/libraries/rust#rust), die häufig verwendet wird.

Öffnen Sie die Datei `src/main.rs` und ersetzen Sie deren Inhalt durch den folgenden Code:

```rust
use async_openai::{Client, config::OpenAIConfig};
use rmcp::{
    RmcpError,
    model::{CallToolRequestParam, ListToolsResult},
    service::{RoleClient, RunningService, ServiceExt},
    transport::{ConfigureCommandExt, TokioChildProcess},
};
use serde_json::{Value, json};
use std::error::Error;
use tokio::process::Command;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Anfangsnachricht
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // OpenAI-Client einrichten
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // MCP-Client einrichten
    let server_dir = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
        .parent()
        .unwrap()
        .join("calculator-server");

    let mcp_client = ()
        .serve(
            TokioChildProcess::new(Command::new("cargo").configure(|cmd| {
                cmd.arg("run").current_dir(server_dir);
            }))
            .map_err(RmcpError::transport_creation::<TokioChildProcess>)?,
        )
        .await?;

    // TODO: MCP-Werkzeugliste abrufen

    // TODO: LLM-Konversation mit Werkzeugaufrufen

    Ok(())
}
```

Dieser Code richtet eine einfache Rust-Anwendung ein, die eine Verbindung zu einem MCP-Server und GitHub Models für LLM-Interaktionen herstellt.

> [!IMPORTANT]
> Stellen Sie sicher, dass Sie vor dem Ausführen der Anwendung die Umgebungsvariable `OPENAI_API_KEY` mit Ihrem GitHub-Token setzen.

Super, für den nächsten Schritt listen wir die Fähigkeiten auf dem Server auf.

### -2- Serverfähigkeiten auflisten

Jetzt verbinden wir uns mit dem Server und fragen seine Fähigkeiten ab:

#### Typescript

Fügen Sie in derselben Klasse die folgenden Methoden hinzu:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // Auflistung von Werkzeugen
    const toolsResult = await this.client.listTools();
}
```

Im vorstehenden Code haben wir:

- Code zum Verbinden mit dem Server hinzugefügt, `connectToServer`.
- Eine `run`-Methode erstellt, die für den Ablauf unserer App zuständig ist. Bisher listet sie nur die Werkzeuge auf, aber wir werden bald mehr hinzufügen.

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
    print("Tool", tool.inputSchema["properties"])
```

Das haben wir hinzugefügt:

- Ressourcen und Werkzeuge aufgelistet und ausgegeben. Für Werkzeuge listen wir außerdem `inputSchema` auf, das wir später verwenden.

#### .NET

```csharp
async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        // TODO: convert tool definition from MCP tool to LLm tool     
    }

    return toolDefinitions;
}
```

Im vorstehenden Code haben wir:

- Die auf dem MCP-Server verfügbaren Werkzeuge aufgelistet
- Für jedes Werkzeug Name, Beschreibung und dessen Schema gelistet. Letzteres verwenden wir, um die Werkzeuge bald aufzurufen.

#### Java

```java
// Erstellen Sie einen Tool-Anbieter, der MCP-Tools automatisch entdeckt
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Der MCP-Tool-Anbieter übernimmt automatisch:
// - Auflisten verfügbarer Tools vom MCP-Server
// - Umwandeln von MCP-Tool-Schemata in das LangChain4j-Format
// - Verwalten der Tool-Ausführung und der Antworten
```

Im vorstehenden Code haben wir:

- Einen `McpToolProvider` erstellt, der automatisch alle Werkzeuge vom MCP-Server entdeckt und registriert
- Der Werkzeuganbieter übernimmt intern die Konvertierung zwischen MCP-Werkzeugschema und dem Tool-Format von LangChain4j
- Dieser Ansatz abstrahiert den manuellen Werkzeug-Listing- und Konvertierungsprozess

#### Rust

Das Abrufen von Werkzeugen vom MCP-Server erfolgt mit der Methode `list_tools`. Fügen Sie in Ihrer `main`-Funktion, nachdem der MCP-Client eingerichtet ist, den folgenden Code hinzu:

```rust
// MCP-Werkzeugauflistung abrufen
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Serverfähigkeiten in LLM-Werkzeuge umwandeln

Der nächste Schritt nach dem Auflisten der Serverfähigkeiten ist, sie in ein vom LLM verstandenes Format zu konvertieren. Sobald wir das getan haben, können wir diese Fähigkeiten als Werkzeuge für unser LLM bereitstellen.

#### TypeScript

1. Fügen Sie folgenden Code hinzu, um die Antwort vom MCP-Server in ein Werkzeugformat zu konvertieren, das das LLM verwenden kann:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Erstelle ein Zod-Schema basierend auf dem Eingabeschema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Setze den Typ explizit auf "Funktion"
            function: {
            name: tool.name,
            description: tool.description,
            parameters: {
            type: "object",
            properties: tool.input_schema.properties,
            required: tool.input_schema.required,
            },
            },
        };
    }

    ```

    Der obige Code nimmt eine Antwort vom MCP-Server und wandelt sie in ein Werkzeugdefinitionsformat um, das das LLM versteht.

1. Aktualisieren wir als Nächstes die `run`-Methode, um die Serverfähigkeiten aufzulisten:

    ```typescript
    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
            name: tool.name,
            description: tool.description,
            input_schema: tool.inputSchema,
            });
        });
    }
    ```

    Im vorstehenden Code haben wir die `run`-Methode aktualisiert, so dass sie das Ergebnis durchläuft und für jeden Eintrag `openAiToolAdapter` aufruft.

#### Python

1. Erstellen wir zuerst die folgende Konverterfunktion

    ```python
    def convert_to_llm_tool(tool):
        tool_schema = {
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description,
                "type": "function",
                "parameters": {
                    "type": "object",
                    "properties": tool.inputSchema["properties"]
                }
            }
        }

        return tool_schema
    ```

    In der Funktion `convert_to_llm_tools` nehmen wir eine MCP-Werkzeugantwort und konvertieren sie in ein Format, das das LLM versteht.

1. Aktualisieren wir nun unseren Clientcode, um diese Funktion wie folgt zu nutzen:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Hier fügen wir einen Aufruf zu `convert_to_llm_tool` hinzu, um die MCP-Werkzeugantwort in etwas zu konvertieren, das wir später dem LLM übergeben können.

#### .NET

1. Fügen wir Code hinzu, um die MCP-Werkzeugantwort in etwas zu konvertieren, das das LLM verstehen kann:

```csharp
ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}
```

Im vorstehenden Code haben wir:

- Eine Funktion `ConvertFrom` erstellt, die Name, Beschreibung und Eingabeschema entgegennimmt.
- Eine Funktionalität definiert, die eine FunctionDefinition erstellt, die an eine ChatCompletionsDefinition übergeben wird. Letzteres versteht das LLM.

1. Schauen wir uns an, wie wir bestehenden Code aktualisieren können, um diese Funktion zu nutzen:

    ```csharp
    async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
    {
        Console.WriteLine("Listing tools");
        var tools = await mcpClient.ListToolsAsync();

        List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

        foreach (var tool in tools)
        {
            Console.WriteLine($"Connected to server with tools: {tool.Name}");
            Console.WriteLine($"Tool description: {tool.Description}");
            Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

            JsonElement propertiesElement;
            tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

            var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
            Console.WriteLine($"Tool definition: {def}");
            toolDefinitions.Add(def);

            Console.WriteLine($"Properties: {propertiesElement}");        
        }

        return toolDefinitions;
    }
    ```    In the preceding code, we've:

    - Update the function to convert the MCP tool response to an LLm tool. Let's highlight the code we added:

        ```csharp
        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);
        ```

        The input schema is part of the tool response but on the "properties" attribute, so we need to extract. Furthermore, we now call `ConvertFrom` with the tool details. Now we've done the heavy lifting, let's see how it call comes together as we handle a user prompt next.

#### Java

```java
// Erstellen Sie eine Bot-Schnittstelle für die natürliche Sprachinteraktion
public interface Bot {
    String chat(String prompt);
}

// Konfigurieren Sie den KI-Dienst mit LLM- und MCP-Werkzeugen
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

Im vorstehenden Code haben wir:

- Ein einfaches `Bot`-Interface für natürliche Sprachinteraktionen definiert
- LangChain4j's `AiServices` verwendet, um das LLM automatisch mit dem MCP-Toolanbieter zu verbinden
- Das Framework übernimmt automatisch die Werkzeugschemakonvertierung und das Funktionsaufruf-Handling im Hintergrund
- Dieser Ansatz eliminiert manuelle Werkzeugkonvertierung – LangChain4j übernimmt die gesamte Komplexität der Umwandlung von MCP-Werkzeugen in LLM-kompatibles Format

#### Rust

Um die MCP-Werkzeugantwort in ein für das LLM verständliches Format zu konvertieren, fügen wir eine Hilfsfunktion hinzu, die die Werkzeugauflistung formatiert. Fügen Sie den folgenden Code in Ihre `main.rs`-Datei unterhalb der `main`-Funktion ein. Diese wird bei Anfragen an das LLM aufgerufen:

```rust
async fn format_tools(tools: &ListToolsResult) -> Result<Vec<Value>, Box<dyn Error>> {
    let tools_json = serde_json::to_value(tools)?;
    let Some(tools_array) = tools_json.get("tools").and_then(|t| t.as_array()) else {
        return Ok(vec![]);
    };

    let formatted_tools = tools_array
        .iter()
        .filter_map(|tool| {
            let name = tool.get("name")?.as_str()?;
            let description = tool.get("description")?.as_str()?;
            let schema = tool.get("inputSchema")?;

            Some(json!({
                "type": "function",
                "function": {
                    "name": name,
                    "description": description,
                    "parameters": {
                        "type": "object",
                        "properties": schema.get("properties").unwrap_or(&json!({})),
                        "required": schema.get("required").unwrap_or(&json!([]))
                    }
                }
            }))
        })
        .collect();

    Ok(formatted_tools)
}
```

Super, wir sind jetzt bereit, Benutzeranfragen zu bearbeiten, also kommen wir zum nächsten Schritt.

### -4- Benutzeranfragen verarbeiten

In diesem Teil des Codes werden wir Benutzeranfragen bearbeiten.

#### TypeScript

1. Fügen Sie eine Methode hinzu, die aufgerufen wird, um unser LLM anzusprechen:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Rufe das Werkzeug des Servers auf
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Mache etwas mit dem Ergebnis
        // TODO

        }
    }
    ```

    Im vorstehenden Code haben wir:

    - Eine Methode `callTools` hinzugefügt.
    - Die Methode nimmt eine Antwort vom LLM entgegen und prüft, welche Werkzeuge ggf. aufgerufen werden sollen:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // Werkzeug aufrufen
        }
        ```

    - Ruft ein Werkzeug auf, falls das LLM anzeigt, dass es aufgerufen werden soll:

        ```typescript
        // 2. Rufen Sie das Werkzeug des Servers auf
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Machen Sie etwas mit dem Ergebnis
        // TODO
        ```

1. Aktualisieren Sie die `run`-Methode, um Aufrufe zum LLM und zum `callTools`-Methodenaufruf einzufügen:

    ```typescript

    // 1. Erstellen Sie Nachrichten, die Eingaben für das LLM sind
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Aufruf des LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Durchgehen der LLM-Antwort, für jede Auswahl prüfen, ob sie Werkzeugaufrufe enthält
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Super, hier ist der vollständige Code:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importiere zod für Schema-Validierung

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // Möglicherweise muss die URL in Zukunft geändert werden: https://models.github.ai/inference
            apiKey: process.env.GITHUB_TOKEN,
        });

        this.client = new Client(
            {
                name: "example-client",
                version: "1.0.0"
            },
            {
                capabilities: {
                prompts: {},
                resources: {},
                tools: {}
                }
            }
            );    
    }

    async connectToServer(transport: Transport) {
        await this.client.connect(transport);
        this.run();
        console.error("MCPClient started on stdin/stdout");
    }

    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
          }) {
          // Erstelle ein zod-Schema basierend auf dem input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Setze den Typ explizit auf "function"
            function: {
              name: tool.name,
              description: tool.description,
              parameters: {
              type: "object",
              properties: tool.input_schema.properties,
              required: tool.input_schema.required,
              },
            },
          };
    }
    
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
      ) {
        for (const tool_call of tool_calls) {
          const toolName = tool_call.function.name;
          const args = tool_call.function.arguments;
    
          console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);
    
    
          // 2. Rufe das Tool des Servers auf
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Mache etwas mit dem Ergebnis
          // TODO
    
         }
    }

    async run() {
        console.log("Asking server for available tools");
        const toolsResult = await this.client.listTools();
        const tools = toolsResult.tools.map((tool) => {
            return this.openAiToolAdapter({
              name: tool.name,
              description: tool.description,
              input_schema: tool.inputSchema,
            });
        });

        const prompt = "What is the sum of 2 and 3?";
    
        const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

        console.log("Querying LLM: ", messages[0].content);
        let response = this.openai.chat.completions.create({
            model: "gpt-4.1-mini",
            max_tokens: 1000,
            messages,
            tools: tools,
        });    

        let results: any[] = [];
    
        // 1. Gehe die LLM-Antwort durch, überprüfe für jede Wahl, ob Tool-Aufrufe enthalten sind
        (await response).choices.map(async (choice: { message: any; }) => {
          const message = choice.message;
          if (message.tool_calls) {
              console.log("Making tool call")
              await this.callTools(message.tool_calls, results);
          }
        });
    }
    
}

let client = new MyClient();
 const transport = new StdioClientTransport({
            command: "node",
            args: ["./build/index.js"]
        });

client.connectToServer(transport);
```

#### Python

1. Fügen wir zunächst notwendige Importe hinzu, um ein LLM aufzurufen:

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

1. Fügen wir anschließend die Funktion hinzu, die das LLM aufruft:

    ```python
    # llm

    def call_llm(prompt, functions):
        token = os.environ["GITHUB_TOKEN"]
        endpoint = "https://models.inference.ai.azure.com"

        model_name = "gpt-4o"

        client = ChatCompletionsClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(token),
        )

        print("CALLING LLM")
        response = client.complete(
            messages=[
                {
                "role": "system",
                "content": "You are a helpful assistant.",
                },
                {
                "role": "user",
                "content": prompt,
                },
            ],
            model=model_name,
            tools = functions,
            # Optionale Parameter
            temperature=1.,
            max_tokens=1000,
            top_p=1.    
        )

        response_message = response.choices[0].message
        
        functions_to_call = []

        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                print("TOOL: ", tool_call)
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                functions_to_call.append({ "name": name, "args": args })

        return functions_to_call
    ```

    Im vorstehenden Code haben wir:

    - Unsere Funktionen, die wir auf dem MCP-Server gefunden und konvertiert haben, an das LLM übergeben.
    - Das LLM mit diesen Funktionen aufgerufen.
    - Das Ergebnis geprüft, welche Funktionen ggf. aufgerufen werden sollen.
    - Schließlich ein Array von aufzurufenden Funktionen übergeben.

1. Abschließend aktualisieren wir unseren Hauptcode:

    ```python
    prompt = "Add 2 to 20"

    # frage das LLM, welche Werkzeuge alle verwenden sollen, falls vorhanden
    functions_to_call = call_llm(prompt, functions)

    # rufe vorgeschlagene Funktionen auf
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Das war der letzte Schritt, im obigen Code:

    - Rufen wir ein MCP-Werkzeug via `call_tool` auf, indem wir eine Funktion übergeben, von der das LLM aufgrund unserer Eingabeaufforderung angenommen hat, dass sie aufgerufen werden soll.
    - Geben wir das Ergebnis des Werkzeugsaufrufs an den MCP-Server aus.

#### .NET

1. Hier ein Beispielcode für die Durchführung einer LLM-Eingabeaufforderung:

    ```csharp
    var tools = await GetMcpTools();

    for (int i = 0; i < tools.Count; i++)
    {
        var tool = tools[i];
        Console.WriteLine($"MCP Tools def: {i}: {tool}");
    }

    // 0. Define the chat history and the user message
    var userMessage = "add 2 and 4";

    chatHistory.Add(new ChatRequestUserMessage(userMessage));

    // 1. Define tools
    ChatCompletionsToolDefinition def = CreateToolDefinition();


    // 2. Define options, including the tools
    var options = new ChatCompletionsOptions(chatHistory)
    {
        Model = "gpt-4.1-mini",
        Tools = { tools[0] }
    };

    // 3. Call the model  

    ChatCompletions? response = await client.CompleteAsync(options);
    var content = response.Content;

    ```

    Im vorstehenden Code haben wir:

    - Werkzeuge vom MCP-Server abgerufen, `var tools = await GetMcpTools()`.
    - Eine Benutzereingabe (`userMessage`) definiert.
    - Ein Optionsobjekt mit Modell und Werkzeugen erstellt.
    - Eine Anfrage an das LLM gesendet.

1. Zum Abschluss prüfen wir, ob das LLM einen Funktionsaufruf vorschlägt:

    ```csharp
    // 4. Check if the response contains a function call
    ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
    for (int i = 0; i < response.ToolCalls.Count; i++)
    {
        var call = response.ToolCalls[i];
        Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
        //Tool call 0: add with arguments {"a":2,"b":4}

        var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
        var result = await mcpClient.CallToolAsync(
            call.Name,
            dict!,
            cancellationToken: CancellationToken.None
        );

        Console.WriteLine(result.Content.First(c => c.Type == "text").Text);

    }
    ```

    Im vorstehenden Code haben wir:

    - Über eine Liste von Funktionsaufrufen iteriert.
    - Für jeden Werkzeugaufruf Name und Argumente analysiert und das Werkzeug auf dem MCP-Server mit dem MCP-Client aufgerufen. Zuletzt geben wir die Ergebnisse aus.

Hier ist der vollständige Code:

```csharp
using Azure;
using Azure.AI.Inference;
using Azure.Identity;
using System.Text.Json;
using ModelContextProtocol.Client;
using ModelContextProtocol.Protocol;

var endpoint = "https://models.inference.ai.azure.com";
var token = Environment.GetEnvironmentVariable("GITHUB_TOKEN"); // Your GitHub Access Token
var client = new ChatCompletionsClient(new Uri(endpoint), new AzureKeyCredential(token));
var chatHistory = new List<ChatRequestMessage>
{
    new ChatRequestSystemMessage("You are a helpful assistant that knows about AI")
};

var clientTransport = new StdioClientTransport(new()
{
    Name = "Demo Server",
    Command = "/workspaces/mcp-for-beginners/03-GettingStarted/02-client/solution/server/bin/Debug/net8.0/server",
    Arguments = [],
});

Console.WriteLine("Setting up stdio transport");

await using var mcpClient = await McpClient.CreateAsync(clientTransport);

ChatCompletionsToolDefinition ConvertFrom(string name, string description, JsonElement jsonElement)
{ 
    // convert the tool to a function definition
    FunctionDefinition functionDefinition = new FunctionDefinition(name)
    {
        Description = description,
        Parameters = BinaryData.FromObjectAsJson(new
        {
            Type = "object",
            Properties = jsonElement
        },
        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase })
    };

    // create a tool definition
    ChatCompletionsToolDefinition toolDefinition = new ChatCompletionsToolDefinition(functionDefinition);
    return toolDefinition;
}



async Task<List<ChatCompletionsToolDefinition>> GetMcpTools()
{
    Console.WriteLine("Listing tools");
    var tools = await mcpClient.ListToolsAsync();

    List<ChatCompletionsToolDefinition> toolDefinitions = new List<ChatCompletionsToolDefinition>();

    foreach (var tool in tools)
    {
        Console.WriteLine($"Connected to server with tools: {tool.Name}");
        Console.WriteLine($"Tool description: {tool.Description}");
        Console.WriteLine($"Tool parameters: {tool.JsonSchema}");

        JsonElement propertiesElement;
        tool.JsonSchema.TryGetProperty("properties", out propertiesElement);

        var def = ConvertFrom(tool.Name, tool.Description, propertiesElement);
        Console.WriteLine($"Tool definition: {def}");
        toolDefinitions.Add(def);

        Console.WriteLine($"Properties: {propertiesElement}");        
    }

    return toolDefinitions;
}

// 1. List tools on mcp server

var tools = await GetMcpTools();
for (int i = 0; i < tools.Count; i++)
{
    var tool = tools[i];
    Console.WriteLine($"MCP Tools def: {i}: {tool}");
}

// 2. Define the chat history and the user message
var userMessage = "add 2 and 4";

chatHistory.Add(new ChatRequestUserMessage(userMessage));


// 3. Define options, including the tools
var options = new ChatCompletionsOptions(chatHistory)
{
    Model = "gpt-4.1-mini",
    Tools = { tools[0] }
};

// 4. Call the model  

ChatCompletions? response = await client.CompleteAsync(options);
var content = response.Content;

// 5. Check if the response contains a function call
ChatCompletionsToolCall? calls = response.ToolCalls.FirstOrDefault();
for (int i = 0; i < response.ToolCalls.Count; i++)
{
    var call = response.ToolCalls[i];
    Console.WriteLine($"Tool call {i}: {call.Name} with arguments {call.Arguments}");
    //Tool call 0: add with arguments {"a":2,"b":4}

    var dict = JsonSerializer.Deserialize<Dictionary<string, object>>(call.Arguments);
    var result = await mcpClient.CallToolAsync(
        call.Name,
        dict!,
        cancellationToken: CancellationToken.None
    );

    Console.WriteLine(result.Content.OfType<TextContentBlock>().First().Text);

}

// 5. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Führe natürlichsprachliche Anfragen aus, die automatisch MCP-Werkzeuge verwenden
    String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
    System.out.println(response);

    response = bot.chat("What's the square root of 144?");
    System.out.println(response);

    response = bot.chat("Show me the help for the calculator service");
    System.out.println(response);
} finally {
    mcpClient.close();
}
```

Im vorstehenden Code haben wir:

- Einfache natürliche Sprachprompts genutzt, um mit den MCP-Server-Werkzeugen zu interagieren
- Das LangChain4j Framework kümmert sich automatisch um:
  - Die Umwandlung von Benutzereingaben in Werkzeugaufrufe bei Bedarf
  - Das Aufrufen der passenden MCP-Werkzeuge basierend auf der Entscheidung des LLM
  - Das Verwalten des Gesprächsflusses zwischen LLM und MCP-Server
- Die `bot.chat()`-Methode gibt natürliche Sprachantworten zurück, die auch Ergebnisse von MCP-Werkzeug-Ausführungen enthalten können
- Dieser Ansatz bietet ein nahtloses Benutzererlebnis, bei dem Nutzer nichts über die unterliegende MCP-Implementierung wissen müssen

Vollständiges Codebeispiel:

```java
public class LangChain4jClient {
    
    public static void main(String[] args) throws Exception {        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .timeout(Duration.ofSeconds(60))
                .build();

        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();

        ToolProvider toolProvider = McpToolProvider.builder()
                .mcpClients(List.of(mcpClient))
                .build();

        Bot bot = AiServices.builder(Bot.class)
                .chatLanguageModel(model)
                .toolProvider(toolProvider)
                .build();

        try {
            String response = bot.chat("Calculate the sum of 24.5 and 17.3 using the calculator service");
            System.out.println(response);

            response = bot.chat("What's the square root of 144?");
            System.out.println(response);

            response = bot.chat("Show me the help for the calculator service");
            System.out.println(response);
        } finally {
            mcpClient.close();
        }
    }
}
```

#### Rust

Hier passiert der Großteil der Arbeit. Wir rufen das LLM mit der initialen Benutzeranfrage auf, verarbeiten die Antwort, um zu prüfen, ob Werkzeuge aufgerufen werden müssen. Falls ja, rufen wir diese Werkzeuge auf und setzen das Gespräch mit dem LLM fort, bis keine weiteren Werkzeugaufrufe nötig sind und wir eine finale Antwort haben.

Wir werden mehrere Aufrufe an das LLM machen, also definieren wir eine Funktion, die diese LLM-Aufrufe übernimmt. Fügen Sie die folgende Funktion in Ihre `main.rs`-Datei ein:

```rust
async fn call_llm(
    client: &Client<OpenAIConfig>,
    messages: &[Value],
    tools: &ListToolsResult,
) -> Result<Value, Box<dyn Error>> {
    let response = client
        .completions()
        .create_byot(json!({
            "messages": messages,
            "model": "openai/gpt-4.1",
            "tools": format_tools(tools).await?,
        }))
        .await?;
    Ok(response)
}
```

Diese Funktion erhält den LLM-Client, eine Liste von Nachrichten (einschließlich der Benutzeranfrage), Werkzeuge vom MCP-Server, sendet eine Anfrage an das LLM und gibt die Antwort zurück.
Die Antwort vom LLM wird ein Array von `choices` enthalten. Wir müssen das Ergebnis verarbeiten, um zu sehen, ob `tool_calls` vorhanden sind. Das zeigt uns, dass das LLM anfordert, dass ein bestimmtes Tool mit Argumenten aufgerufen werden soll. Fügen Sie den folgenden Code ans Ende Ihrer `main.rs`-Datei ein, um eine Funktion zur Handhabung der LLM-Antwort zu definieren:

```rust
async fn process_llm_response(
    llm_response: &Value,
    mcp_client: &RunningService<RoleClient, ()>,
    openai_client: &Client<OpenAIConfig>,
    mcp_tools: &ListToolsResult,
    messages: &mut Vec<Value>,
) -> Result<(), Box<dyn Error>> {
    let Some(message) = llm_response
        .get("choices")
        .and_then(|c| c.as_array())
        .and_then(|choices| choices.first())
        .and_then(|choice| choice.get("message"))
    else {
        return Ok(());
    };

    // Inhalt drucken, wenn verfügbar
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Werkzeugaufrufe bearbeiten
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Assistenten-Nachricht hinzufügen

        // Jeden Werkzeugaufruf ausführen
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Werkzeugergebnis zu Nachrichten hinzufügen
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Gespräch mit Werkzeugergebnissen fortsetzen
        let response = call_llm(openai_client, messages, mcp_tools).await?;
        Box::pin(process_llm_response(
            &response,
            mcp_client,
            openai_client,
            mcp_tools,
            messages,
        ))
        .await?;
    }
    Ok(())
}
```


Wenn `tool_calls` vorhanden sind, extrahiert sie die Tool-Informationen, ruft den MCP-Server mit der Tool-Anfrage auf und fügt die Ergebnisse zu den Konversationsnachrichten hinzu. Anschließend wird die Unterhaltung mit dem LLM fortgesetzt und die Nachrichten werden mit der Antwort des Assistenten und den Ergebnissen des Tool-Aufrufs aktualisiert.

Um die Tool-Aufruf-Informationen, die das LLM für MCP-Aufrufe zurückgibt, zu extrahieren, fügen wir eine weitere Hilfsfunktion hinzu, die alles Nötige zur Durchführung des Aufrufs extrahiert. Fügen Sie den folgenden Code ans Ende Ihrer `main.rs`-Datei ein:

```rust
fn extract_tool_call_info(tool_call: &Value) -> Result<(String, String, String), Box<dyn Error>> {
    let tool_id = tool_call
        .get("id")
        .and_then(|id| id.as_str())
        .unwrap_or("")
        .to_string();
    let function = tool_call.get("function").ok_or("Missing function")?;
    let name = function
        .get("name")
        .and_then(|n| n.as_str())
        .unwrap_or("")
        .to_string();
    let args = function
        .get("arguments")
        .and_then(|a| a.as_str())
        .unwrap_or("{}")
        .to_string();
    Ok((tool_id, name, args))
}
```


Mit allen notwendigen Komponenten können wir nun die initiale Benutzeranfrage verarbeiten und das LLM aufrufen. Aktualisieren Sie Ihre `main`-Funktion, um den folgenden Code einzuschließen:

```rust
// LLM-Unterhaltung mit Werkzeugaufrufen
let response = call_llm(&openai_client, &messages, &tools).await?;
process_llm_response(
    &response,
    &mcp_client,
    &openai_client,
    &tools,
    &mut messages,
)
.await?;
```


Das wird das LLM mit der initialen Benutzeranfrage abfragen, die nach der Summe von zwei Zahlen fragt, und es verarbeitet die Antwort, um dynamisch Tool-Aufrufe zu handhaben.

Großartig, Sie haben es geschafft!

## Aufgabe

Nehmen Sie den Code aus der Übung und bauen Sie den Server mit weiteren Tools aus. Erstellen Sie dann einen Client mit einem LLM, wie in der Übung, und testen Sie ihn mit verschiedenen Eingaben, um sicherzustellen, dass alle Ihre Server-Tools dynamisch aufgerufen werden. Diese Art, einen Client zu erstellen, sorgt für ein großartiges Benutzererlebnis, da der Endnutzer in der Lage ist, Eingaben zu verwenden, statt exakte Client-Befehle, und nichts von eventuell aufgerufenen MCP-Servern bemerkt.

## Lösung

[Lösung](/03-GettingStarted/03-llm-client/solution/README.md)

## Wichtige Erkenntnisse

- Die Integration eines LLM in Ihren Client bietet eine bessere Möglichkeit für Benutzer, mit MCP-Servern zu interagieren.
- Sie müssen die Antwort des MCP-Servers in etwas umwandeln, das das LLM verstehen kann.

## Beispiele

- [Java Rechner](../samples/java/calculator/README.md)
- [.Net Rechner](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Rechner](../samples/javascript/README.md)
- [TypeScript Rechner](../samples/typescript/README.md)
- [Python Rechner](../../../../03-GettingStarted/samples/python)
- [Rust Rechner](../../../../03-GettingStarted/samples/rust)

## Zusätzliche Ressourcen

## Wie geht es weiter

- Nächstes Thema: [Einen Server mit Visual Studio Code konsumieren](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir um Genauigkeit bemüht sind, weisen wir darauf hin, dass automatische Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->