# Erstellen eines Clients mit LLM

> [!NOTE]
> Die Beispiele für Java-Clients verbinden sich über das Legacy HTTP+SSE-Transportprotokoll und
> zielen auf MCP `2025-11-25` SDK-APIs ab. Verwenden Sie ein `2026-07-28` kompatibles SDK und
> Streamable HTTP für neue Remote-Clients.

Bisher haben Sie gesehen, wie man einen Server und einen Client erstellt. Der Client konnte den Server explizit aufrufen, um dessen Werkzeuge, Ressourcen und Prompts aufzulisten. Dies ist jedoch kein sehr praktischer Ansatz. Ihre Nutzer leben im agentischen Zeitalter und erwarten, Prompts zu verwenden und mit einem LLM zu kommunizieren. Es ist ihnen egal, ob Sie MCP verwenden, um Ihre Fähigkeiten zu speichern; sie erwarten einfach, mit natürlicher Sprache zu interagieren. Wie lösen wir das? Die Lösung besteht darin, dem Client ein LLM hinzuzufügen.

## Überblick

In dieser Lektion konzentrieren wir uns darauf, dem Client ein LLM hinzuzufügen und zeigen, wie dies eine viel bessere Erfahrung für den Nutzer bietet.

## Lernziele

Am Ende dieser Lektion können Sie:

- Einen Client mit einem LLM erstellen.
- Nahtlos mit einem MCP-Server unter Verwendung eines LLM interagieren.
- Eine bessere Endnutzererfahrung auf der Client-Seite bieten.

## Vorgehensweise

Versuchen wir zu verstehen, welchen Ansatz wir verfolgen müssen. Ein LLM hinzuzufügen klingt einfach, aber werden wir das tatsächlich tun?

So wird der Client mit dem Server interagieren:

1. Verbindung mit dem Server herstellen.

1. Fähigkeiten, Prompts, Ressourcen und Werkzeuge auflisten und deren Schema speichern.

1. Ein LLM hinzufügen und die gespeicherten Fähigkeiten samt Schema in einem für das LLM verständlichen Format übergeben.

1. Einen Nutzerprompt verarbeiten, indem dieser zusammen mit den vom Client aufgelisteten Werkzeugen an das LLM übergeben wird.

Gut, nun verstehen wir auf hoher Ebene, wie wir das machen können. Probieren wir dies im folgenden Abschnitt aus.

## Übung: Erstellen eines Clients mit einem LLM

In dieser Übung lernen wir, ein LLM zu unserem Client hinzuzufügen.

### Authentifizierung mit GitHub Personal Access Token

Das Erstellen eines GitHub-Tokens ist ein unkomplizierter Prozess. So geht’s:

- Gehen Sie zu GitHub Einstellungen – Klicken Sie auf Ihr Profilbild oben rechts und wählen Sie Einstellungen.
- Navigieren Sie zu Entwickler-Einstellungen – Scrollen Sie nach unten und klicken Sie auf Entwickler-Einstellungen.
- Wählen Sie Personal Access Tokens – Klicken Sie auf Fein granulierte Tokens und dann Neuen Token erstellen.
- Konfigurieren Sie Ihren Token – Fügen Sie eine Notiz zur Referenz hinzu, setzen Sie ein Ablaufdatum und wählen Sie die erforderlichen Berechtigungen aus. Stellen Sie sicher, dass Sie die Models-Berechtigung hinzufügen.
- Generieren und kopieren Sie den Token – Klicken Sie auf Token generieren und kopieren Sie ihn sofort, da Sie ihn später nicht mehr sehen können.

### -1- Mit Server verbinden

