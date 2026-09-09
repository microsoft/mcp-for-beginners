# Erstellen eines Clients mit LLM

Bisher haben Sie gesehen, wie man einen Server und einen Client erstellt. Der Client konnte den Server explizit anrufen, um dessen Werkzeuge, Ressourcen und Prompts aufzulisten. Dies ist jedoch kein sehr praktischer Ansatz. Ihre Nutzer leben im Zeitalter der Agenten und erwarten, Prompts zu verwenden und mit einem LLM zu kommunizieren. Es ist ihnen egal, ob Sie MCP zur Speicherung Ihrer Fähigkeiten verwenden; sie erwarten einfach eine Interaktion in natürlicher Sprache. Wie lösen wir das? Die Lösung ist, dem Client ein LLM hinzuzufügen.

## Überblick

In dieser Lektion konzentrieren wir uns darauf, ein LLM zum Client hinzuzufügen und zeigen, wie dies eine viel bessere Erfahrung für Ihre Nutzer bietet.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:

- Einen Client mit einem LLM zu erstellen.
- Nahtlos mit einem MCP-Server mittels eines LLM zu interagieren.
- Eine bessere Endnutzererfahrung auf der Client-Seite zu bieten.

## Vorgehensweise

Lassen Sie uns zunächst den Ansatz verstehen, den wir verfolgen müssen. Ein LLM hinzuzufügen klingt einfach, aber werden wir das tatsächlich so machen?

So wird der Client mit dem Server interagieren:

1. Verbindung mit dem Server herstellen.

1. Fähigkeiten, Prompts, Ressourcen und Werkzeuge auflisten und deren Schema speichern.

1. Ein LLM hinzufügen und die gespeicherten Fähigkeiten und deren Schema in einem Format übergeben, das das LLM versteht.

1. Einen Nutzer-Prompt verarbeiten, indem er zusammen mit den vom Client gelisteten Werkzeugen an das LLM übergeben wird.

Großartig, nun verstehen wir, wie wir dies auf hoher Ebene tun können. Lassen Sie uns dies im folgenden Übungsteil ausprobieren.

## Übung: Erstellen eines Clients mit einem LLM

In dieser Übung lernen wir, wie wir ein LLM zu unserem Client hinzufügen.

### Authentifizierung mit GitHub Personal Access Token

Einen GitHub-Token zu erstellen ist ein einfacher Vorgang. So geht’s:

- Gehen Sie zu GitHub Settings – Klicken Sie oben rechts auf Ihr Profilbild und wählen Sie Einstellungen.
- Navigieren Sie zu Developer Settings – Scrollen Sie nach unten und klicken Sie auf Entwickler-Einstellungen.
- Wählen Sie Personal Access Tokens – Klicken Sie auf Fein abgestimmte Tokens und dann auf Neuen Token erstellen.
- Konfigurieren Sie Ihren Token – Fügen Sie eine Notiz zur Referenz hinzu, setzen Sie ein Ablaufdatum und wählen Sie die notwendigen Berechtigungen (Scopes). In diesem Fall achten Sie darauf, die Models-Berechtigung hinzuzufügen.
- Token generieren und kopieren – Klicken Sie auf Token generieren und kopieren Sie ihn sofort, da Sie ihn später nicht mehr sehen können.

### -1- Verbindung zum Server herstellen

Erstellen wir zuerst unseren Client:

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

Im obigen Code haben wir:

- Die benötigten Bibliotheken importiert
- Eine Klasse mit zwei Mitgliedern, `client` und `openai`, erstellt, die uns helfen, einen Client zu verwalten und jeweils mit einem LLM zu interagieren.
- Unsere LLM-Instanz so konfiguriert, dass GitHub Models verwendet werden, indem `baseUrl` auf die Inference-API gesetzt wird.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Erstelle Serverparameter für die stdio-Verbindung
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
            # Initialisiere die Verbindung
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

Zunächst müssen Sie die LangChain4j-Abhängigkeiten zu Ihrer `pom.xml`-Datei hinzufügen. Fügen Sie diese Abhängigkeiten hinzu, um die MCP-Integration und die OpenAI-kompatible MiniMax-API zu ermöglichen:

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

