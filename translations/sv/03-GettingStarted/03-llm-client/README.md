# Skapa en klient med LLM

Hittills har du sett hur man skapar en server och en klient. Klienten har kunnat anropa servern explicit för att lista dess verktyg, resurser och prompts. Detta är dock inte en särskilt praktisk metod. Dina användare lever i den agentiska eran och förväntar sig att använda prompts och kommunicera med en LLM istället. De bryr sig inte om du använder MCP för att lagra dina kapaciteter; de förväntar sig helt enkelt att interagera med naturligt språk. Hur löser vi detta? Lösningen är att lägga till en LLM till klienten.

## Översikt

I denna lektion fokuserar vi på att lägga till en LLM till din klient och visar hur detta ger en mycket bättre användarupplevelse.

## Lärandemål

När denna lektion är slut kommer du att kunna:

- Skapa en klient med en LLM.
- Sömlöst interagera med en MCP-server med hjälp av en LLM.
- Ge en bättre slutanvändarupplevelse på klientsidan.

## Tillvägagångssätt

Låt oss försöka förstå tillvägagångssättet vi behöver ta. Att lägga till en LLM låter enkelt, men kommer vi verkligen göra det?

Så här kommer klienten att interagera med servern:

1. Etablera anslutning med servern.

1. Lista kapaciteter, prompts, resurser och verktyg, och spara deras schema.

1. Lägg till en LLM och skicka med de sparade kapaciteterna och deras schema i ett format som LLM förstår.

1. Hantera en användarprompt genom att skicka den till LLM tillsammans med verktygen som listats av klienten.

Bra, nu förstår vi hur vi kan göra detta på en hög nivå, låt oss prova detta i övningen nedan.

## Övning: Skapa en klient med en LLM

I denna övning kommer vi att lära oss att lägga till en LLM till vår klient.

### Autentisering med GitHub Personal Access Token

Att skapa en GitHub-token är en enkel process. Så här gör du:

- Gå till GitHub-inställningar – Klicka på din profilbild uppe till höger och välj Inställningar.
- Navigera till Utvecklarinställningar – Scrolla ner och klicka på Utvecklarinställningar.
- Välj Personliga åtkomsttoken – Klicka på Fine-grained tokens och sedan Generera ny token.
- Konfigurera din token – Lägg till en anteckning för referens, sätt ett utgångsdatum, och välj nödvändiga rättigheter (behörigheter). Se till att lägga till Models-behörigheten i det här fallet.
- Generera och kopiera token – Klicka på Generera token och se till att kopiera den omedelbart, eftersom du inte kommer kunna se den igen.

### -1- Anslut till server

Låt oss först skapa vår klient:

#### TypeScript

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importera zod för schema validering

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

I koden ovan har vi:

- Importerat de nödvändiga biblioteken
- Skapat en klass med två medlemmar, `client` och `openai` som hjälper oss att hantera en klient och interagera med en LLM respektive.
- Konfigurerat vår LLM-instans för att använda GitHub Models genom att sätta `baseUrl` till inferens-API:et.

#### Python

```python
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Skapa serverparametrar för stdio-anslutning
server_params = StdioServerParameters(
    command="mcp",  # Körbar fil
    args=["run", "server.py"],  # Valfria kommandoradsargument
    env=None,  # Valfria miljövariabler
)


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read, write
        ) as session:
            # Initiera anslutningen
            await session.initialize()


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())

```

I koden ovan har vi:

- Importerat de nödvändiga biblioteken för MCP
- Skapat en klient

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

Först behöver du lägga till LangChain4j-konfigurationerna i din `pom.xml`-fil. Lägg till dessa beroenden för att möjliggöra MCP-integration och OpenAI-kompatibel MiniMax-API:

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

Sätt din MiniMax API-nyckel och eventuellt slutpunkt och modell.
`MINIMAX_MODEL_ID` stöder `MiniMax-M3` och `MiniMax-M2.7`. Om
`OPENAI_BASE_URL` inte är satt, stöder `MINIMAX_REGION` `global_en` och `cn_zh`.

