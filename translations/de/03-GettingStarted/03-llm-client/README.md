# Erstellen eines Clients mit LLM

Bis jetzt hast du gesehen, wie man einen Server und einen Client erstellt. Der Client konnte den Server explizit aufrufen, um seine Tools, Ressourcen und Eingabeaufforderungen aufzulisten. Dies ist jedoch keine sehr praktische Vorgehensweise. Deine Nutzer leben im agentischen Zeitalter und erwarten, Prompts zu verwenden und mit einem LLM zu kommunizieren. Es ist ihnen egal, ob du MCP zur Speicherung deiner Fähigkeiten verwendest; sie erwarten einfach, in natürlicher Sprache zu interagieren. Wie lösen wir das also? Die Lösung besteht darin, dem Client ein LLM hinzuzufügen.

## Überblick

In dieser Lektion konzentrieren wir uns darauf, dem Client ein LLM hinzuzufügen und zeigen, wie dies eine wesentlich bessere Nutzererfahrung ermöglicht.

## Lernziele

Am Ende dieser Lektion wirst du in der Lage sein:

- Einen Client mit einem LLM zu erstellen.
- Nahtlos mit einem MCP-Server über ein LLM zu interagieren.
- Eine bessere Endnutzererfahrung auf der Client-Seite zu bieten.

## Vorgehensweise

Lass uns versuchen zu verstehen, wie wir vorgehen müssen. Ein LLM hinzuzufügen klingt einfach, aber werden wir das tatsächlich tun?

So wird der Client mit dem Server interagieren:

1. Verbindung mit dem Server herstellen.

1. Fähigkeiten, Prompts, Ressourcen und Tools auflisten und deren Schema speichern.

1. Ein LLM hinzufügen und die gespeicherten Fähigkeiten sowie deren Schema in einem Format übergeben, das das LLM versteht.

1. Eine Nutzeranfrage bearbeiten, indem diese zusammen mit den vom Client gelisteten Tools an das LLM übergeben wird.

Super, jetzt verstehen wir, wie wir das auf hoher Ebene machen können, probieren wir es in der folgenden Übung aus.

## Übung: Erstellen eines Clients mit einem LLM

In dieser Übung lernen wir, ein LLM zu unserem Client hinzuzufügen.

### Authentifizierung mittels GitHub Personal Access Token

Das Erstellen eines GitHub-Tokens ist ein einfacher Prozess. So kannst du es machen:

- Gehe zu GitHub-Einstellungen – Klicke auf dein Profilbild oben rechts und wähle Einstellungen.
- Navigiere zu Entwickler-Einstellungen – Scrolle nach unten und klicke auf Entwickler-Einstellungen.
- Wähle Persönliche Zugangstoken – Klicke auf Feingranulare Tokens und dann auf Neues Token generieren.
- Konfiguriere dein Token – Füge eine Notiz zur Referenz hinzu, setze ein Ablaufdatum und wähle die benötigten Berechtigungen aus. Füge in diesem Fall unbedingt die Berechtigung „Models“ hinzu.
- Generiere und kopiere das Token – Klicke auf Token generieren und stelle sicher, dass du es sofort kopierst, da du es später nicht nochmal sehen kannst.

### -1- Verbindung zum Server herstellen

Erstellen wir zuerst unseren Client:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Zod für die Schemavalidierung importieren

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
  
Im obigen Code haben wir:

- Die benötigten Bibliotheken importiert  
- Eine Klasse mit zwei Mitgliedern `client` und `openai` erstellt, die uns helfen, einen Client zu verwalten und mit einem LLM zu interagieren.  
- Unsere LLM-Instanz so konfiguriert, dass GitHub Models verwendet werden, indem `baseUrl` auf die Inferenz-API gesetzt wurde.  

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Erstellen Sie Serverparameter für die stdio-Verbindung
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
            # Initialisieren Sie die Verbindung
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```
  
Im obigen Code haben wir:

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

Zuerst musst du die LangChain4j-Abhängigkeiten zu deiner `pom.xml` Datei hinzufügen. Füge diese Abhängigkeiten hinzu, um MCP-Integration und GitHub Models-Unterstützung zu ermöglichen:

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
  
Erstelle dann deine Java-Client-Klasse:

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
    
    public static void main(String[] args) throws Exception {        // Konfigurieren Sie das LLM für die Verwendung von GitHub-Modellen
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .isGitHubModels(true)
                .apiKey(System.getenv("GITHUB_TOKEN"))
                .timeout(Duration.ofSeconds(60))
                .modelName("gpt-4.1-nano")
                .build();

        // Erstellen Sie einen MCP-Transport für die Verbindung zum Server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Erstellen Sie einen MCP-Client
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }
}
```
  