Setzen Sie Ihren MiniMax-API-Schlüssel und optional den Endpunkt und das Modell.
`MINIMAX_MODEL_ID` unterstützt `MiniMax-M3` und `MiniMax-M2.7`. Falls
`OPENAI_BASE_URL` nicht gesetzt ist, unterstützt `MINIMAX_REGION` `global_en` und `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

Um den Endpunkt stattdessen nach Region auszuwählen, lassen Sie `OPENAI_BASE_URL` weg:

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

        // Erstellen Sie MCP-Transport zur Verbindung mit dem Server
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Erstellen Sie MCP-Client
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

- **LangChain4j-Abhängigkeiten hinzugefügt**: Erforderlich für MCP-Integration und OpenAI-kompatible MiniMax-API
- **Die LangChain4j-Bibliotheken importiert**: Für MCP-Integration und OpenAI-Chat-Modellfunktionalität
- **Ein `ChatLanguageModel` erstellt**: Konfiguriert zur Nutzung von MiniMax mit Ihrem MiniMax-API-Schlüssel, Endpunkt und unterstützt Modell-ID
- **HTTP-Transport eingerichtet**: Über Server-Sent Events (SSE) zur Verbindung mit dem MCP-Server
- **Einen MCP-Client erstellt**: Der die Kommunikation mit dem Server übernimmt
- **Die eingebaute MCP-Unterstützung von LangChain4j genutzt**: Welche die Integration zwischen LLMs und MCP-Servern vereinfacht

#### Rust

Dieses Beispiel setzt voraus, dass Sie einen Rust-basierten MCP-Server haben. Falls nicht, sehen Sie die Lektion [01-first-server](../01-first-server/README.md) für die Erstellung des Servers nach.

Sobald Sie Ihren Rust MCP-Server haben, öffnen Sie ein Terminal und navigieren Sie in dasselbe Verzeichnis wie der Server. Führen Sie dann folgenden Befehl aus, um ein neues LLM-Client-Projekt zu erstellen:

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
> Es gibt keine offizielle Rust-Bibliothek für OpenAI, allerdings ist das `async-openai`-Crate eine [community-gepflegte Bibliothek](https://platform.openai.com/docs/libraries/rust#rust), die häufig verwendet wird.

Öffnen Sie die `src/main.rs`-Datei und ersetzen Sie deren Inhalt durch folgenden Code:

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

Dieser Code richtet eine einfache Rust-Anwendung ein, die sich mit einem MCP-Server und GitHub Models für LLM-Interaktionen verbindet.

> [!IMPORTANT]
> Stellen Sie sicher, dass die Umgebungsvariable `OPENAI_API_KEY` mit Ihrem GitHub-Token vor dem Ausführen der Anwendung gesetzt ist.

Großartig, als nächsten Schritt listen wir die Fähigkeiten auf dem Server auf.

### -2- Serverfähigkeiten auflisten

Jetzt verbinden wir uns mit dem Server und fragen nach seinen Fähigkeiten:

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

    // Auflistung von Werkzeugen
    const toolsResult = await this.client.listTools();
}
```

Im obigen Code haben wir:

- Code für die Verbindung zum Server, `connectToServer`, hinzugefügt.
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

Folgendes haben wir hinzugefügt:

- Ressourcen und Werkzeuge aufgelistet und ausgegeben. Für Werkzeuge listen wir auch `inputSchema`, das später verwendet wird.

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

- Die auf dem MCP-Server verfügbaren Werkzeuge aufgelistet
- Für jedes Werkzeug Name, Beschreibung und dessen Schema aufgelistet. Letzteres werden wir bald zum Aufrufen der Werkzeuge verwenden.

#### Java

```java
// Erstellen Sie einen Tool-Anbieter, der MCP-Tools automatisch entdeckt
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// Der MCP-Tool-Anbieter verwaltet automatisch:
// - Auflisten verfügbarer Tools vom MCP-Server
// - Konvertieren von MCP-Tool-Schemas in das LangChain4j-Format
// - Verwalten der Tool-Ausführung und Antworten
```

Im obigen Code haben wir:

- Einen `McpToolProvider` erstellt, der automatisch alle Werkzeuge vom MCP-Server entdeckt und registriert
- Der Tool-Provider handhabt intern die Umwandlung zwischen MCP-Tool-Schemas und dem Tool-Format von LangChain4j
- Dieser Ansatz abstrahiert den manuellen Prozess des Werkzeug-Auflistens und der Konvertierung

#### Rust

Das Abrufen der Werkzeuge vom MCP-Server erfolgt mittels `list_tools`. Fügen Sie in Ihrer `main`-Funktion nach Einrichtung des MCP-Clients folgenden Code hinzu:

```rust
// MCP Werkzeugauflistung holen
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Serverfähigkeiten in LLM-Werkzeuge umwandeln

Der nächste Schritt nach dem Auflisten der Serverfähigkeiten besteht darin, diese in ein Format zu konvertieren, das das LLM versteht. Sobald wir das getan haben, können wir diese Fähigkeiten als Werkzeuge unserem LLM zur Verfügung stellen.

#### TypeScript

1. Fügen Sie folgenden Code hinzu, um eine Antwort vom MCP-Server in ein Werkzeug-Format zu konvertieren, das das LLM nutzen kann:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Erstellen Sie ein Zod-Schema basierend auf dem input_schema
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

    ```

    Der obige Code nimmt eine Antwort vom MCP-Server und konvertiert diese in ein Werkzeug-Definitionsformat, das das LLM verstehen kann.

2. Aktualisieren wir als nächstes die `run`-Methode, um die Serverfähigkeiten aufzulisten:

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

    Im obigen Code haben wir die `run`-Methode aktualisiert, um das Ergebnis zu durchlaufen und für jeden Eintrag `openAiToolAdapter` aufzurufen.

#### Python

1. Erstellen wir zunächst folgende Konvertierungsfunktion

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

    In der Funktion `convert_to_llm_tools` oben nehmen wir eine MCP-Tool-Antwort und konvertieren sie in ein Format, das das LLM versteht.

2. Aktualisieren wir nun unseren Client-Code, um diese Funktion wie folgt zu verwenden:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Hier rufen wir `convert_to_llm_tool` auf, um die MCP-Tool-Antwort in ein Format umzuwandeln, das wir später an das LLM übergeben können.

#### .NET

1. Fügen wir Code hinzu, um die MCP-Tool-Antwort in etwas zu konvertieren, das das LLM versteht

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

- Eine Funktion `ConvertFrom` erstellt, die Name, Beschreibung und Eingangsschema nimmt.
- Eine Funktionalität definiert, die ein `FunctionDefinition` erzeugt, das an eine `ChatCompletionsDefinition` übergeben wird. Letzteres versteht das LLM.

2. Sehen wir uns an, wie wir vorhandenen Code aktualisieren können, um diese Funktion zu nutzen:

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
// Erstellen Sie eine Bot-Schnittstelle für die Interaktion in natürlicher Sprache
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

- Ein einfaches `Bot`-Interface für natürliche Sprachinteraktionen definiert
- Die `AiServices` von LangChain4j genutzt, um das LLM automatisch mit dem MCP-Toolprovider zu verbinden
- Das Framework übernimmt automatisch die Werkzeug-Schema-Konvertierung und Funktionsaufrufe im Hintergrund
- Dieser Ansatz beseitigt manuelle Werkzeugkonvertierung – LangChain4j übernimmt die gesamte Komplexität der Umwandlung von MCP-Werkzeugen in ein LLM-kompatibles Format

#### Rust

Um die MCP-Tool-Antwort in ein Format zu konvertieren, das das LLM versteht, fügen wir eine Hilfsfunktion hinzu, die die Werkzeugliste formatiert. Fügen Sie folgenden Code unter der `main`-Funktion in Ihrer `main.rs`-Datei hinzu. Diese wird bei Anfragen an das LLM verwendet:

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

Großartig, wir sind bereit, Benutzeranfragen zu bearbeiten, also kümmern wir uns als Nächstes darum.

### -4- Benutzerprompt-Anfrage verarbeiten

In diesem Teil des Codes werden wir Benutzeranfragen bearbeiten.

#### TypeScript