```bash
export OPENAI_API_KEY=your_minimax_api_key_here
export OPENAI_BASE_URL=https://api.minimax.io/v1
export MINIMAX_MODEL_ID=MiniMax-M3
```

För att istället välja slutpunkt efter region, utelämna `OPENAI_BASE_URL`:

```bash
unset OPENAI_BASE_URL
export MINIMAX_REGION=cn_zh
```

Skapa sedan din Java-klientklass:

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

        // Skapa MCP-transport för att ansluta till servern
        McpTransport transport = new HttpMcpTransport.Builder()
                .sseUrl("http://localhost:8080/sse")
                .timeout(Duration.ofSeconds(60))
                .logRequests(true)
                .logResponses(true)
                .build();

        // Skapa MCP-klient
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

I koden ovan har vi:

- **Lagt till LangChain4j-beroenden**: Krävs för MCP-integrering och OpenAI-kompatibel MiniMax-API
- **Importerat LangChain4j-biblioteken**: För MCP-integration och OpenAI chattmodellfunktionalitet
- **Skapat en `ChatLanguageModel`**: Konfigurerad att använda MiniMax med din MiniMax API-nyckel, slutpunkt och stödd modell-ID
- **Konfigurerat HTTP-transport**: Använder Server-Sent Events (SSE) för att ansluta till MCP-servern
- **Skapat en MCP-klient**: Som hanterar kommunikationen med servern
- **Använt LangChain4js inbyggda MCP-stöd**: Vilket förenklar integrationen mellan LLM och MCP-servrar

#### Rust

Detta exempel antar att du har en Rust-baserad MCP-server som körs. Om du inte har en, gå tillbaka till [01-first-server](../01-first-server/README.md)-lektionen för att skapa servern.

När du har din Rust MCP-server, öppna en terminal och navigera till samma katalog som servern. Kör sedan följande kommando för att skapa ett nytt LLM-klientprojekt:

```bash
mkdir calculator-llmclient
cd calculator-llmclient
cargo init
```

Lägg till följande beroenden i din `Cargo.toml`-fil:

```toml
[dependencies]
async-openai = { version = "0.29.0", features = ["byot"] }
rmcp = { version = "0.5.0", features = ["client", "transport-child-process"] }
serde_json = "1.0.141"
tokio = { version = "1.46.1", features = ["rt-multi-thread"] }
```

> [!NOTE]
> Det finns inget officiellt Rust-bibliotek för OpenAI, men `async-openai` crate är ett [community underhållet bibliotek](https://platform.openai.com/docs/libraries/rust#rust) som ofta används.

Öppna `src/main.rs`-filen och ersätt dess innehåll med följande kod:

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
    // Startmeddelande
    let mut messages = vec![json!({"role": "user", "content": "What is the sum of 3 and 2?"})];

    // Ställ in OpenAI-klient
    let api_key = std::env::var("OPENAI_API_KEY")?;
    let openai_client = Client::with_config(
        OpenAIConfig::new()
            .with_api_base("https://models.github.ai/inference/chat")
            .with_api_key(api_key),
    );

    // Ställ in MCP-klient
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

    // TODO: Hämta MCP-verktygslista

    // TODO: LLM-samtal med verktygsanrop

    Ok(())
}
```

Denna kod ställer in en grundläggande Rust-applikation som ansluter till en MCP-server och GitHub Models för LLM-interaktioner.

> [!IMPORTANT]
> Se till att sätta miljövariabeln `OPENAI_API_KEY` med din GitHub-token innan du kör applikationen.

Bra, för nästa steg, låt oss lista kapaciteterna på servern.

### -2- Lista servers kapaciteter

Nu ska vi ansluta till servern och fråga efter dess kapaciteter:

#### Typescript

Lägg till följande metoder i samma klass:

```typescript
async connectToServer(transport: Transport) {
     await this.client.connect(transport);
     this.run();
     console.error("MCPClient started on stdin/stdout");
}