Im obigen Code haben wir:

- **LangChain4j-Abhängigkeiten hinzugefügt**: notwendig für MCP-Integration, offiziellen OpenAI-Client und GitHub Models-Unterstützung  
- **LangChain4j-Bibliotheken importiert**: für MCP-Integration und OpenAI Chatmodell-Funktionalität  
- **Ein `ChatLanguageModel` erstellt**: konfiguriert für GitHub Models mit deinem GitHub-Token  
- **HTTP-Transport eingerichtet**: mit Server-Sent Events (SSE) zur Verbindung mit dem MCP-Server  
- **Einen MCP Client erstellt**: der die Kommunikation mit dem Server übernimmt  
- **LangChain4j eingebaute MCP-Unterstützung genutzt**: die die Integration zwischen LLMs und MCP-Servern vereinfacht  

#### Rust

Dieses Beispiel geht davon aus, dass du einen Rust-basierten MCP-Server laufen hast. Falls du noch keinen hast, siehe die Lektion [01-first-server](../01-first-server/README.md), um den Server zu erstellen.

Sobald dein Rust MCP-Server bereit ist, öffne ein Terminal und navigiere in dasselbe Verzeichnis wie der Server. Führe dann folgenden Befehl aus, um ein neues LLM Client-Projekt zu erstellen:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```
  
Füge folgende Abhängigkeiten zu deiner `Cargo.toml` Datei hinzu:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```
  
> [!NOTE]  
> Es gibt keine offizielle Rust-Bibliothek für OpenAI, jedoch ist das `async-openai` Crate eine [community-gepflegte Bibliothek](https://platform.openai.com/docs/libraries/rust#rust), die häufig verwendet wird.

Öffne die Datei `src/main.rs` und ersetze ihren Inhalt mit folgendem Code:

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
> Stelle sicher, dass du die Umgebungsvariable `OPENAI_API_KEY` mit deinem GitHub-Token setzt, bevor du die Anwendung startest.

Super, als nächstes listen wir die Fähigkeiten auf dem Server auf.

### -2- Fähigkeiten des Servers auflisten

Jetzt verbinden wir uns mit dem Server und fragen nach dessen Fähigkeiten:

#### Typescript

Füge in derselben Klasse folgende Methoden hinzu:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // Auflisten von Werkzeugen
    const toolsResult = await this.client.listTools();
}
```
  
Im obigen Code haben wir:

- Code zum Verbinden mit dem Server `connectToServer` hinzugefügt.  
- Eine Methode `run` erstellt, die für unseren App-Ablauf zuständig ist. Bisher listet sie nur die Tools, aber wir werden bald mehr hinzufügen.

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

- Ressourcen und Tools aufgelistet und ausgegeben. Für Tools listen wir auch das `inputSchema` auf, welches wir später verwenden.

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
  
Im obigen Code haben wir:

- Die auf dem MCP-Server verfügbaren Tools aufgelistet  
- Für jedes Tool Name, Beschreibung und dessen Schema ausgegeben. Letzteres werden wir gleich zum Aufruf der Tools verwenden.

#### Java

```java
// Erstelle einen Tool-Anbieter, der MCP-Werkzeuge automatisch entdeckt
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Der MCP-Tool-Anbieter verwaltet automatisch:
// - Auflisten verfügbarer Werkzeuge vom MCP-Server
// - Konvertieren von MCP-Werkzeug-Schemata in das LangChain4j-Format
// - Verwaltung der WerkzeugaAusführung und Antworten
```
  
Im obigen Code haben wir:

- Einen `McpToolProvider` erstellt, der automatisch alle Tools vom MCP-Server findet und registriert  
- Der Tool-Provider konvertiert intern das MCP Tool-Schema in das LangChain4j Tool-Format  
- Dieser Ansatz abstrahiert das manuelle Auflisten und Konvertieren der Tools

#### Rust

Das Abrufen der Tools vom MCP-Server erfolgt mit der Methode `list_tools`. Füge in deiner `main` Funktion nach dem Einrichten des MCP-Clients folgendes hinzu:

```rust
// MCP-Werkzeugauflistung abrufen
let tools = mcp_client.list_tools(Default::default()).await?;
```
  
### -3- Server-Fähigkeiten in LLM-Tools umwandeln

Der nächste Schritt nach dem Auflisten der Server-Fähigkeiten ist, sie in ein Format umzuwandeln, das das LLM versteht. Nachdem wir das getan haben, können wir diese Fähigkeiten als Tools unserem LLM bereitstellen.

#### TypeScript

1. Füge folgenden Code hinzu, um die Antwort vom MCP-Server in ein Tool-Format umzuwandeln, das das LLM nutzen kann:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Erstelle ein Zod-Schema basierend auf dem input_schema
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
  
    Der obige Code nimmt eine Antwort vom MCP Server und wandelt diese in ein Tool-Definitionsformat um, das das LLM versteht.

1. Aktualisieren wir als nächstes die `run` Methode, um die Server-Fähigkeiten aufzulisten:

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
  
    Im obigen Code haben wir die `run` Methode aktualisiert, um durch das Ergebnis zu iterieren und für jeden Eintrag die Funktion `openAiToolAdapter` aufzurufen.

#### Python

1. Erstellen wir zuerst die folgende Konvertierungsfunktion:

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
  
    In der Funktion `convert_to_llm_tools` nehmen wir eine MCP Tool-Antwort und wandeln sie in ein Format um, das das LLM verstehen kann.

1. Aktualisieren wir danach unseren Client-Code, um diese Funktion zu nutzen:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```
  
    Hier fügen wir einen Aufruf zu `convert_to_llm_tool` hinzu, um die MCP Tool-Antwort in etwas umzuwandeln, das wir später dem LLM übergeben können.