1. Fügen Sie eine Methode hinzu, mit der wir unser LLM aufrufen:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Rufen Sie das Tool des Servers auf
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Machen Sie etwas mit dem Ergebnis
        // TODO

        }
    }
    ```

    Im obigen Code haben wir:

    - Eine Methode `callTools` hinzugefügt.
    - Die Methode nimmt eine LLM-Antwort und überprüft, welche Werkzeuge aufgerufen wurden, falls vorhanden:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // Werkzeug aufrufen
        }
        ```

    - Ruft ein Werkzeug auf, falls das LLM angibt, dass es aufgerufen werden soll:

        ```typescript
        // 2. Rufen Sie das Werkzeug des Servers auf
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Mach etwas mit dem Ergebnis
        // TODO
        ```

2. Aktualisieren Sie die `run`-Methode, um Aufrufe ans LLM und `callTools` einzuschließen:

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

    // 3. Gehe die LLM-Antwort durch, überprüfe für jede Auswahl, ob sie Werkzeugaufrufe enthält
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Großartig, hier der gesamte Code:

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
            baseURL: "https://models.inference.ai.azure.com", // Möglicherweise muss in Zukunft auf diese URL gewechselt werden: https://models.github.ai/inference
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
    
          // 3. Verarbeite das Ergebnis
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
    
        // 3. Gehe die LLM-Antwort durch, prüfe für jede Auswahl, ob Werkzeugaufrufe enthalten sind
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

1. Fügen wir einige notwendige Imports zum Aufrufen eines LLM hinzu

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Als nächstes die Funktion, die das LLM aufruft:

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

    - Unsere Funktionen, die wir auf dem MCP-Server gefunden und konvertiert haben, an das LLM übergeben.
    - Dann das LLM mit diesen Funktionen aufgerufen.
    - Danach das Ergebnis überprüft, um zu sehen, welche Funktionen wir aufrufen sollen, falls vorhanden.
    - Schließlich ein Array von Funktionen zum Aufrufen übergeben.