async run() {
    console.log("Asking server for available tools");

    // listar verktyg
    const toolsResult = await this.client.listTools();
}
```

I koden ovan har vi:

- Lagt till kod för att ansluta till servern, `connectToServer`.
- Skapat en `run` metod som ansvarar för att hantera vår appflöde. Hittills listar den bara verktygen men vi kommer snart att lägga till mer.

#### Python

```python
# Lista tillgängliga resurser
resources = await session.list_resources()
print("LISTING RESOURCES")
for resource in resources:
    print("Resource: ", resource)

# Lista tillgängliga verktyg
tools = await session.list_tools()
print("LISTING TOOLS")
for tool in tools.tools:
    print("Tool: ", tool.name)
    print("Tool", tool.inputSchema["properties"])
```

Detta har vi lagt till:

- Listat resurser och verktyg och skrivit ut dem. För verktyg listar vi också `inputSchema` som vi använder senare.

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

I koden ovan har vi:

- Listat verktyg tillgängliga på MCP-servern
- För varje verktyg listat namn, beskrivning och dess schema. Det senare är något vi kommer använda för att anropa verktygen snart.

#### Java

```java
// Skapa en verktygsleverantör som automatiskt upptäcker MCP-verktyg
ToolProvider toolProvider = McpToolProvider.builder()
        .mcpClients(List.of(mcpClient))
        .build();