#### .NET

1. Fügen wir Code hinzu, um die MCP Tool-Antwort in etwas umzuwandeln, das das LLM versteht:

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
  
Im obigen Code haben wir:

- Eine Funktion `ConvertFrom` erstellt, die Name, Beschreibung und Input-Schema entgegennimmt.  
- Funktionalität definiert, die ein `FunctionDefinition` erzeugt, welches an eine `ChatCompletionsDefinition` übergeben wird. Letzteres versteht das LLM.

1. Sehen wir uns an, wie wir vorhandenen Code aktualisieren können, um die Funktion zu nutzen:

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

// Konfigurieren Sie den KI-Dienst mit LLM- und MCP-Tools
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```
  
Im obigen Code haben wir:

- Ein einfaches `Bot` Interface für natürliche Sprachinteraktionen definiert  
- LangChain4j's `AiServices` verwendet, um das LLM automatisch mit dem MCP Tool Provider zu verbinden  
- Das Framework konvertiert automatisch Tool-Schemata und Funktionen im Hintergrund  
- Dadurch entfällt die manuelle Tool-Umwandlung – LangChain4j übernimmt die komplexe Konvertierung von MCP-Tools in ein LLM-kompatibles Format  

#### Rust

Um die MCP Tool-Antwort in ein LLM-verstehbares Format zu konvertieren, fügen wir eine Hilfsfunktion hinzu, die die Tool-Liste formatiert. Füge folgenden Code in deine `main.rs` Datei unterhalb der `main` Funktion ein. Diese wird bei Anfragen an das LLM aufgerufen:

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
  
Super, wir sind bereit, um Nutzeranfragen zu bearbeiten, also lass uns das als nächstes machen.

### -4- Nutzeranfrage bearbeiten

In diesem Codeteil kümmern wir uns um Nutzeranfragen.

#### TypeScript

1. Füge eine Methode hinzu, die unseren LLM aufruft:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Rufen Sie das Werkzeug des Servers auf
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Machen Sie etwas mit dem Ergebnis
        // NOCH ZU ERLEDIGEN

        }
    }
    ```
  
    Im obigen Code haben wir:

    - Eine Methode `callTools` hinzugefügt.  
    - Die Methode nimmt eine LLM-Antwort und prüft, welche Tools aufgerufen wurden, falls vorhanden:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // Werkzeug aufrufen
        }
        ```
  
    - Ruft ein Tool auf, falls das LLM angibt, dass es aufgerufen werden soll:

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
  
1. Aktualisiere die `run` Methode, um LLM-Aufrufe und `callTools` zu integrieren:

    ```typescript

    // 1. Erstellen Sie Nachrichten, die als Eingabe für das LLM dienen
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

    // 3. Gehen Sie die LLM-Antwort durch, überprüfen Sie bei jeder Auswahl, ob Werkzeugaufrufe vorhanden sind
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```
  
Super, hier der vollständige Code:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importiere zod für die Schemavalidierung

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // Möglicherweise muss in Zukunft auf diese URL geändert werden: https://models.github.ai/inference
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
            type: "function" as const, // Typ explizit auf "function" setzen
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
    
        // 1. Gehe die LLM-Antwort durch, prüfe für jede Auswahl, ob Tool-Aufrufe vorhanden sind
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

1. Fügen wir benötigte Importe hinzu, um ein LLM aufzurufen:

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```
  