Erstellen wir zuerst unseren Client:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Zod für Schema-Validierung importieren

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
- Eine Klasse mit zwei Mitgliedern erstellt, `client` und `openai`, welche uns helfen, einen Client zu verwalten und mit einem LLM zu interagieren.
- Die LLM-Instanz so konfiguriert, dass GitHub Models verwendet werden, indem `baseUrl` auf die Inference API gesetzt wurde.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Serverparameter für stdio-Verbindung erstellen
server_params = StdioServerParameters(
    command="mcp",  # Ausführbare Datei
    args=["run", "server.py"],  # Optionale Kommandozeilenargumente
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

Zuerst müssen Sie die LangChain4j-Abhängigkeiten zu Ihrer `pom.xml`-Datei hinzufügen. Fügen Sie diese Abhängigkeiten hinzu, um die MCP-Integration und die OpenAI-kompatible MiniMax-API zu ermöglichen:

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
    
    <!-- Spring Boot Starter (optional, for production apps) -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>
</dependencies>
```

Setzen Sie Ihren MiniMax API-Schlüssel und optional den Endpunkt und das Modell.
`MINIMAX_MODEL_ID` unterstützt `MiniMax-M3` und `MiniMax-M2.7`. Wenn
`OPENAI_BASE_URL` nicht gesetzt ist, unterstützt `MINIMAX_REGION` `global_en` und `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Um stattdessen den Endpunkt nach Region auszuwählen, lassen Sie `OPENAI_BASE_URL` weg:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
                .build();

        // Erstelle MCP-Transport zum Verbinden mit dem Server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Erstelle MCP-Client
        McpClient mcpClient = new DefaultMcpClient.Builder()
                .transport(transport)
                .build();
    }

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

Im obigen Code haben wir:

- **LangChain4j-Abhängigkeiten hinzugefügt**: Erforderlich für die MCP-Integration und die OpenAI-kompatible MiniMax-API
- **Die LangChain4j-Bibliotheken importiert**: Für MCP-Integration und OpenAI-Chatmodell-Funktionalität
- **Ein `ChatLanguageModel` erstellt**: Konfiguriert, um MiniMax mit Ihrem MiniMax-API-Schlüssel, Endpunkt und unterstützter Modell-ID zu verwenden
- **HTTP-Transport eingerichtet**: Verwendung von Server-Sent Events (SSE) zur Verbindung mit dem MCP-Server
- **Einen MCP-Client erstellt**: Der die Kommunikation mit dem Server übernimmt
- **Die eingebaute MCP-Unterstützung von LangChain4j genutzt**: Dies erleichtert die Integration zwischen LLMs und MCP-Servern

#### Rust

Dieses Beispiel geht davon aus, dass Sie einen Rust-basierten MCP-Server laufen haben. Falls nicht, sehen Sie bitte in der Lektion [01-first-server](../01-first-server/README.md) nach, um den Server zu erstellen.

Sobald Sie Ihren Rust-MCP-Server haben, öffnen Sie ein Terminal und navigieren Sie in das gleiche Verzeichnis wie der Server. Führen Sie dann folgenden Befehl aus, um ein neues LLM-Client-Projekt zu erstellen:

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
> Es gibt keine offizielle Rust-Bibliothek für OpenAI, aber die `async-openai`-Crate ist eine von der Community gepflegte Bibliothek, die häufig verwendet wird.

Öffnen Sie die Datei `src/main.rs` und ersetzen Sie deren Inhalt durch folgenden Code:

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

    // Einrichten des OpenAI-Clients
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Einrichten des MCP-Clients
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

Dieser Code richtet eine grundlegende Rust-Anwendung ein, die sich mit einem MCP-Server und GitHub Models zur LLM-Interaktion verbindet.

> [!IMPORTANT]
> Stellen Sie sicher, dass die Umgebungsvariable `OPENAI_API_KEY` mit Ihrem GitHub-Token gesetzt ist, bevor Sie die Anwendung ausführen.

Gut, als nächsten Schritt listen wir die Fähigkeiten auf dem Server auf.

### -2- Serverfähigkeiten auflisten

Nun verbinden wir uns mit dem Server und fragen nach seinen Fähigkeiten:

#### Typescript