// MCP-verktygsleverantören hanterar automatiskt:
// - Listing av tillgängliga verktyg från MCP-servern
// - Konvertering av MCP-verktygsscheman till LangChain4j-format
// - Hantering av verktygsexekvering och svar
```

I koden ovan har vi:

- Skapat en `McpToolProvider` som automatiskt upptäcker och registrerar alla verktyg från MCP-servern
- Verktygsleverantören hanterar konverteringen mellan MCP-verktygsscheman och LangChain4js verktygsformat internt
- Detta tillvägagångssätt abstraherar bort den manuella verktygslistningen och konverteringsprocessen

#### Rust

Att hämta verktyg från MCP-servern görs med metoden `list_tools`. Lägg i din `main`-funktion, efter att MCP-klienten är konfigurerad, till följande kod:

```rust
// Hämta MCP-verktygslista
let tools = mcp_client.list_tools(Default::default()).await?;
```

### -3- Konvertera servers kapaciteter till LLM-verktyg

Nästa steg efter att ha listat serverns kapaciteter är att konvertera dem till ett format som LLM förstår. När vi gjort det kan vi förse LLM med dessa kapaciteter som verktyg.

#### TypeScript

1. Lägg till följande kod för att konvertera svar från MCP Server till ett verktygsformat som LLM kan använda:

    ```typescript
    openAiToolAdapter(tool: {
        name: string;
        description?: string;
        input_schema: any;
        }) {
        // Skapa ett zod-schema baserat på input_schema
        const schema = z.object(tool.input_schema);
    
        return {
            type: "function" as const, // Sätt uttryckligen typen till "funktion"
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

    Koden ovan tar ett svar från MCP Server och konverterar det till ett verktygsdefinitionsformat som LLM kan förstå.

2. Låt oss uppdatera `run`-metoden nästa steg för att lista serverns kapaciteter:

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

    I koden ovan har vi uppdaterat `run`-metoden att mappa genom resultatet och för varje post anropa `openAiToolAdapter`.

#### Python

1. Först, låt oss skapa följande konverteringsfunktion

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

    I funktionen ovan `convert_to_llm_tools` tar vi ett MCP-verktygssvar och konverterar det till ett format som LLM kan förstå.

2. Nästa steg, låt oss uppdatera vår klientkod för att använda denna funktion så här:

    ```python
    functions = []
    for tool in tools.tools:
        print("Tool: ", tool.name)
        print("Tool", tool.inputSchema["properties"])
        functions.append(convert_to_llm_tool(tool))
    ```

    Här lägger vi till ett anrop till `convert_to_llm_tool` för att konvertera MCP-verktygssvaret till något vi kan mata LLM med senare.

#### .NET

1. Låt oss lägga till kod för att konvertera MCP-verktygssvaret till något LLM kan förstå

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

I koden ovan har vi:

- Skapat en funktion `ConvertFrom` som tar namn, beskrivning och input-schema.
- Definierat funktionalitet som skapar en FunctionDefinition som skickas till en ChatCompletionsDefinition. Det senare är något LLM kan förstå.

2. Låt oss se hur vi kan uppdatera viss befintlig kod för att dra nytta av denna funktion:

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
// Skapa ett Bot-gränssnitt för naturlig språkintegration
public interface Bot {
    String chat(String prompt);
}

// Konfigurera AI-tjänsten med LLM- och MCP-verktyg
Bot bot = AiServices.builder(Bot.class)
        .chatLanguageModel(model)
        .toolProvider(toolProvider)
        .build();
```

I koden ovan har vi:

- Definierat ett enkelt `Bot`-gränssnitt för interaktioner med naturligt språk
- Använt LangChain4js `AiServices` för att automatiskt koppla LLM med MCP-verktygsleverantören
- Frameworket hanterar automatiskt verktygsschema-konvertering och funktionsanrop bakom kulisserna
- Detta tillvägagångssätt eliminerar manuell verktygskonvertering - LangChain4j hanterar all komplexitet med att konvertera MCP-verktyg till LLM-kompatibelt format

#### Rust

För att konvertera MCP-verktygssvaret till ett format som LLM kan förstå, kommer vi att lägga till en hjälpfunktion som formaterar verktygslistningen. Lägg till följande kod i din `main.rs` fil under `main` funktionen. Detta kommer att anropas när vi skickar förfrågningar till LLM:

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

Bra, vi är nu redo att hantera användarförfrågningar, så låt oss ta itu med det nästa.

### -4- Hantera användarpromptförfrågan

I denna del av koden kommer vi hantera användarförfrågningar.

#### TypeScript

1. Lägg till en metod som kommer användas för att anropa vår LLM:

    ```typescript
    async callTools(
        tool_calls: OpenAI.Chat.Completions.ChatCompletionMessageToolCall[],
        toolResults: any[]
    ) {
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);


        // 2. Anropa serverns verktyg
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gör något med resultatet
        // ATT GÖRA

        }
    }
    ```

    I koden ovan:

    - Lagt till en metod `callTools`.
    - Metoden tar ett LLM-svar och kontrollerar vilka verktyg som anropats, om några:

        ```typescript
        for (const tool_call of tool_calls) {
        const toolName = tool_call.function.name;
        const args = tool_call.function.arguments;

        console.log(`Calling tool ${toolName} with args ${JSON.stringify(args)}`);

        // anropa verktyg
        }
        ```

    - Anropar ett verktyg, om LLM indikerar att det ska anropas:

        ```typescript
        // 2. Anropa serverns verktyg
        const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
        });

        console.log("Tool result: ", toolResult);

        // 3. Gör något med resultatet
        // ATT GÖRA
        ```

2. Uppdatera `run`-metoden för att inkludera anrop till LLM och anrop av `callTools`:

    ```typescript

    // 1. Skapa meddelanden som är input för LLM
    const prompt = "What is the sum of 2 and 3?"

    const messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [
            {
                role: "user",
                content: prompt,
            },
        ];

    console.log("Querying LLM: ", messages[0].content);

    // 2. Anropar LLM
    let response = this.openai.chat.completions.create({
        model: "gpt-4.1-mini",
        max_tokens: 1000,
        messages,
        tools: tools,
    });    

    let results: any[] = [];

    // 3. Gå igenom LLM-svaret, för varje val, kontrollera om det har verktygsanrop
    (await response).choices.map(async (choice: { message: any; }) => {
        const message = choice.message;
        if (message.tool_calls) {
            console.log("Making tool call")
            await this.callTools(message.tool_calls, results);
        }
    });
    ```

Bra, låt oss visa koden i sin helhet:

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Transport } from "@modelcontextprotocol/sdk/shared/transport.js";
import OpenAI from "openai";
import { z } from "zod"; // Importera zod för schema validering

class MyClient {
    private openai: OpenAI;
    private client: Client;
    constructor(){
        this.openai = new OpenAI({
            baseURL: "https://models.inference.ai.azure.com", // kan behöva ändras till denna url i framtiden: https://models.github.ai/inference
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
          // Skapa ett zod-schema baserat på input_schema
          const schema = z.object(tool.input_schema);
      
          return {
            type: "function" as const, // Sätt explicit typ till "funktion"
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
    
    
          // 2. Anropa serverns verktyg
          const toolResult = await this.client.callTool({
            name: toolName,
            arguments: JSON.parse(args),
          });
    
          console.log("Tool result: ", toolResult);
    
          // 3. Gör något med resultatet
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
    
        // 3. Gå igenom LLM-svaret, för varje val, kontrollera om det finns verktygsanrop
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

1. Låt oss lägga till några importerar som behövs för att anropa en LLM

    ```python
    # llm
    import os
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    import json
    ```

2. Nästa steg, lägg till funktionen som anropar LLM:

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
            # Valfria parametrar
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

    I koden ovan har vi:

    - Skickat våra funktioner, som vi hittade på MCP-servern och konverterade, till LLM.
    - Därefter anropat LLM med dessa funktioner.
    - Sedan undersökt resultatet för att se vilka funktioner vi borde anropa, om några.
    - Slutligen skickat en lista av funktioner att anropa.

3. Sista steget, låt oss uppdatera vår huvudkod:

    ```python
    prompt = "Add 2 to 20"

    # fråga LLM vilka verktyg som ska användas, om några
    functions_to_call = call_llm(prompt, functions)

    # kalla på föreslagna funktioner
    for f in functions_to_call:
        result = await session.call_tool(f["name"], arguments=f["args"])
        print("TOOLS result: ", result.content)
    ```

    Där, det var sista steget, i koden ovan:

    - Anropar ett MCP-verktyg via `call_tool` med en funktion som LLM bedömde att vi borde anropa baserat på vår prompt.
    - Skriver ut resultatet från verktygsanropet till MCP-servern.

#### .NET

1. Låt oss visa kod för att göra en LLM-promptförfrågan:

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

    I koden ovan har vi:

    - Hämtat verktyg från MCP-servern, `var tools = await GetMcpTools()`.
    - Definierat en användarprompt `userMessage`.
    - Konstruerat ett optionsobjekt som specificerar modell och verktyg.
    - Skickat en förfrågan till LLM.

2. Ett sista steg, låt oss se om LLM anser att vi ska anropa en funktion:

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

    I koden ovan har vi:

    - Loopat genom en lista av funktionsanrop.
    - För varje verktygsanrop, tolkat ut namn och argument, och kallat verktyget på MCP-servern med MCP-klienten. Slutligen skriver vi ut resultaten.

Här är koden i sin helhet:

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
    // Utför naturliga språkförfrågningar som automatiskt använder MCP-verktyg
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

I koden ovan har vi:

- Använt enkla prompts med naturligt språk för att interagera med MCP-serverns verktyg
- LangChain4j-ramverket hanterar automatiskt:
  - Konvertering av användarprompter till verktygsanrop vid behov
  - Anrop av lämpliga MCP-verktyg baserat på LLMs beslut
  - Hantering av konversationsflödet mellan LLM och MCP-server
- Metoden `bot.chat()` returnerar svar i naturligt språk som kan inkludera resultat från MCP-verktygsexekveringar
- Detta tillvägagångssätt ger en sömlös användarupplevelse där användarna inte behöver känna till den underliggande MCP-implementeringen

Komplett kodexempel:

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

Här sker huvuddelen av arbetet. Vi kommer anropa LLM med den initiala användarprompten, sedan bearbeta svaret för att se om några verktyg behöver anropas. Om så är fallet, anropar vi dessa verktyg och fortsätter konversationen med LLM tills inga fler verktygsanrop behövs och vi har ett slutgiltigt svar.


Vi kommer att göra flera anrop till LLM, så låt oss definiera en funktion som hanterar LLM-anropet. Lägg till följande funktion i din `main.rs`-fil:

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

Den här funktionen tar LLM-klienten, en lista med meddelanden (inklusive användarens prompt), verktyg från MCP-servern och skickar en förfrågan till LLM, och returnerar svaret.

Svaret från LLM kommer att innehålla en array av `choices`. Vi behöver bearbeta resultatet för att se om några `tool_calls` finns. Detta berättar för oss att LLM begär att ett specifikt verktyg ska anropas med argument. Lägg till följande kod längst ner i din `main.rs`-fil för att definiera en funktion som hanterar LLM-svaret:

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

    // Skriv ut innehåll om tillgängligt
    if let Some(content) = message.get("content").and_then(|c| c.as_str()) {
        println!("🤖 {}", content);
    }

    // Hantera verktygsanrop
    if let Some(tool_calls) = message.get("tool_calls").and_then(|tc| tc.as_array()) {
        messages.push(message.clone()); // Lägg till assistentmeddelande

        // Utför varje verktygsanrop
        for tool_call in tool_calls {
            let (tool_id, name, args) = extract_tool_call_info(tool_call)?;
            println!("⚡ Calling tool: {}", name);

            let result = mcp_client
                .call_tool(CallToolRequestParam {
                    name: name.into(),
                    arguments: serde_json::from_str::<Value>(&args)?.as_object().cloned(),
                })
                .await?;

            // Lägg till verktygsresultat i meddelanden
            messages.push(json!({
                "role": "tool",
                "tool_call_id": tool_id,
                "content": serde_json::to_string_pretty(&result)?
            }));
        }

        // Fortsätt konversationen med verktygsresultat
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

Om `tool_calls` finns extraheras verktygsinformationen, MCP-servern anropas med verktygsförfrågan och resultaten läggs till i konversationsmeddelandena. Den fortsätter sedan konversationen med LLM och meddelandena uppdateras med assistentens svar och verktygsanropsresultat.

För att extrahera information om verktygsanrop som LLM returnerar för MCP-anrop, kommer vi att lägga till en hjälpfunktion till som extraherar allt som behövs för att göra anropet. Lägg till följande kod längst ner i din `main.rs`-fil:

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

Med alla delar på plats kan vi nu hantera den initiala användarprompten och anropa LLM. Uppdatera din `main`-funktion för att inkludera följande kod:

```rust
// LLM-samtal med verktygsanrop
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