1. Dann die Funktion, die das LLM aufruft:

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
  
    Im obigen Code haben wir:

    - Unsere Funktionen, die wir auf dem MCP Server gefunden und konvertiert haben, an das LLM übergeben  
    - Das LLM mit diesen Funktionen aufgerufen  
    - Das Ergebnis untersucht, um zu sehen, welche Funktionen ggf. aufgerufen werden sollen  
    - Am Ende ein Array von Funktionen übergeben, die aufzurufen sind  

1. Als letzten Schritt aktualisieren wir unseren Hauptcode:

    ```python
    prompt = "Add 2 to 20"

    # frage LLM, welche Werkzeuge, falls vorhanden, zu verwenden sind
    functions_to_call = call_llm(prompt, functions)

    # vorgeschlagene Funktionen aufrufen
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```
  
    Das war der letzte Schritt. Im obigen Code:

    - Rufen wir ein MCP-Tool via `call_tool` auf, mit einer Funktion, die das LLM aufgrund des Nutzerprompts als notwendig erachtete  
    - Geben das Ergebnis des Tool-Aufrufs auf dem MCP-Server aus  

#### .NET

1. Zeigen wir Code zum Durchführen einer LLM-Prompt-Anfrage:

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
  
    Im obigen Code haben wir:

    - Tools vom MCP-Server abgerufen, `var tools = await GetMcpTools()`  
    - Einen Nutzer-Prompt `userMessage` definiert  
    - Ein Optionsobjekt mit Modell und Tools erstellt  
    - Eine Anfrage an das LLM gestellt  

1. Zum Schluss prüfen wir, ob das LLM eine Funktion aufrufen möchte:

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
  
    Im obigen Code haben wir:

    - Eine Liste von Funktionsaufrufen durchlaufen  
    - Für jeden Tool-Aufruf den Namen und die Argumente geparst und das Tool über den MCP-Client aufgerufen. Schließlich geben wir die Resultate aus.

Hier der vollständige Code:

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
    // Führen Sie natürliche Sprachanforderungen aus, die automatisch MCP-Tools verwenden
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
  
Im obigen Code haben wir:

- Einfache natürliche Sprach-Prompts genutzt, um mit den MCP Server Tools zu interagieren  
- Das LangChain4j Framework übernimmt automatisch:  
  - Die Umwandlung von Nutzer-Prompts in Tool-Anrufe, wenn nötig  
  - Den Aufruf der passenden MCP Tools anhand der LLM-Entscheidung  
  - Das Management des Gesprächsflusses zwischen LLM und MCP Server  
- Die Methode `bot.chat()` liefert Antworten in natürlicher Sprache, die ggf. Ergebnisse von MCP Tool-Ausführungen enthalten  
- Dieser Ansatz bietet eine nahtlose Nutzererfahrung, bei der Nutzer nichts über die zugrundeliegende MCP-Implementierung wissen müssen  

Vollständiges Code-Beispiel:

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