Fügen Sie in derselben Klasse folgende Methoden hinzu:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // Werkzeuge auflisten
    const toolsResult = await this.client.listTools();
}
```

Im obigen Code haben wir:

- Code zum Verbinden mit dem Server hinzugefügt, `connectToServer`.
- Eine Methode `run` erstellt, die für den Ablauf unserer App verantwortlich ist. Bis jetzt listet sie nur die Werkzeuge auf, aber wir werden bald mehr hinzufügen.

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

Folgendes haben wir ergänzt:

- Ressourcen und Werkzeuge aufgelistet und ausgegeben. Für Werkzeuge listen wir auch das `inputSchema` auf, das wir später verwenden.

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


Im vorherigen Code haben wir:

- Die auf dem MCP Server verfügbaren Tools aufgelistet
- Für jedes Tool Name, Beschreibung und dessen Schema aufgelistet. Letzteres werden wir bald nutzen, um die Tools aufzurufen.

#### Java

```java
// Erstellen Sie einen Tool-Anbieter, der MCP-Tools automatisch entdeckt
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Der MCP-Tool-Anbieter verwaltet automatisch:
// - Auflisten verfügbarer Tools vom MCP-Server
// - Konvertieren von MCP-Tool-Schemas in das LangChain4j-Format
// - Verwaltung der Tool-Ausführung und -Antworten
```

Im vorherigen Code haben wir:

- Einen `McpToolProvider` erstellt, der automatisch alle Tools vom MCP Server entdeckt und registriert
- Der Tool-Provider konvertiert intern zwischen MCP Tool-Schemata und LangChain4j's Tool-Format
- Dieser Ansatz abstrahiert die manuelle Auflistung und Konvertierung der Tools

#### Rust

Die Werkzeuge vom MCP Server werden über die Methode `list_tools` abgerufen. Fügen Sie in Ihrer `main` Funktion nach der Einrichtung des MCP-Clients den folgenden Code hinzu:

```rust
// MCP-Werkzeugauflistung abrufen
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Server-Fähigkeiten in LLM-Tools umwandeln

Der nächste Schritt nach der Auflistung der Server-Fähigkeiten besteht darin, diese in ein Format umzuwandeln, das das LLM versteht. Sobald wir das tun, können wir diese Fähigkeiten dem LLM als Werkzeuge bereitstellen.

#### TypeScript

1. Fügen Sie den folgenden Code hinzu, um die Antwort vom MCP Server in ein Tool-Format zu konvertieren, das das LLM verwenden kann:

    ```typescript
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

    ```

    Der obige Code nimmt eine Antwort vom MCP Server und konvertiert sie in ein Tool-Definitionsformat, das das LLM verstehen kann.

2. Als nächstes aktualisieren wir die `run`-Methode, um die Server-Fähigkeiten aufzulisten:

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

    Im vorangegangenen Code haben wir die `run`-Methode aktualisiert, um das Ergebnis zu mappen und für jeden Eintrag `openAiToolAdapter` aufzurufen.

#### Python

1. Zuerst erstellen wir folgende Konverterfunktion

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

    In der Funktion `convert_to_llm_tools` oben nehmen wir eine MCP Tool-Antwort und konvertieren sie in ein Format, das das LLM verstehen kann.

2. Als nächstes aktualisieren wir unseren Client-Code, um diese Funktion wie folgt zu nutzen:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Hier fügen wir einen Aufruf zu `convert_to_llm_tool` hinzu, um die MCP Tool-Antwort in etwas zu konvertieren, das wir später dem LLM einspeisen können.

#### .NET

1. Fügen wir Code hinzu, um die MCP Tool-Antwort in etwas umzuwandeln, das das LLM verstehen kann

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

Im vorherigen Code haben wir:

- Eine Funktion `ConvertFrom` erstellt, die Name, Beschreibung und Input-Schema entgegennimmt.
- Funktionalität definiert, die eine FunctionDefinition erzeugt, die an eine ChatCompletionsDefinition übergeben wird. Letztere versteht das LLM.

2. Sehen wir uns an, wie wir bestehenden Code aktualisieren können, um diese Funktion oben zu nutzen:

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

Im vorherigen Code haben wir:

- Ein einfaches `Bot` Interface für Interaktionen in natürlicher Sprache definiert
- LangChain4j's `AiServices` verwendet, um das LLM automatisch mit dem MCP Tool-Provider zu verbinden
- Das Framework übernimmt automatisch die Konvertierung von Tool-Schemata und Funktionsaufrufen im Hintergrund
- Dieser Ansatz eliminiert manuelle Tool-Konvertierungen – LangChain4j übernimmt die gesamte Komplexität der Umwandlung von MCP-Tools in ein LLM-kompatibles Format

#### Rust

Um die MCP Tool-Antwort in ein Format zu konvertieren, das das LLM verstehen kann, fügen wir eine Hilfsfunktion hinzu, die die Tool-Auflistung formatiert. Fügen Sie den folgenden Code in Ihre `main.rs` Datei unterhalb der `main` Funktion ein. Dies wird aufgerufen, wenn Anfragen an das LLM gesendet werden:

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

Super, wir sind jetzt bereit, Benutzeranfragen zu bearbeiten, kümmern wir uns als Nächstes darum.

### -4- Benutzeranfragen bearbeiten

In diesem Teil des Codes werden wir Benutzeranfragen bearbeiten.

#### TypeScript

1. Fügen Sie eine Methode hinzu, mit der unser LLM aufgerufen wird:

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

        // 3. Mach etwas mit dem Ergebnis
        // TODO

        }
    }
    ```

    Im vorherigen Code haben wir:

    - Eine Methode `callTools` hinzugefügt.
    - Die Methode nimmt eine LLM-Antwort und prüft, ob Werkzeuge aufgerufen wurden, falls ja:

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

2. Aktualisieren Sie die `run`-Methode, um Aufrufe an das LLM und `callTools` einzubeziehen:

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

    // 3. Gehen Sie die LLM-Antwort durch, überprüfen Sie für jede Auswahl, ob sie Werkzeugaufrufe enthält
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
import { z } from "zod"; // Importiere zod für die Schema-Validierung

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
    
    
          // 2. Rufe das Werkzeug des Servers auf
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Mach etwas mit dem Ergebnis
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
    
        // 3. Gehe die LLM-Antwort durch, überprüfe für jede Auswahl, ob Werkzeugaufrufe vorhanden sind
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

1. Fügen wir einige Importe hinzu, die für den Aufruf des LLM nötig sind

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Als nächstes fügen wir die Funktion hinzu, die das LLM aufruft:

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

    Im vorherigen Code haben wir:

    - Unsere Funktionen, die wir auf dem MCP Server gefunden und konvertiert haben, an das LLM übergeben.
    - Das LLM mit diesen Funktionen aufgerufen.
    - Dann das Ergebnis geprüft, um zu sehen, welche Funktionen gegebenenfalls aufgerufen werden sollen.
    - Schließlich ein Array von Funktionen zum Aufrufen übergeben.

3. Abschließend aktualisieren wir unseren Hauptcode:

    ```python
    prompt = "Add 2 to 20"

    # frage das LLM, welche Werkzeuge es verwenden soll, falls überhaupt
    functions_to_call = call_llm(prompt, functions)

    # rufe vorgeschlagene Funktionen auf
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Das war der letzte Schritt, im obigen Code:

    - Rufen wir ein MCP Tool über `call_tool` auf, das basierend auf unserer Eingabeaufforderung vom LLM als aufzurufen erkannt wurde.
    - Geben das Ergebnis des Tool-Aufrufs zum MCP Server aus.

#### .NET

1. Hier etwas Code zum Ausführen einer LLM Prompt-Anfrage:

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

    Im vorherigen Code haben wir:

    - Werkzeuge vom MCP Server abgefragt, `var tools = await GetMcpTools()`.
    - Eine Benutzeraufforderung `userMessage` definiert.
    - Ein Optionsobjekt konstruiert, in dem Modell und Tools spezifiziert sind.
    - Eine Anfrage an das LLM gestellt.

2. Ein letzter Schritt, prüfen wir, ob das LLM meint, eine Funktion aufrufen zu sollen:

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

    Im vorherigen Code haben wir:

    - Über eine Liste von Funktionsaufrufen iteriert.
    - Für jeden Tool-Aufruf Namen und Argumente ausgepackt und das Tool auf dem MCP Server mit dem MCP-Client aufgerufen. Zum Schluss die Ergebnisse ausgegeben.