Detta kommer att fråga LLM med den initiala användarprompten som ber om summan av två tal, och den kommer att bearbeta svaret för att dynamiskt hantera verktygsanrop.

Bra jobbat, du klarade det!

## Uppgift

Ta koden från övningen och bygg ut servern med fler verktyg. Skapa sedan en klient med en LLM, som i övningen, och testa med olika prompts för att säkerställa att alla dina serververktyg anropas dynamiskt. På detta sätt ger klienten en fantastisk användarupplevelse eftersom användaren kan använda prompts istället för exakta klientkommandon och vara omedveten om att någon MCP-server anropas.

## Lösning

[Lösning](./solution/README.md)

## Viktiga insikter

- Att lägga till en LLM till din klient ger ett bättre sätt för användare att interagera med MCP-servrar.
- Du måste konvertera MCP-serverns svar till något som LLM kan förstå.

## Exempel

- [Java Calculator](../samples/java/calculator/README.md)
- [.Net Calculator](../../../../03-GettingStarted/samples/csharp)
- [JavaScript Calculator](../samples/javascript/README.md)
- [TypeScript Calculator](../samples/typescript/README.md)
- [Python Calculator](../../../../03-GettingStarted/samples/python)
- [Rust Calculator](../../../../03-GettingStarted/samples/rust)

## Ytterligare resurser

## Vad blir nästa steg

- Nästa: [Att använda en server med Visual Studio Code](../04-vscode/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->