Hier passiert der Großteil der Arbeit. Wir rufen das LLM mit dem initialen Nutzer-Prompt auf, verarbeiten die Antwort, um zu prüfen, ob Tools aufgerufen werden müssen. Falls ja, rufen wir diese Tools auf und führen die Konversation mit dem LLM fort, bis keine weiteren Tool-Aufrufe notwendig sind und wir eine finale Antwort haben.

Wir werden mehrere Aufrufe an das LLM machen, also definieren wir eine Funktion, die den LLM-Aufruf übernimmt. Füge folgende Funktion deiner `main.rs` Datei hinzu:

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
  
Diese Funktion nimmt den LLM-Client, eine Liste von Nachrichten (inklusive Nutzer-Prompt), Tools vom MCP-Server und sendet eine Anfrage an das LLM, wobei die Antwort zurückgegeben wird.
Die Antwort von LLM enthält ein Array von `choices`. Wir müssen das Ergebnis verarbeiten, um zu sehen, ob `tool_calls` vorhanden sind. So wissen wir, dass LLM anfordert, ein bestimmtes Tool mit Argumenten aufzurufen. Fügen Sie den folgenden Code am Ende Ihrer Datei `main.rs` hinzu, um eine Funktion zu definieren, die die LLM-Antwort verarbeitet:

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

    // Inhalt drucken, falls verfügbar
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Werkzeugaufrufe behandeln
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Assistentenmeldung hinzufügen

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

        // Unterhaltung mit Werkzeugergebnissen fortsetzen
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

Wenn `tool_calls` vorhanden sind, werden die Tool-Informationen extrahiert, der MCP-Server mit der Tool-Anfrage aufgerufen und die Ergebnisse zu den Konversationsnachrichten hinzugefügt. Dann wird die Konversation mit dem LLM fortgesetzt und die Nachrichten werden mit der Antwort des Assistenten und den Tool-Aufrufergebnissen aktualisiert.

Um die Tool-Aufrufinformationen zu extrahieren, die LLM für MCP-Aufrufe zurückgibt, fügen wir eine weitere Hilfsfunktion hinzu, die alles extrahiert, was für den Aufruf benötigt wird. Fügen Sie den folgenden Code am Ende Ihrer Datei `main.rs` hinzu:

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

Mit allen Bausteinen an Ort und Stelle können wir nun die ursprüngliche Benutzeranfrage verarbeiten und das LLM aufrufen. Aktualisieren Sie Ihre `main`-Funktion und fügen Sie den folgenden Code hinzu:

```rust
// LLM-Konversation mit Werkzeugaufrufen
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

Dies fragt das LLM mit der ursprünglichen Benutzeranfrage nach der Summe von zwei Zahlen ab und verarbeitet die Antwort, um Tool-Aufrufe dynamisch zu handhaben.

Gut gemacht!

## Aufgabe

Nehmen Sie den Code aus der Übung und bauen Sie den Server mit weiteren Tools aus. Erstellen Sie dann einen Client mit einem LLM, wie in der Übung, und testen Sie verschiedene Abfragen, um sicherzustellen, dass alle Ihre Servertools dynamisch aufgerufen werden. Diese Art, einen Client zu erstellen, sorgt für ein großartiges Benutzererlebnis, da die Endbenutzer Abfragen verwenden können anstelle exakter Client-Befehle und nichts von einem MCP-Server-Aufruf mitbekommen.

## Lösung

[Lösung](./solution/README.md)

## Wichtige Erkenntnisse

- Die Integration eines LLM in Ihren Client bietet einen besseren Weg für Benutzer, mit MCP-Servern zu interagieren.
- Sie müssen die MCP-Server-Antwort in etwas umwandeln, das das LLM verstehen kann.

## Beispiele

- [Java Rechner](../samples/java/calculator/README.md)
- [.Net Rechner](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Rechner](../samples/javascript/README.md)
- [TypeScript Rechner](../samples/typescript/README.md)
- [Python Rechner](../../../../03-GettingStarted/samples/python)
- [Rust Rechner](../../../../03-GettingStarted/samples/rust)

## Weitere Ressourcen

## Wie geht es weiter

- Nächstes Thema: [Verwendung eines Servers mit Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir nach Genauigkeit streben, möchten wir darauf hinweisen, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->