Hier ist der komplette Code:

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

// 6. Print the generic response
Console.WriteLine($"Assistant response: {content}");
```

#### Java

```java
try {
    // Führen Sie Anfragen in natürlicher Sprache aus, die automatisch MCP-Werkzeuge verwenden
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

Im vorherigen Code haben wir:

- Einfache natürliche Sprachaufforderungen verwendet, um mit den MCP Server-Tools zu interagieren
- Das LangChain4j-Framework übernimmt automatisch:
  - Die Umwandlung von Benutzereingaben in Tool-Aufrufe bei Bedarf
  - Den Aufruf der passenden MCP Tools basierend auf der Entscheidung des LLM
  - Das Management des Gesprächsflusses zwischen LLM und MCP Server
- Die Methode `bot.chat()` gibt Antworten in natürlicher Sprache zurück, die mögliche Ergebnisse von MCP Tool-Ausführungen beinhalten
- Dieser Ansatz bietet ein nahtloses Benutzererlebnis, bei dem die Nutzer nichts über die zugrundeliegende MCP-Implementierung wissen müssen

Vollständiges Codebeispiel:

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
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class LangChain4jClient {

    private static final String DEFAULT_BASE_URL = "https://api.minimax.io/v1";
    private static final String DEFAULT_MODEL_ID = "MiniMax-M3";
    private static final Map<String, String> REGIONAL_BASE_URLS = Map.of(
            "global_en", "https://api.minimax.io/v1",
            "cn_zh", "https://api.minimaxi.com/v1");
    private static final Set<String> SUPPORTED_MODEL_IDS = Set.of("MiniMax-M3", "MiniMax-M2.7");

    public static void main(String[] args) throws Exception {
        ChatLanguageModel model = OpenAiOfficialChatModel.builder()
                .baseUrl(resolveBaseUrl())
                .apiKey(requireEnv("OPENAI_API_KEY"))
                .timeout(Duration.ofSeconds(60))
                .modelName(resolveModelName())
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

    private static String resolveBaseUrl() {
        String baseUrl = System.getenv("OPENAI_BASE_URL");
        if (baseUrl != null && !baseUrl.isBlank()) {
            return baseUrl;
        }

        String region = System.getenv("MINIMAX_REGION");
        if (region == null || region.isBlank()) {
            return DEFAULT_BASE_URL;
        }

        String regionalBaseUrl = REGIONAL_BASE_URLS.get(region);
        if (regionalBaseUrl == null) {
            throw new IllegalArgumentException("Unsupported MINIMAX_REGION value: " + region
                    + ". Supported values: " + new TreeSet<>(REGIONAL_BASE_URLS.keySet()));
        }
        return regionalBaseUrl;
    }

    private static String resolveModelName() {
        String modelId = System.getenv("MINIMAX_MODEL_ID");
        if (modelId == null || modelId.isBlank()) {
            return DEFAULT_MODEL_ID;
        }
        if (!SUPPORTED_MODEL_IDS.contains(modelId)) {
            throw new IllegalArgumentException("Unsupported MINIMAX_MODEL_ID value: " + modelId
                    + ". Supported values: " + new TreeSet<>(SUPPORTED_MODEL_IDS));
        }
        return modelId;
    }

    private static String requireEnv(String name) {
        String value = System.getenv(name);
        if (value == null || value.isBlank()) {
            throw new IllegalStateException(name + " environment variable is not set");
        }
        return value;
    }
}
```

#### Rust


Hier findet der Großteil der Arbeit statt. Wir rufen das LLM mit der anfänglichen Nutzereingabe auf und verarbeiten dann die Antwort, um zu sehen, ob Werkzeuge aufgerufen werden müssen. Wenn ja, rufen wir diese Werkzeuge auf und führen die Unterhaltung mit dem LLM fort, bis keine weiteren Werkzeugaufrufe mehr benötigt werden und wir eine endgültige Antwort haben.

Wir werden mehrere Aufrufe an das LLM machen, also definieren wir eine Funktion, die den LLM-Aufruf übernimmt. Fügen Sie die folgende Funktion zu Ihrer `main.rs`-Datei hinzu:

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

Diese Funktion nimmt den LLM-Client, eine Liste von Nachrichten (einschließlich der Nutzereingabe), Werkzeuge vom MCP-Server entgegen und sendet eine Anfrage an das LLM, die Antwort wird zurückgegeben.

Die Antwort des LLM enthält ein Array von `choices`. Wir müssen das Ergebnis verarbeiten, um zu sehen, ob `tool_calls` vorhanden sind. Das zeigt uns, dass das LLM den Aufruf eines bestimmten Werkzeugs mit Argumenten verlangt. Fügen Sie den folgenden Code am Ende Ihrer `main.rs`-Datei hinzu, um eine Funktion zur Verarbeitung der LLM-Antwort zu definieren:

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

    // Inhalt ausdrucken, wenn verfügbar
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Tool-Aufrufe behandeln
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Assistentenmeldung hinzufügen

        // Jeden Tool-Aufruf ausführen
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Tool-Ergebnis zu Nachrichten hinzufügen
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Konversation mit Tool-Ergebnissen fortsetzen
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

Wenn `tool_calls` vorhanden sind, werden die Werkzeug-Informationen extrahiert, der MCP-Server mit der Werkzeuganfrage aufgerufen und die Ergebnisse zu den Konversationsnachrichten hinzugefügt. Dann wird die Unterhaltung mit dem LLM fortgesetzt und die Nachrichten werden mit der Antwort des Assistenten und den Ergebnissen des Werkzeugaufrufs aktualisiert.

Um die Werkzeugaufrufinformationen zu extrahieren, die das LLM für MCP-Aufrufe zurückgibt, fügen wir eine weitere Hilfsfunktion hinzu, die alles Nötige für den Aufruf extrahiert. Fügen Sie den folgenden Code am Ende Ihrer `main.rs`-Datei hinzu:

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

Mit allen Bausteinen können wir jetzt die anfängliche Nutzereingabe verarbeiten und das LLM aufrufen. Aktualisieren Sie Ihre `main`-Funktion mit folgendem Code:

```rust
// LLM-Gespräch mit Werkzeugaufrufen
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

Dadurch wird das LLM mit der anfänglichen Nutzereingabe abgefragt, die nach der Summe von zwei Zahlen fragt, und die Antwort wird verarbeitet, um Werkzeugaufrufe dynamisch zu handhaben.

Großartig, Sie haben es geschafft!

## Aufgabe

Nehmen Sie den Code aus der Übung und bauen Sie den Server mit weiteren Werkzeugen aus. Erstellen Sie dann einen Client mit einem LLM, wie in der Übung, und testen Sie ihn mit verschiedenen Eingaben, um sicherzustellen, dass alle Server-Werkzeuge dynamisch aufgerufen werden. Diese Art, einen Client zu bauen, sorgt für eine großartige Benutzererfahrung, da die Nutzer Prompts verwenden können, anstatt exakte Client-Befehle, und nichts von einem MCP-Serveraufruf merken.

## Lösung

[Lösung](./solution/README.md)

## Wichtige Erkenntnisse

- Die Integration eines LLM in Ihren Client bietet den Nutzern eine bessere Interaktionsmöglichkeit mit MCP-Servern.
- Die Antwort des MCP-Servers muss in etwas konvertiert werden, das das LLM verstehen kann.

## Beispiele

- [Java Rechner](../samples/java/calculator/README.md)
- [.Net Rechner](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Rechner](../samples/javascript/README.md)
- [TypeScript Rechner](../samples/typescript/README.md)
- [Python Rechner](../../../../03-GettingStarted/samples/python)
- [Rust Rechner](../../../../03-GettingStarted/samples/rust)

## Zusätzliche Ressourcen

## Was kommt als Nächstes

- Nächstes: [Verbrauch eines Servers mit Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->