3. Abschließend aktualisieren wir unseren Hauptcode:

    ```python
    prompt = "Add 2 to 20"

    # frage das LLM, welche Werkzeuge, falls vorhanden, aktiviert werden sollen
    functions_to_call = call_llm(prompt, functions)

    # rufe vorgeschlagene Funktionen auf
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Damit ist der letzte Schritt erledigt, im obigen Code:

    - Rufen wir ein MCP-Werkzeug per `call_tool` mit einer Funktion auf, von der das LLM meinte, wir sollten sie basierend auf unserem Prompt aufrufen.
    - Geben das Ergebnis des Werkzeugaufrufs am MCP-Server aus.

#### .NET

1. Hier ein Beispielcode zum Durchführen einer LLM-Prompt-Anfrage:

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

    - Werkzeuge vom MCP-Server abgefragt, `var tools = await GetMcpTools()`.
    - Einen Nutzerprompt `userMessage` definiert.
    - Ein Optionsobjekt mit Modell und Werkzeugen erstellt.
    - Eine Anfrage an das LLM gesendet.

2. Noch ein Schritt: Sehen wir, ob das LLM einen Funktionsaufruf meint:

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

    - Eine Liste von Funktionsaufrufen durchlaufen.
    - Für jeden Werkzeugaufruf Name und Argumente extrahiert und das Werkzeug am MCP-Server über den MCP-Client aufgerufen. Abschließend die Ergebnisse ausgegeben.

Hier der gesamte Code:

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

Im obigen Code haben wir:

- Einfache Prompts in natürlicher Sprache verwendet, um mit den MCP-Server-Werkzeugen zu interagieren
- Das LangChain4j-Framework übernimmt automatisch:
  - Die Umwandlung von Nutzer-Prompts in Werkzeugaufrufe bei Bedarf
  - Den Aufruf der passenden MCP-Werkzeuge basierend auf der Entscheidung des LLM
  - Die Verwaltung des Gesprächsflusses zwischen LLM und MCP-Server
- Die Methode `bot.chat()` gibt Antworten in natürlicher Sprache zurück, die Ergebnisse von MCP-Werkzeugausführungen enthalten können
- Dieser Ansatz bietet eine nahtlose Nutzererfahrung, bei der die Nutzer nichts von der zugrunde liegenden MCP-Implementierung wissen müssen

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

Hier findet der Großteil der Logik statt. Wir rufen das LLM mit dem initialen Nutzerprompt auf, verarbeiten die Antwort, um zu prüfen, ob Werkzeuge aufgerufen werden müssen. Falls ja, rufen wir diese Werkzeuge auf und setzen das Gespräch mit dem LLM fort, bis keine weiteren Werkzeugaufrufe notwendig sind und wir eine finale Antwort haben.


Wir werden mehrere Anfragen an das LLM stellen, daher definieren wir eine Funktion, die den LLM-Aufruf übernimmt. Fügen Sie die folgende Funktion zu Ihrer `main.rs` Datei hinzu:

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

Diese Funktion nimmt den LLM-Client, eine Liste von Nachrichten (einschließlich der Benutzereingabe), Werkzeuge vom MCP-Server entgegen und sendet eine Anfrage an das LLM, wobei die Antwort zurückgegeben wird.

Die Antwort des LLM enthält ein Array von `choices`. Wir müssen das Ergebnis verarbeiten, um zu überprüfen, ob `tool_calls` vorhanden sind. Dies zeigt uns, dass das LLM anfragt, ein bestimmtes Werkzeug mit Argumenten aufzurufen. Fügen Sie am Ende Ihrer `main.rs` Datei den folgenden Code hinzu, um eine Funktion zur Handhabung der LLM-Antwort zu definieren:

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

Wenn `tool_calls` vorhanden sind, werden die Werkzeuginformationen extrahiert, der MCP-Server mit der Werkzeuganfrage aufgerufen und die Ergebnisse zu den Konversationsnachrichten hinzugefügt. Danach wird der Dialog mit dem LLM fortgesetzt und die Nachrichten mit der Antwort des Assistenten und den Ergebnissen der Werkzeugaufrufe aktualisiert.

Um Werkzeugaufrufinformationen zu extrahieren, die das LLM für MCP-Anfragen zurückgibt, fügen wir eine weitere Hilfsfunktion hinzu, die alles Nötige zur Durchführung des Aufrufs extrahiert. Fügen Sie den folgenden Code am Ende Ihrer `main.rs` Datei hinzu:

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

Mit allen Teilen an Ort und Stelle können wir nun die anfängliche Benutzereingabe verarbeiten und das LLM aufrufen. Aktualisieren Sie Ihre `main` Funktion mit folgendem Code:

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

Dies fragt das LLM mit der initialen Benutzeraufforderung nach der Summe von zwei Zahlen und verarbeitet die Antwort, um Werkzeugaufrufe dynamisch zu handhaben.

Großartig, Sie haben es geschafft!

## Aufgabe

Nehmen Sie den Code aus der Übung und bauen Sie den Server mit weiteren Werkzeugen aus. Erstellen Sie danach einen Client mit einem LLM, wie in der Übung, und testen Sie ihn mit unterschiedlichen Eingaben, um sicherzustellen, dass alle Serverwerkzeuge dynamisch aufgerufen werden. Diese Art der Client-Erstellung sorgt für eine großartige Benutzererfahrung, da die Nutzer Eingaben in Form von Prompts nutzen können, anstatt genaue Client-Befehle eingeben zu müssen, und dabei nichts von einem MCP-Server-Aufruf mitbekommen.

## Lösung

[Lösung](./solution/README.md)

## Wichtige Erkenntnisse

- Die Integration eines LLM in Ihren Client ermöglicht den Benutzern eine bessere Interaktion mit MCP-Servern.
- Sie müssen die MCP-Server-Antwort in ein Format umwandeln, das das LLM versteht.

## Beispiele

- [Java Rechner](../samples/java/calculator/README.md)
- [.Net Rechner](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Rechner](../samples/javascript/README.md)
- [TypeScript Rechner](../samples/typescript/README.md)
- [Python Rechner](../../../../03-GettingStarted/samples/python)
- [Rust Rechner](../../../../03-GettingStarted/samples/rust)

## Zusätzliche Ressourcen

## Was kommt als Nächstes

- Nächstes: [Verwenden eines Servers mit Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Bei kritischen Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->